::: {#-279817366 .myid}
[]{#_Toc404789221}[]{#struct_0_17007_x1341_1782200747}[]{#_Toc135105529}[]{#_Toc133042077}[]{#_Toc94588229}[]{#_Toc80176776}

**IGMP Snooping \-- IGMP Snooping调试命令 \-- debugging igmp-snooping**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x700155977}

[**[debugging igmp-snooping ]{lang="EN-US"}**[{ **all** \| **entry** \| **error** \| **event** \| **fsm** \| **group** \| **packet** \[ **vlan** *vlan-id* \[ **port** *interface-type interface-number* \] \| **vsi** *vsi-name* \] \| **sync** \| **timer** }]{lang="EN-US"}]{#struct_0_17007_x1341_108329888}

[**[undo debugging igmp-snooping ]{lang="EN-US"}**[{ **all** \| **entry** \| **error** \| **event** \| **fsm** \| **group** \| **packet** \| **sync** \| **timer** }]{lang="EN-US"}]{#struct_0_17007_x1341_1156698836}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x408958556}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1787783524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x256261844}

[[network-admin]{lang="EN-US"}]{#struct_0_17007_x1341_886603080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17007_x1341_x1621988011}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17007_x1341_1428231615}

[**[all]{lang="EN-US"}**]{#struct_0_17007_x1341_1863493820}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[所有调试信息开关。]{style="font-family:宋体"}

[**[entry]{lang="EN-US"}**]{#struct_0_17007_x1341_x1754156773}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[表项调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17007_x1341_108395424}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17007_x1341_699222203}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[fsm]{lang="EN-US"}**]{#struct_0_17007_x1341_x1584115281}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[状态机调试信息开关。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**]{#struct_0_17007_x1341_x2094305594}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[组播组调试信息开关。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_17007_x1341_1431424042}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[报文调试信息开关。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_17007_x1341_x1355070937}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定本参数，表示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_17007_x1341_517009969}[：指定端口，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为端口类型和端口编号。如果未指定本参数，表示所有端口。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ *vsi-name*]{lang="EN-US"}]{#struct_0_17007_x1341_x451906358}[：指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sync]{lang="EN-US"}**]{#struct_0_17007_x1341_x258012521}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[板间消息同步调试信息开关。]{style="font-family:宋体"}

[**[timer]{lang="EN-US"}**]{#struct_0_17007_x1341_1861748849}[：表示]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[定时器调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x2005684585}

[**[debugging igmp-snooping]{lang="EN-US"}**]{#struct_0_17007_x1341_108460960}[命令用来打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging igmp-snooping]{lang="EN-US"}**[命令用来关闭]{style="font-family:
宋体"}[IGMP Snooping]{lang="EN-US"}[调试信息开关。]{style="font-family:
宋体"}

[[缺省情况下，]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}]{#struct_0_17007_x1341_1001211635}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-1 ]{lang="EN-US"}[debugging igmp-snooping entry]{lang="EN-US"}]{#struct_0_17007_x1341_x1712088892}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1315812566}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_984906756}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_1993087581}

[[Create IP entry (*source*, *group*) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1527500096}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_263926595}[VLAN *vlan*]{lang="EN-US"}[上创建]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Create router entry on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_674414923}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_108526496}[VLAN *vlan*]{lang="EN-US"}[上创建路由器表项]{style="font-family:宋体"}

[[Create MAC entry *mac* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1769818658}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x589386256}[VLAN *vlan*]{lang="EN-US"}[上创建]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}

[[Delete IP entry (*source*, *group*) from *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_925117913}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_413496118}[VLAN *vlan*]{lang="EN-US"}[中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Delete router entry from *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_404261420}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1508400429}[VLAN *vlan*]{lang="EN-US"}[中删除路由器表项]{style="font-family:宋体"}

[[Delete port *port* from MAC entry *mac*]{lang="EN-US"}]{#struct_0_17007_x1341_108592032}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1364555337}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[中删除端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Delete (*source*, *group*) from driver]{lang="EN-US"}]{#struct_0_17007_x1341_1508809263}

[[从驱动中删除表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_17007_x1341_x1231537062}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Delete (*source*, *group*) ports from driver]{lang="EN-US"}]{#struct_0_17007_x1341_355992129}

[[从驱动中删除端口（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_17007_x1341_108657568}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Delete (*source*, *group*) slot from driver]{lang="EN-US"}]{#struct_0_17007_x1341_409714142}

[[从驱动中删除板（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_17007_x1341_1394724528}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Delete MAC entry *mac* from driver]{lang="EN-US"}]{#struct_0_17007_x1341_330967738}

[[从驱动中删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1073120909}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Delete *mac* ports from driver]{lang="EN-US"}]{#struct_0_17007_x1341_x2038096813}

[[从驱动中删除端口]{style="font-family:宋体"}*[mac]{lang="EN-US"}*]{#struct_0_17007_x1341_108723104}

[[Delete *mac* slot from driver]{lang="EN-US"}]{#struct_0_17007_x1341_2024729683}

[[从驱动中删除板]{style="font-family:宋体"}*[mac]{lang="EN-US"}*]{#struct_0_17007_x1341_x1123991381}

[[Delete IP entry (*source*, *group*) from the noresource list]{lang="EN-US"}]{#struct_0_17007_x1341_x1077309230}

[[从无资源列表中删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_x2043669677}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Delete IP entry (*source*, *group*) from IP fail list]{lang="EN-US"}]{#struct_0_17007_x1341_107740064}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_348730495}[IP]{lang="EN-US"}[失败列表中删除]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add port *port* to (*source*, *group*) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_528826616}

[[添加端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1828499488}*[port]{lang="NL"}*[到]{style="font-family:宋体"}[VLAN *vlan*]{lang="NL"}[中的表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add port *port* to MAC *mac*]{lang="FR"}]{#struct_0_17007_x1341_1954178038}

[[添加端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_107805600}*[port]{lang="NL"}*[到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="FR"}*

[[Add IP ports from (*source*, *group*) to driver]{lang="EN-US"}]{#struct_0_17007_x1341_496758953}

[[通知驱动添加端口到]{style="font-family:宋体"}]{#struct_0_17007_x1341_x229634384}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add IP slot from (*source*, *group*) to driver]{lang="EN-US"}]{#struct_0_17007_x1341_1229991734}

[[通知驱动添加板到]{style="font-family:宋体"}]{#struct_0_17007_x1341_1203742547}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add MAC ports from *mac* to driver]{lang="EN-US"}]{#struct_0_17007_x1341_108264353}

[[通知驱动添加端口到]{style="font-family:宋体"}]{#struct_0_17007_x1341_1109852818}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Add *mac* slot to driver]{lang="EN-US"}]{#struct_0_17007_x1341_1782266283}

[[通知驱动添加板到]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1130602271}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Add IP entry (*source*, *group*) to IP fail list]{lang="EN-US"}]{#struct_0_17007_x1341_108329889}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_1156698835}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[到]{style="font-family:宋体"}[IP]{lang="EN-US"}[失败列表]{style="font-family:宋体"}

[[Add *mac* to MAC fail list]{lang="EN-US"}]{#struct_0_17007_x1341_x409155164}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_x218286112}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[失败列表]{style="font-family:宋体"}

[[Add IP entry (*source*, *group*) to driver]{lang="EN-US"}]{#struct_0_17007_x1341_108395425}

[[通知驱动添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_699222204}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add MAC *mac* to driver]{lang="EN-US"}]{#struct_0_17007_x1341_x1584115276}

[[通知驱动添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_x171139325}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Add IP entry (*source*, *group*) for the first time]{lang="EN-US"}]{#struct_0_17007_x1341_108460961}

[[第一时间添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_1001211634}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Copy router resource to (*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1712154428}

[[复制路由器资源到表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_17007_x1341_221604995}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Copy router resource to *mac*]{lang="EN-US"}]{#struct_0_17007_x1341_108526497}

[[复制路由器资源到]{style="font-family:宋体"}*[mac]{lang="EN-US"}*]{#struct_0_17007_x1341_1769818657}

[[Copy (\*,G) protocol resource to (*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x589845008}

[[复制（]{style="font-family:宋体"}]{#struct_0_17007_x1341_171609204}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）协议资源到表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Copy (\*,G) info to All (S,G) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_108592033}

[[复制（]{style="font-family:宋体"}]{#struct_0_17007_x1341_1364555338}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）信息到]{style="font-family:宋体"}[VLAN *vlan*]{lang="EN-US"}[上所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Copy (\*,G) protocol slot to All (S,G) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1508219439}

[[复制（]{style="font-family:宋体"}]{#struct_0_17007_x1341_108657569}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）协议板到]{style="font-family:宋体"}[VLAN *vlan*]{lang="EN-US"}[上所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Copy router ports to all entry on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_409714143}

[[复制路由器端口到]{style="font-family:宋体"}]{#struct_0_17007_x1341_1394724527}[VLAN *vlan*]{lang="EN-US"}[上所有表项]{style="font-family:宋体"}

[[Copy router slot to all entry on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_108723105}

[[复制路由器板到]{style="font-family:宋体"}]{#struct_0_17007_x1341_2024729682}[VLAN *vlan*]{lang="EN-US"}[上所有表项]{style="font-family:宋体"}

[[Remove (\*,G) info from All (S,G) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1123925845}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1010776334}[VLAN *vlan*]{lang="EN-US"}[上从所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项中删除（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）信息]{style="font-family:宋体"}

[[Remove (\*,G) protocol ports from All (S,G) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_107740065}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_348730494}[VLAN *vlan*]{lang="EN-US"}[上从所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项中删除（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）协议端口]{style="font-family:宋体"}

[[Remove (\*,G) protocol slot from All (S,G) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_528826615}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_107805601}[VLAN *vlan*]{lang="EN-US"}[上从所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项中删除（]{style="font-family:宋体"}[\*]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）协议板]{style="font-family:宋体"}

[[Remove router ports from all entry on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_496758952}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x229634383}[VLAN *vlan*]{lang="EN-US"}[上从所有表项中删除路由器端口]{style="font-family:宋体"}

[[Remove router slot from all entry on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674348297}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x710700984}[VLAN *vlan*]{lang="EN-US"}[上从所有表项中删除路由器板]{style="font-family:宋体"}

[[Driver hasn\'t enough resource for (*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_929551047}

[[存储表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*]{#struct_0_17007_x1341_1674413833}[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[驱动资源不足]{style="font-family:宋体"}

[[Notify kernel *version* enable/disable]{lang="EN-US"}]{#struct_0_17007_x1341_1216325920}

[[通知内核版本]{style="font-family:宋体"}*[version]{lang="EN-US"}*]{#struct_0_17007_x1341_1829462811}[使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}

[[Insert port *port* to tree]{lang="FR"}]{#struct_0_17007_x1341_1674479369}

[[将端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1099425011}*[port]{lang="FR"}*[插入树]{style="font-family:宋体"}

[[Can\'t find port ]{lang="EN-US"}]{#struct_0_17007_x1341_1674544905}*[port]{lang="FR"}*

[[无法找到端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1132329265}*[port]{lang="FR"}*

[[connect group *group* with MAC entry *mac*]{lang="EN-US"}]{#struct_0_17007_x1341_1938045123}

[[关联组地址]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674610441}*[group]{lang="EN-US"}*[和]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[debugging igmp-snooping error]{lang="EN-US"}]{#struct_0_17007_x1341_781595840}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1325286230}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_x603877024}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x314486856}

[[Multicast address is invalid]{lang="EN-US"}]{#struct_0_17007_x1341_558087126}

[[组播地址非法]{style="font-family:宋体"}]{#struct_0_17007_x1341_x427239010}

[[Wrong IGMPv*n* report packet which receive from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x742122968}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674675977}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上收到错误的版本为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[加入报文]{style="font-family:宋体"}

[[Failed to create Dynamic group (*source*, *group*) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_435786384}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x932466479}[VLAN *vlan*]{lang="EN-US"}[上创建动态表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[失败]{style="font-family:宋体"}

[[Failed to create host response timer on group *group* of port *port* in *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_1454903312}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1454968848}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上为组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[创建查询响应定时器失败]{style="font-family:宋体"}

[[Failed to add host port *port* to (*source*, *group*) on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x901580446}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x223022777}[VLAN *vlan*]{lang="EN-US"}[上添加端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[到动态表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[失败]{style="font-family:宋体"}

[[Failed to notify add host slot slot of (*source*, *group*) to other on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x707860057}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_384299490}[VLAN ]{lang="EN-US"}*[vlan]{lang="EN-US"}*[上通知其它板添加表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[的成员板失败]{style="font-family:宋体"}

[[Failed to add entry (*source*, *group*) to MSIB on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674741513}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_402046985}[VLAN ]{lang="EN-US"}*[vlan]{lang="EN-US"}*[上添加]{style="font-family:宋体"}[MSIB]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）失败]{style="font-family:宋体"}

[[Failed to update dbm data]{lang="EN-US"}]{#struct_0_17007_x1341_711866585}

[[更新]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1226225595}[DBM]{lang="EN-US"}[数据失败]{style="font-family:宋体"}

[[Failed to recover global *config* snooping disable]{lang="EN-US"}]{#struct_0_17007_x1341_x1141040299}

[[全局配置]{style="font-family:宋体"}*[config]{lang="EN-US"}*]{#struct_0_17007_x1341_2001245784}[恢复时失败]{style="font-family:宋体"}

[[Failed to parse message]{lang="EN-US"}]{#struct_0_17007_x1341_1674807049}

[[解析消息失败]{style="font-family:宋体"}]{#struct_0_17007_x1341_778861321}

[[Failed to get port type]{lang="EN-US"}]{#struct_0_17007_x1341_x344332245}

[[获取接口类型失败]{style="font-family:宋体"}]{#struct_0_17007_x1341_1811752891}

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[debugging igmp-snooping event]{lang="EN-US"}]{#struct_0_17007_x1341_x656401529}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1322809686}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_943881711}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_38131161}

[[Successfully enable/disable IGMP snooping on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1673824009}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1429469590}[VLAN *vlan*]{lang="EN-US"}[上使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[成功]{style="font-family:宋体"}

[[Received get level2 multicast IP/mac group message]{lang="EN-US"}]{#struct_0_17007_x1341_188386431}

[[收到获取二层组播]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1144174379}[IP/MAC]{lang="EN-US"}[组信息]{style="font-family:宋体"}

[[Received IGMP snooping debug message]{lang="EN-US"}]{#struct_0_17007_x1341_x11860441}

[[收到]{style="font-family:宋体"}]{#struct_0_17007_x1341_x787045046}[IGMP ]{lang="EN-US"}[Snooping]{lang="EN-US"}[调试信息]{style="font-family:宋体"}

[[Received IGMP snooping group message]{lang="EN-US"}]{#struct_0_17007_x1341_x585594104}

[[收到]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673889545}[IGMP ]{lang="EN-US"}[Snooping]{lang="EN-US"}[组信息]{style="font-family:宋体"}

[[Received IGMP snooping router port message]{lang="EN-US"}]{#struct_0_17007_x1341_147069583}

[[收到]{style="font-family:宋体"}]{#struct_0_17007_x1341_1970115219}[IGMP ]{lang="EN-US"}[Snooping]{lang="EN-US"}[路由器端口信息]{style="font-family:宋体"}

[[Received ha-upgrade event]{lang="EN-US"}]{#struct_0_17007_x1341_x585919814}

[[收到]{style="font-family:宋体"}]{#struct_0_17007_x1341_x625208048}[HA]{lang="EN-US"}[升级事件]{style="font-family:宋体"}

[[Received interface/slot/vlan event (Event:*event,* Sequence*=sequence*)]{lang="EN-US"}]{#struct_0_17007_x1341_420324745}

[[收到接口]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674348298}[/]{lang="EN-US"}[板]{style="font-family:宋体"}[/VLAN]{lang="EN-US"}[事件（事件为]{style="font-family:宋体"}*[event]{lang="EN-US"}*[，序列号为]{style="font-family:宋体"}*[sequence]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Global IGMP snooping is enabled]{lang="EN-US"}]{#struct_0_17007_x1341_x711552952}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_17007_x1341_155642186}[已全局使能]{style="font-family:宋体"}

[[IGMP snooping is disabling globally]{lang="EN-US"}]{#struct_0_17007_x1341_539865071}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_17007_x1341_1261652078}[正在全局关闭]{style="font-family:宋体"}

[[IGMP snooping is enabled/disabled on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_401489081}

[[IGMP Snooping]{lang="NL"}]{#struct_0_17007_x1341_1674413834}[在]{style="font-family:宋体"}[VLAN *vlan*]{lang="NL"}[上已使能]{style="font-family:宋体"}[/]{lang="EN-US"}[关闭]{style="font-family:宋体"}

[[Successfully enable multicast globally in driver]{lang="EN-US"}]{#struct_0_17007_x1341_1216129312}

[[在驱动上全局使能组播成功]{style="font-family:宋体"}]{#struct_0_17007_x1341_1771648324}

[[Successfully call driver enable multicast on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_2031587306}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x310007060}[VLAN *vlan*]{lang="EN-US"}[上调用驱动使能组播成功]{style="font-family:宋体"}

[[Port *port* is down or not belong the vlan *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674479370}

[[端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1098966258}*[port]{lang="EN-US"}*[ down]{lang="EN-US"}[或不属于]{style="font-family:宋体"}[VLAN *vlan*]{lang="EN-US"}

[[Delete all host response timers on port *port*]{lang="EN-US"}]{#struct_0_17007_x1341_1454182416}

[[删除端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_1454247952}*[port]{lang="EN-US"}*[上的所有查询响应定时器]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[debugging igmp-snooping fsm]{lang="EN-US"}]{#struct_0_17007_x1341_x958049305}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1292103062}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_1457856994}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_1499359342}

[[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_178011993}[ state changes from *state1* to *state2* on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674544906}[上表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[状态由]{style="font-family:宋体"}*[state1]{lang="EN-US"}*[迁移到]{style="font-family:宋体"}*[state2]{lang="EN-US"}*

[[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1132132657}[ state changes to *state* on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_2018191856}[上表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[状态迁移到]{style="font-family:宋体"}*[state]{lang="EN-US"}*

[[Notified add/delete host port *port* of ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_940934051}[ to main on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1743306218}[上通知主板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Notified add/delete host slot *slot* of ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1682189849}[ to other on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674610442}[上通知其它板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[成员板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Notified add/delete host slot *slot* of ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_781399232}[ to main on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1555430572}[上通知主板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[成员板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Notified add/delete router port *port* to main on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1703620896}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1665195088}[上通知主板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除路由器端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Notified add/delete router slot *slot* to other on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_130863852}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674675978}[上通知其它板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除路由器板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Notified add/delete router slot *slot* to main on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_435327632}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1022274384}[上通知主板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除路由器板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Notified add/delete global router port *port* to other on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_862170891}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_308081214}[上通知其它板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除全局路由器端口]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Notified add/delete global host port *port* of ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674741514}[ to other on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_402243593}[上通知其它板添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[全局成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Notified delete entry ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_647283087}[ to other on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1640818551}[上通知其它板删除表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Global host attribute is set to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_129002786}[on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674807050}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[设置全局成员特征]{style="font-family:宋体"}

[[Global host attribute is cleared from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_778402570}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1084400882}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除全局成员特征]{style="font-family:宋体"}

[[Global host port *port* is successfully added to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1014855414}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673824010}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加全局成员端口]{style="font-family:宋体"}

[[Global host port *port* is successfully deleted from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1429928341}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1308374994}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除全局成员端口]{style="font-family:宋体"}

[[Global router port *port* is successfully added on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1894648206}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673889546}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加全局路由器端口]{style="font-family:宋体"}

[[Global router port *port* is successfully deleted from *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_147266191}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x2024554455}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除全局路由器端口]{style="font-family:宋体"}

[[Host slot attribute is set to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x933874619}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x130412374}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[设置成员板特征]{style="font-family:宋体"}

[[Host slot attribute is cleared from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674348295}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x710832056}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除成员板特征]{style="font-family:宋体"}

[[Host slot *slot* is successfully added to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1052579353}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674413831}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加成员板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Host slot *slot* is successfully deleted from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1216456992}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x914559522}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除成员板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[[Local host attribute is set to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1988951367}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674479367}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加本地成员特征]{style="font-family:宋体"}

[[Local host attribute is cleared from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1099031795}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x2043519001}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除本地成员特征]{style="font-family:宋体"}

[[Local host port *port* is successfully added to ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674544903}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1132460337}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加本地成员端口]{style="font-family:宋体"}

[[Local host port *port* is successfully deleted from ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1680598716}[ on *vlan*]{lang="EN-US"}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674610439}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除本地成员端口]{style="font-family:宋体"}

[[Local router port *port* is successfully added on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_782120131}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1227394738}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[添加本地路由器端口]{style="font-family:宋体"}

[[Local router port *port* is successfully deleted from *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x918265446}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674675975}[VLAN *vlan*]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[删除本地路由器端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[debugging igmp-snooping group]{lang="EN-US"}]{#struct_0_17007_x1341_435655312}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1302613142}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_x905006494}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1307453013}

[[Add v*n* host port *port*]{lang="FR"}]{#struct_0_17007_x1341_x1237428465}

[[在端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x382067921}*[port]{lang="FR"}*[上添加版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的成员端口]{style="font-family:宋体"}

[[Create Dynamic group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674741511}[ on *vlan*, add host port *port*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_401915913}[上创建动态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[，并添加成员端口]{style="font-family:宋体"}*[port]{lang="FR"}*

[[Succeed in sending special group query packet for group *group* on host port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1777000449}

[[对]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1993396585}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="FR"}*[特定组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[成功发送特定源组查询报文]{style="font-family:宋体"}

[[Router port *port* times out on *vlan*, delete router port]{lang="EN-US"}]{#struct_0_17007_x1341_x604147744}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1888505515}[上路由器端口]{style="font-family:宋体"}*[port]{lang="FR"}*[超时，删除路由器端口]{style="font-family:宋体"}

[[Delete host port *port* for dynamic group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674807047}[ on *vlan*]{lang="EN-US"}

[[删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_778205961}[VLAN *vlan*]{lang="EN-US"}[上对动态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[路由器端口]{style="font-family:宋体"}*[port]{lang="FR"}*

[[Delete dynamic group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x680055377}[ on *vlan*]{lang="EN-US"}

[[删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_8227595}[VLAN *vlan*]{lang="EN-US"}[上的动态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Update v*n* host port *port* for dynamic group:]{lang="EN-US"}[ (*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x480655594}[ on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x231830470}[上更新动态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[的版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*[成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[The v1/v2 host is present, ignore the IGMPv3 BLOCK report packet]{lang="EN-US"}]{#struct_0_17007_x1341_1673824007}

[[版本]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1430387094}[1/]{lang="EN-US"}[版本]{style="font-family:宋体"}[2]{lang="EN-US"}[的主机存在，不处理收到的版本]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[BLOCK]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Delete the port *port* from all dynamic group]{lang="EN-US"}]{#struct_0_17007_x1341_x445741185}

[[将成员端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_323061268}*[port]{lang="EN-US"}*[从所有动态组表项中删除]{style="font-family:宋体"}

[[Delete all host port that on the slot *slot* and delete the slot *slot* from host slot bitmap]{lang="EN-US"}]{#struct_0_17007_x1341_348255753}

[[将属于板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673889543}*[slot]{lang="EN-US"}*[的所有成员端口删除，若该板是成员板，删除该板]{style="font-family:宋体"}

[[Clear all dynamic group on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_147462799}

[[清除]{style="font-family:宋体"}]{#struct_0_17007_x1341_1722973139}[VLAN *vlan*]{lang="EN-US"}[内所有动态组表项]{style="font-family:宋体"}

[[Send group specific query packet for group *group* on host port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_719556746}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x681331931}[上成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[发送特定组查询报文]{style="font-family:宋体"}

[[Create static group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674348296}[ on *vlan*, add host port *port*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x710635448}[上创建静态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[，并添加成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[The host port *port* does not exist in static group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1057607501}[ on *vlan*, add it]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_704088041}[上的静态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[不存在成员端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[，添加成员端口]{style="font-family:宋体"}

[[Delete host port *port* for static group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674413832}*[ ]{lang="EN-US"}*[on *vlan*]{lang="EN-US"}

[[删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_1216260384}[VLAN *vlan*]{lang="EN-US"}[上对静态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[路由器端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Delete static group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x159447713}[ on *vlan*]{lang="EN-US"}

[[删除]{style="font-family:宋体"}]{#struct_0_17007_x1341_1812447819}[VLAN *vlan*]{lang="EN-US"}[上的静态组（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[The port *port* is not router port, add it]{lang="EN-US"}]{#struct_0_17007_x1341_1674479368}

[[端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1099490547}*[port]{lang="EN-US"}*[不是路由器端口，添加]{style="font-family:宋体"}

[[Delete the port *port* from router port list]{lang="EN-US"}]{#struct_0_17007_x1341_x465320319}

[[从路由器端口列表中删除路由器端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_1976443108}*[port]{lang="EN-US"}*

[[Delete the port *port* from all static group]{lang="EN-US"}]{#struct_0_17007_x1341_1674544904}

[[将成员端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1132263729}*[port]{lang="EN-US"}*[从所有静态组表项中删除]{style="font-family:宋体"}

[[Clear all Static group on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1749187010}

[[清除]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1265462307}[VLAN]{lang="EN-US"}[内所有静态组表项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[debugging igmp-snooping packet]{lang="EN-US"}]{#struct_0_17007_x1341_1674610440}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1308272182}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_781530304}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1315009167}

[[Succeed in forwarding IGMP packet to port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x2091784701}

[[成功发送]{style="font-family:宋体"}]{#struct_0_17007_x1341_x243242680}[IGMP]{lang="EN-US"}[报文到]{style="font-family:宋体"}[VLAN *vlan*]{lang="EN-US"}[上的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*

[[Succeed in broadcasting the packet on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x990173330}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674675976}[VLAN *vlan*]{lang="EN-US"}[内成功广播报文]{style="font-family:宋体"}

[[Succeed in delivering up packet to IP]{lang="EN-US"}]{#struct_0_17007_x1341_435720848}

[[将报文上送]{style="font-family:宋体"}]{#struct_0_17007_x1341_1017099552}[IP]{lang="EN-US"}[层成功]{style="font-family:宋体"}

[[Receive IGMPv*n* version general query packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1145648485}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1111746676}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[通用查询报文]{style="font-family:宋体"}

[[Receive IGMP group specific query packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674741512}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_402112521}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[特定组查询报文]{style="font-family:宋体"}

[[Receive IGMPv3 group specific query packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_734380202}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1576779232}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[特定组查询报文]{style="font-family:宋体"}

[[Receive IGMPv*n* report packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1575948686}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1535414031}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报告报文]{style="font-family:宋体"}

[[Receive IGMP leave packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1674807048}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_778926857}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[离开报文]{style="font-family:宋体"}

[[Receive PIMv1 or DVMRP packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_80525528}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1661807842}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取]{style="font-family:宋体"}[PIMv1]{lang="EN-US"}[或]{style="font-family:宋体"}[DVMRP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[The version of IGMP packet that receive from port *port* on *vlan* is higher than the version on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x643529980}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673824008}[VLAN *vlan*]{lang="EN-US"}[上获取的报文版本高于]{style="font-family:宋体"}[VLAN *vlan*]{lang="EN-US"}[版本]{style="font-family:宋体"}

[[The PIM packet which receive from port *port* on *vlan* is not hello report or is fragment]{lang="EN-US"}]{#struct_0_17007_x1341_x1429404054}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1264553680}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取的]{style="font-family:宋体"}[PIM]{lang="EN-US"}[报文不是]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文或]{style="font-family:宋体"}[PIM]{lang="EN-US"}[分片报文]{style="font-family:宋体"}

[[Receive PIMv2 Hello packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1031229182}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673889544}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取到]{style="font-family:宋体"}[PIMv2 Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Receive CBT packet from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_147135119}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_x354828152}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取到]{style="font-family:宋体"}[CBT]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Deal with the IGMP/PIMv2/CBT packet which receive from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1227647008}

[[处理从]{style="font-family:宋体"}]{#struct_0_17007_x1341_189477464}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取到的]{style="font-family:宋体"}[IGMP/PIMv2/CBT]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Forward the group and source specific query packet on port which receive from port *port* on *vlan*, ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_1674348293}

[[转发从]{style="font-family:宋体"}]{#struct_0_17007_x1341_x710963128}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[上获取到的特定源组查询报文]{style="font-family:宋体"}

[[Main slot broadcast the general query packet which receive from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1452313294}

[[主板广播从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674413829}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取到通用查询报文]{style="font-family:宋体"}

[[Forward the group specific query packet on port which receive from port *port* on *vlan*, the group address is *group*]{lang="EN-US"}]{#struct_0_17007_x1341_1216981279}

[[转发从]{style="font-family:宋体"}]{#struct_0_17007_x1341_x944271514}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取的组地址为]{style="font-family:宋体"}*[group]{lang="EN-US"}*[的特定组查询报文]{style="font-family:宋体"}

[[Forward the IGMP report packet on router port which destination IP address is *group* and source IP address is *source* that receive from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1247905094}

[[从路由器端口上转发从]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674479365}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取的（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报告报文]{style="font-family:宋体"}

[[Broadcast PIMv1 or DVMRP packet which receive from port *port* on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1099162867}

[[广播从]{style="font-family:宋体"}]{#struct_0_17007_x1341_540311225}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取的]{style="font-family:宋体"}[PIMv1]{lang="EN-US"}[或]{style="font-family:宋体"}[DVMRP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Send PIMv1 or DVMRP packet to IP]{lang="EN-US"}]{#struct_0_17007_x1341_x1325258354}

[[将]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674544901}[PIMv1/DVMRP]{lang="EN-US"}[报文上送]{style="font-family:宋体"}[IP]{lang="EN-US"}[层成功]{style="font-family:宋体"}

[[The version of IGMP packet is lower than version on *vlan*, the main slot broadcast it on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1132591409}

[[报文版本低于端口版本，主板在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1055200334}[VLAN *vlan*]{lang="EN-US"}[内广播]{style="font-family:宋体"}

[[The IGMP packet which receive from port *port* on *vlan* on Main slot, forward it locally]{lang="EN-US"}]{#struct_0_17007_x1341_1674610437}

[[从主板]{style="font-family:宋体"}]{#struct_0_17007_x1341_781202627}[VLAN *vlan*]{lang="EN-US"}[的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上获取报文，本地转发]{style="font-family:宋体"}

[[The IGMP packet version which receive from IGMP is higher than the version on *vlan*, broadcast it on *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1229269802}

[[报文版本高于端口版本，]{style="font-family:宋体"}]{#struct_0_17007_x1341_1525712630}[VLAN *vlan*]{lang="EN-US"}[内广播]{style="font-family:宋体"}

[[Receive Query packet from *vlan*, it needn\'t to maintain router port, only main slot deal with it]{lang="EN-US"}]{#struct_0_17007_x1341_1674675973}

[[从]{style="font-family:宋体"}]{#struct_0_17007_x1341_436048528}[VLAN *vlan*]{lang="EN-US"}[上获取查询报文，无需维护路由器端口，只有主板处理]{style="font-family:宋体"}

[[The IGMP packet which receive from IGMP on *vlan* on main slot, forward it locally]{lang="EN-US"}]{#struct_0_17007_x1341_x1388214708}

[[从主板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674741509}[VLAN *vlan*]{lang="EN-US"}[上获取的报文，本地转发]{style="font-family:宋体"}

[[Forward the IGMP packet locally]{lang="EN-US"}]{#struct_0_17007_x1341_401391626}

[[本地转发]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1705191411}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Send the IGMP packet up to IP]{lang="EN-US"}]{#struct_0_17007_x1341_1674807045}

[[上送报文至]{style="font-family:宋体"}]{#struct_0_17007_x1341_778074889}[IP]{lang="EN-US"}[层]{style="font-family:宋体"}

[[Receive Query packet from main slot]{lang="EN-US"}]{#struct_0_17007_x1341_x526600123}

[[从主板收到查询报文]{style="font-family:宋体"}]{#struct_0_17007_x1341_1818886551}

[[Host send IGMPv3(*mode*) packet to *port* with *group* and 0 source(s) on *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_1455034382}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1234522781}[内的模拟主机向端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[发送模式为]{style="font-family:宋体"}*[mode]{lang="EN-US"}*[的]{style="font-family:宋体"}[IGMPv3]{lang="EN-US"}[报告报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[debugging igmp-snooping sync]{lang="EN-US"}]{#struct_0_17007_x1341_1673824005}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1277149302}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1430256022}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_361881780}

[[Received a configuration message]{lang="EN-US"}]{#struct_0_17007_x1341_1694003157}

[[接收到配置信息]{style="font-family:宋体"}]{#struct_0_17007_x1341_1866857184}

[[Received a message to add/delete/cancel host slot]{lang="EN-US"}]{#struct_0_17007_x1341_x129662199}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_x32773417}[/]{lang="EN-US"}[删除]{style="font-family:宋体"}[/]{lang="EN-US"}[取消成员板]{style="font-family:宋体"}

[[Received a message to add/delete host ports]{lang="EN-US"}]{#struct_0_17007_x1341_1673889541}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_147331727}[/]{lang="EN-US"}[删除成员接口]{style="font-family:宋体"}

[[Received a message to add/delete router slot]{lang="EN-US"}]{#struct_0_17007_x1341_1054047280}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1583876916}[/]{lang="EN-US"}[删除路由板]{style="font-family:宋体"}

[[Received a message to add/delete router ports]{lang="EN-US"}]{#struct_0_17007_x1341_x1259299749}

[[添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674348294}[/]{lang="EN-US"}[删除路由接口]{style="font-family:宋体"}

[[Received a message to delete entry]{lang="EN-US"}]{#struct_0_17007_x1341_x710766520}

[[删除表项]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1456948237}

[[Receive message from master]{lang="EN-US"}]{#struct_0_17007_x1341_x1951938073}

[[接口板收到主板发的消息]{style="font-family:宋体"}]{#struct_0_17007_x1341_x387073778}

[[Main slot forward the IGMP packet to other IO slot]{lang="EN-US"}]{#struct_0_17007_x1341_1321455464}

[[主板发送]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674413830}[IGMP]{lang="EN-US"}[报文至接口板]{style="font-family:宋体"}

[[The IGMP packet which receive from port *port* on *vlan* on IO slot, send it to the main slot]{lang="EN-US"}]{#struct_0_17007_x1341_1216391456}

[[发送来自于]{style="font-family:宋体"}]{#struct_0_17007_x1341_x564293462}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[的接口板上的消息至主板]{style="font-family:宋体"}

[[Send the IGMP packet to IO slots]{lang="EN-US"}]{#struct_0_17007_x1341_x1012171156}

[[发送]{style="font-family:宋体"}]{#struct_0_17007_x1341_1468962883}[IGMP]{lang="EN-US"}[报文至接口板]{style="font-family:宋体"}

[[Receive IGMP packet from another slot]{lang="EN-US"}]{#struct_0_17007_x1341_1674479366}

[[从其它板收到]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1099097331}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[Synchronize vlan or vsi IGMP snooping disable message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x861371867}

[[同步]{style="font-family:宋体"}]{#struct_0_17007_x1341_1081709956}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[去使能信息到其它板]{style="font-family:宋体"}

[[Successfully set version on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_1674544902}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1132394801}[VLAN *vlan*]{lang="EN-US"}[的版本并同步到其它板]{style="font-family:宋体"}

[[Successfully set drop-unknown on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x1355444090}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1975711116}[VLAN *vlan*]{lang="EN-US"}[的未知报文丢弃并同步到其它板]{style="font-family:宋体"}

[[Successfully set host-aging-time on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x137383946}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674610438}[VLAN *vlan*]{lang="EN-US"}[的成员端口定时器并同步到其它板]{style="font-family:宋体"}

[[Successfully set router-aging-time on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_782054595}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_874757099}[VLAN *vlan*]{lang="EN-US"}[的路由端口定时器并同步到其它板]{style="font-family:宋体"}

[[Successfully set *n* on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x988324590}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674675974}[VLAN *vlan*]{lang="EN-US"}[的特定组查询时间间隔]{style="font-family:宋体"}*[n]{lang="EN-US"}*[并同步到其它板]{style="font-family:宋体"}

[[Successfully set max-response-time on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_435589776}

[[设置]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1975656861}[VLAN *vlan*]{lang="EN-US"}[的最大响应时间并同步到其它板]{style="font-family:宋体"}

[[Successfully recover global IGMP snooping disabled and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_471624902}

[[设置全局]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674741510}[IGMP]{lang="EN-US"}[去使能并同步到其它板]{style="font-family:宋体"}

[[Successfully recover default entry limit globally]{lang="EN-US"}]{#struct_0_17007_x1341_401981449}

[[恢复全局表项数目限制]{style="font-family:宋体"}]{#struct_0_17007_x1341_208912671}

[[Successfully recover default drop-unknown globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x1666427963}

[[恢复默认的全局未知组播丢弃并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1674807046}

[[Successfully recover default host-aging-time globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_778271497}

[[恢复默认的全局成员端口定时器并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_473182095}

[[Successfully recover default router-aging-time globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_1673824006}

[[恢复默认的全局路由端口定时器并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1430321558}

[[Successfully recover default *n* globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x714715144}

[[恢复默认的全局查询时间]{style="font-family:宋体"}]{#struct_0_17007_x1341_1673889542}*[n]{lang="EN-US"}*[并同步到其它板]{style="font-family:宋体"}

[[Successfully recover default max-response-time globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_147528335}

[[恢复默认的全局最大查询时间并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1697753575}

[[Successfully recover default fast-leave globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_1778776691}

[[恢复默认的全局快速离开并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698304698}

[[Successfully recover default group-policy globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_1170077766}

[[恢复默认的全局组过滤并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1641839636}

[[Successfully recover default overflow-replace globally and synchronize message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698239162}

[[恢复默认的全局组替换并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x753071095}

[[Successfully recover IGMP snooping disable on *vlan* and send message to other slots synchronize configuration]{lang="EN-US"}]{#struct_0_17007_x1341_x2138800894}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698173626}[VLAN *vlan*]{lang="EN-US"}[上去使能并同步到其它板]{style="font-family:宋体"}

[[Successfully recover IGMP snooping drop-unknown disable on *vlan* and send message to other slots synchronize configuration]{lang="EN-US"}]{#struct_0_17007_x1341_x741947438}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_1798556332}[VLAN *vlan*]{lang="EN-US"}[上未知组播丢弃并同步到其它板]{style="font-family:宋体"}

[[Successfully recover IGMP snooping Version on *vlan* and send message to other slots synchronize configuration]{lang="EN-US"}]{#struct_0_17007_x1341_x698108090}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_x365264704}[VLAN *vlan*]{lang="EN-US"}[上版本并同步到其它板]{style="font-family:宋体"}

[[Successfully recover IGMP snooping router-aging-time on *vlan* and send message to other slots synchronize configuration]{lang="EN-US"}]{#struct_0_17007_x1341_713159438}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698042554}[VLAN *vlan*]{lang="EN-US"}[上路由端口定时器并同步到其它板]{style="font-family:宋体"}

[[Successfully recover IGMP snooping max-response-time on *vlan* and send message to other slots synchronize configuration]{lang="EN-US"}]{#struct_0_17007_x1341_411057159}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_x615810143}[VLAN *vlan*]{lang="EN-US"}[上最大响应时间并同步到其它板]{style="font-family:宋体"}

[[Successfully set *n* on *vlan* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x697977018}

[[恢复]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1378772189}[VLAN *vlan*]{lang="EN-US"}[上特定组查询时间间隔]{style="font-family:宋体"}*[n]{lang="EN-US"}*[并同步到其它板]{style="font-family:宋体"}

[[Successfully process Port fast-leave message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_571167556}

[[恢复端口快速离开并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697911482}

[[Successfully process Port group-policy message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_976138742}

[[恢复端口组过滤并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x74603983}

[[Successfully process Port group-limit message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x697845946}

[[恢复端口组数目限制并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1026653067}

[[Successfully process Port overflow-replace message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698828986}

[[恢复端口组替换并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x788299304}

[[Synchronize enable or disable IGMP snooping globally message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x1477569526}

[[同步]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698763450}[IGMP]{lang="EN-US"}[的使能或去使能到其它板]{style="font-family:宋体"}

[[Successfully process global entry limit message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x357447559}

[[处理全局表项数目并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_706200143}

[[Synchronize drop-unknown globally message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698304697}

[[处理全局未知报文丢弃并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_1169356870}

[[Successfully process global host-aging-time message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698239161}

[[处理全局成员端口定时器并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x753136631}

[[Successfully process global router-aging-time message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698173625}

[[处理全局路由器端口定时器并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x742012974}

[[Successfully set *n* and synchronize to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x1839913166}

[[处理全局查询时间间隔]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698108089}*[n]{lang="EN-US"}*[并同步到其它板]{style="font-family:宋体"}

[[Successfully process global max-response-time message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x364805951}

[[处理全局最大响应时间并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698042553}

[[Successfully process global fast-leave message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_410860551}

[[处理全局快速离开并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1318431051}

[[Successfully process global group-policy message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x697977017}

[[处理全局组过滤并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1378313437}

[[Successfully process global overflow-replace message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x697911481}

[[处理全局组替换并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_976335350}

[[synchronize configure debug message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x697845945}

[[同步配置]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1026849675}[debug]{lang="EN-US"}[信息到其它板]{style="font-family:宋体"}

[[Successfully process Port fast-leave message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x698828985}

[[处理端口快速离开并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x788233768}

[[Successfully process Port group-limit message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_1224789926}

[[处理全局组数目并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698763449}

[[Successfully process Port group-policy message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x358037382}

[[处理全局组过滤并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698304700}

[[Successfully process Port overflow-replace message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x786761649}

[[处理全局快速离开并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698239164}

[[Successfully process static host port message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x752940023}

[[处理静态成员端口的状态配置信息并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698173628}

[[Successfully process static router port message and sync to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x742340654}

[[处理静态路由器端口的状态配置信息并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698108092}

[[Synchronize configure resetting statistics message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_x365133632}

[[同步清空统计信息配置并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698042556}

[[Synchronize configure resetting groups message to other slots]{lang="EN-US"}]{#struct_0_17007_x1341_411188231}

[[同步清空组信息配置并同步到其它板]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697977020}

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[debugging igmp-snooping timer]{lang="EN-US"}]{#struct_0_17007_x1341_x1378247898}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1287720566}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_112046071}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_146617179}

[[Succeed in creating router port timer, ]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_1048365121}[ seconds for port *port* on *vlan*]{lang="EN-US"}

[[为]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1274747350}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[创建路由器端口定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Succeed in resizing router port timer, ]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_x340131335}[ seconds, for port *port* on *vlan*]{lang="EN-US"}

[[为]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697911484}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[调整路由器端口定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Create host port timer, ]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_976007670}[ seconds, for port:*port,* dynamic group:]{lang="EN-US"}[ (*source*, *group*)]{lang="EN-US"}[ on *vlan*]{lang="EN-US"}

[[为]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1663619851}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[动态组]{style="font-family:宋体"}[（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）创建成员端口定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Resize host port timer, ]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_1820981527}[ seconds, for port:*port*, dynamic group:]{lang="EN-US"}[ (*source*, *group*)]{lang="EN-US"}[ on *vlan*]{lang="EN-US"}

[[为]{style="font-family:宋体"}]{#struct_0_17007_x1341_x307058862}[VLAN *vlan*]{lang="EN-US"}[上端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[动态组]{style="font-family:宋体"}[（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）调整成员端口定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Succeed in creating v]{lang="EN-US"}*[n]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_17007_x1341_x1717856940}[host port timer, *m* seconds, for port *port*]{lang="EN-US"}

[[为端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697845948}*[port]{lang="EN-US"}*[创建版本为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的成员端口定时器，时间为]{style="font-family:宋体"}*[m]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Succeed in resizing v]{lang="EN-US"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_x1027570571}[ host port timer, *m* seconds, for port *port*]{lang="EN-US"}

[[为端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_710889983}*[port]{lang="EN-US"}*[调整版本为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[的成员端口定时器，时间为]{style="font-family:宋体"}*[m]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Down host port timer, *n* seconds, for port *port*]{lang="EN-US"}]{#struct_0_17007_x1341_943072476}

[[对端口]{style="font-family:宋体"}]{#struct_0_17007_x1341_x950706084}*[port]{lang="EN-US"}*[关掉成员端口定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Update v]{lang="NO-BOK"}]{#struct_0_17007_x1341_x698828988}*[n]{lang="NO-BOK"}*[ host port timer]{lang="NO-BOK"}

[[更新版本]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_17007_x1341_x787381800}[的成员端口定时器]{style="font-family:宋体"}

[[The host port *port* times out for dynamic group ]{lang="EN-US"}[(*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x1356285629}[ on *vlan*]{lang="EN-US"}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1621142280}[上对动态组]{style="font-family:宋体"}[（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[超时]{style="font-family:宋体"}

[[Successfully create query information record timer]{lang="EN-US"}]{#struct_0_17007_x1341_1141107228}

[[成功创建查询信息记录定时器]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698763452}

[[Successfully resize query information record timer]{lang="EN-US"}]{#struct_0_17007_x1341_x357578631}

[[成功调整查询信息记录定时器]{style="font-family:宋体"}]{#struct_0_17007_x1341_635803457}

[[Created resend timer, *n* ms]{lang="EN-US"}]{#struct_0_17007_x1341_481506591}

[[创建重传定时器，时间为]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698304699}*[n]{lang="EN-US"}*[毫秒]{style="font-family:宋体"}

[[Create timer to IP fail list, *n* seconds]{lang="EN-US"}]{#struct_0_17007_x1341_1170012230}

[[对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_17007_x1341_475864638}[下驱动失败创建定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Create timer to MAC fail list, *n* seconds.]{lang="EN-US"}]{#struct_0_17007_x1341_x586590935}

[[对]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_17007_x1341_x698239163}[下驱动失败创建定时器，时间为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Successfully create IGMPv1 query present timer on *vlan*, *n* seconds.]{lang="EN-US"}]{#struct_0_17007_x1341_1454772236}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1098761347}[VLAN *vlan*]{lang="EN-US"}[内将]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[查询存在定时器创建为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[Successfully resize IGMPv1 query present timer on *vlan*, *n* seconds.]{lang="EN-US"}]{#struct_0_17007_x1341_1454837772}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1454903308}[VLAN *vlan*]{lang="EN-US"}[内将]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[查询存在定时器调整为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[秒]{style="font-family:宋体"}

[[The IGMPv1 query present times out on *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_x1490893287}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1454968844}[内的]{style="font-family:宋体"}[IGMPv1]{lang="EN-US"}[查询存在定时器超时]{style="font-family:宋体"}

[[Successfully create host response timer, 10 seconds on group *group* of port *port* in *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_x724580154}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_1455034380}[VLAN *vlan*]{lang="EN-US"}[内的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上为组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[将查询响应定时器创建为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[Successfully update host response timer, 10 seconds on group *group* of port *port* in *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_1455099916}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x736668339}[VLAN *vlan*]{lang="EN-US"}[内的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上为组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[将查询响应定时器更新为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[Host response times out on group *group* of port *port* in *vlan*.]{lang="EN-US"}]{#struct_0_17007_x1341_1455165452}

[[VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1454182412}[内的端口]{style="font-family:宋体"}*[port]{lang="EN-US"}*[上组]{style="font-family:宋体"}*[group]{lang="EN-US"}*[的查询响应定时器超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x753005559}

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x1725257062}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[接口驱动调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp-snooping entry]{lang="EN-US"}]{#struct_0_17007_x1341_x831838036}

[\*Sep 15 11:43:28:565 2011 Sysname MCS/7/ENTRY: -MDC=1; Delete MAC entry 0100-5e01-0101 from driver. (G156098)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_2114029552}*[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内从驱动中删除二层]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_1819420902}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp-snooping event]{lang="EN-US"}]{#struct_0_17007_x1341_x1669069663}

[\*Sep 15 11:46:06:924 2011 Sysname MCS/7/EVENT: -MDC=1; Successfully enable IGMP snooping on VLAN 4. (G174304)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x1750747882}*[在]{style="font-family:宋体"}[VLAN 4]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_742984257}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[组播组调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp-snooping group]{lang="EN-US"}]{#struct_0_17007_x1341_x698173627}

[\*Sep 15 11:47:41:455 2011 Sysname MCS/7/GROUP: -MDC=1; Create Dynamic group (0.0.0.0, 225.1.1.1) on VLAN 2, add host port GE1/0/1. (G091840)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x741881902}*[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内创建动态表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[），添加主机端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x2085779860}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[报文调试]{style="font-family:宋体"}[信息开关。]{style="font-family:
宋体"}

[[\<Sysname\> debugging igmp-snooping packet]{lang="EN-US"}]{#struct_0_17007_x1341_x96281299}

[\*Sep 15 11:47:41:455 2011 Sysname MCS/7/PACKET: -MDC=1; Receive IGMPv2 report packet from port GE1/0/1 on VLAN 2. (G162625)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_1134103301}*[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上收到]{style="font-family:宋体"}[IGMPv2]{lang="EN-US"}[成员关系报告报文]{style="font-family:宋体"}*

[[\*Sep 15 13:35:00:846 2011 Sysname MCS/7/PACKET: -MDC=1; Forward the IGMP membership packet on router port which destination IP address is 224.0.0.1 and source IP address is 0.0.0.0 that receive from port GE1/0/1 on VLAN 2. (G163447)]{lang="EN-US"}]{#struct_0_17007_x1341_1192266135}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x1721744862}*[通过]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的端口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送源地址为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[、目的地址为]{style="font-family:宋体"}[224.0.0.1]{lang="EN-US"}[的]{style="font-family:宋体"}[IGMP]{lang="EN-US"}[报文]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x1131047417}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[板间同步调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp-snooping sync]{lang="EN-US"}]{#struct_0_17007_x1341_x698108091}

[\*Sep 15 13:40:04:692 2011 Sysname MCS/7/SYNC: -MDC=1; synchronize configure debug message to other board. (G1710245)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x365330240}*[通知其它板打开调试信息]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x53731097}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[定时器调试]{style="font-family:宋体"}[信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp-snooping timer]{lang="EN-US"}]{#struct_0_17007_x1341_753656394}

[\*Sep 15 13:42:03:448 2011 Sysname MCS/7/TIMER: -MDC=1; Successfully create query information record timer. (G092699)]{lang="EN-US"}

[\*Sep 15 13:42:03:449 2011 Sysname MCS/7/TIMER: -MDC=1; Succeed in creating router port timer, 105 seconds, for port GE1/0/1 on VLAN 1. (G091031)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_37318568}*[创建路由器端口，并将其老化时间设置为]{style="font-family:宋体"}[105]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\*Sep 15 13:35:00:845 2011 Sysname MCS/7/TIMER: -MDC=1; Down host port timer, 2 seconds, for port GE1/0/1. (G091336)]{lang="EN-US"}]{#struct_0_17007_x1341_x1854071842}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x2087593755}*[收到离开报文，并将端口老化时间设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x698042555}[在设备上使能]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[，打开]{style="font-family:宋体"}[IGMP Snooping]{lang="EN-US"}[状态机调试]{style="font-family:宋体"}[信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging igmp -snooping fsm]{lang="EN-US"}]{#struct_0_17007_x1341_410991623}

[\*Sep 15 13:42:10:403 2011 Sysname MCS/7/FSM: -MDC=1; Notified add host self slot 0 of (0.0.0.0,239.255.255.250) to other on VLAN 2. (G061062)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x1324943659}*[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[上通知其它板添加成员板]{style="font-family:宋体"}*

::: {#-1572468486 .myid}
[]{#_Toc404789222}[]{#struct_0_17007_x1341_x1850232975}

**IGMP Snooping \-- IGMP Snooping调试命令 \-- debugging l2mf**

------------------------------------------------------------------------

[[【命令】]{style="font-family:黑体"}]{#struct_0_17007_x1341_1876957991}

[**[debugging l2mf ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **group** \| **msg** }]{lang="EN-US"}]{#struct_0_17007_x1341_x1518044432}

[**[undo debugging l2mf ]{lang="EN-US"}**[{ **all** \| **error** \| **event** \| **group** \| **msg** }]{lang="EN-US"}]{#struct_0_17007_x1341_x1713718280}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17007_x1341_1674113462}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697977019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1378706653}

[[network-admin]{lang="EN-US"}]{#struct_0_17007_x1341_1771282332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17007_x1341_x718528899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x891193508}

[**[all]{lang="EN-US"}**]{#struct_0_17007_x1341_1915275217}[：表示]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[（]{style="font-family:宋体"}[Layer-2 Multicast Forwarding]{lang="EN-US"}[，二层组播转发）所有调试信息开关。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_17007_x1341_x1952816329}[：表示]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[错误调试信息开关。]{style="font-family:宋体"}

[**[event]{lang="EN-US"}**]{#struct_0_17007_x1341_237976276}[：表示]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**]{#struct_0_17007_x1341_187437475}[：表示]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[组播组调试信息开关。]{style="font-family:宋体"}

[**[msg]{lang="EN-US"}**]{#struct_0_17007_x1341_x697911483}[：表示]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_17007_x1341_976204278}

[**[debugging l2mf]{lang="EN-US"}**]{#struct_0_17007_x1341_1344690833}[命令用来打开]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}**[undo debugging l2mf]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[调试信息开关。]{style="font-family:宋体"}

[[缺省情况下，]{style="font-family:宋体"}[L2MF]{lang="EN-US"}]{#struct_0_17007_x1341_1816806289}[调试信息开关处于关闭状态。]{style="font-family:宋体"}

[[表1-9 ]{lang="EN-US"}[debugging l2mf error]{lang="EN-US"}]{#struct_0_17007_x1341_x692064933}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1261551094}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_2005006255}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1975517020}

[[Failed flush set router port message (*source, group*) to driver in VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x697845947}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1026718603}[VLAN *vlan*]{lang="EN-US"}[中下刷路由器端口信息（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）到驱动失败]{style="font-family:宋体"}

[[The port extend information is invalid when add port]{lang="EN-US"}]{#struct_0_17007_x1341_906057975}

[[在添加端口时端口的扩展信息无效]{style="font-family:宋体"}]{#struct_0_17007_x1341_x2137046767}

[[(*source, group*) has been existent in VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1118952179}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1147351825}[VLAN *vlan*]{lang="EN-US"}[中（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）已存在]{style="font-family:宋体"}

[[Can\'t find (*source, group*) in VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x698828987}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x788364840}[VLAN *vlan*]{lang="EN-US"}[中未能找到（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[MAC entry *mac* has been existent in VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_x1982064880}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_194879938}[VLAN *vlan*]{lang="EN-US"}[中]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[已存在]{style="font-family:宋体"}

[[MAC entry *mac* can\'t be found in VLAN *vlan*]{lang="EN-US"}]{#struct_0_17007_x1341_1341742304}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_505633343}[VLAN *vlan*]{lang="EN-US"}[中未能找到]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Failed to parse received message]{lang="EN-US"}]{#struct_0_17007_x1341_x698763451}

[[解析收到的消息失败]{style="font-family:宋体"}]{#struct_0_17007_x1341_x357513095}

[ ]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[debugging l2mf event]{lang="EN-US"}]{#struct_0_17007_x1341_1825281186}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1259519190}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_1394911413}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_1525015276}

[[Port is exisit when add port for entry ]{lang="EN-US"}]{#struct_0_17007_x1341_775673365}[(]{lang="EN-US"}[0.0.0.0, 0.0.0.0]{lang="EN-US"}[)]{lang="EN-US"}[ in]{lang="EN-US"}[ VLAN *vlan*]{lang="EN-US"}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698304702}[VLAN *vlan*]{lang="EN-US"}[中为表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[）添加端口时，该端口已存在]{style="font-family:宋体"}

[[Add port for entry ]{lang="EN-US"}]{#struct_0_17007_x1341_x786630577}[(]{lang="EN-US"}[0.0.0.0, 0.0.0.0]{lang="EN-US"}[) ]{lang="EN-US"}[in]{lang="EN-US"}[ ]{lang="EN-US"}[VLAN]{lang="EN-US"}[ *vlan*]{lang="EN-US"}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_972113198}[VLAN *vlan*]{lang="EN-US"}[中为表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[）添加端口]{style="font-family:宋体"}

[[Delete port for entry ]{lang="EN-US"}]{#struct_0_17007_x1341_x1830500757}[(]{lang="EN-US"}[0.0.0.0, 0.0.0.0]{lang="EN-US"}[)]{lang="EN-US"}[ in ]{lang="EN-US"}[VLAN *vlan*]{lang="EN-US"}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1274036605}[VLAN *vlan*]{lang="EN-US"}[中为表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[）删除端口]{style="font-family:宋体"}

[[Add slot *slot* for entry ]{lang="EN-US"}]{#struct_0_17007_x1341_995409516}[(]{lang="EN-US"}[0.0.0.0, 0.0.0.0]{lang="EN-US"}[)]{lang="EN-US"}[ in ]{lang="EN-US"}[VLAN]{lang="EN-US"}*[ ]{lang="EN-US"}[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x698239166}[VLAN *vlan*]{lang="EN-US"}[中为表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[）添加板]{style="font-family:宋体"}*[slot]{lang="EN-US"}*

[ ]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[debugging l2mf group]{lang="EN-US"}]{#struct_0_17007_x1341_x752808951}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1266491958}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_989239265}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x1741517409}

[[The *number* ports are added/deleted to the entry (*source, group*) of interface *interface*, and it return *value*]{lang="EN-US"}]{#struct_0_17007_x1341_1797511195}

[[在表项（]{style="font-family:宋体"}]{#struct_0_17007_x1341_x811605131}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}[的接口]{style="font-family:宋体"}*[interface]{lang="EN-US"}*[中添加]{style="font-family:宋体"}[/]{lang="EN-US"}[删除了]{style="font-family:宋体"}*[number]{lang="EN-US"}*[个端口，并返回值]{style="font-family:宋体"}*[value]{lang="EN-US"}*

[[Add entry (*source, group*) in ]{lang="EN-US"}]{#struct_0_17007_x1341_x698173630}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x741816367}[VLAN *vlan*]{lang="EN-US"}[中添加表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add MAC entry *mac* in ]{lang="EN-US"}]{#struct_0_17007_x1341_x2120133075}[VLAN]{lang="EN-US"}[ *vlan*]{lang="EN-US"}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1814490390}[VLAN *vlan*]{lang="EN-US"}[中添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*

[[Delete entry (*source, group*) in ]{lang="EN-US"}]{#struct_0_17007_x1341_516406943}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_2063209100}[VLAN *vlan*]{lang="EN-US"}[中删除表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）]{style="font-family:宋体"}

[[Add slot for (*source, group*) in ]{lang="EN-US"}]{#struct_0_17007_x1341_x698108094}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x365526848}[VLAN *vlan*]{lang="EN-US"}[中为表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）添加板]{style="font-family:宋体"}

[[Add port for MAC entry *mac* in ]{lang="EN-US"}]{#struct_0_17007_x1341_1529863371}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x1484156753}[VLAN *vlan*]{lang="EN-US"}[中为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[添加端口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[debugging l2mf msg]{lang="EN-US"}]{#struct_0_17007_x1341_x1490659784}[命令输出信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1262677078}[[字段]{style="font-family:黑体"}]{#struct_0_17007_x1341_1570764667}

[[描述]{style="font-family:黑体"}]{#struct_0_17007_x1341_x698042558}

[[Flush set router port message (*source*, *group*) to driver in ]{lang="EN-US"}]{#struct_0_17007_x1341_410270727}[VLAN]{lang="EN-US"}*[ ]{lang="EN-US"}[vlan]{lang="EN-US"}*[ with port]{lang="EN-US"}

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x511546082}[VLAN *vlan*]{lang="EN-US"}[中拷贝路由器端口信息（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）并下刷驱动]{style="font-family:宋体"}

[[Flush add entry message (*source*, *group*) to driver in ]{lang="EN-US"}]{#struct_0_17007_x1341_x2076394565}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_320420607}[VLAN *vlan*]{lang="EN-US"}[中将表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的]{style="font-family:宋体"}[信息下]{style="font-family:宋体"}[刷]{style="font-family:宋体"}[驱动]{style="font-family:宋体"}

[[Flush add entry Mac message (*mac*) to driver in ]{lang="EN-US"}]{#struct_0_17007_x1341_1007027289}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697977022}[VLAN *vlan*]{lang="EN-US"}[中将]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[的]{style="font-family:宋体"}[信息下刷驱动]{style="font-family:宋体"}

[[Flush L2 multicast configuration message to driver with command]{lang="EN-US"}]{#struct_0_17007_x1341_x1378116826}

[[将二层组播配置信息下刷驱动]{style="font-family:宋体"}]{#struct_0_17007_x1341_1231619442}

[[Save message to Kernel]{lang="EN-US"}]{#struct_0_17007_x1341_x2022030062}

[[保存信息到内核]{style="font-family:宋体"}]{#struct_0_17007_x1341_x207903252}

[[Cache message to fail list]{lang="EN-US"}]{#struct_0_17007_x1341_x697911486}

[[写队列失败]{style="font-family:宋体"}]{#struct_0_17007_x1341_975876598}

[[Process add entry message for entry (*source*, *group*)]{lang="EN-US"}]{#struct_0_17007_x1341_x245302328}

[[处理添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_1242048441}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}*[source]{lang="EN-US"}*[，]{style="font-family:宋体"}*[group]{lang="EN-US"}*[）的消息]{style="font-family:宋体"}

[[Process add entry message for MAC entry *mac*]{lang="EN-US"}]{#struct_0_17007_x1341_x1402214222}

[[处理添加]{style="font-family:宋体"}]{#struct_0_17007_x1341_x697845950}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}*[mac]{lang="EN-US"}*[的消息]{style="font-family:宋体"}

[[Send finish packet message to MCS]{lang="EN-US"}]{#struct_0_17007_x1341_x1027046282}

[[完成向]{style="font-family:宋体"}]{#struct_0_17007_x1341_731228122}[MCS]{lang="EN-US"}[进程打包发送消息]{style="font-family:宋体"}

[[Send L3 multicast enable message to MCS in ]{lang="EN-US"}]{#struct_0_17007_x1341_x1693223228}[VLAN]{lang="EN-US"}[ ]{lang="EN-US"}*[vlan]{lang="EN-US"}*

[[在]{style="font-family:宋体"}]{#struct_0_17007_x1341_70333812}[VLAN *vlan*]{lang="EN-US"}[中向]{style="font-family:宋体"}[MCS]{lang="EN-US"}[进程发送三层组播使能的消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17007_x1341_x698828990}

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x787906087}[打开]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[事件调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2mf event]{lang="EN-US"}]{#struct_0_17007_x1341_x174117236}

[\*Jun  4 12:55:19:912 2012 Sysname L2MF/7/EVENT: -MDC=1; Delete port for entry (0.0.0.0, 0.0.0.0) in VLAN 2. (A171255)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_608520450}*[在]{style="font-family:宋体"}[VLAN ]{lang="EN-US"}[2]{lang="EN-US"}[中为表项（]{style="font-family:
宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:
宋体"}[0.0.0.0]{lang="EN-US"}[）删除端口]{style="font-family:
宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x218158057}[打开]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[组播组调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2mf group]{lang="EN-US"}]{#struct_0_17007_x1341_x1932560657}

[\*Jun  4 12:50:41:191 2012 Sysname L2MF/7/GROUP: -MDC=1; Add MAC entry 0100-5e01-0101 in VLAN 1. (A151783)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x1381182975}*[在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}[0100-5E01-0101]{lang="EN-US"}*

[[\*Jun  4 12:50:41:191 2012 Sysname L2MF/7/GROUP: -MDC=1; Add entry (0.0.0.0, 225.1.1.1) in VLAN 1. (A151071)]{lang="EN-US"}]{#struct_0_17007_x1341_x698763454}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x357185415}*[在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中添加表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[）]{style="font-family:宋体"}*

[[\# ]{lang="EN-US"}]{#struct_0_17007_x1341_x112481536}[打开]{style="font-family:宋体"}[L2MF]{lang="EN-US"}[消息调试信息开关。]{style="font-family:宋体"}

[[\<Sysname\> debugging l2mf msg]{lang="EN-US"}]{#struct_0_17007_x1341_x355574269}

[\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Flush add entry Mac message (0100-5e01-0101) to driver in VLAN 1. (A141939)]{lang="EN-US"}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x784982016}*[在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中]{style="font-family:宋体"}[将]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}[0100-5E01-0101]{lang="EN-US"}[的信息下刷驱动]{style="font-family:宋体"}*

[[\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Save message to Kernel. (A131801)]{lang="EN-US"}]{#struct_0_17007_x1341_760699927}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x1016126272}*[保存信息到内核]{style="font-family:宋体"}*

[[\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Process add entry message for MAC entry 0100-5e01-0101  (A18873)]{lang="EN-US"}]{#struct_0_17007_x1341_x897276505}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x844689735}*[处理添加]{style="font-family:宋体"}[MAC]{lang="EN-US"}[表项]{style="font-family:宋体"}[0100-5E01-0101]{lang="EN-US"}[的消息]{style="font-family:宋体"}*

[[\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Flush add entry message (0.0.0.0, 225.1.1.1) to driver in VLAN 1. (A141815)]{lang="EN-US"}]{#struct_0_17007_x1341_x698304701}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_x786827185}*[在]{style="font-family:宋体"}[VLAN 1]{lang="EN-US"}[中]{style="font-family:宋体"}[将]{style="font-family:宋体"}[表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[）的信息下刷驱动]{style="font-family:宋体"}*

[[\*Jun  4 12:48:53:840 2012 Sysname L2MF/7/MESSAGE: -MDC=1; Process add entry message for entry (0.0.0.0, 225.1.1.1). (A18815)]{lang="EN-US"}]{#struct_0_17007_x1341_x189488314}

[*[// ]{lang="EN-US"}*]{#struct_0_17007_x1341_1654824977}*[处理]{style="font-family:宋体"}[添加]{style="font-family:宋体"}[IP]{lang="EN-US"}[表项（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，]{style="font-family:宋体"}[225.1.1.1]{lang="EN-US"}[）的消息]{style="font-family:宋体"}*
