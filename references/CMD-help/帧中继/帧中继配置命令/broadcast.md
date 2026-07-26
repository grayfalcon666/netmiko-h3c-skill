::: {#-389412524 .myid}
[]{#_Toc31792863}[]{#_Toc31686767}[]{#_Toc136938164}[]{#_Toc96758242}[]{#_Toc42517344}[]{#_Toc38976463}[]{#_Toc38682095}[]{#_Toc38081396}[]{#_Toc35242970}[]{#_Toc33369509}[]{#_Toc404785857}[]{#struct_0_x1106_16493_1737674741}[]{#_Toc364694875}[]{#_Toc353521696}[]{#_Toc341189174}[]{#_Hlt24619044}

**帧中继 \-- 帧中继配置命令 \-- broadcast**

------------------------------------------------------------------------

[**[broadcast]{lang="EN-US"}**]{#struct_0_x1106_16493_x108051864}[命令用来配置帧中继虚电路的广播属性。]{style="font-family:宋体"}

[**[undo broadcast]{lang="EN-US"}**]{#struct_0_x1106_16493_594175255}[命令用来关闭帧中继虚电路的广播属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020021911}

[**[broadcast]{lang="EN-US"}**]{#struct_0_x1106_16493_1647319317}

[**[undo broadcast]{lang="EN-US"}**]{#struct_0_x1106_16493_410803562}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_257709548}

[[静态配置的]{style="font-family:宋体"}]{#struct_0_x1106_16493_x186939810}[帧中继虚电路不具备广播属性，动态学习的帧中继虚电路具备广播属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x851372781}

[[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}]{#struct_0_x1106_16493_1880033530}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1351353048}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1030408031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_832354672}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1052861424}

[[如果]{style="font-family:宋体"}]{#struct_0_x1106_16493_1249816432}[帧中继虚电路具备了广播属性，则所属接口上的广播或组播报文都要在该虚电路上发送一份。如果需要在静态配置的虚电路上发送广播或者组播报文，务必配置本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_972326701}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_1135992079}[打开]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的虚电路的广播属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x2020087447}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[Sysname-Serial2/1/0-fr-dlci-200\] broadcast]{lang="EN-US"}
:::

::: {#-211854468 .myid}
[]{#_Toc404785858}[]{#struct_0_x1106_16493_2138808933}

**帧中继 \-- 帧中继配置命令 \-- display fr compression iphc**

------------------------------------------------------------------------

[**[display fr compression iphc]{lang="SV"}**]{#struct_0_x1106_16493_1597025389}[命令用来显示帧中继]{style="font-family:宋体"}[IPHC]{lang="SV"}[压缩的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1284421237}

[**[display fr compression iphc]{lang="SV"}**]{#struct_0_x1106_16493_457567114}[ { **rtp** \| **tcp** } \[ **interface** *interface-type interface-number* ]{lang="SV"}[\[ **dlci** *number* \] ]{lang="EN-US"}[\]]{lang="SV"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x29053902}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_88214673}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x821645235}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1230414790}

[[network-operator]{lang="EN-US"}]{#struct_0_x1106_16493_x802536910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x2103059846}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1106_16493_2139660901}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1638271196}

[**[rtp]{lang="EN-US"}**]{#struct_0_x1106_16493_1069981882}[：显示]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x1106_16493_738838344}[：显示]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_x456333068}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，将显示该主接口及其子接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。指定子接口时，将只显示该子接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}[不指定接口时，]{style="font-family:宋体"}[将显示所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[**[dlci]{lang="EN-US"}**[ *dlci-number*]{lang="EN-US"}]{#struct_0_x1106_16493_1109169245}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。指定虚电路时，必须首先指定接口。指定主接口和虚电路时，无论指定的虚电路在主接口上还是在子接口上，都会显示这个虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息；指定子接口和虚电路时，如果指定的虚电路在子接口上，将显示这个虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息，如果指定的虚电路在子接口所对应的主接口上，将不显示统计信息。不指定虚电路时，将显示指定接口下的所有虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_598687042}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x1106_16493_x435854072}[压缩的统计信息是基于虚电路的。每个接口下会存在一个或多个虚电路。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x808578904}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_2139726437}[显示]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口下]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[17]{lang="EN-US"}[的虚电路的]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr compression iphc rtp interface serial 2/1/0 dlci 17]{lang="EN-US"}]{#struct_0_x1106_16493_528621382}

[DLCI: 17, Serial2/1/0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 0/0 packets]{lang="EN-US"}

[    Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}

[    Packet-based compression ratio]{lang="EN-US"}[：]{style="font-family:宋体"} [0%]{lang="EN-US"}

[    Byte-based compression ratio]{lang="EN-US"}[：]{style="font-family:宋体"}[ 0%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1589841389}[显示]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr compression iphc tcp interface serial 2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_2139136606}

[DLCI: 16, Serial2/1/0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 0/0 packets]{lang="EN-US"}

[    Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 0%]{lang="EN-US"}

[    Byte-based compression ratio: 0%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[DLCI: 17, Serial2/1/0]{lang="EN-US"}

[  Received:]{lang="EN-US"}

[    Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}

[  Sent:]{lang="EN-US"}

[    Compressed/Total: 0/0 packets]{lang="EN-US"}

[    Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}

[    Packet-based compression ratio: 0%]{lang="EN-US"}

[    Byte-based compression ratio: 0%]{lang="EN-US"}

[  Connections:]{lang="EN-US"}

[    Rx/Tx: 16/16]{lang="EN-US"}

[    Five-Minute-Miss: 0 (Misses/5Mins)]{lang="EN-US"}

[    Max-Miss: 0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display fr compression iphc]{lang="EN-US"}]{#struct_0_x1106_16493_904797955}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1997277740}[[字段]{style="font-family:黑体"}]{#struct_0_x1106_16493_445086783}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1106_16493_752868968}

[[DLCI: 17, Serial2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_1996042910}

[[虚电路编号，虚电路所在的接口]{style="font-family:宋体"}]{#struct_0_x1106_16493_2139202142}

[[Received:]{lang="EN-US"}]{#struct_0_x1106_16493_1275851146}

[[  Compressed/Error/Total: 0/0/0 packets]{lang="EN-US"}]{#struct_0_x1106_16493_304725864}

[[收到报文的统计信息：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x323166234}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compressed]{lang="EN-US"}]{#struct_0_x1106_16493_x1669064802}[：被压缩的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x1106_16493_2139005534}[：错误报文数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x1106_16493_x1410743914}[：总的报文数]{lang="EN-US" style="font-family:宋体"}

[[Sent:]{lang="EN-US"}]{#struct_0_x1106_16493_657246394}

[[  Compressed/Total: 0/0 packets]{lang="EN-US"}]{#struct_0_x1106_16493_x1062892748}

[[  Sent/Saved/Total: 0/0/0 bytes]{lang="EN-US"}]{#struct_0_x1106_16493_2139071070}

[[  Packet-based compression ratio: 0%]{lang="EN-US"}]{#struct_0_x1106_16493_x287730682}

[[  Byte-based compression ratio: 0%]{lang="EN-US"}]{#struct_0_x1106_16493_x1986181867}

[[发送报文的统计信息：]{style="font-family:宋体"}]{#struct_0_x1106_16493_1597022017}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Compressed]{lang="EN-US"}]{#struct_0_x1106_16493_x1048154249}[：被压缩的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x1106_16493_2138874462}[：总的报文数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sent]{lang="EN-US"}]{#struct_0_x1106_16493_x1433258708}[：实际发送的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Saved]{lang="EN-US"}]{#struct_0_x1106_16493_x1075286196}[：节省的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x1106_16493_x619735226}[：在不压缩的情况下，需要发送的字节数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Packet-based compression ratio]{lang="EN-US"}]{#struct_0_x1106_16493_2138939998}[：基于报文的压缩率，表示压缩的报文在总发送报文中的比率，即（]{lang="EN-US" style="font-family:宋体"}[Compressed]{lang="EN-US"}[÷]{lang="EN-US" style="font-family:宋体"}[Total]{lang="EN-US"}[）×]{lang="EN-US" style="font-family:宋体"}[100%]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Byte-based compression ratio]{lang="EN-US"}]{#struct_0_x1106_16493_x1134348411}[：基于字节的压缩率，表示压缩后带宽节省的百分比，即（]{lang="EN-US" style="font-family:宋体"}[Saved]{lang="EN-US"}[÷]{lang="EN-US" style="font-family:宋体"}[Total]{lang="EN-US"}[）×]{lang="EN-US" style="font-family:宋体"}[100%]{lang="EN-US"}

[[Connections]{lang="EN-US"}]{#struct_0_x1106_16493_x1012384839}[：]{style="font-family:宋体"}

[[  Rx/Tx]{lang="EN-US"}]{#struct_0_x1106_16493_335332430}

[[  Five-Minute-Miss: x (Misses/5Mins)]{lang="EN-US"}]{#struct_0_x1106_16493_2138743390}

[[  Max-Miss: x]{lang="EN-US"}]{#struct_0_x1106_16493_2049408269}

[[连接信息：]{style="font-family:宋体"}]{#struct_0_x1106_16493_1813306543}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Rx]{lang="EN-US"}]{#struct_0_x1106_16493_1894379130}[：作为接收方，可解压缩的连接数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tx]{lang="EN-US"}]{#struct_0_x1106_16493_2138808926}[：作为发送方，可压缩的连接数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Five-Minute-Miss]{lang="EN-US"}]{#struct_0_x1106_16493_1597221996}[：最后]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟内，查找表项失败的次数（系统每]{style="font-family:宋体"}[5]{lang="EN-US"}[分钟统计一次查找表项失败的次数，本字段显示的是最新一次统计的结果）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max-Miss]{lang="EN-US"}]{#struct_0_x1106_16493_871359564}[：查找表项失败的最大次数（将每次统计的查找表项失败的次数进行比较，得到最大值在这个字段显示）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1163361333}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_x546649971}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset fr compression iphc]{lang="EN-US"}**]{#struct_0_x1106_16493_x1193858299}

::: {#555224223 .myid}
[]{#_Toc404785859}[]{#struct_0_x1106_16493_x658997326}[]{#_Toc364694851}

**帧中继 \-- 帧中继配置命令 \-- display fr inarp-info**

------------------------------------------------------------------------

[**[display fr inarp-info]{lang="EN-US"}**]{#struct_0_x1106_16493_1183433394}[命令用来显示帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1694106202}

[**[display fr inarp-info]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_x94289469}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1048657773}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_712965254}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x806616474}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1608066341}

[[network-operator]{lang="EN-US"}]{#struct_0_x1106_16493_x1058848607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1265135251}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1106_16493_1383394265}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_334449151}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_587575410}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，显示该主接口及子接口的]{style="font-family:宋体"}[帧中继]{style="font-family:宋体"}[InARP]{lang="SV"}[报文统计信息。]{style="font-family:宋体"}[指定子接口时，显示该子接口的]{style="font-family:宋体"}[帧中继]{style="font-family:宋体"}[InARP]{lang="SV"}[报文统计信息。]{style="font-family:宋体"}[不指定接口时，显示所有接口的帧中继]{style="font-family:宋体"}[InARP]{lang="SV"}[报文统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020152983}

[[帧中继]{style="font-family:宋体"}]{#struct_0_x1106_16493_x922323022}[InARP]{lang="SV"}[报文分为两种：]{style="font-family:宋体"}[InARP]{lang="SV"}[请求报文和]{style="font-family:宋体"}[InARP]{lang="SV"}[应答报文。根据本命令的输出信息，可以诊断]{style="font-family:宋体"}[InARP]{lang="SV"}[协议是否正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x673161526}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_540314978}[显示帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr inarp-info]{lang="EN-US"}]{#struct_0_x1106_16493_1355164738}

[Frame relay InARP statistics for interface Serial2/1/0 (DTE)]{lang="EN-US"}

[  Recvd InARP request  Sent InARP reply  Sent InARP request  Recvd InARP reply]{lang="EN-US"}

[  0                    0                 1                   1]{lang="EN-US"}

[]{#struct_0_x1106_16493_1942442629}[[表1-2 ]{lang="EN-US"}[display fr inarp-info]{lang="EN-US"}]{#_Toc121672380}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1675175439}[[字段]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2108794338}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1106_16493_1802002808}

[[Frame relay InARP statistics for interface Serial2/1/0 (DTE)]{lang="EN-US"}]{#struct_0_x1106_16493_1821129396}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_1576553773}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}[报文统计信息]{style="font-family:宋体"}

[[Recvd InARP request]{lang="EN-US"}]{#struct_0_x1106_16493_2141563131}

[[接收的]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x1312701734}[请求报文]{style="font-family:宋体"}

[[Sent InARP reply]{lang="EN-US"}]{#struct_0_x1106_16493_x2020218519}

[[发送的]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x1787894312}[应答报文]{style="font-family:宋体"}

[[Sent InARP request]{lang="EN-US"}]{#struct_0_x1106_16493_x2176723}

[[发送的]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x1944778068}[请求报文]{style="font-family:宋体"}

[[Recvd InARP reply]{lang="EN-US"}]{#struct_0_x1106_16493_571236921}

[[接收的]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x1618140033}[应答报文]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1668386132}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_1089408909}

::: {#-1288658666 .myid}
[]{#_Toc404785860}[]{#struct_0_x1106_16493_x1266888170}[]{#_Toc364694852}[]{#_Toc136938168}

**帧中继 \-- 帧中继配置命令 \-- display fr lmi-info**

------------------------------------------------------------------------

[**[display fr lmi-info]{lang="EN-US"}**]{#struct_0_x1106_16493_x2028921827}[命令用来显示]{style="font-family:宋体"}[LMI]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1504246844}

[**[display fr lmi-info ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_1587925578}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_760855894}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019759767}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1566684309}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1948738473}

[[network-operator]{lang="EN-US"}]{#struct_0_x1106_16493_174712916}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_578247983}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1106_16493_x1831389513}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x895856264}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1106_16493_x1919086627}[：指定接口的类型和编号，只能指定主接口，不能指定子接口。指定主接口时，显示该主接口的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[信息]{style="font-family:宋体"}[。不指定主接口时，显示所有]{style="font-family:宋体"}[主]{style="font-family:宋体"}[接口的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1190289578}

[[LMI]{lang="EN-US"}]{#struct_0_x1106_16493_681263429}[协议用于维护当前帧中继链路，]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议报文包括状态请求报文和状态报文。根据这些显示信息，可以进行故障的诊断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x64309025}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x887156634}[显示所有接口的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr lmi-info]{lang="EN-US"}]{#struct_0_x1106_16493_x2019825303}

[Frame relay LMI information for interface Serial2/1/1 (DTE, Q933)]{lang="EN-US"}

[  T391DTE: 10 seconds, N391DTE: 6, N392DTE: 3, N393DTE: 4]{lang="EN-US"}

[  Sent status enquiry: 96, Received status: 85]{lang="EN-US"}

[  Status timeout: 3, Discarded messages: 3]{lang="EN-US"}

[Frame relay LMI information for interface Serial2/1/0 (DCE, Q933)]{lang="EN-US"}

[  T392DCE: 15 seconds, N392DCE: 3, N393DCE: 4]{lang="EN-US"}

[  Received status enquiry: 0, Sent status: 0]{lang="EN-US"}

[  Status enquiry timeout: 0, Discarded messages: 0]{lang="EN-US"}

[]{#struct_0_x1106_16493_1126248752}[]{#_Toc121672382}[]{#_Toc96758247}[表1-3 ]{lang="EN-US"}[display fr lmi-info]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1677231483}[[字段]{style="font-family:黑体"}]{#struct_0_x1106_16493_x696067843}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1106_16493_605198807}

[[Frame relay LMI information for interface Serial2/1/1 (DTE, Q933)]{lang="EN-US"}]{#struct_0_x1106_16493_1313647884}

[[帧中继接口]{style="font-family:宋体"}[Serial2/1/1]{lang="EN-US"}]{#struct_0_x1106_16493_x1629259386}[的终端类型为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[，]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[Q.933]{lang="EN-US"}[附录]{style="font-family:宋体"}[A]{lang="EN-US"}[标准]{style="font-family:宋体"}

[[T391DTE: 10 seconds, N391DTE: 6, N392DTE: 3, N393DTE: 4]{lang="EN-US"}]{#struct_0_x1106_16493_x1460977150}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x65261938}[方的]{style="font-family:宋体"}[T391]{lang="EN-US"}[定时器的参数值（单位为秒，]{style="font-family:宋体"}[T391]{lang="EN-US"}[定时器的值通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令配置）、]{style="font-family:宋体"}[N391]{lang="EN-US"}[参数值、]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数值以及]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数值]{style="font-family:宋体"}

[[Sent status enquiry: 96, Received status: 85]{lang="EN-US"}]{#struct_0_x1106_16493_380773135}

[[接口发出的状态请求报文数以及接口接收的状态报文数]{style="font-family:宋体"}]{#struct_0_x1106_16493_1546227755}

[[Status timeout: 3, Discarded messages: 3]{lang="EN-US"}]{#struct_0_x1106_16493_1928789269}

[[状态报文超时的数目以及丢弃报文的数目]{style="font-family:宋体"}]{#struct_0_x1106_16493_x716026632}

[[Frame relay LMI information for interface Serial2/1/0 (DCE, Q933)]{lang="EN-US"}]{#struct_0_x1106_16493_x2019890839}

[[帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_x571679402}[的终端类型为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[，]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型为]{style="font-family:宋体"}[Q.933]{lang="EN-US"}[附录]{style="font-family:宋体"}[A]{lang="EN-US"}[标准]{style="font-family:宋体"}

[[T392DCE: 15 seconds, N392DCE: 3, N393DCE: 4]{lang="EN-US"}]{#struct_0_x1106_16493_651946317}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_523143395}[方的]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数值、]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数值以及]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数值]{style="font-family:宋体"}

[[Received status enquiry: 0, Sent status: 0]{lang="EN-US"}]{#struct_0_x1106_16493_x18319047}

[[接口接收的状态请求报文数以及接口发送的状态报文数]{style="font-family:宋体"}]{#struct_0_x1106_16493_x702135198}

[[Status enquiry timeout: 0, Discarded messages : 0]{lang="EN-US"}]{#struct_0_x1106_16493_x2122631204}

[[状态请求报文超时的数目以及丢弃报文的数目]{style="font-family:宋体"}]{#struct_0_x1106_16493_1179682757}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_311893494}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi n391dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x447164948}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi n392dce]{lang="EN-US"}**]{#struct_0_x1106_16493_x2019956375}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi n392dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x1354287963}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi n393dce]{lang="EN-US"}**]{#struct_0_x1106_16493_x1082615527}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi n393dte]{lang="EN-US"}**]{#struct_0_x1106_16493_967935392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi t392dce]{lang="EN-US"}**]{#struct_0_x1106_16493_x698955830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr lmi type]{lang="EN-US"}**]{#struct_0_x1106_16493_1123648603}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer-hold]{lang="EN-US"}**]{#struct_0_x1106_16493_744085622}

::: {#529833922 .myid}
[]{#_Toc404785861}[]{#struct_0_x1106_16493_x963678284}[]{#_Toc364694853}[]{#_Toc136938169}

**帧中继 \-- 帧中继配置命令 \-- display fr map-info**

------------------------------------------------------------------------

[**[display fr map-info]{lang="EN-US"}**]{#struct_0_x1106_16493_x794002250}[命令用来显示帧中继地址映射表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1665154055}

[**[display fr map-info ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_1831478811}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_578074990}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_245970647}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019497623}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x967862038}

[[network-operator]{lang="EN-US"}]{#struct_0_x1106_16493_1639582463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1686962773}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1106_16493_x1452922475}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2053871867}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_2018875533}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，显示该主接口及子接口的帧中继地址映射表]{style="font-family:宋体"}[。]{style="font-family:宋体"}[指定子接口时，显示该子接口的帧中继地址映射表]{style="font-family:宋体"}[。]{style="font-family:宋体"}[不指定接口时，显示所有接口的]{style="font-family:宋体"}[帧中继地址映射表]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x979413648}

[[通过本命令的显示信息可以查看用户配置的静态地址映射是否正确、动态地址映射是否工作正常等。]{style="font-family:宋体"}]{#struct_0_x1106_16493_436762398}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1377657512}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x393473362}[显示]{style="font-family:宋体"}[所有接口的]{style="font-family:宋体"}[帧中继地址映射表。]{style="font-family:宋体"}

[[\<Sysname\> display fr map-info]{lang="EN-US"}]{#struct_0_x1106_16493_1692387418}

[Map information for interface Serial2/1/0 (DTE)]{lang="EN-US"}

[  DLCI: 100, IP InARP 100.100.1.1, Serial2/1/0]{lang="EN-US"}

[    Creation time: 2012/10/21 14:48:44, Status: Active]{lang="EN-US"}

[  DLCI: 200, IP InARP 100.100.1.1, Serial2/1/0]{lang="EN-US"}

[    Creation time: 2012/10/21 14:34:42, Status: Active]{lang="EN-US"}

[  DLCI: 300, IP 1.1.1.1, Serial2/1/0]{lang="EN-US"}

[    Creation time: 2012/10/21 15:03:35, Status: Active]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display fr map-info]{lang="EN-US"}]{#struct_0_x1106_16493_797429097}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1669879411}[[字段]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019563159}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1106_16493_1283710764}

[[Map information for interface Serial2/1/0 (DTE)]{lang="EN-US"}]{#struct_0_x1106_16493_959739671}

[[显示接口的帧中继地址映射表信息，该接口工作在]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_2059362316}[方式]{style="font-family:宋体"}

[[DLCI: 100, IP InARP 100.100.1.1, Serial2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_x752931146}

[[DLCI]{lang="EN-US"}]{#struct_0_x1106_16493_x576881074}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的虚电路和对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[100.100.1.1]{lang="EN-US"}[通过]{style="font-family:宋体"}[InARP]{lang="EN-US"}[协议建立地址映射，该虚电路配置在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上（如果没有]{style="font-family:宋体"}[InARP]{lang="EN-US"}[关键字，表示是通过手工配置建立的静态地址映射）]{style="font-family:宋体"}

[[Creation time: 2012/10/21 14:48:44]{lang="EN-US"}]{#struct_0_x1106_16493_1761840742}

[[该映射创建的时间]{style="font-family:宋体"}]{#struct_0_x1106_16493_319050439}

[[Status: Active]{lang="EN-US"}]{#struct_0_x1106_16493_x1208212747}

[[该映射的状态，与映射的虚电路状态保持一致，取值可能为：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x499905342}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1106_16493_x1442020265}[：激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactvie]{lang="EN-US"}]{#struct_0_x1106_16493_x1818008482}[：非激活状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020021908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_437531272}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr map ip]{lang="EN-US"}**]{#struct_0_x1106_16493_844433689}

::: {#-824795415 .myid}
[]{#_Toc404785862}[]{#struct_0_x1106_16493_x1588092379}[]{#_Toc364694854}

**帧中继 \-- 帧中继配置命令 \-- display fr pvc-info**

------------------------------------------------------------------------

[**[display fr pvc-info]{lang="EN-US"}**]{#struct_0_x1106_16493_x124141415}[命令用来显示帧中继的永久虚电路状态和该虚电路收发数据的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1312262799}

[**[display fr pvc-info]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \] \[ **dlci** *dlci-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_x2115715400}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x771308072}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x298558114}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2047049425}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_149101679}

[[network-operator]{lang="EN-US"}]{#struct_0_x1106_16493_x2042871334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_485535499}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1106_16493_106904970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_432874383}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_x2020087444}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，显示该主接口及子接口的永久虚电路信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[指定子接口时，显示该子接口的永久虚电路信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[不指定接口时，显示所有接口的]{style="font-family:宋体"}[永久虚电路信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[dlci]{lang="EN-US"}**[ *dlci-number*]{lang="EN-US"}]{#struct_0_x1106_16493_907086615}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。指定虚电路时，显示该永久虚电路的详细信息，不指定虚电路时，显示永久虚电路的概要信息。详细信息相比概要信息增加了帧中继流量管理等信息，例如流量整形信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1427509052}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x735884115}[显示帧中继所有永久虚电路的状态和收发数据的简要统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr pvc-info]{lang="EN-US"}]{#struct_0_x1106_16493_805572779}

[PVC information for interface Serial2/1/0 (DTE, physical UP)]{lang="EN-US"}

[  DLCI: 100, Type: Dynamic, Serial2/1/0]{lang="EN-US"}

[    Encapsulation: ietf, Broadcast]{lang="EN-US"}

[    Creation time: 2012/04/01 23:55:39, Status: Active]{lang="EN-US"}

[    Input: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[    Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[  DLCI: 102, Type: Static, Serial2/1/0.1]{lang="EN-US"}

[    Encapsulation: nonstandard]{lang="EN-US"}

[    Creation time: 2012/04/01 23:56:14, Status: Active]{lang="EN-US"}

[    Input: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[    Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1607987631}[显示指定永久虚电路的状态和收发数据的详细统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fr pvc-info dlci 100]{lang="EN-US"}]{#struct_0_x1106_16493_779884131}

[PVC information for interface Serial2/1/0 (DTE, physical UP)]{lang="EN-US"}

[  DLCI: 100, Type: Dynamic, Serial2/1/0]{lang="EN-US"}

[    Encapsulation: ietf, Broadcast]{lang="EN-US"}

[    Creation time: 2012/04/01 23:55:39, Status: Active]{lang="EN-US"}

[    Input: 0 packets, 0 bytes, 0 dropped ]{lang="EN-US"}

[    Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[    Traffic shaping: Inactive]{lang="EN-US"}

[      CIR allow: 56000 bps]{lang="EN-US"}

[      Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}

[]{#struct_0_x1106_16493_x1003172972}[[表1-5 ]{lang="EN-US"}[display fr pvc-info]{lang="EN-US"}]{#_Toc121672386}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1673347907}[[字段]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020152980}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1106_16493_1806560333}

[[PVC information for interface Serial2/1/0 (DTE, physical UP)]{lang="EN-US"}]{#struct_0_x1106_16493_x831446202}

[[显示帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_968489309}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[信息，该接口工作在]{style="font-family:宋体"}[DTE]{lang="EN-US"}[方式，物理层状态为]{style="font-family:宋体"}[Up]{lang="EN-US"}

[[DLCI: 100, Type: Dynamic, Serial2/1/0]{lang="EN-US"}]{#struct_0_x1106_16493_x631037601}

[[DLCI=100]{lang="EN-US"}]{#struct_0_x1106_16493_855278557}[的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的类型为]{style="font-family:宋体"}[Dynamic]{lang="EN-US"}[，配置在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上，]{style="font-family:宋体"}[PVC]{lang="EN-US"}[类型的取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dynamic]{lang="EN-US"}]{#struct_0_x1106_16493_760412042}[：通过]{style="font-family:宋体"}[LMI]{lang="EN-US"}[动态学习的]{style="font-family:宋体"}[PVC]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x1106_16493_327748162}[：静态配置的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}[，包括通过]{lang="EN-US" style="font-family:宋体"}**[fr map ip]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[fr dlci]{lang="EN-US"}**[配置的]{lang="EN-US" style="font-family:宋体"}[PVC]{lang="EN-US"}

[[Encapsulation: ietf, Broadcast]{lang="EN-US"}]{#struct_0_x1106_16493_1754773612}

[[封装格式为]{style="font-family:宋体"}[IETF]{lang="EN-US"}]{#struct_0_x1106_16493_859948765}[，允许发送广播报文]{style="font-family:宋体"}

[[Creation time: 2012/04/01 23:55:39, Status: Active]{lang="EN-US"}]{#struct_0_x1106_16493_x1260919193}

[[该]{style="font-family:宋体"}[PVC]{lang="EN-US"}]{#struct_0_x1106_16493_123192405}[的创建时间以及]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[PVC]{lang="EN-US"}]{#struct_0_x1106_16493_x2020218516}[状态取值可能为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1106_16493_228528323}[：激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactvie]{lang="EN-US"}]{#struct_0_x1106_16493_818607635}[：非激活状态]{lang="EN-US" style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}]{#struct_0_x1106_16493_x2113439178}

[[接收的报文数、字节数和丢弃报文数]{style="font-family:宋体"}]{#struct_0_x1106_16493_400317045}

[[Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}]{#struct_0_x1106_16493_1257049729}

[[发送的报文数、字节数和丢弃报文数]{style="font-family:宋体"}]{#struct_0_x1106_16493_66934096}

[[Traffic shaping: Inactive]{lang="EN-US"}]{#struct_0_x1106_16493_1246310036}

[[流量整形状态，状态取值可能为：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x451394564}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x1106_16493_x460644414}[：激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x1106_16493_x2019759764}[：非激活状态]{lang="EN-US" style="font-family:宋体"}

[[CIR allow: 56000 bps]{lang="EN-US"}]{#struct_0_x1106_16493_1162199046}

[[允许的承诺信息速率]{style="font-family:宋体"}]{#struct_0_x1106_16493_1014965108}

[[Output: 0 packets, 0 bytes, 0 dropped]{lang="EN-US"}]{#struct_0_x1106_16493_x1077976625}

[[使能流量整形功能后的发送]{style="font-family:宋体"}]{#struct_0_x1106_16493_1698672593}[报文数]{style="font-family:宋体"}[、]{style="font-family:宋体"}[字节数]{style="font-family:宋体"}[和丢弃报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_413298493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[broadcast]{lang="EN-US"}**]{#struct_0_x1106_16493_x1002558364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr dlci]{lang="EN-US"}**]{#struct_0_x1106_16493_849657601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr ]{lang="EN-US"}[encapsulation]{lang="EN-US"}**]{#struct_0_x1106_16493_701782822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr map ip]{lang="EN-US"}**]{#struct_0_x1106_16493_x1982688899}

::: {#99577240 .myid}
[]{#_Toc404785863}[]{#struct_0_x1106_16493_2139660895}

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc enable**

------------------------------------------------------------------------

[**[fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_x317781803}[命令用来开启帧中继]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[**[undo fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_776691237}[命令用来关闭帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1643568027}

[**[fr compression iphc enable]{lang="EN-US"}**[ \[ **nonstandard** \]]{lang="EN-US"}]{#struct_0_x1106_16493_x1119159459}

[**[undo fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_2139726431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_528752454}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x1106_16493_x1618134717}[压缩功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x262946080}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1106_16493_x2082611885}[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1662611155}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x782514143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_2001278778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2140685318}

[**[nonstandard]{lang="EN-US"}**]{#struct_0_x1106_16493_x1898626741}[：非标准的兼容的封装格式。不指定本参数时，则按照标准格式进行报文封装。与友商设备互通时需要配置本参数。配置本参数后，仅支持]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩，不支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x794388181}

[[帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x1106_16493_x589746745}[压缩分为如下两种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RTP]{lang="EN-US"}]{#struct_0_x1106_16493_x2145243578}[头压缩：对报文中的]{style="font-family:宋体"}[RTP/UDP/IP]{lang="EN-US"}[头进行压缩。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x1106_16493_x521854424}[头压缩：对报文中的]{style="font-family:宋体"}[TCP/IP]{lang="EN-US"}[头进行压缩。]{style="font-family:宋体"}

[[开启帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}]{#struct_0_x1106_16493_668217201}[压缩功能后，上述两种压缩功能都将启动；关闭帧中继]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后，上述两种压缩功能都将被禁止。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_697528406}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户必须在链路的两端同时开启帧中继]{style="font-family:宋体"}]{#struct_0_x1106_16493_x432150098}[IPHC]{lang="EN-US"}[压缩功能，该功能才生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户可以在接口视图下和]{style="font-family:宋体"}]{#struct_0_x1106_16493_464577033}[DLCI]{lang="EN-US"}[视图下配置本命令，接口视图下的配置对该接口下的所有虚电路生效，]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下的配置只对本虚电路生效。如果接口视图的配置与]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图的配置不同，则以]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下的配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当帧中继的封装格式为]{style="font-family:宋体"}]{#struct_0_x1106_16493_2131898166}**[ietf]{lang="EN-US"}**[时（通过命令]{style="font-family:宋体"}**[fr encapsulation]{lang="EN-US"}**[配置），开启]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后会触发]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商，协商成功后压缩功能才生效；当帧中继的封装格式为]{style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[时，开启]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后不会触发]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[协商，压缩功能直接生效，而且仅支持]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩，不支持]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩。]{style="font-family:宋体"}[此时，需要链路两端的封装格式都配置为]{lang="EN-US" style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[才能正常通信。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_x1106_16493_x955274128}[IPHC]{lang="EN-US"}[压缩功能时，不会立即停止压缩，需要在接口下或者虚电路所在的接口下执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[与]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作后，才会关闭压缩功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1429086073}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x114406737}[开启帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x589681209}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr compression iphc enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1803830842}[开启]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的帧中继虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_720820061}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 100]{lang="EN-US"}

[\[Sysname-fr-dlci-Serial2/1/0-100\]]{lang="NO-BOK"}[ fr compression iphc enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x436925919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr ]{lang="EN-US"}[encapsulation]{lang="EN-US"}**]{#struct_0_x1106_16493_1039965170}
:::

::: {#2068388228 .myid}
[]{#_Toc404785864}[]{#struct_0_x1106_16493_x449524496}

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc rtp-connections**

------------------------------------------------------------------------

[**[fr compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_1990082252}[命令用来配置接口或虚电路上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数。]{style="font-family:宋体"}

[**[undo fr compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_2070441850}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x60378004}

[**[fr compression iphc rtp-connections ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1106_16493_57667976}

[**[undo fr compression iphc rtp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_x589877817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_536716095}

[[接口或虚电路上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}]{#struct_0_x1106_16493_x965721434}[头压缩的最大连接数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x584542715}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1106_16493_x678732909}[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1622404055}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_980836588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x664499932}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1879503113}

[*[number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1312511744}[：每条虚电路上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。当]{style="font-family:宋体"}*[number]{lang="EN-US"}*[≤]{style="font-family:宋体"}[256]{lang="EN-US"}[时，报文将被压缩成]{style="font-family:宋体"}[COMPRESSED_RTP_8]{lang="EN-US"}[格式，当]{style="font-family:宋体"}*[number]{lang="EN-US"}*[＞]{style="font-family:宋体"}[256]{lang="EN-US"}[时，报文将被压缩成]{style="font-family:宋体"}[COMPRESSED_RTP_16]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x140246636}

[[RTP]{lang="EN-US"}]{#struct_0_x1106_16493_x1669376761}[（]{style="font-family:宋体"}[Real-time Transport Protocol]{lang="EN-US"}[，实时传输协议）是面向连接的协议，一条链路上所能承载的]{style="font-family:宋体"}[RTP]{lang="EN-US"}[连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用]{style="font-family:宋体"}**[fr compression iphc rtp-connections]{lang="EN-US"}**[命令来配置]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数。例如最大连接数配置为]{style="font-family:宋体"}[3]{lang="EN-US"}[时，第]{style="font-family:宋体"}[4]{lang="EN-US"}[条]{style="font-family:宋体"}[RTP]{lang="EN-US"}[连接上的报文就不会被压缩了。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x589812281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口视图下配置了]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1382917057}[RTP]{lang="EN-US"}[头压缩的最大连接数，那么该接口下的所有虚电路都会继承这个最大连接数；如果在该接口下的某]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下配置了不同的最大连接数，那么以这个]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下的配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在开启]{style="font-family:宋体"}]{#struct_0_x1106_16493_x309746742}[IPHC]{lang="EN-US"}[压缩功能后，才能配置本命令。在关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能后，本配置将被清除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1106_16493_x261956937}[本功能后，]{style="font-family:宋体"}[需要在接口下或者虚电路所在的接口下执行]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[与]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作后，配置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1141777078}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1449166274}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_1557815020}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr compression iphc enable]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr compression iphc rtp-connections 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_520084739}[配置]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的帧中继虚电路上允许进行]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_853045062}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 100]{lang="EN-US"}

[\[Sysname-fr-dlci-Serial2/1/0-100\]]{lang="NO-BOK"}[ fr compression iphc enable]{lang="EN-US"}

[\[Sysname-fr-dlci-Serial2/1/0-100\]]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[fr compression iphc rtp-connections 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1162727871}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_x590008889}
:::

::: {#1621291207 .myid}
[]{#_Toc404785865}[]{#struct_0_x1106_16493_932479072}

**帧中继 \-- 帧中继配置命令 \-- fr compression iphc tcp-connections**

------------------------------------------------------------------------

[**[fr compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_2053656969}[命令用来配置接口或虚电路上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数。]{style="font-family:宋体"}

[**[undo fr compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_x1826923214}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_418111473}

[**[fr compression iphc tcp-connections ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1106_16493_x2112670597}

[**[undo fr compression iphc tcp-connections]{lang="EN-US"}**]{#struct_0_x1106_16493_652059909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1739468545}

[[接口或虚电路上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1106_16493_x742934166}[头压缩的最大连接数为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1477558460}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1106_16493_x370720888}[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1974140246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x589943353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x977678162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x910664213}

[*[number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1311660726}[：每条虚电路上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_160426436}

[[TCP]{lang="EN-US"}]{#struct_0_x1106_16493_x441321831}[是面向连接的协议，一条链路上所能承载的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的数目是比较多的，但压缩算法压缩时需对每个连接维护一定的信息，从而占用一定的内存，因此可以用]{style="font-family:宋体"}**[fr compression iphc tcp-connections]{lang="EN-US"}**[命令来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数。例如最大连接数配置为]{style="font-family:宋体"}[3]{lang="EN-US"}[时，第]{style="font-family:宋体"}[4]{lang="EN-US"}[条]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接上的报文就不会被压缩了。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_583566731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口视图下配置了]{style="font-family:宋体"}]{#struct_0_x1106_16493_728344331}[TCP]{lang="EN-US"}[头压缩的最大连接数，那么该接口下的所有虚电路都会继承这个最大连接数；如果在该接口下的某]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下配置了不同的最大连接数，那么以这个]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图下的配置为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在开启]{style="font-family:宋体"}]{#struct_0_x1106_16493_1751115884}[IPHC]{lang="EN-US"}[压缩功能，且不指定]{style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[参数时，才能配置本命令。在关闭]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩功能]{style="font-family:宋体"}[或者更改配置为]{lang="EN-US" style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[模式]{lang="EN-US" style="font-family:宋体"}[后，本配置将被清除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1106_16493_x1955078686}[本功能后，]{style="font-family:宋体"}[需要在接口下或者虚电路所在的接口下执行]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[与]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作后，配置才能生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1537844177}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_1207845293}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x590139961}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr compression iphc enable]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr compression iphc tcp-connections 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_539561004}[配置]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的帧中继虚电路上允许进行]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的最大连接数为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x20494221}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 100]{lang="EN-US"}

[\[Sysname-fr-dlci-Serial2/1/0-100\]]{lang="NO-BOK"}[ fr compression iphc enable]{lang="EN-US"}

[\[Sysname-fr-dlci-Serial2/1/0-100\]]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[fr compression iphc tcp-connections 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1709569902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr compression iphc enable]{lang="EN-US"}**]{#struct_0_x1106_16493_706925706}
:::

::: {#-1453851585 .myid}
[]{#_Toc404785866}[]{#struct_0_x1106_16493_210632391}[]{#_Toc364694855}[]{#_Toc96758255}

**帧中继 \-- 帧中继配置命令 \-- fr dlci**

------------------------------------------------------------------------

[**[fr dlci]{lang="EN-US"}**]{#struct_0_x1106_16493_x1870290390}[命令用来为帧中继接口创建虚电路，并进入相应的帧中继虚电路视图。]{style="font-family:宋体"}

[**[undo fr dlci]{lang="EN-US"}**]{#struct_0_x1106_16493_x2019825300}[命令用来删除帧中继接口的虚电路。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_722964225}

[**[fr dlci]{lang="EN-US"}**[ *dlci-number*]{lang="EN-US"}]{#struct_0_x1106_16493_x1546714523}

[**[undo]{lang="EN-US"}**[ **fr dlci** \[ *dlci-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_x381331393}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1092765395}

[[接口下不存在虚电路。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1658886435}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1475453479}

[[接口视图（包括主接口和子接口）]{style="font-family:宋体"}]{#struct_0_x1106_16493_150382875}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1587820610}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1808839877}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1673149530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_179641205}

[*[dlci-number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1984991505}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[号]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[1008]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[为帧中继协议保留，供特殊使用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1129353153}

[[当帧中继接口类型是]{style="font-family:宋体"}[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_403659488}[或]{style="font-family:宋体"}[NNI]{lang="EN-US"}[时，需要为接口（不论是主接口还是子接口）手动创建虚电路。当帧中继接口类型是]{style="font-family:宋体"}[DTE]{lang="EN-US"}[时，如果接口是主接口，则系统会根据对端设备自动确定虚电路，也可以手工配置虚电路；如果是子接口，则必须手动为接口指定虚电路。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019890836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[虚电路号在一个主接口及其所有子接口上是唯一的。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2137763343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在配置]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**]{#struct_0_x1106_16493_x173664997}[命令时，如果不指定]{lang="EN-US" style="font-family:宋体"}*[dlci-number]{lang="EN-US"}*[，则删除帧中继接口上的所有虚电路。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x792734412}[接口和]{style="font-family:宋体"}[NNI]{lang="EN-US"}[接口在]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协商过程中需要传递虚电路信息，如果接口上配置的虚电路个数太多，协商报文长度超过了接口最大帧长度的限制，会导致]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协商不通过。接口最大帧长度与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_197916850}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1078095856}[为帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[创建一条]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[的虚电路。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_1951516331}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 100]{lang="NO-BOK"}

[\[Sysname-Serial2/1/0-fr-dlci-100\]]{lang="NO-BOK"}
:::

::: {#-1607864256 .myid}
[]{#_Toc404785867}[]{#struct_0_x1106_16493_115763403}[]{#_Toc364694856}

**帧中继 \-- 帧中继配置命令 \-- fr encapsulation**

------------------------------------------------------------------------

[**[fr ]{lang="EN-US"}[encapsulation]{lang="EN-US"}**]{#struct_0_x1106_16493_x755150240}[命令用来配置帧中继接口或者虚电路的封装格式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fr** **encapsulation**]{lang="EN-US"}]{#struct_0_x1106_16493_1244852737}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_829905305}

[**[fr ]{lang="EN-US"}[encapsulation]{lang="EN-US"}**[ { **ietf** \| **nonstandard** }]{lang="EN-US"}]{#struct_0_x1106_16493_1454117994}

[**[undo]{lang="EN-US"}**[ **fr** **encapsulation**]{lang="EN-US"}]{#struct_0_x1106_16493_x670829394}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1641420392}

[[帧中继接口的封装格式为]{style="font-family:宋体"}[IETF]{lang="EN-US"}]{#struct_0_x1106_16493_x1195326627}[，帧中继虚电路采用接口配置的封装格式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019956372}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1106_16493_1018365032}[帧中继]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1743807260}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1838154804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x563913222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1627750533}

[**[ietf]{lang="EN-US"}**]{#struct_0_x1106_16493_x2009603091}[：]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准封装。]{style="font-family:宋体"}

[**[nonstandard]{lang="EN-US"}**]{#struct_0_x1106_16493_1382165085}[：非标准兼容的封装格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1606762926}

[[当封装接口链路层协议为帧中继时，可以选择]{style="font-family:宋体"}[IETF]{lang="EN-US"}]{#struct_0_x1106_16493_316829858}[标准（]{style="font-family:宋体"}**[ietf]{lang="EN-US"}**[），按照]{style="font-family:宋体"}[RFC 1490]{lang="EN-US"}[规定的格式进行封装；也可以选择非标准兼容（]{style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[）的封装格式，它与业界主流路由器的专用封装格式是兼容的。]{style="font-family:宋体"}

[[当帧中继接口封装为以上任何一种帧中继格式后，接口将按该格式发送报文，但接口可以识别和接收这两种报文，也就是说，即使对端设备封装的帧中继格式和本地不同，只要对端设备也支持这两种格式的自动识别，两端设备一样可以通信。但在对端设备不支持对这两种格式的自动识别时，应将两端设备的帧中继格式设为一致。]{style="font-family:宋体"}]{#struct_0_x1106_16493_994354744}

[[虚电路的封装格式以虚电路配置的封装格式优先，缺省时采用接口配置的封装格式，当虚电路配置封装格式后，虚电路按照该格式发送报文。]{style="font-family:宋体"}]{#struct_0_x1106_16493_227023440}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1333066416}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_781790180}[在接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上封装帧中继，并选择非标准兼容封装格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x2019497620}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr encapsulation nonstandard]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_1761021317}[配置]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[200]{lang="EN-US"}[的帧中继虚电路的封装格式为]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准封装。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x477968281}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr dlci 200]{lang="EN-US"}

[\[Sysname-Serial2/1/0-fr-dlci-200\] fr encapsulation ietf]{lang="EN-US"}
:::

::: {#-1581104316 .myid}
[]{#_Toc404785868}[]{#struct_0_x1106_16493_479092244}[]{#_Toc364694857}[]{#_Toc322966303}

**帧中继 \-- 帧中继配置命令 \-- fr inarp**

------------------------------------------------------------------------

[**[fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_739793190}[命令用来使能帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_999738229}[命令用来关闭帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x633893461}

[**[fr inarp]{lang="EN-US"}**[ **ip** \[ *dlci-number* \] ]{lang="EN-US"}]{#struct_0_x1106_16493_281171887}

[**[undo]{lang="EN-US"}**[ **fr inarp** **ip** \[ *dlci-number* \]]{lang="EN-US"}]{#struct_0_x1106_16493_870161762}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1190356193}

[[帧中继]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x69772907}[功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1387924693}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_122833088}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1963602939}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1535392957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1426456970}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019563156}

[**[ip]{lang="EN-US"}**]{#struct_0_x1106_16493_167965517}[：表示对]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行逆向地址解析。]{style="font-family:宋体"}

[*[dlci-number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1065512304}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，表示只对该虚电路号进行逆向地址解析，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1106350243}

[[帧中继在接口上发送数据时，需要进行对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1106_16493_558586554}[地址与本地]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[的映射，该映射可以由手工配置来指定，也可以通过启用]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能来自动完成。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_2028448776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要使能或关闭接口上所有虚电路的]{style="font-family:宋体"}]{#struct_0_x1106_16493_2112474298}[InARP]{lang="EN-US"}[功能，则使用不带任何参数的该命令。如果要使能或关闭指定虚电路上的]{style="font-family:宋体"}[InARP]{lang="EN-US"}[功能，则使用带]{style="font-family:宋体"}*[dlci-number]{lang="EN-US"}*[参数的该命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上（包括子接口）使能]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x780678259}[功能，则接口下所有虚电路也使能此功能，此时可以用]{lang="EN-US" style="font-family:宋体"}**[undo fr inarp ip ]{lang="EN-US"}***[dlci-number]{lang="EN-US"}*[命令单独关闭某条虚电路上的]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[功能；如果用]{lang="EN-US" style="font-family:宋体"}**[undo fr inarp]{lang="EN-US"}**[关闭了某个接口的]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[功能，则接口下所有虚电路也关闭了此功能，此时可以使用]{lang="EN-US" style="font-family:宋体"}**[fr inarp ip ]{lang="EN-US"}***[dlci-number]{lang="EN-US"}*[命令在某条虚电路上使能]{lang="EN-US" style="font-family:宋体"}[InARP]{lang="EN-US"}[功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在主接口下启动]{style="font-family:宋体"}]{#struct_0_x1106_16493_614375512}[InARP]{lang="EN-US"}[功能对该主接口下的子接口同样生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2077542267}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x2024730143}[在帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上的所有虚电路上都允许进行逆向地址解析。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x1780475096}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr inarp ip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1123109205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fr inarp-info]{lang="EN-US"}**]{#struct_0_x1106_16493_x1577628364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr inarp]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_x1106_16493_x2020021909}
:::

::: {#-1230286317 .myid}
[]{#_Toc404785869}[]{#struct_0_x1106_16493_2003615213}[]{#_Toc364694858}

**帧中继 \-- 帧中继配置命令 \-- fr inarp interval**

------------------------------------------------------------------------

[**[fr inarp interval]{lang="EN-US"}**]{#struct_0_x1106_16493_881680051}[命令用来配置]{style="font-family:宋体"}[InARP]{lang="EN-US"}[学习时的请求报文发送间隔时间。]{style="font-family:宋体"}

[**[undo fr inarp interval]{lang="EN-US"}**]{#struct_0_x1106_16493_868818871}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x498013118}

[**[fr inarp]{lang="EN-US"}**[ **interval** *seconds*]{lang="EN-US"}]{#struct_0_x1106_16493_x1421883537}

[**[undo]{lang="EN-US"}**[ **fr inarp** **interval**]{lang="EN-US"}]{#struct_0_x1106_16493_1898183800}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1430390083}

[[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_232661427}[学习时的请求报文发送间隔时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1969444152}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_1058940335}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x752344087}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1784815571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1467792759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1862810790}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1106_16493_1333482187}[：]{style="font-family:宋体"}[InARP]{lang="EN-US"}[学习时的请求报文发送间隔时间，取值范围为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020087445}

[[InARP]{lang="SV"}]{#struct_0_x1106_16493_x1821796740}[功能使能后，]{style="font-family:宋体"}[InARP]{lang="SV"}[学习时的请求报文发送间隔时间才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_925679126}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x1510355421}[配置帧中继接口]{style="font-family:宋体"}[InARP]{lang="EN-US"}[学习时的请求报文发送间隔时间为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x157004304}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr inarp interval 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_820059961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fr inarp-info]{lang="EN-US"}**]{#struct_0_x1106_16493_1231640224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_1490883799}
:::

::: {#-259201658 .myid}
[]{#_Toc404785870}[]{#struct_0_x1106_16493_303036891}[]{#_Toc364694859}[]{#_Toc96758258}

**帧中继 \-- 帧中继配置命令 \-- fr interface-type**

------------------------------------------------------------------------

[**[fr interface-type]{lang="EN-US"}**]{#struct_0_x1106_16493_1625600273}[命令用来配置帧中继接口类型。]{style="font-family:宋体"}

[**[undo fr interface-type]{lang="EN-US"}**]{#struct_0_x1106_16493_445985688}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_142430972}

[**[fr interface-type]{lang="EN-US"}**[ { **dce** \| **dte** \| ]{lang="EN-US"}]{#struct_0_x1106_16493_930303352}**[nni]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo fr interface-type]{lang="EN-US"}**]{#struct_0_x1106_16493_x2020152981}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_240476392}

[[帧中继接口类型为]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_2081202865}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_100827507}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_1601530676}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x569302205}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1842678328}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1569658774}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x281844222}

[**[dce]{lang="EN-US"}**]{#struct_0_x1106_16493_1054480348}[：配置帧中继接口类型为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Circuit-terminating Equipment]{lang="EN-US"}[，数据电路终接设备）。]{style="font-family:宋体"}

[**[dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x1626004343}[：配置帧中继接口类型为]{style="font-family:宋体"}[DTE]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Terminal Equipment]{lang="EN-US"}[，数据终端设备）。]{style="font-family:宋体"}

[**[nni]{lang="EN-US"}**]{#struct_0_x1106_16493_x1375441629}[：配置帧中继接口类型为]{style="font-family:宋体"}[NNI]{lang="EN-US"}[（]{style="font-family:宋体"}[Network-to-Network Interface]{lang="EN-US"}[，网间网接口）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_862141107}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x2039037540}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[类型为]{style="font-family:宋体"}[DCE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x2020218517}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}
:::

::: {#1115344543 .myid}
[]{#_Toc404785871}[]{#struct_0_x1106_16493_x1337555618}[]{#_Toc364694860}[]{#_Toc31686770}

**帧中继 \-- 帧中继配置命令 \-- fr lmi n391dte**

------------------------------------------------------------------------

[**[fr lmi n391dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x1477289546}[命令用来配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N391]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr lmi n391dte]{lang="EN-US"}**]{#struct_0_x1106_16493_817304552}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1235506081}

[**[fr lmi n391dte]{lang="EN-US"}***[ n391-value]{lang="EN-US"}*]{#struct_0_x1106_16493_525285519}

[**[undo fr lmi n391dte]{lang="EN-US"}**]{#struct_0_x1106_16493_1888406421}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_x1106_16493_8740902}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_1014123443}[侧]{style="font-family:宋体"}[N391]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1837193415}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_1569808620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x440816147}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1748063788}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1903702222}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019759765}

[*[n391-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x403884895}[：计数器]{style="font-family:宋体"}[N391]{lang="EN-US"}[的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_993182809}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_1909577850}[设备每隔一定的时间（时间间隔由]{style="font-family:宋体"}[T391]{lang="EN-US"}[决定）要发送一个状态请求报文。状态请求报文有两种类型：链路完整性请求报文和全状态请求报文。参数]{style="font-family:宋体"}[N391]{lang="EN-US"}[定义两种报文的发送比例，即（全状态请求报文数：链路完整性请求报文数）]{style="font-family:宋体"}[=]{lang="EN-US"}[（]{style="font-family:宋体"}[1]{lang="EN-US"}[：]{style="font-family:宋体"}[N391-1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[需要注意的是，配置本命令时，要求接口类型是]{style="font-family:宋体"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x1243447019}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1462549817}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x558095635}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DTE]{lang="EN-US"}[方式，计数器]{style="font-family:宋体"}[N391]{lang="EN-US"}[的值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x828396896}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n391dte 10]{lang="EN-US"}
:::

::: {#712060007 .myid}
[]{#_Toc404785872}[]{#struct_0_x1106_16493_1459165130}[]{#_Toc364694861}[]{#_Toc31686771}

**帧中继 \-- 帧中继配置命令 \-- fr lmi n392dce**

------------------------------------------------------------------------

[**[fr]{lang="EN-US"}**[ **lmi n392dce**]{lang="EN-US"}]{#struct_0_x1106_16493_x1000022550}[命令用来配置]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr lmi n392dce]{lang="EN-US"}**]{#struct_0_x1106_16493_169446836}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_735032142}

[**[fr lmi n392dce]{lang="PT-BR"}**]{#struct_0_x1106_16493_635278989}[ *n392-value*]{lang="PT-BR"}

[**[undo fr lmi n392dce]{lang="PT-BR"}**]{#struct_0_x1106_16493_x2019825301}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2005919130}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x982397648}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1795400286}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_81549360}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1127242370}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1017045671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1392527877}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_127913120}

[*[n392-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x388972467}[：]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1128487955}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_1486012092}[设备每隔一定的时间间隔（时间间隔由]{style="font-family:宋体"}[T392]{lang="EN-US"}[决定）要求]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备发送一个状态请求报文。在一定的时间内，如果]{style="font-family:宋体"}[DCE]{lang="EN-US"}[没有收到状态请求报文，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[就记录该错误。如果错误次数超过门限，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备就认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[N392]{lang="EN-US"}]{#struct_0_x1106_16493_1361940019}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[一起定义了"错误门限"。其中]{style="font-family:宋体"}[N393]{lang="EN-US"}[表示被观察的事件总数，]{style="font-family:宋体"}[N392]{lang="EN-US"}[表示在被观察的事件总数中发生错误的门限。也就是说，如果]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备在]{style="font-family:宋体"}[N393]{lang="EN-US"}[个事件中，发生错误次数达到]{style="font-family:宋体"}[N392]{lang="EN-US"}[，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备就认为错误次数达到门限，由此认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x952741210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x1605796334}[侧的]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数值应小于]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019890837}[DCE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_591120012}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x507317151}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DCE]{lang="EN-US"}[方式，并配置]{style="font-family:宋体"}[N392]{lang="EN-US"}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[分别为]{style="font-family:宋体"}[5]{lang="EN-US"}[和]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:
宋体"}

[]{#struct_0_x1106_16493_2093240044}[]{#_Hlt23153243}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n392dce 5]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n393dce 6]{lang="EN-US"}
:::

::: {#712060016 .myid}
[]{#_Toc404785873}[]{#struct_0_x1106_16493_60640230}[]{#_Toc364694862}[]{#_Toc31686772}

**帧中继 \-- 帧中继配置命令 \-- fr lmi n392dte**

------------------------------------------------------------------------

[**[fr lmi n392dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x1662738181}[命令用来配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr lmi n392dte]{lang="EN-US"}**]{#struct_0_x1106_16493_1666386115}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_490868623}

[**[fr lmi n392dte]{lang="EN-US"}***[ n392-value]{lang="EN-US"}*]{#struct_0_x1106_16493_1942550758}

[**[undo fr lmi n392dte]{lang="EN-US"}**]{#struct_0_x1106_16493_1394623280}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x782566750}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_443428355}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2051902214}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019956373}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x547718909}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x476989880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_86305145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x690801738}

[*[n392-value]{lang="EN-US"}*]{#struct_0_x1106_16493_1347793424}[：]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_904318684}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x801528287}[设备每隔一定的时间要发送一个状态请求报文去查询链路状态，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备收到该报文后立即发送状态报文。如果]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备在规定的时间内没有收到响应，就记录该错误。如果错误次数超过门限，]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备就认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[N392]{lang="EN-US"}]{#struct_0_x1106_16493_1468569123}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[两个参数一起定义了"错误门限"。其中]{style="font-family:宋体"}[N393]{lang="EN-US"}[表示被观察的事件总数，]{style="font-family:宋体"}[N392]{lang="EN-US"}[表示在被观察的事件总数中发生的错误门限。也就是说，如果]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备发送]{style="font-family:宋体"}[N393]{lang="EN-US"}[个状态请求报文中，如果发生错误数达到]{style="font-family:宋体"}[N392]{lang="EN-US"}[，]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备就认为错误次数达到门限，由此认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_144253674}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_1629783949}[侧的]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值应小于]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x307326645}[DTE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_700635707}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x155031593}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DTE]{lang="EN-US"}[方式，并配置]{style="font-family:宋体"}[N392]{lang="EN-US"}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[和]{style="font-family:
宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x2019497621}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n392dte 5]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n393dte 6]{lang="EN-US"}
:::

::: {#-2016823348 .myid}
[]{#_Toc404785874}[]{#struct_0_x1106_16493_194937376}[]{#_Toc364694863}[]{#_Toc31686773}

**帧中继 \-- 帧中继配置命令 \-- fr lmi n393dce**

------------------------------------------------------------------------

[**[fr lmi n393dce]{lang="EN-US"}**]{#struct_0_x1106_16493_202755932}[命令用来配置]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr lmi n393dce]{lang="EN-US"}**]{#struct_0_x1106_16493_1114063091}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1483319115}

[**[fr lmi n393dce]{lang="EN-US"}***[ n393-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x1487583399}

[**[undo fr lmi n393dce]{lang="EN-US"}**]{#struct_0_x1106_16493_x1940134310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x109910462}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_659288513}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_705206781}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_1288821581}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1015354611}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_832856504}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x2019563157}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1734049458}

[*[n393-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x1242348196}[：]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2113178128}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x291538335}[设备每隔一定的时间（时间间隔由]{style="font-family:宋体"}[T392]{lang="EN-US"}[决定）要求]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备发送一个状态请求报文。如果]{style="font-family:宋体"}[DCE]{lang="EN-US"}[在规定时间内没有收到状态请求报文，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[就记录该错误。如果错误次数超过门限，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备就认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[N392]{lang="EN-US"}]{#struct_0_x1106_16493_1643544877}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[一起定义了"错误门限"。其中]{style="font-family:宋体"}[N393]{lang="EN-US"}[表示被观察的总事件数，]{style="font-family:宋体"}[N392]{lang="EN-US"}[表示在被观察的总事件数中发生的错误门限。也就是说，如果]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备在]{style="font-family:宋体"}[N393]{lang="EN-US"}[个事件中，发生错误次数达到]{style="font-family:宋体"}[N392]{lang="EN-US"}[，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备就认为错误次数达到门限，且认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x37523261}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x1116214510}[侧的]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值应小于]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x961493448}[DCE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1471906023}

[[\# ]{lang="SV"}]{#struct_0_x1106_16493_x211895428}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="SV"}[工作在]{style="font-family:宋体"}[DCE]{lang="SV"}[方式，并配置]{style="font-family:宋体"}[N392]{lang="SV"}[和]{style="font-family:宋体"}[N393]{lang="SV"}[为]{style="font-family:
宋体"}[5]{lang="SV"}[和]{style="font-family:宋体"}[6]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_x1106_16493_213004532}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n392dce 5]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n393dce 6]{lang="EN-US"}
:::

::: {#-2016823339 .myid}
[]{#_Toc404785875}[]{#struct_0_x1106_16493_1451409813}[]{#_Toc364694864}[]{#_Toc31686774}

**帧中继 \-- 帧中继配置命令 \-- fr lmi n393dte**

------------------------------------------------------------------------

[**[fr]{lang="EN-US"}**[ **lmi n393dte**]{lang="EN-US"}]{#struct_0_x1106_16493_x2020021914}[命令用来配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr]{lang="EN-US"}**[ **lmi n393dte**]{lang="EN-US"}]{#struct_0_x1106_16493_x1888133092}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x132917190}

[**[fr lmi n393dte]{lang="EN-US"}**[ *n393-value*]{lang="EN-US"}]{#struct_0_x1106_16493_x1025211088}

[**[undo fr lmi n393dte]{lang="EN-US"}**]{#struct_0_x1106_16493_x1494322681}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1151781004}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x306673486}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2060485359}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x574676506}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2039628190}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1384877827}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_257479741}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1453420398}

[*[n393-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x1764612972}[：]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2020087450}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x1062347389}[设备每隔一定的时间要发送一个状态请求报文去查询链路状态，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备收到该报文后立即发送状态报文。如果]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备在规定的时间内没有收到响应，就记录该错误。如果错误次数超过门限，]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备就认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[N392]{lang="EN-US"}]{#struct_0_x1106_16493_x338427336}[和]{style="font-family:宋体"}[N393]{lang="EN-US"}[一起定义了"错误门限"。其中]{style="font-family:宋体"}[N393]{lang="EN-US"}[表示被观察的总事件数，]{style="font-family:宋体"}[N392]{lang="EN-US"}[表示在被观察的总事件数中发生的错误门限。也就是说，如果]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备在]{style="font-family:宋体"}[N393]{lang="EN-US"}[个事件中，发生错误次数达到]{style="font-family:宋体"}[N392]{lang="EN-US"}[，]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备就认为错误次数达到门限，且认为物理通路不可用，所有的虚电路都不可用。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x415005501}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x184733814}[侧的]{style="font-family:宋体"}[N392]{lang="EN-US"}[参数的值应小于]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的]{style="font-family:宋体"}[N393]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1925459853}[DTE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1570633771}

[[\# ]{lang="SV"}]{#struct_0_x1106_16493_x960255654}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="SV"}[工作在]{style="font-family:宋体"}[DTE]{lang="SV"}[方式，并配置]{style="font-family:宋体"}[N392]{lang="SV"}[和]{style="font-family:宋体"}[N393]{lang="SV"}[为]{style="font-family:
宋体"}[5]{lang="SV"}[和]{style="font-family:宋体"}[6]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="SV"}]{#struct_0_x1106_16493_x1499043932}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dte]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n392dte 5]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi n393dte 6]{lang="EN-US"}
:::

::: {#-1276957593 .myid}
[]{#_Toc404785876}[]{#struct_0_x1106_16493_x1136360009}[]{#_Toc364694865}[]{#_Toc31686775}

**帧中继 \-- 帧中继配置命令 \-- fr lmi t392dce**

------------------------------------------------------------------------

[**[fr]{lang="EN-US"}**[ **lmi t392dce**]{lang="EN-US"}]{#struct_0_x1106_16493_2137622313}[命令用来配置]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo fr]{lang="EN-US"}**[ **lmi t392dce**]{lang="EN-US"}]{#struct_0_x1106_16493_300085779}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_233273288}

[**[fr lmi t392dce]{lang="EN-US"}**[ *t392-value*]{lang="EN-US"}]{#struct_0_x1106_16493_x2020152986}

[**[undo fr lmi t392dce]{lang="EN-US"}**]{#struct_0_x1106_16493_x1325607549}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1722582413}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x782361487}[侧]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x711804613}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1446992499}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2143203563}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x276053390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1716352557}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1443947500}

[*[t392-value]{lang="EN-US"}*]{#struct_0_x1106_16493_x1201628233}[：]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1889193643}

[[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_1118194274}[侧]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数定义了]{style="font-family:宋体"}[DCE]{lang="EN-US"}[设备等待一个状态请求报文的最大时间。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x424945803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DCE]{lang="EN-US"}]{#struct_0_x1106_16493_x1695308820}[侧的]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数的值应大于]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧的]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值（该参数的值通过]{style="font-family:宋体"}**[timer-hold]{lang="EN-US"}**[命令配置）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x234960226}[DCE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_481944310}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x2020218522}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DCE]{lang="EN-US"}[方式，并配置]{style="font-family:宋体"}[T392]{lang="EN-US"}[为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x1740905681}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr interface-type dce]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi t392dce 10]{lang="EN-US"}
:::

::: {#-1714653284 .myid}
[]{#_Toc404785877}[]{#struct_0_x1106_16493_49628933}[]{#_Toc364694866}[]{#_Toc31686776}

**帧中继 \-- 帧中继配置命令 \-- fr lmi type**

------------------------------------------------------------------------

[**[fr lmi type]{lang="EN-US"}**]{#struct_0_x1106_16493_799908149}[命令用来配置帧中继]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型。]{style="font-family:宋体"}

[**[undo fr lmi type]{lang="EN-US"}**]{#struct_0_x1106_16493_x1984247149}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1158820908}

[**[fr lmi type]{lang="FR"}**]{#struct_0_x1106_16493_x648695498}[ { **ansi** \| **nonstandard** \| **q933a** }]{lang="FR"}

[**[undo fr lmi type]{lang="EN-US"}**]{#struct_0_x1106_16493_x516049977}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x487915020}

[[接口的]{style="font-family:宋体"}[LMI]{lang="EN-US"}]{#struct_0_x1106_16493_x226849708}[协议类型为]{style="font-family:宋体"}[q933a]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2100501327}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x364803035}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1612349542}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1311834308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x2019759770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1163334246}

[**[ansi]{lang="EN-US"}**]{#struct_0_x1106_16493_447627523}[：]{style="font-family:宋体"}[ANSI T1.617]{lang="EN-US"}[附录]{style="font-family:宋体"}[D]{lang="EN-US"}[标准的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型。]{style="font-family:宋体"}

[**[nonstandard]{lang="EN-US"}**]{#struct_0_x1106_16493_411794970}[：非标准兼容的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型。]{style="font-family:宋体"}

[**[q933a]{lang="EN-US"}**]{#struct_0_x1106_16493_560930582}[：]{style="font-family:宋体"}[ITU-T Q.933]{lang="EN-US"}[附录]{style="font-family:宋体"}[A]{lang="EN-US"}[标准的]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x797484531}

[[LMI]{lang="EN-US"}]{#struct_0_x1106_16493_x793249645}[协议用于维护帧中继协议的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[表，包括：通知]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的增加、探测]{style="font-family:宋体"}[PVC]{lang="EN-US"}[的删除、监控]{style="font-family:宋体"}[PVC]{lang="EN-US"}[状态的变更、验证链路的完整性。]{style="font-family:宋体"}

[[系统支持三种]{style="font-family:宋体"}[LMI]{lang="EN-US"}]{#struct_0_x1106_16493_1015417867}[协议类型：]{style="font-family:宋体"}[ITU-T]{lang="EN-US"}[的]{style="font-family:宋体"}[Q.933]{lang="EN-US"}[附录]{style="font-family:宋体"}[A]{lang="EN-US"}[、]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[的]{style="font-family:宋体"}[T1.617]{lang="EN-US"}[附录]{style="font-family:宋体"}[D]{lang="EN-US"}[、非标准兼容协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1019446982}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_579250211}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[的帧中继]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议类型为非标准兼容协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x179740970}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr lmi type nonstandard]{lang="NO-BOK"}
:::

::: {#1807250245 .myid}
[]{#_Toc404785878}[]{#struct_0_x1106_16493_1069220513}[]{#_Toc364694867}[]{#_Toc31686778}

**帧中继 \-- 帧中继配置命令 \-- fr map ip**

------------------------------------------------------------------------

[**[fr]{lang="EN-US"}**[ **map** **ip**]{lang="EN-US"}]{#struct_0_x1106_16493_1980388365}[命令用来增加一条帧中继的地址映射。]{style="font-family:宋体"}

[**[undo fr]{lang="EN-US"}**[ **map** **ip**]{lang="EN-US"}]{#struct_0_x1106_16493_x382807365}[命令用来删除一条帧中继的地址映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x52911299}

[**[fr]{lang="EN-US"}**[ **map** **ip** { *ip-address* \| **default** } *dlci-number*]{lang="EN-US"}]{#struct_0_x1106_16493_x2019825306}

[**[undo]{lang="EN-US"}**[ **fr** **map ip** { *ip-address* \| **default** }]{lang="EN-US"}]{#struct_0_x1106_16493_1885763639}[]{#_Hlt23155590}[ *dlci-number*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2064514439}

[[系统没有静态地址映射。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1349881302}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x670983818}

[[接口视图（包括主接口和]{style="font-family:宋体"}[P2MP]{lang="EN-US"}]{#struct_0_x1106_16493_658732925}[子接口）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_797387025}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_863313036}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1617875256}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x206864563}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1106_16493_1244578896}[：对端[]{#_Hlt14231758}的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x1106_16493_x1896355820}[：表示创建一条缺省地址映射。]{style="font-family:宋体"}

[*[dlci-number]{lang="EN-US"}*]{#struct_0_x1106_16493_1370131276}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[号]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:
宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[1008]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[为帧中继协议保留，供特殊使用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_731955280}

[[地址映射可以通过手工配置建立，也可以通过]{style="font-family:宋体"}[InARP]{lang="EN-US"}]{#struct_0_x1106_16493_x1333657146}[协议来自动完成。当对端主机较少或有缺省路由的情况下采用手工配置静态地址映射；当对端路由器也支持]{style="font-family:宋体"}[InARP]{lang="EN-US"}[协议而且网络较复杂的情况下，采用]{style="font-family:宋体"}[InARP]{lang="EN-US"}[协议建立动态地址映射。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x391930477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置地址映射中的地址要求是有效的单播地址。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019890842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，如果指定的虚电路不存在，则会创建此虚电路。]{style="font-family:宋体"}]{#struct_0_x1106_16493_188032093}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个接口最多只能配置一条缺省地址映射。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x982616168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个接口到同一个]{style="font-family:宋体"}]{#struct_0_x1106_16493_1771253348}[IP]{lang="EN-US"}[地址只能配置一条地址映射。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_816687591}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_760329573}[接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[连接的对端路由器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[202.38.163.252]{lang="EN-US"}[，在本地]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口上有一条]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[为]{style="font-family:宋体"}[50]{lang="EN-US"}[的虚电路连接到该路由器，配置静态地址映射如下：]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x1136963285}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] fr map ip 202.38.163.252 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_905051755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fr map-info]{lang="EN-US"}**]{#struct_0_x1106_16493_x155446698}
:::

::: {#-1075495185 .myid}
[]{#_Toc404785879}[]{#struct_0_x1106_16493_x1045874962}[]{#_Toc300302738}[]{#_Toc136938195}[]{#_Toc96758273}[]{#_Toc31792862}[]{#_Toc31686766}

**帧中继 \-- 帧中继配置命令 \-- link-protocol fr**

------------------------------------------------------------------------

[**[link-protocol fr]{lang="EN-US"}**]{#struct_0_x1106_16493_x1145911708}[命令用来配置接口封装的链路层协议为帧中继。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x911578449}

[**[link-protocol fr]{lang="EN-US"}**]{#struct_0_x1106_16493_1418950490}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1116406791}

[[除以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1106_16493_1705635294}[接口外，其它接口封装的链路层协议均为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2019956378}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_1824934086}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x2120196011}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x587427764}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x783506752}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1629171203}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x243160997}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[封装的链路层协议为帧中继。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_221122756}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="EN-US"}
:::

::: {#535029839 .myid}
[]{#_Toc404785880}[]{#struct_0_x1106_16493_x590074423}

**帧中继 \-- 帧中继配置命令 \-- reset fr compression iphc**

------------------------------------------------------------------------

[**[reset fr compression iphc]{lang="EN-US"}**]{#struct_0_x1106_16493_x589222455}[命令用来清除帧中继]{style="font-family:
宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1776114446}

[**[reset fr compression iphc]{lang="EN-US"}**[ \[ **rtp** \| **tcp** \] \[ **interface** *interface-type interface-number* \[ **dlci** *number* \] \]]{lang="EN-US"}]{#struct_0_x1106_16493_x1134033065}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x973794354}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_873190667}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x926071141}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_1033532683}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1228276298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1537052308}

[**[rtp]{lang="EN-US"}**]{#struct_0_x1106_16493_x1519556495}[：清除]{style="font-family:宋体"}[IPHC RTP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x1106_16493_1398308045}[：清除]{style="font-family:宋体"}[IPHC TCP]{lang="EN-US"}[头压缩的统计信息。不指定]{style="font-family:宋体"}**[rtp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[参数时，将同时清除]{style="font-family:宋体"}[RTP]{lang="EN-US"}[头压缩和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[头压缩的统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x1106_16493_x289229836}[：清除指定接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。不指定本参数时，将清除所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[**[dlci]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x1106_16493_x632024056}[：清除指定接口、指定虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[表示虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。不指定本参数时，将清除指定接口下的所有虚电路的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x589156919}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x240833125}[清除所有接口的]{style="font-family:宋体"}[IPHC]{lang="EN-US"}[压缩的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset fr compression iphc]{lang="EN-US"}]{#struct_0_x1106_16493_x1640981191}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_470553949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fr compression iphc]{lang="EN-US"}**]{#struct_0_x1106_16493_x318691211}
:::

::: {#727135379 .myid}
[]{#_Toc404785881}[]{#struct_0_x1106_16493_1026518263}[]{#_Toc364694868}[]{#_Toc322966318}

**帧中继 \-- 帧中继配置命令 \-- reset fr inarp**

------------------------------------------------------------------------

[**[reset fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_712300559}[命令用来清除]{style="font-family:宋体"}[InARP]{lang="EN-US"}[协议建立的动态地址映射。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1159611248}

[**[reset fr inarp ]{lang="EN-US"}**[\[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number* \] \]]{lang="EN-US"}]{#struct_0_x1106_16493_x2087854135}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2110207077}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1017156360}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2127293792}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_932283639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x2019497626}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1727376925}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_x1652036460}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[该主接口及子接口的动态地址映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}[指定子接口时，]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[该子接口的动态地址映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}[不指定接口时，清除所有接口的]{style="font-family:宋体"}[动态地址映射]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[dlci]{lang="EN-US"}***[ dlci-number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1908245157}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[1008]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[的虚电路为帧中继协议保留，供特殊使用。指定虚电路时，]{style="font-family:宋体"}[清除该虚电路对应的]{style="font-family:
宋体"}[动态地址映射。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_377753782}

[[在某些特殊情况下，如网络结构修改导致原来建立的动态地址映射失效，需要重新建立新的地址映射，此时可以用该命令清除动态地址映射。]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1154845714}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_72093222}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_452864560}[清除]{style="font-family:宋体"}[InARP]{lang="EN-US"}[协议建立的全部动态地址映射。]{style="font-family:宋体"}

[[\<Sysname\> reset fr inarp]{lang="EN-US"}]{#struct_0_x1106_16493_x659832367}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1165293100}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fr inarp]{lang="EN-US"}**]{#struct_0_x1106_16493_338786888}
:::

::: {#-1245228073 .myid}
[]{#_Toc404785882}[]{#struct_0_x1106_16493_122931368}[]{#_Toc364694869}[]{#_Toc322966319}

**帧中继 \-- 帧中继配置命令 \-- reset fr pvc**

------------------------------------------------------------------------

[**[reset fr pvc]{lang="EN-US"}**]{#struct_0_x1106_16493_428315084}[命令用来清除帧中继的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1378837002}

[**[reset fr pvc]{lang="EN-US"}**[ \[ **interface** *interface-type* *interface-number* \[ **dlci** *dlci-number* \] \]]{lang="EN-US"}]{#struct_0_x1106_16493_1709406982}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1355615395}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_x2019563162}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1801599559}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_134076299}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1814930888}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x701871696}

[**[interface]{lang="SV"}**]{#struct_0_x1106_16493_1929733769}[ *interface-type interface-number*]{lang="SV"}[：指定接口的类型和编号，]{style="font-family:
宋体"}[可以指定主接口]{style="font-family:宋体"}[，]{style="font-family:宋体"}[也可以指定子接口。指定主接口时，]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[该主接口及子接口的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[指定子接口时，]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[该子接口的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}[不指定接口时，清除所有接口的]{style="font-family:宋体"}[PVC]{lang="EN-US"}[统计信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[dlci]{lang="EN-US"}***[ dlci-number]{lang="EN-US"}*]{#struct_0_x1106_16493_x1474129578}[：虚电路]{style="font-family:宋体"}[DLCI]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[16]{lang="EN-US"}[～]{style="font-family:宋体"}[1007]{lang="EN-US"}[。范围]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[、]{style="font-family:宋体"}[1008]{lang="EN-US"}[～]{style="font-family:宋体"}[1023]{lang="EN-US"}[的虚电路为帧中继协议保留，供特殊使用。指定虚电路时，]{style="font-family:宋体"}[清除该虚电路对应的]{style="font-family:
宋体"}[PVC]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_720010191}

[[\# ]{lang="SV"}]{#struct_0_x1106_16493_x1448116511}[清除接口]{style="font-family:宋体"}[Serial2/1/0]{lang="SV"}[下所有]{style="font-family:宋体"}[PVC]{lang="SV"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset fr pvc interface serial 2/1/0]{lang="SV"}]{#struct_0_x1106_16493_x472555564}
:::

::: {#1474946988 .myid}
[]{#_Toc404785883}[]{#struct_0_x1106_16493_1070882867}[]{#_Toc300302743}

**帧中继 \-- 帧中继配置命令 \-- timer-hold**

------------------------------------------------------------------------

[**[timer-hold]{lang="EN-US"}**]{#struct_0_x1106_16493_x472244933}[命令用来配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x1106_16493_x1257778106}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x1514765013}

[**[timer-hold]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x1106_16493_x548670839}

[**[undo timer-hold]{lang="EN-US"}**]{#struct_0_x1106_16493_1331433870}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2096531759}

[[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_x2020021915}[侧]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x322049151}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1106_16493_224991714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2128408321}

[[network-admin]{lang="EN-US"}]{#struct_0_x1106_16493_x1618490179}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1106_16493_160224142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1106_16493_1263835332}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1106_16493_1852545484}[：]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。当]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，表示禁止]{style="font-family:宋体"}[LMI]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1106_16493_x573907601}

[[T391]{lang="EN-US"}]{#struct_0_x1106_16493_1609976298}[参数是一个时间变量，它定义了]{style="font-family:宋体"}[DTE]{lang="EN-US"}[设备发送状态请求报文的时间间隔。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1106_16493_x1527641089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DTE]{lang="EN-US"}]{#struct_0_x1106_16493_2004336196}[侧的]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值应小于]{style="font-family:宋体"}[DCE]{lang="EN-US"}[侧的]{style="font-family:宋体"}[T392]{lang="EN-US"}[参数的值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令时，要求接口类型是]{style="font-family:宋体"}]{#struct_0_x1106_16493_x809631741}[DTE]{lang="EN-US"}[或者]{style="font-family:宋体"}[NNI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1106_16493_2145412675}

[[\# ]{lang="EN-US"}]{#struct_0_x1106_16493_x22262110}[配置帧中继接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DTE]{lang="EN-US"}[方式，并配置]{style="font-family:宋体"}[DTE]{lang="EN-US"}[侧]{style="font-family:宋体"}[T391]{lang="EN-US"}[参数的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1106_16493_x2020087451}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol fr]{lang="NO-BOK"}

[\[Sysname-Serial2/1/0\] fr interface-type dte]{lang="NO-BOK"}

[\[Sysname-Serial2/1/0\] timer-hold 15]{lang="NO-BOK"}
:::
