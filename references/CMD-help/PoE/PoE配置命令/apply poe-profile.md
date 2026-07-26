::: {#-1381293230 .myid}
[]{#_Toc404796816}[]{#struct_0_x6755_56834_1158667139}[]{#_Toc257634895}

**PoE \-- PoE配置命令 \-- apply poe-profile**

------------------------------------------------------------------------

[**[apply poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_1797059727}[命令用来将]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[应用到当前]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo apply poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_1972911931}[命令用来取消]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[在当前]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1452622012}

[**[apply poe-profile]{lang="EN-US"}**[ { **index** *index* \| **name** *profile-name* }]{lang="EN-US"}]{#struct_0_x6755_56834_x1631516360}

[**[undo apply poe-profile]{lang="EN-US"}**[ { **index** *index* \| **name** *profile-name* }]{lang="EN-US"}]{#struct_0_x6755_56834_213645548}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1060946447}

[[没有将]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}]{#struct_0_x6755_56834_1322192459}[应用到当前]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1364079087}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1598157383}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_316525856}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2068162094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1158557735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_639497264}

[**[index]{lang="EN-US"}***[ index]{lang="EN-US"}*]{#struct_0_x6755_56834_x1580641635}[：]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[的索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x6755_56834_x1921301001}[：]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_909613550}

[[\# ]{lang="FR"}]{#struct_0_x6755_56834_x1364144623}[将名为]{style="font-family:宋体"}[forIPphone]{lang="FR"}[的]{style="font-family:宋体"}[PoE profile]{lang="FR"}[应用到]{style="font-family:宋体"}[PoE]{lang="FR"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_899383092}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="FR"}

[\[Sysname-GigabitEthernet1/]{lang="EN-US"}[0/]{lang="FR"}[1\] apply poe-profile name forIPphone]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_787510076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply poe-profile interface]{lang="EN-US"}**]{#struct_0_x6755_56834_538057568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_1267772882}[]{#_Toc257634896}
:::

::: {#-723420404 .myid}
[]{#_Toc404796817}[]{#struct_0_x6755_56834_x1556857703}

**PoE \-- PoE配置命令 \-- apply poe-profile interface**

------------------------------------------------------------------------

[**[apply poe-profile interface]{lang="EN-US"}**]{#struct_0_x6755_56834_1711457206}[命令用来将]{style="font-family:
宋体"}[PoE profile]{lang="EN-US"}[应用到一个或多个]{style="font-family:
宋体"}[PoE]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo apply poe-profile interface]{lang="EN-US"}**]{#struct_0_x6755_56834_x292521669}[命令用来取消]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[在]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1363948015}

[**[apply poe-profile ]{lang="EN-US"}**[{ **index** *index* *\|* **name** *profile-name* } **interface** *interface-range*]{lang="EN-US"}]{#struct_0_x6755_56834_x999832789}

[**[undo apply poe-profile ]{lang="EN-US"}**[{ **index** *index* *\|* **name** *profile-name* } **interface** *interface-range*]{lang="EN-US"}]{#struct_0_x6755_56834_1906851195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1311283076}

[[PoE profile]{lang="EN-US"}]{#struct_0_x6755_56834_1576380311}[没有应用到任何接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1377880792}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1753346609}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1376735705}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x861236617}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1364013551}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x828785182}

[**[index]{lang="EN-US"}***[ index]{lang="EN-US"}*]{#struct_0_x6755_56834_x466771022}[：]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[的索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x6755_56834_1856476676}[：]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符，区分大小写。]{style="font-family:宋体"}

[*[interface-range]{lang="FR"}*]{#struct_0_x6755_56834_x853645080}[：]{style="font-family:宋体"}[以太网接口范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[表示多个以太网接口。表示方式为]{style="font-family:宋体"}*[interface-range]{lang="FR"}*[＝]{style="font-family:宋体"} *[interface-type interface-number]{lang="FR"}*[ \[ **to** *interface-type interface-number* \]]{lang="FR"}[。其中，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为接口类型和接口编号。起始接口号要小于结束接口号，结束接口要和起始接口是同种类型。接口范围可以任意，如果指定范围内存在不支持]{style="font-family:宋体"}[PoE]{lang="EN-US"}[的接口，]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件应用时将忽略这类接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_975023052}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1120223960}[将名称为]{style="font-family:宋体"}[forIPphone]{lang="EN-US"}[的]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[应用到]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x627207691}

[\[Sysname\] apply poe-profile name forIPphone interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_750357523}[将索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[应用到]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[至]{style="font-family:宋体"}[GigabitEthernet1/0/8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x1363816943}

[\[Sysname\] apply poe-profile index 1 interface gigabitethernet 1/0/2 to gigabitethernet 1/0/8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x85023043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_x74386972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe-profile interface]{lang="EN-US"}**]{#struct_0_x6755_56834_416361286}
:::

::: {#-1156149894 .myid}
[]{#_Toc404796818}[]{#struct_0_x6755_56834_x922277693}[]{#_Toc257634897}

**PoE \-- PoE配置命令 \-- display poe device**

------------------------------------------------------------------------

[**[display poe device]{lang="EN-US"}**]{#struct_0_x6755_56834_909020178}[命令用来显示]{style="font-family:宋体"}[PSE]{lang="EN-US"}[（]{style="font-family:宋体"}[Power Sourcing Equipment]{lang="EN-US"}[，供电设备）的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1772356068}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6755_56834_x2116044582}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display poe device]{lang="EN-US"}**]{#struct_0_x6755_56834_x1278676787}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_x1363882479}[模式：]{style="font-family:宋体"}

[**[display poe device ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x1364437929}

[[集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_356151959}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **poe** **device** \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x1839654040}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2012010236}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x991162104}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_876887148}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1316938479}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1974949671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_257536616}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1895424898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1363685871}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x6755_56834_x2109100157}[：显示指定成员设备上所有]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6755_56834_356807319}[：显示指定成员设备上所有]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x994090867}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1670699713}[显示]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。（显示信息与设备的型号相关，请以设备的实际情况为准）（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display poe device]{lang="EN-US"}]{#struct_0_x6755_56834_x1954176537}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 1        0          0          48        0              Off     LSP1POEA]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1908467572}[显示]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。（显示信息与设备的型号相关，请以设备的实际情况为准）（多]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display poe device]{lang="EN-US"}]{#struct_0_x6755_56834_x1363751407}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 7        2         0           24        370            Off     LSP2LTSUC]{lang="EN-US"}

[ 10       3         0           24        370            Off     LSP2LTSUC ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1170164640}[显示所有]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。（显示信息与设备的型号相关）（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe device]{lang="EN-US"}]{#struct_0_x6755_56834_x776000807}

[Chassis 1]{lang="EN-US"}[：]{style="font-family:宋体"}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 4        1         0           1         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[ 7        1         4           8         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[Chassis 2]{lang="EN-US"}[：]{style="font-family:宋体"}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 43       10        4           8         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_356741783}[显示所有]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息。（显示信息与设备的型号相关）（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe device]{lang="EN-US"}]{#struct_0_x6755_56834_356283028}

[Slot 1]{lang="EN-US"}[：]{style="font-family:
宋体"}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 4        1         0           1         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[ 7        1         4           8         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[Slot 2]{lang="EN-US"}[：]{style="font-family:
宋体"}

[ PSE ID  Slot No. SSlot No. PortNum  MaxPower(W)  State  Model]{lang="EN-US"}

[ 43       10        4           8         200            Off    LSBMPOEGV48TP]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display poe device]{lang="EN-US"}]{#struct_0_x6755_56834_x1452539494}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_558602801}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_x592502491}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_1157840086}

[[Chassis 1]{lang="EN-US"}]{#struct_0_x6755_56834_x1364210162}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_x1989332359}[上]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot 1]{lang="EN-US"}]{#struct_0_x6755_56834_356217492}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_1522670996}[上]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的相关信息（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[PSE ID]{lang="EN-US"}]{#struct_0_x6755_56834_416534038}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_2044214962}[编号]{style="font-family:宋体"}

[[Slot No.]{lang="EN-US"}]{#struct_0_x6755_56834_x2092735327}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x283883496}[所在槽位号]{style="font-family:宋体"}

[[SSlot No.]{lang="EN-US"}]{#struct_0_x6755_56834_936693978}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1364275698}[所在子槽位号]{style="font-family:宋体"}

[[PortNum]{lang="EN-US"}]{#struct_0_x6755_56834_1111612972}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_590683046}[上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的数量]{style="font-family:宋体"}

[[MaxPower(W)]{lang="EN-US"}]{#struct_0_x6755_56834_1313542524}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1270604982}[最大供电功率（单位为：瓦）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x6755_56834_x1364079090}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1937229490}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x6755_56834_x89713153}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[正在供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x6755_56834_x435703546}[：]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[停止供电]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Faulty]{lang="EN-US"}]{#struct_0_x6755_56834_x1630185651}[：]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[故障]{lang="EN-US" style="font-family:宋体"}

[[Model]{lang="EN-US"}]{#struct_0_x6755_56834_75437404}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1364144626}[型号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1403062156 .myid}
[]{#_Toc404796819}[]{#struct_0_x6755_56834_1302667619}[]{#_Toc257634898}

**PoE \-- PoE配置命令 \-- display poe interface**

------------------------------------------------------------------------

[**[display poe interface]{lang="EN-US"}**]{#struct_0_x6755_56834_x1411939976}[命令用来显示设备指定]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1633981916}

[**[display poe interface]{lang="EN-US"}**[ \[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x1225875625}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1377407456}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1628117440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1363948018}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_115912458}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1036735102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1442787917}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x2143355821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x708808469}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6755_56834_x189884741}[：指定接口类型及接口编号，显示指定]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。如果未指定本参数，则显示所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x723183658}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1364013554}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的供电状态。]{style="font-family:宋体"}

[[\<Sysname\> display poe interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x6755_56834_x1232069709}

[ PoE Status                         : Enabled]{lang="EN-US"}

[ Power Priority                    : Critical]{lang="EN-US"}

[ Oper                                : On]{lang="EN-US"}

[ IEEE Class                         : 1]{lang="EN-US"}

[ Detection Status                  : Delivering power]{lang="EN-US"}

[ Power Mode                         : Signal]{lang="EN-US"}

[ Current Power                      : 11592    mW]{lang="EN-US"}

[ Average Power                      : 11610    mW]{lang="EN-US"}

[ Peak Power                          : 11684    mW]{lang="EN-US"}

[ Max Power                           : 15400    mW]{lang="EN-US"}

[ Electric Current                   : 244      mA]{lang="EN-US"}

[ Voltage                              : 51.7     V]{lang="EN-US"}

[ PD Description                      : IP Phone For Room 101]{lang="EN-US"}

[]{#struct_0_x6755_56834_x1643852569}[[表1-2 ]{lang="EN-US"}[display poe interface]{lang="EN-US"}]{#_Ref138143377}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_555444913}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_1987092243}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1363816946}

[[PoE status]{lang="EN-US"}]{#struct_0_x6755_56834_x488307570}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_434785}[接口远程供电功能是否开启：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6755_56834_1851055056}[：开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1363882482}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[Power Priority]{lang="EN-US"}]{#struct_0_x6755_56834_x2123625136}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x469389918}[接口供电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x6755_56834_2046750887}[：最高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x6755_56834_x1846331602}[：高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Low]{lang="EN-US"}]{#struct_0_x6755_56834_x1363685874}[：低]{lang="EN-US" style="font-family:宋体"}

[[Oper]{lang="EN-US"}]{#struct_0_x6755_56834_x1349585270}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1927721023}[接口工作状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x6755_56834_x1363751410}[：供电功能处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On]{lang="EN-US"}]{#struct_0_x6755_56834_1558653179}[：正在正常供电]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power-lack]{lang="EN-US"}]{#struct_0_x6755_56834_x451295496}[：]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[剩余保证功率不够，导致无法对优先级为]{lang="EN-US" style="font-family:宋体"}[Critical]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power-deny]{lang="EN-US"}]{#struct_0_x6755_56834_x850744617}[：拒绝供电，]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}[要求功率大于配置功率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power-itself]{lang="EN-US"}]{#struct_0_x6755_56834_1504649281}[：外接设备正在自己供电]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Power-limit]{lang="EN-US"}]{#struct_0_x6755_56834_x1364210161}[：正在受限供电，]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}[要求功率大于配置功率，]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[仍按配置功率供电]{lang="EN-US" style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x423248418}[接口工作状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[IEEE Class]{lang="EN-US"}]{#struct_0_x6755_56834_1067558285}

[[由]{style="font-family:宋体"}[IEEE]{lang="EN-US"}]{#struct_0_x6755_56834_x553996711}[规定的]{style="font-family:宋体"}[PD]{lang="EN-US"}[功率等级，取值为：]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[-]{lang="EN-US"}

[[其中，"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x6755_56834_x420989110}["表示不支持，该值的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Detection Status]{lang="EN-US"}]{#struct_0_x6755_56834_x1364275697}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x4132275}[接口检测状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1364079089}[：]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电]{lang="EN-US" style="font-family:宋体"}[功能处于]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Searching]{lang="EN-US"}]{#struct_0_x6755_56834_1147818689}[：正在搜索]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delivering power]{lang="EN-US"}]{#struct_0_x6755_56834_x530258002}[：正在向]{lang="EN-US" style="font-family:
  宋体"}[PD]{lang="EN-US"}[供电]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x6755_56834_339576520}[：错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Test]{lang="EN-US"}]{#struct_0_x6755_56834_x1364144625}[：测试状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other fault]{lang="EN-US"}]{#struct_0_x6755_56834_1705952146}[：其他错误状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD disconnected]{lang="EN-US"}]{#struct_0_x6755_56834_916339088}[：]{style="font-family:宋体"}[PD]{lang="EN-US"}[未连接]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x2102365697}[接口检测状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[Power Mode]{lang="EN-US"}]{#struct_0_x6755_56834_x1363948017}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_162966625}[接口供电方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Signal]{lang="EN-US"}]{#struct_0_x6755_56834_158812772}[：信号线供电方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spare]{lang="EN-US"}]{#struct_0_x6755_56834_x590490331}[：空闲线供电方式]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1364013553}[接口供电方式不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[Current Power]{lang="EN-US"}]{#struct_0_x6755_56834_334014232}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x663596543}[接口当前功率]{style="font-family:宋体"}

[[包括]{style="font-family:宋体"}[PD]{lang="EN-US"}]{#struct_0_x6755_56834_1128258762}[消耗功率和传输损耗。一般损耗不超过]{style="font-family:宋体"}[1W]{lang="EN-US"}[，损耗的具体情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Average Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1363816945}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1077776371}[接口平均功率]{style="font-family:宋体"}

[[Peak Power]{lang="EN-US"}]{#struct_0_x6755_56834_x2043613105}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x873763043}[接口峰值功率]{style="font-family:宋体"}

[[Max Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1363882481}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1720340609}[接口最大功率]{style="font-family:宋体"}

[[Electric Current]{lang="EN-US"}]{#struct_0_x6755_56834_264750569}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x697837153}[接口当前电流]{style="font-family:宋体"}

[[Voltage]{lang="EN-US"}]{#struct_0_x6755_56834_x1363685873}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x946300743}[接口当前电压]{style="font-family:宋体"}

[[PD Description]{lang="EN-US"}]{#struct_0_x6755_56834_x830467855}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1363751409}[接口所连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[的描述信息，用于辅助用户识别]{style="font-family:宋体"}[PD]{lang="EN-US"}[的类型和位置等]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_348865134}[显示设备所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。]{style="font-family:宋体"}

[[\<Sysname\> display poe interface]{lang="EN-US"}]{#struct_0_x6755_56834_x772348975}

[ Interface    PoE       Priority  CurPower  Oper      IEEE  Detection]{lang="EN-US"}

[                                      (W)                   Class Status]{lang="EN-US"}

[ GE1/0/1      Enabled   Low        4.4       On         1      Delivering Power]{lang="EN-US"}

[ GE1/0/2      Enabled   Critical  0.0       On         -      Disabled]{lang="EN-US"}

[ GE1/0/3      Enabled   Low        0.0       On         -      Disabled]{lang="EN-US"}

[ GE1/0/4      Enabled   Critical  0.0       On         -      Searching]{lang="EN-US"}

[ GE1/0/5      Enabled   Low        4.0       On         2      Delivering Power]{lang="EN-US"}

[ GE1/0/6      Enabled   Low        0.0       On         -      Disabled]{lang="EN-US"}

[ GE1/0/7      Disabled  Low        0.0       Off        -      Fault]{lang="EN-US"}

[   \-\--  On State Ports: 2; Used: 8.4(W); Remaining: 171.6(W)  \-\--]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display poe interface]{lang="EN-US"}]{#struct_0_x6755_56834_x13935266}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_576641009}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1076638866}

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1364210164}

[[Interface]{lang="EN-US"}]{#struct_0_x6755_56834_x826532945}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1849496973}[接口名称简称]{style="font-family:宋体"}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x2089989519}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1364275700}[接口远程供电功能是否开启：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6755_56834_755841363}[：]{lang="EN-US" style="font-family:宋体"}[开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1364079092}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x6755_56834_1194938392}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_941470391}[接口供电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x6755_56834_x1364144628}[：]{lang="EN-US" style="font-family:宋体"}[最高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x6755_56834_x1473269903}[：]{lang="EN-US" style="font-family:宋体"}[高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x6755_56834_1247960625}ow[：]{lang="EN-US" style="font-family:宋体"}[低]{lang="EN-US" style="font-family:宋体"}

[[CurPower]{lang="EN-US"}]{#struct_0_x6755_56834_x817151315}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1684430208}[接口当前功率]{style="font-family:宋体"}

[[Oper]{lang="EN-US"}]{#struct_0_x6755_56834_1735554797}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1363948020}[接口工作状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x6755_56834_x1364013556}ff[：]{style="font-family:宋体"}[供电功能处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x6755_56834_x69270295}n[：]{style="font-family:宋体"}[正在正常供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_x1499316972}ower-lack[：]{style="font-family:
  宋体"}[剩余保证功率不够，导致无法给]{style="font-family:宋体"}Critical[接口供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_x918158862}ower-deny[：]{style="font-family:
  宋体"}[拒绝供电，]{style="font-family:宋体"}PD[要求功率大于配置功率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[Power-itself]{lang="EN-US"}]{#struct_0_x6755_56834_x1363816948}[：]{style="font-family:
  宋体"}[外接设备正在自己供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_x37968876}ower-limit[：]{style="font-family:宋体"}[正在受限供电，]{style="font-family:宋体"}PD[要求功率大于配置功率，]{style="font-family:宋体"}PSE[仍按配置功率供电]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1353228821}[接口工作状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[IEEE Class]{lang="EN-US"}]{#struct_0_x6755_56834_362595713}

[[由]{style="font-family:宋体"}[IEEE]{lang="EN-US"}]{#struct_0_x6755_56834_x701319752}[规定的]{style="font-family:宋体"}[PD]{lang="EN-US"}[功率等级，取值为：]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[-]{lang="EN-US"}

[[其中，"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x6755_56834_x1363882484}["表示不支持，该值的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Detection Status]{lang="EN-US"}]{#struct_0_x6755_56834_x960825722}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_848849105}[接口检测状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1363685876}[：]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电]{lang="EN-US" style="font-family:宋体"}[处于]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Searching]{lang="EN-US"}]{#struct_0_x6755_56834_x186785856}[：正在搜索]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delivering Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1363751412}[：正在向]{lang="EN-US" style="font-family:
  宋体"}[PD]{lang="EN-US"}[供电]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x6755_56834_x1573514703}[：错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Test]{lang="EN-US"}]{#struct_0_x6755_56834_x1694047483}[：测试状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other Fault]{lang="EN-US"}]{#struct_0_x6755_56834_1078103252}[：其他错误状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD Disconnected]{lang="EN-US"}]{#struct_0_x6755_56834_x1364210163}[：]{style="font-family:宋体"}[PD]{lang="EN-US"}[未连接]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_739550996}[接口检测状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[On State Ports]{lang="EN-US"}]{#struct_0_x6755_56834_1618486551}

[[正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_149876179}[接口数量]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_x6755_56834_x1364275699}

[[当前供电]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x454470969}[接口消耗的功率]{style="font-family:宋体"}

[[Remaining]{lang="EN-US"}]{#struct_0_x6755_56834_1255076495}

[[系统总剩余功率]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1359058586}

[ ]{lang="EN-US"}

::: {#-1801470333 .myid}
[]{#_Toc404796820}[]{#struct_0_x6755_56834_1466712196}[]{#_Toc257634899}

**PoE \-- PoE配置命令 \-- display poe interface power**

------------------------------------------------------------------------

[**[display poe interface power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1364079091}[命令用来显示]{style="font-family:
宋体"}[PoE]{lang="EN-US"}[接口的功率信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_791653865}

[**[display poe interface power ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x938897447}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1821541698}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1503811615}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_683098325}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x956338981}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1840277752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1155636389}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1364144627}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1426215736}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6755_56834_x1605053389}[：指定接口类型及接口编号，显示指定]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的功率信息。如果未指定本参数，则显示所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的功率信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1376231247}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1995063118}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的功率信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe interface power gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x6755_56834_x15317210}

[Interface    Current   Peak      Max       PD Description]{lang="EN-US"}

[               (W)       (W)       (W)]{lang="EN-US"}

[ GE1/1        15.0      15.3      15.4      Access Point on Room 509 for Peter]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1819740368}[显示所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的功率信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe interface power]{lang="EN-US"}]{#struct_0_x6755_56834_x1363948019}

[Interface    Current   Peak      Max       PD Description]{lang="EN-US"}

[               (W)       (W)       (W)]{lang="EN-US"}

[ GE1/0/25    4.4        4.5       4.6         IP Phone in Room 309 for Peter Smith]{lang="EN-US"}

[ GE1/0/26    4.4        4.5       15.4        IP Phone in Room 409 for Peter Pan]{lang="EN-US"}

[ GE1/0/27    15.0      15.3       15.4        Access Point in Room 509 for Peter]{lang="EN-US"}

[ GE1/0/28    0.0        0.0        0.0        IP Phone in Room 609 for Peter John]{lang="EN-US"}

[ GE1/0/29    0.0        0.0        0.0        IP Phone in Room 709 for Jack]{lang="EN-US"}

[ GE1/0/30    0.0        0.0        0.0        IP Phone in Room 809 for Alien]{lang="EN-US"}

[\-\-- On State Ports: 3; Used: 23.8(W);  Remaining: 776.2(W) \-\--]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display poe interface power]{lang="EN-US"}]{#struct_0_x6755_56834_1681996399}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_599257041}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_1553358727}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_x847066615}

[[Interface]{lang="EN-US"}]{#struct_0_x6755_56834_x1364013555}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1496813646}[接口简称]{style="font-family:宋体"}

[[CurPower]{lang="EN-US"}]{#struct_0_x6755_56834_1084291544}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x232985517}[接口当前功率]{style="font-family:宋体"}

[[PeakPower]{lang="EN-US"}]{#struct_0_x6755_56834_1398709234}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_894451420}[接口峰值功率]{style="font-family:宋体"}

[[MaxPower]{lang="EN-US"}]{#struct_0_x6755_56834_1299155630}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1363816947}[接口最大功率]{style="font-family:宋体"}

[[PD Description]{lang="EN-US"}]{#struct_0_x6755_56834_x2054391511}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1997737257}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[描述信息，用于辅助用户识别]{style="font-family:宋体"}[PD]{lang="EN-US"}[的类型和位置等]{style="font-family:宋体"}

[[Ports On]{lang="EN-US"}]{#struct_0_x6755_56834_x1051210516}

[[正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x2126346815}[接口数量]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_x6755_56834_x1363882483}

[[所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x557541195}[接口当前消耗功率]{style="font-family:宋体"}

[[Remaining]{lang="EN-US"}]{#struct_0_x6755_56834_522354133}

[[系统总剩余功率]{style="font-family:宋体"}]{#struct_0_x6755_56834_77371355}

[ ]{lang="EN-US"}

::::: {#-1264113148 .myid}
[]{#OLE_LINK14}[]{#OLE_LINK13}[]{#_Toc404796821}[]{#struct_0_x6755_56834_2073673106}[]{#_Toc257634900}

**PoE \-- PoE配置命令 \-- display poe power-usage**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_1338154339}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x1363685875}
:::

**[ ]{lang="EN-US"}**

[**[display poe power-usage]{lang="EN-US"}**]{#struct_0_x6755_56834_216498671}[命令用来显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_827326883}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6755_56834_x1356005404}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display poe power-usage]{lang="EN-US"}**]{#struct_0_x6755_56834_x1072453123}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_1835991905}[模式：]{style="font-family:宋体"}

[**[display poe power-usage ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_12754777}

[[集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_356086426}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **poe** **power-usage** \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_65412167}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_392129613}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1053704679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x698199477}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1363751411}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x7430762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x56330517}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1876781058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1501773808}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x6755_56834_x1731045430}[：显示指定成员设备上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6755_56834_356741786}[：显示指定成员设备上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1177332949}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1639980636}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。]{style="font-family:宋体"}

[[\<Sysname\> dis poe power-usage]{lang="EN-US"}]{#struct_0_x6755_56834_201873781}

[ PoE Current Power                    : 12    W]{lang="EN-US"}

[ PoE Max Power                         : 2000  W]{lang="EN-US"}

[ PoE Max Guaranteed Power            : 2000  W]{lang="EN-US"}

[ PoE Remaining Allocable Power      : 1800  W]{lang="EN-US"}

[ PoE Remaining Guaranteed Power     : 2000  W]{lang="EN-US"}

[ Powered PoE Ports                     : 1]{lang="EN-US"}

[ Statistics by PSE:]{lang="EN-US"}

[ PSE ID  Max     Current  Peak     Average  Remaining      Powered]{lang="EN-US"}

[         (W)     (W)       (W)      (W)        Guaranteed(W) Ports]{lang="EN-US"}

[ 5       200     12        12        6          200             1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2117889311}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe power-usage]{lang="EN-US"}]{#struct_0_x6755_56834_201808245}

[Chassis 1 :]{lang="EN-US"}

[ PoE Current Power                   : 600   W]{lang="EN-US"}

[ PoE Max Power                        : 2000  W]{lang="EN-US"}

[ PoE Max Guaranteed Power           : 1000  W]{lang="EN-US"}

[ PoE Remaining Allocable Power      : 800   W]{lang="EN-US"}

[ PoE Remaining Guaranteed Power    : 600   W]{lang="EN-US"}

[ Powered PoE Ports                    : 60]{lang="EN-US"}

[ Statistics by PSE:]{lang="EN-US"}

[ PSE ID   Max    Current    Peak    Average    Remaining          Powered]{lang="EN-US"}

[          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports]{lang="EN-US"}

[ 4        300     200         230     205         100                 20]{lang="EN-US"}

[ 7        400     300         345     290         200                 30]{lang="EN-US"}

[ 10       500     100         120     110         300                 10]{lang="EN-US"}

[Chassis 2 :]{lang="EN-US"}

[ PoE Current Power                   : 600   W]{lang="EN-US"}

[ PoE Max Power                        : 2000  W]{lang="EN-US"}

[ PoE Max Guaranteed Power           : 1000  W]{lang="EN-US"}

[ PoE Remaining Allocable Power    : 800   W]{lang="EN-US"}

[ PoE Remaining Guaranteed Power    : 600   W]{lang="EN-US"}

[ Powered PoE Ports                   : 60]{lang="EN-US"}

[ Statistics by PSE:]{lang="EN-US"}

[ PSE ID   Max    Current    Peak    Average    Remaining          Powered]{lang="EN-US"}

[          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports]{lang="EN-US"}

[ 35       300     200         230     205         100                 20]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_356414107}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe power-usage]{lang="EN-US"}]{#struct_0_x6755_56834_356348571}

[Slot 1 :]{lang="EN-US"}

[ PoE Current Power                    : 600   W]{lang="EN-US"}

[ PoE Max Power                         : 2000  W]{lang="EN-US"}

[ PoE Max Guaranteed Power            : 1000  W]{lang="EN-US"}

[ PoE Remaining Allocable Power      : 800   W]{lang="EN-US"}

[ PoE Remaining Guaranteed Power     : 600   W]{lang="EN-US"}

[ Powered PoE Ports                     : 60]{lang="EN-US"}

[ Statistics by PSE:]{lang="EN-US"}

[ PSE ID   Max    Current    Peak    Average    Remaining          Powered]{lang="EN-US"}

[          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports]{lang="EN-US"}

[ 4        300     200         230     205         100                 20]{lang="EN-US"}

[ 7        400     300         345     290         200                 30]{lang="EN-US"}

[ 10       500     100         120     110         300                 10]{lang="EN-US"}

[Slot 2 :]{lang="EN-US"}

[ PoE Current Power                     : 600   W]{lang="EN-US"}

[ PoE Max Power                          : 2000  W]{lang="EN-US"}

[ PoE Max Guaranteed Power             : 1000  W]{lang="EN-US"}

[ PoE Remaining Allocable Power       : 800   W]{lang="EN-US"}

[ PoE Remaining Guaranteed Power      : 600   W]{lang="EN-US"}

[ Powered PoE Ports                     : 60]{lang="EN-US"}

[ Statistics by PSE:]{lang="EN-US"}

[ PSE ID   Max    Current    Peak    Average    Remaining          Powered]{lang="EN-US"}

[          (W)     (W)         (W)     (W)         Guaranteed(W)     Ports]{lang="EN-US"}

[ 35       300     200         230     205         100                 20]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display poe power-usage]{lang="EN-US"}]{#struct_0_x6755_56834_212012915}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_591900753}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_92422252}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_202004853}

[[Chassis 1]{lang="EN-US"}]{#struct_0_x6755_56834_1090636858}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_x1355660900}[上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot 1]{lang="EN-US"}]{#struct_0_x6755_56834_356020891}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_355955355}[上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的功率和各]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率信息（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[PoE Current Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1718740365}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_2080699624}[当前消耗功率总和]{style="font-family:宋体"}

[[PoE Max Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1080149260}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_201939317}[最大功率]{style="font-family:宋体"}

[[PoE Max Guaranteed Power]{lang="EN-US"}]{#struct_0_x6755_56834_990288429}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1558571811}[最大保证功率，即电源提供给优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的最大功率]{style="font-family:宋体"}

[[PoE Remaining Allocable Power]{lang="EN-US"}]{#struct_0_x6755_56834_x332817089}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_202135925}[剩余可分配功率]{style="font-family:宋体"}[=PoE]{lang="EN-US"}[最大功率]{style="font-family:宋体"}[--]{lang="EN-US"}[已经开启的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的最大功率之和]{style="font-family:宋体"}

[[PoE Remaining Guaranteed Power]{lang="EN-US"}]{#struct_0_x6755_56834_202070389}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1531413768}[剩余保证功率]{style="font-family:宋体"}[=]{lang="EN-US"}[PoE]{lang="EN-US"}[最大保证功率－]{style="font-family:宋体"}[设备]{style="font-family:宋体"}[中优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[最大]{style="font-family:宋体"}[功率之和（通常]{style="font-family:宋体"}[PoE]{lang="EN-US"}[最大保证功率＝]{style="font-family:宋体"}[PoE]{lang="EN-US"}[最大功率]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[Powered PoE Ports]{lang="EN-US"}]{#struct_0_x6755_56834_767002927}

[[当前设备正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_312017424}[接口总数]{style="font-family:宋体"}

[[PSE ID]{lang="EN-US"}]{#struct_0_x6755_56834_539842775}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x315245365}[编号]{style="font-family:宋体"}

[[Max]{lang="EN-US"}]{#struct_0_x6755_56834_202266997}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x976666345}[最大功率]{style="font-family:宋体"}

[[Current]{lang="EN-US"}]{#struct_0_x6755_56834_x1384006041}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1508059775}[当前功率]{style="font-family:宋体"}

[[Peak]{lang="EN-US"}]{#struct_0_x6755_56834_202201461}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1026053364}[峰值功率]{style="font-family:宋体"}

[[Average]{lang="EN-US"}]{#struct_0_x6755_56834_x2012114505}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x860983594}[平均功率]{style="font-family:宋体"}

[[Remaining Guaranteed ]{lang="EN-US"}]{#struct_0_x6755_56834_291274627}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_202398069}[剩余保证功率]{style="font-family:宋体"}[=]{lang="EN-US"}[PSE]{lang="EN-US"}[最大保证功率－该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[中优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口最大功率之和（通常]{style="font-family:宋体"}[PSE]{lang="EN-US"}[最大保证功率＝]{style="font-family:宋体"}[PSE]{lang="EN-US"}[最大功率]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[]{#struct_0_x6755_56834_585901581}[]{#OLE_LINK8}[[Powered Ports]{lang="EN-US"}]{#OLE_LINK7}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x645083899}[正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#37659263 .myid}
[]{#_Toc404796822}[]{#struct_0_x6755_56834_x206201913}[]{#_Toc257634901}

**PoE \-- PoE配置命令 \-- display poe pse**

------------------------------------------------------------------------

[**[display poe pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x641571494}[命令用来显示]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1220576720}

[[单]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_202332533}[设备：]{style="font-family:宋体"}

[**[display poe pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x2101163796}

[[多]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1190366658}[设备：]{style="font-family:宋体"}

[**[display poe pse ]{lang="EN-US"}**[\[ *pse-id* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x1567813274}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1976292725}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_737726032}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1573446847}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1255008435}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1803171350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_201873782}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_2117889314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1320363994}

[*[pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x769682995}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号。如果不指定该参数，则显示设备上所有在位的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_525601476}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2013544863}[显示设备的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的信息。（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display poe pse]{lang="EN-US"}]{#struct_0_x6755_56834_201808246}

[ PSE ID                                    : 1]{lang="EN-US"}

[ Slot NO.                                  : 0]{lang="EN-US"}

[ PSE Model                                 : LSBMPOEGV48TP]{lang="EN-US"}

[ PSE Status                                : Enabled]{lang="EN-US"}

[ PSE Preempted                             : No]{lang="EN-US"}

[ Power Priority                            : Low]{lang="EN-US"}

[ Current Power                             : 130      W]{lang="EN-US"}

[ Average Power                             : 20       W]{lang="EN-US"}

[ Peak Power                                : 240      W]{lang="EN-US"}

[ Max Power                                 : 200      W]{lang="EN-US"}

[ Remaining Guaranteed Power             : 120      W]{lang="EN-US"}

[ PSE CPLD Version                         : 100]{lang="EN-US"}

[ ]{lang="EN-US"}[PSE Software Version                    : 200]{lang="DE"}

[ PSE Hardware Version                    : 100]{lang="DE"}

[ ]{lang="DE"}[Legacy PD Detection                     : Disabled]{lang="EN-US"}

[ Power Utilization Threshold            : 80]{lang="EN-US"}

[ ]{lang="EN-US"}[PSE Power Policy                         : Disabled]{lang="FR"}

[ PD Power Policy                          : Disabled]{lang="FR"}

[ PD Disconnect-Detection Mode           : DC]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x6755_56834_212012916}[显示]{style="font-family:宋体"}[PSE 7]{lang="FR"}[的信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[多]{style="font-family:宋体"}[PSE]{lang="FR"}[设备]{style="font-family:
宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display poe pse 7]{lang="FR"}]{#struct_0_x6755_56834_202004854}

[ PSE ID                                      : 7]{lang="FR"}

[ Slot No.                                    ]{lang="FR"}[: 2]{lang="EN-US"}

[ PSE Model                                   : LSBMPOEGV48TP]{lang="EN-US"}

[ PSE Status                                  : Enabled]{lang="EN-US"}

[ PSE Preempted                               : No]{lang="EN-US"}

[ Power Priority                              : Low]{lang="EN-US"}

[ Current Power                               : 130      W]{lang="EN-US"}

[ Average Power                               : 20       W]{lang="EN-US"}

[ Peak Power                                   : 240      W]{lang="EN-US"}

[ Max Power                                     : 200      W]{lang="EN-US"}

[ Remaining Guaranteed Power                : 120      W]{lang="EN-US"}

[ ]{lang="EN-US"}[PSE CPLD Version                            : 100]{lang="DE"}

[ PSE Software Version                       : 200]{lang="DE"}

[ ]{lang="DE"}[PSE Hardware Version                       : 100]{lang="EN-US"}

[ Legacy  PD Detection                       : Disabled]{lang="EN-US"}

[ Power Utilization Threshold              : 80]{lang="EN-US"}

[ ]{lang="EN-US"}[PSE Power Policy]{lang="FR"}[                           ]{lang="EN-US"}[: Disabled]{lang="FR"}

[ ]{lang="FR"}[PD Power Policy]{lang="FR"}[ ]{lang="FR"}[                           : Disabled]{lang="EN-US"}

[ PD Disconnect-Detection Mode             : DC]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1090636859}[显示]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe pse 7]{lang="EN-US"}]{#struct_0_x6755_56834_201939318}

[ PSE ID                                       : 7]{lang="EN-US"}

[ Chassis                                      : 1]{lang="EN-US"}

[ Slot No.                                     : 2]{lang="EN-US"}

[ SSlot No.                                    : 0]{lang="EN-US"}

[ PSE Model                                    : LSBMPOEGV48TP]{lang="EN-US"}

[ PSE Status                                   : Disabled]{lang="EN-US"}

[ PSE Preempted                               : No]{lang="EN-US"}

[ Power Priority                              : Low]{lang="EN-US"}

[ Current Power                               : 0        W]{lang="EN-US"}

[ Average Power                               : 0        W]{lang="EN-US"}

[ Peak Power                                     : 0        W]{lang="EN-US"}

[ Max Power                                    : 200      W]{lang="EN-US"}

[ Remaining Guaranteed Power                : 200      W]{lang="EN-US"}

[ ]{lang="EN-US"}[PSE CPLD Version                            : 100]{lang="DE"}

[ PSE Software Version                       : 200]{lang="DE"}

[ ]{lang="DE"}[PSE Hardware Version                       : 100]{lang="EN-US"}

[ Legacy PD Detection                        : Disabled]{lang="EN-US"}

[ Power Utilization Threshold               : 80]{lang="EN-US"}

[ PSE Power Policy                            : Disabled]{lang="EN-US"}

[ PD Power Policy                             : Disabled]{lang="EN-US"}

[ PD Disconnect Detection Mode              : DC]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display poe pse]{lang="EN-US"}]{#struct_0_x6755_56834_990288440}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_618253905}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_1589384422}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_941181438}

[[PSE ID]{lang="EN-US"}]{#struct_0_x6755_56834_202135926}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x880918483}[编号]{style="font-family:宋体"}

[[Slot No.]{lang="EN-US"}]{#struct_0_x6755_56834_1389863039}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1116668368}[所在槽号]{style="font-family:宋体"}

[[SSlot No.]{lang="EN-US"}]{#struct_0_x6755_56834_x1356005405}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1356070941}[所在的子槽位号]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_x6755_56834_129477045}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_169957457}[所在设备的成员编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[PSE Model]{lang="EN-US"}]{#struct_0_x6755_56834_202070390}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x424901359}[模块型号]{style="font-family:宋体"}

[[PSE Status]{lang="EN-US"}]{#struct_0_x6755_56834_x187009451}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_202266998}[供电状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1355677725}[：已使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_x1355743261}[：未使能]{style="font-family:宋体"}

[[Preempted]{lang="EN-US"}]{#struct_0_x6755_56834_x976666356}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1383940506}[供电抢占状态（该显示信息的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x6755_56834_202201462}[：表示该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[没有被抢占]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x6755_56834_202398070}[：表示该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[虽然被开启了，但是被其他]{style="font-family:宋体"}[PSE]{lang="EN-US"}[抢占了，无法供电]{style="font-family:宋体"}

[[Power Priority]{lang="EN-US"}]{#struct_0_x6755_56834_x1752750570}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1834939029}[供电优先级]{style="font-family:宋体"}

[[Current Power]{lang="EN-US"}]{#struct_0_x6755_56834_x862829521}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x981929587}[当前功率]{style="font-family:宋体"}

[[Average Power]{lang="EN-US"}]{#struct_0_x6755_56834_202332534}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x2101163801}[平均功率]{style="font-family:宋体"}

[[Peak Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1949422796}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x2057294582}[峰值功率]{style="font-family:宋体"}

[[Max Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1399154517}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_201873779}[最大功率]{style="font-family:宋体"}

[[Remaining Guaranteed Power]{lang="EN-US"}]{#struct_0_x6755_56834_1780182295}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x157250029}[剩余保证功率]{style="font-family:宋体"}[=]{lang="EN-US"}[PSE]{lang="EN-US"}[最大保证功率]{style="font-family:宋体"}[-]{lang="EN-US"}[该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[中优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[的接口最大功率之和]{style="font-family:宋体"}

[[PSE CPLD Version]{lang="EN-US"}]{#struct_0_x6755_56834_1556869605}

[[PSE CPLD]{lang="EN-US"}]{#struct_0_x6755_56834_201808243}[（]{style="font-family:宋体"}[Complex Programmable Logical Device]{lang="EN-US"}[，复杂可编程逻辑器件）版本]{style="font-family:宋体"}

[[PSE Software Version]{lang="EN-US"}]{#struct_0_x6755_56834_212012913}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_92422254}[软件版本]{style="font-family:宋体"}

[[PSE Hardware Version]{lang="EN-US"}]{#struct_0_x6755_56834_x1610361038}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_202004851}[硬件版本]{style="font-family:宋体"}

[[Legacy PD Detection]{lang="EN-US"}]{#struct_0_x6755_56834_1090636856}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1355005540}[非标准]{style="font-family:宋体"}[PD]{lang="EN-US"}[检测：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6755_56834_201939315}[：开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_202070387}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[Power Utilization Threshold]{lang="EN-US"}]{#struct_0_x6755_56834_1531413782}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_766609721}[功率告警阈值]{style="font-family:宋体"}

[[PSE Power Policy]{lang="EN-US"}]{#struct_0_x6755_56834_1269066371}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_202266995}[功率管理策略模式]{style="font-family:宋体"}

[[PD Power Policy]{lang="EN-US"}]{#struct_0_x6755_56834_x976666343}

[[PD]{lang="EN-US"}]{#struct_0_x6755_56834_x1384137113}[功率管理策略模式]{style="font-family:宋体"}

[[PD Disconnect Detection Mode]{lang="EN-US"}]{#struct_0_x6755_56834_x218801863}

[[PD]{lang="EN-US"}]{#struct_0_x6755_56834_202201459}[断开检测方式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1117013087 .myid}
[]{#_Toc404796823}[]{#struct_0_x6755_56834_x1312598804}[]{#_Toc257634902}

**PoE \-- PoE配置命令 \-- display poe pse interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_x332054165}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_406982465}
:::

[ ]{lang="EN-US"}

[**[display poe pse interface]{lang="EN-US"}**]{#struct_0_x6755_56834_x1566175286}[命令用来显示指定]{style="font-family:
宋体"}[PSE]{lang="EN-US"}[上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x580305118}

[**[display poe pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}***[ interface]{lang="EN-US"}**]{#struct_0_x6755_56834_202398067}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_585901583}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x645083897}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x205808697}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2134939333}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_383399819}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_63615059}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_164923948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_202332531}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x2101163798}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号，可以用]{style="font-family:宋体"}**[display poe device]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号和槽号的对应关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x740027964}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1702377120}[显示]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[上连接的所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电状态。]{style="font-family:宋体"}

[[\<Sysname\> display poe pse 7 interface]{lang="EN-US"}]{#struct_0_x6755_56834_x1093890572}

[ Interface   PoE        Priority  CurPower  Oper                IEEE     Detection]{lang="EN-US"}

[                                      (W)                             Class    Status]{lang="EN-US"}

[ GE1/0/1     Enabled   Low        4.4        On                   1         Delivering Power]{lang="EN-US"}

[ GE1/0/2     Enabled   Critical  0.0        Power-lack          -        Disabled]{lang="EN-US"}

[ GE1/0/3     Enabled   Low        0.0        Power-deny          -        Disabled]{lang="EN-US"}

[ GE1/0/4     Enabled   Critical  0.0        On                   -         Searching]{lang="EN-US"}

[ GE1/0/5     Enabled   Low        4.0        Power-limit        2         Delivering Power]{lang="EN-US"}

[ GE1/0/6     Enabled   Low        0.0        Power-itself       -         Disabled]{lang="EN-US"}

[ GE1/0/7     Disabled  Low        0.0        Off                  -         Fault]{lang="EN-US"}

[   \-\--  On State Ports: 2; Used: 8.4(W); Remaining: 171.6 (W)  \-\--]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display poe pse interface]{lang="EN-US"}]{#struct_0_x6755_56834_201873780}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_606071089}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_2117889312}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_1319970778}

[[Interface]{lang="EN-US"}]{#struct_0_x6755_56834_x132119551}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x270921142}[接口简称]{style="font-family:宋体"}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x617247163}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_202004852}[接口远程供电功能是否开启：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x6755_56834_201939316}[：开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_202135924}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x6755_56834_x880918485}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1389469823}[接口供电优先级：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Critical]{lang="EN-US"}]{#struct_0_x6755_56834_x841988429}[：]{lang="EN-US" style="font-family:宋体"}[最高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[High]{lang="EN-US"}]{#struct_0_x6755_56834_202070388}[：]{lang="EN-US" style="font-family:宋体"}[高]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x6755_56834_1531413769}ow[：]{lang="EN-US" style="font-family:宋体"}[低]{lang="EN-US" style="font-family:宋体"}

[[CurPower]{lang="EN-US"}]{#struct_0_x6755_56834_766937391}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x835807308}[接口当前功率]{style="font-family:宋体"}

[[Oper]{lang="EN-US"}]{#struct_0_x6755_56834_738690374}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_202266996}[接口工作状态]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x6755_56834_202398068}ff[：]{style="font-family:宋体"}[供电功能处于关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x6755_56834_585901582}n[：]{style="font-family:宋体"}[正在正常供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_x645083896}ower-lack[：]{style="font-family:
  宋体"}[剩余保证功率不够，导致无法给]{style="font-family:宋体"}Critical[接口供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_x205743161}ower-deny[：]{style="font-family:
  宋体"}[拒绝供电，]{style="font-family:宋体"}PD[要求功率大于配置功率]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{style="font-size:10.0pt;font-family:Symbol"}[Power-itself]{lang="EN-US"}]{#struct_0_x6755_56834_x149914392}[：]{style="font-family:
  宋体"}[外接设备正在自己供电]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x6755_56834_202332532}ower-limit[：]{style="font-family:宋体"}[正在受限供电，]{style="font-family:宋体"}PD[要求功率大于配置功率，]{style="font-family:宋体"}PSE[仍按配置功率供电]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x2101163795}[接口工作状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[IEEE Class]{lang="EN-US"}]{#struct_0_x6755_56834_375717283}

[[PD]{lang="EN-US"}]{#struct_0_x6755_56834_1491481398}[功率等级]{style="font-family:宋体"}

[[Detection Status]{lang="EN-US"}]{#struct_0_x6755_56834_x898047083}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_201873777}[接口检测状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x6755_56834_202004849}[：]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电]{lang="EN-US" style="font-family:宋体"}[处于]{style="font-family:宋体"}[关闭]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Searching]{lang="EN-US"}]{#struct_0_x6755_56834_x1248015312}[：正在搜索]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Delivering Power]{lang="EN-US"}]{#struct_0_x6755_56834_x1707031105}[：正在向]{lang="EN-US" style="font-family:
  宋体"}[PD]{lang="EN-US"}[供电]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Fault]{lang="EN-US"}]{#struct_0_x6755_56834_x665011416}[：错误]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Test]{lang="EN-US"}]{#struct_0_x6755_56834_201939313}[：测试状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Other Fault]{lang="EN-US"}]{#struct_0_x6755_56834_990288433}[：其他错误状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PD Disconnected]{lang="EN-US"}]{#struct_0_x6755_56834_780080359}[：]{style="font-family:宋体"}[PD]{lang="EN-US"}[未连接]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1201760568}[接口检测状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[[On State Ports ]{lang="EN-US"}]{#struct_0_x6755_56834_202135921}

[[正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x880918482}[接口数量]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_x6755_56834_1389797503}

[[该]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_313316578}[上供电]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口消耗的功率]{style="font-family:宋体"}

[[Remaining ]{lang="EN-US"}]{#struct_0_x6755_56834_202070385}

[[此]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1531413780}[上剩余功率]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#889115469 .myid}
[]{#_Toc404796824}[]{#struct_0_x6755_56834_766478649}[]{#_Toc257634903}

**PoE \-- PoE配置命令 \-- display poe pse interface power**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_x1347422951}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x2122564959}
:::

[ ]{lang="EN-US"}

[**[display poe pse interface power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1666021828}[命令用来显示指定]{style="font-family:宋体"}[PSE]{lang="EN-US"}[上]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的功率信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_202266993}

[**[display poe pse ]{lang="EN-US"}***[pse-id]{lang="EN-US"}*[ **interface power**]{lang="EN-US"}]{#struct_0_x6755_56834_x976666349}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1383743897}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_229974276}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1459839709}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1289376838}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1853202226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1856951765}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x2047496367}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_202201457}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x1312598790}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号，可以用]{style="font-family:宋体"}**[display poe device]{lang="EN-US"}**[命令查看]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号和槽号的对应关系。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1994003416}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1007090395}[显示]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[连接的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的功率信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe pse 7 interface power]{lang="EN-US"}]{#struct_0_x6755_56834_x1698618399}

[Interface  Current   Peak       Max        PD Description]{lang="EN-US"}

[            (W)        (W)        (W)]{lang="EN-US"}

[ GE1/0/25  4.4        4.5        4.6         IP Phone on Room 309 for Peter Smith]{lang="EN-US"}

[ GE1/0/26  4.4        4.5        15.4        IP Phone on Room 409 for Peter Pan]{lang="EN-US"}

[ GE1/0/27  15.0       15.3       15.4        Access Point on Room 509 for Peter]{lang="EN-US"}

[ GE1/0/28  0.0        0.0        5.0         IP Phone on Room 609 for Peter John]{lang="EN-US"}

[ GE1/0/29  0.0        0.0        4.0         IP Phone on Room 709 for Jack]{lang="EN-US"}

[ GE1/0/30  0.0        0.0        5.0         IP Phone on Room 809 for Alien]{lang="EN-US"}

[   \-\--  On State Ports: 3; Used: 23.8(W);  Remaining: 776.2(W) \-\--]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display poe pse interface power]{lang="EN-US"}]{#struct_0_x6755_56834_202398065}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_633146481}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_585901585}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_x645083903}

[[Interface]{lang="EN-US"}]{#struct_0_x6755_56834_1750768590}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1466812814}[接口简称]{style="font-family:宋体"}

[[Current]{lang="EN-US"}]{#struct_0_x6755_56834_x1242874887}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1064993885}[接口当前功率]{style="font-family:宋体"}

[[Peak]{lang="EN-US"}]{#struct_0_x6755_56834_202332529}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_237488370}[接口峰值功率]{style="font-family:宋体"}

[[Max]{lang="EN-US"}]{#struct_0_x6755_56834_1229036569}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1245596336}[接口最大功率]{style="font-family:宋体"}

[[PD Description]{lang="EN-US"}]{#struct_0_x6755_56834_x1102215280}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1198406321}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[描述信息，用于辅助用户识别]{style="font-family:宋体"}[PD]{lang="EN-US"}[的类型和位置等]{style="font-family:宋体"}

[[Ports On]{lang="EN-US"}]{#struct_0_x6755_56834_201873778}

[[正在供电的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1780182296}[接口数量]{style="font-family:宋体"}

[[Used]{lang="EN-US"}]{#struct_0_x6755_56834_x157184493}

[[所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1536221293}[接口当前消耗功率]{style="font-family:宋体"}

[[Remaining]{lang="EN-US"}]{#struct_0_x6755_56834_x1387457867}

[[此]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_201808242}[上的剩余功率]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#2096758968 .myid}
[]{#_Toc404796825}[]{#struct_0_x6755_56834_212012912}[]{#_Toc257634904}[]{#_Toc139168962}

**PoE \-- PoE配置命令 \-- display poe-power**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_202004850}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_1090636855}
:::

[ ]{lang="EN-US"}

[**[display poe-power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1354808932}[命令用来显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_219812796}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6755_56834_x1355939871}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[display poe-power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1782464416}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_1639556578}[模式：]{style="font-family:宋体"}

[**[display poe-power ]{lang="EN-US"}**[\[ **chassis** *chassis-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x2026624194}

[[集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_1922891257}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **poe-power** \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x1438406794}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1222483638}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_201939314}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_990288428}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1558571810}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1233266852}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1311364054}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1861145343}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1316513096}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x6755_56834_x1570105015}[：显示指定成员设备的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6755_56834_1922825721}[：显示指定成员设备的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，表示所有成员设备。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2077988386}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_202135922}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe-power]{lang="EN-US"}]{#struct_0_x6755_56834_202070386}

[ PoE Current Power                    : 1870     W]{lang="EN-US"}

[ PoE Average Power                    : 2100     W]{lang="EN-US"}

[ PoE Peak Power                        : 2350     W]{lang="EN-US"}

[ PoE Max Power                          : 2000     W]{lang="EN-US"}

[ PoE Nominal Power                     : 2500     W]{lang="EN-US"}

[ PoE Current Electric Current        : 3.00     A]{lang="EN-US"}

[ PoE Current Voltage                   : 55.00    V]{lang="EN-US"}

[ PoE Lower Input Threshold            : 111.22   V]{lang="EN-US"}

[ PoE Upper Input Threshold            : 131.00   V]{lang="EN-US"}

[ PoE Lower Output Threshold           : 45.00    V]{lang="EN-US"}

[ PoE Upper Output Threshold           : 57.00    V]{lang="EN-US"}

[ PoE Hardware Version                  : 0002]{lang="EN-US"}

[ PoE Software Version                  : 0001]{lang="EN-US"}

[ PoE Power Supplies                     : 2]{lang="EN-US"}

[ PoE Power Supply 1:]{lang="EN-US"}

[ Manufacturer                          : Tyco Electronics Com]{lang="EN-US"}

[ Type                                    : PSE2500-A]{lang="EN-US"}

[ Status                                  : Normal]{lang="EN-US"}

[ PoE Power Supply 2:]{lang="EN-US"}

[ Manufacturer                           : Tyco Electronics Com]{lang="EN-US"}

[ Type                                    : PSE2500-B]{lang="EN-US"}

[ Status                                  : Normal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1531413783}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe-power]{lang="EN-US"}]{#struct_0_x6755_56834_202201458}

[Chassis 1 ]{lang="EN-US"}[：]{style="font-family:宋体"}

[ PoE Current Power                     : 1870     W]{lang="EN-US"}

[ PoE Average Power                     : 2100     W]{lang="EN-US"}

[ PoE Peak Power                         : 2350     W]{lang="EN-US"}

[ PoE Max Power                          : 2000     W]{lang="EN-US"}

[ PoE Nominal Power                     : 2500     W]{lang="EN-US"}

[ PoE Current Electric Current        : 3.00     A]{lang="EN-US"}

[ PoE Current Voltage                   : 55.00    V]{lang="EN-US"}

[ PoE Lower Input Threshold            : 111.22   V]{lang="EN-US"}

[ PoE Upper Input Threshold            : 131.00   V]{lang="EN-US"}

[ PoE Lower Output Threshold           : 45.00    V]{lang="EN-US"}

[ PoE Upper Output Threshold           : 57.00    V]{lang="EN-US"}

[ PoE Hardware Version                  : 0002]{lang="EN-US"}

[ PoE Software Version                  : 0001]{lang="EN-US"}

[ PoE Power Supplies                    : 2]{lang="EN-US"}

[ PoE Power Supply 1:]{lang="EN-US"}

[     Manufacturer                       : Tyco Electronics Com]{lang="EN-US"}

[     Type                                 : PSE2500-A]{lang="EN-US"}

[     Status                              : Normal]{lang="EN-US"}

[ PoE Power Supply 2:]{lang="EN-US"}

[     Manufacturer                       : Tyco Electronics Com]{lang="EN-US"}

[     Type                                : PSE2500-B]{lang="EN-US"}

[     Status                              : Normal]{lang="EN-US"}

[Chassis 2 ]{lang="EN-US"}[：]{style="font-family:宋体"}

[PoE Current Power                      : 1870     W]{lang="EN-US"}

[ PoE Average Power                     : 2100     W]{lang="EN-US"}

[ PoE Peak Power                         : 2350     W]{lang="EN-US"}

[ PoE Max Power                           : 2000     W]{lang="EN-US"}

[ PoE Nominal Power                      : 2500     W]{lang="EN-US"}

[ PoE Current Electric Current         : 3.00     A]{lang="EN-US"}

[ PoE Current Voltage                    : 55.00    V]{lang="EN-US"}

[ PoE Lower Input Threshold             : 111.22   V]{lang="EN-US"}

[ PoE Upper Input Threshold             : 131.00   V]{lang="EN-US"}

[ PoE Lower Output Threshold            : 45.00    V]{lang="EN-US"}

[ PoE Upper Output Threshold           : 57.00    V]{lang="EN-US"}

[ PoE Hardware Version                   : 0002]{lang="EN-US"}

[ PoE Software Version                   : 0001]{lang="EN-US"}

[ PoE Power Supplies                      : 2]{lang="EN-US"}

[ PoE Power Supply 1:]{lang="EN-US"}

[ Manufacturer                             : Tyco Electronics Com]{lang="EN-US"}

[ Type                                       : PSE2500-A]{lang="EN-US"}

[ Status                                     : Normal]{lang="EN-US"}

[ PoE Power Supply 2:]{lang="EN-US"}

[ Manufacturer                              : Tyco Electronics Com]{lang="EN-US"}

[ Type                                        : PSE2500-B]{lang="EN-US"}

[ Status                                      ]{lang="EN-US"}[：]{style="font-family:宋体"}[Normal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1922432506}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的信息。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display poe-power]{lang="EN-US"}]{#struct_0_x6755_56834_1922235898}

[Slot 1 ]{lang="EN-US"}[：]{style="font-family:
宋体"}

[ PoE Current Power                     : 1870     W]{lang="EN-US"}

[ PoE Average Power                     : 2100     W]{lang="EN-US"}

[ PoE Peak Power                        : 2350     W]{lang="EN-US"}

[ PoE Max Power                          : 2000     W]{lang="EN-US"}

[ PoE Nominal Power                     : 2500     W]{lang="EN-US"}

[ PoE Current Electric Current        : 3.00     A]{lang="EN-US"}

[ PoE Current Voltage                   : 55.00    V]{lang="EN-US"}

[ PoE Lower Input Threshold            : 111.22   V]{lang="EN-US"}

[ PoE Upper Input Threshold            : 131.00   V]{lang="EN-US"}

[ PoE Lower Output Threshold           : 45.00    V]{lang="EN-US"}

[ PoE Upper Output Threshold           : 57.00    V]{lang="EN-US"}

[ PoE Hardware Version                  : 0002]{lang="EN-US"}

[ PoE Software Version                  : 0001]{lang="EN-US"}

[ PoE Power Supplies                    : 2]{lang="EN-US"}

[ PoE Power Supply 1:]{lang="EN-US"}

[     Manufacturer                       : Tyco Electronics Com]{lang="EN-US"}

[     Type                                : PSE2500-A]{lang="EN-US"}

[     Status                              : Normal]{lang="EN-US"}

[ PoE Power Supply 2:]{lang="EN-US"}

[     Manufacturer                       : Tyco Electronics Com]{lang="EN-US"}

[     Type                                 : PSE2500-B]{lang="EN-US"}

[     Status                              : Normal]{lang="EN-US"}

[Slot 2 ]{lang="EN-US"}[：]{style="font-family:
宋体"}

[PoE Current Power                      : 1870     W]{lang="EN-US"}

[ PoE Average Power                     : 2100     W]{lang="EN-US"}

[ PoE Peak Power                        : 2350     W]{lang="EN-US"}

[ PoE Max Power                          : 2000     W]{lang="EN-US"}

[ PoE Nominal Power                     : 2500     W]{lang="EN-US"}

[ PoE Current Electric Current        : 3.00     A]{lang="EN-US"}

[ PoE Current Voltage                   : 55.00    V]{lang="EN-US"}

[ PoE Lower Input Threshold            : 111.22   V]{lang="EN-US"}

[ PoE Upper Input Threshold            : 131.00   V]{lang="EN-US"}

[ PoE Lower Output Threshold           : 45.00    V]{lang="EN-US"}

[ PoE Upper Output Threshold           : 57.00    V]{lang="EN-US"}

[ PoE Hardware Version                  : 0002]{lang="EN-US"}

[ PoE Software Version                  : 0001]{lang="EN-US"}

[ PoE Power Supplies                    : 2]{lang="EN-US"}

[ PoE Power Supply 1:]{lang="EN-US"}

[ Manufacturer                           : Tyco Electronics Com]{lang="EN-US"}

[ Type                                    : PSE2500-A]{lang="EN-US"}

[ Status                                  : Normal]{lang="EN-US"}

[ PoE Power Supply 2:]{lang="EN-US"}

[ Manufacturer                           : Tyco Electronics Com]{lang="EN-US"}

[ Type                                    : PSE2500-B]{lang="EN-US"}

[ Status                                  ]{lang="EN-US"}[：]{style="font-family:宋体"}[Normal]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display poe-power]{lang="EN-US"}]{#struct_0_x6755_56834_x1312598805}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_627373361}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_1234029776}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_1221805405}

[[Chassis 1]{lang="EN-US"}]{#struct_0_x6755_56834_x547695353}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_1937748931}[的相关信息（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[Slot 1]{lang="EN-US"}]{#struct_0_x6755_56834_1922170362}

[[成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x6755_56834_x1848626237}[的相关信息（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[PoE Current Power]{lang="EN-US"}]{#struct_0_x6755_56834_1889646997}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_202398066}[当前功率]{style="font-family:宋体"}

[[PoE Average Power]{lang="EN-US"}]{#struct_0_x6755_56834_585901584}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x645083902}[平均功率]{style="font-family:宋体"}

[[PoE Peak Power]{lang="EN-US"}]{#struct_0_x6755_56834_1750834126}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x441364066}[峰值功率]{style="font-family:宋体"}

[[PoE Max Power]{lang="EN-US"}]{#struct_0_x6755_56834_1362509447}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_202332530}[最大供电功率]{style="font-family:宋体"}

[[PoE Nominal Power]{lang="EN-US"}]{#struct_0_x6755_56834_x2101163797}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1538516697}[额定功率]{style="font-family:宋体"}

[[PoE Current Electric Current]{lang="EN-US"}]{#struct_0_x6755_56834_x934007992}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1785101355}[当前电流]{style="font-family:宋体"}

[[PoE Current Voltage ]{lang="EN-US"}]{#struct_0_x6755_56834_2124188082}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x163197986}[当前电压]{style="font-family:宋体"}

[[PoE Lower Input Threshold]{lang="EN-US"}]{#struct_0_x6755_56834_1775587574}

[[输入交流电欠压阈值]{style="font-family:宋体"}]{#struct_0_x6755_56834_x204309657}

[[PoE Upper Input Threshold]{lang="EN-US"}]{#struct_0_x6755_56834_x979826055}

[[输入交流电过压阈值]{style="font-family:宋体"}]{#struct_0_x6755_56834_2124122546}

[[PoE Lower Output Threshold]{lang="EN-US"}]{#struct_0_x6755_56834_x526643152}

[[输出直流电欠压阈值]{style="font-family:宋体"}]{#struct_0_x6755_56834_1424187247}

[[PoE Upper Output Threshold]{lang="EN-US"}]{#struct_0_x6755_56834_582008618}

[[输出直流电过压阈值]{style="font-family:宋体"}]{#struct_0_x6755_56834_2124319154}

[[PoE Hardware Version]{lang="EN-US"}]{#struct_0_x6755_56834_620707882}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1515541697}[硬件版本号]{style="font-family:宋体"}

[[PoE Software Version]{lang="EN-US"}]{#struct_0_x6755_56834_x1726587510}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x985361475}[软件版本号]{style="font-family:宋体"}

[[PoE Power Supplies]{lang="EN-US"}]{#struct_0_x6755_56834_2124253618}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x537426705}[电源数目]{style="font-family:宋体"}

[[Manufacturer]{lang="EN-US"}]{#struct_0_x6755_56834_1219426652}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x709104174}[电源制造商，当设备不支持获取该参数时，该信息将显示为]{style="font-family:宋体"}[NONE]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x6755_56834_2124450226}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x899471387}[电源类型，当设备不支持获取该参数时，该信息将显示为]{style="font-family:宋体"}[NONE]{lang="EN-US"}

[[Status]{lang="EN-US"}]{#struct_0_x6755_56834_1303556498}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_2083064966}[电源状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x6755_56834_2124384690}[：正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_x6755_56834_1832408151}[：不在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_x6755_56834_x360728214}[：关机]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x6755_56834_2124581298}[：主用正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby ]{lang="EN-US"}]{#struct_0_x6755_56834_1827773460}[：备用正常]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Balanced]{lang="EN-US"}]{#struct_0_x6755_56834_82547030}[：负载分担]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redundant]{lang="EN-US"}]{#struct_0_x6755_56834_725923913}[：冗余备份]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Alarm]{lang="EN-US"}]{#struct_0_x6755_56834_2124515762}[：告警]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Faulty]{lang="EN-US"}]{#struct_0_x6755_56834_x1678915149}[：故障]{style="font-family:宋体"}

[[不同型号的设备支持的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1280005403}[电源状态不同，请以设备的实际情况为准]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1319701084 .myid}
[]{#_Toc404796826}[]{#struct_0_x6755_56834_2124712370}[]{#_Toc257634912}

**PoE \-- PoE配置命令 \-- display poe-profile**

------------------------------------------------------------------------

[**[display poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_x1684205445}[命令用来显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_738338954}

[**[display poe-profile ]{lang="EN-US"}**[\[ **index** *index* \| **name** *profile-name* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x808702638}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x957872046}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_903481811}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x589309822}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x989129623}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x2115234776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2124646834}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_1091911274}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1747903214}

[**[index]{lang="EN-US"}***[ index]{lang="EN-US"}*]{#struct_0_x6755_56834_1022742034}[：]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件的索引，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x6755_56834_593894584}[：]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1367360507}

[[如果不指定参数，将显示当前已存在的所有的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_2124188083}[配置文件的配置和应用信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x163132450}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2124122547}[显示当前的所有]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe-profile]{lang="EN-US"}]{#struct_0_x6755_56834_x526577616}

[ PoE Profile     Index   ApplyNum  Interfaces     Configuration]{lang="EN-US"}

[ forIPphone      1        6          GE1/0/5         poe enable]{lang="EN-US"}

[                                        GE1/0/6        poe priority critical]{lang="EN-US"}

[                                        GE1/0/7]{lang="EN-US"}

[                                        GE1/0/8]{lang="EN-US"}

[                                        GE1/0/9]{lang="EN-US"}

[                                        GE1/0/10]{lang="EN-US"}

[ forAP            2        2          GE1/0/11       poe enable]{lang="EN-US"}

[                                        GE1/0/12       poe max-power 14000]{lang="EN-US"}

[   \-\--  Total PoE profiles: 3, total ports: 0  \-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x2094822244}[显示索引为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe-profile index 1]{lang="EN-US"}]{#struct_0_x6755_56834_2124319155}

[ PoE Profile     Index   ApplyNum  Interfaces   Configuration]{lang="EN-US"}

[ forIPphone      1        6          GE1/0/5       poe enable]{lang="EN-US"}

[                                       GE1/0/6       poe priority critical]{lang="EN-US"}

[                                       GE1/0/7]{lang="EN-US"}

[                                       GE1/0/8]{lang="EN-US"}

[                                       GE1/0/9]{lang="EN-US"}

[                                       GE1/0/1]{lang="EN-US"}

[   \-\--  Total ports: 0  \-\--]{lang="EN-US"}

[]{#struct_0_x6755_56834_620642346}[[表1-10 ]{lang="EN-US"}[display poe-profile]{lang="EN-US"}]{#_Ref216168243}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_651690513}[[字段]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1847881396}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1701710765}

[[PoE Profile]{lang="EN-US"}]{#struct_0_x6755_56834_96358238}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1714980119}[配置文件的名称]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_x6755_56834_1812835562}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_2124253619}[配置文件的索引]{style="font-family:宋体"}

[[ApplyNum]{lang="EN-US"}]{#struct_0_x6755_56834_x537492241}

[[应用到的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1967862836}[接口数量]{style="font-family:宋体"}

[[Interfaces]{lang="EN-US"}]{#struct_0_x6755_56834_x1259810092}

[[应用了]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1776958010}[配置文件的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口名称简称]{style="font-family:宋体"}

[[Configuration]{lang="EN-US"}]{#struct_0_x6755_56834_x292253946}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_2124450227}[配置文件的配置项]{style="font-family:宋体"}

[[Total PoE profiles]{lang="EN-US"}]{#struct_0_x6755_56834_2124384691}

[[创建的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1832473687}[配置文件数目]{style="font-family:宋体"}

[[total ports]{lang="EN-US"}]{#struct_0_x6755_56834_2124515763}

[[应用]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1678980685}[配置文件的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1898623418 .myid}
[]{#_Toc404796827}[]{#struct_0_x6755_56834_x1775132119}[]{#_Toc257634913}[]{#_Toc220040517}[]{#_Toc220053792}[]{#_Toc220062494}[]{#_Toc220040524}[]{#_Toc220053799}[]{#_Toc220062501}[]{#_Toc220040525}[]{#_Toc220053800}[]{#_Toc220062502}[]{#_Toc220040526}[]{#_Toc220053801}[]{#_Toc220062503}[]{#_Toc220040548}[]{#_Toc220053823}[]{#_Toc220062525}[]{#_Toc220040549}[]{#_Toc220053824}[]{#_Toc220062526}[]{#_Toc220040556}[]{#_Toc220053831}[]{#_Toc220062533}[]{#_Toc220040557}[]{#_Toc220053832}[]{#_Toc220062534}[]{#_Toc220040579}[]{#_Toc220053854}[]{#_Toc220062556}

**PoE \-- PoE配置命令 \-- display poe-profile interface**

------------------------------------------------------------------------

[**[display poe-profile interface]{lang="EN-US"}**]{#struct_0_x6755_56834_2139178571}[命令用来显示指定]{style="font-family:
宋体"}[PoE]{lang="EN-US"}[接口当前生效的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件配置项和应用的所有信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x306008822}

[**[display poe-profile interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x6755_56834_2124712371}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1684270981}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x389608812}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_719954003}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_981614215}

[[network-operator]{lang="EN-US"}]{#struct_0_x6755_56834_x1067304483}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x178676046}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x6755_56834_285523559}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x323628720}

[*[interface-type interfece-number]{lang="EN-US"}*]{#struct_0_x6755_56834_2124646835}[：指定接口类型及接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1091976810}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x579780419}[显示]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的当前]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件配置和应用的所有信息。]{style="font-family:宋体"}

[[\<Sysname\> display poe-profile interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x6755_56834_812974752}

[ PoEProfile     Index   ApplyNum  Interface   Effective configuration]{lang="EN-US"}

[ forIPphone      1        6          GE1/0/1    poe enable]{lang="EN-US"}

[                                                    poe priority critical]{lang="EN-US"}

[[因为]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x401155895}[配置文件的配置项（]{style="font-family:宋体"}[Configuration]{lang="EN-US"}[）可能只有部分应用成功，所以显示的是该接口当前生效的配置项（]{style="font-family:宋体"}[Effective configuration]{lang="EN-US"}[），其它字段的描述请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-10]{lang="EN-US"}](?-1319701084#_Ref216168243)[。]{style="font-family:
宋体"}
:::

::: {#423027199 .myid}
[]{#_Toc404796828}[]{#struct_0_x6755_56834_x810338337}[]{#_Toc257634914}[]{#_Toc220040583}[]{#_Toc220053858}[]{#_Toc220062560}[]{#_Toc220040584}[]{#_Toc220053859}[]{#_Toc220062561}[]{#_Toc220040603}[]{#_Toc220053878}[]{#_Toc220062580}[]{#_Toc220040604}[]{#_Toc220053879}[]{#_Toc220062581}[]{#_Toc220040605}[]{#_Toc220053880}[]{#_Toc220062582}[]{#_Toc220040606}[]{#_Toc220053881}[]{#_Toc220062583}

**PoE \-- PoE配置命令 \-- poe disconnect**

------------------------------------------------------------------------

[**[poe disconnect]{lang="EN-US"}**]{#struct_0_x6755_56834_x726239465}[命令用来配置]{style="font-family:宋体"}[PD]{lang="EN-US"}[断开检测的方式。]{style="font-family:宋体"}

[**[undo poe disconnect]{lang="EN-US"}**]{#struct_0_x6755_56834_x1118103006}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124188080}

[**[poe disconnect]{lang="EN-US"}**[ { **ac** \| **dc** }]{lang="EN-US"}]{#struct_0_x6755_56834_x163066914}

[**[undo poe disconnect]{lang="EN-US"}**]{#struct_0_x6755_56834_x934093823}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1778624948}

[[PD]{lang="EN-US"}]{#struct_0_x6755_56834_984396692}[断开检测的方式与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1660856099}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1673924206}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1812658613}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_38540735}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2124122544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x526774224}

[**[ac]{lang="EN-US"}**]{#struct_0_x6755_56834_1838886668}[：]{style="font-family:宋体"}[PD]{lang="EN-US"}[断开检测方式为交流检测方式。]{style="font-family:宋体"}

[**[dc]{lang="EN-US"}**]{#struct_0_x6755_56834_80030435}[：]{style="font-family:宋体"}[PD]{lang="EN-US"}[断开检测方式为直流检测方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_95723611}

[[改变]{style="font-family:宋体"}[PD]{lang="EN-US"}]{#struct_0_x6755_56834_x627986022}[断开的检测方式，可能会导致连接的]{style="font-family:宋体"}[PD]{lang="EN-US"}[断电，请谨慎使用。]{style="font-family:宋体"}

[[由于不同型号的设备采用的的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_165967050}[芯片不同，用户在配置时采用哪种检测方式以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x854910840}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x298126614}[配置]{style="font-family:宋体"}[PD]{lang="EN-US"}[断开检测的方式为直流检测方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_2124319152}

[\[Sysname\] poe disconnect dc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_620576810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x1358517706}
:::

::: {#1057741334 .myid}
[]{#OLE_LINK4}[]{#OLE_LINK3}[]{#_Toc404796829}[]{#struct_0_x6755_56834_x496761497}[]{#_Toc257634915}

**PoE \-- PoE配置命令 \-- poe enable**

------------------------------------------------------------------------

[**[poe enable]{lang="EN-US"}**]{#struct_0_x6755_56834_2124253616}[命令用来开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电功能。]{style="font-family:宋体"}

[**[undo poe enable]{lang="EN-US"}**]{#struct_0_x6755_56834_2124450224}[命令用来关闭]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x899602459}

[**[poe enable]{lang="EN-US"}**]{#struct_0_x6755_56834_x228377292}

[**[undo poe enable]{lang="EN-US"}**]{#struct_0_x6755_56834_1608420453}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x332782750}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_2124384688}[接口远程供电功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124581296}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1827380244}[接口视图]{style="font-family:宋体"}[/PoE profile]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_890254335}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x5388146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x2012532370}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1794261837}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[PoE profile]{lang="EN-US"}]{#struct_0_x6755_56834_x212657365}[视图下配置时，如果该]{lang="EN-US" style="font-family:宋体"}[PoE profile]{lang="EN-US"}[已经应用到]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口，需先取消该]{lang="EN-US" style="font-family:宋体"}[PoE profile]{lang="EN-US"}[在]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口视图下配置时，若已用]{style="font-family:宋体"}]{#struct_0_x6755_56834_2027571068}[PoE]{lang="EN-US"}[配置文件对该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口进行过配置，应先取消]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件在该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124515760}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1679046221}[开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_2124712368}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] poe enable]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x6755_56834_2124646832}[在]{style="font-family:宋体"}[PoE profile abc]{lang="EN-US"}[中，开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_1092042346}

[\[Sysname\] poe-profile abc]{lang="FR"}

[\[]{lang="EN-US"}[Sysname]{lang="FR"}[-poe-profile-abc-1\] poe enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_834695035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_2065063561}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe interface]{lang="EN-US"}**]{#struct_0_x6755_56834_x2063162078}
:::

::::: {#1326584299 .myid}
[]{#OLE_LINK28}[]{#OLE_LINK27}[]{#_Toc404796830}[]{#struct_0_x6755_56834_x2047771157}[]{#_Toc257634916}

**PoE \-- PoE配置命令 \-- poe enable pse**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 14 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_93457829}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_2124188081}
:::

[ ]{lang="EN-US"}

[**[poe enable pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x163001378}[命令用来开启]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的远程供电功能。]{style="font-family:宋体"}

[**[undo poe enable pse]{lang="EN-US"}**]{#struct_0_x6755_56834_2124319153}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_620511274}

[**[poe enable pse ]{lang="EN-US"}***[pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x1724048174}

[**[undo]{lang="EN-US"}**[ **poe enable pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_578584519}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1099410437}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_2124253617}[远程供电功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x538147601}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_647332926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1497890162}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2124450225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x899667995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x687957239}

[*[pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x1906531552}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1373569484}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2124384689}[开启]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的远程供电功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_1832997976}

[\[Sysname\] poe enable pse 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1819429338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x786405167}
:::::

::: {#1225018322 .myid}
[]{#OLE_LINK26}[]{#OLE_LINK25}[]{#_Toc404796831}[]{#struct_0_x6755_56834_977243126}[]{#_Toc257634917}

**PoE \-- PoE配置命令 \-- poe legacy enable**

------------------------------------------------------------------------

[**[poe legacy enable]{lang="EN-US"}**]{#struct_0_x6755_56834_2124581297}[命令用来开启]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的检测非标准]{style="font-family:宋体"}[PD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo poe legacy enable]{lang="EN-US"}**]{#struct_0_x6755_56834_2124712369}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1684795268}

[[单]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1025728114}[设备：]{style="font-family:宋体"}

[**[poe legacy enable]{lang="EN-US"}**]{#struct_0_x6755_56834_x1494689704}

[**[undo]{lang="EN-US"}**[ **poe legacy enable**]{lang="EN-US"}]{#struct_0_x6755_56834_1799653480}

[[多]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_190904993}[设备：]{style="font-family:宋体"}

[**[poe legacy enable]{lang="EN-US"}**[ **pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_x99009186}

[**[undo]{lang="EN-US"}**[ **poe legacy enable** **pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_2124646833}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1092107882}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_2124188078}[检测非标准]{style="font-family:宋体"}[PD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x162542641}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x562558369}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_746552402}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1959791633}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x426856424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x701687640}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x1167765640}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124122542}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2124319150}[开启]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的检测非标准]{style="font-family:宋体"}[PD]{lang="EN-US"}[功能。（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_620445738}

[\[Sysname\] poe legacy enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_2124253614}[开启]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的检测非标准]{style="font-family:宋体"}[PD]{lang="EN-US"}[功能。（多]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x538213137}

[\[Sysname\] poe legacy enable pse 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2146609526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display poe pse]{lang="EN-US"}**]{#struct_0_x6755_56834_2000088017}
:::

::: {#-308036322 .myid}
[]{#_Toc404796832}[]{#struct_0_x6755_56834_x206455742}[]{#_Toc257634918}

**PoE \-- PoE配置命令 \-- poe max-power**

------------------------------------------------------------------------

[**[poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_54540397}[命令用来配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的最大功率。]{style="font-family:宋体"}

[**[undo poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_666584333}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124450222}

[**[poe max-power]{lang="EN-US"}**[ *max-power*]{lang="EN-US"}]{#struct_0_x6755_56834_x899209243}

[**[undo poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1004336116}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2046503903}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1263201417}[接口的最大功率为]{style="font-family:宋体"}[15400]{lang="EN-US"}[毫瓦。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x140619324}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x579523839}[接口视图]{style="font-family:宋体"}[/PoE profile]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1568831227}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2124384686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1832539224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x748600141}

[*[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_1992036755}[：为]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口分配的最大供电功率，单位为毫瓦，按照一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1598078490}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_117617661}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的最大功率为]{style="font-family:宋体"}[12000]{lang="EN-US"}[毫瓦。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_835907723}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] poe max-power 12000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_485822044}[通过]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的最大供电功率为]{style="font-family:宋体"}[12000]{lang="EN-US"}[毫瓦。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_2124581294}

[\[Sysname\] poe-profile abc]{lang="FR"}

[\[]{lang="EN-US"}[Sysname]{lang="FR"}[-poe-profile-abc-1\] poe max-power 12000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1827511316}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe max-power(System view)]{lang="EN-US"}**]{#struct_0_x6755_56834_1269147609}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe power max-value]{lang="EN-US"}**]{#struct_0_x6755_56834_x2112912406}
:::

::: {#991081612 .myid}
[]{#_Toc404796833}[]{#struct_0_x6755_56834_1410653207}[]{#_Toc257634919}

**PoE \-- PoE配置命令 \-- poe max-power (System view)**

------------------------------------------------------------------------

[**[poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_500541202}[命令用来配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的最大供电功率。]{style="font-family:宋体"}

[**[undo poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_x389666250}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1096167013}

[[单]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_2124515758}[设备：]{style="font-family:宋体"}

[**[poe max-power ]{lang="EN-US"}***[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_x1679570508}

[**[undo]{lang="EN-US"}**[ **poe max-power**]{lang="EN-US"}]{#struct_0_x6755_56834_1788391367}

[[多]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1121522639}[设备：]{style="font-family:宋体"}

[**[poe pse ]{lang="EN-US"}***[pse-id]{lang="EN-US"}***[ max-power ]{lang="EN-US"}***[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_x1263357918}

[**[undo poe pse ]{lang="EN-US"}***[pse-id]{lang="EN-US"}***[ max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_756798771}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124712366}

[[不同型号的设备支持的缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1683812228}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x956279751}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1899355617}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_966912306}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x37302389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1802860077}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_206709479}

[*[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_2124646830}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的最大功率，单位为瓦，按照一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_1092173418}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x773574002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为保证对优先级为]{lang="EN-US" style="font-family:宋体"}[Critical]{lang="EN-US"}]{#struct_0_x6755_56834_x1661152053}[的]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的供电，]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[最大功率必须大于或等于该]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[所有]{lang="EN-US" style="font-family:宋体"}[Critical]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的最大功率之和。当]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[上所有]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}[消耗的功率大于]{lang="EN-US" style="font-family:宋体"}[PSE]{lang="EN-US"}[最大功率时，将会有]{lang="EN-US" style="font-family:宋体"}[PD]{lang="EN-US"}[断电。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各]{style="font-family:宋体"}]{#struct_0_x6755_56834_x212963665}[PSE]{lang="EN-US"}[的最大供电功率之和不能超过]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的最大供电功率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_899839275}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_751995236}[配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的最大供电功率为]{style="font-family:宋体"}[150]{lang="EN-US"}[瓦。（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_2124188079}

[\[Sysname\] poe max-power 150]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x162477105}[配置]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的最大供电功率为]{style="font-family:宋体"}[150]{lang="EN-US"}[瓦。（多]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x1379446399}

[\[Sysname\] poe pse 7 max-power 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1532312372}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe priority pse]{lang="EN-US"}**]{#struct_0_x6755_56834_x168690060}
:::

::: {#-173644980 .myid}
[]{#_Toc404796834}[]{#struct_0_x6755_56834_x224452216}[]{#_Toc257634920}

**PoE \-- PoE配置命令 \-- poe mode**

------------------------------------------------------------------------

[**[poe mode]{lang="EN-US"}**]{#struct_0_x6755_56834_334424717}[命令用来配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电模式。]{style="font-family:宋体"}

[**[undo poe mode]{lang="EN-US"}**]{#struct_0_x6755_56834_657585160}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x842685458}

[**[poe mode]{lang="EN-US"}**[ { **signal** \| **spare** }]{lang="EN-US"}]{#struct_0_x6755_56834_2124122543}

[**[undo poe mode]{lang="EN-US"}**]{#struct_0_x6755_56834_x526315472}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_642032446}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_83968850}[接口远程供电模式为采用信号线供电。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x995842158}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1409432942}[接口视图]{style="font-family:宋体"}[/PoE profile]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x624084436}

[[network-admin]{lang="FR"}]{#struct_0_x6755_56834_1989881354}

[[mdc-admin]{lang="FR"}]{#struct_0_x6755_56834_2124319151}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_620380202}

[**[signal]{lang="EN-US"}**]{#struct_0_x6755_56834_x802349511}[：]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电方式为采用信号线供电，即使用]{style="font-family:宋体"}[3/5]{lang="EN-US"}[类双绞线中传输数据所用的线对（]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:宋体"}[3]{lang="EN-US"}[、]{style="font-family:
宋体"}[6]{lang="EN-US"}[）同时传输直流电。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[spare]{lang="EN-US"}**]{#struct_0_x6755_56834_575277685}[：]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电方式为采用空闲线供电，即使用]{style="font-family:宋体"}[3/5]{lang="EN-US"}[类双绞线中没有被使用的线对（]{style="font-family:宋体"}[4]{lang="EN-US"}[、]{style="font-family:宋体"}[5]{lang="EN-US"}[、]{style="font-family:宋体"}[7]{lang="EN-US"}[、]{style="font-family:
宋体"}[8]{lang="EN-US"}[）来传输直流电。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x917415660}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1083256948}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电的方式为采用信号线供电。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_344154350}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] poe mode signal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x2143303906}[通过]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口远程供电的方式为采用信号线供电。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_2124253615}

[\[Sysname\] poe-profile abc]{lang="FR"}

[\[]{lang="EN-US"}[Sysname]{lang="FR"}[-poe-profile-abc-1\] poe mode signal]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x538278673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_597984963}
:::

::: {#-777720402 .myid}
[]{#_Toc404796835}[]{#struct_0_x6755_56834_x1090320087}[]{#_Toc257634921}

**PoE \-- PoE配置命令 \-- poe pd-description**

------------------------------------------------------------------------

[**[poe pd-description]{lang="EN-US"}**]{#struct_0_x6755_56834_1732379220}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo poe pd-description]{lang="EN-US"}**]{#struct_0_x6755_56834_x1901574792}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1267983021}

[**[poe pd-description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x6755_56834_x779251558}

[**[undo poe pd-description]{lang="EN-US"}**]{#struct_0_x6755_56834_2124450223}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x899274779}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1298266088}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[的描述信息为空，即没有描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1435451933}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x784818179}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x412114796}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_726115455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1538519920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1518083094}

[*[text]{lang="EN-US"}*]{#struct_0_x6755_56834_2124384687}[：]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1832604760}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_870138471}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口连接]{style="font-family:宋体"}[PD]{lang="EN-US"}[的描述信息为连接]{style="font-family:宋体"}[101]{lang="EN-US"}[室的]{style="font-family:宋体"}[IP]{lang="EN-US"}[电话。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x780660672}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] poe pd-description IP Phone For Room 101]{lang="EN-US"}
:::

::: {#-1024130322 .myid}
[]{#_Toc404796836}[]{#struct_0_x6755_56834_204358958}[]{#_Toc257634922}

**PoE \-- PoE配置命令 \-- poe pd-policy priority**

------------------------------------------------------------------------

[**[poe pd-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1432375523}[命令用来配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口功率管理策略为优先级策略。]{style="font-family:宋体"}

[**[undo poe pd-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1275186745}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2124581295}

[**[poe pd-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1827576852}

[**[undo poe pd-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1616923140}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x415062480}

[[没有配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_1398794363}[接口功率管理策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_31861438}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1855196455}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2117014505}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1658355956}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2124515759}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1679636044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在没有开启]{style="font-family:宋体"}]{#struct_0_x6755_56834_2124712367}[PoE]{lang="EN-US"}[接口功率管理的情况下，如果]{style="font-family:宋体"}[PSE]{lang="EN-US"}[功率过载，则不对新接入的]{style="font-family:宋体"}[PD]{lang="EN-US"}[供电。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在开启]{style="font-family:宋体"}]{#struct_0_x6755_56834_2124646831}[PoE]{lang="EN-US"}[接口功率管理优先级策略的情况下，如果]{style="font-family:宋体"}[PSE]{lang="EN-US"}[功率过载，接入新的]{style="font-family:宋体"}[PD]{lang="EN-US"}[，将对优先级低的]{style="font-family:宋体"}[PD]{lang="EN-US"}[断电，保证优先级高的]{style="font-family:宋体"}[PD]{lang="EN-US"}[供电。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1092238954}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x267471846}[配置]{style="font-family:宋体"}[PD]{lang="EN-US"}[功率管理策略为优先级策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_9475555}

[\[Sysname\] poe pd-policy priority]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x819231744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x2008195748}
:::

::::: {#1676417483 .myid}
[]{#_Toc404796837}[]{#struct_0_x6755_56834_1309108431}[]{#_Toc257634923}

**PoE \-- PoE配置命令 \-- poe power max-value**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 15 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_x604695273}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x78235475}
:::

[ ]{lang="EN-US"}

[**[poe power max-value]{lang="EN-US"}**]{#struct_0_x6755_56834_1611536143}[命令用来配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的最大供电功率。]{style="font-family:宋体"}

[**[undo poe power max-value]{lang="EN-US"}**]{#struct_0_x6755_56834_x59052621}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x695857350}

[[集中式设备]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x6755_56834_1372353663}[分布式设备－独立运行模式：]{style="font-family:宋体"}

[**[poe power max-value ]{lang="EN-US"}***[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_688298816}

[**[undo poe power max-value]{lang="EN-US"}**]{#struct_0_x6755_56834_479901118}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_x212676842}[模式：]{style="font-family:宋体"}

[**[poe power chassis]{lang="EN-US"}***[ chassis-number ]{lang="EN-US"}***[max-value ]{lang="EN-US"}***[max-power]{lang="EN-US"}*]{#struct_0_x6755_56834_x604760809}

[**[undo poe power chassis]{lang="EN-US"}***[ chassis-number]{lang="EN-US"}***[ max-value]{lang="EN-US"}**]{#struct_0_x6755_56834_x1955073660}

[[集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x6755_56834_1518820298}[模式：]{style="font-family:宋体"}

[**[poe]{lang="EN-US"}**[ **power** **slot** *slot-number* **max-value** *max-power*]{lang="EN-US"}]{#struct_0_x6755_56834_1286145061}

[**[undo]{lang="EN-US"}**[ **poe** **power** **slot** *slot-number* **max-value**]{lang="EN-US"}]{#struct_0_x6755_56834_x874791332}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1140058159}

[[不同型号的设备支持的缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x6755_56834_1360455857}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1782553162}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1235288625}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1155810765}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_2107169953}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1191169930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604564201}

[*[max-power]{lang="FR"}*]{#struct_0_x6755_56834_1518060462}[：]{style="font-family:宋体"}[PoE]{lang="FR"}[电源的最大供电功率]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[PoE]{lang="FR"}[电源能提供给各]{style="font-family:
宋体"}[PSE]{lang="FR"}[的最大功率，单位为瓦，以一定的步长取值。不同型号的设备支持的步长和取值范围不同，请以设备的实际情况为准。考虑到瞬时峰值功率的影响，实际可用的最大功率比配置的要多]{style="font-family:宋体"}[5%]{lang="EN-US"}[左右的额度。]{style="font-family:宋体"}

[**[chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x6755_56834_913114410}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x6755_56834_1518754762}[：表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_669343896}

[[需要注意的是，配置的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x284584603}[电源最大供电功率不可大于]{style="font-family:宋体"}[PoE]{lang="EN-US"}[电源的额定功率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_797316919}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_119013880}[配置设备的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[最大功率为]{style="font-family:宋体"}[2000]{lang="EN-US"}[瓦。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_1216394166}

[\[Sysname\] poe power max-value 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604629737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_1076890389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe max-power(System view)]{lang="EN-US"}**]{#struct_0_x6755_56834_x877841401}
:::::

::: {#758594117 .myid}
[]{#_Toc404796838}[]{#struct_0_x6755_56834_x1505849752}[]{#_Toc257634924}

**PoE \-- PoE配置命令 \-- poe priority**

------------------------------------------------------------------------

[**[poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x1431389348}[命令用来配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **poe priority**]{lang="EN-US"}]{#struct_0_x6755_56834_x1075357109}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1110095804}

[**[poe priority]{lang="EN-US"}**[ { **critical** \| **high** \| **low** }]{lang="EN-US"}]{#struct_0_x6755_56834_8073843}

[**[undo poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_2053216950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604433129}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x826508088}[接口供电优先级为]{style="font-family:宋体"}**[low]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_827762201}

[[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1774831739}[接口视图]{style="font-family:宋体"}[/PoE profile]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1994344046}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x2137314504}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_248509351}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1278282153}

[**[critical]{lang="EN-US"}**]{#struct_0_x6755_56834_x604498665}[：配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级为最高，即将该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口置为供电保证模式，插入该接口的]{style="font-family:宋体"}[PD]{lang="EN-US"}[可以以最高优先级得到供电。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_x6755_56834_283022911}[：配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级为高。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_x6755_56834_936458390}**[：]{style="font-family:宋体"}**[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级为低。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x823800030}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x6755_56834_719454685}[PSE]{lang="EN-US"}[功率过载的情况下，优先对供电优先级高的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口进行供电。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1034803265}[PoE]{lang="EN-US"}[配置文件视图下配置时，如果该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件已经应用到]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口，需先取消该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件在]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x6755_56834_x406759538}[PoE]{lang="EN-US"}[接口视图下配置时，若已用]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件对该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口进行过配置，应先取消]{style="font-family:宋体"}[PoE]{lang="EN-US"}[配置文件在该]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口的应用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了相同的优先级，接口编号小的]{style="font-family:宋体"}]{#struct_0_x6755_56834_1871973115}[PoE]{lang="EN-US"}[接口的优先级高，支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604302057}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1601107995}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_1992828924}

[\[Sysname\] interface gigabitEthernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] poe priority critical]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_28357327}[通过]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[配置]{style="font-family:宋体"}[PoE]{lang="EN-US"}[接口供电优先级为]{style="font-family:宋体"}[Critical]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_1379593780}

[\[Sysname\] poe-profile abc]{lang="FR"}

[\[]{lang="EN-US"}[Sysname]{lang="FR"}[-poe-profile-abc-1\] poe priority critical]{lang="EN-US"}

[\[Sysname-poe-profile-abc-1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitEthernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] apply poe-profile name abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1730783495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe pd-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x604367593}
:::

::::: {#1812833052 .myid}
[]{#_Toc404796839}[]{#struct_0_x6755_56834_x2020258072}[]{#_Toc257634925}

**PoE \-- PoE配置命令 \-- poe priority (system view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 16 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_1989608224}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_211276374}
:::

[ ]{lang="EN-US"}

[**[poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x1126327624}[命令用来配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电优先级。]{style="font-family:宋体"}

[**[undo poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x1964653296}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1892213114}

[**[poe priority ]{lang="EN-US"}**[{ **critical** \| **high** \| **low** } **pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_x1765934307}

[**[undo]{lang="EN-US"}**[ **poe priority pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_x604170985}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_381939926}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1471687801}[供电优先级为]{style="font-family:宋体"}**[low]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x383419444}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1543771313}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x539248626}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x2145941818}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x813293013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604236521}

[**[critical]{lang="EN-US"}**]{#struct_0_x6755_56834_x464594445}[：配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电优先级为最高，即将该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[置为供电保证模式，可以以最高优先级得到供电。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_x6755_56834_1928917909}[：配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电优先级为高。]{style="font-family:宋体"}

[**[low]{lang="EN-US"}**]{#struct_0_x6755_56834_2000928286}**[：]{style="font-family:宋体"}**[配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电优先级为低。]{style="font-family:宋体"}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x575489296}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1990924012}

[[当]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x868483534}[功率过载时，]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x6755_56834_x604695272}[PSE]{lang="EN-US"}[功率管理优先级策略，将优先对供电优先级高的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[进行供电（如果优先级相同，]{style="font-family:宋体"}[PSE ID]{lang="EN-US"}[小的优先供电）。比如有新的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}[功能，该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[优先级配置高，系统将对供电优先级低的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[断电，以保证对优先级高的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的供电；如果]{style="font-family:宋体"}[PSE]{lang="EN-US"}[优先级配置低，该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[将不能获得供电。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有配置]{style="font-family:宋体"}]{#struct_0_x6755_56834_x604760808}[PSE]{lang="EN-US"}[功率管理优先级策略，如果有新的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}[功能，该]{style="font-family:宋体"}[PSE]{lang="EN-US"}[将不能获得供电。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1955008124}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x604564200}[配置]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的供电优先级为]{style="font-family:宋体"}[critical]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_1518125998}

[\[Sysname\] poe priority critical pse 7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_838230733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe pse-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x56365270}
:::::

::::: {#1900204047 .myid}
[]{#_Toc404796840}[]{#struct_0_x6755_56834_x1626076485}[]{#_Toc257634926}

**PoE \-- PoE配置命令 \-- poe pse-policy priority**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 17 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_x850993857}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x413166310}
:::

[ ]{lang="EN-US"}

[**[poe pse-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x29050031}[命令用来配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[功率管理策略为优先级策略。]{style="font-family:宋体"}

[**[undo poe pse-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_x604629736}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1076955925}

[**[poe pse-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1110544815}

[**[undo poe pse-policy priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1336137455}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_2083960624}

[[没有配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x865310298}[功率管理策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_811802860}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1160561542}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1598502976}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x604433128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x826573624}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1209949960}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在没有开启]{style="font-family:宋体"}]{#struct_0_x6755_56834_x604498664}[PSE]{lang="EN-US"}[功率管理的情况下，如果]{style="font-family:宋体"}[PoE]{lang="EN-US"}[功率过载，则不对新接入的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在开启]{style="font-family:宋体"}]{#struct_0_x6755_56834_x604302056}[PSE]{lang="EN-US"}[功率管理优先级策略的情况下，如果]{style="font-family:宋体"}[PoE]{lang="EN-US"}[功率过载，分为两种情况：如果新接入的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[优先级是最低的（为]{style="font-family:宋体"}[Low]{lang="EN-US"}[），则不对新接入的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电；如果接入新的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[优先级高（为]{style="font-family:宋体"}[High]{lang="EN-US"}[或者]{style="font-family:宋体"}[Critical]{lang="EN-US"}[），将对优先级低的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[断电，保证给优先级高的]{style="font-family:宋体"}[PSE]{lang="EN-US"}[供电。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1601042459}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x1648045913}[配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[功率管理策略为优先级策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_1396477275}

[\[Sysname\] poe pse-policy priority]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1716990783}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe priority(System view)]{lang="EN-US"}**]{#struct_0_x6755_56834_x604367592}
:::::

::::: {#-675560330 .myid}
[]{#_Toc404796841}[]{#struct_0_x6755_56834_x2020192536}[]{#_Toc257634927}

**PoE \-- PoE配置命令 \-- poe temperature-protection**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_2048938139}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x1315579167}
:::

[ ]{lang="EN-US"}

[**[poe temperature-protection enable]{lang="EN-US"}**]{#struct_0_x6755_56834_x352753980}[命令用来开启设备]{style="font-family:宋体"}[PoE]{lang="EN-US"}[过温保护功能。]{style="font-family:宋体"}

[**[undo poe temperature-protection enable]{lang="EN-US"}**]{#struct_0_x6755_56834_1323996387}[命令用来关闭设备]{style="font-family:宋体"}[PoE]{lang="EN-US"}[过温保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_260655499}

[**[poe temperature-protection enable]{lang="EN-US"}**]{#struct_0_x6755_56834_x1322718736}

[**[undo poe temperature-protection enable]{lang="EN-US"}**]{#struct_0_x6755_56834_x604170984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_381874390}

[[设备的]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x1668768011}[过温保护功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x464937359}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1564454429}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x777694843}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_431609136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1178827649}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_719551242}

[[设备开启]{style="font-family:宋体"}[PoE]{lang="EN-US"}]{#struct_0_x6755_56834_x604236520}[过温保护功能后，系统会实时监控设备内部温度：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备内部温度超过上限阈值时，设备进行自我保护，自动关闭所有端口的]{style="font-family:宋体"}]{#struct_0_x6755_56834_x464659981}[PoE]{lang="EN-US"}[供电功能；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备内部温度低于下限阈值时，设备自动恢复所有端口的]{style="font-family:宋体"}]{#struct_0_x6755_56834_2046292305}[PoE]{lang="EN-US"}[供电功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1231900125}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x604695275}[关闭设备]{style="font-family:宋体"}[PoE]{lang="EN-US"}[过温保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x78366547}

[\[Sysname\] undo poe temperature-protection enable]{lang="EN-US"}
:::::

::::: {#-108888547 .myid}
[]{#_Toc404796842}[]{#struct_0_x6755_56834_x364344267}[]{#_Toc257634928}

**PoE \-- PoE配置命令 \-- poe update**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PoE命令.files/image001.png){#图片 18 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x6755_56834_742454101}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x6755_56834_x2138272173}
:::

[ ]{lang="EN-US"}

[**[poe update]{lang="EN-US"}**]{#struct_0_x6755_56834_x604760811}[命令用来在线升级]{style="font-family:宋体"}[PSE]{lang="EN-US"}[固件。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1954549373}

[[单]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_998295853}[设备：]{style="font-family:宋体"}

[**[poe update ]{lang="EN-US"}**[{ **full** \| **refresh** } *filename*]{lang="EN-US"}]{#struct_0_x6755_56834_x604564203}

[[多]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1517929390}[设备：]{style="font-family:宋体"}

[**[poe update ]{lang="EN-US"}**[{ **full** \| **refresh** } *filename* \[ **pse** *pse-id* \]]{lang="EN-US"}]{#struct_0_x6755_56834_1056257089}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x936250098}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_1560142312}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1239956705}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x1375786306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1381621753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1851200570}

[**[full]{lang="FR"}**]{#struct_0_x6755_56834_x604498667}[：用]{style="font-family:宋体"}[full]{lang="FR"}[模式升级]{style="font-family:宋体"}[PSE]{lang="FR"}[固件，一般用于]{style="font-family:宋体"}[PSE]{lang="FR"}[固件不可用时。]{style="font-family:宋体"}

[**[refresh]{lang="FR"}**]{#struct_0_x6755_56834_x604302059}[：用]{style="font-family:宋体"}[refresh]{lang="FR"}[模式升级]{style="font-family:宋体"}[PSE]{lang="FR"}[固件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[filename]{lang="FR"}*]{#struct_0_x6755_56834_x1600452635}[：]{style="font-family:宋体"}[升级文件的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[64]{lang="FR"}[个字符。该文件必须在设备文件系统的根目录下。升级文件的扩展名与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pse]{lang="EN-US"}***[ pse-id]{lang="EN-US"}*]{#struct_0_x6755_56834_x604367595}[：]{style="font-family:宋体"}[PSE]{lang="EN-US"}[编号，不指定该参数，表示升级所有]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的固件。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604170987}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[full]{lang="EN-US"}]{#struct_0_x6755_56834_382070998}[模式的升级方式是在用]{style="font-family:宋体"}[refresh]{lang="EN-US"}[模式升级出现异常的情况下使用的，其它情况下，请勿用]{style="font-family:宋体"}[full]{lang="EN-US"}[模式进行升级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x604236523}[固件固件损坏的情况下（表现为所有的]{style="font-family:宋体"}[PoE]{lang="EN-US"}[命令执行不成功）可以用]{style="font-family:宋体"}[full]{lang="EN-US"}[模式进行升级，使固件恢复。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x464463373}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x604695274}[在线升级]{style="font-family:宋体"}[PSE]{lang="EN-US"}[固件。（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x78432083}

[\[Sysname\] poe update refresh 0400_001.S19]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_x604760810}[在线升级]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[固件。（多]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x604564202}

[\[Sysname\] poe update refresh 0400_001.S19 pse 7]{lang="EN-US"}
:::::

::: {#-1688573535 .myid}
[]{#_Toc404796843}[]{#struct_0_x6755_56834_1517994926}[]{#_Toc257634932}

**PoE \-- PoE配置命令 \-- poe-profile**

------------------------------------------------------------------------

[**[poe-profile]{lang="FR"}**]{#struct_0_x6755_56834_x949758357}[命令用来创建]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[，]{style="font-family:宋体"}[并进入]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}[ ]{lang="EN-US"}[视图。]{style="font-family:
宋体"}

[**[undo poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_x243812794}[命令用来删除指定的]{style="font-family:宋体"}[PoE profile ]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_973023395}

[**[poe-profile]{lang="EN-US"}**[ *profile-name* \[ *index* \]]{lang="EN-US"}]{#struct_0_x6755_56834_x928209020}

[**[undo poe-profile ]{lang="EN-US"}**[{ **index** *index* \| **name** *profile-name* }]{lang="EN-US"}]{#struct_0_x6755_56834_x350545369}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1046326117}

[[没有创建]{style="font-family:宋体"}[PoE profile]{lang="EN-US"}]{#struct_0_x6755_56834_x604629738}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1077873429}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_x846288740}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x247089792}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x83220012}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x713760273}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_770626240}

[*[profile-name]{lang="FR"}*]{#struct_0_x6755_56834_x794353429}[：]{style="font-family:宋体"}[PoE profile ]{lang="FR"}[的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[15]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，区分大小写。]{style="font-family:宋体"}[以英文字母]{style="font-family:宋体"}[\[a-z,A-Z\]]{lang="FR"}[开始]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并且不能为保留关键字]{style="font-family:宋体"}**[undo]{lang="FR"}**[、]{style="font-family:宋体"}**[all]{lang="FR"}**[、]{style="font-family:宋体"}**[name]{lang="FR"}**[、]{style="font-family:宋体"}**[interface]{lang="FR"}**[、]{style="font-family:宋体"}**[user]{lang="FR"}**[、]{style="font-family:宋体"}**[poe]{lang="FR"}**[、]{style="font-family:宋体"}**[disable]{lang="FR"}**[、]{style="font-family:宋体"}**[max-power]{lang="FR"}**[、]{style="font-family:宋体"}**[mode]{lang="FR"}**[、]{style="font-family:宋体"}**[priority]{lang="FR"}**[和]{style="font-family:宋体"}**[enable]{lang="FR"}**[等。]{style="font-family:宋体"}

[*[index]{lang="FR"}*]{#struct_0_x6755_56834_69781520}[：]{style="font-family:宋体"}[PoE profile ]{lang="FR"}[的索引]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[100]{lang="FR"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604433130}

[[批量配置]{style="font-family:宋体"}]{#struct_0_x6755_56834_x604302058}[PoE]{lang="FR"}[接口时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[一般采用]{style="font-family:宋体"}[PoE Profile]{lang="FR"}[配置。如果不指定索引值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[系统会为此]{style="font-family:宋体"}[PoE profile ]{lang="FR"}[自动分配索引]{style="font-family:宋体"}[，]{style="font-family:宋体"}[从]{style="font-family:宋体"}[1]{lang="FR"}[开始。]{style="font-family:
宋体"}

[[如果]{style="font-family:宋体"}]{#struct_0_x6755_56834_x1600387099}[PoE profile]{lang="FR"}[已经应用]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不允许删除该]{style="font-family:宋体"}[PoE profile]{lang="FR"}[。必须先执行]{style="font-family:宋体"}**[undo apply poe-profile]{lang="FR"}**[，]{style="font-family:宋体"}[取消]{style="font-family:宋体"}[PoE profile ]{lang="FR"}[在指定]{style="font-family:宋体"}[PoE]{lang="FR"}[接口的应用后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[才能删除该]{style="font-family:宋体"}[PoE profile ]{lang="FR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1157085750}

[[\# ]{lang="FR"}]{#struct_0_x6755_56834_1603919373}[创建名称为]{style="font-family:宋体"}[abc]{lang="FR"}[的]{style="font-family:宋体"}[PoE profile]{lang="FR"}[，指定索引为]{style="font-family:宋体"}[3]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_440155194}

[\[Sysname\] poe-profile abc 3]{lang="FR"}

[\[Sysname-poe-profile-abc-3\]]{lang="FR"}

[[\#]{lang="FR"}]{#struct_0_x6755_56834_x1178369111}[创建名称为]{style="font-family:宋体"}[def]{lang="FR"}[的]{style="font-family:宋体"}[PoE profile]{lang="FR"}[，不指定索引]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x6755_56834_x604367594}

[\[Sysname\] poe-profile def]{lang="FR"}

[\[Sysname-poe-profile-def-1\]]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2019799320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply poe-profile]{lang="EN-US"}**]{#struct_0_x6755_56834_x1728311926}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe enable]{lang="EN-US"}**]{#struct_0_x6755_56834_1784273878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe priority]{lang="EN-US"}**]{#struct_0_x6755_56834_1925317403}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe max-power]{lang="EN-US"}**]{#struct_0_x6755_56834_x1184645272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[poe mode]{lang="EN-US"}**]{#struct_0_x6755_56834_1667685862}
:::

::: {#-1081202798 .myid}
[]{#_Toc404796844}[]{#struct_0_x6755_56834_x604170986}[]{#_Toc291754523}[]{#_Toc257634929}

**PoE \-- PoE配置命令 \-- poe utilization-threshold**

------------------------------------------------------------------------

[**[poe utilization-threshold]{lang="FR"}**]{#struct_0_x6755_56834_382005462}[命令用来配置]{style="font-family:宋体"}[PSE]{lang="FR"}[的功率告警阈值。]{style="font-family:宋体"}

[**[undo poe utilization-threshold]{lang="FR"}**]{#struct_0_x6755_56834_486693104}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1658736105}

[[单]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_1616394109}[设备：]{style="font-family:宋体"}

[**[poe utilization-threshold ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x6755_56834_x604236522}

[**[undo poe utilization-threshold]{lang="EN-US"}**]{#struct_0_x6755_56834_x464528909}

[[多]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x693142451}[设备：]{style="font-family:宋体"}

[**[poe utilization-threshold ]{lang="EN-US"}***[value]{lang="EN-US"}*[ **pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_x748209050}

[**[undo poe utilization-threshold]{lang="EN-US"}**[ **pse** *pse-id*]{lang="EN-US"}]{#struct_0_x6755_56834_x1556534757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x6755_56834_1921218692}

[[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_217962737}[的功率告警阈值为]{style="font-family:宋体"}[80%]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x6755_56834_691564498}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x6755_56834_815839454}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x604695277}

[[network-admin]{lang="EN-US"}]{#struct_0_x6755_56834_x78497619}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x6755_56834_1094528651}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x424955089}

[*[value]{lang="FR"}*]{#struct_0_x6755_56834_x168254476}[：]{style="font-family:宋体"}[功率告警阈值]{style="font-family:宋体"}[,]{lang="FR"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[99]{lang="FR"}[，]{style="font-family:
宋体"}[单位为百分比。]{style="font-family:宋体"}

[**[pse]{lang="FR"}**]{#struct_0_x6755_56834_1344992007}*[ pse-id]{lang="FR"}*[：]{style="font-family:宋体"}[PSE]{lang="FR"}[编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x2111874695}

[[当]{style="font-family:宋体"}[PSE]{lang="EN-US"}]{#struct_0_x6755_56834_x1957523879}[的功率使用百分比首次超过或者低于设置的告警阈值时，系统将生成告警信息，发送给设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x6755_56834_x604760813}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x6755_56834_x1954680445}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_1760498582}[配置]{style="font-family:宋体"}[PSE]{lang="EN-US"}[的功率告警阈值为]{style="font-family:宋体"}[90%]{lang="EN-US"}[。（单]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x801853833}

[\[Sysname\] poe utilization-threshold 90]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x6755_56834_768638284}[配置]{style="font-family:宋体"}[PSE 7]{lang="EN-US"}[的功率告警阈值为]{style="font-family:宋体"}[90%]{lang="EN-US"}[。（多]{style="font-family:宋体"}[PSE]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x6755_56834_x604564205}

[\[Sysname\] poe utilization-threshold 90 pse 7]{lang="EN-US"}
:::
