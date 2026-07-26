::: {#-1804984392 .myid}
[]{#_Toc404796449}[]{#struct_0_x1358_x5075_x427181683}

**NQA \-- NQA调试命令 \-- debugging nqa**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_2032170344}

[**[debugging nqa]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **reaction** }]{lang="EN-US"}]{#struct_0_x1358_x5075_x845281227}

[**[undo debugging nqa]{lang="EN-US"}**[ { **all** \| **error** \| **event** \| **reaction** }]{lang="EN-US"}]{#struct_0_x1358_x5075_x461470395}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_1447371083}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1372079988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_154026664}

[[network-admin]{lang="EN-US"}]{#struct_0_x1358_x5075_x1935964039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1358_x5075_1435894927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_x762201152}

[**[all]{lang="EN-US"}**]{#struct_0_x1358_x5075_x989948615}[：表示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x1358_x5075_x560422792}[：表示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x1358_x5075_471206530}[：表示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的事件调试信息开关。]{style="font-family:宋体"}

[**[reaction]{lang="EN-US"}**]{#struct_0_x1358_x5075_x1605087758}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的联动项调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_x406048871}

[**[debugging nqa]{lang="EN-US"}**]{#struct_0_x1358_x5075_x1192127149}[命令用来打开]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}**[undo debugging nqa ]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_x1358_x5075_154354344}[的调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging nqa error]{lang="EN-US"}]{#struct_0_x1358_x5075_1782697619}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x515239256}[[字段]{style="font-family:黑体"}]{#struct_0_x1358_x5075_863294721}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1358_x5075_1106891258}

[[Failed to allocate memory for creating NQA entry (*owner*-*tag*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x1158768768}

[[NQA]{lang="EN-US"}]{#struct_0_x1358_x5075_x848459928}[测试组调度分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for creating NQA template *name*.]{lang="EN-US"}]{#struct_0_x1358_x5075_x851825981}

[[NQA]{lang="EN-US"}]{#struct_0_x1358_x5075_154419880}[模板分配内存失败]{style="font-family:宋体"}

[[Failed to allocate memory for creating NQA entry (instance-*xxxxxxxxxxxxxxxx*?).]{lang="EN-US"}]{#struct_0_x1358_x5075_2029447310}

[[NQA]{lang="EN-US"}]{#struct_0_x1358_x5075_958772041}[实例分配内存失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to create start-time timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1957587657}

[[创建]{style="font-family:宋体"}[start-time]{lang="EN-US"}]{#struct_0_x1358_x5075_x83023235}[定时器失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to create life-time timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_x203240670}

[[创建]{style="font-family:宋体"}[life-time]{lang="EN-US"}]{#struct_0_x1358_x5075_737276089}[定时器失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to allocate memory for schedule.]{lang="EN-US"}]{#struct_0_x1358_x5075_154223272}

[[创建调度项分配内存失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x545039649}

[[NQA entry (*owner*-*tag*): Failed to receive packet (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x350213672}

[[表项接收报文失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x908880881}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to receive packet (error code: *error-code*)]{lang="EN-US"}]{#struct_0_x1358_x5075_x1606618642}

[[实例接收报文失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_154288808}

[[NQA entry (*owner*-*tag*): Failed to send packet (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x1001789523}

[[表项发送报文失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_2145014400}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to send packet (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x1567595287}

[[实例发送报文失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1065378408}

[[NQA entry (*owner*-*tag*): Probe timed out.]{lang="EN-US"}]{#struct_0_x1358_x5075_154616488}

[[表项探测超时]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x352161470}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Probe timed out.]{lang="EN-US"}]{#struct_0_x1358_x5075_914849126}

[[实例探测超时]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1889479277}

[[NQA entry (*owner*-*tag*): Failed to create statistics interval timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_1591061420}

[[创建统计间隔定时器失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_154682024}

[[NQA entry (*owner*-*tag*): Failed to create history keep-time timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_x418495791}

[[创建历史老化定时器失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1651429259}

[[NQA entry (*owner*-*tag*): Failed to create statistics hold-time timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_x244900220}

[[创建统计老化定时器失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720176144}

[[NQA entry (*owner*-*tag*): Failed to create socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x307410290}

[[表项创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_300675433}[失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_999878134}

[[实例创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_x47251011}[失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to set asynchronous socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_1720241680}

[[表项设置异步]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_107456692}[失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set asynchronous socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_433713156}

[[实例设置异步]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_164137754}[失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to set TTL option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_1720045072}

[[表项设置]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_x1358_x5075_x1071000043}[选项失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set TTL option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_462134800}

[[实例设置]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_x1358_x5075_1720110608}[选项失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to set ToS option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_1676358592}

[[表项设置]{style="font-family:宋体"}[ToS]{lang="EN-US"}]{#struct_0_x1358_x5075_x1254715320}[选项失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to set ToS option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_218386592}

[[实例设置]{style="font-family:宋体"}[ToS]{lang="EN-US"}]{#struct_0_x1358_x5075_1720438288}[选项失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to set bypass-route option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_x1502029765}

[[设置路由表旁路选项失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_225704706}

[[NQA entry (owner-tag): Failed to set socket sync pcb (error code: error-code).]{lang="EN-US"}]{#struct_0_x1358_x5075_x366614737}

[[设置同步]{style="font-family:宋体"}[pcb]{lang="EN-US"}]{#struct_0_x1358_x5075_567866351}[选项失败]{style="font-family:宋体"}

[[NQA entry (owner-tag): Failed to set socket out interface (error code: error-code).]{lang="EN-US"}]{#struct_0_x1358_x5075_902469988}

[[设置出接口失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x366811345}

[[NQA entry (owner-tag): Failed to set socket send buffer (error code: error-code).]{lang="EN-US"}]{#struct_0_x1358_x5075_206607967}

[[设置报文缓冲区长度失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1378347243}

[[NQA entry (*owner*-*tag*): Failed to find FIB entry according to next hop address.]{lang="EN-US"}]{#struct_0_x1358_x5075_x295638951}

[[根据下一跳地址查找]{style="font-family:宋体"}[FIB]{lang="EN-US"}]{#struct_0_x1358_x5075_1720503824}[表项失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to set next hop option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_896307471}

[[设置下一条选项失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_310984642}

[[NQA entry (*owner*-*tag*): Failed to bind socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_1720307216}

[[表项]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_x282149018}[绑定失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to bind socket (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_203363371}

[[实例]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_1720372752}[绑定失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to get interface index.]{lang="EN-US"}]{#struct_0_x1358_x5075_871570747}

[[获取接口索引失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_635540288}

[[NQA entry (*owner*-*tag*): Failed to get IP address from the source interface.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1534386726}

[[无法从源接口获取]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1358_x5075_1720700432}[地址]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to get VRF index.]{lang="EN-US"}]{#struct_0_x1358_x5075_2064659323}

[[表项获取]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x1358_x5075_x833349810}[索引失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to get VRF index.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720765968}

[[实例获取]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x1358_x5075_x272968281}[索引失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to allocate memory for sending packets.]{lang="EN-US"}]{#struct_0_x1358_x5075_58285588}

[[表项为发送报文分配内存失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720176145}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to allocate memory for sending packets.]{lang="EN-US"}]{#struct_0_x1358_x5075_x307475826}

[[实例为发送报文分配内存失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1318373269}

[[NQA entry (*owner*-*tag*): Failed to register socket to epoll.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720241681}

[[表项注册]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_107522228}[到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to register socket to epoll.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720045073}

[[实例注册]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_x1070934507}[到]{style="font-family:宋体"}[epoll]{lang="EN-US"}[失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to create probe timeout timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1492987079}

[[表项创建探测定时器失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720110609}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create probe timeout timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_1676293056}

[[实例创建探测定时器失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1297045016}

[[NQA entry (*owner*-*tag*): Failed to create frequency timer.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720438289}

[[表项创建]{style="font-family:宋体"}[frequency]{lang="EN-US"}]{#struct_0_x1358_x5075_x1502095301}[定时器失败]{style="font-family:宋体"}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to create frequency timer]{lang="EN-US"}]{#struct_0_x1358_x5075_1720503825}

[[实例创建]{style="font-family:宋体"}[frequency]{lang="EN-US"}]{#struct_0_x1358_x5075_896373007}[定时器失败]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Failed to initialize statistics resources.]{lang="EN-US"}]{#struct_0_x1358_x5075_x49648309}

[[初始化统计资源失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720307217}

[[NQA entry (*owner*-*tag*): Failed to allocate memory for creating test resources.]{lang="EN-US"}]{#struct_0_x1358_x5075_x282083482}

[[创建测试资源失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720372753}

[[NQA entry (*owner*-*tag*): Failed to set socket port reuse option (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_871505211}

[[设置]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1358_x5075_x2075314826}[端口重用选项失败]{style="font-family:宋体"}

[[NQA entry (%s-%s): Failed to connect to the server (error code: *error-code*).]{lang="EN-US"}]{#struct_0_x1358_x5075_1720700433}

[[表项发起连接失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_2064724859}

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?): Failed to connect to the server (error code: *error-code*)]{lang="EN-US"}]{#struct_0_x1358_x5075_1720765969}

[[实例发起连接失败]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x272902745}

[[NQA template *name* doesn\'t exist.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1139086314}

[[模板]{style="font-family:宋体"}[XXX]{lang="EN-US"}]{#struct_0_x1358_x5075_1720176142}[不存在]{style="font-family:宋体"}

[[Incomplete NQA operation parameters. Can\'t start NQA operation.]{lang="EN-US"}]{#struct_0_x1358_x5075_x307017074}

[[必配信息不全，无法启动测试]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1720241678}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging nqa event]{lang="EN-US"}]{#struct_0_x1358_x5075_107980991}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x491767864}[[字段]{style="font-family:黑体"}]{#struct_0_x1358_x5075_x1800594805}

[[描述]{style="font-family:黑体"}]{#struct_0_x1358_x5075_1345871841}

[[NQA entry (*owner*-*tag*): Create start-time timer successfully, interval is *number*s.]{lang="EN-US"}]{#struct_0_x1358_x5075_1054390125}

[[创建]{style="font-family:宋体"}[start-time]{lang="EN-US"}]{#struct_0_x1358_x5075_x1246419658}[定时器成功，定时器间隔时间为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[秒]{style="font-family:宋体"}[.]{lang="EN-US"}

[[NQA entry (*owner*-*tag*): Refresh start-time timer successfully, interval is *number*s.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1628293264}

[[刷新]{style="font-family:宋体"}[start-time]{lang="EN-US"}]{#struct_0_x1358_x5075_1720045070}[定时器成功，定时器间隔时间为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Create life-time timer successfully, interval is *number*s.]{lang="EN-US"}]{#struct_0_x1358_x5075_x1071131115}

[[创建]{style="font-family:宋体"}[life-time]{lang="EN-US"}]{#struct_0_x1358_x5075_1254746730}[定时器成功，定时器间隔时间为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Refresh start-time timer successfully, interval is *number*s.]{lang="EN-US"}]{#struct_0_x1358_x5075_x189372143}

[[刷新]{style="font-family:宋体"}[life-time]{lang="EN-US"}]{#struct_0_x1358_x5075_472079191}[定时器成功，定时器间隔时间为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*) schedule FSM: Create Schedule Event, status is *current-status*.]{lang="EN-US"}]{#struct_0_x1358_x5075_2084410333}

[[创建]{style="font-family:宋体"}[schedule]{lang="EN-US"}]{#struct_0_x1358_x5075_203844472}[事件，调度状态初始为]{style="font-family:宋体"}*[current-status]{lang="EN-US"}*

[[NQA entry (*owner*-*tag*) schedule FSM: Delete Schedule Event, status is *current-status*.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720110606}

[[表项删除]{style="font-family:宋体"}[schedule]{lang="EN-US"}]{#struct_0_x1358_x5075_1675965376}[事件，当前调度状态为]{style="font-family:宋体"}*[current-status]{lang="EN-US"}*

[[NQA entry (instance-*xxxxxxxxxxxxxxxx*?) schedule FSM: Delete Schedule Event, status is ]{lang="EN-US"}]{#struct_0_x1358_x5075_x1543597643}*[current-status]{lang="EN-US"}*[.]{lang="EN-US"}

[[实例删除]{style="font-family:宋体"}[schedule]{lang="EN-US"}]{#struct_0_x1358_x5075_1488847895}[事件，当前调度状态为]{style="font-family:宋体"}*[current-status]{lang="EN-US"}*

[[NQA entry (*owner*-*tag*) schedule FSM: *event*, status changed from *previous-status* to *current-status*.]{lang="EN-US"}]{#struct_0_x1358_x5075_x35335102}

[[状态机发生]{style="font-family:宋体"}*[event]{lang="EN-US"}*]{#struct_0_x1358_x5075_x1832419953}[事件，调度状态由]{style="font-family:宋体"}*[previous-status]{lang="EN-US"}*[变为]{style="font-family:宋体"}*[current-status]{lang="EN-US"}*

[[NQA entry (*owner-tag*): Failed to start the NQA operation because the operation configurations are incomplete.]{lang="EN-US"}]{#struct_0_x1358_x5075_x366418122}

[[测试组配置参数不完整，无法启动测试。]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1034321006}

[[NQA entry (*owner*-*tag*): Failed to start the UDP traceroute operation because the initial TTL is greater than the TTL.]{lang="EN-US"}]{#struct_0_x1358_x5075_x366352586}

[[初始化跳数大于最大跳数，无法启动]{style="font-family:宋体"}[UDP-tracert]{lang="EN-US"}]{#struct_0_x1358_x5075_x968029663}[测试。]{style="font-family:宋体"}

[[NQA reacts to system time changing.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720438286}

[[响应系统时间修改]{style="font-family:宋体"}]{#struct_0_x1358_x5075_x1502160837}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging nqa reaction]{lang="EN-US"}]{#struct_0_x1358_x5075_653270899}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x497676856}[[字段]{style="font-family:黑体"}]{#struct_0_x1358_x5075_1411095391}

[[描述]{style="font-family:黑体"}]{#struct_0_x1358_x5075_x1121819923}

[[NQA entry (*owner*-*tag*): Trigger-only reaction (*number*) is created.]{lang="EN-US"}]{#struct_0_x1358_x5075_x2003355132}

[[测试组（管理员名字为]{style="font-family:宋体"}*[owner]{lang="EN-US"}*]{#struct_0_x1358_x5075_1071448996}[，操作标签为]{style="font-family:宋体"}*[tag]{lang="EN-US"}*[）联动项（序号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[）创建]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*): Trigger-only reaction (*number*) is deleted.]{lang="EN-US"}]{#struct_0_x1358_x5075_1720503822}

[[测试组（管理员名字为]{style="font-family:宋体"}*[owner]{lang="EN-US"}*]{#struct_0_x1358_x5075_896700687}[，操作标签为]{style="font-family:宋体"}*[tag]{lang="EN-US"}*[）联动项（序号为]{style="font-family:宋体"}*[number]{lang="EN-US"}*[）删除]{style="font-family:宋体"}

[[NQA entry (*owner*-*tag*) reaction (*number*): Status changed from *previous-status* to *current-status*.]{lang="EN-US"}]{#struct_0_x1358_x5075_1206528250}

[[联动项状态发生改变]{style="font-family:宋体"}]{#struct_0_x1358_x5075_858048540}

[[NQA entry (*owner*-*tag*) reaction (*number*): Trigger notified.]{lang="EN-US"}]{#struct_0_x1358_x5075_1487919005}

[[触发联动通知]{style="font-family:宋体"}]{#struct_0_x1358_x5075_1386628622}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1358_x5075_1720307214}

[[\# ]{lang="EN-US"}]{#struct_0_x1358_x5075_x282280090}[利用]{style="font-family:宋体"}[NQA]{lang="EN-US"}[进行]{style="font-family:宋体"}[ICMP-echo]{lang="EN-US"}[测试，打开所有]{style="font-family:宋体"}[NQA]{lang="EN-US"}[的调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> terminal monitor]{lang="PT-BR"}]{#struct_0_x1358_x5075_2116502591}

[\<Sysname\> debugging nqa all]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x1358_x5075_x1002303608}[创建]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，]{style="font-family:宋体"}[NQA]{lang="PT-BR"}[测试组]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并配置测试类型、创建联动项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1358_x5075_107102915}

[\[Sysname\] track 1 nqa entry admin test reaction 1.]{lang="PT-BR"}

[\[Sysname\] nqa entry admin test]{lang="PT-BR"}

[\[Sysname-nqa-admin-test\] type icmp-echo]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] destination ip 10.2.2.1]{lang="EN-US"}

[\[Sysname-nqa-admin-test-icmp-echo\] reaction 1 checked-element probe-fail threshold-type consecutive 3 action-type trigger-only]{lang="EN-US"}

[\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test): Trigger-only reaction (1) is created.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1358_x5075_x440722537}*[创建联动项。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x1358_x5075_x988927938}[删除联动项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-nqa-admin-test-icmp-echo\] undo reaction 1]{lang="EN-US"}]{#struct_0_x1358_x5075_1720372750}

[\[Sysname-nqa-admin-test-icmp-echo\] quit]{lang="EN-US"}

[\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test): Trigger-only reaction (1) is deleted.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1358_x5075_871439675}*[联动项被删除。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x1358_x5075_256903241}[调度]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试组，测试开始时间为]{style="font-family:宋体"}[21:48:25]{lang="EN-US"}[，当前系统时间为]{style="font-family:宋体"}[21:47:25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] nqa schedule admin test start-time ]{lang="PT-BR"}[21:48:25]{lang="EN-US"}]{#struct_0_x1358_x5075_694890623}[ ]{lang="EN-US"}[lifetime 180]{lang="PT-BR"}

[\[Sysname\] quit]{lang="PT-BR"}

[\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test): ]{lang="EN-US"}[Create start-time timer successfully, interval is 60s.]{lang="EN-US"}

[\*Apr 29 21:47:25:630 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test) ]{lang="EN-US"}[schedule FSM: Create Schedule Event, status is Waiting.]{lang="EN-US"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x1358_x5075_1004366675}*[已成功调度]{style="font-family:宋体"}[NQA]{lang="PT-BR"}[测试组，等待启动测试。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x1358_x5075_1521945922}[将]{style="font-family:宋体"}[当前系统时间修改为]{style="font-family:宋体"}[21:49:00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>]{lang="PT-BR"}[ ]{lang="PT-BR"}[clock datetime 21:49:00 2011/04/29]{lang="EN-US"}]{#struct_0_x1358_x5075_1720700430}

[\*Apr 29 21:49:00:206 2011 Sysname NQA/7/ Event: -VD=1; ]{lang="EN-US"}[NQA reacts to system time changing.]{lang="EN-US"}

[*[// NQA]{lang="EN-US"}*]{#struct_0_x1358_x5075_2064528251}*[响应系统时间修改。]{style="font-family:宋体"}*

[[\*Apr 29 21:49:01:206 2011 Sysname NQA/7/ Event: -VD=1; ]{lang="EN-US"}]{#struct_0_x1358_x5075_x1599823207}[NQA entry (admin-test): Create life-time timer successfully, interval is 76s.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1358_x5075_x595335868}*[创建]{style="font-family:宋体"}[life-time]{lang="EN-US"}[定时器。]{style="font-family:宋体"}*

[[\*Apr 29 21:49:02:206 2011 Sysname NQA/7/ Event: -VD=1; NQA entry (admin-test)]{lang="EN-US"}]{#struct_0_x1358_x5075_x2092072018}[ schedule FSM: System Time Change Event, status changed from Waiting to Running.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1358_x5075_593049546}*[启动]{style="font-family:宋体"}[NQA]{lang="EN-US"}[测试。]{style="font-family:宋体"}*

[[\*Apr 29 21:49:25:630 2011 Sysname NQA/7/ Reaction: -VD=1; NQA entry (admin-test)  reaction (1): ]{lang="EN-US"}]{#struct_0_x1358_x5075_x744047206}[Status changed from invalid to over-threshold.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x1358_x5075_1932314978}*[联动项的状态改变，由]{style="font-family:宋体"}[invalid]{lang="EN-US"}[变为]{style="font-family:宋体"}[over-threshold]{lang="EN-US"}[。]{style="font-family:宋体"}*
