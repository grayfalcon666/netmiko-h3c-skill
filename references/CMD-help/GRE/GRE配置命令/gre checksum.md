::: {#1748490644 .myid}
[]{#_Toc404787174}[]{#struct_0_x1894_x1442_x1303864653}[]{#_Toc263339110}

**GRE \-- GRE配置命令 \-- gre checksum**

------------------------------------------------------------------------

[**[gre checksum]{lang="EN-US"}**]{#struct_0_x1894_x1442_1340289272}[命令用来开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}[报文校验和功能。]{style="font-family:宋体"}

[**[undo gre checksum]{lang="EN-US"}**]{#struct_0_x1894_x1442_1222991244}[命令用来关闭]{style="font-family:宋体"}[GRE]{lang="EN-US"}[报文校验和功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1905547432}

[**[gre checksum]{lang="EN-US"}**]{#struct_0_x1894_x1442_x133052143}

[**[undo gre checksum]{lang="EN-US"}**]{#struct_0_x1894_x1442_127388385}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_1999677597}

[[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_x732514491}[报文校验和功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_1304236046}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1894_x1442_789581158}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_830196620}

[[network-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_1432365008}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_x297218505}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_1296072875}

[[通过]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_1275162492}[校验和验证可以检查报文的完整性。]{style="font-family:宋体"}

[[隧道两端可以根据各自的实际应用需要决定是否要开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_x1283580393}[报文校验和功能。如果发送方开启了]{style="font-family:宋体"}[GRE]{lang="EN-US"}[报文校验和功能，则会根据]{style="font-family:宋体"}[GRE]{lang="EN-US"}[头及]{style="font-family:宋体"}[Payload]{lang="EN-US"}[信息计算校验和，并将包含校验和信息的报文发送给对端。接收方对收到的报文计算校验和，并与报文中的校验和比较，如果一致则对报文进行进一步处理，否则丢弃该报文。]{style="font-family:宋体"}

[[需要注意的是，接收方是否对收到的报文进行校验和验证，取决于报文中是否携带校验和信息，与接收方的配置无关。]{style="font-family:宋体"}]{#struct_0_x1894_x1442_1448906482}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x732580027}

[[\# ]{lang="EN-US"}]{#struct_0_x1894_x1442_123200117}[开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}[报文校验和功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1894_x1442_207855749}

[\[Sysname\] interface tunnel 2 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel2\] gre checksum]{lang="EN-US"}
:::

::: {#127380674 .myid}
[]{#_Toc404787175}[]{#struct_0_x1894_x1442_1298165671}[]{#_Toc263339111}[]{#_Toc167869181}[]{#_Toc167869182}[]{#_Toc167869183}[]{#_Toc167869184}[]{#_Toc167869185}[]{#_Toc167869186}[]{#_Toc167869187}[]{#_Toc167869188}[]{#_Toc167869189}[]{#_Toc167869190}[]{#_Toc167869191}[]{#_Toc167869192}[]{#_Toc167869193}[]{#_Toc167869194}[]{#_Toc167869195}[]{#_Toc167869196}[]{#_Toc167869197}[]{#_Toc167869198}[]{#_Toc167869200}[]{#_Toc167869201}

**GRE \-- GRE配置命令 \-- gre key**

------------------------------------------------------------------------

[**[gre key]{lang="EN-US"}**]{#struct_0_x1894_x1442_x1278232990}[命令用来设置]{style="font-family:宋体"}[GRE]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo gre key]{lang="EN-US"}**]{#struct_0_x1894_x1442_867000608}[命令用来取消]{style="font-family:宋体"}[GRE]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1326380487}

[**[gre key]{lang="EN-US"}**[ *key-number*]{lang="EN-US"}]{#struct_0_x1894_x1442_x9641889}

[**[undo gre key]{lang="EN-US"}**]{#struct_0_x1894_x1442_x796877396}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x732121275}

[[没有设置]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_2050387313}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_210364335}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1894_x1442_x870145259}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x385785910}

[[network-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_x149976043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_1661228557}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x197349574}

[*[key-number]{lang="EN-US"}*]{#struct_0_x1894_x1442_x1507062696}[：]{style="font-family:宋体"}[GRE]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1801999453}

[[通过设置]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_x732186811}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[，可以防止设备接收非法报文。]{style="font-family:宋体"}

[[配置了]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}]{#struct_0_x1894_x1442_1726150872}[后，发送方会在其发送的报文中携带]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[信息。接收方收到报文后将报文中的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[与接收方本地配置的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[进行比较，如果一致则对报文进行进一步处理；否则丢弃该报文。]{style="font-family:宋体"}

[[隧道两端必须设置相同的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}]{#struct_0_x1894_x1442_2090152901}[，或者都不设置]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1346346347}

[[\# ]{lang="EN-US"}]{#struct_0_x1894_x1442_1328095644}[设置]{style="font-family:宋体"}[GRE]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{style="font-family:宋体"}[GRE Key]{lang="EN-US"}[为]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1894_x1442_x544418285}

[\[Sysname\] interface tunnel 2 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel2\] gre key 123]{lang="EN-US"}
:::

::: {#809257258 .myid}
[]{#_Toc404787176}[]{#struct_0_x1894_x1442_x1102596563}[]{#_Toc263339115}[]{#_Toc167869203}[]{#_Toc167869204}[]{#_Toc167869206}[]{#_Toc167869207}[]{#_Toc167869208}[]{#_Toc167869209}[]{#_Toc167869210}[]{#_Toc167869211}[]{#_Toc167869212}[]{#_Hlt19451604}[]{#_Toc167869213}[]{#_Toc167869214}[]{#_Toc167869215}[]{#_Toc167869216}[]{#_Toc167869217}[]{#_Toc167869218}[]{#_Toc167869219}[]{#_Toc167869220}[]{#_Toc167869221}[]{#_Toc167869223}[]{#_Toc167869224}[]{#_Toc167869225}[]{#_Toc167869226}[]{#_Toc248810082}[]{#_Toc248810083}[]{#_Toc248810084}[]{#_Toc248810085}

**GRE \-- GRE配置命令 \-- keepalive**

------------------------------------------------------------------------

[**[keepalive]{lang="EN-US"}**]{#struct_0_x1894_x1442_783907263}[命令用来开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能，并配置]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送周期及最大发送次数。]{style="font-family:宋体"}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_x1894_x1442_x732645566}[命令用来关闭]{style="font-family:宋体"}[GRE]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_912169935}

[**[keepalive ]{lang="EN-US"}**[\[ *interval* \[ *times* \] \]]{lang="EN-US"}]{#struct_0_x1894_x1442_852650676}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_x1894_x1442_1800037355}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_1505395134}

[[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_x1322095856}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x2004592587}

[[Tunnel]{lang="EN-US"}]{#struct_0_x1894_x1442_763545122}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x971340269}

[[network-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_1356530212}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1894_x1442_x732711102}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x290755046}

[*[interval]{lang="EN-US"}*]{#struct_0_x1894_x1442_x1539341291}[：]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[*[times]{lang="EN-US"}*]{#struct_0_x1894_x1442_2020546988}[：]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的最大传送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1189396924}

[[开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_x960351283}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能后，设备会以]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[为周期从]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口发送]{style="font-family:宋体"}[GRE]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文。如果连续发送]{style="font-family:宋体"}*[times]{lang="EN-US"}*[个]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，仍然没有收到隧道对端的回应，则把本端]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的状态置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。如果]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口为]{style="font-family:宋体"}[down]{lang="EN-US"}[状态时，收到对端回复的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[确认报文，则]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的状态将转换为]{style="font-family:宋体"}[up]{lang="EN-US"}[，否则保持]{style="font-family:宋体"}[down]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[需要注意的是，不论设备上是否开启了]{style="font-family:宋体"}[GRE]{lang="EN-US"}]{#struct_0_x1894_x1442_1235326342}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能，设备接收到]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文后，都会对其进行应答。]{style="font-family:宋体"}

[[模式为]{style="font-family:宋体"}[GRE over IPv6]{lang="EN-US"}]{#struct_0_x1894_x1442_582708022}[隧道的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口不支持本命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1894_x1442_x1461900284}

[[\# ]{lang="EN-US"}]{#struct_0_x1894_x1442_x357760383}[开启]{style="font-family:宋体"}[GRE]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[功能，并配置]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送周期为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，最大传送次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1894_x1442_x732776638}

[\[Sysname\] interface tunnel 2 mode gre]{lang="EN-US"}

[\[Sysname-Tunnel2\] keepalive 20 5]{lang="EN-US"}
:::
