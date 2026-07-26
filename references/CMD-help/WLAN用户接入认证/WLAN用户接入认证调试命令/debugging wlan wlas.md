::: {#-1207344884 .myid}
[]{#struct_0_x4197_x8870_x678085957}[]{#_Toc404794990}[]{#_Ref385402523}

**WLAN用户接入认证 \-- WLAN用户接入认证调试命令 \-- debugging wlan wlas**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_30695272}

[**[debugging]{lang="EN-US"}**[ **wlan** **wlas** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } }]{lang="EN-US"}]{#struct_0_x4197_x8870_x1599900657}

[**[undo]{lang="EN-US"}**[ **debugging** **wlan** **wlas** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } }]{lang="EN-US"}]{#struct_0_x4197_x8870_1219437258}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_1619228983}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4197_x8870_2066786870}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_1863664207}

[[network-admin]{lang="EN-US"}]{#struct_0_x4197_x8870_2087003638}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4197_x8870_733615111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x449023848}

[**[all]{lang="EN-US"}**]{#struct_0_x4197_x8870_x413492277}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[所有类型的调试开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x4197_x8870_x39196308}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[错误类型的调试开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x4197_x8870_x146290495}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[事件类型的调试开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_x4197_x8870_224661667}[：表示]{style="font-family:宋体"}[WWLAS]{lang="EN-US"}[状态加类型调试开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_x4197_x8870_1503099896}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[定时器类型调试开关。]{style="font-family:宋体"}

[**[packet receive]{lang="EN-US"}**]{#struct_0_x4197_x8870_1545157973}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[接收报文的调试开关。]{style="font-family:宋体"}

[**[packet send]{lang="EN-US"}**]{#struct_0_x4197_x8870_x615973708}[：表示]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[发送报文的调试开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_871920944}

[**[debugging wlan wlas]{lang="EN-US"}**]{#struct_0_x4197_x8870_x834515152}[命令用来打开]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}**[undo debugging wlan wlas]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[WLAS]{lang="EN-US"}]{#struct_0_x4197_x8870_x1202152590}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging wlan wlas error]{lang="EN-US"}]{#struct_0_x4197_x8870_x1868579983}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x93540744}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x92650922}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x563144022}

[[Failed to allocate memory for EAP-Request/Identity.]{lang="EN-US"}]{#struct_0_x4197_x8870_1498215214}

[[EAP]{lang="EN-US"}]{#struct_0_x4197_x8870_x653674817}[的认证请求报文申请内存空间失败]{style="font-family:宋体"}

[[Failed to allocate memory for EAP-Success.]{lang="EN-US"}]{#struct_0_x4197_x8870_1268326495}

[[Success]{lang="EN-US"}]{#struct_0_x4197_x8870_x1700458614}[报文申请内存空间失败]{style="font-family:宋体"}

[[Failed to allocate memory for EAP-Failure.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1316995409}

[[Failure]{lang="EN-US"}]{#struct_0_x4197_x8870_x1501889708}[报文申请内存空间失败]{style="font-family:宋体"}

[[Failed to allocate memory for EAP-Request/Challenge.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1626840350}

[[EAP]{lang="EN-US"}]{#struct_0_x4197_x8870_1398794976}[认证的]{style="font-family:宋体"}[challenge request]{lang="EN-US"}[报文申请内存空间失败]{style="font-family:宋体"}

[[Failed to allocate memory for EAP-Request/PAP.]{lang="EN-US"}]{#struct_0_x4197_x8870_1943349951}

[[构造]{style="font-family:宋体"}[PAP]{lang="EN-US"}]{#struct_0_x4197_x8870_x562012823}[报文时，申请内存空间失败]{style="font-family:宋体"}

[[Failed to process EAP packet: invalid password length.]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650921}

[[非法密码长度导致处理]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144019}[报文失败]{style="font-family:宋体"}

[[Sent a packet with unknown EAP code *Code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1497887531}

[[使用未知的]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_x4197_x8870_x78459839}[报文类型]{style="font-family:宋体"}*[Code]{lang="EN-US"}*[发送报文]{style="font-family:宋体"}

[[\[BSSID: *BSSID* \] Failed to create the temporary service stop timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x776560647}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1204290147}[为]{style="font-family:宋体"} *[BSSID  ]{lang="EN-US"}*[，开启临时关闭服务定时器失败]{style="font-family:宋体"}

[[\[MAC: User*MAC*; BSSID: *BSSID*\] Failed to create the re-authentication timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2128075728}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x814318782}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启重认证定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the held timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_578254620}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650924}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启]{style="font-family:宋体"}[held]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the server response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144016}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1498477355}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启服务器回应定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the client response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_526568639}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1296039719}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启客户端回应定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to match the hash information. ]{lang="EN-US"}]{#struct_0_x4197_x8870_80756537}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1929274708}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，匹配哈希信息失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the handshake timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x195730791}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1066195375}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启握手定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Invalid server string length *length*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650923}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144021}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[ server string]{lang="EN-US"}[长度非法]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to fill the EAPOL packet with EAP messages.]{lang="EN-US"}]{#struct_0_x4197_x8870_1498411822}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1067719792}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，填充]{style="font-family:宋体"}[EAPOL]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the Block MAC timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1266243797}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1953254954}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启]{style="font-family:宋体"}[Block MAC]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the accounting-update timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1509307818}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650926}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启用户计费更新定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the session timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144018}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1497821995}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启会话超时定时器失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Failed to create the Fail VLAN client timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1896127260}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x871510741}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启]{style="font-family:宋体"}[Fail VLAN]{lang="EN-US"}[用户定时器失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging wlan wlas event]{lang="EN-US"}]{#struct_0_x4197_x8870_1071768337}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x69402602}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x1630171183}

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x82239374}

[[Got secure handshake hash info from the EAP message.]{lang="EN-US"}]{#struct_0_x4197_x8870_1511087820}

[[从]{style="font-family:宋体"}[EAP]{lang="EN-US"}]{#struct_0_x4197_x8870_x2071758399}[消息中成功获取到安全握手的]{style="font-family:宋体"}[HASH]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Decoded old IPv4 address *address*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1238779870}

[[成功解析]{style="font-family:宋体"}[old  IPv4]{lang="EN-US"}]{#struct_0_x4197_x8870_885212414}[地址信息]{style="font-family:宋体"}

[[Decoded new IPv4 address *address*.]{lang="EN-US"}]{#struct_0_x4197_x8870_968977489}

[[成功解析]{style="font-family:宋体"}[new IPv4]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650925}[地址信息]{style="font-family:宋体"}

[[Decoded IPv6 address *address*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144015}

[[成功解析]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x4197_x8870_1498673963}[地址信息]{style="font-family:宋体"}

[[Received unknown IP address type.]{lang="EN-US"}]{#struct_0_x4197_x8870_112261780}

[[获取到未知类型的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4197_x8870_x738345213}[地址信息]{style="font-family:宋体"}

[[Decoded username *username*.]{lang="EN-US"}]{#struct_0_x4197_x8870_89299785}

[[成功解析用户名]{style="font-family:宋体"}*[username]{lang="EN-US"}*]{#struct_0_x4197_x8870_x1783248437}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Got secure handshake hash info from the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_1087823164}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1475477035}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功获取从服务器下发的安全握手]{style="font-family:宋体"}[HASH]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authentication request to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650928}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144012}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向服务器发送认证请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authentication request to the home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_377097486}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_51510755}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[发送认证请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authorization request to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_1498215211}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x653871425}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向服务器发送授权请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authorization request to the home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1995489973}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1076268723}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送授权请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1136034189}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_413918843}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned continue.]{lang="EN-US"}]{#struct_0_x4197_x8870_2022941840}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650927}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回]{style="font-family:宋体"}[contiue]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144017}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1498542891}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回]{style="font-family:宋体"}[processing]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned failure.]{lang="EN-US"}]{#struct_0_x4197_x8870_508849885}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_270058013}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回失败]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned max tries.]{lang="EN-US"}]{#struct_0_x4197_x8870_1169364874}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650930}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回已到达认证最大次数]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authentication request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1775508140}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2101768313}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authorization request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_146347121}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1723779042}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authorization request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1640936211}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92650929}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回]{style="font-family:宋体"}[processing]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed authorization request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x563144011}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1498411819}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent the server string notification packet.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1068309619}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1481364189}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功发送]{style="font-family:宋体"}[ server string notification]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received an async authentication response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_470006744}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966058}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，用户收到异步认证回应，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received an async authorization response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x33205275}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x781071648}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，用户收到异步授权回应，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received an async accounting-start response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_188594332}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x866909778}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，用户收到异步计费开始回应，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received an async accounting-update response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966057}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1983217360}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，用户收到异步计费更新回应，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received an async accounting-stop response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_223991175}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1362989745}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，用户收到异步计费终止回应，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-start request to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1460133268}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966060}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向服务器发送实时计费开始请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-start request to the home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x429406032}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x90761181}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送实时计费开始请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-update request to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x389632243}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1244374022}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向服务器发送实时计费更新请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-update request to the home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_330108855}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1413464123}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送实时计费更新请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-stop request to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_676324056}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1730557450}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向服务器发送实时计费停止请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-stop request to the home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1235975086}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1680732083}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送实时计费停止请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-stop request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x536103263}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966059}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费停止请求，返回]{style="font-family:宋体"}[processing]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-stop request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1532878666}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_229357808}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[ AAA]{lang="EN-US"}[处理实时计费停止请求，返回失败，编号为]{style="font-family:宋体"}*[Code]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-start request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x434722961}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1600992278}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费开始请求，返回]{style="font-family:宋体"}[processing]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-start request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966062}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1552431657}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费开始请求，返回]{style="font-family:宋体"}[sucess]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-start request and returned max tries.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1697810535}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x362046529}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费开始请求，返回已达到认证最大次数]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-start request and returned failure code *Code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x701572092}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1579349997}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费开始请求，返回失败，编号为]{style="font-family:宋体"}*[Code]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-update request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966061}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1176451698}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费更新请求，返回]{style="font-family:宋体"}[processing]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-update request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1091256337}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_736774791}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费更新请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA processed accounting-update request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_960915903}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966064}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理实时计费更新请求，返回失败，编号为]{style="font-family:宋体"}*[Code]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the roam-in client.]{lang="EN-US"}]{#struct_0_x4197_x8870_1579736225}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1175121989}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除漫入用户]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the inter-AC roam-in client.]{lang="EN-US"}]{#struct_0_x4197_x8870_1896192796}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1632014511}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除]{style="font-family:宋体"}[AC]{lang="EN-US"}[间漫游的漫入用户]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an authentication-success msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1943246963}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1454278776}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的认证成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received a continue-authentication msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_377163022}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_430255304}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的认证]{style="font-family:宋体"}[continue]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an authentication-failure msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1594147509}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1396293156}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的认证失败信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an uthorization-success msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1134735846}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1488794185}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的授权成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an accounting-start success msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1538020373}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x951773919}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的开始计费成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an accounting-start failure msg from home AC because of server unreachable.]{lang="EN-US"}]{#struct_0_x4197_x8870_x28063568}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1481870395}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的开始计费不可达信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an accounting-update success msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_731451319}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x616788684}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的更新计费成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC received an accounting-update failure msg from home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x834632622}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1240740855}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的更新计费失败信息]{style="font-family:宋体"}

[]{#struct_0_x4197_x8870_x431348095}[]{#OLE_LINK2}[[\[MAC: *UserMAC*; BSSID: *BSSID*\]]{lang="EN-US"}]{#OLE_LINK1}[ Foreign AC received a message from home AC for changed session control authorization info.]{lang="EN-US"}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1339787027}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[收到从]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送来的]{style="font-family:宋体"}[session control ]{lang="EN-US"}[授权变化信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC sent an authentication request to home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997432036}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x70528898}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送认证请求信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC sent an accounting-update request to home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950377869}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x607387437}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送计费更新请求信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Foreign AC sent a cut-off request to home AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_778505486}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x822333351}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Foreign AC]{lang="EN-US"}[向]{style="font-family:宋体"}[home AC]{lang="EN-US"}[发送]{style="font-family:宋体"}[cut off]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the roam-back client.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1594081973}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2098116098}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除漫回用户信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an async authentication response:]{lang="EN-US"}]{#struct_0_x4197_x8870_1134801382}

[[ RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_29269888}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1538085909}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到异步认证回应]{style="font-family:宋体"} [，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authentication request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_171822611}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x27998032}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authentication request and returned continue.]{lang="EN-US"}]{#struct_0_x4197_x8870_x22543646}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_731516855}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回]{style="font-family:宋体"}[continue ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authentication request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_508989525}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x834567086}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回]{style="font-family:宋体"}[processing ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authentication request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1899463851}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x431282559}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理认证请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[ ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an async authorization response:]{lang="EN-US"}]{#struct_0_x4197_x8870_x990000350}

[[ RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997366500}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950312333}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到异步授权回应]{style="font-family:宋体"} [，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authorization request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x17828296}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_778571022}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authorization request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1227596504}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1594016437}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回]{style="font-family:宋体"}[processing ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an authorization request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1134866918}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_443624156}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理授权请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[ ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an async accounting-start response:               RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1538151445}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2108710812}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到异步开始计费回应]{style="font-family:宋体"} [，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-start request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x27932496}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_731582391}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理开始计费请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-start request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1746628907}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x834501550}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理开始计费请求，返回]{style="font-family:宋体"}[processing ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-start request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1881632222}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x431217023}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理开始计费请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[ ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an async accounting-update response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1376158750}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997300964}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到异步计费更新回应]{style="font-family:宋体"} [，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-update request and returned success.]{lang="EN-US"}]{#struct_0_x4197_x8870_x857975914}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950246797}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理计费更新请求，返回成功]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-update request and returned processing.]{lang="EN-US"}]{#struct_0_x4197_x8870_1334614705}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_778636558}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理计费更新请求，返回]{style="font-family:宋体"}[processing ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] AAA of the home AC processed an accounting-update request and returned failure code *code*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1593950901}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1845670272}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[处理计费更新请求，返回失败，编号为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[ ]{lang="EN-US"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an async accounting-stop response: RespCode=*RespCode*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1134932454}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1567294161}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到异步终止计费回应]{style="font-family:宋体"} [，回应的状态编号为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received disconnection session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_1538216981}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x213832674}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到断开]{style="font-family:宋体"}[session control ]{lang="EN-US"}[连接事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received authorization change session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_x27866960}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1225582926}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到]{style="font-family:宋体"}[session control ]{lang="EN-US"}[授权信息变化事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received unknown session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_731647927}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x781968655}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到未知]{style="font-family:宋体"}[ session control ]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an authentication request from foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x834436014}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x431151487}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发来的认证请求信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received an accounting-update request from foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1782672749}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997235428}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发来的计费更新请求信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC received a cut-off request from foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x639155604}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950181261}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[收到]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发来的]{style="font-family:宋体"}[cut off]{lang="EN-US"}[请求信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an authentication-success msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x76880612}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_778702094}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送认证成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent a continue-authentication msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1593885365}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1908475195}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送认证]{style="font-family:宋体"}[continue]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an authentication-failure msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1134997990}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1990899244}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送认证失败信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an authorization-success msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_1538282517}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x199754093}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送授权成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an accounting-start success msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x27801424}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_731713463}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送计费开始成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an accounting-start failure msg to foreign AC because of server unreachable.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1132675601}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x834370478}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送计费开始不可达信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an accounting-update success msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2028150215}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x431085951}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送计费更新成功信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent an accounting-update failure msg to foreign AC.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997169892}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x19100723}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送计费更新失败信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Home AC sent a message to foreign AC for changed session control authorization info.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950115725}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1318515458}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向]{style="font-family:宋体"}[foreign AC]{lang="EN-US"}[发送]{style="font-family:宋体"}[session control ]{lang="EN-US"}[授权信息改变信息]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Username of the inter-roam user changed.]{lang="EN-US"}]{#struct_0_x4197_x8870_778767630}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1593819829}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[AC]{lang="EN-US"}[间漫游用户的用户名发生改变]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authentication request from the home AC to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_597412243}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1135063526}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向服务器发送认证请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an authorization request from the home AC to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1558017608}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1538348053}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向服务器发送授权请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-start request from the home AC to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x27735888}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1775346354}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向服务器发送开始计费请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-update request from the home AC to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_731778999}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1209066736}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向服务器发送计费更新请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Sent an accounting-stop request from the home AC to the server.]{lang="EN-US"}]{#struct_0_x4197_x8870_x834304942}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x431020415}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[home  AC]{lang="EN-US"}[向服务器发送计费终止请求]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received disconnection session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1997104356}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1489474982}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，收到断开]{style="font-family:宋体"}[session control ]{lang="EN-US"}[连接事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received authorization change session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1950050189}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x218885936}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，收到]{style="font-family:宋体"}[session control ]{lang="EN-US"}[授权信息变化事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received unknown session control event.]{lang="EN-US"}]{#struct_0_x4197_x8870_778833166}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1728037557}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，收到未知]{style="font-family:宋体"}[ session control ]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received authorization information: VLAN ID *vlan-id*, ACL number *acl-number*, user profile *userprofile-name*.]{lang="EN-US"}]{#struct_0_x4197_x8870_1012704441}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1000845798}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，收到授权信息，包括]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[信息]{style="font-family:宋体"} *[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[信息]{style="font-family:宋体"} *[acl-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[UserPorfile ]{lang="EN-US"}[信息]{style="font-family:宋体"}*[userprofile-name]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] No authorization information was received.]{lang="EN-US"}]{#struct_0_x4197_x8870_1404130325}

[[未收到授权信息]{style="font-family:宋体"}]{#struct_0_x4197_x8870_1654399945}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Received session control event *event*.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1276723131}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966063}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，收到]{style="font-family:宋体"}[ Session Control ]{lang="EN-US"}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Started 802.1X authentication.]{lang="EN-US"}]{#struct_0_x4197_x8870_13652284}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x77684935}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开始进行]{style="font-family:宋体"}[802.1x]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Started MAC authentication.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966066}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_416936811}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开始]{style="font-family:宋体"}[ MAC]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Started OUI authentication.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2119132719}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_500491930}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，进行]{style="font-family:宋体"}[OUI]{lang="EN-US"}[模式认证]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Started Bypass authentication.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2048966065}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1149147130}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，进行]{style="font-family:宋体"}[BYPASS]{lang="EN-US"}[模式认证]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the client  that was being authenticated.]{lang="EN-US"}]{#struct_0_x4197_x8870_x778909824}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x881071758}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除正在认证的用户]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the client that has been authenticated.]{lang="EN-US"}]{#struct_0_x4197_x8870_289686102}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1872811659}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除已认证的用户]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Removed the roam-out client.]{lang="EN-US"}]{#struct_0_x4197_x8870_1865465703}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_289686103}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除漫出用户]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Checked client secure handshake hash.]{lang="EN-US"}]{#struct_0_x4197_x8870_1872811660}

[[Client hash                 : *hashvalue1*]{lang="EN-US"}]{#struct_0_x4197_x8870_1864875882}

[[Current server hash   : *hashvalue2*]{lang="EN-US"}]{#struct_0_x4197_x8870_289686100}

[[Previous server hash: *hashvalue3*]{lang="EN-US"}]{#struct_0_x4197_x8870_1872811657}

[[Previous server hash used times: *times1*]{lang="EN-US"}]{#struct_0_x4197_x8870_1864810343}

[[Hash mismatches: *times2*]{lang="EN-US"}]{#struct_0_x4197_x8870_289686101}

[[校验客户端安全握手]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_x4197_x8870_1872811658}[，客户端]{style="font-family:宋体"}[hash]{lang="EN-US"}[值为]{style="font-family:宋体"}*[hashvalue1]{lang="EN-US"}*[，服务器当前下发的]{style="font-family:宋体"}[hash]{lang="EN-US"}[值为]{style="font-family:宋体"}*[hashvalue2]{lang="EN-US"}*[，服务器上一次下发的]{style="font-family:宋体"}[hash]{lang="EN-US"}[值为]{style="font-family:宋体"}*[hashvalue3]{lang="EN-US"}*[，旧]{style="font-family:宋体"}[hash]{lang="EN-US"}[值使用的次数]{style="font-family:宋体"}*[times1]{lang="EN-US"}*[，]{style="font-family:宋体"}[hash]{lang="EN-US"}[值不匹配的次数]{style="font-family:宋体"}*[times2]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging wlan wlas fsm]{lang="EN-US"}]{#struct_0_x4197_x8870_1865400167}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x76664720}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x1915989178}

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_839486136}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] BE state machine entered *State* state.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1570570587}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1382108524}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[BE]{lang="EN-US"}[状态机进入]{style="font-family:宋体"}*[State]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] PAE state machine entered *State* state.]{lang="EN-US"}]{#struct_0_x4197_x8870_289686098}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031788}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[PAE]{lang="EN-US"}[状态机进入]{style="font-family:宋体"}*[State]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] MAC-authentication state machine entered *State* state.]{lang="EN-US"}]{#struct_0_x4197_x8870_2106298498}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1145879560}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[认证状态机进入]{style="font-family:宋体"}*[State]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging wlan wlas timer]{lang="EN-US"}]{#struct_0_x4197_x8870_1500142663}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x83681472}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_953039514}

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_1537469506}

[[\[BSSID: *BSSID*\] Temporary service stop timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_400114899}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_289686099}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，临时关闭服务定时器超时]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] Deleted the temporary service stop timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031789}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_2106232962}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}[，]{style="font-family:宋体"}*[删除临时关闭服务定时器]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] Created the temporary service stop timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x307548693}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x92563932}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}[，]{style="font-family:宋体"}*[成功开启临时关闭服务定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Held timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_1911560971}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2044066691}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[ Held]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Re-authentication timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_1195063796}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_289686096}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，重认证定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Server response timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031786}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_2106953858}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，服务器定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Client response timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_70361472}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1662428872}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，客户端定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the re-authentication  timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_860728942}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1381279963}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启重认证定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the held timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_289686097}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031787}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启]{style="font-family:宋体"}[Held]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the held timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_2106888322}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1187071173}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"} [删除]{style="font-family:宋体"}[Held]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the re-authentication timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1680635964}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_289686094}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除重认证定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the server response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031784}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_2107084930}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，开启服务器超时定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the server response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1963857448}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_537828541}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除服务器超时定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the client response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x227966443}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1315170173}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启客户端超时定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the client response timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_289686095}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1116031785}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除客户端超时定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Handshake timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_2107019394}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1190146261}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，握手定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the handshake timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x420134458}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_85601894}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启握手定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the handshake timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629034}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x766870244}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除握手定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Accounting-update timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_x862248509}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_581401546}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，更新计费定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the accounting-update timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2138746384}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1602656779}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启用户更新计费定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the accounting-update timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1875571496}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629033}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除计费更新定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Refreshed the accounting-update timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1170154771}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_366661166}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，更新实时计费时间]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Session timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1437351892}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629036}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，会话定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the session timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1929669658}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x2101131357}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启会话超时定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Refreshed the session timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1338780180}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x448523086}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，更新]{style="font-family:宋体"}[Session]{lang="EN-US"}[定时器时间]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the session timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_1567464604}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629035}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除会话定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Block MAC timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_1962013111}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1098363292}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Block MAC]{lang="EN-US"}[定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the Block MAC timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629038}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1202498224}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除]{style="font-family:宋体"}[Block MAC]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the Block MAC timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_299092032}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1267223265}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启]{style="font-family:宋体"}[Block MAC]{lang="EN-US"}[定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Fail VLAN client timer expired.]{lang="EN-US"}]{#struct_0_x4197_x8870_x2084267917}

[[ BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_1452375635}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，]{style="font-family:宋体"}[Fail VLAN]{lang="EN-US"}[用户定时器超时]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Deleted the Fail VLAN client timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x963060176}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_644615438}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，删除]{style="font-family:宋体"}[Fail VLAN]{lang="EN-US"}[用户定时器]{style="font-family:宋体"}

[[\[MAC: *UserMAC*; BSSID: *BSSID*\] Created the Fail VLAN client timer.]{lang="EN-US"}]{#struct_0_x4197_x8870_x189181044}

[[BSSID]{lang="EN-US"}]{#struct_0_x4197_x8870_x1893680898}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[UserMAC]{lang="EN-US"}*[，成功开启]{style="font-family:宋体"}[Fail VLAN]{lang="EN-US"}[用户定时器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging wlan wlas packet receive]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629037}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x57470518}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_799213697}

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_1548625981}

[[\[MAC: *userMAC*, BSSID:*BSSID* \] ]{lang="EN-US"}]{#struct_0_x4197_x8870_x223222326}

[[\-\-\-\--Packet HEAD\-\-\-\--]{lang="EN-US"}]{#struct_0_x4197_x8870_x1472468502}

[[Mac Frame Type: *PAEType*]{lang="EN-US"}]{#struct_0_x4197_x8870_x1627788985}

[[Protocol Version ID: *VersionID*]{lang="EN-US"}]{#struct_0_x4197_x8870_x527570726}

[[Packet Type: *PacketType*]{lang="EN-US"}]{#struct_0_x4197_x8870_1080361274}

[[Packet Length: *Length*]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629040}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x4197_x8870_1558794120}[地址为]{style="font-family:宋体"}*[UserMac]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，接收到]{style="font-family:宋体"}[EAPOL]{lang="EN-US"}[报文，报文的协议类型为]{style="font-family:宋体"}*[PAEType]{lang="EN-US"}*[，报文协议版本]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[VersionID]{lang="EN-US"}*[，报文的数据帧类型为]{style="font-family:宋体"}*[PacketType]{lang="EN-US"}*[，报文的长度为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging wlan wlas packet send]{lang="EN-US"}]{#struct_0_x4197_x8870_1091523137}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x56679032}[[字段]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x2137589192}

[[描述]{style="font-family:黑体"}]{#struct_0_x4197_x8870_x980812300}

[[\[MAC: *userMAC*, BSSID:*BSSID* \] ]{lang="EN-US"}]{#struct_0_x4197_x8870_x1204986824}

[[\-\-\-\--Packet HEAD\-\-\-\--]{lang="EN-US"}]{#struct_0_x4197_x8870_512105149}

[[Mac Frame Type: *MacType*]{lang="EN-US"}]{#struct_0_x4197_x8870_1696700286}

[[Protocol Version ID: *VersionID*]{lang="EN-US"}]{#struct_0_x4197_x8870_x224896941}

[[Packet Type: *PacketType*]{lang="EN-US"}]{#struct_0_x4197_x8870_x807724894}

[[Packet Length: *Length*]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629039}

[[\-\-\-\--Packet Body\-\-\-\--]{lang="EN-US"}]{#struct_0_x4197_x8870_x363585717}

[[Code: *Code*]{lang="EN-US"}]{#struct_0_x4197_x8870_x1906808787}

[[Identifier: *Identifier* ]{lang="EN-US"}]{#struct_0_x4197_x8870_x1635328238}

[[Length: *Length*]{lang="EN-US"}]{#struct_0_x4197_x8870_x1781779022}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x4197_x8870_1483044682}[地址为]{style="font-family:宋体"}*[UserMac]{lang="EN-US"}*[，]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[为]{style="font-family:宋体"}*[BSSID]{lang="EN-US"}*[，发送]{style="font-family:宋体"}[EAPOL]{lang="EN-US"}[报文，报文的协议类型为]{style="font-family:宋体"}*[PAEType]{lang="EN-US"}*[，报文的协议版本]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[VersionID]{lang="EN-US"}*[，报文的数据帧类型为]{style="font-family:宋体"}*[PacketType]{lang="EN-US"}*[，报文的长度为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*[，]{style="font-family:宋体"}[Packet Body]{lang="EN-US"}[字段的内容是一个]{style="font-family:宋体"}[EAP]{lang="EN-US"}[报文，]{style="font-family:宋体"}[EAP]{lang="EN-US"}[报文的类型为]{style="font-family:宋体"}*[Code]{lang="EN-US"}*[，标示符为]{style="font-family:宋体"}*[Identifier]{lang="EN-US"}*[，长度为]{style="font-family:宋体"}*[Length]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4197_x8870_1196575190}

[[\# ]{lang="EN-US"}]{#struct_0_x4197_x8870_x1666629042}[在设备上配置]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[用户接入认证，打开]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[事件调试信息开关，打印如下调试信息：]{style="font-family:宋体"}

[[\<AC\> debugging wlan wlas event]{lang="EN-US"}]{#struct_0_x4197_x8870_395994706}

[\*May 12 16:39:27:253 2014 H3C STAMGR/7/Event: \[MAC:0023-8933-2098; BSSID:000f-e2]{lang="EN-US"}

[01-0701\]Sent an authentication request.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x4197_x8870_737143601}*[发送一个认证报文。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x4197_x8870_x473180610}[打开]{style="font-family:宋体"}[WLAS]{lang="EN-US"}[定时器调试开关，打印如下调试信息：]{style="font-family:宋体"}

[[\*May 12 16:39:24:437 2014 H3C STAMGR/7/Timer: \[MAC:0023-8933-2098; BSSID:000f-e2]{lang="EN-US"}]{#struct_0_x4197_x8870_1036583421}

[01-0701\]Created the client response timer.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x4197_x8870_460753169}*[创建一个客户端回应定时器。]{style="font-family:宋体"}*
