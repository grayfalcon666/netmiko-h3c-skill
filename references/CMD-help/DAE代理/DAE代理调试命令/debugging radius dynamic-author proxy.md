::: {#1644630841 .myid}
[]{#_Toc404793999}[]{#struct_0_x1104_x1396_756024038}[]{#_Toc212180723}

**DAE代理 \-- DAE代理调试命令 \-- debugging radius dynamic-author proxy**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_74136075}

[**[debugging radius dynamic-author proxy ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1104_x1396_x1740871369}

[**[undo debugging radius dynamic-author proxy ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x1104_x1396_503692785}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_145990972}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1104_x1396_1291998245}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_x333860174}

[[network-admin]{lang="EN-US"}]{#struct_0_x1104_x1396_x1158618348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1104_x1396_x1150623765}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_x1884961819}

[**[all]{lang="EN-US"}**]{#struct_0_x1104_x1396_2055934918}[：表示]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1104_x1396_x392084262}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1104_x1396_1623783339}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x1104_x1396_942313804}[：表示报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_289470117}

[**[debugging radius dynamic-author proxy]{lang="EN-US"}**]{#struct_0_x1104_x1396_x1852661223}[命令用来打开]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的调试信息开关。]{style="font-family:宋体"}**[undo debugging radius dynamic-author proxy]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x667128935}[代理的所有调试信息开关均处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging radius dynamic-author proxy error]{lang="EN-US"}]{#struct_0_x1104_x1396_x1394836503}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1398880508}[[字段]{style="font-family:黑体"}]{#struct_0_x1104_x1396_x528918211}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1104_x1396_45852307}

[[Failed to bind port *port-num*.]{lang="EN-US"}]{#struct_0_x1104_x1396_1719297812}

[[绑定端口]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*]{#struct_0_x1104_x1396_x2014938622}[失败]{style="font-family:宋体"}

[[Failed to get DAE client\'s key by IP *IP-addr*.]{lang="EN-US"}]{#struct_0_x1104_x1396_698984084}

[[通过]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1104_x1396_1708743409}[地址]{style="font-family:宋体"}*[IP-addr]{lang="EN-US"}*[获取]{style="font-family:宋体"}[DAE]{lang="EN-US"}[客户端的密钥失败]{style="font-family:宋体"}

[[Packet length is invalid.]{lang="EN-US"}]{#struct_0_x1104_x1396_1011330797}

[[报文长度非法]{style="font-family:宋体"}[.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1184627391}

[[Packet type is invalid.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1916728364}

[[报文类型非法]{style="font-family:宋体"}[.]{lang="EN-US"}]{#struct_0_x1104_x1396_1484014515}

[[Failed to authenticate packet.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852726759}

[[校验报文失败]{style="font-family:宋体"}]{#struct_0_x1104_x1396_x1140633350}

[[Failed to sent packet to DAE Client (IP *ip-addr*).]{lang="EN-US"}]{#struct_0_x1104_x1396_x698043110}

[[向]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1104_x1396_x1553414288}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[客户端发送报文失败]{style="font-family:宋体"}

[[Failed to get error code from packet.]{lang="EN-US"}]{#struct_0_x1104_x1396_x632442173}

[[从报文中获取错误码失败]{style="font-family:宋体"}]{#struct_0_x1104_x1396_x469054513}

[[The DAE packet code *code* is not support.]{lang="EN-US"}]{#struct_0_x1104_x1396_x263392565}

[[不支持的]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x913569249}[报文类型]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Failed to receive packet from socket (ID *socket-ID*).]{lang="EN-US"}]{#struct_0_x1104_x1396_x662764865}

[[从]{style="font-family:宋体"}[Socket]{lang="EN-US"}]{#struct_0_x1104_x1396_x743443500}[（]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[socket-ID]{lang="EN-US"}*[）接收报文失败]{style="font-family:宋体"}

[[Failed to get session for packet (ID *packet-ID*).]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852792295}

[[无法为报文（]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1104_x1396_x1585517682}[为]{style="font-family:宋体"}*[packet-ID]{lang="EN-US"}*[）找到会话上下文]{style="font-family:宋体"}

[[Failed to send DAE request to NAS (IP *ip-addr*).]{lang="EN-US"}]{#struct_0_x1104_x1396_2057555064}

[[向]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1104_x1396_1011274158}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[的]{style="font-family:宋体"}[NAS]{lang="EN-US"}[发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求失败]{style="font-family:宋体"}

[[Failed to get NAS.]{lang="EN-US"}]{#struct_0_x1104_x1396_1514985430}

[[找不到]{style="font-family:宋体"}[NAS]{lang="EN-US"}]{#struct_0_x1104_x1396_1136615887}[（]{style="font-family:宋体"}[BAS AC]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Failed to send DAE request to NAS.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1225142822}

[[向]{style="font-family:宋体"}[NAS]{lang="EN-US"}]{#struct_0_x1104_x1396_x1733123056}[（]{style="font-family:宋体"}[BAS AC]{lang="EN-US"}[）发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求报文失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging radius dynamic-author proxy event]{lang="EN-US"}]{#struct_0_x1104_x1396_x1211291837}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1403988589}[[字段]{style="font-family:黑体"}]{#struct_0_x1104_x1396_x1852857831}

[[描述]{style="font-family:黑体"}]{#struct_0_x1104_x1396_1507363416}

[[Reset statistics of DAE packets.]{lang="EN-US"}]{#struct_0_x1104_x1396_1360899952}

[[清空]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_1415324298}[报文统计信息]{style="font-family:宋体"}

[[Enable DAE proxy.]{lang="EN-US"}]{#struct_0_x1104_x1396_201775021}

[[开启]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852399079}[代理功能]{style="font-family:宋体"}

[[Disable DAE proxy.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1717607724}

[[关闭]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x11009786}[代理功能]{style="font-family:宋体"}

[[Got framed IP *ip-addr*.]{lang="EN-US"}]{#struct_0_x1104_x1396_1725646418}

[[获取到]{style="font-family:宋体"}[framed IP]{lang="EN-US"}]{#struct_0_x1104_x1396_x552449432}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*

[[DAE proxy received response with no request.]{lang="EN-US"}]{#struct_0_x1104_x1396_1132536520}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852464615}[代理收到没有请求的应答]{style="font-family:宋体"}

[[DAE proxy received retransmit request pkt.]{lang="EN-US"}]{#struct_0_x1104_x1396_x178170677}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x54984201}[代理收到重传请求报文]{style="font-family:宋体"}

[[DAE proxy cached DAE response from NAS (IP *ip-addr*).]{lang="EN-US"}]{#struct_0_x1104_x1396_x577230692}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x145554987}[代理缓存来自]{style="font-family:宋体"}[NAS]{lang="EN-US"}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[）的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[应答]{style="font-family:宋体"}

[[DAE proxy created tunnel \[DAE Client IP *ip-addr1*, Port *port-num*, Local IP *ip-addr2*\].]{lang="EN-US"}]{#struct_0_x1104_x1396_x1914159413}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_1696462918}[代理创建透传通道，]{style="font-family:宋体"}[DAE]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr1]{lang="EN-US"}*[，端口号为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*[，本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr2]{lang="EN-US"}*

[[DAE proxy deleted tunnel \[DAE Client IP *ip-addr1*, Port *port-num*, Local IP *ip-addr2*\].]{lang="EN-US"}]{#struct_0_x1104_x1396_x948146445}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_612128037}[代理删除透传通道，]{style="font-family:宋体"}[DAE]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr1]{lang="EN-US"}*[，端口号为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*[，本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr2]{lang="EN-US"}*

[[DAE proxy tunnel timed out.]{lang="EN-US"}]{#struct_0_x1104_x1396_2064651804}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852923366}[代理的透传通道超时（一个通道中有多个会话）]{style="font-family:宋体"}

[[DAE proxy session timed out.]{lang="EN-US"}]{#struct_0_x1104_x1396_276076549}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x2051699157}[代理的会话超时]{style="font-family:宋体"}

[[DAE proxy created session with id *session-id*.]{lang="EN-US"}]{#struct_0_x1104_x1396_x426553086}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x706715886}[代理创建]{style="font-family:宋体"}[session ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[session-id]{lang="EN-US"}*[的会话]{style="font-family:宋体"}

[[DAE proxy deleted session with id *session-id*.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1156171629}

[[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x355919221}[代理销毁]{style="font-family:宋体"}[session ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[session-id]{lang="EN-US"}*[的会话]{style="font-family:宋体"}

[[Start to connect WLAN.]{lang="EN-US"}]{#struct_0_x1104_x1396_x835837143}

[[开始与]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_x1104_x1396_x1852988902}[模块建立连接]{style="font-family:宋体"}

[[Stop connecting to WLAN.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1967298531}

[[停止与]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_x1104_x1396_x530669415}[模块建立连接]{style="font-family:宋体"}

[[Set NAS port as *port-num*.]{lang="EN-US"}]{#struct_0_x1104_x1396_1151341330}

[[设置]{style="font-family:宋体"}[NAS]{lang="EN-US"}]{#struct_0_x1104_x1396_369209500}[端口为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging radius dynamic-author proxy packet]{lang="EN-US"}]{#struct_0_x1104_x1396_x1564234245}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1402022191}[[字段]{style="font-family:宋体"}]{#struct_0_x1104_x1396_922193677}

[[描述]{style="font-family:宋体"}]{#struct_0_x1104_x1396_228026782}

[[Received DAE packet: SRC IP = ]{lang="EN-US"}*[ip-addr]{lang="EN-US"}*]{#struct_0_x1104_x1396_x74069890}[, Port = ]{lang="EN-US"}*[port-num]{lang="EN-US"}*[, Type = ]{lang="EN-US"}*[type]{lang="EN-US"}*

[[收到]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_x570575257}[报文：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[，端口号为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[[Sent DAE packet: DEST IP = ]{lang="EN-US"}*[ip-addr]{lang="EN-US"}*]{#struct_0_x1104_x1396_x1853054438}[, Port = ]{lang="EN-US"}*[port-num]{lang="EN-US"}*[, Type = ]{lang="EN-US"}*[type]{lang="EN-US"}*

[[发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}]{#struct_0_x1104_x1396_448701464}[报文：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[，端口号为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1104_x1396_193279191}

[]{#_Toc212180724}[[\# ]{lang="EN-US"}]{#struct_0_x1104_x1396_x871653344}[在]{style="font-family:宋体"}[Master AC]{lang="EN-US"}[上开启]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理功能，并打开]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的错误调试信息开关。若]{style="font-family:宋体"}[Master AC]{lang="EN-US"}[收到来自]{style="font-family:宋体"}[DAE Client]{lang="EN-US"}[的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求报文，当校验]{style="font-family:宋体"}[Authenticator]{lang="EN-US"}[属性失败的时候，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius dynamic-author proxy error]{lang="EN-US"}]{#struct_0_x1104_x1396_1961523040}

[\*Aug  7 18:09:38:603 2012 Sysname RADIUS DYNAMIC-AUTHOR PROXY/7/ERROR: -MDC=1; Failed to authenticate packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1104_x1396_x721702666}*[校验报文失败]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1104_x1396_98560690}[在]{style="font-family:宋体"}[Master AC]{lang="EN-US"}[上打开]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的事件调试信息开关，当]{style="font-family:宋体"}[Master AC]{lang="EN-US"}[上开启]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理功能时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius dynamic-author proxy event]{lang="EN-US"}]{#struct_0_x1104_x1396_x1763096967}

[\*Feb  1 16:54:50:621 2013 Sysname DAE PROXY/7/Event: -MDC=1; Enable DAE proxy.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1104_x1396_1577234917}*[开启]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理功能]{style="font-family:宋体"}*

[[\*Feb  1 16:54:50:621 2013 Sysname DAE PROXY/7/Event: -MDC=1; Start to connect WLAN.]{lang="EN-US"}]{#struct_0_x1104_x1396_x1777530955}

[*[// ]{lang="EN-US"}*]{#struct_0_x1104_x1396_x106882815}*[开始与]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[模块建立连接]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_x1104_x1396_1633945775}[在]{style="font-family:宋体"}[Master AC]{lang="EN-US"}[上开启]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理功能，打开]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理的报文调试信息开关，当]{style="font-family:宋体"}[DAE]{lang="EN-US"}[代理收到]{style="font-family:宋体"}[DM_REQ]{lang="EN-US"}[报文时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging radius dynamic-author proxy packet]{lang="EN-US"}]{#struct_0_x1104_x1396_x1853119974}

[\*Feb  1 17:21:34:322 2013 Sysname DAE PROXY/7/Packet: -MDC=1; Received DAE packet: SRC IP = 6.6.6.6, Port = 1360, Type = disconnect request packet]{lang="EN-US"}

[28 00 00 19 4b f5 f0 07 0c 30 d9 6b f9 09 6d 68]{lang="EN-US"}

[95 29 97 b9 01 05 68 33 63]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1104_x1396_1491050573}*[收到]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[6.6.6.6]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[1360]{lang="EN-US"}[，报文类型为]{style="font-family:宋体"}[disconnect request]{lang="EN-US"}*

[[\*Feb  1 17:21:34:324 2013 Sysname DAE PROXY/7/Packet: -MDC=1; Sent DAE packet: DEST IP = 111.8.200.2, Port = 3799, Type = disconnect request packet]{lang="EN-US"}]{#struct_0_x1104_x1396_714758322}

[28 00 00 19 4b f5 f0 07 0c 30 d9 6b f9 09 6d 68]{lang="EN-US"}

[95 29 97 b9 01 05 68 33 63]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1104_x1396_1430762772}*[发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[地址为]{style="font-family:宋体"}[111.8.200.2]{lang="EN-US"}[，]{style="font-family:宋体"}[端口为]{style="font-family:宋体"}[3799]{lang="EN-US"}[，报文类型为]{style="font-family:宋体"}[disconnect request]{lang="EN-US"}*

*[ ]{lang="EN-US"}*
