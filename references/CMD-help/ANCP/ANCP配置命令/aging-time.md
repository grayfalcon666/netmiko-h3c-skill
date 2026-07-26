::: {#202222485 .myid}
[]{#_Toc404785519}[]{#struct_0_x9115_x5297_558497965}

**ANCP \-- ANCP配置命令 \-- aging-time**

------------------------------------------------------------------------

[**[aging-time]{lang="EN-US"}**]{#struct_0_x9115_x5297_516764964}[命令用来配置线路表项的老化时间。]{style="font-family:宋体"}

[**[undo aging-time]{lang="EN-US"}**]{#struct_0_x9115_x5297_1198986069}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1355497662}

[**[aging-time]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x9115_x5297_363918414}

[**[undo aging-time]{lang="EN-US"}**]{#struct_0_x9115_x5297_1843673609}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1914384647}

[[线路表项的老化时间为]{style="font-family:宋体"}[150]{lang="EN-US"}]{#struct_0_x9115_x5297_x924147971}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1932620747}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_263430300}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x985695087}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_98208827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1139936841}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1478677822}

[*[value]{lang="EN-US"}*]{#struct_0_x9115_x5297_x1201268427}[：线路表项的老化时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示在线路状态变为]{style="font-family:宋体"}[Down]{lang="EN-US"}[时立即删除该线路表项。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_942873460}

[[线路表项即设备记录的用户]{style="font-family:宋体"}[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_1105231643}[线路信息。当用户所在的接入线路上线或变化时，设备会创建或更新相应线路表项。当用户所在的接入线路下线时，设备将在老化时间过后删除对应的线路表项。]{style="font-family:宋体"}

[[需要注意的是，如果]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_143038667}[客户端在收到设备下发的业务策略后需要将线路重启（即将线路]{style="font-family:宋体"}[down]{lang="EN-US"}[掉，让其重新接入），则需要在设备上配置较长的线路表项老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x9115_x5297_x2139542521}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1757397993}[配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[test1]{lang="EN-US"}[的线路表项的老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x405371691}

[\[sysname\] ancp neighbor test1]{lang="EN-US"}

[\[sysname-ancp-neighbor-test1\] aging-time 100]{lang="EN-US"}
:::

::: {#925550835 .myid}
[]{#_Toc404785520}[]{#struct_0_x9115_x5297_71919013}

**ANCP \-- ANCP配置命令 \-- ancp access-loop-configure**

------------------------------------------------------------------------

[**[ancp access-loop-configure]{lang="EN-US"}**]{#struct_0_x9115_x5297_x997272680}[命令用来向对端]{style="font-family:
宋体"}[DSLAM]{lang="EN-US"}[下发指定线路的业务策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1419232187}

[**[ancp]{lang="EN-US"}**[ **access-loop-configure** **circuit-id** *circuit-id* **service-profile** *profile-name* \[ **timeout** *time-value* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_x1377760409}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_444025573}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_207016263}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x88796840}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1334140809}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1073549175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1861781055}

[**[circuit-id]{lang="EN-US"}***[ circuit-id]{lang="EN-US"}*]{#struct_0_x9115_x5297_x1449200726}[：用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以通过]{style="font-family:宋体"}**[display ancp access-loop]{lang="EN-US"}**[命令查看用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_x2143062015}[：设备下发的业务策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[timeout ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_x9115_x5297_1005649354}[：系统等待对端回应的超时时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不关注对端回应。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1894006038}

[[执行本命令可以向对端]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_1212105188}[下发指定线路的业务策略，业务策略的具体参数（如]{style="font-family:宋体"}[QoS]{lang="EN-US"}[参数、带宽等）需要在对端的]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[设备上定义。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1476566321}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1806529938}[向接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[Dslam1/1:100]{lang="EN-US"}[的线路下发业务策略]{style="font-family:宋体"}[text-profile]{lang="EN-US"}[，不关注对端回应。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_348994745}

[\[Sysname\] ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile timeout 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1548694625}[指定接入线路不存在。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x1766134230}

[\[Sysname\] ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile]{lang="EN-US"}

[Issuing service profile name text-profile for Dslam1/1:100. Please wait...]{lang="EN-US"}

[Access line Dslam1/1:100 doesn't exist.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1139116314}[向接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[Dslam1/1:100]{lang="EN-US"}[的线路下发业务策略]{style="font-family:宋体"}[text-profile]{lang="EN-US"}[，下发成功。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_492534766}

[\[Sysname\] ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile timeout 10]{lang="EN-US"}

[Issuing service profile name text-profile for Dslam1/1:100. Please wait...]{lang="EN-US"}

[Issued the service profile name successfully.]{lang="EN-US"}

[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x809915875}[向接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[Dslam1/1:100]{lang="EN-US"}[的线路下发业务策略]{style="font-family:宋体"}[text-profile]{lang="EN-US"}[，下发失败。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_135477449}

[\[Sysname\] ancp access-loop-configure circuit-id Dslam1/1:100 service-profile text-profile]{lang="EN-US"}

[Issuing service profile name text-profile for Dslam1/1:100. Please wait...]{lang="EN-US"}

[Failed to issue the service profile name. Operation timed out.]{lang="EN-US"}

[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}

[[下发业务策略失败的原因还有如下几种：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1185000899}

[[Failed to issue the service profile name. ]{lang="EN-US"}]{#struct_0_x9115_x5297_1787019402}[]{#OLE_LINK13}[[Invalid request]{lang="EN-US"}]{#OLE_LINK12}[ message.]{lang="EN-US"}

[Failed to issue the service profile name. One or more of the specified ports are down.]{lang="EN-US"}

[Failed to issue the service profile name. Out of resources.]{lang="EN-US"}

[Failed to issue the service profile name. Request message type not implemented.]{lang="EN-US"}

[Failed to issue the service profile name. Malformed message.]{lang="EN-US"}

[Failed to issue the service profile name. Mandatory TLV missing.]{lang="EN-US"}

[Failed to issue the service profile name. Invalid TLV contents.]{lang="EN-US"}

[Failed to issue the service profile name. Unknown error.]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[下发业务策略结果显示信息描述表]{style="font-family:黑体"}]{#struct_0_x9115_x5297_264652596}

[]{#table_struct_0_x505083400}[[显示信息]{style="font-family:黑体"}]{#struct_0_x9115_x5297_478796200}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1429845071}

[[Access line Dslam1/1:100 doesn\'t exist]{lang="EN-US"}]{#struct_0_x9115_x5297_927541213}

[[指定接入线路不存在]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x88458398}

[[The DSL line configuration capability is not supported]{lang="EN-US"}]{#struct_0_x9115_x5297_1140641848}

[[指定接入线路对应的邻居不支持线路配置能力]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x128468949}

[[Issued the service profile name succeessfully]{lang="EN-US"}]{#struct_0_x9115_x5297_288335412}

[[下发业务策略成功]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x755352388}

[[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}]{#struct_0_x9115_x5297_2037844233}

[[该信息为对端]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x653249239}[反馈的详细信息，如果对端不反馈则不显示，具体显示信息请以实际情况为准]{style="font-family:宋体"}

[[Failed to issue the service profile name]{lang="EN-US"}]{#struct_0_x9115_x5297_136238870}

[[下发业务策略失败]{style="font-family:宋体"}]{#struct_0_x9115_x5297_102477591}

[[Operation timed out]{lang="EN-US"}]{#struct_0_x9115_x5297_906417583}

[[下发业务策略超时]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1640646469}

[[Invalid request message]{lang="EN-US"}]{#struct_0_x9115_x5297_x1694248890}

[[无效的请求报文]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x793580887}

[[One or more of the specified ports are down]{lang="EN-US"}]{#struct_0_x9115_x5297_x2080561651}

[[一个或者多个指定接入线路对应的端口状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x9115_x5297_x172672760}

[[Out of resources]{lang="EN-US"}]{#struct_0_x9115_x5297_1702322811}

[[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_682900181}[资源不足]{style="font-family:宋体"}

[[Request message type not implemented]{lang="EN-US"}]{#struct_0_x9115_x5297_1819511543}

[[请求报文类型不支持]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1908707299}

[[Malformed message]{lang="EN-US"}]{#struct_0_x9115_x5297_356614483}

[[非法报文]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x282583661}

[[Mandatory TLV missing]{lang="EN-US"}]{#struct_0_x9115_x5297_x994783182}

[[必要的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9115_x5297_x1026560544}[丢失]{style="font-family:宋体"}

[[Invalid TLV contents]{lang="EN-US"}]{#struct_0_x9115_x5297_1537596514}

[[无效的]{style="font-family:宋体"}[TLV]{lang="EN-US"}]{#struct_0_x9115_x5297_1575299904}[内容]{style="font-family:宋体"}

[[Unknown error]{lang="EN-US"}]{#struct_0_x9115_x5297_x1944118315}

[[未知的错误]{style="font-family:宋体"}]{#struct_0_x9115_x5297_454930453}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x557032378}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_1695615085}

::: {#1335874510 .myid}
[]{#_Toc404785521}[]{#struct_0_x9115_x5297_x496388541}[]{#_Toc185927308}[]{#_Toc123026768}

**ANCP \-- ANCP配置命令 \-- ancp enable**

------------------------------------------------------------------------

[**[ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_539523397}[命令用来使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_805431827}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_702342100}

[**[ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1349546479}

[**[undo ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1461276724}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_2065915007}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_684559625}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1916430821}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_324469923}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1967215882}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1523344627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1168155316}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1787708469}

[[只有在使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1837814322}[功能并配置了建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口后，系统才开始进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听并处理]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的请求和]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[业务。]{style="font-family:宋体"}

[[关闭]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_2105607338}[功能后，所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接会被断开，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听功能关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1795787397}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x288743747}[使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_1721356398}

[\[Sysname\] ancp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_480660163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ancp source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_337413195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1834633264}
:::

::: {#-732699466 .myid}
[]{#_Toc404785522}[]{#struct_0_x9115_x5297_x2003559402}

**ANCP \-- ANCP配置命令 \-- ancp neighbor**

------------------------------------------------------------------------

[**[ancp ]{lang="EN-US"}[neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_1593836455}[命令用来创建]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居并进入该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居视图。]{style="font-family:宋体"}

[**[undo ancp neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_1499414751}[命令用来删除指定的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_520366736}

[**[ancp neighbor]{lang="EN-US"}**[ *neighbor-name*]{lang="EN-US"}]{#struct_0_x9115_x5297_1526821247}

[**[undo ancp neighbor]{lang="EN-US"}**[ *neighbor-name*]{lang="EN-US"}]{#struct_0_x9115_x5297_x1698650250}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1553434242}

[[不存在]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x1959701988}[邻居。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x623276017}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1356130432}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x457150390}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1218645505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x178852947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1823796277}

[*[neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_x802076080}[：]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1376049580}

[[用户可以创建多个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_389225356}[邻居，并为每个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居分别配置参数，从而对每个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居进行单独管理。]{style="font-family:宋体"}

[[执行本命令时，如果不存在该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1754919446}[邻居则创建一个新的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居并进入该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居视图，如果存在该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居则直接进入该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居视图。]{style="font-family:宋体"}

[[删除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x1522772950}[邻居时，会清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居下的所有配置信息和状态信息，并断开已经建立的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接关系和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_2052502226}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x318689413}[创建]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[test1]{lang="EN-US"}[，并进入该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x1347026149}

[\[sysname\] ancp neighbor test1]{lang="EN-US"}

[\[sysname-ancp-neighbor-test1\]]{lang="EN-US"}
:::

::: {#-1692573373 .myid}
[]{#_Toc404785523}[]{#struct_0_x9115_x5297_1289721281}

**ANCP \-- ANCP配置命令 \-- ancp oam**

------------------------------------------------------------------------

[**[ancp oam]{lang="EN-US"}**]{#struct_0_x9115_x5297_942807924}[命令用来触发对指定接入线路的]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1300665633}

[**[ancp oam]{lang="EN-US"}**[ \[ **count** *test-counter* \| **timeout** *time-value* \] \* **access-loop** *circuit-id*]{lang="EN-US"}]{#struct_0_x9115_x5297_1219244141}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1515530281}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1121100115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_343754971}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_220216636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x839057352}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1601864665}

[**[count]{lang="EN-US"}[ ]{lang="EN-US"}***[test-counter]{lang="EN-US"}*]{#struct_0_x9115_x5297_1766782291}[：]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[进行探测的次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeout ]{lang="EN-US"}***[time-value]{lang="EN-US"}*]{#struct_0_x9115_x5297_335428775}[：系统等待]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[检测回应的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[access-loop]{lang="EN-US"}[ ]{lang="EN-US"}***[circuit-id]{lang="EN-US"}*]{#struct_0_x9115_x5297_1155132427}[：用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以通过]{style="font-family:宋体"}**[display ancp access-loop]{lang="EN-US"}**[命令查看用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_903560122}

[[ANCP OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x553927196}[检测用于检测用户的接入线路是否正常。]{style="font-family:宋体"}

[[执行本命令后，系统会向对端]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_789103287}[发送]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[检测消息，该消息中携带了本命令配置的各参数值。收到]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[检测消息后，]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[检测指定的接入线路的状态，最多进行]{style="font-family:宋体"}*[test-counter]{lang="EN-US"}*[次探测，并反馈检测结果。如果在本命令所配置的超时时间内未收到]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[的检测回应，则表明]{style="font-family:宋体"}[ANCP OAM]{lang="EN-US"}[检测失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1073614711}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x593113868}[配置对指定接入线路的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[检测，指定接入线路不存在。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x1557608498}

[\[sysname\] ancp oam count 5 timeout 5 access-loop Dslam1/1:100]{lang="EN-US"}

[OAM testing Dslam1/1:100. Please wait...]{lang="EN-US"}

[Access line Dslam1/1:100 doesn\'t exist.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x2013424516}[配置对指定接入线路的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[检测，检测结果成功。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_1760458615}

[\[sysname\] ancp oam count 5 timeout 5 access-loop Dslam1/1:100]{lang="EN-US"}

[OAM testing Dslam1/1:100. Please wait...]{lang="EN-US"}

[OAM test succeeded.]{lang="EN-US"}

[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_748072560}[配置对指定接入线路的]{style="font-family:宋体"}[OAM]{lang="EN-US"}[检测，检测结果失败。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_1328325678}

[\[sysname\] ancp oam count 5 timeout 5 access-loop Dslam2/1:100]{lang="EN-US"}

[OAM testing Dslam2/1:100. Please wait...]{lang="EN-US"}

[OAM test failed. Loopback test timed out]{lang="EN-US"}

[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}

[[检测结果还有如下几种：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x526395855}

[[The neighbor doesn\'t support OAM operation.]{lang="EN-US"}]{#struct_0_x9115_x5297_492469230}

[OAM test failed. One or more of the specified ports don't exist.]{lang="EN-US"}

[OAM test failed. Loopback test timed out.]{lang="EN-US"}

[OAM test failed. DSL access line status showtime.]{lang="EN-US"}

[OAM test failed. DSL access line status idle.]{lang="EN-US"}

[OAM test failed. DSL access line status silent.]{lang="EN-US"}

[OAM test failed. DSL access line status training.]{lang="EN-US"}

[OAM test failed. DSL access line integrity error.]{lang="EN-US"}

[OAM test failed. DSLAM resource not available.]{lang="EN-US"}

[OAM test failed. Invalid test parameter.]{lang="EN-US"}

[OAM test failed. Unknown error.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[ANCP OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x1164113703}[检测结果显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x507841468}[[显示信息]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1271478792}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1081977109}

[[Access line Dslam1/1:100 doesn\'t exist]{lang="EN-US"}]{#struct_0_x9115_x5297_x228873083}

[[指定接入线路不存在]{style="font-family:宋体"}]{#struct_0_x9115_x5297_21454773}

[[The neighbor doesn\'t support OAM operation.]{lang="EN-US"}]{#struct_0_x9115_x5297_1379593397}

[[指定接入线路对应的邻居不支持]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x1799968504}[检测能力]{style="font-family:宋体"}

[[OAM test succeeded]{lang="EN-US"}]{#struct_0_x9115_x5297_x1429910607}

[[OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_693979370}[检测成功]{style="font-family:宋体"}

[[Status info: xxxxxxxxxxxxxxxxxxxx]{lang="EN-US"}]{#struct_0_x9115_x5297_x1321506006}

[[该信息为对端]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x1333694205}[反馈的详细信息，如果对端不反馈则不显示，具体显示信息请以实际情况为准]{style="font-family:宋体"}

[[OAM test failed]{lang="EN-US"}]{#struct_0_x9115_x5297_x115159781}

[[OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x1711078833}[检测失败]{style="font-family:宋体"}

[[One or more of the specified ports don't exist]{lang="EN-US"}]{#struct_0_x9115_x5297_2141192871}

[[一个或者多个指定接入线路对应的端口不存在]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1043221943}

[[Loopback test timed out]{lang="EN-US"}]{#struct_0_x9115_x5297_136173334}

[[环回检测超时]{style="font-family:宋体"}]{#struct_0_x9115_x5297_964800832}

[[DSL access line status showtime]{lang="EN-US"}]{#struct_0_x9115_x5297_x2122447305}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_334040444}[接入线路状态为]{style="font-family:宋体"}[SHOWTIME]{lang="EN-US"}

[[关于]{style="font-family:宋体"}[SHOWTIME]{lang="EN-US"}]{#struct_0_x9115_x5297_x261068432}[状态的详细介绍请参见]{style="font-family:宋体"}[ITU-T G.993.2]{lang="EN-US"}

[[DSL access line status idle]{lang="EN-US"}]{#struct_0_x9115_x5297_x1876526199}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_709317092}[接入线路状态为]{style="font-family:宋体"}[IDLE]{lang="EN-US"}

[[关于]{style="font-family:宋体"}[IDLE]{lang="EN-US"}]{#struct_0_x9115_x5297_482557706}[状态的详细介绍请参见]{style="font-family:宋体"}[ITU-T G.993.2]{lang="EN-US"}

[[DSL access line status silent]{lang="EN-US"}]{#struct_0_x9115_x5297_1702257275}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_x949845505}[接入线路状态为]{style="font-family:宋体"}[SILENT]{lang="EN-US"}

[[关于]{style="font-family:宋体"}[SILENT]{lang="EN-US"}]{#struct_0_x9115_x5297_x1345801215}[状态的详细介绍请参见]{style="font-family:宋体"}[ITU-T G.993.2]{lang="EN-US"}

[[DSL access line status training]{lang="EN-US"}]{#struct_0_x9115_x5297_75300042}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_1645752876}[接入线路状态为]{style="font-family:宋体"}[TRAINING]{lang="EN-US"}

[[关于]{style="font-family:宋体"}[TRAINING]{lang="EN-US"}]{#struct_0_x9115_x5297_1390828087}[状态的详细介绍请参见]{style="font-family:宋体"}[ITU-T G.993.2]{lang="EN-US"}

[[DSL access line integrity error]{lang="EN-US"}]{#struct_0_x9115_x5297_x1695632683}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_x1026626080}[接入线路不完整]{style="font-family:宋体"}

[[DSLAM resource not available]{lang="EN-US"}]{#struct_0_x9115_x5297_411078367}

[[DSLAM]{lang="EN-US"}]{#struct_0_x9115_x5297_x215444809}[资源不可用]{style="font-family:宋体"}

[[Invalid test parameter]{lang="EN-US"}]{#struct_0_x9115_x5297_x1571576567}

[[检测参数非法]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x579423497}

[[Unknown error]{lang="EN-US"}]{#struct_0_x9115_x5297_x724273374}

[[未知的错误]{style="font-family:宋体"}]{#struct_0_x9115_x5297_605314689}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_511069072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_1717761253}

::: {#1103761060 .myid}
[]{#_Toc404785524}[]{#struct_0_x9115_x5297_x1422684125}

**ANCP \-- ANCP配置命令 \-- ancp session interval**

------------------------------------------------------------------------

[**[ancp session interval]{lang="EN-US"}**]{#struct_0_x9115_x5297_539457861}[命令用来配置发送邻接报文的时间间隔。]{style="font-family:宋体"}

[**[undo ancp session interval]{lang="EN-US"}**]{#struct_0_x9115_x5297_x774069449}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1763895331}

[**[ancp session interval]{lang="EN-US"}**[ *interval-value*]{lang="EN-US"}]{#struct_0_x9115_x5297_1365744077}

[**[undo ancp session]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_x9115_x5297_1908811230}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x804743298}

[[发送邻接报文的时间间隔为]{style="font-family:宋体"}[25]{lang="EN-US"}]{#struct_0_x9115_x5297_1662221555}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1540962131}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1734801298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1924869754}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1500531790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1417177112}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x913398734}

[*[interval-value]{lang="EN-US"}*]{#struct_0_x9115_x5297_515471127}[：发送邻接报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1698078744}

[[在]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x9115_x5297_837071832}[连接建立成功之后，]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端和]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[服务器都会向对端发送]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文试图建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接，]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文中携带本端配置的发送邻接报文时间间隔；]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接建立过程中，两端协商发送邻接报文的时间间隔（取两端配置的时间间隔中的较大值），后续]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[、]{style="font-family:宋体"}[ACK]{lang="EN-US"}[报文均以协商后的时间间隔发送。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_2105541802}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1755089959}[配置发送邻接报文的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x1053403822}

[\[sysname\] ancp session interval 15]{lang="EN-US"}
:::

::: {#522489833 .myid}
[]{#_Toc404785525}[]{#struct_0_x9115_x5297_1638476191}

**ANCP \-- ANCP配置命令 \-- ancp session retransmit**

------------------------------------------------------------------------

[**[ancp session retransmit]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1658705047}[命令用来配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接建立过程中]{style="font-family:宋体"}[SYN]{lang="EN-US"}[、]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文的最大重传次数。]{style="font-family:宋体"}

[**[undo ancp session retransmit]{lang="EN-US"}**]{#struct_0_x9115_x5297_1917045561}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x881564932}

[**[ancp session retransmit]{lang="EN-US"}**[ *retransmit-value*]{lang="EN-US"}]{#struct_0_x9115_x5297_1735071542}

[**[undo ancp session]{lang="EN-US"}[ retransmit]{lang="EN-US"}**]{#struct_0_x9115_x5297_1132765315}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1803301452}

[[SYN]{lang="EN-US"}]{#struct_0_x9115_x5297_x984152556}[、]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文的最大重传次数为]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_470899502}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_989484198}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x623341553}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_959411628}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x166764589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_330298331}

[*[retransmit-value]{lang="EN-US"}*]{#struct_0_x9115_x5297_x658528857}[：最大重传次数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1238460604}

[[在]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1484508009}[邻接建立过程中，如果在发送邻接报文的时间间隔内未收到对端回应的报文，则会向对端重新发送上一个报文。如果]{style="font-family:宋体"}[SYN]{lang="EN-US"}[或者]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文的重发次数达到该命令所配置的最大重传次数时还未收到对端回应的报文，则终止]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接建立过程，断开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1903088119}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1173567295}[配置]{style="font-family:宋体"}[SYN]{lang="EN-US"}[、]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文的最大重传次数为]{style="font-family:宋体"}[100]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x786069199}

[\[sysname\] ancp session retransmit 100]{lang="EN-US"}
:::

::: {#846476360 .myid}
[]{#_Toc404785526}[]{#struct_0_x9115_x5297_x1724247103}

**ANCP \-- ANCP配置命令 \-- ancp source-interface**

------------------------------------------------------------------------

[**[ancp source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_1211566892}[命令用来配置建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的全局源接口。]{style="font-family:宋体"}

[**[undo ancp source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_1028779457}[命令用来删除全局源接口的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1416213257}

[**[ancp source-interface loopback]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x9115_x5297_443500747}

[**[undo ancp source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1619877310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_942742388}

[[未配置全局源接口。]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1592700621}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1591977911}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1161740712}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1431196151}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1748970443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1128512846}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1492049225}

[**[loopback ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9115_x5297_601112380}[：[]{#_Hlt24945619}指定]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口为全局源接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_408979822}

[[只有在使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x92946950}[功能并配置了建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口后，系统才开始进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听并处理]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的请求和]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[业务。]{style="font-family:宋体"}

[[指定了源接口后，系统使用该源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9115_x5297_1623923403}[地址（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[主地址]{style="font-family:宋体"}[/]{lang="EN-US"}[第一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址）和]{style="font-family:宋体"}[6068]{lang="EN-US"}[端口号作为本端的源地址和源端口号进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听，与对端建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接；系统发送]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[报文的源地址为源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_161321097}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除源接口的配置后，]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1808074089}[TCP]{lang="EN-US"}[监听功能关闭；修改源接口后，使用新源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[6068]{lang="EN-US"}[端口号作为本端的源地址和源端口号进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听。对源接口的删除或者修改不会影响已经建立好的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[全局源接口对所有邻居生效，在邻居视图下配置的源接口只对当前邻居生效。如果同时配置了全局源接口和邻居视图下的源接口，则会优先使用邻居视图下配置的源接口。]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x622922162}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1777538320}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1580828980}[配置建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的全局源接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_x1073680247}

[\[sysname\] ancp source-interface loopback 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1297877920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1919366078}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_1382041513}
:::

::: {#1414888716 .myid}
[]{#_Toc404785527}[]{#struct_0_x9115_x5297_1940777996}

**ANCP \-- ANCP配置命令 \-- display ancp access-loop**

------------------------------------------------------------------------

[**[display ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_x775226265}[命令用来显示]{style="font-family:
宋体"}[ANCP]{lang="EN-US"}[接入线路表项信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_164871544}

[**[display ancp access-loop]{lang="EN-US"}**[ \[ **circuit-id** *circuit-id* \| **neighbor** *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_x499260001}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_921970051}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x305257779}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1171632502}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x618523832}

[[network-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_x626428755}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_492403694}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_x354732637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x414447239}

[**[circuit-id]{lang="EN-US"}***[ circuit-id]{lang="EN-US"}*]{#struct_0_x9115_x5297_x931772615}[：用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以通过]{style="font-family:宋体"}**[display ancp access-loop]{lang="EN-US"}**[命令查看用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}***[ neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_x1969173523}[：]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_607012479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何参数，则显示所有接入线路表项的简要信息。]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x873666156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1697464730}**[circuit-id]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，则显示指定接入线路的详细信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x9115_x5297_497988825}**[neighbor]{lang="EN-US"}**[参数，则显示指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居下的所有接入线路表项的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1865778751}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x613975312}[显示所有接入线路表项的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp access-loop]{lang="EN-US"}]{#struct_0_x9115_x5297_x1731120943}

[Total entries: 1]{lang="EN-US"}

[Neighbor name     Peer ID           Circuit ID         State]{lang="EN-US"}

[bras              0001-0002-0003    circuit4:430       UP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x853381599}[显示指定接入线路的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp access-loop circuit-id circuit4:430]{lang="EN-US"}]{#struct_0_x9115_x5297_x1429976143}

[Neighbor name                       : bras]{lang="EN-US"}

[Circuit ID                          : circuit4:430]{lang="EN-US"}

[Remote ID                           : -]{lang="EN-US"}

[Peer ID                             : 0001-0002-0003]{lang="EN-US"}

[DSL type                            : ADSL1]{lang="EN-US"}

[Actual data rate upstream           : 64 kbps]{lang="EN-US"}

[Actual data rate downstream         : 128 kbps]{lang="EN-US"}

[Min data rate upstream              : 32 kbps]{lang="EN-US"}

[Min data rate downstream            : 32 kbps]{lang="EN-US"}

[Attainable data rate upstream       : 1024 kbps]{lang="EN-US"}

[Attainable data rate downstream     : 8192 kbps]{lang="EN-US"}

[Max data rate upstream              : 1024 kbps]{lang="EN-US"}

[Max data rate downstream            : 8192 kbps]{lang="EN-US"}

[Min low power data rate upstream    : 32 kbps]{lang="EN-US"}

[Min low power data rate downstream  : 32 kbps]{lang="EN-US"}

[Max delay upstream                  : 20 s]{lang="EN-US"}

[Max delay downstream                : 8192 s]{lang="EN-US"}

[Actual delay upstream               : 20 s]{lang="EN-US"}

[Actual delay downstream             : 20 s]{lang="EN-US"}

[Data link                           : ETHERNET]{lang="EN-US"}

[Encapsulation 1                     : Untagged Ethernet]{lang="EN-US"}

[Encapsulation 2                     : NA]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1808996623}[显示指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居下的所有接入线路表项的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp access-loop neighbor dslam1]{lang="EN-US"}]{#struct_0_x9115_x5297_1391070199}

[Total entries: 1]{lang="EN-US"}

[Neighbor name    Peer ID               Circuit ID                       State]{lang="EN-US"}

[dslam1           0001-0002-0003        001882362CFF eth 0/3/0/2:6       UP]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ancp access-loop]{lang="EN-US"}]{#struct_0_x9115_x5297_1402951844}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x515511320}[[字段]{style="font-family:黑体"}]{#struct_0_x9115_x5297_642750306}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9115_x5297_136107798}

[[Total entries]{lang="EN-US"}]{#struct_0_x9115_x5297_1387365377}

[[表项总数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1286651547}

[[Neighbor name]{lang="EN-US"}]{#struct_0_x9115_x5297_x99357753}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1506777760}[邻居的名称]{style="font-family:宋体"}

[[Peer ID]{lang="EN-US"}]{#struct_0_x9115_x5297_x1443331757}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x858322265}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[，即线路所属的]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_x9115_x5297_541460728}

[[接入线路的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9115_x5297_1702191739}

[[Remote ID]{lang="EN-US"}]{#struct_0_x9115_x5297_x515073946}

[[远程]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x9115_x5297_x1875151901}

[[State]{lang="EN-US"}]{#struct_0_x9115_x5297_x1726444820}

[[接入线路的状态，线路在线则为]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x9115_x5297_2003414438}[状态，反之为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[DSL type]{lang="EN-US"}]{#struct_0_x9115_x5297_x700913060}

[[DSL]{lang="EN-US"}]{#struct_0_x9115_x5297_376274217}[类型：]{style="font-family:宋体"}[ADSL1]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL2]{lang="EN-US"}[、]{style="font-family:宋体"}[ADSL2+]{lang="EN-US"}[、]{style="font-family:宋体"}[VDSL1]{lang="EN-US"}[、]{style="font-family:宋体"}[VDSL2]{lang="EN-US"}[、]{style="font-family:宋体"}[SDSL]{lang="EN-US"}[、]{style="font-family:宋体"}[Other]{lang="EN-US"}

[[Actual data rate upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_1727018151}

[[接入线路的实际上行速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_x1867261764}

[[Actual data rate downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x1026691616}

[[接入线路的实际下行速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_2113622472}

[[Min data rate upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_1206849459}

[[接入线路的上行最小速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_x338215848}

[[Min data rate downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x2005886234}

[[接入线路的下行最小速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_1312230366}

[[Attainable data rate upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x911014551}

[[接入线路的上行可获速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_539392325}

[[Attainable data rate downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x269489970}

[[接入线路的下行可获速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_x2098663156}

[[Max data rate upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x823528598}

[[接入线路的上行最大速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_x502094310}

[[Max data rate downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_x42876182}

[[接入线路的下行最大速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_252605976}

[[Min low power data rate upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_1759461579}

[[接入线路的上行低压最小速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_2105476266}

[[Min low power data rate downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_2098397473}

[[接入线路的下行低压最小速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x9115_x5297_x1930706911}

[[Max delay upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_869439876}

[[接入线路的上行最大时延，单位为秒]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1471598016}

[[Max delay downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_34901901}

[[接入线路的下行最大时延，单位为秒]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x623407089}

[[Actual delay upstream]{lang="EN-US"}]{#struct_0_x9115_x5297_1362332868}

[[接入线路的上行实际时延，单位为秒]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1853866717}

[[Actual delay downstream]{lang="EN-US"}]{#struct_0_x9115_x5297_708197967}

[[接入线路的下行实际时延，单位为秒]{style="font-family:宋体"}]{#struct_0_x9115_x5297_474164887}

[[Data link]{lang="EN-US"}]{#struct_0_x9115_x5297_2145965169}

[[数据链路类型：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1940465611}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ATM ALL5]{lang="EN-US"}]{#struct_0_x9115_x5297_942676852}[：]{lang="EN-US" style="font-family:宋体"}[ATM]{lang="EN-US"}[链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETHERNET]{lang="EN-US"}]{#struct_0_x9115_x5297_x1144129951}[：以太网链路]{lang="EN-US" style="font-family:宋体"}

[[Encapsulation 1]{lang="EN-US"}]{#struct_0_x9115_x5297_x158987302}

[[封装头]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x9115_x5297_1402061489}[的信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x9115_x5297_1404803197}[：不携带封装头]{style="font-family:宋体"}[1]{lang="EN-US"}[的信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Untagged Ethernet]{lang="EN-US"}]{#struct_0_x9115_x5297_x686051762}[：不带]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的以太网报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Single-tagged Ethernet]{lang="EN-US"}]{#struct_0_x9115_x5297_14989470}[：携带一层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的以太网报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Double-tagged Ethernet]{lang="EN-US"}]{#struct_0_x9115_x5297_x1073745783}[：携带双层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的以太网报文]{style="font-family:宋体"}

[[Encapsulation 2]{lang="EN-US"}]{#struct_0_x9115_x5297_556514853}

[[封装头]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x9115_x5297_1802149329}[的信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_x9115_x5297_1721777468}[：不携带封装头]{style="font-family:宋体"}[2]{lang="EN-US"}[的信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPPoA LLC]{lang="EN-US"}]{#struct_0_x9115_x5297_101891805}[：基于逻辑链路控制的]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PPPoA Null]{lang="EN-US"}]{#struct_0_x9115_x5297_492338158}[：]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPoA LLC]{lang="EN-US"}]{#struct_0_x9115_x5297_1685033825}[：基于逻辑链路控制的]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPoA Null]{lang="EN-US"}]{#struct_0_x9115_x5297_x1355480360}[：]{style="font-family:宋体"}[IPoA]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet over AAL5 LLC with FCS]{lang="EN-US"}]{#struct_0_x9115_x5297_1139680343}[：携带]{style="font-family:
  宋体"}[FCS]{lang="EN-US"}[校验的基于]{style="font-family:宋体"}[ATM]{lang="EN-US"}[逻辑链路控制的以太网报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet over AAL5 LLC without FCS]{lang="EN-US"}]{#struct_0_x9115_x5297_478155989}[：不携带]{style="font-family:宋体"}[FCS]{lang="EN-US"}[校验的基于]{style="font-family:宋体"}[ATM]{lang="EN-US"}[逻辑链路控制的以太网报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet over AAL5 NULL with FCS]{lang="EN-US"}]{#struct_0_x9115_x5297_x1430041679}[：携带]{style="font-family:
  宋体"}[FCS]{lang="EN-US"}[校验的基于]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的以太网报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet over AAL5 NULL without FCS]{lang="EN-US"}]{#struct_0_x9115_x5297_1135725418}[：不携带]{style="font-family:宋体"}[FCS]{lang="EN-US"}[校验的基于]{style="font-family:宋体"}[ATM]{lang="EN-US"}[的以太网报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1594936756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1355530050}

::: {#-1960499303 .myid}
[]{#_Toc404785528}[]{#struct_0_x9115_x5297_696604955}[]{#_Toc349839370}

**ANCP \-- ANCP配置命令 \-- display ancp neighbor**

------------------------------------------------------------------------

[**[display ancp neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_872089095}[命令用来显示]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居信息，包括配置信息与状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x644460941}

[**[display ancp neighbor]{lang="EN-US"}**[ \[ *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_x180547247}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1004380832}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1556667376}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_582295644}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_136042262}

[[network-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_x1736622976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1342887955}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_x1341721032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x2122982367}

[*[neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_2133106522}[：]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1418715391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_x9115_x5297_69689306}[ANCP]{lang="EN-US"}[邻居的名称，则显示当前所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的简要信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1531559119}[ANCP]{lang="EN-US"}[邻居的名称，则显示指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x9115_x5297_968684334}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1913446038}[显示所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp neighbor]{lang="EN-US"}]{#struct_0_x9115_x5297_1092966105}

[Total entries: 2]{lang="EN-US"}

[Neighbor name       Peer ID             State      Access loop number]{lang="EN-US"}

[default-neighbor    -                   Unused     0]{lang="EN-US"}

[dslam1              0001-0002-0003      Used       3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1521270596}[显示指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp neighbor dslam1]{lang="EN-US"}]{#struct_0_x9115_x5297_1702126203}

[Neighbor name                        : dslam1]{lang="EN-US"}

[Peer ID                              : 0001-0002-0003]{lang="EN-US"}

[Source interface                     : LoopBack1]{lang="EN-US"}

[Session message interval             : 25 s]{lang="EN-US"}

[Session message retransmit           : 255]{lang="EN-US"}

[Aging time                           : 150 s]{lang="EN-US"}

[State                                : Used]{lang="EN-US"}

[Peer IP                              : 1.1.1.1]{lang="EN-US"}

[Peer port                            : 8093]{lang="EN-US"}

[Neighbor capacities                  : discovery, line-cfg, oam]{lang="EN-US"}

[Negotiated interval                  : 25.0 s]{lang="EN-US"}

[Access loop number                   : 0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ancp neighbor]{lang="EN-US"}]{#struct_0_x9115_x5297_625085696}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x519281308}[[字段]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1657359600}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9115_x5297_2134922608}

[[Total entries]{lang="EN-US"}]{#struct_0_x9115_x5297_x1944063865}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_2044717435}[邻居总数]{style="font-family:宋体"}

[[Neighbor name]{lang="EN-US"}]{#struct_0_x9115_x5297_x571609040}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1410132305}[邻居的名称]{style="font-family:宋体"}

[[Peer ID]{lang="EN-US"}]{#struct_0_x9115_x5297_1260002256}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x754303739}[邻居的]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Source interface]{lang="EN-US"}]{#struct_0_x9115_x5297_x1026757152}

[[建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_969933893}[邻接的源接口]{style="font-family:宋体"}

[[Session message interval]{lang="EN-US"}]{#struct_0_x9115_x5297_x387198468}

[[用户配置的发送邻接报文的时间间隔]{style="font-family:宋体"}]{#struct_0_x9115_x5297_2100600713}

[[Session message retransmit]{lang="EN-US"}]{#struct_0_x9115_x5297_436344748}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1999335298}[邻接建立过程中]{style="font-family:宋体"}[SYN]{lang="EN-US"}[、]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}[报文的最大重传次数]{style="font-family:宋体"}

[[Aging time]{lang="EN-US"}]{#struct_0_x9115_x5297_1474803354}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_551594141}[邻居的接入线路表项的老化时间]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x9115_x5297_x375882115}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x314250184}[邻居的使用情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Used]{lang="EN-US"}]{#struct_0_x9115_x5297_x1012215309}[：表示已使用该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居，即]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备和该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居对应的]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[之间已经建立了邻接关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unused]{lang="EN-US"}]{#struct_0_x9115_x5297_539326789}[：表示未使用该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居，即]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备和该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居对应的]{style="font-family:宋体"}[DSLAM]{lang="EN-US"}[之间还没有建立邻接关系]{style="font-family:宋体"}

[[Peer IP]{lang="EN-US"}]{#struct_0_x9115_x5297_917748877}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1721740624}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Peer port]{lang="EN-US"}]{#struct_0_x9115_x5297_x1072483460}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x1840885152}[邻居的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Neighbor capacities]{lang="EN-US"}]{#struct_0_x9115_x5297_88065460}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1033174567}[邻居支持的能力集：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[discovery]{lang="EN-US"}]{#struct_0_x9115_x5297_1908032146}[：]{lang="EN-US" style="font-family:宋体"}[动态拓扑发现]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[line-cfg]{lang="EN-US"}]{#struct_0_x9115_x5297_2105410730}[：]{lang="EN-US" style="font-family:宋体"}[线路配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[oam]{lang="EN-US"}]{#struct_0_x9115_x5297_x633661456}[：]{lang="EN-US" style="font-family:宋体"}[OAM]{lang="EN-US"}[检测]{lang="EN-US" style="font-family:宋体"}

[[Neigotiated interval ]{lang="EN-US"}]{#struct_0_x9115_x5297_x851349954}

[[两端协商后的发送邻接报文的时间间隔]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x479190422}

[[Access loop number]{lang="EN-US"}]{#struct_0_x9115_x5297_1027604986}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1919770938}[邻居下接入线路总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1875376953}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ancp neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_x623472625}

::: {#-632184769 .myid}
[]{#_Toc404785529}[]{#struct_0_x9115_x5297_1351674511}[]{#display_ancp_neighbor-profile__tb_01}[]{#tb_01}

**ANCP \-- ANCP配置命令 \-- display ancp statistic**

------------------------------------------------------------------------

[**[display ancp statistic]{lang="EN-US"}**]{#struct_0_x9115_x5297_x510700958}[命令用来显示]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1073074882}

[**[display ancp statistic]{lang="EN-US"}**[ \[ **neighbor** *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_1744439147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x94085952}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x467981497}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1849595469}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1232594268}

[[network-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_x1360838138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1553838973}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9115_x5297_1531365607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_942611316}

[**[neighbor]{lang="EN-US"}***[ neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_1624485788}[：查看指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定本参数时，将显示所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1915234926}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1743704133}[显示当前所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ancp statistic]{lang="EN-US"}]{#struct_0_x9115_x5297_x1073811319}

[Received ack packets                  : 1311]{lang="EN-US"}

[Received syn packets                  : 0]{lang="EN-US"}

[Received synack packets               : 2]{lang="EN-US"}

[Received reset ack packets            : 0]{lang="EN-US"}

[Received port up packets              : 1]{lang="EN-US"}

[Received port down packets            : 0]{lang="EN-US"}

[Received oam packets                  : 0]{lang="EN-US"}

[Received access loop config packets   : 0]{lang="EN-US"}

[Received update packets               : 0]{lang="EN-US"}

[Received generic response packets     : 0]{lang="EN-US"}

[Received unknown packets              : 0]{lang="EN-US"}

[Dropped packets                       : 0]{lang="EN-US"}

[Sent ack packets                      : 1311]{lang="EN-US"}

[Sent syn packets                      : 6]{lang="EN-US"}

[Sent synack packets                   : 0]{lang="EN-US"}

[Sent reset ack packets                : 0]{lang="EN-US"}

[Sent oam packets                      : 0]{lang="EN-US"}

[Sent access loop config packets       : 0]{lang="EN-US"}

[Sent generic response packets         : 0]{lang="EN-US"}

[]{#OLE_LINK19}[[Packet]{lang="EN-US"}]{#OLE_LINK18}[s failing to be sent            : 0]{lang="EN-US"}

[]{#OLE_LINK15}[[Adjacency]{lang="EN-US"}]{#OLE_LINK14}[ up                          : 2]{lang="EN-US"}

[Adjacency failed                      : 0]{lang="EN-US"}

[Adjacency down                        : 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x651529784}[显示指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\>display ancp statistic neighbor dslam1]{lang="EN-US"}]{#struct_0_x9115_x5297_x244964690}

[Received ack packets                  : 981]{lang="EN-US"}

[Received syn packets                  : 0]{lang="EN-US"}

[Received synack packets               : 1]{lang="EN-US"}

[Received reset ack packets            : 0]{lang="EN-US"}

[Received port up packets              : 1]{lang="EN-US"}

[Received port down packets            : 0]{lang="EN-US"}

[Received oam packets                  : 0]{lang="EN-US"}

[Received access loop config packets   : 0]{lang="EN-US"}

[Received update packets               : 0]{lang="EN-US"}

[Received generic response packets     : 0]{lang="EN-US"}

[Received unknown packets              : 0]{lang="EN-US"}

[Dropped packets                       : 0]{lang="EN-US"}

[Sent ack packets                      : 981]{lang="EN-US"}

[Sent syn packets                      : 1]{lang="EN-US"}

[Sent synack packets                   : 1]{lang="EN-US"}

[Sent reset ack packets                : 0]{lang="EN-US"}

[Sent oam packets                      : 0]{lang="EN-US"}

[Sent access loop config packets       : 0]{lang="EN-US"}

[Sent generic response packets         : 0]{lang="EN-US"}

[Packets failing to be sent            : 0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ancp statistic]{lang="EN-US"}]{#struct_0_x9115_x5297_1630093136}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x489292434}[[字段]{style="font-family:黑体"}]{#struct_0_x9115_x5297_802916792}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9115_x5297_2098321647}

[[Received ack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_834262762}

[[接收的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x9115_x5297_492272622}[报文数]{style="font-family:宋体"}

[[Received syn packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1047316982}

[[接收的]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x9115_x5297_1388176452}[报文数]{style="font-family:宋体"}

[[Received synack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x841064306}

[[接收的]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}]{#struct_0_x9115_x5297_171392510}[报文数]{style="font-family:宋体"}

[[Received reset ack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1577098802}

[[接收的]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}]{#struct_0_x9115_x5297_21109607}[报文数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}]{#struct_0_x9115_x5297_1541207294}[报文：一种邻接报文，用于重置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接）]{style="font-family:宋体"}

[[Received port up packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1198785271}

[[接收的]{style="font-family:宋体"}[Port Up]{lang="EN-US"}]{#struct_0_x9115_x5297_1062689831}[报文数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[Port Up]{lang="EN-US"}]{#struct_0_x9115_x5297_x1430107215}[报文：线路上线报文。当]{style="font-family:宋体"}[AN]{lang="EN-US"}[感知到下挂线路上线时会发送]{style="font-family:宋体"}[Port Up]{lang="EN-US"}[报文通知]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备上线接入线路的参数）]{style="font-family:宋体"}

[[Received port down packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x2028922642}

[[接收的]{style="font-family:宋体"}[Port Down]{lang="EN-US"}]{#struct_0_x9115_x5297_x1234459159}[报文数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[Port Down]{lang="EN-US"}]{#struct_0_x9115_x5297_x1793862262}[报文：线路下线报文。当]{style="font-family:宋体"}[AN]{lang="EN-US"}[感知到下挂线路下线时会发送]{style="font-family:宋体"}[Port Down]{lang="EN-US"}[报文通知]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备删除接入线路的参数）]{style="font-family:宋体"}

[[Received oam packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1395534915}

[[接收的线路]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_903889498}[检测报文数]{style="font-family:宋体"}

[[Received access loop config packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x893230793}

[[接收的线路配置报文数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_135976726}

[[Received unknown packets]{lang="EN-US"}]{#struct_0_x9115_x5297_487978105}

[[接收的未知报文数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x116020271}

[[Received update packets]{lang="EN-US"}]{#struct_0_x9115_x5297_1738789302}

[[接收的]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_x9115_x5297_840713462}[报文数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[Update]{lang="EN-US"}]{#struct_0_x9115_x5297_1929711616}[报文：邻接更新报文。当组网环境中出现其它]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备时，]{style="font-family:宋体"}[AN]{lang="EN-US"}[发送邻接更新报文通知]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备组网环境中存在]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备的数目和]{style="font-family:宋体"}[AN]{lang="EN-US"}[端下挂的接入线路数目）]{style="font-family:宋体"}

[[Received generic response packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x302667749}

[[接收的]{style="font-family:宋体"}[Generic Response]{lang="EN-US"}]{#struct_0_x9115_x5297_1702060667}[报文数]{style="font-family:宋体"}

[[（]{style="font-family:宋体"}[Generic Response]{lang="EN-US"}]{#struct_0_x9115_x5297_x1317592081}[报文：一般应答报文。该报文可以作为给请求报文的应答，也可以因为某种错误原因主动发送）]{style="font-family:宋体"}

[[Dropped packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x2073714679}

[[丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x171478581}

[[Sent ack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_1310416303}

[[发送的]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x9115_x5297_x776409641}[报文数]{style="font-family:宋体"}

[[Sent syn packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1026822688}

[[发送的]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x9115_x5297_219820985}[报文数]{style="font-family:宋体"}

[[Sent synack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1349504396}

[[发送的]{style="font-family:宋体"}[SYNACK]{lang="EN-US"}]{#struct_0_x9115_x5297_x1889766934}[报文数]{style="font-family:宋体"}

[[Sent reset ack packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x529441997}

[[发送的]{style="font-family:宋体"}[RSTACK]{lang="EN-US"}]{#struct_0_x9115_x5297_x1504152069}[报文数]{style="font-family:宋体"}

[[Sent oam packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x308677712}

[[发送的线路]{style="font-family:宋体"}[OAM]{lang="EN-US"}]{#struct_0_x9115_x5297_539261253}[检测报文数]{style="font-family:宋体"}

[[Sent access loop config packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x661102794}

[[发送的线路配置报文数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1699875309}

[[Sent generic response packets]{lang="EN-US"}]{#struct_0_x9115_x5297_x1574128267}

[[发送的]{style="font-family:宋体"}[Generic Response]{lang="EN-US"}]{#struct_0_x9115_x5297_1783001160}[报文数]{style="font-family:宋体"}

[[Packets failing to be sent]{lang="EN-US"}]{#struct_0_x9115_x5297_x1482167278}

[[发送失败的报文数]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x965660591}

[[Adjancency up]{lang="EN-US"}]{#struct_0_x9115_x5297_2105345194}

[[建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x1023713836}[邻接成功的次数]{style="font-family:宋体"}

[[Adjancency failed]{lang="EN-US"}]{#struct_0_x9115_x5297_x1326444205}

[[建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_714946663}[邻接失败的次数]{style="font-family:宋体"}

[[Adjancency down]{lang="EN-US"}]{#struct_0_x9115_x5297_1282305479}

[[关闭]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_2128068251}[邻接的次数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_333499452}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ancp statistic]{lang="EN-US"}**]{#struct_0_x9115_x5297_1414347016}

::: {#1861968652 .myid}
[]{#_Toc404785530}[]{#struct_0_x9115_x5297_x548701724}

**ANCP \-- ANCP配置命令 \-- peer-id**

------------------------------------------------------------------------

[**[peer-id]{lang="EN-US"}**]{#struct_0_x9115_x5297_x578648567}[命令用来配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo peer-id]{lang="EN-US"}**]{#struct_0_x9115_x5297_2044288490}[命令用来取消已配置的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_529062900}

[**[peer-id]{lang="EN-US"}**[ *peer-id*]{lang="EN-US"}]{#struct_0_x9115_x5297_x623538161}

[**[undo peer-id]{lang="EN-US"}**]{#struct_0_x9115_x5297_2110694934}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x634729647}

[[未配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_x1402924298}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x683651011}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1072937415}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_168131304}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x365296899}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1511513147}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x894654804}

[*[peer-id]{lang="EN-US"}*]{#struct_0_x9115_x5297_842987731}[：]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[，即]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，唯一标识一个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居，形式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_685300183}

[[TCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1780978420}[连接建立后，]{style="font-family:宋体"}[BRAS]{lang="EN-US"}[设备根据]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址来判断]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端所属的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居。如果]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与某个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[匹配，则该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端就属于该]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_232640884}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1553216329}[ANCP]{lang="EN-US"}[邻居只能配置一个]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[。不同]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居不允许配置相同的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[取消已配置的]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1841243999}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[时，会断开已经建立的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接关系和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x2139697292}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1291849884}[配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[test1]{lang="EN-US"}[的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1-2-3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_942545780}

[[\[sysname\] ancp neighbor test1]{lang="EN-US"}]{#struct_0_x9115_x5297_250731625}

[[\[sysname-ancp-neighbor-test1\] peer-id 1-2-3]{lang="EN-US"}]{#struct_0_x9115_x5297_1321795576}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1176688053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ancp ]{lang="EN-US"}[neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_131502056}
:::

::: {#1467229070 .myid}
[]{#_Toc404785531}[]{#struct_0_x9115_x5297_144114987}

**ANCP \-- ANCP配置命令 \-- reset ancp access-loop**

------------------------------------------------------------------------

[**[reset ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_949706029}[命令用来清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[接入线路表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x61508036}

[**[reset ancp access-loop]{lang="EN-US"}**[ \[ **circuit-id** *circuit-id* \| **neighbor** *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_x326905418}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_790471661}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_1821897430}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1276755518}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1032940936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x1426556554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x387581785}

[**[circuit-id]{lang="EN-US"}***[ circuit-id]{lang="EN-US"}*]{#struct_0_x9115_x5297_x1825130130}[：用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以通过]{style="font-family:宋体"}**[display ancp access-loop]{lang="EN-US"}**[命令查看用户的接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[neighbor]{lang="EN-US"}***[ neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_x184422814}[：]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x353543245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何参数，则清除所有]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1073876855}[ANCP]{lang="EN-US"}[接入线路表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x9115_x5297_1705226071}**[circuit-id]{lang="EN-US"}**[参数]{style="font-family:宋体"}[，则清除指定接入线路的表项；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_1294667108}[参数，则清除指定]{lang="EN-US" style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居下的所有接入线路表项。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_179358982}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x873775464}[清除接入线路]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0001-0002-0003 eth 1/162 3:11]{lang="EN-US"}[的线路表项。]{style="font-family:宋体"}

[[\<Sysname\> reset ancp access-loop circuit-id "0001-0002-0003 eth 1/162 3:11"]{lang="EN-US"}]{#struct_0_x9115_x5297_1815371889}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1689677659}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ancp access-loop]{lang="EN-US"}**]{#struct_0_x9115_x5297_628273092}
:::

::: {#-293702194 .myid}
[]{#_Toc404785532}[]{#struct_0_x9115_x5297_x1348511512}

**ANCP \-- ANCP配置命令 \-- reset ancp neighbor**

------------------------------------------------------------------------

[**[reset ancp neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_1146153970}[命令用来清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的状态信息，并关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1843842847}

[**[reset ancp neighbor]{lang="EN-US"}**[ \[ *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_2032949660}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x2019674232}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x386283811}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1815883860}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x930554548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_5181452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x15434241}

[*[neighbor-name]{lang="EN-US"}*]{#struct_0_x9115_x5297_492207086}[：清除指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的状态信息，并关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，将清除所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的状态信息，并关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1807016233}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1662093824}[清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[的状态信息，并关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[\<Sysname\> reset ancp neighbor dslam1]{lang="EN-US"}]{#struct_0_x9115_x5297_791982494}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_458407703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ancp neighbor]{lang="EN-US"}**]{#struct_0_x9115_x5297_1653456960}
:::

::: {#-1219467142 .myid}
[]{#_Toc350359509}[]{#_Toc404785533}[]{#struct_0_x9115_x5297_2057595112}[]{#_Toc350359511}

**ANCP \-- ANCP配置命令 \-- reset ancp statistic**

------------------------------------------------------------------------

[**[reset ancp statistic]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1336159829}[命令用来清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1704322372}

[**[reset ancp statistic]{lang="EN-US"}**[ \[ **neighbor** *neighbor-name* \]]{lang="EN-US"}]{#struct_0_x9115_x5297_141179607}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1893405183}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9115_x5297_483692918}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1739796228}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1253583745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_x467220839}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1434919071}

[**[neighbor]{lang="EN-US"}**[ *neighbor-name*]{lang="EN-US"}]{#struct_0_x9115_x5297_x1648344012}[：清除指定]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}*[neighbor-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定本参数时，将清除所有]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x37879313}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_x1295889487}[清除]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[dslam1]{lang="EN-US"}[的]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ancp statistic neighbor dslam1]{lang="EN-US"}]{#struct_0_x9115_x5297_x1713718071}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1055752935}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ancp statistic]{lang="EN-US"}**]{#struct_0_x9115_x5297_111067024}
:::

::: {#1089642682 .myid}
[]{#_Toc404785534}[]{#struct_0_x9115_x5297_156763359}[]{#_Toc349839362}

**ANCP \-- ANCP配置命令 \-- source-interface**

------------------------------------------------------------------------

[**[source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_487043427}[命令用来在邻居视图下配置建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口。]{style="font-family:宋体"}

[**[undo source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_x1943735561}[命令用来删除邻居视图下所配置的建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1317630510}

[**[source-interface loopback]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x9115_x5297_x1120664350}

[**[undo source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_196130369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1105219143}

[[未配置邻居视图下的源接口。]{style="font-family:宋体"}]{#struct_0_x9115_x5297_2066299504}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_572331724}

[[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_764456543}[邻居视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_175033336}

[[network-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1905837924}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9115_x5297_1090093237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x980682019}

[**[loopback ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x9115_x5297_270194454}[：指定]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口为源接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_x1188960121}

[[只有在使能]{style="font-family:宋体"}[ANCP]{lang="EN-US"}]{#struct_0_x9115_x5297_1125395522}[功能并配置了建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口后，系统才开始进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听并处理]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[客户端建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的请求和]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[业务。]{style="font-family:宋体"}

[[指定了源接口后，系统使用该源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9115_x5297_x912206284}[地址（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[主地址]{style="font-family:宋体"}[/]{lang="EN-US"}[第一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[全球单播地址）和]{style="font-family:宋体"}[6068]{lang="EN-US"}[端口号作为本端的源地址和源端口号进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听，与对端建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接；系统发送]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[报文的源地址为源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1437615319}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除源接口配置后，]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x1104889181}[TCP]{lang="EN-US"}[监听功能关闭；修改源接口后，使用新源接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[6068]{lang="EN-US"}[端口号作为本端的源地址和源端口号进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听。对源接口的删除或者修改不会影响已经建立好的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在邻居视图下配置的源接口只对当前邻居生效。如果同时配置了全局源接口和邻居视图下的源接口，则会优先使用邻居视图下配置的源接口。]{style="font-family:宋体"}]{#struct_0_x9115_x5297_x2074846304}

[[【举例】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x9115_x5297_1509819783}

[[\# ]{lang="EN-US"}]{#struct_0_x9115_x5297_1502559324}[配置]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[test1]{lang="EN-US"}[建立]{style="font-family:宋体"}[ANCP]{lang="EN-US"}[邻接的源接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9115_x5297_740768955}

[[\[sysname\] ancp neighbor test1]{lang="EN-US"}]{#struct_0_x9115_x5297_717759148}

[[\[sysname-ancp-neighbor-test1\] source-interface loopback 100]{lang="EN-US"}]{#struct_0_x9115_x5297_2067899979}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9115_x5297_1739527693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ancp enable]{lang="EN-US"}**]{#struct_0_x9115_x5297_2040182445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ancp ]{lang="EN-US"}[source-interface]{lang="EN-US"}**]{#struct_0_x9115_x5297_1240288698}
:::
