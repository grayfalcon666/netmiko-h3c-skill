::: {#318432791 .myid}
[]{#_Toc404792588}[]{#struct_0_99677_28654_x138941669}[]{#_Toc130718952}[]{#_Toc87257691}

**Portal \-- Portal调试命令 \-- debugging portal**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_99677_28654_2078830167}

[**[debugging portal]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** }]{lang="EN-US"}]{#struct_0_99677_28654_x649517180}

[**[undo debugging portal ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** }]{lang="EN-US"}]{#struct_0_99677_28654_1841875503}

[[【视图】]{style="font-family:黑体"}]{#struct_0_99677_28654_1759700221}

[[用户视图]{style="font-family:宋体"}]{#struct_0_99677_28654_2123703469}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_99677_28654_375162135}

[[network-admin]{lang="EN-US"}]{#struct_0_99677_28654_x57825222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_99677_28654_1601497872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_99677_28654_x2139651787}

[**[all]{lang="EN-US"}**]{#struct_0_99677_28654_x862638778}[：表示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_99677_28654_973438127}[：表示错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_99677_28654_1571667627}[：表示事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_99677_28654_590379977}[：表示状态机调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_99677_28654_1939090687}

[**[debugging portal]{lang="EN-US"}**]{#struct_0_99677_28654_x1710353133}[命令用来打开]{style="font-family:宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging portal]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x1489444914}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[]{#struct_0_99677_28654_228706837}[[表1-1 ]{lang="EN-US"}[debugging portal error]{lang="EN-US"}]{#_Toc130718926}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_314761424}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_99677_28654_368690720}
:::

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_x1935160391}

[[Failed to create the detection timer for portal server *server-name*.]{lang="EN-US"}]{#struct_0_99677_28654_x566225177}

[[创建]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_99677_28654_2018600867}[服务器探测定时器失败，]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器名称为]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*

[[User (IP:*user-ip*) will log off because of no IP address assigned by the DHCP server.]{lang="EN-US"}]{#struct_0_99677_28654_x605619992}

[[由于未能成功被]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_99677_28654_x439153889}[服务器分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，用户将被强制下线，用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[user-ip]{lang="EN-US"}*

[[Portal server didn\'t confirm the new IP. User will logoff.]{lang="EN-US"}]{#struct_0_99677_28654_x1949411677}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x1488855090}[服务器在指定时间内没有确认更新的用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，该用户将被强制下线]{style="font-family:宋体"}

[[Failed to start the timer for waiting for a new IP.]{lang="EN-US"}]{#struct_0_99677_28654_826002258}

[[开启等待更新]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_1202804371}[地址定时器失败]{style="font-family:宋体"}

[[Failed to open the timer for confirming new IP.]{lang="EN-US"}]{#struct_0_99677_28654_331150675}

[[开启确认新]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_x371333573}[地址定时器失败]{style="font-family:宋体"}

[[Failed to open the timer for waiting for ACK_NTF_LOGOUT.]{lang="EN-US"}]{#struct_0_99677_28654_x42043712}

[[开启等待]{style="font-family:宋体"}[ACK_NTF_LOGOUT]{lang="EN-US"}]{#struct_0_99677_28654_x1508799297}[报文定时器失败]{style="font-family:宋体"}

[[Failed to send user-rule result.]{lang="EN-US"}]{#struct_0_99677_28654_369809252}

[[向主控板发送添加用户规则的结果失败]{style="font-family:宋体"}]{#struct_0_99677_28654_383870706}

[[Failed to send user traffic info.]{lang="EN-US"}]{#struct_0_99677_28654_x1488789554}

[[向主控板发送用户流量信息失败]{style="font-family:宋体"}]{#struct_0_99677_28654_1422756066}

[[Failed to send mesh messages to all cards.]{lang="EN-US"}]{#struct_0_99677_28654_x2001778097}

[[向所有板发送]{style="font-family:宋体"}[Mesh]{lang="EN-US"}]{#struct_0_99677_28654_804064510}[消息失败]{style="font-family:宋体"}

[[Failed to send mesh messages to LPU.]{lang="EN-US"}]{#struct_0_99677_28654_1620049740}

[[向接口板发送]{style="font-family:宋体"}[Mesh]{lang="EN-US"}]{#struct_0_99677_28654_x1265545898}[消息失败]{style="font-family:宋体"}

[[Failed to send mesh messages to MPUs.]{lang="EN-US"}]{#struct_0_99677_28654_x1696553287}

[[向主控板发送]{style="font-family:宋体"}[Mesh]{lang="EN-US"}]{#struct_0_99677_28654_x963594631}[消息失败]{style="font-family:宋体"}

[[Failed to look up FIB info.]{lang="EN-US"}]{#struct_0_99677_28654_76704568}

[[查找快转信息失败]{style="font-family:宋体"}]{#struct_0_99677_28654_1455480866}

[[Packet validity check failed because packet length and version did not match.]{lang="EN-US"}]{#struct_0_99677_28654_x325376885}

[[报文长度和版本均不匹配，报文合法性检查失败]{style="font-family:宋体"}]{#struct_0_99677_28654_1740249033}

[[Packet validity check failed due to invalid authenticator.]{lang="EN-US"}]{#struct_0_99677_28654_1328569737}

[[authenticator]{lang="EN-US"}]{#struct_0_99677_28654_207441071}[字段非法，报文合法性检查失败]{style="font-family:宋体"}

[[Packet validity check failed due to failure of getting user access interface by user IP.]{lang="EN-US"}]{#struct_0_99677_28654_x1127864053}

[[无法通过用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_x220130024}[地址找到用户接入的接口，报文合法性检查失败]{style="font-family:宋体"}

[[Unknown source of packet.]{lang="EN-US"}]{#struct_0_99677_28654_76770104}

[[报文源未知]{style="font-family:宋体"}]{#struct_0_99677_28654_318841988}

[[Failed to receive ICMP packet.]{lang="EN-US"}]{#struct_0_99677_28654_x1492828369}

[[无法收到]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_99677_28654_x1613505631}[报文]{style="font-family:宋体"}

[[Failed to open ICMP socket.]{lang="EN-US"}]{#struct_0_99677_28654_x238332481}

[[无法打开]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_99677_28654_2135346032}[的套接字]{style="font-family:宋体"}

[[Failed to send ICMP6 packet.]{lang="EN-US"}]{#struct_0_99677_28654_414392002}

[[发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_99677_28654_76835640}[的报文失败]{style="font-family:宋体"}

[[Failed to get ARP refresh time.]{lang="EN-US"}]{#struct_0_99677_28654_676149592}

[[获取]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_99677_28654_x47940505}[更新时间失败]{style="font-family:宋体"}

[[Failed to send ARP request.]{lang="EN-US"}]{#struct_0_99677_28654_1405050963}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_99677_28654_922428400}[请求失败]{style="font-family:宋体"}

[[Failed to get ND refresh time.]{lang="EN-US"}]{#struct_0_99677_28654_1513979710}

[[获取]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_99677_28654_76901176}[更新时间失败]{style="font-family:宋体"}

[[Failed to find user while receiving accounting-update response.]{lang="EN-US"}]{#struct_0_99677_28654_184270022}

[[收到计费更新回应时查找用户信息失败]{style="font-family:宋体"}]{#struct_0_99677_28654_38617975}

[[Failed to create user because the user count  reached the upper limit.]{lang="EN-US"}]{#struct_0_99677_28654_2118874125}

[[用户数量达到最大值，创建用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_x1986541046}

[[Failed to create user for failing to get the physical info.]{lang="EN-US"}]{#struct_0_99677_28654_391158746}

[[获取用户物理信息失败，创建用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_76442424}

[[Failed to create user due to memory application failure.]{lang="EN-US"}]{#struct_0_99677_28654_x1387836901}

[[申请用户资源失败，导致创建用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_x1258590160}

[[Failed to find user for ACK_NTF_LOGOUT.]{lang="EN-US"}]{#struct_0_99677_28654_x1938489958}

[[找不到用户信息来发送]{style="font-family:宋体"}[ACK_NTF_LOGOUT]{lang="EN-US"}]{#struct_0_99677_28654_1100778337}[报文]{style="font-family:宋体"}

[[Failed to find user for AFF_NTF_USERIPCHAN.]{lang="EN-US"}]{#struct_0_99677_28654_1546176612}

[[找不到用户信息来发送]{style="font-family:宋体"}[AFF_NTF_USERIPCHAN]{lang="EN-US"}]{#struct_0_99677_28654_76507960}[报文]{style="font-family:宋体"}

[[ACL *acl-number* doesn\'t exist or ACL type is not supported.]{lang="EN-US"}]{#struct_0_99677_28654_584538343}

[[ACL *acl-number*]{lang="EN-US"}]{#struct_0_99677_28654_x1238843811}[不存在，或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的类型不支持]{style="font-family:宋体"}

[[Failed to set pam items for authentication.]{lang="EN-US"}]{#struct_0_99677_28654_1756633422}

[[设置用于认证的]{style="font-family:宋体"}[pam items]{lang="EN-US"}]{#struct_0_99677_28654_1516619515}[失败]{style="font-family:宋体"}

[[Failed to find user by MAC (*mac-addr*).]{lang="EN-US"}]{#struct_0_99677_28654_x814167405}

[[根据]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_99677_28654_751916536}[地址没有找到用户]{style="font-family:宋体"}

[[Failed to create PAM handle.]{lang="EN-US"}]{#struct_0_99677_28654_98912594}

[[创建]{style="font-family:宋体"}[PAM handle]{lang="EN-US"}]{#struct_0_99677_28654_x363828711}[失败]{style="font-family:宋体"}

[[Failed to create DHCP client: Not enough memory.]{lang="EN-US"}]{#struct_0_99677_28654_1284996335}

[[内存不足导致创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_99677_28654_1206738816}[租约表项失败]{style="font-family:宋体"}

[[Failed to create DHCP client.]{lang="EN-US"}]{#struct_0_99677_28654_1202255230}

[[创建]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_99677_28654_710765360}[租约表项失败]{style="font-family:宋体"}

[[Failed to create DHCPv6 client: Not enough memory.]{lang="EN-US"}]{#struct_0_99677_28654_1237226659}

[[因为内存不足，创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_99677_28654_x7532815}[表项失败]{style="font-family:宋体"}

[[Failed to create DHCPv6 client.]{lang="EN-US"}]{#struct_0_99677_28654_816488239}

[[创建]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_99677_28654_2032031628}[表项失败]{style="font-family:宋体"}

[[Failed to create the pre-auth user: Not enough memory.]{lang="EN-US"}]{#struct_0_99677_28654_1558551126}

[[内存不足，创建认证前用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_1155266599}

[[Failed to create the pre-auth user: The user already existed.]{lang="EN-US"}]{#struct_0_99677_28654_531458472}

[[用户已存在，创建认证前用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_x1573616756}

[[Failed to create the pre-auth user: All-zero MAC address.]{lang="EN-US"}]{#struct_0_99677_28654_x1818541866}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_99677_28654_x410817342}[地址为全]{style="font-family:宋体"}[0]{lang="EN-US"}[，创建认证前用户失败]{style="font-family:宋体"}

[[Failed to get author info for pre-auth user.]{lang="EN-US"}]{#struct_0_99677_28654_861358008}

[[无法获取认证前域中的授权信息，创建认证前用户失败]{style="font-family:宋体"}]{#struct_0_99677_28654_x814101869}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging portal event ]{lang="EN-US"}]{#struct_0_99677_28654_1790588192}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_307590768}[[字段]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_76573496}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_2141340874}

[[Portal server *server-name* turned to *newstate* state.]{lang="EN-US"}]{#struct_0_99677_28654_x2074134865}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_1727982324}[服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[状态变化为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_99677_28654_x1419568144}[：服务器可达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_99677_28654_x1798676753}[：服务器不可达]{style="font-family:宋体"}

[[Portal server *server-name* started detection.]{lang="EN-US"}]{#struct_0_99677_28654_336200627}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x1904539931}[服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[开启可达性探测功能]{style="font-family:宋体"}

[[Portal server *server-name* refreshed detection timer.]{lang="EN-US"}]{#struct_0_99677_28654_x1868139887}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_83035606}[服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[刷新探测定时器]{style="font-family:宋体"}

[[Portal server *server-name* refreshed detection action because status is down when configuration was changed.]{lang="EN-US"}]{#struct_0_99677_28654_475665649}

[[修改配置时，因为服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*]{#struct_0_99677_28654_76639032}[状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，所以服务器刷新了探测动作]{style="font-family:宋体"}

[[Portal server *server-name* stopped detection.]{lang="EN-US"}]{#struct_0_99677_28654_x1541693149}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_1229045650}[服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[停止探测]{style="font-family:宋体"}

[[Portal web-server *server-name* turned to *newstate* state.]{lang="EN-US"}]{#struct_0_99677_28654_1227216402}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x1312797972}[重定向服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[状态变化为]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[，]{style="font-family:宋体"}*[newstate]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_99677_28654_165161632}[：服务器可达]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_99677_28654_x601069270}[：服务器不可达]{lang="EN-US" style="font-family:宋体"}

[[Portal web-server *server-name* started detection.]{lang="EN-US"}]{#struct_0_99677_28654_x1004205585}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x735029361}[重定向服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[开启可达性探测功能]{style="font-family:宋体"}

[[Portal web-server *server-name* refreshed detection timer.]{lang="EN-US"}]{#struct_0_99677_28654_77228856}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x960313964}[重定向服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[刷新探测定时器]{style="font-family:宋体"}

[[Portal web-server *server-name* refreshed detection action for status is down when changing configuration.]{lang="EN-US"}]{#struct_0_99677_28654_x698450246}

[[修改配置时，因为重定向服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*]{#struct_0_99677_28654_x384621016}[状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，所以服务器刷新了探测动作]{style="font-family:宋体"}

[[Portal web-server *server-name* detecting stopped.]{lang="EN-US"}]{#struct_0_99677_28654_621001158}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x540118259}[重定向服务器]{style="font-family:宋体"}*[server-name]{lang="EN-US"}*[停止探测]{style="font-family:宋体"}

[[Stopped the auth_sm timer.]{lang="EN-US"}]{#struct_0_99677_28654_x1637370467}

[[关闭认证状态机定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_2114450402}

[[The number of failures of receiving ACK_NTF_LOGOUTpacket reached the upper limit.]{lang="EN-US"}]{#struct_0_99677_28654_77294392}

[[等待]{style="font-family:宋体"}[ACK_NTF_LOGOUT]{lang="EN-US"}]{#struct_0_99677_28654_108149964}[报文的次数达到最大值]{style="font-family:宋体"}

[[Started the auth_sm timer, timeout=*time sec*.]{lang="EN-US"}]{#struct_0_99677_28654_469845677}

[[打开认证状态机的定时器，定时器的值为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_99677_28654_x1941885592}[秒]{style="font-family:宋体"}

[[User(IP:*ip-addr*) was not online when DHCP relay client information is deleted.]{lang="EN-US"}]{#struct_0_99677_28654_2138766402}

[[当]{style="font-family:宋体"}[DHCP relay]{lang="EN-US"}]{#struct_0_99677_28654_x263839931}[用户表项被删除时，对应的用户不在线]{style="font-family:宋体"}

[[Received an event *event-id* from VLAN *vlan-id* on interface *interface-type interface-num*.]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_99677_28654_x1976372852}

[[接收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_76704567}[事件，事件]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[event-id]{lang="EN-US"}*[，]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[，]{style="font-family:宋体"}*[,]{lang="EN-US"}*[接口索引为]{style="font-family:宋体"}*[ifindex]{lang="EN-US"}*

[[Portal Web server host name *host-name*, port *port-num*.]{lang="EN-US"}]{#struct_0_99677_28654_x118497246}

[[根据]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_99677_28654_x21543108}[地址获取到]{style="font-family:宋体"}[Portal Web server]{lang="EN-US"}[的主机名为]{style="font-family:宋体"}*[ host-name]{lang="EN-US"}*[,]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}*[port-num]{lang="EN-US"}*

[[User-SM \[*ip-addr*\]]{lang="EN-US"}]{#struct_0_99677_28654_x790209014}

[[用户状态机]{style="font-family:宋体"}[\[]{lang="EN-US"}]{#struct_0_99677_28654_x410645488}[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[\]]{lang="EN-US"}

[[User-SM \[*ip-addr*\]: Received ICMP response successfully. ]{lang="EN-US"}]{#struct_0_99677_28654_x686804808}

[[接收]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_99677_28654_x1114302503}[回应报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Sent ICMP request successfully.]{lang="EN-US"}]{#struct_0_99677_28654_76770103}

[[发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_99677_28654_76835639}[请求报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Received ICMPv6 response successfully.]{lang="EN-US"}]{#struct_0_99677_28654_343601745}

[[接收]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_99677_28654_x2133938493}[回应报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Sent ICMPv6 request successfully.]{lang="EN-US"}]{#struct_0_99677_28654_550393807}

[[发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_99677_28654_366327475}[请求报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Sent ARP request successfully.]{lang="EN-US"}]{#struct_0_99677_28654_76901175}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_99677_28654_x1389708090}[请求报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Sent ND request successfully.]{lang="EN-US"}]{#struct_0_99677_28654_1189197385}

[[发送]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_99677_28654_1601361180}[请求报文成功]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: ARP entry refreshed.]{lang="EN-US"}]{#struct_0_99677_28654_213555359}

[[ARP]{lang="EN-US"}]{#struct_0_99677_28654_x1568047793}[表项已刷新]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: ND entry refreshed.]{lang="EN-US"}]{#struct_0_99677_28654_76442423}

[[ND]{lang="EN-US"}]{#struct_0_99677_28654_x196195813}[表项已刷新]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Number of detection attempts reached the upper limit.]{lang="EN-US"}]{#struct_0_99677_28654_1950057332}

[[探测次数到达最大值]{style="font-family:宋体"}]{#struct_0_99677_28654_509146325}

[[User-SM \[*ip-addr*\]: Detection timer timed out and sent packet again.]{lang="EN-US"}]{#struct_0_99677_28654_571271775}

[[探测定时器超时，重发探测报文]{style="font-family:宋体"}]{#struct_0_99677_28654_773220709}

[[User-SM \[*ip-addr*\]: Started detect idle timer, timeout=*time* sec.]{lang="EN-US"}]{#struct_0_99677_28654_76507959}

[[开启闲置探测定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_x172241534}

[[User-SM \[*ip-addr*\]: Started detect waiting-response timer, timeout=*time* sec.]{lang="EN-US"}]{#struct_0_99677_28654_x1194291905}

[[开启等待探测回应定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_45203147}

[[User-SM \[*ip-addr*\]: Stopped detect timer.]{lang="EN-US"}]{#struct_0_99677_28654_76573495}

[[关闭探测定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_185025738}

[[User-SM \[*ip-addr*\]: Started  detect function.]{lang="EN-US"}]{#struct_0_99677_28654_719975694}

[[开启探测功能]{style="font-family:宋体"}]{#struct_0_99677_28654_1332946836}

[[User-SM \[*ip-addr*\]: Started  idle-cut timer, timeout=*time* sec.]{lang="EN-US"}]{#struct_0_99677_28654_2002791101}

[[开启闲置切断定时器，定时器超时时长为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_99677_28654_76639031}[秒]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Stopped idle-cut timer.]{lang="EN-US"}]{#struct_0_99677_28654_796959011}

[[关闭闲置切断定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_x1241695836}

[[User-SM \[*ip-addr*\]: Idle-cut timer timed out and user will logoff.]{lang="EN-US"}]{#struct_0_99677_28654_x1939848301}

[[闲置切断定时器超时，用户被强制下线]{style="font-family:宋体"}]{#struct_0_99677_28654_212215649}

[[User-SM \[*ip-addr*\]: Started session-timeout timer, timeout= *time*(s).]{lang="EN-US"}]{#struct_0_99677_28654_77228855}

[[打开会话超时定时器，定时器超时时长为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_99677_28654_996001172}[秒]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Stopped session-timeout timer.]{lang="EN-US"}]{#struct_0_99677_28654_x1480202767}

[[关闭会话超时定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_x1800797665}

[[User-SM \[*ip-addr*\]: Session timer timeout and user will logoff.]{lang="EN-US"}]{#struct_0_99677_28654_77294391}

[[会话定时器超时，用户将被强制下线]{style="font-family:宋体"}]{#struct_0_99677_28654_1682128076}

[[User-SM \[*ip-addr*\]: Started user-sync timer, timeout=*time* sec.]{lang="EN-US"}]{#struct_0_99677_28654_1496044159}

[[开启用户同步定时器，定时器超时时长为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_99677_28654_x87020772}[秒]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Stopped user-sync timer.]{lang="EN-US"}]{#struct_0_99677_28654_76704566}

[[关闭用户同步定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_1837817890}

[[User-SM \[*ip-addr*\]: User-sync timer time out and user will logoff.]{lang="EN-US"}]{#struct_0_99677_28654_203011657}

[[用户同步定时器超时，用户将被强制下线]{style="font-family:宋体"}]{#struct_0_99677_28654_886382332}

[[User-SM \[*ip-addr*\]: Number of accounting-update attempts reached the upper limit.]{lang="EN-US"}]{#struct_0_99677_28654_1324338220}

[[计费更新的失败次数达到最大值]{style="font-family:宋体"}]{#struct_0_99677_28654_76770102}

[[User-SM \[*ip-addr*\]: open accounting-update timer, timeout=*time*(s)]{lang="EN-US"}]{#struct_0_99677_28654_701179012}

[[开启实时计费定时器，定时器超时时长为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_99677_28654_x814421288}[秒]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Close accounting-update timer.]{lang="EN-US"}]{#struct_0_99677_28654_x1325507062}

[[关闭实时计费定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_76835638}

[[User-SM \[*ip-addr*\]: Number of accounting-update attempts without responses reached the upper limit.]{lang="EN-US"}]{#struct_0_99677_28654_x1612713391}

[[实时计费更新报文无响应次数达到最大值]{style="font-family:宋体"}]{#struct_0_99677_28654_x1460441754}

[[User-SM \[*ip-addr*\]: Notified User-Detect-SM to start detection.]{lang="EN-US"}]{#struct_0_99677_28654_x268944037}

[[通知]{style="font-family:宋体"}[detect-sm]{lang="EN-US"}]{#struct_0_99677_28654_76901174}[模块开启探测]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notify User-Detect-SM to stop detection.]{lang="EN-US"}]{#struct_0_99677_28654_566607046}

[[通知]{style="font-family:宋体"}[detect-sm]{lang="EN-US"}]{#struct_0_99677_28654_x240631099}[模块停止探测]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Failed to find physical info for ack_info.]{lang="EN-US"}]{#struct_0_99677_28654_1477871154}

[[封装]{style="font-family:宋体"}[ACK_INFO]{lang="EN-US"}]{#struct_0_99677_28654_76442422}[报文时查找用户物理信息]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notified auth-sm to process the REQ_CHALLENGE packet.]{lang="EN-US"}]{#struct_0_99677_28654_1760119323}

[[通知认证状态机模块处理]{style="font-family:宋体"}[REQ_CHALLENGE]{lang="EN-US"}]{#struct_0_99677_28654_x2002967695}[报文]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notified auth-sm to process the REQ_AUTH packet.]{lang="EN-US"}]{#struct_0_99677_28654_76507958}

[[通知认证状态机模块处理]{style="font-family:宋体"}[REQ_AUTH]{lang="EN-US"}]{#struct_0_99677_28654_1784073602}[报文]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notified  auth-sm to process the REQ_LOGOUT packet.]{lang="EN-US"}]{#struct_0_99677_28654_x457309482}

[[通知认证状态机模块处理]{style="font-family:宋体"}[REQ_LOGOUT]{lang="EN-US"}]{#struct_0_99677_28654_x1641733523}[报文]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notified  auth-sm to process the ACK_NTF_LOGOUT packet.]{lang="EN-US"}]{#struct_0_99677_28654_76573494}

[[通知认证状态机模块处理]{style="font-family:宋体"}[ACK_NTF_LOGOUT]{lang="EN-US"}]{#struct_0_99677_28654_x1771289398}[报文]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Notified  auth-sm to process the AFF_NTF_USERIPCHAN packet.]{lang="EN-US"}]{#struct_0_99677_28654_1643621479}

[[通知认证状态机模块处理]{style="font-family:宋体"}[AFF_NTF_USERIPCHAN]{lang="EN-US"}]{#struct_0_99677_28654_76639030}[报文]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: The new ACL *acl-number* authorized  by policy server is the same as the old one.]{lang="EN-US"}]{#struct_0_99677_28654_x1159356125}

[[策略服务器授权给用户的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_99677_28654_1110417895}[号和之前授权过的相同]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AAA processed authentication request and returned *result-string*.]{lang="EN-US"}]{#struct_0_99677_28654_77228854}

[[AAA]{lang="EN-US"}]{#struct_0_99677_28654_x1342650988}[处理了认证请求并返回认证结果]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_99677_28654_x921020182}[：成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_x2092302228}[：处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[continue]{lang="EN-US"}]{#struct_0_99677_28654_77294390}[：继续]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_99677_28654_x274187060}[：失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[error]{lang="EN-US"}]{#struct_0_99677_28654_1046563069}[：错误]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AAA processed authorization request and returned *result-string*.]{lang="EN-US"}]{#struct_0_99677_28654_76704565}

[[AAA]{lang="EN-US"}]{#struct_0_99677_28654_263839778}[处理了授权请求并返回授权结果]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_99677_28654_x1268930003}[：成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_76770101}[：处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_99677_28654_x1255136124}[：失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[error]{lang="EN-US"}]{#struct_0_99677_28654_1864577763}[：错误]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AAA processed accounting-start request and returned *result-string*.]{lang="EN-US"}]{#struct_0_99677_28654_x17661088}

[[AAA]{lang="EN-US"}]{#struct_0_99677_28654_76835637}[处理了开始计费请求并返回计费结果]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_x2039680431}[：处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非]{lang="EN-US" style="font-family:宋体"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_467561009}[：成功]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AAA processed accounting-update request and returned *result-string*.]{lang="EN-US"}]{#struct_0_99677_28654_76901173}

[[AAA]{lang="EN-US"}]{#struct_0_99677_28654_x1007371066}[处理了实时计费请求并返回计费结果]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_99677_28654_1103010057}[：成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_76442421}[：处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[failed]{lang="EN-US"}]{#struct_0_99677_28654_186141211}[：失败]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AAA processed accounting-stop request and returned *result-string*.]{lang="EN-US"}]{#struct_0_99677_28654_x1283507075}

[[AAA]{lang="EN-US"}]{#struct_0_99677_28654_76507957}[处理了停止计费请求并返回计费结果]{style="font-family:宋体"}*[result-string]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_210095490}[：处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[非]{lang="EN-US" style="font-family:宋体"}[processing]{lang="EN-US"}]{#struct_0_99677_28654_x1929254772}[：成功]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: AUTH-SM logged out the user and notified USER-SM to do.\]  ]{lang="EN-US"}]{#struct_0_99677_28654_76573493}

[[认证状态机完成了用户下线处理，通知用户状态机继续处理]{style="font-family:宋体"}]{#struct_0_99677_28654_567362762}

[[User-SM \[*ip-addr*\]: Auth-SM notified]{lang="EN-US"}]{#struct_0_99677_28654_1678142413}

[[ User-SM that user-ip updated.]{lang="EN-US"}]{#struct_0_99677_28654_76639029}

[[认证状态机通知用户状态机，用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_833694856}[已更新]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Received authentication response, RespCode=*resp-code*.]{lang="EN-US"}]{#struct_0_99677_28654_97113257}

[[收到认证回应报文，回应代码为]{style="font-family:宋体"}*[resp-code]{lang="EN-US"}*]{#struct_0_99677_28654_77228853}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_99677_28654_2143012244}[：表示]{lang="EN-US" style="font-family:宋体"}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[26]{lang="EN-US"}]{#struct_0_99677_28654_x1819324893}[：表示失败]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Received authorization response, RespCode=*resp-code*.]{lang="EN-US"}]{#struct_0_99677_28654_77294389}

[[收到授权回应报文回应代码为]{style="font-family:宋体"}*[resp-code]{lang="EN-US"}*]{#struct_0_99677_28654_482592817}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_99677_28654_76704564}[：表示成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[26]{lang="EN-US"}]{#struct_0_99677_28654_x2074812382}[：表示失败]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Received accounting-start response.]{lang="EN-US"}]{#struct_0_99677_28654_759716020}

[[收到开始计费回应报文]{style="font-family:宋体"}]{#struct_0_99677_28654_76770100}

[[User-SM \[*ip-addr*\]: Received accounting-update response.]{lang="EN-US"}]{#struct_0_99677_28654_1083516036}

[[收到更新计费回应报文]{style="font-family:宋体"}]{#struct_0_99677_28654_x73768956}

[[User-SM \[*ip-addr*\]: Received accounting-stop response.]{lang="EN-US"}]{#struct_0_99677_28654_76835636}

[[收到停止计费回应报文]{style="font-family:宋体"}]{#struct_0_99677_28654_76901172}

[[User-SM \[*ip-addr*\]:  Detection failed and user logged off.]{lang="EN-US"}]{#struct_0_99677_28654_948944070}

[[用户探测失败，用户被强制下线]{style="font-family:宋体"}]{#struct_0_99677_28654_1193251990}

[[User-SM \[*ip-addr*\]: Received rule result *result*.]{lang="EN-US"}]{#struct_0_99677_28654_76442420}

[[接收到用户规则下发结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*]{#struct_0_99677_28654_2142456347}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_99677_28654_76507956}[：成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail]{lang="EN-US"}]{#struct_0_99677_28654_x2128556670}[：]{lang="EN-US" style="font-family:宋体"}[失败]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: User is logging off now.]{lang="EN-US"}]{#struct_0_99677_28654_x1597905311}

[[用户正在下线过程中]{style="font-family:宋体"}]{#struct_0_99677_28654_76573492}

[[User-SM \[*ip-addr*\]: Notified Auth-SM to log user out.]{lang="EN-US"}]{#struct_0_99677_28654_x1388952374}

[[通知认证状态机强制用户下线]{style="font-family:宋体"}]{#struct_0_99677_28654_76639028}

[[User-SM \[*ip-addr*\]: Received set-policy COA/POD notification.]{lang="EN-US"}]{#struct_0_99677_28654_77228852}

[[用户状态机接收到]{style="font-family:宋体"}[COA/POD]{lang="EN-US"}]{#struct_0_99677_28654_x195639916}[通知，其中，]{style="font-family:宋体"}[COA]{lang="EN-US"}[用于授权变更，]{style="font-family:宋体"}[POD]{lang="EN-US"}[用于强制用户下线]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Recover failed and user logged off.]{lang="EN-US"}]{#struct_0_99677_28654_1762462963}

[[获取用于恢复用户信息的数据失败，用户被强制下线]{style="font-family:宋体"}]{#struct_0_99677_28654_77294388}

[[User-SM \[*ip-addr*\]: Receiving last traffic when user is logging off..]{lang="EN-US"}]{#struct_0_99677_28654_x1473722319}

[[用户下线时，最后一次接收到流量更新消息]{style="font-family:宋体"}]{#struct_0_99677_28654_76704563}

[[User-SM \[*ip-addr*\]: User IP changed.]{lang="EN-US"}]{#struct_0_99677_28654_646176802}

[[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_76770099}[变更]{style="font-family:宋体"}

[[Received DHCP event: operation=*event*, IP=*ip-addr*, MAC=*mac-addr*, interface=*ifname*.]{lang="EN-US"}]{#struct_0_99677_28654_617764344}

[[收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_99677_28654_x1053455629}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，]{style="font-family:宋体"}*[event]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Add]{lang="EN-US"}]{#struct_0_99677_28654_1592412167}[：]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约添加事件]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Del]{lang="EN-US"}]{#struct_0_99677_28654_1068103038}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Get]{lang="EN-US"}]{#struct_0_99677_28654_x394808963}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约获取事件]{style="font-family:宋体"}

[[BUTT]{lang="EN-US"}]{#struct_0_99677_28654_1424398934}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约平滑结束事件]{style="font-family:宋体"}

[[USER: Received a message for adding DHCP client (MAC=*mac-addr*, IP=*ip-addr*, Interface=*ifname*, VPN instance=*vpn-instance*).]{lang="EN-US"}]{#struct_0_99677_28654_1021114407}

[[收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_99677_28654_x1707768948}[租约创建消息（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[mac-addr]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[，接入接口为]{style="font-family:宋体"}*[ifname]{lang="EN-US"}*[，所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例为]{style="font-family:宋体"}*[vpn-instance]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[User-SM\[*ip-addr*\]: Added ARP rule. ]{lang="EN-US"}]{#struct_0_99677_28654_x2111053475}

[[为用户添加对应的]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_99677_28654_x544969534}[规则]{style="font-family:宋体"}

[[User-SM\[*ip-addr*\]: Started User-SM timer (*interval* sec). ]{lang="EN-US"}]{#struct_0_99677_28654_x948254061}

[[开启用户状态机定时器，超时时间为]{style="font-family:宋体"}*[interval]{lang="EN-US"}*]{#struct_0_99677_28654_617829880}[秒]{style="font-family:宋体"}

[[User-SM\[*ip-addr*\]: Received deployment results of all rules. ]{lang="EN-US"}]{#struct_0_99677_28654_x497915367}

[[收到所有用户规则下发的结果]{style="font-family:宋体"}]{#struct_0_99677_28654_x141619471}

[[User-SM\[*ip-addr*\]: Stopped User-SM timer. ]{lang="EN-US"}]{#struct_0_99677_28654_1424464470}

[[关闭用户状态机定时器]{style="font-family:宋体"}]{#struct_0_99677_28654_1021179943}

[[User-SM\[*ip-addr*\]: Entered state: *vsrp-state*.]{lang="EN-US"}]{#struct_0_99677_28654_x841724616}

[[用户进入]{style="font-family:宋体"}[VRSP]{lang="EN-US"}]{#struct_0_99677_28654_x1707703412}[状态]{style="font-family:宋体"}*[vsrp-state]{lang="EN-US"}*[，状态取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[vsrp_master]{lang="EN-US"}]{#struct_0_99677_28654_x2110987939}[：开始为]{lang="EN-US" style="font-family:宋体"}[VRSP]{lang="EN-US"}[双机主用户授权]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[vsrp_master_ok]{lang="EN-US"}]{#struct_0_99677_28654_1495184860}[：]{lang="EN-US" style="font-family:宋体"}[VRSP]{lang="EN-US"}[主用户授权完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[vsrp_backup]{lang="EN-US"}]{#struct_0_99677_28654_x544903998}[：开始为]{lang="EN-US" style="font-family:宋体"}[VRSP]{lang="EN-US"}[备用户授权]{lang="EN-US" style="font-family:宋体"}

[[vsrp_backup_ok]{lang="EN-US"}]{#struct_0_99677_28654_x948188525}[：]{style="font-family:宋体"}[VRSP]{lang="EN-US"}[备用户授权完成]{style="font-family:宋体"}

[[Created pre-auth user for VSRP backup.]{lang="EN-US"}]{#struct_0_99677_28654_x1770146399}

[[在]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_99677_28654_617895416}[备份设备上创建认证前用户]{style="font-family:宋体"}

[[Can\'t create pre-auth user: Portal was disabled.]{lang="EN-US"}]{#struct_0_99677_28654_1458498199}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x497849831}[未使能，不创建认证前用户]{style="font-family:宋体"}

[[Can\'t create pre-auth user: No pre-auth domain configured.]{lang="EN-US"}]{#struct_0_99677_28654_x1227551433}

[[接口未配置认证前域，不创建认证前用户]{style="font-family:宋体"}]{#struct_0_99677_28654_1068234110}

[[Inappropriate state. Dropped batch-user-backup message.]{lang="EN-US"}]{#struct_0_99677_28654_371926649}

[[本机未处于]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_99677_28654_x141553935}[双机稳态，丢弃批量备份用户数据的消息]{style="font-family:宋体"}

[[Port and user not in the same VLAN.]{lang="EN-US"}]{#struct_0_99677_28654_1441832083}

[[接口所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_1424530006}[与用户所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Deauthorized pre-auth user: User coming online.]{lang="EN-US"}]{#struct_0_99677_28654_x584436931}

[[用户认证上线，取消认证前域下发的授权]{style="font-family:宋体"}]{#struct_0_99677_28654_1021245479}

[[Can\'t create pre-auth user when user was offline because of unavailable port.]{lang="EN-US"}]{#struct_0_99677_28654_x413346222}

[[端口不可用，强制用户下线，且不创建认证前用户]{style="font-family:宋体"}]{#struct_0_99677_28654_x1707637876}

[[Can\'t create pre-auth user: Unsupported portal-auth type.]{lang="EN-US"}]{#struct_0_99677_28654_x268822272}

[[Layer3]{lang="EN-US"}]{#struct_0_99677_28654_x2110922403}[方式的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证不支持认证前域，不创建认证前用户]{style="font-family:宋体"}

[[Can\'t create pre-auth user: Interface was not operating correctly.]{lang="EN-US"}]{#struct_0_99677_28654_x538512351}

[[接口工作状态不正常，不创建认证前用户]{style="font-family:宋体"}]{#struct_0_99677_28654_x544838462}

[[Can\'t create pre-auth user: VSRP was down on the interface.]{lang="EN-US"}]{#struct_0_99677_28654_48936615}

[[VSRP]{lang="EN-US"}]{#struct_0_99677_28654_x948122989}[状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，不创建认证前用户]{style="font-family:宋体"}

**[ ]{lang="EN-US"}**

[[表1-3 ]{lang="EN-US"}[debugging portal fsm ]{lang="EN-US"}]{#struct_0_99677_28654_1484000017}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_323142646}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_99677_28654_x2036566159}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_1396629255}

[[AUTH_SM \[*ip-addr*\]: Entered *state* state.]{lang="EN-US"}]{#struct_0_99677_28654_1056259827}

[[认证状态机（用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_1379947918}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[）进入状态]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticating]{lang="EN-US"}]{#struct_0_99677_28654_1702787816}[：正在认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticated]{lang="EN-US"}]{#struct_0_99677_28654_1463845208}[：认证成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Continue]{lang="EN-US"}]{#struct_0_99677_28654_76835635}[：认证持续]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssigningNewIP]{lang="EN-US"}]{#struct_0_99677_28654_x1657343407}[：等待分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedNewIP]{lang="EN-US"}]{#struct_0_99677_28654_1965115832}[：分配到]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_99677_28654_x554853709}[：在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting]{lang="EN-US"}]{#struct_0_99677_28654_x934832837}[：强制下线状态，等待]{style="font-family:宋体"}[NTF_LOGOUT]{lang="EN-US"}[响应]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_99677_28654_937282638}[：下线处理状态]{style="font-family:宋体"}

[[Auth-SM: Started to run.]{lang="EN-US"}]{#struct_0_99677_28654_1733758769}

[[认证状态机开始运转]{style="font-family:宋体"}]{#struct_0_99677_28654_x723601013}

[[User_Detect_SM \[*ip-addr*\]: Entered *state* state.]{lang="EN-US"}]{#struct_0_99677_28654_x1979877835}

[[用户探测状态机（用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_99677_28654_x1094963264}[地址为]{style="font-family:宋体"}*[ip-addr]{lang="EN-US"}*[）进入状态]{style="font-family:宋体"}*[state]{lang="EN-US"}*[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detected]{lang="EN-US"}]{#struct_0_99677_28654_76901171}[：已探测状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Wait_Detect]{lang="EN-US"}]{#struct_0_99677_28654_x625034042}[：等待探测状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Detecting]{lang="EN-US"}]{#struct_0_99677_28654_2035363331}[：正在探测状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DetectFail]{lang="EN-US"}]{#struct_0_99677_28654_x1739686765}[：探测失败状态]{style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: State changed from *old-state* to *new-state*.]{lang="EN-US"}]{#struct_0_99677_28654_x870173177}

[[用户状态机状态发生变化（旧状态]{style="font-family:宋体"}*[old-state]{lang="EN-US"}*[ -\> ]{lang="EN-US"}]{#struct_0_99677_28654_1174697618}[新状态]{style="font-family:宋体"}*[new-state]{lang="EN-US"}*[），状态包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticating]{lang="EN-US"}]{#struct_0_99677_28654_1356037067}[：正在认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting_Author]{lang="EN-US"}]{#struct_0_99677_28654_x1288506150}[：等待授权结果]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting_Rule_OK]{lang="EN-US"}]{#struct_0_99677_28654_76442419}[：等待规则下发结果]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_99677_28654_x1746491412}[：在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline_Waiting_Traffic]{lang="EN-US"}]{#struct_0_99677_28654_828361037}[：下线等待各板流量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline_Waiting_Acctoff]{lang="EN-US"}]{#struct_0_99677_28654_195858624}[：等待停止计费回应]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Done]{lang="EN-US"}]{#struct_0_99677_28654_x1969329976}[：用户下线完成]{lang="EN-US" style="font-family:宋体"}

[[User-SM \[*ip-addr*\]: Begin to run.]{lang="EN-US"}]{#struct_0_99677_28654_1593942451}

[[用户状态机开始运转]{style="font-family:宋体"}]{#struct_0_99677_28654_x815108526}

[[User-SM \[*ip-addr*\]: User deleted]{lang="EN-US"}]{#struct_0_99677_28654_1355904752}

[[用户被删除]{style="font-family:宋体"}]{#struct_0_99677_28654_76507955}

**[ ]{lang="EN-US"}**

[[【举例】]{style="font-family:黑体"}]{#struct_0_99677_28654_592432514}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_x1552104142}[在一台配置了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[的设备上打开]{style="font-family:宋体"}[Portal]{lang="EN-US"}[状态机调试信息开关，当有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户上线时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal fsm]{lang="EN-US"}]{#struct_0_99677_28654_x133017764}

[\*Jan  7 00:06:44:214 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x240942116}*[用户状态机开始运转，用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[197.197.197.1]{lang="EN-US"}*

[[\*Jan  7 00:06:44:214 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_x85776258}

[User-SM\[197.197.197.1\]: State changed from Initial to Authenticating.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1999304322}*[用户状态机从]{style="font-family:宋体"}[Initial]{lang="EN-US"}[切换为]{style="font-family:宋体"}[Authenticating]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:06:44:219 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_840121604}

[Auth-SM: Started to run.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1114908391}*[认证状态机开始运转]{style="font-family:宋体"}*

[[\*Jan  7 00:06:44:220 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_x898062113}

[Auth_SM\[197.197.197.1\]: Entered state Authenticating.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_2079669258}*[认证状态机进入]{style="font-family:宋体"}[Authenticating]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}]{#struct_0_99677_28654_76573491}

[\*Jan  7 00:06:44:645 2011 Sysname PORTAL/7/FSM]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[用户状态机不变]{style="font-size:10.5pt;
font-family:宋体"}*

[Auth-SM: Started to run.]{lang="EN-US"}

[\*Jan  7 00:06:44:645 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[Auth_SM\[197.197.197.1\]: Entered state Authenticated.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_949699786}*[用户状态机进入]{style="font-family:宋体"}[Authenticated]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:06:44:646 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_716893243}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[\*Jan  7 00:06:44:646 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Authenticating to Waiting_Author.]{lang="EN-US"}

[\*Jan  7 00:06:44:657 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Waiting_Author to Waiting_Rule_OK.]{lang="EN-US"}

[*[//  ]{lang="EN-US"}*]{#struct_0_99677_28654_196355176}*[用户状态机首先切换为]{style="font-family:宋体"}[Waiting_Author]{lang="EN-US"}[，然后切换为]{style="font-family:宋体"}[Waiting_Rule_OK]{lang="EN-US"}*

[[\*Jan  7 00:06:44:667 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_709937086}

[Auth-SM: Started to run.]{lang="EN-US"}

[\*Jan  7 00:06:44:668 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[Auth_SM\[197.197.197.1\]: Entered state Online.]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[认证状态机进入]{style="font-size:10.5pt;
font-family:宋体"}[Online]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[状态]{style="font-size:
10.5pt;font-family:宋体"}*

[\*Jan  7 00:06:44:670 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[\*Jan  7 00:06:44:671 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Waiting_Rule_OK to Online.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1576386872}*[用户状态机切换为]{style="font-family:宋体"}[Online]{lang="EN-US"}*

[[\*Jan  7 00:21:31:710 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_307317313}

[User-Detect-SM\[197.197.197.1\]: Entered state Initial.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1339597060}*[用户状态机进入]{style="font-family:宋体"}[Iintial]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[User-Detect-SM\[197.197.197.1\]: Entered state Detected.]{lang="EN-US"}]{#struct_0_99677_28654_76639027}

[\*Jan  7 00:21:32:469 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1549587320}*[用户探测状态机进入]{style="font-family:宋体"}[Detected]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:35:16:169 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_1469038326}

[Auth-SM: Started to run.]{lang="EN-US"}

[\*Jan  7 00:35:16:170 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[Auth_SM\[197.197.197.1\]: Entered state Offline.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1811763466}*[认证状态机进入]{style="font-family:宋体"}[Offline]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:35:16:171 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_x1529515768}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[\*Jan  7 00:35:16:172 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Online to Offline_Waiting_Traffic.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1514618599}*[用户状态机切换为]{style="font-family:宋体"}[Offline_Waiting_Traffic]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:35:16:180 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_x42489405}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[\*Jan  7 00:35:16:181 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Offline_Waiting_Traffic to Offline_Waiting_Acctoff.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1373384555}*[用户状态机切换为]{style="font-family:宋体"}[Offline_Waiting_Accoff]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:35:16:758 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_1345456019}

[User-SM\[197.197.197.1\]: Begin to run.]{lang="EN-US"}

[\*Jan  7 00:35:16:759 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: State changed from Offline_Waiting_Acctoff to Done.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_665225135}*[用户状态机切换为]{style="font-family:宋体"}[Done]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Jan  7 00:35:16:759 2011 Sysname PORTAL/7/FSM:]{lang="EN-US"}]{#struct_0_99677_28654_33198769}

[User-SM\[197.197.197.1\]: User deleted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_77228851}*[用户被删除]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_1760675220}[在一台配置了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[的设备上打开]{style="font-family:宋体"}[Portal]{lang="EN-US"}[事件调试信息开关，当有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户上线时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal event]{lang="EN-US"}]{#struct_0_99677_28654_x1670473074}

[\*Jan  7 00:38:37:954 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}

[Auth-SM\[197.197.197.1\]: Started the auth_sm timer, timeout=15 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x129508331}*[开启认证状态机定时器，时长为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:38:37:955 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x452155888}

[User-SM\[197.197.197.1\]: Notified Auth-SM to process the REQ_CHALLENGE packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x2106610953}*[通知协议状态机处理]{style="font-family:宋体"}[REQ_CHALLENGE]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan  7 00:38:37:963 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1187396311}

[User-SM\[197.197.197.1\]: Notified Auth-SM to process the REQ_AUTH packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1804427468}*[通知协议状态机处理]{style="font-family:宋体"}[REQ_AUTH]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan  7 00:38:37:965 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_843153717}

[User-SM\[197.197.197.1\]: AAA processed authentication request and returned processing.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_99677_28654_x965947253}*[处理认证请求，并返回结果为正在处理]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:425 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x1784131101}

[User-SM\[197.197.197.1\]: Received authentication response, RespCode=0.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_656510319}*[收到]{style="font-family:宋体"}[AAA]{lang="EN-US"}[的认证回应消息，响应码为]{style="font-family:宋体"}[0]{lang="EN-US"}*

[[\*Jan  7 00:38:38:436 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_77294387}

[User-SM\[197.197.197.1\]: AAA processed authorization request and returned success.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_99677_28654_x1429092303}*[处理授权请求，返回结果为成功]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:448 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x134995205}

[User-SM\[197.197.197.1\]: Started User-SM timer, timeout=600 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x363357199}*[开启用户状态机定时器，时长为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:451 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x1107799767}

[User-SM\[197.197.197.1\]: Received rule result success.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1403738084}*[收到规则下发成功的消息]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:452 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_248032463}

[User-SM\[197.197.197.1\]: Stopped User-SM timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1400554309}*[关闭用户状态机定时器]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:453 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_749462366}

[User-SM\[197.197.197.1\]: AAA processed accounting-start request and returned proc]{lang="EN-US"}

[essing.]{lang="EN-US"}

[*[// AAA]{lang="EN-US"}*]{#struct_0_99677_28654_45998126}*[处理开始计费请求，并返回结果为正在处理]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:455 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x759472369}

[User-SM\[197.197.197.1\]: Started session-timeout timer, timeout=900902 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1395652264}*[开启会话超时定时器，时长为]{style="font-family:宋体"}[900902]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:456 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x607418616}

[User-SM\[197.197.197.1\]: Started idle-cut timer, timeout=600 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x179530182}*[开启]{style="font-family:宋体"}[Idle-cut]{lang="EN-US"}[定时器，时长为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:457 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1642788509}

[User-SM\[197.197.197.1\]: Notify User-Detect-SM detecting started.]{lang="EN-US"}

[\*Jan  7 00:38:38:458 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}

[User-Detect-SM\[197.197.197.1\]: Start detect function.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_635496524}*[通知用户探测状态机开启探测]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:458 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x763772624}

[User-Detect-SM\[197.197.197.1\]: Started detect idle timer, length=60(sec).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_548997786}*[开启探测闲置定时器，时长为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:546 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_743162674}

[User-SM\[197.197.197.1\]: Received accounting-start response.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1378423093}*[收到开始计费回应消息]{style="font-family:宋体"}*

[[\*Jan  7 00:38:38:549 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x610031323}

[User-SM\[197.197.197.1\]: Started accounting-update timer, timeout=720 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x439788257}*[开启实时计费定时器，时长为]{style="font-family:宋体"}[720]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:39:38:686 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x1204320373}

[User-Detect-SM\[197.197.197.1\]: Stopped detect timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1336816091}*[关闭探测定时器]{style="font-family:宋体"}*

[[\*Jan  7 00:39:39:687 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x242210076}

[User-Detect-SM\[197.197.197.1\]: Sent ICMP request successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x986967899}*[发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[请求报文成功]{style="font-family:宋体"}*

[[\*Jan  7 00:58:49:689 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1642854045}

[User-Detect-SM\[197.197.197.1\]: Started detect waiting-response timer, timeout=3 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_705785957}*[开启等待探测回应定时器，时长为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 00:58:52:687 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_590560465}

[User-Detect-SM\[197.197.197.1\]: ARP entry refreshed.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_240576027}*[用户]{style="font-family:宋体"}[ARP]{lang="EN-US"}[表项刷新]{style="font-family:宋体"}*

[[User-Detect-SM\[197.197.197.1\]: Stopped detect timer.]{lang="EN-US"}]{#struct_0_99677_28654_872159055}

[\*Jan  7 00:58:52:689 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_521882912}*[关闭探测定时器]{style="font-family:宋体"}*

[[\*Jan  7 01:00:36:547 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1984373496}

[User-SM\[197.197.197.1\]: Notified Auth-SM to process the REQ_LOGOUT packet.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_865207027}*[通知认证状态机处理]{style="font-family:宋体"}[REQ_LOGOUT]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jan  7 01:00:36:549 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_427769502}

[User-SM\[197.197.197.1\]: Auth-SM logged out the user and notified User-SM to proce.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_934575773}*[认证状态机处理完成，通知用户状态机处理]{style="font-family:宋体"}*

[[\*Jan  7 01:00:36:556 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x2090853767}

[User-SM\[197.197.197.1\]: Started User-SM timer, timeout=60 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_380717604}*[开启用户状态机定时器，时长为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 01:00:36:562 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1642919581}

[User-SM\[197.197.197.1\]: Receiving last traffic when offline.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x908370903}*[获取用户的流量信息]{style="font-family:宋体"}*

[[\*Jan  7 01:00:36:562 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_714273025}

[User-SM\[197.197.197.1\]: Stopped User-SM timer.]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[关闭用户状态机定时器]{style="font-size:10.5pt;
font-family:宋体"}*

[\*Jan  7 01:00:36:563 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: AAA processed accounting-stop request and returned processing.]{lang="EN-US"}

*[// AAA]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[处理停止计费请求，并返回结果为正在处理]{style="font-size:
10.5pt;font-family:宋体"}*

[\*Jan  7 01:00:36:563 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}

[User-SM\[197.197.197.1\]: Started User-SM timer, timeout=60 sec.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x670750328}*[开启用户状态机定时器，时长为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:169 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1445724831}

[User-SM\[197.197.197.1\]: Received accounting-stop response.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_359624972}*[收到计费停止响应报文]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:170 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x268093833}

[User-SM\[197.197.197.1\]: Stopped User-SM timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_972914226}*[关闭用户状态机定时器]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:172 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x2041955580}

[User-SM\[197.197.197.1\]: Stopped session-timeout timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1635445940}*[关闭会话超时定时器]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:172 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1043647883}

[User-SM\[197.197.197.1\]: Stopped idle-cut timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1642985117}*[关闭]{style="font-family:宋体"}[Idle-cut]{lang="EN-US"}[定时器]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:173 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_1447617756}

[User-SM\[197.197.197.1\]: Notify User-Detect-SM detecting stopped.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_239926408}*[通知用户探测状态机关闭探测功能]{style="font-family:宋体"}*

[[\*Jan  7 01:00:37:174 2011 Sysname PORTAL/7/EVENT:]{lang="EN-US"}]{#struct_0_99677_28654_x1117512098}

[User-Detect-SM\[197.197.197.1\]: Stopped detect timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1427543314}*[关闭探测定时器]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_x948057453}[在一台指定了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前域的设备上打开]{style="font-family:宋体"}[Portal]{lang="EN-US"}[事件调试信息开关，当有用户申请地址时，因为指定的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前域不存在，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal event]{lang="EN-US"}]{#struct_0_99677_28654_x951662242}

[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}

[Received DHCP event: operation=Add, IP=0x12120001, MAC=1cbd-b9e3-b0ed, interface=GigabitEthernet1/0/3.]{lang="EN-US"}

[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}

[USER: Received a message for adding DHCP client (MAC=1cbd-b9e3-b0ed, IP=18.18.0.1, Interface=GigabitEthernet1/0/3, VPN instance=).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_478874009}*[收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[上报的租约创建事件]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/ERROR: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_618026488}

[Failed to find user by MAC (1cbd-b9e3-b0ed).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1707201505}*[根据上报租约的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址找不到用户]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:933 2014 Sysname PORTAL/7/ERROR: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_2088400287}

[Failed to get author info for pre-auth user.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1267045523}*[获取认证前域授权信息失败，创建认证前用户失败]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_1853317097}[在一台配置了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证前域的设备上打开]{style="font-family:宋体"}[Portal]{lang="EN-US"}[事件调试信息开关，当有用户申请地址时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal event]{lang="EN-US"}]{#struct_0_99677_28654_x174918416}

[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}

[Received DHCP event: operation=Add, IP=0x12120001, MAC=1cbd-b9e3-b0ed, interface=GigabitEthernet1/0/3.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_639786509}*[收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[上报的租约创建事件]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x149513734}

[USER: Received a message for adding DHCP client (MAC=1cbd-b9e3-b0ed, IP=18.18.0.1, Interface=GigabitEthernet1/0/3, VPN instance=). ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x295461741}*[收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[上报的租约创建事件]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/ERROR: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_564638094}

[Failed to find user by MAC (1cbd-b9e3-b0ed). ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_53883632}*[根据租约找不到对应用户]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:923 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x497718759}

[User-SM\[18.18.0.1\]: Added ARP rule.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_770212205}*[添加]{style="font-family:宋体"}[ARP]{lang="EN-US"}[规则]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:924 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x2085936879}

[User-SM\[18.18.0.1\]: Added user rule.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1253693108}*[添加认证前用户规则]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:933 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x851261698}

[User-SM\[18.18.0.1\]: Started User-SM timer (600 sec). ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1649312445}*[开启规则等待定时器]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:944 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1310235648}

[User-SM\[18.18.0.1\]: Received deployment results of all rules.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1154456772}*[收到规则下发结果]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:945 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x818712247}

[User-SM\[18.18.0.1\]: Stopped User-SM timer.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1116531078}*[停止规则等待定时器]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:945 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1068365182}

[User-SM\[18.18.0.1\]: Entered state vsrp_master.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1200645394}*[进入授权下发状态]{style="font-family:宋体"}*

[[\*Sep 24 06:29:31:946 2014 Sysname PORTAL/7/EVENT: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x2115608858}

[User-SM\[18.18.0.1\]: Entered state vsrp_master_ok.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1292258287}*[授权下发完成]{style="font-family:宋体"}*

::: {#1148771241 .myid}
[]{#_Toc404792589}[]{#struct_0_99677_28654_529517005}

**Portal \-- Portal调试命令 \-- debugging portal interface**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_99677_28654_189286279}

[**[debugging portal]{lang="EN-US"}**[ { **all** \| **packet** \[ **acl** *acl-number* \] \| **rule** } **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_99677_28654_564686454}

[**[undo debugging portal]{lang="EN-US"}**[ { **all** \| **packet** \[ **acl** *acl-number* \] \| **rule** } **interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_99677_28654_52584185}

[[【视图】]{style="font-family:黑体"}]{#struct_0_99677_28654_x1176192596}

[[用户视图]{style="font-family:宋体"}]{#struct_0_99677_28654_1905966857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_99677_28654_689376254}

[[network-admin]{lang="EN-US"}]{#struct_0_99677_28654_2113360103}

[[mdc-admin]{lang="EN-US"}]{#struct_0_99677_28654_x742262783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_99677_28654_1642526365}

[**[all]{lang="EN-US"}**]{#struct_0_99677_28654_x2033940594}[：表示所有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_99677_28654_1777504399}[：表示]{style="font-family:宋体"}[Portal]{lang="EN-US"}[协议报文调试信息开关。]{style="font-family:宋体"}

[**[rule]{lang="EN-US"}**]{#struct_0_99677_28654_466093782}[：表示]{style="font-family:宋体"}[Portal ]{lang="EN-US"}[规则调试信息开关。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_99677_28654_x1424331330}[：]{style="font-family:宋体"}[表示仅输出与指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[permit]{lang="EN-US"}[规则匹配的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[协议报文的调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_99677_28654_1267129029}[：表示指定接口的调试信息开关。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_99677_28654_x1866390674}

[**[debugging portal interface]{lang="EN-US"}**]{#struct_0_99677_28654_1563779345}[命令用来打开指定接口的]{style="font-family:
宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}**[undo debugging portal interface]{lang="EN-US"}**[命令用来关闭指定接口的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，接口上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x1177410775}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging portal packet interface]{lang="EN-US"}]{#struct_0_99677_28654_x1932796705}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_325296786}[[字段]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_96694163}
:::

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_1909719189}

[[Portal received *pkt-num* bytes of packet \[Type: *type-name*(*type-num*) ErrCode: *err-code*, IP: *user-ip*\]]{lang="EN-US"}]{#struct_0_99677_28654_x1620361996}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_170159980}[接收到报文，字节数为]{style="font-family:宋体"}*[pkt-num]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type-name]{lang="EN-US"}*[（类型代码为]{style="font-family:宋体"}*[type-num]{lang="EN-US"}*[），错误码为]{style="font-family:宋体"}*[err-code]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[user-ip]{lang="EN-US"}

[[Portal sent *pkt-num* bytes of packet \[Type: *type-name*(*type-num*), ErrCode: *err-code*, IP: *user-ip*\]]{lang="EN-US"}]{#struct_0_99677_28654_1642591901}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_x2044479539}[发送报文，字节数为]{style="font-family:宋体"}*[pkt-num]{lang="EN-US"}*[，报文类型为]{style="font-family:宋体"}*[type-name]{lang="EN-US"}*[（类型代码为]{style="font-family:宋体"}*[type-num]{lang="EN-US"}*[），错误码为]{style="font-family:宋体"}*[err-code]{lang="EN-US"}*[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[user-ip]{lang="EN-US"}*

[[\[ *attr-type-code attr-type-name* \] \[ a*ttr-length* \] \[ *attr-data* \]]{lang="EN-US"}]{#struct_0_99677_28654_1612360970}

[[Portal]{lang="EN-US"}]{#struct_0_99677_28654_1420363080}[协议属性列表信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-type-code]{lang="EN-US"}*]{#struct_0_99677_28654_x1512205876}[：属性类型编号]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-type-name]{lang="EN-US"}*]{#struct_0_99677_28654_185445670}[：属性类型名称]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-length]{lang="EN-US"}*]{#struct_0_99677_28654_454125803}[：属性值长度]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[attr-data]{lang="EN-US"}*]{#struct_0_99677_28654_x461777943}[：属性值内容]{lang="EN-US" style="font-family:宋体"}

**[ ]{lang="EN-US"}**

[[表1-5 ]{lang="EN-US"}[debugging portal rule interface]{lang="EN-US"}]{#struct_0_99677_28654_1457607072}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_320296930}[[字段]{style="font-family:黑体;
   color:black"}]{#struct_0_99677_28654_x426707829}

[[描述]{style="font-family:黑体;color:black"}]{#struct_0_99677_28654_x272724766}

[[L3 Interface = *interface-name*, L2 Interface= *port-name*, VLAN= *src-vlan-id*, SrcMac = *src-mac*, SrcIP = *src-ip*, DstIP = *dst-ip,* Protocol = *protocol-name*, SrcPort = *src-port-num*, DstPort = *dst-port-num*, VPN Instance = *vpn-index*]{lang="EN-US"}]{#struct_0_99677_28654_1642657437}

[[符合匹配规则的报文信息]{style="font-family:宋体"}]{#struct_0_99677_28654_1507064971}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3 Interface]{lang="EN-US"}]{#struct_0_99677_28654_2075981404}[：用户接入的三层接口名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2 Interface]{lang="EN-US"}]{#struct_0_99677_28654_x750144862}[：用户接入的二层端口名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_x12640361}[：用户]{lang="EN-US" style="font-family:宋体"}[接入的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcM]{lang="EN-US"}]{#struct_0_99677_28654_506355496}[ac]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[报文的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstMac: ]{lang="EN-US"}]{#struct_0_99677_28654_x1892674149}[报文的目的]{style="font-family:宋体"}[mac]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIP]{lang="EN-US"}]{#struct_0_99677_28654_306811868}[：]{lang="EN-US" style="font-family:宋体"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstIP]{lang="EN-US"}]{#struct_0_99677_28654_x1495226805}[：]{lang="EN-US" style="font-family:宋体"}[报文的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protocol]{lang="EN-US"}]{#struct_0_99677_28654_1642722973}[：报文的传输层协议类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcPort]{lang="EN-US"}]{#struct_0_99677_28654_x1619895753}[：]{lang="EN-US" style="font-family:宋体"}[报文的源端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstPort]{lang="EN-US"}]{#struct_0_99677_28654_1628248009}[：]{lang="EN-US" style="font-family:宋体"}[报文的目的端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Vpn Instance]{lang="EN-US"}]{#struct_0_99677_28654_509729017}[：]{lang="EN-US" style="font-family:宋体"}[报文所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引]{style="font-family:宋体"}

[[DRV_FREE_RULE:]{lang="EN-US"}]{#struct_0_99677_28654_x1751824412}

[[Interface= *interface-name*]{lang="EN-US"}]{#struct_0_99677_28654_x1153274332}

[[VLAN             = *vlan-id*]{lang="EN-US"}]{#struct_0_99677_28654_2070491996}

[[SrcMAC           = *src-mac*]{lang="EN-US"}]{#struct_0_99677_28654_x2027506584}

[[SrcIP            = *src-ip*]{lang="EN-US"}]{#struct_0_99677_28654_x2135110585}

[[SrcMask          = *src-mask*]{lang="EN-US"}]{#struct_0_99677_28654_1643312797}

[[DstIP            = *dst-ip*]{lang="EN-US"}]{#struct_0_99677_28654_686971577}

[[DstMask          = *dst-mask*]{lang="EN-US"}]{#struct_0_99677_28654_x667714492}

[[L4Protocol       = *protocol-name*]{lang="EN-US"}]{#struct_0_99677_28654_1325462489}

[[SrcPortMin       = *min-src-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_2070617242}

[[SrcPortMax       = *max-src-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_286814163}

[[DstPortMin       = *min-dst-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_2080816002}

[[DstPortMax       = *max-dst-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_x1125297377}

[[Operation        = *operation*]{lang="EN-US"}]{#struct_0_99677_28654_1643378333}

[[下发给驱动的免认证规则的内容：]{style="font-family:宋体"}]{#struct_0_99677_28654_1454827725}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_99677_28654_1237971918}[：用户]{lang="EN-US" style="font-family:宋体"}[接入的接口名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_x1624268966}[：用户]{lang="EN-US" style="font-family:宋体"}[接入的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcMac]{lang="EN-US"}]{#struct_0_99677_28654_1381986400}[：]{lang="EN-US" style="font-family:宋体"}[用户的源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIP]{lang="EN-US"}]{#struct_0_99677_28654_x1473880191}[：]{lang="EN-US" style="font-family:宋体"}[用户报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcMask]{lang="EN-US"}]{#struct_0_99677_28654_x995123507}[：报文]{lang="EN-US" style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstIP]{lang="EN-US"}]{#struct_0_99677_28654_1642788508}[：用户报文的]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstMask]{lang="EN-US"}]{#struct_0_99677_28654_635562060}[：用]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L4Protocol]{lang="EN-US"}]{#struct_0_99677_28654_x1994520986}[：报文的传输层协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcPortMax]{lang="EN-US"}]{#struct_0_99677_28654_574565553}[：最大源端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcPortMin]{lang="EN-US"}]{#struct_0_99677_28654_x1613179451}[：]{lang="EN-US" style="font-family:宋体"}[最小源端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstPortMin]{lang="EN-US"}]{#struct_0_99677_28654_1905592880}[：]{lang="EN-US" style="font-family:宋体"}[最小目的端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstPortM]{lang="EN-US"}]{#struct_0_99677_28654_x1613022695}[ax]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[最大目的端口号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation]{lang="EN-US"}]{#struct_0_99677_28654_1642854044}[：]{lang="EN-US" style="font-family:宋体"}[规则的动作，包括]{style="font-family:宋体"}[add]{lang="EN-US"}[（添加）和]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[DRV_USER_RULE:]{lang="EN-US"}]{#struct_0_99677_28654_705720421}

[[L2 Interface           = *interface-name*]{lang="EN-US"}]{#struct_0_99677_28654_x929875748}

[[L3 Interface = *nterface-name*]{lang="EN-US"}]{#struct_0_99677_28654_x675109881}

[[VLAN             = *vlan-id*]{lang="EN-US"}]{#struct_0_99677_28654_483321984}

[[SrcIP            = *src-ip*]{lang="EN-US"}]{#struct_0_99677_28654_x1873268581}

[[SrcMac           = *src-mac*]{lang="EN-US"}]{#struct_0_99677_28654_1514832555}

[[AuthorACL        = *acl-num*]{lang="EN-US"}]{#struct_0_99677_28654_1642919580}

[[Operation        = *operation*]{lang="EN-US"}]{#struct_0_99677_28654_x908436439}

[[SetDrvFlag    =  *operation*]{lang="EN-US"}]{#struct_0_99677_28654_1546574489}

[[下发给驱动的用户规则的内容：]{style="font-family:宋体"}]{#struct_0_99677_28654_1938059470}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ L2 Interface]{lang="EN-US"}]{#struct_0_99677_28654_x978565795}[：用户接入的]{lang="EN-US" style="font-family:
  宋体"}[二层]{style="font-family:宋体"}[接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L3]{lang="EN-US"}]{#struct_0_99677_28654_1642985116}[ Interface]{lang="EN-US"}[：用户接入的三层接口名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_1447683292}[：用户接入的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIP]{lang="EN-US"}]{#struct_0_99677_28654_1351798528}[：用户报文的的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcM]{lang="EN-US"}]{#struct_0_99677_28654_x2143827574}[ac]{lang="EN-US"}[：用户报文的源]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthorACL]{lang="EN-US"}]{#struct_0_99677_28654_2093794416}[：用户的授权]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation]{lang="EN-US"}]{#struct_0_99677_28654_x1154605448}[：规则的动作]{lang="EN-US" style="font-family:宋体"}[，包括]{style="font-family:宋体"}[add]{lang="EN-US"}[（添加）和]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SetDrvFlag]{lang="EN-US"}]{#struct_0_99677_28654_1642526364}[：下发驱动的动作，包括需要下发和不需要下发]{style="font-family:宋体"}

[[DRV_REDIRECT_RULE:]{lang="EN-US"}]{#struct_0_99677_28654_x2033875058}

[[Interface = *interface-name*]{lang="EN-US"}]{#struct_0_99677_28654_1686648843}

[[VLAN             = *vlan-id*]{lang="EN-US"}]{#struct_0_99677_28654_507040339}

[[Protocol         = *protocol-name*]{lang="EN-US"}]{#struct_0_99677_28654_298621209}

[[SrcIP            = *src-ip*]{lang="EN-US"}]{#struct_0_99677_28654_1642591900}

[[SrcMask          = *src-mask*]{lang="EN-US"}]{#struct_0_99677_28654_x2044545075}

[[DstIP            = *dst-ip*]{lang="EN-US"}]{#struct_0_99677_28654_x1468720048}

[[DstMask          = *dst-mask*]{lang="EN-US"}]{#struct_0_99677_28654_1549892688}

[[L4 Protocol       = *protocol-name*]{lang="EN-US"}]{#struct_0_99677_28654_1642657436}

[[DstPort          = *dst-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_1506999435}

[[Operation        = *operation*]{lang="EN-US"}]{#struct_0_99677_28654_x704431050}

[[下发给驱动的重定向规则的内容：]{style="font-family:宋体"}]{#struct_0_99677_28654_2070308353}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_99677_28654_1511424774}[：用户接入的接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_1642722972}[：用户接入的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protocol]{lang="EN-US"}]{#struct_0_99677_28654_x1619830217}[：用户报文的传输层协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIP]{lang="EN-US"}]{#struct_0_99677_28654_x809319742}[：]{lang="EN-US" style="font-family:宋体"}[用户报文]{style="font-family:宋体"}[的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcMask]{lang="EN-US"}]{#struct_0_99677_28654_1643312796}[：报文的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstIP]{lang="EN-US"}]{#struct_0_99677_28654_686906041}[：]{lang="EN-US" style="font-family:宋体"}[用户报文]{style="font-family:宋体"}[的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstMask]{lang="EN-US"}]{#struct_0_99677_28654_1643378332}[：报文的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L4Protocol]{lang="EN-US"}]{#struct_0_99677_28654_1454762189}[：报文的传输层协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstPort]{lang="EN-US"}]{#struct_0_99677_28654_1623538546}[：报文的目的端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation]{lang="EN-US"}]{#struct_0_99677_28654_x1419257840}[：规则的动作]{lang="EN-US" style="font-family:宋体"}[，包括]{style="font-family:宋体"}[add]{lang="EN-US"}[（添加）和]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[DRV_DENY_RULE:]{lang="EN-US"}]{#struct_0_99677_28654_1642788507}

[[Interface          = *interface-name*]{lang="EN-US"}]{#struct_0_99677_28654_635889740}

[[VLAN             = *vlan-id*]{lang="EN-US"}]{#struct_0_99677_28654_x1466836905}

[[Protocol         = *protocol-name*]{lang="EN-US"}]{#struct_0_99677_28654_x893145735}

[[SrcIP            = *src-ip*]{lang="EN-US"}]{#struct_0_99677_28654_x1801485454}

[[SrcMask          = *src-mask*]{lang="EN-US"}]{#struct_0_99677_28654_1642854043}

[[DstIP            = *dst-ip*]{lang="EN-US"}]{#struct_0_99677_28654_705392741}

[[DstMask          = *dst-port-num*]{lang="EN-US"}]{#struct_0_99677_28654_80534584}

[[Operation        = *operation*]{lang="EN-US"}]{#struct_0_99677_28654_1963899633}

[[下发给驱动的]{style="font-family:宋体"}[deny]{lang="EN-US"}]{#struct_0_99677_28654_1642919579}[规则的内容：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_99677_28654_x907846618}[：用户接入的接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_99677_28654_1336269595}[：用户接入的]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Protocol]{lang="EN-US"}]{#struct_0_99677_28654_1662338449}[：用户报文的传输层协议号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcIP]{lang="EN-US"}]{#struct_0_99677_28654_1642985115}[：]{lang="EN-US" style="font-family:宋体"}[用户报文]{style="font-family:宋体"}[的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SrcMask]{lang="EN-US"}]{#struct_0_99677_28654_1447486684}[：报文的源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstIP]{lang="EN-US"}]{#struct_0_99677_28654_x172521544}[：用户报文的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DstMask]{lang="EN-US"}]{#struct_0_99677_28654_x1181315639}[：报文的目的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Operation]{lang="EN-US"}]{#struct_0_99677_28654_1642526363}[：规则的动作]{lang="EN-US" style="font-family:宋体"}[，包括]{style="font-family:宋体"}[add]{lang="EN-US"}[（添加）和]{style="font-family:宋体"}[delete]{lang="EN-US"}[（删除）]{style="font-family:宋体"}

[[IN Matching free rule.]{lang="EN-US"}]{#struct_0_99677_28654_x2033809522}

[[入方向匹配到免认证规则]{style="font-family:宋体"}]{#struct_0_99677_28654_x1909029011}

[[Out Matching free rule.]{lang="EN-US"}]{#struct_0_99677_28654_1642591899}

[[出方向匹配到免认证规则]{style="font-family:宋体"}]{#struct_0_99677_28654_x88688684}

[[IN Matching Redirect rule.]{lang="EN-US"}]{#struct_0_99677_28654_x1333514592}

[[入方向匹配到重定向规则]{style="font-family:宋体"}]{#struct_0_99677_28654_600632087}

[[Out Matching Redirect rule.]{lang="EN-US"}]{#struct_0_99677_28654_1642657435}

[[出方向匹配到重定向规则]{style="font-family:宋体"}]{#struct_0_99677_28654_1507196043}

[[IN Matching deny rule.]{lang="EN-US"}]{#struct_0_99677_28654_1687948548}

[[入方向匹配到]{style="font-family:宋体"}[deny]{lang="EN-US"}]{#struct_0_99677_28654_x283520650}[规则]{style="font-family:宋体"}

[[Out Matching deny rule.]{lang="EN-US"}]{#struct_0_99677_28654_1642722971}

[[出方向匹配到]{style="font-family:宋体"}[deny]{lang="EN-US"}]{#struct_0_99677_28654_x1619764681}[规则]{style="font-family:宋体"}

[[IN Matching User rule.]{lang="EN-US"}]{#struct_0_99677_28654_x1234616197}

[[入方向匹配到用户规则]{style="font-family:宋体"}]{#struct_0_99677_28654_1643312795}

[[Out Matching User rule.]{lang="EN-US"}]{#struct_0_99677_28654_687102649}

[[出方向匹配到用户规则]{style="font-family:宋体"}]{#struct_0_99677_28654_x381430995}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_99677_28654_x1438759695}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_x908890753}[在一台配置了]{style="font-family:宋体"}[Portal]{lang="EN-US"}[的设备上打开接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[报文调试信息开关，当有]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户上线时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal packet interface]{lang="EN-US"}[ gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_99677_28654_1643378331}

[\*Nov  1 09:23:02:146 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[Portal received 34 bytes of packet\[Type:req_info(9) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:146 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 09 00 00 05 c9 00 00 09 09 00 02 00 00 00 01]{lang="EN-US"}

[02 5c 3a 80 b3 dd 5e 16 72 4a 62 91 7e b2 31 47]{lang="EN-US"}

[08 02]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1454696653}*[设备收到]{style="font-family:宋体"}[REQ_INFO]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1613719848}

[Portal sent 62 bytes of packet\[Type:ack_info(10) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[  8 PORT                \] \[ 24\] \[Sysname-vlan-00-65535@vlan\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:23:02:147 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 0a 00 00 05 c9 00 00 09 09 00 02 00 00 00 02]{lang="EN-US"}

[a3 28 68 91 2b 15 b0 d3 f4 e3 22 ae 7f 01 e3 26]{lang="EN-US"}

[08 18 48 33 43 2d 76 6c 61 6e 2d 30 30 2d 36 35]{lang="EN-US"}

[35 33 35 40 76 6c 61 6e 0a 06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1773548796}*[设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[ACK_INFO]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x1995468910}

[Portal received 32 bytes of packet\[Type:req_challenge(1) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 01 00 00 05 c9 00 00 09 09 00 02 00 00 00 00]{lang="EN-US"}

[5d 68 8d 7c 58 67 51 6f d8 1a f9 d8 ed ae 35 90]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1317428650}*[设备收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[REQ_CHALLENGE]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x144325125}

[Portal sent 56 bytes of packet\[Type:ack_challenge(2) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[  3 CHALLENGE           \] \[ 18\] \[a89c5701492727bed97dbb09ac1d821f\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:23:02:151 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 02 00 00 05 c9 00 04 09 09 00 02 00 00 00 02]{lang="EN-US"}

[d0 a1 65 24 b2 8f c0 1d c0 bb a1 39 1f 5b cb 42]{lang="EN-US"}

[03 12 a8 9c 57 01 49 27 27 be d9 7d bb 09 ac 1d]{lang="EN-US"}

[82 1f 0a 06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1961734942}*[设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[ACK_CHALLENGE]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1642788506}

[Portal received 86 bytes of packet\[Type:req_auth(3) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[  1 USERNAME            \] \[ 12\] \[yangliping\]]{lang="EN-US"}

[\[  4 CHAPPWD             \] \[ 18\] \[10271c91c981016ca0b7df2ab21af265\]]{lang="EN-US"}

[\[  3 CHALLENGE           \] \[ 18\] \[a89c5701492727bed97dbb09ac1d821f\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:23:02:155 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 03 00 00 05 c9 00 04 09 09 00 02 00 00 00 04]{lang="EN-US"}

[ee 86 98 7e 66 5e c1 41 46 96 15 cc a3 7f 51 5f]{lang="EN-US"}

[01 0c 79 61 6e 67 6c 69 70 69 6e 67 04 12 10 27]{lang="EN-US"}

[1c 91 c9 81 01 6c a0 b7 df 2a b2 1a f2 65 03 12]{lang="EN-US"}

[a8 9c 57 01 49 27 27 be d9 7d bb 09 ac 1d 82 1f]{lang="EN-US"}

[0a 06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_635955276}*[设备收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[REQ_AUTH]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[%Nov  1 09:23:02:338 2012 Sysname PORTAL/6/PORTAL_USER_LOGON_SUCCESS: -MDC=1; -UserName=\[yangliping\]-IPAddr=\[9.9.0.2\]-IfName=\[Ethernet1/1\]-VlanID=\[65535\]-MACAddr=]{lang="EN-US"}]{#struct_0_99677_28654_x1853678197}

[\[0200-4c4f-4f50\]:User got online successfully.]{lang="EN-US"}

[\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[Portal sent 63 bytes of packet\[Type:ack_auth(4) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[ 11 SESSIONID           \] \[  8\] \[0200-4c4f-4f50\]]{lang="EN-US"}

[\[ 33 RELAYMSG            \] \[  4\] \[6\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:23:02:339 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 04 00 00 05 c9 00 04 09 09 00 02 00 00 00 05]{lang="EN-US"}

[bf 6a eb d9 38 48 6e 90 06 06 31 a4 72 72 f3 79]{lang="EN-US"}

[0b 08 02 00 4c 4f 4f 50 21 04 36 06 21 09 09 6c]{lang="EN-US"}

[69 70 69 6e 67 21 04 21 29 0a 06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1558694322}*[设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[ACK_AUTH]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:23:02:357 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1642854042}

[Portal received 32 bytes of packet\[Type:aff_ack_auth(7) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:357 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 07 00 00 05 c9 00 04 09 09 00 02 00 00 00 00]{lang="EN-US"}

[70 4b cd 55 1a cc ec fe 0f ce eb bf c0 c2 3c a5]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_705327205}*[设备收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[AFF_ACK_AUTH]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_68887062}

[Portal sent 53 bytes of packet\[Type:ntf_user_notify(19) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[ 33 RELAYMSG            \] \[ 15\] \[=M4BzIltI\>o\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:23:02:441 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 13 00 00 05 c9 00 04 09 09 00 02 00 00 00 02]{lang="EN-US"}

[e9 fe 48 a0 10 ed e3 65 fb 11 2f 2e 77 32 e3 21]{lang="EN-US"}

[21 0f 3d 0a 4d 34 42 7a 49 6c 74 49 3e 06 6f 0a]{lang="EN-US"}

[06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x491565057}*[设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器发送]{style="font-family:宋体"}[NTF_USER_NOTIFY]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\<Sysname\>\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x882342948}

[Portal received 44 bytes of packet\[Type:req_logout(5) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 05 00 00 05 ca 00 00 09 09 00 02 00 00 00 02]{lang="EN-US"}

[b2 8a 69 17 fe 31 df 51 fa 47 26 f6 56 93 a6 0a]{lang="EN-US"}

[0a 06 09 09 00 01 0c 06 00 00 00 00]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1883546793}*[设备收到]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[REQ_LOGOUT]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x1480843768}

[Portal sent 46 bytes of packet\[Type:ack_logout(6) ErrCode:0 IP:9.9.0.2\]]{lang="EN-US"}

[\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[\[ 11 SESSIONID           \] \[  8\] \[0200-4c4f-4f50\]]{lang="EN-US"}

[\[ 10 BASIP               \] \[  6\] \[9.9.0.1\]]{lang="EN-US"}

[\*Nov  1 09:27:52:952 2012 Sysname PORTAL/7/PACKET: -MDC=1;]{lang="EN-US"}

[02 06 00 00 05 ca 00 00 09 09 00 02 00 00 00 02]{lang="EN-US"}

[57 25 4e 31 a7 c1 61 a0 76 e0 26 8e 46 aa 4f 3a]{lang="EN-US"}

[0b 08 02 00 4c 4f 4f 50 0a 06 09 09 00 01]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1794686972}*[设备向]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务器回应]{style="font-family:宋体"}[ACK_LOGOUT]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_99677_28654_1642919578}[打开接口]{style="font-family:宋体"}[Vlan-interface6]{lang="EN-US"}[上的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[规则调试信息开关，当该接口上使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[认证时，将输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debug portal rule interface vlan-interface 6]{lang="EN-US"}]{#struct_0_99677_28654_x907912154}

[\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}

[ DRV_FREE_RULE:]{lang="EN-US"}

[    Interface        = ]{lang="EN-US"}[GigabitEthernet 1/0/1]{lang="EN-US"}

[    VLAN             = 6]{lang="EN-US"}

[    SrcMAC           = 0000-0000-0000]{lang="EN-US"}

[    SrcIP            = 0.0.0.0]{lang="EN-US"}

[    SrcMask          = 0.0.0.0]{lang="EN-US"}

[    DstIP            = 192.168.0.111]{lang="EN-US"}

[    DstMask          = 255.255.255.255]{lang="EN-US"}

[    L4Protocol       = 0]{lang="EN-US"}

[    SrcPortMin       = 0]{lang="EN-US"}

[    SrcPortMax       = 0]{lang="EN-US"}

[    DstPortMin       = 0]{lang="EN-US"}

[    DstPortMax       = 0]{lang="EN-US"}

[    Operation        = 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_2123368590}*[使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[后添加的免认证规则内容]{style="font-family:宋体"}*

[[\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_x1207841893}

[ DRV_REDIRECT_RULE:]{lang="EN-US"}

[    Interface        = ]{lang="EN-US"}[GigabitEthernet 1/0/1]{lang="EN-US"}

[    VLAN             = 6]{lang="EN-US"}

[    Protocol         = 2]{lang="EN-US"}

[    SrcIP            = 0.0.0.0]{lang="EN-US"}

[    SrcMask          = 0.0.0.0]{lang="EN-US"}

[    DstIP            = 0.0.0.0]{lang="EN-US"}

[    DstMask          = 0.0.0.0]{lang="EN-US"}

[    L4Protocol       = 6]{lang="EN-US"}

[    DstPort          = 80]{lang="EN-US"}

[    Operation        = 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x290443337}*[使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[后添加的重定向规则内容]{style="font-family:宋体"}*

[[\*Nov  1 09:30:18:689 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}]{#struct_0_99677_28654_1642985114}

[ DRV_DENY_RULE:]{lang="EN-US"}

[    Interface        = ]{lang="EN-US"}[GigabitEthernet 1/0/1]{lang="EN-US"}

[    VLAN             = 6]{lang="EN-US"}

[    Protocol         = 2]{lang="EN-US"}

[    SrcIP            = 0.0.0.0]{lang="EN-US"}

[    SrcMask          = 0.0.0.0]{lang="EN-US"}

[    DstIP            = 0.0.0.0]{lang="EN-US"}

[    DstMask          = 0.0.0.0]{lang="EN-US"}

[    Operation        = 1]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1447552220}*[使能]{style="font-family:宋体"}[Portal]{lang="EN-US"}[后添加的]{style="font-family:宋体"}[deny]{lang="EN-US"}[规则内容]{style="font-family:宋体"}*

[[\*Jan  6 20:17:06:382 2011 Sysname PORTAL/7/RULE:]{lang="EN-US"}]{#struct_0_99677_28654_x1346741765}

[ DRV_USER_RULE:]{lang="EN-US"}

[    L2 Interface     = N/A]{lang="EN-US"}

[    L3 Interface     = ]{lang="EN-US"}[GigabitEthernet 1/0/1]{lang="EN-US"}

[    VLAN             = 6]{lang="EN-US"}

[    SrcIP            = 9.9.0.1]{lang="EN-US"}

[    SrcMAC           = 0200-4c4f-4f50]{lang="EN-US"}

[    AuthorACL        = 3000]{lang="EN-US"}

[    Operation        = 0]{lang="EN-US"}

[    SetDrvFlag       = 1 ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_289880170}*[用户上线后添加的用户规则内容]{style="font-family:宋体"}*

[[Out Matching free rule]{lang="EN-US"}]{#struct_0_99677_28654_x619456887}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_919714778}*[出方向匹配到]{style="font-family:宋体"}[free]{lang="EN-US"}[规则]{style="font-family:宋体"}*

[[L3 Interface = ]{lang="EN-US"}[GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, DstMAC = 0000-0000-0000, SrcIP = 9.9.0.2, DstIP = 192.168.0.34]{lang="EN-US"}]{#struct_0_99677_28654_x373232839}

[ L4Protocol = 6, SrcPort = 1699, DstPort = 23, VPN Instance = 0]{lang="EN-US"}

[\*Nov  1 09:30:19:967 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_234023696}*[符合匹配规则的报文信息]{style="font-family:宋体"}*

[[ IN Matching free rule]{lang="EN-US"}]{#struct_0_99677_28654_143620971}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1642526362}*[入方向匹配到]{style="font-family:宋体"}[free]{lang="EN-US"}[规则]{style="font-family:宋体"}*

[[L3 Interface = ]{lang="EN-US"}[GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, SrcMac = 0200-4c4f-4f50,SrcIP = 9.9.0.2, DstIP = 192.168.0.34]{lang="EN-US"}]{#struct_0_99677_28654_x2033743986}

[ L4Protocol = 6, SrcPort = 1699, DstPort = 23, VPN Instance = 0]{lang="EN-US"}

[\*Nov  1 09:30:20:088 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x941131319}*[符合匹配规则的报文信息]{style="font-family:宋体"}*

[[OUT Matching Deny rule]{lang="EN-US"}]{#struct_0_99677_28654_738952551}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_1490396241}*[出方向匹配到]{style="font-family:宋体"}[deny]{lang="EN-US"}[规则]{style="font-family:宋体"}*

[[L3 Interface = ]{lang="EN-US"}[GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, DstMAC = 0200-4c4f-4f50,SrcIP = 9.9.0.2, DstIP = 9.9.0.1]{lang="EN-US"}]{#struct_0_99677_28654_x506510846}

[ L4Protocol = 1, SrcPort = 0, DstPort = 0, VPN Instance = 0]{lang="EN-US"}

[\*Nov  1 09:30:31:603 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_x1773211322}*[符合匹配规则的报文信息]{style="font-family:宋体"}*

*[ ]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[ IN Matching Deny rule]{lang="EN-US"}]{#struct_0_99677_28654_1088638856}

[ L3 Interface = ]{lang="EN-US"}[GigabitEthernet1/0/2, L2 Interface = \--, VLAN = \--, SrcMac = 14d6-4d14-bd9b,]{lang="EN-US"}

[SrcIP = 10.153.72.116, DstIP = 239.255.255.250]{lang="EN-US"}

[ L4Protocol = 17, SrcPort = 49159, DstPort = 1900, VPN Instance = 0]{lang="EN-US"}

[\*Nov  1 09:30:31:683 2012 Sysname PORTAL/7/RULE: -MDC=1;]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_99677_28654_282120787}*[报文经过设备访问外网]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
