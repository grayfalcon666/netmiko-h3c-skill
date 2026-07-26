::: {#-2080607475 .myid}
[]{#_Toc404794062}[]{#struct_0_x2450_x2859_410996836}[]{#_Toc363638091}[]{#_Toc233198545}

**MACsec \-- MACsec调试命令 \-- debugging macsec**

------------------------------------------------------------------------

[**[debugging macsec]{lang="EN-US"}**]{#struct_0_x2450_x2859_x177360268}[命令用来打开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[debugging macsec]{lang="EN-US"}**]{#struct_0_x2450_x2859_901906980}[命令用来关闭]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_2084524778}

[**[debugging macsec ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x2450_x2859_x1003864703}

[**[undo debugging macsec ]{lang="EN-US"}**[{ **all** \| **error** \| **event** }]{lang="EN-US"}]{#struct_0_x2450_x2859_258232414}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x2143208267}

[[MACsec]{lang="EN-US"}]{#struct_0_x2450_x2859_576806856}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_572628461}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2450_x2859_x1826860878}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_1874888867}

[[network-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_x925659347}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_706829831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_1590793515}

[**[all]{lang="EN-US"}**]{#struct_0_x2450_x2859_477887097}[：表示所有的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[调试信息开关，包括错误调试信息开关、事件调试信息开关和]{style="font-family:宋体"}[MKA]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x2450_x2859_229711512}[：表示]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_x2450_x2859_2014423450}[：表示]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1837261996}

[]{#struct_0_x2450_x2859_x999984709}[[表1-1 ]{lang="EN-US"}[debugging macsec error]{lang="EN-US"}]{#_Toc130718927}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x296525408}[[字段]{style="font-family:黑体"}]{#struct_0_x2450_x2859_1110309110}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2450_x2859_514733446}

[[Received an invalid packet (type: *invalid type*) on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1471176847}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1923354482}[接收了错误的报文，]{style="font-family:宋体"}*[invalid type]{lang="EN-US"}*[表示错误类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}[ destination ]{lang="EN-US"}]{#struct_0_x2450_x2859_x390828928}[MAC]{lang="EN-US"}[ address]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[非法的]{style="font-family:宋体"}[目的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}]{#struct_0_x2450_x2859_x885489197}[ packet]{lang="EN-US"}[ length]{lang="EN-US"}[：表示无效的报文长度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incompatible]{lang="EN-US"}[ MKA ]{lang="EN-US"}]{#struct_0_x2450_x2859_706895367}[v]{lang="EN-US"}[ersion]{lang="EN-US"}[ ID]{lang="EN-US"}[：表示不兼容的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[版本]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[incompatible]{lang="EN-US"}[ ]{lang="EN-US"}]{#struct_0_x2450_x2859_x1550935809}[EAPOL]{lang="EN-US"}[ ]{lang="EN-US"}[v]{lang="EN-US"}[ersion]{lang="EN-US"}[ ID]{lang="EN-US"}[：表示不兼容的]{style="font-family:宋体"}[EAPOL]{lang="EN-US"}[版本]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[length error in ]{lang="EN-US"}[basic ]{lang="EN-US"}]{#struct_0_x2450_x2859_x1797843237}[parameter ]{lang="EN-US"}[set]{lang="EN-US"}[：表示基本参数集长度错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown algorithm agility]{lang="EN-US"}]{#struct_0_x2450_x2859_2105597374}[：表示不可识别的算法灵活度]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unknown CKN]{lang="EN-US"}]{#struct_0_x2450_x2859_x1818659490}[：表示不可识别的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[mismatched]{lang="EN-US"}[ ICV]{lang="EN-US"}]{#struct_0_x2450_x2859_x1394177150}[：表示错误的]{lang="EN-US" style="font-family:宋体"}[ICV]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SCI conflict]{lang="EN-US"}]{#struct_0_x2450_x2859_1746846898}[：表示收到的报文]{style="font-family:宋体"}[SCI]{lang="EN-US"}[和本端]{style="font-family:宋体"}[SCI]{lang="EN-US"}[相同]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid message number]{lang="EN-US"}]{#struct_0_x2450_x2859_x1675655372}[：表示非法的消息编号]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}[ SCI]{lang="EN-US"}]{#struct_0_x2450_x2859_x737090643}[：表示非法的]{style="font-family:宋体"}[SCI]{lang="EN-US"}

[[Failed to send packets on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_706960903}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1132459804}[发送报文失败]{style="font-family:宋体"}

[[Failed to get the RxSC PN on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1702672289}

[[获取接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1713948039}[的接收通道]{style="font-family:宋体"}[PN]{lang="EN-US"}[（]{style="font-family:宋体"}[Packet Number]{lang="EN-US"}[）值失败]{style="font-family:宋体"}

[[Failed to get the next TxSC PN on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1169933934}

[[获取接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x631132043}[的发送通道的下一个]{style="font-family:宋体"}[PN]{lang="EN-US"}[值失败]{style="font-family:宋体"}

[[Failed to set the link status on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1997261633}

[[设置接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_1305732177}[的链路状态失败]{style="font-family:宋体"}

[[Failed to *operate* *object* on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1204238938}

[[操作接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_707026439}[失败]{style="font-family:宋体"}

[*[operate]{lang="EN-US"}*]{#struct_0_x2450_x2859_x117641806}[表示操作类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[create]{lang="EN-US"}]{#struct_0_x2450_x2859_927489604}[：表示创建]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[modify]{lang="EN-US"}]{#struct_0_x2450_x2859_x520483011}[：表示修改]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[delete]{lang="EN-US"}]{#struct_0_x2450_x2859_x1749852375}[：表示删除]{lang="EN-US" style="font-family:宋体"}

[*[object]{lang="EN-US"}*]{#struct_0_x2450_x2859_x69153954}[表示操作对象，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TxS]{lang="EN-US"}]{#struct_0_x2450_x2859_1778388118}[C]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[发送]{lang="EN-US" style="font-family:宋体"}[SC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RxS]{lang="EN-US"}]{#struct_0_x2450_x2859_x1620799408}[C]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[接收]{lang="EN-US" style="font-family:宋体"}[SC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TxS]{lang="EN-US"}]{#struct_0_x2450_x2859_706567687}[A]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[发送]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RxS]{lang="EN-US"}]{#struct_0_x2450_x2859_1872229567}[A]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[接收]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#struct_0_x2450_x2859_x840361000}[[表1-2 ]{lang="EN-US"}[debugging macsec event]{lang="EN-US"}]{#_Toc130718928}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x295333874}[[字段]{style="font-family:黑体"}]{#struct_0_x2450_x2859_2103346568}

[[描述]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x122748934}

[[Received *event* event on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_386836054}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_2068597477}[收到了事件]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_x2450_x2859_1147238316}[表示接口事件类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACTIVE]{lang="EN-US"}]{#struct_0_x2450_x2859_x2099189521}[：表示接口激活事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DEACTIVE]{lang="EN-US"}]{#struct_0_x2450_x2859_x1711838670}[：表示接口去激活事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DELETE]{lang="EN-US"}]{#struct_0_x2450_x2859_706633223}[：表示接口删除事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2450_x2859_950739738}[：表示接口]{style="font-family:宋体"}[UP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2450_x2859_1694736365}[：表示接口]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACCHANGE]{lang="EN-US"}]{#struct_0_x2450_x2859_x2048114309}[：表示接口]{style="font-family:宋体"}[MAC]{lang="EN-US"}[变化事件]{style="font-family:宋体"}

[[Received *event* event of slot *slot-id*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1140909894}

[[收到板事件，]{style="font-family:宋体"}*[slot-id]{lang="EN-US"}*]{#struct_0_x2450_x2859_236149803}[表示槽位号或成员编号]{style="font-family:宋体"}

[*[event]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1339776262}[表示事件类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[INSERT]{lang="EN-US"}]{#struct_0_x2450_x2859_x815157684}[：表示插入事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[REMOVE]{lang="EN-US"}]{#struct_0_x2450_x2859_x2142550355}[：表示拔出事件]{lang="EN-US" style="font-family:宋体"}

[[Received dot1x *event* event on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_x2022030581}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_706698759}[收到了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的事件。]{style="font-family:宋体"}*[event]{lang="EN-US"}*[表示事件类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[USER_ONLINE]{lang="EN-US"}]{#struct_0_x2450_x2859_121138021}[：表示用户上线事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[USER_OFFLINE]{lang="EN-US"}]{#struct_0_x2450_x2859_1761674569}[：表示用户下线事件]{style="font-family:宋体"}

[[The agent slot received a packet for a slot that was in the ISSU process.]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x2450_x2859_x2041960977}

[[代理板收到了]{style="font-family:宋体"}[ISSU]{lang="EN-US"}]{#struct_0_x2450_x2859_x2044101182}[重定向过来的报文]{style="font-family:宋体"}

[[Connection status changed to *state* because of *reason* on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_1206028232}

[[由于]{style="font-family:宋体"}*[reason]{lang="EN-US"}*]{#struct_0_x2450_x2859_857917635}[，导致接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[连接状态变化。]{style="font-family:宋体"}*[state]{lang="EN-US"}*[表示连接状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x2450_x2859_x1153496491}[：表示未知状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Pending]{lang="EN-US"}]{#struct_0_x2450_x2859_706764295}[：表示挂起状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unauthenticated]{lang="EN-US"}]{#struct_0_x2450_x2859_536617553}[：表示未认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Authenticated]{lang="EN-US"}]{#struct_0_x2450_x2859_x1374713425}[：表示认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secured]{lang="EN-US"}]{#struct_0_x2450_x2859_x1903521713}[：表示安全状态]{style="font-family:宋体"}

[*[reason]{lang="EN-US"}*]{#struct_0_x2450_x2859_2094887767}[表示原因，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP initialization]{lang="EN-US"}]{#struct_0_x2450_x2859_690995141}[：表示受控端口初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[no active instance]{lang="EN-US"}]{#struct_0_x2450_x2859_707354119}[：表示没有激活的实例]{style="font-family:宋体"}

[[The MKA participant with CKN *ckn* aged out on interface *interface-type interface-number.*]{lang="EN-US"}]{#struct_0_x2450_x2859_178955852}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_82694648}[上]{style="font-family:宋体"}[CKN]{lang="EN-US"}[为]{style="font-family:宋体"}*[ckn]{lang="EN-US"}*[的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[参与者老化]{style="font-family:宋体"}

[[The *type* peer with SCI *sci*, CKN *ckn*, and MI *mi* aged out on interface *interface-type interface-number.*]{lang="EN-US"}]{#struct_0_x2450_x2859_x53930176}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_1008299440}[上]{style="font-family:宋体"}[SCI]{lang="EN-US"}[为]{style="font-family:宋体"}*[sci]{lang="EN-US"}*[、]{style="font-family:宋体"}[CKN]{lang="EN-US"}[为]{style="font-family:宋体"}*[ckn]{lang="EN-US"}*[和]{style="font-family:宋体"}[MI]{lang="EN-US"}[为]{style="font-family:宋体"}*[mi]{lang="EN-US"}*[的]{style="font-family:宋体"}[peer]{lang="EN-US"}[老化。]{style="font-family:宋体"}*[type]{lang="EN-US"}*[表示]{style="font-family:宋体"}[peer]{lang="EN-US"}[的类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[live]{lang="EN-US"}]{#struct_0_x2450_x2859_x1137885789}[：表示已经学习到的]{style="font-family:宋体"}[peer]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[potential]{lang="EN-US"}]{#struct_0_x2450_x2859_707419655}[：表示正在协商中的]{style="font-family:宋体"}[peer]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1569401087}

[[\# ]{lang="EN-US"}]{#struct_0_x2450_x2859_7712309}[在设备上打开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[错误调试信息开关。使能]{style="font-family:宋体"}[MKA]{lang="EN-US"}[功能且配置了]{style="font-family:宋体"}[PSK]{lang="EN-US"}[的接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到非法的加密报文]{style="font-family:宋体"}[时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging macsec error]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2450_x2859_1940661470}

[[\*Aug  6 19:02:52:755 2013 Sysname MACSEC/7/ERROR: -MDC=1; Received an invalid packet (type: mismatched ICV) on interface GigabitEthernet1/0/1.]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2450_x2859_1135458344}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_x29378197}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到非法的]{style="font-family:宋体"}[PDU]{lang="EN-US"}[报文，原因是错误的]{style="font-family:宋体"}[ICV ]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_x2450_x2859_1899409836}[在设备上打开]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[事件调试信息开关。在设备的]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging macsec event]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2450_x2859_143015607}

[[\*Aug 10 18:35:29:602 2013 Sysname MACSEC/7/EVENT: -MDC=1; Received DOWN event on interface GigabitEthernet1/0/1. ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x2450_x2859_x964416567}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_1727913196}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[发生了端口]{style="font-family:宋体"}[Down]{lang="EN-US"}[事件]{style="font-family:宋体"}*

::: {#-1871554430 .myid}
[]{#_Toc404794063}[]{#struct_0_x2450_x2859_1668386960}[]{#_Toc363638092}

**MACsec \-- MACsec调试命令 \-- debugging macsec mka fsm**

------------------------------------------------------------------------

[**[debugging macsec mka fsm]{lang="EN-US"}**]{#struct_0_x2450_x2859_x1676341358}[命令用来打开端口的]{style="font-family:
宋体"}[MKA]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ debugging macsec mka fsm]{lang="EN-US"}**]{#struct_0_x2450_x2859_913817203}[命令用来关闭端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1473962951}

[**[debugging macsec mka fsm ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2450_x2859_706829830}

[**[undo debugging macsec mka fsm ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2450_x2859_1590793516}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_478083705}

[[端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_x2450_x2859_957857490}[状态机调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1570953993}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2450_x2859_x1271479674}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x2111803980}

[[network-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_x281106780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_1091841429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_594993932}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2450_x2859_x1799861444}[：打开指定端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[状态机调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开所有端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1800302561}

[[表1-3 ]{lang="EN-US"}[debugging macsec mka fsm]{lang="EN-US"}]{#struct_0_x2450_x2859_x179263561}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x298169832}[[字段]{style="font-family:黑体"}]{#struct_0_x2450_x2859_706895366}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1550935810}

[[Transitioned to *state* state on interface **** *interface-type interface-number.*]{lang="EN-US"}]{#struct_0_x2450_x2859_124405528}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x705960451}[的状态发生迁移，]{style="font-family:宋体"}*[state]{lang="EN-US"}*[表示迁移到的状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_CHANGE]{lang="EN-US"}]{#struct_0_x2450_x2859_881586625}[：表示端口连接状态变化，状态机准备迁移]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_ALLOWED]{lang="EN-US"}]{#struct_0_x2450_x2859_x186119951}[：表示端口未认证，允许收发未加密报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_AUTHENTICATED]{lang="EN-US"}]{#struct_0_x2450_x2859_1482888231}[：表示端口通过认证，允许收发未加密报文]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_SECURED]{lang="EN-US"}]{#struct_0_x2450_x2859_1993527699}[：表示端口采用安全通信方式，准备安装收发]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_RECEIVE]{lang="EN-US"}]{#struct_0_x2450_x2859_x823604050}[：表示端口安装接收]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_RECEIVING]{lang="EN-US"}]{#struct_0_x2450_x2859_x1606144207}[：表示端口入方向就绪，可接收新]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[加密的报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_READY]{lang="EN-US"}]{#struct_0_x2450_x2859_706960902}[：表示端口等待]{lang="EN-US" style="font-family:宋体"}[Key Server]{lang="EN-US"}[通知，准备安装发送]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_TRANSMIT]{lang="EN-US"}]{#struct_0_x2450_x2859_x1132459803}[：表示端口使能发送]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_TRANSMITTING]{lang="EN-US"}]{#struct_0_x2450_x2859_2105956816}[：表示端口出方向就绪，可以发送新]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}[加密的报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_ABANDON]{lang="EN-US"}]{#struct_0_x2450_x2859_182648661}[：表示端口丢弃了刚生成的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CP_RETIRE]{lang="EN-US"}]{#struct_0_x2450_x2859_475679269}[：表示端口出入方向都已就绪，可使用新]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[收发报文]{lang="EN-US" style="font-family:宋体"}

[*[timer]{lang="EN-US"}*[ timer expired on interface *interface-type interface-number*.]{lang="EN-US"}]{#struct_0_x2450_x2859_355411765}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1311118291}[的定时器超时。]{style="font-family:宋体"}*[timer]{lang="EN-US"}*[表示定时器类型，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RetireWhen]{lang="EN-US"}]{#struct_0_x2450_x2859_402022281}[：新的]{style="font-family:宋体"}[SAK]{lang="EN-US"}[应用于发送]{style="font-family:宋体"}[SC]{lang="EN-US"}[后，强制在定时器溢出前不再应用新的]{style="font-family:宋体"}[SAK]{lang="EN-US"}[用于发送]{style="font-family:宋体"}[SC]{lang="EN-US"}[。定时器超时值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TransmitWhen]{lang="EN-US"}]{#struct_0_x2450_x2859_x1201797034}[：]{lang="EN-US" style="font-family:宋体"}[Key Server]{lang="EN-US"}[应用新的]{lang="EN-US" style="font-family:宋体"}[SAK]{lang="EN-US"}[用于发送]{lang="EN-US" style="font-family:宋体"}[SC]{lang="EN-US"}[前，需等待对端通知已应用新的]{lang="EN-US" style="font-family:宋体"}[SAK]{lang="EN-US"}[用于接收]{lang="EN-US" style="font-family:宋体"}[SC]{lang="EN-US"}[。为了防止]{lang="EN-US" style="font-family:宋体"}[Key Server]{lang="EN-US"}[无限期的等待对端通知，定时器溢出前，]{lang="EN-US" style="font-family:宋体"}[Key Server]{lang="EN-US"}[必须收到通知。定时器超时值为]{lang="EN-US" style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_707026438}

[[\# ]{lang="EN-US"}]{#struct_0_x2450_x2859_x117641805}[在设备上打开]{style="font-family:宋体"}[MKA]{lang="EN-US"}[状态机调试信息开关。当设备接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[SAK]{lang="EN-US"}[刷新时，输出如下调试信息。]{style="font-family:宋体"}

[[\<Sysname\> debugging macsec mka fsm]{lang="PT-BR"}]{#struct_0_x2450_x2859_927686212}

[\*Sep 12 13:27:51:780 2013 Sysname MACSEC/7/FSM: -MDC=1; Transferred to CP_RECEIVE state on interface GigabitEthernet1/0/1.]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_x228836145}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的状态机处于]{style="font-family:宋体"}[CP_RECEIVE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Sep 12 13:27:51:781 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_RECEIVING state on interface GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x2450_x2859_1608849570}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_800537691}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的状态机处于]{style="font-family:宋体"}[CP_RECEIVING]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Sep 12 13:27:51:786 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_TRANSMIT state on interface GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x2450_x2859_x1945032951}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_x2028703116}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的状态机处于]{style="font-family:宋体"}[CP_TRANSMIT]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Sep 12 13:27:51:786 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_TRANSMITTING state on interface GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x2450_x2859_x1637894688}

[*[// ]{lang="EN-US"}*]{#struct_0_x2450_x2859_1429757585}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的状态机处于]{style="font-family:宋体"}[CP_TRANSMITTING]{lang="EN-US"}[状态]{style="font-family:宋体"}*

[[\*Sep 12 13:27:55:780 2013 Sysname MACSEC/7/FSM: -MDC=1; Transitioned to CP_RETIRE state on interface GigabitEthernet1/0/1.]{lang="EN-US"}]{#struct_0_x2450_x2859_x458637604}

[*[/ /]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1766145394}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的状态机处于]{style="font-family:宋体"}[CP_RETIRE]{lang="EN-US"}[状态]{style="font-family:宋体"}*

::: {#-1138246759 .myid}
[]{#_Toc404794064}[]{#struct_0_x2450_x2859_706567686}[]{#_Toc363638093}

**MACsec \-- MACsec调试命令 \-- debugging macsec mka packet**

------------------------------------------------------------------------

[**[debugging macsec mka packet]{lang="EN-US"}**]{#struct_0_x2450_x2859_1872229568}[命令用来打开端口的]{style="font-family:
宋体"}[MKA]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ debugging macsec mka packet]{lang="EN-US"}**]{#struct_0_x2450_x2859_x840164392}[命令用来关闭端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x994689448}

[**[debugging macsec mka packet]{lang="EN-US"}**[ \[ **send** \| **receive** \] \[ **interface** *interface-type interface-number* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x2450_x2859_1830292728}

[**[undo debugging macsec mka packet ]{lang="EN-US"}**[\[ **send** \| **receive** \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2450_x2859_x945750383}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x1465642631}

[[端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_x2450_x2859_361399596}[报文调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_1387485542}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2450_x2859_882621937}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_1987471133}

[[network-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_x23336054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2450_x2859_x196222410}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x782484404}

[**[send]{lang="EN-US"}**]{#struct_0_x2450_x2859_706633222}[：打开发送]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[receive]{lang="EN-US"}**]{#struct_0_x2450_x2859_950739737}[：打开接收]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的调试信息开关。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x2450_x2859_1694736358}[：打开指定端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文调试信息开关，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，则打开所有端口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x2450_x2859_x2048966276}[：打开]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的详细调试信息开关。如果未指定本参数，则打开]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的摘要调试信息开关。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_417002349}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[send]{lang="EN-US"}**]{#struct_0_x2450_x2859_1667142824}[和]{style="font-family:宋体"}**[receive]{lang="EN-US"}**[参数，则表示同时打开发送和接收]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的调试信息开关；]{style="font-family:宋体"}**[debugging all]{lang="EN-US"}**[和]{style="font-family:宋体"}**[debugging macsec all]{lang="EN-US"}**[命令优先打开]{style="font-family:宋体"}[MKA]{lang="EN-US"}[报文的摘要调试信息开关。]{style="font-family:宋体"}

[[表1-4 ]{lang="EN-US"}[debugging macsec mka packet]{lang="EN-US"}]{#struct_0_x2450_x2859_x1827193628}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x271441244}[[字段]{style="font-family:黑体"}]{#struct_0_x2450_x2859_617178007}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2450_x2859_465311352}

[[Sent]{lang="EN-US"}]{#struct_0_x2450_x2859_x354242083}***[ ]{lang="EN-US"}***[a MACsec Packet (length: *length*) on interface **** ]{lang="EN-US"}*[interface-type interface-number]{lang="EN-US"}*[.]{lang="EN-US"}

[[接口]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2450_x2859_x777058135}[发送报文，报文长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Received a MACsec Packet (length: *length*) on interface interface-type interface-number]{lang="EN-US"}]{#struct_0_x2450_x2859_706698758}

[[接口]{style="font-family:宋体"}]{#struct_0_x2450_x2859_121138020}*[interface-type interface-number]{lang="EN-US"}*[收到报文，报文长度是]{style="font-family:宋体"}*[length]{lang="EN-US"}*

[[Basic parameters]{lang="EN-US"}]{#struct_0_x2450_x2859_1761674568}

[[基本参数集信息]{style="font-family:宋体"}]{#struct_0_x2450_x2859_x2041895441}

[[Live Peer List parameters]{lang="EN-US"}]{#struct_0_x2450_x2859_x493518534}

[]{#struct_0_x2450_x2859_2147057965}[[Live Peer List]{lang="EN-US"}]{#_Toc348878024}[参数集]{style="font-family:宋体"}[信息]{style="font-family:宋体"}

[[Potential Peer List parameters]{lang="EN-US"}]{#struct_0_x2450_x2859_x1316687788}

[[Potential Peer List]{lang="EN-US"}]{#struct_0_x2450_x2859_x1320725257}[参数集信息]{style="font-family:宋体"}

[[Distributed SAK parameters]{lang="EN-US"}]{#struct_0_x2450_x2859_x1074847031}

[[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_1979885493}[分发参数集信息]{style="font-family:宋体"}

[[SAK Use parameters]{lang="EN-US"}]{#struct_0_x2450_x2859_706764294}

[[SAK USE]{lang="EN-US"}]{#struct_0_x2450_x2859_536617554}[参数集信息]{style="font-family:宋体"}

[[Tx priority]{lang="EN-US"}]{#struct_0_x2450_x2859_x1374713428}

[[报文发送端的优先级]{style="font-family:宋体"}]{#struct_0_x2450_x2859_1275700336}

[[Key Server]{lang="EN-US"}]{#struct_0_x2450_x2859_x867552087}

[[是否是]{style="font-family:宋体"}[Key Server]{lang="EN-US"}]{#struct_0_x2450_x2859_1851329123}[，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示是，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不是]{style="font-family:宋体"}

[[MACsec desire]{lang="EN-US"}]{#struct_0_x2450_x2859_1052726643}

[[接口是否期望对发送的数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_x2450_x2859_881617170}[保护，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示期望保护，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不期望保护]{style="font-family:宋体"}

[[MACsec capability]{lang="EN-US"}]{#struct_0_x2450_x2859_707354118}

[[发送端的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_x2450_x2859_178955851}[能力，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x2450_x2859_82694645}[：表示不支持]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_x2450_x2859_x391637184}[：表示只支持完整性服务，不支持机密性服务]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_x2450_x2859_x171468022}[：]{style="font-family:宋体"} [表示支持完整性服务，可选择支持机密性服务（加密偏移量只能为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_x2450_x2859_125328809}[：]{style="font-family:宋体"} [表示支持完整性服务，可选择支持机密性服务（加密偏移量可支持]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[30]{lang="EN-US"}[及]{style="font-family:宋体"}[50]{lang="EN-US"}[）]{style="font-family:宋体"}

[[MI]{lang="EN-US"}]{#struct_0_x2450_x2859_1438698018}

[[Live Peer]{lang="EN-US"}]{#struct_0_x2450_x2859_707419654}[或]{style="font-family:宋体"}[Potential Peer]{lang="EN-US"}[的成员]{style="font-family:宋体"}[ID]{lang="EN-US"}[，在基本参数集中表示本端的成员]{style="font-family:宋体"}[ID]{lang="EN-US"}[，在]{style="font-family:宋体"}[Live Peer]{lang="EN-US"}[或]{style="font-family:宋体"}[Potential Peer]{lang="EN-US"}[参数集中表示对端的成员]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[MN]{lang="EN-US"}]{#struct_0_x2450_x2859_x1569401088}

[[消息编号，在基本参数集中表示本端的消息标号，在]{style="font-family:宋体"}[Live Peer]{lang="EN-US"}]{#struct_0_x2450_x2859_1217565890}[或]{style="font-family:宋体"}[Potential Peer]{lang="EN-US"}[参数集中表示对端的消息编号]{style="font-family:宋体"}

[[CKN]{lang="EN-US"}]{#struct_0_x2450_x2859_x970104228}

[[CAK]{lang="EN-US"}]{#struct_0_x2450_x2859_2140984422}[的标识，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字节的十六进制字符]{style="font-family:宋体"}

[[Plain Tx]{lang="EN-US"}]{#struct_0_x2450_x2859_x132619362}

[[是否采用明文进行发送，]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x2450_x2859_876286740}[表示明文发送，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示密文发送]{style="font-family:宋体"}

[[Plain Rx]{lang="EN-US"}]{#struct_0_x2450_x2859_706829825}

[[是否采用明文进行接收，]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_x2450_x2859_x747858641}[表示明文接收，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示密文接收]{style="font-family:宋体"}

[[Latest Key's AN]{lang="EN-US"}]{#struct_0_x2450_x2859_x964512091}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_593562212}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Latest Key for Tx]{lang="EN-US"}]{#struct_0_x2450_x2859_913042961}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_1042899579}[是否用于发送，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示用于发送，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不用于发送]{style="font-family:宋体"}

[[Latest Key for Rx]{lang="EN-US"}]{#struct_0_x2450_x2859_706895361}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x1550935807}[是否用于接收，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示用于接收，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不用于接收]{style="font-family:宋体"}

[[Latest Key Server's MI]{lang="EN-US"}]{#struct_0_x2450_x2859_2046785365}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x1494558357}[的]{style="font-family:宋体"}[Key Server]{lang="EN-US"}[的成员]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Latest KN]{lang="EN-US"}]{#struct_0_x2450_x2859_x1302494264}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x964083343}[的编号]{style="font-family:宋体"}

[[Latest LPN]{lang="EN-US"}]{#struct_0_x2450_x2859_706960897}

[[最近]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x375679931}[的最小可接受报文编号]{style="font-family:宋体"}

[[Old Key's AN]{lang="EN-US"}]{#struct_0_x2450_x2859_x1781667509}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x594946497}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Old Key for Tx]{lang="EN-US"}]{#struct_0_x2450_x2859_994381766}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x148825243}[是否用于发送，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示用于发送，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不用于发送]{style="font-family:宋体"}

[[Old Key for Rx]{lang="EN-US"}]{#struct_0_x2450_x2859_707026433}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x117641812}[是否用于接收，]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示用于接收，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示不用于接收]{style="font-family:宋体"}

[[Old Key Server's MI]{lang="EN-US"}]{#struct_0_x2450_x2859_927751747}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_1350015374}[的]{style="font-family:宋体"}[Key Server]{lang="EN-US"}[成员]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Old KN]{lang="EN-US"}]{#struct_0_x2450_x2859_1031527951}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_706567681}[的编号]{style="font-family:宋体"}

[[Old LPN]{lang="EN-US"}]{#struct_0_x2450_x2859_1872229569}

[[旧的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x840229928}[的最小可接受报文编号]{style="font-family:宋体"}

[[Distributed SAK's AN]{lang="EN-US"}]{#struct_0_x2450_x2859_x1019008483}

[[分发]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x774040689}[所属]{style="font-family:宋体"}[SA]{lang="EN-US"}[的编号，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}

[[Confidentiality offset]{lang="EN-US"}]{#struct_0_x2450_x2859_706633217}

[[加密偏移]{style="font-family:宋体"}[,]{lang="EN-US"}]{#struct_0_x2450_x2859_x1387912418}[取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unused]{lang="EN-US"}]{#struct_0_x2450_x2859_1566865824}[：表示使用明文通信]{style="font-family:宋体"}[,]{lang="EN-US"}[不使用]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x2450_x2859_x1841456692}[：表示使用加密偏移，偏移值为]{style="font-family:宋体"}[0]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[30]{lang="EN-US"}]{#struct_0_x2450_x2859_653107523}[：表示使用加密偏移，偏移值为]{style="font-family:宋体"}[30]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[50]{lang="EN-US"}]{#struct_0_x2450_x2859_706698753}[：表示使用加密偏移，偏移值为]{style="font-family:宋体"}[50]{lang="EN-US"}

[[SAK No.]{lang="EN-US"}]{#struct_0_x2450_x2859_121138031}

[[SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x576977591}[的编号]{style="font-family:宋体"}

[[Wrapped SAK]{lang="EN-US"}]{#struct_0_x2450_x2859_x205960719}

[[经过]{style="font-family:宋体"}[AES-CMAC]{lang="EN-US"}]{#struct_0_x2450_x2859_x564137528}[算法加密的]{style="font-family:宋体"}[SAK]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2450_x2859_x622964481}

[[\# ]{lang="EN-US"}]{#struct_0_x2450_x2859_706764289}[在设备上打开]{style="font-family:宋体"}[MKA]{lang="PT-BR"}[报文的摘要调试信息开关。当设备的]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和对端]{style="font-family:宋体"}[建立会话后，输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging macsec mka packet]{lang="EN-US"}]{#struct_0_x2450_x2859_x1419697587}

[\*Nov 11 10:02:55:374 2013 Sysname MACSEC/7/PKT: -MDC=1;]{lang="EN-US"}

[Received a MACsec Packet (length: 120) on interface GigabitEthernet1/0/1.]{lang="EN-US"}

[Basic Parameters]{lang="EN-US"}

[Tx priority           : 0]{lang="EN-US"}

[MACsec desire         : No]{lang="EN-US"}

[Key Server            : Yes]{lang="EN-US"}

[MACsec capability     : 3]{lang="EN-US"}

[MI                    : 1F777A1092C1702A19FC9450]{lang="EN-US"}

[MN                    : 21]{lang="EN-US"}

[CKN                   : 1234]{lang="EN-US"}

[SAK Use parameters]{lang="EN-US"}

[Plain Tx              : No]{lang="EN-US"}

[Plain Rx              : No]{lang="EN-US"}

[Old Key\'s AN          : 0]{lang="EN-US"}

[Old Key for Tx        : Yes]{lang="EN-US"}

[Old Key for Rx        : Yes]{lang="EN-US"}

[Old KN                : 1]{lang="EN-US"}

[Old LPN               : 131]{lang="EN-US"}

[Old Key Server's MI   : 1F777A1092C1702A19FC9450]{lang="EN-US"}

[Live Peer List parameters]{lang="EN-US"}

[MI                    : 229DAD7854B5E6FA42124793]{lang="EN-US"}

[MN                    : 21]{lang="EN-US"}

[*[//]{lang="EN-US"}*]{#struct_0_x2450_x2859_x1584138907}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收对端报文，长度为]{style="font-family:宋体"}[120]{lang="EN-US"}[字节，对报文进行解析得到如下信息：接收的报文编号是]{style="font-family:宋体"}[21]{lang="EN-US"}[，成员]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1F777A1092C1702A19FC9450]{lang="EN-US"}[，对端是]{style="font-family:宋体"}[Key Server]{lang="EN-US"}[，优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[，需要加密保护，]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[能力是]{style="font-family:宋体"}[3]{lang="EN-US"}[，]{style="font-family:宋体"}[CKN]{lang="EN-US"}[是]{style="font-family:宋体"}[1234]{lang="EN-US"}[，并有一个]{style="font-family:宋体"}[Live Peer]{lang="EN-US"}[，即本端，是]{style="font-family:宋体"}[Client]{lang="EN-US"}[，报文编号是]{style="font-family:宋体"}[21]{lang="EN-US"}[，成员]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[229DAD7854B5E6FA42124793]{lang="EN-US"}[，使用]{style="font-family:宋体"}[Old key]{lang="EN-US"}[加解密发送和接收的报文，]{style="font-family:宋体"}[Old key]{lang="EN-US"}[的编号是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[LPN]{lang="EN-US"}[是]{style="font-family:宋体"}[131]{lang="EN-US"}[。]{style="font-family:宋体"}*

[[\# ]{lang="PT-BR"}]{#struct_0_x2450_x2859_1817289523}[在设备上打开]{style="font-family:宋体"}[MKA]{lang="PT-BR"}[报文的详细调试信息开关。当设备的]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和对端]{style="font-family:宋体"}[建立会话后，输出如下调试信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging macsec mka packet verbose]{lang="PT-BR"}]{#struct_0_x2450_x2859_707354113}

[\*Nov 11 10:08:06:375 2013 Sysname MACSEC/7/PKT: -MDC=1;]{lang="PT-BR"}

[Sent a MACsec Packet (length: 120) on interface ]{lang="PT-BR"}[GigabitEthernet1/0/1]{lang="EN-US"}[.]{lang="PT-BR"}

[03 05 00 74 01 00 70 1e 00 0c 29 94 b7 5c 00 07]{lang="PT-BR"}

[22 9d ad 78 54 b5 e6 fa 42 12 47 93 00 00 00 b3]{lang="PT-BR"}

[00 80 c2 01 12 34 00 00 03 07 00 28 00 00 00 00]{lang="PT-BR"}

[00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00]{lang="PT-BR"}

[1f 77 7a 10 92 c1 70 2a 19 fc 94 50 00 00 00 02]{lang="PT-BR"}

[00 00 00 9d 01 00 00 10 1f 77 7a 10 92 c1 70 2a]{lang="PT-BR"}

[19 fc 94 50 00 00 00 b0 cc 55 07 84 34 6d 7f 74]{lang="PT-BR"}

[26 8e 99 bd 42 45 4e 4c]{lang="PT-BR"}

[*[// ]{lang="PT-BR"}*]{#struct_0_x2450_x2859_178955846}*[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送的长度为]{style="font-family:宋体"}[120]{lang="PT-BR"}[字节的]{style="font-family:宋体"}[MKA]{lang="PT-BR"}[报文内容]{style="font-family:宋体"}*
