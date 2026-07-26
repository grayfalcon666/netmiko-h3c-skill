::: {#271424435 .myid}
[]{#_Toc404785942}[]{#struct_0_x4550_11699_x1210807624}[]{#_Toc353873267}[]{#_Toc353818160}

**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta error**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4550_11699_1348262391}

[**[debugging rta error]{lang="EN-US"}**]{#struct_0_x4550_11699_736713433}

[**[undo debugging rta error]{lang="EN-US"}**]{#struct_0_x4550_11699_x2122792616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4550_11699_438770669}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1038726143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4550_11699_375140687}

[[network-admin]{lang="EN-US"}]{#struct_0_x4550_11699_x386047629}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4550_11699_x1083465255}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x2027722973}

[**[debugging rta error]{lang="EN-US"}**]{#struct_0_x4550_11699_344797432}[命令用来打开终端接入错误调试信息开关。]{style="font-family:宋体"}**[undo debugging rta error]{lang="EN-US"}**[命令关闭终端接入错误调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，终端接入错误调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4550_11699_x556505149}

[[表1-1 ]{lang="EN-US"}[debugging rta error]{lang="EN-US"}]{#struct_0_x4550_11699_2081663846}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1186061684}[[字段]{style="font-family:黑体"}]{#struct_0_x4550_11699_x1478560100}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4550_11699_x1725824709}

[[Failed to activate listening port *port-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_375108333}

[[指定监听端口]{style="font-family:宋体"}*[port-id]{lang="EN-US"}*]{#struct_0_x4550_11699_606090739}[的转发组激活失败]{style="font-family:宋体"}

[[Unknown mesh message.]{lang="EN-US"}]{#struct_0_x4550_11699_x1811912926}

[[消息处理函数为空]{style="font-family:宋体"}]{#struct_0_x4550_11699_x89570742}

[[Invalid mesh message.]{lang="EN-US"}]{#struct_0_x4550_11699_34511589}

[[消息为空]{style="font-family:宋体"}]{#struct_0_x4550_11699_1350285803}

[[Failed to send mesh message to all slots.]{lang="EN-US"}]{#struct_0_x4550_11699_1830346316}

[[组播通道向所有节点同步数据失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_1758211081}

[[Mesh data is too long.]{lang="EN-US"}]{#struct_0_x4550_11699_x1778011985}

[[发送数据过长]{style="font-family:宋体"}]{#struct_0_x4550_11699_324143466}

[[Failed to get mesh channel.]{lang="EN-US"}]{#struct_0_x4550_11699_x959993202}

[[Server]{lang="EN-US"}]{#struct_0_x4550_11699_x824928995}[根据]{style="font-family:宋体"}[LIP]{lang="EN-US"}[获取]{style="font-family:宋体"}[Client]{lang="EN-US"}[的单播通道失败]{style="font-family:宋体"}

[[Failed to send mesh message to interface cards.]{lang="EN-US"}]{#struct_0_x4550_11699_1364633246}

[[向指定接口板同步数据失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x2005814953}

[[Failed to send mesh message to server\'s MPU.]{lang="EN-US"}]{#struct_0_x4550_11699_184309917}

[[Client]{lang="EN-US"}]{#struct_0_x4550_11699_1206213966}[向]{style="font-family:宋体"}[Server]{lang="EN-US"}[的主控板发送数据失败]{style="font-family:宋体"}

[[Failed to create mesh message.]{lang="EN-US"}]{#struct_0_x4550_11699_x1806323821}

[[创建]{style="font-family:宋体"}[mesh]{lang="EN-US"}]{#struct_0_x4550_11699_1056429433}[消息失败]{style="font-family:宋体"}

[[Failed to allocate memory for RTC relay epoll of forward group *group-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_x615033653}

[[为指定转发组]{style="font-family:宋体"}*[group-id]{lang="EN-US"}*]{#struct_0_x4550_11699_x1092324380}[分配]{style="font-family:宋体"}[Relay Epoll ]{lang="EN-US"}[数据内存失败]{style="font-family:宋体"}

[[Failed to assign index to RTC relay client.]{lang="EN-US"}]{#struct_0_x4550_11699_x460943880}

[[创建转发组内客户端索引失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_693075842}

[[Failed to get index of RTC relay forward group.]{lang="EN-US"}]{#struct_0_x4550_11699_345742185}

[[获取转发组的索引失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_288729211}

[[Failed to allocate memory for RTC relay forward group.]{lang="EN-US"}]{#struct_0_x4550_11699_x509654508}

[[为转发组分配存储空间失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_368755727}

[[Number of RTC relay clients for forward group *group-id* exceeded the maximum.]{lang="EN-US"}]{#struct_0_x4550_11699_x1905013466}

[[转发组]{style="font-family:宋体"}[group-id ]{lang="EN-US"}]{#struct_0_x4550_11699_x1372647990}[的客户端已达最大支持数目]{style="font-family:宋体"}

[[Failed to set socket option for RTC relay client.]{lang="EN-US"}]{#struct_0_x4550_11699_x252835352}

[[设置]{style="font-family:宋体"}[RTC Relay]{lang="EN-US"}]{#struct_0_x4550_11699_x2012173311}[客户端的]{style="font-family:宋体"}[socket]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[Failed to update RTC relay keepalive option (Server-ID: *server-id*, Client-ID: *client-id*).]{lang="EN-US"}]{#struct_0_x4550_11699_1412594257}

[[更新指定]{style="font-family:宋体"}[RTC Relay]{lang="EN-US"}]{#struct_0_x4550_11699_x865085717}[客户端的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[Failed to update RTC relay sendbuff option (Server-ID: *server-id*, Client-ID: *client-id*).]{lang="EN-US"}]{#struct_0_x4550_11699_7825254}

[[更新指定]{style="font-family:宋体"}[RTC Relay]{lang="EN-US"}]{#struct_0_x4550_11699_837439727}[客户端的]{style="font-family:宋体"}[sendbuff]{lang="EN-US"}[的大小失败]{style="font-family:宋体"}

[[Failed to update RTC relay recvbuff option (Server-ID: *server-id*, Client-ID: *client-id*).]{lang="EN-US"}]{#struct_0_x4550_11699_449156601}

[[更新指定]{style="font-family:宋体"}[RTC Relay]{lang="EN-US"}]{#struct_0_x4550_11699_680275202}[客户端的]{style="font-family:宋体"}[recvbuff]{lang="EN-US"}[的大小失败]{style="font-family:宋体"}

[[Failed to update RTC relay nodelay option (Server-ID: *server-id*, Client-ID: *client-id*).]{lang="EN-US"}]{#struct_0_x4550_11699_x153489684}

[[更新指定]{style="font-family:宋体"}[RTC Relay]{lang="EN-US"}]{#struct_0_x4550_11699_x971496754}[客户端的]{style="font-family:宋体"}[nodelay]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[\[Server *server-id* Client *client-id*\] Failed to save data to other clients in the forward group..]{lang="EN-US"}]{#struct_0_x4550_11699_1768209956}

[[将从指定]{style="font-family:宋体"}[client]{lang="EN-US"}]{#struct_0_x4550_11699_1316561877}[获取的报文保存到转发组内其他客户端失败]{style="font-family:宋体"}

[[Invalid negotiation packet.]{lang="EN-US"}]{#struct_0_x4550_11699_1250594786}

[[协商报文无效]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1719573625}

[[RTC relay client accepted invalid socket for forward group *group-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_2084170951}

[[指定转发组接收的客户端连接的]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_x956274037}[无效]{style="font-family:宋体"}

[[Failed to add relay client socket to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_x1043390600}

[[添加客户端连接]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_1009309730}[到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to allocate memory for updating client buffer.]{lang="EN-US"}]{#struct_0_x4550_11699_2004106627}

[[更新客户端缓存时申请内存失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_1535311932}

[[Failed to add RTC relay data to epoll for listening port *port-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_x1007640417}

[[添加指定端口]{style="font-family:宋体"}[port-id]{lang="EN-US"}]{#struct_0_x4550_11699_x190380635}[的]{style="font-family:宋体"}[relay]{lang="EN-US"}[数据到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to create RTC relay forward group.]{lang="EN-US"}]{#struct_0_x4550_11699_x556774211}

[[创建转发组数据失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1434771394}

[[Failed to create the backup terminal timer.]{lang="EN-US"}]{#struct_0_x4550_11699_x131602323}

[[创建链路备份定时器失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_256822281}

[[TTY\[*tty-number*\]:Failed to create the auto-close timer.]{lang="EN-US"}]{#struct_0_x4550_11699_x2122858152}

[[创建自动断链定时器失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_362139250}

[[TTY\[*tty-number*\]:Failed to create the auto-link timer.]{lang="EN-US"}]{#struct_0_x4550_11699_1864176690}

[[创建自动建链定时器失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x790163640}

[[TTY\[*tty-number*\] IF\[*ifIndex*\]:Failed to create TTY.]{lang="EN-US"}]{#struct_0_x4550_11699_1911736268}

[[指定接口]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}]{#struct_0_x4550_11699_606025203}[下的]{style="font-family:宋体"}[tty]{lang="EN-US"}[创建失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] VTY\[*vty-number*\]:Transmitting VTY template failed.]{lang="EN-US"}]{#struct_0_x4550_11699_x239263942}

[[根据]{style="font-family:宋体"}[tty]{lang="EN-US"}]{#struct_0_x4550_11699_139024008}[模板填充运行数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] VTY\[*vty-number*\]:Transmitting multipeer client failed.]{lang="EN-US"}]{#struct_0_x4550_11699_x960058738}

[[传输一对多客户端阶段失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x276399223}

[[TTY\[*tty-number*\]  IfIndex\[*ifIndex*\]: Activation failed.]{lang="EN-US"}]{#struct_0_x4550_11699_2144921773}

[[激活阶段失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_375106208}

[[Failed to get active VTY.]{lang="EN-US"}]{#struct_0_x4550_11699_1056363897}

[[获取当前生效的]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_x4550_11699_x142031012}[失败]{style="font-family:宋体"}

[[Failed to send TCP *send-size* data to APP. Error Code:  *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_1674609924}

[[向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_x4550_11699_2037783375}[发送]{style="font-family:宋体"}[TCP]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to send UDP *send-size* data for APP, Error code: *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_x509720044}

[[向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_x4550_11699_1149301128}[发送]{style="font-family:宋体"}[UDP]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to add epoll out event for socket *socket-fd.*]{lang="EN-US"}]{#struct_0_x4550_11699_1255258262}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_2098448941}[添加]{style="font-family:宋体"}[OUT]{lang="EN-US"}[事件失败]{style="font-family:宋体"}

[[The VRF *VpnName* is not found.]{lang="EN-US"}]{#struct_0_x4550_11699_1412528721}

[[获取]{style="font-family:宋体"}[vrf]{lang="EN-US"}]{#struct_0_x4550_11699_x1245992616}[索引失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to send synchronization data to Multi-UDP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1022213119}

[[向]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x4550_11699_967370270}[一对多组网各]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[发送报文失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to send *IfName* data to Single-UDP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x153555220}

[[UDP]{lang="EN-US"}]{#struct_0_x4550_11699_x121001119}[发送数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:Failed to get active APP.]{lang="EN-US"}]{#struct_0_x4550_11699_136213774}

[[获取当前生效的]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_x4550_11699_x1903131666}[失败]{style="font-family:宋体"}

[[Failed to encrtypt by MD5.]{lang="EN-US"}]{#struct_0_x4550_11699_x1719639161}

[[对验证字符串以及密码进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_x4550_11699_1009244194}[加密失败]{style="font-family:宋体"}

[[Failed to decrypt authentication password.]{lang="EN-US"}]{#struct_0_x4550_11699_1618015887}

[[对密码进行解密失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1439538451}

[[TTY\[*tty-number*\]: Failed to send authentication message due to invalid APP state\< *state* \>.]{lang="EN-US"}]{#struct_0_x4550_11699_x556839747}

[[APP]{lang="EN-US"}]{#struct_0_x4550_11699_1612456773}[状态错误导致发送验证信息到]{style="font-family:宋体"}[APP]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to send negotiation packet from client to server.]{lang="EN-US"}]{#struct_0_x4550_11699_x571216427}

[[TCP]{lang="EN-US"}]{#struct_0_x4550_11699_x1377518212}[连接建立后]{style="font-family:宋体"}[Client]{lang="EN-US"}[端向]{style="font-family:宋体"}[Server]{lang="EN-US"}[端发送协商报文失败]{style="font-family:宋体"}

[[UDP server remote IP or port is different, remote IP: *ip* vs *ip*; remote port: *port-id* vs *port-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_x2122923688}

[[UDP SERVER]{lang="EN-US"}]{#struct_0_x4550_11699_232012648}[接收数据时的]{style="font-family:宋体"}[remote IP]{lang="EN-US"}[或端口不一致]{style="font-family:宋体"}

[[TTY\[*tty-number*\]APP\[*app-number*\]:Reached the APP buffer threshould.]{lang="EN-US"}]{#struct_0_x4550_11699_1179729360}

[[达到]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_605959667}[缓冲区的阈值]{style="font-family:宋体"}

[[The TTY\[*tty-number*\] is not found.]{lang="EN-US"}]{#struct_0_x4550_11699_x1509733602}

[[没有找到指定的]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_480242322}

[[The APP\[*app-number*\] is not found.]{lang="EN-US"}]{#struct_0_x4550_11699_x960124274}

[[没有找到指定的]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_840561448}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to create TCP client socket for epoll out.]{lang="EN-US"}]{#struct_0_x4550_11699_x717025371}

[[将描述符从]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_1056298361}[中移出时创建客户端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:Failed to create the idle timer.]{lang="EN-US"}]{#struct_0_x4550_11699_x239810003}

[[指定]{style="font-family:宋体"}[TTY *tty-number*\] ]{lang="EN-US"}]{#struct_0_x4550_11699_x1778195689}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接空闲超时定时器失败]{style="font-family:宋体"}

[[Failed to set TCP server socketoption.]{lang="EN-US"}]{#struct_0_x4550_11699_x509785580}

[[设置]{style="font-family:宋体"}[server]{lang="EN-US"}]{#struct_0_x4550_11699_x1222690669}[端与]{style="font-family:宋体"}[client]{lang="EN-US"}[端通信的]{style="font-family:宋体"}[Socket]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to allocate epoll data for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1920294585}

[[指定]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1412463185}[的]{style="font-family:宋体"}[app]{lang="EN-US"}[创建]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to add epoll data for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x807688488}

[[将指定]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x153620756}[的]{style="font-family:宋体"}[app]{lang="EN-US"}[的]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to create TCP client socket.]{lang="EN-US"}]{#struct_0_x4550_11699_x916262194}

[[创建]{style="font-family:宋体"}[tcp client ]{lang="EN-US"}]{#struct_0_x4550_11699_x1275664196}[端]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to create UDP socket.]{lang="EN-US"}]{#struct_0_x4550_11699_x1719704697}

[[创建]{style="font-family:宋体"}[UDP socket]{lang="EN-US"}]{#struct_0_x4550_11699_x286433516}[失败]{style="font-family:宋体"}

[[Failed to get the TCP client IP address.]{lang="EN-US"}]{#struct_0_x4550_11699_x1248997298}

[[获取]{style="font-family:宋体"}[client]{lang="EN-US"}]{#struct_0_x4550_11699_x528339494}[端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to find APP by the TCP client IP address.]{lang="EN-US"}]{#struct_0_x4550_11699_1009178658}

[[通过]{style="font-family:宋体"}[client]{lang="EN-US"}]{#struct_0_x4550_11699_1599391912}[端]{style="font-family:宋体"}[IP]{lang="EN-US"}[查找]{style="font-family:宋体"}[app]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to check VPN  by the TCP client.]{lang="EN-US"}]{#struct_0_x4550_11699_x556905283}

[[TCP client]{lang="EN-US"}]{#struct_0_x4550_11699_124693486}[检验]{style="font-family:宋体"}[VPN]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[The negotiated APP is not  the current APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x6131643}

[[协商的]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x2122989224}[不是当前]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[Failed to check negotiation data by the TCP server.]{lang="EN-US"}]{#struct_0_x4550_11699_1771770870}

[[TCP server]{lang="EN-US"}]{#struct_0_x4550_11699_605894131}[端检查协商数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Failed to add the TCP server socket *socket-fd* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_810914711}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_x1323525278}[中添加]{style="font-family:宋体"}[TCP server]{lang="EN-US"}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[文件描述符]{style="font-family:宋体"}*[socket-fd ]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[Failed to check TCP client terminal number.]{lang="EN-US"}]{#struct_0_x4550_11699_x960189810}

[[TCP server]{lang="EN-US"}]{#struct_0_x4550_11699_x246157179}[验证]{style="font-family:宋体"}[client]{lang="EN-US"}[端终端索引号失败]{style="font-family:宋体"}

[[Failed to negotiate by the TCP server socket *socket-fd.*]{lang="EN-US"}]{#struct_0_x4550_11699_1056232825}

[[指定]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_x1700971493}[的]{style="font-family:宋体"}[TCP server]{lang="EN-US"}[端接收协商报文后协商失败]{style="font-family:宋体"}

[[Failed to receive the TCP client negotiation data by the TCP server socket *socket-fd.*]{lang="EN-US"}]{#struct_0_x4550_11699_810615370}

[[指定]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_x509851116}[的]{style="font-family:宋体"}[TCP server]{lang="EN-US"}[端接收客户端的协商报文失败]{style="font-family:宋体"}

[[Failed to spawn TCP server socket by listening socket *socket-fd.*]{lang="EN-US"}]{#struct_0_x4550_11699_1537631873}

[[通过监听]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_366518328}[创建]{style="font-family:宋体"}[TCP server socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add TCP server socket *socket-fd* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_1546680913}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_x16366700}[中添加]{style="font-family:宋体"}[TCP server ]{lang="EN-US"}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[文件描述符失败]{style="font-family:宋体"}

[[Failed to create TCP listening socket by port *port-id.*]{lang="EN-US"}]{#struct_0_x4550_11699_1364414915}

[[创建指定端口]{style="font-family:宋体"}*[port-id]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x4550_11699_x19403028}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to add TCP listening socket *socket-fd* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_x1039784647}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_x1304264455}[中添加]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[文件描述符失败]{style="font-family:宋体"}

[[Failed to allocate temporary receive-buffer for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1585486969}

[[申请临时接受数据缓冲区失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x21309457}

[[TTY\[*tty-number*\]\]:Failed to find the TTY for  asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x1894079454}

[[没有找到异步接口上的]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1143396386}

[[TTY\[*tty-number*\]:Failed to receive the data from]{lang="EN-US"}]{#struct_0_x4550_11699_2089191503}

[[asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x494346453}

[[从异步接口上接收数据失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x422687555}

[[IfIndex\[*ifIndex*\]:Failed to open asynchronization]{lang="EN-US"}]{#struct_0_x4550_11699_x2024305406}

[[ interface device.]{lang="EN-US"}]{#struct_0_x4550_11699_x1988771496}

[[打开指定异步接口]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}]{#struct_0_x4550_11699_x961459217}[设备失败]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Failed to allocate epoll data for]{lang="EN-US"}]{#struct_0_x4550_11699_x1867452154}

[[ asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_740111859}

[[为指定的异步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x4550_11699_1499967270}[分配]{style="font-family:宋体"}[epoll ]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Failed to add epoll data for ]{lang="EN-US"}]{#struct_0_x4550_11699_x261698524}

[[asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x825972082}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_2145381115}[中添加指定异步串口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*[的]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Failed to put asynchronization interface authorization.]{lang="EN-US"}]{#struct_0_x4550_11699_1190450553}

[[释放指定异步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x4550_11699_367024164}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[使用权失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to create ]{lang="EN-US"}]{#struct_0_x4550_11699_x92096605}

[[asynchronization buffer.]{lang="EN-US"}]{#struct_0_x4550_11699_x375633388}

[[创建异步处理数据]{style="font-family:宋体"}[buffer]{lang="EN-US"}]{#struct_0_x4550_11699_1640986468}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to get ]{lang="EN-US"}]{#struct_0_x4550_11699_1546615377}

[[asynchronization interface authorization.]{lang="EN-US"}]{#struct_0_x4550_11699_x1979259459}

[[和]{style="font-family:宋体"}[tty]{lang="EN-US"}]{#struct_0_x4550_11699_x19468564}[交互获取异步接口的使用权失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:Failed to send data to ]{lang="EN-US"}]{#struct_0_x4550_11699_x1585552505}

[[asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_297696338}

[[发送数据到异步接口上的]{style="font-family:宋体"}[tty]{lang="EN-US"}]{#struct_0_x4550_11699_x2140693552}[失败]{style="font-family:宋体"}

[[Failed to send *send-size*-byte asynchronization data. Error code: *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_1143330850}

[[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*]{#struct_0_x4550_11699_x1799470090}[字节异步数据失败]{style="font-family:宋体"}[,]{lang="EN-US"}[打印系统错误号]{style="font-family:宋体"}*[errno]{lang="EN-US"}*

[[Failed to send *send-size*-byte asynchronization data.]{lang="EN-US"}]{#struct_0_x4550_11699_x422753091}

[[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*]{#struct_0_x4550_11699_x1242079403}[字节异步数据失败]{style="font-family:宋体"}

[[Failed to receive *receive-size* data from]{lang="EN-US"}]{#struct_0_x4550_11699_x1988837032}

[[ asynchronization interface, errno is *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_x1569980813}

[[从异步接口接收数据失败，系统错误号]{style="font-family:宋体"}*[errno]{lang="EN-US"}*]{#struct_0_x4550_11699_740046323}

[[Failed to allocate memory for asynchronous ]{lang="EN-US"}]{#struct_0_x4550_11699_x826037618}

[[temporary receive-buffer.]{lang="EN-US"}]{#struct_0_x4550_11699_x1108309032}

[[申请临时的异步接受数据缓存失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x527712644}

[[Invalid socket or empty send-buffer for]{lang="EN-US"}]{#struct_0_x4550_11699_1190385017}

[[ synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x375698924}

[[同步接口向指定的发送]{style="font-family:宋体"}[packet socket]{lang="EN-US"}]{#struct_0_x4550_11699_927489511}[时的]{style="font-family:宋体"}[socket]{lang="EN-US"}[无效或发送缓存为空]{style="font-family:宋体"}

[[Failed to send *send-size*-byte synchronization data. Error code: *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_1546549841}

[[发送数据失败，系统错误号]{style="font-family:宋体"}*[errno]{lang="EN-US"}*]{#struct_0_x4550_11699_762469537}

[[Invalid socket or empty receive-buffer for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x19534100}

[[同步接口从指定的]{style="font-family:宋体"}[packet socket]{lang="EN-US"}]{#struct_0_x4550_11699_x1585618041}[接收数据时]{style="font-family:宋体"}[socket]{lang="EN-US"}[无效或接收缓存为空]{style="font-family:宋体"}

[[Failed to receive data  from synchronization interface. Error code: *errno.*]{lang="EN-US"}]{#struct_0_x4550_11699_730689189}

[[从同步接口接收数据失败，系统错误号]{style="font-family:宋体"}*[errno]{lang="EN-US"}*]{#struct_0_x4550_11699_1143265314}

[[TTY\[*tty-number*\]:Failed to find the TTY for ]{lang="EN-US"}]{#struct_0_x4550_11699_x422818627}

[[synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x873158986}

[[同步接口上找不到指定的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}]{#struct_0_x4550_11699_x1988902568}

[[TTY\[*tty-number*\] IF\[*ifIndex*\]:Failed to receive the data from synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_739980787}

[[从指定应用接口]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}]{#struct_0_x4550_11699_810792139}[的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[接收同步数据失败]{style="font-family:宋体"}

[[IF\[*ifIndex*\]:Failed to creare socket for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x826103154}

[[指定的同步接口]{style="font-family:宋体"}[ifIndex]{lang="EN-US"}]{#struct_0_x4550_11699_x1888330077}[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Failed to bind IP and set socket for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1190319481}

[[指定的同步接口]{style="font-family:宋体"}[IfIndex]{lang="EN-US"}]{#struct_0_x4550_11699_x375764460}[绑定报文特征地址及设置]{style="font-family:宋体"}[socket]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to create ]{lang="EN-US"}]{#struct_0_x4550_11699_x321792756}

[[packet socket for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1546484305}

[[为指定同步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x4550_11699_x19599636}[上应用的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[创建]{style="font-family:宋体"}[packet socket]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to add socket]{lang="EN-US"}]{#struct_0_x4550_11699_x688582726}

[[ to epoll for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x1585683577}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_120986697}[中添加指定同步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*[上应用的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[的]{style="font-family:宋体"}[socket]{lang="EN-US"}[文件描述符失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to allocate]{lang="EN-US"}]{#struct_0_x4550_11699_1143199778}

[[ epoll data for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x422884163}

[[向]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_x856215698}[中添加指定同步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*[上应用的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[的]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to create]{lang="EN-US"}]{#struct_0_x4550_11699_x1988968104}

[[ buffer for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_739915251}

[[创建指定同步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x4550_11699_x826168690}[上应用的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[使用的]{style="font-family:宋体"}[buffer]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to create]{lang="EN-US"}]{#struct_0_x4550_11699_1963369894}

[[ temporary buffer for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1190253945}

[[创建指定同步接口]{style="font-family:宋体"}*[ifIndex]{lang="EN-US"}*]{#struct_0_x4550_11699_x375829996}[上应用的]{style="font-family:宋体"}[TTY *tty-number*]{lang="EN-US"}[使用的临时缓存]{style="font-family:宋体"}[buffer]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Failed to send data to ]{lang="EN-US"}]{#struct_0_x4550_11699_x1784288873}

[[synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1546418769}

[[取出]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_x19665172}[缓冲区的数据发送到同步接口终端失败]{style="font-family:宋体"}

[[Failed to allocate temporary receive-buffer for synchronization.]{lang="EN-US"}]{#struct_0_x4550_11699_354136522}

[[为同步接口上分配临时接收缓存失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1585749113}

[[Protocol operation failed.]{lang="EN-US"}]{#struct_0_x4550_11699_1143134242}

[[协议操作失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_1316778319}

[[Failed to copy protocol option.]{lang="EN-US"}]{#struct_0_x4550_11699_x422949699}

[[拷贝协议选项失败]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1989033640}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x925112444}

[[\# ]{lang="EN-US"}]{#struct_0_x4550_11699_x1587746297}[在设备上进行]{style="font-family:宋体"}[ERROR]{lang="EN-US"}[的相关配置，打开]{style="font-family:宋体"}[ERROR]{lang="EN-US"}[的调试信息开关。当用户登录设备时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rta error]{lang="EN-US"}]{#struct_0_x4550_11699_2142002636}

[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1; RTC relay client for forward group 1 has been used up.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_1697861154}*[转发组]{style="font-family:宋体"}[1]{lang="EN-US"}[下已经有十个客户端，此时再次链接该转发组。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1; Failed to decrypt authentication password.]{lang="EN-US"}]{#struct_0_x4550_11699_x582425842}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_1015909364}*[对密码进行解密失败。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1;Failed to create the backup terminal timer.]{lang="EN-US"}]{#struct_0_x4550_11699_2044343357}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_x1356217838}*[创建链路备份定时器失败。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/ERROR: -MDC=1;TTY\[1\]:Failed to find the TTY for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x26893130}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_259823172}*[找不到同步接口上指定的]{style="font-family:宋体"}[TTY 1]{lang="EN-US"}[。]{style="font-family:宋体"}*

::: {#-355880302 .myid}
[]{#_Toc404785943}[]{#struct_0_x4550_11699_x1614293168}[]{#_Toc353873268}[]{#_Toc353818161}

**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta event**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4550_11699_739849715}

[**[debugging rta event]{lang="EN-US"}**]{#struct_0_x4550_11699_816624345}

[**[undo debugging rta event]{lang="EN-US"}**]{#struct_0_x4550_11699_x449262747}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4550_11699_1205675890}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4550_11699_x144807242}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x1926313273}

[[network-admin]{lang="EN-US"}]{#struct_0_x4550_11699_x2066781194}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4550_11699_x440237861}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4550_11699_604227999}

[**[debugging rta event]{lang="EN-US"}**]{#struct_0_x4550_11699_x1256833141}[命令用来打开终端接入事件调试信息开关。]{style="font-family:宋体"}**[undo debugging rta event]{lang="EN-US"}**[命令关闭终端接入事件调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，终端接入事件调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4550_11699_1763699771}

[[表1-2 ]{lang="EN-US"}[debugging rta event]{lang="EN-US"}]{#struct_0_x4550_11699_x551410873}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_1194059516}[[字段]{style="font-family:黑体"}]{#struct_0_x4550_11699_x1053035889}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4550_11699_x826234226}

[[Responded to the interface deactive event caused by interface removal.]{lang="EN-US"}]{#struct_0_x4550_11699_x1470091704}

[[由删除引起的接口去激活事件已经响应]{style="font-family:宋体"}]{#struct_0_x4550_11699_56155474}

[[Responded to the interface up event.]{lang="EN-US"}]{#struct_0_x4550_11699_861497732}

[[接口]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x4550_11699_1268094065}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface down event.]{lang="EN-US"}]{#struct_0_x4550_11699_x2122111426}

[[接口]{style="font-family:宋体"}[DOWN]{lang="EN-US"}]{#struct_0_x4550_11699_1706089495}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface deactive event.]{lang="EN-US"}]{#struct_0_x4550_11699_x808174251}

[[接口]{style="font-family:宋体"}[DEACTIVE]{lang="EN-US"}]{#struct_0_x4550_11699_x1004747960}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface active event.]{lang="EN-US"}]{#struct_0_x4550_11699_1190188409}

[[接口]{style="font-family:宋体"}[ACTIVE]{lang="EN-US"}]{#struct_0_x4550_11699_1965339574}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface delete event.]{lang="EN-US"}]{#struct_0_x4550_11699_1018110897}

[[接口]{style="font-family:宋体"}[DELETE]{lang="EN-US"}]{#struct_0_x4550_11699_x607779585}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface aschange event.]{lang="EN-US"}]{#struct_0_x4550_11699_606210815}

[[接口]{style="font-family:宋体"}[ASCHANGE]{lang="EN-US"}]{#struct_0_x4550_11699_854626577}[事件已经响应]{style="font-family:宋体"}

[[Responded to the interface changeencap event.]{lang="EN-US"}]{#struct_0_x4550_11699_x1198194736}

[[接口]{style="font-family:宋体"}[CHANGEENCAP]{lang="EN-US"}]{#struct_0_x4550_11699_x375895532}[事件已经响应]{style="font-family:宋体"}

[[The RemoteTermConn license active event is processed.]{lang="EN-US"}]{#struct_0_x4550_11699_x1120378667}

[[远程终端]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x4550_11699_1802478790}[事件已经激活]{style="font-family:宋体"}

[[The RemoteTermConn license deactive event is processed.]{lang="EN-US"}]{#struct_0_x4550_11699_x1769158587}

[[远程终端]{style="font-family:宋体"}[License]{lang="EN-US"}]{#struct_0_x4550_11699_682042331}[事件已经去激活]{style="font-family:宋体"}

[[The mesh server is connected.]{lang="EN-US"}]{#struct_0_x4550_11699_1219523497}

[[Mesh]{lang="EN-US"}]{#struct_0_x4550_11699_1546353233}[通道]{style="font-family:宋体"}[Server]{lang="EN-US"}[端连通]{style="font-family:宋体"}

[[The mesh server is disconnected.]{lang="EN-US"}]{#struct_0_x4550_11699_1148768090}

[[Mesh]{lang="EN-US"}]{#struct_0_x4550_11699_433449030}[通道]{style="font-family:宋体"}[Server]{lang="EN-US"}[端断开]{style="font-family:宋体"}

[[The mesh client is connected.]{lang="EN-US"}]{#struct_0_x4550_11699_x1702035300}

[[Mesh]{lang="EN-US"}]{#struct_0_x4550_11699_630063462}[通道]{style="font-family:宋体"}[Client]{lang="EN-US"}[端连通]{style="font-family:宋体"}

[[The mesh client is disconnected.]{lang="EN-US"}]{#struct_0_x4550_11699_270981033}

[[Mesh]{lang="EN-US"}]{#struct_0_x4550_11699_x959638019}[通道]{style="font-family:宋体"}[Client]{lang="EN-US"}[端断开]{style="font-family:宋体"}

[[Updated RTC relay keepalive option. Server-ID: *server-id*, Client-ID: *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x19730708}

[[更新]{style="font-family:宋体"}[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_x1173906841}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[配置的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[参数成功]{style="font-family:宋体"}

[[Updated RTC relay sendbuff option. Server-ID: *server-id*, Client-ID: *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_1322886869}

[[更新]{style="font-family:宋体"}[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_673597864}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[配置的]{style="font-family:宋体"}[sendbuff]{lang="EN-US"}[参数成功]{style="font-family:宋体"}

[[Updated RTC relay recvbuff option. Server-ID: *server-id*, Client-ID: *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x1585814649}

[[更新]{style="font-family:宋体"}[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_1968163279}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[配置的]{style="font-family:宋体"}[recvbuff]{lang="EN-US"}[参数成功]{style="font-family:宋体"}

[[Updated RTC relay nodelay option. Server-ID: *server-id*, Client-ID: *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x494685823}

[[更新]{style="font-family:宋体"}[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_1606386742}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[配置的]{style="font-family:宋体"}[nodelay]{lang="EN-US"}[参数成功]{style="font-family:宋体"}

[[Received negotiation data. Server-ID: *server-id*, Client-ID : *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_159714630}

[[收到]{style="font-family:宋体"}[Client]{lang="EN-US"}]{#struct_0_x4550_11699_1143068706}[和]{style="font-family:宋体"}[Relay server]{lang="EN-US"}[的协商数据]{style="font-family:宋体"}

[[Updated RTC relay buffer-size. Server-ID: *server-id*, Client-ID: *client-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x1872107346}

[[更新]{style="font-family:宋体"}[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_x996747889}[的转发组缓存大小成功]{style="font-family:宋体"}

[[RTC relay created socket for listening port *listen-port-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_1299290859}

[[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_x1723901710}[创建监听端口成功]{style="font-family:宋体"}

[[RTC relay deleted listening port *listen-port-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x423015235}

[[Relay server]{lang="EN-US"}]{#struct_0_x4550_11699_x42229084}[删除监听端口成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The primary and backup links deactived.]{lang="EN-US"}]{#struct_0_x4550_11699_1901854898}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1315435861}[的主链路和备份链路失效]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The backup terminal timer timed out.]{lang="EN-US"}]{#struct_0_x4550_11699_x1989099176}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1715064435}[备份链路定时器超时]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The backup terminal timer is deleted.]{lang="EN-US"}]{#struct_0_x4550_11699_215930771}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1818027951}[备份链路定时器删除]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The backup terminal timer is created.]{lang="EN-US"}]{#struct_0_x4550_11699_739784179}

[[创建]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1661482101}[备份链路定时器]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link teardown timer timed out.]{lang="EN-US"}]{#struct_0_x4550_11699_194737041}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x5094406}[自动断链定时器超时]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link teardown timer is deleted.]{lang="EN-US"}]{#struct_0_x4550_11699_x826299762}

[[删除]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1524360669}[自动断链定时器]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link teardown timer is created.]{lang="EN-US"}]{#struct_0_x4550_11699_x1871466959}

[[创建]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x562092203}[自动断链定时器]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link establishment timer timed out.]{lang="EN-US"}]{#struct_0_x4550_11699_1190122873}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_415330139}[自动建链定时器超时]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link establishment timer is deleted.]{lang="EN-US"}]{#struct_0_x4550_11699_x122184869}

[[删除]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x346476957}[自动建链定时器]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The automatic link establishment timer is created.]{lang="EN-US"}]{#struct_0_x4550_11699_x375961068}

[[创建]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1846505917}[自动建链定时器]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state is No Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1798848589}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1680570961}[的单链路状态机为]{style="font-family:宋体"}[No Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state changed to Primary Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1894091060}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x339231074}[的单链路状态机切换为]{style="font-family:宋体"}[Primary Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state changed to Backup Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x430740145}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_114487020}[的单链路状态机切换为]{style="font-family:宋体"}[Backup Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state is Primary Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1176288562}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x87199056}[的单链路状态机为]{style="font-family:宋体"}[Primary Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state is Backup Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1889729826}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1451596921}[的单链路状态机为]{style="font-family:宋体"}[Backup Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The single link state changed to No Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1902274904}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1883059194}[的单链路状态机切换为]{style="font-family:宋体"}[No Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link state is No Active.]{lang="EN-US"}]{#struct_0_x4550_11699_1277286434}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x232132376}[的双链路状态机为]{style="font-family:宋体"}[No Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link state changed to Primary Active.]{lang="EN-US"}]{#struct_0_x4550_11699_192203585}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x288797507}[的双链路状态机切换为]{style="font-family:宋体"}[Primary Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link state changed to Backup Active.]{lang="EN-US"}]{#struct_0_x4550_11699_124035806}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x906237745}[的双链路状态机切换为]{style="font-family:宋体"}[Backup Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link state is Primate Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x662483315}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1854881448}[的双链路状态机为]{style="font-family:宋体"}[Primate Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link current state is Backup Active.]{lang="EN-US"}]{#struct_0_x4550_11699_x1378879782}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_874001907}[的双链路状态机为]{style="font-family:宋体"}[Backup Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] Primary IfIndex\[*ifIndex*\] Backup IfIndex\[*ifIndex*\]:The double link state changed to No Active.]{lang="EN-US"}]{#struct_0_x4550_11699_1331721942}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1398693853}[的双链路状态机切换为]{style="font-family:宋体"}[No Active]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The phase of TTY starting is incompleted.]{lang="EN-US"}]{#struct_0_x4550_11699_x692082034}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1965636621}[创建未完成]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:TTY created successfully.]{lang="EN-US"}]{#struct_0_x4550_11699_559550250}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_1397120727}[创建成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Creating TTY.]{lang="EN-US"}]{#struct_0_x4550_11699_1324340601}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x253676541}[正在创建]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:Transmitting TTY template succeeded.]{lang="EN-US"}]{#struct_0_x4550_11699_x241743340}

[[传输]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x867722030}[配置模板成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\] VTY\[*vty-number*\]:Transmitting VTY template succeeded.]{lang="EN-US"}]{#struct_0_x4550_11699_1680505425}

[[传输]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_x4550_11699_114421484}[配置模板创建成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\] VTY\[*vty-number*\]:Transmitting multipeer client succeeded.]{lang="EN-US"}]{#struct_0_x4550_11699_x349605456}

[[传输]{style="font-family:宋体"}[multipeer client]{lang="EN-US"}]{#struct_0_x4550_11699_x1451662457}[配置模板创建成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:TTY activated successfully.]{lang="EN-US"}]{#struct_0_x4550_11699_1277220898}

[[初始化]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1405668032}[各模块，激活]{style="font-family:宋体"}[TTY]{lang="EN-US"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:TTY deactivated successfully.]{lang="EN-US"}]{#struct_0_x4550_11699_x1083399480}

[[去初始化]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x288863043}[各模块，去激活]{style="font-family:宋体"}[TTY]{lang="EN-US"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:TTY deleted successfully.]{lang="EN-US"}]{#struct_0_x4550_11699_534040783}

[[删除]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_540339280}[各模块]{style="font-family:宋体"}

[[All TTY deactived successfully.]{lang="EN-US"}]{#struct_0_x4550_11699_x1854946984}

[[去激活所有]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_823259349}[业务]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The TTY is processing interface up event.]{lang="EN-US"}]{#struct_0_x4550_11699_873936371}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_2015404960}[正在处理接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:The TTY is processing interface down event.]{lang="EN-US"}]{#struct_0_x4550_11699_x692147570}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x1126131143}[正在处理接口]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully added epoll out event for socket *socket-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_1324275065}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x243280301}[成功添加]{style="font-family:宋体"}[EPOLL OUT]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully sent synchronization data for Multi-UDP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_1355550892}

[[成功发送]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x4550_11699_x241808876}[同步数据到]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully sent *data-len* data for Single-UDP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1641564505}

[[成功发送]{style="font-family:宋体"}[Single-UDP]{lang="EN-US"}]{#struct_0_x4550_11699_1680439889}[数据到]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully sent data-len data for Single-TCP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1869265224}

[[成功发送]{style="font-family:宋体"}[Single-TCP]{lang="EN-US"}]{#struct_0_x4550_11699_1411440955}[数据到]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Block to send data-len data for Single-TCP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_114355948}

[[停止发送]{style="font-family:宋体"}[Single-TCP]{lang="EN-US"}]{#struct_0_x4550_11699_x727229266}[数据到]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[TTY\[*tty-number*\]:Clear terminal buffer for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1451727993}

[[清除]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_689733099}[的终端缓存]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Deal connectionless for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_292240012}

[[处理处于无连接状态的]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_1277155362}

[[TTY\[*tty-number*\]:Failed to send data to APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1778937157}

[[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x288928579}[发送消息失败]{style="font-family:宋体"}

[[Receive data *data-len* form UDP client APP, errno is *errno*.]{lang="EN-US"}]{#struct_0_x4550_11699_193962098}

[[从]{style="font-family:宋体"}[CLIENT APP]{lang="EN-US"}]{#struct_0_x4550_11699_x1855012520}[收到]{style="font-family:宋体"}[UDP]{lang="EN-US"}[数据]{style="font-family:宋体"}[,recvfrom]{lang="EN-US"}[函数错误码为]{style="font-family:宋体"}

[[Receive data data-len from UDP server APP, errno is data-len.]{lang="EN-US"}]{#struct_0_x4550_11699_x1945210121}

[[从]{style="font-family:宋体"}[SERVER APP]{lang="EN-US"}]{#struct_0_x4550_11699_873870835}[收到]{style="font-family:宋体"}[UDP]{lang="EN-US"}[数据，]{style="font-family:宋体"}[recvfrom]{lang="EN-US"}[函数错误码为]{style="font-family:宋体"}

[[Receive data data-len from TCP client APP, errno is data-len.]{lang="EN-US"}]{#struct_0_x4550_11699_x745942155}

[[从]{style="font-family:宋体"}[CLIENT APP]{lang="EN-US"}]{#struct_0_x4550_11699_x692213106}[收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[数据，]{style="font-family:宋体"}[recv]{lang="EN-US"}[函数错误码为]{style="font-family:宋体"}

[[Receive data data-len from TCP server APP, errno is data-len.]{lang="EN-US"}]{#struct_0_x4550_11699_1596835761}

[[从]{style="font-family:宋体"}[SERVER APP]{lang="EN-US"}]{#struct_0_x4550_11699_x1888832133}[收到]{style="font-family:宋体"}[TCP]{lang="EN-US"}[数据，]{style="font-family:宋体"}[recv]{lang="EN-US"}[函数错误码为]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:TCP socket is closed at the other side.]{lang="EN-US"}]{#struct_0_x4550_11699_1324209529}

[[TCP]{lang="EN-US"}]{#struct_0_x4550_11699_1248284051}[链接另一端的]{style="font-family:宋体"}[socket]{lang="EN-US"}[已经关闭]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully created TCP client socket for epoll out.]{lang="EN-US"}]{#struct_0_x4550_11699_x241874412}

[[成功创建]{style="font-family:宋体"}[CLIENT]{lang="EN-US"}]{#struct_0_x4550_11699_729628517}[端的]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}[用于处理]{style="font-family:宋体"}[epoll out]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Processed the epoll error event or epoll hup event for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_1680374353}

[[处理]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_1578650115}[的]{style="font-family:宋体"}[epoll error]{lang="EN-US"}[事件和]{style="font-family:宋体"}[epoll hup]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Processed the epoll out event for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1136118587}

[[处理]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_114290412}[的]{style="font-family:宋体"}[epoll out]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Processed the epoll in event for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1451793529}

[[处理]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x872531068}[的]{style="font-family:宋体"}[epoll in]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:The idle timer timed out.]{lang="EN-US"}]{#struct_0_x4550_11699_x2051568185}

[[链接空闲定时器超时]{style="font-family:宋体"}]{#struct_0_x4550_11699_1277089826}

[[TTY*\[tty-number*\]:The idle timer is deleted.]{lang="EN-US"}]{#struct_0_x4550_11699_x216523882}

[[删除链接空闲定时器]{style="font-family:宋体"}]{#struct_0_x4550_11699_x288994115}

[[TTY\[*tty-number*\]:The idle timer is created.]{lang="EN-US"}]{#struct_0_x4550_11699_x677242948}

[[创建链接空闲定时器]{style="font-family:宋体"}]{#struct_0_x4550_11699_1432283918}

[[TTY\[*tty-number*\]:The idle timer is refreshed.]{lang="EN-US"}]{#struct_0_x4550_11699_x1855078056}

[[刷新连接空闲定时器]{style="font-family:宋体"}]{#struct_0_x4550_11699_1175300906}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully allocated epoll data for APP.]{lang="EN-US"}]{#struct_0_x4550_11699_873805299}

[[成功为]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x692278642}[分配]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully added epoll data for app.]{lang="EN-US"}]{#struct_0_x4550_11699_1324143993}

[[成功为]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x229863029}[添加]{style="font-family:宋体"}[epoll]{lang="EN-US"}[数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully created TCP client socket.]{lang="EN-US"}]{#struct_0_x4550_11699_x241939948}

[[成功创建]{style="font-family:宋体"}[CLIENT]{lang="EN-US"}]{#struct_0_x4550_11699_1680308817}[端]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully created UDP socket.]{lang="EN-US"}]{#struct_0_x4550_11699_x305212741}

[[成功创建]{style="font-family:宋体"}[UDP socket]{lang="EN-US"}]{#struct_0_x4550_11699_114224876}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Successfully added the TCP server socket *socket-id* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_1248651506}

[[成功的把]{style="font-family:宋体"}[SERVER]{lang="EN-US"}]{#struct_0_x4550_11699_145405999}[端]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}[加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}

[[Successfully negotiated by the TCP server socket *socket-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_x1451859065}

[[SERVER]{lang="EN-US"}]{#struct_0_x4550_11699_897054687}[端]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}[协商成功]{style="font-family:宋体"}

[[Successfully spawned TCP listening socket by socket *socket-id*.]{lang="EN-US"}]{#struct_0_x4550_11699_1277024290}

[[成功创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4550_11699_x289059651}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[通过其他]{style="font-family:宋体"}[socket]{lang="EN-US"}

[[Successfully added TCP server socket *socket-id* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_1736184772}

[[成功的把]{style="font-family:宋体"}[SERVER]{lang="EN-US"}]{#struct_0_x4550_11699_1819034260}[端]{style="font-family:宋体"}[TCP socket]{lang="EN-US"}[加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}

[[Successfully created TCP listening socket by port *port-number*.]{lang="EN-US"}]{#struct_0_x4550_11699_x1855143592}

[[成功的通过端口]{style="font-family:宋体"}[port-number]{lang="EN-US"}]{#struct_0_x4550_11699_873739763}[创建]{style="font-family:宋体"}[TCP ]{lang="EN-US"}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}

[[Successfully added TCP listening socket *socket-id* to epoll.]{lang="EN-US"}]{#struct_0_x4550_11699_693817650}

[[成功的添加]{style="font-family:宋体"}[TCP ]{lang="EN-US"}]{#struct_0_x4550_11699_x692344178}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[到]{style="font-family:宋体"}[epoll]{lang="EN-US"}

[[Successfully deleted TCP listening socket *socket-id* from epoll and close.]{lang="EN-US"}]{#struct_0_x4550_11699_1324078457}

[[成功的从]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_474470587}[删除]{style="font-family:宋体"}[TCP ]{lang="EN-US"}[监听]{style="font-family:宋体"}[socket]{lang="EN-US"}[，并关闭]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Successfully allocated epoll data for asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x242005484}

[[成功的为异步接口分派]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_1680243281}[数据]{style="font-family:宋体"}

[[IfIndex\[*ifIndex*\]:Successfully added epoll data for asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_114159340}

[[成功的为异步接口添加数据]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1451924601}

[[IfIndex\[*ifIndex*\]:Successfully put asynchronization interface authorization.]{lang="EN-US"}]{#struct_0_x4550_11699_1276958754}

[[释放指定异步接口的]{style="font-family:宋体"}[TTY]{lang="EN-US"}]{#struct_0_x4550_11699_x604336371}[使用权限成功]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Successfully got asynchronization interface authorization.]{lang="EN-US"}]{#struct_0_x4550_11699_x289125187}

[[成功的获取异步接口授权]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1818260634}

[[TTY\[*tty-number*\]:Obtained data from APP buffer for asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x1855209128}

[[从]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x2128024352}[缓存获取异步接口数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\]:Process the epoll in event for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1994817779}

[[处理同步接口的]{style="font-family:宋体"}[epoll in]{lang="EN-US"}]{#struct_0_x4550_11699_873674227}[事件]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Successfully created packet socket for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x2120083503}

[[成功的创建同步接口的]{style="font-family:宋体"}[packet socket]{lang="EN-US"}]{#struct_0_x4550_11699_x692409714}

[[TTY\[*tty-number*\]IfIndex\[*ifIndex*\]:Successfully allocated epoll data for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1324012921}

[[成功的为同步接口分派]{style="font-family:宋体"}[epoll]{lang="EN-US"}]{#struct_0_x4550_11699_1320951064}[数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifIndex*\]:Successfully added socket to epoll for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x242071020}

[[成功的把同步接口]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x4550_11699_1737458951}[加入]{style="font-family:宋体"}[epoll]{lang="EN-US"}

[[TTY\[*tty-number*\] IF\[*ifIndex*\]:Obtained data from APP buffer for synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1814461009}

[[成功的从]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x4550_11699_x950824954}[缓存获取同步接口数据]{style="font-family:宋体"}

[[Obtained serial interface statistics(CRC error counts: *error-number*, input packets: *packets).*]{lang="EN-US"}]{#struct_0_x4550_11699_248377068}

[[下驱动获取串口统计信息]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1134204214}

[[The serial interface checked for encapsulation.]{lang="EN-US"}]{#struct_0_x4550_11699_x1317706873}

[[内核态检查为封装状态]{style="font-family:宋体"}]{#struct_0_x4550_11699_x1070918688}

[[The serial interface checked for decapsulation.]{lang="EN-US"}]{#struct_0_x4550_11699_1411176482}

[[内核态检查为去封装状态]{style="font-family:宋体"}]{#struct_0_x4550_11699_1657335348}

[[Processed mdc init event.]{lang="EN-US"}]{#struct_0_x4550_11699_x154907459}

[[处理]{style="font-family:宋体"}[mdc]{lang="EN-US"}]{#struct_0_x4550_11699_x638467410}[初始化事件]{style="font-family:宋体"}

[[Processed mdc start event.]{lang="EN-US"}]{#struct_0_x4550_11699_1100973250}

[[处理]{style="font-family:宋体"}[mdc start]{lang="EN-US"}]{#struct_0_x4550_11699_x1720991400}[事件]{style="font-family:宋体"}

[[Processed mdc stop event.]{lang="EN-US"}]{#struct_0_x4550_11699_1007891955}

[[处理]{style="font-family:宋体"}[mdc stop]{lang="EN-US"}]{#struct_0_x4550_11699_x1353017472}[事件]{style="font-family:宋体"}

[[Processed protocol enable control message.]{lang="EN-US"}]{#struct_0_x4550_11699_x558191986}

[[处理]{style="font-family:宋体"}[Rtc]{lang="EN-US"}]{#struct_0_x4550_11699_x2077524638}[协议特征使能]{style="font-family:宋体"}

[[Processed protocol disable control message.]{lang="EN-US"}]{#struct_0_x4550_11699_126199857}

[[处理]{style="font-family:宋体"}[Rtc]{lang="EN-US"}]{#struct_0_x4550_11699_1458230649}[协议特征去使能]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4550_11699_157033815}

[[\# ]{lang="EN-US"}]{#struct_0_x4550_11699_1397723220}[打开]{style="font-family:宋体"}[EVENT]{lang="EN-US"}[的事件调试信息开关。用户通过串口登录设备的操作时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="NO-BOK"}[debugging rta event]{lang="EN-US"}]{#struct_0_x4550_11699_269220477}

[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1;The interface up event is responsed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_x1158865326}*[接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件已经响应。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY\[1\]:The primary and backup links deactived.]{lang="EN-US"}]{#struct_0_x4550_11699_x107853292}

[*[// TTY 1]{lang="EN-US"}*]{#struct_0_x4550_11699_2000977234}*[的主链路和备份链路失效。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY\[1\]:The phase of Transmitting TTY template is successful.]{lang="EN-US"}]{#struct_0_x4550_11699_x1346341906}

[*[// ]{lang="PT-BR"}*]{#struct_0_x4550_11699_x1267159797}*[传输]{style="font-family:宋体"}[TTY 1]{lang="EN-US"}[配置模板创建成功。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; TTY\[1\]VTY\[0\]:The phase of transmitting VTY template is successful.]{lang="EN-US"}]{#struct_0_x4550_11699_x1621503228}

[*[// ]{lang="PT-BR"}*]{#struct_0_x4550_11699_1207641432}*[传输]{style="font-family:宋体"}[TTY 1]{lang="EN-US"}[下的]{style="font-family:宋体"}[VTY 0]{lang="EN-US"}[配置模板创建成功。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/EVENT: -MDC=1; Process mdc start event.]{lang="EN-US"}]{#struct_0_x4550_11699_x1440114624}

[*[// ]{lang="PT-BR"}*]{#struct_0_x4550_11699_x1143423936}*[处理]{style="font-family:宋体"}[mdc start]{lang="EN-US"}[事件。]{style="font-family:宋体"}*

::: {#790849552 .myid}
[]{#_Toc265747197}[]{#_Toc205709448}[]{#_Toc189473990}[]{#_Toc404785944}[]{#struct_0_x4550_11699_x561599062}[]{#_Toc353873269}[]{#_Toc353818162}

**RTC终端接入 \-- RTC终端接入调试命令 \-- debugging rta packet**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4550_11699_1247539437}

[**[debugging rta packet]{lang="EN-US"}**[ { **brief** \| **detail** } { **all** \| **recv-remote** \| **recv-terminal** \| **send-remote** \| **send-terminal** } *terminal-number*]{lang="EN-US"}]{#struct_0_x4550_11699_x1637786459}

[**[undo debugging rta packet ]{lang="EN-US"}**[{ **brief** \| **detail** } { **all** \| **recv-remote** \| **recv-terminal** \| **send-remote** \| **send-terminal** } *terminal-number*]{lang="EN-US"}]{#struct_0_x4550_11699_560708409}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x1376131750}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4550_11699_1086478717}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4550_11699_1631244821}

[[network-admin]{lang="EN-US"}]{#struct_0_x4550_11699_1814395473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4550_11699_x2120195304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x50318724}

[**[brief]{lang="EN-US"}**]{#struct_0_x4550_11699_x794997077}[：打开简要报文信息调试开关。]{style="font-family:宋体"}

[**[detail]{lang="EN-US"}**]{#struct_0_x4550_11699_1655216929}[：打开详细报文信息调试开关。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4550_11699_x1977652818}[：显示所有报文信息。]{style="font-family:宋体"}

[**[recv-remote]{lang="EN-US"}**]{#struct_0_x4550_11699_1858051397}[：显示设备从对端接收到的报文信息。]{style="font-family:宋体"}

[**[recv-terminal]{lang="EN-US"}**]{#struct_0_x4550_11699_1316335725}[：显示设备从终端接收到的报文信息。]{style="font-family:宋体"}

[**[send-remote]{lang="EN-US"}**]{#struct_0_x4550_11699_x14261477}[：显示设备向对端发送的报文信息。]{style="font-family:宋体"}

[**[send-terminal]{lang="EN-US"}**]{#struct_0_x4550_11699_x1426702555}[：显示设备向终端发送的报文信息。]{style="font-family:宋体"}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_x4550_11699_2025134613}[：需要显示信息的终端号。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x693218159}

[**[debugging rta packet]{lang="EN-US"}**]{#struct_0_x4550_11699_1239974055}[命令用来打开终端接入报文调试信息开关。]{style="font-family:宋体"}**[undo debugging rta packet]{lang="EN-US"}**[命令关闭终端接入报文调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，终端接入报文调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4550_11699_187253133}

[[表1-3 ]{lang="EN-US"}[debugging rta packet]{lang="EN-US"}]{#struct_0_x4550_11699_667860936}[命令输出信息列表]{style="font-family:黑体"}

[]{#table_struct_0_1500849134}[[字段]{style="font-family:黑体"}]{#struct_0_x4550_11699_248311532}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4550_11699_812626325}

[[TTY\[*tty-number*\] APP\[*app-number*\]: Sent *send-size* bytes synchronization data to remote Multi-UDP APP(IP=*ip*, Port=*port-id*).]{lang="EN-US"}]{#struct_0_x4550_11699_x262624391}

[[UDP]{lang="EN-US"}]{#struct_0_x4550_11699_x511511559}[一对多组网时，指定]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*[号的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[上的第]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*[个]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*[ ]{lang="EN-US"}[字节的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[数据数据到多个对端]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Sent *send-size* bytes data of *ifname* to Single-UDP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x495886875}

[[UDP]{lang="EN-US"}]{#struct_0_x4550_11699_x338620452}[一对一组网时，指定]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*[号的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[上的第]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*[个]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*[个字节数据到对端]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Sent *send-size* bytes data of *ifname* to Single-TCP APP.]{lang="EN-US"}]{#struct_0_x4550_11699_755950296}

[[TCP]{lang="EN-US"}]{#struct_0_x4550_11699_x91217461}[一对一组网时，指定]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*[号的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[上的第]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*[个]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*[个字节数据到对端]{style="font-family:宋体"}

[[TTY\[*tty-number*\] APP\[*app-number*\]:Received *receive-size* bytes data from remote APP.]{lang="EN-US"}]{#struct_0_x4550_11699_x1043094393}

[[指定]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*]{#struct_0_x4550_11699_x1317772409}[号的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[上的第]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*[个]{style="font-family:宋体"}[APP]{lang="EN-US"}[从对端接收]{style="font-family:宋体"}*[receive-size]{lang="EN-US"}*[个字节的数据]{style="font-family:宋体"}

[[APP\[*app-number*\] sent MD5 challenge to client failed.]{lang="EN-US"}]{#struct_0_x4550_11699_x302058225}

[[指定]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*]{#struct_0_x4550_11699_110859608}[的]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}[MD5]{lang="EN-US"}[加密信息到]{style="font-family:宋体"}[client]{lang="EN-US"}[端失败]{style="font-family:宋体"}

[[APP\[*app-number*\] sent MD5 challenge to server failed.]{lang="EN-US"}]{#struct_0_x4550_11699_1786383493}

[[指定]{style="font-family:宋体"}*[app-number]{lang="EN-US"}*]{#struct_0_x4550_11699_227410672}[的]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}[MD5]{lang="EN-US"}[加密信息到]{style="font-family:宋体"}[server]{lang="EN-US"}[端失败]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifindex*\]:Received *receive-size* bytes data from terminal in asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x2079333435}

[[指定终端号]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*]{#struct_0_x4550_11699_1598483277}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[从异步接口上的终端接收]{style="font-family:宋体"}*[receive-size]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifindex*\]:Sent *send-size* bytes data to terminal in asynchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_1411110946}

[[指定终端号]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*]{#struct_0_x4550_11699_1682375946}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*[字节的数据到异步接口上的终端]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifindex*\]:Received *receive-size* bytes data from terminal in synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x866992481}

[[指定终端号]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*]{#struct_0_x4550_11699_1857555175}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[从同步接口上的终端接收]{style="font-family:宋体"}*[receive-size]{lang="EN-US"}*[字节的数据]{style="font-family:宋体"}

[[TTY\[*tty-number*\] IfIndex\[*ifindex*\]:Sent *send-size* bytes data to terminal in synchronization interface.]{lang="EN-US"}]{#struct_0_x4550_11699_x823468702}

[[指定终端号]{style="font-family:宋体"}*[tty-number]{lang="EN-US"}*]{#struct_0_x4550_11699_x891378128}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[发送]{style="font-family:宋体"}*[send-size]{lang="EN-US"}*[字节的数据到同步接口上的终端]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4550_11699_x154972995}

[[\# ]{lang="EN-US"}]{#struct_0_x4550_11699_155126209}[打开]{style="font-family:宋体"}[PACKET]{lang="EN-US"}[的事件调试信息开关，当用户使用串口登录设备时，设备上输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging rta packet brief all 1]{lang="EN-US"}]{#struct_0_x4550_11699_x670352363}

[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/PACKET: -MDC=1; TTY\[1\] APP\[1\]:Send 88 bytes data of async to Single-TCP APP.]{lang="EN-US"}

[*[// ]{lang="EN-US"}[TCP]{lang="EN-US"}*]{#struct_0_x4550_11699_x1685984403}*[一对一组网时，指定的]{style="font-family:宋体"}[TTY 1]{lang="EN-US"}[上的第]{style="font-family:宋体"}[1]{lang="EN-US"}[个]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}[88]{lang="EN-US"}[个字节数据到对端。]{style="font-family:宋体"}*

[[\*Aug  7 18:20:48:047 2012 System RTERMCON/7/PACKET: -MDC=1; APP\[1\] send MD5 challenge to client failed.]{lang="EN-US"}]{#struct_0_x4550_11699_x1514590991}

[*[// ]{lang="EN-US"}*]{#struct_0_x4550_11699_337255235}*[指定]{style="font-family:宋体"}[app-number]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[APP]{lang="EN-US"}[发送]{style="font-family:宋体"}[MD5]{lang="EN-US"}[加密信息到]{style="font-family:宋体"}[client]{lang="EN-US"}[端失败。]{style="font-family:宋体"}*
