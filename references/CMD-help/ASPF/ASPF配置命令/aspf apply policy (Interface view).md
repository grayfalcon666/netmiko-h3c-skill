::: {#-1770915345 .myid}
[]{#_Toc404793414}[]{#struct_0_x4698_11175_2137688496}[]{#_Toc313525669}[]{#_Toc298766609}

**ASPF \-- ASPF配置命令 \-- aspf apply policy (Interface view)**

------------------------------------------------------------------------

[**[aspf apply policy]{lang="EN-US"}**]{#struct_0_x4698_11175_1428139437}[命令用来在接口上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **aspf apply policy**]{lang="EN-US"}]{#struct_0_x4698_11175_x1693037261}[命令用来删除接口上应用的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2100395426}

[**[aspf]{lang="EN-US"}**[ **apply policy** *aspf-policy-number* { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x4698_11175_x783655473}

[**[undo aspf]{lang="EN-US"}**[ **apply policy** *aspf*]{lang="EN-US"}]{#struct_0_x4698_11175_x361329611}*[-policy-number]{lang="EN-US"}*[ { **inbound** \| **outbound** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1025110183}

[[接口上没有应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x1848691783}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1951970684}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_x718685649}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2137622960}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x2083393004}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x1921697191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1567538650}

[*[aspf-policy-number]{lang="EN-US"}*]{#struct_0_x4698_11175_1749960741}[：]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4698_11175_1992114866}[：对接口入方向的报文应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4698_11175_369896188}[：对接口出方向的报文应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1198728576}

[[只有将定义好的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1137028737}[策略应用到接口上，才能对通过接口的流量进行检测。由于]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[对于应用层协议状态的保存和维护都是基于接口的，因此在实际应用中，必须保证报文入口的一致性，即必须保证连接发起方发送的报文和响应端返回的报文经过同一接口。]{style="font-family:宋体"}

[[可以同时在接口的出方向和入方向上都应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x1271416332}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2137164209}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x858966579}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的出方向上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_164837191}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] aspf apply policy 1 outbound]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x2117945198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_x400612762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf policy all]{lang="EN-US"}**]{#struct_0_x4698_11175_x803993488}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf policy interface]{lang="EN-US"}**]{#struct_0_x4698_11175_x939295436}
:::

::::: {#1691015890 .myid}
[]{#_Toc353115151}[]{#_Toc404793415}[]{#struct_0_x4698_11175_x1353384453}

**ASPF \-- ASPF配置命令 \-- aspf apply policy (Zonepair view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_x954754891}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_1450516553}
:::

[ ]{lang="EN-US"}

[**[aspf apply policy]{lang="EN-US"}**]{#struct_0_x4698_11175_x2007865143}[命令用来在安全域间实例上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **aspf apply policy**]{lang="EN-US"}]{#struct_0_x4698_11175_191647964}[命令用来取消应用在安全域间实例上的指定]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1353318917}

[**[aspf apply policy]{lang="EN-US"}**[ *aspf-policy-number*]{lang="EN-US"}]{#struct_0_x4698_11175_x309364439}

[**[undo aspf apply policy]{lang="EN-US"}**[ *aspf-policy-number*]{lang="EN-US"}]{#struct_0_x4698_11175_x1442725008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1382526913}

[[安全域间实例上应用了一个缺省的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_47599764}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1998936326}

[[安全域间实例视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_x464502598}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1170666908}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x1353515525}

[[mdc-admin*[ ]{style="color:blue"}*]{lang="EN-US"}]{#struct_0_x4698_11175_1337233391}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1708165615}

[*[aspf-policy-number]{lang="EN-US"}*]{#struct_0_x4698_11175_x188978480}[：]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[，其中]{style="font-family:宋体"}*[max_number]{lang="EN-US"}*[的取值与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2068815999}

[[创建]{style="font-family:宋体"}]{#struct_0_x4698_11175_339053907}[安全域间实例时，系统默认为该实例应用一个缺省的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，该策略支持对所有协议进行]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[检测，但]{style="font-family:宋体"}[默认的策略不可改变，如果需要调整]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，需要自定义一个]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并在安全域间实例上引用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x134531300}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_27356633}[在安全域间实例上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_x1353449989}

[\[Sysname\] security-zone name trust]{lang="EN-US"}

[\[Sysname-security-zone-Trust\] import interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-security-zone-Trust\] quit]{lang="EN-US"}

[\[Sysname\] security-zone name untrust]{lang="EN-US"}

[\[Sysname-security-zone-Untrust\] import interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-security-zone-Untrust\] quit]{lang="EN-US"}

[\[Sysname\] zone-pair security source trust destination untrust]{lang="EN-US"}

[\[Sysname-zone-pair-security-Trust-Untrust\] aspf apply policy 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1687108216}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_x1865756039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf policy all]{lang="EN-US"}**]{#struct_0_x4698_11175_1880567739}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[zone]{lang="EN-US"}**]{#struct_0_x4698_11175_x1013853025}**[-pair security]{lang="EN-US"}**[（基础命令参考]{style="font-family:宋体"}[/]{lang="EN-US"}[安全域）]{style="font-family:宋体"}
:::::

::: {#12420881 .myid}
[]{#_Toc404793416}[]{#struct_0_x4698_11175_1442814695}[]{#_Toc313525663}[]{#_Toc298766603}[]{#_Toc272768848}[]{#_Toc33096877}[]{#_Toc135454115}[]{#_Toc135454116}[]{#_Toc135454117}[]{#_Toc135454119}[]{#_Toc135454120}[]{#_Toc135454121}[]{#_Toc135454122}[]{#_Toc135454123}[]{#_Toc135454124}[]{#_Toc135454125}[]{#_Toc135454126}[]{#_Toc135454127}[]{#_Toc135454128}[]{#_Toc135454129}[]{#_Toc135454130}[]{#_Toc135454131}[]{#_Toc135454132}[]{#_Toc135454133}[]{#_Toc135454134}[]{#_Toc135454135}[]{#_Toc135454136}[]{#_Toc135454137}[]{#_Toc135454138}[]{#_Toc135454139}[]{#_Toc135454140}

**ASPF \-- ASPF配置命令 \-- aspf policy**

------------------------------------------------------------------------

[**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_457535593}[命令用来创建]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略，并进入]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **aspf policy**]{lang="EN-US"}]{#struct_0_x4698_11175_2137098673}[命令用来删除指定的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1039379833}

[**[aspf policy]{lang="EN-US"}**[ *aspf-policy-number*]{lang="EN-US"}]{#struct_0_x4698_11175_1803240830}

[**[undo]{lang="EN-US"}**[ **aspf policy** *aspf-policy-number*]{lang="EN-US"}]{#struct_0_x4698_11175_x534109143}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_482415176}

[[不存在]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1354797845}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1198322807}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_580218778}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1791258784}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_2137033137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x2052948680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x796315022}

[*[aspf-policy-number]{lang="EN-US"}*]{#struct_0_x4698_11175_x1226669134}[：]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1971139800}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x1728357579}[创建]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入该]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_1534654733}

[\[Sysname\] aspf policy 1]{lang="EN-US"}

[\[Sysname-aspf-policy-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_914244203}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf all]{lang="EN-US"}**]{#struct_0_x4698_11175_2068281285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_2136967601}
:::

::::: {#75545529 .myid}
[]{#_Toc404793417}[]{#struct_0_x4698_11175_x1679185536}[]{#_Toc313525664}[]{#_Toc298766604}[]{#_Toc272768849}[]{#_Toc33096878}

**ASPF \-- ASPF配置命令 \-- detect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_1640044196}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_x1516211870}
:::

[ ]{lang="EN-US"}

[**[detect]{lang="EN-US"}**]{#struct_0_x4698_11175_1478091689}[命令用来为应用层协议或传输层协议配置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **detect**]{lang="EN-US"}]{#struct_0_x4698_11175_1427816548}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_500386214}

[**[detect]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4698_11175_1283729476}[{ **dccp** \| ]{lang="ES-AR"}**[gtp]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **icmp** \| **icmpv6** \|]{lang="ES-AR"}**[ ]{lang="ES-AR"}[ils ]{lang="ES-AR"}**[\| **mgcp** \| **nbt** \| **pptp** \| **rawip** \| **rsh** \| ]{lang="ES-AR"}**[rtsp]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[sctp ]{lang="ES-AR"}**[\| ]{lang="EN-US"}**[sqlnet]{lang="ES-AR"}**[ \| **tcp** \| ]{lang="ES-AR"}**[tftp]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **udp** \|]{lang="ES-AR"}**[ ]{lang="ES-AR"}[udp-lite]{lang="EN-US"}[ ]{lang="EN-US"}**[\| **xdmcp** ]{lang="ES-AR"}[}]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **detect** ]{lang="EN-US"}]{#struct_0_x4698_11175_1764640475}[{ **dccp** \| ]{lang="ES-AR"}**[gtp]{lang="EN-US"}[ ]{lang="EN-US"}**[\| **icmp** \| **icmpv6** \|]{lang="ES-AR"}**[ ]{lang="ES-AR"}[ils ]{lang="ES-AR"}**[\| **mgcp** \| **nbt** \| **pptp** \| **rawip** \|]{lang="ES-AR"}**[ ]{lang="ES-AR"}[rsh]{lang="ES-AR"}**[ \| ]{lang="ES-AR"}**[rtsp]{lang="EN-US"}**[ \|]{lang="EN-US"}[ ]{lang="EN-US"}**[sctp ]{lang="ES-AR"}**[\| **sqlnet** \| **tcp** \| ]{lang="ES-AR"}**[tftp]{lang="EN-US"}**[ ]{lang="EN-US"}[\| **udp** \| ]{lang="ES-AR"}**[udp-lite ]{lang="EN-US"}**[\| **xdmcp**]{lang="ES-AR"}[ ]{lang="ES-AR"}[}]{lang="EN-US"}

[**[detect]{lang="EN-US"}**[ { **dns \| ftp** \| **h323** \| **http** \| **sccp** \| **sip** \| **smtp** } \[ **action drop** \]]{lang="EN-US"}]{#struct_0_x4698_11175_x186350593}

[**[undo detect]{lang="EN-US"}**[ { **dns** \| **ftp** \| **h323** \| **http** \| **sccp** \| **sip** \| **smtp** }]{lang="EN-US"}]{#struct_0_x4698_11175_1395737746}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2136902065}

[[未配置应用层和传输层协议]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x2062094207}[检测。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x2018094880}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1902906802}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x358675463}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x283399226}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_593957966}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_188953787}

[**[dccp]{lang="ES-AR"}**]{#struct_0_x4698_11175_1521734811}[：表示]{style="font-family:宋体"}[DCCP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Datagram Congestion Control Protocol]{lang="PT-BR"}[，数据报拥塞控制协议）协议，属于]{style="font-family:宋体"}[传输层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[dns]{lang="EN-US"}**]{#struct_0_x4698_11175_x1752434534}[：表示]{style="font-family:宋体"}[DNS]{lang="EN-US"}[协议，属于应用层协议。]{style="font-family:宋体"}

[**[ftp]{lang="PT-BR"}**]{#struct_0_x4698_11175_2136836529}[：表示]{style="font-family:宋体"}[FTP]{lang="PT-BR"}[协议，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[gtp]{lang="PT-BR"}**]{#struct_0_x4698_11175_x1287315874}[：表示]{style="font-family:宋体"}[GTP]{lang="PT-BR"}[（]{style="font-family:宋体"}[GPRS Tunneling Protocol]{lang="PT-BR"}[，]{style="font-family:宋体"}[GPRS]{lang="PT-BR"}[隧道协议）协议，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[h323]{lang="PT-BR"}**]{#struct_0_x4698_11175_x966480229}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[H.323]{lang="PT-BR"}[协议族]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[http]{lang="PT-BR"}**]{#struct_0_x4698_11175_169945303}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[协议，属于应用层协议。]{style="font-family:宋体"}

[**[icmp]{lang="EN-US"}**]{#struct_0_x4698_11175_95756614}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[传输层协议；]{style="font-family:宋体"}

[**[icmpv6]{lang="EN-US"}**]{#struct_0_x4698_11175_x1150176875}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[传输层协议；]{style="font-family:宋体"}

[**[ils]{lang="ES-AR"}**]{#struct_0_x4698_11175_427102222}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[ILS]{lang="EN-US"}[（]{style="font-family:宋体"}[Internet Locator Service]{lang="EN-US"}[，互联网定位服务）协议，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[应用层协议；]{style="font-family:宋体"}

[**[mgcp]{lang="ES-AR"}**]{#struct_0_x4698_11175_2099120440}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[MGCP]{lang="ES-AR"}[（]{style="font-family:宋体"}[Media Gateway Control Protocol]{lang="ES-AR"}[，]{style="font-family:宋体"}[媒体网关控制协议]{style="font-family:宋体"}[）]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[nbt]{lang="ES-AR"}**]{#struct_0_x4698_11175_434195399}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[NBT]{lang="ES-AR"}[（]{style="font-family:宋体"}[NetBIOS over TCP/IP]{lang="ES-AR"}[，]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[TCP/IP]{lang="ES-AR"}[的网络基本输入输出系统]{style="font-family:宋体"}[）]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[pptp]{lang="ES-AR"}**]{#struct_0_x4698_11175_1317779686}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[PPTP]{lang="ES-AR"}[（]{style="font-family:宋体"}[Point-to-Point Tunneling Protocol]{lang="ES-AR"}[，]{style="font-family:宋体"}[点到点隧道协议]{style="font-family:
宋体"}[）]{style="font-family:宋体"}[协议]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:
宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:
宋体"}

[**[rawip]{lang="ES-AR"}**]{#struct_0_x4698_11175_1388875935}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[Raw IP]{lang="EN-US"}[协议]{style="font-family:宋体"}[，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[传输层协议；]{style="font-family:宋体"}

[**[rsh]{lang="ES-AR"}**]{#struct_0_x4698_11175_427036686}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[RSH]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Shell]{lang="EN-US"}[，远程外壳）协议，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[应用层协议；]{style="font-family:宋体"}

[**[rtsp]{lang="EN-US"}**]{#struct_0_x4698_11175_x906576526}[：表示]{style="font-family:宋体"}[RTSP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Real Time Streaming Protocol]{lang="PT-BR"}[，实时流协议）协议，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[sccp]{lang="PT-BR"}**]{#struct_0_x4698_11175_1720376193}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SCCP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Skinny Client Control Protocol]{lang="PT-BR"}[，]{style="font-family:宋体"}[瘦小客户端控制协议]{style="font-family:宋体"}[）]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[sctp]{lang="ES-AR"}**]{#struct_0_x4698_11175_514120311}[：表示]{style="font-family:宋体"}[SCTP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Stream Control Transmission Protocol]{lang="PT-BR"}[，流控制传输协议）协议，属于]{style="font-family:宋体"}[传输层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[sip]{lang="PT-BR"}**]{#struct_0_x4698_11175_x1311588744}[：表示]{style="font-family:宋体"}[SIP]{lang="PT-BR"}[（]{style="font-family:宋体"}[Session Iniation Protocol]{lang="PT-BR"}[，会话初始化协议）协议，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[smtp]{lang="EN-US"}**]{#struct_0_x4698_11175_1185938010}[：表示]{style="font-family:宋体"}[SMTP]{lang="EN-US"}[协议，属于应用层协议。]{style="font-family:宋体"}

[**[sqlnet]{lang="ES-AR"}**]{#struct_0_x4698_11175_x307082557}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[SQLNET]{lang="PT-BR"}[协议]{style="font-family:宋体"}[，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[tcp]{lang="PT-BR"}**]{#struct_0_x4698_11175_2136770993}[：表示]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[协议，属于]{style="font-family:宋体"}[传输层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[tftp]{lang="EN-US"}**]{#struct_0_x4698_11175_1868171378}[：表示]{style="font-family:宋体"}[TFTP]{lang="PT-BR"}[协议，属于]{style="font-family:宋体"}[应用层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[udp]{lang="PT-BR"}**]{#struct_0_x4698_11175_889636939}[：表示]{style="font-family:宋体"}[UDP]{lang="PT-BR"}[协议，属于]{style="font-family:宋体"}[传输层协议]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[udp-lite]{lang="PT-BR"}**]{#struct_0_x4698_11175_x57386709}[：表示]{style="font-family:宋体"}[UDP-Lite]{lang="PT-BR"}[协议，属于]{style="font-family:宋体"}[传输层协议；]{style="font-family:宋体"}

[**[xdmcp]{lang="ES-AR"}**]{#struct_0_x4698_11175_426577933}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[XDMCP]{lang="EN-US"}[（]{style="font-family:宋体"}[X Display Manager Control Protocol]{lang="EN-US"}[，]{style="font-family:宋体"}[X]{lang="EN-US"}[显示监控）协议，]{style="font-family:宋体"}[属于]{style="font-family:宋体"}[应用层协议。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_x4698_11175_x1396138638}[：设置对检测到的非法报文的处理行为。若不指定该参数，则表示放行报文。]{style="font-family:宋体"}

[**[drop]{lang="EN-US"}**]{#struct_0_x4698_11175_x646954997}[：表示丢弃报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1237404178}

[[可通过多次执行本命令配置多种协议类型的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1550991912}[检测。]{style="font-family:宋体"}

[[在未配置应用层协议检测，直接配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4698_11175_2052566861}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[检测的情况下，可能会产生接收不到应答报文的情况，故建议应用层协议检测和]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}[检测配合使用。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[Telnet]{lang="EN-US"}]{#struct_0_x4698_11175_x274178797}[应用，直接配置通用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[检测即可实现]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[需要注意的是，目前，设备对支持]{style="font-family:宋体"}**[action]{lang="EN-US"}**]{#struct_0_x4698_11175_x992854111}[参数的应用层协议才支持进行协议状态合法性检查，对不符合协议状态的报文可根据配置进行丢弃。对于其它应用层协议，仅进行连接状态信息的维护，不做协议状态合法性检查。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1631757027}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_284603830}[配置对]{style="font-family:宋体"}[FTP]{lang="EN-US"}[协议报文进行]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_2136705457}

[\[Sysname\] aspf policy 1]{lang="EN-US"}

[\[Sysname-aspf-policy-1\] detect ftp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1075102071}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **aspf** **policy**]{lang="EN-US"}]{#struct_0_x4698_11175_x1901126111}
:::::

::: {#1125107606 .myid}
[]{#_Toc404793418}[]{#struct_0_x4698_11175_1877969401}[]{#_Toc313525665}[]{#_Toc298766605}

**ASPF \-- ASPF配置命令 \-- display aspf all**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **aspf** **all**]{lang="EN-US"}]{#struct_0_x4698_11175_x1866392979}[命令用来查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略配置信息及接口应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1248945087}

[**[display aspf all]{lang="EN-US"}**]{#struct_0_x4698_11175_543024358}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_204110076}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_1244739310}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2137688497}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_1428204973}

[[netword-operator]{lang="EN-US"}]{#struct_0_x4698_11175_1830379959}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x596687496}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4698_11175_x1499555062}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_34988541}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_377690898}[查看所有的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display aspf all]{lang="EN-US"}]{#struct_0_x4698_11175_2137622961}

[ASPF policy configuration:]{lang="EN-US"}

[  Policy number: 1]{lang="EN-US"}

[    Enable ICMP error message check]{lang="EN-US"}

[    Disable TCP SYN packet check]{lang="EN-US"}

[    Detect these protocols:]{lang="EN-US"}

[      FTP]{lang="EN-US"}

[      TCP]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface configuration:]{lang="EN-US"}

[  GigabitEthernet1/0/1]{lang="EN-US"}

[    Inbound policy : 1]{lang="EN-US"}

[    Outbound policy: none]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display aspf all]{lang="EN-US"}]{#struct_0_x4698_11175_x2083327468}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1118537714}[[字段]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1494248}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4698_11175_x129605595}

[[ASPF policy configuration]{lang="EN-US"}]{#struct_0_x4698_11175_x1551850544}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x1510513380}[策略的配置信息]{style="font-family:宋体"}

[[Policy number]{lang="EN-US"}]{#struct_0_x4698_11175_2137164206}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x858114611}[策略号]{style="font-family:宋体"}

[[Enable ICMP error message check]{lang="EN-US"}]{#struct_0_x4698_11175_x1375461477}

[[使能]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x4698_11175_1029958193}[差错报文检测功能]{style="font-family:宋体"}

[[Enable TCP SYN packet check]{lang="EN-US"}]{#struct_0_x4698_11175_x635250790}

[[丢弃非]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x4698_11175_182510057}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文]{style="font-family:宋体"}

[[Disable ICMP error message check]{lang="EN-US"}]{#struct_0_x4698_11175_x583584828}

[[去使能]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x4698_11175_2137098670}[差错报文检测功能]{style="font-family:宋体"}

[[Disable TCP SYN packet check]{lang="EN-US"}]{#struct_0_x4698_11175_1039314297}

[[不丢弃非]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x4698_11175_716260043}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文]{style="font-family:宋体"}

[[Detect these protocols]{lang="EN-US"}]{#struct_0_x4698_11175_x2102249183}

[[需要检测的协议]{style="font-family:宋体"}]{#struct_0_x4698_11175_1709593052}

[[Interface configuration]{lang="EN-US"}]{#struct_0_x4698_11175_x1716080986}

[[接口下应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_2137033134}[策略的配置信息]{style="font-family:宋体"}

[[Inbound policy]{lang="EN-US"}]{#struct_0_x4698_11175_x2052752072}

[[接口入方向上应用的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x576423939}[策略编号]{style="font-family:宋体"}

[[Outbound policy]{lang="EN-US"}]{#struct_0_x4698_11175_x533301476}

[[接口出方向上应用的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x931893841}[策略编号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1530308690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf]{lang="EN-US"}**]{#struct_0_x4698_11175_2136967598}**[ apply policy]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_276539767}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_x1924499741}

::: {#-2107480144 .myid}
[]{#_Toc404793419}[]{#struct_0_x4698_11175_x768326995}[]{#_Toc313525666}[]{#_Toc298766606}[]{#_Toc272768851}

**ASPF \-- ASPF配置命令 \-- display aspf interface**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **aspf** **interface**]{lang="EN-US"}]{#struct_0_x4698_11175_x1866539877}[命令用来查看接口上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_74712468}

[**[display aspf interface]{lang="EN-US"}**]{#struct_0_x4698_11175_x2051219420}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1661058718}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1240490265}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2136902062}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x2062552959}

[[netword-operator]{lang="EN-US"}]{#struct_0_x4698_11175_1935624119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_1717060204}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4698_11175_1306002724}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x2066466122}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x1070986085}[查看接口上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略信息。]{style="font-family:宋体"}

[[\<Sysname\> display aspf interface]{lang="EN-US"}]{#struct_0_x4698_11175_2136836526}

[Interface configuration:]{lang="EN-US"}

[  GigabitEthernet1/0/1]{lang="EN-US"}

[    Inbound policy : 1]{lang="EN-US"}

[    Outbound policy: none]{lang="EN-US"}

[]{#struct_0_x4698_11175_x1286594978}[]{#_Toc138067669}[]{#_Toc95386916}[]{#_Toc85621930}[]{#_Toc81452878}[]{#_Toc74712935}[]{#_Toc74712793}[]{#_Toc72595591}[]{#_Toc66003025}[]{#_Toc60131206}[]{#_Toc42655609}[[表1-2 ]{lang="EN-US"}[display aspf interface]{lang="EN-US"}]{#_Toc40150007}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1114078354}[[字段]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1074451043}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4698_11175_1568080900}

[[Interface configuration]{lang="EN-US"}]{#struct_0_x4698_11175_x936815669}

[[接口上应用]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1955175438}[策略的配置信息]{style="font-family:宋体"}

[[Inbound policy]{lang="EN-US"}]{#struct_0_x4698_11175_1803541994}

[[接口入方向上应用的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x144140309}[策略编号]{style="font-family:宋体"}

[[Outbound policy]{lang="EN-US"}]{#struct_0_x4698_11175_2136770990}

[[接口出方向上应用的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1868367986}[策略编号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1988789284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf]{lang="EN-US"}**]{#struct_0_x4698_11175_1408779980}**[ apply policy]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_x1064026892}

::: {#-1542800029 .myid}
[]{#_Toc404793420}[]{#struct_0_x4698_11175_x565318538}[]{#_Toc313525667}[]{#_Toc298766607}

**ASPF \-- ASPF配置命令 \-- display aspf policy**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **aspf** **policy**]{lang="EN-US"}]{#struct_0_x4698_11175_1790802983}[命令用来查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1973522826}

[**[display]{lang="EN-US"}**[ **aspf** **policy** *aspf-policy-number*]{lang="EN-US"}]{#struct_0_x4698_11175_2136705454}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1075167607}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1170506769}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1687374623}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_62671358}

[[netword-operator]{lang="EN-US"}]{#struct_0_x4698_11175_2077198896}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x1642429612}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4698_11175_x258620615}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_310047434}

[*[aspf-policy-number]{lang="EN-US"}*]{#struct_0_x4698_11175_2137688494}[：]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1428270509}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x566972974}[查看策略号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display aspf policy 1]{lang="EN-US"}]{#struct_0_x4698_11175_x1396073102}

[ASPF policy configuration:]{lang="EN-US"}

[  Policy number: 1]{lang="EN-US"}

[    ICMP error message check: Disabled]{lang="EN-US"}

[    TCP SYN packet check: Enabled]{lang="EN-US"}

[    Inspected protocol   Action]{lang="EN-US"}

[     FTP                  Drop]{lang="EN-US"}

[     TCP                  -]{lang="EN-US"}

[     HTTP                 None]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display aspf policy]{lang="EN-US"}]{#struct_0_x4698_11175_894634715}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1109194546}[[字段]{style="font-family:黑体"}]{#struct_0_x4698_11175_1552553660}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4698_11175_x10369382}

[[ASPF policy configuration]{lang="EN-US"}]{#struct_0_x4698_11175_2137622958}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x2083917289}[策略的配置信息]{style="font-family:宋体"}

[[Policy number]{lang="EN-US"}]{#struct_0_x4698_11175_837805666}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x989787596}[策略号]{style="font-family:宋体"}

[[ICMP error message check]{lang="EN-US"}]{#struct_0_x4698_11175_990683879}

[[ICMP]{lang="EN-US"}]{#struct_0_x4698_11175_95807305}[差错报文检测功能的开启状态]{style="font-family:宋体"}

[[TCP SYN packet check]{lang="EN-US"}]{#struct_0_x4698_11175_2137164207}

[[非]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x4698_11175_x858049075}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文丢弃功能是否开启]{style="font-family:宋体"}

[[Inspected protocol]{lang="EN-US"}]{#struct_0_x4698_11175_x992788575}

[[待检测的协议]{style="font-family:宋体"}]{#struct_0_x4698_11175_1736094780}

[[Action]{lang="EN-US"}]{#struct_0_x4698_11175_1812546214}

[[对检测到的非法报文的处理行为]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1234899527}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_x4698_11175_x1789151044}[：丢弃]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x4698_11175_777732090}[：不做处理，放行]{lang="EN-US" style="font-family:宋体"}

[["]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x4698_11175_x1799357629}["表示该协议不支持此配置项]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_288143927}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_1749236535}

::::: {#-1079275371 .myid}
[]{#_Toc404793421}[]{#struct_0_x4698_11175_x1869903756}[]{#_Toc313525668}[]{#_Toc298766608}[]{#_Toc272768853}[]{#_Toc33096882}

**ASPF \-- ASPF配置命令 \-- display aspf session**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_1839519380}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_x1165540163}
:::

[ ]{lang="EN-US"}

[**[display aspf session]{lang="EN-US"}**]{#struct_0_x4698_11175_x1302078010}[命令用来查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的会话表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2137033135}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1352794630}

[**[display aspf session]{lang="EN-US"}**[ \[ **ipv4** \| **ipv6** \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4698_11175_x2052817608}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4698_11175_x2106395372}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display aspf session]{lang="EN-US"}**[ \[ **ipv4** \| **ipv6** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4698_11175_x1099436224}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_x4698_11175_x351868081}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[display aspf session]{lang="EN-US"}**[ \[ **ipv4** \| **ipv6** \] \[ ]{lang="EN-US"}]{#struct_0_x4698_11175_x1353384455}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}**[ slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1094182425}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_x861900970}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_313991588}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x1078606733}

[[netword-operator]{lang="EN-US"}]{#struct_0_x4698_11175_1261084436}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_792864313}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4698_11175_x1505790202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_2136967599}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4698_11175_276605303}[：查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4698_11175_x1644321512}[：查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x4698_11175_208044523}[ *slot-number*]{lang="EN-US"}[：显示指定单板上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，显示所有单板上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x4698_11175_x1920814465}[ *slot-number*]{lang="EN-US"}[：显示指定成员设备上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，显示所有成员设备上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4698_11175_x92154651}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x4698_11175_x1353318919}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备的指定单板上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，显示所有成员设备的所有单板上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4698_11175_x2014468952}[：]{style="font-family:宋体"}[显示指定单板]{style="font-family:宋体"}[上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则显示所有单板上]{style="font-family:宋体"}[的]{style="font-family:
宋体"}[ASPF]{lang="EN-US"}[会话表]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x4698_11175_140974255}[ *cpu-number*]{lang="EN-US"}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4698_11175_x1323252764}[：查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表的详细信息。若不指定该参数，则表示查看]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_542803663}

[[不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**]{#struct_0_x4698_11175_x2026948185}[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数时，表示查看所有的]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[会话表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_17243281}

[]{#_Toc272768855}[]{#_Toc33096883}[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_1980745982}[显示]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表的概要信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4]{lang="EN-US"}]{#struct_0_x4698_11175_2136902063}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[ ]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x2062487423}[显示]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表的概要信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4]{lang="EN-US"}]{#struct_0_x4698_11175_2136836527}

[Slot 1:]{lang="EN-US"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[ ]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x1286660514}[显示]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4]{lang="EN-US"}]{#struct_0_x4698_11175_141937452}

[Slot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[ ]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_1884084150}[显示]{style="font-family:宋体"}[IPv4 ASPF]{lang="EN-US"}[会话的详细信息。（集中式设备）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4 verbose]{lang="EN-US"}]{#struct_0_x4698_11175_2136705455}

[Initiator:]{lang="FR"}

[  ]{lang="FR"}[Source       IP]{lang="EN-US"}[/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source       IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:          1 packets         60 bytes]{lang="FR"}

[Responder-\>Initiator:          0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x4698_11175_1075233143}[显示]{style="font-family:宋体"}[IPv4 ASPF]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4 verbose]{lang="EN-US"}]{#struct_0_x4698_11175_2137688495}

[Slot 1:]{lang="EN-US"}

[Initiator:]{lang="FR"}

[  Source      IP]{lang="EN-US"}[/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         6048 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x4698_11175_1428336045}[显示]{style="font-family:宋体"}[IPv4 ASPF]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="FR"}[模式]{style="font-family:宋体"}[）]{style="font-family:
宋体"}

[[\<Sysname\> display aspf session ipv4 verbose]{lang="FR"}]{#struct_0_x4698_11175_2137622959}

[Slot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP]{lang="EN-US"}[/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application: SSH]{lang="FR"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: Dest]{lang="EN-US"}[Zone]{lang="FR"}

[State: ICMP_REQUEST]{lang="FR"}

[Application: OTHER]{lang="FR"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         6048 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x4698_11175_1829707523}[显示]{style="font-family:宋体"}[ASPF]{lang="FR"}[创建的]{style="font-family:宋体"}[IPv4]{lang="FR"}[会话表的概要信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[独立运行模式]{style="font-family:宋体"}[/]{lang="FR"}[集中式]{style="font-family:宋体"}[IRF]{lang="FR"}[设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4]{lang="EN-US"}]{#struct_0_x4698_11175_1829773059}

[CPU 0 on slot 1:]{lang="EN-US"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[ ]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_1444843861}[显示]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表的概要信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4]{lang="EN-US"}]{#struct_0_x4698_11175_1829314307}

[CPU 0 on s]{lang="EN-US"}[lot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1877]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/22]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: TCP(6)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Initiator:]{lang="EN-US"}

[  Source      IP/port: 192.168.1.18/1792]{lang="EN-US"}

[  Destination IP/port: 192.168.1.55/2048]{lang="EN-US"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="EN-US"}

[  Protocol: ICMP(1)]{lang="EN-US"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[ ]{lang="EN-US"}

[Total sessions found: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_1872454039}[显示]{style="font-family:宋体"}[IPv4 ASPF]{lang="EN-US"}[会话的详细信息。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[[\<Sysname\> display aspf session ipv4 verbose]{lang="EN-US"}]{#struct_0_x4698_11175_1829445379}

[CPU 0 on slot 1:]{lang="EN-US"}

[Initiator:]{lang="FR"}

[  Source      IP]{lang="EN-US"}[/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[ ]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application]{lang="FR"}[: SSH]{lang="EN-US"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: ICMP_REQUEST]{lang="FR"}

[Application]{lang="FR"}[: OTHER]{lang="EN-US"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         6048 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[\# ]{lang="FR"}]{#struct_0_x4698_11175_292935048}[显示]{style="font-family:宋体"}[IPv4 ASPF]{lang="FR"}[会话的详细信息。]{style="font-family:宋体"}[（]{style="font-family:宋体"}[分布式设备]{style="font-family:宋体"}[－]{style="font-family:宋体"}[IRF]{lang="FR"}[模式]{style="font-family:宋体"}[）]{style="font-family:
宋体"}

[[\<Sysname\> display aspf session ipv4 verbose]{lang="FR"}]{#struct_0_x4698_11175_1829052163}

[CPU 0 on s]{lang="EN-US"}[lot 1 in chassis 1:]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP]{lang="EN-US"}[/port: 192.168.1.18/1877]{lang="FR"}

[  Destination IP/port: 192.168.1.55/22]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/22]{lang="FR"}

[  Destination IP/port: 192.168.1.18/1877]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: TCP(6)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: TCP_SYN_SENT]{lang="FR"}

[Application]{lang="FR"}[: SSH]{lang="EN-US"}

[Start time: 2011-07-29 19:12:36  TTL: 28s]{lang="FR"}

[Initiator-\>Responder:         1 packets         48 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Initiator:]{lang="FR"}

[  Source      IP/port: 192.168.1.18/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.55/2048]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/1]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[SrcZone]{lang="FR"}

[Responder:]{lang="FR"}

[  Source      IP/port: 192.168.1.55/1792]{lang="FR"}

[  Destination IP/port: 192.168.1.18/0]{lang="FR"}

[  DS-Lite tunnel peer: -]{lang="EN-US"}

[  VPN instance/VLAN ID/VLL ID: -/-/-]{lang="FR"}

[  Protocol: ICMP(1)]{lang="FR"}

[  Inbound interface: GigabitEthernet1/0/2]{lang="EN-US"}

[  Source security zone: ]{lang="EN-US"}[DestZone]{lang="FR"}

[State: ICMP_REQUEST]{lang="FR"}

[Application]{lang="FR"}[: OTHER]{lang="EN-US"}

[Start time: 2011-07-29 19:12:33  TTL: 55s]{lang="FR"}

[Initiator-\>Responder:         1 packets         6048 bytes]{lang="FR"}

[Responder-\>Initiator:         0 packets          0 bytes]{lang="FR"}

[ ]{lang="FR"}

[Total sessions found: 2]{lang="FR"}

[[表1-4 ]{lang="EN-US"}[display aspf session]{lang="EN-US"}]{#struct_0_x4698_11175_x2083851753}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1109578034}[[字段]{style="font-family:黑体"}]{#struct_0_x4698_11175_x591719145}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1828975400}

[[Initiator]{lang="EN-US"}]{#struct_0_x4698_11175_x1789690996}

[[发起方到响应方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_x4698_11175_1800313825}

[[Responder]{lang="FR"}]{#struct_0_x4698_11175_x7098508}

[[响应方到发起方的连接对应的会话信息]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1547758935}

[[Source IP/port]{lang="EN-US"}]{#struct_0_x4698_11175_x1698464616}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4698_11175_x591784681}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[Dest IP/port]{lang="FR"}]{#struct_0_x4698_11175_1226242235}

[[目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4698_11175_1368989013}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[DS-Lite tunnel peer]{lang="EN-US"}]{#struct_0_x4698_11175_x1067168478}

[[DS-Lite]{lang="FR"}]{#struct_0_x4698_11175_x780108181}[隧道对端地址。会话不属于任何]{style="font-family:宋体"}[DS-Lite]{lang="FR"}[隧道时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[本字段显示为]{style="font-family:宋体"}["]{style="font-family:宋体"}[-]{lang="FR"}["]{style="font-family:宋体"}

[[VPN-instance/VLAN ID/VLL ID]{lang="FR"}]{#struct_0_x4698_11175_2012029545}

[[会话所属的]{style="font-family:宋体"}[MPLS L3VPN/]{lang="EN-US"}]{#struct_0_x4698_11175_223488229}[二层转发时会话所属的]{style="font-family:宋体"}[VLAN ID/]{lang="EN-US"}[二层转发时会话所属的]{style="font-family:宋体"}[INLINE]{lang="EN-US"}[。未指定的参数则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x4698_11175_1629024465}

[[传输层协议类型，取值包括：]{style="font-family:宋体"}[DCCP]{lang="EN-US"}]{#struct_0_x4698_11175_x591850217}[、]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[、]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[、]{style="font-family:宋体"}[Raw IP ]{lang="EN-US"}[、]{style="font-family:宋体"}[SCTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP-Lite]{lang="EN-US"}

[[括号中的数字表示协议号]{style="font-family:宋体"}]{#struct_0_x4698_11175_x308533591}

[[Inbound interface]{lang="FR"}]{#struct_0_x4698_11175_x1067758299}

[[报文的入接口]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1086830457}

[[Source security zone]{lang="FR"}]{#struct_0_x4698_11175_x1133557501}

[[源安全域，即入接口所属的安全域。若接口不属于任何安全域，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x4698_11175_x402099992}["]{style="font-family:宋体"}

[[该参数的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x4698_11175_x982906392}

[[State]{lang="EN-US"}]{#struct_0_x4698_11175_x573532969}

[[会话的协议状态]{style="font-family:宋体"}]{#struct_0_x4698_11175_2056252315}

[[Application]{lang="EN-US"}]{#struct_0_x4698_11175_x2144063858}

[[应用层协议类型，取值包括：]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_x4698_11175_x243723692}[、]{style="font-family:宋体"}[DNS]{lang="EN-US"}[等，]{style="font-family:宋体"}[OTHER]{lang="FR"}[表示未知协议类型，其对应的端口为非知名端口]{style="font-family:宋体"}

[[Start time]{lang="EN-US"}]{#struct_0_x4698_11175_x591915753}

[[会话的创建时间]{style="font-family:宋体"}]{#struct_0_x4698_11175_470910037}

[[TTL]{lang="EN-US"}]{#struct_0_x4698_11175_x957477244}

[[会话剩余存活时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x4698_11175_x238239152}

[[Initiator-\>Responder]{lang="FR"}]{#struct_0_x4698_11175_2127588895}

[[发起方到响应方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1876571055}

[[Responder-\>Initiator]{lang="FR"}]{#struct_0_x4698_11175_x592046825}

[[响应方到发起方的报文数、报文字节数]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1567289736}

[[Total sessions found]{lang="EN-US"}]{#struct_0_x4698_11175_x1624105851}

[[当前查找到的会话总数]{style="font-family:宋体"}]{#struct_0_x4698_11175_x352954846}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_551559294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset aspf session]{lang="EN-US"}**]{#struct_0_x4698_11175_x592112361}

::::: {#571769650 .myid}
[]{#_Toc33096884}[]{#_Toc404793422}[]{#struct_0_x4698_11175_342047849}[]{#_Toc313525670}[]{#_Toc298766610}[]{#_Toc272768856}

**ASPF \-- ASPF配置命令 \-- icmp-error drop**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_x1518350159}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_x469896141}
:::

[ ]{lang="EN-US"}

[**[icmp]{lang="EN-US"}**[-**error drop**]{lang="EN-US"}]{#struct_0_x4698_11175_1637997926}[命令用来开启]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文检测功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **icmp**-**error drop**]{lang="EN-US"}]{#struct_0_x4698_11175_1211676196}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_217968160}

[**[icmp]{lang="EN-US"}**[-**error drop**]{lang="EN-US"}]{#struct_0_x4698_11175_x1244482515}

[**[undo]{lang="EN-US"}**[ **icmp**-**error drop**]{lang="EN-US"}]{#struct_0_x4698_11175_x592177897}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x3499469}

[[ICMP]{lang="EN-US"}]{#struct_0_x4698_11175_659715828}[差错报文检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x625371658}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x345082452}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x558356689}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_761280157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x559974386}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1903829129}

[[正常]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x4698_11175_x591194857}[差错报文中均携带有本报文对应连接的相关信息，根据这些信息可以匹配到相应的连接。如果匹配失败，则根据当前配置决定是否丢弃该]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_81000456}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x1342022659}[设置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略]{style="font-family:宋体"}[1]{lang="EN-US"}[丢弃非法的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[差错报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_1825346805}

[\[Sysname\] aspf policy 1]{lang="EN-US"}

[\[Sysname-aspf-policy-1\] icmp-error drop]{lang="EN-US"}

[]{#_Toc272768858}[]{#_Toc33096887}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1711781171}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_1603078033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **aspf** **policy**]{lang="EN-US"}]{#struct_0_x4698_11175_445499588}
:::::

::::: {#-1290731094 .myid}
[]{#_Toc404793423}[]{#struct_0_x4698_11175_x1863202890}[]{#_Toc313525671}[]{#_Toc298766611}[]{#_Toc272768859}

**ASPF \-- ASPF配置命令 \-- reset aspf session**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_x591260393}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_1658332539}
:::

[ ]{lang="EN-US"}

[**[reset aspf session]{lang="EN-US"}**]{#struct_0_x4698_11175_1580088314}[命令用来删除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[的会话表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1205218662}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1353384449}

[**[reset aspf session ]{lang="EN-US"}**[\[ **ipv4 \| ipv6** \]]{lang="EN-US"}]{#struct_0_x4698_11175_x455949027}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1761258409}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset aspf session ]{lang="EN-US"}**[\[ **ipv4 \| ipv6** \] \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4698_11175_1856048168}

[[分布式设备－]{style="font-family:宋体"}]{#struct_0_x4698_11175_x1353318913}[IRF]{lang="EN-US"}[模式：]{style="font-family:宋体"}

[**[reset aspf session ]{lang="EN-US"}**[\[ **ipv4 \| ipv6** \] \[ ]{lang="EN-US"}]{#struct_0_x4698_11175_1660004029}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1135992023}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4698_11175_589199943}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_765013294}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x584506823}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x591719144}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1828909864}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4698_11175_1118915419}[：删除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4698_11175_775250384}[：删除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话表项。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x4698_11175_x1353515521}[ *slot-number*]{lang="EN-US"}[：删除指定单板上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。不指定该参数时，删除所有单板上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x4698_11175_x1353449985}[ *slot-number*]{lang="EN-US"}[：删除指定成员设备上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。不指定该参数时，删除所有成员设备上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4698_11175_310998804}[：]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，则]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项]{style="font-family:宋体"}[。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x4698_11175_x994720972}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：删除指定成员设备的指定单板上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。不指定该参数时，删除所有成员设备的所有单板上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}[（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4698_11175_1765981981}[：]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[指定单板]{style="font-family:宋体"}[上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，则]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[所有单板上]{style="font-family:宋体"}[的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项]{style="font-family:宋体"}[。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**]{#struct_0_x4698_11175_652748359}[ *cpu-number*]{lang="EN-US"}[：删除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的会话表项，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。]{style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}[（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1305563854}

[[如果不指定]{style="font-family:宋体"}**[ipv4]{lang="EN-US"}**]{#struct_0_x4698_11175_1343542123}[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则表示删除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的所有会话表项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_391535099}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x1511916469}[清除]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[创建的所有会话表项。]{style="font-family:宋体"}

[[\<Sysname\> reset aspf session]{lang="EN-US"}]{#struct_0_x4698_11175_x1500657307}

[]{#_Toc272768860}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x591784680}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display aspf session]{lang="EN-US"}**]{#struct_0_x4698_11175_1226176699}
:::::

::::: {#-113030061 .myid}
[]{#_Toc404793424}[]{#struct_0_x4698_11175_x189773180}[]{#_Toc313525672}[]{#_Toc298766612}

**ASPF \-- ASPF配置命令 \-- tcp syn-check**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ASPF命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4698_11175_x1093808006}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4698_11175_767472892}
:::

[ ]{lang="EN-US"}

[**[tcp syn-check]{lang="EN-US"}**]{#struct_0_x4698_11175_473134565}[命令用来开启非]{style="font-family:宋体"}[SYN]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文丢弃功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **tcp syn-check**]{lang="EN-US"}]{#struct_0_x4698_11175_x531449618}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x1981934896}

[**[tcp syn-check]{lang="EN-US"}**]{#struct_0_x4698_11175_615894992}

[**[undo]{lang="EN-US"}**[ **tcp syn-check**]{lang="EN-US"}]{#struct_0_x4698_11175_x591850216}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x308468055}

[[不丢弃非]{style="font-family:宋体"}[SYN]{lang="EN-US"}]{#struct_0_x4698_11175_864327229}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x2019658639}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_1076804956}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4698_11175_x445053330}

[[network-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x459629616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4698_11175_x665640185}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4698_11175_1464082829}

[[ASPF]{lang="EN-US"}]{#struct_0_x4698_11175_x591915752}[对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的首报文进行检测，查看是否为]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文，如果不是]{style="font-family:宋体"}[SYN]{lang="EN-US"}[报文则根据当前配置决定是否丢弃该报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4698_11175_470975573}

[[\# ]{lang="EN-US"}]{#struct_0_x4698_11175_x973449647}[设置]{style="font-family:宋体"}[ASPF]{lang="EN-US"}[策略]{style="font-family:宋体"}[1]{lang="EN-US"}[丢弃非]{style="font-family:宋体"}[SYN]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[首报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4698_11175_x1460672240}

[\[Sysname\] aspf policy 1]{lang="EN-US"}

[\[Sysname-aspf-policy-1\] tcp syn-check]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4698_11175_623586961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aspf policy]{lang="EN-US"}**]{#struct_0_x4698_11175_419899612}
:::::
