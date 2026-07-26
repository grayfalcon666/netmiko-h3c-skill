::: {#-313423029 .myid}
[]{#_Toc361834728}[]{#_Toc361319128}[]{#_Toc361230552}[]{#_Toc361164421}[]{#_Toc360546793}[]{#_Toc359856175}[]{#_Toc359586004}[]{#_Toc359420149}[]{#_Toc357603287}[]{#_Toc357095105}[]{#_Toc356916779}[]{#_Toc356835031}[]{#_Toc404794121}[]{#struct_0_14212_10009_233884139}[]{#_Toc361834734}[]{#_Toc361319134}[]{#_Toc361230558}[]{#_Toc361164427}[]{#_Toc361068250}

**MACsec \-- MACsec配置命令 \-- confidentiality-offset**

------------------------------------------------------------------------

[**[confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_758027008}[命令用来配置]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量。]{style="font-family:宋体"}

[**[undo confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_1521180081}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x562547784}

[**[confidentiality-offset]{lang="EN-US"}**[ *offset-value*]{lang="EN-US"}]{#struct_0_14212_10009_x2027335319}

[**[undo confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_1112670261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_1188103389}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1867578704}[加密偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示整个数据帧都要加密。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_141541941}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_183645405}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x553958874}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x420177982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_1264290866}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_1746818064}

[*[offset-value]{lang="EN-US"}*]{#struct_0_14212_10009_x594614357}[：]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量，取值包括]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[和]{style="font-family:宋体"}[50]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_x961546025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1136075579}[加密偏移量，表示从用户数据帧帧头开始偏移多少字节后开始加密。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x16120213}[加密偏移量最终以密钥服务器发布的加密偏移量为准。如果本端不是密钥服务器，则应用密钥服务器发布的加密偏移量；如果本端是密钥服务器，则应用本端配置的加密偏移量。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_14212_10009_1112604725}[MKA]{lang="EN-US"}[策略中配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量，在该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略成功应用到接口上之后，将会覆盖该接口上配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_803788621}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_497960567}[在]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[abcd]{lang="EN-US"}[中配置]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量为]{style="font-family:宋体"}[30]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_1600159386}

[\[Sysname\] mka policy abcd]{lang="EN-US"}

[\[Sysname-mka-policy-abcd\] confidentiality-offset 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x220447435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_x178090818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1685585510}
:::

::: {#-1191241757 .myid}
[]{#_Toc404794122}[]{#struct_0_14212_10009_x2043180349}[]{#_Toc361834743}[]{#_Toc361319143}[]{#_Toc361230567}[]{#_Toc361164436}[]{#_Toc360546804}[]{#_Toc359856184}[]{#_Toc359586013}[]{#_Toc359420162}[]{#_Toc357603300}

**MACsec \-- MACsec配置命令 \-- display macsec**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **macsec**]{lang="EN-US"}]{#struct_0_14212_10009_258458778}[命令用来显示接口的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_51366108}

[**[display]{lang="EN-US"}[ macsec ]{lang="EN-US"}**[\[]{lang="EN-US" style="color:black"}**[ interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ [\] \[ ]{style="color:black"}**verbose** [\]]{style="color:black"}]{lang="EN-US"}]{#struct_0_14212_10009_x658701088}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_1112145968}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1214407385}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_1541765444}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1170020961}

[[network-operator]{lang="EN-US"}]{#struct_0_14212_10009_825398859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x135273328}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14212_10009_x1946593654}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_x927996645}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14212_10009_x1245046653}[：显示接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行的摘要信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示指定接口类型和接口编号。不指定该参数，则表示显示所有接口上的]{style="font-family:
宋体"}[MACsec]{lang="EN-US"}[运行信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14212_10009_86323055}[：显示接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行的详细信息。若不指定该参数，则表示显示]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1142996769}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1687586575}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行的]{style="font-family:宋体"}[摘要]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display macsec interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14212_10009_1112080432}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[  Protect frames         : Yes]{lang="EN-US"}

[  Active MKA policy      : PL01]{lang="EN-US"}

[  Replay protection      : Enabled]{lang="EN-US"}

[  Replay window size     : 0 frames]{lang="EN-US"}

[  Confidentiality offset : 0 bytes]{lang="EN-US"}

[  Validation mode        : Check]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_34407718}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[运行的]{style="font-family:宋体"}[详细]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display macsec interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_14212_10009_x321476491}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[  Protect frames         : Yes]{lang="EN-US"}

[  Active MKA policy      : PL01]{lang="EN-US"}

[  Replay protection      : Enabled]{lang="EN-US"}

[  Replay window size     : 0 frames]{lang="EN-US"}

[  Confidentiality offset : 0 bytes]{lang="EN-US"}

[  Validation mode        : Check]{lang="EN-US"}

[  Included SCI           : No]{lang="EN-US"}

[  SCI conflict           : No]{lang="EN-US"}

[  Cipher suite           : GCM-AES-128]{lang="EN-US"}

[  Transmit secure channel:]{lang="EN-US"}

[    SCI           : 000C29F6A4380004]{lang="EN-US"}

[      Elapsed time: 00h:02m:19s]{lang="EN-US"}

[      Current SA  : AN 0        PN 1]{lang="EN-US"}

[  Receive secure channels:]{lang="EN-US"}

[    SCI           : 000C29258D430124]{lang="EN-US"}

[      Elapsed time: 00h:02m:17s]{lang="EN-US"}

[      Current SA  : AN 0        LPN 1]{lang="EN-US"}

[      Previous SA : AN N/A      LPN N/A]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display macsec]{lang="EN-US"}]{#struct_0_14212_10009_1969100841}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_990390862}[[字段]{style="font-family:黑体"}]{#struct_0_14212_10009_x1686875215}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14212_10009_x1978344135}

[[Interface ]{lang="EN-US"}]{#struct_0_14212_10009_x217938607}

[[使能了]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1414559706}[协议的接口名称]{style="font-family:宋体"}

[[Protect frames]{lang="EN-US"}]{#struct_0_14212_10009_1112014896}

[[接口上是否开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1606801288}[数据帧保护功能，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_14212_10009_x1353541756}[：需要进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[数据帧保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_14212_10009_1818632451}[：不进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[数据帧保护]{style="font-family:宋体"}

[[接口上不存在]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_730012584}[主要行动者时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Active MKA policy]{lang="EN-US"}]{#struct_0_14212_10009_x1675275960}

[[接口应用的且生效的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_2120813175}[策略。接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[数据帧保护功能时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}[；如果接口上开启了]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[数据帧保护功能但没有应用实际生效的策略，不显示该字段]{style="font-family:宋体"}

[[Replay protection]{lang="EN-US"}]{#struct_0_14212_10009_891651119}

[[接口的重播保护功能的开启状态，包括以下取值：]{style="font-family:宋体"}]{#struct_0_14212_10009_1458284997}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_14212_10009_x1466805538}[：处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14212_10009_591694855}[：处于关闭状态]{style="font-family:宋体"}

[[接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1111949360}[数据帧保护功能未开启时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Replay window size]{lang="EN-US"}]{#struct_0_14212_10009_1290089533}

[[接口的重播保护窗口大小，单位为数据帧。接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1641627451}[数据帧保护功能或接口上未开启重播保护功能时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Confidentiality offset]{lang="EN-US"}]{#struct_0_14212_10009_2020736137}

[[接口的加密偏移量，单位为字节。接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_341917195}[数据帧保护功能时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Validation mode]{lang="EN-US"}]{#struct_0_14212_10009_x876378130}

[[接口上的数据帧校验模式，包括以下取值：]{style="font-family:宋体"}]{#struct_0_14212_10009_x1106748087}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Check]{lang="EN-US"}]{#struct_0_14212_10009_x206887635}[：检查模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14212_10009_841764792}[：校验功能关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Strict]{lang="EN-US"}]{#struct_0_14212_10009_x309488887}[：严格校验模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14212_10009_1112408112}[：接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[数据帧保护功能]{style="font-family:宋体"}

[[Included SCI]{lang="EN-US"}]{#struct_0_14212_10009_x783701640}

[[数据帧的]{style="font-family:宋体"}[SecTAG]{lang="EN-US"}]{#struct_0_14212_10009_1238809003}[里是否携带]{style="font-family:宋体"}[SCI]{lang="EN-US"}[，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_14212_10009_x637713328}[：携带]{style="font-family:宋体"}[SCI]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_14212_10009_1641699150}[：未携带]{style="font-family:宋体"}[SCI]{lang="EN-US"}

[[接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x25076477}[数据帧保护功能时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[SCI conflict]{lang="EN-US"}]{#struct_0_14212_10009_x1090314177}

[[收到的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1206486370}[协议报文的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[和本端的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[是否相同，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_14212_10009_x313324391}[：收到的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[和本端的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[相同]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_14212_10009_1112342576}[：没有收到]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文或者收到的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[和本端的]{style="font-family:宋体"}[SCI]{lang="EN-US"}[不相同]{style="font-family:宋体"}

[[Cipher suite]{lang="EN-US"}]{#struct_0_14212_10009_1218649105}

[[保护数据帧的加密套件。接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1974220064}[数据帧保护功能时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Transmit secure channel]{lang="EN-US"}]{#struct_0_14212_10009_736834891}

[[发送数据帧的安全通道信息。接口上未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1121217266}[数据帧保护功能时，不显示安全通道信息]{style="font-family:宋体"}

[[Receive secure channels]{lang="EN-US"}]{#struct_0_14212_10009_1913183288}

[[接收数据帧的安全通道信息。接口上的未开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_2133698349}[数据帧保护功能时，不显示安全通道信息]{style="font-family:宋体"}

[[Elapsed time]{lang="EN-US"}]{#struct_0_14212_10009_x1069765192}

[[SC]{lang="EN-US"}]{#struct_0_14212_10009_1112277040}[存在的时间]{style="font-family:宋体"}

[[SCI]{lang="EN-US"}]{#struct_0_14212_10009_x760251898}

[[SCI]{lang="EN-US"}]{#struct_0_14212_10009_x844327627}[信息，由]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址和]{style="font-family:宋体"}[Port ID]{lang="EN-US"}[组成，为一个十六进制数]{style="font-family:宋体"}

[[Current SA]{lang="EN-US"}]{#struct_0_14212_10009_x460273176}

[[安全通道当前使用的]{style="font-family:宋体"}[SA ]{lang="EN-US"}]{#struct_0_14212_10009_259882604}

[[若无此信息，则对应的]{style="font-family:宋体"}[AN]{lang="EN-US"}]{#struct_0_14212_10009_1087910901}[、]{style="font-family:宋体"}[PN]{lang="EN-US"}[和]{style="font-family:宋体"}[LPN]{lang="EN-US"}[显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Previous SA]{lang="EN-US"}]{#struct_0_14212_10009_1112211504}

[[安全通道使用的前一个]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_14212_10009_x344485684}

[[若无此信息，则对应的]{style="font-family:宋体"}[AN]{lang="EN-US"}]{#struct_0_14212_10009_x158485627}[和]{style="font-family:宋体"}[LPN]{lang="EN-US"}[显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[PN]{lang="EN-US"}]{#struct_0_14212_10009_x538137724}

[[发送的报文编号]{style="font-family:宋体"}]{#struct_0_14212_10009_x1319992256}

[[AN]{lang="EN-US"}]{#struct_0_14212_10009_1112670256}

[[SA]{lang="EN-US"}]{#struct_0_14212_10009_1187775710}[编号]{style="font-family:宋体"}

[[LPN]{lang="EN-US"}]{#struct_0_14212_10009_649510425}

[[SAK]{lang="EN-US"}]{#struct_0_14212_10009_x1538323146}[可接收的最小报文编号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1528598327}

[]{#_Toc357095117}[]{#_Toc356916792}[]{#_Toc356835044}[]{#_Toc359420161}[]{#_Toc357603299}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[mka]{lang="EN-US"}[ apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_745854819}

::: {#2070473963 .myid}
[]{#_Toc404794123}[]{#struct_0_14212_10009_x284774455}[]{#_Toc361834744}[]{#_Toc361319144}[]{#_Toc361230568}[]{#_Toc361164437}[]{#_Toc360546805}[]{#_Toc359856185}[]{#_Toc359586014}

**MACsec \-- MACsec配置命令 \-- display mka policy**

------------------------------------------------------------------------

[**[display mka policy]{lang="EN-US"}**]{#struct_0_14212_10009_1190860662}[命令用来显示]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1112604720}

[**[display mka]{lang="EN-US"}**[ { **default-policy** \| **policy** \[ **name** *policy-name* \] }]{lang="EN-US"}]{#struct_0_14212_10009_803460941}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x599368032}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14212_10009_364806408}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_1842309359}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_1164729705}

[[network-operator]{lang="EN-US"}]{#struct_0_14212_10009_x263838930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x410354447}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14212_10009_2040505516}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_867293606}

[**[default-policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1052112034}[：表示显示默认的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1242009893}[：表示显示指定的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14212_10009_725896910}[：指定]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略名。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[16]{lang="EN-US"}[个任意字符的字符串，区分大小写[。若不指定该参数，]{style="color:black"}则表示显示所有当前已有的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1411071153}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1112145967}[显示所有]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display mka policy]{lang="EN-US"}]{#struct_0_14212_10009_1213555417}

[PolicyName          ReplayProtection   WindowSize    ConfOffset    Validation]{lang="EN-US"}

[default-policy      Yes                0             0             Check]{lang="EN-US"}

[policy1             Yes                0             30            Check]{lang="EN-US"}

[policy2             Yes                100           0             Disabled]{lang="EN-US"}

[policy3             No                 0             0             Strict]{lang="EN-US"}

[policy4             Yes                200           50            Check]{lang="EN-US"}

[policy5             Yes                0             0             Check]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display mka policy]{lang="EN-US"}]{#struct_0_14212_10009_2017944148}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1019620706}[[字段]{style="font-family:黑体"}]{#struct_0_14212_10009_x1970288189}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14212_10009_x669087247}

[[PolicyName]{lang="EN-US"}]{#struct_0_14212_10009_x1649323880}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_2076236568}[策略名]{style="font-family:宋体"}

[[ReplayProtection]{lang="EN-US"}]{#struct_0_14212_10009_x1290214432}

[[重播保护功能是否开启]{style="font-family:宋体"}]{#struct_0_14212_10009_x1886469038}

[[WindowSize]{lang="EN-US"}]{#struct_0_14212_10009_x566261605}

[[重播保护窗口大小，单位为数据帧]{style="font-family:宋体"}]{#struct_0_14212_10009_1112080431}

[[ConfOffset]{lang="EN-US"}]{#struct_0_14212_10009_34604326}

[[加密偏移量，单位为字节]{style="font-family:宋体"}]{#struct_0_14212_10009_x1787810553}

[[Validation]{lang="EN-US"}]{#struct_0_14212_10009_x100690844}

[[数据帧校验模式，包括以下取值：]{style="font-family:宋体"}]{#struct_0_14212_10009_1986982312}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Check]{lang="EN-US"}]{#struct_0_14212_10009_378178838}[：检查模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_14212_10009_x143603150}[：校验功能关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Strict]{lang="EN-US"}]{#struct_0_14212_10009_x1040671496}[：严格校验模式]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc353442650}[]{#_Toc345072405}[]{#_Toc345072234}[]{#_Toc257636547}[]{#_Toc173836550}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1593743358}

[]{#_Toc357603301}[]{#_Toc357095116}[]{#_Toc356916791}[]{#_Toc356835043}[]{#_Toc361164438}[]{#_Toc360546806}[]{#_Toc359856186}[]{#_Toc359586015}[]{#_Toc359420163}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka policy]{lang="EN-US"}**]{#struct_0_14212_10009_1559689845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_1016943879}

::: {#1808300597 .myid}
[]{#_Toc404794124}[]{#struct_0_14212_10009_427599408}[]{#_Toc361834745}[]{#_Toc361319146}[]{#_Toc361230569}

**MACsec \-- MACsec配置命令 \-- display mka session**

------------------------------------------------------------------------

[**[display mka session]{lang="EN-US"}**]{#struct_0_14212_10009_x899288801}[命令用来显示]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1112014895}

[**[display mka session ]{lang="EN-US"}**[\[ **interface**]{lang="EN-US"}*[ interface-type interface-number]{lang="EN-US"}*[ \| **local-sci** *sci-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_14212_10009_1606604680}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x992676325}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14212_10009_x840495205}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x570248323}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_1024941314}

[[network-operator]{lang="EN-US"}]{#struct_0_14212_10009_89106261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x428482715}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14212_10009_x1676285299}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_1603148075}

[**[interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_14212_10009_443205799}[：显示指定接口的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[的会话信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号]{style="font-family:
宋体"}[。若]{style="font-family:宋体;color:black"}[不指定该参数，则表示显示所有接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[**[local-sci]{lang="EN-US"}***[ sci-id]{lang="EN-US"}*]{#struct_0_14212_10009_1678746192}[：表示本地发送通道标识。]{style="font-family:宋体"}*[sci-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的十六进制数，不区分大小写。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_14212_10009_x1869352882}[：]{style="font-family:宋体"}[显示接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[的会话的详细信息。若不指定该参数，则表示显示]{style="font-family:宋体"}[MKA]{lang="EN-US"}[的会话的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x660662572}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1111949359}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display mka session interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14212_10009_1290679360}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[Tx-SCI    : 000C29F6A4380004]{lang="EN-US"}

[Priority  : 0]{lang="EN-US"}

[Capability: 3]{lang="EN-US"}

[  CKN for participant: ABCD]{lang="EN-US"}

[    Key server            : Yes]{lang="EN-US"}

[    MI (MN)               : D7B00EDA353242704CC6B0DB (7)]{lang="EN-US"}

[    Live peers            : 1]{lang="EN-US"}

[    Potential peers       : 0]{lang="EN-US"}

[    Principal actor       : Yes]{lang="EN-US"}

[    MKA session status    : Secured]{lang="EN-US"}

[    Confidentiality offset: 30 bytes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_2034843378}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display mka session interface gigabitethernet 1/0/1 verbose]{lang="EN-US"}]{#struct_0_14212_10009_1112408111}

[Interface GigabitEthernet1/0/1]{lang="EN-US"}

[Tx-SCI    : 000C29F6A4380004]{lang="EN-US"}

[Priority  : 0]{lang="EN-US"}

[Capability: 3]{lang="EN-US"}

[  CKN for participant: ABCD]{lang="EN-US"}

[    Key server            : Yes]{lang="EN-US"}

[    MI (MN)               : D7B00EDA353242704CC6B0DB (7)]{lang="EN-US"}

[    Live peers            : 1]{lang="EN-US"}

[    Potential peers       : 0]{lang="EN-US"}

[    Principal actor       : Yes]{lang="EN-US"}

[    MKA session status    : Secured]{lang="EN-US"}

[    Confidentiality offset: 30 bytes]{lang="EN-US"}

[    Current SAK status    : Rx & Tx]{lang="EN-US"}

[    Current SAK AN        : 0]{lang="EN-US"}

[    Current SAK KI (KN)   : 4273791304C1C26259C94C3400000001 (1)]{lang="EN-US"}

[    Previous SAK status   : N/A]{lang="EN-US"}

[    Previous SAK AN       : N/A]{lang="EN-US"}

[    Previous SAK KI (KN)  : N/A]{lang="EN-US"}

[    Live peer list:]{lang="EN-US"}

[    MI                        MN         Priority  Capability  Rx-SCI]{lang="EN-US"}

[    EA58DC3F8715953DBC6593F0  840        100       3           00E0020000000106]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Potential peer list:]{lang="EN-US"}

[    MI                        MN         Priority  Capability  Rx-SCI]{lang="EN-US"}

[    DA58DC3Q4573543DBC6699F0  3          200       3           00E0021200000107]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mka session ]{lang="EN-US"}]{#struct_0_14212_10009_x783505032}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1023260700}[[字段]{style="font-family:黑体"}]{#struct_0_14212_10009_x1112765486}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14212_10009_x627084768}

[[Interface ]{lang="EN-US"}]{#struct_0_14212_10009_1112342575}

[[接口名称]{style="font-family:宋体"}]{#struct_0_14212_10009_1218845713}

[[Tx-SCI]{lang="EN-US"}]{#struct_0_14212_10009_x1497996819}

[[发送]{style="font-family:宋体"}[SCI]{lang="EN-US"}]{#struct_0_14212_10009_753774800}[，采用十六进制格式]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_14212_10009_1930010535}

[[表示密钥服务器的优先级，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_14212_10009_x1956899556}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[[Capability]{lang="EN-US"}]{#struct_0_14212_10009_1810002049}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_91626483}[能力，取值如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_14212_10009_831037469}[：]{style="font-family:宋体"}[表示不支持]{lang="EN-US" style="font-family:宋体"}[MACsec]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1]{lang="EN-US"}]{#struct_0_14212_10009_1583608194}[：表示只支持完整性服务，不支持机密性服务]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2]{lang="EN-US"}]{#struct_0_14212_10009_1112277039}[：表示支持完整性服务，可选择支持机密性服务（加密偏移量只能为]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3]{lang="EN-US"}]{#struct_0_14212_10009_x759793153}[：表示支持完整性服务，可选择支持机密性服务（加密偏移量可支持]{style="font-family:宋体"}[0]{lang="EN-US"}[，]{style="font-family:宋体"}[30]{lang="EN-US"}[及]{style="font-family:宋体"}[50]{lang="EN-US"}[）]{style="font-family:宋体"}

[[CKN for participant]{lang="EN-US"}]{#struct_0_14212_10009_x183331619}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1664399653}[实例的]{style="font-family:宋体"}[CKN]{lang="EN-US"}

[[Key server]{lang="EN-US"}]{#struct_0_14212_10009_1452614580}

[[本端是否为密钥服务器]{style="font-family:宋体"}]{#struct_0_14212_10009_x577482133}

[[MI]{lang="EN-US"}]{#struct_0_14212_10009_x195892297}

[[成员标识，采用十六进制格式]{style="font-family:宋体"}]{#struct_0_14212_10009_x676250246}

[[MN]{lang="EN-US"}]{#struct_0_14212_10009_675742168}

[[消息序号]{style="font-family:宋体"}]{#struct_0_14212_10009_1112211503}

[[Live peers]{lang="EN-US"}]{#struct_0_14212_10009_x344682292}

[[已经学习到的对端的个数]{style="font-family:宋体"}]{#struct_0_14212_10009_1805592673}

[[Potential peers]{lang="EN-US"}]{#struct_0_14212_10009_1277639180}

[[正在协商中的对端的个数]{style="font-family:宋体"}]{#struct_0_14212_10009_229645146}

[[Principal actor]{lang="EN-US"}]{#struct_0_14212_10009_1999493139}

[[该]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x427754919}[实例是否为主要行动者。其中，]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例表示]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议在该接口上的运行实体，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例处于]{style="font-family:宋体"}[Active]{lang="EN-US"}[状态时，被称为主要行动者]{style="font-family:宋体"}

[[MKA session status]{lang="EN-US"}]{#struct_0_14212_10009_1112670255}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1187841246}[会话的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_14212_10009_1428876041}[：表示未知状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}[ending]{lang="EN-US"}]{#struct_0_14212_10009_x872265306}[：]{lang="EN-US" style="font-family:宋体"}[表示挂起状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[nauthenticate]{lang="EN-US"}]{#struct_0_14212_10009_x1313513554}[d]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示未认证状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="EN-US"}[uthenticated]{lang="EN-US"}]{#struct_0_14212_10009_x408092191}[：]{lang="EN-US" style="font-family:宋体"}[表示认证状态，接口已通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secured]{lang="EN-US"}]{#struct_0_14212_10009_1112604719}[：表示安全状态，会话将被保护]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_14212_10009_803002190}[：表示该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者]{style="font-family:宋体"}

[[Confidentiality offset]{lang="EN-US"}]{#struct_0_14212_10009_x1450853879}

[[密钥服务器发布的加密偏移量，明文通信或该]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x2054918470}[实例不是主要行动者时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Current SAK status ]{lang="EN-US"}]{#struct_0_14212_10009_x1818279443}

[[当前使用的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_x1506289315}[的状态（]{style="font-family:宋体"}[Tx]{lang="EN-US"}[表示用于发送，]{style="font-family:宋体"}[Rx]{lang="EN-US"}[表示用于接收），当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Current SAK AN]{lang="EN-US"}]{#struct_0_14212_10009_x1201863208}

[[当前使用的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_x352632410}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[编号，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Current SAK KI]{lang="EN-US"}]{#struct_0_14212_10009_708861445}

[[当前使用的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_675163949}[的密钥标识，由]{style="font-family:宋体"}[12]{lang="EN-US"}[字节的密钥服务器的]{style="font-family:宋体"}[MI]{lang="EN-US"}[和]{style="font-family:宋体"}[KN]{lang="EN-US"}[组成，采用十六进制格式，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[KN]{lang="EN-US"}]{#struct_0_14212_10009_1487877785}

[[SAK]{lang="EN-US"}]{#struct_0_14212_10009_x575679421}[编号，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Previous SAK status]{lang="EN-US"}]{#struct_0_14212_10009_x1578047157}

[[前一个]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_1398139279}[的状态（]{style="font-family:宋体"}[Tx]{lang="EN-US"}[表示用于发送，]{style="font-family:宋体"}[Rx]{lang="EN-US"}[表示用于接收），当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Previous SAK AN]{lang="EN-US"}]{#struct_0_14212_10009_883965726}

[[前一个]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_708795909}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[编号，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Previous SAK KI]{lang="EN-US"}]{#struct_0_14212_10009_1664167569}

[[前一个]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_x542014481}[的密钥标识，由]{style="font-family:宋体"}[12]{lang="EN-US"}[字节的密钥服务器的]{style="font-family:宋体"}[MI]{lang="EN-US"}[和]{style="font-family:宋体"}[KN]{lang="EN-US"}[组成，采用十六进制格式，当该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[实例不是主要行动者或]{style="font-family:宋体"}[SAK]{lang="EN-US"}[不存在时，显为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Live peer list]{lang="EN-US"}]{#struct_0_14212_10009_x139313675}

[[已经学习到的对端列表，当不存在]{style="font-family:宋体"}[Live peer]{lang="EN-US"}]{#struct_0_14212_10009_497243860}[时，不显示该字段]{style="font-family:宋体"}

[[Potential peer list]{lang="EN-US"}]{#struct_0_14212_10009_708730373}

[[正在协商过程中的对端列表，当不存在]{style="font-family:宋体"}[Potential peer]{lang="EN-US"}]{#struct_0_14212_10009_1673390319}[时，不显示该字段]{style="font-family:宋体"}

[[Rx-SCI ]{lang="EN-US"}]{#struct_0_14212_10009_2091398440}

[[接收]{style="font-family:宋体"}[SCI]{lang="EN-US"}]{#struct_0_14212_10009_x1338464595}[，采用十六进制格式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc353442649}[]{#_Toc345072404}[]{#_Toc345072233}[]{#_Toc257636546}[]{#_Toc124742951}[]{#_Toc101584103}[]{#struct_0_14212_10009_x535476068}[]{#_Toc137470881}[]{#_Toc137475416}[]{#_Toc137547115}[]{#_Toc137470883}[]{#_Toc137475418}[]{#_Toc137547117}[]{#_Toc124742952}[]{#_Toc124742953}[]{#_Toc124742954}[]{#_Toc124742955}[]{#_Toc124742956}[]{#_Toc124742957}[]{#_Toc124742958}[]{#_Toc124742959}[]{#_Toc124742960}[]{#_Toc124742961}[]{#_Toc124742962}[]{#_Toc124742963}[]{#_Toc124742964}[]{#_Toc124742965}[]{#_Toc124742966}[]{#_Toc124742968}[]{#_Toc124742969}[]{#_Toc124742971}[]{#_timer}[【相关命令】]{style="font-family:黑体"}

[]{#_Toc361834746}[]{#_Toc361319147}[]{#_Toc361230570}[]{#_Toc361164439}[]{#_Toc360546807}[]{#_Toc359856187}[]{#_Toc359586016}[]{#_Toc359420164}[]{#_Toc357603302}[]{#_Toc357095118}[]{#_Toc356916793}[]{#_Toc356835045}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset mka session]{lang="EN-US"}**]{#struct_0_14212_10009_143784290}

::: {#-1259127324 .myid}
[]{#_Toc404794125}[]{#struct_0_14212_10009_2137062729}

**MACsec \-- MACsec配置命令 \-- display mka statistics**

------------------------------------------------------------------------

[**[display mka statistics]{lang="EN-US"}**]{#struct_0_14212_10009_x473894446}[命令用来显示接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_708664837}

[**[display mka statistics ]{lang="EN-US"}**[\[ **interface** *i*]{lang="EN-US"}*[nterface-type interface-number ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_14212_10009_870103019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_1547255161}

[[任意视图]{style="font-family:宋体"}]{#struct_0_14212_10009_x1951144376}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_26415023}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_434326149}

[[network-operator]{lang="EN-US"}]{#struct_0_14212_10009_x1211063383}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_1871450474}

[[mdc-operator]{lang="EN-US"}]{#struct_0_14212_10009_424293504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_x578433099}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_14212_10009_x749963486}[：指定接口类型和接口编号[。若不指定该参数，则表示显示所有]{style="color:black"}接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1219075359}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_434791161}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mka statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14212_10009_709123589}

[Interface GigabitEthernet1/0/1 statistics]{lang="EN-US"}

[MKPDUs with invalid CKN : 0]{lang="EN-US"}

[MKPDUs with invalid ICV : 0]{lang="EN-US"}

[MKPDUs with Rx error    : 0]{lang="EN-US"}

[CKN for participant     : ABCD]{lang="EN-US"}

[  Tx MKPDUs             : 2379]{lang="EN-US"}

[  Rx MKPDUs             : 2375]{lang="EN-US"}

[  MKPDUs with invalid MN: 0]{lang="EN-US"}

[  MKPDUs with Tx error  : 0]{lang="EN-US"}

[  SAKs distributed      : 0]{lang="EN-US"}

[  SAKs received         : 5]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display mka statistics]{lang="EN-US"}]{#struct_0_14212_10009_x2136171331}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1017769180}[[字段]{style="font-family:黑体"}]{#struct_0_14212_10009_227959181}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_14212_10009_736408589}

[[Interface Gigabitethernet1/0/1 statistics ]{lang="EN-US"}]{#struct_0_14212_10009_x1999666860}

[[接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_26125017}[统计信息]{style="font-family:宋体"}

[[MKPDUs with invalid CKN]{lang="EN-US"}]{#struct_0_14212_10009_709058053}

[[收到的且找不到匹配]{style="font-family:宋体"}[CKN]{lang="EN-US"}]{#struct_0_14212_10009_571293319}[的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文个数]{style="font-family:宋体"}

[[MKPDUs with invalid ICV]{lang="EN-US"}]{#struct_0_14212_10009_x1174366913}

[[ICV]{lang="EN-US"}]{#struct_0_14212_10009_x2070306719}[校验失败的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文个数]{style="font-family:宋体"}

[[MKPDUs with Rx error]{lang="EN-US"}]{#struct_0_14212_10009_x1441322054}

[[接收到错误的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1176688922}[协议报文个数]{style="font-family:宋体"}

[[CKN for participant]{lang="EN-US"}]{#struct_0_14212_10009_940740587}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x1252816878}[实例的]{style="font-family:宋体"}[CKN ]{lang="EN-US"}

[[Tx MKPDUs]{lang="EN-US"}]{#struct_0_14212_10009_x545805539}

[[实例发送的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x1455901693}[协议报文个数]{style="font-family:宋体"}

[[Rx MKPDUs ]{lang="EN-US"}]{#struct_0_14212_10009_x1127826462}

[[实例接收的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_708992517}[协议报文个数]{style="font-family:宋体"}

[[MKPDUs with invalid MN]{lang="EN-US"}]{#struct_0_14212_10009_x1687378469}

[[实例接收到非法]{style="font-family:宋体"}[MN]{lang="EN-US"}]{#struct_0_14212_10009_x1110200444}[的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议报文个数]{style="font-family:宋体"}

[[MKPDUs with Tx error]{lang="EN-US"}]{#struct_0_14212_10009_1775948762}

[[实例发送错误的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x963277043}[协议报文个数]{style="font-family:宋体"}

[[SAKs distributed]{lang="EN-US"}]{#struct_0_14212_10009_1866944731}

[[实例分发的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_1416045840}[个数]{style="font-family:宋体"}

[[SAKs received]{lang="EN-US"}]{#struct_0_14212_10009_x647601414}

[[实例接收的]{style="font-family:宋体"}[SAK]{lang="EN-US"}]{#struct_0_14212_10009_2012972587}[个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_708926981}

[]{#struct_0_14212_10009_x509858452}[]{#_Toc350937957}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}**[reset mka statistics]{lang="EN-US"}**

::: {#-1167606329 .myid}
[]{#_Toc404794126}[]{#struct_0_14212_10009_738694842}[]{#_Toc361834729}[]{#_Toc361319129}[]{#_Toc361230553}[]{#_Toc361164422}[]{#_Toc360546794}[]{#_Toc359856176}[]{#_Toc359586005}[]{#_Toc359420150}[]{#_Toc357603288}[]{#_Toc357095109}[]{#_Toc356916783}[]{#_Toc356835035}

**MACsec \-- MACsec配置命令 \-- macsec confidentiality-offset**

------------------------------------------------------------------------

[**[macsec confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_x1421428225}[命令用来配置接口上的]{style="font-family:
宋体"}[MACsec]{lang="EN-US"}[加密偏移量。]{style="font-family:
宋体"}

[**[undo macsec confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_x1002609539}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1820537303}

[**[macsec confidentiality-offset ]{lang="EN-US"}***[offset-value]{lang="EN-US"}*]{#struct_0_14212_10009_x462533778}

[**[undo macsec confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_137068281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_x827974150}

[[接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_881209166}[加密偏移量为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示整个数据帧都要加密。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1566856683}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_709385733}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_67810503}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_414344912}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_466569416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_x532409860}

[*[offset-value]{lang="EN-US"}*]{#struct_0_14212_10009_641667797}[：数据帧的加密偏移量，取值包括]{style="font-family:宋体"}[0]{lang="EN-US"}[、]{style="font-family:宋体"}[30]{lang="EN-US"}[和]{style="font-family:宋体"}[50]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_522935056}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1898044667}[加密偏移量，表示从用户数据帧帧头开始偏移多少字节后开始加密。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果首先在接口上通过]{style="font-family:宋体"}]{#struct_0_14212_10009_694088016}**[mka apply policy]{lang="EN-US"}**[命令应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，然后在该接口上配置加密偏移量，则]{style="font-family:宋体"}[接口上应用的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略将被取消，取而代之保存的配置将是，接口上配置的加密偏移量以及该]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略中]{lang="EN-US" style="font-family:宋体"}[的除]{style="font-family:宋体"}[加密偏移量之外的]{lang="EN-US" style="font-family:宋体"}[其它所有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本端不是密钥服务器，则应用密钥服务器发布的加密偏移量；如果本端是密钥服务器，则应用本端配置的加密偏移量，并将该值发布给对端。]{style="font-family:宋体"}]{#struct_0_14212_10009_1534666583}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1824773206}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_908342960}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[加密偏移量为]{style="font-family:宋体"}[30]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_709320197}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] macsec confidentiality-offset 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_2059455055}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confidentiality-offset ]{lang="EN-US"}**]{#struct_0_14212_10009_1609421322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display macsec]{lang="EN-US"}**]{#struct_0_14212_10009_1988532226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka session]{lang="EN-US"}**]{#struct_0_14212_10009_x2137748073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x2111941982}
:::

::: {#-383988886 .myid}
[]{#_Toc404794127}[]{#struct_0_14212_10009_x1742807718}

**MACsec \-- MACsec配置命令 \-- macsec desire**

------------------------------------------------------------------------

[**[macsec desire]{lang="EN-US"}**]{#struct_0_14212_10009_1533160911}[命令用来启用]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护，即接口期望对发送的数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护。]{style="font-family:宋体"}

[**[undo macsec desire]{lang="EN-US"}**]{#struct_0_14212_10009_1472730362}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1686621012}

[**[macsec desire]{lang="EN-US"}**]{#struct_0_14212_10009_1478214691}

[**[undo]{lang="EN-US"}**[ **macsec desire**]{lang="EN-US"}]{#struct_0_14212_10009_x2090858580}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_708861444}

[[接口上不需要对发送的数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_675163950}[保护。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x850774366}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_315105342}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_392740540}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_687001105}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_1978376932}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_364769487}

[**[macsec desire]{lang="EN-US"}**]{#struct_0_14212_10009_x765499088}[命令仅用来告知对端，本端发送的数据帧需要进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护，但最终本端发送的数据帧是否启用]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护，要由密钥服务器来决策。决策策略是：密钥服务器和它的对端支持]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[功能，且它们至少有一个请求]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1672212750}

[]{#_Toc353442637}[]{#_Toc345072393}[]{#_Toc345072222}[]{#_Toc257636535}[]{#_Toc124742944}[]{#_Toc101584096}[]{#struct_0_14212_10009_x1426776445}[]{#_Toc350937938}[]{#_display_rrpp_brief}[\# ]{lang="EN-US"}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[期望对发送的数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[保护。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_708795908}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] macsec desire]{lang="EN-US"}
:::

::: {#-1770238915 .myid}
[]{#_Toc124742947}[]{#_Toc101584099}[]{#_Toc404794128}[]{#struct_0_14212_10009_1664167568}[]{#_Toc361834730}[]{#_Toc361319130}[]{#_Toc361230554}[]{#_Toc361164423}[]{#_Toc360546795}[]{#_Toc359856177}[]{#_Toc359586006}[]{#_Toc359420151}[]{#_Toc357603289}[]{#_Toc357095110}[]{#_Toc356916784}[]{#_Toc356835036}[]{#_Toc376250730}[]{#_Toc376250731}[]{#_Toc350937941}[]{#_Toc350937942}[]{#_Toc350937943}

**MACsec \-- MACsec配置命令 \-- macsec replay-protection enable**

------------------------------------------------------------------------

[**[macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x541948945}[命令用来开启接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[**[undo macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x29182330}[命令用来关闭接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1892824872}

[**[macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_1026433893}

[**[undo macsec]{lang="EN-US"}**[ **replay-protection enable**]{lang="EN-US"}]{#struct_0_14212_10009_x1963486924}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_x469268523}

[[接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1347320776}[重播保护功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_929317880}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_x1964060226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x974794069}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1217866484}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_708730372}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_1673390318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_2091332904}[重播保护功能可以单独开启，且仅针对接收到的数据帧。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重播保护功能可以防止本端收到乱序或重复的数据帧。]{style="font-family:宋体"}]{#struct_0_14212_10009_x940154285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果首先在接口上通过]{style="font-family:宋体"}]{#struct_0_14212_10009_757743191}**[mka apply policy]{lang="EN-US"}**[命令应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，然后在该接口上使能]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[接口上应用的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略将被取消，取而代之保存的配置将是，接口上已开启]{lang="EN-US" style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能以及该]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略中]{lang="EN-US" style="font-family:宋体"}[的除]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能之外的]{lang="EN-US" style="font-family:宋体"}[其它所有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1759421954}

[]{#_Toc173836544}[]{#_Toc356835037}[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x1800949778}[开启接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_1564298680}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] macsec replay-protection enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1347571923}

[]{#_Toc360546796}[]{#_Toc359856178}[]{#_Toc359586007}[]{#_Toc359420152}[]{#_Toc357603290}[]{#_Toc357095111}[]{#_Toc356916785}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display macsec]{lang="EN-US"}**]{#struct_0_14212_10009_1025390970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_899429378}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec ]{lang="EN-US"}[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_x1313401681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_1930373668}
:::

::: {#-349464456 .myid}
[]{#_Toc404794129}[]{#struct_0_14212_10009_x1951954473}[]{#_Toc361834731}[]{#_Toc361319131}[]{#_Toc361230555}[]{#_Toc361164424}

**MACsec \-- MACsec配置命令 \-- macsec replay-protection window-size**

------------------------------------------------------------------------

[**[macsec replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_1998684960}[命令用来配置接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **macsec replay-protection window-size**]{lang="EN-US"}]{#struct_0_14212_10009_708664836}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_870103020}

[**[macsec replay-protection window-size ]{lang="EN-US"}***[size-value]{lang="EN-US"}*]{#struct_0_14212_10009_x26722958}

[**[undo macsec]{lang="EN-US"}**[ **replay-protection window-size**]{lang="EN-US"}]{#struct_0_14212_10009_x677318563}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_1903975775}

[[接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x405313075}[重播保护窗口大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[个数据帧，表示不允许接收乱序或重复的数据帧。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_2053012589}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_x1493618862}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_2035941675}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_204903087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1695598756}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1867919290}

[*[size-value]{lang="EN-US"}*]{#struct_0_14212_10009_x618892490}[：重播保护窗口大小，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为数据帧。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_x212997645}

[[在某些组网下（如数据帧经过运营商网络转发），因为用户数据帧的发送优先级不同，在转发过程中会被重新排序，最终到达接收端会出现乱序。如果要正常接收这些乱序的数据帧，需要开启重播保护功能，且配置重播保护窗口。假设配置的重播保护窗口大小为]{style="font-family:宋体"}[a]{lang="EN-US"}]{#struct_0_14212_10009_x1083881575}[，如果接收到了一个报文序号（]{style="font-family:宋体"}[PN]{lang="EN-US"}[，]{style="font-family:宋体"}[Packet Number]{lang="EN-US"}[）为]{style="font-family:宋体"}[x]{lang="EN-US"}[的报文，则下一个允许被接收的报文的]{style="font-family:宋体"}[PN]{lang="EN-US"}[必须大于或等于]{style="font-family:宋体"}[x-a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该功能仅在重播保护功能开启的情况下有效。]{style="font-family:宋体"}]{#struct_0_14212_10009_876451592}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请结合数据帧在传输网络中的转发途径，选择适当的重播保护窗口大小。若数据帧有可能被多次转发，那么乱序的可能性和乱序的范围会比较大，则建议适当调大重播保护窗口，反之调小。]{style="font-family:宋体"}]{#struct_0_14212_10009_68662296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果首先在接口上通过]{style="font-family:宋体"}]{#struct_0_14212_10009_709123588}**[mka apply policy]{lang="EN-US"}**[命令应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，然后在该接口上配置了]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[接口上应用的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略将被取消，取而代之保存的配置将是，接口上配置的]{lang="EN-US" style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小以及该]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略中]{lang="EN-US" style="font-family:宋体"}[的除]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小之外的]{lang="EN-US" style="font-family:宋体"}[其它所有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x2136171330}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x1338124760}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x1501313445}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] macsec replay-protection window-size 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_966344873}

[]{#_Toc345072407}[]{#_Toc345072236}[]{#_Toc345062691}[]{#_Toc257636549}[]{#_Toc211322925}[]{#_Toc209515198}[]{#_Toc356835038}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[display macsec]{lang="EN-US"}**]{#struct_0_14212_10009_1219087386}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x738100808}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1525489137}[]{#_Toc361834732}[]{#_Toc361319132}[]{#_Toc361230556}[]{#_Toc361164425}[]{#_Toc360546797}[]{#_Toc359856179}[]{#_Toc359586008}[]{#_Toc359420153}[]{#_Toc357603291}[]{#_Toc357095112}[]{#_Toc356916786}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_x2130961339}
:::

::: {#1144097536 .myid}
[]{#_Toc404794130}[]{#struct_0_14212_10009_x1973778940}

**MACsec \-- MACsec配置命令 \-- macsec validation mode**

------------------------------------------------------------------------

[**[macsec validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_438560756}[命令用来配置接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[[ **undo macsec validation mode**]{lang="EN-US"}]{#struct_0_14212_10009_995410180}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_709058052}

[**[macsec validation mode ]{lang="EN-US"}**[{ **check** \| **disabled** \| **strict** }]{lang="EN-US"}]{#struct_0_14212_10009_571293318}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[macsec validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_x1174366912}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_658576636}

[[接口上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_2049393177}[校验模式为]{style="font-family:宋体"}**[check]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_283361812}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_46312882}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_1582803349}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_1773994450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x868415922}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_843475021}

[**[check]{lang="EN-US"}**]{#struct_0_14212_10009_351612576}[：]{style="font-family:宋体;color:black"}[检查模式，表示[只作校验，但不丢弃非法数据帧]{style="color:black"}。]{style="font-family:宋体"}

[[[disabled]{lang="EN-US"}]{.commandkeywords}]{#struct_0_14212_10009_708992516}[：]{style="font-family:宋体;color:black"}[不对接收数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_14212_10009_x1687378470}[：]{style="font-family:宋体;color:black"}[严格校验模式，表示校验数据帧，并丢弃非法数据帧。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_99587601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在网络中部署支持]{style="font-family:宋体"}]{#struct_0_14212_10009_x754772421}[MACsec]{lang="EN-US"}[的设备时，为避免两端因密钥协商不一致而造成流量丢失，建议两端均先配置为]{style="font-family:宋体"}**[check]{lang="EN-US"}**[模式，在密钥协商成功后，再配置为]{style="font-family:宋体"}**[strict]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果首先在接口上通过]{style="font-family:宋体"}]{#struct_0_14212_10009_x324007565}**[mka apply policy]{lang="EN-US"}**[命令应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，然后在该接口上配置]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式]{lang="EN-US" style="font-family:宋体"}[，则]{style="font-family:宋体"}[接口上应用的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略将被取消，取而代之保存的配置将是，接口上配置的]{lang="EN-US" style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式及该]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略中]{lang="EN-US" style="font-family:宋体"}[的除]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式之外的]{lang="EN-US" style="font-family:宋体"}[其它所有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x269972521}

[]{#_Toc353442644}[]{#_Toc345072399}[]{#_Toc345072228}[]{#_Toc257636541}[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x1296561443}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1 ]{lang="EN-US"}[上的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[的校验模式为严格校验模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_1126765108}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] macsec validation mode strict]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1792092754}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display macsec]{lang="EN-US"}**]{#struct_0_14212_10009_x1492089856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_708926980}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_x509858451}
:::

::: {#-319518573 .myid}
[]{#_Toc361834733}[]{#_Toc361319133}[]{#_Toc361230557}[]{#_Toc361164426}[]{#_Toc360546798}[]{#_Toc404794131}[]{#struct_0_14212_10009_738498234}[]{#_Toc361834738}[]{#_Toc361319138}[]{#_Toc361230562}[]{#_Toc361164431}[]{#_Toc360546799}

**MACsec \-- MACsec配置命令 \-- mka apply policy**

------------------------------------------------------------------------

[**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1330088549}[命令用来在接口上应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1965438874}[命令用来取消接口上应用的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_2144307517}

[**[mka apply policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14212_10009_1559687082}

[**[undo mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x61999975}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_1698759481}

[[接口上没有应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_442842848}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x127744975}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1700998926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x6830180}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x2006007471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_709385732}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_67810504}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14212_10009_1605986000}[：]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个任意字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_1485114360}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口上应用了]{style="font-family:宋体"}]{#struct_0_14212_10009_x884848191}[MKA]{lang="EN-US"}[策略时，策略下配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[参数，包括加密偏移、校验模式、重播保护功能和重播保护窗口值会覆盖接口下配置的对应的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[参数，且当修改策略下的配置时，接口相应的配置也会改变。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}**[undo ]{lang="EN-US"}**]{#struct_0_14212_10009_720609437}**[mka apply policy]{lang="EN-US"}**[取消接口上应用的指定]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{lang="EN-US" style="font-family:宋体"}[时，接口上的加密偏移、]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式、重播保护功能和重播保护窗口大小都恢复为缺省情况。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当一个]{style="font-family:宋体"}]{#struct_0_14212_10009_848485585}[MKA]{lang="EN-US"}[策略被删除时，应用了该策略的接口上会自动应用缺省]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[default-policy]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口应用了一个不存在的]{style="font-family:宋体"}]{#struct_0_14212_10009_1496701199}[MKA]{lang="EN-US"}[策略时，该接口会自动应用缺省]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[default-policy]{lang="EN-US"}[。之后，如果该策略被创建后，则接口会自动应用配置的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x854137942}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_113754565}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上应用]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[abcd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Syaname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x64565906}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mka apply policy abcd]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1420940540}

[]{#_Toc360546800}[]{#_Toc359856180}[]{#_Toc359586009}[]{#_Toc359420154}[]{#_Toc357603292}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_x1046504662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka policy]{lang="EN-US"}**]{#struct_0_14212_10009_724731917}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_1079984997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_x698939819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_709320196}
:::

::: {#1826065647 .myid}
[]{#_Toc404794132}[]{#struct_0_14212_10009_2059455056}[]{#_Toc361834739}[]{#_Toc361319139}[]{#_Toc361230563}[]{#_Toc361164432}[]{#_Toc372548018}[]{#_Toc372615760}[]{#_Toc372615792}

**MACsec \-- MACsec配置命令 \-- mka enable**

------------------------------------------------------------------------

[**[mka enable]{lang="EN-US"}**]{#struct_0_14212_10009_1609486858}[命令用来使能接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[undo mka enable]{lang="EN-US"}**]{#struct_0_14212_10009_x415167336}[命令用来关闭接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1725086028}

[**[mka enable]{lang="EN-US"}**]{#struct_0_14212_10009_x480298959}

[**[undo mka enable]{lang="EN-US"}**]{#struct_0_14212_10009_x2137350293}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_978475679}

[[接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1481211493}[协议处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_174713926}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_x1762566865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1099919596}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_1278546446}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_708861447}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_675163951}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口使能]{style="font-family:宋体"}]{#struct_0_14212_10009_x850774367}[MKA]{lang="EN-US"}[协议后，将触发密钥协商过程，并在密钥协商成功之后建立]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_315170878}[协议负责接口上]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[安全通道的建立和管理，以及]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[所使用密钥的协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1599815294}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x974408146}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x1579655765}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mka enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x2147231075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka session]{lang="EN-US"}**]{#struct_0_14212_10009_x1293675535}
:::

::: {#-161187474 .myid}
[]{#_Toc404794133}[]{#struct_0_14212_10009_2056547809}

**MACsec \-- MACsec配置命令 \-- mka policy**

------------------------------------------------------------------------

[**[mka policy]{lang="EN-US"}**]{#struct_0_14212_10009_708795911}[命令用来创建一个]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，并进入]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略视图。如果该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略已创建，则直接进入]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo mka policy]{lang="EN-US"}**]{#struct_0_14212_10009_x674484583}[命令用来删除指定的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1129305330}

[**[mka policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14212_10009_x405154251}

[**[undo mka policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_14212_10009_x1091714232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_794289043}

[[存在一个缺省的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_x1303041195}[策略，名称为]{style="font-family:宋体"}[default-policy]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x193120313}

[[系统视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1438262691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_1612185226}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_553411288}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_144633141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1398949739}

[*[policy-name]{lang="EN-US"}*]{#struct_0_14212_10009_766947308}[：]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个任意字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_708730375}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1673390325}[（]{style="font-family:宋体"}[MACsec Key Agreement]{lang="EN-US"}[，]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[密钥协商）策略用于管理在]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略视图下的相关配置，包括加密偏移量、接收数据帧校验模式、重播保护使能和重播保护窗口大小。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14212_10009_2091660583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统中可配置多个]{style="font-family:宋体"}]{#struct_0_14212_10009_980503654}[MKA]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_859384492}[策略]{lang="EN-US" style="font-family:宋体"}[default-policy]{lang="EN-US"}[不能被删除和修改。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1962588757}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1801922995}[创建一个名称为]{style="font-family:宋体"}[abcd]{lang="EN-US"}[的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略，并进入该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[[\<Syaname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x5949034}

[\[Sysname\] mka policy abcd]{lang="EN-US"}

[\[Sysname-mka-policy-abcd\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_303819164}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[confidentiality-offset]{lang="EN-US"}**]{#struct_0_14212_10009_x2016569373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka]{lang="EN-US"}**]{#struct_0_14212_10009_1103450359}**[ ]{lang="EN-US"}[policy]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_1855988577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_808503493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_1780638566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_x1716727215}
:::

::: {#-793650312 .myid}
[]{#_Toc361834735}[]{#_Toc361319135}[]{#_Toc361230559}[]{#_Toc361164428}[]{#_Toc361068251}[]{#_Toc404794134}[]{#struct_0_14212_10009_708664839}[]{#_Toc361834740}[]{#_Toc361319140}[]{#_Toc361230564}[]{#_Toc361164433}[]{#_Toc360546801}[]{#_Toc359856181}[]{#_Toc359586010}[]{#_Toc359420155}[]{#_Toc357603293}[]{#_Toc357095115}[]{#_Toc356916790}[]{#_Toc356835042}

**MACsec \-- MACsec配置命令 \-- mka priority**

------------------------------------------------------------------------

[**[mka priority]{lang="EN-US"}**]{#struct_0_14212_10009_870103013}[命令用来配置]{style="font-family:宋体"}[MKA]{lang="EN-US"}[密钥服务器的优先级。]{style="font-family:宋体"}

[**[undo mka priority]{lang="EN-US"}**]{#struct_0_14212_10009_1547255155}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1950882229}

[**[mka priority ]{lang="EN-US"}***[priority-value]{lang="EN-US"}*]{#struct_0_14212_10009_x133789196}

[**[undo mka priority]{lang="EN-US"}**]{#struct_0_14212_10009_884675324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_2133780669}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1683818625}[密钥服务器的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1638739565}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1811459092}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x336841499}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1029017981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_1141785175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_1806755243}

[*[priority-value]{lang="EN-US"}*]{#struct_0_14212_10009_1893100180}[：]{style="font-family:宋体"}[MKA]{lang="EN-US"}[密钥服务器优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_709123591}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x179856203}[使用的安全密钥通过]{style="font-family:宋体"}[MKA]{lang="EN-US"}[协议进行协商生成。密钥服务器负责生成和发布]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话所使用的安全密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果采用]{style="font-family:宋体"}]{#struct_0_14212_10009_1448001189}[802.1X]{lang="EN-US"}[认证生成的]{style="font-family:宋体"}[CAK]{lang="EN-US"}[，接入设备的接口自动被选举为密钥服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果采用用户配置的预共享密钥，优先级较高（值较小）的接口被选举为密钥服务器。如果两端的优先级相同，则比较]{style="font-family:宋体"}]{#struct_0_14212_10009_778877033}[SCI]{lang="EN-US"}[（]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[+]{lang="EN-US"}[端口的]{style="font-family:宋体"}[ID]{lang="EN-US"}[），]{style="font-family:宋体"}[SCI]{lang="EN-US"}[值较小的一端将被选举为密钥服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[优先级为]{style="font-family:宋体"}]{#struct_0_14212_10009_415259943}[255]{lang="EN-US"}[的设备端口不能被选举为密钥服务器。相互连接的端口不能都配置优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[，否则]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话选举不出密钥服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_1386889327}[]{#_Toc137470879}[]{#_Toc137475414}[]{#_Toc137547113}[]{#_rrpp_enable}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x1053538769}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[MKA]{lang="EN-US"}[密钥服务优先级为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_323314134}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mka priority 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_218535907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka session]{lang="EN-US"}**]{#struct_0_14212_10009_1182284302}
:::

::: {#-1214227581 .myid}
[]{#_Toc404794135}[]{#struct_0_14212_10009_x1494005216}[]{#_Toc360546802}[]{#_Toc359856182}[]{#_Toc359586011}[]{#_Toc359420156}[]{#_Toc357603294}[]{#_Toc357095114}[]{#_Toc356916789}[]{#_Toc361834741}[]{#_Toc361319141}[]{#_Toc361230565}[]{#_Toc361164434}[]{#_Toc356835041}

**MACsec \-- MACsec配置命令 \-- mka psk**

------------------------------------------------------------------------

[**[mka psk]{lang="EN-US"}**]{#struct_0_14212_10009_709058055}[命令用来配置]{style="font-family:宋体"}[MKA]{lang="EN-US"}[预共享]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[**[undo mka psk]{lang="EN-US"}**]{#struct_0_14212_10009_571293321}[命令用来删除配置的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[预共享]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1164285255}

[**[mka ]{lang="EN-US"}[psk ckn ]{lang="EN-US"}***[name]{lang="EN-US"}***[ cak simple ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_14212_10009_x706438376}

[**[undo mka psk]{lang="EN-US"}**]{#struct_0_14212_10009_x1608149440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_2100095777}

[[不存在]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1172594295}[预共享密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1640954151}

[[以太网接口视图]{style="font-family:宋体"}]{#struct_0_14212_10009_821230002}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_880418573}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x308444006}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1457404978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_708992519}

[**[ckn]{lang="EN-US"}***[ name]{lang="EN-US"}*]{#struct_0_14212_10009_x1687378475}[：表示]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥的名称（]{style="font-family:宋体"}[CKN]{lang="EN-US"}[，]{style="font-family:宋体"}[CAK Name]{lang="EN-US"}[），]{style="font-family:宋体"}*[name]{lang="EN-US"}*[为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:
宋体"}[64]{lang="EN-US"}[个字符的字符串，只能包含偶数个]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数字，不区分大小写。]{style="font-family:宋体"}

[**[cak]{lang="EN-US"}**]{#struct_0_14212_10009_859102488}[：表示]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_14212_10009_103957673}[：表示以明文方式设置预共享密钥。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_14212_10009_x1236128959}[：设置的明文密钥，为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符，且只能为偶数个]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_1233953813}

[[CA]{lang="EN-US"}]{#struct_0_14212_10009_x1720940400}[密钥（]{style="font-family:宋体"}[CAK]{lang="EN-US"}[，]{style="font-family:宋体"}[Secure Connectivity Association Key]{lang="EN-US"}[）有两种来源：]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证过程中生成的]{style="font-family:宋体"}[CAK]{lang="EN-US"}[；通过命令行手工配置。用户手工配置的]{style="font-family:宋体"}[CAK]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[当接口上没有启用]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_14212_10009_1452977268}[认证功能时，可以通过]{style="font-family:宋体"}**[mka psk]{lang="EN-US"}**[配置两端使用的]{style="font-family:宋体"}[CAK]{lang="EN-US"}[，但必须保证两端的]{style="font-family:宋体"}[CAK]{lang="EN-US"}[配置一致，否则不能建立正常的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_14212_10009_x1362037841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两端建立正常的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_1373366519}[会话后，若要删除配置的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}[，则建议首先在密钥服务器端执行]{lang="EN-US" style="font-family:宋体"}**[undo mka psk]{lang="EN-US"}**[命令，然后在非密钥服务器端执行]{lang="EN-US" style="font-family:宋体"}**[mka psk]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除配置的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}]{#struct_0_14212_10009_x1765871411}[会导致已建立的相应的]{lang="EN-US" style="font-family:宋体"}[MKA]{lang="EN-US"}[会话删除。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当前系统支持的加密算法套件要求所使用的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}]{#struct_0_14212_10009_x9078862}[、]{lang="EN-US" style="font-family:宋体"}[CAK]{lang="EN-US"}[的长度都必须为]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[个字符。在运行加密算法套件时，对于长度不足]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[个字符的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[CAK]{lang="EN-US"}[，系统会自动在其后补零，使其满足]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[个字符；对于长度大于]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[个字符的]{lang="EN-US" style="font-family:宋体"}[CKN]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[CAK]{lang="EN-US"}[，系统只获取其前]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[个字符。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1646736085}

[]{#_Toc353442647}[]{#_Toc345072402}[]{#_Toc345072231}[]{#_Toc257636544}[]{#_Toc124742949}[]{#_Toc101584101}[]{#struct_0_14212_10009_483961815}[]{#_Toc137470872}[]{#_Toc137475407}[]{#_Toc137547106}[]{#_Toc137470874}[]{#_Toc137475409}[]{#_Toc137547108}[]{#_Toc137470875}[]{#_Toc137475410}[]{#_Toc137547109}[]{#_rrpp_domain}[\# ]{lang="EN-US"}[在接口]{style="font-family:
宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置预共享]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥的名称为]{style="font-family:宋体"}[AB]{lang="EN-US"}[，预共享]{style="font-family:宋体"}[CA]{lang="EN-US"}[密钥为明文]{style="font-family:宋体"}[1234]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_708926983}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] mka psk ckn AB cak simple 1234]{lang="EN-US"}
:::

::: {#-1598495216 .myid}
[]{#_Toc353442648}[]{#_Toc345072403}[]{#_Toc345072232}[]{#_Toc257636545}[]{#_Toc124742950}[]{#_Toc101584102}[]{#_Toc361834748}[]{#_Toc361319149}[]{#_Toc361230572}[]{#_Toc361164441}[]{#_Toc360546809}[]{#_Toc359856189}[]{#_Toc359586018}[]{#_Toc359420159}[]{#_Toc357603297}[]{#_Toc357095119}[]{#_Toc356916794}[]{#_Toc356835046}[]{#_Toc404794136}[]{#struct_0_14212_10009_x509858450}[]{#_Toc376250740}[]{#_Toc376250741}

**MACsec \-- MACsec配置命令 \-- replay-protection enable**

------------------------------------------------------------------------

[**[replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_738563770}[命令用来开启]{style="font-family:
宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[**[undo replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_1371257495}[命令用来关闭]{style="font-family:
宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_340360263}

[**[replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x562744715}

[**[undo replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x1623985199}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_1115536058}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1266422347}[重播保护功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_1399230442}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_75454707}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1399311537}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x721640242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_709385735}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_67810509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_x1497340208}[重播保护功能可以单独开启，且仅针对接收到的数据帧。重播保护为了防止收到乱序或重复的数据帧。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_14212_10009_x1811005168}[MKA]{lang="EN-US"}[策略中开启的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能状态，在该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略成功应用到接口上之后，将会覆盖该接口上已开启的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1595443231}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_502143272}[在]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[abcd]{lang="EN-US"}[中开启]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x1607267176}

[\[Sysname\] mka policy abcd]{lang="EN-US"}

[\[Sysname-mka-policy-abcd\] replay-protection enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_733573245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_x933895165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1265001458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_1871740145}
:::

::: {#1288750376 .myid}
[]{#_Toc404794137}[]{#struct_0_14212_10009_x1154534230}[]{#_Toc361834736}[]{#_Toc361319136}[]{#_Toc361230560}

**MACsec \-- MACsec配置命令 \-- replay-protection window-size**

------------------------------------------------------------------------

[**[replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_709320199}[命令用来配置]{style="font-family:
宋体"}[MACsec]{lang="EN-US"}[重播保护窗口大小。]{style="font-family:宋体"}

[**[undo replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_2059455057}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1609552394}

[**[replay-protection window-size ]{lang="EN-US"}***[size-value]{lang="EN-US"}*]{#struct_0_14212_10009_x1900463593}

[**[undo replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_380108628}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1995373402}

[[MACsec]{lang="EN-US"}]{#struct_0_14212_10009_1474764224}[重播保护窗口大小为]{style="font-family:宋体"}[0]{lang="EN-US"}[个数据帧，表示不允许接收乱序或重复的数据帧。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_2109474580}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_641788497}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x738739437}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1908075793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_178301377}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_708861446}

[*[size-value]{lang="EN-US"}*]{#struct_0_14212_10009_675163952}[：重播保护窗口大小，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为数据帧。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_x850774364}

[[在某些组网下（如数据帧穿过运营商网络），数据帧因为发送优先级的不同，在转发过程中会被重新排序，最终到达接收端会出现乱序。如果要正常接收这些乱序的数据帧，需配置重播保护窗口。假设配置的重播保护窗口大小为]{style="font-family:宋体"}[a]{lang="EN-US"}]{#struct_0_14212_10009_315236414}[，如果接收到了一个报文序号（]{style="font-family:宋体"}[PN]{lang="EN-US"}[，]{style="font-family:宋体"}[Packet Number]{lang="EN-US"}[）为]{style="font-family:宋体"}[x]{lang="EN-US"}[的报文，则下一个允许被接收的报文的]{style="font-family:宋体"}[PN]{lang="EN-US"}[必须大于或等于]{style="font-family:宋体"}[x-a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该功能仅在重播保护功能开启的情况下有效。]{style="font-family:宋体"}]{#struct_0_14212_10009_257444286}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请结合数据帧在传输网络中的转发途径，选择适当的重播保护窗口大小。若数据帧有可能被多次转发，那么乱序的可能性和乱序的范围会比较大，则建议适当调大重播保护窗口，反之调小。]{style="font-family:宋体"}]{#struct_0_14212_10009_x409202111}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_14212_10009_x2147022967}[MKA]{lang="EN-US"}[策略中配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口值，在该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略成功应用到接口上之后，将会覆盖该接口上配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[重播保护窗口值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1917639991}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_x1487768906}[在]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[abcd]{lang="EN-US"}[中配置重播保护窗口大小为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_x1904315009}

[\[Sysname\] mka policy abcd]{lang="EN-US"}

[\[Sysname-mka-policy-abcd\] replay-protection window-size 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1265622440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec replay-protection window-size]{lang="EN-US"}**]{#struct_0_14212_10009_1716206780}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec replay-protection enable]{lang="EN-US"}**]{#struct_0_14212_10009_1277357716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x1381073870}
:::

::: {#925693080 .myid}
[]{#_Toc404794138}[]{#struct_0_14212_10009_708795910}

**MACsec \-- MACsec配置命令 \-- reset mka session**

------------------------------------------------------------------------

[**[reset mka session]{lang="EN-US"}**]{#struct_0_14212_10009_x674484584}[命令用来重建接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1128977650}

[**[reset mka session ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_14212_10009_772259363}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1971619932}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1123713526}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1968991918}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_158388545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x225919627}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_284367662}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14212_10009_1618377715}[：]{style="font-family:宋体;color:black"}[指定接口类型和接口编号]{style="font-family:宋体"}[。若不指定该参数，则表示重建所有]{style="font-family:宋体;
color:black"}[接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_1368029665}

[[重建接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}]{#struct_0_14212_10009_877601685}[会话是指，先清除接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话，然后立即触发协商建立新的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_2030635572}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1284162008}[重建接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[\<Sysname\> reset mka session interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14212_10009_1234996765}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_708730374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka session]{lang="EN-US"}**]{#struct_0_14212_10009_1673390324}
:::

::: {#686379139 .myid}
[]{#_Toc404794139}[]{#struct_0_14212_10009_2091595047}[]{#_Toc361834749}[]{#_Toc361319150}[]{#_Toc361230573}[]{#_Toc361164442}[]{#_Toc360546810}[]{#_Toc359856190}[]{#_Toc359586019}[]{#_Toc359420160}[]{#_Toc357603298}[]{#_Toc357095120}[]{#_Toc356916795}[]{#_Toc356835047}

**MACsec \-- MACsec配置命令 \-- reset mka statistics**

------------------------------------------------------------------------

[**[reset mka statistics]{lang="EN-US"}**]{#struct_0_14212_10009_x620910044}[命令用来清除接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1258290760}

[**[reset mka statistics ]{lang="EN-US"}**[\[ **interface** *interface-type interface-number*]{lang="EN-US"}*[ ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_14212_10009_x1919156840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1969322988}

[[用户视图]{style="font-family:宋体"}]{#struct_0_14212_10009_1194911249}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_520348399}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_x1958764858}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_x502809493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_1547438945}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_14212_10009_708664838}[：]{style="font-family:宋体;color:black"}[指定接口类型和接口编号]{style="font-family:宋体"}[。若不指定该参数，则表示清除所有]{style="font-family:宋体;
color:black"}[接口上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_870103014}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1547255158}[清除接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的]{style="font-family:宋体"}[MKA]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mka statistics interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_14212_10009_x1951603125}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_497177320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display mka statistics]{lang="EN-US"}**]{#struct_0_14212_10009_x205875964}
:::

::: {#-906224679 .myid}
[]{#_Toc404794140}[]{#struct_0_14212_10009_1811757291}[]{#_Toc361834737}[]{#_Toc361319137}[]{#_Toc361230561}[]{#_Toc361164430}[]{#_Toc361068253}

**MACsec \-- MACsec配置命令 \-- validation mode**

------------------------------------------------------------------------

[**[validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_851999064}[命令用来配置]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[**[undo validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_2043748312}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_1863113741}

[**[validation mode]{lang="EN-US"}**[ { **check** \| **disabled** \| **strict** }]{lang="EN-US"}]{#struct_0_14212_10009_2096607618}

[**[undo validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_x598490870}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_14212_10009_1431709227}

[**[check]{lang="EN-US"}**]{#struct_0_14212_10009_x1016052487}[模式，表示只作校验，但不丢弃非法数据帧。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_14212_10009_1193888593}

[[MKA]{lang="EN-US"}]{#struct_0_14212_10009_709123590}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_14212_10009_x179856202}

[[network-admin]{lang="EN-US"}]{#struct_0_14212_10009_1448066725}

[[mdc-admin]{lang="EN-US"}]{#struct_0_14212_10009_2008582198}

[[【参数】]{style="font-family:黑体"}]{#struct_0_14212_10009_2015047245}

[**[check]{lang="EN-US"}**]{#struct_0_14212_10009_885353795}[：]{style="font-family:宋体;color:black"}[检查模式，表示[只作校验，但不丢弃非法数据帧]{style="color:black"}。]{style="font-family:宋体"}

[[[disabled]{lang="EN-US"}]{.commandkeywords}]{#struct_0_14212_10009_246746643}[：]{style="font-family:宋体;color:black"}[不对接收数据帧进行]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_14212_10009_x1660615820}[：]{style="font-family:宋体;color:black"}[严格校验模式，表示校验数据帧，并丢弃非法数据帧。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_14212_10009_x1351979745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在网络中部署支持]{style="font-family:宋体"}]{#struct_0_14212_10009_x1433478411}[MACsec]{lang="EN-US"}[的设备时，为避免两端因密钥协商不一致而造成流量丢失，建议两端均先配置为]{style="font-family:宋体"}**[check]{lang="EN-US"}**[模式，在密钥协商成功后，再配置为]{style="font-family:宋体"}**[strict]{lang="EN-US"}**[模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_14212_10009_1566781206}[MKA]{lang="EN-US"}[策略中配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式，在该]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略成功应用到接口上之后，将会覆盖该接口上配置的]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_14212_10009_2002896901}

[[\# ]{lang="EN-US"}]{#struct_0_14212_10009_1675165591}[在]{style="font-family:宋体"}[MKA]{lang="EN-US"}[策略]{style="font-family:宋体"}[abcd]{lang="EN-US"}[中配置]{style="font-family:宋体"}[MACsec]{lang="EN-US"}[校验模式为严格校验模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_14212_10009_709058054}

[\[Sysname\] mka policy abcd]{lang="EN-US"}

[\[Sysname-mka-policy-abcd\] validation mode strict]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_14212_10009_571293320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[macsec validation mode]{lang="EN-US"}**]{#struct_0_14212_10009_1164285256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mka apply policy]{lang="EN-US"}**]{#struct_0_14212_10009_x706634984}
:::
