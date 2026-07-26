::: {#-582348807 .myid}
[]{#_Toc404793318}[]{#struct_0_12438_x2040_1369324439}[]{#_Toc320977758}[]{#_Toc320977705}[]{#_Toc320977672}[]{#_Toc320977658}[]{#_Toc320956813}

**SSL VPN \-- SSL VPN调试命令 \-- debugging sslvpn**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_12438_x2040_1997678174}

[**[debugging]{lang="EN-US"}**[ **sslvpn** { **all** \| **aaa** \| **error** \| **event** \| **fsm** \| **packet** \[ **verbose** \] \| **timer** }]{lang="EN-US"}]{#struct_0_12438_x2040_x1804553332}

[**[undo]{lang="EN-US"}**[ **debugging sslvpn** { **all** \| **aaa** \| **error** \| **event** \| **fsm** \| **packet** \[ **verbose** \] \| **timer** }]{lang="EN-US"}]{#struct_0_12438_x2040_554279373}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x2132754726}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12438_x2040_1194369240}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12438_x2040_166739801}

[[network-admin]{lang="EN-US"}]{#struct_0_12438_x2040_x607801579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12438_x2040_239691391}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x710116554}

[**[all]{lang="EN-US"}**]{#struct_0_12438_x2040_x1443775670}[：表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[aaa]{lang="EN-US"}**]{#struct_0_12438_x2040_1534114429}[：表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[认证调试信息开关]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_12438_x2040_x1050328431}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_12438_x2040_x1565886741}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_12438_x2040_1312013942}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_12438_x2040_1879877464}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_12438_x2040_x1712489716}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[报文详细信息调试信息开关。如果不指定本参数，则表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[报文简要信息调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_12438_x2040_x1214928487}[：表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_12438_x2040_519832650}

[**[debugging]{lang="EN-US"}**[ **sslvpn**]{lang="EN-US"}]{#struct_0_12438_x2040_x1347604222}[命令用来打开]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **sslvpn**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_12438_x2040_89956159}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging sslvpn aaa]{lang="FR"}]{#struct_0_12438_x2040_x32659576}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2018878875}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_x805592214}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_512493582}

[[Failed to send offline request to kernel. contextID: *contextID*; onlineID: *onlineID.*]{lang="FR"}]{#struct_0_12438_x2040_2018766801}

[[通知内核下线请求失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_544072123}*[contextID]{lang="FR"}*[为下线请求所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为需要下线的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Parse the ]{lang="FR"}[private information in the authentication request]{lang="EN-US"}]{#struct_0_12438_x2040_943499287}[. original length: *original-length*, decode length: *decode-length*.]{lang="FR"}

[[解析认证请求中的私有信息，]{style="font-family:宋体"}]{#struct_0_12438_x2040_341450053}*[original-length]{lang="FR"}*[为私有信息的原始长度，]{style="font-family:宋体"}*[decode-length]{lang="FR"}*[为私有信息解码后的长度]{style="font-family:宋体"}

 

[[Set pam user IPv4 *ipv4-address*. result: *result*.]{lang="FR"}]{#struct_0_12438_x2040_x186188533}

[[向]{style="font-family:宋体"}]{#struct_0_12438_x2040_1037082510}[pam]{lang="FR"}[设置用户的]{style="font-family:宋体"}[IPv4]{lang="FR"}[地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[ipv4-address]{lang="FR"}*[为设置的]{style="font-family:宋体"}[IPv4]{lang="FR"}[地址，]{style="font-family:宋体"}*[result]{lang="FR"}*[为设置结果]{style="font-family:宋体"}

 

[[Set pam user IPv6 ]{lang="EN-US"}]{#struct_0_12438_x2040_105709136}*[ipv6-address]{lang="FR"}*[. result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向]{style="font-family:宋体"}[pam]{lang="EN-US"}]{#struct_0_12438_x2040_608022652}[设置用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[ipv6-address]{lang="FR"}*[为设置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[result]{lang="FR"}*[为设置结果]{style="font-family:宋体"}

 

[[Set pam server string. length: *length*; result: ]{lang="EN-US"}]{#struct_0_12438_x2040_443106015}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向]{style="font-family:宋体"}[pam]{lang="EN-US"}]{#struct_0_12438_x2040_452682860}[设置服务属性，]{style="font-family:宋体"}*[length]{lang="EN-US"}*[为服务属性的长度，]{style="font-family:宋体"}*[result]{lang="FR"}*[为设置结果]{style="font-family:宋体"}

 

[[Set pam user MAC *mac-address*. result: ]{lang="EN-US"}]{#struct_0_12438_x2040_984728140}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向]{style="font-family:宋体"}[pam]{lang="EN-US"}]{#struct_0_12438_x2040_x1337600453}[设置用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[设置的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[result]{lang="FR"}*[为设置结果]{style="font-family:宋体"}

 

[[Authorizing policy group: *name*.]{lang="EN-US"}]{#struct_0_12438_x2040_x1084746796}

[[认证的]{style="font-family:宋体"}[policy group]{lang="EN-US"}]{#struct_0_12438_x2040_x1956808154}[名称]{style="font-family:宋体"}

 

[[Deleted accounting update timer. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_123324486}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[删除计费更新定时器，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1813463795}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Deleted accounting session timer. contextID: contextID; onlineID: ]{lang="EN-US"}]{#struct_0_12438_x2040_741517015}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[删除计费会话定时器，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x542708867}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Succeeded in updating accounting. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1113401081}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[更新计费成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1637803160}*[contextID]{lang="FR"}*[为更新计费所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to update accounting. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1827616039}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[更新计费失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x2119119268}*[contextID]{lang="FR"}*[为更新计费所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Accounting update timer timed out. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_124939054}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[计费更新定时器超时，]{style="font-family:宋体"}]{#struct_0_12438_x2040_2105951221}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Succeeded in creating accounting update timer. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x634484039}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[创建计费更新定时器成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1766256599}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to create accounting update time. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1259251914}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[创建计费更新定时器失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1312575305}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Accounting session timer timed out. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x2050982649}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[计费会话定时器超时，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x327474717}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Succeeded in creating accounting session timer. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1110954261}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[创建计费会话定时器成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_12284002}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to create accounting session timer. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x306832027}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[创建计费会话定时器失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1268315982}*[contextID]{lang="FR"}*[为定时器所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为定时器对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Accounting started. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1266039392}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[开始计费，]{style="font-family:宋体"}]{#struct_0_12438_x2040_69280646}*[contextID]{lang="FR"}*[为所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Processed asynchronous authentication response. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1002262738}*[contextID]{lang="FR"}*[; requestID: *requestID*; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[处理异步认证应答，]{style="font-family:宋体"}]{#struct_0_12438_x2040_503397107}*[contextID]{lang="FR"}*[为认证应答所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为认证应答对应的上线请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"} *[result]{lang="FR"}*[为]{style="font-family:宋体"}[认证应答消息的处理结果]{style="font-family:宋体"}

 

[[Processed asynchronous authorization response. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1214869904}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[处理异步授权应答，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1481264546}*[contextID]{lang="FR"}*[为授权应答所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为授权应答对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为]{style="font-family:宋体"}[授权应答消息的处理结果]{style="font-family:宋体"}

 

[[Processed asynchronous accounting start response. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1734298148}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[处理异步计费开始应答，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1215907272}*[contextID]{lang="FR"}*[为计费开始应答所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为计费开始应答对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为]{style="font-family:宋体"}[计费开始应答消息的处理结果]{style="font-family:宋体"}

 

[[Processed asynchronous accounting stop response. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1789803534}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[处理异步计费结束应答，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1392115386}*[contextID]{lang="FR"}*[为计费结束应答所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为计费结束应答对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为]{style="font-family:宋体"}[计费结束应答消息的处理结果]{style="font-family:宋体"}

 

[[Processed asynchronous accounting update response. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1756817310}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[处理异步计费更新应答，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x84819395}*[contextID]{lang="FR"}*[为计费更新应答所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为计费更新应答对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为]{style="font-family:宋体"}[计费更新应答消息的处理结果]{style="font-family:宋体"}

 

[[Authentication timeout. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1948490797}*[contextID]{lang="FR"}*[; requestID: *requestID*.]{lang="EN-US"}

[[认证请求超时，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1788298073}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[认证请求]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为]{style="font-family:宋体"}[认证请求]{style="font-family:宋体"}[对应的上线请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Begin to add request online node. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1868246306}*[contextID]{lang="FR"}*[; requestID: *requestID*.]{lang="EN-US"}

[[开始进行上线请求处理，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x167704547}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[上线请求]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为]{style="font-family:宋体"}[上线请求]{style="font-family:宋体"}[对应的上线请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Succeeded in adding request online node. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x792398897}*[contextID]{lang="FR"}*[; requestID: *requestID*; username: *username*.]{lang="EN-US"}

[[成功添加上线请求节点，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1650903336}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[上线请求]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为]{style="font-family:宋体"}[上线请求]{style="font-family:宋体"}[对应的上线请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[username]{lang="EN-US"}*[为上线请求的用户名]{style="font-family:宋体"}

 

[[Deleted online node. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x556706505}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[删除上线节点，]{style="font-family:宋体"}]{#struct_0_12438_x2040_116668169}*[contextID]{lang="FR"}*[为上线节点所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为上线节点对应的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Move online node. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1238382548}*[contextID]{lang="FR"}*[; requestID: *requestID*; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[上线请求节点转为上线节点，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1978054456}*[contextID]{lang="FR"}*[为上线请求节点所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为上线请求节点的上线请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为上线节点的上线]{style="font-family:宋体"}[ID]{lang="FR"}[。]{style="font-family:宋体"}

 

[[Activated Context ]{lang="EN-US"}]{#struct_0_12438_x2040_1077980019}*[contextID]{lang="FR"}*[.]{lang="EN-US"}

[[激活]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_12438_x2040_1482044385}[，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为对应的]{style="font-family:宋体"}[Context]{lang="EN-US"}

 

[[Inactivated Context ]{lang="EN-US"}]{#struct_0_12438_x2040_x1543419434}*[contextID]{lang="FR"}*[.]{lang="EN-US"}

[[去激活]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_12438_x2040_690271598}[，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为对应的]{style="font-family:宋体"}[Context]{lang="EN-US"}

 

[[Send offline request to daemon. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1577798749}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向守护进程发送下线请求，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x844334282}*[contextID]{lang="FR"}*[为下线请求所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为请求下线的在线]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为发送请求结果]{style="font-family:宋体"}

 

[[Send online request to daemon. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_1509834377}*[contextID]{lang="FR"}*[; requestID: *requestID*; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向守护进程发送上线请求，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1511519572}*[contextID]{lang="FR"}*[为上线请求所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为请求上线的]{style="font-family:宋体"}[请求]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为发送请求结果]{style="font-family:宋体"}

 

[[Send client IP info to daemon. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x139971397}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[向守护进程发送客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12438_x2040_2050453094}[，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为客户端对应的在线]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}*[result]{lang="FR"}*[为发送结果]{style="font-family:宋体"}

 

[[Failed to get the common name from the certificate.]{lang="EN-US"}]{#struct_0_12438_x2040_1884549073}

[[从证书中获取]{style="font-family:宋体"}[common name]{lang="EN-US"}]{#struct_0_12438_x2040_1110722189}[失败]{style="font-family:宋体"}

 

[[Certificate common name is *name*.]{lang="EN-US"}]{#struct_0_12438_x2040_1728453510}

[[证书中的]{style="font-family:宋体"}[common name]{lang="EN-US"}]{#struct_0_12438_x2040_1093439789}[为]{style="font-family:宋体"}*[name]{lang="EN-US"}*

 

[[Certificate authentication succeeded. contextID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x683721026}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[证书认证成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_318465132}*[contextID]{lang="FR"}*[为所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为对应的在线]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[User *name* authentication request.]{lang="EN-US"}]{#struct_0_12438_x2040_x1584143409}

[[用户认证请求，]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_12438_x2040_1026080293}[为发起认证请求的用户名]{style="font-family:宋体"}

 

[[Web login request.]{lang="EN-US"}]{#struct_0_12438_x2040_340407255}

[[通过浏览器发起登录请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1247618809}

 

[[Failed to get request content from web.]{lang="EN-US"}]{#struct_0_12438_x2040_1239002098}

[[处理浏览器登录请求，获取请求信息失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x613810616}

 

[[Web logout request.]{lang="EN-US"}]{#struct_0_12438_x2040_1761989409}

[[通过浏览器发起登出请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_1125034186}

 

[[Online check. No session ID.]{lang="EN-US"}]{#struct_0_12438_x2040_x89169556}

[[上线检查处理，获取]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_12438_x2040_1108182074}[会话信息失败]{style="font-family:宋体"}

 

[[Online check. sessionID: *sessionID*.]{lang="EN-US"}]{#struct_0_12438_x2040_x533644648}

[[上线检查处理，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x902426516}[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[sessionID]{lang="EN-US"}*

 

[[Online check. onlineID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x441049755}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[上线检查处理，用户上线]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_12438_x2040_x238605864}[为]{style="font-family:宋体"}*[onlineID]{lang="FR"}*

 

[[Failed to get MIME when log in.]{lang="EN-US"}]{#struct_0_12438_x2040_x1790010416}

[[处理客户端登录请求时，分配]{style="font-family:宋体"}[MIME]{lang="EN-US"}]{#struct_0_12438_x2040_778295907}[失败]{style="font-family:宋体"}

 

[[Failed to get request content when log in.]{lang="EN-US"}]{#struct_0_12438_x2040_1481330082}

[[处理客户端登录请求时，获取请求信息失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1794148467}

 

[[Authentication request. result: ]{lang="EN-US"}]{#struct_0_12438_x2040_1179770269}*[result]{lang="FR"}*[; client MAC: *mac-address*; private info length: *length*.]{lang="EN-US"}

[[认证请求信息，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x2035665748}*[result]{lang="FR"}*[为获取请求信息的结果，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为客户端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[length]{lang="EN-US"}*[为私有信息长度]{style="font-family:宋体"}

 

[[Client login request.]{lang="EN-US"}]{#struct_0_12438_x2040_x84753859}

[[通过客户端发起登录请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1773423088}

 

[[Client logout request.]{lang="EN-US"}]{#struct_0_12438_x2040_846443176}

[[通过客户端发起登出请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_7266694}

 

[[Client online check. onlineID: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1650837800}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[客户端上线检查，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1791787755}*[onlineID]{lang="FR"}*[客户端对应的用户在线]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Authentication success. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1452329697}*[contextID]{lang="FR"}*[; requestID: *requestID*.]{lang="EN-US"}

[[认证成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_602427449}*[contextID]{lang="FR"}*[为认证所在的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[认证成功的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[The number of online users has reached the limit. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_1078045555}*[contextID]{lang="FR"}*[; requestID: *requestID*.]{lang="EN-US"}

[[在线用户数目已经达到最大数，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1820290341}*[contextID]{lang="FR"}*[为达到在线用户数上限的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为当前请求上线的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Authentication failed. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_x893177258}*[contextID]{lang="FR"}*[; requestID: *requestID*; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[认证失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x844268746}*[contextID]{lang="FR"}*[为认证失败的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为当前请求上线的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[为失败原因]{style="font-family:宋体"}

 

[[Authorization succeeded context: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1307855488}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; policy group: *PGroupid*.]{lang="EN-US"}

[[授权成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1024894540}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[授权成功]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[PGroupid]{lang="EN-US"}*[为授权的策略组]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Succeeded in refreshing authorization information. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_1963724073}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; policy group: *PGroupid*.]{lang="EN-US"}

[[成功更新授权信息，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1884614609}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[授权]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[PGroupid]{lang="EN-US"}*[为授权更新后的策略组]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Authorization failed. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_1459702172}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[授权失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1407763583}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[授权]{style="font-family:宋体"}[失败的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[为失败原因]{style="font-family:宋体"}

 

[[Accounting succeeded. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_318530668}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[计费成功，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1130256333}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[计费成功]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Accounting failed. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_1044982820}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[; result: ]{lang="EN-US"}*[result]{lang="FR"}*[.]{lang="EN-US"}

[[计费失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1010981239}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[计费]{style="font-family:宋体"}[失败的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前请求上线的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[为失败原因]{style="font-family:宋体"}

 

[[Offline process. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_x1247553273}*[contextID]{lang="FR"}*[; onlineID: ]{lang="EN-US"}*[onlineID]{lang="FR"}*[.]{lang="EN-US"}

[[下线处理，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1920394738}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[下线处理]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为当前在线的]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Failed to allocate onlineID. context: ]{lang="EN-US"}]{#struct_0_12438_x2040_1921801012}*[contextID]{lang="FR"}*[; requestID: *requestID*.]{lang="EN-US"}

[[分配在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_12438_x2040_1125099722}[失败，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[分配在线用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为当前请求上线的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging sslvpn error]{lang="FR"}]{#struct_0_12438_x2040_x2143007403}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1738519503}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_1425158710}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_x622471014}

[[Failed to send authentication error to kernel. contextID: *contextID*; requestID: ]{lang="FR"}*[requestID]{lang="EN-US"}*]{#struct_0_12438_x2040_1751348723}[.]{lang="FR"}

[[通知内核认证失败时发生错误，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x2033333751}*[contextID]{lang="FR"}*[为]{style="font-family:宋体"}[认证请求]{style="font-family:宋体"}[的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="EN-US"}*[为请求上线的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Failed to send context *contextID* idle timer to kernel.]{lang="FR"}]{#struct_0_12438_x2040_1863987609}

[[空闲定时器超时，通知内核失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1818787102}*[contextID]{lang="FR"}*[为定时器所在的]{style="font-family:宋体"}[Context]{lang="FR"}

 

[[Failed to send context ]{lang="EN-US"}]{#struct_0_12438_x2040_774293276}*[contextID]{lang="FR"}*[ authentication exception timer to kernel.]{lang="EN-US"}

[[认证请求异常定时器超时，通知内核失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x696434172}*[contextID]{lang="FR"}*[为定时器所在的]{style="font-family:宋体"}[Context]{lang="FR"}

 

[[DNS query *hostname* failed.]{lang="EN-US"}]{#struct_0_12438_x2040_x235407209}

[[DNS]{lang="EN-US"}]{#struct_0_12438_x2040_x440984219}[查找失败，]{style="font-family:宋体"}*[hostname]{lang="EN-US"}*[为要查找的主机名]{style="font-family:宋体"}

 

[[DNS connection closed.]{lang="EN-US"}]{#struct_0_12438_x2040_167264072}

[[与]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_12438_x2040_1712927938}[的连接断开]{style="font-family:宋体"}

 

[[Failed to create the data of SSL server policy *ssl-policy*.]{lang="EN-US"}]{#struct_0_12438_x2040_x372279143}

[[根据服务器策略生成]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x921638810}[数据失败，]{style="font-family:宋体"}*[ssl-policy]{lang="EN-US"}*[为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略名]{style="font-family:宋体"}

 

[[Failed to send the data of SSL server policy *ssl-policy*. error code: *error-code*; total length: *length1*; sent length: *length2*; sending length *length3*.]{lang="EN-US"}]{#struct_0_12438_x2040_x924866959}

[[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x363784031}[数据下内核失败，]{style="font-family:宋体"}*[ssl-policy]{lang="EN-US"}*[为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略名，]{style="font-family:宋体"}*[error-code]{lang="EN-US"}*[为下内核失败原因，]{style="font-family:宋体"}*[length1]{lang="EN-US"}*[为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[数据的总长度，]{style="font-family:宋体"}*[length2]{lang="EN-US"}*[为已经下内核的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[数据长度，]{style="font-family:宋体"}*[length3]{lang="EN-US"}*[为发生失败时下内核的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[数据长度。]{style="font-family:宋体"}

 

[[Failed to add port forward list to kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_1615197142}

[[通知内核添加端口转发列表失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1481395618}

 

[[Failed to delete port forward list from kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_x1429291363}

[[通知内核删除端口转发列表失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_3089147}

 

[[Failed to add local port to kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_x320617147}

[[通知内核添加]{style="font-family:宋体"}[local port]{lang="EN-US"}]{#struct_0_12438_x2040_x1577349885}[配置失败]{style="font-family:宋体"}

 

[[Failed to delete local port from kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_683594349}

[[通知内核删除]{style="font-family:宋体"}[local port]{lang="EN-US"}]{#struct_0_12438_x2040_1484287183}[配置失败]{style="font-family:宋体"}

 

[[Failed to add refer port forward to kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_x124529283}

[[通知内核添加]{style="font-family:宋体"}[port forward list]{lang="EN-US"}]{#struct_0_12438_x2040_x2089674060}[引用配置失败]{style="font-family:宋体"}

 

[[Failed to delete refer port forward from kernel.]{lang="EN-US"}]{#struct_0_12438_x2040_x84688323}

[[通知内核删除]{style="font-family:宋体"}[port forward list]{lang="EN-US"}]{#struct_0_12438_x2040_x2137416392}[引用配置失败]{style="font-family:宋体"}

 

[[Failed to send ]{lang="EN-US"}]{#struct_0_12438_x2040_x300765361}[validated ]{lang="FR"}[code timer to kernel.]{lang="EN-US"}

[[验证码定时器超时，通知内核失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1822242954}

 

[[Failed to update input statistic.]{lang="EN-US"}]{#struct_0_12438_x2040_1900748123}

[[更新]{style="font-family:宋体"}[input]{lang="EN-US"}]{#struct_0_12438_x2040_x1866479517}[方向统计信息失败]{style="font-family:宋体"}

 

[[Link output with invalid index.]{lang="EN-US"}]{#struct_0_12438_x2040_x1552009485}

[[IPAC]{lang="EN-US"}]{#struct_0_12438_x2040_x1650772264}[转发业务中收到报文的出接口为非法接口索引]{style="font-family:宋体"}

 

[[The number of loops (*LoopTimes*) reached the limit.]{lang="EN-US"}]{#struct_0_12438_x2040_x1047864297}

[[报文在本机环回的次数达到上限，]{style="font-family:宋体"}*[LoopTimes]{lang="EN-US"}*]{#struct_0_12438_x2040_1650687601}[为报文在本机的环回次数]{style="font-family:宋体"}

 

[[Failed to load result *ResultCode* (*language*) string.]{lang="EN-US"}]{#struct_0_12438_x2040_967636113}

[[加载输出信息失败，]{style="font-family:宋体"}*[ResultCode]{lang="EN-US"}*]{#struct_0_12438_x2040_x93725037}[为错误码，]{style="font-family:宋体"}*[language]{lang="EN-US"}*[为加载语言]{style="font-family:宋体"}

 

[[Failed to set cookie svpnuid *sessionID*.]{lang="EN-US"}]{#struct_0_12438_x2040_x379461142}

[[设置]{style="font-family:宋体"}[Cookie]{lang="EN-US"}]{#struct_0_12438_x2040_1078111091}[失败，]{style="font-family:宋体"}*[sessionID]{lang="EN-US"}*[为要设置到]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[中的会话]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Failed to set the header of client connection response.]{lang="EN-US"}]{#struct_0_12438_x2040_x1417887674}

[[设置客户端连接应答报文的首部失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x171472764}

 

[[Failed to add a context.]{lang="EN-US"}]{#struct_0_12438_x2040_x1083380805}

[[添加]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_12438_x2040_1025414923}[失败]{style="font-family:宋体"}

 

[[Failed to add a refrenced gateway for the context.]{lang="FR"}]{#struct_0_12438_x2040_x1408671502}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1549294451}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to delete a reference gateway from the context.]{lang="FR"}]{#struct_0_12438_x2040_x844203210}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_1104649232}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[失败。]{style="font-family:宋体"}

 

[[Failed to modify context gateway..]{lang="FR"}]{#struct_0_12438_x2040_x1820639976}

[[修改]{style="font-family:宋体"}]{#struct_0_12438_x2040_x407567267}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[失败。]{style="font-family:宋体"}

 

[[Failed to enable a context.]{lang="FR"}]{#struct_0_12438_x2040_x24555754}

[[Context]{lang="FR"}]{#struct_0_12438_x2040_1884680145}[使能失败]{style="font-family:宋体"}

 

[[Failed to enable validated code.]{lang="FR"}]{#struct_0_12438_x2040_1100969772}

[[验证码使能失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x777634759}

 

[[Failed to enable dynamic password.]{lang="FR"}]{#struct_0_12438_x2040_x309406415}

[[动态口令使能失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1685904023}

 

[[Failed to disable dynamic password.]{lang="FR"}]{#struct_0_12438_x2040_318596204}

[[动态口令去使能失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1948288151}

 

[[Failed to enable certificate anthentication function.]{lang="FR"}]{#struct_0_12438_x2040_x1005721357}

[[使能证书认证功能失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1809644776}

 

[[Failed to disable certificate anthentication function.]{lang="FR"}]{#struct_0_12438_x2040_19293641}

[[关闭证书认证功能失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1247487737}

 

[[Failed to add default policy group.]{lang="FR"}]{#struct_0_12438_x2040_218807558}

[[添加缺省策略组失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1229304304}

 

[[Failed to delete default policy group.]{lang="FR"}]{#struct_0_12438_x2040_1228235159}

[[删除缺省策略组失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1120283052}

 

[[Failed to modify the max number of users.]{lang="FR"}]{#struct_0_12438_x2040_1552219372}

[[修改最大用户数失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1125165258}

 

[[Failed to process vpn instance in context.]{lang="FR"}]{#struct_0_12438_x2040_1062786549}

[[Context]{lang="FR"}]{#struct_0_12438_x2040_x374075631}[下处理]{style="font-family:宋体"}**[vpn-instance]{lang="FR"}**[命令失败]{style="font-family:宋体"}

 

[[Failed to add an EMO (Endpoint Mobile Office) server.]{lang="FR"}]{#struct_0_12438_x2040_71524205}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_x440918683}[EMO]{lang="FR"}[服务器失败]{style="font-family:宋体"}

 

[[Failed to delete an EMO (Endpoint Mobile Office) server.]{lang="EN-US"}]{#struct_0_12438_x2040_2106766995}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_2016215159}[EMO]{lang="FR"}[服务器失败]{style="font-family:宋体"}

 

[[Failed to enable context log.]{lang="FR"}]{#struct_0_12438_x2040_x800238032}

[[使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_308123029}[Context]{lang="FR"}[下的]{style="font-family:宋体"}[syslog]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to disable context log.]{lang="FR"}]{#struct_0_12438_x2040_1481461154}

[[去使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1392841852}[Context]{lang="FR"}[下的]{style="font-family:宋体"}[syslog]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to set redirect response of client.]{lang="FR"}]{#struct_0_12438_x2040_x77627772}

[[设置客户端重定向应答报文失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_8800481}

 

[[Failed to set the header of client domain list. response]{lang="FR"}]{#struct_0_12438_x2040_x84622787}

[[设置客户端]{style="font-family:宋体"}[domain list]{lang="EN-US"}]{#struct_0_12438_x2040_x2101360226}[应答报文的首部失败]{style="font-family:宋体"}

 

[[Failed to get gateway when getting client information.]{lang="FR"}]{#struct_0_12438_x2040_x1319341503}

[[处理客户端信息时，获取]{style="font-family:宋体"}]{#struct_0_12438_x2040_x631049173}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get the match context when getting client information.]{lang="FR"}]{#struct_0_12438_x2040_424350186}

[[处理客户端信息时，获取匹配的]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1650706728}[Context]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get URL when processing domain list request.]{lang="FR"}]{#struct_0_12438_x2040_x406808175}

[[处理]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1628006725}[domain list]{lang="FR"}[请求报文，获取]{style="font-family:宋体"}[URL]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get gateway when checking web query.]{lang="FR"}]{#struct_0_12438_x2040_1078176627}

[[浏览器登录，检查请求信息时，获取]{style="font-family:宋体"}]{#struct_0_12438_x2040_x655953784}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to match context when checking web query.]{lang="FR"}]{#struct_0_12438_x2040_303732004}

[[浏览器登录，检查请求信息时，匹配]{style="font-family:宋体"}]{#struct_0_12438_x2040_2056064052}[Context]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get URL when processing input header.]{lang="EN-US"}]{#struct_0_12438_x2040_x844137674}

[[处理报文首部时，获取]{style="font-family:宋体"}]{#struct_0_12438_x2040_x453981761}[URL]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get URL when processing error web.]{lang="FR"}]{#struct_0_12438_x2040_546274893}

[[浏览器请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_x951542118}[error]{lang="FR"}[页面，获取]{style="font-family:宋体"}[URL]{lang="FR"}[失败。]{style="font-family:宋体"}

 

[[Failed to get URL when checking context for web.]{lang="FR"}]{#struct_0_12438_x2040_1884745681}

[[浏览器访问，检查]{style="font-family:宋体"}]{#struct_0_12438_x2040_x119947760}[Context]{lang="FR"}[是否使能时，获取]{style="font-family:宋体"}[URL]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get gateway when match context.]{lang="FR"}]{#struct_0_12438_x2040_x1561573481}

[[匹配]{style="font-family:宋体"}]{#struct_0_12438_x2040_x723411924}[Context]{lang="FR"}[时获取]{style="font-family:宋体"}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to deliver parse body.]{lang="FR"}]{#struct_0_12438_x2040_318661740}

[[分发解析报文体失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1336554237}

 

[[Failed to find pattern for deliver.]{lang="FR"}]{#struct_0_12438_x2040_761604504}

[[报文分发时，查找匹配模式失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_735857011}

 

[[Failed to build pattern string *string*.]{lang="FR"}]{#struct_0_12438_x2040_x1247422201}

[[构建模式匹配信息失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_928729289}*[string]{lang="FR"}*[为要匹配的字符串]{style="font-family:宋体"}

 

[[Failed to set HTTP header field.]{lang="FR"}]{#struct_0_12438_x2040_x493310963}

[[封装]{style="font-family:宋体"}]{#struct_0_12438_x2040_1125230794}[HTTP]{lang="FR"}[报文头域失败]{style="font-family:宋体"}

 

[[Invalid method in request.]{lang="FR"}]{#struct_0_12438_x2040_x911395815}

[[请求报文中的方法非法]{style="font-family:宋体"}]{#struct_0_12438_x2040_x84922354}

 

[[Failed to get user name.]{lang="FR"}]{#struct_0_12438_x2040_32349197}

[[获取用户名失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x440853147}

 

[[Failed to add user name.]{lang="FR"}]{#struct_0_12438_x2040_x1779262157}

[[添加用户名失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1069898002}

 

[[Failed to get host header.]{lang="FR"}]{#struct_0_12438_x2040_1481526690}

[[获取]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1011523570}[host]{lang="FR"}[首部失败]{style="font-family:宋体"}

 

[[Failed to add host header.]{lang="FR"}]{#struct_0_12438_x2040_x145322473}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_x84557251}[host]{lang="FR"}[首部失败]{style="font-family:宋体"}

 

[[Failed to get host name.]{lang="FR"}]{#struct_0_12438_x2040_x2039535622}

[[获取主机名失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x518347027}

 

[[Failed to add host name.]{lang="FR"}]{#struct_0_12438_x2040_x1650641192}

[[添加主机名失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1470628269}

 

[[Failed to add time data.]{lang="FR"}]{#struct_0_12438_x2040_x1116368921}

[[添加时间信息失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1078242163}

 

[[Failed to add data to MBUF.]{lang="FR"}]{#struct_0_12438_x2040_510598785}

[[向]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1388744787}[MBUF]{lang="FR"}[添加数据失败]{style="font-family:宋体"}

 

[[Failed to get file becaust user had no authority.]{lang="FR"}]{#struct_0_12438_x2040_x844072138}

[[获取文件失败，失败原因是用户没有权限]{style="font-family:宋体"}]{#struct_0_12438_x2040_1091708725}

 

[[Failed to open file.]{lang="FR"}]{#struct_0_12438_x2040_1019720566}

[[打开文件失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1884811217}

 

[[Failed to get file state.]{lang="FR"}]{#struct_0_12438_x2040_1097657092}

[[获取文件状态失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x971518707}

 

[[Failed to read file file.]{lang="FR"}]{#struct_0_12438_x2040_318727276}

[[读取文件失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1271757450}

 

[[Failed to add a gateway.]{lang="FR"}]{#struct_0_12438_x2040_x1926418388}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1247356665}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to set gateway IP address.]{lang="FR"}]{#struct_0_12438_x2040_x1502192024}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_1270440353}[Gateway]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址失败]{style="font-family:
  宋体"}

 

[[Failed to enable a gateway.]{lang="FR"}]{#struct_0_12438_x2040_1125296330}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_1434209001}[使能失败]{style="font-family:宋体"}

 

[[Failed to set SSL server policy.]{lang="FR"}]{#struct_0_12438_x2040_x1646443110}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x440787611}[SSL]{lang="FR"}[服务器端策略失败]{style="font-family:宋体"}

 

[[Failed to set HTTP redirect.]{lang="FR"}]{#struct_0_12438_x2040_969198187}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x610139385}[HTTP]{lang="FR"}[重定向失败]{style="font-family:宋体"}

 

[[Failed to clear HTTP redirect.]{lang="FR"}]{#struct_0_12438_x2040_1481592226}

[[清除]{style="font-family:宋体"}]{#struct_0_12438_x2040_1707904407}[HTTP]{lang="FR"}[重定向失败]{style="font-family:宋体"}

 

[[Failed to process vpn instance in gateway.]{lang="FR"}]{#struct_0_12438_x2040_x84491715}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_1505348265}[下处理]{style="font-family:宋体"}**[vpn-instance]{lang="FR"}**[命令失败]{style="font-family:宋体"}

 

[[Failed to find context *id*.]{lang="FR"}]{#struct_0_12438_x2040_1026410726}

[[查找]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1650575656}[Context]{lang="FR"}[失败，]{style="font-family:宋体"}*[id]{lang="FR"}*[为要查找的]{style="font-family:宋体"}[Context ID]{lang="FR"}

 

[[Failed to add a route list *id*.]{lang="FR"}]{#struct_0_12438_x2040_1946153693}

[[添加路由列表失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1607413995}*[id]{lang="FR"}*[为路由列表的]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to add a route to route list *id*.]{lang="FR"}]{#struct_0_12438_x2040_1078307699}

[[向路由列表添加路由失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_924875818}*[id]{lang="FR"}*[为路由列表的]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to update output statistics.]{lang="FR"}]{#struct_0_12438_x2040_x1461123491}

[[更新出方向统计信息失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x844006602}

 

[[IPAC: Failed to get IP packet information.]{lang="FR"}]{#struct_0_12438_x2040_1109677256}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1884876753}[代理：获取报文]{style="font-family:宋体"}[IP]{lang="FR"}[信息失败]{style="font-family:宋体"}

 

[[IPAC: Failed to get match IP form ACL.]{lang="FR"}]{#struct_0_12438_x2040_x1670946909}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_318792812}[代理：获取匹配的]{style="font-family:宋体"}[ACL]{lang="FR"}[规则失败]{style="font-family:宋体"}

 

[[IPAC: Failed to check ip tunnel acl.]{lang="FR"}]{#struct_0_12438_x2040_692635891}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1419098767}[代理：]{style="font-family:宋体"}[ACL]{lang="FR"}[规则检查失败]{style="font-family:宋体"}

 

[[IPAC: IP connection error.]{lang="FR"}]{#struct_0_12438_x2040_x1247291129}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1798987245}[代理：连接错误]{style="font-family:宋体"}

 

[[IPAC: Failed to receive data from IP connection.]{lang="FR"}]{#struct_0_12438_x2040_x1464715731}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1125361866}[代理：从连接上接收数据失败]{style="font-family:宋体"}

 

[[IPAC: Failed to add data to packet. length: *length*; value: *value*.]{lang="FR"}]{#struct_0_12438_x2040_1477617820}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x440722075}[代理：向报文中添加数据失败，]{style="font-family:宋体"}*[length]{lang="FR"}*[为要添加的数据长度，]{style="font-family:宋体"}*[value]{lang="FR"}*[为要添加的数据内容]{style="font-family:宋体"}

 

[[IPAC: Failed to get gateway address.]{lang="FR"}]{#struct_0_12438_x2040_1731930170}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1727130632}[代理：获取]{style="font-family:宋体"}[Gateway]{lang="FR"}[地址失败]{style="font-family:宋体"}

 

[[IPAC: Failed to get server.]{lang="FR"}]{#struct_0_12438_x2040_x22405401}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1524772359}[代理：获取]{style="font-family:宋体"}[Server]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[IPAC: Failed to get IP resource.]{lang="FR"}]{#struct_0_12438_x2040_1543678540}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1764693913}[代理：获取]{style="font-family:宋体"}[IP]{lang="FR"}[代理资源失败]{style="font-family:宋体"}

 

[[IPAC: Failed to hand shake because VPN instance does not exist.]{lang="FR"}]{#struct_0_12438_x2040_x1185204815}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x354399930}[代理：握手协商失败，原因是]{style="font-family:宋体"}[VPN]{lang="FR"}[不存在]{style="font-family:宋体"}

 

[[IPAC: Failed to allocate IP address.]{lang="FR"}]{#struct_0_12438_x2040_x1208016280}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_380879126}[代理：分配]{style="font-family:宋体"}[IP]{lang="FR"}[地址失败]{style="font-family:宋体"}

 

[[IPAC: Failed to add peer.]{lang="FR"}]{#struct_0_12438_x2040_x574386136}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1991773869}[代理：添加]{style="font-family:宋体"}[Peer]{lang="FR"}[数据失败]{style="font-family:宋体"}

 

[[IPAC: Failed to send reply packet.]{lang="FR"}]{#struct_0_12438_x2040_x456594157}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_705896451}[代理：发送应答报文失败]{style="font-family:宋体"}

 

[[Failed to reference an address pool.]{lang="FR"}]{#struct_0_12438_x2040_x425689928}

[[引用地址池失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1140394013}

 

[[Failed to add a policy group.]{lang="FR"}]{#struct_0_12438_x2040_625897870}

[[添加策略组失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1588489342}

 

[[Failed to add an address pool.]{lang="FR"}]{#struct_0_12438_x2040_x1982474783}

[[添加地址池失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x693196649}

 

[[Failed to add a port forward list *id*.]{lang="FR"}]{#struct_0_12438_x2040_x378635761}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_1738039444}[端口转发列表失败，]{style="font-family:宋体"}*[id]{lang="EN-US"}*[为端口转发列表的]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[Failed to add a local port *port*.]{lang="FR"}]{#struct_0_12438_x2040_1187448180}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_682807838}[local port]{lang="FR"}[失败，]{style="font-family:宋体"}*[port]{lang="FR"}*[为要添加的本地端口]{style="font-family:宋体"}

 

[[Failed to add local port node in kernel resource.]{lang="FR"}]{#struct_0_12438_x2040_x22339865}

[[内核资源添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_801547732}[local port]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[HTTP Redirect: Failed to get gateway.]{lang="FR"}]{#struct_0_12438_x2040_1543744076}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_1424584961}[重定向：获取]{style="font-family:宋体"}[Gateway]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[HTTP Redirect: Failed to get gateway port.]{lang="FR"}]{#struct_0_12438_x2040_x2117639989}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_x1185139279}[重定向：获取]{style="font-family:宋体"}[Gateway]{lang="FR"}[的端口失败]{style="font-family:宋体"}

 

[[HTTP Redirect: Received request without host.]{lang="FR"}]{#struct_0_12438_x2040_380944662}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_x1384577760}[重定向：接收的请求报文中没有]{style="font-family:宋体"}[host]{lang="FR"}[首部]{style="font-family:宋体"}

 

[[HTTP Redirect: Received request without URI.]{lang="FR"}]{#struct_0_12438_x2040_x1991708333}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_1953607863}[重定向：接收的请求报文中没有]{style="font-family:宋体"}[URI]{lang="FR"}[信息]{style="font-family:宋体"}

 

[[HTTP Redirect: Failed to create response packet.]{lang="FR"}]{#struct_0_12438_x2040_x425624392}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_215166773}[重定向：创建应答报文失败]{style="font-family:宋体"}

 

[[HTTP Redirect: Failed to set header.]{lang="FR"}]{#struct_0_12438_x2040_412280980}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_1140459549}[重定向：封装首部信息失败]{style="font-family:宋体"}

 

[[Failed to find resource list: *id*.]{lang="FR"}]{#struct_0_12438_x2040_x970302271}

[[获取资源列表失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1588423806}*[id]{lang="FR"}*[为列表]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to add resource list in kernel. listID: *id*.]{lang="FR"}]{#struct_0_12438_x2040_1144746194}

[[内核资源添加资源列表失败，]{style="font-family:宋体"}]{#struct_0_12438_x2040_x378570225}*[id]{lang="FR"}*[为列表]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Loading other SSL server policy *name*.]{lang="FR"}]{#struct_0_12438_x2040_576258654}

[[正在下发其他]{style="font-family:宋体"}]{#struct_0_12438_x2040_1187513716}[SSL]{lang="FR"}[服务器端策略，]{style="font-family:宋体"}*[name]{lang="FR"}*[为正在下发的]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略名]{style="font-family:宋体"}

 

[[Updating SSL server policy *name* with invalid offset.]{lang="FR"}]{#struct_0_12438_x2040_1460798005}

[[下发更新]{style="font-family:宋体"}]{#struct_0_12438_x2040_x22274329}[SSL]{lang="FR"}[服务器端策略时，数据偏移错误，]{style="font-family:宋体"}*[name]{lang="FR"}*[为正在下发的]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略名]{style="font-family:宋体"}

 

[[Failed to set SSL server context.]{lang="FR"}]{#struct_0_12438_x2040_x735486123}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_1543809612}[SSL]{lang="FR"}[服务策略上下文数据失败]{style="font-family:宋体"}

 

[[Invalid SSL data length.]{lang="FR"}]{#struct_0_12438_x2040_x1381213119}

[[SL]{lang="FR"}]{#struct_0_12438_x2040_x1185073743}[服务策略文数据长度非法]{style="font-family:宋体"}

 

[[Failed to create SSL server policy *name.*]{lang="FR"}]{#struct_0_12438_x2040_1948481532}

[[创建]{style="font-family:宋体"}]{#struct_0_12438_x2040_381010198}[SSL]{lang="FR"}[服务器端策略失败，]{style="font-family:宋体"}*[name]{lang="FR"}*[为要创建的]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略名]{style="font-family:宋体"}

 

[[Static redirect error.]{lang="FR"}]{#struct_0_12438_x2040_x662468639}

[[静态页面重定向错误]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1991642797}

 

[[Static set head field failed.]{lang="FR"}]{#struct_0_12438_x2040_x1195896917}

[[静态页面设置头域错误]{style="font-family:宋体"}]{#struct_0_12438_x2040_x425558856}

 

[[Static receive request with invalid method.]{lang="FR"}]{#struct_0_12438_x2040_1140525085}

[[静态页面收到的请求报文携带了非法的方法]{style="font-family:宋体"}]{#struct_0_12438_x2040_x912464534}

 

[[Failed to set login message.]{lang="FR"}]{#struct_0_12438_x2040_x1588358270}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x268647431}[login]{lang="FR"}[信息失败]{style="font-family:宋体"}

 

[[Failed to set title message.]{lang="FR"}]{#struct_0_12438_x2040_x378504689}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_2138559700}[title]{lang="FR"}[信息失败]{style="font-family:宋体"}

 

[[Failed to set logo.]{lang="FR"}]{#struct_0_12438_x2040_1187579252}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_1070876303}[logo]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to add VPN instance *id*.]{lang="FR"}]{#struct_0_12438_x2040_x22208793}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_1652198362}[VPN]{lang="FR"}[实例失败，]{style="font-family:宋体"}*[id]{lang="FR"}*[为]{style="font-family:宋体"}[VPN]{lang="FR"}[实例]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[WebAC: Failed to get source IP address.]{lang="FR"}]{#struct_0_12438_x2040_1543875148}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1812129024}[代理：获取源]{style="font-family:宋体"}[IP]{lang="FR"}[地址失败]{style="font-family:宋体"}

 

[[WebAC: Failed to get match ip form acl.]{lang="FR"}]{#struct_0_12438_x2040_x1185008207}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1166696454}[代理：匹配]{style="font-family:宋体"}[ACL]{lang="FR"}[规则失败]{style="font-family:宋体"}

 

[[WebAC: Failed to check authorization.]{lang="FR"}]{#struct_0_12438_x2040_381075734}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1640853861}[代理：检查授权失败]{style="font-family:宋体"}

 

[[WebAC: Failed to connect server.]{lang="FR"}]{#struct_0_12438_x2040_x1991577261}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x425493320}[代理：连接服务器失败]{style="font-family:宋体"}

 

[[WebAC: Failed to create FTCP connection.]{lang="FR"}]{#struct_0_12438_x2040_2122342187}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1140590621}[代理：创建]{style="font-family:宋体"}[FTCP]{lang="FR"}[连接失败]{style="font-family:宋体"}

 

[[WebAC: Failed to resolve server name.]{lang="FR"}]{#struct_0_12438_x2040_1804354353}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x1588292734}[代理：解析服务器域名失败]{style="font-family:宋体"}

 

[[WebAC: Failed to get request URL.]{lang="FR"}]{#struct_0_12438_x2040_283468484}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x378439153}[代理：获取请求]{style="font-family:宋体"}[URL]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[WebAC: Failed to parse request URL.]{lang="FR"}]{#struct_0_12438_x2040_203352335}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1187644788}[代理：解析请求]{style="font-family:宋体"}[URL]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[WebAC: Server host name was too long.]{lang="FR"}]{#struct_0_12438_x2040_x22143257}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x2123699565}[代理：服务器主机名超长]{style="font-family:宋体"}

 

[[WebAC: Failed to allocate WebAC.]{lang="FR"}]{#struct_0_12438_x2040_1543940684}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x162315594}[代理：申请]{style="font-family:宋体"}[Web]{lang="FR"}[代理节点失败]{style="font-family:宋体"}

 

[[WebAC: Failed to run finite state machine.]{lang="FR"}]{#struct_0_12438_x2040_x1184942671}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_381141270}[代理：运行有限状态机失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get TCPAC node index.]{lang="FR"}]{#struct_0_12438_x2040_x1840507919}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1991511725}[代理：获取]{style="font-family:宋体"}[TCP]{lang="FR"}[代理节点索引失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to response TCP client.]{lang="FR"}]{#struct_0_12438_x2040_x1879658612}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x425427784}[代理：向]{style="font-family:宋体"}[TCP]{lang="FR"}[客户端回复应答失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to connect remote server.]{lang="FR"}]{#struct_0_12438_x2040_1140656157}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1810139117}[代理：连接远端服务器失败]{style="font-family:宋体"}

 

[[TCPAC: Client connection error.]{lang="FR"}]{#struct_0_12438_x2040_x1588227198}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_2143162447}[代理：与客户端的连接发送错误]{style="font-family:宋体"}

 

[[TCPAC: Failed to resolve server name.]{lang="FR"}]{#struct_0_12438_x2040_x378373617}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1754368326}[代理：解析服务器域名失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get server from HTTP header.]{lang="FR"}]{#struct_0_12438_x2040_1187710324}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x22077721}[代理：从]{style="font-family:宋体"}[HTTP]{lang="FR"}[头域中获取服务器信息失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get server by resource *id.*]{lang="FR"}]{#struct_0_12438_x2040_207916257}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1544006220}[代理：根据资源]{style="font-family:宋体"}[ID]{lang="FR"}[获取服务器信息失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to parse resource.]{lang="FR"}]{#struct_0_12438_x2040_x645560267}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1184877135}[代理：解析资源信息失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to check authorization in handshake.]{lang="FR"}]{#struct_0_12438_x2040_381206806}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1868145013}[代理：握手过程中检查授权失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get source IP address.]{lang="FR"}]{#struct_0_12438_x2040_x1991446189}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1470248109}[代理：获取源]{style="font-family:宋体"}[IP]{lang="FR"}[地址失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get match ip form acl.]{lang="FR"}]{#struct_0_12438_x2040_x425362248}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x378308081}[代理：匹配]{style="font-family:宋体"}[ACL]{lang="FR"}[规则失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get remote server.]{lang="FR"}]{#struct_0_12438_x2040_1187775860}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1369554462}[代理：获取远端服务器失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to get VPN instance.]{lang="FR"}]{#struct_0_12438_x2040_x156295449}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1409788492}[代理：获取]{style="font-family:宋体"}[VPN]{lang="FR"}[实例失败]{style="font-family:宋体"}

 

[[TCPAC: No authority for TCP access.]{lang="FR"}]{#struct_0_12438_x2040_922339418}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1319094863}[代理：]{style="font-family:宋体"}[TCP]{lang="FR"}[接入没有被授权]{style="font-family:宋体"}

 

[[TCPAC: Failed to create TCPAC.]{lang="FR"}]{#struct_0_12438_x2040_246989078}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_2063222347}[代理：创建]{style="font-family:宋体"}[TCP]{lang="FR"}[代理节点失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to connect remote server.]{lang="FR"}]{#struct_0_12438_x2040_x2125663917}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1247864651}[代理：连接远端服务器失败]{style="font-family:宋体"}

 

[[TCPAC: Failed to handshake.]{lang="FR"}]{#struct_0_12438_x2040_x559579976}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1006503965}[代理：]{style="font-family:宋体"}[TCP]{lang="FR"}[握手失败]{style="font-family:宋体"}

 

[[Failed to get context by context ID.]{lang="FR"}]{#struct_0_12438_x2040_x1661489498}

[[根据]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1722379390}[ID]{lang="FR"}[查找]{style="font-family:宋体"}[Context]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to get context by context name.]{lang="FR"}]{#struct_0_12438_x2040_x579760654}

[[根据名字查找]{style="font-family:宋体"}]{#struct_0_12438_x2040_x512525809}[Context]{lang="FR"}[失败]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging sslvpn event]{lang="FR"}]{#struct_0_12438_x2040_x1397739442}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1686858049}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_1001311732}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_1053558132}

[[Succeeded in creating the data of SSL server policy *name*, total length *length*..]{lang="FR"}]{#struct_0_12438_x2040_x747321019}

[[成功创建]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1730574938}[SSL]{lang="FR"}[服务器端策略数据，]{style="font-family:宋体"}*[name]{lang="FR"}*[为]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略名，]{style="font-family:宋体"}*[length]{lang="FR"}*[为创建的数据长度]{style="font-family:宋体"}

 

[[TCPAC connection hasn\'t been created.]{lang="FR"}]{#struct_0_12438_x2040_x1606208894}

[[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_839228779}[代理连接还没有完成]{style="font-family:宋体"}

 

[[Succeeded in adding wadj for *interface-name*.]{lang="EN-US"}]{#struct_0_12438_x2040_x697178340}

[[成功添加指定出接口的邻接表，]{style="font-family:宋体"}*[ interface-name]{lang="EN-US"}*]{#struct_0_12438_x2040_1405583557}[为出接口名称]{style="font-family:宋体"}

 

[[Failed to add wadj for *interface-name*.]{lang="EN-US"}]{#struct_0_12438_x2040_456699561}

[[添加指定出接口的邻接表失败，]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_12438_x2040_799573127}[为出接口名称]{style="font-family:宋体"}

 

[[Succeeded in deleting adj for *interface-name*.]{lang="EN-US"}]{#struct_0_12438_x2040_x156229913}

[[成功删除指定出接口的邻接表，]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_12438_x2040_x771415517}[为出接口名称]{style="font-family:宋体"}

 

[[Failed to delete adj for *interface-name*.]{lang="EN-US"}]{#struct_0_12438_x2040_839606352}

[[删除指定出接口的邻接表失败，]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_12438_x2040_x1318579101}[为出接口名称]{style="font-family:宋体"}

 

[[Succeeded in adding a context.]{lang="EN-US"}]{#struct_0_12438_x2040_810176667}

[[添加]{style="font-family:宋体"}[Context]{lang="EN-US"}]{#struct_0_12438_x2040_801777311}[成功]{style="font-family:宋体"}

 

[[Succeeded in adding context gateway.]{lang="FR"}]{#struct_0_12438_x2040_396542169}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_x198786976}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[成功]{style="font-family:宋体"}

 

[[Succeeded in deleting context gateway.]{lang="FR"}]{#struct_0_12438_x2040_928059261}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_1409854028}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[成功]{style="font-family:宋体"}

 

[[Succeeded in modifying context gateway.]{lang="FR"}]{#struct_0_12438_x2040_x608766640}

[[修改]{style="font-family:宋体"}]{#struct_0_12438_x2040_456514238}[Context]{lang="FR"}[引用]{style="font-family:宋体"}[Gateway]{lang="FR"}[成功]{style="font-family:宋体"}

 

[[Succeeded in enabling a context.]{lang="FR"}]{#struct_0_12438_x2040_x1356126299}

[[Context]{lang="FR"}]{#struct_0_12438_x2040_x1879498430}[使能成功]{style="font-family:宋体"}

 

[[Succeeded in enabling validated code.]{lang="FR"}]{#struct_0_12438_x2040_x1381026918}

[[验证码使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1859575688}[成功]{style="font-family:宋体"}

 

[[Succeeded in enabling dynamic password.]{lang="FR"}]{#struct_0_12438_x2040_850498782}

[[动态口令使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1319029327}[成功]{style="font-family:宋体"}

 

[[Succeeded in disabling dynamic password.]{lang="FR"}]{#struct_0_12438_x2040_x405003249}

[[动态口令去使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1857455137}[成功]{style="font-family:宋体"}

 

[[Succeeded in enabling certificate anthentication.]{lang="FR"}]{#struct_0_12438_x2040_x1348373412}

[[证书认证使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x260133271}[成功]{style="font-family:宋体"}

 

[[Succeeded in disabling certificate anthentication.]{lang="FR"}]{#struct_0_12438_x2040_1976532621}

[[证书认证去使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x978313832}[成功]{style="font-family:宋体"}

 

[[Succeeded in adding a default policy group.]{lang="FR"}]{#struct_0_12438_x2040_247054614}

[[添加缺省策略组]{style="font-family:宋体"}]{#struct_0_12438_x2040_1163650127}[成功]{style="font-family:宋体"}

 

[[Succeeded in deleting the default policy group.]{lang="FR"}]{#struct_0_12438_x2040_1390695304}

[[删除缺省策略组]{style="font-family:宋体"}]{#struct_0_12438_x2040_196458044}[成功]{style="font-family:宋体"}

 

[[Succeeded in modifying the max number of users.]{lang="FR"}]{#struct_0_12438_x2040_213930789}

[[修改最大用户数]{style="font-family:宋体"}]{#struct_0_12438_x2040_86354477}[成功]{style="font-family:宋体"}

 

[[Succeeded in processing VPN instance in context.]{lang="FR"}]{#struct_0_12438_x2040_x2125598381}

[[Context]{lang="FR"}]{#struct_0_12438_x2040_207720720}[下处理]{style="font-family:宋体"}[vpn instance]{lang="FR"}[命令]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in adding an EMO (Endpoint Mobile Office) server.]{lang="FR"}]{#struct_0_12438_x2040_1872916299}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_257486731}[EMO]{lang="FR"}[服务器]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in deleting the EMO (Endpoint Mobile Office) server.]{lang="FR"}]{#struct_0_12438_x2040_x1617465821}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1099349945}[EMO]{lang="FR"}[服务器]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in enabling context log.]{lang="FR"}]{#struct_0_12438_x2040_x559514440}

[[使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1212604415}[Context]{lang="FR"}[下的]{style="font-family:宋体"}[syslog]{lang="FR"}[成功。]{style="font-family:宋体"}

 

[[Succeeded to disabling context log.]{lang="FR"}]{#struct_0_12438_x2040_x1233558116}

[[去使能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1886924158}[Context]{lang="FR"}[下的]{style="font-family:宋体"}[syslog]{lang="FR"}[成功。]{style="font-family:宋体"}

 

[[Request domain list when checking context for web.]{lang="FR"}]{#struct_0_12438_x2040_1724213422}

[[浏览器请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_x575303184}[domain list]{lang="FR"}[页面]{style="font-family:宋体"}

 

[[Request error when checking context for web.]{lang="FR"}]{#struct_0_12438_x2040_1006569501}

[[浏览器请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_2138324154}[error]{lang="FR"}[页面]{style="font-family:宋体"}

 

[[Succeeded in matching the only context.]{lang="FR"}]{#struct_0_12438_x2040_1684944262}

[[成功匹配到唯一引用的]{style="font-family:宋体"}]{#struct_0_12438_x2040_x226801476}[Context]{lang="FR"}

 

[[Succeeded in matching context by virtual-host *host-name*.]{lang="FR"}]{#struct_0_12438_x2040_x968198540}

[[通过虚拟主机名]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1722313854}*[host-name]{lang="FR"}*[成功匹配到]{style="font-family:宋体"}[Context]{lang="FR"}

 

[[Succeeded in matching context by domain *domain-name*.]{lang="FR"}]{#struct_0_12438_x2040_x1615346729}

[[通过域名]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1548103406}*[domain-name]{lang="FR"}*[成功匹配到]{style="font-family:宋体"}[Context]{lang="FR"}

 

[[Succeeded in matching default context.]{lang="FR"}]{#struct_0_12438_x2040_30453328}

[[成功匹配到默认]{style="font-family:宋体"}]{#struct_0_12438_x2040_1409764000}[Context]{lang="FR"}

 

[[Succeeded in saving dynamic web file information.]{lang="FR"}]{#struct_0_12438_x2040_x512460273}

[[成功保存动态]{style="font-family:宋体"}]{#struct_0_12438_x2040_926536355}[Web]{lang="FR"}[页面信息]{style="font-family:宋体"}

 

[[Succeeded in adding a user name *name*.]{lang="FR"}]{#struct_0_12438_x2040_2094649285}

[[成功添加用户名]{style="font-family:宋体"}]{#struct_0_12438_x2040_371864307}*[name]{lang="FR"}*

 

[[Succeeded in adding time *time*.]{lang="FR"}]{#struct_0_12438_x2040_1913429786}

[[成功添加时间信息]{style="font-family:宋体"}]{#struct_0_12438_x2040_1053623668}*[time]{lang="FR"}*

 

[[Succeeded in deleting a user customized file.]{lang="FR"}]{#struct_0_12438_x2040_2026424056}

[[成功删除用户自定义文件]{style="font-family:宋体"}]{#struct_0_12438_x2040_1941001588}

 

[[Succeeded in reading file. read length: *length*.]{lang="FR"}]{#struct_0_12438_x2040_x414336919}

[[成功读取文件，文件长度为]{style="font-family:宋体"}]{#struct_0_12438_x2040_x156164377}*[length]{lang="FR"}*

 

[[Succeeded in enabling a gateway.]{lang="FR"}]{#struct_0_12438_x2040_1178935189}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_x1259040327}[使能]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in disabling a gateway.]{lang="FR"}]{#struct_0_12438_x2040_52792769}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_74244202}[去使能]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in adding a gateway.]{lang="FR"}]{#struct_0_12438_x2040_1409919564}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_1334524984}[Gateway]{lang="FR"}[成功]{style="font-family:宋体"}

 

[[Succeeded in setting gateway IP address.]{lang="FR"}]{#struct_0_12438_x2040_x861650412}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x879812219}[Gateway]{lang="FR"}[的]{style="font-family:宋体"}[IP]{lang="FR"}[地址]{style="font-family:
  宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in enabling a gateway.]{lang="FR"}]{#struct_0_12438_x2040_x1318963791}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_1929845514}[使能成功]{style="font-family:宋体"}

 

[[Succeeded in setting SSL server policy.]{lang="FR"}]{#struct_0_12438_x2040_x1063529210}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x2161959}[SSL]{lang="FR"}[服务器端策略]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in clearing SSL server policy.]{lang="FR"}]{#struct_0_12438_x2040_247120150}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1130318935}[SSL]{lang="FR"}[服务器端策略]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in setting HTTP redirect.]{lang="FR"}]{#struct_0_12438_x2040_x945259009}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x719836641}[HTTP]{lang="FR"}[重定向]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in clearing HTTP redirect.]{lang="FR"}]{#struct_0_12438_x2040_x2125532845}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1689709641}[HTTP]{lang="FR"}[重定向]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in processing VPN instance in gateway.]{lang="FR"}]{#struct_0_12438_x2040_1086019193}

[[Gateway]{lang="FR"}]{#struct_0_12438_x2040_x1068349652}[下处理]{style="font-family:宋体"}[vpn instance]{lang="FR"}[命令]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in adding a route list *id*.]{lang="FR"}]{#struct_0_12438_x2040_x559448904}

[[添加路由列表]{style="font-family:宋体"}]{#struct_0_12438_x2040_1439864672}[成功]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[id]{lang="FR"}*[为路由列表]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Succeeded in adding a route to route list *id*.]{lang="FR"}]{#struct_0_12438_x2040_x327335508}

[[向路由列表添加路由]{style="font-family:宋体"}]{#struct_0_12438_x2040_1006635037}[成功]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[id]{lang="FR"}*[为路由列表]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[IPAC: No IP tunnel acl resource.]{lang="FR"}]{#struct_0_12438_x2040_1011247788}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1542289914}[代理：没有配置]{style="font-family:宋体"}[IP]{lang="FR"}[代理]{style="font-family:宋体"}[ACL]{lang="FR"}[规则]{style="font-family:宋体"}

 

[[IPAC: The ACL check result is *result*.]{lang="FR"}]{#struct_0_12438_x2040_x1761976949}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1722248318}[代理：]{style="font-family:宋体"}[ACL]{lang="FR"}[规则检查结果为]{style="font-family:宋体"}*[result]{lang="FR"}*

 

[[The IP address range is from *start-address* to *end-address* and the mask is *mask*.]{lang="FR"}]{#struct_0_12438_x2040_x1386589809}

[[分配的]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1308833383}[IP]{lang="FR"}[地址范围为从]{style="font-family:宋体"}*[start-address]{lang="FR"}*[到]{style="font-family:宋体"}*[end-address]{lang="FR"}*[，]{style="font-family:宋体"}[IP]{lang="FR"}[地址的掩码为]{style="font-family:
  宋体"}*[mask]{lang="FR"}*

 

[[The first subnet address range is from *start-address* to *end-address*.]{lang="FR"}]{#struct_0_12438_x2040_x512394737}

[[第一个地址子区间]{style="font-family:宋体"}]{#struct_0_12438_x2040_496215236}

 

[[Succeeded in allocating address *ip-address* from *start-address* to *end-address*.]{lang="FR"}]{#struct_0_12438_x2040_x1257822308}

[[从]{style="font-family:宋体"}]{#struct_0_12438_x2040_1293520168}[IP]{lang="FR"}[地址范围]{style="font-family:宋体"}*[start-address]{lang="FR"}*[到]{style="font-family:宋体"}*[end-address]{lang="FR"}*[中成功分配地址]{style="font-family:宋体"}*[ip-address]{lang="FR"}*

 

[[Succeeded in referring all routes.]{lang="FR"}]{#struct_0_12438_x2040_1053689204}

[[成功引用所有路由]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1526377204}

 

[[Succeeded in referring a route.]{lang="FR"}]{#struct_0_12438_x2040_493782569}

[[成功引用一条路由]{style="font-family:宋体"}]{#struct_0_12438_x2040_x156098841}

 

[[Succeeded in refering a route list.]{lang="FR"}]{#struct_0_12438_x2040_x409430407}

[[成功引用一个路由列表]{style="font-family:宋体"}]{#struct_0_12438_x2040_583135586}

 

[[Succeeded in refering an address pool.]{lang="FR"}]{#struct_0_12438_x2040_1409985100}

[[成功引用一个地址池]{style="font-family:宋体"}]{#struct_0_12438_x2040_x248223286}

 

[[Succeeded in clearing an address pool.]{lang="FR"}]{#struct_0_12438_x2040_1336777737}

[[成功清除一个地址池]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1318898255}

 

[[Succeeded in adding a policy group.]{lang="FR"}]{#struct_0_12438_x2040_1232064000}

[[成功添加一个策略组]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1728691537}

 

[[Succeeded in adding an address pool.]{lang="FR"}]{#struct_0_12438_x2040_182724439}

[[成功添加一个地址池]{style="font-family:宋体"}]{#struct_0_12438_x2040_247185686}

 

[[Succeeded in deleting an address pool.]{lang="FR"}]{#struct_0_12438_x2040_x1918180570}

[[成功删除一个地址池]{style="font-family:宋体"}]{#struct_0_12438_x2040_x2125467309}

 

[[Succeeded in adding a port forward list *id*.]{lang="FR"}]{#struct_0_12438_x2040_x2065463609}

[[添加]{style="font-family:宋体"}]{#struct_0_12438_x2040_540406474}[端口转发列表]{style="font-family:宋体"}*[id]{lang="FR"}*[成功]{style="font-family:宋体"}

 

[[Succeeded in deleting a port portfwd list *id*.]{lang="FR"}]{#struct_0_12438_x2040_x559383368}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_306877552}[端口转发列表]{style="font-family:宋体"}*[id]{lang="FR"}*[成功]{style="font-family:宋体"}

 

[[Succeeded in adding a local port *port*.]{lang="FR"}]{#struct_0_12438_x2040_x1966435726}

[[添加本地端口]{style="font-family:宋体"}]{#struct_0_12438_x2040_1006700573}*[port]{lang="FR"}*[成功]{style="font-family:宋体"}

 

[[Succeeded in receiving the data of SSL server policy *name*. total length: *length1*; received length: *length2*; receiving length: *length3*.]{lang="FR"}]{#struct_0_12438_x2040_x933944432}

[[成功接收到]{style="font-family:宋体"}]{#struct_0_12438_x2040_246026379}[SSL]{lang="FR"}[服务器端策略]{style="font-family:宋体"}*[name]{lang="FR"}*[的]{style="font-family:宋体"}[数据]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[length1]{lang="FR"}*[为]{style="font-family:宋体"}[SSL]{lang="FR"}[数据的总长度]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[length2]{lang="FR"}*[为已经接收的]{style="font-family:宋体"}[SSL]{lang="FR"}[数据长度]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[length3]{lang="FR"}*[为正在接收的]{style="font-family:宋体"}[SSL]{lang="FR"}[数据长度]{style="font-family:宋体"}

 

[[Succeeded in setting SSL server context.]{lang="FR"}]{#struct_0_12438_x2040_x1722182782}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x216040443}[SSL]{lang="FR"}[服务策略上下文数据成功]{style="font-family:宋体"}

 

[[Succeeded in setting login message.]{lang="FR"}]{#struct_0_12438_x2040_x2119773771}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x512329201}[login]{lang="FR"}[信息成功]{style="font-family:宋体"}

 

[[Succeeded in setting title message.]{lang="FR"}]{#struct_0_12438_x2040_x1454898536}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_1053754740}[title]{lang="FR"}[信息成功]{style="font-family:宋体"}

 

[[Succeeded in setting logo.]{lang="FR"}]{#struct_0_12438_x2040_1248023112}

[[设置]{style="font-family:宋体"}]{#struct_0_12438_x2040_x237449414}[logo]{lang="FR"}[成功]{style="font-family:宋体"}

 

[[Deleted context *context-id* from VPN *vpn-id*.]{lang="FR"}]{#struct_0_12438_x2040_x156033305}

[[从]{style="font-family:宋体"}]{#struct_0_12438_x2040_x385117228}[VPN]{lang="FR"}[实例]{style="font-family:宋体"}*[vpn-id]{lang="FR"}*[内删除]{style="font-family:宋体"}[Context *context-id*]{lang="FR"}

 

[[Failed to get VPN instance *id*.]{lang="FR"}]{#struct_0_12438_x2040_x1345936842}

[[获取]{style="font-family:宋体"}]{#struct_0_12438_x2040_1410050636}[VPN]{lang="FR"}[实例]{style="font-family:宋体"}*[vpn-id]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[WebAC: No web ACL resource.]{lang="FR"}]{#struct_0_12438_x2040_x667482842}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x1859581315}[代理：没有配置]{style="font-family:宋体"}[Web]{lang="FR"}[代理]{style="font-family:宋体"}[ACL]{lang="FR"}[规则]{style="font-family:宋体"}

 

[[WebAC: The acl check result *result*]{lang="FR"}]{#struct_0_12438_x2040_x1318832719}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x1585722451}[代理：]{style="font-family:宋体"}[ACL]{lang="FR"}[规则检查结果为]{style="font-family:宋体"}*[result]{lang="FR"}*[ ]{lang="FR"}

 

[[TCPAC: Succeeded in connecting remote server.]{lang="FR"}]{#struct_0_12438_x2040_516761892}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_247251222}[代理：成功连接远端服务器]{style="font-family:宋体"}

 

[[TCPAC: Connecting remote server *server.*]{lang="FR"}]{#struct_0_12438_x2040_1437995485}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x2125401773}[代理：连接远端服务器，]{style="font-family:宋体"}*[server]{lang="FR"}*[为远端服务器域名或者]{style="font-family:宋体"}[IP]{lang="FR"}[地址]{style="font-family:宋体"}

 

[[TCPAC: Get a local port resource %u from list %u.]{lang="FR"}]{#struct_0_12438_x2040_1437282935}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_2107637392}[代理：从资源列表中获取资源节点]{style="font-family:宋体"}

 

[[TCPAC: Get resource description *description*.]{lang="FR"}]{#struct_0_12438_x2040_x559317832}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1484833287}[代理：获取资源描述信息]{style="font-family:宋体"}*[description]{lang="FR"}*

 

[[TCPAC: No TCP ACL resource.]{lang="FR"}]{#struct_0_12438_x2040_x859045417}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_1006766109}[代理：没有配置]{style="font-family:宋体"}[TCP]{lang="FR"}[代理]{style="font-family:宋体"}[ACL]{lang="FR"}[规则]{style="font-family:宋体"}

 

[[TCPAC: The acl check result *result*.]{lang="FR"}]{#struct_0_12438_x2040_x548139841}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1722117246}[代理：]{style="font-family:宋体"}[ACL]{lang="FR"}[规则检查结果为]{style="font-family:宋体"}*[result]{lang="FR"}*[ ]{lang="FR"}

 

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging sslvpn timer]{lang="FR"}]{#struct_0_12438_x2040_2048121511}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1646084535}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_294824846}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_163044325}

[[Offline for idle timeout. contextID: *id*; onlineID: *id*.]{lang="FR"}]{#struct_0_12438_x2040_x1894938322}

[[空闲]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1252075593}[定时器超时，触发下线，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为下线请求所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[onlineID]{lang="FR"}*[为需要下线的在线用户]{style="font-family:宋体"}[ID]{lang="FR"}

 

[[Failed to log in for exception timeout. contextID: *id*; requestID: *id*.]{lang="FR"}]{#struct_0_12438_x2040_914350641}

[[异常定时器超时]{style="font-family:宋体"}]{#struct_0_12438_x2040_1300014522}[，]{style="font-family:宋体"}[登录失败]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[contextID]{lang="FR"}*[为上线请求所属的]{style="font-family:宋体"}[Context]{lang="FR"}[，]{style="font-family:宋体"}*[requestID]{lang="FR"}*[为上线请求]{style="font-family:宋体"}[ID]{lang="FR"}

 

[ ]{lang="FR"}

[[表1-5 ]{lang="EN-US"}[debugging sslvpn packet]{lang="FR"}]{#struct_0_12438_x2040_x1299843496}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1650903905}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_x426215692}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_1238475484}

[[IPAC: Failed to input packet for interface link status was down.]{lang="FR"}]{#struct_0_12438_x2040_x512263665}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_564753443}[代理：]{style="font-family:宋体"}[Input]{lang="FR"}[报文失败，原因是接口链路状态是]{style="font-family:宋体"}[Down]{lang="FR"}

 

[[IPAC: Failed to forward packet by IP.]{lang="EN-US"}]{#struct_0_12438_x2040_1257070795}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1853217528}[代理：通过]{style="font-family:宋体"}[IP]{lang="FR"}[转发报文失败]{style="font-family:宋体"}

 

[[Client connection request.]{lang="FR"}]{#struct_0_12438_x2040_1596444125}

[[客户端连接请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_x295884138}

 

[[Default context receive request body.]{lang="FR"}]{#struct_0_12438_x2040_164755734}

[[默认]{style="font-family:宋体"}]{#struct_0_12438_x2040_871169063}[Context]{lang="FR"}[接收请求报文体。]{style="font-family:宋体"}

 

[[Match domain of context is *domain*.]{lang="FR"}]{#struct_0_12438_x2040_534191752}

[[匹配到]{style="font-family:宋体"}]{#struct_0_12438_x2040_1053820276}[Context]{lang="FR"}[下的]{style="font-family:宋体"}[Domain]{lang="FR"}[。]{style="font-family:宋体"}

 

[[Deliver receive body overflow.]{lang="EN-US"}]{#struct_0_12438_x2040_859382798}

[[分发时接收的报文体长度超过最大长度]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1563629616}

 

[[Deliver to *pattern*.]{lang="EN-US"}]{#struct_0_12438_x2040_2124539014}

[[分发到特定模式，]{style="font-family:宋体"}*[pattern]{lang="EN-US"}*]{#struct_0_12438_x2040_x1713618700}[为模式描述]{style="font-family:宋体"}

 

[[Deliver receive a body.]{lang="FR"}]{#struct_0_12438_x2040_1679946171}

[[分发时接收报文体]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1467879546}

 

[[Deliver receive a request without URL.]{lang="FR"}]{#struct_0_12438_x2040_652822109}

[[分发时接收的请求报文中没有]{style="font-family:宋体"}]{#struct_0_12438_x2040_x155967769}[URL]{lang="FR"}[信息]{style="font-family:宋体"}

 

[[Deliver receive request. method: *method*; URL: *url*.]{lang="FR"}]{#struct_0_12438_x2040_x1815100757}

[[分发时接收到请求报文，报文中的方法为]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1511669938}*[method]{lang="FR"}*[、]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}*[url]{lang="FR"}*

 

[[Deliver receive a request with bad body type.]{lang="FR"}]{#struct_0_12438_x2040_753023238}

[[分发时接收的请求报文中携带的报文体类型是非法值]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1195907952}

 

[[DNS resolved host *host* to address *ip-address*.]{lang="FR"}]{#struct_0_12438_x2040_x1979793950}

[[DNS]{lang="FR"}]{#struct_0_12438_x2040_452865100}[将主机名]{style="font-family:宋体"}*[host]{lang="FR"}*[解析为]{style="font-family:宋体"}[IP]{lang="FR"}[地址]{style="font-family:宋体"}*[ip-address]{lang="FR"}*

 

[[Received a client request with invalid file, and redirected it to a new file.]{lang="EN-US"}]{#struct_0_12438_x2040_1410116172}

[[客户端请求的文件不存在，重定向到新的文件]{style="font-family:宋体"}]{#struct_0_12438_x2040_x322376129}

 

[[The URL in the request is *url*.]{lang="FR"}]{#struct_0_12438_x2040_260708291}

[[请求报文中的]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1378865615}[URL]{lang="FR"}[为]{style="font-family:宋体"}*[url]{lang="FR"}*

 

[[IPAC: Failed to output.]{lang="FR"}]{#struct_0_12438_x2040_x1574906876}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x533912973}[代理：]{style="font-family:宋体"}[Output]{lang="FR"}[报文失败]{style="font-family:宋体"}

 

[[IPAC: Failed to get interface referenced by context *id*.]{lang="FR"}]{#struct_0_12438_x2040_x1318767183}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1315647958}[代理：获取]{style="font-family:宋体"}[Context]{lang="FR"}[引用的]{style="font-family:宋体"}[SSLVPN-AC]{lang="FR"}[接口失败]{style="font-family:宋体"}

 

[[IPAC: *interface* is not associated with the context *id*.]{lang="FR"}]{#struct_0_12438_x2040_594573689}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x222332976}[代理：报文的入接口与]{style="font-family:宋体"}[Context]{lang="FR"}[引用的接口不同]{style="font-family:宋体"}

 

[[IPAC: Failed to get VPN instance.]{lang="FR"}]{#struct_0_12438_x2040_1271523892}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1756539144}[代理：获取]{style="font-family:宋体"}[VPN]{lang="FR"}[实例失败]{style="font-family:宋体"}

 

[[IPAC: Failed to get connect from peer.]{lang="FR"}]{#struct_0_12438_x2040_314791078}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_247316758}[代理：从连接上获取]{style="font-family:宋体"}[peer]{lang="FR"}[数据失败]{style="font-family:宋体"}

 

[[IPAC: Failed to prepend packet.]{lang="FR"}]{#struct_0_12438_x2040_x135434444}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_23269419}[代理：预处理报文失败]{style="font-family:宋体"}

 

[[IPAC: Failed to forward packet.]{lang="FR"}]{#struct_0_12438_x2040_x1194092460}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_398853583}[代理：转发报文失败]{style="font-family:宋体"}

 

[[IPAC: Failed to output IPAC packet for interface link status was down.]{lang="FR"}]{#struct_0_12438_x2040_1695069791}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x2125336237}[代理：]{style="font-family:宋体"}[Output]{lang="FR"}[报文失败，原因是接口链路状态是]{style="font-family:宋体"}[Down]{lang="FR"}

 

[[IPAC: Failed to get peer data.]{lang="EN-US"}]{#struct_0_12438_x2040_1991453303}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1470039464}[代理：获取]{style="font-family:宋体"}[Peer]{lang="FR"}[数据失败]{style="font-family:宋体"}

 

[[IPAC: Received a keepalive packet from *ip-address*.]{lang="FR"}]{#struct_0_12438_x2040_1821712611}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1238572214}[代理：收到]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="FR"}*[.]{lang="FR"}[的客户端发送的保活报文]{style="font-family:宋体"}

 

[[IPAC: Received a data packet fragmentation with *length1* bytes. totle length: *length2*.]{lang="FR"}]{#struct_0_12438_x2040_x1785725521}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x559252296}[代理：接收到]{style="font-family:宋体"}[IP]{lang="FR"}[数据报文的分片，长度为]{style="font-family:宋体"}*[length1]{lang="FR"}*[，报文的总长度为]{style="font-family:宋体"}*[length2]{lang="FR"}*

 

[[IPAC: Failed to input packet by interface *interface-name*.]{lang="FR"}]{#struct_0_12438_x2040_1106249897}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1594899862}[代理：通过指定接口]{style="font-family:宋体"}[Input]{lang="FR"}[报文失败]{style="font-family:宋体"}

 

[[IPAC: Received an incomplete network extended packet with *length* bytes.]{lang="FR"}]{#struct_0_12438_x2040_x1282851273}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_1006831645}[代理：收到的网络扩展报文长度没有达到最小长度]{style="font-family:宋体"}

 

[[IPAC: Received a packet with unknown type from client.]{lang="EN-US"}]{#struct_0_12438_x2040_x167209087}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1936986019}[代理：从客户端收到报文的扩展类型是未知的类型]{style="font-family:宋体"}

 

[[IPAC: Added data to packet. length: *length*; value: *value*.]{lang="FR"}]{#struct_0_12438_x2040_x1952972877}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_x1389946913}[代理：向报文中添加数据，]{style="font-family:宋体"}*[length]{lang="FR"}*[为要添加的数据长度，]{style="font-family:宋体"}*[value]{lang="FR"}*[为要添加的数据内容]{style="font-family:宋体"}

 

[[IPAC: Received a packet without authentication.]{lang="EN-US"}]{#struct_0_12438_x2040_x1722051710}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_59052376}[代理：接收报文未认证]{style="font-family:宋体"}

 

[[IPAC: Received a packet with invalied User-Agent.]{lang="FR"}]{#struct_0_12438_x2040_1124299132}

[[IP]{lang="FR"}]{#struct_0_12438_x2040_603278738}[代理：接收到的报文携带非法的]{style="font-family:宋体"}[User-Agent]{lang="FR"}[字段]{style="font-family:宋体"}

 

[[Failed to allocate peer node because VPN instance doesn\'t exist.]{lang="FR"}]{#struct_0_12438_x2040_x447178570}

[[申请]{style="font-family:宋体"}]{#struct_0_12438_x2040_x512198129}[peer]{lang="FR"}[节点失败，原因是]{style="font-family:宋体"}[VPN]{lang="FR"}[实例不存在]{style="font-family:宋体"}

 

[[Added peer *peer-address*. VPN instance: *id*.]{lang="FR"}]{#struct_0_12438_x2040_x1091209485}

[[在]{style="font-family:宋体"}]{#struct_0_12438_x2040_1325750021}[VPN]{lang="FR"}[实例内添加]{style="font-family:宋体"}[peer]{lang="FR"}[节点]{style="font-family:宋体"}*[peer-address]{lang="FR"}*

 

[[Found peer ]{lang="EN-US"}]{#struct_0_12438_x2040_141505409}*[peer-address]{lang="FR"}*[.]{lang="EN-US"}

[[查找到]{style="font-family:宋体"}]{#struct_0_12438_x2040_x169093240}[peer]{lang="FR"}[节点]{style="font-family:宋体"}*[peer-address]{lang="FR"}*

 

[[Failed to find peer *peer-address* in VPN instance *id*.]{lang="FR"}]{#struct_0_12438_x2040_1053885812}

[[在]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1060643583}[VPN]{lang="FR"}[实例内]{style="font-family:宋体"}[查找]{style="font-family:宋体"}[peer]{lang="FR"}[节点]{style="font-family:宋体"}*[peer-address]{lang="FR"}*[失败]{style="font-family:宋体"}

 

[[Delete peer *peer-address*.]{lang="FR"}]{#struct_0_12438_x2040_x611730026}

[[删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_1116983997}[peer]{lang="FR"}[节点]{style="font-family:宋体"}*[peer-address]{lang="FR"}*

 

[[HTTP Redirect: Recvived a request. host: *host*; URI: *uri*.]{lang="FR"}]{#struct_0_12438_x2040_245374695}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_x2095751982}[重定向：接收到请求报文]{style="font-family:宋体"}

 

[[HTTP Redirect: Set location *uri*.]{lang="FR"}]{#struct_0_12438_x2040_x100989970}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_x1173091531}[重定向：设置重定向路径为]{style="font-family:宋体"}*[uri]{lang="FR"}*

 

[[Static receive request. url: *url*.]{lang="FR"}]{#struct_0_12438_x2040_1811458636}

[[静态页面接收请求]{style="font-family:宋体"}]{#struct_0_12438_x2040_2009966970}

 

[[The validate code was not needed.]{lang="FR"}]{#struct_0_12438_x2040_1980497743}

[[没有打开验证码功能]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1192766277}

 

[[Failed to get validate code.]{lang="FR"}]{#struct_0_12438_x2040_x917424719}

[[获取验证码失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1476371720}

 

[[The validate code was timed out.]{lang="FR"}]{#struct_0_12438_x2040_1188479121}

[[验证码超时]{style="font-family:宋体"}]{#struct_0_12438_x2040_x688961869}

 

[[The validate code was invalide.]{lang="FR"}]{#struct_0_12438_x2040_648659222}

[[验证码错误]{style="font-family:宋体"}]{#struct_0_12438_x2040_1727885296}

 

[[Found VPN instance *id*.]{lang="FR"}]{#struct_0_12438_x2040_159700239}

[[查找]{style="font-family:宋体"}]{#struct_0_12438_x2040_517893999}[VPN]{lang="FR"}[实例]{style="font-family:宋体"}

 

[[WebAC: Return *result* to trans for down write event.]{lang="FR"}]{#struct_0_12438_x2040_x1723993773}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_1865110546}[代理：向]{style="font-family:宋体"}[KHTTP]{lang="FR"}[模块返回]{style="font-family:宋体"}[down]{lang="FR"}[连接写事件处理结果，处理结果为]{style="font-family:宋体"}*[result]{lang="FR"}*

 

[[WebAC: Response Header: *header.*]{lang="FR"}]{#struct_0_12438_x2040_x1145154639}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x157909832}[代理：应答报文首部信息为]{style="font-family:宋体"}*[header]{lang="FR"}*

 

[[WebAC: Received a request. URL: *url*.]{lang="FR"}]{#struct_0_12438_x2040_727982890}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_789870513}[代理：接收到请求报文，请求报文的]{style="font-family:宋体"}[URL]{lang="FR"}[为]{style="font-family:宋体"}*[url]{lang="FR"}*

 

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging sslvpn packet verbose]{lang="FR"}]{#struct_0_12438_x2040_x1441817550}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1634654193}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_949086772}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_x1640961062}

[*[Interface]{lang="FR"}*]{#struct_0_12438_x2040_x1929274103}[ *operator* packet: *string*]{lang="FR"}

[[接收或发送]{style="font-family:宋体"}]{#struct_0_12438_x2040_563784102}[IP]{lang="FR"}[接入的报文]{style="font-family:宋体"}

[*[Interface]{lang="FR"}*]{#struct_0_12438_x2040_1408174109}[为处理报文的接口名，如]{style="font-family:宋体"}[SSLVPN-AC1]{lang="FR"}

[*[operator]{lang="FR"}*]{#struct_0_12438_x2040_941618743}[用来说明报文的方向，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[input]{lang="EN-US"}]{#struct_0_12438_x2040_454530984}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[代理从客户端接收报文，转发到服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[output]{lang="EN-US"}]{#struct_0_12438_x2040_1266829346}[：]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[代理从服务器接收报文，转发到客户端]{lang="EN-US" style="font-family:宋体"}

[*[string]{lang="FR"}*]{#struct_0_12438_x2040_71312011}[为报文具体内容]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging sslvpn fsm]{lang="FR"}]{#struct_0_12438_x2040_78811131}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1635755111}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_1633022549}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_693370452}

[[WebAC: State changed from *state1* to *state2*.]{lang="FR"}]{#struct_0_12438_x2040_x2082790363}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_x1320709246}[代理：状态从]{style="font-family:宋体"}*[state1]{lang="FR"}*[切换到]{style="font-family:宋体"}*[state2]{lang="FR"}*

 

[[WebAC: Handle event *event* in *state* state.]{lang="FR"}]{#struct_0_12438_x2040_x660180828}

[[Web]{lang="FR"}]{#struct_0_12438_x2040_920854722}[代理：在状态]{style="font-family:宋体"}*[state]{lang="FR"}*[处理事件]{style="font-family:宋体"}*[event]{lang="FR"}*

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x84172994}

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_x614716704}[打开]{style="font-family:宋体"}[SSL VPN AAA]{lang="EN-US"}[调试信息开关。使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[客户端连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn aaa]{lang="EN-US"}]{#struct_0_12438_x2040_452377589}

[Authentication request. result: 0x0; client MAC: 1cbd-b9e3-b142; private info length: 32.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_12438_x2040_x1389641367}*[解析认证请求中的信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_x31514175}[打开]{style="font-family:宋体"}[SSL VPN ERROR]{lang="EN-US"}[调试信息开关。创建]{style="font-family:宋体"}[SSL VPN Context]{lang="EN-US"}[，如果发生错误，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn error]{lang="EN-US"}]{#struct_0_12438_x2040_2105499004}

[\*Oct 11 06:50:45:602  2014 H3C SSLVPN/7/SSLVPN_ERROR: -MDC=1; Failed to add a context.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12438_x2040_x668913312}*[创建]{style="font-family:宋体"}[Context]{lang="EN-US"}[失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_1131642744}[打开]{style="font-family:宋体"}[SSL VPN EVENT]{lang="EN-US"}[调试信息开关。使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[客户端连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn event]{lang="EN-US"}]{#struct_0_12438_x2040_x516686325}

[\*Oct 11 06:50:45:602 2014 H3C SSLVPN/7/SSLVPN_EVENT: -MDC=1; Succeed in matching default context.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12438_x2040_x110855665}*[连接请求报文匹配到默认]{style="font-family:宋体"}[Context]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_x1016909584}[打开]{style="font-family:宋体"}[SSL VPN TIMER]{lang="EN-US"}[调试信息开关。创建]{style="font-family:宋体"}[SSL VPN Context]{lang="EN-US"}[，如果发生错误，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn timer]{lang="EN-US"}]{#struct_0_12438_x2040_x1422275476}

[\*Oct 11 06:50:45:602  2014 H3C SSLVPN/7/SSLVPN_TIMER: -MDC=1; Offline for idle timeout. contextID: 0x3; onlineID: 0x1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12438_x2040_1211027708}*[空闲定时器检查到用户老化，请求下线]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_1411480000}[打开]{style="font-family:宋体"}[SSL VPN PACKET]{lang="EN-US"}[调试信息开关。使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[客户端连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn packet]{lang="EN-US"}]{#struct_0_12438_x2040_1233454241}

[\*Oct 11 06:59:57:747 2014 H3C SSLVPN/7/SSLVPN_PACKET: -MDC=1; Deliver receive request, method:NET_EXTEND, url:/]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_12438_x2040_x1333312985}*[分发时接收到请求报文，报文中的方法为]{style="font-family:宋体"}[NET_EXTEND]{lang="EN-US"}[，请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为"]{style="font-family:宋体"}[/]{lang="EN-US"}["]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_1819249994}[打开]{style="font-family:宋体"}[SSL VPN PACKET VERBOSE]{lang="EN-US"}[调试信息开关。使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[客户端连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn packet verbose]{lang="EN-US"}]{#struct_0_12438_x2040_1455228276}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1;  SSLVPN-AC1 input packet:                                             ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 45 00 00 60  00 0c 00 00  80 11 11 6e  0a 0a 0a 01                    ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 0a 0a 0a ff  00 89 00 89  00 4c 90 54  fd 47 29 10                    ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 00 01 00 00  00 00 00 01  20 45 4d 44  41 44 49 44                    ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 46 44 43 44  47 45 42 43  41 43 41 43  41 43 41 43                    ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 41 43 41 43  41 43 41 43  41 00 00 20  00 01 c0 0c                    ]{lang="EN-US"}

[\*Oct 11 07:00:02:663 2014 H3C SSLVPN/7/SSLVPN_VERBOSE: -MDC=1; 00 20 00 01  00 04 93 e0  00 06 60 00  0a 0a 0a 01]{lang="EN-US"}

[*[// SSLVPN-AC1]{lang="EN-US"}*]{#struct_0_12438_x2040_1962068524}*[接收到]{style="font-family:宋体"}[input]{lang="EN-US"}[报文及具体报文内容。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_374714102}[打开]{style="font-family:宋体"}[SSL VPN [FSM]{#_GoBack}]{lang="EN-US"}[调试信息开关。使用]{style="font-family:宋体"}[Web]{lang="EN-US"}[代理方式连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging sslvpn fsm]{lang="EN-US"}]{#struct_0_12438_x2040_x1738625075}

[\*Oct 11 06:50:45:602 2014 H3C SSLVPN/7/SSLVPN_EVENT: -MDC=1; WebAC: Handle event UP OUT in state Connecting.]{lang="EN-US"}

[*[// Web]{lang="EN-US"}*]{#struct_0_12438_x2040_1879344633}*[代理，在]{style="font-family:宋体"}[Connecting]{lang="EN-US"}[状态处理]{style="font-family:宋体"}[UP OUT]{lang="EN-US"}[事件]{style="font-family:宋体"}*

::: {#-1181828007 .myid}
[]{#_Toc404793319}[]{#struct_0_12438_x2040_233965465}[]{#_Toc400805750}

**SSL VPN \-- SSL VPN调试命令 \-- debugging khttp**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x395495819}

[**[debugging]{lang="EN-US"}**[ **khttp** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_12438_x2040_x1969978379}

[**[undo]{lang="EN-US"}**[ **debugging** **khttp** { **all** \| **error** \| **event** \| **fsm** \| **packet** }]{lang="EN-US"}]{#struct_0_12438_x2040_1256129059}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x1514449612}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1052787842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x28546778}

[[network-admin]{lang="EN-US"}]{#struct_0_12438_x2040_1583194819}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12438_x2040_x955561539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12438_x2040_245440231}

[**[all]{lang="EN-US"}**]{#struct_0_12438_x2040_1234317279}[：表示]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_12438_x2040_887469932}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_12438_x2040_x163629859}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_12438_x2040_296743244}[：表示]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_12438_x2040_884027649}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x580410872}

[**[debugging]{lang="EN-US"}**[ **khttp**]{lang="EN-US"}]{#struct_0_12438_x2040_x22067984}[命令用来打开]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **debugging** **khttp**]{lang="EN-US"}[命令用来关闭]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[KHTTP]{lang="EN-US"}]{#struct_0_12438_x2040_579934993}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging khttp error]{lang="FR"}]{#struct_0_12438_x2040_953953877}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1632400413}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_x199370892}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_x1783028275}

[[Failed to close server *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_x133004010}

[[关闭]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_1811524172}[实例下的服务器失败，服务器的地址为]{style="font-family:宋体"}*[server-address]{lang="FR"}*[、端口号为]{style="font-family:宋体"}*[port]{lang="FR"}*

 

[[Failed to set SSL context to server *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_2020726505}

[[设置]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x420725238}[实例下服务器使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[上下文失败]{style="font-family:宋体"}

 

[[Repeated to open server *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_x1096113235}

[[重复打开]{style="font-family:宋体"}]{#struct_0_12438_x2040_1695510461}[VPN]{lang="FR"}[实例下的服务器]{style="font-family:宋体"}

 

[[Failed to listen server ]{lang="EN-US"}]{#struct_0_12438_x2040_671832071}*[server-address/port]{lang="FR"}*[ in VPN ]{lang="EN-US"}*[id]{lang="FR"}*[.]{lang="FR"}

[[监听]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x1588861187}[实例下的服务器失败]{style="font-family:宋体"}

 

[[Failed to add server]{lang="EN-US"}]{#struct_0_12438_x2040_x488824672}*[ server-address/port]{lang="FR"}*[ in VPN ]{lang="EN-US"}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[在]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x917359183}[下添加服务器失败]{style="font-family:宋体"}

 

[[Failed to create a new SSL connection.]{lang="EN-US"}]{#struct_0_12438_x2040_x2084240767}

[[创建新的]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x1112341109}[连接失败]{style="font-family:宋体"}

 

[[SSL connect failed because SSL handle is invalid.]{lang="EN-US"}]{#struct_0_12438_x2040_1742378554}

[[由于]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_432400595}[句柄非法，]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接失败]{style="font-family:宋体"}

 

[[Failed to connect SSL server.]{lang="EN-US"}]{#struct_0_12438_x2040_564707593}

[[连接]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x344992509}[服务器失败]{style="font-family:宋体"}

 

[[Failed to accept SSL connection because SSL handle is invalid.]{lang="EN-US"}]{#struct_0_12438_x2040_991307901}

[[由于]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_648724758}[句柄非法，接受]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接失败]{style="font-family:宋体"}

 

[[Failed to accept SSL connection.]{lang="EN-US"}]{#struct_0_12438_x2040_x190466172}

[[接受]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x1989734560}[连接失败]{style="font-family:宋体"}

 

[[Failed to connect to server ]{lang="EN-US"}]{#struct_0_12438_x2040_x534780025}*[server-address/port]{lang="FR"}*[ ]{lang="FR"}[in VPN]{lang="EN-US"}[ ]{lang="EN-US"}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[连接]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_492692147}[实例内的服务器失败]{style="font-family:宋体"}

 

[[Failed to connect to SSL server]{lang="EN-US"}]{#struct_0_12438_x2040_x532704724}*[ ]{lang="EN-US"}[server-address/port ]{lang="FR"}*[in VPN ]{lang="EN-US"}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[连接]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x120844217}[实例内的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器失败]{style="font-family:宋体"}

 

[[Failed to accept a new FTCP handle.]{lang="EN-US"}]{#struct_0_12438_x2040_x1723928237}

[[接受新]{style="font-family:宋体"}[FTCP]{lang="EN-US"}]{#struct_0_12438_x2040_2067176416}[句柄失败]{style="font-family:宋体"}

 

[[Failed to create a connection. TCP: *handle*.]{lang="EN-US"}]{#struct_0_12438_x2040_x1391721845}

[[从]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_x1321857962}[创建连接失败]{style="font-family:宋体"}

 

[[Failed to accept a new handle.]{lang="EN-US"}]{#struct_0_12438_x2040_1729678077}

[[接受新句柄失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_1058461808}

 

[[Failed to create a connection: \[TCP= *handle*\] \[SSL= *handle*\].]{lang="EN-US"}]{#struct_0_12438_x2040_383299570}

[[创建连接失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x157844296}

 

[[Failed to bind TCP handle:]{lang="EN-US"}]{#struct_0_12438_x2040_x1145560920}*[ X.X.X.X/port]{lang="FR"}*[ in VPN ]{lang="EN-US"}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_x103500018}[句柄失败]{style="font-family:宋体"}

 

[[Failed to listen: ]{lang="EN-US"}]{#struct_0_12438_x2040_296022340}*[X.X.X.X/port]{lang="FR"}*[ in VPN ]{lang="EN-US"}*[id]{lang="FR"}*[..]{lang="EN-US"}

[[监听失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_2027726042}

 

[[Failed to create TCP handle..]{lang="EN-US"}]{#struct_0_12438_x2040_x407421426}

[[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_1408239645}[句柄失败。]{style="font-family:宋体"}

 

[[Failed to set service type tcp\[*handle*\].]{lang="EN-US"}]{#struct_0_12438_x2040_x1792918109}

[[设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_x269494273}[服务类型失败。]{style="font-family:宋体"}

 

[[Failed to create a connection tcp\[*handle*\].]{lang="EN-US"}]{#struct_0_12438_x2040_x956173387}

[[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12438_x2040_111514669}[连接失败。]{style="font-family:宋体"}

 

[[Failed to add server for the MDC is invalid.]{lang="EN-US"}]{#struct_0_12438_x2040_x128651723}

[[MDC]{lang="EN-US"}]{#struct_0_12438_x2040_x1320643710}[非法，添加服务器失败]{style="font-family:宋体"}

 

[[Failed to add server for the data of MDC is invalid.]{lang="EN-US"}]{#struct_0_12438_x2040_x621177583}

[[MDC]{lang="EN-US"}]{#struct_0_12438_x2040_x1998091215}[下数据非法，添加服务失败]{style="font-family:宋体"}

 

[[Failed to add server because of insufficient resource.]{lang="FR"}]{#struct_0_12438_x2040_x735416126}

[[内存不足，]{style="font-family:宋体"}]{#struct_0_12438_x2040_1945041246}[添加服务失败]{style="font-family:宋体"}

 

[[Body receive: There is not a dispatch.]{lang="FR"}]{#struct_0_12438_x2040_x110790129}

[[体接收，没有注册分发处理函数。]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1430793534}

 

[[State(*state*) of transaction could not run phase.]{lang="FR"}]{#struct_0_12438_x2040_1385523381}

[[Transaction]{lang="FR"}]{#struct_0_12438_x2040_x1713634756}[的当前状态不能进行状态切换]{style="font-family:宋体"}

 

[[Receive HTTP request with invalid content-length.]{lang="FR"}]{#struct_0_12438_x2040_x300410757}

[[接收]{style="font-family:宋体"}]{#struct_0_12438_x2040_286847333}[HTTP]{lang="FR"}[请求报文携带了无效的]{style="font-family:宋体"}[Content-length]{lang="FR"}[字段]{style="font-family:宋体"}

 

[[Transaction, Direction=Request, Parse result=Failed, Parse length=*length*.]{lang="FR"}]{#struct_0_12438_x2040_1455293812}

[[Transaction]{lang="FR"}]{#struct_0_12438_x2040_82691969}[解析报文异常信息]{style="font-family:宋体"}

 

[[Failed to merge packet data (*length*).]{lang="FR"}]{#struct_0_12438_x2040_x1230110599}

[[合并]{style="font-family:宋体"}]{#struct_0_12438_x2040_20884190}[Mbuf]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Failed to combine data(*length*) with the previous data(*length*).]{lang="FR"}]{#struct_0_12438_x2040_245505767}

[[连接]{style="font-family:宋体"}]{#struct_0_12438_x2040_460318810}[Mbuf]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Head send: Failed to analyse sending type.]{lang="FR"}]{#struct_0_12438_x2040_x1924746403}

[[头发送，判断发送类型失败]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1849737781}

 

[[Body send: Failed to prepend buffer.]{lang="FR"}]{#struct_0_12438_x2040_x1909234821}

[[体发送，扩展]{style="font-family:宋体"}]{#struct_0_12438_x2040_1811589708}[MBuf]{lang="FR"}[失败]{style="font-family:宋体"}

 

[[Body send: Failed to fill chunk.]{lang="FR"}]{#struct_0_12438_x2040_1256076479}

[[体发送，填充]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1876072076}[chunk]{lang="FR"}[封装失败。]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging sslvpn event]{lang="FR"}]{#struct_0_12438_x2040_618638219}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1614365525}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_x537235429}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_42506983}

[[Succeeded in setting SSL context to server: *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_2099165583}

[[设置]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x917293647}[实例下服]{style="font-family:宋体"}[务器使用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[上下文成功]{style="font-family:宋体"}

 

[[Succeeded in closing server: %s in VPN ]{lang="EN-US"}]{#struct_0_12438_x2040_1907455014}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[关]{style="font-family:宋体"}]{#struct_0_12438_x2040_2082302572}[闭]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例下的]{style="font-family:宋体"}[服务器成功]{style="font-family:宋体"}

 

[[Succeeded in adding server: %s in VPN ]{lang="EN-US"}]{#struct_0_12438_x2040_x1607368427}*[id]{lang="FR"}*[.]{lang="EN-US"}

[[添加]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x1600062499}[下的服务成功。]{style="font-family:宋体"}

 

[[Succeeded in creating a new SSL connection: %#lx.]{lang="EN-US"}]{#struct_0_12438_x2040_x1238899700}

[[创建新的]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_583633149}[连接成功]{style="font-family:宋体"}

 

[[Succeeded in connecting SSL server.]{lang="EN-US"}]{#struct_0_12438_x2040_x188248168}

[[连接]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_648790294}[服务器成功]{style="font-family:宋体"}

 

[[SSL connection(write) was not completed.]{lang="EN-US"}]{#struct_0_12438_x2040_1335390562}

[[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x152431300}[连接写操作过程中]{style="font-family:宋体"}

 

[[SSL connection(read) was not completed.]{lang="EN-US"}]{#struct_0_12438_x2040_241925614}

[[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_1490280852}[连接读操作过程中]{style="font-family:宋体"}

 

[[Succeeded in accepting SSL connection.]{lang="FR"}]{#struct_0_12438_x2040_1474189554}

[[成功接受]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_155982714}[连接]{style="font-family:宋体"}

 

[[SSL connection is being created.]{lang="FR"}]{#struct_0_12438_x2040_1919218639}

[[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x1088968132}[连接建立过程中]{style="font-family:宋体"}

 

[[Connection received input event: \[TCP *handle*\] \[*string*\].]{lang="FR"}]{#struct_0_12438_x2040_x1723862701}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x656854637}[连接接收到]{style="font-family:宋体"}[Input]{lang="FR"}[事件]{style="font-family:宋体"}

 

[[Connection received output event: \[TCP *handle*\] \[*string*\].]{lang="FR"}]{#struct_0_12438_x2040_x602791773}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x332962272}[连接接收到]{style="font-family:宋体"}[Output]{lang="FR"}[事件]{style="font-family:宋体"}

 

[[Succeeded in connecting server *server-address/port*.]{lang="FR"}]{#struct_0_12438_x2040_1940769833}

[[连接服务器成功]{style="font-family:宋体"}]{#struct_0_12438_x2040_x157778760}

 

[[Connection received error event *error*. \[TCP *handle*\] \[*string*\].]{lang="FR"}]{#struct_0_12438_x2040_x1568696446}

[[TCP]{lang="FR"}]{#struct_0_12438_x2040_x1786974680}[连接接收到]{style="font-family:宋体"}[Error]{lang="FR"}[事件]{style="font-family:宋体"}

 

[[Connected to server *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_2048495323}

[[连接]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x1663182326}[实例内的服务器]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Connected to SSL server *server-address/port* in VPN *id*.]{lang="FR"}]{#struct_0_12438_x2040_600446436}

[[连接]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_1408305181}[实例内的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器]{style="font-family:宋体"}[成功]{style="font-family:宋体"}

 

[[Succeeded in accepting a connection: \[*string*\].]{lang="FR"}]{#struct_0_12438_x2040_x626365684}

[[成功接受一个连接]{style="font-family:宋体"}]{#struct_0_12438_x2040_1110876989}

 

[[Succeeded in accepting a SSL connection: \[*string*\] \[SSL=*handle*\].]{lang="FR"}]{#struct_0_12438_x2040_x1784353445}

[[成功接受一个]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_12438_x2040_x1679045890}[连接]{style="font-family:宋体"}

 

[[Succeeded in listening a connection: %s in VPN %u.]{lang="FR"}]{#struct_0_12438_x2040_1094523337}

[[监听]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_12438_x2040_x1320578174}[实例下的服务连接成功]{style="font-family:宋体"}

 

[[Connection closed.]{lang="FR"}]{#struct_0_12438_x2040_1223749986}

[[连接关闭]{style="font-family:宋体"}]{#struct_0_12438_x2040_x710390550}

 

[[Connection has been deleted.]{lang="FR"}]{#struct_0_12438_x2040_1705431638}

[[连接已经被删除]{style="font-family:宋体"}]{#struct_0_12438_x2040_x293103613}

 

[[Not enough memory resource.]{lang="FR"}]{#struct_0_12438_x2040_x110724593}

[[内存不足]{style="font-family:宋体"}]{#struct_0_12438_x2040_157852981}

 

[[Memory resource is restored.]{lang="FR"}]{#struct_0_12438_x2040_x736879889}

[[内存资源恢复]{style="font-family:宋体"}]{#struct_0_12438_x2040_1016664923}

 

[[Body send: Succeeded in sending body.]{lang="FR"}]{#struct_0_12438_x2040_388880205}

[[体发送，发送体成功]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1548975027}

 

[[Transaction has been deleted.]{lang="FR"}]{#struct_0_12438_x2040_1455359348}

[[Transaction]{lang="EN-US"}]{#struct_0_12438_x2040_1200051565}[已经被删除]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging sslvpn packet]{lang="FR"}]{#struct_0_12438_x2040_x691169141}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1622540881}[[字段]{style="font-family:黑体"}]{#struct_0_12438_x2040_x1742336982}

[[描述]{style="font-family:黑体"}]{#struct_0_12438_x2040_1614473878}

[[Body receive: the dispatch result of body-in(*result*) event is *event*.]{lang="FR"}]{#struct_0_12438_x2040_x249780530}

[[体接收，]{style="font-family:宋体"}[body-in]{lang="EN-US"}]{#struct_0_12438_x2040_2106921332}[事件的分发结果。]{style="font-family:宋体"}

 

[[Body receive: Received a null body.]{lang="FR"}]{#struct_0_12438_x2040_1207470776}

[[体接收：接收到空体]{style="font-family:宋体"}]{#struct_0_12438_x2040_1702503267}

 

[[Body receive: Received body.]{lang="FR"}]{#struct_0_12438_x2040_245571303}

[[体接收：接收到体]{style="font-family:宋体"}]{#struct_0_12438_x2040_1630255777}

 

[[Header receive: the dispatch result of head-ok event is *result*.]{lang="FR"}]{#struct_0_12438_x2040_486919768}

[[头接收，]{style="font-family:宋体"}[head-ok]{lang="EN-US"}]{#struct_0_12438_x2040_x1443926355}[事件的分发结果]{style="font-family:宋体"}

 

[[Parse a header: *string*, value: *string*.]{lang="FR"}]{#struct_0_12438_x2040_x2109381468}

[[解析一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_12438_x2040_x1850129777}[首部]{style="font-family:宋体"}

 

[[Delete old header: *string*, value: *string*.]{lang="FR"}]{#struct_0_12438_x2040_66128990}

[[删除旧的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_12438_x2040_x1762253624}[首部]{style="font-family:宋体"}

 

[[Encapsulate a header: *string*, value: *string*.]{lang="FR"}]{#struct_0_12438_x2040_x376126208}

[[封装]{style="font-family:宋体"}]{#struct_0_12438_x2040_1811655244}[H]{lang="FR"}[TTP]{lang="EN-US"}[首部]{style="font-family:宋体"}

 

[[Encapsulate response code: *id* *string*.]{lang="FR"}]{#struct_0_12438_x2040_2014995120}

[[封装]{style="font-family:宋体"}]{#struct_0_12438_x2040_x1084861142}[H]{lang="FR"}[TTP]{lang="EN-US"}[应答码]{style="font-family:宋体"}

 

[[Received a packet with *length* bytes on the conncetion.]{lang="FR"}]{#struct_0_12438_x2040_1320207698}

[[在连接上接收到]{style="font-family:宋体"}]{#struct_0_12438_x2040_x761741442}*[length]{lang="FR"}*[字节的报文]{style="font-family:宋体"}

 

[[Query: *string*.]{lang="FR"}]{#struct_0_12438_x2040_709268997}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_1284252811}[报文的请求信息为]{style="font-family:宋体"}*[string]{lang="FR"}*

 

[[URI: *uri*.]{lang="FR"}]{#struct_0_12438_x2040_x917228111}

[[HTTP]{lang="FR"}]{#struct_0_12438_x2040_653489874}[报文的]{style="font-family:宋体"}[URI]{lang="FR"}[为]{style="font-family:宋体"}*[uri]{lang="FR"}*

 

[[Transaction, Direction=Request, State=%s \--\> %s, Parse Length=%ld.]{lang="FR"}]{#struct_0_12438_x2040_x723870343}

[[Transaction]{lang="FR"}]{#struct_0_12438_x2040_1142817239}[状态切换及解析报文信息]{style="font-family:宋体"}

 

[[Header send: Succeeded in sending header.]{lang="FR"}]{#struct_0_12438_x2040_x1436222520}

[[头发送：发送头成功]{style="font-family:宋体"}]{#struct_0_12438_x2040_x930763698}

 

[[Transaction finished.]{lang="FR"}]{#struct_0_12438_x2040_x1955047590}

[[Transaction]{lang="FR"}]{#struct_0_12438_x2040_648855830}[结束]{style="font-family:宋体"}

 

[[Transaction has been closed.]{lang="FR"}]{#struct_0_12438_x2040_437498960}

[[Transaction]{lang="FR"}]{#struct_0_12438_x2040_1666319688}[已经关闭]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12438_x2040_x1794104407}

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_x1280287047}[打开]{style="font-family:宋体"}[KHTTP ERROR]{lang="EN-US"}[调试信息开关。配置冲突时重复打开一个]{style="font-family:宋体"}[server]{lang="EN-US"}[，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging khttp error]{lang="EN-US"}]{#struct_0_12438_x2040_x188630016}

[\*Sep 19 09:55:52:338 2014 H3C KHTTP/7/ERROR: Repeated to open server: 192.168.10.109/443 in VPN 0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12438_x2040_x1096465109}*[提示相应]{style="font-family:宋体"}[server]{lang="EN-US"}[已经打开]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_12438_x2040_1024515847}[打开]{style="font-family:宋体"}[KHTTP EVENT]{lang="EN-US"}[调试信息开关。连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging khttp event]{lang="EN-US"}]{#struct_0_12438_x2040_x1420372632}

[\*Oct 11 09:30:27:572 2014 H3C KHTTP/7/EVENT: -MDC=1; Connection received input event: \[TCP e9e94000\] \[Local=192.168.10.109:443, Peer=0.0.0.0:0\].]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_12438_x2040_x1434279128}*[连接接收到]{style="font-family:宋体"}[Input]{lang="EN-US"}[事件。]{style="font-family:宋体"}*

[[\#]{lang="EN-US"}]{#struct_0_12438_x2040_x1723797165}[打开]{style="font-family:宋体"}[KHTTP PACKET]{lang="EN-US"}[调试信息开关。连接]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务时，打印以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging khttp packet]{lang="EN-US"}]{#struct_0_12438_x2040_1606356910}

[\*Oct 11 09:30:31:609 2014 H3C KHTTP/7/PACKET: -MDC=1; Parse a Head: Accept, value: application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, \*/\*.]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_12438_x2040_1808403777}*[显示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文]{style="font-family:宋体"}[Accept]{lang="EN-US"}[首部信息。]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*
