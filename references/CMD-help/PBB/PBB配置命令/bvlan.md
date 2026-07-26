::: {#1223385164 .myid}
[]{#_Toc404784347}[]{#struct_0_14574_x2122_x1729324174}[]{#_Toc344127268}

**PBB \-- PBB配置命令 \-- bvlan**

------------------------------------------------------------------------

[**[bvlan]{lang="EN-US"}**]{#struct_0_14574_x2122_x12840640}[命令用来为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo bvlan]{lang="EN-US"}**]{#struct_0_14574_x2122_x943522910}[命令用来删除]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x504158214}

[**[bvlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_14574_x2122_x528706123}

[**[undo bvlan]{lang="EN-US"}**]{#struct_0_14574_x2122_1254168642}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1320798670}

[[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x1992632226}[实例未指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x66007113}

[[VSI PBB]{lang="EN-US"}]{#struct_0_14574_x2122_x1036086019}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x218905286}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1231958235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x943457374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1037027916}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_14574_x2122_1653585737}[：]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的编号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1922179737}

[[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x2103389540}[实例必须指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[才能够生效，只有]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[和]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[都相同的]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例才能互通。一个]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例只能够指定一个]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[，多个不同的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[可以指定相同的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x422910294}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x464911930}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能，创建]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[web]{lang="EN-US"}[，其]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，指定该]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_x943391838}

[\[Sysname\] l2vpn enable]{lang="EN-US"}

[\[Sysname\] vsi web]{lang="EN-US"}

[\[Sysname-vsi-web\] pbb i-sid 100]{lang="EN-US"}

[\[Sysname-vsi-web-100\] bvlan 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1445692811}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_1507547741}
:::

::: {#-1607827180 .myid}
[]{#_Toc404784348}[]{#struct_0_14574_x2122_961380627}

**PBB \-- PBB配置命令 \-- display l2vpn minm connection**

------------------------------------------------------------------------

[**[display l2vpn minm connection]{lang="EN-US"}**]{#struct_0_14574_x2122_x2135552783}[命令用来显示]{style="font-family:
宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1234262622}

[**[display l2vpn minm connection ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_14574_x2122_x1885274479}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_212702308}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_147686696}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x943326302}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x1682614965}

[[network-operator]{lang="EN-US"}]{#struct_0_14574_x2122_84515572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x972888613}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14574_x2122_x256352726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1128724236}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_14574_x2122_x408899960}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1085666473}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x458272611}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn minm connection]{lang="EN-US"}]{#struct_0_14574_x2122_x943260766}

[Total number of MinM connections: 2]{lang="EN-US"}

[Types: MC - multicast, UC - unicast]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 1]{lang="EN-US"}

[Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface]{lang="EN-US"}

[68       1         00e0-3948-0100  4001   PBB     UC    GE1/0/1]{lang="EN-US"}

[-        1         011e-8300-0001  4001   PBB     MC    GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 2]{lang="EN-US"}

[Link ID  I-SID     BMAC            BVLAN  Owner   Type  Interface]{lang="EN-US"}

[69       2         00e0-3948-0300  4002   PBB     UC    GE1/0/2]{lang="EN-US"}

[-        2         011e-8300-0002  4002   PBB     MC    GE1/0/2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display l2vpn minm connection]{lang="EN-US"}]{#struct_0_14574_x2122_x1732898650}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2129740822}[[字段]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1251561067}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14574_x2122_1858718308}

[[VSI name]{lang="EN-US"}]{#struct_0_14574_x2122_115198344}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_386254365}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_14574_x2122_x943195230}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_14574_x2122_267629305}[连接的链路标识符]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_14574_x2122_x1297703719}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_14574_x2122_x225387096}

[[BMAC]{lang="EN-US"}]{#struct_0_14574_x2122_1898220645}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14574_x2122_x236496653}

[[BVLAN]{lang="EN-US"}]{#struct_0_14574_x2122_1101592928}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14574_x2122_x943129694}

[[Owner]{lang="EN-US"}]{#struct_0_14574_x2122_x596104649}

[[表项生成者，取值为]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_14574_x2122_x1495926775}[或]{style="font-family:宋体"}[SPB]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_14574_x2122_1332372710}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_14574_x2122_x786432395}[连接的属性标记，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MC]{lang="EN-US"}]{#struct_0_14574_x2122_x573154372}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UC]{lang="EN-US"}]{#struct_0_14574_x2122_x943064158}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_14574_x2122_x145736199}

[[出接口]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1535027752}

[ ]{lang="EN-US"}

::: {#485530473 .myid}
[]{#_Toc404784349}[]{#struct_0_14574_x2122_x92693058}[]{#_Toc242067216}[]{#_Toc185927308}[]{#_Toc123026768}

**PBB \-- PBB配置命令 \-- display l2vpn minm forwarding**

------------------------------------------------------------------------

[**[display l2vpn minm forwarding]{lang="EN-US"}**]{#struct_0_14574_x2122_x925105723}[命令用来显示]{style="font-family:
宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x10968318}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14574_x2122_637173009}

[**[display l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_14574_x2122_333387378}

[[分布式设备―独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14574_x2122_x944047198}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ ]{lang="EN-US"}]{#struct_0_14574_x2122_1283180890}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14574_x2122_1371174732}[模式：]{style="font-family:宋体"}

[**[display ]{lang="EN-US"}[l2vpn minm forwarding ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \] \[ **chassis** *chassis-number* ]{lang="EN-US"}]{#struct_0_14574_x2122_x54261933}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_168241921}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_307381937}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x548793949}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_913022169}

[[network-operator]{lang="EN-US"}]{#struct_0_14574_x2122_686669393}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x943981662}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14574_x2122_x939227576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_251429913}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_14574_x2122_742205599}[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14574_x2122_374783120}[：显示指定单板上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示主控板上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备―独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14574_x2122_x2118799738}[：显示指定成员设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14574_x2122_x1029384987}[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_14574_x2122_x1721081484}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主控板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}***[ slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_14574_x2122_1343268008}[：显示指定单板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果不指定本参数，则显示]{style="font-family:宋体"}[Master]{lang="EN-US"}[设备上主控板的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14574_x2122_605757185}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_730775685}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x910101806}[显示所有的]{style="font-family:宋体"}[MAC-in-MAC]{lang="EN-US"}[转发表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn minm forwarding]{lang="EN-US"}]{#struct_0_14574_x2122_x943522909}

[Total number of MinM connections: 4]{lang="EN-US"}

[Types: MC - multicast, UC -- unicast]{lang="EN-US"}

[Status Flag: \* - inactive]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 1]{lang="EN-US"}

[Link ID I-SID     BMAC            BVLAN Owner Type Interface]{lang="EN-US"}

[68      1         00e0-3948-0100  4001  PBB   UC   GE1/0/1]{lang="EN-US"}

[-       1         011e-8300-0001  4001  PBB   MC   GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI name: 2]{lang="EN-US"}

[Link ID I-SID     BMAC            BVLAN Owner Type Interface]{lang="EN-US"}

[69      2         00e0-3948-0300  4002  PBB   UC   GE1/0/2]{lang="EN-US"}

[-       2         011e-8300-0002  4002  PBB   MC   GE1/0/2]{lang="EN-US"}

[                                                   GE1/0/3]{lang="EN-US"}

[                                                   GE1/0/4]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display l2vpn minm forwarding]{lang="EN-US"}]{#struct_0_14574_x2122_x503568391}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2099519371}[[字段]{style="font-family:黑体"}]{#struct_0_14574_x2122_1954321953}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14574_x2122_x899960682}

[[VSI name]{lang="EN-US"}]{#struct_0_14574_x2122_x943457373}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1037355596}[名称]{style="font-family:宋体"}

[[Link ID]{lang="EN-US"}]{#struct_0_14574_x2122_x1809592784}

[[MAC-in-MAC]{lang="EN-US"}]{#struct_0_14574_x2122_x1650266990}[连接的链路标识符]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_14574_x2122_x903075739}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_14574_x2122_x405588090}

[[BMAC]{lang="EN-US"}]{#struct_0_14574_x2122_821270052}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14574_x2122_x943391837}

[[BVLAN]{lang="EN-US"}]{#struct_0_14574_x2122_1446544779}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14574_x2122_575893698}

[[Owner]{lang="EN-US"}]{#struct_0_14574_x2122_1327257435}

[[表项生成者，取值为]{style="font-family:宋体"}[PBB]{lang="EN-US"}]{#struct_0_14574_x2122_1210957700}[或]{style="font-family:宋体"}[SPB]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_14574_x2122_230652057}

[[属性标记，取值包括：]{style="font-family:宋体"}]{#struct_0_14574_x2122_x943326301}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MC]{lang="EN-US"}]{#struct_0_14574_x2122_x1682680501}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UC]{lang="EN-US"}]{#struct_0_14574_x2122_x868018789}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_14574_x2122_1346796416}

[[出接口]{style="font-family:宋体"}]{#struct_0_14574_x2122_890013652}

[[如果接口后面带有"]{style="font-family:宋体"}[\*]{lang="EN-US"}]{#struct_0_14574_x2122_x943260765}["，则表示该接口下刷驱动失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1007637280 .myid}
[]{#_Toc404784350}[]{#struct_0_14574_x2122_x1732964186}

**PBB \-- PBB配置命令 \-- display l2vpn vsi**

------------------------------------------------------------------------

[**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_1900848613}[命令用来显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1057175623}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14574_x2122_x898644325}**[l2vpn]{lang="EN-US"}**[ ]{lang="EN-US"}**[vsi]{lang="EN-US"}**[ \[]{lang="EN-US"}*[ ]{lang="EN-US"}***[name]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*[ ]{lang="EN-US"}[\] \[ ]{lang="EN-US"}**[verbose]{lang="EN-US"}**[ \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_894695633}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_x796155163}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1105363824}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_597012340}

[[network-operator]{lang="EN-US"}]{#struct_0_14574_x2122_x943195229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_267039480}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14574_x2122_261290574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x2147003097}

[**[name]{lang="EN-US"}**]{#struct_0_14574_x2122_x365469622}*[ vsi-name]{lang="EN-US"}*[：显示指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14574_x2122_x1196494583}[：显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。如果不指定本参数，则显示]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x372147541}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x2125969153}[显示所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display l2vpn vsi verbose]{lang="EN-US"}]{#struct_0_14574_x2122_x943064157}

[VSI Name: 1]{lang="EN-US"}

[  VSI Index               : 0]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : -]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  PBB I-SID               : 1]{lang="EN-US"}

[  PBB Connections:]{lang="EN-US"}

[    BMAC            BVLAN            Link ID    Type]{lang="EN-US"}

[    00e0-3948-0100  4001             68         Unicast]{lang="EN-US"}

[    011e-8300-0001  4001             -          Multicast]{lang="EN-US"}

[  ACs:]{lang="EN-US"}

[    AC                               Link ID    State]{lang="EN-US"}

[    BAGG1 srv1                       0          Down]{lang="EN-US"}

[ ]{lang="EN-US"}

[VSI Name: 2]{lang="EN-US"}

[  VSI Index               : 1]{lang="EN-US"}

[  VSI State               : Up]{lang="EN-US"}

[  MTU                     : 1500]{lang="EN-US"}

[  Bandwidth               : 102400 kbps]{lang="EN-US"}

[  Broadcast Restrain      : 5%]{lang="EN-US"}

[  Multicast Restrain      : 100%]{lang="EN-US"}

[  Unknown Unicast Restrain: 100%]{lang="EN-US"}

[  MAC Learning            : Enabled]{lang="EN-US"}

[  MAC Table Limit         : -]{lang="EN-US"}

[  Drop Unknown            : Disabled]{lang="EN-US"}

[  PBB I-SID               : 2]{lang="EN-US"}

[  PBB Connections:]{lang="EN-US"}

[    BMAC            BVLAN            Link ID    Type]{lang="EN-US"}

[    00e0-3948-0300  4002             69         Unicast]{lang="EN-US"}

[    011e-8300-0002  4002             -          Multicast]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display l2vpn vsi]{lang="EN-US"}]{#struct_0_14574_x2122_x145801735}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2098792653}[[字段]{style="font-family:黑体"}]{#struct_0_14574_x2122_1537246830}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14574_x2122_1943481381}

[[VSI Name]{lang="EN-US"}]{#struct_0_14574_x2122_252622837}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x1736258575}[名称]{style="font-family:宋体"}

[[VSI Index]{lang="EN-US"}]{#struct_0_14574_x2122_611175231}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x944047197}[索引]{style="font-family:宋体"}

[[VSI Description]{lang="EN-US"}]{#struct_0_14574_x2122_1283377498}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x1022634657}[的描述信息，如果不配置，则此行不显示]{style="font-family:宋体"}

[[VSI State]{lang="EN-US"}]{#struct_0_14574_x2122_659507221}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x930721296}[的状态，取值包括]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_14574_x2122_1949789732}[：]{lang="EN-US" style="font-family:宋体"}[up]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_14574_x2122_x943981661}[：]{lang="EN-US" style="font-family:宋体"}[down]{lang="EN-US"}[状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_14574_x2122_x939030968}[[：通过]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}**[shutdown]{lang="EN-US"}**[[命令手工关闭]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[VSI]{lang="EN-US"}

[[MTU]{lang="EN-US"}]{#struct_0_14574_x2122_2144854445}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1934386149}[上配置的最大传输单元]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_14574_x2122_x1804850172}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_418226635}[的带宽限制值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}

[[Broadcast Restrain]{lang="EN-US"}]{#struct_0_14574_x2122_x943522912}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x504027142}[的广播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的广播流量速率超出特定值（带宽限制值×广播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃广播报文]{style="font-family:宋体"}

[[Multicast Restrain]{lang="EN-US"}]{#struct_0_14574_x2122_1434668618}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1468643760}[的组播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的组播流量速率超出特定值（带宽限制值×组播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃组播报文]{style="font-family:宋体"}

[[Unknown Unicast Restrain]{lang="EN-US"}]{#struct_0_14574_x2122_520532309}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x943457376}[的未知单播抑制百分比。当]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的未知单播流量速率超出特定值（带宽限制值×未知单播抑制百分比）时，该]{style="font-family:宋体"}[VSI]{lang="EN-US"}[会丢弃未知单播流量报文]{style="font-family:宋体"}

[[MAC Learning]{lang="EN-US"}]{#struct_0_14574_x2122_1037158988}

[[是否使能了]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14574_x2122_1599257036}[地址学习功能，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14574_x2122_x855454328}[：使能了]{lang="EN-US" style="font-family:宋体"}[MAC]{lang="EN-US"}[地址学习功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14574_x2122_2020155423}[[：未使能]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}[MAC]{lang="EN-US"}[[地址学习功能]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[MAC Table Limit]{lang="EN-US"}]{#struct_0_14574_x2122_x943391840}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1446217100}[内]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表项的最大数目]{style="font-family:宋体"}

[[取值为]{style="font-family:宋体"}]{#struct_0_14574_x2122_984874257}[[Unlimited]{lang="EN-US"}]{.ItemListinTableCharChar}[，表示不限制]{style="font-family:宋体"}[[VSI]{lang="EN-US"}]{.ItemListinTableCharChar}[内]{style="font-family:宋体"}[[MAC]{lang="EN-US"}]{.ItemListinTableCharChar}[地址表项的最大数目]{style="font-family:宋体"}

[[Drop Unknown]{lang="EN-US"}]{#struct_0_14574_x2122_1192458318}

[[当]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1426043728}[内学习到的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址数达到最大值后，是否禁止转发源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址表里的报文：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14574_x2122_x943326304}[：表示禁止转发]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14574_x2122_x1683008181}[[：表示允许转发]{lang="EN-US" style="font-family:宋体"}]{.TableTextChar}

[[Hub-Spoke]{lang="EN-US"}]{#struct_0_14574_x2122_1230329274}

[[是否使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}]{#struct_0_14574_x2122_1878017402}[能力。取值为]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[，表示使能了]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力；如果未使能]{style="font-family:宋体"}[Hub-spoke]{lang="EN-US"}[能力，则不显示该字段]{style="font-family:宋体"}

[[Hub-spoke]{lang="EN-US"}]{#struct_0_14574_x2122_x626165996}[不适用于]{style="font-family:宋体"}[PBB]{lang="EN-US"}[，]{style="font-family:宋体"}[PBB]{lang="EN-US"}[不关心该字段取值]{style="font-family:宋体"}

[[PBB I-SID]{lang="EN-US"}]{#struct_0_14574_x2122_x943260768}

[[PBB]{lang="EN-US"}]{#struct_0_14574_x2122_x1732767578}[骨干网服务实例编号]{style="font-family:宋体"}

[[PBB Connections]{lang="EN-US"}]{#struct_0_14574_x2122_1507942787}

[[PBB]{lang="EN-US"}]{#struct_0_14574_x2122_201996692}[连接]{style="font-family:宋体"}

[[BMAC]{lang="EN-US"}]{#struct_0_14574_x2122_x943195232}

[[骨干网]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14574_x2122_267760377}

[[BVLAN]{lang="EN-US"}]{#struct_0_14574_x2122_310746471}

[[骨干网]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14574_x2122_x335417769}

[[Type]{lang="EN-US"}]{#struct_0_14574_x2122_x943129696}

[[属性标记，取值包括：]{style="font-family:宋体"}]{#struct_0_14574_x2122_x595973577}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multicast]{lang="EN-US"}]{#struct_0_14574_x2122_x1321940811}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unicast]{lang="EN-US"}]{#struct_0_14574_x2122_x1805055480}[：单播表项，该表项的支持情况与产品型号有关，请以产品的实际情况为准]{style="font-family:宋体"}

[[ACs]{lang="EN-US"}]{#struct_0_14574_x2122_x943064160}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x146260484}[的]{style="font-family:宋体"}[AC]{lang="EN-US"}[列表]{style="font-family:宋体"}

[[AC]{lang="EN-US"}]{#struct_0_14574_x2122_244060324}

[[接入电路，取值有如下两种：]{style="font-family:宋体"}]{#struct_0_14574_x2122_x944047200}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[三层接口名称：如]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1437283997}[GE0/1/4]{lang="EN-US"}[。在三层接口下关联]{style="font-family:宋体"}[VSI]{lang="EN-US"}[时，]{style="font-family:宋体"}[AC]{lang="EN-US"}[取值为此方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[[二层接口名称和以太网服务实例：如]{style="font-family:宋体"}]{.TableTextChar}]{#struct_0_14574_x2122_x1469776598}[GE0/1/3 srv1]{lang="EN-US"}[[。在以太网服务实例下关联]{style="font-family:宋体"}]{.TableTextChar}[VSI]{lang="EN-US"}[[时，]{style="font-family:宋体"}]{.TableTextChar}[AC]{lang="EN-US"}[[取值为此方式]{style="font-family:宋体"}]{.TableTextChar}

[[Link ID]{lang="EN-US"}]{#struct_0_14574_x2122_438097069}

[[AC]{lang="EN-US"}]{#struct_0_14574_x2122_x943981664}[在]{style="font-family:宋体"}[VSI]{lang="EN-US"}[内的链路]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_14574_x2122_x938834360}

[[AC]{lang="EN-US"}]{#struct_0_14574_x2122_1800343721}[的状态，取值包括]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[ ]{lang="EN-US"}

::::: {#-1110489258 .myid}
[]{#_Toc404784351}[]{#struct_0_14574_x2122_x1593856140}[]{#_Toc344127262}[]{#_Toc339896856}

**PBB \-- PBB配置命令 \-- display pbb connection**

------------------------------------------------------------------------

[**[display pbb connection]{lang="EN-US"}**]{#struct_0_14574_x2122_x943522911}[命令用来显示]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x504092678}

[**[display pbb connection ]{lang="EN-US"}**[\[ **vsi** *vsi-name* \]]{lang="EN-US"}]{#struct_0_14574_x2122_x1307703482}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_259825465}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_1105862224}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x220186194}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_188290968}

[[network-operator]{lang="EN-US"}]{#struct_0_14574_x2122_470500886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x1040141380}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14574_x2122_x943457375}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1036962380}

[**[vsi ]{lang="EN-US"}***[vsi-name]{lang="EN-US"}*]{#struct_0_14574_x2122_855375154}[：显示指定]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定该参数，将显示所有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x87795626}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PBB命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_14574_x2122_802078336}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令具体的显示信息与设备的实际情况有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14574_x2122_704817969}
:::

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x2079505491}[显示所有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display pbb connection]{lang="EN-US"}]{#struct_0_14574_x2122_x943391839}

[VSIIndex  I-SID   BMAC            BVLAN  Port       Type  Aging]{lang="EN-US"}

[0         1       011e-8300-0001  4001   GE1/0/1    MC    N]{lang="EN-US"}

[0         1       00e0-3948-0100  4001   GE1/0/1    UC    Y]{lang="EN-US"}

[1         2       011e-8300-0002  4002   GE1/0/2    MC    N]{lang="EN-US"}

[                                         GE1/0/3]{lang="EN-US"}

[                                         GE1/0/4]{lang="EN-US"}

[1         2       00e0-3948-0300  4002   GE1/0/2    UC    Y]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display pbb connection]{lang="EN-US"}]{#struct_0_14574_x2122_1445627275}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2109330565}[[字段]{style="font-family:黑体"}]{#struct_0_14574_x2122_x457835386}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1991529458}

[[VSIIndex]{lang="EN-US"}]{#struct_0_14574_x2122_443052161}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x943326303}[实例的索引]{style="font-family:宋体"}

[[I-SID]{lang="EN-US"}]{#struct_0_14574_x2122_x1682549429}

[[骨干网服务实例编号]{style="font-family:宋体"}]{#struct_0_14574_x2122_161206408}

[[BMAC]{lang="EN-US"}]{#struct_0_14574_x2122_x1361455224}

[[B-MAC]{lang="EN-US"}]{#struct_0_14574_x2122_x1300539801}[地址]{style="font-family:宋体"}

[[BVLAN]{lang="EN-US"}]{#struct_0_14574_x2122_x124686568}

[[B-VLAN]{lang="EN-US"}]{#struct_0_14574_x2122_x943260767}[的编号]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_14574_x2122_x1732833114}

[[出接口的名称]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1363529988}

[[Type]{lang="EN-US"}]{#struct_0_14574_x2122_x1568172731}

[[表项类型：]{style="font-family:宋体"}]{#struct_0_14574_x2122_x581329612}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UC]{lang="EN-US"}]{#struct_0_14574_x2122_x2681750}[：单播表项]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MC]{lang="EN-US"}]{#struct_0_14574_x2122_x943195231}[：组播表项]{lang="EN-US" style="font-family:宋体"}

[[Aging]{lang="EN-US"}]{#struct_0_14574_x2122_267563769}

[[老化标记：]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1582207035}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Y]{lang="EN-US"}]{#struct_0_14574_x2122_x1317729537}[：支持老化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_14574_x2122_x415751221}[：不支持老化]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x547267033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset pbb connection]{lang="EN-US"}**]{#struct_0_14574_x2122_x943129695}

::: {#-900899430 .myid}
[]{#_Toc404784352}[]{#struct_0_14574_x2122_x596039113}[]{#_Toc344127270}

**PBB \-- PBB配置命令 \-- encapsulation**

------------------------------------------------------------------------

[**[encapsulation]{lang="EN-US"}**]{#struct_0_14574_x2122_x1422849074}[命令用来配置当前]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例对应的数据封装类型。]{style="font-family:宋体"}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_14574_x2122_1866385669}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1829608180}

[**[encapsulation ]{lang="EN-US"}**[{ **ethernet** \| **vlan** }]{lang="EN-US"}]{#struct_0_14574_x2122_x129312642}

[**[undo encapsulation]{lang="EN-US"}**]{#struct_0_14574_x2122_1922099761}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_491408729}

[[数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14574_x2122_x348232506}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x943064159}

[[VSI PBB]{lang="EN-US"}]{#struct_0_14574_x2122_x145670663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1135808914}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x1925531414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x1933067914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1096387456}

[**[ethernet]{lang="EN-US"}**]{#struct_0_14574_x2122_1126430075}[：数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**]{#struct_0_14574_x2122_x236047527}[：数据封装类型为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_541548776}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x985568954}[配置]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[web]{lang="EN-US"}[对应的数据封装类型为]{style="font-family:宋体"}[Ethernet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_x614293512}

[\[Sysname\] l2vpn enable]{lang="EN-US"}

[\[Sysname\] vsi web]{lang="EN-US"}

[\[Sysname-vsi-web\] pbb i-sid 100]{lang="EN-US"}

[\[Sysname-vsi-web-100\] encapsulation ethernet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_60126250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pbb i-sid]{lang="EN-US"}**]{#struct_0_14574_x2122_220418638}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_x1348927418}
:::

::: {#2070950537 .myid}
[]{#_Toc404784353}[]{#struct_0_14574_x2122_x1797437642}

**PBB \-- PBB配置命令 \-- l2vpn enable**

------------------------------------------------------------------------

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_14574_x2122_888662882}[命令用来使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_14574_x2122_1420815331}[命令用来关闭]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1244386568}

[**[l2vpn enable]{lang="EN-US"}**]{#struct_0_14574_x2122_x1119123371}

[**[undo l2vpn enable]{lang="EN-US"}**]{#struct_0_14574_x2122_x1621160905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_703599102}

[[L2VPN]{lang="EN-US"}]{#struct_0_14574_x2122_x951416859}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_543241962}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1797503178}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_414068380}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x1303594242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_192490220}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_777067503}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x1148028882}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_x1585544966}

[\[Sysname\] l2vpn enable]{lang="EN-US"}
:::

::: {#-1639074051 .myid}
[]{#_Toc404784354}[]{#struct_0_14574_x2122_x943981663}

**PBB \-- PBB配置命令 \-- pbb i-sid**

------------------------------------------------------------------------

[**[pbb i-sid]{lang="EN-US"}**]{#struct_0_14574_x2122_x939162040}[命令用来创建]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例，并进入]{style="font-family:宋体"}[VSI PBB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo pbb i-sid]{lang="EN-US"}**]{#struct_0_14574_x2122_x189215934}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x366441652}

[**[pbb i-sid]{lang="EN-US"}**[ *i-sid*]{lang="EN-US"}]{#struct_0_14574_x2122_x1351903774}

[**[undo ]{lang="EN-US"}[pbb i-sid]{lang="EN-US"}**]{#struct_0_14574_x2122_171637859}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_70167062}

[[未创建]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x1590436397}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1038048695}

[[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_622561033}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1608248012}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1081672175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x723874317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1183043728}

[*[i-sid]{lang="EN-US"}*]{#struct_0_14574_x2122_x2084757016}[：指定]{style="font-family:宋体"}[PBB]{lang="EN-US"}[的骨干网服务实例编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1636641168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_14574_x2122_x2117801316}[PBB VSI]{lang="EN-US"}[实例就是创建一个]{style="font-family:宋体"}[PBB]{lang="EN-US"}[类型的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并同时指定其]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个]{style="font-family:宋体"}]{#struct_0_14574_x2122_1291929098}[VSI]{lang="EN-US"}[视图下，]{style="font-family:宋体"}[PBB]{lang="EN-US"}[和]{style="font-family:宋体"}[SPB]{lang="EN-US"}[的]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[不能相同。有关]{style="font-family:宋体"}[SPB]{lang="EN-US"}[的详细介绍，请参见"]{style="font-family:宋体"}[SPB]{lang="EN-US"}[配置指导"中的"]{style="font-family:宋体"}[SPBM]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[PBBN]{lang="EN-US"}]{#struct_0_14574_x2122_792652722}[中同一]{lang="EN-US" style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例必须指定相同的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[，不同]{lang="EN-US" style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的]{lang="EN-US" style="font-family:宋体"}[I-SID]{lang="EN-US"}[不能]{lang="EN-US" style="font-family:宋体"}[相]{style="font-family:宋体"}[同。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_872693276}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x318556213}[创建]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[，其]{style="font-family:宋体"}[I-SID]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI PBB]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_622626569}

[\[Sysname\] vsi vpn1]{lang="EN-US"}

[\[Sysname-vsi-vpn1\] pbb i-sid 100]{lang="EN-US"}

[\[Sysname-vsi-vpn1-100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_1375647825}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn ]{lang="EN-US"}**]{#struct_0_14574_x2122_117210058}**[minm connection]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn minm forwarding]{lang="EN-US"}**]{#struct_0_14574_x2122_1540371680}
:::

::: {#233825342 .myid}
[]{#_Toc344127266}[]{#_Toc404784355}[]{#struct_0_14574_x2122_x16861045}[]{#_Toc344127269}[]{#_Toc339896859}

**PBB \-- PBB配置命令 \-- pbb uplink**

------------------------------------------------------------------------

[**[pbb uplink]{lang="EN-US"}**]{#struct_0_14574_x2122_x970776183}[命令用来将接口指定为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口。]{style="font-family:宋体"}

[**[undo pbb uplink]{lang="EN-US"}**]{#struct_0_14574_x2122_1728888396}[命令用来取消接口作为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x2029594696}

[**[pbb uplink ]{lang="EN-US"}**[{ **all** \| **vsi** *vsi-name-list* }]{lang="EN-US"}]{#struct_0_14574_x2122_622692105}

[**[undo pbb uplink ]{lang="EN-US"}**[{ **all** \| **vsi** *vsi-name-list* }]{lang="EN-US"}]{#struct_0_14574_x2122_x1732080736}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_2130356633}

[[接口不是任何]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x2058346814}[实例的上行口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x324008430}

[[二层以太网接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14574_x2122_476161357}[二层聚合接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x463364768}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x253037739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1521074537}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_622757641}

[**[all]{lang="EN-US"}**]{#struct_0_14574_x2122_x1315951521}[：配置接口为所有]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的上行口。]{style="font-family:宋体"}

[**[vsi ]{lang="EN-US"}***[vsi-name-list]{lang="EN-US"}*]{#struct_0_14574_x2122_12861448}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名字列表，配置接口为某个或多个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的上行口。表示方式为]{style="font-family:宋体"}*[vsi-name-list]{lang="EN-US"}*[ = { *vsi-name* }&\<1-10\>]{lang="EN-US"}[。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1093649886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_705395144}[实例需要指定上行口后才能够正常工作。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若接口是所有]{style="font-family:宋体"}]{#struct_0_14574_x2122_x728197163}[PBB VSI]{lang="EN-US"}[实例的上行口，此时若需要将其改为某个]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口，需先取消该接口是所有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口的配置，否则配置不生效；若接口是某些]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口，此时还可以将其改为是所有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的上行口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以指定]{style="font-family:宋体"}]{#struct_0_14574_x2122_x443839433}[PBB VSI]{lang="EN-US"}[实例的名称后，再创建对应的]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合接口配置为上行口时，必须所有的聚合成员端口都支持]{style="font-family:宋体"}]{#struct_0_14574_x2122_x795399354}[PBB]{lang="EN-US"}[。否则，配置不成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合接口先配置为上行口，之后将某个接口加入该聚合组，若该接口不支持]{style="font-family:宋体"}]{#struct_0_14574_x2122_x1035924373}[PBB]{lang="EN-US"}[，则该接口加入聚合成功，但是会打印日志信息提示用户该接口不支持]{style="font-family:宋体"}[PBB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_622823177}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_59804343}[使能]{style="font-family:宋体"}[L2VPN]{lang="EN-US"}[功能，创建]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[web]{lang="EN-US"}[和]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[mail]{lang="EN-US"}[，将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[、]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[指定为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[web]{lang="EN-US"}[和]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[mail]{lang="EN-US"}[的上行口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_1602173345}

[\[Sysname\] l2vpn enable]{lang="EN-US"}

[\[Sysname\] vsi web]{lang="EN-US"}

[\[Sysname-vsi-web\] pbb i-sid 100]{lang="EN-US"}

[\[Sysname-vsi-web-100\] bvlan 100]{lang="EN-US"}

[\[Sysname-vsi-web-100\] quit]{lang="EN-US"}

[\[Sysname-vsi-web\] quit]{lang="EN-US"}

[\[Sysname\] vsi mail]{lang="EN-US"}

[\[Sysname-vsi-mail\] pbb i-sid 200]{lang="EN-US"}

[\[Sysname-vsi-mail-200\] bvlan 200]{lang="EN-US"}

[\[Sysname-vsi-mail-200\] quit]{lang="EN-US"}

[\[Sysname-vsi-mail\] quit]{lang="EN-US"}

[\[Sysname\] interface range gigabitethernet 1/0/1 to gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-if-range\] pbb uplink vsi web mail]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x703025357}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_x2097268863}
:::

::: {#1411662741 .myid}
[]{#_Toc404784356}[]{#struct_0_14574_x2122_2140033251}

**PBB \-- PBB配置命令 \-- reset pbb connection**

------------------------------------------------------------------------

[**[reset pbb connection]{lang="EN-US"}**]{#struct_0_14574_x2122_622888713}[命令用来清除]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_20226763}

[**[reset pbb connection]{lang="EN-US"}**[ \[ { **bvlan** ]{lang="EN-US"}*[vlan-id]{lang="EN-US"}*[ \| **interface** ]{lang="EN-US"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[ } \* \| **vsi** ]{lang="EN-US"}*[vsi-name ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_14574_x2122_595409550}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x917779194}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_x2080242938}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1960634182}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_x264813551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1698463636}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x739640742}

[**[bvlan]{lang="EN-US"}**[ ]{lang="EN-US"}*[vlan-id]{lang="EN-US"}*]{#struct_0_14574_x2122_622954249}[：清除指定]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[内]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。如果未指定该参数，将清除所有]{style="font-family:宋体"}[B-VLAN]{lang="EN-US"}[内]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_14574_x2122_1601240771}[：清除指定接口上]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口名称和接口编号。如果未指定该参数，将清除所有接口上]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}**[ ]{lang="EN-US"}*[vsi-name]{lang="EN-US"}*]{#struct_0_14574_x2122_1392911406}[：清除指定]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定该参数，将清除所有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例的连接信息。本参数的支持情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x272309525}

[[只有]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}]{#struct_0_14574_x2122_1241734794}[连接信息中的单播表项可以通过本命令进行清除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1218416382}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x1169177153}[清除]{style="font-family:宋体"}[PBB VSI]{lang="EN-US"}[实例]{style="font-family:宋体"}[web]{lang="EN-US"}[的]{style="font-family:宋体"}[连接信息。]{style="font-family:宋体"}

[[\<Sysname\> reset pbb connection vsi web]{lang="EN-US"}]{#struct_0_14574_x2122_236431547}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_623019785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pbb connection]{lang="EN-US"}**]{#struct_0_14574_x2122_x810903193}
:::

::: {#-981054953 .myid}
[]{#_Toc404784357}[]{#struct_0_14574_x2122_x1797044426}

**PBB \-- PBB配置命令 \-- vsi**

------------------------------------------------------------------------

[**[vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_63400221}[命令用来创建一个]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。如果指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[已经存在，则直接进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vsi**]{lang="EN-US"}]{#struct_0_14574_x2122_x347518466}[命令用来删除指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x290474487}

[**[vsi]{lang="IT"}**]{#struct_0_14574_x2122_430045337}[ *vsi-name*]{lang="IT"}

[**[undo]{lang="IT"}**]{#struct_0_14574_x2122_x1667196205}[ ]{lang="IT"}**[vsi]{lang="IT"}**[ *vsi-name*]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1118247087}

[[设备上不存在任何]{style="font-family:宋体"}[VSI]{lang="EN-US"}]{#struct_0_14574_x2122_x759945873}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1792300061}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14574_x2122_x648591543}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x1797109962}

[[network-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1138998450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14574_x2122_1235728593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14574_x2122_439400843}

[*[vsi-name]{lang="EN-US"}*]{#struct_0_14574_x2122_x393896239}[：]{style="font-family:宋体"}[VSI]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14574_x2122_475336672}

[[\# ]{lang="EN-US"}]{#struct_0_14574_x2122_x558214070}[创建名为]{style="font-family:宋体"}[test]{lang="EN-US"}[的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[VSI]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14574_x2122_x1231937675}

[\[Sysname\] vsi test]{lang="EN-US"}

[\[Sysname-vsi-test\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14574_x2122_x2024852872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display l2vpn vsi]{lang="EN-US"}**]{#struct_0_14574_x2122_629343244}

[ ]{lang="EN-US"}
:::
