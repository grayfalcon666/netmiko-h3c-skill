::: {#-524958785 .myid}
[]{#_Toc126925295}[]{#_Toc404792281}[]{#struct_0_14687_18620_828768411}[]{#_Toc298419658}[]{#_Toc263759886}[]{#_Toc226262545}[]{#_Toc198110083}[]{#_Toc117857772}[]{#_Toc81455570}[]{#_Toc56569629}[]{#_Toc41626754}[]{#_Toc39395242}

**QoS策略 \-- 定义类的命令 \-- display traffic classifier**

------------------------------------------------------------------------

[**[display traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_x875076826}[命令用来显示类的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x614286017}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_2004859697}

[**[display traffic classifier]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *classifier-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_x2004228906}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14687_18620_x2088339494}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display traffic classifier]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *classifier-name* \] \[ **slot**]{lang="EN-US"}]{#struct_0_14687_18620_x1849431188}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_14687_18620_x429569522}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display traffic classifier]{lang="EN-US"}**[ { **system-defined** \| **user-defined**]{lang="EN-US"}]{#struct_0_14687_18620_1058413226}[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:black"}[} \[ *classifier-name* \] \[]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1614071486}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1087532927}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x863680279}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x210820729}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x2003901226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1630096130}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1358018739}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1510225430}

[**[system-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x694766660}[：系统定义类。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_14687_18620_683216767}[：用户定义类。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[classifier-name]{lang="EN-US"}*]{#struct_0_14687_18620_1250531685}[：类名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有类的配置信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_472297435}*[ slot-number]{lang="EN-US"}*[：显示指定单板的流分类的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示主用主控板的类的配置信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x820884700}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的流分类的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，将显示主用设备的类的配置信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x198563583}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[流分类的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示主用设备上类的配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_x2003835690}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的流分类的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示全局主用主控板的类的配置信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x2112436163}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[流分类的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示全局主用主控板上类的配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1240690442}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[流分类的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1233076995}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1927451163}[显示用户定义类的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display traffic classifier user-defined]{lang="EN-US"}]{#struct_0_14687_18620_499316838}

[ ]{lang="EN-US"}

[  User-defined classifier information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Classifier: 1 (ID 100)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Classifier: 2 (ID 101)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Classifier: 3 (ID 102)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x2004425513}[显示系统定义类]{style="font-family:宋体"}[default-class]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display traffic classifier system-defined default-class]{lang="EN-US"}]{#struct_0_14687_18620_764621007}

[ ]{lang="EN-US"}

[  System-defined classifier information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[   Classifier: default-class (ID 0)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match any]{lang="EN-US"}

[]{#struct_0_14687_18620_x735958508}[[表1-1 ]{lang="EN-US"}[display traffic classifier]{lang="EN-US"}]{#_Ref298418803}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1873753465}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x73431089}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1160912312}

[[User-defined classifier information]{lang="EN-US"}]{#struct_0_14687_18620_411127925}

[[用户自定义类的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x2004359977}

[[System-defined classifier information]{lang="EN-US"}]{#struct_0_14687_18620_x1928705262}

[[系统定义类的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_1839414566}

[[Classifier]{lang="EN-US"}]{#struct_0_14687_18620_2029339177}

[[类的名字及其内容，内容可以有多种类型]{style="font-family:宋体"}]{#struct_0_14687_18620_2097954860}

[[Operator]{lang="EN-US"}]{#struct_0_14687_18620_154410313}

[[分类规则之间的逻辑关系]{style="font-family:宋体"}]{#struct_0_14687_18620_x2004556585}

[[Rule(s)]{lang="EN-US"}]{#struct_0_14687_18620_x912182204}

[[分类规则]{style="font-family:宋体"}]{#struct_0_14687_18620_549054692}

[ ]{lang="EN-US"}

::: {#-1354469580 .myid}
[]{#_Toc404792282}[]{#struct_0_14687_18620_709898562}[]{#_Toc298419659}[]{#_Toc263759887}[]{#_Toc226262546}[]{#_Toc198110084}

**QoS策略 \-- 定义类的命令 \-- if-match**

------------------------------------------------------------------------

[**[if-match]{lang="EN-US"}**]{#struct_0_14687_18620_x1151558173}[命令用来定义匹配数据包的规则。]{style="font-family:宋体"}

[**[undo if-match]{lang="EN-US"}**]{#struct_0_14687_18620_x516561571}[命令用来删除配置的匹配数据包的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1454071271}

[**[if-match ]{lang="EN-US"}**[\[ **not** \] *match-criteria*]{lang="EN-US"}]{#struct_0_14687_18620_x2004491049}

[**[undo if-match]{lang="EN-US"}**[ \[ **not** \] *match-criteria*]{lang="EN-US"}]{#struct_0_14687_18620_x799679255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_2139819256}

[[没有定义匹配数据包的规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_455555028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1403850792}

[[类视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1728699671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_91307556}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1839481026}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1570376558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2004163369}

[**[not]{lang="EN-US"}**]{#struct_0_14687_18620_1458036423}[：不匹配该规则。]{style="font-family:宋体"}

[*[match-criteria]{lang="EN-US"}*]{#struct_0_14687_18620_1345284465}[：类的匹配规则，具体情况如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-2]{lang="EN-US"}](?-1354469580#_Ref213127397)[所示。]{style="font-family:
宋体"}

[]{#struct_0_14687_18620_x1720946258}[[表1-2 ]{lang="EN-US"}[类的匹配规则取值]{style="font-family:
黑体"}]{#_Ref213127397}

[]{#table_struct_0_1869946745}[[取值]{style="font-family:黑体"}]{#struct_0_14687_18620_2077184338}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1086716558}

[**[acl]{lang="EN-US"}**[ \[ **ipv6** \] { *acl-numbe*r \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_14687_18620_x2004097833}

[[定义匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_14687_18620_x793929581}[的规则]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_14687_18620_x936833762}[是]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的序号，]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[序号的取值范围是]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[，]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[序号的取值范围是]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}

[*[acl-name]{lang="EN-US"}*]{#struct_0_14687_18620_x803973200}[是]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头，为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不可以使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}

[**[app-group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_14687_18620_x2113962708}

[[定义匹配应用组的规则，]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1056108046}[为系统预定义应用组的名称。应用组的取值范围与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[**[application]{lang="EN-US"}***[ app-name]{lang="EN-US"}*]{#struct_0_14687_18620_x2004294441}

[[定义匹配应用名的规则，]{style="font-family:宋体"}*[app-name]{lang="EN-US"}*]{#struct_0_14687_18620_239501765}[为系统预定义应用的名称。应用名的取值范围与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_x439566132}

[[定义匹配所有数据包的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_x1120863939}

[**[cellular ]{lang="EN-US"}***[cellular-mode]{lang="EN-US"}*]{#struct_0_14687_18620_560951304}

[[定义匹配所处网络环境属性的的规则，]{style="font-family:宋体"}*[cellular-mode]{lang="EN-US"}*]{#struct_0_14687_18620_x1518100813}[的取值可以为]{style="font-family:宋体"}[2g]{lang="EN-US"}[，]{style="font-family:宋体"}[3g]{lang="EN-US"}[，]{style="font-family:宋体"}[4g]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[**[classifier]{lang="EN-US"}**]{#struct_0_14687_18620_1618183674}**[ ]{lang="EN-US" style="font-size:
  10.0pt"}***[classifier-name]{lang="EN-US"}*

[[定义匹配]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_964142905}[类的规则，]{style="font-family:宋体"}*[classifier-name]{lang="EN-US"}*[为类名]{style="font-family:宋体"}

[**[control-plane protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_x2004228905}

[[定义匹配控制平面或者管理口控制平面协议的规则，]{style="font-family:宋体"}*[protocol-name]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_640543861}[为系统预定义匹配协议报文类型名称的列表，具体如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}1-3]{lang="EN-US"}](?-1354469580#_Ref362545063)[所示，]{style="font-family:
  宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:
  宋体"}[8]{lang="EN-US"}[次。协议类型的取值范围与设备的型号有关，请以设备的实际情况为准]{style="font-family:
  宋体"}

[**[control-plane protocol-group ]{lang="EN-US"}***[protocol-group-name]{lang="EN-US"}*]{#struct_0_14687_18620_1986570938}

[[定义匹配控制平面或者管理口控制平面协议组的规则，]{style="font-family:宋体"}*[protocol-group-name]{lang="EN-US"}*]{#struct_0_14687_18620_x2003901225}[取值为]{style="font-family:宋体"}[critical]{lang="EN-US"}[、]{style="font-family:宋体"}[exception]{lang="EN-US"}[、]{style="font-family:宋体"}[important]{lang="EN-US"}[、]{style="font-family:宋体"}[management]{lang="EN-US"}[、]{style="font-family:宋体"}[monitor]{lang="EN-US"}[、]{style="font-family:宋体"}[normal]{lang="EN-US"}[、]{style="font-family:宋体"}[redirect]{lang="EN-US"}

[**[customer-dot1p]{lang="EN-US"}**[ *dot1p-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_x1226811603}

[[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_1293236761}[内层]{style="font-family:宋体"}[VLAN Tag 802.1p]{lang="EN-US"}[优先级的规则，]{style="font-family:宋体"}*[dot1p-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值的列表，]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[customer-vlan-id ]{lang="EN-US"}***[vlan-id-list]{lang="EN-US"}*]{#struct_0_14687_18620_x864337369}

[[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x2003835689}[内层]{style="font-family:宋体"}[VLAN Tag VLAN ID]{lang="EN-US"}[的规则，]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list ]{lang="EN-US"}*[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[vlan-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id1]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id2]{lang="EN-US"}*[取值范围为]{style="font-family:
  宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，且]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[的值；]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[destination-mac]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_14687_18620_1852102256}

[[定义匹配目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14687_18620_176765889}[地址的规则]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}**[ *dscp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_716091066}

[[定义匹配]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x438341569}[的规则，]{style="font-family:宋体"}*[dscp-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[取值的列表，]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次；也可以输入关键字，具体如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所示]{style="font-family:宋体"}

[**[forwarding-layer ]{lang="SV"}**]{#struct_0_14687_18620_445279645}[{ **bridge** \| **route** }]{lang="SV"}

[[定义匹配转发报文的二、三层属性的规则：]{style="font-family:宋体"}]{#struct_0_14687_18620_199775444}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bridge]{lang="SV"}**]{#struct_0_14687_18620_x1850922308}[：]{style="font-family:宋体"}[只匹配二层转发报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route]{lang="EN-US"}**]{#struct_0_14687_18620_x438276033}[：只匹配三层转发报文]{style="font-family:宋体"}

[**[inbound-interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_14687_18620_431552696}

[[定义匹配入接口的规则，]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x987113087}[为接口类型和接口编号]{style="font-family:宋体"}

[**[ip-precedence]{lang="EN-US"}**[ *ip-precedence-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_1155256260}

[[定义匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x438472641}[优先级的规则，]{style="font-family:宋体"}*[ip-precedence-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级的列表，]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[local-precedence ]{lang="EN-US"}***[local-precedence-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_1610271693}

[[定义匹配本地优先级的规则，]{style="font-family:宋体"}*[local-precedence-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_760516804}[为本地优先级的列表，本地优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[mpls-exp]{lang="EN-US"}**[ *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_711962400}

[[定义匹配第一层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}]{#struct_0_14687_18620_x438407105}[优先级的规则，]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[的列表，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[mpls-label]{lang="EN-US"}**[ { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_14687_18620_38765762}

[[定义匹配第一层]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_14687_18620_x96935761}[标签的规则，]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签值的列表，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}***[ to]{lang="EN-US"}**[ *label-value2*]{lang="EN-US"}[表示一个]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的范围，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[的值，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}

[**[packet-length]{lang="EN-US"}**]{#struct_0_14687_18620_x438079425}[ ]{lang="EN-US" style="font-size:
  10.0pt"}[{ **min**]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.0pt"}*[min-value]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt"}[\|]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:10.0pt"}**[max ]{lang="EN-US"}***[max-value]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt"}[} \*]{lang="EN-US"}

[[定义匹配报文长度的规则，]{style="font-family:宋体"}*[min-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1542581778}[为匹配报文最小长度的字节数，]{style="font-family:宋体"}*[max-value]{lang="EN-US"}*[为匹配报文最大长度的字节数]{style="font-family:宋体"}

[**[protocol]{lang="EN-US"}**[ *protocol-name*]{lang="EN-US"}]{#struct_0_14687_18620_2092720833}

[[定义匹配协议的规则，]{style="font-family:宋体"}*[protocol-name]{lang="EN-US"}*]{#struct_0_14687_18620_2046905358}[取值为]{style="font-family:宋体"}[arp]{lang="EN-US"}[、]{style="font-family:宋体"}[ip]{lang="EN-US"}[、]{style="font-family:宋体"}[ipv6 ]{lang="EN-US"}

[**[qos-local-id]{lang="EN-US"}**[ *local-id-value*]{lang="EN-US"}]{#struct_0_14687_18620_x438013889}

[[定义匹配]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_1552897602}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值的规则，]{style="font-family:宋体"}*[local-id-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}

[**[rtp start-port]{lang="EN-US"}**]{#struct_0_14687_18620_1935274955}**[ ]{lang="EN-US" style="font-size:
  10.0pt"}***[start-port-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt"}**[end-port]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt"}*[end-port-number]{lang="EN-US"}*

[[定义匹配]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_14687_18620_182272756}[协议端口的规则。]{style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[为起始]{style="font-family:宋体"}[RTP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[；]{style="font-family:宋体"}*[end-port-number]{lang="EN-US"}*[为结束]{style="font-family:宋体"}[RTP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}

[**[second-mpls-exp]{lang="EN-US"}**[ *exp-value*&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_x438210497}

[[定义匹配第二层]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}]{#struct_0_14687_18620_825876968}[优先级的规则，]{style="font-family:宋体"}*[exp-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[EXP]{lang="EN-US"}[的列表，]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[second-mpls-label]{lang="EN-US"}**[ { *label-value*&\<1-8\> \| *label-value1* **to** *label-value2* }]{lang="EN-US"}]{#struct_0_14687_18620_x2074579252}

[[定义匹配第二层]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_14687_18620_x438144961}[标签的规则，]{style="font-family:宋体"}*[label-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签值的列表，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}***[ to]{lang="EN-US"}***[ label-value2]{lang="EN-US"}*[表示一个]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的范围，]{style="font-family:宋体"}*[label-value1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[label-value2]{lang="EN-US"}*[的值，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}

[**[service-dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}]{#struct_0_14687_18620_x1151856738}

[[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x20531942}[外层]{style="font-family:宋体"}[VLAN Tag 802.1p]{lang="EN-US"}[优先级的规则，]{style="font-family:宋体"}*[dot1p-value]{lang="EN-US"}*[&\<1-8\>]{lang="EN-US"}[为]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值的列表，]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-8\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[service-vlan-id]{lang="EN-US"}**[ *vlan-id-list*]{lang="EN-US"}]{#struct_0_14687_18620_185207414}

[[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x437817281}[外层]{style="font-family:宋体"}[VLAN Tag VLAN ID]{lang="EN-US"}[的规则，]{style="font-family:宋体"}*[vlan-id-list]{lang="EN-US"}*[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示方式为]{style="font-family:宋体"}*[vlan-id-list ]{lang="EN-US"}*[= { *vlan-id* \| *vlan-id1* **to** *vlan-id2* }&\<1-10\>]{lang="EN-US"}[，]{style="font-family:
  宋体"}*[vlan-id]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id1]{lang="EN-US"}*[、]{style="font-family:
  宋体"}*[vlan-id2]{lang="EN-US"}*[取值范围为]{style="font-family:
  宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[，且]{style="font-family:宋体"}*[vlan-id1]{lang="EN-US"}*[的值必须小于]{style="font-family:宋体"}*[vlan-id2]{lang="EN-US"}*[的值；]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以重复输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**[ *mac-address*]{lang="EN-US"}]{#struct_0_14687_18620_1797031246}

[[定义匹配源]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14687_18620_1140581397}[地址的规则]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_14687_18620_70478643}[[表1-3 ]{lang="EN-US"}[系统预定义匹配协议报文类型名称的列表]{style="font-family:
黑体"}]{#_Ref362545063}

[]{#table_struct_0_1964124765}[[报文类型]{style="font-family:黑体"}]{#struct_0_14687_18620_x677224209}

[[说明]{style="font-family:黑体"}]{#struct_0_14687_18620_70413107}

[[default]{lang="EN-US"}]{#struct_0_14687_18620_845493074}

[[其他协议]{style="font-family:宋体"}]{#struct_0_14687_18620_70871859}

[[arp]{lang="EN-US"}]{#struct_0_14687_18620_x1151619593}

[[ARP]{lang="EN-US"}]{#struct_0_14687_18620_192398701}[协议]{style="font-family:宋体"}

[[arp-snooping]{lang="EN-US" style="font-size:10.0pt;font-family:\"Segoe UI\",\"sans-serif\";color:black"}]{#struct_0_14687_18620_70806323}

[[ARP Snooping]{lang="EN-US"}]{#struct_0_14687_18620_1636431517}[协议]{style="font-family:宋体"}

[[bgp]{lang="EN-US"}]{#struct_0_14687_18620_1636365981}

[[BGP]{lang="EN-US"}]{#struct_0_14687_18620_1636300445}[协议]{style="font-family:宋体"}

[[bgp4+]{lang="EN-US"}]{#struct_0_14687_18620_1636234909}

[[IPv6 BGP]{lang="EN-US"}]{#struct_0_14687_18620_1636693661}

[[bpdu-tunnel]{lang="EN-US"}]{#struct_0_14687_18620_1636628125}

[[BPDU Tunnel]{lang="EN-US"}]{#struct_0_14687_18620_1636562589}[协议]{style="font-family:宋体"}

[[cdp]{lang="EN-US"}]{#struct_0_14687_18620_1636497053}

[[CDP]{lang="EN-US"}]{#struct_0_14687_18620_1636955805}[协议]{style="font-family:宋体"}

[[cfd]{lang="EN-US"}]{#struct_0_14687_18620_1636890269}

[[CFD]{lang="EN-US"}]{#struct_0_14687_18620_1636431516}[协议]{style="font-family:宋体"}

[[dhcp]{lang="EN-US"}]{#struct_0_14687_18620_1636365980}

[[DHCP]{lang="EN-US"}]{#struct_0_14687_18620_1636300444}[协议]{style="font-family:宋体"}

[[dhcp-snooping]{lang="EN-US"}]{#struct_0_14687_18620_1636234908}

[[DHCP Snooping]{lang="EN-US"}]{#struct_0_14687_18620_1636693660}[协议]{style="font-family:宋体"}

[[dhcpv6]{lang="EN-US"}]{#struct_0_14687_18620_1636628124}

[[IPv6 DHCP]{lang="EN-US"}]{#struct_0_14687_18620_1636562588}[协议]{style="font-family:宋体"}

[[dldp]{lang="EN-US"}]{#struct_0_14687_18620_1636497052}

[[DLDP]{lang="EN-US"}]{#struct_0_14687_18620_1636955804}[协议]{style="font-family:宋体"}

[[dot1x]{lang="EN-US"}]{#struct_0_14687_18620_1636890268}

[[802.1p ]{lang="EN-US"}]{#struct_0_14687_18620_1636431515}[协议]{style="font-family:宋体"}

[[gmrp]{lang="EN-US"}]{#struct_0_14687_18620_1636365979}

[[GMRP]{lang="EN-US"}]{#struct_0_14687_18620_1636300443}[协议]{style="font-family:宋体"}

[[mvrp]{lang="EN-US"}]{#struct_0_14687_18620_1636693659}

[[MVRP]{lang="EN-US"}]{#struct_0_14687_18620_1636628123}[协议（包含]{style="font-family:宋体"}[GVRP]{lang="EN-US"}[协议）]{style="font-family:宋体"}

[[http]{lang="EN-US"}]{#struct_0_14687_18620_1636562587}

[[HTTP]{lang="EN-US"}]{#struct_0_14687_18620_1636497051}[协议]{style="font-family:宋体"}

[[https]{lang="EN-US"}]{#struct_0_14687_18620_1636955803}

[[HTTPS]{lang="EN-US"}]{#struct_0_14687_18620_1636890267}[协议]{style="font-family:宋体"}

[[icmp]{lang="EN-US"}]{#struct_0_14687_18620_1636431514}

[[ICMP]{lang="EN-US"}]{#struct_0_14687_18620_1636365978}[协议]{style="font-family:宋体"}

[[icmpv6]{lang="EN-US"}]{#struct_0_14687_18620_1636300442}

[[IPv6 ICMP]{lang="EN-US"}]{#struct_0_14687_18620_1636234906}[协议]{style="font-family:宋体"}

[[igmp]{lang="EN-US"}]{#struct_0_14687_18620_1636693658}

[[IGMP]{lang="EN-US"}]{#struct_0_14687_18620_1636628122}[协议]{style="font-family:宋体"}

[[igmp-snooping]{lang="EN-US"}]{#struct_0_14687_18620_1636562586}

[[IGMP Snooping]{lang="EN-US"}]{#struct_0_14687_18620_1636955802}[协议]{style="font-family:宋体"}

[[irdp]{lang="EN-US"}]{#struct_0_14687_18620_1636890266}

[[IRDP]{lang="EN-US"}]{#struct_0_14687_18620_1636431513}[协议]{style="font-family:宋体"}

[[isis]{lang="EN-US"}]{#struct_0_14687_18620_1636365977}

[[IS-IS]{lang="EN-US"}]{#struct_0_14687_18620_1636300441}[协议]{style="font-family:宋体"}

[[lacp]{lang="EN-US"}]{#struct_0_14687_18620_1636234905}

[[LACP]{lang="EN-US"}]{#struct_0_14687_18620_1636693657}[协议]{style="font-family:宋体"}

[[ldp]{lang="EN-US"}]{#struct_0_14687_18620_1636628121}

[[LDP]{lang="EN-US"}]{#struct_0_14687_18620_1636562585}[协议]{style="font-family:宋体"}

[[ldp6]{lang="EN-US"}]{#struct_0_14687_18620_1636497049}

[[IPv6 LDP]{lang="EN-US"}]{#struct_0_14687_18620_1636890265}[协议]{style="font-family:宋体"}

[[lldp]{lang="EN-US"}]{#struct_0_14687_18620_1636431512}

[[LLDP]{lang="EN-US"}]{#struct_0_14687_18620_1636365976}[协议]{style="font-family:宋体"}

[[mld]{lang="EN-US"}]{#struct_0_14687_18620_1636300440}

[[MLD]{lang="EN-US"}]{#struct_0_14687_18620_1636234904}[协议]{style="font-family:宋体"}

[[msdp]{lang="EN-US"}]{#struct_0_14687_18620_1636693656}

[[MSDP]{lang="EN-US"}]{#struct_0_14687_18620_1636628120}[协议]{style="font-family:宋体"}

[[ntp]{lang="EN-US"}]{#struct_0_14687_18620_1636562584}

[[NTP]{lang="EN-US"}]{#struct_0_14687_18620_1636955800}[协议]{style="font-family:宋体"}

[[oam]{lang="EN-US"}]{#struct_0_14687_18620_1636890264}

[[OAM]{lang="EN-US"}]{#struct_0_14687_18620_x1092451838}[协议]{style="font-family:宋体"}

[[ospf-multicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092517374}

[[OSPF]{lang="EN-US"}]{#struct_0_14687_18620_x1092582910}[组播]{style="font-family:宋体"}

[[ospf-unicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092648446}

[[OSPF]{lang="EN-US"}]{#struct_0_14687_18620_x1092189694}[单播]{style="font-family:宋体"}

[[ospf3-multicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092320766}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14687_18620_x1092386302}[组播]{style="font-family:宋体"}

[[ospf3-unicast]{lang="EN-US"}]{#struct_0_14687_18620_x1091927550}

[[OSPFv3]{lang="EN-US"}]{#struct_0_14687_18620_x1091993086}[单播]{style="font-family:宋体"}

[[pim-multicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092451839}

[[PIM]{lang="EN-US"}]{#struct_0_14687_18620_x1092517375}[组播]{style="font-family:宋体"}

[[pim-unicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092648447}

[[PIM]{lang="EN-US"}]{#struct_0_14687_18620_x1092189695}[单播]{style="font-family:宋体"}

[[pim6-multicast]{lang="EN-US"}]{#struct_0_14687_18620_x1092255231}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_14687_18620_x1092320767}[组播]{style="font-family:宋体"}

[[pim6-unicast]{lang="EN-US" style="font-size:10.0pt;font-family:\"Segoe UI\",\"sans-serif\";color:black"}]{#struct_0_14687_18620_x1092386303}

[[IPv6 PIM]{lang="EN-US"}]{#struct_0_14687_18620_x1091993087}[单播]{style="font-family:宋体"}

[[portal]{lang="EN-US"}]{#struct_0_14687_18620_x1092451840}

[[PORTAL]{lang="EN-US"}]{#struct_0_14687_18620_x1092517376}[协议]{style="font-family:宋体"}

[[pppoe-negotiation]{lang="EN-US"}]{#struct_0_14687_18620_x1092582912}

[[PPPoE]{lang="EN-US"}]{#struct_0_14687_18620_x1092648448}[协商]{style="font-family:宋体"}

[[pvst]{lang="EN-US"}]{#struct_0_14687_18620_x1092255232}

[[PVST]{lang="EN-US"}]{#struct_0_14687_18620_x1092320768}[协议]{style="font-family:宋体"}

[[radius]{lang="EN-US"}]{#struct_0_14687_18620_x1092386304}

[[RADIUS]{lang="EN-US"}]{#struct_0_14687_18620_x1091927552}[协议]{style="font-family:宋体"}

[[rip]{lang="EN-US"}]{#struct_0_14687_18620_x1091993088}

[[RIP]{lang="EN-US"}]{#struct_0_14687_18620_x1092517377}[协议]{style="font-family:宋体"}

[[ripng]{lang="EN-US"}]{#struct_0_14687_18620_x1092582913}

[[RIPng]{lang="EN-US"}]{#struct_0_14687_18620_x1092648449}[协议]{style="font-family:宋体"}

[[rrpp]{lang="EN-US"}]{#struct_0_14687_18620_x1092189697}

[[RRPP]{lang="EN-US"}]{#struct_0_14687_18620_x1092320769}[协议]{style="font-family:宋体"}

[[rsvp]{lang="EN-US"}]{#struct_0_14687_18620_x1092386305}

[[RSVP]{lang="EN-US"}]{#struct_0_14687_18620_x1091927553}[协议]{style="font-family:宋体"}

[[smart-link]{lang="EN-US"}]{#struct_0_14687_18620_x1091993089}

[[Smart Link]{lang="EN-US"}]{#struct_0_14687_18620_x1092451842}[协议]{style="font-family:宋体"}

[[snmp]{lang="EN-US"}]{#struct_0_14687_18620_x1092582914}

[[SNMP]{lang="EN-US"}]{#struct_0_14687_18620_x1092648450}[协议]{style="font-family:宋体"}

[[stp]{lang="EN-US"}]{#struct_0_14687_18620_x1092189698}

[[STP]{lang="EN-US"}]{#struct_0_14687_18620_x1092255234}[协议]{style="font-family:宋体"}

[[tacacs]{lang="EN-US"}]{#struct_0_14687_18620_x1092386306}

[[TACACS]{lang="EN-US"}]{#struct_0_14687_18620_x1091927554}[协议]{style="font-family:宋体"}

[[udld]{lang="EN-US"}]{#struct_0_14687_18620_x1091993090}

[[UDLD]{lang="EN-US"}]{#struct_0_14687_18620_x1092517379}[协议]{style="font-family:宋体"}

[[udp-helper]{lang="EN-US"}]{#struct_0_14687_18620_x1092582915}

[[UDP]{lang="EN-US"}]{#struct_0_14687_18620_x1092648451}[中继转发]{style="font-family:宋体"}

[[vrrp]{lang="EN-US"}]{#struct_0_14687_18620_x1092189699}

[[VRRP]{lang="EN-US"}]{#struct_0_14687_18620_x1092320771}[协议]{style="font-family:宋体"}

[[vrrp6]{lang="EN-US"}]{#struct_0_14687_18620_x1092386307}

[[IPv6 VRRP]{lang="EN-US"}]{#struct_0_14687_18620_x1091927555}[协议]{style="font-family:宋体"}

[[vtp]{lang="EN-US"}]{#struct_0_14687_18620_829862463}

[[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_829796927}[中继协议]{style="font-family:宋体"}

[[ip-option]{lang="EN-US"}]{#struct_0_14687_18620_829731391}

[[带选项字段的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_14687_18620_829665855}[报文]{style="font-family:宋体"}

[[ipv6-option]{lang="EN-US"}]{#struct_0_14687_18620_830059071}

[[带选项字段的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_14687_18620_829993535}[报文]{style="font-family:宋体"}

[[ssh]{lang="EN-US"}]{#struct_0_14687_18620_829927999}

[[SSH]{lang="EN-US"}]{#struct_0_14687_18620_830321215}[协议]{style="font-family:宋体"}

[[telnet]{lang="EN-US"}]{#struct_0_14687_18620_829862462}

[[TELNET]{lang="EN-US"}]{#struct_0_14687_18620_829796926}[协议]{style="font-family:宋体"}

[[ftp]{lang="EN-US"}]{#struct_0_14687_18620_829731390}

[[FTP]{lang="EN-US"}]{#struct_0_14687_18620_830124606}[协议]{style="font-family:宋体"}

[[tftp]{lang="EN-US"}]{#struct_0_14687_18620_830059070}

[[TFTP]{lang="EN-US"}]{#struct_0_14687_18620_829993534}[协议]{style="font-family:宋体"}

[[bfd]{lang="EN-US"}]{#struct_0_14687_18620_830386750}

[[BFD]{lang="EN-US"}]{#struct_0_14687_18620_830321214}[协议]{style="font-family:宋体"}

[[ttl-expires]{lang="EN-US"}]{#struct_0_14687_18620_829862461}

[[TTL]{lang="EN-US"}]{#struct_0_14687_18620_829731389}[超时]{style="font-family:宋体"}

[[hoplimit-expires]{lang="EN-US"}]{#struct_0_14687_18620_829665853}

[[Hop Limit]{lang="EN-US"}]{#struct_0_14687_18620_830124605}[超时]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x437751745}

[[在定义各个规则的时候，注意事项如下：]{style="font-family:宋体"}]{#struct_0_14687_18620_x135107049}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_14687_18620_1988789307}[的规则]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果类中引用的]{style="font-family:宋体"}]{#struct_0_14687_18620_x547600684}[ACL]{lang="EN-US"}[不存在，则不能在硬件中下发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1165291113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对同一个类，允许通过]{style="font-family:宋体"}]{#struct_0_14687_18620_x2122250835}[ACL]{lang="EN-US"}[名称和序号的方式分别引用一次同一个]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于有些产品而言，当]{style="font-family:宋体"}]{#struct_0_14687_18620_2041135878}**[if-match]{lang="EN-US"}**[中引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的动作为]{style="font-family:宋体"}**[deny]{lang="EN-US"}**[时，则跳出该]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[，继续进行后续规则的查找；对于有些产品而言，直接忽略]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的动作，以流行为中定义的动作为准，报文匹配只使用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的分类域。具体情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配用户组或者应用名的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_x1459037924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_1842422329}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配所处网络环境属性的的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_x64411391}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_1371642926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令用于匹配指定网络环境下的报文。]{style="font-family:宋体"}]{#struct_0_14687_18620_1941315065}**[2g]{lang="EN-US"}**[表示匹配处于]{style="font-family:宋体"}[2G]{lang="EN-US"}[网络环境下的报文，]{style="font-family:宋体"}**[3g]{lang="EN-US"}**[表示匹配处于]{style="font-family:宋体"}[3G]{lang="EN-US"}[网络环境下的报文，]{style="font-family:宋体"}**[4g]{lang="EN-US"}**[表示匹配处于]{style="font-family:宋体"}[4G]{lang="EN-US"}[网络环境下的报文。]{style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配类的规则]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14687_18620_x438341568}

[[如果匹配类的规则之间既有逻辑与，又有逻辑或的关系，采用本匹配方法可以解决。]{style="font-family:宋体"}]{#struct_0_14687_18620_445345181}

[[例如，需要定义]{style="font-family:宋体"}[classA]{lang="EN-US"}]{#struct_0_14687_18620_1004575736}[，满足以下关系：规则]{style="font-family:宋体"}[1 & ]{lang="EN-US"}[规则]{style="font-family:宋体"}[2 \| ]{lang="EN-US"}[规则]{style="font-family:宋体"}[3]{lang="EN-US"}[，可以这样定义：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traffic classifier classB operator and]{lang="EN-US"}]{#struct_0_14687_18620_x839751091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[if-match]{lang="EN-US"}]{#struct_0_14687_18620_425946660}[规则]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[if-match]{lang="EN-US"}]{#struct_0_14687_18620_x1641655056}[规则]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[traffic classifier classA operator or]{lang="EN-US"}]{#struct_0_14687_18620_1466319131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[if-match]{lang="EN-US"}]{#struct_0_14687_18620_x460184651}[规则]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[if-match classifier classB]{lang="EN-US"}]{#struct_0_14687_18620_x522980566}

[[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x438276032}

[[(5)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配目的]{style="font-family:宋体"}]{#struct_0_14687_18620_431487160}[MAC]{lang="EN-US"}[地址规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1405978081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配目的]{style="font-family:宋体"}]{#struct_0_14687_18620_1202990932}[MAC]{lang="EN-US"}[地址规则只对以太网接口有意义。]{style="font-family:宋体"}

[[(6)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配源]{style="font-family:宋体"}]{#struct_0_14687_18620_369435330}[MAC]{lang="EN-US"}[地址规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_1492382200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配源]{style="font-family:宋体"}]{#struct_0_14687_18620_x1803980902}[MAC]{lang="EN-US"}[地址规则只对以太网接口有意义。]{style="font-family:宋体"}

[[(7)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_257214017}[DSCP]{lang="EN-US"}[的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x438472640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_1610206157}[DSCP]{lang="EN-US"}[值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x463409503}[DSCP]{lang="EN-US"}[的规则时，指定的所有]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[(8)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_172355847}[内]{style="font-family:宋体"}[层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[和]{style="font-family:宋体"}[外层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[ 802.1p]{lang="EN-US"}[优先级的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_692967441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_x1450294582}[802.1p]{lang="EN-US"}[优先级值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值，系统默认为一个；多个不同的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x49733202}[802.1p]{lang="EN-US"}[优先级的规则时，指定的所有]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[(9)[      ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x848479088}[IP]{lang="EN-US"}[优先级的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x428135735}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_x438407104}[IP]{lang="EN-US"}[优先级值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值，系统默认为一个；多个不同的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_38831298}[IP]{lang="EN-US"}[优先级的规则时，指定的所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[(10)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配本地优先级的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_x778488009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。每条命令在配置后，本地优先级的值将自动按照从小到大的顺序排序。]{style="font-family:宋体"}]{#struct_0_14687_18620_335568294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个本地优先级值，最多可指定]{style="font-family:宋体"}]{#struct_0_14687_18620_404632479}[8]{lang="EN-US"}[个；如果指定了多个相同的本地优先级值，系统默认为一个；多个不同的本地优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配本地优先级的规则时，指定的所有本地优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}]{#struct_0_14687_18620_845831247}

[[(11)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x618637882}[MPLS EXP]{lang="EN-US"}[优先级的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_1697400705}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_985880616}[MPLS EXP]{lang="EN-US"}[优先级值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级值，系统默认为一个；多个不同的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x438079424}[MPLS EXP]{lang="EN-US"}[优先级的规则时，指定的所有]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MPLS EXP]{lang="EN-US"}]{#struct_0_14687_18620_x1542647314}[为]{style="font-family:
宋体"}[MPLS]{lang="EN-US"}[报文特有的参数，该匹配规则仅对]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于软转发]{style="font-family:宋体"}]{#struct_0_14687_18620_868209053}[QoS]{lang="EN-US"}[，]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文不支持匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[相关匹配规则。]{style="font-family:宋体"}

[[(12)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{lang="EN-US" style="font-family:宋体"}[MPLS Label]{lang="EN-US"}]{#struct_0_14687_18620_x890924805}[的规则]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_305330422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_x1465431616}[MPLS Label]{lang="EN-US"}[值，如果指定了多个相同的]{style="font-family:宋体"}[MPLS Label]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[MPLS Label]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x618263836}[MPLS Label]{lang="EN-US"}[的规则时，指定的所有]{style="font-family:宋体"}[MPLS Label]{lang="EN-US"}[值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[(13)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x617515992}[内]{style="font-family:宋体"}[层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[和]{style="font-family:宋体"}[外层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[ VLAN ID]{lang="EN-US"}[的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x438013888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_1552832066}[VLAN ID]{lang="EN-US"}[值，如果指定了多个相同的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_x1198834984}[VLAN ID]{lang="EN-US"}[的规则时，指定的所有]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若只携带单层]{style="font-family:宋体"}]{#struct_0_14687_18620_x1137693567}[VLAN Tag]{lang="EN-US"}[，可以用]{style="font-family:宋体"}[外层]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[规则来匹配。]{style="font-family:宋体"}

[[(14)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配报文长度的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_627542260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_x895614924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只配置]{lang="EN-US" style="font-family:宋体"}**[min]{lang="EN-US"}**]{#struct_0_14687_18620_x703530799}[，则表示匹配大于]{lang="EN-US" style="font-family:宋体"}*[min-value]{lang="EN-US"}*[长度的报文；如果只配置]{lang="EN-US" style="font-family:宋体"}**[max]{lang="EN-US"}**[，表示匹配小于]{lang="EN-US" style="font-family:宋体"}*[max-value]{lang="EN-US"}*[长度的报文；同时配置]{lang="EN-US" style="font-family:宋体"}**[min]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[max]{lang="EN-US"}**[，表示匹配长度在]{lang="EN-US" style="font-family:宋体"}*[min-value]{lang="EN-US"}*[～]{lang="EN-US" style="font-family:宋体"}*[max-value]{lang="EN-US"}*[之间的报文。其中]{lang="EN-US" style="font-family:宋体"}*[max-value]{lang="EN-US"}*[必须大于等于]{lang="EN-US" style="font-family:宋体"}*[min-value]{lang="EN-US"}*[。]{lang="EN-US" style="font-family:宋体"}

[[(15)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配预定义的上送控制平面或者管理口控制平面报文类型的规则]{style="font-family:宋体"}]{#struct_0_14687_18620_x2098204343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_2059801523}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一条命令可以配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_x438210496}[protocol]{lang="EN-US"}[，如果指定了多个相同的]{style="font-family:宋体"}[protocol]{lang="EN-US"}[，系统默认为一个；多个不同的]{style="font-family:宋体"}[protocol]{lang="EN-US"}[是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除某条匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_825811432}[protocol]{lang="EN-US"}[的规则时，指定的所有]{style="font-family:宋体"}[protocol]{lang="EN-US"}[必须与该规则中定义的完全相同才会删除，顺序可不一样。]{style="font-family:宋体"}

[[(16)[   ]{style="font:7.0pt "}]{lang="EN-US"}[定义匹配]{style="font-family:宋体"}]{#struct_0_14687_18620_1082289231}[RTP]{lang="EN-US"}[协议端口的规则]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令用于匹配落在指定]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_14687_18620_719210356}[端口号范围内的]{lang="EN-US" style="font-family:宋体"}[RTP]{lang="EN-US"}[报文，即匹配所有在]{lang="EN-US" style="font-family:宋体"}*[start-port-number]{lang="EN-US"}*[与]{lang="EN-US" style="font-family:
宋体"}*[end-port-number]{lang="EN-US"}*[之间的偶数]{lang="EN-US" style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号的报文。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个类下可配置多条这样的命令，各个配置之间互相不覆盖。]{style="font-family:宋体"}]{#struct_0_14687_18620_1049878837}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1349392473}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1997715217}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0050-ba27-bed3]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x438144960}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match destination-mac 0050-ba27-bed3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1151791202}[定义类]{style="font-family:宋体"}[class2]{lang="EN-US"}[的匹配规则为：匹配源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[0050-ba27-bed2]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x447835989}

[\[Sysname\] traffic classifier class2]{lang="EN-US"}

[\[Sysname-classifier-class2\] if-match source-mac 0050-ba27-bed2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x220023799}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x178430404}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match customer-dot1p 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_336724607}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x437817280}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match service-dot1p 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1796965710}[定义类匹配]{style="font-family:宋体"}[ACL3101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2048740011}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match acl 3101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1174817384}[定义类匹配]{style="font-family:宋体"}[ACL flow]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1347912946}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match acl name flow]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x786097869}[定义类匹配]{style="font-family:宋体"}[IPv6 ACL3101]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x437751744}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match acl ipv6 3101]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x135172585}[定义类匹配]{style="font-family:宋体"}[IPv6 ACL flow]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1163774782}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match acl ipv6 name flow]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x191945265}[定义匹配所有数据包的规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x437812139}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match any]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_599706702}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[6]{lang="EN-US"}[或]{style="font-family:
宋体"}[9]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x676479930}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match dscp 1 6 9]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x438341571}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[6]{lang="EN-US"}[的报文。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_445803934}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match ip-precedence 1 6]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_888160327}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配本地优先级值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[6]{lang="EN-US"}[的报文。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_944839717}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match local-precedence 1 6]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1566710521}[定义类匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_2012566376}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match protocol ip]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_602006014}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[RTP]{lang="EN-US"}[端口号在]{style="font-family:宋体"}[16384]{lang="EN-US"}[和]{style="font-family:宋体"}[32767]{lang="EN-US"}[之间的偶数]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x438276035}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match rtp start-port 16384 end-port 32767]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_431945912}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[内层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值为]{style="font-family:宋体"}[1]{lang="EN-US"}[或]{style="font-family:宋体"}[6]{lang="EN-US"}[或]{style="font-family:宋体"}[9]{lang="EN-US"}[的报文。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2116542239}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match customer-vlan-id 1 6 9]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1399035677}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[的匹配规则为：匹配]{style="font-family:宋体"}[外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[或]{style="font-family:宋体"}[7]{lang="EN-US"}[或]{style="font-family:宋体"}[10]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_54179459}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match service-vlan-id 2 7 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_722424494}[定义]{style="font-family:宋体"}[类]{style="font-family:宋体"}[class1]{lang="EN-US"}[匹配]{style="font-family:宋体"}[qos-local-id 3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x438472643}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match qos-local-id 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1610140621}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[匹配应用组]{style="font-family:宋体"}[multimedia]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x808123129}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match app-group multimedia]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_957316162}[定义类]{style="font-family:宋体"}[class1]{lang="EN-US"}[匹配应用名]{style="font-family:宋体"}[3link]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1868636586}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match app-name 3link]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1073379940}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置匹配]{style="font-family:宋体"}[MPLS-Label]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[到]{style="font-family:
宋体"}[10000]{lang="EN-US"}[的报文类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x438407107}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match mpls-label 1 to 10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_38634690}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置只匹配二层转发报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1644368788}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match forwarding-layer bridge]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2086922440}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置匹配上送控制平面或管理口控制平面的]{style="font-family:宋体"}[ARP]{lang="EN-US"}[协议报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1885306770}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match control-plane protocol arp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x438079427}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置匹配上送控制平面或管理口控制平面的]{style="font-family:宋体"}[normal]{lang="EN-US"}[协议组报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1542712850}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match control-plane protocol-group normal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1987895989}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置匹配报文长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[字节的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x444220039}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match packet-length min 100 max 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x64476927}[在流分类]{style="font-family:宋体"}[class1]{lang="EN-US"}[中配置匹配处于]{style="font-family:宋体"}[3G]{lang="EN-US"}[网络环境下的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1709845220}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\] if-match cellular 3g]{lang="EN-US"}

::: {#2115911716 .myid}
[]{#_Toc404792283}[]{#struct_0_14687_18620_x863891287}[]{#_Toc298419660}[]{#_Toc263759888}[]{#_Toc226262547}[]{#_Toc198110085}[]{#_Toc117857789}[]{#_Toc81455594}[]{#_Toc56569682}[]{#_Toc54510442}[]{#_Toc42593999}

**QoS策略 \-- 定义类的命令 \-- traffic classifier**

------------------------------------------------------------------------

[**[traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_x1770023317}[命令用来定义一个类，并进入类视图。]{style="font-family:宋体"}

[**[undo traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_x711448895}[命令用来删除一个类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x438013891}

[**[traffic classifier]{lang="EN-US"}**[ *classifier-name* \[ **operator** { **and** \| **or** } \]]{lang="EN-US"}]{#struct_0_14687_18620_1553421889}

[**[undo traffic classifier]{lang="EN-US"}**[ *classifier-name*]{lang="EN-US"}]{#struct_0_14687_18620_790999033}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x12383408}

[[没有定义类。]{style="font-family:宋体"}]{#struct_0_14687_18620_1982607224}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1753426689}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_960708115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_983479825}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x438210499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_824959464}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1793619286}

[*[classifier-name]{lang="EN-US"}*]{#struct_0_14687_18620_x163849492}[：类名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[operator]{lang="EN-US"}**]{#struct_0_14687_18620_x1716850286}[：指定各规则之间的逻辑运算符。缺省情况为]{style="font-family:宋体"}**[and]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[and]{lang="EN-US"}**]{#struct_0_14687_18620_838293151}[：指定类下的规则之间是逻辑与的关系，即数据包必须匹配全部规则才属于该类。]{style="font-family:宋体"}

[**[or]{lang="EN-US"}**]{#struct_0_14687_18620_1922303676}[：指定类下的规则之间是逻辑或的关系，即数据包只要匹配其中任何一个规则就属于该类。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1059810861}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1388393029}[定义一个名为]{style="font-family:宋体"}[class1]{lang="EN-US"}[的类。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x438144963}

[\[Sysname\] traffic classifier class1]{lang="EN-US"}

[\[Sysname-classifier-class1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1151987810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_1202543382}
:::

::: {#825363998 .myid}
[]{#_Toc404792285}[]{#struct_0_14687_18620_1730709482}[]{#_Toc298419662}[]{#_Toc263759890}[]{#_Toc226262549}[]{#_Toc198110087}

**QoS策略 \-- 定义流行为的命令 \-- accounting**

------------------------------------------------------------------------

[**[accounting]{lang="EN-US"}**]{#struct_0_14687_18620_995968254}[命令用来配置流量统计动作。]{style="font-family:宋体"}

[**[undo accounting]{lang="EN-US"}**]{#struct_0_14687_18620_x1580705475}[命令用来取消流量统计动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601172807}

[**[accounting ]{lang="EN-US"}**[\[ **byte** \| **packet** \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x437817283}

[**[undo accounting]{lang="EN-US"}**]{#struct_0_14687_18620_1797162318}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_358510422}

[[没有配置流量统计动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1242906938}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_630294284}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_978132442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x586717178}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x48586018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_705381750}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x437751747}

[**[byte]{lang="EN-US"}**]{#struct_0_14687_18620_x134975977}[：]{style="font-family:宋体"}[表示报文基于字节进行统计。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_14687_18620_840604652}[：]{style="font-family:宋体"}[表示报文基于包进行统计。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x50911577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备仅支持一种统计方式或者不支持配置流统计单位时，命令行中不提示]{style="font-family:宋体"}]{#struct_0_14687_18620_x822069278}**[byte]{lang="EN-US"}**[和]{style="font-family:宋体"}**[packet]{lang="EN-US"}**[关键字，默认的统计单位由产品决定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备支持两种统计方式，但在某一时刻仅能使用一种统计单位进行统计时，]{style="font-family:宋体"}]{#struct_0_14687_18620_x903472668}**[byte]{lang="EN-US"}**[和]{style="font-family:宋体"}**[packet]{lang="EN-US"}**[为必选参数，即必须在配置中指明流统计单位。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备支持同时按两种方式进行统计，]{style="font-family:宋体"}]{#struct_0_14687_18620_10815538}**[byte]{lang="EN-US"}**[和]{style="font-family:宋体"}**[packet]{lang="EN-US"}**[为可选参数，也可以两种统计方式同时指定。若用户不指明统计单位，则采用默认的统计单位进行统计，默认的统计单位和是否可以同时指定两种方式进行统计由产品决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1868106985}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x438341570}[为流行为配置流量统计动作，基于字节进行统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_445869470}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] accounting byte]{lang="EN-US"}
:::

::: {#1390680525 .myid}
[]{#_Toc404792286}[]{#struct_0_14687_18620_157564520}[]{#_Toc298419663}[]{#_Toc263759891}[]{#_Toc226262550}[]{#_Toc198110088}

**QoS策略 \-- 定义流行为的命令 \-- car**

------------------------------------------------------------------------

[**[car]{lang="EN-US"}**]{#struct_0_14687_18620_720409237}[命令用来配置流量监管动作。]{style="font-family:宋体"}

[**[undo car]{lang="EN-US"}**]{#struct_0_14687_18620_622600495}[命令用来取消流量监管动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1686617108}

[**[car cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*[ \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \* \[ **hierarchy-car** *hierarchy-car-name* \[ **mode** { **and** \| **or** } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x541502247}

[**[car cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*[ \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \* \[ **hierarchy-car** *hierarchy-car-name* \[ **mode** { **and** \| **or** } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_1334533636}

[**[undo car]{lang="EN-US"}**]{#struct_0_14687_18620_x438276034}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_431880376}

[[没有配置流量监管动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x895774493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x376506179}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1893973509}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x610666059}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1505475609}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2103547284}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2107598553}

[**[cir]{lang="EN-US"}***[ committed-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_x438472642}[：承诺信息速率。流量的平均速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs ]{lang="EN-US"}***[committee-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_1610075085}[：承诺突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *excess-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x62233875}[：超出突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir ]{lang="EN-US"}***[peak-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_1327670761}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[green ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_1214264216}[：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[red ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_x1205086254}[：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[yellow ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_535960212}[：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[action]{lang="EN-US"}*]{#struct_0_14687_18620_x1477825637}[：对数据包采取的动作，有以下几种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[discard]{lang="EN-US"}**]{#struct_0_14687_18620_x438407106}[：丢弃数据包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pass]{lang="EN-US"}**]{#struct_0_14687_18620_38700226}[：允许数据包通过。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-atmclp-pass]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_x460059074}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dot1p-pass]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_701100064}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dscp-pass]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_1157032867}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-frde-pass]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_1936014305}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-lp-pass ]{lang="EN-US"}***[new-local-precedence]{lang="EN-US"}*]{#struct_0_14687_18620_1962820271}[：设置新的本地优先级，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-mpls-exp-pass]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_x452242743}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-prec-pass]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_978127021}[：设置新的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[*[hierarchy-car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x438079426}[：分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_14687_18620_x1542778386}[：分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[和]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作的合作模式。有]{style="font-family:宋体"}**[and]{lang="EN-US"}**[和]{style="font-family:宋体"}**[or]{lang="EN-US"}**[两种模式，默认为]{style="font-family:宋体"}**[and]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[and]{lang="EN-US"}**]{#struct_0_14687_18620_506895374}[：在该模式下，对于多条数据流应用同一个分层]{style="font-family:
宋体"}[CAR]{lang="EN-US"}[，必须每条流满足各自的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置，同时各流量之和又满足分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置，流量才能正常通过。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[or]{lang="EN-US"}**]{#struct_0_14687_18620_787718030}[：在该模式下，对于多条数据流应用同一个分层]{style="font-family:
宋体"}[CAR]{lang="EN-US"}[，只要每条流满足各自的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置或者各流量之和满足分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置，流量即可正常通过。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x706208926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上应用的策略中使用]{style="font-family:宋体"}]{#struct_0_14687_18620_785290645}**[car]{lang="EN-US"}**[时，可以应用到接口报文的接收或者发送方向。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果多次使用该命令在同一个流行为上配置，最后一次配置生效。]{style="font-family:宋体"}]{#struct_0_14687_18620_1002131663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_2062456936}[支持的动作与设备相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置]{style="font-family:宋体"}]{#struct_0_14687_18620_x1126177559}[峰值速率]{style="font-family:宋体"}[表示所配置的是单速桶流量监管，否则表示双速桶流量监管。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x438013890}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1553356353}[为流行为配置流量监管。报文正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，承诺突发尺寸为]{style="font-family:宋体"}[50000bytes]{lang="EN-US"}[，速率大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，报文]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值改为]{style="font-family:宋体"}[0]{lang="EN-US"}[并发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1161664108}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] car cir 200 cbs 50000 ebs 0 green pass red remark-dscp-pass 0]{lang="EN-US"}
:::

::: {#-308098617 .myid}
[]{#_Toc404792287}[]{#struct_0_14687_18620_1990952549}[]{#_Toc298419664}[]{#_Toc263759892}[]{#_Toc226262551}[]{#_Toc198110089}

**QoS策略 \-- 定义流行为的命令 \-- display traffic behavior**

------------------------------------------------------------------------

[**[display traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x290492844}[命令用来显示流行为的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_458767603}

[]{#OLE_LINK9}[]{#OLE_LINK8}[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_x23638937}

[**[display traffic behavior]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *behavior-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_1464668790}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14687_18620_x438210498}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display traffic behavior]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *behavior-name* \] \[ **slot**]{lang="EN-US"}]{#struct_0_14687_18620_824893928}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_14687_18620_x1440253967}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display traffic behavior]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *behavior-name* \] \[]{lang="EN-US"}]{#struct_0_14687_18620_1310950106}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1547893762}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_456423727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_186871616}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2041843475}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x438144962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1151922274}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_690632930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_2062163765}

[**[system-defined]{lang="EN-US"}**]{#struct_0_14687_18620_415081653}[：系统定义行为。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x1935650045}[：用户定义行为。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[behavior-name]{lang="EN-US"}*]{#struct_0_14687_18620_1903419737}[：行为名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示所有流行为的配置信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_1923169498}*[ slot-number]{lang="EN-US"}*[：显示指定单板的流行为的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用主控板的流行为的配置信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x437817282}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的流行为的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用设备的流行为的配置信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1986791228}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[流行为的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备上流行为的配置信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_1797096782}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的流行为的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示全局主用主控板的流行为的配置信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x762789}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[流行为的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板上流行为的配置信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_325590107}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[流行为的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1950040538}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2046436626}[显示用户定义行为的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display traffic behavior user-defined]{lang="EN-US"}]{#struct_0_14687_18620_x437751746}

[ ]{lang="EN-US"}

[  User-defined behavior information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: 1 (ID 100)]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[      Primap pre-defined table: dscp-dp]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 30 (kbps)]{lang="EN-US"}

[        Discard Method: Tail]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: 2 (ID 101)]{lang="EN-US"}

[      Accounting enable: Packet]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[      Redirecting: ]{lang="EN-US"}

[        Redirect to the CPU]{lang="EN-US"}

[      Mirroring: ]{lang="EN-US"}

[        Mirror to the VLAN: VLAN 1000]{lang="EN-US"}

[      Expedited Forwarding:]{lang="EN-US"}

[        Bandwidth 50 (kbps) CBS 1250 (Bytes)]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: 3 (ID 102)]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x135041513}[显示系统定义行为的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display traffic behavior system-defined]{lang="EN-US"}]{#struct_0_14687_18620_x438341573}

[ ]{lang="EN-US"}

[  System-defined behavior information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: be (ID 0)]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: af (ID 1)]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%)]{lang="EN-US"}

[        Discard Method: Tail]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: ef (ID 2)]{lang="EN-US"}

[      Expedited Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%) Cbs-ratio 25]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Behavior: be-flow-based (ID 3)]{lang="EN-US"}

[      Flow based Weighted Fair Queue:]{lang="EN-US"}

[        Max number of hashed queues: 256]{lang="EN-US"}

[        Discard Method: IP Precedence based WRED]{lang="EN-US"}

[        Exponential Weight: 9]{lang="EN-US"}

[        Pre  Low   High  Dis-prob]{lang="EN-US"}

[        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[        0    10    30    10]{lang="EN-US"}

[        1    10    30    10]{lang="EN-US"}

[        2    10    30    10]{lang="EN-US"}

[        3    10    30    10]{lang="EN-US"}

[        4    10    30    10]{lang="EN-US"}

[        5    10    30    10]{lang="EN-US"}

[        6    10    30    10]{lang="EN-US"}

[        7    10    30    10]{lang="EN-US"}

[]{#struct_0_14687_18620_445672862}[[表1-4 ]{lang="EN-US"}[display traffic behavior]{lang="EN-US"}]{#_Ref298418812}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1622572825}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x2087471799}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x438276037}

[[User-defined behavior information]{lang="EN-US"}]{#struct_0_14687_18620_431814840}

[[用户自定义流行为的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_1404474521}

[[System-defined behavior information]{lang="EN-US"}]{#struct_0_14687_18620_840955348}

[[系统定义流行为的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x2131375989}

[[Behavior]{lang="EN-US"}]{#struct_0_14687_18620_52495772}

[[行为的名字及其内容，内容可以有多种类型]{style="font-family:宋体"}]{#struct_0_14687_18620_x438472645}

[[Marking]{lang="EN-US"}]{#struct_0_14687_18620_1610533837}

[[标记相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x793008463}

[[Remark dscp]{lang="EN-US"}]{#struct_0_14687_18620_x159809434}

[[重新标记报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x967564469}[优先级值]{style="font-family:宋体"}

[[Committed Access Rate]{lang="EN-US"}]{#struct_0_14687_18620_x438407109}

[[流量限速的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_39552194}

[[CIR]{lang="EN-US"}]{#struct_0_14687_18620_x488225459}

[[承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_x1179284662}

[[CBS]{lang="EN-US"}]{#struct_0_14687_18620_1519481546}

[[承诺突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x438079429}

[[EBS]{lang="EN-US"}]{#struct_0_14687_18620_x1543368210}

[[超出突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_656118873}

[[Green action]{lang="EN-US"}]{#struct_0_14687_18620_93622540}

[[对绿色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_788010853}

[[Red action]{lang="EN-US"}]{#struct_0_14687_18620_x438013893}

[[对红色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_1553552961}

[[Yellow action]{lang="EN-US"}]{#struct_0_14687_18620_16792373}

[[对黄色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_484928595}

[[Primap pre-defined table]{lang="EN-US"}]{#struct_0_14687_18620_x438210501}

[[预定义映射表相关信息。对于映射表的描述可以参考]{style="font-family:宋体"}]{#struct_0_14687_18620_x1130831375}[[2.1  ]{lang="EN-US"}](#_Ref307496562)[[[[优先级映射表配置命令]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}]{lang="EN-US"}](#_Ref307496567)

[[Primap color-map-dp]{lang="EN-US"}]{#struct_0_14687_18620_x1258810645}

[[根据报文颜色标记丢弃优先级的映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_210546418}

[[Primap pre-defined color table]{lang="EN-US"}]{#struct_0_14687_18620_x438144965}

[[预定义带颜色映射表相关信息。对于带颜色映射表的描述可以参考]{style="font-family:宋体"}]{#struct_0_14687_18620_x1151594594}[[2.1  ]{lang="EN-US"}](#_Ref307496562)[[[[优先级映射表配置命令]{lang="EN-US"}]{lang="EN-US" style="font-family:
  宋体"}]{lang="EN-US"}](#_Ref307496567)

[[Assured Forwarding]{lang="EN-US"}]{#struct_0_14687_18620_2011015028}

[[确保转发（]{style="font-family:宋体"}[AF]{lang="EN-US"}]{#struct_0_14687_18620_1136678519}[队列）的相关信息]{style="font-family:宋体"}

[[Bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_x437817285}

[[队列的带宽]{style="font-family:宋体"}]{#struct_0_14687_18620_1797293390}

[[Discard Method]{lang="EN-US"}]{#struct_0_14687_18620_1955330838}

[[丢弃方式]{style="font-family:宋体"}]{#struct_0_14687_18620_276636983}

[[Accounting enable]{lang="EN-US"}]{#struct_0_14687_18620_x437751749}

[[流量统计动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x135369193}

[[Filter enable]{lang="EN-US"}]{#struct_0_14687_18620_1165496952}

[[流量过滤动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x438341572}

[[Remark mpls-exp]{lang="EN-US"}]{#struct_0_14687_18620_445738398}

[[重新标记报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1069265446}[优先级值]{style="font-family:宋体"}

[[Redirecting]{lang="EN-US"}]{#struct_0_14687_18620_774740761}

[[流量重定向相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x438276036}

[[Mirroring]{lang="EN-US"}]{#struct_0_14687_18620_431749304}

[[流量镜像相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x1920953639}

[[Expedited Forwarding]{lang="EN-US"}]{#struct_0_14687_18620_x438472644}

[[加速转发（]{style="font-family:宋体"}[EF]{lang="EN-US"}]{#struct_0_14687_18620_1610468301}[队列）相关信息]{style="font-family:宋体"}

[[none]{lang="EN-US"}]{#struct_0_14687_18620_x1639208584}

[[表示没有配置其他流行为]{style="font-family:宋体"}]{#struct_0_14687_18620_1188404611}

[[Flow based Weighted Fair Queue]{lang="EN-US"}]{#struct_0_14687_18620_x438407108}

[[基于流的加权公平队列相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_39617730}

[[Max number of hashed queues]{lang="EN-US"}]{#struct_0_14687_18620_x1405509215}

[[加权公平队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_x438079428}

[[Exponential Weight]{lang="EN-US"}]{#struct_0_14687_18620_x1543433746}

[[计算平均队列长度的指数]{style="font-size:9.0pt;
  font-family:宋体"}]{#struct_0_14687_18620_x1349970067}

[[Pre]{lang="EN-US"}]{#struct_0_14687_18620_x438013892}

[[报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_1553487425}[优先级]{style="font-family:宋体"}

[[Low]{lang="EN-US"}]{#struct_0_14687_18620_x431033263}

[[队列下限]{style="font-family:宋体"}]{#struct_0_14687_18620_x438210500}

[[High]{lang="EN-US"}]{#struct_0_14687_18620_x1130896911}

[[队列上限]{style="font-family:宋体"}]{#struct_0_14687_18620_x1102868413}

[[Dis-prob]{lang="EN-US"}]{#struct_0_14687_18620_x438144964}

[[计算丢弃概率时的分母]{style="font-family:宋体"}]{#struct_0_14687_18620_x1151529058}

[ ]{lang="EN-US"}

::: {#1557880777 .myid}
[]{#_Toc404792288}[]{#struct_0_14687_18620_558280744}[]{#_Toc298419665}[]{#_Toc263759893}[]{#_Toc226262552}[]{#_Toc198110090}

**QoS策略 \-- 定义流行为的命令 \-- filter**

------------------------------------------------------------------------

[**[filter]{lang="EN-US"}**]{#struct_0_14687_18620_610190034}[命令用来配置流量过滤动作。]{style="font-family:宋体"}

[**[undo filter]{lang="EN-US"}**]{#struct_0_14687_18620_x1930688752}[命令用来取消流量过滤动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x547292191}

[**[filter ]{lang="EN-US"}**[{ **deny** \| **permit** }]{lang="EN-US"}]{#struct_0_14687_18620_x437817284}

[**[undo filter]{lang="EN-US"}**]{#struct_0_14687_18620_1797227854}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x73675378}

[[没有配置流量过滤动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1747822760}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2018385048}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1025557993}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x599689079}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1893731574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_559408056}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x437751748}

[**[deny]{lang="EN-US"}**]{#struct_0_14687_18620_x135434729}[：丢弃数据包。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_14687_18620_x1933897687}[：允许数据包通过。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1387288855}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_104780511}[为流行为配置丢弃数据包的过滤动作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1461263108}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] filter deny]{lang="EN-US"}
:::

::: {#-174551452 .myid}
[]{#_Toc298419666}[]{#_Toc263759901}[]{#_Toc226262564}[]{#_Toc198110102}[]{#_Toc198110098}[]{#_Toc307323568}[]{#_Toc327195743}[]{#_Toc319675433}[]{#_Toc404792289}[]{#struct_0_14687_18620_x1854364402}[]{#_Toc335120867}[]{#_Toc333831515}

**QoS策略 \-- 定义流行为的命令 \-- gts**

------------------------------------------------------------------------

[**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_231667622}[命令用来采用绝对值的方式为流行为配置流量整形动作。]{style="font-family:宋体"}

[**[undo gts]{lang="EN-US"}**]{#struct_0_14687_18620_1127742372}[命令用来取消流量整形动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1017176900}

[**[gts cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*[ \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1885741712}

[**[gts cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*[ \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_1334402565}

[**[undo gts]{lang="EN-US"}**]{#struct_0_14687_18620_314610401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1449683146}

[[没有配置流量整形动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x6697227}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1180488768}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_431636807}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127807908}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1306050109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2049235990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1790001722}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_x2079016033}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *committed-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x1416764291}[：承诺突发尺寸，实际平均速率在承诺速率以内时的突发流量，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *excess-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_1206261698}[：超出突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x307717954}[：峰值速率。]{style="font-family:宋体"}[PIR]{lang="EN-US"}[必须大于等于]{style="font-family:宋体"}[CIR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[queue-length]{lang="EN-US"}***[ queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_1127611300}[：队列的最大长度，缺省值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_551331897}

[[接口上应用的策略中使用]{style="font-family:宋体"}**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_2092931348}[时，只能应用到接口的出方向。]{style="font-family:宋体"}

[[接口上应用配置了]{style="font-family:宋体"}**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_x729229756}[的策略将导致原有的]{style="font-family:宋体"}**[qos gts]{lang="EN-US"}**[命令失效。]{style="font-family:宋体"}

[[如果多次使用该命令在同一个流行为上配置，最后一次的配置将覆盖前面的配置。]{style="font-family:宋体"}]{#struct_0_14687_18620_1079581221}

[[不配置]{style="font-family:宋体"}[PIR]{lang="EN-US"}]{#struct_0_14687_18620_447800556}[表示所配置的是单速桶流量整形，否则表示双速桶流量整形。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x266944569}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_393933839}[为流行为配置]{style="font-family:宋体"}[GTS]{lang="EN-US"}[，正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，承诺突发尺寸为]{style="font-family:宋体"}[50000bytes]{lang="EN-US"}[，速率大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，将进入队列缓存，缓存队列长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1352511769}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] gts cir 200 cbs 50000 ebs 0 queue-length 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127676836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gts percent]{lang="EN-US"}**]{#struct_0_14687_18620_905267813}
:::

::: {#-705676063 .myid}
[]{#_Toc404792290}[]{#struct_0_14687_18620_x1152391348}[]{#_Toc335120872}[]{#_Toc333831516}[]{#_Toc335120868}[]{#_Toc335120869}[]{#_Toc335120870}[]{#_Toc335120871}

**QoS策略 \-- 定义流行为的命令 \-- gts percent**

------------------------------------------------------------------------

[**[gts percent]{lang="EN-US"}**]{#struct_0_14687_18620_367645929}[命令用来采用百分比的方式为流行为配置流量整形动作。]{style="font-family:宋体"}

[**[undo gts]{lang="EN-US"}**]{#struct_0_14687_18620_1886524302}[命令用来取消流量整形动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x239974085}

[**[gts percent cir]{lang="EN-US"}**[ *cir-percent* \[ **cbs** *cbs-time* \[ **ebs** *ebs-time* \] \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_187240596}

[**[undo gts]{lang="EN-US"}**]{#struct_0_14687_18620_1083937362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x70200290}

[[没有配置流量整形动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1128004516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x387620493}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1820441293}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1167057536}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1526285264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_242079314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_803833109}

[**[cir ]{lang="EN-US"}***[cir-percent]{lang="EN-US"}*]{#struct_0_14687_18620_x856573327}[：承诺信息速率百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}[CIR]{lang="EN-US"}[的实际值是百分比值乘以接口带宽值。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *cbs-time*]{lang="EN-US"}]{#struct_0_14687_18620_1128070052}[：某段时间内的承诺突发尺寸，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[500ms]{lang="EN-US"}[。]{style="font-family:宋体"}[CBS]{lang="EN-US"}[的实际值是]{style="font-family:宋体"}[CBS]{lang="EN-US"}[的配置时间值乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *ebs-time*]{lang="EN-US"}]{#struct_0_14687_18620_353055715}[：某段时间内的超出突发尺寸，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0ms]{lang="EN-US"}[。]{style="font-family:宋体"}[EBS]{lang="EN-US"}[的实际值是]{style="font-family:宋体"}[EBS]{lang="EN-US"}[的配置时间值乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。]{style="font-family:宋体"}

[**[queue-length]{lang="EN-US"}***[ queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_x1568755921}[：队列的最大长度，缺省值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1269846732}

[[接口上应用的策略中使用]{style="font-family:宋体"}**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_x1026692210}[时，只能应用到接口的出方向。]{style="font-family:宋体"}

[[接口上应用配置了]{style="font-family:宋体"}**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_1173163366}[的策略将导致原有的]{style="font-family:宋体"}**[qos gts]{lang="EN-US"}**[命令失效。]{style="font-family:宋体"}

[[如果多次使用该命令在同一个流行为上配置，最后一次的配置将覆盖前面的配置。]{style="font-family:宋体"}]{#struct_0_14687_18620_757508485}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1511648753}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1127873444}[配置使用流量整形，正常流量为]{style="font-family:宋体"}[50%]{lang="EN-US"}[的接口带宽，在第一时间可以有]{style="font-family:宋体"}[200ms]{lang="EN-US"}[×]{style="font-family:宋体"}[50%]{lang="EN-US"}[接口带宽的突发流量通过，以后速率小于等于]{style="font-family:宋体"}[50%]{lang="EN-US"}[的接口带宽时正常发送，速率大于]{style="font-family:宋体"}[50%]{lang="EN-US"}[的接口带宽时，将进入队列缓存。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x629108563}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] gts percent cir 50 cbs 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1817598550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[gts]{lang="EN-US"}**]{#struct_0_14687_18620_1580252862}
:::

::: {#376916168 .myid}
[]{#_Toc404792291}[]{#struct_0_14687_18620_x1176203649}

**QoS策略 \-- 定义流行为的命令 \-- nest top-most**

------------------------------------------------------------------------

[**[nest]{lang="EN-US"}**[ **top-most**]{lang="EN-US"}]{#struct_0_14687_18620_1304906826}[命令用来配置添加]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的动作。]{lang="EN-US" style="font-family:宋体"}

[**[undo nest]{lang="EN-US"}**[ **top-most**]{lang="EN-US"}]{#struct_0_14687_18620_x728560649}[命令用来取消添加]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1231093444}

[**[nest top-most vlan ]{lang="EN-US"}***[vlan-id ]{lang="EN-US"}*[\[ **dot1p** *802.1p* \]]{lang="EN-US"}]{#struct_0_14687_18620_1127938980}

[**[undo nest top-most]{lang="EN-US"}**]{#struct_0_14687_18620_94689177}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1583057603}

[[没有配置添加]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_14687_18620_x92194893}[的动作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1019586196}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1750920641}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1595399187}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1902696128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x766702372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1128266660}

[**[vlan]{lang="EN-US"}**[ ]{lang="EN-US"}*[vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1950266642}[：添加的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot1p ]{lang="EN-US"}***[802.1p]{lang="EN-US"}*]{#struct_0_14687_18620_51052375}[：添加的]{style="font-family:
宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。如果不指定该参数，则表示报文外层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级和内层保持一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1611894404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[引用了添加]{lang="EN-US" style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}]{#struct_0_14687_18620_x428284251}[动作的]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[策略只能应用到接口的入方向上。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个流行为上多次配置本命令，新配置将覆盖旧配置。]{style="font-family:宋体"}]{#struct_0_14687_18620_1851534917}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x423079421}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x504292887}[在流行为]{style="font-family:宋体"}[b1]{lang="EN-US"}[上配置如下动作：添加]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[为]{style="font-family:宋体"}[123]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[，并配置该层]{style="font-family:宋体"}[VLAN Tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1128332196}

[\[Sysname\] traffic behavior b1]{lang="EN-US"}

[\[Sysname-behavior-b1\] nest top-most vlan 123 dot1p 3]{lang="EN-US"}
:::

::: {#-528896007 .myid}
[]{#_Toc404792292}[]{#struct_0_14687_18620_x431547086}[]{#_Toc291749942}

**QoS策略 \-- 定义流行为的命令 \-- packet-rate**

------------------------------------------------------------------------

[**[packet-rate]{lang="EN-US"}**]{#struct_0_14687_18620_1386775723}[命令用来为流行为配置限速动作。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[packet-rate]{lang="EN-US"}**]{#struct_0_14687_18620_x1887125990}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1963068785}

[]{#struct_0_14687_18620_1923460844}[**[packet-rate]{lang="EN-US"}**]{#OLE_LINK13}**[ ]{lang="EN-US"}***[value]{lang="EN-US"}*

[**[undo packet-rate]{lang="EN-US"}**]{#struct_0_14687_18620_x1023724712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x489839347}

[[没有配置限速动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1127742373}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1017111364}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_232454920}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2063548661}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x323247464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2084336619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1275188945}

[*[value]{lang="EN-US"}*]{#struct_0_14687_18620_1142001684}[：协议报文速率，单位为包每秒（]{style="font-family:宋体"}[pps]{lang="EN-US"}[）。取值范围和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127807909}

[[通过限速可以实现]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_14687_18620_1306115645}[的协议报文防攻击功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1805216470}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1091564189}[为流行为]{style="font-family:宋体"}[copp]{lang="EN-US"}[配置]{style="font-family:宋体"}[CPU]{lang="EN-US"}[报文限速动作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_884792900}

[\[Sysname\] traffic behavior copp]{lang="EN-US"}

[\[Sysname-behavior-copp\] packet-rate 1600]{lang="EN-US"}
:::

::: {#-1399075487 .myid}
[]{#_Toc404792293}[]{#struct_0_14687_18620_x238323719}

**QoS策略 \-- 定义流行为的命令 \-- primap color-map-dp**

------------------------------------------------------------------------

[**[primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1364154062}[命令用来配置流行为中的动作为根据报文颜色标记报文的丢弃优先级。]{style="font-family:宋体"}

[**[undo primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1118381595}[命令用来取消流行为中的根据报文颜色标记报文的丢弃优先级的动作。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127611301}

[**[primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_551266361}

[**[undo primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_561813270}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1763904203}

[[没有配置流优先级映射动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_964830480}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x936276076}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_401799348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1966182656}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1127676837}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_905202277}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1247697256}

[[本命令需要和]{style="font-family:宋体"}[car]{lang="EN-US"}]{#struct_0_14687_18620_x826540920}[结合在一起使用。]{style="font-family:宋体"}

[[映射关系为：红色对应丢弃优先级]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_14687_18620_1273758007}[，黄色对应丢弃优先级]{style="font-family:宋体"}[1]{lang="EN-US"}[，绿色对应丢弃优先级]{style="font-family:宋体"}[0]{lang="EN-US"}[。此映射关系固定，不能修改。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_453349326}

[[ # ]{lang="EN-US"}]{#struct_0_14687_18620_x938314436}[根据报文的颜色标记报文的丢弃优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1128004517}

[\[Sysname\] traffic behavior behavior1]{lang="EN-US"}

[\[Sysname-behavior-behavior1\] car cir 1600]{lang="EN-US"}

[\[Sysname-behavior-behavior1\] primap color-map-dp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x387554957}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_467277628}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap pre-defined color]{lang="EN-US"}**]{#struct_0_14687_18620_x661136382}
:::

::: {#1291455863 .myid}
[]{#_Toc404792294}[]{#struct_0_14687_18620_497867866}[]{#_Toc307323569}[]{#_primap_pre-defined}

**QoS策略 \-- 定义流行为的命令 \-- primap pre-defined**

------------------------------------------------------------------------

[**[primap pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_92044272}[命令用来配置流行为中的动作为使用相应的优先级映射表为报文获取其他的优先级参数。]{style="font-family:宋体"}

[**[undo primap pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x1202162974}[命令用来取消流行为中的使用相应优先级映射表为报文映射优先级的动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1405667900}

[**[primap pre-defined]{lang="EN-US"}**[ { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_516653433}

[**[undo primap pre-defined]{lang="EN-US"}**[ { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_1128070053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_352990179}

[[没有配置流优先级映射动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_867147496}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1263066987}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1080478351}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x701050351}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1926230138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1688194017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127873445}

[**[pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x629174099}[：预先定义的优先级映射表。]{style="font-family:宋体"}

[**[dot11e-lp]{lang="EN-US"}**]{#struct_0_14687_18620_x1385681313}[：]{style="font-family:宋体"}[802.11e]{lang="EN-US"}[优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_579603853}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1920574163}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x529440565}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dot1p-exp]{lang="EN-US"}**]{#struct_0_14687_18620_2063008093}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dot1p-lp]{lang="EN-US"}**]{#struct_0_14687_18620_x697064852}**[：]{style="font-family:宋体"}**[802.1p]{lang="EN-US"}[优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[dot1p-rpr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14687_18620_x250284119}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[**[dscp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_1127938981}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[dscp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_94623641}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到丢弃优先级映射表。]{style="font-family:宋体"}

[**[dscp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x1166338202}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dscp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_84677646}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dscp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_962533185}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到本地优先级映射表。]{style="font-family:宋体"}

[**[dscp-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_1266468520}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[exp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_2010951282}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[exp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1931707064}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到丢弃优先级映射表。]{style="font-family:宋体"}

[**[exp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1128266661}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[exp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_x1950201106}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[exp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_x1955406358}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到本地优先级映射表。]{style="font-family:宋体"}

[**[exp-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_226358649}**[：]{style="font-family:宋体"}**[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[**[ippre-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_x545717497}**[：]{style="font-family:宋体"}**[IP]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dot11e]{lang="EN-US"}**]{#struct_0_14687_18620_x287192464}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[802.11e]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_1506827051}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_x636256073}**[：]{style="font-family:宋体"}**[本地优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[lp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x304940875}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[lp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_1128332197}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[lp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_x431612622}**[：]{style="font-family:宋体"}**[本地优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[up-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_1753271305}[：用户优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[up-dp]{lang="EN-US"}**]{#struct_0_14687_18620_x564809545}[：用户优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[up-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x171314810}[：用户优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[up-exp]{lang="EN-US"}**]{#struct_0_14687_18620_1275647115}[：用户优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[up-fc]{lang="EN-US"}**]{#struct_0_14687_18620_x499745845}[：用户优先级到转发类映射表。]{style="font-family:宋体"}

[**[up-lp]{lang="EN-US"}**]{#struct_0_14687_18620_2052621333}[：用户优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[up-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_1127742370}[：用户优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[up-up]{lang="EN-US"}**]{#struct_0_14687_18620_x1017045828}[：用户优先级到用户优先级映射表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x530114094}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1943670682}[使用]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到丢弃优先级映射表为报文获取丢弃优先级参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_609371036}

[\[Sysname\] traffic behavior behavior1]{lang="EN-US"}

[\[Sysname-behavior-behavior1\] primap pre-defined dscp-dp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1642543647}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_x77803885}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1838439615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap pre-defined color]{lang="EN-US"}**]{#struct_0_14687_18620_1127807906}
:::

::: {#-1997689606 .myid}
[]{#_Toc404792295}[]{#struct_0_14687_18620_1306705469}[]{#_Toc307323570}[]{#_primap_pre-defined_color}

**QoS策略 \-- 定义流行为的命令 \-- primap pre-defined color**

------------------------------------------------------------------------

[**[primap pre-defined color]{lang="EN-US"}**]{#struct_0_14687_18620_1429105302}[命令用来配置流行为中的动作为使用相应的带颜色优先级映射表为报文获取其他的优先级参数。]{style="font-family:
宋体"}

[**[undo primap pre-defined color]{lang="EN-US"}**]{#struct_0_14687_18620_x480979472}[命令用来取消流行为中的使用相应的带颜色优先级映射表为报文映射优先级的动作。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x961538803}

[**[prim]{lang="EN-US"}[ap]{lang="EN-US"}**[ **pre-defined** **color** { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_2092792909}

[**[undo prim]{lang="EN-US"}[ap]{lang="EN-US"}**[ **pre-defined** **color** { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p** \| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_x1086692649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1457922771}

[[没有配置流优先级映射动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1127611298}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1405507520}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1179993115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1619795195}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x243637605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x576140663}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1375207929}

[**[pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_2064612430}[：预先定义的优先级映射表。]{style="font-family:宋体"}

[**[color]{lang="EN-US"}**]{#struct_0_14687_18620_1068576962}[：使用带颜色优先级映射表做映射。]{style="font-family:宋体"}

[**[dot11e-lp]{lang="EN-US"}**]{#struct_0_14687_18620_1127676834}[：]{style="font-family:宋体"}[802.11e]{lang="EN-US"}[优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_905398885}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dp]{lang="EN-US"}**]{#struct_0_14687_18620_52095199}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[dot1p-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x785896159}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dot1p-exp]{lang="EN-US"}**]{#struct_0_14687_18620_1524838048}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dot1p-lp]{lang="EN-US"}**]{#struct_0_14687_18620_x432744525}**[：]{style="font-family:宋体"}**[802.1p]{lang="EN-US"}[优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[dot1p-rpr]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14687_18620_x284290996}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[**[dscp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x1103281089}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[dscp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1128004514}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到丢弃优先级映射表。]{style="font-family:宋体"}

[**[dscp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x387489421}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dscp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_539366575}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[dscp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_1653581379}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到本地优先级映射表。]{style="font-family:宋体"}

[**[dscp-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_x361648177}**[：]{style="font-family:宋体"}**[DSCP]{lang="EN-US"}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[**[exp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_647724207}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[exp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_x1913257863}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到丢弃优先级映射表。]{style="font-family:宋体"}

[**[exp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_903739369}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[exp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_x667834390}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[exp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_1128070050}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到本地优先级映射表。]{style="font-family:宋体"}

[**[exp-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_353186787}[：]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[ippre-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_x351294118}**[：]{style="font-family:宋体"}**[IP]{lang="EN-US"}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dot11e]{lang="EN-US"}**]{#struct_0_14687_18620_233971578}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[802.11e]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x1176714900}[：本地优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[lp-dp]{lang="EN-US"}**]{#struct_0_14687_18620_x1802224937}**[：]{style="font-family:宋体"}**[本地优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[lp-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1540063541}**[：]{style="font-family:宋体"}**[本地优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[lp-exp]{lang="EN-US"}**]{#struct_0_14687_18620_1547751230}[：本地优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[lp-lp]{lang="EN-US"}**]{#struct_0_14687_18620_1127873442}**[：]{style="font-family:宋体"}**[本地优先级到本地优先级映射表]{style="font-family:宋体"}

[**[up-dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x628977491}[：用户优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[up-dp]{lang="EN-US"}**]{#struct_0_14687_18620_957844776}[：用户优先级到丢弃优先级映射表。]{style="font-family:宋体"}

[**[up-dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x1520592593}[：用户优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[up-exp]{lang="EN-US"}**]{#struct_0_14687_18620_1376650121}[：用户优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表。]{style="font-family:宋体"}

[**[up-fc]{lang="EN-US"}**]{#struct_0_14687_18620_x1591724861}[：用户优先级到转发类映射表。]{style="font-family:宋体"}

[**[up-lp]{lang="EN-US"}**]{#struct_0_14687_18620_886909108}[：用户优先级到本地优先级映射表。]{style="font-family:宋体"}

[**[up-rpr]{lang="EN-US"}**]{#struct_0_14687_18620_x255008264}[：用户优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表。]{style="font-family:宋体"}

[**[up-up]{lang="EN-US"}**]{#struct_0_14687_18620_2109511291}[：用户优先级到用户优先级映射表。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127938978}

[[本命令需要和]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_94164884}[结合在一起使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2023843036}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1857259072}[使用带颜色的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到丢弃优先级映射表为报文获取丢弃优先级参数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_674567818}

[\[Sysname\] traffic behavior behavior1]{lang="EN-US"}

[\[Sysname-behavior-behavior1\] car cir 1600]{lang="EN-US"}

[\[Sysname-behavior-behavior1\] primap pre-defined color dscp-dp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1865730554}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table color]{lang="EN-US"}**]{#struct_0_14687_18620_x1149086864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap color-map-dp]{lang="EN-US"}**]{#struct_0_14687_18620_1128266658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primap pre-defined ]{lang="EN-US"}**]{#struct_0_14687_18620_x1950790929}
:::

::: {#-1895218117 .myid}
[]{#_Toc404792296}[]{#struct_0_14687_18620_x1405270940}[]{#_Toc307323571}

**QoS策略 \-- 定义流行为的命令 \-- redirect**

------------------------------------------------------------------------

[**[redirect]{lang="EN-US"}**]{#struct_0_14687_18620_1725151938}[命令用来为流行为配置流量重定向动作。]{style="font-family:宋体"}

[**[undo redirect]{lang="EN-US"}**]{#struct_0_14687_18620_x1298749348}[命令用来取消流量重定向动作配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2030357830}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_1335057927}

[**[redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \[ **vlan** *vlan-id* \] \| **vsi** *vsi-name* }]{lang="EN-US"}]{#struct_0_14687_18620_2047929422}

[**[undo redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* }]{lang="EN-US"}]{#struct_0_14687_18620_x1501474947}

[[分布式设备]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_14687_18620_1334599168}[独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \[ **vlan** *vlan-id* \] \| **vsi** *vsi-name* \| **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_14687_18620_603145391}

[**[undo redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* \| **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_14687_18620_111438766}

[[分布式设备]{style="font-family:宋体"}[-IRF]{lang="EN-US"}]{#struct_0_14687_18620_1334533632}[模式：]{style="font-family:宋体"}

[**[redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \[ **vlan** *vlan-id* \] \| **vsi** *vsi-name* \| **chassis** *chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_14687_18620_x535066350}

[**[undo redirect]{lang="EN-US"}**[ { **cpu** \| **failover-group** *group-name* \| **interface** *interface-type interface-number* \| **vsi** *vsi-name* \| **chassis** *chassis-number* **slot** *slot-number* }]{lang="EN-US"}]{#struct_0_14687_18620_1334730240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1045047182}

[[没有配置流量重定向动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1128332194}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x431416014}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x189859492}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1282544952}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_965232952}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x764054666}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1199764169}

[**[cpu]{lang="EN-US"}**]{#struct_0_14687_18620_975579838}[：重定向到]{style="font-family:宋体"}[CPU]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[failover-group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_14687_18620_1334664704}[：重定向到备份组。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示备份组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**]{#struct_0_14687_18620_1127742371}[：重定向到指定的接口。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1016980292}[：指定接口类型和接口编号（对于重定向到隧道来说，接口类型是]{style="font-family:宋体"}**[tunnel]{lang="EN-US"}**[；对于重定向到二层聚合接口来说，接口类型是]{style="font-family:宋体"}**[bridge-aggregation]{lang="EN-US"}**[；对于重定向到三层聚合接口来说，接口类型是]{style="font-family:宋体"}**[route-aggregation]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_x268253215}[：对重定向到接口的报文封装的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为封装的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vsi]{lang="EN-US"}***[ vsi-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1663000041}[：重定向到指定]{style="font-family:宋体"}[VSI]{lang="EN-US"}[（]{style="font-family:宋体"}[Virtual Station Interface]{lang="EN-US"}[，虚拟服务器接口）]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[vsi-name]{lang="EN-US"}*[：表示指定的]{style="font-family:宋体"}[VSI]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_1059209837}*[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[重定向到]{style="font-family:宋体"}[指定的单板，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x1986987836}*[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[重定向到]{style="font-family:宋体"}[指定成员设备，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x346150234}*[ slot-number]{lang="EN-US"}*[：]{style="font-family:宋体"}[重定向到]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_1536054669}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[重定向到]{style="font-family:宋体"}[指定成员设备上的指定单板，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_x274394934}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：]{style="font-family:宋体"}[重定向到]{style="font-family:宋体"}[指定的单板，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x930251150}

[[在配置重定向动作时，同一个流行为中重定向类型只能为重定向到]{style="font-family:宋体"}[CPU]{lang="EN-US"}]{#struct_0_14687_18620_367095121}[、重定向到接口、重定向到]{style="font-family:宋体"}[VSI]{lang="EN-US"}[、重定向到单板、重定向到备份组中的一种，以最后一次配置为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_674739937}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1816124603}[为流行为配置流量重定向动作，重定向到]{style="font-family:宋体"}[CPU cpu]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1662803433}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] redirect cpu]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_215367463}[为流行为配置流量重定向动作，重定向到接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1127807907}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] redirect interface gigabitethernet1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_85630075}[为流行为配置流量重定向动作，重定向到]{style="font-family:宋体"}[VSI aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1662868969}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] redirect vsi aaa]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1334271488}[为流行为配置流量重定向动作，重定向到]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1307533126}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] redirect slot 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_994418789}[为流行为配置流量重定向动作，重定向到备份组]{style="font-family:宋体"}[bakgrp1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1737693889}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] redirect failover-group bakgrp1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1306771005}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[classifier behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x1662543836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_x900082604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_1742931784}
:::

::: {#2064325960 .myid}
[]{#_Toc404792297}[]{#struct_0_14687_18620_x1100499119}[]{#_Toc327195748}[]{#_Toc291486418}

**QoS策略 \-- 定义流行为的命令 \-- remark customer-vlan-id**

------------------------------------------------------------------------

[**[remark customer-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x594678925}[命令用来重标记报文的]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo remark customer-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x482049652}[命令用来取消重标记报文的]{style="font-family:
宋体"}[CVLAN]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x305065020}

[**[remark customer-vlan-id]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_14687_18620_1127611299}

[**[undo remark customer-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x1405573056}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_676843907}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1734018334}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1614759435}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_213830919}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1630681147}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x366043079}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1336705490}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127676835}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_905333349}[：表示重标记报文内层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[）的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1886657164}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x703439441}[在流行为]{style="font-family:宋体"}[b1]{lang="EN-US"}[上配置重标记报文的]{style="font-family:宋体"}[CVLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 111]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x587593000}

[\[Sysname\] traffic behavior b1]{lang="EN-US"}

[\[Sysname-behavior-b1\] remark customer-vlan-id 111]{lang="EN-US"}
:::

::: {#1290301749 .myid}
[]{#_Toc404792298}[]{#struct_0_14687_18620_350408751}

**QoS策略 \-- 定义流行为的命令 \-- remark dot1p**

------------------------------------------------------------------------

[**[remark dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x2120517319}[命令用来重新标记报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级或配置内外层标签优先级复制功能。]{style="font-family:宋体"}

[**[undo remark dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_1128004515}[命令用来取消标记报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级或内外层标签优先级复制功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x387423885}

[**[remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **dot1p** *dot1p-value*]{lang="EN-US"}]{#struct_0_14687_18620_2039533655}

[**[undo remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **dot1p**]{lang="EN-US"}]{#struct_0_14687_18620_707165531}

[**[remark]{lang="EN-US"}**[ **dot1p** **customer-dot1p-trust**]{lang="EN-US"}]{#struct_0_14687_18620_x1673693141}

[**[undo remark]{lang="EN-US"}**[ **dot1p**]{lang="EN-US"}]{#struct_0_14687_18620_x1777878728}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1078241324}

[[没有配置重新标记报文的动作或没有配置内外层标签优先级复制功能。]{style="font-family:宋体"}]{#struct_0_14687_18620_531480748}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_136996684}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1128070051}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_353121251}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1180895859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2136347796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_582463635}

[**[green]{lang="EN-US"}**]{#struct_0_14687_18620_997735023}[：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_1394561845}[：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_x757800085}[：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_1127873443}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[customer-dot1p-trust]{lang="EN-US"}**]{#struct_0_14687_18620_x629043027}[：]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略应用到端口后，将内层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级复制为外层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}[的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_535125574}

[[命令]{style="font-family:宋体"}**[remark dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_1443155268}[和]{style="font-family:宋体"}**[remark dot1p customer-dot1p-trust]{lang="EN-US"}**[是覆盖关系。]{style="font-family:
宋体"}

[[如果报文只携带一层]{style="font-family:宋体"}[VLAN tag]{lang="EN-US"}]{#struct_0_14687_18620_x316742168}[，则配置]{style="font-family:宋体"}**[remark dot1p customer-dot1p-trust]{lang="EN-US"}**[不会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1901663864}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1181846451}[重新标记报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1652964142}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark dot1p 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1127938979}[配置内外层标签优先级复制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_94099348}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark dot1p customer-dot1p-trust]{lang="EN-US"}
:::

::: {#-1903846230 .myid}
[]{#_Toc404792299}[]{#struct_0_14687_18620_788785034}[]{#_Toc298419667}[]{#_Toc263759902}[]{#_Toc226262565}[]{#_Toc198110103}

**QoS策略 \-- 定义流行为的命令 \-- remark drop-precedence**

------------------------------------------------------------------------

[**[remark drop-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_1367236344}[命令用来重新标记报文的丢弃优先级。]{style="font-family:宋体"}

[**[undo remark drop-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_598871988}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x991086896}

[**[remark drop-precedence]{lang="EN-US"}**[ *drop-precedence-value*]{lang="EN-US"}]{#struct_0_14687_18620_x261681554}

[**[undo remark drop-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1142647260}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1128266659}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1950725393}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x300876237}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x119219427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x409206218}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1394812427}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1138514832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x642338891}

[*[drop-precedence-value]{lang="EN-US"}*]{#struct_0_14687_18620_1853666779}[：丢弃优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1128332195}

[[本命令仅应用在入方向。]{style="font-family:宋体"}]{#struct_0_14687_18620_x431481550}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x586125829}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1550879599}[重新标记报文的丢弃优先级值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1094036402}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark drop-precedence 2]{lang="EN-US"}
:::

::: {#-580725274 .myid}
[]{#_Toc404792300}[]{#struct_0_14687_18620_x1149655406}[]{#_Toc298419668}[]{#_Toc263759903}[]{#_Toc226262566}[]{#_Toc198110104}

**QoS策略 \-- 定义流行为的命令 \-- remark dscp**

------------------------------------------------------------------------

[**[remark dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1139712482}[命令用来重新标记报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo remark dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x1451229720}[命令用来取消标记报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1127742368}

[**[remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **dscp** *dscp-value*]{lang="EN-US"}]{#struct_0_14687_18620_x1016521541}

[**[undo remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **dscp**]{lang="EN-US"}]{#struct_0_14687_18620_1688476231}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x521510874}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x2075000515}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x633948861}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x64780339}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1109025473}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x19008150}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1127807904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1306836541}

[**[green]{lang="EN-US"}**]{#struct_0_14687_18620_x134214628}[：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_x1148186749}[：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_1163179850}[：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_282207093}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所示。]{style="font-family:宋体"}

[]{#struct_0_14687_18620_737093474}[[表1-5 ]{lang="EN-US"}[DSCP]{lang="EN-US"}]{#_Ref163816081}[关键字与值的对应表]{style="font-family:黑体"}

[]{#table_struct_0_1641569689}[[关键字]{style="font-family:黑体"}]{#struct_0_14687_18620_1127611296}
:::

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1404590016}[值（二进制）]{style="font-family:黑体"}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x532381592}[值（十进制）]{style="font-family:黑体"}

[[default]{lang="EN-US"}]{#struct_0_14687_18620_x929927763}

[[000000]{lang="EN-US"}]{#struct_0_14687_18620_492932380}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_x1518109553}

[[af11]{lang="EN-US"}]{#struct_0_14687_18620_1127676832}

[[001010]{lang="EN-US"}]{#struct_0_14687_18620_905529957}

[[10]{lang="EN-US"}]{#struct_0_14687_18620_1843491609}

[[af12]{lang="EN-US"}]{#struct_0_14687_18620_x723404819}

[[001100]{lang="EN-US"}]{#struct_0_14687_18620_26619628}

[[12]{lang="EN-US"}]{#struct_0_14687_18620_x1390007077}

[[af13]{lang="EN-US"}]{#struct_0_14687_18620_1128004512}

[[001110]{lang="EN-US"}]{#struct_0_14687_18620_x387882637}

[[14]{lang="EN-US"}]{#struct_0_14687_18620_916937785}

[[af21]{lang="EN-US"}]{#struct_0_14687_18620_x269704655}

[[010010]{lang="EN-US"}]{#struct_0_14687_18620_x1701252144}

[[18]{lang="EN-US"}]{#struct_0_14687_18620_1128070048}

[[af22]{lang="EN-US"}]{#struct_0_14687_18620_353711076}

[[010100]{lang="EN-US"}]{#struct_0_14687_18620_x1922691981}

[[20]{lang="EN-US"}]{#struct_0_14687_18620_x1835384323}

[[af23]{lang="EN-US"}]{#struct_0_14687_18620_1127873440}

[[010110]{lang="EN-US"}]{#struct_0_14687_18620_x628846419}

[[22]{lang="EN-US"}]{#struct_0_14687_18620_x1773987674}

[[af31]{lang="EN-US"}]{#struct_0_14687_18620_809055564}

[[011010]{lang="EN-US"}]{#struct_0_14687_18620_1752813502}

[[26]{lang="EN-US"}]{#struct_0_14687_18620_1127938976}

[[af32]{lang="EN-US"}]{#struct_0_14687_18620_94820244}

[[011100]{lang="EN-US"}]{#struct_0_14687_18620_x868730103}

[[28]{lang="EN-US"}]{#struct_0_14687_18620_x1449909913}

[[af33]{lang="EN-US"}]{#struct_0_14687_18620_1128266656}

[[011110]{lang="EN-US"}]{#struct_0_14687_18620_x1949873425}

[[30]{lang="EN-US"}]{#struct_0_14687_18620_x775634837}

[[af41]{lang="EN-US"}]{#struct_0_14687_18620_1378997547}

[[100010]{lang="EN-US"}]{#struct_0_14687_18620_1128332192}

[[34]{lang="EN-US"}]{#struct_0_14687_18620_x431809230}

[[af42]{lang="EN-US"}]{#struct_0_14687_18620_x1015606443}

[[100100]{lang="EN-US"}]{#struct_0_14687_18620_x1580920045}

[[36]{lang="EN-US"}]{#struct_0_14687_18620_1127742369}

[[af43]{lang="EN-US"}]{#struct_0_14687_18620_x1016456005}

[[100110]{lang="EN-US"}]{#struct_0_14687_18620_x1410845565}

[[38]{lang="EN-US"}]{#struct_0_14687_18620_1127807905}

[[cs1]{lang="EN-US"}]{#struct_0_14687_18620_1306902077}

[[001000]{lang="EN-US"}]{#struct_0_14687_18620_x1256965744}

[[8]{lang="EN-US"}]{#struct_0_14687_18620_x251183163}

[[cs2]{lang="EN-US"}]{#struct_0_14687_18620_1127611297}

[[010000]{lang="EN-US"}]{#struct_0_14687_18620_x1404655552}

[[16]{lang="EN-US"}]{#struct_0_14687_18620_673636763}

[[cs3]{lang="EN-US"}]{#struct_0_14687_18620_1127676833}

[[011000]{lang="EN-US"}]{#struct_0_14687_18620_905464421}

[[24]{lang="EN-US"}]{#struct_0_14687_18620_x1990299638}

[[cs4]{lang="EN-US"}]{#struct_0_14687_18620_x686335179}

[[100000]{lang="EN-US"}]{#struct_0_14687_18620_1128004513}

[[32]{lang="EN-US"}]{#struct_0_14687_18620_x387817101}

[[cs5]{lang="EN-US"}]{#struct_0_14687_18620_495231807}

[[101000]{lang="EN-US"}]{#struct_0_14687_18620_1128070049}

[[40]{lang="EN-US"}]{#struct_0_14687_18620_353645540}

[[cs6]{lang="EN-US"}]{#struct_0_14687_18620_792774165}

[[110000]{lang="EN-US"}]{#struct_0_14687_18620_1127873441}

[[48]{lang="EN-US"}]{#struct_0_14687_18620_x628911955}

[[cs7]{lang="EN-US"}]{#struct_0_14687_18620_x1849854382}

[[111000]{lang="EN-US"}]{#struct_0_14687_18620_1127938977}

[[56]{lang="EN-US"}]{#struct_0_14687_18620_94754708}

[[ef]{lang="EN-US"}]{#struct_0_14687_18620_x709155282}

[[101110]{lang="EN-US"}]{#struct_0_14687_18620_1128266657}

[[46]{lang="EN-US"}]{#struct_0_14687_18620_x1949807889}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_517666310}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1270192484}[重新标记报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1128332193}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark dscp 6]{lang="EN-US"}

::: {#-1210551591 .myid}
[]{#_Toc404792301}[]{#struct_0_14687_18620_x431874766}[]{#_Toc298419669}[]{#_Toc263759904}[]{#_Toc226262568}[]{#_Toc198110106}[]{#_Toc232219776}[]{#_Toc232395361}[]{#_Toc232395737}[]{#_Toc232219777}[]{#_Toc232395362}[]{#_Toc232395738}[]{#_Toc232219778}[]{#_Toc232395363}[]{#_Toc232395739}[]{#_Toc232219779}[]{#_Toc232395364}[]{#_Toc232395740}[]{#_Toc232219780}[]{#_Toc232395365}[]{#_Toc232395741}[]{#_Toc232219781}[]{#_Toc232395366}[]{#_Toc232395742}[]{#_Toc232219782}[]{#_Toc232395367}[]{#_Toc232395743}[]{#_Toc232219783}[]{#_Toc232395368}[]{#_Toc232395744}[]{#_Toc232219784}[]{#_Toc232395369}[]{#_Toc232395745}[]{#_Toc232219785}[]{#_Toc232395370}[]{#_Toc232395746}[]{#_Toc232219786}[]{#_Toc232395371}[]{#_Toc232395747}[]{#_Toc232219787}[]{#_Toc232395372}[]{#_Toc232395748}[]{#_Toc232219788}[]{#_Toc232395373}[]{#_Toc232395749}[]{#_Toc232219789}[]{#_Toc232395374}[]{#_Toc232395750}[]{#_Toc232219792}[]{#_Toc232395377}[]{#_Toc232395753}

**QoS策略 \-- 定义流行为的命令 \-- remark ip-precedence**

------------------------------------------------------------------------

[**[remark ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_225513641}[命令用来重新标记报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo remark ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1349690228}[命令用来取消标记报文的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_968192012}

[**[remark]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **green** \| **red** \| **yellow** \] **ip-precedence** *ip-precedence-value*]{lang="EN-US"}]{#struct_0_14687_18620_27104868}

[**[undo remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **ip-precedence**]{lang="EN-US"}]{#struct_0_14687_18620_x29303231}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601140983}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1565363270}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x576081472}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1768321794}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1755413002}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_560943047}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_450433904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1715984330}

[**[green]{lang="EN-US"}**]{#struct_0_14687_18620_x1601075447}[：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_x2125925572}[：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_1841594452}[：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-precedence-value]{lang="EN-US"}*]{#struct_0_14687_18620_1397846212}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1041842394}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_840849823}[重新标记报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_526115302}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark ip-precedence 6]{lang="EN-US"}
:::

::: {#-527874778 .myid}
[]{#_Toc404792302}[]{#struct_0_14687_18620_x1601272055}[]{#_Toc298419670}[]{#_Toc263759905}[]{#_Toc226262569}[]{#_Toc198110107}

**QoS策略 \-- 定义流行为的命令 \-- remark local-precedence**

------------------------------------------------------------------------

[**[remark local-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1093149578}[命令用来重新标记报文的本地优先级。]{style="font-family:宋体"}

[**[undo remark local-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_1154554187}[命令用来取消标记报文的本地优先级。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_517493258}

[**[remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **local-precedence** *local-precedence-value*]{lang="EN-US"}]{#struct_0_14687_18620_207490090}

[**[undo remark ]{lang="EN-US"}**[\[ **green** \| **red** \| **yellow** \] **local-precedence**]{lang="EN-US"}]{#struct_0_14687_18620_1253254973}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x806464792}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_x2036087851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601206519}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x543772484}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x944822206}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1829820260}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1499263576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x849709643}

[**[green]{lang="EN-US"}**]{#struct_0_14687_18620_x21615904}[：对绿色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_x963181997}[：对红色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_x1176595115}[：对黄色报文进行重标记。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[local-precedence-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1600878839}[：本地优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2014293625}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2060163727}[重新标记报文的本地优先级值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x617241415}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark local-precedence 2]{lang="EN-US"}
:::

::: {#1324038445 .myid}
[]{#_Toc226262574}[]{#_Toc198110112}[]{#_Toc404792303}[]{#struct_0_14687_18620_x1567072928}[]{#_Toc298419671}[]{#_Toc263759906}[]{#_Toc231802637}[]{#_Toc226447927}[]{#_Toc226262571}[]{#_Toc198110109}[]{#_Toc232219795}[]{#_Toc232395380}[]{#_Toc232395756}[]{#_Toc232219796}[]{#_Toc232395381}[]{#_Toc232395757}[]{#_Toc232219797}[]{#_Toc232395382}[]{#_Toc232395758}[]{#_Toc232219798}[]{#_Toc232395383}[]{#_Toc232395759}[]{#_Toc232219799}[]{#_Toc232395384}[]{#_Toc232395760}[]{#_Toc232219800}[]{#_Toc232395385}[]{#_Toc232395761}[]{#_Toc232219801}[]{#_Toc232395386}[]{#_Toc232395762}[]{#_Toc232219802}[]{#_Toc232395387}[]{#_Toc232395763}[]{#_Toc232219803}[]{#_Toc232395388}[]{#_Toc232395764}[]{#_Toc232219804}[]{#_Toc232395389}[]{#_Toc232395765}[]{#_Toc232219805}[]{#_Toc232395390}[]{#_Toc232395766}[]{#_Toc232219806}[]{#_Toc232395391}[]{#_Toc232395767}[]{#_Toc232219807}[]{#_Toc232395392}[]{#_Toc232395768}[]{#_Toc232219808}[]{#_Toc232395393}[]{#_Toc232395769}[]{#_Toc232219809}[]{#_Toc232395394}[]{#_Toc232395770}[]{#_Toc232219814}[]{#_Toc232395399}[]{#_Toc232395775}[]{#_Toc232219815}[]{#_Toc232395400}[]{#_Toc232395776}[]{#_Toc232219817}[]{#_Toc232395402}[]{#_Toc232395778}[]{#_Toc232219818}[]{#_Toc232395403}[]{#_Toc232395779}[]{#_Toc232219819}[]{#_Toc232395404}[]{#_Toc232395780}[]{#_Toc232219820}[]{#_Toc232395405}[]{#_Toc232395781}[]{#_Toc232219821}[]{#_Toc232395406}[]{#_Toc232395782}[]{#_Toc232219822}[]{#_Toc232395407}[]{#_Toc232395783}[]{#_Toc232219823}[]{#_Toc232395408}[]{#_Toc232395784}[]{#_Toc232219824}[]{#_Toc232395409}[]{#_Toc232395785}[]{#_Toc232219825}[]{#_Toc232395410}[]{#_Toc232395786}[]{#_Toc232219826}[]{#_Toc232395411}[]{#_Toc232395787}[]{#_Toc232219827}[]{#_Toc232395412}[]{#_Toc232395788}[]{#_Toc232219831}[]{#_Toc232395416}[]{#_Toc232395792}[]{#_Toc232219832}[]{#_Toc232395417}[]{#_Toc232395793}[]{#_Toc232219833}[]{#_Toc232395418}[]{#_Toc232395794}[]{#_Toc232219834}[]{#_Toc232395419}[]{#_Toc232395795}[]{#_Toc232219835}[]{#_Toc232395420}[]{#_Toc232395796}[]{#_Toc232219836}[]{#_Toc232395421}[]{#_Toc232395797}[]{#_Toc232219837}[]{#_Toc232395422}[]{#_Toc232395798}[]{#_Toc232219838}[]{#_Toc232395423}[]{#_Toc232395799}[]{#_Toc232219839}[]{#_Toc232395424}[]{#_Toc232395800}[]{#_Toc232219840}[]{#_Toc232395425}[]{#_Toc232395801}[]{#_Toc232219841}[]{#_Toc232395426}[]{#_Toc232395802}[]{#_Toc232219842}[]{#_Toc232395427}[]{#_Toc232395803}[]{#_Toc232219843}[]{#_Toc232395428}[]{#_Toc232395804}[]{#_Toc232219844}[]{#_Toc232395429}[]{#_Toc232395805}[]{#_Toc232219845}[]{#_Toc232395430}[]{#_Toc232395806}[]{#_Toc232219846}[]{#_Toc232395431}[]{#_Toc232395807}

**QoS策略 \-- 定义流行为的命令 \-- remark qos-local-id**

------------------------------------------------------------------------

[**[remark qos-local-id]{lang="EN-US"}**]{#struct_0_14687_18620_1347144988}[命令用来重新标记报文的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo remark qos-local-id]{lang="EN-US"}**]{#struct_0_14687_18620_1292923203}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600813303}

[**[remark qos-local-id ]{lang="EN-US"}***[local-id-value]{lang="EN-US"}*]{#struct_0_14687_18620_x139372962}

[**[undo remark qos-local-id]{lang="EN-US"}**]{#struct_0_14687_18620_x1500460178}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x559269717}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_1098261028}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1972823122}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1242015900}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_225502725}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x168105896}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1601009911}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x57977456}

[*[local-id-value]{lang="EN-US"}*]{#struct_0_14687_18620_831640847}[：]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1967865059}

[[一般情况下，在]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_1067796327}[策略的入方向对报文的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值进行标记，在]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的出方向根据标记的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值对报文进行分类以及指定相应的流行为，两者要结合使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_942935823}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1818425062}[重新标记报文的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1600944375}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] remark qos-local-id 2]{lang="EN-US"}
:::

::: {#-139963787 .myid}
[]{#_Toc298419672}[]{#_Toc263759907}[]{#_Toc404792304}[]{#struct_0_14687_18620_921674423}[]{#_Toc327195755}[]{#_Toc291486419}[]{#_Toc226447928}[]{#_Toc226262572}[]{#_Toc198110110}

**QoS策略 \-- 定义流行为的命令 \-- remark service-vlan-id**

------------------------------------------------------------------------

[**[remark service-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x179702469}[命令用来重标记报文的]{style="font-family:宋体"}[SVLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo remark service-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x2010125354}[命令用来取消重标记报文的]{style="font-family:
宋体"}[SVLAN]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1230807002}

[**[remark service-vlan-id ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_x2072526033}

[**[undo remark service-vlan-id]{lang="EN-US"}**]{#struct_0_14687_18620_x365535129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2014746582}

[[没有配置重新标记报文的动作。]{style="font-family:宋体"}]{#struct_0_14687_18620_647538616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600616695}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1349163705}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x427438308}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1896503760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1239424382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1758838221}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1254036537}[：表示重标记报文外层]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[（]{style="font-family:宋体"}[SVLAN]{lang="EN-US"}[）的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2020944589}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1600551159}[在流行为]{style="font-family:宋体"}[b1]{lang="EN-US"}[上配置重标记报文的]{style="font-family:宋体"}[SVLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 222]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1093639818}

[\[Sysname\] traffic behavior b1]{lang="EN-US"}

[\[Sysname-behavior-b1\] remark service-vlan-id 222]{lang="EN-US"}
:::

::: {#467432228 .myid}
[]{#_Toc404792305}[]{#struct_0_14687_18620_x256819465}

**QoS策略 \-- 定义流行为的命令 \-- traffic behavior**

------------------------------------------------------------------------

[**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x755227832}[命令用来定义一个流行为，并进入流行为视图。]{style="font-family:宋体"}

[**[undo traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_1714274728}[命令用来删除一个流行为。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1389942736}

[**[traffic behavior]{lang="EN-US"}**[ *behavior-name*]{lang="EN-US"}]{#struct_0_14687_18620_x33583852}

[**[undo traffic behavior]{lang="EN-US"}**[ *behavior-name*]{lang="EN-US"}]{#struct_0_14687_18620_x1601140982}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_14687_18620_x720671}

[[没有定义流行为。]{style="font-family:宋体"}]{#struct_0_14687_18620_892704568}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_296021920}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_884545228}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x78875715}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_398631648}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_731273165}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1847883324}

[*[behavior-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1601075446}[：流行为名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x559841631}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1218478476}[定义一个名为]{style="font-family:宋体"}[behavior1]{lang="EN-US"}[的流行为。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x440594196}

[\[Sysname\] traffic behavior behavior1]{lang="EN-US"}

[\[Sysname-behavior-behavior1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1401471284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x746526745}
:::

::: {#-860699747 .myid}
[]{#_Toc404792306}[]{#struct_0_14687_18620_x951495280}[]{#_Toc327195757}[]{#_Toc325978421}[]{#_Toc198110113}

**QoS策略 \-- 定义流行为的命令 \-- traffic-policy**

------------------------------------------------------------------------

[**[traffic-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1601272054}[命令用来在父策略流行为视图下应用一个子策略。]{style="font-family:宋体"}

[**[undo traffic-policy]{lang="EN-US"}**]{#struct_0_14687_18620_472934363}[命令用来删除关联的子策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x77759347}

[**[traffic-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14687_18620_x1457883393}

[**[undo traffic-policy]{lang="EN-US"}**]{#struct_0_14687_18620_1756345885}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1937973724}

[[没有配置嵌套策略]{style="font-family:宋体"}]{#struct_0_14687_18620_2070557895}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x868651097}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1063479768}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601206518}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2109856425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1718598639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_425976572}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1251423894}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果策略不存在，则自动创建该策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x176487493}

[[通过在流行为视图下应用子策略，可以实现策略嵌套功能。即由]{style="font-family:宋体"}**[traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_2011908493}[命令定义的某一类流量，除了执行父策略中定义的行为外，还由子策略再次对该类流量进行分类，并执行子策略中定义的行为。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14687_18620_1133878314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在父策略行为下应用子策略时，最多只能嵌套二层策略，并且不能嵌套自己。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1600878838}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个流行为中至多只能嵌套一个子策略。]{style="font-family:宋体"}]{#struct_0_14687_18620_x714589730}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果子策略中配置了]{style="font-family:宋体"}]{#struct_0_14687_18620_x333002488}[CBQ]{lang="EN-US"}[，那么父策略中必须配置]{style="font-family:宋体"}[GTS]{lang="EN-US"}[，并且配置的父策略]{style="font-family:宋体"}[GTS]{lang="EN-US"}[带宽必须大于子策略]{style="font-family:宋体"}[CBQ]{lang="EN-US"}[带宽，否则配置失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[嵌套策略时，如果父策略的]{style="font-family:宋体"}]{#struct_0_14687_18620_x333068024}[GTS]{lang="EN-US"}[配置采用百分比形式，则子策略]{style="font-family:宋体"}[CBQ]{lang="EN-US"}[带宽配置不允许采用绝对值形式；]{style="font-family:宋体"}[如果父策略的]{style="font-family:宋体"}[GTS]{lang="EN-US"}[配置采用绝对值形式，则子策略]{style="font-family:宋体"}[CBQ]{lang="EN-US"}[带宽配置既可以采用百分比形式，也可以采用绝对值形式]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[子策略中不允许配置]{style="font-family:宋体"}]{#struct_0_14687_18620_1021706939}[GTS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[嵌套策略支持对]{style="font-family:宋体"}]{#struct_0_14687_18620_x780187060}[IPv4]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的处理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果嵌套策略已经应用在接口上，则不允许删除嵌套的子策略，必须先解除子策略和父策略的嵌套关系。]{style="font-family:宋体"}]{#struct_0_14687_18620_984785461}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1791725561}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x52120042}[配置策略嵌套，在父策略下应用子策略]{style="font-family:宋体"}[child]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1306853197}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] traffic-policy child]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600813302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic classifier]{lang="EN-US"}**]{#struct_0_14687_18620_1426710979}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_496907142}
:::

::: {#2104565970 .myid}
[]{#_Toc404792308}[]{#struct_0_14687_18620_1256665529}[]{#_Toc298419674}[]{#_Toc263759910}[]{#_Toc226262577}[]{#_Toc198110115}

**QoS策略 \-- 定义策略和应用策略的命令 \-- classifier behavior**

------------------------------------------------------------------------

[**[classifier behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x1100554810}[命令用来为类指定流行为。]{style="font-family:宋体"}

[**[undo classifier]{lang="EN-US"}**]{#struct_0_14687_18620_x1648040717}[命令用来取消为类指定的流行为。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x259671323}

[**[classifier]{lang="EN-US"}**[ *classifier-name* **behavior** *behavior-name* \[ **mode** { **dcbx** \| **qppb-manipulation** } \]]{lang="EN-US"}]{#struct_0_14687_18620_x1601009910}

[**[undo classifier]{lang="EN-US"}***[ classifier-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1624061397}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1738406847}

[[没有为类指定流行为。]{style="font-family:宋体"}]{#struct_0_14687_18620_1606101852}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1029347432}

[[策略视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2144682133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_960787050}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1817330297}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1833761471}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600944374}

[*[classifier-name]{lang="EN-US"}*]{#struct_0_14687_18620_x644409518}[：类名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[behavior-name]{lang="EN-US"}*]{#struct_0_14687_18620_891235009}[：流行为名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[mode dcbx]{lang="EN-US"}**]{#struct_0_14687_18620_1304305430}[：表示该策略为]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Center Bridging Exchange Protocol]{lang="EN-US"}[，数据中心桥能力交换协议）模式。有关]{style="font-family:宋体"}[DCBX]{lang="EN-US"}[的介绍，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[以太网交换配置指导"中的"]{style="font-family:宋体"}[LLDP]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode qppb-manipulation]{lang="EN-US"}**]{#struct_0_14687_18620_x1517867903}[：]{style="font-family:宋体"}[设置类和流行为对应关系用于匹配]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由策略中]{style="font-family:宋体"}**[apply qos-local-id]{lang="EN-US"}**[的信息。即类中]{style="font-family:宋体"}**[if-match qos-local-id]{lang="EN-US"}**[匹配的内容]{style="font-family:宋体"}[对应路由策略命令中]{style="font-family:宋体"}**[apply qos-local-id]{lang="EN-US"}**[命令设置的信息，具体内容请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由配置指导"中的"路由策略"。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1161784087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[策略下每个类只能与一个流行为关联。]{style="font-family:宋体"}]{#struct_0_14687_18620_1490298319}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置本命令时指定的类和流行为不存在，系统将创建一个空的类和空的流行为。]{style="font-family:宋体"}]{#struct_0_14687_18620_313635862}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_14687_18620_x1735937778}**[undo]{lang="EN-US"}**[命令指定的类为系统预定义类]{style="font-family:宋体"}[default-class]{lang="EN-US"}[，表示恢复]{style="font-family:宋体"}[default-class]{lang="EN-US"}[对应的流行为为系统预定义流行为]{style="font-family:宋体"}[be]{lang="EN-US"}[，而不是取消对应的流行为。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}**[mode]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ **dcbx** \| **qppb-manipulation** }]{lang="EN-US"}]{#struct_0_14687_18620_x1600616694}[参数]{lang="EN-US" style="font-family:宋体"}[，对于类和流行为的配置会存在一些特殊限制，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1379719650}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_292833699}[在策略]{style="font-family:宋体"}[user1]{lang="EN-US"}[中为类]{style="font-family:宋体"}[database]{lang="EN-US"}[指定采用流行为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x725140083}

[\[Sysname\] qos policy user1]{lang="EN-US"}

[\[Sysname-qospolicy-user1\] classifier database behavior test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1517867898}[在策略]{style="font-family:宋体"}[user1]{lang="EN-US"}[中为类]{style="font-family:宋体"}[database]{lang="EN-US"}[指定采用流行为]{style="font-family:宋体"}[test]{lang="EN-US"}[，对应关系用于匹配]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由策略中]{style="font-family:宋体"}**[apply qos-local-id]{lang="EN-US"}**[的信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x62899781}

[\[Sysname\] qos policy user1]{lang="EN-US"}

[\[Sysname-qospolicy-user1\] classifier database behavior test mode qppb-manipulation]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x154664756}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_911089762}
:::

::: {#-2078986776 .myid}
[]{#_Toc404792309}[]{#struct_0_14687_18620_2108004434}[]{#_Toc298419675}[]{#_Toc263759911}[]{#_Toc226262578}[]{#_Toc198110116}[]{#_Toc191699843}[]{#_Toc189799345}[]{#_Toc133401306}

**QoS策略 \-- 定义策略和应用策略的命令 \-- control-plane**

------------------------------------------------------------------------

[**[control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_x1600551158}[命令用来进入控制平面视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1635243537}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_2079306}

[**[control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_1474093192}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_914991513}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[control-plane]{lang="EN-US"}**[ **slot** *slot-number* ]{lang="EN-US"}[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1075116811}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x327496393}[模式：]{style="font-family:宋体"}

[**[control-plane chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_796465193}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1335644740}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1601140985}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_402563856}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x731265927}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_270047975}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1219939998}

[]{#OLE_LINK3}[]{#OLE_LINK2}[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x2048374896}[：指定单板。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1265736050}[：指定成员设备。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x286817239}[：指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1019867374}[：指定成员设备上指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1649040576}[：指定单板。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_1793055873}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1852901180}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1601075449}[进入控制平面视图。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1362472670}

[\[Sysname\] control-plane]{lang="EN-US"}

[\[Sysname-cp\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x698729349}[进入]{style="font-family:宋体"}[3]{lang="EN-US"}[号板控制平面视图。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1133048616}

[\[Sysname\] control-plane slot 3]{lang="EN-US"}

[\[Sysname-cp-slot3\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1718661109}[进入]{style="font-family:宋体"}[3]{lang="EN-US"}[号成员设备控制平面视图。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1111986247}

[\[Sysname\] control-plane slot 3]{lang="EN-US"}

[\[Sysname-cp-slot3\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1434194632}[进入]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[号板控制平面视图。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1601272057}

[\[Sysname\] control-plane chassis 1 slot 3]{lang="EN-US"}

[\[Sysname-cp-chassis1-slot3\]]{lang="EN-US"}
:::

::: {#-93667434 .myid}
[]{#_Toc298419676}[]{#_Toc263759912}[]{#_Toc226262579}[]{#_Toc198110117}[]{#_Toc404792310}[]{#struct_0_14687_18620_2039018304}[]{#_Toc353798054}[]{#_Toc351557499}[]{#_Toc347748658}

**QoS策略 \-- 定义策略和应用策略的命令 \-- control-plane management**

------------------------------------------------------------------------

[**[control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_1059237234}[命令用来进入管理口控制平面视图。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_833221907}

[**[control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_x1601206521}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x187476588}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1435643432}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600878841}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1658390945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_722674999}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x579521791}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1600813305}[进入管理口控制平面视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_667196092}

[\[Sysname\] control-plane management]{lang="EN-US"}

[\[Sysname-cp-management\]]{lang="EN-US"}
:::

::: {#2029732777 .myid}
[]{#_Toc404792311}[]{#struct_0_14687_18620_704124966}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy**

------------------------------------------------------------------------

[**[display qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1930083449}[命令用来显示]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1259536759}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_739723138}

[**[display qos policy]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *policy-name* \[ **classifier** *classifier-name* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x1601009913}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14687_18620_x1220776870}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos policy]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *policy-name* \[ **classifier** *classifier-name* \] \] \[ **slot**]{lang="EN-US"}]{#struct_0_14687_18620_x1908290782}[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_14687_18620_1952030970}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display qos policy]{lang="EN-US"}**[ { **system-defined** \| **user-defined** } \[ *policy-name* \[ **classifier** *classifier-name* \] \] \[]{lang="EN-US"}]{#struct_0_14687_18620_1562977558}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1882489572}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1854126418}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_430038284}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_684402062}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1600944377}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x241124991}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1931755096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_781700524}

[**[system-defined]{lang="EN-US"}**]{#struct_0_14687_18620_2058832244}[：系统定义]{style="font-family:宋体"}[策略]{style="font-family:宋体"}[。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_14687_18620_44052054}[：用户定义策略。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_1887197843}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示所有用户定义策略的配置信息。]{style="font-family:宋体"}

[**[classifier]{lang="EN-US"}***[ classifier-name]{lang="EN-US"}*]{#struct_0_14687_18620_946525480}[：策略中的类名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示策略中所有类相关的配置信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x1600616697}*[ slot-number]{lang="EN-US"}*[：显示指定单板的策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用主控板的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x1783004177}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1232146999}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[策略的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[策略的信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_x1376166315}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示全局主用主控板的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x333936942}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[策略的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的]{style="font-family:宋体"}[策略的信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_1892001724}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[策略的信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1430203455}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1482811160}[显示用户定义策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-defined]{lang="EN-US"}]{#struct_0_14687_18620_x1600551161}

[ ]{lang="EN-US"}

[  User-defined QoS policy information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Policy: 1 (ID 100)]{lang="EN-US"}

[   Classifier: 1 (ID 100)]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[   Classifier: 2 (ID 101)]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable: Packet]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3 (ID 102)]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_737606066}[显示系统定义策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy system-defined]{lang="EN-US"}]{#struct_0_14687_18620_x1601140984}

[ ]{lang="EN-US"}

[  System-defined QoS policy information:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Policy: default (ID 0)]{lang="EN-US"}

[   Classifier: default-class (ID 0)]{lang="EN-US"}

[     Behavior: be]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[   Classifier: ef (ID 1)]{lang="EN-US"}

[     Behavior: ef]{lang="EN-US"}

[      Expedited Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%) Cbs-ratio 25]{lang="EN-US"}

[   Classifier: af1 (ID 2)]{lang="EN-US"}

[     Behavior: af]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%)]{lang="EN-US"}

[        Discard Method: Tail]{lang="EN-US"}

[   Classifier: af2 (ID 3)]{lang="EN-US"}

[     Behavior: af]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%)]{lang="EN-US"}

[        Discard Method: Tail]{lang="EN-US"}

[   Classifier: af3 (ID 4)]{lang="EN-US"}

[     Behavior: af]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%)]{lang="EN-US"}

[        Discard Method: Tail]{lang="EN-US"}

[   Classifier: af4 (ID 5)]{lang="EN-US"}

[     Behavior: af]{lang="EN-US"}

[      Assured Forwarding:]{lang="EN-US"}

[        Bandwidth 20 (%)]{lang="EN-US"}

[[        Discard Method: Tail]{lang="EN-US"}]{#_Ref298401448}

[[表1-6 ]{lang="EN-US"}[display qos policy]{lang="EN-US"}]{#struct_0_14687_18620_x1163520085}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1635262073}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1617247125}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601075448}

[[User-defined QoS policy information]{lang="EN-US"}]{#struct_0_14687_18620_x1366410685}

[[用户自定义策略的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_1890029711}

[[System-defined QoS policy information]{lang="EN-US"}]{#struct_0_14687_18620_1910325049}

[[系统定义策略的信息]{style="font-family:宋体"}]{#struct_0_14687_18620_645817109}

[[Policy]{lang="EN-US"}]{#struct_0_14687_18620_x1415736681}

[[策略名]{style="font-family:宋体"}]{#struct_0_14687_18620_x1601272056}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x689865051}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#-1558328321 .myid}
[]{#_Toc404792312}[]{#struct_0_14687_18620_243436657}[]{#_Toc298419677}[]{#_Toc263759913}[]{#_Toc226262580}[]{#_Toc198110118}[]{#_Toc191699845}[]{#_Toc189799346}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane**

------------------------------------------------------------------------

[**[display qos policy control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_x1626988866}[命令用来显示控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1025406045}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_x670807518}

[**[display qos policy control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_x1601206520}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x1753560529}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos policy control-plane]{lang="EN-US"}**[ **slot** *slot-number* ]{lang="EN-US"}[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_1884905934}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_313900369}[模式：]{style="font-family:宋体"}

[**[display qos policy control-plane]{lang="EN-US"}**[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_500269371}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600878840}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1070492410}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_734363865}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_318098941}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x908444275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1216822317}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x813169531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1651834282}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1600813304}[：显示指定单板的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x2061687263}[：显示指定成员设备的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1991661886}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1644765722}[：显示指定成员设备上指定单板的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_120251352}[：]{style="font-family:宋体"}[显示指定单板的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_1891805116}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1842585074}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1601009912}[显示应用到控制平面的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane]{lang="EN-US"}]{#struct_0_14687_18620_x1600944376}

[ ]{lang="EN-US"}

[Control plane]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Policy: 1]{lang="EN-US"}

[   Classifier: 1]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Yellow packets: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Red packets   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Classifier: 2]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable:]{lang="EN-US"}

[        0 (Packets)]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display qos policy control-plane]{lang="EN-US"}]{#struct_0_14687_18620_x1807208932}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1628591193}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_227215005}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600616696}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_x216920236}

[[对进入控制平面（]{style="font-family:宋体"}[Inbound]{lang="EN-US"}]{#struct_0_14687_18620_x1600551160}[）的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略]{style="font-family:宋体"}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x1991277289}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_93842713}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x1773478598}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_1087612846}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_x1601140987}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x760235558}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_292906917}[[表]{style="font-family:宋体"}[1-6]{lang="EN-US"}](#_0_14687_18620_x1163520085)[。]{style="font-family:宋体"}

::: {#-770832082 .myid}
[]{#_Toc298419678}[]{#_Toc263759915}[]{#_Toc226262582}[]{#_Toc198110120}[]{#_Toc312071813}[]{#_Toc291749961}[]{#_Toc263759914}[]{#_Toc226262581}[]{#_Toc198110119}[]{#_Toc191699846}[]{#_Toc189799347}[]{#_Toc404792313}[]{#struct_0_14687_18620_x1906360103}[]{#_Toc353798057}[]{#_Toc351557500}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane management**

------------------------------------------------------------------------

[**[display qos policy control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_x1601075451}[命令用于显示管理口控制平面应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1006307846}

[**[display qos policy control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_x1674608166}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1601272059}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1232449250}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1397734193}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1601206523}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1350276002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x685224140}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1600878843}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_495591531}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x915748931}[显示对进入管理口控制平面的报文应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane management]{lang="EN-US"}]{#struct_0_14687_18620_x1601009915}

[ ]{lang="EN-US"}

[Control plane management]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Policy: a]{lang="EN-US"}

[   Classifier: default-class]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match any]{lang="EN-US"}

[     Behavior: be]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[   Classifier: a]{lang="EN-US"}

[     Matched : 3 (Packets) 180 (Bytes)]{lang="EN-US"}

[     Operator: OR]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match control-plane protocol arp]{lang="EN-US"}

[      If-match control-plane protocol rip]{lang="EN-US"}

[      If-match control-plane protocol-group critical]{lang="EN-US"}

[      If-match acl 3001]{lang="EN-US"}

[      If-match control-plane protocol bgp]{lang="EN-US"}

[      If-match control-plane protocol bgp4+]{lang="EN-US"}

[      If-match control-plane protocol ftp]{lang="EN-US"}

[      If-match control-plane protocol http https icmp icmp6 ripng snmp]{lang="EN-US"}

[     Behavior: a]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 128 (kbps), CBS 8000 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 3 (Packets) 180 (Bytes)]{lang="EN-US"}

[        Yellow packets: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Red packets   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display qos policy control-plane management]{lang="EN-US"}]{#struct_0_14687_18620_x2027345924}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1658130905}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600944379}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600616699}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x976435123}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1600551163}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_1900405480}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1601140986}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_1968647797}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1601075450}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x1722575509}[[表]{style="font-family:宋体"}[1-6]{lang="EN-US"}](#_0_14687_18620_x1163520085)[。]{style="font-family:宋体"}

::: {#434974333 .myid}
[]{#_Toc404792314}[]{#struct_0_14687_18620_x1601272058}[]{#_Toc353798058}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane management pre-defined**

------------------------------------------------------------------------

[**[display qos policy control-plane management pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x1496434105}[命令用来显示系统预定义的管理口控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1547575820}

[**[display qos policy control-plane management pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_x1601206522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1378607353}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x618497081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600878842}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2061675472}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x628715881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1600813306}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x898887849}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_894606144}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1601009914}[显示系统预定义的管理口控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane management pre-defined]{lang="EN-US"}]{#struct_0_14687_18620_x1600944378}

[Pre-defined control plane policy management]{lang="EN-US"}

[  Protocol          Priority   Bandwidth (kbps)   Group]{lang="EN-US"}

[  Default           N/A        100000             N/A]{lang="EN-US"}

[  ARP               N/A        128                normal]{lang="EN-US"}

[  BGP               N/A        256                critical]{lang="EN-US"}

[  BGPv6             N/A        256                critical]{lang="EN-US"}

[  HTTP              N/A        512                management]{lang="EN-US"}

[  HTTPS             N/A        512                management]{lang="EN-US"}

[  ICMP              N/A        128                monitor]{lang="EN-US"}

[  ICMPv6            N/A        128                monitor]{lang="EN-US"}

[  OSPF Multicast    N/A        256                critical]{lang="EN-US"}

[  OSPF Unicast      N/A        256                critical]{lang="EN-US"}

[  OSPFv3 Multicast  N/A        256                critical]{lang="EN-US"}

[  OSFPv3 Unicast    N/A        256                critical]{lang="EN-US"}

[  RIP               N/A        1024               critical]{lang="EN-US"}

[  RIPng             N/A        256                critical]{lang="EN-US"}

[  SNMP              N/A        512                management]{lang="EN-US"}

[  SSH               N/A        512                management]{lang="EN-US"}

[  TELNET            N/A        512                management]{lang="EN-US"}

[  FTP               N/A        512                management]{lang="EN-US"}

[  TFTP              N/A        512                management]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display qos policy control-plane management pre-defined]{lang="EN-US"}]{#struct_0_14687_18620_1324958950}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1654981177}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1600616698}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_589648818}

[[Pre-defined control plane policy management]{lang="EN-US"}]{#struct_0_14687_18620_x1600551162}

[[预定义管理口控制平面策略内容]{style="font-family:宋体"}]{#struct_0_14687_18620_x828477875}

[[Protocol]{lang="EN-US"}]{#struct_0_14687_18620_321173318}

[[系统预定义协议报文类型]{style="font-family:宋体"}]{#struct_0_14687_18620_321238854}

[[Priority]{lang="EN-US"}]{#struct_0_14687_18620_x1501650666}

[[优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_321042246}

[[Bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_x1310518285}

[[带宽]{style="font-family:宋体"}]{#struct_0_14687_18620_321107782}

[[Group]{lang="EN-US"}]{#struct_0_14687_18620_x1700957892}

[[协议组]{style="font-family:宋体"}]{#struct_0_14687_18620_321435462}

[ ]{lang="EN-US"}

::: {#-309650549 .myid}
[]{#_Toc404792315}[]{#struct_0_14687_18620_x445329748}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy control-plane pre-defined**

------------------------------------------------------------------------

[**[display qos policy control-plane pre-defined]{lang="EN-US"}**]{#struct_0_14687_18620_1813654116}[命令用来显示系统预定义的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2004166834}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_321500998}

[**[display qos policy control-plane]{lang="EN-US"}**[ **pre-defined**]{lang="EN-US"}]{#struct_0_14687_18620_x13488920}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x1973480620}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos policy control-plane]{lang="EN-US"}**[ **pre-defined** \[ **slot** *slot-number* ]{lang="EN-US"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x1532863938}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_183253221}[模式：]{style="font-family:宋体"}

[**[display qos policy control-plane]{lang="EN-US"}**[ **pre-defined** \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x1509425745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x318899189}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1751253862}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_321304390}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1808949550}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1207937606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x648970092}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x125824583}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_681914232}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_314768903}[：显示指定单板的系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x962833142}[：显示指定成员设备的系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x737287005}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-numbe*r]{lang="EN-US"}]{#struct_0_14687_18620_321369926}[：显示指定成员设备上指定单板的系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1991596350}[：]{style="font-family:宋体"}[显示指定单板的系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_x836881627}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上系统预定义的控制平面策略信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1105711832}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定槽位号，则显示所有在位单板的系统预定义的控制平面应用]{style="font-family:宋体"}]{#struct_0_14687_18620_x585847022}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定成员编号，则显示所有成员设备的系统预定义的控制平面应用]{style="font-family:宋体"}]{#struct_0_14687_18620_x1856658624}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}[（集中式]{lang="EN-US" style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定成员编号和槽位号，则显示所有成员设备上在位单板的系统预定义的控制平面应用]{style="font-family:宋体"}]{#struct_0_14687_18620_x274345395}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1848401912}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1206405140}[显示]{style="font-family:宋体"}[3]{lang="EN-US"}[号板系统预定义的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane pre-defined slot 3]{lang="EN-US"}]{#struct_0_14687_18620_321697606}

[Pre-defined control plane policy slot 3]{lang="EN-US"}

[  Protocol          Priority   Bandwidth (kbps)]{lang="EN-US"}

[  ARP               1          1000]{lang="EN-US"}

[  ARP Snooping      2          2000]{lang="EN-US"}

[  BGP               3          3000]{lang="EN-US"}

[  BGPv6             4          4000]{lang="EN-US"}

[  BPDU Tunnel       5          5000]{lang="EN-US"}

[  CDP               6          6000]{lang="EN-US"}

[  CFD               7          7000]{lang="EN-US"}

[  DHCP              0          8000]{lang="EN-US"}

[  DHCP Snooping     1          9000]{lang="EN-US"}

[  DHCPv6            2          10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1718360904}[显示]{style="font-family:宋体"}[3]{lang="EN-US"}[号成员设备系统预定义的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane pre-defined slot 3]{lang="EN-US"}]{#struct_0_14687_18620_321763142}

[Pre-defined control plane policy slot 3]{lang="EN-US"}

[  Protocol          Priority   Bandwidth (kbps)]{lang="EN-US"}

[  ARP               1          1000]{lang="EN-US"}

[  ARP Snooping      2          2000]{lang="EN-US"}

[  BGP               3          3000]{lang="EN-US"}

[  BGPv6             4          4000]{lang="EN-US"}

[  BPDU Tunnel       5          5000]{lang="EN-US"}

[  CDP               6          6000]{lang="EN-US"}

[  CFD               7          7000]{lang="EN-US"}

[  DHCP              0          8000]{lang="EN-US"}

[  DHCP Snooping     1          9000]{lang="EN-US"}

[  DHCPv6            2          10000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1287092148}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[号单板系统预定义的控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display qos policy control-plane pre-defined chassis 1 slot 3]{lang="EN-US"}]{#struct_0_14687_18620_x1326764680}

[Pre-defined control plane policy chassis 1 slot 3]{lang="EN-US"}

[  Protocol          Priority   Bandwidth (kbps)]{lang="EN-US"}

[  ARP               1          1000]{lang="EN-US"}

[  ARP Snooping      2          2000]{lang="EN-US"}

[  BGP               3          3000]{lang="EN-US"}

[  BGPv6             4          4000]{lang="EN-US"}

[  BPDU Tunnel       5          5000]{lang="EN-US"}

[  CDP               6          6000]{lang="EN-US"}

[  CFD               7          7000]{lang="EN-US"}

[  DHCP              0          8000]{lang="EN-US"}

[  DHCP Snooping     1          9000]{lang="EN-US"}

[  DHCPv6            2          10000]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display qos policy control-plane pre-defined]{lang="EN-US"}]{#struct_0_14687_18620_27829810}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1675491897}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_289201126}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_321173319}

[[Pre-defined control plane policy]{lang="EN-US"}]{#struct_0_14687_18620_x532242706}

[[预定义控制平面策略内容]{style="font-family:宋体"}]{#struct_0_14687_18620_x918369498}

[[Protocol]{lang="EN-US"}]{#struct_0_14687_18620_x695532926}

[[系统预定义协议报文类型]{style="font-family:宋体"}]{#struct_0_14687_18620_x824034095}

[[Priority]{lang="EN-US"}]{#struct_0_14687_18620_x2120012289}

[[优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_321238855}

[[Bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_x1501650665}

[[带宽]{style="font-family:宋体"}]{#struct_0_14687_18620_1038711779}

[ ]{lang="EN-US"}

::: {#946742357 .myid}
[]{#_Toc404792316}[]{#struct_0_14687_18620_337879078}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy global**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **qos policy global**]{lang="EN-US"}]{#struct_0_14687_18620_2129472672}[命令用来显示基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1917522200}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_321042247}

[**[display qos policy global]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1310518286}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x365029339}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos policy global]{lang="EN-US"}**[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x12783580}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1813535733}[模式：]{style="font-family:宋体"}

[**[display qos policy global]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x71283721}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x805091396}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_2065655056}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_676368025}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_321107783}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1700957893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_995603268}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1272404331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_788137712}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_538622810}[：显示对全局接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_139575768}[：显示对全局发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x430912289}[：显示指定单板的基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_321435463}[：显示指定成员设备的基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1496867428}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x445329747}[：显示指定成员设备上指定单板的基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1232015927}[：]{style="font-family:宋体"}[显示指定单板的基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_x837405915}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1812933220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定显示方向，则同时显示出入两个方向基于全局应用]{style="font-family:宋体"}]{#struct_0_14687_18620_x1985567189}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定槽位号，则显示主用主控板上基于全局应用]{style="font-family:宋体"}]{#struct_0_14687_18620_x895042623}[QoS]{lang="EN-US"}[策略的信息，不显示各单板的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定成员编号，则显示主设备上基于全局应用]{style="font-family:宋体"}]{#struct_0_14687_18620_810236941}[QoS]{lang="EN-US"}[策略的信息，不显示各成员设备的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定成员编号和槽位号，则显示全局主用主控板上基于全局应用]{style="font-family:宋体"}]{#struct_0_14687_18620_1825527622}[QoS]{lang="EN-US"}[策略的信息，不显示各单板的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x598819168}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_321500999}[显示基于全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy global inbound]{lang="EN-US"}]{#struct_0_14687_18620_321304391}

[  Direction: Inbound]{lang="EN-US"}

[  Type     : Extension]{lang="EN-US"}

[  Policy: 1]{lang="EN-US"}

[   Classifier: 1]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Yellow packets: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Red packets   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Classifier: 2]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable:]{lang="EN-US"}

[        0 (Packets)]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display qos policy global]{lang="EN-US"}]{#struct_0_14687_18620_x1808949551}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1677523801}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1520945749}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1773617862}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_1883590541}

[[对接收到（]{style="font-family:宋体"}[Inbound]{lang="EN-US"}]{#struct_0_14687_18620_321369927}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[发送（]{style="font-family:宋体"}[Outbound]{lang="EN-US"}[）的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_14687_18620_848899203}

[[策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：]{style="font-family:宋体"}]{#struct_0_14687_18620_848899200}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enhancement]{lang="EN-US"}]{#struct_0_14687_18620_1205217768}[：增强型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Extension]{lang="EN-US"}]{#struct_0_14687_18620_1943644396}[：扩展型]{lang="EN-US" style="font-family:宋体"}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x1105711833}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_980236919}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_1336761233}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1415274462}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_321697607}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1718360903}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x1680979646}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#-2095222111 .myid}
[]{#_Toc404792317}[]{#struct_0_14687_18620_1107066434}[]{#_Toc298419679}[]{#_Toc263759916}[]{#_Toc226262583}[]{#_Toc198110121}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy interface**

------------------------------------------------------------------------

[**[display qos policy interface]{lang="EN-US"}**]{#struct_0_14687_18620_1226181921}[命令用来显示接口上]{style="font-family:
宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x941316006}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_259773012}

[**[display qos policy interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_768562507}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_2065189902}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos policy interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_259707476}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1042538863}[模式：]{style="font-family:宋体"}

[**[display qos policy interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x538633601}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x634149941}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_321763143}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1287092149}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1402118675}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x590952282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1274756443}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_251719756}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1453550807}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x562617234}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_x837012700}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}[输入本参数时，无法输入参数]{style="font-family:宋体"}**[inbound]{lang="EN-US"}**[或]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_259379796}[：显示指定单板上指定接口的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。只有当接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口、聚合接口等类型时才支持此参数。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1587429203}[：显示指定成员设备指定接口的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。只有当接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[虚接口、聚合口等类型时才支持此参数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x737352541}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的指定接口的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。只有当接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[虚接口、聚合口等类型时才支持此参数。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_209130138}[：显示指定成员设备上指定单板的指定接口的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。只有当接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[虚接口、聚合口等类型时才支持此参数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1991530814}[：]{style="font-family:宋体"}[显示指定单板的指定接口的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。只有当接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[虚接口、聚合口等类型时才支持此参数。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_242469605}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_321173316}[：显示对接口接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x532242697}[：显示对接口发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1038011167}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定显示方向，则同时显示出入两个方向接口上应用]{style="font-family:宋体"}]{#struct_0_14687_18620_1485283462}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口为]{lang="EN-US" style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}]{#struct_0_14687_18620_1054933787}[接口，将显示继承该]{lang="EN-US" style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口的所有]{lang="EN-US" style="font-family:宋体"}[Virtual-Access]{lang="EN-US"}[接口下的]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{lang="EN-US" style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[本身无]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[信息显示。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x447429087}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1022612791}[显示对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy interface gigabitethernet 1/0/1 inbound]{lang="EN-US"}]{#struct_0_14687_18620_321042244}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[  Policy: 1]{lang="EN-US"}

[   Classifier: 1]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Yellow packets: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Red packets   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Classifier: 2]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable:]{lang="EN-US"}

[        0 (Packets)]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_848899207}[显示所有接口上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的接口的配置信息和运行情况。]{style="font-family:宋体"}

[[\<Sysname\>dis qos policy interface]{lang="EN-US"}]{#struct_0_14687_18620_x1107415938}

[Interface: GigabitEthernet5/0/1]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[  Type     : Enhancement]{lang="EN-US"}

[  Policy: a]{lang="EN-US"}

[   Classifier: a]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match any]{lang="EN-US"}

[     Behavior: a]{lang="EN-US"}

[      Mirroring:]{lang="EN-US"}

[        Mirror to the interface: GigabitEthernet5/0/10]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets)]{lang="EN-US"}

[        Red packets   : 0 (Packets)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet5/0/17]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[  Policy: b]{lang="EN-US"}

[   Classifier: b]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match any]{lang="EN-US"}

[     Behavior: b]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 200 (kbps), CBS 12500 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0(Packets)]{lang="EN-US"}

[        Red packets   : 0 (Packets)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet5/0/17]{lang="EN-US"}

[  Direction: Inbound]{lang="EN-US"}

[  Type     : Enhancement]{lang="EN-US"}

[  Policy: a]{lang="EN-US"}

[   Classifier: a]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match any]{lang="EN-US"}

[     Behavior: a]{lang="EN-US"}

[      Mirroring:]{lang="EN-US"}

[        Mirror to the interface: GigabitEthernet5/0/10]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets)]{lang="EN-US"}

[        Red packets   : 0 (Packets)]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display qos policy interface]{lang="EN-US"}]{#struct_0_14687_18620_x1310518283}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1670995673}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x768313866}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_490831565}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_321107780}

[[Policy]{lang="EN-US"}]{#struct_0_14687_18620_x1700957890}[应用在接口的方向]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_14687_18620_x1107415937}

[[策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：]{style="font-family:宋体"}]{#struct_0_14687_18620_x807638962}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enhancement]{lang="EN-US"}]{#struct_0_14687_18620_1086166654}[：增强型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Extension]{lang="EN-US"}]{#struct_0_14687_18620_x1107415940}[：扩展型]{lang="EN-US" style="font-family:宋体"}

[[Matched]{lang="EN-US"}]{#struct_0_14687_18620_592318741}

[[符合]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_14687_18620_x1434079709}[分类]{style="font-family:
  宋体"}[规则的数据包数目]{style="font-size:10.0pt;font-family:宋体"}

[[5-]{lang="EN-US" style="font-size:10.0pt"}[minute]{lang="EN-US"}]{#struct_0_14687_18620_2065486928}[ statistics]{lang="EN-US" style="font-size:10.0pt"}

[[最近]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_14687_18620_321435460}[5]{lang="EN-US" style="font-size:10.0pt"}[分钟的流速统计信息]{style="font-size:10.0pt;font-family:
  宋体"}

[[Forwarded]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_14687_18620_x445329746}

[[符合分类规则的成功转发报文在统计周期内的平均速率]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_14687_18620_1812998756}

[[Dropped]{lang="EN-US" style="font-size:10.0pt"}]{#struct_0_14687_18620_x437147429}

[[符合分类规则的丢弃报文在统计周期内的平均速率]{style="font-size:10.0pt;font-family:宋体"}]{#struct_0_14687_18620_1424720957}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_227095428}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_321500996}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x13488934}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_365171536}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_2127812016}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_1706626958}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_321304388}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#-1792546697 .myid}
[]{#_Toc404792318}[]{#struct_0_14687_18620_x1107415939}[]{#_Toc375927545}[]{#_Toc375553169}[]{#_Toc373826864}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy l2vpn-pw**

------------------------------------------------------------------------

[**[display qos policy l2vpn-pw]{lang="EN-US"}**]{#struct_0_14687_18620_711390812}[命令用来显示]{style="font-family:
宋体"}[L2VPN PW]{lang="EN-US"}[上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x385052318}

[**[display qos policy l2vpn-pw ]{lang="EN-US"}**[\[ **peer** *ip-address* **pw-id** ]{lang="EN-US"}]{#struct_0_14687_18620_x141534513}*[pw-id ]{lang="EN-US" style="font-size:9.0pt;
color:black"}*[\] \[ **outbound** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1672069436}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_368710114}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x739974297}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_62918802}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x223197165}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x710308812}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1052477646}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1107415934}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_758444979}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。若未指定本参数，则]{style="font-family:宋体;
color:black"}[显示]{style="font-family:宋体"}[所有]{style="font-family:宋体;color:black"}[PW]{lang="EN-US"}[上的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1441715005}[：显示对]{style="font-family:宋体"}[PW]{lang="EN-US"}[发送的报文应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1447113022}

[[如果未指定显示方向，则显示出方向]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_1755959066}[上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1510517716}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_919969306}[显示远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[、]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[PW]{lang="EN-US"}[发送报文方向上应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy l2vpn-pw peer 1.1.1.1 pw-id 1 outbound]{lang="EN-US"}]{#struct_0_14687_18620_x1107415933}

[ ]{lang="EN-US"}

[L2VPN-PW: peer 1.1.1.1, pw-id 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Direction: Outbound]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Policy: 1]{lang="EN-US"}

[   Classifier: 1]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Yellow packets: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[        Red packets   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Classifier: 2]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable:]{lang="EN-US"}

[        0 (Packets)]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3]{lang="EN-US"}

[     Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[     5-minute statistics:]{lang="EN-US"}

[      Forwarded: 0/0 (pps/bps)]{lang="EN-US"}

[      Dropped  : 0/0 (pps/bps)]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display qos policy l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_1517959866}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1508958643}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1009988672}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1107415936}

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_1921244393}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_248340909}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_x1107415935}

[[Policy]{lang="EN-US"}]{#struct_0_14687_18620_x1970438376}[应用在]{style="font-family:宋体"}[PW]{lang="EN-US"}[的方向]{style="font-family:宋体"}

[[Matched]{lang="EN-US"}]{#struct_0_14687_18620_x1107415930}

[[符合]{style="font-family:宋体"}]{#struct_0_14687_18620_x1210923489}[分类]{style="font-family:宋体"}[规则的数据包数目]{style="font-family:宋体"}

[[5-]{lang="EN-US"}[minute]{lang="EN-US"}]{#struct_0_14687_18620_x234839324}[ statistics]{lang="EN-US"}

[[最近]{style="font-family:宋体"}]{#struct_0_14687_18620_x1107415929}[5]{lang="EN-US"}[分钟的流速统计信息]{style="font-family:宋体"}

[[Forwarded]{lang="EN-US"}]{#struct_0_14687_18620_711325276}

[[符合分类规则的成功转发报文在统计周期内的平均速率]{style="font-family:宋体"}]{#struct_0_14687_18620_x1532558803}

[[Dropped]{lang="EN-US"}]{#struct_0_14687_18620_466562174}

[[符合分类规则的丢弃报文在统计周期内的平均速率]{style="font-family:宋体"}]{#struct_0_14687_18620_1037349933}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_466562175}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_1037349932}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x1127201410}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_466562172}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_1037349927}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_466562173}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_1037349926}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#-691550254 .myid}
[]{#_Toc404792319}[]{#struct_0_14687_18620_x1095009247}[]{#_Toc396402594}[]{#_Toc396374904}[]{#_Toc206560160}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos policy user-profile**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **qos policy** **user-profile**]{lang="EN-US"}]{#struct_0_14687_18620_x1809956703}[命令用来显示用户上线后]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_471074694}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_2080823744}

[**[display qos policy user-profile]{lang="EN-US"}**[ \[ **name** *profile-name* \] \[ **user-id** *user-id* \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_467465554}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x1568375138}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **qos policy user-profile** \[ **name** *profile-name* \] \[ **user-id** *user-id* \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_943377779}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x307178246}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **qos policy user-profile** \[ **name** *profile-name* \] \[ **user-id** *user-id* \] \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_661624243}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_741015080}

[[ ]{lang="EN-US"}]{#struct_0_14687_18620_2037158635}[无]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1262398734}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_313634586}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1230912213}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1790916851}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1993195330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_553301733}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1290295736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1981201609}

[**[name ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1047955080}[：指定]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含英文字母]{style="font-family:宋体"}[\[a-z,A-Z\]]{lang="EN-US"}[、数字、下划线，且必须以英文字母开始，区分大小写。]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的名称必须全局唯一。如果未指定本参数，将显示所有]{style="font-family:宋体"}[User]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[Profile]{lang="EN-US"}[下应用]{style="font-family:宋体"}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[user-id]{lang="EN-US"}***[ user-id]{lang="EN-US"}*]{#struct_0_14687_18620_1564077405}[：表示在线用户的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，为系统所分配，为十六进制数。若未指定本参数，则显示所有用户在]{style="font-family:宋体"}[User]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[Profile]{lang="EN-US"}[下应用]{style="font-family:宋体"}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1341686792}[：显示指定单板上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的在线用户的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1684768761}[：显示指定成员设备上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的在线用户上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_198824498}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1294027288}[：显示指定成员设备指定单板上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有成员设备所有单板上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_518128861}[：显示指定单板上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_1823982039}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上指定用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息和运行情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1898978286}[：显示在线用户在入方向上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_171160246}[：显示在线用户在出方向上]{style="font-family:宋体"}[应用]{lang="EN-US" style="font-family:
宋体"}[QoS]{lang="EN-US"}[策略的信息]{lang="EN-US" style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1026090074}

[[如果未指定显示方向，则同时显示出入两个方向上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_x691659184}[策略的配置信息和运行情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1748366085}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1930298589}[显示指定全局用户（]{style="font-family:宋体"}[从聚合口等全局口上线的用户]{style="font-family:
宋体"}[）在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile name abc user-id 30000000 inbound]{lang="EN-US"}]{#struct_0_14687_18620_874424757}

[User-Profile: abc]{lang="EN-US"}

[  User ID: 0x30000000(global)]{lang="EN-US"}

[    Direction: Inbound]{lang="EN-US"}

[    Policy: p1]{lang="EN-US"}

[     Classifier: default-class]{lang="EN-US"}

[       Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[       Operator: AND]{lang="EN-US"}

[       Rule(s) :]{lang="EN-US"}

[        If-match any]{lang="EN-US"}

[       Behavior: be]{lang="EN-US"}

[        -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1119491738}[显示指定的非全局用户在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile name abc user-id 30000001 inbound]{lang="EN-US"}]{#struct_0_14687_18620_1556123655}

[User-Profile: abc]{lang="EN-US"}

[  slot 2:]{lang="EN-US"}

[    User ID: 0x30000001(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2056898339}[显示指定]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下所有用户的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile name abc inbound]{lang="EN-US"}]{#struct_0_14687_18620_x288374657}

[User-Profile: abc]{lang="EN-US"}

[  User ID: 0x30000000(global)]{lang="EN-US"}

[    Direction: Inbound]{lang="EN-US"}

[    Policy: p1]{lang="EN-US"}

[     Classifier: default-class]{lang="EN-US"}

[       Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[       Operator: AND]{lang="EN-US"}

[       Rule(s) :]{lang="EN-US"}

[        If-match any]{lang="EN-US"}

[       Behavior: be]{lang="EN-US"}

[        -none-]{lang="EN-US"}

[  ]{lang="EN-US"}

[  slot 2:]{lang="EN-US"}

[    User ID: 0x30000001(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[ ]{lang="EN-US"}

[  slot 3:]{lang="EN-US"}

[    User ID: 0x30000002(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_145168122}[显示指定单板上所有用户在]{style="font-family:宋体"}[User Profile abc]{lang="EN-US"}[下应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile name abc slot 2]{lang="EN-US"}]{#struct_0_14687_18620_1633939644}

[User-Profile: abc]{lang="EN-US"}

[User ID: 0x30000000(global)]{lang="EN-US"}

[    Direction: Inbound]{lang="EN-US"}

[    Policy: p1]{lang="EN-US"}

[     Classifier: default-class]{lang="EN-US"}

[       Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[       Operator: AND]{lang="EN-US"}

[       Rule(s) :]{lang="EN-US"}

[        If-match any]{lang="EN-US"}

[       Behavior: be]{lang="EN-US"}

[        -none-]{lang="EN-US"}

[ ]{lang="EN-US"}

[  User ID: 0x30000001(local)]{lang="EN-US"}

[    Direction: Inbound]{lang="EN-US"}

[    Policy: p1]{lang="EN-US"}

[     Classifier: default-class]{lang="EN-US"}

[       Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[       Operator: AND]{lang="EN-US"}

[       Rule(s) :]{lang="EN-US"}

[        If-match any]{lang="EN-US"}

[       Behavior: be]{lang="EN-US"}

[        -none-]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_14687_18620_x887995340}[显示所有单板上指定用户在]{style="font-family:宋体"}[User Profile abc]{lang="EN-US"}[下应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile name abc user-id 30000001]{lang="EN-US"}]{#struct_0_14687_18620_x1094943711}

[User-Profile: abc]{lang="EN-US"}

[  slot 2:]{lang="EN-US"}

[    User ID: 0x30000001(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[ ]{lang="EN-US"}

[  slot 3:]{lang="EN-US"}

[    User ID: 0x30000001(local)]{lang="EN-US"}

[      Direction: Inbound ]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x432453143}[显示所有]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的在线用户的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的配置信息和运行情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos policy user-profile]{lang="EN-US"}]{#struct_0_14687_18620_471140230}

[User-Profile: abc]{lang="EN-US"}

[  slot 3:]{lang="EN-US"}

[    User ID: 0x30000000(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[ ]{lang="EN-US"}

[User-Profile: a12]{lang="EN-US"}

[  slot 4:]{lang="EN-US"}

[    User ID: 0x30000001(local)]{lang="EN-US"}

[      Direction: Inbound]{lang="EN-US"}

[      Policy: p1]{lang="EN-US"}

[       Classifier: default-class]{lang="EN-US"}

[         Matched : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[         Operator: AND]{lang="EN-US"}

[         Rule(s) :]{lang="EN-US"}

[          If-match any]{lang="EN-US"}

[         Behavior: be]{lang="EN-US"}

[          -none-]{lang="EN-US"}

[       Classifier: a]{lang="EN-US"}

[        Operator: AND]{lang="EN-US"}

[        Rule(s) :]{lang="EN-US"}

[         If-match any]{lang="EN-US"}

[        Behavior: a]{lang="EN-US"}

[         Mirroring:]{lang="EN-US"}

[          Mirror to the interface: GigabitEthernet1/0/1]{lang="EN-US"}

[         Committed Access Rate:]{lang="EN-US"}

[           CIR 100 (kbps), CBS 6250 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[           Green action  : pass]{lang="EN-US"}

[           Yellow action : pass]{lang="EN-US"}

[           Red action    : discard]{lang="EN-US"}

[           Green packets : 0 (Packets)]{lang="EN-US"}

[           Red packets   : 0 (Packets)]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display qos policy user-profile ]{lang="EN-US"}]{#struct_0_14687_18620_2077230959}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1242615647}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_2037224171}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1047889544}

[[User-Profile ]{lang="EN-US"}]{#struct_0_14687_18620_1872890911}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_518194397}[名称]{style="font-family:宋体"}

[[User ID]{lang="EN-US"}]{#struct_0_14687_18620_269283527}

[[上线用户的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14687_18620_x691593648}

[[global]{lang="EN-US"}]{#struct_0_14687_18620_874490293}

[[该用户从聚合口等全局口上线]{style="font-family:宋体"}]{#struct_0_14687_18620_x1569163950}

[[local]{lang="EN-US"}]{#struct_0_14687_18620_x1854393062}

[[该用户从物理口上线]{style="font-family:宋体"}]{#struct_0_14687_18620_x1846588925}

[[Mirror to the interface]{lang="EN-US"}]{#struct_0_14687_18620_x288309121}

[[镜像到接口]{style="font-family:宋体"}]{#struct_0_14687_18620_1634005180}

[[CIR]{lang="EN-US"}]{#struct_0_14687_18620_x2132292085}

[[承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_x1094878175}

[[CBS]{lang="EN-US"}]{#struct_0_14687_18620_821371978}

[[承诺突发尺寸，也就是容纳突发流量的令牌桶深度，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_471205766}

[[EBS]{lang="EN-US"}]{#struct_0_14687_18620_2037289707}

[[超出突发尺寸，在双令牌桶算法中超出突发流量超过承诺突发流量的部分，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_482949269}

[[PIR]{lang="EN-US"}]{#struct_0_14687_18620_x1047824008}

[[峰值信息速率]{style="font-family:宋体"}]{#struct_0_14687_18620_198325144}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_518259933}

[[Policy]{lang="EN-US"}]{#struct_0_14687_18620_x691528112}[应用在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的方向]{style="font-family:宋体"}

[[Matched]{lang="EN-US"}]{#struct_0_14687_18620_977830188}

[[符合分类规则的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_874555829}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x1854327526}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x238380883}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x288243585}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_1634070716}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_x979626725}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1094812639}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x62593337}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#-1825249506 .myid}
[]{#_Toc404792320}[]{#struct_0_14687_18620_529702618}[]{#_Toc298419680}[]{#_Toc263759917}[]{#_Toc226262584}[]{#_Toc198110122}[]{#_Toc380516262}[]{#_Toc380516446}

**QoS策略 \-- 定义策略和应用策略的命令 \-- display qos vlan-policy**

------------------------------------------------------------------------

[**[display qos vlan-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x712298265}[命令用来显示基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1137997516}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_x869550556}

[**[display qos vlan-policy ]{lang="EN-US"}**[{ **name** *policy-name* \| **vlan** \[ *vlan-id* \] } \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1816780502}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_372623070}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos vlan-policy ]{lang="EN-US"}**[{ **name** *policy-name* \| **vlan** \[ *vlan-id* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_321369924}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1105711834}[模式：]{style="font-family:宋体"}

[**[display qos vlan-policy ]{lang="EN-US"}**[{ **name** *policy-name* \| **vlan** \[ *vlan-id* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_220722032}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1820649691}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1255459770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1903415145}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x710627404}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_2080655225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1919372744}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_321697604}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1718360906}

[**[name]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14687_18620_x2084264173}[：显示指定策略名称的基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[表示策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_14687_18620_x650751817}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x190808561}[：显示对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接收到的报文应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_25788879}[：显示对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[发送的报文应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1227516904}[：显示指定单板上基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1357035001}[：显示指定成员设备上基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1853163324}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_321763140}[：显示指定成员设备上指定单板的基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1791942778}[：]{style="font-family:宋体"}[显示指定单板上基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_x836947167}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上基于]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1287092150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定显示方向，则同时显示出入两个方向基于]{style="font-family:宋体"}]{#struct_0_14687_18620_x1682929504}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定槽位号，则显示主用主控板上基于]{style="font-family:宋体"}]{#struct_0_14687_18620_1194264472}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定成员编号，则显示主设备上基于]{style="font-family:宋体"}]{#struct_0_14687_18620_x1865340068}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定成员编号和槽位号，则显示全局主用主控板上基于]{style="font-family:宋体"}]{#struct_0_14687_18620_x177159397}[VLAN]{lang="EN-US"}[应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x237246334}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1971914568}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos vlan-policy vlan 2]{lang="EN-US"}]{#struct_0_14687_18620_321238853}

[Vlan 2]{lang="EN-US"}

[  Direction: Outbound]{lang="EN-US"}

[  Type     : Extension]{lang="EN-US"}

[  Policy: 1]{lang="EN-US"}

[   Classifier: 1]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match acl 2000]{lang="EN-US"}

[     Behavior: 1]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark dscp 3]{lang="EN-US"}

[      Committed Access Rate:]{lang="EN-US"}

[        CIR 112 (kbps), CBS 7000 (Bytes), EBS 512 (Bytes)]{lang="EN-US"}

[        Green action  : pass]{lang="EN-US"}

[        Yellow action : pass]{lang="EN-US"}

[        Red action    : discard]{lang="EN-US"}

[        Green packets : 0(Packets) 0(Bytes)]{lang="EN-US"}

[        Yellow packets: 0(Packets) 0(Bytes)]{lang="EN-US"}

[        Red packets   : 0(Packets) 0(Bytes)]{lang="EN-US"}

[   Classifier: 2]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      If-match not protocol ipv6]{lang="EN-US"}

[     Behavior: 2]{lang="EN-US"}

[      Accounting enable:]{lang="EN-US"}

[        0 (Packets)]{lang="EN-US"}

[      Filter enable: Permit]{lang="EN-US"}

[      Marking:]{lang="EN-US"}

[        Remark mpls-exp 4]{lang="EN-US"}

[   Classifier: 3]{lang="EN-US"}

[     Operator: AND]{lang="EN-US"}

[     Rule(s) :]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[     Behavior: 3]{lang="EN-US"}

[      -none-]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display qos vlan-policy]{lang="EN-US"}]{#struct_0_14687_18620_x1501650663}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1672170745}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_232142725}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1544663877}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_x1020145933}

[[对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_321042245}[接收到（]{style="font-family:宋体"}[Inbound]{lang="EN-US"}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[发送（]{style="font-family:宋体"}[Outbound]{lang="EN-US"}[）的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_14687_18620_466562177}

[[策略的应用类型，与应用策略的命令对应。应用时没有指定类型时，显示信息中也没有此字段。取值有：]{style="font-family:宋体"}]{#struct_0_14687_18620_1037349930}

[[Extension]{lang="EN-US"}]{#struct_0_14687_18620_466562182}[：扩展型]{style="font-family:宋体"}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x1310518284}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_797770075}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x1697965383}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x948622984}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_x1008719774}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_321107781}

[ ]{lang="EN-US"}

[[其它显示信息解释请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x1700957891}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-524958785#_Ref298418803)[和]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?-308098617#_Ref298418812)[。]{style="font-family:宋体"}

::: {#23177979 .myid}
[]{#_Toc404792321}[]{#struct_0_14687_18620_x2136564614}[]{#_Toc298419681}[]{#_Toc263759918}[]{#_Toc226262585}[]{#_Toc198110123}

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy (interface view, PVC view, control plane view, control plane management view,PW view)**

------------------------------------------------------------------------

[**[qos apply policy]{lang="EN-US"}**]{#struct_0_14687_18620_321435461}[命令用来在接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、]{style="font-family:宋体"}[PW]{lang="EN-US"}[、控制平面或管理口控制平面上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo qos apply policy]{lang="EN-US"}**]{#struct_0_14687_18620_x445329745}[命令用来取消接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、]{style="font-family:宋体"}[PW]{lang="EN-US"}[、控制平面或管理口控制平面上应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1812802148}

[**[qos apply policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*[ { **inbound** \| **outbound** } \[ **enhancement** \] \[ **extension** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1596843285}

[**[undo qos apply policy]{lang="EN-US"}**[ *policy-name* { **inbound** \| **outbound** } \[ **enhancement** \]]{lang="EN-US"}]{#struct_0_14687_18620_321500997}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x13488935}

[[没有在接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_14687_18620_365171535}[、控制平面、管理口控制平面或]{style="font-family:宋体"}[PW]{lang="EN-US"}[上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_2127812013}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_321304389}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[控制平面视图]{style="font-family:宋体"}[/]{lang="EN-US"}[管理口控制平面视图]{style="font-family:宋体"}[/]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI LDP PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_529702617}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x712298276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1137931981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1686528159}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_576962937}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_321369925}[：对接口或控制平面或管理口控制平面接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1105711835}[：对接口发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[enhancement]{lang="EN-US"}**]{#struct_0_14687_18620_466562183}[：对策略增强应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_14687_18620_x1489752962}[：对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1786805973}

[[策略在接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_14687_18620_x1718360905}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[上应用的规则如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在应用策略时，如果策略中为确保转发和加速转发的类指定的带宽之和超过接口、]{style="font-family:宋体"}]{#struct_0_14687_18620_x1797765318}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[允许的可用带宽，则在该接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[不可应用。如果对接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[修改了可用带宽，此时如果策略中为确保转发和加速转发的类指定的带宽之和超过接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[允许的可用带宽，则将策略删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[入方向的策略与类关联的行为不允许有]{lang="EN-US" style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1203517371}[、]{lang="EN-US" style="font-family:宋体"}**[queue ef]{lang="EN-US"}**[与]{lang="EN-US" style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[配置，也不允许有]{lang="EN-US" style="font-family:宋体"}[GTS]{lang="EN-US"}[配置。]{lang="EN-US" style="font-family:宋体"}

[[在控制平面和管理口控制平面上应用策略时，不支持配置了]{style="font-family:宋体"}[CBQ]{lang="EN-US"}]{#struct_0_14687_18620_x1797044422}[的策略。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_x465051130}[下应用策略时，只能应用在]{style="font-family:宋体"}[PW]{lang="EN-US"}[的出方向上。]{style="font-family:宋体"}

[[在同一个接口的同一个方向上，可以同时应用增强类型和普通类型策略，意味着一个报文会被两个策略处理。增强型策略对报文的处理性能较高，但支持的参数不够丰富。]{style="font-family:宋体"}]{#struct_0_14687_18620_38507772}

[[在同一个接口的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。]{style="font-family:宋体"}]{#struct_0_14687_18620_1796596952}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_689066049}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1261291013}[将策略]{style="font-family:宋体"}[USER1]{lang="EN-US"}[应用到接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_820408623}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/1\] qos apply policy USER1 outbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_607397544}[对进入]{style="font-family:宋体"}[3]{lang="EN-US"}[号槽控制平面的报文应用策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_321763141}

[\[Sysname\] control-plane slot 3]{lang="EN-US"}

[\[Sysname-cp-slot3\] qos apply policy aaa inbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1287092151}[对进入管理口控制平面的报文应用策略]{style="font-family:宋体"}[bbb]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_321173314}

[\[Sysname\] control-plane management]{lang="EN-US"}

[\[Sysname-cp-management\] qos apply policy bbb inbound]{lang="EN-US"}

[]{#struct_0_14687_18620_x1489752961}[]{#_Toc379981639}[\# ]{lang="EN-US"}[在]{style="font-family:宋体"}[PW]{lang="EN-US"}[的]{style="font-family:宋体"}[出方向上应]{style="font-family:宋体"}[用策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x868335657}

[\[Sysname\] xconnect-group a]{lang="EN-US"}

[\[Sysname-xcg-a\] connection a]{lang="EN-US"}

[\[Sysname-xcg-a-a\] peer 1.1.1.1 pw-id 1]{lang="EN-US"}

[\[Sysname-xcg-a-a-1.1.1.1-1\] qos apply policy 1 outbound]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_119171055}[将增强型策略]{style="font-family:宋体"}[aaa]{lang="EN-US"}[应用到接口]{style="font-family:宋体"}[GigabitEthernet5/0/1]{lang="EN-US"}[的出方向上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_778328145}

[\[Sysname\] interface GigabitEthernet5/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet5/0/1\]qos apply policy aaa outbound enhancement]{lang="EN-US"}
:::

::: {#-1233400799 .myid}
[]{#_Toc404792322}[]{#struct_0_14687_18620_1635308105}[]{#_Toc345405287}[]{#_Toc198110124}

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy (user-profile view)**

------------------------------------------------------------------------

[**[qos apply policy]{lang="EN-US"}**]{#struct_0_14687_18620_x615204331}[命令用来在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下]{style="font-family:宋体"}[应用策略。]{style="font-family:宋体"}

[**[undo qos apply policy]{lang="EN-US"}**]{#struct_0_14687_18620_2019075173}[命令用来取消]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下应用的]{style="font-family:宋体"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_186930812}

[**[qos apply policy]{lang="EN-US"}***[ policy-name]{lang="EN-US"}*[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_x1403277543}

[**[undo qos apply policy]{lang="EN-US"}**[ *policy-name* { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_1991317581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x285029021}

[[没有在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_1267536843}[下应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_777457351}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_1328058263}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1489752964}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1627850544}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_713119880}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x145317810}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1999423975}[：入方向，对设备接收的上线用户流量（即上线用户发送的流量）应用策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_1086978645}[：出方向，对设备发送的上线用户流量（即上线用户接收的流量）应用策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_x707276425}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_784456179}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_1065983569}[被]{style="font-family:宋体"}[删除将导致其下引用]{style="font-family:
宋体"}[的]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[策略]{lang="EN-US" style="font-family:宋体"}[被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2066960264}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_884471248}[对设备发送的上线用户]{style="font-family:宋体"}[user]{lang="EN-US"}[的流量应用策略]{style="font-family:宋体"}[test]{lang="EN-US"}[（该策略已经建立）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x471895010}

[\[Sysname\] user-profile user]{lang="EN-US"}

[\[Sysname-user-profile-user\] qos apply policy test outbound]{lang="EN-US"}
:::

::: {#1040247935 .myid}
[]{#_Toc404792323}[]{#_Toc298419682}[]{#_Toc263759920}[]{#_Toc226262587}[]{#_Toc198110125}[]{#struct_0_14687_18620_x532242695}[]{#_Toc380516266}[]{#_Toc380516450}[]{#_Toc380516267}[]{#_Toc380516451}

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos apply policy global**

------------------------------------------------------------------------

[**[qos apply policy global]{lang="EN-US"}**]{#struct_0_14687_18620_321238850}[命令用来全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo qos apply policy global]{lang="EN-US"}**]{#struct_0_14687_18620_x1501650662}[命令用来取消全局应用的]{style="font-family:
宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1333941216}

[**[qos apply policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}***[ global ]{lang="EN-US"}**[{ **inbound** \| **outbound** } \[ **enhancement** \] \[ **extension** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1165448093}

[**[undo qos apply policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*[ **global** { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_x223879739}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1203247952}

[[没有在全局应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_378765824}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2089366947}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1584037562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_321042242}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1310518289}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_750715908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x659872833}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1966208551}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x114481637}[：对设备所有端口接收到的流量应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1279369725}[：对设备所有端口发送的流量应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[enhancement]{lang="EN-US"}**]{#struct_0_14687_18620_1205348838}[：对策略增强应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_14687_18620_x1489752963}**[：]{style="font-family:宋体"}**[对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2084785027}

[[全局应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_321107778}[策略对全部流量生效。]{style="font-family:宋体"}

[[在同一个接口的同一个方向上，可以同时应用增强类型和普通类型策略，意味着一个报文会被两个策略处理。增强型策略对报文的处理性能较高，但支持的参数不够丰富。]{style="font-family:宋体"}]{#struct_0_14687_18620_1205676518}

[[在全局的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。]{style="font-family:宋体"}]{#struct_0_14687_18620_x2031135071}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1402368326}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1776170777}[将名为]{style="font-family:宋体"}[user1]{lang="EN-US"}[的扩展策略应用到全局的入方向上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1401250118}

[\[Sysname\] qos apply policy user1 global inbound extension]{lang="EN-US"}
:::

::: {#-1594134040 .myid}
[]{#_Toc404792324}[]{#struct_0_14687_18620_1915495467}[]{#_Toc298419683}[]{#_Toc263759921}[]{#_Toc226262588}[]{#_Toc198110126}

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos policy**

------------------------------------------------------------------------

[**[qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1550163344}[命令用来定义一个策略，并进入策略视图。]{style="font-family:宋体"}

[**[undo qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_x47172092}[命令用来删除一个策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_321435458}

[**[qos policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14687_18620_x2019307850}

[**[undo qos policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14687_18620_192257792}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_2097725088}

[[没有定义策略。]{style="font-family:宋体"}]{#struct_0_14687_18620_196979158}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_722520062}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1492916762}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2117288126}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_136486200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_321500994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x13488932}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_365171542}[：策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x975514196}

[[如果该策略已经被应用，则不允许删除该策略，需要先在应用的位置上取消对该策略的应用，然后再使用]{style="font-family:宋体"}**[undo qos policy]{lang="EN-US"}**]{#struct_0_14687_18620_1506137301}[命令删除该策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2078245275}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_518358544}[定义一个名为]{style="font-family:宋体"}[user1]{lang="EN-US"}[的策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_321304386}

[\[Sysname\] qos policy user1]{lang="EN-US"}

[\[Sysname-qospolicy-user1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_529702604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[classifier behavior]{lang="EN-US"}**]{#struct_0_14687_18620_1626353883}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos apply policy]{lang="EN-US"}**]{#struct_0_14687_18620_1916244427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos apply policy global]{lang="EN-US"}**]{#struct_0_14687_18620_635951057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos vlan-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1081866560}
:::

::: {#1929249263 .myid}
[]{#_Toc404792325}[]{#struct_0_14687_18620_x874861053}[]{#_Toc298419684}[]{#_Toc263759922}[]{#_Toc226262589}[]{#_Toc198110127}

**QoS策略 \-- 定义策略和应用策略的命令 \-- qos vlan-policy**

------------------------------------------------------------------------

[**[qos vlan-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1797157277}[命令用来在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos vlan-policy**]{lang="EN-US"}]{#struct_0_14687_18620_1819075049}[命令用来取消指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[上应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_321369922}

[**[qos vlan-policy]{lang="EN-US"}**[ *policy-name* **vlan** *vlan-id-list* { **inbound** \| **outbound** } \[ **extension** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1105711836}

[**[undo qos vlan-policy]{lang="EN-US"}**[ *policy-name* **vlan** *vlan-id-list* { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_1383521446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1901914982}

[[没有在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_x1016007369}[上应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_2045562639}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_181161535}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x316317009}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_321697602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1718360908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1404134069}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14687_18620_2024470073}[：策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[vlan-id-list]{lang="EN-US"}*]{#struct_0_14687_18620_x307288094}[：]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[列表，形式可以是]{style="font-family:宋体"}*[vlan-id ]{lang="EN-US"}***[to]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*[，其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。可以输入多个不连续的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，中间以空格隔开。设备最多允许用户同时指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1028560271}[：对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_178271032}[：对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_14687_18620_x1489752960}**[：]{style="font-family:宋体"}**[对策略扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_697748284}

[[在同一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_202178616}[的同一个方向上，不能同时应用扩展类型和普通类型策略，二者取其一。扩展型策略可以使用更多的硬件资源，但支持的参数类型较少。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_59275022}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_321763138}[在]{style="font-family:宋体"}[VLAN 200]{lang="EN-US"}[、]{style="font-family:宋体"}[300]{lang="EN-US"}[、]{style="font-family:宋体"}[400]{lang="EN-US"}[、]{style="font-family:宋体"}[500]{lang="EN-US"}[的入方向上扩展应用]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[策略]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1051560002}

[\[Sysname\] qos vlan-policy test vlan 200 300 400 500 inbound extension]{lang="EN-US"}
:::

::: {#2011008818 .myid}
[]{#_Toc404792326}[]{#struct_0_14687_18620_965026926}[]{#_Toc298419685}[]{#_Toc263759923}[]{#_Toc226262590}[]{#_Toc198110128}[]{#_Toc191699854}[]{#_Toc189799350}

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy control-plane**

------------------------------------------------------------------------

[**[reset qos policy control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_1315468057}[命令用来清除控制平面应用]{style="font-family:
宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2086316404}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_442323844}

[**[reset qos policy control-plane]{lang="EN-US"}**]{#struct_0_14687_18620_321173315}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x532242694}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset qos policy control-plane]{lang="EN-US"}**[ **slot** *slot-number* ]{lang="EN-US"}[\[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_1038076703}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_1891380197}[模式：]{style="font-family:宋体"}

[**[reset qos policy control-plane]{lang="EN-US"}**[ ]{lang="EN-US"}**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_321238851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1501650661}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x930656689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1553073753}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_577602959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_87624344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_321042243}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1310518290}[：清除指定单板的基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1171663929}[：清除指定成员设备的基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x603265885}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-numbe*r]{lang="EN-US"}]{#struct_0_14687_18620_301863362}[：清除指定成员设备上指定单板的基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-numbe*r]{lang="EN-US"}]{#struct_0_14687_18620_x678545474}[：清除指定单板的基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_729267849}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上基于控制平面应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_321107779}

[]{#_Toc298419686}[]{#_Toc263759924}[]{#_Toc226262591}[]{#_Toc198110129}[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1402368325}[清除控制平面的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略统计信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy control-plane]{lang="EN-US"}]{#struct_0_14687_18620_x1776367385}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_321435459}[清除应用到]{style="font-family:宋体"}[3]{lang="EN-US"}[号板控制平面的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy control-plane slot 3]{lang="EN-US"}]{#struct_0_14687_18620_x2019307849}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_321500995}[清除应用到]{style="font-family:宋体"}[3]{lang="EN-US"}[号成员设备控制平面的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy control-plane slot 3]{lang="EN-US"}]{#struct_0_14687_18620_321304387}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_529702603}[清除应用到]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[号板控制平面的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy control-plane chassis 1 slot 3]{lang="EN-US"}]{#struct_0_14687_18620_1626353888}
:::

::: {#-27773090 .myid}
[]{#_Toc404792327}[]{#struct_0_14687_18620_321369923}[]{#_Toc353798068}[]{#_Toc351557505}

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy control-plane management**

------------------------------------------------------------------------

[**[reset qos policy control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_x1105711837}[命令用来清除管理口控制平面]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_321697603}

[**[reset qos policy control-plane management]{lang="EN-US"}**]{#struct_0_14687_18620_x1718360907}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_321763139}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1051560001}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887257259}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x990718584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1887322795}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x561017256}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1887126187}[清除管理口控制平面]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy control-plane management]{lang="EN-US"}]{#struct_0_14687_18620_x1383243647}
:::

::: {#246394446 .myid}
[]{#_Toc404792328}[]{#struct_0_14687_18620_244261122}

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos policy global**

------------------------------------------------------------------------

[**[reset qos policy global]{lang="EN-US"}**]{#struct_0_14687_18620_1887191723}[命令用来清除全局应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x936317972}

[**[reset qos policy global ]{lang="EN-US"}**[\[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1515027352}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_196058554}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1247189548}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_299523374}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x160043499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1516731944}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887519403}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1411139218}[：清除全局接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x739101372}[：清除全局发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1633512817}

[[如果不指定方向，则同时清除出入两个方向全局应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_730856876}[策略的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2052501151}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_71345179}[清除全局入方向应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset qos policy global inbound]{lang="EN-US"}]{#struct_0_14687_18620_1815455428}
:::

::: {#-506329347 .myid}
[]{#_Toc404792329}[]{#struct_0_14687_18620_1887584939}[]{#_Toc298419687}[]{#_Toc263759925}[]{#_Toc226262592}[]{#_Toc198110130}

**QoS策略 \-- 定义策略和应用策略的命令 \-- reset qos vlan-policy**

------------------------------------------------------------------------

[**[reset qos vlan-policy]{lang="EN-US"}**]{#struct_0_14687_18620_1329613114}[命令用来清除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1743416978}

[**[reset qos vlan-policy ]{lang="EN-US"}**[\[ **vlan** *vlan-id* \] \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_14687_18620_371346661}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1593645475}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1015265664}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2082135040}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1265258093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_848799023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887388331}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_1031590592}[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1862331263}[：清除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接收到的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_1342494482}[：清除对]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[发送的报文应用]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x11833106}

[[如果不指定方向，则同时清除出入两个方向]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_x779723353}[应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2067826881}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1051490302}[清除]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[应用的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[策略的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset qos vlan-policy vlan 2]{lang="EN-US"}]{#struct_0_14687_18620_1887453867}
:::

::: {#1403398289 .myid}
[]{#_Toc404792331}[]{#struct_0_14687_18620_1864106171}[]{#_Toc335120907}

**QoS策略 \-- 接口流速统计配置命令 \-- qos flow-interval**

------------------------------------------------------------------------

[**[qos flow-interval]{lang="EN-US"}**]{#struct_0_14687_18620_1170607954}[命令用来配置接口流速统计时间。]{style="font-family:宋体"}

[**[undo qos flow-interval]{lang="EN-US"}**]{#struct_0_14687_18620_1270840263}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x622119931}

[**[qos flow-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_14687_18620_x1390732728}

[**[undo qos flow-interval]{lang="EN-US"}**]{#struct_0_14687_18620_151863008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1663698154}

[[接口流速统计时间为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_14687_18620_1887781547}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x560469072}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_498069773}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1193885431}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1056463684}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1760704828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_86417959}

[*[interval]{lang="EN-US"}*]{#struct_0_14687_18620_1887847083}[：流速统计时间，单位为分钟。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x613428157}

[[我们可以统计经过]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_14687_18620_x596478087}[策略流分类后每类报文的发送和丢弃速率。假设流速统计时间为]{style="font-family:宋体"}[t]{lang="EN-US"}[（]{style="font-family:宋体"}[t]{lang="EN-US"}[默认为]{style="font-family:
宋体"}[5]{lang="EN-US"}[分钟），则系统将统计最近]{style="font-family:宋体"}[t]{lang="EN-US"}[时间内每类报文发送和丢弃的平均速率，且每]{style="font-family:宋体"}[t/5]{lang="EN-US"}[分钟刷新一次统计速率。]{style="font-family:宋体"}

[[子接口的流速统计时间采用主接口的统计时间。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1023704748}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_746668817}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1087411269}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的流速统计时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1645210503}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos flow-interval 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1794817001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos policy interface]{lang="EN-US"}**]{#struct_0_14687_18620_1887257260}
:::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#-2075031760 .myid}
[]{#_Toc404792334}[]{#struct_0_14687_18620_450741712}[]{#_Toc263759930}[]{#_Toc226262597}[]{#_Toc198110197}[]{#_Toc115171258}

**优先级映射 \-- 优先级映射表配置命令 \-- display qos map-table**

------------------------------------------------------------------------

[**[display qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_2094361917}[命令用来显示指定优先级映射表配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1915541229}

[**[display qos map-table]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \] \[ **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** \]]{lang="EN-US"}]{#struct_0_14687_18620_10194917}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887322796}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x560820648}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1264067011}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_918324232}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1044796412}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_250684404}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_2093738088}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x293558483}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1887126188}[：接收报文方向。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1383047039}[：发送报文方向。]{style="font-family:宋体"}

[]{#struct_0_14687_18620_x2000244982}[[表2-1 ]{lang="EN-US"}[优先级映射表]{style="font-family:
黑体"}]{#_Ref298430323}

[]{#table_struct_0_1665814041}[[优先级映射]{style="font-family:黑体"}]{#struct_0_14687_18620_823568072}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_440938084}

[[dot11e-lp]{lang="EN-US"}]{#struct_0_14687_18620_x1431564604}

[[802.11e]{lang="EN-US"}]{#struct_0_14687_18620_1136680448}[优先级到本地优先级映射表]{style="font-family:宋体"}

[[dot1p-dot1p]{lang="EN-US"}]{#struct_0_14687_18620_1887191724}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_x936776724}[优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[dot1p-dp]{lang="EN-US"}]{#struct_0_14687_18620_x407373438}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_1559592041}[优先级到丢弃优先级映射表]{style="font-family:宋体"}

[[dot1p-dscp]{lang="EN-US"}]{#struct_0_14687_18620_699611955}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_1887519404}[优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[dot1p-exp]{lang="EN-US"}]{#struct_0_14687_18620_1410680466}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_x315620131}[优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[dot1p-lp]{lang="EN-US"}]{#struct_0_14687_18620_x617360676}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_783733332}[优先级到本地优先级映射表]{style="font-family:宋体"}

[[dot1p-rpr]{lang="EN-US"}]{#struct_0_14687_18620_1887584940}

[[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_1330202935}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[dscp-dot1p]{lang="EN-US"}]{#struct_0_14687_18620_2096103056}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_224521717}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[dscp-dp]{lang="EN-US"}]{#struct_0_14687_18620_1262546951}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_1887388332}[到丢弃优先级映射表]{style="font-family:宋体"}

[[dscp-dscp]{lang="EN-US"}]{#struct_0_14687_18620_1031525056}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_496749934}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[dscp-exp]{lang="EN-US"}]{#struct_0_14687_18620_150540052}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_1887453868}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[dscp-lp]{lang="EN-US"}]{#struct_0_14687_18620_x1404698031}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_2115767245}[到本地优先级映射表]{style="font-family:宋体"}

[[dscp-rpr]{lang="EN-US"}]{#struct_0_14687_18620_680553764}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_1887781548}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[exp-dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x561058896}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1308392320}[到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[exp-dp]{lang="EN-US"}]{#struct_0_14687_18620_1275411161}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1887847084}[到丢弃优先级映射表]{style="font-family:宋体"}

[[exp-dscp]{lang="EN-US"}]{#struct_0_14687_18620_x613493693}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_x2144570156}[到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[exp-exp]{lang="EN-US"}]{#struct_0_14687_18620_x529851834}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1887257257}[到]{style="font-family:宋体"}[EXP]{lang="EN-US"}[映射表]{style="font-family:宋体"}

[[exp-lp]{lang="EN-US"}]{#struct_0_14687_18620_x990849656}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_x640676559}[到本地优先级映射表]{style="font-family:宋体"}

[[exp-rpr]{lang="EN-US"}]{#struct_0_14687_18620_852710898}

[[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1887322793}[到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[ippre-rpr]{lang="EN-US"}]{#struct_0_14687_18620_x561148328}

[[IP]{lang="EN-US"}]{#struct_0_14687_18620_886864874}[优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}[优先级映射表]{style="font-family:宋体"}

[[lp-dot11e]{lang="EN-US"}]{#struct_0_14687_18620_1887126185}

[[本地优先级到]{style="font-family:宋体"}[802.11e]{lang="EN-US"}]{#struct_0_14687_18620_x1383374719}[优先级映射表]{style="font-family:宋体"}

[[lp-dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x590285674}

[[本地优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_1243317070}[优先级映射表]{style="font-family:宋体"}

[[lp-dp]{lang="EN-US"}]{#struct_0_14687_18620_1887191721}

[[本地优先级到丢弃优先级映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_x936449044}

[[lp-dscp]{lang="EN-US"}]{#struct_0_14687_18620_x814279980}

[[本地优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_1887519401}[映射表]{style="font-family:宋体"}

[[lp-exp]{lang="EN-US"}]{#struct_0_14687_18620_1411008146}

[[本地优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}]{#struct_0_14687_18620_x725767679}[映射表]{style="font-family:宋体"}

[[lp-lp]{lang="EN-US"}]{#struct_0_14687_18620_1887584937}

[[本地优先级到本地优先级映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_1330268474}

[[up-dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x280184266}

[[用户优先级到]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_1887388329}[优先级映射表]{style="font-family:宋体"}

[[up-dp]{lang="EN-US"}]{#struct_0_14687_18620_1031066303}

[[用户优先级到丢弃优先级映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_x1871827995}

[[up-dscp]{lang="EN-US"}]{#struct_0_14687_18620_1887453865}

[[用户优先级到]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1404894639}[映射表]{style="font-family:宋体"}

[[up-exp]{lang="EN-US"}]{#struct_0_14687_18620_1923199147}

[[用户优先级到]{style="font-family:宋体"}[EXP]{lang="EN-US"}]{#struct_0_14687_18620_1887781545}[映射表]{style="font-family:宋体"}

[[up-fc]{lang="EN-US"}]{#struct_0_14687_18620_x560338000}

[[用户优先级到转发类映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_1887847081}

[[up-lp]{lang="EN-US"}]{#struct_0_14687_18620_x613297085}

[[用户优先级到本地优先级映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_x201439603}

[[up-rpr]{lang="EN-US"}]{#struct_0_14687_18620_1887257258}

[[用户优先级到]{style="font-family:宋体"}[RPR]{lang="EN-US"}]{#struct_0_14687_18620_x990784120}[优先级映射表]{style="font-family:宋体"}

[[up-up]{lang="EN-US"}]{#struct_0_14687_18620_x309987146}

[[用户优先级到用户优先级映射表]{style="font-family:宋体"}]{#struct_0_14687_18620_1887322794}

**[ ]{lang="EN-US"}**

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_1887126186}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x1383178111}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1737445304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定表的类型，将显示所有映射表的配置情况。]{style="font-family:宋体"}]{#struct_0_14687_18620_x2063348337}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定方向，将显示所有方向的映射表的配置情况。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1033924467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何参数，即]{lang="EN-US" style="font-family:宋体"}**[display qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_x1874328869}[命令将显示所有映射表（以及带颜色映射表）的配置情况。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887191722}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x936383508}[显示]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到本地优先级映射表的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos map-table dot1p-lp]{lang="EN-US"}]{#struct_0_14687_18620_1887519402}

[MAP-TABLE NAME: dot1p-lp   TYPE: pre-define   DIRECTION: inbound]{lang="EN-US"}

[IMPORT  :  EXPORT]{lang="EN-US"}

[   0    :    2]{lang="EN-US"}

[   1    :    0]{lang="EN-US"}

[   2    :    1]{lang="EN-US"}

[   3    :    3]{lang="EN-US"}

[   4    :    4]{lang="EN-US"}

[   5    :    5]{lang="EN-US"}

[   6    :    6]{lang="EN-US"}

[   7    :    7]{lang="EN-US"}

[MAP-TABLE NAME: dot1p-lp   TYPE: pre-define   DIRECTION: outbound]{lang="EN-US"}

[IMPORT  :  EXPORT]{lang="EN-US"}

[   0    :    2]{lang="EN-US"}

[   1    :    0]{lang="EN-US"}

[   2    :    1]{lang="EN-US"}

[   3    :    3]{lang="EN-US"}

[   4    :    4]{lang="EN-US"}

[   5    :    5]{lang="EN-US"}

[   6    :    6]{lang="EN-US"}

[   7    :    7]{lang="EN-US"}

[MAP-TABLE NAME: dot1p-lp   TYPE: pre-define]{lang="EN-US"}

[IMPORT  :  EXPORT]{lang="EN-US"}

[   0    :    2]{lang="EN-US"}

[   1    :    0]{lang="EN-US"}

[   2    :    1]{lang="EN-US"}

[   3    :    3]{lang="EN-US"}

[   4    :    4]{lang="EN-US"}

[   5    :    5]{lang="EN-US"}

[   6    :    6]{lang="EN-US"}

[   7    :    7]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[display qos map-table]{lang="EN-US"}]{#struct_0_14687_18620_1411073682}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1687246809}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1280157516}

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1269312219}

[[MAP-TABLE NAME]{lang="EN-US"}]{#struct_0_14687_18620_1887584938}

[[映射表的名字]{style="font-family:宋体"}]{#struct_0_14687_18620_1329678650}

[[TYPE]{lang="EN-US"}]{#struct_0_14687_18620_977000561}

[[映射表的类型]{style="font-family:宋体"}]{#struct_0_14687_18620_2015080544}

[[DIRECTION]{lang="EN-US"}]{#struct_0_14687_18620_487061672}

[[映射表的方向]{style="font-family:宋体"}]{#struct_0_14687_18620_1887388330}

[[IMPORT]{lang="EN-US"}]{#struct_0_14687_18620_1031656128}

[[映射表的输入值]{style="font-family:宋体"}]{#struct_0_14687_18620_2042506145}

[[EXPORT]{lang="EN-US"}]{#struct_0_14687_18620_x1991869478}

[[映射表的输出值]{style="font-family:宋体"}]{#struct_0_14687_18620_x835828035}

[ ]{lang="EN-US"}

::::: {#889727510 .myid}
[]{#_Toc115171259}[]{#_Toc404792335}[]{#struct_0_14687_18620_x1651669008}[]{#_Toc263759931}[]{#_Toc226262598}[]{#_Toc198110198}[]{#_Toc167527001}[]{#_Toc281559420}

**优先级映射 \-- 优先级映射表配置命令 \-- display qos map-table color**

------------------------------------------------------------------------

[**[display qos map-table color]{lang="EN-US"}**]{#struct_0_14687_18620_1887453866}[命令用来显示指定带颜色优先级映射表配置情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1404829103}[]{#_Toc281559421}

[**[display qos map-table color]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **green** \| **yellow** \| **red** \] \[ **inbound** \| **outbound** \] ]{lang="EN-US"}]{#struct_0_14687_18620_x229028297}[]{#_Toc281559422}[\[ **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1957864771}[]{#_Toc281559423}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_546328994}[]{#_Toc281559424}

[]{#struct_0_14687_18620_x2141908279}[]{#_Toc281559425}[【缺省用户角色】]{style="font-family:黑体"}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_102875164}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_2145888286}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1887781546}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x560403536}

[]{#struct_0_14687_18620_x717390057}[]{#_Toc281559426}[【参数】]{style="font-family:黑体"}[]{#_Toc281559427}

[]{#struct_0_14687_18620_1718866518}[]{#_Toc281559428}**[green]{lang="EN-US"}**[：绿色报文。]{style="font-family:宋体"}[]{#_Toc281559429}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_x56038061}[：黄色报文。]{style="font-family:宋体"}[]{#_Toc281559430}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_1239818497}[：红色报文。]{style="font-family:宋体"}[]{#_Toc281559431}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1887847082}[：接收报文方向。]{style="font-family:宋体"}[]{#_Toc281559432}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x613362621}[：发送报文方向。]{style="font-family:宋体"}[]{#_Toc281559433}

[[其它参数请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_614525219}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}2-1]{lang="EN-US"}](?-2075031760#_Ref298430323)[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[]{#struct_0_14687_18620_1887257255}[]{#_Toc281559453}[![说明](QoS命令.files/image001.png){#图片 2 border="0" width="62" height="25"}]{lang="EN-US"}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x990980728}
:::

[ ]{lang="EN-US"}

[]{#struct_0_14687_18620_511846024}[]{#_Toc281559454}[【使用指导】]{style="font-family:黑体"}

[[经过流量监管处理的报文被分成了三种颜色（绿色、黄色、红色），为了对不同颜色报文进行优先级映射，设备提供了多张带颜色优先级映射表，分别对应相应颜色的优先级映射关系。流量监管对报文处理的相关内容请参见流量监管章节内容。]{style="font-family:宋体"}]{#struct_0_14687_18620_1560343721}

[]{#struct_0_14687_18620_x1090604611}[]{#_Toc281559455}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[如果未指定表的类型，将显示所有带颜色映射表的配置情况。]{style="font-family:宋体"}[]{#_Toc281559457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定颜色，将显示所有颜色的带颜色映射表的配置情况。]{style="font-family:宋体"}]{#struct_0_14687_18620_821111058}[]{#_Toc281559458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定方向，将显示所有方向带颜色映射表的配置情况。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1704517931}[]{#_Toc281559459}[]{#_Toc281559460}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1563656831}[]{#_Toc281559461}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1887322791}[显示绿色报文的接收报文方向的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到本地优先级映射表的配置信息。]{style="font-family:宋体"}[]{#_Toc281559462}

[[\<Sysname\> display qos map-table color green inbound exp-lp]{lang="EN-US"}]{#struct_0_14687_18620_x561279400}[]{#_Toc281559463}

[MAP-TABLE NAME: exp-lp   TYPE: pre-define   COLOR: green   DIRECTION: inbound[]{#_Toc281559464}]{lang="EN-US"}

[IMPORT  :  EXPORT[]{#_Toc281559465}]{lang="EN-US"}

[   0    :    0[]{#_Toc281559466}]{lang="EN-US"}

[   1    :    1[]{#_Toc281559467}]{lang="EN-US"}

[   2    :    2[]{#_Toc281559468}]{lang="EN-US"}

[   3    :    3[]{#_Toc281559469}]{lang="EN-US"}

[   4    :    4[]{#_Toc281559470}]{lang="EN-US"}

[   5    :    5[]{#_Toc281559471}]{lang="EN-US"}

[   6    :    6[]{#_Toc281559472}]{lang="EN-US"}

[   7    :    7 ]{lang="EN-US"}[]{#_Toc281559473}

[]{#_Toc164250243}[]{#_Toc163028021}[[表2-3 ]{lang="EN-US"}[display qos map-table color]{lang="EN-US"}]{#struct_0_14687_18620_510914660}[命令显示信息描述表]{style="font-family:黑体"}[]{#_Toc281559474}

[]{#table_struct_0_1689450137}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x2096104451}[]{#_Toc281559475}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1887126183}[]{#_Toc281559476}

[]{#_Toc281559477}

[[MAP-TABLE NAME]{lang="EN-US"}]{#struct_0_14687_18620_x1383505791}[]{#_Toc281559478}

[[映射表的名字]{style="font-family:宋体"}]{#struct_0_14687_18620_1091578405}[]{#_Toc281559479}

[]{#_Toc281559480}

[[TYPE]{lang="EN-US"}]{#struct_0_14687_18620_x1334332622}[]{#_Toc281559481}

[[映射表的类型]{style="font-family:宋体"}]{#struct_0_14687_18620_x835334693}[]{#_Toc281559482}

[]{#_Toc281559483}

[[COLOR]{lang="EN-US"}]{#struct_0_14687_18620_1114574799}[]{#_Toc281559484}

[[映射表的颜色]{style="font-family:宋体"}]{#struct_0_14687_18620_1887191719}[]{#_Toc281559485}

[]{#_Toc281559486}

[[DIRECTION]{lang="EN-US"}]{#struct_0_14687_18620_x936973329}[]{#_Toc281559487}

[[映射表的方向]{style="font-family:宋体"}]{#struct_0_14687_18620_x1575659631}[]{#_Toc281559488}

[]{#_Toc281559489}

[[IMPORT]{lang="EN-US"}]{#struct_0_14687_18620_x1428509556}[]{#_Toc281559490}

[[映射表的输入值]{style="font-family:宋体"}]{#struct_0_14687_18620_x1472432096}[]{#_Toc281559491}

[]{#_Toc281559492}

[[EXPORT]{lang="EN-US"}]{#struct_0_14687_18620_1887519399}[]{#_Toc281559493}

[[映射表的输出值]{style="font-family:宋体"}]{#struct_0_14687_18620_x544782693}[]{#_Toc281559494}

[]{#_Toc281559495}

[]{#_Toc281559496}[ ]{lang="EN-US"}

::: {#-1087837495 .myid}
[]{#_Toc404792336}[]{#struct_0_14687_18620_x1873926079}[]{#_Toc263759932}[]{#_Toc226262599}[]{#_Toc198110199}

**优先级映射 \-- 优先级映射表配置命令 \-- import**

------------------------------------------------------------------------

[**[import]{lang="EN-US"}**]{#struct_0_14687_18620_700535106}[命令用来配置指定优先级映射表的映射关系。]{style="font-family:宋体"}

[**[undo import]{lang="EN-US"}**]{#struct_0_14687_18620_x801603936}[命令用来删除配置的优先级映射表的映射关系，恢复其为缺省的映射关系。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1567785722}

[**[import]{lang="EN-US"}**[ ]{lang="EN-US"}*[import-value-list]{lang="EN-US"}*[ **export** *export-value*]{lang="EN-US"}]{#struct_0_14687_18620_x1276753383}

[**[undo import]{lang="EN-US"}**[ { ]{lang="EN-US"}*[import-value-list]{lang="EN-US"}*[ \| **all** }]{lang="EN-US"}]{#struct_0_14687_18620_1887584935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1330399546}

[[优先级映射表的映射关系请参见配置指导中的附录]{style="font-family:宋体"}[ B]{lang="EN-US"}]{#struct_0_14687_18620_x696957577}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_936942369}

[[优先级映射表视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x352596296}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1276065489}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_929665744}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1132664150}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887388327}

[*[import-value-list]{lang="EN-US"}*]{#struct_0_14687_18620_1031721663}[：输入值列表。]{style="font-family:宋体"}

[*[export-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1855283163}[：输出值。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_14687_18620_x415572667}[：]{style="font-family:宋体"}[删除配置地该映射表的所有映射关系，恢复其为缺省的映射关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1779296586}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1855123682}[配置]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到丢弃优先级映射表的映射关系，与]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[相对应的丢弃优先级为]{style="font-family:
宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x739981543}

[\[Sysname\] qos map-table dot1p-dp]{lang="EN-US"}

[\[Sysname-maptbl-dot1p-dp\] import 4 5 export 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1887453863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_x1405025711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table color]{lang="EN-US"}**]{#struct_0_14687_18620_415577938}
:::

::::: {#-1819781733 .myid}
[]{#_Toc404792337}[]{#struct_0_14687_18620_1260011688}[]{#_Toc263759933}[]{#_Toc226262600}[]{#_Toc198110200}

**优先级映射 \-- 优先级映射表配置命令 \-- qos map-table**

------------------------------------------------------------------------

[**[qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_44157023}[命令用来进入指定的优先级映射表视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1452143724}

[**[qos map-table]{lang="EN-US"}**[ \[ **inbound** \| **outbound** \] { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_x410698343}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1528531013}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1887781543}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x560731216}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_456431104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1371452224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1890721211}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_692577202}[：接收报文方向。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_1936916108}[：发送报文方向。]{style="font-family:宋体"}

[[其它参数请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_x1551357250}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}2-1]{lang="EN-US"}](?-2075031760#_Ref298430323)[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_1887847079}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x613821376}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_231104132}

[[每个优先级映射存在无方向、接收报文方向、发送报文方向三张不同的映射表。如果不指定方向，则表示进入无方向的优先级映射表视图。对映射表方向的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_805274635}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x317553936}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1589736620}[进入接收报文方向的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到丢弃优先级映射表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_182411332}

[\[Sysname\] qos map-table inbound dot1p-dp]{lang="EN-US"}

[\[Sysname-maptbl-in-dot1p-dp\]]{lang="NL"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1887257256}[进入发送报文方向的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级到丢弃优先级映射表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x990915192}

[\[Sysname\] qos map-table outbound dot1p-dp]{lang="EN-US"}

[\[Sysname-maptbl-out-dot1p-dp\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1240958052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table]{lang="EN-US"}**]{#struct_0_14687_18620_x907417716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import]{lang="EN-US"}**]{#struct_0_14687_18620_1736003378}
:::::

::::: {#1323497046 .myid}
[]{#_Toc115171260}[]{#_Toc404792338}[]{#struct_0_14687_18620_1796966844}[]{#_Toc263759934}[]{#_Toc226262601}[]{#_Toc198110201}[]{#_Toc167527003}

**优先级映射 \-- 优先级映射表配置命令 \-- qos map-table color**

------------------------------------------------------------------------

[**[qos map-table color]{lang="EN-US"}**]{#struct_0_14687_18620_x1202962241}[命令用来进入指定的带颜色优先级映射表视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_985016340}

[**[qos map-table]{lang="EN-US"}**[ **color** { **green** \| **yellow** \| **red** } \[ **inbound** \| **outbound** \] { **dot11e-lp** \| **dot1p-dot1p** \| **dot1p-dp** \| **dot1p-dscp** \| **dot1p-exp** \| **dot1p-lp** \| **dot1p-rpr** \| **dscp-dot1p**\| **dscp-dp** \| **dscp-dscp** \| **dscp-exp** \| **dscp-lp** \| **dscp-rpr** \| **exp-dot1p** \| **exp-dp** \| **exp-dscp** \| **exp-exp** \| **exp-lp** \| **exp-rpr** \| **ippre-rpr** \| **lp-dot11e** \| **lp-dot1p** \| **lp-dp** \| **lp-dscp** \| **lp-exp** \| **lp-lp** \| **up-dot1p** \| **up-dp** \| **up-dscp** \| **up-exp** \| **up-fc** \| **up-lp** \| **up-rpr** \| **up-up** }]{lang="EN-US"}]{#struct_0_14687_18620_1887322792}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x561082792}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1609369998}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x794935946}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x688946090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x141545845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1670794398}

[**[green]{lang="EN-US"}**]{#struct_0_14687_18620_1434964520}[：绿色报文。]{style="font-family:宋体"}

[**[yellow]{lang="EN-US"}**]{#struct_0_14687_18620_1887126184}[：黄色报文。]{style="font-family:宋体"}

[**[red]{lang="EN-US"}**]{#struct_0_14687_18620_x1383309183}[：红色报文。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_659690325}[：接收报文方向。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_108322306}[：发送报文方向。]{style="font-family:宋体"}

[[其它参数请参见]{style="font-family:宋体"}]{#struct_0_14687_18620_324207387}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}2-1]{lang="EN-US"}](?-2075031760#_Ref298430323)[。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){#图片 4 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_x953629006}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x837147896}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_189695032}

[[经过流量监管处理的报文被分成了三种颜色（绿色、黄色、红色），为了对不同颜色报文进行优先级映射，设备提供了多张带颜色优先级映射表，分别对应相应颜色的优先级映射关系。流量监管对报文处理的相关内容请参见流量监管章节内容。]{style="font-family:宋体"}]{#struct_0_14687_18620_1887191720}

[[每个优先级映射（颜色也相同）存在无方向、接收报文方向、发送报文方向三张不同的映射表。如果不指定方向，则表示进入无方向的优先级映射表视图。对映射表方向的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x936514580}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1950019568}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x464992779}[进入绿色报文的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[到本地优先级映射表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1572271398}

[\[Sysname\] qos map-table color green exp-lp]{lang="EN-US"}

[\[Sysname-maptbl-green-exp-lp\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1855245387}[进入红色报文的接收报文方向的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[到本地优先级映射表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1887519400}

[\[Sysname\] qos map-table color red inbound dscp-lp]{lang="EN-US"}

[\[Sysname-maptbl-red-in-dscp-lp\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1410942610}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos map-table color]{lang="EN-US"}**]{#struct_0_14687_18620_x1828119863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import]{lang="EN-US"}**]{#struct_0_14687_18620_2036894311}
:::::

::: {#-825556734 .myid}
[]{#_Toc404792340}[]{#struct_0_14687_18620_1442403590}[]{#_Toc263759936}[]{#_Toc226262603}[]{#_Toc198110203}[]{#_Toc115171262}

**优先级映射 \-- 端口优先级配置命令 \-- qos priority**

------------------------------------------------------------------------

[**[qos priority]{lang="EN-US"}**]{#struct_0_14687_18620_2012270270}[命令用来配置当前端口的端口优先级。]{style="font-family:宋体"}

[**[undo qos priority]{lang="EN-US"}**]{#struct_0_14687_18620_1393621085}[命令用来恢复端口优先级为缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1278600152}

[[支持多种类型端口优先级的设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_1887584936}

[**[qos priority ]{lang="EN-US"}**[{ **dot1p** ]{lang="EN-US"}[\| **dp** \| **dscp** \| **exp** \| **lp** } *priority-value*]{lang="EN-US"}]{#struct_0_14687_18620_1330334010}

[**[undo]{lang="EN-US"}**[ **qos** **priority** { **dot1p** \| **dp** \| **dscp** \| **exp** \| **lp** }]{lang="EN-US"}]{#struct_0_14687_18620_2082357971}

[[支持一种类型端口优先级的设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_x1623013348}

[**[qos priority ]{lang="EN-US"}***[priority-value]{lang="EN-US"}*]{#struct_0_14687_18620_x363506630}

[**[undo qos priority]{lang="EN-US"}**]{#struct_0_14687_18620_x1117397818}

[[上面两种情况都支持的设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_1707565342}

[**[qos priority ]{lang="EN-US"}**[\[ **dot1p** ]{lang="EN-US"}[\| **dp** \| **dscp** \| **exp** \| **lp** \] *priority-value*]{lang="EN-US"}]{#struct_0_14687_18620_x1576965559}

[**[undo]{lang="EN-US"}**[ **qos** **priority** \[ **dot1p** \| **dp** \| **dscp** \| **exp** \| **lp** \]]{lang="EN-US"}]{#struct_0_14687_18620_1887388328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1031131839}

[[支持一种类型端口优先级的设备]{style="font-family:宋体"}]{#struct_0_14687_18620_1290117216}[，端口优先级的缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[；支持多种类型端口优先级的设备，]{style="font-family:宋体"}**[lp]{lang="EN-US"}**[类型优先级的缺省值为]{style="font-family:宋体"}[2]{lang="EN-US"}[，]{style="font-family:宋体"}**[dp]{lang="EN-US"}**[类型优先级的缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，其余类型优先级没有缺省值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1219677482}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_464222598}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x56766133}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x282618337}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1887453864}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1404960175}

[*[priority-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1414206995}[：端口优先级值。当设备只支持一种类型的端口优先级时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[；当设备支持多种类型的端口优先级时，各优先级的取值范围如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}2-4]{lang="EN-US"}](?-825556734#_Ref189542338)[所示。]{style="font-family:
宋体"}

[]{#struct_0_14687_18620_x1863771689}[[表2-4 ]{lang="EN-US"}[各种端口优先级取值范围]{style="font-family:
黑体"}]{#_Ref189542338}

[]{#table_struct_0_1683403513}[[端口优先级类型]{style="font-family:黑体"}]{#struct_0_14687_18620_x1461903479}
:::

[*[priority-value]{lang="EN-US"}*]{#struct_0_14687_18620_x712572970}[取值范围]{style="font-family:黑体"}

[[说明]{style="font-family:黑体"}]{#struct_0_14687_18620_17557836}

[**[dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_1887781544}[（]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级）]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_x560272464}[～]{style="font-family:宋体"}[7]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_14687_18620_x1482683951}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_2009153713}[（]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级）]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_474587756}[～]{style="font-family:宋体"}[63]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_14687_18620_1514661473}

[**[exp]{lang="EN-US"}**]{#struct_0_14687_18620_1887847080}[（]{style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级）]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_x613231549}[～]{style="font-family:宋体"}[7]{lang="EN-US"}

[[-]{lang="EN-US"}]{#struct_0_14687_18620_1376017755}

[**[dp]{lang="EN-US"}**]{#struct_0_14687_18620_305888273}[（]{style="font-family:宋体"}[丢弃优先级）]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_1603678702}[～]{style="font-family:宋体"}[2]{lang="EN-US"}

[[丢弃优先级值越大的报文越被优先丢弃]{style="font-family:宋体"}]{#struct_0_14687_18620_x841626096}

[**[lp]{lang="EN-US"}**]{#struct_0_14687_18620_971986421}[（]{style="font-family:宋体"}[本地优先级）]{style="font-family:宋体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_702805537}[～]{style="font-family:宋体"}[7]{lang="EN-US"}

[[本地优先级值越大的报文，进入的队列优先级越高，从而能够获得优先的调度]{style="font-family:宋体"}]{#struct_0_14687_18620_x1371358070}

[ ]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){#图片 5 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_732637397}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x841560560}
:::

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1350111537}

[[对于支持多种类型端口优先级的设备，不同类型的端口优先级可以同时在同一个接口上配置，同一种类型的端口优先级配置采用覆盖方式。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1320374186}

[[需要注意的是，]{style="font-family:宋体"}]{#struct_0_14687_18620_1863637656}[对于上面两种情况都支持的设备，可能会出现某种类型不支持，此时配置失败，具体请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1833335870}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x479334873}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的端口优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[（支持一种类型端口优先级的设备）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1365038225}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos priority 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x410276106}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[20]{lang="EN-US"}[（支持多种类型端口优先级的设备）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x841757168}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos priority dscp 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1364380264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos trust interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1608756243}

::: {#-420797680 .myid}
[]{#_Toc404792342}[]{#struct_0_14687_18620_x1986024349}[]{#_Toc384134574}[]{#_Toc373747479}

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark { tcp-port \| udp-port }**

------------------------------------------------------------------------

[**[display qos remark ]{lang="EN-US"}**[{ **tcp-port** \| **udp-port** }]{lang="EN-US"}]{#struct_0_14687_18620_801998774}[命令用来]{style="font-family:宋体"}[显示所有]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口的报文优先级配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1363569548}

[**[display qos remark ]{lang="EN-US"}**[{ **tcp-port** \| **udp-port** }]{lang="EN-US"}]{#struct_0_14687_18620_x291848443}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1470463539}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1767250242}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x838446063}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1203501411}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_802064310}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1095805688}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1080538494}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_881775104}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_109095436}[显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口的优先级配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos remark tcp-port]{lang="EN-US"}]{#struct_0_14687_18620_x1004918284}

[TCP port based priorities]{lang="EN-US"}[：]{style="font-family:宋体"}

[ IP type   Port     DSCP   dot1p]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ IPv4      30       -      4]{lang="EN-US"}

[ IPv6      31-40    cs7    -]{lang="EN-US"}

[ IPAll     50       cs6    -]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_802391990}[显示]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口的优先级配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos remark udp-port]{lang="EN-US"}]{#struct_0_14687_18620_x559847421}

[UDP port based priorities]{lang="EN-US"}[：]{style="font-family:宋体"}

[ IP type   Port    DSCP   dot1p]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ IPv4      30      -      4]{lang="EN-US"}

[ IPv6      31-40   cs7    -]{lang="EN-US"}

[ IPAll     50      cs6    -]{lang="EN-US"}

[[表2-5 ]{lang="EN-US"}[display qos remark { tcp-port \| udp-port }]{lang="EN-US"}]{#struct_0_14687_18620_x794246447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_983450858}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_802457526}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x285216943}

[[IP type]{lang="EN-US"}]{#struct_0_14687_18620_801867703}

[[IP]{lang="EN-US"}]{#struct_0_14687_18620_801933239}[类型，取值情况如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4]{lang="EN-US"}]{#struct_0_14687_18620_x180472352}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv6]{lang="EN-US"}]{#struct_0_14687_18620_801736631}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPAll]{lang="EN-US"}]{#struct_0_14687_18620_801802167}[：表示所有的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_14687_18620_x1723422186}

[[端口号]{style="font-family:宋体"}]{#struct_0_14687_18620_802129847}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_802195383}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1986024350}[优先级值]{style="font-family:宋体"}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_801998775}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_802064311}[优先级值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#427429804 .myid}
[]{#_Toc404792343}[]{#struct_0_14687_18620_1095805689}[]{#_Toc384134577}[]{#_Toc373747481}

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark ip-address**

------------------------------------------------------------------------

[**[display qos remark ]{lang="EN-US"}[ip-address]{lang="EN-US"}**]{#struct_0_14687_18620_1080472958}[命令用]{style="font-family:宋体"}[来显示所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的报文优先级配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1640795571}

[**[display qos remark ip-address]{lang="EN-US"}**]{#struct_0_14687_18620_421782940}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x933028105}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x164657529}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_802391991}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x559847422}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x794443055}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x689715112}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x2110288878}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x540458686}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1901508141}[显示]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址优先级的配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos remark ip-address]{lang="EN-US"}]{#struct_0_14687_18620_802457527}

[IP address based priorities:]{lang="EN-US"}

[ IP address                                       DSCP      dot1p]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 10.13.3.50/24                                    -         4]{lang="EN-US"}

[ 123.17.3.50/16                                   -         4]{lang="EN-US"}

[ 10::121/120                                      cs7       -]{lang="EN-US"}

[[表2-6 ]{lang="EN-US"}[display qos remark ip-address]{lang="EN-US"}]{#struct_0_14687_18620_x285216944}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_975185106}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_478621050}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1927015649}

[[IP address]{lang="EN-US"}]{#struct_0_14687_18620_x1926950113}

[[IP]{lang="EN-US"}]{#struct_0_14687_18620_618526851}[地址]{style="font-family:宋体"}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1927146721}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1927081185}[优先级值]{style="font-family:宋体"}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x285177775}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x1926753505}[优先级值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#177683058 .myid}
[]{#_Toc404792344}[]{#struct_0_14687_18620_1392697789}[]{#_Toc384134580}[]{#_Toc373747485}

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark protocol**

------------------------------------------------------------------------

[**[display qos remark protocol]{lang="EN-US"}**]{#struct_0_14687_18620_x698888946}[命令用来]{style="font-family:
宋体"}[显示所有协议报文优先级的配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926687969}

[**[display qos remark protocol]{lang="EN-US"}**]{#struct_0_14687_18620_x1633943622}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_733544720}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2060608288}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_283948836}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1577430516}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1926884577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x795107524}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_853973566}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1023534995}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1680645926}[显示协议优先级配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos remark protocol]{lang="EN-US"}]{#struct_0_14687_18620_x1926819041}

[Protocol priorities]{lang="EN-US"}[：]{style="font-family:宋体"}

[ Protocol      dot1p]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ IP            -]{lang="EN-US"}

[ IPX           2]{lang="EN-US"}

[ ARP           5]{lang="EN-US"}

[ AppleTalk     -]{lang="EN-US"}

[ SNA           -]{lang="EN-US"}

[ NetBEUI       -]{lang="EN-US"}

[[表2-7 ]{lang="EN-US"}[display qos remark protocol]{lang="EN-US"}]{#struct_0_14687_18620_x1905753406}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1000843266}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926491361}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1839578393}

[[Protocol]{lang="EN-US"}]{#struct_0_14687_18620_x1926425825}

[[协议类型，取值包括：]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x1927015648}[、]{style="font-family:宋体"}[IPX]{lang="EN-US"}[、]{style="font-family:宋体"}[ARP]{lang="EN-US"}[、]{style="font-family:宋体"}[AppleTalk]{lang="EN-US"}[、]{style="font-family:宋体"}[SNA]{lang="EN-US"}[和]{style="font-family:宋体"}[NetBEUI]{lang="EN-US"}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x51359132}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x1926950112}[优先级值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1248932185 .myid}
[]{#_Toc404792345}[]{#struct_0_14687_18620_x947557090}[]{#_Toc384134582}[]{#_Toc373747487}

**优先级映射 \-- 全局优先级配置命令 \-- display qos remark vlan**

------------------------------------------------------------------------

[**[display qos remark vlan]{lang="EN-US"}**]{#struct_0_14687_18620_x1127887}[命令用来]{style="font-family:宋体"}[显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的报文优先级配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1927146720}

[**[display qos remark vlan]{lang="EN-US"}**]{#struct_0_14687_18620_883602052}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_582168226}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_2017266906}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1608719976}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x89386811}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x2139717168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1927081184}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1280906166}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1072914307}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_928843340}[显示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的优先级配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos remark vlan]{lang="EN-US"}]{#struct_0_14687_18620_x222748677}

[VLAN based priorities:]{lang="EN-US"}

[ VLAN        DSCP      dot1p]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 4           -         4]{lang="EN-US"}

[ 5           cs6       -]{lang="EN-US"}

[ 6           -         5]{lang="EN-US"}

[[表]{style="font-family:黑体"}[2-7 display qos remark vlan]{lang="EN-US"}]{#struct_0_14687_18620_x737696174}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_993506952}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926753504}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926687968}

[[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_x67859681}

[[VLAN ID]{lang="EN-US"}]{#struct_0_14687_18620_x1926884576}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x1926819040}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_823129949}[优先级值]{style="font-family:宋体"}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x1926491360}

[[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_889304962}[优先级值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1089921296 .myid}
[]{#_Toc404792346}[]{#struct_0_14687_18620_x1926425824}[]{#_Toc384134585}[]{#_Toc373747483}

**优先级映射 \-- 全局优先级配置命令 \-- display qos type-of-service**

------------------------------------------------------------------------

[**[display qos type-of-service]{lang="EN-US"}**]{#struct_0_14687_18620_961233854}[命令用来]{style="font-family:
宋体"}[显示服务类型的配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1763325909}

[**[display qos type-of-service]{lang="EN-US"}**]{#struct_0_14687_18620_1245068822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1110841168}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1001643683}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1912287889}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1927015651}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1871020705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1534118649}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x433337870}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_110068840}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1184118656}[显示服务类型的配置情况。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x546710333}

[\[Sysname\] qos type-of-service dscp]{lang="EN-US"}

[\[Sysname\] display qos type-of-service]{lang="EN-US"}

[ Type of service: dscp]{lang="EN-US"}

[[表2-8 ]{lang="EN-US"}[display qos type-of-service ]{lang="EN-US"}]{#struct_0_14687_18620_x1926950115}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1018730590}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1781326265}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1927146723}

[[Type of service]{lang="EN-US"}]{#struct_0_14687_18620_x1927081187}

[[服务类型，取值为]{style="font-family:宋体"}**[ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1447977189}[或]{style="font-family:宋体"}**[dscp]{lang="EN-US"}**

[[disabled]{lang="EN-US"}]{#struct_0_14687_18620_x1926753507}

[[非使能]{style="font-family:宋体"}]{#struct_0_14687_18620_x1739470093}

[[ip-precedence]{lang="EN-US"}]{#struct_0_14687_18620_x1926687971}

[[IP]{lang="EN-US"}]{#struct_0_14687_18620_x1926884579}[优先级]{style="font-family:宋体"}

[[dscp]{lang="EN-US"}]{#struct_0_14687_18620_x1926819043}

[[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_x742953992}[优先级]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#886750314 .myid}
[]{#struct_0_14687_18620_x1926491363}[]{#_Toc404792347}[]{#_Toc384134572}[]{#_Toc373747477}

**优先级映射 \-- 全局优先级配置命令 \-- qos remark { tcp-port \| udp-port }**

------------------------------------------------------------------------

[**[qos remark ]{lang="EN-US"}**[{ **tcp-port** \| **udp-port** }]{lang="EN-US"}]{#struct_0_14687_18620_x676778979}[命令重标记指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号的报文优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos remark** { **tcp-port** \| **udp-port** }]{lang="EN-US"}]{#struct_0_14687_18620_750214602}[命令用来取消指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口的报文的优先级配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_395375480}

[**[qos remark ]{lang="EN-US"}**[{ **tcp-port** \| **udp-port** } \[ **ipv4** \| **ipv6** \] *start-value* \[ **to** *end-value* \] { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]{lang="EN-US"}]{#struct_0_14687_18620_1963674182}

[**[undo qos remark ]{lang="EN-US"}**[{ **tcp-port** \| **udp-port** } \[ **ipv4** \| **ipv6** \] *start-value* \[ **to** *end-value* \] { **dot1p** \| **dscp** }]{lang="EN-US"}]{#struct_0_14687_18620_x68344322}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x473378736}

[[没有为指定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_14687_18620_x1926425827}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号的报文优先级进行重标记。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_557949327}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_395352360}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1970553053}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1104248125}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_970526240}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x278112131}

[**[ipv4]{lang="EN-US"}**]{#struct_0_14687_18620_374729521}[：指定匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_14687_18620_x1927015650}[：指定匹配]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的报文。如果未指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[，则表示匹配所有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[*[start-value]{lang="EN-US"}*[ \[ **to** *end-value* \]]{lang="EN-US"}]{#struct_0_14687_18620_304936764}[：指定一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号范围。]{style="font-family:宋体"}*[start-value]{lang="EN-US"}*[表示起始端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}*[end-value]{lang="EN-US"}*[表示结束端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}*[end-value]{lang="EN-US"}*[的值要大于或等于]{style="font-family:宋体"}*[start-value]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[**[dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_x82643992}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_71441101}[：]{style="font-family:
宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所]{style="font-family:宋体"}[示]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1355232084}

[[若报文同时匹配上目的端口规则和源端口规则，则匹配目的端口规则的配置生效。]{style="font-family:宋体"}]{#struct_0_14687_18620_x12829675}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_370087803}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x845496618}[重标记]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号属于]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[25]{lang="EN-US"}[的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1926950114}

[\[Sysname\] qos remark tcp-port ipv6 20 to 25 dot1p 4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_215242324}[重标记]{style="font-family:宋体"}[UCP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[69]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1038662463}

[\[Sysname\] qos remark udp-port ipv4 69 dot1p 4]{lang="EN-US"}
:::

::: {#590998464 .myid}
[]{#_Toc404792348}[]{#struct_0_14687_18620_x2032140791}[]{#_Toc384134575}[]{#_Toc384134573}

**优先级映射 \-- 全局优先级配置命令 \-- qos remark ip-address**

------------------------------------------------------------------------

[**[qos remark ip-address]{lang="EN-US"}**]{#struct_0_14687_18620_1034242363}[命令用来]{style="font-family:宋体"}[重标记指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的报文优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos remark ip-address**]{lang="EN-US"}]{#struct_0_14687_18620_x172949867}[命令用来取消]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址报文的]{style="font-family:宋体"}[优先级配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x358946453}

[**[qos remark ip-address ]{lang="EN-US"}**[{ *ipv4-address* \[ *mask-length \| mask* \] \| *ipv6-address* \[ *prefix-length* \] } { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]{lang="EN-US"}]{#struct_0_14687_18620_x1927146722}

[**[undo qos remark ip-address ]{lang="EN-US"}**[{ *ipv4-address* \[ *mask-length \| mask* \] \| *ipv6-address* \[ *prefix-length* \] }{ **dot1p** \| **dscp** }]{lang="EN-US"}]{#struct_0_14687_18620_x279197362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_737954045}

[[没有为指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_985275107}[地址的报文优先级进行重标记。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1775120860}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_803166154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x293160501}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1651563102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1927081186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_118106752}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_14687_18620_x931080891}[：指定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}[为点分十进制格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_14687_18620_33874342}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的]{style="font-family:宋体"}[掩码长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_14687_18620_831076835}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的掩码，]{style="font-family:宋体"}[为点分十进制格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_14687_18620_x1575238786}[：指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_14687_18620_x1077279862}[：]{style="font-family:宋体"}[前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1926753506}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_989413262}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}](http://press/data/infoblade/Comware%20V7平台中文/1.2.11%20ACL和QoS/1.2.11.02%20QoS/QoS命令.htm#_Ref163816081)[[1-5]{lang="EN-US"}](http://press/data/infoblade/Comware%20V7平台中文/1.2.11%20ACL和QoS/1.2.11.02%20QoS/QoS命令.htm#_Ref163816081)[所示]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x730690210}

[[若同时匹配上源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x533208363}[地址和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，则匹配目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的配置生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1332115774}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x419757676}[重标记]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.15.10.1/24]{lang="EN-US"}[的报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_716523354}

[\[Sysname\] qos remark ip-address 10.15.10.1 24 dot1p 4]{lang="EN-US"}
:::

::: {#-1507689303 .myid}
[]{#_Toc404792349}[]{#struct_0_14687_18620_x1926687970}[]{#_Toc384134578}[]{#_Toc373747484}[]{#_Toc384134576}

**优先级映射 \-- 全局优先级配置命令 \-- qos remark protocol**

------------------------------------------------------------------------

[**[qos remark protocol]{lang="EN-US"}**]{#struct_0_14687_18620_x424024505}[命令用来重标记指定协议报文的优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos remark protocol**]{lang="EN-US"}]{#struct_0_14687_18620_195374600}[命令用来取消指定协议报文的优先级配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1962579698}

[**[qos remark protocol ]{lang="EN-US"}***[protocol-name ]{lang="EN-US"}***[dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1597862788}

[**[undo qos remark protocol ]{lang="EN-US"}***[protocol-name ]{lang="EN-US"}***[dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x1730135630}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926884578}

[[没有为]{style="font-family:宋体"}]{#struct_0_14687_18620_320637723}[指定协议报文的]{style="font-family:宋体"}[优先级进行重标记。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_88897751}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2067484798}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1126084176}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x238329479}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1398730122}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926819042}

[**[protocol ]{lang="EN-US"}***[protocol-name]{lang="EN-US"}*]{#struct_0_14687_18620_1985929363}[：指定协议类型为]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPX]{lang="EN-US"}[、]{style="font-family:宋体"}[ARP]{lang="EN-US"}[、]{style="font-family:宋体"}[AppleTalk]{lang="EN-US"}[、]{style="font-family:宋体"}[SNA]{lang="EN-US"}[或]{style="font-family:宋体"}[NetBEUI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_x260094448}**[：]{style="font-family:宋体"}**[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_6943432}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1444039162}[重标记]{style="font-family:宋体"}[ARP]{lang="EN-US"}[协议报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_262298959}

[\[Sysname\] qos remark protocol arp dot1p 4]{lang="EN-US"}
:::

::: {#1137721755 .myid}
[]{#_Toc404792350}[]{#struct_0_14687_18620_x644530303}[]{#_Toc384134581}[]{#_Toc373747486}[]{#_Toc384134579}

**优先级映射 \-- 全局优先级配置命令 \-- qos remark vlan**

------------------------------------------------------------------------

[**[qos remark vlan]{lang="EN-US"}**]{#struct_0_14687_18620_956043566}[命令用来重标记指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围的报文的优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos remark vlan**]{lang="EN-US"}]{#struct_0_14687_18620_x1926491362}[命令用来取消指定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[或]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[范围报文的优先级配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2052104376}

[**[qos remark vlan ]{lang="EN-US"}***[start-vlan-id ]{lang="EN-US"}*[\[ **to** *end-vlan-id* \] { **dot1p** *dot1p-value* \| **dscp** *dscp-value* }]{lang="EN-US"}]{#struct_0_14687_18620_857163196}

[**[undo qos remark vlan ]{lang="EN-US"}***[start-vlan-id ]{lang="EN-US"}*[\[ **to** *end-vlan-id* \] { **dot1p** \| **dscp** }]{lang="EN-US"}]{#struct_0_14687_18620_x2102601268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x15250590}

[[没有为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_298494819}[内的报文的优先级进行重标记。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_511952071}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_14349447}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1926425826}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2124033268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1290173130}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_847760169}

[*[start-vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_1629346236}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[start-vlan-id]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_14687_18620_158026441}**[to]{lang="EN-US"}***[ ]{lang="EN-US"}[end-vlan-id]{lang="EN-US"}*[：指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号范围。]{style="font-family:宋体"}*[start-vlan-id]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}*[end-vlan-id]{lang="EN-US"}*[的值要大于或等于]{style="font-family:宋体"}*[start-vlan-id]{lang="EN-US"}*[的值。]{style="font-family:宋体"}

[**[dot1p ]{lang="EN-US"}***[dot1p-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1210693088}[：]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1927015653}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所示]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1261147177}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x745960229}[重标记]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[内的报文的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x65924684}

[\[Sysname\] qos remark vlan 2 dot1p 4]{lang="EN-US"}
:::

::: {#-1701198815 .myid}
[]{#_Toc404792351}[]{#struct_0_14687_18620_x2476480}[]{#_Toc384134583}[]{#_Toc373747482}

**优先级映射 \-- 全局优先级配置命令 \-- qos type-of-service**

------------------------------------------------------------------------

[**[qos ]{lang="EN-US"}[type-of-service]{lang="EN-US"}**]{#struct_0_14687_18620_426432363}[命令用来配置设备的服务类型]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos** **type-of-service**]{lang="EN-US"}]{#struct_0_14687_18620_x1019372424}[命令用来取消服务类型的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x91508719}

[**[qos type-of-service]{lang="EN-US"}**[ { **ip-precedence** \| **dscp** }]{lang="EN-US"}]{#struct_0_14687_18620_x1926950117}

[**[undo qos type-of-service]{lang="EN-US"}**]{#struct_0_14687_18620_x1350841617}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x912151588}

[[没有配置设备的服务类型。]{style="font-family:宋体"}]{#struct_0_14687_18620_152001911}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x199537325}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1764137631}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1927146725}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1643116939}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_745572373}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_432123124}

[**[ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1589668930}[：全局信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，以此优先级进行优先级映射。]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1315476774}[：全局信任]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，以此优先级进行优先级映射。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1694952916}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1221628338}[配置服务类型为]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1927081189}

[\[Sysname\] qos type-of-service dscp]{lang="EN-US"}
:::

::: {#163396193 .myid}
[]{#_Toc404792353}[]{#struct_0_14687_18620_2105525153}[]{#_Toc263759938}[]{#_Toc226262605}[]{#_Toc198110205}[]{#_Toc115171264}

**优先级映射 \-- 端口优先级信任模式配置命令 \-- display qos trust interface**

------------------------------------------------------------------------

[**[display qos trust interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1010278762}[命令用来显示当前配置的端口优先级信任模式信息和端口优先级的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841691632}

[**[display qos trust]{lang="EN-US"}**[ **interface** \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1755281880}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_2111637500}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_956263809}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1977103278}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1680995774}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x780747434}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_194421466}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x841363952}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2143314857}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1173395511}[：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的端口优先级信任模式信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x60166491}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1722235888}[显示当前配置的端口优先级信任模式信息（支持一种类型端口优先级的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display qos trust interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_524442761}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Port priority trust information]{lang="EN-US"}

[  Port priority:4]{lang="EN-US"}

[  Port priority trust type: exp,  Override: disable]{lang="EN-US"}

[[表2-9 ]{lang="EN-US"}[display qos trust interface]{lang="EN-US"}]{#struct_0_14687_18620_x1093276594}[命令显示信息描述表（支持一种类型端口优先级的设备）]{style="font-family:黑体"}

[]{#table_struct_0_1684101177}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x841298416}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x215566973}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x774390857}

[[接口名，由接口类型和接口编号构成]{style="font-family:宋体"}]{#struct_0_14687_18620_x1709243848}

[[Port priority trust information]{lang="EN-US"}]{#struct_0_14687_18620_1724011169}

[[端口优先级信任信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x841495024}

[[Port priority]{lang="EN-US"}]{#struct_0_14687_18620_596030335}

[[端口优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_449421505}

[[Port priority trust type]{lang="EN-US"}]{#struct_0_14687_18620_x1136418366}

[[端口优先级信任类型，取值为：]{style="font-family:宋体"}]{#struct_0_14687_18620_x1355358980}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_14687_18620_x1667487422}[：根据报文的类型，自动提取报文中的优先级字段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dot11e]{lang="EN-US"}]{#struct_0_14687_18620_x841429488}[：]{lang="EN-US" style="font-family:宋体"}[dot11e]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x1808979255}[：]{lang="EN-US" style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dscp]{lang="EN-US"}]{#struct_0_14687_18620_x741227879}[：]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[exp]{lang="EN-US"}]{#struct_0_14687_18620_1038272927}[：]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_14687_18620_x841101808}[：不信任任何优先级]{lang="EN-US" style="font-family:宋体"}

[[Override]{lang="EN-US"}]{#struct_0_14687_18620_1369408870}

[[是否覆盖报文本身的优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_1613606509}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_971370008}[显示当前配置的端口优先级信任模式信息（支持多种类型端口优先级的设备）。]{style="font-family:宋体"}

[[\<Sysname\> display qos trust interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_x841036272}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Port priority trust information]{lang="EN-US"}

[  Port dot1p priority: 4]{lang="EN-US"}

[  Port dscp priority: 32]{lang="EN-US"}

[  Port dp priority: 1]{lang="EN-US"}

[  Port exp priority: 7]{lang="EN-US"}

[  Port lp priority: 5]{lang="EN-US"}

[  Port priority trust type: exp,  Override: disable]{lang="EN-US"}

[[表2-10 ]{lang="EN-US"}[display qos trust interface]{lang="EN-US"}]{#struct_0_14687_18620_1360155845}[命令显示信息描述表（支持多种类型端口优先级的设备）]{style="font-family:黑体"}

[]{#table_struct_0_1678050457}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1782684344}

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1887745641}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_1253258573}

[[接口名，由接口类型和接口编号构成]{style="font-family:宋体"}]{#struct_0_14687_18620_x125580756}

[[Port priority trust information]{lang="EN-US"}]{#struct_0_14687_18620_x841626095}

[[端口优先级信任信息]{style="font-family:宋体"}]{#struct_0_14687_18620_971789813}

[[Port dot1p priority]{lang="EN-US"}]{#struct_0_14687_18620_x262551409}

[[端口]{style="font-family:宋体"}[802.1p]{lang="EN-US"}]{#struct_0_14687_18620_686724544}[优先级]{style="font-family:宋体"}

[[Port dscp priority]{lang="EN-US"}]{#struct_0_14687_18620_679705872}

[[端口]{style="font-family:宋体"}[DSCP]{lang="EN-US"}]{#struct_0_14687_18620_406230605}[优先级]{style="font-family:宋体"}

[[Port dp priority]{lang="EN-US"}]{#struct_0_14687_18620_x841560559}

[[端口丢弃优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_1349521716}

[[Port exp priority]{lang="EN-US"}]{#struct_0_14687_18620_725989327}

[[端口]{style="font-family:宋体"}[EXP]{lang="EN-US"}]{#struct_0_14687_18620_x1291079997}[优先级]{style="font-family:宋体"}

[[Port lp priority]{lang="EN-US"}]{#struct_0_14687_18620_x841757167}

[[端口本地优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_1364314728}

[[Port priority trust type]{lang="EN-US"}]{#struct_0_14687_18620_x463591843}

[[端口优先级信任类型，取值为：]{style="font-family:宋体"}]{#struct_0_14687_18620_554276292}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[auto]{lang="EN-US"}]{#struct_0_14687_18620_x1681241536}[：根据报文的类型，自动提取报文中的优先级字段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dot11e]{lang="EN-US"}]{#struct_0_14687_18620_x841691631}[：]{lang="EN-US" style="font-family:宋体"}[dot11e]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dot1p]{lang="EN-US"}]{#struct_0_14687_18620_x1755347416}[：]{lang="EN-US" style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dscp]{lang="EN-US"}]{#struct_0_14687_18620_x1218323074}[：]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[exp]{lang="EN-US"}]{#struct_0_14687_18620_902074415}[：]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[优先级]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[none]{lang="EN-US"}]{#struct_0_14687_18620_x841363951}[：不信任任何优先级]{lang="EN-US" style="font-family:宋体"}

[[Override]{lang="EN-US"}]{#struct_0_14687_18620_x2143511465}

[[是否覆盖报文本身的优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_x1947697521}

[ ]{lang="EN-US"}

::::: {#1279462988 .myid}
[]{#_Toc404792354}[]{#struct_0_14687_18620_x1855700280}[]{#_Toc263759939}[]{#_Toc226262606}[]{#_Toc198110206}[]{#_Toc115171265}

**优先级映射 \-- 端口优先级信任模式配置命令 \-- qos trust**

------------------------------------------------------------------------

[**[qos trust]{lang="EN-US"}**]{#struct_0_14687_18620_1303548341}[命令用来配置端口优先级信任模式。]{style="font-family:宋体"}

[**[undo qos trust]{lang="EN-US"}**]{#struct_0_14687_18620_2092746779}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841298415}

[**[qos trust]{lang="EN-US"}**[ { **auto** \| **dot11e** \| **dot1p** \| **dscp** \| **exp** \| **none** } \[ **override** \]]{lang="EN-US"}]{#struct_0_14687_18620_x215632509}

[**[undo qos trust]{lang="EN-US"}**]{#struct_0_14687_18620_x799610455}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x205642133}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1416300651}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1871641275}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_460481764}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x460035253}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x841495023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_596489087}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2082258595}

[**[auto]{lang="EN-US"}**]{#struct_0_14687_18620_524497818}[：表示根据报文的类型，自动提取报文中的优先级字段进行优先级映射。对于二层报文，采用]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级；对于三层报文，采用]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级；对于]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文，采用]{style="font-family:宋体"}[EXP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dot11e]{lang="EN-US"}**]{#struct_0_14687_18620_1972295323}[：]{style="font-family:宋体"}[信任]{style="font-family:宋体"}[802.11]{lang="EN-US"}[报文携带的]{style="font-family:宋体"}[dot11e]{lang="EN-US"}[优先级，以此优先级进行优先级映射。该参数只能在]{style="font-family:宋体"}[WLAN-ESS]{lang="EN-US"}[接口上进行配置。]{style="font-family:宋体"}

[**[dot1p]{lang="EN-US"}**]{#struct_0_14687_18620_x1492872424}[：信任报文自带的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，以此优先级进行优先级映射。]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x1785010234}[：信任]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文自带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[，以此优先级进行优先级映射。]{style="font-family:宋体"}

[**[exp]{lang="EN-US"}**]{#struct_0_14687_18620_x841429487}[：信任]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文自带的]{style="font-family:宋体"}[EXP]{lang="EN-US"}[，以此优先级进行优先级映射。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_14687_18620_x1809175863}[：不信任任何优先级。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[override]{lang="EN-US"}**]{#struct_0_14687_18620_1872877898}[：表示通过优先级映射表取得的优先级将覆盖报文本身的优先级，缺省为不覆盖。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){#图片 6 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_x100107507}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[各个参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_415649456}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1542536744}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1423017868}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置优先级信任模式为信任报文自带的]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x841101807}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos trust dot1p]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1368950118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos trust interface]{lang="EN-US"}**]{#struct_0_14687_18620_1996903078}[]{#_Toc292375533}[]{#_Toc263760003}[]{#_Toc226262670}[]{#_Toc198110179}[]{#_Ref122760117}[]{#_Ref122760115}[]{#_Toc121389321}[]{#_Toc232219687}[]{#_Toc232395272}[]{#_Toc232395632}[]{#_Toc232219688}[]{#_Toc232395273}[]{#_Toc232395633}[]{#_Toc232219690}[]{#_Toc232395275}[]{#_Toc232395635}[]{#_Toc232219691}[]{#_Toc232395276}[]{#_Toc232395636}[]{#_Toc232219692}[]{#_Toc232395277}[]{#_Toc232395637}[]{#_Toc232219693}[]{#_Toc232395278}[]{#_Toc232395638}[]{#_Toc232219694}[]{#_Toc232395279}[]{#_Toc232395639}[]{#_Toc232219695}[]{#_Toc232395280}[]{#_Toc232395640}[]{#_Toc232219696}[]{#_Toc232395281}[]{#_Toc232395641}[]{#_Toc232219697}[]{#_Toc232395282}[]{#_Toc232395642}[]{#_Toc232219698}[]{#_Toc232395283}[]{#_Toc232395643}[]{#_Toc232219699}[]{#_Toc232395284}[]{#_Toc232395644}[]{#_Toc232219700}[]{#_Toc232395285}[]{#_Toc232395645}[]{#_Toc232219701}[]{#_Toc232395286}[]{#_Toc232395646}[]{#_Toc232219702}[]{#_Toc232395287}[]{#_Toc232395647}[]{#_Toc232219703}[]{#_Toc232395288}[]{#_Toc232395648}[]{#_Toc232219704}[]{#_Toc232395289}[]{#_Toc232395649}[]{#_Toc232219705}[]{#_Toc232395290}[]{#_Toc232395650}[]{#_Toc232219706}[]{#_Toc232395291}[]{#_Toc232395651}[]{#_Toc232219707}[]{#_Toc232395292}[]{#_Toc232395652}[]{#_Toc232219710}[]{#_Toc232395295}[]{#_Toc232395655}[]{#_Toc232219711}[]{#_Toc232395296}[]{#_Toc232395656}[]{#_Toc232219712}[]{#_Toc232395297}[]{#_Toc232395657}[]{#_Toc232219715}[]{#_Toc232395300}[]{#_Toc232395660}[]{#_Toc232219716}[]{#_Toc232395301}[]{#_Toc232395661}[]{#_Toc232219717}[]{#_Toc232395302}[]{#_Toc232395662}[]{#_Toc232219718}[]{#_Toc232395303}[]{#_Toc232395663}[]{#_Toc232219719}[]{#_Toc232395304}[]{#_Toc232395664}[]{#_Toc232219720}[]{#_Toc232395305}[]{#_Toc232395665}[]{#_Toc232219721}[]{#_Toc232395306}[]{#_Toc232395666}[]{#_Toc232219722}[]{#_Toc232395307}[]{#_Toc232395667}[]{#_Toc232219723}[]{#_Toc232395308}[]{#_Toc232395668}[]{#_Toc232219724}[]{#_Toc232395309}[]{#_Toc232395669}[]{#_Toc232219725}[]{#_Toc232395310}[]{#_Toc232395670}[]{#_Toc232219726}[]{#_Toc232395311}[]{#_Toc232395671}[]{#_Toc232219735}[]{#_Toc232395320}[]{#_Toc232395680}[]{#_Toc232219736}[]{#_Toc232395321}[]{#_Toc232395681}[]{#_Toc232219738}[]{#_Toc232395323}[]{#_Toc232395683}[]{#_Toc232219739}[]{#_Toc232395324}[]{#_Toc232395684}[]{#_Toc232219740}[]{#_Toc232395325}[]{#_Toc232395685}[]{#_Toc232219741}[]{#_Toc232395326}[]{#_Toc232395686}[]{#_Toc232219742}[]{#_Toc232395327}[]{#_Toc232395687}[]{#_Toc232219743}[]{#_Toc232395328}[]{#_Toc232395688}[]{#_Toc232219744}[]{#_Toc232395329}[]{#_Toc232395689}[]{#_Toc232219745}[]{#_Toc232395330}[]{#_Toc232395690}[]{#_Toc232219746}[]{#_Toc232395331}[]{#_Toc232395691}[]{#_Toc232219747}[]{#_Toc232395332}[]{#_Toc232395692}[]{#_Toc232219748}[]{#_Toc232395333}[]{#_Toc232395693}[]{#_Toc232219749}[]{#_Toc232395334}[]{#_Toc232395694}[]{#_Toc232219752}[]{#_Toc232395337}[]{#_Toc232395697}[]{#_Toc232395699}[]{#_Toc232395700}[]{#_Toc232395701}[]{#_Toc232395702}[]{#_Toc232395703}[]{#_Toc232395704}[]{#_Toc232395705}[]{#_Toc232395706}[]{#_Toc232395707}[]{#_Toc232395708}[]{#_Toc232395709}[]{#_Toc232395710}[]{#_Toc232395711}[]{#_Toc232219755}[]{#_Toc232395340}[]{#_Toc232395716}[]{#_Toc232219756}[]{#_Toc232395341}[]{#_Toc232395717}[]{#_Toc232219757}[]{#_Toc232395342}[]{#_Toc232395718}[]{#_Toc232219758}[]{#_Toc232395343}[]{#_Toc232395719}[]{#_Toc232219759}[]{#_Toc232395344}[]{#_Toc232395720}[]{#_Toc232219760}[]{#_Toc232395345}[]{#_Toc232395721}[]{#_Toc232219761}[]{#_Toc232395346}[]{#_Toc232395722}[]{#_Toc232219762}[]{#_Toc232395347}[]{#_Toc232395723}[]{#_Toc232219763}[]{#_Toc232395348}[]{#_Toc232395724}[]{#_Toc232219764}[]{#_Toc232395349}[]{#_Toc232395725}[]{#_Toc232219765}[]{#_Toc232395350}[]{#_Toc232395726}[]{#_Toc232219766}[]{#_Toc232395351}[]{#_Toc232395727}[]{#_Toc232219767}[]{#_Toc232395352}[]{#_Toc232395728}[]{#_Toc232219768}[]{#_Toc232395353}[]{#_Toc232395729}[]{#_Toc136320727}[]{#_Toc136320728}[]{#_Toc136320729}[]{#_Toc136320730}[]{#_Toc136320731}[]{#_Toc136320732}[]{#_Toc136320733}[]{#_Toc136320734}[]{#_Toc136320735}[]{#_Toc136320736}[]{#_Toc136320737}[]{#_Toc136320738}[]{#_Hlt12351224}[]{#_Hlt8879577}[]{#_Hlt535641528}[]{#_Toc238290181}[]{#_Toc238290182}[]{#_Toc238290183}[]{#_Toc238290184}[]{#_Toc238290185}[]{#_Toc238290186}[]{#_Toc238290187}[]{#_Toc238290188}[]{#_Toc238290189}[]{#_Toc238290190}[]{#_Toc238290191}[]{#_Toc238290192}[]{#_Toc238290193}[]{#_Toc238290194}[]{#_Toc238290195}[]{#_Toc238290196}[]{#_Toc238290197}[]{#_Toc238290199}[]{#_Toc238290200}
:::::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section4 style="layout-grid:15.85pt"}
:::

::: {#1432667186 .myid}
[]{#_Toc404792357}[]{#struct_0_14687_18620_x100465500}[]{#_Toc312330751}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- display qos car interface**

------------------------------------------------------------------------

[**[display qos car interface]{lang="EN-US"}**]{#struct_0_14687_18620_1573927017}[命令用来显示接口的流量监管配置情况和统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1232370405}

[**[display qos car interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x841036271}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1360352453}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1344717534}

[[【缺省级别】]{style="font-family:黑体"}]{#struct_0_14687_18620_x280231360}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2036418339}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1698306304}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x865296986}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_66509884}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841626098}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_972117493}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的流量监管配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1696300893}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x2136385338}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的流量监管配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos car interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_x1768340883}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Direction: inbound]{lang="EN-US"}

[  Rule: If-match any]{lang="EN-US"}

[   CIR 128 (kbps), CBS 8000 (Bytes), PIR 128 (kbps), EBS 512 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1926687972}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[的流量监管配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos car interface gigabitethernet 1/0/2]{lang="EN-US"}]{#struct_0_14687_18620_x1586823919}

[Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[ Direction: inbound]{lang="EN-US"}

[  Rule: If-match any]{lang="EN-US"}

[   CIR 50 (%), CBS 600 (ms), EBS 0 (ms)]{lang="EN-US"}[，]{style="font-family:宋体"}[PIR 50 (%)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[[表3-1 ]{lang="EN-US"}[display qos car interface]{lang="EN-US"}]{#struct_0_14687_18620_x841560562}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1708757081}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1350242609}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1834695709}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x803090990}

[[接口名，由接口类型和接口编号结合在一起组成]{style="font-family:宋体"}]{#struct_0_14687_18620_1452404853}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_615993884}

[[指定流量监管的方向]{style="font-family:宋体"}]{#struct_0_14687_18620_x841757170}

[[Rule]{lang="EN-US"}]{#struct_0_14687_18620_1363855977}

[[数据包的匹配规则]{style="font-family:宋体"}]{#struct_0_14687_18620_495688144}

[[CIR]{lang="EN-US"}]{#struct_0_14687_18620_x660891129}

[[承诺信息速率，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_x1065773468}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[%]{lang="EN-US"}

[[CBS]{lang="EN-US"}]{#struct_0_14687_18620_x841691634}

[[承诺突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x1755675096}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[EBS]{lang="EN-US"}]{#struct_0_14687_18620_x1974866871}

[[超出突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x2008309132}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[PIR]{lang="EN-US"}]{#struct_0_14687_18620_1788577868}

[[峰值信息速率，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_x841363954}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[%]{lang="EN-US"}

[[Green action]{lang="EN-US"}]{#struct_0_14687_18620_x2143708073}

[[对绿色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x1402916302}

[[Yellow action]{lang="EN-US"}]{#struct_0_14687_18620_490995935}

[[对黄色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x1248188660}

[[Red action]{lang="EN-US"}]{#struct_0_14687_18620_x841298418}

[[对红色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x215960189}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x407186678}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_748083728}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x841495026}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_596161407}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_2003834363}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_104523987}

[ ]{lang="EN-US"}

::: {#-88513480 .myid}
[]{#_Toc312330752}[]{#_Toc404792358}[]{#struct_0_14687_18620_1759927692}[]{#_Toc335120923}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- display qos carl**

------------------------------------------------------------------------

[**[display qos carl]{lang="EN-US"}**]{#struct_0_14687_18620_x841429490}[命令用来显示]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1809503544}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_x1139047255}

[**[display qos carl]{lang="EN-US"}**[ \[ *carl-index* \]]{lang="EN-US"}]{#struct_0_14687_18620_76761905}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_14687_18620_110628484}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos carl]{lang="EN-US"}**[ \[ *carl-index* \] \[ **slot**]{lang="EN-US"}]{#struct_0_14687_18620_x1139506008}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}*[slot-number ]{lang="EN-US"}*[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_14687_18620_x1139571544}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display qos carl]{lang="EN-US"}**[ \[ *carl-index* \] \[]{lang="EN-US"}]{#struct_0_14687_18620_551027679}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[chassis]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体;color:blue"}*[chassis-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}**[slot]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:blue"}*[slot-number]{lang="EN-US"}*[ ]{lang="EN-US" style="font-size:10.0pt;font-family:宋体;color:blue"}[\[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x892656507}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1779036259}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1613478196}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_203718344}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x287671088}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x841101810}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1368884583}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x756013768}

[*[carl-index]{lang="EN-US"}*]{#struct_0_14687_18620_x52653103}[：]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的号码，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x1139702616}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用主控板的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[的配置信息。]{style="font-family:宋体"}[（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_14687_18620_x1139243864}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。]{style="font-family:宋体"}[如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的配置信息。]{style="font-family:宋体"}[（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1632240787}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_14687_18620_x2078828045}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，则显全局主用主控板上的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的配置信息。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x400311877}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表信息]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_278863620}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2086767148}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x574401630}[显示所有的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[\<Sysname\> display qos carl 1]{lang="EN-US"}]{#struct_0_14687_18620_x841036274}

[List  Rules]{lang="EN-US"}

[1     destination-ip-address range 1.1.1.1 to 1.1.1.2 per-address shared-bandwidth]{lang="EN-US"}

[2     destination-ip-address subnet 1.1.1.1 22 per-address shared-bandwidth]{lang="EN-US"}

[4     dscp 1 2 3 4 5 6 7 cs1]{lang="EN-US"}

[5     mac 0000-0000-0000]{lang="EN-US"}

[6     mpls-exp 0 1 2]{lang="EN-US"}

[9     precedence 0 1 2 3 4 5 6 7]{lang="EN-US"}

[10    source-ip-address range 1.1.1.1 to 1.1.1.2]{lang="EN-US"}

[11    source-ip-address subnet 1.1.1.1 31]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display qos carl]{lang="EN-US"}]{#struct_0_14687_18620_1360549061}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1704746457}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_636429030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_724317701}

[[List]{lang="EN-US"}]{#struct_0_14687_18620_x965876949}

[[CAR]{lang="EN-US"}]{#struct_0_14687_18620_x167584410}[列表号码]{style="font-family:宋体"}

[[Rules]{lang="EN-US"}]{#struct_0_14687_18620_x841626097}

[[数据包的匹配规则]{style="font-family:宋体"}]{#struct_0_14687_18620_971920885}

[ ]{lang="EN-US"}

::: {#1470967990 .myid}
[]{#_Toc404792359}[]{#struct_0_14687_18620_x106575925}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car (interface view)**

------------------------------------------------------------------------

[**[qos]{lang="EN-US"}**[ **car**]{lang="EN-US"}]{#struct_0_14687_18620_1605908552}[命令用来在接口上配置流量监管。]{style="font-family:宋体"}

[**[undo qos car]{lang="EN-US"}**]{#struct_0_14687_18620_x871708771}[命令用来取消接口上流量监管的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1886298679}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-numbe*r \| **carl** *carl-index* } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x841560561}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-numbe*r \| **carl** *carl-index* } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x231615840}

[**[undo qos car]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-number* \| **carl** *carl-index* }]{lang="EN-US"}]{#struct_0_14687_18620_1350046001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_656632175}

[[接口上没有配置流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_836414019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1134783867}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1984399707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x646625448}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_437826498}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1434717526}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841757169}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_1364445800}[：对接口接收到的数据包进行流量监管。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1970562481}[：对接口发送的数据包进行流量监管。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_1753719172}[：对所有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包进行流量监管。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}**[\[ **ipv6** \] *acl-number*]{lang="EN-US"}]{#struct_0_14687_18620_184833253}[：对匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的数据包进行流量监管。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[；否则表示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[carl ]{lang="EN-US"}***[carl-index]{lang="EN-US"}*]{#struct_0_14687_18620_1198938822}[：对匹配]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的数据包进行限速。]{style="font-family:宋体"}*[carl-index]{lang="EN-US"}*[为承诺访问速率列表编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_1380364972}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *committed-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_500386304}[：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *excess-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x841691633}[：过度突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x1755216344}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[green ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_710775844}[：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[red ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_409710195}[：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[yellow ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_1358745257}[：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[action]{lang="EN-US"}*]{#struct_0_14687_18620_109501870}[：对数据包采取的动作，有以下几种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[continue]{lang="EN-US"}**]{#struct_0_14687_18620_x1211517995}[：继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[discard]{lang="EN-US"}**]{#struct_0_14687_18620_x1444994431}[：丢弃数据包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pass]{lang="EN-US"}**]{#struct_0_14687_18620_x841363953}[：允许数据包通过。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-atmclp-continue]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_x2143380393}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-atmclp-pass]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_699363853}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dot1p-continue]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_x1569680087}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dot1p-pass]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_x1004623827}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dscp-continue]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_x1535048896}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dscp-pass]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_1037625589}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-frde-continue]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_x1804218918}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-frde-pass]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_x841298417}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-lp-continue]{lang="EN-US"}**[ *new-lp*]{lang="EN-US"}]{#struct_0_14687_18620_x215501437}[：设置新的报文的]{lang="EN-US" style="font-family:宋体"}[lp]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-lp-pass]{lang="EN-US"}**[ *new-lp*]{lang="EN-US"}]{#struct_0_14687_18620_x28549662}[：设置新的报文的]{lang="EN-US" style="font-family:宋体"}[lp]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-mpls-exp-continue]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_1182150178}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-mpls-exp-pass]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_95975254}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-prec-continue]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_x980179034}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[IP]{lang="EN-US"}[优先级，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-prec-pass]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_371659817}[：设置新的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x664231456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令的重复执行将在接口上配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_x841495025}[CAR]{lang="EN-US"}[策略，策略的执行顺序与配置的先后顺序一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_596095871}[支持的动作与设备相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_438405174}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x279012118}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_775809744}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上对满足]{style="font-family:宋体"}[ANY]{lang="EN-US"}[规则的报文进行流量监管。报文正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，在第一时间可以有大于正常流量的突发流量通过，以后速率小于等于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时正常发送，大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，报文优先级改为]{style="font-family:宋体"}[0]{lang="EN-US"}[并发送。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1717707951}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos car outbound any cir 200 cbs 5000 ebs 0 green pass red remark-prec-pass 0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_741689367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos car]{lang="EN-US"}**]{#struct_0_14687_18620_x1486582057}**[ interface]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos ]{lang="EN-US"}**]{#struct_0_14687_18620_x841429489}**[carl]{lang="EN-US"}**
:::

::: {#-860906988 .myid}
[]{#_Toc404792360}[]{#struct_0_14687_18620_1965256944}[]{#_Toc384134594}[]{#_Toc373747492}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car percent (interface view)**

------------------------------------------------------------------------

[**[qos]{lang="EN-US"}**[ **car percent**]{lang="EN-US"}]{#struct_0_14687_18620_1964667121}[命令用来]{style="font-family:宋体"}[采用百分比的方式]{style="font-family:宋体"}[在接口上配置流量监管。]{style="font-family:宋体"}

[**[undo qos car]{lang="EN-US"}**]{#struct_0_14687_18620_x609451067}[命令用来取消接口上流量监管的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x347511294}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-numbe*r \| **carl** *carl-index* } **percent** **cir** *cir-percent* \[ **cbs** *cbs-time* \[ **ebs** *ebs-time* \] \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x1830320685}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-numbe*r \| **carl** *carl-index* } **percent** **cir** *cir-percent* \[ **cbs** *cbs-time* \] **pir** *pir-percent* \[ **ebs** *ebs-time* \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x1785501136}

[**[undo qos car]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-number* \| **carl** *carl-index* }]{lang="EN-US"}]{#struct_0_14687_18620_x494671364}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1502170674}

[[接口上没有配置百分比形式的流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_109086017}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1964732657}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_980368550}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_207784023}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1104750465}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_529671055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1514256307}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1714985565}[：对接口接收到的数据包进行流量监管。参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x199084630}[：对接口发送的数据包进行流量监管。参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_x1375602770}[：对所有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包进行流量监管。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}**[\[ **ipv6** \] *acl-number*]{lang="EN-US"}]{#struct_0_14687_18620_1964536049}[：对匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的数据包进行流量监管。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[；否则表示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[carl ]{lang="EN-US"}***[carl-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1370943801}[：对匹配]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的数据包进行限速。]{style="font-family:宋体"}*[carl-index]{lang="EN-US"}*[为承诺访问速率列表编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[percent]{lang="EN-US"}**[ **cir** *cir-percent*]{lang="EN-US"}]{#struct_0_14687_18620_758813964}[：以百分比的形式来指定承诺信息速率。取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *cbs-time*]{lang="EN-US"}]{#struct_0_14687_18620_x155374189}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[CBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *ebs-time*]{lang="EN-US"}]{#struct_0_14687_18620_924131268}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[EBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir ]{lang="EN-US"}***[pir-percent]{lang="EN-US"}*]{#struct_0_14687_18620_x2014938925}[：以百分比的形式来指定峰值速率，取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。峰值速率不能比承诺信息速率小。该参数的支持情况与设备的型号有关。]{style="font-family:宋体"}

[**[green ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_x60530802}[：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[red ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_698979830}[：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[yellow ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_x2109361138}[：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[action]{lang="EN-US"}*]{#struct_0_14687_18620_1964601585}[：对数据包采取的动作，有以下几种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[continue]{lang="EN-US"}**]{#struct_0_14687_18620_966379565}[：继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[discard]{lang="EN-US"}**]{#struct_0_14687_18620_354728084}[：丢弃数据包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[pass]{lang="EN-US"}**]{#struct_0_14687_18620_1490893581}[：允许数据包通过。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-atmclp-continue]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_690289116}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-atmclp-pass]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_798850054}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-dot1p-continue]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_978017613}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-dot1p-pass]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_558988945}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-dscp-continue]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_991507653}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-dscp-pass]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_1964929265}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-frde-continue]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_1423254122}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-frde-pass]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_x423992908}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-lp-continue]{lang="EN-US"}**[ *new-lp*]{lang="EN-US"}]{#struct_0_14687_18620_1509485299}[：设置新的报文的]{lang="EN-US" style="font-family:宋体"}[lp]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-lp-pass]{lang="EN-US"}**[ *new-lp*]{lang="EN-US"}]{#struct_0_14687_18620_x2032440715}[：设置新的报文的]{lang="EN-US" style="font-family:宋体"}[lp]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-mpls-exp-continue]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_x941352025}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-mpls-exp-pass]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_1964994801}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-prec-continue]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_244327697}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[IP]{lang="EN-US"}[优先级，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[remark-prec-pass]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_893090668}[：设置新的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1544796531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[该命令的重复执行将在接口上配置多个]{style="font-family:宋体"}]{#struct_0_14687_18620_464329535}[CAR]{lang="EN-US"}[策略，策略的执行顺序与配置的先后顺序一致。]{style="font-family:宋体"}

[]{#struct_0_14687_18620_1472450878}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CAR]{lang="EN-US"}]{#_Toc384134595}[支持的动作与设备相关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1900246994}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1629408128}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1608440253}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上对满足]{style="font-family:宋体"}[ANY]{lang="EN-US"}[规则的报文进行流量监管。]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CIR 50%]{lang="EN-US"}[，]{style="font-family:宋体"}[CBS 1000 ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1964798193}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos car outbound any percent cir 50 cbs 1000]{lang="EN-US"}
:::

::: {#-1567858224 .myid}
[]{#_Toc404792361}[]{#struct_0_14687_18620_x1105253248}[]{#_Toc345405313}[]{#_Toc198110073}[]{#_Toc391557792}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos car (user-profile view,session-group-profile view)**

------------------------------------------------------------------------

[**[qos]{lang="EN-US"}**[ **car**]{lang="EN-US"}]{#struct_0_14687_18620_1908162790}[命令用来在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[或]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[下]{style="font-family:宋体"}[配置流量监管。]{style="font-family:宋体"}

[**[undo qos car]{lang="EN-US"}**]{#struct_0_14687_18620_1166162574}[命令用来取消流量监管的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x831767322}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **any** **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_191857895}

[**[qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **any** **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \]]{lang="EN-US"}]{#struct_0_14687_18620_x231353695}

[**[undo qos car]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_x1923438249}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1837642413}

[[没有配置流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_x659153279}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1552116687}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_x946031325}[视图]{style="font-family:宋体"}[/Session Group Profile]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1140360455}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2088549386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_396917414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1062280603}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1524476914}[：对上线用户发送的报文进行限速。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_621118960}[：对上线用户接收到的报文进行限速。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_x1375660164}[：对所有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包进行限速。]{style="font-family:宋体"}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_x1105253247}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *committed-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x1271059259}[：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *excess-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x1867227029}[：过度突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0 byte]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x1114680890}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1331566834}

[[数据流量符合承诺速率时，允许数据包通过；数据流量不符合承诺速率时，丢弃数据包。]{style="font-family:宋体"}]{#struct_0_14687_18620_1291506423}

[[如果多次重复使用该命令，则最后一次配置生效。]{style="font-family:宋体"}]{#struct_0_14687_18620_57229630}

[[Session Group Profile]{lang="EN-US"}]{#struct_0_14687_18620_x1385463447}[视图应用]{style="font-family:宋体"}[CAR]{lang="EN-US"}[策略时，只支持]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[方向。]{style="font-family:宋体"}

[[不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_56068145}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1918328524}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_84912674}[对上线用户]{style="font-family:宋体"}[user]{lang="EN-US"}[接收的报文进行流量监管。报文正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，允许]{style="font-family:宋体"}[50000byte]{lang="EN-US"}[的突发流量通过，速率小于等于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时正常发送，大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，报文被丢弃。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1355005526}

[\[Sysname\] user-profile user]{lang="EN-US"}

[\[Sysname-user-profile-user\] qos car outbound any cir 200 cbs 50000]{lang="EN-US"}
:::

::: {#-1573708025 .myid}
[]{#_Toc404792362}[]{#struct_0_14687_18620_x1809044791}[]{#_Toc335120925}[]{#_Toc333831524}[]{#_Toc198110074}[]{#_Toc380516295}[]{#_Toc380516479}

**流量监管、流量整形和限速 \-- 流量监管配置命令 \-- qos carl**

------------------------------------------------------------------------

[**[qos carl]{lang="EN-US"}**]{#struct_0_14687_18620_x1899612788}[命令用来创建或修改]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[undo qos carl]{lang="EN-US"}**]{#struct_0_14687_18620_2063555070}[命令用来删除]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_408194678}

[**[qos carl]{lang="EN-US"}**[ *carl-index* { **dscp** *dscp-list* \| **mac** *mac-address* \| **mpls-exp** *mpls-exp-value* \| **precedence** *precedence-value* \| { **destination-ip-address** \| **source-ip-address** } { **range** *start-ip-address* **to** *end-ip-address* \| **subnet** *ip-address* *mask-length* } \[ **per-address** \[ **shared-bandwidth** \] \] }]{lang="EN-US"}]{#struct_0_14687_18620_1222789716}

[**[undo qos carl]{lang="EN-US"}**[ *carl-index*]{lang="EN-US"}]{#struct_0_14687_18620_26823923}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x876118501}

[[没有配置]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_x841101809}[列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1369343334}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1910722109}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_548791486}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1425328179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1686035496}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x384188815}

[*[carl-index]{lang="EN-US"}*]{#struct_0_14687_18620_289251216}[：]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表号码，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}***[ dscp-list]{lang="EN-US"}*]{#struct_0_14687_18620_x841036273}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[取值列表。]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[为区分服务编码点，用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{style="font-family:宋体"}[可以配置多个]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}***[ mac-address]{lang="EN-US"}*]{#struct_0_14687_18620_1360221381}[：]{style="font-family:宋体"}[16]{lang="EN-US"}[进制的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[mpls-exp]{lang="EN-US"}**[ *mpls-exp-value*]{lang="EN-US"}]{#struct_0_14687_18620_x1358968671}[：]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}[可以配置多个]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[值，系统默认为一个；多个不同的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[**[precedence]{lang="EN-US"}***[ precedence-value]{lang="EN-US"}*]{#struct_0_14687_18620_899458672}[：优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}[可以配置多个]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[值，最多可指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个；如果指定了多个相同的]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[值，系统默认为一个；多个不同的]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**[值是或的关系，即只要有一个值匹配，就算匹配这条规则。]{style="font-family:宋体"}

[**[destination-ip-address]{lang="EN-US"}**]{#struct_0_14687_18620_x551724247}[：基于目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[source-ip-address]{lang="EN-US"}**]{#struct_0_14687_18620_x1455873981}[：基于源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[**[range]{lang="EN-US"}***[ start-ip-address ]{lang="EN-US"}***[to]{lang="EN-US"}***[ end-ip-address]{lang="EN-US"}*]{#struct_0_14687_18620_x2128495934}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段起始地址和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段终止地址。]{style="font-family:宋体"}*[end-ip-address]{lang="EN-US"}*[必须大于]{style="font-family:宋体"}*[start-ip-addres]{lang="EN-US"}*[。]{style="font-family:宋体"}**[range]{lang="EN-US"}**[指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址数量上限与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[subnet]{lang="EN-US"}***[ ip-address mask-length]{lang="EN-US"}*]{#struct_0_14687_18620_x56871958}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[子网地址和]{style="font-family:宋体"}[IP]{lang="EN-US"}[子网地址掩码长度。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[per-address]{lang="EN-US"}**]{#struct_0_14687_18620_x841626100}[：表示对网段内逐]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址流量进行限速，]{style="font-family:宋体"}[cir]{lang="EN-US"}[为各]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址独享的限制带宽，不能被网段内其他]{style="font-family:宋体"}[IP]{lang="EN-US"}[流量共享。如果未指定本参数，将对整个网段的流量进行限速，]{style="font-family:宋体"}[cir]{lang="EN-US"}[为该网段内所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址带宽之和，各个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址带宽按照流量大小的比例进行分配。]{style="font-family:宋体"}

[**[shared-bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_x1367058962}[：表示网段内各]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的流量共享剩余带宽]{style="font-family:宋体"}[，]{style="font-family:宋体"}[cir]{lang="EN-US"}[为该网段内所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址共享带宽之和，根据当前存在流量的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址数量，动态平均分配各]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址占用的带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_14687_18620_x357625158}

[[可以选择基于优先级、基于]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_14687_18620_x1673286713}[地址、基于]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级、基于]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[或基于]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段建立]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表。]{style="font-family:宋体"}

[[对于不同的]{style="font-family:宋体"}*[carl-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1750835985}[，该命令的重复执行将创建多个]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表，对于同一个]{style="font-family:宋体"}*[carl-index]{lang="EN-US"}*[，该命令的重复执行将修改]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表的参数。]{style="font-family:宋体"}

[[指定单个]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x756803608}[地址限速请使用接口视图下]{style="font-family:宋体"}**[qos car acl]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[【举例】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_14687_18620_1910019387}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_630207834}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上应用]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[1]{lang="EN-US"}[是对源地址属于子网]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[内每台主机限速]{style="font-family:宋体"}[100kbps]{lang="EN-US"}[，网段内各]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的流量不共享剩余带宽。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x841560564}

[\[Sysname\] qos carl 1 source-ip-address subnet 1.1.1.0 24 per-address]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos car outbound carl 1 cir 100 cbs 6250 ebs 0 green pass red discard]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1349849393}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上应用]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}[CAR]{lang="EN-US"}[列表]{style="font-family:宋体"}[2]{lang="EN-US"}[是对源地址属于]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段]{style="font-family:宋体"}[1.1.2.100]{lang="EN-US"}[～]{style="font-family:宋体"}[1.1.2.199]{lang="EN-US"}[内所有]{style="font-family:宋体"}[主机]{style="font-family:宋体"}[限速]{style="font-family:宋体"}[5Mbps]{lang="EN-US"}[，网段内各]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的流量共享剩余带宽。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1860459592}

[\[Sysname\] qos carl 2 source-ip-address range 1.1.2.100 to 1.1.2.199 per-address shared-bandwidth]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos car outbound carl 2 cir 5000 cbs 3125 ebs 31250 green pass red discard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1247468782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos carl]{lang="EN-US"}**]{#struct_0_14687_18620_1893959339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos ]{lang="EN-US"}**]{#struct_0_14687_18620_x947831278}**[car]{lang="EN-US"}**
:::

::: {#1962938428 .myid}
[]{#_Toc404792364}[]{#struct_0_14687_18620_x841757172}[]{#_Toc312330754}[]{#_Toc306981585}[]{#_Toc263759952}[]{#_Toc226262619}[]{#_Toc198110076}[]{#_Toc117165490}

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- display qos gts interface**

------------------------------------------------------------------------

[**[display qos gts interface]{lang="EN-US"}**]{#struct_0_14687_18620_1363987049}[命令用来显示接口的流量整形配置情况和统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1212449510}

[**[display qos gts interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_76231901}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1764434782}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x753785413}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_630303651}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x266997860}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x841691636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1755544024}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_2034955332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2096971705}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_2091197582}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的流量整形配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x591871890}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x650137066}[显示所有接口的流量整形配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos gts interface]{lang="EN-US"}]{#struct_0_14687_18620_x841363956}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Rule: If-match acl 2001]{lang="EN-US"}

[  CIR 200 (kbps), CBS 50000 (Bytes), PIR 55000 (kbps), EBS 0 (Bytes)]{lang="EN-US"}

[  Queue Length: 100 (Packets)]{lang="EN-US"}

[  Queue Size: 70 (Packets)]{lang="EN-US"}

[  Passed   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[  Discarded: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[  Delayed  : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[ Rule: If-match acl 2001]{lang="EN-US"}

[  CIR 50 (%), CBS 600 (ms), EBS 0 (ms)]{lang="EN-US"}

[  Queue Length: 100 (Packets)]{lang="EN-US"}

[  Queue Size: 70 (Packets)]{lang="EN-US"}

[  Passed   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[  Discarded: 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[  Delayed  : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[[表3-2 ]{lang="EN-US"}[display qos gts]{lang="EN-US"}]{#struct_0_14687_18620_x2143577001}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1706325529}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x171810579}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1670447872}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x1277723768}

[[接口名，由接口类型和接口编号结合在一起组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x841298420}

[[Rule]{lang="EN-US"}]{#struct_0_14687_18620_x215435902}

[[匹配规则]{style="font-family:宋体"}]{#struct_0_14687_18620_1961439342}

[[CIR]{lang="EN-US"}]{#struct_0_14687_18620_99820295}

[[承诺信息速率，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_1534736480}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[%]{lang="EN-US"}

[[CBS]{lang="EN-US"}]{#struct_0_14687_18620_116337547}

[[承诺突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x841495028}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[EBS]{lang="EN-US"}]{#struct_0_14687_18620_595768191}

[[超出突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x1450860489}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[PIR]{lang="EN-US"}]{#struct_0_14687_18620_1110710595}

[[峰值速率，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_2116551869}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[%]{lang="EN-US"}

[[Queue Length]{lang="EN-US"}]{#struct_0_14687_18620_x841429492}

[[缓冲队列能够容纳的数据包的个数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1809372472}

[[Queue Size]{lang="EN-US"}]{#struct_0_14687_18620_x985897821}

[[当前缓冲区中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_1700635457}

[[Passed]{lang="EN-US"}]{#struct_0_14687_18620_x841101812}

[[已经通过的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1368753511}

[[Discarded]{lang="EN-US"}]{#struct_0_14687_18620_829403453}

[[被丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_547898529}

[[Delayed]{lang="EN-US"}]{#struct_0_14687_18620_x841036276}

[[被延迟发送的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1360417989}

[ ]{lang="EN-US"}

::: {#-1651688055 .myid}
[]{#_Toc404792365}[]{#struct_0_14687_18620_980779917}[]{#_Toc312330755}[]{#_Toc306981586}[]{#_Toc263759953}[]{#_Toc226262620}[]{#_Toc198110077}[]{#_Toc117165491}

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts (interface view)**

------------------------------------------------------------------------

[**[qos gts]{lang="EN-US"}**]{#struct_0_14687_18620_x1988535541}[命令用来在接口上配置流量整形。]{style="font-family:宋体"}

[**[undo qos gts]{lang="EN-US"}**]{#struct_0_14687_18620_893219593}[命令用来取消接口上流量整形的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1097721789}

[**[qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-id* } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1319378007}

[**[qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-id* } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_x231419230}

[**[undo qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-id* }]{lang="EN-US"}]{#struct_0_14687_18620_x841626099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_972051957}

[[接口上没有配置流量整形。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1106941228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1378213246}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_840238444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_977342532}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1488564221}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_777275705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841560563}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_1350177073}[：对所有的数据包进行流量整形。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}**[\[ **ipv6** \] *acl-number*]{lang="EN-US"}]{#struct_0_14687_18620_x2082933576}[：对匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的数据包进行流量整形。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[；否则表示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_631296891}**[：]{style="font-family:宋体"}**[对队列]{style="font-family:宋体"}[queue]{lang="EN-US"}[上的数据包进行流量整形，]{style="font-family:宋体"}*[queue-id]{lang="EN-US"}*[为匹配的队列号。]{style="font-family:宋体"}

[**[cir]{lang="EN-US"}**[ *committed-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_1840483614}[：承诺信息速率[，单位为]{#OLE_LINK7}]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}***[ committed-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_x178008394}[：承诺突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}***[ excess-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_x1591452486}[：超出突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x531834442}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}[PIR]{lang="EN-US"}[必须大于等于]{style="font-family:宋体"}[CIR]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[queue-length]{lang="EN-US"}**[ *queue-length*]{lang="EN-US"}]{#struct_0_14687_18620_x841757171}[：缓存队列的最大长度。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1198753842}

[[不配置峰值速率表示所配置的是单速桶流量整形，否则表示双速桶流量整形。]{style="font-family:宋体"}]{#struct_0_14687_18620_2127166079}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1363921513}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_457361217}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上对满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则]{style="font-family:宋体"}[2001]{lang="EN-US"}[的报文进行流量整形。正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[突发流量为]{style="font-family:宋体"}[50000bytes]{lang="EN-US"}[，以后速率小于等于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时正常发送，速率大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，将进入缓存队列，缓存队列长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x713094656}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos gts acl 2001 cir 200 cbs 50000 ebs 0 queue-length 100]{lang="EN-US"}
:::

::: {#-1815987909 .myid}
[]{#_Toc404792366}[]{#struct_0_14687_18620_1964667119}[]{#_Toc384134602}[]{#_Toc373747495}

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts percent (interface view)**

------------------------------------------------------------------------

[**[qos gts percent]{lang="EN-US"}**]{#struct_0_14687_18620_1964732655}[命令用来]{style="font-family:宋体"}[采用百分比的方式]{style="font-family:宋体"}[在接口上配置流量整形。]{style="font-family:宋体"}

[**[undo qos gts]{lang="EN-US"}**]{#struct_0_14687_18620_980499622}[命令用来取消接口上流量整形的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1288645647}

[**[qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-number* } **percent** **cir** *cir-percent* \[ **cbs** *cbs-time* \[ **ebs** *ebs-time* \] \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1423851981}

[**[qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-number* } **percent** **cir** *cir-percent* \[ **cbs** *cbs-time* \] **pir** *pir-percent* \[ **ebs** *ebs-time* \] \[ **queue-length** *queue-length* \]]{lang="EN-US"}]{#struct_0_14687_18620_x31178991}

[**[undo qos gts ]{lang="EN-US"}**[{ **any** \| **acl** \[ **ipv6** \] *acl-number* \| **queue** *queue-number* }]{lang="EN-US"}]{#struct_0_14687_18620_x776142082}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1964536047}

[[接口上没有配置百分比形式的流量整形。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1371337017}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1490597512}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1279013722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1852949963}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2071963932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x456418347}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1964601583}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_965986349}[：对所有的数据包进行流量整形。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}**[\[ **ipv6** \] *acl-number*]{lang="EN-US"}]{#struct_0_14687_18620_1599530440}[：对匹配]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的数据包进行流量整形。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[；否则表示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[queue ]{lang="EN-US"}***[queue-number]{lang="EN-US"}*]{#struct_0_14687_18620_x58763259}[：对队列]{style="font-family:宋体"}[queue]{lang="EN-US"}[上的数据包进行流量整形，]{style="font-family:宋体"}*[queue-number]{lang="EN-US"}*[为匹配的队列号。]{style="font-family:宋体"}

[**[percent]{lang="EN-US"}**[ **cir** *cir-percent*]{lang="EN-US"}]{#struct_0_14687_18620_x1166255106}[：以百分比的形式来指定承诺信息速率。取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *cbs-time*]{lang="EN-US"}]{#struct_0_14687_18620_1798456305}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[CBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *ebs-time*]{lang="EN-US"}]{#struct_0_14687_18620_x1407893154}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[EBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir ]{lang="EN-US"}***[pir-percent]{lang="EN-US"}*]{#struct_0_14687_18620_1964929263}[：以百分比的形式来指定峰值速率，取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。峰值速率不能比承诺信息速率小。该参数的支持情况与设备的型号有关。]{style="font-family:宋体"}

[**[queue-length]{lang="EN-US"}**[ *queue-length*]{lang="EN-US"}]{#struct_0_14687_18620_1423647338}[：缓存队列的最大长度。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1520072652}

[[不配置峰值速率表示所配置的是单速桶流量整形，否则表示双速桶流量整形。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1520072655}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1208238336}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x737946187}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上对所有的报文进行流量整形。]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[CIR 50%]{lang="EN-US"}[，]{style="font-family:宋体"}[CBS 1000 ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2084111927}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos gts any percent cir 50 cbs 1000]{lang="EN-US"}
:::

::: {#-205376142 .myid}
[]{#_Toc404792367}[]{#struct_0_14687_18620_468724866}[]{#_Toc391557799}

**流量监管、流量整形和限速 \-- 流量整形配置命令 \-- qos gts(user-profile view)**

------------------------------------------------------------------------

[**[qos gts]{lang="EN-US"}**]{#struct_0_14687_18620_1670168018}[命令用来在]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下配置流量整形。]{style="font-family:宋体"}

[**[undo qos gts]{lang="EN-US"}**]{#struct_0_14687_18620_x860450802}[命令用来取消]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[流量整形的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1866473796}

[**[qos gts cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] ]{lang="EN-US"}]{#struct_0_14687_18620_x1311133408}

[**[undo qos gts ]{lang="EN-US"}**]{#struct_0_14687_18620_1287929664}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_388646416}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_x627949086}[下没有配置流量整形。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x869459145}

[[User Profile]{lang="EN-US"}]{#struct_0_14687_18620_1320481035}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1531619320}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_468724867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1670168017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x859860978}

[**[cir]{lang="EN-US"}**[ *committed-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_2054025994}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}***[ committed-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_775147906}[：承诺突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}***[ excess-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_x2051065123}[：超出突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0 byte]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1923842163}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x672785388}[对上线用户接收的匹配队列]{style="font-family:宋体"}[7]{lang="EN-US"}[的报文进行流量整形。正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[突发流量为]{style="font-family:宋体"}[50000bytes]{lang="EN-US"}[，以后速率小于等于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时正常发送，速率大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，将进入缓存队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_2044682362}

[\[Sysname\] user-profile user]{lang="EN-US"}

[\[Sysname-user-profile-user\] qos gts cir 200 cbs 50000]{lang="EN-US"}
:::

::: {#-905589114 .myid}
[]{#_Toc404792369}[]{#struct_0_14687_18620_1356466971}[]{#_Toc312330757}[]{#_Toc307235756}

**流量监管、流量整形和限速 \-- 限速配置命令 \-- display qos lr**

------------------------------------------------------------------------

[**[display qos lr]{lang="EN-US"}**]{#struct_0_14687_18620_x2030016280}[命令用来显示接口或]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的限速配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841691635}

[**[display qos lr ]{lang="EN-US"}**[{ **interface** \[ *interface-type interface-number* \] \| **l2vpn-pw** \[ **peer** *ip-address* **pw-id** *pw-id* \] }]{lang="EN-US"}]{#struct_0_14687_18620_x1755609560}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_2045724625}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x973249332}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x268834713}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x908987341}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1582936172}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_139323792}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1431712376}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x841363955}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x2143773609}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的限速配置情况和运行统计信息。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_1501322758}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的限速配置情况和运行统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将]{style="font-family:宋体;
color:black"}[显示]{style="font-family:宋体"}[所有]{style="font-family:宋体;color:black"}[PW]{lang="EN-US"}[上的限速配置情况和运行统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_158284505}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x218581576}[显示所有接口的接口限速配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos lr interface]{lang="EN-US"}]{#struct_0_14687_18620_845372902}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Direction: Inbound]{lang="EN-US"}

[  CIR 2000 (kbps), CBS 20000 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[  Passed   : 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Discarded: 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Delayed  : 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Active shaping: No]{lang="EN-US"}

[Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[ Direction: Outbound]{lang="EN-US"}

[  CIR 50 (%), CBS 600 (ms), EBS 0 (ms)]{lang="EN-US"}

[  Passed   : 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Discarded: 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Delayed  : 1000 (Packets) 1000 (Bytes)]{lang="EN-US"}

[  Active shaping: No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1670168020}[显示所]{style="font-family:宋体"}[有]{style="font-family:
宋体"}[PW]{lang="EN-US"}[上]{style="font-family:宋体"}[的]{style="font-family:宋体"}[限速配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos lr l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_468724865}

[L2VPN-PW: peer 1.2.3.4, pw-id 1]{lang="EN-US"}

[  Direction: Outbound]{lang="EN-US"}

[   CIR 1024 (kbps), CBS 64000 (Bytes), EBS 0 (Bytes)]{lang="EN-US"}

[   Passed   : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Delayed  : 0 (Packets) 0 (Bytes)]{lang="EN-US"}

[   Active shaping: No]{lang="EN-US"}

[[表3-3 ]{lang="EN-US"}[display qos lr]{lang="EN-US"}]{#struct_0_14687_18620_x1419940142}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1699736249}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x841298419}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x215894653}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_1093576072}

[[接口名，由接口类型和接口编号结合在一起组成]{style="font-family:宋体"}]{#struct_0_14687_18620_1217216827}

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_468724870}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_x668484136}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_598470299}

[[方向，可以是]{style="font-family:宋体"}[Inbound]{lang="EN-US"}]{#struct_0_14687_18620_x841495027}[、]{style="font-family:宋体"}[Outbound]{lang="EN-US"}

[[CIR]{lang="EN-US"}]{#struct_0_14687_18620_596226943}

[[承诺信息速率，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_14687_18620_767824586}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[%]{lang="EN-US"}

[[CBS]{lang="EN-US"}]{#struct_0_14687_18620_2016311573}

[[承诺突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_1934459747}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[EBS]{lang="EN-US"}]{#struct_0_14687_18620_x841429491}

[[超出突发尺寸，当采用绝对值形式输入时，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}]{#struct_0_14687_18620_x1809569080}[；当采用百分比形式时，单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[ ]{lang="EN-US"}[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）]{style="font-family:宋体"}

[[Passed]{lang="EN-US"}]{#struct_0_14687_18620_x1370804842}

[[已经通过的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_x68611383}

[[Discarded]{lang="EN-US"}]{#struct_0_14687_18620_x1875324980}

[[被丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_x841101811}

[[Delayed]{lang="EN-US"}]{#struct_0_14687_18620_1368819047}

[[被延迟发送的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_2022318731}

[[Active shaping]{lang="EN-US"}]{#struct_0_14687_18620_1750584213}

[[当前限速配置是否被激活，]{style="font-family:宋体"}[Yes]{lang="EN-US"}]{#struct_0_14687_18620_x841036275}[表示激活，]{style="font-family:宋体"}[No]{lang="EN-US"}[表示未激活]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1104300420 .myid}
[]{#_Toc404792370}[]{#struct_0_14687_18620_1360614597}[]{#_Toc312330758}[]{#_Toc307235757}

**流量监管、流量整形和限速 \-- 限速配置命令 \-- qos lr**

------------------------------------------------------------------------

[**[qos lr]{lang="EN-US"}**]{#struct_0_14687_18620_x2147146243}[命令用来配置限速。]{style="font-family:宋体"}

[**[undo qos lr]{lang="EN-US"}**]{#struct_0_14687_18620_992629412}[命令用来取消配置的限速。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_292585276}

[**[qos lr ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_740954003}

[**[undo qos lr]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_1360005572}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_588683992}

[[没有配置限速。]{style="font-family:宋体"}]{#struct_0_14687_18620_724457845}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_398315146}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x1757813902}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI LDP PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_552292370}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_498958245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1722123937}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_611687316}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x210597163}[：]{style="font-family:宋体"}[对接收的数据流进行限速。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_724523381}[：]{style="font-family:宋体"}[对发送的数据流进行限速。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cir]{lang="EN-US"}**[ *committed-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_106804594}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}***[ committed-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_329751255}[：承诺突发尺寸，单位为]{style="font-family:宋体"}[bytes]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}***[ excess-burst-size]{lang="EN-US"}*]{#struct_0_14687_18620_490235735}[：超出突发尺寸，在双令牌桶算法中超出承诺突发流量的部分，单位为]{style="font-family:宋体"}[bytes]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x674014207}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1959777286}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上出方向的报文进行限速。正常流速为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[突发流量为]{style="font-family:宋体"}[50000bytes]{lang="EN-US"}[，以后速率小于等于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时正常发送，速率大于]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[时，将进行限速。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_724326773}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos lr outbound cir 200 cbs 50000]{lang="EN-US"}
:::

::: {#-823629305 .myid}
[]{#_Toc404792371}[]{#struct_0_14687_18620_1964798188}[]{#_Toc384134609}[]{#_Toc373747473}

**流量监管、流量整形和限速 \-- 限速配置命令 \-- qos lr percent**

------------------------------------------------------------------------

[**[qos lr percent]{lang="EN-US"}**]{#struct_0_14687_18620_1430040203}[命令用来]{style="font-family:宋体"}[采用百分比的方式]{style="font-family:宋体"}[在接口上配置接口限速。]{style="font-family:宋体"}

[**[undo qos lr]{lang="EN-US"}**]{#struct_0_14687_18620_x183167717}[命令用来取消接口上配置接口限速的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_487301689}

[**[qos lr ]{lang="EN-US"}**[{ **inbound** \| **outbound** } **percent cir** *cir-percent* \[ **cbs** *cbs-time* \[ **ebs** *ebs-time* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x871834705}

[**[undo qos lr]{lang="EN-US"}**[ { **inbound \| outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_797955439}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1964863724}

[[接口上没有配置百分比形式的限速。]{style="font-family:宋体"}]{#struct_0_14687_18620_1742450839}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1271808852}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1332637910}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1893065716}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1805601155}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1386337814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1965191404}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x568997816}[：限制接口上入方向报文的速率。本参数的支持情况与设备的型号有关。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1351265820}[：限制接口上出方向报文的速率。本参数的支持情况与设备的型号有关。]{style="font-family:宋体"}

[**[percent cir ]{lang="EN-US"}***[cir-percent]{lang="EN-US"}*]{#struct_0_14687_18620_x2111628802}[：以百分比的形式来指定承诺信息速率。取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *cbs-time*]{lang="EN-US"}]{#struct_0_14687_18620_x1913487389}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[CBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[CBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[cbs-time]{lang="EN-US"}*[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *ebs-time*]{lang="EN-US"}]{#struct_0_14687_18620_x1514733805}[：用指定的时间（单位为]{style="font-family:宋体"}[ms]{lang="EN-US"}[）来设置]{style="font-family:宋体"}[EBS]{lang="EN-US"}[，实际的]{style="font-family:宋体"}[EBS]{lang="EN-US"}[值是]{style="font-family:宋体"}*[ebs-time]{lang="EN-US"}*[乘以实际的承诺信息速率（]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[值乘以接口带宽）。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir ]{lang="EN-US"}***[pir-percent]{lang="EN-US"}*]{#struct_0_14687_18620_718179434}[：以百分比的形式来指定峰值速率，取值范围为]{style="font-family:宋体"}[1\~100]{lang="EN-US"}[。峰值速率不能比承诺信息速率小。不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。该参数的支持情况与设备的型号有关。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1365299313}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x877243539}[在接口]{style="font-family:宋体"}[GigabitEthernet 1/0/1]{lang="EN-US"}[上配置限制接口出方向的报文速率]{style="font-family:宋体"}[，指定]{style="font-family:宋体"}[CIR 50%]{lang="EN-US"}[，]{style="font-family:宋体"}[CBS 1000 ms]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1965256940}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos lr outbound percent cir 50 cbs 1000]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section5 style="layout-grid:15.85pt"}
:::

::: {#-239124752 .myid}
[]{#_Toc404792374}[]{#struct_0_14687_18620_x1126948164}[]{#_Toc375927584}

**拥塞管理 \-- 拥塞管理公共配置命令 \-- display qos queue interface**

------------------------------------------------------------------------

[**[display qos queue interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1539270201}[命令用来显示接口或]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[上队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x290832571}

[**[display qos queue interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x1487590276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1530232691}

[[任意]{style="font-family:宋体"}]{#struct_0_14687_18620_x588161560}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1359169281}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1049798225}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1794369615}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_488062811}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_190496350}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_649047592}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x858351497}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的接口队列配置情况和运行统计信息。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_x1404666474}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的先进先出队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2137480845}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x928839398}[显示所有接口下的队列信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue interface]{lang="EN-US"}]{#struct_0_14687_18620_x1487590275}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0]{lang="EN-US"}

[  Weight: IP Precedence]{lang="EN-US"}

[  Queues: Active/Max active/Total 0/0/128]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: GigabitEthernet1/0/2 ]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0 ]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0 ]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[[表4-1 ]{lang="EN-US"}[display qos queue interface]{lang="EN-US"}]{#struct_0_14687_18620_x1933517218}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1522680634}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x499822108}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1487590270}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x1487590269}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x1487590272}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_439135777}

[[当前出队列的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x1487590271}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_x1487590266}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x1487590265}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_86387838}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_1424915135}

[[FIFO queuing]{lang="EN-US"}]{#struct_0_14687_18620_86387839}

[[先进先出队列]{style="font-family:宋体"}]{#struct_0_14687_18620_86387836}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_86387837}

[[队列中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_1087208127}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_86387842}

[[队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_86387843}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_86387840}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x863947848}

[[Weighted Fair queuing]{lang="EN-US"}]{#struct_0_14687_18620_86387841}

[[加权公平队列]{style="font-family:宋体"}]{#struct_0_14687_18620_86387846}

[[Weight]{lang="EN-US"}]{#struct_0_14687_18620_86387847}

[[权重类型，分为两类：]{style="font-family:宋体"}[IP Precedence]{lang="EN-US"}]{#struct_0_14687_18620_x1869927298}[和]{style="font-family:宋体"}[DSCP]{lang="EN-US"}

[[Queues]{lang="EN-US"}]{#struct_0_14687_18620_423746923}

[[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1869927297}[队列的信息]{style="font-family:宋体"}

[[Active]{lang="EN-US"}]{#struct_0_14687_18620_x1869927300}

[[激活的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1869927299}[队列数目]{style="font-family:宋体"}

[[Max active]{lang="EN-US"}]{#struct_0_14687_18620_x1142337018}

[[最大激活过的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1869927294}[队列数目]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_14687_18620_x1869927293}

[[当前配置的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1869927296}[队列总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#33849701 .myid}
[]{#_Toc404792375}[]{#struct_0_14687_18620_x382822131}[]{#_Toc375927586}[]{#_Toc375553162}[]{#_Toc373826857}[]{#_Toc375927585}

**拥塞管理 \-- 拥塞管理公共配置命令 \-- display qos queue l2vpn-pw**

------------------------------------------------------------------------

[**[display qos queue l2vpn-pw]{lang="EN-US"}**]{#struct_0_14687_18620_x1199350727}[命令用来显示]{style="font-family:
宋体"}[PW]{lang="EN-US"}[上队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1988504902}

[**[display qos queue l2vpn-pw ]{lang="EN-US"}**[\[ **peer** *ip-address* **pw-id** *pw-id* \]]{lang="EN-US"}]{#struct_0_14687_18620_1299401019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1669012595}

[[任意]{style="font-family:宋体"}]{#struct_0_14687_18620_x1706088602}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_882932978}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2078906555}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1869927295}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1183261810}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x248976306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1389472239}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_x864684717}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的队列配置情况和统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将显示所有]{style="font-family:宋体;
color:black"}[PW]{lang="EN-US"}[上的队列配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_407565297}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1483732481}[显示]{style="font-family:宋体"}[PW]{lang="EN-US"}[下的]{style="font-family:宋体"}[所有队列。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_x1149743358}

[L2VPN-PW: peer 1.1.1.1, pw-id 1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0 ]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0 ]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[L2VPN-PW: peer 2.2.2.2 pw-id 2]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0]{lang="EN-US"}

[  Weight: IP Precedence]{lang="EN-US"}

[  Queues: Active/Max active/Total 0/0/128]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display qos queue l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_x604298586}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1517312975}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1869927290}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1869927289}

 

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_831597597}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_1748270507}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

 

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_831597596}

[[当前出队列的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_831597599}

 

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_831597598}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_1748270494}

 

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_831597601}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_831597600}

 

[[Weighted Fair queuing]{lang="EN-US"}]{#struct_0_14687_18620_831597603}

[[加权公平队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x1407579892}

 

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_831597602}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_831597605}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_831597604}

[[队列中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x1407579889}

 

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_x1124717539}

[[队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_x1124717540}

 

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_x1124717537}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x1124717538}

 

[[Weight]{lang="EN-US"}]{#struct_0_14687_18620_x877827378}

[[权重类型，分为两类：]{style="font-family:宋体"}[IP Precedence]{lang="EN-US"}]{#struct_0_14687_18620_x1124717535}[和]{style="font-family:宋体"}[DSCP]{lang="EN-US"}

 

[[Queues]{lang="EN-US"}]{#struct_0_14687_18620_x1124717536}

[[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1124717533}[队列的信息]{style="font-family:宋体"}

 

[[Active]{lang="EN-US"}]{#struct_0_14687_18620_1494825617}

[[激活的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1124717534}[队列数目]{style="font-family:宋体"}

 

[[Max active]{lang="EN-US"}]{#struct_0_14687_18620_x1124717531}

[[最大激活过的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1124717532}[队列数目]{style="font-family:宋体"}

 

[[Total]{lang="EN-US"}]{#struct_0_14687_18620_449260573}

[[当前配置的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_549954116}[队列总数]{style="font-family:宋体"}

 

[ ]{lang="EN-US"}

::: {#-933176059 .myid}
[]{#_Toc404792376}[]{#struct_0_14687_18620_150655861}[]{#_Toc375927587}[]{#_Toc375553166}[]{#_Toc373826861}

**拥塞管理 \-- 拥塞管理公共配置命令 \-- reset qos statistics l2vpn-pw**

------------------------------------------------------------------------

[**[reset qos statistics l2vpn-pw]{lang="EN-US"}**]{#struct_0_14687_18620_1269221405}[命令用来]{style="font-family:
宋体"}[清除]{style="font-family:宋体"}[PW]{lang="EN-US"}[下]{style="font-family:宋体"}[QoS]{lang="EN-US"}[的统计]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_449260572}

[**[reset qos statistics l2vpn-pw ]{lang="EN-US"}**[\[ **peer** *ip-address* **pw-id** *pw-id* \]]{lang="EN-US"}]{#struct_0_14687_18620_549954115}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1676293975}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_199812981}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x843432164}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1232939038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1769651152}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1279599400}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_1666186616}[：清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将]{style="font-family:宋体;
color:black"}[清除]{style="font-family:宋体"}[所有]{style="font-family:宋体;color:black"}[PW]{lang="EN-US"}[上的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x700575923}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_368195659}[清除]{style="font-family:宋体"}[QoS]{lang="EN-US"}[统计计数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset qos statistics l2vpn-pw peer 1.1.1.1 pw-id 1 ]{lang="EN-US"}]{#struct_0_14687_18620_431707925}
:::

::: {#-537655195 .myid}
[]{#_Toc318812698}[]{#_Toc327195798}[]{#_Toc325978425}[]{#_Toc291750008}[]{#_Toc263759959}[]{#_Toc226262626}[]{#_Toc198110135}[]{#_Toc117857744}[]{#_Toc81455542}[]{#_Toc56569601}[]{#_Toc404792378}[]{#struct_0_14687_18620_145853552}[]{#_Toc327195799}[]{#_Toc325978426}

**拥塞管理 \-- FIFO队列配置命令 \-- display qos queue fifo**

------------------------------------------------------------------------

[**[display qos queue fifo]{lang="EN-US"}**]{#struct_0_14687_18620_2118966629}[命令用来显示指定接口、指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[或所有接口及]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的先进先出队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1961156751}

[**[display qos queue fifo interface ]{lang="EN-US"}**[{]{lang="EN-US"}[ \[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \| **l2vpn-pw** \[ **peer** *ip-address* **pw-id** *pw-id* \] }]{lang="EN-US"}]{#struct_0_14687_18620_440078164}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_724392309}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1366210199}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1391154181}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x561566990}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1470309171}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x768105392}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_2086954942}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1641495568}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_724719989}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口的先进先出队列配置情况和统计信息。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_x96866618}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名，]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的先进先出队列配置情况和统计信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_449260575}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的先进先出队列配置情况和统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将显示所有]{style="font-family:宋体;
color:black"}[PW]{lang="EN-US"}[上的先进先出队列配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_635716525}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_288014375}[显示所有接口的先进先出队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue fifo interface]{lang="EN-US"}]{#struct_0_14687_18620_961476080}

[Interface: GigabitEthernet1/0/2 ]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0 ]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0 ]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_449260574}[显示所]{style="font-family:宋体"}[有]{style="font-family:宋体"}[PW]{lang="EN-US"}[下的]{style="font-family:宋体"}[先进先出队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue fifo l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_549954109}

[L2VPN-PW: peer 1.1.1.1, pw-id 1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - FIFO queuing: Size/Length/Discards 0/75/0]{lang="EN-US"}

[[表4-2 ]{lang="EN-US"}[display qos queue fifo]{lang="EN-US"}]{#struct_0_14687_18620_x653647125}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1694787193}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_860275339}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_724785525}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_345820554}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_2121127234}

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_449260577}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_449260576}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_1698935392}

[[当前出队列的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_1546433885}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_x767635778}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_724588917}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_792741068}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x100787858}

[[FIFO queuing]{lang="EN-US"}]{#struct_0_14687_18620_1590316883}

[[先进先出队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x1850326531}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_724654453}

[[队列中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_316430148}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_x1871200372}

[[队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_401975324}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_724982133}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_1706336240}

[ ]{lang="EN-US"}

::: {#-1017134508 .myid}
[]{#_Toc404792379}[]{#struct_0_14687_18620_1154354502}

**拥塞管理 \-- FIFO队列配置命令 \-- qos fifo queue-length**

------------------------------------------------------------------------

[**[qos fifo queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_1282495176}[命令用来]{style="font-family:宋体"}[配置先进先出队列的长度。]{style="font-family:宋体"}

[**[undo qos fifo queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_917814770}[命令用来]{style="font-family:
宋体"}[恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1252419081}

[**[qos fifo queue-length]{lang="EN-US"}***[ queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_x901129374}

[**[undo qos fifo queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_725047669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x294629636}

[[先进先出队列的长度为]{style="font-family:宋体"}[75]{lang="EN-US"}]{#struct_0_14687_18620_1007226097}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2094264999}

[[接口]{style="font-family:宋体"}]{#struct_0_14687_18620_970055373}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI LDP PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1560333524}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x719277635}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_339953300}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_724457846}

[*[queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_398315147}[：队列的长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1757813901}

[[若是子接口，则接口需要使能]{style="font-family:宋体"}[LR]{lang="EN-US"}]{#struct_0_14687_18620_2118376311}[功能以保证队列生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_763552054}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x205260019}[配置]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[队列的长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_627503295}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos fifo queue-length 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1613496139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue fifo interface]{lang="EN-US"}**]{#struct_0_14687_18620_724523382}[]{#_Toc318812699}
:::

::: {#1541572376 .myid}
[]{#_Toc404792381}[]{#struct_0_14687_18620_459778765}

**拥塞管理 \-- 优先级队列配置命令 \-- display qos queue pq interface**

------------------------------------------------------------------------

[**[display qos queue pq interface]{lang="EN-US"}**]{#struct_0_14687_18620_1671280814}[命令用来显示指定接口、指定]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[或所有接口及]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[上的优先级队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1285868215}

[**[display qos queue pq interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_623924779}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_189372812}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2131053706}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2137825529}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2134549090}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1579337487}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x641369950}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1524225414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1507297044}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_121537024}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[优先级队列配置情况和统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_x1982593724}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[优先级队列配置情况和统计信息]{style="font-family:宋体"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134614626}

[[若指定接口为]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}]{#struct_0_14687_18620_x1147259282}[接口，将显示继承该]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口的所有]{style="font-family:宋体"}[Virtual-Access]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[QoS PQ]{lang="EN-US"}[的信息，]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[本身无]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_428920634}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1040167957}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的优先级队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue pq interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_1795128671}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Priority queuing: PQL 1 Size/Length/Discards]{lang="EN-US"}

[Top:  0/20/0    Middle:  0/40/0    Normal:  0/60/0    Bottom:  0/80/0]{lang="EN-US"}

[[表4-3 ]{lang="EN-US"}[display qos queue pq interface]{lang="EN-US"}]{#struct_0_14687_18620_485864378}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x443143387}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_2134745698}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_2135335522}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_2135401058}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_2134811235}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_2134942307}

[[出队列信息]{style="font-family:宋体"}]{#struct_0_14687_18620_2135007843}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_2134549091}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2134680163}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_2134745699}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2135335523}

[[Priority queuing]{lang="EN-US"}]{#struct_0_14687_18620_2135401059}

[[优先级队列，指明使用的优先级队列列表]{style="font-family:宋体"}]{#struct_0_14687_18620_2134876772}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_2134942308}

[[队列中数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_2135007844}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_2134614628}

[[队列大小]{style="font-family:宋体"}]{#struct_0_14687_18620_2134680164}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_2134745700}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_2135335524}

[[Top]{lang="EN-US"}]{#struct_0_14687_18620_2134811237}

[[高优先级队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2134876773}

[[Middle]{lang="EN-US"}]{#struct_0_14687_18620_2134942309}

[[中优先级队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2134549093}

[[Normal]{lang="EN-US"}]{#struct_0_14687_18620_2134614629}

[[普通优先级队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2134680165}

[[Bottom]{lang="EN-US"}]{#struct_0_14687_18620_2135335525}

[[低优先级队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2135401061}

[ ]{lang="EN-US"}

::: {#17583483 .myid}
[]{#_Toc404792382}[]{#struct_0_14687_18620_x1142844287}

**拥塞管理 \-- 优先级队列配置命令 \-- display qos pql**

------------------------------------------------------------------------

[**[display qos pql]{lang="EN-US"}**]{#struct_0_14687_18620_x1326570425}[命令用来显示指定或者所有优先级队列列表的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1719041522}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_760189067}

[**[display qos pql]{lang="EN-US"}**[ \[ *pql-index* \]]{lang="EN-US"}]{#struct_0_14687_18620_2134811230}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_1979355898}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos pql]{lang="EN-US"}**[ \[ *pql-index* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x791309580}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_1565265000}[模式：]{style="font-family:宋体"}

[**[display qos pql]{lang="EN-US"}**[ \[ *pql-index* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_204380948}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x506638392}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1457285500}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134876766}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1945887134}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1243091828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_979679347}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_363075739}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1879724319}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_445338119}[：]{style="font-family:宋体"} [优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_2134942302}[：显示指定单板的优先级队列列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的优先级队列列表的内容。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x382668665}[：显示指定成员设备的优先级队列列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主用设备的优先级队列列表的内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1230532616}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的优先级队列列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的优先级队列列表的内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1190109270}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[优先级队列列表的内容]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示全局主用主控板的优先级队列列表的内容。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_351403439}[：]{style="font-family:宋体"}[显示指定单板的优先级队列列表的内容，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的优先级队列列表的内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x364495074}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x471701424}[显示优先列表。]{style="font-family:宋体"}

[[\<Sysname\> display qos pql]{lang="EN-US"}]{#struct_0_14687_18620_2135007838}

[Current PQL configuration:]{lang="EN-US"}

[List  Queue   Parameters]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[1     Top     Protocol ip less-than 1000]{lang="EN-US"}

[2     Normal  Length 80]{lang="EN-US"}

[2     Bottom  Length 40]{lang="EN-US"}

[3     Middle  Inbound-interface GigabitEthernet1/0/1]{lang="EN-US"}

[4     Top     Local-precedence  7]{lang="EN-US"}
:::

::: {#1104365984 .myid}
[]{#_Toc404792383}[]{#struct_0_14687_18620_459385548}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pq**

------------------------------------------------------------------------

[**[qos pq]{lang="EN-US"}**]{#struct_0_14687_18620_x60973046}[命令用来在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上应用优先级队列调度机制。]{style="font-family:宋体"}

[**[undo qos pq]{lang="EN-US"}**]{#struct_0_14687_18620_450425222}[命令用来将接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上的拥塞管理策略恢复到]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2046941712}

[**[qos pq pql]{lang="EN-US"}**[ *pql-index*]{lang="EN-US"}]{#struct_0_14687_18620_624666616}

[**[undo qos pq]{lang="EN-US"}**]{#struct_0_14687_18620_x1606719101}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134549086}

[[接口拥塞管理策略为]{style="font-family:宋体"}[FIFO]{lang="EN-US"}]{#struct_0_14687_18620_x1579730702}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1948725658}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x161880663}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1217912378}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1055995730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x457057054}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134614622}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1147521426}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x835539423}

[[对于同一个接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_14687_18620_685183663}[，若优先队列的应用命令的重复使用，则最新的配置生效。]{style="font-family:宋体"}

[[可以为优先列表的组配置多条分类规则，在进行流分类时，数据流按照顺序进行匹配，如果匹配上某规则，则进入相应的队列，匹配结束；如果数据包不与任何规则匹配，则进入缺省队列。]{style="font-family:宋体"}]{#struct_0_14687_18620_1898532085}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x245797156}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1244318311}[将第]{style="font-family:宋体"}[12]{lang="EN-US"}[组的优先列表应用到]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_2134680158}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos pq pql 12]{lang="EN-US"}
:::

::: {#-1771736173 .myid}
[]{#_Toc404792384}[]{#struct_0_14687_18620_x1171126047}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql default-queue**

------------------------------------------------------------------------

[**[qos pql default-queue]{lang="EN-US"}**]{#struct_0_14687_18620_459713919}[命令用来为]{style="font-family:宋体"}[未匹配任何规则的数据包指定一个缺省队列。]{style="font-family:宋体"}

[**[undo qos pql default-queue]{lang="EN-US"}**]{#struct_0_14687_18620_x1019926050}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_248090370}

[**[qos pql ]{lang="EN-US"}***[pql-index]{lang="EN-US"}***[ default-queue]{lang="EN-US"}**[ { **bottom** \| **middle** \| **normal** \| **top** }]{lang="EN-US"}]{#struct_0_14687_18620_182908173}

[**[undo qos pql]{lang="EN-US"}**[ *pql-index* **default-queue**]{lang="EN-US"}]{#struct_0_14687_18620_2134745694}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_415875435}

[[队列为]{style="font-family:宋体"}**[normal]{lang="EN-US"}**]{#struct_0_14687_18620_1002257930}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_117670394}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x254826171}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x558811288}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2017034631}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_2135335518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x750075665}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1926736539}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_x2086385076}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列，优先级依次降低。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1095103863}

[[进行流分类的时候，如果数据包不与任何规则匹配，则进入缺省队列。]{style="font-family:宋体"}]{#struct_0_14687_18620_x788923713}

[[对于同一个]{style="font-family:宋体"}*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1230557362}[，该命令重复使用操作，将设定新的缺省队列。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2135401054}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1142647680}[将优先列表中第]{style="font-family:宋体"}[12]{lang="EN-US"}[组中无对应规则的包的缺省队列设定为]{style="font-family:宋体"}[bottom]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x777468302}

[\[Sysname\] qos pql 12 default-queue bottom]{lang="EN-US"}
:::

::: {#2060772601 .myid}
[]{#_Toc404792385}[]{#struct_0_14687_18620_2059230630}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql inbound-interface**

------------------------------------------------------------------------

[**[qos pql inbound-interface]{lang="EN-US"}**]{#struct_0_14687_18620_1990596685}[命令用来配置基于接口的分类规则。]{style="font-family:
宋体"}

[**[undo qos pql inbound-interface]{lang="EN-US"}**]{#struct_0_14687_18620_x661241528}[命令用来删除相应的分类规则。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1402956486}

[**[qos pql ]{lang="EN-US"}***[pql-index]{lang="EN-US"}*[ **inbound-interface** *interface-type interface-number* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]{lang="EN-US"}]{#struct_0_14687_18620_2134811231}

[**[undo qos pql]{lang="EN-US"}**[ *pql-index* **inbound-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_14687_18620_1979290362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_445789515}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1620719716}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_157814611}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1939672952}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1175970231}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2134876767}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1945952670}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1595374710}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1722659681}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_1491815704}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列]{style="font-family:宋体"}[,]{lang="EN-US" style="font-family:宋体"}[优先级依次降低。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_685225334}

[[该命令按报文输入的接口进行匹配。对于同一个]{style="font-family:宋体"}*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x216946307}[，该命令可以重复使用，为来自不同接口的报文，建立不同的分类规则*。*]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134942303}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x382603129}[配置组号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的优先列表的分类规则，使得来自]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的报文进入]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1533333647}

[\[Sysname\] qos pql 12 inbound-interface gigabitethernet 1/0/1 queue middle]{lang="EN-US"}
:::

::: {#-153300695 .myid}
[]{#_Toc404792386}[]{#struct_0_14687_18620_x153515556}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql local-precedence**

------------------------------------------------------------------------

[**[qos pql local-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1303598232}[命令用来配置基于本地优先级的分类规则]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[undo qos pql local-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_728378092}[命令用来删除相应的规则]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x970629851}

[**[qos pql ]{lang="EN-US"}***[pql-index]{lang="EN-US"}*[ **local-pecedence** *local-precedence-list* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]{lang="EN-US"}]{#struct_0_14687_18620_2135007839}

[**[undo]{lang="EN-US"}**[ **qos pql** *pql-index* **local-precedence** *local-precedence-list*]{lang="EN-US"}]{#struct_0_14687_18620_459451084}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1818379216}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_x104516218}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_553900666}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_618076894}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2050378742}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2134549087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1579665166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2127028093}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_963507500}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[local-precedence-list]{lang="EN-US"}*]{#struct_0_14687_18620_620030875}[：要匹配的本地优先级的列表，最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}*[local-precedence]{lang="EN-US"}*[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_856533661}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列，优先级依次降低。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_2134614623}

[[该命令按报文的本地优先级进行匹配。对于同一个]{style="font-family:宋体"}*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1147586962}[，该命令可以重复使用，为不同本地优先级的报文，建立不同的分类规则*。*]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1913650684}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1821440789}[配置组号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的优先列表的分类规则，使得本地优先级等于]{style="font-family:宋体"}[3]{lang="EN-US"}[的报文进入]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1839801988}

[\[Sysname\] qos pql 12 local-precedence 3 queue middle]{lang="EN-US"}
:::

::: {#-479343190 .myid}
[]{#_Toc404792387}[]{#struct_0_14687_18620_x1901102895}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql protocol**

------------------------------------------------------------------------

[**[qos pql protocol]{lang="EN-US"}**]{#struct_0_14687_18620_x1266038918}[命令用来配置基于协议的分类规则。]{style="font-family:宋体"}

[**[undo qos pql protocol]{lang="EN-US"}**]{#struct_0_14687_18620_2134680159}[命令用来删除相应的分类规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1171060511}

[**[qos pql]{lang="EN-US"}**[ *pql-index* **protocol** { **ip** \| **ipv6** } \[ *queue-key key-value* \] **queue** { **bottom** \| **middle** \| **normal** \| **top** }]{lang="EN-US"}]{#struct_0_14687_18620_260683422}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[qos pql]{lang="EN-US"}**[ *pql-index* **protocol** { **ip** \| **ipv6** } \[ *queue-key key-value* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1754011542}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_837636073}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_x445755666}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1480766366}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_2134745695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_415940971}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1367687376}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x973175872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x683974712}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1282271303}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_2135335519}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列，优先级依次降低。]{style="font-family:宋体"}

[*[queue-key key-value]{lang="EN-US"}*]{#struct_0_14687_18620_x750141201}[：将]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文分类进入队列。]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[的取值见下表。当不输入]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[时，表示所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列。]{style="font-family:宋体"}

[[表4-4 ]{lang="EN-US"}[queue-key]{lang="EN-US"}]{#struct_0_14687_18620_731020650}[和]{style="font-family:黑体"}[key-value]{lang="EN-US"}[的取值]{style="font-family:黑体"}

[]{#table_struct_0_x413588943}[*[queue-key]{lang="EN-US"}*]{#struct_0_14687_18620_2135401055}
:::

[*[key-value]{lang="EN-US"}*]{#struct_0_14687_18620_x594072121}

[[说明]{style="font-family:黑体"}]{#struct_0_14687_18620_x593941049}

[[acl]{lang="EN-US"}]{#struct_0_14687_18620_x593875513}

[[access-list-number]{lang="EN-US"}]{#struct_0_14687_18620_x594334265}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符合某访问控制列表定义的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x594268729}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[fragments]{lang="EN-US"}]{#struct_0_14687_18620_x594137657}

[[-]{lang="EN-US"}]{#struct_0_14687_18620_x593547833}

[[分片的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x593482297}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[greater-than]{lang="EN-US"}]{#struct_0_14687_18620_x594006584}

[[长度值（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x593941048}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[长度大于某个计数值的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x593875512}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[less-than]{lang="EN-US"}]{#struct_0_14687_18620_x594268728}

[[长度值（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x594203192}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[长度小于某个计数值的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x594137656}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[tcp]{lang="EN-US"}]{#struct_0_14687_18620_x593482296}

[[端口号（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x594072119}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[源或目的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_14687_18620_x594006583}[端口号为指定的端口号的]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[udp]{lang="EN-US"}]{#struct_0_14687_18620_x593875511}

[[端口号（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x594334263}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[源或目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_14687_18620_x594268727}[端口号为指定的端口号的]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x594203191}

[[设备是以规则被配置的顺序来匹配数据包，如果发现数据包与某个规则匹配，便结束整个查找。]{style="font-family:宋体"}]{#struct_0_14687_18620_1800062890}

[[对于同一个]{style="font-family:宋体"}*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1541946027}[，该命令可以重复使用，为]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包建立多种分类规则。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*]{#struct_0_14687_18620_x5929202}[指定为]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[或]{style="font-family:宋体"}**[udp]{lang="EN-US"}**[时，]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[的值既可以直接使用端口名称，也可以使用相关端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x749451411}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1906407959}[配置组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的优先列表的分类规则，使满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}[为]{style="font-family:宋体"}[3100]{lang="EN-US"}[规则定义的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进入]{style="font-family:宋体"}[top]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x594137655}

[\[Sysname\] qos pql 5 protocal ip acl 3100 queue top]{lang="EN-US"}

::: {#-812308301 .myid}
[]{#_Toc404792388}[]{#struct_0_14687_18620_x2128045513}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql protocol mpls exp**

------------------------------------------------------------------------

[**[qos pql protocol mpls exp]{lang="EN-US"}**]{#struct_0_14687_18620_1416975102}[命令用来配置基于]{style="font-family:
宋体"}[MPLS EXP]{lang="EN-US"}[优先级的分类规则。]{style="font-family:
宋体"}

[**[undo qos pql protocol mpls exp]{lang="EN-US"}**]{#struct_0_14687_18620_x1081056817}[命令用来删除相应的分类规则。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1165445760}

[**[qos pql ]{lang="EN-US"}***[pql-index]{lang="EN-US"}*[ **protocol mpls exp** *exp-list* **queue** { **bottom** \| **middle** \| **normal** \| **top** }]{lang="EN-US"}]{#struct_0_14687_18620_x723412403}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[qos]{lang="EN-US"}**[ **pql** *pql-index* **protocol** **mpls** exp *exp-list*]{lang="EN-US"}]{#struct_0_14687_18620_1506929293}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x593547831}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_782539425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x933410926}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2051939691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_164412623}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x577337323}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x593482295}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1994638089}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x822948430}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[exp-list]{lang="EN-US"}*]{#struct_0_14687_18620_x479549804}[：要匹配的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的报文列表，最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}*[exp]{lang="EN-US"}*[，]{style="font-family:宋体"}*[exp]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_264628461}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列，优先级依次降低。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1934007131}

[[该命令按报文的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}]{#struct_0_14687_18620_1014012528}[优先级进行匹配，对于同一个]{style="font-family:宋体"}*[pql-index]{lang="EN-US"}*[，该命令可以重复使用，为不同]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的报文建立不同的分类规则]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x594072118}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_240008203}[配置组号为]{style="font-family:宋体"}[12]{lang="EN-US"}[的优先列表的分类规则，将]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[的报文进入]{style="font-family:
宋体"}[top]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2014171594}

[\[Sysname\] qos pql 5 protocal mpls exp 2 4 queue top]{lang="EN-US"}
:::

::: {#599567608 .myid}
[]{#_Toc404792389}[]{#struct_0_14687_18620_376876979}

**拥塞管理 \-- 优先级队列配置命令 \-- qos pql queue**

------------------------------------------------------------------------

[**[qos pql queue ]{lang="EN-US"}**]{#struct_0_14687_18620_x1375790298}[命令用来设置各队列的长度（所容纳的数据包个数）。]{style="font-family:宋体"}

[**[undo qos pql queue]{lang="EN-US"}**]{#struct_0_14687_18620_x967140749}[命令用来恢复队列长度的缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1282875581}

[**[qos pql]{lang="EN-US"}**[ *pql-index* **queue** { **bottom** \| **middle** \| **normal** \| **top** } **queue-length** *queue-length*]{lang="EN-US"}]{#struct_0_14687_18620_x594006582}

[**[undo qos pql]{lang="EN-US"}**[ *cql-index* **queue** { **bottom** \| **middle** \| **normal** \| **top** } **queue-length**]{lang="EN-US"}]{#struct_0_14687_18620_x970912146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x593892330}

[[高优先队列的缺省长度值为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_14687_18620_x36094603}[，]{style="font-family:宋体"}[中优先队列的缺省长度值为]{style="font-family:宋体"}[40]{lang="EN-US"}[，]{style="font-family:宋体"}[正常优先队列的缺省长度值为]{style="font-family:宋体"}[60]{lang="EN-US"}[，]{style="font-family:宋体"}[低优先队列的缺省长度值为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1748950346}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1596342962}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x593941046}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1149153770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x304361697}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1541642843}

[*[pql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1134571400}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[top]{lang="EN-US"}**]{#struct_0_14687_18620_x1172922403}[、]{style="font-family:宋体"}**[middle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bottom]{lang="EN-US"}**[：对应]{style="font-family:宋体"}[PQ]{lang="EN-US"}[的四个队列，优先级依次降低。]{style="font-family:宋体"}

[**[queue-length]{lang="EN-US"}***[ queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_x593875510}[：队列的最大长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1898611834}

[[如果队列的长度达到最大值时，后面收到的属于该队列的数据包将被丢弃。]{style="font-family:宋体"}]{#struct_0_14687_18620_x278797363}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x428324441}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1488465551}[配置优先列表第]{style="font-family:宋体"}[5]{lang="EN-US"}[组]{style="font-family:宋体"}[top]{lang="EN-US"}[队列的长度为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1167506928}

[\[Sysname\] qos pql 5 queue top queue-length 10]{lang="EN-US"}
:::

::: {#-320322937 .myid}
[]{#_Toc404792391}[]{#struct_0_14687_18620_999159881}

**拥塞管理 \-- 定制队列配置命令 \-- display qos queue cq interface**

------------------------------------------------------------------------

[**[display qos queue cq interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1779838629}[命令用来显示指定接口、指定]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[或所有接口及]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[上的定制队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_789268168}

[**[display qos queue cq interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_985188702}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x428534938}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x594268726}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1435664552}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1910129256}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1706609336}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1584982617}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1244695827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1862474303}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x594203190}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[定制队列配置情况和统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_1799997354}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[定制队列配置情况和统计信息]{style="font-family:宋体"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1348979747}

[[若指定接口为]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}]{#struct_0_14687_18620_x81109978}[接口，将显示继承该]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口的所有]{style="font-family:宋体"}[Virtual-Access]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[QoS CQ]{lang="EN-US"}[的信息，]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[本身无]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1261896174}

[[\#]{lang="EN-US"}]{#struct_0_14687_18620_379522667}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的定制队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\>display qos queue cq interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_x594137654}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Custom queuing: CQL 1 Size/Length/Discards]{lang="EN-US"}

[ 1:   0/  20/0          2:   0/  20/0          3:   0/  20/0]{lang="EN-US"}

[ 4:   0/  20/0          5:   0/  20/0          6:   0/  20/0]{lang="EN-US"}

[ 7:   0/  20/0          8:   0/  20/0          9:   0/  20/0]{lang="EN-US"}

[10:   0/  20/0         11:   0/  20/0         12:   0/  20/0]{lang="EN-US"}

[13:   0/  20/0         14:   0/  20/0         15:   0/  20/0]{lang="EN-US"}

[16:   0/  20/0]{lang="EN-US"}

[[表4-5 ]{lang="EN-US"}[display qos queue cq interface]{lang="EN-US"}]{#struct_0_14687_18620_x2127979977}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x101128513}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x593547830}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x594072125}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x594006589}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x593941053}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_x594334269}

[[出队列信息]{style="font-family:宋体"}]{#struct_0_14687_18620_x594268733}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_x594203197}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x593547837}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_x593482301}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x594072124}

[[Custom queuing]{lang="EN-US"}]{#struct_0_14687_18620_x593941052}

[[定制队列，指明使用的定制队列列表]{style="font-family:宋体"}]{#struct_0_14687_18620_x593875516}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_x594334268}

[[队列中数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x594203196}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_x594137660}

[[队列大小]{style="font-family:宋体"}]{#struct_0_14687_18620_x593547836}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_x593482300}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x997291112}

[ ]{lang="EN-US"}

::: {#17583470 .myid}
[]{#_Toc404792392}[]{#struct_0_14687_18620_137670887}

**拥塞管理 \-- 定制队列配置命令 \-- display qos cql**

------------------------------------------------------------------------

[**[display qos cql]{lang="EN-US"}**]{#struct_0_14687_18620_x1526362155}[命令用来显示指定或所有定制队列列表的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x526043352}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_1806523969}

[**[display qos cql]{lang="EN-US"}**[ \[ *cql-index* \]]{lang="EN-US"}]{#struct_0_14687_18620_x997225576}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_1683325773}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos cql]{lang="EN-US"}**[ \[ *cql-index* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_1439678108}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_395491761}[模式：]{style="font-family:宋体"}

[**[display qos cql]{lang="EN-US"}**[ \[ *cql-index* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x523900116}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1684668859}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_242930260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997160040}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_886449566}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_803058674}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_484590885}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x465055139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1931319448}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_852382140}[：优先列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。如果未指定本参数，则显示所有列表的内容。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x997618792}[：显示指定单板的定制列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示主用主控板的定制列表的内容。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1346011542}[：显示指定成员设备的定制列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示主用设备的类的定制列表的内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x335682397}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的定制列表的内容，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的定制列表的内容。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_871479413}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[定制列表的内容]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。]{style="font-family:宋体"}[如果未指定本参数，将显示全局主用主控板的定制列表的内容。]{style="font-family:宋体"}[（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1901766338}[：]{style="font-family:宋体"}[显示指定单板的定制列表的内容，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的定制列表的内容。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1037365525}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1812607431}[显示所有定制列表的内容。]{style="font-family:宋体"}

[[\<Sysname\> display qos cql]{lang="EN-US"}]{#struct_0_14687_18620_x997553256}

[Current CQL configuration:]{lang="EN-US"}

[List  Queue  Parameters]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[2     3      Protocol ip fragments]{lang="EN-US"}

[3     6      Length 100]{lang="EN-US"}

[3     1      Inbound-interface GigabitEthernet1/0/1]{lang="EN-US"}

[4     5      Local-precedence 7]{lang="EN-US"}
:::

::: {#1104365971 .myid}
[]{#_Toc404792393}[]{#struct_0_14687_18620_907069498}

**拥塞管理 \-- 定制队列配置命令 \-- qos cq**

------------------------------------------------------------------------

[**[qos cq]{lang="EN-US"}**]{#struct_0_14687_18620_x1266801455}[命令用来在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上应用定制队列。]{style="font-family:宋体"}

[**[undo qos cq]{lang="EN-US"}**]{#struct_0_14687_18620_x1324783311}[命令用来将接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上的拥塞管理策略恢复到]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_387064952}

[**[qos cq cql ]{lang="EN-US"}***[cql-index]{lang="EN-US"}*[ ]{lang="EN-US"}]{#struct_0_14687_18620_x1109650602}

[**[undo qos cq]{lang="EN-US"}**]{#struct_0_14687_18620_x1010053260}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997487720}

[[接口拥塞管理策略为]{style="font-family:宋体"}[FIFO]{lang="EN-US"}]{#struct_0_14687_18620_151296706}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1025214306}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x374009460}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2069096486}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x797703451}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x997422184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1688354039}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1018776061}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1\~16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x987173376}

[[对于同一个接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_14687_18620_x1568682041}[，若定制队列的应用命令的重复使用，则最新的配置生效。]{style="font-family:宋体"}

[[可以为定制列表的组配置多条分类规则，在进行流分类时，数据流按照顺序进行匹配，如果匹配上某规则，则进入相应的队列，匹配结束；如果数据包不与任何规则匹配，则进入缺省队列。]{style="font-family:宋体"}]{#struct_0_14687_18620_1860550422}

[[若是]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_14687_18620_x1663806681}[接口、子接口、三层聚合接口、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[捆绑接口、]{style="font-family:宋体"}[RPR]{lang="EN-US"}[逻辑接口，或是封装了]{style="font-family:宋体"}[PPPoE]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoEoA]{lang="EN-US"}[、]{style="font-family:宋体"}[PPPoFR]{lang="EN-US"}[、]{style="font-family:宋体"}[MPoFR]{lang="EN-US"}[（]{style="font-family:宋体"}[FR]{lang="EN-US"}[接口未使能帧中继流量整形功能）协议的]{style="font-family:宋体"}[VT]{lang="EN-US"}[、]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[接口，则接口需要使能]{style="font-family:宋体"}[LR]{lang="EN-US"}[功能以保证队列生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x996832360}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1671314801}[将第]{style="font-family:宋体"}[5]{lang="EN-US"}[组的定制列表应用到]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1061619605}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos cq cql 5]{lang="EN-US"}
:::

::: {#-1787807860 .myid}
[]{#_Toc404792394}[]{#struct_0_14687_18620_1379672909}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql default-queue**

------------------------------------------------------------------------

[**[qos cql default-queue]{lang="EN-US"}**]{#struct_0_14687_18620_2095324667}[命令用来为未匹配任何规则的数据包指定一个缺省队列。]{style="font-family:宋体"}

[**[undo qos cql default-queue]{lang="EN-US"}**]{#struct_0_14687_18620_x489021965}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x996766824}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **default-queue** *queue-id*]{lang="EN-US"}]{#struct_0_14687_18620_x263843968}

[**[undo]{lang="EN-US"}**[ **qos** **cql** *cql-index* **default-queue**]{lang="EN-US"}]{#struct_0_14687_18620_x467828841}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1078164716}

[[队列号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_14687_18620_522127189}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1007720384}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1683151999}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997356647}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_901844734}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1756588320}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1264777134}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_2078830140}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x649713790}[：队列号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x509829924}

[[在进行流分类的时候，如果数据包不与任何规则匹配，则进入缺省队列。]{style="font-family:宋体"}]{#struct_0_14687_18620_x997291111}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_137474279}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x311091755}[指定定制列表第]{style="font-family:宋体"}[5]{lang="EN-US"}[组的缺省队列为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_13196569}

[\[Sysname\] qos cql 5 default-queue 2]{lang="EN-US"}
:::

::: {#836885000 .myid}
[]{#_Toc404792395}[]{#struct_0_14687_18620_x1410474340}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql inbound-interface**

------------------------------------------------------------------------

[**[qos cql inbound-interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1944798731}[命令用来建立基于接口的分类规则。]{style="font-family:宋体"}

[**[undo qos cql inbound-interface]{lang="EN-US"}**]{#struct_0_14687_18620_x997225575}[命令用来删除相应的分类规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1683260237}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **inbound-interface** *interface-type interface-number* **queue** *queue-id*]{lang="EN-US"}]{#struct_0_14687_18620_x2031913038}

[**[undo qos cql]{lang="EN-US"}**[ *cql-index* **inbound-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_14687_18620_x812486237}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1210729516}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_x899975176}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1048214442}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x997160039}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_887039393}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x327171191}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_795178345}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_922594546}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1505228034}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x997618791}[：指定的接口类型和接口编号]{style="font-family:宋体"}*[。]{style="font-family:黑体;
color:#0096d6"}*

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1345814934}[：队列号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2048298909}

[[该命令按报文输入的接口进行匹配。对于同一个]{style="font-family:宋体"}*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_912186740}[，该命令可以重复使用，为来自不同接口的报文，建立不同的分类规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_540401109}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1862432888}[配置组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的定制列表的分类规则，将来自]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的报文进入队列]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x997553255}

[\[Sysname\] qos cql 5 **inbound-interface** gigabitethernet 1/0/1 **queue 3**]{lang="EN-US"}
:::

::: {#-172877800 .myid}
[]{#_Toc404792396}[]{#struct_0_14687_18620_906872890}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql local-precedence**

------------------------------------------------------------------------

[**[qos cql local-precedence]{lang="EN-US" style="color:windowtext"}**]{#struct_0_14687_18620_x781661029}[命令用来建立基于本地优先级的分类规则]{style="font-family:宋体;color:windowtext"}[。]{style="font-family:黑体"}

[**[undo qos cql local-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_568965572}[命令用来删除相应的规则]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1812180536}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **local-precedence** *local-precedence-list* **queue** *queue-id*]{lang="EN-US"}]{#struct_0_14687_18620_x1181809403}

[**[undo]{lang="EN-US"}**[ **qos cql** *cql-index* **local-precedence** *local-precedence-list*]{lang="EN-US"}]{#struct_0_14687_18620_x953863668}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997487719}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_150837951}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_732511614}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_927478017}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1672392011}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1909802762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x997422183}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1688812791}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1286107844}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[local-precedence-list]{lang="EN-US"}*]{#struct_0_14687_18620_527227687}[：要匹配的本地优先级的列表，最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}*[local-precedence]{lang="EN-US"}*[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1990320096}[：定制队列的队列号，取值范围为]{style="font-family:宋体"}[1\~16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x692365111}

[[该命令按报文的本地优先级进行匹配。对于同一个]{style="font-family:宋体"}*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_805602227}[，该命令可以重复使用，为不同本地优先级的报文建立不同的分类规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x996832359}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1671773550}[配置组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的定制列表的分类规则，将本地优先级等于]{style="font-family:宋体"}[4]{lang="EN-US"}[的报文进入队列]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x96163525}

[\[Sysname\] qos cql 5 local-precedence 4 queue 3]{lang="EN-US"}
:::

::: {#-479362633 .myid}
[]{#_Toc404792397}[]{#struct_0_14687_18620_824404112}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql protocol**

------------------------------------------------------------------------

[**[qos cql protocol]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14687_18620_43504120}[命令用来配置基于协议的分类规则。]{style="font-family:
宋体"}

[**[undo qos cql protocol]{lang="EN-US"}**]{#struct_0_14687_18620_x1382143105}[命令用来删除相应的分类规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x928958588}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **protocol** { **ip** \| **ipv6** } \[ *queue-key key-value* \] **queue** *queue-id*]{lang="EN-US"}]{#struct_0_14687_18620_x996766823}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[qos cql]{lang="EN-US"}**[ *cql-index* **protocol** { **ip** \| **ipv6** } \[ *queue-key key-value* \]]{lang="EN-US"}]{#struct_0_14687_18620_x263909504}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_315552108}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1424054191}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_654589800}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_47828016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997356646}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_901910270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x942982696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2084362106}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x517344538}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1080992964}[：队列号，取值范围为]{style="font-family:宋体"}[1\~16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-key key-value]{lang="EN-US"}*]{#struct_0_14687_18620_1635683607}[：]{style="font-family:黑体;
color:#0096d6"}[将]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文分类进入队列。]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[的取值见下表。当不输入]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*[和]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[时，表示所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列。]{style="font-family:宋体"}

[[表4-6 ]{lang="EN-US"}[queue-key]{lang="EN-US"}]{#struct_0_14687_18620_x997291110}[和]{style="font-family:黑体"}[key-value]{lang="EN-US"}[的取值]{style="font-family:黑体"}

[]{#table_struct_0_x93121789}[*[queue-key]{lang="EN-US"}*]{#struct_0_14687_18620_x997225574}
:::

[*[key-value]{lang="EN-US"}*]{#struct_0_14687_18620_x997160038}

[[说明]{style="font-family:黑体"}]{#struct_0_14687_18620_x997618790}

[[acl]{lang="EN-US"}]{#struct_0_14687_18620_x997487718}

[[access-list-number]{lang="EN-US"}]{#struct_0_14687_18620_x997422182}[（]{style="font-family:宋体"}[2000]{lang="EN-US"}[\~]{lang="EN-US" style="font-family:Symbol"}[3999]{lang="EN-US"}[）]{style="font-family:宋体"}

[[符合某访问控制列表定义的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x996766822}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文就进入队列]{style="font-family:宋体"}

[[fragments]{lang="EN-US"}]{#struct_0_14687_18620_x997356645}

[[-]{lang="EN-US"}]{#struct_0_14687_18620_x997291109}

[[只要是分片的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x997225573}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文就进入队列]{style="font-family:宋体"}

[[greater-than]{lang="EN-US"}]{#struct_0_14687_18620_x997618789}

[[长度值（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x997553253}[\~]{lang="EN-US" style="font-family:Symbol"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[长度大于指定长度值的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x997487717}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[less-than]{lang="EN-US"}]{#struct_0_14687_18620_x996832357}

[[长度值（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x996766821}[\~]{lang="EN-US" style="font-family:Symbol"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[长度小于指定长度值的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x997356652}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[tcp]{lang="EN-US"}]{#struct_0_14687_18620_x997225580}

[[端口号（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x997160044}[\~]{lang="EN-US" style="font-family:Symbol"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[源或目的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_14687_18620_x997618796}[端口号为指定的端口号的]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[[udp]{lang="EN-US"}]{#struct_0_14687_18620_x997487724}

[[端口号（]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14687_18620_x997422188}[\~]{lang="EN-US" style="font-family:Symbol"}[65535]{lang="EN-US"}[）]{style="font-family:宋体"}

[[源或目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_14687_18620_x996832364}[端口号为指定的端口号的]{style="font-family:宋体"}[IP]{lang="EN-US"}[或者]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x996766828}

[[系统是以规则被配置的顺序来匹配数据包，如果发现数据包与某个规则匹配，便结束整个查找。]{style="font-family:宋体"}]{#struct_0_14687_18620_x263581824}

[[对于同一个]{style="font-family:宋体"}*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_699110846}[，该命令可以重复使用，为]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包建立多种分类规则。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}*[queue-key]{lang="EN-US"}*]{#struct_0_14687_18620_x1030318607}[指定为]{style="font-family:宋体"}[tcp]{lang="EN-US"}[或]{style="font-family:宋体"}[udp]{lang="EN-US"}[时，]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[的值既可以直接使用端口名称，也可以使用相关端口号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1308457631}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_460800164}[配置组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的定制列表的分类规则，将匹配访问控制列表]{style="font-family:宋体"}[3100]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进入队列]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x997356651}

[\[Sysname\] qos cql 5 protocol ip acl 3100 queue 3]{lang="EN-US"}

::: {#-2082043299 .myid}
[]{#_Toc404792398}[]{#struct_0_14687_18620_901975807}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql protocol mpls exp**

------------------------------------------------------------------------

[**[qos cql protocol mpls exp]{lang="EN-US"}**]{#struct_0_14687_18620_x1004419157}[命令用来配置基于]{style="font-family:
宋体"}[MPLS EXP]{lang="EN-US"}[优先级的分类规则。]{style="font-family:
宋体"}

[**[undo qos cql protocol mpls exp]{lang="EN-US"}**]{#struct_0_14687_18620_x1798404538}[命令用来删除相应的分类规则**。**]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1090006775}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **protocol mpls exp** *exp-list* **queue** *queue-id*]{lang="EN-US"}]{#struct_0_14687_18620_1372406248}

[**[undo qos cql]{lang="EN-US"}**[ *cql-index* **protocol mpls exp** *exp-list*]{lang="EN-US"}]{#struct_0_14687_18620_x597954527}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997291115}

[[没有配置任何分类规则。]{style="font-family:宋体"}]{#struct_0_14687_18620_137736423}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1204156519}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1752618382}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1400583762}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1702519226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1699095897}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997225579}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_1684046669}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[exp-list]{lang="EN-US"}*]{#struct_0_14687_18620_x625647443}[：要匹配的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的报文列表，最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}*[exp]{lang="EN-US"}*[，]{style="font-family:宋体"}*[exp]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1891922686}[：队列号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1752304142}

[[该命令按报文的]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}]{#struct_0_14687_18620_1470115966}[优先级进行匹配，对于同一个]{style="font-family:宋体"}*[cql-index]{lang="EN-US"}*[，该命令可以重复使用，为不同]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级的报文建立不同的分类规则]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997160043}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_886646174}[配置组号为]{style="font-family:宋体"}[5]{lang="EN-US"}[的定制列表的分类规则，将]{style="font-family:宋体"}[MPLS EXP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[的报文进入队列]{style="font-family:
宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1816125832}

[\[Sysname\] qos cql 5 protocol mpls exp 2 4 queue 3]{lang="EN-US"}
:::

::: {#599548099 .myid}
[]{#_Toc404792399}[]{#struct_0_14687_18620_120480470}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql queue**

------------------------------------------------------------------------

[**[qos cql queue ]{lang="EN-US"}**]{#struct_0_14687_18620_595850574}[命令用来设置各队列的长度（所容纳的数据包个数）**。**]{style="font-family:宋体"}

[**[undo qos cql queue]{lang="EN-US"}**]{#struct_0_14687_18620_x1978741393}[命令用来恢复队列长度的缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997618795}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **queue** *queue-id* **queue-length** *queue-length*]{lang="EN-US"}]{#struct_0_14687_18620_1346077078}

[**[undo qos cql ]{lang="EN-US"}***[cql-index]{lang="EN-US"}*[ **queue** *queue-id* **queue-length**]{lang="EN-US"}]{#struct_0_14687_18620_x1421345580}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x623993971}

[[队列长度值是]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_14687_18620_x197697654}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1953798917}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1960785527}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x997553259}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_906610746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_2094768628}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x433019081}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x1132129820}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1530435214}[：队列号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_x997487723}[：队列的最大长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_151231170}

[[如果队列的长度达到最大值时，后面收到的属于该队列的数据包将被丢弃。]{style="font-family:宋体"}]{#struct_0_14687_18620_x246837076}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1206859064}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_760015342}[指定定制列表第]{style="font-family:宋体"}[5]{lang="EN-US"}[组队列]{style="font-family:宋体"}[4]{lang="EN-US"}[的长度为]{style="font-family:宋体"}[40]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x164588121}

[\[Sysname\] qos cql 5 queue 4 queue-length 40]{lang="EN-US"}
:::

::: {#1230225604 .myid}
[]{#_Toc404792400}[]{#struct_0_14687_18620_x997422187}

**拥塞管理 \-- 定制队列配置命令 \-- qos cql queue serving**

------------------------------------------------------------------------

[**[qos cql queue serving]{lang="EN-US"}**]{#struct_0_14687_18620_1688550647}[命令用来设置各队列每次轮询所发送数据包的字节数。]{style="font-family:宋体"}

[**[undo qos cql queue serving]{lang="EN-US"}**]{#struct_0_14687_18620_1841788618}[命令用来恢复发送数据包数的缺省值。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_160032846}

[**[qos cql]{lang="EN-US"}**[ *cql-index* **queue** *queue-id* **serving** *byte-count*]{lang="EN-US"}]{#struct_0_14687_18620_x1380923162}

[**[undo]{lang="EN-US"}***[ ]{lang="EN-US"}***[qos cql]{lang="EN-US"}**[ *cql-index* **queue** *queue-id* **serving**]{lang="EN-US"}]{#struct_0_14687_18620_936041407}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_575357785}

[[发送数据包的字节数为]{style="font-family:宋体"}[1500]{lang="EN-US"}]{#struct_0_14687_18620_x996832363}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1671118193}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1865322502}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_7224613}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1688370904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x798725911}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x996766827}

[*[cql-index]{lang="EN-US"}*]{#struct_0_14687_18620_x263647360}[：定制列表的组号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1290710587}[：队列号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[byte-count]{lang="EN-US"}*]{#struct_0_14687_18620_x1677194408}[：队列每次轮询所发送的数据包的字节数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1438831402}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1907908744}[指定定制列表第]{style="font-family:宋体"}[5]{lang="EN-US"}[组队列]{style="font-family:宋体"}[2]{lang="EN-US"}[每次轮询所发送数据包的字节数为]{style="font-family:宋体"}[1400]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_568727293}

[\[Sysname\] qos cql 5 queue 2 serving 1400]{lang="EN-US"}
:::

::: {#2081021327 .myid}
[]{#_Toc404792402}[]{#struct_0_14687_18620_329751256}[]{#_Toc335120937}

**拥塞管理 \-- 加权公平队列配置命令 \-- display qos queue wfq**

------------------------------------------------------------------------

[**[display qos queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_490235736}[命令用来显示指定接口、指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[或所有接口及]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1976931181}

[**[display qos queue wfq interface]{lang="EN-US"}**[ { \[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \| **l2vpn-pw** \[ **peer** *ip-address* **pw-id** *pw-id* \] }]{lang="EN-US"}]{#struct_0_14687_18620_2054869148}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_682969033}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x80603852}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_724326774}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1370612491}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x49275390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_220317815}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1624130597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x654654878}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_747315297}[：指定的接口类型和接口编号。如果未指定本参数，将显示所有接口的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_x97587516}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[加权公平队列配置情况和统计信息]{style="font-family:宋体"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_449260580}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将显示所有]{style="font-family:宋体;
color:black"}[PW]{lang="EN-US"}[上的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2019687273}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_724392310}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue wfq interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_x972441954}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0]{lang="EN-US"}

[  Weight: IP Precedence]{lang="EN-US"}

[  Queues: Active/Max active/Total 0/0/128]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1359258177}[显示]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[下的]{style="font-family:宋体"}[加权公平队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue wfq l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_46713388}

[L2VPN-PW: peer 1.1.1.1, pw-id 1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Weighted Fair queuing: Size/Length/Discards 0/64/0]{lang="EN-US"}

[  Weight: IP Precedence]{lang="EN-US"}

[  Queues: Active/Max active/Total 0/0/128]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[表]{style="font-family:黑体"}[4-4 display qos queue wfq]{lang="EN-US"}]{#struct_0_14687_18620_x1461416473}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1725322393}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x360578819}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_661814350}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_724719990}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x1702935644}

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_x1507054563}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_x1507054564}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_x1718931721}

[[当前出队列的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_2007272945}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_x945410579}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_724785526}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_345820553}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2121127239}

[[Weighted Fair queuing]{lang="EN-US"}]{#struct_0_14687_18620_1698738784}

[[加权公平队列]{style="font-family:宋体"}]{#struct_0_14687_18620_828945275}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_724588918}

[[队列中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_792741059}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_x2057102995}

[[队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_x1150962295}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_2048428206}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_724654454}

[[Weight]{lang="EN-US"}]{#struct_0_14687_18620_316430149}

[[权重类型，分为两类：]{style="font-family:宋体"}[IP Precedence]{lang="EN-US"}]{#struct_0_14687_18620_x1871200371}[和]{style="font-family:宋体"}[DSCP]{lang="EN-US"}

[[Queues]{lang="EN-US"}]{#struct_0_14687_18620_x1309203}

[[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_724982134}[队列的信息]{style="font-family:宋体"}

[[Active]{lang="EN-US"}]{#struct_0_14687_18620_1706336247}

[[激活的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_1154682182}[队列数目]{style="font-family:宋体"}

[[Max active]{lang="EN-US"}]{#struct_0_14687_18620_1678064545}

[[最大激活过的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_725047670}[队列数目]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_14687_18620_2044022533}

[[当前配置的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_1361727010}[队列总数]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc333831532}

::: {#-1999388350 .myid}
[]{#_Toc404792403}[]{#struct_0_14687_18620_957055913}[]{#_Toc335120938}

**拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq**

------------------------------------------------------------------------

[**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1326827239}[命令用来在接口、]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或]{style="font-family:宋体"}[PW]{lang="EN-US"}[上应用加权公平队列或修改加权公平队列的参数。]{style="font-family:宋体"}

[**[undo qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_1426953693}[命令用来恢复缺省拥塞管理机制]{style="font-family:宋体"}[FIFO]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_724457843}

[**[qos wfq ]{lang="EN-US"}**[\[ **dscp** \| **precedence** \] \[ **queue-number** *total-queue-number* \| **queue-length** *max-queue-length* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_398315144}

[**[undo qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1757813904}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1358861424}

[[接口]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_2048765808}[上没有配置]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2083464859}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_854908525}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[交叉连接]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI LDP PW]{lang="EN-US"}[视图]{style="font-family:宋体"}[/VSI]{lang="EN-US"}[静态]{style="font-family:宋体"}[PW]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_724523379}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_444511610}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1609076016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x158367859}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_987742704}[：区分服务编码点权重类型。]{style="font-family:宋体"}

[**[precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1542285010}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级权重类型。]{style="font-family:宋体"}

[**[queue-length ]{lang="EN-US"}***[max-queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_1220525552}[：队列的最大长度，即每个队列中可容纳的数据包的最大个数，超出后数据包将被丢弃，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[queue-number]{lang="EN-US"}***[ total-queue-number]{lang="EN-US"}*]{#struct_0_14687_18620_1010947433}[：队列的总数目，可取的值为：]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[32]{lang="EN-US"}[、]{style="font-family:宋体"}[64]{lang="EN-US"}[、]{style="font-family:宋体"}[128]{lang="EN-US"}[、]{style="font-family:宋体"}[256]{lang="EN-US"}[、]{style="font-family:宋体"}[512]{lang="EN-US"}[、]{style="font-family:宋体"}[1024]{lang="EN-US"}[、]{style="font-family:宋体"}[2048]{lang="EN-US"}[、]{style="font-family:宋体"}[4096]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_14687_18620_724326771}

[[如果未指定权重类型，系统默认权重类型为]{style="font-family:宋体"}**[precedence]{lang="EN-US"}**]{#struct_0_14687_18620_1370612486}[。]{style="font-family:宋体"}

[[若是子接口，则接口需要使能]{style="font-family:宋体"}[LR]{lang="EN-US"}]{#struct_0_14687_18620_x49603069}[功能以保证队列生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_677324088}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1215817913}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[，并设置队列长度为]{style="font-family:宋体"}[100]{lang="EN-US"}[，总队列个数设置为]{style="font-family:宋体"}[512]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1684486591}

[\[Sysname\] interface gigabitethernet1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq queue-length 100 queue-number 512]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2063622188}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos ]{lang="EN-US"}**]{#struct_0_14687_18620_724392307}**[queue wfq]{lang="EN-US"}[ interface]{lang="EN-US"}**
:::

::: {#-1236906023 .myid}
[]{#_Toc404792405}[]{#struct_0_14687_18620_1218684381}

**拥塞管理 \-- 实时传输协议队列的配置命令 \-- display qos queue rtpq interface**

------------------------------------------------------------------------

[**[display qos queue rtpq interface]{lang="EN-US"}**]{#struct_0_14687_18620_1986778967}[命令用来显示指定接口、指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[或所有接口及]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的当前]{style="font-family:宋体"}[IP RTP Priority]{lang="EN-US"}[的队列信息，包括当前的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[长度和]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的丢包数。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x744762817}

[**[display qos queue rtpq interface ]{lang="EN-US"}**[\[ *interface-type* *interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_569317117}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1119235349}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1376708254}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_388730835}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1017498036}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1612338822}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x126410874}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1769668259}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_568727294}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_1207795061}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口上]{style="font-family:宋体"}[当前]{style="font-family:宋体"}[IP RTP Priority]{lang="EN-US"}[的队列信息，]{style="font-family:宋体"}[包括当前的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[长度和]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的丢包数。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_1639410326}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[当前]{style="font-family:宋体"}[IP RTP Priority]{lang="EN-US"}[的队列信息，]{style="font-family:宋体"}[包括当前的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[长度和]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的丢包数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_274666648}

[[如指定接口为]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}]{#struct_0_14687_18620_610368492}[接口，将显示继承该]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[接口的所有]{style="font-family:宋体"}[Virtual-Access]{lang="EN-US"}[接口下的]{style="font-family:宋体"}[QoS RTP]{lang="EN-US"}[队列的信息，]{style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}[本身无]{style="font-family:宋体"}[QoS]{lang="EN-US"}[信息显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1266296919}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x655610467}[显示当前]{style="font-family:宋体"}[IP RTP Priority]{lang="EN-US"}[的队列信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue rtpq interface]{lang="EN-US"}]{#struct_0_14687_18620_568792830}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - RTP queuing: Size/Max/Outputs/Discards 0/0/0/0]{lang="EN-US"}

[[表4-7 ]{lang="EN-US"}[display qos queue rtpq interface]{lang="EN-US"}]{#struct_0_14687_18620_91865230}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x62503585}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_568858366}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_568923902}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_568530686}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_568596222}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_569251582}

[[当前的输出队列]{style="font-family:宋体"}]{#struct_0_14687_18620_569317118}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_568727295}

[[队列中数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_568858367}

[[Max]{lang="EN-US"}]{#struct_0_14687_18620_568923903}

[[队列中数据包的历史最大数目]{style="font-family:宋体"}]{#struct_0_14687_18620_568530687}

[[Outputs]{lang="EN-US"}]{#struct_0_14687_18620_568596223}

[[发送出去的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_569251583}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_569317119}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_568727296}

::: {#-1163774496 .myid}
[]{#_Toc404792406}[]{#struct_0_14687_18620_568792832}

**拥塞管理 \-- 实时传输协议队列的配置命令 \-- qos rtpq**

------------------------------------------------------------------------

[**[qos rtpq]{lang="EN-US"}**]{#struct_0_14687_18620_91865232}[命令用来启动接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[下]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列特性，为某个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的端口范围的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文保留一个实时业务。]{style="font-family:宋体"}

[**[undo qos rtpq ]{lang="EN-US"}**]{#struct_0_14687_18620_56882175}[命令用来关闭接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列特性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x129448700}

[**[qos rtpq start-port]{lang="EN-US"}**[ *first-rtp-port-number* **end-port** *last-rtp-port-number* **bandwidth** *bandwidth* \[ **cbs** *committee-burst-size* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1225546192}

[**[undo qos rtpq]{lang="EN-US"}**]{#struct_0_14687_18620_x1205885943}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1449160902}

[[接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_14687_18620_x1663130795}[上没有启动]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列特性]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_568858368}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x914361809}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1612733857}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x525228307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1598773875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_640881114}

[**[start-port]{lang="EN-US"}***[ first-rtp-port-numbe]{lang="EN-US"}*[r]{lang="EN-US"}]{#struct_0_14687_18620_1342077956}[：指定发起]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的第一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的]{style="font-family:宋体"}[端口号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[end-port]{lang="EN-US"}***[ last-rtp-port-number]{lang="EN-US"}*]{#struct_0_14687_18620_568923904}[：指定发起]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的最后一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的]{style="font-family:宋体"}[端口号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[bandwidth ]{lang="EN-US"}***[bandwidth]{lang="EN-US"}*]{#struct_0_14687_18620_1847015022}[：]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列所占用的带宽，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *committee-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_1382475271}[：指定承诺突发尺寸，取值范围为]{style="font-family:
宋体"}[1500]{lang="EN-US"}[～]{style="font-family:
宋体"}[2000000]{lang="EN-US"}[字节，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1231176206}

[[该命令主要应用于对时延敏感的应用，如实时语音传输。]{style="font-family:宋体"}**[qos rtpq]{lang="EN-US"}**]{#struct_0_14687_18620_x1530064921}[命令为语音业务提供最优先服务。]{style="font-family:宋体"}

[[在配置]{style="font-family:宋体"}**[bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_1635911782}[参数时，配置值通常应大于此实时业务所需的带宽总量，以预防突发流量的冲击。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1739824992}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1115733585}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上启动]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列特性，发起]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的第一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的端口号为]{style="font-family:宋体"}[16384]{lang="EN-US"}[，发起]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文的最后一个]{style="font-family:宋体"}[UDP]{lang="EN-US"}[目的端口号为]{style="font-family:宋体"}[32767]{lang="EN-US"}[，]{style="font-family:宋体"}[RTP]{lang="EN-US"}[报文占用]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[的带宽，如果输出接口拥塞，进入]{style="font-family:宋体"}[RTP]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_568465152}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos rtpq start-port 16384 end-port 32767 bandwidth 64]{lang="EN-US"}
:::

::: {#-1365481909 .myid}
[]{#_Toc318812701}[]{#_Toc198110160}[]{#_Toc404792408}[]{#struct_0_14687_18620_x565947378}[]{#_Toc327195801}[]{#_Toc325978428}[]{#_Toc291750032}[]{#_Toc263759983}[]{#_Toc226262650}[]{#_Toc198110159}[]{#_Toc117857768}[]{#_Toc81455566}[]{#_Toc56569625}[]{#_Toc41626750}

**拥塞管理 \-- 基于类的队列配置命令 \-- display qos queue cbq**

------------------------------------------------------------------------

[**[display qos queue cbq]{lang="EN-US"}**]{#struct_0_14687_18620_x593997342}[命令用来显示指定接口、指]{style="font-family:宋体"}[定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[或所有接口与]{style="font-family:宋体"}[PVC]{lang="EN-US"}[、所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的基于类的队列配置信息和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x439248096}

[**[display qos queue cbq interface]{lang="EN-US"}**[ { \[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \] \| **l2vpn-pw** \[ **peer** *ip-address* **pw-id** *pw-id* \] }]{lang="EN-US"}]{#struct_0_14687_18620_x1553824064}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x668337334}

[[任意]{style="font-family:宋体"}]{#struct_0_14687_18620_x833007300}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_724719987}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_635716515}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1668300761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x660032404}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1419966059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1281473727}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_1489240661}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口的基于类的队列配置信息和运行情况。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_1468955179}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的基于类的队列配置信息和运行情况。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}***[pw-id]{lang="EN-US"}***[ pw-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1507054557}[：显示]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[PW]{lang="EN-US"}[上的加权公平队列配置情况和统计信息。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[远端]{style="font-family:宋体;color:black"}[PE]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[LSR ID]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;
color:black"}*[pw-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[PW]{lang="EN-US" style="color:black"}[的]{style="font-family:宋体;color:black"}[PW ID]{lang="EN-US" style="color:black"}[，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[4294967295]{lang="EN-US" style="color:black"}[。如果未指定本参数，将显示所有]{style="font-family:宋体;
color:black"}[PW]{lang="EN-US"}[上的基于类的队列配置情况和统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x759990346}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_724785523}[显示所有接口的基于类的队列配置信息和运行情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue cbq interface]{lang="EN-US"}]{#struct_0_14687_18620_345820548}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Class Based Queuing: Size/Discards 0/0]{lang="EN-US"}

[Queue Size: EF/AF/BE 0/0/0]{lang="EN-US"}

[  BE Queues: Active/Max active/Total 0/0/256]{lang="EN-US"}

[  AF Queues: Allocated 1]{lang="EN-US"}

[  Bandwidth(kbps): Available/Max reserve 74992/75000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1553635902}[显示]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[PW]{lang="EN-US"}[下的]{style="font-family:宋体"}[基于类的队列配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue cbq l2vpn-pw]{lang="EN-US"}]{#struct_0_14687_18620_1306603746}

[L2VPN-PW: peer 1.1.1.1, pw-id 1]{lang="EN-US"}

[Output queue - Urgent queuing: Size/Length/Discards 0/100/0]{lang="EN-US"}

[Output queue - Protocol queuing: Size/Length/Discards 0/500/0]{lang="EN-US"}

[Output queue - Class Based Queuing: Size/Discards 0/0]{lang="EN-US"}

[Queue Size: EF/AF/BE 0/0/0]{lang="EN-US"}

[  BE Queues: Active/Max active/Total 0/0/256]{lang="EN-US"}

[  AF Queues: Allocated 1]{lang="EN-US"}

[  Bandwidth(kbps): Available/Max reserve 74992/75000]{lang="EN-US"}

[[表4-8 ]{lang="EN-US"}[display qos queue cbq]{lang="EN-US"}]{#struct_0_14687_18620_x217524914}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1721307673}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x570972949}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1394404373}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_724588915}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_792741070}

[[L2VPN-PW]{lang="EN-US"}]{#struct_0_14687_18620_x1507054555}

[[显示指定]{style="font-family:宋体"}[PW]{lang="EN-US"}]{#struct_0_14687_18620_x1507054556}[的信息，]{style="font-family:宋体"}[PW]{lang="EN-US"}[通过远端]{style="font-family:宋体"}[PE]{lang="EN-US"}[地址和]{style="font-family:宋体"}[PW ID]{lang="EN-US"}[唯一标识]{style="font-family:宋体"}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_1855527286}

[[当前出队列的相关信息]{style="font-family:宋体"}]{#struct_0_14687_18620_464974905}

[[Urgent queuing]{lang="EN-US"}]{#struct_0_14687_18620_x557234001}

[[紧急队列]{style="font-family:宋体"}]{#struct_0_14687_18620_724654451}

[[Protocol queuing]{lang="EN-US"}]{#struct_0_14687_18620_316430146}

[[协议队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x1871200386}

[[Class Based Queuing]{lang="EN-US"}]{#struct_0_14687_18620_x1924082256}

[[基于类的队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x14931362}

[[Size]{lang="EN-US"}]{#struct_0_14687_18620_724982131}

[[队列中数据包的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_1706336242}

[[Length]{lang="EN-US"}]{#struct_0_14687_18620_1154485574}

[[队列的长度]{style="font-family:宋体"}]{#struct_0_14687_18620_x1448551037}

[[Discards]{lang="EN-US"}]{#struct_0_14687_18620_1024033867}

[[丢弃的数据包数目]{style="font-family:宋体"}]{#struct_0_14687_18620_725047667}

[[EF]{lang="EN-US"}]{#struct_0_14687_18620_x294629634}

[[加速转发队列]{style="font-family:宋体"}]{#struct_0_14687_18620_1007357169}

[[AF]{lang="EN-US"}]{#struct_0_14687_18620_x1711177252}

[[保证转发队列]{style="font-family:宋体"}]{#struct_0_14687_18620_724457844}

[[BE]{lang="EN-US"}]{#struct_0_14687_18620_398315145}

[[尽力转发队列]{style="font-family:宋体"}]{#struct_0_14687_18620_x1757813903}

[[Active]{lang="EN-US"}]{#struct_0_14687_18620_x1013791571}

[[BE]{lang="EN-US"}]{#struct_0_14687_18620_724523380}[队列当前处于激活状态的队列数]{style="font-family:宋体"}

[[Max active]{lang="EN-US"}]{#struct_0_14687_18620_106804595}

[[BE]{lang="EN-US"}]{#struct_0_14687_18620_329751254}[队列最大处于激活状态队列数]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_14687_18620_490235734}

[[BE]{lang="EN-US"}]{#struct_0_14687_18620_724326772}[队列总数]{style="font-family:宋体"}

[[Bandwidth(kbps)]{lang="EN-US"}]{#struct_0_14687_18620_1370612489}

[[带宽]{style="font-family:宋体"}]{#struct_0_14687_18620_x48751101}

[[Available]{lang="EN-US"}]{#struct_0_14687_18620_1743567207}

[[CBQ]{lang="EN-US"}]{#struct_0_14687_18620_724392308}[当前可用带宽]{style="font-family:宋体"}

[[Max reserve]{lang="EN-US"}]{#struct_0_14687_18620_1366210198}

[[CBQ]{lang="EN-US"}]{#struct_0_14687_18620_1391219717}[最大预留带宽]{style="font-family:宋体"}

[]{#_Toc318812702}[]{#_Toc263759985}[[ ]{lang="EN-US"}]{#_Toc325978429}

::: {#636519534 .myid}
[]{#_Toc318812703}[]{#_Toc263759986}[]{#_Toc404792409}[]{#struct_0_14687_18620_x2068693125}[]{#_Toc327195803}[]{#_Toc325978430}

**拥塞管理 \-- 基于类的队列配置命令 \-- qos reserved-bandwidth**

------------------------------------------------------------------------

[**[qos reserved-bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_x725861571}[命令用来设置最大预留带宽占可用带宽的百分比]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo qos reserved-bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_724719988}[命令用来恢复缺省情况]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_635716524}

[**[qos reserved-bandwidth pct]{lang="EN-US"}**[ *percent*]{lang="EN-US"}]{#struct_0_14687_18620_288014376}

[**[undo qos reserved-bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_961476079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x698277150}

[[最大预留带宽占可用带宽的百分比为]{style="font-family:宋体"}[80]{lang="EN-US"}]{#struct_0_14687_18620_774478362}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_750040305}

[[接口]{style="font-family:宋体"}]{#struct_0_14687_18620_724785524}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_345820555}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2121127233}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1699394144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_744434495}

[*[percent]{lang="EN-US"}*]{#struct_0_14687_18620_1924159368}[：预留带宽占可用带宽的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_734874934}

[[为队列分配带宽时，考虑到部分带宽用于控制协议报文、二层帧头等，通常配置的最大预留带宽不大于可用带宽的]{style="font-family:宋体"}[80]{lang="EN-US"}]{#struct_0_14687_18620_690766586}[％。]{style="font-family:宋体"}

[[建议慎重使用该命令修改最大预留带宽。如果配置的最大预留带宽过大，发送的报文加上链路层的帧头有可能大于接口最大可用带宽，导致接口无法满足需求，建议使用缺省最大预留带宽。]{style="font-family:宋体"}]{#struct_0_14687_18620_724588916}

[[接口最大可用带宽通过命令]{style="font-family:宋体"}**[bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_792741069}[进行配置，具体情况请参见接口分册命令参考中的介绍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x100787859}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1590382419}[配置]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口的最大预留带宽占可用带宽的百分比为]{style="font-family:宋体"}[70]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_865955736}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos reserved-bandwidth 70]{lang="EN-US"}
:::

::: {#561627462 .myid}
[]{#_Toc318812704}[]{#_Toc404792410}[]{#struct_0_14687_18620_x1919873515}[]{#_Toc327195804}[]{#_Toc325978431}

**拥塞管理 \-- 基于类的队列配置命令 \-- queue af**

------------------------------------------------------------------------

[**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1434402708}[命令用来配置类]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[AF]{lang="EN-US"}[队列]{style="font-family:宋体"}[，并配置类可确保的最小带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo queue af]{lang="EN-US"}**]{#struct_0_14687_18620_724654452}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_316430147}

[**[queue af bandwidth]{lang="EN-US"}**[ { *bandwidth* \| **pct** *percentage* ]{lang="EN-US"}]{#struct_0_14687_18620_x1871200385}[\| ]{lang="EN-US" style="font-size:11.0pt;
color:black"}**[remaining-pct]{lang="EN-US"}**[ ]{lang="EN-US"}*[remaining-percentage]{lang="EN-US" style="font-size:10.0pt;color:black"}[ ]{lang="EN-US"}*[}]{lang="EN-US"}

[**[undo queue af]{lang="EN-US"}**]{#struct_0_14687_18620_1967600513}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1672172425}

[[没有配置类采用]{style="font-family:宋体"}[AF]{lang="EN-US"}]{#struct_0_14687_18620_159981087}[队列。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2062985301}

[[流行为]{style="font-family:宋体"}]{#struct_0_14687_18620_x228800772}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_724982132}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1706336241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1154288966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1668008493}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_14687_18620_x1540051220}[：带宽，单位]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pct]{lang="EN-US"}**[ *percentage*]{lang="EN-US"}]{#struct_0_14687_18620_x2133212527}[：可用带宽的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[remaining-pct ]{lang="EN-US" style="font-size:11.0pt"}***[remaining-percentage]{lang="EN-US"}*]{#struct_0_14687_18620_x512333882}[：剩余带宽的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x597199742}

[[当在策略下将类与]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_725047668}[所属行为关联时，必须满足：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下为]{style="font-family:宋体"}]{#struct_0_14687_18620_x294629635}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列指定的带宽之和必须不大于该策略所应用接口的可用带宽；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下为]{style="font-family:宋体"}]{#struct_0_14687_18620_1007291633}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列指定的带宽百分比之和必须不大于]{style="font-family:宋体"}[100]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下]{style="font-family:宋体"}]{#struct_0_14687_18620_x1690330940}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列的带宽的配置必须都采用相同的值的类型，比如都采用绝对值形式，或者都采用百分比形式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1032058759}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1261419604}[为行为]{style="font-family:宋体"}[database]{lang="EN-US"}[配置采用]{style="font-family:宋体"}[AF]{lang="EN-US"}[队列，并且确保最小带宽为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1237394187}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue af bandwidth 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1532379850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue cbq interface]{lang="EN-US"}**]{#struct_0_14687_18620_724457841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_398315142}
:::

::: {#-1763971366 .myid}
[]{#_Toc318812705}[]{#_Toc404792411}[]{#struct_0_14687_18620_x1757813906}[]{#_Toc327195806}[]{#_Toc325978432}[]{#_Toc327195805}

**拥塞管理 \-- 基于类的队列配置命令 \-- queue ef**

------------------------------------------------------------------------

[**[queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_x1773306458}[命令用来配置类]{style="font-family:宋体"}[采用]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列]{style="font-family:宋体"}[，并配置最大带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_1536729782}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1901741310}

[**[queue ef bandwidth]{lang="EN-US"}**[ { *bandwidth* \[ **cbs** *burst* \] \| **pct** *percentage* \[ **cbs-ratio** *ratio* \] }]{lang="EN-US"}]{#struct_0_14687_18620_1290246181}

[**[undo queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_x1927200227}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_724523377}

[[没有配置类采用]{style="font-family:宋体"}[EF]{lang="EN-US"}]{#struct_0_14687_18620_444511608}[队列。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_729576152}

[[流行为]{style="font-family:宋体"}]{#struct_0_14687_18620_179227077}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_585586929}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_8733401}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1435996552}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1245697341}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_14687_18620_724326769}[：带宽，单位]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}[取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *burst*]{lang="EN-US"}]{#struct_0_14687_18620_x585702642}[：指定承诺突发尺寸，单位为字节，取值范围与设备的型号有关，请以设备的实际情况为准，缺省值为]{style="font-family:宋体"}*[bandwidth]{lang="EN-US"}*[×]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pct]{lang="EN-US"}**[ *percentage*]{lang="EN-US"}]{#struct_0_14687_18620_x1477813286}[：可用带宽的百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cbs-ratio ]{lang="EN-US"}***[ratio]{lang="EN-US"}*]{#struct_0_14687_18620_1698580656}[：允许的突发因子，取值范围为]{style="font-family:宋体"}[25]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，缺省值是]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1179756540}

[[该命令在流行为视图下不能与]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x2099356964}[，]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**[同时使用。]{style="font-family:宋体"}

[[在策略下，缺省类]{style="font-family:宋体"}[default-class]{lang="EN-US"}]{#struct_0_14687_18620_x764624876}[不能与]{style="font-family:宋体"}**[queue ef]{lang="EN-US"}**[所属]{style="font-family:宋体"}[behavior]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[当在策略下将类与]{style="font-family:宋体"}**[queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_x702811148}[所属行为关联时，必须满足：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下为]{style="font-family:宋体"}]{#struct_0_14687_18620_724392305}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列指定的带宽之和必须不大于该策略所应用接口的可用带宽。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下为]{style="font-family:宋体"}]{#struct_0_14687_18620_1366210203}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列指定的带宽百分比之和必须不大于]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下]{style="font-family:宋体"}]{#struct_0_14687_18620_x565816306}[AF]{lang="EN-US"}[队列和]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列的带宽的配置必须都采用相同的值的类型，比如都采用绝对值形式，或者都采用百分比形式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设置百分比形式]{lang="EN-US" style="font-family:宋体"}**[queue ef bandwidth]{lang="EN-US"}**[ **pct** *percentage* \[ **cbs-ratio** *ratio* \]]{lang="EN-US"}]{#struct_0_14687_18620_957472105}[，]{lang="EN-US" style="font-family:
宋体"}[CBS = ]{lang="EN-US"}[接口可用带宽×]{lang="EN-US" style="font-family:
宋体"}*[percentage]{lang="EN-US"}*[×]{lang="EN-US" style="font-family:宋体"}*[ratio]{lang="EN-US"}*[÷]{lang="EN-US" style="font-family:宋体"}[100]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设置绝对值形式]{lang="EN-US" style="font-family:宋体"}**[queue ef bandwidth]{lang="EN-US"}**[ *bandwidth* \[ **cbs** *burst* \]]{lang="EN-US"}]{#struct_0_14687_18620_1519115821}[，]{lang="EN-US" style="font-family:宋体"}[CBS = *burst*]{lang="EN-US"}[，若不指定]{lang="EN-US" style="font-family:宋体"}*[burst]{lang="EN-US"}*[，则]{lang="EN-US" style="font-family:宋体"}[CBS = *bandwidth*]{lang="EN-US"}[×]{lang="EN-US" style="font-family:
宋体"}[25]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x726637864}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x636121856}[配置报文进入]{style="font-family:宋体"}[EF]{lang="EN-US"}[队列，最大带宽为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[承诺突发尺寸]{style="font-family:宋体"}[为]{style="font-family:宋体"}[5000bytes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_724719985}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue ef bandwidth 200 cbs 5000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_635716513}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue cbq interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1668300767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x1822831818}
:::

::: {#2022973888 .myid}
[]{#_Toc404792412}[]{#struct_0_14687_18620_568792826}[]{#_Toc382405969}[]{#_Toc373826859}

**拥塞管理 \-- 基于类的队列配置命令 \-- queue sp**

------------------------------------------------------------------------

[**[queue sp]{lang="EN-US"}**]{#struct_0_14687_18620_568858362}[命令用来配置类采用]{style="font-family:宋体"}[SP]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[**[undo queue sp]{lang="EN-US"}**]{#struct_0_14687_18620_x914361799}[用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1568103850}

[**[queue sp]{lang="EN-US"}**]{#struct_0_14687_18620_639807872}

[**[undo queue sp]{lang="EN-US"}**]{#struct_0_14687_18620_901092946}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1908692053}

[[没有配置类采用]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_14687_18620_568923898}[队列。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1691172385}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1759960181}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x616553487}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1986562892}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1075874796}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1945303438}

[[配置了该命令的行为不能与缺省类关联使用。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1661107997}

[[队列长度为固定值，取值与产品的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1529858603}

[[在同一流行为视图下]{style="font-family:宋体"}**[queue ]{lang="EN-US"}**]{#struct_0_14687_18620_568465146}**[sp]{lang="EN-US"}**[不能与]{style="font-family:宋体"}**[queue ]{lang="EN-US"}[ef]{lang="EN-US"}**[命令同时使用。]{style="font-family:宋体"}

[[在同一流行为视图下]{style="font-family:宋体"}**[queue ]{lang="EN-US"}**]{#struct_0_14687_18620_1322376144}**[sp]{lang="EN-US"}**[不能与]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**[和]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**[命令同时使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_261573321}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1856136524}[配置报文进入]{style="font-family:宋体"}[SP]{lang="EN-US"}[队列。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x235171596}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue sp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1639148910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue cbq interface]{lang="EN-US"}**]{#struct_0_14687_18620_568530682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x1764536380}
:::

::: {#2100456657 .myid}
[]{#_Toc39395261}[]{#_Toc404792413}[]{#struct_0_14687_18620_x685487874}[]{#_Toc327195808}[]{#_Toc325978433}[]{#_Toc388619197}[]{#_Toc327195807}

**拥塞管理 \-- 基于类的队列配置命令 \-- queue wfq**

------------------------------------------------------------------------

[**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_943628993}[命令用来为缺省类配置采用公平队列。]{style="font-family:宋体"}

[**[undo queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x589733089}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_968478841}

[**[queue wfq ]{lang="EN-US"}**[\[ **queue-number** *total-queue-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1790840737}

[**[undo queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_724785521}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_345820550}

[[没有为缺省类配置采用公平队列]{style="font-family:宋体"}]{#struct_0_14687_18620_2121127238}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1698673248}

[[流行为]{style="font-family:宋体"}]{#struct_0_14687_18620_22346389}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1770695127}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1219924627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_453891688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_724588913}

[**[queue-number]{lang="EN-US"}***[ total-queue-number]{lang="EN-US"}*]{#struct_0_14687_18620_792741064}[：公平队列的数目，可取的值为]{style="font-family:宋体"}[16]{lang="EN-US"}[、]{style="font-family:宋体"}[32]{lang="EN-US"}[、]{style="font-family:宋体"}[64]{lang="EN-US"}[、]{style="font-family:宋体"}[128]{lang="EN-US"}[、]{style="font-family:宋体"}[256]{lang="EN-US"}[、]{style="font-family:宋体"}[512]{lang="EN-US"}[、]{style="font-family:宋体"}[1024]{lang="EN-US"}[、]{style="font-family:宋体"}[2048]{lang="EN-US"}[、]{style="font-family:宋体"}[4096]{lang="EN-US"}[，即]{style="font-family:宋体"}[2]{lang="EN-US"}[的幂数，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x100787854}

[[配置了该命令的行为仅仅可以与缺省类关联使用，另外，该命令还可以搭配]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_1590054739}[命令或]{style="font-family:宋体"}**[wred]{lang="EN-US"}**[命令使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2041457435}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1860636459}[为缺省类配置使用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[，队列数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_724654449}

[\[Sysname\] traffic behavior test]{lang="EN-US"}

[\[Sysname-behavior-test\] queue wfq queue-number 16]{lang="EN-US"}

[\[Sysname\] qos policy user1]{lang="EN-US"}

[\[Sysname-qospolicy-user1\] classifier default-class behavior test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2022222006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue cbq interface]{lang="EN-US"}**]{#struct_0_14687_18620_1114535729}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[traffic behavior]{lang="EN-US"}**]{#struct_0_14687_18620_x895589807}
:::

::: {#-2024078745 .myid}
[]{#_Toc404792414}[]{#struct_0_14687_18620_530648211}[]{#_Toc327195810}[]{#_Toc325978434}[]{#_Toc327195809}[]{#_Toc263759990}[]{#_Toc226262656}[]{#_Toc198110165}[]{#_Toc117857790}[]{#_Toc81455595}[]{#_Toc56569650}[]{#_Toc41626777}[]{#_Toc39395265}

**拥塞管理 \-- 基于类的队列配置命令 \-- queue-length**

------------------------------------------------------------------------

[**[queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_1060776499}[命令用来配置最大队列长度，丢弃方式为尾部丢弃]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_1316884230}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x394996086}

[**[queue-length]{lang="EN-US"}**[ *queue-length*]{lang="EN-US"}]{#struct_0_14687_18620_341643208}

[**[undo queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_724982129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x249978902}

[[丢弃方式为尾部丢弃方式，队列长度为]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_14687_18620_473282187}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_135236113}

[[流行为]{style="font-family:宋体"}]{#struct_0_14687_18620_x279924580}[视]{style="font-family:宋体"}[图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1180816728}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x148414558}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x676970779}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_725047665}

[*[queue-length]{lang="EN-US"}*]{#struct_0_14687_18620_x294629632}[：队列最大阈值，取值范围和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1006963953}

[[该命令必须在配置了]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1674596819}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[后使用。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**]{#struct_0_14687_18620_x1030988168}[后，若执行]{style="font-family:宋体"}**[undo queue af]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo queue wfq]{lang="EN-US"}**[命令，则]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**[也同时被取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x469419858}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_111997194}[配置尾部丢弃，队列长度最大为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_724457842}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue af bandwidth 200]{lang="EN-US"}

[\[Sysname-behavior-database\] queue-length 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_398315143}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_14687_18620_x1757813905}**[af]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x207222517}
:::

::: {#-1536376486 .myid}
[]{#_Toc404792415}[]{#struct_0_14687_18620_932382601}[]{#_Toc344129983}[]{#_Toc341855935}

**拥塞管理 \-- 基于类的队列配置命令 \-- wred**

------------------------------------------------------------------------

[**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_x1298765511}[命令用来配置丢弃方式为加权随机早期检测。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **wred**]{lang="EN-US"}]{#struct_0_14687_18620_504047927}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1578716366}

[**[wred]{lang="EN-US"}**[ \[ **dscp** \| **ip-precedence** \]]{lang="EN-US"}]{#struct_0_14687_18620_1960964161}

[**[undo wred]{lang="EN-US"}**]{#struct_0_14687_18620_724523378}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_444511611}

[[没有配]{style="font-family:宋体"}]{#struct_0_14687_18620_x1609076017}[置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1724451800}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_50336265}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1611392086}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x54079521}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1607027810}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_724326770}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1370612487}[：表明在为一个包计算丢弃概率时使用的是]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x49668605}[：表明在为一个包计算丢弃概率时使用的是]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值。缺省情况下使用的是]{style="font-family:宋体"}**[ip-precedence]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_677973920}

[[该命令必须在配置了]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1253442297}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[后使用。]{style="font-family:宋体"}**[wred]{lang="EN-US"}**[和]{style="font-family:宋体"}**[queue-length]{lang="EN-US"}**[这两个命令不能同时有效。取消该配置时将删除]{style="font-family:宋体"}[WRED]{lang="EN-US"}[相关的其他配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x222917378}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x713192163}[配置采用加权早期检测方式，丢弃概率以]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_724392306}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue wfq]{lang="EN-US"}

[\[Sysname-behavior-database\] wred]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1366210204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x565881842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_607688286}
:::

::: {#-863953509 .myid}
[]{#_Toc404792416}[]{#struct_0_14687_18620_327877054}[]{#_Toc344129986}[]{#_Toc341855936}[]{#_Toc291750040}[]{#_Toc263759991}[]{#_Toc226262657}[]{#_Toc198110166}[]{#_Toc117857791}[]{#_Toc81455596}[]{#_Toc56569651}[]{#_Toc41626778}[]{#_Toc39395266}[]{#_Toc344129807}[]{#_Toc344129984}[]{#_Toc344129808}[]{#_Toc344129985}

**拥塞管理 \-- 基于类的队列配置命令 \-- wred dscp**

------------------------------------------------------------------------

[**[wred dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x1556075348}[命令用来设置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[各]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的下限、上限和丢弃概率。]{style="font-family:宋体"}

[**[undo wred dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1069272367}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x15844026}

[**[wred dscp]{lang="EN-US"}**[ *dscp-value* **low-limit** *low-limit* **high-limit** *high-limit* \[ **discard-probability** *discard-prob* \]]{lang="EN-US"}]{#struct_0_14687_18620_724719986}

[**[undo wred dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_635716514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1668300760}

[[下限缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_14687_18620_906051537}[，上限缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[，丢弃概率缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1322432595}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1813257369}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1983022588}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1560441004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_724785522}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_345820549}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_x217524915}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所示。]{style="font-family:宋体"}

[**[low-limit ]{lang="EN-US"}***[low-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x571038485}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[下限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x922985286}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[上限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_14687_18620_528720884}[：丢弃概率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_328384980}

[[进行本命令配置以前，必须已用]{style="font-family:宋体"}**[wred dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x545637045}[命令使能了基于]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[丢弃方式。]{style="font-family:宋体"}

[[取消]{style="font-family:宋体"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_724588914}[配置，]{style="font-family:宋体"}**[wred dscp]{lang="EN-US"}**[配置同时被取消。]{style="font-family:宋体"}

[[取消]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_792741071}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[配置，丢弃参数的配置同时被取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1855527285}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_464778297}[设置]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}[的报文的队列下限为]{style="font-family:
宋体"}[20]{lang="EN-US"}[，上限为]{style="font-family:宋体"}[40]{lang="EN-US"}[，丢弃概率为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1943517692}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue wfq]{lang="EN-US"}

[\[Sysname-behavior-database\] wred dscp]{lang="EN-US"}

[\[Sysname-behavior-database\] wred dscp 3 low-limit 20 high-limit 40 discard-probability 15]{lang="EN-US"}

[]{#_Toc341855937}[]{#_Toc291750041}[]{#_Toc263759992}[]{#_Toc226262658}[]{#_Toc198110167}[]{#_Toc117857792}[]{#_Toc81455597}[]{#_Toc56569652}[]{#_Toc41626779}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_896327670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_1473784121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_724654450}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_316430145}
:::

::: {#432088633 .myid}
[]{#_Toc404792417}[]{#struct_0_14687_18620_x1871200383}[]{#_Toc344129987}

**拥塞管理 \-- 基于类的队列配置命令 \-- wred ip-precedence**

------------------------------------------------------------------------

[**[wred ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1164567369}[命令用来设置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[各优先级的下限、上限和丢弃概率。]{style="font-family:宋体"}

[**[undo wred ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x1150414259}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x33205473}

[**[wred ip-precedence]{lang="EN-US"}**[ *precedence* **low-limit** *low-limit* **high-limit** *high-limit* \[ **discard-probability** *discard-prob* \]]{lang="EN-US"}]{#struct_0_14687_18620_25497412}

[**[undo wred ip-precedence]{lang="EN-US"}**[ *precedence*]{lang="EN-US"}]{#struct_0_14687_18620_x525621164}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_724982130}

[[下限缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_14687_18620_1706336243}[，上限缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[，丢弃概率缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1154420038}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_523445390}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_102594870}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x355412079}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x7796392}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1027798447}

[*[precedence]{lang="EN-US"}*]{#struct_0_14687_18620_725047666}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x294629633}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[下限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US"}*]{#struct_0_14687_18620_1006898417}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[上限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_14687_18620_1359398841}[：丢弃概率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x404239864}

[[进行本命令配置以前，必须已用]{style="font-family:宋体"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_1253771821}[命令使能了基于]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[丢弃方式。]{style="font-family:宋体"}

[[取消]{style="font-family:宋体"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_1133359127}[配置，]{style="font-family:宋体"}**[wred ip-precedence]{lang="EN-US"}**[配置同时被取消。]{style="font-family:宋体"}

[[取消]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_886654333}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[配置，丢弃参数的配置同时被取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648195150}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1094629915}[设置优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[的报文的队列下限为]{style="font-family:宋体"}[20]{lang="EN-US"}[，上限为]{style="font-family:宋体"}[40]{lang="EN-US"}[，丢弃概率为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1568358135}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue wfq]{lang="EN-US"}

[\[Sysname-behaviro-database\] wred ip-precedence]{lang="EN-US"}

[\[Sysname-behavior-database\] wred ip-precedence 3 low-limit 20 high-limit 40 discard-probability 15]{lang="EN-US"}

[]{#_Toc341855938}[]{#_Toc291750042}[]{#_Toc263759993}[]{#_Toc226262659}[]{#_Toc198110168}[]{#_Toc117857793}[]{#_Toc81455598}[]{#_Toc56569653}[]{#_Toc41626780}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1498656531}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1417789026}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_1800958396}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_x2034317404}
:::

::: {#-2056630190 .myid}
[]{#_Toc404792418}[]{#struct_0_14687_18620_x1648129614}[]{#_Toc344129988}

**拥塞管理 \-- 基于类的队列配置命令 \-- wred weighting-constant**

------------------------------------------------------------------------

[**[wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_550111425}[命令用来设置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[计算平均队列长度的指数。]{style="font-family:宋体"}

[**[undo wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_x1849039571}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x559979651}

[**[wred weighting-constant]{lang="EN-US"}**[ *exponent*]{lang="EN-US"}]{#struct_0_14687_18620_x864410843}

[**[undo wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_x1884217016}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x224574764}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x45666609}[计算平均队列长度的指数为]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648326222}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1457208217}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2132373872}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2066148361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1766957580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x509312279}

[*[exponent]{lang="EN-US"}*]{#struct_0_14687_18620_358352867}[：指数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1702376835}

[[需配置了]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1648260686}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[，并已用]{style="font-family:宋体"}**[wred]{lang="EN-US"}**[使能了]{style="font-family:宋体"}[WRED]{lang="EN-US"}[丢弃方式。]{style="font-family:宋体"}

[[如果取消]{style="font-family:宋体"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_557281499}[配置，]{style="font-family:宋体"}**[wred weighting-constant]{lang="EN-US"}**[配置同时被取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1481313025}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_767635774}[配置计算平均队列长度的指数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_244539946}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue af bandwidth 200]{lang="EN-US"}

[\[Sysname-behavior-database\] wred ip-precedence]{lang="EN-US"}

[\[Sysname-behavior-database\] wred weighting-constant 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x539471837}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_973499898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1647933006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_1275416039}
:::

::: {#-1969927489 .myid}
[]{#_Toc404792420}[]{#struct_0_14687_18620_x511522418}

**拥塞管理 \-- 报文信息预提取命令 \-- qos pre-classify**

------------------------------------------------------------------------

[**[qos pre-classify]{lang="EN-US"}**]{#struct_0_14687_18620_x876418746}[命令用来开启报文信息预提取功能。]{style="font-family:宋体"}

[**[undo qos pre-classify]{lang="EN-US"}**]{#struct_0_14687_18620_51010987}[命令用来关闭报文信息预提取功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1759361153}

[**[qos pre-classify]{lang="EN-US" style="color:windowtext"}**]{#struct_0_14687_18620_949399707}

[**[undo qos]{lang="EN-US"}**[ **pre-classify**]{lang="EN-US"}]{#struct_0_14687_18620_x1800278980}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_165639375}

[[报文信息预提取功能处于关闭状态]{style="font-family:宋体"}]{#struct_0_14687_18620_144688997}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1013228474}

[[Tunnel]{lang="EN-US"}]{#struct_0_14687_18620_x890216276}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_299896498}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1692656313}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1417667368}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2072082808}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_165180623}[在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上使能报文信息预提取功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1735420009}

[\[Sysname\] interface tunnel 1]{lang="EN-US"}

[\[Sysname-Tunnel1\] qos pre-classify]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section6 style="layout-grid:15.85pt"}
:::

::: {#985528416 .myid}
[]{#_Toc404792423}[]{#struct_0_14687_18620_1702312592}[]{#_Toc292375535}[]{#_Toc263760005}[]{#_Toc226262672}[]{#_Toc198110181}[]{#_Toc121389323}

**硬件实现拥塞管理 \-- 严格优先级队列配置命令 \-- display qos queue sp**

------------------------------------------------------------------------

[**[display qos queue sp interface]{lang="EN-US"}**]{#struct_0_14687_18620_x510969139}[命令用来显示接口的]{style="font-family:
宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[Strict Priority]{lang="EN-US"}[，严格优先级）队列配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_241763135}

[**[display qos queue sp interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1647867470}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_941274326}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1531954433}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1971995016}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_597660082}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x525654841}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_438775601}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_114773001}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648064078}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_1180916243}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[SP]{lang="EN-US"}[队列配置情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1721802875}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x2115078924}[显示]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的严格优先级队列配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue sp interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_1323893607}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Output queue: Strict Priority queuing]{lang="EN-US"}

[[表5-1 ]{lang="EN-US"}[display qos queue sp interface]{lang="EN-US"}]{#struct_0_14687_18620_x171470679}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1718876121}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_93192836}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647998542}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x314203410}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_2109502505}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_1459367510}

[[当前出队列类型]{style="font-family:宋体"}]{#struct_0_14687_18620_1367471352}

[ ]{lang="EN-US"}

::: {#1104431523 .myid}
[]{#_Toc404792424}[]{#struct_0_14687_18620_x151599138}[]{#_Toc292375536}[]{#_Toc263760006}[]{#_Toc226262673}[]{#_Toc198110182}[]{#_Toc121389324}[]{#_Toc342308515}[]{#_Toc342308516}

**硬件实现拥塞管理 \-- 严格优先级队列配置命令 \-- qos sp**

------------------------------------------------------------------------

[**[qos sp]{lang="EN-US"}**]{#struct_0_14687_18620_x1647670862}[命令用来在接口上配置严格优先队列。]{style="font-family:宋体"}

[**[undo qos sp]{lang="EN-US"}**]{#struct_0_14687_18620_1497279719}[命令用来恢复接口上缺省的队列算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1954332805}

[**[qos sp]{lang="EN-US"}**]{#struct_0_14687_18620_x898105865}

[**[undo qos sp]{lang="EN-US"}**]{#struct_0_14687_18620_2040890221}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1511705009}

[[接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1380357082}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1255134558}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1647605326}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1578585071}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1405894890}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1161259237}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1839249350}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1178450531}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[SP]{lang="EN-US"}[模式的队列调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x171585644}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos sp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x316907467}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue sp interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1648195149}
:::

::: {#-1535130307 .myid}
[]{#_Toc404792426}[]{#struct_0_14687_18620_x129141007}[]{#_Toc292375538}[]{#_Toc263760008}[]{#_Toc226262675}[]{#_Toc198110184}[]{#_Toc121389326}

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- display qos queue wrr interface**

------------------------------------------------------------------------

[**[display qos queue wrr interface]{lang="EN-US"}**]{#struct_0_14687_18620_x427199120}[命令用来显示接口的]{style="font-family:宋体"}[WRR]{lang="EN-US"}[（]{style="font-family:宋体"}[Weighted Round Robin]{lang="EN-US"}[，加权轮询）队列配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1201216070}

[**[display qos queue wrr interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_1256590691}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1982211191}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1648129613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1309626312}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_489491677}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x357094508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_272637753}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x306269661}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x153089491}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x589356583}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列配置情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1760767446}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1648326221}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue wrr interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_x1053923690}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Output queue: Weighted Round Robin queuing]{lang="EN-US"}

[ Queue ID        Queue    name      Group           Weight]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 0               be              1               1]{lang="EN-US"}

[ 1               af1             1               1]{lang="EN-US"}

[ 2               af2             1               1]{lang="EN-US"}

[ 3               af3             1               1]{lang="EN-US"}

[ 4               af4             1               1]{lang="EN-US"}

[ 5               ef              1               1]{lang="EN-US"}

[ 6               cs6             1               1]{lang="EN-US"}

[ 7               cs7             sp              N/A]{lang="EN-US"}

[[表5-2 ]{lang="EN-US"}[display qos queue wrr interface]{lang="EN-US"}]{#struct_0_14687_18620_x1225784611}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1718157945}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_100628585}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648260685}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_960566026}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_738083145}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_x684141678}

[[当前出队列类型]{style="font-family:宋体"}]{#struct_0_14687_18620_940488958}

[[Queue ID]{lang="EN-US"}]{#struct_0_14687_18620_x1647933005}

[[队列号]{style="font-family:宋体"}]{#struct_0_14687_18620_872131512}

[[Queue name]{lang="EN-US"}]{#struct_0_14687_18620_398648716}

[[队列名字]{style="font-family:宋体"}]{#struct_0_14687_18620_758631751}

[[Group]{lang="EN-US"}]{#struct_0_14687_18620_1672540150}

[[分组号，说明队列属于哪一个分组，缺省情况下，队列所属的分组号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_14687_18620_2098410590}

[[Weight]{lang="EN-US"}]{#struct_0_14687_18620_1991134377}

[[各个队列的调度权重，当前]{style="font-family:宋体"}[WRR]{lang="EN-US"}]{#struct_0_14687_18620_x1647867469}[队列调度权重的计算方式为]{style="font-family:宋体"}[Weight]{lang="EN-US"}[，]{style="font-family:宋体"}[ N/A]{lang="EN-US"}[表示该队列采用]{style="font-family:宋体"}[SP]{lang="EN-US"}[调度算法]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1891507987 .myid}
[]{#_Toc404792427}[]{#struct_0_14687_18620_x1431444205}[]{#_Toc292375539}[]{#_Toc263760009}[]{#_Toc226262676}[]{#_Toc198110185}[]{#_Toc121389327}[]{#_Toc115171180}[]{#_Toc342308520}[]{#_Toc342308521}

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr**

------------------------------------------------------------------------

[**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_2070566023}[命令用于在接口上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，并指明当前]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列调度权重的计算方式。]{style="font-family:宋体"}

[**[undo qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x907942839}[命令用于在接口上取消]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，恢复缺省的队列算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1687095440}

[**[qos wrr ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_x1149452676}

[**[undo qos wrr ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_2072289760}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648064077}

[[接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1584200770}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_475101110}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x438002830}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x10695962}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x28701896}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2008113364}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_201128807}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_x1647998541}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_1251880531}[：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_2009408522}

[[必须先使用]{style="font-family:宋体"}**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x1107247929}[命令在接口上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，然后才能进行]{style="font-family:宋体"}[WRR]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2112973047}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_502965514}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，并按照权重进行计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1647670861}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr weight]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1093995192}[在接口]{style="font-family:宋体"}[GigabitEthernet1/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，并按照每次轮询可发送的字节数进行计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1603384672}

[\[Sysname\] interface gigabitethernet 1/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr byte-count]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1532365191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wrr interface]{lang="EN-US"}**]{#struct_0_14687_18620_1767311536}
:::

::: {#1813098140 .myid}
[]{#_Toc404792428}[]{#struct_0_14687_18620_x823736186}[]{#_Toc292375540}[]{#_Toc263760010}[]{#_Toc226262677}[]{#_Toc198110186}[]{#_Toc121389328}[]{#_Toc290907807}

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr { byte-count \| weight }**

------------------------------------------------------------------------

[**[qos wrr ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_1515133005}[命令用来配置]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列或修改]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列的参数。]{style="font-family:宋体"}

[**[undo qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x1647605325}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1150298284}

[[支持]{style="font-family:宋体"}[WRR]{lang="EN-US"}]{#struct_0_14687_18620_x65418717}[分组：]{style="font-family:宋体"}

[**[qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*[ **group** { **1** \| **2** } { **byte-count** \| **weight** } *schedule-value*]{lang="EN-US"}]{#struct_0_14687_18620_697090501}

[**[undo qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x202934791}

[[不支持]{style="font-family:宋体"}[WRR]{lang="EN-US"}]{#struct_0_14687_18620_x431111108}[分组：]{style="font-family:宋体"}

[**[qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*[ { **byte-count** \| **weight** } *schedule-value*]{lang="EN-US"}]{#struct_0_14687_18620_199585141}

[**[undo qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1648195152}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2037537967}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_152455401}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1185243343}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1575353571}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x87446385}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_2132244253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1417792023}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648129616}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1712910839}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ { **1** \| **2** }]{lang="EN-US"}]{#struct_0_14687_18620_x1146944514}[：表示该队列属于哪个]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组，缺省为]{style="font-family:宋体"}[group 1]{lang="EN-US"}[。其中]{style="font-family:宋体"}[group 1]{lang="EN-US"}[表示该队列属于]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[group 2]{lang="EN-US"}[表示该队列属于]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组]{style="font-family:宋体"}[2]{lang="EN-US"}[。各组之间执行优先级调度，由组]{style="font-family:宋体"}[1]{lang="EN-US"}[至组]{style="font-family:宋体"}[2]{lang="EN-US"}[优先级依次降低。支持的组数，根据设备类型的不同可能不同。]{style="font-family:宋体"}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_1395366347}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_x804175358}[：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[schedule-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1098631197}[：配置队列的调度权重，取值范围和缺省的调度权重值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x885044928}

[[必须先使用]{style="font-family:宋体"}**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x2020665740}[命令在接口上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，然后才能进行本配置。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1648326224}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[]{#struct_0_14687_18620_x650639163}[[表5-3 ]{lang="EN-US"}*[queue-id]{lang="EN-US"}*]{#_Ref293562576}[数字和关键字对应表]{style="font-family:黑体"}

[]{#table_struct_0_1711972665}[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x265870583}[数字]{style="font-family:黑体"}
:::

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1795743280}[关键字]{style="font-family:黑体"}

[[0]{lang="EN-US"}]{#struct_0_14687_18620_190491963}

[[be]{lang="EN-US"}]{#struct_0_14687_18620_x550749131}

[[1]{lang="EN-US"}]{#struct_0_14687_18620_x1648260688}

[[af1]{lang="EN-US"}]{#struct_0_14687_18620_1720080913}

[[2]{lang="EN-US"}]{#struct_0_14687_18620_x638962720}

[[af2]{lang="EN-US"}]{#struct_0_14687_18620_x478163921}

[[3]{lang="EN-US"}]{#struct_0_14687_18620_x961317227}

[[af3]{lang="EN-US"}]{#struct_0_14687_18620_x1647933008}

[[4]{lang="EN-US"}]{#struct_0_14687_18620_112616625}

[[af4]{lang="EN-US"}]{#struct_0_14687_18620_x1022145904}

[[5]{lang="EN-US"}]{#struct_0_14687_18620_2022084672}

[[ef]{lang="EN-US"}]{#struct_0_14687_18620_1009603834}

[[6]{lang="EN-US"}]{#struct_0_14687_18620_x1647867472}

[[cs6]{lang="EN-US"}]{#struct_0_14687_18620_2104073740}

[[7]{lang="EN-US"}]{#struct_0_14687_18620_x238247214}

[[cs7]{lang="EN-US"}]{#struct_0_14687_18620_1746895903}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_278586620}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1648064080}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，并按照每次轮询可发送的字节数进行计算，配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[的调度权重为]{style="font-family:宋体"}[100]{lang="EN-US"}[，分组为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_823964987}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr byte-count]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr 0 group 1 byte-count 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1663786662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wrr interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1216540922}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x1618369424}

::: {#1586949297 .myid}
[]{#_Toc404792429}[]{#struct_0_14687_18620_202344355}[]{#_Toc292375541}[]{#_Toc263760011}[]{#_Toc226262678}[]{#_Toc198110187}

**硬件实现拥塞管理 \-- 加权轮询队列配置命令 \-- qos wrr group sp**

------------------------------------------------------------------------

[**[qos wrr group sp]{lang="EN-US"}**]{#struct_0_14687_18620_x1765046863}[命令用来配置队列加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，采用严格优先级调度算法。]{style="font-family:宋体"}

[**[undo qos wrr group sp]{lang="EN-US"}**]{#struct_0_14687_18620_x1647998544}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_492365644}

[**[qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*[ **group sp**]{lang="EN-US"}]{#struct_0_14687_18620_103888489}

[**[undo qos wrr ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1060913582}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x223629186}

[[接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_832183061}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x788246926}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x795202181}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647670864}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_690710665}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1346498365}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1898911704}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_477047947}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sp]{lang="EN-US"}**]{#struct_0_14687_18620_x299563239}[：队列加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，采用严格优先级调度算法。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1842202676}

[[此命令需要在端口队列为]{style="font-family:宋体"}[WRR]{lang="EN-US"}]{#struct_0_14687_18620_x1891869981}[调度模式下使用。]{style="font-family:宋体"}

[[SP]{lang="EN-US"}]{#struct_0_14687_18620_x1647605328}[组与普通]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组不同，加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组的端口队列采用严格优先级调度算法，不再采用加权轮循调度算法。调度时先调度]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，然后调度其他]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组。]{style="font-family:宋体"}

[[必须先使用]{style="font-family:宋体"}**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_1197352451}[命令在接口上使能]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，然后才能进行本配置。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1547210857}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1800197487}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_325088943}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WRR]{lang="EN-US"}[队列，并配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组进行严格优先级调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1188318049}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr weight]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wrr 0 group sp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1457728839}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wrr interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1648195151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wrr]{lang="EN-US"}**]{#struct_0_14687_18620_x471454026}
:::

::: {#-487261942 .myid}
[]{#_Toc404792431}[]{#struct_0_14687_18620_x758467582}[]{#_Toc292375544}[]{#_Toc263760015}[]{#_Toc226262682}[]{#_Toc198110191}[]{#_Toc121389331}

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- display qos queue wfq interface**

------------------------------------------------------------------------

[**[display qos queue wfq interface]{lang="EN-US"}**]{#struct_0_14687_18620_589546067}[命令用来显示接口的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1969965106}

[**[display qos queue wfq interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x504391252}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648129615}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_2116195366}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x648456690}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x470723148}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_394819385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x604256609}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1113184757}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1952700279}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x1648326223}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[配置情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_108875724}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1680026394}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/1]{lang="EN-US"}[的加权公平队列配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue wfq interface gigabitethernet 1/1]{lang="EN-US"}]{#struct_0_14687_18620_x1069152420}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Output queue: Hardware Weighted Fair Queuing]{lang="EN-US"}

[ Queue ID        Queue name      Group           Byte count      Min Bandwidth]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="NL"}

[ 0               be              1               1               64]{lang="NL"}

[ 1               af1             1               1               64]{lang="NL"}

[ 2               af2             1               1               64]{lang="NL"}

[ 3               af3             1               1               64]{lang="NL"}

[ 4               af4             1               1               64]{lang="NL"}

[ ]{lang="NL"}[5               ef              1               1               64]{lang="EN-US"}

[ 6               cs6             1               1               64]{lang="EN-US"}

[ 7               cs7             1               1               64]{lang="EN-US"}

[[表5-4 ]{lang="EN-US"}[display qos queue wfq interface]{lang="EN-US"}]{#struct_0_14687_18620_663380534}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1742511961}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648260687}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_2123365440}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_1177864423}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x1449064851}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_536877039}

[[当前出队列类型]{style="font-family:宋体"}]{#struct_0_14687_18620_x1647933007}

[[Queue ID]{lang="EN-US"}]{#struct_0_14687_18620_x290667902}

[[队列号]{style="font-family:宋体"}]{#struct_0_14687_18620_x1886217470}

[[Queue name]{lang="EN-US"}]{#struct_0_14687_18620_398583178}

[[队列名字]{style="font-family:宋体"}]{#struct_0_14687_18620_861594139}

[[Group]{lang="EN-US"}]{#struct_0_14687_18620_x1031274820}

[[分组号，说明队列属于哪一个分组，缺省情况下，队列所属的分组号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_14687_18620_1863507129}

[[Byte-count]{lang="EN-US"}]{#struct_0_14687_18620_x1647867471}

[[队列调度权重值]{style="font-family:宋体"}]{#struct_0_14687_18620_x1787609029}

[[当前]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_1980408630}[队列调度权重的计算方式为]{style="font-family:宋体"}[Byte-count]{lang="EN-US"}

[[Min-Bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_791204375}

[[队列的最小保证带宽值]{style="font-family:宋体"}]{#struct_0_14687_18620_x628912687}

[ ]{lang="EN-US"}

::: {#-1133088567 .myid}
[]{#_Toc121389332}[]{#_Toc404792432}[]{#struct_0_14687_18620_x1648064079}[]{#_Toc292375545}[]{#_Toc263760016}[]{#_Toc226262683}[]{#_Toc198110192}[]{#_Toc342308527}[]{#_Toc342308528}[]{#_Toc290907813}

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos bandwidth queue**

------------------------------------------------------------------------

[**[qos bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_x1547967112}[命令用来配置端口队列的最小带宽保证。]{style="font-family:宋体"}

[**[undo qos bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_324501010}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2022062932}

[**[qos bandwidth queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}***[ min ]{lang="EN-US"}***[bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_1399263384}

[**[undo qos bandwidth queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x697763050}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_593152121}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x793210910}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647998543}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1880287351}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_360015845}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1374437349}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x35247874}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1874290843}

[*[queue-id]{lang="FR"}*]{#struct_0_14687_18620_106157424}[：]{style="font-family:宋体"}[队列序号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[min]{lang="EN-US"}***[ bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_2085561745}[：最小保证带宽值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。端口流量拥塞时能够保证的最小队列带宽。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647670863}

[[必须先使用]{style="font-family:宋体"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x68804222}[命令在接口上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，然后才能进行本配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1442339537}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x770351761}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[的最小保证带宽值为]{style="font-family:宋体"}[100kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_2018282908}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq weight]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos bandwidth queue 0 min 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_553389868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_1748674430}
:::

::: {#1525868130 .myid}
[]{#_Toc404792433}[]{#struct_0_14687_18620_x1647605327}[]{#_Toc292375546}[]{#_Toc263760017}[]{#_Toc226262684}[]{#_Toc198110193}[]{#_Toc290907815}

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq**

------------------------------------------------------------------------

[**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x12501130}[命令用来在接口上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，并指明当前]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列调度权重的计算方式。]{style="font-family:宋体"}

[**[undo qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_1049261327}[命令用来在接口上取消]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，恢复缺省的队列算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1834727601}

[**[qos wfq ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_x2006534423}

[**[undo qos wfq ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_x1496442001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x875550790}

[[接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_532611689}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1220557200}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1648195154}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1230968913}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x994897663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1325360318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x143439194}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_476588744}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_1990290841}[：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_2088327411}

[[必须先使用]{style="font-family:宋体"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1648129618}[命令在接口上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，然后才能进行]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1775487403}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1583250579}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，并按照权重进行计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_993032118}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq weight]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_379109043}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，并按照每次轮询可发送的字节数进行计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1588899799}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq byte-count]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1648326226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wfq interface]{lang="EN-US"}**]{#struct_0_14687_18620_512160251}
:::

::: {#-814811518 .myid}
[]{#_Toc263760018}[]{#_Toc226262685}[]{#_Toc198110194}[]{#_Toc176927363}[]{#_Toc176922428}[]{#_Toc404792434}[]{#struct_0_14687_18620_2097745111}[]{#_Toc292375547}[]{#_Toc290907817}[]{#_Toc181070974}[]{#_Toc181070975}[]{#_Toc181070978}[]{#_Toc181070979}[]{#_Toc181070980}[]{#_Toc181070981}[]{#_Toc181070982}[]{#_Toc181070983}[]{#_Toc181070984}[]{#_Toc181070985}[]{#_Toc181070986}[]{#_Toc181070987}[]{#_Toc181070988}[]{#_Toc181070989}[]{#_Toc181070990}[]{#_Toc181070991}[]{#_Toc181070993}

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq { byte-count \| weight }**

------------------------------------------------------------------------

[**[qos wfq ]{lang="EN-US"}**[{ **byte-count** \| **weight** }]{lang="EN-US"}]{#struct_0_14687_18620_x2145539619}[命令用来配置]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列或修改]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列的参数。]{style="font-family:宋体"}

[**[undo qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_2088035869}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1397273086}

[[支持]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_654244630}[分组：]{style="font-family:宋体"}

[**[qos wfq ]{lang="EN-US"}***[queue-id ]{lang="EN-US"}***[group]{lang="EN-US"}**[ { **1** \| **2** } { **byte-count** \| **weight** } *schedule-value*]{lang="EN-US"}]{#struct_0_14687_18620_x2099484214}

[**[undo qos wfq ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_157682786}

[[不支持]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_x1648260690}[分组：]{style="font-family:宋体"}

[**[qos wfq ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*[ { **byte-count** \| **weight** } *schedule-value*]{lang="EN-US"}]{#struct_0_14687_18620_1363916089}

[**[undo qos wfq ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1505620401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1253386532}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_318335381}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1421411851}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x587899190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1181674183}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1647933010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_468781449}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_432878441}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1405373653}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}**[ { **1** \| **2** }]{lang="EN-US"}]{#struct_0_14687_18620_x1090998417}[：表示该队列属于哪个]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[优先组，缺省为]{style="font-family:宋体"}[group 1]{lang="EN-US"}[。其中]{style="font-family:宋体"}[group 1]{lang="EN-US"}[表示该队列属于]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[优先组]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[group 2]{lang="EN-US"}[表示该队列属于]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[优先组]{style="font-family:宋体"}[2]{lang="EN-US"}[。各组之间执行优先级调度，由组]{style="font-family:宋体"}[1]{lang="EN-US"}[至组]{style="font-family:宋体"}[2]{lang="EN-US"}[优先级依次降低。支持的组数，根据设备类型的不同可能不同。]{style="font-family:宋体"}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_x1551252169}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_x641314561}[：表示按照权重进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[schedule-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1890238822}[：配置队列的调度权重，缺省的调度权重值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647867474}

[[必须先使用]{style="font-family:宋体"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1028094142}[命令在接口上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，然后才能进行本配置。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_818226291}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1705814024}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1839336113}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，并按照每次轮询可发送的字节数进行计算，配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[的调度权重为]{style="font-family:宋体"}[100]{lang="EN-US"}[，分组为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x748860233}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq byte-count]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq 0 group 1 byte-count 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x748351020}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wfq interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1648064082}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_1986764401}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_1888831869}
:::

::: {#-90526952 .myid}
[]{#_Toc404792435}[]{#struct_0_14687_18620_x423433461}[]{#_Toc292375548}[]{#_Toc290907819}

**硬件实现拥塞管理 \-- 加权公平队列配置命令 \-- qos wfq group sp**

------------------------------------------------------------------------

[**[qos wfq group sp]{lang="EN-US"}**]{#struct_0_14687_18620_293625647}[命令用来配置队列加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，采用严格优先级调度算法。]{style="font-family:宋体"}

[**[undo qos wfq group sp]{lang="EN-US"}**]{#struct_0_14687_18620_1159405341}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x546251390}

[**[qos wfq ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*[ **group sp**]{lang="EN-US"}]{#struct_0_14687_18620_x1647998546}

[**[undo qos wfq ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1655165058}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_338157037}

[[接口上缺省的队列算法与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_482963284}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_251267285}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_2141523890}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x494812460}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1132315279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_264041868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647670866}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x472088749}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sp]{lang="EN-US"}**]{#struct_0_14687_18620_1469734079}[：队列加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，采用严格优先级调度算法。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1467603490}

[[此命令需要在端口队列为]{style="font-family:宋体"}[WFQ]{lang="EN-US"}]{#struct_0_14687_18620_1228288185}[调度模式下使用。]{style="font-family:宋体"}

[[SP]{lang="EN-US"}]{#struct_0_14687_18620_x1186277134}[组与普通]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[优先组不同，加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组的端口队列采用严格优先级调度算法，不再采用加权轮循调度算法。调度时先调度]{style="font-family:宋体"}[SP]{lang="EN-US"}[组，然后调度其他]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[优先组。]{style="font-family:宋体"}

[[必须先使用]{style="font-family:宋体"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x240581698}[命令在接口上使能]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，然后才能进行本配置。]{style="font-family:宋体"}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_312247763}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1647605330}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1553648347}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[队列，并配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[加入]{style="font-family:宋体"}[SP]{lang="EN-US"}[组进行严格优先级调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1605514846}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq weight]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq 0 group sp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x495185885}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue wfq interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1904704661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_1323211383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x127162187}
:::

::: {#-1769892725 .myid}
[]{#_Toc404792437}[]{#struct_0_14687_18620_1948812706}[]{#_Toc384134650}[]{#_Toc323024783}[]{#_Toc323024785}

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- display qos queue gmb interface**

------------------------------------------------------------------------

[**[display qos queue gmb interface]{lang="EN-US"}**]{#struct_0_14687_18620_608262552}[命令用来显示]{style="font-family:宋体"}[接口的队列最小带宽配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_307601356}

[**[display qos queue gmb interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[interface-type]{lang="EN-US"}*[ *interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_398779783}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_731172067}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_800189141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2110475497}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1317184708}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_816502642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x323344139}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_399107463}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_2027365012}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_14687_18620_1150011626}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列最小带宽配置情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_397193336}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1759092735}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的队列最小保证带宽配置情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue gmb interface gigabitethernet 1/1]{lang="EN-US"}]{#struct_0_14687_18620_399172999}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Output queue: Guaranteed Minimum Bandwidth queuing]{lang="EN-US"}

[ Queue ID   Queue name   Min bandwidth]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 0          be           2]{lang="EN-US"}

[ 1          af1          3]{lang="EN-US"}

[ 2          af2          30]{lang="EN-US"}

[ 3          af3          10]{lang="EN-US"}

[ 4          af4          10]{lang="EN-US"}

[ 5          ef           10]{lang="EN-US"}

[ 6          cs6          10]{lang="EN-US"}

[ 7          cs7          strict]{lang="EN-US"}

[[表5-5 ]{lang="EN-US"}[display qos queue gmb interface]{lang="EN-US"}]{#struct_0_14687_18620_1731737300}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_901915474}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_398583176}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_398452104}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_398517640}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_398910856}

[[Output queue]{lang="EN-US"}]{#struct_0_14687_18620_398714248}

[[当前出队列类型]{style="font-family:宋体"}]{#struct_0_14687_18620_399107464}

[[Queue ID]{lang="EN-US"}]{#struct_0_14687_18620_399173000}

[[队列]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14687_18620_x4701348}

[[Queue name]{lang="EN-US"}]{#struct_0_14687_18620_x4832420}

[[队列名字]{style="font-family:宋体"}]{#struct_0_14687_18620_x4439204}

[[Min bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_x4373668}

[[队列的最小保证带宽值]{style="font-family:宋体"}]{#struct_0_14687_18620_x4570276}

[ ]{lang="EN-US"}

::: {#-1690670925 .myid}
[]{#_Toc404792438}[]{#struct_0_14687_18620_x4504740}[]{#_Toc384134648}[]{#_Toc373747468}[]{#_Toc384134651}

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- qos gmb**

------------------------------------------------------------------------

[**[qos gmb]{lang="EN-US"}**]{#struct_0_14687_18620_1752318304}[命令用来]{style="font-family:宋体"}[使能接口的]{style="font-family:宋体"}[GMB]{lang="EN-US"}[调度模式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos gmb**]{lang="EN-US"}]{#struct_0_14687_18620_x1400190453}[命令用来取消]{style="font-family:宋体"}[接口的]{style="font-family:宋体"}[GMB]{lang="EN-US"}[调度模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x120184401}

[**[qos gmb ]{lang="EN-US"}**]{#struct_0_14687_18620_149892713}

[**[undo qos gmb]{lang="EN-US"}**]{#struct_0_14687_18620_898812960}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_634020061}

[[没有配置]{style="font-family:宋体"}[GMB]{lang="EN-US"}]{#struct_0_14687_18620_x4177060}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1197417191}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x539471492}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1320718848}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x667453291}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1012236515}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x907059488}

[[必须先使用]{style="font-family:宋体"}**[qos gmb]{lang="EN-US"}**]{#struct_0_14687_18620_x652015127}[命令在接口上使能]{style="font-family:宋体"}[GMB]{lang="EN-US"}[模式，才能进行]{style="font-family:宋体"}[队列的最小带宽保证]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x4111524}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x795735385}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[GMB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1624212512}

[]{#_Toc361324561}[[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}]{#_Toc350844407}

[\[Sysname-GigabitEthernet1/0/1\] qos gmb]{lang="EN-US"}
:::

::: {#-383551948 .myid}
[]{#struct_0_14687_18620_x751428264}[]{#_Toc373747469}[]{#_Toc404792439}[]{#_Toc384134649}

**硬件实现拥塞管理 \-- 最小带宽保证队列配置命令 \-- qos gmb min-bandwidth**

------------------------------------------------------------------------

[**[qos gmb min-bandwidth]{lang="EN-US"}**]{#struct_0_14687_18620_1074370406}[命令用来]{style="font-family:宋体"}[配置指定队列的最小带宽保证。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos gmb** ]{lang="EN-US"}]{#struct_0_14687_18620_1196373290}[命令用来]{style="font-family:宋体"}[恢复缺省配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_386267896}

[**[qos gmb]{lang="EN-US"}**[ *queue-id* **min-bandwidth** { **percent** *percent* \| **strict** }]{lang="EN-US"}]{#struct_0_14687_18620_x4701347}

[**[undo qos gmb ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1277364693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_550346100}

[[没有配置队列最小带宽保证。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1545172988}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1099737025}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1786093588}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1131894618}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1680653914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x4635811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x362039517}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1836388318}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[percent]{lang="EN-US"}**[ *percent*]{lang="EN-US"}]{#struct_0_14687_18620_892568186}[：以百分比的形式为指定队列配置最小保证带宽。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_14687_18620_1997455816}[：表示不指定具体的带宽，此队列占用自己所需要的带宽，剩余带宽由其他队列分配。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_2012198393}

[[必须先使用]{style="font-family:宋体"}]{#struct_0_14687_18620_x4832419}**[qos gmb]{lang="EN-US"}**[命令在接口上使能]{style="font-family:宋体"}[GMB]{lang="EN-US"}[模式，然后才能进行本配置。]{style="font-family:宋体"}

[[任意队列都可以配置成]{style="font-family:宋体"}[strict]{lang="EN-US"}]{#struct_0_14687_18620_1510595270}[，但一个接口只能有一个队列为]{style="font-family:宋体"}[strict]{lang="EN-US"}[。]{style="font-family:宋体"}*[queue-id]{lang="EN-US"}*[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x543923633}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1399364888}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上为队列]{style="font-family:宋体"}[0]{lang="EN-US"}[设置]{style="font-family:宋体"}[10%]{lang="EN-US"}[的最小保证带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_414460724}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos gmb]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos gmb 0 min-bandwidth percent 10]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1929320306}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上为队列]{style="font-family:宋体"}[1]{lang="EN-US"}[设置]{style="font-family:宋体"}[strict]{lang="EN-US"}[模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x4766883}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos gmb]{lang="EN-US"}

[ \[Sysname-GigabitEthernet1/0/1\] qos gmb 1 min-bandwidth strict]{lang="EN-US"}
:::

::::: {#464393208 .myid}
[]{#_Toc404792441}[]{#struct_0_14687_18620_x883783687}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- bandwidth queue**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_1226821754}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_1756997494}
:::

[ ]{lang="EN-US"}

[**[bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_x787221581}[命令用来配置队列调度策略下队列的最小带宽保证。]{style="font-family:宋体"}

[**[undo bandwidth queue]{lang="EN-US"}**]{#struct_0_14687_18620_1845099668}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_665214287}

[**[bandwidth queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}***[ min ]{lang="EN-US"}***[bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_1641750007}

[**[undo bandwidth queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x747486348}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_279015727}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_712360032}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1585060150}

[[队列调度策略视图]{style="font-family:宋体"}]{#struct_0_14687_18620_507410294}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1878913770}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1287068214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x924857588}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_362843465}

[*[queue-id]{lang="FR"}*]{#struct_0_14687_18620_971135354}[：]{style="font-family:宋体"}[队列序号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[min]{lang="EN-US"}***[ bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1809463934}[：最小保证带宽值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。端口流量拥塞时能够保证的最小队列带宽。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1798045501}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_335372088}[配置队列]{style="font-family:宋体"}[1]{lang="EN-US"}[的最小保证带宽为]{style="font-family:宋体"}[128kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_231961560}

[\[Sysname\] qos qmprofile myprofile]{lang="EN-US"}

[\[Sysname-qmprofile-myprofile\] bandwidth queue 1 min 128]{lang="EN-US"}
:::::

::: {#1265496337 .myid}
[]{#_Toc404792442}[]{#struct_0_14687_18620_691345388}[]{#_Toc292375551}[]{#_Toc263760025}[]{#_Toc226262687}[]{#_Toc375644766}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- display qos qmprofile configuration**

------------------------------------------------------------------------

[**[display qos qmprofile configuration]{lang="EN-US"}**]{#struct_0_14687_18620_962234707}[命令用来显示队列调度策略的配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_583392624}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_477108694}

[**[display qos qmprofile ]{lang="EN-US"}**[\[ **four-queue** \] **configuration** \[ *profile-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_x307897439}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x500740168}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos qmprofile ]{lang="EN-US"}**[\[ **four-queue** \] **configuration** \[ *profile-name* \]]{lang="EN-US"}[ \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_1306063238}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1648129617}[模式：]{style="font-family:宋体"}

[**[display qos qmprofile ]{lang="EN-US"}**[\[ **four-queue** \] **configuration** \[ *profile-name* \]]{lang="EN-US"}[ \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_14687_18620_x1015972516}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1049729228}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_242965738}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_689615614}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x480304127}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_2092111607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_467195696}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x1648326225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_915444778}

[**[four-queue]{lang="EN-US"}**]{#struct_0_14687_18620_451423264}[：显示四队列调度策略的配置情况，若未指定该参数，则显示八队列调度策略的配置情况。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_1306530288}[：队列调度策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则显示所有队列调度策略的配置情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_277553999}[：显示指定单板的队列调度策略的配置情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的队列调度策略的配置情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x2074669266}[：显示指定成员设备的队列调度策略的配置情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示主用设备的队列调度策略的配置情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_986118726}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的队列调度策略的配置情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的队列调度策略的配置情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1226956488}[：显示指定成员设备上指定单板的队列调度策略的配置情况。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的队列调度策略的配置情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x2082823692}[：]{style="font-family:宋体"}[显示指定单板的队列调度策略的配置情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的队列调度策略的配置情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_14687_18620_17368873}[：指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[号。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x18791930}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1262283502}[显示队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[的配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos qmprofile configuration myprofile]{lang="EN-US"}]{#struct_0_14687_18620_x1647933009}

[Queue management profile: myprofile (ID 1)]{lang="FR"}

[ Queue ID    Type    Group    ]{lang="FR"}[Schedule  Schedule  Min           Max         Service]{lang="EN-US"}

[                              unit      value     bandwidth     bandwidth   type]{lang="EN-US"}[ ]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="FR"}

[ be          SP      N/A      ]{lang="FR"}[N/A        N/A      64            10000       STB]{lang="PT-BR"}

[ af1         WFQ     1        byte-count]{lang="FR"}[ ]{lang="FR"}[N/A      100           10000       STB]{lang="PT-BR"}

[ ]{lang="FR"}[af2         WRR     1        weight     100      100           10000       VoIP]{lang="NL"}

[ af3         WRR     1        weight     100      100           10000       HSI]{lang="NL"}

[ af4         WRR     1        weight     50       100           10000       HSI]{lang="NL"}

[ ]{lang="NL"}[ef          WRR     1        weight     50       100           10000       STB]{lang="PT-BR"}

[ cs6         WRR     1        weight     100      100           10000       STB]{lang="PT-BR"}

[ cs7         WRR     1        weight     50       100           10000       HSI]{lang="PT-BR"}

[\# ]{lang="EN-US"}[显示所有四队列调度策略的配置情况。]{style="font-family:宋体"}

[\<Sysname\> display qos qmprofile four-queue configuration ]{lang="EN-US"}

[Queue management profile: b (ID 1) four-queue]{lang="FR"}

[ Queue ID  Type  Group  Schedule   Schedule  Min           Max          Service]{lang="FR"}

[                        unit       value     bandwidth     bandwidth    type]{lang="FR"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="FR"}

[ be        SP    N/A    N/A        N/A       64            64           HSI]{lang="FR"}

[ af1       SP    N/A    N/A        N/A       64            64           HSI]{lang="FR"}

[ af2       SP    N/A    N/A        N/A       64            64           HSI]{lang="FR"}

[ ef        WRR   2      byte-count 64        100           1000         VoIP]{lang="FR"}

[[表5-6 ]{lang="EN-US"}[display qos qmprofile configuration]{lang="EN-US"}]{#struct_0_14687_18620_x1453467316}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1743062777}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_496506660}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_552073835}

[[Queue management profile]{lang="EN-US"}]{#struct_0_14687_18620_988530781}

[[队列调度策略名称]{style="font-family:宋体"}]{#struct_0_14687_18620_1894314863}

[[Queue ID]{lang="EN-US"}]{#struct_0_14687_18620_x1647867473}

[[队列号]{style="font-family:宋体"}]{#struct_0_14687_18620_x624809615}

[[Type]{lang="EN-US"}]{#struct_0_14687_18620_x1548281009}

[[队列调度类型，包括]{style="font-family:宋体"}[SP]{lang="EN-US"}]{#struct_0_14687_18620_546166921}[（严格优先级）、]{style="font-family:宋体"}[WRR]{lang="EN-US"}[（加权轮询调度）、]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[（加权公平队列）]{style="font-family:宋体"}

[[对队列调度类型的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_14687_18620_1862275920}

[[Group]{lang="EN-US"}]{#struct_0_14687_18620_x1648064081}

[[优先组，]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_14687_18620_x1904918368}[表示无效]{style="font-family:宋体"}

[[Schedule unit]{lang="FR"}]{#struct_0_14687_18620_x1493180465}

[[队列调度单位，包括]{style="font-family:宋体"}[weight]{lang="EN-US"}]{#struct_0_14687_18620_x1493114929}[和]{style="font-family:宋体"}[byte-count]{lang="FR"}[，]{style="font-family:宋体"}[N/A]{lang="EN-US"}[表示无效]{style="font-family:宋体"}

[[Schedule vlaue]{lang="FR"}]{#struct_0_14687_18620_x1493704754}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[队列调度单位为]{style="font-family:宋体"}]{#struct_0_14687_18620_x1493835826}[weight]{lang="EN-US"}[时，表示权重值]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[队列调度单位为]{style="font-family:宋体"}]{#struct_0_14687_18620_x1493770290}[byte-count]{lang="FR"}[时，表示字节个数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14687_18620_x1493442610}[表示无效]{lang="EN-US" style="font-family:宋体"}

[[Min Bandwidth]{lang="FR"}]{#struct_0_14687_18620_278950191}

[[最小保证带宽]{style="font-family:宋体"}]{#struct_0_14687_18620_1177673647}

[[Max bandwidth]{lang="EN-US"}]{#struct_0_14687_18620_x1504891874}

[[最大带宽值]{style="font-family:宋体"}]{#struct_0_14687_18620_x1504891871}

[[Service type]{lang="EN-US"}]{#struct_0_14687_18620_x1504891872}

[[服务类型，包括]{style="font-family:宋体"}[HSI]{lang="EN-US"}]{#struct_0_14687_18620_x1504891869}[、]{style="font-family:宋体"}[STB]{lang="EN-US"}[、]{style="font-family:宋体"}[VoIP]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#-1666347074 .myid}
[]{#_Toc404792443}[]{#struct_0_14687_18620_x717098708}[]{#_Toc292375552}[]{#_Toc263760026}[]{#_Toc226262688}[]{#_Toc342308535}[]{#_Toc342308536}[]{#_Toc342308537}[]{#_Toc290907826}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- display qos qmprofile interface**

------------------------------------------------------------------------

[**[display qos qmprofile interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1647998545}[命令用来显示接口的队列调度策略的配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1073718297}

[**[display qos qmprofile interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1399189171}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1285872419}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x73800346}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1094298041}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1964933569}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_2135666808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1647670865}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x875373276}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_537884352}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_973838136}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列调度策略的配置情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_481214124}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x830309598}[显示指定接口的队列调度策略的配置情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos qmprofile interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14687_18620_173478520}

[Interface: GigabitEthernet1/]{lang="FR"}[0/]{lang="EN-US"}[1]{lang="FR"}

[ Queue management profile: myprofile]{lang="FR"}

[[表5-7 ]{lang="EN-US"}[display qos qmprofile interface]{lang="EN-US"}]{#struct_0_14687_18620_x1647605329}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1736877497}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1531530904}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x471531405}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_1204915653}

[[接口名称]{style="font-family:宋体"}]{#struct_0_14687_18620_987130319}

[[Queue management profile]{lang="EN-US"}]{#struct_0_14687_18620_1584383958}

[[队列调度策略名称]{style="font-family:宋体"}]{#struct_0_14687_18620_x82111209}

[ ]{lang="FR"}

::: {#923933844 .myid}
[]{#_Toc404792444}[]{#struct_0_14687_18620_1619782148}[]{#_Toc292375553}[]{#_Toc263760027}[]{#_Toc226262689}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos apply qmprofile(interface view)**

------------------------------------------------------------------------

[**[qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_x1009837175}[命令用来在接口上应用队列调度策略。]{style="font-family:宋体"}

[**[undo qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_x629317651}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2111212662}

[**[qos apply qmprofile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_x218624218}

[**[undo qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_x330717878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1008237340}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x82045673}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x306833373}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x113148600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1964542222}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1895875127}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x735466709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1216415396}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_1558157285}[：队列调度策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82242281}

[[每个接口只能应用一个队列调度策略。]{style="font-family:宋体"}]{#struct_0_14687_18620_x432280947}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1243734509}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_196178185}[在接口上应用队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_897239051}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos apply qmprofile myprofile]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_2057260784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos qmprofile interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1717692330}
:::

::: {#654073819 .myid}
[]{#_Toc404792445}[]{#struct_0_14687_18620_x1504891867}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos apply qmprofile(session-group-profile view)**

------------------------------------------------------------------------

[**[qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_x708258074}[命令用来在]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[上应用队列调度策略。]{style="font-family:宋体"}

[**[undo qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_561026450}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x55261490}

[**[qos apply qmprofile ]{lang="EN-US"}**[\[ **four-queue** \] *profile-name*]{lang="EN-US"}]{#struct_0_14687_18620_x1555226530}

[**[undo qos apply qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_1054943525}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x67910121}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x680948385}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1105485698}

[[Session Group Profile]{lang="EN-US"}]{#struct_0_14687_18620_x1391836655}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_634208743}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1555488589}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x223622804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x280696112}

[**[four-queue]{lang="EN-US"}**]{#struct_0_14687_18620_1731723315}[：表示]{style="font-family:宋体"}[在]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[上应用四队列调度策略。]{style="font-family:宋体"}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_1053044321}[：队列调度策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_485315239}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[每个]{lang="EN-US" style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}]{#struct_0_14687_18620_x2146032002}[只能应用一个队列调度策略。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[Session Group Profile]{lang="EN-US"}]{#struct_0_14687_18620_x1655911159}[上可以应用四队列或八队列的队列调度策略。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_497570938}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_773457646}[在]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[上应用四队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1504891868}

[\[Sysname\] user-profile a123 type session-group]{lang="EN-US"}

[\[Sysname-session-group]{lang="EN-US"}[-profile]{lang="PT-BR"}[-a123\] qos apply qmprofile four-queue myprofile]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1111542601}[在]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[上应用八队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1683962668}

[\[Sysname\] user-profile a123 type session-group ]{lang="EN-US"}

[\[Sysname-session-group]{lang="EN-US"}[-profile]{lang="PT-BR"}[-a123\] qos apply  qmprofile myprofile ]{lang="EN-US"}
:::

::: {#-1766015149 .myid}
[]{#_Toc404792446}[]{#struct_0_14687_18620_x82176745}[]{#_Toc292375554}[]{#_Toc263760028}[]{#_Toc226262690}[]{#_Toc380516348}[]{#_Toc380516532}[]{#_Toc290907829}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- qos qmprofile**

------------------------------------------------------------------------

[]{#struct_0_14687_18620_1243253981}[**[qos qmprofile]{lang="EN-US"}**]{#OLE_LINK1}[命令用来创建用户自定义的队列调度策略，并进入相应的队列调度策略视图。]{style="font-family:宋体"}

[**[undo qos qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_1781387125}[命令用来删除用户自定义的队列调度策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x570043037}

[**[qos qmprofile ]{lang="EN-US"}***[profile-name ]{lang="EN-US"}*[\[ **type four-queue** \]]{lang="EN-US"}]{#struct_0_14687_18620_x2140965320}

[**[undo qos qmprofile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_x710494655}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1310237965}

[[不存在用户自定义的队列调度策略。]{style="font-family:宋体"}]{#struct_0_14687_18620_x361793020}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81849065}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1530974880}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_427573647}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1049811980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1302087823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1910174461}

[*[profile-name]{lang="EN-US"}*]{#struct_0_14687_18620_1571918222}[：队列调度策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[type four-queue]{lang="EN-US"}**]{#struct_0_14687_18620_1731395635}[：指定创建的队列调度策略类型为四队列调度策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_220172041}

[[不能删除已经应用到接口的队列调度策略，必须先在应用的接口上取消对该队列调度策略的应用，然后再删除该队列调度策略。]{style="font-family:宋体"}]{#struct_0_14687_18620_x81783529}

[[不能删除已经应用到]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}]{#struct_0_14687_18620_1864338714}[的队列调度策略，必须先在应用的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[上取消对该队列调度策略的应用，然后再删除该队列调度策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_2056663289}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1770306297}[创建自定义的队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并进入队列调度策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1915424574}

[\[Sysname\] qos qmprofile myprofile]{lang="EN-US"}

[\[Sysname-qmprofile-myprofile\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2005643032}[创建自定义的四队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并进入四队列调度策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1963547889}

[\[Sysname\] qos qmprofile myprofile type four-queue]{lang="EN-US"}

[\[Sysname-qmprofile-four-queue-myprofile\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_950551386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos qmprofile interface]{lang="EN-US"}**]{#struct_0_14687_18620_310299857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[queue]{lang="EN-US"}**]{#struct_0_14687_18620_1420148512}
:::

::: {#-1985250189 .myid}
[]{#_Toc404792447}[]{#struct_0_14687_18620_x81980137}[]{#_Toc292375555}[]{#_Toc263760029}[]{#_Toc226262691}[]{#_Toc380516350}[]{#_Toc380516534}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- queue**

------------------------------------------------------------------------

[**[queue]{lang="EN-US"}**]{#struct_0_14687_18620_x1242669437}[命令用来配置队列调度参数。]{style="font-family:宋体"}

[**[undo queue]{lang="EN-US"}**]{#struct_0_14687_18620_1004551900}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x777349150}

[**[queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **sp** \| **wfq**]{lang="EN-US"}[ \[ **group** *group-id* \] { **weight \| byte-count** } *schedule-value* \| **wrr** **group** *group-id* { **weight \| byte-count** } *schedule-value* } \[ **max-bandwidth** *bandwidth-value* \| **service-type** *service-type-value* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x276567867}

[**[undo queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x202487447}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1605349577}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_181910090}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81914601}

[[队列调度策略视图]{style="font-family:宋体"}]{#struct_0_14687_18620_301710161}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1533179926}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_500341851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x712394687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1952406337}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1339594353}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sp]{lang="EN-US"}**]{#struct_0_14687_18620_1036629780}[：配置队列为严格优先级调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x81586921}[：配置队列为加权公平调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[wrr]{lang="EN-US"}**]{#struct_0_14687_18620_573375325}[：配置队列为加权轮询调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}***[ group-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1072400037}[：优先组号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_72444727}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_72248119}[：表示按照权重新进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[schedule]{lang="EN-US"}[-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1872442491}[：]{style="font-family:宋体"}[配置队列的]{style="font-family:宋体"}[调度权重。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[max-bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_14687_18620_69086237}[：最大限制带宽]{style="font-family:宋体"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-type ]{lang="EN-US"}***[service-type-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1074749785}[：服务类型。包括]{style="font-family:宋体"}[HSI]{lang="EN-US"}[（]{style="font-family:宋体"}[High Speed Internet]{lang="EN-US"}[，高速上网）、]{style="font-family:宋体"}[STB]{lang="EN-US"}[（]{style="font-family:宋体"}[Set Top Box]{lang="EN-US"}[，机顶盒）、]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[（]{style="font-family:宋体"}[Voice Over Internet Protocol]{lang="EN-US"}[，在]{style="font-family:宋体"}[IP]{lang="EN-US"}[网络上传送语音）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1735421353}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x722243957}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x800170365}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1901588697}[创建自定义的队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[为严格优先级调度。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x81521385}

[\[Sysname\] qos qmprofile myprofile]{lang="EN-US"}

[\[Sysname-qmprofile-myprofile\] queue 0 sp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1452766245}[创建自定义的队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并配置队列]{style="font-family:宋体"}[1]{lang="EN-US"}[为加权轮询调度，权重为]{style="font-family:宋体"}[100]{lang="EN-US"}[，分组为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1369598226}

[\[Sysname\] qos qmprofile myprofile]{lang="EN-US"}

[\[Sysname-qmprofile-myprofile\] queue 1 wrr group 1 weight 100]{lang="EN-US"}[]{#_Toc160880913}[]{#_Toc161027172}[]{#_Toc160880914}[]{#_Toc161027173}[]{#_Toc160880915}[]{#_Toc161027174}[]{#_Toc160880916}[]{#_Toc161027175}[]{#_Toc160880917}[]{#_Toc161027176}[]{#_Toc160880918}[]{#_Toc161027177}[]{#_Toc160880919}[]{#_Toc161027178}[]{#_Toc160880920}[]{#_Toc161027179}[]{#_Toc160880921}[]{#_Toc161027180}[]{#_Toc160880922}[]{#_Toc161027181}[]{#_Toc160880923}[]{#_Toc161027182}[]{#_Toc160880924}[]{#_Toc161027183}[]{#_Toc160880925}[]{#_Toc161027184}[]{#_Toc160880926}[]{#_Toc161027185}[]{#_Toc160880927}[]{#_Toc161027186}[]{#_Toc160880928}[]{#_Toc161027187}[]{#_Toc160880929}[]{#_Toc161027188}[]{#_Toc160880930}[]{#_Toc161027189}[]{#_Toc160880931}[]{#_Toc161027190}[]{#_Toc160880932}[]{#_Toc161027191}[]{#_Toc160880933}[]{#_Toc161027192}[]{#_Toc160880935}[]{#_Toc161027194}[]{#_Toc160880936}[]{#_Toc161027195}[]{#_Toc160880937}[]{#_Toc161027196}[]{#_Toc160880939}[]{#_Toc161027198}[]{#_Toc160880940}[]{#_Toc161027199}[]{#_Toc160880941}[]{#_Toc161027200}[]{#_Toc160880942}[]{#_Toc161027201}[]{#_Toc160880943}[]{#_Toc161027202}[]{#_Toc160880944}[]{#_Toc161027203}[]{#_Toc160880945}[]{#_Toc161027204}[]{#_Toc160880946}[]{#_Toc161027205}[]{#_Toc160880947}[]{#_Toc161027206}[]{#_Toc160880948}[]{#_Toc161027207}[]{#_Toc160880949}[]{#_Toc161027208}[]{#_Toc160880950}[]{#_Toc161027209}[]{#_Toc160880951}[]{#_Toc161027210}[]{#_Toc160880952}[]{#_Toc161027211}[]{#_Toc160880953}[]{#_Toc161027212}[]{#_Toc160880954}[]{#_Toc161027213}[]{#_Toc160880955}[]{#_Toc161027214}[]{#_Toc160880957}[]{#_Toc161027216}[]{#_Toc160880959}[]{#_Toc161027218}[]{#_Toc160880960}[]{#_Toc161027219}[]{#_Toc160880961}[]{#_Toc161027220}[]{#_Toc160880963}[]{#_Toc161027222}[]{#_Toc160880964}[]{#_Toc161027223}[]{#_Toc160880965}[]{#_Toc161027224}[]{#_Toc160880966}[]{#_Toc161027225}[]{#_Toc160880967}[]{#_Toc161027226}[]{#_Toc160880968}[]{#_Toc161027227}[]{#_Toc160880969}[]{#_Toc161027228}[]{#_Toc160880970}[]{#_Toc161027229}[]{#_Toc160880972}[]{#_Toc161027231}[]{#_Toc160880973}[]{#_Toc161027232}[]{#_Toc160880974}[]{#_Toc161027233}[]{#_Toc160880975}[]{#_Toc161027234}[]{#_Toc160880976}[]{#_Toc161027235}[]{#_Toc160880977}[]{#_Toc161027236}[]{#_Toc160880978}[]{#_Toc161027237}[]{#_Toc160880979}[]{#_Toc161027238}[]{#_Toc160880980}[]{#_Toc161027239}[]{#_Toc160880981}[]{#_Toc161027240}[]{#_Toc160880982}[]{#_Toc161027241}[]{#_Toc160880983}[]{#_Toc161027242}[]{#_Toc160880984}[]{#_Toc161027243}[]{#_Toc160880989}[]{#_Toc161027248}[]{#_Toc160880993}[]{#_Toc161027252}[]{#_Toc160881018}[]{#_Toc161027277}[]{#_Toc146354038}[]{#_Toc146354039}[]{#_Toc146354040}[]{#_Toc146354041}[]{#_Toc146354042}[]{#_Toc146354043}[]{#_Toc146354044}[]{#_Toc146354045}[]{#_Toc146354046}[]{#_Toc146354047}[]{#_Toc146354048}[]{#_Toc146354049}[]{#_Toc146354050}[]{#_Toc146354051}[]{#_Toc146354054}[]{#_Toc146354055}[]{#_Toc146354071}[]{#_Toc160881019}[]{#_Toc161027278}[]{#_Toc160881020}[]{#_Toc161027279}[]{#_Toc160881021}[]{#_Toc161027280}[]{#_Toc160881022}[]{#_Toc161027281}[]{#_Toc160881023}[]{#_Toc161027282}[]{#_Toc160881024}[]{#_Toc161027283}[]{#_Toc160881025}[]{#_Toc161027284}[]{#_Toc160881026}[]{#_Toc161027285}[]{#_Toc160881027}[]{#_Toc161027286}[]{#_Toc160881028}[]{#_Toc161027287}[]{#_Toc160881029}[]{#_Toc161027288}[]{#_Toc160881031}[]{#_Toc161027290}[]{#_Toc172464011}[]{#_Toc172464906}[]{#_Toc172464012}[]{#_Toc172464907}[]{#_Toc172464013}[]{#_Toc172464908}[]{#_Toc172464014}[]{#_Toc172464909}[]{#_Toc172464015}[]{#_Toc172464910}[]{#_Toc172464016}[]{#_Toc172464911}[]{#_Toc172464017}[]{#_Toc172464912}[]{#_Toc172464019}[]{#_Toc172464914}[]{#_Toc172464020}[]{#_Toc172464915}[]{#_Toc172464021}[]{#_Toc172464916}[]{#_Toc172464022}[]{#_Toc172464917}[]{#_Toc172464023}[]{#_Toc172464918}[]{#_Toc172464024}[]{#_Toc172464919}[]{#_Toc172464025}[]{#_Toc172464920}[]{#_Toc172464026}[]{#_Toc172464921}[]{#_Toc172464027}[]{#_Toc172464922}[]{#_Toc172464028}[]{#_Toc172464923}[]{#_Toc172464029}[]{#_Toc172464924}[]{#_Toc172464030}[]{#_Toc172464925}[]{#_Toc172464035}[]{#_Toc172464930}[]{#_Toc172464056}[]{#_Toc172464951}[]{#_Toc172464057}[]{#_Toc172464952}[]{#_Toc172464060}[]{#_Toc172464955}[]{#_Toc172464062}[]{#_Toc172464957}[]{#_Toc172464063}[]{#_Toc172464958}[]{#_Toc172464068}[]{#_Toc172464963}[]{#_Toc172464070}[]{#_Toc172464965}[]{#_Toc172464076}[]{#_Toc172464971}[]{#_Toc172464077}[]{#_Toc172464972}[]{#_Toc172464127}[]{#_Toc172465022}[]{#_Toc172464128}[]{#_Toc172465023}[]{#_Toc172464129}[]{#_Toc172465024}[]{#_Toc172464130}[]{#_Toc172465025}[]{#_Toc172464131}[]{#_Toc172465026}[]{#_Toc172464132}[]{#_Toc172465027}[]{#_Toc172464133}[]{#_Toc172465028}[]{#_Toc172464134}[]{#_Toc172465029}[]{#_Toc172464135}[]{#_Toc172465030}[]{#_Toc172464136}[]{#_Toc172465031}[]{#_Toc172464137}[]{#_Toc172465032}[]{#_Toc172464138}[]{#_Toc172465033}[]{#_Toc172464139}[]{#_Toc172465034}[]{#_Toc172464140}[]{#_Toc172465035}[]{#_Toc172464141}[]{#_Toc172465036}[]{#_Toc172464142}[]{#_Toc172465037}[]{#_Toc172464143}[]{#_Toc172465038}[]{#_Toc172464144}[]{#_Toc172465039}[]{#_Toc172464145}[]{#_Toc172465040}[]{#_Toc172464146}[]{#_Toc172465041}[]{#_Toc172464147}[]{#_Toc172465042}[]{#_Toc172464148}[]{#_Toc172465043}[]{#_Toc172464152}[]{#_Toc172465047}[]{#_Toc172464153}[]{#_Toc172465048}[]{#_Toc172464154}[]{#_Toc172465049}[]{#_Toc172464155}[]{#_Toc172465050}[]{#_Toc172464156}[]{#_Toc172465051}[]{#_Toc172464157}[]{#_Toc172465052}[]{#_Toc172464158}[]{#_Toc172465053}[]{#_Toc172464159}[]{#_Toc172465054}[]{#_Toc172464160}[]{#_Toc172465055}[]{#_Toc172464161}[]{#_Toc172465056}[]{#_Toc172464162}[]{#_Toc172465057}[]{#_Toc172464163}[]{#_Toc172465058}[]{#_Toc160881037}[]{#_Toc161027296}[]{#_Toc160881038}[]{#_Toc161027297}[]{#_Toc160881039}[]{#_Toc161027298}[]{#_Toc160881040}[]{#_Toc161027299}[]{#_Toc160881041}[]{#_Toc161027300}[]{#_Toc160881042}[]{#_Toc161027301}[]{#_Toc160881043}[]{#_Toc161027302}[]{#_Toc160881044}[]{#_Toc161027303}[]{#_Toc160881045}[]{#_Toc161027304}[]{#_Toc160881046}[]{#_Toc161027305}[]{#_Toc160881047}[]{#_Toc161027306}[]{#_Toc160881048}[]{#_Toc161027307}[]{#_Toc160881049}[]{#_Toc161027308}[]{#_Toc160881050}[]{#_Toc161027309}[]{#_Toc160881051}[]{#_Toc161027310}[]{#_Toc160881052}[]{#_Toc161027311}[]{#_Toc160881053}[]{#_Toc161027312}[]{#_Toc160881054}[]{#_Toc161027313}[]{#_Toc160881055}[]{#_Toc161027314}[]{#_Toc160881057}[]{#_Toc161027316}[]{#_Toc160881058}[]{#_Toc161027317}[]{#_Toc160881059}[]{#_Toc161027318}[]{#_Toc160881061}[]{#_Toc161027320}[]{#_Toc160881062}[]{#_Toc161027321}[]{#_Toc160881063}[]{#_Toc161027322}[]{#_Toc160881064}[]{#_Toc161027323}[]{#_Toc160881065}[]{#_Toc161027324}[]{#_Toc160881066}[]{#_Toc161027325}[]{#_Toc160881067}[]{#_Toc161027326}[]{#_Toc160881068}[]{#_Toc161027327}[]{#_Toc160881069}[]{#_Toc161027328}[]{#_Toc160881070}[]{#_Toc161027329}[]{#_Toc160881074}[]{#_Toc161027333}[]{#_Toc160881075}[]{#_Toc161027334}[]{#_Toc160881096}[]{#_Toc161027355}[]{#_Toc160881097}[]{#_Toc161027356}[]{#_Toc160881100}[]{#_Toc161027359}[]{#_Toc160881102}[]{#_Toc161027361}[]{#_Toc160881103}[]{#_Toc161027362}[]{#_Toc160881108}[]{#_Toc161027367}[]{#_Toc160881110}[]{#_Toc161027369}[]{#_Toc160881116}[]{#_Toc161027375}[]{#_Toc160881117}[]{#_Toc161027376}[]{#_Toc160881155}[]{#_Toc161027414}[]{#_Toc160881157}[]{#_Toc161027416}[]{#_Toc160881158}[]{#_Toc161027417}[]{#_Toc160881159}[]{#_Toc161027418}[]{#_Toc160881160}[]{#_Toc161027419}[]{#_Toc160881161}[]{#_Toc161027420}[]{#_Toc160881162}[]{#_Toc161027421}[]{#_Toc160881163}[]{#_Toc161027422}[]{#_Toc160881164}[]{#_Toc161027423}[]{#_Toc160881165}[]{#_Toc161027424}[]{#_Toc160881166}[]{#_Toc161027425}[]{#_Toc172464165}[]{#_Toc172465060}[]{#_Toc172464166}[]{#_Toc172465061}[]{#_Toc172464167}[]{#_Toc172465062}[]{#_Toc172464168}[]{#_Toc172465063}[]{#_Toc172464169}[]{#_Toc172465064}[]{#_Toc172464170}[]{#_Toc172465065}[]{#_Toc172464171}[]{#_Toc172465066}[]{#_Toc172464173}[]{#_Toc172465068}[]{#_Toc172464174}[]{#_Toc172465069}[]{#_Toc172464175}[]{#_Toc172465070}[]{#_Toc172464176}[]{#_Toc172465071}[]{#_Toc172464177}[]{#_Toc172465072}[]{#_Toc172464178}[]{#_Toc172465073}[]{#_Toc172464179}[]{#_Toc172465074}[]{#_Toc172464180}[]{#_Toc172465075}[]{#_Toc172464181}[]{#_Toc172465076}[]{#_Toc172464182}[]{#_Toc172465077}[]{#_Toc172464183}[]{#_Toc172465078}[]{#_Toc172464184}[]{#_Toc172465079}[]{#_Toc172464200}[]{#_Toc172465095}[]{#_Toc172464201}[]{#_Toc172465096}[]{#_Toc172464250}[]{#_Toc172465145}[]{#_Toc172464251}[]{#_Toc172465146}[]{#_Toc172464252}[]{#_Toc172465147}[]{#_Toc172464253}[]{#_Toc172465148}[]{#_Toc172464254}[]{#_Toc172465149}[]{#_Toc172464255}[]{#_Toc172465150}[]{#_Toc172464256}[]{#_Toc172465151}[]{#_Toc172464257}[]{#_Toc172465152}[]{#_Toc172464258}[]{#_Toc172465153}[]{#_Toc172464259}[]{#_Toc172465154}[]{#_Toc172464260}[]{#_Toc172465155}[]{#_Toc172464261}[]{#_Toc172465156}[]{#_Toc172464262}[]{#_Toc172465157}[]{#_Toc172464263}[]{#_Toc172465158}[]{#_Toc172464264}[]{#_Toc172465159}[]{#_Toc172464265}[]{#_Toc172465160}[]{#_Toc172464266}[]{#_Toc172465161}[]{#_Toc172464268}[]{#_Toc172465163}[]{#_Toc172464270}[]{#_Toc172465165}[]{#_Toc172464272}[]{#_Toc172465167}[]{#_Toc172464273}[]{#_Toc172465168}[]{#_Toc172464274}[]{#_Toc172465169}[]{#_Toc172464275}[]{#_Toc172465170}[]{#_Toc172464276}[]{#_Toc172465171}[]{#_Toc172464277}[]{#_Toc172465172}[]{#_Toc172464278}[]{#_Toc172465173}[]{#_Toc172464279}[]{#_Toc172465174}[]{#_Toc172464280}[]{#_Toc172465175}[]{#_Toc172464281}[]{#_Toc172465176}[]{#_Toc172464282}[]{#_Toc172465177}[]{#_Toc237689677}[]{#_Toc237689678}[]{#_Toc155761560}[]{#_Toc155761561}[]{#_Toc155761562}[]{#_Toc155761563}[]{#_Toc155761564}[]{#_Toc155761565}[]{#_Toc155761566}[]{#_Toc155761567}[]{#_Toc155761568}[]{#_Toc155761569}[]{#_Toc155761570}[]{#_Toc155761571}[]{#_Toc155761572}[]{#_Toc155761573}[]{#_Toc155761579}[]{#_Toc155761580}[]{#_Toc155761602}[]{#_Toc155761604}[]{#_Toc155761605}[]{#_Toc155761606}[]{#_Toc155761607}[]{#_Toc155761608}[]{#_Toc155761609}[]{#_Toc155761610}[]{#_Toc155761611}[]{#_Toc155761612}[]{#_Toc155761613}[]{#_Toc155761619}[]{#_Toc155761620}[]{#_Toc155761636}[]{#_Toc237689680}[]{#_Toc237689683}[]{#_Toc237689684}[]{#_Toc237689685}[]{#_Toc237689686}[]{#_Toc237689687}[]{#_Toc237689688}[]{#_Toc237689689}[]{#_Toc237689690}[]{#_Toc237689691}[]{#_Toc237689692}[]{#_Toc237689693}[]{#_Toc237689694}[]{#_Toc237689699}[]{#_Toc237689700}[]{#_Toc237689701}[]{#_Toc237689702}[]{#_Toc237689703}[]{#_Toc237689704}[]{#_Toc237689705}[]{#_Toc237689706}[]{#_Toc237689707}[]{#_Toc237689708}[]{#_Toc237689709}[]{#_Toc237689710}[]{#_Toc237689711}[]{#_Toc237689712}[]{#_Toc237689713}[]{#_Toc237689714}[]{#_Toc237689715}[]{#_Toc237689716}[]{#_Toc237689717}[]{#_Toc237689718}[]{#_Toc237689719}[]{#_Toc237689722}[]{#_Toc237689723}[]{#_Toc237689725}[]{#_Toc237689729}[]{#_Toc237689730}[]{#_Toc237689731}[]{#_Toc237689732}[]{#_Toc237689733}[]{#_Toc237689734}[]{#_Toc237689735}[]{#_Toc237689736}[]{#_Toc237689737}[]{#_Toc237689738}[]{#_Toc237689739}[]{#_Toc237689740}[]{#_Toc237689741}[]{#_Toc237689742}[]{#_Toc237689743}[]{#_Toc237689744}[]{#_Toc237689745}[]{#_Toc237689746}[]{#_Toc143514304}[]{#_Toc143517533}[]{#_Toc143514305}[]{#_Toc143517534}[]{#_Toc143514306}[]{#_Toc143517535}[]{#_Toc143514307}[]{#_Toc143517536}[]{#_Toc143514308}[]{#_Toc143517537}[]{#_Toc143514309}[]{#_Toc143517538}[]{#_Toc143514310}[]{#_Toc143517539}[]{#_Toc143514311}[]{#_Toc143517540}[]{#_Toc143514312}[]{#_Toc143517541}[]{#_Toc143514313}[]{#_Toc143517542}[]{#_Toc143514314}[]{#_Toc143517543}[]{#_Toc143514315}[]{#_Toc143517544}[]{#_Toc143514318}[]{#_Toc143517547}[]{#_Toc143514326}[]{#_Toc143517555}[]{#_Toc143514342}[]{#_Toc143517571}[]{#_Hlt11753812}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_444640847}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos qmprofile interface]{lang="EN-US"}**]{#struct_0_14687_18620_525521970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos qmprofile]{lang="EN-US"}**]{#struct_0_14687_18620_2100380812}
:::

::: {#-996162241 .myid}
[]{#_Toc404792448}[]{#struct_0_14687_18620_69086236}

**硬件实现拥塞管理 \-- 队列调度策略配置命令 \-- queue(four-queue qmprofile view)**

------------------------------------------------------------------------

[**[queue]{lang="EN-US"}**]{#struct_0_14687_18620_881565351}[命令用来配置队列调度参数。]{style="font-family:宋体"}

[**[undo queue]{lang="EN-US"}**]{#struct_0_14687_18620_1399505052}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_447526360}

[**[queue]{lang="EN-US"}**[ *queue-id* { **sp** \| **wrr** **group** *group-id* { **weight** \| **byte-count** } *schedule-value* } \[ **min-bandwidth** *bandwidth-value* \| **max-bandwidth** *bandwidth-value* \| **service-type** *service-type-value* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_527733985}

[**[undo queue ]{lang="EN-US"}***[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x196277576}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1137482263}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1678115381}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1652750837}

[[四队列调度策略视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1489099604}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1557239299}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x163637268}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_986993093}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_480146108}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x841907202}[：队列序号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sp]{lang="EN-US"}**]{#struct_0_14687_18620_x207959380}[：配置队列为严格优先级调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[wrr]{lang="EN-US"}**]{#struct_0_14687_18620_1252592450}[：配置队列为加权轮询调度。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[group]{lang="EN-US"}***[ group-id]{lang="EN-US"}*]{#struct_0_14687_18620_x1627899083}[：]{style="font-family:宋体"}[WRR]{lang="EN-US"}[优先组号。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_x1226839701}[：表示按照权重新进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[byte-count]{lang="EN-US"}**]{#struct_0_14687_18620_919232728}[：表示按照每次轮询可发送的字节数进行计算。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[schedule]{lang="EN-US"}[-value]{lang="EN-US"}*]{#struct_0_14687_18620_2040600460}[：]{style="font-family:宋体"}[配置队列的]{style="font-family:宋体"}[调度权重。]{style="font-family:宋体"}[不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[min bandwidth]{lang="EN-US"}***[ bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1874774119}[：]{style="font-family:宋体"}[最小保证带宽值，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。端口流量拥塞时能够保证的最小队列带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[max bandwidth ]{lang="EN-US"}***[bandwidth-value]{lang="EN-US"}*]{#struct_0_14687_18620_x690610205}[：最大限制带宽]{style="font-family:宋体"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[service-type]{lang="EN-US"}***[ service-type-value]{lang="EN-US"}*]{#struct_0_14687_18620_x1795021210}[：服务类型。包括]{style="font-family:宋体"}[HSI]{lang="EN-US"}[（]{style="font-family:宋体"}[High Speed Internet]{lang="EN-US"}[，高速上网）、]{style="font-family:宋体"}[STB]{lang="EN-US"}[（]{style="font-family:宋体"}[SetTop Box]{lang="EN-US"}[，机顶盒）、]{style="font-family:宋体"}[VoIP]{lang="EN-US"}[（]{style="font-family:宋体"}[Voice Over Internet Protocol]{lang="EN-US"}[，在]{style="font-family:宋体"}[IP]{lang="EN-US"}[网络上传送语音）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_771023653}

[[对同一个队列多次配置时，后一次配置会覆盖前面的配置，以最后一次配置为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1447308139}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x967669404}[除了支持数字外，还支持直接输入关键字，具体情况请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}5-3]{lang="EN-US"}](?1813098140#_Ref293562576)[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_937796272}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_69086239}[创建自定义的四队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并配置队列]{style="font-family:宋体"}[0]{lang="EN-US"}[为严格优先级调度，最小带宽为]{style="font-family:宋体"}[40]{lang="EN-US"}[，服务类型为]{style="font-family:宋体"}[HSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1601609383}

[\[Sysname\] qos qmprofile myprofile type four-queue ]{lang="EN-US"}

[\[Sysname-qmprofile-four-queue-myprofile\] queue 0 sp min bandwidth 40 service-type hsi]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_939212066}[创建自定义的四队列调度策略]{style="font-family:宋体"}[myprofile]{lang="EN-US"}[，并配置队列]{style="font-family:宋体"}[1]{lang="EN-US"}[为加权轮询调度，权重为]{style="font-family:宋体"}[63]{lang="EN-US"}[，分组为]{style="font-family:宋体"}[1, ]{lang="EN-US"}[最小保证带宽为]{style="font-family:宋体"}[40]{lang="EN-US"}[，服务类型为]{style="font-family:宋体"}[HSI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1456769384}

[\[Sysname\] qos qmprofile myprofile type four-queue]{lang="EN-US"}

[\[Sysname-qmprofile-four-queue-myprofile\] queue 1 wrr group 1 weight 63 min bandwidth 40 service-type hsi]{lang="EN-US"}
:::

::: {#323274444 .myid}
[]{#_Toc404792450}[]{#struct_0_14687_18620_325469251}[]{#_Toc250037247}

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue af**

------------------------------------------------------------------------

[**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1786039398}[命令用来配置类进行确保转发（]{style="font-family:宋体"}[Assured-forwarding]{lang="EN-US"}[），并配置类可确保的最小带宽]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo queue af]{lang="EN-US"}**]{#struct_0_14687_18620_1797914429}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1522149875}

[**[queue af bandwidth]{lang="EN-US"}**[ *bandwidth* \[ **pir** *peak-information-rate* \]]{lang="EN-US"}]{#struct_0_14687_18620_509496632}

[**[undo queue af]{lang="EN-US"}**]{#struct_0_14687_18620_231830488}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1364249205}

[[没有配置类进行确保转发。]{style="font-family:宋体"}]{#struct_0_14687_18620_789390289}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2123999533}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1441618533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_934471785}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1073748603}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_980586446}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x124465408}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_14687_18620_661103495}[：可确保的最小带宽，单位]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x424756722}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_987240519}

[[当在策略下将类与]{style="font-family:宋体"}]{#struct_0_14687_18620_x1690549349}**[queue af]{lang="EN-US"}**[所属行为关联时，必须满足：同一个策略下为确保转发（]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**[）]{style="font-family:宋体"}[和加速转发]{style="font-family:
宋体"}[（]{style="font-family:宋体"}**[queue ef]{lang="EN-US"}**[）的类指定的带宽]{style="font-family:宋体"}[之和必须不大于该策略所应用接口的]{style="font-family:宋体"}[可用带宽。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_531025995}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1154014053}[为行为]{style="font-family:宋体"}[database]{lang="EN-US"}[配置确保转发，并且确保最小带宽为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1543059981}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue af bandwidth 200]{lang="EN-US"}
:::

::: {#-1581192182 .myid}
[]{#_Toc404792451}[]{#struct_0_14687_18620_1038334006}

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue ef**

------------------------------------------------------------------------

[**[queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_x454212910}[命令用来配置类进行加速转发（]{style="font-family:宋体"}[Expedited-forwarding]{lang="EN-US"}[），报文进入绝对优先级队列，并配置最大带宽。]{style="font-family:宋体"}

[**[undo queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_88410288}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1886594630}

[**[queue ef bandwidth]{lang="EN-US"}**[ *bandwidth* \[ **cbs** *burst* \] \[ **pir** *peak-information-rate* \]]{lang="EN-US"}]{#struct_0_14687_18620_x883980295}

[**[undo queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_x1103805096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_891611947}

[[没有配置类进行加速转发。]{style="font-family:宋体"}]{#struct_0_14687_18620_240537359}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1844903060}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1486999062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_585123344}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1112913530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_278819119}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x738205901}

[*[bandwidth]{lang="EN-US"}*]{#struct_0_14687_18620_53189353}[：带宽，单位]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *burst*]{lang="EN-US"}]{#struct_0_14687_18620_x995339602}[：指定承诺突发尺寸，单位为字节。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x1287264822}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x120355148}

[**[queue ef]{lang="EN-US"}**]{#struct_0_14687_18620_1689887530}[命令用来配置加速转发（]{style="font-family:宋体"}[Expedited-forwarding]{lang="EN-US"}[），报文进入绝对优先级队列，并配置最大带宽。]{style="font-family:宋体"}**[undo queue ef]{lang="EN-US"}**[命令用来取消配置。]{style="font-family:宋体"}

[[本命令的注意事项如下。]{style="font-family:宋体"}]{#struct_0_14687_18620_235787325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令在流行为视图下不能与]{style="font-family:宋体"}]{#struct_0_14687_18620_1797848893}**[queue af]{lang="EN-US"}**[同时使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个策略下为确保转发（]{style="font-family:宋体"}]{#struct_0_14687_18620_1131786965}**[queue af]{lang="EN-US"}**[）和加速转发（]{style="font-family:宋体"}**[queue ef]{lang="EN-US"}**[）的类指定的带宽之和必须不大于该策略所应用接口的可用带宽。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设置绝对值形式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_14687_18620_297610122}**[queue ef bandwidth]{lang="EN-US"}**[ *bandwidth* \[ **cbs** *burst* \]]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[CBS = *burst*]{lang="EN-US"}[，若不指定]{lang="EN-US" style="font-family:宋体"}*[burst]{lang="EN-US"}*[，则]{lang="EN-US" style="font-family:宋体"}[CBS = *bandwidth*]{lang="EN-US"}[×]{lang="EN-US" style="font-family:
宋体"}[25]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_231764952}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_817834273}[配置报文进入优先级队列，最大带宽为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，]{style="font-family:宋体"}*[burst]{lang="EN-US"}*[为]{style="font-family:宋体"}[5000bytes]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x849135580}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue ef bandwidth 200 cbs 5000]{lang="EN-US"}
:::

::: {#-754646752 .myid}
[]{#_Toc404792452}[]{#struct_0_14687_18620_1441552997}

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- queue wfq**

------------------------------------------------------------------------

[**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1340843514}[命令用来为缺省类配置采用公平队列。]{style="font-family:宋体"}

[**[undo queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_2117583523}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x581330188}

[**[queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x124530944}

[**[undo queue wfq]{lang="EN-US"}**]{#struct_0_14687_18620_305529149}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x469063751}

[[没有为缺省类配置采用公平队列]{style="font-family:宋体"}]{#struct_0_14687_18620_1682472492}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1690614885}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_186030771}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2074835923}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1040033429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1038268470}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1456192054}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x470139967}[为流行为]{style="font-family:宋体"}[test]{lang="EN-US"}[配置]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x884045831}

[\[Sysname\] traffic behavior test]{lang="EN-US"}

[\[Sysname-behaviro-test\] queue wfq]{lang="EN-US"}
:::

::: {#452723700 .myid}
[]{#_Toc404792453}[]{#struct_0_14687_18620_x2031645938}

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- weight**

------------------------------------------------------------------------

[**[weight]{lang="EN-US"}**]{#struct_0_14687_18620_x1291773667}[命令用来配置]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[的权重。]{style="font-family:宋体"}

[**[undo weight]{lang="EN-US"}**]{#struct_0_14687_18620_83461246}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1898618251}

[**[weight]{lang="EN-US"}**[ weight-value]{lang="EN-US"}]{#struct_0_14687_18620_1844837524}

[**[undo weight]{lang="EN-US"}**]{#struct_0_14687_18620_x2027947063}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2083179715}

[[对于]{style="font-family:宋体"}[AF]{lang="EN-US"}]{#struct_0_14687_18620_667231217}[和]{style="font-family:宋体"}[EF]{lang="EN-US"}[，]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[的权重为]{style="font-family:宋体"}[1]{lang="EN-US"}[；对于]{style="font-family:宋体"}[BE]{lang="EN-US"}[，]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[的权重为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_278753583}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_942387737}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1213014566}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1432459082}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1287330358}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x37206200}

[*[weight-value]{lang="EN-US"}*]{#struct_0_14687_18620_990767825}[：权重的值。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1797783357}

[[在]{style="font-family:宋体"}]{#struct_0_14687_18620_1961622133}[AF]{lang="EN-US"}[最小可保证带宽和峰值速率之间的流量采用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[调度；在]{style="font-family:宋体"}[EF]{lang="EN-US"}[最大带宽和峰值速率之间的流量采用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[调度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1494074179}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_151704650}[配置流行为]{style="font-family:宋体"}[database1]{lang="EN-US"}[采用]{style="font-family:宋体"}[AF]{lang="EN-US"}[，最小可保证带宽为]{style="font-family:宋体"}[200kbps]{lang="EN-US"}[，峰值速率为]{style="font-family:宋体"}[500kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[200]{lang="EN-US"}[～]{style="font-family:宋体"}[500kbps]{lang="EN-US"}[之间的流量采用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[，其权重为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_231699416}

[\[Sysname\] traffic behavior database1]{lang="EN-US"}

[\[Sysname-behavior-database1\] queue af bandwidth 200 pir 500]{lang="EN-US"}

[\[Sysname-behavior-database1\] weight 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1556007361}[配置流行为]{style="font-family:宋体"}[database2]{lang="EN-US"}[采用]{style="font-family:宋体"}[EF]{lang="EN-US"}[，最大带宽为]{style="font-family:宋体"}[400kbps]{lang="EN-US"}[，峰值速率为]{style="font-family:宋体"}[800kbps]{lang="EN-US"}[，]{style="font-family:宋体"}[400]{lang="EN-US"}[～]{style="font-family:宋体"}[800kbps]{lang="EN-US"}[之间的流量采用]{style="font-family:宋体"}[WFQ]{lang="EN-US"}[，其权重为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1300690137}

[\[Sysname\] traffic behavior database2]{lang="EN-US"}

[\[Sysname-behavior-database2\] queue ef bandwidth 400 pir 800]{lang="EN-US"}

[\[Sysname-behavior-database2\] weight 200]{lang="EN-US"}
:::

::: {#-968778503 .myid}
[]{#_Toc404792454}[]{#struct_0_14687_18620_1575770725}

**硬件实现拥塞管理 \-- 基于类的队列配置命令 \-- wred**

------------------------------------------------------------------------

[**[wred]{lang="EN-US"}**]{#struct_0_14687_18620_x448973661}[命令用来配置丢弃方式为加权随机早期检测。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **wred**]{lang="EN-US"}]{#struct_0_14687_18620_427269394}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x738486943}

[**[wred]{lang="EN-US"}**[ \[ **dscp** \| **ip-precedence** \]]{lang="EN-US"}]{#struct_0_14687_18620_9686784}

[**[undo wred]{lang="EN-US"}**]{#struct_0_14687_18620_x159368440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1756731140}

[[没有配]{style="font-family:宋体"}]{#struct_0_14687_18620_x41701360}[置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1556397157}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_933651076}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_112407194}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1268406145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1172486198}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1484845100}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1070710129}[：表明在为一个包计算丢弃概率时使用的是]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x749828103}[：表明在为一个包计算丢弃概率时使用的是]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值，缺省情况下使用的是]{style="font-family:宋体"}[ip-precedence]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1549486423}

[[该命令必须在配置了]{style="font-family:宋体"}**[queue af]{lang="EN-US"}**]{#struct_0_14687_18620_x1119860136}[或]{style="font-family:宋体"}**[queue wfq]{lang="EN-US"}**[后使用。当接口上应用了配置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[的策略后，原有的接口级的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[配置失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1979055252}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1937665317}[配置采用加权早期检测方式，丢弃概率以]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1771777329}

[\[Sysname\] traffic behavior database]{lang="EN-US"}

[\[Sysname-behavior-database\] queue wfq]{lang="EN-US"}

[\[Sysname-behavior-database\] wred]{lang="EN-US"}
:::

::: {#825680193 .myid}
[]{#_Toc404792456}[]{#struct_0_14687_18620_x82111208}

**硬件实现拥塞管理 \-- 低时延队列调度模式配置命令 \-- queue low-latency enable**

------------------------------------------------------------------------

[**[queue low-latency enable]{lang="EN-US"}**]{#struct_0_14687_18620_1619782147}[命令用来开启低时延队列调度模式。]{style="font-family:
宋体"}

[**[undo queue low-latency enable]{lang="EN-US"}**]{#struct_0_14687_18620_x1009509495}[命令用来关闭低时延队列调度模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x217819155}

[**[queue low-latency enable]{lang="EN-US"}**]{#struct_0_14687_18620_1785070425}

[**[undo queue low-latency enable]{lang="EN-US"}**]{#struct_0_14687_18620_x857507981}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x455032267}

[[低时延队列调度模式处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14687_18620_440797293}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82045672}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x306833372}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x113083064}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1986753510}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x827260297}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_861601965}

[[在对转发时延性能要求较高的场景下，可开启低时延队列调度模式，使得系统获得更高的转发时延性能。]{style="font-family:宋体"}]{#struct_0_14687_18620_x92975379}

[[支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}]{#struct_0_14687_18620_x1488625835}[的设备，本命令只有缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[支持。]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的相关内容请参见"基本配置指导"中的"]{style="font-family:宋体"}[MDC]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82242280}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x432280946}[开启低时延队列调度模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1243800045}

[\[Sysname\] queue low-latency enable]{lang="EN-US"}

**[ ]{lang="EN-US"}**
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section7 style="layout-grid:15.85pt"}
:::

::: {#446107805 .myid}
[]{#_Toc341855941}[]{#_Toc291750089}[]{#_Toc263760037}[]{#_Toc226262699}[]{#_Toc198110213}[]{#_Toc115171246}[]{#_Toc81455608}[]{#_Toc56569661}[]{#_Toc404792459}[]{#struct_0_14687_18620_x357545177}[]{#_Toc344130014}[]{#_Toc341855940}[]{#_Toc291750088}[]{#_Toc263760036}[]{#_Toc226262698}[]{#_Toc198110212}[]{#_Toc115171245}[]{#_Toc81455607}[]{#_Toc56569660}

**拥塞避免 \-- WRED配置命令 \-- display qos wred interface**

------------------------------------------------------------------------

[**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1660900506}[命令用来显示指定接口、指定]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[或所有接口及]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[配置情况和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82176744}

[**[display qos wred interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \[ **pvc** { *pvc-name* \| *vpi/vci* } \] \]]{lang="EN-US"}]{#struct_0_14687_18620_1243253980}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1781321589}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1776610343}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1503644480}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x658135983}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x16930058}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1771708651}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_x81849064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1530974881}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_427508111}[：指定的接口类型和接口编号。]{style="font-family:宋体"}[如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[配置情况和统计信息。]{style="font-family:宋体"}

[**[pvc]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *pvc-name* \| *vpi/vci* }]{lang="EN-US"}]{#struct_0_14687_18620_709047077}[：显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上的指定]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的信息，只有当接口为]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口时才能指定本参数。]{style="font-family:宋体"}*[pvc-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[PVC]{lang="EN-US"}[名。]{style="font-family:宋体"}*[vpi/vci]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VPI/VCI]{lang="EN-US"}[值。如果未指定本参数，将显示指定]{style="font-family:宋体"}[ATM]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[配置情况和统计信息]{style="font-family:宋体"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_295349098}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1976572172}[显示所有接口的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[配置情况和统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos wred interface]{lang="EN-US"}]{#struct_0_14687_18620_x81783528}

[Interface: GigabitEthernet1/0/4]{lang="EN-US"}

[ Current WRED configuration:]{lang="EN-US"}

[ Exponent: 9 (1/512)]{lang="EN-US"}

[ Pre  Low   High  Dis-prob Random-discard  Tail-discard]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0    10    30    10       0               0]{lang="EN-US"}

[1    10    30    10       0               0]{lang="EN-US"}

[2    10    30    10       0               0]{lang="EN-US"}

[3    10    30    10       0               0]{lang="EN-US"}

[4    10    30    10       0               0]{lang="EN-US"}

[5    10    30    10       0               0]{lang="EN-US"}

[6    10    30    10       0               0]{lang="EN-US"}

[7    10    30    10       0               0]{lang="EN-US"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[Interface: GigabitEthernet1/0/3]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14687_18620_2056663290}

[[ Current WRED configuration:]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14687_18620_1769847546}

[[ Applied WRED table name: q1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_14687_18620_x1034255612}

[[表1-5 ]{lang="EN-US"}[display qos wred interface]{lang="EN-US"}]{#struct_0_14687_18620_552207370}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1740386393}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_505446572}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x81980136}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x1242669436}

[[接口名，由接口类型和接口编号组成]{style="font-family:宋体"}]{#struct_0_14687_18620_x561532041}

[[Exponent]{lang="EN-US"}]{#struct_0_14687_18620_57018974}

[[计算平均队列长度的指数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1350733454}

[[Pre]{lang="EN-US"}]{#struct_0_14687_18620_x1402328386}

[[报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_14687_18620_x81914600}[优先级]{style="font-family:宋体"}

[[Low]{lang="EN-US"}]{#struct_0_14687_18620_301710160}

[[队列下限]{style="font-family:宋体"}]{#struct_0_14687_18620_x1533179927}

[[High]{lang="EN-US"}]{#struct_0_14687_18620_2066425792}

[[队列上限]{style="font-family:宋体"}]{#struct_0_14687_18620_x643068209}

[[Dis-prob]{lang="EN-US"}]{#struct_0_14687_18620_x81586920}

[[计算丢弃概率时的分母]{style="font-family:宋体"}]{#struct_0_14687_18620_573375326}

[[Random-discard]{lang="EN-US"}]{#struct_0_14687_18620_x1072400038}

[[随机丢弃的报文的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_x756697244}

[[Tail-discard]{lang="EN-US"}]{#struct_0_14687_18620_x81521384}

[[尾丢弃报文的数目]{style="font-family:宋体"}]{#struct_0_14687_18620_1452766246}

[[Current WRED configuration]{lang="EN-US"}]{#struct_0_14687_18620_1369794834}

[[当前]{style="font-family:宋体"}[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x21355046}[的配置情况]{style="font-family:宋体"}

[[Applied WRED table name]{lang="EN-US"}]{#struct_0_14687_18620_x1872375168}

[[当前应用的]{style="font-family:宋体"}[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x82111211}[表的名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1458308787 .myid}
[]{#_Toc404792460}[]{#struct_0_14687_18620_x718870004}[]{#_Toc344130015}

**拥塞避免 \-- WRED配置命令 \-- qos wred enable**

------------------------------------------------------------------------

[**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_1504432928}[命令用来在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上使能]{style="font-family:宋体"}[WRED]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_x860145103}[命令用来恢复缺省的队列丢弃方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2100533304}

[**[qos wred ]{lang="EN-US"}**[\[ **dscp** \| **ip-precedence** \] **enable**]{lang="EN-US"}]{#struct_0_14687_18620_1194297222}

[**[undo qos wred ]{lang="EN-US"}**[\[ **dscp** \| **ip-precedence** \] **enable**]{lang="EN-US"}]{#struct_0_14687_18620_1666567560}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82045675}

[[队列丢弃方法为尾丢弃。]{style="font-family:宋体"}]{#struct_0_14687_18620_x306833371}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x113279672}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x400621007}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1893426751}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x232898214}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1320716270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1563183696}

[**[dscp]{lang="EN-US"}**]{#struct_0_14687_18620_x82242283}[：表明计算丢弃概率时使用的是]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x432280945}[：表明计算丢弃概率时使用的是]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级值。缺省情况下使用的是]{style="font-family:宋体"}**[ip-precedence]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1243865581}

[[有的产品本命令在可直接配置；有的产品必须先在接口上配置]{style="font-family:宋体"}**[qos wfq]{lang="EN-US"}**]{#struct_0_14687_18620_x1376131835}[命令，才能配置本命令。具体情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1845862539}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x2043324007}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上使能]{style="font-family:宋体"}[WRED]{lang="EN-US"}[，丢弃概率以]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级计算。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1637350697}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq queue-length 100 queue-number 512]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred ip-precedence enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82176747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_1243253983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_1781256053}
:::

::: {#-1295923160 .myid}
[]{#_Toc115171247}[]{#_Toc81455609}[]{#_Toc56569662}[]{#_Toc404792461}[]{#struct_0_14687_18620_x990486290}[]{#_Toc344130016}[]{#_Toc341855942}[]{#_Toc291750090}[]{#_Toc263760038}[]{#_Toc226262700}[]{#_Toc198110214}[]{#_Toc160613206}

**拥塞避免 \-- WRED配置命令 \-- qos wred dscp**

------------------------------------------------------------------------

[**[qos wred dscp]{lang="EN-US"}**]{#struct_0_14687_18620_101191522}[命令用来设置各]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的下限、上限和丢弃概率。]{style="font-family:宋体"}

[**[undo qos wred dscp]{lang="EN-US"}**]{#struct_0_14687_18620_1520591309}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x954947625}

[**[qos wred dscp]{lang="EN-US"}**[ *dscp-value* **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]{lang="EN-US"}]{#struct_0_14687_18620_x531643729}

[**[undo qos wred dscp]{lang="EN-US"}**[ *dscp-value*]{lang="EN-US"}]{#struct_0_14687_18620_x81849067}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1530974882}

[[下限缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_14687_18620_427442575}[，上限缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[，丢弃概率缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1671725474}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x939230125}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_615178735}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1163974211}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1382098194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81783531}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_14687_18620_x281988879}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，也可以是关键字，如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-5]{lang="EN-US"}](?-580725274#_Ref163816081)[所示。]{style="font-family:宋体"}

[**[low-limit ]{lang="EN-US"}***[low-limit]{lang="EN-US"}*]{#struct_0_14687_18620_747610226}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[下限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US"}*]{#struct_0_14687_18620_1971389590}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[上限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_14687_18620_x894952528}[：丢弃概率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1987525970}

[[必须先使用]{style="font-family:宋体"}**[qos wred dscp enable]{lang="EN-US"}**]{#struct_0_14687_18620_x458637871}[在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上应用基于]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[后，才可以进行本配置。阈值限制的是平均队列长度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_910541455}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1310659445}[在接口上设置]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[63]{lang="EN-US"}[的报文的队列下限为]{style="font-family:宋体"}[20]{lang="EN-US"}[，上限为]{style="font-family:宋体"}[40]{lang="EN-US"}[，丢弃概率为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x81980139}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq queue-length 100 queue-number 512]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred dscp enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred dscp 63 low-limit 20 high-limit 40 discard-probability 15]{lang="EN-US"}

[]{#_Toc341855943}[]{#_Toc291750091}[]{#_Toc263760039}[]{#_Toc226262701}[]{#_Toc198110215}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1242669427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_1004486364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_x1202778982}
:::

::: {#806118468 .myid}
[]{#_Toc404792462}[]{#struct_0_14687_18620_1781391917}[]{#_Toc344130017}

**拥塞避免 \-- WRED配置命令 \-- qos wred ip-precedence**

------------------------------------------------------------------------

[**[qos wred ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_1026681902}[命令用来设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级的下限、上限和丢弃概率。]{style="font-family:宋体"}

[**[undo qos wred ip-precedence]{lang="EN-US"}**]{#struct_0_14687_18620_x81914603}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_301710159}

[**[qos wred ip-precedence]{lang="EN-US"}**[ *ip-precedence* **low-limit** *low-limit* **high-limit** *high-limit* **discard-probability** *discard-prob*]{lang="EN-US"}]{#struct_0_14687_18620_805472226}

[**[undo qos wred ip-precedence]{lang="EN-US"}**[ *ip-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_x823175845}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x411327744}

[[下限缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_14687_18620_1260340955}[，上限缺省值为]{style="font-family:宋体"}[30]{lang="EN-US"}[，丢弃概率缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x734833684}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_x820422727}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81586923}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_573375327}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1072400039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1972186111}

[**[ip-precedence]{lang="EN-US"}***[ ip-precedence]{lang="EN-US"}*]{#struct_0_14687_18620_2014441611}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x1061190514}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[下限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x1959285041}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[上限，单位为报文个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_14687_18620_x602413469}[：丢弃概率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81521387}

[[必须先使用]{style="font-family:宋体"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_1452766243}[在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上应用基于]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[后，才可以进行本配置。阈值限制的是平均队列长度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1369467154}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_28738432}[在接口上设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[的报文的队列下限为]{style="font-family:宋体"}[20]{lang="EN-US"}[，上限为]{style="font-family:宋体"}[40]{lang="EN-US"}[，丢弃概率为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1372612228}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq queue-length 100 queue-number 512]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred ip-precedence enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred ip-precedence 3 low-limit 20 high-limit 40 discard-probability 15]{lang="EN-US"}

[]{#_Toc341855944}[]{#_Toc291750092}[]{#_Toc263760040}[]{#_Toc226262702}[]{#_Toc198110216}[]{#_Toc115171248}[]{#_Toc81455610}[]{#_Toc56569663}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1148429256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1506452288}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_x82111210}
:::

::: {#314741243 .myid}
[]{#_Toc404792463}[]{#struct_0_14687_18620_x718870005}[]{#_Toc344130018}

**拥塞避免 \-- WRED配置命令 \-- qos wred weighting-constant**

------------------------------------------------------------------------

[**[qos wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_1504367392}[命令用来设置]{style="font-family:
宋体"}[WRED]{lang="EN-US"}[计算平均队列长度的指数。]{style="font-family:宋体"}

[**[undo qos wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_1060995540}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_921737648}

[**[qos wred weighting-constant]{lang="EN-US"}**[ *exponent*]{lang="EN-US"}]{#struct_0_14687_18620_x1699017586}

[**[undo qos wred weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_x1509617508}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82045674}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x306833370}[计算平均队列长度的指数为]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x113214136}

[[接口视图]{style="font-family:宋体"}[/PVC]{lang="EN-US"}]{#struct_0_14687_18620_1581491300}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1246434424}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x701514068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1920320436}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1302580218}

[**[weighting-constant]{lang="EN-US"}***[ exponent]{lang="EN-US"}*]{#struct_0_14687_18620_x82242282}[：计算平均队列长度的指数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x432280944}

[[必须先使用]{style="font-family:宋体"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_1243931117}[在接口或]{style="font-family:宋体"}[PVC]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WRED]{lang="EN-US"}[后，才可以配置]{style="font-family:宋体"}[WRED]{lang="EN-US"}[的参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_191412043}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1943075579}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上配置计算平均队列长度的指数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_408022338}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wfq queue-length 100 queue-number 512]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred weighting-constant 6]{lang="EN-US"}

[]{#struct_0_14687_18620_1228729870}[]{#_Toc322968440}[]{#_Toc263759947}[]{#_Toc226262614}[]{#_Toc198110071}[]{#_Toc117165486}[]{#_Toc81455531}[]{#_Toc322968474}[]{#_Toc263759979}[]{#_Toc226262646}[]{#_Toc198110155}[]{#_Toc117857762}[]{#_Toc81455560}[]{#_Toc322968475}[]{#_Toc263759980}[]{#_Toc226262647}[]{#_Toc198110156}[]{#_Toc117857763}[]{#_Toc81455561}[]{#_Toc322968476}[]{#_Toc263759981}[]{#_Toc226262648}[]{#_Toc198110157}[]{#_Toc117857764}[]{#_Toc81455562}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_x82176746}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred enable]{lang="EN-US"}**]{#struct_0_14687_18620_1243253982}
:::

::: {#-459368645 .myid}
[]{#_Toc404792465}[]{#struct_0_14687_18620_x937527471}[]{#_Toc292899232}[]{#_Toc291750094}[]{#_Toc263760042}[]{#_Toc226262704}[]{#_Toc198110218}[]{#_Toc115171250}[]{#_Toc347748747}[]{#_Toc347748748}[]{#_Toc347748749}[]{#_Toc347748750}[]{#_Toc347748751}[]{#_Toc347748752}[]{#_Toc347748753}[]{#_Toc347748754}[]{#_Toc347748755}[]{#_Toc347748756}[]{#_Toc347748757}[]{#_Toc347748758}[]{#_Toc347748759}[]{#_Toc347748760}[]{#_Toc347748761}[]{#_Toc347748762}[]{#_Toc347748763}[]{#_Toc347748764}[]{#_Toc347748765}[]{#_Toc347748766}[]{#_Toc347748779}

**拥塞避免 \-- WRED表配置命令 \-- display qos wred table**

------------------------------------------------------------------------

[**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_1992197286}[命令用来显示]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表的配置情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1592799967}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_14687_18620_1894176307}

[**[display qos wred table]{lang="EN-US"}**[ \[ **name** *table-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1131920956}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x81849066}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos wred table]{lang="EN-US"}**[ \[ **name** *table-name* \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_1530974883}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_427377039}[模式：]{style="font-family:宋体"}

[**[display qos wred table]{lang="EN-US"}**[ \[ **name** *table-name* \] \[ **chassis** *chassis-number* **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_14687_18620_x1905713056}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1383789114}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2064088600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1197780212}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_796917237}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x81783530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x281988878}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_747675762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1951374911}

[**[name]{lang="EN-US"}***[ table-name]{lang="EN-US"}*]{#struct_0_14687_18620_x829924259}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表的名字。如果未指定本参数，则显示所有]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x94032050}[：显示指定单板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示主用主控板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_757010669}[：显示指定成员设备的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1252513149}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示主用设备的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1754519306}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，则显示全局主用主控板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1120074310}[：]{style="font-family:宋体"}[显示指定单板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示全局主用主控板的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表配置情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x151965928}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_430681061}[显示]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表]{style="font-family:宋体"}[1]{lang="EN-US"}[的配置情况，表]{style="font-family:
宋体"}[1]{lang="EN-US"}[是一个已经配置好的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[参数表。]{style="font-family:宋体"}

[[\<Sysname\> display qos wred table name 1]{lang="EN-US"}]{#struct_0_14687_18620_x81914602}

[Table name: 1]{lang="EN-US"}

[Table type: Queue based WRED]{lang="EN-US"}

[QID   gmin  gmax  gprob  ymin  ymax  yprob  rmin  rmax  rprob  exponent  ECN]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[1     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[2     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[3     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[4     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[5     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[6     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[7     100   1000  10     100   1000  10     100   1000  10     9         N]{lang="EN-US"}

[[表6-1 ]{lang="EN-US"}[display qos wred table]{lang="EN-US"}]{#struct_0_14687_18620_301710158}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1735751513}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_805472225}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x823175844}

[[Table name]{lang="EN-US"}]{#struct_0_14687_18620_x81586922}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_573375328}[表名]{style="font-family:宋体"}

[[Table type]{lang="EN-US"}]{#struct_0_14687_18620_x1072400048}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x756893852}[表类型]{style="font-family:宋体"}

[[QID]{lang="EN-US"}]{#struct_0_14687_18620_x756050632}

[[队列]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_14687_18620_x81521386}

[[gmin]{lang="EN-US"}]{#struct_0_14687_18620_1452766244}

[[绿色报文的队列下限]{style="font-family:宋体"}]{#struct_0_14687_18620_1369663762}

[[gmax]{lang="EN-US"}]{#struct_0_14687_18620_1615376725}

[[绿色报文的队列上限]{style="font-family:宋体"}]{#struct_0_14687_18620_1631776379}

[[gprob]{lang="EN-US"}]{#struct_0_14687_18620_x82111213}

[[绿色报文的丢弃概率]{style="font-family:宋体"}]{#struct_0_14687_18620_x718870006}

[[ymin]{lang="EN-US"}]{#struct_0_14687_18620_1504564000}

[[黄色报文的队列下限]{style="font-family:宋体"}]{#struct_0_14687_18620_1833432498}

[[ymax]{lang="EN-US"}]{#struct_0_14687_18620_x82045677}

[[黄色报文的队列上限]{style="font-family:宋体"}]{#struct_0_14687_18620_x306833369}

[[yprob]{lang="EN-US"}]{#struct_0_14687_18620_x112755383}

[[黄色报文的丢弃概率]{style="font-family:宋体"}]{#struct_0_14687_18620_x1175703399}

[[rmin]{lang="EN-US"}]{#struct_0_14687_18620_x82242285}

[[红色报文的队列下限]{style="font-family:宋体"}]{#struct_0_14687_18620_x432280943}

[[rmax]{lang="EN-US"}]{#struct_0_14687_18620_1243996653}

[[红色报文的队列上限]{style="font-family:宋体"}]{#struct_0_14687_18620_968460050}

[[rprob]{lang="EN-US"}]{#struct_0_14687_18620_x82176749}

[[红色报文的丢弃概率]{style="font-family:宋体"}]{#struct_0_14687_18620_1243253993}

[[exponent]{lang="EN-US"}]{#struct_0_14687_18620_1781256052}

[[计算平均队列长度指数]{style="font-family:宋体"}]{#struct_0_14687_18620_x990420754}

[[ECN]{lang="EN-US"}]{#struct_0_14687_18620_x81849069}

[[是否对该队列开启了拥塞通知功能，]{style="font-family:宋体"}[Y]{lang="EN-US"}]{#struct_0_14687_18620_1530974884}[表示开启，]{style="font-family:宋体"}[N]{lang="EN-US"}[表示未开启]{style="font-family:宋体"}

[ ]{lang="SV"}

::: {#-558863757 .myid}
[]{#_Toc404792466}[]{#struct_0_14687_18620_427835791}[]{#_Toc292899233}

**拥塞避免 \-- WRED表配置命令 \-- qos wred apply**

------------------------------------------------------------------------

[**[qos wred apply]{lang="EN-US"}**]{#struct_0_14687_18620_1493133035}[命令用来在接口上应用]{style="font-family:宋体"}[WRED]{lang="EN-US"}[全局表。]{style="font-family:宋体"}

[**[undo qos wred apply]{lang="EN-US"}**]{#struct_0_14687_18620_180812476}[命令用来恢复接口缺省的尾丢弃模式，它同时取消]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表的应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_572519993}

[**[qos wred apply]{lang="EN-US"}**[ \[ *table-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_x81783533}

[**[undo qos wred apply]{lang="EN-US"}**]{#struct_0_14687_18620_x281988877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_747479154}

[[接口没有应用]{style="font-family:宋体"}[WRED]{lang="EN-US"}]{#struct_0_14687_18620_517776925}[全局表，即接口采用尾丢弃。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_2109147956}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_208565460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1798619745}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1729146777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x81980141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x51028347}

[*[table-name]{lang="EN-US"}*]{#struct_0_14687_18620_x118590428}[：]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1162334844}

[[如果不指定]{style="font-family:宋体"}[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x539941289}[表的名称，则在接口上应用缺省]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x172003740}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_359757362}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x81914605}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos wred apply table1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_301710157}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred interface]{lang="EN-US"}**]{#struct_0_14687_18620_805472240}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_323835233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_549385581}
:::

::: {#-1247177378 .myid}
[]{#_Toc404792467}[]{#struct_0_14687_18620_x2140888047}[]{#_Toc292899234}[]{#_Toc291750095}[]{#_Toc263760043}[]{#_Toc226262705}[]{#_Toc198110219}

**拥塞避免 \-- WRED表配置命令 \-- qos wred table**

------------------------------------------------------------------------

[**[qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x573989093}[命令用来创建全局]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表，同时进入该]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表视图。]{style="font-family:宋体"}

[**[undo qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_1654253943}[命令用来删除全局]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81586925}

[**[qos wred]{lang="EN-US"}**[ **queue** **table** *table-name*]{lang="EN-US"}]{#struct_0_14687_18620_573375321}

[**[undo qos wred queue table]{lang="EN-US"}**[ *table-name*]{lang="EN-US"}]{#struct_0_14687_18620_x1072400041}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1615759143}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1240085756}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_325182984}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1229278048}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1564268798}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x81521389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1452766241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1369336082}

[**[queue]{lang="EN-US"}**]{#struct_0_14687_18620_x376631415}[：基于队列的表，拥塞时根据报文所在队列进行随机丢弃。]{style="font-family:宋体"}

[**[table ]{lang="EN-US"}***[table-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1612870107}[：指定表的名称。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1852240672}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备不允许删除正在使用的表。如果想删除正在使用的表，请先在接口上取消应用的]{style="font-family:宋体"}]{#struct_0_14687_18620_568075604}[WRED]{lang="EN-US"}[表。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省]{lang="EN-US" style="font-family:宋体"}[WRED]{lang="EN-US"}]{#struct_0_14687_18620_x1543942066}[表可以通过]{lang="EN-US" style="font-family:宋体"}**[display qos wred table]{lang="EN-US"}**[命令显示，不允许修改和删除。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82111212}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x718870007}[创建基于]{style="font-family:宋体"}[queue]{lang="EN-US"}[的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表]{style="font-family:宋体"}[queue-table1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1504498464}

[\[Sysname\] qos wred queue table queue-table1]{lang="EN-US"}

[\[Sysname-wred-table-queue-table1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_593938491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x167169585}
:::

::: {#-1405045818 .myid}
[]{#_Toc404792468}[]{#struct_0_14687_18620_x749539204}[]{#_Toc292899235}[]{#_Toc291750098}[]{#_Toc263760046}[]{#_Toc226262708}[]{#_Toc198110222}[]{#_Toc115171254}

**拥塞避免 \-- WRED表配置命令 \-- queue**

------------------------------------------------------------------------

[**[queue]{lang="EN-US"}**]{#struct_0_14687_18620_x400610655}[命令用来配置基于队列的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表的内容。]{style="font-family:宋体"}

[**[undo queue]{lang="EN-US"}**]{#struct_0_14687_18620_x82045676}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x306833368}

[**[queue]{lang="EN-US"}**[ *queue-id* \[ **drop-level** *drop-level* \] **low-limit** *low-limit* **high-limit** *high-limit* \[ **discard-probability** *discard-prob* \]]{lang="EN-US"}]{#struct_0_14687_18620_x112689847}

[**[undo queue ]{lang="EN-US"}**[{ *queue-id* \| **all** }]{lang="EN-US"}]{#struct_0_14687_18620_1192362784}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x134778990}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_1956808599}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_448055528}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_2108139921}[表视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x82242284}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x432280942}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1244062189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_454711960}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_1914783716}[：队列编号。]{style="font-family:宋体"}

[**[drop-level ]{lang="EN-US"}***[drop-level]{lang="EN-US"}*]{#struct_0_14687_18620_426485492}[：丢弃级别，在进行报文丢弃时参考的参数，]{style="font-family:宋体"}[0]{lang="EN-US"}[对应绿色报文、]{style="font-family:宋体"}[1]{lang="EN-US"}[对应黄色报文、]{style="font-family:宋体"}[2]{lang="EN-US"}[对应红色报文。如果未指定本参数，后续配置的参数对该队列所有丢弃级别的报文都生效。]{style="font-family:宋体"}

[**[low-limit]{lang="EN-US"}***[ low-limit]{lang="EN-US"}*]{#struct_0_14687_18620_2125664203}[：队列平均长度的下限。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[high-limit]{lang="EN-US"}***[ high-limit]{lang="EN-US"}*]{#struct_0_14687_18620_x1665379019}[：队列平均长度的上限。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[discard-probability]{lang="EN-US"}***[ discard-prob]{lang="EN-US"}*]{#struct_0_14687_18620_x82176748}[：丢弃概率的分母，取值越大，计算出的丢弃概率越小。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1243253992}

[[当队列平均长度小于下限时，不丢弃报文。当队列平均长度在上限和下限之间时，设备随机丢弃报文，队列越长，丢弃概率越高。当队列平均长度超过上限时，丢弃所有到来的报文。]{style="font-family:宋体"}]{#struct_0_14687_18620_1781190516}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x937461935}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1192989191}[配置基于队列的]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表]{style="font-family:宋体"}[queue-table1]{lang="EN-US"}[中队列]{style="font-family:宋体"}[1]{lang="EN-US"}[的丢弃参数：丢弃级别为]{style="font-family:宋体"}[1]{lang="EN-US"}[，队列平均长度的下限为]{style="font-family:宋体"}[10]{lang="EN-US"}[，队列平均长度的上限为]{style="font-family:宋体"}[20]{lang="EN-US"}[，丢弃概率的分母为]{style="font-family:宋体"}[30%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x556049666}

[\[Sysname\] qos wred queue table queue-table1]{lang="EN-US"}

[\[Sysname-wred-table-queue-table1\] queue 1 drop-level 1 low-limit 10 high-limit 20 discard-probability 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x714923553}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x81849068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_1530974885}
:::

::: {#-552530838 .myid}
[]{#_Toc292899236}[]{#_Toc291750099}[]{#_Toc263760047}[]{#_Toc226262709}[]{#_Toc198110223}[]{#_Toc404792469}[]{#struct_0_14687_18620_427770255}[]{#_Toc309812054}

**拥塞避免 \-- WRED表配置命令 \-- queue ecn**

------------------------------------------------------------------------

[**[queue ecn]{lang="EN-US"}**]{#struct_0_14687_18620_x587527774}[命令用来对指定队列开启拥塞通知功能。]{style="font-family:宋体"}

[**[undo queue ecn]{lang="EN-US"}**]{#struct_0_14687_18620_x783506784}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1628777992}

[**[queue]{lang="EN-US"}**[ *queue-id* **ecn**]{lang="EN-US"}]{#struct_0_14687_18620_1295630058}

[**[undo queue ]{lang="EN-US"}***[queue-id ]{lang="EN-US"}***[ecn]{lang="EN-US"}**]{#struct_0_14687_18620_196368486}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81783532}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_14687_18620_x281988876}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_747544690}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_571528767}[表视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1035167992}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1681803484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1116365670}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_187676520}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x81980140}[：队列编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_x51028346}

[[在报文的发送端和接收端都支持]{style="font-family:宋体"}[ECN]{lang="EN-US"}]{#struct_0_14687_18620_x118590429}[功能时，设备可以通过对]{style="font-family:宋体"}[ECN]{lang="EN-US"}[域的识别和标记将拥塞状况告知终端，避免拥塞加剧。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1162269308}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x540597295}[在]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表]{style="font-family:宋体"}[queue-table1]{lang="EN-US"}[中，对队列]{style="font-family:宋体"}[1]{lang="EN-US"}[开启拥塞通知功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1525860910}

[\[Sysname\] qos wred queue table queue-table1]{lang="EN-US"}

[\[Sysname-wred-table-queue-table1\] queue 1 ecn]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_436482776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x868520552}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x81914604}
:::

::: {#168379057 .myid}
[]{#_Toc404792470}[]{#struct_0_14687_18620_301710156}

**拥塞避免 \-- WRED表配置命令 \-- queue weighting-constant**

------------------------------------------------------------------------

[**[queue weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_805472239}[命令用来配置计算平均队列长度的指数。]{style="font-family:
宋体"}

[**[undo queue weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_1515476312}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_795798999}

[**[queue]{lang="EN-US"}**[ *queue-id* **weighting-constant** *exponent* ]{lang="EN-US"}]{#struct_0_14687_18620_x1094632278}

[**[undo queue ]{lang="EN-US"}***[queue-id ]{lang="EN-US"}***[weighting-constant]{lang="EN-US"}**]{#struct_0_14687_18620_1799316018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x81586924}

[[计算平均队列长度的指数为]{style="font-family:宋体"}[9]{lang="EN-US"}]{#struct_0_14687_18620_573375322}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1072400042}

[[WRED]{lang="EN-US"}]{#struct_0_14687_18620_2019043670}[表视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1338729766}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1396944785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_993339898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1679828954}

[*[queue-id]{lang="EN-US"}*]{#struct_0_14687_18620_x81521388}[：队列编号。]{style="font-family:宋体"}

[**[weighting-constant]{lang="EN-US"}***[ exponent]{lang="EN-US"}*]{#struct_0_14687_18620_1452766242}[：计算平均队列长度的指数，]{style="font-family:宋体"}*[exponent]{lang="EN-US"}*[的取值范围和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1369532690}

[[平均队列长度的指数越大，计算平均队列长度时对队列的实时变化越不敏感。计算队列平均长度的公式为：平均队列长度]{style="font-family:宋体"}[=]{lang="EN-US"}]{#struct_0_14687_18620_1210268776}[（以前的平均队列长度×（]{style="font-family:宋体"}[1-1/[2^n^]{style="color:black"}]{lang="EN-US"}[））＋（当前队列长度×（]{style="font-family:宋体"}[1/[2^n^]{style="color:black"}]{lang="EN-US"}[））。其中]{style="font-family:宋体"}[n]{lang="EN-US"}[表示指数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x2136036800}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1173047737}[在]{style="font-family:宋体"}[WRED]{lang="EN-US"}[表]{style="font-family:宋体"}[queue-table1]{lang="EN-US"}[中，配置计算平均队列长度的指数为]{style="font-family:宋体"}[12]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_2078257142}

[\[Sysname\] qos wred queue table queue-table1]{lang="EN-US"}

[\[Sysname-wred-table-queue-table1\] queue 1 weighting-constant 12]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_105606983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x1997806374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qos wred table]{lang="EN-US"}**]{#struct_0_14687_18620_x605400176}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section8 style="layout-grid:15.85pt"}
:::

::: {#1303569074 .myid}
[]{#_Toc404792473}[]{#struct_0_14687_18620_463435541}[]{#_Toc312330790}

**全局CAR \-- 全局CAR配置命令 \-- car name**

------------------------------------------------------------------------

[**[car]{lang="EN-US"}**[ **name**]{lang="EN-US"}]{#struct_0_14687_18620_x1997871910}[命令用来配置全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[**[undo car]{lang="EN-US"}**]{#struct_0_14687_18620_x1404827843}[用来删除全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x496546240}

[**[car]{lang="EN-US"}**]{#struct_0_14687_18620_1089408832}[ ]{lang="EN-US"}**[name ]{lang="EN-US"}***[car-name ]{lang="EN-US"}*[\[ **hierarchy-car** *hierarchy-car-name* \[ **mode** { **and** \| **or** } \] \]]{lang="EN-US"}

[**[undo car]{lang="EN-US"}**]{#struct_0_14687_18620_1072222743}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1000792445}

[[没有配置全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_1858514541}[动作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1345540606}

[[流行为视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1997937446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_584241274}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_451955236}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x667089132}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x222760923}

[*[car-name]{lang="EN-US"}*]{#struct_0_14687_18620_102039933}[：聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[hierarchy-car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x99594887}[：分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[mode]{lang="EN-US"}**]{#struct_0_14687_18620_x1268088403}[：分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[和聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作的合作模式。有]{style="font-family:宋体"}**[and]{lang="EN-US"}**[和]{style="font-family:宋体"}**[or]{lang="EN-US"}**[两种模式，默认为]{style="font-family:宋体"}**[and]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[and]{lang="EN-US"}**]{#struct_0_14687_18620_x1998002982}[：在该模式下，对于多条数据流应用同一个分层]{style="font-family:
宋体"}[CAR]{lang="EN-US"}[，必须每条流满足各自的聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置，同时各流量之和又满足分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置，流量才能正常通过。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[or]{lang="EN-US"}**]{#struct_0_14687_18620_38419755}[：在该模式下，对于多条数据流应用同一个分层]{style="font-family:
宋体"}[CAR]{lang="EN-US"}[，只要每条流满足各自的聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置或者各流量之和满足分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[配置，流量即可正常通过。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_881251839}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_309314360}[配置流行为]{style="font-family:宋体"}[be1]{lang="EN-US"}[的聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作为]{style="font-family:宋体"}[aggcar-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_843379259}

[\[Sysname\] traffic behavior be1]{lang="EN-US"}

[\[Sysname-behavior-be1\] car name aggcar-1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_813045710}[配置流行为]{style="font-family:宋体"}[be1]{lang="EN-US"}[的聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作为]{style="font-family:宋体"}[aggcar-1]{lang="EN-US"}[，分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[动作为]{style="font-family:宋体"}[hcar]{lang="EN-US"}[，合作模式为]{style="font-family:宋体"}[or]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1300574097}

[\[Sysname\] traffic behavior be1]{lang="EN-US"}

[\[Sysname-behavior-be1\] car name aggcar-1 hierarchy-car hcar mode or]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1998068518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos car name]{lang="EN-US"}**]{#struct_0_14687_18620_x952547389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display traffic behavior user-defined]{lang="EN-US"}**]{#struct_0_14687_18620_1538966069}
:::

::: {#-711088594 .myid}
[]{#_Toc404792474}[]{#struct_0_14687_18620_232073923}[]{#_Toc312330791}

**全局CAR \-- 全局CAR配置命令 \-- display qos car name**

------------------------------------------------------------------------

[**[display qos car name]{lang="EN-US"}**]{#struct_0_14687_18620_1512849588}[命令用来显示全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x259509151}

[**[display qos car name]{lang="EN-US"}**[ \[ *car-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_1820140204}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x721472575}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998134054}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1898166805}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x699383356}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_x801781747}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_759260700}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1516024475}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x133441641}

[*[car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1036947972}[：全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。显示指定全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息。如果未指定本参数，将显示所有全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息，包含聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[和分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1998199590}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1054033982}[显示全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息。（]{style="font-family:宋体"}[集中式设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display qos car name]{lang="EN-US"}]{#struct_0_14687_18620_x1998265126}

[ Name: a]{lang="EN-US"}

[  Mode: aggregative]{lang="EN-US"}

[   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Name: b]{lang="EN-US"}

[  Mode: hierarchy]{lang="EN-US"}

[   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x370385263}[显示全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息。（]{style="font-family:宋体"}[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display qos car name]{lang="EN-US"}]{#struct_0_14687_18620_x1997282086}

[ Name: a]{lang="EN-US"}

[  Mode: aggregative]{lang="EN-US"}

[   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Slot 1:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Slot 2:]{lang="EN-US"}

[   Apply failed]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Name: b]{lang="EN-US"}

[  Mode: hierarchy]{lang="EN-US"}

[   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Slot 1:]{lang="EN-US"}

[   Apply failed]{lang="EN-US"}

[  Slot 2:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1153553793}[显示全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置和统计信息。（]{style="font-family:宋体"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display qos car name]{lang="EN-US"}]{#struct_0_14687_18620_x1997806373}

[ Name: a]{lang="EN-US"}

[  Mode: aggregative]{lang="EN-US"}

[   CIR 33 (kbps) CBS: 2062 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Chassis 1 Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Chassis 2 Slot 1:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Chassis 2 Slot 2:]{lang="EN-US"}

[   Apply failed]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Name: b]{lang="EN-US"}

[  Mode: hierarchy]{lang="EN-US"}

[   CIR 55 (kbps) CBS: 3437 (Bytes) PIR: 888 (kbps) EBS: 0 (Bytes)]{lang="EN-US"}

[   Green action  : pass]{lang="EN-US"}

[   Yellow action : pass]{lang="EN-US"}

[   Red action    : discard]{lang="EN-US"}

[  Chassis 1 Slot 0:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[  Chassis 2 Slot 1:]{lang="EN-US"}

[   Apply failed]{lang="EN-US"}

[  Chassis 2 Slot 2:]{lang="EN-US"}

[   Green packets : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Yellow packets: 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[   Red packets   : 0 (Packets), 0 (Bytes)]{lang="EN-US"}

[[表7-1 ]{lang="EN-US"}[display qos car name]{lang="EN-US"}]{#struct_0_14687_18620_x1008684703}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1732046873}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1749832583}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_455563679}

[[Name]{lang="EN-US"}]{#struct_0_14687_18620_632116520}

[[全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_390510633}[的名称]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_14687_18620_x1997871909}

[[全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_x195039798}[的类型]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[aggregative]{lang="EN-US"}]{#struct_0_14687_18620_143199173}[：聚合]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[hierarchy]{lang="EN-US"}]{#struct_0_14687_18620_x198467752}[：分层]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}

[[CIR  CBS  PIR  EBS]{lang="EN-US"}]{#struct_0_14687_18620_x169239869}

[[流量监管流量的参数配置]{style="font-family:宋体"}]{#struct_0_14687_18620_187625567}

[[Green action]{lang="EN-US"}]{#struct_0_14687_18620_x1997937445}

[[对绿色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x981842667}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[discard]{lang="EN-US"}]{#struct_0_14687_18620_1526422582}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_14687_18620_x544072551}[：允许报文通过]{style="font-family:宋体"}

[[Yellow action]{lang="EN-US"}]{#struct_0_14687_18620_x1998002981}

[[对黄色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x364864772}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[discard]{lang="EN-US"}]{#struct_0_14687_18620_x453577679}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_14687_18620_x577977808}[：允许报文通过]{style="font-family:宋体"}

[[Red action]{lang="EN-US"}]{#struct_0_14687_18620_x996390422}

[[对红色报文的动作]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998068517}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[discard]{lang="EN-US"}]{#struct_0_14687_18620_613536552}[：丢弃报文]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[pass]{lang="EN-US"}]{#struct_0_14687_18620_x754995218}[：允许报文通过]{style="font-family:宋体"}

[[Green packets]{lang="EN-US"}]{#struct_0_14687_18620_x1040012315}

[[绿色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998134053}

[[Yellow packets]{lang="EN-US"}]{#struct_0_14687_18620_x24147496}

[[黄色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_1922186984}

[[Red packets]{lang="EN-US"}]{#struct_0_14687_18620_x610252157}

[[红色报文的流量统计]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998199589}

[ ]{lang="EN-US"}

::: {#1199209200 .myid}
[]{#_Toc404792475}[]{#struct_0_14687_18620_868345855}[]{#_Toc312330792}

**全局CAR \-- 全局CAR配置命令 \-- qos car (interface view)**

------------------------------------------------------------------------

[**[qos]{lang="EN-US"}**[ **car**]{lang="EN-US"}]{#struct_0_14687_18620_709815225}[命令用来在接口上应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo qos car]{lang="EN-US"}**]{#struct_0_14687_18620_x1135585841}[命令用来删除接口上应用的聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1231969162}

[**[qos car]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-number* } **name** *car-name*]{lang="EN-US"}]{#struct_0_14687_18620_696665139}

[**[undo qos car ]{lang="EN-US"}**[{ **inbound** \| **outbound** } { **any** \| **acl** \[ **ipv6** \] *acl-number* }]{lang="EN-US"}]{#struct_0_14687_18620_x1998265125}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1195698678}

[[没有在接口上应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_895202188}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_791529991}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_436345753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x341479543}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x698799419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_418450643}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1997282085}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1556838320}[：对接口接收到的数据包应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_1603487811}[：对接口发送的数据包应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_14687_18620_x1878163145}[：对所有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_14687_18620_1008358902}[：对匹配]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[的数据包应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[acl ipv6 ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_14687_18620_774686949}[：对匹配]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的数据包应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1406057277}[：聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1348895751}

[[用户可以在接口上重复执行本命令，从而在接口上应用多个聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_x1997347621}[，各个聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的执行顺序与配置顺序一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1686624482}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2147075111}[在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的入方向上对满足]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则]{style="font-family:宋体"}[2000]{lang="EN-US"}[的报文应用聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[策略]{style="font-family:宋体"}[aggcar-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1678648955}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] qos car inbound ACL 2000 name aggcar-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_109928686}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos car interface]{lang="EN-US"}**]{#struct_0_14687_18620_x420068825}
:::

::: {#294603688 .myid}
[]{#_Toc404792476}[]{#struct_0_14687_18620_2013111630}[]{#_Toc312330793}

**全局CAR \-- 全局CAR配置命令 \-- qos car (system view)**

------------------------------------------------------------------------

[**[qos car]{lang="EN-US"}**]{#struct_0_14687_18620_x1997806376}[命令用来配置聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[或分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **qos car**]{lang="EN-US"}]{#struct_0_14687_18620_x1768199590}[命令用来取消聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[或分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1744643927}

[**[qos car ]{lang="EN-US"}***[car-name ]{lang="EN-US"}*[{ **aggregative** \| **hierarchy** } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \[ **ebs** *excess-burst-size* \] \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_1154666230}

[**[qos car ]{lang="EN-US"}***[car-name ]{lang="EN-US"}*[{ **aggregative** \| **hierarchy** } **cir** *committed-information-rate* \[ **cbs** *committed-burst-size* \] **pir** *peak-information-rate* \[ **ebs** *excess-burst-size* \] \[ **green** *action* \| **red** *action* \| **yellow** *action* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_1328176646}

[**[undo qos car ]{lang="EN-US"}***[car-name]{lang="EN-US"}*]{#struct_0_14687_18620_939551018}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_1935832618}

[[没有配置聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_14687_18620_103152968}[或分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1502264131}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1997871912}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1727340039}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_113521663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_1564879908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1835934342}

[*[car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1988804212}[：全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[aggregative]{lang="EN-US"}**]{#struct_0_14687_18620_722615590}[：该全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[为聚合模式。]{style="font-family:宋体"}

[**[hierarchy]{lang="EN-US"}**]{#struct_0_14687_18620_1035779178}[：该全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[为分层模式。]{style="font-family:宋体"}

[**[cir ]{lang="EN-US"}***[committed-information-rate]{lang="EN-US"}*]{#struct_0_14687_18620_x1997937448}[：承诺信息速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[cbs]{lang="EN-US"}**[ *committed-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_x934788500}[：承诺突发尺寸，即实际平均速率在承诺速率以内时的突发流量，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ebs]{lang="EN-US"}**[ *excess-burst-size*]{lang="EN-US"}]{#struct_0_14687_18620_479299470}[：过度突发尺寸，单位为]{style="font-family:宋体"}[byte]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pir]{lang="EN-US"}**[ *peak-information-rate*]{lang="EN-US"}]{#struct_0_14687_18620_x1353509684}[：峰值速率，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。取值范围和缺省值与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[green ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_1519385744}[：数据包的流量符合承诺速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[red ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_x699440356}[：数据包的流量既不符合承诺速率也不符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[yellow ]{lang="EN-US"}***[action]{lang="EN-US"}*]{#struct_0_14687_18620_x1172298199}[：数据包的流量不符合承诺速率但是符合峰值速率时对数据包采取的动作，缺省动作为]{style="font-family:宋体"}**[pass]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[action]{lang="EN-US"}*]{#struct_0_14687_18620_2143963526}[：对数据包采取的动作，有以下几种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[discard]{lang="EN-US"}**]{#struct_0_14687_18620_x1998002984}[：丢弃数据包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pass]{lang="EN-US"}**]{#struct_0_14687_18620_x1124379659}[：允许数据包通过。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-atmclp-continue]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_1218315820}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-atmclp-pass]{lang="EN-US"}**[ *new-atmclp*]{lang="EN-US"}]{#struct_0_14687_18620_x1153735909}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[ATM]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:
宋体"}[CLP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dot1p-continue]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_381174707}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dot1p-pass]{lang="EN-US"}**[ *new-cos*]{lang="EN-US"}]{#struct_0_14687_18620_466383204}[：设置新的]{lang="EN-US" style="font-family:宋体"}[802.1P]{lang="EN-US"}[报文的优先级值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dscp-continue]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_397289106}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-dscp-pass]{lang="EN-US"}**[ *new-dscp*]{lang="EN-US"}]{#struct_0_14687_18620_2049357436}[：设置报文新的]{lang="EN-US" style="font-family:宋体"}[DSCP]{lang="EN-US"}[值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{lang="EN-US" style="font-family:宋体"}**[af11]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af12]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af13]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af21]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af22]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af23]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af31]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af32]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af33]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af41]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af42]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[af43]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs1]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs2]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs3]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs4]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs5]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[cs7]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ef]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-frde-continue]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_x1998068520}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-frde-pass]{lang="EN-US"}**[ *new-frde*]{lang="EN-US"}]{#struct_0_14687_18620_x1308974357}[：设置新的]{lang="EN-US" style="font-family:宋体"}[FR]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[DE]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-mpls-exp-continue]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_x1132959897}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并继续由下一个]{lang="EN-US" style="font-family:宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-mpls-exp-pass]{lang="EN-US"}**[ *new-exp*]{lang="EN-US"}]{#struct_0_14687_18620_122039356}[：设置新的]{lang="EN-US" style="font-family:宋体"}[MPLS]{lang="EN-US"}[报文的]{lang="EN-US" style="font-family:宋体"}[EXP]{lang="EN-US"}[标志位的值，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-prec-continue]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_181899730}[：设置新的]{lang="EN-US" style="font-family:
宋体"}[IP]{lang="EN-US"}[优先级，并继续由下一个]{lang="EN-US" style="font-family:
宋体"}[CAR]{lang="EN-US"}[策略处理，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remark-prec-pass]{lang="EN-US"}**[ *new-precedence*]{lang="EN-US"}]{#struct_0_14687_18620_x1226737511}[：设置新的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，并允许数据包通过，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_122446042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合]{style="font-family:宋体"}]{#struct_0_14687_18620_322253662}[CAR]{lang="EN-US"}[配置需要在接口上应用或在策略中引用后才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[分层]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998134056}[CAR]{lang="EN-US"}[配置需要在策略中引用后才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不配置峰值速率表示所配置的是单速桶流量监管，否则表示双速桶流量监管。]{style="font-family:宋体"}]{#struct_0_14687_18620_x755398562}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_735367391}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1722395795}[配置聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[采取的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数取值，]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[取值为]{style="font-family:宋体"}[200]{lang="EN-US"}[，]{style="font-family:宋体"}**[cbs]{lang="EN-US"}**[取值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[，对于红色报文采取丢弃的动作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1172756008}

[\[Sysname\] qos car aggcar-1 aggregative cir 200 cbs 2000 red discard]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x851513272}[配置分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[采取的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数取值，]{style="font-family:宋体"}**[cir]{lang="EN-US"}**[取值为]{style="font-family:宋体"}[120]{lang="EN-US"}[，]{style="font-family:宋体"}**[cbs]{lang="EN-US"}**[取值为]{style="font-family:宋体"}[4000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2029546340}

[\[Sysname\] qos car h-car hierarchy cir 120 cbs 4000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x374948125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos car name]{lang="EN-US"}**]{#struct_0_14687_18620_x1998199592}
:::

::: {#-1787415573 .myid}
[]{#_Toc404792477}[]{#struct_0_14687_18620_108765432}[]{#_Toc312330794}

**全局CAR \-- 全局CAR配置命令 \-- reset qos car name**

------------------------------------------------------------------------

[**[reset qos car name]{lang="EN-US"}**]{#struct_0_14687_18620_x1103869542}[命令用来清除全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1500749822}

[**[reset qos car name]{lang="EN-US"}**[ \[ *car-name* \]]{lang="EN-US"}]{#struct_0_14687_18620_523582713}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x281172769}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1240573141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_929382340}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1998265128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_792414151}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1525190359}

[*[car-name]{lang="EN-US"}*]{#struct_0_14687_18620_x1981926461}[：全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的名称，首字符需要以字母开头，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。清除指定全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的统计信息。如果未指定本参数，将清除所有全局]{style="font-family:宋体"}[CAR]{lang="EN-US"}[的统计信息，包含聚合]{style="font-family:宋体"}[CAR]{lang="EN-US"}[和分层]{style="font-family:宋体"}[CAR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_863406580}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1695488100}[清除全局]{style="font-family:宋体"}[CAR aggcar-1]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> reset qos car name aggcar-1]{lang="EN-US"}]{#struct_0_14687_18620_887851711}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section9 style="layout-grid:15.85pt"}
:::

::: {#1447135005 .myid}
[]{#_Toc404792480}[]{#struct_0_14687_18620_x1603892487}[]{#_Toc307323638}[]{#_Toc265568516}[]{#_Toc263760081}[]{#_Toc226262748}[]{#_Toc198110271}

**报文统计配置命令 \-- 报文统计配置命令 \-- display qos traffic-counter**

------------------------------------------------------------------------

[**[display qos traffic-counter]{lang="EN-US"}**]{#struct_0_14687_18620_x1201257312}[命令用来显示报文统计信息和计数器的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x292772662}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_1886403856}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x950533554}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1831562082}[模式：]{style="font-family:宋体"}

[**[display qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1441153912}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1997347624}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x2089909009}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x613691595}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1356750412}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1411523761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1065048405}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_59341318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_654938176}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1997806375}[：]{style="font-family:宋体"}[入方向报文统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_2123483179}[：出方向报文统计。]{style="font-family:宋体"}

[**[counter0]{lang="EN-US"}**]{#struct_0_14687_18620_1550550451}**[：]{style="font-family:宋体"}**[计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[counter1]{lang="EN-US"}**]{#struct_0_14687_18620_x1063836568}**[：]{style="font-family:宋体"}**[计数器]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1320081007}[：显示指定单板的报文统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1531750523}[：显示指定成员设备的报文统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_360362815}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的报文统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_1958941879}[：显示指定成员设备上指定单板的报文统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1903116154}[：]{style="font-family:宋体"}[显示指定单板的报文统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_674410322}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1997871911}[显示]{style="font-family:宋体"}[4]{lang="EN-US"}[号板的出方向报文统计信息和计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos traffic-counter outbound counter0 slot 4]{lang="EN-US"}]{#struct_0_14687_18620_161256098}

[Slot 4 outbound counter0 mode:]{lang="EN-US"}

[ Interface: all]{lang="EN-US"}

[ VLAN: all]{lang="EN-US"}

[ Local precedence: all]{lang="EN-US"}

[ Drop priority: all]{lang="EN-US"}

[ Traffic-counter summary:]{lang="EN-US"}

[  Unicast: 1 packets]{lang="EN-US"}

[  Multicast: 1 packets]{lang="EN-US"}

[  Broadcast: 1 packets]{lang="EN-US"}

[  Control packets: 1 packets]{lang="EN-US"}

[  Bridge egress filtered packets: 1 packets]{lang="EN-US"}

[  Tail drop packets: 1 packets]{lang="EN-US"}

[  Tail drop multicast packets: 1 packets]{lang="EN-US"}

[  Forwarding restrictions packets: 1 packets]{lang="EN-US"}

[]{#_Toc307323639}[]{#_Toc265568517}[]{#_Toc263760082}[]{#_Toc226262749}[]{#_Toc198110272}[[表8-1 ]{lang="EN-US"}[display qos traffic-counter]{lang="EN-US"}]{#struct_0_14687_18620_1417217161}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2029234553}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_x1997937447}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_x2144642081}

[[Slot 4 outbound counter0 mode]{lang="EN-US"}]{#struct_0_14687_18620_x1606009931}

[[单板上某计数器统计出方向流量的监控对象]{style="font-family:宋体"}]{#struct_0_14687_18620_x58108317}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_1504497513}

[[本计数器所统计的接口]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998002983}

[[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_x1527664186}

[[本计数器所统计的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_x1291801690}

[[Local precedence]{lang="EN-US"}]{#struct_0_14687_18620_x1885885248}

[[本计数器所统计的本地优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_x1138785766}

[[Drop priority]{lang="EN-US"}]{#struct_0_14687_18620_x1998068519}

[[本计数器所统计的丢弃优先级]{style="font-family:宋体"}]{#struct_0_14687_18620_1776335966}

[[Traffic-counter summary]{lang="EN-US"}]{#struct_0_14687_18620_472617724}

[[本计数器统计信息汇总]{style="font-family:宋体"}]{#struct_0_14687_18620_1267706332}

[[Unicast]{lang="EN-US"}]{#struct_0_14687_18620_819728144}

[[单播报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998134055}

[[Multicast]{lang="EN-US"}]{#struct_0_14687_18620_x830716550}

[[组播报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_1389164925}

[[Broadcast]{lang="EN-US"}]{#struct_0_14687_18620_1067665853}

[[广播报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998199591}

[[Control packets]{lang="EN-US"}]{#struct_0_14687_18620_512049959}

[[控制报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_x696042294}

[[Bridge egress filtered packets]{lang="EN-US"}]{#struct_0_14687_18620_x1378665469}

[[下行桥过滤报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998265127}

[[Tail drop packets]{lang="EN-US"}]{#struct_0_14687_18620_x1936469204}

[[尾丢弃报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_233796888}

[[Tail drop multicast packets]{lang="EN-US"}]{#struct_0_14687_18620_x697193439}

[[尾丢弃组播报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1997282087}

[[Forwarding restrictions packets]{lang="EN-US"}]{#struct_0_14687_18620_1575329562}

[[禁止转发报文数]{style="font-family:宋体"}]{#struct_0_14687_18620_376183736}

[ ]{lang="EN-US"}

::: {#342909688 .myid}
[]{#_Toc404792481}[]{#struct_0_14687_18620_x1290044904}

**报文统计配置命令 \-- 报文统计配置命令 \-- qos traffic-counter**

------------------------------------------------------------------------

[**[qos traffic-counter]{lang="EN-US"}**]{#struct_0_14687_18620_1422745308}[命令用来使能报文统计功能，并指定统计的流量类型。]{style="font-family:宋体"}

[**[undo qos traffic-counter]{lang="EN-US"}**]{#struct_0_14687_18620_x1997347623}[命令用来关闭报文统计功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1445543400}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x2031563112}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number* \[ **drop-priority** *drop-priority* \| **interface** *interface-type interface-number* \| **local-precedence** *local-precedence* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x1018772271}

[**[undo qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_302797413}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_376330190}[模式：]{style="font-family:宋体"}

[**[qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number* \[ **drop-priority** *drop-priority* \| **interface** *interface-type interface-number* \| **local-precedence** *local-precedence* \| **vlan** *vlan-id* \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x2120892541}

[**[undo qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x1138061241}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1997806378}

[[报文统计功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_14687_18620_1363968292}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1427526186}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x245567349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1641990700}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_802439854}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1145900378}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1997871914}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_564540625}[：]{style="font-family:宋体"}[入方向报文统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_967014328}[：出方向报文统计。]{style="font-family:宋体"}

[**[counter0]{lang="EN-US"}**]{#struct_0_14687_18620_1835386770}[：计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[counter1]{lang="EN-US"}**]{#struct_0_14687_18620_x45929465}[：计数器]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_x632414346}[：在指定单板上使能报文统计功能。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_708710442}[：在指定成员设备上使能报文统计功能。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_91296016}[：在指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上使能报文统计功能。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_858927163}[：在指定成员设备的指定单板上使能报文统计功能。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x999581276}[：在指定单板上使能报文统计功能。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[drop-priority]{lang="EN-US" style="font-size:10.0pt"}***[ drop-priority]{lang="EN-US"}*]{#struct_0_14687_18620_x1997937450}[：丢弃优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_x578623676}[：指定绑定的端口类型和端口编号。]{style="font-family:宋体"}

[**[local-precedence]{lang="EN-US"}***[ local-precedence]{lang="EN-US"}*]{#struct_0_14687_18620_x1890683042}[：本地优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。本参数的支持情况和设备的型号有关，请以设备的实际情况为准。]{style="font-family:
宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_14687_18620_x752368203}[：]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_542873375}

[[一块单板提供两组计数器用于统计单板流量，监控的对象可以是端口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_14687_18620_1071219025}[、本地优先级和丢弃优先级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当不指定端口时，则监控单板上所有端口的流量。]{style="font-family:宋体"}]{#struct_0_14687_18620_1903172564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当不指定]{style="font-family:宋体"}]{#struct_0_14687_18620_x1945224553}[VLAN]{lang="EN-US"}[时，则监控所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的流量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当不指定本地优先级时，则监控所有本地优先级的流量。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998002986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当不指定丢弃优先级时，则监控所有丢弃优先级的流量。]{style="font-family:宋体"}]{#struct_0_14687_18620_2007788223}

[[需要注意的是，使用]{style="font-family:宋体"}**[qos traffic-counter]{lang="EN-US"}**]{#struct_0_14687_18620_998292516}[命令重新设置某单板的监控对象后，计数器的值会自动清空。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1372904812}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_623183437}[配置]{style="font-family:宋体"}[4]{lang="EN-US"}[号板的计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[统计]{style="font-family:宋体"}[GigabitEthernet4/1/1]{lang="EN-US"}[端口的出方向流量。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_1133848113}

[\[Sysname\] qos traffic-counter outbound counter0 slot 4 interface gigabitethernet 4/1/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x672941846}[配置]{style="font-family:宋体"}[4]{lang="EN-US"}[号成员设备的计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[统计]{style="font-family:宋体"}[GigabitEthernet4/1/1]{lang="EN-US"}[端口的出方向流量。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1998068522}

[\[Sysname\] qos traffic-counter outbound counter0 slot 4 interface gigabitethernet 4/1/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x146174943}[配置]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[4]{lang="EN-US"}[号板的计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[统计]{style="font-family:宋体"}[GigabitEthernet1/4/1/1]{lang="EN-US"}[端口的出方向流量。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x2043724197}

[\[Sysname\] qos traffic-counter outbound counter0 chassis 1 slot 4 interface gigabitethernet 1/4/1/1]{lang="EN-US"}
:::

::: {#270693277 .myid}
[]{#_Toc404792482}[]{#struct_0_14687_18620_x1646460200}[]{#_Toc307323640}[]{#_Toc265568518}[]{#_Toc263760083}[]{#_Toc226262750}[]{#_Toc198110273}

**报文统计配置命令 \-- 报文统计配置命令 \-- reset qos traffic-counter**

------------------------------------------------------------------------

[**[reset qos traffic-counter]{lang="EN-US"}**]{#struct_0_14687_18620_1351398647}[命令用来清除报文统计计数器的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_577227272}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_14687_18620_x1652814472}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x212576613}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_14687_18620_x1998134058}[模式：]{style="font-family:宋体"}

[**[reset qos traffic-counter]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **counter0** \| **counter1** } **chassis** *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_x783662383}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1480565763}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1195496091}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1802661615}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_1103750530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1292426356}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_1461942332}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1998199594}[：]{style="font-family:宋体"}[入方向报文统计。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_915334486}[：出方向报文统计。]{style="font-family:宋体"}

[**[counter0]{lang="EN-US"}**]{#struct_0_14687_18620_1464103118}[：计数器]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[counter1]{lang="EN-US"}**]{#struct_0_14687_18620_793555327}[：计数器]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_890007444}[：清除指定单板的报文统计计数器的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_1297813475}[：清除指定成员设备的报文统计计数器的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}***[ slot-number]{lang="EN-US"}*]{#struct_0_14687_18620_2060664484}[：清除指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的报文统计计数器的统计信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_99285465}[：清除指定成员设备上指定单板的报文统计计数器的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_14687_18620_155261425}[：清除指定单板的报文统计计数器的统计信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_590953426}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1998265130}[清除]{style="font-family:宋体"}[4]{lang="EN-US"}[号板的出方向报文统计计数器的统计信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[[\<Sysname\> reset qos traffic-counter outbound counter0 slot 4]{lang="EN-US"}]{#struct_0_14687_18620_436249327}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1520722655}[清除]{style="font-family:宋体"}[4]{lang="EN-US"}[号成员设备的出方向报文统计计数器的统计信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> reset qos traffic-counter outbound counter0 slot 4]{lang="EN-US"}]{#struct_0_14687_18620_x743638331}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_1223145062}[清除]{style="font-family:宋体"}[1]{lang="EN-US"}[号成员设备]{style="font-family:宋体"}[4]{lang="EN-US"}[号板的出方向报文统计计数器的统计信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> reset qos traffic-counter outbound counter0 chassis 1 slot 4]{lang="EN-US"}]{#struct_0_14687_18620_476042738}
:::

[\
]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

::: {.Section10 style="layout-grid:15.85pt"}
:::

::: {#-1368442782 .myid}
[]{#_Toc404792485}[]{#struct_0_14687_18620_x1960057311}[]{#_Toc307323643}[]{#_Toc291750138}[]{#_Toc263760086}[]{#_Toc226262753}[]{#_Toc198000724}

**端口队列统计 \-- 端口队列统计配置命令 \-- display qos queue-statistics interface outbound**

------------------------------------------------------------------------

[**[display qos queue-statistics interface outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1367380998}[命令用来显示]{style="font-family:宋体"}[端口队列出方向的统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1646709115}

[**[display qos queue-statistics]{lang="EN-US"}**[ **interface** \[ *interface-type interface-number* \] **outbound**]{lang="EN-US"}]{#struct_0_14687_18620_393501926}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_92093648}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14687_18620_793044868}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x34431103}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1997347626}

[[network-operator]{lang="EN-US"}]{#struct_0_14687_18620_1042258873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x2025920271}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14687_18620_1762138593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x555503925}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_1848218778}[：指定接口类型和接口编号。如果未指定本参数，将显示所有接口的队列出方向统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1953437455}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1306591854}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的队列出方向统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display qos queue-statistics interface gigabitethernet 1/0/1 outbound]{lang="EN-US"}]{#struct_0_14687_18620_x1998002985}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ Direction: outbound]{lang="EN-US"}

[ Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[ Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[ Queue 0]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 1]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 2]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 3]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 4]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 5]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 6]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[ Queue 7]{lang="EN-US"}

[  Forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Dropped: 1 packets, 1 bytes]{lang="EN-US"}

[  Green forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Green dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Yellow dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Red forwarded: 0 packets, 0 bytes]{lang="EN-US"}

[  Red dropped: 0 packets, 0 bytes]{lang="EN-US"}

[  Total queue length: 0 packets]{lang="EN-US"}

[  Current queue length: 0 packets, 0% use ratio]{lang="EN-US"}

[[表9-1 ]{lang="EN-US"}[display qos queue-statistics interface outbound]{lang="EN-US"}]{#struct_0_14687_18620_1604503696}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2023914265}[[字段]{style="font-family:黑体"}]{#struct_0_14687_18620_1510190770}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14687_18620_1433339146}

[[Interface]{lang="EN-US"}]{#struct_0_14687_18620_x1998068521}

[[端口队列统计的端口]{style="font-family:宋体"}]{#struct_0_14687_18620_1419908998}

[[Direction]{lang="EN-US"}]{#struct_0_14687_18620_x2089047841}

[[端口队列统计的方向]{style="font-family:宋体"}]{#struct_0_14687_18620_359483985}

[[Forwarded]{lang="EN-US"}]{#struct_0_14687_18620_x1262406324}

[[转发的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_x1998134057}

[[Dropped]{lang="EN-US"}]{#struct_0_14687_18620_x1993515964}

[[丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1384522839}

[[Queue 0]{lang="EN-US"}]{#struct_0_14687_18620_x504066664}[、]{style="font-family:宋体"}[Queue 1]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 2]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 3]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 4]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 5]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 6]{lang="EN-US"}[、]{style="font-family:宋体"}[Queue 7]{lang="EN-US"}

[[某端口队列统计信息]{style="font-family:宋体"}]{#struct_0_14687_18620_1052694961}

[[Green forwarded]{lang="EN-US"}]{#struct_0_14687_18620_x1998199593}

[[绿色报文转发的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1674849373}

[[Green dropped]{lang="EN-US"}]{#struct_0_14687_18620_x1101194606}

[[绿色报文丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_928193548}

[[Yellow forwarded]{lang="EN-US"}]{#struct_0_14687_18620_x1998265129}

[[黄色报文转发的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_x773669790}

[[Yellow dropped]{lang="EN-US"}]{#struct_0_14687_18620_x440407722}

[[黄色报文丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_x963589559}

[[Red forwarded]{lang="EN-US"}]{#struct_0_14687_18620_x1997282089}

[[红色报文转发的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1124990868}

[[Red dropped]{lang="EN-US"}]{#struct_0_14687_18620_x2054475077}

[[红色报文丢弃的数据包数目和字节数]{style="font-family:宋体"}]{#struct_0_14687_18620_1491376358}

[[Total queue length]{lang="EN-US"}]{#struct_0_14687_18620_x1997347625}

[[队列总长度]{style="font-family:宋体"}]{#struct_0_14687_18620_638974346}

[[Current queue length]{lang="EN-US"}]{#struct_0_14687_18620_353625161}

[[当前队列长度]{style="font-family:宋体"}]{#struct_0_14687_18620_x794257476}

[[use ratio]{lang="EN-US"}]{#struct_0_14687_18620_x431722433}

[[队列使用率]{style="font-family:宋体"}]{#struct_0_14687_18620_1368574959}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1552491922}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_14687_18620_x1974620173}[（]{lang="EN-US" style="font-family:宋体"}[接口管理]{style="font-family:宋体"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[以太网接口]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

::: {#-164062798 .myid}
[]{#_Toc404792486}[]{#struct_0_14687_18620_353959701}[]{#_Toc307323644}[]{#_Toc291750139}[]{#_Toc263760087}[]{#_Toc226262754}

**端口队列统计 \-- 端口队列统计配置命令 \-- qos queue-statistics**

------------------------------------------------------------------------

[**[qos queue-statistics ]{lang="EN-US"}**[{ **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_x1747931349}[命令用来]{style="font-family:宋体"}[使能端口队列统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo qos queue-statistics ]{lang="EN-US"}**[{ **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_x431787969}[命令用来]{style="font-family:宋体"}[关闭端口队列统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_1780778211}

[**[qos queue-statistics]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_614912567}

[**[undo qos queue-statistics]{lang="EN-US"}**[ { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_14687_18620_887670816}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1099060817}

[[端口队列统计功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_14687_18620_814120633}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1688755710}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14687_18620_1845921405}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_x431853505}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_606689202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_555425927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1129042916}

[**[inbound]{lang="EN-US"}**]{#struct_0_14687_18620_277328062}[：使能]{style="font-family:宋体"}[入方向]{style="font-family:宋体"}[端口队列统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_14687_18620_721823813}[：使能出方向]{style="font-family:宋体"}[端口队列统计功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_1777484934}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1900738831}[使能出方向端口队列统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1730186850}

[\[Sysname\] qos queue-statistics outbound]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1275686260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display qos queue-statistics]{lang="EN-US"}**[ **interface**]{lang="EN-US"}]{#struct_0_14687_18620_2113870779}**[ outbound]{lang="EN-US"}**
:::

::: {#-215784677 .myid}
[]{#_Toc404792487}[]{#struct_0_14687_18620_1306245174}

**端口队列统计 \-- 端口队列统计配置命令 \-- reset qos queue-statistics interface outbound**

------------------------------------------------------------------------

[**[reset qos queue-statistics interface outbound]{lang="EN-US"}**]{#struct_0_14687_18620_x1283036364}[命令用来清除端口队列出方向的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x845038072}

[**[reset qos queue-statistics interface]{lang="EN-US"}**]{#struct_0_14687_18620_x616069127}[ \[ ]{lang="EN-US" style="font-size:
10.0pt;font-family:宋体;color:black"}*[interface-type interface-number]{lang="EN-US"}*[ \] ]{lang="EN-US" style="font-size:10.0pt;font-family:
宋体;color:black"}**[outbound]{lang="EN-US"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_1112670711}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1532885790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_2112814228}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x777401846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x338784793}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_374018131}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14687_18620_546730287}[：]{style="font-family:宋体"}[指定接口类型和接口编号。如果未指定本参数，将清除所有接口的队列出方向统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1696519128}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_x1019353654}[清除所有接口的队列统计计数]{style="font-family:宋体"}

[[\<Sysname\> reset qos queue-statistics interface outbound]{lang="EN-US"}]{#struct_0_14687_18620_x239615995}

[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_2065760061}[清除接口]{style="font-family:宋体"}[Ten-GigabitEthernet 9/0/1]{lang="EN-US"}[的队列统计计数]{style="font-family:宋体"}

[[\<Sysname\> reset qos queue-statistics interface Ten-GigabitEthernet 9/0/1 outbound]{lang="EN-US"}]{#struct_0_14687_18620_x85899470}
:::

::::: {#-1926989024 .myid}
[]{#_Toc404792490}[]{#struct_0_14687_18620_1639052952}[]{#_Toc356995908}[]{#_Toc356995718}

**QPPB \-- QPPB配置命令 \-- bgp-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](QoS命令.files/image002.png){#图片 3 border="0" width="63" height="25"}]{lang="EN-US"}]{#struct_0_14687_18620_x1701577131}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_14687_18620_x1090420222}
:::

[ ]{lang="EN-US"}

[**[bgp-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1090354686}[命令用来配置]{style="font-family:宋体"}[QPPB]{lang="EN-US"}[功能，即通过]{style="font-family:宋体"}[BGP]{lang="EN-US"}[传播路由策略中设置的]{style="font-family:宋体"}**[apply ip-precedence]{lang="EN-US"}**[和]{style="font-family:宋体"}**[apply qos-local-id]{lang="EN-US"}**[信息。]{style="font-family:宋体"}

[**[undo bgp-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1090551294}[命令用来取消配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1090485758}

[**[bgp-policy]{lang="EN-US"}**[ { **destination** \| **source** } { **ip-prec-map** \| **ip-qos-map** } \*]{lang="EN-US"}]{#struct_0_14687_18620_x2101200724}

[**[undo bgp-policy]{lang="EN-US"}**[ { **destination** \| **source** } \[ **ip-prec-map** \| **ip-qos-map** \] \*]{lang="EN-US"}]{#struct_0_14687_18620_x1090158078}

[**[bgp-policy]{lang="EN-US"}**[ { **destination** \| **source** } **ip-prec-map ip-qos-map**]{lang="EN-US"}]{#struct_0_14687_18620_x1090092542}

[**[undo bgp-policy]{lang="EN-US"}**[ { **destination** \| **source** } \[ **ip-prec-map ip-qos-map** \]]{lang="EN-US"}]{#struct_0_14687_18620_x1090289150}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14687_18620_956292486}

[[没有配置]{style="font-family:宋体"}[QPPB]{lang="EN-US"}]{#struct_0_14687_18620_x1090223614}[功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1089895934}

[[接口视图]{style="font-family:宋体"}]{#struct_0_14687_18620_x1089830398}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14687_18620_1951818388}

[[network-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1090420223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14687_18620_x1090354687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1090551295}

[**[destination]{lang="EN-US"}**]{#struct_0_14687_18620_1746613087}[：使用目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[查找路由。]{style="font-family:宋体"}

[**[source]{lang="EN-US" style="font-size:11.0pt;color:black"}**]{#struct_0_14687_18620_x1090485759}[：使用源]{style="font-family:宋体"}[IP]{lang="EN-US"}[查找路由。如果指定本参数，则以源]{style="font-family:宋体"}[IP]{lang="EN-US"}[为目的进行反向查找。]{style="font-family:宋体"}

[**[ip-prec-map]{lang="EN-US"}**]{#struct_0_14687_18620_x1090158079}[：设置]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[ip-qos-map]{lang="EN-US"}**]{#struct_0_14687_18620_x1090092543}[：设置]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14687_18620_1601673122}

[[本配置只在接口入方向生效。]{style="font-family:宋体"}]{#struct_0_14687_18620_x1090289151}

[[MPLS L3VPN]{lang="EN-US"}]{#struct_0_14687_18620_x1090223615}[网络中，]{style="font-family:宋体"}[PE]{lang="EN-US"}[公网接口入方向]{style="font-family:宋体"}[QoS]{lang="EN-US"}[业务在本配置之前进行；其他网络环境中]{style="font-family:宋体"}[QoS]{lang="EN-US"}[业务在本配置之后进行。]{style="font-family:宋体"}

[[如果存在两条]{style="font-family:宋体"}**[bgp-policy]{lang="EN-US"}**]{#struct_0_14687_18620_x1089895935}[命令，分别指定]{style="font-family:宋体"}[source]{lang="EN-US"}[和]{style="font-family:宋体"}[destination]{lang="EN-US"}[，后者的设置操作会覆盖前者。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1089830399}

[]{#_Toc130529683}[]{#_Toc69790677}[[\# ]{lang="EN-US"}]{#struct_0_14687_18620_385734447}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[查找路由获得]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14687_18620_x1090420224}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bgp-policy source ip-prec-map ip-qos-map]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14687_18620_x1090354688}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply ip-precedence]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14687_18620_x1090551296}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply qos-local-id]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_14687_18620_x1090485760}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[route-policy ]{lang="EN-US"}**]{#struct_0_14687_18620_x1745166972}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略）]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}
:::::
