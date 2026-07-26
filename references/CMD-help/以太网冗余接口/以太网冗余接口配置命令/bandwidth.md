::: {#1742433432 .myid}
[]{#_Toc404796128}[]{#struct_0_x2137_x5306_1216558435}[]{#_Toc384716990}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- bandwidth**

------------------------------------------------------------------------

[**[bandwidth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1765824167}[命令用来配置以太网冗余接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1768347770}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x535027080}

[**[bandwidth]{lang="EN-US"}***[ bandwidth-value]{lang="EN-US"}*]{#struct_0_x2137_x5306_1878106725}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x2101284728}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1178648154}

[[接口的期望带宽为]{style="font-family:宋体"}[10000kbit/s]{lang="EN-US"}]{#struct_0_x2137_x5306_x337310044}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1704387126}

[[以太网冗余接口视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1304658395}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1952630919}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1563436238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x2026303764}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1502727274}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x2137_x5306_x789282478}[：表示接口的期望带宽，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1878172261}

[[接口的期望带宽会影响链路开销值，具体介绍请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x2137_x5306_x1710547424}[路由配置指导"中的"]{style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x250315040}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x710431963}[配置以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的期望带宽为]{style="font-family:宋体"}[50kbit/s]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x1809687033}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] bandwidth 50]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc404796129}[]{#struct_0_x2137_x5306_x1782689181}[]{#_Toc384716991}[]{#_Toc372399732}[]{#_Toc350872177}[]{#_Toc347149590}[]{#_Toc342919787}[]{#_Toc335656811}[]{#_Toc329007815}[]{#_Toc309912009}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x2137_x5306_x829683856}[命令用来恢复以太网冗余接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1298374802}

[**[default]{lang="EN-US"}**]{#struct_0_x2137_x5306_358671204}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1148749280}

[[以太网冗余接口视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1878237797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x533169081}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1326902716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1877970487}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1893611213}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1755309007}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1497279120}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x106972420}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x360707953}[将以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_1878303333}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404796130}[]{#struct_0_x2137_x5306_x2096518712}[]{#_Toc384716992}[]{#_Toc372399733}[]{#_Toc350872178}[]{#_Toc347149591}[]{#_Toc342919788}[]{#_Toc335656812}[]{#_Toc375757511}[]{#_Toc375757512}[]{#_Toc375757513}[]{#_Toc375757514}[]{#_Toc375757515}[]{#_Toc375757516}[]{#_Toc375757517}[]{#_Toc375757518}[]{#_Toc375757519}[]{#_Toc375757520}[]{#_Toc375757521}[]{#_Toc375757525}[]{#_Toc375757526}[]{#_Toc375757527}[]{#_Toc375757528}[]{#_Toc375757529}[]{#_Toc375757530}[]{#_Toc375757532}[]{#_Toc375757533}[]{#_Toc375757535}[]{#_Toc375757536}[]{#_Toc375757537}[]{#_Toc375757538}[]{#_Toc375757539}[]{#_Toc375757540}[]{#_Toc375757541}[]{#_Toc375757542}[]{#_Toc375757543}[]{#_Toc375757544}[]{#_Toc375757545}[]{#_Toc375757546}[]{#_Toc375757547}[]{#_Toc375757548}[]{#_Toc375757549}[]{#_Toc375757550}[]{#_Toc375757551}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x2137_x5306_x745085861}[命令用来配置以太网冗余接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1537232234}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x184221406}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x2137_x5306_1537325283}

[**[undo description]{lang="EN-US"}**]{#struct_0_x2137_x5306_430951982}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1601644671}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"} [Interface]{lang="EN-US"}]{#struct_0_x2137_x5306_1762194958}["，比如：]{style="font-family:宋体"}[Reth-redundancy1 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1382688283}

[[以太网冗余接口视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1933038176}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x162285064}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1877713502}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1626384705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_683499926}

[*[text]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1225185156}[：以太网冗余接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x788188831}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x332292209}[配置以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[master-interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_1914424103}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] description master-interface]{lang="EN-US"}
:::

::: {#-415016280 .myid}
[]{#_Toc404796131}[]{#struct_0_x2137_x5306_1953552141}[]{#_Toc384716989}[]{#_Toc372399730}[]{#_Toc335656814}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- display interface reth**

------------------------------------------------------------------------

[**[display interface reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1974715596}[命令用来显示以太网冗余接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_398700567}

[**[display interface]{lang="EN-US"}**[ \[ **reth** \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}]{#struct_0_x2137_x5306_x797526544}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1877779038}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1095820490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1010659710}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1228739501}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_925851924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1303416113}

[**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1132628360}[：显示以太网冗余接口的相关信息]{style="font-family:宋体"}[.]{lang="EN-US"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_1398838931}[：显示指定以太网冗余接口的信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示以太网冗余接口的编号，取值为已创建的以太网冗余接口的编号。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x2137_x5306_x727272754}[：显示接口的概要信息。不指定该参数时，将显示接口的详细信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x2137_x5306_2076174824}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。不指定该参数时，将不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x2137_x5306_1877844574}[：用来显示用户配置的接口的全部描述信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1209796208}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2137_x5306_x1271395137}**[reth]{lang="EN-US"}**[参数，将显示设备支持的所有接口的相关信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x249805924}[参数，不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示所有]{lang="EN-US" style="font-family:宋体"}[以太网冗余接口]{lang="EN-US" style="font-family:宋体"}[的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_526824451}[参数，同时指定了]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将显示指定]{lang="EN-US" style="font-family:宋体"}[以太网冗余接口]{lang="EN-US" style="font-family:宋体"}[的相关信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x540928651}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1903212165}[显示以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface reth 1]{lang="EN-US"}]{#struct_0_x2137_x5306_1877910110}

[Reth1]{lang="EN-US"}

[Current state: UP]{lang="EN-US"}

[Line protocol state: UP]{lang="EN-US"}

[Description: Reth1 Interface]{lang="EN-US"}

[Bandwidth: 10000kbps]{lang="EN-US"}

[Maximum Transmit Unit: 1500]{lang="EN-US"}

[Internet protocol processing: disabled]{lang="EN-US"}

[IP Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0cda-41b5-cf30]{lang="EN-US"}

[IPv6 Packet Frame Type:PKTFMT_ETHNT_2, Hardware Address: 0cda-41b5-cf30]{lang="EN-US"}

[Physical: Reth, baudrate: 10000000 bps]{lang="EN-US"}

[Last clearing of counters: Never]{lang="EN-US"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="EN-US"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x337955871}[显示]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface reth 1 brief]{lang="EN-US"}]{#struct_0_x2137_x5306_x1811899412}

[Brief information about interfaces in route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[RETH1                DOWN DOWN     \--]{lang="EN-US"}

[[表]{style="font-family:黑体"}[1-3 display interface reth]{lang="EN-US"}]{#struct_0_x2137_x5306_549442785}[[命令显示信息描述表]{style="font-family:黑体"}]{.TableDescriptionChar}

[]{#table_struct_0_x534576052}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_x5306_459914443}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x2020600393}

[[Current state]{lang="EN-US"}]{#struct_0_x2137_x5306_x1637084597}

[[接口当前的物理状态和管理状态，可能的取值及含义如下：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1877975646}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN(Administratively)]{lang="EN-US"}]{#struct_0_x2137_x5306_439128501}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}[shutdown]{lang="EN-US"}[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2137_x5306_x974478914}[：表示该接口的管理状态为开启，但没有成员接口或成员接口物理状态都为]{style="font-family:宋体"}[DOWN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2137_x5306_1185373606}[：表示该接口的管理状态为开启，且至少有一个成员接口物理状态为]{style="font-family:宋体"}[UP]{lang="EN-US"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x2137_x5306_1525613306}

[[接口的链路协议状态，可能的状态及含义如下：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1925419374}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2137_x5306_1908559052}[：该接口的协议状态为开启]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2137_x5306_x72598345}[：该接口的协议状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2137_x5306_1878041182}

[[接口描述信息]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1411498084}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x2137_x5306_1594206593}

[[接口期望带宽，由接]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x970833379}[口下]{style="font-family:宋体"}[bandwidth]{lang="EN-US"}[命令配置]{style="font-family:宋体"}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x2137_x5306_594245531}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1735010940}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x2137_x5306_860221951}

[[网络层协议处理状况。]{style="font-family:宋体"}[disabled]{lang="EN-US"}]{#struct_0_x2137_x5306_x342730970}[表示接口尚未配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，不能处理]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文。当接口配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址之后，本字段将变为"]{style="font-family:宋体"}[Internet Address]{lang="EN-US"}["，后面显示接口配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IP Packet Frame Type]{lang="EN-US"}]{#struct_0_x2137_x5306_1878106718}

[[以太网帧格式]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2100957045}

[[Hardware Address]{lang="EN-US"}]{#struct_0_x2137_x5306_x1854389556}

[[接口的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2137_x5306_157783647}[地址]{style="font-family:宋体"}

[[IPv6 Packet Frame Type]{lang="EN-US"}]{#struct_0_x2137_x5306_x568594521}

[[IPv6]{lang="EN-US"}]{#struct_0_x2137_x5306_1878172254}[报文发送帧格式]{style="font-family:宋体"}

[[Physical]{lang="EN-US"}]{#struct_0_x2137_x5306_x1710875101}

[[接口的类型为]{style="font-family:宋体"}[Reth]{lang="EN-US"}]{#struct_0_x2137_x5306_559487255}

[[baudrate]{lang="EN-US"}]{#struct_0_x2137_x5306_1006263559}

[[接口的波特率为]{style="font-family:宋体"}[10000000bps]{lang="EN-US"}]{#struct_0_x2137_x5306_619818900}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x2137_x5306_1878237790}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_x533365689}[命令清除接口下的统计信息的时间。如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_x2137_x5306_668048194}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2137_x5306_803327391}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的报文数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_x2137_x5306_374907778}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x2137_x5306_1878303326}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"} [packets/sec]{lang="EN-US"}[表示平均每秒输出的报文数]{style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_x2137_x5306_x2096191033}

[[该接口接收的数据报文个数、字节数，以及由于没有接收缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x2137_x5306_2068027597}

[[Output]{lang="EN-US"}]{#struct_0_x2137_x5306_x793675903}

[[该接口发送的数据报文个数、字节数，以及由于没有发送缓冲而被丢弃的报文个数]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x561937353}

[[Brief information on interface(s) under route mode]{lang="EN-US"}]{#struct_0_x2137_x5306_1877713503}

[[三层接口的概要信息]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1626450241}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x2137_x5306_x63622313}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x2137_x5306_1625052810}[Link]{lang="EN-US"}[属性值为"]{lang="EN-US" style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{lang="EN-US" style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复端口本身的物理状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果某接口的]{lang="EN-US" style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x2137_x5306_x296346346}[属性值为"]{lang="EN-US" style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{lang="EN-US" style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口]{lang="EN-US" style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x2137_x5306_x741601538}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x2137_x5306_1877779039}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的网络层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2137_x5306_x1095754954}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x577060976}

[[Link]{lang="EN-US"}]{#struct_0_x2137_x5306_207159705}

[[接口物理连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1436774323}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2137_x5306_1391673936}[：表示本链路物理上是连通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2137_x5306_1877844575}[：表示本链路物理上是不通的]{lang="EN-US" style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x2137_x5306_1209730672}

[[接口协议连接状态，取值可能为：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1117332368}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x2137_x5306_x1750262768}[：该接口的协议状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x2137_x5306_70112734}[：该接口的协议状态为开启]{lang="EN-US" style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x2137_x5306_1877910111}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x2137_x5306_x337890335}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x2137_x5306_x1031871720}

[[接口的描述信息。使用]{style="font-family:宋体"}**[display interface brief]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1783898948}[命令，不指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，该字段最多显示]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符；指定]{style="font-family:宋体"}**[description]{lang="EN-US"}**[参数时，可显示配置的全部描述信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-46245448 .myid}
[]{#_Toc404796132}[]{#struct_0_x2137_x5306_x89631043}[]{#_Toc384716982}[]{#_Toc372399728}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- display reth interface**

------------------------------------------------------------------------

[**[display reth]{lang="DE"}**]{#struct_0_x2137_x5306_1086531015}[ **interface**]{lang="DE"}[命令用来显示以太网冗余接口的成员接口的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1877975647}

[**[display reth interface ]{lang="DE"}[reth]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_439194037}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1793409630}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1023753912}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_237146449}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1905130351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x890231856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x447893277}

[**[reth ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_1356635444}[：表示接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_638901700}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x1115343241}[显示以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display reth interface reth 1]{lang="EN-US"}]{#struct_0_x2137_x5306_1831091092}

[Reth1 :]{lang="EN-US"}

[  Redundancy group  : aa]{lang="EN-US"}

[  Member         Physical status       Forwarding status      Presence status]{lang="EN-US"}

[  GE1/0/1      UP                    Active                 Normal]{lang="EN-US"}

[  GE1/0/2      UP                    Inactive               Normal]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x861882434}[显示以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display reth interface reth 1]{lang="EN-US"}]{#struct_0_x2137_x5306_302713599}

[Reth1 :]{lang="EN-US"}

[  Redundancy group  : aa]{lang="EN-US"}

[  Member         Physical status       Forwarding status      Presence status]{lang="EN-US"}

[  GE1/2/0/1      UP                    Active                 Normal]{lang="EN-US"}

[  GE1/2/0/2      UP                    Inactive               Normal]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display reth]{lang="EN-US"}]{#struct_0_x2137_x5306_348245351}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x513187522}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1878041183}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1411432548}

[[Reth1]{lang="EN-US"}]{#struct_0_x2137_x5306_1280056167}

[[以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}]{#struct_0_x2137_x5306_1061511342}[的信息]{style="font-family:宋体"}

[[Redundancy group]{lang="EN-US"}]{#struct_0_x2137_x5306_162252736}

[[以太网冗余接口所在的冗余组，未加入冗余组时显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}]{#struct_0_x2137_x5306_x994918753}

[[Member]{lang="EN-US"}]{#struct_0_x2137_x5306_x2089123409}

[[成员接口的名称]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1024835387}

[[Physical status]{lang="EN-US"}]{#struct_0_x2137_x5306_2061227279}

[[成员接口的物理状态：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1691318081}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down(redundancy down)]{lang="EN-US"}]{#struct_0_x2137_x5306_1878106719}[：表示该接口被]{lang="EN-US" style="font-family:
  宋体"}[Reth]{lang="EN-US"}[模块]{style="font-family:宋体"}[关闭，即接口状态为冗余关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x2137_x5306_x2101022581}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路关闭）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x2137_x5306_x1249375411}[：该接口的管理状态和物理状态均为开启]{lang="EN-US" style="font-family:宋体"}

[[Forwarding status]{lang="EN-US"}]{#struct_0_x2137_x5306_139215114}

[[成员接口的转发状态：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1453857801}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x2137_x5306_1348061813}[：成员接口可以正常]{lang="EN-US" style="font-family:宋体"}[收]{style="font-family:宋体"}[发]{lang="EN-US" style="font-family:宋体"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x2137_x5306_x93669264}[：成员接口不能]{lang="EN-US" style="font-family:宋体"}[收发报文]{style="font-family:宋体"}

[[Presence status]{lang="EN-US"}]{#struct_0_x2137_x5306_x401683441}

[[成员接口的在位状态：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_730823949}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x2137_x5306_1878172255}[表示在位]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Absent]{lang="EN-US"}]{#struct_0_x2137_x5306_x1710809565}[表示不在位]{lang="EN-US" style="font-family:宋体"}

[]{#_Toc384716983}[ ]{lang="EN-US"}

::: {#896220264 .myid}
[]{#_Toc404796133}[]{#struct_0_x2137_x5306_x786729834}[]{#_Toc384716960}[]{#_Toc372399723}[]{#_Toc364783464}[]{#_Toc384716984}[]{#_Toc385922822}[]{#_Toc385923374}[]{#_Toc384716985}[]{#_Toc385922823}[]{#_Toc385923375}[]{#_Toc384716986}[]{#_Toc385922824}[]{#_Toc385923376}[]{#_Toc384716987}[]{#_Toc385922825}[]{#_Toc385923377}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- interface reth**

------------------------------------------------------------------------

[**[interface]{lang="EN-US"}**[ **reth**]{lang="EN-US"}]{#struct_0_x2137_x5306_x1281616692}[命令用来创建以太网冗余接口并进入该接口视图。]{style="font-family:宋体"}

[**[undo interface reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1730427727}[命令用来删除以太网冗余接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_979409752}

[**[interface]{lang="EN-US"}**[ **reth** *interface-number*]{lang="EN-US"}]{#struct_0_x2137_x5306_464579281}

[**[undo interface reth]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x2137_x5306_1365788162}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1157541529}

[[未创建以太网冗余接口。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1878237791}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x533300153}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1306009012}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1073389404}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1374151753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1530169134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x40352455}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_965002164}[：[]{#_Hlt24806852}接口编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_185912833}

[[删除以太网冗余接口时，如果该接口下存在成员接口，则不允许删除。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1273481673}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1543192603}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1878303327}[创建以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x2096256569}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\]]{lang="EN-US"}
:::

::: {#857643302 .myid}
[]{#_Toc404796134}[]{#struct_0_x2137_x5306_x715276990}[]{#_Toc372399725}[]{#_Toc364783465}[]{#_Toc385922791}[]{#_Toc385923379}[]{#_Toc385922792}[]{#_Toc385923380}[]{#_Toc385922793}[]{#_Toc385923381}[]{#_Toc385922794}[]{#_Toc385923382}[]{#_Toc385922795}[]{#_Toc385923383}[]{#_Toc385922796}[]{#_Toc385923384}[]{#_Toc385922797}[]{#_Toc385923385}[]{#_Toc385922798}[]{#_Toc385923386}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- member interface**

------------------------------------------------------------------------

[**[member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1282360535}[命令用来给以太网冗余]{style="font-family:宋体"}[接口]{style="font-family:宋体"}[添加成员接口。]{style="font-family:宋体"}

[**[undo member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_1710052773}[命令用来将成员接口从以太网冗余]{style="font-family:宋体"}[接口中]{style="font-family:宋体"}[删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_136256501}

[**[member interface ]{lang="EN-US"}***[interface-type interface-number ]{lang="EN-US"}***[priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_x2137_x5306_x716465615}

[**[undo member interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_1648111726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x513755053}

[[以太网冗余]{style="font-family:宋体"}]{#struct_0_x2137_x5306_914108563}[接口下没有任何]{style="font-family:宋体"}[成员接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x535362674}

[[以太网冗余接口]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x671954048}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x851169849}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1854808639}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1963903202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x840716170}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1758046770}[：接口类型和接口编号。]{style="font-family:宋体"}

[*[priority]{lang="EN-US"}*]{#struct_0_x2137_x5306_x543350152}[：成员接口的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1405161735}

[[成员接口的优先级数值越大，优先级越高]{style="font-family:宋体"}]{#struct_0_x2137_x5306_2030409829}[。当两成员接口的链路状态均为]{style="font-family:宋体"}[UP]{lang="EN-US"}[时，系统会让优先级高的成员接口处于激活状态，优先级低的处于非激活状态。激活接口可以收发报文，非激活接口不能收发报文。]{style="font-family:宋体"}

[[以太网冗余接口的成员接口的类型可以为：三层以太网接口、三层]{style="font-family:宋体"}[GigabitEthernet]{lang="EN-US"}]{#struct_0_x2137_x5306_868563293}[接口、三层]{style="font-family:宋体"}[Ten-GigabitEthernet]{lang="EN-US"}[接口、三层]{style="font-family:宋体"}[TwentyGigE]{lang="EN-US"}[接口、三层]{style="font-family:宋体"}[FortyGigE]{lang="EN-US"}[接口、三层]{style="font-family:宋体"}[HundredGigE]{lang="EN-US"}[接口、三层聚合口、]{style="font-family:宋体"}[EFM]{lang="EN-US"}[接口及上述接口的子接口。]{style="font-family:宋体"}

[[每个以太网冗余接口下最多可添加两个成员接口。同一以太网冗余接口的]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2127321185}[成员接口的类型和速率最好相同，例如均为]{style="font-family:宋体"}[100M]{lang="PT-BR"}[三层以太网接口，从而能够保证成员接口切换后不因带宽过窄，影响正常的流量转发。]{style="font-family:宋体"}

[[一个物理接口加入一个以太网冗余接口后，不能加入其它以太网冗余接口。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_567425419}

[[当以太网冗余接口的成员接口包含子接口时，不能指定该以太网冗余接口为]{style="font-family:宋体"}]{#struct_0_x2137_x5306_395835065}[IPv6]{lang="PT-BR"}[静态邻居表项的出接口。关于]{style="font-family:宋体"}[IPv6]{lang="PT-BR"}[静态邻居表项的详细描述请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="PT-BR"}[业务配置指导"中的"]{style="font-family:宋体"}[Ipv6]{lang="PT-BR"}[基础"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_726277163}

[[\# ]{lang="PT-BR"}]{#struct_0_x2137_x5306_x851104313}[给]{style="font-family:宋体"}[以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="PT-BR"}[中添加成员接口]{style="font-family:宋体"}[GigabitEthernet1/0]{lang="PT-BR"}[/1]{lang="EN-US"}[，并指定优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[；添加成员接口]{style="font-family:宋体"}[GigabitEthernet]{lang="NO-BOK"}[1/0/2]{lang="EN-US"}[，并指定优先级为]{style="font-family:宋体"}[50]{lang="EN-US"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_1486167963}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] member interface gigabitethernet 1/0/1 priority 100]{lang="EN-US"}

[\[Sysname-Reth1\] member interface gigabitethernet 1/0/2 priority 50]{lang="EN-US"}

[[\# ]{lang="PT-BR"}]{#struct_0_x2137_x5306_x712058714}[给]{style="font-family:宋体"}[以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="PT-BR"}[中添加成员接口]{style="font-family:宋体"}[GigabitEthernet1/1/0]{lang="PT-BR"}[/1]{lang="EN-US"}[，并指定优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[；添加成员接口]{style="font-family:宋体"}[GigabitEthernet]{lang="NO-BOK"}[1/1/0/2]{lang="EN-US"}[，并指定优先级为]{style="font-family:宋体"}[50]{lang="EN-US"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_1660594281}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] member interface gigabitethernet 1/2/0/1 priority 100]{lang="EN-US"}

[\[Sysname-Reth1\] member interface gigabitethernet 1/2/0/2 priority 50]{lang="EN-US"}
:::

::: {#988247972 .myid}
[]{#_Toc404796135}[]{#struct_0_x2137_x5306_x1357916890}[]{#_Toc384716993}[]{#_Toc372399734}[]{#_Toc350872181}[]{#_Toc347149598}[]{#_Toc342919794}[]{#_Toc335656818}[]{#_Toc317856914}[]{#_Toc309228572}[]{#_Toc13287745}[]{#_Toc384716961}[]{#_Toc385922800}[]{#_Toc385923388}[]{#_Toc384716962}[]{#_Toc385922801}[]{#_Toc385923389}[]{#_Toc384716963}[]{#_Toc385922802}[]{#_Toc385923390}[]{#_Toc384716964}[]{#_Toc385922803}[]{#_Toc385923391}[]{#_Toc384716965}[]{#_Toc385922804}[]{#_Toc385923392}[]{#_Toc384716966}[]{#_Toc385922805}[]{#_Toc385923393}[]{#_Toc384716967}[]{#_Toc385922806}[]{#_Toc385923394}[]{#_Toc384716968}[]{#_Toc385922807}[]{#_Toc385923395}[]{#_Toc384716969}[]{#_Toc385922808}[]{#_Toc385923396}[]{#_Toc384716970}[]{#_Toc385922809}[]{#_Toc385923397}[]{#_Toc384716971}[]{#_Toc385922810}[]{#_Toc385923398}[]{#_Toc384716972}[]{#_Toc385922811}[]{#_Toc385923399}[]{#_Toc384716973}[]{#_Toc385922812}[]{#_Toc385923400}[]{#_Toc384716974}[]{#_Toc385922813}[]{#_Toc385923401}[]{#_Toc384716975}[]{#_Toc385922814}[]{#_Toc385923402}[]{#_Toc384716976}[]{#_Toc385922815}[]{#_Toc385923403}[]{#_Toc384716977}[]{#_Toc385922816}[]{#_Toc385923404}[]{#_Toc384716978}[]{#_Toc385922817}[]{#_Toc385923405}[]{#_Toc384716979}[]{#_Toc385922818}[]{#_Toc385923406}[]{#_Toc384716980}[]{#_Toc385922819}[]{#_Toc385923407}[]{#_Toc384716981}[]{#_Toc385922820}[]{#_Toc385923408}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x2137_x5306_167725423}[命令用来配置以太网冗余接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[（]{style="font-family:宋体"}[Maximum Transmission Unit]{lang="EN-US"}[，最大传输单元）值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1273362509}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1802185477}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x2137_x5306_229993173}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x2137_x5306_x91105723}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_636765781}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x2137_x5306_x997563041}[值为]{style="font-family:宋体"}[1500]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1289799737}

[[以太网冗余接口视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x610973993}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1554019639}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x851038777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x889219462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2009142277}

[*[size]{lang="EN-US"}*]{#struct_0_x2137_x5306_850406859}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，单位为字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1330716079}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x2137_x5306_x338033662}[值影响]{style="font-family:宋体"}[IP]{lang="EN-US"}[协议报文在该接口上传输时的分片与重组。]{style="font-family:宋体"}

[[需要注意的是，配置了]{style="font-family:宋体"}**[mtu]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1198565816}[命令后需要执行命令]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[和]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[，这样该配置才能在接口上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1629719726}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_157749402}[配置以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x988346640}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] mtu 200]{lang="EN-US"}
:::

::: {#2052875588 .myid}
[]{#_Toc404796136}[]{#struct_0_x2137_x5306_x589877821}[]{#_Toc384716988}[]{#_Toc350872182}[]{#_Toc257220493}[]{#_Toc214762440}[]{#_Toc213490054}[]{#_Toc207010309}[]{#_Toc207010042}[]{#_Toc139515326}[]{#_Toc372399729}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- reset counters interface**

------------------------------------------------------------------------

[**[reset counters interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_536585024}[命令用来清除以太网冗余接口的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x39698084}

[**[reset counters interface ]{lang="EN-US"}**[\[ **reth** \[ *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x2137_x5306_x850973241}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_705795353}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x928469338}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1601968844}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1349531746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1219862689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1252203247}

[**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_1104856966}[：清除]{style="font-family:宋体"}[以太网冗余接口]{style="font-family:宋体"}[的统计信息。]{style="font-family:宋体"}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_1737296926}[：]{style="font-family:宋体"}[以太网冗余接口的]{style="font-family:宋体"}[编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x535483356}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_2049070898}

[[如果不指定]{style="font-family:宋体"}**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x850907705}[参数，则清除所有接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_x41172303}[参数而不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[以太网冗余接口]{lang="EN-US" style="font-family:宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}**[reth]{lang="EN-US"}**]{#struct_0_x2137_x5306_1652847858}[参数，同时指定了]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[参数，将清除指定]{lang="EN-US" style="font-family:宋体"}[以太网冗余接口]{lang="EN-US" style="font-family:宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_884863952}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1151891090}[清除]{style="font-family:宋体"}[以太网冗余接口]{style="font-family:宋体"}[Reth]{lang="NO-BOK"}[1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface ]{lang="EN-US"}]{#struct_0_x2137_x5306_x1984450699}[reth ]{lang="NO-BOK"}[1]{lang="EN-US"}
:::

::: {#1170655049 .myid}
[]{#_Toc404796137}[]{#struct_0_x2137_x5306_x1416907798}[]{#_Toc384716994}[]{#_Toc372399735}[]{#_Toc350872248}[]{#_Toc345946921}

**以太网冗余接口 \-- 以太网冗余接口配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1709893782}[命令用来关闭以太网冗余接口。]{style="font-family:宋体"}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2137_x5306_594332007}[命令用来打开以太网冗余接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_234828540}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x2137_x5306_x443033278}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x2137_x5306_x850842169}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1858013653}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1353566019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1703569613}

[[以太网冗余接口视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x978502472}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1996614553}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1242835666}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x961944317}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_39646230}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x1653628512}[关闭以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_385312180}

[\[Sysname\] interface reth 1]{lang="EN-US"}

[\[Sysname-Reth1\] shutdown]{lang="EN-US"}

[ ]{lang="EN-US"}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::::: {#-893184388 .myid}
[]{#_Toc404796140}[]{#struct_0_x2137_x5306_x736120904}[]{#_Toc384717036}[]{#_Toc375743817}

**冗余组 \-- 冗余组配置命令 \-- bind chassis**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](冗余备份命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2137_x5306_450806236}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
楷体_GB2312"}]{#struct_0_x2137_x5306_x1115277705}
:::

[ ]{lang="EN-US"}

[**[bind chassis]{lang="EN-US"}**]{#struct_0_x2137_x5306_x850776633}[命令用来将冗余组节点和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备绑定。]{style="font-family:宋体"}

[**[undo bind chassis]{lang="EN-US"}**]{#struct_0_x2137_x5306_344274701}[命令用来取消冗余组节点和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1881803663}

[**[bind chassis ]{lang="EN-US"}***[chassis-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x163344051}

[**[undo bind chassis]{lang="EN-US"}**]{#struct_0_x2137_x5306_1766585172}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1888524844}

[[冗余组节点未绑定任何成员设备。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x833402569}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1612696527}

[[冗余组节点视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x977670634}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_637076158}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1594711592}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1628687512}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1032929533}

[*[chassis-]{lang="NO-BOK"}[number]{lang="EN-US"}*]{#struct_0_x2137_x5306_1835282469}[：设备在]{style="font-family:宋体"}[IRF]{lang="NO-BOK"}[中的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x59572587}

[[一个冗余组节点只能绑定一个成员设备。冗余组节点和成员设备绑定后，可以将这个成员设备上的部分接口添加到冗余组节点中作为冗余组节点的成员接口。这样，使用两个冗余组节点，就能实现一台成员设备上的部分接口和另一台成员设备上的部分接口互为备份。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x850711097}

[[一个成员设备只能和一个节点绑定。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2051128637}

[[冗余组节点下有成员接口时不能使用该命令修改绑定关系。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2033287654}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_745999268}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_530391862}[将冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[节点]{style="font-family:宋体"}[1]{lang="EN-US"}[与成员设备]{style="font-family:宋体"}[3]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_887076533}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] bind chassis 3]{lang="EN-US"}
:::::

::::: {#1778129723 .myid}
[]{#_Toc404796141}[]{#struct_0_x2137_x5306_1613605650}

**冗余组 \-- 冗余组配置命令 \-- bind slot**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](冗余备份命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2137_x5306_1361142448}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
楷体_GB2312"}]{#struct_0_x2137_x5306_x554681113}
:::

[ ]{lang="EN-US"}

[**[bind slot]{lang="EN-US"}**]{#struct_0_x2137_x5306_x179732944}[命令用来将冗余组节点和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备绑定。]{style="font-family:宋体"}

[**[undo bind slot]{lang="EN-US"}**]{#struct_0_x2137_x5306_x308708651}[命令用来取消冗余组节点和]{style="font-family:宋体"}[IRF]{lang="EN-US"}[成员设备的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x287271334}

[**[bind slot ]{lang="EN-US"}***[slot-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x839796512}

[**[undo bind slot]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1085277823}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1318271742}

[[冗余组节点未绑定任何成员设备。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_268275920}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_316029588}

[[冗余组节点视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1900319255}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1849737859}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_2028650160}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1393350749}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x740760416}

[*[slot-]{lang="NO-BOK"}[number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1874792592}[：设备在]{style="font-family:宋体"}[IRF]{lang="NO-BOK"}[中的成员编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1206433274}

[[一个冗余组节点只能绑定一个成员设备。冗余组节点和成员设备绑定后，可以将这个成员设备上的部分接口添加到冗余组节点中作为冗余组节点的成员接口。这样，使用两个冗余组节点，就能实现一台成员设备上的部分接口和另一台成员设备上的部分接口互为备份。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x525877594}

[[一个成员设备只能和一个节点绑定。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x4485815}

[[冗余组节点下有成员接口时不能使用该命令修改绑定关系。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x112416979}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1513309224}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1877382823}[将冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[节点]{style="font-family:宋体"}[1]{lang="EN-US"}[与成员设备]{style="font-family:宋体"}[1]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_408624738}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] bind slot 1]{lang="EN-US"}
:::::

::: {#1646413827 .myid}
[]{#_Toc404796142}[]{#struct_0_x2137_x5306_1950198875}[]{#_Toc384717074}[]{#_Toc375743824}[]{#_Toc372399743}[]{#_Toc364783477}[]{#_Toc385922902}[]{#_Toc385923415}[]{#_Toc385922903}[]{#_Toc385923416}[]{#_Toc385922904}[]{#_Toc385923417}[]{#_Toc385922905}[]{#_Toc385923418}[]{#_Toc385922906}[]{#_Toc385923419}[]{#_Toc385922907}[]{#_Toc385923420}[]{#_Toc385922908}[]{#_Toc385923421}[]{#_Toc385922909}[]{#_Toc385923422}[]{#_Toc385922910}[]{#_Toc385923423}[]{#_Toc385922911}[]{#_Toc385923424}[]{#_Toc385922912}[]{#_Toc385923425}[]{#_Toc385922913}[]{#_Toc385923426}

**冗余组 \-- 冗余组配置命令 \-- display redundancy group**

------------------------------------------------------------------------

[**[display redundancy group]{lang="EN-US"}**]{#struct_0_x2137_x5306_x674051635}[命令用来显示冗余组的相关信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1974242562}

[]{#struct_0_x2137_x5306_697245313}[]{#_Toc168716193}[]{#_Toc148450109}[]{#_Toc136938063}[]{#_Toc96758137}[]{#_Toc31795070}[**[display ]{lang="EN-US"}**]{#_Toc505401507}**[redundancy ]{lang="EN-US"}[group]{lang="EN-US"}***[ ]{lang="EN-US"}*[\[ *group-name* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1229884316}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1211064427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1339041901}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1545008383}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1376800735}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x850645561}

[*[group-name]{lang="EN-US"}*]{#struct_0_x2137_x5306_1497148358}[：冗余组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1545515963}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_854090763}[显示冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的相关信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display redundancy group aaa]{lang="EN-US"}]{#struct_0_x2137_x5306_x711993178}

[Redundancy group aaa (ID 1):]{lang="EN-US"}

[  Node ID      Slot        Priority   Status           Track weight]{lang="EN-US"}

[  1            Slot1       100        Secondary        -255]{lang="EN-US"}

[  2            Slot2       99         Primary          255]{lang="EN-US"}

[ ]{lang="EN-US"}

[Preempt delay time remained   : 0    min]{lang="EN-US"}

[Preempt delay timer setting   : 1    min]{lang="EN-US"}

[Remaining hold-down time      : 0    sec]{lang="EN-US"}

[Hold-down timer setting       : 300  sec]{lang="EN-US"}

[Manual switchover request     : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[Member interfaces:]{lang="EN-US"}

[    Reth1          Reth2]{lang="EN-US"}

[Member failover groups:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Node 1:]{lang="EN-US"}

[  Node member     Physical status]{lang="EN-US"}

[    GE1/0/2       DOWN]{lang="EN-US"}

[    GE1/0/4       DOWN(redundancy down)]{lang="EN-US"}

[  Track info:]{lang="EN-US"}

[    Track    Status       Reduced weight     Interface]{lang="EN-US"}

[    1        Negative     255                GE1/0/2(Fault)]{lang="EN-US"}

[    2        Negative     255                GE1/0/4]{lang="EN-US"}

[Node 2:]{lang="EN-US"}

[  Node member    Physical status]{lang="EN-US"}

[    GE2/0/2   UP]{lang="EN-US"}

[    GE2/0/4    UP]{lang="EN-US"}

[  Track info]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Track    Status       Reduced weight     Interface]{lang="EN-US"}

[    3        Positive     55                 GE2/0/2]{lang="EN-US"}

[    4        Positive     55                 GE2/0/4]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_538174815}[显示冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的相关信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display redundancy group aaa]{lang="EN-US"}]{#struct_0_x2137_x5306_x850580025}

[Redundancy group aaa (ID 1):]{lang="EN-US"}

[  Node ID      Chassis        Priority   Status           Track weight]{lang="EN-US"}

[  1            Chassis1       100        Secondary        -255]{lang="EN-US"}

[  2            Chassis2       99         Primary          255]{lang="EN-US"}

[ ]{lang="EN-US"}

[Preempt delay time remained   : 0    min]{lang="EN-US"}

[Preempt delay timer setting   : 1    min]{lang="EN-US"}

[Remaining hold-down time      : 0    sec]{lang="EN-US"}

[Hold-down timer setting       : 300  sec]{lang="EN-US"}

[Manual switchover request     : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[Member interfaces:]{lang="EN-US"}

[    Reth1          Reth2]{lang="EN-US"}

[Member failover groups:]{lang="EN-US"}

[    groupa]{lang="EN-US"}

[    groupabc]{lang="EN-US"}

[ ]{lang="EN-US"}

[Node 1:]{lang="EN-US"}

[  Node member     Physical status]{lang="EN-US"}

[    GE1/1/0/2     DOWN]{lang="EN-US"}

[    GE1/1/0/4     DOWN(redundancy down)]{lang="EN-US"}

[  Track info:]{lang="EN-US"}

[    Track    Status       Reduced weight     Interface]{lang="EN-US"}

[    1        Negative     255                GE1/1/0/2(Fault)]{lang="EN-US"}

[    2        Negative     255                GE1/1/0/4]{lang="EN-US"}

[Node 2:]{lang="EN-US"}

[  Node member    Physical status]{lang="EN-US"}

[    GE2/1/0/2    UP]{lang="EN-US"}

[    GE2/1/0/4    UP]{lang="EN-US"}

[  Track info]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Track    Status       Reduced weight     Interface]{lang="EN-US"}

[    3        Positive     55                 GE2/1/0/2]{lang="EN-US"}

[    4        Positive     55                 GE2/1/0/4]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display redundancy group]{lang="EN-US"}]{#struct_0_x2137_x5306_706802280}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x516822732}[[字段]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1601297540}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1950136594}

[[Redundancy group aaa (ID 1)]{lang="EN-US"}]{#struct_0_x2137_x5306_x1428264631}

[[冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}]{#struct_0_x2137_x5306_1365383172}[（该冗余组的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Node ID]{lang="EN-US"}]{#struct_0_x2137_x5306_1110487487}

[[冗余组节点的编号]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x851169848}

[[Chassis]{lang="EN-US"}]{#struct_0_x2137_x5306_1854874175}

[[节点绑定的成员设备的编号（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2137_x5306_1233211810}[模式）]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x2137_x5306_94575876}

[[节点绑定的成员设备的编号（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2137_x5306_x1699748356}[设备）]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x2137_x5306_1419944129}

[[节点的优先级]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1641490840}

[[Status]{lang="EN-US"}]{#struct_0_x2137_x5306_1761327373}

[[对应节点当前所处的状态：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1284799444}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Primary]{lang="EN-US"}]{#struct_0_x2137_x5306_x851104312}[：当前]{lang="EN-US" style="font-family:宋体"}[节点]{style="font-family:宋体"}[为主节点，能够正常收发报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Secondary]{lang="EN-US"}]{#struct_0_x2137_x5306_1486233499}[：当前节点为备节点；当优先级高的节点为备节点时，节点上的所有成员接口会被冗余组强制设置为]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}[状态，不能收发报文；当优先级低的节点为备节点时，节点的所有成员接口能够正常收发报文，为主节点分担流量]{lang="EN-US" style="font-family:宋体"}

[[Track weight]{lang="EN-US"}]{#struct_0_x2137_x5306_556663568}

[[节点的当前权重值]{style="font-family:宋体"}]{#struct_0_x2137_x5306_821201548}

[[Preempt delay time remained]{lang="EN-US"}]{#struct_0_x2137_x5306_x285377401}

[[剩余的倒回延时，单位为分钟]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x754277798}

[[Preempt delay timer setting]{lang="EN-US"}]{#struct_0_x2137_x5306_872333730}

[[配置的倒回延时，单位为分钟]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1578510034}

[[Remaining hold-down time]{lang="EN-US"}]{#struct_0_x2137_x5306_x1470027030}

[[剩余的状态保持时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x851038776}

[[Hold-down timer setting]{lang="EN-US"}]{#struct_0_x2137_x5306_x889284998}

[[配置的状态保持时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1927747243}

[[Manual switchover request]{lang="EN-US"}]{#struct_0_x2137_x5306_x2072592664}

[[手工倒换请求，取值为：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1526681939}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_x2137_x5306_290904142}[：表示存在手动倒换请求]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x2137_x5306_x850973240}[：表示无倒换请求]{lang="EN-US" style="font-family:宋体"}

[[Member interfaces]{lang="EN-US"}]{#struct_0_x2137_x5306_705729817}

[[冗余组中添加的以太网冗余接口]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x219500506}

[[Member failover groups]{lang="EN-US"}]{#struct_0_x2137_x5306_x301739394}

[[冗余组中添加的备份组]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x850907704}

[[Node 1]{lang="EN-US"}]{#struct_0_x2137_x5306_x41106767}

[[冗余组节点的详细信息]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x690207151}

[[Node member]{lang="EN-US"}]{#struct_0_x2137_x5306_x637953510}

[[冗余组节点的成员接口]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1267488657}

[[Physical status]{lang="EN-US"}]{#struct_0_x2137_x5306_x1468027285}

[[成员接口的物理状态：]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x850842168}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down(redundancy down)]{lang="EN-US"}]{#struct_0_x2137_x5306_1858079189}[：表示该接口被]{lang="EN-US" style="font-family:
  宋体"}[Reth]{lang="EN-US"}[模块]{style="font-family:宋体"}[关闭，即接口状态为冗余关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x2137_x5306_2051757382}[：表示该接口的管理状态为开启，但物理状态为关闭（可能因为没有物理连线或者线路关闭）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x2137_x5306_1383655468}[：该接口的管理状态和物理状态均为开启]{lang="EN-US" style="font-family:宋体"}

[[Track info]{lang="EN-US"}]{#struct_0_x2137_x5306_x60965327}

[[冗余组节点关联的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_x1127121653}[项的信息]{style="font-family:宋体"}

[[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_x850776632}

[[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_344209165}[项的编号]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x2137_x5306_1200467946}

[[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_x286883533}[项的状态]{style="font-family:宋体"}

[[Reduced weight]{lang="EN-US"}]{#struct_0_x2137_x5306_x1268395820}

[[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_1844379043}[项的当前权重值]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x2137_x5306_x850711096}

[[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_x2033353190}[项的关联接口，如果显示为]{style="font-family:宋体"}[Fault]{lang="EN-US"}[，则表示该接口已故障；如果显示为]{style="font-family:宋体"}[Absent]{lang="EN-US"}[，则表示该接口当前不在位]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#947372872 .myid}
[]{#_Toc404796143}[]{#struct_0_x2137_x5306_x1712132902}[]{#_Toc384717063}

**冗余组 \-- 冗余组配置命令 \-- hold-down-interval**

------------------------------------------------------------------------

[**[hold-down-interval]{lang="EN-US"}**]{#struct_0_x2137_x5306_1219488406}[命令用来指定冗余组节点状态的保持时间，这段时间内不能发生主备倒换。]{style="font-family:宋体"}

[**[undo hold-down-interval]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_x1919112839}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_694345237}

[[保持时间为]{style="font-family:宋体"}]{#struct_0_x2137_x5306_630865054}[1]{lang="NO-BOK"}[秒。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2080769339}

[**[hold-down-interval]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_2030254742}[ ]{lang="NO-BOK"}*[second]{lang="NO-BOK"}*

[**[undo hold-down-interval]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_x668322328}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1590228426}

[[冗余组视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x850645560}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1497213894}

[[network-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x2044462315}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x603101309}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_86467961}

[*[second]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1872398019}[：保持时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_547906260}

[[当网络不稳定，监测接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x2137_x5306_x1701835463}[链路状态频繁改变，会导致]{style="font-family:宋体"}[Track]{lang="EN-US"}[项状态在短时间内频繁改变，连带导致冗余组需要不断的响应主备倒换事件，使用保持定时器可以避免这种情况的发生。当节点完成主备倒换后，系统启动保持定时器。在保持时间内，不允许再次发生主备倒换。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x953190881}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_21230078}[将冗余节点的状态保持时间配置为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x148066521}

[\[Sysname\] redundancy group aa]{lang="EN-US"}

[\[Sysname-redundancy-group-aa\] hold-down-interval 300]{lang="EN-US"}
:::

::::: {#1212021666 .myid}
[]{#_Toc404796144}[]{#struct_0_x2137_x5306_x1837148982}[]{#_Toc384717013}[]{#_Toc375743814}[]{#_Toc385922946}[]{#_Toc385923429}[]{#_Toc385922947}[]{#_Toc385923430}[]{#_Toc385922948}[]{#_Toc385923431}[]{#_Toc385922949}[]{#_Toc385923432}[]{#_Toc384717064}[]{#_Toc385922950}[]{#_Toc385923433}[]{#_Toc384717065}[]{#_Toc385922951}[]{#_Toc385923434}[]{#_Toc384717066}[]{#_Toc385922952}[]{#_Toc385923435}[]{#_Toc384717067}[]{#_Toc385922953}[]{#_Toc385923436}

**冗余组 \-- 冗余组配置命令 \-- member failover group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](冗余备份命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2137_x5306_854156299}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
楷体_GB2312"}]{#struct_0_x2137_x5306_x1547340836}
:::

[ ]{lang="EN-US"}

[**[member failover group]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1424518359}[命令用来将备份组加入冗余组。]{style="font-family:宋体"}

[**[undo member failover group]{lang="EN-US"}**]{#struct_0_x2137_x5306_254392958}[命令用来将备份组从冗余组下删除。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x850580024}

[**[member failover group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x2137_x5306_706867816}

[**[undo member failover group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_x2137_x5306_1977455686}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_229610076}

[[冗余组下没有备份组。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1134081083}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_619475563}

[[冗余组视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x691365901}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x589855820}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1695124598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_665594608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1897286792}

[*[group-name]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1205124580}[：备份组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x861422299}

[[一个备份组只能加入一个冗余组。备份组加入冗余组后主备倒换受冗余组的影响。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1428294273}

[[一个冗余组下最多可以加入]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_x2137_x5306_x851169847}[个备份组，且必须是已经创建的备份组。否则，本命令将执行失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1855201855}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_2045817019}[将备份组]{style="font-family:宋体"}[bb]{lang="EN-US"}[加入冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x552538297}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] member failover group bb]{lang="EN-US"}
:::::

::: {#-1347435832 .myid}
[]{#_Toc404796145}[]{#struct_0_x2137_x5306_702453576}[]{#_Toc384717005}[]{#_Toc375743813}[]{#_Toc372399739}[]{#_Toc364783472}[]{#_Toc385922860}[]{#_Toc385923438}[]{#_Toc385922861}[]{#_Toc385923439}[]{#_Toc385922862}[]{#_Toc385923440}[]{#_Toc385922863}[]{#_Toc385923441}[]{#_Toc384717014}[]{#_Toc385922864}[]{#_Toc385923442}[]{#_Toc384717015}[]{#_Toc385922865}[]{#_Toc385923443}[]{#_Toc384717016}[]{#_Toc385922866}[]{#_Toc385923444}[]{#_Toc384717017}[]{#_Toc385922867}[]{#_Toc385923445}[]{#_Toc384717018}[]{#_Toc385922868}[]{#_Toc385923446}[]{#_Toc384717019}[]{#_Toc385922869}[]{#_Toc385923447}[]{#_Toc384717020}[]{#_Toc385922870}[]{#_Toc385923448}

**冗余组 \-- 冗余组配置命令 \-- member interface**

------------------------------------------------------------------------

[**[member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1468220436}[命令用来将以太网冗余接口加入冗余组。]{style="font-family:宋体"}

[**[undo member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_1115020486}[命令用来将以太网冗余接口从冗余组下删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1657797347}

[**[member interface reth]{lang="EN-US"}**[ ]{lang="EN-US"}*[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_29479048}

[**[undo member interface reth ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x712613565}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1935575793}

[[冗余组下没有添加以太网冗余接口。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x289887964}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1473141955}

[[冗余组视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1462127995}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1732404992}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x851104311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1486299035}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_585320308}

[**[reth ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x2147436922}[：以太网冗余接口的编号。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2094976243}

[[一个以太网冗余接口只能加入一个冗余组。以太网冗余接口加入冗余组后主备倒换受冗余组的影响。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_318714901}

[[一个冗余组下最多可以加入]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_x2137_x5306_1452228245}[个以太网冗余接口，且必须是已经创建的以太网冗余接口。否则，本命令将执行失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_910084655}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1969761203}[将以太网冗余接口]{style="font-family:宋体"}[Reth1]{lang="EN-US"}[加到冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x109197306}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] member interface reth 1]{lang="EN-US"}
:::

::: {#1985170616 .myid}
[]{#_Toc404796146}[]{#struct_0_x2137_x5306_x952676688}[]{#_Toc384717021}[]{#_Toc375743815}[]{#_Toc385922848}[]{#_Toc385923450}[]{#_Toc385922849}[]{#_Toc385923451}[]{#_Toc385922850}[]{#_Toc385923452}[]{#_Toc385922851}[]{#_Toc385923453}[]{#_Toc384717006}[]{#_Toc385922852}[]{#_Toc385923454}[]{#_Toc384717007}[]{#_Toc385922853}[]{#_Toc385923455}[]{#_Toc384717008}[]{#_Toc385922854}[]{#_Toc385923456}[]{#_Toc384717009}[]{#_Toc385922855}[]{#_Toc385923457}[]{#_Toc384717010}[]{#_Toc385922856}[]{#_Toc385923458}[]{#_Toc384717011}[]{#_Toc385922857}[]{#_Toc385923459}[]{#_Toc384717012}[]{#_Toc385922858}[]{#_Toc385923460}

**冗余组 \-- 冗余组配置命令 \-- node**

------------------------------------------------------------------------

[**[node]{lang="EN-US"}**]{#struct_0_x2137_x5306_1170814769}[命令用来创建冗余组节点，并进入冗余组节点视图。]{style="font-family:宋体"}

[**[undo node]{lang="EN-US"}**]{#struct_0_x2137_x5306_x851038775}[命令用来删除冗余组节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x889088390}

[**[node ]{lang="EN-US"}***[node-id]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1900568795}

[**[undo node ]{lang="EN-US"}***[node-id]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1821316980}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x195232276}

[[未创建任何冗余组节点。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x654820282}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x76942572}

[[冗余组视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1813944244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1060602924}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_490749909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_135997655}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x270964659}

[[node-id]{lang="EN-US"}]{#struct_0_x2137_x5306_x850973239}[：表示冗余组节点编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_705271068}

[[每个冗余组下最多可创建两个冗余组节点，这两个冗余组节点为主备关系。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_78318270}

[[当冗余组节点绑定了]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2137_x5306_1276094159}[成员设备时，不能删除该冗余组节点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_922683254}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x192660566}[在冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[下，创建冗余组节点]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_645801577}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}
:::

::: {#-237404391 .myid}
[]{#_Toc404796147}[]{#struct_0_x2137_x5306_1740947588}[]{#_Toc384717022}[]{#_Toc375743816}[]{#_Toc385922872}[]{#_Toc385923462}[]{#_Toc385922873}[]{#_Toc385923463}[]{#_Toc385922874}[]{#_Toc385923464}[]{#_Toc385922875}[]{#_Toc385923465}[]{#_Toc385922876}[]{#_Toc385923466}[]{#_Toc385922877}[]{#_Toc385923467}[]{#_Toc385922878}[]{#_Toc385923468}[]{#_Toc385922879}[]{#_Toc385923469}[]{#_Toc385922880}[]{#_Toc385923470}[]{#_Toc385922881}[]{#_Toc385923471}

**冗余组 \-- 冗余组配置命令 \-- node-member interface**

------------------------------------------------------------------------

[**[node-member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_x941753425}[命令用来为冗余组节点添加成员接口。]{style="font-family:宋体"}

[**[undo node-member interface]{lang="EN-US"}**]{#struct_0_x2137_x5306_756128984}[命令用来将成员接口从冗余]{style="font-family:
宋体"}[节点中]{style="font-family:宋体"}[删除。]{style="font-family:宋体"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x280819254}

[[冗余组节点下不存在任何成员接口。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x850907703}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x41565519}

[**[node-member interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x941674313}

[**[undo node-member interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x27771101}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1373729272}

[[冗余组节点视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_151539936}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1526216070}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1688843538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x68467128}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_179681742}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1623602111}[：接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1020504646}

[[执行本命令前，请先执行]{style="font-family:宋体"}**[bind chassis]{lang="EN-US"}**]{#struct_0_x2137_x5306_x850842167}[或]{style="font-family:宋体"}**[bind slot]{lang="EN-US"}**[命令。否则，本命令执行失败。]{style="font-family:宋体"}

[[本命令中加入的成员接口必须是冗余组节点绑定的]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x2137_x5306_1858144725}[成员设备上的接口。]{style="font-family:宋体"}

[[一个冗余组节点下最多可添加]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_x2137_x5306_949899908}[个成员接口，但是这些成员接口不能是聚合口和子接口，不能是以太网冗余接口的成员接口。]{style="font-family:宋体"}

[[一个接口加入一个冗余组节点后，就不能再加入其它的冗余组节点]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1325293091}[[。]{style="font-size:9.0pt;font-family:宋体"}]{.TableTextChar}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x285634070}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1218516889}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[加到冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的节点]{style="font-family:宋体"}[1]{lang="EN-US"}[中。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_411889088}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\]node-member interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x1115146633}[将接口]{style="font-family:宋体"}[GigabitEthernet1/2/0/1]{lang="EN-US"}[加到冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的节点]{style="font-family:宋体"}[1]{lang="EN-US"}[中。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_1065439842}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\]node-member interface gigabitethernet 1/2/0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_763962119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bind chassis]{lang="EN-US"}**]{#struct_0_x2137_x5306_1462011340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bind slot]{lang="EN-US"}**]{#struct_0_x2137_x5306_x257243029}
:::

::: {#1451789774 .myid}
[]{#_Toc404796148}[]{#struct_0_x2137_x5306_x838078798}[]{#_Toc384717058}[]{#_Toc385922883}[]{#_Toc385923473}[]{#_Toc385922884}[]{#_Toc385923474}[]{#_Toc385922885}[]{#_Toc385923475}[]{#_Toc385922886}[]{#_Toc385923476}[]{#_Toc385922887}[]{#_Toc385923477}[]{#_Toc384717023}[]{#_Toc385922888}[]{#_Toc385923478}[]{#_Toc384717024}[]{#_Toc385922889}[]{#_Toc385923479}[]{#_Toc384717025}[]{#_Toc385922890}[]{#_Toc385923480}[]{#_Toc384717026}[]{#_Toc385922891}[]{#_Toc385923481}[]{#_Toc384717027}[]{#_Toc385922892}[]{#_Toc385923482}[]{#_Toc384717028}[]{#_Toc385922893}[]{#_Toc385923483}[]{#_Toc384717029}[]{#_Toc385922894}[]{#_Toc385923484}[]{#_Toc384717030}[]{#_Toc385922895}[]{#_Toc385923485}[]{#_Toc384717031}[]{#_Toc385922896}[]{#_Toc385923486}[]{#_Toc384717032}[]{#_Toc385922897}[]{#_Toc385923487}[]{#_Toc384717033}[]{#_Toc385922898}[]{#_Toc385923488}[]{#_Toc384717034}[]{#_Toc385922899}[]{#_Toc385923489}[]{#_Toc384717035}[]{#_Toc385922900}[]{#_Toc385923490}

**冗余组 \-- 冗余组配置命令 \-- preempt-delay**

------------------------------------------------------------------------

[**[preempt-delay]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_x379091330}[命令用来指定冗余组节点的倒回延时。]{style="font-family:宋体"}

[**[undo preempt-delay]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_1332645121}[命令用来恢复情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x850776631}

[**[preempt-delay]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_344405773}[ ]{lang="NO-BOK"}*[delay-time]{lang="NO-BOK"}*

[**[undo preempt-delay]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_1109128266}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x2122004315}

[[倒回延时为]{style="font-family:宋体"}]{#struct_0_x2137_x5306_952715448}[1]{lang="NO-BOK"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1472364388}

[[冗余组]{style="font-family:宋体"}]{#struct_0_x2137_x5306_649267086}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1769028092}

[[network-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x205672724}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x1729165204}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x379744223}

[*[delay-time]{lang="NO-BOK"}*]{#struct_0_x2137_x5306_166253840}[：冗余组将业务倒回到高优先级节点的等待时间，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="NO-BOK"}[～]{style="font-family:宋体"}[12]{lang="NO-BOK"}[，单位为分钟，]{style="font-family:宋体"}[配置为]{style="font-family:宋体"}[0]{lang="NO-BOK"}[时表示不倒回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x850711095}

[[当冗余组内优先级高的节点倒回条件就绪时（譬如故障恢复），会触发倒回事件，但启动倒回定时器。由于需要整体倒回，在冗余组倒回的过程中会同时触发很多事件（比如接口状态变化等），这些事件的处理需要时间。倒回定时器能够为冗余组提供一段时间，让节点准备完毕后，再将业务从优先级低的节点倒换到优先级高的节点。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2033418726}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_318181714}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x164246699}[配置冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的倒回等待时间为]{style="font-family:宋体"}[2]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x1498948549}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] preempt-delay 2]{lang="EN-US"}
:::

::: {#567732879 .myid}
[]{#_Toc404796149}[]{#struct_0_x2137_x5306_x1337406257}[]{#_Toc384717037}[]{#_Toc375743818}[]{#_Toc384717059}[]{#_Toc385922941}[]{#_Toc385923492}[]{#_Toc384717060}[]{#_Toc385922942}[]{#_Toc385923493}[]{#_Toc384717061}[]{#_Toc385922943}[]{#_Toc385923494}[]{#_Toc384717062}[]{#_Toc385922944}[]{#_Toc385923495}

**冗余组 \-- 冗余组配置命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_x2137_x5306_968222278}[命令用来配置冗余组节点的优先级。]{style="font-family:宋体"}

[**[undo priority]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1651921907}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x168032331}

[**[priority ]{lang="EN-US"}***[priority]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1378743913}

[**[undo priority]{lang="EN-US"}**]{#struct_0_x2137_x5306_x850645559}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1496624071}

[[冗余组节点的优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x2137_x5306_1856842448}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1087453911}

[[冗余组节点视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_47317586}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_811968920}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_723406505}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_102020241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x432792233}

[*[priority]{lang="EN-US"}*]{#struct_0_x2137_x5306_1984482287}[：优先级的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x850580023}

[[冗余组节点的优先级数值越大，节点的优先级越高。缺省情况下，优先级高的冗余组节点为主节点，优先级低的为备节点。当冗余组下两个节点优先级相同时，编号小的为主节点，编号大的为备节点。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_706409064}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x492815798}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_550536321}[将冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[节点]{style="font-family:宋体"}[1]{lang="EN-US"}[的优先级设置为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x2057855380}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] priority 3]{lang="EN-US"}
:::

::: {#-360577910 .myid}
[]{#_Toc404796150}[]{#struct_0_x2137_x5306_441606651}[]{#_Toc384716997}[]{#_Toc375743812}[]{#_Toc372399738}[]{#_Toc364783471}[]{#_Toc385922915}[]{#_Toc385923497}[]{#_Toc385922916}[]{#_Toc385923498}[]{#_Toc385922917}[]{#_Toc385923499}[]{#_Toc385922918}[]{#_Toc385923500}[]{#_Toc385922919}[]{#_Toc385923501}[]{#_Toc384717038}[]{#_Toc385922920}[]{#_Toc385923502}[]{#_Toc384717039}[]{#_Toc385922921}[]{#_Toc385923503}[]{#_Toc384717040}[]{#_Toc385922922}[]{#_Toc385923504}[]{#_Toc384717041}[]{#_Toc385922923}[]{#_Toc385923505}

**冗余组 \-- 冗余组配置命令 \-- redundancy group**

------------------------------------------------------------------------

[**[redundancy group]{lang="EN-US"}**]{#struct_0_x2137_x5306_1248713049}[命令用来创建冗余组并进入该冗余组视图。]{style="font-family:宋体"}

[**[undo redundancy group]{lang="EN-US"}**]{#struct_0_x2137_x5306_1712180958}[命令用来删除冗余组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1214383368}

[**[redundancy group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_x2137_x5306_x800807051}

[**[undo redundancy group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_x2137_x5306_x851169846}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1855267391}

[[设备上不存在任何冗余组。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1880689395}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_446010745}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x523407712}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x661615427}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1044158326}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_189388401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1383912944}

[[group-name]{lang="EN-US"}]{#struct_0_x2137_x5306_x1114635803}[：冗余组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x150710220}

[[如果冗余组不存在，则先创建该冗余组，再进入该冗余组视图。如果冗余组已经创建，则直接进入该冗余组视图。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x404622674}

[[多次执行该命令可创建多个冗余组，最多可创建]{style="font-family:宋体"}[255]{lang="EN-US"}]{#struct_0_x2137_x5306_x1080424337}[个。]{style="font-family:宋体"}

[[当冗余组中还有冗余接口或者冗余组节点时，不能删除该冗余组。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x851104310}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1486364571}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x630109696}[创建名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的冗余组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_823136835}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}
:::

::: {#-933077269 .myid}
[]{#_Toc404796151}[]{#struct_0_x2137_x5306_1305246997}

**冗余组 \-- 冗余组配置命令 \-- snmp-agent trap enable redundancy**

------------------------------------------------------------------------

[**[snmp-agent trap enable rddc]{lang="EN-US"}**]{#struct_0_x2137_x5306_2019954009}[命令用来开启冗余组告警功能。]{style="font-family:
宋体"}

[**[undo snmp-agent trap enable rddc]{lang="EN-US"}**]{#struct_0_x2137_x5306_1305246996}[命令用来关闭冗余组告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2019888473}

[**[snmp-agent trap enable rddc]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1776968581}

[**[undo snmp-agent trap enable rddc]{lang="EN-US"}**]{#struct_0_x2137_x5306_1305246995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2019822937}

[[冗余组告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_1305246994}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2019757401}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_602565920}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1305246993}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_2020216153}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1305246992}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2020150617}

[[开启冗余组告警功能后，在冗余组人工倒换、故障接口恢复、故障接口生成时，会生成告警信息，并将该信息发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x2137_x5306_x1985009923}[模块。通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关特性。]{style="font-family:宋体"}

[[有关告警信息的详细描述，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x2137_x5306_1305246991}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_2020085081}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_x253592296}[开启冗余组告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x461436611}

[\[Sysname\] snmp-agent trap enable rddc]{lang="EN-US"}
:::

::: {#1027014707 .myid}
[]{#_Toc404796152}[]{#struct_0_x2137_x5306_x490089504}[]{#_Toc384717068}[]{#_Toc385922836}[]{#_Toc385923507}[]{#_Toc385922837}[]{#_Toc385923508}[]{#_Toc385922838}[]{#_Toc385923509}[]{#_Toc385922839}[]{#_Toc385923510}[]{#_Toc384716998}[]{#_Toc385922840}[]{#_Toc385923511}[]{#_Toc384716999}[]{#_Toc385922841}[]{#_Toc385923512}[]{#_Toc384717000}[]{#_Toc385922842}[]{#_Toc385923513}[]{#_Toc384717001}[]{#_Toc385922843}[]{#_Toc385923514}[]{#_Toc384717002}[]{#_Toc385922844}[]{#_Toc385923515}[]{#_Toc384717003}[]{#_Toc385922845}[]{#_Toc385923516}[]{#_Toc384717004}[]{#_Toc385922846}[]{#_Toc385923517}

**冗余组 \-- 冗余组配置命令 \-- switchover request**

------------------------------------------------------------------------

[**[switchover request]{lang="EN-US"}**]{#struct_0_x2137_x5306_1492257742}[命令用来手工触发指定冗余组进行主备倒换，让冗余组工作在优先级低的节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x602944114}

[**[switchover request]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_x327695311}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1932287032}

[[冗余组视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1743782874}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1368637619}

[[network-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_421561286}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x757790800}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1611468117}

[[当冗余组主备结点无故障]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x851038774}[，]{style="font-family:宋体"}[业务运行在优先级高的节点时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[用户可通过此命令触发冗余组主备倒换]{style="font-family:宋体"}[，让]{style="font-family:宋体"}[业务运行到备结点]{style="font-family:宋体"}[，以便]{style="font-family:宋体"}[用户可更换主节点上的部件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x889153926}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1149554634}[手工触发指定冗余组的主备倒换。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x1857654586}

[\[Sysname\] redundancy group aa]{lang="EN-US"}

[\[Sysname-redundancy-group-aa\] switchover request]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1250486515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[switchover reset]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1880397590}
:::

::: {#1092602500 .myid}
[]{#_Toc404796153}[]{#struct_0_x2137_x5306_91143605}[]{#_Toc384717071}[]{#_Toc384717069}[]{#_Toc385922955}[]{#_Toc385923519}[]{#_Toc384717070}[]{#_Toc385922956}[]{#_Toc385923520}

**冗余组 \-- 冗余组配置命令 \-- switchover reset**

------------------------------------------------------------------------

[**[switchover reset]{lang="EN-US"}**]{#struct_0_x2137_x5306_x306514349}[命令用来手工触发一次冗余组倒回，让冗余组工作在优先级高的节点。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_651084723}

[**[switchover reset]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_x1679663809}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x669301966}

[[冗余组]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x2010737257}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_446253019}

[[network-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_x850973238}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_x2137_x5306_705205532}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1881488254}

[[当冗余组主备结点无故障，业务运行在优先级低的节点时，用户可通过此命令手工触发冗余组进行倒回。]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x990246286}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_76943025}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1078419187}[在冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[内手动触发一次倒回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_564402968}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] switchover reset]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x1829090228}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[s]{lang="EN-US"}[witchover request]{lang="EN-US"}**]{#struct_0_x2137_x5306_1024943065}
:::

::: {#1609214304 .myid}
[]{#_Toc404796154}[]{#struct_0_x2137_x5306_x704474996}[]{#_Toc384717042}[]{#_Toc375743819}[]{#_Toc384717072}[]{#_Toc385922958}[]{#_Toc385923522}[]{#_Toc384717073}[]{#_Toc385922959}[]{#_Toc385923523}

**冗余组 \-- 冗余组配置命令 \-- track**

------------------------------------------------------------------------

[**[track]{lang="EN-US"}**]{#struct_0_x2137_x5306_x1825324074}[命令用来关联]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[**[undo track]{lang="EN-US"}**]{#struct_0_x2137_x5306_1377099666}[命令用来取消关联。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1187257242}

[**[track]{lang="EN-US"}**[ ]{lang="EN-US"}*[track-entry-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **reduced** *weight-reduced* \] \[ **interface** *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_x2137_x5306_x850907702}

[**[undo track]{lang="EN-US"}**[ ]{lang="EN-US"}*[track-entry-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x41499983}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1383269182}

[[冗余组节点下没有关联任何]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_x1548728465}[项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_842005547}

[[冗余组节点视图]{style="font-family:宋体"}]{#struct_0_x2137_x5306_x1466962021}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_624326037}

[[network-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_1365452306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2137_x5306_x1216463746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_x2028620704}

[*[track-entry-number]{lang="EN-US"}*]{#struct_0_x2137_x5306_x1758502518}[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项的序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[reduced]{lang="EN-US"}**[ *weight-reduced*]{lang="EN-US"}]{#struct_0_x2137_x5306_x850842166}[：权重的变化值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interface]{lang="NO-BOK"}**]{#struct_0_x2137_x5306_1858210261}[ ]{lang="NO-BOK"}*[interface-type interface-num]{lang="NO-BOK"}[ber]{lang="EN-US"}*[：]{style="font-family:宋体"}[Track]{lang="EN-US"}[项关联接口的类型和编号。当影响]{style="font-family:宋体"}[Track]{lang="NO-BOK"}[项]{style="font-family:宋体"}[状态改变的接口是以太网冗余接口的成员接口或是冗余组节点的成员接口时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[建议配置该参数]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并将该参数配置成与]{style="font-family:宋体"}[Track]{lang="EN-US"}[项接口一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_1714824533}

[[一个节点最多能够配置]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_x2137_x5306_1785648779}[个]{style="font-family:宋体"}[Track]{lang="EN-US"}[项。]{style="font-family:宋体"}

[[建议先创建]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_1134416466}[项，再将该]{style="font-family:宋体"}[Track]{lang="EN-US"}[项和冗余组关联。否则，可能会导致冗余组没有有效的]{style="font-family:宋体"}[Track]{lang="EN-US"}[项而触发倒换。]{style="font-family:宋体"}

[[当已将某物理接口配置为某冗余组内高优先级冗余组节点的成员接口，或者为某冗余组内以太网冗余接口的高优先级成员接口时，请不要将该物理接口的子接口配置为该冗余组内高优先级冗余组节点的]{style="font-family:宋体"}[Track]{lang="EN-US"}]{#struct_0_x2137_x5306_397880159}[项关联接口。因为物理接口被协议关闭时，会导致其子接口状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}[，该子接口将无法触发自动倒回，此时，需要手工倒回。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2137_x5306_446871161}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_451002844}[将冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[和]{style="font-family:宋体"}[track 1]{lang="EN-US"}[、]{style="font-family:宋体"}[track 2]{lang="EN-US"}[关联。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x1115081097}

[\[Sysname\] track 1 interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname\] track 2 interface gigabitethernet 2/0/1]{lang="EN-US"}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] track 1 reduced 50 interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] track 2 reduced 50 interface gigabitethernet 2/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x2137_x5306_1304409032}[将冗余组]{style="font-family:宋体"}[aaa]{lang="EN-US"}[和]{style="font-family:宋体"}[track 1]{lang="EN-US"}[、]{style="font-family:宋体"}[track 2]{lang="EN-US"}[关联。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2137_x5306_x1572127526}

[\[Sysname\] track 1 interface gigabitethernet 1/2/0/1]{lang="EN-US"}

[\[Sysname\] track 2 interface gigabitethernet 2/2/0/1]{lang="EN-US"}

[\[Sysname\] redundancy group aaa]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa\] node 1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] track 1 reduced 50 interface gigabitethernet 1/2/0/1]{lang="EN-US"}

[\[Sysname-redundancy-group-aaa-node1\] track 2 reduced 50 interface gigabitethernet 2/2/0/1]{lang="EN-US"}
:::
