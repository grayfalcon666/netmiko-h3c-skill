::: {#1892081314 .myid}
[]{#_Toc404786109}[]{#struct_0_x5045_19324_1852208261}

**DHCP \-- DHCP调试命令 \-- debugging dhcp client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5045_19324_1695599149}

[**[debugging dhcp client]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_x1237369198}

[**[undo debugging dhcp client]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_1082409551}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5045_19324_1928152748}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1086251781}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x930848232}

[[network-admin]{lang="EN-US"}]{#struct_0_x5045_19324_1852404869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5045_19324_1397576223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5045_19324_1031094590}

[**[all]{lang="EN-US"}**]{#struct_0_x5045_19324_106906278}[：表示]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x5045_19324_x781304582}[：表示]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端的报文不可识别或错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5045_19324_1377179404}[：表示]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x5045_19324_1589779317}[：表示]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x172996910}

[**[debugging dhcp client]{lang="EN-US"}**]{#struct_0_x5045_19324_x51396985}[命令用来打开]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}**[undo debugging dhcp client]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_1717830457}[客户端调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging dhcp client packet]{lang="EN-US"}]{#struct_0_x5045_19324_932840481}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1148566273}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_1852339333}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_1307399540}

[[From *ip-address* port *port*]{lang="EN-US"}]{#struct_0_x5045_19324_649608572}

[[接收报文的源地址和端口号]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1697408773}

[[To *ip-address* port *port*]{lang="EN-US"}]{#struct_0_x5045_19324_161508614}

[[发送报文的目的地址和端口号]{style="font-family:宋体"}]{#struct_0_x5045_19324_453570142}

[[interface *interface-name*]{lang="EN-US"}]{#struct_0_x5045_19324_x666858529}

[[接收或发送报文的接口]{style="font-family:宋体"}]{#struct_0_x5045_19324_1851880582}

[[Message type: *message-type*]{lang="EN-US"}]{#struct_0_x5045_19324_x1612831727}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x675626570}[报文的操作类型，有两种：]{style="font-family:宋体"}[REQUEST]{lang="EN-US"}[和]{style="font-family:宋体"}[REPLY]{lang="EN-US"}

[[Hardware type: *hardware-type*]{lang="EN-US"}]{#struct_0_x5045_19324_x1573339547}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1779922917}[客户端的硬件类型]{style="font-family:宋体"}

[[Hardware address length: *length*]{lang="EN-US"}]{#struct_0_x5045_19324_1851815046}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_720035078}[客户端的硬件地址长度]{style="font-family:宋体"}

[[Hops: *hops*]{lang="EN-US"}]{#struct_0_x5045_19324_493816331}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1742637999}[报文经过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继到服务器的跳数]{style="font-family:宋体"}

[[Transaction ID: *transaction-ID*]{lang="EN-US"}]{#struct_0_x5045_19324_1525409773}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1852011654}[客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程]{style="font-family:宋体"}

[[Seconds: *seconds*]{lang="EN-US"}]{#struct_0_x5045_19324_2146939001}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1728491649}[客户端从开始申请到当前经过的时间]{style="font-family:宋体"}

[[Broadcast flag: *flag*]{lang="EN-US"}]{#struct_0_x5045_19324_x628628740}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1697621621}[广播标记：]{style="font-family:宋体"}[1]{lang="EN-US"}[为广播，]{style="font-family:宋体"}[0]{lang="EN-US"}[为单播]{style="font-family:宋体"}

[[Client IP address: *client-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_1851946118}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x65836983}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Your IP address: *your-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_333587073}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_250612526}[服务器分配给客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Server IP address: *server-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_1852142726}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1743666106}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay agent IP address: *gateway-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_2046920689}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_835335684}[中继的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client hardware address: *client-hardware-address*]{lang="EN-US"}]{#struct_0_x5045_19324_1852077190}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1368913099}[客户端的硬件地址]{style="font-family:宋体"}

[[Server host name: *host-name*]{lang="EN-US"}]{#struct_0_x5045_19324_x752701313}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1852273798}[服务器的主机名]{style="font-family:宋体"}

[[Boot file name: *file-name*]{lang="EN-US"}]{#struct_0_x5045_19324_x983316615}

[[启动文件名及路径]{style="font-family:宋体"}]{#struct_0_x5045_19324_598617536}

[[DHCP message type: *type*]{lang="EN-US"}]{#struct_0_x5045_19324_x2014991024}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1852208262}[报文的类型，有]{style="font-family:宋体"}[8]{lang="EN-US"}[种类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_1695533613}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPDISCOVER]{lang="EN-US"}]{#struct_0_x5045_19324_1461910071}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCPOFFER]{lang="EN-US"}]{#struct_0_x5045_19324_x895855960}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPREQUEST]{lang="EN-US"}]{#struct_0_x5045_19324_1852404870}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPDECLINE]{lang="EN-US"}]{#struct_0_x5045_19324_1397117470}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_x2084516564}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPNAK]{lang="EN-US"}]{#struct_0_x5045_19324_1852339334}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPRELEASE]{lang="EN-US"}]{#struct_0_x5045_19324_1307727220}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPINFORM]{lang="EN-US"}]{#struct_0_x5045_19324_x100564644}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging dhcp client event]{lang="EN-US"}]{#struct_0_x5045_19324_419283891}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1156150244}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_1851880579}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1613290482}

[*[InterfaceName]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x5045_19324_x1749310863}

[[配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1405719729}[客户端的接口]{style="font-family:宋体"}

[[DHCP/BOOTP FSM state transfered (*state1*\--\> *state2*) successfully.]{lang="EN-US"}]{#struct_0_x5045_19324_x1915339522}

[[DHCP/BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_80936405}[客户端从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[状态转换为]{style="font-family:宋体"}*[state2]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[[Resending DHCP request packet timed out. Stopped sending.]{lang="EN-US"}]{#struct_0_x5045_19324_1851815043}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_720362758}[请求报文重发超时，停止发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}

[[Successfully sent ARP request for address (*ip-address*).]{lang="EN-US"}]{#struct_0_x5045_19324_x1612486905}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x5045_19324_x1473779709}[成功]{style="font-family:宋体"}

[[Received no ARP reply for *ip-address*, so the IP address is available.]{lang="EN-US"}]{#struct_0_x5045_19324_1972264790}

[[没有收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x5045_19324_1852011651}[回应，分配的地址可用]{style="font-family:宋体"}

[[Successfully sent *Message-Type* packet.]{lang="EN-US"}]{#struct_0_x5045_19324_2147266681}

[[发送]{style="font-family:宋体"}*[Message-Type]{lang="EN-US"}*]{#struct_0_x5045_19324_x77235335}[报文成功]{style="font-family:宋体"}

[[Successfully enabled/disabled DHCP.]{lang="EN-US"}]{#struct_0_x5045_19324_682260179}

[[启用]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5045_19324_328829385}[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[功能成功]{style="font-family:宋体"}

[[Successfully enabled/disabled protocol on cpu.]{lang="EN-US"}]{#struct_0_x5045_19324_1851946115}

[[启用]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5045_19324_x65640375}[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[功能上送]{style="font-family:宋体"}[CPU]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Failed to add IP address. ]{lang="EN-US"}]{#struct_0_x5045_19324_159814844}

[[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_x1191464007}[地址失败]{style="font-family:宋体"}

[[Notified route module to add routes.]{lang="EN-US"}]{#struct_0_x5045_19324_1852142723}

[[通知路由模块添加路由]{style="font-family:宋体"}]{#struct_0_x5045_19324_1743862714}

[[Notified route module to delete routes.]{lang="EN-US"}]{#struct_0_x5045_19324_460020120}

[[通知路由模块删除路由]{style="font-family:宋体"}]{#struct_0_x5045_19324_1369736131}

[[Received *Message-Type* packet in *state* state. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1852077187}

[[在]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_x5045_19324_1368585420}[状态收到]{style="font-family:宋体"}*[Message-Type]{lang="EN-US"}*[报文，不合法，忽略该报文]{style="font-family:宋体"}

[[Received DHCPACK, *ip-address* is not our requested address. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x365979090}

[[收到的]{style="font-family:宋体"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_1945235829}[报文中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不是请求地地址，忽略该报文]{style="font-family:宋体"}

[[Received DHCPACK from non-selected server *ip-address*. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1852273795}

[[收到的]{style="font-family:宋体"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_x982988935}[报文不是来自选择的]{style="font-family:宋体"}[Server]{lang="EN-US"}[，忽略该报文]{style="font-family:宋体"}

[[Lease is below min time. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x1262051210}

[[租约小于最小时间，忽略该报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_1206071311}

[[Received duplicate lease. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1852208259}

[[收到重复的租约，忽略该报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_1696123438}

[[Beginning to detect IP address conflict via ARP.]{lang="EN-US"}]{#struct_0_x5045_19324_565705405}

[[开始通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_x5045_19324_1852404867}[进行冲突检测]{style="font-family:宋体"}

[[Interface hardware address changed. Transfered to INIT state.]{lang="EN-US"}]{#struct_0_x5045_19324_1397183007}

[[接口硬件地址变化。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1852339331}[客户端状态迁移到]{style="font-family:宋体"}[INIT]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Allocated IP (*ip-address*) has been used by another host.]{lang="EN-US"}]{#struct_0_x5045_19324_1851880580}

[[分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_1851815044}[地址已经被其它客户端使用]{style="font-family:宋体"}

[[Allocated IP (*ip-address*) conflicts with some other interface.]{lang="EN-US"}]{#struct_0_x5045_19324_1852011652}

[[分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_1851946116}[地址与本机其它接口冲突]{style="font-family:宋体"}

[[T1 timer expired. Begin to renew.]{lang="EN-US"}]{#struct_0_x5045_19324_1852142724}

[[T1]{lang="EN-US"}]{#struct_0_x5045_19324_1852077188}[时间到期，开始续约操作]{style="font-family:宋体"}

[[Lease expired. ]{lang="EN-US"}]{#struct_0_x5045_19324_1368388812}

[[租约到期]{style="font-family:宋体"}]{#struct_0_x5045_19324_1852273796}

[[Successfully notified the client\'s information change.]{lang="EN-US"}]{#struct_0_x5045_19324_x983185543}

[[Client]{lang="EN-US"}]{#struct_0_x5045_19324_1852208260}[状态发生变化时，成功通知外部模块]{style="font-family:宋体"}[option]{lang="EN-US"}[信息变化]{style="font-family:宋体"}

**[ ]{lang="EN-US"}**

[[表1-3 ]{lang="EN-US"}[debugging dhcp client error]{lang="EN-US"}]{#struct_0_x5045_19324_1695664685}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1131248640}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_x900060450}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1028788103}

[*[InterfaceName]{lang="EN-US"}*[:]{lang="EN-US"}]{#struct_0_x5045_19324_1852404868}

[[配置为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1397641759}[客户端的接口]{style="font-family:宋体"}

[*[operation]{lang="EN-US"}*]{#struct_0_x5045_19324_x1658788917}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_224365416}[客户端状态机变化和事件处理]{style="font-family:宋体"}

[[Failed to allocate memory for new packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1852339332}

[[申请报文内存失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_1307334004}

[[Failed to send *Message-Type* packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x1290930567}

[[发送]{style="font-family:宋体"}*[Message-Type]{lang="EN-US"}*]{#struct_0_x5045_19324_x3258142}[报文失败]{style="font-family:宋体"}

[[The *field* field of the received *Message-Typ*e packet is invalid. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1851880577}

[*[Message-Type]{lang="EN-US"}*]{#struct_0_x5045_19324_x1612635122}[报文中的]{style="font-family:宋体"}*[field]{lang="EN-US"}*[域无效，忽略该报文]{style="font-family:宋体"}

[[The received *Message-Type* packet is for another client (*ip-address).* Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x530112627}

[[接收到的]{style="font-family:宋体"}*[Message-Type]{lang="EN-US"}*]{#struct_0_x5045_19324_1851815041}[报文是发送给客户端]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的，忽略该报文]{style="font-family:宋体"}

[[Failed to enable/disable DHCP.]{lang="EN-US"}]{#struct_0_x5045_19324_720231686}

[[启用]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5045_19324_x787942597}[关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[功能失败]{style="font-family:宋体"}

[[Failed to enable/disable BOOTP.]{lang="EN-US"}]{#struct_0_x5045_19324_1852011649}

[[启用]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5045_19324_x2147176326}[关闭]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[功能失败]{style="font-family:宋体"}

[[The length of *option-type* option is invalid (%d bytes). Ignored it.]{lang="EN-US"}]{#struct_0_x5045_19324_1851946113}

[*[option-type]{lang="EN-US"}*]{#struct_0_x5045_19324_x65509303}[域长度非法，忽略此域。]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[subnet mask]{lang="EN-US"}]{#struct_0_x5045_19324_1470206934}[：子网掩码]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[server identifier]{lang="EN-US"}]{#struct_0_x5045_19324_1852142721}[：服务器标识]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[router]{lang="EN-US"}]{#struct_0_x5045_19324_1743993786}[：默认网关]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[tftp]{lang="EN-US"}[ server address]{lang="EN-US"}]{#struct_0_x5045_19324_1852077185}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AC list]{lang="EN-US"}]{#struct_0_x5045_19324_1368716492}[：接入控制器]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[domain name servers]{lang="EN-US"}]{#struct_0_x5045_19324_x1921249530}[：域名服务器地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[static router]{lang="EN-US"}]{#struct_0_x5045_19324_1852273793}[：静态路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[classless static router]{lang="EN-US"}]{#struct_0_x5045_19324_x982857863}[：无类静态路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BIMS server]{lang="EN-US"}]{#struct_0_x5045_19324_1852208257}[：]{style="font-family:
  宋体"}[BIMS]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[The length of *option-type* option is too long (%d bytes). Only save part of it.]{lang="EN-US"}]{#struct_0_x5045_19324_1695730222}

[*[option-type]{lang="EN-US"}*]{#struct_0_x5045_19324_1852404865}[域长度太长，仅保存部分域。]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[router]{lang="EN-US"}]{#struct_0_x5045_19324_1397314079}[：默认网关]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[tftp]{lang="EN-US"}[ server address]{lang="EN-US"}]{#struct_0_x5045_19324_1852339329}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[boot file name]{lang="EN-US"}]{#struct_0_x5045_19324_1308054899}[：启动文件名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[AC list]{lang="EN-US"}]{#struct_0_x5045_19324_65140301}[：接入控制器]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[tftp]{lang="EN-US"}[ server name]{lang="EN-US"}]{#struct_0_x5045_19324_1851880578}[：]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[服务器名称]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[domain name servers]{lang="EN-US"}]{#struct_0_x5045_19324_x1613224946}[：域名服务器地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[domain name]{lang="EN-US"}]{#struct_0_x5045_19324_1851815042}[：域名]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[static router]{lang="EN-US"}]{#struct_0_x5045_19324_720297222}[：静态路由]{style="font-family:宋体"}

[[The *option-type* option is invalid. Ignored it.]{lang="EN-US"}]{#struct_0_x5045_19324_x1292660748}

[*[option-type]{lang="EN-US"}*]{#struct_0_x5045_19324_273423193}[域内容非法，忽略此域。]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*[取值包括：]{style="font-family:宋体"} [router]{lang="EN-US"}[：默认网关]{style="font-family:宋体"}

[[Discarding packet with bogus htype/hlen.]{lang="EN-US"}]{#struct_0_x5045_19324_1852011650}

[[丢弃包含假]{style="font-family:宋体"}[htype/hlen]{lang="EN-US"}]{#struct_0_x5045_19324_2147201145}[域的报文]{style="font-family:宋体"}

[[Decoding options field failed.]{lang="EN-US"}]{#struct_0_x5045_19324_658025386}

[[解析选项域错误]{style="font-family:宋体"}]{#struct_0_x5045_19324_1851946114}

[[Received a duplicate DHCPACK packet. Ignored the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x65574839}

[[接收到重复的]{style="font-family:宋体"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_1852142722}[报文，忽略该报文]{style="font-family:宋体"}

[[Address conflicts.]{lang="EN-US"}]{#struct_0_x5045_19324_1743928250}

[[地址冲突]{style="font-family:宋体"}]{#struct_0_x5045_19324_1852077186}

[[Transfered to unknown FSM state.]{lang="EN-US"}]{#struct_0_x5045_19324_1368519884}

[[迁移到未知状态]{style="font-family:宋体"}]{#struct_0_x5045_19324_1852273794}

[[Skip parsing the current PXE server TLV in verdor specific information option due to invalid server type.]{lang="EN-US"}]{#struct_0_x5045_19324_1852208258}

[[由于]{style="font-family:宋体"}[PXE]{lang="EN-US"}]{#struct_0_x5045_19324_1696188974}[服务器类型错误，跳过当前]{style="font-family:宋体"}[PXE]{lang="EN-US"}[引导服务器地址列表，继续解析]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[的其他字段]{style="font-family:宋体"}

[[Skip parsing the current PXE server TLV in verdor specific information option due to length error.]{lang="EN-US"}]{#struct_0_x5045_19324_1852404866}

[[由于]{style="font-family:宋体"}[PXE]{lang="EN-US"}]{#struct_0_x5045_19324_1397248543}[地址列表长度错误，跳过当前]{style="font-family:宋体"}[PXE]{lang="EN-US"}[引导服务器地址列表，继续解析]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[的其他字段]{style="font-family:宋体"}

[[Skip parsing the current PXE server TLV in verdor specific information option due to invalid server number.]{lang="EN-US"}]{#struct_0_x5045_19324_1852339330}

[[由于]{style="font-family:宋体"}[PXE]{lang="EN-US"}]{#struct_0_x5045_19324_1307465076}[服务器数目错误，跳过当前]{style="font-family:宋体"}[PXE]{lang="EN-US"}[引导服务器地址列表，继续解析]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[的其他字段]{style="font-family:宋体"}

[[Skip parsing the current PXE server TLV in verdor specific information option due to unknown error.]{lang="EN-US"}]{#struct_0_x5045_19324_x520772414}

[[由于未知错误，跳过当前]{style="font-family:宋体"}[PXE]{lang="EN-US"}]{#struct_0_x5045_19324_x918033745}[引导服务器地址列表，继续解析]{style="font-family:宋体"}[Option 43]{lang="EN-US"}[的其他字段]{style="font-family:宋体"}

[[Failed to parse verdor specific information option. Ignore it.]{lang="EN-US"}]{#struct_0_x5045_19324_x520313662}

[[解析]{style="font-family:宋体"}[Option 43]{lang="EN-US"}]{#struct_0_x5045_19324_1415405281}[域失败，忽略此域]{style="font-family:宋体"}

[[The destination IP address of classless static route option is wrong.]{lang="EN-US"}]{#struct_0_x5045_19324_x520772413}

[[Option 121]{lang="EN-US"}]{#struct_0_x5045_19324_x918492497}[选项中的目的地址错误]{style="font-family:宋体"}

[[The mask length of classless static route option is wrong.]{lang="EN-US"}]{#struct_0_x5045_19324_x520837949}

[[Option 121]{lang="EN-US"}]{#struct_0_x5045_19324_1050774844}[选项中的掩码长度错误]{style="font-family:宋体"}

[[Failed to parse classless static route option. Ignore it.]{lang="EN-US"}]{#struct_0_x5045_19324_x520641341}

[[解析]{style="font-family:宋体"}[Option 121]{lang="EN-US"}]{#struct_0_x5045_19324_x924092872}[域失败，忽略该域]{style="font-family:宋体"}

[[The destination IP address of static route option is wrong.]{lang="EN-US"}]{#struct_0_x5045_19324_x520706877}

[[Option 33]{lang="EN-US"}]{#struct_0_x5045_19324_x520510269}[选项中的目的地址错误]{style="font-family:宋体"}

[[Failed to parse static route option. Ignore it.]{lang="EN-US"}]{#struct_0_x5045_19324_x1711275714}

[[解析]{style="font-family:宋体"}[Option 33]{lang="EN-US"}]{#struct_0_x5045_19324_x520575805}[域失败，忽略该域]{style="font-family:宋体"}

[[Failed to parse ACS parameters in verdor specific information option.]{lang="EN-US"}]{#struct_0_x5045_19324_1852679015}

[[Option 43]{lang="EN-US"}]{#struct_0_x5045_19324_x520379197}[选项中]{style="font-family:宋体"}[ACS]{lang="EN-US"}[参数解析失败]{style="font-family:宋体"}

[[Failed to parse ACS provision code in verdor specific information option.]{lang="EN-US"}]{#struct_0_x5045_19324_x187557248}

[[Option 43]{lang="EN-US"}]{#struct_0_x5045_19324_x520444733}[选项中]{style="font-family:宋体"}[ACS provision code]{lang="EN-US"}[解析失败]{style="font-family:宋体"}

[[Malformed packet dhcp:]{lang="EN-US"}]{#struct_0_x5045_19324_10957604}

[[option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_x5045_19324_699156719}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_476491509}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[The received BOOTP/DHCP packet is not a BOOTPREPLY.]{lang="EN-US"}]{#struct_0_x5045_19324_x520248125}

[[接收到的]{style="font-family:宋体"}[BOOTP/DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1380820363}[报文不是应答报文]{style="font-family:宋体"}

[[Received an invalid DHCP packet, the type is *type-id*]{lang="EN-US"}]{#struct_0_x5045_19324_x520313661}

[[接收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520772416}[报文为非法报文，类型为]{style="font-family:宋体"}*[type-id]{lang="EN-US"}*[ ]{lang="EN-US"}

[[Failed to add allocated IP *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_x918164817}

[[添加分配的地址失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_x520837952}

[[Failed to get the index of receiving interface.]{lang="EN-US"}]{#struct_0_x5045_19324_x520641344}

[[获取入接口的接口索引失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_x923896264}

[[Received an invalid DHCP/BOOTP packet, the length of the packet is too short.]{lang="EN-US"}]{#struct_0_x5045_19324_x520706880}

[[收到非法]{style="font-family:宋体"}[DHCP/BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_x520510272}[报文，报文长度过短]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1711603395}

[[\# DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x2113243909}[客户端从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获得]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。打开]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的所有调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging dhcp client all]{lang="EN-US"}]{#struct_0_x5045_19324_1547998853}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ip address dhcp-alloc]{lang="EN-US"}

[\[Sysname-Vlan-interface2\]]{lang="EN-US"}

[\*Jan 19 15:16:24:424 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Successfully enabled protocol on cpu.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1846077321}*[协议上送成功。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:24:426 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520575808}

[Successfully notified the client\'s information change.]{lang="EN-US"}

[*[// Client]{lang="EN-US"}*]{#struct_0_x5045_19324_1851958119}*[状态发生变化时，成功通知外部模块]{style="font-family:宋体"}[option]{lang="EN-US"}[信息变化。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x510801725}

[Vlan-interface2: Successfully enabled DHCP.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_x1274192249}*[接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[获取]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置成功。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520379200}

[Vlan-interface2 DHCP FSM state transfered (HALT\--\>INIT) successfully.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1386355337}*[客户端从]{style="font-family:宋体"}[HALT]{lang="EN-US"}[状态迁移为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520444736}

[Vlan-interface2 DHCP FSM state transfered (INIT\--\>SELECTING) successfully.]{lang="EN-US"}

[\*Jan 19 15:16:24:428 2012 Sysname DHCPC/7/PACKET: -MDC=1;]{lang="EN-US"}

[To 255.255.255.255 port 67, interface Vlan-interface2]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 2883026512]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 1]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000c-295c-e3a6]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPDISCOVER (1)]{lang="EN-US"}

[\*Jan 19 15:16:24:429 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Vlan-interface2 Successfully sent DHCPDISCOVER packet.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1846750958}*[客户端成功发送]{style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[报文，状态机从]{style="font-family:宋体"}[INIT]{lang="EN-US"}[状态迁移为]{style="font-family:宋体"}[SELECTING]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:24:622 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520313664}

[Vlan-interface2 Received a packet.]{lang="EN-US"}

[\*Jan 19 15:16:24:622 2012 Sysname DHCPC/7/PACKET: -MDC=1;]{lang="EN-US"}

[From 192.168.38.254 port 67, interface Vlan-interface2]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 2883026512]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 1]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 22.0.0.2]{lang="EN-US"}

[    Server IP address: 22.0.0.1   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000c-295c-e3a6]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPOFFER (2)]{lang="EN-US"}

[// DHCP]{lang="EN-US"}[客户端收到]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[22.0.0.1]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发送的]{style="font-family:宋体"}[DHCP-OFFER]{lang="EN-US"}[报文，分配到的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[22.0.0.2]{lang="EN-US"}[，租约时间为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒（即一天）。]{style="font-family:宋体"}

[\*Jan 19 15:16:26:117 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Vlan-interface2 DHCP FSM state transfered (SELECTING\--\>REQUESTING) successfully.]{lang="EN-US"}

[\*Jan 19 15:16:26:117 2012 Sysname DHCPC/7/PACKET: -MDC=1;]{lang="EN-US"}

[To 255.255.255.255 port 67, interface Vlan-interface2]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 2883026512]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 1]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000c-295c-e3a6]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[DHCP message type: DHCPREQUEST (3)]{lang="EN-US"}

[\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Vlan-interface2 Successfully sent DHCPREQUEST packet.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1415012065}*[客户端成功发送]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文，状态机从]{style="font-family:宋体"}[SELECTING]{lang="EN-US"}[状态迁移为]{style="font-family:宋体"}[REQUESTING]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520772415}

[Vlan-interface2 Received a packet.]{lang="EN-US"}

[\*Jan 19 15:16:26:118 2012 Sysname DHCPC/7/PACKET: -MDC=1;]{lang="EN-US"}

[From 192.168.38.254 port 67, interface Vlan-interface2]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 2883026512]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 1]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 22.0.0.2]{lang="EN-US"}

[    Server IP address: 22.0.0.1   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000c-295c-e3a6]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPACK (5)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x918099281}*[客户端接收]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520837951}

[Vlan-interface2: Beginning to detect IP address conflict via ARP.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1050250557}*[客户端开始通过]{style="font-family:宋体"}[ARP]{lang="EN-US"}[进行冲突检测。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:27:119 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_1757619542}

[Vlan-interface2 Successfully sent ARP request for address 22.0.0.2.]{lang="EN-US"}

[\*Jan 19 15:16:27:119 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Vlan-interface2 Transfer to BOUND state if no ARP reply is received in 2 seconds. ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_x44280569}*[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文成功，如果在]{style="font-family:宋体"}[2]{lang="EN-US"}[秒内没有收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[响应报文，则转变为]{style="font-family:宋体"}[BOUND]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x520641343}

[Vlan-interface2 Successfully sent ARP request for address 22.0.0.2.]{lang="EN-US"}

[\*Jan 19 15:16:28:118 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}

[Vlan-interface2 Transfer to BOUND state if no ARP reply is received in 1 second]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_x924223944}*[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文成功，如果在]{style="font-family:宋体"}[1]{lang="EN-US"}[秒内没有收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[响应报文，则转变为]{style="font-family:宋体"}[BOUND]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:29:117 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_403529347}

[Vlan-interface2 Received no ARP reply for 22.0.0.2, so the IP address is available.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_976057596}*[没有收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[响应报文，开始使用该地址。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:29:127 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x479872939}

[Notified route module to add 1 route.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_x520706879}*[成功通知路由模块添加]{style="font-family:宋体"}[1]{lang="EN-US"}[条路由。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:29:129 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_280369221}

[Successfully notified the client\'s information change.]{lang="EN-US"}

[*[// Client]{lang="EN-US"}*]{#struct_0_x5045_19324_x520737162}*[状态发生变化时，成功通知外部模块]{style="font-family:宋体"}[option]{lang="EN-US"}[信息变化。]{style="font-family:宋体"}*

[[\*Jan 19 15:16:29:129 2012 Sysname DHCPC/7/Debug: -MDC=1;]{lang="EN-US"}]{#struct_0_x5045_19324_x1715434271}

[Vlan-interface2 DHCP FSM state transfered (REQUESTING\--\>BOUND) successfully.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x1871475377}*[状态迁移为]{style="font-family:宋体"}[BOUND]{lang="EN-US"}[状态。]{style="font-family:宋体"}*

::: {#-1754639150 .myid}
[]{#_Toc404786110}[]{#struct_0_x5045_19324_x1717750230}

**DHCP \-- DHCP调试命令 \-- debugging dhcp relay**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x520510271}

[**[debugging dhcp relay]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** \[ **client** **mac** *mac-address* \] }]{lang="EN-US"}]{#struct_0_x5045_19324_x1711800003}

[**[undo]{lang="EN-US"}**[ **debugging dhcp relay** { **all** \| **error** \| **event** \| **packet** \[ **client mac** *mac-address* \] }]{lang="EN-US"}]{#struct_0_x5045_19324_1496527006}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x2034905947}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5045_19324_17842377}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5045_19324_145081736}

[[network-admin]{lang="EN-US"}]{#struct_0_x5045_19324_x520575807}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5045_19324_1852547943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x162663379}

[**[all]{lang="EN-US"}**]{#struct_0_x5045_19324_978485080}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x5045_19324_363042305}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5045_19324_x1516928580}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x5045_19324_x520379199}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的报文调试信息开关。]{style="font-family:宋体"}

[**[client]{lang="EN-US"}**[ **mac** *mac-address*]{lang="EN-US"}]{#struct_0_x5045_19324_x188212608}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继为指定]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端转发报文的调试信息开关，其中]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5045_19324_883710738}

[**[debugging dhcp relay]{lang="EN-US"}**]{#struct_0_x5045_19324_244437242}[命令用来打开]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继调试信息开关。]{style="font-family:宋体"}**[undo debugging dhcp relay]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1254797954}[中继调试信息功能开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging dhcp relay packet]{lang="EN-US"}]{#struct_0_x5045_19324_x278212726}[调试信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1136932841}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_x520444735}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_1846947566}

[[From *ip-address*]{lang="EN-US"}]{#struct_0_x5045_19324_x1769407574}

[[接收报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_2012181985}

[[To *ip-address*]{lang="EN-US"}]{#struct_0_x5045_19324_x910392400}

[[发送报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_x520248127}

[[interface *interface-name*]{lang="EN-US"}]{#struct_0_x5045_19324_1380689291}

[[接收或发送报文的接口]{style="font-family:宋体"}]{#struct_0_x5045_19324_x665630982}

[[Message type: *message-type*]{lang="EN-US"}]{#struct_0_x5045_19324_x71687795}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_148785080}[报文的操作类型，有两种：]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[和]{style="font-family:宋体"}[DHCP-REPLY]{lang="EN-US"}

[[Hardware type: *hardware-type*]{lang="EN-US"}]{#struct_0_x5045_19324_552695402}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520313663}[客户端的硬件类型]{style="font-family:宋体"}

[[Hardware address length: *length*]{lang="EN-US"}]{#struct_0_x5045_19324_1415339745}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1778240127}[客户端的硬件地址长度]{style="font-family:宋体"}

[[Hops: *hops*]{lang="EN-US"}]{#struct_0_x5045_19324_1270573441}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520772418}[报文经过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继转发的跳数]{style="font-family:宋体"}

[[Transaction ID: *transaction-ID*]{lang="EN-US"}]{#struct_0_x5045_19324_x918820177}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_493540126}[客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程]{style="font-family:宋体"}

[[Seconds: *seconds*]{lang="EN-US"}]{#struct_0_x5045_19324_x261977085}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520837954}[客户端从开始申请到当前经过的时间，目前没有使用，固定为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Broadcast flag: *flag*]{lang="EN-US"}]{#struct_0_x5045_19324_1050053949}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1395312452}[广播标记：]{style="font-family:宋体"}[1]{lang="EN-US"}[为广播，]{style="font-family:宋体"}[0]{lang="EN-US"}[为单播]{style="font-family:宋体"}

[[Client IP address: *client-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_x419795049}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x2058538867}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Your IP address: *your-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_x520641346}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x924027336}[服务器分配给客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Server IP address: *server-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_x774927398}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1773843983}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay agent IP address: *gateway-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_x520706882}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_279648332}[中继的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client hardware address: *client-hardware-address*]{lang="EN-US"}]{#struct_0_x5045_19324_x1973424420}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520510274}[客户端的硬件地址]{style="font-family:宋体"}

[[Server host name: *host-name*]{lang="EN-US"}]{#struct_0_x5045_19324_x1711996611}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x742376167}[服务器的主机名]{style="font-family:宋体"}

[[Boot file name: *file-name*]{lang="EN-US"}]{#struct_0_x5045_19324_1647465828}

[[启动文件名及路径]{style="font-family:宋体"}]{#struct_0_x5045_19324_x520575810}

[[DHCP message type: *type*]{lang="EN-US"}]{#struct_0_x5045_19324_1852482406}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x952943785}[报文的类型，有]{style="font-family:宋体"}[8]{lang="EN-US"}[种类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_x520379202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPDISCOVER]{lang="EN-US"}]{#struct_0_x5045_19324_1386224265}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DHCPOFFER]{lang="EN-US"}]{#struct_0_x5045_19324_868043298}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPREQUEST]{lang="EN-US"}]{#struct_0_x5045_19324_1230415704}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPDECLINE]{lang="EN-US"}]{#struct_0_x5045_19324_x520444738}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_1846095598}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPNAK]{lang="EN-US"}]{#struct_0_x5045_19324_x576526852}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPRELEASE]{lang="EN-US"}]{#struct_0_x5045_19324_x520248130}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPINFORM]{lang="EN-US"}]{#struct_0_x5045_19324_1380492684}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging dhcp relay event]{lang="EN-US"}]{#struct_0_x5045_19324_x675377728}[调试信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1114530037}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_381176130}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_1637910571}

[[Add relay agent option (*byte-count* bytes) to the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x520313666}

[[向报文中添加了]{style="font-family:宋体"}*[byte-count]{lang="EN-US"}*]{#struct_0_x5045_19324_1415143137}[个字节的]{style="font-family:宋体"}[relay agent option]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Can't find an interface to process the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x134043852}

[[找不到处理报文的接口，一般原因为对应的接口没有启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1992709701}[功能]{style="font-family:宋体"}

[[Discard packet with invalid hlen.]{lang="EN-US"}]{#struct_0_x5045_19324_x520772417}

[[丢弃]{style="font-family:宋体"}[hlen]{lang="EN-US"}]{#struct_0_x5045_19324_x918230353}[域不正确的报文]{style="font-family:宋体"}

[[Discard packet with invalid options.]{lang="EN-US"}]{#struct_0_x5045_19324_113103350}

[[丢弃选项内容不正确的报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_674990518}

[[Interface *interface-name* is activated.]{lang="EN-US"}]{#struct_0_x5045_19324_x1501181666}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x520837953}[被激活]{style="font-family:宋体"}

[[Add an IP address *ip-address* to the interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_1050119485}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_1349276967}[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface *interface-name* is deactivated.]{lang="EN-US"}]{#struct_0_x5045_19324_718375032}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x520641345}[被去激活]{style="font-family:宋体"}

[[Delete an IP address *ip-address* from the interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x923830728}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x1439759906}[删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface *interface-name* is deleted.]{lang="EN-US"}]{#struct_0_x5045_19324_x506064998}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x520706881}[被删除]{style="font-family:宋体"}

[[The MAC address of interface *interface-name* is changed..]{lang="EN-US"}]{#struct_0_x5045_19324_279844940}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x5045_19324_214577980}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址改变]{style="font-family:宋体"}

[[The packet is a response for refreshing client information.]{lang="EN-US"}]{#struct_0_x5045_19324_x520510273}

[[收到的报文是用户地址表项刷新应答报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1711668931}

[[The packet is neither BOOTPREPLY nor BOOTPREQUEST.]{lang="EN-US"}]{#struct_0_x5045_19324_550842723}

[[收到的报文即不是请求报文也不是应答报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_x423726787}

[[The received DHCP packet was dropped because it was sent by the receiving relay agent.]{lang="EN-US"}]{#struct_0_x5045_19324_x520575809}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1851892583}[中继收到自己发送的报文后，丢弃该报文]{style="font-family:宋体"}

[[Discard the packet containing option 82 according to the relay information strategy.]{lang="EN-US"}]{#struct_0_x5045_19324_1526020827}

[[由于携带中继信息选项，根据]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x520379201}[中继信息处理策略，丢弃该报文]{style="font-family:宋体"}

[[Source MAC check failed.]{lang="EN-US"}]{#struct_0_x5045_19324_1386289801}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x5045_19324_x1009301641}[地址检测失败]{style="font-family:宋体"}

[[Detect unknown interface event *event* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x520444737}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_1846816494}[检测到不支持的接口事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Detect unknown IP address event *event* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_1766033203}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x520248129}[检测到不支持的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[The received DHCP packet was dropped because it has traversed a maximum of 16 relay agents]{lang="EN-US"}]{#struct_0_x5045_19324_1380033931}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x274070824}[中继收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文达到最大跳数]{style="font-family:宋体"}[16]{lang="EN-US"}[，丢弃该报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging dhcp relay error]{lang="EN-US"}]{#struct_0_x5045_19324_x1231093347}[调试信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1120971685}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_1720170549}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x520313665}

[[DHCP is not enabled.]{lang="EN-US"}]{#struct_0_x5045_19324_1414946529}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_987819314}[功能未使能]{style="font-family:宋体"}

[[Error occurs when calculation the value of option *option-code*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1691367537}

[[计算选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x5045_19324_1130101560}[的选项值出错]{style="font-family:宋体"}

[[Failed to get IP address of interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x888496029}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_1045311527}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to process relay agent option.]{lang="EN-US"}]{#struct_0_x5045_19324_1362278550}

[[处理选项]{style="font-family:宋体"}[relay agent option]{lang="EN-US"}]{#struct_0_x5045_19324_x261443783}[失败]{style="font-family:宋体"}

[[Failed to send packet.]{lang="EN-US"}]{#struct_0_x5045_19324_410943261}

[[报文发送失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_x115923402}

[[Relay agent option (*option-length* bytes) wasn't added to the packet, because there's no enough space in the packet ]{lang="EN-US"}]{#struct_0_x5045_19324_1045245991}

[[报文没有足够的空间存储长度为]{style="font-family:宋体"}*[option-length]{lang="EN-US"}*]{#struct_0_x5045_19324_1031005758}[字节的]{style="font-family:宋体"}[relay agent option]{lang="EN-US"}[选项。忽略]{style="font-family:宋体"}[relay agent option]{lang="EN-US"}[选项，不将其添加到报文中]{style="font-family:宋体"}

[[Malformed packet dhcp:]{lang="EN-US"}]{#struct_0_x5045_19324_10498851}

[[option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_x5045_19324_x1263020480}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_11088674}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[The number of dynamic client entries has reached the maximum.]{lang="EN-US"}]{#struct_0_x5045_19324_2074136087}

[[动态用户地址表项达到最大值]{style="font-family:宋体"}]{#struct_0_x5045_19324_x365632561}

[[The number of temporary client entries has reached the maximum.]{lang="EN-US"}]{#struct_0_x5045_19324_1045442599}

[[临时用户地址表项达到最大值]{style="font-family:宋体"}]{#struct_0_x5045_19324_1759468067}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5045_19324_2077935970}

[[\# DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_279938311}[客户端通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获得]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。打开]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继的所有调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_x5045_19324_1045573671}

[Current terminal monitor is on.]{lang="EN-US"}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> debugging dhcp relay all]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 25 11:36:20:913 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}

[From 0.0.0.0 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554434]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPDISCOVER (1)]{lang="EN-US"}

[\*Mar 25 11:36:20:916 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}

[To 2.0.0.2 port 67, interface is selected by routing table]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 1, Transaction ID: 33554434]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPDISCOVER (1)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x1387344237}*[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[请求报文，并向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.0.0.2]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器转发该报文。]{style="font-family:宋体"}*

[[\*Mar 25 11:36:21:430 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}]{#struct_0_x5045_19324_1045704743}

[From 2.0.0.2 port 67, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 1, Transaction ID: 33554434]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPOFFER (2)]{lang="EN-US"}

[\*Mar 25 11:36:21:432 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}

[To 1.0.0.10 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554434]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPOFFER (2)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_987001101}*[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[DHCP-OFFER]{lang="EN-US"}[响应报文，并广播发送该报文。]{style="font-family:宋体"}*

[[\*Mar 25 11:36:22:378 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}]{#struct_0_x5045_19324_1045639207}

[From 0.0.0.0 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554435]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPREQUEST (3)]{lang="EN-US"}

[\*Mar 25 11:36:22:385 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}

[To 2.0.0.2 port 67, interface is selected by routing table]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 1, Transaction ID: 33554435]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPREQUEST (3)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x624206585}*[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端发来的]{style="font-family:宋体"}[DHCP-REQUESET]{lang="EN-US"}[请求报文，并向]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.0.0.2]{lang="EN-US"}[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器转发该报文。]{style="font-family:宋体"}*

[[\*Mar 25 11:36:22:390 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}]{#struct_0_x5045_19324_1045835815}

[From 2.0.0.2 port 67, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 1, Transaction ID: 33554435]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPACK (5)]{lang="EN-US"}

[\*Mar 25 11:36:22:393 2011 Sysname DHCPR/7/PACKET:]{lang="EN-US"}

[To 1.0.0.10 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554435]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 1.0.0.1]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPACK (5)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x922622724}*[中继接收到]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器发来的]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[响应报文，并广播发送该报文。]{style="font-family:宋体"}*

::: {#-209254234 .myid}
[]{#_Toc404786111}[]{#struct_0_x5045_19324_1796204678}[]{#_Toc205700592}[]{#_Toc205697805}

**DHCP \-- DHCP调试命令 \-- debugging dhcp server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1638716579}

[**[debugging dhcp server]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_1243669718}

[**[undo debugging dhcp server]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_923950342}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5045_19324_184985401}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5045_19324_x758157215}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1360608825}

[[network-admin]{lang="EN-US"}]{#struct_0_x5045_19324_x1188722844}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5045_19324_1210893656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x147151281}

[**[all]{lang="EN-US"}**]{#struct_0_x5045_19324_x1696037538}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x5045_19324_1243079895}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5045_19324_1348689216}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x5045_19324_x1670292218}[：表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5045_19324_1181798953}

[**[debugging dhcp server]{lang="EN-US"}**]{#struct_0_x5045_19324_x1664822722}[命令用来打开]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}**[undo debugging dhcp server]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x822385131}[服务器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging dhcp server packet]{lang="EN-US"}]{#struct_0_x5045_19324_x1600347351}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1952432023}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_x892308189}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_1763868916}

[[From *ip-address*:*port*]{lang="EN-US"}]{#struct_0_x5045_19324_1243145431}

[[接收报文的源地址和端口号]{style="font-family:宋体"}]{#struct_0_x5045_19324_958195173}

[[To *ip-address*:*port*]{lang="EN-US"}]{#struct_0_x5045_19324_x1986196738}

[[发送报文的目的地址和端口号]{style="font-family:宋体"}]{#struct_0_x5045_19324_940989534}

[[interface *interface-name*]{lang="EN-US"}]{#struct_0_x5045_19324_139430277}

[[接收或发送报文的接口]{style="font-family:宋体"}]{#struct_0_x5045_19324_755855257}

[[Message type: *message-type*]{lang="EN-US"}]{#struct_0_x5045_19324_1514545610}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1243210967}[报文的操作类型，有两种：]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[和]{style="font-family:宋体"}[DHCP-REPLY]{lang="EN-US"}

[[Hardware type: *hardware-type*]{lang="EN-US"}]{#struct_0_x5045_19324_224085018}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1076180565}[客户端的硬件类型]{style="font-family:宋体"}

[[Hardware address length: *length*]{lang="EN-US"}]{#struct_0_x5045_19324_x493865750}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1723761781}[客户端的硬件地址长度]{style="font-family:宋体"}

[[Hops: *hops*]{lang="EN-US"}]{#struct_0_x5045_19324_1243276503}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x974616458}[报文经过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继到服务器的跳数]{style="font-family:宋体"}

[[Transaction ID: *transaction-ID*]{lang="EN-US"}]{#struct_0_x5045_19324_693419622}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x229437955}[客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程]{style="font-family:宋体"}

[[Seconds: *seconds*]{lang="EN-US"}]{#struct_0_x5045_19324_1973783744}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1242817751}[客户端从开始申请到当前经过的时间，目前没有使用，固定为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Broadcast flag: *flag*]{lang="EN-US"}]{#struct_0_x5045_19324_209779658}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1353697989}[广播标记：]{style="font-family:宋体"}[1]{lang="EN-US"}[为广播，]{style="font-family:宋体"}[0]{lang="EN-US"}[为单播]{style="font-family:宋体"}

[[Client IP address: *client-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_850857687}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1234426270}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Your IP address: *your-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_1242883287}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_946392635}[服务器分配给客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Server IP address: *server-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_133836388}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1489537489}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Relay agent IP address: *gateway-ip*]{lang="EN-US"}]{#struct_0_x5045_19324_1242948823}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_2128209797}[中继的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client hardware address: *client-hardware-address*]{lang="EN-US"}]{#struct_0_x5045_19324_345850009}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1306664173}[客户端的硬件地址]{style="font-family:宋体"}

[[Server host name: *host-name*]{lang="EN-US"}]{#struct_0_x5045_19324_278918669}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1243014359}[服务器的主机名]{style="font-family:宋体"}

[[Boot file name: *file-name*]{lang="EN-US"}]{#struct_0_x5045_19324_x955158163}

[[启动文件名及路径]{style="font-family:宋体"}]{#struct_0_x5045_19324_x187787560}

[[DHCP message type: *type*]{lang="EN-US"}]{#struct_0_x5045_19324_x137583908}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1243604183}[报文的类型，有]{style="font-family:宋体"}[8]{lang="EN-US"}[种类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BOOTP]{lang="EN-US"}]{#struct_0_x5045_19324_x570265296}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPDISCOVER]{lang="EN-US"}]{#struct_0_x5045_19324_x1356505178}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPOFFER]{lang="EN-US"}]{#struct_0_x5045_19324_1525122536}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPREQUEST]{lang="EN-US"}]{#struct_0_x5045_19324_1243669719}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[DHCPDECLINE]{lang="EN-US"}]{#struct_0_x5045_19324_923884806}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPACK]{lang="EN-US"}]{#struct_0_x5045_19324_2079316105}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPNAK]{lang="EN-US"}]{#struct_0_x5045_19324_x1050483835}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPRELEASE]{lang="EN-US"}]{#struct_0_x5045_19324_x1485803457}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DHCPINFORM]{lang="EN-US"}]{#struct_0_x5045_19324_x1955855637}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging dhcp server event]{lang="EN-US"}]{#struct_0_x5045_19324_169170422}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1949486154}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_2078354101}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_1671625295}

[[Add a conflict IP *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_250385054}

[[添加冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485737921}

[[Can't find an interface to process the packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x748728503}

[[找不到处理报文的接口，一般原因为对应的接口没有启用]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1579136584}[功能]{style="font-family:宋体"}

[[Client was rebooted.]{lang="EN-US"}]{#struct_0_x5045_19324_1984491649}

[[客户端重启。收到客户端]{style="font-family:宋体"}[DISCOVER]{lang="EN-US"}]{#struct_0_x5045_19324_1665002373}[报文时，如果已经给该客户端分配过租约，且该租约有效，则判断为该客户端重启]{style="font-family:宋体"}

[[Client is rebinding its lease.]{lang="EN-US"}]{#struct_0_x5045_19324_x1294516984}

[[客户端续约]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1485672385}

[[Client is renewing its lease.]{lang="EN-US"}]{#struct_0_x5045_19324_1389583591}

[[客户端续约]{style="font-family:宋体"}]{#struct_0_x5045_19324_x2007760323}

[[The client selected another server.]{lang="EN-US"}]{#struct_0_x5045_19324_x199208738}

[[客户端选用了其他]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x2084339544}[服务器分配的地址]{style="font-family:宋体"}

[[The client selected the local server.]{lang="EN-US"}]{#struct_0_x5045_19324_x1849234705}

[[客户端选用了本服务器分配的地址]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1485606849}

[[Sent DHCPACK to *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_x823156107}

[[向地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_1511135135}[回复]{style="font-family:宋体"}[DHCPACK]{lang="EN-US"}[应答]{style="font-family:宋体"}

[[No requested address specified in the DHCPDECLINE.]{lang="EN-US"}]{#struct_0_x5045_19324_x1697029417}

[[DHCP-DECLINE]{lang="EN-US"}]{#struct_0_x5045_19324_22117625}[报文中没有指定请求的地址]{style="font-family:宋体"}

[[The server identifier in the DHCPDECLINE is different from that of the local server.]{lang="EN-US"}]{#struct_0_x5045_19324_x1486065601}

[[DHCP-DECLINE]{lang="EN-US"}]{#struct_0_x5045_19324_x17557562}[报文中的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[与本地服务器的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[不同]{style="font-family:宋体"}

[[Add conflict IP *ip-address* failed, because the number of conflict IP addresses has reached the maximum.]{lang="EN-US"}]{#struct_0_x5045_19324_1755406383}

[[添加冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x274110222}[失败。原因为冲突地址数量达到系统上限]{style="font-family:宋体"}

[[Add conflict IP *ip-address* failed, because there is no matching lease.]{lang="EN-US"}]{#struct_0_x5045_19324_x80150022}

[[添加冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1486000065}[失败。原因为没有找到对应的租约]{style="font-family:宋体"}

[[Adding conflict IP *ip-address* is ignored, because the declined IP address is static.]{lang="EN-US"}]{#struct_0_x5045_19324_1059527186}

[[添加冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1885604807}[被忽略。原因为请求的地址为静态绑定的地址]{style="font-family:宋体"}

[[Added conflict IP *ip-address* successfully.]{lang="EN-US"}]{#struct_0_x5045_19324_x2074427565}

[[添加的冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_576890218}[成功]{style="font-family:宋体"}

[[Ignored the DHCPINFORM, because the source address of the DHCPINFORM is invalid.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485934529}

[[DHCP-INFORM]{lang="EN-US"}]{#struct_0_x5045_19324_x1251562899}[被忽略。原因是报文的源地址无效]{style="font-family:宋体"}

[[The DHCPRELEASE specified requested address option.]{lang="EN-US"}]{#struct_0_x5045_19324_1007299286}

[[DHCP-RELEASE]{lang="EN-US"}]{#struct_0_x5045_19324_x1485868993}[报文中携带了请求地址选项。（报文中不应该携带此选项）]{style="font-family:宋体"}

[[The server identifier in the DHCPRELEASE is different from that of the local server.]{lang="EN-US"}]{#struct_0_x5045_19324_1625108022}

[[DHCP-RELEASE]{lang="EN-US"}]{#struct_0_x5045_19324_419944602}[报文中的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[与本地服务器的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[不同]{style="font-family:宋体"}

[[Release IP *ip-address* failed, because the lease is not found.]{lang="EN-US"}]{#struct_0_x5045_19324_2144415074}

[[释放地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x387130873}[失败。原因是没有找到对应的租约]{style="font-family:宋体"}

[[Released IP *ip-address* successfully.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485279169}

[[成功释放地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1687301075}

[[Receive a DHCPREQUEST message for *request-ip-address*  from *dst-ip-address/interface-name*; server identifier is *server-identifier.*]{lang="EN-US"}]{#struct_0_x5045_19324_196749481}

[[从地址]{style="font-family:宋体"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_58860979}*[、]{style="font-family:宋体"}*[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[收到请求地址]{style="font-family:宋体"}*[request-ip-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文，报文中的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[server-identifier]{lang="EN-US"}*

[[Discard packet with invalid hlen.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485213633}

[[丢弃]{style="font-family:宋体"}[hlen]{lang="EN-US"}]{#struct_0_x5045_19324_1580889602}[字段取值不正确的报文]{style="font-family:宋体"}

[[Discard packet with invalid options.]{lang="EN-US"}]{#struct_0_x5045_19324_x1579530708}

[[丢弃选项内容不正确的报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_425370508}

[[Discard the *message-type* packet: Invalid chaddr.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485803456}

[[丢弃类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x5045_19324_773027718}[的报文。原因是报文]{style="font-family:宋体"}[chaddr]{lang="EN-US"}[域无效]{style="font-family:宋体"}

[[Discard the *message-type* packet: Ignore BOOTP request.]{lang="EN-US"}]{#struct_0_x5045_19324_x1733124727}

[[丢弃类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485737920}[的报文。原因是不处理]{style="font-family:宋体"}[BOOTP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Discard the *message-type* packet: Invalid op field.]{lang="EN-US"}]{#struct_0_x5045_19324_817355438}

[[丢弃类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x5045_19324_344203439}[的报文。原因是报文]{style="font-family:宋体"}[op]{lang="EN-US"}[域无效]{style="font-family:宋体"}

[[Discard the *message-type* packet: Invalid packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x737711889}

[[丢弃类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485672384}[的报文。原因是报文无效]{style="font-family:宋体"}

[[Failed to allocate a lease to client.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485606848}

[[分配租约失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_1905727248}

[[Failed to find lease *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_1043693918}

[[找不到为地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1486065600}[分配的租约]{style="font-family:宋体"}

[[Interface *interface-name* is activated.]{lang="EN-US"}]{#struct_0_x5045_19324_x1583641503}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x758698057}[被激活]{style="font-family:宋体"}

[[Add an IP address *ip-address* to the interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1486000064}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x506556755}[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface *interface-name* is deactivated.]{lang="EN-US"}]{#struct_0_x5045_19324_118610555}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485934528}[被去激活]{style="font-family:宋体"}

[[Delete an IP address *ip-address* from the interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_314521042}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_759053076}[删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*

[[Interface *interface-name* is deleted.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485868992}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_59024081}[被删除]{style="font-family:宋体"}

[[The MAC address of interface *interface-name* is changed.]{lang="EN-US"}]{#struct_0_x5045_19324_2023602309}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_x5045_19324_x1485279168}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址改变]{style="font-family:宋体"}

[[The client identifier of the lease for *ip-address* does not match that in the packet. ]{lang="EN-US"}]{#struct_0_x5045_19324_x121217134}

[[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1032221672}[对应的租约中记录的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[client-identifier]{lang="EN-US"}*[，和报文中的不匹配]{style="font-family:宋体"}

[[No matching network for the client.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485213632}

[[没有找到匹配的网段]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1147993753}

[[Received an ICMP echo reply from *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_599751304}

[[收到地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485803459}[的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[应答]{style="font-family:宋体"}

[[Received a DHCP packet without options.]{lang="EN-US"}]{#struct_0_x5045_19324_x1505516943}

[[收到一个没有选项的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1485737923}[报文]{style="font-family:宋体"}

[[Requested IP *ip-address* is unavailable; Reallocate another IP.]{lang="EN-US"}]{#struct_0_x5045_19324_414070911}

[[报文中请求的地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x194230102}[不能分配，尝试分配其他的地址]{style="font-family:宋体"}

[[Send an ICMP echo request to *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485672387}

[[向地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x1742584291}[发送]{style="font-family:宋体"}[ICMP echo request]{lang="EN-US"}[请求]{style="font-family:宋体"}

[[Discarded the DHCP packet because the op field did not match the DHCP message type option.]{lang="EN-US"}]{#struct_0_x5045_19324_10957601}

[[由于]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1890797807}[报文中的操作类型字段和]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文类型选项不匹配，丢弃该]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The packet *message-type* from *ip-address* is too short.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485606851}

[[来自地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x466860211}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[报文，报文长度过短]{style="font-family:宋体"}

[[Detect unknown interface event *event* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x487972409}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x1486065603}[检测到不支持的接口事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Detect unknown IP address event *event* on interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1180356976}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_x1486000067}[检测到不支持的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Receive a *message-type* message from *dst-ip-address/interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x2072640696}

[[从地址]{style="font-family:宋体"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x442885208}*[、]{style="font-family:宋体"}*[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[收到类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Send a *message-type* message on *dst-ip-address/interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485934531}

[[通过地址]{style="font-family:宋体"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_x895398075}*[、]{style="font-family:宋体"}*[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[发送类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Receive an unknown message (type *message-type*) from *dst-ip-address/interface-name;* Discarded the message.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485868995}

[[从地址]{style="font-family:宋体"}*[dst-ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_818538968}*[、]{style="font-family:宋体"}*[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[收到未知类型的报文，类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[ ]{lang="EN-US"}[。丢弃此报文]{style="font-family:宋体"}

[[Discarded the received DHCP packet because no gateway is configured]{lang="EN-US"}]{#struct_0_x5045_19324_324605696}

[[由于未配置网关，丢弃收到的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_324671232}[报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging dhcp server error]{lang="EN-US"}]{#struct_0_x5045_19324_x1972149977}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1970686332}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_1437637357}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x546326781}

[[No lease contains the source address *ip-address* of the ICMP echo reply.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485279171}

[[收到的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5045_19324_x2043465899}[应答地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[没有绑定任何租约]{style="font-family:宋体"}

[[DHCP is not enabled.]{lang="EN-US"}]{#struct_0_x5045_19324_1142021741}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x657475467}[功能未使能]{style="font-family:宋体"}

[[Error occurs when calculation the value of option *option-code*.]{lang="EN-US"}]{#struct_0_x5045_19324_x160322681}

[[计算选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x5045_19324_x1582036447}[的选项值出错]{style="font-family:宋体"}

[[Failed to receive ICMP echo reply.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485213635}

[[接收]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5045_19324_774320548}[应答报文失败]{style="font-family:宋体"}

[[Failed to allocate a lease: Because the number of leases has reached the maximum.]{lang="EN-US"}]{#struct_0_x5045_19324_468503620}

[[分配租约失败，数量达到上限]{style="font-family:宋体"}]{#struct_0_x5045_19324_153635748}

[[Failed to create timer for ICMP echo request.]{lang="EN-US"}]{#struct_0_x5045_19324_1955575652}

[[创建]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x5045_19324_x2108695196}[请求应答超时定时器失败]{style="font-family:宋体"}

[[Failed to get IP address of interface *interface-name*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1485803458}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_x5045_19324_1223366412}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to send ICMP echo request to *ip-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_x321303858}

[[向地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_x5045_19324_1965514445}[发送]{style="font-family:宋体"}[ICMP echo]{lang="EN-US"}[请求失败]{style="font-family:宋体"}

[[Failed to send packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x989649519}

[[报文发送失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1485737922}

[[Malformed packet dhcp: option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_x5045_19324_10498849}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1832411557}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[No free IP in the address range of the pool or the class.]{lang="EN-US"}]{#struct_0_x5045_19324_1980154852}

[[address range]{lang="EN-US"}]{#struct_0_x5045_19324_x1208661564}[、]{style="font-family:宋体"}[class range]{lang="EN-US"}[中没有可分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[No free IP in the network *network-address*.]{lang="EN-US"}]{#struct_0_x5045_19324_1006095206}

[[网段]{style="font-family:宋体"}*[network-address]{lang="EN-US"}*]{#struct_0_x5045_19324_1380281073}[中没有可分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[No enough space for option *option-code.*]{lang="EN-US"}]{#struct_0_x5045_19324_x1485672386}

[[报文中没有空间存储选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_x5045_19324_x176500350}[的选项内容]{style="font-family:宋体"}

[[No enough space for more options.]{lang="EN-US"}]{#struct_0_x5045_19324_x1068891547}

[[报文中没有空间存储过多的选项]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1700507133}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5045_19324_2065903676}

[[\# ]{lang="EN-US"}]{#struct_0_x5045_19324_670999500}[在设备上配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器功能，打开]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器的所有调试开关。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[中继与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器相连，并申请地址。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_x5045_19324_x1485606850}

[Current terminal monitor is on.]{lang="EN-US"}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> debugging dhcp server all]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 25 11:27:42:714 2011 Sysname DHCPS/7/PACKET:]{lang="EN-US"}

[From 0.0.0.0 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554432]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPDISCOVER (1)]{lang="EN-US"}

[\*Mar 25 11:27:42:714 2011 Sysname DHCPS/7/EVENT: Receive a DHCPDISCOVER message from GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x2032944152}*[服务器收到一个]{style="font-family:宋体"}[DHCPDISCOVER]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[\*Mar 25 11:27:42:717 2011 Sysname DHCPS/7/EVENT: Send an ICMP echo request to 1.0.0.10.]{lang="EN-US"}]{#struct_0_x5045_19324_x1486065602}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_1548526379}*[服务器发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文检测地址]{style="font-family:宋体"}[1.0.0.10]{lang="EN-US"}[是否被占用。]{style="font-family:宋体"}*

[[\*Mar 25 11:27:43:228 2011 Sysname DHCPS/7/EVENT: Send a DHCPOFFER message on GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x5045_19324_x1732147315}

[\*Mar 25 11:27:43:233 2011 Sysname DHCPS/7/PACKET:]{lang="EN-US"}

[To 1.0.0.10 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554432]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPOFFER (2)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x2096696386}*[服务器发送]{style="font-family:宋体"}[DHCP-OFFER]{lang="EN-US"}[应答报文。]{style="font-family:宋体"}*

[[\*Mar 25 11:27:43:246 2011 Sysname DHCPS/7/PACKET:]{lang="EN-US"}]{#struct_0_x5045_19324_x1486000066}

[From 0.0.0.0 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REQUEST (1)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554433]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 0.0.0.0]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPREQUEST (3)]{lang="EN-US"}

[\*Mar 25 11:27:43:247 2011 Sysname DHCPS/7/EVENT: Receive a DHCPREQUEST message for 1.0.0.10 from GigabitEthernet1/0/1; The server identifier is 1.0.0.1.]{lang="EN-US"}

[\*Mar 25 11:27:43:249 2011 Sysname DHCPS/7/EVENT: The client selected the local server.]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_656242659}*[服务器收到一个]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[[%Mar 25 11:27:43:250 2011 Sysname DHCPS/5/ALLOCATE_IP: Server IP = 1.0.0.1, DHCP client IP = 1.0.0.10, DHCP client hardware address = 0014-2226-a962, DHCP client lease = 86400 seconds.]{lang="EN-US"}]{#struct_0_x5045_19324_x851316485}

[\*Mar 25 11:27:43:253 2011 Sysname DHCPS/7/EVENT: Send a DHCPACK message on GigabitEthernet1/0/1.]{lang="EN-US"}

[\*Mar 25 11:27:43:255 2011 Sysname DHCPS/7/PACKET:]{lang="EN-US"}

[To 1.0.0.10 port 68, interface GigabitEthernet1/0/1]{lang="EN-US"}

[    Message type: REPLY (2)]{lang="EN-US"}

[    Hardware type: 1, Hardware address length: 6]{lang="EN-US"}

[    Hops: 0, Transaction ID: 33554433]{lang="EN-US"}

[    Seconds: 0, Broadcast flag: 0]{lang="EN-US"}

[    Client IP address: 0.0.0.0   Your IP address: 1.0.0.10]{lang="EN-US"}

[    Server IP address: 0.0.0.0   Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 0014-2226-a962]{lang="EN-US"}

[    Server host name: not configured]{lang="EN-US"}

[    Boot file name: not configured]{lang="EN-US"}

[    DHCP message type: DHCPACK (5)]{lang="EN-US"}

[*[// DHCP]{lang="EN-US"}*]{#struct_0_x5045_19324_x1485934530}*[服务器发送]{style="font-family:宋体"}[DHCP-ACK]{lang="EN-US"}[应答报文。]{style="font-family:宋体"}*

::: {#1761314864 .myid}
[]{#_Toc404786112}[]{#struct_0_x5045_19324_1700656696}[]{#_Toc318035915}[]{#_Toc205700595}[]{#_Toc205697808}[]{#_Toc288816810}[]{#_Toc288816811}[]{#_Toc288816813}[]{#_Toc288816817}[]{#_Toc288816820}[]{#_Toc288816833}[]{#_Toc288816846}[]{#_Toc288816849}[]{#_Toc288816852}[]{#_Toc288816854}[]{#_Toc288816868}[]{#_Toc288816869}

**DHCP \-- DHCP调试命令 \-- debugging dhcp snooping**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1180955418}

[**[debugging dhcp snooping]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **information** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_1150435359}

[**[undo debugging dhcp snooping]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **information** \| **packet** }]{lang="EN-US"}]{#struct_0_x5045_19324_1178262913}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5045_19324_1834884734}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5045_19324_1920156072}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1709290866}

[[network-admin]{lang="EN-US"}]{#struct_0_x5045_19324_x1487954976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5045_19324_80214945}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1580641668}

[**[all]{lang="EN-US"}**]{#struct_0_x5045_19324_x1968158560}[：表示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x5045_19324_x2093942591}[：表示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x5045_19324_x494319224}[：表示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[information]{lang="EN-US"}**]{#struct_0_x5045_19324_93588563}[：表示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x5045_19324_x349742430}[：表示]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1196021698}

[**[debugging dhcp snooping]{lang="EN-US"}**]{#struct_0_x5045_19324_80804769}[命令用来打开]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging dhcp snooping]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[DHCP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}]{#struct_0_x5045_19324_x716877392}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging dhcp snooping error]{lang="EN-US"}]{#struct_0_x5045_19324_2061649860}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1999801932}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_226236242}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x876728352}

[[Failed to parse DHCP packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x724083257}

[[解析]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_80870305}[报文信息失败]{style="font-family:宋体"}

[[Failed to parse IP information (Perhaps the packet is not a UDP packet).]{lang="EN-US"}]{#struct_0_x5045_19324_90269822}

[[解析]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_1117720138}[信息失败，可能因为不是]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Failed to parse IP header.]{lang="EN-US"}]{#struct_0_x5045_19324_x198769465}

[[解析]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_650579155}[报文头部信息失败]{style="font-family:宋体"}

[[The packet is not a UDP packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1411152373}

[[此报文不是]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x5045_19324_1646364425}[报文]{style="font-family:宋体"}

[[The packet is a bad UDP packet.]{lang="EN-US"}]{#struct_0_x5045_19324_2012246410}

[[此报文是错误的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x5045_19324_1415766425}[报文]{style="font-family:宋体"}

[[Failed to parse UDP header.]{lang="EN-US"}]{#struct_0_x5045_19324_x570364420}

[[解析]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x5045_19324_990172327}[头部信息失败]{style="font-family:宋体"}

[[L3Output: Failed to parse IP information (Perhaps the packet is not a UDP packet).]{lang="EN-US"}]{#struct_0_x5045_19324_1646429961}

[[监听三层出方向报文：解析]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_x1131258686}[信息失败，可能因为不是]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[L3Output: Failed to parse DHCP packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x1550933768}

[[监听三层出方向报文：解析]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_36414021}[报文信息失败]{style="font-family:宋体"}

[[Failed to send packets. The egress and ingress interfaces are the same *interface-index.*]{lang="EN-US"}]{#struct_0_x5045_19324_51989157}

[[发送报文失败，因为入接口和出接口相同]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1646495497}

[[Failed to send packets. The interface *interface-index* is invalid.]{lang="EN-US"}]{#struct_0_x5045_19324_415425929}

[[发送报文失败，因为接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_2045657222}[无效]{style="font-family:宋体"}

[[Failed to send packets. The interface *interface-index* does not belong to the current VLAN.]{lang="EN-US"}]{#struct_0_x5045_19324_x178261874}

[[发送报文失败，因为接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1646561033}[不属于当前]{style="font-family:宋体"}[vlan]{lang="EN-US"}

[[The interface *interface-index* is an aggregation group member, which can't send the packets.]{lang="EN-US"}]{#struct_0_x5045_19324_2006693838}

[[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_275817231}[是聚合口成员，不能从该接口发送报文]{style="font-family:宋体"}

[[Failed to send packets. The interface *interface-index* is down.]{lang="EN-US"}]{#struct_0_x5045_19324_1732521721}

[[发送报文失败，因为接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1646102281}[是]{style="font-family:宋体"}[down]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Failed to send packets in VLAN (interface is *interface-index*).]{lang="EN-US"}]{#struct_0_x5045_19324_x1515496840}

[[vlan]{lang="EN-US"}]{#struct_0_x5045_19324_x955412544}[内接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[转发报文失败]{style="font-family:宋体"}

[[Successfully sent packets in VLAN (interface is *interface-index*).]{lang="EN-US"}]{#struct_0_x5045_19324_x935392937}

[[vlan]{lang="EN-US"}]{#struct_0_x5045_19324_1646167817}[内接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[转发报文成功]{style="font-family:宋体"}

[[The option field of DHCP packet is too short (The value is *value*).]{lang="EN-US"}]{#struct_0_x5045_19324_1284177070}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1991955751}[报文]{style="font-family:宋体"}[option]{lang="EN-US"}[域太短，值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Packet statistics error: ERROR_NO_ENOUGH_RESOURCE OutBufsize is *size*]{lang="EN-US"}]{#struct_0_x5045_19324_1253553500}

[[获取报文统计信息错误，因为长度不足，长度值为]{style="font-family:宋体"}*[size]{lang="EN-US"}*]{#struct_0_x5045_19324_1646233353}

[[ISSU recovery error (error is *error*).]{lang="EN-US"}]{#struct_0_x5045_19324_x740372607}

[[ISSU]{lang="EN-US"}]{#struct_0_x5045_19324_219621334}[恢复失败]{style="font-family:宋体"}*[error]{lang="EN-US"}*

[[ISSU file saving failed (error is *error*).]{lang="EN-US"}]{#struct_0_x5045_19324_x1564676587}

[[ISSU]{lang="EN-US"}]{#struct_0_x5045_19324_1646298889}[存储文件失败]{style="font-family:宋体"}*[error]{lang="EN-US"}*

[[Opening *filename* failed.]{lang="EN-US"}]{#struct_0_x5045_19324_x1925781273}

[[打开文件]{style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_x5045_19324_867004738}[失败]{style="font-family:宋体"}

[[The length of file header is error (len is *length*).]{lang="EN-US"}]{#struct_0_x5045_19324_1646888713}

[[文件头长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_x5045_19324_x1211570266}[错误]{style="font-family:宋体"}

[[File header error.]{lang="EN-US"}]{#struct_0_x5045_19324_x1517875225}

[[文件头错误]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1859317389}

[[Insufficient storage space.]{lang="EN-US"}]{#struct_0_x5045_19324_1646954249}

[[存储空间不足]{style="font-family:宋体"}]{#struct_0_x5045_19324_1622896710}

[[Failed to get file attribute: fstat *string*]{lang="EN-US"}]{#struct_0_x5045_19324_x211924574}

[[获取文件属性失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646364426}

[[Failed to delete IPCIM entries by VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_x5045_19324_2012180874}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_x520095684}[删除]{style="font-family:宋体"}[vlan(*vlan id*)]{lang="EN-US"}[下的表项]{style="font-family:宋体"}

[[Failed to delete IPCIM entries on interface *interface-index.*]{lang="EN-US"}]{#struct_0_x5045_19324_1646429962}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_x1131324222}[删除接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[下的表项]{style="font-family:宋体"}

[[Failed to delete an IPCIM entry.]{lang="EN-US"}]{#struct_0_x5045_19324_956727273}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_1646495498}[删除一条表项]{style="font-family:宋体"}

[[Failed to synchronize IPCIM results.]{lang="EN-US"}]{#struct_0_x5045_19324_415229321}

[[同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_1014870656}[结束失败]{style="font-family:宋体"}

[[Failed to synchronize IPCIM.]{lang="EN-US"}]{#struct_0_x5045_19324_1646561034}

[[同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_2007152590}[失败]{style="font-family:宋体"}

[[Failed to set rule on the the port *interface-index*.]{lang="EN-US"}]{#struct_0_x5045_19324_1060056537}

[[设置接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x635236497}[规则失败]{style="font-family:宋体"}

[[Failed to set the request rule.]{lang="EN-US"}]{#struct_0_x5045_19324_1646102282}

[[设置请求方向规则失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1515300232}

[[Failed to set the reply rule.]{lang="EN-US"}]{#struct_0_x5045_19324_1478875971}

[[设置应答方向规则失败]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646167818}

[[Failed to send synchronous message to chassis *chassis-number* slot *slot-number*.]{lang="EN-US"}]{#struct_0_x5045_19324_1283587246}

[[发送到框号]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_x5045_19324_1646233354}[，板号]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[.]{lang="EN-US"}[的同步消息失败]{style="font-family:宋体"}

[[Failed to send asynchronous message to chassis *chassis-number* slot *slot-number*.]{lang="EN-US"}]{#struct_0_x5045_19324_x740307071}

[[发送到框号]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_x5045_19324_1787415038}[，板号]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[的异步消息失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging dhcp snooping event]{lang="EN-US"}]{#struct_0_x5045_19324_x583156233}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2002510487}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_1646298890}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x1925322520}

[[Started to delete the running database.]{lang="EN-US"}]{#struct_0_x5045_19324_x1670965818}

[[开始删除正在运行的数据库]{style="font-family:宋体"}]{#struct_0_x5045_19324_1145163070}

[[Started to reset the running database.]{lang="EN-US"}]{#struct_0_x5045_19324_1561448223}

[[开始重置正在运行的数据库]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1068978575}

[[Set global configuration to database *result*.]{lang="EN-US"}]{#struct_0_x5045_19324_1864216623}

[[设置全局配置数据库]{style="font-family:宋体"}*[result]{lang="EN-US"}*]{#struct_0_x5045_19324_1646888714}

[[Deleted global configuration from database *result*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1211897946}

[[删除全局配置数据库]{style="font-family:宋体"}*[result]{lang="EN-US"}*]{#struct_0_x5045_19324_x1272822892}

[[Set interface *interface-index* used configuration database *result.*]{lang="EN-US"}]{#struct_0_x5045_19324_1269909498}

[[设置接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x2037243279}[生效配置数据库]{style="font-family:宋体"}*[result.]{lang="EN-US"}*

[[Deleted interface *interface-index* used configuration database *result.*.]{lang="EN-US"}]{#struct_0_x5045_19324_1646954250}

[[删除接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1623355461}[生效配置数据库]{style="font-family:宋体"}*[result.]{lang="EN-US"}*

[[Set interface *interface-index* unused configuration database *result.*.]{lang="EN-US"}]{#struct_0_x5045_19324_970446387}

[[设置接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x627258255}[未生效配置数据库]{style="font-family:宋体"}*[result.]{lang="EN-US"}*

[[Try to add an IP-MAC entry to the running database.]{lang="EN-US"}]{#struct_0_x5045_19324_312190346}

[[尝试向运行数据库添加]{style="font-family:宋体"}[IP-MAC]{lang="EN-US"}]{#struct_0_x5045_19324_1646364423}[表项]{style="font-family:宋体"}

[[Try to delete an IP-MAC entry from the running database.]{lang="EN-US"}]{#struct_0_x5045_19324_2011853194}

[[尝试从运行数据库删除]{style="font-family:宋体"}[IP-MAC]{lang="EN-US"}]{#struct_0_x5045_19324_x403269164}[表项]{style="font-family:宋体"}

[[Try to delete IP-MAC entries from the running database by interface *interface-index*.]{lang="EN-US"}]{#struct_0_x5045_19324_971901485}

[[尝试向运行数据根据接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1860629789}[删除]{style="font-family:宋体"}[IP-MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Try to move the data from the database *number* to the database *number*.]{lang="EN-US"}]{#struct_0_x5045_19324_1646429959}

[[尝试移动数据库]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1130734399}

[[Try to delete database.]{lang="EN-US"}]{#struct_0_x5045_19324_404219223}

[[尝试删除数据库]{style="font-family:宋体"}]{#struct_0_x5045_19324_x1641069251}

[[Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) to all slots.]{lang="EN-US"}]{#struct_0_x5045_19324_1646495495}

[[开始发送异步消息]{style="font-family:宋体"}[(*DataType*]{lang="EN-US"}]{#struct_0_x5045_19324_415557001}*[，]{style="font-family:宋体"}[OpType]{lang="EN-US"}*[)]{lang="EN-US"}[到所有单板]{style="font-family:
  宋体"}

[[Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) to slot *slot-number*.]{lang="EN-US"}]{#struct_0_x5045_19324_1294012464}

[[开始发送异步消息]{style="font-family:宋体"}[(*DataType*]{lang="EN-US"}]{#struct_0_x5045_19324_x989302915}*[，]{style="font-family:宋体"}[OpType]{lang="EN-US"}*[)]{lang="EN-US"}[到单板]{style="font-family:
  宋体"}*[slot-number]{lang="EN-US"}*[.]{lang="EN-US"}

[[Start to send asynchronous message (DataType: *DataType* OpType: *OpType*) by if *interface-index*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1786881196}

[[开始发送异步消息]{style="font-family:宋体"}[(*DataType*]{lang="EN-US"}]{#struct_0_x5045_19324_1646561031}*[，]{style="font-family:宋体"}[OpType]{lang="EN-US"}*[)]{lang="EN-US"}[到接口]{style="font-family:
  宋体"}*[interface-index]{lang="EN-US"}*[所在板]{style="font-family:宋体"}

[[Start to send synchronous message to slot *slot-number*.]{lang="EN-US"}]{#struct_0_x5045_19324_2006824910}

[[开始发送同步消息到单板]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*]{#struct_0_x5045_19324_x906499890}

[[Set the global rule *rule-id*.]{lang="EN-US"}]{#struct_0_x5045_19324_1646102279}

[[设置全局规则]{style="font-family:宋体"}*[rule-id]{lang="EN-US"}*]{#struct_0_x5045_19324_x1514972539}

[[Set the port *interface-index* rule *rule-id*.]{lang="EN-US"}]{#struct_0_x5045_19324_x477109315}

[[设置接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x298063734}[规则]{style="font-family:宋体"}*[rule-id]{lang="EN-US"}*

[[Set the rate limit.]{lang="EN-US"}]{#struct_0_x5045_19324_1646167815}

[[设置限速]{style="font-family:宋体"}]{#struct_0_x5045_19324_1284308142}

[[Started to synchronize IPCIM.]{lang="EN-US"}]{#struct_0_x5045_19324_89182905}

[[开始同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_x954206669}

[[Finished synchronizing IPCIM.]{lang="EN-US"}]{#struct_0_x5045_19324_1646233351}

[[结束同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_x5045_19324_x740503679}

[[Deleted if *interface-index*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1328440168}

[[删除接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1646298887}[处理]{style="font-family:宋体"}

[[Inactivated if *interface-index*..]{lang="EN-US"}]{#struct_0_x5045_19324_x1925650201}

[[去激活接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x524874005}[处理]{style="font-family:宋体"}

[[Activated if *interface-index*.]{lang="EN-US"}]{#struct_0_x5045_19324_1188704111}

[[激活接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1646888711}[处理]{style="font-family:宋体"}

[[Added port *interface-index* to aggregate interface.]{lang="EN-US"}]{#struct_0_x5045_19324_x1211701338}

[[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x526102115}[加入聚合口处理]{style="font-family:宋体"}

[[Removed port *interface-index* from aggregate interface. ]{lang="EN-US"}]{#struct_0_x5045_19324_1646954247}

[[接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_1623552070}[离开聚合口处理]{style="font-family:宋体"}

[[The slot *slot-number* is inserted.]{lang="EN-US"}]{#struct_0_x5045_19324_965221487}

[[单板]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*]{#struct_0_x5045_19324_1646364424}[插入完成]{style="font-family:宋体"}

[[The number of MAC-PORT entries has reached the maximum. ]{lang="EN-US"}]{#struct_0_x5045_19324_2012311946}

[[MAC-PORT]{lang="EN-US"}]{#struct_0_x5045_19324_x895450270}[表项达到最大值]{style="font-family:宋体"}

[[Successfully added a MAC-port entry (mac is *mac-address*, ifindex is *interface-index*,CVlan is *CVlan*, CSVlan is *CSVlan*, SVlan is *SVlan*, SSVlan is *SSVlan*, MsgType is *MsgType*)]{lang="EN-US"}]{#struct_0_x5045_19324_1646429960}

[[Failed to add a MAC-port entry (mac is *mac-address*, ifindex is *interface-index*, CVlan is *CVlan*, CSVlan is *CSVlan*, SVlan is *SVlan*, SSVlan is *SSVlan*, MsgType is *MsgType*)]{lang="EN-US"}]{#struct_0_x5045_19324_x1131193150}

[[添加]{style="font-family:宋体"}[MAC-PORT]{lang="EN-US"}]{#struct_0_x5045_19324_x1988426423}[表项]{style="font-family:宋体"}[(*mac*]{lang="EN-US"}*[地址，]{style="font-family:宋体"}[interface-index]{lang="EN-US"}*[,]{lang="EN-US"}*[，]{style="font-family:宋体"}[server vlan]{lang="EN-US"}[，]{style="font-family:宋体"}[server second vlan]{lang="EN-US"}[，]{style="font-family:宋体"}[MsgType]{lang="EN-US"}*[)]{lang="EN-US"}[成功]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[[添加]{style="font-family:宋体"}[MAC-PORT]{lang="EN-US"}]{#struct_0_x5045_19324_1646495496}[表项]{style="font-family:宋体"}[(*mac*]{lang="EN-US"}*[地址，]{style="font-family:宋体"}[interface-index]{lang="EN-US"}*[,]{lang="EN-US"}*[，]{style="font-family:宋体"}[server vlan]{lang="EN-US"}[，]{style="font-family:宋体"}[server second vlan]{lang="EN-US"}[，]{style="font-family:宋体"}[MsgType]{lang="EN-US"}*[)]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[The number of packet nodes has reached the maximum.]{lang="EN-US"}]{#struct_0_x5045_19324_415360393}

[[packet]{lang="EN-US"}]{#struct_0_x5045_19324_1862972166}[结点个数超过最大值]{style="font-family:宋体"}

[[Notify user to get *number* packet nodes, the result is *result.*]{lang="EN-US"}]{#struct_0_x5045_19324_x1427620899}

[[通知用户态获取]{style="font-family:宋体"}[packet]{lang="EN-US"}]{#struct_0_x5045_19324_1646561032}[结点]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，结果是]{style="font-family:宋体"}*[result]{lang="EN-US"}*

[[Assign the rate limit to driver: interface *interface-index*, LimitRate *LimitRate*, result *result.*]{lang="EN-US"}]{#struct_0_x5045_19324_2006759374}

[[向驱动下发限速]{style="font-family:宋体"}[(*interface-index*]{lang="EN-US"}]{#struct_0_x5045_19324_1758605506}*[，]{style="font-family:
  宋体"}[LimitRate]{lang="EN-US"}[，]{style="font-family:
  宋体"}[result.]{lang="EN-US"}*[)]{lang="EN-US"}

[[Obtained kernel data: DataType is *DataType*, OperType is *OperType*, ProcResult is *ProcResult*]{lang="EN-US"}]{#struct_0_x5045_19324_1646102280}

[[获取内核态数据]{style="font-family:宋体"}[(*DataType*]{lang="EN-US"}]{#struct_0_x5045_19324_x1515431304}*[，]{style="font-family:宋体"}[OperType]{lang="EN-US"}[，]{style="font-family:宋体"}[ProcResult]{lang="EN-US"}*[)]{lang="EN-US"}

[[Set kernel data: DataType is *DataType*, OperType is *OperType*, ProcResult is *ProcResult*]{lang="EN-US"}]{#struct_0_x5045_19324_x578092835}

[[向内核态下发数据]{style="font-family:宋体"}[(*DataType*]{lang="EN-US"}]{#struct_0_x5045_19324_1646167816}[，]{style="font-family:宋体"}*[OperType]{lang="EN-US"}*[，]{style="font-family:宋体"}*[ProcResult]{lang="EN-US"}*[)]{lang="EN-US"}

[[Responded to bridge MAC change: DEV_EVT_BMAC_CHANGE]{lang="EN-US"}]{#struct_0_x5045_19324_1284242606}

[[响应桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x5045_19324_1646233352}[变化]{style="font-family:宋体"}

[[Child process *number* of parent process *number* exited: exitcode is *exitcode*]{lang="EN-US"}]{#struct_0_x5045_19324_x740438143}

[[父进程]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x5045_19324_936162857}[的子进程]{style="font-family:宋体"}*[number]{lang="EN-US"}*[退出]{style="font-family:宋体"}*[exitcode]{lang="EN-US"}*

[[No MAC-port entry is found when adding a packet node.]{lang="EN-US"}]{#struct_0_x5045_19324_1646298888}

[[添加]{style="font-family:宋体"}[packet]{lang="EN-US"}]{#struct_0_x5045_19324_x1925846809}[结点时，没有找到]{style="font-family:宋体"}[MAC-PORT]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Successfully added a MAC-port entry by packet type *type-id*.]{lang="EN-US"}]{#struct_0_x5045_19324_x337327170}

[[报文]{style="font-family:宋体"}*[type-id]{lang="EN-US"}*]{#struct_0_x5045_19324_1646888712}[添加]{style="font-family:宋体"}[MAC-PORT]{lang="EN-US"}[表项成功]{style="font-family:宋体"}

[[Delete an IP-MAC entry from database *number*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1211504730}

[[从]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x5045_19324_1646954248}[删除一条]{style="font-family:宋体"}[IP-MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Add an IP-MAC entry to database *number*..]{lang="EN-US"}]{#struct_0_x5045_19324_1622831174}

[[向]{style="font-family:宋体"}[DBM]{lang="EN-US"}]{#struct_0_x5045_19324_x213080199}[添加一条]{style="font-family:宋体"}[IP-MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging dhcp snooping information]{lang="EN-US"}]{#struct_0_x5045_19324_1646364421}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1983174929}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_2011984266}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x61683263}

[[Fill circuit-id in padding format *type*:Length is *length*.]{lang="EN-US"}]{#struct_0_x5045_19324_1121184237}

[[以]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x5045_19324_2081055060}[填充方式填充]{style="font-family:宋体"}[circuit id]{lang="EN-US"}[，填充长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*[.]{lang="EN-US"}

[[填充方式如下几种：]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646429957}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[normal]{lang="EN-US"}]{#struct_0_x5045_19324_x1131651903}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[verbose]{lang="EN-US"}]{#struct_0_x5045_19324_1039161840}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[string]{lang="EN-US"}]{#struct_0_x5045_19324_1449107557}

[[Fill remote-id in padding format *type*:Length is *length*..]{lang="EN-US"}]{#struct_0_x5045_19324_1221524661}

[[以]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_x5045_19324_1404788939}[填充方式填充]{style="font-family:宋体"}[remote id]{lang="EN-US"}[，填充长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*[.]{lang="EN-US"}

[[填充方式如下几种：]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646495493}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[normal]{lang="EN-US"}]{#struct_0_x5045_19324_415688073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[sysname]{lang="EN-US"}]{#struct_0_x5045_19324_x42332507}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[string]{lang="EN-US"}]{#struct_0_x5045_19324_334340909}

[[Stripping Option 82 succeeded: offset is *offset*, stripped length is *length*.]{lang="EN-US"}]{#struct_0_x5045_19324_x1623829182}

[[剥离]{style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_x5045_19324_1646561029}[，偏移量]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[，剥离长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Padded packet: padded length is *length*..]{lang="EN-US"}]{#struct_0_x5045_19324_2006300623}

[[填充报文，填充长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*[.]{lang="EN-US"}]{#struct_0_x5045_19324_1404704456}

[[Recalculated IP and UDP checksum.]{lang="EN-US"}]{#struct_0_x5045_19324_x1500449286}

[[重新计算]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5045_19324_546826282}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[校验和]{style="font-family:宋体"}

[[Received packet: Option 82 offset is *offset*, Option 82 handling strategy is *type*.]{lang="EN-US"}]{#struct_0_x5045_19324_1646102277}

[[Option 82]{lang="EN-US"}]{#struct_0_x5045_19324_x1515627899}[在报文中的偏移量是]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[，处理策略是]{style="font-family:宋体"}*[type]{lang="EN-US"}*[，]{style="font-family:宋体"}

[[处理策略：]{style="font-family:宋体"}]{#struct_0_x5045_19324_1400800336}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[replace]{lang="EN-US"}]{#struct_0_x5045_19324_1124999907}[：替换成新的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[内容]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[keep]{lang="EN-US"}]{#struct_0_x5045_19324_1646167813}[：保持现有的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[内容]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[drop]{lang="EN-US"}]{#struct_0_x5045_19324_1283914926}[：删除现有的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[内容]{style="font-family:宋体"}

[ ]{lang="FR"}

[[表1-13 ]{lang="EN-US"}[debugging dhcp snooping packet]{lang="EN-US"}]{#struct_0_x5045_19324_1373522101}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1981004451}[[字段]{style="font-family:黑体"}]{#struct_0_x5045_19324_x569303654}

[[描述]{style="font-family:黑体"}]{#struct_0_x5045_19324_x488145202}

[[Started to parse DHCP option (len is *length*).]{lang="EN-US"}]{#struct_0_x5045_19324_x784561298}

[[开始解析]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1646233349}[报文]{style="font-family:宋体"}[option]{lang="EN-US"}[域，域长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Option *number* is found: the offset is *offset*]{lang="EN-US"}]{#struct_0_x5045_19324_x741027968}

[[选项]{style="font-family:宋体"}*[number]{lang="EN-US"}*]{#struct_0_x5045_19324_x1300444832}[找到，偏移量是]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[Before VLAN mapping: MBUFIfIndex is *MBUFIfIndex*, IfIndex is *interface-index*, InFstVLAN is *InFstVLAN*,InSecVLAN is *InSecVLAN*, OutFstVLAN is *OutFstVLAN*, OutSecVLAN is *OutSecVLAN*]{lang="EN-US"}]{#struct_0_x5045_19324_1227587138}

[[VLAN mapping]{lang="EN-US"}]{#struct_0_x5045_19324_x172507487}[处理前，]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中的接口索引]{style="font-family:宋体"}*[MBUFIfIndex]{lang="EN-US"}*[，接收报文的接口索引]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[,]{lang="EN-US"}[，入方向]{style="font-family:宋体"}[first vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[InFstVLAN]{lang="EN-US"}*[，入方向]{style="font-family:宋体"}[second vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[InSecVLAN]{lang="EN-US"}*[，出方向]{style="font-family:宋体"}[first vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[OutFstVLAN]{lang="EN-US"}*[，出方向]{style="font-family:宋体"}[second vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[OutSecVLAN]{lang="EN-US"}*

[[After VLAN mapping: MBUFIfIndex is *MBUFIfIndex*, IfIndex is *interface-index* InFstVLAN is *InFstVLAN*, InSecVLAN is *InSecVLAN*, OutFstVLAN is *OutFstVLAN*, OutSecVLAN is *OutSecVLAN*]{lang="EN-US"}]{#struct_0_x5045_19324_1646298885}

[[VLAN mapping]{lang="EN-US"}]{#struct_0_x5045_19324_x1925519129}[处理后，]{style="font-family:宋体"}[MBUF]{lang="EN-US"}[中的接口索引]{style="font-family:宋体"}*[MBUFIfIndex]{lang="EN-US"}*[，接收报文的接口索引]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[，入方向]{style="font-family:宋体"}[first vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[InFstVLAN]{lang="EN-US"}*[，入方向]{style="font-family:宋体"}[second vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[InSecVLAN]{lang="EN-US"}*[，出方向]{style="font-family:宋体"}[first vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[OutFstVLAN]{lang="EN-US"}*[，出方向]{style="font-family:宋体"}[second vlan]{lang="EN-US"}[是]{style="font-family:宋体"}*[OutSecVLAN]{lang="EN-US"}*

[[Started to check MAC validity in DHCP packets.]{lang="EN-US"}]{#struct_0_x5045_19324_2035146122}

[[开始检查]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x5045_19324_x1714479359}[有效性]{style="font-family:宋体"}

[[Started to check validity of the DHCP-request-packet.]{lang="EN-US"}]{#struct_0_x5045_19324_1459732181}

[[开始请求方向报文有效性检查]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646888709}

[[The MAC in the DHCP packet doesn\'t match the source MAC in Ethernet header.]{lang="EN-US"}]{#struct_0_x5045_19324_x1212225627}

[[以太帧头的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x5045_19324_145752990}[与]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Invalid packet by request-check.]{lang="EN-US"}]{#struct_0_x5045_19324_x1693690709}

[[通过请求方向报文有效检查，此报文无效]{style="font-family:宋体"}]{#struct_0_x5045_19324_x832843087}

[[Successfully sent packets in VLAN (interface is *interface-index*).]{lang="EN-US"}]{#struct_0_x5045_19324_1646954245}

[[vlan]{lang="EN-US"}]{#struct_0_x5045_19324_1623683142}[内接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*[转发报文成功]{style="font-family:宋体"}

[[Delivered the request packet to CPU, continue]{lang="EN-US"}]{#struct_0_x5045_19324_1325371754}

[[请求方向报文上送本机，继续处理]{style="font-family:宋体"}]{#struct_0_x5045_19324_1674750107}

[[Sent the packet through the trusted port.]{lang="EN-US"}]{#struct_0_x5045_19324_1646364422}

[[从信任端口转发报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_2011918730}

[[Sent the cast packet, through the trusted port.]{lang="EN-US"}]{#struct_0_x5045_19324_x824271824}

[[广播报文从信任端口转发]{style="font-family:宋体"}]{#struct_0_x5045_19324_1397978447}

[[Failed to send a DHCP packet.]{lang="EN-US"}]{#struct_0_x5045_19324_x870010190}

[[发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1646429958}[报文失败]{style="font-family:宋体"}

[[L3Output: Started to process DHCP packets.]{lang="EN-US"}]{#struct_0_x5045_19324_x1130668863}

[[三层出方向开始处理报文]{style="font-family:宋体"}]{#struct_0_x5045_19324_430904329}

[[L3Output: Ignored request packets.]{lang="EN-US"}]{#struct_0_x5045_19324_x1053582763}

[[三层出方向请求报文不处理]{style="font-family:宋体"}]{#struct_0_x5045_19324_1646495494}

[[Started to process DHCP packets.]{lang="EN-US"}]{#struct_0_x5045_19324_415491465}

[[开始处理]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_x1428931500}[报文]{style="font-family:宋体"}

[[The DHCP packet is sent to slot *slot-number.*]{lang="EN-US"}]{#struct_0_x5045_19324_1245698883}

[[DHCP]{lang="EN-US"}]{#struct_0_x5045_19324_1646561030}[报文透传主用板]{style="font-family:宋体"}*[slot-number.]{lang="EN-US"}*

[[Sent a DHCP reply packet to DHCP relay agent.]{lang="EN-US"}]{#struct_0_x5045_19324_2006890446}

[[发送给]{style="font-family:宋体"}[DHCP relay]{lang="EN-US"}]{#struct_0_x5045_19324_1003099749}[的报文]{style="font-family:宋体"}

[[Received packets from interface *interface-index*]{lang="EN-US"}]{#struct_0_x5045_19324_1616395617}

[[            Transaction ID: *Transaction ID*]{lang="EN-US"}]{#struct_0_x5045_19324_1646102278}

[[            Client IP address: *ip-address* Your IP address: *ip-address*]{lang="EN-US"}]{#struct_0_x5045_19324_x1514907003}

[[            Relay agent IP address: *ip-address*]{lang="EN-US"}]{#struct_0_x5045_19324_293031935}

[[            Client hardware address: *hardware address*]{lang="EN-US"}]{#struct_0_x5045_19324_1646167814}

[[            Request IP address: *ip-address* Server ID: *server-id*]{lang="EN-US"}]{#struct_0_x5045_19324_1284373678}

[[            Client First VLAN ID: *vlan-id* Client Second VLAN ID: *vlan-id*]{lang="EN-US"}]{#struct_0_x5045_19324_48169721}

[[            Server First VLAN ID: *vlan-id* Server Second VLAN ID: *vlan-id*]{lang="EN-US"}]{#struct_0_x5045_19324_x1944843386}

[[            DHCP message type: *message-type*\"]{lang="EN-US"}]{#struct_0_x5045_19324_1646233350}

[[从接口]{style="font-family:宋体"}*[interface-index]{lang="EN-US"}*]{#struct_0_x5045_19324_x740569215}[接收到报文，报文中的]{style="font-family:宋体"}*[Transaction ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}[，]{style="font-family:宋体"}*[服务器分配客户端的]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，中继]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，客户端硬件地址]{style="font-family:宋体"}*[hardware address]{lang="EN-US"}*[，请求的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，服务器]{style="font-family:宋体"}[ID*server-id*]{lang="EN-US"}[，客户端第一层]{style="font-family:宋体"}[VLAN ID *vlan-id*]{lang="EN-US"}[，客户端第]{style="font-family:宋体"}[2]{lang="EN-US"}[层]{style="font-family:宋体"}[VLAN ID *vlan-id*]{lang="EN-US"}[。服务器第一层]{style="font-family:宋体"}[VLAN ID*vlan-id*]{lang="EN-US"}[，服务器第]{style="font-family:宋体"}[2]{lang="EN-US"}[层]{style="font-family:宋体"}[VLAN ID *vlan-id*]{lang="EN-US"}[。]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文类型]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5045_19324_935209632}

[[\#]{lang="EN-US"}]{#struct_0_x5045_19324_x680884487}[打开]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[上的所有调试信息开关，]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[客户端从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获得]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[DHCP Snooping]{lang="EN-US"}[设备连接在客户端和服务器之间进行侦听。]{style="font-family:宋体"}

[[\<Sysname\> debugging dhcp snooping all]{lang="EN-US"}]{#struct_0_x5045_19324_1646298886}

[\<Sysname\> terminal monitor]{lang="EN-US"}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.     ]{lang="EN-US"}

[*[// DHCP Snooping]{lang="EN-US"}*]{#struct_0_x5045_19324_x1925715737}*[开始处理报文。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found]{lang="EN-US"}]{#struct_0_x5045_19324_697014574}[：]{style="font-family:宋体"}[the offset is 4.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_980055286}*[解析报文，报文携带]{style="font-family:宋体"}[option53]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 12 is found]{lang="EN-US"}]{#struct_0_x5045_19324_1549490227}[：]{style="font-family:宋体"}[the offset is 7.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_940655443}*[解析报文，报文携带]{style="font-family:宋体"}[option12]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 50 is found: the offset is 25]{lang="EN-US"}]{#struct_0_x5045_19324_x1224600614}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_1104141027}*[解析报文，报文携带]{style="font-family:宋体"}[option50]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 55 is found]{lang="EN-US"}]{#struct_0_x5045_19324_x1794729884}[：]{style="font-family:宋体"}[the offset is 31]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_1646888710}*[解析报文，报文携带]{style="font-family:宋体"}[option55]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 57 is found]{lang="EN-US"}]{#struct_0_x5045_19324_x1211635802}[：]{style="font-family:宋体"}[the offset is 40]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_923337273}*[解析报文，报文携带]{style="font-family:宋体"}[option57]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 60 is found]{lang="EN-US"}]{#struct_0_x5045_19324_586423423}[：]{style="font-family:宋体"}[the offset is 44]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_1582830963}*[解析报文，报文携带]{style="font-family:宋体"}[option60]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Option 61 is found]{lang="EN-US"}]{#struct_0_x5045_19324_x1706592657}[：]{style="font-family:宋体"}[the offset is 71]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x5045_19324_326379292}*[解析报文，报文携带]{style="font-family:宋体"}[option61]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0]{lang="EN-US"}]{#struct_0_x5045_19324_1088107681}

[, IfIndex is 4, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0]{lang="EN-US"}

[*[// VLAN mapping]{lang="EN-US"}*]{#struct_0_x5045_19324_1646954246}*[处理前，报文携带的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等信息。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,]{lang="EN-US"}]{#struct_0_x5045_19324_1623486534}

[ IfIndex is 4, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is0]{lang="EN-US"}

[*[// VLAN mapping]{lang="EN-US"}*]{#struct_0_x5045_19324_1330137640}*[处理后，报文携带的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等信息。]{style="font-family:宋体"}*

[[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 105)]{lang="EN-US"}]{#struct_0_x5045_19324_x726485178}

*[// ]{lang="EN-US"}[解析报文的]{style="font-family:
宋体"}[option]{lang="EN-US"}[域。]{style="font-family:
宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET:]{lang="EN-US"}

[Receiveed packets from interface Ten-GigabitEthernet1/0/3]{lang="EN-US"}

[    Transaction ID: 9e604c7b]{lang="EN-US"}

[    Client IP address: 0.0.0.0            Your IP address: 0.0.0.0]{lang="EN-US"}

[    Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000f-e25d-f27c]{lang="EN-US"}

[    Request IP address: 9.2.2.2           Server ID: N/A]{lang="EN-US"}

[    Client First VLAN ID: 1               Client Second VLAN ID: N/A]{lang="EN-US"}

[    Server First VLAN ID: 1               Server Second VLAN ID: N/A]{lang="EN-US"}

[    DHCP message type: DHCPDISCOVER]{lang="EN-US"}

*[// DHCP Snooping]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/KENTRY: Successfully added a MAC-port entry(mac is 000f-e25d-f27c, ifindex is 4, CVlan is 1, CSVlan is 65535, SVlan is 1, SSVlan is 0, MsgType is 1)     ]{lang="EN-US"}

*[// ]{lang="EN-US"}[添加]{style="font-family:
宋体"}[MAC-PORT]{lang="EN-US"}[表项。]{style="font-family:
宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/6/PACKET: Successfully added a MAC-port entry ]{lang="EN-US"}

[by packet type(1).]{lang="EN-US"}

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Fill circuit-id in padding format ]{lang="EN-US"}

[normal]{lang="EN-US"}[：]{style="font-family:
宋体"} [Length is 8.]{lang="EN-US"}

*[// ]{lang="EN-US"}[填充]{style="font-family:
宋体"}[option82]{lang="EN-US"}[的]{style="font-family:
宋体"}[circuit id]{lang="EN-US"}[。]{style="font-family:
宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Fill remote-id in padding format ]{lang="EN-US"}

[normal]{lang="EN-US"}[：]{style="font-family:
宋体"} [Length is 10.]{lang="EN-US"}

*[// ]{lang="EN-US"}[填充]{style="font-family:
宋体"}[option82]{lang="EN-US"}[的]{style="font-family:
宋体"}[remote id]{lang="EN-US"}[。]{style="font-family:
宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.       ]{lang="EN-US"}

*[// ]{lang="EN-US"}[计算]{style="font-family:
宋体"}[IP]{lang="EN-US"}[头和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[头校验和。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/INFO: Received packet Option 82 offset is ]{lang="EN-US"}

[0, option 82 strategy is Replace.]{lang="EN-US"}

*[// ]{lang="EN-US"}[接收的报文携带]{style="font-family:
宋体"}[option 82]{lang="EN-US"}[，对此报文的处理策略]{style="font-family:宋体"}[replace]{lang="EN-US"}[。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:872 2011 Sysname DHCPSP4/7/PACKET:]{lang="EN-US"}

*[// ]{lang="EN-US"}[从]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[下的]{style="font-family:宋体"}[e1/0/4]{lang="EN-US"}[接口转发报文。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: Successfully sent packet in vlan ]{lang="EN-US"}

[(interface is 5)                                                 \
]{lang="EN-US"}*[// ]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[转发报文成功。]{style="font-size:10.5pt;font-family:宋体"}*

[\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: Failed to send packets. The interfa]{lang="EN-US"}

[ce(12) is down.]{lang="EN-US"}

*[// ]{lang="EN-US"}[从接口索引为]{style="font-family:
宋体"}[12]{lang="EN-US"}[的接口转发报文失败，因为此接口状态]{style="font-family:
宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:873 2011 Sysname DHCPSP4/6/PACKET: BroadCast packet, Trans packet to t]{lang="EN-US"}

[rust port and continue]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 7.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 51 is found, the offset is 13]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 58 is found, the offset is 19]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 59 is found, the offset is 25]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 1 is found, the offset is 31.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len=64).]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Option 82 is found, the offset is 37]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0, IfIndex is 5, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MacPort ifSendIndex]{lang="EN-US"}

[is 4, CVlan is 1, CSVlan is 65535, SSVlan is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MarkFlag is 0, OutPort]{lang="EN-US"}

[Index is 4, OutFstVLAN is 1]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,]{lang="EN-US"}

[ IfIndex is 5, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/PACKET:]{lang="EN-US"}

[Receive packets from interface Ten-GigabitEthernet1/0/4]{lang="EN-US"}

[    Transaction ID: 9e604c7b]{lang="EN-US"}

[    Client IP address: 0.0.0.0            Your IP address: 9.2.2.2]{lang="EN-US"}

[    Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000f-e25d-f27c]{lang="EN-US"}

[    Request IP address: N/A               Server ID: 9.0.0.1]{lang="EN-US"}

[    Client First VLAN ID: 1               Client Second VLAN ID: N/A]{lang="EN-US"}

[    Server First VLAN ID: 1               Server Second VLAN ID: N/A]{lang="EN-US"}

[    DHCP message type: DHCPOFFER]{lang="EN-US"}

*[// DHCP Snooping]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[DHCP-OFFER]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Stripping Option 82 succeeded: offset is ]{lang="EN-US"}

[319, stripped length is 20.]{lang="EN-US"}

*[// ]{lang="EN-US"}[剥离]{style="font-family:
宋体"}[option82]{lang="EN-US"}[选项。]{style="font-family:
宋体"}*

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Padded packet: padded length is 20.]{lang="EN-US"}

[\*Jan  1 00:43:17:881 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 12 is found, the offset is 7.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 111)]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 50 is found, the offset is 25]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 31]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 55 is found, the offset is 37]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 57 is found, the offset is 46]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 60 is found, the offset is 50]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Option 61 is found, the offset is 77]{lang="EN-US"}

[.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0]{lang="EN-US"}

[, IfIndexis 4, InFstVLANis 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,]{lang="EN-US"}

[ IfIndex is 4, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/KENTRY: Successfully added a MAC-port(mac is 000f]{lang="EN-US"}

[-e25d-f27c, ifindex is 4, CVlan is 1, CSVlan is 65535, SVlan is 1, SSVlan is 0, MsgType is 3)]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/6/PACKET: Successfully added a MAC-port entry ]{lang="EN-US"}

[by packet type(3).]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/PACKET:]{lang="EN-US"}

[Receiveed packets from interface Ten-GigabitEthernet1/0/3]{lang="EN-US"}

[    Transaction ID: 9e604c7b]{lang="EN-US"}

[    Client IP address: 0.0.0.0            Your IP address: 0.0.0.0]{lang="EN-US"}

[    Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000f-e25d-f27c]{lang="EN-US"}

[    Request IP address: 9.2.2.2           Server ID: 9.0.0.1]{lang="EN-US"}

[    Client First VLAN ID: 1               Client Second VLAN ID: N/A]{lang="EN-US"}

[    Server First VLAN ID: 1               Server Second VLAN ID: N/A]{lang="EN-US"}

[    DHCP message type: DHCPREQUEST]{lang="EN-US"}

*[// DHCP Snooping]{lang="EN-US"}[收到一个]{style="font-family:宋体"}[DHCP-REQUEST]{lang="EN-US"}[报文。]{style="font-family:宋体"}*

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Fill circuit-id in padding format ]{lang="EN-US"}

[ normal:Length is 8.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Fill remote-id in padding format ]{lang="EN-US"}

[normal: Length is 10.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.]{lang="EN-US"}

[\*Jan  1 00:43:17:884 2011 Sysname DHCPSP4/7/INFO: Receiveed packet Option 82 offset is ]{lang="EN-US"}

[0, Option 82 strategy is Replace.]{lang="EN-US"}

[\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/KENTRY: Notify user to get 1 packet node]{lang="EN-US"}

[s, the result is 0.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: Successfully Sent packets in vlan (interface is 5).]{lang="EN-US"}

[\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: Failed to send packets. The interfa]{lang="EN-US"}

[ce(12) is down.]{lang="EN-US"}

[\*Jan  1 00:43:17:885 2011 Sysname DHCPSP4/6/PACKET: BroadCast packet, Trans packet to t]{lang="EN-US"}

[rust port and continue]{lang="EN-US"}

[\*Jan  1 00:43:17:886 2011 Sysname DHCPSP4/6/2KNL: Started to send synchronous message ]{lang="EN-US"}

[to slot(1).]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 53 is found, the offset is 4.]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 54 is found, the offset is 7.]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 51 is found, the offset is 13]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 58 is found, the offset is 19]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 59 is found, the offset is 25]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 1 is found, the offset is 31.]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Option 82 is found, the offset is 37]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET: Started to process DHCP packets.]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET: Started to parse DHCP option(len is 64).]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: Before VLAN mapping: MBUFIfIndex is 0]{lang="EN-US"}

[, IfIndex is 5, InFstVLAN is 1, InSecVLAN is 65535, OutFstVLAN is 0, OutSecVLAN is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MacPort ifSendIndex]{lang="EN-US"}

[is 4, CVlan is 1, CSVlan is 65535, SSVlan is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: IN VLAN mapping: MarkFlag is 0, OutPort]{lang="EN-US"}

[Index is 4, OutFstVLAN is 1]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/6/PACKET: After VLAN mapping: MBUFIfIndex is 0,]{lang="EN-US"}

[ IfIndex is 5, InFstVLAN is 1,InSecVLAN is 65535, OutFstVLAN is 1, OutSecVLAN is 0]{lang="EN-US"}

[\*Jan  1 00:43:17:894 2011 Sysname DHCPSP4/7/PACKET:]{lang="EN-US"}

[Received packets from interface Ten-GigabitEthernet1/0/4]{lang="EN-US"}

[    Transaction ID: 9e604c7b]{lang="EN-US"}

[    Client IP address: 0.0.0.0            Your IP address: 9.2.2.2]{lang="EN-US"}

[    Relay agent IP address: 0.0.0.0]{lang="EN-US"}

[    Client hardware address: 000f-e25d-f27c]{lang="EN-US"}

[    Request IP address: N/A               Server ID: 9.0.0.1]{lang="EN-US"}

[    Client First VLAN ID: 1               Client Second VLAN ID: N/A]{lang="EN-US"}

[    Server First VLAN ID: 1               Server Second VLAN ID: N/A]{lang="EN-US"}

[    DHCP message type: DHCPACK]{lang="EN-US"}

*[//]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}*[ ]{lang="EN-US"}*[DHCP Snooping]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[收到一个]{style="font-size:10.5pt;font-family:宋体"}[DHCP-ACK]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[报文。]{style="font-size:10.5pt;font-family:宋体"}*

[\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: StrippingOption 82 succeeded: offset is ]{lang="EN-US"}

[319, stripped length is 20.]{lang="EN-US"}

[\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: Padded packet: Paddedlength is 20.]{lang="EN-US"}

[\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/7/INFO: Recalculated IP and UDP checksum.]{lang="EN-US"}

[\*Jan  1 00:43:17:895 2011 Sysname DHCPSP4/6/KENTRY: Notify user to get 1 packet node]{lang="EN-US"}

[s, the result is 0.]{lang="EN-US"}

*[// ]{lang="EN-US"}[通知用户态获取报文信息。]{style="font-family:
宋体"}*

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:896 2011 Sysname DHCPSP4/6/2KNL: Started to send synchronous message ]{lang="EN-US"}

[to slot(1).]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:897 2011 Sysname DHCPSP4/6/DBM: Try to add an IP-MAC entry to the running database.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Jan  1 00:43:17:901 2011 Sysname DHCPSP4/6/DBM: Failed to add an IP-MAC entry to database (0)]{lang="EN-US"}
