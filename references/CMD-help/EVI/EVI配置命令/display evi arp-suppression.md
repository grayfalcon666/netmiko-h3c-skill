::: {#927173033 .myid}
[]{#_Toc404798343}[]{#struct_0_20244_20619_504778375}[]{#_Toc309203838}[]{#_Toc303421790}

**EVI \-- EVI配置命令 \-- display evi arp-suppression**

------------------------------------------------------------------------

[**[display evi arp-suppression]{lang="EN-US"}**]{#struct_0_20244_20619_x1462780197}[命令用来显示]{style="font-family:
宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_71731136}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20244_20619_x1194763915}

[**[display evi arp-suppression interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_x862650830}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20244_20619_2134122883}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display evi arp-suppression interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_439939447}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20244_20619_x1905977872}[模式：]{style="font-family:宋体"}

[**[display evi arp-suppression interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_x1142874684}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_24445653}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_1374082538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_48963134}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1194698379}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_801369177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1401792984}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x801818037}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1096521407}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_x2147097745}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_961527526}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示所有]{style="font-family:宋体"}[VLAN]{lang="FR"}[的]{style="font-family:宋体"}[EVI ARP]{lang="FR"}[泛洪抑制表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_1640923329}[：显示指定]{style="font-family:宋体"}[单板的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示主用主控板上的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_1988873749}[：显示指定成员设备的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_1110097817}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_x1194370699}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示全局主用主控板上的]{style="font-family:宋体"}[EVI ARP]{lang="FR"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_1724938687}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_20244_20619_x1475930455}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_20244_20619_x861796820}[：显示]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1869733131}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1451380417}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> display evi arp-suppression interface tunnel 101]{lang="EN-US"}]{#struct_0_20244_20619_x64518180}

[IP Address      MAC Address    VLAN ID  Interface                Aging Status]{lang="EN-US"}

[1.1.1.2         000f-e201-0101 1        EVI-link1                14    Valid]{lang="EN-US"}

[1.1.1.3         000f-e201-0202 1        EVI-link1                18    Invalid]{lang="EN-US"}

[1.1.1.4         000f-e201-0203 1        EVI-link1                10    Collision]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_960333157}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi arp-suppression interface tunnel 101 count]{lang="EN-US"}]{#struct_0_20244_20619_1236383408}

[Total entries: 3]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display evi arp-suppression]{lang="EN-US"}]{#struct_0_20244_20619_x1194305163}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2054191011}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1038430866}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x894233451}

[[IP Address]{lang="EN-US"}]{#struct_0_20244_20619_1218824109}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_x1904748919}[泛洪抑制表项的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MAC Address]{lang="EN-US"}]{#struct_0_20244_20619_225758172}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_x301554666}[泛洪抑制表项的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_x1194501771}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_1652366286}[泛洪抑制表项所属的激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_1235446153}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_x1857016996}[泛洪抑制表项对应的入接口，也就是学习到]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项的接口]{style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_20244_20619_x1674528869}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_2014453521}[泛洪抑制表项的老化时间，单位为分钟]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_20244_20619_x1194436235}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_1933906896}[泛洪抑制表项的表项状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_20244_20619_x878368057}[：有效。表项建立的初始状态为有效，有效时可以根据该表项进行代答]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_20244_20619_1441094987}[：无效。表项自最后一次更新后]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟内没有收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[更新报文，变为无效状态，此时不能根据该表项代答。无效状态能保持]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟，]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟内无更新报文，则删除该表项]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Collision]{lang="EN-US"}]{#struct_0_20244_20619_1765896546}[：冲突。如果收到]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文时发现相同]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的泛洪抑制表项已经存在，但是]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址发生变化，则认为发生攻击，此时泛洪抑制表项处于冲突状态，不能根据该表项代答，并在]{style="font-family:宋体"}[25]{lang="EN-US"}[分钟后删除此表项]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_20244_20619_x1194108555}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_x1869199008}[泛洪抑制表项的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_883480694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_1156859514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ evi arp-suppression]{lang="EN-US"}**]{#struct_0_20244_20619_1502827589}

::: {#-349076811 .myid}
[]{#_Toc404798344}[]{#struct_0_20244_20619_401637562}[]{#_Toc312867793}

**EVI \-- EVI配置命令 \-- display evi isis brief**

------------------------------------------------------------------------

[**[display evi isis brief]{lang="EN-US"}**]{#struct_0_20244_20619_x2003350062}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_669451171}

[**[display evi isis brief]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_x1194043019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_478975709}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1156005731}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x105601167}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_954754625}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_411739571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1775481389}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x26134480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194632842}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_643484879}[：显示指定]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果不指定本参数]{style="font-family:宋体"}[，将显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x485974673}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2072242250}[显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis brief]{lang="EN-US"}]{#struct_0_20244_20619_x1329515914}

[Site ID: 10]{lang="EN-US"}

[Isolation Count: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Process ID: 0]{lang="EN-US"}

[Network-entity: 00.0011.2200.0001.00]{lang="EN-US"}

[LSP-length receive: 16384]{lang="EN-US"}

[LSP-length originate: 1400]{lang="EN-US"}

[Timers:]{lang="EN-US"}

[  LSP-max-age: 1200s]{lang="EN-US"}

[  LSP-refresh: 900s]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display evi isis brief]{lang="EN-US"}]{#struct_0_20244_20619_272106155}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2048450563}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_x1072325644}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194567306}

[[Site ID]{lang="EN-US"}]{#struct_0_20244_20619_x853475352}

[[本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_x1744065659}

[[Isolation Count]{lang="EN-US"}]{#struct_0_20244_20619_x437856565}

[[本设备被多少其他站点所隔离。若该数目不为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_20244_20619_x853540888}[，则表示本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[仍与其他站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[有冲突且本设备被隔离，则本设备不对外发布]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文；若该数目为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则表示本设备未被隔离，此时对外发布]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Process ID]{lang="EN-US"}]{#struct_0_20244_20619_x1897434425}

[[进程实例号]{style="font-family:宋体"}]{#struct_0_20244_20619_x390164274}

[[Network-entity]{lang="EN-US"}]{#struct_0_20244_20619_613087241}

[[网络实体名称]{style="font-family:宋体"}]{#struct_0_20244_20619_654893525}

[[LSP-length receive]{lang="EN-US"}]{#struct_0_20244_20619_x183973589}

[[可以接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1194763914}[的最大长度]{style="font-family:宋体"}

[[LSP-length originate]{lang="EN-US"}]{#struct_0_20244_20619_703433111}

[[生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_616203930}[的最大长度]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_20244_20619_x536738294}

[[LSP-max-age]{lang="EN-US"}]{#struct_0_20244_20619_1520535444}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1686710937}[的最大生存时间]{style="font-family:宋体"}

[[LSP-refresh]{lang="EN-US"}]{#struct_0_20244_20619_x1194698378}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x764714764}[的刷新周期]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-138722627 .myid}
[]{#_Toc404798345}[]{#struct_0_20244_20619_x749341740}[]{#_Toc312867794}[]{#_Toc338171755}[]{#_Toc338432171}[]{#_Toc338171756}[]{#_Toc338432172}

**EVI \-- EVI配置命令 \-- display evi isis graceful-restart status**

------------------------------------------------------------------------

[**[display evi isis graceful-restart status]{lang="EN-US"}**]{#struct_0_20244_20619_436569507}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_311527061}

[**[display evi isis graceful-restart status]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_x1289290656}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1541489789}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1194370698}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1867086535}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1092947823}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_476236831}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_585996754}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_2134237893}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x326325616}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_1168614183}[：显示指定]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果不指定本参数]{style="font-family:宋体"}[，将显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_162211326}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1194305162}[显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis graceful-restart status]{lang="EN-US"}]{#struct_0_20244_20619_x1690452489}

[Process ID: 0]{lang="EN-US"}

[Restart status: RESTARTING]{lang="EN-US"}

[Restart phase: LSDB synchronization]{lang="EN-US"}

[Restart interval: 300s]{lang="EN-US"}

[T3 remaining time: 65531s]{lang="EN-US"}

[Total number of interfaces: 1]{lang="EN-US"}

[Number of waiting LSPs: 0]{lang="EN-US"}

[T2 remaining time: 56s]{lang="EN-US"}

[  Interface: EVI-Link0]{lang="EN-US"}

[    T1 remaining time: 2]{lang="EN-US"}

[    RA received: N]{lang="EN-US"}

[    CSNP received: N]{lang="EN-US"}

[    T1 expired number: 3]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display evi isis ]{lang="EN-US"}[graceful]{lang="EN-US"}]{#struct_0_20244_20619_71671431}[-restart status]{lang="EN-US"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2049178307}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1338876187}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194501770}

[[Process ID]{lang="EN-US"}]{#struct_0_20244_20619_x1076517069}

[[进程实例号]{style="font-family:宋体"}]{#struct_0_20244_20619_153907816}

[[Restart status]{lang="EN-US"}]{#struct_0_20244_20619_191609336}

[[重启状态：]{style="font-family:宋体"}]{#struct_0_20244_20619_695117658}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_20244_20619_x1036563567}[：重启完成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STARTING]{lang="EN-US"}]{#struct_0_20244_20619_x1849852271}[：重启开始]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESTARTING]{lang="EN-US"}]{#struct_0_20244_20619_x1194436234}[：重启中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UNKNOWN]{lang="EN-US"}]{#struct_0_20244_20619_367822955}[：未知状态]{lang="EN-US" style="font-family:宋体"}

[[Restart phase]{lang="EN-US"}]{#struct_0_20244_20619_x625208628}

[[重启阶段：]{style="font-family:宋体"}]{#struct_0_20244_20619_1567335819}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_20244_20619_1986960116}[：]{style="font-family:宋体"}[初始阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_20244_20619_x1194108554}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC receiving]{lang="EN-US"}]{#struct_0_20244_20619_x303115067}[：]{style="font-family:宋体"}[接收]{lang="EN-US" style="font-family:宋体"}[本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[上报]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stable]{lang="EN-US"}]{#struct_0_20244_20619_906508256}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_20244_20619_x504472944}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新和泛洪的]{style="font-family:宋体"}[阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_20244_20619_x851769297}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[完成的阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknow]{lang="EN-US"}]{#struct_0_20244_20619_x1194043018}[n]{lang="EN-US"}[：]{style="font-family:
  宋体"}[未知阶段]{lang="EN-US" style="font-family:宋体"}

[[Restart interval]{lang="EN-US"}]{#struct_0_20244_20619_2045059650}

[[重启间隔]{style="font-family:宋体"}]{#struct_0_20244_20619_135942349}

[[T3 remaining time]{lang="EN-US"}]{#struct_0_20244_20619_1657915075}

[[定时器]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_20244_20619_591256807}[的剩余时间]{style="font-family:宋体"}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_20244_20619_x1194632845}

[[进程实例下的所有接口数]{style="font-family:宋体"}]{#struct_0_20244_20619_1402999766}

[[Number of waiting LSPs]{lang="EN-US"}]{#struct_0_20244_20619_164379704}

[[等待的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1264321431}[报文数]{style="font-family:宋体"}

[[T2 remaining time]{lang="EN-US"}]{#struct_0_20244_20619_377005689}

[[定时器]{style="font-family:宋体"}[T2]{lang="EN-US"}]{#struct_0_20244_20619_x1194567309}[的剩余时间]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_1281787624}

[[接口名]{style="font-family:宋体"}]{#struct_0_20244_20619_1847383268}

[[T1 remaining time]{lang="EN-US"}]{#struct_0_20244_20619_x2121740452}

[[定时器]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_20244_20619_x1194763917}[的剩余时间]{style="font-family:宋体"}

[[RA received]{lang="EN-US"}]{#struct_0_20244_20619_300148584}

[[RA]{lang="EN-US"}]{#struct_0_20244_20619_x551722249}[接收标记位]{style="font-family:宋体"}

[[CSNP received]{lang="EN-US"}]{#struct_0_20244_20619_x293992071}

[[CSNP]{lang="EN-US"}]{#struct_0_20244_20619_x1194698381}[接收标记位]{style="font-family:宋体"}

[[T1 expired number]{lang="EN-US"}]{#struct_0_20244_20619_1156616497}

[[定时器]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_20244_20619_x1942329036}[的超时次数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#482573732 .myid}
[]{#_Toc404798346}[]{#struct_0_20244_20619_x1382011896}[]{#_Toc312867796}

**EVI \-- EVI配置命令 \-- display evi isis local-mac**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}[ evi isis local-mac]{lang="EN-US"}**]{#struct_0_20244_20619_1638799453}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194370701}

[**[display]{lang="EN-US"}[ evi isis local-mac]{lang="EN-US"}**[ { **dynamic** \| **static** } \[ **interface** **tunnel** *interface-number* \[ **vlan** *vlan-id* \] \[ **filtered** \| **passed** \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_20244_20619_x1217437357}

[**[display]{lang="EN-US"}[ evi isis local-mac]{lang="EN-US"}**[ **nonadvertised** \[ **interface** **tunnel** *interface-number* \[ **vlan** *vlan-id* \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_20244_20619_x852819992}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1410550257}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_97256575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_61780078}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1101960340}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x605636960}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1937955547}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1518351119}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194305165}

[**[dynamic]{lang="EN-US"}**]{#struct_0_20244_20619_x124368548}[：显示本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[nonadvertised]{lang="EN-US"}**]{#struct_0_20244_20619_x1342265901}[：显示本地非发布]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。非发布]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址包括：泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[static]{lang="EN-US"}**]{#struct_0_20244_20619_1812994526}[：显示本地静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_1149884008}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。如果不指定本参数，将显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x1476824990}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[filtered]{lang="EN-US"}**]{#struct_0_20244_20619_x852885528}[：只显示本地存在，但是被路由策略过滤掉、不能发布的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[passed]{lang="EN-US"}**]{#struct_0_20244_20619_1788324872}[：只显示没有被路由策略过滤掉、允许发布的本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_20244_20619_x1756618515}[：显示本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1010829604}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1194501773}[显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac dynamic]{lang="EN-US"}]{#struct_0_20244_20619_489566872}

[Process ID: 0]{lang="EN-US"}

[Tunnel interface: Tunnel0]{lang="EN-US"}

[  VLAN ID: 100]{lang="EN-US"}

[    MAC address: 00aa-00bb-00cc]{lang="EN-US"}

[    MAC address: 00aa-00cc-00bb (Filtered)]{lang="EN-US"}

[    MAC address: 00cc-00aa-00bb]{lang="EN-US"}

[  VLAN ID: 50]{lang="EN-US"}

[    MAC address: 00bb-00aa-00cc]{lang="EN-US"}

[    MAC address: 00bb-00cc-00aa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x853344279}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下允许发布的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 passed]{lang="EN-US"}]{#struct_0_20244_20619_x973987901}

[Process ID: 0]{lang="EN-US"}

[Tunnel interface: Tunnel0]{lang="EN-US"}

[  VLAN ID: 100]{lang="EN-US"}

[    MAC address: 00aa-00bb-00cc]{lang="EN-US"}

[    MAC address: 00cc-00aa-00bb]{lang="EN-US"}

[  VLAN ID: 50]{lang="EN-US"}

[    MAC address: 00bb-00aa-00cc]{lang="EN-US"}

[    MAC address: 00bb-00cc-00aa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x724918374}[显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地非发布]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac nonadvertised]{lang="EN-US"}]{#struct_0_20244_20619_1376233105}

[MAC Flags: F-Flooding, B-Blackhole, P-Multiport, M-Multicast]{lang="EN-US"}

[Process ID: 3]{lang="EN-US"}

[  Tunnel interface: Tunnel3]{lang="EN-US"}

[  VLAN ID: 111]{lang="EN-US"}

[    MAC address: 0005-0005-0005]{lang="EN-US"}

[          Flags: F]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1194436237}[显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac static]{lang="EN-US"}]{#struct_0_20244_20619_771107482}

[Process ID: 0]{lang="EN-US"}

[Tunnel interface: Tunnel0]{lang="EN-US"}

[  VLAN ID: 100]{lang="EN-US"}

[    MAC address: 00aa-00bb-00cc]{lang="EN-US"}

[    MAC address: 00aa-00cc-00bb (Filtered)]{lang="EN-US"}

[    MAC address: 00cc-00aa-00bb]{lang="EN-US"}

[  VLAN ID: 50]{lang="EN-US"}

[    MAC address: 00bb-00aa-00cc]{lang="EN-US"}

[    MAC address: 00bb-00cc-00aa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x853409815}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下被路由策略过滤不允许发布的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的本地静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac static interface tunnel 0 filtered]{lang="EN-US"}]{#struct_0_20244_20619_x853475351}

[Process ID: 0]{lang="EN-US"}

[Tunnel interface: Tunnel0]{lang="EN-US"}

[  VLAN ID: 100]{lang="EN-US"}

[    MAC address: 00aa-00cc-00bb (Filtered)]{lang="EN-US"}

[  VLAN ID: 50]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1682488840}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 count]{lang="EN-US"}]{#struct_0_20244_20619_x60829167}

[5 MAC addresses found.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1743869051}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下允许发布的本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac dynamic interface tunnel 0 passed count]{lang="EN-US"}]{#struct_0_20244_20619_x853540887}

[4 MAC addresses found.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_204730994}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下被路由策略过滤不允许发布的本地静态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis local-mac static interface tunnel 0 filtered count]{lang="EN-US"}]{#struct_0_20244_20619_x1545056223}

[1 MAC addresses found.]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ]{lang="EN-US"}[evi isis local-mac]{lang="EN-US"}]{#struct_0_20244_20619_1991337301}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2078406787}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_866307435}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194108557}

[[Process ID]{lang="EN-US"}]{#struct_0_20244_20619_1262968874}

[[进程实例号]{style="font-family:宋体"}]{#struct_0_20244_20619_1137421776}

[[Tunnel interface]{lang="EN-US"}]{#struct_0_20244_20619_x61628423}

[[进程实例对应的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x473848731}[接口]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_x1626120660}

[[进程实例下的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x1194043021}

[[MAC address]{lang="EN-US"}]{#struct_0_20244_20619_835009461}

[[MAC]{lang="EN-US"}]{#struct_0_20244_20619_641100847}[地址]{style="font-family:宋体"}

[[(Filtered)]{lang="EN-US"}]{#struct_0_20244_20619_x853082135}

[[被路由策略过滤掉、不能发布的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1742862224}[地址]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_20244_20619_845450359}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x347545477}[本地非发布]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址标记：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F-Flooding]{lang="EN-US"}]{#struct_0_20244_20619_x228084895}[：泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址（即通过]{style="font-family:宋体"}**[evi selective-flooding mac-address]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[选择性泛洪的]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[B-Blackhole]{lang="EN-US"}]{#struct_0_20244_20619_x1194632844}[：黑洞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P-Multiport]{lang="EN-US"}]{#struct_0_20244_20619_x163084175}[：多端口单播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[M-Multicast]{lang="EN-US"}]{#struct_0_20244_20619_x580455735}[：组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[5 MAC addresses found]{lang="EN-US"}]{#struct_0_20244_20619_x827814925}

[[本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1873727630}[地址的数目，本例中本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目为]{style="font-family:宋体"}[5]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1888154093 .myid}
[]{#_Toc404798347}[]{#struct_0_20244_20619_x1194567308}[]{#_Toc312867795}

**EVI \-- EVI配置命令 \-- display evi isis lsdb**

------------------------------------------------------------------------

[**[display evi isis lsdb]{lang="EN-US"}**]{#struct_0_20244_20619_x1447095731}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的链路状态数据库。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_872877039}

[**[display evi isis lsdb]{lang="EN-US"}**[ \[ **local** \| **lsp-id** *lspid* \| **verbose** \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_1873694046}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x487061715}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1736591200}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_2108142205}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x907792942}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x625080245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1194763916}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_1866232525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x120111806}

[**[local]{lang="EN-US"}**]{#struct_0_20244_20619_156005744}[：显示当前设备产生的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}**[ *lspid*]{lang="EN-US"}]{#struct_0_20244_20619_x726694900}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}[SYSID*.*Pseudonode ID-fragment num]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[SYSID]{lang="EN-US"}[是]{style="font-family:宋体"}[产生该]{style="font-family:宋体"}[LSP]{lang="EN-GB"}[的结点或伪结点的]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[，]{style="font-family:宋体"}[fragment num]{lang="EN-US"}[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_20244_20619_2127179565}[：显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。如果不指定本参数，将显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_520568939}[：显示指定]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的链路状态信息。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的链路状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1739730198}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1194698380}[显示链路状态数据库的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis lsdb]{lang="EN-US"}]{#struct_0_20244_20619_x409467444}

[ ]{lang="EN-US"}

[               Link state database information for EVI-ISIS(0)]{lang="EN-US"}

[LSP ID                 Seq num     Checksum  Holdtime  Length    Overload]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0011.2200.0001.00-00\*  0x000000f3  0xd95e    45        47        0]{lang="EN-US"}

[0011.2200.0101.00-00   0x00000017  0xbb6f    1139      85        0]{lang="EN-US"}

[0011.2200.0101.02-00   0x00000002  0x7973    805       54        0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: \*-Self LSP, +-Self LSP(Extended)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_191123255}[显示链路状态数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis lsdb verbose]{lang="EN-US"}]{#struct_0_20244_20619_x1194370700}

[ ]{lang="EN-US"}

[                Link state database information for EVI-ISIS(1)]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 3822.d69e.ee00.00-00\*]{lang="EN-US"}

[Sequence number: 0x00000001]{lang="EN-US"}

[Checksum: 0xe0b5]{lang="EN-US"}

[Holdtime: 820s]{lang="EN-US"}

[Length: 47]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 3822.d69e.ee00.00]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 3ce5.a600.7600.02, Cost: 16777214]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 3ce5.a600.7600.00-00]{lang="EN-US"}

[Sequence number: 0x00000007]{lang="EN-US"}

[Checksum: 0xc98a]{lang="EN-US"}

[Holdtime: 1163s]{lang="EN-US"}

[Length: 72]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 3ce5.a600.7600.00]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 3ce5.a600.7600.02, Cost: 16777214]{lang="EN-US"}

[MAC addresses:]{lang="EN-US"}

[  VLAN ID: 1   Confidence: 1]{lang="EN-US"}

[    3822-d69e-ef68]{lang="EN-US"}

[    d485-64aa-7f23]{lang="EN-US"}

[    3408-0499-b44c]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSP ID: 3ce5.a600.7600.02-00]{lang="EN-US"}

[Sequence number: 0x00000001]{lang="EN-US"}

[Checksum: 0xe16d]{lang="EN-US"}

[Holdtime: 819s]{lang="EN-US"}

[Length: 54]{lang="EN-US"}

[Overload: 0]{lang="EN-US"}

[Source: 3ce5.a600.7600.02]{lang="EN-US"}

[Neighbour]{lang="EN-US"}

[    ID: 3822.d69e.ee00.00, Cost: 0]{lang="EN-US"}

[    ID: 3ce5.a600.7600.00, Cost: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Flags: \*-Self LSP, +-Self LSP(Extended)]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display evi isis lsdb]{lang="EN-US"}]{#struct_0_20244_20619_x1194305164}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2072362019}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1441715393}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_2128536989}

[[Link state database information for EVI-ISIS(0)]{lang="EN-US"}]{#struct_0_20244_20619_x1228521916}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2098824852}[进程]{style="font-family:宋体"}[0]{lang="EN-US"}[的链路状态数据库信息]{style="font-family:宋体"}

[[LSP ID]{lang="EN-US"}]{#struct_0_20244_20619_x1571248653}

[[链路状态报文]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_1719188207}

[[Seqence number]{lang="EN-US"}]{#struct_0_20244_20619_x1194501772}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_2055650813}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_20244_20619_x26404653}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_1285348355}[校验和]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_20244_20619_864080570}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1194436236}[生存时间，随着时间推移递减]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_20244_20619_x794976459}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_824971194}[长度]{style="font-family:宋体"}

[[Overload]{lang="EN-US"}]{#struct_0_20244_20619_x1443769869}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1940472831}[中]{style="font-family:宋体"}[Overload bit]{lang="EN-US"}[的置位情况。]{style="font-family:宋体"}[1]{lang="EN-US"}[表示置位，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有置位]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_20244_20619_1692569994}

[[LSP]{lang="SV"}]{#struct_0_20244_20619_x1194108556}[生成路由器的]{style="font-family:宋体"}[System ID]{lang="SV"}

[[Neighbour ID]{lang="EN-US"}]{#struct_0_20244_20619_x1465914481}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_1055845023}[生成路由器邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Cost]{lang="EN-US"}]{#struct_0_20244_20619_745069828}

[[开销值]{style="font-family:宋体"}]{#struct_0_20244_20619_x136007883}

[[MAC address]{lang="EN-US"}]{#struct_0_20244_20619_x1194043020}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1893873894}[生成路由器的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_x1134801633}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_1731932825}[生成路由器的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址所在的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}

[[Confidence]{lang="EN-US"}]{#struct_0_20244_20619_x1194632847}

[[可信度]{style="font-family:宋体"}]{#struct_0_20244_20619_240200352}

[[Flags: \*-Self LSP, +-Self LSP(Extended)]{lang="EN-US"}]{#struct_0_20244_20619_x1721195824}

[[带]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_20244_20619_312902686}[号表示是本地生成的、原始系统]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[带]{style="font-family:宋体"}[+]{lang="EN-US"}]{#struct_0_20244_20619_1515602466}[号表示是本地生成的、虚拟系统]{style="font-family:宋体"}[LSP]{lang="EN-US"}[（]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩展分片）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1111785451 .myid}
[]{#_Toc404798348}[]{#struct_0_20244_20619_x1194567311}[]{#_Toc312867797}

**EVI \-- EVI配置命令 \-- display evi isis peer**

------------------------------------------------------------------------

[**[display evi isis peer]{lang="EN-US"}**]{#struct_0_20244_20619_1637952448}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_2039545133}

[**[display]{lang="EN-US"}**[ **evi isis** **peer** \[ *process-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_x445398605}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1408218565}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1795962618}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_116941325}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_556970260}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1194763919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_750487278}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_1060708909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x939938157}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_971278285}[：显示指定的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下的邻居信息。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_2005285296}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1898798647}[显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[0]{lang="EN-US"}[的邻居信息。（此例为无冲突的站点内邻居）]{style="font-family:宋体"}

[[\<Sysname\> display evi isis peer 0]{lang="EN-US"}]{#struct_0_20244_20619_x1194698383}

[Process ID: 0]{lang="EN-US"}

[System ID: 0011.2200.0101]{lang="EN-US"}

[Link interface: Tunnel0]{lang="EN-US"}

[Circuit ID: 0011.2200.0301.01]{lang="EN-US"}

[State: Up]{lang="EN-US"}

[Site ID: 1]{lang="EN-US"}

[Hold time: 29s]{lang="EN-US"}

[Neighbour DED priority: 64]{lang="EN-US"}

[Uptime: 00:10:56]{lang="EN-US"}

[ ]{lang="EN-US"}

[Process ID: 0]{lang="EN-US"}

[System ID: 0011.2200.0101]{lang="EN-US"}

[Link interface: EVI-Link0]{lang="EN-US"}

[Circuit ID: \-\--]{lang="EN-US"}

[State: Init]{lang="EN-US"}

[Site ID: 1]{lang="EN-US"}

[Hold time: 29s]{lang="EN-US"}

[Neighbour DED priority: 64]{lang="EN-US"}

[Uptime: 00:00:58]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x853082138}[显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[0]{lang="EN-US"}[的邻居信息（此例为有冲突的站点间邻居）。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis peer 0]{lang="EN-US"}]{#struct_0_20244_20619_x853147674}

[Process ID: 0]{lang="EN-US"}

[System ID: 0011.2200.0301]{lang="EN-US"}

[Link interface: EVI-Link0]{lang="EN-US"}

[Circuit ID: \-\--]{lang="EN-US"}

[State: Init]{lang="EN-US"}

[Site ID: 1 (Conflict)]{lang="EN-US"}

[Hold time: 27s]{lang="EN-US"}

[Neighbor DED priority: 64]{lang="EN-US"}

[Uptime: 00:00:00]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display evi isis peer]{lang="EN-US"}]{#struct_0_20244_20619_x1975551385}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2071062563}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_2117222185}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1361244364}

[[Process ID]{lang="EN-US"}]{#struct_0_20244_20619_x1194370703}

[[进程实例号]{style="font-family:宋体"}]{#struct_0_20244_20619_1914730525}

[[System ID]{lang="EN-US"}]{#struct_0_20244_20619_394659014}

[[邻居的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_x1959117899}

[[Link interface]{lang="EN-US"}]{#struct_0_20244_20619_382352358}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1258976884}[：与对端相连的本地]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x1194305167}[-]{lang="EN-US"}[link]{lang="EN-US"}[：与对端相连的本地]{lang="EN-US" style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}

[[Circuit ID]{lang="EN-US"}]{#struct_0_20244_20619_x1287167962}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_3114677}

[[State]{lang="EN-US"}]{#struct_0_20244_20619_x1267177021}

[[邻居状态：]{style="font-family:宋体"}]{#struct_0_20244_20619_1680198705}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_20244_20619_x1896426886}[：]{lang="EN-US" style="font-family:宋体"}[邻居初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_20244_20619_x1194501775}[：邻接关系建立]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_20244_20619_x673232542}[：邻接关系断开]{style="font-family:宋体"}

[[Site ID]{lang="EN-US"}]{#struct_0_20244_20619_x853213210}

[[邻居的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_x853082137}[。括号中的]{style="font-family:宋体"}[Conflict]{lang="EN-US"}[表示邻居的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[与本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[有冲突。当站点间邻居的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[与本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[一致、或者站点内邻居的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[与本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[不一致，则认为邻居的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[与本地站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[有冲突]{style="font-family:宋体"}

[[Hold time]{lang="EN-US"}]{#struct_0_20244_20619_126348046}

[[存活时间，随着时间推移递减，如果在存活时间内还没有收到邻居发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_20244_20619_260854598}[报文，则认为邻居已经失效，如果收到了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则存活时间将重置为初始值]{style="font-family:宋体"}

[[Neighbour DED Priority]{lang="EN-US"}]{#struct_0_20244_20619_765812362}

[[邻居接口]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_20244_20619_x1194436239}[优先级]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_20244_20619_x35461572}

[[邻居关系保持的时间]{style="font-family:宋体"}]{#struct_0_20244_20619_x1961907262}

[ ]{lang="EN-US"}

::: {#-679947844 .myid}
[]{#_Toc404798349}[]{#struct_0_20244_20619_x584142666}

**EVI \-- EVI配置命令 \-- display evi isis remote-mac**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}[ evi isis remote-mac]{lang="EN-US"}**]{#struct_0_20244_20619_1277385518}[命令用来显示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_2127729404}

[**[display]{lang="EN-US"}**[ **evi isis** **remote-mac** \[ **interface** **tunnel** *interface-number* \[ **vlan** *vlan-id* \] \[ **count** \] \]]{lang="EN-US"}]{#struct_0_20244_20619_x1194108559}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_812630180}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_962183781}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x431890987}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1382802207}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_1144032564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1154439846}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_910709958}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1194043023}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_x327789953}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。如果不指定本参数，将显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x1629218069}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_20244_20619_x452867688}[：显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2124692776}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_440278170}[显示所有]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis remote-mac]{lang="EN-US"}]{#struct_0_20244_20619_x1194632846}

[Process ID: 0]{lang="EN-US"}

[  Tunnel interface: Tunnel0]{lang="EN-US"}

[  VLAN ID: 3]{lang="EN-US"}

[    MAC address: 0033-0011-0022]{lang="EN-US"}

[      Interface:  EVI-Link0]{lang="EN-US"}

[          Flags:  0x2]{lang="EN-US"}

[  VLAN ID: 2]{lang="EN-US"}

[    MAC address: 0022-0033-0011]{lang="EN-US"}

[      Interface:  EVI-Link0]{lang="EN-US"}

[    MAC address: 0033-0022-0011]{lang="EN-US"}

[      Interface:  EVI-Link0]{lang="EN-US"}

[          Flags:  0x2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1325883589}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[下的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis remote-mac interface tunnel 0 count]{lang="EN-US"}]{#struct_0_20244_20619_737265973}

[3 mac address(es) found.]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display evi isis ]{lang="EN-US"}[remote-mac]{lang="EN-US"}]{#struct_0_20244_20619_x1298661143}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2065466083}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1137971825}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_643211095}

[[Process ID]{lang="EN-US"}]{#struct_0_20244_20619_x1194567310}

[[进程实例号]{style="font-family:宋体"}]{#struct_0_20244_20619_x1090930907}

[[Tunnel interface]{lang="EN-US"}]{#struct_0_20244_20619_x1037809712}

[[进程实例对应的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1976137749}[接口]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_x1775948858}

[[进程实例下的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x231749960}

[[MAC address]{lang="EN-US"}]{#struct_0_20244_20619_x836889871}

[[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1194763918}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_x1978396077}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_104064347}[链路索引]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_20244_20619_x320483598}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x26386640}[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址标记：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x1]{lang="EN-US"}]{#struct_0_20244_20619_x1194698382}[：该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[本地动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址冲突]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x2]{lang="EN-US"}]{#struct_0_20244_20619_753331970}[：该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址已经下发到远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0x4]{lang="EN-US"}]{#struct_0_20244_20619_993405808}[：该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址与]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[本地的静态或泛洪]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址冲突]{style="font-family:宋体"}

[[3 mac address(es) found]{lang="EN-US"}]{#struct_0_20244_20619_1645991811}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_963622728}[地址的数目，本例中远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的数目为]{style="font-family:宋体"}[3]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#114951646 .myid}
[]{#_Toc404798350}[]{#struct_0_20244_20619_1638126875}[]{#_Toc312867798}[]{#_Toc338171761}[]{#_Toc338432177}[]{#_Toc338171762}[]{#_Toc338432178}[]{#_Toc338171763}[]{#_Toc338432179}[]{#_Toc338171764}[]{#_Toc338432180}[]{#_Toc338171765}[]{#_Toc338432181}[]{#_Toc338171766}[]{#_Toc338432182}[]{#_Toc338171767}[]{#_Toc338432183}[]{#_Toc338171768}[]{#_Toc338432184}[]{#_Toc338171769}[]{#_Toc338432185}[]{#_Toc338171770}[]{#_Toc338432186}[]{#_Toc338171771}[]{#_Toc338432187}[]{#_Toc338171772}[]{#_Toc338432188}[]{#_Toc338171773}[]{#_Toc338432189}[]{#_Toc338171774}[]{#_Toc338432190}[]{#_Toc338171775}[]{#_Toc338432191}[]{#_Toc338171776}[]{#_Toc338432192}[]{#_Toc338171777}[]{#_Toc338432193}[]{#_Toc338171778}[]{#_Toc338432194}[]{#_Toc338171779}[]{#_Toc338432195}[]{#_Toc338171780}[]{#_Toc338432196}[]{#_Toc338171781}[]{#_Toc338432197}[]{#_Toc338171782}[]{#_Toc338432198}[]{#_Toc338171783}[]{#_Toc338432199}[]{#_Toc338171784}[]{#_Toc338432200}[]{#_Toc338171785}[]{#_Toc338432201}[]{#_Toc338171786}[]{#_Toc338432202}[]{#_Toc338171787}[]{#_Toc338432203}[]{#_Toc338171788}[]{#_Toc338432204}[]{#_Toc338171789}[]{#_Toc338432205}[]{#_Toc338171790}[]{#_Toc338432206}[]{#_Toc338171791}[]{#_Toc338432207}[]{#_Toc338171792}[]{#_Toc338432208}[]{#_Toc338171793}[]{#_Toc338432209}[]{#_Toc338171794}[]{#_Toc338432210}[]{#_Toc338171795}[]{#_Toc338432211}[]{#_Toc338171796}[]{#_Toc338432212}[]{#_Toc338171797}[]{#_Toc338432213}[]{#_Toc338171798}[]{#_Toc338432214}[]{#_Toc338171799}[]{#_Toc338432215}[]{#_Toc338171800}[]{#_Toc338432216}[]{#_Toc338171801}[]{#_Toc338432217}[]{#_Toc338171802}[]{#_Toc338432218}[]{#_Toc338171803}[]{#_Toc338432219}[]{#_Toc338171804}[]{#_Toc338432220}[]{#_Toc338171805}[]{#_Toc338432221}[]{#_Toc338171806}[]{#_Toc338432222}[]{#_Toc338171807}[]{#_Toc338432223}[]{#_Toc338171808}[]{#_Toc338432224}[]{#_Toc338171809}[]{#_Toc338432225}[]{#_Toc338171810}[]{#_Toc338432226}[]{#_Toc338171811}[]{#_Toc338432227}[]{#_Toc338171812}[]{#_Toc338432228}[]{#_Toc338171813}[]{#_Toc338432229}[]{#_Toc338171814}[]{#_Toc338432230}[]{#_Toc338171815}[]{#_Toc338432231}[]{#_Toc338171816}[]{#_Toc338432232}[]{#_Toc338171817}[]{#_Toc338432233}[]{#_Toc338171818}[]{#_Toc338432234}[]{#_Toc338171819}[]{#_Toc338432235}[]{#_Toc338171820}[]{#_Toc338432236}[]{#_Toc338171821}[]{#_Toc338432237}[]{#_Toc338171822}[]{#_Toc338432238}[]{#_Toc338171823}[]{#_Toc338432239}[]{#_Toc338171824}[]{#_Toc338432240}[]{#_Toc338171825}[]{#_Toc338432241}[]{#_Toc338171826}[]{#_Toc338432242}[]{#_Toc338171827}[]{#_Toc338432243}[]{#_Toc338171828}[]{#_Toc338432244}[]{#_Toc338171829}[]{#_Toc338432245}[]{#_Toc338171830}[]{#_Toc338432246}[]{#_Toc338171831}[]{#_Toc338432247}[]{#_Toc338171832}[]{#_Toc338432248}[]{#_Toc338171833}[]{#_Toc338432249}[]{#_Toc338171834}[]{#_Toc338432250}[]{#_Toc338171835}[]{#_Toc338432251}[]{#_Toc338171836}[]{#_Toc338432252}[]{#_Toc338171837}[]{#_Toc338432253}[]{#_Toc338171838}[]{#_Toc338432254}[]{#_Toc338171839}[]{#_Toc338432255}[]{#_Toc338171840}[]{#_Toc338432256}[]{#_Toc338171841}[]{#_Toc338432257}[]{#_Toc338171842}[]{#_Toc338432258}[]{#_Toc338171843}[]{#_Toc338432259}[]{#_Toc338171844}[]{#_Toc338432260}[]{#_Toc338171845}[]{#_Toc338432261}[]{#_Toc338171846}[]{#_Toc338432262}[]{#_Toc338171847}[]{#_Toc338432263}[]{#_Toc338171848}[]{#_Toc338432264}[]{#_Toc338171849}[]{#_Toc338432265}[]{#_Toc338171850}[]{#_Toc338432266}[]{#_Toc338171851}[]{#_Toc338432267}[]{#_Toc338171852}[]{#_Toc338432268}[]{#_Toc338171853}[]{#_Toc338432269}[]{#_Toc338171854}[]{#_Toc338432270}[]{#_Toc338171855}[]{#_Toc338432271}[]{#_Toc338171889}[]{#_Toc338432305}[]{#_Toc303068831}[]{#_Toc303068832}[]{#_Toc338171890}[]{#_Toc338432306}[]{#_Toc338171891}[]{#_Toc338432307}[]{#_Toc338171892}[]{#_Toc338432308}[]{#_Toc338171893}[]{#_Toc338432309}[]{#_Toc338171894}[]{#_Toc338432310}[]{#_Toc338171895}[]{#_Toc338432311}[]{#_Toc338171896}[]{#_Toc338432312}[]{#_Toc338171897}[]{#_Toc338432313}[]{#_Toc338171898}[]{#_Toc338432314}[]{#_Toc338171899}[]{#_Toc338432315}[]{#_Toc338171900}[]{#_Toc338432316}[]{#_Toc338171901}[]{#_Toc338432317}[]{#_Toc338171902}[]{#_Toc338432318}[]{#_Toc338171903}[]{#_Toc338432319}[]{#_Toc338171904}[]{#_Toc338432320}[]{#_Toc338171905}[]{#_Toc338432321}[]{#_Toc338171906}[]{#_Toc338432322}[]{#_Toc338171907}[]{#_Toc338432323}[]{#_Toc338171908}[]{#_Toc338432324}[]{#_Toc338171909}[]{#_Toc338432325}[]{#_Toc338171910}[]{#_Toc338432326}[]{#_Toc338171911}[]{#_Toc338432327}[]{#_Toc338171941}[]{#_Toc338432357}[]{#_Toc338171942}[]{#_Toc338432358}[]{#_Toc338171943}[]{#_Toc338432359}[]{#_Toc338171944}[]{#_Toc338432360}[]{#_Toc338171945}[]{#_Toc338432361}[]{#_Toc338171946}[]{#_Toc338432362}[]{#_Toc338171947}[]{#_Toc338432363}[]{#_Toc338171948}[]{#_Toc338432364}[]{#_Toc338171949}[]{#_Toc338432365}[]{#_Toc338171950}[]{#_Toc338432366}[]{#_Toc338171951}[]{#_Toc338432367}[]{#_Toc338171952}[]{#_Toc338432368}[]{#_Toc338171953}[]{#_Toc338432369}[]{#_Toc338171954}[]{#_Toc338432370}[]{#_Toc338171955}[]{#_Toc338432371}[]{#_Toc338171956}[]{#_Toc338432372}[]{#_Toc338171957}[]{#_Toc338432373}[]{#_Toc338171958}[]{#_Toc338432374}[]{#_Toc338171959}[]{#_Toc338432375}[]{#_Toc338171960}[]{#_Toc338432376}[]{#_Toc338171961}[]{#_Toc338432377}[]{#_Toc338171962}[]{#_Toc338432378}[]{#_Toc338171963}[]{#_Toc338432379}[]{#_Toc338171964}[]{#_Toc338432380}[]{#_Toc338171965}[]{#_Toc338432381}[]{#_Toc338171966}[]{#_Toc338432382}[]{#_Toc338171967}[]{#_Toc338432383}[]{#_Toc338171968}[]{#_Toc338432384}[]{#_Toc338171969}[]{#_Toc338432385}[]{#_Toc338171970}[]{#_Toc338432386}[]{#_Toc338171971}[]{#_Toc338432387}[]{#_Toc338171972}[]{#_Toc338432388}[]{#_Toc338171973}[]{#_Toc338432389}[]{#_Toc338171974}[]{#_Toc338432390}[]{#_Toc338171975}[]{#_Toc338432391}[]{#_Toc338171976}[]{#_Toc338432392}[]{#_Toc338171977}[]{#_Toc338432393}[]{#_Toc338171978}[]{#_Toc338432394}[]{#_Toc338171979}[]{#_Toc338432395}[]{#_Toc338171980}[]{#_Toc338432396}[]{#_Toc338171981}[]{#_Toc338432397}[]{#_Toc338171982}[]{#_Toc338432398}[]{#_Toc338171983}[]{#_Toc338432399}[]{#_Toc338171984}[]{#_Toc338432400}[]{#_Toc338171985}[]{#_Toc338432401}[]{#_Toc338171986}[]{#_Toc338432402}[]{#_Toc338171987}[]{#_Toc338432403}[]{#_Toc338171988}[]{#_Toc338432404}[]{#_Toc338171989}[]{#_Toc338432405}[]{#_Toc338171990}[]{#_Toc338432406}[]{#_Toc338171991}[]{#_Toc338432407}[]{#_Toc338171992}[]{#_Toc338432408}[]{#_Toc338171993}[]{#_Toc338432409}[]{#_Toc338171994}[]{#_Toc338432410}[]{#_Toc338171995}[]{#_Toc338432411}[]{#_Toc338171996}[]{#_Toc338432412}[]{#_Toc338171997}[]{#_Toc338432413}[]{#_Toc338171998}[]{#_Toc338432414}[]{#_Toc338171999}[]{#_Toc338432415}[]{#_Toc338172000}[]{#_Toc338432416}[]{#_Toc338172001}[]{#_Toc338432417}[]{#_Toc338172002}[]{#_Toc338432418}[]{#_Toc338172003}[]{#_Toc338432419}[]{#_Toc338172004}[]{#_Toc338432420}[]{#_Toc338172005}[]{#_Toc338432421}[]{#_Toc338172006}[]{#_Toc338432422}[]{#_Toc338172007}[]{#_Toc338432423}[]{#_Toc338172008}[]{#_Toc338432424}[]{#_Toc338172009}[]{#_Toc338432425}[]{#_Toc338172010}[]{#_Toc338432426}[]{#_Toc338172011}[]{#_Toc338432427}[]{#_Toc338172012}[]{#_Toc338432428}[]{#_Toc338172013}[]{#_Toc338432429}[]{#_Toc338172038}[]{#_Toc338432454}[]{#_Toc338172039}[]{#_Toc338432455}[]{#_Toc338172040}[]{#_Toc338432456}[]{#_Toc338172041}[]{#_Toc338432457}[]{#_Toc338172042}[]{#_Toc338432458}[]{#_Toc338172043}[]{#_Toc338432459}[]{#_Toc338172044}[]{#_Toc338432460}[]{#_Toc338172045}[]{#_Toc338432461}[]{#_Toc338172046}[]{#_Toc338432462}[]{#_Toc338172047}[]{#_Toc338432463}[]{#_Toc338172048}[]{#_Toc338432464}[]{#_Toc338172049}[]{#_Toc338432465}[]{#_Toc338172050}[]{#_Toc338432466}[]{#_Toc338172051}[]{#_Toc338432467}[]{#_Toc338172052}[]{#_Toc338432468}[]{#_Toc338172053}[]{#_Toc338432469}[]{#_Toc338172054}[]{#_Toc338432470}[]{#_Toc338172055}[]{#_Toc338432471}[]{#_Toc338172056}[]{#_Toc338432472}[]{#_Toc338172057}[]{#_Toc338432473}[]{#_Toc338172058}[]{#_Toc338432474}[]{#_Toc338172059}[]{#_Toc338432475}[]{#_Toc338172078}[]{#_Toc338432494}[]{#_Toc338172079}[]{#_Toc338432495}[]{#_Toc338172080}[]{#_Toc338432496}[]{#_Toc338172081}[]{#_Toc338432497}

**EVI \-- EVI配置命令 \-- display evi isis tunnel**

------------------------------------------------------------------------

[**[display evi isis tunnel]{lang="EN-US"}**]{#struct_0_20244_20619_x1194370702}[命令用来显示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_348646584}

[**[display evi isis tunnel]{lang="EN-US"}**[ \[ *tunnel-number* \]]{lang="EN-US"}]{#struct_0_20244_20619_1757984383}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_409096581}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_1363976241}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1884156341}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x168427618}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_578310528}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1498370723}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1194305166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_278915979}

[*[tunnel-number]{lang="EN-US"}*]{#struct_0_20244_20619_x1101055397}[：显示指定]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[信息。如果不指定本参数，将显示所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1007801246}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1694714494}[显示]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{style="font-family:宋体"}[101]{lang="EN-US"}[上的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi isis tunnel 101]{lang="EN-US"}]{#struct_0_20244_20619_x1194501774}

[Tunnel101]{lang="EN-US"}

[MTU: 1400]{lang="EN-US"}

[DED: Yes]{lang="EN-US"}

[DED priority: 80]{lang="EN-US"}

[Hello timer: 10s]{lang="EN-US"}

[Hello multiplier: 3]{lang="EN-US"}

[CSNP timer: 10s]{lang="EN-US"}

[LSP timer: 100ms]{lang="EN-US"}

[LSP transmit-throttle count: 5]{lang="EN-US"}

[AEF: Yes]{lang="EN-US"}

[EVI-Link0    DED: Yes]{lang="EN-US"}

[LAV:]{lang="EN-US"}

[  1,50,100]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ]{lang="EN-US"}[evi isis]{lang="EN-US"}]{#struct_0_20244_20619_892851399}[ tunnel]{lang="EN-US"}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2065712771}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_30059244}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x833165744}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x703554811}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_651609005}[隧道接口编号]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_20244_20619_1043982242}

[[链路]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_20244_20619_x1620878979}[值]{style="font-family:宋体"}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_x1194436238}

[[是否被选举为]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_20244_20619_x1601545513}[：]{style="font-family:宋体"}[Yes]{lang="EN-US"}[表示是；]{style="font-family:宋体"}[No]{lang="EN-US"}[表示否]{style="font-family:宋体"}

[[DED priority]{lang="EN-US"}]{#struct_0_20244_20619_1958841418}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_x1619677331}[优先级]{style="font-family:宋体"}

[[Hello timer]{lang="EN-US"}]{#struct_0_20244_20619_1104284401}

[[Hello]{lang="EN-US"}]{#struct_0_20244_20619_x1194108558}[报文发送时间间隔]{style="font-family:宋体"}

[[Hello multiplier]{lang="EN-US"}]{#struct_0_20244_20619_x1916253175}

[[Hello]{lang="EN-US"}]{#struct_0_20244_20619_1531044281}[报文失效数目]{style="font-family:宋体"}

[[CSNP timer]{lang="EN-US"}]{#struct_0_20244_20619_x1169603930}

[[CSNP]{lang="EN-US"}]{#struct_0_20244_20619_x1531372489}[报文发送时间间隔]{style="font-family:宋体"}

[[LSP timer]{lang="EN-US"}]{#struct_0_20244_20619_326296371}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1194043022}[的最小发送时间间隔]{style="font-family:宋体"}

[[LSP transmit-throttle count]{lang="EN-US"}]{#struct_0_20244_20619_1238293988}

[[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x276985360}[的最大传输数量]{style="font-family:宋体"}

[[AEF]{lang="EN-US"}]{#struct_0_20244_20619_712674127}

[[本设备是否可以作为扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_712608591}[的授权转发设备。如果双归属站点内某设备核心侧故障，其该属性显示为]{style="font-family:宋体"}[No]{lang="EN-US"}[，表示本设备不能作为任何]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的授权转发设备；如果某设备核心侧正常，其该属性显示为]{style="font-family:宋体"}[Yes]{lang="EN-US"}[，表示本设备可以作为扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的授权转发设备]{style="font-family:宋体"}

[[EVI-link]{lang="EN-US"}]{#struct_0_20244_20619_x1422434129}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_727681458}[虚拟链接]{style="font-family:宋体"}

[[LAV]{lang="EN-US"}]{#struct_0_20244_20619_1705111277}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1053910934}[接口下的激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1469832405 .myid}
[]{#_Toc404798351}[]{#struct_0_20244_20619_x991531227}[]{#_Toc302983407}[]{#_Toc303068837}[]{#_Toc302983408}[]{#_Toc303068838}

**EVI \-- EVI配置命令 \-- display evi link**

------------------------------------------------------------------------

[**[display evi link]{lang="EN-US"}**]{#struct_0_20244_20619_2042278249}[命令用来显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道创建的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x118170649}

[**[display evi link interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_792908310}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1078167509}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_727746994}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1749221670}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1515407179}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_1114281023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1661955894}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1034957704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x14630997}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_x920245657}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1292721440}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_727550386}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[创建的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_20244_20619_x2010214529}[display evi link interface tunnel 0]{lang="IT"}

[Interface     Status Source          Destination]{lang="IT"}

[EVI]{lang="EN-US"}[-Link0     UP     1.1.1.1         1.1.2.1]{lang="IT"}

[EVI]{lang="EN-US"}[-Link1     UP     1.1.1.1         1.1.3.1]{lang="IT"}

[[表1-9 ]{lang="EN-US"}[display evi link]{lang="EN-US"}]{#struct_0_20244_20619_1827071448}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2096729987}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_x1080776577}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x532804456}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_1453002919}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_224803802}[接口名]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_20244_20619_508156975}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_727615922}[接口的链路]{style="font-family:宋体"}[UP/DOWN]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_20244_20619_x2140274191}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x291282839}[接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道本端地址]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_20244_20619_1245002826}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_1669946018}[接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道对端地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1900788069 .myid}
[]{#_Toc404798352}[]{#struct_0_20244_20619_x433648059}

**EVI \-- EVI配置命令 \-- display evi mac-address**

------------------------------------------------------------------------

[**[display evi mac-address]{lang="EN-US"}**]{#struct_0_20244_20619_1606780848}[命令用来显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_727943602}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_20244_20619_1150998077}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_316983493}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ **mac-address** *mac-address* **vlan** *vlan-id*]{lang="EN-US"}]{#struct_0_20244_20619_2098535499}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20244_20619_x755586537}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_125253320}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ **mac-address** *mac-address* **vlan** *vlan-id* \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20244_20619_1107871389}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_20244_20619_829790085}[模式：]{style="font-family:宋体"}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ \[ **vlan** *vlan-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **count** \]]{lang="EN-US"}]{#struct_0_20244_20619_1988588384}

[**[display evi mac-address interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*[ **mac-address** *mac-address* **vlan** *vlan-id* \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_20244_20619_1018548735}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_728009138}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x2056990065}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x483312900}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_2037209939}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1119012716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1363008797}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_1289727723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_931321060}

[**[interface]{lang="EN-US"}[ tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_1834820335}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_20244_20619_727812530}[：显示指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x1570539213}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_x558979853}[：显示指定]{style="font-family:宋体"}[单板的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_263136037}[：显示指定成员设备的]{style="font-family:宋体"}[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_x1618785540}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，将显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_x1114503179}[：显示指定成员设备上指定单板的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位]{style="font-family:宋体"}[号。]{style="font-family:宋体"}[如果不指定本参数，]{style="font-family:宋体"}[将显示全局主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="FR"}[地址信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_20244_20619_x671118500}[：显示指定单板的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[chassis]{lang="EN-US"}[-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，将显示全局主用主控板上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu ]{lang="EN-US"}***[cpu-number]{lang="EN-US"}*]{#struct_0_20244_20619_1252821830}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_20244_20619_x1556430688}[：显示远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息的数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_185443184}

[[\# ]{lang="FR"}]{#struct_0_20244_20619_1262596078}[显示]{style="font-family:宋体"}[EVI]{lang="FR"}[隧道接口]{style="font-family:
宋体"}[Tunnel101]{lang="FR"}[下的远端]{style="font-family:宋体"}[MAC]{lang="FR"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi mac-address interface tunnel 101]{lang="FR"}]{#struct_0_20244_20619_x2092757306}

[MAC Address      VLAN ID   Port]{lang="EN-US"}

[000f-e201-0101   1         EVI-link1]{lang="EN-US"}

[000f-e202-0101   2         EVI-link1, EVI-link2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_727878066}[显示]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下的远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息的数目。]{style="font-family:宋体"}

[[\<Sysname\> display evi mac-address interface tunnel 101 count]{lang="EN-US"}]{#struct_0_20244_20619_2759350}

[Total entries: 2]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display evi mac-address]{lang="EN-US"}]{#struct_0_20244_20619_x1751640848}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2090232835}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_611960388}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_368674977}

[[MAC Address]{lang="EN-US"}]{#struct_0_20244_20619_x342212902}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1554831498}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_310747952}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_728205746}[地址所属]{style="font-family:宋体"}[VLAN]{lang="EN-US"}

[[Port]{lang="EN-US"}]{#struct_0_20244_20619_956218303}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x2043621498}[地址对应的出端口（]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示出端口无效，已被删除）]{style="font-family:宋体"}

[[Total entries]{lang="EN-US"}]{#struct_0_20244_20619_680473368}

[[远端]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1860005701}[地址信息的数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1709292840 .myid}
[]{#_Toc404798353}[]{#struct_0_20244_20619_x777452150}[]{#_Toc302983411}[]{#_Toc303068841}[]{#_Toc302983412}[]{#_Toc303068842}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client member**

------------------------------------------------------------------------

[**[display evi neighbor-discovery client member]{lang="EN-US"}**]{#struct_0_20244_20619_x327881799}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_728271282}

[**[display evi neighbor-discovery]{lang="EN-US"}**[ \[ **ipv6** \] **client** **member** \[ **interface tunnel** *interface-number* \| **local** *local-ip* ]{lang="EN-US"}]{#struct_0_20244_20619_x559320081}[｜]{style="font-family:宋体"} **[remote ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*[ \| **server** *server-ip* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1888416319}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1558224861}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1406487248}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1967301873}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_1806580939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1579361094}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1114455931}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_160723275}

[**[ipv6]{lang="EN-US"}**]{#struct_0_20244_20619_727681459}[：显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居信息。不指定本参数，则显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_1705111276}[：显示通过指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口学到的邻居信息。]{style="font-family:宋体"}

[**[local ]{lang="EN-US"}***[local-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x1053845398}[：显示通过指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址对应的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口学到的邻居信息。]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[表示本地]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[remote ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*]{#struct_0_20244_20619_1604685284}[：显示设备学到的指定邻居]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[client-ip]{lang="EN-US"}*[表示邻居]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[server ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x84776266}[：显示通过指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的邻居信息。]{style="font-family:宋体"}*[server-ip]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1346951111}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_136069219}[学到的邻居信息，包括邻居的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址、桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、创建时间、老化时间、邻居之间的]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}[状态等信息。]{style="font-family:宋体"}

[[如果不指定任何参数，将显示设备上本地]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_1733901511}[学到的所有邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_882155351}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_727746995}[显示设备上]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery client member]{lang="EN-US"}]{#struct_0_20244_20619_1749221669}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[Local Address: 20.0.0.2]{lang="EN-US"}

[Server Address: 20.0.1.1]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status ]{lang="EN-US"}

[20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    13        Up ]{lang="EN-US"}

[20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    12        Up ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[Local Address: 20.0.0.2]{lang="EN-US"}

[Server Address: 20.0.1.2]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status ]{lang="EN-US"}

[20.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up ]{lang="EN-US"}

[20.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Up ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2]{lang="EN-US"}

[Local Address: 21.0.0.1]{lang="EN-US"}

[Server Address: 21.0.1.2]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[21.0.2.1        000F-0000-0A3E    2011/01/01 12:12:12    25        Up ]{lang="EN-US"}

[21.0.3.1        000F-0000-0A3F    2011/01/01 12:12:12    19        Down ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel2    Network ID: 3]{lang="EN-US"}

[Local Address: 21.0.0.2]{lang="EN-US"}

[Server Address: NA]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[21.0.2.1        NA                2011/01/01 12:12:12    25        Up ]{lang="EN-US"}

[21.0.3.1        NA                2011/01/01 12:12:12    19        Up ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1514817356}[显示设备上]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery ipv6 client member]{lang="EN-US"}]{#struct_0_20244_20619_727550387}

[Interface: Tunnel0    Network ID: 1                                    ]{lang="EN-US"}

[Local Address: 2000::2                                                 ]{lang="EN-US"}

[Server Address: 2000::1:1                                              ]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[2000::2:1       000F-0000-0A3E    2011/01/01 12:12:12    13        Up  ]{lang="EN-US"}

[2000::3:1       000F-0000-0A3F    2011/01/01 12:12:12    12        Up  ]{lang="EN-US"}

[                                                                       ]{lang="EN-US"}

[Interface: Tunnel0    Network ID: 1                                    ]{lang="EN-US"}

[Local Address: 2000::2                                                 ]{lang="EN-US"}

[Server Address: 2000::1:2                                              ]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[2000::2:1       000F-0000-0A3E    2011/01/01 12:12:12    25        Up  ]{lang="EN-US"}

[2000::3:1       000F-0000-0A3F    2011/01/01 12:12:12    19        Up  ]{lang="EN-US"}

[                                                                       ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2                                    ]{lang="EN-US"}

[Local Address: 2001::1                                                 ]{lang="EN-US"}

[Server Address: 2001::1:1                                              ]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[2001::2:1       000F-0000-0A3E    2011/01/01 12:12:12    25        Up  ]{lang="EN-US"}

[2001::3:1       000F-0000-0A3F    2011/01/01 12:12:12    19        Down]{lang="EN-US"}

[                                                                       ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2                                    ]{lang="EN-US"}

[Local Address: 2002::2                                                 ]{lang="EN-US"}

[Server Address: NA                                                     ]{lang="EN-US"}

[Neighbor        System ID         Created Time           Expire    Status]{lang="EN-US"}

[2002::1         NA                2011/01/01 12:12:12    25        Up  ]{lang="EN-US"}

[2002::3:1       NA                2011/01/01 12:12:12    19        Up  ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display evi neighbor-discovery client member]{lang="EN-US"}]{#struct_0_20244_20619_x2010214528}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2092264163}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_727615923}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x2140274190}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_x1857366780}

[[启动]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x1199436146}[功能的接口名称]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_x795172967}

[[配置的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_x1053934487}

[[Local Address]{lang="EN-US"}]{#struct_0_20244_20619_1484575685}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_727943603}[隧道接口的源端地址]{style="font-family:宋体"}

[[Server Address]{lang="EN-US"}]{#struct_0_20244_20619_1150998076}

[[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_317049029}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[未知]{style="font-family:宋体"}

[[Neighbor]{lang="EN-US"}]{#struct_0_20244_20619_x703189760}

[[通过]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_1014434383}[学到的邻居]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_20244_20619_1274599189}

[[邻居的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_728009139}[地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址未知]{style="font-family:宋体"}

[[Created Time]{lang="EN-US"}]{#struct_0_20244_20619_x2056990066}

[[邻居创建的时间]{style="font-family:宋体"}]{#struct_0_20244_20619_1082771041}

[[Expire ]{lang="EN-US"}]{#struct_0_20244_20619_695528368}

[[邻居的老化时间，单位为秒]{style="font-family:宋体"}]{#struct_0_20244_20619_x925128319}

[[Status]{lang="EN-US"}]{#struct_0_20244_20619_x817715794}

[[与邻居之间]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}]{#struct_0_20244_20619_727812531}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_20244_20619_x1570539212}[：表示可以通过]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}[进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_20244_20619_1007104088}[：表示不可以通过]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}[进行传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NA]{lang="EN-US"}]{#struct_0_20244_20619_x927992273}[：表示尚未创建]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1953980108 .myid}
[]{#_Toc404798354}[]{#struct_0_20244_20619_1845095150}[]{#_Toc303068844}[]{#_Toc303068845}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client statistics**

------------------------------------------------------------------------

[**[display evi neighbor-discovery client statistics]{lang="EN-US"}**]{#struct_0_20244_20619_x1206786552}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_727878067}

[**[display evi neighbor-discovery client statistics interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_2759351}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x185556907}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_398142977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1557381320}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_553661267}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1206194667}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1498593533}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_2091842104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_728205747}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_956218302}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口对应的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2043621497}

[[通过本命令可以查看使能]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x1241840933}[功能后，接口收到和发送]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_336408322}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2015450855}[显示]{style="font-family:宋体"}[IPv4 EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery client statistics interface tunnel 0]{lang="EN-US"}]{#struct_0_20244_20619_728271283}

[Server Address: 10.0.0.1]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        170              Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     170              Purge:      0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server Address: 10.0.0.2]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        99               Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     100              Purge:      0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x559320080}[显示]{style="font-family:宋体"}[IPv6 EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery client statistics interface tunnel 1]{lang="EN-US"}]{#struct_0_20244_20619_1888350783}

[Server Address: 2000::1:1]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        170              Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     170              Purge:      13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server Address: 2000::1:2]{lang="EN-US"}

[Received packets:]{lang="EN-US"}

[  Reply:        99               Error:      1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Register:     100              Purge:      0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display evi neighbor-discovery client statistics]{lang="EN-US"}]{#struct_0_20244_20619_800225165}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2086527811}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_2059252301}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x750440680}

[[Server Address]{lang="EN-US"}]{#struct_0_20244_20619_727681456}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_1705111287}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Received packets]{lang="EN-US"}]{#struct_0_20244_20619_x1053910947}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x588050092}[收到的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_20244_20619_x1377614850}[：表示注册应答报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_20244_20619_1772636527}[：]{style="font-family:宋体"}[表示错误指示报文]{lang="EN-US" style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_20244_20619_298381412}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_727746992}[发送的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_20244_20619_1749221672}[：]{style="font-family:宋体"}[表示注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Purge]{lang="EN-US"}]{#struct_0_20244_20619_x1515538251}[：]{style="font-family:宋体"}[表示注销报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1866244963 .myid}
[]{#_Toc404798355}[]{#struct_0_20244_20619_x50831699}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery client summary**

------------------------------------------------------------------------

[**[display evi neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_20244_20619_1091230285}[命令用来在]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_178084071}

[**[display evi neighbor-discovery]{lang="EN-US"}**[ \[ **ipv6** \] **client summary**]{lang="EN-US"}]{#struct_0_20244_20619_x1744341398}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1943163445}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_727550384}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2010214531}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1470775552}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_798921340}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_987293967}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_1503279752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1146371491}

[**[ipv6]{lang="EN-US"}**]{#struct_0_20244_20619_x1328695155}[：显示]{style="font-family:宋体"}[IPv6 ENDC]{lang="EN-US"}[的运行信息。不指定本参数，则显示]{style="font-family:宋体"}[IPv4 ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_719965693}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_1332946744}[的运行信息，包括]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的配置信息、]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[与]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的连接状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_727615920}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2140274193}[显示]{style="font-family:宋体"}[IPv4 ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery client summary]{lang="EN-US"}]{#struct_0_20244_20619_x1454082253}

[                         Status: I-Init  E-Establish  P-Probe]{lang="EN-US"}

[Interface    Local Address   Server Address  Network ID  Reg  Auth      Status ]{lang="EN-US"}

[Tunnel0      20.0.0.2        20.0.0.1        1           15   enabled   E      ]{lang="EN-US"}

[Tunnel0      20.0.0.2        20.0.0.3        1           15   enabled   P      ]{lang="EN-US"}

[Tunnel1      21.0.0.2        21.0.0.1        2           15   disabled  P  ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1639495161}[显示]{style="font-family:宋体"}[IPv6 ENDC]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery ipv6 client summary]{lang="EN-US"}]{#struct_0_20244_20619_x881930867}

[                         Status: I-Init  E-Establish  P-Probe]{lang="EN-US"}

[Interface    Local Address   Server Address  Network ID  Reg  Auth      Status]{lang="EN-US"}

[Tunnel0      2000::1:1       2000::2:1       1           15   enabled   E     ]{lang="EN-US"}

[Tunnel0      2000::1:1       2000::3:1       1           15   enabled   P     ]{lang="EN-US"}

[Tunnel1      2001::1:2       2001::1:1       2           15   disabled  P      ]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display evi neighbor-discovery client summary]{lang="EN-US"}]{#struct_0_20244_20619_1761101129}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2088078083}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_727943600}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_1150998079}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_317114565}

[[启动]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x311653828}[功能的接口名称]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_20244_20619_65697036}

[[本地]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x410083084}[隧道接口的源端地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Server Address]{lang="EN-US"}]{#struct_0_20244_20619_852456416}

[[配置的远端]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_728009136}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_x2056990071}

[[配置的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_1842351464}[，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Reg]{lang="EN-US"}]{#struct_0_20244_20619_1615313042}

[[注册时间间隔]{style="font-family:宋体"}]{#struct_0_20244_20619_2050991994}

[[Auth]{lang="EN-US"}]{#struct_0_20244_20619_x1745313117}

[[是否使能认证功能：]{style="font-family:宋体"}]{#struct_0_20244_20619_x429955438}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_20244_20619_727812528}[：]{style="font-family:宋体"}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_20244_20619_385775931}[：]{style="font-family:宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_20244_20619_1474645232}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x615476589}[与]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的连接状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_20244_20619_1249164250}[：表示初始状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_20244_20619_727878064}[：表示已建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_20244_20619_2759352}[：表示未建立连接正在探测]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1380527034}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_20244_20619_1248384159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_20244_20619_144798090}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_20244_20619_x637975889}

::: {#-1612608302 .myid}
[]{#_Toc404798356}[]{#struct_0_20244_20619_x1879335944}[]{#_Toc302983416}[]{#_Toc303068848}[]{#_Toc302983419}[]{#_Toc303068851}[]{#_Toc302983420}[]{#_Toc303068852}[]{#_Toc302983421}[]{#_Toc303068853}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server member**

------------------------------------------------------------------------

[**[display evi neighbor-discovery server member]{lang="EN-US"}**]{#struct_0_20244_20619_1488883997}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的成员信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x55180842}

[**[display evi neighbor-discovery ]{lang="EN-US"}**[\[ **ipv6** \] **server member** \[ **interface tunnel** *interface-number* \| **local** *local-ip* \| **remote** *client-ip* \]]{lang="EN-US"}]{#struct_0_20244_20619_728205744}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_956218305}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x2043621496}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1487042422}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1391693374}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x2125596013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_566721095}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1043578106}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1506436986}

[**[ipv6]{lang="EN-US"}**]{#struct_0_20244_20619_x1173350384}[：显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[成员信息。不指定本参数，则显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[成员信息。]{style="font-family:宋体"}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_728271280}[：显示通过指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口学到的成员信息。]{style="font-family:宋体"}

[**[local ]{lang="EN-US"}***[local-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x559320079}[：显示通过指定]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的成员信息。]{style="font-family:宋体"}*[local-ip]{lang="EN-US"}*[表示本地]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[remote ]{lang="EN-US"}***[client-ip]{lang="EN-US"}*]{#struct_0_20244_20619_1887892032}[：显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址的成员信息。]{style="font-family:宋体"}*[client-ip]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1342403275}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_351337543}[学到的成员信息，包括成员的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址、桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址、创建时间、老化时间等信息。]{style="font-family:宋体"}

[[如果不指定任何参数，将显示设备上]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_1684101651}[学到的所有成员信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_932310000}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x131640887}[显示设备上]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[成员信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery server member]{lang="EN-US"}]{#struct_0_20244_20619_727681457}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[IP Address: 11.0.0.1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time     ]{lang="EN-US"}

[11.0.0.3        000F-0001-0001    25        2011/01/01 00:00:43]{lang="EN-US"}

[11.0.0.4        000F-0001-0002    15        2011/01/01 01:00:46]{lang="EN-US"}

[11.0.0.5        000F-0001-0003    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2]{lang="EN-US"}

[IP Address: 11.0.1.2]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time       ]{lang="EN-US"}

[11.0.1.3        000F-0001-0011    19        2011/01/01 00:19:31]{lang="EN-US"}

[11.0.1.4        000F-0001-0012    30        2011/01/01 02:00:43]{lang="EN-US"}

[11.0.1.5        000F-0001-0013    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel2    Network ID: 3]{lang="EN-US"}

[IP Address: 12.0.0.1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time  ]{lang="EN-US"}

[12.0.0.2        000F-0002-0001    30        2011/01/01 03:20:43]{lang="EN-US"}

[12.0.0.3        000F-0002-0002    37        2011/01/01 03:27:46]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1705111286}[显示设备上]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学到的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[成员信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery ipv6 server member]{lang="EN-US"}]{#struct_0_20244_20619_727746993}

[Interface: Tunnel0    Network ID: 1]{lang="EN-US"}

[IP Address: 2000::1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time     ]{lang="EN-US"}

[2000::3         000F-0001-0001    25        2011/01/01 00:00:43]{lang="EN-US"}

[2000::4         000F-0001-0002    15        2011/01/01 01:00:46]{lang="EN-US"}

[2000::5         000F-0001-0003    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel1    Network ID: 2]{lang="EN-US"}

[IP Address: 2000::2]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time         ]{lang="EN-US"}

[2000::3         000F-0001-0001    19        2011/01/01 00:19:31]{lang="EN-US"}

[2000::4         000F-0001-0002    30        2011/01/01 02:00:43]{lang="EN-US"}

[2000::5         000F-0001-0003    20        2011/01/01 01:02:13]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: Tunnel2    Network ID: 3]{lang="EN-US"}

[IP Address: 3000::1]{lang="EN-US"}

[Client Address  System ID         Expire    Created Time       ]{lang="EN-US"}

[3000::2         000F-0002-0001    30        2011/01/01 03:20:43]{lang="EN-US"}

[3000::3         000F-0002-0002    37        2011/01/01 03:27:46]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display evi neighbor-discovery server member]{lang="EN-US"}]{#struct_0_20244_20619_1749221671}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2080898275}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_x1515341643}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_611790838}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_x231830249}

[[启动]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_1501618963}[功能的接口名称]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_727550385}

[[配置的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_x2010214530}

[[IP Address]{lang="EN-US"}]{#struct_0_20244_20619_x1258107803}

[[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_1138065473}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client Address]{lang="EN-US"}]{#struct_0_20244_20619_139513369}

[[学到的成员的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_20244_20619_1525480118}[地址]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[System ID]{lang="EN-US"}]{#struct_0_20244_20619_1928737628}

[[学到的成员的桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_727615921}[地址]{style="font-family:宋体"}

[[Expire ]{lang="EN-US"}]{#struct_0_20244_20619_x2140274192}

[[成员的剩余老化时间]{style="font-family:宋体"}]{#struct_0_20244_20619_1274801102}

[[Created Time]{lang="EN-US"}]{#struct_0_20244_20619_x85737628}

[[成员的创建时间]{style="font-family:宋体"}]{#struct_0_20244_20619_x1601751410}

[ ]{lang="EN-US"}

::: {#-1627752222 .myid}
[]{#_Toc404798357}[]{#struct_0_20244_20619_x1986886283}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server statistics**

------------------------------------------------------------------------

[**[display evi neighbor-discovery server statistics]{lang="EN-US"}**]{#struct_0_20244_20619_554070435}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_727943601}

[**[display evi neighbor-discovery server statistics interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_1150998078}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_317180101}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_2048702081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x871543304}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1956738811}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_116050313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_330019065}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x2067588274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_760578239}

[**[interface tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_728009137}[：显示指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2056990072}

[[通过本命令可以查看使能]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_x886531891}[功能后，接口收到和发送报文的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_214219119}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x302142570}[显示]{style="font-family:宋体"}[IPv4 EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel0]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery server statistics interface tunnel 0]{lang="EN-US"}]{#struct_0_20244_20619_x210368604}

[Received packets:]{lang="EN-US"}

[  Register:     170              Purge:      13   ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Reply:        170              Error:      1    ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x179603692}[显示]{style="font-family:宋体"}[IPv6 EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery server statistics interface tunnel 1]{lang="EN-US"}]{#struct_0_20244_20619_727812529}

[Received packets:]{lang="EN-US"}

[  Register:     170              Purge:      13   ]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[  Reply:        170              Error:      1    ]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display evi neighbor-discovery server statistics]{lang="EN-US"}]{#struct_0_20244_20619_385775932}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2110953379}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1474645229}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x615935340}

[[Received packets]{lang="EN-US"}]{#struct_0_20244_20619_x707448626}

[[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_x395143621}[收到的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Register]{lang="EN-US"}]{#struct_0_20244_20619_1543817167}[：表示注册报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Purge]{lang="EN-US"}]{#struct_0_20244_20619_727878065}[：表示注销报文]{lang="EN-US" style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_20244_20619_2759353}

[[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_x1348356321}[发送的报文统计信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reply]{lang="EN-US"}]{#struct_0_20244_20619_23740583}[：表示注册应答报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_20244_20619_1634238481}[：表示错误指示报文]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1593401250 .myid}
[]{#_Toc404798358}[]{#struct_0_20244_20619_1706801708}[]{#_Toc302983424}[]{#_Toc303068856}[]{#_Toc302983425}[]{#_Toc303068857}

**EVI \-- EVI配置命令 \-- display evi neighbor-discovery server summary**

------------------------------------------------------------------------

[**[display evi neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_20244_20619_1540003708}[命令用来在]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[上显示]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1152896826}

[**[display evi neighbor-discovery]{lang="EN-US"}**[ \[ **ipv6** \] **server summary**]{lang="EN-US"}]{#struct_0_20244_20619_728205745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_956218304}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x2043621495}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x79041519}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_309822462}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_1590305367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_75216546}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_1125994731}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1036017740}

[**[ipv6]{lang="EN-US"}**]{#struct_0_20244_20619_728271281}[：显示]{style="font-family:宋体"}[IPv6 ENDS]{lang="EN-US"}[的运行信息。不指定本参数，则显示]{style="font-family:宋体"}[IPv4 ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x559320078}

[[通过本命令可以查看]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_1887826496}[的运行信息，包括]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的配置信息、通过该]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[学习到的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[个数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_190799783}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1823047533}[显示]{style="font-family:宋体"}[IPv4 ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery server summary]{lang="EN-US"}]{#struct_0_20244_20619_x891281914}

[Interface      Local Address   Network ID    Auth        Members]{lang="EN-US"}

[Tunnel0        20.0.0.1        1             enabled     10      ]{lang="EN-US"}

[Tunnel2        21.0.0.1        2             disabled    20      ]{lang="EN-US"}

[Tunnel3        22.0.0.1        NA            disabled    0        ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1987137305}[显示]{style="font-family:宋体"}[IPv6 ENDS]{lang="EN-US"}[的运行信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi neighbor-discovery ipv6 server summary]{lang="EN-US"}]{#struct_0_20244_20619_727681454}

[Interface      Local Address   Network ID    Auth        Members]{lang="EN-US"}

[Tunnel0        2000::1         1             enabled     10      ]{lang="EN-US"}

[Tunnel2        2000::2         2             disabled    20      ]{lang="EN-US"}

[Tunnel1        2000::3         NA            disabled    0       ]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display evi neighbor-discovery server summary]{lang="EN-US"}]{#struct_0_20244_20619_1705111289}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2110266627}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_x1053517731}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x2055615244}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_x1307152548}

[[启动]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_x1148102219}[功能的接口名称]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_20244_20619_x754794201}

[[接口的源端地址，]{style="font-family:宋体"}[NA]{lang="EN-US"}]{#struct_0_20244_20619_1689329727}[表示未配置]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_727746990}

[[接口下配置的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_1749221674}[，]{style="font-family:宋体"}[NA]{lang="EN-US"}[表示未配置]{style="font-family:宋体"}

[[Auth]{lang="EN-US"}]{#struct_0_20244_20619_x1515145035}

[[是否使能认证功能：]{style="font-family:宋体"}]{#struct_0_20244_20619_x19970370}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[enabled]{lang="EN-US"}]{#struct_0_20244_20619_x1327445897}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[disabled]{lang="EN-US"}]{#struct_0_20244_20619_1744445832}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Members]{lang="EN-US"}]{#struct_0_20244_20619_727550382}

[[通过该]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_x2010214533}[学习到的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_307976138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_20244_20619_1690613765}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_20244_20619_182254227}

::: {#-58272938 .myid}
[]{#_Toc404798359}[]{#struct_0_20244_20619_712805197}[]{#_Toc364422900}[]{#_Toc351711391}

**EVI \-- EVI配置命令 \-- display evi vlan-mapping**

------------------------------------------------------------------------

[**[display evi vlan-mapping]{lang="EN-US"}**]{#struct_0_20244_20619_x1643147530}[命令用来显示]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[的]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1254615621}

[**[display evi ]{lang="EN-US"}[vlan-mapping]{lang="EN-US"}**[ \[ *process-id* \[ **vlan** *vlan-id* \] \]]{lang="EN-US"}]{#struct_0_20244_20619_713263949}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1690839715}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_713198413}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_660679189}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1010924017}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1214851477}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_712739662}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x1782632255}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1265059232}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_712674126}[：显示指定的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，将显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x1429762518}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的映射信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[如果不指定本参数，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x663080617}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x410312608}[显示所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下的所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display evi vlan-mapping]{lang="EN-US"}]{#struct_0_20244_20619_712608590}

[                         VLAN mappings for EVI IS-IS(0)]{lang="EN-US"}

[Local-VID  Peer-ID          Remote-VID  Interface   Remote-site]{lang="EN-US"}

[120        c4ca.d9e0.b804   121         EVI-Link2   10]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         VLAN mappings for EVI IS-IS(1)]{lang="EN-US"}

[Local-VID  Peer-ID          Remote-VID  Interface   Remote-site]{lang="EN-US"}

[150        3822.d659.6204   180         EVI-Link1   2]{lang="EN-US"}

[300        3822.d659.6204   301         EVI-Link1   2]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display evi vlan-mapping]{lang="EN-US"}]{#struct_0_20244_20619_957922441}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1958761540}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_712543054}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1292953230}

[[VLAN mappings for EVI IS-IS(0)]{lang="EN-US"}]{#struct_0_20244_20619_713001806}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_617324655}[进程]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射信息]{style="font-family:宋体"}

[[Local-VID]{lang="EN-US"}]{#struct_0_20244_20619_712936270}

[[本设备上的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x417791185}[号]{style="font-family:宋体"}

[[Peer-ID]{lang="EN-US"}]{#struct_0_20244_20619_712870734}

[[与本设备关于上述]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x411851530}[有映射关系的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[Remote-VID]{lang="EN-US"}]{#struct_0_20244_20619_712870731}

[[邻居上与上述]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x411851525}[映射的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_712805195}

[[邻居所属的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x1643147528}[接口]{style="font-family:宋体"}

[[Remote-site]{lang="EN-US"}]{#struct_0_20244_20619_713263947}

[[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_1690839721}[映射所对应的远端站点]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#489325041 .myid}
[]{#_Toc307929275}[]{#_Toc309203840}[]{#_Toc404798360}[]{#struct_0_20244_20619_1475091566}[]{#_Toc313451969}

**EVI \-- EVI配置命令 \-- display interface evi-link**

------------------------------------------------------------------------

[**[display interface evi-link]{lang="EN-US"}**]{#struct_0_20244_20619_918798450}[命令用来显示]{style="font-family:
宋体"}[EVI-Link]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1706792753}

[**[display interface]{lang="EN-US"}**[ \[ **evi-link** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_20244_20619_727615918}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x183959049}

[[任意视图]{style="font-family:宋体"}]{#struct_0_20244_20619_913904910}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_2023711456}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x579560482}

[[network-operator]{lang="EN-US"}]{#struct_0_20244_20619_850133607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_905127692}

[[mdc-operator]{lang="EN-US"}]{#struct_0_20244_20619_x2097510601}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x77315574}

[*[interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_727943598}[：显示指定]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口编号，取值为已创建的]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_20244_20619_744978534}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_20244_20619_x705518853}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_20244_20619_1300203679}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1043556835}

[[本命令可以显示]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x1561512984}[接口的相关信息，包括缺省]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[、链路类型、]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道源端地址、]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道目的端地址、]{style="font-family:宋体"}[Network ID]{lang="IT"}[等。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20244_20619_x1839781412}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{style="font-family:宋体"}]{#struct_0_20244_20619_753256186}**[evi-link]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[evi-link]{lang="EN-US"}**]{#struct_0_20244_20619_295274096}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有已创建的]{lang="EN-US" style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_728009134}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2056990069}[显示接口]{style="font-family:宋体"}[EVI-Link0]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_20244_20619_1486055568}[display interface evi-link 0]{lang="IT"}

[EVI]{lang="EN-US"}[-Link0]{lang="IT"}

[Current state: UP]{lang="IT"}

[Description: ]{lang="IT"}[EVI]{lang="EN-US"}[-Link0 Interface]{lang="IT"}

[PVID: 1]{lang="IT"}

[Port link-type: trunk]{lang="IT"}

[ VLAN Passing:   none]{lang="IT"}

[ VLAN permitted: none]{lang="IT"}

[ Trunk port encapsulation:  IEEE 802.1q]{lang="IT"}

[This ]{lang="IT"}[EVI]{lang="EN-US"}[-link belongs to Tunnel0]{lang="IT"}

[Source 1.1.1.1, Destination 1.1.2.1]{lang="IT"}

[Network ID 1]{lang="IT"}

[[表1-18 ]{lang="EN-US"}[display interface evi-link]{lang="EN-US"}]{#struct_0_20244_20619_2100608639}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2112158083}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_x1546470270}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_x1725844547}

[[Current state]{lang="EN-US"}]{#struct_0_20244_20619_727812526}

[[接口的物理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_20244_20619_385775921}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_20244_20619_x481669904}[：该接口的物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_20244_20619_1016534255}[：该接口的物理状态为开启]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_20244_20619_217727620}

[[接口描述信息]{style="font-family:宋体"}]{#struct_0_20244_20619_90563558}

[[PVID]{lang="EN-US"}]{#struct_0_20244_20619_x1694314696}[: 1]{lang="IT"}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x1377824704}[接口的缺省]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}

[[Port link-type]{lang="EN-US"}]{#struct_0_20244_20619_728205742}[: trunk]{lang="IT"}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_956218299}[接口的链路类型为]{style="font-family:宋体"}[trunk]{lang="EN-US"}

[[VLAN Passing]{lang="EN-US"}]{#struct_0_20244_20619_331766513}

[[Trunk]{lang="EN-US"}]{#struct_0_20244_20619_x747414857}[口实际可以通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[已经创建，并且接口允许其通过），对于]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口来说，始终显示]{style="font-family:宋体"}[none]{lang="EN-US"}

[[VLAN permitted]{lang="EN-US"}]{#struct_0_20244_20619_x963297562}

[[Trunk]{lang="EN-US"}]{#struct_0_20244_20619_312824025}[口允许通过的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[不一定存在，可能没有创建），对于]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口来说，始终显示]{style="font-family:宋体"}[none]{lang="EN-US"}

[[Trunk port encapsulation]{lang="EN-US"}]{#struct_0_20244_20619_728271278}

[[Trunk]{lang="EN-US"}]{#struct_0_20244_20619_x1368624151}[口上封装的协议类型]{style="font-family:宋体"}

[[This EVI-link belongs to Tunnel0]{lang="EN-US"}]{#struct_0_20244_20619_x1108162979}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_2052163442}[接口所属的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道实例]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_20244_20619_87407194}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_727681455}[接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道本端地址]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_20244_20619_1705111288}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x1053452195}[接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道对端地址]{style="font-family:宋体"}

[[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_113884998}

[[EVI-Link]{lang="EN-US"}]{#struct_0_20244_20619_x1143585704}[接口所属的]{style="font-family:宋体"}[Network ID]{lang="IT"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_727746991}[显示接口]{style="font-family:宋体"}[EVI-Link0]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_20244_20619_1749221673}[display interface evi-link 0 brief]{lang="IT"}

[Brief information on interface(s) under bridge mode:]{lang="IT"}

[Link: ADM - administratively down; Stby - standby]{lang="IT"}

[Speed or Duplex: (a)/A - auto; H - half; F - full]{lang="IT"}

[Type: A - access; T - trunk; H - hybrid]{lang="IT"}

[Interface            Link Speed   Duplex Type PVID Description]{lang="IT"}

[ELNK0                UP   \--      \--     T    1]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_20244_20619_x1515472715}[显示当前物理状态为]{style="font-family:宋体"}[down]{lang="IT"}[的]{style="font-family:宋体"}[EVI-Link]{lang="IT"}[接口的信息以及]{style="font-family:宋体"}[down]{lang="IT"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface evi-link brief down]{lang="IT"}]{#struct_0_20244_20619_1507266866}

[Brief information on interface(s) under bridge mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Interface            Link Cause]{lang="EN-US"}

[ELNK0]{lang="IT"}[                DOWN Not connected]{lang="EN-US"}

[[表1-19 ]{lang="EN-US"}[display interface evi-link brief]{lang="EN-US"}]{#struct_0_20244_20619_x1043329693}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2108144643}[[字段]{style="font-family:黑体"}]{#struct_0_20244_20619_1732849777}

[[描述]{style="font-family:黑体"}]{#struct_0_20244_20619_727550383}

[[Brief information on interface(s) under bridge mode]{lang="IT"}]{#struct_0_20244_20619_x2010214532}

[[二层接口的概要信息]{style="font-family:宋体"}]{#struct_0_20244_20619_1874060079}

[[Interface]{lang="EN-US"}]{#struct_0_20244_20619_931083532}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_20244_20619_1949401480}

[[Link]{lang="EN-US"}]{#struct_0_20244_20619_x969754635}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_20244_20619_x1277889578}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_20244_20619_727615919}[：表示接口物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_20244_20619_x183959048}[：表示接口物理上不通]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_20244_20619_913970446}[：表示]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能打开]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_20244_20619_x641572772}[：表示该接口是一个备份接口]{style="font-family:宋体"}

[[Speed]{lang="EN-US"}]{#struct_0_20244_20619_x332060675}

[[接口的速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}]{#struct_0_20244_20619_13754796}

[[Duplex]{lang="EN-US"}]{#struct_0_20244_20619_727943599}

[[接口的双工模式，取值可能为：]{style="font-family:宋体"}]{#struct_0_20244_20619_744978533}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_20244_20619_x783627335}[：表示双工模式由自动协商结果决定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="EN-US"}]{#struct_0_20244_20619_x705715461}[：表示全双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[F(a)]{lang="EN-US"}]{#struct_0_20244_20619_1653880973}[：表示自动协商的结果为全双工]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_20244_20619_728009135}[：表示半双工]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H(a)]{lang="EN-US"}]{#struct_0_20244_20619_x2056990070}[：表示自动协商的结果为半双工]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_20244_20619_276267523}

[[链路类型，取值可能为：]{style="font-family:宋体"}]{#struct_0_20244_20619_x639070572}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_20244_20619_x858857043}[：表示]{lang="EN-US" style="font-family:宋体"}[Access]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_20244_20619_727812527}[：表示]{style="font-family:宋体"}[Trunk]{lang="EN-US"}[链路类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_20244_20619_385775922}[：表示]{lang="EN-US" style="font-family:宋体"}[Hybrid]{lang="EN-US"}[链路类型]{lang="EN-US" style="font-family:宋体"}

[[PVID]{lang="EN-US"}]{#struct_0_20244_20619_x481669907}

[[接口的缺省]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_1016599791}

[[Description]{lang="EN-US"}]{#struct_0_20244_20619_x1639369528}

[[用户通过]{style="font-family:宋体"}**[description]{lang="EN-US"}**]{#struct_0_20244_20619_727878063}[命令给接口配置的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[[Cause]{lang="EN-US"}]{#struct_0_20244_20619_2759355}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_20244_20619_1783811561}[的原因，取值为]{style="font-family:宋体"}[Administratively]{lang="EN-US"}[时表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态；取值为]{style="font-family:宋体"}[Not connected]{lang="EN-US"}[时表示没有物理连接（可能没有插网线或者网线故障）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#856040934 .myid}
[]{#_Toc404798361}[]{#struct_0_20244_20619_x723916022}

**EVI \-- EVI配置命令 \-- evi arp-suppression enable**

------------------------------------------------------------------------

[**[evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_x1583277944}[命令用来开启]{style="font-family:
宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[**[undo evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_x209091183}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_728205743}

[**[evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_956218298}

[**[undo evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_331766514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x747414854}

[[EVI ARP]{lang="EN-US"}]{#struct_0_20244_20619_x963100954}[泛洪抑制功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_372252862}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1231564648}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x670809694}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x454104680}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_728271279}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1368624150}

[[边缘设备通过侦听]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_1620720376}[隧道终结的流量建立]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项，当侦听到本站点内主机请求其它站点主机的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求时，优先根据]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项进行代答，没有表项的则将]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求泛洪到公网。该功能可以大大减少]{style="font-family:宋体"}[ARP]{lang="EN-US"}[泛洪的次数。]{style="font-family:宋体"}

[[需要注意的是，如果在动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x1618982152}[地址表项老化时间内，远端站点的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[边缘设备没有流量转发到本地站点，那么远端]{style="font-family:宋体"}[EVI]{lang="EN-US"}[边缘设备上的动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项就会老化删除，同时通过]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[通告本地站点的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[边缘设备也删除对应表项。此时，如果本地站点内其他主机向对端站点内主机发出]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求，本地]{style="font-family:宋体"}[EVI]{lang="EN-US"}[边缘设备会根据]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项对该]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求进行代答。但是，报文在转发时会因为在本地]{style="font-family:宋体"}[EVI]{lang="EN-US"}[边缘设备的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表中没有对应表项而被丢弃，造成流量黑洞。]{style="font-family:宋体"}

[[为了避免]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_1511301674}[边缘设备错误地代答本地的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[请求造成流量黑洞，用户需要配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项老化时间不小于]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项老化时间。]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项的缺省老化时间为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟，动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的缺省老化时间与设备型号有关，请以设备实际情况为准。可以通过命令]{style="font-family:宋体"}**[display mac-address aging-time]{lang="EN-US"}**[和]{style="font-family:
宋体"}**[mac-address timer]{lang="EN-US"}**[查看和配置动态]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的老化时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_704263031}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1873357097}[在]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下开启]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2078507990}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel 101\] evi arp-suppression enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x110029895}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi arp-suppression]{lang="EN-US"}**]{#struct_0_20244_20619_945816045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-address timer]{lang="EN-US"}**]{#struct_0_20244_20619_x1619047688}[（二层技术]{lang="EN-US" style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换命令参考]{lang="EN-US" style="font-family:宋体"}[/MAC]{lang="EN-US"}[地址表）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ evi arp-suppression]{lang="EN-US"}**]{#struct_0_20244_20619_546325247}
:::

::: {#1214032688 .myid}
[]{#_Toc404798362}[]{#struct_0_20244_20619_x2001201897}[]{#_Toc312867800}

**EVI \-- EVI配置命令 \-- evi designated-vlan**

------------------------------------------------------------------------

[**[evi designated-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_x40812489}[命令用来配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[evi designated-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_122995524}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1990907116}

[**[evi designated-vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_20244_20619_76139554}

[**[undo ]{lang="EN-US"}[evi designated-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_1756582524}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1978188999}

[[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x679834783}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1275843958}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x58873699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001136361}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1912418671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1287825782}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_731430265}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_157942285}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_20244_20619_73141}

[[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_681213413}[用来进行站点内]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的交互。]{style="font-family:宋体"}

[[网络规划时，必须保证各边缘设备在其指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_1892006312}[内可达。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x630308382}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2001332969}[配置指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_1737152065}

[\[Sysname\] evi designated-vlan 2]{lang="EN-US"}
:::

::::: {#-553476736 .myid}
[]{#_Toc404798363}[]{#struct_0_20244_20619_x1719861705}

**EVI \-- EVI配置命令 \-- evi enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](EVI命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_20244_20619_1926038713}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_20244_20619_x185673545}
:::

**[ ]{lang="EN-US"}**

[**[evi enable]{lang="EN-US"}**]{#struct_0_20244_20619_x1195323243}[命令用来开启接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo evi enable]{lang="EN-US"}**]{#struct_0_20244_20619_x1451821848}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1533311809}

[**[evi enable]{lang="EN-US"}**]{#struct_0_20244_20619_1063559330}

[**[undo evi enable]{lang="EN-US"}**]{#struct_0_20244_20619_x2001267433}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_480596017}

[[接口的]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x1078915685}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1491270500}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_20244_20619_710236399}[三层以太网接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1880462705}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1773105736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_591814235}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1061352759}

[[用户需要在接入]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x2000939753}[网络的所有物理接口上开启]{style="font-family:宋体"}[EVI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1102964158}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x426372695}[开启接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_2002512438}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] evi enable]{lang="EN-US"}
:::::

::: {#-1534104400 .myid}
[]{#_Toc404798364}[]{#struct_0_20244_20619_2087267923}[]{#_Toc312867801}

**EVI \-- EVI配置命令 \-- evi extend-vlan**

------------------------------------------------------------------------

[**[evi extend-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_x1924347778}[命令用来配置扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo evi extend-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_1110202175}[命令用来取消配置的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1724914738}

[**[evi]{lang="EN-US"}[ extend-vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_20244_20619_x540647347}

[**[undo evi ]{lang="EN-US"}[extend-vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_20244_20619_x2000874217}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_257952927}

[[没有配置扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x1099886792}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x991705087}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x315653087}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_2131195158}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2070888147}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_280824602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1786249125}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_20244_20619_x2001070825}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，指定了扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1422908480}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x539772071}[配置扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[15]{lang="EN-US"}[和]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x959263764}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi extend-vlan 1 to 10 15 100 to 200]{lang="EN-US"}
:::

::::: {#1745583417 .myid}
[]{#_Toc404798365}[]{#struct_0_20244_20619_343184400}

**EVI \-- EVI配置命令 \-- evi flooding enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](EVI命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_20244_20619_x1345374011}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_20244_20619_x526299143}
:::

**[ ]{lang="EN-US"}**

[**[evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_587602468}[命令用来开启]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能。]{style="font-family:宋体"}

[**[undo evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_386791031}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001005289}

[**[evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_2009517643}

[**[undo evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_852522337}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1933093756}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x1689024071}[泛洪功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1739561355}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2120153923}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_470374797}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x119771873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2000677609}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_855223329}

[[缺省情况下，边缘设备对于未知地址的帧（包括未知单播帧和未知组播帧）只在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_751034641}[内的站点内部接口上进行泛洪，不会泛洪到其它站点。如果用户希望未知地址的帧可以泛洪到其它站点，可以开启]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能，当边缘设备收到未知地址的帧时，可以通过]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道泛洪转发到其它站点。]{style="font-family:宋体"}

[**[evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_666883186}[命令和]{style="font-family:宋体"}**[evi selective-flooding mac-address]{lang="EN-US"}**[命令的区别如下：]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_x452613141}[命令是]{lang="EN-US" style="font-family:宋体"}[将]{style="font-family:宋体"}[所有的未知单播帧和未知组播帧都向其它站点泛洪]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi selective-flooding mac-address]{lang="EN-US"}**]{#struct_0_20244_20619_x1378839298}[命令]{lang="EN-US" style="font-family:宋体"}[是针对某业务的]{lang="EN-US" style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[放开限制，]{lang="EN-US" style="font-family:宋体"}[仅将配置的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围内向]{style="font-family:宋体"}[其它站点]{lang="EN-US" style="font-family:宋体"}[泛洪。]{style="font-family:宋体"}

[[上述两个命令的使用场景不同，建议用户不要同时配置。如果用户同时配置了这两条命令，系统实际执行的是]{style="font-family:宋体"}**[evi flooding enable]{lang="EN-US"}**]{#struct_0_20244_20619_x351423256}[命令，无法实现]{style="font-family:宋体"}**[evi selective-flooding mac-address]{lang="EN-US"}**[命令的控制效果]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1406244027}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1988233578}[在]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下开启]{style="font-family:宋体"}[EVI]{lang="EN-US"}[泛洪功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2000612073}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel 101\] evi flooding enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x71149617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi selective-flooding mac-address]{lang="EN-US"}**]{#struct_0_20244_20619_x259343399}
:::::

::: {#-1689227581 .myid}
[]{#_Toc404798366}[]{#struct_0_20244_20619_675320928}[]{#_Toc312867806}

**EVI \-- EVI配置命令 \-- evi isis ded-priority**

------------------------------------------------------------------------

[**[evi isis]{lang="EN-US"}[ ded-priority]{lang="EN-US"}**]{#struct_0_20244_20619_2144483214}[命令用来配置]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo evi isis]{lang="EN-US"}[ ded-priority]{lang="EN-US"}**]{#struct_0_20244_20619_382387007}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_711797231}

[**[evi isis]{lang="EN-US"}[ ded-priority ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_20244_20619_x1757346989}

[**[undo evi isis ded-priority]{lang="EN-US"}**]{#struct_0_20244_20619_1376211552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_730316977}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_x2001201896}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1606896430}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_2062596574}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x376831215}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1995207065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2016294938}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1551329431}

[*[value]{lang="EN-US"}*]{#struct_0_20244_20619_1644647789}[：配置]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_966786196}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_x2001136360}[分为站点内]{style="font-family:宋体"}[DED]{lang="EN-US"}[和站点间]{style="font-family:宋体"}[DED]{lang="EN-US"}[，二者的选举方式和作用不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[站点内]{style="font-family:宋体"}]{#struct_0_20244_20619_x816464684}[DED]{lang="EN-US"}[：站点内的各边缘设备通过交互]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文来选举站点内]{style="font-family:宋体"}[DED]{lang="EN-US"}[。由站点内]{style="font-family:宋体"}[DED]{lang="EN-US"}[来分配各边缘设备的激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[站点间]{style="font-family:宋体"}]{#struct_0_20244_20619_1223795985}[DED]{lang="EN-US"}[：每个]{style="font-family:宋体"}[EVI Link]{lang="EN-US"}[两端的边缘设备通过交互]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文选举出一个站点间]{style="font-family:宋体"}[DED]{lang="EN-US"}[。站点间的边缘设备通过站点间]{style="font-family:宋体"}[DED]{lang="EN-US"}[周期性发布]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步。]{style="font-family:宋体"}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_892523942}[优先级数值越高，被选中的可能性就越大；如果两台边缘设备的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级相同，则]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址较大的边缘设备会被选中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_337602336}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1509794074}[配置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[的]{style="font-family:宋体"}[DED]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x846465555}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis ded-priority 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x610880640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **evi isis** **tunnel**]{lang="EN-US"}]{#struct_0_20244_20619_x840314084}
:::

::: {#-205923979 .myid}
[]{#_Toc404798367}[]{#struct_0_20244_20619_x2016143691}[]{#_Toc364422908}[]{#_Toc351711389}

**EVI \-- EVI配置命令 \-- evi isis preferred-vlan**

------------------------------------------------------------------------

[**[evi isis preferred-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_653543976}[命令用来配置优先分配给本设备的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，本设备将优先作为这些扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的授权转发设备。]{style="font-family:宋体"}

[**[undo evi isis preferred-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_x2016209227}[命令用来取消优先分配给本设备的扩展]{style="font-family:
宋体"}[VLAN]{lang="EN-US"}[的配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1400979714}

[**[evi isis preferred-vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_20244_20619_x846578633}

[**[undo evi isis preferred-vlan]{lang="EN-US"}**[ *vlan-list*]{lang="EN-US"}]{#struct_0_20244_20619_x2016274763}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1943389352}

[[没有配置优先分配给本设备的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x534643606}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x658483345}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2016340299}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_435529036}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x818016170}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2015881547}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x820674432}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_20244_20619_867708715}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，指定了优先分配给本设备的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2015947083}

[[边缘设备配置了优先作为扩展]{style="font-family:宋体"}[VLAN X]{lang="EN-US"}]{#struct_0_20244_20619_x1959382277}[的授权转发设备后，]{style="font-family:宋体"}[DED]{lang="EN-US"}[会优先将扩展]{style="font-family:宋体"}[VLAN X]{lang="EN-US"}[分配给该边缘设备作为激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。两台或多台站点内边缘设备都配置了同样的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则仍按照原来的平均和连续的原则分配激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。取消配置后，如果该扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[没有被其他边缘设备配置为优先分配的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，按稳定原则不改变其授权转发设备。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20244_20619_332016319}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次配置本命令，其结果是多次配置]{style="font-family:宋体"}]{#struct_0_20244_20619_756254985}[VLAN]{lang="EN-US"}[的合集。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的优先分配给本设备的扩展]{style="font-family:宋体"}]{#struct_0_20244_20619_x2016012619}[VLAN]{lang="EN-US"}[必须是所配置的扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的子集，如果用户配置的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[本身就不是扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则不起作用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1019471621}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x182218744}[配置本设备优先作为扩展]{style="font-family:宋体"}[VLAN1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[的授权转发设备。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2016078155}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis preferred-vlan 1 to 10 15 100 to 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x249289588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi extend-vlan]{lang="EN-US"}**]{#struct_0_20244_20619_897591831}
:::

::: {#152098546 .myid}
[]{#_Toc404798368}[]{#struct_0_20244_20619_x2001332968}[]{#_Toc312867802}

**EVI \-- EVI配置命令 \-- evi isis timer csnp**

------------------------------------------------------------------------

[**[evi isis timer csnp]{lang="EN-US"}**]{#struct_0_20244_20619_x991731290}[命令用来配置]{style="font-family:宋体"}[DED]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo evi isis timer csnp]{lang="EN-US"}**]{#struct_0_20244_20619_2042212790}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x50835994}

[**[evi isis timer csnp]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_20244_20619_x1272771953}

[**[undo evi isis timer csnp]{lang="EN-US"}**]{#struct_0_20244_20619_1686168109}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_83743354}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_395150309}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1669971740}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2001267432}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1085487924}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_122031081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1794126852}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1455668794}

[*[seconds]{lang="EN-US"}*]{#struct_0_20244_20619_1078079024}[：]{style="font-family:宋体"}[DED]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1787421802}

[[DED]{lang="EN-US"}]{#struct_0_20244_20619_x770704837}[使用]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步，只有在被选举为]{style="font-family:宋体"}[DED]{lang="EN-US"}[的设备上进行该项配置才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_69719306}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x80337812}[配置]{style="font-family:宋体"}[DED]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2000939752}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis timer csnp 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_463119783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **evi isis** **tunnel**]{lang="EN-US"}]{#struct_0_20244_20619_x312368664}
:::

::: {#-389062720 .myid}
[]{#_Toc404798369}[]{#struct_0_20244_20619_652244762}[]{#_Toc312867803}

**EVI \-- EVI配置命令 \-- evi isis timer hello**

------------------------------------------------------------------------

[**[evi isis timer hello]{lang="EN-US"}**]{#struct_0_20244_20619_133996761}[命令用来配置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo evi isis timer hello]{lang="EN-US"}**]{#struct_0_20244_20619_x1963739612}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1202078875}

[**[evi isis timer ]{lang="EN-US"}[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_20244_20619_x1599551289}

[**[undo evi isis timer hello]{lang="EN-US"}**]{#struct_0_20244_20619_x1346374637}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000874216}

[[EVI IS-IS Hello]{lang="EN-US"}]{#struct_0_20244_20619_1824036868}[报文的发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1808616112}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_564399325}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_678935850}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_82687089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1180983299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_56407527}

[*[seconds]{lang="EN-US"}*]{#struct_0_20244_20619_x1496364442}[：配置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001070824}

[[EVI IS-IS Hello]{lang="EN-US"}]{#struct_0_20244_20619_143175461}[报文的发送时间间隔越短，网络收敛越快，但也需要占用更多的系统资源；因此，需要根据实际情况指定]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[DED]{lang="EN-US"}]{#struct_0_20244_20619_x1725545905}[发送]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的时间间隔是]{style="font-family:宋体"}**[evi isis timer ]{lang="EN-US"}[hello]{lang="EN-US"}**[命令设置的时间间隔的]{style="font-family:宋体"}[1/3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1672154035}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1855477702}[配置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1109724080}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis timer hello 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_507811741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **evi isis** **tunnel**]{lang="EN-US"}]{#struct_0_20244_20619_1306815212}
:::

::: {#-428882458 .myid}
[]{#_Toc404798370}[]{#struct_0_20244_20619_1040738792}[]{#_Toc312867804}

**EVI \-- EVI配置命令 \-- evi isis timer holding-multiplier**

------------------------------------------------------------------------

[**[evi isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_20244_20619_x2001005288}[命令用来配置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文失效数目。]{style="font-family:宋体"}

[**[undo evi isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_20244_20619_443433702}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1124246054}

[**[evi isis timer holding-multiplier]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_20244_20619_x1673704721}

[**[undo evi isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_20244_20619_x30952559}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1063831469}

[[EVI IS-IS Hello]{lang="EN-US"}]{#struct_0_20244_20619_x739352109}[报文失效数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_834259847}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1625882129}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000677608}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1873660026}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x957494867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1290280995}

[*[value]{lang="EN-US"}*]{#struct_0_20244_20619_x332769050}[：配置邻居的]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文失效数目，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1976888592}

[[当前边缘设备可以将邻接关系保持时间通过]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}]{#struct_0_20244_20619_520253864}[报文通知邻居边缘设备，如果邻居边缘设备在邻接关系保持时间内没有收到来自当前边缘设备的]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文，将宣告邻接关系失效。]{style="font-family:宋体"}

[[邻接关系保持时间＝]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}]{#struct_0_20244_20619_x443172825}[报文失效数目×]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文发送时间间隔。]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文失效数目，即宣告邻接关系失效前]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[没有收到的邻居]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的数目。通过设置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文失效数目和]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻接关系保持时间，即邻居边缘设备要花多长时间能够监测到链路已经失效并重新进行路由计算。]{style="font-family:宋体"}

[[邻接关系保持时间最大不能超过]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_20244_20619_1261643667}[秒，超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒时，算作]{style="font-family:宋体"}[65535]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1545621163}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2000612072}[配置]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文失效数目]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_1494934324}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis timer holding-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x751818256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi isis tunnel]{lang="EN-US"}**]{#struct_0_20244_20619_1072207841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi isis timer hello]{lang="EN-US"}**]{#struct_0_20244_20619_x590578604}
:::

::: {#1468725198 .myid}
[]{#_Toc404798371}[]{#struct_0_20244_20619_1321107757}[]{#_Toc312867805}

**EVI \-- EVI配置命令 \-- evi isis timer lsp**

------------------------------------------------------------------------

[**[evi isis timer lsp]{lang="EN-US"}**]{#struct_0_20244_20619_x1550729429}[命令用来配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[在接口上发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔以及一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目。]{style="font-family:宋体"}

[**[undo evi isis timer lsp]{lang="EN-US"}**]{#struct_0_20244_20619_x37155100}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1912442309}

[**[evi isis timer lsp]{lang="EN-US"}**[ ]{lang="EN-US"}*[time ]{lang="EN-US"}*[\[ **count** *count* \]]{lang="EN-US"}]{#struct_0_20244_20619_x2001201899}

[**[undo ]{lang="EN-US"}[evi isis timer lsp]{lang="EN-US"}**]{#struct_0_20244_20619_1478217285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1402960968}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_249963205}[的最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x250387651}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_1259389424}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x917809805}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1788543838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1564541492}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001136363}

[*[time]{lang="EN-US"}*]{#struct_0_20244_20619_x1219749211}[：发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，为]{style="font-family:宋体"}[100]{lang="EN-US"}[的整数倍，单位为毫秒。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**[ ]{lang="EN-US"}*[count]{lang="EN-US"}*]{#struct_0_20244_20619_x1975314139}[：一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_1838889819}

[[当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_20244_20619_1546470479}[的内容发生变化时，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[将把发生变化的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散出去，用户可以对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送时间间隔进行调节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x31308976}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1403322868}[配置发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_1819884245}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis timer lsp 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1869862541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **evi isis** **brief**]{lang="EN-US"}]{#struct_0_20244_20619_x2001332971}
:::

::: {#-305263964 .myid}
[]{#_Toc404798372}[]{#struct_0_20244_20619_x2015947086}[]{#_Toc364422913}[]{#_Toc351711388}

**EVI \-- EVI配置命令 \-- evi isis track**

------------------------------------------------------------------------

[**[evi isis track]{lang="EN-US"}**]{#struct_0_20244_20619_x1199867390}[命令用来配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo evi isis track]{lang="EN-US"}**]{#struct_0_20244_20619_x1092569208}[命令用来删除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2016012622}

[**[evi isis track ]{lang="EN-US"}***[track-entry-number]{lang="EN-US"}*]{#struct_0_20244_20619_1066722396}

[**[undo evi isis track]{lang="EN-US"}**]{#struct_0_20244_20619_x1004192614}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x865846592}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2016078158}[不与任何]{style="font-family:宋体"}[Track]{lang="EN-US"}[项联动。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1365034835}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_1080205354}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2015619406}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_209457553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2055558627}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2015684942}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_20244_20619_352962443}[：指定]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_2068273462}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2016143693}[关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项后，可以通过]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的状态来检测上行口的故障。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_1816343390}[接口下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[实例最多关联一个]{style="font-family:宋体"}[Track]{lang="EN-US"}[项，当配置多次时，最后配置的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项生效。关于]{style="font-family:宋体"}[Track]{lang="EN-US"}[的详细介绍请参见"可靠性"中的"]{style="font-family:宋体"}[Track]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_880060272}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2016209229}[配置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[上运行的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1374957808}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] evi isis track 1]{lang="EN-US"}
:::

::: {#1445277343 .myid}
[]{#_Toc404798373}[]{#struct_0_20244_20619_1380987241}

**EVI \-- EVI配置命令 \-- evi neighbor-discovery authentication**

------------------------------------------------------------------------

[**[evi neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_20244_20619_853398560}[命令用来使能]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[**[undo evi neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_20244_20619_635103427}[命令用来关闭]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1327549153}

[**[evi neighbor-discovery authentication]{lang="EN-US"}**[ { **cipher** \| **simple** } ]{lang="EN-US"}]{#struct_0_20244_20619_303363053}*[password]{lang="EN-US"}*

[**[undo evi neighbor-discovery authentication]{lang="EN-US"}**]{#struct_0_20244_20619_x51311396}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_2139976774}

[[ENDP]{lang="EN-US"}]{#struct_0_20244_20619_x1442898412}[认证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1295405738}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2001267435}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x682203397}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1840238501}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_1317660912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1188234466}

[**[cipher]{lang="EN-US"}**]{#struct_0_20244_20619_464472610}[：表示以密文方式设置认证密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_20244_20619_2143646613}[：表示以明文方式设置认证密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_20244_20619_912096246}[：设置的明文认证密码或密文认证密码，区分大小写。明文认证密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串；密文认证密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x646890487}

[[为了安全起见，可以配置]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_20244_20619_x2000939755}[认证功能来防止恶意的节点注册到]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_20244_20619_x296395104}[认证功能后，发送]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文的设备会使用配置的密码和]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对报文进行摘要运算，然后把运算结果放到报文的认证字段。对端设备收到]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[报文后，如果该设备未配置认证功能，则认为报文合法；如果设备配置了认证功能，则利用本端配置的密码和]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法对报文进行摘要运算，然后比较运算结果与报文认证字段携带的信息是否一致，如果一致则认为报文合法，如果不一致则认为报文非法。]{style="font-family:宋体"}

[[在一个安全的网络中，可以不配置]{style="font-family:宋体"}[ENDP]{lang="EN-US"}]{#struct_0_20244_20619_1594655637}[认证功能。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20244_20619_x960252358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个]{style="font-family:宋体"}]{#struct_0_20244_20619_2007304659}[EVI]{lang="EN-US"}[网络实例中所有的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[与]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[必须配置相同的认证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的认证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_20244_20619_x2075072211}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1071981277}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1412500346}[使能]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[认证功能，并以方式设置指定明文认证密码为]{style="font-family:宋体"}[web-evi]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_20244_20619_x833551234}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery authentication simple web-evi]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000874219}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_20244_20619_708291621}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery ipv6 client summary]{lang="EN-US"}**]{#struct_0_20244_20619_x474265588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery ipv6 server summary]{lang="EN-US"}**]{#struct_0_20244_20619_x1429512282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_20244_20619_x324140569}
:::

::: {#1919736554 .myid}
[]{#_Toc404798374}[]{#struct_0_20244_20619_x1828192049}

**EVI \-- EVI配置命令 \-- evi neighbor-discovery client enable**

------------------------------------------------------------------------

[**[evi neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_20244_20619_x814884715}[命令用来使能接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能，同时指定对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo evi neighbor-discovery client enable]{lang="EN-US"}**]{#struct_0_20244_20619_x1736333940}[命令用来关闭接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_977535572}

[**[evi neighbor-discovery client enable ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x1015762688}

[**[undo evi neighbor-discovery client enable ]{lang="EN-US"}***[server-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x2001070827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x260109066}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_837873790}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1283364244}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_561531389}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_522819193}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1580427433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_2083525005}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x479022565}

[*[server-ip]{lang="EN-US"}*]{#struct_0_20244_20619_x2001005291}[：]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[要连接的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_1653221747}

[[为了防止]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_431075515}[异常导致]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[不能加入]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络，用户可以为每个]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[指定两个]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[，这两个]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[同时有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1950265765}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1113230351}[使能]{style="font-family:宋体"}[IPv4 ENDC]{lang="EN-US"}[功能，该]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址为]{style="font-family:宋体"}[11.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_20244_20619_351092996}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery client enable 11.0.0.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1298912302}[使能]{style="font-family:宋体"}[IPv6 ENDC]{lang="EN-US"}[功能，该]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2000::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_20244_20619_1576977855}

[\[Sysname\] interface tunnel 0 mode evi ipv6]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery client enable 2000::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x543393047}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_20244_20619_x2000677611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery ipv6 client summary]{lang="EN-US"}**]{#struct_0_20244_20619_1211388153}
:::

::: {#-1462631934 .myid}
[]{#_Toc404798375}[]{#struct_0_20244_20619_x599872995}

**EVI \-- EVI配置命令 \-- evi neighbor-discovery client register-interval**

------------------------------------------------------------------------

[**[evi neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_20244_20619_x1257357957}[命令用来配置]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔。]{style="font-family:宋体"}

[**[undo evi neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_20244_20619_927519502}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_666808511}

[**[evi neighbor-discovery client register-interval ]{lang="EN-US"}**]{#struct_0_20244_20619_x1636467380}*[time-value]{lang="EN-US"}*

[**[undo evi neighbor-discovery client register-interval]{lang="EN-US"}**]{#struct_0_20244_20619_1073657078}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1711635397}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x2000612075}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1233949031}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1741350815}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x321926545}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x371976061}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x465650048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x352247414}

[*[time-value]{lang="EN-US"}*]{#struct_0_20244_20619_1725481385}[：注册时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_643475454}

[[ENDP]{lang="EN-US"}]{#struct_0_20244_20619_1511662623}[协议中用到了]{style="font-family:宋体"}[3]{lang="EN-US"}[个定时器：探测定时器、注册定时器、老化定时器。]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[探测定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20244_20619_x2001201898}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x87866656}[请求加入]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络时会启用探测定时器，该定时器以]{style="font-family:宋体"}[5]{lang="EN-US"}[秒的时间间隔定时向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送注册报文，收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[应答报文后会停止探测定时器。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[注册定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20244_20619_x1728987547}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_572399452}[加入]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络后，为了通告自己工作正常，会定时向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送注册报文，该定时器的默认时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒，用户可以通过配置]{style="font-family:宋体"}**[evi neighbor-discovery client register-interval]{lang="EN-US"}**[命令来调整该时间间隔。]{style="font-family:
宋体"}

[[如果]{style="font-family:宋体"}[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x6598806}[连续发送]{style="font-family:宋体"}[5]{lang="EN-US"}[个注册报文，都未能收到]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[的应答报文，则认为网络故障，此时需要清除之前学到的邻居信息，同时重新启用探测定时器。]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[老化定时器]{lang="EN-US" style="font-family:宋体"}]{#struct_0_20244_20619_1580995536}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_x469648046}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[发送的注册报文中携带注册时间间隔，]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[会记录该时间间隔。]{style="font-family:宋体"}

[[ENDC]{lang="EN-US"}]{#struct_0_20244_20619_160070834}[加入]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络后，如果]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[在]{style="font-family:宋体"}[5]{lang="EN-US"}[倍的注册时间内未收到]{style="font-family:
宋体"}[ENDC]{lang="EN-US"}[的注册报文则认为]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[出现故障，此时需要把]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[从]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络中删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1335740508}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2001136362}[配置]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[向]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[注册的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_20244_20619_346334730}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery client register-interval 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1419281626}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery client summary]{lang="EN-US"}**]{#struct_0_20244_20619_745107960}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery ipv6 client summary]{lang="EN-US"}**]{#struct_0_20244_20619_x2059256888}
:::

::: {#-1729921500 .myid}
[]{#_Toc404798376}[]{#struct_0_20244_20619_x295715478}

**EVI \-- EVI配置命令 \-- evi neighbor-discovery server enable**

------------------------------------------------------------------------

[**[evi neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_20244_20619_553419800}[命令用来使能接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo evi neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_20244_20619_850110671}[命令用来关闭接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1818024248}

[**[evi neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_20244_20619_x2001332970}

[**[undo evi neighbor-discovery server enable]{lang="EN-US"}**]{#struct_0_20244_20619_x1347896114}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1281998279}

[[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_39625066}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1587806068}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x30777435}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_292996078}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1078843890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1283902554}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001267434}

[[使能接口的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}]{#struct_0_20244_20619_2046679958}[功能时，会同时使能该接口的]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[功能（该]{style="font-family:宋体"}[ENDC]{lang="EN-US"}[对应的]{style="font-family:宋体"}[ENDS]{lang="EN-US"}[地址为该接口的源地址）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x721792753}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_2065754803}[使能]{style="font-family:宋体"}[IPv4 ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_20244_20619_712907160}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery server enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x810184971}[使能]{style="font-family:宋体"}[IPv6 ENDS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="DA"}]{#struct_0_20244_20619_111125633}

[\[Sysname\] interface tunnel 0 mode evi ]{lang="DA"}[ipv6]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi neighbor-discovery server enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_525266586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery ipv6 server summary]{lang="EN-US"}**]{#struct_0_20244_20619_x1977430578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi neighbor-discovery server summary]{lang="EN-US"}**]{#struct_0_20244_20619_x2000939754}
:::

::: {#-1715512666 .myid}
[]{#_Toc404798377}[]{#struct_0_20244_20619_1269688837}

**EVI \-- EVI配置命令 \-- evi network-id**

------------------------------------------------------------------------

[**[evi network-id]{lang="EN-US"}**]{#struct_0_20244_20619_1806413487}[命令用来配置]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo evi network-id]{lang="EN-US"}**]{#struct_0_20244_20619_x1204572461}[命令用来删除]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_569786541}

[**[evi network-id ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_20244_20619_x981228526}

[**[undo evi network-id]{lang="EN-US"}**]{#struct_0_20244_20619_x376922258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1903684631}

[[没有配置]{style="font-family:宋体"}[Network ID]{lang="EN-US"}]{#struct_0_20244_20619_x777652719}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000874218}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2020591734}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x957990445}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1321726698}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1945220542}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_12648188}

[*[number]{lang="EN-US"}*]{#struct_0_20244_20619_1145806639}[：]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_1952810797}

[[一个站点需要加入]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x1588976624}[网络时，必须指定加入的]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络实例的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x102791573}[隧道只能属于一个]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络实例，一个站点加入多个]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络实例时，需要创建多个]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口，并使用该命令指定多个]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口分别属于哪个]{style="font-family:宋体"}[EVI]{lang="EN-US"}[网络实例。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001070826}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1305974875}[配置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Network ID]{lang="EN-US"}[为]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_1216017714}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] evi network-id 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x958039617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_20244_20619_x1632296479}
:::

::: {#-618772984 .myid}
[]{#_Toc404798378}[]{#struct_0_20244_20619_152490597}[]{#_Toc309203841}

**EVI \-- EVI配置命令 \-- evi selective-flooding mac-address**

------------------------------------------------------------------------

[**[evi selective-flooding mac-address]{lang="EN-US"}**]{#struct_0_20244_20619_421975276}[命令用来配置]{style="font-family:宋体"}[选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[evi selective-flooding mac-address]{lang="EN-US"}**]{#struct_0_20244_20619_x1092221101}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_710351199}

[**[evi selective-flooding mac-address ]{lang="EN-US"}***[mac-address ]{lang="EN-US"}***[vlan]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_20244_20619_x2001005290}*[vlan-id-list]{lang="SV"}*

[**[undo evi selective-flooding mac-address]{lang="EN-US"}***[ mac-address ]{lang="EN-US"}***[vlan]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_20244_20619_87137806}*[vlan-id-list]{lang="SV"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1771370030}

[[未配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_40318246}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1850330553}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_1332074189}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_401883815}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_554537871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1113532469}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000677610}

[*[mac-address]{lang="EN-US"}*]{#struct_0_20244_20619_x1517495202}[：选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不能为全]{style="font-family:宋体"}[F]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ ]{lang="EN-US"}*]{#struct_0_20244_20619_609319218}*[vlan-id-list]{lang="SV"}*[：指定]{style="font-family:宋体"}[选择性]{style="font-family:宋体"}[泛洪]{style="font-family:宋体"}[MAC]{lang="SV"}[地址]{style="font-family:
宋体"}[所属的]{style="font-family:宋体"}[VLAN]{lang="SV"}[范围，]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[ = { *vlan-id1* \[ **to** *vlan-id2* \] }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id2*]{lang="EN-US"}[的值要大于或等于]{style="font-family:宋体"}*[vlan]{lang="EN-US"}*[-*id1*]{lang="EN-US"}[的值，]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_844779929}

[[缺省情况下，边缘设备对于未知地址的帧（包括未知单播帧和未知组播帧）只在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x1418692922}[内的站点内部接口上进行泛洪，不会泛洪到其它站点。如果用户希望某些]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的帧可以泛洪到其它站点，可以通过本命令配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，当报文的目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址匹配该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址时，报文可以通过]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道泛洪转发到其它站点。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20244_20619_1282518663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[选择性泛洪]{style="font-family:宋体"}]{#struct_0_20244_20619_1393152497}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VLAN]{lang="SV"}[范围]{style="font-family:宋体"}[受到]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口下激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的范围影响，最终生效的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围为激活]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[和配置指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[之交集。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不要将可以学习到的单播]{style="font-family:宋体"}]{#struct_0_20244_20619_x678727855}[MAC]{lang="EN-US"}[地址设置为选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，否则可能会导致报文在远端设备被丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1117369941}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2000612074}[在]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下配置选择性泛洪的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_332134910}

[\[Sysname\] interface tunnel 101 mode evi]{lang="EN-US"}

[\[Sysname-tunnel 101\] evi selective-flooding mac-address 000f-e201-0101 vlan 1 to 10]{lang="EN-US"}
:::

::: {#1658840012 .myid}
[]{#_Toc404798379}[]{#struct_0_20244_20619_x2015881552}[]{#_Toc364422920}[]{#_Toc351711396}

**EVI \-- EVI配置命令 \-- evi site-id**

------------------------------------------------------------------------

[**[evi site-id]{lang="EN-US"}**]{#struct_0_20244_20619_x61225081}[命令用来指定一个设备所属的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo evi site-id]{lang="EN-US"}**]{#struct_0_20244_20619_x2015947088}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x749528696}

[**[evi site-id ]{lang="EN-US"}***[site-id]{lang="EN-US"}*]{#struct_0_20244_20619_407025165}

[**[undo evi site-id]{lang="EN-US"}**]{#struct_0_20244_20619_x2016012624}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x96077018}

[[站点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_1228546415}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2016078160}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1008607867}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_687817038}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x537913559}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2015619408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x240881141}

[*[site-id]{lang="EN-US"}*]{#struct_0_20244_20619_x497645975}[：站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2015684944}

[[站点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_1159531497}[用来唯一标识边缘设备所处的站点。如果没有为边缘设备配置站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[（采用缺省站点]{style="font-family:宋体"}[ID 0]{lang="EN-US"}[），则其他边缘设备认为该设备为站点间边缘设备。相同站点内的多台边缘设备必须配置相同的的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，不同站点间的边缘设备必须配置不同的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[或者均采用缺省站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当两台设备均在本地站点时，如果为设备配置不同的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_x1326010404}[或至少一台设备采用缺省站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，则会出现冲突，此时会将桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址较小的设备隔离；当两台设备分别为不同站点时，配置相同的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[时会出现冲突，此时同样会将桥]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址较小的设备隔离。此处的隔离是针对]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议来说的，被隔离的设备对于]{style="font-family:宋体"}[EVI IS-IS Hello]{lang="EN-US"}[报文将进行只收不发的处理，对于其它]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议报文将不会进行交互。设备被隔离的情况可以通过]{style="font-family:宋体"}**[display evi isis brief]{lang="EN-US"}**[命令和]{style="font-family:宋体"}**[display evi isis peer]{lang="EN-US"}**[命令查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2016143695}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1315824492}[配置设备所属的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[201]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1850549111}

[\[Sysname\] evi site-id 201]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2016209231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi-isis brief]{lang="EN-US"}**]{#struct_0_20244_20619_x1731253704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi isis peer]{lang="EN-US"}**]{#struct_0_20244_20619_x1624293619}
:::

::: {#-438344201 .myid}
[]{#_Toc404798380}[]{#struct_0_20244_20619_x2016274767}[]{#_Toc364422921}[]{#_Toc351711397}

**EVI \-- EVI配置命令 \-- evi vlan-mapping**

------------------------------------------------------------------------

[**[evi vlan-mapping]{lang="EN-US"}**]{#struct_0_20244_20619_382209476}[命令用来配置本设备上某]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与其他站点的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的映射关系。]{style="font-family:宋体"}

[**[undo evi vlan-mapping]{lang="EN-US"}**]{#struct_0_20244_20619_x411215636}[命令用来删除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2016340303}

[**[evi vlan-mapping ]{lang="EN-US"}***[local-vlan-id]{lang="EN-US"}*[ **translated** *remote-vlan-id* \[ **site** *site-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_1955017561}

[**[undo evi vlan-mapping]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[local-vlan-id ]{lang="EN-US"}***[translated]{lang="EN-US"}**[ *remote-vlan-id* \[ **site** *site-id* \] \]]{lang="EN-US"}]{#struct_0_20244_20619_x1695222566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2015881551}

[[未配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_342059446}[映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_73161045}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2015947087}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_366216551}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_790467120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2016012623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x499361545}

[*[local-vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x615010003}[：本地]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[remote-vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x2016078159}[：远端站点的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[site-id]{lang="EN-US"}*]{#struct_0_20244_20619_1363848520}[：远端站点的站点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。不指定本参数时，表示到其它所有站点的映射关系。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_1680256494}

[**[undo]{lang="EN-US"}**]{#struct_0_20244_20619_x2015619407}[命令中不指定任何参数时，表示删除所有的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[映射关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1356626388}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_851482076}[配置]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[与站点]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN 200]{lang="EN-US"}[进行映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2015684943}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] evi vlan-mapping 100 translated 200 site 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1919046384}[配置]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[与其它所有站点的]{style="font-family:宋体"}[VLAN 200]{lang="EN-US"}[进行映射。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1865683373}

[\[Sysname\] interface tunnel 101]{lang="EN-US"}

[\[Sysname-tunnel101\] evi vlan-mapping 100 translated 200]{lang="EN-US"}
:::

::: {#-41990894 .myid}
[]{#_Toc404798381}[]{#struct_0_20244_20619_355681392}[]{#_Toc312867799}

**EVI \-- EVI配置命令 \-- evi-isis**

------------------------------------------------------------------------

[**[evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_1709227347}[命令用来]{style="font-family:宋体"}[创建]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程，并进入]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_x1361739264}[命令用来删除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程或者]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下的配置数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x186897631}

[**[evi-isis ]{lang="EN-US"}***[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_x972643520}

[**[undo evi-isis ]{lang="EN-US"}***[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_466319194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1926253826}

[[不存在]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2001201901}[进程。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1122576750}

[[系统视图]{style="font-family:宋体"}]{#struct_0_20244_20619_13060612}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1338865464}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1155388418}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1887188467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_1741520817}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_1797407537}[：]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x407384890}

[[一个]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_547345260}[实例对应一个]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[EVI ]{lang="EN-US"}[IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x450190823}[进程有如下两种方法：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x1640107516}[接口下配置]{lang="EN-US" style="font-family:宋体"}[可以创建]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[的配置项]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}[此时]{lang="EN-US" style="font-family:宋体"}[会自动创建]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[，其进程]{style="font-family:宋体"}[ID]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口号相同]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{lang="EN-US" style="font-family:宋体"}**[evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_x450256359}[命令]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}[此时该]{lang="EN-US" style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程与相同编号的]{lang="EN-US" style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口相对应。]{lang="EN-US" style="font-family:宋体"}

[[创建]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x1617545664}[进程后，用户可以通过]{style="font-family:宋体"}**[evi-isis]{lang="EN-US"}**[命令进入]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[视图，配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程的协议参数。]{style="font-family:宋体"}

[[需要注意的是，如果没有配置扩展]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x399894442}[，对应的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程不生效。]{style="font-family:宋体"}

[[删除]{style="font-family:宋体"}[EVI ]{lang="EN-US"}[IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x449797607}[进程的时机如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有执行过]{style="font-family:宋体"}]{#struct_0_20244_20619_x370881942}**[evi-isis]{lang="EN-US"}**[命令]{style="font-family:宋体"}[，只是通过在]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口下配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[配置项而自动创建了]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程，在此种情况下，]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:
宋体"}[EVI Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[配置项]{style="font-family:宋体"}[时会自动删除对应的]{lang="EN-US" style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果执行过]{style="font-family:宋体"}]{#struct_0_20244_20619_1917226596}**[evi-isis]{lang="EN-US"}**[命令，那么]{style="font-family:宋体"}[删除]{lang="EN-US" style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[下的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[配置项]{style="font-family:宋体"}[时]{lang="EN-US" style="font-family:宋体"}[不]{style="font-family:宋体"}[会]{lang="EN-US" style="font-family:宋体"}[自动]{style="font-family:宋体"}[删除对应的]{lang="EN-US" style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}[，只能通过]{style="font-family:宋体"}**[undo evi-isis]{lang="EN-US"}**[命令来删除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}**[undo evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_x449863143}[命令时，如果]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程对应的]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口存在]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[配置项，则不会删除进程，只会清除]{style="font-family:宋体"}[进程下的配置数据]{lang="EN-US" style="font-family:宋体"}[；如果]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程对应的]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[接口下不存在]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[配置项，则会删除进程，并清除]{style="font-family:宋体"}[进程下的配置数据]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2064314947}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x886763085}[进入]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_567464058}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001332973}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi]{lang="EN-US"}**]{#struct_0_20244_20619_x1751180641}**[ ]{lang="EN-US"}[isis brief]{lang="EN-US"}**
:::

::: {#-283085117 .myid}
[]{#_Toc404798382}[]{#struct_0_20244_20619_21667123}[]{#_Toc364422923}[]{#_Toc351711387}

**EVI \-- EVI配置命令 \-- filter-policy**

------------------------------------------------------------------------

[**[filter-policy]{lang="EN-US"}**]{#struct_0_20244_20619_x449928679}[命令用来配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程绑定的路由策略。]{style="font-family:宋体"}

[**[undo filter-policy]{lang="EN-US"}**]{#struct_0_20244_20619_759871110}[命令用来删除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程绑定的路由策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x471610938}

[**[filter-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_20244_20619_x449994215}

[**[undo filter-policy]{lang="EN-US"}**]{#struct_0_20244_20619_x1172422840}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x481948887}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x449535463}[进程没有绑定路由策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_422032224}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x449600999}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x19000937}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1970998219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x450059750}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1266015779}

[*[policy-name]{lang="EN-US"}*]{#struct_0_20244_20619_1315845999}[：路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x450125286}

[[绑定路由策略后，该]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x1237931273}[进程只向其它站点通告路由策略允许的站点本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x950503548}[进程绑定的路由策略的配置中仅有如下两类匹配条件生效：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x450190822}[地址列表过滤的匹配条件]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VLAN]{lang="EN-US"}]{#struct_0_20244_20619_x1640173052}[范围的匹配条件]{style="font-family:宋体"}

[[关于路由策略的详细介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_20244_20619_1628941272}[路由配置指导"中的"路由策略"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x450256358}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1617611200}[配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程绑定路由策略]{style="font-family:宋体"}[EVI-Filter]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_379320725}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\] filter-policy EVI-Filter]{lang="EN-US"}
:::

::: {#63544256 .myid}
[]{#_Toc404798383}[]{#struct_0_20244_20619_x761031953}[]{#_Toc312867807}

**EVI \-- EVI配置命令 \-- graceful-restart**

------------------------------------------------------------------------

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_20244_20619_1898812663}[命令用来使能]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_20244_20619_x1388614027}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x424368912}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_20244_20619_592291280}

[**[undo ]{lang="EN-US"}[graceful-restart]{lang="EN-US"}**]{#struct_0_20244_20619_x639890677}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1833493269}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2001267437}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1845002811}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_316319881}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1836361300}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1756209315}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_707351952}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_598212973}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1691273711}[使能]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[101]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x420476411}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\] graceful-restart]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1256593441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi isis graceful-restart status]{lang="EN-US"}**]{#struct_0_20244_20619_x2000939757}
:::

::: {#16863910 .myid}
[]{#_Toc404798384}[]{#struct_0_20244_20619_866404310}[]{#_Toc312867808}

**EVI \-- EVI配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_20244_20619_655805221}[命令用来配置]{style="font-family:
宋体"}[EVI IS-IS]{lang="EN-US"}[协议的]{style="font-family:
宋体"}[GR]{lang="EN-US"}[重启间隔时间。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_20244_20619_x441770412}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1374088846}

[**[graceful-restart interval]{lang="EN-US"}**[ *interval-value*]{lang="EN-US"}]{#struct_0_20244_20619_x481894367}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_20244_20619_x1437263912}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1395088621}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x1413864358}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000874221}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_1064718589}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1887743627}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_208667256}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_443711999}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1404882949}

[*[interval-value]{lang="EN-US"}*]{#struct_0_20244_20619_x811014597}[：指定]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间（期望重启时间），取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1266525212}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_414226993}[配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2001070829}

[\[Sysname\] evi-isis 1]{lang="EN-US"}

[\[Sysname-evi-isis-1\] graceful-restart interval 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_190229628}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi isis graceful-restart status]{lang="EN-US"}**]{#struct_0_20244_20619_1571425626}
:::

::: {#-121527311 .myid}
[]{#_Toc404798385}[]{#struct_0_20244_20619_x2022397752}[]{#_Toc398738206}[]{#_Toc382506823}

**EVI \-- EVI配置命令 \-- gre key vlan-id**

------------------------------------------------------------------------

[**[gre key vlan-id]{lang="EN-US"}**]{#struct_0_20244_20619_485434183}[命令用来设置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口为发送的报文中添加根据]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[生成的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo gre key]{lang="EN-US"}**]{#struct_0_20244_20619_1256102737}[命令用来取消]{style="font-family:宋体"}[EVI]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1117307973}

[**[gre key]{lang="EN-US"}**[ **vlan-id**]{lang="EN-US"}]{#struct_0_20244_20619_1768305343}

[**[undo gre key]{lang="EN-US"}**]{#struct_0_20244_20619_2087033593}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_2052453967}

[[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x2021939000}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口发送的报文中不携带]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x453198635}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_1679726301}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1089867705}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1768396830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_8791908}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_2082448616}

[[通过设置]{style="font-family:宋体"}[EVI]{lang="EN-US"}]{#struct_0_20244_20619_x2022004536}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口发送报文时携带]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[后，发送方会在其发送的报文中携带]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[信息。接收方收到报文后将报文中的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[与接收方本地配置的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[进行比较，如果一致则对报文进行进一步处理；否则丢弃该报文。这样就可以防止设备接收非法报文。因此为保证通信正常，隧道两端必须设置相同的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[，或者都不设置]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[执行本命令后，边缘设备将根据报文中的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_20244_20619_x694307658}[自动生成]{style="font-family:宋体"}[EVI]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[，并封装到报文中。]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[的高]{style="font-family:宋体"}[12]{lang="EN-US"}[位为]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，低]{style="font-family:宋体"}[20]{lang="EN-US"}[位为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[部分产品发送报文时，报文中的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}]{#struct_0_20244_20619_x2058118535}[字段携带了]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。设备在与这些产品通信时需要配置本命令，使发出报文中的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[字段也携带]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1734212449}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1999634794}[设置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口为发送的报文添加根据]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[生成的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_1899543025}

[\[Sysname\] interface tunnel 1 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel2\] gre key vlan-id]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_2095053367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interf]{lang="SV"}[ace tunnel]{lang="EN-US"}**]{#struct_0_20244_20619_x1225920927}
:::

::: {#809257258 .myid}
[]{#_Toc404798386}[]{#struct_0_20244_20619_x580611499}[]{#_Toc312402795}[]{#_Toc338172110}[]{#_Toc338432526}[]{#_Toc338172111}[]{#_Toc338432527}[]{#_Toc338172112}[]{#_Toc338432528}[]{#_Toc338172113}[]{#_Toc338432529}[]{#_Toc338172114}[]{#_Toc338432530}[]{#_Toc338172115}[]{#_Toc338432531}[]{#_Toc338172116}[]{#_Toc338432532}[]{#_Toc338172117}[]{#_Toc338432533}[]{#_Toc338172118}[]{#_Toc338432534}[]{#_Toc338172119}[]{#_Toc338432535}[]{#_Toc338172120}[]{#_Toc338432536}[]{#_Toc338172121}[]{#_Toc338432537}[]{#_Toc338172122}[]{#_Toc338432538}[]{#_Toc338172123}[]{#_Toc338432539}[]{#_Toc338172124}[]{#_Toc338432540}[]{#_Toc338172125}[]{#_Toc338432541}[]{#_Toc338172126}[]{#_Toc338432542}[]{#_Toc338172127}[]{#_Toc338432543}[]{#_Toc338172128}[]{#_Toc338432544}[]{#_Toc338172129}[]{#_Toc338432545}[]{#_Toc338172130}[]{#_Toc338432546}[]{#_Toc338172131}[]{#_Toc338432547}[]{#_Toc338172132}[]{#_Toc338432548}[]{#_Toc338172133}[]{#_Toc338432549}[]{#_Toc338172134}[]{#_Toc338432550}[]{#_Toc338172135}[]{#_Toc338432551}[]{#_Toc338172136}[]{#_Toc338432552}[]{#_Toc338172137}[]{#_Toc338432553}

**EVI \-- EVI配置命令 \-- keepalive**

------------------------------------------------------------------------

[**[keepalive]{lang="EN-US"}**]{#struct_0_20244_20619_x823150129}[命令用来配置]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道探测对端状态的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期和最大发送次数。]{style="font-family:宋体"}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_20244_20619_x1620901677}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_257113706}

[**[keepalive]{lang="EN-US"}**[ \[ *seconds* \[ *times* \] \]]{lang="EN-US"}]{#struct_0_20244_20619_958820133}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_20244_20619_x992933419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x783365958}

[[keepalive]{lang="EN-US"}]{#struct_0_20244_20619_x2001005293}[报文的发送周期为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最大发送次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1478946135}

[[Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x810110112}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x695872997}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x815841925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_264724104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1511543895}

[*[seconds]{lang="EN-US"}*]{#struct_0_20244_20619_x831568302}[：]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[*[times]{lang="EN-US"}*]{#struct_0_20244_20619_144803660}[：]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的最大发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x339900364}

[[EVI Tunnel]{lang="EN-US"}]{#struct_0_20244_20619_x2000677613}[接口配置的]{style="font-family:宋体"}[ENDP]{lang="EN-US"}[协议会学习邻居信息并建立]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口。设备会从基于]{style="font-family:宋体"}[EVI Tunnel]{lang="EN-US"}[建立的各个]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口周期性发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果超时时间（即配置的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送周期）内没有收到对端的回应，则本端重新发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果达到最大发送次数后仍然没有收到对端的回应，则把本端]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的状态置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。如果]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，当收到对端回复的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[确认报文或收到对端发送的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文时，]{style="font-family:宋体"}[EVI-Link]{lang="EN-US"}[接口的状态将转换为]{style="font-family:宋体"}[up]{lang="EN-US"}[，否则保持]{style="font-family:宋体"}[down]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1920779729}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_1756884151}[配置]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的发送周期为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，最大发送次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_389632417}

[\[Sysname\] interface tunnel 0 mode evi]{lang="EN-US"}

[\[Sysname-Tunnel0\] keepalive 20 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_684663345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_20244_20619_x1774538611}
:::

::: {#-1553303123 .myid}
[]{#_Toc404798387}[]{#struct_0_20244_20619_1147857735}[]{#_Toc312867809}

**EVI \-- EVI配置命令 \-- log-peer-change enable**

------------------------------------------------------------------------

[**[log-peer-change enable]{lang="EN-US"}**]{#struct_0_20244_20619_301923272}[命令用来打开邻接状态变化的输出开关。]{style="font-family:宋体"}

[**[undo log-peer-change enable]{lang="EN-US"}**]{#struct_0_20244_20619_x2000612077}[命令用来关闭邻接状态变化的输出开关。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1898218851}

[**[log-peer-change enable]{lang="EN-US"}**]{#struct_0_20244_20619_2094183450}

[**[undo log-peer-change enable]{lang="EN-US"}**]{#struct_0_20244_20619_703983093}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1847000218}

[[邻接状态变化的输出开关处于打开状态。]{style="font-family:宋体"}]{#struct_0_20244_20619_590889941}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x814601488}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x174170548}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x964492808}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x918943110}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2001201900}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x443507191}

[[当打开邻接状态变化的输出开关后，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_852937265}[邻接状态变化时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定日志信息的输出规则（即是否允许输出以及输出方向）。有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1650538244}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x257898175}[关闭邻接状态变化的输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x362965022}

[\[Sysname\] evi-isis 1]{lang="EN-US"}

[\[Sysname-evi-isis-1\] ]{lang="EN-US"}[undo log-peer-change enable]{lang="NO-BOK"}
:::

::: {#693948098 .myid}
[]{#_Toc404798388}[]{#struct_0_20244_20619_x713463634}[]{#_Toc309203842}

**EVI \-- EVI配置命令 \-- reset evi arp-suppression**

------------------------------------------------------------------------

[**[reset evi arp-suppression]{lang="EN-US"}**]{#struct_0_20244_20619_1938388174}[命令用来清除]{style="font-family:
宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_580762133}

[**[reset evi arp-suppression interface ]{lang="EN-US"}[tunnel]{lang="EN-US"}***[ interface-number ]{lang="EN-US"}*[\[ **vlan** *vlan-id* \]]{lang="EN-US"}]{#struct_0_20244_20619_x2001136364}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1152903784}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20244_20619_x1683241439}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_1251725521}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_1271520683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_174601324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_998362942}

[**[interface ]{lang="EN-US"}[tunnel]{lang="EN-US"}***[ interface-number]{lang="EN-US"}*]{#struct_0_20244_20619_x2098895719}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口下的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_20244_20619_x900080278}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果]{style="font-family:宋体"}[不指定]{style="font-family:宋体"}[本参数]{style="font-family:宋体"}[，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x625348485}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x2001332972}[清除]{style="font-family:宋体"}[EVI]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel101]{lang="EN-US"}[下的]{style="font-family:宋体"}[EVI ARP]{lang="EN-US"}[泛洪抑制表项。]{style="font-family:宋体"}

[[\<Sysname\> reset evi arp-suppression interface tunnel 101]{lang="EN-US"}]{#struct_0_20244_20619_x185096700}

[This will delete all entries under the specified interface. Continue? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1228919492}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi arp-suppressio]{lang="EN-US"}[n]{lang="EN-US"}**]{#struct_0_20244_20619_x370424390}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[evi arp-suppression enable]{lang="EN-US"}**]{#struct_0_20244_20619_x458369806}
:::

::: {#2070418077 .myid}
[]{#_Toc404798389}[]{#struct_0_20244_20619_471212645}[]{#_Toc311280240}

**EVI \-- EVI配置命令 \-- reset evi isis all**

------------------------------------------------------------------------

[**[reset evi isis all]{lang="EN-US"}**]{#struct_0_20244_20619_778950899}[命令用来清除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下所有的动态数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1907443577}

[**[reset evi isis all ]{lang="EN-US"}**[\[ *process-id*]{lang="EN-US"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_20244_20619_96866387}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2001267436}

[[用户视图]{style="font-family:宋体"}]{#struct_0_20244_20619_883880544}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_852027561}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_x2059079720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_x1947446721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x973789409}

[*[process-id]{lang="EN-US"}*]{#struct_0_20244_20619_x1054611153}[：]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定本参数，将清除所有]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程下所有的动态数据。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_1890837527}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x476656574}[清除]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下所有的动态数据。]{style="font-family:宋体"}

[[\<Sysname\> reset evi isis all 1]{lang="EN-US"}]{#struct_0_20244_20619_x2000939756}
:::

::: {#870763228 .myid}
[]{#_Toc404798390}[]{#struct_0_20244_20619_x450190825}[]{#_Toc355684604}[]{#_Toc350517160}[]{#_Toc185927308}[]{#_Toc123026768}

**EVI \-- EVI配置命令 \-- snmp context-name**

------------------------------------------------------------------------

[**[snmp context-name]{lang="EN-US"}**]{#struct_0_20244_20619_x450256361}[命令用来配置管理]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[**[undo snmp context-name]{lang="EN-US"}**]{#struct_0_20244_20619_x1617021377}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x449797609}

[**[snmp context-name ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_20244_20619_x370750870}

[**[undo snmp context-name]{lang="EN-US"}**]{#struct_0_20244_20619_x1968045407}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x449863145}

[[没有配置管理]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_21798195}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x205386898}

[[EVI IS-IS]{lang="FR"}]{#struct_0_20244_20619_x449928681}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_759346835}

[[network-admin]{lang="FR"}]{#struct_0_20244_20619_801872231}

[[mdc-admin]{lang="FR"}]{#struct_0_20244_20619_x449994217}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1172291768}

[*[context-name]{lang="FR"}*]{#struct_0_20244_20619_620418277}[：]{style="font-family:宋体"}[管理]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[协议的]{style="font-family:宋体"}[SNMP]{lang="FR"}[实体所使用的上下文名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x449535465}

[[与]{style="font-family:宋体"}]{#struct_0_20244_20619_421901152}[IS-IS]{lang="FR"}[相同部分的]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[信息使用了]{style="font-family:宋体"}[IS-IS]{lang="FR"}[的标准]{style="font-family:宋体"}[MIB]{lang="FR"}[（]{style="font-family:宋体"}[Management Information Base]{lang="FR"}[，]{style="font-family:宋体"}[管理信息库]{style="font-family:宋体"}[）]{style="font-family:宋体"}[对]{style="font-family:宋体"}[NMS]{lang="FR"}[（]{style="font-family:宋体"}[Network Management System]{lang="FR"}[，]{style="font-family:宋体"}[网络管理系统]{style="font-family:宋体"}[）]{style="font-family:宋体"}[提供]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[信息对象的管理]{style="font-family:宋体"}[，]{style="font-family:宋体"}[但标准]{style="font-family:宋体"}[IS-IS MIB]{lang="FR"}[中定义的]{style="font-family:宋体"}[MIB]{lang="FR"}[为单实例管理对象]{style="font-family:宋体"}[，]{style="font-family:宋体"}[无法同时对]{style="font-family:宋体"}[IS-IS]{lang="FR"}[和]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[进行管理。因此，参考]{style="font-family:宋体"}[RFC 4750]{lang="EN-US"}[中对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[多实例的管理方法，需要为管理]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[定义一个上下文名称，以区分来自]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求是要对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[还是]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进行管理。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_20244_20619_1262975877}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有使用标准]{style="font-family:宋体"}]{#struct_0_20244_20619_x449601001}[IS-IS MIB]{lang="EN-US"}[的协议，如]{style="font-family:宋体"}[EVI]{lang="EN-US"}[、]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[、]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[等，]{style="font-family:宋体"}[都需]{style="font-family:宋体"}[要配置上下文名称以区分]{lang="EN-US" style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求的管理对象。各协议（包括各协议中的每个进程）配置的上下文名称都不能相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[由于上下文名称只是]{style="font-family:宋体"}]{#struct_0_20244_20619_x776305109}[SNMPv3]{lang="EN-US"}[独有的概念，因此对于]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[，会将团体名映射为上下文名称以对不同协议进行区分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x450059752}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x1265884707}[配置管理]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称为]{style="font-family:宋体"}[eviisis100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1713484803}

[\[Sysname\] evi-isis 100]{lang="EN-US"}

[\[Sysname-evi-isis-100\] snmp context-name eviisis100]{lang="EN-US"}
:::

::: {#-1345481650 .myid}
[]{#_Toc404798391}[]{#struct_0_20244_20619_x450125288}[]{#_Toc355684605}[]{#_Toc350517161}

**EVI \-- EVI配置命令 \-- snmp-agent trap enable evi-isis**

------------------------------------------------------------------------

[**[snmp-agent trap enable evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_x1237275913}[命令用来开启]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable evi-isis]{lang="EN-US"}**]{#struct_0_20244_20619_x893692001}[命令用来关闭]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x450190824}

[**[snmp-agent trap enable evi-isis]{lang="EN-US"}**[ \[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **link-disconnect** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}]{#struct_0_20244_20619_x1640041980}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| ]{lang="EN-US"}**[new-ded]{lang="NO-BOK"}**[ \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** \] \*]{lang="EN-US"}

[**[undo snmp-agent trap enable evi-isis]{lang="EN-US"}**[ \[ **adjacency-state-change** \| **area-mismatch** \| **buffsize-mismatch** \| **id-length-mismatch** \| **link-disconnect** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **max-seq-exceeded** \| ]{lang="EN-US"}]{#struct_0_20244_20619_1528162740}**[maxarea-mismatch]{lang="NO-BOK"}**[ \| ]{lang="EN-US"}**[new-ded]{lang="NO-BOK"}**[ \| **own-lsp-purge** \| **protocol-support** \| **rejected-adjacency** \| **skip-sequence-number** \| **topology-change** \| **version-skew** \] \*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_x450256360}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x1617086913}[的所有告警功能均处于开启状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x658494152}

[[系统]{style="font-family:宋体"}]{#struct_0_20244_20619_x449797608}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x370816406}

[[network-admin]{lang="FR"}]{#struct_0_20244_20619_x2018984283}

[[mdc-admin]{lang="FR"}]{#struct_0_20244_20619_x449863144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_21863731}

[**[adjacency-state-change]{lang="FR"}**]{#struct_0_20244_20619_x449928680}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[邻接状态变化的告警信息。]{style="font-family:宋体"}

[**[area-mismatch]{lang="FR"}**]{#struct_0_20244_20619_759412371}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Hello]{lang="FR"}[报文区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[buffsize-mismatch]{lang="FR"}**]{#struct_0_20244_20619_x2111446731}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[LSP]{lang="FR"}[长度与产生缓冲区大小不匹配的告警信息。]{style="font-family:宋体"}

[**[id-length-mismatch]{lang="FR"}**]{#struct_0_20244_20619_x449994216}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[EVI IS-IS]{lang="FR"}[报文中]{style="font-family:宋体"}[System ID]{lang="FR"}[长度不匹配的告警信息。]{style="font-family:宋体"}

[**[link-disconnect]{lang="FR"}**]{#struct_0_20244_20619_x1172357304}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ED]{lang="FR"}[的公网侧故障的告警信息。]{style="font-family:宋体"}

[**[lsp-parse-error]{lang="FR"}**]{#struct_0_20244_20619_369044545}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[LSP]{lang="FR"}[解析错误的告警信息。]{style="font-family:宋体"}

[**[lsp-size-exceeded]{lang="FR"}**]{#struct_0_20244_20619_x449535464}[：]{style="font-family:宋体"}[表示超大]{style="font-family:宋体"}[LSP]{lang="FR"}[导致泛洪失败的告警信息。]{style="font-family:宋体"}

[**[max-seq-exceeded]{lang="FR"}**]{#struct_0_20244_20619_421835616}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[LSP]{lang="FR"}[序列号超过最大序列号的告警信息。]{style="font-family:宋体"}

[**[maxarea-mismatch]{lang="NO-BOK"}**]{#struct_0_20244_20619_1214044467}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Hello]{lang="FR"}[报文最大区域地址不匹配的告警信息。]{style="font-family:宋体"}

[**[new-ded]{lang="NO-BOK"}**]{#struct_0_20244_20619_x449601000}[：]{style="font-family:宋体"}[表示本设备成为新的]{style="font-family:宋体"}[DED]{lang="NO-BOK"}[的告警信息。]{style="font-family:宋体"}

[**[own-lsp-purge]{lang="FR"}**]{#struct_0_20244_20619_x776239573}[：]{style="font-family:宋体"}[表示尝试清除本地]{style="font-family:宋体"}[LSP]{lang="FR"}[的告警信息。]{style="font-family:宋体"}

[**[protocol-support]{lang="FR"}**]{#struct_0_20244_20619_84469860}[：]{style="font-family:宋体"}[表示报文协议支持类型不匹配的告警信息。]{style="font-family:宋体"}

[**[rejected-adjacency]{lang="FR"}**]{#struct_0_20244_20619_x450059755}[：]{style="font-family:宋体"}[表示无法根据]{style="font-family:宋体"}[Hello]{lang="FR"}[报文建立邻接关系的告警信息。]{style="font-family:宋体"}

[**[skip-sequence-number]{lang="FR"}**]{#struct_0_20244_20619_x1266212387}[：]{style="font-family:宋体"}[表示跳过已产生过的]{style="font-family:宋体"}[LSP]{lang="FR"}[序列号的告警信息。]{style="font-family:宋体"}

[**[topology-change]{lang="FR"}**]{#struct_0_20244_20619_1270781925}[：]{style="font-family:宋体"}[表示站点内]{style="font-family:宋体"}[ED]{lang="FR"}[拓扑变化的告警信息。但同一事件导致发送了]{style="font-family:宋体"}[new-ded]{lang="FR"}[，]{style="font-family:宋体"}[则不发送本告警信息。]{style="font-family:宋体"}

[**[version-skew]{lang="FR"}**]{#struct_0_20244_20619_x450125291}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Hello]{lang="FR"}[报文版本号不匹配的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1237865736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何参数，将开启]{lang="EN-US" style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2058046401}[所有类型的告警功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[开启]{style="font-family:宋体"}]{#struct_0_20244_20619_x450190827}[EVI IS-IS]{lang="EN-US"}[模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1639845372}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x63372849}[开启]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[邻居状态变化的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x450256363}

[\[Sysname\] snmp-agent trap enable evi-isis adjacency-state-change]{lang="EN-US"}
:::

::: {#490996559 .myid}
[]{#_Toc404798392}[]{#struct_0_20244_20619_x1862479045}[]{#_Toc338172142}[]{#_Toc338432558}[]{#_Toc338172143}[]{#_Toc338432559}[]{#_Toc338172144}[]{#_Toc338432560}[]{#_Toc338172145}[]{#_Toc338432561}[]{#_Toc338172146}[]{#_Toc338432562}[]{#_Toc338172147}[]{#_Toc338432563}[]{#_Toc338172148}[]{#_Toc338432564}[]{#_Toc338172149}[]{#_Toc338432565}[]{#_Toc338172150}[]{#_Toc338432566}[]{#_Toc338172151}[]{#_Toc338432567}[]{#_Toc338172152}[]{#_Toc338432568}[]{#_Toc338172153}[]{#_Toc338432569}[]{#_Toc338172154}[]{#_Toc338432570}[]{#_Toc338172155}[]{#_Toc338432571}[]{#_Toc338172156}[]{#_Toc338432572}[]{#_Toc338172157}[]{#_Toc338432573}[]{#_Toc338172158}[]{#_Toc338432574}[]{#_Hlt19451604}[]{#_Toc338172159}[]{#_Toc338432575}[]{#_Toc338172160}[]{#_Toc338432576}[]{#_Toc338172161}[]{#_Toc338432577}[]{#_Toc338172162}[]{#_Toc338432578}[]{#_Toc338172163}[]{#_Toc338432579}[]{#_Toc338172164}[]{#_Toc338432580}[]{#_Toc338172165}[]{#_Toc338432581}[]{#_Toc338172166}[]{#_Toc338432582}[]{#_Toc338172167}[]{#_Toc338432583}[]{#_Toc338172168}[]{#_Toc338432584}[]{#_Toc338172169}[]{#_Toc338432585}[]{#_Toc338172170}[]{#_Toc338432586}[]{#_Toc338172171}[]{#_Toc338432587}[]{#_Toc338172172}[]{#_Toc338432588}[]{#_Toc338172173}[]{#_Toc338432589}[]{#_Toc338172174}[]{#_Toc338432590}[]{#_Toc338172175}[]{#_Toc338432591}[]{#_Toc338172176}[]{#_Toc338432592}[]{#_Toc338172177}[]{#_Toc338432593}[]{#_Toc338172178}[]{#_Toc338432594}[]{#_Toc338172179}[]{#_Toc338432595}[]{#_Toc338172180}[]{#_Toc338432596}[]{#_Toc338172181}[]{#_Toc338432597}[]{#_Toc338172182}[]{#_Toc338432598}

**EVI \-- EVI配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

[**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_20244_20619_1579830486}[命令用来配置当前边缘设备生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间。]{style="font-family:宋体"}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_20244_20619_834614278}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1669100624}

[**[timer lsp-max-age ]{lang="EN-US"}***[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_20244_20619_x17804370}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_20244_20619_716928566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_939950353}

[[当前边缘设备生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1852499872}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x514766503}

[[EVI IS-IS]{lang="EN-US"}]{#struct_0_20244_20619_x2000874220}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1664164766}

[[network-admin]{lang="EN-US"}]{#struct_0_20244_20619_662049421}

[[mdc-admin]{lang="EN-US"}]{#struct_0_20244_20619_312754953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_519783737}

[*[seconds]{lang="EN-US"}*]{#struct_0_20244_20619_402242265}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间，取值范围是]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_212994204}

[[每个]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_20244_20619_x1996091576}[都有一个最大生存时间，随着时间的推移最大生存时间将逐渐减小，当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[将启动清除过期]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的过程。用户可根据网络的实际情况调整]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1138569646}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_150172488}[配置生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[分钟，即]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x2001070828}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\] timer lsp-max-age 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1756313569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **evi isis** **brief**]{lang="EN-US"}]{#struct_0_20244_20619_x435042460}
:::

::: {#-1091829735 .myid}
[]{#_Toc404798393}[]{#struct_0_20244_20619_x848573725}[]{#_Toc312867812}

**EVI \-- EVI配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_20244_20619_x755196782}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期。]{style="font-family:宋体"}

[**[undo timer lsp-refresh]{lang="EN-US"}**]{#struct_0_20244_20619_501167707}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x37525117}

[**[timer lsp-refresh]{lang="FR"}**]{#struct_0_20244_20619_109350203}[ *second*s]{lang="FR"}

[**[undo timer lsp-refresh]{lang="FR"}**]{#struct_0_20244_20619_x2001005292}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1249937220}

[[LSP]{lang="FR"}]{#struct_0_20244_20619_557710246}[刷新周期为]{style="font-family:宋体"}[900]{lang="FR"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_1398607127}

[[EVI IS-IS]{lang="FR"}]{#struct_0_20244_20619_839699716}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_218556414}

[[network-admin]{lang="FR"}]{#struct_0_20244_20619_x1196933756}

[[mdc-admin]{lang="FR"}]{#struct_0_20244_20619_x1211392138}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x764662574}

[*[second]{lang="FR"}*]{#struct_0_20244_20619_x1543238978}[s]{lang="FR"}[：]{style="font-family:宋体"}[LSP]{lang="FR"}[刷新周期]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65534]{lang="FR"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2000677612}

[**[timer lsp-refresh]{lang="FR"}**]{#struct_0_20244_20619_x354695788}[命令配置的时间必须小于]{style="font-family:宋体"}**[timer lsp-max-age]{lang="FR"}**[命令配置的时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[以保证在]{style="font-family:宋体"}[LSP]{lang="FR"}[失效前进行刷新。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1978684468}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_x636223503}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期为]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x1902291317}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\] ]{lang="EN-US"}[timer lsp-refresh 1500]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_1059215565}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display evi isis brief]{lang="EN-US"}**]{#struct_0_20244_20619_x1485775282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_20244_20619_x2017287187}
:::

::: {#1347731002 .myid}
[]{#_Toc404798394}[]{#struct_0_20244_20619_x2000612076}

**EVI \-- EVI配置命令 \-- virtual-system**

------------------------------------------------------------------------

[**[virtual-system]{lang="EN-US"}**]{#struct_0_20244_20619_x830664504}[命令用来为系统创建一个]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[虚拟系统。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_20244_20619_208867433}**[virtual-system]{lang="EN-US"}**[命令用来删除一个系统中已经存在的]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[虚拟系统。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_20244_20619_x911786594}

[**[virtual-system ]{lang="EN-US"}**]{#struct_0_20244_20619_x94782465}*[system-id]{lang="EN-US"}*

[**[undo ]{lang="FR"}**]{#struct_0_20244_20619_1592737633}**[virtual-system ]{lang="EN-US"}***[system-id]{lang="EN-US"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_20244_20619_1134611683}

[[系统中没有创建]{style="font-family:宋体"}]{#struct_0_20244_20619_x1550868410}[EVI IS-IS]{lang="FR"}[虚拟系统。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_20244_20619_x822671253}

[[EVI IS-IS]{lang="FR"}]{#struct_0_20244_20619_x1252886984}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_20244_20619_378070234}

[[network-admin]{lang="FR"}]{#struct_0_20244_20619_x2133817888}

[[mdc-admin]{lang="FR"}]{#struct_0_20244_20619_x982029710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_20244_20619_x1694428216}

[*[system-id]{lang="FR"}*]{#struct_0_20244_20619_x1686507145}[：]{style="font-family:宋体"}[虚拟系统的系统]{style="font-family:宋体"}[ID]{lang="FR"}[，]{style="font-family:宋体"}[用来标识虚拟系统]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[格式为]{style="font-family:
宋体"}[XXXX.XXXX.XXXX]{lang="FR"}[，]{style="font-family:宋体"}[X]{lang="FR"}[表示十六进制数字。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_20244_20619_986785991}

[[当本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_20244_20619_x2044575202}[地址数超过系统的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片集所能携带的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数时，可以配置]{style="font-family:宋体"}[EVI IS-IS]{lang="EN-US"}[虚拟系统来扩展]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片数量，以增加系统所能发布的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数量。]{style="font-family:宋体"}

[[创建虚拟系统前，系统最多可以发送约]{style="font-family:宋体"}[55]{lang="EN-US"}]{#struct_0_20244_20619_x1206270340}[×]{style="font-family:宋体"}[2^10^]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，每创建一个虚拟系统，最多可以多发送]{style="font-family:宋体"}[55]{lang="EN-US"}[×]{style="font-family:宋体"}[2^10^]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。用户可以根据本地]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表的规模，来决定创建的虚拟系统的个数。]{style="font-family:宋体"}

[[创建虚拟系统时，用户要保证所配置的虚拟系统的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_20244_20619_1887292493}[在网络中是唯一的，否则会出现不可预知的错误。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_20244_20619_x2107011467}

[[\# ]{lang="EN-US"}]{#struct_0_20244_20619_378004698}[创建一个系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0001.0001.0001]{lang="EN-US"}[的虚拟系统。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_20244_20619_x963880915}

[\[Sysname\] evi-isis 101]{lang="EN-US"}

[\[Sysname-evi-isis-101\] ]{lang="EN-US"}[virtual-system 0001.0001.0001]{lang="NO-BOK"}
:::
