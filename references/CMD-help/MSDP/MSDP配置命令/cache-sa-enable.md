::: {#-1168560752 .myid}
[]{#_Toc404789807}[]{#struct_0_12956_16881_1235595400}[]{#_Toc293993430}[]{#_Toc94588307}[]{#_Toc80176823}

**MSDP \-- MSDP配置命令 \-- cache-sa-enable**

------------------------------------------------------------------------

[**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1873752559}[命令用来使能]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文缓存机制，即缓存]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中所包含的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:宋体"}

[**[undo cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1240977538}[命令用来关闭]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文缓存机制。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1987153923}

[**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x474613650}

[**[undo cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1024166049}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1767497414}

[[SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873949167}[报文缓存机制处于使能状态，即设备在收到]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文后缓存其中包含的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1792836653}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1982171650}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1763965335}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x974483616}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x433555687}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_871865205}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1873883631}[在公网实例中使能]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文缓存机制，使设备在收到]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文后缓存其中包含的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1508034110}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] cache-sa-enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_727971414}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp sa-cache]{lang="EN-US"}**]{#struct_0_12956_16881_1940188452}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp sa-count]{lang="EN-US"}**]{#struct_0_12956_16881_x1215698796}
:::

::: {#-1491890176 .myid}
[]{#_Toc404789808}[]{#struct_0_12956_16881_x591117310}[]{#_Toc293993431}[]{#_Toc94588309}[]{#_Toc80176825}[]{#_Toc135121746}[]{#_Toc135121747}[]{#_Toc135121749}[]{#_Toc135121750}[]{#_Toc135121751}[]{#_Toc135121752}[]{#_Toc135121753}[]{#_Toc135121754}[]{#_Toc135121755}[]{#_Toc135121756}[]{#_Toc135121757}[]{#_Toc135121758}[]{#_Toc135121759}[]{#_Toc135121760}[]{#_Toc135121761}

**MSDP \-- MSDP配置命令 \-- display msdp brief**

------------------------------------------------------------------------

[**[display msdp brief]{lang="FR"}**]{#struct_0_12956_16881_72718907}[命令用来显示]{style="font-family:宋体"}[MSDP]{lang="FR"}[对等体的简要信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1873555951}

[**[display msdp]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **brief** \[ **state** { **connect** \| **disabled** \| **established** \| **listen** \| **shutdown** } \]]{lang="EN-US"}]{#struct_0_12956_16881_x1199863126}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1859547948}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12956_16881_136049709}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_154764172}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x769279956}

[[network-operator]{lang="EN-US"}]{#struct_0_12956_16881_1700982881}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_436746644}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12956_16881_x1727661325}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1873490415}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x1069290539}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[**[state]{lang="EN-US"}**]{#struct_0_12956_16881_1587112112}[：显示处于指定状态下]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的简要信息。如果未指定本参数，将显示处于所有状态下]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的简要信息。]{style="font-family:宋体"}

[**[connect]{lang="EN-US"}**]{#struct_0_12956_16881_x406811109}[：表示连接状态。]{style="font-family:宋体"}

[**[disabled]{lang="EN-US"}**]{#struct_0_12956_16881_742483585}[：表示连接失败状态。]{style="font-family:宋体"}

[**[established]{lang="FR"}**]{#struct_0_12956_16881_x1709064812}[：]{style="font-family:宋体"}[表示会话状态。]{style="font-family:宋体"}

[**[listen]{lang="FR"}**]{#struct_0_12956_16881_320328841}[：]{style="font-family:宋体"}[表示监听状态。]{style="font-family:宋体"}

[**[shutdown]{lang="EN-US"}**]{#struct_0_12956_16881_1464057853}[：表示手动关闭状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x742554612}

[[\# ]{lang="FR"}]{#struct_0_12956_16881_x1874080242}[显示公网实例中处于所有状态下]{style="font-family:宋体"}[MSDP]{lang="FR"}[对等体的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display msdp brief]{lang="EN-US"}]{#struct_0_12956_16881_1527277770}

[Configured   Established  Listen       Connect      Shutdown     Disabled]{lang="EN-US"}

[1            1            0            0            0            0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Peer address    State       Up/Down time    AS         SA count   Reset count]{lang="EN-US"}

[20.20.20.20     Established 00:00:13        100        0          0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display msdp brief]{lang="EN-US"}]{#struct_0_12956_16881_x1648640119}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1682313010}[[字段]{style="font-family:黑体"}]{#struct_0_12956_16881_x1426796111}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12956_16881_1552616462}

[[Configured]{lang="EN-US"}]{#struct_0_12956_16881_2058534}

[[已配置的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1874014706}[对等体的数量]{style="font-family:宋体"}

[[Established]{lang="EN-US"}]{#struct_0_12956_16881_x88361100}

[[处于]{style="font-family:宋体"}[Established]{lang="EN-US"}]{#struct_0_12956_16881_1995225543}[状态的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的数量]{style="font-family:宋体"}

[[Listen]{lang="EN-US"}]{#struct_0_12956_16881_x1349732668}

[[处于]{style="font-family:宋体"}[Listen]{lang="EN-US"}]{#struct_0_12956_16881_2076065830}[状态的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的数量]{style="font-family:宋体"}

[[Connect]{lang="EN-US"}]{#struct_0_12956_16881_x1230731686}

[[处于]{style="font-family:宋体"}[Connect]{lang="EN-US"}]{#struct_0_12956_16881_x1340615606}[状态的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的数量]{style="font-family:宋体"}

[[Shutdown]{lang="EN-US"}]{#struct_0_12956_16881_x1874211314}

[[处于]{style="font-family:宋体"}[Shutdown]{lang="EN-US"}]{#struct_0_12956_16881_677159078}[状态的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的数量]{style="font-family:宋体"}

[[Disabled]{lang="EN-US"}]{#struct_0_12956_16881_1643517620}

[[处于]{style="font-family:宋体"}[Disabled]{lang="EN-US"}]{#struct_0_12956_16881_x865731539}[状态的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的数量]{style="font-family:宋体"}

[[Peer address]{lang="EN-US"}]{#struct_0_12956_16881_1580111365}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1874145778}[对等体的地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12956_16881_590594879}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_218871472}[对等体的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_12956_16881_x1877590720}[：连接建立，处于会话状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listen]{lang="EN-US"}]{#struct_0_12956_16881_x316066981}[：连接建立，本地作为服务器端，处于监听状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connect]{lang="EN-US"}]{#struct_0_12956_16881_x1109148953}[：连接未建立，本地作为客户端，处于连接状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown]{lang="EN-US"}]{#struct_0_12956_16881_x1873818098}[：被关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_12956_16881_1420414424}[：连接失败]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[Up/Down time]{lang="EN-US"}]{#struct_0_12956_16881_89678066}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_2142699650}[对等体连接已建立]{style="font-family:宋体"}[/]{lang="EN-US"}[失败的时长]{style="font-family:宋体"}

[[AS]{lang="EN-US"}]{#struct_0_12956_16881_x1873752562}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x31189493}[对等体所在自治系统的号码，"]{style="font-family:宋体"}[?]{lang="EN-US"}["表示无法获得自治系统号码]{style="font-family:宋体"}

[[SA count]{lang="EN-US"}]{#struct_0_12956_16881_x375020146}

[[缓存中从该]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1464794729}[对等体获得的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量]{style="font-family:宋体"}

[[Reset count]{lang="EN-US"}]{#struct_0_12956_16881_x1129825265}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1873949170}[对等体连接复位的次数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1663444700 .myid}
[]{#_Toc404789809}[]{#struct_0_12956_16881_x1389617662}[]{#_Toc293993432}[]{#_Toc94588310}[]{#_Toc80176826}

**MSDP \-- MSDP配置命令 \-- display msdp peer-status**

------------------------------------------------------------------------

[**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_469298130}[命令用来显示]{style="font-family:
宋体"}[MSDP]{lang="EN-US"}[对等体的详细状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1171010107}

[**[display msdp ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[peer-status]{lang="EN-US"}**[ \[ *peer-address* \]]{lang="EN-US"}]{#struct_0_12956_16881_1208349445}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1270268548}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12956_16881_2035463645}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1363377589}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1873883634}

[[network-operator]{lang="EN-US"}]{#struct_0_12956_16881_748519223}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x2050853734}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12956_16881_x1260440742}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x214898105}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x467765255}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_291137643}[：显示指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2071994056}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_1865336220}[显示公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[20.20.20.20]{lang="EN-US"}[的详细状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display msdp peer-status 20.20.20.20]{lang="EN-US"}]{#struct_0_12956_16881_x1873490418}

[MSDP peer 20.20.20.20; AS 100]{lang="EN-US"}

[ Description:]{lang="EN-US"}

[ Information about connection status:]{lang="EN-US"}

[   State: Disabled]{lang="EN-US"}

[   Up/down time: 14:41:08]{lang="EN-US"}

[   Resets: 0]{lang="EN-US"}

[   Connection interface: LoopBack0 (20.20.20.30)]{lang="EN-US"}

[   Received/sent messages: 867/867]{lang="EN-US"}

[   Discarded input messages: 0]{lang="EN-US"}

[   Discarded output messages: 0]{lang="EN-US"}

[   Elapsed time since last connection or counters clear: 14:42:40]{lang="EN-US"}

[   Mesh group peer joined: momo]{lang="EN-US"}

[   Last disconnect reason: Hold timer expired with truncated message]{lang="EN-US"}

[   Truncated packet: 5 bytes in buffer, type: 1, length: 20, without packet time: 75s]{lang="EN-US"}

[ Information about (Source, Group)-based SA filtering policy:]{lang="EN-US"}

[   Import policy: None]{lang="EN-US"}

[   Export policy: None]{lang="EN-US"}

[ Information about SA-Requests:]{lang="EN-US"}

[   Policy to accept SA-Requests: None]{lang="EN-US"}

[   Sending SA-Requests status: Disable]{lang="EN-US"}

[ Minimum TTL to forward SA with encapsulated data: 0]{lang="EN-US"}

[ SAs learned from this peer: 0, SA cache maximum for the peer: 4294967295]{lang="EN-US"}

[ Input queue size: 0, Output queue size: 0]{lang="EN-US"}

[ Counters for MSDP messages:]{lang="EN-US"}

[   RPF check failure: 0]{lang="EN-US"}

[   Incoming/outgoing SA: 0/0]{lang="EN-US"}

[   Incoming/outgoing SA-Request: 0/0]{lang="EN-US"}

[   Incoming/outgoing SA-Response: 0/0]{lang="EN-US"}

[   Incoming/outgoing Keepalive: 867/867]{lang="EN-US"}

[   Incoming/outgoing Notification: 0/0]{lang="EN-US"}

[   Incoming/outgoing Traceroutes in progress: 0/0]{lang="EN-US"}

[   Incoming/outgoing Traceroute reply: 0/0]{lang="EN-US"}

[   Incoming/outgoing Unknown: 0/0]{lang="EN-US"}

[   Incoming/outgoing data packet: 0/0]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display msdp peer-status]{lang="EN-US"}]{#struct_0_12956_16881_46454708}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1678298262}[[字段]{style="font-family:黑体"}]{#struct_0_12956_16881_x1734855814}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12956_16881_1845772189}

[[MSDP peer]{lang="EN-US"}]{#struct_0_12956_16881_1493457463}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1010512702}[对等体的地址]{style="font-family:宋体"}

[[AS]{lang="EN-US"}]{#struct_0_12956_16881_x1874080241}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_1123993243}[对等体所在自治系统的号码，"]{style="font-family:宋体"}[?]{lang="EN-US"}["表示无法获得自治系统号码]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_12956_16881_x794980210}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1449711992}[对等体的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Established]{lang="EN-US"}]{#struct_0_12956_16881_60817906}[：连接建立，处于会话状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Listen]{lang="EN-US"}]{#struct_0_12956_16881_2007525065}[：连接建立，本地作为服务器端，处于监听状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connect]{lang="EN-US"}]{#struct_0_12956_16881_x1874014705}[：连接未建立，本地作为客户端，处于连接状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown]{lang="EN-US"}]{#struct_0_12956_16881_x1654445041}[：关闭状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_12956_16881_x1797943817}[：连接失败]{lang="EN-US" style="font-family:宋体"}[状态]{style="font-family:宋体"}

[[Up/Down time]{lang="EN-US"}]{#struct_0_12956_16881_2099240388}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x761246734}[对等体连接已建立]{style="font-family:宋体"}[/]{lang="EN-US"}[失败的时长]{style="font-family:宋体"}

[[Resets]{lang="EN-US"}]{#struct_0_12956_16881_x1874211313}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x888924863}[对等体连接复位的次数]{style="font-family:宋体"}

[[Connection interface]{lang="EN-US"}]{#struct_0_12956_16881_x833611851}

[[用于与对端对等体地址建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_12956_16881_2066574909}[连接的接口及其]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Received/sent messages]{lang="EN-US"}]{#struct_0_12956_16881_x1763567142}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1874145777}[通过该连接接收和发送的报文数目]{style="font-family:宋体"}

[[Discarded input messages]{lang="EN-US"}]{#struct_0_12956_16881_x168920008}

[[丢弃的入报文数目]{style="font-family:宋体"}]{#struct_0_12956_16881_x1873818097}

[[Discarded output messages]{lang="EN-US"}]{#struct_0_12956_16881_x145669517}

[[丢弃的出报文数目]{style="font-family:宋体"}]{#struct_0_12956_16881_x1873752561}

[[Elapsed time since last connection or counters clear]{lang="EN-US"}]{#struct_0_12956_16881_x1597273434}

[[最近一次清除该]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x909539832}[对等体信息时刻距现在的时间]{style="font-family:宋体"}

[[Mesh group peer joined]{lang="EN-US"}]{#struct_0_12956_16881_x1873949169}

[[该对等体加入全连接组的名称，注意如果未加入全连接组则不显示此行信息]{style="font-family:宋体"}]{#struct_0_12956_16881_1695561589}

[[Last disconnect reason]{lang="EN-US"}]{#struct_0_12956_16881_x86383754}

[[与该对等体的连接上一次断开的原因，如果为空表示与该对等体建立连接以来还没有断开过：]{style="font-family:宋体"}]{#struct_0_12956_16881_504123905}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold timer expired without message]{lang="EN-US"}]{#struct_0_12956_16881_x1873883633}[：]{lang="EN-US" style="font-family:宋体"}[Hold timer]{lang="EN-US"}[超时，且此时接收缓冲区中没有任何报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hold timer expired with truncated message]{lang="EN-US"}]{#struct_0_12956_16881_x1873555953}[：]{style="font-family:宋体"}[Hold timer]{lang="EN-US"}[超时，且此时接收缓冲区中有不完整的报文：]{style="font-family:宋体"}

[[a.[  ]{style="font:7.0pt "}]{lang="EN-US"}[bytes in buffer]{lang="EN-US"}]{#struct_0_12956_16881_1932304756}[：断开连接时接收缓冲区中数据的实际长度]{style="font-family:宋体"}

[[b.[  ]{style="font:7.0pt "}]{lang="EN-US"}[type]{lang="EN-US"}]{#struct_0_12956_16881_660488911}[：断开连接时接收缓冲区中报文的类型]{style="font-family:宋体"}

[[c.[   ]{style="font:7.0pt "}]{lang="EN-US"}[length]{lang="EN-US"}]{#struct_0_12956_16881_670245086}[：断开连接时接收缓冲区中报文的长度，注意如果报文过小无法解析出这个字段则不显示该信息]{style="font-family:宋体"}

[[d.[  ]{style="font:7.0pt "}]{lang="EN-US"}[without packet time]{lang="EN-US"}]{#struct_0_12956_16881_x1873490417}[：断开连接的时间到最后一次处理报文的时间间隔]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Remote peer has been closed]{lang="EN-US"}]{#struct_0_12956_16881_2062877343}[：接收报文时发现对等体已经被关闭]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP ERROR/HUP event received]{lang="EN-US"}]{#struct_0_12956_16881_x1874080244}[：发送报文时]{style="font-family:
  宋体"}[TCP socket]{lang="EN-US"}[收到]{style="font-family:
  宋体"}[ERROR/HUP]{lang="EN-US"}[事件]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Illegal message received]{lang="EN-US"}]{#struct_0_12956_16881_x1874014708}[：接收到了不合法的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Notification received]{lang="EN-US"}]{#struct_0_12956_16881_x1874211316}[：接收到了]{style="font-family:宋体"}[Notification]{lang="EN-US"}[报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reset command executed]{lang="EN-US"}]{#struct_0_12956_16881_x485640336}[：用户执行了]{style="font-family:宋体"}**[reset msdp peer]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown command executed]{lang="EN-US"}]{#struct_0_12956_16881_1095320873}[：用户执行了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interface downed]{lang="EN-US"}]{#struct_0_12956_16881_x1196271409}[：收到与对等体建立连接的接口]{style="font-family:宋体"}[down]{lang="EN-US"}[的事件]{style="font-family:宋体"}

[[Information about (Source, Group)-based SA filtering policy]{lang="EN-US"}]{#struct_0_12956_16881_x1874145780}

[[SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873818100}[报文过滤列表信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Import policy]{lang="EN-US"}]{#struct_0_12956_16881_1776054961}[：接收指定]{lang="EN-US" style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[报文的过滤列表]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Export policy]{lang="EN-US"}]{#struct_0_12956_16881_x1873752564}[：转发指定]{lang="EN-US" style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[报文的过滤列表]{lang="EN-US" style="font-family:宋体"}

[[Information about SA-Requests]{lang="EN-US"}]{#struct_0_12956_16881_x1873949172}

[[SA]{lang="EN-US"}]{#struct_0_12956_16881_1742550220}[请求报文信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Policy to accept SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873555956}[-R]{lang="EN-US"}[equests]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[针对]{style="font-family:宋体"}[来自指定]{lang="EN-US" style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[请求]{style="font-family:宋体"}[报文的过滤规则]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[None]{lang="EN-US"}[表示]{style="font-family:宋体"}[不对]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文进行过滤]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Sending SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873490420}[-R]{lang="EN-US"}[equests status]{lang="EN-US"}[：是否使能在收到一个新的组加入报文时，向其指定的]{lang="EN-US" style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体发送]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文]{lang="EN-US" style="font-family:宋体"}

[[Minimum TTL to forward SA with encapsulated data]{lang="EN-US"}]{#struct_0_12956_16881_x309972260}

[[封装在]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x1874080243}[报文中的组播数据包的最小]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值]{style="font-family:宋体"}

[[SAs learned from this peer]{lang="EN-US"}]{#struct_0_12956_16881_x38806171}

[[已缓存从指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1874014707}[对等体学到的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量]{style="font-family:宋体"}

[[SA cache maximum for the peer]{lang="EN-US"}]{#struct_0_12956_16881_1477722841}

[[可缓存从指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x393798176}[对等体学到的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的最大数量]{style="font-family:宋体"}

[[Input queue size]{lang="EN-US"}]{#struct_0_12956_16881_x1874211315}

[[接收缓冲区中所缓存的数据长度]{style="font-family:宋体"}]{#struct_0_12956_16881_x2051724277}

[[Output queue size]{lang="EN-US"}]{#struct_0_12956_16881_22973976}

[[发送缓冲区中所缓存的数据长度]{style="font-family:宋体"}]{#struct_0_12956_16881_x1874145779}

[[Counters for MSDP messages]{lang="EN-US"}]{#struct_0_12956_16881_x975489062}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1873818099}[报文的统计数：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RPF check failure]{lang="EN-US"}]{#struct_0_12956_16881_x1873752563}[：未通过]{lang="EN-US" style="font-family:
  宋体"}[RPF]{lang="EN-US"}[检查而被丢弃的]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}[报文的统计数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873949171}[：接收和发送的]{lang="EN-US" style="font-family:
  宋体"}[SA]{lang="EN-US"}[报文的统计数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873883635}[-R]{lang="EN-US"}[equest]{lang="EN-US"}[：接收和发送的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文的统计数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing SA]{lang="EN-US"}]{#struct_0_12956_16881_x1873555955}[-R]{lang="EN-US"}[esponse]{lang="EN-US"}[：接收和发送的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[回应]{style="font-family:宋体"}[报文的统计数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing Keepalive]{lang="EN-US"}]{#struct_0_12956_16881_x1873490419}[：接收和发送的]{style="font-family:
  宋体"}[Keepalive]{lang="EN-US"}[报文的统计数]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing Notification]{lang="EN-US"}]{#struct_0_12956_16881_x307996299}[：接收和发送的]{style="font-family:
  宋体"}[Notification]{lang="EN-US"}[报文的统计数]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing ]{lang="EN-US"}]{#struct_0_12956_16881_x307930763}[Traceroutes in progress]{lang="EN-US"}[：接收和发送的]{style="font-family:宋体"}[Traceroute in progress]{lang="EN-US"}[报文的统计数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing ]{lang="EN-US"}]{#struct_0_12956_16881_x308127371}[Traceroute reply]{lang="EN-US"}[：接收和发送的]{style="font-family:宋体"}[Traceroute replys]{lang="EN-US"}[报文的统计数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing Unknown]{lang="EN-US"}]{#struct_0_12956_16881_x308061835}[：接收和发送的无法识别类型报文的统计数]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Incoming/outgoing data packet]{lang="EN-US"}]{#struct_0_12956_16881_x307734155}[：接收和发送的封装有组播数据的]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[报文的统计数]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1160701072 .myid}
[]{#_Toc404789810}[]{#struct_0_12956_16881_665306094}[]{#_Toc293993433}[]{#_Toc94588311}[]{#_Toc80176827}

**MSDP \-- MSDP配置命令 \-- display msdp sa-cache**

------------------------------------------------------------------------

[**[display msdp sa-cache]{lang="EN-US"}**]{#struct_0_12956_16881_1254229903}[命令用来显示]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307668619}

[**[display msdp ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[sa-cache]{lang="EN-US"}**[ \[ *group-address* \| *source-address* \| *as-number* \] \*]{lang="EN-US"}]{#struct_0_12956_16881_x97544581}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x421371825}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12956_16881_872904084}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2057745044}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_69207465}

[[network-operator]{lang="EN-US"}]{#struct_0_12956_16881_x810468863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_70023035}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12956_16881_x1835032885}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307865227}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_1071069423}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_12956_16881_1127816086}[：显示包含指定组播组地址的信息，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将显示包含所有组播组地址的信息。]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_12956_16881_x618968662}[：显示包含指定组播源地址的信息。如果未指定本参数，将显示包含所有组播源地址的信息。]{style="font-family:宋体"}

[*[as-number]{lang="EN-US"}*]{#struct_0_12956_16881_953776087}[：显示指定自治系统的信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，将显示所有自治系统的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1187499302}

[[只有配置了]{style="font-family:宋体"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_513208103}[命令之后，执行本命令才会有相应的显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_2079821693}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x307799691}[显示公网实例]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项信息。]{style="font-family:
宋体"}

[[\<Sysname\> display msdp sa-cache]{lang="EN-US"}]{#struct_0_12956_16881_x1689122047}

[Total Source-Active Cache - 5 entries]{lang="EN-US"}

[Matched 5 entries]{lang="EN-US"}

[ ]{lang="EN-US"}

[Source          Group           Origin RP       Pro  AS         Uptime   Expires]{lang="EN-US"}

[10.10.1.2       225.0.0.1       10.10.10.10     BGP  100        00:00:11 00:05:49]{lang="EN-US"}

[10.10.1.2       225.0.0.2       10.10.10.10     BGP  100        00:00:11 00:05:49]{lang="EN-US"}

[10.10.1.2       225.0.0.3       10.10.10.10     BGP  100        00:00:11 00:05:49]{lang="EN-US"}

[10.10.1.2       225.0.0.4       10.10.10.10     BGP  100        00:00:11 00:05:49]{lang="EN-US"}

[10.10.1.2       225.0.0.5       10.10.10.10     BGP  100        00:00:11 00:05:49]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display msdp sa-cache]{lang="EN-US"}]{#struct_0_12956_16881_1118534975}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2023292583}[[字段]{style="font-family:黑体"}]{#struct_0_12956_16881_x448014615}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12956_16881_826490365}

[[Total Source-Active Cache]{lang="EN-US"}]{#struct_0_12956_16881_x1023685552}

[[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307472011}[缓存中组播源的总数]{style="font-family:宋体"}

[[Matched]{lang="EN-US"}]{#struct_0_12956_16881_x475527125}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x638170779}[匹配的组播源总数]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_12956_16881_x1643453940}

[[组播源源地址]{style="font-family:宋体"}]{#struct_0_12956_16881_x1223653980}

[[Group]{lang="EN-US"}]{#struct_0_12956_16881_2005842880}

[[组播源组地址]{style="font-family:宋体"}]{#struct_0_12956_16881_x307406475}

[[Origin RP]{lang="EN-US"}]{#struct_0_12956_16881_1087822493}

[[生成该（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_1664388411}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的源]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Pro]{lang="EN-US"}]{#struct_0_12956_16881_x900288747}

[[源]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12956_16881_1305580948}[的自治系统号码来源于何种协议类型，"]{style="font-family:宋体"}[?]{lang="EN-US"}["表示无法获得协议类型]{style="font-family:宋体"}

[[AS]{lang="EN-US"}]{#struct_0_12956_16881_831791939}

[[源]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12956_16881_x307996298}[的自治系统号码，"]{style="font-family:宋体"}[?]{lang="EN-US"}["表示无法获得自治系统号码]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_12956_16881_1447746310}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_x1713993772}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项缓存已存在的时间]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_12956_16881_422430893}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_727434131}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项缓存超时剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc293993434}[]{#_Toc94588312}[]{#_Toc80176828}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307930762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_1488122305}

::: {#-1537045135 .myid}
[]{#_Toc404789811}[]{#struct_0_12956_16881_x381383139}

**MSDP \-- MSDP配置命令 \-- display msdp sa-count**

------------------------------------------------------------------------

[**[display msdp sa-count]{lang="EN-US"}**]{#struct_0_12956_16881_1650970609}[命令用来显示]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1370872855}

[**[display msdp ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[sa-count]{lang="EN-US"}**[ \[ *as-number* \]]{lang="EN-US"}]{#struct_0_12956_16881_x2117477743}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x920684486}

[[任意视图]{style="font-family:宋体"}]{#struct_0_12956_16881_680013622}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x308127370}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_2052148907}

[[network-operator]{lang="EN-US"}]{#struct_0_12956_16881_1618066695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_1760685651}

[[mdc-operator]{lang="EN-US"}]{#struct_0_12956_16881_1894423181}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1508640160}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x1192778447}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示公网实例的信息。]{style="font-family:宋体"}

[*[as-number]{lang="EN-US"}*]{#struct_0_12956_16881_x1490901754}[：显示指定自治系统的信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，将显示所有自治系统的信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x293827196}

[[只有配置了]{style="font-family:宋体"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x308061834}[命令之后，执行本命令才会有相应的显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_471295258}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_785515930}[显示公网实例]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量。]{style="font-family:
宋体"}

[[\<Sysname\> display msdp sa-count]{lang="EN-US"}]{#struct_0_12956_16881_1971534761}

[(S, G) entries statistics, counted by peer]{lang="EN-US"}

[  Peer address       SA count]{lang="EN-US"}

[  10.10.10.10        5]{lang="EN-US"}

[ ]{lang="EN-US"}

[(S, G) entries statistics, counted by AS]{lang="EN-US"}

[  AS         Source count        Group count]{lang="EN-US"}

[  ?          3                   3]{lang="EN-US"}

[ ]{lang="EN-US"}

[5 (S, G) entries in total]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display msdp sa-count]{lang="EN-US"}]{#struct_0_12956_16881_592119498}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2018653631}[[字段]{style="font-family:黑体"}]{#struct_0_12956_16881_x1638444967}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_12956_16881_x307734154}

[[(S, G) entries statistics, counted by peer]{lang="EN-US"}]{#struct_0_12956_16881_665371630}

[[按照对等体，统计缓存中（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_x1097970974}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量]{style="font-family:宋体"}

[[Peer address]{lang="EN-US"}]{#struct_0_12956_16881_x842616868}

[[发送]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307668618}[报文的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体地址]{style="font-family:宋体"}

[[SA count]{lang="EN-US"}]{#struct_0_12956_16881_x97610117}

[[来自该对等体的（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_613453148}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项数量]{style="font-family:宋体"}

[[(S, G) entries statistics, counted by AS]{lang="EN-US"}]{#struct_0_12956_16881_x1163230674}

[[按照源]{style="font-family:宋体"}[RP]{lang="EN-US"}]{#struct_0_12956_16881_x173582383}[所属的自治系统，统计缓存中（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的数量]{style="font-family:宋体"}

[[AS]{lang="EN-US"}]{#struct_0_12956_16881_x307865226}

[[自治系统号码，"]{style="font-family:宋体"}[?]{lang="EN-US"}]{#struct_0_12956_16881_1071003887}["表示无法获得自治系统号码]{style="font-family:宋体"}

[[Source count]{lang="EN-US"}]{#struct_0_12956_16881_1895147930}

[[来自该自治系统的组播源的统计数]{style="font-family:宋体"}]{#struct_0_12956_16881_x312881880}

[[Group count]{lang="EN-US"}]{#struct_0_12956_16881_693198478}

[[来自该自治系统的组播组的统计数]{style="font-family:宋体"}]{#struct_0_12956_16881_x307799690}

[[(S, G) entries in total]{lang="EN-US"}]{#struct_0_12956_16881_x1689056511}

[[（]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_12956_16881_692321017}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc80176829}[]{#_Toc293993435}[]{#_Toc94588313}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1827989988}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_635208295}

::: {#1239596456 .myid}
[]{#_Toc404789812}[]{#struct_0_12956_16881_x264823213}

**MSDP \-- MSDP配置命令 \-- encap-data-enable**

------------------------------------------------------------------------

[**[encap-data-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x307472010}[命令用来使能在]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中封装组播数据报文。]{style="font-family:宋体"}

[**[undo encap-data-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x475461589}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_941460972}

[**[encap-data-enable]{lang="EN-US"}**]{#struct_0_12956_16881_1353798342}

[**[undo encap-data-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1493317236}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1541067665}

[[在]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307406474}[报文中只包含（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项，不封装组播数据报文。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1087756957}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x355573684}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1585539935}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1457353652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x829794732}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307996301}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x890447107}[在公网实例中使能在]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中封装组播数据报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_278764224}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] encap-data-enable]{lang="EN-US"}
:::

::: {#877043181 .myid}
[]{#_Toc404789813}[]{#struct_0_12956_16881_x307930765}[]{#_Toc293993436}[]{#_Toc94588314}

**MSDP \-- MSDP配置命令 \-- import-source**

------------------------------------------------------------------------

[**[import-source]{lang="EN-US"}**]{#struct_0_12956_16881_1487663553}[命令用来配置]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的创建规则。]{style="font-family:宋体"}

[**[undo import-source]{lang="EN-US"}**]{#struct_0_12956_16881_x308127373}[命令用来取消]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的创建规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_2052083371}

[**[import-source]{lang="EN-US"}**[ \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_12956_16881_x726418746}

[**[undo import-source]{lang="EN-US"}**]{#struct_0_12956_16881_x1121737165}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1355214004}

[[在创建]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x308061837}[报文时，对其通告的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项不作限制，即]{style="font-family:
宋体"}[SA]{lang="EN-US"}[报文通告域内所有的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_471229722}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x783457028}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_2005836476}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x307734157}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_665437166}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2033348013}

[*[acl-number]{lang="EN-US"}*]{#struct_0_12956_16881_x1021955399}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本或高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。如果指定了本参数，则对通告的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项进行过滤；如果未指定本参数、指定的]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则过滤掉所有（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。在进行规则匹配时，对]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[规则中的协议号将不作检查。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_466009209}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_12956_16881_x676124667}[IPv4]{lang="DA"}[基本]{style="font-family:宋体"}[ACL]{lang="DA"}[，]{style="font-family:
宋体"}[该]{style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定]{style="font-family:宋体"}[组播组]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="DA" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_1990786555}[IPv4]{lang="DA"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[，]{lang="EN-US" style="font-family:宋体"}[该]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="DA"}[规则中的]{lang="EN-US" style="font-family:宋体"}**[source]{lang="DA"}**[参数用来]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[组播]{lang="EN-US" style="font-family:宋体"}[源的]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[组播组]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:
宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[除了可以使用本命令控制]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307668621}[报文的创建，还可以使用]{lang="EN-US" style="font-family:宋体"}**[peer sa-policy]{lang="EN-US"}**[命令控制]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[报文的接收和转发。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x97020294}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x307865229}[在公网实例中配置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体创建]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文时，通告组播路由表中的特定的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项：组播源在]{style="font-family:
宋体"}[10.10.0.0/16]{lang="EN-US"}[网段，组播组地址为]{style="font-family:
宋体"}[225.1.0.0/16]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1070414063}

[\[Sysname\] acl advanced 3101]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3101\] rule permit ip source 10.10.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3101\] quit]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] import-source acl 3101]{lang="EN-US"}

[]{#_Toc293993437}[]{#_Toc94588315}[]{#_Toc80176830}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2059663635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[peer sa-policy]{lang="EN-US"}**]{#struct_0_12956_16881_x945198454}
:::

::: {#-441955143 .myid}
[]{#_Toc404789814}[]{#struct_0_12956_16881_x307799693}

**MSDP \-- MSDP配置命令 \-- msdp**

------------------------------------------------------------------------

[**[msdp]{lang="EN-US"}**]{#struct_0_12956_16881_x1689253119}[命令用来使能]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo msdp]{lang="EN-US"}**]{#struct_0_12956_16881_383426517}[命令用来关闭]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[，并清除]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[视图下的所有配置，以释放]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[占用的资源。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1218460339}

[**[msdp]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12956_16881_1190579733}

[**[undo msdp]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_12956_16881_1198603926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_185858712}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1767443409}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1916162643}

[[系统视图]{style="font-family:宋体"}]{#struct_0_12956_16881_x307472013}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x475396053}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_119913925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1710342368}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1418809681}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x1645267870}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，表示公网实例。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_962639008}

[[只有在相应实例中先使能了]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_12956_16881_x470920686}[组播路由，本命令才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1525415188}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x307406477}[使能公网实例中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播路由，并使能公网实例中的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[、进入公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1087953565}

[\[Sysname\] multicast routing]{lang="EN-US"}

[\[Sysname-mrib\] quit]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\]]{lang="EN-US"}

[]{#_Toc293993438}[]{#_Toc94588316}[]{#_Toc80176832}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_2048524722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[multicast routing]{lang="EN-US"}**]{#struct_0_12956_16881_x846830326}[（]{style="font-family:宋体"}[IP]{lang="EN-US"}[组播命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[组播路由与转发]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-7372008 .myid}
[]{#_Toc404789815}[]{#struct_0_12956_16881_x1383132716}

**MSDP \-- MSDP配置命令 \-- originating-rp**

------------------------------------------------------------------------

[**[originating-rp]{lang="EN-US"}**]{#struct_0_12956_16881_x307996300}[命令用来将接口配置为创建]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的生成]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo originating-rp]{lang="EN-US"}**]{#struct_0_12956_16881_x890381571}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307930764}

[**[originating-rp]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12956_16881_1487729089}

[**[undo originating-rp]{lang="EN-US"}**]{#struct_0_12956_16881_1384466124}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1402888230}

[[创建]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x308127372}[报文的]{style="font-family:宋体"}[RP]{lang="EN-US"}[为实际]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_2052017835}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_1302718550}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1293666406}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1849573793}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_411291297}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_457704864}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_12956_16881_x494109913}[：指定接口类型和接口编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_1286802480}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_x308061836}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_471164186}[在公网实例中将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置为创建]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的生成]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_929463374}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] originating-rp gigabitethernet 1/0/1]{lang="EN-US"}

[]{#_Toc94588317}[]{#_Toc80176833}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_x307734156}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_665502702}[在公网实例中将接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[配置为创建]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的生成]{style="font-family:宋体"}[RP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x835922100}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] originating-rp vlan-interface 100]{lang="EN-US"}
:::

::: {#1903411553 .myid}
[]{#_Toc404789816}[]{#struct_0_12956_16881_x307668620}[]{#_Toc293993439}

**MSDP \-- MSDP配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_12956_16881_x97085830}[命令用来创建]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer**]{lang="EN-US"}]{#struct_0_12956_16881_1789615659}[命令用来删除]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x367477197}

[**[peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}*[ **connect-interface** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12956_16881_x575647352}

[**[undo peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x452441652}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1368423921}

[[没有创建]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1178029797}[对等体。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1275220349}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x307865228}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1070348527}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1120178260}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1074341733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_28884612}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_1074125811}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[**[connect-interface]{lang="EN-US"}**[ *interface-type interface-number*]{lang="EN-US"}]{#struct_0_12956_16881_x1489923398}[：指定接口类型和接口编号，本地路由器以该接口的主地址为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[与远端]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2083040955}

[[在执行其它]{style="font-family:宋体"}**[peer]{lang="EN-US"}**]{#struct_0_12956_16881_2015566840}[命令之前必须先执行本命令，否则系统将提示该]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体不存在。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307799692}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_x1689187583}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1363923602}[在公网实例中把使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的路由器配置成为本地路由器的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体，接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为本地连接端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_572149988}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 connect-interface gigabitethernet 1/0/1]{lang="EN-US"}

[]{#_Toc94588318}[]{#_Toc80176834}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_885996746}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_177934218}[在公网实例中把使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的路由器配置成为本地交换机的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体，接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[为本地连接端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_271326807}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 connect-interface vlan-interface 100]{lang="EN-US"}
:::

::: {#-1234819269 .myid}
[]{#_Toc404789817}[]{#struct_0_12956_16881_x307472012}[]{#_Toc293993440}

**MSDP \-- MSDP配置命令 \-- peer description**

------------------------------------------------------------------------

[**[peer description]{lang="EN-US"}**]{#struct_0_12956_16881_x475330517}[命令用来配置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的描述信息。]{style="font-family:宋体"}

[**[undo peer description]{lang="EN-US"}**]{#struct_0_12956_16881_x635043297}[命令用来删除]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_192763458}

[**[peer ]{lang="EN-US"}***[peer-address ]{lang="EN-US"}***[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_12956_16881_x83402438}

[**[undo peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}***[ description]{lang="EN-US"}**]{#struct_0_12956_16881_1136725819}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1215246924}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x2137825357}[对等体没有描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1546003139}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x307406476}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1087888029}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1071918700}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_509690209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1344840347}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_1580605790}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_12956_16881_x830292417}[：]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，可以包含空格，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_1393347366}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x266547863}[在公网实例中为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体添加描述信息"]{style="font-family:宋体"}[CustomerA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x307996303}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 description CustomerA]{lang="EN-US"}
:::

::: {#-360119588 .myid}
[]{#_Toc404789818}[]{#struct_0_12956_16881_x890578179}[]{#_Toc293993441}[]{#_Toc94588319}[]{#_Toc80176835}

**MSDP \-- MSDP配置命令 \-- peer mesh-group**

------------------------------------------------------------------------

[**[peer mesh-group]{lang="EN-US"}**]{#struct_0_12956_16881_1490649393}[命令用来把]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体加入全连接组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer mesh-group**]{lang="EN-US"}]{#struct_0_12956_16881_1906917119}[命令用来把]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体从全连接组中删除。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1813544811}

[**[peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}***[ mesh-group]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_12956_16881_x1811794733}

[**[undo peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}***[ mesh-group]{lang="EN-US"}**]{#struct_0_12956_16881_x1679734405}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1092864165}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x307930767}[对等体不属于任何全连接组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1487794625}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_175262079}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1772496087}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1254232020}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_85221525}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1759514145}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_1365856765}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[name]{lang="EN-US"}*]{#struct_0_12956_16881_1873874540}[：全连接组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不可以包含空格，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x308127375}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_2051952299}[在公网实例中把]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体加入到全连接组"]{style="font-family:宋体"}[Group1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_186265096}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 mesh-group Group1]{lang="EN-US"}
:::

::: {#867443202 .myid}
[]{#_Toc404789819}[]{#struct_0_12956_16881_176771972}[]{#_Toc293993442}[]{#_Toc94588320}[]{#_Toc80176836}

**MSDP \-- MSDP配置命令 \-- peer minimum-ttl**

------------------------------------------------------------------------

[**[peer minimum-ttl]{lang="EN-US"}**]{#struct_0_12956_16881_x308061839}[命令用来配置封装在]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中组播数据报文的最小]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer minimum-ttl**]{lang="EN-US"}]{#struct_0_12956_16881_470574362}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1457546578}

[**[peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}*[ **minimum-ttl** *ttl-value*]{lang="EN-US"}]{#struct_0_12956_16881_1592702374}

[**[undo]{lang="EN-US"}**[ **peer** *peer-address* **minimum-ttl**]{lang="EN-US"}]{#struct_0_12956_16881_348221198}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1233314641}

[[封装在]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307734159}[报文中组播数据报文的最小]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_666092526}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1442284042}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1859150197}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x944933730}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x290415337}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x307668623}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x97151366}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[ttl-value]{lang="EN-US"}*]{#struct_0_12956_16881_x966232323}[：指定最小]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x708441642}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x307865231}[在公网实例中进行配置，使只有]{style="font-family:宋体"}[TTL]{lang="EN-US"}[值大于或等于]{style="font-family:宋体"}[10]{lang="EN-US"}[的组播数据报文才能被封装到]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中，并转发给]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[110.10.10.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1070938350}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 110.10.10.1 minimum-ttl 10]{lang="EN-US"}
:::

::: {#1865672028 .myid}
[]{#_Toc94588321}[]{#_Toc80176837}[]{#_Toc404789820}[]{#struct_0_12956_16881_1505267469}[]{#_Toc293993443}

**MSDP \-- MSDP配置命令 \-- peer password**

------------------------------------------------------------------------

[**[peer password]{lang="EN-US"}**]{#struct_0_12956_16881_652771838}[命令用来配置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer password**]{lang="EN-US"}]{#struct_0_12956_16881_x2105755101}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x140087002}

[**[peer ]{lang="EN-US"}**]{#struct_0_12956_16881_x2096838301}*[peer-address]{lang="EN-US"}*[ **password** { **cipher** \| **simple** } *password*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **peer** *peer-address* **password**]{lang="EN-US"}]{#struct_0_12956_16881_x307799695}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1689384191}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x330754392}[对等体建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时不进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x243462061}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1368250338}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_2064043701}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1452123420}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x189544673}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1623988026}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x307472015}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_12956_16881_x475264981}[：表示以密文形式设置]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_12956_16881_x592522175}[：表示以明文形式设置]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证密钥。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_12956_16881_x29213484}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证密钥内容，区分大小写。如果以密文形式设置，则为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[137]{lang="EN-US"}[个字符的字符串；如果以明文形式设置，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x57608182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参与]{style="font-family:宋体"}]{#struct_0_12956_16881_235900161}[MD5]{lang="EN-US"}[认证的两端]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体必须配置相同的认证方式和密钥，否则将由于不能通过认证而无法建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的]{style="font-family:宋体"}]{#struct_0_12956_16881_x1087593482}[MD5]{lang="EN-US"}[认证密钥，均将以密文方式保存在配置文件中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x842718193}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1940408750}[在公网实例中配置与]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[10.1.100.1]{lang="EN-US"}[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时进行]{style="font-family:宋体"}[MD5]{lang="EN-US"}[认证，并以明文方式设置密钥为]{style="font-family:宋体"}[aabbcc]{lang="EN-US"}[（在对端也要进行类似配置）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x307406479}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 10.1.100.1 password simple aabbcc]{lang="EN-US"}
:::

::: {#386481696 .myid}
[]{#_Toc404789821}[]{#struct_0_12956_16881_1087036061}[]{#_Toc293993444}

**MSDP \-- MSDP配置命令 \-- peer request-sa-enable**

------------------------------------------------------------------------

[**[peer request-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x307930766}[命令用来使能发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文，即当路由器收到新的组加入报文时，向其]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[**[undo peer request-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x308127374}[命令用来禁止发送]{style="font-family:
宋体"}[SA]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_2051886763}

[**[peer]{lang="EN-US"}**[ *peer-address* **request-sa-enable**]{lang="EN-US"}]{#struct_0_12956_16881_x954049556}

[**[undo peer]{lang="EN-US"}**[ *peer-address* **request-sa-enable**]{lang="EN-US"}]{#struct_0_12956_16881_1738809821}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_396379217}

[[路由器收到新的组加入报文时，不向其]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x307734158}[对等体发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文，而是等待下一周期]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的到来。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_666158062}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1439419009}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_497400546}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1097301455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x307668622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x97216902}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_1673652359}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1016914441}

[[在使能发送]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_x307799694}[请求报文功能之前，必须首先关闭]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文缓存机制，否则设备不会向外发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1689318655}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x307406478}[在公网实例中关闭]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文缓存机制，并配置当路由器收到新的组加入报文时，向其]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[发送]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1614318002}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] undo cache-sa-enable]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 request-sa-enable]{lang="EN-US"}

[]{#_Toc293993445}[]{#_Toc94588322}[]{#_Toc80176838}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_1219930655}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1874000893}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_x1168827069}
:::

::: {#-1199376304 .myid}
[]{#_Toc404789822}[]{#struct_0_12956_16881_124664980}

**MSDP \-- MSDP配置命令 \-- peer sa-cache-maximum**

------------------------------------------------------------------------

[**[peer sa-cache-maximum]{lang="EN-US"}**]{#struct_0_12956_16881_1094475015}[命令用来配置可缓存从指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体学到的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的最大数量。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer sa-cache-maximum**]{lang="EN-US"}]{#struct_0_12956_16881_x865159687}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x354553732}

[**[peer ]{lang="EN-US"}***[peer-address ]{lang="EN-US"}***[sa-cache-maximum]{lang="EN-US"}**[ *sa-limit*]{lang="EN-US"}]{#struct_0_12956_16881_x791636840}

[**[undo peer ]{lang="EN-US"}***[peer-address ]{lang="EN-US"}***[sa-cache-maximum]{lang="EN-US"}**]{#struct_0_12956_16881_x1213460576}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1614383538}

[[可缓存从任一]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_53389171}[对等体学到的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的最大数量为]{style="font-family:
宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x88627454}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_138876592}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x903561702}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1560372702}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_473251108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1666747287}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_1614186930}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[sa-limit]{lang="EN-US"}*]{#struct_0_12956_16881_x1480593860}[：指定可缓存的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项的最大数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_1735890502}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x405400558}[在公网实例中配置最多可缓存]{style="font-family:宋体"}[100]{lang="EN-US"}[条从]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[学到的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x1084821147}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 sa-cache-maximum 100]{lang="EN-US"}

[]{#_Toc293993446}[]{#_Toc94588323}[]{#_Toc80176839}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_1481573175}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp brief]{lang="EN-US"}**]{#struct_0_12956_16881_1737359919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_x1769912967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp sa-count]{lang="EN-US"}**]{#struct_0_12956_16881_960098947}
:::

::: {#-1714517911 .myid}
[]{#_Toc404789823}[]{#struct_0_12956_16881_1614252466}

**MSDP \-- MSDP配置命令 \-- peer sa-policy**

------------------------------------------------------------------------

[**[peer sa-policy]{lang="EN-US"}**]{#struct_0_12956_16881_474487858}[命令用来配置接收或转发]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的过滤规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer sa-policy**]{lang="EN-US"}]{#struct_0_12956_16881_1614580146}[命令用来删除接收或转发]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文的过滤规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1114176387}

[**[peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}***[ sa-policy]{lang="EN-US"}**[ { **export** \| **import** } \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_12956_16881_849782189}

[**[undo peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}***[ sa-policy]{lang="EN-US"}**[ { **export** \| **import** }]{lang="EN-US"}]{#struct_0_12956_16881_1614645682}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_853697211}

[[不对接收或转发的]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_1614449074}[报文进行过滤，即接收或转发所有]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1497877284}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x1114904431}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1614514610}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x723200276}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x796458832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1579450703}

[**[import]{lang="EN-US"}**]{#struct_0_12956_16881_1614842290}[：表示对来自指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文进行过滤。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_12956_16881_1614907826}[：表示对转发给指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文进行过滤。]{style="font-family:宋体"}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_2065266842}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_12956_16881_1614318003}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。如果指定了本参数，则对]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文进行过滤；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则过滤掉所有]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_1219996191}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="DA"}]{#struct_0_12956_16881_1990917625}[规则中的]{lang="EN-US" style="font-family:
宋体"}**[source]{lang="DA"}**[参数用来]{lang="EN-US" style="font-family:宋体"}[指定]{style="font-family:宋体"}[组播]{lang="EN-US" style="font-family:宋体"}[源的]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}[范围]{style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="DA"}**[参数用来指定]{lang="EN-US" style="font-family:宋体"}[组播组]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[地址]{lang="EN-US" style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:
宋体"}[，]{lang="EN-US" style="font-family:宋体"}[若指定了]{lang="EN-US" style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[而除]{lang="EN-US" style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{lang="EN-US" style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[除了可以使用本命令控制]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_1614383539}[报文的接收和转发，还可以使用]{lang="EN-US" style="font-family:宋体"}**[import-source]{lang="EN-US"}**[命令控制]{lang="EN-US" style="font-family:宋体"}[SA]{lang="EN-US"}[报文的创建。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_53323635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_1614186931}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1480659396}[在公网实例中配置向]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[只转发通过]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3100]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1614252467}

[\[Sysname\] acl advanced 3100]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3100\] rule permit ip source 170.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3100\] quit]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 connect-interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 sa-policy export acl 3100]{lang="EN-US"}

[]{#_Toc94588324}[]{#_Toc80176840}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_474553394}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_1614580147}[在公网实例中配置向]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[只转发通过]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3100]{lang="EN-US"}[过滤的]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x1114241923}

[\[Sysname\] acl advanced 3100]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3100\] rule permit ip source 170.15.0.0 0.0.255.255 destination 225.1.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3100\] quit]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 connect-interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-msdp\] peer 125.10.7.6 sa-policy export acl 3100]{lang="EN-US"}

[]{#_Toc293993447}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_942297734}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_x850010566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-source]{lang="EN-US"}**]{#struct_0_12956_16881_1614645683}
:::

::: {#2096568546 .myid}
[]{#_Toc404789824}[]{#struct_0_12956_16881_853631675}

**MSDP \-- MSDP配置命令 \-- peer sa-request-policy**

------------------------------------------------------------------------

[**[peer sa-request-policy]{lang="EN-US"}**]{#struct_0_12956_16881_1614449075}[命令用来配置]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文的过滤规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **peer sa-request-policy**]{lang="EN-US"}]{#struct_0_12956_16881_1614514611}[命令用来删除]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文的过滤规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x723134740}

[**[peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}*[ **sa-request-policy** \[ **acl** *acl-number* \]]{lang="EN-US"}]{#struct_0_12956_16881_x411619740}

[**[undo peer ]{lang="EN-US"}***[peer-address]{lang="EN-US"}*[ **sa-request-policy**]{lang="EN-US"}]{#struct_0_12956_16881_456327968}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1926762197}

[[不对]{style="font-family:宋体"}[SA]{lang="EN-US"}]{#struct_0_12956_16881_1614842291}[请求报文进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x670688529}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_676879846}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1737912219}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1981097785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x302878796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_1614907827}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_2065201306}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_12956_16881_1614318000}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。如果指定了本参数，则对]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文进行过滤；如果未指定本参数、指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在或]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中未配置有效规则，则过滤掉所有]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_1991179769}

[[ACL]{lang="DA"}]{#struct_0_12956_16881_x1424474339}[规则中的]{style="font-family:宋体"}**[source]{lang="DA"}**[参数用来指定组播组的地址范围]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若指定了]{style="font-family:宋体"}**[vpn-instance]{lang="DA"}**[参数则此规则不生效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[而除]{style="font-family:宋体"}**[fragment]{lang="DA"}**[和]{style="font-family:宋体"}**[time-range]{lang="DA"}**[以外的其它可选参数都将被忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_1220061727}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_1614186928}[在公网实例中配置]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文的过滤规则：在来自]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[175.58.6.5]{lang="EN-US"}[的]{style="font-family:宋体"}[SA]{lang="EN-US"}[请求报文中，除了来自组地址范围]{style="font-family:宋体"}[225.1.1.0/24]{lang="EN-US"}[的被接收外，其它的均被忽略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x1481118147}

[\[Sysname\] acl basic 2001]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] rule permit source 225.1.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2001\] quit]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 175.58.6.5 sa-request-policy acl 2001]{lang="EN-US"}
:::

::: {#-1888544168 .myid}
[]{#_Toc404789825}[]{#struct_0_12956_16881_x1604106231}[]{#_Toc293993448}[]{#_Toc94588325}[]{#_Toc80176842}

**MSDP \-- MSDP配置命令 \-- reset msdp peer**

------------------------------------------------------------------------

[**[reset msdp peer]{lang="EN-US"}**]{#struct_0_12956_16881_x198224356}[命令用来重置与]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，并清除]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的所有统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_200538090}

[**[reset msdp]{lang="EN-US"}**[ \[ **vpn-instance** *vpn-instance-name* \] **peer** \[ *peer-address* \]]{lang="EN-US"}]{#struct_0_12956_16881_1180636870}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1430413407}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12956_16881_1614252464}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_474618930}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_580536292}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_523905493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x625659476}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x374858993}[：重置指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将重置公网实例的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_549740082}[：重置与指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，将重置与所有]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_1845839919}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x75342784}[重置公网实例中与]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，并清除该]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的所有统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset msdp peer 125.10.7.6]{lang="EN-US"}]{#struct_0_12956_16881_1614580144}
:::

::: {#1856728320 .myid}
[]{#_Toc404789826}[]{#struct_0_12956_16881_x1114307459}[]{#_Toc293993449}[]{#_Toc94588326}[]{#_Toc80176843}

**MSDP \-- MSDP配置命令 \-- reset msdp sa-cache**

------------------------------------------------------------------------

[**[reset msdp sa-cache]{lang="EN-US"}**]{#struct_0_12956_16881_x1007501147}[命令用来清除]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x126861082}

[**[reset msdp ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[sa-cache ]{lang="EN-US"}**[\[ *group-address* \]]{lang="EN-US"}]{#struct_0_12956_16881_x1804503425}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_1643238968}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12956_16881_298445041}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x707957898}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1516523422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_1614645680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_853566139}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_920107485}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。]{style="font-family:宋体"}

[*[group-address]{lang="EN-US"}*]{#struct_0_12956_16881_886772705}[：从]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中清除指定组播组所对应的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项，取值范围为]{style="font-family:宋体"}[224.0.1.0]{lang="EN-US"}[～]{style="font-family:宋体"}[239.255.255.255]{lang="EN-US"}[。如果未指定本参数，将从]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中清除所有的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1683448438}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1264827028}[清除公网实例]{style="font-family:宋体"}[SA]{lang="EN-US"}[缓存中组播组]{style="font-family:宋体"}[225.5.4.3]{lang="EN-US"}[所对应的（]{style="font-family:宋体"}[S]{lang="EN-US"}[，]{style="font-family:宋体"}[G]{lang="EN-US"}[）表项。]{style="font-family:
宋体"}

[[\<Sysname\> reset msdp sa-cache 225.5.4.3]{lang="FR"}]{#struct_0_12956_16881_768314626}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x876656892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cache-sa-enable]{lang="EN-US"}**]{#struct_0_12956_16881_x1127760278}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[display msdp sa-cache]{lang="EN-US"}**]{#struct_0_12956_16881_1614449072}
:::

::: {#-313424371 .myid}
[]{#_Toc404789827}[]{#struct_0_12956_16881_x1498008356}[]{#_Toc293993450}[]{#_Toc94588327}[]{#_Toc80176844}

**MSDP \-- MSDP配置命令 \-- reset msdp statistics**

------------------------------------------------------------------------

[**[reset msdp statistics]{lang="EN-US"}**]{#struct_0_12956_16881_x312248282}[命令用来在不重置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的情况下，清除]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_1421113035}

[**[reset msdp ]{lang="EN-US"}**[\[ **vpn-instance** *vpn-instance-name* \] ]{lang="EN-US"}**[statistics]{lang="EN-US"}**[ \[ *peer-address* \]]{lang="EN-US"}]{#struct_0_12956_16881_x734228079}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_726238915}

[[用户视图]{style="font-family:宋体"}]{#struct_0_12956_16881_x871495251}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1193762899}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1457811215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_1614514608}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x722675987}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_12956_16881_x2841648}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例的信息，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除公网实例的信息。]{style="font-family:宋体"}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x1361299306}[：清除指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的统计信息。如果未指定本参数，将清除所有]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1280593702}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x669355829}[清除公网实例]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset msdp statistics 125.10.7.6]{lang="EN-US"}]{#struct_0_12956_16881_x1635162105}
:::

::: {#972175597 .myid}
[]{#_Toc80176845}[]{#_Toc404789828}[]{#struct_0_12956_16881_1073812074}[]{#_Toc293993451}[]{#_Toc94588328}[]{#_Toc80176841}[]{#_Toc60064474}[]{#_Toc60649436}[]{#_Toc76003070}[]{#_Toc76444995}[]{#_Toc60064475}[]{#_Toc60649437}[]{#_Toc76003071}[]{#_Toc76444996}[]{#_Toc60064477}[]{#_Toc60649439}[]{#_Toc76003073}[]{#_Toc76444998}[]{#_Toc60064478}[]{#_Toc60649440}[]{#_Toc76003074}[]{#_Toc76444999}[]{#_Toc60064479}[]{#_Toc60649441}[]{#_Toc76003075}[]{#_Toc76445000}[]{#_Toc60064480}[]{#_Toc60649442}[]{#_Toc76003076}[]{#_Toc76445001}[]{#_Toc60064481}[]{#_Toc60649443}[]{#_Toc76003077}[]{#_Toc76445002}[]{#_Toc60064482}[]{#_Toc60649444}[]{#_Toc76003078}[]{#_Toc76445003}[]{#_Toc60064483}[]{#_Toc60649445}[]{#_Toc76003079}[]{#_Toc76445004}[]{#_Toc60064484}[]{#_Toc60649446}[]{#_Toc76003080}[]{#_Toc76445005}[]{#_Toc60064485}[]{#_Toc60649447}[]{#_Toc76003081}[]{#_Toc76445006}[]{#_Toc60064486}[]{#_Toc60649448}[]{#_Toc76003082}[]{#_Toc76445007}[]{#_Toc60064487}[]{#_Toc60649449}[]{#_Toc76003083}[]{#_Toc76445008}[]{#_Toc60064488}[]{#_Toc60649450}[]{#_Toc76003084}[]{#_Toc76445009}

**MSDP \-- MSDP配置命令 \-- shutdown (MSDP view)**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_12956_16881_2123832634}[命令用来关闭]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_12956_16881_1614842288}[命令用来打开]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x671147282}

[**[shutdown]{lang="EN-US"}**[ *peer-address*]{lang="EN-US"}]{#struct_0_12956_16881_1417955578}

[**[undo shutdown]{lang="EN-US"}**[ *peer-address*]{lang="EN-US"}]{#struct_0_12956_16881_x1440128558}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_362565624}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x709213587}[对等体的连接处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x541557732}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x4470232}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1249754610}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1614907824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_2065135770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x511341078}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x1673503303}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_993762499}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x778215412}[在公网实例中关闭]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体]{style="font-family:宋体"}[125.10.7.6]{lang="EN-US"}[的连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x499490898}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] shutdown 125.10.7.6]{lang="EN-US"}

[]{#_Toc293993452}[]{#_Toc94588329}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1866717652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp brief]{lang="EN-US"}**]{#struct_0_12956_16881_1614318001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_1220127263}
:::

::: {#-177703868 .myid}
[]{#_Toc404789829}[]{#struct_0_12956_16881_217366312}

**MSDP \-- MSDP配置命令 \-- static-rpf-peer**

------------------------------------------------------------------------

[**[static-rpf-peer]{lang="EN-US"}**]{#struct_0_12956_16881_1136303457}[命令用来配置静态]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[undo static-rpf-peer]{lang="EN-US"}**]{#struct_0_12956_16881_268536278}[命令用来删除静态]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_555516191}

[**[static-rpf-peer]{lang="EN-US"}**[ *peer-address* \[ **rp-policy** *ip-prefix-name* \]]{lang="EN-US"}]{#struct_0_12956_16881_x1273913519}

[**[undo static-rpf-peer]{lang="EN-US"}**[ *peer-address*]{lang="EN-US"}]{#struct_0_12956_16881_x1829488944}

[[【]{style="font-family:黑体"}]{#struct_0_12956_16881_x1898509467}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[不存在任何静态]{style="font-family:宋体"}[RPF]{lang="EN-US"}]{#struct_0_12956_16881_1614383537}[对等体。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_53716851}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_1834910365}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x825289738}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_x1397482970}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_946712584}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x2104117056}

[*[peer-address]{lang="EN-US"}*]{#struct_0_12956_16881_x2031887171}[：指定]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体的地址。]{style="font-family:宋体"}

[**[rp-policy]{lang="EN-US"}**[ *ip-prefix-name*]{lang="EN-US"}]{#struct_0_12956_16881_1614186929}[：指定基于]{style="font-family:宋体"}[SA]{lang="EN-US"}[报文中]{style="font-family:宋体"}[RP]{lang="EN-US"}[地址的过滤策略。]{style="font-family:宋体"}*[ip-prefix-name]{lang="EN-US"}*[表示过滤策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1498073892}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_1854252186}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x1896137707}[在公网实例中将]{style="font-family:宋体"}[130.10.7.6]{lang="EN-US"}[配置为静态]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体，源]{style="font-family:宋体"}[RP]{lang="EN-US"}[的地址范围为]{style="font-family:宋体"}[130.10.0.0/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_641169960}

[\[Sysname\] ip prefix-list list1 permit 130.10.0.0 16 great-equal 16 less-equal 32]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 130.10.7.6 connect-interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-msdp\] static-rpf-peer 130.10.7.6 rp-policy list1]{lang="EN-US"}

[]{#_Toc94588330}[]{#_Toc80176846}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[交换应用：]{lang="EN-US" style="font-family:宋体"}]{#struct_0_12956_16881_x1516235081}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_x433365232}[在公网实例中将]{style="font-family:宋体"}[130.10.7.6]{lang="EN-US"}[配置为静态]{style="font-family:宋体"}[RPF]{lang="EN-US"}[对等体，源]{style="font-family:宋体"}[RP]{lang="EN-US"}[的地址范围为]{style="font-family:宋体"}[130.10.0.0/16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_1614514609}

[\[Sysname\] ip prefix-list list1 permit 130.10.0.0 16 great-equal 16 less-equal 32]{lang="EN-US"}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] peer 130.10.7.6 connect-interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-msdp\] static-rpf-peer 130.10.7.6 rp-policy list1]{lang="EN-US"}

[]{#_Toc293993453}[[【]{style="font-family:黑体"}]{#struct_0_12956_16881_x722610451}[相关命令]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display msdp peer-status]{lang="EN-US"}**]{#struct_0_12956_16881_x1969094242}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip prefix-list]{lang="EN-US"}**]{#struct_0_12956_16881_x1738325237}
:::

::: {#-110412887 .myid}
[]{#_Toc404789830}[]{#struct_0_12956_16881_1086439045}[]{#_Toc362965363}[]{#_Toc362951750}

**MSDP \-- MSDP配置命令 \-- timer keepalive**

------------------------------------------------------------------------

[**[timer keepalive]{lang="EN-US"}**]{#struct_0_12956_16881_883771053}[命令用来配置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体会话的]{style="font-family:宋体"}[保活时间和保持时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo timer keepalive]{lang="EN-US"}**]{#struct_0_12956_16881_x539021666}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x940151535}

[**[timer]{lang="EN-US"}**[ **keepalive** *keepalive* *holdtime*]{lang="EN-US"}]{#struct_0_12956_16881_x821394075}

[**[undo timer keepalive]{lang="EN-US"}**]{#struct_0_12956_16881_x1850462574}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_1655300079}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_1086242437}[会话的保活时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒，保持时间为]{style="font-family:宋体"}[75]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1890087301}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_190539749}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_1439465943}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_811715980}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_1278824202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1177287061}

[*[keepalive]{lang="EN-US"}*]{#struct_0_12956_16881_355067689}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[保活时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[21845]{lang="EN-US"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[*[holdtime]{lang="EN-US"}*]{#struct_0_12956_16881_1086307973}[：]{style="font-family:宋体"}[表示保持]{style="font-family:宋体"}[时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1077029531}

[[当]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_969701363}[对等体之间建立会话后，会定时互发]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文（其发送间隔被称为保活时间），以免对端认为会话已中断。如果一端在保持时间内未收到对端的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文或其它报文，便断开此会话。由于]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体之间没有保活时间和保持时间的协商机制，因此必须为两端配置相同的保活时间和保持时间，且保活时间必须小于保持时间。]{style="font-family:宋体"}

[[需要注意的是，本]{style="font-family:宋体"}]{#struct_0_12956_16881_x567797658}[命令会对已建立的]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[会话立即生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_452874662}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_2069050889}[在公网实例中配置]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体会话的]{style="font-family:宋体"}[保活时间和保持时间分别]{style="font-family:宋体"}[为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒和]{style="font-family:宋体"}[180]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_12956_16881_1086111365}

[\[Sysname\] msdp]{lang="DA"}

[\[Sysname-msdp\] timer keepalive 60 180]{lang="DA"}
:::

::: {#-1521287974 .myid}
[]{#_Toc404789831}[]{#struct_0_12956_16881_718183621}

**MSDP \-- MSDP配置命令 \-- timer retry**

------------------------------------------------------------------------

[**[timer retry]{lang="EN-US"}**]{#struct_0_12956_16881_x167819223}[命令用来配置建立]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接的重试周期。]{style="font-family:宋体"}

[**[undo timer retry]{lang="EN-US"}**]{#struct_0_12956_16881_1969156493}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_12956_16881_x497021112}

[**[timer retry ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_12956_16881_x457133915}

[**[undo timer retry]{lang="EN-US"}**]{#struct_0_12956_16881_1614842289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_12956_16881_x671212818}

[[建立]{style="font-family:宋体"}[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_x100734189}[对等体连接的重试周期为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_12956_16881_x388578311}

[[MSDP]{lang="EN-US"}]{#struct_0_12956_16881_360685556}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_12956_16881_x594779904}

[[network-admin]{lang="EN-US"}]{#struct_0_12956_16881_1084099796}

[[mdc-admin]{lang="EN-US"}]{#struct_0_12956_16881_x971421908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_12956_16881_x1315861020}

[*[interval]{lang="EN-US"}*]{#struct_0_12956_16881_1614907825}[：表示重试周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_12956_16881_2065070234}

[[\# ]{lang="EN-US"}]{#struct_0_12956_16881_294209358}[在公网实例中配置建立]{style="font-family:宋体"}[MSDP]{lang="EN-US"}[对等体连接的重试周期为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_12956_16881_x1693269326}

[\[Sysname\] msdp]{lang="EN-US"}

[\[Sysname-msdp\] timer retry 60]{lang="EN-US"}
:::
