::: {#1763009166 .myid}
[]{#_Toc95362256}[]{#_Toc37217646}[]{#_Toc30751576}[]{#_Toc15982605}[]{#_Toc6373264}[]{#_Toc298249418}[]{#_Ref135293160}[]{#_Toc95362249}[]{#_Toc404786502}[]{#struct_0_x9830_11811_1262930670}[]{#_Toc306705052}[]{#_Toc295825272}

**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding aging-time**

------------------------------------------------------------------------

[**[display ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_x1647422808}[命令用来显示快速转发表项的老化时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_195123570}

[**[display ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_2083315276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x859393710}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_580686936}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x2040321297}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_x1236139434}

[[network-operator]{lang="EN-US"}]{#struct_0_x9830_11811_897171116}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_209639916}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9830_11811_x943640044}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_220533140}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_195058034}[显示快速转发表项的老化时间。]{style="font-family:宋体"}

[[\<Sysname\> display ip fast-forwarding aging-time]{lang="EN-US"}]{#struct_0_x9830_11811_x1838668694}

[ Aging time: 30s]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip fast-forwarding aging-time]{lang="EN-US"}]{#struct_0_x9830_11811_1091394375}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1175292578}[[字段]{style="font-family:黑体"}]{#struct_0_x9830_11811_151530299}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9830_11811_843848712}

[[Aging time]{lang="EN-US"}]{#struct_0_x9830_11811_18665581}

[[快转表项的老化时间]{style="font-family:宋体"}]{#struct_0_x9830_11811_1005887284}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_736133307}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_196041074}

::: {#1632687427 .myid}
[]{#_Toc404786503}[]{#struct_0_x9830_11811_85873476}

**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding cache**

------------------------------------------------------------------------

[**[display ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_1628620368}[命令用来显示快速转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2106602391}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9830_11811_1606364782}

[**[display ip fast-forwarding cache]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_x9830_11811_1358820976}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9830_11811_811082766}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip fast-forwarding cache]{lang="EN-US"}**[ \[ *ip-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_2131792979}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9830_11811_x1677987402}[模式：]{style="font-family:宋体"}

[**[display ip fast-forwarding cache]{lang="EN-US"}**[ \[ *ip-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_x78911283}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_195975538}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_x58532447}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1629558541}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_x1810966512}

[[network-operator]{lang="EN-US"}]{#struct_0_x9830_11811_1185104658}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_x1999287868}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9830_11811_x934048957}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x1838905726}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x9830_11811_1044984966}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的快速转发表信息。如果不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，将显示所有快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_2117831090}[：显示指定单板的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x9830_11811_x594836726}[：显示指定成员设备的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x9830_11811_1913712771}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x1355542560}[：显示指定成员设备上指定单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_703793654}[：显示指定单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板的快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x9830_11811_1818035596}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的快速转发表信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x1715008903}

[**[display ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x1710018293}[命令用来显示快速转发表信息，包括每条数据流的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、源端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、目的端口号、协议号、输入接口号、输出接口号、内部标记等信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2087097186}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_834717882}[显示所有快速转发表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip fast-forwarding cache]{lang="EN-US"}]{#struct_0_x9830_11811_2117765554}

[Total number of fast-forwarding entries: 3]{lang="EN-US"}

[SIP            SPort DIP            DPort Pro Input_If   Output_If   Flg]{lang="EN-US"}

[7.0.0.13       68    8.0.0.1        67    17  GE1/0/3    GE1/0/1      5]{lang="EN-US"}

[8.0.0.1        67    7.0.0.13       68    17  GE1/0/1    GE1/0/3      5]{lang="EN-US"}

[8.0.0.1        8     7.0.0.13       0     1   GE1/0/2    GE1/0/3      5]{lang="EN-US"}

[]{#struct_0_x9830_11811_x1374595495}[[表1-2 ]{lang="EN-US"}[display ip fast-forwarding cache]{lang="EN-US"}]{#_Toc228073406}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1178491376}[[字段]{style="font-family:黑体"}]{#struct_0_x9830_11811_101268679}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9830_11811_x170004960}

[[Total number of fast-forwarding entries]{lang="EN-US"}]{#struct_0_x9830_11811_x1458318331}

[[快速转发表项数目]{style="font-family:宋体"}]{#struct_0_x9830_11811_x1755911361}

[[SIP]{lang="EN-US"}]{#struct_0_x9830_11811_x1914774741}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9830_11811_2117700018}[地址]{style="font-family:宋体"}

[[SPort]{lang="EN-US"}]{#struct_0_x9830_11811_2135554180}

[[源端口号]{style="font-family:宋体"}]{#struct_0_x9830_11811_1201681993}

[[DIP]{lang="EN-US"}]{#struct_0_x9830_11811_x1060530102}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9830_11811_x1362814396}[地址]{style="font-family:宋体"}

[[DPort]{lang="EN-US"}]{#struct_0_x9830_11811_x220199871}

[[目的端口号]{style="font-family:宋体"}]{#struct_0_x9830_11811_2117634482}

[[Pro]{lang="EN-US"}]{#struct_0_x9830_11811_x600126646}

[[协议号]{style="font-family:宋体"}]{#struct_0_x9830_11811_x953951728}

[[Input_If]{lang="EN-US"}]{#struct_0_x9830_11811_1136033361}

[[报文入接口类型和接口号（"]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x9830_11811_x2072409668}["表示接口存在但是该快速转发不涉及入接口，"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示接口不存在）]{style="font-family:宋体"}

[[Output_If]{lang="EN-US"}]{#struct_0_x9830_11811_x1626949794}

[[报文出接口类型和接口号（"]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x9830_11811_2117568946}["表示接口存在但是该快速转发不涉及出接口，"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示接口不存在）]{style="font-family:宋体"}

[[Flg]{lang="EN-US"}]{#struct_0_x9830_11811_1679072675}

[[内部标记，主要是标记分片等内部操作信息]{style="font-family:宋体"}]{#struct_0_x9830_11811_x1835000253}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1067225525}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x139899698}

::: {#1009758923 .myid}
[]{#_Ref135293171}[]{#_Toc404786504}[]{#struct_0_x9830_11811_x326298789}[]{#_Toc298249419}[]{#_Toc233801336}[]{#_Toc234730244}[]{#_Toc234742408}

**快速转发 \-- 快速转发配置命令 \-- display ip fast-forwarding fragcache**

------------------------------------------------------------------------

[**[display ip fast-forwarding fragcache]{lang="EN-US"}**]{#struct_0_x9830_11811_2117503410}[命令用来显示分片报文快速转发表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1774689013}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9830_11811_1036458834}

[**[display ip fast-forwarding fragcache]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_x9830_11811_95992176}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9830_11811_x1162756491}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ip fast-forwarding fragcache]{lang="EN-US"}**[ \[ *ip-address* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_x1078866321}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9830_11811_2128255044}[模式：]{style="font-family:宋体"}

[**[display ip fast-forwarding fragcache]{lang="EN-US"}**[ \[ *ip-address* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_751880520}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_875907703}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_x199291299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2117437874}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_2097573314}

[[network-operator]{lang="EN-US"}]{#struct_0_x9830_11811_x1727861123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_x1685894949}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x9830_11811_x412429579}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x61734177}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x9830_11811_3562937}[：显示指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的分片报文快速转发表信息。如果不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，将显示所有分片报文快速转发表信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x205884413}[：显示指定单板的分片报文快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x9830_11811_x590560175}[：显示指定成员设备的分片报文快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示所有成员设备的分片报文快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_x9830_11811_x1265574814}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的分片报文快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的分片报文快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_2117372338}[：显示指定成员设备上指定单板的分片报文快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x1818661338}[：显示指定单板的分片报文快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板的分片报文快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x9830_11811_1818297740}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的分片报文快速转发表信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x1757868340}

[**[display ip fast-forwarding fragcache]{lang="EN-US"}**]{#struct_0_x9830_11811_1031549459}[命令用来显示分片报文快速转发表信息，包括分片报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、源端口号、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、目的端口号、协议号、输入接口号、分片]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{style="font-family:宋体"}[ID]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x1885322062}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_671425520}[显示所有分片报文快速转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip fast-forwarding fragcache]{lang="EN-US"}]{#struct_0_x9830_11811_x143506130}

[Total number of fragment fast-forwarding entries: 3]{lang="EN-US"}

[SIP             SPort DIP             DPort Pro Input_If    ID]{lang="EN-US"}

[7.0.0.13        68    8.0.0.1         67    17  GE1/0/3     2]{lang="EN-US"}

[8.0.0.1         67    7.0.0.13        68    17  GE1/0/1     3]{lang="EN-US"}

[8.0.0.1         8     7.0.0.13        0     1   GE1/0/2     5]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ip fast-forwarding fragcache]{lang="EN-US"}]{#struct_0_x9830_11811_x1800186484}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1204069264}[[字段]{style="font-family:黑体"}]{#struct_0_x9830_11811_1883900431}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x9830_11811_2118355378}

[[Total number of fragment fast-forwarding entries]{lang="EN-US"}]{#struct_0_x9830_11811_x806267441}

[[分片报文快速转发表项数目]{style="font-family:宋体"}]{#struct_0_x9830_11811_1103777421}

[[SIP]{lang="EN-US"}]{#struct_0_x9830_11811_647201116}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9830_11811_x497376539}[地址]{style="font-family:宋体"}

[[SPort]{lang="EN-US"}]{#struct_0_x9830_11811_x1619063043}

[[源端口号]{style="font-family:宋体"}]{#struct_0_x9830_11811_x730846793}

[[DIP]{lang="EN-US"}]{#struct_0_x9830_11811_2118289842}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9830_11811_1089415323}[地址]{style="font-family:宋体"}

[[DPort]{lang="EN-US"}]{#struct_0_x9830_11811_x1299399177}

[[目的端口号]{style="font-family:宋体"}]{#struct_0_x9830_11811_x865486561}

[[Pro]{lang="EN-US"}]{#struct_0_x9830_11811_x1940726548}

[[协议号]{style="font-family:宋体"}]{#struct_0_x9830_11811_x1789169633}

[[Input_If]{lang="EN-US"}]{#struct_0_x9830_11811_2117831091}

[[报文入接口类型和接口号（"]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x9830_11811_x594902262}["表示接口存在但是该快速转发不涉及入接口，"]{style="font-family:宋体"}[-]{lang="EN-US"}["表示接口不存在）]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_x9830_11811_1807760721}

[[分片]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x9830_11811_x1959255157}[报文]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_190666361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_2117765555}

::: {#1894304990 .myid}
[]{#_Toc298249421}[]{#_Ref135293180}[]{#_Toc95362257}[]{#_Toc37217649}[]{#_Toc404786505}[]{#struct_0_x9830_11811_x203416663}[]{#_Toc306705056}[]{#_Toc295825275}[]{#_Toc373848454}[]{#_Toc373848455}[]{#_Toc373848456}[]{#_Toc373848457}[]{#_Toc373848458}[]{#_Toc373848459}[]{#_Toc373848460}[]{#_Toc373848461}[]{#_Toc373848462}[]{#_Toc373848463}[]{#_Toc373848464}[]{#_Toc373848465}[]{#_Toc373848466}[]{#_Toc373848467}[]{#_Toc373848468}[]{#_Toc373848469}[]{#_Toc373848470}[]{#_Toc373848471}[]{#_Toc373848472}[]{#_Toc373848473}[]{#_Toc373848474}[]{#_Toc373848475}[]{#_Toc373848476}[]{#_Toc373848477}[]{#_Toc373848478}[]{#_Toc373848479}[]{#_Toc373848480}[]{#_Toc234742411}[]{#_Toc234742412}[]{#_Toc233801338}[]{#_Toc234730247}[]{#_Toc234742413}[]{#_Toc233801340}[]{#_Toc234730249}[]{#_Toc234742415}[]{#_Toc233801341}[]{#_Toc234730250}[]{#_Toc234742416}[]{#_Toc233801342}[]{#_Toc234730251}[]{#_Toc234742417}[]{#_Toc233801344}[]{#_Toc234730253}[]{#_Toc234742419}

**快速转发 \-- 快速转发配置命令 \-- ip fast-forwarding aging-time**

------------------------------------------------------------------------

[**[ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_2117568947}[命令用来配置快速转发表项的老化时间。]{style="font-family:
宋体"}

[**[undo ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_1679138211}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1697222670}

[**[ip fast-forwarding aging-time ]{lang="EN-US"}***[aging-time]{lang="EN-US"}*]{#struct_0_x9830_11811_x2128580677}

[**[undo ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_x1885888383}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x238661154}

[[快速转发表项的老化时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x9830_11811_1340042813}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_149052063}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_1872779273}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2117503411}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_1774754549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_929564429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x1404221322}

[*[aging-time]{lang="EN-US"}*]{#struct_0_x9830_11811_1450492628}[：快速转发表项的老化时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1874738009}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_588943310}[配置快速转发表项的老化时间为]{style="font-family:宋体"}[20s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9830_11811_x376901033}

[\[Sysname\] ip fast-forwarding aging-time 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1928629832}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip fast-forwarding aging-time]{lang="EN-US"}**]{#struct_0_x9830_11811_2117437875}
:::

::: {#-1213605163 .myid}
[]{#_Toc404786506}[]{#struct_0_x9830_11811_1695115867}[]{#_Toc365028485}

**快速转发 \-- 快速转发配置命令 \-- ip fast-forwarding load-shaing**

------------------------------------------------------------------------

[**[ip fast-forwarding load-sharing]{lang="EN-US"}**]{#struct_0_x9830_11811_x2025867676}[命令用来开启快转负载分担功能。]{style="font-family:宋体"}

[**[undo ip fast-forwardingload-shaing]{lang="EN-US"}**]{#struct_0_x9830_11811_574026442}[命令用来关闭快转负载分担功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x559521627}

[**[ip fast-forwarding load-sharing]{lang="EN-US"}**]{#struct_0_x9830_11811_x1222410800}

[**[undo ip fast-forwarding load-sharing]{lang="EN-US"}**]{#struct_0_x9830_11811_1839061850}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1946656899}

[[快转负载分担功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x9830_11811_129031926}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x298434725}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_x499189613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1721437232}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_1256111811}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_889237592}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9830_11811_179359846}

[[关闭快速转发负载分担功能后，将会根据入接口的不同对五元组标识的数据流再次做出区分，即将入接口作为区分数据流的另一特征标识。]{style="font-family:宋体"}]{#struct_0_x9830_11811_x147999953}

[[开启快速转发负载分担功能后，当一条数据流从不同入接口上来进行转发时，不再根据入接口不同区分数据流，根据五元组标识一条数据流。]{style="font-family:宋体"}]{#struct_0_x9830_11811_x1775293661}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x243426474}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_1374770609}[开启快转负载分担功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x9830_11811_532316453}

[\[Sysname\] ip fast-forwarding load-sharing]{lang="EN-US"}
:::

::: {#952357089 .myid}
[]{#_Toc404786507}[]{#struct_0_x9830_11811_2097507778}[]{#_Toc373848483}

**快速转发 \-- 快速转发配置命令 \-- reset ip fast-forwarding cache**

------------------------------------------------------------------------

[**[reset ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x152190741}[命令用来清除快速转发表中的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x2110524926}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x9830_11811_x486167275}

[**[reset ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x1784765901}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x9830_11811_x1225313804}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ip fast-forwarding cache]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_x525357479}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x9830_11811_x1965978508}[模式：]{style="font-family:宋体"}

[**[reset ip fast-forwarding cache]{lang="EN-US"}**[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x9830_11811_x1473082102}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2117372339}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x9830_11811_x1757933876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x9830_11811_x92292305}

[[network-admin]{lang="EN-US"}]{#struct_0_x9830_11811_x670146677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x9830_11811_1833680282}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x9830_11811_1658262753}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_1208695841}[：清除指定单板的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x1312134485}[：清除指定成员设备的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则清除所有成员设备的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_703728118}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则清除所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的快速转发表信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_1909801418}[：清除指定成员设备上指定单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x2025155237}[：清除指定单板的快速转发表信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则清除所有单板的快速转发表信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x9830_11811_x910847754}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的快速转发表信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x9830_11811_2118355379}

[[执行]{style="font-family:宋体"}**[reset ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x806332977}[命令后，快速转发表中不再有任何快速转发表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x9830_11811_402065362}

[[\# ]{lang="EN-US"}]{#struct_0_x9830_11811_1907260790}[清除快速转发表信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip fast-forwarding cache]{lang="EN-US"}]{#struct_0_x9830_11811_2132550691}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x9830_11811_136775860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip fast-forwarding cache]{lang="EN-US"}**]{#struct_0_x9830_11811_x1657491821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip fast-forwarding fragcache]{lang="EN-US"}**]{#struct_0_x9830_11811_1997781443}

[ ]{lang="EN-US"}
:::
