::: {#-944854543 .myid}
[]{#_Toc404785826}[]{#struct_0_18608_20265_x1368158780}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber interface-leased**

------------------------------------------------------------------------

[**[display ip subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_x1527436839}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x346946607}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_1302877713}

[**[display ip subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x366614735}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_567997423}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_93713768}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_x2053447209}[模式：]{style="font-family:宋体"}

[**[display ip subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x154074498}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1051451600}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_918249804}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1687941050}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1610476264}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_1121447380}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x652427575}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x310918574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1965393963}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_1122285357}[：]{style="font-family:宋体;color:black"}[显示指定接口上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1957570988}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1615564112}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:
宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1317406594}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x366811343}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_604842171}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_206739039}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1750615727}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x18293307}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber interface-leased interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x663105361}

[Basic:]{lang="EN-US"}

[  Access interface           : GE1/0/1]{lang="EN-US"}

[  VPN instance               : N/A]{lang="EN-US"}

[  Username                   : a]{lang="EN-US"}

[  User ID                    : 0x30000000]{lang="EN-US"}

[  State                      : Online]{lang="EN-US"}

[  Service node               : Slot ]{lang="EN-US"}[1 CPU 0]{lang="EN-US"}

[  Domain                     : radius]{lang="EN-US"}

[  Login time                 : May 14 20:04:42 2014]{lang="EN-US"}

[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}

[ ]{lang="EN-US"}

[AAA:]{lang="EN-US"}

[  IP pool                    : ipoe]{lang="EN-US"}

[  Session idle time          : N/A]{lang="EN-US"}

[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}

[  Max multicast addresses    : 4]{lang="EN-US"}

[  Multicast address list     : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[QoS:]{lang="EN-US"}

[  User profile               : h3c (active)]{lang="EN-US"}

[  Session group profile      : N/A]{lang="EN-US"}

[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}

[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flow statistic:]{lang="EN-US"}

[  Uplink   packets/bytes     : 0/0]{lang="EN-US"}

[  DownLink packets/bytes     : 0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ITA:]{lang="EN-US"}

[  Level-1 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-3 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-4 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-5 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-6 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-7 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[  Level-8 uplink   packets/bytes: 0/0]{lang="EN-US"}

[          downLink packets/bytes: 0/0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip subscriber interface-leased]{lang="EN-US"}]{#struct_0_18608_20265_1564567493}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2040245735}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x366745807}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x1702860690}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_516252651}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_516318187}[会话的基本信息]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_628668223}

[[用户所在的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_1868459920}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_x1847123187}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_515728362}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_18608_20265_x277312256}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_2134698841}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_x394875464}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_x439581576}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_814902748}

[[用户状态：]{style="font-family:宋体"}]{#struct_0_18608_20265_x365893839}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_841775462}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_x1048317675}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_x1474007041}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_1108583733}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass ]{lang="EN-US"}]{#struct_0_18608_20265_x908415317}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_x435144600}[：]{lang="EN-US" style="font-family:宋体"}[用户已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_340332452}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_x365828303}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_1552645360}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_1936514497}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_515859434}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_6636053}

[[认证使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_x1287816940}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_993608202}

[[用户登录时间，即用户授权成功的时间，格式为设备时间，如：]{style="font-family:宋体"}[YYYY-MM-DD HH:MM:SS UTC]{lang="EN-US"}]{#struct_0_18608_20265_515924970}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_201557644}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_x1364526297}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1359037580}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1285420236}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_x722569489}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_515990506}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_1406847993}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_386891962}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_1735399912}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_516056042}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_1920615211}[：表示未下发会话时长]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_x519186996}[：表示会话时长无限制]{lang="EN-US" style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_x1516782778}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_516121578}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_1509984793}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_725677365}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1895518990}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_516187114}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x437602825}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_174902281}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_796416672}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_516252650}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x565838129}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_1030388977}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_516318186}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_628668222}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_1868459919}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1846533366}[授权的]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_515728365}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in]{lang="EN-US"}[active]{lang="EN-US"}]{#struct_0_18608_20265_807253625}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_x250213912}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_515793901}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x802208956}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1774217494}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_1327201352}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_415082688}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_1383437715}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_515859437}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x935958257}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1479702579}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x935958258}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic]{lang="EN-US"}]{#struct_0_18608_20265_993608201}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1546511400}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_1582228389}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_515924973}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_1359037577}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1285223641}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_515990509}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1406847992}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_386957498}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_516056045}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_1920615218}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_x518597172}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x727960381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_1676345796}

::: {#-1936275722 .myid}
[]{#_Toc404785827}[]{#struct_0_18608_20265_x916876559}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber interface-leased statistics**

------------------------------------------------------------------------

[**[display ip subscriber interface-leased statistics]{lang="EN-US"}**]{#struct_0_18608_20265_1817885778}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1030856205}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_x366745808}

[**[display ip subscriber interface-leased statistics ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x1703319442}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_283379842}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber interface-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1128026795}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_899824104}[模式：]{style="font-family:宋体"}

[**[display ip subscriber interface-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *[chassis-number ]{style="color:black"}***slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x2029519399}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1936136411}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_1579578064}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1252364169}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_328094406}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_x115130309}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x90648038}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1009979030}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1335960151}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x1984685461}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户已经上线和正在上线的统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x365893840}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板中]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1915387797}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1317472130}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x376473124}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持[IRF3]{lang="SV"}的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_2072560855}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="SV"}**]{#struct_0_18608_20265_1133147932}*[cpu-number]{lang="SV"}*[：]{style="font-family:
宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="SV"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="SV"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_2139666218}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1666523047}[显示设备上已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber interface-leased statistics]{lang="EN-US"}]{#struct_0_18608_20265_x1416711947}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip subscriber interface-leased statistics]{lang="EN-US"}]{#struct_0_18608_20265_696207572}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2036410565}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_1873509712}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_712186610}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_532492844}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x365828304}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1552448752}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x2007512735}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1239912545}

[[处于正在认证状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x1340923027}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_x1108335929}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_1000269509}[认证失败]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_x193839713}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x888926923}[认证成功]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_342240899}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x366418129}[拥有]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;
  color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1034910830}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x519629837}[在线]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1610154778}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_x441329802}

[ ]{lang="EN-US"}

::: {#2033260989 .myid}
[]{#_Toc404785828}[]{#struct_0_18608_20265_1309294225}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber offline statistics**

------------------------------------------------------------------------

[**[display ip subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x321456490}[命令用来显示]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线原因的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1973491753}

[**[display ip subscriber offline statistics ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_878165987}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1310826348}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x1312088033}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x366352593}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x968357342}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_x126070492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_519635051}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1594275891}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x866369814}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_738521255}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户下线原因的统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:
宋体"}[IPoE]{lang="EN-US"}[用户下线原因的统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_233731191}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1832479909}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线原因的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber offline statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x2078764076}

[Total               : 100]{lang="EN-US"}

[User request        : 0]{lang="EN-US"}

[DHCP lease expire   : 0]{lang="EN-US"}

[AAA lease expire    : 0]{lang="EN-US"}

[Command cut         : 80]{lang="EN-US"}

[AAA terminate       : 0]{lang="EN-US"}

[Authenticate fail   :]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:8.0pt;color:black"}[0]{lang="EN-US"}

[Authorization fail  : ]{lang="EN-US" style="color:black"}[0]{lang="EN-US"}

[Idle timeout        : 10]{lang="EN-US"}

[Detect fail         : 10]{lang="EN-US"}

[Not enough resource : 0]{lang="EN-US"}

[DHCP request timeout: 0]{lang="EN-US"}

[Interface down      : 0]{lang="EN-US"}

[Interface shutdown  : 0]{lang="EN-US"}

[VSRP event          : 0]{lang="EN-US"}

[DHCP notify         : 0]{lang="EN-US"}

[Other               : 0]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ip subscriber offline statistics]{lang="EN-US"}]{#struct_0_18608_20265_x366549201}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2031083451}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_1822093544}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_1129550261}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_1515139895}

[[下线的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_1973433657}

[[User request]{lang="EN-US"}]{#struct_0_18608_20265_71674137}

[[用户主动要求下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_192061718}

[[DHCP lease expire]{lang="EN-US"}]{#struct_0_18608_20265_x931348725}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x825653492}[租约到期正常下线的用户数]{style="font-family:宋体"}

[[AAA lease expire]{lang="EN-US"}]{#struct_0_18608_20265_1346461554}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_882554856}[租约到期正常下线的用户数]{style="font-family:宋体"}

[[Command cut]{lang="EN-US"}]{#struct_0_18608_20265_x366483665}

[[通过命令行下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x214860005}

[[AAA terminate]{lang="EN-US"}]{#struct_0_18608_20265_1146671905}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1284327377}[强制下线的用户数]{style="font-family:宋体"}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_x960822201}

[[认证失败的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x321910018}

[[Authorization fail]{lang="EN-US"}]{#struct_0_18608_20265_x402128450}

[[授权失败的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x975923788}

[[Idle timeout]{lang="EN-US"}]{#struct_0_18608_20265_x1236109433}

[[用户空闲超时下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x366680273}

[[Detect fail]{lang="EN-US"}]{#struct_0_18608_20265_x576380537}

[[在线探测失败下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x995950022}

[[Not enough resource]{lang="EN-US"}]{#struct_0_18608_20265_618604168}

[[硬件资源不足下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x2123510128}

[[DHCP request timeout]{lang="EN-US"}]{#struct_0_18608_20265_x944608661}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_449754730}[请求超时下线的用户数]{style="font-family:宋体"}

[[Interface down]{lang="EN-US"}]{#struct_0_18608_20265_333035624}

[[因接口状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_18608_20265_x366614737}[下线的用户数]{style="font-family:宋体"}

[[Interface shutdown]{lang="EN-US"}]{#struct_0_18608_20265_567866351}

[[主动]{style="font-family:宋体"}[shutdown]{lang="EN-US"}]{#struct_0_18608_20265_902469988}[接口导致下线的用户数]{style="font-family:宋体"}

[[VSRP event]{lang="EN-US"}]{#struct_0_18608_20265_1245276849}

[[收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_18608_20265_x662861702}[（]{style="font-family:宋体"}[Virtual Service Redundancy Protocol]{lang="EN-US"}[，虚拟业务冗余协议）]{style="font-family:宋体"}

[事件通知而下线的用户数]{style="font-family:宋体"}

[[DHCP notify]{lang="EN-US"}]{#struct_0_18608_20265_x1149790622}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1087574176}[通知下线的用户数]{style="font-family:宋体"}

[[Other]{lang="EN-US"}]{#struct_0_18608_20265_x366811345}

[[其它状况触发下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_206607967}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1378347243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x1815904332}

::: {#-1864132843 .myid}
[]{#_Toc404785829}[]{#struct_0_18608_20265_x234027439}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber session**

------------------------------------------------------------------------

[**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_2040693727}[命令用来显示静态配置和动态触发的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:
宋体"}[IPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1628226298}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_x1394849052}

[**[display ip subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ip** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_x1148747986}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_380023003}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ip** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_x49013977}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_1128467498}[模式：]{style="font-family:宋体"}

[**[display ip subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ip** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_x366745809}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1703253906}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_890852871}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1597971963}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1703106008}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_1031671040}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1483694022}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_985705883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x136059022}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x1317793298}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:
宋体"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_437088206}*[ domain-name]{lang="SV"}*[：显示使用指定]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域认证的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[domain-name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:宋体"}[@]{lang="SV"}["]{style="font-family:
宋体"}[字符。]{style="font-family:宋体"}

[**[ip]{lang="SV"}**]{#struct_0_18608_20265_701368268}*[ ip-address]{lang="SV"}*[：显示]{style="font-family:宋体;color:black"}[指定源]{style="font-family:宋体;color:black"}[IP]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[ip-address]{lang="SV"}*[为指定的]{style="font-family:宋体"}[IPv4]{lang="SV"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="SV"}**]{#struct_0_18608_20265_1009385787}*[vpn-instance-name]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[指定用户所属的]{style="font-family:宋体;
color:black"}[VPN]{lang="SV" style="color:black"}[，]{style="font-family:宋体;color:black"}*[vpn-instance-name]{lang="SV"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="SV"}[的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[31]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[ IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mac ]{lang="SV"}**]{#struct_0_18608_20265_x338728180}*[mac-address]{lang="SV"}*[：显示]{style="font-family:
宋体;color:black"}[指定源]{style="font-family:宋体;color:black"}[MAC]{lang="SV" style="color:black"}[地址的]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体;color:black"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_18608_20265_x79329386}[：显示]{style="font-family:宋体;color:black"}[静态配置的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，不指定该参数时将显示静态配置的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话和动态触发创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[username ]{lang="SV"}**]{#struct_0_18608_20265_x365893841}*[name]{lang="SV"}*[：显示指定]{style="font-family:宋体;
color:black"}[用户名的]{style="font-family:宋体;color:black"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体;color:black"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:
宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1915322261}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1587682320}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_248546275}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x806515209}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1317537666}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_1902131274}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18608_20265_x1169123223}[：显示]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话[的详细信息。]{style="color:black"}]{style="font-family:宋体"}[如果不指定该参数，则只显示]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1477738705}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1659932622}[显示用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber session ip 1.1.1.1 vpn-instance vpn1]{lang="EN-US"}]{#struct_0_18608_20265_408369845}

[  Type: D-Dhcp   S-Static     U-Unclassified-ip    N-Ndrs ]{lang="EN-US"}

[Interface            IP address                MAC address    Type  State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[GE1/0/1]{lang="EN-US"}[              1.1.1.1                   000d-88f8-0eab D     Online]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x844251558}[显示所有静态配置和动态触发的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[的详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber session verbose]{lang="EN-US"}]{#struct_0_18608_20265_1456375106}

[[ Basic:]{lang="EN-US"}]{#struct_0_18608_20265_x365828305}

[[  Username                   : abc]{lang="EN-US"}]{#struct_0_18608_20265_515793903}

[[  Domain                     : radius]{lang="EN-US"}]{#struct_0_18608_20265_x802208958}

[[  VPN instance               : vpn1]{lang="EN-US"}]{#struct_0_18608_20265_1383830931}

[[  IP address                 : 1.1.1.1]{lang="EN-US"}]{#struct_0_18608_20265_x1170704789}

[[  MAC address                : 000d-88f8-0eab]{lang="EN-US"}]{#struct_0_18608_20265_1424575263}

[[  Service-VLAN/Customer-VLAN : -/-]{lang="EN-US"}]{#struct_0_18608_20265_x554511002}

[[  Access interface           : GE1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_1794014670}

[[  User ID                    : 0x380800b5]{lang="EN-US"}]{#struct_0_18608_20265_1616915231}

[[  VPI/VCI(for ATM)           : -/-]{lang="EN-US"}]{#struct_0_18608_20265_515859439}

[[  DHCP lease                 : N/A]{lang="EN-US"}]{#struct_0_18608_20265_993608191}

[[  DHCP remain lease          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x333922809}

[[  Login time                 : May  9 08:56:29 2014]{lang="EN-US"}]{#struct_0_18608_20265_805162030}

[[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}]{#struct_0_18608_20265_x201857955}

[[  Service node               : Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_18608_20265_x985907624}

[[  Type                       : Static]{lang="EN-US"}]{#struct_0_18608_20265_63021854}

[[  State                      : Online]{lang="EN-US"}]{#struct_0_18608_20265_x696493490}

[ ]{lang="EN-US"}

[[AAA:]{lang="EN-US"}]{#struct_0_18608_20265_543606876}

[[  IP pool                    : N/A]{lang="EN-US"}]{#struct_0_18608_20265_542157037}

[[  Session idle time          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_515924975}

[[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}]{#struct_0_18608_20265_1359037575}

[[  Max multicast addresses    : 4]{lang="EN-US"}]{#struct_0_18608_20265_1285092569}

[[  Multicast address list     : N/A]{lang="EN-US"}]{#struct_0_18608_20265_430083650}

[ ]{lang="EN-US"}

[[QoS:]{lang="EN-US"}]{#struct_0_18608_20265_1829172917}

[[  User profile               : abc (active)]{lang="EN-US"}]{#struct_0_18608_20265_x2093212424}

[[  Session group profile      : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1089734011}

[[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_571028056}

[[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_1708651612}

[ ]{lang="EN-US"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_1786812483}

[[  Uplink   packets/bytes     : 594341/76075648]{lang="EN-US"}]{#struct_0_18608_20265_515990511}

[[  DownLink packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x931804160}

[ ]{lang="EN-US"}

[[ITA:]{lang="EN-US"}]{#struct_0_18608_20265_1176572073}

[[  Level-1 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_1657019797}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x212708026}

[[  Level-2 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_1240168346}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1054992531}

[[  Level-3 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_x1644283213}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x396874482}

[[  Level-4 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_x1738016483}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_516056047}

[[  Level-5 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_1920615216}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x518728244}

[[  Level-6 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_1643149211}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x2070127320}

[[  Level-7 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_180224597}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1781099316}

[[  Level-8 uplink   packets/bytes: 66038/8452864]{lang="EN-US"}]{#struct_0_18608_20265_x1712765131}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_142422346}

[[表1-3 ]{lang="EN-US"}[display ip subscriber session]{lang="EN-US"}]{#struct_0_18608_20265_1552514288}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2061765139}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x1982705143}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x971067240}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_516121583}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1593341426}[会话的基本信息]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_18608_20265_516187119}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_x437602830}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_1034321006}

[[用户认证时使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_x1721065309}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_386127425}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_x1707664017}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_18608_20265_1075518278}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18608_20265_1254657927}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_18608_20265_x537332592}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18608_20265_x374420610}[地址]{style="font-family:宋体"}

[[Service-VLAN/Customer-VLAN]{lang="EN-US"}]{#struct_0_18608_20265_516252655}

[[用户所在的公网]{style="font-family:宋体"}[VLAN/]{lang="EN-US"}]{#struct_0_18608_20265_x565838124}[私网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_516318191}

[[用户接入的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_x1709983931}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_267234043}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_x1008064539}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[VPI/VCI(for ATM)]{lang="EN-US"}]{#struct_0_18608_20265_1794498373}

[[ATM]{lang="EN-US"}]{#struct_0_18608_20265_526168911}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[DHCP lease]{lang="EN-US"}]{#struct_0_18608_20265_515728366}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_515793902}[服务器分配给用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x802208959}[：表示无]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_1383765395}[：表示租约无限长]{lang="EN-US" style="font-family:宋体"}

[[DHCP remain lease]{lang="EN-US"}]{#struct_0_18608_20265_751222289}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_515859438}[服务器分配给用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_993608190}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_x333922808}

[[用户登录时间，即用户授权成功的时间，格式为设备时间，如：]{style="font-family:宋体"}[YYYY-MM-DD HH:MM:SS UTC]{lang="EN-US"}]{#struct_0_18608_20265_515924974}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_1792818782}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_241152724}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_1359037576}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_1285289177}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_515990510}

[[Type]{lang="EN-US"}]{#struct_0_18608_20265_x1707164578}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1833263690}[会话的创建类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_828803567}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unclassified-ip]{lang="EN-US"}]{#struct_0_18608_20265_x1411655675}[：未知源]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[报文触发创建]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_18608_20265_x1684902796}[：静态配置]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_x366483658}

[[用户状态：]{style="font-family:宋体"}]{#struct_0_18608_20265_x214663400}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_x1000719426}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_x234286908}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}[中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_498727099}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_x1225825622}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass]{lang="EN-US"}]{#struct_0_18608_20265_x366680266}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_x576183928}[：]{lang="EN-US" style="font-family:宋体"}[会话已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_x561285480}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_x1132435552}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_516056046}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_516121582}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_x1593341425}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1549121920}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_516187118}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x437602829}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_516252654}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x565838125}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_1029602545}[：表示未授权会话时长]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_516318190}[：表示会话时长无限制]{lang="EN-US" style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_x1709983932}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x77890276}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_2081812304}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_x328630093}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_210502049}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_2081877840}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_845137854}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_x2051349545}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_2081943376}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_x1901464314}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x784829356}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_2082008912}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x1565473254}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_2082074448}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_x471974559}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x365832883}[授权的]{style="font-family:宋体"}[Session ]{lang="EN-US"}[Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session ]{lang="EN-US"}[Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_2082139984}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_1157446235}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:
  宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_2082205520}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_315077044}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x790225738}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_638019852}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_638019859}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x1443580741}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_2082271056}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_695066439}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_638019858}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1443580740}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_1789244829}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic]{lang="EN-US"}]{#struct_0_18608_20265_109065203}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_2082336592}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_711873419}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_2082402128}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x843087295}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x687224486}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_2081812303}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x328171341}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_2081877839}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_845727677}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1180007623}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_2081943375}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1819425341 .myid}
[]{#_Toc404785830}[]{#struct_0_18608_20265_1672864874}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber session statistics**

------------------------------------------------------------------------

[**[display ip subscriber session statistics]{lang="EN-US"}**]{#struct_0_18608_20265_560596593}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1542215910}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_x131340729}

[**[display ip subscriber session statistics ]{lang="EN-US"}**[\[ **session-type** { **dhcp** \| **static** \| **unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x366680267}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_x576118392}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber session statistics ]{lang="EN-US"}**[\[ **session-type** { **dhcp** \| **static** \| **unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1716822758}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_993803953}[模式：]{style="font-family:宋体"}

[**[display ip subscriber session statistics ]{lang="EN-US"}**[\[ **session-type** { **dhcp** \| **static** \| **unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *[chassis-number ]{style="color:black"}***slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_1369924321}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_805512463}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_327380046}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1582115607}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x2143044007}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1242749814}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1092395233}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1758554137}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1077074948}

[**[session-type]{lang="EN-US"}**]{#struct_0_18608_20265_1501736243}[：用户上线类型。]{style="font-family:宋体"}[不指定该参数，则表示显示所有类型的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[**[dhcp]{lang="EN-US"}**]{#struct_0_18608_20265_1286212794}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_18608_20265_x366614731}[：]{style="font-family:宋体"}[表示静态个人用户。]{style="font-family:宋体"}

[**[unclassified-ip]{lang="EN-US"}**]{#struct_0_18608_20265_568259567}[：表示]{style="font-family:宋体"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x2087735842}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1057249607}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[ slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1109618420}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:
宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1389468719}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x536951212}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持[IRF3]{lang="SV"}的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1339414636}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="SV"}**]{#struct_0_18608_20265_x1559859621}*[cpu-number]{lang="SV"}*[：]{style="font-family:
宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="SV"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="SV"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_453618952}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1494495221}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber session statistics session-type dhcp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x1537034756}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ip subscriber session statistics]{lang="EN-US"}]{#struct_0_18608_20265_2140411881}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2053353165}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x366811339}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_207394404}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_x1017841243}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_2002531135}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_488868900}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_2003776248}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1272316036}

[[处于正在认证状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x771886897}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_2033827501}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_352889281}[认证失败]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_x1547037908}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x366745803}[认证成功]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1702598546}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x436299060}[成功分配到]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;
  color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1397943768}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x1158268174}[在线]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1848704686}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_1609265409}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1218997042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_431650973}

::: {#-111112461 .myid}
[]{#_Toc404785831}[]{#struct_0_18608_20265_x1975771005}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber subnet-leased**

------------------------------------------------------------------------

[**[display ip subscriber subnet-leased]{lang="EN-US"}**]{#struct_0_18608_20265_x365893835}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1915060122}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_20907303}

[**[display ip subscriber subnet-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_571558032}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_x502074233}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber subnet-leased]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_1941422828}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_1567250974}[模式]{style="font-family:宋体"}

[**[display ip subscriber subnet-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1107078128}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x458982683}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x1023800896}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1313688316}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1813484768}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_103252449}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1941193237}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_1927663387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x365828299}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x403014409}[：]{style="font-family:宋体;color:black"}[显示指定接口上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x986332438}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1588438186}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:
宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1342414552}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_249436234}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1952943903}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_62546511}[：]{style="font-family:
宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x67788850}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1885625898}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[子网专线用户信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber subnet-leased interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x769702653}

[Basic:]{lang="EN-US"}

[  Access interface           : GE1/0/1]{lang="EN-US"}

[[  VPN instance               : N/A]{lang="EN-US"}]{#struct_0_18608_20265_2082074450}

[[  Username                   : a]{lang="EN-US"}]{#struct_0_18608_20265_x472498846}

[[  Network                    : 11.11.11.0/24]{lang="EN-US"}]{#struct_0_18608_20265_2082139986}

[[  User ID                    : 0x30000001]{lang="EN-US"}]{#struct_0_18608_20265_1157315163}

[[  State                      : Online]{lang="EN-US"}]{#struct_0_18608_20265_x1533026773}

[[  Service node               : Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_18608_20265_x1792798181}

[[  Domain                     : radius]{lang="EN-US"}]{#struct_0_18608_20265_1229536511}

[[  Login time                 : May 14 20:08:35 2014]{lang="EN-US"}]{#struct_0_18608_20265_1246120456}

[[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}]{#struct_0_18608_20265_1389403183}

[ ]{lang="EN-US"}

[[AAA:]{lang="EN-US"}]{#struct_0_18608_20265_319636412}

[[  IP pool                    : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x26861004}

[[  Session idle time          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_2082205522}

[[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}]{#struct_0_18608_20265_314945972}

[[  Max multicast addresses    : 4]{lang="EN-US"}]{#struct_0_18608_20265_1215714633}

[[  Multicast address list     : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1110890291}

[ ]{lang="EN-US"}

[[QoS:]{lang="EN-US"}]{#struct_0_18608_20265_142672932}

[[  User profile               : cc (active)]{lang="EN-US"}]{#struct_0_18608_20265_1193757940}

[[  Session group profile      : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1294349077}

[[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_351273464}

[[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_2082271058}

[ ]{lang="EN-US"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_695983943}

[[  Uplink   packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x467060524}

[[  DownLink packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1105666146}

[ ]{lang="EN-US"}

[[ITA:]{lang="EN-US"}]{#struct_0_18608_20265_x615445286}

[[  Level-1 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1637953653}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1071216495}

[[  Level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1652161115}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x343625643}

[[  Level-3 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_2082336594}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_712266635}

[[  Level-4 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_780939257}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x2108088112}

[[  Level-5 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1453916589}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_287458694}

[[  Level-6 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_965731407}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x973573936}

[[  Level-7 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_2082402130}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x842563006}

[[  Level-8 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1208196244}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1474628869}

[[表1-5 ]{lang="EN-US"}[display ip subscriber subnet-leased]{lang="EN-US"}]{#struct_0_18608_20265_935660191}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2047787801}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x1278030373}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_998835017}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_2081812305}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x328564557}[会话的基本信息]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_x525979950}

[[用户所在的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_2081877841}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_845203390}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_1383456969}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[User name]{lang="EN-US"}]{#struct_0_18608_20265_x1721382561}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_1355024269}

[[Network]{lang="EN-US"}]{#struct_0_18608_20265_x786083157}

[[用户所在的子网地址]{style="font-family:宋体"}]{#struct_0_18608_20265_x769637117}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_x271691325}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_143560228}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_x1242694121}

[[用户的认证状态]{style="font-family:宋体"}]{#struct_0_18608_20265_1729428596}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_46042651}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_x1621730669}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}[中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_x1821583200}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_x769833725}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass]{lang="EN-US"}]{#struct_0_18608_20265_1315209114}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_1309488547}[：]{lang="EN-US" style="font-family:宋体"}[会话已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_x1476474822}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_x1607526157}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_2082074449}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_x471909023}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_1619716463}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_x38430854}

[[用户认证时使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_x769768189}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_2082139985}

[[用户登录时间]{style="font-family:宋体"}]{#struct_0_18608_20265_2082205521}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_x936261181}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_1342283480}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_315011508}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x780741279}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_x585713240}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_2082271057}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_695131975}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_465844009}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_2082336593}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_711938955}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_1532697472}[：表示未授权会话时长]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_2082402129}[：表示会话时长无限制]{lang="EN-US" style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_x843152831}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_2037720980}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_2081812308}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_x328892237}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_979561235}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_869895385}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_2081877844}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_844875710}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1592661589}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_2081943380}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1901071099}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_2082008916}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x1565211110}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_282351580}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_2082074452}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x472629918}[授权的]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_1909188941}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_2082139988}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:
  宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_1156659803}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_1165448460}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_2082205524}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x933795572}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x500393042}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_503938177}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_315339188}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1049995163}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x933795565}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x500327507}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_134762225}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic]{lang="EN-US"}]{#struct_0_18608_20265_2082271060}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_695459652}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_2082336596}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_712135563}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x246563801}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_2082402132}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_x842694078}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1645625125}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_2081812307}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_x328433485}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x957849807}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_2081877843}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_321656243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_1013519317}

::: {#862972530 .myid}
[]{#_Toc404785832}[]{#struct_0_18608_20265_1009530048}

**IPoE \-- IPv4 IPoE配置命令 \-- display ip subscriber subnet-leased statistics**

------------------------------------------------------------------------

[**[display ip subscriber subnet-leased statistics]{lang="EN-US"}**]{#struct_0_18608_20265_1633100611}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1482036474}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_x1912381267}

[**[display ip subscriber subnet-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x1325949357}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_x2030362307}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip subscriber subnet-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x769637118}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_x271494717}[模式：]{style="font-family:宋体"}

[**[display ip subscriber]{lang="EN-US"}**[ **subnet-leased statistics** \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *[chassis-number ]{style="color:black"}***slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_138269930}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1594865933}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x1553010032}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x895390109}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1482676796}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_359125241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1677354675}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x2038757482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_875758724}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x1147269613}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户已经上线和正在上线的子网专线统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_449713430}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x769833726}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1389272111}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1315405722}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_338136701}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="SV"}**]{#struct_0_18608_20265_130769524}*[cpu-number]{lang="SV"}*[：]{style="font-family:
宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="SV"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="SV"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式[/]{lang="EN-US"}集中式[IRF]{lang="EN-US"}设备[/]{lang="EN-US"}分布式设备－[IRF]{lang="EN-US"}模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1043950251}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x451263820}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上已经上线和正在上线的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip subscriber ]{lang="EN-US"}]{#struct_0_18608_20265_x429353964}**[subnet-leased]{lang="EN-US" style="font-size:9.5pt;font-family:\"Courier New\";color:black;
background:#CCE8CC;font-weight:normal"}**[ statistics interface gigabitethernet 1/0/1]{lang="EN-US"}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ip subscriber ]{lang="EN-US"}]{#struct_0_18608_20265_x134062386}**[subnet-leased]{lang="EN-US" style="font-size:9.5pt;font-family:\"Arial\",\"sans-serif\";color:black;background:
#CCE8CC;font-weight:normal"}**[ statistics]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2073206229}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x377828643}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x361275865}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_x1732614237}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x769768190}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1735818389}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x448218894}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1889645947}

[[处于]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_337886771}[正在认证状态的用户数]{style="font-family:
  宋体"}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_x1382190557}

[[处于认证失败]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_x2091195491}[状态]{style="font-family:
  宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_x528973510}

[[处于认证成功]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_1255694220}[状态]{style="font-family:
  宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x769964798}

[[处于成功分配到]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x260180965}[地址]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x742973253}

[[处于在线]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_450927890}[状态]{style="font-family:
  宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_699315200}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_x815246959}

[ ]{lang="EN-US"}

::: {#1650155390 .myid}
[]{#_Toc404785833}[]{#struct_0_18608_20265_x1053368306}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber 8021p**

------------------------------------------------------------------------

[**[ip subscriber 8021p]{lang="EN-US"}**]{#struct_0_18608_20265_x1370825112}[命令用于配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[中的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[**[undo ip subscriber 8021p]{lang="EN-US"}**]{#struct_0_18608_20265_1752125530}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769899262}

[**[ip subscriber 8021p]{lang="EN-US"}**[ *8021p-list* **domain** *domain-name*]{lang="EN-US"}]{#struct_0_18608_20265_x1374162552}

[**[undo ip subscriber 8021p ]{lang="EN-US"}***[8021p-list]{lang="EN-US"}*]{#struct_0_18608_20265_1926181206}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x905074596}

[[未指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_1810809569}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[中的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_455750752}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_552132597}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_292406566}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_777898388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_652382460}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_2081637622}

[*[8021p-list]{lang="SV"}*]{#struct_0_18608_20265_2000668930}[：]{style="font-family:宋体;color:black"}[802.1p]{lang="SV"}[值]{style="font-family:宋体"}[列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示一个或多个]{style="font-family:宋体"}[802.1p]{lang="SV"}[值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[8021p-list]{lang="SV"}*[ = { *8021p-value* \[ **to** *8021p-value* \] }&\<1-8\>]{lang="SV"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[8021p-value]{lang="SV"}*[为指定]{style="font-family:宋体"}*[8021p]{lang="SV"}*[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="SV"}[～]{style="font-family:宋体"}[7]{lang="SV"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_607108226}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[8021p]{lang="SV"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2074738506}

[[本命令用来配置指定]{style="font-family:宋体;color:windowtext"}]{#struct_0_18608_20265_x286439232}[802.1p]{lang="EN-US" style="color:windowtext"}[值范围内的未知源]{style="font-family:宋体;
color:windowtext"}[IP]{lang="EN-US" style="color:windowtext"}[接入用户认证时使用的认证域，通过指定的认证域对进行认证、授权、计费。]{style="font-family:宋体;color:windowtext"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x770095870}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1646813034}[在子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.100]{lang="SV"}[上配置内层]{style="font-family:宋体"}[VLAN TAG]{lang="SV"}[中]{style="font-family:宋体"}[802.1p]{lang="SV"}[值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[2]{lang="SV"}[到]{style="font-family:宋体"}[5]{lang="SV"}[的]{style="font-family:宋体"}[IPv4]{lang="SV"}[未知源]{style="font-family:
宋体"}[IP]{lang="SV"}[接入]{style="font-family:宋体"}[用户认证使用的]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域为]{style="font-family:宋体"}[1pdm]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_828821045}

[\[Sysname\] interface gigabitethernet 1/0/1.100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ip subscriber service-identify 8021p second-vlan]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ip subscriber 8021p 2 to 5 domain 1pdm]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1793158854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x57131204}
:::

::: {#1704666007 .myid}
[]{#_Toc404785834}[]{#struct_0_18608_20265_1357769583}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber dhcp domain**

------------------------------------------------------------------------

[**[ip subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_251942117}[命令用来配置]{style="font-family:
宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用的认证域。]{style="font-family:
宋体"}

[**[undo ip subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_1677296781}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1056239842}

[**[ip subscriber dhcp domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_1383683476}

[**[undo]{lang="EN-US"}**[ **ip subscriber dhcp domain**]{lang="EN-US"}]{#struct_0_18608_20265_726925966}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1664022067}

[[IPv4 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x401536961}[个人接入用户的认证域为缺省认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x770030334}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1219428765}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_440969591}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1286428341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_743428626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x839314909}

[*[domain-name]{lang="SV"}*]{#struct_0_18608_20265_29102022}[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1180234801}

[[本命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x213303178}[报文触发接入的]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户在认证时使用的域名，该域名必须在接入设备上存在且配置完整。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[ip subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_x268340110}[命令后，如果]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中携带]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[，]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[内容符合域名的格式要求，并且接口配置了]{style="font-family:宋体"}**[ip subscriber trust option60]{lang="EN-US"}**[命令]{style="font-family:宋体"}[，则]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[中的信息作为指定的认证域进行认证；否则，使用本命令指定的认证域。]{style="font-family:宋体"}

[[如果不配置]{style="font-family:宋体"}**[ip subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_x2098716444}[命令，且]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中未携带]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[，则使用缺省认证域认证。]{style="font-family:宋体"}

[[当用户需要将]{style="font-family:宋体"}[Option 60]{lang="EN-US"}]{#struct_0_18608_20265_x564462750}[字段中的信息按字符串形式解析时，请确保]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[字段内容中不出现字符串结束字符和不可见字符，否则在生成域名时将产生异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1750332802}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_2120715396}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用的认证域为]{style="font-family:宋体"}[ipoe]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x769178366}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber dhcp domain ipoe]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_2120055782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_542493062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_1120205312}
:::

::: {#-330909306 .myid}
[]{#_Toc404785835}[]{#struct_0_18608_20265_x200662573}[]{#_Toc380594776}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber dhcp max-session**

------------------------------------------------------------------------

[**[ip subscriber dhcp max-session]{lang="EN-US"}**]{#struct_0_18608_20265_x281540497}[命令用来配置接口上允许]{style="font-family:
宋体"}[DHCPv4]{lang="EN-US"}[报文触发创建的]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的最大数。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber** **dhcp** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_1876509908}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1064953103}

[**[ip subscriber dhcp]{lang="EN-US"}**[ **max-session** *max-number*]{lang="EN-US"}]{#struct_0_18608_20265_915342339}

[**[undo]{lang="EN-US"}**[ **ip subscriber** **dhcp** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_x1280646053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x338219352}

[[未限制接口上允许]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_1102254633}[报文触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1440872085}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1739217312}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_464107404}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x769112830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1454175753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1222859757}

[*[max-number]{lang="EN-US"}*]{#struct_0_18608_20265_603735764}[：允许]{style="font-family:宋体;color:black"}[DHCPv4]{lang="EN-US" style="color:black"}[报文触发]{style="font-family:宋体;
color:black"}[创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1310169382}

[[DHCPv4]{lang="SV"}]{#struct_0_18608_20265_x6146757}[报文触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话数目]{style="font-family:宋体"}[达到最大值后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[后续]{style="font-family:宋体"}[DHCPv4]{lang="SV"}[报文不能触发创建]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1098165837}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1477213912}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上允许]{style="font-family:宋体"}[DHCPv4]{lang="SV"}[报[文]{style="color:black"}触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[最大数为]{style="font-family:宋体"}[100]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x1163875869}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber dhcp max-session 100]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1025828370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1202163325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x432951506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x689934755}
:::

::: {#-2049183674 .myid}
[]{#_Toc404785836}[]{#struct_0_18608_20265_x1242176527}[]{#_Toc403480390}[]{#_Toc401341512}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber dhcp password option60**

------------------------------------------------------------------------

[**[ip subscriber dhcp password option60]{lang="EN-US"}**]{#struct_0_18608_20265_1343325280}[命令用来配置]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[**[undo ip subscriber dhcp password option60]{lang="EN-US"}**]{#struct_0_18608_20265_x394205664}[命令用来取消]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_323907414}

[**[ip subscriber dhcp password option60 ]{lang="EN-US"}**[\[ **offset** *offset* \] \[ **length** *length* \]]{lang="EN-US"}]{#struct_0_18608_20265_2144287273}

[**[undo]{lang="EN-US"}**[ **ip subscriber dhcp password option60**]{lang="EN-US"}]{#struct_0_18608_20265_x1943539705}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_951010460}

[[IPv4 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1438709113}[个人接入用户未使用]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1557939448}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1852877782}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1386993716}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1100545615}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x79377113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1359302231}

[**[offset ]{lang="EN-US"}***[offset]{lang="EN-US"}*]{#struct_0_18608_20265_x700664249}[：表示从]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[首部偏移指定字节后的内容作为认证密码，]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[表示字节偏移量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，单位为字节。如果未指定本参数，将从]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[首部后的内容作为认证密码。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}***[ length]{lang="EN-US"}*]{#struct_0_18608_20265_740082707}[：表示从]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[所处的位置开始，取指定长度的字节作为认证密码，]{style="font-family:宋体"}*[length]{lang="EN-US"}*[表示获取字节的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，单位为字节。如果未指定本参数，将从]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[所处的位置开始取剩余的所有内容作为认证密码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1241683650}

[[本命令用来配置]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1613566824}[报文触发接入的]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户在认证时使用的认证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[ip subscriber dhcp password option60]{lang="EN-US"}**]{#struct_0_18608_20265_x747600182}[命令后，]{lang="EN-US" style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户认证密码的选择情况如下：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果]{lang="EN-US" style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_1795690903}[报文中携带的]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[可用（]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[内容为可见字符，]{lang="EN-US" style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[126]{lang="EN-US"}[），则使用]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[中的指定范围的]{lang="EN-US" style="font-family:宋体"}[Option]{lang="EN-US"}[内容作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果]{lang="EN-US" style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_137058410}[报文中未携带]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[，或者]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[内容不符合可见字符的格式要求（可见字符，]{lang="EN-US" style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[126]{lang="EN-US"}[），但同时配置了]{lang="EN-US" style="font-family:宋体"}**[ip subscriber password]{lang="EN-US"}**[命令，则使用]{lang="EN-US" style="font-family:
宋体"}**[ip subscriber password]{lang="EN-US"}**[命令配置的密码；否则使用缺省字符串]{lang="EN-US" style="font-family:宋体"}[vlan]{lang="EN-US"}[作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未配置]{lang="EN-US" style="font-family:宋体"}**[ip subscriber dhcp password option60]{lang="EN-US"}**]{#struct_0_18608_20265_1486706828}[命令，但是配置了]{lang="EN-US" style="font-family:宋体"}**[ip subscriber password]{lang="EN-US"}**[命令，则使用]{lang="EN-US" style="font-family:宋体"}**[ip subscriber password]{lang="EN-US"}**[命令配置的密码；否则使用缺省字符串]{lang="EN-US" style="font-family:
宋体"}[vlan]{lang="EN-US"}[作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18608_20265_x2134351799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在配置了信任]{lang="EN-US" style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_x406664079}[报文中的]{lang="EN-US" style="font-family:宋体"}[Option 60]{lang="EN-US"}[的情况下，配置的]{lang="EN-US" style="font-family:宋体"}**[ip subscriber dhcp password option60]{lang="EN-US"}**[命令才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户需要将]{style="font-family:宋体"}]{#struct_0_18608_20265_x1993227247}[Option 60]{lang="EN-US"}[字段中的信息作为认证密码时，请确保]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[字段内容中不出现字符串结束字符和不可见字符（可见字符，]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[126]{lang="EN-US"}[），否则在生成用户密码时将产生异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x571301658}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1384549789}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用从]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}[10]{lang="EN-US"}[个字节后的]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节内容作为认证密码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1296284006}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber dhcp password option60 offset 10 length 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1785908799}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_1083422301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x827617864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_61574401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x966519701}
:::

::: {#-591524956 .myid}
[]{#_Toc404785837}[]{#struct_0_18608_20265_x769702655}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber dhcp username**

------------------------------------------------------------------------

[**[ip subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_935266975}[命令用来配置]{style="font-family:
宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户的认证用户名。]{style="font-family:
宋体"}

[**[undo ip subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x306023761}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_657882081}

[**[ip subscriber]{lang="EN-US"}**[ **dhcp** **username include** { **circuit-id** \| **client-id** \| **nas-port-id** \| **port** \[ *separator* \] \| **remote-id** \| **second-vlan** \[ *separator* \] \| **slot** \[ *separator* \] \| **source-mac** \[ **separator** *separator* \] \| **subslot** \[ *separator* \] \| **sysname** \[ *separator* \] \| **vendor-class** \| **vendor-specific** \| **vlan** \[ *separator* \] } \*]{lang="EN-US"}]{#struct_0_18608_20265_x1946740600}

[**[undo]{lang="EN-US"}**[ **ip subscriber dhcp username**]{lang="EN-US"}]{#struct_0_18608_20265_858174118}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1601698422}

[[IPv4 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x788618681}[个人接入用户使用报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为认证用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1262526555}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x495448376}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_2043052370}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_342183462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1252480904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1111172237}

[**[circuit-id]{lang="EN-US"}**]{#struct_0_18608_20265_x769637119}[：]{style="font-family:宋体;color:black"}[表示以]{style="font-family:宋体"}[DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Interface Identifier Option]{lang="SV"}[（]{style="font-family:宋体"}[Option82 sub-option1]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息为用户名。]{style="font-family:宋体"}

[**[client-id]{lang="EN-US"}**]{#struct_0_18608_20265_x271560253}[：表示]{style="font-family:宋体;color:black"}[以]{style="font-family:宋体;color:black"}[DHCP]{lang="SV" style="color:black"}[报文中的]{style="font-family:宋体;color:black"}[Client Identifier Option]{lang="EN-US" style="color:black"}[（]{style="font-family:
宋体;color:black"}[Option61]{lang="EN-US" style="color:black"}[）]{style="font-family:宋体;color:black"}[字段]{style="font-family:宋体"}[中的信息作为用户名。]{style="font-family:宋体;color:black"}

[**[nas-port-id]{lang="SV"}**]{#struct_0_18608_20265_930611813}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="SV"}[属性作为用户名。]{style="font-family:宋体"}

[**[port]{lang="SV"}**]{#struct_0_18608_20265_1022519570}[：]{style="font-family:宋体"}[表示以报文接入的端口号作为用户名。]{style="font-family:宋体"}

[**[remote-id]{lang="SV"}**]{#struct_0_18608_20265_x1700010326}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Remote Identifier Option]{lang="SV"}[（]{style="font-family:宋体"}[Option82 sub-option2]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息作为用户名。]{style="font-family:
宋体"}

[**[s]{lang="EN-US"}**]{#struct_0_18608_20265_x197899093}**[econd-vlan]{lang="SV"}**[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1581583677}[：]{style="font-family:宋体"}[表示以报文接入的槽位号作为用户名。]{style="font-family:宋体"}

[**[source-mac]{lang="SV"}**]{#struct_0_18608_20265_1673386600}[：]{style="font-family:宋体;color:black"}[表示以用户报文的源]{style="font-family:宋体;
color:black"}[MAC]{lang="SV" style="color:black"}[地址作为用户名。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="SV"}**]{#struct_0_18608_20265_87290059}*[separator]{lang="SV"}*[：]{style="font-family:
宋体"}[MAC]{lang="SV"}[地址分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以为任意可配置的可见字符。若指定了分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="SV"}["，]{style="font-family:
宋体"}[则用户名形如]{style="font-family:宋体"}[xxxx-xxxx-xxxx]{lang="SV"}[；]{style="font-family:宋体"}[若不指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则用户名为]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="SV"}[形式。]{style="font-family:宋体"}

[**[subslot]{lang="SV"}**]{#struct_0_18608_20265_x837615056}[：]{style="font-family:宋体"}[表示以报文接入的子卡号作为用户名。]{style="font-family:宋体"}

[**[sysname]{lang="SV"}**]{#struct_0_18608_20265_1805687761}[：]{style="font-family:宋体"}[表示以报文接入设备的设备名作为用户名。]{style="font-family:宋体"}

[**[vendor-class]{lang="SV"}**]{#struct_0_18608_20265_529843995}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Vendor Class Option]{lang="SV"}[（]{style="font-family:宋体"}[Option60]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息作为用户名。]{style="font-family:宋体"}

[**[vendor-specific]{lang="SV"}**]{#struct_0_18608_20265_1062678205}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Vendor Specific Option]{lang="SV"}[（]{style="font-family:宋体"}[Option82 sub-option9]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息作为用户名。]{style="font-family:
宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_1022519569}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[*[separator]{lang="SV"}*]{#struct_0_18608_20265_x198357846}[：]{style="font-family:宋体"}[当前字段分隔符，用在当前字段后面以连接后面的一个字段，可以为任意可配置的可见字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1113739598}

[[该命令用来配置]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_331897465}[用户在认证时使用的用户名，该用户名必须与认证服务器上配置的用户名保持一致。]{style="font-family:宋体"}

[[在允许的用户名类型范围内，该命令支持任意形式、任意顺序的用户名组合。例如：若配置]{style="font-family:宋体"}**[ip subscriber dhcp username include vendor-class vendor-specific]{lang="EN-US"}**]{#struct_0_18608_20265_x1309946387}[，则用户名为]{style="font-family:宋体"}[Option60]{lang="SV"}[字段内容和]{style="font-family:宋体"}[Option82 sub9]{lang="SV"}[字段内容的拼接，且两个字段之间无分隔符。]{style="font-family:宋体"}

[[当用户需要将]{style="font-family:宋体"}[Option]{lang="EN-US"}]{#struct_0_18608_20265_1884234177}[字段中的信息按字符串形式解析时，请确保]{style="font-family:宋体"}[Option]{lang="EN-US"}[字段内容中不出现字符串结束符和不可见字符，否则可能生成错误的用户名。]{style="font-family:宋体"}

[[建议不要使用]{style="font-family:宋体"}]{#struct_0_18608_20265_1368916016}[@]{lang="SV"}[作为分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[避免携带]{style="font-family:宋体"}[@]{lang="SV"}[字符的用户名在]{style="font-family:
宋体"}[AAA]{lang="SV"}[服务器端不能被正确解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x883668447}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x341598120}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上]{style="font-family:宋体"}[IPv4 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[Client Identifier Option]{lang="EN-US"}[字段]{style="font-family:宋体"}[中的信息作为用户名]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x769833727}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber dhcp username ]{lang="SV"}[include]{lang="EN-US"}[ client-id]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1315340186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x604568256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x451111395}
:::

::: {#1445905218 .myid}
[]{#_Toc404785838}[]{#struct_0_18608_20265_300449124}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber dscp**

------------------------------------------------------------------------

[**[ip subscriber dscp]{lang="EN-US"}**]{#struct_0_18608_20265_x1976594293}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber** **dscp**]{lang="EN-US"}]{#struct_0_18608_20265_x2145667197}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1495197507}

[**[ip subscriber dscp ]{lang="EN-US"}***[dscp-value-list]{lang="EN-US"}*[ **domain** *domain-name*]{lang="EN-US"}]{#struct_0_18608_20265_1187892521}

[**[undo ip subscriber dscp]{lang="EN-US"}***[ dscp-value-list]{lang="EN-US"}*]{#struct_0_18608_20265_x903508682}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1530435107}

[[未指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_1557581199}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769768191}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1735883925}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_35752111}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_41005163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x2130182973}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_819097982}

[*[dscp-value-list]{lang="EN-US"}*]{#struct_0_18608_20265_x1521133076}[：]{style="font-family:宋体;
color:black"}[DSCP]{lang="SV"}[值]{style="font-family:宋体"}[列表，表示一个或多个]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的值，表示方式为]{style="font-family:宋体"}*[dscp-value-list]{lang="EN-US"}*[ = *dscp-value* \[ **to** *dscp-value* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[dscp-value]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_x2129455292}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[DSCP]{lang="SV"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x298397832}

[[本]{style="font-family:宋体"}]{#struct_0_18608_20265_220240482}[命令]{style="font-family:宋体"}[用来配置指定]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[范围内的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发的用户认证时使用的认证域，通过指定的认证域进行认证、授权、计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_372697691}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x1034206945}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置]{style="font-family:宋体"}[DSCP]{lang="SV"}[值范围为]{style="font-family:宋体"}[1]{lang="SV"}[到]{style="font-family:
宋体"}[4]{lang="SV"}[的]{style="font-family:宋体"}[IPv4]{lang="SV"}[未知源]{style="font-family:宋体"}[IP]{lang="SV"}[接入]{style="font-family:宋体"}[用户认证使用的]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域为]{style="font-family:宋体"}[dscpdm]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x1054976109}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber service-identify dscp]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber dscp 1 to 4 domain ]{lang="EN-US"}[dscpdm]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1458190443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x769964799}
:::

::: {#1043081544 .myid}
[]{#_Toc404785839}[]{#struct_0_18608_20265_x260115429}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber enable**

------------------------------------------------------------------------

[**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1542821946}[命令用来在接口上使能]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[功能并指定用户的接入模式。]{style="font-family:宋体"}

[**[undo ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1935052901}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x150335754}

[**[ip subscriber ]{lang="EN-US"}**[{ **l2-connected** \| **routed** } **enable**]{lang="EN-US"}]{#struct_0_18608_20265_414427942}

[**[undo ip subscriber ]{lang="EN-US"}**[{ **l2-connected** \| **routed** } **enable**]{lang="EN-US"}]{#struct_0_18608_20265_x1239136118}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1037387656}

[[接口上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1302640490}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1386208337}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1168710048}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2084249622}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1914329157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1223860548}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1496501540}

[**[l2-connected]{lang="EN-US"}**]{#struct_0_18608_20265_x769899263}[：指定二层接入模式]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[rout]{lang="SV"}[ed]{lang="EN-US"}**]{#struct_0_18608_20265_x1374228088}[：指定三层接入模式]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_839161245}

[[只有在接口上使能了]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1811450051}[功能后，其它的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[相关配置才能生效。]{style="font-family:宋体"}

[[不允许直接修改]{style="font-family:宋体"}[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_2035745948}[的接入模式，必须关闭]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[功能之后，重新使能]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[功能时指定新的接入模式。]{style="font-family:宋体"}

[[在聚合接口视图下使能]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1022519574}[功能时，必须同时通过]{style="font-family:宋体"}**[service]{lang="EN-US"}**[命令指定聚合接口下流量的业务处理板；否则会产生无法统计用户流量的现象。有关]{style="font-family:宋体"}**[service]{lang="EN-US"}**[命令的详细介绍请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考"中的"以太网链路聚合"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1455079800}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1623217486}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能二层接入模式的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_2124136318}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber l2-connected enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x79311577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service]{lang="EN-US"}**]{#struct_0_18608_20265_1361609583}[（二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[以太网链路聚合）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1831057216 .myid}
[]{#_Toc404785840}[]{#struct_0_18608_20265_288964039}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber initiator dhcp enable**

------------------------------------------------------------------------

[**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1567134932}[命令用来在接口上使能]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[**[undo ip subscriber initiator dhcp enable ]{lang="EN-US"}**]{#struct_0_18608_20265_1315123558}[命令用来关闭接口上]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_551069498}

[**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x919419062}

[**[undo ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x770095871}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1646747498}

[[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_x721683340}[报文不能触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1270898542}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_967085867}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2012238139}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1650076120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_396888488}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x124904378}

[[接口上使能该功能后，收到的首个]{style="font-family:宋体"}[DHCP Discover]{lang="EN-US"}]{#struct_0_18608_20265_x871813300}[报文或直接申请地址的]{style="font-family:宋体"}[DHCP Request]{lang="EN-US"}[报文会触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话；关闭该功能后，该接口上收到的]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文不能触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话，已有的由]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文触发生成的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话不会被删除。]{style="font-family:宋体"}

[[接口上可同时配置]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_1969911710}[报文和未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1088603969}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_253756047}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_813435071}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber initiator dhcp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x770030335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1219363229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x712005767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_1941254023}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1924493738}
:::

::: {#7558316 .myid}
[]{#_Toc404785841}[]{#struct_0_18608_20265_x1964994258}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber initiator unclassified-ip enable**

------------------------------------------------------------------------

[**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x243019592}[命令用来在接口上使能未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[**[undo ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_1307912660}[命令用来关闭接口上的未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1626785393}

[**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x390517429}

[**[undo ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_623549087}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_105379609}

[[未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_2033936647}[报文不能触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_741350935}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_723000126}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769178367}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_2119990246}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1201735849}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x213009614}

[[接口使能该功能后，收到的未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_x322502155}[报文会触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话；关闭该功能后，该接口上收到的未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文不能触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话，已有的由未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话不会被删除。]{style="font-family:宋体"}

[[接口上可同时配置]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_x1705710988}[报文和未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_144330023}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x729267204}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1646425062}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber initiator unclassified-ip enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1865759709}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x673632322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1020662796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_117502464}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_200148855}
:::

::: {#53725897 .myid}
[]{#_Toc404785842}[]{#struct_0_18608_20265_x769112831}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber interface-leased**

------------------------------------------------------------------------

[**[ip subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_x1454241289}[命令用来配置]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber interface-leased**]{lang="EN-US"}]{#struct_0_18608_20265_982854179}[命令用来删除已配置的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_689161721}

[**[ip subscriber interface-leased]{lang="EN-US"}**[ **username** *name* **password** { **ciphertext** \| **plaintext** } *password* \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_x881217890}

[**[undo]{lang="EN-US"}**[ **ip subscriber interface-leased**]{lang="EN-US"}]{#struct_0_18608_20265_1361945104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1763285420}

[[未配置]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_562862866}[接口专线用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x644167557}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1354090942}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1164518677}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1046565300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x854151480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769702656}

[**[username]{lang="SV"}**]{#struct_0_18608_20265_935332511}*[ name]{lang="SV"}*[：指定用户认证时使用的用户名，其中]{style="font-family:宋体;color:black"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写]{style="font-family:
宋体"}[。]{style="font-family:宋体;color:black"}

[**[password]{lang="SV"}**]{#struct_0_18608_20265_2082470966}[：指定用户认证时使用的密码。]{style="font-family:宋体;color:black"}

[**[ciphertext]{lang="SV"}**]{#struct_0_18608_20265_x1224512653}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以密文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[plaintext]{lang="SV"}**]{#struct_0_18608_20265_1161312731}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以明文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_1912159528}[：]{style="font-family:宋体;color:black"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_508245313}*[ domain-name]{lang="SV"}*[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果未指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将使用缺省]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的]{style="font-family:宋体"} ["]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1876685400}

[[一个]{style="font-family:宋体"}]{#struct_0_18608_20265_1589023382}[IPv4 ]{lang="SV"}[IPoE]{lang="EN-US"}[接口专线用户代表了该接口接入的所有]{style="font-family:宋体"}[IPv4]{lang="SV"}[用户，接口上接入的所有]{style="font-family:宋体"}[IPv4]{lang="SV"}[用户统一认证、授权和计费。该]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[专线用户认证成功后，接口上接入的所有]{style="font-family:宋体"}[IPv4]{lang="SV"}[用户流量均允许通过，且共享一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话，并基于接口进行授权和计费。]{style="font-family:宋体"}

[[每个]{style="font-family:宋体"}]{#struct_0_18608_20265_x981794098}[接口只能配置一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户。]{style="font-family:宋体"}

[[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_1127880578}[IPoE]{lang="SV"}[个人接入用户]{style="font-family:宋体"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接口专线用户和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1724658397}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1368971390}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[接口专线用户]{style="font-family:宋体"}[：]{style="font-family:宋体"}[认证使用的用户名为]{style="font-family:宋体"}[intuser]{lang="SV"}[，]{style="font-family:宋体"}[认证使用的密码为明文]{style="font-family:宋体"}[pw123]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x769637120}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber interface-leased username intuser password plaintext pw123]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x272019008}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_1243867176}
:::

::: {#1562384427 .myid}
[]{#_Toc404785843}[]{#struct_0_18608_20265_991034316}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber nas-port-id format**

------------------------------------------------------------------------

[**[ip subscriber nas-port-id]{lang="EN-US"}**[ **format**]{lang="EN-US"}]{#struct_0_18608_20265_x514341507}[命令用于为]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接入用户配置]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性的封装格式，即]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接入用户进行认证时，接入设备向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性的封装格式。]{style="font-family:宋体"}

[**[undo ip subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_1182096832}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1676697769}

[**[ip subscriber nas-port-id format cn-telecom ]{lang="EN-US"}**[{ **version1.0** \| **version2.0** }]{lang="EN-US"}]{#struct_0_18608_20265_219184069}

[**[undo ip subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_x802141395}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1365796211}

[[按]{style="font-family:宋体"}[version 1.0]{lang="EN-US"}]{#struct_0_18608_20265_x871231730}[的格式填充]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_38112575}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_780626367}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769833728}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1315536794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1685777857}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_978375900}

[**[version1.0]{lang="EN-US"}**]{#struct_0_18608_20265_486302971}[：封装格式为]{style="font-family:宋体"}[version 1.0]{lang="EN-US"}[，表示发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性以电信]{style="font-family:宋体"}[163]{lang="EN-US"}[大后台要求的格式填充。]{style="font-family:宋体"}

[**[version2.0]{lang="EN-US"}**]{#struct_0_18608_20265_569970317}[：封装格式为]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[，表示发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性以]{style="font-family:宋体"}[YDT 2275-2011]{lang="EN-US"}[宽带接入用户线路（端口）标识要求的格式填充。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1163531649}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[version 1.0]{lang="EN-US"}]{#struct_0_18608_20265_788743088}[封装格式：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网接口和三层聚合接口]{style="font-family:宋体"}]{#struct_0_18608_20265_1326931200}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=0;]{lang="EN-US"}]{#struct_0_18608_20265_x1571379372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网子接口和三层聚合子接口（携带单层]{style="font-family:宋体"}]{#struct_0_18608_20265_1584861386}[VLAN Tag]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=*vlan_id*;]{lang="EN-US"}]{#struct_0_18608_20265_x1842812148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网子接口和三层聚合子接口（携带双层]{style="font-family:宋体"}]{#struct_0_18608_20265_x769768192}[VLAN Tag]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[ slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=*inner-vlan*;vlanid2=*outer-vlan*;]{lang="EN-US"}]{#struct_0_18608_20265_1735687317}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基于]{style="font-family:宋体"}]{#struct_0_18608_20265_x378030328}[ATM]{lang="EN-US"}[链路的三层虚拟以太网接口（]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vpi=*vpi*;vci=*vci*;]{lang="EN-US"}]{#struct_0_18608_20265_x1388379747}

[[其中，]{style="font-family:宋体"}*[slot_num]{lang="EN-US"}*]{#struct_0_18608_20265_445409123}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的槽位号；]{style="font-family:宋体"}*[subslot_num]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的子槽位号；]{style="font-family:宋体"}*[port_num]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的端口号；]{style="font-family:宋体"}*[vlan_id]{lang="EN-US"}*[表示接入用户的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[inner-vlan]{lang="EN-US"}*[表示接入用户的内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[outer-vlan]{lang="EN-US"}*[表示接入用户的外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的]{style="font-family:宋体"}[VPI]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的]{style="font-family:宋体"}[VCI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[version 2.0]{lang="EN-US"}]{#struct_0_18608_20265_1609407346}[封装格式：]{lang="EN-US" style="font-family:宋体"}

[[{eth\|trunk\|atm} NAS_slot/NAS_subslot/NAS_port:svlan.cvlan AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port]{lang="EN-US"}]{#struct_0_18608_20265_x1147961038}

[[其中，]{style="font-family:宋体"}[{eth\|trunk\|atm}]{lang="EN-US"}]{#struct_0_18608_20265_x602336657}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的类型，包括以太接口、]{style="font-family:宋体"}[trunk]{lang="EN-US"}[类型的以太网接口或]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口；]{style="font-family:宋体"}[NAS_slot]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的槽位号；]{style="font-family:宋体"}[NAS_subslot]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的子槽位号；]{style="font-family:宋体"}[NAS_port]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的端口号；]{style="font-family:宋体"}[svlan]{lang="EN-US"}[表示接入用户的]{style="font-family:宋体"}[SVLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}[cvlan]{lang="EN-US"}[表示接入用户的]{style="font-family:宋体"}[CVLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}[AccessNodeIdentifier]{lang="EN-US"}[表示接入节点的标识；]{style="font-family:宋体"}[ANI_rack]{lang="EN-US"}[表示接入节点机架号；]{style="font-family:宋体"}[ANI_frame]{lang="EN-US"}[表示接入节点机框号；]{style="font-family:宋体"}[ANI_slot]{lang="EN-US"}[表示接入节点槽位号；]{style="font-family:宋体"}[ANI_subslot]{lang="EN-US"}[表示接入节点子槽位号；]{style="font-family:宋体"}[ANI_port]{lang="EN-US"}[表示接入节点端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_77322833}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1477605681}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备使用]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式封装]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x336948578}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber nas-port-id format cn-telecom version2.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_99715019}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1999982188}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_x1630827716}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ip subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x769964800}
:::

::: {#374222208 .myid}
[]{#_Toc404785844}[]{#struct_0_18608_20265_x304286700}[]{#_Toc369161204}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber nas-port-id nasinfo-insert**

------------------------------------------------------------------------

[**[ip subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x790898186}[命令用于配置在提取出的]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文的]{style="font-family:宋体"}[Option 82 Circuit-ID]{lang="EN-US"}[子选项内容中插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息，并使用插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息后的内容作为]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo ip subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_373260760}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_123776777}

[**[ip subscriber nas-port-id]{lang="EN-US"}**[ **nasinfo-insert** ]{lang="EN-US"}]{#struct_0_18608_20265_x1169049872}

[**[undo ip subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x1915596052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1991860134}

[[如果收到的]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_2070508630}[报文带有]{style="font-family:宋体"}[Option 82 Circuit-ID]{lang="EN-US"}[子选项，则直接使用该子选项内容作为]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性字符串。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1591704626}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x961237689}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1224036567}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1507805872}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1459590673}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_2032905819}

[[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1545486263}[中继组网环境下，接入设备能捕获用户的]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文，并从报文中提取出]{style="font-family:宋体"}[DHCP Option82 Circuit-ID]{lang="EN-US"}[子选项信息。在配置了]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性的封装格式为]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式，且信任]{style="font-family:宋体"}[DHCP Option 82]{lang="EN-US"}[的情况下，若配置了本命令，则接入设备处理如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果收到的]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1120122410}[报文带有]{lang="EN-US" style="font-family:宋体"}[Option82 Circuit-ID]{lang="EN-US"}[子选项，则从收到的]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文中解析]{lang="EN-US" style="font-family:宋体"}[Option82 Circuit-ID]{lang="EN-US"}[子选项，并按]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式要求在原有]{lang="EN-US" style="font-family:宋体"}[Circuit-ID]{lang="EN-US"}[子选项的内容里插入]{lang="EN-US" style="font-family:宋体"}[NAS]{lang="EN-US"}[信息（该信息标识了用户在本设备上的接入位置信息），然后将其作为]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性内容。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果收到的]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x769899264}[报文不带]{lang="EN-US" style="font-family:宋体"}[Option82 Circuit-ID]{lang="EN-US"}[子选项，则按]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式要求封装，填充]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性中的]{lang="EN-US" style="font-family:宋体"}[NAS]{lang="EN-US"}[信息字段（]{lang="EN-US" style="font-family:宋体"}[NAS_slot/NAS_subslot/NAS_port:svlan.cvlan]{lang="EN-US"}[），并将]{lang="EN-US" style="font-family:宋体"}[AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port]{lang="EN-US"}[部分修改为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[本功能对原]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1373769336}[报文中]{style="font-family:宋体"}[Option82]{lang="EN-US"}[子选项不产生任何影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1609146743}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1925477072}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备使用]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[客户端上报的]{style="font-family:宋体"}[Option82]{lang="EN-US"}[信息，并在其中插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息，然后将其封装为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1417273924}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber nas-port-id nasinfo-insert]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x631510888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x698883461}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_x394082091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_x1979237374}
:::

::: {#-2095155920 .myid}
[]{#_Toc404785845}[]{#struct_0_18608_20265_2126088632}[]{#_Toc364707446}[]{#_Toc364707447}[]{#_Toc364707448}[]{#_Toc364707449}[]{#_Toc364707450}[]{#_Toc364707451}[]{#_Toc364707452}[]{#_Toc364707453}[]{#_Toc364707454}[]{#_Toc364707455}[]{#_Toc364707456}[]{#_Toc364707457}[]{#_Toc364707458}[]{#_Toc364707459}[]{#_Toc364707460}[]{#_Toc364707461}[]{#_Toc364707462}[]{#_Toc364707463}[]{#_Toc364707464}[]{#_Toc364707465}[]{#_Toc349553570}[]{#_Toc349553571}[]{#_Toc349553572}[]{#_Toc349553573}[]{#_Toc349553574}[]{#_Toc349553575}[]{#_Toc349553576}[]{#_Toc349553577}[]{#_Toc349553578}[]{#_Toc349553579}[]{#_Toc349553580}[]{#_Toc349553581}[]{#_Toc349553582}[]{#_Toc349553583}[]{#_Toc349553584}[]{#_Toc349553585}[]{#_Toc349553586}[]{#_Toc349553587}[]{#_Toc349553588}[]{#_Toc349553589}[]{#_Toc349553590}[]{#_Toc349553591}[]{#_Toc349553592}[]{#_Toc349553593}[]{#_Toc349553594}[]{#_Toc349553595}[]{#_Toc349553596}[]{#_Toc349553597}[]{#_Toc349553598}[]{#_Toc349553599}[]{#_Toc349553600}[]{#_Toc349553601}[]{#_Toc349553602}[]{#_Toc349553603}[]{#_Toc349553604}[]{#_Toc349553605}[]{#_Toc349553606}[]{#_Toc349553607}[]{#_Toc349553608}[]{#_Toc349553609}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber nas-port-type**

------------------------------------------------------------------------

[**[ip subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_1251593274}[命]{style="font-size:
10.0pt;font-family:宋体;color:black"}[令用来配置接口的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接入端口类型]{style="font-family:宋体"}[。]{style="font-size:10.0pt;font-family:宋体;color:black"}

[**[undo ip subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_1601685144}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1792644438}

[**[ip subscriber nas-port-type ]{lang="EN-US"}**[{ **802.11** \| **adsl-cap** \| **adsl-dmt** \| **async** \| **cable** \| **ethernet** \| **g.3-fax** \| **hdlc** \| **idsl** \| **isdn-async-v110** \| **isdn-async-v120** \| **isdn-sync** \| **piafs** \| **sdsl** \| **sync** \| **virtual** \| **wireless-other** \| **x.25** \| **x.75** \| **xdsl** }]{lang="EN-US"}]{#struct_0_18608_20265_1222201742}

[**[undo ip subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_x770095872}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1646681962}

[[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1515210712}[接入端口类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1787835271}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1181322645}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1041993307}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x735719916}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x794160399}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_851912088}

[**[802.11]{lang="SV"}**]{#struct_0_18608_20265_x315744556}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[符合]{style="font-family:宋体"}[Wireless-IEEE 802.11]{lang="EN-US"}[标准的接口类型，对应的编码值为]{style="font-family:宋体"}[19]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[adsl-cap]{lang="SV"}**]{#struct_0_18608_20265_x1809275607}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ADSL-CAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Carrierless Amplitude Phase Modulation]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[adsl-dmt]{lang="SV"}**]{#struct_0_18608_20265_x86201432}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ADSL-DMT]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Discrete Multi-Tone]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[13]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[async]{lang="SV"}**]{#struct_0_18608_20265_127726286}[：]{style="font-family:宋体;color:black"}[Async]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cable]{lang="SV"}**]{#struct_0_18608_20265_x254140799}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Cable]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[17]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ethernet]{lang="SV"}**]{#struct_0_18608_20265_x995495425}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Ethernet]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g.3-fax]{lang="SV"}**]{#struct_0_18608_20265_x770030336}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[G.3 Fax]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hdlc]{lang="SV"}**]{#struct_0_18608_20265_1219559837}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[HDLC]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[idsl]{lang="SV"}**]{#struct_0_18608_20265_1946891454}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[IDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[ISDN Digital Subscriber Line]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v110]{lang="SV"}**]{#struct_0_18608_20265_x802900116}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ISDN Async V.110]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v120]{lang="SV"}**]{#struct_0_18608_20265_x1738411576}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ISDN Async V.120]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-sync]{lang="SV"}**]{#struct_0_18608_20265_x2147296310}[：]{style="font-family:宋体"}[ISDN Sync]{lang="EN-US"}[口类型，对应的编码值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[piafs]{lang="SV"}**]{#struct_0_18608_20265_1858930161}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[符合]{style="font-family:宋体"}[PIAFS]{lang="EN-US"}[（]{style="font-family:宋体"}[PHS]{lang="EN-US"}[（]{style="font-family:宋体"}[Personal Handyphone System]{lang="EN-US"}[）]{style="font-family:宋体"}[Internet Access Forum Standard]{lang="EN-US"}[）标准的接口类型，对应的编码值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdsl]{lang="SV"}**]{#struct_0_18608_20265_136520684}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[SDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Symmetric DSL]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sync]{lang="SV"}**]{#struct_0_18608_20265_1530531764}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Sync]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[virtual]{lang="SV"}**]{#struct_0_18608_20265_x1558601766}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Virtual]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[wireless-other]{lang="SV"}**]{#struct_0_18608_20265_x1430773012}[：]{style="font-family:宋体"}[Wireless-other]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[18]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.25]{lang="SV"}**]{#struct_0_18608_20265_x670915798}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[X.25]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.75]{lang="SV"}**]{#struct_0_18608_20265_270164155}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[X.75]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[xdsl]{lang="SV"}**]{#struct_0_18608_20265_x785675192}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[XDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Digital Subscriber Line of unknown type]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769178368}

[[此处配置的端口接入类型]{style="font-family:宋体"}]{#struct_0_18608_20265_2119662566}[值将作为向]{style="font-family:宋体"}[RADIUS]{lang="FR"}[服务器发送的]{style="font-family:宋体"}[RADIUS]{lang="FR"}[请求报文的]{style="font-family:宋体"}[NAS-Port-Type]{lang="FR"}[属性值]{style="font-family:宋体"}[，用于]{style="font-family:宋体"}[向]{style="font-family:宋体"}[RADIUS]{lang="FR"}[服务器正确传递用户的接入端口信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1535897678}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x762235758}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接入端口类型为]{style="font-family:宋体"}[SDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}]{#struct_0_18608_20265_943024037}[Sysname]{lang="SV"}[\> system-view]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="SV"}[\] ]{lang="EN-US"}[interface ]{lang="SV"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber nas-port-type sdsl]{lang="EN-US"}
:::

::: {#-1045913091 .myid}
[]{#_Toc404785846}[]{#struct_0_18608_20265_x2142424346}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber password**

------------------------------------------------------------------------

[**[ip subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x1164202659}[命令用来配置]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人接入用户的认证密码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber password**]{lang="EN-US"}]{#struct_0_18608_20265_533089292}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_2073160679}

[**[ip subscriber password ]{lang="EN-US"}**[{ **ciphertext** \| **plaintext** } *password*]{lang="EN-US"}]{#struct_0_18608_20265_1333143582}

[**[undo]{lang="EN-US"}**[ **ip subscriber password**]{lang="EN-US"}]{#struct_0_18608_20265_x1955821169}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1291292438}

[[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1755632435}[个人接入用户的认证密码为字符串]{style="font-family:宋体"}[vlan]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x610264902}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x816929690}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769112832}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1454306825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1444378537}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1692931884}

[**[ciphertext]{lang="EN-US"}**]{#struct_0_18608_20265_1049835088}[：表示]{style="font-family:宋体;color:black"}[以密文方式配置用户的认证密码。]{style="font-family:宋体"}

[**[plaintext]{lang="EN-US"}**]{#struct_0_18608_20265_1471735045}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;color:black"}[以明文方式配置用户的认证密码。]{style="font-family:宋体"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_234107}[：]{style="font-family:宋体;color:black"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x838695392}

[[如果接口上同时配置了]{style="font-family:宋体;color:black"}**[ip subscriber dhcp password option60]{lang="EN-US" style="color:black"}**]{#struct_0_18608_20265_x1241979919}[命令和]{style="font-family:宋体;color:black"}**[ip subscriber password]{lang="EN-US" style="color:black"}**[命令，则优先使用]{style="font-family:
宋体;color:black"}**[ip subscriber dhcp password option60]{lang="EN-US" style="color:black"}**[命令获取的字符串作为认证密码。]{style="font-family:宋体;
color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1685644435}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x56843393}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[个人接入用户认证时使用的密码为明文]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1317503209}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber password plaintext 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1299482060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x119640335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber unclassified-ip username]{lang="EN-US"}**]{#struct_0_18608_20265_x769702649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber dhcp password option60]{lang="EN-US"}**]{#struct_0_18608_20265_2080498935}
:::

::: {#-1277760185 .myid}
[]{#_Toc404785847}[]{#struct_0_18608_20265_936053408}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber service-identify**

------------------------------------------------------------------------

[**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_571032501}[命令用来配置]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的业务识别方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber service-identify**]{lang="EN-US"}]{#struct_0_18608_20265_x290237933}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1879270885}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_757747173}[三层聚合口视图]{style="font-family:宋体"}

[**[ip subscriber service-identify]{lang="EN-US"}**[ **dscp**]{lang="EN-US"}]{#struct_0_18608_20265_x908286464}

[**[undo]{lang="EN-US"}**[ **ip subscriber service-identify**]{lang="EN-US"}]{#struct_0_18608_20265_1557322224}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x254592005}[三层聚合子接口视图]{style="font-family:宋体"}

[**[ip subscriber service-identify]{lang="EN-US"}**[ { **8021p** { **second-vlan** \| **vlan** } \| **dscp** \| **second-vlan** \| **vlan** }]{lang="EN-US"}]{#struct_0_18608_20265_x595130060}

[**[undo]{lang="EN-US"}**[ **ip subscriber service-identify**]{lang="EN-US"}]{#struct_0_18608_20265_x159963745}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x152201959}

[[未指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_x1668186809}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的业务识别方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_17701239}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1267164698}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769637113}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x271953469}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1788053639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_292026640}

[**[8021p second-vlan]{lang="SV"}**]{#struct_0_18608_20265_1824210407}[：表示]{style="font-family:宋体;color:black"}[QinQ]{lang="SV" style="font-size:
10.0pt;color:black"}[模式下基]{style="font-size:10.0pt;font-family:宋体;
color:black"}[于内层]{style="font-family:宋体"}[VLAN ]{lang="SV" style="font-size:10.0pt;color:black"}[Tag]{lang="EN-US"}[中的]{style="font-size:10.0pt;font-family:宋体;color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;color:black"}[值]{style="font-size:10.0pt;
font-family:宋体;color:black"}[识别业务]{style="font-size:10.0pt;font-family:
宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[8021p vlan]{lang="SV"}**]{#struct_0_18608_20265_974205986}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-size:10.0pt;
font-family:宋体;color:black"}[VLAN ]{lang="SV" style="font-size:10.0pt;
color:black"}[Tag]{lang="SV"}[中的]{style="font-size:10.0pt;
font-family:宋体;color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;
color:black"}[值]{style="font-size:10.0pt;font-family:宋体;
color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[，]{style="font-size:10.0pt;font-family:宋体;color:black"}[QinQ]{lang="SV" style="font-size:10.0pt;color:black"}[模式下基]{style="font-size:10.0pt;
font-family:宋体;color:black"}[于外层]{style="font-family:宋体"}[V]{lang="SV"}[LAN ]{lang="SV" style="font-size:10.0pt;color:black"}[Tag]{lang="SV"}[中的]{style="font-size:10.0pt;font-family:宋体;color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;color:black"}[值]{style="font-size:10.0pt;font-family:宋体;color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[dscp]{lang="SV"}**]{#struct_0_18608_20265_61504214}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-family:宋体;
color:black"}[DSCP]{lang="SV" style="color:black"}[值识别业务。]{style="font-family:宋体;color:black"}

[**[second-vlan]{lang="SV"}**]{#struct_0_18608_20265_586588112}[：]{style="font-family:宋体;color:black"}[QinQ]{lang="SV" style="font-size:10.0pt;
color:black"}[模式下]{style="font-size:10.0pt;font-family:宋体;
color:black"}[基于内层]{style="font-family:宋体"}[VLAN ID]{lang="SV" style="font-size:10.0pt;color:black"}[识别业务]{style="font-size:10.0pt;
font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_833271293}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-size:10.0pt;
font-family:宋体;color:black"}[VLAN ID]{lang="SV" style="font-size:10.0pt;
color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;
color:black"}[，]{style="font-size:10.0pt;font-family:宋体;
color:black"}[QinQ]{lang="SV" style="font-size:10.0pt;color:black"}[模式下基于外层]{style="font-family:宋体"}[VLAN ID]{lang="SV" style="font-size:10.0pt;
color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;
color:black"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1936713772}

[[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18608_20265_1558700180}[用户认证时使用的认证域由报文中携带的业务信息来决定。不同的业务特征可以对应不同的认证域，每一个接口可以指定仅识别某种类型业务的报文。例如，接口上若指定了基于]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值识别业务，且通过]{style="font-family:宋体"}**[ip subscriber dscp 1 domain aabcc]{lang="EN-US"}**[命令指定了]{style="font-family:
宋体"}[DSCP]{lang="EN-US"}[值]{style="font-family:宋体"}[1]{lang="EN-US"}[与认证域]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[的映射关系，则]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}[1]{lang="EN-US"}[的用户认证时将会使用认证域]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一个接口上只能指定一个业务识别方式。]{style="font-family:宋体"}]{#struct_0_18608_20265_x856283977}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1572367345}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1453801049}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户认证使用[基于]{style="color:black"}]{style="font-family:宋体"}[DSCP]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;
color:black"}[业务识别方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x769833721}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber service-identify dscp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1314946970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber 8021p]{lang="EN-US"}**]{#struct_0_18608_20265_x1372656329}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber dscp]{lang="EN-US"}**]{#struct_0_18608_20265_1395016230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber vlan]{lang="EN-US"}**]{#struct_0_18608_20265_1523597796}
:::

::: {#2099634993 .myid}
[]{#_Toc404785848}[]{#struct_0_18608_20265_x683163992}[]{#_Toc364682904}[]{#_Toc364707468}[]{#_Toc364682905}[]{#_Toc364707469}[]{#_Toc364682906}[]{#_Toc364707470}[]{#_Toc364682907}[]{#_Toc364707471}[]{#_Toc364682908}[]{#_Toc364707472}[]{#_Toc364682909}[]{#_Toc364707473}[]{#_Toc364682910}[]{#_Toc364707474}[]{#_Toc364682911}[]{#_Toc364707475}[]{#_Toc364682912}[]{#_Toc364707476}[]{#_Toc364682913}[]{#_Toc364707477}[]{#_Toc364682914}[]{#_Toc364707478}[]{#_Toc364682915}[]{#_Toc364707479}[]{#_Toc364682916}[]{#_Toc364707480}[]{#_Toc364682917}[]{#_Toc364707481}[]{#_Toc364682918}[]{#_Toc364707482}[]{#_Toc364682919}[]{#_Toc364707483}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber session static**

------------------------------------------------------------------------

[**[ip subscriber session static]{lang="EN-US"}**]{#struct_0_18608_20265_343265218}[命令用来配置静态]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[会话。]{style="font-family:
宋体"}

[**[undo ip subscriber session static]{lang="EN-US"}**]{#struct_0_18608_20265_x327354871}[命令用来删除指定的静态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x386978158}

[**[ip subscriber session static ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \[ **second-vlan** *vlan-id* \] \] \[ **mac** *mac-address* \] \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_144482420}

[**[undo ip subscriber session static ip ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[\[ **vlan** *vlan-id* \[ **second-vlan** *vlan-id* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_719548514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1660132368}

[[未配置静态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1300249832}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_666582428}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x2086925902}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1809799760}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x769768185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1735621782}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1527750725}

[**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_1076114300}*[ ip-address]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[用户的]{style="font-family:宋体"}[IPv4]{lang="SV"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_1464469332}*[ vlan-id]{lang="SV"}*[：表示用户报文的外层]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[。其中]{style="font-family:宋体;color:black"}*[vlan-id]{lang="SV"}*[表示]{style="font-family:宋体"}[VLAN ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:
宋体"}

[**[second-vlan]{lang="SV"}**]{#struct_0_18608_20265_x1103879412}*[ vlan-id]{lang="SV"}*[：表示用户报文的内层]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[。其中]{style="font-family:宋体;color:black"}*[vlan-id]{lang="SV"}*[表示]{style="font-family:宋体"}[VLAN ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:
宋体"}

[**[mac]{lang="SV"}**]{#struct_0_18608_20265_x2129007530}*[ mac-address]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;color:black"}[用户的]{style="font-family:宋体"}[MAC]{lang="SV" style="color:black"}[地址，]{style="font-family:宋体;color:black"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体;color:black"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_147892112}[ *domain-name*]{lang="SV"}[：]{style="font-family:宋体"}[指定认证使用的]{style="font-family:宋体"}[ISP]{lang="SV"}[域名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:
宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:宋体"}[@]{lang="SV"}["]{style="font-family:
宋体"}[字符]{style="font-family:宋体"}[。]{style="font-family:
宋体"}[如果未指定该参数]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[将使用缺省]{style="font-family:宋体"}[认证]{style="font-family:
宋体"}[域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的"]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_629784387}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18608_20265_x1843642684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令的]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**]{#struct_0_18608_20265_x918651944}[和]{lang="EN-US" style="font-family:宋体"}**[second-vlan]{lang="EN-US"}**[参数仅子接口支持，非子接口不支持。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{style="font-family:宋体"}]{#struct_0_18608_20265_x715039160}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[的匹配优先级高于动态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。若已经存在静态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，则与之匹配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文不会触发新的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话；若存在一个未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发建立的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，则再配置一个能与该未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文匹配的静态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，会覆盖已经存在的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[系统支持配置多个静态]{style="font-family:宋体"}]{#struct_0_18608_20265_1013055987}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相同]{style="font-family:宋体"}]{#struct_0_18608_20265_1823761134}[IP]{lang="SV"}[、外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[、内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[的静态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[只能存在一条]{style="font-family:宋体"}[，]{style="font-family:宋体"}[后配置的不能覆盖已配置的。若要修改相关参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[必须删除当前配置后重新配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_x769964793}[静态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话、接口专线用户和子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x259722213}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1460210039}[在接]{style="font-family:宋体"}[口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一条静态]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话：]{style="font-family:宋体"}[用户]{style="font-family:宋体"}[IP]{lang="SV"}[地址为]{style="font-family:
宋体"}[1.1.1.1]{lang="SV"}[，]{style="font-family:宋体"}[认证使用的认证域为]{style="font-family:宋体"}[dm1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1680387061}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber session static ip 1.1.1.1 domain dm1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x196143778}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x802830388}
:::

::: {#481775551 .myid}
[]{#_Toc404785849}[]{#struct_0_18608_20265_x1353649682}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber subnet-leased**

------------------------------------------------------------------------

[**[ip subscriber subnet-leased]{lang="EN-US"}**]{#struct_0_18608_20265_930870126}[命令用来配置]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber subnet-leased**]{lang="EN-US"}]{#struct_0_18608_20265_x1448102350}[命令用来删除指定的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1079329660}

[**[ip subscriber subnet-leased ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *mask* \| *mask-length* } **username** *name* **password** { **ciphertext** \| **plaintext** } *password* \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_x1761016937}

[**[undo]{lang="EN-US"}**[ **ip subscriber subnet-leased ip** *ip-address* { *mask* \| *mask-length* }]{lang="EN-US"}]{#struct_0_18608_20265_447738251}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x747566822}

[[未配置]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x2139204210}[子网专线用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769899257}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1373965945}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1581067478}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x878364407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x936717174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_14451940}

[**[ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_18608_20265_1767268782}[：表示]{style="font-family:宋体;color:black"}[用户的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[*[mask]{lang="SV"}*]{#struct_0_18608_20265_x9392339}[：]{style="font-family:宋体;color:black"}[IP]{lang="SV"}[地址的网络]{style="font-family:宋体"}[掩码，为点分十进制形式。]{style="font-family:宋体;color:black"}

[*[mask-length]{lang="SV"}*]{#struct_0_18608_20265_x107317137}[：]{style="font-family:宋体;color:black"}[IP]{lang="SV" style="color:black"}[地址的网络掩码长度，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体"}[31]{lang="SV" style="color:black"}[。]{style="font-family:宋体;color:black"}

[**[username]{lang="SV"}**]{#struct_0_18608_20265_x1915859243}*[ name]{lang="SV"}*[：指定用户认证时使用的用户名，其中]{style="font-family:宋体;color:black"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写]{style="font-family:
宋体"}[。]{style="font-family:宋体;color:black"}

[**[password]{lang="SV"}**]{#struct_0_18608_20265_1685846049}[：指定用户认证时使用的密码。]{style="font-family:宋体;color:black"}

[**[ciphertext]{lang="SV"}**]{#struct_0_18608_20265_x223977565}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以密文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[plaintext]{lang="SV"}**]{#struct_0_18608_20265_67341596}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以明文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_x1400687435}[：]{style="font-family:宋体;color:black"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1572934368}*[ domain-name]{lang="SV"}*[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符]{style="font-family:宋体"}[。]{style="font-family:宋体"}[如果未指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将使用缺省]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的]{style="font-family:宋体"} ["]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x770095865}

[[一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1647009641}[子网专线用户代表了该接口接入的所有该子网内]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户，该子网内的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户统一认证、授权和计费。该]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[专线用户认证成功后，接口上接入的所有该子网内]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户流量均允许通过，且共享一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话，并基于子网进行授权和计费。]{style="font-family:宋体"}

[[每个子网只能配置一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1987075404}[子网专线用户。]{style="font-family:宋体"}

[[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_x418791815}[IPoE]{lang="SV"}[个人接入用户]{style="font-family:宋体"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接口专线用户和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_655908390}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1457564090}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一个]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[子网专线用户]{style="font-family:宋体"}[：]{style="font-family:宋体"}[子网网段为]{style="font-family:宋体"}[1.1.1.1/24]{lang="SV"}[，]{style="font-family:宋体"}[认证使用的用户名为]{style="font-family:宋体"}[netuser]{lang="SV"}[，]{style="font-family:宋体"}[认证使用的明文密码为]{style="font-family:宋体"}[pw123]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x825535989}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber subnet-leased ip 1.1.1.1 24 username ]{lang="SV"}[netuser ]{lang="EN-US"}[password plaintext ]{lang="SV"}[pw123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1820107632}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber subnet-leased]{lang="EN-US"}**]{#struct_0_18608_20265_86621989}
:::

::: {#1713420039 .myid}
[]{#_Toc404785850}[]{#struct_0_18608_20265_x1087463425}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber timer quiet**

------------------------------------------------------------------------

[**[ip subscriber timer quiet]{lang="EN-US"}**]{#struct_0_18608_20265_1999529889}[命令用来配置]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[用户的静默时间。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber timer quiet**]{lang="EN-US"}]{#struct_0_18608_20265_x61981025}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1397894371}

[**[ip subscriber timer quiet]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_18608_20265_2024251404}

[**[undo]{lang="EN-US"}**[ **ip subscriber timer quiet**]{lang="EN-US"}]{#struct_0_18608_20265_x770030329}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1219625372}

[[IPv4 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_445801133}[用户的静默时间功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_536255346}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1653186816}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_70936910}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1232720777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1733028671}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1386829702}

[*[time]{lang="EN-US"}*]{#struct_0_18608_20265_x276478419}[：]{style="font-family:宋体;color:black"}[IPoE]{lang="EN-US" style="color:black"}[用户的静默时间，]{style="font-family:宋体;
color:black"}[取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_973757862}

[[本命令用来设置用户认证失败以后，设备需要等待的时间间隔。在静默期间，设备不对来自认证失败用户的报文进行认证处理，直接丢弃，可以防止该类用户报文持续发送给服务器认证而对设备性能造成影响。静默期后，如果设备再次收到该用户的报文，则依然可以对其进行认证处理。]{style="font-family:宋体"}]{#struct_0_18608_20265_616486777}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x725784693}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1307300075}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户的静默时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x769178361}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber timer quiet 100]{lang="EN-US"}
:::

::: {#2050563623 .myid}
[]{#_Toc404785851}[]{#struct_0_18608_20265_2120121318}[]{#_Toc369161201}[]{#_Toc380594792}[]{#_Toc380594793}[]{#_Toc380594794}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber trust**

------------------------------------------------------------------------

[**[ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_x643523688}[命令用于配置信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的指定]{style="font-family:宋体"}[Option]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ip subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_1466735771}[命令用来取消信任]{style="font-family:
宋体"}[DHCPv4]{lang="EN-US"}[报文中指定的]{style="font-family:宋体"}[Option]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x930637191}

[**[ip subscriber trust]{lang="EN-US"}**[ { **option60** \| **option82** }]{lang="EN-US"}]{#struct_0_18608_20265_x784890613}

[**[undo ip subscriber trust]{lang="EN-US"}**[ { **option60** \| **option82** ]{lang="EN-US"}]{#struct_0_18608_20265_x1995553426}[}]{lang="EN-US" style="font-size:11.5pt"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_110903086}

[[不信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_x1336400912}[报文中的任何]{style="font-family:宋体"}[Option]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_476749667}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1910307571}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1052146146}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x697145004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x217480334}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1523293231}

[**[option60]{lang="EN-US"}**]{#struct_0_18608_20265_x1078488591}[：表示信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[option82]{lang="EN-US"}**]{#struct_0_18608_20265_x583808992}[：表示信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x534916450}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1659068258}[组网环境中，接入设备可以提取用户的]{style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[信息。如果接入设备信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[信息，则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{style="font-family:宋体"}[Option 60]{lang="EN-US"}]{#struct_0_18608_20265_1324076685}[内容有效（无非法字符]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[等），且没有域名分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}[字符的情况下，]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用整个]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[的内容作为指定的认证域进行认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{style="font-family:宋体"}[Option 60]{lang="EN-US"}]{#struct_0_18608_20265_x1427027294}[内容中包含了域名分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}[字符，且]{style="font-family:宋体"}[@]{lang="EN-US"}[字符后的字符串有效（无非法字符]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[等）的情况下，]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[@]{lang="EN-US"}[字符之后的字符串作为指定的认证域进行认证。如果在]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[内容中包括多个]{style="font-family:宋体"}[@]{lang="EN-US"}[字符，则使用最后一个]{style="font-family:宋体"}[@]{lang="EN-US"}[字符之后的字符串作为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户的认证域名。]{style="font-family:宋体"}

[[如果接入设备不信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_797366722}[报文中的]{style="font-family:宋体"}[Option 60]{lang="EN-US"}[信息，但是接口上配置了]{style="font-family:宋体"}**[ip subscriber dhcp domain]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用该命令指定的认证域进行认证；否则，使用缺省认证域进行认证。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x769112825}[中继组网环境中，接入设备可以提取用户的]{style="font-family:宋体"}[DHCP-DISCOVER]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[信息。如果接入设备信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接入设备在采用]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}]{#struct_0_18608_20265_x1453979144}[格式封装]{lang="EN-US" style="font-family:宋体"}[RADIUS NAS-PORT-ID]{lang="EN-US"}[属性时，会根据]{lang="EN-US" style="font-family:宋体"}[Option 82]{lang="EN-US"}[信息中的]{lang="EN-US" style="font-family:宋体"}[Circuit-ID]{lang="EN-US"}[子选项内容封装发往]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接入设备会根据]{lang="EN-US" style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_18608_20265_x392930137}[中的]{lang="EN-US" style="font-family:宋体"}[Circuit-ID]{lang="EN-US"}[子选项内容封装发往]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[DSL_AGENT_CIRCUIT_ID]{lang="EN-US"}[属性；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接入设备会根据]{lang="EN-US" style="font-family:宋体"}[Option 82]{lang="EN-US"}]{#struct_0_18608_20265_1260791433}[中的]{lang="EN-US" style="font-family:宋体"}[R]{lang="EN-US"}[emote]{lang="EN-US"}[-ID]{lang="EN-US"}[子选项内容封装发往]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[DSL_AGENT_REMOTE_ID]{lang="EN-US"}[属性。]{lang="EN-US" style="font-family:宋体"}

[[如果不信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}]{#struct_0_18608_20265_409651209}[报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[，则接入设备在封装以上]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[属性时，不采用]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[中的任何信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1342678386}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1651254568}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备信任]{style="font-family:宋体"}[DHCPv4]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 82]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_1307549417}

[\[Sysname\] interface gigabitgigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitGigabitEthernet1/0/1\] ip subscriber trust option82]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1205590124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_1357404874}
:::

::: {#-1867886808 .myid}
[]{#_Toc404785852}[]{#struct_0_18608_20265_x1276560197}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber unclassified-ip domain**

------------------------------------------------------------------------

[**[ip subscriber unclassified-ip domain]{lang="EN-US"}**]{#struct_0_18608_20265_1972226856}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户使用的认证域。]{style="font-family:宋体"}

[**[undo ip subscriber unclassified-ip domain]{lang="EN-US"}**]{#struct_0_18608_20265_x1866731282}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x231846767}

[**[ip subscriber unclassified-ip domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_1519778271}

[**[undo]{lang="EN-US"}**[ **ip subscriber unclassified-ip domain**]{lang="EN-US"}]{#struct_0_18608_20265_x1101157996}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x769702650}

[[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_935463583}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的认证域为缺省认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1921582227}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1596219790}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x591141982}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1308078334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1480734525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1442980066}

[*[domain-name]{lang="SV"}*]{#struct_0_18608_20265_x1151778127}[：认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:
black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_126384703}

[[该命令用来配置未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18608_20265_1427145474}[报文触发接入的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接入用户在认证时使用的认证域，该域名必须在接入设备上存在且配置完整。]{style="font-family:宋体"}

[[如果指定接口上配置了]{style="font-family:宋体"}**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_121624051}[，则优先使用]{style="font-family:宋体"}**[ip subscriber service-identify]{lang="EN-US"}**[指定的业务识别方式获取对应的认证域。只有在未匹配到]{style="font-family:宋体"}**[ip subscriber service-identify]{lang="EN-US"}**[命令指定的认证域时，才使用]{style="font-family:宋体"}**[ip subscriber unclassified-ip domain]{lang="EN-US"}**[命令指定的认证域。如果]{style="font-family:宋体"}**[ip subscriber unclassified-ip domain]{lang="EN-US"}**[命令也未配置，则使用缺省认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_215680358}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x4081217}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上的]{style="font-family:宋体"}[IPv4]{lang="SV"}[未知源]{style="font-family:宋体"}[IP]{lang="SV"}[接入用户使用的认证域为]{style="font-family:
宋体"}[ipoe]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x769637114}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber unclassified-ip domain ipoe]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x271756861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1793737150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x276233813}
:::

::: {#-748362205 .myid}
[]{#_Toc404785853}[]{#struct_0_18608_20265_1774155383}[]{#_Toc380594797}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber unclassified-ip max-session**

------------------------------------------------------------------------

[**[ip subscriber unclassified-ip max-session]{lang="EN-US"}**]{#struct_0_18608_20265_1349030576}[命令用来配置接口上允许未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文触发创建的动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话的最大数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber unclassified-ip max-session**]{lang="EN-US"}]{#struct_0_18608_20265_1903641563}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1940297789}

[**[ip subscriber]{lang="EN-US"}**[ **unclassified-ip max-session** *max-number*]{lang="EN-US"}]{#struct_0_18608_20265_x373555959}

[**[undo]{lang="EN-US"}**[ **ip subscriber** **unclassified-ip** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_636182582}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1738244520}

[[未限制接口上允许未知源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_1047965147}[报文创建的动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1471290142}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_732897813}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1379942370}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x769833722}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1315143578}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_562997048}

[*[max-number]{lang="EN-US"}*]{#struct_0_18608_20265_176759244}[：允许未知源]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[报文触发]{style="font-family:宋体;
color:black"}[创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x32949158}

[[未知源]{style="font-family:宋体"}]{#struct_0_18608_20265_608073211}[IPv4]{lang="SV"}[报文触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话数目]{style="font-family:宋体"}[达到最大值后]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[后续未知源]{style="font-family:
宋体"}[IPv4]{lang="SV"}[报文不能触发创建]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1115656273}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_926702169}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上允许未知源]{style="font-family:宋体"}[IPv4]{lang="SV"}[报文触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[最大数为]{style="font-family:宋体"}[100]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_1635247606}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber **unclassified-ip** max-session 100]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1368082549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1347070669}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_367719697}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x563484672}
:::

::: {#1293299776 .myid}
[]{#_Toc404785854}[]{#struct_0_18608_20265_1848308662}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber unclassified-ip username**

------------------------------------------------------------------------

[**[ip subscriber unclassified-ip username]{lang="EN-US"}**]{#struct_0_18608_20265_x769768186}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的认证用户名。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber unclassified-ip username**]{lang="EN-US"}]{#struct_0_18608_20265_1735425174}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1944466034}

[**[ip subscriber unclassified-ip username include ]{lang="EN-US"}**[{ **nas-port-id** \| **port** \[ *separator* \] \| **second-vlan** \[ *separator* \] \| **slot** \[ *separator* \] \| **source-ip** \[ **separator**  *separator-char* \] \| **source-mac** \[ **separator** *separator* \] \| **subslot** \[ *separator* \] \| **sysname** \[ *separator* \] \| **vlan** \[ *separator* \] } \*]{lang="EN-US"}]{#struct_0_18608_20265_x1094683432}

[**[undo]{lang="EN-US"}**[ **ip subscriber unclassified-ip username**]{lang="EN-US"}]{#struct_0_18608_20265_x1380792411}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1660395262}

[[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_x1460823305}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户采用[用户报文的]{style="color:black"}源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为认证用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2037356856}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1218521445}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1572332656}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_255984382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x472794796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x138160873}

[**[nas-port-id]{lang="EN-US"}**]{#struct_0_18608_20265_x1101929973}[：表示使用用户的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性作为用户名。]{style="font-family:宋体"}

[**[port]{lang="SV"}**]{#struct_0_18608_20265_x169121513}[：]{style="font-family:宋体"}[表示以报文接入的端口号作为用户名。]{style="font-family:宋体"}

[**[s]{lang="EN-US"}**]{#struct_0_18608_20265_213292381}**[econd-vlan]{lang="SV"}**[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1734900715}[：]{style="font-family:宋体"}[表示以报文接入的槽位号作为用户名]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_18608_20265_493024383}[：表示使用用户报文的]{style="font-family:宋体;color:black"}[源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为用户名]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="EN-US"}***[separator]{lang="EN-US"}*]{#struct_0_18608_20265_x769964794}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址分隔符，可以为任意可配置的可见字符。若指定了分隔符，例如"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则用户名形如]{style="font-family:宋体"}[192-168-1-1]{lang="EN-US"}[；若不指定该参数，则用户名为]{style="font-family:宋体"}[x.x.x.x]{lang="EN-US"}[形式。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_18608_20265_x259918821}[：表示使用用户报文的]{style="font-family:宋体;color:black"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为用户名]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="EN-US"}***[separator-char]{lang="EN-US"}*]{#struct_0_18608_20265_x174811196}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址分隔符，可以为任意可配置的可见字符。若指定了分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="SV"}["，]{style="font-family:
宋体"}[则用户名形如]{style="font-family:宋体"}[xxxx-xxxx-xxxx]{lang="SV"}[；]{style="font-family:宋体"}[若不指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则用户名为]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="SV"}[形式。]{style="font-family:宋体"}

[**[subslot]{lang="SV"}**]{#struct_0_18608_20265_x169121514}[：]{style="font-family:宋体"}[表示以报文接入的子卡号作为用户名。]{style="font-family:宋体"}

[**[sysname]{lang="SV"}**]{#struct_0_18608_20265_212833629}[：]{style="font-family:宋体"}[表示以报文接入设备的设备名作为用户名。]{style="font-family:宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_x1182253683}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[*[separator]{lang="SV"}*]{#struct_0_18608_20265_x299673134}[：]{style="font-family:宋体"}[当前字段分隔符，用在当前字段后面以连接后面的一个字段，可以为任意可配置的可见字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x158888337}

[[本命令用来配置未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18608_20265_x614033434}[报文触发接入的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户在认证时使用的用户名，该用户名必须与认证服务器上配置的用户名保持一致。此类用户进行]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[认证时使用的密码由]{style="font-family:宋体"}**[ip subscriber password]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[在允许的用户名类型范围内，该命令支持任意形式、任意顺序的用户名组合。例如：若配置]{style="font-family:宋体"}**[ip subscriber unclassified-ip username include source-ip source-mac]{lang="EN-US"}**]{#struct_0_18608_20265_2036364266}[，则用户名为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址字段]{style="font-family:宋体"}[和]{style="font-family:宋体"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[字段内容的拼接，且两个字段之间无分隔符。]{style="font-family:宋体"}

[[建议不要使用]{style="font-family:宋体"}]{#struct_0_18608_20265_965500417}[@]{lang="SV"}[作为分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[避免携带]{style="font-family:宋体"}[@]{lang="SV"}[字符的用户名在]{style="font-family:
宋体"}[AAA]{lang="SV"}[服务器端不能被正确解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x676842103}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x498144200}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上的未知源]{style="font-family:宋体"}[IPv4]{lang="SV"}[用户使用用户报文的源]{style="font-family:宋体"}[IPv4]{lang="SV"}[地址作为用户名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_2085615630}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber unclassified-ip username include source-ip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_937865785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1042310801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_1253196095}
:::

::: {#-927449916 .myid}
[]{#_Toc404785855}[]{#struct_0_18608_20265_1890478409}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber user-detect**

------------------------------------------------------------------------

[**[ip subscriber user-detect]{lang="EN-US"}**]{#struct_0_18608_20265_x1612663983}[命令用来开启静态]{style="font-family:
宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人接入用户在线探测功能，并配置其探测方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber user-detect**]{lang="EN-US"}]{#struct_0_18608_20265_x769899258}[命令用来关闭静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人接入用户在线探测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1374555769}

[**[ip subscriber user-detect ]{lang="EN-US"}**[{ **arp** \| **icmp** } **retry** *times* **interval** *interval*]{lang="EN-US"}]{#struct_0_18608_20265_1250181840}

[**[undo]{lang="EN-US"}**[ **ip subscriber user-detect** ]{lang="EN-US"}]{#struct_0_18608_20265_70561883}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x623527577}

[[静态]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x208237406}[动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人接入用户在线探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x452571503}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x976519729}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1403578603}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_961660959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1861178048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x474239271}

[**[arp]{lang="EN-US"}**]{#struct_0_18608_20265_982837347}[：]{style="font-family:宋体;color:black"}[表示使用]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求报文作为探测报文。]{style="font-family:宋体"}

[**[icmp]{lang="SV"}**]{#struct_0_18608_20265_x106516517}[：]{style="font-family:宋体;color:black"}[表示使用]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[请求报文作为探测报文。]{style="font-family:宋体"}

[**[retry]{lang="SV"}[ ]{lang="SV"}**]{#struct_0_18608_20265_x770095866}*[times]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[探测失败后允许重复尝试的最大次数]{style="font-family:宋体;
color:black"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体;color:black"}[2]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[5]{lang="EN-US" style="color:black"}[。例如，]{style="font-family:宋体;color:black"}*[times]{lang="SV"}*[值为]{style="font-family:宋体;color:black"}[2]{lang="EN-US" style="color:black"}[表示连续三次失败就认为用户不在线。]{style="font-family:宋体;color:black"}

[**[interval ]{lang="SV"}**]{#struct_0_18608_20265_1646944105}*[interval]{lang="SV"}*[：]{style="font-family:
宋体;color:black"}[探测的时间间隔]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;color:black"}[取值范围为]{style="font-family:宋体;
color:black"}[30]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[1200]{lang="SV" style="color:black"}[，]{style="font-family:宋体;color:black"}[单位为秒。]{style="font-family:宋体;
color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x713068478}

[[接口上的静态]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x2021558641}[动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[个人接入用户上线后，设备会定时统计用户流量。若一个探测间隔（]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[）内用户流量无变化，则该探测间隔结束后，设备将发送一次探测报文。]{style="font-family:宋体"}[如果设备在探测间隔内未收到用户的报文，则认为一次探测失败。]{style="font-family:宋体"}

[[若设备首次探测失败，将继续做指定次数（]{style="font-family:宋体"}*[times]{lang="EN-US"}*]{#struct_0_18608_20265_1570988364}[）的重复探测，若全部]{style="font-family:宋体"}[探测尝试都]{style="font-family:宋体"}[失败（即]{style="font-family:宋体"}[一直]{style="font-family:宋体"}[未收到该用户报文），则认为此用户不在线，停止发送探测报文并删除用户；若设备在探测中收到用户的报文，则认为用户在线，重置探测定时器并开始下一次探测]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[对于与接口]{style="font-family:宋体"}]{#struct_0_18608_20265_992513805}[在同一网段内的静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[IPoE]{lang="SV"}[个人接入]{style="font-family:宋体"}[用]{style="font-family:宋体"}[户，可使用]{style="font-family:宋体"}[ARP]{lang="SV"}[请求]{style="font-family:宋体"}[或]{style="font-family:
宋体"}[ICMP]{lang="SV"}[请求]{style="font-family:宋体"}[报文对用户进行探测；]{style="font-family:宋体"}[对于与接口不]{style="font-family:宋体"}[在同一网段内的静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[IPoE]{lang="SV"}[个人接入]{style="font-family:宋体"}[用]{style="font-family:宋体"}[户，应使用]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[请求]{style="font-family:宋体"}[报文对用户进行探测。]{style="font-family:宋体"}

[[接口上不可同时启用两种方式对静态]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1139013286}[动态]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[IPoE]{lang="SV"}[个人接入用户进行探测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1262127534}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x2061466647}[开启接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使用]{style="font-family:宋体"}[ARP]{lang="SV"}[请求报文对静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[个人接入用户进行在线探测，[探测失败后允许重复尝试]{style="color:black"}]{style="font-family:宋体"}[5]{lang="EN-US" style="color:black"}[次，探测的时间间隔为]{style="font-family:宋体;color:black"}[100]{lang="EN-US" style="color:black"}[秒]{style="font-family:宋体;
color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x311864616}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ip subscriber user-detect arp retry 5 interval 100]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1157257844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1478349551}
:::

::: {#1054183514 .myid}
[]{#_Toc404785856}[]{#struct_0_18608_20265_x203323960}

**IPoE \-- IPv4 IPoE配置命令 \-- ip subscriber vlan**

------------------------------------------------------------------------

[**[ip subscriber vlan]{lang="EN-US"}**]{#struct_0_18608_20265_x1934001044}[命令用于配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip subscriber vlan**]{lang="EN-US"}]{#struct_0_18608_20265_x770030330}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1219166621}

[**[ip subscriber vlan]{lang="EN-US"}***[ vlan-list]{lang="EN-US"}***[ domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_x717689286}

[**[undo ip subscriber vlan]{lang="EN-US"}***[ vlan-list]{lang="EN-US"}*]{#struct_0_18608_20265_x1029962973}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x304328410}

[[未指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_18608_20265_754161114}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x436429376}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1337922261}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1807745748}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1041125057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_73197035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x169240884}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_18608_20265_2103648410}[：]{style="font-family:宋体;color:black"}[VLAN]{lang="SV"}[列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示一个或多个]{style="font-family:宋体"}[VLAN]{lang="SV"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:
宋体"}*[vlan-list]{lang="SV"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="SV"}[，]{style="font-family:
宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:
宋体"}*[vlan-id]{lang="SV"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="SV"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1408810116}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1387453727}

[[本命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_18608_20265_x769178362}[范围内未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户进行认证时使用的认证域，通过指定的认证域进行认证、授权、计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_2120317926}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1331868195}[在子接口]{style="font-family:宋体"}[GigabitEthernet1/0/1.100]{lang="EN-US"}[上配置内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[到]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户认证使用的认证域为]{style="font-family:宋体"}[vlandm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1070089998}

[\[Sysname\] interface gigabitethernet 1/0/1.100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ip subscriber service-identify second-vlan]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ip subscriber vlan 2 to 100 domain vlandm]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_767536449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x391975534}
:::

::: {#503964332 .myid}
[]{#_Toc404785857}[]{#struct_0_18608_20265_235832410}

**IPoE \-- IPv4 IPoE配置命令 \-- reset ip subscriber offline statistics**

------------------------------------------------------------------------

[**[reset ip subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_1248347521}[命令用来清除]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_954334452}

[**[reset ip subscriber offline statistics ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x152662126}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1423772051}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18608_20265_1103699130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1019362584}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1335419894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x769112826}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1454044680}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_1518932148}[：]{style="font-family:宋体;color:black"}[表示清除指定接口上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将]{style="font-family:
宋体"}[清除所有接口上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1455940917}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1271777681}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[用户下线统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip subscriber offline statistics interface gigabitethernet 1/0/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_923696037}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x444648433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_269334117}
:::

::: {#498410241 .myid}
[]{#_Toc404785858}[]{#struct_0_18608_20265_x1125722388}

**IPoE \-- IPv4 IPoE配置命令 \-- reset ip subscriber session**

------------------------------------------------------------------------

[**[reset ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_307510256}[命令用来清除动态触发创建的]{style="font-family:
宋体"}[IPv4 IPoE]{lang="EN-US"}[会话，强制用户下线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_816780706}

[**[reset ip subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ip** *ip-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **username** *name* \]]{lang="EN-US"}]{#struct_0_18608_20265_1904320156}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1676336118}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x413214358}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1126868066}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_796381288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x420535172}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1622188907}

[**[interface ]{lang="SV"}**]{#struct_0_18608_20265_153540760}*[interface-type interface-number]{lang="SV" style="color:black"}*[：表示]{style="font-family:宋体;color:black"}[清除指定接口动态触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="SV"}*[表示接口类型和接口编号。如果未指定本参数]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[将]{style="font-family:宋体"}[清除所有接口]{style="font-family:宋体"}[动态]{style="font-family:宋体"}[触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_x1447315771}*[ domain-name]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除使用]{style="font-family:宋体"}[指定]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域认证的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[domain-name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:宋体"}[@]{lang="SV"}["]{style="font-family:
宋体"}[字符。]{style="font-family:宋体"}

[**[ip]{lang="SV"}**]{#struct_0_18608_20265_x869769353}*[ ip-address]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;color:black"}[清除指定]{style="font-family:宋体"}[IP]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话，]{style="font-family:宋体"}*[ip-address]{lang="SV"}*[为指定的]{style="font-family:宋体"}[IPv4]{lang="SV"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="SV"}**]{#struct_0_18608_20265_1693970727}*[vpn-instance-name]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除[指定]{style="color:black"}]{style="font-family:宋体"}[VPN]{lang="SV" style="color:black"}[的]{style="font-family:宋体;color:black"}[IPv4 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}*[vpn-instance-name]{lang="SV"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="SV"}[的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:
宋体"}[31]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mac]{lang="SV"}**]{#struct_0_18608_20265_1990875015}*[ mac-address]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除指定[源]{style="color:black"}]{style="font-family:宋体"}[MAC]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体"}

[**[username ]{lang="SV"}**]{#struct_0_18608_20265_x1100368523}*[name]{lang="SV"}*[：表示]{style="font-family:宋体;
color:black"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体;color:black"}[用户名]{style="font-family:宋体;
color:black"}[的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_83432460}

[[本命令用来清除动态触发创建的]{style="font-family:宋体"}]{#struct_0_18608_20265_335378754}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并强制用户下线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[如果不指定条件]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则表示删除所有动态]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[专线用户和静态个人用户不能通过]{style="font-family:宋体"}]{#struct_0_18608_20265_1671359609}**[reset ip subscriber session]{lang="SV" style="color:black"}**[命令强制下线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[只能通过相应的]{style="font-family:宋体"}**[undo]{lang="SV"}**[命令删除配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1101011894}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1222219900}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上动态触发创建的]{style="font-family:宋体"}[IPv4 IPoE]{lang="SV"}[会话，]{style="font-family:宋体"}[强制用户下线。]{style="font-family:宋体"}

[[\<Sysname\> reset ip subscriber session interface gigabitethernet 1/0/1]{lang="SV" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_796446824}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1310944122}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1315208777}
:::

::: {#594279436 .myid}
[]{#_Toc404785860}[]{#struct_0_18608_20265_x2141105052}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber interface-leased**

------------------------------------------------------------------------

[**[display ipv6 subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_x1573208715}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_348231340}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_x1503462924}

[**[display ipv6 subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_1321845236}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_397858056}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1101910808}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_x1271305664}[模式]{style="font-family:宋体"}

[**[display ipv6 subscriber interface-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_1162146759}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x192737452}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_1037802208}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_796250216}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1629347105}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_788112384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x971183826}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x2096793963}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1796380884}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_1965775047}[：]{style="font-family:宋体;color:black"}[显示指定接口上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_971676278}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1064355411}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:
宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1252709827}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[slot-number]{lang="SV"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1831923006}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持[IRF3]{lang="SV"}的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1119877632}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_185632911}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[接口专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1457476978}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1494771944}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber interface-leased interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_1645798325}

[[Basic:]{lang="EN-US"}]{#struct_0_18608_20265_796315752}

[[  Access interface           : GE1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_1678855460}

[[  VPN instance               : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x276590123}

[[  Username                   : a]{lang="EN-US"}]{#struct_0_18608_20265_x1403583906}

[[  User ID                    : 0x40000000]{lang="EN-US"}]{#struct_0_18608_20265_623210817}

[[  State                      : Online]{lang="EN-US"}]{#struct_0_18608_20265_x1002005490}

[[  Service node               : Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_18608_20265_20225517}

[[  Domain                     : radius6]{lang="EN-US"}]{#struct_0_18608_20265_1678920996}

[[  Login time                 : May 14 20:20:11 2014]{lang="EN-US"}]{#struct_0_18608_20265_461714406}

[[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}]{#struct_0_18608_20265_x1205721196}

[ ]{lang="EN-US"}

[[AAA:]{lang="EN-US"}]{#struct_0_18608_20265_x46218710}

[[  IP pool                    : ipoe]{lang="EN-US"}]{#struct_0_18608_20265_x1464577794}

[[  Session idle time          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1913019660}

[[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}]{#struct_0_18608_20265_107689320}

[[  Max multicast addresses    : 4]{lang="EN-US"}]{#struct_0_18608_20265_x487151462}

[[  Multicast address list     : N/A]{lang="EN-US"}]{#struct_0_18608_20265_986626300}

[ ]{lang="EN-US"}

[[QoS:]{lang="EN-US"}]{#struct_0_18608_20265_x506736793}

[[  User profile               : h3c6 (active)]{lang="EN-US"}]{#struct_0_18608_20265_1678986532}

[[  Session group profile      : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1628696450}

[[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_x1799271836}

[[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_970345126}

[ ]{lang="EN-US"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_x2094025306}

[[  Uplink   packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_905344980}

[[  DownLink packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1626829426}

[ ]{lang="EN-US"}

[[ITA:]{lang="EN-US"}]{#struct_0_18608_20265_x893891508}

[[  Level-1 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_580235790}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1679052068}

[[  Level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1457316286}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_260982960}

[[  Level-3 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x379244685}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x598813631}

[[  Level-4 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x826226470}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_68556665}

[[  Level-5 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_358373575}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1367520796}

[[  Level-6 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1679117604}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_2043640814}

[[  Level-7 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1596573800}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1040298951}

[[  Level-8 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_36169971}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1918527930}

[[表1-7 ]{lang="EN-US"}[display ipv6 subscriber interface-leased]{lang="EN-US"}]{#struct_0_18608_20265_285698662}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2076030561}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x828286045}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x76212356}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_x1050355578}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_33143828}[会话的基本信息]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_x1050290042}

[[用户所在的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_x930375769}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_1193188145}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_x1050224506}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_18608_20265_1553975003}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_x2695966}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_x803144150}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_982172488}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_890535715}

[[用户的认证状态]{style="font-family:宋体"}]{#struct_0_18608_20265_x1689805912}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_x952368774}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_796184680}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_1630795504}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_844942770}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass ]{lang="EN-US"}]{#struct_0_18608_20265_1596855796}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_x1884048002}[：]{lang="EN-US" style="font-family:宋体"}[用户已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_x611872003}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_x37361174}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1050093434}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_2063773293}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_x1050027898}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_x1944551417}

[[认证使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_x1229272398}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_x1382373596}

[[用户登录时间]{style="font-family:宋体"}]{#struct_0_18608_20265_217373398}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_x1118557635}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_x2082651086}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1049962362}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1087978057}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_1875381668}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1049896826}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_x2081598991}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_1915388215}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_x1175016927}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1049831290}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1341932101}[：表示未授权会话时长]{style="font-family:宋体"}

[[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_x309170302}[：表示会话时长无限制]{style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_x1049765754}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1119214717}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1962223662}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_x1050355579}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1599227769}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_719703435}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1044074}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_x1050290043}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_635708172}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_x511339789}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1050224507}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x33845836}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x453998735}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_x1050158971}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_x870781875}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_461213190}[授权的]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1050093435}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x665110062}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:
  宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_x503242562}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1050027899}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1346509759}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1815984827}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x907815320}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x631883537}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_1616075939}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1049962363}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1815984828}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x908405144}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_1815984825}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic]{lang="EN-US"}]{#struct_0_18608_20265_478105884}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_255245714}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1049896827}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_647284364}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x2049077983}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1049831291}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_1386951254}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1278405355}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1049765755}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_x1609668638}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1050355576}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_1552173602}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1236435861}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x308977441}

::: {#-1045808708 .myid}
[]{#_Toc404785861}[]{#struct_0_18608_20265_x666611820}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber interface-leased statistics**

------------------------------------------------------------------------

[**[display ipv6 subscriber interface-leased statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18608_20265_180196894}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1507379103}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_1299529087}

[**[display ipv6 subscriber interface-leased statistics ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_796119143}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_1659743941}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber interface-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_1553647322}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_410580111}[模式：]{style="font-family:宋体"}

[**[display ipv6 subscriber interface-leased statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *[chassis-number ]{style="color:black"}***slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_951419419}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1145501056}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x1566263349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x207472177}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1686767665}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1154165541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x393955545}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_2037220439}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1293944919}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x1623774733}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[接口专线用户已经上线和正在上线的统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_796184679}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_439154407}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[接口专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:
宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_494514937}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[ IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1780356670}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[接口专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1618429922}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[接口专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_1373659339}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息，]{style="font-family:宋体"}[cpu-number]{lang="EN-US"}[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x898622641}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1399571147}[显示设备上已经上线和正在上线的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接口专线用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber interface-leased statistics]{lang="EN-US"}]{#struct_0_18608_20265_1873241928}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ipv6 subscriber interface-leased statistics]{lang="EN-US"}]{#struct_0_18608_20265_x850214740}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2065454193}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x438296713}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_1601829050}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_x1395180455}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_795988071}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x35582830}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x446654491}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x2146484437}

[[处于正在认证状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_2122752069}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_378474620}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x1619961784}[认证失败]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_x889747581}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_1176412902}[认证成功]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1823990343}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_796053607}[成功分配到]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;
  color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1908017844}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x1999755973}[在线]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_158464176}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_x1085477948}

[ ]{lang="EN-US"}

::: {#-1460141502 .myid}
[]{#_Toc404785862}[]{#struct_0_18608_20265_1351956566}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber offline statistics**

------------------------------------------------------------------------

[**[display ipv6 subscriber offline statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18608_20265_x1668978614}[命令用来显示]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户下线原因的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_422763899}

[**[display ipv6 subscriber offline statistics ]{lang="EN-US"}**[\[ **interface** *[interface]{style="color:black"}*]{lang="EN-US"}]{#struct_0_18608_20265_167101556}*[-type ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface]{lang="EN-US" style="color:black"}[-]{lang="EN-US" style="font-size:
10.0pt;color:black"}[number ]{lang="EN-US" style="color:black"}*[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1054708445}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_796905575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x890470064}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x491575765}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_689603545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_678926582}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_1533976755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2079577408}

[**[interface]{lang="EN-US" style="color:black"}**]{#struct_0_18608_20265_1959505256}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}***[interface]{lang="EN-US" style="color:black"}[-type ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface]{lang="EN-US" style="color:black"}[-]{lang="EN-US" style="font-size:
10.0pt;color:black"}[number]{lang="EN-US" style="color:black"}*[：]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[显示指定接口上]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户下线原因的统计]{lang="EN-US" style="font-family:宋体"}[信息]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}*[interface-type]{lang="EN-US" style="color:black"}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface-number]{lang="EN-US" style="color:
black"}*[表示接口类型和接口编号。]{lang="EN-US" style="font-family:宋体"}[如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户下线原因的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2007048860}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_192921258}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户下线原因的统计信息]{style="font-family:宋体"}

[[\<Sysname\> displsy ipv6 subscriber offline statistics interface gigabitethernet1/0/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_x296215216}

[[Total               : 100]{lang="EN-US"}]{#struct_0_18608_20265_796971111}

[User request        : 0]{lang="EN-US"}

[DHCP  lease expire  : 0]{lang="EN-US"}

[AAA lease expire    : 0]{lang="EN-US"}

[Command cut         : 80]{lang="EN-US"}

[AAA terminate       : 0]{lang="EN-US"}

[Authenticate fail]{lang="EN-US" style="color:black"}[   :]{lang="EN-US" style="font-size:8.0pt;color:black"}[ 0]{lang="EN-US"}

[Authorization fail]{lang="EN-US" style="color:black"}[  :]{lang="EN-US" style="font-size:8.0pt;color:black"}[ 0]{lang="EN-US"}

[Idle timeout        : 10]{lang="EN-US"}

[Detect fail         : 10]{lang="EN-US"}

[Not enough resource : 0]{lang="EN-US"}

[DHCP request timeout: 0]{lang="EN-US"}

[Interface down      : 0]{lang="EN-US"}

[Interface shutdown  : 0]{lang="EN-US"}

[VSRP event          : 0]{lang="EN-US"}

[DHCP notify         : 0]{lang="EN-US"}

[Other               : 0]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ipv6 subscriber offline statistics]{lang="EN-US"}]{#struct_0_18608_20265_1469885981}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2066181789}

[ ]{lang="EN-US"}
:::

[ ]{lang="EN-US"}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_434084307}

[[下线的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_108968139}

[[User request]{lang="EN-US"}]{#struct_0_18608_20265_651357138}

[[用户主动要求下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_167801399}

[[DHCP lease expired]{lang="EN-US"}]{#struct_0_18608_20265_x1109284454}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1079842043}[租约到期正常下线的用户数]{style="font-family:宋体"}

[[AAA lease expired]{lang="EN-US"}]{#struct_0_18608_20265_x1044046535}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_796381286}[租约到期正常下线的用户数]{style="font-family:宋体"}

[[Command cut]{lang="EN-US"}]{#struct_0_18608_20265_x420535162}

[[通过命令行下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_1622188906}

[[AAA terminate]{lang="EN-US"}]{#struct_0_18608_20265_153606296}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1528758698}[强制下线的用户数]{style="font-family:宋体"}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_x828872499}

[[认证失败的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_1462233881}

[[Authorization fail]{lang="EN-US"}]{#struct_0_18608_20265_945926615}

[[授权失败的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_562923324}

[[Idle timeout]{lang="EN-US"}]{#struct_0_18608_20265_796446822}

[[用户空闲超时下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x1310944120}

[[Detect fail]{lang="EN-US"}]{#struct_0_18608_20265_152409363}

[[在线探测失败下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x831024717}

[[Not enough resource]{lang="EN-US"}]{#struct_0_18608_20265_1000017730}

[[硬件资源不足下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_240878012}

[[DHCP request timeout]{lang="EN-US"}]{#struct_0_18608_20265_x1406265524}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1744133838}[请求超时下线的用户数]{style="font-family:宋体"}

[[Interface down]{lang="EN-US"}]{#struct_0_18608_20265_x1185951972}

[[因接口状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_18608_20265_796250214}[下线的用户数]{style="font-family:宋体"}

[[Interface shutdown]{lang="EN-US"}]{#struct_0_18608_20265_x1629347107}

[[主动]{style="font-family:宋体"}[shutdown]{lang="EN-US"}]{#struct_0_18608_20265_x374687030}[接口导致下线的用户数]{style="font-family:宋体"}

[[VSRP event]{lang="EN-US"}]{#struct_0_18608_20265_836782533}

[[收到]{style="font-family:宋体"}[VSRP]{lang="EN-US"}]{#struct_0_18608_20265_x2126531229}[（]{style="font-family:宋体"}[Virtual Service Redundancy Protocol]{lang="EN-US"}[，虚拟业务冗余协议）]{style="font-family:宋体"}

[事件通知而下线的用户数]{style="font-family:宋体"}

[[DHCP notify]{lang="EN-US"}]{#struct_0_18608_20265_769910394}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_365814074}[通知下线的用户数]{style="font-family:宋体"}

[[Other ]{lang="EN-US"}]{#struct_0_18608_20265_796315750}

[[其它状况触发下线的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_285698660}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x828286043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x76605572}

::: {#1367947875 .myid}
[]{#_Toc404785863}[]{#struct_0_18608_20265_x1290836120}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber session**

------------------------------------------------------------------------

[**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_673639189}[命令用来显示静态配置和动态触发的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_690258528}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_1170295967}

[**[display ipv6 subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ipv6** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_84448028}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_617171892}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ipv6** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_551186853}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_x1690003565}[模式]{style="font-family:宋体"}

[**[display ipv6 subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ipv6** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **static** \| **username** *name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_18608_20265_301279133}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_796119142}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_1659743940}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1553712858}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1947583628}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_168004343}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1907490087}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_1180588437}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_660984310}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_444699345}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:
宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1720236266}*[ domain-name]{lang="SV"}*[：显示使用指定]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域认证的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，]{style="font-family:宋体"}*[domain-name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"} ["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:宋体"}[以及]{style="font-family:
宋体"}["]{style="font-family:宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。]{style="font-family:宋体"}

[**[ipv6]{lang="SV"}**]{#struct_0_18608_20265_1273776877}*[ ipv6-address]{lang="SV"}*[：显示]{style="font-family:宋体;color:black"}[指定源]{style="font-family:宋体;color:black"}[IP]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[ipv6-address]{lang="SV"}*[为指定的]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="SV"}**]{#struct_0_18608_20265_x1521225649}*[vpn-instance-name]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[指定用户所属的]{style="font-family:宋体;
color:black"}[VPN]{lang="SV" style="color:black"}[，]{style="font-family:宋体;color:black"}*[vpn-instance-name]{lang="SV"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="SV"}[的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[31]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mac]{lang="SV"}**]{#struct_0_18608_20265_1554023390}*[ mac-address]{lang="SV"}*[：显示]{style="font-family:宋体;color:black"}[指定源]{style="font-family:宋体;color:black"}[MAC]{lang="SV" style="color:black"}[地址的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体;color:black"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_18608_20265_x1696872648}[：显示]{style="font-family:宋体;color:black"}[静态配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，不指定该参数时将显示静态配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话和动态触发创建的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[username ]{lang="SV"}**]{#struct_0_18608_20265_796184678}*[name]{lang="SV"}*[：显示指定]{style="font-family:宋体;
color:black"}[用户名的]{style="font-family:宋体;color:black"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:
宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_439154408}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的静态配置和动态触发的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1780356657}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1071634540}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1373200589}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（]{style="font-family:宋体"}[不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1876676243}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_x963627711}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，]{style="font-family:宋体"}[cpu-number]{lang="EN-US"}[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_18608_20265_x84586046}[：显示]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US" style="color:black"}[会话的详细信息。]{style="font-family:宋体;color:black"}[如果不指定该参数，则只显示]{style="font-family:宋体"}[IPoE]{lang="EN-US" style="color:black"}[会话]{style="font-family:宋体;color:black"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1459753424}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1738786529}[显示用户]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[2000::1]{lang="EN-US"}[，所属]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber session ipv6 2000::1 vpn-instance vpn1]{lang="EN-US"}]{#struct_0_18608_20265_1667640193}

[Type: D-Dhcp   S-Static     U-Unclassified-ip   N-Ndrs]{lang="EN-US"}

[Interface            IP address                MAC address    Type  State ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[RAGG1024             2000::1                   000d-88f8-0eab D     Online]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1731744658}[显示所有静态配置和动态触发的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[个人]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[的详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber session verbose]{lang="EN-US"}]{#struct_0_18608_20265_x2093858232}

[[Basic:]{lang="EN-US"}]{#struct_0_18608_20265_795988070}

[[  Username                   : abc]{lang="EN-US"}]{#struct_0_18608_20265_x1050027897}

[[  Domain                     : radius6]{lang="EN-US"}]{#struct_0_18608_20265_x172520015}

[[  VPN instance               : vpn1]{lang="EN-US"}]{#struct_0_18608_20265_x26344863}

[[  IP address                 : 2000::1]{lang="EN-US"}]{#struct_0_18608_20265_x469074835}

[[  MAC address                : 000d-88f8-0eab]{lang="EN-US"}]{#struct_0_18608_20265_x1049962361}

[[  Service-VLAN/Customer-VLAN : -/-]{lang="EN-US"}]{#struct_0_18608_20265_1640905298}

[[  Access interface           : GE1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x1516837660}

[[  User ID                    : 0x48080008]{lang="EN-US"}]{#struct_0_18608_20265_2006766509}

[[  VPI/VCI(for ATM)           : -/-]{lang="EN-US"}]{#struct_0_18608_20265_216531072}

[[  DHCP lease                 : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1479588182}

[[  DHCP remain lease          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1660730942}

[[  Login time                 : May  9 09:10:01 2014]{lang="EN-US"}]{#struct_0_18608_20265_x2134404130}

[[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}]{#struct_0_18608_20265_x1474984603}

[[  Service node               : Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_18608_20265_x427776211}

[[  Type                       : Unclassified-ip]{lang="EN-US"}]{#struct_0_18608_20265_x1049896825}

[[  State                      : Online]{lang="EN-US"}]{#struct_0_18608_20265_1810083778}

[ ]{lang="EN-US"}

[[AAA:]{lang="EN-US"}]{#struct_0_18608_20265_x1429297319}

[[  IP pool                    : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1790095625}

[[  Session idle time          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1135588991}

[[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1943029415}

[[  Max multicast addresses    : 4]{lang="EN-US"}]{#struct_0_18608_20265_186365874}

[[  Multicast address list     : N/A]{lang="EN-US"}]{#struct_0_18608_20265_2133896878}

[ ]{lang="EN-US"}

[[QoS:]{lang="EN-US"}]{#struct_0_18608_20265_x1397088669}

[[  User profile               : h3c6 (active)]{lang="EN-US"}]{#struct_0_18608_20265_x1049831289}

[[  Session group profile      : N/A]{lang="EN-US"}]{#struct_0_18608_20265_1743116078}

[[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_104433689}

[[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_x1302624176}

[ ]{lang="EN-US"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_385461869}

[[  Uplink   packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1968751008}

[[  DownLink packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1276459002}

[ ]{lang="EN-US"}

[[ITA:]{lang="EN-US"}]{#struct_0_18608_20265_1659247147}

[[  Level-1 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1994061081}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1049765753}

[[  Level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x446869224}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1415173305}

[[  Level-3 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_2086558951}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1040398785}

[[  Level-4 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1131106706}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_581757700}

[[  Level-5 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1267558689}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1461146023}

[[  Level-6 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1339057264}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1050355574}

[[  Level-7 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1579994280}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1527511851}

[[  Level-8 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1393791249}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1272511151}

[[图1-1 ]{lang="EN-US"}[display ipv6 subscriber session]{lang="EN-US"}]{#struct_0_18608_20265_x35582829}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_2090702197}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_1891997676}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x1627665372}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_x1050290038}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x123347963}[会话的基本信息]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_18608_20265_1998556258}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_x1050224502}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_796053606}

[[用户认证时使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_x1908017845}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_x433672032}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_x1887515640}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_18608_20265_x1318584681}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18608_20265_1176184057}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_18608_20265_x1481373863}

[[用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_18608_20265_452073502}[地址]{style="font-family:宋体"}

[[Service-VLAN/Customer-VLAN]{lang="EN-US"}]{#struct_0_18608_20265_x1050158966}

[[用户所在的公网]{style="font-family:宋体"}[VLAN/]{lang="EN-US"}]{#struct_0_18608_20265_x1274000866}[私网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示没有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息）]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_x1050093430}

[[用户接入的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_94404825}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_x753150773}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_x1361776126}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[VPI/VCI(for ATM)]{lang="EN-US"}]{#struct_0_18608_20265_1413381418}

[[ATM]{lang="EN-US"}]{#struct_0_18608_20265_x463499090}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[DHCP lease]{lang="EN-US"}]{#struct_0_18608_20265_x1049962358}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_430855109}[服务器分配给用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1059290212}[：表示无]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[租约]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_x1049896822}[：表示租约无限长]{lang="EN-US" style="font-family:宋体"}

[[DHCP remain lease]{lang="EN-US"}]{#struct_0_18608_20265_243999837}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_757771298}[服务器分配给用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址租约剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1049831286}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_1790170245}

[[用户登录时间]{style="font-family:宋体"}]{#struct_0_18608_20265_x2020124527}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_x1118819779}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_1253767680}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1049765750}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_x850153751}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_x2012965838}

[[Type]{lang="EN-US"}]{#struct_0_18608_20265_x1050355575}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x13910339}[会话的创建类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1050290039}[：]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unclassified-ip]{lang="EN-US"}]{#struct_0_18608_20265_1442735978}[：未知源]{lang="EN-US" style="font-family:
  宋体"}[IP]{lang="EN-US"}[报文触发创建]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_18608_20265_78964139}[：静态配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NDRS]{lang="EN-US"}]{#struct_0_18608_20265_646507093}[：]{lang="EN-US" style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[报文触发创建]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_x1050224503}

[[用户状态：]{style="font-family:宋体"}]{#struct_0_18608_20265_x2003214304}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_x1050158967}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_292083075}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_654845532}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_x1050093431}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass]{lang="EN-US"}]{#struct_0_18608_20265_1660488766}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_x1008947603}[：]{lang="EN-US" style="font-family:宋体"}[会话已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_x1050027895}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_x1335319429}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1143735499}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1049962359}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_1996939050}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1322991128}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_x1049896823}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1322084104}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_x1049831287}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_224086304}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_305775030}[：表示未授权会话时长]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_x1049765751}[：表示会话时长无限制]{lang="EN-US" style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_715930190}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1453640105}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1840991619}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_x451815637}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1453574569}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_2122669908}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1175174892}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_x1453509033}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x48448610}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_x1453443497}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1153550666}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_18608_20265_1403069544}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in]{lang="EN-US"}]{#struct_0_18608_20265_x1453377961}[a]{lang="EN-US"}[ctive]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_1645787776}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_x1453312425}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x769147703}[授权的]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session]{lang="EN-US"}[ Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_18608_20265_x652128003}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in]{lang="EN-US"}]{#struct_0_18608_20265_x1453246889}[a]{lang="EN-US"}[ctive]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_45623752}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1453181353}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_2034677145}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1714308415}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1714308414}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_660537576}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1453115817}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x2070097001}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1714308417}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_257253049}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x1081595743}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_x1249440702}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1453050281}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_2034289263}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1453640106}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1437707092}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x466639528}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_x1453574570}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_200290071}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1453509034}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_711066277}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1453443498}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_x2025671383}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1010390051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x267091747}

::: {#-326186944 .myid}
[]{#_Toc404785864}[]{#struct_0_18608_20265_x723741449}[]{#_Toc345424013}[]{#_Toc345404991}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber session statistics**

------------------------------------------------------------------------

[**[display ipv6 subscriber session statistics]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_18608_20265_x1223461351}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_844703834}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_2116682299}

[**[display ipv6 subscriber session statistics ]{lang="EN-US"}**[\[ **session-type** { **dhcp** \| **ndrs** \| **static** \| **unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_554897321}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_987479342}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber session statistics]{lang="EN-US"}**[ \[ **session-type** { **dhcp** \| **ndrs** \| **static \| unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot***[ slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \]*[ ]{style="color:black"}*\]]{lang="EN-US"}]{#struct_0_18608_20265_163759947}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_796250220}[模式：]{style="font-family:宋体"}

[**[display ipv6 subscriber session statistics]{lang="EN-US"}**[ \[ **session-type** { **dhcp** \| **ndrs \|** **static** \|  **unclassified-ip** } \] \[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *[chassis-number ]{style="color:black"}***slot*[ ]{style="color:black"}****[slot-number ]{style="color:black"}*\[ **cpu** *cpu-number* \]*[ ]{style="color:black"}*\]]{lang="EN-US"}]{#struct_0_18608_20265_709305049}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_824590126}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x1120152793}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_532437395}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x239697707}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_182027524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x319039915}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x601554443}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1377813426}

[**[session-type]{lang="EN-US"}**]{#struct_0_18608_20265_x1191139172}[：用户上线类型。]{style="font-family:宋体"}[不指定该参数，则表示显示所有类型的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[**[dhcp]{lang="EN-US"}**]{#struct_0_18608_20265_x27931579}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[用户]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ndrs]{lang="EN-US"}**]{#struct_0_18608_20265_x1171038216}**[：]{style="font-family:宋体"}**[表示]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发认证的用户]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_18608_20265_16335069}[：]{style="font-family:宋体"}[表示静态个人用户。]{style="font-family:宋体"}

[**[unclassified-ip]{lang="EN-US"}**]{#struct_0_18608_20265_376708133}[：表示]{style="font-family:宋体"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_796315756}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[个人用户已经上线和正在上线的统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_285698658}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1128029085}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:
宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x668546621}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[ IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x841855669}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_1609998040}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[个人用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[ IPoE]{lang="EN-US"}[个人用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_188593151}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息，]{style="font-family:宋体"}[cpu-number]{lang="EN-US"}[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_684714727}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x174661910}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上已经上线和正在上线的静态和动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber session statistics session-type dhcp interface gigabitethernet 1/0/1 ]{lang="EN-US"}]{#struct_0_18608_20265_x1686598107}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display ipv6 subscriber session statistics]{lang="EN-US"}]{#struct_0_18608_20265_758859070}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2082159063}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_x211002008}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_796119148}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_1659743946}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_1554106074}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1040476500}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_1255442352}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1756939438}

[[处于正在认证状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_83546644}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_x1244511313}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_1542273494}[认证失败]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_x529281163}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_796184684}[认证成功]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1630795508}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_844680626}[成功分配到]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;
  color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_593535687}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_x618390773}[在线]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x1388916140}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_1746523436}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1381813912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_131858894}

::: {#1455198768 .myid}
[]{#_Toc404785865}[]{#struct_0_18608_20265_1716234582}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber subnet-leased**

------------------------------------------------------------------------

[**[display ipv6 subscriber subnet-leased]{lang="EN-US"}**]{#struct_0_18608_20265_795988076}[命令用来显示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x35582827}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_1891997666}

[**[display ipv6 subscriber subnet-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}]{#struct_0_18608_20265_x1627665373}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_x55039624}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber subnet-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_100218529}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_843737803}[模式]{style="font-family:宋体"}

[**[display ipv6 subscriber subnet-leased ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_2137641946}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1693477819}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_458338060}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1367776689}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x602385694}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_x352569314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_462037672}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_796053612}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_430634311}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_x479356372}[：]{style="font-family:宋体;color:black"}[显示指定接口上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x944652857}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1309223005}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:
宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_225185994}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1445941359}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有成员设备上在位单板的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1120188471}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[子网专线用户信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_988662832}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息，]{style="font-family:宋体"}[cpu-number]{lang="EN-US"}[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1376186366}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x2035093364}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网专线用户信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber subnet-leased interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x308856166}

[[Basic:]{lang="EN-US"}]{#struct_0_18608_20265_796905580}

[[  Access interface           : GE1/0/1]{lang="EN-US"}]{#struct_0_18608_20265_x1453181351}

[[  VPN instance               : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1097490737}

[[  Username                   : a]{lang="EN-US"}]{#struct_0_18608_20265_x465123775}

[[  Network                    : 99::/64]{lang="EN-US"}]{#struct_0_18608_20265_x1957921139}

[[  User ID                    : 0x40000001]{lang="EN-US"}]{#struct_0_18608_20265_x1453115815}

[[  State                      : Online]{lang="EN-US"}]{#struct_0_18608_20265_x907297587}

[[  Service node               : Slot 1 CPU 0]{lang="EN-US"}]{#struct_0_18608_20265_2135576201}

[[  Domain                     : radius6]{lang="EN-US"}]{#struct_0_18608_20265_794763143}

[[  Login time                 : May 14 20:22:14 2014]{lang="EN-US"}]{#struct_0_18608_20265_x1562534458}

[[  Online time (hh:mm:ss)     : 00:16:37]{lang="EN-US"}]{#struct_0_18608_20265_x534328893}

[ ]{lang="EN-US"}

[[AAA:]{lang="EN-US"}]{#struct_0_18608_20265_x212950394}

[[  IP pool                    : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x701377781}

[[  Session idle time          : N/A]{lang="EN-US"}]{#struct_0_18608_20265_753946345}

[[  Session duration           : N/A, remaining: N/A]{lang="EN-US"}]{#struct_0_18608_20265_x154570936}

[[  Max multicast addresses    : 4]{lang="EN-US"}]{#struct_0_18608_20265_x1453050279}

[[  Multicast address list     : N/A]{lang="EN-US"}]{#struct_0_18608_20265_x1903726777}

[ ]{lang="EN-US"}

[[QoS:]{lang="EN-US"}]{#struct_0_18608_20265_710451435}

[[  User profile               : h3c6 (active)]{lang="EN-US"}]{#struct_0_18608_20265_x238035918}

[[  Session group profile      : N/A]{lang="EN-US"}]{#struct_0_18608_20265_550148775}

[[  Inbound CAR                : CIR 1000bps PIR 2000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_893546815}

[[  Outbound CAR               : CIR 3000bps PIR 4000bps (active)]{lang="EN-US"}]{#struct_0_18608_20265_97833749}

[ ]{lang="EN-US"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_1095908108}

[[  Uplink   packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1936896686}

[[  DownLink packets/bytes     : 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1569139429}

[ ]{lang="EN-US"}

[[ITA:]{lang="EN-US"}]{#struct_0_18608_20265_x1453640104}

[[  Level-1 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x274907678}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1445677542}

[[  Level-2 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1887632521}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x172454408}

[[  Level-3 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_1515967723}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1161725798}

[[  Level-4 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1166692317}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x295423074}

[[  Level-5 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1453574568}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_556585967}

[[  Level-6 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1340075743}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_504969319}

[[  Level-7 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_284475124}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x2030851115}

[[  Level-8 uplink   packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1239600292}

[[          downLink packets/bytes: 0/0]{lang="EN-US"}]{#struct_0_18608_20265_x1926118282}

[[表1-11 ]{lang="EN-US"}[display ipv6 subscriber subnet-leased]{lang="EN-US"}]{#struct_0_18608_20265_x935100083}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2082779609}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_2081350152}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_443574857}

[[Basic]{lang="EN-US"}]{#struct_0_18608_20265_x1453509032}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1517635331}[会话的基本信息]{style="font-family:宋体"}

[[Access interface]{lang="EN-US"}]{#struct_0_18608_20265_x1453443496}

[[用户所在的接口名称]{style="font-family:宋体"}]{#struct_0_18608_20265_x1575332689}

[[VPN instance]{lang="EN-US"}]{#struct_0_18608_20265_x860481622}

[[用户所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_18608_20265_702060001}[实例，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示用户属于公网]{style="font-family:宋体"}

[[User name]{lang="EN-US"}]{#struct_0_18608_20265_1170182213}

[[用户认证时使用的用户名]{style="font-family:宋体"}]{#struct_0_18608_20265_796971116}

[[Network]{lang="EN-US"}]{#struct_0_18608_20265_1469885974}

[[用户所在的子网地址]{style="font-family:宋体"}]{#struct_0_18608_20265_433887696}

[[User ID]{lang="EN-US"}]{#struct_0_18608_20265_x65661580}

[[用户]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_18608_20265_x1720865853}[，只有用户在线后才会由系统分配，]{style="font-family:宋体"}[0xffffffff]{lang="EN-US"}[表示暂未分配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_18608_20265_x1149876277}

[[用户的认证状态]{style="font-family:宋体"}]{#struct_0_18608_20265_695182863}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_18608_20265_2003124912}[：初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_18608_20265_796381291}[：]{lang="EN-US" style="font-family:宋体"}[正在]{style="font-family:宋体"}[下线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_18608_20265_1535779971}[：认证中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthFail]{lang="EN-US"}]{#struct_0_18608_20265_x638630673}[：认证失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AuthPass]{lang="EN-US"}]{#struct_0_18608_20265_304866007}[：认证通过]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AssignedIP]{lang="EN-US"}]{#struct_0_18608_20265_275200923}[：]{lang="EN-US" style="font-family:宋体"}[会话已具备]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_18608_20265_2125154505}[：用户在线]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Backup]{lang="EN-US"}]{#struct_0_18608_20265_662066322}[：备份状态，表示该用户是由对端备份到本端的]{style="font-family:宋体"}

[[Service node]{lang="EN-US"}]{#struct_0_18608_20265_x1453312424}

[[为用户提供认证服务的节点信息]{style="font-family:宋体"}]{#struct_0_18608_20265_1959735652}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_18608_20265_1529339310}

[[Domain]{lang="EN-US"}]{#struct_0_18608_20265_555693890}

[[用户认证时使用的认证域名]{style="font-family:宋体"}]{#struct_0_18608_20265_1666496477}

[[Login time]{lang="EN-US"}]{#struct_0_18608_20265_x1453246888}

[[用户登录时间]{style="font-family:宋体"}]{#struct_0_18608_20265_1611707693}

[[Online time (hh:mm:ss)]{lang="EN-US"}]{#struct_0_18608_20265_1791138863}

[[用户本次上线的在线时长]{style="font-family:宋体"}]{#struct_0_18608_20265_x937744492}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1453181352}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x694206210}[会话的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[授权信息]{style="font-family:宋体"}

[[IP pool name]{lang="EN-US"}]{#struct_0_18608_20265_x94433607}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1453115816}[授权的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[地址池名称，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[Session idle time]{lang="EN-US"}]{#struct_0_18608_20265_658786354}

[[用户闲置切断时间，单位为秒，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_1573447261}[表示不进行闲置切断]{style="font-family:宋体"}

[[Session duration]{lang="EN-US"}]{#struct_0_18608_20265_x1453050280}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_468205322}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话超时时间，单位为秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_18608_20265_x490541611}[：表示未授权会话时长]{style="font-family:宋体"}

[[Unlimited]{lang="EN-US"}]{#struct_0_18608_20265_x1453640101}[：表示会话时长无限制]{style="font-family:宋体"}

[[remaining]{lang="EN-US"}]{#struct_0_18608_20265_484607209}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x981776986}[授权的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话剩余时长]{style="font-family:宋体"}

[[只在]{style="font-family:宋体"}[Service node]{lang="EN-US"}]{#struct_0_18608_20265_372649547}[上可以查看到有效的剩余时长，非]{style="font-family:宋体"}[Service node]{lang="EN-US"}[上该字段显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[，会话时长无限制该字段显示]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Max multicast addresses]{lang="EN-US"}]{#struct_0_18608_20265_x1453574565}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x559159280}[授权用户可加入的组播组的最大数目]{style="font-family:宋体"}

[[Multicast address list]{lang="EN-US"}]{#struct_0_18608_20265_x103996870}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x1453509029}[授权用户可加入的组播组地址列表，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[未授权该属性]{style="font-family:宋体"}

[[QoS]{lang="EN-US"}]{#struct_0_18608_20265_758185980}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1150800202}[会话的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_18608_20265_x1453443493}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_x815817802}[授权的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称。若未授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_18608_20265_x515422276}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in]{lang="EN-US"}]{#struct_0_18608_20265_x1453377957}[a]{lang="EN-US"}[ctive]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[User Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_483053898}

[[Session group profile]{lang="EN-US"}]{#struct_0_18608_20265_x1453312421}

[[AAA]{lang="EN-US"}]{#struct_0_18608_20265_1200220765}[授权的]{style="font-family:宋体"}[Session ]{lang="EN-US"}[Group Profile]{lang="EN-US"}[名称]{lang="EN-US" style="font-family:宋体"}[。若未授权]{style="font-family:宋体"}[Session ]{lang="EN-US"}[Group Profile]{lang="EN-US"}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[a]{lang="EN-US"}[ctive]{lang="EN-US"}]{#struct_0_18608_20265_507978798}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[in]{lang="EN-US"}]{#struct_0_18608_20265_x1453246885}[a]{lang="EN-US"}[ctive]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[AAA]{lang="EN-US"}[授权]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[失败或者设备上不存在该]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[授权结果未知]{lang="EN-US" style="font-family:宋体"}]{#struct_0_18608_20265_1658761860}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_x19484658}

[[上行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x1453181349}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：上行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：上行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1813822140}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1200022805}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_x1525605852}[：表示上行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_18608_20265_x741194841}

[[下行方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_x513196454}[值（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：下行平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：下行峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[若未授权]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_18608_20265_1813822137}[，则显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[。授权状态包括如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[active]{lang="EN-US"}]{#struct_0_18608_20265_x1199695128}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[inactive]{lang="EN-US"}]{#struct_0_18608_20265_975528281}[：表示下行]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[限速下发失败]{lang="EN-US" style="font-family:宋体"}

[[Flow statistic:]{lang="EN-US"}]{#struct_0_18608_20265_x1453115813}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x100728533}[会话的流量统计信息]{style="font-family:宋体"}

[[Uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_1179489888}

[[上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1453050277}[字节数]{style="font-family:宋体"}

[[Downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x1453388083}

[[下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1319455338}[字节数]{style="font-family:宋体"}

[[ITA]{lang="EN-US"}]{#struct_0_18608_20265_x1453640102}

[[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_887891736}[会话的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[（]{style="font-family:宋体"}[Intelligent Target Accounting]{lang="EN-US"}[，智能靶向计费）业务流量统计信息]{style="font-family:宋体"}

[[Level-*n* uplink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_234591940}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_x1453574566}[的上行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[[downlink packets/bytes]{lang="EN-US"}]{#struct_0_18608_20265_x962443807}

[[计费等级为]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_18608_20265_1516470037}[的下行流量报文数]{style="font-family:宋体"}[/]{lang="EN-US"}[字节数，]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_796971115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[i]{lang="EN-US"}[p]{lang="EN-US"}**]{#struct_0_18608_20265_1469885977}**[v6]{lang="EN-US"}[ subscriber enable]{lang="EN-US"}**

::: {#695560739 .myid}
[]{#_Toc404785866}[]{#struct_0_18608_20265_433691088}

**IPoE \-- IPv6 IPoE配置命令 \-- display ipv6 subscriber subnet-leased statistics**

------------------------------------------------------------------------

[**[display ipv6 subscriber subnet-leased statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x607650105}[命令用来显示已经上线和正在上线的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1718029917}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_18608_20265_2080349386}

[**[display ipv6 subscriber ]{lang="EN-US"}**]{#struct_0_18608_20265_2033728025}**[subnet-leased]{lang="EN-US" style="font-size:9.5pt;font-family:\"Arial\",\"sans-serif\";color:black;background:
#CCE8CC"}[ statistics]{lang="EN-US"}**[ \[ **interface** *[interface-type interface-number]{style="color:black"}* \]]{lang="EN-US"}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_18608_20265_1880075605}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ipv6 subscriber subnet-leased statistics]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_2112011897}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_18608_20265_847217666}[模式：]{style="font-family:宋体"}

[**[display ipv6 subscriber subnet-leased statistics]{lang="EN-US"}**[ \[ **interface** *interface-type interface-number* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1291711913}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_425474379}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x595807591}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_997038924}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1045182907}

[[network-operator]{lang="EN-US"}]{#struct_0_18608_20265_393096761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_16952738}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18608_20265_x1203705055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1476631071}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US" style="color:black"}*]{#struct_0_18608_20265_2129320710}[：]{style="font-family:宋体;color:black"}[显示指定接口上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[IPv4 IPoE]{lang="EN-US"}[子网专线用户已经上线和正在上线的统计]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x1568790853}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x587296669}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）]{style="font-family:
宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_1387788800}*[ slot-number]{lang="SV"}*[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="SV"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[子网专线]{style="font-family:宋体"}[用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟槽位号。如果未指定本参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[ IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[集中式]{style="font-family:宋体"}[IRF]{lang="SV"}[设备]{style="font-family:宋体"}[）（支持]{style="font-family:宋体"}[IRF3]{lang="SV"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_x1200476809}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定成员设备上指定单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_18608_20265_104452665}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[显示指定单板上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="SV"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="SV"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="SV"}*[表示单板]{style="font-family:宋体"}[/PEX]{lang="SV"}[所在的槽位号。如果未指定本参数，将显示所有单板上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[ IPoE]{lang="EN-US"}[子网专线用户统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_18608_20265_1468064917}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[子网专线用户统计信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示单板上的]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1626809911}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x853259189}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上已经上线和正在上线的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 subscriber ]{lang="EN-US"}]{#struct_0_18608_20265_393162297}**[subnet-leased]{lang="EN-US" style="font-size:9.5pt;font-family:\"Courier New\";color:black;
background:#CCE8CC;font-weight:normal"}**[ statistics interface gigabitethernet 1/0/1 ]{lang="EN-US"}

[Total                : 100]{lang="EN-US"}

[Init                 : 0]{lang="EN-US"}

[Authenticating       : 20]{lang="EN-US"}

[Authenticate fail    : 0]{lang="EN-US"}

[Authenticate pass    : 20]{lang="EN-US"}

[Assigned IP          : 10]{lang="EN-US"}

[Online               : 50]{lang="EN-US"}

[Backup               : 0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display ipv6 subscriber ]{lang="EN-US"}]{#struct_0_18608_20265_x1151863274}**[subnet-leased]{lang="EN-US" style="font-size:9.5pt;font-family:\"Arial\",\"sans-serif\";color:black;
background:#CCE8CC;font-weight:normal"}**[ statistics]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2106208063}[[字段]{style="font-family:黑体"}]{#struct_0_18608_20265_622329254}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18608_20265_x348192941}

[[Total]{lang="EN-US"}]{#struct_0_18608_20265_x1672599663}

[[接入的总用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x1965055450}

[[Init]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_466745383}

[[处于初始状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_900439326}

[[Authenticating]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1155583352}

[[处于正在认证状态的用户数]{style="font-family:宋体"}]{#struct_0_18608_20265_x266811750}

[[Authenticate fail]{lang="EN-US"}]{#struct_0_18608_20265_1185715806}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_392965689}[认证失败]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Authenticate pass]{lang="EN-US"}]{#struct_0_18608_20265_2002207329}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_2039444726}[认证成功]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Assigned IP ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_1900951220}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_2082248540}[成功分配到]{style="font-family:宋体;color:black"}[IP]{lang="EN-US" style="color:black"}[地址]{style="font-family:宋体;
  color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Online ]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x809318957}

[[处于]{style="font-family:宋体"}]{#struct_0_18608_20265_1688638942}[在线]{style="font-family:宋体;color:black"}[状态]{style="font-family:宋体"}[的用户数]{style="font-family:宋体;color:black"}

[[Backup]{lang="EN-US" style="color:black"}]{#struct_0_18608_20265_x2093755821}

[[处于备份状态的用户数]{style="font-family:宋体;color:black"}]{#struct_0_18608_20265_31940988}

**[ ]{lang="EN-US"}**

::: {#-873786769 .myid}
[]{#_Toc404785867}[]{#struct_0_18608_20265_393031225}[]{#_Toc345424002}[]{#_Toc345404980}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber 8021p**

------------------------------------------------------------------------

[**[ipv6 subscriber 8021p]{lang="EN-US"}**]{#struct_0_18608_20265_1543304555}[命令用于配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[中的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[**[undo ipv6 subscriber 8021p]{lang="EN-US"}**]{#struct_0_18608_20265_x158371441}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2118812271}

[**[ipv6 subscriber 8021p]{lang="EN-US"}**[ *8021p-list* **domain** *domain-name*]{lang="EN-US"}]{#struct_0_18608_20265_x153071138}

[**[undo ipv6 subscriber 8021p]{lang="EN-US"}***[ 8021p-list]{lang="EN-US"}*]{#struct_0_18608_20265_253132043}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_18608_20265_1443833}

[[未指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x139673738}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[中的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1845405843}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_532910527}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1787610343}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_230586155}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1577683713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_392834617}

[*[8021p-list]{lang="SV"}*]{#struct_0_18608_20265_2029666754}[：]{style="font-family:宋体;color:black"} [802.1p]{lang="SV"}[值]{style="font-family:宋体"}[列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示一个或多个]{style="font-family:宋体"}[802.1p]{lang="SV"}[值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:宋体"}*[8021p-list]{lang="SV"}*[ = { *8021p-value* \[ **to** *8021p-value* \] }&\<1-8\>]{lang="SV"}[，]{style="font-family:宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[8021p-value]{lang="SV"}*[为指定]{style="font-family:宋体"}*[8021p]{lang="SV"}*[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="SV"}[～]{style="font-family:宋体"}[7]{lang="SV"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1755594352}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[8021p]{lang="SV"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_899305980}

[[本命令用来配置指定]{style="font-family:宋体;color:windowtext"}]{#struct_0_18608_20265_28072131}[802.1p]{lang="EN-US" style="color:windowtext"}[值范围内的]{style="font-family:宋体;
color:windowtext"}[IPv6]{lang="EN-US" style="color:windowtext"}[未知源]{style="font-family:宋体;color:windowtext"}[IP]{lang="EN-US" style="color:windowtext"}[接入用户认证时使用的认证域，通过指定的认证域进行认证授权。]{style="font-family:宋体;color:windowtext"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x117858513}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x625969160}[在子接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1.100]{lang="EN-US"}[上配置内层]{style="font-family:宋体"}[VLAN TAG]{lang="EN-US"}[中]{style="font-family:宋体"}[802.1p]{lang="SV"}[值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[2]{lang="SV"}[到]{style="font-family:宋体"}[5]{lang="SV"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="SV"}[接入]{style="font-family:
宋体"}[用户认证使用的]{style="font-family:宋体"}[认证]{style="font-family:
宋体"}[域为]{style="font-family:宋体"}[1pdm]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_823008045}

[\[Sysname\] interface gigabitethernet 1/0/1.100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ipv6 subscriber service-identify 8021p second-vlan]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ipv6 subscriber 8021p 2 to 5 domain ]{lang="EN-US"}[1pdm]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x451662167}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_1490553239}
:::

::: {#1901206888 .myid}
[]{#_Toc404785868}[]{#struct_0_18608_20265_x1240597960}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber dhcp domain**

------------------------------------------------------------------------

[**[ipv6 subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_x876509297}[命令用来配置]{style="font-family:
宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用的认证域。]{style="font-family:
宋体"}

[**[undo ipv6 subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_x1492391690}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_392900153}

[**[ipv6 subscriber dhcp domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_1272029174}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber dhcp domain**]{lang="EN-US"}]{#struct_0_18608_20265_x705291367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_919692628}

[[IPv6 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1157652684}[个人接入用户的认证域为缺省认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x753648735}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1000761439}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1114234334}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1069471696}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1170814998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1452024199}

[*[domain-name]{lang="SV"}*]{#struct_0_18608_20265_x685641788}[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_150518222}

[[本命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x522044778}[报文触发接入的]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户在认证时使用的域名，该域名必须在接入设备上存在且配置完整。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[ipv6 subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_392703545}[命令后，如果用户报文中携带]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[，]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[内容符合域名的格式要求，并且接口配置了]{style="font-family:宋体"}**[ipv6 subscriber trust option16]{lang="EN-US"}**[命令]{style="font-family:宋体"}[，则]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接入用户使用]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[作为指定的认证域进行认证；否则，使用本命令指定的认证域。]{style="font-family:宋体"}

[[如果不配置]{style="font-family:宋体"}**[ipv6 subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_689163656}[命令，且]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中未携带]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[，则使用缺省认证域认证。]{style="font-family:宋体"}

[[当用户需要将]{style="font-family:宋体"}[Option 16]{lang="EN-US"}]{#struct_0_18608_20265_x1642323150}[字段中的信息按字符串形式解析时，请确保]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[字段内容中不出现字符串结束字符和不可见字符，否则在生成域名时将产生异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_2076957192}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x492474821}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用的认证域为]{style="font-family:宋体"}[ipoe]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_x201328493}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber dhcp domain ipoe]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x308505118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_x693880757}**[v6]{lang="EN-US"}[ subscriber initiator dhcp enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_1956193957}**[v6]{lang="EN-US"}[ subscriber ]{lang="EN-US"}[dhcp username]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_x534525501}
:::

::: {#198764963 .myid}
[]{#_Toc404785869}[]{#struct_0_18608_20265_x1779841242}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber dhcp max-session**

------------------------------------------------------------------------

[**[ipv6 subscriber dhcp max-session]{lang="EN-US"}**]{#struct_0_18608_20265_1786252176}[命令用来配置接口上允许]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的最大数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber dhcp max-session**]{lang="EN-US"}]{#struct_0_18608_20265_x958296448}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1941648961}

[**[ipv6 subscriber dhcp]{lang="EN-US"}**[ **max-session** *max-number*]{lang="EN-US"}]{#struct_0_18608_20265_736290918}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber dhcp** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_392769081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1702089825}

[[未限制接口上允许]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x10603267}[报文触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_31328069}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x18342946}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1694307507}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_662162794}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1522245781}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1313068616}

[*[max-number]{lang="EN-US"}*]{#struct_0_18608_20265_x2094159364}[：[允许]{style="color:black"}]{style="font-family:宋体"}[DHCPv6]{lang="EN-US" style="color:black"}[触发]{style="font-family:宋体;
color:black"}[创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1973698649}

[[DHCPv6]{lang="SV"}]{#struct_0_18608_20265_2072134902}[报文触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话数目]{style="font-family:宋体"}[达到最大值后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[后续]{style="font-family:宋体"}[DHCPv6]{lang="SV"}[报文不能触发创建]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x987235695}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x794129594}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上允许]{style="font-family:宋体"}[DHCPv6]{lang="SV" style="color:black"}[报文]{style="font-family:宋体;color:black"}[触发创建的]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[最大数为]{style="font-family:宋体"}[100]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_393621049}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber dhcp max-session 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1964110754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_793680207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1563826732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1954737637}
:::

::: {#-110208790 .myid}
[]{#_Toc404785870}[]{#struct_0_18608_20265_x927538872}[]{#_Toc403480424}[]{#_Toc401341513}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber dhcp password option16**

------------------------------------------------------------------------

[**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_x1357928940}[命令用来配置]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[**[undo ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_x1231340895}[命令用来取消]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x599790941}

[**[ipv6 subscriber dhcp password option16 ]{lang="EN-US"}**[\[ **offset** *offset* \] \[ **length** *length* \]]{lang="EN-US"}]{#struct_0_18608_20265_x123001269}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber dhcp password option16**]{lang="EN-US"}]{#struct_0_18608_20265_x1934658291}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1488321211}

[[IPv6 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1171909681}[个人接入用户未使用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[作为认证密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1313348213}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1440524833}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x959811386}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x2017821062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x975002230}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1233065262}

[**[offset ]{lang="EN-US"}***[offset]{lang="EN-US"}*]{#struct_0_18608_20265_x1240562144}[：表示从]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[首部偏移指定字节后的内容作为认证密码，]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[表示字节偏移量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，单位为字节。如果未指定本参数，将从]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[中起始处后的内容作为认证密码。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *length*]{lang="EN-US"}]{#struct_0_18608_20265_1890044418}[：表示从]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[所处的位置开始，取指定长度的字节作为认证密码，]{style="font-family:宋体"}*[length]{lang="EN-US"}*[表示获取字节的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，单位为字节。如果未指定本参数，将从]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[所处的位置开始取剩余的所有内容作为认证密码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1067068184}

[[本命令用来配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1781772012}[报文触发接入的]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户在认证时使用的认证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_974884313}[命令后，]{lang="EN-US" style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户认证密码的选择情况如下：]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x748687923}[报文中携带的]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[可用（]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[内容为可见字符，]{lang="EN-US" style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[126]{lang="EN-US"}[），则使用]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[中的指定范围的]{lang="EN-US" style="font-family:宋体"}[Option]{lang="EN-US"}[内容作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[如果]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1515664762}[报文中未携带]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[，或者]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[内容不符合可见字符的格式要求（可见字符，]{lang="EN-US" style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[126]{lang="EN-US"}[），但同时配置了]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令，则使用]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令配置的密码；否则使用缺省字符串]{lang="EN-US" style="font-family:宋体"}[vlan]{lang="EN-US"}[作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未配置]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_890338770}[命令，但是配置了]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令，则使用]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令配置的密码；否则使用缺省字符串]{lang="EN-US" style="font-family:宋体"}[vlan]{lang="EN-US"}[作为认证密码。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18608_20265_x1643846671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在配置了信任]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1351191125}[报文中的]{lang="EN-US" style="font-family:宋体"}[Option 16]{lang="EN-US"}[的情况下，配置的]{lang="EN-US" style="font-family:宋体"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**[命令才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户需要将]{style="font-family:宋体"}]{#struct_0_18608_20265_x672777151}[Option 16]{lang="EN-US"}[字段中的信息作为认证密码时，请确保]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[字段内容中不出现字符串结束字符和不可见字符（可见字符，]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码数值范围]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[126]{lang="EN-US"}[），否则在生成用户密码时将产生异常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1434695253}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x170450279}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用从]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[首部偏移]{style="font-family:宋体"}[10]{lang="EN-US"}[个字节后的]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节内容作为认证密码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x695139708}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber dhcp password option16 offset 10 length 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x70906834}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x614230703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x77762730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_x1108063801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x2014434229}
:::

::: {#1177171376 .myid}
[]{#_Toc404785871}[]{#struct_0_18608_20265_x145823957}[]{#_Toc345423998}[]{#_Toc345404976}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber dhcp username**

------------------------------------------------------------------------

[**[ipv6 subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_1996987698}[命令用于配置]{style="font-family:
宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户的认证用户名。]{style="font-family:
宋体"}

[**[undo ipv6 subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x295515094}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x210467872}

[**[ipv6 subscriber dhcp username include]{lang="EN-US"}**[ { **circuit-id** \| **client-id** \| **nas-port-id** \| **port** \[ *separator* \] \| **remote-id** \| **second-vlan** \[ *separator* \] \| **slot** \[ *separator* \] \| **source-mac** \[ **separator** *separator* \] \| **subslot** \[ *separator* \] \| **sysname** \[ *separator* \] \| **vendor-class** \| **vendor-specific \| vlan** \[ *separator* \] } \*]{lang="EN-US"}]{#struct_0_18608_20265_1810843453}

[**[undo ipv6 subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_885827151}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_928172610}

[[IPv6 DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1475378767}[个人接入用户使用报文源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为认证用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x599748528}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_393686585}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x724843483}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x577282124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x196089072}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_803736523}

[**[circuit-id]{lang="EN-US"}**]{#struct_0_18608_20265_905570299}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[IPv6 DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Interface Identifier Option]{lang="SV"}[（]{style="font-family:宋体"}[Option18]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息为用户名。]{style="font-family:宋体"}

[**[client-id]{lang="SV"}**]{#struct_0_18608_20265_774461835}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以]{style="font-family:宋体;color:black"}[IPv6 [DHCP]{style="color:black"}]{lang="SV"}[报文中的]{style="font-family:宋体;color:black"}[Client Identifier Option]{lang="SV" style="color:black"}[（]{style="font-family:宋体;color:black"}[Option1]{lang="SV" style="color:black"}[）字段中的信息作为用户名。]{style="font-family:宋体;
color:black"}

[**[nas-port-id]{lang="SV"}**]{#struct_0_18608_20265_1094700542}[：]{style="font-family:宋体"}[表示以用户认证报文中的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="SV"}[属性作为用户名。]{style="font-family:宋体"}

[**[port]{lang="SV"}**]{#struct_0_18608_20265_x524830022}[：]{style="font-family:宋体"}[表示以报文接入的端口号作为用户名。]{style="font-family:宋体"}

[**[remote-id]{lang="SV"}**]{#struct_0_18608_20265_x1638442928}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[IPv6 DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Remote Identifier Option]{lang="SV"}[（]{style="font-family:宋体"}[Option37]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息作为用户名。]{style="font-family:宋体"}

[**[second-vlan]{lang="SV"}**]{#struct_0_18608_20265_1431485121}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x2147103342}[：]{style="font-family:宋体"}[表示以报文接入的槽位号作为用户名。]{style="font-family:宋体"}

[**[source-mac]{lang="SV"}**]{#struct_0_18608_20265_1420969556}[：]{style="font-family:宋体;color:black"}[表示以用户报文的源]{style="font-family:宋体;
color:black"}[MAC]{lang="SV" style="color:black"}[地址作为用户名。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="SV"}**]{#struct_0_18608_20265_x744403919}*[separator]{lang="SV"}*[：]{style="font-family:
宋体"}[MAC]{lang="SV"}[地址分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以为任意可配置的可见字符。若指定了分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="SV"}["，]{style="font-family:
宋体"}[则用户名形如]{style="font-family:宋体"}[xxxx-xxxx-xxxx]{lang="SV"}[；]{style="font-family:宋体"}[若不指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则用户名为]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="SV"}[形式。]{style="font-family:宋体"}

[**[subslot]{lang="SV"}**]{#struct_0_18608_20265_x769933794}[：]{style="font-family:宋体"}[表示以报文接入的子卡号作为用户名。]{style="font-family:宋体"}

[**[sysname]{lang="SV"}**]{#struct_0_18608_20265_1315274624}[：]{style="font-family:宋体"}[表示以报文接入设备的设备名作为用户名。]{style="font-family:宋体"}

[**[vendor-class]{lang="SV"}**]{#struct_0_18608_20265_1163435187}[：]{style="font-family:宋体"}[表示以]{style="font-family:宋体"}[IPv6 DHCP]{lang="SV"}[报文中的]{style="font-family:宋体"}[Vendor Class Option]{lang="SV"}[（]{style="font-family:宋体"}[Option16]{lang="SV"}[）]{style="font-family:宋体"}[字段中的信息作为用户名。]{style="font-family:宋体"}

[**[vendor-specific]{lang="SV"}**]{#struct_0_18608_20265_x2131518889}[：]{lang="EN-US" style="font-family:宋体"}[表示以]{lang="EN-US" style="font-family:
宋体"}[IPv6 DHCP]{lang="SV"}[报文中的]{lang="EN-US" style="font-family:
宋体"}[Vendor Specific Option]{lang="SV"}[（]{lang="EN-US" style="font-family:宋体"}[Option]{lang="SV"}[17]{lang="SV"}[）]{lang="EN-US" style="font-family:宋体"}[字段中的信息作为用户名。]{lang="EN-US" style="font-family:
宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_901437393}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[*[separator]{lang="SV"}*]{#struct_0_18608_20265_x1802254974}[：]{style="font-family:宋体"}[当前字段分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[用在当前字段后面以连接后面的一个字段]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以为任意可配置的可见字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1795683749}

[[该命令用来配置]{style="font-family:宋体"}]{#struct_0_18608_20265_393096760}[IPv6 DHCP]{lang="SV"}[接入]{style="font-family:宋体"}[用户在认证时使用的用户名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[该用户名必须与认证服务器上配置的用户名保持一致。此类用户进行]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[认证时使用的密码由]{style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[在允许的用户名类型范围内，该命令支持任意形式、任意顺序的用户名组合。例如：若配置]{style="font-family:宋体"}**[ipv6 subscriber dhcp username include vendor-class vendor-specific]{lang="EN-US"}**]{#struct_0_18608_20265_16952737}[，则用户名为]{style="font-family:宋体"}[Option16]{lang="SV"}[字段内容和]{style="font-family:宋体"}[Option17]{lang="SV"}[字段内容的拼接，且两个字段之间无分隔符。]{style="font-family:宋体"}

[[当用户需要将]{style="font-family:宋体"}[Option]{lang="EN-US"}]{#struct_0_18608_20265_x865998047}[字段中的信息按字符串形式解析时，请确保]{style="font-family:宋体"}[Option]{lang="EN-US"}[字段内容中不出现字符串结束符和不可见字符，否则可能生成错误的用户名。]{style="font-family:宋体"}

[[建议不要使用]{style="font-family:宋体"}]{#struct_0_18608_20265_x962646582}[@]{lang="SV"}[作为分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[避免携带]{style="font-family:宋体"}[@]{lang="SV"}[字符的用户名在]{style="font-family:
宋体"}[AAA]{lang="SV"}[服务器端不能被正确解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_89947341}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x470934494}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上]{style="font-family:宋体"}[IPv6 DHCP]{lang="EN-US"}[个人接入用户使用]{style="font-family:宋体"}[Client Identifier Option]{lang="EN-US"}[字段]{style="font-family:宋体"}[中的信息作为用户名]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_1180357977}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber dhcp username include client-id]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2105158299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_176999499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_1683301655}
:::

::: {#-1522414806 .myid}
[]{#_Toc345423999}[]{#_Toc345404977}[]{#_Toc404785872}[]{#struct_0_18608_20265_1448274994}[]{#_Toc345424003}[]{#_Toc345404981}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber dscp**

------------------------------------------------------------------------

[**[ipv6 subscriber dscp]{lang="EN-US"}**]{#struct_0_18608_20265_1550807459}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值与用户认证域的映射关系。]{style="font-family:宋体"}

[**[undo ipv6 subscriber dscp]{lang="EN-US"}**]{#struct_0_18608_20265_1307177936}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x524844645}

[**[ipv6 subscriber dscp]{lang="EN-US"}***[ dscp-value-list]{lang="EN-US"}*[ **domain** *domain-name*]{lang="EN-US"}]{#struct_0_18608_20265_393162296}

[**[undo ipv6 subscriber dscp]{lang="EN-US"}***[ dscp-value-list]{lang="EN-US"}*]{#struct_0_18608_20265_x1151863273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1025613781}

[[未指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1105096329}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x720114632}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x649908631}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_620934795}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_272851862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x860435369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1821468753}

[*[dscp-value-list]{lang="EN-US"}*]{#struct_0_18608_20265_x1923885009}[：]{style="font-family:宋体;
color:black"}[DSCP]{lang="SV"}[值]{style="font-family:宋体"}[列表，表示一个或多个]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的值，表示方式为]{style="font-family:宋体"}*[dscp-value-list]{lang="EN-US"}*[ ={ *dscp-value* \[ **to** *dscp-value* \] }&\<1-8\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[dscp-value]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_x1379533040}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[DSCP]{lang="SV"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1345149343}

[[本命令用来配置指定]{style="font-family:宋体;color:windowtext"}]{#struct_0_18608_20265_994598190}[DSCP]{lang="EN-US" style="color:windowtext"}[范围内的]{style="font-family:宋体;
color:windowtext"}[IPv6]{lang="EN-US" style="color:windowtext"}[未知源]{style="font-family:宋体;color:windowtext"}[IP]{lang="EN-US" style="color:windowtext"}[报文触发的用户认证时使用的认证域，通过指定的认证域进行认证授权。]{style="font-family:宋体;color:windowtext"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_392965688}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_2002207330}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值范围为]{style="font-family:宋体"}[1]{lang="SV"}[到]{style="font-family:
宋体"}[4]{lang="SV"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="SV"}[接入]{style="font-family:宋体"}[用户认证使用的]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域为]{style="font-family:宋体"}[dscpdm]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_2040034551}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber service-identify dscp]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber dscp 1 to 4 domain ]{lang="EN-US"}[dscpdm]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1868012306}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x994134028}
:::

::: {#616245893 .myid}
[]{#_Toc404785873}[]{#struct_0_18608_20265_x2123499508}[]{#_Toc345423991}[]{#_Toc345404969}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber enable**

------------------------------------------------------------------------

[**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1846976361}[命令用来在接口上使能]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[功能并指定用户的接入模式。]{style="font-family:宋体"}

[**[undo ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_516943846}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x538665350}

[**[ipv6 subscriber ]{lang="EN-US"}**[{ **l2-connected** \| **routed** } **enable**]{lang="EN-US"}]{#struct_0_18608_20265_x1702847534}

[**[undo ipv6 subscriber ]{lang="EN-US"}**[{ **l2-connected** \| **routed** } **enable**]{lang="EN-US"}]{#struct_0_18608_20265_x87458015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x993328539}

[[接口上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1570078481}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_393031224}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1543304554}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x158436977}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1763129068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1390224245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_603990879}

[**[l2-connected]{lang="EN-US"}**]{#struct_0_18608_20265_293707020}[：指定二层接入模式，表示]{style="font-family:宋体;color:black"}[此接口上用户通过二层网络接入。]{style="font-family:宋体;color:black"}

[**[rout]{lang="SV"}[ed]{lang="EN-US"}**]{#struct_0_18608_20265_1963526298}[：指定三层接入模式，表示]{style="font-family:宋体;color:black"}[此接口上用户通过三层网络接入。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1239019820}

[[只有在接口上使能了]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1139942287}[功能后，其它的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[相关配置才能生效。]{style="font-family:宋体"}

[[不允许直接修改]{style="font-family:宋体"}[IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x673962674}[的接入模式，必须关闭]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[功能之后，重新使能]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[功能时指定新的接入模式。]{style="font-family:宋体"}

[[在聚合接口视图下使能]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1431485117}[功能时，必须同时通过]{style="font-family:宋体"}**[service slot]{lang="EN-US"}**[命令指定聚合接口下流量的业务处理板；否则会产生无法统计用户流量的现象。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_2093476886}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x312396322}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能二层接入模式的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_240892788}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber l2-connected enable]{lang="EN-US"}
:::

::: {#1429398263 .myid}
[]{#_Toc404785874}[]{#struct_0_18608_20265_392834616}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber initiator dhcp enable**

------------------------------------------------------------------------

[**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_2029666753}[命令用来在接口上使能]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[**[undo ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_1755922032}[命令用来关闭接口上]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x291816780}

[**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1901195289}

[**[undo ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1192433925}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1532171043}

[[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1821220964}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_874591268}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x449612473}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1139464101}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1951673381}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x289749242}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1792011060}

[[接口上使能该功能后，收到的首个]{style="font-family:宋体"}[DHCP Solicit]{lang="EN-US"}]{#struct_0_18608_20265_392900152}[报文或直接申请地址的]{style="font-family:宋体"}[DHCP Request]{lang="EN-US"}[报文会触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话；关闭该功能后，该接口上收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，已有的由]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文触发生成的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话不会被删除。]{style="font-family:宋体"}

[[接口上可同时配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1272029175}[报文、]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[和未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x705356903}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1712773718}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1564825871}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber initiator dhcp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1417300820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1734296534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x243366740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1355131569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1082447645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1686103128}
:::

::: {#-583562010 .myid}
[]{#_Toc404785875}[]{#struct_0_18608_20265_507323934}[]{#_Toc369161220}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber initiator ndrs enable**

------------------------------------------------------------------------

[**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x553121074}[命令用来在接口上使能]{style="font-family:宋体"}[IPV6 ND RS]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[**[undo ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1973912217}[命令用来关闭接口上]{style="font-family:宋体"}[IPV6 ND RS]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_392703544}

[**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_689163657}

[**[undo ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1642323149}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1008090987}

[[RS]{lang="EN-US"}]{#struct_0_18608_20265_438355626}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x803124274}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1353989306}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1523507131}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1043743070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x329269730}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1373575718}

[[接口上使能该功能后，收到的首个]{style="font-family:宋体"}[IPV6 ND RS]{lang="EN-US"}]{#struct_0_18608_20265_x1751346634}[报文会触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话；关闭该功能后，该接口上收到的]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，已有的由]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[报文触发生成的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话不会被删除。]{style="font-family:宋体"}

[[接口上可同时配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1779823578}[报文、]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[和未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1080731808}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_392769080}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1702089824}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber initiator ndrs enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1555480674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_2141332619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x2083631749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_331011697}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1922177599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_957410551}
:::

::: {#-227485159 .myid}
[]{#_Toc404785876}[]{#struct_0_18608_20265_x1646219073}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber initiator unclassified-ip enable**

------------------------------------------------------------------------

[**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_1179146115}[命令用来在接口上使能未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[**[undo ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1266880373}[命令用来关闭接口上的未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_791640556}

[**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_255740038}

[**[undo ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x1438181109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_393621048}

[[未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1964110753}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_390395680}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_417792887}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1831568928}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1244297265}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x97661051}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x190119232}

[[接口使能该功能后，收到的未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x370734034}[报文会触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话；关闭该功能后，该接口上收到的未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文不能触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，已有的由未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话不会被删除。]{style="font-family:宋体"}

[[接口上可同时配置]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1873663249}[报文、]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[和未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x501110436}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1027870497}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发生成]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x97186400}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_393686584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x724843482}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_x577347660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_624773438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x413773098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1929868536}
:::

::: {#492771131 .myid}
[]{#_Toc404785877}[]{#struct_0_18608_20265_x1107699791}[]{#_Toc345423996}[]{#_Toc345404974}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber interface-leased**

------------------------------------------------------------------------

[**[ipv6 subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_x234647214}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber interface-leased**]{lang="EN-US"}]{#struct_0_18608_20265_881034499}[命令用来删除已配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[接口专线用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_88404354}

[**[ipv6 subscriber interface-leased username]{lang="EN-US"}**[ *name* **password** { **ciphertext** \| **plaintext** } *password* \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_x1858808051}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber interface-leased**]{lang="EN-US"}]{#struct_0_18608_20265_801769205}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1164784955}

[[未配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_2051286492}[接口专线用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_393096759}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1557025366}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_645653767}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x68888957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1681779409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1252872482}

[**[username]{lang="SV"}**]{#struct_0_18608_20265_x534161715}*[ name]{lang="SV"}*[：指定用户认证时使用的用户名，其中]{style="font-family:宋体;color:black"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1\~255]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[password]{lang="SV"}**]{#struct_0_18608_20265_521366899}[：指定用户认证时使用的密码。]{style="font-family:宋体;color:black"}

[**[ciphertext]{lang="SV"}**]{#struct_0_18608_20265_x1851680330}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以密文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[plaintext]{lang="SV"}**]{#struct_0_18608_20265_x1856089734}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以明文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_1322352597}[：]{style="font-family:宋体;color:black"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1826626866}*[ domain-name]{lang="SV"}*[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[如果未配置该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将使用缺省]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的]{style="font-family:宋体"} ["]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_2069908066}

[[一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_436904228}[接口专线用户代表了该接口接入的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户，接口上接入的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户统一认证、授权和计费。该]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[专线用户认证成功后，接口上接入的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户流量均允许通过，且共享一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，并基于接口进行授权和计费。]{style="font-family:宋体"}

[[每个接口只能配置一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_393162295}[接口专线用户。]{style="font-family:宋体"}

[[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_x1151863276}[IPoE]{lang="SV"}[个人接入用户]{style="font-family:宋体"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接口专线用户和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1785128668}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x817638784}[在]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一个]{style="font-family:宋体"}[IPv6 ]{lang="SV"}[IPoE]{lang="EN-US"}[接口专线用户]{style="font-family:宋体"}[：]{style="font-family:宋体"}[认证使用的用户名为]{style="font-family:宋体"}[intuser]{lang="SV"}[，认证使用的密码为明文]{style="font-family:宋体"}[pw123]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x285837377}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber interface-leased username ]{lang="EN-US"}[intuser ]{lang="SV"}[password plaintext pw123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_828220220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber interface-leased]{lang="EN-US"}**]{#struct_0_18608_20265_1350215687}
:::

::: {#-527644849 .myid}
[]{#_Toc404785878}[]{#struct_0_18608_20265_x2071994812}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber nas-port-id format**

------------------------------------------------------------------------

[**[ipv6 subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_x104294400}[命令用于为]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入用户配置]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性封装格式，即在]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入用户进行认证时，接入设备向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性的封装格式。]{style="font-family:宋体"}

[**[undo ipv6 subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_x1448033492}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1348680582}

[**[ipv6 subscriber nas-port-id format cn-telecom]{lang="EN-US"}**[ { **version1.0** \| **version2.0** } ]{lang="EN-US"}]{#struct_0_18608_20265_x524641903}

[**[undo ipv6 subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_x1535674828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2044766146}

[[按]{style="font-family:宋体"}[version 1.0]{lang="EN-US"}]{#struct_0_18608_20265_392965687}[的格式要求填充发往]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性内容。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_2002207343}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_2039837940}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2045728315}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1123544142}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x363831091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_2024969834}

[**[version1.0]{lang="EN-US"}**]{#struct_0_18608_20265_1250312070}[：填充格式为]{style="font-family:宋体"}[version 1.0]{lang="EN-US"}[，表示发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性以电信]{style="font-family:宋体"}[163]{lang="EN-US"}[大后台要求的格式填充。]{style="font-family:宋体"}

[**[version2.0]{lang="EN-US"}**]{#struct_0_18608_20265_x1113703427}[：填充格式为]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[，表示发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性以]{style="font-family:宋体"}[YDT 2275-2011]{lang="EN-US"}[宽带接入用户线路（端口）标识要求的格式填充。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1101701174}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[version 1.0]{lang="EN-US"}]{#struct_0_18608_20265_1524421696}[封装格式：]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网接口和三层聚合接口]{style="font-family:宋体"}]{#struct_0_18608_20265_x1966495745}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=0;]{lang="EN-US"}]{#struct_0_18608_20265_x315306416}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网子接口和三层聚合子接口（携带单层]{style="font-family:宋体"}]{#struct_0_18608_20265_x641549453}[VLAN Tag]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=*vlan_id*;]{lang="EN-US"}]{#struct_0_18608_20265_393031223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层以太网子接口和三层聚合子接口（携带双层]{style="font-family:宋体"}]{#struct_0_18608_20265_1543304557}[VLAN Tag]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[ slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vlanid=*inner-vlan*;vlanid2=*outer-vlan*;]{lang="EN-US"}]{#struct_0_18608_20265_x158502513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基于]{style="font-family:宋体"}]{#struct_0_18608_20265_1796606261}[ATM]{lang="EN-US"}[链路的三层虚拟以太网接口（]{style="font-family:宋体"}[IPoEoA]{lang="EN-US"}[接入）]{style="font-family:宋体"}

[[slot=*slot_num*;subslot=*subslot_num*;port=*port_num*;vpi=*vpi*;vci=*vci*;]{lang="EN-US"}]{#struct_0_18608_20265_728318362}

[[其中，]{style="font-family:宋体"}*[slot_num]{lang="EN-US"}*]{#struct_0_18608_20265_550824244}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的槽位号；]{style="font-family:宋体"}*[subslot_num]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的子槽位号；]{style="font-family:宋体"}*[port_num]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的端口号；]{style="font-family:宋体"}*[vlan_id]{lang="EN-US"}*[表示接入用户的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[inner-vlan]{lang="EN-US"}*[表示接入用户的内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[outer-vlan]{lang="EN-US"}*[表示接入用户的外层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}*[vpi]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的]{style="font-family:宋体"}[VPI]{lang="EN-US"}[；]{style="font-family:宋体"}*[vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的]{style="font-family:宋体"}[VCI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[version 2.0]{lang="EN-US"}]{#struct_0_18608_20265_x1561253395}[封装格式：]{lang="EN-US" style="font-family:宋体"}

[[{eth\|trunk\|atm} NAS_slot/NAS_subslot/NAS_port:svlan.cvlan AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port]{lang="EN-US"}]{#struct_0_18608_20265_981981625}

[[其中，]{style="font-family:宋体"}[{eth\|trunk\|atm}]{lang="EN-US"}]{#struct_0_18608_20265_694881518}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的类型，包括以太接口、]{style="font-family:宋体"}[trunk]{lang="EN-US"}[类型的以太网接口或]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口；]{style="font-family:宋体"}[NAS_slot]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的槽位号；]{style="font-family:宋体"}[NAS_subslot]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的子槽位号；]{style="font-family:宋体"}[NAS_port]{lang="EN-US"}[表示]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[接入接口的端口号；]{style="font-family:宋体"}[svlan]{lang="EN-US"}[表示接入用户的]{style="font-family:宋体"}[SVLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}[cvlan]{lang="EN-US"}[表示接入用户的]{style="font-family:宋体"}[CVLAN ID]{lang="EN-US"}[；]{style="font-family:宋体"}[AccessNodeIdentifier]{lang="EN-US"}[表示接入节点的标识；]{style="font-family:宋体"}[ANI_rack]{lang="EN-US"}[表示接入节点机架号；]{style="font-family:宋体"}[ANI_frame]{lang="EN-US"}[表示接入节点机框号；]{style="font-family:宋体"}[ANI_slot]{lang="EN-US"}[表示接入节点槽位号；]{style="font-family:宋体"}[ANI_subslot]{lang="EN-US"}[表示接入节点子槽位号；]{style="font-family:宋体"}[ANI_port]{lang="EN-US"}[表示接入节点端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x975058560}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x417964863}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性封装格式为]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_1624745320}

[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_1647826347}

[[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber nas-port-id format cn-telecom version2.0]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_x1861515473}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_392834615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_2029666756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_1755725424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_876535206}
:::

::: {#1611823104 .myid}
[]{#_Toc404785879}[]{#struct_0_18608_20265_437999341}[]{#_Toc369161242}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber nas-port-id nasinfo-insert**

------------------------------------------------------------------------

[**[ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x608922795}[命令用于配置在提取出的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[内容中插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息，并使用插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息后的内容作为]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_460589207}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x835181499}

[**[ipv6 subscriber nas-port-id]{lang="EN-US"}**[ **nasinfo-insert** ]{lang="EN-US"}]{#struct_0_18608_20265_343698798}

[**[undo ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x2108772951}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_18608_20265_8675801}

[[如果收到的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1145483648}[报文带有]{style="font-family:宋体"}[Option18]{lang="EN-US"}[选项，则直接使用该选项的内容作为]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性字符串。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1598959949}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1868559419}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_392900151}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1272029176}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x705422439}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x265746386}

[[在]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_1307696401}[中继组网环境下，接入设备能捕获用户的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文，并从报文中提取出]{style="font-family:宋体"}[DHCPv6 Option18]{lang="EN-US"}[选项信息。在配置了]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性封装格式为]{style="font-family:宋体"}[version 2.0]{lang="EN-US"}[且且信任]{style="font-family:宋体"}[DHCP Option 18]{lang="EN-US"}[的情况下，如果配置了本命令，则接入设备处理如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果收到的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_1065880798}[报文带有]{lang="EN-US" style="font-family:宋体"}[Option18]{lang="EN-US"}[，则从收到的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中解析]{lang="EN-US" style="font-family:宋体"}[Option18]{lang="EN-US"}[，并按]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式要求在原有的选项内容里插入]{lang="EN-US" style="font-family:宋体"}[NAS]{lang="EN-US"}[信息（该信息标识了用户在本设备上的接入位置信息），然后将其作为]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性内容。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果收到的]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1281273141}[报文不带]{lang="EN-US" style="font-family:宋体"}[Option18]{lang="EN-US"}[，则按]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}[格式要求封装，填充]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性中的]{lang="EN-US" style="font-family:宋体"}[NAS]{lang="EN-US"}[信息字段（]{lang="EN-US" style="font-family:宋体"}[NAS_slot/NAS_subslot/NAS_port:svlan.cvlan]{lang="EN-US"}[），并将]{lang="EN-US" style="font-family:宋体"}[AccessNodeIdentifier/ANI_rack/ANI_frame/ANI_slot/ANI_subslot/ANI_port]{lang="EN-US"}[部分修改为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[/]{lang="EN-US"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[本功能对原]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x542621657}[报文中]{style="font-family:宋体"}[Option18]{lang="EN-US"}[选项不产生任何影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1013745199}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x939826546}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备使用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端上报的]{style="font-family:宋体"}[Option18]{lang="EN-US"}[信息，并在其中插入]{style="font-family:宋体"}[NAS]{lang="EN-US"}[信息，然后将其封装为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1314653731}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber nas-port-id format cn-telecom version2.0]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber trust option18]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x235519961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x294645069}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_392703543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_689163658}
:::

::: {#-986486859 .myid}
[]{#_Toc404785880}[]{#struct_0_18608_20265_x1642323152}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber nas-port-type**

------------------------------------------------------------------------

[**[ipv6 subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_x1055210690}[命]{style="font-size:
10.0pt;font-family:宋体;color:black"}[令用来配置接口的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入端口类型]{style="font-family:宋体"}[。]{style="font-size:10.0pt;font-family:宋体;color:black"}

[**[undo ipv6 subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_1361527244}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1339130722}

[**[ipv6 subscriber nas-port-type]{lang="EN-US"}**[ { **802.11** \| **adsl-cap** \| **adsl-dmt** \| **async** \| **cable** \| **ethernet** \| **g.3-fax** \| **hdlc** \| **idsl** \| **isdn-async-v110** \| **isdn-async-v120** \| **isdn-sync** \| **piafs** \| **sdsl** \| **sync** \| **virtual** \| **wireless-other** \| **x.25** \| **x.75** \| **xdsl** }]{lang="EN-US"}]{#struct_0_18608_20265_x422439686}

[**[undo ipv6 subscriber nas-port-type]{lang="EN-US"}**]{#struct_0_18608_20265_1850546899}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x40605483}

[[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_776323819}[接入端口类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_611816756}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1950571484}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1280487387}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x892873529}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_392769079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1872833431}

[**[802.11]{lang="SV"}**]{#struct_0_18608_20265_x1653888869}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[符合]{style="font-family:宋体"}[Wireless-IEEE 802.11]{lang="EN-US"}[标准的接口类型，对应的编码值为]{style="font-family:宋体"}[19]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[adsl-cap]{lang="SV"}**]{#struct_0_18608_20265_1736972434}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ADSL-CAP]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Carrierless Amplitude Phase Modulation]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[adsl-dmt]{lang="SV"}**]{#struct_0_18608_20265_x1743454934}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ADSL-DMT]{lang="EN-US"}[（]{style="font-family:宋体"}[Asymmetric DSL]{lang="EN-US"}[，]{style="font-family:宋体"}[Discrete Multi-Tone]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[13]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[async]{lang="SV"}**]{#struct_0_18608_20265_1864777533}[：]{style="font-family:宋体;color:black"}[Async]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cable]{lang="SV"}**]{#struct_0_18608_20265_364676011}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Cable]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[17]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ethernet]{lang="SV"}**]{#struct_0_18608_20265_1613511541}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Ethernet]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[g.3-fax]{lang="SV"}**]{#struct_0_18608_20265_1372229602}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[G.3 Fax]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hdlc]{lang="SV"}**]{#struct_0_18608_20265_649862102}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[HDLC]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[idsl]{lang="SV"}**]{#struct_0_18608_20265_1692321125}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[IDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[ISDN Digital Subscriber Line]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[14]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v110]{lang="SV"}**]{#struct_0_18608_20265_x1528896462}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ISDN Async V.110]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-async-v120]{lang="SV"}**]{#struct_0_18608_20265_343505293}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[ISDN Async V.120]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isdn-sync]{lang="SV"}**]{#struct_0_18608_20265_x1187252788}[：]{style="font-family:宋体"}[ISDN Sync]{lang="EN-US"}[口类型，对应的编码值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[piafs]{lang="SV"}**]{#struct_0_18608_20265_393621047}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[符合]{style="font-family:宋体"}[PIAFS]{lang="EN-US"}[（]{style="font-family:宋体"}[PHS]{lang="EN-US"}[（]{style="font-family:宋体"}[Personal Handyphone System]{lang="EN-US"}[）]{style="font-family:宋体"}[Internet Access Forum Standard]{lang="EN-US"}[）标准的接口类型，对应的编码值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdsl]{lang="SV"}**]{#struct_0_18608_20265_x1964110764}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[SDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Symmetric DSL]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sync]{lang="SV"}**]{#struct_0_18608_20265_793876815}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Sync]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[virtual]{lang="SV"}**]{#struct_0_18608_20265_562012069}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[Virtual]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[wireless-other]{lang="SV"}**]{#struct_0_18608_20265_1893147331}[：]{style="font-family:宋体"}[Wireless-other]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[18]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.25]{lang="SV"}**]{#struct_0_18608_20265_566283560}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[X.25]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[x.75]{lang="SV"}**]{#struct_0_18608_20265_x1172338586}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[X.75]{lang="EN-US"}[接口类型，对应的编码值为]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[xdsl]{lang="SV"}**]{#struct_0_18608_20265_13713595}[：]{style="font-size:12.0pt;font-family:宋体;color:black"}[XDSL]{lang="EN-US"}[（]{style="font-family:宋体"}[Digital Subscriber Line of unknown type]{lang="EN-US"}[）接口类型，对应的编码值为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1610871846}

[[此处配置的端口接入类型]{style="font-family:宋体"}]{#struct_0_18608_20265_x742490564}[值将作为向]{style="font-family:宋体"}[RADIUS]{lang="FR"}[服务器发送的]{style="font-family:宋体"}[RADIUS]{lang="FR"}[请求报文的]{style="font-family:宋体"}[NAS-Port-Type]{lang="FR"}[属性值]{style="font-family:宋体"}[，用于]{style="font-family:宋体"}[向]{style="font-family:宋体"}[RADIUS]{lang="FR"}[服务器正确传递用户的接入端口信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_104862035}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x2054798449}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IPOE]{lang="EN-US"}[接入端口类型为]{style="font-family:宋体"}[SDSL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}]{#struct_0_18608_20265_x1724684206}[Sysname]{lang="SV"}[\> system-view]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="SV"}[\] ]{lang="EN-US"}[interface ]{lang="SV"}[gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="SV"}[GigabitEthernet1/0/1]{lang="EN-US"}[\] ipv6 subscriber nas-port-type sdsl]{lang="SV"}
:::

::: {#2116741287 .myid}
[]{#_Toc404785881}[]{#struct_0_18608_20265_x1735742908}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber ndrs domain**

------------------------------------------------------------------------

[**[ipv6 subscriber ndrs domain]{lang="EN-US"}**]{#struct_0_18608_20265_393686583}[命令用来配置]{style="font-family:
宋体"}[IPv6 ND RS]{lang="EN-US"}[个人接入用户使用的认证域。]{style="font-family:
宋体"}

[**[undo ipv6 subscriber ndrs domain]{lang="EN-US"}**]{#struct_0_18608_20265_x724843481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x577413196}

[**[ipv6 subscriber ndrs domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_1387362082}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber ndrs domain**]{lang="EN-US"}]{#struct_0_18608_20265_2084998743}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_594986188}

[[IPv6 ND RS]{lang="EN-US"}]{#struct_0_18608_20265_1323083261}[个人接入用户使用缺省认证域作为认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x931360329}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x414195148}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1369821209}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1076027035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_518563241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1575518723}

[*[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_994370371}[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="EN-US" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_393096758}

[[本命令用来配置]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}]{#struct_0_18608_20265_x1557025367}[报文触发接入的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入用户在认证时使用的域名，该域名必须与认证服务器上配置的域名保持一致。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[ipv6 subscriber ndrs domain]{lang="EN-US"}**]{#struct_0_18608_20265_x2083229588}[命令后，对于]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[报文触发认证的]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接入用户使用本命令指定的域名进行认证，否则使用缺省认证域认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1874316519}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_580606369}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[接入用户使用的认证域为]{style="font-family:宋体"}[ipoe]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x838361518}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber ndrs domain ipoe]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1206742424}

[**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_x291882411}
:::

::: {#-2089230011 .myid}
[]{#_Toc404785882}[]{#struct_0_18608_20265_2009152882}[]{#_Toc369161223}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber ndrs max-session**

------------------------------------------------------------------------

[**[ipv6 subscriber ndrs max-session]{lang="EN-US"}**]{#struct_0_18608_20265_1995976154}[命令用来配置接口上允许]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的最大数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber ndrs max-session**]{lang="EN-US"}]{#struct_0_18608_20265_x553303871}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x375614353}

[**[ipv6 subscriber ndrs]{lang="EN-US"}**[ **max-session** *max-number* ]{lang="EN-US"}]{#struct_0_18608_20265_1241306416}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber ndrs** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_393162294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1151863275}

[[未限制接口上允许创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x2106554101}[会话数目]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x10522235}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1741358981}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x193861432}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x2108640753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_763908864}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2108120976}

[*[max-number]{lang="EN-US"}*]{#struct_0_18608_20265_x1115181427}[：[允许]{style="color:black"}]{style="font-family:宋体"}[RS]{lang="EN-US" style="color:black"}[触发]{style="font-family:宋体;color:black"}[创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1958633500}

[[RS]{lang="EN-US"}]{#struct_0_18608_20265_x1169793985}[报文触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话数目达到最大值后，后续]{style="font-family:宋体"}[RS]{lang="EN-US"}[报文不能触发创建]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文、未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文等触发创建]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话不会受此最大值限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_727588099}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_392965686}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上允许]{style="font-family:宋体"}[RS]{lang="EN-US" style="color:black"}[报文]{style="font-family:宋体;color:black"}[触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话最大数为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_2002207344}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber ndrs max-session 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_2040296692}

[**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1469744262}

[**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_489957339}

[**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_137946611}
:::

::: {#-386972605 .myid}
[]{#_Toc404785883}[]{#struct_0_18608_20265_x1399590876}[]{#_Toc349553662}[]{#_Toc349553663}[]{#_Toc349553664}[]{#_Toc349553665}[]{#_Toc349553666}[]{#_Toc349553667}[]{#_Toc349553668}[]{#_Toc349553669}[]{#_Toc349553670}[]{#_Toc349553671}[]{#_Toc349553672}[]{#_Toc349553673}[]{#_Toc349553674}[]{#_Toc349553675}[]{#_Toc349553676}[]{#_Toc349553677}[]{#_Toc349553678}[]{#_Toc349553679}[]{#_Toc349553680}[]{#_Toc349553681}[]{#_Toc349553682}[]{#_Toc349553683}[]{#_Toc349553684}[]{#_Toc349553685}[]{#_Toc349553686}[]{#_Toc349553687}[]{#_Toc349553688}[]{#_Toc349553689}[]{#_Toc349553690}[]{#_Toc349553691}[]{#_Toc349553692}[]{#_Toc349553693}[]{#_Toc349553694}[]{#_Toc349553695}[]{#_Toc349553696}[]{#_Toc349553697}[]{#_Toc349553698}[]{#_Toc349553699}[]{#_Toc349553700}[]{#_Toc349553701}[]{#_Toc349553702}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber ndrs username**

------------------------------------------------------------------------

[**[ipv6 subscriber ndrs username]{lang="EN-US"}**]{#struct_0_18608_20265_731076940}[命令用来配置]{style="font-family:
宋体"}[IPv6 ND RS]{lang="EN-US"}[接入用户的认证用户名。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber ndrs username**]{lang="EN-US"}]{#struct_0_18608_20265_1564810007}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1358671165}

[**[ipv6 subscriber ndrs username include ]{lang="EN-US"}**[{ **nas-port-id** \| **port** \[ *separator* \] \| **second-vlan** \[ *separator* \] \| **slot** \[ *separator* \] \| **source-mac** \[ **separator** *separator* \] \| **subslot** \[ *separator* \] \| **sysname** \[ *separator* \] \| **vlan** \[ *separator* \] } \*]{lang="EN-US"}]{#struct_0_18608_20265_1809832960}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber ndrs username**]{lang="EN-US"}]{#struct_0_18608_20265_393031222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1543304556}

[[IPv6 ND RS]{lang="EN-US"}]{#struct_0_18608_20265_x158568049}[接入用户采用[用户报文的]{style="color:black"}源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为认证用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1736939334}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_979452977}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1456251717}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1315303569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1312589197}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_622933192}

[**[nas-port-id]{lang="EN-US"}**]{#struct_0_18608_20265_x1157133739}[：表示使用用户的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性作为用户名。]{style="font-family:宋体"}

[**[port]{lang="SV"}**]{#struct_0_18608_20265_x1716471107}[：]{style="font-family:宋体"}[表示以报文接入的端口号作为用户名。]{style="font-family:宋体"}

[**[s]{lang="EN-US"}**]{#struct_0_18608_20265_x773990945}**[econd-vlan]{lang="SV"}**[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_763429599}[：]{style="font-family:宋体"}[表示以报文接入的槽位号作为用户名。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**]{#struct_0_18608_20265_653345837}[：表示使用用户报文的]{style="font-family:宋体;color:black"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为用户名[。]{style="color:black"}]{style="font-family:宋体"}

[**[separator ]{lang="EN-US"}***[separator]{lang="EN-US"}*]{#struct_0_18608_20265_x1328702590}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址分隔符，可以为任意可配置的可见字符。若指定了分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="SV"}["，]{style="font-family:
宋体"}[则用户名形如]{style="font-family:宋体"}[xxxx-xxxx-xxxx]{lang="SV"}[；]{style="font-family:宋体"}[若不指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则用户名为]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="SV"}[形式。]{style="font-family:宋体"}

[**[subslot]{lang="SV"}**]{#struct_0_18608_20265_x1716471106}[：]{style="font-family:宋体"}[表示以报文接入的子卡号作为用户名。]{style="font-family:宋体"}

[**[sysname]{lang="SV"}**]{#struct_0_18608_20265_1954892410}[：]{style="font-family:宋体"}[表示以报文接入设备的设备名作为用户名。]{style="font-family:宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_636304082}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[*[separator]{lang="SV"}*]{#struct_0_18608_20265_2077963849}[：]{style="font-family:宋体"}[当前字段分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[用在当前字段后面以连接后面的一个字段]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以为任意可配置的可见字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1057900957}

[[本命令用来配置]{style="font-family:宋体"}[IPv6 RS]{lang="EN-US"}]{#struct_0_18608_20265_x2133996461}[报文触发接入的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入用户在认证时使用的用户名，该用户名必须与认证服务器上配置的用户名保持一致。此类用户进行]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[认证时使用的密码由]{style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[在允许的用户名类型范围内，该命令支持任意形式、任意顺序的用户名组合。例如：若配置]{style="font-family:宋体"}**[ipv6 subscriber ndrs username include nas-port-id source-mac]{lang="EN-US"}**]{#struct_0_18608_20265_392834614}[，则用户名为]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性字段]{style="font-family:宋体"}[和]{style="font-family:宋体"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[字段内容的拼接，且两个字段之间无分隔符]{style="font-family:宋体"}

[[建议不要使用]{style="font-family:宋体"}]{#struct_0_18608_20265_x1365472359}[@]{lang="SV"}[作为分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[避免携带]{style="font-family:宋体"}[@]{lang="SV"}[字符的用户名在]{style="font-family:
宋体"}[AAA]{lang="SV"}[服务器端不能被正确解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_2029666755}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1755528816}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6 ND RS]{lang="EN-US"}[接入用户使用[用户报文的]{style="color:black"}源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址作为用户名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x301872828}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber ndrs username include source-mac]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1486293170}

[**[ipv6 subscriber initiator ndrs enable]{lang="EN-US"}**]{#struct_0_18608_20265_2117075738}

[**[ipv6 subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x1763027336}
:::

::: {#2125303927 .myid}
[]{#_Toc352071428}[]{#_Toc404785884}[]{#struct_0_18608_20265_575970273}[]{#_Toc345424004}[]{#_Toc345404982}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber password**

------------------------------------------------------------------------

[**[ipv6 subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_x2145637510}[命令用来配置动态]{style="font-family:
宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户的认证密码。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber password**]{lang="EN-US"}]{#struct_0_18608_20265_x1166952989}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x912446842}

[**[ipv6 subscriber password ]{lang="EN-US"}**[{ **ciphertext** \| **plaintext** } *password*]{lang="EN-US"}]{#struct_0_18608_20265_938720215}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber password**]{lang="EN-US"}]{#struct_0_18608_20265_392900150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1272029177}

[[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x705487975}[个人接入用户的认证密码为字符串]{style="font-family:宋体"}[vlan]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_176901945}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1757684627}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1982812768}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x936669894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1954091801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1071100022}

[**[ciphertext]{lang="EN-US"}**]{#struct_0_18608_20265_695416038}[：表示]{style="font-family:宋体;color:black"}[以密文方式配置用户的认证密码。]{style="font-family:宋体"}

[**[plaintext]{lang="EN-US"}**]{#struct_0_18608_20265_x1324742861}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;color:black"}[以明文方式配置用户的认证密码。]{style="font-family:宋体"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_x2060186981}[：]{style="font-family:宋体"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1596595896}

[[如果接口上同时配置了]{style="font-family:宋体"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_1931299779}[命令和]{style="font-family:宋体"}**[ipv6 subscriber password]{lang="EN-US"}**[命令，则优先使用]{style="font-family:宋体"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**[命令获取的字符串作为认证密码。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_392703542}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_689163659}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[个人接入用户认证时使用的密码为明文的]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1642323151}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber password plaintext 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x651926163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber dhcp username]{lang="EN-US"}**]{#struct_0_18608_20265_x978307255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_1976125738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber unclassified-ip username]{lang="EN-US"}**]{#struct_0_18608_20265_x207187272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber dhcp password option16]{lang="EN-US"}**]{#struct_0_18608_20265_1488059067}
:::

::: {#-1359081096 .myid}
[]{#_Toc404785885}[]{#struct_0_18608_20265_96358059}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber service-identify**

------------------------------------------------------------------------

[**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_1047772999}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的业务识别方式。]{style="font-family:宋体"}

[**[undo ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x1509270984}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_118916695}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_35479694}[三层聚合口视图]{style="font-family:宋体"}

[**[ipv6 subscriber service-identify]{lang="EN-US"}**[ **dscp**]{lang="EN-US"}]{#struct_0_18608_20265_x1914352317}

[**[undo]{lang="EN-US"}**[ **ip subscriber service-identify**]{lang="EN-US"}]{#struct_0_18608_20265_392769078}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1872833432}[三层聚合子接口视图]{style="font-family:宋体"}

[**[ipv6 subscriber service-identify]{lang="EN-US"}**[ { **8021p** { **second-vlan** \| **vlan** } \| **dscp** \| **second-vlan** \| **vlan** }]{lang="EN-US"}]{#struct_0_18608_20265_x1654085477}

[**[undo]{lang="EN-US"}**[ **ip subscriber service-identify**]{lang="EN-US"}]{#struct_0_18608_20265_x1237480735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_1638901308}

[[未指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_677355352}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的业务识别方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1466272597}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x900907717}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_528764825}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1591950753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x682674298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_271718304}

[**[8021p second-vlan]{lang="SV"}**]{#struct_0_18608_20265_393621046}[：表示]{style="font-family:宋体;color:black"}[QinQ]{lang="SV" style="font-size:
10.0pt;color:black"}[模式下基于内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[中的]{style="font-size:10.0pt;font-family:宋体;
color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;color:black"}[值]{style="font-size:10.0pt;font-family:宋体;color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[8021p vlan]{lang="SV"}**]{#struct_0_18608_20265_x1964110763}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-size:10.0pt;
font-family:宋体;color:black"}[VLAN ]{lang="SV" style="font-size:10.0pt;
color:black"}[Tag]{lang="SV"}[中的]{style="font-size:10.0pt;
font-family:宋体;color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;
color:black"}[值]{style="font-size:10.0pt;font-family:宋体;
color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[，]{style="font-size:10.0pt;font-family:宋体;color:black"}[QinQ]{lang="SV"}[模式下基于外层]{style="font-family:宋体"}[V]{lang="SV"}[LAN ]{lang="SV" style="font-size:10.0pt;color:black"}[Tag]{lang="SV"}[中的]{style="font-size:10.0pt;font-family:宋体;color:black"}[802.1p]{lang="SV" style="font-size:10.0pt;color:black"}[值]{style="font-size:10.0pt;
font-family:宋体;color:black"}[识别业务]{style="font-size:10.0pt;font-family:
宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[dscp]{lang="SV"}**]{#struct_0_18608_20265_390592288}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-family:宋体;
color:black"}[DSCP]{lang="SV" style="color:black"}[值识别业务。]{style="font-family:宋体;color:black"}

[**[second-vlan]{lang="SV"}**]{#struct_0_18608_20265_x1624887021}[：]{style="font-family:宋体;color:black"}[QinQ]{lang="SV" style="font-size:10.0pt;
color:black"}[模式]{style="font-size:10.0pt;font-family:宋体;
color:black"}[下基于内层]{style="font-family:宋体"}[VLAN ID]{lang="SV"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_497292866}[：表示]{style="font-family:宋体;color:black"}[基于]{style="font-size:10.0pt;
font-family:宋体;color:black"}[VLAN ID]{lang="SV" style="font-size:10.0pt;
color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;
color:black"}[，]{style="font-size:10.0pt;font-family:宋体;
color:black"}[Qin]{lang="SV" style="font-size:10.0pt;color:black"}[Q]{lang="SV"}[模式下基于外层]{style="font-family:宋体"}[V]{lang="SV"}[LAN ID]{lang="SV" style="font-size:10.0pt;color:black"}[识别业务]{style="font-size:10.0pt;font-family:宋体;color:black"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x266110495}

[[对于未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_31137978}[用户认证时使用的认证域由报文中携带的业务信息来决定。不同的业务特征可以对应不同的认证域，每一个接口可以指定仅识别某种类型业务的报文。例如，接口上若指定了基于]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值识别业务，且通过]{style="font-family:宋体"}**[ipv6 subscriber dscp 1 domain aabcc]{lang="EN-US"}**[命令指定了]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值]{style="font-family:宋体"}[1]{lang="EN-US"}[与认证域]{style="font-family:
宋体"}[aabbcc]{lang="EN-US"}[的映射关系，则]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}[1]{lang="EN-US"}[的用户认证时将会使用认证域]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一个接口上只能指定一个业务识别方式。]{style="font-family:宋体"}]{#struct_0_18608_20265_x1694537276}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_162745798}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_1095810760}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户认证使用[基于]{style="color:black"}]{style="font-family:宋体"}[DSCP]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;
color:black"}[业务识别方式]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x856336469}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber service-identify dscp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1228458356}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_393686582}**[v6]{lang="EN-US"}[ subscriber 8021p]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_x724843480}**[v6]{lang="EN-US"}[ subscriber dscp]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_x577478732}**[v6]{lang="EN-US"}[ subscriber vlan]{lang="EN-US"}**
:::

::: {#1551584135 .myid}
[]{#_Toc404785886}[]{#struct_0_18608_20265_1463180713}[]{#_Toc345423995}[]{#_Toc345404973}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber session static**

------------------------------------------------------------------------

[**[ipv6 subscriber session static]{lang="EN-US"}**]{#struct_0_18608_20265_1688753070}[命令用来配置静态]{style="font-family:
宋体"}[IPv6 ]{lang="SV"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[**[undo ipv6 subscriber session static]{lang="EN-US"}**]{#struct_0_18608_20265_259719790}[命令用来删除指定的静态]{style="font-family:宋体"}[IPv6 ]{lang="SV"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_2006827109}

[**[ipv6 subscriber session static ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \[ **second-vlan** *vlan-id* \] \] \[ **mac** *mac-address* \] \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_x2106624974}

[**[undo ipv6 subscriber session static ipv6 ]{lang="EN-US"}***[ipv6-address ]{lang="EN-US"}*[\[ **vlan** *vlan-id* \[ **second-vlan** *vlan-id* \] \]]{lang="EN-US"}]{#struct_0_18608_20265_x1745369835}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1159330750}

[[未配置静态]{style="font-family:宋体"}]{#struct_0_18608_20265_2001545976}[IPv6 ]{lang="SV"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1415995028}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_393096765}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_16952742}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1664672930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1072827028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_933985032}

[**[ipv6]{lang="EN-US"}**]{#struct_0_18608_20265_356135853}**[ ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:
宋体;color:black"}[用户的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="SV"}[地址。]{lang="EN-US" style="font-family:宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_x264919535}*[ vlan-id]{lang="SV"}*[：表示用户报文的外层]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[。其中]{style="font-family:宋体;color:black"}*[vlan-id]{lang="SV"}*[表示]{style="font-family:宋体"}[VLAN ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:
宋体"}

[**[second-vlan]{lang="SV"}**]{#struct_0_18608_20265_179695979}*[ vlan-id]{lang="SV"}*[：表示用户报文的内层]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[。其中]{style="font-family:宋体;color:black"}*[vlan-id]{lang="SV"}*[表示]{style="font-family:宋体"}[VLAN ID]{lang="SV"}[，取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:
宋体"}

[**[mac]{lang="SV"}**]{#struct_0_18608_20265_x430293479}*[ mac-address]{lang="SV"}*[：]{style="font-family:宋体"}[表示]{style="font-family:宋体;color:black"}[用户的]{style="font-family:宋体"}[MAC]{lang="SV" style="color:black"}[地址，]{style="font-family:宋体;color:black"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体;color:black"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_2136168069}*[ domain-name]{lang="SV"}*[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。如果未指定该参数，将使用缺省认证域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的]{style="font-family:宋体"} ["]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1421192459}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18608_20265_2054151708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令的]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**]{#struct_0_18608_20265_710321044}[和]{lang="EN-US" style="font-family:宋体"}**[second-vlan]{lang="EN-US"}**[参数仅子接口支持，非子接口不支持。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[静态]{style="font-family:宋体"}]{#struct_0_18608_20265_393162301}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[的匹配优先级高于动态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。若已经存在静态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，则与之匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文不会触发新的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话；若存在一个未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文触发建立的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，则再配置一个能与该未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文匹配的静态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话，会覆盖已经存在的动态]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="SV" style="font-size:10.0pt;font-family:Symbol"}[系统支持配置多个静态]{style="font-family:宋体"}]{#struct_0_18608_20265_x12746379}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[相同]{style="font-family:宋体"}]{#struct_0_18608_20265_948330288}[IP]{lang="SV"}[、外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[、内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[的静态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[只能存在一条]{style="font-family:宋体"}[，]{style="font-family:宋体"}[后配置的不能覆盖已配置的。若要修改相关参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[必须删除当前配置后重新配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_79801455}[静态]{style="font-family:宋体"}[IPoE]{lang="SV"}[会话、接口专线用户和子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x346575369}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x1832602784}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一条静态]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话：]{style="font-family:宋体"}[用户]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址为]{style="font-family:宋体"}[2000::1]{lang="SV"}[，]{style="font-family:宋体"}[认证使用的认证域为]{style="font-family:宋体"}[dm1]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_570313254}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber session static ipv6 2000::1 domain dm1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1416898956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1871992584}
:::

::: {#566247494 .myid}
[]{#_Toc404785887}[]{#struct_0_18608_20265_1912823879}[]{#_Toc345423997}[]{#_Toc345404975}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber subnet-leased**

------------------------------------------------------------------------

[**[ipv6 subscriber subnet-leased ]{lang="EN-US"}**]{#struct_0_18608_20265_190817873}[命令用来配置]{style="font-family:
宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户。]{style="font-family:
宋体"}

[**[undo ipv6 subscriber subnet-leased ]{lang="EN-US"}**]{#struct_0_18608_20265_x1608791902}[命令用来删除指定的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[子网专线用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2000116903}

[**[ipv6 subscriber subnet-leased ipv6 ]{lang="EN-US"}***[ipv6-address prefix-length]{lang="EN-US"}*[ **username** *name* **password** { **ciphertext** \| **plaintext** } *password* \[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18608_20265_467163078}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber subnet-leased ipv6** *ipv6-address prefix-length*]{lang="EN-US"}]{#struct_0_18608_20265_392965693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x336444821}

[[未配置]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_1375735849}[子网专线用户。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1064267141}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_306747326}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x604657247}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1216917640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_2081610824}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1261136689}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_18608_20265_x1938223289}[：表示用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_18608_20265_1479534121}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[子网前]{style="font-family:宋体"}[缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[username]{lang="SV"}**]{#struct_0_18608_20265_1792149198}*[ name]{lang="SV"}*[：指定用户认证时使用的用户名，其中]{style="font-family:宋体;color:black"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写]{style="font-family:
宋体"}[。]{style="font-family:宋体;color:black"}

[**[password]{lang="SV"}**]{#struct_0_18608_20265_x2107031791}[：指定用户认证时使用的密码。]{style="font-family:宋体;color:black"}

[**[ciphertext]{lang="SV"}**]{#struct_0_18608_20265_177095044}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以密文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[plaintext]{lang="SV"}**]{#struct_0_18608_20265_393031229}[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;
color:black"}[以明文方式配置用户认证使用的密码]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[*[password]{lang="SV"}*]{#struct_0_18608_20265_1543304567}[：]{style="font-family:宋体;color:black"}[设置的明文密码或密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。密文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[117]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[；]{style="font-family:宋体"}[明文密码为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[63]{lang="SV"}[个字符的字符串。]{style="font-family:
宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_x158502514}*[ domain-name]{lang="SV"}*[：指定认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[如果未配置该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[将使用缺省]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[域来认证用户。关于缺省认证域的相关配置请参见"安全配置指导"中的]{style="font-family:宋体"} ["]{style="font-family:宋体"}[AAA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1796933941}

[[一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_384956856}[子网专线用户代表了该接口接入的所有该子网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户，该子网内的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户统一认证、授权和计费。该]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[专线用户认证成功后，接口上接入的所有该子网内]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户流量均允许通过，且共享一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，并基于子网进行授权和计费。]{style="font-family:宋体"}

[[每个子网只能配置一个]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x1186144113}[子网专线用户。]{style="font-family:宋体"}

[[同一接口下，]{style="font-family:宋体"}]{#struct_0_18608_20265_232936128}[IPoE]{lang="SV"}[个人接入用户]{style="font-family:宋体"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[接口专线用户和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[子网专线用户的配置互斥，只能选择其中的一种配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x177431713}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x632713757}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置一个]{style="font-family:宋体"}[IPv6 ]{lang="SV"}[IPoE]{lang="EN-US"}[子网专线用户：用户]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀为]{style="font-family:宋体"}[2001:10::100/64]{lang="EN-US"}[，认证使用的用户名为]{style="font-family:宋体"}[netuser]{lang="EN-US"}[，认证使用的密码为明文]{style="font-family:宋体"}[pw123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_703616851}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber subnet-leased ipv6 2001:10::100 64 username netuser password plaintext pw123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_427991119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber subnet-leased]{lang="EN-US"}**]{#struct_0_18608_20265_1180674583}
:::

::: {#1491800085 .myid}
[]{#_Toc404785888}[]{#struct_0_18608_20265_1392724388}[]{#_Toc345424007}[]{#_Toc345404985}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber timer quiet**

------------------------------------------------------------------------

[**[ipv6 subscriber timer quiet]{lang="EN-US"}**]{#struct_0_18608_20265_392834621}[命令用来配置]{style="font-family:
宋体"}[IPv6 IPoE]{lang="EN-US"}[用户的静默时间。]{style="font-family:
宋体"}

[**[undo ipv6 subscriber timer quiet]{lang="EN-US"}**]{#struct_0_18608_20265_x691322424}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1745108139}

[**[ipv6 subscriber timer quiet]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_18608_20265_1884612751}

[**[undo ipv6 subscriber timer quiet]{lang="EN-US"}**]{#struct_0_18608_20265_309431797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1204435872}

[[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_548471500}[用户的静默时间功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1277579748}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_563733923}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1116326797}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1916084960}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_704763799}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1096883686}

[*[time]{lang="EN-US"}*]{#struct_0_18608_20265_575927673}[：]{style="font-family:宋体;color:black"}[IPoE]{lang="EN-US" style="color:black"}[用户的静默时间，]{style="font-family:宋体;color:black"}[取值范围为]{style="font-family:
宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x191407957}

[[本命令用来设置用户认证失败以后，设备需要等待的时间间隔。在静默期间，设备不对来自认证失败用户的报文进行认证处理，直接丢弃，可以防止该类用户报文持续发送给服务器认证而对设备性能造成影响。静默期后，如果设备再次收到该用户的报文，则依然可以对其进行认证处理。]{style="font-family:宋体"}]{#struct_0_18608_20265_392900157}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1272029170}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x705553511}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上配置]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户的静默时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_115244198}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber timer quiet 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1679511558}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_x813577835}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x794409192}
:::

::: {#1220284466 .myid}
[]{#_Toc404785889}[]{#struct_0_18608_20265_x1831007046}[]{#_Toc369161240}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber trust**

------------------------------------------------------------------------

[**[ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_1336554370}[命令用于配置信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的指定]{style="font-family:宋体"}[Option]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ipv6 subscriber trust]{lang="EN-US"}**]{#struct_0_18608_20265_1324696071}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1829156255}

[**[ipv6 subscriber trust ]{lang="EN-US"}**[{ **option16** \| **option18** \| **option37** }]{lang="EN-US"}]{#struct_0_18608_20265_x1428893076}

[**[undo ipv6 subscriber trust ]{lang="EN-US"}**[{ **option16** I **option18** \| **option37** }]{lang="EN-US"}]{#struct_0_18608_20265_x689274644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_392703549}

[[不信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_689163668}[报文中的任何]{style="font-family:宋体"}[Option]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1078666032}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_493547620}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_1297618790}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_913421210}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_3152923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x129910982}

[**[option16]{lang="EN-US"}**]{#struct_0_18608_20265_1521744384}[：表示信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[option18]{lang="EN-US"}**]{#struct_0_18608_20265_332333509}[：表示信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option18]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[option37]{lang="EN-US"}**]{#struct_0_18608_20265_265145653}[：表示信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option37]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1739432594}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1207138971}[组网环境中，接入设备可以提取用户]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[信息。如果接入设备信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[信息，则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{style="font-family:宋体"}[Option 16]{lang="EN-US"}]{#struct_0_18608_20265_817586369}[内容有效（无非法字符]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[等），且没有域名分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}[字符的情况下，]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用整个]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[的内容作为指定的认证域进行认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在]{style="font-family:宋体"}[Option 16]{lang="EN-US"}]{#struct_0_18608_20265_594789420}[内容中包含了域名分隔符]{style="font-family:宋体"}[@]{lang="EN-US"}[字符，且]{style="font-family:宋体"}[@]{lang="EN-US"}[字符后的字符串有效（无非法字符]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[等）的情况下，]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[@]{lang="EN-US"}[字符之后的字符串作为指定的认证域进行认证。如果在]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[内容中包括多个]{style="font-family:宋体"}[@]{lang="EN-US"}[字符，则使用最后一个]{style="font-family:宋体"}[@]{lang="EN-US"}[字符之后的字符串作为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户的认证域名。]{style="font-family:宋体"}

[[如果接入设备不信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1926734082}[报文中的]{style="font-family:宋体"}[Option 16]{lang="EN-US"}[信息，但是接口上配置了]{style="font-family:宋体"}**[ipv6 subscriber dhcp domain]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用该命令指定的认证域进行认证；否则，使用缺省认证域进行认证。]{style="font-family:宋体"}

[[DHCP]{lang="EN-US"}]{#struct_0_18608_20265_x1488244735}[中继组网环境中，接入设备可以提取用户]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的指定]{style="font-family:宋体"}[Option]{lang="EN-US"}[信息。如果接入设备信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option 18]{lang="EN-US"}[，则：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接入设备在采用]{lang="EN-US" style="font-family:宋体"}[version 2.0]{lang="EN-US"}]{#struct_0_18608_20265_1807897997}[格式封装]{lang="EN-US" style="font-family:宋体"}[RADIUS NAS-PORT-ID]{lang="EN-US"}[属性时，会根据]{lang="EN-US" style="font-family:宋体"}[Option 18]{lang="EN-US"}[选项内容封装发往]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接入设备会根据]{lang="EN-US" style="font-family:宋体"}[Option 18]{lang="EN-US"}]{#struct_0_18608_20265_348356794}[选项的内容封装发往]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{lang="EN-US" style="font-family:宋体"}[DSL_AGENT_CIRCUIT_ID]{lang="EN-US"}[属性。]{lang="EN-US" style="font-family:宋体"}

[[如果接入设备信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_18608_20265_392769085}[报文中的]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[，则接入设备会根据]{style="font-family:宋体"}[Option 37]{lang="EN-US"}[选项的内容封装发往]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[DSL_AGENT_REMOTE_ID]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1702089821}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1979971735}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置设备信任]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Option18]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x1904529485}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber trust option18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_358944970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber dhcp domain]{lang="EN-US"}**]{#struct_0_18608_20265_x938852554}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator dhcp enable]{lang="EN-US"}**]{#struct_0_18608_20265_1560216025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber nas-port-id format]{lang="EN-US"}**]{#struct_0_18608_20265_1594036141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber nas-port-id nasinfo-insert]{lang="EN-US"}**]{#struct_0_18608_20265_x1737539098}
:::

::: {#2082704026 .myid}
[]{#_Toc404785890}[]{#struct_0_18608_20265_1411865942}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber unclassified-ip domain**

------------------------------------------------------------------------

[**[ipv6 subscriber unclassified-ip domain]{lang="EN-US"}**]{#struct_0_18608_20265_1285186034}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户使用的认证域。]{style="font-family:宋体"}

[**[undo ipv6 subscriber unclassified-ip domain]{lang="EN-US"}**]{#struct_0_18608_20265_36397192}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_255931740}

[**[ipv6 subscriber unclassified-ip domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_x808261713}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber unclassified-ip domain**]{lang="EN-US"}]{#struct_0_18608_20265_966157658}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_393621053}

[[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_374541400}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的认证域为缺省认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1535535467}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1303170414}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_916726732}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x820993583}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_862216086}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1787252109}

[*[domain-name]{lang="SV"}*]{#struct_0_18608_20265_x556822915}[：认证使用的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:
black"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_153094615}

[[该命令用来配置未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_1162291904}[报文触发接入的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[接入用户在认证时使用的缺省域名，该域名必须在接入设备上存在且配置完整。]{style="font-family:宋体"}

[[如果指定接口上配置了]{style="font-family:宋体"}**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_x2114598743}[，则优先使用]{style="font-family:宋体"}**[ipv6 subscriber service-identify]{lang="EN-US"}**[指定的业务识别方式获取对应的认证域。只有在未匹配到]{style="font-family:宋体"}**[ipv6 subscriber service-identify]{lang="EN-US"}**[命令指定的认证域时，才使用]{style="font-family:宋体"}**[ipv6 subscriber unclassified-ip domain]{lang="EN-US"}**[命令指定的认证域。如果]{style="font-family:宋体"} **[ipv6 subscriber unclassified-ip domain]{lang="EN-US"}**[命令也未配置，则使用缺省认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1225357931}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x1963475093}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="SV"}[未知源]{style="font-family:宋体"}[IP]{lang="SV"}[接入]{style="font-family:
宋体"}[用户使用的认证域为]{style="font-family:宋体"}[ipoe]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_393686589}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber unclassified-ip domain ipoe]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x724843487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_18608_20265_x577019980}**[v6]{lang="EN-US"}[ subscriber initiator unclassified-ip enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_1397811231}
:::

::: {#119948508 .myid}
[]{#_Toc404785891}[]{#struct_0_18608_20265_1429922571}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber unclassified-ip max-session**

------------------------------------------------------------------------

[**[ipv6 subscriber unclassified-ip max-session]{lang="EN-US"}**]{#struct_0_18608_20265_x872735758}[命令用来配置接口上允许未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文触发创建的动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话的最大数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber unclassified-ip max-session**]{lang="EN-US"}]{#struct_0_18608_20265_x2064621456}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_2136349190}

[**[ipv6 subscriber unclassified-ip max-session ]{lang="EN-US"}***[max-number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_18608_20265_1027094587}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber unclassified-ip** **max-session**]{lang="EN-US"}]{#struct_0_18608_20265_x393780884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1829362096}

[[未限制接口上允许未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1510575628}[报文创建的动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1097246865}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1972233093}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_393096764}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_16952741}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x90694818}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1062037849}

[*[max-number ]{lang="EN-US"}*]{#struct_0_18608_20265_x1525259898}[：[允许未知源]{style="color:black"}]{style="font-family:宋体"}[IPv6]{lang="EN-US" style="color:black"}[报文触发]{style="font-family:宋体;
color:black"}[创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_x948672460}

[[未知源]{style="font-family:宋体"}]{#struct_0_18608_20265_x1350686628}[IPv6]{lang="SV"}[报文]{style="font-family:宋体"}[触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话数目]{style="font-family:宋体"}[达到最大值后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[后续未知源]{style="font-family:宋体"}[IPv6]{lang="SV"}[报文不能触发创建]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话。]{style="font-family:宋体"}[DHCPv6]{lang="SV"}[报文触发创建]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[不会受此最大值限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_697419881}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x1134529976}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上允许未知源]{style="font-family:宋体"}[IPv6]{lang="SV" style="color:black"}[报文]{style="font-family:宋体;color:black"}[触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[最大数为]{style="font-family:宋体"}[100]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_358657545}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="SV"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber unclassified-ip max-session 100]{lang="SV"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x446253474}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_1744870410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_x465091890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_393162300}
:::

::: {#-1505874465 .myid}
[]{#_Toc404785892}[]{#struct_0_18608_20265_x12746378}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber unclassified-ip username**

------------------------------------------------------------------------

[**[ipv6 subscriber unclassified-ip username]{lang="EN-US"}**]{#struct_0_18608_20265_948330289}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户的认证用户名。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber unclassified-ip username**]{lang="EN-US"}]{#struct_0_18608_20265_79801456}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1227402743}

[**[ipv6 subscriber unclassified-ip username include]{lang="EN-US"}**[ { **nas-port-id** \| **port** \[ *separator* \] \| **second-vlan** \[ *separator* \] \| **slot** \[ *separator* \] \| **source-ip** \[ **separator** *separator* \] *\|* **source-mac** \[ **separator** *separator* \] \| **subslot** \[ *separator* \] \| **sysname** \[ *separator* \] \| **vlan** \[ *separator* \] } \*]{lang="EN-US"}]{#struct_0_18608_20265_x1705960306}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber unclassified-ip username**]{lang="EN-US"}]{#struct_0_18608_20265_2086643304}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1499662696}

[[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x992643662}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户采用[用户报文的]{style="color:black"}源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为认证用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x414529384}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_587662019}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x747166528}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1817662762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1817896025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_392965692}

[**[nas-port-id]{lang="EN-US"}**]{#struct_0_18608_20265_x336444820}[：表示使用用户的]{style="font-family:宋体"}[NAS-PORT-ID]{lang="EN-US"}[属性作为用户名。]{style="font-family:宋体"}

[**[port]{lang="SV"}**]{#struct_0_18608_20265_1811659456}[：]{style="font-family:宋体"}[表示以报文接入的端口号作为用户名。]{style="font-family:宋体"}

[**[s]{lang="EN-US"}**]{#struct_0_18608_20265_x1101253349}**[econd-vlan]{lang="SV"}**[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[**[slot]{lang="SV"}**]{#struct_0_18608_20265_x820720664}[：]{style="font-family:宋体"}[表示以报文接入的槽位号作为用户名。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**]{#struct_0_18608_20265_1375670313}[：表示使用用户报文的]{style="font-family:宋体;color:black"}[源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为用户名]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="EN-US"}***[separator]{lang="EN-US"}*]{#struct_0_18608_20265_x1079692092}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址分隔符，可以为任意可配置的可见字符。若指定了分隔符，例如"]{style="font-family:宋体"}[-]{lang="EN-US"}["，则用户名形如]{style="font-family:宋体"}[1-2-3]{lang="EN-US"}[；若不指定该参数，则用户名形如]{style="font-family:宋体"}[1::2:3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-mac]{lang="SV"}**]{#struct_0_18608_20265_x424634128}[：]{style="font-family:宋体;color:black"}[表示使用用户报文的]{style="font-family:宋体;
color:black"}[源]{style="font-family:宋体"}[MAC]{lang="SV"}[地址作为用户名]{style="font-family:宋体"}[。]{style="font-family:宋体;color:black"}

[**[separator ]{lang="SV"}**]{#struct_0_18608_20265_x570478804}*[separator]{lang="SV"}*[：]{style="font-family:
宋体"}[MAC]{lang="SV"}[地址分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[可以为任意可配置的可见字符。若指定了分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[例如]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="SV"}["，]{style="font-family:
宋体"}[则用户名形如]{style="font-family:宋体"}[xxxx-xxxx-xxxx]{lang="SV"}[；]{style="font-family:宋体"}[若不指定该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则用户名为]{style="font-family:宋体"}[xxxxxxxxxxxx]{lang="SV"}[形式。]{style="font-family:宋体"}

[**[subslot]{lang="SV"}**]{#struct_0_18608_20265_x1483406983}[：]{style="font-family:宋体"}[表示以报文接入的子卡号作为用户名。]{style="font-family:宋体"}

[**[sysname]{lang="SV"}**]{#struct_0_18608_20265_691810370}[：]{style="font-family:宋体"}[表示以报文接入设备的设备名作为用户名。]{style="font-family:宋体"}

[**[vlan]{lang="SV"}**]{#struct_0_18608_20265_1811659453}[：]{style="font-family:宋体"}[表示以认证报文中的]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN]{lang="SV"}[作为用户名。]{style="font-family:宋体"}

[*[separator]{lang="SV" style="color:black"}*]{#struct_0_18608_20265_x1101449957}[：]{style="font-family:宋体;
color:black"}[当前字段分隔符]{style="font-family:宋体;color:black"}[，]{style="font-family:宋体;color:black"}[用在当前字段后面以连接后面的一个字段]{style="font-family:宋体;
color:black"}[，]{style="font-family:宋体;color:black"}[可以为任意可配置的可见字符。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1832541606}

[[本命令用来配置未知源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_x1878745123}[报文触发接入的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户在认证时使用的用户名，该用户名必须与认证服务器上配置的用户名保持一致。]{style="font-family:宋体"}

[[在允许的用户名类型范围内，该命令支持任意形式、任意顺序的用户名组合。例如：若配置]{style="font-family:宋体"}**[ipv6 subscriber unclassified-ip username include source-ip source-mac]{lang="EN-US"}**]{#struct_0_18608_20265_1795664458}[，则用户名为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址字段]{style="font-family:宋体"}[和]{style="font-family:宋体"}[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[字段内容的拼接，且两个字段之间无分隔符。]{style="font-family:宋体"}

[[建议不要使用]{style="font-family:宋体"}]{#struct_0_18608_20265_x1366062187}[@]{lang="SV"}[作为分隔符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[避免携带]{style="font-family:宋体"}[@]{lang="SV"}[字符的用户名在]{style="font-family:
宋体"}[AAA]{lang="SV"}[服务器端不能被正确解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1525142829}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_1869069834}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上的未知源]{style="font-family:宋体"}[IPv6]{lang="SV"}[用户使用[用户报文的]{style="color:black"}源]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址作为用户名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_18608_20265_884351888}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber unclassified-ip username include source-ip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x730660374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber initiator unclassified-ip enable]{lang="EN-US"}**]{#struct_0_18608_20265_1774969559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber password]{lang="EN-US"}**]{#struct_0_18608_20265_393031228}
:::

::: {#-439554978 .myid}
[]{#_Toc404785893}[]{#struct_0_18608_20265_1543304566}[]{#_Toc345424005}[]{#_Toc345404983}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber user-detect**

------------------------------------------------------------------------

[**[ipv6 subscriber user-detect]{lang="EN-US"}**]{#struct_0_18608_20265_x158568050}[命令用来开启静态]{style="font-family:
宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户在线探测功能，并配置其探测方式。]{style="font-family:宋体"}

[**[undo ipv6 subscriber user-detect]{lang="EN-US"}**]{#struct_0_18608_20265_1737398087}[命令用来关闭静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户在线探测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1792784909}

[**[ipv6 subscriber user-detect ]{lang="EN-US"}**[{ **icmpv6** \| **nd** } **retry** *times* **interval** *interval* ]{lang="EN-US"}]{#struct_0_18608_20265_1799301815}

[**[undo]{lang="EN-US"}**[ **ipv6 subscriber user-detect** ]{lang="EN-US"}]{#struct_0_18608_20265_x634526669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_x192153277}

[[静态]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x153827380}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户在线探测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_691847896}

[[三层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_x1923445766}[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2117493954}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x737201269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1685099185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_392834620}

[**[icmpv6]{lang="EN-US"}**]{#struct_0_18608_20265_x691322425}[：表示使用]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[请求报文作为探测报文。]{style="font-family:宋体"}

[**[nd]{lang="EN-US"}**]{#struct_0_18608_20265_1745042603}[：表示使用]{style="font-family:宋体"}[ND NS]{lang="EN-US"}[报文作为探测报文。]{style="font-family:宋体"}

[**[retry ]{lang="EN-US"}**]{#struct_0_18608_20265_x452765025}*[times]{lang="EN-US"}*[：[探测失败后允许重复尝试的最大次数]{style="color:black"}]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体;color:black"}[2]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[5]{lang="EN-US" style="color:black"}[。例如，]{style="font-family:宋体;color:black"}*[times]{lang="SV"}*[值为]{style="font-family:宋体;color:black"}[2]{lang="EN-US" style="color:black"}[表示连续三次失败就认为用户不在线。]{style="font-family:宋体;color:black"}

[**[interval ]{lang="EN-US"}**]{#struct_0_18608_20265_x578835545}*[interval]{lang="EN-US"}*[：[探测的时间间隔]{style="color:black"}]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1200]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_1986027727}

[[接口上的静态]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_1889457477}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户上线后，设备会定时统计用户流量。若一个探测间隔（]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[）内用户流量无变化，则该探测间隔结束后，设备将发送一次探测报文。]{style="font-family:宋体"}[如果设备在探测间隔内未收到用户的报文，则认为一次探测失败。]{style="font-family:宋体"}

[[若设备首次探测失败，将继续做指定次数（]{style="font-family:宋体"}*[times]{lang="EN-US"}*]{#struct_0_18608_20265_x775105348}[）的重复探测，若全部]{style="font-family:宋体"}[探测尝试都]{style="font-family:宋体"}[失败（即一直未收到该用户报文），则认为此用户不在线，停止发送探测报文并删除用户；若设备在探测中收到用户的报文，则认为用户在线，重置探测定时器并开始下一次探测。]{style="font-family:宋体"}

[[对于与]{style="font-family:宋体"}]{#struct_0_18608_20265_x1765974072}[接口在同一网段内的静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户，可使用]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[ND NS]{lang="SV"}[或]{style="font-family:宋体"}[ICMPv6]{lang="SV"}[请求]{style="font-family:宋体"}[报文对用户进行探测；]{style="font-family:宋体"}[对于与接口不]{style="font-family:宋体"}[在同一网段内的静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[个人接入用户，应使用]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[请求]{style="font-family:宋体"}[报文对用户进行探测。]{style="font-family:宋体"}

[[接口上不可同时启用两种方式对]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}]{#struct_0_18608_20265_x13559331}[个人接入用户进行探测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1959045360}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x996333727}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上使用]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[ND NS]{lang="SV"}[报文对静态]{style="font-family:宋体"}[/]{lang="EN-US"}[动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[个人接入用户进行在线检测，[探测失败后允许重复尝试]{style="color:black"}]{style="font-family:宋体"}[3]{lang="EN-US" style="color:black"}[次，探测的时间间隔为]{style="font-family:宋体;color:black"}[50]{lang="EN-US" style="color:black"}[秒]{style="font-family:宋体;color:black"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_x292829195}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 subscriber user-detect nd retry 3 interval 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1599140547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber enable]{lang="EN-US"}**]{#struct_0_18608_20265_392900156}
:::

::: {#-1246764538 .myid}
[]{#_Toc345424014}[]{#_Toc345404992}[]{#_Toc404785894}[]{#struct_0_18608_20265_1272029171}[]{#_Toc345424001}[]{#_Toc345404979}

**IPoE \-- IPv6 IPoE配置命令 \-- ipv6 subscriber vlan**

------------------------------------------------------------------------

[**[ipv6 subscriber vlan]{lang="EN-US"}**]{#struct_0_18608_20265_x705619047}[命令用于配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[值与认证域的映射关系。]{style="font-family:宋体"}

[**[undo ipv6 subscriber vlan]{lang="EN-US"}**]{#struct_0_18608_20265_x1080030438}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1968464200}

[**[ipv6 subscriber vlan ]{lang="EN-US"}***[vlan-list ]{lang="EN-US"}*[ ]{lang="EN-US"}**[domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18608_20265_x2061359692}

[**[undo ipv6 subscriber vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_18608_20265_780695574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18608_20265_700207696}

[[未指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_18608_20265_1680470940}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文的内]{style="font-family:宋体"}[/]{lang="EN-US"}[外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与认证域的映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1894156567}

[[三层以太网子接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_18608_20265_561375446}[三层聚合子接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_185059125}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_1895673808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x298321254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_392703548}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_18608_20265_689163669}[：]{style="font-family:宋体;color:black"}[VLAN]{lang="SV"}[列表]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示一个或多个]{style="font-family:宋体"}[VLAN]{lang="SV"}[，]{style="font-family:宋体"}[表示方式为]{style="font-family:
宋体"}*[vlan-list]{lang="SV"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="SV"}[，]{style="font-family:
宋体"}[其中]{style="font-family:宋体"}[，]{style="font-family:
宋体"}*[vlan-id]{lang="SV"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="SV"}[的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4094]{lang="SV"}[。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1078666033}*[ domain-name]{lang="SV"}*[：表示与指定的]{style="font-family:宋体;color:black"}[VLAN]{lang="SV" style="color:black"}[范围相关联的]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域名，为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[255]{lang="EN-US" style="color:black"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体;
color:black"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:
宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:
宋体"}[@]{lang="SV"}["]{style="font-family:宋体"}[字符[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_493482084}

[[本命令用来配置指定]{style="font-family:宋体;color:windowtext"}]{#struct_0_18608_20265_x224461140}[VLAN]{lang="EN-US" style="color:windowtext"}[范围内未知源]{style="font-family:宋体;
color:windowtext"}[IPv6]{lang="EN-US" style="color:windowtext"}[接入用户进行认证时使用的认证域，通过指定的认证域进行认证授权。]{style="font-family:宋体;color:windowtext"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_333280759}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1929401001}[在子接口]{style="font-family:宋体"}[GigabitEthernet 1/1.100]{lang="EN-US"}[上配置内层]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[到]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[未知源]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户认证使用的认证域为]{style="font-family:宋体"}[vlandm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18608_20265_902994646}

[\[Sysname\] interface gigabitethernet 1/0/1.100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ipv6 subscriber service-identify second-vlan]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1.100\] ipv6 subscriber vlan 2 to 100 domain vlandm]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x581604963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 subscriber service-identify]{lang="EN-US"}**]{#struct_0_18608_20265_755046297}
:::

::: {#93634357 .myid}
[]{#_Toc404785895}[]{#struct_0_18608_20265_x645062293}[]{#_Toc345424019}[]{#_Toc345404997}

**IPoE \-- IPv6 IPoE配置命令 \-- reset ipv6 subscriber offline statistics**

------------------------------------------------------------------------

[**[reset ipv6 subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x986437844}[命令用来清除]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户下线统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_1171759807}

[**[reset ipv6 subscriber offline statistics ]{lang="EN-US"}**[\[ **[interface]{style="color:black"}**]{lang="EN-US"}]{#struct_0_18608_20265_392769084}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}***[interface]{lang="EN-US" style="color:black"}[-type ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface]{lang="EN-US" style="color:black"}[-]{lang="EN-US" style="font-size:
10.0pt;color:black"}[number]{lang="EN-US" style="color:black"}*[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_x1702089820}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18608_20265_x413887794}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_x2021439549}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1652631995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_x1735444913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_631638807}

[**[interface]{lang="EN-US" style="color:black"}**]{#struct_0_18608_20265_1545112538}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}***[interface]{lang="EN-US" style="color:black"}[-type ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface]{lang="EN-US" style="color:black"}[-]{lang="EN-US" style="font-size:
10.0pt;color:black"}[number]{lang="EN-US" style="color:black"}*[：]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:black"}[表示]{style="font-family:宋体"}[清除指定接口上的]{lang="EN-US" style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户下线统计信息，]{lang="EN-US" style="font-family:宋体"}*[interface-type]{lang="EN-US" style="color:black"}[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[interface-number]{lang="EN-US" style="color:
black"}*[表示接口类型和接口编号。]{lang="EN-US" style="font-family:宋体"}[如果未指定本参数，]{style="font-family:宋体"}[将]{style="font-family:宋体"}[清除所有接口上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户下线统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1266571905}

[[\# ]{lang="EN-US"}]{#struct_0_18608_20265_x1494628412}[清除所有接口上的]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[用户的下线统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 subscriber offline statistics]{lang="EN-US"}]{#struct_0_18608_20265_x390741289}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_x142822987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber offline statistics]{lang="EN-US"}**]{#struct_0_18608_20265_x1401345884}

[ ]{lang="EN-US"}
:::

::: {#1303587622 .myid}
[]{#_Toc404785896}[]{#struct_0_18608_20265_1098565916}

**IPoE \-- IPv6 IPoE配置命令 \-- reset ipv6 subscriber session**

------------------------------------------------------------------------

[**[reset ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_393621052}[命令用来清除动态触发创建的]{style="font-family:
宋体"}[IPv6 IPoE]{lang="EN-US"}[会话，强制用户下线。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_374541401}

[**[reset ipv6 subscriber session ]{lang="EN-US"}**[\[ **interface** *[interface-type interface-number]{style="color:black"}* \] \[ **domain** *domain-name* \| **ipv6** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \] \| **mac** *mac-address* \| **username** *name* \]]{lang="EN-US"}]{#struct_0_18608_20265_1535535468}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18608_20265_1304153454}

[[用户视图]{style="font-family:宋体"}]{#struct_0_18608_20265_1970908981}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18608_20265_650350352}

[[network-admin]{lang="EN-US"}]{#struct_0_18608_20265_37122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18608_20265_1054899814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18608_20265_1102795845}

[**[interface ]{lang="SV"}**]{#struct_0_18608_20265_x1280742764}*[interface-type interface-number]{lang="SV" style="color:black"}*[：表示]{style="font-family:宋体;color:black"}[清除指定接口动态触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[interface-type interface-number]{lang="SV"}*[表示接口类型和接口编号。如果未指定本参数]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[将]{style="font-family:宋体"}[清除所有接口]{style="font-family:宋体"}[动态]{style="font-family:宋体"}[触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[domain]{lang="SV"}**]{#struct_0_18608_20265_1041456866}*[ domain-name]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除使用]{style="font-family:宋体"}[指定]{style="font-family:宋体;color:black"}[ISP]{lang="SV" style="color:black"}[域认证的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[domain-name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\\]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\|]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}["]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[:]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\*]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="SV"}["]{style="font-family:
宋体"}[、]{style="font-family:宋体"}["]{style="font-family:宋体"}[\<]{lang="SV"}["]{style="font-family:宋体"}[、]{style="font-family:
宋体"}["]{style="font-family:宋体"}[\>]{lang="SV"}["]{style="font-family:宋体"}[以及]{style="font-family:宋体"}["]{style="font-family:宋体"}[@]{lang="SV"}["]{style="font-family:
宋体"}[字符。]{style="font-family:宋体"}

[**[ipv6]{lang="SV"}**]{#struct_0_18608_20265_x1059158098}*[ ipv6-address]{lang="SV"}*[：]{style="font-family:宋体;color:black"}[表示]{style="font-family:宋体;color:black"}[清除指定]{style="font-family:宋体"}[IP]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话，]{style="font-family:宋体"}*[ipv6-address]{lang="SV"}*[为指定的]{style="font-family:宋体"}[IPv6]{lang="SV"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="SV"}**]{#struct_0_18608_20265_1500953954}*[vpn-instance-name]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除[指定]{style="color:black"}]{style="font-family:宋体"}[VPN]{lang="SV" style="color:black"}[的]{style="font-family:宋体;color:black"}[IPv6 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}*[vpn-instance-name]{lang="SV"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="SV"}[的]{style="font-family:宋体"}[VPN]{lang="SV"}[实例名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:
宋体"}[31]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv6 IPoE]{lang="EN-US"}[会话]{style="font-family:宋体"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_18608_20265_1337241130}*[ ]{lang="EN-US"}[mac-address]{lang="SV"}*[：表示]{style="font-family:宋体;color:black"}[清除指定[源]{style="color:black"}]{style="font-family:宋体"}[MAC]{lang="SV"}[地址的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}[形式为]{style="font-family:宋体"}[H-H-H]{lang="SV"}[。]{style="font-family:宋体"}

[**[username ]{lang="SV"}**]{#struct_0_18608_20265_947101887}*[name]{lang="SV"}*[：表示]{style="font-family:宋体;
color:black"}[清除]{style="font-family:宋体"}[指定]{style="font-family:宋体;color:black"}[用户名]{style="font-family:宋体;
color:black"}[的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话[，]{style="color:black"}]{style="font-family:宋体"}*[name]{lang="SV"}*[为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18608_20265_393686588}

[[本命令]{style="font-family:宋体"}]{#struct_0_18608_20265_x724843486}[用来]{style="font-family:宋体;color:black"}[清除动态触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并强制用户下线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[如果不指定条件]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则表示删除所有动态]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[专线用户和静态个人用户不能通过]{style="font-family:宋体"}]{#struct_0_18608_20265_x577085516}**[reset ipv6 subscriber session]{lang="SV" style="color:black"}**[命令强制下线]{style="font-family:宋体"}[，]{style="font-family:宋体"}[只能通过相应的]{style="font-family:宋体"}**[undo]{lang="SV"}**[命令删除配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18608_20265_1767989100}

[[\# ]{lang="SV"}]{#struct_0_18608_20265_x391765401}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="SV"}[上动态触发创建的]{style="font-family:宋体"}[IPv6 IPoE]{lang="SV"}[会话，]{style="font-family:宋体"}[强制用户下线。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 subscriber session interface gigabitethernet 1/0/1]{lang="SV" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_18608_20265_x1714322407}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18608_20265_605461571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 subscriber session]{lang="EN-US"}**]{#struct_0_18608_20265_x1605058720}
:::
