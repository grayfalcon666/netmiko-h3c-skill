::: {#-794325652 .myid}
[]{#_Toc404786934}[]{#struct_0_90630_81574_1745295028}[]{#_Toc359402199}

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_90630_81574_x14817724}

[**[debugging ipv6 dhcp client ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x1069954624}

[**[undo debugging ipv6 dhcp client ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x1591069536}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90630_81574_1745360564}

[[用户视图]{style="font-family:宋体"}]{#struct_0_90630_81574_x2022030342}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90630_81574_x208034327}

[[network-admin]{lang="EN-US"}]{#struct_0_90630_81574_702399212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90630_81574_1745163956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90630_81574_1544867614}

[**[all]{lang="EN-US"}**]{#struct_0_90630_81574_x1434256441}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_90630_81574_x41795731}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_90630_81574_1745229492}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_90630_81574_x878158461}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_90630_81574_685268254}

[**[debugging ipv6 dhcp client]{lang="EN-US"}**]{#struct_0_90630_81574_1388715308}[命令用来打开]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 dhcp client]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[客户端调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1472708120}[客户端调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging ipv6 dhcp client error]{lang="EN-US"}]{#struct_0_90630_81574_1745557172}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x268094644}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_755235880}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x1203392511}

[[Failed to notify the client\'s information change.]{lang="EN-US"}]{#struct_0_90630_81574_1745622708}

[[通知其他模块失败，通知内容为客户端信息的变化]{style="font-family:宋体"}]{#struct_0_90630_81574_1508203101}

[[Failed to acquire IRT]{lang="EN-US"}]{#struct_0_90630_81574_x29446256}

[[不能获取]{style="font-family:宋体"}[IRT]{lang="EN-US"}]{#struct_0_90630_81574_1745426100}[值]{style="font-family:宋体"}

[[Failed to acquire interface control block.]{lang="EN-US"}]{#struct_0_90630_81574_x1964931153}

[[不能获取接口控制块]{style="font-family:宋体"}]{#struct_0_90630_81574_1745491636}

[[Response without a server ID.]{lang="EN-US"}]{#struct_0_90630_81574_x836519953}

[[回应报文中没有]{style="font-family:宋体"}[server ID]{lang="EN-US"}]{#struct_0_90630_81574_218174134}

[[Response without a client ID.]{lang="EN-US"}]{#struct_0_90630_81574_1745819316}

[[回应报文中没有]{style="font-family:宋体"}[client ID]{lang="EN-US"}]{#struct_0_90630_81574_694049857}

[[Advertise message with matching transaction ID and mismatching client ID.]{lang="EN-US"}]{#struct_0_90630_81574_1745884852}

[[交互]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_90630_81574_28930150}[符合但]{style="font-family:宋体"}[client ID]{lang="EN-US"}[不符合的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Discarded invalid Advertise packet.]{lang="EN-US"}]{#struct_0_90630_81574_x720918944}

[[丢弃无效的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_1745295029}[报文。]{style="font-family:宋体"}

[[Invalid DHCPv6 preference option length.]{lang="EN-US"}]{#struct_0_90630_81574_x14883260}

[[无效的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1745360565}[优先级选项长度]{style="font-family:宋体"}

[[Invalid server ID option information.]{lang="EN-US"}]{#struct_0_90630_81574_x2021964806}

[[无效的]{style="font-family:宋体"}[serverID]{lang="EN-US"}]{#struct_0_90630_81574_1745163957}[选项内容]{style="font-family:宋体"}

[[Discarded invalid reply packet.]{lang="EN-US"}]{#struct_0_90630_81574_1544933150}

[[丢弃无效的]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_90630_81574_1745229493}[报文]{style="font-family:宋体"}

[[Corrupt IAADDR options.]{lang="EN-US"}]{#struct_0_90630_81574_x878092925}

[[不完整的]{style="font-family:宋体"}[IA]{lang="EN-US"}]{#struct_0_90630_81574_1745557173}[地址选项]{style="font-family:宋体"}

[[Invalid IAADDR option.]{lang="EN-US"}]{#struct_0_90630_81574_755170344}

[[无效的]{style="font-family:宋体"}[IA]{lang="EN-US"}]{#struct_0_90630_81574_1745622709}[地址选项信息]{style="font-family:宋体"}

[[Corrupt IA_NA options.]{lang="EN-US"}]{#struct_0_90630_81574_1508268637}

[[不完整的]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}]{#struct_0_90630_81574_1745426101}[选项]{style="font-family:宋体"}

[[Invalid IA_NA option.]{lang="EN-US"}]{#struct_0_90630_81574_x1964865617}

[[无效的]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}]{#struct_0_90630_81574_1745491637}[选项信息]{style="font-family:宋体"}

[[Corrupt IAPREFIX options.]{lang="EN-US"}]{#struct_0_90630_81574_x836585489}

[[不完整的]{style="font-family:宋体"}[IA]{lang="EN-US"}]{#struct_0_90630_81574_1745819317}[前缀选项]{style="font-family:宋体"}

[[Invalid IAPREFIX option.]{lang="EN-US"}]{#struct_0_90630_81574_693984321}

[[无效的]{style="font-family:宋体"}[IAPREFIX]{lang="EN-US"}]{#struct_0_90630_81574_1745884853}[选项信息]{style="font-family:宋体"}

[[Corrupt IA_PD options.]{lang="EN-US"}]{#struct_0_90630_81574_28995686}

[[不完整的]{style="font-family:宋体"}[IA_PD]{lang="EN-US"}]{#struct_0_90630_81574_1745295026}[选项]{style="font-family:宋体"}

[[Invalid IA_PD option.]{lang="EN-US"}]{#struct_0_90630_81574_x14162364}

[[无效的]{style="font-family:宋体"}[IA_PD]{lang="EN-US"}]{#struct_0_90630_81574_1745360562}[选项]{style="font-family:宋体"}

[[Invalid status code length *length.*]{lang="EN-US"}]{#struct_0_90630_81574_1745163954}

[[无效的状态码选项长度]{style="font-family:宋体"}]{#struct_0_90630_81574_1544998686}

[[Wrong IA type in Advertise message]{lang="EN-US"}]{#struct_0_90630_81574_1745229490}

[[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_x878027389}[报文中]{style="font-family:宋体"}[IA]{lang="EN-US"}[类型错误]{style="font-family:宋体"}

[[Wrong IA type in Reply message.]{lang="EN-US"}]{#struct_0_90630_81574_1745557170}

[[Reply]{lang="EN-US"}]{#struct_0_90630_81574_755366952}[报文中]{style="font-family:宋体"}[IA]{lang="EN-US"}[类型错误]{style="font-family:宋体"}

[[Discarded reply without Rapid-Commit.]{lang="EN-US"}]{#struct_0_90630_81574_1745622706}

[[丢弃不包含]{style="font-family:宋体"}[Rapid-Commit]{lang="EN-US"}]{#struct_0_90630_81574_1507809885}[选项的]{style="font-family:宋体"}[Reply]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Can\'t renew without an active binding.]{lang="EN-US"}]{#struct_0_90630_81574_1745426098}

[[不存在有效的绑定无法启动]{style="font-family:宋体"}[renew]{lang="EN-US"}]{#struct_0_90630_81574_1745491634}[操作]{style="font-family:宋体"}

[[Malformed packet dhcp6:]{lang="EN-US"}]{#struct_0_90630_81574_x509267168}

[[option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_90630_81574_x1584771446}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_90630_81574_x509332704}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[Invalid unicast option length *length*.]{lang="EN-US"}]{#struct_0_90630_81574_x836388881}

[[无效的单播选项长度]{style="font-family:宋体"}]{#struct_0_90630_81574_1745819314}

[[IPv6 socket initilization failed.]{lang="EN-US"}]{#struct_0_90630_81574_694180929}

[[IPv6 socket]{lang="EN-US"}]{#struct_0_90630_81574_1745884850}[初始化发生错误]{style="font-family:宋体"}

[[Invalid lifetime in the reply packet.]{lang="EN-US"}]{#struct_0_90630_81574_28799078}

[[Reply]{lang="EN-US"}]{#struct_0_90630_81574_1745295027}[报文中的生命期非法]{style="font-family:宋体"}

[[Failed to send packet: only *send-length* of *total-length* bytes were sent.]{lang="EN-US"}]{#struct_0_90630_81574_1745360563}

[[发送报文失败，共]{style="font-family:宋体"}*[ total-length]{lang="EN-US"}*]{#struct_0_90630_81574_x2021833734}[字节的报文仅发送出]{style="font-family:宋体"}*[send-length]{lang="EN-US"}*[字节]{style="font-family:宋体"}

[[Failed to create max delay timer.]{lang="EN-US"}]{#struct_0_90630_81574_1745163955}

[[创建延迟发送定时器失败]{style="font-family:宋体"}]{#struct_0_90630_81574_1545064222}

[[Failed to create IPv6 socket, error: *error-number.*]{lang="EN-US"}]{#struct_0_90630_81574_1745229491}

[[创建]{style="font-family:宋体"}[IPv6 socket ]{lang="EN-US"}]{#struct_0_90630_81574_1745557171}[失败，错误码]{style="font-family:宋体"}*[error-number.]{lang="EN-US"}*

[[Failed to bind socket.]{lang="EN-US"}]{#struct_0_90630_81574_755301416}

[[Socket ID: *socket-id*, error: *error-number*.]{lang="EN-US"}]{#struct_0_90630_81574_1745622707}

[[绑定]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_90630_81574_1745426099}[失败，]{style="font-family:宋体"}[Socket ID *socket-id*]{lang="EN-US"}[，错误码]{style="font-family:宋体"} *[error-number]{lang="EN-US"}*

[[ Failed to set socket option.]{lang="EN-US"}]{#struct_0_90630_81574_374310840}

[[ Socket ID: *socket-id*, error: *error-number*.]{lang="EN-US"}]{#struct_0_90630_81574_1745491635}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_90630_81574_1745819315}[选项失败，]{style="font-family:宋体"}[Socket ID *socket-id*]{lang="EN-US"}[，错误码]{style="font-family:宋体"} *[error-number]{lang="EN-US"}*

[[Failed to receive packet from socket. ]{lang="EN-US"}]{#struct_0_90630_81574_694115393}

[[Socket ID: *socket-id*, error: *error-number*.]{lang="EN-US"}]{#struct_0_90630_81574_1745884851}

[[不能从]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_90630_81574_1745295024}[接收报文，]{style="font-family:宋体"}[Socket ID *socket-id*]{lang="EN-US"}[，错误码]{style="font-family:宋体"} *[error-number]{lang="EN-US"}*

[[Discarded packet with no IA or address.]{lang="EN-US"}]{#struct_0_90630_81574_x14031292}

[[丢弃不含]{style="font-family:宋体"}[IA]{lang="EN-US"}]{#struct_0_90630_81574_1745360560}[或地址的]{style="font-family:宋体"}[Advertise]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Response with mismatching client ID]{lang="EN-US"}]{#struct_0_90630_81574_264339749}

[[收到了应答报文，报文中的客户端]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_90630_81574_x1301744192}[和当前设备不匹配]{style="font-family:宋体"}

[[Wrong length of option 52]{lang="EN-US"}]{#struct_0_90630_81574_1226079916}

[[Option 52]{lang="EN-US"}]{#struct_0_90630_81574_x573682350}[长度错误]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging ipv6 dhcp client event]{lang="EN-US"}]{#struct_0_90630_81574_x2021768198}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x200147418}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_1071076063}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_1745163952}

[[Refresh event scheduled in *time* seconds.]{lang="EN-US"}]{#struct_0_90630_81574_1545129758}

[[在]{style="font-family:宋体"}*[time]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_90630_81574_1611488556}[秒后启动刷新事件日程表]{style="font-family:宋体"}

[[Immediately selected the server that sent the Advertise message.]{lang="EN-US"}]{#struct_0_90630_81574_1745229488}

[[立即选择发出该]{style="font-family:宋体"}[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_x877503102}[报文的]{style="font-family:宋体"}[server]{lang="EN-US"}

[[Recorded the server that sent the Advertise message.]{lang="EN-US"}]{#struct_0_90630_81574_x1910540549}

[[记录发出该]{style="font-family:宋体"}[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_1745557168}[报文的]{style="font-family:宋体"}[server]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Client information change notified successfully.]{lang="EN-US"}]{#struct_0_90630_81574_754842665}

[[成功通知客户端信息变化]{style="font-family:宋体"}]{#struct_0_90630_81574_1745622704}

[[Address expired.]{lang="EN-US"}]{#struct_0_90630_81574_1507940957}

[[地址过期]{style="font-family:宋体"}]{#struct_0_90630_81574_x253812027}

[[Prefix expired.]{lang="EN-US"}]{#struct_0_90630_81574_1745426096}

[[前缀过期]{style="font-family:宋体"}]{#struct_0_90630_81574_373852088}

[[Formed *msg-type*, *time* ms elapsed.]{lang="EN-US"}]{#struct_0_90630_81574_x1533473547}

[[生成]{style="font-family:宋体"}*[msg-type]{lang="EN-US"}*]{#struct_0_90630_81574_1745491632}[报文，其]{style="font-family:宋体"}[elapsed time]{lang="EN-US"}[选项为]{style="font-family:宋体"}*[time]{lang="EN-US"}*[ ms]{lang="EN-US"}

[*[message-type]{lang="EN-US"}*[ status code: *status code*.]{lang="EN-US"}]{#struct_0_90630_81574_x836782097}

[[报文]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*]{#struct_0_90630_81574_1745819312}[的状态码为]{style="font-family:宋体"}*[status code]{lang="EN-US"}*

[*[Interface-name]{lang="EN-US"}*[: DHCPC6 *client-type* FSM state changed from *former-state* to *later-state* successfully. ]{lang="EN-US"}]{#struct_0_90630_81574_693787713}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_1745884848}[上]{style="font-family:宋体"}*[client-type]{lang="EN-US"}*[类型的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端从]{style="font-family:宋体"}*[former-state]{lang="EN-US"}*[状态转换到]{style="font-family:宋体"}*[later-state]{lang="EN-US"}*[状态]{style="font-family:宋体"}

[[客户端类型的取值包括：]{style="font-family:宋体"}]{#struct_0_90630_81574_28274789}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD]{lang="EN-US"}]{#struct_0_90630_81574_x81082210}[：表示请求]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀的客户端]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADDR]{lang="EN-US"}]{#struct_0_90630_81574_1745295025}[：表示请求]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的客户端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stateless]{lang="EN-US"}]{#struct_0_90630_81574_x14096828}[：表示]{lang="EN-US" style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[无状态客户端]{lang="EN-US" style="font-family:宋体"}

[[状态的取值包括：]{style="font-family:宋体"}]{#struct_0_90630_81574_1745360561}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IDLE]{lang="EN-US"}]{#struct_0_90630_81574_x2021702662}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SOLICIT]{lang="EN-US"}]{#struct_0_90630_81574_1745163953}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_90630_81574_1545195294}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OPEN]{lang="EN-US"}]{#struct_0_90630_81574_478012892}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RENEW]{lang="EN-US"}]{#struct_0_90630_81574_1745229489}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REBIND]{lang="EN-US"}]{#struct_0_90630_81574_x877437566}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RELEASE]{lang="EN-US"}]{#struct_0_90630_81574_1745557169}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DECLINE]{lang="EN-US"}]{#struct_0_90630_81574_754777129}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}[NFO-REQUESTING]{lang="EN-US"}]{#struct_0_90630_81574_1745622705}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging ipv6 dhcp client packet]{lang="EN-US"}]{#struct_0_90630_81574_1508006493}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x183871494}[[字段]{style="font-family:宋体"}]{#struct_0_90630_81574_758779160}

[[描述]{style="font-family:宋体"}]{#struct_0_90630_81574_1745426097}

[[Packet sent]{lang="EN-US"}]{#struct_0_90630_81574_373917624}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1224876863}[报文已发送]{style="font-family:宋体"}

[[Packet received]{lang="EN-US"}]{#struct_0_90630_81574_1745491633}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x836847633}[报文已收到]{style="font-family:宋体"}

[[Type *message-type*(*number*)]{lang="EN-US"}]{#struct_0_90630_81574_x976452281}

[[报文类型（报文类型号）]{style="font-family:宋体"}]{#struct_0_90630_81574_1745819313}

[[Transaction-ID *transaction-id*]{lang="EN-US"}]{#struct_0_90630_81574_693722177}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_437093052}[客户端发起申请时生成的一个随机数，用来唯一标识一次申请过程]{style="font-family:宋体"}

[[Option]{lang="EN-US"}]{#struct_0_90630_81574_1745884849}

[[选项类型及类型号]{style="font-family:宋体"}]{#struct_0_90630_81574_28340325}

[[Length]{lang="EN-US"}]{#struct_0_90630_81574_x983588327}

[[选项长度]{style="font-family:宋体"}]{#struct_0_90630_81574_286498801}

[[Information]{lang="EN-US"}]{#struct_0_90630_81574_x697196247}

[[选项信息]{style="font-family:宋体"}]{#struct_0_90630_81574_x983522791}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90630_81574_231496606}

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_2105532555}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上启动]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的无状态配置，打开报文调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 dhcp client packet]{lang="EN-US"}]{#struct_0_90630_81574_x983653863}

[\*Feb 12 09:52:12:990 2013 Sysname DHCPC6/7/Packet: -MDC=1;]{lang="EN-US"}

[Vlan-interface2, Packet sent:]{lang="EN-US"}

[Type Information-request(11)]{lang="EN-US"}

[Transaction-id 0x07e0d3]{lang="EN-US"}

[Option               Length  Information ]{lang="EN-US"}

[CLIENTID(1)          10      00030001000fe2ff0000]{lang="EN-US"}

[ORO(6)               12      DOMAIN_LIST(24)]{lang="EN-US"}

[                             DNS_SERVERS(23)]{lang="EN-US"}

[                             SIP_SERVER_A(22)]{lang="EN-US"}

[                             AC-LIST(52)]{lang="EN-US"}

[                             DS-LITE(64)]{lang="EN-US"}

[                             SIP_SERVER_D(21)]{lang="EN-US"}

[ELAPSED_TIME(8)      2       0]{lang="EN-US"}

[*[// DHCPv6]{lang="EN-US"}*]{#struct_0_90630_81574_x916467565}*[客户端发送]{style="font-family:宋体"}[INFORMATION-REQUEST]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Feb 12 10:00:45:696 2013 Sysname DHCPC6/7/Packet: -MDC=1;]{lang="EN-US"}]{#struct_0_90630_81574_x983326183}

[Vlan-interface2, Packet received:]{lang="EN-US"}

[Type Reply(7)]{lang="EN-US"}

[Transaction-id 0x07e0d3]{lang="EN-US"}

[Option               Length  Information ]{lang="EN-US"}

[CLIENTID(1)          10      00030001000fe2ff0000]{lang="EN-US"}

[SERVERID(2)          10      0003000100238963c4ba]{lang="EN-US"}

[DNS-SERVERS(23)      16      1:2:3::5]{lang="EN-US"}

[DOMAIN-LIST(24)      9       abc.com]{lang="EN-US"}

[*[// DHCPv6]{lang="EN-US"}*]{#struct_0_90630_81574_x2120077881}*[客户端收到]{style="font-family:宋体"}[REPLY]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_127098978}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上启动]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的无状态配置，打开事件调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 dhcp client event]{lang="EN-US"}]{#struct_0_90630_81574_x2145117579}

[\*Feb 20 17:37:26:502 2013 Sysname DHCPC6/7/Event: -MDC=1;]{lang="EN-US"}

[[Client information change notified successfully.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_90630_81574_475592214}

[*[//]{lang="EN-US"}*]{#struct_0_90630_81574_x983260647}*[成功通知客户端信息变化]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_x570276796}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[上启动]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的无状态配置，打开错误调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 dhcp client error]{lang="EN-US"}]{#struct_0_90630_81574_x191906441}

[\*Feb 25 09:05:19:102 2013 Sysname DHCPC6/7/Error: -MDC=1;]{lang="EN-US"}

[[Failed to acquire IRT ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_90630_81574_x9826372}

[*[//]{lang="EN-US"}*]{#struct_0_90630_81574_x983457255}*[不能获取]{style="font-family:宋体"}[IRT]{lang="EN-US"}[值]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_x1739218242}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[作为]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端以二报文交互方式申请]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，打开]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端的所有调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging ipv6 dhcp client all]{lang="EN-US"}]{#struct_0_90630_81574_772344130}

[\*Feb  9 14:37:40:312 2013 Sysname DHCPC6/7/Event: -MDC=1;]{lang="EN-US"}

[GigabitEthernet1/0/1: DHCPC6 ADDR FSM state changed from IDLE to SOLICIT successfully.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_x417886704}*[接口]{style="font-family:宋体"}[gigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[ADDR]{lang="EN-US"}[类型的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端从]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[状态转换到]{style="font-family:宋体"}[SOLICIT]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Feb  9 14:37:40:312 2013 Sysname DHCPC6/7/Packet: -MDC=1;]{lang="EN-US"}]{#struct_0_90630_81574_x983064039}

[GigabitEthernet1/0/1, Packet sent:]{lang="EN-US"}

[Type Solicit(1)]{lang="EN-US"}

[Transaction-ID 0xd60e00]{lang="EN-US"}

[Option               Length  Information]{lang="EN-US"}

[RAPID_COMMIT(14)     0]{lang="EN-US"}

[CLIENTID(1)          10      00030001000fe2ff0000]{lang="EN-US"}

[IA_NA(3)             40      IAID: 0xf0019]{lang="EN-US"}

[                             T1: 0]{lang="EN-US"}

[                             T2: 0]{lang="EN-US"}

[IAADDR(5)            24      Address: ::]{lang="EN-US"}

[                             Preferred lifetime: 0]{lang="EN-US"}

[                             Valid lifetime: 0]{lang="EN-US"}

[ORO(6)               12      DOMAIN_LIST(24)]{lang="EN-US"}

[                             DNS_SERVERS(23)]{lang="EN-US"}

[                             SIP_SERVER_A(22)]{lang="EN-US"}

[                             AC-LIST(52)]{lang="EN-US"}

[                             DS-LITE(64)]{lang="EN-US"}

[                             SIP_SERVER_D(21)]{lang="EN-US"}

[ELAPSED_TIME(8)      2       0]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_1373116019}*[发送的报文内容]{style="font-family:宋体"}*

[[\*Feb  9 14:37:40:468 2013 Sysname DHCPC6/7/Packet: -MDC=1;]{lang="EN-US"}]{#struct_0_90630_81574_x982998503}

[GigabitEthernet1/0/1, Packet received:]{lang="EN-US"}

[Type Reply(7)]{lang="EN-US"}

[Transaction-ID 0xd60e00]{lang="EN-US"}

[Option               Length  Information]{lang="EN-US"}

[RAPID_COMMIT(14)     0]{lang="EN-US"}

[CLIENTID(1)          10      00030001000fe2ff0000]{lang="EN-US"}

[SERVERID(2)          14      0003000100238963c4ba]{lang="EN-US"}

[IA_NA(3)             74      IAID: 0xf0019]{lang="EN-US"}

[                             T1: 300]{lang="EN-US"}

[                             T2: 400]{lang="EN-US"}

[IAADDR(5)            24      Address: 100::9DD8:D090:A1A6:7858]{lang="EN-US"}

[                             Preferred lifetime: 500]{lang="EN-US"}

[                             Valid lifetime: 600]{lang="EN-US"}

[STATUS_CODE(13)      30      status-code: Success(0)]{lang="EN-US"}

[DNS_SERVERS(23)      32      2000::FF]{lang="EN-US"}

[                             2000::FE]{lang="EN-US"}

[DOMAIN_LIST(24)      32      example.com]{lang="EN-US"}

[                             example2.test.com]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_x495607689}*[收到应答报文，输出接收到的报文的内容]{style="font-family:宋体"}*

[[\*Feb  9 14:37:40:488 2013 Sysname DHCPC6/7/Event: -MDC=1;]{lang="EN-US"}]{#struct_0_90630_81574_x983588326}

[GigabitEthernet1/0/1: DHCPC6 ADDR FSM state changed from SOLICIT to OPEN successfully.]{lang="EN-US"}

*[// ]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[接口]{style="font-size:10.5pt;
font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US" style="font-size:10.5pt;
font-family:\"Arial\",\"sans-serif\""}[上]{style="font-size:10.5pt;font-family:宋体"}[ADDR]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[类型的]{style="font-size:10.5pt;font-family:宋体"}[DHCPv6]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[客户端从]{style="font-size:10.5pt;font-family:宋体"}[SOLICIT]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[状态转换到]{style="font-size:10.5pt;font-family:宋体"}[OPEN]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}[状态]{style="font-size:10.5pt;font-family:宋体"}*

::: {#709743257 .myid}
[]{#_Toc404786935}[]{#struct_0_90630_81574_286433265}

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp relay**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_90630_81574_1184706521}

[**[debugging ipv6 dhcp relay ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x1989189559}

[**[undo debugging ipv6 dhcp relay]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x983522790}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90630_81574_231431070}

[[用户视图]{style="font-family:宋体"}]{#struct_0_90630_81574_x637732863}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90630_81574_34982893}

[[network-admin]{lang="EN-US"}]{#struct_0_90630_81574_x1121243335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90630_81574_x255390307}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90630_81574_x604769752}

[**[all]{lang="EN-US"}**]{#struct_0_90630_81574_1085868794}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_90630_81574_x983719398}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_90630_81574_x1294527271}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_90630_81574_x332838746}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_90630_81574_x1601796117}

[**[debugging ipv6 dhcp relay]{lang="EN-US"}**]{#struct_0_90630_81574_x659667845}[命令用来打开]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[中继调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 dhcp relay]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[中继调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1571275409}[中继调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging ipv6 dhcp relay packet]{lang="EN-US"}]{#struct_0_90630_81574_x961637607}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x161264608}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_1223643587}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x983653862}

[[From *ipv6-address* port *port*]{lang="EN-US"}]{#struct_0_90630_81574_x916402029}

[[接收报文时表示报文的源地址和端口号]{style="font-family:宋体"}]{#struct_0_90630_81574_685304169}

[[To *ipv6-address* port *port*]{lang="EN-US"}]{#struct_0_90630_81574_x610954502}

[[发送报文时表示报文的目的地址和端口号]{style="font-family:宋体"}]{#struct_0_90630_81574_x983326182}

[[interface *interface-name*]{lang="EN-US"}]{#struct_0_90630_81574_x2120143417}

[[接收或发送报文的接口名称]{style="font-family:宋体"}]{#struct_0_90630_81574_x1357634557}

[[Message type: *message-type*]{lang="EN-US"}]{#struct_0_90630_81574_x230901973}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x1586074024}[消息类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Solicit]{lang="EN-US"}]{#struct_0_90630_81574_x983260646}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_x570342332}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Request]{lang="EN-US"}]{#struct_0_90630_81574_x1751061648}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confirm]{lang="EN-US"}]{#struct_0_90630_81574_467850812}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Renew]{lang="EN-US"}]{#struct_0_90630_81574_x1430946992}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rebind]{lang="EN-US"}]{#struct_0_90630_81574_x983457254}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_90630_81574_x1739152706}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Release ]{lang="EN-US"}]{#struct_0_90630_81574_1363302079}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Decline]{lang="EN-US"}]{#struct_0_90630_81574_469187876}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reconfigure]{lang="EN-US"}]{#struct_0_90630_81574_x983391718}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Information-Request]{lang="EN-US"}]{#struct_0_90630_81574_x157370075}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Relay-Forward]{lang="EN-US"}]{#struct_0_90630_81574_1560408623}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Relay-Reply]{lang="EN-US"}]{#struct_0_90630_81574_903982705}

[[Transaction ID: *transaction-id*]{lang="EN-US"}]{#struct_0_90630_81574_x983064038}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1373050483}[客户端发起申请时生成的一个随机数，用来唯一标示一次申请过程]{style="font-family:宋体"}

[[Hop count: *hops*]{lang="EN-US"}]{#struct_0_90630_81574_1377580287}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x982998502}[报文经过的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的数目，如果是]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[或者是]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文时输出]{style="font-family:宋体"}

[[Link address: *ipv6-address*]{lang="EN-US"}]{#struct_0_90630_81574_x495542153}

[[链路地址，如果]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_853818581}[报文为]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[或]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文，则打印该字段]{style="font-family:宋体"}

[[Peer address: *ipv6-address*]{lang="EN-US"}]{#struct_0_90630_81574_x983588329}

[[对端地址，如果]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_285843441}[报文为]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[或]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文，则打印该字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging ipv6 dhcp relay event]{lang="EN-US"}]{#struct_0_90630_81574_x998553943}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x164898908}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_676710457}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x983522793}

[[Received a short packet from *ipv6-address* port *port-number*, length *length* bytes.]{lang="EN-US"}]{#struct_0_90630_81574_231627678}

[[收到一个来自地址为]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1561846176}[端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的短包]{style="font-family:宋体"}

[[Can not find an interface to process the packet.]{lang="EN-US"}]{#struct_0_90630_81574_x983719401}

[[找不到处理报文的接口，一般为对应的接口没有启用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x2104421168}[功能]{style="font-family:宋体"}

[[Discard the *message-type* message from *ipv6-address* port *port-number*.]{lang="EN-US"}]{#struct_0_90630_81574_x983653865}

[[丢弃从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x916860781}[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[收到的类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Discard the *message-type* message to *ipv6-address* port *port-number*.]{lang="EN-US"}]{#struct_0_90630_81574_x983326185}

[[丢弃发送到地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x983260649}[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[的类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Interface *interface-name* is activated.]{lang="EN-US"}]{#struct_0_90630_81574_x570145724}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x983457257}[被激活]{style="font-family:宋体"}

[[Add an IPv6 address *ipv6-address* to the interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x1739087170}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x1135438882}[添加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*

[[Interface *interface-name* is deactivated.]{lang="EN-US"}]{#struct_0_90630_81574_x983391721}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x156911322}[被去激活]{style="font-family:宋体"}

[[Delete an IPv6 address *ipv6-address* from the interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x983064041}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x982998505}[删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*

[[Interface *interface-name* is deleted.]{lang="EN-US"}]{#struct_0_90630_81574_x983588328}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_285777905}[被删除]{style="font-family:宋体"}

[[The MAC address of interface *interface-name* is changed..]{lang="EN-US"}]{#struct_0_90630_81574_x983522792}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_90630_81574_231562142}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址改变]{style="font-family:宋体"}

[[Invalid packet length.]{lang="EN-US"}]{#struct_0_90630_81574_x983719400}

[[报文长度无效]{style="font-family:宋体"}]{#struct_0_90630_81574_x983653864}

[[Invalid relay message option.]{lang="EN-US"}]{#struct_0_90630_81574_x983326184}

[[报文中的]{style="font-family:宋体"}[relay message option]{lang="EN-US"}]{#struct_0_90630_81574_x2120536633}[选项无效]{style="font-family:宋体"}

[[The length of relay-forward or relay-reply packet is invalid.]{lang="EN-US"}]{#struct_0_90630_81574_x347383994}

[[Relay-forward]{lang="EN-US"}]{#struct_0_90630_81574_x983260648}[或]{style="font-family:宋体"}[Relay-reply]{lang="EN-US"}[报文长度无效]{style="font-family:宋体"}

[[No relay message option.]{lang="EN-US"}]{#struct_0_90630_81574_x570211260}

[[报文中缺少]{style="font-family:宋体"}[relay message option]{lang="EN-US"}]{#struct_0_90630_81574_x983457256}[选项]{style="font-family:宋体"}

[[Relay the *message-type* message from *ipv6-address* port *port-number* to a DHCPv6 server.]{lang="EN-US"}]{#struct_0_90630_81574_x1739021634}

[[将从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x983391720}[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[收到的类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的上行报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器]{style="font-family:宋体"}

[[Relay the *message-type* message from *ipv6-address* port *port-number* to a DHCPv6 client.]{lang="EN-US"}]{#struct_0_90630_81574_x156845786}

[[将从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x983064040}[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[收到的类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的上行报文转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{style="font-family:宋体"}

[[The hop count exceeds the limit.]{lang="EN-US"}]{#struct_0_90630_81574_1372526190}

[[报文中记录的跳数超过最大值]{style="font-family:宋体"}]{#struct_0_90630_81574_x982998504}

[[The relay-reply packet is a multicast packet.]{lang="EN-US"}]{#struct_0_90630_81574_x983588331}

[[收到的]{style="font-family:宋体"}[relay-reply]{lang="EN-US"}]{#struct_0_90630_81574_x983522795}[报文是组播报文]{style="font-family:宋体"}

[[Relay a message with unknown type *message-type-id* to *ipv6-address* port *port-number*.]{lang="EN-US"}]{#struct_0_90630_81574_231234462}

[[转发报文类型为]{style="font-family:宋体"}*[message-type-id]{lang="EN-US"}*]{#struct_0_90630_81574_x983719403}[的未知类型的下行报文到地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*

[[Relay a message with unknown type *message-type-id* from *ipv6-address* port *port-number*.]{lang="EN-US"}]{#struct_0_90630_81574_x983653867}

[[转发从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x916729709}[端口号]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[收到的类型]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}*[message-type-id]{lang="EN-US"}*[的未知类型的上行报文]{style="font-family:宋体"}

[[Unknown interface event *event* is detected on interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x983326187}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x983260651}[检测到不支持的接口事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Unknown IP address event *event* is detected on interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x570670013}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_938594900}[检测到不支持的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging ipv6 dhcp relay error]{lang="EN-US"}]{#struct_0_90630_81574_1059022374}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x145885796}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_x743883808}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_938660436}

[[Error occurs when calculation the value of option *option-code*.]{lang="EN-US"}]{#struct_0_90630_81574_x1086888130}

[[计算选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_90630_81574_938988116}[的选项的值出错]{style="font-family:宋体"}

[[Failed to get IPv6 address of interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x83490141}

[[获取接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_939053652}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址失败]{style="font-family:宋体"}

[[Failed to send packet.]{lang="EN-US"}]{#struct_0_90630_81574_1392402278}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_90630_81574_938857044}

[[Malformed packet dhcp6:]{lang="EN-US"}]{#struct_0_90630_81574_1056620169}

[[option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_90630_81574_x964025143}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_90630_81574_x1763481757}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[Not enough space for option *option-code.*]{lang="EN-US"}]{#struct_0_90630_81574_x2002938637}

[[报文中没有空间存储选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_90630_81574_938922580}[的选项内容]{style="font-family:宋体"}

[[Not enough space for more options.]{lang="EN-US"}]{#struct_0_90630_81574_1828117571}

[[报文中没有空间存储过多的选项]{style="font-family:宋体"}]{#struct_0_90630_81574_939250260}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90630_81574_1679723772}

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_1680845113}[打开]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继的报文调试信息开关。]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端通过]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[中继从]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器获取]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址时，将打印如下信息。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_90630_81574_938725973}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 25 11:51:01:194 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}

[From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Solicit (1)]{lang="EN-US"}

[Transaction ID: 0x00003889]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_2133943548}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到]{style="font-family:宋体"}[Solicit]{lang="EN-US"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[Transaction ID]{lang="FR"}[为]{style="font-family:宋体"}[0x00003889]{lang="FR"}*

[[\*Mar 25 11:51:01:195 2011 Sysname DHCPR6/7/EVENT: Relay the Solicit message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 server.]{lang="EN-US"}]{#struct_0_90630_81574_938594901}

[\*Mar 25 11:51:01:196 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}

[To 2::2 port 547, interface is selected by routing table]{lang="EN-US"}

[Message type: Relay-Forward (12)]{lang="EN-US"}

[Hop count: 0]{lang="EN-US"}

[Link address: 1::1]{lang="EN-US"}

[Peer address: fe80::215:32ff:fe1b:8901]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_1059022375}*[将接收到的]{style="font-family:宋体"}[Solicit]{lang="EN-US"}[报文封装在]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[报文中，并转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器]{style="font-family:宋体"}[2::2]{lang="EN-US"}*

[[\*Mar 25 11:51:01:198 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}]{#struct_0_90630_81574_x743949344}

[From 2::2 port 547, interface GigabitEthernet1/0/2]{lang="EN-US"}

[Message type: Relay-Reply (13)]{lang="EN-US"}

[Hop count: 0]{lang="EN-US"}

[Link address: 1::1]{lang="EN-US"}

[Peer address: fe80::215:32ff:fe1b:8901]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x340579551}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[接收到]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 25 11:51:01:199 2011 Sysname DHCPR6/7/EVENT: Relay the Advertise message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 client.]{lang="EN-US"}]{#struct_0_90630_81574_938660437}

[\*Mar 25 11:51:01:200 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}

[To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Advertise (2)]{lang="EN-US"}

[Transaction ID: 0x00003889]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x1086888131}*[从]{style="font-family:宋体"}[Relay-reply]{lang="EN-US"}[报文中解析出]{style="font-family:宋体"}[Advertise]{lang="EN-US"}[报文，并转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{style="font-family:宋体"}[fe80::215:32ff:fe1b:8901]{lang="EN-US"}[，]{style="font-family:宋体"}[Transaction ID]{lang="FR"}[为]{style="font-family:宋体"}[0x00003889]{lang="FR"}*

[[\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}]{#struct_0_90630_81574_x2030409199}

[From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Request (3)]{lang="EN-US"}

[Transaction ID: 0x0000388a]{lang="EN-US"}

[\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/EVENT: Relay the Request message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 server.]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x1140535829}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到]{style="font-family:宋体"}[Request]{lang="EN-US"}[报文]{style="font-family:宋体"}[，]{style="font-family:宋体"}[Transaction ID]{lang="FR"}[为]{style="font-family:宋体"}[0x0000388a]{lang="FR"}*

[[\*Mar 25 11:51:02:121 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}]{#struct_0_90630_81574_938988117}

[To 2::2 port 547, interface is selected by routing table]{lang="EN-US"}

[Message type: Relay-Forward (12)]{lang="EN-US"}

[Hop count: 0]{lang="EN-US"}

[Link address: 1::1]{lang="EN-US"}

[Peer address: fe80::215:32ff:fe1b:8901]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x83490142}*[将接收到的]{style="font-family:宋体"}[Request]{lang="EN-US"}[报文封装在]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[报文中，并转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器]{style="font-family:宋体"}[2::2]{lang="EN-US"}*

[[\*Mar 25 11:51:02:125 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}]{#struct_0_90630_81574_x453874085}

[From 2::2 port 547, interface GigabitEthernet1/0/2]{lang="EN-US"}

[Message type: Relay-Reply (13)]{lang="EN-US"}

[Hop count: 0]{lang="EN-US"}

[Link address: 1::1]{lang="EN-US"}

[Peer address: fe80::215:32ff:fe1b:8901]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x1362812759}*[从接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[接收到]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Mar 25 11:51:02:126 2011 Sysname DHCPR6/7/EVENT: Relay the Reply message from fe80::215:32ff:fe1b:8901 port 546 to a DHCPv6 client.]{lang="EN-US"}]{#struct_0_90630_81574_939053653}

[\*Mar 25 11:51:02:127 2011 Sysname DHCPR6/7/PACKET:]{lang="EN-US"}

[To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Reply (7)]{lang="EN-US"}

[Transaction ID: 0x0000388a]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_1392402279}*[从]{style="font-family:宋体"}[Relay-reply]{lang="EN-US"}[报文中解析出]{style="font-family:宋体"}[Reply]{lang="EN-US"}[报文，并转发给]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端]{style="font-family:宋体"}[fe80::215:32ff:fe1b:8901]{lang="EN-US"}[，]{style="font-family:宋体"}[Transaction ID]{lang="FR"}[为]{style="font-family:宋体"}[0x0000388a]{lang="FR"}*

::: {#1336858558 .myid}
[]{#_Toc205697826}[]{#_Toc189624764}[]{#_Toc187290810}[]{#_Toc177820253}[]{#OLE_LINK52}[]{#_Toc404786936}[]{#struct_0_90630_81574_x326805133}[]{#_Toc288815457}

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp server**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_90630_81574_x1929796596}

[**[debugging ipv6 dhcp server ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_90630_81574_126996079}

[**[undo debugging ipv6 dhcp server ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x2078190930}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90630_81574_540115532}

[[用户视图]{style="font-family:宋体"}]{#struct_0_90630_81574_x1236051508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90630_81574_x1290051275}

[[network-admin]{lang="EN-US"}]{#struct_0_90630_81574_1807637861}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90630_81574_x1629453965}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90630_81574_x326739597}

[**[all]{lang="EN-US"}**]{#struct_0_90630_81574_1505630967}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的所有调试信息开关]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_90630_81574_703341473}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_90630_81574_1540040770}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_90630_81574_x405060644}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_90630_81574_1640231034}[：表示]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文的详细信息。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_90630_81574_1193130161}

[**[debugging ipv6 dhcp server]{lang="EN-US"}**]{#struct_0_90630_81574_1813993616}[命令用来打开]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}**[undo debugging ipv6 dhcp server]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[DHCPv6]{lang="EN-US"}[服务器的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x1180064210}[服务器的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-7 ]{lang="EN-US"}[debugging ipv6 dhcp server packet]{lang="EN-US"}]{#struct_0_90630_81574_x327329420}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_810118847}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_x1571808660}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_729954476}

[[From *ipv6-address* port *port*]{lang="EN-US"}]{#struct_0_90630_81574_653267190}

[[接收报文时表示报文的源地址和端口号]{style="font-family:宋体"}]{#struct_0_90630_81574_x1663204908}

[[To *ipv6-address* port *port*]{lang="EN-US"}]{#struct_0_90630_81574_20486688}

[[发送报文时表示报文的目的地址和端口号]{style="font-family:宋体"}]{#struct_0_90630_81574_1774049426}

[[interface *interface-name*]{lang="EN-US"}]{#struct_0_90630_81574_1775377301}

[[接收或发送报文的接口名称]{style="font-family:宋体"}]{#struct_0_90630_81574_x327263884}

[[Message type: *message-type*]{lang="EN-US"}]{#struct_0_90630_81574_1537695359}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x1934373426}[消息类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Solicit]{lang="EN-US"}]{#struct_0_90630_81574_929123187}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_90630_81574_x300875299}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Request]{lang="EN-US"}]{#struct_0_90630_81574_x523421452}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Confirm]{lang="EN-US"}]{#struct_0_90630_81574_x327460492}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Renew]{lang="EN-US"}]{#struct_0_90630_81574_x353435297}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rebind]{lang="EN-US"}]{#struct_0_90630_81574_x259609719}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_90630_81574_1437278983}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Release]{lang="EN-US"}]{#struct_0_90630_81574_1327217197}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Decline]{lang="EN-US"}]{#struct_0_90630_81574_x372326530}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reconfigure]{lang="EN-US"}]{#struct_0_90630_81574_x327394956}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Information-Request]{lang="EN-US"}]{#struct_0_90630_81574_1545154192}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Relay-Forward]{lang="EN-US"}]{#struct_0_90630_81574_x652644031}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Relay-Reply]{lang="EN-US"}]{#struct_0_90630_81574_2011373661}

[[Transaction ID: *transaction-id*]{lang="EN-US"}]{#struct_0_90630_81574_1548524078}

[[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x327067276}[客户端发起申请时生成的一个随机数，用来唯一标示一次申请过程]{style="font-family:宋体"}

[[Link address: *ipv6-address*]{lang="EN-US"}]{#struct_0_90630_81574_1595247574}

[[链路地址，如果]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1005899148}[报文为]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[或]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文，则打印该字段]{style="font-family:宋体"}

[[Peer address: *ipv6-address*]{lang="EN-US"}]{#struct_0_90630_81574_1501772889}

[[对端地址，如果]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1352153690}[报文为]{style="font-family:宋体"}[Relay-Forward]{lang="EN-US"}[或]{style="font-family:宋体"}[Relay-Reply]{lang="EN-US"}[报文，则打印该字段]{style="font-family:宋体"}

[[Options:]{lang="EN-US"}]{#struct_0_90630_81574_x327001740}

[[  option *option-name* *option-code*]{lang="EN-US"}]{#struct_0_90630_81574_x349735669}

[[    *option-value*]{lang="EN-US"}]{#struct_0_90630_81574_733524894}

[[报文选项，显示详细报文信息时输出，]{style="font-family:宋体"}*[option-name]{lang="EN-US"}*]{#struct_0_90630_81574_x2063032273}[为报文选项对应的名字，]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*[为选项的数值，]{style="font-family:宋体"}*[option-value]{lang="EN-US"}*[为报文选项的内容]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging ipv6 dhcp server event]{lang="EN-US"}]{#struct_0_90630_81574_17868335}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_806646877}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_x327198348}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x1979800151}

[[Received a short packet from *ipv6-address* port *port-number*, length *length* bytes.]{lang="EN-US"}]{#struct_0_90630_81574_x1104271812}

[[收到一个来自地址为]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1116466363}[端口号为]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*[的短包]{style="font-family:宋体"}

[[Add a conflict IP *ipv6-address*.]{lang="EN-US"}]{#struct_0_90630_81574_936766933}

[[添加冲突地址]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*]{#struct_0_90630_81574_x504741646}

[[Address *ipv6-address* is not bound to client.]{lang="EN-US"}]{#struct_0_90630_81574_x1680120285}

[[地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x327132812}[没有和客户端绑定]{style="font-family:宋体"}

[[Can not find an interface to process the packet.]{lang="EN-US"}]{#struct_0_90630_81574_x1206326772}

[[找不到处理报文的接口，一般为对应的接口没有启用]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_574072504}[功能]{style="font-family:宋体"}

[[Released prefix *ipv6-prefix* is not bound to the client.]{lang="EN-US"}]{#struct_0_90630_81574_x1352280661}

[[客户端请求释放的前缀]{style="font-family:宋体"}]{#struct_0_90630_81574_x1575964876}*[ipv6-]{lang="DA"}[prefix]{lang="EN-US"}*[没有和客户端绑定]{style="font-family:
  宋体"}

[[Client declines address ]{lang="DA"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_2014650374}[.]{lang="DA"}

[[客户端通过]{style="font-family:宋体"}]{#struct_0_90630_81574_x326805132}[Decline]{lang="DA"}[报文报告地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[冲突]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: Client identifier ]{lang="EN-US"}]{#struct_0_90630_81574_x1929862132}[inexistent]{lang="FR"}[.]{lang="EN-US"}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1782025224}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中没有]{style="font-family:宋体"}[client identifier]{lang="EN-US"}

[[Discard *message-type* from *ipv6-address*: ]{lang="EN-US"}]{#struct_0_90630_81574_x1518616966}[Server identifier exists.]{lang="FR"}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_797220748}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中包含]{style="font-family:宋体"}[server identifier]{lang="EN-US"}

[[Discard *message-type* from *ipv6-address*: ]{lang="EN-US"}]{#struct_0_90630_81574_x326739596}[Server identifier inexistent]{lang="FR"}[.]{lang="EN-US"}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1505696503}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中没有]{style="font-family:宋体"}[server identifier]{lang="EN-US"}

[[Discard *message-type* from *ipv6-address*: Server identifier mismatched.]{lang="EN-US"}]{#struct_0_90630_81574_x153809699}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x954916015}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中的]{style="font-family:宋体"}[server identifier]{lang="EN-US"}[不匹配]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: ]{lang="EN-US"}]{#struct_0_90630_81574_1823881037}[IA_NA option exists]{lang="FR"}[.]{lang="EN-US"}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x327329423}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中包含]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: IA_TA option exists..]{lang="EN-US"}]{#struct_0_90630_81574_x1571874196}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_717307488}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中包含]{style="font-family:宋体"}[IA_TA]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: IA_PD option exists.]{lang="EN-US"}]{#struct_0_90630_81574_1540156917}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_13142035}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文中包含]{style="font-family:宋体"}[IA_PD]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: unicast packet.]{lang="EN-US"}]{#struct_0_90630_81574_x327263887}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1537629823}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是报文是单播报文]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: Unsupported message type.]{lang="EN-US"}]{#struct_0_90630_81574_729498899}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x156787919}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是不支持的消息类型]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: Unsupported message type for the stateless server.]{lang="EN-US"}]{#struct_0_90630_81574_x327460495}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x352976545}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是无状态配置服务器不支持的消息类型]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: Failed to find pool.]{lang="EN-US"}]{#struct_0_90630_81574_x1807141048}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_510414530}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是找不到地址池。]{style="font-family:宋体"}

[[Discard message-type from *ipv6-address*: can\'t find the pool.]{lang="EN-US"}]{#struct_0_90630_81574_x327394959}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_1544957584}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是找不到地址池。]{style="font-family:宋体"}

[[Discard message-type from *ipv6-address*: can\'t find the prefix pool.]{lang="EN-US"}]{#struct_0_90630_81574_1276574639}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x257030449}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是找不到前缀地址池。]{style="font-family:宋体"}

[[Discard *message-type* from *ipv6-address*: can't find the network.]{lang="EN-US"}]{#struct_0_90630_81574_875622817}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x327067279}[的消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文。原因是找不到]{style="font-family:宋体"}[network]{lang="EN-US"}[。]{style="font-family:宋体"}

[[Discard unknown packet received from *ipv6-address*.]{lang="EN-US"}]{#struct_0_90630_81574_1594657750}

[[丢弃来自地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_215272706}[的未知报文]{style="font-family:宋体"}

[[Interface *interface-name* is activated.]{lang="EN-US"}]{#struct_0_90630_81574_x1669273542}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x327001743}[被激活]{style="font-family:宋体"}

[[Add an IPv6 address *ipv6-address* to the interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x349539061}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x497800540}[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*

[[Interface *interface-name* is deactivated.]{lang="EN-US"}]{#struct_0_90630_81574_x327198351}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x1979341398}[被去激活]{style="font-family:宋体"}

[[Delete an IPv6 address *ipv6-address* from the interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_139512889}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x1908231249}[删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*

[[Interface *interface-name* is deleted.]{lang="EN-US"}]{#struct_0_90630_81574_x327132815}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x1206785524}[被删除]{style="font-family:宋体"}

[[The MAC address of interface *interface-name* is changed.]{lang="EN-US"}]{#struct_0_90630_81574_123149050}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_90630_81574_x2004151145}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址改变]{style="font-family:宋体"}

[[No IA_NA or IA_TA option needs to be confirmed.]{lang="EN-US"}]{#struct_0_90630_81574_x326805135}

[[报文中没有需要确认的]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}]{#struct_0_90630_81574_x1929665524}[或]{style="font-family:宋体"}[IA_TA]{lang="EN-US"}[选项]{style="font-family:宋体"}

[[Relay-forward from *ipv6-address* with link address *link-address* and peer address *peer-address* misses the relay message option.]{lang="EN-US"}]{#struct_0_90630_81574_x667519686}

[[从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x326739599}[收到的]{style="font-family:宋体"}[Relay-forward]{lang="EN-US"}[报文中没有]{style="font-family:宋体"}[relay message option]{lang="EN-US"}[选项，该报文中的]{style="font-family:宋体"}[link address]{lang="EN-US"}[字段为]{style="font-family:宋体"}*[link-address]{lang="EN-US"}*[和]{style="font-family:宋体"}[peer address]{lang="EN-US"}[字段为]{style="font-family:宋体"}*[peer-address]{lang="EN-US"}*

[[Released address *ipv6-address*.]{lang="EN-US"}]{#struct_0_90630_81574_1506286327}

[[释放地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x672461473}

[[Releases prefix *ipv6-prefix*.]{lang="EN-US"}]{#struct_0_90630_81574_x327329422}

[[释放地址前缀]{style="font-family:宋体"}*[ipv6-prefix]{lang="EN-US"}*]{#struct_0_90630_81574_x1571939732}

[[Send *send-bytes* of *total-bytes* bytes.]{lang="EN-US"}]{#struct_0_90630_81574_998584498}

[[发送了]{style="font-family:宋体"}*[total-bytes]{lang="EN-US"}*]{#struct_0_90630_81574_x327263886}[字节报文中的]{style="font-family:宋体"}*[send-byte]{lang="EN-US"}*[字节数据]{style="font-family:宋体"}

[[Send *message-type* to *ipv6-address*.]{lang="EN-US"}]{#struct_0_90630_81574_1537564287}

[[向地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x1126743533}[发送消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Received *message-type* from *ipv6-address*]{lang="EN-US"}]{#struct_0_90630_81574_x1789895237}

[[从地址]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_90630_81574_x1790026309}[接收到消息类型为]{style="font-family:宋体"}*[message-type]{lang="EN-US"}*[的报文]{style="font-family:宋体"}

[[Unknown interface event *event* is detected on interface *interface-name*.]{lang="EN-US"}]{#struct_0_90630_81574_x327460494}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x353042081}[检测到不支持的接口事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[Detect unknown IP address event *event* on interface *interface-name*. ]{lang="EN-US"}]{#struct_0_90630_81574_x260962201}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_x327394958}[检测到不支持的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging ipv6 dhcp server error]{lang="EN-US"}]{#struct_0_90630_81574_1545023120}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_830699577}[]{#OLE_LINK103}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_x1054027972}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x575148939}

[[Error occurs when calculation the value of option *option-code*.]{lang="EN-US"}]{#struct_0_90630_81574_814767396}

[[计算选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_90630_81574_1014622344}[的选项的值出错]{style="font-family:宋体"}

[[Error occurs when parsing *option-type* option.]{lang="EN-US"}]{#struct_0_90630_81574_x327067278}

[[解析类型为]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*]{#struct_0_90630_81574_1594592214}[的选项失败]{style="font-family:宋体"}

[[Error occurs when calculation the value of *option-type* option.]{lang="EN-US"}]{#struct_0_90630_81574_1786080978}

[[计算选项类型为]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*]{#struct_0_90630_81574_x1294764168}[选项的值出错]{style="font-family:宋体"}

[[Malformed packet dhcp6:]{lang="EN-US"}]{#struct_0_90630_81574_1056489096}

[[option length does not equal its option buffer length.]{lang="EN-US"}]{#struct_0_90630_81574_1056423560}

[[非法的]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_90630_81574_204523194}[报文：服务器选项的实际长度和选项中"]{style="font-family:宋体"}[L]{lang="EN-US"}["字段标识的长度不相等]{style="font-family:宋体"}

[[Failed to allocate a NA lease: Because the number of leases has reached the maximum. ]{lang="EN-US"}]{#struct_0_90630_81574_x840023510}

[[分配]{style="font-family:宋体"}[NA]{lang="EN-US"}]{#struct_0_90630_81574_x1773888562}[租约失败，数量达到上限]{style="font-family:宋体"}

[[Failed to allocate a prefix lease: Because the number of leases has reached the maximum.]{lang="EN-US"}]{#struct_0_90630_81574_x327001742}

[[分配前缀租约失败，数量达到上限]{style="font-family:宋体"}]{#struct_0_90630_81574_x349604597}

[[Failed to get interface address or link address.]{lang="EN-US"}]{#struct_0_90630_81574_x410697941}

[[获取接口地址或者报文链路地址失败]{style="font-family:宋体"}]{#struct_0_90630_81574_x303020162}

[[Failed to add *option-type* option to the packet.]{lang="EN-US"}]{#struct_0_90630_81574_2105667708}

[[向报文中保存]{style="font-family:宋体"}*[option-type]{lang="EN-US"}*]{#struct_0_90630_81574_x1035438724}[选项失败]{style="font-family:宋体"}

[[Failed to send packet.]{lang="EN-US"}]{#struct_0_90630_81574_x327198350}

[[发送报文失败]{style="font-family:宋体"}]{#struct_0_90630_81574_x1979275862}

[[Failed to set *status-code* status code in the reply packet.]{lang="EN-US"}]{#struct_0_90630_81574_x937897489}

[[在]{style="font-family:宋体"}[Reply]{lang="EN-US"}]{#struct_0_90630_81574_2006549838}[报文中设置状态码]{style="font-family:宋体"}*[status-code]{lang="EN-US"}*[失败]{style="font-family:宋体"}

[[No free IP in the address range of the pool..]{lang="EN-US"}]{#struct_0_90630_81574_1805529340}

[[address range]{lang="EN-US"}]{#struct_0_90630_81574_x327132814}[中没有可分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[No free IP in the network *network-address*.]{lang="EN-US"}]{#struct_0_90630_81574_x1206719988}

[[网段]{style="font-family:宋体"}*[network-address]{lang="EN-US"}*]{#struct_0_90630_81574_x2123221131}[中没有可分配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[No free prefix in prefix pool *prefix-pool-index*.]{lang="EN-US"}]{#struct_0_90630_81574_x1399583885}

[[前缀地址池]{style="font-family:宋体"}*[prefix-pool-index]{lang="EN-US"}*]{#struct_0_90630_81574_1834612560}[中没有可分配的前缀]{style="font-family:宋体"}

[[No enough space for option *option-code.*]{lang="EN-US"}]{#struct_0_90630_81574_x326805134}

[[报文中没有空间存储选项编号为]{style="font-family:宋体"}*[option-code]{lang="EN-US"}*]{#struct_0_90630_81574_x1929731060}[的选项内容]{style="font-family:宋体"}

[[No enough space for more options.]{lang="EN-US"}]{#struct_0_90630_81574_40298378}

[[报文中没有空间存储过多的选项]{style="font-family:宋体"}]{#struct_0_90630_81574_x244404515}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90630_81574_60636897}

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_x327281945}[打开]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[服务器的所有调试信息开关。]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[客户端申请]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址时，设备上将打印如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="EN-US"}]{#struct_0_90630_81574_x326739598}

[\<Sysname\> terminal logging level 7]{lang="EN-US"}

[\<Sysname\> debugging ipv6 dhcp server all]{lang="EN-US"}

[\<Sysname\> debugging ipv6 dhcp server packet verbose]{lang="EN-US"}

[\<Sysname\>]{lang="EN-US"}

[\*Mar 25 11:45:06:338 2011 Sysname DHCPS6/7/PACKET:]{lang="EN-US"}

[From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Solicit (1)]{lang="EN-US"}

[Transaction ID: 0x00009c46]{lang="EN-US"}

[Options:]{lang="EN-US"}

[  option client-id 14]{lang="EN-US"}

[    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01]{lang="EN-US"}

[  option ia-na 40]{lang="EN-US"}

[    00:00:00:01:ff:ff:ff:ff:ff:ff:ff:ff:00:05:00:18:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ff:ff:ff:ff:ff:ff:ff:ff]{lang="EN-US"}

[  option elapsed-time 2]{lang="EN-US"}

[    1]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_1506351863}*[服务器收到客户端]{style="font-family:宋体"}[fe80::215:32ff:fe1b:8901]{lang="EN-US"}[发送的]{style="font-family:宋体"}[SOLICIT]{lang="FR"}[消息]{style="font-family:宋体"}[，]{style="font-family:宋体"}[其中携带一个]{style="font-family:宋体"}[IA_NA]{lang="FR"}[选项]{style="font-family:宋体"}*

[[\*Mar 25 11:45:06:339 2011 Sysname DHCPS6/7/EVENT: Send Advertise to fe80::215:32ff:fe1b:8901 port 546.]{lang="EN-US"}]{#struct_0_90630_81574_1594984882}

[\*Mar 25 11:45:06:340 2011 Sysname DHCPS6/7/PACKET:]{lang="EN-US"}

[To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Advertise (2)]{lang="EN-US"}

[Transaction ID: 0x00009c46]{lang="EN-US"}

[Options:]{lang="EN-US"}

[  option client-id 14]{lang="EN-US"}

[    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01]{lang="EN-US"}

[  option server-id 10]{lang="EN-US"}

[    00:03:00:01:00:11:22:33:44:00]{lang="EN-US"}

[  option ia-na 40]{lang="EN-US"}

[    00:00:00:01:00:04:9d:40:00:07:62:00:00:05:00:18:00:01:00:00:00:00:00:00:00:00:00:00:00:00:00:10:00:09:3a:80:00:27:8d:00]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 25 11:45:06:340 2011 Sysname DHCPS6/7/EVENT: Send 80 of 80 bytes.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_x169399815}*[服务器向客户端发送]{style="font-family:宋体"}[ADVERTISE]{lang="EN-US"}[消息，报文中包含为]{style="font-family:宋体"}[IA_NA]{lang="EN-US"}[选项拟分配的地址]{style="font-family:宋体"}[1::10 ]{lang="EN-US"}*

[[\*Mar 25 11:45:06:373 2011 Sysname DHCPS6/7/PACKET:]{lang="EN-US"}]{#struct_0_90630_81574_166785191}

[From fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Request (3)]{lang="EN-US"}

[Transaction ID: 0x00009c47]{lang="EN-US"}

[Options:]{lang="EN-US"}

[  option client-id 14]{lang="EN-US"}

[    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01]{lang="EN-US"}

[  option server-id 10]{lang="EN-US"}

[    00:03:00:01:00:11:22:33:44:00]{lang="EN-US"}

[  option ia-na 40]{lang="EN-US"}

[    00:00:00:01:ff:ff:ff:ff:ff:ff:ff:ff:00:05:00:18:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:ff:ff:ff:ff:ff:ff:ff:ff]{lang="EN-US"}

[  option elapsed-time 2]{lang="EN-US"}

[    3]{lang="EN-US"}

[ ]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_1595050418}*[服务器收到客户端发送的]{style="font-family:宋体"}[REQUEST]{lang="EN-US"}[消息]{style="font-family:宋体"}*

[[%Mar 25 11:45:06:374 2011 Sysname DHCPS6/5/ALLOCATE_IP: Server IP = 1::1, DHCPv6 client IP = 1::10, DHCPv6 client DUID = 0001-0006-b794-1c15-0015-321b-8901, IAID = 00000001, DHCPv6 client lease = 2592000 seconds.]{lang="EN-US"}]{#struct_0_90630_81574_608524461}

[\*Mar 25 11:45:06:374 2011 Sysname DHCPS6/7/EVENT: Send Reply to fe80::215:32ff:fe1b:8901 port 546.]{lang="EN-US"}

[\*Mar 25 11:45:06:375 2011 Sysname DHCPS6/7/PACKET:]{lang="EN-US"}

[To fe80::215:32ff:fe1b:8901 port 546, interface GigabitEthernet1/0/1]{lang="EN-US"}

[Message type: Reply (7)]{lang="EN-US"}

[Transaction ID: 0x00009c47]{lang="EN-US"}

[Options:]{lang="EN-US"}

[  option client-id 14]{lang="EN-US"}

[    00:01:00:06:b7:94:1c:15:00:15:32:1b:89:01]{lang="EN-US"}

[  option server-id 10]{lang="EN-US"}

[    00:03:00:01:00:11:22:33:44:00]{lang="EN-US"}

[  option ia-na 40]{lang="EN-US"}

[    00:00:00:01:00:04:9d:40:00:07:62:00:00:05:00:18:00:01:00:00:00:00:00:00:00:00:00:00:00:00:00:10:00:09:3a:80:00:27:8d:00]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Mar 25 11:45:06:375 2011 Sysname DHCPS6/7/EVENT: Send 80 of 80 bytes.]{lang="EN-US"}

[*[// ]{lang="FR"}*]{#struct_0_90630_81574_x1800786920}*[服务器向客户端发送]{style="font-family:宋体"}[REPLY]{lang="FR"}[消息]{style="font-family:宋体"}[，确认将]{style="font-family:宋体"}[地址]{style="font-family:宋体"}[1::10]{lang="EN-US"}[分配给客户端]{style="font-family:宋体"}*

::: {#-408659621 .myid}
[]{#_Toc404786937}[]{#struct_0_90630_81574_1595247024}[]{#_Toc288816871}[]{#_Toc288816872}[]{#_Toc288816873}[]{#_Toc288816877}[]{#_Toc288816892}[]{#_Toc288816893}[]{#_Toc288816910}[]{#_Toc288816911}[]{#_Toc288816912}[]{#_Toc288816927}[]{#_Toc288816928}[]{#_Toc288816930}

**DHCPv6 \-- DHCPv6调试命令 \-- debugging ipv6 dhcp snooping**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_90630_81574_x1715090041}

[**[debugging ipv6 dhcp snooping ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_x986169981}

[**[undo debugging ipv6 dhcp snooping ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **packet** }]{lang="EN-US"}]{#struct_0_90630_81574_1980503074}

[[【视图】]{style="font-family:黑体"}]{#struct_0_90630_81574_x434175441}

[[用户视图]{style="font-family:宋体"}]{#struct_0_90630_81574_733780741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_90630_81574_1346477771}

[[network-admin]{lang="EN-US"}]{#struct_0_90630_81574_2064776264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_90630_81574_x2061040940}

[[【参数】]{style="font-family:黑体"}]{#struct_0_90630_81574_1595312560}

[**[all]{lang="EN-US"}**]{#struct_0_90630_81574_1393913755}[：表示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_90630_81574_x1842677318}[：表示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_90630_81574_x1970593985}[：表示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_90630_81574_852675872}[：表示]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_90630_81574_x969412037}

[**[debugging ipv6 dhcp snooping]{lang="EN-US"}**]{#struct_0_90630_81574_x2051143045}[命令用来打开]{style="font-family:
宋体"}[DHCPv6 Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}**[undo debugging ipv6 dhcp snooping]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}]{#struct_0_90630_81574_x1224771170}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-10 ]{lang="EN-US"}[debugging ipv6 dhcp snooping error]{lang="EN-US"}]{#struct_0_90630_81574_1595115952}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_854067033}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_x140462495}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_1043605535}

[[Failed to delete IPCIM entries by VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_90630_81574_x1228806720}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x610619958}[删除]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[下的表项失败]{style="font-family:宋体"}

[[Failed to delete IPCIM entries on interface *interface-name*]{lang="EN-US"}]{#struct_0_90630_81574_x1234566368}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x402898388}[删除接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[下的表项失败]{style="font-family:宋体"}

[[Failed to delete an IPCIM entry.]{lang="EN-US"}]{#struct_0_90630_81574_1595181488}

[[通知]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x2146245654}[删除一条]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}[表项失败]{style="font-family:宋体"}

[[Failed to synchronize IPCIM results.]{lang="EN-US"}]{#struct_0_90630_81574_1356765642}

[[同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_1036377517}[结果失败]{style="font-family:宋体"}

[[Failed to synchronize IPCIM.]{lang="EN-US"}]{#struct_0_90630_81574_475838318}

[[同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x581586395}[失败]{style="font-family:宋体"}

[[Insufficient storage space.]{lang="EN-US"}]{#struct_0_90630_81574_1595509168}

[[存储空间不足]{style="font-family:宋体"}]{#struct_0_90630_81574_x1286193516}

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging ipv6 dhcp snooping event]{lang="EN-US"}]{#struct_0_90630_81574_1664828515}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_847714604}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_1466019308}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x78437489}

[[Number of DHCPv6 snooping entries has reached the maximum (interface is *interface-name*)]{lang="EN-US"}]{#struct_0_90630_81574_x1610672373}

[[接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*]{#struct_0_90630_81574_1595574704}[下的]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[表项个数达到最大值]{style="font-family:宋体"}

[[Started to synchronize IPCIM.]{lang="EN-US"}]{#struct_0_90630_81574_982919797}

[[开始同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x1662460623}

[[Finished synchronizing IPCIM.]{lang="EN-US"}]{#struct_0_90630_81574_1598075919}

[[结束同步]{style="font-family:宋体"}[IPCIM]{lang="EN-US"}]{#struct_0_90630_81574_x900286850}

[[Finished recovering entries.]{lang="EN-US"}]{#struct_0_90630_81574_x609035791}

[[表项恢复完成]{style="font-family:宋体"}]{#struct_0_90630_81574_1594984881}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging ipv6 dhcp snooping packet]{lang="EN-US"}]{#struct_0_90630_81574_x169203207}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_849436529}[[字段]{style="font-family:黑体"}]{#struct_0_90630_81574_562462323}

[[描述]{style="font-family:黑体"}]{#struct_0_90630_81574_x1504870031}

[[Received a DHCPv6 *type* packet.]{lang="EN-US"}]{#struct_0_90630_81574_x661766430}

[[收到类型为]{style="font-family:宋体"}]{#struct_0_90630_81574_1700060421}*[type]{lang="EN-US"}*[的]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文，]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文类型为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SOLICIT]{lang="EN-US"}]{#struct_0_90630_81574_x1967315989}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REQUEST]{lang="EN-US"}]{#struct_0_90630_81574_1595050417}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CONFIRM]{lang="EN-US"}]{#struct_0_90630_81574_609376429}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RENEW]{lang="EN-US"}]{#struct_0_90630_81574_1996688516}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REBIND]{lang="EN-US"}]{#struct_0_90630_81574_x1423658094}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RELEASE]{lang="EN-US"}]{#struct_0_90630_81574_426309633}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DECLINE]{lang="EN-US"}]{#struct_0_90630_81574_1594853809}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INFORMATION-REQUEST]{lang="EN-US"}]{#struct_0_90630_81574_x2066286125}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADVERTISE]{lang="EN-US"}]{#struct_0_90630_81574_1630205302}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RECONFIGURE]{lang="EN-US"}]{#struct_0_90630_81574_1244909141}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REPLY]{lang="EN-US"}]{#struct_0_90630_81574_411458598}

[[L3Output: Started to process DHCPv6 packets.]{lang="EN-US"}]{#struct_0_90630_81574_1594919345}

[[三层出方向开始处理报文]{style="font-family:宋体"}]{#struct_0_90630_81574_x2077409770}

[[L3Output: Ignored request packets.]{lang="EN-US"}]{#struct_0_90630_81574_x1983245488}

[[三层出方向请求报文不处理]{style="font-family:宋体"}]{#struct_0_90630_81574_139220701}

[[Started to process DHCPv6 packets.]{lang="EN-US"}]{#struct_0_90630_81574_1658768777}

[[开始处理]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_1595247025}[报文]{style="font-family:宋体"}

[[DHCPv6 packet sent to slot *slot-number*]{lang="EN-US"}]{#struct_0_90630_81574_x1715024505}

[[DHCP]{lang="EN-US"}]{#struct_0_90630_81574_x1721334437}[报文透传主用板]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*

[[Processed a DHCPv6 RELAY-REPLY packet.]{lang="EN-US"}]{#struct_0_90630_81574_1411818419}

[[处理]{style="font-family:宋体"}]{#struct_0_90630_81574_846113012}[DHCPv6 RELAY-REPLY]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Successfully sent packets in VLAN (interface is *interface-name*).]{lang="EN-US"}]{#struct_0_90630_81574_1595312561}

[[VLAN]{lang="EN-US"}]{#struct_0_90630_81574_1393848219}[内的接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[转发报文成功]{style="font-family:宋体"}

[[Failed to send a DHCP packet.]{lang="EN-US"}]{#struct_0_90630_81574_x1013337396}

[[发送]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_90630_81574_1948701636}[报文失败]{style="font-family:宋体"}

[[Sending the packet to all ports in VLAN *vlan-id*.]{lang="EN-US"}]{#struct_0_90630_81574_1595115953}

[[将]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}]{#struct_0_90630_81574_x140528031}[报文发送到]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[内的所有端口]{style="font-family:宋体"}

[[Sending the packet by interface *interface-name* of VLAN *vlan-id.*]{lang="EN-US"}]{#struct_0_90630_81574_x959269370}

[[设备通过]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}]{#struct_0_90630_81574_x1668341219}[内接口]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[转发报文]{style="font-family:宋体"}

[[Started to check validity of the DHCP-request-packet.]{lang="EN-US"}]{#struct_0_90630_81574_1595181489}

[[开始请求方向报文有效性检查]{style="font-family:宋体"}]{#struct_0_90630_81574_x2146180118}

[[Filled option 18 information: Length is *length*, PortIndex is *interface-name* Outer VLAN is *vlan-id,* Inner VLAN is *vlan-id*, DUID is *duid*.]{lang="EN-US"}]{#struct_0_90630_81574_x1226751377}

[[填充]{style="font-family:宋体"}[Option 18]{lang="EN-US"}]{#struct_0_90630_81574_x461551684}[：长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，接口索引是]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，外层]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[，]{style="font-family:宋体"}[DUID]{lang="EN-US"}[是]{style="font-family:宋体"}*[duid]{lang="EN-US"}*

[[Successfully stripped Option *option-id*: Offset is *offset,* Stripped length is *length.*]{lang="EN-US"}]{#struct_0_90630_81574_1595509169}

[[剥离]{style="font-family:宋体"}[Option *option-id*]{lang="EN-US"}]{#struct_0_90630_81574_x1286127980}[，偏移量]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[，剥离长度]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Padded option 18: Offset is *offset.*]{lang="EN-US"}]{#struct_0_90630_81574_x1725252216}

[[在报文中填充]{style="font-family:宋体"}[Option18]{lang="EN-US"}]{#struct_0_90630_81574_736056894}[选项，偏移量]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[Failed to pad option 18.]{lang="EN-US"}]{#struct_0_90630_81574_1595574705}

[[在报文中填充]{style="font-family:宋体"}[Option18]{lang="EN-US"}]{#struct_0_90630_81574_982854261}[选项失败]{style="font-family:宋体"}

[[Failed to strip option 18.]{lang="EN-US"}]{#struct_0_90630_81574_1079392924}

[[在报文中剥离]{style="font-family:宋体"}[Option18]{lang="EN-US"}]{#struct_0_90630_81574_x1864098206}[选项失败]{style="font-family:宋体"}

[[Filled option 37 information: Length is *length* Enterprise number is *number*, PortIndex is *interface-name*, Outer VLAN is *vlan-id*, Inner VLAN is *vlan-id*, DUID is *duid.*]{lang="EN-US"}]{#struct_0_90630_81574_1594984878}

[[填充]{style="font-family:宋体"}[Option 37]{lang="EN-US"}]{#struct_0_90630_81574_x169793034}[：长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*[，厂商标识是]{style="font-family:宋体"}*[number]{lang="EN-US"}*[，接口索引是]{style="font-family:宋体"}*[interface-name]{lang="EN-US"}*[，外层]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[，内层]{style="font-family:宋体"}[VLAN *vlan-id*]{lang="EN-US"}[，]{style="font-family:宋体"}[DUID]{lang="EN-US"}[是]{style="font-family:宋体"}*[duid]{lang="EN-US"}*

[[Padded option 37: Offset is *offset.*]{lang="EN-US"}]{#struct_0_90630_81574_156532539}

[[填充报文]{style="font-family:宋体"}[Option37]{lang="EN-US"}]{#struct_0_90630_81574_1595050414}[，偏移量]{style="font-family:宋体"}*[offset]{lang="EN-US"}*

[[Failed to pad option 37.]{lang="EN-US"}]{#struct_0_90630_81574_609310893}

[[填充]{style="font-family:宋体"}[Option37]{lang="EN-US"}]{#struct_0_90630_81574_137139692}[失败]{style="font-family:宋体"}

[[Failed to strip option 37.]{lang="EN-US"}]{#struct_0_90630_81574_x59182898}

[[剥离]{style="font-family:宋体"}[Option37]{lang="EN-US"}]{#struct_0_90630_81574_1594853806}[失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_90630_81574_x2065303085}

[[\# ]{lang="EN-US"}]{#struct_0_90630_81574_x1136216770}[打开]{style="font-family:宋体"}[DHCPv6 Snooping]{lang="EN-US"}[的报文调试信息开关，并收到]{style="font-family:宋体"}[DHCPv6 Reply]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> terminal debugging]{lang="EN-US"}]{#struct_0_90630_81574_x1518156234}

[\<Sysname\> debugging ipv6 dhcp snooping packet]{lang="EN-US"}

[\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1-Chassis=3-Slot=3; The DHCPv6 ]{lang="EN-US"}

[packet is sent to slot 58.]{lang="EN-US"}

[*[// DHCPv6]{lang="EN-US"}*]{#struct_0_90630_81574_x159518323}*[报文透传至]{style="font-family:宋体"}[58]{lang="EN-US"}[号单板]{style="font-family:宋体"}*

[[\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Started to process DHCPv6 packets.]{lang="EN-US"}]{#struct_0_90630_81574_1594919342}

[*[// DHCPv6 Snooping]{lang="EN-US"}*]{#struct_0_90630_81574_x2076951018}*[预处理报文]{style="font-family:宋体"}*

[[\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Received a DHCPv6 REPLY packet.]{lang="EN-US"}]{#struct_0_90630_81574_865254719}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_455282192}*[接收到]{style="font-family:宋体"}[DHCPv6 Reply]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\*Jun 16 19:45:07:340 2012 H3C DHCPSP6/7/PACKET: -VD=1; Sending the packet to all ports in VLAN 2.]{lang="EN-US"}]{#struct_0_90630_81574_x1952015860}

[*[// ]{lang="EN-US"}*]{#struct_0_90630_81574_x1715442932}*[将]{style="font-family:宋体"}[DHCPv6]{lang="EN-US"}[报文在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内转发]{style="font-family:宋体"}*

[ ]{lang="EN-US"}
