::: {#-332958193 .myid}
[]{#_Toc404796821}[]{#struct_0_73523_x1515_x825918263}[]{#_Toc263690035}[]{#_Toc206560110}

**SNMP \-- SNMP调试命令 \-- debugging snmp agent packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_73523_x1515_1732355727}

[**[debugging snmp agent]{lang="EN-US"}**[ **packet** { **header** \| **receive** \| **send** }]{lang="EN-US"}]{#struct_0_73523_x1515_1289408052}

[**[undo debugging snmp agent packet]{lang="EN-US"}**[ { **header** \| **receive** \| **send** }]{lang="EN-US"}]{#struct_0_73523_x1515_x599600623}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73523_x1515_325527140}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73523_x1515_x598825038}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x475560836}

[[network-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x579009953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x604498668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73523_x1515_282695231}

[**[header]{lang="EN-US"}**]{#struct_0_73523_x1515_56495947}[：表示]{style="font-family:宋体"}[SNMP Agent]{lang="EN-US"}[数据包消息头调试信息开关。向信息中心输出]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文头的版本、团体名或用户名等信息。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_73523_x1515_x92184274}[：表示接收到的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[数据包调试信息开关。向信息中心输出]{style="font-family:宋体"}[Agent]{lang="EN-US"}[接收到的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文的类型、]{style="font-family:宋体"}[request-id]{lang="EN-US"}[、]{style="font-family:宋体"}[error-status]{lang="EN-US"}[、]{style="font-family:宋体"}[error-index]{lang="EN-US"}[和绑定节点列表等信息。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**]{#struct_0_73523_x1515_x1321800946}[：表示发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[数据包调试信息开关。向信息中心输出]{style="font-family:宋体"}[Agent]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[响应消息的类型、]{style="font-family:宋体"}[request-id]{lang="EN-US"}[、]{style="font-family:宋体"}[error-status]{lang="EN-US"}[、]{style="font-family:宋体"}[error-index]{lang="EN-US"}[和绑定节点列表等信息。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1603505924}

[**[debugging snmp agent]{lang="EN-US"}**[ **packet**]{lang="EN-US"}]{#struct_0_73523_x1515_151035081}[命令]{style="font-family:宋体"}[用来打开]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[消息报文内容的调试开关。]{style="font-family:宋体"}**[undo debugging snmp agent packet]{lang="EN-US"}**[命令]{style="font-family:
宋体"}[用来关闭]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[消息报文内容的调试开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1262746298}[消息报文内容的调试开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging snmp agent packet header]{lang="EN-US"}]{#struct_0_73523_x1515_x1826118100}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1523884463}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_x604302060}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1600911388}

[[Incoming *SNMP-version* packet]{lang="EN-US"}]{#struct_0_73523_x1515_x365931595}

[[接收到]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_718509645}[报文]{style="font-family:宋体"}

[*[SNMP-version]{lang="EN-US"}*]{#struct_0_73523_x1515_728450853}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本（取值]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[、]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Community name: *community-name*]{lang="EN-US"}]{#struct_0_73523_x1515_850573428}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x604367596}[（]{style="font-family:宋体"}[v1/v2c]{lang="EN-US"}[）访问团体名]{style="font-family:宋体"}

[[Security model: v3]{lang="EN-US"}]{#struct_0_73523_x1515_x2019930392}

[[SNMP v3]{lang="EN-US"}]{#struct_0_73523_x1515_x371415310}[安全模型]{style="font-family:宋体"}

[[Security level: *security-level*]{lang="EN-US"}]{#struct_0_73523_x1515_x2022940593}

[[SNMP v3]{lang="EN-US"}]{#struct_0_73523_x1515_2078356083}[安全级别，]{style="font-family:宋体"}*[security-level]{lang="EN-US"}*[取值为以下]{style="font-family:宋体"}[3]{lang="EN-US"}[种：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[NoAuthNoPriv]{lang="EN-US"}*]{#struct_0_73523_x1515_495903629}*[：]{lang="EN-US" style="font-family:
  宋体"}*[无认证无加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[AuthNoPriv]{lang="EN-US"}*]{#struct_0_73523_x1515_x604170988}*[：]{lang="EN-US" style="font-family:
  宋体"}*[有认证无加密]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[AuthPriv]{lang="EN-US"}*]{#struct_0_73523_x1515_381612246}*[：]{lang="EN-US" style="font-family:
  宋体"}*[有认证有加密]{lang="EN-US" style="font-family:宋体"}

[[User name: *user-name*]{lang="EN-US"}]{#struct_0_73523_x1515_1658000212}

[[SNMP v3]{lang="EN-US"}]{#struct_0_73523_x1515_784868625}[用户名]{style="font-family:宋体"}

[[SnmpEngineID: *engineID*]{lang="EN-US"}]{#struct_0_73523_x1515_1231449475}

[[SNMP]{lang="SV"}]{#struct_0_73523_x1515_x2028845871}[引擎]{style="font-family:宋体"}[ID]{lang="SV"}

[[SnmpEngineBoots: *n*]{lang="EN-US"}]{#struct_0_73523_x1515_x604236524}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x464397837}[引擎重启的次数]{style="font-family:宋体"}

[[SnmpEngineTime: *n*]{lang="EN-US"}]{#struct_0_73523_x1515_x768257757}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1823387429}[引擎运行的时间（单位：]{style="font-family:宋体"}[s]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging snmp agent packet receive]{lang="EN-US"}]{#struct_0_73523_x1515_1418923331}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1493802095}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_1774314714}

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_554633108}

[[PACKET]{lang="EN-US"}]{#struct_0_73523_x1515_1925883799}

[[报文包含的信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_x800616272}

[[PACKET_SRC]{lang="EN-US"}]{#struct_0_73523_x1515_736942811}

[[报文源地址信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_2033095817}

[[Packet received from *address* via UDP]{lang="EN-US"}]{#struct_0_73523_x1515_x780287596}

[[通过]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_73523_x1515_1774380250}[协议从]{style="font-family:宋体"}*[address]{lang="EN-US"}*[接收到的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[address]{lang="EN-US"}*]{#struct_0_73523_x1515_x555928276}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的源地址]{style="font-family:宋体"}

[[Request ID: *request-id*]{lang="EN-US"}]{#struct_0_73523_x1515_1761449922}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1544692492}[请求报文的编号（用于匹配]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[响应报文）]{style="font-family:宋体"}

[[Error status: *error-status*]{lang="EN-US"}]{#struct_0_73523_x1515_x1489347994}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1774183642}[请求报文中的错误状态]{style="font-family:宋体"}

[[Error index: *error-index*]{lang="EN-US"}]{#struct_0_73523_x1515_x1357207162}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1499196455}[请求报文中的错误索引]{style="font-family:宋体"}

[[VBLIST]{lang="EN-US"}]{#struct_0_73523_x1515_x1554260326}

[[变量绑定对列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_1260068894}

[[Get request]{lang="EN-US"}]{#struct_0_73523_x1515_869641963}

[[SNMP get]{lang="EN-US"}]{#struct_0_73523_x1515_1774249178}[请求]{style="font-family:宋体"}

[[Set request]{lang="EN-US"}]{#struct_0_73523_x1515_x945480744}

[[SNMP set]{lang="EN-US"}]{#struct_0_73523_x1515_x678948526}[请求]{style="font-family:宋体"}

[[Get-next request]{lang="EN-US"}]{#struct_0_73523_x1515_2111528461}

[[SNMP get-next]{lang="EN-US"}]{#struct_0_73523_x1515_928685473}[请求]{style="font-family:宋体"}

[[Get-bulk request]{lang="EN-US"}]{#struct_0_73523_x1515_1774576858}

[[SNMP get-bulk]{lang="EN-US"}]{#struct_0_73523_x1515_1750396928}[请求]{style="font-family:宋体"}

[[Non-repeaters: *non-repeaters*]{lang="EN-US"}]{#struct_0_73523_x1515_1182165391}

[[get-bulk]{lang="EN-US"}]{#struct_0_73523_x1515_1248050771}[请求操作的]{style="font-family:宋体"}[non-repeaters]{lang="EN-US"}[字段]{style="font-family:宋体"}

[[Max-repetitions: *max-repetitions*]{lang="EN-US"}]{#struct_0_73523_x1515_1774642394}

[[get-bulk]{lang="EN-US"}]{#struct_0_73523_x1515_x1375134205}[请求操作的]{style="font-family:宋体"}[max-repetitions]{lang="EN-US"}[字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging snmp agent packet send]{lang="EN-US"}]{#struct_0_73523_x1515_x2047500256}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1498126895}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_x994003582}

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_x949500056}

[[PACKET]{lang="EN-US"}]{#struct_0_73523_x1515_1361121588}

[[报文包含的信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_1774445786}

[[PACKET_DES]{lang="EN-US"}]{#struct_0_73523_x1515_2118554203}

[[报文目的地址信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_x416494797}

[[Packet sent to *address* via UDP]{lang="EN-US"}]{#struct_0_73523_x1515_x1521179376}

[[通过]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_73523_x1515_130325551}[协议发送给]{style="font-family:宋体"}*[address]{lang="EN-US"}*[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[*[address]{lang="EN-US"}*]{#struct_0_73523_x1515_x657298638}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文的目的地址]{style="font-family:宋体"}

[[Request ID: *request-id*]{lang="EN-US"}]{#struct_0_73523_x1515_1774511322}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x969949238}[响应报文的编号（用于匹配]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文）]{style="font-family:宋体"}

[[Error status: *error-status*]{lang="EN-US"}]{#struct_0_73523_x1515_x468389525}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x648744792}[响应报文中的错误状态]{style="font-family:宋体"}

[[Error index: error-index]{lang="EN-US"}]{#struct_0_73523_x1515_x1262076149}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x2118160317}[响应报文中的错误索引]{style="font-family:宋体"}

[[VBLIST]{lang="EN-US"}]{#struct_0_73523_x1515_1774839002}

[[变量绑定对列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_1008409227}

[[Response]{lang="EN-US"}]{#struct_0_73523_x1515_x736150309}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x945954289}[响应报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1453244593}

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_1774904538}[在一台启动了]{style="font-family:宋体"}[SNMP v1]{lang="EN-US"}[功能并配置相应读写团体名的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文消息头调试开关，使用网管软件访问设备。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_943588940}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent packet header]{lang="EN-US"}

[\*Jul 27 08:37:26:313 2007 Sysname SNMP/7/HEADER:]{lang="EN-US"}

[   Incoming SNMPv1 packet]{lang="EN-US"}

[   Community name: public]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_x118135832}*[设备接收到版本为]{style="font-family:宋体"}[v1]{lang="EN-US"}[的请求报文，团体名为]{style="font-family:宋体"}[public]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_x1220923414}[在一台启动了]{style="font-family:宋体"}[SNMP v2c]{lang="EN-US"}[功能并配置相应读写团体名的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文消息头调试开关，使用网管软件访问设备。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_756911811}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent packet header]{lang="EN-US"}

[\*Jul 27 08:37:26:313 2007 Sysname SNMP/7/HEADER:]{lang="EN-US"}

[   Incoming SNMPv2c packet]{lang="EN-US"}

[   Community name: private]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_1892521293}*[设备接收到版本为]{style="font-family:宋体"}[v2c]{lang="EN-US"}[的请求报文，团体名为]{style="font-family:宋体"}[private]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_1774314715}[在一台启动了]{style="font-family:宋体"}[SNMP v3]{lang="EN-US"}[功能并配置相应组、用户名的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文消息头调试开关，使用网管软件访问设备。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_554567572}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent packet header]{lang="EN-US"}

[\*Jul 27 08:51:00:563 2007 Sysname SNMP/7/HEADER:]{lang="EN-US"}

[   Incoming SNMPv3 packet]{lang="EN-US"}

[   Security model: v3]{lang="EN-US"}

[   Security level: AuthNoPriv]{lang="EN-US"}

[   User name: v3user1]{lang="EN-US"}

[   SnmpEngineID: 000063A27F00000100001707]{lang="EN-US"}

[   SnmpEngineBoots: 1]{lang="EN-US"}

[   SnmpEngineTime: 54591]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_x1066478140}*[设备接收到版本为]{style="font-family:宋体"}[v3]{lang="EN-US"}[的请求报文，安全模型为]{style="font-family:宋体"}[v3]{lang="EN-US"}[，安全级别为认证不加密，用户名为]{style="font-family:宋体"}[v3user1]{lang="EN-US"}[，]{style="font-family:宋体"} [SNMP]{lang="EN-US"}[引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[000063A27F00000100001707]{lang="EN-US"}[，其重启次数为]{style="font-family:宋体"}[1]{lang="EN-US"}[，运行时间为]{style="font-family:宋体"}[54591]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_x2013048288}[在一台启动了]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[功能并配置相应读写团体名的设备上打开信息中心调试开关和接收到的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[数据包调试信息开关，使用网管软件对设备上的]{style="font-family:宋体"}[sysUpTime.0]{lang="EN-US"}[对象进行]{style="font-family:宋体"}[get]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_1774380251}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent packet receive]{lang="EN-US"}

[\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/PACKET_SRC:]{lang="EN-US"}

[   Packet received from 10.165.81.75 via UDP]{lang="EN-US"}

[\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/PACKET:]{lang="EN-US"}

[   Get request]{lang="EN-US"}

[   Request ID: 13]{lang="EN-US"}

[   Error status: 0]{lang="EN-US"}

[   Error index: 0]{lang="EN-US"}

[\*Jul 27 08:58:52:594 2007 Sysname SNMP/7/VBLIST:]{lang="EN-US"}

[   sysUpTime.0:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_x555862740}*[设备接收到来自]{style="font-family:宋体"}[10.165.81.75]{lang="EN-US"}[，通过]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文传递的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文，消息的操作类型为]{style="font-family:宋体"}[get]{lang="EN-US"}[请求，请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[13]{lang="EN-US"}[，错误状态为]{style="font-family:宋体"}[0]{lang="EN-US"}[，错误索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，绑定变量为]{style="font-family:宋体"}[sysUpTime.0]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_x1323300398}[在一台启动了]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[功能并配置相应读写团体名的设备上打开信息中心调试开关和发送的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[数据包调试信息开关，使用网管软件对设备上的]{style="font-family:宋体"}[sysUpTime.0]{lang="EN-US"}[对象进行]{style="font-family:宋体"}[get]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_x1138749266}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent packet send]{lang="EN-US"}

[\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/PACKET:]{lang="EN-US"}

[   Response]{lang="EN-US"}

[   Request ID: 16]{lang="EN-US"}

[   Error status: 0]{lang="EN-US"}

[   Error index: 0]{lang="EN-US"}

[\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/VBLIST:]{lang="EN-US"}

[   sysUpTime.0: 5563114]{lang="EN-US"}

[\*Jul 27 09:08:21:563 2007 Sysname SNMP/7/PACKET_DES:]{lang="EN-US"}

[   Packet sent to 10.165.81.75 via UDP]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_1774183643}*[设备向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.165.81.75]{lang="EN-US"}[的网管发送]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[响应报文，报文类型为]{style="font-family:宋体"}[response]{lang="EN-US"}[，对应的请求报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[16]{lang="EN-US"}[，错误状态为]{style="font-family:宋体"}[0]{lang="EN-US"}[，错误索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，绑定变量为]{style="font-family:宋体"}[sysUpTime.0]{lang="EN-US"}[，值为]{style="font-family:宋体"}[5563114]{lang="EN-US"}*[。]{style="font-family:宋体"}

::: {#948925407 .myid}
[]{#_Toc404796822}[]{#struct_0_73523_x1515_x1357141626}[]{#_Toc263690036}[]{#_Toc206560111}

**SNMP \-- SNMP调试命令 \-- debugging snmp agent process**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_73523_x1515_1827742078}

[**[debugging snmp agent]{lang="EN-US"}**[ **process** { **all** \| **decode** \| **stack** \| **txrx** } \[ **error** \| **info** \| **warning** \]]{lang="EN-US"}]{#struct_0_73523_x1515_x1884218180}

[**[undo debugging snmp agent process]{lang="EN-US"}**[ { **all** \| **decode** \| **stack** \| **txrx** } \[ **error** \| **info** \| **warning** \]]{lang="EN-US"}]{#struct_0_73523_x1515_1522663029}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1446014612}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73523_x1515_x330563128}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73523_x1515_900028173}

[[network-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x940329396}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73523_x1515_1774249179}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x945415208}

[**[all]{lang="EN-US"}**]{#struct_0_73523_x1515_1283306365}[：表示]{style="font-family:宋体"}[Agent]{lang="EN-US"}[运行时各阶段（包括]{style="font-family:宋体"}**[decode]{lang="EN-US"}**[、]{style="font-family:宋体"}**[stack]{lang="EN-US"}**[和]{style="font-family:宋体"}**[txrx]{lang="EN-US"}**[）的调试信息开关。]{style="font-family:宋体"}

[**[decode]{lang="EN-US"}**]{#struct_0_73523_x1515_1359831241}[：表示]{style="font-family:宋体"}[Agent]{lang="EN-US"}[解析]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文时的调试信息开关。]{style="font-family:宋体"}

[**[stack]{lang="EN-US"}**]{#struct_0_73523_x1515_x330518670}[：表示]{style="font-family:宋体"}[Agent]{lang="EN-US"}[处理]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文中]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时的调试信息开关。]{style="font-family:宋体"}

[**[txrx]{lang="EN-US"}**]{#struct_0_73523_x1515_x673478833}[：表示]{style="font-family:宋体"}[Agent]{lang="EN-US"}[收发]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[消息时的调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_73523_x1515_x1339335255}[：表示调试信息等级为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的错误信息。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_73523_x1515_1224426195}[：表示调试信息等级为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的提示信息。]{style="font-family:宋体"}

[**[warning]{lang="EN-US"}**]{#struct_0_73523_x1515_1774576859}[：表示调试信息等级为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的重要信息。]{style="font-family:宋体"}

[[若在调试开关命令中不指定输出调试信息的等级，则输出]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_73523_x1515_1750331392}[关闭所有等级的调试信息。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1227247473}

[**[debugging snmp agent process]{lang="EN-US"}**]{#struct_0_73523_x1515_245116843}[命令用来打开]{style="font-family:
宋体"}[Agent]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging snmp agent process]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[Agent]{lang="EN-US"}[的调试信息开关。缺省情况下，]{style="font-family:宋体"}[Agent]{lang="EN-US"}[的调试信息开关都处于关闭状态。缺省情况下，]{style="font-family:宋体"}[Agent]{lang="EN-US"}[的调试信息开关都处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging snmp agent process decode]{lang="EN-US"}]{#struct_0_73523_x1515_285129988}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1503859343}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_1888897171}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_1569772608}

[[DECODE_INFO]{lang="EN-US"}]{#struct_0_73523_x1515_1084308640}

[[解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1774642395}[请求报文时调试级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[DECODE_WARNING]{lang="EN-US"}]{#struct_0_73523_x1515_x1375068669}

[[解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x616281431}[请求报文时调试级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[DECODE_ERROR]{lang="EN-US"}]{#struct_0_73523_x1515_x854237858}

[[解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_2070725029}[请求报文时调试级别]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[Decode SNMP request]{lang="EN-US"}]{#struct_0_73523_x1515_x496662982}

[[解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1774445787}[请求]{style="font-family:宋体"}

[[Failed to parse ASN.1 data while decoding SNMP request]{lang="EN-US"}]{#struct_0_73523_x1515_2118619739}

[[解析]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_762194210}[请求报文中的]{style="font-family:宋体"}[ASN.1]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to decode SNMPv3 message version (*version*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1642331016}

[[解码]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1029197090}[消息版本失败]{style="font-family:宋体"}

[*[version]{lang="EN-US"}*]{#struct_0_73523_x1515_1774511323}[：]{style="font-family:宋体"}[解析出的版本]{style="font-family:宋体"}

[[Failed to decode SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x970014774}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x578235388}[（]{style="font-family:宋体"}[protocol data unit]{lang="EN-US"}[，协议数据单元）失败]{style="font-family:宋体"}

[[Failed to decode SNMPv1/v2c PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x1925750875}

[[解码]{style="font-family:宋体"}[SNMPv1/v2c PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1793909089}[失败]{style="font-family:宋体"}

[[Failed to decode SNMP message version]{lang="EN-US"}]{#struct_0_73523_x1515_1774839003}

[[解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1008343691}[消息版本失败]{style="font-family:宋体"}

[[Decode SNMPv1/v2c request PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1266331499}

[[解码]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}]{#struct_0_73523_x1515_x1531393917}[请求]{style="font-family:宋体"}[PDU]{lang="EN-US"}

[[Failed to decode community and version]{lang="EN-US"}]{#struct_0_73523_x1515_191616596}

[[解码团体名和版本失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1774904539}

[[Failed to decode PDU type, request ID, error status, and error index]{lang="EN-US"}]{#struct_0_73523_x1515_943654476}

[[解码]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x2135334866}[类型、请求报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[、错误状态和错误索引失败]{style="font-family:宋体"}

[[Failed to decode variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_x275865828}

[[解码变量绑定列表失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x848076586}

[[Parse community and version]{lang="EN-US"}]{#struct_0_73523_x1515_1774314712}

[[解析团体名和版本]{style="font-family:宋体"}]{#struct_0_73523_x1515_554239892}

[[Parse PDU type, request ID, error status, and error index]{lang="EN-US"}]{#struct_0_73523_x1515_x194652214}

[[解析]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_2078096688}[类型、请求报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[、错误状态和错误索引]{style="font-family:宋体"}

[[Decode variable-binding]{lang="EN-US"}]{#struct_0_73523_x1515_1774380248}

[[解码变量绑定对]{style="font-family:宋体"}]{#struct_0_73523_x1515_x556452563}

[[Failed to parse value while decoding variable-binding]{lang="EN-US"}]{#struct_0_73523_x1515_x1850144424}

[[解码变量绑定对时解析其绑定值失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1107947494}

[[Failed to parse OID while decoding variable-binding]{lang="EN-US"}]{#struct_0_73523_x1515_1774183640}

[[解码变量绑定对时解析其绑定]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_73523_x1515_x1357338234}[（]{style="font-family:宋体"}[object identifier]{lang="EN-US"}[，对象标识符）失败]{style="font-family:宋体"}

[[Parse value in variable-binding]{lang="EN-US"}]{#struct_0_73523_x1515_x188535861}

[[解析变量绑定对中的绑定值]{style="font-family:宋体"}]{#struct_0_73523_x1515_1192201172}

[[Parse OID in variable-binding]{lang="EN-US"}]{#struct_0_73523_x1515_1774249176}

[[解析变量绑定对中的绑定]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_73523_x1515_x945611816}

[[Decode SNMP message version]{lang="EN-US"}]{#struct_0_73523_x1515_1697089066}

[[解析]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1363033919}[消息版本]{style="font-family:宋体"}

[[SNMP message version decoding failure: Invalid version.]{lang="EN-US"}]{#struct_0_73523_x1515_1774576856}

[[解析出的版本无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_1750790144}

[[Decode SNMPv3 message version]{lang="EN-US"}]{#struct_0_73523_x1515_1905730731}

[[解码]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1774642392}[消息版本]{style="font-family:宋体"}

[[Decode SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x1375265277}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1578756651}

[[Failed to parse message ID while decoding SNMPv3 PDU ]{lang="EN-US"}]{#struct_0_73523_x1515_1774445784}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_2118423131}[时解析消息]{style="font-family:宋体"}[ID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[SNMPv3 PDU decoding failure: PDU size (*max-size*)smaller than the required minimum PDU size(*min-size*).]{lang="EN-US"}]{#struct_0_73523_x1515_401513306}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x1818914322}[时消息最大数据长度小于系统设定的最小值]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1774511320}[：接收消息的最大数据长度]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[min-size]{lang="EN-US"}*]{#struct_0_73523_x1515_x969818166}[：系统设定的消息最小数据长度]{lang="EN-US" style="font-family:宋体"}

[[Failed to parse message flags while decoding SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x1613792018}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774839000}[时解析消息标志位失败]{style="font-family:宋体"}

[[Failed to parse security model (*security-model*) ]{lang="EN-US"}]{#struct_0_73523_x1515_1008278155}

[[解析消息安全模型失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x759314169}

[*[security-model]{lang="EN-US"}*]{#struct_0_73523_x1515_1774904536}[：安全模型值]{style="font-family:宋体"}

[[Failed to parse authoritative engine ID]{lang="EN-US"}]{#struct_0_73523_x1515_942933580}

[[解析权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_73523_x1515_x1295453126}[失败]{style="font-family:宋体"}

[[Unknown engine ID]{lang="EN-US"}]{#struct_0_73523_x1515_1774314713}

[[未知的引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_73523_x1515_554174356}

[[Failed to authenticate SNMPv3 message]{lang="EN-US"}]{#struct_0_73523_x1515_1774380249}

[[认证]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_x556387027}[消息失败]{style="font-family:宋体"}

[[Failed to decrypt SNMPv3 message]{lang="EN-US"}]{#struct_0_73523_x1515_x1444298232}

[[解密]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1774183641}[消息失败]{style="font-family:宋体"}

[[SNMPv3 message not in time window]{lang="EN-US"}]{#struct_0_73523_x1515_x1357272698}

[[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1368907335}[消息不在时间窗内]{style="font-family:宋体"}

[[Unknown security model (*security-model*)]{lang="EN-US"}]{#struct_0_73523_x1515_1774249177}

[[未知的安全模型]{style="font-family:宋体"}]{#struct_0_73523_x1515_x945546280}

[*[security-model]{lang="EN-US"}*]{#struct_0_73523_x1515_1677481365}[：安全模型值]{style="font-family:宋体"}

[[SNMPv3 PDU decoding failure: Unknown PDU handler.]{lang="EN-US"}]{#struct_0_73523_x1515_1774576857}

[[解码]{style="font-family:宋体"}[SNMPv3 PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1750724608}[时解析出未知的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[处理者]{style="font-family:宋体"}

[[Decrypt security parameters in SNMPv3 message]{lang="EN-US"}]{#struct_0_73523_x1515_1774642393}

[[解密]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_x1375199741}[消息中的安全参数]{style="font-family:宋体"}

[[SNMPv3 message decoding failure: Wrong security level (*security-level*). ]{lang="EN-US"}]{#struct_0_73523_x1515_472410683}

[[解析出错误的安全级别]{style="font-family:宋体"}]{#struct_0_73523_x1515_1774445785}

[*[security-level]{lang="EN-US"}*]{#struct_0_73523_x1515_2118488667}[：安全级别值]{style="font-family:宋体"}

[[Failed to decode security parameters]{lang="EN-US"}]{#struct_0_73523_x1515_1774511321}

[[解码安全参数失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x969883702}

[[Decode security parameters in SNMPv3 message]{lang="EN-US"}]{#struct_0_73523_x1515_x2028437607}

[[解码]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1774839001}[消息中的安全参数]{style="font-family:宋体"}

[[Authoritative engine ID in SNMPv3 message doesn\'t match entity engine ID.]{lang="EN-US"}]{#struct_0_73523_x1515_1008212619}

[[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1774904537}[消息中的权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[与实体引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Failed to validate authentication protocol version]{lang="EN-US"}]{#struct_0_73523_x1515_942999116}

[[认证协议版本验证失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1444136814}

[[SNMPv3 message decoding failure: Unsupported security level (*security-level*).]{lang="EN-US"}]{#struct_0_73523_x1515_1774314710}

[[解码安全参数时解析出不支持的安全级别]{style="font-family:宋体"}]{#struct_0_73523_x1515_554370964}

[*[security-level]{lang="EN-US"}*]{#struct_0_73523_x1515_1774380246}[：安全级别值]{style="font-family:宋体"}

[[SNMPv3 message decoding failure: Unknown username.]{lang="EN-US"}]{#struct_0_73523_x1515_x556059347}

[[解码安全参数时解析出未知的用户名]{style="font-family:宋体"}]{#struct_0_73523_x1515_1774183638}

[[SNMPv3 message decoding failure: Invalid USM parameter.]{lang="EN-US"}]{#struct_0_73523_x1515_x1357862525}

[[解码安全参数时解析出无效的]{style="font-family:宋体"}[USM]{lang="EN-US"}]{#struct_0_73523_x1515_1535824802}[（]{style="font-family:宋体"}[User-based Security Model]{lang="EN-US"}[，基于用户的安全模型）参数]{style="font-family:宋体"}

[[SNMPv3 message decoding failure: Invalid authoritative engine ID.]{lang="EN-US"}]{#struct_0_73523_x1515_1774249174}

[[解码安全参数时解析出无效的权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_73523_x1515_x945742888}

[[Failed to parse authentication parameters while decoding security parameters]{lang="EN-US"}]{#struct_0_73523_x1515_1774576854}

[[解码安全参数时解析认证参数失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1750659072}

[[Failed to parse authoritative engine uptime while decoding security parameters]{lang="EN-US"}]{#struct_0_73523_x1515_1774642390}

[[解码安全参数时解析权威引擎运行时间失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1375396349}

[[Failed to parse number of authoritative engine boots while decoding security parameters]{lang="EN-US"}]{#struct_0_73523_x1515_1774445782}

[[解码安全参数时解析权威引擎启动次数失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_2118292059}

[[Failed to parse authoritative engine ID while decoding security parameters]{lang="EN-US"}]{#struct_0_73523_x1515_1774511318}

[[解码安全参数时解析权威引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_73523_x1515_x969293881}[失败]{style="font-family:宋体"}

[[Decode scoped PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x2070970773}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774838998}

[[Failed to parse context engineID while decoding scoped PDU]{lang="EN-US"}]{#struct_0_73523_x1515_252022575}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774904534}[时解析上下文引擎]{style="font-family:宋体"}[ID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[SNMP scoped PDU decoding failure: PDU size (]{lang="EN-US"}]{#struct_0_73523_x1515_942802508}[*[parsed-PDU-size]{lang="EN-US"}*]{.ItemListinTableCharChar}[) larger than the required maximum PDU size (]{lang="EN-US"}[*[max-PDU-size]{lang="EN-US"}*]{.ItemListinTableCharChar}[). ]{lang="EN-US"}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774314711}[时解析出的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[大小大于系统预设的最大值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parsed-PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_554305428}*[：]{lang="EN-US" style="font-family:宋体"}*[解析出的]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1774380247}*[：]{lang="EN-US" style="font-family:
  宋体"}*[系统预设的最大]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[Failed to decode variable-bindings while decoding scoped PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x555993811}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774183639}[时解码变量绑定列表失败]{style="font-family:宋体"}

[[SNMP scoped PDU decoding failure: Wrong PDU size. ]{lang="EN-US"}]{#struct_0_73523_x1515_x1357796989}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774249175}[时加密]{style="font-family:宋体"}[PDU]{lang="EN-US"}[大小有误]{style="font-family:宋体"}

[[Failed to parse context name while decoding scoped PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x945677352}

[[解码加密的]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1774576855}[时解析上下文名字失败]{style="font-family:宋体"}

[[Decrypt SNMPv3 message]{lang="EN-US"}]{#struct_0_73523_x1515_1750593536}

[[解密]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}]{#struct_0_73523_x1515_1774642391}[消息]{style="font-family:宋体"}

[[Check time window]{lang="EN-US"}]{#struct_0_73523_x1515_x1375330813}

[[检查时间窗]{style="font-family:宋体"}]{#struct_0_73523_x1515_1774445783}

[[SNMP request successfully decoded ]{lang="EN-US"}]{#struct_0_73523_x1515_2118357595}

[[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1774511319}[请求报文解码成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging snmp agent process txrx]{lang="EN-US"}]{#struct_0_73523_x1515_x969359417}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1487914191}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1613041497}

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_x517490169}

[[TXRX_INFO]{lang="EN-US"}]{#struct_0_73523_x1515_1774838999}

[[收发]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_251957039}[消息时调试级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[TXRX_WARNING]{lang="EN-US"}]{#struct_0_73523_x1515_500037823}

[[收发]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x585517084}[消息时调试级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[TXRX_ERROR]{lang="EN-US"}]{#struct_0_73523_x1515_x1871797597}

[[收发]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1296498058}[消息时调试级别为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[Create IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1774904535}

[[创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_942868044}

[[Failed to create IPv4 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_x496938686}

[[创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_319652282}[失败]{style="font-family:宋体"}

[[Failed to set IPv4 socket to nonblocking while creating IPv4 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_1215326044}

[[创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954568641}[时设置]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}[属性为非阻塞失败]{style="font-family:宋体"}

[[Failed to set IPv4 socket to asynchronizing while creating IPv4 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_1749391174}

[[创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_838776980}[时设置]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}[属性为异步失败]{style="font-family:宋体"}

[[Failed to bind IP address and port while creating IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1443143493}

[[创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_2079526993}[时绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号失败]{style="font-family:宋体"}

[[Create IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_476832834}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954503105}

[[Failed to create IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x537619303}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_763302673}[失败]{style="font-family:宋体"}

[[Failed to set IPv6 socket to nonblocking while creating IPv6 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_x2018176419}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_558345607}[时设置]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}[属性为非阻塞时失败]{style="font-family:宋体"}

[[Failed to set IPv6 socket to asynchronizing while creating IPv6 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_x954699713}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1382818567}[时设置]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}[属性为异步失败]{style="font-family:宋体"}

[[Failed to set IPv6 socket option while creating IPv6 socket (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1159999080}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1773632203}[时设置]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}[属性失败（该属性控制本]{style="font-family:宋体"}[socket]{lang="EN-US"}[使用的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号能否再与其他]{style="font-family:宋体"}[socket]{lang="EN-US"}[绑定）]{style="font-family:宋体"}

[*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954634177}[：错误码]{style="font-family:宋体"}

[[Failed to bind IP address and port while creating IPv6 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_1034559584}

[[创建]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1732003005}[时绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号失败]{style="font-family:宋体"}

[[Create socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1460303435}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954306497}

[[Failed to create IPv4 socket while initializing socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1708444017}

[[初始化]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_73523_x1515_x615850467}[时创建]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Send PDU through IPv4 socket at  *time-hour:time-minute:time-second* (PDU size: *PDU-size*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1873620194}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954240961}[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}[并打出时间戳显示发送时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_1817899489}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x272812958}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_2006117428}[[：]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[秒]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_x954437569}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[Failed to send PDU through IPv4 socket at *time-hour:time-minute:time-second* (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2092055982}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_440927065}[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}[失败并打出时间戳显示发送时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_975507246}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x954372033}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x148109067}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x1128125896}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Sending PDU through IPv6 socket failure: Invalid interface index. ]{lang="EN-US"}]{#struct_0_73523_x1515_x954044353}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_639180596}[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}[的接口索引无效]{style="font-family:宋体"}

[[Send PDU through IPv6 socket at  *time-hour:time-minute:time-second* (PDU size*: PDU-size*)]{lang="EN-US"}]{#struct_0_73523_x1515_x530212353}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x953978817}[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}[并打出时间戳显示发送时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_357537735}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x453283035}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_1339528211}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PDU-size]{lang="EN-US"}]{#struct_0_73523_x1515_x954568640}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[Failed to send PDU through IPv6 socket at *time-hour:time-minute:time-second* (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1749325638}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_454485540}[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}[失败并打出时间戳显示发送时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_x954503104}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x537684839}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x954699712}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1382884103}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[PDU sending failure: Invalid destination address. ]{lang="EN-US"}]{#struct_0_73523_x1515_x2018752298}

[[发送]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x954634176}[时目的地址无效]{style="font-family:宋体"}

[[Failed to set IPv4 socket option while receiving PDU through IPv4 socket ]{lang="EN-US"}]{#struct_0_73523_x1515_1034625120}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1708405296}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时设置]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}[属性失败（该属性控制是否能从收到的报文里解析出目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）]{style="font-family:宋体"}

[[System is busy while receiving PDU through IPv4 socket.]{lang="EN-US"}]{#struct_0_73523_x1515_x954306496}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1708509553}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时系统正忙]{style="font-family:宋体"}

[[Receive PDU (*PDU-size*) when SNMP agent is disabled ]{lang="EN-US"}]{#struct_0_73523_x1515_x1961676384}

[[接收到]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x954240960}[，但是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[服务器没有使能]{style="font-family:宋体"}

[*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1817833953}[：]{style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{style="font-family:宋体"}

[[Receive PDU through IPv4 socket at *time-hour:time-minute:time-second* (PDU size: *PDU-size*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1857706417}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954437568}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[并打出时间戳显示接收时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_x2091990446}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_1157648637}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x954372032}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_x148043531}*[：]{lang="EN-US" style="font-family:
  宋体"}*[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to receive PDU through IPv4 socket at *time-hour:time-minute:time-second*  (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954044352}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_639115060}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[失败并打出时间戳显示接收时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_x929744185}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x953978816}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_357603271}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_572134843}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Receive PDU through IPv6 socket at *time-hour:time-minute:time-second* (PDU size: *PDU-size*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954568643}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1749522246}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[并打出时间戳显示接收时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_x954503107}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x537750375}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x1150229834}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_x954699715}*[：]{lang="EN-US" style="font-family:
  宋体"}*[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to receive PDU through IPv6 socket at *time-hour:time-minute:time-second* (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1382949639}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954634179}[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}[失败并打出时间戳显示接收时间]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_1034952800}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_x954306499}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x1708050801}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1512152562}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to read queue while receiving PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x954240963}

[[接收]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1817768417}[时读队列失败]{style="font-family:宋体"}

[[Close SNMP agent IPv4/IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x954437571}

[[关闭]{style="font-family:宋体"}[SNMP agent socket]{lang="EN-US"}]{#struct_0_73523_x1515_x2092580271}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging snmp agent process stack]{lang="EN-US"}]{#struct_0_73523_x1515_x783455956}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1193647759}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_x699233291}

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_x954372035}

[[STACK_INFO]{lang="EN-US"}]{#struct_0_73523_x1515_x148240139}

[[处理]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1882845015}[请求报文中]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时调试级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[STACK_WARNING]{lang="EN-US"}]{#struct_0_73523_x1515_x722401546}

[[处理]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1190234634}[请求报文中]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时调试级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[STACK_ERROR]{lang="EN-US"}]{#struct_0_73523_x1515_648841091}

[[处理]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x954044355}[请求报文中]{style="font-family:宋体"}[PDU]{lang="EN-US"}[时调试级别为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息]{style="font-family:宋体"}

[[Create MOR message for get-request and parse MOR messageMOR message for response]{lang="EN-US"}]{#struct_0_73523_x1515_639049524}

[[创建]{style="font-family:宋体"}[get]{lang="EN-US"}]{#struct_0_73523_x1515_x2142988167}[请求报文，解析响应消息]{style="font-family:宋体"}

[[Get-request processing failure: Invalid variable-bindings.]{lang="EN-US"}]{#struct_0_73523_x1515_x576151716}

[ ]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[get]{lang="EN-US"}]{#struct_0_73523_x1515_979078495}[请求时变量绑定列表无效]{style="font-family:宋体"}

[[Get-request processing failure: No such node.]{lang="EN-US"}]{#struct_0_73523_x1515_x953978819}

[[处理]{style="font-family:宋体"}[get]{lang="EN-US"}]{#struct_0_73523_x1515_357406663}[请求时无此节点]{style="font-family:宋体"}

[[Failed to create MOR message while handling get-request (node name: *node-name*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x462559195}

[[处理]{style="font-family:宋体"}[get]{lang="EN-US"}]{#struct_0_73523_x1515_x987369231}[请求时创建]{style="font-family:宋体"}[MOR]{lang="EN-US"}[（]{style="font-family:宋体"}[Managed Object Repository]{lang="EN-US"}[，配置管理对象）消息失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1572869199}*[：]{lang="EN-US" style="font-family:
  宋体"}*[节点名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954568642}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to send command or get response while handling get-request (node name: *node-name*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1749456710}

[[处理]{style="font-family:宋体"}[get]{lang="EN-US"}]{#struct_0_73523_x1515_x1489991760}[请求时发送命令或获取响应失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1459984274}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_126701953}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Create MOR message for set-request and parse MOR message for response]{lang="EN-US"}]{#struct_0_73523_x1515_x954503106}

[[创建]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_x537815911}[请求报文，解析响应消息]{style="font-family:宋体"}

[[Failed to create MOR message while handling set-request (node name: *node-name*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x6972400}

[[处理]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_189941606}[请求时创建]{style="font-family:宋体"}[MOR]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x954699714}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1383015175}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to send command or get response while handling set-request (node name: *node-name*, error code: * error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1122221694}

[[处理]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1580837044}[请求时发送命令或取得响应失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x954634178}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1035018336}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Create MOR message for get-next-request and parse MOR message for response]{lang="EN-US"}]{#struct_0_73523_x1515_193509876}

[[创建]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_1264302585}[请求报文，解析响应消息]{style="font-family:宋体"}

[[Create MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_x954306498}

[[创建]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x1708116337}[请求消息]{style="font-family:宋体"}

[[MOR message building failure: Invalid node. ]{lang="EN-US"}]{#struct_0_73523_x1515_x258316491}

[[构造]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1492465295}[消息时节点无效]{style="font-family:宋体"}

[[Failed to create MOR message for leaf node *node-name* while building MOR message (error code: *err-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954240962}

[[构造]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1817702881}[消息时创建叶子节点的]{style="font-family:宋体"}[MOR]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1087169658}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1778996098}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append index node *node-name*'s value to MOR message while building MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954437570}

[[构造]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x2092514735}[消息时向]{style="font-family:宋体"}[MOR]{lang="EN-US"}[消息添加索引节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1867419948}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954372034}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append column node *node-name*'s value to MOR message while building MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x148174603}

[[构造]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_893009503}[消息时向]{style="font-family:宋体"}[MOR]{lang="EN-US"}[消息添加列节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_20637596}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954044354}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Append index node's value to MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_638983988}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x855889232}[消息添加索引节点值]{style="font-family:宋体"}

[[Failed to get index node *node-name*'s value  by OID while appending index value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x953978818}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_357472199}[消息添加索引值时通过]{style="font-family:宋体"}[OID]{lang="EN-US"}[（]{style="font-family:宋体"}[object identifier]{lang="EN-US"}[，对象标识符）获取索引节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1966557181}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954568645}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to check validity of *node-name*\'s value while appending index value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1749653318}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_33672953}[消息添加索引值时数据有效性检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_2114685650}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954503109}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append index node *node-name*'s value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x537357159}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x365394821}[消息添加索引节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x954699717}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1383080711}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Append column node's value to MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_x954634181}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1034428519}[消息添加列节点值]{style="font-family:宋体"}

[[Set instance *instance* in batches]{lang="EN-US"}]{#struct_0_73523_x1515_171424110}

[[以批量处理的方式设置实例]{style="font-family:宋体"}]{#struct_0_73523_x1515_x954306501}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_630077062}[：实例]{style="font-family:宋体"}

[[Set instance * instance* in batches]{lang="EN-US"}]{#struct_0_73523_x1515_x2045967008}

[[以批量处理的方式获取实例]{style="font-family:宋体"}]{#struct_0_73523_x1515_x954240965}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_1817637345}[：实例]{style="font-family:宋体"}

[[Get *instance*'s next instance in batches]{lang="EN-US"}]{#struct_0_73523_x1515_x1443399302}

[[以批量处理的方式获取下一个实例]{style="font-family:宋体"}]{#struct_0_73523_x1515_x954437573}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_x2092711343}[：实例]{style="font-family:宋体"}

[[Failed to get *node-name*\'s brother node while appending column node's value to MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_x954372037}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x148371211}[消息添加列节点值时取兄弟节点失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1877637751}[：节点名]{style="font-family:宋体"}

[[Instance *instance* doesn't exist while appending column node's value to MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_x954044357}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_638918452}[消息添加列节点值时实例不存在]{style="font-family:宋体"}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_x1251464202}[：实例]{style="font-family:宋体"}

[[Failed to check *node-name*\'s access permission or VACM while appending column node's value to MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_x953978821}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_357930948}[消息添加列节点值时访问权限或]{style="font-family:宋体"}[VACM]{lang="EN-US"}[（]{style="font-family:宋体"}[View-based Access Control Model]{lang="EN-US"}[，基于视图的访问控制模型）检查失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x954568644}[：节点名]{style="font-family:宋体"}

[[Failed to check validity of *node-name*\'s value while appending column node's value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1749587782}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1269234739}[消息添加列节点值时数据有效性检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x954503108}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[err-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x537422695}*[：]{style="font-family:宋体"}*[错误码]{style="font-family:宋体"}

[[Failed to handle index node *node-name* while appending column node's value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954699716}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1383146247}[消息添加列节点值时处理索引节点失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x797876083}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954634180}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append column node *node-name'*s value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_1034494055}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x954306500}[消息添加列节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_630011526}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x954240964}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Fill variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_1817571809}

[[填充变量绑定列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_1636798439}

[[Get value from MOR message (MOR type: *MOR-type*)]{lang="EN-US"}]{#struct_0_73523_x1515_x954437572}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x2092645807}[消息中取值]{style="font-family:宋体"}

[*[MOR-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x954372036}[：]{style="font-family:宋体"}[MOR]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Parse MOR message and fill variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_x148305675}

[[解析]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x954044356}[响应消息，填充变量绑定列表]{style="font-family:宋体"}

[[Failed to get *node-name*\'s MOR while parsing MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_638852916}

[[解析]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x953978820}[消息时取节点对应]{style="font-family:宋体"}[MOR]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_357996484}[：节点名]{style="font-family:宋体"}

[[Failed to get *node-name*\'s value from MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611515300}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x2037347986}[响应消息中取节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611580836}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_265063806}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to check validity of *node-name*\'s value while parsing MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611384228}

[[解析]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_43581290}[消息时数据有效性检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611449764}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x122070085}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to convert *node-name*\'s data type from MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611777444}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x607602431}[消息中转换数据类型失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611842980}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1108023129}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to check validity of *node-name*\'s value while parsing MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611646372}

[[解析]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_938576205}[消息时，数据有效性检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611711908}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x241887356}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Convert data type *data-type* from MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_612039588}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_2108733423}[消息中转换数据类型]{style="font-family:宋体"}

[*[data-type]{lang="EN-US"}*]{#struct_0_73523_x1515_612105124}[：数据类型]{style="font-family:宋体"}

[[Invalid node while handling get-next-request]{lang="EN-US"}]{#struct_0_73523_x1515_611515301}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x2037347987}[请求时节点无效]{style="font-family:宋体"}

[[Failed to create MOR message while handling get-next-request (node name: *node-name*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611580837}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_265063807}[请求时创建]{style="font-family:宋体"}[MOR]{lang="EN-US"}[消息失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611384229}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_43581291}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to send command or get response while handling get-next-request (node name: *node-name*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611449765}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x122070084}[请求时发送命令或取得响应失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611777445}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x607602432}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append column node *node-name*'s value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611842981}

[[添加列节点值至]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_611646373}[消息失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_938576206}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_611711909}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append index node *node-name*'s value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x241887357}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_612039589}[消息添加索引节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_2108733422}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_612105125}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to append column node *node-name*'s value to MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611515298}

[[向]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1118502417}[消息添加列节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611580834}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_265063804}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[MOR message processing failure: Parameter number *parameter-number* smaller than index number *index-number*.]{lang="EN-US"}]{#struct_0_73523_x1515_611384226}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_611449762}[消息中取得的参数个数小于索引个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[parameter-number]{lang="EN-US"}*]{#struct_0_73523_x1515_x122070087}*[：]{lang="EN-US" style="font-family:宋体"}*[参数个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[index-number]{lang="EN-US"}*]{#struct_0_73523_x1515_611777442}*[：]{lang="EN-US" style="font-family:
  宋体"}*[索引个数]{lang="EN-US" style="font-family:宋体"}

[[Failed to get value from MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611842978}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_770316129}[消息中取值失败]{style="font-family:宋体"}

[[*[error-code]{lang="EN-US"}*]{.ItemListinTableCharChar}]{#struct_0_73523_x1515_611646370}[*[：]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[[错误码]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Failed to get *node-name*\'s MOR from MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_938576203}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_611711906}[消息中取节点的]{style="font-family:宋体"}[mor]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[*[node-name]{lang="EN-US"}*]{.ItemListinTableCharChar}]{#struct_0_73523_x1515_612039586}[*[：]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[[节点名]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Failed to get *node-name*\'s value from MOR message (error code: *err-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_2108733421}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_612105122}[消息中取节点值失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611515299}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_1118502416}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to check validity of *node-name*\'s value from MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611580835}

[[解析]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_611384227}[消息时，数据有效性检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_43581297}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_611449763}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to convert *node-name*\'s data type from MOR message (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611777443}

[[转换]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_x607602426}[消息中的数据类型失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_611842979}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_611646371}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Failed to get *node-name*\'s OID from MOR message]{lang="EN-US"}]{#struct_0_73523_x1515_938576204}

[[从]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_611711907}[消息中取节点的]{style="font-family:宋体"}[OID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_612039587}[：节点名]{style="font-family:宋体"}

[[Failed to allocate memory]{lang="EN-US"}]{#struct_0_73523_x1515_2108733420}

[[内存分配失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_612105123}

[[Create MOR message for leaf node]{lang="EN-US"}]{#struct_0_73523_x1515_611515296}

[[为叶子节点创建]{style="font-family:宋体"}[MOR]{lang="EN-US"}]{#struct_0_73523_x1515_1118502411}[消息]{style="font-family:宋体"}

[[Get instance *instance*.0 in batches]{lang="EN-US"}]{#struct_0_73523_x1515_611580832}

[[批量取节点实例]{style="font-family:宋体"}[.0]{lang="EN-US"}]{#struct_0_73523_x1515_611384224}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_43581294}[：实例]{style="font-family:宋体"}

[[Set instance *instance*.0 in batches]{lang="EN-US"}]{#struct_0_73523_x1515_611449760}

[[批量设置节点实例]{style="font-family:宋体"}[.0]{lang="EN-US"}]{#struct_0_73523_x1515_611777440}

[*[instance]{lang="EN-US"}*]{#struct_0_73523_x1515_611842976}[：实例]{style="font-family:宋体"}

[[Getting ASN variable failure: Unknown ASN data type *data-type*. ]{lang="EN-US"}]{#struct_0_73523_x1515_770316127}

[[从]{style="font-family:宋体"}[ASN]{lang="EN-US"}]{#struct_0_73523_x1515_611646368}[变量取值时]{style="font-family:宋体"}[ASN]{lang="EN-US"}[数据类型未知]{style="font-family:宋体"}

[*[data-typ]{lang="EN-US"}*[e]{lang="EN-US"}]{#struct_0_73523_x1515_611711904}[：数据类型]{style="font-family:宋体"}

[[Variable-binding value]{lang="EN-US"}]{#struct_0_73523_x1515_x241887360}[ converting failure: Unknown convert type *convert-type*. ]{lang="EN-US"}

[[转换变量绑定值时转换类型未知]{style="font-family:宋体"}]{#struct_0_73523_x1515_612039584}

[*[convert-type]{lang="EN-US"}*]{#struct_0_73523_x1515_612105120}[：转换类型]{style="font-family:宋体"}

[[Failed to complexly convert ASN value (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_611515297}

[[执行]{style="font-family:宋体"}[ASN]{lang="EN-US"}]{#struct_0_73523_x1515_1118502410}[值复杂转换失败]{style="font-family:宋体"}

[*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_611580833}[：错误码]{style="font-family:宋体"}

[[Complex ASN value]{lang="EN-US"}]{#struct_0_73523_x1515_611384225}[ converting failure: Invalid node *node-name*. ]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[ASN]{lang="EN-US"}]{#struct_0_73523_x1515_611449761}[值复杂转换时节点无效]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x122070088}[：节点名]{style="font-family:宋体"}

[[Complex ASN value converting failure: Unknown relation (*relation*) between registered node and index. ]{lang="EN-US"}]{#struct_0_73523_x1515_611777441}

[[执行]{style="font-family:宋体"}[ASN]{lang="EN-US"}]{#struct_0_73523_x1515_611842977}[值复杂转换时注册节点与索引的关系未知]{style="font-family:宋体"}

[*[relation]{lang="EN-US"}*]{#struct_0_73523_x1515_611646369}[：关系值]{style="font-family:宋体"}

[[Failed to check community *community* \'s acl *acl-number*]{lang="EN-US"}]{#struct_0_73523_x1515_x1400075948}

[[检查团体名]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_73523_x1515_611711905}[（]{style="font-family:宋体"}[Access Control List]{lang="EN-US"}[，访问控制列表）失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[community]{lang="EN-US"}*]{#struct_0_73523_x1515_612039585}[：团体名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a*cl-number*]{lang="EN-US"}]{#struct_0_73523_x1515_612105121}[：访问控制列表编号]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to check user *user-name*\'s acl *acl-number*]{lang="EN-US"}]{#struct_0_73523_x1515_x1451259145}

[[检查用户]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_73523_x1515_x2117368055}[失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[user-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117302519}[：用户名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[acl-number]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117499127}[：访问控制列表编号]{lang="EN-US" style="font-family:宋体"}

[[Failed to check group\'s acl *acl-number*]{lang="EN-US"}]{#struct_0_73523_x1515_x2117433591}

[[检查组]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_73523_x1515_271925634}[失败]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117105911}[：访问控制列表编号]{style="font-family:宋体"}

[[Failed to check context name]{lang="EN-US"}]{#struct_0_73523_x1515_x2117040375}

[[上下文名字检查失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117236983}

[[Failed to read SNMP socket asynchronous events]{lang="EN-US"}]{#struct_0_73523_x1515_x2117171447}

[[读]{style="font-family:宋体"}[SNMP socket]{lang="EN-US"}]{#struct_0_73523_x1515_788047307}[异步事件失败]{style="font-family:宋体"}

[[Failed to create socket ]{lang="EN-US"}]{#struct_0_73523_x1515_x2116843767}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_73523_x1515_x2116778231}[失败]{style="font-family:宋体"}

[[Community name is null.]{lang="EN-US"}]{#struct_0_73523_x1515_x2117368054}

[[团体名为空]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117302518}

[[Invalid community name *community-name*]{lang="EN-US"}]{#struct_0_73523_x1515_x39629786}

[[团体名无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117499126}

[*[community-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117433590}[：团体名]{style="font-family:宋体"}

[[Failed to check community name *community-name*\'s access right (PDU type: *pdu-type*, error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2117105910}

[[团体名访问权限检查失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117040374}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[community-name]{lang="EN-US"}]{#struct_0_73523_x1515_x2117236982}[：团体名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pdu-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x2043294477}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117171446}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误码]{lang="EN-US" style="font-family:宋体"}

[[Invalid variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_x2116843766}

[[变量绑定列表无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2116778230}

[[PDU type *PDU-type* not consistent with PDU version *PDU-version*]{lang="EN-US"}]{#struct_0_73523_x1515_x2117368057}

[[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x2117302521}[类型和]{style="font-family:宋体"}[PDU]{lang="EN-US"}[版本不兼容]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PDU-type]{lang="EN-US"}]{#struct_0_73523_x1515_x2117499129}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[PDU-version]{lang="EN-US"}*]{#struct_0_73523_x1515_x157356932}*[：]{lang="EN-US" style="font-family:宋体"}*[PDU]{lang="EN-US"}[版本]{lang="EN-US" style="font-family:宋体"}

[[PDU type is *PDU-type* and PDU version is *PDU-version*.]{lang="EN-US"}]{#struct_0_73523_x1515_x2117433593}

[[显示]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x2117105913}[类型和]{style="font-family:宋体"}[PDU]{lang="EN-US"}[版本]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PDU-type]{lang="EN-US"}]{#struct_0_73523_x1515_x2117040377}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[PDU-version]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117236985}*[：]{lang="EN-US" style="font-family:宋体"}*[PDU]{lang="EN-US"}[版本]{lang="EN-US" style="font-family:宋体"}

[[No such PDU type (*PDU-type*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2117171449}

[[无此]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x2116843769}[类型]{style="font-family:宋体"}

[*[PDU-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x2116778233}[：]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Get-next request processing failure: Invalid request.]{lang="EN-US"}]{#struct_0_73523_x1515_x2117368056}

[ ]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x146115863}[请求时请求无效]{style="font-family:宋体"}

[[Failed to append necessary OID for *node-name* while processing request for get-next (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2117302520}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x2117499128}[请求时为节点添加]{style="font-family:宋体"}[OID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117433592}[：节点名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117105912}[：错误码]{lang="EN-US" style="font-family:宋体"}

[[Get *node-name*\'s next instance]{lang="EN-US"}]{#struct_0_73523_x1515_x2117040376}

[[取当前节点的下一个实例]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117236984}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117171448}[：节点名]{style="font-family:宋体"}

[[Get-next request processing failure: Finding *next-node* from ]{lang="EN-US"}]{#struct_0_73523_x1515_x2116843768}[*[cur-node ]{lang="EN-US"}*]{.ItemListinTableCharChar}[timed out (*time* ms).]{lang="EN-US"}

[ ]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x1202118011}[请求时从当前节点查找下一节点超时]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time]{lang="EN-US"}*]{#struct_0_73523_x1515_x2116778232}*[：]{lang="EN-US" style="font-family:宋体"}*[时间]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[cur-node]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117368059}*[：]{lang="EN-US" style="font-family:
  宋体"}*[当前节点名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[next-node]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117302523}*[：]{lang="EN-US" style="font-family:
  宋体"}*[下一个节点名]{lang="EN-US" style="font-family:宋体"}

[[Get-next request processing failure: The table that ]{lang="EN-US"}]{#struct_0_73523_x1515_x2117499131}[contains ]{lang="EN-US"}[*[node-name]{lang="EN-US"}*]{.ItemListinTableCharChar}[ might be empty.]{lang="EN-US"}

[ ]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x2117433595}[请求时包含]{style="font-family:宋体"}[*[node-name]{lang="EN-US"}*]{.ItemListinTableCharChar}[*[节点的]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[表可能为空]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117105915}[：节点名]{style="font-family:宋体"}

[[Failed to pass checking*node-name*\'s access permission while processing request for get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x2117040379}

[[处理]{style="font-family:宋体"}[get-next]{lang="EN-US"}]{#struct_0_73523_x1515_x2117236987}[请求时访问权限检查失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117171451}[：节点名]{style="font-family:宋体"}

[[Process request]{lang="EN-US"}]{#struct_0_73523_x1515_x2116843771}

[[处理请求]{style="font-family:宋体"}]{#struct_0_73523_x1515_1882930168}

[[Invalid request]{lang="EN-US"}]{#struct_0_73523_x1515_x2116778235}

[[请求无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117368058}

[[Request processing failure: Invalid message entry.]{lang="EN-US"}]{#struct_0_73523_x1515_x2117302522}

[ ]{lang="EN-US"}

[[处理请求时消息表项无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_x2117499130}

[[Failed to check \'.0\' at the end of leaf node while processing request for get/set (error status: *error-status*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2117433594}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x2117105914}[请求时叶子节点尾部]{style="font-family:宋体"}['.0']{lang="EN-US"}[字符检查失败]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x2117040378}[：错误状态]{style="font-family:宋体"}

[[Get/set request processing failure (error status: *error-status*): No index for column node.]{lang="EN-US"}]{#struct_0_73523_x1515_x2117236986}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x2117171450}[请求时列节点无索引]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x2116843770}[：错误状态]{style="font-family:宋体"}

[[Failed to append necessary OID while processing request for get/set (error status: *error-status*)]{lang="EN-US"}]{#struct_0_73523_x1515_x2116778234}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x195053754}[请求时为节点添加]{style="font-family:宋体"}[OID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x194988218}[：错误状态]{style="font-family:宋体"}

[[Get/set request processing failure (error status: *error-status*): Incomplete index.]{lang="EN-US"}]{#struct_0_73523_x1515_x195184826}

[ ]{lang="EN-US"}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x195119290}[请求时索引不完整]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x194791610}[：错误状态]{style="font-family:宋体"}

[[Failed to check validity of index while processing request for get/set (error status: *error-status*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194726074}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x194922682}[请求时索引的合法性检查失败]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x194857146}[：错误状态]{style="font-family:宋体"}

[[Failed to process request for get/set (error status: *error-status*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194529466}

[[处理]{style="font-family:宋体"}[get/set]{lang="EN-US"}]{#struct_0_73523_x1515_x194463930}[请求失败]{style="font-family:宋体"}

[*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x195053753}[：错误状态]{style="font-family:宋体"}

[[PDU type is *PDU-type*, PDU version is *PDU-version*, non-repeaters is *non-repeaters*, max-repetitions is *max-repetitions*.]{lang="EN-US"}]{#struct_0_73523_x1515_x194988217}

[[显示]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x195184825}[类型和]{style="font-family:宋体"}[get-bulk]{lang="EN-US"}[参数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x195119289}*[：]{lang="EN-US" style="font-family:
  宋体"}*[PDU]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-version]{lang="EN-US"}*]{#struct_0_73523_x1515_x194791609}*[：]{lang="EN-US" style="font-family:
  宋体"}*[PDU]{lang="EN-US"}[版本]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[non-repeaters]{lang="EN-US"}*]{#struct_0_73523_x1515_x194726073}*[：]{lang="EN-US" style="font-family:
  宋体"}*[get-bulk]{lang="EN-US"}[操作参数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-repetitions]{lang="EN-US"}*]{#struct_0_73523_x1515_x194922681}*[：]{lang="EN-US" style="font-family:宋体"}*[get-bulk]{lang="EN-US"}[操作参数]{lang="EN-US" style="font-family:宋体"}

[[PDU type is *PDU-type*, non-repeaters is 0, max-repetitions is 0.]{lang="EN-US"}]{#struct_0_73523_x1515_x194857145}

[[显示]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x194529465}[类型，参数]{style="font-family:宋体"}[N]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，参数]{style="font-family:宋体"}[M]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}

[*[PDU-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x194463929}[：]{style="font-family:宋体"}[PDU]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Request processing failure: Invalid message table.]{lang="EN-US"}]{#struct_0_73523_x1515_x195053756}

[[处理请求时消息表无效]{style="font-family:宋体"}]{#struct_0_73523_x1515_x194988220}

[[Request processing failure: Non leaf or column node (node name: *node-name*, node type: *node-type*).]{lang="EN-US"}]{#struct_0_73523_x1515_x195184828}

[[非叶子节点或列节点]{style="font-family:宋体"}]{#struct_0_73523_x1515_x195119292}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x194791612}*[：]{lang="EN-US" style="font-family:
  宋体"}*[节点名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-type]{lang="EN-US"}*]{#struct_0_73523_x1515_x194726076}*[：]{lang="EN-US" style="font-family:
  宋体"}*[节点类型]{lang="EN-US" style="font-family:宋体"}

[[Request processing failure: No node can pass VACM chek.]{lang="EN-US"}]{#struct_0_73523_x1515_x194922684}

[[处理请求时无节点可通过]{style="font-family:宋体"}[VACM]{lang="EN-US"}]{#struct_0_73523_x1515_x194529468}[检查]{style="font-family:宋体"}

[[Request processing failure: No index memory space.]{lang="EN-US"}]{#struct_0_73523_x1515_x194463932}

[[处理请求时无索引的存储空间]{style="font-family:宋体"}]{#struct_0_73523_x1515_x195053755}

[[Failed to check VACM (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194988219}

[[VACM]{lang="EN-US"}]{#struct_0_73523_x1515_x195184827}[检查失败]{style="font-family:宋体"}

[*[error-code]{lang="EN-US"}*]{#struct_0_73523_x1515_x195119291}[：错误码]{style="font-family:宋体"}

[[Processing error (error status: *error-status*, error index: *error-index*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194791611}

[[错误处理]{style="font-family:宋体"}]{#struct_0_73523_x1515_x194726075}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x194922683}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_x194857147}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Read request]{lang="EN-US"}]{#struct_0_73523_x1515_x194529467}

[[读请求]{style="font-family:宋体"}]{#struct_0_73523_x1515_x195053758}

[[Request reading failure: Invalid PDU version (*PDU-version*).]{lang="EN-US"}]{#struct_0_73523_x1515_x194988222}

[[读请求时]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_x195184830}[版本无效]{style="font-family:宋体"}

[[*[PDU-version]{lang="EN-US"}*]{.ItemListinTableCharChar}]{#struct_0_73523_x1515_x195119294}[*[：]{lang="EN-US" style="font-family:宋体"}*[PDU]{lang="EN-US"}]{.ItemListinTableCharChar}[[版本]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Failed to add new entry to global message table while reading request]{lang="EN-US"}]{#struct_0_73523_x1515_x194791614}

[[读请求时在全局消息列表中增加一行失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x194726078}

[[Failed to decode SNMP request while reading request (error code: *error-code*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194922686}

[[读请求时解码]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x194857150}[请求报文失败]{style="font-family:宋体"}

[[*[error-code]{lang="EN-US"}*]{.ItemListinTableCharChar}]{#struct_0_73523_x1515_x194529470}[*[：]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[[错误码]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Make request]{lang="EN-US"}]{#struct_0_73523_x1515_x195053757}

[[构造请求]{style="font-family:宋体"}]{#struct_0_73523_x1515_x194988221}

[[Failed to update request (node name: *node-name*)]{lang="EN-US"}]{#struct_0_73523_x1515_x195184829}

[[更新请求失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x195119293}

[[*[node-name]{lang="EN-US"}*]{.ItemListinTableCharChar}]{#struct_0_73523_x1515_x194791613}[*[：]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[[节点名]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Send response to NMS (error status: *error-status*, error index: *error-index*)]{lang="EN-US"}]{#struct_0_73523_x1515_x194726077}

[[向网管发送响应报文]{style="font-family:宋体"}]{#struct_0_73523_x1515_x194922685}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_x194529469}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_x194463933}[*[：]{lang="EN-US" style="font-family:宋体"}*]{.ItemListinTableCharChar}[[错误索引]{lang="EN-US" style="font-family:宋体"}]{.ItemListinTableCharChar}

[[Response sending failure: PDU size (*PDU-size*) greater than max PDU size (*max-PDU-size*).]{lang="EN-US"}]{#struct_0_73523_x1515_1371030187}

[[发送响应时]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1371095723}[超大]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1370899115}[：当前]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[的大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1370964651}[：系统]{lang="EN-US" style="font-family:
  宋体"}[PDU]{lang="EN-US"}[的最大值]{lang="EN-US" style="font-family:
  宋体"}

[[Response sending failure: PDU size (*PDU-size*) greater than max PDU size (*max-PDU-size*) or SNMPv3 max PDU size (*v3- max-PDU-size)*.]{lang="EN-US"}]{#struct_0_73523_x1515_1371292331}

[[发送响应时]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1371161259}[超大]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1371226795}*[：]{lang="EN-US" style="font-family:
  宋体"}*[当前]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[的大小]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[max-PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1371554475}*[：]{lang="EN-US" style="font-family:
  宋体"}*[系统]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[的最大值]{lang="EN-US" style="font-family:宋体"}

[[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{.ItemListinTableCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCharCha1}*[v3- max-PDU-size]{lang="EN-US"}*]{#struct_0_73523_x1515_1371620011}*[：]{lang="EN-US" style="font-family:宋体"}*[SNMPv3]{lang="EN-US"}[版本]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[最大值]{lang="EN-US" style="font-family:宋体"}

[[Failed to allocate memory while sending response]{lang="EN-US"}]{#struct_0_73523_x1515_1371030188}

[[发送响应时申请空间失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1370899116}

[[Failed to execute set operation in reserve 1 (error status: *error-status*, error index: *error-index*)]{lang="EN-US"}]{#struct_0_73523_x1515_1370964652}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371292332}[原子操作]{style="font-family:宋体"}[reserve 1]{lang="EN-US"}[失败（]{style="font-family:宋体"}[set]{lang="EN-US"}[操作细分为多个处理步骤，每个步骤会对应一个原子操作）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371357868}[：错误状态]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1371226796}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Failed to execute set operation in reserve 2 (error status: ]{lang="EN-US"}]{#struct_0_73523_x1515_1371554476}[*[err]{lang="EN-US"}*]{.ItemListinTableCharChar}*[or-s]{lang="EN-US"}*[*[tatus]{lang="EN-US"}*]{.ItemListinTableCharChar}[, error index: *error-index*)]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371620012}[原子操作]{style="font-family:宋体"}[reserve 2]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371030185}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1371095721}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Failed to execute set operation in action (error status: ]{lang="EN-US"}]{#struct_0_73523_x1515_1370964649}[*[err]{lang="EN-US"}*]{.ItemListinTableCharChar}*[or-s]{lang="EN-US"}*[*[tatus]{lang="EN-US"}*]{.ItemListinTableCharChar}[, error index: *error-index*)]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371292329}[原子操作]{style="font-family:宋体"}[action]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371357865}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1371161257}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Failed to execute set operation in commit (error status: ]{lang="EN-US"}]{#struct_0_73523_x1515_1371554473}[*[err]{lang="EN-US"}*]{.ItemListinTableCharChar}*[or-s]{lang="EN-US"}*[*[tatus]{lang="EN-US"}*]{.ItemListinTableCharChar}[, error index: *error-index*)]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371620009}[原子操作]{style="font-family:宋体"}[commit]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371030186}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1371095722}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Failed to execute set operation in undo (error status: ]{lang="EN-US"}]{#struct_0_73523_x1515_1370964650}[*[err]{lang="EN-US"}*]{.ItemListinTableCharChar}*[or-s]{lang="EN-US"}*[*[tatus]{lang="EN-US"}*]{.ItemListinTableCharChar}[, error index: *error-index*)]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371292330}[原子操作]{style="font-family:宋体"}[undo]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371357866}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1371161258}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Failed to execute set operation in free (error status: ]{lang="EN-US"}]{#struct_0_73523_x1515_1371554474}[*[err]{lang="EN-US"}*]{.ItemListinTableCharChar}*[or-s]{lang="EN-US"}*[*[tatus]{lang="EN-US"}*]{.ItemListinTableCharChar}[, error index: *error-index*)]{lang="EN-US"}

[[执行]{style="font-family:宋体"}[set]{lang="EN-US"}]{#struct_0_73523_x1515_1371620010}[原子操作]{style="font-family:宋体"}[free]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-status]{lang="EN-US"}*]{#struct_0_73523_x1515_1371030183}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[error-index]{lang="EN-US"}*]{#struct_0_73523_x1515_1370899111}*[：]{lang="EN-US" style="font-family:
  宋体"}*[错误索引]{lang="EN-US" style="font-family:宋体"}

[[Send report message to NMS]{lang="EN-US"}]{#struct_0_73523_x1515_1370964647}

[[向网管发送报文信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_1371292327}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x472506755}

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_1043250695}[在一台启动了]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[功能并配置相应读写团体名的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[处理请求报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}[级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试开关，使用网管软件对设备上的]{style="font-family:宋体"}[sysUpTime]{lang="EN-US"}[对象进行]{style="font-family:宋体"}[get]{lang="EN-US"}[操作。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_1371161255}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp agent process stack info]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Read request]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   PDU type is 160 and PDU version is 1.]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Make request]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Process request]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Get instance sysUpTime.0]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Create MOR message for get-request and parse MOR message for response]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Create MOR message]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Create MOR message for leaf node]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Get instance sysUpTime.0 in batches]{lang="EN-US"}

[\*Jul 27 09:42:13:578 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Parse MOR message and fill variable-bindings]{lang="EN-US"}

[\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Get value from MOR message (MOR type: 3)]{lang="EN-US"}

[\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Convert data type 43 from MOR message]{lang="EN-US"}

[\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Fill variable-bindings]{lang="EN-US"}

[\*Jul 27 09:42:13:594 2007 Sysname SNMP/7/STACK_INFO:]{lang="EN-US"}

[   Send response to NMS (error status: 0, error index: 0)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_x1998864302}*[设备处理]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}[并生成响应消息过程的]{style="font-family:宋体"}[info]{lang="EN-US"}[级调试信息]{style="font-family:宋体"}*

::: {#196157614 .myid}
[]{#_Toc404796823}[]{#struct_0_73523_x1515_1443335207}[]{#_Toc263690037}[]{#_Toc206560112}

**SNMP \-- SNMP调试命令 \-- debugging snmp trap packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x329521624}

[**[debugging snmp trap packet]{lang="EN-US"}**]{#struct_0_73523_x1515_x947882542}

[**[undo debugging snmp trap]{lang="EN-US"}**[ **packet**]{lang="EN-US"}]{#struct_0_73523_x1515_808921240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_73523_x1515_1371226791}

[[SNMP ]{lang="EN-US"}]{#struct_0_73523_x1515_1106178274}[告警调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73523_x1515_775735462}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73523_x1515_1951611071}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1463373779}

[[network-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x1880858794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73523_x1515_1838177415}

[[【描述】]{style="font-family:黑体"}]{#struct_0_73523_x1515_2006955820}

[**[debugging snmp trap packet]{lang="EN-US"}**]{#struct_0_73523_x1515_x522625755}[命令用来打开告警报文的调试开关。]{style="font-family:
宋体"}**[undo debugging snmp trap packet]{lang="EN-US"}**[命令用来关闭告警报文的调试开关。缺省情况下，]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging snmp trap packet]{lang="EN-US"}]{#struct_0_73523_x1515_1371554471}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1188400271}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_1906181835}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_1760729189}

[[TRAP_PACKET]{lang="EN-US"}]{#struct_0_73523_x1515_x1617812683}

[[告警报文调试信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_x438085790}

[*[trap-name]{lang="EN-US"}*[ *version* send to: *address*]{lang="EN-US"}]{#struct_0_73523_x1515_2000657055}

[[系统发送]{style="font-family:宋体"}[trap-name ]{lang="EN-US"}]{#struct_0_73523_x1515_1371620007}[告警到]{style="font-family:宋体"}[address]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_338375877}[：告警报文的名称]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}*[version]{lang="FR"}*]{#struct_0_73523_x1515_398838334}[：]{lang="EN-US" style="font-family:宋体"}[报警版本]{lang="EN-US" style="font-family:宋体"}[（]{lang="EN-US" style="font-family:宋体"}[取值为]{lang="EN-US" style="font-family:
  宋体"}[trap\<v1\>]{lang="FR"}[、]{lang="EN-US" style="font-family:宋体"}[trap\<v2\>]{lang="FR"}[和]{lang="EN-US" style="font-family:宋体"}[inform]{lang="FR"}[三种）]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[address]{lang="EN-US"}*]{#struct_0_73523_x1515_x1351222800}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[Request ID: *request-id*]{lang="EN-US"}]{#struct_0_73523_x1515_1752447466}

[[告警报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1371030184}[中的]{style="font-family:宋体"}[request-id]{lang="EN-US"}[字段，]{style="font-family:宋体"}*[request-id]{lang="EN-US"}*[取值]{style="font-family:宋体"}[恒为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Error status: *error-status*]{lang="EN-US"}]{#struct_0_73523_x1515_x2006567681}

[[告警报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_1629108786}[中的]{style="font-family:宋体"}[error-status]{lang="EN-US"}[字段，]{style="font-family:宋体"}*[error-status]{lang="EN-US"}*[取值恒为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Error index: *error-index*]{lang="EN-US"}]{#struct_0_73523_x1515_x1435445104}

[[告警报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}]{#struct_0_73523_x1515_638372233}[中的]{style="font-family:宋体"}[error-index]{lang="EN-US"}[字段，]{style="font-family:宋体"}*[error-index]{lang="EN-US"}*[取值恒为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[UDP port: *port-number*]{lang="EN-US"}]{#struct_0_73523_x1515_x1183223887}

[[目的主机接收告警信息的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_73523_x1515_1371095720}[端口号]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_73523_x1515_1492161242}[：]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Trap successfully sent.]{lang="EN-US"}]{#struct_0_73523_x1515_952951799}

[[告警发送成功]{style="font-family:宋体"}]{#struct_0_73523_x1515_1613880512}

[[VBLIST]{lang="EN-US"}]{#struct_0_73523_x1515_1370899112}

[[告警报文中变量绑定对列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1209132405}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1955450014}

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_x986461553}[在一台使能了]{style="font-family:宋体"}[SNMP trap]{lang="EN-US"}[发送功能的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP ]{lang="EN-US"}[告警报文调试开关。在系统视图下依次执行]{style="font-family:宋体"}**[undo snmp-agent]{lang="EN-US"}**[和]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[两条命令，设备发送]{style="font-family:宋体"}[warmStart]{lang="EN-US"}[告警。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_1370964648}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp trap packet]{lang="SV"}

[\[Sysname\] undo snmp-agent]{lang="SV"}

[\[Sysname\] snmp-agent]{lang="SV"}

[\[Sysname\]]{lang="SV"}

[\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/TRAP_PACKET:]{lang="SV"}

[   warmStart trap\<v2\> send to: 10.165.81.75]{lang="SV"}

[   Request ID: 0]{lang="SV"}

[   Error status: 0]{lang="SV"}

[   Error index: 0]{lang="SV"}

[   UDP port: 162]{lang="SV"}

[   ]{lang="SV"}[Trap successfully sent.]{lang="EN-US"}

[\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/VBLIST:]{lang="SV"}

[   sysUpTime.0: 5936387]{lang="SV"}

[\*Jul 27 10:10:35:297 2007 Sysname SNMP/7/VBLIST:]{lang="SV"}

[   snmpTrapOID.0: 1.3.6.1.6.3.1.1.5.2]{lang="SV"}

[*[// ]{lang="EN-US"}*]{#struct_0_73523_x1515_741410384}*[设备向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.165.81.75]{lang="EN-US"}[的主机发送]{style="font-family:宋体"}[v2]{lang="EN-US"}[版的]{style="font-family:宋体"}[trap]{lang="EN-US"}[告警报文，告警节点名为]{style="font-family:宋体"}[warmStart]{lang="EN-US"}[，报文]{style="font-family:宋体"}[PDU]{lang="EN-US"}[中的请求]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[，错误状态为]{style="font-family:宋体"}[0]{lang="EN-US"}[，错误索引为]{style="font-family:宋体"}[0]{lang="EN-US"}[，目的主机的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[162]{lang="EN-US"}[，发送成功，绑定变量]{style="font-family:宋体"}[sysUpTime.0]{lang="EN-US"}[和]{style="font-family:宋体"}[snmpTrapOID.0]{lang="EN-US"}[的值分别是]{style="font-family:宋体"}[5936387]{lang="EN-US"}[和]{style="font-family:宋体"}[1.3.6.1.6.3.1.1.5.2]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#239664673 .myid}
[]{#_Toc404796824}[]{#struct_0_73523_x1515_x120615509}[]{#_Toc263690038}[]{#_Toc206560113}

**SNMP \-- SNMP调试命令 \-- debugging snmp trap process**

------------------------------------------------------------------------

[**[debugging snmp trap process]{lang="EN-US"}**]{#struct_0_73523_x1515_932750281}[命令用来打开告警处理的调试信息开关。]{style="font-family:
宋体"}

[**[undo debugging snmp trap process]{lang="EN-US"}**]{#struct_0_73523_x1515_x1198900580}[命令用来关闭告警处理的调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1218336851}

[**[debugging snmp trap]{lang="EN-US"}**[ **process** \[ **error** \| **info** \| **warning** \]]{lang="EN-US"}]{#struct_0_73523_x1515_120873249}

[**[undo debugging snmp trap]{lang="EN-US"}**[ **process** \[ **error** \| **info** \| **warning** \]]{lang="EN-US"}]{#struct_0_73523_x1515_1371292328}

[[【视图】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x472572291}

[[用户视图]{style="font-family:宋体"}]{#struct_0_73523_x1515_1441328031}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x259725100}

[[network-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x857298011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_73523_x1515_x1638361410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_73523_x1515_1347466551}

[**[error]{lang="EN-US"}**]{#struct_0_73523_x1515_2127333291}[：表示调试信息等级为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[error]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的错误信息。]{style="font-family:宋体"}

[**[info]{lang="EN-US"}**]{#struct_0_73523_x1515_x237927276}[：表示调试信息等级为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的提示信息。]{style="font-family:宋体"}

[**[warning]{lang="EN-US"}**]{#struct_0_73523_x1515_1371357864}[：表示调试信息等级为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息开关，输出级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}[的调试信息。该类调试信息指的是]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[协议栈或系统运行时的重要信息。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x424248273}

[**[debugging snmp trap process]{lang="EN-US"}**]{#struct_0_73523_x1515_x595352185}[命令用来打开告警处理的调试信息开关。]{style="font-family:
宋体"}**[undo debugging snmp trap process]{lang="EN-US"}**[命令用来关闭告警处理的调试信息开关。缺省情况下，]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-8 ]{lang="EN-US"}[debugging snmp trap process]{lang="EN-US"}]{#struct_0_73523_x1515_638074021}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1158652559}[[字段]{style="font-family:黑体"}]{#struct_0_73523_x1515_1279416549}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1958154207}

[[TRAP_INFO]{lang="EN-US"}]{#struct_0_73523_x1515_46290585}

[[告警处理时级别为]{style="font-family:宋体"}[info]{lang="EN-US"}]{#struct_0_73523_x1515_1371161256}[的调试信息]{style="font-family:宋体"}

[[TRAP_WARNING]{lang="EN-US"}]{#struct_0_73523_x1515_x1999060910}

[[告警处理时级别为]{style="font-family:宋体"}[warning]{lang="EN-US"}]{#struct_0_73523_x1515_x237657382}[的调试信息]{style="font-family:宋体"}

[[TRAP_ERROR]{lang="EN-US"}]{#struct_0_73523_x1515_x407730932}

[[告警处理时级别为]{style="font-family:宋体"}[error]{lang="EN-US"}]{#struct_0_73523_x1515_x59379320}[的调试信息]{style="font-family:宋体"}

[[Failed to create trap socket]{lang="EN-US"}]{#struct_0_73523_x1515_1371226792}

[[创建告警]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_73523_x1515_1105981666}[失败]{style="font-family:宋体"}

[[Trap socket is closed.]{lang="EN-US"}]{#struct_0_73523_x1515_128096096}

[[告警]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1627097523}[被关闭]{style="font-family:宋体"}

[[No available remote configuration parameters for generating traps]{lang="EN-US"}]{#struct_0_73523_x1515_1253906313}

[[远端的参数配置无效，不能生成告警信息]{style="font-family:宋体"}]{#struct_0_73523_x1515_1371554472}

[[Trap message timed out]{lang="EN-US"}]{#struct_0_73523_x1515_1906116299}

[[告警消息超时]{style="font-family:宋体"}]{#struct_0_73523_x1515_2091191546}

[[Create trap IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1754933460}

[[创建发送告警的]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x898795862}

[[Failed to create trap IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1371620008}

[[创建发送告警的]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_339227845}[失败]{style="font-family:宋体"}

[[Failed to bind trap IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_2106108684}

[[绑定发送告警的]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1551612904}[失败]{style="font-family:宋体"}

[[Create trap IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357853168}

[[创建发送告警的]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1764085332}

[[Failed to create trap IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1238407893}

[[创建发送告警的]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x627394867}[失败]{style="font-family:宋体"}

[[Failed to bind trap IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357787632}

[[绑定发送告警的]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1631194574}[失败]{style="font-family:宋体"}

[[Close trap IPv4/IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x319470956}

[[关闭发送告警的]{style="font-family:宋体"}[IPv4/IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1780470432}

[[Send trap through IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357984240}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_589767836}[发送告警]{style="font-family:宋体"}

[[Failed to get source IP address while sending trap through IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1984322663}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1512010679}[发送告警时获取]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[源地址失败]{style="font-family:宋体"}

[[Trap sending through IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357918704}[ failure: Invalid VPN index.]{lang="EN-US"}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_72358866}[发送告警时]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引无效]{style="font-family:宋体"}

[[Failed to send trap through IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1372658538}

[[通过]{style="font-family:宋体"}[IPv4 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1046319082}[发送告警失败]{style="font-family:宋体"}

[[Send trap through IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357591024}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_884656203}[发送告警]{style="font-family:宋体"}

[[Trap sending through IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x983927835}[ failure: Invalid IPv6 interface index.]{lang="EN-US"}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_x1357525488}[发送告警时]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口索引无效]{style="font-family:宋体"}

[[Failed to send trap through IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1243518396}

[[通过]{style="font-family:宋体"}[IPv6 socket]{lang="EN-US"}]{#struct_0_73523_x1515_1727260692}[发送告警失败]{style="font-family:宋体"}

[[Send trap message to trap queue]{lang="EN-US"}]{#struct_0_73523_x1515_x1357722096}

[[发送告警消息至告警队列]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1394269234}

[[Failed to get the number of messages in trap queue]{lang="EN-US"}]{#struct_0_73523_x1515_x603008124}

[[取告警队列中消息个数失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1904569001}

[[Trap queue is full.]{lang="EN-US"}]{#struct_0_73523_x1515_x1357656560}

[[告警队列满]{style="font-family:宋体"}]{#struct_0_73523_x1515_751643000}

[[Failed to read trap queue]{lang="EN-US"}]{#struct_0_73523_x1515_1065609914}

[[读告警队列失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1357328880}

[[Failed to write trap event]{lang="EN-US"}]{#struct_0_73523_x1515_x1210500448}

[[写告警事件失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x664383175}

[[Failed to add trap message to trap queue]{lang="EN-US"}]{#struct_0_73523_x1515_x1357263344}

[[向告警队列添加告警消息失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_125126723}

[[Process trap message in trap queue at * time-hour:time-minute*:*time-second*]{lang="EN-US"}]{#struct_0_73523_x1515_x712313581}

[[在]{style="font-family:宋体"}[time-hour]{lang="EN-US"}]{#struct_0_73523_x1515_x1357853167}[：]{style="font-family:宋体"}[time-minute]{lang="EN-US"}[：]{style="font-family:宋体"}[time-second]{lang="EN-US"}[时间处理告警队列中的一个告警消息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_x1321028383}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_1574457531}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357787631}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to parse trap message]{lang="EN-US"}]{#struct_0_73523_x1515_2034479101}

[[解析告警消息失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_962804059}

[[Parse trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1357984239}

[[解析告警消息]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1783081767}

[[Wrong data type of 1st parameter in trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1357918703}

[[告警消息中的第一个参数数据类型错误]{style="font-family:宋体"}]{#struct_0_73523_x1515_1638442807}

[[Failed to parse data value of 1st parameter in trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x144441908}

[[解析告警消息中第一个参数的数值失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1357591023}

[[Failed to find trap node specified in trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1844227152}

[[查找告警消息中指定告警节点失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1499341838}

[[Node specified in trap message is not trap-type.]{lang="EN-US"}]{#struct_0_73523_x1515_x1357525487}

[[告警消息中指定的节点不是]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_73523_x1515_33664815}[类型]{style="font-family:宋体"}

[[Failed to get trap\'s index-lists]{lang="EN-US"}]{#struct_0_73523_x1515_x1357722095}

[[取告警绑定节点的索引列表失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1334614121}

[[Failed to build trap\'s variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_665862763}

[[构造告警变量绑定列表失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1357656559}

[[Failed to get trap\'s generic trap type]{lang="EN-US"}]{#struct_0_73523_x1515_x458276117}

[[取告警的]{style="font-family:宋体"}[generic]{lang="EN-US"}]{#struct_0_73523_x1515_162543172}[类型失败]{style="font-family:宋体"}

[[Get trap\'s index-lists]{lang="EN-US"}]{#struct_0_73523_x1515_x1357328879}

[[取告警绑定节点的索引列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_x57043}

[[Failed to search *trap-name\'s* binding node]{lang="EN-US"}]{#struct_0_73523_x1515_x1357263343}

[[查找告警绑定节点失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1440957218}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357853170}[：告警节点名]{style="font-family:宋体"}

[[Get index-list of *trap-name*\'s binding node *node-name*]{lang="EN-US"}]{#struct_0_73523_x1515_1407920508}

[[取告警绑定节点的索引列表]{style="font-family:宋体"}]{#struct_0_73523_x1515_1944265411}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357787634}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1500973308}[：绑定节点名]{lang="EN-US" style="font-family:宋体"}

[[Wrong number of parameters in *trap-name*\'s trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1357984242}

[[告警消息中参数个数错误]{style="font-family:宋体"}]{#struct_0_73523_x1515_1752567250}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1735592917}[：告警节点名]{style="font-family:宋体"}

[[The parameter type in *trap-name*\'s trap message doesn\'t match its binding node *node-name*\'s.]{lang="EN-US"}]{#struct_0_73523_x1515_x1357918706}

[[告警消息中参数类型与其绑定节点的参数类型不匹配]{style="font-family:宋体"}]{#struct_0_73523_x1515_1235158280}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357591026}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_2047455617}[：绑定节点名]{lang="EN-US" style="font-family:宋体"}

[[Failed to get *node-name*\'s value from *trap-name*\'s trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1357525490}

[[从告警消息中取绑定节点的实例值失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1599683220}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357722098}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1381668288}[：绑定节点名]{lang="EN-US" style="font-family:宋体"}

[[Failed to check *node-name*\'s value from *trap-name*\'s trap message]{lang="EN-US"}]{#struct_0_73523_x1515_x1357656562}

[[告警消息中绑定节点的实例值数据检查失败]{style="font-family:宋体"}]{#struct_0_73523_x1515_1914442414}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1174805354}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357328882}[：绑定变量节点名]{lang="EN-US" style="font-family:宋体"}

[[Build *trap-name*\'s variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_1921667434}

[[构造]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_73523_x1515_x1357263346}[的变量绑定列表失败]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1037672691}[：告警节点名]{style="font-family:宋体"}

[[Empty binding node for *trap-name*]{lang="EN-US"}]{#struct_0_73523_x1515_x1357853169}

[[告警绑定节点为空]{style="font-family:宋体"}]{#struct_0_73523_x1515_198001391}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357787633}[：告警节点名]{style="font-family:宋体"}

[[Wrong binding node *node-name* for *trap-name*]{lang="EN-US"}]{#struct_0_73523_x1515_x1097688781}

[[错误的告警绑定节点]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1357984241}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x2139115519}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357918705}[：绑定节点名]{lang="EN-US" style="font-family:宋体"}

[[Failed to copy *node-name*\'s value]{lang="EN-US"}]{#struct_0_73523_x1515_x1493725075}

[[拷贝]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357591025}[节点实例值失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x681427738}[：绑定节点名]{style="font-family:宋体"}

[[Failed to convert binding node *node-name*\'s index value to OID]{lang="EN-US"}]{#struct_0_73523_x1515_x1357525489}

[[转换绑定节点]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1485364959}[的索引值为]{style="font-family:宋体"}[OID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357722097}[：绑定节点名]{style="font-family:宋体"}

[[Prepare to generate and send trap *trap-name*]{lang="EN-US"}]{#struct_0_73523_x1515_171814707}

[[准备生成并发送告警]{style="font-family:宋体"}]{#struct_0_73523_x1515_x1357656561}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x814440941}[：告警节点名]{style="font-family:宋体"}

[[Failed to get *trap-name*\'s OID]{lang="EN-US"}]{#struct_0_73523_x1515_x1357328881}

[[取告警节点]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_73523_x1515_x1357263345}[失败]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1691210664}[：告警节点名]{style="font-family:宋体"}

[[Failed to build *trap-name*\'s v2 variable-bindings]{lang="EN-US"}]{#struct_0_73523_x1515_x1357853172}

[[构造]{style="font-family:宋体"}[trap]{lang="EN-US"}]{#struct_0_73523_x1515_x1724247374}[的绑定变量列表失败]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357787636}[：告警节点名]{style="font-family:宋体"}

[[Invalid snmpNotifyType]{lang="EN-US"}]{#struct_0_73523_x1515_x338173894}

[[无效的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_x1357984244}[告警类型]{style="font-family:宋体"}

[[No valid entries in snmpTargetAddrTable for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_x1379600632}

[[没有有效的]{style="font-family:宋体"}[snmpTargetAddrTable]{lang="EN-US"}]{#struct_0_73523_x1515_x1357918708}[配置表项发送告警]{style="font-family:宋体"}

[[Filter address *address* for sending *trap-name*]{lang="EN-US"}]{#struct_0_73523_x1515_x1357591028}

[[发送告警消息时过滤掉目的地址为]{style="font-family:宋体"}*[address]{lang="EN-US"}*]{#struct_0_73523_x1515_x1084712265}[的]{style="font-family:宋体"}[trap]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357525492}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[address]{lang="EN-US"}*]{#struct_0_73523_x1515_436883806}[：发送告警的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[No entry in snmpTargetParamsTable matches snmpTargetAddrParams *value*. ]{lang="EN-US"}]{#struct_0_73523_x1515_x1357722100}

[[在]{style="font-family:宋体"}[snmpTargetParamsTable]{lang="EN-US"}]{#struct_0_73523_x1515_1737439897}[表中没有与节点]{style="font-family:宋体"}[snmpTargetAddrParams]{lang="EN-US"}[的实例值匹配的表项]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357656564}[：]{style="font-family:宋体"}[snmpTargetAddrParams]{lang="EN-US"}[节点的一个实例值]{style="font-family:宋体"}

[[Wrong message processing model (*message-processing-model*) or unsupported SNMP version (*version*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1357328884}

[[错误的消息处理模型或不支持的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_73523_x1515_1115098380}[版本]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[message-processing-model]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357263348}[：消息处理模型值]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[version]{lang="EN-US"}*]{#struct_0_73523_x1515_x1488011385}[：]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本]{lang="EN-US" style="font-family:宋体"}

[[Failed to check trap *trap-name*\'s VACM (security model: *security-model*, security name: *security-name*, security level: *security-level*)]{lang="EN-US"}]{#struct_0_73523_x1515_x1357853171}

[*[Trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357787635}[告警的]{style="font-family:宋体"}[VACM]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_65110633}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[security-model]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357984243}[：安全模型值]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[security-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x976316105}[：安全名]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[security-level]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357918707}[：安全等级值]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to get *trap-name*\'s source IP address]{lang="EN-US"}]{#struct_0_73523_x1515_x1357591027}

[[获取]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_73523_x1515_481371676}[告警的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357525491}[：告警节点名]{style="font-family:宋体"}

[[Failed to create *trap-name* packet]{lang="EN-US"}]{#struct_0_73523_x1515_x1129200135}

[[创建]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_73523_x1515_x1357722099}[告警报文失败]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357656563}[：告警节点名]{style="font-family:宋体"}

[[Unknown destination IP type (*type*) for sending *trap-name*]{lang="EN-US"}]{#struct_0_73523_x1515_348358473}

[[发送的]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357328883}[告警报文目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型未知]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[type]{lang="EN-US"}*]{#struct_0_73523_x1515_x1357263347}[：目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_528411250}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[Trap-name successfully sent at *time-hour*:*time-minute*:*time-second*]{lang="EN-US"}]{#struct_0_73523_x1515_208230773}

[[Trap-name]{lang="EN-US"}]{#struct_0_73523_x1515_208296309}[告警于]{style="font-family:宋体"}[time-hour]{lang="EN-US"}[：]{style="font-family:宋体"}[time-minute]{lang="EN-US"}[：]{style="font-family:宋体"}[time-second]{lang="EN-US"}[时间成功发送]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x468454140}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-hour]{lang="EN-US"}*]{#struct_0_73523_x1515_208099701}[：小时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-minute]{lang="EN-US"}*]{#struct_0_73523_x1515_1587201912}[：分钟]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[time-second]{lang="EN-US"}*]{#struct_0_73523_x1515_208165237}[：秒]{lang="EN-US" style="font-family:
  宋体"}

[[Failed to create *trap-name* packet (PDU size: *pdu-size*)]{lang="EN-US"}]{#struct_0_73523_x1515_208492917}

[[创建]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x1341769372}[的告警报文失败]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_208558453}[：告警节点名]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[pdu-size]{lang="EN-US"}*]{#struct_0_73523_x1515_208361845}[：]{lang="EN-US" style="font-family:宋体"}[PDU]{lang="EN-US"}[大小]{lang="EN-US" style="font-family:宋体"}

[[Search entries in snmpTargetAddrTable to match snmpNotifyTag *value*]{lang="EN-US"}]{#struct_0_73523_x1515_208427381}

[[在]{style="font-family:宋体"}[snmpTargetAddrTable]{lang="EN-US"}]{#struct_0_73523_x1515_x1727859179}[表中寻找与节点]{style="font-family:宋体"}[snmpNotifyTag]{lang="EN-US"}[的实例值匹配的表项]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_73523_x1515_208755061}[：]{style="font-family:宋体"}[snmpNotifyTag]{lang="EN-US"}[节点的一个实例值]{style="font-family:宋体"}

[[Search entries in snmpTargetParamsTable to match snmpTargetAddrParams *value*]{lang="EN-US"}]{#struct_0_73523_x1515_208820597}

[[在]{style="font-family:宋体"}[ snmpTargetParamsTable]{lang="EN-US"}]{#struct_0_73523_x1515_x555372111}[表中寻找与节点]{style="font-family:宋体"}[snmpTargetAddrParams]{lang="EN-US"}[的实例值匹配的表项]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_73523_x1515_208230774}[：]{style="font-family:宋体"}[snmpTargetAddrParams]{lang="EN-US"}[节点的一个实例值]{style="font-family:宋体"}

[[Create *trap-name* packet]{lang="EN-US"}]{#struct_0_73523_x1515_208296310}

[[创建]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_1870198029}[的告警报文]{style="font-family:宋体"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_208099702}[：告警节点名]{style="font-family:宋体"}

[[Encode *SNMP-version* trap]{lang="EN-US"}]{#struct_0_73523_x1515_208165238}

[[编码告警报文]{style="font-family:宋体"}]{#struct_0_73523_x1515_208492918}

[*[SNMP-version]{lang="EN-US"}*]{#struct_0_73523_x1515_x1341769373}[：]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[版本（取值]{style="font-family:宋体"}[SNMPv1]{lang="EN-US"}[和]{style="font-family:宋体"}[SNMPv2c]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Get generic trap type]{lang="EN-US"}]{#struct_0_73523_x1515_208558454}

[[获取告警类型]{style="font-family:宋体"}]{#struct_0_73523_x1515_208361846}

[[Get enterprise OID]{lang="EN-US"}]{#struct_0_73523_x1515_x826948003}

[[获取企业]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_73523_x1515_208427382}

[[Failed to get sysObjectID while getting enterprise OID]{lang="EN-US"}]{#struct_0_73523_x1515_208755062}

[[获取企业]{style="font-family:宋体"}[OID]{lang="EN-US"}]{#struct_0_73523_x1515_208820598}[时，获取]{style="font-family:宋体"}[sysObjectID]{lang="EN-US"}[节点值失败]{style="font-family:宋体"}

[[Check trap *trap-name*\'s VACM]{lang="EN-US"}]{#struct_0_73523_x1515_x555372098}

[[检查]{style="font-family:宋体"}*[trap-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_73523_x1515_208230771}[告警的]{style="font-family:宋体"}[VACM]{lang="EN-US"}

[*[trap-name]{lang="EN-US"}*]{#struct_0_73523_x1515_208296307}[：告警节点名]{style="font-family:宋体"}

[[Failed to get binding node *node-name*\'s OID]{lang="EN-US"}]{#struct_0_73523_x1515_208099699}

[[获取绑定节点]{style="font-family:宋体"}*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x332377387}[的]{style="font-family:宋体"}[OID]{lang="EN-US"}[失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_208165235}[：绑定节点名]{style="font-family:宋体"}

[[Failed to check *node-name*\'s VACM]{lang="EN-US"}]{#struct_0_73523_x1515_208492915}

[*[Node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_208558451}[节点的]{style="font-family:宋体"}[VACM]{lang="EN-US"}[检查失败]{style="font-family:宋体"}

[*[node-name]{lang="EN-US"}*]{#struct_0_73523_x1515_x235455105}[：]{style="font-family:宋体"}[MIB]{lang="EN-US"}[节点名]{style="font-family:宋体"}

[[Get source IPv4 address for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_208361843}

[[获取发送告警的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_73523_x1515_208427379}[地址]{style="font-family:宋体"}

[[Get source IPv6 address for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_208755059}

[[获取发送告警的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_73523_x1515_483158795}[地址]{style="font-family:宋体"}

[[Failed to get source IPv4 address for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_208820595}

[[获取发送告警的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_73523_x1515_208230772}[地址失败]{style="font-family:宋体"}

[[Failed to get source IPv6 address for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_208296308}

[[获取发送告警的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_73523_x1515_208099700}[地址失败]{style="font-family:宋体"}

[[Unknown destination IP type (*type*) for sending trap]{lang="EN-US"}]{#struct_0_73523_x1515_1587201913}

[[发送告警时目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_73523_x1515_208165236}[类型未知]{style="font-family:宋体"}

[*[type]{lang="EN-US"}*]{#struct_0_73523_x1515_208492916}[：类型]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_73523_x1515_x1341769371}

[[\# ]{lang="EN-US"}]{#struct_0_73523_x1515_x890758651}[在一台使能了]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警发送功能的设备上打开信息中心调试开关和]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[告警子模块级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的]{style="font-family:宋体"}[调试开关。]{style="font-family:宋体"}[在系统视图下依次执行]{style="font-family:宋体"}**[undo snmp-agent]{lang="EN-US"}**[和]{style="font-family:宋体"}**[snmp-agent]{lang="EN-US"}**[两条命令，设备发送]{style="font-family:宋体"}[warmStart]{lang="EN-US"}[告警。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_73523_x1515_208361844}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> debugging snmp trap process info]{lang="SV"}

[\[Sysname\] undo snmp-agent]{lang="SV"}

[\[Sysname\] snmp-agent]{lang="SV"}

[\[Sysname\]]{lang="EN-US"}

[\*Jul 27 10:21:22:938 2007 Sysname SNMP/7/TRAP_INFO:]{lang="DA"}

[   S]{lang="DA"}[end trap message to trap queue]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Create trap IPv4 socket]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Create trap IPv6 socket]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Process trap message in trap queue at 10:21:22]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Parse trap message]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Get trap\'s index-lists]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Build warmStart\'s variable-bindings]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Get generic trap type]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Prepare to generate and send trap warmStart]{lang="EN-US"}

[\*Jul 27 10:21:22:984 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Search entries in snmpTargetAddrTable to match snmpNotifyTag TrapHost]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Search entries in snmpTargetParamsTable to match snmpTargetAddrParams traphost.u2.192.168.123.123]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Check trap warmStart\'s VACM]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Get source IPv4 address for sending trap]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Search entries in snmpTargetParamsTable to match snmpTargetAddrParams traphost.uu.10.165.81.75]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Check trap warmStart\'s VACM]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Get source IPv4 address for sending trap]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Create warmStart packet]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Get enterprise OID]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Encode SNMPv2c trap]{lang="EN-US"}

[\*Jul 27 10:21:23:00 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   Send trap through IPv4 socket]{lang="EN-US"}

[\*Jul 27 10:21:23:16 2007 Sysname SNMP/7/TRAP_INFO:]{lang="EN-US"}

[   warmStart successfully sent at 10:21:22]{lang="EN-US"}

[*[// SNMP]{lang="EN-US"}*]{#struct_0_73523_x1515_x826948001}*[告警子模块处理告警消息，发送]{style="font-family:宋体"}[warmStart]{lang="EN-US"}[告警报文，输出级别为]{style="font-family:宋体"}[info]{lang="EN-US"}[的调试信息。]{style="font-family:宋体"}*
