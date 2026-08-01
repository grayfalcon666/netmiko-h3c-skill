<!-- CMD-INDEX
  debugging wlan wlas                 | 用户视图             | L5
-->

**WLAN用户接入认证 \-- WLAN用户接入认证调试命令 \-- debugging wlan wlas**

------------------------------------------------------------------------

【命令】

**[debugging**[ **wlan** **wlas** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } }]]

**[undo**[ **debugging** **wlan** **wlas** { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } }]]

【视图】

用户视图

【缺省用户角色】

network-admin

mdc-admin

【参数】

**[all**]：表示WLAS所有类型的调试开关。

**[error**]：表示WLAS错误类型的调试开关。

**[event**]：表示WLAS事件类型的调试开关。

**[fsm**]：表示WWLAS状态加类型调试开关。

**[timer**]：表示WLAS定时器类型调试开关。

**[packet receive**]：表示WLAS接收报文的调试开关。

**[packet send**]：表示WLAS发送报文的调试开关。

【描述】

**[debugging wlan wlas**]命令用来打开WLAS调试开关。**undo debugging wlan wlas**命令用来关闭WLAS调试开关。

缺省情况下，WLAS调试信息开关处于关闭状态。

表1-1 debugging wlan wlas error命令输出信息描述表

字段

描述

Failed to allocate memory for EAP-Request/Identity.

EAP的认证请求报文申请内存空间失败

Failed to allocate memory for EAP-Success.

Success报文申请内存空间失败

Failed to allocate memory for EAP-Failure.

Failure报文申请内存空间失败

Failed to allocate memory for EAP-Request/Challenge.

EAP认证的challenge request报文申请内存空间失败

Failed to allocate memory for EAP-Request/PAP.

构造PAP报文时，申请内存空间失败

Failed to process EAP packet: invalid password length.

非法密码长度导致处理EAP报文失败

Sent a packet with unknown EAP code *Code*.

使用未知的EAP报文类型*Code*发送报文

BSSID: *BSSID*  Failed to create the temporary service stop timer.

BSSID为 *BSSID  *，开启临时关闭服务定时器失败

MAC: User*MAC*; BSSID: *BSSID* Failed to create the re-authentication timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启重认证定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the held timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启held定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the server response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启服务器回应定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the client response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启客户端回应定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to match the hash information.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，匹配哈希信息失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the handshake timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启握手定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Invalid server string length *length*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC* server string长度非法

MAC: *UserMAC*; BSSID: *BSSID* Failed to fill the EAPOL packet with EAP messages.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，填充EAPOL报文失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the Block MAC timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启Block MAC定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the accounting-update timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启用户计费更新定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the session timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启会话超时定时器失败

MAC: *UserMAC*; BSSID: *BSSID* Failed to create the Fail VLAN client timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启Fail VLAN用户定时器失败

表1-2 debugging wlan wlas event命令输出信息描述表

字段

描述

Got secure handshake hash info from the EAP message.

从EAP消息中成功获取到安全握手的HASH信息

Decoded old IPv4 address *address*.

成功解析old  IPv4地址信息

Decoded new IPv4 address *address*.

成功解析new IPv4地址信息

Decoded IPv6 address *address*.

成功解析IPv6地址信息

Received unknown IP address type.

获取到未知类型的IP地址信息

Decoded username *username*.

成功解析用户名*username*

MAC: *UserMAC*; BSSID: *BSSID* Got secure handshake hash info from the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功获取从服务器下发的安全握手HASH信息

MAC: *UserMAC*; BSSID: *BSSID* Sent an authentication request to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向服务器发送认证请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an authentication request to the home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC发送认证请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an authorization request to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向服务器发送授权请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an authorization request to the home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向home AC发送授权请求

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned continue.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回contiue

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned failure.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回失败

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned max tries.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回已到达认证最大次数

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authentication request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理认证请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authorization request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理授权请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authorization request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理授权请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA processed authorization request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理授权请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* Sent the server string notification packet.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功发送 server string notification报文

MAC: *UserMAC*; BSSID: *BSSID* Received an async authentication response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，用户收到异步认证回应，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Received an async authorization response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，用户收到异步授权回应，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Received an async accounting-start response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，用户收到异步计费开始回应，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Received an async accounting-update response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，用户收到异步计费更新回应，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Received an async accounting-stop response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，用户收到异步计费终止回应，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-start request to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向服务器发送实时计费开始请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-start request to the home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向home AC发送实时计费开始请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-update request to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向服务器发送实时计费更新请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-update request to the home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向home AC发送实时计费更新请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-stop request to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向服务器发送实时计费停止请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-stop request to the home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，向home AC发送实时计费停止请求

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-stop request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费停止请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-stop request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*， AAA处理实时计费停止请求，返回失败，编号为*Code*

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-start request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费开始请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-start request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费开始请求，返回sucess

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-start request and returned max tries.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费开始请求，返回已达到认证最大次数

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-start request and returned failure code *Code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费开始请求，返回失败，编号为*Code*

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-update request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费更新请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-update request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费更新请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA processed accounting-update request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AAA处理实时计费更新请求，返回失败，编号为*Code*

MAC: *UserMAC*; BSSID: *BSSID* Removed the roam-in client.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除漫入用户

MAC: *UserMAC*; BSSID: *BSSID* Removed the inter-AC roam-in client.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除AC间漫游的漫入用户

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an authentication-success msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的认证成功信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received a continue-authentication msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的认证continue信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an authentication-failure msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的认证失败信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an uthorization-success msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的授权成功信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an accounting-start success msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的开始计费成功信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an accounting-start failure msg from home AC because of server unreachable.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的开始计费不可达信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an accounting-update success msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的更新计费成功信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received an accounting-update failure msg from home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的更新计费失败信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC received a message from home AC for changed session control authorization info.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC收到从home AC发送来的session control 授权变化信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC sent an authentication request to home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC向home AC发送认证请求信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC sent an accounting-update request to home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC向home AC发送计费更新请求信息

MAC: *UserMAC*; BSSID: *BSSID* Foreign AC sent a cut-off request to home AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Foreign AC向home AC发送cut off信息

MAC: *UserMAC*; BSSID: *BSSID* Removed the roam-back client.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除漫回用户信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an async authentication response:

 RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到异步认证回应 ，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authentication request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理认证请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authentication request and returned continue.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理认证请求，返回continue

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authentication request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理认证请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authentication request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理认证请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an async authorization response:

 RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到异步授权回应 ，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authorization request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理授权请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authorization request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理授权请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an authorization request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理授权请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an async accounting-start response:               RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到异步开始计费回应 ，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-start request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理开始计费请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-start request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理开始计费请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-start request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理开始计费请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an async accounting-update response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到异步计费更新回应 ，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-update request and returned success.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理计费更新请求，返回成功

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-update request and returned processing.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理计费更新请求，返回processing

MAC: *UserMAC*; BSSID: *BSSID* AAA of the home AC processed an accounting-update request and returned failure code *code*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC的AAA处理计费更新请求，返回失败，编号为*code*

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an async accounting-stop response: RespCode=*RespCode*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到异步终止计费回应 ，回应的状态编号为*RespCode*

MAC: *UserMAC*; BSSID: *BSSID* Home AC received disconnection session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到断开session control 连接事件

MAC: *UserMAC*; BSSID: *BSSID* Home AC received authorization change session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到session control 授权信息变化事件

MAC: *UserMAC*; BSSID: *BSSID* Home AC received unknown session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到未知 session control 事件

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an authentication request from foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到foreign AC发来的认证请求信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC received an accounting-update request from foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到foreign AC发来的计费更新请求信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC received a cut-off request from foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC收到foreign AC发来的cut off请求信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an authentication-success msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送认证成功信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent a continue-authentication msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送认证continue信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an authentication-failure msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送认证失败信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an authorization-success msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送授权成功信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an accounting-start success msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送计费开始成功信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an accounting-start failure msg to foreign AC because of server unreachable.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送计费开始不可达信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an accounting-update success msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送计费更新成功信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent an accounting-update failure msg to foreign AC.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送计费更新失败信息

MAC: *UserMAC*; BSSID: *BSSID* Home AC sent a message to foreign AC for changed session control authorization info.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向foreign AC发送session control 授权信息改变信息

MAC: *UserMAC*; BSSID: *BSSID* Username of the inter-roam user changed.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，AC间漫游用户的用户名发生改变

MAC: *UserMAC*; BSSID: *BSSID* Sent an authentication request from the home AC to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向服务器发送认证请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an authorization request from the home AC to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向服务器发送授权请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-start request from the home AC to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向服务器发送开始计费请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-update request from the home AC to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向服务器发送计费更新请求

MAC: *UserMAC*; BSSID: *BSSID* Sent an accounting-stop request from the home AC to the server.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，home  AC向服务器发送计费终止请求

MAC: *UserMAC*; BSSID: *BSSID* Received disconnection session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，收到断开session control 连接事件

MAC: *UserMAC*; BSSID: *BSSID* Received authorization change session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，收到session control 授权信息变化事件

MAC: *UserMAC*; BSSID: *BSSID* Received unknown session control event.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，收到未知 session control 事件

MAC: *UserMAC*; BSSID: *BSSID* Received authorization information: VLAN ID *vlan-id*, ACL number *acl-number*, user profile *userprofile-name*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，收到授权信息，包括VLAN 信息 *vlan-id*，ACL信息 *acl-number*，UserPorfile 信息*userprofile-name*

MAC: *UserMAC*; BSSID: *BSSID* No authorization information was received.

未收到授权信息

MAC: *UserMAC*; BSSID: *BSSID* Received session control event *event*.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，收到 Session Control 事件*event*

MAC: *UserMAC*; BSSID: *BSSID* Started 802.1X authentication.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开始进行802.1x认证

MAC: *UserMAC*; BSSID: *BSSID* Started MAC authentication.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开始 MAC认证

MAC: *UserMAC*; BSSID: *BSSID* Started OUI authentication.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，进行OUI模式认证

MAC: *UserMAC*; BSSID: *BSSID* Started Bypass authentication.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，进行BYPASS模式认证

MAC: *UserMAC*; BSSID: *BSSID* Removed the client  that was being authenticated.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除正在认证的用户

MAC: *UserMAC*; BSSID: *BSSID* Removed the client that has been authenticated.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除已认证的用户

MAC: *UserMAC*; BSSID: *BSSID* Removed the roam-out client.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除漫出用户

MAC: *UserMAC*; BSSID: *BSSID* Checked client secure handshake hash.

Client hash                 : *hashvalue1*

Current server hash   : *hashvalue2*

Previous server hash: *hashvalue3*

Previous server hash used times: *times1*

Hash mismatches: *times2*

校验客户端安全握手hash，客户端hash值为*hashvalue1*，服务器当前下发的hash值为*hashvalue2*，服务器上一次下发的hash值为*hashvalue3*，旧hash值使用的次数*times1*，hash值不匹配的次数*times2*

表1-3 debugging wlan wlas fsm命令输出信息描述表

字段

描述

MAC: *UserMAC*; BSSID: *BSSID* BE state machine entered *State* state.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，BE状态机进入*State*状态

MAC: *UserMAC*; BSSID: *BSSID* PAE state machine entered *State* state.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，PAE状态机进入*State*状态

MAC: *UserMAC*; BSSID: *BSSID* MAC-authentication state machine entered *State* state.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，MAC认证状态机进入*State*状态

表1-4 debugging wlan wlas timer命令输出信息描述表

字段

描述

BSSID: *BSSID* Temporary service stop timer expired.

BSSID为*BSSID*，临时关闭服务定时器超时

BSSID: *BSSID* Deleted the temporary service stop timer.

BSSID为*BSSID，*删除临时关闭服务定时器

BSSID: *BSSID* Created the temporary service stop timer.

BSSID为*BSSID，*成功开启临时关闭服务定时器

MAC: *UserMAC*; BSSID: *BSSID* Held timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*， Held定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Re-authentication timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，重认证定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Server response timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，服务器定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Client response timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，客户端定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Created the re-authentication  timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启重认证定时器

MAC: *UserMAC*; BSSID: *BSSID* Created the held timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启Held定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the held timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*， 删除Held定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the re-authentication timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除重认证定时器

MAC: *UserMAC*; BSSID: *BSSID* Created the server response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，开启服务器超时定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the server response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除服务器超时定时器

MAC: *UserMAC*; BSSID: *BSSID* Created the client response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启客户端超时定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the client response timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除客户端超时定时器

MAC: *UserMAC*; BSSID: *BSSID* Handshake timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，握手定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Created the handshake timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启握手定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the handshake timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除握手定时器

MAC: *UserMAC*; BSSID: *BSSID* Accounting-update timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，更新计费定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Created the accounting-update timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启用户更新计费定时器

MAC: *UserMAC*; BSSID: *BSSID* Deleted the accounting-update timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除计费更新定时器

MAC: *UserMAC*; BSSID: *BSSID* Refreshed the accounting-update timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，更新实时计费时间

MAC: *UserMAC*; BSSID: *BSSID* Session timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，会话定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Created the session timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启会话超时定时器

MAC: *UserMAC*; BSSID: *BSSID* Refreshed the session timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，更新Session定时器时间

MAC: *UserMAC*; BSSID: *BSSID* Deleted the session timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除会话定时器

MAC: *UserMAC*; BSSID: *BSSID* Block MAC timer expired.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Block MAC定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Deleted the Block MAC timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除Block MAC定时器

MAC: *UserMAC*; BSSID: *BSSID* Created the Block MAC timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启Block MAC定时器

MAC: *UserMAC*; BSSID: *BSSID* Fail VLAN client timer expired.

 BSSID为*BSSID*，用户的MAC地址为*UserMAC*，Fail VLAN用户定时器超时

MAC: *UserMAC*; BSSID: *BSSID* Deleted the Fail VLAN client timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，删除Fail VLAN用户定时器

MAC: *UserMAC*; BSSID: *BSSID* Created the Fail VLAN client timer.

BSSID为*BSSID*，用户的MAC地址为*UserMAC*，成功开启Fail VLAN用户定时器

表1-5 debugging wlan wlas packet receive命令输出信息描述表

字段

描述

MAC: *userMAC*, BSSID:*BSSID*

\-\-\-\--Packet HEAD\-\-\-\--

Mac Frame Type: *PAEType*

Protocol Version ID: *VersionID*

Packet Type: *PacketType*

Packet Length: *Length*

用户的MAC地址为*UserMac*，BSSID为*BSSID*，接收到EAPOL报文，报文的协议类型为*PAEType*，报文协议版本ID为*VersionID*，报文的数据帧类型为*PacketType*，报文的长度为*Length*

表1-6 debugging wlan wlas packet send命令输出信息描述表

字段

描述

MAC: *userMAC*, BSSID:*BSSID*

\-\-\-\--Packet HEAD\-\-\-\--

Mac Frame Type: *MacType*

Protocol Version ID: *VersionID*

Packet Type: *PacketType*

Packet Length: *Length*

\-\-\-\--Packet Body\-\-\-\--

Code: *Code*

Identifier: *Identifier*

Length: *Length*

用户的MAC地址为*UserMac*，BSSID为*BSSID*，发送EAPOL报文，报文的协议类型为*PAEType*，报文的协议版本ID为*VersionID*，报文的数据帧类型为*PacketType*，报文的长度为*Length*，Packet Body字段的内容是一个EAP报文，EAP报文的类型为*Code*，标示符为*Identifier*，长度为*Length*

【举例】

\# 在设备上配置WLAN用户接入认证，打开WLAS事件调试信息开关，打印如下调试信息：

\<AC\> debugging wlan wlas event

\*May 12 16:39:27:253 2014 H3C STAMGR/7/Event: [MAC:0023-8933-2098; BSSID:000f-e2

01-0701Sent an authentication request.]

*[//*]*发送一个认证报文。*

\# 打开WLAS定时器调试开关，打印如下调试信息：

\*May 12 16:39:24:437 2014 H3C STAMGR/7/Timer: MAC:0023-8933-2098; BSSID:000f-e2

01-0701Created the client response timer.

*[//*]*创建一个客户端回应定时器。*
