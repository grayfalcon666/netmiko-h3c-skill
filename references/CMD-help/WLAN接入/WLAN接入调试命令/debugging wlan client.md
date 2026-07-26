::: {#2010852181 .myid}
[]{#_Toc404794856}[]{#struct_0_16776_x1311_x1832812258}

**WLAN接入 \-- WLAN接入调试命令 \-- debugging wlan client**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x463447814}

[**[debugging wlan client]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_16776_x1311_x224243328}

[**[undo debugging wlan client ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **fsm** \| **timer** \| **packet** { **receive** \| **send** } \[ **verbose** \] }]{lang="EN-US"}]{#struct_0_16776_x1311_1109941893}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16776_x1311_1384748903}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1641229767}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1005355950}

[[network-admin]{lang="EN-US"}]{#struct_0_16776_x1311_x2132087516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16776_x1311_x340317507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x654980634}

[**[all]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_294011474}[：表示客户端所有类型的调试开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_x1957403516}[：表示客户端错误类型的调试开关。]{style="font-family:
宋体"}

[**[event]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_2058870511}[：表示客户端事件类型的调试开关。]{style="font-family:
宋体"}

[**[fsm]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_x1140648055}[：表示客户端状态机类型调试开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_1455689021}[：表示客户端定时器类型调试开关。]{style="font-family:
宋体"}

[**[packet receive]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_x1168354038}[：表示客户端接收报文的调试开关。]{style="font-family:宋体"}

[**[packet send]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_406763046}[：表示客户端发送报文的调试开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_x575062131}[：显示详细的调试信息，如果不指定，显示简要的调试信息。]{style="font-family:
宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x426972461}

[**[debugging wlan client]{lang="EN-US"}**]{#struct_0_16776_x1311_1619913453}[命令用来打开客户端调试信息开关。]{style="font-family:宋体"}**[undo debugging wlan client]{lang="EN-US"}**[命令用来关闭客户端调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，客户端调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_16776_x1311_x2142722513}

[[表1-1 ]{lang="EN-US"}[debugging wlan client ]{lang="EN-US"}[error]{lang="EN-US"}]{#struct_0_16776_x1311_294011475}[命令输出信息描述表（]{style="font-family:黑体"}[AC/FAT AP]{lang="EN-US"}[）]{style="font-family:黑体"}

[]{#table_struct_0_x1316116862}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1957403517}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x670012844}

[[Failed to send the (re)association response.]{lang="EN-US"}]{#struct_0_16776_x1311_x885527860}

[[发送（重）关联回应失败]{style="font-family:宋体"}]{#struct_0_16776_x1311_1886823070}

[[Failed to send the delete mobile message to the uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_574357972}

[[上行同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_414207147}[消息失败]{style="font-family:宋体"}

[[Failed to enable packet socket for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_16776_x1311_902472553}

[[使能]{style="font-family:宋体"}[BSS *BSSID*]{lang="EN-US"}]{#struct_0_16776_x1311_294011472}[的]{style="font-family:宋体"}[packet socket ]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to assign the port to a VLAN when creating a BSS.]{lang="EN-US"}]{#struct_0_16776_x1311_x1957403514}

[[创建]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_16776_x1311_x1073297371}[时向端口添加]{style="font-family:宋体"}[Vlan]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[Failed to remove the port from a VLAN.]{lang="EN-US"}]{#struct_0_16776_x1311_x1312224056}

[[端口退出]{style="font-family:宋体"}[Vlan]{lang="EN-US"}]{#struct_0_16776_x1311_495890030}[失败]{style="font-family:宋体"}

[[Failed to inform service *service* of AP event.]{lang="EN-US"}]{#struct_0_16776_x1311_x454553915}

[[向业务模块]{style="font-family:宋体"}*[service]{lang="EN-US"}*]{#struct_0_16776_x1311_1662948506}[通知]{style="font-family:宋体"}[AP]{lang="EN-US"}[事件失败]{style="font-family:宋体"}

[*[service]{lang="EN-US"}*]{#struct_0_16776_x1311_x326062644}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BASIC]{lang="EN-US"}]{#struct_0_16776_x1311_294011473}[：基础模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11ABG]{lang="EN-US"}]{#struct_0_16776_x1311_x1957403515}[：]{lang="EN-US" style="font-family:宋体"}[802.11abg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WMM]{lang="EN-US"}]{#struct_0_16776_x1311_492786570}[：无线]{lang="EN-US" style="font-family:宋体"}[QoS ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11R]{lang="EN-US"}]{#struct_0_16776_x1311_x2038317148}[：]{lang="EN-US" style="font-family:宋体"}[802.11r ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11I]{lang="EN-US"}]{#struct_0_16776_x1311_x1326615895}[：]{lang="EN-US" style="font-family:宋体"}[802.11i ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11N]{lang="EN-US"}]{#struct_0_16776_x1311_1848479212}[：]{lang="EN-US" style="font-family:宋体"}[802.11n ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11AC]{lang="EN-US"}]{#struct_0_16776_x1311_294011470}[：]{lang="EN-US" style="font-family:宋体"}[802.11ac ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROAM]{lang="EN-US"}]{#struct_0_16776_x1311_x1957403512}[：漫游模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11W]{lang="EN-US"}]{#struct_0_16776_x1311_89502043}[：]{lang="EN-US" style="font-family:宋体"}[802.11w ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WLAS AM]{lang="EN-US"}]{#struct_0_16776_x1311_x569031757}[：无线接入认证端]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WLAS CM]{lang="EN-US"}]{#struct_0_16776_x1311_303142135}[：无线接入客户端]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_16776_x1311_862492805}[：]{lang="EN-US" style="font-family:宋体"}[VLAN ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD_POLICY]{lang="EN-US"}]{#struct_0_16776_x1311_294011471}[：策略转发]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SAVI]{lang="EN-US"}]{#struct_0_16776_x1311_x1957403513}[：源地址有效验证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCO]{lang="EN-US"}]{#struct_0_16776_x1311_1655585984}[：组播优化]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[Failed to inform service *service* of radio event.]{lang="EN-US"}]{#struct_0_16776_x1311_728817006}

[[向业务模块]{style="font-family:宋体"}*[service]{lang="EN-US"}*]{#struct_0_16776_x1311_x1032823349}[通知]{style="font-family:宋体"}[radio]{lang="EN-US"}[事件失败]{style="font-family:宋体"}

[*[service]{lang="EN-US"}*]{#struct_0_16776_x1311_x1737441739}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BASIC]{lang="EN-US"}]{#struct_0_16776_x1311_494388977}[：基础模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11ABG]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303658}[：]{lang="EN-US" style="font-family:宋体"}[802.11abg]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WMM]{lang="EN-US"}]{#struct_0_16776_x1311_148216272}[：无线]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11R]{lang="EN-US"}]{#struct_0_16776_x1311_x1509192165}[：]{lang="EN-US" style="font-family:宋体"}[802.11r]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11I]{lang="EN-US"}]{#struct_0_16776_x1311_x1458180594}[：]{lang="EN-US" style="font-family:宋体"}[802.11i]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11N]{lang="EN-US"}]{#struct_0_16776_x1311_x1635451523}[：]{lang="EN-US" style="font-family:宋体"}[  802.11n]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11AC]{lang="EN-US"}]{#struct_0_16776_x1311_x1771183181}[：]{lang="EN-US" style="font-family:宋体"}[802.11ac]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ROAM]{lang="EN-US"}]{#struct_0_16776_x1311_x113339658}[：漫游模块]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11W]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303657}[：]{lang="EN-US" style="font-family:宋体"}[802.11w]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WLAS AM]{lang="EN-US"}]{#struct_0_16776_x1311_2070530573}[：无线接入认证端]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[WLAS CM]{lang="EN-US"}]{#struct_0_16776_x1311_1479092394}[：无线接入客户端]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_16776_x1311_998907444}[：]{lang="EN-US" style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FWD_POLICY]{lang="EN-US"}]{#struct_0_16776_x1311_1742497642}[：策略转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SAVI]{lang="EN-US"}]{#struct_0_16776_x1311_1683618886}[：源地址有效验证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MCO]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303660}[：组播优化]{lang="EN-US" style="font-family:宋体"}

[[\[APID: *APID[, ]{style="color:#17365D"}*Radio ID*[: ]{style="color:#17365D"}RadioID[, ]{style="color:#17365D"}*WLAN ID*[: ]{style="color:#17365D"}WlanID*\] Failed to delete all clients.]{lang="EN-US"}]{#struct_0_16776_x1311_504381096}

[[删除所有的]{style="font-family:宋体"}[Client]{lang="EN-US"}]{#struct_0_16776_x1311_367669608}[失败]{style="font-family:宋体"}

[[Failed to get BSS *BSSID*.]{lang="EN-US"}]{#struct_0_16776_x1311_x538187680}

[[获取]{style="font-family:宋体"}[BSS *BSSID*]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303659}[失败]{style="font-family:宋体"}[.]{lang="EN-US"}

[[Failed to create a BSS.]{lang="EN-US"}]{#struct_0_16776_x1311_x1417867669}

[[创建]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_16776_x1311_1421655163}[失败。]{style="font-family:宋体"}

[[Received unsupported queue message.]{lang="EN-US"}]{#struct_0_16776_x1311_2037175751}

[[收到了不支持的队列消息]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1662303662}

[[\[BSSID: *BSSID*\] Failed to send add wlan message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_1667180510}

[[发送下行]{style="font-family:宋体"}[add wlan]{lang="EN-US"}]{#struct_0_16776_x1311_934761387}[消息失败]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] Failed to send delete wlan message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1080103782}

[[发送下行]{style="font-family:宋体"}[delete wlan]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303661}[消息失败]{style="font-family:宋体"}

[[Failed to disable packet socket for BSS *BSSID*.]{lang="EN-US"}]{#struct_0_16776_x1311_x1061702845}

[[去使能]{style="font-family:宋体"}[BSS *BSSID*]{lang="EN-US"}]{#struct_0_16776_x1311_x1082084142}[的]{style="font-family:宋体"}[packet socket ]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to send add mobile message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x809384194}

[[下同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303664}[消息失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to send add mobile message to uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1821217732}

[[上同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x1484843848}[消息失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to send delete mobile message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1794555661}

[[下同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303663}[消息失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to send delete mobile message to uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_101096569}

[[上同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x807902760}[消息失败]{style="font-family:宋体"}

[[Failed to process radio up event.]{lang="EN-US"}]{#struct_0_16776_x1311_1183844491}

[[处理]{style="font-family:宋体"}[radio up]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303666}[事件失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging wlan client]{lang="EN-US"}[ error]{lang="EN-US"}]{#struct_0_16776_x1311_x658418318}[命令输出信息描述表]{style="font-family:黑体"}[(]{lang="EN-US"}[仅]{style="font-family:黑体"}[FAT AP)]{lang="EN-US"}

[]{#table_struct_0_x1317341160}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x816867487}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_1244809156}

[[Failed to process a probe request: The frame doesn\'t contain mandatory IE.]{lang="EN-US"}]{#struct_0_16776_x1311_411917380}

[[处理探测请求帧失败，由于报文没有包含强制]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_16776_x1311_362189296}[元素]{style="font-family:宋体"}

[[Failed to get the BSS: Invalid BSSID.]{lang="EN-US"}]{#struct_0_16776_x1311_1099502373}

[[获取]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_16776_x1311_x1662303665}[失败：]{style="font-family:宋体"}[BSSID]{lang="EN-US"}[无效]{style="font-family:宋体"}

[[Failed to decode the SSID IE: The length of the SSID exceeds the upper limit.]{lang="EN-US"}]{#struct_0_16776_x1311_907665623}

[[解析]{style="font-family:宋体"}[SSID IE]{lang="EN-US"}]{#struct_0_16776_x1311_281021964}[失败，由于]{style="font-family:宋体"}[SSID ]{lang="EN-US"}[长度大于上限]{style="font-family:宋体"}

[[Failed to decode the supported rates IE: The length exceeds the upper limit.]{lang="EN-US"}]{#struct_0_16776_x1311_2034575515}

[[解析]{style="font-family:宋体"}[Supported rates IE]{lang="EN-US"}]{#struct_0_16776_x1311_x954613323}[失败，由于]{style="font-family:宋体"}[rates]{lang="EN-US"}[长度大于上限]{style="font-family:宋体"}

[[Failed to decode the FH Parameter Set IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x918186760}

[[解析]{style="font-family:宋体"}[FH Parameter Set IE]{lang="EN-US"}]{#struct_0_16776_x1311_522369866}[失败，由于]{style="font-family:宋体"}[FH Parameter Set]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the DSSS Parameter Set IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_801556604}

[[解析]{style="font-family:宋体"}[DSSS Parameter Set IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1070200933}[失败，由于]{style="font-family:宋体"}[DSSS Parameter Set]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the CF Parameter Set IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_676348502}

[[解析]{style="font-family:宋体"}[CF Parameter Set IE]{lang="EN-US"}]{#struct_0_16776_x1311_x204964761}[失败，由于]{style="font-family:宋体"}[CF Parameter Set]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the TIM IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_594592813}

[[解析]{style="font-family:宋体"}[TIM IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1479813470}[失败，由于]{style="font-family:宋体"}[TIM]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the IBSS Parameter Set IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_535453622}

[[解析]{style="font-family:宋体"}[IBSS Parameter Set IE]{lang="EN-US"}]{#struct_0_16776_x1311_791501006}[失败，由于]{style="font-family:宋体"}[IBSS Parameter Set]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Country IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x1930237023}

[[解析]{style="font-family:宋体"}[Country IE]{lang="EN-US"}]{#struct_0_16776_x1311_676348503}[失败，由于]{style="font-family:宋体"}[Country]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Hopping Pattern Parameters IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x204964762}

[[解析]{style="font-family:宋体"}[Hopping Pattern Parameters IE]{lang="EN-US"}]{#struct_0_16776_x1311_594527277}[失败，由于]{style="font-family:宋体"}[Hopping Pattern Parameters]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the BSS Load IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x1862645289}

[[解析]{style="font-family:宋体"}[BSS Load IE]{lang="EN-US"}]{#struct_0_16776_x1311_1879324465}[失败，由于]{style="font-family:宋体"}[BSS Load]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Challenge text IE: The length exceeds the upper limit or is equal to 0.]{lang="EN-US"}]{#struct_0_16776_x1311_676348500}

[[解析]{style="font-family:宋体"}[Challenge text IE]{lang="EN-US"}]{#struct_0_16776_x1311_x204964759}[失败，由于]{style="font-family:宋体"}[Challenge text ]{lang="EN-US"}[长度大于上限]{style="font-family:宋体"} [或]{style="font-family:宋体"} [等于]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Failed to decode the Power Constraint IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_595117104}

[[解析]{style="font-family:宋体"}[Power Constraint IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1468686513}[失败，由于]{style="font-family:宋体"}[Power Constraint]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the TPC Report IE: Invalid  length.]{lang="EN-US"}]{#struct_0_16776_x1311_1243723382}

[[解析]{style="font-family:宋体"}[TPC Report IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1351758126}[失败，由于]{style="font-family:宋体"}[TPC Report]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Supported Channels IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_1456422816}

[[解析]{style="font-family:宋体"}[Supported Channels IE]{lang="EN-US"}]{#struct_0_16776_x1311_676348501}[失败，由于]{style="font-family:宋体"}[Supported Channels]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Quiet IE: Invalid  length.]{lang="EN-US"}]{#struct_0_16776_x1311_x204964760}

[[无效]{style="font-family:宋体"}[Quiet]{lang="EN-US"}]{#struct_0_16776_x1311_594658349}[长度：]{style="font-family:宋体"}

[[解析后的长度为非标准长度]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1964851563}

[[Failed to decode the ERP IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x1744075862}

[[解析]{style="font-family:宋体"}[ERP IE]{lang="EN-US"}]{#struct_0_16776_x1311_676348498}[失败，由于]{style="font-family:宋体"}[ERP]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the HT Capabilities IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_1788086214}

[[解析]{style="font-family:宋体"}[HT Capabilities IE]{lang="EN-US"}]{#struct_0_16776_x1311_x725262168}[失败，由于]{style="font-family:宋体"}[HT Capabilities]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the RSN Capabilities IE: The length is below the lower limit.]{lang="EN-US"}]{#struct_0_16776_x1311_x1341855259}

[[解析]{style="font-family:宋体"}[RSN IE]{lang="EN-US"}]{#struct_0_16776_x1311_676348499}[失败，由于]{style="font-family:宋体"}[RSN]{lang="EN-US"}[长度小于下限]{style="font-family:宋体"}

[[Failed to decode the Extended Supported Rates IE: The length is equal to 0.]{lang="EN-US"}]{#struct_0_16776_x1311_1788086213}

[[解析]{style="font-family:宋体"}[Extended Supported Rates IE]{lang="EN-US"}]{#struct_0_16776_x1311_x724803416}[失败，由于]{style="font-family:宋体"}[Extended Supported Rates]{lang="EN-US"}[长度为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[Failed to decode the HT Operation IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x568959059}

[[解析]{style="font-family:宋体"}[HT Operation IE]{lang="EN-US"}]{#struct_0_16776_x1311_1888088422}[失败，由于]{style="font-family:宋体"}[HT Operation]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the 20/40 BSS Coexistence IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_676348496}

[[解析]{style="font-family:宋体"}[20/40 BSS Coexistence IE]{lang="EN-US"}]{#struct_0_16776_x1311_1788086216}[失败，由于]{style="font-family:宋体"}[20/40 BSS Coexistence]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the 20/40 BSS Intolerant Channel Report IE: The length is smaller than 1.]{lang="EN-US"}]{#struct_0_16776_x1311_x725131096}

[[解析]{style="font-family:宋体"}[20/40 BSS Intolerant Channel Report IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1722583706}[失败，由于]{style="font-family:宋体"}[20/40 BSS Intolerant Channel Report]{lang="EN-US"}[长度小于]{style="font-family:
  宋体"}[1]{lang="EN-US"}

[[Failed to decode the Extended Capabilities IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_676348497}

[[解析]{style="font-family:宋体"}[Extended Capabilities IE]{lang="EN-US"}]{#struct_0_16776_x1311_1788086215}[失败，由于]{style="font-family:宋体"}[Extended Capabilities]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[Failed to decode the Power Capability IE: Invalid length.]{lang="EN-US"}]{#struct_0_16776_x1311_x725196632}

[[解析]{style="font-family:宋体"}[Power Capability IE]{lang="EN-US"}]{#struct_0_16776_x1311_x151185505}[失败，由于]{style="font-family:宋体"}[Power Capability]{lang="EN-US"}[长度为非标准长度]{style="font-family:宋体"}

[[\[APID: *APID[, ]{style="color:#17365D"}*Radio ID*[: ]{style="color:#17365D"}RadioID[, ]{style="color:#17365D"}*Session ID*[: ]{style="color:#17365D"}SessionID*\] Failed to process radio down event.]{lang="EN-US"}]{#struct_0_16776_x1311_676348494}

[[处理]{style="font-family:宋体"}[Radio Down]{lang="EN-US"}]{#struct_0_16776_x1311_1788086218}[事件失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging wlan client]{lang="EN-US"}[ event]{lang="EN-US"}]{#struct_0_16776_x1311_x725524312}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1295324510}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x137613621}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x865773714}

[[Can\'t create BSS: The AP is in down state.]{lang="EN-US"}]{#struct_0_16776_x1311_x1177125063}

[[由于]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_16776_x1311_x1643413359}[处于]{style="font-family:宋体"} [Down]{lang="EN-US"}[状态，不满足创建]{style="font-family:宋体"}[BSS]{lang="EN-US"}[的条件]{style="font-family:宋体"}

[[Can\'t create BSS: The service template is disabled.]{lang="EN-US"}]{#struct_0_16776_x1311_x1156331307}

[[由于服务模板未使能，不满足创建]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_16776_x1311_x593643972}[的条件]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID[, ]{style="color:#17365D"}*WLAN ID*[ ]{style="color:#17365D"}WlanID*\] Received update BSS message.]{lang="EN-US"}]{#struct_0_16776_x1311_676348495}

[[成功收到]{style="font-family:宋体"}[Update BSS]{lang="EN-US"}]{#struct_0_16776_x1311_1788086217}[消息]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID*\] Processed AP create event successfully.]{lang="EN-US"}]{#struct_0_16776_x1311_x725065560}

[[处理]{style="font-family:宋体"}[AP Create]{lang="EN-US"}]{#struct_0_16776_x1311_x1336171872}[事件成功]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID*\] Processed radio down event successfully.]{lang="EN-US"}]{#struct_0_16776_x1311_x408441293}

[[处理]{style="font-family:宋体"}[Radio Down]{lang="EN-US"}]{#struct_0_16776_x1311_x1369479676}[事件成功]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID[, ]{style="color:#17365D"}*WLAN ID*[ ]{style="color:#17365D"}WlanID*\] BSS already exists.]{lang="EN-US"}]{#struct_0_16776_x1311_x1139180021}

[[BSS]{lang="EN-US"}]{#struct_0_16776_x1311_1865826902}[已经存在]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID*\] Unsupported radio event *event*.]{lang="EN-US"}]{#struct_0_16776_x1311_38800998}

[[无效的]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_16776_x1311_x1829554378}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[\[APID *APID* \] Unsupported AP event *event*.]{lang="EN-US"}]{#struct_0_16776_x1311_x1573441474}

[[无效的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_16776_x1311_182208128}[事件]{style="font-family:宋体"}*[event]{lang="EN-US"}*

[[\[APID: *APID*\] Received add wlan response message. ]{lang="EN-US"}]{#struct_0_16776_x1311_x1227839373}

[[收到]{style="font-family:宋体"}[add wlan]{lang="EN-US"}]{#struct_0_16776_x1311_x243370107}[响应消息]{style="font-family:宋体"}

[[\[APID: *APID*\] Received delete wlan response message. ]{lang="EN-US"}]{#struct_0_16776_x1311_1865826903}

[[收到]{style="font-family:宋体"}[delete wlan]{lang="EN-US"}]{#struct_0_16776_x1311_38735462}[响应消息]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] Sent add wlan message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x613097297}

[[成功发送下行]{style="font-family:宋体"}[add wlan]{lang="EN-US"}]{#struct_0_16776_x1311_x583907764}[消息]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] Sent delete wlan message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_205431581}

[[成功发送下行]{style="font-family:宋体"}[delete wlan]{lang="EN-US"}]{#struct_0_16776_x1311_x1560424219}[消息]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Sent add mobile message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1631121686}

[[下同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_764735724}[消息成功]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Received add mobile response message from downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_1865826900}

[[收到下同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_38669926}[回应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Can\'t send add mobile message to uplink device: Reached the end of the IOCTL tunnel.]{lang="EN-US"}]{#struct_0_16776_x1311_1334062332}

[[因为已经是顶层，不能发送上同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x512426414}[消息]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Sent add mobile message to uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_1865826901}

[[上同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_38604390}[消息成功]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Received add mobile response message from the uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_592909204}

[[收到上同步]{style="font-family:宋体"}[add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x1470559218}[回应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Sent delete mobile message to downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_119464799}

[[下同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_1865826898}[消息成功]{style="font-family:宋体"}

[[\[APID :*APID*\] ]{lang="EN-US"}[Received delete mobile response message from downlink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1917120915}

[[收到下同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x1148536773}[回应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Can\'t send delete mobile message to uplink device: Reached the end of the IOCTL tunnel.]{lang="EN-US"}]{#struct_0_16776_x1311_x707635027}

[[因为已经是顶层，不能发送上同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_1865826899}[消息]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Sent delete mobile message to uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x1917186451}

[[上同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x2002888008}[消息成功]{style="font-family:宋体"}

[[\[APID: *APID*\] ]{lang="EN-US"}[Received delete mobile response message from uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x745654031}

[[收到上同步]{style="font-family:宋体"}[delete mobile]{lang="EN-US"}]{#struct_0_16776_x1311_1865826896}[回应]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging wlan client]{lang="EN-US"}[ event]{lang="EN-US"}]{#struct_0_16776_x1311_x1917251987}[命令输出信息描述表]{style="font-family:黑体"}[(]{lang="EN-US"}[仅]{style="font-family:黑体"}[FAT AP)]{lang="EN-US"}

[]{#table_struct_0_x1297656834}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1333802278}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x783019859}

[[\[APID: *APID*\] Failed to reply to the broadcast probe request: The AP is not allowed to reply to broadcast probe requests.]{lang="EN-US"}]{#struct_0_16776_x1311_x1035004987}

[[AP]{lang="EN-US"}]{#struct_0_16776_x1311_x164544340}[设置不允许回复广播探查]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Radio ID*[ ]{style="color:#17365D"}RadioID*\] Processed radio up event successfully.]{lang="EN-US"}]{#struct_0_16776_x1311_x1088359531}

[[处理]{style="font-family:宋体"}[Radio Up]{lang="EN-US"}]{#struct_0_16776_x1311_x2007997868}[事件成功]{style="font-family:宋体"}

[[\[APID *APID[, ]{style="color:#17365D"}*Session ID*[ ]{style="color:#17365D"}SessionID*\] Processed AP down event successfully.]{lang="EN-US"}]{#struct_0_16776_x1311_1865826897}

[[处理]{style="font-family:宋体"}[AP Down]{lang="EN-US"}]{#struct_0_16776_x1311_x1917317523}[事件成功]{style="font-family:宋体"}

[[\[BSSID: *BSSID*\] ]{lang="EN-US"}[Processing update beacon.]{lang="EN-US"}]{#struct_0_16776_x1311_x1408013354}

[[处理]{style="font-family:宋体"}[Update beacon]{lang="EN-US"}]{#struct_0_16776_x1311_x961036885}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging wlan client]{lang="EN-US"}[ fsm]{lang="EN-US"}]{#struct_0_16776_x1311_1642847226}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1304356392}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1638663224}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x356218967}

[[Changed the client\'s status from *state1* to*[ ]{style="color:#1F497D"}state2*.]{lang="EN-US"}]{#struct_0_16776_x1311_1803392697}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_244923088}[状态从]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}[state2]{lang="EN-US"}

[[state1]{lang="EN-US"}]{#struct_0_16776_x1311_x1981073637}[和]{style="font-family:宋体"}[state2]{lang="EN-US"}*[取值]{style="font-family:宋体"}*[如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UnAuth]{lang="EN-US"}]{#struct_0_16776_x1311_1865826894}[：未认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Auth]{lang="EN-US"}]{#struct_0_16776_x1311_x1917383059}[：]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}[认证状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UserAuth]{lang="EN-US"}]{#struct_0_16776_x1311_x2044002412}[：用户认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Run]{lang="EN-US"}]{#struct_0_16776_x1311_1610188749}[：]{lang="EN-US" style="font-family:宋体"}[ Run]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[\[MAC: *MAC* BSSID: *BSSID*\] Received disassociation in the Run state: Reason code=*reasoncode*.]{lang="EN-US"}]{#struct_0_16776_x1311_1853991393}

[[由于]{style="font-family:宋体"}*[reasoncode]{lang="EN-US"}*]{#struct_0_16776_x1311_610053976}[，收到处于]{style="font-family:宋体"}[Run]{lang="EN-US"}[状态的客户端的去关联报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x774430963}

[[\# ]{lang="EN-US"}]{#struct_0_16776_x1311_607781508}[打开]{style="font-family:宋体"}[stamgr]{lang="EN-US"}[模块的所有类型的调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wlan client all]{lang="EN-US"}]{#struct_0_16776_x1311_1865826895}

[\[APID: *APID*\] Deleted an AP.]{lang="EN-US"}

[*[//\[APID: 1\]]{lang="EN-US"}*]{#struct_0_16776_x1311_x1917448595}*[删除]{style="font-family:宋体"}[AP]{lang="EN-US"}[成功。]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_16776_x1311_x1994720887}[打开]{style="font-family:宋体"}[stamgr]{lang="EN-US"}[模块的状态机相关的调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wlan client fsm]{lang="EN-US"}]{#struct_0_16776_x1311_x987193011}

[Changed the client\'s state from UnAuth to*[ ]{style="color:#1F497D"}*Auth.]{lang="EN-US"}

[*[//Client]{lang="EN-US"}*]{#struct_0_16776_x1311_1172164557}*[的状态由未认证状态迁移到了认证状态。]{style="font-family:宋体"}*

::: {#-1177942419 .myid}
[]{#_Toc404794857}[]{#struct_0_16776_x1311_x429717671}

**WLAN接入 \-- WLAN接入调试命令 \-- debugging wlan client mac**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x2041017121}

[**[debugging wlan client mac ]{lang="EN-US" style="color:black"}***[mac-address]{lang="EN-US"}*]{#struct_0_16776_x1311_920732007}

[**[undo debugging wlan client mac ]{lang="EN-US" style="color:black"}**]{#struct_0_16776_x1311_900350484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_16776_x1311_1299452887}

[[任意视图]{style="font-family:宋体"}]{#struct_0_16776_x1311_1415999227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x216583111}

[[network-admin]{lang="EN-US"}]{#struct_0_16776_x1311_x90488234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_16776_x1311_1089734828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x547665537}

[*[mac-address]{lang="EN-US" style="color:black"}*]{#struct_0_16776_x1311_1589818301}[：]{style="font-family:宋体"}[客户端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_16776_x1311_1379979665}

[**[debugging wlan client mac]{lang="EN-US" style="color:windowtext"}**]{#struct_0_16776_x1311_x1724835217}[用来基于客户端]{style="font-family:宋体;color:windowtext"}[MAC]{lang="EN-US" style="color:windowtext"}[地址打开调试开关。]{style="font-family:宋体;
color:windowtext"}**[undo ]{lang="EN-US" style="color:windowtext"}[debugging wlan client mac]{lang="EN-US" style="color:windowtext"}**[用来关闭指定]{style="font-family:宋体;color:windowtext"}[MAC]{lang="EN-US" style="color:windowtext"}[地址的客户端的调试开关。]{style="font-family:宋体;color:windowtext"}

[[缺省情况下，客户端的调试信息开关处于关闭状态]{style="font-family:宋体;color:windowtext"}]{#struct_0_16776_x1311_1262920764}

[[表1-6 ]{lang="EN-US"}[debugging wlan client mac error]{lang="EN-US"}]{#struct_0_16776_x1311_693523111}[命令输出信息描述表（仅]{style="font-family:黑体"}[AC]{lang="EN-US"}[）]{style="font-family:黑体"}

[]{#table_struct_0_x1301150552}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_1314161338}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_172789866}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to send add mobile message to the uplink device.]{lang="EN-US"}]{#struct_0_16776_x1311_x90488233}

[[Add Mobile]{lang="EN-US"}]{#struct_0_16776_x1311_1089734833}[上行同步失败。]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to fill VLAN information to the add mobile message.]{lang="EN-US"}]{#struct_0_16776_x1311_x547206784}

[[Add Mobile]{lang="EN-US"}]{#struct_0_16776_x1311_1597592833}[消息中填充]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[信息失败。]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to process the open system authentication request: The BSS doesn\'t support ]{lang="EN-US"}[open system authentication.]{lang="EN-US"}]{#struct_0_16776_x1311_454913748}

[[BSS ]{lang="EN-US"}]{#struct_0_16776_x1311_x945100942}[不支持开放式认证]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to authenticate the client: Radio obtaining failure.]{lang="EN-US"}]{#struct_0_16776_x1311_921964743}

[[由于获取]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_16776_x1311_458659619}[失败，导致认证失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to process the open system authentication request: Wrong serial number.]{lang="EN-US"}]{#struct_0_16776_x1311_x90488236}

[[收到的开放式认证报文序列号错误，处理认证请求报文失败]{style="font-family:宋体"}]{#struct_0_16776_x1311_1089734830}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to process IE in the (re)association request.]{lang="EN-US"}]{#struct_0_16776_x1311_x547141248}

[[处理（重）关联请求报文]{style="font-family:宋体"}[IE]{lang="EN-US"}]{#struct_0_16776_x1311_x1958312607}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to associate with the AP: The number of clients exceeded the limit. ]{lang="EN-US"}]{#struct_0_16776_x1311_1951737137}

[[由于关联客户端数据达到上限，关联]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_16776_x1311_1303966838}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to process (re)association request in Run state.]{lang="EN-US"}]{#struct_0_16776_x1311_x208925704}

[[Run]{lang="EN-US"}]{#struct_0_16776_x1311_x90488235}[状态下处理（重）关联请求失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to p]{lang="EN-US"}[rocess (re)association request in Run state without sending (re)association response.]{lang="EN-US"}]{#struct_0_16776_x1311_1089734827}

[[Run]{lang="EN-US"}]{#struct_0_16776_x1311_x546944641}[状态下处理]{style="font-family:宋体"}[（重）关联请求失败，但不发送（重）关联响应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to process (re)association request in Auth state.]{lang="EN-US"}]{#struct_0_16776_x1311_x1971896510}

[[Auth]{lang="EN-US"}]{#struct_0_16776_x1311_848309080}[状态下处理]{style="font-family:宋体"}[（重）关联请求失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to p]{lang="EN-US"}[rocess (re)association request in Auth state without sending (re)association response. ]{lang="EN-US"}]{#struct_0_16776_x1311_1227460859}

[[Auth]{lang="EN-US"}]{#struct_0_16776_x1311_x90488238}[状态下处理]{style="font-family:宋体"}[（重）关联请求失败，但不发送（重）关联响应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to get AID.]{lang="EN-US"}]{#struct_0_16776_x1311_1089734840}

[[获取]{style="font-family:宋体"}[AID]{lang="EN-US"}]{#struct_0_16776_x1311_x547141247}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to update radio capabilities.]{lang="EN-US"}]{#struct_0_16776_x1311_x1957591711}

[[更新]{style="font-family:宋体"}[Radio]{lang="EN-US"}]{#struct_0_16776_x1311_x1631870821}[能力集失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to send add mobile messages.]{lang="EN-US"}]{#struct_0_16776_x1311_936118786}

[[下发]{style="font-family:宋体"}[Add mobile]{lang="EN-US"}]{#struct_0_16776_x1311_x90488237}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Received invalid frame in ]{lang="EN-US"}[Unauth state.]{lang="EN-US"}]{#struct_0_16776_x1311_1089734829}

[[在]{style="font-family:宋体"}[Unauth]{lang="EN-US"}]{#struct_0_16776_x1311_x547600001}[状态下收到错误报文]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Frame check failed: Invalid frame length.]{lang="EN-US"}]{#struct_0_16776_x1311_x17952369}

[[由于报文长度不合法，报文校验失败]{style="font-family:宋体"}]{#struct_0_16776_x1311_x60066044}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Frame check failed: Invalid frame header.]{lang="EN-US"}]{#struct_0_16776_x1311_x1728515673}

[[由于报文头无效，报文校验失败]{style="font-family:宋体"}]{#struct_0_16776_x1311_x90488240}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to p]{lang="EN-US"}[rocess (re)association request in Userauth state without sending (re)association response.]{lang="EN-US"}]{#struct_0_16776_x1311_x101906256}

[[Userauth]{lang="EN-US"}]{#struct_0_16776_x1311_1574034170}[状态下处理]{style="font-family:宋体"}[（重）关联失败，但不发送（重）关联响应]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to release AID.]{lang="EN-US"}]{#struct_0_16776_x1311_319096697}

[[释放]{style="font-family:宋体"}[AID]{lang="EN-US"}]{#struct_0_16776_x1311_772618305}[失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to process the authentication request: Unsupported algorithm.]{lang="EN-US"}]{#struct_0_16776_x1311_x90488239}

[[算法不支持导致处理认证请求失败。]{style="font-family:宋体"}]{#struct_0_16776_x1311_1089734839}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to process the authentication request: Mismatched algorithm.]{lang="EN-US"}]{#struct_0_16776_x1311_x547600000}

[[算法不匹配导致处理认证请求失败。]{style="font-family:宋体"}]{#struct_0_16776_x1311_x18017905}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to send the (re)association response.]{lang="EN-US"}]{#struct_0_16776_x1311_x132967385}

[[发送（重）关联回应失败]{style="font-family:宋体"}]{#struct_0_16776_x1311_x640514769}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging wlan client]{lang="EN-US"}[ mac event]{lang="EN-US"}]{#struct_0_16776_x1311_x90488242}[命令输出信息描述表（仅]{style="font-family:黑体"}[AC]{lang="EN-US"}[）]{style="font-family:黑体"}

[]{#table_struct_0_x1278146462}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x101906254}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_1574165242}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Allocated AID successfully.]{lang="EN-US"}]{#struct_0_16776_x1311_x820669764}

[[分配]{style="font-family:宋体"}[AID]{lang="EN-US"}]{#struct_0_16776_x1311_x361686257}[成功]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Processing (re)association request...]{lang="EN-US"}]{#struct_0_16776_x1311_x1402020565}

[[处理（重）关联报文]{style="font-family:宋体"}]{#struct_0_16776_x1311_1983341659}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Processing association request in Auth state...]{lang="EN-US"}]{#struct_0_16776_x1311_x2139493331}

[[认证状态下处理关联报文]{style="font-family:宋体"}]{#struct_0_16776_x1311_x90488241}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Processed association request successfully, and sent association response.]{lang="EN-US"}]{#struct_0_16776_x1311_x101906257}

[[处理关联请求成功，并发送关联回应]{style="font-family:宋体"}]{#struct_0_16776_x1311_1574099706}

[[\[MAC: *mac-address*, BSSID: *BSSID*\]]{lang="EN-US"}[ Processed (re)association request successfully when the client was in Run state .]{lang="EN-US"}]{#struct_0_16776_x1311_x433972333}

[[用户处于]{style="font-family:宋体"}[Run]{lang="EN-US"}]{#struct_0_16776_x1311_x313471955}[状态下，（重）关联请求处理成功]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\]]{lang="EN-US"}[ Processed (re)association request successfully when the client was in Auth state.]{lang="EN-US"}]{#struct_0_16776_x1311_x845980155}

[[用户处于]{style="font-family:宋体"}[Auth]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803370}[状态下，（重）关联请求处理成功]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Checking association load of the device...]{lang="EN-US"}]{#struct_0_16776_x1311_296591058}

[[检查设备的关联负载]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1360181766}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] Failed to ]{lang="EN-US"}[process (re)association request in Run state.]{lang="EN-US"}]{#struct_0_16776_x1311_346677042}

[[Userauth]{lang="EN-US"}]{#struct_0_16776_x1311_x106542229}[状态下处理]{style="font-family:宋体"}[（重）关联请求失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging wlan client timer]{lang="EN-US"}]{#struct_0_16776_x1311_x740423669}[命令输出信息描述表（仅]{style="font-family:黑体"}[AC]{lang="EN-US"}[）]{style="font-family:黑体"}

[]{#table_struct_0_x1275770972}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1332765512}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1970357231}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Keepalive timer expired.]{lang="EN-US"}]{#struct_0_16776_x1311_607218683}

[[保活定时器超时]{style="font-family:宋体"}]{#struct_0_16776_x1311_2117915328}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Idle timer expired.]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803369}

[[闲置定时器超时]{style="font-family:宋体"}]{#struct_0_16776_x1311_x2075996401}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Userauth state timer expired.]{lang="EN-US"}]{#struct_0_16776_x1311_x1402663669}

[[用户认证状态状态定时器超时]{style="font-family:宋体"}]{#struct_0_16776_x1311_1064680370}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Auth state timer expired.]{lang="EN-US"}]{#struct_0_16776_x1311_1082151811}

[[认证状态状态定时器超时]{style="font-family:宋体"}]{#struct_0_16776_x1311_x829494289}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Unauth state timer expired.]{lang="EN-US"}]{#struct_0_16776_x1311_x66965772}

[[未认证状态状态定时器超时]{style="font-family:宋体"}]{#struct_0_16776_x1311_x426225216}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Failed to process authentication request: The client is being deleted.]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803372}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_1459390472}[正在删除中，处理认证请求失败]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Created keepalive timer.]{lang="EN-US"}]{#struct_0_16776_x1311_1309943091}

[[创建保活定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1432703439}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Created idle timer.]{lang="EN-US"}]{#struct_0_16776_x1311_115319270}

[[创建闲置定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x2105852996}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Created state timer.]{lang="EN-US"}]{#struct_0_16776_x1311_1637851499}

[[创建状态定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x2046803371}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Refreshed state timer.]{lang="EN-US"}]{#struct_0_16776_x1311_1862674999}

[[刷新状态定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1794234883}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Refreshed keepalive timer.]{lang="EN-US"}]{#struct_0_16776_x1311_x1693616466}

[[刷新保活定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1646915619}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Deleted state timer.]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803374}

[[删除状态定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x2029007770}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Refreshed idle timer.]{lang="EN-US"}]{#struct_0_16776_x1311_67084019}

[[刷新闲置定时器]{style="font-family:宋体"}]{#struct_0_16776_x1311_x1558870049}

[ ]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[debugging wlan client fsm]{lang="EN-US"}]{#struct_0_16776_x1311_x112442865}[命令输出信息描述表（仅]{style="font-family:黑体"}[AC]{lang="EN-US"}[）]{style="font-family:黑体"}

[]{#table_struct_0_x1279777830}[[字段]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1884493459}

[[描述]{style="font-family:黑体"}]{#struct_0_16776_x1311_x1660495851}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client state: Unauth.]{lang="EN-US"}]{#struct_0_16776_x1311_1338751148}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803373}[状态：]{style="font-family:宋体"} [未认证]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client state: Auth.]{lang="EN-US"}]{#struct_0_16776_x1311_x1269492883}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_674001439}[状态：已认证]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client state: Userauth.]{lang="EN-US"}]{#struct_0_16776_x1311_x2122689557}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_x942301352}[状态：用户认证]{style="font-family:宋体"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client state: Run.]{lang="EN-US"}]{#struct_0_16776_x1311_598115725}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_x1245133795}[状态：]{style="font-family:宋体"} [Run]{lang="EN-US"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client went online. Status changed to Run.]{lang="EN-US"}]{#struct_0_16776_x1311_x1596312859}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_1282460214}[已经上线，状态迁移到了]{style="font-family:宋体"}[Run]{lang="EN-US"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Client went offline. Status changed to Unauth.]{lang="EN-US"}]{#struct_0_16776_x1311_x1783400723}

[[Client]{lang="EN-US"}]{#struct_0_16776_x1311_404893895}[已经下线，状态迁移到了]{style="font-family:宋体"}[Unauth]{lang="EN-US"}

[[\[MAC: *mac-address*, BSSID: *BSSID*\] ]{lang="EN-US"}[Received deauthentication or disassociation request from client in *state* state: Reason code=*Reasoncode*.]{lang="EN-US"}]{#struct_0_16776_x1311_x2046803376}

[[收到处于当前状态的]{style="font-family:宋体"}[Client]{lang="EN-US"}]{#struct_0_16776_x1311_x866208356}[发来的含有原因码的去认证]{style="font-family:宋体"}[/]{lang="EN-US"}[去关联报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_16776_x1311_x2023719995}

[[\# ]{lang="EN-US"}]{#struct_0_16776_x1311_x319721691}[打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[ 05-0A-31-22-11-11]{lang="EN-US"}[的无线客户端的调试开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging wlan client mac 05-0A-31-22-11-11]{lang="EN-US"}]{#struct_0_16776_x1311_x524067282}

[\[MAC: *05-0A-31-22-11-11*, BSSID: *ab-ab-ab-ab-ab-ab*\] ]{lang="EN-US"}[Created idle timer.]{lang="EN-US"}

[*[//BSSID]{lang="EN-US"}*]{#struct_0_16776_x1311_409373648}*[为]{style="font-family:宋体"}[ab-ab-ab-ab-ab-ab]{lang="EN-US"}[的无线服务为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[05-0A-31-22-11-11]{lang="EN-US"}[的用户创建了闲置定时器。]{style="font-family:宋体"}*
