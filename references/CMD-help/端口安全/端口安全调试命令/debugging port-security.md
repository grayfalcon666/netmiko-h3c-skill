::: {#1005327470 .myid}
[]{#_Toc404792788}[]{#struct_0_95801_42839_2037466074}[]{#_Toc233198545}

**端口安全 \-- 端口安全调试命令 \-- debugging port-security**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_95801_42839_887496679}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_95801_42839_x1447818416}

[**[debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_95801_42839_x710552561}

[**[undo debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_95801_42839_518711629}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_95801_42839_x133476466}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_95801_42839_908982627}

[**[undo debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** } \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_95801_42839_1436909373}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_95801_42839_x843657716}[模式：]{style="font-family:宋体"}

[**[debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** } ]{lang="EN-US"}]{#struct_0_95801_42839_2014366344}[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="SV"}

[**[undo debugging port-security]{lang="EN-US"}**[ { **all** \| **error** \| **event** } ]{lang="EN-US"}]{#struct_0_95801_42839_104980787}[\[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_95801_42839_1842019276}

[[用户视图]{style="font-family:宋体"}]{#struct_0_95801_42839_x1168155314}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_95801_42839_x1344459413}

[[network-admin]{lang="EN-US"}]{#struct_0_95801_42839_59528944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_95801_42839_1273184860}

[[【参数】]{style="font-family:黑体"}]{#struct_0_95801_42839_1599539030}

[**[all]{lang="EN-US"}**]{#struct_0_95801_42839_1915764375}[：表示端口安全的所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_95801_42839_x843723252}[：表示端口安全的错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_95801_42839_1616682195}[：表示端口安全的事件调试信息开关。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95801_42839_x2009392203}[：表示指定单板的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95801_42839_x1193371410}[：表示指定成员设备的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_95801_42839_x1152155503}[：表示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的调试信息开关，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_95801_42839_1645270412}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示成员设备上指定单板的调试信息开关，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="SV"}**]{#struct_0_95801_42839_x1980504776}[ *chassis-number* **slot** *slot-number*]{lang="SV"}[：]{style="font-family:宋体"}[表示指定单板的调试信息开关，]{style="font-family:宋体"}*[chassis-number]{lang="SV"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_95801_42839_557007896}

[]{#OLE_LINK1}[**[debugging port-security]{lang="EN-US"}**]{#struct_0_95801_42839_x122978520}[命令用来打开端口安全调试信息开关。]{style="font-family:宋体"}**[undo debugging port-security]{lang="EN-US"}**[命令用来关闭端口安全调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，端口安全调试信息开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_95801_42839_1149740691}

[]{#struct_0_95801_42839_474628974}[[表1-1 ]{lang="EN-US"}[debug port-security error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_424755292}[[字段]{style="font-family:黑体"}]{#struct_0_95801_42839_x843788788}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_95801_42839_x1146177967}

[[Failed to initialize the socket.]{lang="EN-US"}]{#struct_0_95801_42839_572433909}

[[初始化]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_95801_42839_2145270904}[失败]{style="font-family:宋体"}

[[Failed to get socketFd by slot: *slot.*]{lang="EN-US"}]{#struct_0_95801_42839_415708947}

[[通过板号获取]{style="font-family:宋体"}[socketFd]{lang="EN-US"}]{#struct_0_95801_42839_x1586347962}[失败]{style="font-family:宋体"}

[[Failed to sync information.]{lang="EN-US"}]{#struct_0_95801_42839_1613151169}

[[同步信息失败]{style="font-family:宋体"}]{#struct_0_95801_42839_x843854324}

[[Failed to recover authentication session]{lang="EN-US"}]{#struct_0_95801_42839_x316522648}

[[恢复认证会话失败]{style="font-family:宋体"}]{#struct_0_95801_42839_1189734732}

[[User authorization failed]{lang="EN-US"}]{#struct_0_95801_42839_x708097664}

[[用户认证失败]{style="font-family:宋体"}]{#struct_0_95801_42839_x1321120180}

[ ]{lang="EN-US"}

[]{#struct_0_95801_42839_x709774557}[[表1-2 ]{lang="EN-US"}[debug port-security event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_426962716}[[字段]{style="font-family:黑体"}]{#struct_0_95801_42839_206816243}

[[描述]{style="font-family:黑体"}]{#struct_0_95801_42839_391000093}

[*[app]{lang="EN-US"}*[ is being started.]{lang="EN-US"}]{#struct_0_95801_42839_1856634016}

[[端口安全启动]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x830778782}[模块]{style="font-family:宋体"}

[[Notify *app* of portsec_enable event.]{lang="EN-US"}]{#struct_0_95801_42839_x1780119658}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x2054402985}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知端口安全使能事件]{style="font-family:宋体"}

[[Notify *app* of portsec_portmode event*.*]{lang="EN-US"}]{#struct_0_95801_42839_x843461108}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_815957481}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知端口模式设置事件]{style="font-family:宋体"}

[[Notify *app* of authorization_info_deleted event.]{lang="EN-US"}]{#struct_0_95801_42839_1363635176}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_2011863690}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知授权信息删除事件]{style="font-family:宋体"}

[[Notify *app* of auth_fail_policy_proc event.]{lang="EN-US"}]{#struct_0_95801_42839_1550490068}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x323476342}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知认证失败处理事件]{style="font-family:宋体"}

[[Notify *app* of if_vlan event*.*]{lang="EN-US"}]{#struct_0_95801_42839_x843526644}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_1621972369}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知接口]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Notify *app* of HA event*.*]{lang="EN-US"}]{#struct_0_95801_42839_x1255007244}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x421399505}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知]{style="font-family:宋体"}[HA]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Notify *app* of if_event*.*]{lang="EN-US"}]{#struct_0_95801_42839_x366470550}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x2135285433}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知接口事件]{style="font-family:宋体"}

[[Notify *app* of authorization_success event.]{lang="EN-US"}]{#struct_0_95801_42839_x1085898243}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x1086356995}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知授权成功事件]{style="font-family:宋体"}

[[Notify *app* of vctrl_success_rsp event.]{lang="EN-US"}]{#struct_0_95801_42839_x1969408886}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x886251716}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知]{style="font-family:宋体"}[vctrl]{lang="EN-US"}[设置成功回应事件]{style="font-family:宋体"}

[[Notify *app* of vctrl_fail_rsp event.]{lang="EN-US"}]{#struct_0_95801_42839_x1086291459}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x1851400913}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知]{style="font-family:宋体"}[vctrl]{lang="EN-US"}[设置失败回应事件]{style="font-family:宋体"}

[[Notify *app* of vctrl_del_notify event.]{lang="EN-US"}]{#struct_0_95801_42839_x1423762255}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x1086225923}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知]{style="font-family:宋体"}[vctrl]{lang="EN-US"}[删除事件]{style="font-family:宋体"}

[[Notify *app* of mac_vlan event.]{lang="EN-US"}]{#struct_0_95801_42839_x286969579}

[[端口安全向]{style="font-family:宋体"}[app]{lang="EN-US"}]{#struct_0_95801_42839_x448457459}[模块]{style="font-family:宋体"}[/]{lang="EN-US"}[线程通知]{style="font-family:宋体"}[mac-vlan]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[Creating block-mac-aging timer, period is 3 minutes.]{lang="EN-US"}]{#struct_0_95801_42839_x843592180}

[[创建阻塞]{style="font-family:宋体"}[mac]{lang="EN-US"}]{#struct_0_95801_42839_1254303745}[老化定时器，老化时间是]{style="font-family:宋体"}[3]{lang="EN-US"}[分钟]{style="font-family:宋体"}

[[All authentication sessions on interface *interface-name* have been deleted.]{lang="EN-US"}]{#struct_0_95801_42839_x583809185}

[[接口上所有认证会话已经被删除]{style="font-family:宋体"}]{#struct_0_95801_42839_x1695869640}

[[After the node is removed from the hash table, delete the corresponding timer.]{lang="EN-US"}]{#struct_0_95801_42839_x983124838}

[[节点从]{style="font-family:宋体"}[hash]{lang="EN-US"}]{#struct_0_95801_42839_x843133428}[表中删除后，删除与其相关的定时器]{style="font-family:宋体"}

[[Dealing with cfg queue message recevied from other threads.]{lang="EN-US"}]{#struct_0_95801_42839_x1524523986}

[[端口安全主进程开始处理从其它线程接收的配置队列消息]{style="font-family:宋体"}]{#struct_0_95801_42839_1847881805}

[[IO board received and processed the message.]{lang="EN-US"}]{#struct_0_95801_42839_953464681}

[[IO]{lang="EN-US"}]{#struct_0_95801_42839_2124826955}[板接收和处理主控板发来的消息]{style="font-family:宋体"}

[[Creating a timer which period is 1 second.]{lang="EN-US"}]{#struct_0_95801_42839_x843198964}

[[创建一个周期为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_95801_42839_1243723165}[秒的定时器]{style="font-family:宋体"}

[[Reconnection from IO board to master timed out.]{lang="EN-US"}]{#struct_0_95801_42839_x969093408}

[[IO]{lang="EN-US"}]{#struct_0_95801_42839_x70484431}[板重连接主控板超时]{style="font-family:宋体"}

[[IO board connected to master successfully. Close reconnection timer.]{lang="EN-US"}]{#struct_0_95801_42839_x672742318}

[[IO]{lang="EN-US"}]{#struct_0_95801_42839_x843657715}[板连接主控板成功，关闭重连接定时器]{style="font-family:宋体"}

[[IO board failed to connect to master.]{lang="EN-US"}]{#struct_0_95801_42839_2014300808}

[[IO]{lang="EN-US"}]{#struct_0_95801_42839_x235800575}[板连接主控板失败]{style="font-family:宋体"}

[[A MAC *mac-add* triggered intrusion protection.]{lang="EN-US"}]{#struct_0_95801_42839_79225620}

[[一个源地址为]{style="font-family:宋体"}*[mac-add]{lang="EN-US"}*]{#struct_0_95801_42839_x843723251}[的数据帧触发了入侵保护]{style="font-family:宋体"}

[[Session created]{lang="EN-US"}]{#struct_0_95801_42839_1616485587}

[[创建会话]{style="font-family:宋体"}]{#struct_0_95801_42839_x485072263}

[[Session deleted]{lang="EN-US"}]{#struct_0_95801_42839_x2030347570}

[[删除会话]{style="font-family:宋体"}]{#struct_0_95801_42839_x843788787}

[[Processing session-end msg, and attempt to free the session]{lang="EN-US"}]{#struct_0_95801_42839_x1145588143}

[[处理会话结束信息并试图释放会话]{style="font-family:宋体"}]{#struct_0_95801_42839_1686336077}

[[Processing session-end msg, trigger intruction and free the session]{lang="EN-US"}]{#struct_0_95801_42839_x745512757}

[[处理会话结束信息，触发入侵检测并释放会话]{style="font-family:宋体"}]{#struct_0_95801_42839_x843854323}

[[New_mac processing finished]{lang="EN-US"}]{#struct_0_95801_42839_x1282077961}

[[New-mac]{lang="EN-US"}]{#struct_0_95801_42839_x843395571}[处理结束]{style="font-family:宋体"}

[[Received new_mac notification result is *result*, flag is *flag*]{lang="EN-US"}]{#struct_0_95801_42839_x709840093}

[[收到]{style="font-family:宋体"}[new-mac]{lang="EN-US"}]{#struct_0_95801_42839_993522158}[处理的通知结果是]{style="font-family:宋体"}*[result]{lang="EN-US"}*[，标志是]{style="font-family:宋体"}*[flag]{lang="EN-US"}*[。其中，]{style="font-family:宋体"}*[result]{lang="EN-US"}*[的取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PORTSEC_MAC_PROCESSING]{lang="EN-US"}]{#struct_0_95801_42839_x843461107}[（正在处理）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PORTSEC_MAC_HANDLED]{lang="EN-US"}]{#struct_0_95801_42839_816285161}[（已经处理）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PORTSEC_MAC_NOTCONCERN]{lang="EN-US"}]{#struct_0_95801_42839_998171385}[（不关心）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PORTSEC_MAC_DROP]{lang="EN-US"}]{#struct_0_95801_42839_x1178787709}[（丢弃）]{style="font-family:宋体"}

[[Successfully recovered authentication session]{lang="EN-US"}]{#struct_0_95801_42839_1516295591}

[[成功恢复认证会话]{style="font-family:宋体"}]{#struct_0_95801_42839_x843592179}

[[New_mac finished, try auth-fail processing]{lang="EN-US"}]{#struct_0_95801_42839_1253844988}

[[New-mac]{lang="EN-US"}]{#struct_0_95801_42839_x803843675}[处理结束，尝试认证失败处理]{style="font-family:宋体"}

[[Received *msg* msg from user]{lang="EN-US"}]{#struct_0_95801_42839_x843133427}

[[收到用户消息]{style="font-family:宋体"}*[msg]{lang="EN-US"}*]{#struct_0_95801_42839_x1524851666}

[[Notify new_mac event when user passed MAC authenticaiton]{lang="EN-US"}]{#struct_0_95801_42839_735107651}

[[当用户通过]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_95801_42839_x1672392728}[地址认证时，通知]{style="font-family:宋体"}[new-mac]{lang="EN-US"}[事件]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_95801_42839_x843198963}

[[\# ]{lang="EN-US"}]{#struct_0_95801_42839_1244181917}[在一台未启动端口安全功能的设备上，打开端口安全所有调试功能，输出以下调试信息。]{style="font-family:宋体"}

[[\<Sysname\>debugging port-security all]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x1491027885}

[[\# ]{lang="EN-US"}]{#struct_0_95801_42839_1489069175}[使能端口安全。]{style="font-family:宋体"}

[[\<Sysname\> port-security enable]{lang="EN-US"}]{#struct_0_95801_42839_x347715782}

[[\*Jan  1 00:03:32:450 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1330820008}

[[Notify 802.1X of portsec_enable event.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_119870483}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x233755973}*[端口安全向]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块通知端口安全使能事件]{style="font-family:宋体"}*

[[\*Jan  1 00:03:32:452 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1041931182}

[[Notify 802.1X of portsec_enable event.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_722426229}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_338035541}*[端口安全向]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证模块通知端口安全使能事件]{style="font-family:宋体"}*

[[\*Jan  1 00:03:32:456 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1654437271}

[[Notify AutoLearn of portsec_enable event.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x2001079218}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x1601619993}*[端口安全向]{style="font-family:宋体"}[autolearn]{lang="EN-US"}[线程通知端口安全使能事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_95801_42839_676484791}[配置端口安全模式为]{style="font-family:宋体"}[mac-else-userlogin-secure-ext]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-GigabitEthernet1/0\] port-security port-mode mac-else-userlogin-secure-ext]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1224959882}

[[\*Jan  1 01:33:45:369 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1110002740}

[[Notify 802.1X of portsec_portmode event.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_577575923}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x2123625677}*[端口安全向]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[线程通知端口模式配置事件]{style="font-family:宋体"}*

[[\*Jan  1 01:33:45:371 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_722360693}

[[Notify MAC-Auth of portsec_portmode event.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x657707009}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x568868242}*[端口安全向]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[认证模块通知端口模式配置事件]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_95801_42839_x1211728661}[当有]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户上线时，输出以下调试信息。]{style="font-family:宋体"}

[[\*Jan  1 02:30:05:947 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1338460187}

[[MAC-Auth \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received new_mac notification result is PORTSEC_MAC_PROCESSING, flag is 0x80000000.]{lang="EN-US"}]{#struct_0_95801_42839_x426699617}

[*[//]{lang="EN-US"}*]{#struct_0_95801_42839_x391636212}*[端口安全收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证模块对用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[的]{style="font-family:宋体"}[new_mac]{lang="EN-US"}[事件处理结果为]{style="font-family:宋体"}[PORTSEC_MAC_PROCESSING]{lang="EN-US"}*

[[\*Jan  1 02:30:05:948 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_983830428}

[[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Session created.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x331718430}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_492865425}*[端口安全创建了用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[的认证会话]{style="font-family:宋体"}*

[[\*Jan  1 02:30:05:955 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_722295157}

[[MAC-Auth \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received PS_QUEMSG_SESS_MSG_FAIL msg from user.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x704475171}

[*[//]{lang="EN-US"}*]{#struct_0_95801_42839_x1861994385}*[端口安全接收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[认证线程发出的对用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[认证失败的队列消息]{style="font-family:宋体"}*

[[\*Jan  1 02:30:05:956 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x1721832530}

[[MAC-Auth \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received PS_QUEMSG_SESS_MSG_END msg from user.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_190054789}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_2097053985}*[端口安全接收到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[认证线程发出的对用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[结束认证的队列消息]{style="font-family:宋体"}*

[[\*Jan  1 02:30:05:958 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_188739155}

[[802.1X \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received new_mac notification result is PORTSEC_MAC_PROCESSING, flag is 0x80000000.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x555226067}

[*[//]{lang="EN-US"}*]{#struct_0_95801_42839_1829516862}*[端口安全收到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块对用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[的]{style="font-family:宋体"}[new_mac]{lang="EN-US"}[事件处理结果为]{style="font-family:宋体"}[PORTSEC_MAC_PROCESSING]{lang="EN-US"}*

[[\*Jan  1 02:30:05:987 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_722229621}

[[802.1X \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received PS_QUEMSG_SESS_MSG_SUCC msg from user.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x1501482783}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x1077261969}*[端口安全收到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块发出的对]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[认证成功的队列消息]{style="font-family:宋体"}*

[[\*Jan  1 02:30:05:997 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1124201235}

[[802.1X \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received PS_QUEMSG_SESS_MSG_AUTZ msg from user.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_1844881594}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_1475721072}*[端口安全收到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块发出的对]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[授权成功的队列消息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_95801_42839_x1787445230}[该]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户下线时，输出以下调试信息。]{style="font-family:宋体"}

[[\*Jan  1 02:30:14:658 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_625061249}

[[802.1X \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Received PS_QUEMSG_SESS_MSG_END msg from user.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x1877336791}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_1218637474}*[端口安全接收到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[模块发出的对用户]{style="font-family:宋体"}[1cbd-b9e3-b0ed]{lang="EN-US"}[结束认证的队列消息]{style="font-family:宋体"}*

[[\*Jan  1 02:30:14:659 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_722688373}

[[802.1X \[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Processing session-end msg, and attempt to free the session.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x1400211152}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x418447201}*[端口安全处理认证结束消息，尝试释放认证会话]{style="font-family:宋体"}*

[[\*Jan  1 02:30:14:663 2011 Sysname PORTSEC/7/EVENT:]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_x65386696}

[[\[1cbd-b9e3-b0ed:VLAN1:GE1/0/1\] Session deleted.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_95801_42839_2060793704}

[*[// ]{lang="EN-US"}*]{#struct_0_95801_42839_x623663875}*[端口安全删除了认证会话]{style="font-family:宋体"}*

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}
