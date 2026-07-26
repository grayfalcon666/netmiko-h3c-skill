::: {#-1393833350 .myid}
[]{#_Toc404783904}[]{#struct_0_14203_x1491_622757639}[]{#_Toc344393999}

**MAC地址表 \-- MAC地址表调试命令 \-- debugging mac-address**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_14203_x1491_1022700631}

[**[debugging mac-address ]{lang="EN-US"}**[{ **event** \| **hardware** \| **search** \| **synchronization** }]{lang="EN-US"}]{#struct_0_14203_x1491_x942394494}

[**[undo debugging mac-address ]{lang="EN-US"}**[{ **event** \| **hardware** \| **search** \| **synchronization** }]{lang="EN-US"}]{#struct_0_14203_x1491_667631242}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14203_x1491_x2081816554}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14203_x1491_x142345636}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14203_x1491_x1040207073}

[[network-admin]{lang="EN-US"}]{#struct_0_14203_x1491_x1850863030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14203_x1491_x544797304}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14203_x1491_105171561}

[**[event]{lang="EN-US"}**]{#struct_0_14203_x1491_622823175}[：表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表模块事件调试信息开关。]{style="font-family:宋体"}

[**[hardware]{lang="EN-US"}**]{#struct_0_14203_x1491_59804345}[：表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表模块下驱动调试信息开关。]{style="font-family:宋体"}

[**[search]{lang="EN-US"}**]{#struct_0_14203_x1491_1219836321}[：表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表模块向驱动查找]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时的调试开关。]{style="font-family:宋体"}

[**[synchronization]{lang="EN-US"}**]{#struct_0_14203_x1491_2010049877}[：表示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表模块板间同步调试开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14203_x1491_1142368488}

[**[debugging mac-address]{lang="EN-US"}**]{#struct_0_14203_x1491_x1465390903}[命令用来打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表调试信息开关。]{style="font-family:宋体"}**[undo debugging mac-address]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_x2104513050}[地址表调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging mac-address]{lang="EN-US"}[ event]{lang="EN-US"}]{#struct_0_14203_x1491_x1413822989}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1489761899}[[字段]{style="font-family:黑体"}]{#struct_0_14203_x1491_187948014}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14203_x1491_622888711}

[[Received VLAN event, Event type: *type*, Interface *interface-name*, VLAN list: *list*]{lang="EN-US"}]{#struct_0_14203_x1491_20226761}

[[收到]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14203_x1491_213072526}[事件（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}

[[Received interface event, Event type: *type*, interface number: *number*, Sequence: *Sequence*, Interface list: *interface-name-list*]{lang="EN-US"}]{#struct_0_14203_x1491_x874266246}

[[收到接口事件（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}]{#struct_0_14203_x1491_x257376901}

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging mac-address]{lang="EN-US"}[ hardware]{lang="EN-US"}]{#struct_0_14203_x1491_1629435526}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1490589827}[[字段]{style="font-family:黑体"}]{#struct_0_14203_x1491_x1767910004}

[[描述]{style="font-family:黑体"}]{#struct_0_14203_x1491_622954247}

[[Notify driver to add an item: MAC address *mac-address*, VLAN ID *vid*, State *state*, Interface *interface-name*.]{lang="EN-US"}]{#struct_0_14203_x1491_1601240773}

[[Return of adding item: result *result*, Driver context\[0\] *context*, Driver context\[1\] *context*]{lang="EN-US"}]{#struct_0_14203_x1491_1393042478}

[[通知驱动添加一条表项并返回添加结果（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}]{#struct_0_14203_x1491_x672960644}

[[Notify driver to delete an item: MAC address *mac-address*, VLAN ID *vid*, State *state*, Interface *interface-name*, Driver context\[0\] *context*, Driver context\[1\] *context*]{lang="EN-US"}]{#struct_0_14203_x1491_x618003745}

[[Return of deleting item: result *result*]{lang="EN-US"}]{#struct_0_14203_x1491_x968657949}

[[通知驱动删除一条表项并返回删除结果（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}]{#struct_0_14203_x1491_1784893895}

[[MAC change notification from driver: Type *type*, Interface *interface-name*, VLAN ID *vid*, MAC type *type*, MAC address *mac-address*]{lang="EN-US"}]{#struct_0_14203_x1491_623019783}

[[驱动]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_x810903199}[变化的通知（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}

[[Set the MAC *action* notification flag *flag* of interface *interface-name* to driver(1 enable, 2 disable)]{lang="EN-US"}]{#struct_0_14203_x1491_x298617542}

[[向驱动设置接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_282172166}[变化通知标记]{style="font-family:宋体"}

[[Set MAC address learning priority for interface *interface-name*: *priority* (1 high, 2 low)]{lang="EN-US"}]{#struct_0_14203_x1491_x1497916447}

[[设置接口地址学习优先级]{style="font-family:宋体"}]{#struct_0_14203_x1491_x180074326}

[[Set forwarding status for interface *interface-name*: *status* (1 enable, 2 disable)]{lang="EN-US"}]{#struct_0_14203_x1491_622036743}

[[设置接口的转发状态：]{style="font-family:宋体"}]{#struct_0_14203_x1491_x176578274}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14203_x1491_520248715}[：允许转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_14203_x1491_1494511934}[：禁止转发]{lang="EN-US" style="font-family:宋体"}

[[Set forwarding status for VLAN ID *vid*: *status* (1 enable, 2 disable)]{lang="EN-US"}]{#struct_0_14203_x1491_1641472878}

[[设置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14203_x1491_858937882}[的转发状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14203_x1491_622102279}[：允许转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_14203_x1491_x1743519846}[：禁止转发]{lang="EN-US" style="font-family:宋体"}

[[Set max address number for interface *interface-name*: *number*]{lang="EN-US"}]{#struct_0_14203_x1491_x1205871886}

[[设置接口下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_x1755836331}[学习最大个数]{style="font-family:宋体"}

[[Set max address number for VLAN ID *vid*: *number*]{lang="EN-US"}]{#struct_0_14203_x1491_1166535457}

[[设置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14203_x1491_622561032}[下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[学习最大个数]{style="font-family:宋体"}

[[Set learning status for VLAN ID *vid*: *status* (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)]{lang="EN-US"}]{#struct_0_14203_x1491_x1608248013}

[[设置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14203_x1491_x1647211180}[的表项学习状态，其中]{style="font-family:宋体"}[status]{lang="EN-US"}[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_14203_x1491_510851476}[：]{lang="EN-US" style="font-family:宋体"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14203_x1491_x136845895}[：]{lang="EN-US" style="font-family:宋体"}[不学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_14203_x1491_622626568}[：不学习并丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_14203_x1491_1375647824}[：不学习、丢弃、并通知平台]{style="font-family:宋体"}

[[Set learning status for interface *interface-name*: *status* (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)]{lang="EN-US"}]{#struct_0_14203_x1491_117144522}

[[设置接口的表项学习状态，其中]{style="font-family:宋体"}[status]{lang="EN-US"}]{#struct_0_14203_x1491_453022294}[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_14203_x1491_622692104}[：]{lang="EN-US" style="font-family:宋体"}[学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14203_x1491_x1732080735}[：]{lang="EN-US" style="font-family:宋体"}[不学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_14203_x1491_x598526722}[：不学习并丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_14203_x1491_x2012147907}[：不学习、丢弃、并通知平台]{style="font-family:宋体"}

[[Set global address learning status: status (0 learn, 1 not learn, 3 not learn & drop, 7 not learn & drop & notify)]{lang="EN-US"}]{#struct_0_14203_x1491_622757640}

[[设置全局的表项学习状态，其中]{style="font-family:宋体"}[status]{lang="EN-US"}]{#struct_0_14203_x1491_x1315951520}[的取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_14203_x1491_x1553222493}[：学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14203_x1491_23764349}[：不学习]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_14203_x1491_622823176}[：不学习并丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[7]{lang="EN-US"}]{#struct_0_14203_x1491_59804342}[：不学习、丢弃、并通知平台]{style="font-family:宋体"}

[[Set MAC roaming: Action: *action*]{lang="EN-US"}]{#struct_0_14203_x1491_x736478815}

[[设置]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_x549157013}[全局同步]{style="font-family:宋体"}

[[Return of setting control: result *result*]{lang="EN-US"}]{#struct_0_14203_x1491_622888712}

[[设置控制信息后的返回结果]{style="font-family:宋体"}]{#struct_0_14203_x1491_20226762}

[[New data: Learn *data*, Drop *data*, Notify *data*]{lang="EN-US"}]{#struct_0_14203_x1491_x1743242610}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_1995615489}[未知报文学习设置新数据]{style="font-family:宋体"}

[[Old data: Learn *data*, Drop *data*, Notify *data*]{lang="EN-US"}]{#struct_0_14203_x1491_622954248}

[[源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_1601240772}[未知报文学习设置旧数据]{style="font-family:宋体"}

[[Check unknown MAC: Scope *scope*, VLAN ID *vid*, Interface *interface-name*, Action *action*, Result *result*]{lang="EN-US"}]{#struct_0_14203_x1491_1393108014}

[[检查源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_623019784}[未知报文学习能力（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}

[[Set unknown MAC: Module *module*, Scope *scope*, VLAN ID *vid*, Interface *interface-name*, Action *action*, MDCDeletingFlag *flag*]{lang="EN-US"}]{#struct_0_14203_x1491_x810903192}

[[设置源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_x299207366}[未知报文学习动作（非主控板、备板和当前接口所在板，接口名会显示为接口索引）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging mac-address]{lang="EN-US"}[ search]{lang="EN-US"}]{#struct_0_14203_x1491_1833409048}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1192614103}[[字段]{style="font-family:黑体"}]{#struct_0_14203_x1491_x348699440}

[[描述]{style="font-family:黑体"}]{#struct_0_14203_x1491_622036744}

[[Find item from driver: MAC address *mac-addres*s, VLAN ID *vid*]{lang="EN-US"}]{#struct_0_14203_x1491_x176578271}

[[Return of finding item: result *result*, MAC address *mac-addres*s, VLAN ID *vid*, State *state*, Interface *interface-name*]{lang="EN-US"}]{#struct_0_14203_x1491_520445323}

[[向驱动查询一条表项并返回查询结果]{style="font-family:宋体"}]{#struct_0_14203_x1491_1021484752}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging mac-address]{lang="EN-US"}[ synchronization]{lang="EN-US"}]{#struct_0_14203_x1491_x812818197}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1198142570}[[字段]{style="font-family:黑体"}]{#struct_0_14203_x1491_x72058880}

[[描述]{style="font-family:黑体"}]{#struct_0_14203_x1491_1670227472}

[[Received message from *channel* of chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_14203_x1491_622102280}

[[收到从框号为]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_14203_x1491_x551878767}[板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[通道为]{style="font-family:宋体"}*[channel]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[[Connected to *channel* of chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_14203_x1491_x1875470366}

[[与框号为]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_14203_x1491_341617449}[板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[的]{style="font-family:宋体"}*[channel]{lang="EN-US"}*[通道建立连接]{style="font-family:宋体"}

[[Disconnected from *channel* of chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_14203_x1491_75026153}

[[与框号为]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_14203_x1491_x1509664152}[板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[的]{style="font-family:宋体"}*[channel]{lang="EN-US"}*[通道断开]{style="font-family:宋体"}

[[Pull global configuration]{lang="EN-US"}]{#struct_0_14203_x1491_787840596}

[[从主控板拉全局配置]{style="font-family:宋体"}]{#struct_0_14203_x1491_622561029}

[[Pull interface configuration]{lang="EN-US"}]{#struct_0_14203_x1491_730404142}

[[从主控板拉端口下配置]{style="font-family:宋体"}]{#struct_0_14203_x1491_x1158316291}

[[Pull static configuration]{lang="EN-US"}]{#struct_0_14203_x1491_x650989649}

[[从主控板拉]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14203_x1491_516760358}[静态表项]{style="font-family:宋体"}

[[Pull VLAN configuration]{lang="EN-US"}]{#struct_0_14203_x1491_770351447}

[[从主控板拉]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14203_x1491_622626565}[下配置]{style="font-family:宋体"}

[[Pull smooth status]{lang="EN-US"}]{#struct_0_14203_x1491_1375647821}

[[从主控板拉平滑状态]{style="font-family:宋体"}]{#struct_0_14203_x1491_117472202}

[[Failed to send synchronization message]{lang="EN-US"}]{#struct_0_14203_x1491_1401298398}

[[发送同步消息失败]{style="font-family:宋体"}]{#struct_0_14203_x1491_x1665808133}

[[Enqueue message: Type: *type*, Length: *length*, Number: *number*]{lang="EN-US"}]{#struct_0_14203_x1491_1558420739}

[[消息入实时同步队列]{style="font-family:宋体"}]{#struct_0_14203_x1491_622692101}

[[Received pull message from chassis *chassis-number* slot *slot-number*]{lang="EN-US"}]{#struct_0_14203_x1491_x1732080740}

[[收到从框号为]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*]{#struct_0_14203_x1491_x1001483569}[板号为]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[PULL]{lang="EN-US"}[消息]{style="font-family:宋体"}

[[Sent synchronization message with length *length*]{lang="EN-US"}]{#struct_0_14203_x1491_x175586190}

[[发送长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_14203_x1491_x2141209077}[的同步消息]{style="font-family:宋体"}

[[Received synchronization message with length *length*]{lang="EN-US"}]{#struct_0_14203_x1491_622757637}

[[接收到长度为]{style="font-family:宋体"}*[length]{lang="EN-US"}*]{#struct_0_14203_x1491_1022700633}[的同步消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14203_x1491_x942525566}

[[\# ]{lang="EN-US"}]{#struct_0_14203_x1491_1424798560}[打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的]{style="font-family:宋体"}[event]{lang="EN-US"}[调试开关，关闭接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-address event]{lang="EN-US"}]{#struct_0_14203_x1491_622823173}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] shutdown]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] \*Dec 27 17:49:11:808 2012 Sysname MAC/7/EVENT: -MDC=1-Chassis=2]{lang="EN-US"}

[-Slot=3;]{lang="EN-US"}

[ Received interface event, Event type: 0x20000040, interface number: 1, Sequence]{lang="EN-US"}

[: 44, interface list:]{lang="EN-US"}

[\*\*\[0\]: GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:49:11:810 2012 Sysname MAC/7/EVENT: -MDC=1;]{lang="EN-US"}

[ Received interface event, Event type: 0x20000040, interface number: 1, Sequence]{lang="EN-US"}

[: 64, interface list:]{lang="EN-US"}

[\*\*\[0\]: GE1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14203_x1491_59804339}[打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的]{style="font-family:宋体"}[hardware]{lang="EN-US"}[调试开关，并添加一条]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-address hardware]{lang="EN-US"}]{#struct_0_14203_x1491_x304352614}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mac-address static 3-2-2 interface gigabitethernet 1/0/1 vlan 10]{lang="EN-US"}

[\[Sysname\] \*Dec 27 17:31:26:161 2012 Sysname MAC/7/HARDWARE: -MDC=1;]{lang="EN-US"}

[ Notify driver to add an item: MAC address 0003-0002-0002, VLAN ID 0xa, State 0x]{lang="EN-US"}

[1, interface GE1/0/1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:31:26:161 2012 Sysname MAC/7/HARDWARE: -MDC=1;]{lang="EN-US"}

[ Return of adding item: result 0x0, Driver context\[0\] 0xffffffffffffffff, Driver]{lang="EN-US"}

[ context\[1\] 0xffffffffffffffff.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:31:26:162 2012 Sysname MAC/7/HARDWARE: -MDC=1-Chassis=2-Slot=3;]{lang="EN-US"}

[ Notify driver to add an item: MAC address 0003-0002-0002, VLAN ID 0xa, State 0x]{lang="EN-US"}

[1, interface GE1/0/1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:31:26:162 2012 Sysname MAC/7/HARDWARE: -MDC=1-Chassis=2-Slot=3;]{lang="EN-US"}

[ Return of adding item: result 0x0, Driver context\[0\] 0xffffffffffffffff, Driver]{lang="EN-US"}

[ context\[1\] 0xffffffffffffffff.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14203_x1491_x1140324404}[打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的]{style="font-family:宋体"}[search]{lang="EN-US"}[调试开关，添加一条多端口]{style="font-family:宋体"}[ARP]{lang="EN-US"}[并匹配多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-address search]{lang="EN-US"}]{#struct_0_14203_x1491_622888709}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mac-address multiport 4-4-4 interface gigabitethernet 1/0/1 vlan 10]{lang="EN-US"}

[\[Sysname\] arp multiport 2.2.2.3 4-4-4 10]{lang="EN-US"}

[\[Sysname\] \*Dec 27 17:40:26:079 2012 Sysname MAC/7/SEARCH: -MDC=1;]{lang="EN-US"}

[ Find item from driver: MAC address 0004-0004-0004, VLAN ID 0xa.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:40:26:079 2012 Sysname MAC/7/SEARCH: -MDC=1;]{lang="EN-US"}

[ Return of finding item: result 0x60010023, MAC address 0004-0004-0004, VLAN ID]{lang="EN-US"}

[0x0, State 0x0, Interface GE1/0/1.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:40:26:112 2012 Sysname MAC/7/SEARCH: -MDC=1-Chassis=2-Slot=3;]{lang="EN-US"}

[ Find item from driver: MAC address 0004-0004-0004, VLAN ID 0xa.]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:40:26:112 2012 Sysname MAC/7/SEARCH: -MDC=1-Chassis=2-Slot=3;]{lang="EN-US"}

[ Return of finding item: result 0x60010023, MAC address 0004-0004-0004, VLAN ID]{lang="EN-US"}

[0xdb81, State 0x0, Interface GE1/0/1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14203_x1491_1976541889}[打开]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的]{style="font-family:宋体"}[synchronization]{lang="EN-US"}[调试开关，添加一条静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项。]{style="font-family:宋体"}

[[\<Sysname\> debugging mac-address synchronization]{lang="EN-US"}]{#struct_0_14203_x1491_622954245}

[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] mac-address static 6-6-6 interface gigabitethernet 1/0/1 vlan 10]{lang="EN-US"}

[\[Sysname\] \*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;]{lang="EN-US"}

[ Connected to user synchronization channel of chassis 2 slot 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;]{lang="EN-US"}

[ Received message from user synchronization channel of chassis 2 slot 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;]{lang="EN-US"}

[ Enqueue message: Type: 0, Length: 64, Number: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1;]{lang="EN-US"}

[ Sent synchronization message with length 64]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:46:18:145 2012 Sysname MAC/7/SYNC: -MDC=1-Chassis=2-Slot=1;]{lang="EN-US"}

[ Received message from multicast synchronization channel of chassis 2 slot 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*Dec 27 17:46:18:217 2012 Sysname MAC/7/SYNC: -MDC=1;]{lang="EN-US"}

[ Disconnected from user synchronization channel of chassis 2 slot 1]{lang="EN-US"}

[ ]{lang="EN-US"}
