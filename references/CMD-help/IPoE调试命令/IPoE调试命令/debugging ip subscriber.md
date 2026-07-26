::: {#1845972079 .myid}
[]{#_Toc205697826}[]{#_Toc189624764}[]{#_Toc187290810}[]{#_Toc177820253}[]{#_Toc404785616}[]{#struct_0_82812_37953_x1416746051}[]{#_Ref380667589}[]{#_Ref380667585}[]{#_Toc288815457}

**IPoE调试命令 \-- IPoE调试命令 \-- debugging ip subscriber**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_82812_37953_655370170}

[**[debugging ip subscriber ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_82812_37953_357011945}

[**[undo debugging ip subscriber ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_82812_37953_x143846675}

[[【视图】]{style="font-family:黑体"}]{#struct_0_82812_37953_911955501}

[[用户视图]{style="font-family:宋体"}]{#struct_0_82812_37953_x1978040196}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_82812_37953_814354614}

[[network-admin]{lang="EN-US"}]{#struct_0_82812_37953_1959246235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_82812_37953_x447845970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_82812_37953_x205605890}

[**[all]{lang="EN-US"}**]{#struct_0_82812_37953_x138463054}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的所有调试信息开关]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_82812_37953_97670961}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_82812_37953_923336857}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_82812_37953_160028701}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_82812_37953_x1397390851}

[**[debugging ]{lang="EN-US"}[ip subscriber]{lang="EN-US"}**]{#struct_0_82812_37953_1503961105}[命令用来打开基于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[ip subscriber]{lang="EN-US"}**[命令用来关闭基于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，基于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_82812_37953_414095197}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ip subscriber error]{lang="EN-US"}]{#struct_0_82812_37953_x2090622430}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_57700420}[[字段]{style="font-family:黑体"}]{#struct_0_82812_37953_x1199206987}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_82812_37953_x1683136363}

[[Failed to set an ANCP policy: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*, Reason=*reason*.]{lang="EN-US"}]{#struct_0_82812_37953_1230738541}

[[设置]{style="font-family:宋体"}]{#struct_0_82812_37953_x2028947050}[ANCP]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Node Control Protocol]{lang="EN-US"}[）策略失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1959049627}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x96905904}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x851316705}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x434948474}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1856079819}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1880642893}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x194671103}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1057574452}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1687239476}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_483608441}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_234499501}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1959115163}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x431104531}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x159314013}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x162390083}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1358028565}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1611097915}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x2110891203}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_281770372}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1958918555}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x481572665}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_964778903}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1181254900}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1668605269}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reason]{lang="EN-US"}]{#struct_0_82812_37953_x41575798}[：原因]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[包括以下取值：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Success]{lang="EN-US"}]{#struct_0_82812_37953_661145443}[：成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Line down]{lang="EN-US"}]{#struct_0_82812_37953_x1612072668}[：链路断掉]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Invalid ]{lang="EN-US"}]{#struct_0_82812_37953_x1933559262}[ID]{lang="EN-US"}[：无效的]{lang="EN-US" style="font-family:宋体"}[id]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Not implement]{lang="EN-US"}]{#struct_0_82812_37953_1958984091}[：未生效]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[No enough resource]{lang="EN-US"}]{#struct_0_82812_37953_x427273849}[：资源不足]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Process timeout]{lang="EN-US"}]{#struct_0_82812_37953_1601986179}[：处理超时]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[Other reason]{lang="EN-US"}]{#struct_0_82812_37953_x1389687811}[：其他原因]{lang="EN-US" style="font-family:宋体"}

[[Failed to send an ARP request: Interface= interface-name, IP=ip, VLAN=vlan, CVLAN= cvlan.]{lang="EN-US"}]{#struct_0_82812_37953_239844134}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_57916605}[失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_571230322}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1958787483}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x788794261}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_431363962}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to select srcAddr: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_239844131}

[[选择]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_82812_37953_1434587334}[源地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1232947546}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_811628012}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1958853019}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_x2015836617}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to send an ICMP packet: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_239844132}

[[发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_82812_37953_x1985163571}[报文失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1778379027}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_467886471}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1959704987}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_x469740996}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to get ARP refresh time: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_239844137}

[[获取]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_1530018818}[表项时间戳失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1198016013}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_497564434}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1959770523}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_x438754126}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to enable the user detection function: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN =*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_x700393452}

[[使能用户探测功能失败]{style="font-family:宋体"}]{#struct_0_82812_37953_x40410437}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x311573690}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1959180706}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x38591246}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_x1722590189}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Received an error ICMP reply.]{lang="EN-US"}]{#struct_0_82812_37953_x500309545}

[[接收到错误的]{style="font-family:宋体"}]{#struct_0_82812_37953_x676787569}[ICMP]{lang="EN-US"}[回复报文]{style="font-family:宋体"}

[[Failed to get info from an ICMP reply.]{lang="EN-US"}]{#struct_0_82812_37953_1959246242}

[[从]{style="font-family:宋体"}]{#struct_0_82812_37953_x447780427}[ICMP]{lang="EN-US"}[回复报文中提取信息失败]{style="font-family:宋体"}

[[Failed to enable the interface detection function.]{lang="EN-US"}]{#struct_0_82812_37953_x596962957}

[[使能接口探测功能失败]{style="font-family:宋体"}]{#struct_0_82812_37953_x1014743730}

[[Invalid IP(0.0.0.0) for an ARP rule.]{lang="EN-US"}]{#struct_0_82812_37953_x987971964}

[[(0.0.0.0)]{lang="EN-US"}]{#struct_0_82812_37953_1959049634}[为]{style="font-family:宋体"}[ARP]{lang="EN-US"}[非法地址]{style="font-family:宋体"}

[[Failed to reconnect to ARP, and returned Code=*code*.]{lang="EN-US"}]{#struct_0_82812_37953_x96840369}

[[重连]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_x1252491492}[失败]{style="font-family:宋体"}[.:]{lang="EN-US"}[返回值为]{style="font-family:宋体"}[code]{lang="EN-US"}

[[HA upgrading failed]{lang="EN-US"}]{#struct_0_82812_37953_x634722905}

[[备升主升级失败]{style="font-family:宋体"}]{#struct_0_82812_37953_x1735341077}

[[Malloc failure for muliticast addresses..]{lang="EN-US"}]{#struct_0_82812_37953_1959115170}

[[给组播地址分配内存失败]{style="font-family:宋体"}]{#struct_0_82812_37953_x431170066}

[[Failed to set DSL line characters.]{lang="EN-US"}]{#struct_0_82812_37953_977134090}

[[设置]{style="font-family:宋体"}]{#struct_0_82812_37953_472732465}[DSL line]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to update ANCP policy *name*.]{lang="EN-US"}]{#struct_0_82812_37953_1958918562}

[[更新]{style="font-family:宋体"}]{#struct_0_82812_37953_x481638204}[ANCP]{lang="EN-US"}[策略（名字为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）失败]{style="font-family:宋体"}[. ]{lang="EN-US"}

[[Failed to open the session-timeout timer.]{lang="EN-US"}]{#struct_0_82812_37953_x1768185772}

[[打开]{style="font-family:宋体"}]{#struct_0_82812_37953_x1689325110}[session-timeout]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to open the idle-cut timer.]{lang="EN-US"}]{#struct_0_82812_37953_1958984098}

[[打开]{style="font-family:宋体"}]{#struct_0_82812_37953_x427863673}[idle-cut]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[Failed to open the accounting-update timer.]{lang="EN-US"}]{#struct_0_82812_37953_x1071816790}

[[打开]{style="font-family:宋体"}]{#struct_0_82812_37953_x1903869599}[accounting-update]{lang="EN-US"}[定时器失败]{style="font-family:宋体"}

[[VPN doesn\'t exist and session will be offline..]{lang="EN-US"}]{#struct_0_82812_37953_368229251}

[[下发的授权]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_82812_37953_1958787490}[属性在设备上不存在]{style="font-family:宋体"}[，强制会话处于下线状态]{style="font-family:宋体"}

[[Failed to set pam items during authentication.]{lang="EN-US"}]{#struct_0_82812_37953_x788728724}

[[认证时设置]{style="font-family:宋体"}]{#struct_0_82812_37953_x691429326}[pam items]{lang="EN-US"}[属性失败]{style="font-family:宋体"}

[[Can\'t insert NAS information, because the Circuit ID option is invalid.]{lang="EN-US"}]{#struct_0_82812_37953_1958853026}

[[由于]{style="font-family:宋体"}]{#struct_0_82812_37953_x2015377862}[Circuit ID]{lang="EN-US"}[无效，不能插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Failed to find sessions (UserID=*userid*).]{lang="EN-US"}]{#struct_0_82812_37953_x513489309}

[[根据]{style="font-family:宋体"}]{#struct_0_82812_37953_492307161}[userid]{lang="EN-US"}[查找]{style="font-family:宋体"}[session]{lang="EN-US"}[失败（用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[userid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Userprofile has been deleted (UserID=*userid*).]{lang="EN-US"}]{#struct_0_82812_37953_x677407879}

[[Userprofile]{lang="EN-US"}]{#struct_0_82812_37953_1959704994}[已经被删除了（用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[userid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to notify the kernel to get traffic.]{lang="EN-US"}]{#struct_0_82812_37953_x469675459}

[[通知内核获取流量失败]{style="font-family:宋体"}]{#struct_0_82812_37953_504195216}

[[Failed to send a traffic message.]{lang="EN-US"}]{#struct_0_82812_37953_457787535}

[[流量消息发送失败]{style="font-family:宋体"}]{#struct_0_82812_37953_1959770530}

[[Failed to send VSRP batch session messages (]{lang="EN-US"}[VSRP instance=*vsrp-instance-name*]{lang="EN-US"}]{#struct_0_82812_37953_x438557517}[).]{lang="EN-US"}

[[发送]{style="font-family:宋体"}]{#struct_0_82812_37953_x719027036}[VSRP]{lang="EN-US"}[批备会话消息失败（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to process a VSRP MAC event.]{lang="EN-US"}]{#struct_0_82812_37953_1959180705}

[[处理]{style="font-family:宋体"}]{#struct_0_82812_37953_x38394638}[VSRP]{lang="EN-US"}[虚]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化事件失败]{style="font-family:宋体"}

[[Failed to connect to the peer of VSRP instance (]{lang="EN-US"}[VSRP instance=*vsrp-instance-name*)]{lang="EN-US"}]{#struct_0_82812_37953_1155346061}[.]{lang="EN-US"}

[[连接到]{style="font-family:宋体"}]{#struct_0_82812_37953_2101635472}[VSRP]{lang="EN-US"}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[）对端失败]{style="font-family:宋体"}

[[Failed to synchronize a VSRP event to IO.]{lang="EN-US"}]{#struct_0_82812_37953_1959246241}

[[同步]{style="font-family:宋体"}]{#struct_0_82812_37953_x447583819}[VSRP]{lang="EN-US"}[事件到接口板失败]{style="font-family:宋体"}

[[Failed to send a control message to IO (]{lang="EN-US"}[VSRP instance=*vsrp-instance-name*)]{lang="EN-US"}]{#struct_0_82812_37953_x1031955307}[.]{lang="EN-US"}

[[往接口板发送控制消息失败（]{style="font-family:宋体"}]{#struct_0_82812_37953_1283672711}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[vsrp-instance-name]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Failed to process the packet.]{lang="EN-US"}]{#struct_0_82812_37953_1959049633}

[[处理报文失败]{style="font-family:宋体"}]{#struct_0_82812_37953_x96643761}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ip subscriber timer]{lang="EN-US"}]{#struct_0_82812_37953_x1523756672}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_80123525}[[字段]{style="font-family:黑体"}]{#struct_0_82812_37953_x826561458}

[[描述]{style="font-family:黑体"}]{#struct_0_82812_37953_x341805607}

[[Session-timer expired and session was offline.]{lang="EN-US"}]{#struct_0_82812_37953_x657214463}

[[会话定时器超时，用户下线]{style="font-family:宋体"}[.]{lang="EN-US"}]{#struct_0_82812_37953_x1739382924}

[[Failed to find sessions after a session-timer expired.]{lang="EN-US"}]{#struct_0_82812_37953_1233240442}

[[会话超时定时器超时时未找到会话]{style="font-family:宋体"}]{#struct_0_82812_37953_2141394273}

[[Check session expired: current time=*time1*, old stamp=*time2* sec.]{lang="EN-US"}]{#struct_0_82812_37953_1959115169}

[[检查会话超时，当前时间为]{style="font-family:宋体"}*[time1]{lang="EN-US"}*]{#struct_0_82812_37953_x430711315}[，会话开始时间为]{style="font-family:宋体"}*[time2]{lang="EN-US"}*

[[Refreshed a session-timeout timer, current time=*time*, timeout=*timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x583569892}

[[更新会话定时器，当前时间为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_82812_37953_x873261932}[，超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[.]{lang="EN-US"}

[[Opened a session-timeout timer, current time=*time*, timeout=*timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x853897921}

[[打开会话定时器，当前时间为]{style="font-family:宋体"}*[time]{lang="EN-US"}*]{#struct_0_82812_37953_269468370}[，]{style="font-family:宋体"} [超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*[.]{lang="EN-US"}

[[Closed the idle-cut timer.]{lang="EN-US"}]{#struct_0_82812_37953_x2066026852}

[[关闭空闲定时器]{style="font-family:宋体"}[.]{lang="EN-US"}]{#struct_0_82812_37953_x497619784}

[[Failed to find sessions after an idle-timer expired.]{lang="EN-US"}]{#struct_0_82812_37953_x1957950212}

[[空闲定时器超时后未找到会话]{style="font-family:宋体"}]{#struct_0_82812_37953_x195031247}

[[Idle-cut timer expired and session was offline.]{lang="EN-US"}]{#struct_0_82812_37953_2073997474}

[[空闲定时器超时用户下线]{style="font-family:宋体"}]{#struct_0_82812_37953_1958918561}

[[Opened an idle-cut timer: timeout = * timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x481834812}

[[打开空闲定时器，]{style="font-family:宋体"}]{#struct_0_82812_37953_x997910567} [超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*

[[Closed an accounting-update timer.]{lang="EN-US"}]{#struct_0_82812_37953_2084775556}

[[关闭计费更新定时器]{style="font-family:宋体"}]{#struct_0_82812_37953_2096804316}

[[Failed to find sessions after an accounting-update timer expired (IP=*ip*).]{lang="EN-US"}]{#struct_0_82812_37953_572857745}

[[计费更新定时器超时后（]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_718778024}[地址为]{style="font-family:宋体"}*[ip]{lang="EN-US"}*[）未找到会话]{style="font-family:宋体"}

[[Refreshed an accounting-update timer: timeout=*timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x1311417053}

[[重刷计费更新定时器，]{style="font-family:宋体"}]{#struct_0_82812_37953_1958984097} [超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*

[[Opened an accounting-update timer: timeout=*timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x427142777}

[[打开计费更新定时器，]{style="font-family:宋体"}]{#struct_0_82812_37953_x1840059898} [超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*

[[Created timer *tid*, which will expire in *time* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x910217490}

[[创建一个定时器（定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_82812_37953_x1284553075}[为]{style="font-family:宋体"}*[tid]{lang="EN-US"}*[），]{style="font-family:宋体"}*[times]{lang="EN-US"}*[秒后超时]{style="font-family:宋体"}

[[Deleted timer *tid*.]{lang="EN-US"}]{#struct_0_82812_37953_1689804359}

[[删除一个定时器（定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_82812_37953_x159233830}[为]{style="font-family:宋体"}*[tid]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Refreshed timer *tid*: timeout=*timeout* sec.]{lang="EN-US"}]{#struct_0_82812_37953_x194866157}

[[重刷定时器（定时器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_82812_37953_1958787489}[为]{style="font-family:宋体"}*[tid]{lang="EN-US"}*[），超时时间为]{style="font-family:宋体"}*[timeout]{lang="EN-US"}*

[[Sent an ICMP packet successfully]{lang="EN-US"}]{#struct_0_82812_37953_x789187477}[: Interface=*interface*]{lang="EN-US"}*[-name]{lang="EN-US"}*[, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*]{lang="EN-US"}

[[发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_82812_37953_x1889492428}[报文成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_39543767}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x431793809}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1958853025}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_x2015574470}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[User detection timer expired: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_x1555571415}

[[用户探测定时器超时]{style="font-family:宋体"}]{#struct_0_82812_37953_1636551212}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1488740389}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x355480363}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x812518769}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_1959704993}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Closed a session-timeout timer.]{lang="EN-US"}]{#struct_0_82812_37953_x470003139}

[[关闭会话超时定时器]{style="font-family:宋体"}]{#struct_0_82812_37953_399078967}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ip subscriber event]{lang="EN-US"}]{#struct_0_82812_37953_x613271842}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_78658092}[[字段]{style="font-family:黑体"}]{#struct_0_82812_37953_1429888347}

[[描述]{style="font-family:黑体"}]{#struct_0_82812_37953_x551954508}

[[ARP/ND Rule thread processed request msg(MsgType=*type*).]{lang="EN-US"}]{#struct_0_82812_37953_x649584511}

[[ARP/ND Rule]{lang="EN-US"}]{#struct_0_82812_37953_x510509375}[线程处理请求消息（消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Sent an ARP request successfully: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN =*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_1959770529}

[[发送]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_x439147342}[成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_831620155}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1580640850}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x7178452}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_1138184629}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Added user detection entry successfully: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_x1821490546}

[[添加探测用户成功]{style="font-family:宋体"}]{#struct_0_82812_37953_1466499702}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_669590283}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1508790935}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_43223393}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_537804020}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Deleted user detection entry: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_583607299}

[[删除探测用户]{style="font-family:宋体"}]{#struct_0_82812_37953_x555553452}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x2106420069}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1169182483}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x2126250447}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_x1090573012}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Enabled user detection: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_43157857}

[[开启用户探测]{style="font-family:宋体"}]{#struct_0_82812_37953_69489307}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1089418043}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x458829294}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1449778351}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_1708732375}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Received an ICMP reply: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_1001011787}

[[接收]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_82812_37953_43092321}[回复报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_2020158038}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x482751533}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_2005776811}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_392626303}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Refreshed user detection: Interface=*interface-name*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_x143226642}

[[重刷用户探测]{style="font-family:宋体"}]{#struct_0_82812_37953_43026785}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1239464040}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_188957223}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x393441896}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_x237719151}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[FSM EVT: Deleted a session, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_42961249}

[[状态机事件：删除会话]{style="font-family:宋体"}]{#struct_0_82812_37953_x1745610056}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x2131829972}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1545437212}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_440396306}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1788123393}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_42895713}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_264952752}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1080422510}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1879339593}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_640866328}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1755418780}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_42830177}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_294241507}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x152380921}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1043919402}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x505390046}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_257159452}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_42764641}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_677246743}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x479961695}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1295217070}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1111546853}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_43747681}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_2016509908}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x2021116}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[FSM EVT: Got a session offline, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_43682145}

[[状态机事件：强制会话下线]{style="font-family:宋体"}]{#struct_0_82812_37953_x799599142}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_82812_37953_x552792938}[nterface]{lang="EN-US"}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x409204366}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1723384614}[：]{lang="EN-US" style="font-family:宋体"}[用户]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_43223392}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1800848140}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1348249826}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_266821001}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x420198649}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_43157856}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1886825829}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1132530660}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x987450027}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x417905428}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_43092320}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_63842902}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1748264654}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_456159664}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1979775633}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_43026784}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1099188120}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_812048081}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1707625734}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_42961248}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_210705080}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[FSM EVT: In INITIAL state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_x1947461783}

[[状态机事件：当前为]{style="font-family:宋体"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_605880415}[状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_42895712}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_x1691362384}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_2026407583}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_349811520}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x652890659}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_42830176}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_x1662073629}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_x1429718494}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_212450695}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_42764640}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1661405417}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_1796000302}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1904236716}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_43747680}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x322142252}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_641395208}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_369688329}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_43682144}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_1156715994}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_831118754}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_43223391}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_155466996}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x1319348987}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x2019941941}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_43157855}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x312847717}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1072580539}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_43092319}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1148745689}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1322096479}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_43026783}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1908492184}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1280514726}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_42961247}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_930749112}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1057011115}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_42895711}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x117384272}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_42830175}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_676578531}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1893499833}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_146885034}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_42764639}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: DHCP lease expired, Event=OFFLINE, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_x448816826}

[[状态机事件：会话的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_82812_37953_43747679}[租约超时，用户下线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1602907059}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1108705130}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_43682143}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x417262118}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1437275964}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_43223390}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_2111782132}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_2108821328}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_43157854}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_2025804443}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1069329425}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_43092318}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1189906471}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_87646084}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_43026782}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_47822952}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_42961246}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1407903048}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x2080303286}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_42895710}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x2073699408}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x755573620}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_42830174}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1279736605}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In ONLINE state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_42764638}

[[状态机事件：当前为用户在线状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_1507498310}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_x1839675330}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_43747678}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x735745101}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_43682142}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1539053018}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_602048950}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_43223397}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_x226870028}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_43157861}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_488562176}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1064884174}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_43092325}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1255483990}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_43026789}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_474789992}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_2127054559}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_42961253}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1732159005}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_42895717}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x499721296}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1433292362}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_42830181}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x41041350}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_42764645}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1441920791}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_958022328}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_43747685}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1513783340}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_43682149}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1494423002}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_43223396}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1729445108}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1223830134}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_43157860}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1467752960}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_43092324}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x700831146}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_43026788}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1863862168}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x177884444}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_42961252}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x606493155}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_42895716}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In ASSIGNEDIP state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_1838930864}

[[状态机事件：当前为会话已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x390261770}[地址状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_42830180}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_x1997356486}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_42764644}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x896731369}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_43747684}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_442531796}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_x2096584163}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_43682148}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_x844229158}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609307334}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1148091942}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_1609241798}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1227790527}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_1789342593}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_1609176262}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1526985466}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1609110726}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1511644212}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_1609045190}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x358716695}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1608979654}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1918419912}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_2117787868}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1608914118}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_795538733}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1608848582}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1928214591}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1609831622}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x734226562}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1609766086}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1907290938}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1609307333}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1147764262}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1609241797}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1228642495}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609176261}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1527051002}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1609110725}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1511447604}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1609045189}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1608979653}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1917961160}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1608914117}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In AUTHPASS state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_794686765}

[[状态机事件：当前为认证通过状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_1608848581}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_x1928411199}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_1609831621}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x734292098}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1609766085}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1907225402}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609307332}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_1609241796}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_1228708031}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_1609176260}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1527116538}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1609110724}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_x1511513140}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1609045188}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_x359240984}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_1608979652}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1918026696}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1608914116}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1608848580}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_x1928345663}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1609831620}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x734357634}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1609766084}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1609307331}[：]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}[的创建]{style="font-family:宋体"}[类型]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括]{lang="EN-US" style="font-family:宋体"}[以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1147895334}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1609241795}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1228511423}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1609176259}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1609110723}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1511316532}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1609045187}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x358389016}[：会话状态，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1608979651}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1608914115}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_794817837}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1608848579}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609831619}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x734816387}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1609766083}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1609307338}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1609241802}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1183815878}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1609176266}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1527247610}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In AUTHFAIL state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_1609110730}

[[状态机事件：当前为认证失败状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_1609045194}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_x358454551}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_1608979658}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1608914122}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_794883376}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1608848586}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609831626}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_x733964418}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_1609766090}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_1609307337}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1148026406}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1609241801}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_1183619270}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1609176265}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_1609110729}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x1510661172}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_1609045193}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1608979657}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1608914121}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_795079984}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1608848585}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1609831625}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x734029954}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1609766089}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1206022807}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1722366644}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1205957271}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1205891735}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x2145347714}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1205826199}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1205760663}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1773872015}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1205695127}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1205629591}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1205564055}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1342638672}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1206547095}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1206481559}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1635555324}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1206022806}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1205957270}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_599752855}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1205891734}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1205826198}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In INVALID state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_1205760662}

[[状态机事件：当前为无效状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_1773937551}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_1205695126}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_1205629590}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1205564054}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1342573136}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1206547094}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1206481558}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_1635620860}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_1206022805}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_1205957269}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1205891733}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x2145740930}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_1205826197}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_1205760661}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_1205695125}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x966759763}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_1205629589}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1205564053}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1206547093}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_x296713951}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1206481557}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1206022804}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1205957268}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_600277142}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1205891732}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1205826196}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1205760660}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1205695124}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x966825299}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1205629588}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1205564052}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1206547092}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x296648415}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1206481556}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1206022811}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1205957275}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_599556247}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1205891739}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1205826203}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1205760667}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1205695131}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x967021908}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1205629595}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1205564059}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In AUTH state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_1206547099}

[[状态机事件：当前为认证中状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_1206481563}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_1206022810}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_1722301107}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1205957274}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1205891738}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1205826202}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1205760666}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_1205695130}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_1205629594}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_1205564058}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1206547098}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1206481562}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_x1522860548}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_x1522926084}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_1345881710}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x1522991620}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1523057156}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1523122692}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1523188228}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_x1523253764}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x674107219}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1523319300}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1522336260}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x1522401796}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1522860549}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1522926085}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1522991621}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_338762388}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523057157}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523122693}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523188229}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1523253765}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1523319301}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1522336261}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x696361430}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1522401797}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1522860550}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1522926086}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x1522991622}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1523057158}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1755551765}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1523122694}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1523188230}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1523253766}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: In BACKUP state, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_x1523319302}

[[状态机事件：当前为备份状态，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_x1522336262}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_x1522401798}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_x1522860551}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_2052196524}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1522926087}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1522991623}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1523057159}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_x1523122695}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_x1523188231}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_x1523253767}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1523319303}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1522336263}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_x1522401799}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_x1522860544}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_x1522926080}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x1522991616}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_x2034087215}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1523057152}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1523188224}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_734302367}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1523253760}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1523319296}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1522336256}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x1522401792}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1522860545}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1522926081}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1522991617}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1523057153}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523122689}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523188225}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1523253761}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1523319297}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1522336257}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_110273160}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1522401793}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1926145075}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1926210611}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1926276147}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x1926341683}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1926407219}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1926472755}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1415528371}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1926538291}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1926603827}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: Went on fsm, Event=OTHER, Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_x1925620787}

[[状态机事件：]{style="font-family:宋体"}[session]{lang="EN-US"}]{#struct_0_82812_37953_x1925686323}[平滑后，将状态机继续走下去]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1926210612}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1926276148}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1926341684}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x1926407220}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1926472756}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1926538292}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1926603828}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1925620788}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1925686324}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1926145077}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1926210613}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1926276149}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1926341685}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1926407221}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1926472757}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1926538293}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1925620789}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1925686325}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x1926145078}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1373919100}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1926210614}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1926341686}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1648401372}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1926472758}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[FSM EVT: Triggered the fsm, received an *event*, event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_x1926538294}

[[状态机事件：触发状态机，收到了]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_82812_37953_x1926603830}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Event]{lang="EN-US"}]{#struct_0_82812_37953_x1925620790}[：事件名称，]{lang="EN-US" style="font-family:宋体"}[包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CREATEANDGO]{lang="EN-US"}]{#struct_0_82812_37953_x1925686326}[：配置创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1926145071}[：报文触发]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1926210607}[：进行认证的条件已经满足（静态需要此事件）]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1926276143}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1926341679}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNIP]{lang="EN-US"}]{#struct_0_82812_37953_x1926407215}[：地址分配成功（动态]{lang="EN-US" style="font-family:宋体"}[dhcp session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AGE]{lang="EN-US"}]{#struct_0_82812_37953_x1926472751}[：老化（动态]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEOK]{lang="EN-US"}]{#struct_0_82812_37953_x1926538287}[：规则下发成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RULEFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1926603823}[：规则下发失败]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1925620783}[：用户下线事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[QUIET]{lang="EN-US"}]{#struct_0_82812_37953_x1925686319}[：静默定时器超时]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DESTROY]{lang="EN-US"}]{#struct_0_82812_37953_x1926145072}[：删除]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[CHANGE OF AUTHORIZATION]{lang="EN-US"}]{#struct_0_82812_37953_x1926210608}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权属性变更]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE OK]{lang="EN-US"}]{#struct_0_82812_37953_x1926276144}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[USERPROFILE FAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1926341680}[：]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发驱动失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1926407216}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP]{lang="EN-US"}[对端设备发送过来的]{lang="EN-US" style="font-family:宋体"}[session]{lang="EN-US"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP to ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1926472752}[：收到]{lang="EN-US" style="font-family:宋体"}[VSRP backup]{lang="EN-US"}[变]{lang="EN-US" style="font-family:宋体"}[master]{lang="EN-US"}[的事件]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OTHER]{lang="EN-US"}]{#struct_0_82812_37953_x1926538288}[：无事件触发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1925620784}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x360061134}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x360126670}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x360192206}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x360257742}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x360323278}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x360388814}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x360454350}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x360519886}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x359536846}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x359602382}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x360126671}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x360192207}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x360257743}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x360323279}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x360388815}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x360454351}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x360519887}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x359536847}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x359602383}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x360126672}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x360192208}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x360257744}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x360323280}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[Added an ARP rule successfully: Interface=*interface-name,* VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*]{lang="EN-US"}]{#struct_0_82812_37953_x360388816}*[.]{lang="EN-US"}*

[[添加一条]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_x360454352}[规则成功，]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x360519888}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x359536848}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x359602384}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x360126673}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x360192209}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x360257745}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x360323281}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x360388817}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x360454353}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x360519889}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x359536849}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x360061130}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x360126666}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x360192202}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x360257738}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x360323274}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x360388810}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x360454346}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x360519882}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x359602378}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x360061131}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x360126667}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x360192203}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x360257739}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[Deleted an ARP rule successfully: IP=*ip*.]{lang="EN-US"}]{#struct_0_82812_37953_x360388811}

[[删除一条]{style="font-family:宋体"}[ARP]{lang="EN-US"}]{#struct_0_82812_37953_x360454347}[规则成功，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip]{lang="EN-US"}*

[[Successfully notified DHCP to release a client.]{lang="EN-US"}]{#struct_0_82812_37953_x360519883}

[[通知]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_82812_37953_x359536843}[释放]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[用户信息成功]{style="font-family:宋体"}

[[Failed to notify DHCP to release the IP address of the client and returned Code=*code*.]{lang="EN-US"}]{#struct_0_82812_37953_x359602379}

[[通知]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_82812_37953_x763345661}[释放]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[用户信息失败，返回值为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Deleted a session by DHCPv4 event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_x763411197}

[[因]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_82812_37953_x763476733}[事件删除]{style="font-family:宋体"}[session]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x763542269}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x763607805}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x763738877}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x763804413}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x762821373}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x762886909}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x763345662}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x763411198}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x763476734}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x763542270}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x763607806}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x763673342}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x763738878}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x763804414}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x762821374}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x762886910}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x763411199}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x763476735}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x763542271}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x763607807}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x763673343}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x763738879}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x763804415}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x762821375}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[User ID]{lang="EN-US"}]{#struct_0_82812_37953_x763345664}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_82812_37953_x763411200}

[[Flag ]{lang="EN-US"}]{#struct_0_82812_37953_x763476736}

[[支持的网络特征掩码]{style="font-family:宋体"}]{#struct_0_82812_37953_x763542272}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x01]{lang="EN-US"}]{#struct_0_82812_37953_x763607808}[：接口有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x02]{lang="EN-US"}]{#struct_0_82812_37953_x763673344}[：用户]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x04]{lang="EN-US"}]{#struct_0_82812_37953_x763738880}[：用户]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x08]{lang="EN-US"}]{#struct_0_82812_37953_x763804416}[：用户]{lang="EN-US" style="font-family:宋体"}[PVC ID]{lang="EN-US"}[有效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x10]{lang="EN-US"}]{#struct_0_82812_37953_x762821376}[：用户]{style="font-family:宋体"}[VPN]{lang="EN-US"}[索引有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x20]{lang="EN-US"}]{#struct_0_82812_37953_x762886912}[：用户]{style="font-family:宋体"}[SVLAN]{lang="EN-US"}[有效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x40]{lang="EN-US"}]{#struct_0_82812_37953_x763411193}[：用户]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[有效]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x763476729}

[[用户使用的接口索引]{style="font-family:宋体"}]{#struct_0_82812_37953_x763542265}

[[VPN instance]{lang="EN-US"}]{#struct_0_82812_37953_x763607801}

[[用户]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_82812_37953_x763738873}[实例]{style="font-family:宋体"}

[[Src IP]{lang="EN-US"}]{#struct_0_82812_37953_x763804409}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x762821369}[地址]{style="font-family:宋体"}

[[PVC ID ]{lang="EN-US"}]{#struct_0_82812_37953_x763345658}

[[ATM]{lang="EN-US"}]{#struct_0_82812_37953_x763411194}[接口的]{style="font-family:宋体"}[PVC ID]{lang="EN-US"}

[[SVLAN ID]{lang="EN-US"}]{#struct_0_82812_37953_x763476730}

[[用户的服务器端]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_82812_37953_x763542266}

[[CVLAN ID]{lang="EN-US"}]{#struct_0_82812_37953_x763607802}

[[用户的客户端]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_82812_37953_x763738874}

[[MAC address]{lang="EN-US"}]{#struct_0_82812_37953_x763804410}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_82812_37953_x762821370}[地址]{style="font-family:宋体"}

[[Service type]{lang="EN-US"}]{#struct_0_82812_37953_x762886906}

[[用户的服务类型，包括以下取值：]{style="font-family:宋体"}]{#struct_0_82812_37953_802672744}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_82812_37953_802607208}[：]{lang="EN-US" style="font-family:宋体"}[HSI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_82812_37953_802541672}[：]{lang="EN-US" style="font-family:宋体"}[STB]{lang="EN-US"}[（机顶盒）]{lang="EN-US" style="font-family:宋体"}

[[Access limit]{lang="EN-US"}]{#struct_0_82812_37953_802476136}

[[用户可点播的组播节目数目]{style="font-family:宋体"}]{#struct_0_82812_37953_802345064}

[[User profile]{lang="EN-US"}]{#struct_0_82812_37953_802279528}

[[授权下发的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_82812_37953_803262568}[名字]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_82812_37953_802738279}

[[用户名]{style="font-family:宋体"}]{#struct_0_82812_37953_802672743}

[[Username len]{lang="EN-US"}]{#struct_0_82812_37953_802607207}

[[用户名长度]{style="font-family:宋体"}]{#struct_0_82812_37953_802541671}

[[Max multicasts]{lang="EN-US"}]{#struct_0_82812_37953_802410599}

[[最大组播数]{style="font-family:宋体"}]{#struct_0_82812_37953_802345063}

[[Sent a mcast user *type* message.]{lang="EN-US"}]{#struct_0_82812_37953_802279527}

[[发送组播用户事件类型是]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_82812_37953_803197031}[的消息，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[online]{lang="EN-US"}]{#struct_0_82812_37953_802738278}[：]{lang="EN-US" style="font-family:宋体"}[用户上线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[offline]{lang="EN-US"}]{#struct_0_82812_37953_802672742}[：用户下线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[authchange]{lang="EN-US"}]{#struct_0_82812_37953_802607206}[：]{lang="EN-US" style="font-family:宋体"}[授权属性变更]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[smooth]{lang="EN-US"}]{#struct_0_82812_37953_802476134}[：平滑]{lang="EN-US" style="font-family:宋体"}

[[Sent a mcast user smooth start message.]{lang="EN-US"}]{#struct_0_82812_37953_802410598}

[[发送组播用户平滑开始消息]{style="font-family:宋体"}]{#struct_0_82812_37953_802345062}

[[Sent a mcast user smooth end message.]{lang="EN-US"}]{#struct_0_82812_37953_803262566}

[[发送组播用户平滑结束消息]{style="font-family:宋体"}]{#struct_0_82812_37953_803197030}

[[AAA processed *type* request and returned *result.*]{lang="EN-US"}]{#struct_0_82812_37953_802738277}

[[AAA]{lang="EN-US"}]{#struct_0_82812_37953_802672741}[处理]{style="font-family:宋体"}*[type]{lang="EN-US"}*[类型请求并返回结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[uthentication]{lang="EN-US"}]{#struct_0_82812_37953_802541669}[：认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[authorization]{lang="EN-US"}]{#struct_0_82812_37953_802476133}[：授权]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-start]{lang="EN-US"}]{#struct_0_82812_37953_802410597}[：计费开始]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-update]{lang="EN-US"}]{#struct_0_82812_37953_802279525}[：实时计费]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-stop]{lang="EN-US"}]{#struct_0_82812_37953_803262565}[：计费停止]{lang="EN-US" style="font-family:
  宋体"}

[*[result]{lang="EN-US"}*]{#struct_0_82812_37953_803197029}[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_82812_37953_802672748}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing]{lang="EN-US"}]{#struct_0_82812_37953_802607212}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail(Errcode =]{lang="EN-US"}]{#struct_0_82812_37953_802541676}[ *code*]{lang="EN-US"}[) ]{lang="EN-US"}[：失败]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:宋体"}[错误码]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}

[[Received AAA *type* response and returned *result,* the traffic level is *level.*.]{lang="EN-US"}]{#struct_0_82812_37953_802476140}

[[接收]{style="font-family:宋体"}[AAA*type*]{lang="EN-US"}]{#struct_0_82812_37953_802345068}[类型回复并返回结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，流量级别为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[authentication]{lang="EN-US"}]{#struct_0_82812_37953_802279532}[：]{style="font-family:宋体"}[认证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[authorization]{lang="EN-US"}]{#struct_0_82812_37953_803262572}[：]{style="font-family:宋体"} [授权]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-start]{lang="EN-US"}]{#struct_0_82812_37953_803197036}[：]{style="font-family:宋体"} [计费开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-update]{lang="EN-US"}]{#struct_0_82812_37953_802738283}[：]{style="font-family:宋体"}[实时计费]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[accounting-stop]{lang="EN-US"}]{#struct_0_82812_37953_802607211}[：]{style="font-family:宋体"} [计费停止]{lang="EN-US" style="font-family:宋体"}

[*[result]{lang="EN-US"}*]{#struct_0_82812_37953_802541675}[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[success]{lang="EN-US"}]{#struct_0_82812_37953_802476139}[：]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[processing ]{lang="EN-US"}]{#struct_0_82812_37953_802410603}[：]{style="font-family:宋体"}[处理中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fail(Errcode ]{lang="EN-US"}]{#struct_0_82812_37953_802345067}[ ]{lang="EN-US"}[=]{lang="EN-US"}[ *code*]{lang="EN-US"}[)]{lang="EN-US"}[：]{style="font-family:宋体"}[失败]{lang="EN-US" style="font-family:宋体"}[（]{style="font-family:宋体"}[错误码]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}*[code]{lang="EN-US"}*[）]{lang="EN-US" style="font-family:宋体"}

[[Set an ANCP policy.]{lang="EN-US"}]{#struct_0_82812_37953_802279531}

[[设置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_82812_37953_803197035}[策略]{style="font-family:宋体"}

[[Setting ANCP policy *name* failed.]{lang="EN-US"}]{#struct_0_82812_37953_399453753}

[[设置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_82812_37953_399388217}[策略（名字为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）失败]{style="font-family:宋体"}

[[Updated an ANCP policy.]{lang="EN-US"}]{#struct_0_82812_37953_399322681}

[[更新]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_82812_37953_399257145}[策略]{style="font-family:宋体"}

[[Session timeout is zero in the accounting-update reply.]{lang="EN-US"}]{#struct_0_82812_37953_399126073}

[[在计费更新报文回应报文中，最新下发的]{style="font-family:宋体"}[session-timeout]{lang="EN-US"}]{#struct_0_82812_37953_399060537}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Session authentication info: domain=*domain*.]{lang="EN-US"}]{#struct_0_82812_37953_398995001}

[[会话认证信息：]{style="font-family:宋体"}]{#struct_0_82812_37953_399978041} [认证域名为]{style="font-family:宋体"}*[domain]{lang="EN-US"}*

[[Session (IP=*ip*) processed reconnected to AAA.]{lang="EN-US"}]{#struct_0_82812_37953_399912505}

[[会话（]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_399388216}[地址为]{style="font-family:宋体"}*[ip]{lang="EN-US"}*[）与]{style="font-family:宋体"}[AAA]{lang="EN-US"}[模块进行重连接]{style="font-family:宋体"}

[[Remanent_Volume is zero and session will be offline.]{lang="EN-US"}]{#struct_0_82812_37953_399322680}

[[用户的剩余流量为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_82812_37953_399257144}[，强制会话下线]{style="font-family:宋体"}

[[Session requested offline: state=*state*]{lang="EN-US"}]{#struct_0_82812_37953_399191608}

[[会话请求下线，状态值为]{style="font-family:宋体"}[state]{lang="EN-US"}]{#struct_0_82812_37953_399126072}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_82812_37953_398995000}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_82812_37953_399978040}[：认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_82812_37953_399912504}[：等待授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_82812_37953_399453751}[：在线状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_82812_37953_399388215}[：计费状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_82812_37953_399257143}[：计费停止状态]{lang="EN-US" style="font-family:宋体"}

[[Session state error in the authentication response, state=*state*.]{lang="EN-US"}]{#struct_0_82812_37953_399191607}

[[认证回应中的会话状态错误，状态值为]{style="font-family:宋体"}[state]{lang="EN-US"}]{#struct_0_82812_37953_399126071}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_82812_37953_399060535}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_82812_37953_399978039}[：认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_82812_37953_399912503}[：等待授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_82812_37953_399453750}[：在线状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_82812_37953_399388214}[：计费状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_82812_37953_399322678}[：计费停止状态]{lang="EN-US" style="font-family:宋体"}

[[Session state error in the authorization response, state=*state*.]{lang="EN-US"}]{#struct_0_82812_37953_399191606}

[[授权回应中的会话状态错误，状态值为]{style="font-family:宋体"}[state]{lang="EN-US"}]{#struct_0_82812_37953_399126070}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_82812_37953_399060534}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_82812_37953_398994998}[：认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_82812_37953_399912502}[：等待授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_82812_37953_399453757}[：在线状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_82812_37953_399388221}[：计费状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_82812_37953_399322685}[：计费停止状态]{lang="EN-US" style="font-family:宋体"}

[[Session state error in the accounting-start response, state=*state*.]{lang="EN-US"}]{#struct_0_82812_37953_399191613}

[[开始计费回应中的会话状态错误，状态值为]{style="font-family:宋体"}[state]{lang="EN-US"}]{#struct_0_82812_37953_399126077}[，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_82812_37953_399060541}[：初始化状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_82812_37953_398995005}[：认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_82812_37953_399978045}[：等待授权状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_82812_37953_399453756}[：在线状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4]{lang="EN-US"}]{#struct_0_82812_37953_399388220}[：计费状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5]{lang="EN-US"}]{#struct_0_82812_37953_399322684}[：计费停止状态]{lang="EN-US" style="font-family:宋体"}

[[Updated VPN info in session.]{lang="EN-US"}]{#struct_0_82812_37953_399257148}

[[更新会话信息中的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_82812_37953_399126076}[属性]{style="font-family:宋体"}

[[Updated session-timeout in session.]{lang="EN-US"}]{#struct_0_82812_37953_399060540}

[[更新会话信息中的]{style="font-family:宋体"}[session-timeout]{lang="EN-US"}]{#struct_0_82812_37953_398995004}[属性]{style="font-family:宋体"}

[[Session timeout is zero in COA and session will be offline.]{lang="EN-US"}]{#struct_0_82812_37953_399978044}

[[在]{style="font-family:宋体"}[COA]{lang="EN-US"}]{#struct_0_82812_37953_399912508}[报文中]{style="font-family:宋体"}[session-timeout]{lang="EN-US"}[属性为]{style="font-family:宋体"}[0]{lang="EN-US"}[，强制会话下线]{style="font-family:宋体"}

[[Updated the user profile in session.]{lang="EN-US"}]{#struct_0_82812_37953_1965472158}

[[更新会话信息中的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_82812_37953_1965406622}[属性]{style="font-family:宋体"}

[[Received a notification message for setting AAA COA.]{lang="EN-US"}]{#struct_0_82812_37953_1965341086}

[[接收到设置策略]{style="font-family:宋体"}[COA]{lang="EN-US"}]{#struct_0_82812_37953_1965275550}[通知消息]{style="font-family:宋体"}

[[Received a notification message for setting policy POD.]{lang="EN-US"}]{#struct_0_82812_37953_1965210014}

[[接收到设置策略]{style="font-family:宋体"}[POD]{lang="EN-US"}]{#struct_0_82812_37953_1965078942}[通知消息]{style="font-family:宋体"}

[[Received an ACK Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_1966061982}

[[接收到一个]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_82812_37953_1965996446}[回应报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1965472157}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1965406621}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1965341085}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1965275549}[：]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}[的创建]{style="font-family:宋体"}[类型]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[包括]{lang="EN-US" style="font-family:宋体"}[以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1965144477}[：无效类型]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1965078941}[：接口专线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1966061981}[：子网专线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1965537692}[：静态配置]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1965472156}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1965406620}[：未知源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1965275548}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1965210012}[：会话状态，]{lang="EN-US" style="font-family:宋体"}[state]{lang="EN-US"}[包括以下取值：]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1965078940}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1966061980}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1965537691}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1965472155}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1965341083}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1965275547}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1965210011}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1965078939}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1966061979}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1965996443}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1965537698}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1965406626}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[Received an ACK Reply packet to assign IP address: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*Received*.*]{lang="EN-US"}]{#struct_0_82812_37953_1965341090}

[[接收到一个已分配]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1965275554}[地址的]{style="font-family:宋体"}[ACK]{lang="EN-US"}[回应报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1965144482}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1965078946}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1966061986}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1965537697}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1965472161}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1965341089}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1965275553}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1965144481}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1965078945}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1965996449}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_32541025}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_32672097}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_32737633}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_32344417}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_32409953}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_33065313}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_33130849}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_32541024}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_32672096}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_32737632}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_32278880}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_32409952}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_32475488}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_33065312}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[Received a Renew Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_32541023}

[[接收到一个]{style="font-family:宋体"}[renew]{lang="EN-US"}]{#struct_0_82812_37953_32606559}[回应报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_32672095}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_32278879}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_32344415}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_32475487}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_33065311}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_32541022}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_32672094}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_32737630}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_32344414}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_32409950}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_33065310}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_33130846}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_32541029}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_32672101}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_32737637}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_32278885}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_32409957}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_32475493}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_33065317}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_32541028}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_32606564}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_32672100}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_32278884}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_32344420}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[Received a NAK Reply packet: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_32409956}

[[接收到一个]{style="font-family:宋体"}[NAK]{lang="EN-US"}]{#struct_0_82812_37953_33065316}[回应报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_33130852}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1598624966}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1598756038}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1598821574}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1598362822}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1598493894}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1598559430}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1599214790}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1598624965}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1598690501}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1598821573}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1598362821}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1598493893}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1598559429}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1599149253}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1598624964}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1598690500}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1598821572}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1598362820}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1598428356}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1598559428}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1599149252}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1599214788}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1598690499}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[Received a sync session message: Interface=*interface-name,* VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node,* type=*type.*]{lang="EN-US"}]{#struct_0_82812_37953_1598756035}

[[接收到同步过来的会话信息]{style="font-family:宋体"}]{#struct_0_82812_37953_1598362819}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1598428355}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1598493891}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1599149251}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1599214787}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1598690506}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1598756042}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1598821578}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1598428362}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1598493898}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1599149258}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1599214794}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1598690505}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1598756041}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_1598362825}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_1598428361}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_1598559433}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_1599149257}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1195340439}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_1195471511}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_1195537047}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1195143831}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_1195274903}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1195864727}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1195340438}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[type]{lang="EN-US"}]{#struct_0_82812_37953_1195471510}[：]{lang="EN-US" style="font-family:宋体"}[消息]{style="font-family:宋体"}[类型]{lang="EN-US" style="font-family:宋体"}

[[Received a sync message from node *node*.]{lang="EN-US"}]{#struct_0_82812_37953_1195537046}

[[从节点号是]{style="font-family:宋体"}*[node]{lang="EN-US"}*]{#struct_0_82812_37953_1195143830}[的单板接收到同步消息]{style="font-family:宋体"}

[[Begun to batch sessions.]{lang="EN-US"}]{#struct_0_82812_37953_1427159847}

[[开始批备会话信息]{style="font-family:宋体"}]{#struct_0_82812_37953_1427159853}

[[Begun to age and process all sessions.]{lang="EN-US"}]{#struct_0_82812_37953_1195274902}

[[开始]{style="font-family:宋体"}]{#struct_0_82812_37953_1195864726} [老化和处理所有会话]{style="font-family:宋体"}

[[Requested to add a user-profile/Car rule (UserID=*id*).]{lang="EN-US"}]{#struct_0_82812_37953_1195340437}

[[请求添加]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_82812_37953_1195471509}[规则（用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Requested to delete a user-profile/Car rule (UserID=*id*).]{lang="EN-US"}]{#struct_0_82812_37953_1195537045}

[[请求删除]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_82812_37953_1195209365}[规则（用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received result of setting user profile (UserID=*id*, Result=*result*).]{lang="EN-US"}]{#struct_0_82812_37953_1195930261}

[[接收设置]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_82812_37953_1195405972}[的结果（用户]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[id]{lang="EN-US"}*[，]{style="font-family:宋体"} [结果为]{style="font-family:宋体"}*[result]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Rule thread processed request messages (MessageType=*type*).]{lang="EN-US"}]{#struct_0_82812_37953_1195537044}

[[Rule]{lang="EN-US"}]{#struct_0_82812_37953_1195078292}[线程处理请求消息（消息类型为]{style="font-family:宋体"}*[type]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Remanent volume has been exhausted and session will be offline.]{lang="EN-US"}]{#struct_0_82812_37953_1195209364}

[[剩余流量已经耗尽，会话下线]{style="font-family:宋体"}]{#struct_0_82812_37953_1195864724}

[[Deleted cache sessions successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node*.]{lang="EN-US"}]{#struct_0_82812_37953_1195340443}

[[成功删除缓存中的会话]{style="font-family:宋体"}]{#struct_0_82812_37953_1195405979}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1195537051}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1195143835}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1195274907}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1195930267}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1195340442}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1195471514}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1195078298}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_1195209370}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1195274906}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1195930266}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1533477380}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1533346308}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1533805060}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1533673988}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1533018628}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1533542917}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1533411845}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1533805061}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x1533739525}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1533608453}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1532953093}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1533477382}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1533346310}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1533739526}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[IPoE Channel is connecting to the peer of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533673990}

[[本实例和实例名字是]{style="font-family:宋体"}*[name]{lang="EN-US"}*]{#struct_0_82812_37953_x1533018630}[的对端建立备份通道]{style="font-family:宋体"}

[[IPoE Channel is listening to the peer of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533542919}

[[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_x1533411847}[通道正在监听实例名字是]{style="font-family:宋体"}*[name]{lang="EN-US"}*[的对端]{style="font-family:宋体"}

[[Synchronized VSRP event to IO successfully.]{lang="EN-US"}]{#struct_0_82812_37953_x1533805063}

[[同步]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533673991}[事件到接口板成功]{style="font-family:宋体"}

[[Received a VSRP event(*type*) of instance *name* on IO.]{lang="EN-US"}]{#struct_0_82812_37953_x1533608455}

[[接收到接口板上]{style="font-family:宋体"}*[type]{lang="EN-US"}*]{#struct_0_82812_37953_x1532953095}[类型的]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）事件]{style="font-family:宋体"}

[[Received a VSRP status event(status=*status*) of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533477376}

[[接收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533346304}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）状态事件（状态值为]{style="font-family:宋体"}*[status]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a VSRP backupmode event(mode=*mode*) of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533805056}

[[接收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533673984}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）备份方式事件（备份方式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a VSRP interval event(interval=*interval*) of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533018624}

[[接收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533542913}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）的流量备份间隔事件（间隔时长是]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a VSRP traffic threshold event(value=*val*) of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533411841}

[[接收]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533805057}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）的流量备份阈值事件（阈值为]{style="font-family:宋体"}*[value]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Received a VSRP VMAC event(mac=*mac*) of instance *name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1533739521}

[[接收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1533608449}[（]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*[）的虚]{style="font-family:宋体"}[MAC]{lang="EN-US"}[事件（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Sent a VSRP control message to IO successfully, instance=*name*.]{lang="EN-US"}]{#struct_0_82812_37953_x1936827443}

[[发送]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1936761907}[控制信息到接口板成功，]{style="font-family:宋体"}[VSRP]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}*[name]{lang="EN-US"}*

[[Added cache sessions for VSRP successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node,*]{lang="EN-US"}]{#struct_0_82812_37953_x1937089587}

[[成功添加了]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_82812_37953_x1937024051}[缓冲会话]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1936892979}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1936237619}[PN]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[V]{lang="EN-US"}[PN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1936761908}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_x1936630836}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1937024052}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1936892980}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1936237620}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1936761909}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1936630837}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1937024053}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x1936892981}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x1936237621}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1936761910}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1936696374}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1937089590}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1936958518}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1936303158}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x1936827439}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x1936696367}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x1937089583}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1936958511}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x1936892975}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x1936237615}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_x1936761904}[：服务]{lang="EN-US" style="font-family:宋体"}[板卡号]{style="font-family:宋体"}

[[Channel is connected.]{lang="EN-US"}]{#struct_0_82812_37953_x1936630832}

[[通道连接建立]{style="font-family:宋体"}]{#struct_0_82812_37953_x1937024048}

[[Channel is disconnected.]{lang="EN-US"}]{#struct_0_82812_37953_x1936892976}

[[通道连接断开]{style="font-family:宋体"}]{#struct_0_82812_37953_x1936237616}

[[Dropped a DHCP packet from *mac* because of invalid state *state*.]{lang="EN-US"}]{#struct_0_82812_37953_x370677966}

[[由于会话状态]{style="font-family:宋体"}]{#struct_0_82812_37953_x370612430} [（状态值为]{style="font-family:宋体"}*[state]{lang="EN-US"}*[）无效，丢弃]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Started to authenticate unclassified IP packets from *ip*.]{lang="EN-US"}]{#struct_0_82812_37953_x371005646}

[[开始对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x370874574}[地址是]{style="font-family:宋体"}*[ip]{lang="EN-US"}*[的未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进行认证]{style="font-family:宋体"}

[[Dropped IP packets from *ip* because of invalid state *state*.]{lang="EN-US"}]{#struct_0_82812_37953_x370219214}

[[由于会话状态（状态值为]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_82812_37953_x370743503}[）无效，丢弃]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[ip]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Dropped a DHCP packet from *mac* which is in state *state*.]{lang="EN-US"}]{#struct_0_82812_37953_x370612431}

[[丢弃处于会话状态（状态值是]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_82812_37953_x371005647}[）的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Started to authenticate packets because of init state of interface leased.]{lang="EN-US"}]{#struct_0_82812_37953_x370874575}

[[接口专线处于]{style="font-family:宋体"}[Init]{lang="EN-US"}]{#struct_0_82812_37953_x370219215}[状态，开始认证报文]{style="font-family:宋体"}

[[Dropped the packet because of invalid state *state* of interface leased.]{lang="EN-US"}]{#struct_0_82812_37953_x370153679}

[[接口专线处于无效状态（状态值是]{style="font-family:宋体"}*[state]{lang="EN-US"}*]{#struct_0_82812_37953_x370677968}[），丢弃报文]{style="font-family:宋体"}

[[Tried to add a session, but IPoE is not enabled on interface.]{lang="EN-US"}]{#struct_0_82812_37953_x370546896}

[[添加会话时，接口上没有使能]{style="font-family:宋体"}[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_x370940112}

[[Connected to LICENSE module.]{lang="EN-US"}]{#struct_0_82812_37953_680230840}

[[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_x482568574}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接建立成功]{style="font-family:宋体"}

[[Failed to connect to LICENSE module.]{lang="EN-US"}]{#struct_0_82812_37953_x2001598348}

[[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_x1511150260}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接建立失败]{style="font-family:宋体"}

[[Disconnected from LICENSE module.]{lang="EN-US"}]{#struct_0_82812_37953_1621017622}

[[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_1217733095}[模块与]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[模块的连接断开成功]{style="font-family:宋体"}

[[Received LICENSE event: ]{lang="EN-US"}]{#struct_0_82812_37953_x348350846}[]{#_GoBack}[EventType=*event-type*.]{lang="EN-US"}

[[IPoE]{lang="EN-US"}]{#struct_0_82812_37953_54868145}[收到]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}[的]{style="font-family:宋体"}[EventType]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[EventType]{lang="EN-US"}]{#struct_0_82812_37953_x1107931269}[类型如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Installed]{lang="EN-US"}]{#struct_0_82812_37953_x1914500323}[：安装]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Uninstalled]{lang="EN-US"}]{#struct_0_82812_37953_1217667559}[：卸载]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Expired]{lang="EN-US"}]{#struct_0_82812_37953_x301362215}[：]{lang="EN-US" style="font-family:宋体"}[过期]{lang="EN-US" style="font-family:宋体"}

[[Changed the session limit from old-value to new-value per card.]{lang="EN-US"}]{#struct_0_82812_37953_54802609}

[[更新]{style="font-family:宋体"}[LICENSE]{lang="EN-US"}]{#struct_0_82812_37953_x1107996805}[定制的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[单板会话限制数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[old-value]{lang="EN-US"}*]{#struct_0_82812_37953_1620886550}[：旧的]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[单板会话限制数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[new-value]{lang="EN-US"}*]{#struct_0_82812_37953_814317496}[：新的]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[单本会话限制数]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_82812_37953_1906442981}

[[\# ]{lang="EN-US"}]{#struct_0_82812_37953_183581240}[打开]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[的所有调试信息开关。未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的报文触发]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[认证时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_82812_37953_x370874576}

[\<Sysname\> terminal debugging]{lang="EN-US"}

[\<Sysname\> debugging ip subscriber all]{lang="EN-US"}

[\<Sysname\> \*Dec  1 16:43:12:878 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Started to authenticate unclassified IP packets from 1.2.3.4.]{lang="EN-US"}

*[//]{lang="EN-US"}[开始对]{style="font-family:
宋体"}[ip]{lang="EN-US"}[地址是]{style="font-family:宋体"}*[1.2.3.4]{lang="EN-US"}*[的未知源]{style="font-family:宋体"}[ip]{lang="EN-US"}[报文进行认证]{style="font-family:宋体"}*[         ]{lang="EN-US"}

[\*Dec  1 16:43:12:879 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, Event = INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：触发，事件：初始化，接口是]{style="font-family:
宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}[(]{lang="EN-US"}[非堆叠设备]{style="font-family:宋体"}[)]{lang="EN-US"}*

[\*Dec  1 16:43:12:879 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID= 0xffffffff, Service node = slot 5 cpu 0\...]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：触发，事件：初始化，接口是]{style="font-family:
宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}[(]{lang="EN-US"}[堆叠设备]{style="font-family:宋体"}[)]{lang="EN-US"}*

[\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INVALID, EVENT =INIT, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=chassis 1 slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：无效状态，事件：初始化，接口是]{style="font-family:
宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INIT, EVENT =AUTH, Interface=GE5/2/2, VRF=0, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=INVALID, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：初始状态，事件：认证请求，接口是]{style="font-family:
宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}[   ]{lang="EN-US"}*

[\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/TIMER: -MDC=1-Slot=5;]{lang="EN-US"}

[Created a timer(TID=3), which will expire in 600s.]{lang="EN-US"}

*[//]{lang="EN-US"}[创建一个定时器（定时器]{style="font-family:
宋体"}[id]{lang="EN-US"}[是]{style="font-family:
宋体"}[3]{lang="EN-US"}[），]{style="font-family:宋体"}[600]{lang="EN-US"}[秒钟后超时]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:880 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Session authentication info: domain=radius.]{lang="EN-US"}

*[//session]{lang="EN-US"}[认证信息：域]{style="font-family:宋体"}* *[是]{style="font-family:宋体"}[ radius]{lang="EN-US"}*

[\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[AAA processed authentication requests and returned success.]{lang="EN-US"}

*[//]{lang="EN-US"}[接收到]{style="font-family:
宋体"}[AAA]{lang="EN-US"}[的认证回应结果是成功]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[AAA processed authorization requests and returned success.]{lang="EN-US"}

*[//AAA]{lang="EN-US"}[处理授权请求返回结果是成功]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTH, EVENT = AUTHPASS, Interface = GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=AUTH, UserID=0xffffffff, Service node=slot 5 cpu 0..]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：触发，事件：认证通过，接口是]{style="font-family:
宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTHPASS, EVENT=ASSIGNIP, Interface=GE5/2/2, VRF=1, IP =1.2.3.4, Type=UNKNOWN-IP-PKT, State=AUTHPASS, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：认证通过状态，事件：分配]{style="font-family:
宋体"}[ip]{lang="EN-US"}[地址，接口是]{style="font-family:宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:881 2013 Sysname IPOE/7/TIMER: -MDC=1-Slot=5;]{lang="EN-US"}

[Deleted a timer(TID=3)]{lang="EN-US"}

*[//]{lang="EN-US"}[删除一个定时器（定时器]{style="font-family:
宋体"}[id]{lang="EN-US"}[是]{style="font-family:
宋体"}[3]{lang="EN-US"}[）]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:883 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Rule thread processed request message(MessageType=0).]{lang="EN-US"}

*[//rule]{lang="EN-US"}[线程处理请求下发]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[消息（消息类型是]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:883 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Requested to add a user-profile rule(UserID=0x30000007).]{lang="EN-US"}

*[//]{lang="EN-US"}[请求添加]{style="font-family:
宋体"}[userprofile]{lang="EN-US"}[规则（用户]{style="font-family:宋体"}[id]{lang="EN-US"}[是]{style="font-family:宋体"}[0x30000007]{lang="EN-US"}[）]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:886 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Received result of user profile settings(UserID=0x30000007, Result=0).]{lang="EN-US"}

*[//]{lang="EN-US"}[接收设置]{style="font-family:
宋体"}[userprofile]{lang="EN-US"}[的结果（用户]{style="font-family:宋体"}[id]{lang="EN-US"}[是]{style="font-family:宋体"}[0x30000007]{lang="EN-US"}[，结果是]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:888 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = USERPROFILE OK, Interface=GE5/2/2, VRF= 1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ASSIGNEDIP, UserID=0x30000007, Service node=slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：触发，事件：下发]{style="font-family:
宋体"}[userprofile]{lang="EN-US"}[成功，接口是]{style="font-family:宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:888 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state ASSIGNEDIP, EVENT=USERPROFILE OK, Interface= GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ASSIGNEDIP, UserID=0x30000007, Service node=slot 5 cpu 0]{lang="EN-US"}

*[//]{lang="EN-US"}[状态机事件处理：分配]{style="font-family:
宋体"}[IP]{lang="EN-US"}[状态，事件：下发]{style="font-family:
宋体"}[userprofile]{lang="EN-US"}[成功，接口是]{style="font-family:宋体"}[GE5/2/2]{lang="EN-US"}[，显示具体的]{style="font-family:宋体"}[session]{lang="EN-US"}[信息]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Added an ARP entry successfully, Interface=GE5/2/2, VRF=1, IP=1.2.3.4, Type=UNKNOWN-IP-PKT, State=ONLINE, UserID=0x30000007, Service node=slot 5 cpu 0.]{lang="EN-US"}

*[//]{lang="EN-US"}[添加]{style="font-family:
宋体"}[ARP]{lang="EN-US"}[规则成功]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[AAA processed accounting-start requests and returned success.]{lang="EN-US"}

*[//AAA]{lang="EN-US"}[处理计费开始请求，返回结果是处理成功]{style="font-family:宋体"}*

[\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Added a detection user successfully, Interface=GigabitEthernet5/2/2, IP=1.2.3.4, VLAN=65535, CVLAN=65535.]{lang="EN-US"}

*[//]{lang="EN-US"}[添加探测用户成功]{style="font-family:
宋体"}*

[\*Dec  1 16:43:12:890 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}

[Sent mcast user online message.]{lang="EN-US"}

*[//]{lang="EN-US"}[发送组播用户在线消息]{style="font-family:
宋体"}*

[[\*Dec  1 16:43:12:891 2013 Sysname IPOE/7/EVENT: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_82812_37953_x265260732}

[ User ID            : 0x30000007]{lang="EN-US"}

[ Flag               : 23]{lang="EN-US"}

[ Interface          : GE1/0/1]{lang="EN-US"}

[ VPN instance       : 1]{lang="EN-US"}

[ Src IP             : 1.2.3.4]{lang="EN-US"}

[ PVC ID             : 0]{lang="EN-US"}

[ SVLAN ID           : N/A]{lang="EN-US"}

[ CVLAN ID           : N/A]{lang="EN-US"}

[ MAC address        : aaaa-aaaa-aaaa]{lang="EN-US"}

[ Service type       : 0]{lang="EN-US"}

[ Access limit       : 4]{lang="EN-US"}

[ User profile       : a]{lang="EN-US"}

[ User name          : 1.2.3.4]{lang="EN-US"}

[ User name len      : 7]{lang="EN-US"}

[ Max multicast num  : 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1411702625}*[打印传给可控组播的消息]{style="font-family:宋体"}*

::: {#-1665104344 .myid}
[]{#_Toc404785617}[]{#struct_0_82812_37953_1880955207}[]{#_Toc288816871}[]{#_Toc288816872}[]{#_Toc288816873}[]{#_Toc288816877}[]{#_Toc288816892}[]{#_Toc288816893}[]{#_Toc288816910}[]{#_Toc288816911}[]{#_Toc288816912}[]{#_Toc288816927}[]{#_Toc288816928}[]{#_Toc288816930}

**IPoE调试命令 \-- IPoE调试命令 \-- debugging ipv6 subscriber**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_82812_37953_x1415398062}

[**[debugging ipv6 subscriber ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_82812_37953_x1671254563}

[**[undo debugging ipv6 subscriber ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **timer** }]{lang="EN-US"}]{#struct_0_82812_37953_x370743505}

[[【视图】]{style="font-family:黑体"}]{#struct_0_82812_37953_x424642755}

[[用户视图]{style="font-family:宋体"}]{#struct_0_82812_37953_x980030765}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_82812_37953_x802339836}

[[network-admin]{lang="EN-US"}]{#struct_0_82812_37953_1775700599}

[[mdc-admin]{lang="EN-US"}]{#struct_0_82812_37953_x980274004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_82812_37953_324605620}

[**[all]{lang="EN-US"}**]{#struct_0_82812_37953_729776050}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的所有调试信息开关]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_82812_37953_1646542434}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_82812_37953_x1124181507}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_82812_37953_x2082168830}[：表示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_82812_37953_1627762143}

[**[debugging ]{lang="EN-US"}[ipv6 subscriber]{lang="EN-US"}**]{#struct_0_82812_37953_x831710032}[命令用来打开基于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[ipv6 subscriber]{lang="EN-US"}**[命令用来关闭基于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，基于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_82812_37953_1762124473}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[需要注意的是，与]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_82812_37953_x370677969}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的调试信息开关相同的信息以下不再列出，可参考"]{style="font-family:宋体"}[[1.1.1  ]{lang="EN-US"}](?1845972079#_Ref380667585)[[debugging ip subscriber]{lang="EN-US"}](?1845972079#_Ref380667589)["输出信息描述表。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging ipv6 subscriber error]{lang="EN-US"}]{#struct_0_82812_37953_1125206474}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_85772887}[[字段]{style="font-family:黑体"}]{#struct_0_82812_37953_x115848467}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_82812_37953_x1314752521}

[[Failed to receive an ICMPv6 reply..]{lang="EN-US"}]{#struct_0_82812_37953_x376094683}

[[接收到错误的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_82812_37953_x481766401}[回应报文]{style="font-family:宋体"}

[[Failed to receive info from an ICMP6 reply.]{lang="EN-US"}]{#struct_0_82812_37953_x1385288125}

[[从]{style="font-family:宋体"}]{#struct_0_82812_37953_813889221}[ICMPv6]{lang="EN-US"}[回复报文中提取信息失败]{style="font-family:宋体"}

[[Failed to reconnect to ND and returned Code = *code*]{lang="EN-US"}*[.]{lang="EN-US"}*]{#struct_0_82812_37953_x1869276957}

[[重连]{style="font-family:宋体"}]{#struct_0_82812_37953_1015101212}[ND]{lang="EN-US"}[失败]{style="font-family:宋体"}[.]{lang="EN-US"}[返回值为]{style="font-family:宋体"}*[code]{lang="EN-US"}*

[[Failed to select srcAddr6: Interface=interface: IP=ip, VLAN=vlan, CVLAN=cvlan.]{lang="EN-US"}]{#struct_0_82812_37953_235518755}

[[选择]{style="font-family:宋体"}]{#struct_0_82812_37953_x370612433}[IPv6]{lang="EN-US"}[源地址失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x49419276}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_807746662}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x470808116}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecV]{lang="EN-US"}]{#struct_0_82812_37953_1608080938}[LAN]{lang="EN-US"}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to send an ICMP6 packet: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_235518756}

[[发送]{style="font-family:宋体"}]{#struct_0_82812_37953_x160892741}[ICMPv6]{lang="EN-US"}[报文失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_728500986}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x269210191}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x370546897}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_1526644235}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Failed to get ND refresh time: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_235518761}

[[获取]{style="font-family:宋体"}]{#struct_0_82812_37953_x931559662}[ND]{lang="EN-US"}[表项时间戳失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1213525325}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x1036379470}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x697311862}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_x1024806590}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Invalid DHCPv6 message (hop=*hop*).]{lang="EN-US"}]{#struct_0_82812_37953_x371005649}

[[非法的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_82812_37953_x443064472}[消息（跳数为]{style="font-family:宋体"}*[hop]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Invalid DHCPv6 Relay message (level=*level*, length=*len*).]{lang="EN-US"}]{#struct_0_82812_37953_x1900265989}

[[非法的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_82812_37953_x146818318}[中继消息（值为]{style="font-family:宋体"}*[level]{lang="EN-US"}*[，协议长度为]{style="font-family:宋体"}*[len]{lang="EN-US"}*[）]{style="font-family:宋体"}

*[ ]{lang="EN-US"}*

[[表1-5 ]{lang="EN-US"}[debugging ip subscriber event]{lang="EN-US"}]{#struct_0_82812_37953_x1741179223}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_87939291}[[字段]{style="font-family:黑体"}]{#struct_0_82812_37953_x1902640467}

[[描述]{style="font-family:黑体"}]{#struct_0_82812_37953_x31977587}

[[Added a ND rule successfully: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_x578473840}

[[添加一条]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_82812_37953_787576605}[规则成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x370940113}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPN]{lang="EN-US"}]{#struct_0_82812_37953_1906508517}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x291649504}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_2051607796}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_629663886}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_2091095332}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1717938688}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_906930397}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x422719545}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x370874577}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x838085268}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_1247976102}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x1203796211}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_x1726808904}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_789709101}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_x1605711221}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x1563464214}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_x306956664}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x370809041}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_768928140}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_1414779460}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x597084921}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_1602615214}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_433679023}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[Deleted a ND rule successfully, IP=*ip*.]{lang="EN-US"}]{#struct_0_82812_37953_1286733946}

[[删除一条]{style="font-family:宋体"}[ND]{lang="EN-US"}]{#struct_0_82812_37953_x370219217}[规则成功，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[IP]{lang="EN-US"}

[[Deleted a session by DHCPv6 event: Interface=*interface-name*, VRF*=vrf*, IP=*ip*, Type=*type*, State=*state*, UserID=*userid*, Service node=*node.*]{lang="EN-US"}]{#struct_0_82812_37953_379709545}

[[因]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_82812_37953_x1188844040}[事件删除]{style="font-family:宋体"}[session]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x1343764578}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPN]{lang="EN-US"}]{#struct_0_82812_37953_x441234838}[：]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[索引]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x177390019}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_82812_37953_1265893919}[：]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话的创建类型，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_x370153681}[：无效类型]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[IF-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_1143109263}[：接口专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[SUBNET-LEASE]{lang="EN-US"}]{#struct_0_82812_37953_x1860346580}[：子网专线]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[STATIC]{lang="EN-US"}]{#struct_0_82812_37953_x1337385607}[：静态配置]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[DHCP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_x308355014}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN-IP-PKT]{lang="EN-US"}]{#struct_0_82812_37953_1265514505}[：未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[RS-PKT]{lang="EN-US"}]{#struct_0_82812_37953_534324629}[：]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_82812_37953_x370743498}[：会话状态，包括以下取值：]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INVALID]{lang="EN-US"}]{#struct_0_82812_37953_1531344710}[：无效状态]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[INIT]{lang="EN-US"}]{#struct_0_82812_37953_21971664}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[OFFLINE]{lang="EN-US"}]{#struct_0_82812_37953_594293188}[：正在下线中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTH]{lang="EN-US"}]{#struct_0_82812_37953_648193630}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHFAIL]{lang="EN-US"}]{#struct_0_82812_37953_x370677962}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[AUTHPASS]{lang="EN-US"}]{#struct_0_82812_37953_1125927370}[：认证成功]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ASSIGNEDIP]{lang="EN-US"}]{#struct_0_82812_37953_x103891423}[：会话已具备]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[ONLINE]{lang="EN-US"}]{#struct_0_82812_37953_x528456061}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[BACKUP]{lang="EN-US"}]{#struct_0_82812_37953_x1082189785}[：备份状态]{style="font-family:宋体"}

[[¡[ ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:5.0pt;font-family:Wingdings"}[UNKNOWN]{lang="EN-US"}]{#struct_0_82812_37953_x370612426}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserID]{lang="EN-US"}]{#struct_0_82812_37953_x49615883}[：用户]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Service node]{lang="EN-US"}]{#struct_0_82812_37953_1952678089}[：服务板卡号]{lang="EN-US" style="font-family:宋体"}

[[Sent an NS packet successfully: Interface=interface, IP=ip, VLAN=vlan, CVLAN =cvlan.]{lang="EN-US"}]{#struct_0_82812_37953_1824635686}

[[发送]{style="font-family:宋体"}[NS]{lang="EN-US"}]{#struct_0_82812_37953_x2065292401}[报文成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_1742408971}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_x370546890}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_1526709771}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_1756187882}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Sent an ICMP6 packet successfully: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_991024597}

[[发送]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_82812_37953_x371005642}[报文成功]{style="font-family:宋体"}[.]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x442474648}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_460996326}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x1124951808}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_1859469583}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[Received an ICMP6 reply: Interface=*interface*, IP=*ip*, VLAN=*vlan*, CVLAN=*cvlan*.]{lang="EN-US"}]{#struct_0_82812_37953_1824635683}

[[接收]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_82812_37953_1906180836}[回复报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface]{lang="EN-US"}]{#struct_0_82812_37953_x968350774}[：接口名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_82812_37953_1481515242}[：]{lang="EN-US" style="font-family:宋体"}[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_82812_37953_x647709230}[LAN]{lang="EN-US"}[：外层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SecVLAN]{lang="EN-US"}]{#struct_0_82812_37953_x370874570}[：内层]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_82812_37953_x838412948}

[[\# ]{lang="EN-US"}]{#struct_0_82812_37953_x1179202611}[打开基于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[的所有调试信息开关。配置静态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，当接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上收到对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_82812_37953_815114125}

[\<Sysname\> terminal debugging]{lang="EN-US"}

[\<Sysname\> debugging ipv6 subscriber all]{lang="EN-US"}

[\<Sysname\>\*Dec  1 17:23:05:900 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=1; FSM EVT: Trigger, EVENT=CREATEANDGO, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INVALID, UserID=0xffffffff, Service node=0x8000.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1590244831}*[状态机事件处理：触发，事件：命令行配置，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:05:900 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INVALID, EVENT=CREATEANDGO, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INVALID, UserID=0xffffffff, Service node=0x8000..]{lang="EN-US"}]{#struct_0_82812_37953_1184831581}

[*[//]{lang="EN-US"}*]{#struct_0_82812_37953_x425268467}*[状态机事件处理：无效状态，事件：命令行配置，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:683 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Started to authen]{lang="EN-US"}]{#struct_0_82812_37953_1331864968}

[ticate unclassified IP packets from 2::1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x987151955}*[接收]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:684 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT = AUTH, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INIT, UserID=0xffffffff, Service node=slot 5 cpu 0..]{lang="EN-US"}]{#struct_0_82812_37953_1501542655}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1792853493}*[状态机事件处理：触发，事件：认证请求，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:685 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state INIT, EVENT =AUTH, Interface=GE5/2/2, VRF=65535, IP=2::1, Type=STATIC, State=INIT, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}]{#struct_0_82812_37953_x370809034}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_769124753}*[状态机事件处理：初始状态，事件：认证请求，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:685 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Session authentication info: domain=radius.]{lang="EN-US"}]{#struct_0_82812_37953_x995380350}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1316018743}*[会话认证信息：认证域]{style="font-family:宋体"}* *[是]{style="font-family:宋体"}[ radius]{lang="EN-US"}*

[[\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed authentication requests and returned success.]{lang="EN-US"}]{#struct_0_82812_37953_x753567973}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x907034063}*[接收到]{style="font-family:宋体"}[AAA]{lang="EN-US"}[的认证回应结果是成功]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed authorization requests and returned success.]{lang="EN-US"}]{#struct_0_82812_37953_x635649304}

[*[// AAA]{lang="EN-US"}*]{#struct_0_82812_37953_1342444305}*[处理授权请求返回结果是成功]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:686 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTH, EVENT=AUTHPASS, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=AUTH, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}]{#struct_0_82812_37953_x790990618}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_1538139784}*[状态机事件处理：状态是认证中，事件：认证成功，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:687 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state AUTHPASS, EVENT=ASSIGNIP, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=AUTHPASS, UserID=0xffffffff, Service node=slot 5 cpu 0.]{lang="EN-US"}]{#struct_0_82812_37953_199050544}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1861372457}*[状态机事件处理：状态是认证成功，事件：分配]{style="font-family:宋体"}[ip]{lang="EN-US"}[地址，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:688 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Rule thread processed request message (MessageType=0).]{lang="EN-US"}]{#struct_0_82812_37953_1544697383}

[*[// rule]{lang="EN-US"}*]{#struct_0_82812_37953_105512084}*[线程处理请求下发]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[消息（消息类型是]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:688 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Requested to add a user-profile rule(UserID=0x40000001).]{lang="EN-US"}]{#struct_0_82812_37953_x370219210}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_380168297}*[请求添加]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[规则（用户]{style="font-family:宋体"}[id]{lang="EN-US"}[是]{style="font-family:宋体"}[0x40000001]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:691 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5;]{lang="EN-US"}]{#struct_0_82812_37953_18625145}

[Received result of user profile settings (UserID=0x40000001, Result=0).]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1907222920}*[接收设置]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[的结果（用户]{style="font-family:宋体"}[id]{lang="EN-US"}[是]{style="font-family:宋体"}[0x40000001]{lang="EN-US"}[，结果是]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:693 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: Trigger, EVENT=USERPROFILE OK, Interface=GE5/2/2, VRF=0, IP=2::1, Type=STATIC, State=ASSIGNEDIP, UserID=0x40000001, Service node=slot 5 cpu 0.]{lang="EN-US"}]{#struct_0_82812_37953_x1375594996}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_x1598705336}*[状态机事件处理：触发，事件：]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[下发成功，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:693 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; FSM EVT: state ASSIGNEDIP, EVENT=USERPROFILE OK, Interface=GE5/2/2, VRF=0, IP =2::1, Type=STATIC, State=ASSIGNEDIP, UserID=0x40000001, Service node=slot 5 cpu 0.]{lang="EN-US"}]{#struct_0_82812_37953_x827412907}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_1614801550}*[状态机事件处理：分配到]{style="font-family:宋体"}[ip]{lang="EN-US"}[地址状态，事件：]{style="font-family:宋体"}[userprofile]{lang="EN-US"}[下发成功，接口是]{style="font-family:宋体"}[GE1/0/1]{lang="EN-US"}[，显示具体的会话信息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:696 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; AAA processed accounting-start requests and returned success..]{lang="EN-US"}]{#struct_0_82812_37953_1240305542}

[*[// AAA]{lang="EN-US"}*]{#struct_0_82812_37953_724559396}*[处理计费开始请求，返回结果是处理成功]{style="font-family:宋体"}*

[[Added a detection user successfully, Interface=GigabitEthernet5/2/2, IP=2::1, VLAN=65535, CVLAN=65535.]{lang="EN-US"}]{#struct_0_82812_37953_2041492760}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_65752737}*[添加探测用户成功]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:697 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=5; Sent mcast user online message.]{lang="EN-US"}]{#struct_0_82812_37953_x1943758594}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_1546671543}*[发送组播用户在线消息]{style="font-family:宋体"}*

[[\*Dec  1 17:23:25:697 2013 Sysname IP6OE/7/EVENT: -MDC=1-Slot=1;]{lang="EN-US"}]{#struct_0_82812_37953_x370153674}

[ User ID            : 0x40000001]{lang="EN-US"}

[ Flag               : 21]{lang="EN-US"}

[ Interface          : GE1/0/1]{lang="EN-US"}

[ VPN instance       : N/A]{lang="EN-US"}

[ Src IP             : 2::1]{lang="EN-US"}

[ PVC ID             : 0]{lang="EN-US"}

[ SVLAN ID           : N/A]{lang="EN-US"}

[ CVLAN ID           : N/A]{lang="EN-US"}

[ MAC address        : N/A]{lang="EN-US"}

[ Service type       : 0]{lang="EN-US"}

[ Access limit       : 4]{lang="EN-US"}

[ User profile       : a]{lang="EN-US"}

[ User name          : a]{lang="EN-US"}

[ User name len      : 1]{lang="EN-US"}

[ Max multicast num  : 0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_82812_37953_1143436946}*[打印传给可控组播的消息]{style="font-family:宋体"}*
