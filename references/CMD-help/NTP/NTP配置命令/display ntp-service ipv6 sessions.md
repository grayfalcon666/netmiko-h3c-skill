::: {#1118283940 .myid}
[]{#_Toc263348855}[]{#_Toc99531671}[]{#_Toc45103617}[]{#_Toc95306334}[]{#_Toc20563798}[]{#_Toc404796655}[]{#struct_0_19838_x2835_x763041459}[]{#_Toc296433154}

**NTP \-- NTP配置命令 \-- display ntp-service ipv6 sessions**

------------------------------------------------------------------------

[**[dis]{lang="EN-US"}[play ntp-service ipv6 sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_x1788111625}[命令用来显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1030401944}

[**[display ntp-service ipv6 sessions]{lang="EN-US"}**[ \[ **verbose** \]]{lang="EN-US"}]{#struct_0_19838_x2835_2062601018}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1603714089}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1892682244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x79689133}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_967018249}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_x138986452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x277087809}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_x666810206}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x637394489}

[**[verbose]{lang="EN-US"}**]{#struct_0_19838_x2835_x1472655395}[：显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的详细信息。如果不指定该参数，则只显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_620689341}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1867345197}[显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service ipv6 sessions]{lang="EN-US"}]{#struct_0_19838_x2835_966952713}

[Notes: 1 source(master), 2 source(peer), 3 selected, 4 candidate, 5 configured.]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Source:   \[125\]3000::32]{lang="EN-US"}

[ Reference: 127.127.1.0           Clock stratum: 2]{lang="EN-US"}

[ Reachabilities: 1                Poll interval: 64]{lang="EN-US"}

[ Last receive time: 6             Offset: -0.0]{lang="EN-US"}

[ Roundtrip delay: 0.0             Dispersion: 0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total sessions: 1]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ntp-service ipv6 sessions]{lang="EN-US"}]{#struct_0_19838_x2835_x50355826}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x527217077}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_x11692512}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1006358319}

[[\[12345\]]{lang="EN-US"}]{#struct_0_19838_x2835_909753660}

[[1]{lang="EN-US"}]{#struct_0_19838_x2835_615604072}[：系统选中的时间服务器，即当前与设备进行时间同步的时间服务器]{style="font-family:宋体"}

[[2]{lang="EN-US"}]{#struct_0_19838_x2835_966887177}[：该时间服务器的时钟层数小于等于]{style="font-family:宋体"}[15]{lang="EN-US"}

[[3]{lang="EN-US"}]{#struct_0_19838_x2835_x781654275}[：该时间服务器的时钟通过了时钟选择算法]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_19838_x2835_554506138}[：该时间服务器的时钟为候选的时钟]{style="font-family:宋体"}

[[5]{lang="EN-US"}]{#struct_0_19838_x2835_496609140}[：该时间服务器是通过配置命令指定的]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_19838_x2835_x1086540956}

[[时间服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_966821641}[地址。若该字段显示为]{style="font-family:宋体"}[::]{lang="EN-US"}[，表示时间服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[Reference]{lang="EN-US"}]{#struct_0_19838_x2835_x1991430856}

[[时间服务器的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_197119952}

[[当参考时钟为本地时钟时，本字段的显示情况和]{style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x893969549}[字段的取值有关：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_189402387}[[Clock stratum]{lang="EN-US"}]{.TableTextChar}[字段为]{lang="EN-US" style="font-family:
  宋体"}[0]{lang="EN-US"}[或]{lang="EN-US" style="font-family:
  宋体"}[1]{lang="EN-US"}[时，本字段显示为]{lang="EN-US" style="font-family:
  宋体"}[Local]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1078461727}[[Clock stratum]{lang="EN-US"}]{.TableTextChar}[字段为其他值时，本字段显示为]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址前]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位的]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示]{lang="EN-US" style="font-family:宋体"}

[[当参考时钟为网络中其他设备的时钟时，本字段显示为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_967804681}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示。若该字段显示为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[，表示本地设备还未与时间服务器建立连接]{style="font-family:宋体"}

[[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_1613041201}

[[时间服务器的时钟层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1720545143}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_1459751496}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，时钟的准确度最高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[Reachabilities]{lang="EN-US"}]{#struct_0_19838_x2835_967739145}

[[时间服务器的可达性计数，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x2835_1853808281}[表示时间服务器不可达]{style="font-family:宋体"}

[[Poll interval]{lang="EN-US"}]{#struct_0_19838_x2835_1714931945}

[[轮询间隔，即两个连续]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1273983130}[报文之间的时间间隔，单位为秒]{style="font-family:宋体"}

[[Last receive time]{lang="EN-US"}]{#struct_0_19838_x2835_1692539772}

[[最近一次接收到]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_967280394}[报文或更新本地时间到当前时间的时间间隔]{style="font-family:宋体"}

[[缺省单位为秒；如果时间间隔大于]{style="font-family:宋体"}[2048]{lang="EN-US"}]{#struct_0_19838_x2835_x1008809931}[秒，则显示为分钟]{style="font-family:宋体"}[m]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[300]{lang="EN-US"}[分钟，则显示为小时]{style="font-family:宋体"}[h]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[96]{lang="EN-US"}[小时，则显示为天]{style="font-family:宋体"}[d]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[999]{lang="EN-US"}[天，则显示为年]{style="font-family:宋体"}[y]{lang="EN-US"}[；如果最近一次接收到]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文或更新本地时间比当前时间晚，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_19838_x2835_2104961667}

[[系统时钟相对于参考时钟的时钟偏移，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1407284555}

[[Roundtrip delay]{lang="EN-US"}]{#struct_0_19838_x2835_1447302120}

[[本地设备到时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_967214858}

[[Dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_974368287}

[[系统时钟相对于参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_920680448}

[[Total sessions]{lang="EN-US"}]{#struct_0_19838_x2835_x1092676386}

[[总的会话数目]{style="font-family:宋体"}]{#struct_0_19838_x2835_967149322}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x934689081}[显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service ipv6 sessions verbose]{lang="EN-US"}]{#struct_0_19838_x2835_967083786}

[ ]{lang="EN-US"}

[ Clock source: 1::1]{lang="EN-US"}

[ Session ID: 36144]{lang="EN-US"}

[ Clock stratum: 16]{lang="EN-US"}

[ Clock status:  configured, insane, valid, unsynced]{lang="EN-US"}

[ Reference clock ID: INIT]{lang="EN-US"}

[ VPN instance: Not specified]{lang="EN-US"}

[ Local mode: sym_active, local poll interval: 6]{lang="EN-US"}

[ Peer mode: unspec, peer poll interval: 10]{lang="EN-US"}

[ Offset: 0.0000ms, roundtrip delay: 0.0000ms, dispersion:  15937ms]{lang="EN-US"}

[ Root roundtrip delay: 0.0000ms, root dispersion: 0.0000ms]{lang="EN-US"}

[ Reachabilities:0, sync distance: 15.938]{lang="EN-US"}

[ Precision: 2\^10, version: 4, source interface: Not specified]{lang="EN-US"}

[ Reftime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ Orgtime: d17cbb21.0f318106  Tue, May 17 2011  9:15:13.059]{lang="EN-US"}

[ Rcvtime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ Xmttime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ Roundtrip delay samples: 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000]{lang="EN-US"}

[ Offset samples: 0.00  0.00  0.00  0.00  0.00  0.00  0.00  0.00]{lang="EN-US"}

[ Filter order: 0     1     2     3     4     5     6     7]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total sessions: 1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ntp-service ipv6 sessions verbose]{lang="EN-US"}]{#struct_0_19838_x2835_x1283155293}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x530198453}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_1159272842}

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1769718751}

[[Clock source]{lang="EN-US"}]{#struct_0_19838_x2835_x820913237}

[[时间服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_967018250}[地址。若该字段显示为]{style="font-family:宋体"}[::]{lang="EN-US"}[，表示时间服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[Session ID]{lang="EN-US"}]{#struct_0_19838_x2835_x2095301595}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_x1833019534}

[[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x1478677586}

[[时间服务器的时钟层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_767444668}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_x399845834}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，表示时钟的准确度最高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[Clock status]{lang="EN-US"}]{#struct_0_19838_x2835_966952714}

[[会话的状态，该字段的取值及含义为：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x50355831}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[configured]{lang="EN-US"}]{#struct_0_19838_x2835_1944622617}[：表示该会话是配置命令所建立的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_19838_x2835_x1065067939}[：表示该会话是动态生成的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[master]{lang="EN-US"}]{#struct_0_19838_x2835_x53611823}[：表示该会话对应的时间服务器是当前系统的主时间服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[selected]{lang="EN-US"}]{#struct_0_19838_x2835_1517520616}[：表示该会话对应时间服务器的时钟通过了时钟选择算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[candidate]{lang="EN-US"}]{#struct_0_19838_x2835_966887178}[：表示该会话对应时间服务器的时钟为候选时钟]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sane]{lang="EN-US"}]{#struct_0_19838_x2835_x781654290}[：表示该会话对应的时间服务器可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insane]{lang="EN-US"}]{#struct_0_19838_x2835_554833824}[：表示该会话对应的时间服务器不可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_19838_x2835_x231024696}[：表示该会话对应的时间服务器是有效的（通过验证、处于同步状态、层数有效、根延时]{style="font-family:宋体"}[/]{lang="EN-US"}[离差未越界等）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}]{#struct_0_19838_x2835_x1586032838}[：表示该会话对应的时间服务器是无效的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unsynced]{lang="EN-US"}]{#struct_0_19838_x2835_966821642}[：表示该会话对应时间服务器的时钟未同步或层数非法]{style="font-family:宋体"}

[[Reference clock ID]{lang="EN-US"}]{#struct_0_19838_x2835_x1991430859}

[[时间服务器的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_244174119}

[[当参考时钟为本地时钟时，本字段的显示情况和]{style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x215831608}[字段的取值有关：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_967804682}[字段为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[时，本字段显示为]{lang="EN-US" style="font-family:宋体"}[Local]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_1613041202}[字段为其他值时，本字段显示为]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[位的]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示]{lang="EN-US" style="font-family:宋体"}

[[当参考时钟为网络中其他设备的时钟时，本字段显示为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_x1720348535}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示。若该字段显示为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[，表示本地设备还未与时间服务器建立连接]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_19838_x2835_x989924486}

[[时间服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_19838_x2835_967739146}[实例的名称，如果时间服务器位于公网，则显示为]{style="font-family:宋体"}[Not specified]{lang="EN-US"}

[[Local mode]{lang="EN-US"}]{#struct_0_19838_x2835_1853808280}

[[本地设备的工作模式，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_1714997481}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unspec]{lang="EN-US"}]{#struct_0_19838_x2835_x134448992}[：未指定模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_active]{lang="EN-US"}]{#struct_0_19838_x2835_967280391}[：主动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_passive]{lang="EN-US"}]{#struct_0_19838_x2835_x1008809934}[：被动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[client]{lang="EN-US"}]{#struct_0_19838_x2835_x1786721102}[：客户端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_19838_x2835_x772736431}[：服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcast]{lang="EN-US"}]{#struct_0_19838_x2835_967214855}[：广播服务器模式或组播服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bclient]{lang="EN-US"}]{#struct_0_19838_x2835_974368282}[：广播客户端模式或组播客户端模式]{style="font-family:宋体"}

[[local poll interval]{lang="EN-US"}]{#struct_0_19838_x2835_920680451}

[[本地设备的轮询间隔，显示的是]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_19838_x2835_967149319}[的次幂数，单位为秒，比如]{style="font-family:宋体"}[6]{lang="EN-US"}[表示轮询间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[6]{lang="EN-US"}[次幂，即]{style="font-family:宋体"}[64s]{lang="EN-US"}

[[Peer mode]{lang="EN-US"}]{#struct_0_19838_x2835_639289022}

[[对端设备的工作模式，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x707249102}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unspec]{lang="EN-US"}]{#struct_0_19838_x2835_1141836338}[：未指定模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_active]{lang="EN-US"}]{#struct_0_19838_x2835_967083783}[：主动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_passive]{lang="EN-US"}]{#struct_0_19838_x2835_x1283155296}[：被动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[client]{lang="EN-US"}]{#struct_0_19838_x2835_399757955}[：客户端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_19838_x2835_x1006029030}[：服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcast]{lang="EN-US"}]{#struct_0_19838_x2835_967018247}[：广播服务器模式或组播服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bclient]{lang="EN-US"}]{#struct_0_19838_x2835_x138986454}[：广播客户端模式或组播客户端模式]{style="font-family:宋体"}

[[peer poll interval]{lang="EN-US"}]{#struct_0_19838_x2835_x276694593}

[[对端设备的轮询间隔，显示的是]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_19838_x2835_966952711}[的次幂数，单位为秒，比如]{style="font-family:宋体"}[6]{lang="EN-US"}[表示轮询间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[6]{lang="EN-US"}[次幂，即]{style="font-family:宋体"}[64s]{lang="EN-US"}

[[Offset]{lang="EN-US"}]{#struct_0_19838_x2835_x50355828}

[[系统时钟相对于参考时钟的时钟偏移，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x11692510}

[[roundtrip delay]{lang="EN-US"}]{#struct_0_19838_x2835_966887175}

[[本地设备到时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x781654277}

[[dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_554375066}

[[系统时钟相对于参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x167890054}

[[Root roundtrip delay]{lang="EN-US"}]{#struct_0_19838_x2835_966821639}

[[本地设备到主时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_729558336}

[[root dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_x1378885447}

[[系统时钟相对主参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_967804679}

[[Reachabilities]{lang="EN-US"}]{#struct_0_19838_x2835_1275334201}

[[时间服务器的可达性计数，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x2835_x496302186}[表示时间服务器不可达]{style="font-family:宋体"}

[[sync distance]{lang="EN-US"}]{#struct_0_19838_x2835_967739143}

[[表示相对上一级时间服务器的同步距离，由误差]{style="font-family:宋体"}[disper]{lang="EN-US"}]{#struct_0_19838_x2835_1853808275}[和往返时延]{style="font-family:宋体"}[delay]{lang="EN-US"}[计算而来，单位为秒]{style="font-family:宋体"}

[[Precision]{lang="EN-US"}]{#struct_0_19838_x2835_1715194086}

[[系统时钟的精度]{style="font-family:宋体"}]{#struct_0_19838_x2835_967280392}

[[version]{lang="EN-US"}]{#struct_0_19838_x2835_x1008809933}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1027206215}[版本，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}

[[source interface]{lang="EN-US"}]{#struct_0_19838_x2835_967214856}

[[源接口，未指定源接口时，此字段显示为]{style="font-family:宋体"}[Not specified]{lang="EN-US"}]{#struct_0_19838_x2835_974368285}

[[Reftime]{lang="EN-US"}]{#struct_0_19838_x2835_967149320}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x934689083}[报文中的参考时间戳]{style="font-family:宋体"}

[[Orgtime]{lang="EN-US"}]{#struct_0_19838_x2835_x1058008294}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_967083784}[报文中的起始时间戳]{style="font-family:宋体"}

[[Rcvtime]{lang="EN-US"}]{#struct_0_19838_x2835_x1283155295}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1965841896}[报文的接收时间戳]{style="font-family:宋体"}

[[Xmttime]{lang="EN-US"}]{#struct_0_19838_x2835_967018248}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x138986451}[报文的发送时间戳]{style="font-family:宋体"}

[[Roundtrip delay samples]{lang="EN-US"}]{#struct_0_19838_x2835_966952712}

[[本地设备到时间服务器往返时延的抽样值]{style="font-family:宋体"}]{#struct_0_19838_x2835_x50355825}

[[Offset samples]{lang="EN-US"}]{#struct_0_19838_x2835_x11692515}

[[相对于参考时钟的时钟偏移的抽样值]{style="font-family:宋体"}]{#struct_0_19838_x2835_966887176}

[[Filter order]{lang="EN-US"}]{#struct_0_19838_x2835_x781654276}

[[样本信息排序]{style="font-family:宋体"}]{#struct_0_19838_x2835_966821640}

[[Reference clock status]{lang="EN-US"}]{#struct_0_19838_x2835_x1991430857}

[[本地时钟的工作状态，只有通过]{style="font-family:宋体"}**[ntp-service refclock-master]{lang="EN-US"}**]{#struct_0_19838_x2835_1763203893}[命令设置本地时钟作为参考时钟时，才会显示该字段]{style="font-family:宋体"}

[[当本地时钟的]{style="font-family:宋体"}[reach]{lang="EN-US"}]{#struct_0_19838_x2835_967804680}[值等于]{style="font-family:宋体"}[255]{lang="EN-US"}[时，该字段取值为]{style="font-family:宋体"}[working normally]{lang="EN-US"}[；否则，该字段取值为]{style="font-family:宋体"}[working abnormally]{lang="EN-US"}

[[Total sessions]{lang="EN-US"}]{#struct_0_19838_x2835_1613041200}

[[总的会话数目]{style="font-family:宋体"}]{#struct_0_19838_x2835_967739144}

[ ]{lang="EN-US"}

::: {#545500664 .myid}
[]{#_Toc404796656}[]{#struct_0_19838_x2835_1853808282}[]{#_Toc296433155}

**NTP \-- NTP配置命令 \-- display ntp-service sessions**

------------------------------------------------------------------------

[**[display ntp-service sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_1714866409}[命令用来显示]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1731138222}

[**[display ntp-service sessions ]{lang="EN-US"}**[\[ **verbose** \]]{lang="EN-US"}]{#struct_0_19838_x2835_x1489638724}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1409002896}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_1720662699}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1469702948}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_967280389}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_947505194}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1348608520}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_533837411}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1537159631}

[**[verbose]{lang="EN-US"}**]{#struct_0_19838_x2835_x1949153991}[：显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话的详细信息。如果不指定该参数，则只显示所有会话的简要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x146796678}

[[设备作为]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1413895630}[广播服务器或]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播服务器时，在设备上执行]{style="font-family:宋体"}**[display ntp-service sessions]{lang="EN-US"}**[命令不会显示与该广播服务器或组播服务器对应的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话信息，但是这些会话会统计在总的会话数中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_967214853}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_974368280}[显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service sessions]{lang="EN-US"}]{#struct_0_19838_x2835_920680453}

[       source          reference       stra reach poll  now offset  delay disper]{lang="EN-US"}

[\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*]{lang="EN-US"}

[\[12345\]LOCAL(0)        LOCL               0     1   64    - 0.0000 0.0000 7937.9]{lang="EN-US"}

[    \[5\]0.0.0.0         INIT              16     0   64    - 0.0000 0.0000 0.0000]{lang="EN-US"}

[Notes: 1 source(master), 2 source(peer), 3 selected, 4 candidate, 5 configured.]{lang="EN-US"}

[ Total sessions: 1]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ntp-service sessions]{lang="EN-US"}]{#struct_0_19838_x2835_1245975783}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x509136725}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_967149317}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_639289028}

[[source]{lang="EN-US"}]{#struct_0_19838_x2835_x707249112}

[[参考时钟为本地时钟时，显示为]{style="font-family:宋体"}[LOCAL(*number*)]{lang="EN-US"}]{#struct_0_19838_x2835_1141836339}[，表示本地时钟的地址为]{style="font-family:宋体"}[127.127.1.*number*]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的进程号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}

[[参考时钟为网络中其他设备的时钟时，显示为时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_x1688238291}[地址。若该字段显示为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，表示时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[reference]{lang="EN-US"}]{#struct_0_19838_x2835_528907911}

[[时间服务器的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_967083781}

[[当参考时钟为本地时钟时，本字段的显示情况和]{style="font-family:宋体"}[stra]{lang="EN-US"}]{#struct_0_19838_x2835_x1283155298}[字段的取值有关：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19838_x2835_1918787729}[stra]{lang="EN-US"}[字段为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[时，本字段将显示为]{style="font-family:宋体"}[LOCL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_19838_x2835_2088008033}[stra]{lang="EN-US"}[字段为其他值时，本字段将显示为本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[当参考时钟为网络中其他设备的时钟时，本字段显示为该设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_967018245}[地址，若该设备为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[设备，则本字段显示为该设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示。若该字段显示为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[，表示本地设备还未与时间服务器建立连接]{style="font-family:宋体"}

[[stra]{lang="EN-US"}]{#struct_0_19838_x2835_x138986456}

[[时间服务器的时钟层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x276825665}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_1320378578}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，表示时钟的准确度最高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[reach]{lang="EN-US"}]{#struct_0_19838_x2835_747362522}

[[时间服务器的可达性计数，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x2835_966952709}[表示时间服务器不可达]{style="font-family:宋体"}

[[poll]{lang="EN-US"}]{#struct_0_19838_x2835_x2006670972}

[[轮询间隔，即两个连续]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1024538941}[报文之间的时间间隔，单位为秒]{style="font-family:宋体"}

[[now]{lang="EN-US"}]{#struct_0_19838_x2835_x1948372486}

[[最近一次接收到]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_939215855}[报文或更新本地时间到当前时间的时间间隔]{style="font-family:宋体"}

[[缺省单位为秒；如果时间间隔大于]{style="font-family:宋体"}[2048]{lang="EN-US"}]{#struct_0_19838_x2835_966887173}[秒，则显示为分钟]{style="font-family:宋体"}[m]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[300]{lang="EN-US"}[分钟，则显示为小时]{style="font-family:宋体"}[h]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[96]{lang="EN-US"}[小时，则显示为天]{style="font-family:宋体"}[d]{lang="EN-US"}[；如果时间间隔大于]{style="font-family:宋体"}[999]{lang="EN-US"}[天，则显示为年]{style="font-family:宋体"}[y]{lang="EN-US"}[；如果最近一次接收到]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文或更新本地时间比当前时间晚，则显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[offset]{lang="EN-US"}]{#struct_0_19838_x2835_x781654279}

[[系统时钟相对于参考时钟的时钟偏移，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_554243994}

[[delay]{lang="EN-US"}]{#struct_0_19838_x2835_x1739109172}

[[本地设备到时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_230735084}

[[disper]{lang="EN-US"}]{#struct_0_19838_x2835_966821637}

[[系统时钟相对于参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_729558330}

[[\[12345\]]{lang="EN-US"}]{#struct_0_19838_x2835_x1378885453}

[[1]{lang="EN-US"}]{#struct_0_19838_x2835_481925522}[：系统选中的时间服务器，即当前与设备进行时间同步的时间服务器]{style="font-family:宋体"}

[[2]{lang="EN-US"}]{#struct_0_19838_x2835_967804677}[：该时间服务器的时钟层数小于等于]{style="font-family:宋体"}[15]{lang="EN-US"}

[[3]{lang="EN-US"}]{#struct_0_19838_x2835_1275334199}[：该时间服务器的时钟通过了时钟选择算法]{style="font-family:宋体"}

[[4]{lang="EN-US"}]{#struct_0_19838_x2835_1077151631}[：该时间服务器的时钟为候选时钟]{style="font-family:宋体"}

[[5]{lang="EN-US"}]{#struct_0_19838_x2835_1907343436}[：该时间服务器的时钟是配置命令指定的]{style="font-family:宋体"}

[[Total sessions]{lang="EN-US"}]{#struct_0_19838_x2835_967739141}

[[总的会话数目]{style="font-family:宋体"}]{#struct_0_19838_x2835_1853808277}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1715063014}[显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service sessions verbose]{lang="EN-US"}]{#struct_0_19838_x2835_967280390}

[ Clock source: 192.168.1.40]{lang="EN-US"}

[ Session ID: 35888]{lang="EN-US"}

[ Clock stratum: 2]{lang="EN-US"}

[ Clock status:  configured, master, sane, valid]{lang="EN-US"}

[ Reference clock ID: 127.127.1.0]{lang="EN-US"}

[ VPN instance: Not specified]{lang="EN-US"}

[ Local mode: client, local poll interval: 6]{lang="EN-US"}

[ Peer mode: server, peer poll interval: 6]{lang="EN-US"}

[ Offset: 0.2862ms, roundtrip delay: 3.2653ms, dispersion: 4.5166ms]{lang="EN-US"}

[ Root roundtrip delay: 0.0000ms, root dispersion: 10.910ms]{lang="EN-US"}

[ Reachabilities:31, sync distance: 0.0194]{lang="EN-US"}

[ Precision: 2\^18, version: 3, source interface: Not specified]{lang="EN-US"}

[ Reftime: d17cbba5.1473de1e  Tue, May 17 2011  9:17:25.079]{lang="EN-US"}

[ Orgtime: 00000000.00000000  Thu, Feb  7 2036  6:28:16.000]{lang="EN-US"}

[ Rcvtime: d17cbbc0.b1959a30  Tue, May 17 2011  9:17:52.693]{lang="EN-US"}

[ Xmttime: d17cbbc0.b1959a30  Tue, May 17 2011  9:17:52.693]{lang="EN-US"}

[ Roundtrip delay samples: 0.007 0.010 0.006 0.011 0.010 0.005 0.007 0.003]{lang="EN-US"}

[ Offset samples: 5629.55 3913.76 5247.27 6526.92 31.99 148.72 38.27 0.29]{lang="EN-US"}

[ Filter order: 7     5     2     6     0     4     1     3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total sessions: 1]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ntp-service sessions verbose]{lang="EN-US"}]{#struct_0_19838_x2835_x1008809935}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x516649493}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_x220637161}

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1358394111}

[[Clock source]{lang="EN-US"}]{#struct_0_19838_x2835_631270106}

[[时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_967214854}[地址。若该字段显示为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，表示时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[Session ID]{lang="EN-US"}]{#struct_0_19838_x2835_974368283}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_920680452}

[[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_1245975784}

[[时间服务器的时钟层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x727718682}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_967149318}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，表示时钟的准确度越高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[Clock status]{lang="EN-US"}]{#struct_0_19838_x2835_639289021}

[[会话的状态，该字段的取值及含义为：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x707249103}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[configured]{lang="EN-US"}]{#struct_0_19838_x2835_1141901874}[：表示该会话是配置命令所建立的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dynamic]{lang="EN-US"}]{#struct_0_19838_x2835_663926605}[：表示该会话是动态生成的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[master]{lang="EN-US"}]{#struct_0_19838_x2835_1080430112}[：表示该会话对应的时间服务器是当前系统的主时间服务器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[selected]{lang="EN-US"}]{#struct_0_19838_x2835_967083782}[：表示该会话对应时间服务器的时钟通过了时钟选择算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[candidate]{lang="EN-US"}]{#struct_0_19838_x2835_x1283155297}[：表示该会话对应时间服务器的时钟为候选时钟]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sane]{lang="EN-US"}]{#struct_0_19838_x2835_x1166325986}[：表示该会话对应的时间服务器通过身份验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[insane]{lang="EN-US"}]{#struct_0_19838_x2835_1616913126}[：表示该会话对应的时间服务器未通过身份验证]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[valid]{lang="EN-US"}]{#struct_0_19838_x2835_x421812690}[：表示该会话对应的时间服务器是有效的（通过验证、处于同步状态、层数有效、根延时]{style="font-family:宋体"}[/]{lang="EN-US"}[离差未越界等）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[invalid]{lang="EN-US"}]{#struct_0_19838_x2835_967018246}[：表示该会话对应的时间服务器是无效的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unsynced]{lang="EN-US"}]{#struct_0_19838_x2835_x138986453}[：表示该会话对应时间服务器的时钟未同步或层数非法]{style="font-family:宋体"}

[[Reference clock ID]{lang="EN-US"}]{#struct_0_19838_x2835_x277022273}

[[时间服务器的参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_2140728014}

[[当参考时钟为本地时钟时，本字段的显示情况和]{style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x959587315}[字段的取值有关：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_966952710}[字段取值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[时，本字段将显示为]{lang="EN-US" style="font-family:宋体"}[LOCL]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{lang="EN-US" style="font-family:宋体"}[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x50355827}[字段取值为其他值时，本字段将显示为本地时钟的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[当参考时钟为网络中其他设备的时钟时，本字段显示为该设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_x11692513}[地址，若该设备为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[设备，则本字段显示为该设备的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值，摘要信息按照点分十进制形式显示。若该字段显示为]{style="font-family:宋体"}[INIT]{lang="EN-US"}[，表示本地设备还未与时间服务器建立连接]{style="font-family:宋体"}

[[VPN instance]{lang="EN-US"}]{#struct_0_19838_x2835_966887174}

[[时间服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_19838_x2835_x781654278}[实例的名称，如果时间服务器位于公网，则显示为]{style="font-family:宋体"}[Not specified]{lang="EN-US"}

[[Local mode]{lang="EN-US"}]{#struct_0_19838_x2835_554309530}

[[本地设备的工作模式，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_1401083136}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unspec]{lang="EN-US"}]{#struct_0_19838_x2835_966821638}[：未指定模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_active]{lang="EN-US"}]{#struct_0_19838_x2835_729558335}[：主动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_passive]{lang="EN-US"}]{#struct_0_19838_x2835_x1378885448}[：被动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[client]{lang="EN-US"}]{#struct_0_19838_x2835_x1890793009}[：客户端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_19838_x2835_967804678}[：服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcast]{lang="EN-US"}]{#struct_0_19838_x2835_1275334200}[：广播服务器模式或组播服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bclient]{lang="EN-US"}]{#struct_0_19838_x2835_x496367722}[：广播客户端模式或组播客户端模式]{style="font-family:宋体"}

[[local poll interval]{lang="EN-US"}]{#struct_0_19838_x2835_1459657313}

[[本地设备的轮询间隔，显示的是]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_19838_x2835_967739142}[的次幂数，单位为秒，比如]{style="font-family:宋体"}[6]{lang="EN-US"}[表示轮询间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[6]{lang="EN-US"}[次幂，即]{style="font-family:宋体"}[64s]{lang="EN-US"}

[[Peer mode]{lang="EN-US"}]{#struct_0_19838_x2835_1853808276}

[[对端设备的工作模式，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_1715128550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unspec]{lang="EN-US"}]{#struct_0_19838_x2835_218016224}[：未指定模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_active]{lang="EN-US"}]{#struct_0_19838_x2835_x1405372602}[：主动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_passive]{lang="EN-US"}]{#struct_0_19838_x2835_x1145330703}[：被动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[client]{lang="EN-US"}]{#struct_0_19838_x2835_x426682352}[：客户端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_19838_x2835_x744822061}[：服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcast]{lang="EN-US"}]{#struct_0_19838_x2835_x1405438138}[：广播服务器模式或组播服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bclient]{lang="EN-US"}]{#struct_0_19838_x2835_1862612430}[：广播客户端模式或组播客户端模式]{style="font-family:宋体"}

[[peer poll interval]{lang="EN-US"}]{#struct_0_19838_x2835_x224707395}

[[对端设备的轮询间隔，显示的是]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_19838_x2835_x1405503674}[的次幂数，单位为秒，比如]{style="font-family:宋体"}[6]{lang="EN-US"}[表示轮询间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[6]{lang="EN-US"}[次幂，即]{style="font-family:宋体"}[64s]{lang="EN-US"}

[[Offset]{lang="EN-US"}]{#struct_0_19838_x2835_609717838}

[[系统时钟相对于参考时钟的时钟偏移，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_1808897527}

[[roundtrip delay]{lang="EN-US"}]{#struct_0_19838_x2835_x1749253963}

[[本地设备到时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405569210}

[[dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_x65434628}

[[系统时钟相对于参考时钟的最大误差]{style="font-family:宋体"}]{#struct_0_19838_x2835_730936989}

[[Root roundtrip delay]{lang="EN-US"}]{#struct_0_19838_x2835_x1405634746}

[[本地设备到主时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_881366602}

[[root dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_x836237404}

[[系统时钟相对主参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405700282}

[[Reachabilities]{lang="EN-US"}]{#struct_0_19838_x2835_x681925356}

[[时间服务器的可达性计数，]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x2835_1171688528}[表示时间服务器不可达]{style="font-family:宋体"}

[[sync distance]{lang="EN-US"}]{#struct_0_19838_x2835_x1405765818}

[[表示相对上一级时间服务器的同步距离，由误差]{style="font-family:宋体"}[disper]{lang="EN-US"}]{#struct_0_19838_x2835_x240439074}[和往返时延]{style="font-family:宋体"}[delay]{lang="EN-US"}[计算而来，单位为秒]{style="font-family:宋体"}

[[Precision]{lang="EN-US"}]{#struct_0_19838_x2835_1834298054}

[[系统时钟的精度]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405831354}

[[version]{lang="EN-US"}]{#struct_0_19838_x2835_x963793648}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1404848314}[版本，取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}

[[source interface]{lang="EN-US"}]{#struct_0_19838_x2835_1753336232}

[[源接口，未指定源接口时，此字段显示为]{style="font-family:宋体"}[Not specified]{lang="EN-US"}]{#struct_0_19838_x2835_1021340046}

[[Reftime]{lang="EN-US"}]{#struct_0_19838_x2835_x1404913850}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_984541890}[报文中的参考时间戳]{style="font-family:宋体"}

[[Orgtime]{lang="EN-US"}]{#struct_0_19838_x2835_1493435858}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405372601}[报文中的起始时间戳]{style="font-family:宋体"}

[[Rcvtime]{lang="EN-US"}]{#struct_0_19838_x2835_420753238}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1313678796}[报文的接收时间戳]{style="font-family:宋体"}

[[Xmttime]{lang="EN-US"}]{#struct_0_19838_x2835_x1405438137}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x153810205}[报文的发送时间戳]{style="font-family:宋体"}

[[Roundtrip delay samples]{lang="EN-US"}]{#struct_0_19838_x2835_x1405503673}

[[本地设备到时间服务器往返时延的抽样值]{style="font-family:宋体"}]{#struct_0_19838_x2835_1013002365}

[[Offset samples]{lang="EN-US"}]{#struct_0_19838_x2835_x2073289739}

[[相对于参考时钟的时钟偏移的抽样值]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405569209}

[[Filter order]{lang="EN-US"}]{#struct_0_19838_x2835_1856945209}

[[抽样信息排序]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405634745}

[[Reference clock status]{lang="EN-US"}]{#struct_0_19838_x2835_x1847516753}

[[本地时钟的工作状态，只有通过]{style="font-family:宋体"}**[ntp-service refclock-master]{lang="EN-US"}**]{#struct_0_19838_x2835_1069320701}[命令设置本地时钟作为参考时钟时，才会显示该字段]{style="font-family:宋体"}

[[当本地时钟的]{style="font-family:宋体"}[reach]{lang="EN-US"}]{#struct_0_19838_x2835_x1405700281}[值等于]{style="font-family:宋体"}[255]{lang="EN-US"}[时，该字段取值为]{style="font-family:宋体"}[working normally]{lang="EN-US"}[；否则，该字段取值为]{style="font-family:宋体"}[working abnormally]{lang="EN-US"}

[[Total sessions]{lang="EN-US"}]{#struct_0_19838_x2835_x278640829}

[[总的会话数目]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405765817}

[ ]{lang="EN-US"}

::: {#139705391 .myid}
[]{#_Toc404796657}[]{#struct_0_19838_x2835_2132213921}[]{#_Toc296433156}

**NTP \-- NTP配置命令 \-- display ntp-service status**

------------------------------------------------------------------------

[**[display ntp-service status]{lang="EN-US"}**]{#struct_0_19838_x2835_x229016335}[命令用来显示]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[服务的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1905912001}

[**[display ntp-service status]{lang="EN-US"}**]{#struct_0_19838_x2835_1466335841}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1650681102}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1109727287}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2087181568}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1405831353}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_602290293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1408958517}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_x1787705444}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1117912829}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_129562203}[时间已同步时，显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service status]{lang="EN-US"}]{#struct_0_19838_x2835_x1404848313}

[ Clock status: synchronized]{lang="EN-US"}

[ Clock stratum: 2]{lang="EN-US"}

[ System peer: LOCAL(0)]{lang="EN-US"}

[ Local mode: client]{lang="EN-US"}

[ Reference clock ID: 127.127.1.0]{lang="EN-US"}

[ Leap indicator: 00]{lang="EN-US"}

[ Clock jitter: 0.000977 s]{lang="EN-US"}

[ Stability: 0.000 pps]{lang="EN-US"}

[ Clock precision: 2\^-10]{lang="EN-US"}

[ Root delay: 0.00000 ms]{lang="EN-US"}

[ Root dispersion: 3.96367 ms]{lang="EN-US"}

[ Reference time: d0c5fc32.92c70b1e  Wed, Dec 29 2010 18:28:02.573]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1782116177}[时间未同步时，显示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service status]{lang="EN-US"}]{#struct_0_19838_x2835_x1255774707}

[ Clock status: unsynchronized]{lang="EN-US"}

[ Clock stratum: 16]{lang="EN-US"}

[ Reference clock ID: none]{lang="EN-US"}

[ Clock jitter: 0.000000 s]{lang="EN-US"}

[ Stability: 0.000 pps]{lang="EN-US"}

[ Clock precision: 2\^-10]{lang="EN-US"}

[ Root delay: 0.00000 ms]{lang="EN-US"}

[ Root dispersion: 0.00002 ms]{lang="EN-US"}

[ Reference time: d0c5fc32.92c70b1e  Wed, Dec 29 2010 18:28:02.573]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ntp-service status]{lang="EN-US"}]{#struct_0_19838_x2835_x1555361712}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x494966837}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1404913849}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_x937706875}

[[Clock status]{lang="EN-US"}]{#struct_0_19838_x2835_x1578894977}

[[系统时间的状态，取值为：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1924767026}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[synchronized]{lang="EN-US"}]{#struct_0_19838_x2835_220880398}[：系统时间已同步]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unsynchronized]{lang="EN-US"}]{#struct_0_19838_x2835_1849205198}[：系统时间未同步]{lang="EN-US" style="font-family:宋体"}

[[Clock stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x364059074}

[[系统时钟的层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405372604}

[[System peer]{lang="EN-US"}]{#struct_0_19838_x2835_x338761649}

[[系统时钟选中的时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_1948020247}[地址]{style="font-family:宋体"}

[[Local mode]{lang="EN-US"}]{#struct_0_19838_x2835_198919130}

[[相对于选中的时间服务器，本地设备的工作模式，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_975760366}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unspec]{lang="EN-US"}]{#struct_0_19838_x2835_396354719}[：未指定模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_active]{lang="EN-US"}]{#struct_0_19838_x2835_x1405438140}[：主动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[sym_passive]{lang="EN-US"}]{#struct_0_19838_x2835_x2076321114}[：被动对等体模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[client]{lang="EN-US"}]{#struct_0_19838_x2835_1350775053}[：客户端模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[server]{lang="EN-US"}]{#struct_0_19838_x2835_x920134226}[：服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[broadcast]{lang="EN-US"}]{#struct_0_19838_x2835_1051405927}[：广播服务器模式或组播服务器模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[bclient]{lang="EN-US"}]{#struct_0_19838_x2835_x1405503676}[：广播客户端模式或组播客户端模式]{style="font-family:宋体"}

[[Reference clock ID]{lang="EN-US"}]{#struct_0_19838_x2835_1772517252}

[[参考时钟]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_676690789}

[[(1)[    ]{style="font:7.0pt "}]{lang="EN-US"}[对于]{style="font-family:宋体"}[IPv4 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x837261533}[服务器：]{style="font-family:宋体"}

[[本地设备从远程时间服务器获取时间同步时，表示远程服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_1010920787}[地址]{style="font-family:宋体"}

[[本地设备从本地时钟获取时间同步时，表示本地时钟的标识：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405569212}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地时钟的层数为]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1228234042}[1]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[Local]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地时钟的层数为其他值时，显示为本地时钟的]{style="font-family:宋体"}]{#struct_0_19838_x2835_942211912}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[(2)[    ]{style="font:7.0pt "}]{lang="EN-US"}[对于]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_282356538}[服务器：]{style="font-family:宋体"}

[[本地设备从远程时间服务器获取时间同步时，表示远程服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_x1405634748}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值]{style="font-family:宋体"}

[[本地设备从本地时钟获取时间同步时，表示本地时钟的标识：]{style="font-family:宋体"}]{#struct_0_19838_x2835_1331705296}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地时钟的层数为]{style="font-family:宋体"}]{#struct_0_19838_x2835_530894252}[1]{lang="EN-US"}[时，显示为]{style="font-family:宋体"}[Local]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地时钟的层数为其他值时，显示为本地时钟的]{style="font-family:宋体"}]{#struct_0_19838_x2835_920135847}[IPv6]{lang="EN-US"}[地址前]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[摘要值]{style="font-family:宋体"}

[[Leap indicator]{lang="EN-US"}]{#struct_0_19838_x2835_x1405700284}

[[告警状态，取值包括：]{style="font-family:宋体"}]{#struct_0_19838_x2835_480874058}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[00]{lang="EN-US"}]{#struct_0_19838_x2835_x1375072444}[：正常状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[01]{lang="EN-US"}]{#struct_0_19838_x2835_x534157625}[：闰秒标志，表示一天中的最后一分钟有]{style="font-family:宋体"}[61]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[10]{lang="EN-US"}]{#struct_0_19838_x2835_x1405765820}[：闰秒标志，表示一天中的最后一分钟有]{style="font-family:宋体"}[59]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[11]{lang="EN-US"}]{#struct_0_19838_x2835_x596734970}[：时间未被同步的告警状态]{style="font-family:宋体"}

[[Clock jitter]{lang="EN-US"}]{#struct_0_19838_x2835_x1836255052}

[[系统时钟相对于参考时钟的偏移量，单位为秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_387031566}

[[Stability]{lang="EN-US"}]{#struct_0_19838_x2835_x1405831356}

[[时钟频率的稳定性，取值越小，时钟频率越稳定]{style="font-family:宋体"}]{#struct_0_19838_x2835_199005766}

[[Clock precision]{lang="EN-US"}]{#struct_0_19838_x2835_877645134}

[[系统时钟的精度]{style="font-family:宋体"}]{#struct_0_19838_x2835_55040396}

[[Root delay]{lang="EN-US"}]{#struct_0_19838_x2835_x1404848316}

[[本地设备到主时间服务器的往返时延，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1378831650}

[[Root dispersion]{lang="EN-US"}]{#struct_0_19838_x2835_1075665340}

[[系统时钟相对主参考时钟的最大误差，单位为毫秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1141468526}

[[Reference time]{lang="EN-US"}]{#struct_0_19838_x2835_x1404913852}

[[参考时间戳]{style="font-family:宋体"}]{#struct_0_19838_x2835_x178257524}

[ ]{lang="EN-US"}

::: {#569752568 .myid}
[]{#_Toc404796658}[]{#struct_0_19838_x2835_x873576222}[]{#_Toc296433157}

**NTP \-- NTP配置命令 \-- display ntp-service trace**

------------------------------------------------------------------------

[**[display ntp-service trace]{lang="EN-US"}**]{#struct_0_19838_x2835_265207296}[命令用来显示从本地设备回溯到主时间服务器的各个]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[时间服务器的简要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x308072621}

[**[display ntp-service trace]{lang="EN-US"}**]{#struct_0_19838_x2835_x1808464054}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405372603}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_1583552652}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1787268499}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1817498324}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_499951995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1890396765}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_1891123716}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2024408386}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x166939298}[显示从本地设备回溯到主时间服务器的各个]{style="font-family:宋体"}[NTP]{lang="EN-US"}[时间服务器的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ntp-service trace]{lang="EN-US"}]{#struct_0_19838_x2835_x1405438139}

[Server     127.0.0.1]{lang="EN-US"}

[Stratum    3, jitter  0.000, synch distance 0.0000.]{lang="EN-US"}

[Server     3000::32]{lang="EN-US"}

[Stratum    2 , jitter 790.00, synch distance 0.0000.]{lang="EN-US"}

[RefID      127.127.1.0]{lang="EN-US"}

[[以上信息显示了服务器]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}]{#struct_0_19838_x2835_296528489}[的同步链：服务器]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[同步到服务器]{style="font-family:宋体"}[3000::32]{lang="EN-US"}[，服务器]{style="font-family:宋体"}[3000::32]{lang="EN-US"}[从本地时钟得到同步。]{style="font-family:宋体"}

[[表1-6 ]{lang="EN-US"}[display ntp-service trace]{lang="EN-US"}]{#struct_0_19838_x2835_1029511550}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x499152917}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_981182421}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_449771040}

[[Server]{lang="EN-US"}]{#struct_0_19838_x2835_x446020593}

[[时间服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405503675}[地址]{style="font-family:宋体"}

[[Stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x2119165517}

[[表示相应服务器的时钟层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2117933117}

[[jitter]{lang="EN-US"}]{#struct_0_19838_x2835_1423649468}

[[表示相对上一级时钟的时钟偏差的均方根，单位为秒]{style="font-family:宋体"}]{#struct_0_19838_x2835_x498512629}

[[synch distance]{lang="EN-US"}]{#struct_0_19838_x2835_2116369614}

[[表示相对上一级时间服务器的同步距离，由误差]{style="font-family:宋体"}[disper]{lang="EN-US"}]{#struct_0_19838_x2835_x1405569211}[和往返时延]{style="font-family:宋体"}[delay]{lang="EN-US"}[计算而来，单位为秒]{style="font-family:宋体"}

[[RefID]{lang="EN-US"}]{#struct_0_19838_x2835_1500649313}

[[主时间服务器的标识，主参考时钟的层数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_19838_x2835_x285655781}[时，显示为]{style="font-family:宋体"}[Local]{lang="EN-US"}[；为其他值时，显示为主参考时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-341715587 .myid}
[]{#_Toc404796659}[]{#struct_0_19838_x2835_x1552118725}[]{#_Toc296433158}

**NTP \-- NTP配置命令 \-- ntp-service acl**

------------------------------------------------------------------------

[**[ntp-service acl]{lang="EN-US"}**]{#struct_0_19838_x2835_2091884120}[命令用来设置对端设备对本地设备]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务的访问控制权限。]{style="font-family:宋体"}

[**[undo ntp-service acl]{lang="EN-US"}**]{#struct_0_19838_x2835_x228581998}[命令用来取消设置的访问控制权限。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1578928675}

[**[ntp-service]{lang="EN-US"}**[ { **peer** \| **query** \| **server** \| **synchronization** } **acl** *acl-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x1405634747}

[**[undo ntp-service]{lang="EN-US"}**[ { **peer** \| **query** \| **server** \| **synchronization** } **acl** *acl-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x684717339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x627268902}

[[对端设备对本地设备]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x108878451}[服务的访问控制权限为]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_226989753}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x549030269}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_960827495}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1956572124}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x978208007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405700283}

[**[peer]{lang="EN-US"}**]{#struct_0_19838_x2835_884158585}[：完全访问权限。该权限既允许对端设备向本地设备的时间同步，对本地设备进行控制查询（查询]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的一些状态，比如告警信息、验证状态、时间服务器信息等），同时本地设备也可以向对端设备的时间同步。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_19838_x2835_x936247484}[：仅具有控制查询的权限。该权限只允许对端设备对本地设备的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务进行控制查询，但是不能向本地设备的时间同步。]{style="font-family:宋体"}

[**[server]{lang="EN-US"}**]{#struct_0_19838_x2835_x1568635880}[：服务器访问与查询权限。该权限允许对端设备向本地设备的时间同步，对本地设备进行控制查询，但本地设备不会向对端设备的时间同步。]{style="font-family:宋体"}

[**[synchronization]{lang="EN-US"}**]{#struct_0_19838_x2835_19875984}[：仅具有访问服务器的权限。该权限只允许对端设备向本地设备的时间同步，但不能进行控制查询。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_19838_x2835_2082063066}[：指定应用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Control List]{lang="EN-US"}[，访问控制列表）。通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[过滤的对端设备具有本命令中指定的访问控制权限。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为基本访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x465439140}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x330698485}[服务的访问控制权限从高到低依次为]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[、]{style="font-family:宋体"}**[server]{lang="EN-US"}**[、]{style="font-family:宋体"}**[synchronization]{lang="EN-US"}**[、]{style="font-family:宋体"}**[query]{lang="EN-US"}**[。当设备接收到一个]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务请求时，会按照权限从高到低的顺序依次进行匹配，第一个匹配的权限为此设备具有的访问控制权限。如果没有匹配的权限，则不允许对端设备与本地设备进行时间同步、对本端进行控制查询，也不允许本端设备与对端设备进行时间同步。]{style="font-family:宋体"}

[**[ntp-service acl]{lang="EN-US"}**]{#struct_0_19838_x2835_x306673739}[命令提供了一种最小限度的安全措施，更安全的方法是进行身份验证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405765819}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1325644867}[配置]{style="font-family:宋体"}[10.10.0.0/16]{lang="EN-US"}[网段的对端设备对本地设备具有完全访问权限。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_587882796}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 10.10.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] ntp-service peer acl 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_2139777440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_2079763118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1820222207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_983335166}
:::

::: {#140876308 .myid}
[]{#_Toc404796660}[]{#struct_0_19838_x2835_x1405831355}[]{#_Toc296433159}

**NTP \-- NTP配置命令 \-- ntp-service authentication enable**

------------------------------------------------------------------------

[**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1765089707}[命令用来使能]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[**[undo ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_487400334}[命令用来关闭]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1335923867}

[**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x1656846191}

[**[undo ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_2087554616}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_469450111}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1268265166}[身份验证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1509796145}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x927601138}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1404848315}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x975547123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x68990619}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1707987317}

[[在一些对安全性要求较高的网络中，运行]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_860823299}[协议时需要启用]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证功能。通过客户端和服务器端的身份验证，保证客户端只与通过验证的设备进行时间同步，避免客户端从非法的服务器获得错误的时间同步信息。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1158654843}[身份验证功能后，还需要设置身份验证密钥，并将其设置为可信密钥，才能正确地进行身份验证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2112100757}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x891658370}[使能]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1404913851}

[\[Sysname\] ntp-service authentication enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x581542051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1143430039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x270711981}
:::

::: {#-2023666399 .myid}
[]{#_Toc404796661}[]{#struct_0_19838_x2835_2142211599}[]{#_Toc296433160}

**NTP \-- NTP配置命令 \-- ntp-service authentication-keyid**

------------------------------------------------------------------------

[**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1051153481}[命令用来设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[**[undo ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x2076644173}[命令用来取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_495042240}

[**[ntp-service authentication-keyid]{lang="EN-US"}**[ *keyid* **authentication-mode md5** { **cipher** \| **simple** } *value*]{lang="EN-US"}]{#struct_0_19838_x2835_x1440471204}

[**[undo ntp-service authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x1405372606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_824037765}

[[没有设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1130305212}[身份验证密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x875573704}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1035962629}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1852497577}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_632353869}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_600423013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1971517918}

[*[keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_x1405438142}[：密钥编号，用来标识身份验证密钥，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[authentication-mode md5]{lang="EN-US"}**]{#struct_0_19838_x2835_x913521700}[：表示采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行身份验证。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_19838_x2835_1710054883}[：表示以密文形式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_19838_x2835_903665544}[：表示以明文形式设置密钥。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x2835_1275063158}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法的密钥值，明文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，密文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1474800037}

[[在一些对安全性要求较高的网络中，运行]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_161166336}[协议时需要启用身份验证功能。通过客户端和服务器端的身份验证，保证客户端只与通过验证的设备进行时间同步，提高了时间同步的安全性。]{style="font-family:宋体"}

[[本命令用来设置用于身份验证的密钥。客户端和服务器上需要配置相同的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_x428890357}[及密钥值，否则无法实现时间同步。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405503678}[验证密钥后，还需要通过]{style="font-family:宋体"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**[命令将该密钥设置为可信密钥。如果]{style="font-family:宋体"}[NTP]{lang="EN-US"}[验证密钥被指定为可信密钥，删除密钥后，该密钥将自动变为不可信密钥，不必再执行]{style="font-family:宋体"}**[undo ntp-service reliable authentication-keyid]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2072111350}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过重复执行本命令，可以配置多个]{style="font-family:宋体"}]{#struct_0_19838_x2835_1803698500}[NTP]{lang="EN-US"}[身份验证密钥。设备上最多可以配置]{style="font-family:宋体"}[128]{lang="EN-US"}[个]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的密钥，均以密文的形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x192296832}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1314320714}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1116903499}[设置]{style="font-family:宋体"}[MD5]{lang="EN-US"}[身份验证密钥，密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，密钥为]{style="font-family:宋体"}[BetterKey]{lang="EN-US"}[，以明文形式输入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1775393226}

[\[Sysname\] ntp-service authentication enable]{lang="EN-US"}

[\[Sysname\] ntp-service authentication-keyid 10 authentication-mode md5 simple BetterKey]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_153501057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x1405569214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x2034803096}
:::

::: {#1512299486 .myid}
[]{#_Toc404796662}[]{#struct_0_19838_x2835_x742673059}[]{#_Toc296433161}

**NTP \-- NTP配置命令 \-- ntp-service broadcast-client**

------------------------------------------------------------------------

[**[ntp-service broadcast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_67935481}[命令用来配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播客户端模式，并使用当前接口接收]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文。]{style="font-family:宋体"}

[**[undo ntp-service broadcast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_1247585070}[命令用来取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播客户端模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_720495965}

[**[ntp-service broadcast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x989780803}

[**[undo ntp-service broadcast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_1731478797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1759987337}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405634750}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1688001192}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x540283899}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1592681463}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x2102245039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1980929595}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1950238231}

[[配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_459721256}[广播客户端模式后，设备将在接口上监听]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播服务器发送的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文，根据接收到的报文实现时间同步。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在广播客户端模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405700286}[广播客户端配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1643673472}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1855311603}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_433565849}[配置设备工作在广播客户端模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上接收]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1727486545}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service broadcast-client]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x442026553}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1248482499}[配置设备工作在广播客户端模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上接收]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1795728861}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service broadcast-client]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405765822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service broadcast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x1759534384}
:::

::: {#1837730916 .myid}
[]{#_Toc404796663}[]{#struct_0_19838_x2835_677684382}[]{#_Toc296433162}[]{#_Toc282091753}

**NTP \-- NTP配置命令 \-- ntp-service broadcast-server**

------------------------------------------------------------------------

[**[ntp-service broadcast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1264618786}[命令用来配置设备工作在]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[广播服务器模式，并使用当前接口发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文。]{style="font-family:宋体"}

[**[undo ntp-service broadcast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1363259066}[命令用来取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播服务器模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1681925075}

[**[ntp-service broadcast-server]{lang="EN-US"}**[ \[ **authentication-keyid** *keyid* \| **version** *number* \]]{lang="EN-US"}]{#struct_0_19838_x2835_x1166885546}[]{#_Hlt23405413}[ \*]{lang="EN-US"}

[**[undo ntp-service broadcast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x2134794172}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1695551744}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1405831358}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_649344460}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1797452528}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1582011063}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1460054184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_2046389272}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1151709150}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x75949241}[：指定向广播客户端发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备无法同步使能了身份验证功能的广播客户端。]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_19838_x2835_x1404848318}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_140198124}

[[配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1251109022}[广播服务器模式后，设备将通过该接口周期性地向广播地址]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在广播服务器模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_283773591}[广播服务器配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_991150451}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1053619479}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x364817147}[配置设备工作在广播服务器模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥进行加密，设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1250209279}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service broadcast-server authentication-keyid 4 version 4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1404913854}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x984826578}[配置设备工作在广播服务器模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[广播报文，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥进行加密，设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1488965983}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service broadcast-server authentication-keyid 4 version 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1203491113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service broadcast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x1499077139}
:::

::: {#-1330105517 .myid}
[]{#_Toc296433163}[]{#_Toc404796664}[]{#struct_0_19838_x2835_17552561}[]{#_Toc337719109}[]{#_Toc322619810}

**NTP \-- NTP配置命令 \-- ntp-service dscp**

------------------------------------------------------------------------

[**[ntp-server dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_x440772172}[命令用来配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ntp-server dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_x217569222}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405372605}

[**[ntp-service dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_19838_x2835_x1904845590}

[**[undo ntp-service dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_760197733}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1757702426}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x784385161}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_726895529}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_233800239}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_346091977}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1885411821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1405438141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_652562241}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_19838_x2835_1925185129}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1141058066}

[[DSCP]{lang="EN-US"}]{#struct_0_19838_x2835_x1410227970}[携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1043879140}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x835789596}[配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1638001924}

[\[Sysname\] ntp-service dscp 30]{lang="EN-US"}
:::

::: {#1518268708 .myid}
[]{#_Toc404796665}[]{#struct_0_19838_x2835_x1405503677}

**NTP \-- NTP配置命令 \-- ntp-service enable**

------------------------------------------------------------------------

[**[ntp-service enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x956366103}[命令用来开启]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[undo ntp-service enable]{lang="EN-US"}**]{#struct_0_19838_x2835_128988806}[命令用来关闭]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x620179048}

[**[ntp-service]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_19838_x2835_1839536707}

[**[undo]{lang="EN-US"}**[ **ntp-service** **enable**]{lang="EN-US"}]{#struct_0_19838_x2835_x724489406}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1358226742}

[[没有开启]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_53825984}[服务。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_741917278}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1405569213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_337849899}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_154634280}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_806312642}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x389994216}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x2062280772}[开启]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_867658023}

[\[Sysname\] ntp-service enable]{lang="EN-US"}
:::

::: {#-1229184800 .myid}
[]{#_Toc404796666}[]{#struct_0_19838_x2835_648564301}

**NTP \-- NTP配置命令 \-- ntp-service inbound enable**

------------------------------------------------------------------------

[**[ntp-service inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x1405634749}[命令用来配置接口处理收到的]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:
宋体"}

[**[undo ntp-service inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x234378645}[命令配置接口不处理收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1601537806}

[**[ntp-service inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x2119597801}

[**[undo ntp-service inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x606629475}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x611513575}

[[接口处理收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1587972943}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1734432216}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_1143930317}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405700285}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_2046957999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x268112132}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x929429002}

[[如果不允许设备为某个接口对应网段内的对端设备提供时间同步，或不允许设备从某个接口对应网段内的对端设备获得时间同步，则可以在该接口上执行]{style="font-family:宋体"}**[undo ntp-service inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_437918411}[命令，使该接口不处理收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1710944782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x665725327}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1694013333}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[不处理收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1405765821}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo ntp-service inbound enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_969348971}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1125557154}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[不处理收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_522434605}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] undo ntp-service inbound enable]{lang="EN-US"}
:::

::: {#-1588746737 .myid}
[]{#_Toc404796667}[]{#struct_0_19838_x2835_x1609549362}[]{#_Toc296433164}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 acl**

------------------------------------------------------------------------

[**[ntp-service ipv6 acl]{lang="EN-US"}**]{#struct_0_19838_x2835_928252367}[命令用来设置对端设备对本地设备]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务的访问控制权限。]{style="font-family:宋体"}

[**[undo ntp-service ipv6 acl]{lang="EN-US"}**]{#struct_0_19838_x2835_x976215977}[命令用来取消设置的访问控制权限。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1405831357}

[**[ntp-service ipv6]{lang="EN-US"}**[ { **peer** \| **query** \| **server** \| **synchronization** } **acl** *acl-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x1367078175}

[**[undo ntp-service ipv6]{lang="EN-US"}**[ { **peer** \| **query** \| **server** \| **synchronization** } **acl** *acl-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x1399399519}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_210238320}

[[对端设备对本地设备]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1440522795}[服务的访问控制权限为]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1371383290}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_1794581490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1263395701}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1699439882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1404848317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_187252291}

[**[peer]{lang="EN-US"}**]{#struct_0_19838_x2835_x1649271397}[：完全访问权限。该权限既允许对端设备向本地设备的时间同步，对本地设备进行控制查询（查询]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的一些状态，比如告警信息、验证状态、时间服务器信息等），同时本地设备也可以向对端设备的时间同步。]{style="font-family:宋体"}

[**[query]{lang="EN-US"}**]{#struct_0_19838_x2835_2130703399}[：仅具有控制查询的权限。该权限只允许对端设备对本地设备的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务进行控制查询，但是不能向本地设备的时间同步。]{style="font-family:宋体"}

[**[server]{lang="EN-US"}**]{#struct_0_19838_x2835_656178445}[：服务器访问与查询权限。该权限允许对端设备向本地设备的时间同步，对本地设备进行控制查询，但本地设备不会向对端设备的时间同步。]{style="font-family:宋体"}

[**[synchronization]{lang="EN-US"}**]{#struct_0_19838_x2835_436799400}[：仅具有访问服务器的权限。该权限只允许对端设备向本地设备的时间同步，但不能进行控制查询。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_19838_x2835_2145390572}[：指定应用的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[Access Control List]{lang="EN-US"}[，访问控制列表）。通过]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[过滤的对端设备具有本命令中指定的访问控制权限。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1597819217}

[[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1404913853}[服务的访问控制权限从高到低依次为]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[、]{style="font-family:宋体"}**[server]{lang="EN-US"}**[、]{style="font-family:宋体"}**[synchronization]{lang="EN-US"}**[、]{style="font-family:宋体"}**[query]{lang="EN-US"}**[。当设备接收到一个]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务请求时，会按照权限从高到低的顺序依次进行匹配，第一个匹配的权限为此设备具有的访问控制权限。如果没有匹配的权限，则不允许对端设备与本地设备进行时间同步、对本端进行控制查询，也不允许本端设备与对端设备进行时间同步。]{style="font-family:宋体"}

[**[ntp-service ipv6 acl]{lang="EN-US"}**]{#struct_0_19838_x2835_x1744341465}[命令提供了一种最小限度的安全措施，更安全的方法是进行身份验证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1947798425}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1579839579}[配置]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[网段的对端设备对本地设备具有完全访问权限。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x293332334}

[\[Sysname\] acl ipv6 basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2001\] rule permit source 2001::1 64]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] ntp-service ipv6 peer acl 2001]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_340016273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x800902634}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_160711339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x542200026}
:::

::: {#-668114416 .myid}
[]{#_Toc296433165}[]{#_Toc404796668}[]{#struct_0_19838_x2835_x1337978711}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 dscp**

------------------------------------------------------------------------

[**[ntp-server ipv6 dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_914378810}[命令用来配置]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ntp-server ipv6 dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_2024015445}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_873515410}

[**[ntp-service ipv6 dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_19838_x2835_774528086}

[**[undo ntp-service ipv6 dscp]{lang="EN-US"}**]{#struct_0_19838_x2835_x1943721453}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1702399148}

[[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160645803}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[56]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_193579072}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_908072124}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_52890040}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1818048925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1717196289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x369302881}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_19838_x2835_x1162278367}[：]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_285768220}

[[DSCP]{lang="EN-US"}]{#struct_0_19838_x2835_160580267}[携带在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[Traffic class]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_326973874}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1871357593}[配置]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1154909142}

[\[Sysname\] ntp-service ipv6 dscp 30]{lang="EN-US"}
:::

::: {#-1316677017 .myid}
[]{#_Toc404796669}[]{#struct_0_19838_x2835_x1251134830}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 inbound enable**

------------------------------------------------------------------------

[**[ntp-]{lang="EN-US"}[service ipv6 inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x193306614}[命令用来配置接口处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ ntp-service ipv6 inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1405161211}[命令用来配置接口不处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x690841497}

[**[ntp-service ipv6 inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_160514731}

[**[undo ntp-service ipv6 inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x2008186470}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x641736981}

[[接口处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_481580502}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2121577335}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_2086243934}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_883619347}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_996189027}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_77886049}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160449195}

[[如果不允许设备为某个接口对应网段内的对端设备提供时间同步，或不允许设备从某个接口对应网段内的对端设备获得时间同步，则可以在该接口上执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}[ ntp-service ipv6 inbound enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x1213163523}[命令，使该接口不处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1865748882}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1469665653}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1404985064}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[不处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_440297932}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo ntp-service ipv6 inbound enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_951330579}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1047690969}[配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[不处理收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_160383659}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] undo ntp-service ipv6 inbound enable]{lang="EN-US"}
:::

::: {#-319958958 .myid}
[]{#_Toc404796670}[]{#struct_0_19838_x2835_x329708512}[]{#_Toc296433166}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 multicast-client**

------------------------------------------------------------------------

[**[ntp-service ipv6 multicast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x1741838764}[命令用来配置设备工作在]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播客户端模式，并使用当前接口接收]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[**[undo ntp-service ipv6 multicast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x549638377}[命令用来取消]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播客户端模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1022511510}

[**[ntp-service ipv6 multicast-client]{lang="EN-US"}**[ *ipv6-multicast-address*]{lang="EN-US"}]{#struct_0_19838_x2835_x1869427545}

[**[undo ntp-service ipv6 multicast-client]{lang="EN-US"}**[ *ipv6-multicast-address*]{lang="EN-US"}]{#struct_0_19838_x2835_1197548657}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1116884177}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160318123}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1890740122}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_550867480}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x71637481}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1701815494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x410686991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1873495012}

[*[ipv6-multicast-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x803124830}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址。]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播客户端和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播服务器上配置的组播地址必须相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1793704778}

[[配置设备工作在]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160252587}[组播客户端模式后，设备将在接口上监听目的地址为指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文，根据接收到的报文实现时间同步。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_x1474532790}[组播客户端模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播客户端配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_686444388}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1995412380}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1800892155}[配置设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播客户端模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上接收目的地址为组播地址]{style="font-family:宋体"}[FF21::1]{lang="EN-US"}[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_1149319599}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service ipv6 multicast-client ff21::1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_840392037}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1787379359}[配置设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播客户端模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上接收目的地址为组播地址]{style="font-family:宋体"}[FF21::1]{lang="EN-US"}[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_161235627}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service ipv6 multicast-client ff21::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2144080258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service ipv6 multicast-]{lang="EN-US"}**]{#struct_0_19838_x2835_x1224588752}**[server]{lang="EN-US"}**
:::

::: {#-853279708 .myid}
[]{#_Toc404796671}[]{#struct_0_19838_x2835_x2097282064}[]{#_Toc296433167}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 multicast-server**

------------------------------------------------------------------------

[**[ntp-service ipv6 multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x632484830}[命令用来配置设备工作在]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播服务器模式，并使用当前接口发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[**[undo ntp-service ipv6 multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_732172329}[命令用来取消]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播服务器模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x424708257}

[**[ntp-service ipv6 multicast-server]{lang="EN-US"}**[ *ipv6-multicast-address* \[ **authentication-keyid** *keyid* \| **ttl** *ttl-number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_x604264880}

[**[undo ntp-service ipv6 multicast-server]{lang="EN-US"}**[ *ipv6-multicast-address*]{lang="EN-US"}]{#struct_0_19838_x2835_161170091}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1538131138}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_990617697}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1782633716}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1802495956}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1621426769}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x56014301}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_2009497232}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160711340}

[*[ipv6-multicast-address]{lang="EN-US"}*]{#struct_0_19838_x2835_1414115119}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址。]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播客户端和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播服务器上配置的组播地址必须相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x1353489704}[：指定向组播客户端发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备无法同步使能了身份验证功能的组播客户端。]{style="font-family:宋体"}

[**[ttl]{lang="EN-US"}***[ ttl-number]{lang="EN-US"}*]{#struct_0_19838_x2835_375715465}[：指定组播报文的生存期。]{style="font-family:宋体"}*[ttl-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1951615486}

[[配置设备工作在]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x258220592}[组播服务器模式后，设备将通过该接口周期性地向指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_x1264258594}[组播服务器模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[组播服务器配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_89284170}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1746055245}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_160645804}[配置设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播服务器模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址]{style="font-family:宋体"}[FF21::1]{lang="EN-US"}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥加密]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_193579065}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service ipv6 multicast-server ff21::1 authentication-keyid 4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1048243009}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_896050576}[配置设备工作在]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播服务器模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址]{style="font-family:宋体"}[FF21::1]{lang="EN-US"}[发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥加密]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_847557653}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service ipv6 multicast-server ff21::1 authentication-keyid 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1431565842}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service ipv6 multicast-]{lang="EN-US"}**]{#struct_0_19838_x2835_2076877404}**[client]{lang="EN-US"}**
:::

::: {#1825078258 .myid}
[]{#_Toc404796672}[]{#struct_0_19838_x2835_160580268}[]{#_Toc296433168}[]{#_Toc322619817}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 source**

------------------------------------------------------------------------

[**[ntp-service ipv6 source]{lang="EN-US"}**]{#struct_0_19838_x2835_326973875}[命令用来指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口。]{style="font-family:宋体"}

[**[undo ntp-service ipv6 source]{lang="EN-US"}**]{#struct_0_19838_x2835_1871357594}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1154843606}

[**[ntp-service ipv6 source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x822991631}

[**[undo ntp-service]{lang="EN-US"}**[ **ipv6 source**]{lang="EN-US"}]{#struct_0_19838_x2835_x1989249449}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1261685814}

[[没有指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1538024816}[报文的源接口，设备自动选择报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，具体选择原则请参见]{style="font-family:宋体"}[RFC 3484]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1830973650}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_160514732}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2008186467}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x238517990}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1709147308}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1365737061}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_19838_x2835_x1658073674}[：接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x902701701}

[[如果指定了]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_398288416}[报文的源接口，则设备在主动发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文时，将采用源接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址作为发送报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，从而保证]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[应答报文的目的地址均为此地址。]{style="font-family:宋体"}

[[设备对接收到的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1343012882}[请求报文进行应答时，应答报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址始终为接收到]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[请求报文的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[如果不想让本地设备上其他接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_160449196}[地址成为应答报文的目的地址，可以使用本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在命令]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x1213163522}[或]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 unicast-peer]{lang="EN-US"}**[中指定了]{lang="EN-US" style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口，则以]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 unicast-server]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 unicast-peer]{lang="EN-US"}**[命令指定源接口的为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口视图下配置了]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_299664941}[命令，则]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[组播报文的源接口为配置了]{lang="EN-US" style="font-family:宋体"}**[ntp-service ipv6 multicast-server]{lang="EN-US"}**[命令的接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_19838_x2835_2075800316}[NTP]{lang="EN-US"}[源接口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，则设备不再发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x725080193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1827602540}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x685499184}[配置]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1378347852}

[\[Sysname\] ntp-service ipv6 source gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_160383660}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1626606615}[配置]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x468759960}

[\[Sysname\] ntp-service ipv6 source vlan-interface 1]{lang="EN-US"}
:::

::: {#-790691245 .myid}
[]{#_Toc404796673}[]{#struct_0_19838_x2835_1675817256}[]{#_Toc296433169}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 unicast-peer**

------------------------------------------------------------------------

[**[ntp-service]{lang="EN-US"}**[ **ipv6 unicast-peer**]{lang="EN-US"}]{#struct_0_19838_x2835_1942321930}[命令用来为设备指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[被动对等体。]{style="font-family:宋体"}

[**[undo ntp-service]{lang="EN-US"}**[ **ipv6 unicast-peer**]{lang="EN-US"}]{#struct_0_19838_x2835_x1309099881}[命令用来取消为设备指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[被动对等体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x957177773}

[**[ntp-service ipv6 unicast-peer ]{lang="EN-US"}**[{ *peer-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid* \| **priority** \| **source** *interface-type interface-number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_953467332}

[**[undo ntp-service ipv6 unicast-peer ]{lang="EN-US"}**[{ *peer-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x2835_160318124}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1890740119}

[[没有为设备指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_1310447903}[被动对等体。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x341935812}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1815235613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x51950540}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1277571150}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_577224646}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2041716768}

[*[peer-name]{lang="EN-US"}*]{#struct_0_19838_x2835_160252588}[：被动对等体的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x1474532779}[：被动对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。该地址只能是一个单播地址，不能为组播地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x2835_1895642609}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}***[ keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_809856821}[：指定向对等体发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与对等体之间不会进行身份验证。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**]{#struct_0_19838_x2835_x335491816}[：在同等条件下，优先选择]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[或]{style="font-family:宋体"}*[peer-name]{lang="EN-US"}*[指定的对等体为同步对等体。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_19838_x2835_1458007543}[：指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口。如果指定的被动对等体地址不是链路本地地址，则本地设备给对端发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文时，报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为指定源接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。如果指定的被动对等体地址是链路本地地址，则]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文从指定的源接口发送，并且报文的源地址为该接口的链路本地地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则设备自动选择报文的源]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址，具体选择原则请参见]{style="font-family:宋体"}[RFC 3484]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_961279192}

[[为设备指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_19838_x2835_x1339773362}[被动对等体后，主动对等体和被动对等体的时间可以互相同步。如果双方的时钟都处于同步状态，则层数大的时钟与层数小的时钟的时间同步。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_x145707443}[向某个]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo ntp-service ipv6 unicast-peer]{lang="EN-US"}**]{#struct_0_19838_x2835_161235628}[命令时，如果指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{lang="EN-US" style="font-family:
宋体"}[VPN]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置；如果没有指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被动对等体的]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2144080267}[IPv6]{lang="EN-US"}[地址为链路本地地址时，必须指定报文的源接口，并且不能指定被动对等体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1627676671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_1115032238}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1085283312}[配置设备工作在主动对等体模式，被动对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1374289128}

[\[Sysname\] ntp-service ipv6 unicast-peer 2001::1 source gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_818989390}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_423632232}[配置设备工作在主动对等体模式，被动对等体的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_161170092}

[\[Sysname\] ntp-service ipv6 unicast-peer 2001::1 source vlan-interface 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1538131137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_989634657}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_282222605}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1228522012}
:::

::: {#1006572148 .myid}
[]{#_Toc404796674}[]{#struct_0_19838_x2835_x263346439}[]{#_Toc296433170}[]{#_Toc286234192}

**NTP \-- NTP配置命令 \-- ntp-service ipv6 unicast-server**

------------------------------------------------------------------------

[**[ntp-service]{lang="EN-US"}[ ipv6 unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x533472120}[命令用来为设备指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ ntp-service ipv6 unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x136524854}[命令用来取消为设备指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160711337}

[**[ntp-service ipv6 unicast-server]{lang="EN-US"}**[ { *server-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid* \| **priority** \| **source** *interface-type interface-number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_x542200012}

[**[undo ntp-service ipv6 unicast-server ]{lang="EN-US"}**[{ *server-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x2835_x1337716564}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x290913699}

[[没有为设备指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1871198014}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_590635082}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x993455349}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1520796666}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_640436802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_160645801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_193579070}

[*[server-name]{lang="EN-US"}*]{#struct_0_19838_x2835_908072122}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_19838_x2835_52890038}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。该地址只能是一个单播地址，不能为组播地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x2835_x1707085162}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}***[ keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_213613778}[：指定向]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器发送报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器之间不会进行身份验证。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**]{#struct_0_19838_x2835_662743664}[：指定在同等条件下，优先选择该服务器。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_19838_x2835_x1975112644}[：指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口。如果指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器地址不是链路本地地址，则本地设备给服务器发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文时，报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为指定源接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。如果指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器地址是链路本地地址，则]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文从指定的源接口发送，并且报文的源地址为该接口的链路本地地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则设备自动选择报文的源]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址，具体选择原则请参见]{style="font-family:宋体"}[RFC 3484]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1163958573}

[[为设备指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160580265}[服务器后，设备可以与该服务器的时间同步，但是服务器不会与设备的时间同步。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_326973872}[向某个]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo ntp-service ipv6 unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1871357587}[命令时，如果指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{lang="EN-US" style="font-family:
宋体"}[VPN]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置；如果没有指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1154646999}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址时，必须指定报文的源接口，并且不能指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1432870327}

[[ # ]{lang="EN-US"}]{#struct_0_19838_x2835_x675986024}[配置设备的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x27541881}

[\[Sysname\] ntp-service ipv6 unicast-server 2001::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x798204506}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_160514729}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_330465682}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x725613342}
:::

::: {#1632918122 .myid}
[]{#_Toc404796675}[]{#struct_0_19838_x2835_1782669166}[]{#_Toc296433171}[]{#_Toc286234194}

**NTP \-- NTP配置命令 \-- ntp-service max-dynamic-sessions**

------------------------------------------------------------------------

[**[ntp-service max-dynamic-sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_2035238636}[命令用来配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[动态会话的最大数目。]{style="font-family:宋体"}

[**[undo ntp-service max-dynamic-sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_x1002197713}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x867461150}

[**[ntp-service max-dynamic-sessions]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_19838_x2835_1069716962}

[**[undo ntp-service max-dynamic-sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_x824766701}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160449193}

[[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1213163517}[动态会话的最大数目为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x460046554}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x901587971}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_565268247}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1914492001}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x2117451096}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1615045028}

[*[number]{lang="EN-US"}*]{#struct_0_19838_x2835_1254712055}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[动态会话的最大数目，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160383657}

[[同一设备同一时间内存在的会话数目最多为]{style="font-family:宋体"}[128]{lang="EN-US"}]{#struct_0_19838_x2835_x329708514}[个，其中包括静态会话数和动态会话数。静态会话是用户手动配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[相关命令而建立的会话；动态会话是]{style="font-family:宋体"}[NTP]{lang="EN-US"}[运行过程中建立的临时会话。]{style="font-family:宋体"}

[[本配置用来限制动态会话的数目，以避免设备上维护过多的动态会话，占用过多的系统资源。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1741707692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1235764227}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x619298975}[设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[动态会话的最大数目为]{style="font-family:宋体"}[50]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_2045212365}

[\[Sysname\] ntp-service max-dynamic-sessions 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1383091671}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ntp-service sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_1502669842}
:::

::: {#616059293 .myid}
[]{#_Toc404796676}[]{#struct_0_19838_x2835_160318121}[]{#_Toc296433172}

**NTP \-- NTP配置命令 \-- ntp-service multicast-client**

------------------------------------------------------------------------

[**[ntp-service multicast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x1890740124}[命令用来配置设备工作在]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[组播客户端模式，并使用当前接口接收]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[**[undo ntp-service multicast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_1713666894}[命令用来取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播客户端模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_786230817}

[**[ntp-service multicast-client]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_19838_x2835_1356371216}

[**[undo ntp-service multicast-client]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_19838_x2835_x1703497574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_331121741}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1146064645}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_135593583}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_160252585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1474532792}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1849243802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_364564349}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_2117519091}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x242996997}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的组播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，缺省值为]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[。组播客户端和组播服务器上配置的组播地址必须相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_611669530}

[[配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x647805877}[组播客户端模式后，设备将在接口上监听目的地址为指定组播地址的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，根据接收到的报文实现时间同步。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在组播客户端模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1981461503}[组播客户端配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_161235625}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x2144080256}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x61789338}[配置设备工作在组播客户端模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上接收目的地址为]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x418351785}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service multicast-client 224.0.1.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_343629225}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1774062200}[配置设备工作在组播客户端模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上接收目的地址为]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_492057071}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service multicast-client 224.0.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_161170089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x418183990}
:::

::: {#1671228245 .myid}
[]{#_Toc404796677}[]{#struct_0_19838_x2835_1827173442}[]{#_Toc296433173}

**NTP \-- NTP配置命令 \-- ntp-service multicast-server**

------------------------------------------------------------------------

[**[ntp-service multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_82416022}[命令用来配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播服务器模式，并使用当前接口发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播报文。]{style="font-family:宋体"}

[**[undo ntp-service multicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x1513337942}[命令用来取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}[组播服务器模式的配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_859367899}

[**[ntp-service multicast-server ]{lang="EN-US"}**[\[ *ip-address* \] \[ **authentication-keyid** *keyid* \| **ttl** *ttl-number* \| **version** *number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_x347288270}[]{#_Hlt23405132}

[**[undo ntp-service multicast-server]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_19838_x2835_81311101}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1487337946}

[[设备没有工作在任何]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160711338}[模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x542200025}

[[接口视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1337782103}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1973154351}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_201616511}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x813869549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1652358310}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x1743259150}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的组播]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，缺省值为]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[。组播客户端和组播服务器上配置的组播地址必须相同。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_160645802}[：指定向组播客户端发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，使用指定的密钥[计算报文的摘要。]{#_Hlt15876277}]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，则本端设备无法同步使能了身份验证功能的组播客户端。]{style="font-family:宋体"}

[**[ttl ]{lang="EN-US"}***[ttl-number]{lang="EN-US"}*]{#struct_0_19838_x2835_193579071}[：指定组播报文的生存期。]{style="font-family:宋体"}*[ttl-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_19838_x2835_908072123}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_52890039}

[[配置设备工作在]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_249229974}[组播服务器模式后，设备将通过该接口周期性地向指定的组播地址发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[如果在接口上配置了设备工作在组播服务器模式，则建议不要将该接口加入聚合组。如果要将接口加入聚合组，则建议先取消]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x2147011981}[组播服务器配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_388452740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x894972634}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x736477869}[配置设备工作在组播服务器模式，在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口上发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的目的地址为组播地址]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥加密]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，并设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_160580266}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ntp-service multicast-server []{#_Hlt15876317}224.0.1.1 version 4 authentication-keyid 4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_326973873}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1871357588}[配置设备工作在组播服务器模式，在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的目的地址为组播地址]{style="font-family:宋体"}[224.0.1.1]{lang="EN-US"}[，用]{style="font-family:宋体"}[4]{lang="EN-US"}[号密钥加密]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文，并设置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1154581463}

[\[Sysname\] interface vlan-interface 1]{lang="EN-US"}

[\[Sysname-Vlan-interface1\] ntp-service multicast-server 224.0.1.1 version 4 authentication-keyid 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1877213740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service multicast-client]{lang="EN-US"}**]{#struct_0_19838_x2835_x1024756941}
:::

::::: {#1786188565 .myid}
[]{#_Toc404796678}[]{#struct_0_19838_x2835_700604892}[]{#_Toc296433174}

**NTP \-- NTP配置命令 \-- ntp-service refclock-master**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](NTP命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_19838_x2835_160514730}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_19838_x2835_x2008186469}
:::

[ ]{lang="EN-US"}

[**[ntp-service refclock-master]{lang="EN-US"}**]{#struct_0_19838_x2835_568051064}[命令用来设置本地时钟作为参考时钟。]{style="font-family:
宋体"}

[**[undo ntp-service refclock-master]{lang="EN-US"}**]{#struct_0_19838_x2835_432563926}[命令用来取消本地时钟作为参考时钟。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x697878252}

[**[ntp-service refclock-master]{lang="EN-US"}**[ \[ *ip-address* \] \[ *stratum* \]]{lang="EN-US"}]{#struct_0_19838_x2835_x550600243}

[**[undo ntp-service refclock-master]{lang="EN-US"}**[ \[ *ip-address* \]]{lang="EN-US"}]{#struct_0_19838_x2835_x683806002}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x499700061}

[[设备未采用本地时钟作为参考时钟。]{style="font-family:宋体"}]{#struct_0_19838_x2835_917644870}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160449194}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1213163524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1106233995}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1873301624}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x633356529}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1630865127}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_1556085465}[：本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[127.127.1.u]{lang="EN-US"}[。]{style="font-family:宋体"}[u]{lang="EN-US"}[的取值范围为]{style="font-family:
宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[，表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[的进程号。如果不指定]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[，则系统默认值是]{style="font-family:宋体"}[127.127.1.0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[stratum]{lang="EN-US"}*]{#struct_0_19838_x2835_483319311}[：本地时钟所处的层数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。时钟的层数定义了时钟的准确度，层数取值越小，时钟的准确度越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1858702255}

[[实际网络中，通常将从权威时钟（如原子时钟）获得时间同步的]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_160383658}[服务器的层数设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并将其作为主时间服务器同步网络中其他设备的时钟。网络中的设备与主时间服务器的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[距离，即]{style="font-family:宋体"}[NTP]{lang="EN-US"}[同步链上]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的数目，决定了设备上时钟的层数。]{style="font-family:宋体"}

[[在某些网络中，例如无法与外界通信的孤立网络，网络中的设备无法与权威时钟进行时间同步。此时，可以从该网络中选择一台时钟较为准确的设备，指定该设备与本地时钟进行时间同步，即采用本地时钟作为参考时钟，使得该设备的时钟处于同步状态。该设备作为时间服务器为网络中的其他设备提供时间同步，从而实现整个网络的时间同步。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x329708513}

[[请谨慎使用本配置，以免导致网络中设备的时间错误。在执行本命令之前，建议先调整本地系统时间。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1741773228}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x788253974}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x396832857}[设置本地设备时钟作为参考时钟，层数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_1060519278}

[\[Sysname\] ntp-service refclock-master 2]{lang="EN-US"}
:::::

::: {#648159924 .myid}
[]{#_Toc404796679}[]{#struct_0_19838_x2835_595337959}[]{#_Toc296433175}

**NTP \-- NTP配置命令 \-- ntp-service reliable authentication-keyid**

------------------------------------------------------------------------

[**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1876313190}[命令用来指定已创建的密钥是可信的。]{style="font-family:宋体"}

[**[undo ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_160318122}[命令用来取消可信密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1890740121}

[**[ntp-service reliable authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_954152007}

[**[undo ntp-service reliable authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x820158121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1934645845}

[[没有配置可信密钥。]{style="font-family:宋体"}]{#struct_0_19838_x2835_1078262129}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_506928765}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1982434494}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160252586}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1474532789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1896363505}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x483001601}

[*[keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_1591261345}[：密钥编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1070930857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使能身份验证功能后，客户端只会与提供可信密钥的服务器进行时间同步；如果服务器提供的密钥不是可信的，那么客户端不会与其同步。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2028350666}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置本命令前，请确保认证开关已经打开并且配置了密钥，即保证该密钥的存在性后才能设定它是否可信。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1053108494}[如果]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[验证密钥被指定为可信密钥，删除密钥后，该密钥将自动变为不可信密钥，不必再执行]{lang="EN-US" style="font-family:宋体"}**[undo ntp-service reliable authentication-keyid]{lang="EN-US"}**[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令可以多次配置，最多可以配置]{style="font-family:宋体"}]{#struct_0_19838_x2835_1682522213}[128]{lang="EN-US"}[个可信密钥。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_161235626}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x2144080257}[使能]{style="font-family:宋体"}[NTP]{lang="EN-US"}[身份验证功能，配置编号为]{style="font-family:宋体"}[37]{lang="EN-US"}[的密钥采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行身份验证，密钥值为]{style="font-family:宋体"}[BetterKey]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1627873279}

[\[Sysname\] ntp-service authentication enable]{lang="EN-US"}

[\[Sysname\] ntp-service authentication-keyid 37 authentication-mode md5 BetterKey]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_788574090}[指定该密钥为可信密钥。]{style="font-family:宋体"}

[[\[Sysname\] ntp-service reliable authentication-keyid 37]{lang="EN-US"}]{#struct_0_19838_x2835_x49717977}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1952838614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1991674028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1882641707}
:::

::: {#1495469721 .myid}
[]{#_Toc404796680}[]{#struct_0_19838_x2835_161170090}[]{#_Toc296433176}

**NTP \-- NTP配置命令 \-- ntp-service source**

------------------------------------------------------------------------

[**[ntp-service source]{lang="EN-US"}**]{#struct_0_19838_x2835_1538131139}[命令用来指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口。]{style="font-family:宋体"}

[**[undo ntp-service source]{lang="EN-US"}**]{#struct_0_19838_x2835_990552161}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_648197643}

[**[ntp-service source]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_19838_x2835_x1386200121}

[**[undo ntp-service source]{lang="EN-US"}**]{#struct_0_19838_x2835_708913856}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_729331955}

[[没有指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x438295208}[报文的源接口，设备根据路由表查找报文的出接口，并采用出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_431463146}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_160711335}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x542200014}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1337847636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1426871069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_606983309}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_19838_x2835_384406809}[：接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_267313203}

[[如果指定了]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1701253465}[报文的源接口，则设备在主动发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，将报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址设置为指定接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，从而保证]{style="font-family:宋体"}[NTP]{lang="EN-US"}[应答报文的目的地址均为此地址。]{style="font-family:宋体"}

[[设备对接收到的]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_388738962}[请求报文进行应答时，应答报文的源地址始终为接收到]{style="font-family:宋体"}[NTP]{lang="EN-US"}[请求报文的目的地址。]{style="font-family:宋体"}

[[如果不想让本地设备上其他接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_19838_x2835_160645799}[地址成为应答报文的目的地址，可以使用本命令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在命令]{lang="EN-US" style="font-family:宋体"}**[ntp-service unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_243368255}[或]{lang="EN-US" style="font-family:宋体"}**[ntp-service unicast-peer]{lang="EN-US"}**[中指定了]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口，则以]{lang="EN-US" style="font-family:宋体"}**[ntp-service unicast-server]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[ntp-service unicast-peer]{lang="EN-US"}**[命令指定源接口的为准。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在接口视图下配置了]{lang="EN-US" style="font-family:宋体"}**[ntp-service broadcast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_810873367}[或]{lang="EN-US" style="font-family:宋体"}**[ntp-service multicast-server]{lang="EN-US"}**[命令，则]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[广播或组播模式报文的源接口为配置了上述命令的接口。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_19838_x2835_1064290510}[NTP]{lang="EN-US"}[源接口处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态，则设备不再发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2067835891}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1563771517}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1614695647}[配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x684440317}

[\[Sysname\] ntp-service source gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_160580263}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_326973870}[配置]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_19838_x2835_1871357589}

[\[Sysname\] ntp-service source vlan-interface 1]{lang="EN-US"}
:::

::: {#1584960076 .myid}
[]{#_Toc404796681}[]{#struct_0_19838_x2835_x1154515927}[]{#_Toc296433177}[]{#_Toc322619827}[]{#_Toc322619828}[]{#_Toc322619829}[]{#_Toc322619830}[]{#_Toc322619831}

**NTP \-- NTP配置命令 \-- ntp-service unicast-peer**

------------------------------------------------------------------------

[**[ntp-service unicast-peer]{lang="EN-US"}**]{#struct_0_19838_x2835_544994190}[命令用来为设备指定被动对等体。]{style="font-family:
宋体"}

[**[undo ntp-service unicast-peer]{lang="EN-US"}**]{#struct_0_19838_x2835_x1580030362}[命令用来取消为设备指定的被动对等体。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x640554672}

[**[ntp-service]{lang="EN-US"}**[ **unicast-peer** { *peer-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid* \| **priority** \| **source** *interface-type interface-number* \| **version** *number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_x709476665}

[**[undo]{lang="EN-US"}**[ **ntp-service** **unicast-peer** { *peer-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x2835_160514727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_330465696}

[[没有为设备指定被动对等体。]{style="font-family:宋体"}]{#struct_0_19838_x2835_1613038822}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_211397118}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_818315960}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1296851165}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x722738416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1616730543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1522570512}

[*[peer-name]{lang="EN-US"}*]{#struct_0_19838_x2835_160449191}[：被动对等体的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x1213163519}[：被动对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该地址只能是一个单播地址，不能为广播地址、组播地址或本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x2835_1058983220}[：指定被动对等体所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示被动对等体位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_1598932503}[：指定向对等体发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与对等体之间不会进行身份验证。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**]{#struct_0_19838_x2835_332885583}[：在同等条件下，优先选择]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[或]{style="font-family:宋体"}*[peer-name]{lang="EN-US"}*[指定的对等体为同步对等体。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x2137863134}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口。本地设备给对端发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，报文的源地址为指定源接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则根据路由表查找报文的出接口，并采用出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_19838_x2835_x1750890060}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_652813812}

[[为设备指定被动对等体后，主动对等体和被动对等体的时间可以互相同步。如果双方的时钟都处于同步状态，则层数大的时钟与层数小的时钟的时间同步。]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1522681137}

[[配置]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_1097472960}[向某个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{style="font-family:宋体"}[PE]{lang="EN-US"}[或]{style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{style="font-family:宋体"}

[[在执行]{style="font-family:宋体"}**[undo ntp-service unicast-peer]{lang="EN-US"}**]{#struct_0_19838_x2835_160383655}[命令时，如果指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置；如果没有指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[被动对等体配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x329708516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1741576620}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1550217714}[配置设备工作在主动对等体模式，被动对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_1928014207}

[\[Sysname\] ntp-service unicast-peer 10.1.1.1 version 4 source gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_19838_x2835_x1846255244}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x543007314}[配置设备工作在主动对等体模式，被动对等体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[，]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_160318119}

[\[Sysname\] ntp-service unicast-peer 10.1.1.1 version 4 source vlan-interface 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_447912028}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x2108612693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1455962896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1459471683}
:::

::: {#-1359568525 .myid}
[]{#_Toc404796682}[]{#struct_0_19838_x2835_x689265555}[]{#_Toc296433178}[]{#_Toc286234202}

**NTP \-- NTP配置命令 \-- ntp-service unicast-server**

------------------------------------------------------------------------

[**[ntp-service unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1435339595}[命令用来为设备指定]{style="font-family:
宋体"}[NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo ntp-service unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1852065140}[命令用来取消为设备指定的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1769611762}

[**[ntp-service]{lang="EN-US"}**[ **unicast-server** { *server-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid* \| **priority** \| **source** *interface-type interface-number* \| **version** *number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_710037574}

[**[undo]{lang="EN-US"}**[ **ntp-service** ]{lang="EN-US"}]{#struct_0_19838_x2835_160252583}[]{#_Hlt23405300}**[unicast-server]{lang="EN-US"}**[ { *server-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1474532786}

[[没有为设备指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x120059130}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_76225000}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x975428774}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x27042388}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_969504546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_276026379}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_161235623}

[*[server-name]{lang="EN-US"}*]{#struct_0_19838_x2835_x2144080262}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_x2030961198}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该地址只能是一个单播地址，不能为广播地址、组播地址或本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_19838_x2835_224350844}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_916708436}[：指定向]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器发送报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器之间不会进行身份验证。]{style="font-family:宋体"}

[**[priority]{lang="EN-US"}**]{#struct_0_19838_x2835_x430685242}[：指定在同等条件下，优先选择该服务器。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x974873646}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口。本地设备给服务器发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，报文的源地址为指定源接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则根据路由表查找报文的出接口，并采用出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[version ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_19838_x2835_x451577958}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x801193422}

[[为设备指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_161170087}[服务器后，设备可以与该服务器的时间同步，但是服务器不会与设备的时间同步。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_x418184004}[向某个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{style="font-family:宋体"}[PE]{lang="EN-US"}[或]{style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{style="font-family:宋体"}

[[在执行]{style="font-family:宋体"}**[undo ntp-service unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_x118774650}[命令时，如果指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置；如果没有指定]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1176918743}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1855535562}[配置设备的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x648983497}

[\[Sysname\] ntp-service unicast-server 10.1.1.1 version 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_640720158}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_378829510}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_160711336}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ntp-service reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x542200011}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#636240601 .myid}
[]{#_Toc404796685}[]{#struct_0_19838_x2835_1356001504}[]{#_Toc296433182}[]{#_Toc365967117}[]{#_Toc365967118}[]{#_Toc365967119}[]{#_Toc365967120}[]{#_Toc365967121}[]{#_Toc365967122}[]{#_Toc365967123}[]{#_Toc365967124}[]{#_Toc365967125}[]{#_Toc365967126}[]{#_Toc365967127}[]{#_Toc365967128}[]{#_Toc365967129}[]{#_Toc365967130}[]{#_Toc365967131}[]{#_Toc365967132}[]{#_Toc365967133}[]{#_Toc365967150}

**SNTP \-- SNTP配置命令 \-- display sntp ipv6 sessions**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}[ sntp ipv6 sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_1019392118}[命令用来显示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x576316397}

[**[display sntp ipv6 sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_2127478230}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_160383656}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x329708515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1741642156}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1180657788}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_x1722100471}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_489375557}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_x1415601695}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2006312525}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1226739774}[显示]{style="font-family:宋体"}[IPv6 SNTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display sntp ipv6 sessions]{lang="EN-US"}]{#struct_0_19838_x2835_160318120}

[SNTP server: 2001::1]{lang="EN-US"}

[Stratum: 16]{lang="EN-US"}

[Version: 4]{lang="EN-US"}

[Last receive time: No packet was received.]{lang="EN-US"}

[ ]{lang="EN-US"}

[SNTP server: 2001::100]{lang="EN-US"}

[Stratum: 3]{lang="EN-US"}

[Version: 4]{lang="EN-US"}

[Last receive time: Fri, Oct 21 2011 11:28:28.058 (Synced)]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display sntp ipv6 sessions]{lang="EN-US"}]{#struct_0_19838_x2835_x1890740123}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x476730005}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_2116951421}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_x627211586}

[[SNTP server]{lang="EN-US"}]{#struct_0_19838_x2835_x45517496}

[[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_160252584}[服务器，即]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器。若该字段显示为]{style="font-family:宋体"}[::]{lang="EN-US"}[，表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[Stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x1474532791}

[[时钟的层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2042438967}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_1504135186}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，表示时钟的准确度越高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_19838_x2835_161235624}

[[版本号]{style="font-family:宋体"}]{#struct_0_19838_x2835_x2144080255}

[[Last receive time]{lang="EN-US"}]{#struct_0_19838_x2835_x465073865}

[[最后一次接收到]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_2006613551}[会话消息的时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Synced]{lang="EN-US"}]{#struct_0_19838_x2835_630366997}[表示设备的本地时钟从该服务器获得同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No packet was received.]{lang="EN-US"}]{#struct_0_19838_x2835_161170088}[表示设备未从该服务器接收到]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[会话消息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1765034926 .myid}
[]{#_Toc404796686}[]{#struct_0_19838_x2835_x2074411029}

**SNTP \-- SNTP配置命令 \-- display sntp sessions**

------------------------------------------------------------------------

[**[display sntp sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_x575770074}[命令用来显示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_742720162}

[**[display sntp sessions]{lang="EN-US"}**]{#struct_0_19838_x2835_x2074214421}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x517616302}

[[任意视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_286178324}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x113466111}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_420395986}

[[network-operator]{lang="EN-US"}]{#struct_0_19838_x2835_1909729039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x2074279957}

[[mdc-operator]{lang="EN-US"}]{#struct_0_19838_x2835_1215994093}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x53422477}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_913051519}[显示]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[\<Sysname\> display sntp sessions]{lang="EN-US"}]{#struct_0_19838_x2835_1840245650}

[SNTP server     Stratum   Version    Last receive time]{lang="EN-US"}

[1.0.1.11        2         4          Tue, May 17 2011  9:11:20.833 (Synced)]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[display sntp sessions]{lang="EN-US"}]{#struct_0_19838_x2835_x1364924854}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x325122698}[[字段]{style="font-family:黑体"}]{#struct_0_19838_x2835_x2074083349}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_19838_x2835_608117450}

[[SNTP server]{lang="EN-US"}]{#struct_0_19838_x2835_2001087480}

[[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_x2074148885}[服务器，即]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器。若该字段显示为]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[，表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址尚未解析成功]{style="font-family:宋体"}

[[Stratum]{lang="EN-US"}]{#struct_0_19838_x2835_x1915979223}

[[时钟的层数]{style="font-family:宋体"}]{#struct_0_19838_x2835_1061005599}

[[时钟层数决定了时钟的准确度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_19838_x2835_1342151370}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，层数取值越小，表示时钟的准确度越高，层数为]{style="font-family:宋体"}[16]{lang="EN-US"}[的时钟处于未同步状态]{style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_19838_x2835_x2074607640}

[[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_x104525004}[版本号]{style="font-family:宋体"}

[[Last receive time]{lang="EN-US"}]{#struct_0_19838_x2835_543897674}

[[上一次接收到消息的时间，]{style="font-family:宋体"}[Synced]{lang="EN-US"}]{#struct_0_19838_x2835_1624316374}[标识本地时钟从该服务器获得同步]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1842084453 .myid}
[]{#_Toc404796687}[]{#struct_0_19838_x2835_x418183989}[]{#_Toc296433183}

**SNTP \-- SNTP配置命令 \-- sntp authentication enable**

------------------------------------------------------------------------

[**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1826583617}[命令用来使能]{style="font-family:
宋体"}[SNTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[**[undo sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1232113935}[命令用来关闭]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x157251178}

[**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_784366917}

[**[undo sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1173766810}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1586696119}

[[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_1726795280}[身份验证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_134141365}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_499830450}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_312612343}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_128354579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1709227487}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x170098188}

[[在一些对安全性要求较高的网络中，运行]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_1661033659}[协议时需要启用身份验证功能。通过客户端和服务器端的身份验证，保证客户端只与通过验证的服务器进行时间同步，避免客户端从非法的服务器获得错误的时间同步信息。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_1726729744}[身份验证功能后，还需要设置身份验证密钥，并将其设置为可信密钥，才能正确地进行身份验证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1609321709}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1224448167}[使能]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[身份验证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x2043881422}

[\[Sysname\] sntp authentication enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_62113604}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_370930816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x983580708}
:::

::: {#2088430263 .myid}
[]{#_Toc404796688}[]{#struct_0_19838_x2835_1406682315}[]{#_Toc296433184}

**SNTP \-- SNTP配置命令 \-- sntp authentication-keyid**

------------------------------------------------------------------------

[**[sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1726664208}[命令用来设置]{style="font-family:
宋体"}[SNTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[**[undo sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1669488945}[命令用来取消]{style="font-family:
宋体"}[SNTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x824660373}

[**[sntp authentication-keyid]{lang="EN-US"}**[ *keyid* **authentication-mode md5** { **cipher** \| **simple** } *value*]{lang="EN-US"}]{#struct_0_19838_x2835_x2146238053}

[**[undo sntp authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_718035054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x935961201}

[[没有设置]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_x269390243}[身份验证密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1013194983}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_248764266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1726598672}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_851630097}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1872764689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1688402166}

[*[keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_x2137541522}[：密钥编号，用来标识身份验证密钥，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[authentication-mode md5]{lang="EN-US"}**]{#struct_0_19838_x2835_x1488003580}[：表示采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行身份验证。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_19838_x2835_1596046462}[：表示以密文形式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_19838_x2835_1261847016}[：表示以明文形式设置密钥。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_19838_x2835_1162380032}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法的密钥值，明文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，密文形式输入密钥时为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1726533136}

[[在一些对安全性要求较高的网络中，运行]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_1262653710}[协议时需要启用身份验证功能。通过客户端和服务器端的身份验证，保证客户端只与通过验证的服务器进行同步，提高了网络安全性。]{style="font-family:宋体"}

[[本命令用来设置用于身份验证的密钥。客户端和服务器上需要配置相同的密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_19838_x2835_274968922}[及密钥值，否则无法实现时间同步。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_x376024821}[验证密钥后，还需要通过]{style="font-family:宋体"}**[sntp reliable authentication-keyid]{lang="EN-US"}**[命令将该密钥设置为可信密钥。如果]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[验证密钥被指定为可信密钥，删除密钥后，该密钥将自动变为不可信密钥，不必再执行]{style="font-family:宋体"}**[undo sntp reliable authentication-keyid]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_19838_x2835_1154339849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过重复执行本命令，可以配置多个]{style="font-family:宋体"}]{#struct_0_19838_x2835_909989229}[SNTP]{lang="EN-US"}[身份验证密钥。设备上最多可以配置]{style="font-family:宋体"}[128]{lang="EN-US"}[个]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[身份验证密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的密钥，均以密文的形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_19838_x2835_404459006}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x592826628}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_1726467600}[设置]{style="font-family:宋体"}[MD5]{lang="EN-US"}[身份验证密钥，密钥]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，密钥为]{style="font-family:宋体"}[BetterKey]{lang="EN-US"}[，以明文形式输入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_2031402688}

[\[Sysname\] sntp authentication enable]{lang="EN-US"}

[\[Sysname\] sntp authentication-keyid 10 authentication-mode md5 simple BetterKey]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_2040132172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_59264439}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x12287628}
:::

::: {#-1124152731 .myid}
[]{#_Toc296433185}[]{#_Toc404796689}[]{#struct_0_19838_x2835_x1559881554}

**SNTP \-- SNTP配置命令 \-- sntp enable**

------------------------------------------------------------------------

[**[sntp enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x1430518277}[命令用来开启]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[undo sntp enable]{lang="EN-US"}**]{#struct_0_19838_x2835_1875986345}[命令用来关闭]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1726402064}

[**[sntp]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_19838_x2835_500112527}

[**[undo]{lang="EN-US"}**[ **sntp** **enable**]{lang="EN-US"}]{#struct_0_19838_x2835_1372936649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1372328058}

[[没有开启]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_833524987}[服务。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1841717026}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x583926672}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x180081023}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1726336528}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1267944138}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_31008016}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_627607678}[开启]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1049046228}

[\[Sysname\] sntp enable]{lang="EN-US"}
:::

::: {#261251668 .myid}
[]{#_Toc404796690}[]{#struct_0_19838_x2835_x1076159990}

**SNTP \-- SNTP配置命令 \-- sntp ipv6 unicast-server**

------------------------------------------------------------------------

[**[sntp]{lang="EN-US"}**[ **ipv6** **unicast-server**]{lang="EN-US"}]{#struct_0_19838_x2835_95642142}[命令用来为设备指定]{style="font-family:
宋体"}[IPv6 NTP]{lang="EN-US"}[服务器。]{style="font-family:
宋体"}

[**[undo sntp]{lang="EN-US"}**[ **ipv6 unicast-server**]{lang="EN-US"}]{#struct_0_19838_x2835_668866405}[命令用来取消为设备指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1022438189}

[**[sntp ipv6 unicast-server]{lang="EN-US"}**[ { *server-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid* \| **source** *interface-type interface-number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_1727319568}

[**[undo sntp ipv6 unicast-server ]{lang="EN-US"}**[{ *server-name* \| *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x2835_97537399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1122023816}

[[没有为设备指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1335186088}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1745398635}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x1495724047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_449739693}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_654847166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_1727254032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_2077909428}

[*[server-name]{lang="EN-US"}*]{#struct_0_19838_x2835_1943539144}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_19838_x2835_980442274}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x2835_2042582996}*[：]{style="font-family:宋体"}*[指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x1212985799}[：指定向]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器发送报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器之间不会进行身份验证。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19838_x2835_x278539515}[：指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文的源接口。如果指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器地址不是链路本地地址，则本地设备给服务器发送]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文时，报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为指定源接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。如果指定的]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[服务器地址是链路本地地址，则]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}[报文从指定的源接口发送，并且报文的源地址为该接口的链路本地地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则设备自动选择报文的源]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址，具体选择原则请参见]{style="font-family:宋体"}[RFC 3484]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x338827026}

[[为设备指定]{style="font-family:宋体"}[IPv6 NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1923646792}[服务器后，设备可以与该服务器进行时间同步。设备的时间获得同步后，不能作为服务器为其他设备提供时间同步。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_1726795281}[向某个]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo sntp unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_134075829}[命令时，如果指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{lang="EN-US" style="font-family:
宋体"}[VPN]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置；如果没有指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1485379514}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址时，必须指定报文的源接口，并且不能指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1485629522}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x457619727}[配置设备的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x69197050}

[\[Sysname\] sntp ipv6 unicast-server 2001::1 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_577185417}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_30536965}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1726729745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1609387245}
:::

::: {#-881181227 .myid}
[]{#_Toc404796691}[]{#struct_0_19838_x2835_1166901729}[]{#_Toc296433186}

**SNTP \-- SNTP配置命令 \-- sntp reliable authentication-keyid**

------------------------------------------------------------------------

[**[sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1120257854}[命令用来指定已创建的密钥是可信的。]{style="font-family:宋体"}

[**[undo sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1016086646}[命令用来取消可信密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1992357241}

[**[sntp reliable authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x1617113753}

[**[undo sntp reliable authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x293578909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x9273042}

[[没有配置可信密钥。]{style="font-family:宋体"}]{#struct_0_19838_x2835_1726664209}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1669554481}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_1932404124}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1042956845}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1575450863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1658993828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_505402263}

[*[keyid]{lang="EN-US"}*]{#struct_0_19838_x2835_x58512680}[：密钥编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1726598673}

[[使能身份验证功能后，客户端只会同步到提供可信密钥的服务器；如果服务器提供的密钥不是可信的，那么客户端不会与其同步。]{style="font-family:宋体"}]{#struct_0_19838_x2835_851564561}

[[本命令的使用前提是认证开关已经打开并且配置了密钥，即保证该密钥的存在性后才能设定它是否可信。如果]{style="font-family:宋体"}[SNTP]{lang="EN-US"}]{#struct_0_19838_x2835_x1962902437}[验证密钥被指定为可信密钥，删除密钥后，该密钥将自动变为不可信密钥，不必再执行]{style="font-family:宋体"}**[undo sntp reliable authentication-keyid]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x674535026}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x381722574}[使能]{style="font-family:宋体"}[SNTP]{lang="EN-US"}[身份验证功能，配置编号为]{style="font-family:宋体"}[37]{lang="EN-US"}[的密钥采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行身份验证，密钥值为]{style="font-family:宋体"}[BetterKey]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1830462506}

[\[Sysname\] sntp authentication enable]{lang="EN-US"}

[\[Sysname\] sntp authentication-keyid 37 authentication-mode md5 BetterKey]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x878612314}[指定该密钥为可信密钥。]{style="font-family:宋体"}

[[\[Sysname\] sntp reliable authentication-keyid 37]{lang="EN-US"}]{#struct_0_19838_x2835_638643190}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1726533137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_1262588174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_698003020}
:::

::: {#310517453 .myid}
[]{#_Toc404796692}[]{#struct_0_19838_x2835_1917409773}[]{#_Toc296433187}

**SNTP \-- SNTP配置命令 \-- sntp unicast-server**

------------------------------------------------------------------------

[**[sntp]{lang="EN-US"}**[ **unicast-server**]{lang="EN-US"}]{#struct_0_19838_x2835_1068119259}[命令用来为设备指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo sntp]{lang="EN-US"}**[ **unicast-server**]{lang="EN-US"}]{#struct_0_19838_x2835_1996825461}[命令用来取消为设备指定的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_472561020}

[**[sntp unicast-server]{lang="EN-US"}**[ { *server-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \] \[ **authentication-keyid** *keyid \|* **source** *interface-type interface-number \|* **version** *number* \] \*]{lang="EN-US"}]{#struct_0_19838_x2835_230825890}

[**[undo sntp unicast-server ]{lang="EN-US"}**[{ *server-name* \| *ip-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_19838_x2835_1726467601}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_19838_x2835_2031468224}

[[没有为设备指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1985523192}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1449065923}

[[系统视图]{style="font-family:宋体"}]{#struct_0_19838_x2835_x760271174}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1275357897}

[[network-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1514745141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_19838_x2835_x1993991864}

[[【参数】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1970136190}

[*[server-name]{lang="EN-US"}*]{#struct_0_19838_x2835_1726402065}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的主机名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_19838_x2835_500178063}[：]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该地址只能是一个单播地址，不能为广播地址、组播地址或本地时钟的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_19838_x2835_x164228208}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[authentication-keyid]{lang="EN-US"}**[ *keyid*]{lang="EN-US"}]{#struct_0_19838_x2835_x1801421878}[：指定向]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器发送报文时，使用指定的密钥计算报文的摘要。]{style="font-family:宋体"}*[keyid]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，则本端设备与]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器之间不会进行身份验证。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_19838_x2835_2066966498}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源接口。本地设备给服务器发送]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文时，报文的源地址为指定源接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和接口编号。如果未指定本参数，则根据路由表查找报文的出接口，并采用出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[NTP]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[version]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_19838_x2835_x643432037}[：指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}[版本号。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1646581734}

[[为设备指定]{style="font-family:宋体"}[NTP]{lang="EN-US"}]{#struct_0_19838_x2835_1238326668}[服务器后，设备可以与该服务器进行时间同步。设备的时间获得同步后，不能作为服务器为其他设备提供时间同步。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}]{#struct_0_19838_x2835_x571134970}[向某个]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[内的其他]{lang="EN-US" style="font-family:宋体"}[PE]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[CE]{lang="EN-US"}[同步时，需要指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{lang="EN-US" style="font-family:宋体"}**[undo sntp unicast-server]{lang="EN-US"}**]{#struct_0_19838_x2835_1726336529}[命令时，如果指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消指定]{lang="EN-US" style="font-family:
宋体"}[VPN]{lang="EN-US"}[内]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置；如果没有指定]{lang="EN-US" style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[参数，则取消公网中]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{lang="EN-US" style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[的]{lang="EN-US" style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_19838_x2835_1267878602}

[[\# ]{lang="EN-US"}]{#struct_0_19838_x2835_x1457279508}[配置设备的]{style="font-family:宋体"}[NTP]{lang="EN-US"}[服务器为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，版本号为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_19838_x2835_x1978346389}

[\[Sysname\] sntp unicast-server 10.1.1.1 version 4]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_19838_x2835_x1919854657}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication enable]{lang="EN-US"}**]{#struct_0_19838_x2835_x952906995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1931462827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sntp reliable authentication-keyid]{lang="EN-US"}**]{#struct_0_19838_x2835_x1106849250}

[ ]{lang="EN-US"}
:::
