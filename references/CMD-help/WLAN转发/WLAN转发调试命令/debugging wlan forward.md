::: {#-1717150054 .myid}
[]{#_Toc404795299}[]{#struct_0_x8385_17946_x2094079316}[]{#_Toc205700592}[]{#_Toc205697805}

**WLAN转发 \-- WLAN转发调试命令 \-- debugging wlan forward**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x8385_17946_x526739225}

[**[debugging wlan forward]{lang="EN-US"}**[ { **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x8385_17946_x1349575957}

[**[undo debugging wlan forward]{lang="EN-US"}**[ { **all** \| **error** \| **packet** }]{lang="EN-US"}]{#struct_0_x8385_17946_x1836226736}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x8385_17946_x480119106}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x8385_17946_2137986090}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x8385_17946_673652242}

[[network-admin]{lang="EN-US"}]{#struct_0_x8385_17946_x1733435388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x8385_17946_x188392235}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x8385_17946_1631804246}

[**[all]{lang="EN-US"}**]{#struct_0_x8385_17946_x1111408214}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x8385_17946_x1460546499}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发的错误调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x8385_17946_171649337}[：表示]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发的报文调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x8385_17946_x1675279747}

[**[debugging ]{lang="EN-US"}[wlan forward]{lang="EN-US"}**]{#struct_0_x8385_17946_x1052082420}[命令用来打开]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发调试信息开关。]{style="font-family:宋体"}**[undo debugging ]{lang="EN-US"}[wlan forward]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_x8385_17946_1546736224}[转发的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging wlan forward packet]{lang="EN-US"}]{#struct_0_x8385_17946_384600016}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1789780390}[[字段]{style="font-family:黑体"}]{#struct_0_x8385_17946_x1764476082}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x8385_17946_x266135044}

[[Received a frame from a radio.]{lang="EN-US"}]{#struct_0_x8385_17946_29714372}

[[从]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_x8385_17946_1443851252}[收到了帧]{style="font-family:宋体"}

[[Forwarded the frame received from the radio locally.]{lang="EN-US"}]{#struct_0_x8385_17946_2009511788}

[[从]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x8385_17946_1645317151}[口收到帧进行本地转发]{style="font-family:宋体"}

[[Received a frame from the AC.]{lang="EN-US"}]{#struct_0_x8385_17946_976092404}

[[接收来自]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_x8385_17946_287720748}[的帧]{style="font-family:宋体"}

[[Received a frame from the AP.]{lang="EN-US"}]{#struct_0_x8385_17946_1992322899}

[[接收来自]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_x8385_17946_x1675279746}[的帧]{style="font-family:宋体"}

[[Sent a deauthentication frame.]{lang="EN-US"}]{#struct_0_x8385_17946_1676800935}

[[STA]{lang="EN-US"}]{#struct_0_x8385_17946_1095644161}[不存在，发送]{style="font-family:宋体"}[deauth]{lang="EN-US"}[帧]{style="font-family:宋体"}

[[Sent a frame to the BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_315566801}

[[BSS_SND]{lang="EN-US"}]{#struct_0_x8385_17946_1652408744}[：发送帧到]{style="font-family:宋体"}[bss]{lang="EN-US"}

[[Sent a frame for IP or IPv6 forwarding.]{lang="EN-US"}]{#struct_0_x8385_17946_x1949251232}

[[发送帧到]{style="font-family:宋体"}[ip]{lang="EN-US"}]{#struct_0_x8385_17946_x806392512}[或]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[进行转发]{style="font-family:宋体"}

[[Sent a frame to a radio for transmission.]{lang="EN-US"}]{#struct_0_x8385_17946_x1577318452}

[[发送帧到]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_x8385_17946_x1721471261}[进行发送]{style="font-family:宋体"}

[[Received a frame from the WLAN management module to a radio..]{lang="EN-US"}]{#struct_0_x8385_17946_x91219593}

[[接收来自]{style="font-family:宋体"}[WLAN ]{lang="EN-US"}]{#struct_0_x8385_17946_x1675279745}[管理发往]{style="font-family:宋体"}[radio]{lang="EN-US"}[的帧]{style="font-family:宋体"}

[[Received a frame from the WLAN management module to a BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_110716994}

[[接收来自]{style="font-family:宋体"}[WLAN ]{lang="EN-US"}]{#struct_0_x8385_17946_x1194508990}[管理发往]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的帧]{style="font-family:宋体"}

[[Sent a frame to another card.]{lang="EN-US"}]{#struct_0_x8385_17946_2014095157}

[[发送一个帧到别的板]{style="font-family:宋体"}]{#struct_0_x8385_17946_x1084926342}

[[The radio-based service dropped a frame. Phase for the service is *phase*. Service ID is *sid*. Position for the service in the MAP is *bitmap*. Result is *result*.]{lang="EN-US"}]{#struct_0_x8385_17946_x1479236248}

[[进行基于]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x8385_17946_884386538}[口的业务处理并释放帧]{style="font-family:宋体"}

[*[phase]{lang="EN-US"}*]{#struct_0_x8385_17946_x1890385778}[表示业务的阶段，]{style="font-family:宋体"}*[sid]{lang="EN-US"}*[表示业务的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}*[bitmap]{lang="EN-US"}*[表示业务在]{style="font-family:宋体"}[MAP]{lang="EN-US"}[中的位置，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[表示业务处理结果]{style="font-family:宋体"}

[*[result]{lang="EN-US"}*]{#struct_0_x8385_17946_x1675279744}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x8385_17946_x1455366947}[：报文已经被业务丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x8385_17946_x1196651513}[：报文已经被业务消费处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x8385_17946_x205301057}[：报文已经被业务放入队列]{style="font-family:宋体"}

[[The BSS-based service dropped a frame. Phase for the service is *phase*. Service ID is *sid*. Position for the service in the MAP is *bitmap*. Result is *result*.]{lang="EN-US"}]{#struct_0_x8385_17946_x934386271}

[[进行基于]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_x230360829}[的业务处理并释放帧]{style="font-family:宋体"}

[*[phase]{lang="EN-US"}*]{#struct_0_x8385_17946_x1199775180}[表示业务的阶段，]{style="font-family:宋体"}*[sid]{lang="EN-US"}*[表示业务的]{style="font-family:宋体"}*[ID]{lang="EN-US"}*[，]{style="font-family:宋体"}*[bitmap]{lang="EN-US"}*[表示业务在]{style="font-family:宋体"}[MAP]{lang="EN-US"}[中的位置，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[表示业务处理结果。]{style="font-family:宋体"}

[*[result]{lang="EN-US"}*]{#struct_0_x8385_17946_x2122197425}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x8385_17946_x1675279743}[：报文已经被业务丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x8385_17946_917286048}[：报文已经被业务消费处理]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x8385_17946_x802598001}[：报文已经被业务放入队列]{style="font-family:宋体"}

[[Received a CAPWAP fragment. Fragments received are not complete.]{lang="EN-US"}]{#struct_0_x8385_17946_597726747}

[[收到一个]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_1778215749}[分片报文，且分片报文没有收全]{style="font-family:宋体"}

[[Received a CAPWAP control packet. ]{lang="EN-US"}]{#struct_0_x8385_17946_1457427229}

[[收到]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_x8385_17946_x812780462}[CAPWAP]{lang="EN-US" style="font-size:10.0pt;font-family:\"Segoe UI\",\"sans-serif\";
  color:black"}[控制报文]{style="font-size:10.0pt;font-family:宋体;
  color:black"}

[[BSS sent a packet it intercepted to the Packet Socket.]{lang="EN-US"}]{#struct_0_x8385_17946_663372408}

[[报文被]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_x1224661990}[侦听上送到]{style="font-family:宋体"}[Packet Socket]{lang="EN-US"}

[[Radio sent a packet it intercepted to the Packet Socket.]{lang="EN-US"}]{#struct_0_x8385_17946_x717316774}

[[报文被]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_x8385_17946_x621102198}[侦听上送到]{style="font-family:宋体"}[Packet Socket]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging wlan forward error]{lang="EN-US"}]{#struct_0_x8385_17946_x1647318527}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1781684920}[[字段]{style="font-family:黑体"}]{#struct_0_x8385_17946_x1018985227}

[[描述]{style="font-family:黑体"}]{#struct_0_x8385_17946_x358645472}

[[Failed to get BSS *bssid* info from the CAPWAP frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x272651323}

[[Capwap]{lang="EN-US"}]{#struct_0_x8385_17946_17927716}[帧处理过程中，根据]{style="font-family:宋体"}*[bssid]{lang="EN-US"}*[获取]{style="font-family:宋体"}[BSS]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Failed to parse the DOT11 frame from the WLAN management module to a radio.]{lang="EN-US"}]{#struct_0_x8385_17946_663372409}

[[解析来自]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_x8385_17946_x1224661989}[管理发往]{style="font-family:宋体"}[radio]{lang="EN-US"}[的]{style="font-family:宋体"}[dot11]{lang="EN-US"}[帧失败]{style="font-family:宋体"}

[[Failed to parse the DOT11 frame from the WLAN management module to a BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_1204931991}

[[解析来自]{style="font-family:宋体"}[WLAN]{lang="EN-US"}]{#struct_0_x8385_17946_x907045017}[管理发往]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的]{style="font-family:宋体"}[dot11]{lang="EN-US"}[帧失败]{style="font-family:宋体"}

[[Failed to parse the frame from a tunnel.]{lang="EN-US"}]{#struct_0_x8385_17946_2080192388}

[[解析来自]{style="font-family:宋体"}[tunnel]{lang="EN-US"}]{#struct_0_x8385_17946_x1511489182}[的帧失败]{style="font-family:宋体"}

[[Failed to send the data frame for Layer 2 forwarding.]{lang="EN-US"}]{#struct_0_x8385_17946_1528485082}

[[发送数据帧给]{style="font-family:宋体"}[mac]{lang="EN-US"}]{#struct_0_x8385_17946_457954706}[做二层转发失败]{style="font-family:宋体"}

[[Failed to convert the format of the unicast frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x1928239309}

[[单播数据帧格式转换失败]{style="font-family:宋体"}]{#struct_0_x8385_17946_x1958293961}

[[Failed to get BSS *bssid* info from the data frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x1880383228}

[[数据帧处理过程中，获取]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_663372410}[信息失败]{style="font-family:宋体"}

[[Failed to get BSS *bssid* info from the management frame.]{lang="EN-US"}]{#struct_0_x8385_17946_731653154}

[[管理帧处理过程中，获取]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_1574139493}[信息失败]{style="font-family:宋体"}

[[Failed to get radio info.]{lang="EN-US"}]{#struct_0_x8385_17946_1924143979}

[[获取]{style="font-family:宋体"}[radio]{lang="EN-US"}]{#struct_0_x8385_17946_392466837}[信息失败]{style="font-family:宋体"}

[[Failed to get BSS *bssid* info.]{lang="EN-US"}]{#struct_0_x8385_17946_x1990143875}

[[获取]{style="font-family:宋体"}*[bssid]{lang="EN-US"}*]{#struct_0_x8385_17946_99547261}[的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[信息失败]{style="font-family:宋体"}

[[Failed to send the data frame for IP or IPv6 forwarding.]{lang="EN-US"}]{#struct_0_x8385_17946_x813802855}

[[发送数据帧做]{style="font-family:宋体"}[ip]{lang="EN-US"}]{#struct_0_x8385_17946_663372411}[或]{style="font-family:宋体"}[ipv6]{lang="EN-US"}[转发失败]{style="font-family:宋体"}

[[Dropped a management frame with a broadcast, multicast, or all-zero source MAC address.]{lang="EN-US"}]{#struct_0_x8385_17946_731653155}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_1574139494}[管理帧，丢弃，因为源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[是组播、广播或全零]{style="font-family:宋体"}

[[Dropped a data frame with a wrong protocol version.]{lang="EN-US"}]{#struct_0_x8385_17946_1924078443}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_1113970876}[数据帧，丢弃，因为版本号错误]{style="font-family:宋体"}

[[Dropped a data frame with an unsupported subtype *subtype*.]{lang="EN-US"}]{#struct_0_x8385_17946_60097537}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_82419366}[数据帧，丢弃，因为子类型不被支持]{style="font-family:宋体"}

[*[subtype]{lang="EN-US"}*]{#struct_0_x8385_17946_x308446905}[目前我们只支持：]{style="font-family:宋体"}

[[DOT11_FRAME_SUBTYPE_DATA]{lang="EN-US"}]{#struct_0_x8385_17946_663372412}[：子类型为]{style="font-family:宋体"}[Data]{lang="EN-US"}[的数据帧]{style="font-family:宋体"}

[[DOT11_FRAME_SUBTYPE_QOS_DATA]{lang="EN-US"}]{#struct_0_x8385_17946_731653156}[：子类型为]{style="font-family:宋体"}[QOS]{lang="EN-US"}[的数据帧]{style="font-family:宋体"}

[[Dropped a management frame with an unsupported subtype.]{lang="EN-US"}]{#struct_0_x8385_17946_1574139495}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_1924012907}[管理帧，丢弃，因为子类型不被支持]{style="font-family:宋体"}

[[Dropped a data frame with a broadcast, multicast, or all-zero source MAC address.]{lang="EN-US"}]{#struct_0_x8385_17946_1967922454}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_882785248}[数据帧，丢弃，因为源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[是广播、组播或全零]{style="font-family:宋体"}

[[Dropped a frame with the same source MAC address and BSSID.]{lang="EN-US"}]{#struct_0_x8385_17946_663372413}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_731653157}[帧，丢弃，因为源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[和]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[相同]{style="font-family:宋体"}

[[Dropped a frame with different destination MAC address and BSSID.]{lang="EN-US"}]{#struct_0_x8385_17946_1574139496}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_1923947371}[管理帧，丢弃，因为目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[和]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[不相同]{style="font-family:宋体"}

[[The client doesn\'t belong to BSS *bssid* for the data frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x651706847}

[[STA]{lang="EN-US"}]{#struct_0_x8385_17946_663372414}[用户不属于此数据帧的]{style="font-family:宋体"}*[bssid]{lang="EN-US"}*[对应的]{style="font-family:宋体"}[BSS ]{lang="EN-US"}

[[The client doesn\'t belong to BSS *bssid* for the management frame.]{lang="EN-US"}]{#struct_0_x8385_17946_731653150}

[[STA]{lang="EN-US"}]{#struct_0_x8385_17946_1574139489}[用户不属于此管理帧的]{style="font-family:宋体"}*[bssid]{lang="EN-US"}*[对应的]{style="font-family:宋体"}[BSS]{lang="EN-US"}

[[The radio is not up.]{lang="EN-US"}]{#struct_0_x8385_17946_1924799340}

[[Radio]{lang="EN-US"}]{#struct_0_x8385_17946_759254262}[状态没有]{style="font-family:宋体"}[up]{lang="EN-US"}

[[Failed to get the tunnel info..]{lang="EN-US"}]{#struct_0_x8385_17946_663372415}

[[Tunnel]{lang="EN-US"}]{#struct_0_x8385_17946_731653151}[不存在]{style="font-family:宋体"}

[[Failed to get the client info.]{lang="EN-US"}]{#struct_0_x8385_17946_1574139490}

[[STA]{lang="EN-US"}]{#struct_0_x8385_17946_1924340587}[不存在]{style="font-family:宋体"}

[[Failed to get the forwarding info from the BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_663372416}

[[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_731653152}[中转发信息不存在]{style="font-family:宋体"}

[[Invalid forwarding type.]{lang="EN-US"}]{#struct_0_x8385_17946_1574139491}

[[获取到的转发类型非法]{style="font-family:宋体"}]{#struct_0_x8385_17946_1924275051}

[[Invalid frame type.]{lang="EN-US"}]{#struct_0_x8385_17946_396482132}

[[非法的帧类型]{style="font-family:宋体"}]{#struct_0_x8385_17946_663372417}

[[The frame is too short.]{lang="EN-US"}]{#struct_0_x8385_17946_731653153}

[[帧长度过小]{style="font-family:宋体"}]{#struct_0_x8385_17946_1574139492}

[[Failed to get radio info by the radio ID and the WLAN ID.]{lang="EN-US"}]{#struct_0_x8385_17946_1924209515}

[[无法通过]{style="font-family:宋体"}[RID]{lang="EN-US"}]{#struct_0_x8385_17946_1887260052}[和]{style="font-family:宋体"}[WLAN ID]{lang="EN-US"}[获取]{style="font-family:宋体"}[Radio]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[WLAN forwarding dropped a frame because the BSS failed to process the frame.]{lang="EN-US"}]{#struct_0_x8385_17946_1852850808}

[[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_x574020599}[侦听处理失败，]{style="font-family:宋体"}[WLANFW]{lang="EN-US"}[丢弃了帧]{style="font-family:宋体"}

[[BSS accepted a frame it intercepted.]{lang="EN-US"}]{#struct_0_x8385_17946_x1235943021}

[[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_1750341795}[侦听接管了帧]{style="font-family:宋体"}

[[The frame sent for Layer 2 forwarding is not a data frame.]{lang="EN-US"}]{#struct_0_x8385_17946_1852850809}

[[发往]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x8385_17946_x573955063}[转发的]{style="font-family:宋体"}[DOT11]{lang="EN-US"}[帧不是一个数据帧]{style="font-family:宋体"}

[[The radio ID in the data frame is different from the radio ID in the BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_67133618}

[[数据帧的]{style="font-family:宋体"}[radio ID]{lang="EN-US"}]{#struct_0_x8385_17946_1424850917}[和]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中]{style="font-family:宋体"}[radio]{lang="EN-US"}[成员的]{style="font-family:宋体"}[ID]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[The radio ID in the management frame is different from the radio ID in the BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_238170839}

[[管理帧的]{style="font-family:宋体"}[radio ID]{lang="EN-US"}]{#struct_0_x8385_17946_1852850810}[和]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中]{style="font-family:宋体"}[radio]{lang="EN-US"}[成员的]{style="font-family:宋体"}[ID]{lang="EN-US"}[不一致]{style="font-family:宋体"}

[[Invalid frame with multiple CAPWAP headers.]{lang="EN-US"}]{#struct_0_x8385_17946_x574544888}

[[进行了多次]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_756208851}[头封装的非法帧]{style="font-family:宋体"}

[[The CAPWAP frame is too short.]{lang="EN-US"}]{#struct_0_x8385_17946_x422603410}

[[Capwap]{lang="EN-US"}]{#struct_0_x8385_17946_1852850811}[帧长度过短]{style="font-family:宋体"}

[[The frame type doesn\'t match the forwarding policy.]{lang="EN-US"}]{#struct_0_x8385_17946_x574479352}

[[帧类型和转发策略不匹配]{style="font-family:宋体"}]{#struct_0_x8385_17946_x1170478832}

[[Dropped a management frame with an unsupported subtype.]{lang="EN-US"}]{#struct_0_x8385_17946_1768501966}

[[收到]{style="font-family:宋体"}[DOT11]{lang="EN-US"}]{#struct_0_x8385_17946_1852850812}[管理帧，丢弃，因为子类型不被支持]{style="font-family:宋体"}

[[There is no client in BSS *bssid*.]{lang="EN-US"}]{#struct_0_x8385_17946_x574413816}

[*[bssid]{lang="EN-US"}*]{#struct_0_x8385_17946_1144878874}[对应的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[中没有用户]{style="font-family:宋体"}

[[QoS frame discarded because it was sent by a non-QoS client.]{lang="EN-US"}]{#struct_0_x8385_17946_x1968379989}

[[收到非]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x8385_17946_1852850813}[类型的]{style="font-family:宋体"}[STA]{lang="EN-US"}[发送的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[帧，丢弃该]{style="font-family:宋体"}[QoS]{lang="EN-US"}[帧]{style="font-family:宋体"}

[[Radio received a mesh frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x574348280}

[[Radio]{lang="EN-US"}]{#struct_0_x8385_17946_x778085027}[收到一个]{style="font-family:宋体"}[mesh]{lang="EN-US"}[类型的帧]{style="font-family:宋体"}

[[Received a frame with invalid format from the BSS.]{lang="EN-US"}]{#struct_0_x8385_17946_288907117}

[[从]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x8385_17946_1852850814}[中获取的帧格式非法]{style="font-family:宋体"}

[[The frame is too large to be fragmented.]{lang="EN-US"}]{#struct_0_x8385_17946_x574282744}

[[帧太大无法被分片]{style="font-family:宋体"}]{#struct_0_x8385_17946_x483202290}

[[Received a duplicate fragment.]{lang="EN-US"}]{#struct_0_x8385_17946_1852850815}

[[收到重复的分片报文]{style="font-family:宋体"}]{#struct_0_x8385_17946_x574217208}

[[Number of received fragments reached the limit. There are more fragments to be sent.]{lang="EN-US"}]{#struct_0_x8385_17946_323176675}

[[接收的分片报文数已达到允许最大值，但是还有更多的分片]{style="font-family:宋体"}]{#struct_0_x8385_17946_1852850816}

[[Fragments out of sequence.]{lang="EN-US"}]{#struct_0_x8385_17946_x574151672}

[[分片报文的顺序不正确]{style="font-family:宋体"}]{#struct_0_x8385_17946_1902677341}

[[Number of reassembly queues reached the limit. Can\'t add another reassembly queue. ]{lang="EN-US"}]{#struct_0_x8385_17946_1852850817}

[[重组队列达到了临界值，不能再增加重组队列了]{style="font-family:宋体"}]{#struct_0_x8385_17946_x574086136}

[[Received an invalid CAPWAP fragment.]{lang="EN-US"}]{#struct_0_x8385_17946_1459928383}

[[收到非法的]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_x103464328}[分片报文]{style="font-family:宋体"}

[[Dropped a CAPWAP frame with an invalid radio MAC address.]{lang="EN-US"}]{#struct_0_x8385_17946_x103693360}

[[收到]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_x882017013}[报文丢弃，因为]{style="font-family:宋体"}[Radio mac]{lang="EN-US"}[字段不合法]{style="font-family:宋体"}

[[Dropped a CAPWAP frame with an invalid W field.]{lang="EN-US"}]{#struct_0_x8385_17946_x103464327}

[[收到]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_x102710320}[报文丢弃，因为]{style="font-family:宋体"}[W]{lang="EN-US"}[字段不合法]{style="font-family:宋体"}

[[Dropped a CAPWAP frame with no wireless specific information.]{lang="EN-US"}]{#struct_0_x8385_17946_x2067795577}

[[丢弃]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_x103464326}[帧，由于]{style="font-family:宋体"}[CAPWAP]{lang="EN-US"}[头中未携带无线信息选项]{style="font-family:宋体"}

[[Dropped a CAPWAP frame with wrong header length.]{lang="EN-US"}]{#struct_0_x8385_17946_x102775856}

[[收到]{style="font-family:宋体"}[Capwap]{lang="EN-US"}]{#struct_0_x8385_17946_x1268369271}[报文丢弃，因为报文的头长度字段与实际的头长度不相等]{style="font-family:宋体"}

[[Failed to create a fragment node.]{lang="EN-US"}]{#struct_0_x8385_17946_x103464325}

[[创建分片节点失败]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_x8385_17946_x102841392}

[[Failed to create a fragment management node.]{lang="EN-US"}]{#struct_0_x8385_17946_658663048}

[[创建分片管理节点失败]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_x8385_17946_x103464324}

[[Failed to convert the format of the frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x102906928}

[[帧格式转换失败]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_x8385_17946_x103464323}

[[Failed to encrypt the data frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x102972464}

[[数据帧加密失败]{style="font-size:10.0pt;font-family:宋体;color:black"}]{#struct_0_x8385_17946_1869088907}

[[Failed to add the TKIP MIC into the frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x103464322}

[[向帧中添加]{style="font-family:宋体"}[TKIP MIC]{lang="EN-US"}]{#struct_0_x8385_17946_x103038000}[失败]{style="font-family:宋体"}

[[Failed to decrypt the data frame.]{lang="EN-US"}]{#struct_0_x8385_17946_650745174}

[[数据帧解密失败]{style="font-family:宋体"}]{#struct_0_x8385_17946_x103464321}

[[Invalid TKIP MIC.]{lang="EN-US"}]{#struct_0_x8385_17946_x103103536}

[[TKIP MIC]{lang="EN-US"}]{#struct_0_x8385_17946_288783427}[非法]{style="font-family:宋体"}

[[Invalid W field in the CAPWAP frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x103464320}

[[CAPWAP]{lang="EN-US"}]{#struct_0_x8385_17946_x103169072}[帧中的]{style="font-family:宋体"}[W]{lang="EN-US"}[字段非法]{style="font-family:宋体"}

[[Failed to get forwarding info from the tunnel. ]{lang="EN-US"}]{#struct_0_x8385_17946_x103464319}

[[从隧道中获取转发信息失败]{style="font-family:宋体"}]{#struct_0_x8385_17946_x103627827}

[[Dropped the frame because of too many encapsulations.]{lang="EN-US"}]{#struct_0_x8385_17946_x1631826061}

[[帧封装次数过多，丢弃报文]{style="font-family:宋体"}]{#struct_0_x8385_17946_x2059779464}

[[Failed to decrypt the management frame.]{lang="EN-US"}]{#struct_0_x8385_17946_372057260}

[[管理帧解密失败]{style="font-family:宋体"}]{#struct_0_x8385_17946_x1468263176}

[[Failed to encrypt the management frame.]{lang="EN-US"}]{#struct_0_x8385_17946_x2059779463}

[[管理帧加密失败]{style="font-family:宋体"}]{#struct_0_x8385_17946_775341787}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x8385_17946_1445648996}

[[\# ]{lang="EN-US"}]{#struct_0_x8385_17946_715974771}[在]{style="font-family:宋体"}[AC]{lang="EN-US"}[，]{style="font-family:宋体"}[AP]{lang="EN-US"}[上打开]{style="font-family:宋体"}[WLAN]{lang="EN-US"}[转发的所有调试开关，]{style="font-family:宋体"}[STA]{lang="EN-US"}[发送一个报文给]{style="font-family:宋体"}[ PC]{lang="EN-US"}[，将输出如下调试信息。]{style="font-family:宋体"}

[[\*May  4 10:19:37:470 2015 H3C WLANFW/7/PACKET:]{lang="EN-US"}]{#struct_0_x8385_17946_1809373834}

[interface = WLAN-Radio1/0/1 payload =]{lang="EN-US"}

[08 01 2C 00 00 0F E2 00 12 81 9C D3 6D 9D EA 85]{lang="EN-US"}

[08 2E 5F 2B 22 FE 70 09 AA AA 03 00 00 00 08 00]{lang="EN-US"}

[45 00 00 3C C4 6F 00 00 80 01 F2 75 C0 A8 01 07]{lang="EN-US"}

[C0 A8 01 84 08 00 48 5C 04 00 01 00 61 62 63 64]{lang="EN-US"}

[65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74]{lang="EN-US"}

[75 76 77 61 62 63 64 65 66 67 68 69]{lang="EN-US"}

[prompt: Received a frame from a radio.]{lang="EN-US"}

[*[// AP]{lang="EN-US"}*]{#struct_0_x8385_17946_931114869}*[收到一个报文，接收接口为]{style="font-family:宋体"}[WLAN-Radio1/0/1]{lang="EN-US"}*

[[\*May  4 10:19:37:470 2015 H3C WLANFW/7/PACKET:]{lang="EN-US"}]{#struct_0_x8385_17946_x2059779462}

[payload =]{lang="EN-US"}

[45 00 00 88 71 B6 00 00 FF 11 00 00 C0 A8 01 0E]{lang="EN-US"}

[C0 A8 01 0D 6D 40 14 7F 00 74 00 00 00 20 43 20]{lang="EN-US"}

[00 00 00 00 04 00 00 00 00 00 00 00 08 01 2C 00]{lang="EN-US"}

[00 0F E2 00 12 81 9C D3 6D 9D EA 85 08 2E 5F 2B]{lang="EN-US"}

[22 FE 70 09 AA AA 03 00 00 00 08 00 45 00 00 3C]{lang="EN-US"}

[C4 6F 00 00 80 01 F2 75 C0 A8 01 07 C0 A8 01 84]{lang="EN-US"}

[08 00 48 5C 04 00 01 00 61 62 63 64 65 66 67 68]{lang="EN-US"}

[69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 61]{lang="EN-US"}

[prompt: Sent a frame for IP or IPv6 forwarding.]{lang="EN-US"}

[*[// AP]{lang="EN-US"}*]{#struct_0_x8385_17946_x790742154}*[把报文通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[转发发送出去]{style="font-family:宋体"}*

[[\*May 20 10:45:08:919 2014 H3C WLANFW/7/PACKET:]{lang="EN-US"}]{#struct_0_x8385_17946_x452772588}

[interface = Vlan-interface1 payload =]{lang="EN-US"}

[45 00 00 88 71 B8 00 00 FF 11 C6 40 C0 A8 01 0E]{lang="EN-US"}

[C0 A8 01 0D 6D 40 14 7F 00 74 00 00 00 20 43 20]{lang="EN-US"}

[00 00 00 00 04 00 00 00 00 00 00 00 08 01 2C 00]{lang="EN-US"}

[00 0F E2 00 12 81 9C D3 6D 9D EA 85 08 2E 5F 2B]{lang="EN-US"}

[22 FE 90 09 AA AA 03 00 00 00 08 00 45 00 00 3C]{lang="EN-US"}

[C4 A0 00 00 80 01 F2 44 C0 A8 01 07 C0 A8 01 84]{lang="EN-US"}

[08 00 46 5C 04 00 03 00 61 62 63 64 65 66 67 68]{lang="EN-US"}

[69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 61]{lang="EN-US"}

[prompt: Received a frame from AP.]{lang="EN-US"}

[*[// AC]{lang="EN-US"}*]{#struct_0_x8385_17946_589105534}*[收到一个来自]{style="font-family:宋体"}[AP]{lang="EN-US"}[的报文，接收接口为]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}*
