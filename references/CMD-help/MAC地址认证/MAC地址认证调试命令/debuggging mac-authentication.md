::: {#75961557 .myid}
[]{#_Toc404792527}[]{#struct_0_17602_x6333_x319912208}[]{#_Toc233198545}

**MAC地址认证 \-- MAC地址认证调试命令 \-- debuggging mac-authentication**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17602_x6333_1805117900}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900364459}

[**[debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_17602_x6333_1297413750}

[**[undo debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_17602_x6333_1672936019}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_17602_x6333_x1053626496}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17602_x6333_1255348645}

[**[undo debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_17602_x6333_x1430009336}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_17602_x6333_x1086949698}[模式：]{style="font-family:宋体"}

[**[debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** } ]{lang="EN-US"}]{#struct_0_17602_x6333_767171051}[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="SV"}

[**[undo debugging mac-authentication ]{lang="EN-US"}**[{ **all** \| **error** \| **event** } ]{lang="EN-US"}]{#struct_0_17602_x6333_1457986234}[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17602_x6333_1900429995}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17602_x6333_x656196384}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17602_x6333_x215927205}

[[network-admin]{lang="EN-US"}]{#struct_0_17602_x6333_756107165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17602_x6333_1250537189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17602_x6333_469300281}

[**[all]{lang="EN-US"}**]{#struct_0_17602_x6333_1241012850}[：表示所有信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17602_x6333_1131960995}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17602_x6333_1473385469}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_17602_x6333_1015059193}[：表示指定单板的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_17602_x6333_1900495531}[：表示指定成员设备的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot ]{lang="EN-US"}***[slot-mumber]{lang="EN-US"}*]{#struct_0_17602_x6333_x214794095}[：表示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_17602_x6333_2092984942}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示成员设备上指定单板的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_17602_x6333_x837049035}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示指定单板的调试信息开关。]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17602_x6333_x1891951285}

[]{#OLE_LINK1}[**[debug mac-authentication]{lang="EN-US"}**]{#struct_0_17602_x6333_1573114244}[命令用来打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证调试信息开关。]{style="font-family:宋体"}**[undo debug mac-authentication]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_x1890252969}[地址认证调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_17602_x6333_x770595960}[[表1-1 ]{lang="EN-US"}[debugging mac-authentication error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x607187590}[[字段]{style="font-family:黑体"}]{#struct_0_17602_x6333_x309501898}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17602_x6333_1250190823}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving authenticate response.]{lang="EN-US"}]{#struct_0_17602_x6333_1900561067}

[[收到认证回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_x1829726244}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving authorization response.]{lang="EN-US"}]{#struct_0_17602_x6333_1100341268}

[[收到授权回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_1583192230}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving accounting response.]{lang="EN-US"}]{#struct_0_17602_x6333_998608413}

[[收到计费回应消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_1900626603}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to find user by *mac* and *interface-type interface-num* when receiving session control cut request.]{lang="EN-US"}]{#struct_0_17602_x6333_x239465250}

[[收到包含]{style="font-family:宋体"}[Cut]{lang="EN-US"}]{#struct_0_17602_x6333_2137365391}[命令字的]{style="font-family:宋体"}[Session Control]{lang="EN-US"}[消息时，根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[和接口名]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[无法找到对应的用户]{style="font-family:宋体"}

[[Failed to set the interface driver.]{lang="EN-US"}]{#struct_0_17602_x6333_x1631010569}

[[设置接口的驱动失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1425618771}

[[Failed to add socket to epoll.]{lang="EN-US"}]{#struct_0_17602_x6333_622092089}

[[socket]{lang="EN-US"}]{#struct_0_17602_x6333_1900692139}[加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to create socket.]{lang="EN-US"}]{#struct_0_17602_x6333_934820463}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_17602_x6333_758026033}[失败]{style="font-family:宋体"}

[[Failed to connect to master.]{lang="EN-US"}]{#struct_0_17602_x6333_x815309396}

[[连接主控板失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1755315582}

[[Failed to write message to maca que. *msgtype*]{lang="EN-US"}]{#struct_0_17602_x6333_1899709099}

[[写消息到]{style="font-family:宋体"}[maca]{lang="EN-US"}]{#struct_0_17602_x6333_x1386004782}[队列失败，]{style="font-family:宋体"}*[msgtype]{lang="EN-US"}*[表示消息类型]{style="font-family:宋体"}

[[Failed to accept connect.]{lang="EN-US"}]{#struct_0_17602_x6333_x326590627}

[[接收连接失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_748028215}

[[Failed to create global socket.]{lang="EN-US"}]{#struct_0_17602_x6333_x1416268681}

[[创建全局]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_17602_x6333_1755846598}[失败]{style="font-family:宋体"}

[[Failed to process message for the message type is invalid.]{lang="EN-US"}]{#struct_0_17602_x6333_1899774635}

[[消息处理失败因为消息类型非法]{style="font-family:宋体"}]{#struct_0_17602_x6333_x657773893}

[[Failed to add socket to lpu connection table.]{lang="EN-US"}]{#struct_0_17602_x6333_x998206239}

[[将]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_17602_x6333_1485901494}[加入长连接链表失败]{style="font-family:宋体"}

[[Failed to accept connection with the global known port.]{lang="EN-US"}]{#struct_0_17602_x6333_1900233388}

[[在全局知名端口接收连接失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1025462391}

[[Failed to find online user\'s mac and add mac to driver again.]{lang="EN-US"}]{#struct_0_17602_x6333_873740750}

[[在线用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_x1277636498}[地址不存在，向驱动重新添加该]{style="font-family:宋体"}[MAC]{lang="EN-US"}

[[Invalid queue message received.]{lang="EN-US"}]{#struct_0_17602_x6333_1037679580}

[[接收到的队列消息不合法]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900298924}

[[Failed to create user for the number of users reached the maximum. ]{lang="EN-US"}]{#struct_0_17602_x6333_250613771}

[[用户数已达最大值，创建用户失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1450937127}

[[Failed to allocate memory for user.]{lang="EN-US"}]{#struct_0_17602_x6333_x759189359}

[[为用户申请内存失败]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900364460}

[[Failed to start acct-update period timer when receiving acct-start response, terminate user session.]{lang="EN-US"}]{#struct_0_17602_x6333_1296823927}

[[当收到计费开始响应消息时，打开计费更新周期定时器失败，结束用户会话]{style="font-family:宋体"}]{#struct_0_17602_x6333_895351254}

[[Failed to allocate memory for pam handle.]{lang="EN-US"}]{#struct_0_17602_x6333_1900429996}

[[为]{style="font-family:宋体"}[pam handle]{lang="EN-US"}]{#struct_0_17602_x6333_x656130848}[分配内存失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_17602_x6333_x958598655}[[表1-2 ]{lang="EN-US"}[debugging mac-authentication event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x608313574}[[字段]{style="font-family:黑体"}]{#struct_0_17602_x6333_1109694279}

[[描述]{style="font-family:黑体"}]{#struct_0_17602_x6333_x180029939}

[[Received EPOLLERR or EPOLLHUP event.]{lang="EN-US"}]{#struct_0_17602_x6333_689837002}

[[收到]{style="font-family:宋体"}[EPOLLERR]{lang="EN-US"}]{#struct_0_17602_x6333_1900495532}[或]{style="font-family:宋体"}[EPOLLHUP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Reconnect timer timeout, reconnecting to mpu.]{lang="EN-US"}]{#struct_0_17602_x6333_2093181550}

[[重连定时器超时，向]{style="font-family:宋体"}[mpu]{lang="EN-US"}]{#struct_0_17602_x6333_44357419}[重新发起连接]{style="font-family:宋体"}

[[Successfully connected to master, closed reconnect timer.]{lang="EN-US"}]{#struct_0_17602_x6333_x917008347}

[[和主控板连接成功，关闭重连定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_266958477}

[[Processing If_Delete event:]{lang="EN-US"}]{#struct_0_17602_x6333_x51045924}

[[处理接口删除事件]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900561068}

[[Processing If_Deactive event:]{lang="EN-US"}]{#struct_0_17602_x6333_x1829660708}

[[处理接口去激活事件]{style="font-family:宋体"}]{#struct_0_17602_x6333_1887668409}

[[Processing If_Active event:]{lang="EN-US"}]{#struct_0_17602_x6333_x1335766440}

[[处理接口激活事件]{style="font-family:宋体"}]{#struct_0_17602_x6333_x673864237}

[[Processing If_Down event:]{lang="EN-US"}]{#struct_0_17602_x6333_1900626604}

[[处理接口]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_17602_x6333_x239924002}[事件]{style="font-family:宋体"}

[[Processing HA UPGRADE event.]{lang="EN-US"}]{#struct_0_17602_x6333_197464204}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17602_x6333_1890065911}[升级事件]{style="font-family:宋体"}

[[Processing HA DEGRADE event.]{lang="EN-US"}]{#struct_0_17602_x6333_x91703683}

[[处理]{style="font-family:宋体"}[HA]{lang="EN-US"}]{#struct_0_17602_x6333_1034009328}[降级事件]{style="font-family:宋体"}

[[Processing the event of IFEVENT.]{lang="EN-US"}]{#struct_0_17602_x6333_1900692140}

[[正在处理接口事件]{style="font-family:宋体"}]{#struct_0_17602_x6333_935410286}

[[User will log off for failing to change state.]{lang="EN-US"}]{#struct_0_17602_x6333_1976588742}

[[用户因为状态变迁失败而下线]{style="font-family:宋体"}]{#struct_0_17602_x6333_x147812472}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] User received stop accounting response, RespCode=*RespCode.*]{lang="EN-US"}]{#struct_0_17602_x6333_x1666242407}

[[用户（]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_1899709100}[地址为]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[，所属]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[，接入端口为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[）收到停止计费回应消息，响应码为]{style="font-family:宋体"}*[RespCode]{lang="EN-US"}*

[[Processing new_mac event]{lang="EN-US"}]{#struct_0_17602_x6333_569851609}

[[处理]{style="font-family:宋体"}[new-mac]{lang="EN-US"}]{#struct_0_17602_x6333_1152790842}[事件]{style="font-family:宋体"}

[[Notified PortSec of new_mac result]{lang="EN-US"}]{#struct_0_17602_x6333_x1301011276}

[[通知端口安全]{style="font-family:宋体"}[new-mac]{lang="EN-US"}]{#struct_0_17602_x6333_1899774636}[结果]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlan*:*interface-type interface-num*\] Processing unauthor event.]{lang="EN-US"}]{#struct_0_17602_x6333_x657970501}

[[处理]{style="font-family:宋体"}[unauthor]{lang="EN-US"}]{#struct_0_17602_x6333_x1739328787}[事件]{style="font-family:宋体"}

[[Processing IfVlanDel event, interface Index is *index*, VLAN ID = *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x2104320865}

[[处理]{style="font-family:宋体"}[ifVlanDel]{lang="EN-US"}]{#struct_0_17602_x6333_454900079}[事件，接口索引为]{style="font-family:宋体"}*[interface-type interface-num]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Processing Auth_Fail_Proc notification]{lang="EN-US"}]{#struct_0_17602_x6333_1900233385}

[[处理]{style="font-family:宋体"}[Auth_Fail_Proc ]{lang="EN-US"}]{#struct_0_17602_x6333_x1025790071}[通知事件]{style="font-family:宋体"}

[[Notified PortSec of Auth_Fail_Proc result]{lang="EN-US"}]{#struct_0_17602_x6333_x132021854}

[[通知端口安全]{style="font-family:宋体"}[Auth_Fail_Proc]{lang="EN-US"}]{#struct_0_17602_x6333_574975247}[结果]{style="font-family:宋体"}

[[Added silent mac address]{lang="EN-US"}]{#struct_0_17602_x6333_1900298921}

[[添加静默]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_925026562}[地址]{style="font-family:宋体"}

[[User server timer timeout and logged off]{lang="EN-US"}]{#struct_0_17602_x6333_x1862861870}

[[用户的服务器定时器超时，用户下线]{style="font-family:宋体"}]{#struct_0_17602_x6333_x400159294}

[[User reauth timer timeout and was authenticated again]{lang="EN-US"}]{#struct_0_17602_x6333_1900364457}

[[用户重认证定时器超时，重新认证]{style="font-family:宋体"}]{#struct_0_17602_x6333_1297282678}

[[User state Initialize changed to Disconnect]{lang="EN-US"}]{#struct_0_17602_x6333_x1864208454}

[[用户状态从初始化转到断开连接]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900429993}

[[User state Disconnect changed to Authenticating]{lang="EN-US"}]{#struct_0_17602_x6333_x655803168}

[[用户状态从断开连接转到开始认证]{style="font-family:宋体"}]{#struct_0_17602_x6333_x849636039}

[[User state Authenticating changed to Authenticated]{lang="EN-US"}]{#struct_0_17602_x6333_x1915005461}

[[用户状态从开始认证转到认证成功]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900495529}

[[User state Authenticated changed to Initialize]{lang="EN-US"}]{#struct_0_17602_x6333_2092460655}

[[用户状态从认证转到初始化]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1110094675}

[[User was being authenticated with name *user-name* and password *string*]{lang="EN-US"}]{#struct_0_17602_x6333_1440464350}

[[用户（名称为]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*]{#struct_0_17602_x6333_1900561065}[，密码为]{style="font-family:宋体"}*[string]{lang="EN-US"}*[）进行认证]{style="font-family:宋体"}

[[User started server timer, length *time*s]{lang="EN-US"}]{#struct_0_17602_x6333_x1829857316}

[[用户开启服务定时器，时长是]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_17602_x6333_x1170574180}[秒]{style="font-family:宋体"}

[[User closed server timer]{lang="EN-US"}]{#struct_0_17602_x6333_1900626601}

[[用户关闭服务定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_x239596322}

[[User started reauth timer, length *time*s]{lang="EN-US"}]{#struct_0_17602_x6333_x619710148}

[[用户开启重认证定时器，时长是]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_17602_x6333_1900692137}[秒]{style="font-family:宋体"}

[[User closed reauth timer]{lang="EN-US"}]{#struct_0_17602_x6333_935737967}

[[用户关闭重认证定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_x2091945096}

[[User closed session timer]{lang="EN-US"}]{#struct_0_17602_x6333_1899709097}

[[用户关闭会话定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1386397998}

[[User session timer timeout and logged off]{lang="EN-US"}]{#struct_0_17602_x6333_147877874}

[[用户的会话定时器超时，用户下线]{style="font-family:宋体"}]{#struct_0_17602_x6333_1899774633}

[[User started session timer, length *time*s]{lang="EN-US"}]{#struct_0_17602_x6333_x657642821}

[[用户开启会话定时器，时长是]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_17602_x6333_1728121234}[秒]{style="font-family:宋体"}

[[The times of no-response accounting-update reached the maximum]{lang="EN-US"}]{#struct_0_17602_x6333_1900233386}

[[无响应计费更新时间达到最大值]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1025855607}

[[AAA processed accounting-update request and returned processing]{lang="EN-US"}]{#struct_0_17602_x6333_1990937326}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900298922}[处理计费更新请求并返回结果]{style="font-family:宋体"}

[[AAA processed accounting-update request and returned success]{lang="EN-US"}]{#struct_0_17602_x6333_925223170}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_x450310592}[处理计费更新请求并返回成功]{style="font-family:宋体"}

[[AAA processed accounting-update request and returned fail]{lang="EN-US"}]{#struct_0_17602_x6333_1900364458}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1297348214}[处理计费更新请求并返回失败]{style="font-family:宋体"}

[[User started update-accounting timer, length *time*s]{lang="EN-US"}]{#struct_0_17602_x6333_x285101063}

[[用户开启更新计费定时器，时长是]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_17602_x6333_1900429994}[秒]{style="font-family:宋体"}

[[User closed update-accounting timer]{lang="EN-US"}]{#struct_0_17602_x6333_x656261920}

[[用户关闭更新计费定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900495530}

[[User closed offline-detect timer]{lang="EN-US"}]{#struct_0_17602_x6333_2093050478}

[[用户关闭下线检测定时器]{style="font-family:宋体"}]{#struct_0_17602_x6333_823020595}

[[User mac not hitted and user logged off]{lang="EN-US"}]{#struct_0_17602_x6333_1900561066}

[[没找到用户对应的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_x1829791780}[，用户下线]{style="font-family:宋体"}

[[User started offline-detect timer, length *time*s]{lang="EN-US"}]{#struct_0_17602_x6333_1900626602}

[[用户开启下线检测定时器，时长是]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_17602_x6333_x239530786}[秒]{style="font-family:宋体"}

[[AAA processed accounting-stop request and returned processing]{lang="EN-US"}]{#struct_0_17602_x6333_x199957892}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900692138}[处理计费停止请求并返回正在处理]{style="font-family:宋体"}

[[AAA processed accounting-stop request and returned success]{lang="EN-US"}]{#struct_0_17602_x6333_934885999}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1899709098}[处理计费停止请求并返回成功]{style="font-family:宋体"}

[[AAA processed authentication request and returned processing]{lang="EN-US"}]{#struct_0_17602_x6333_x1385939246}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_x1350721504}[处理认证请求并返回正在处理]{style="font-family:宋体"}

[[AAA processed authentication request and returned success]{lang="EN-US"}]{#struct_0_17602_x6333_1899774634}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_x657839429}[处理认证请求并返回成功]{style="font-family:宋体"}

[[AAA processed authentication request and returned fail]{lang="EN-US"}]{#struct_0_17602_x6333_1900233383}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_x1026183287}[处理认证请求并返回失败]{style="font-family:宋体"}

[[AAA processed authentication request and returned error]{lang="EN-US"}]{#struct_0_17602_x6333_x1268743974}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900298919}[处理认证请求并返回错误]{style="font-family:宋体"}

[[AAA processed authorization request and returned processing]{lang="EN-US"}]{#struct_0_17602_x6333_924502275}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900364455}[处理授权请求并返回正在处理]{style="font-family:宋体"}

[[AAA processed authorization request and returned success]{lang="EN-US"}]{#struct_0_17602_x6333_1297151606}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900429991}[处理授权请求并返回成功]{style="font-family:宋体"}

[[AAA processed authorization request and returned failed]{lang="EN-US"}]{#struct_0_17602_x6333_x655934240}

[[AAA]{lang="EN-US"}]{#struct_0_17602_x6333_1900495527}[处理授权请求并返回失败]{style="font-family:宋体"}

[[User was deleted]{lang="EN-US"}]{#struct_0_17602_x6333_2093378159}

[[用户被删除]{style="font-family:宋体"}]{#struct_0_17602_x6333_1900561063}

[[A user was logging off. A accounting-start request for the new user with the same name will be send after the current user logged off.]{lang="EN-US"}]{#struct_0_17602_x6333_x1829988388}

[[有用户正在下线，此时如果有相同用户名的用户上线，则设备发为其发送的计费开始请求将在当前用户成功下线后发送]{style="font-family:宋体"}]{#struct_0_17602_x6333_769098399}

[[User received authentication response, ]{lang="EN-US"}]{#struct_0_17602_x6333_1900626599}

[[用户收到认证回应]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1813050139}

[[User received authorization response]{lang="EN-US"}]{#struct_0_17602_x6333_1900692135}

[[用户收到授权回应]{style="font-family:宋体"}]{#struct_0_17602_x6333_935606895}

[[User received start accounting response]{lang="EN-US"}]{#struct_0_17602_x6333_1899709095}

[[用户收到计费开始回应]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1386266926}

[[User received update accounting response]{lang="EN-US"}]{#struct_0_17602_x6333_1899774631}

[[用户收到计费更新回应]{style="font-family:宋体"}]{#struct_0_17602_x6333_x657511749}

[[\[*mac*:VLAN*vlanid*:*interface-type interface-num*\] Auth-delay timer time out.]{lang="EN-US"}]{#struct_0_17602_x6333_x1489641517}

[[用户认证延迟定时器超时]{style="font-family:宋体"}]{#struct_0_17602_x6333_x1489575981}

[[\[*mac*:VLAN*vlanid*:*interface-type interface-num*\] Succeeded to add User to critical vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x455528479}

[[用户成功被添加到]{style="font-family:宋体"}[critical VLAN]{lang="EN-US"}]{#struct_0_17602_x6333_x1489510445}[中]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlanid*:*interface-type interface-num*\] Succeeded to add User to guest vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x1489444909}

[[用户成功被添加到]{style="font-family:宋体"}[guest VLAN]{lang="EN-US"}]{#struct_0_17602_x6333_181587134}[中]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlanid*:*interface-type interface-num*\] Delete User from critical vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x1488855085}

[[用户从]{style="font-family:宋体"}[critical VLAN]{lang="EN-US"}]{#struct_0_17602_x6333_1229221249}[中退出]{style="font-family:宋体"}

[[\[*mac*:VLAN*vlanid*:*interface-type interface-num*\] Delete User from guest vlan *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x1488789549}

[[用户从]{style="font-family:宋体"}[guest VLAN]{lang="EN-US"}]{#struct_0_17602_x6333_1019537075}[中退出]{style="font-family:宋体"}

[[Authorization ACL number is *acl-number*.]{lang="EN-US"}]{#struct_0_17602_x6333_x1489379374}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_17602_x6333_1485760720}[编号是]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*

[[Authorization VLAN ID is *vlan-id*.]{lang="EN-US"}]{#struct_0_17602_x6333_x1489313838}

[[授权]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_17602_x6333_x1489248302}[是]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*

[[Processing MAC-authentication delay.]{lang="EN-US"}]{#struct_0_17602_x6333_2123335085}

[[处理用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17602_x6333_x1489182766}[认证延迟]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17602_x6333_x568033838}

[[\# ]{lang="EN-US"}]{#struct_0_17602_x6333_638287411}[在一台启动了]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证功能的设备上，打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证的所有调试功能，有用户上线时，将输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-authentication all]{lang="EN-US"}]{#struct_0_17602_x6333_1900233384}

[\*Jan  1 14:48:13:347 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1[\] Processing new_mac event.]{.TerminalDisplayChar}]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x1025724535}*[处理]{style="font-family:宋体"}[new_mac]{lang="EN-US"}[事件，用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1cbd-b9e3-c434]{lang="EN-US"}[，用户所在的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，用户接入的接口名为]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}*

[[\*Jan  1 14:48:13:349 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_269544532}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User state changed from Initialize to Authenticating.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_1849993854}*[用户状态从初始化变更为正在认证]{style="font-family:宋体"}*

[[\*Jan  1 14:48:13:350 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_394645017}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User was being authenticated with name yangliping and]{lang="EN-US"}

[ password \*\*\*.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x1985070119}*[用户使用用户名"]{style="font-family:宋体"}[yangliping]{lang="EN-US"}["和密码]{style="font-family:宋体"}[\*\*\*\*]{lang="EN-US"}[正在进行认证]{style="font-family:宋体"}*

[[\*Jan  1 14:48:13:351 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1900298920}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User started server timer, length=100(s).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_925092098}*[开启用户服务器超时定时器，时长为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  1 14:48:13:354 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_861619194}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] AAA processed authentication request and returned processing[.]{.TerminalDisplayChar}]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_17602_x6333_x804214219}*[处理用户的认证请求，返回处理结果为：正在处理]{style="font-family:宋体"}*

[[\*Jan  1 14:48:13:355 2011 Sysname MACA/7/EVENT: ]{lang="EN-US"}]{#struct_0_17602_x6333_x1859206357}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] Notified PortSec of new new_mac result: 1. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x245019853}*[通知端口安全]{style="font-family:宋体"}[new-mac]{lang="EN-US"}[结果为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Jan  1 14:48:14:400 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1620388312}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User received authentication response, RespCode=0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_1033099481}*[用户收到认证回应消息，响应码为]{style="font-family:宋体"}[1]{lang="EN-US"}*

[[\*Jan  1 14:48:14:401 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1900364456}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User state changed from Authenticating to Authenticated.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_1297217142}*[用户状态从认证中变更为已通过认证]{style="font-family:宋体"}*

[[\*Jan  1 14:48:14:402 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_850447758}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User closed server timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x2092393769}*[关闭用户服务器超时定时器]{style="font-family:宋体"}*

[[\*Jan  1 14:48:14:404 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_x1683891136}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] AAA processed authorization request and returned success.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_17602_x6333_x1035153406}*[处理用户授权请求，返回处理结果为：成功]{style="font-family:宋体"}*

[[\*Jan  1 14:48:14:405 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_x624568747}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User started session timer, length=86400(s)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x1925143020}*[开启用户会话定时器，时长为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  1 14:48:14:409 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1900429992}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User started offline-detect timer, length=300(s).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x655868704}*[开启用户在线探测定时器，时长为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  1 14:48:14:414 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_263034852}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User started update-accounting timer, length=600(s).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_1983687888}*[开启用户实时计费定时器，时长为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17602_x6333_1430377737}[该用户下线时，将输出如下调试信息：]{style="font-family:宋体"}

[[\*Jan  1 14:50:40:800 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1788131184}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User state Authenticated changed to Disconnect.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x760615963}*[用户状态从已认证变更为下线]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:801 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1900495528}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User closed server timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_2092526191}*[关闭用户服务器超时定时器]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:802 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_x1512360580}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User closed update-accounting timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x806644719}*[关闭用户实时计费定时器]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:803 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_x2032483313}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User closed session timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_2027836001}*[关闭用户会话定时器]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:804 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_x409518815}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User closed offline-detect timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_x1056598500}*[关闭用户在线探测定时器]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:808 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1900561064}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] AAA processed accounting-stop request and returned success.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_17602_x6333_x1829922852}*[处理用户的计费停止请求，返回处理结果为：成功]{style="font-family:宋体"}*

[[\*Jan  1 14:50:40:809 2011 Sysname MACA/7/EVENT:]{lang="EN-US"}]{#struct_0_17602_x6333_1358832764}

[\[1cbd-b9e3-c434:VLAN2:GE1/0/1\] User was deleted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17602_x6333_1260665561}*[用户被删除]{style="font-family:宋体"}*
