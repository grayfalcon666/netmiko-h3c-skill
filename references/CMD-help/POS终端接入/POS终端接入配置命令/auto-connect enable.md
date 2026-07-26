::: {#-770730439 .myid}
[]{#_Toc404785976}[]{#struct_0_x1991_x1755_338310643}

**POS终端接入 \-- POS终端接入配置命令 \-- auto-connect enable**

------------------------------------------------------------------------

[**[auto-connect enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_337401866}[命令用来开启自动建立连接功能，即]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入设备自动为长连接模式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板建立与前置机之间的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[undo auto-connect]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1991_x1755_115378087}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1227773298}

[**[auto-connect enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_2074374411}

[**[undo auto-connect enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x772539826}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x788469522}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1890511698}[应用模板自动建立连接功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1839441736}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x37984823}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1776049708}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_469310355}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1532500620}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1419131918}

[[只有长连接模式的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1030108762}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板才支持该配置，配置后]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板会立即向前置机发起连接，该连接建立后只能用于非透传模式下的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[长连接复用。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_788649337}[应用模板的连接模式由短连接修改为长连接时，]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入设备会立即向前置机发起连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x972691354}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_476679721}[开启长连接模式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的自动建立连接功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1089564523}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] auto-connect enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x891401927}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa server enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2004635252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer auto-connect]{lang="EN-US"}**]{#struct_0_x1991_x1755_x58087792}
:::

::: {#-1248280115 .myid}
[]{#_Toc305860298}[]{#_Toc404785977}[]{#struct_0_x1991_x1755_x1876667346}[]{#_Toc358227428}[]{#_Toc336625607}

**POS终端接入 \-- POS终端接入配置命令 \-- backup app**

------------------------------------------------------------------------

[**[backup app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x20133299}[命令用来配置备份]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[**[undo backup app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x636680236}[用来取消备份]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1209918163}

[**[backup app ]{lang="EN-US"}***[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x732448955}

[**[undo backup app]{lang="EN-US"}**]{#struct_0_x1991_x1755_1263175535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1303864653}

[[未配置备份]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1340289272}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1222991244}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1905547432}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x133052143}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_127388385}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1999677597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1113771277}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x732514491}[：备份应用]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1304236046}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_789581158}[交易时，若某]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机不可达，则向其备份]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机发起连接。仅]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板支持备份]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[若指定的]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x1991_x1755_830196620}[不存在或者]{style="font-family:宋体"}[APP]{lang="EN-US"}[类型不是]{style="font-family:宋体"}[TCP]{lang="EN-US"}[，则允许配置成功，但不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1432365008}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x297218505}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1296072875}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1275162492}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[2]{lang="EN-US"}[，配置其备份应用服务器为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x732580027}

[\[Sysname\] posa app 2 type tcp]{lang="EN-US"}

[\[Sysname-posa-app2\] backup app 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_123200117}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer quiet]{lang="EN-US"}**]{#struct_0_x1991_x1755_207855749}
:::

::: {#2122706439 .myid}
[]{#_Toc404785978}[]{#struct_0_x1991_x1755_1298165671}[]{#_Toc358227429}[]{#_Toc336625596}

**POS终端接入 \-- POS终端接入配置命令 \-- caller-number enable**

------------------------------------------------------------------------

[**[caller-number enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1278232990}[命令用来使能主叫号码发送功能，即在进行]{style="font-family:宋体"}[POS]{lang="EN-US"}[交易时向前置机发送]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的主叫号码。]{style="font-family:宋体"}

[**[undo caller-number enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_867000608}[命令用来关闭主叫号码发送功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1326380487}

[**[caller-number enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x9641889}

[**[undo caller-number enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x796877396}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x732121275}

[[主叫号码发送功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_2050387313}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_210364335}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x870145259}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x385785910}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x149976043}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1661228557}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x197349574}

[[该功能对于]{style="font-family:宋体"}[FCM POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1507062696}[机和]{style="font-family:宋体"}[AM POS]{lang="EN-US"}[机有效，只有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板才支持此配置。]{style="font-family:宋体"}

[[当配置此功能后，设备向前置机转发]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x732186811}[机报文时会发送]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的主叫号码（]{style="font-family:宋体"}[FCM POS]{lang="EN-US"}[机接入与]{style="font-family:宋体"}[AM POS]{lang="EN-US"}[机接入两种方式下发送主叫号码的格式不同）。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[AM POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1726150872}[机接入方式，需要将应用模板配置为短连接模式，此功能才能生效。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[FCM POS]{lang="EN-US"}]{#struct_0_x1991_x1755_2090152901}[机接入方式，需要将应用模板配置为非透传模式，此功能才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1346346347}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1328095644}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，使能主叫号码发送功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x544418285}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] mode temporary]{lang="EN-US"}

[\[Sysname-posa-app1\] caller-number enable]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404785979}[]{#struct_0_x1991_x1755_x1102596563}[]{#_Toc358227430}[]{#_Toc336625597}[]{#_Toc275956209}

**POS终端接入 \-- POS终端接入配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1991_x1755_783907263}[命令用来配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1991_x1755_x732645566}[命令用来删除配置的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_912169935}

[**[description]{lang="FR"}**]{#struct_0_x1991_x1755_852650676}[ *text*]{lang="FR"}

[**[undo description]{lang="FR"}**]{#struct_0_x1991_x1755_1800037355}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1505395134}

[[没有配置]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1322095856}[应用模板的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2004592587}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_763545122}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x971340269}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x732711102}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x290755046}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1539341291}

[*[text]{lang="FR"}*]{#struct_0_x1991_x1755_2020546988}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[字符的字符串，区分大小写，合法字符是不为"？"的可打印字符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1189396924}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x960351283}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板，并配置它的描述信息为"]{style="font-family:宋体"}[ChinaBank1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1235326342}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] description ChinaBank1]{lang="EN-US"}
:::

::: {#429957819 .myid}
[]{#_Toc404785980}[]{#struct_0_x1991_x1755_x1461900284}[]{#_Toc358227431}[]{#_Toc336625617}

**POS终端接入 \-- POS终端接入配置命令 \-- display fcm statistics**

------------------------------------------------------------------------

[**[display fcm statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x732776638}[命令用来显示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1456932484}

[**[display fcm statistics]{lang="EN-US"}**[ \[ **interface** **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* } \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x2073877999}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x775538668}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1373724045}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1363081450}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1159537690}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x137169862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1006244423}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x732842174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x695940021}

[**[interface]{lang="EN-US"}**[ **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* }]{lang="EN-US"}]{#struct_0_x1991_x1755_x82303349}[：显示指定接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息。]{style="font-family:宋体"}[interface-number]{lang="EN-US"}[表示物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口编号，用来显示物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息；]{style="font-family:宋体"}[interface-number:setnumber.subnumber]{lang="EN-US"}[表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口的编号，用来显示指定通道化]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口下子接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息。如果不指定该参数，则显示所有物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口、通道化]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的子接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1081826876}

[[设备重启、以及执行]{style="font-family:宋体"}**[reset fcm statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1872666715}[命令行会删除该统计值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1411863754}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1056070065}[显示接口]{style="font-family:宋体"}[FCM2/1/0]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display fcm statistics interface fcm 2/1/0]{lang="EN-US"}]{#struct_0_x1991_x1755_672182258}

[Interface TerminalID ConnectFailed TimedOut Transactions (Total/Success)]{lang="EN-US"}

[Fcm2/1/0  5          20            30       100/20]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display fcm statistics]{lang="EN-US"}]{#struct_0_x1991_x1755_1665204368}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1758643688}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x732383422}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2087605994}

[[Interface]{lang="EN-US"}]{#struct_0_x1991_x1755_x748375501}

[[接入的接口，只能为]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_1613280059}[接口]{style="font-family:宋体"}

[[TerminalID]{lang="EN-US"}]{#struct_0_x1991_x1755_1357907307}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1080816557}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，若未绑定终端则显示为]{style="font-family:宋体"}[-]{lang="EN-US"}

[[ConnectFailed]{lang="EN-US"}]{#struct_0_x1991_x1755_448487331}

[[因拨号协商不成功的次数]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x732448958}

[[TimedOut]{lang="EN-US"}]{#struct_0_x1991_x1755_1263372143}

[[因交易超时而断开的次数，此值与]{style="font-family:宋体"}[Success]{lang="EN-US"}]{#struct_0_x1991_x1755_x1665385183}[的统计不互斥，交易了多个报文但总交易时间超时的交易，既统计为]{style="font-family:宋体"}[TimeOut]{lang="EN-US"}[又统计为]{style="font-family:宋体"}[Success]{lang="EN-US"}

[[Transactions]{lang="EN-US"}]{#struct_0_x1991_x1755_961961259}

[[该接口下]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1751369395}[交易次数，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Total]{lang="EN-US"}]{#struct_0_x1991_x1755_x71888969}[：总交易数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Success]{lang="EN-US"}]{#struct_0_x1991_x1755_x1983577242}[：该接口下成功转发了交易报文的]{style="font-family:宋体"}[POS]{lang="EN-US"}[交易次数。在]{style="font-family:宋体"}[FCM]{lang="EN-US"}[交易过程中，]{style="font-family:宋体"}[POS]{lang="EN-US"}[机拨号后只要成功收发了交易报文，就认为本次交易成功，此统计值就加]{style="font-family:宋体"}[1]{lang="EN-US"}[。此值与]{style="font-family:宋体"}[TimedOut]{lang="EN-US"}[的统计不互斥，即交易了多个报文但总交易时间超时的交易，既统计为]{style="font-family:宋体"}[TimeOut]{lang="EN-US"}[又统计为]{style="font-family:宋体"}[Success]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1304563726}

[]{#struct_0_x1991_x1755_x365842774}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset fcm]{lang="EN-US"}**]{#_Toc193529388}

::: {#1188793636 .myid}
[]{#_Toc404785981}[]{#struct_0_x1991_x1755_x445838597}[]{#_Toc358227432}[]{#_Toc336625622}[]{#_Toc316550517}[]{#_Toc316550518}

**POS终端接入 \-- POS终端接入配置命令 \-- display posa connection terminal**

------------------------------------------------------------------------

[**[display posa connection terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1300449615}[命令用来显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_869873473}

[**[display posa connection terminal]{lang="EN-US"}**[ \[ *terminal-id* \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x783399779}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1445718940}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1867060572}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_913831874}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x732580030}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_123265652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1002777505}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_877822298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1403336719}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x578417340}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果不指定该参数，则显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端的连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x767800951}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1252318780}[显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa connection terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066281036}

[Total TCP connections : 2]{lang="EN-US"}

[Total FCM connections : 1]{lang="EN-US"}

[Total flow connections: 1]{lang="EN-US"}

[Max concurrent trades : 65535]{lang="EN-US"}

[Current non-TCP trades: 2]{lang="EN-US"}

[Current TCP trades    : 60]{lang="EN-US"}

[ ]{lang="EN-US"}

[ID  Type  Interface    SrcIP:SrcPort         DstIP:DstPort         Trades]{lang="EN-US"}

[1   TCP   -            192.168.100.100:1319  192.168.100.236:3000  10]{lang="EN-US"}

[1   TCP   -            192.168.100.100:1320  192.168.100.236:3000  20]{lang="EN-US"}

[5   TCP   -            192.168.100.200:1323  192.168.100.236:4000  30]{lang="EN-US"}

[6   FCM   Fcm10/0:0.0  -                     -                     1]{lang="EN-US"}

[7   Flow  Asy1/0       -                     -                     1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066346572}[显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa connection terminal 1]{lang="EN-US"}]{#struct_0_x1991_x1755_x732121278}

[ID  Type  Interface    SrcIP:SrcPort         DstIP:DstPort         Trades]{lang="EN-US"}

[1   TCP   -            192.168.100.100:1319  192.168.100.236:3000  10]{lang="EN-US"}

[1   TCP   -            192.168.100.100:1320  192.168.100.236:3000  20]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display posa status terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_2050583921}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1459844312}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1389083360}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x860814627}

[[Total TCP connections]{lang="EN-US"}]{#struct_0_x1991_x1755_555567657}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_258431283}[接入方式下的当前连接总数]{style="font-family:宋体"}

[[Total FCM connections]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066412108}

[[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_1581836034}[接入方式下的当前连接总数]{style="font-family:宋体"}

[[Total flow connections]{lang="EN-US"}]{#struct_0_x1991_x1755_x836935774}

[[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_208444396}[接入方式下的当前连接总数]{style="font-family:宋体"}

[[Max coucurrent trades ]{lang="EN-US"}]{#struct_0_x1991_x1755_612955864}

[[系统支持的最大并发交易数]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1107802730}

[[Current non-TCP trades]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066477644}

[[当前并发的所有非]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1695800177}[交易数]{style="font-family:宋体"}

[[Current TCP trades]{lang="EN-US"}]{#struct_0_x1991_x1755_x744865998}

[[当前并发的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x19745783}[交易数]{style="font-family:宋体"}

[[ID]{lang="EN-US"}]{#struct_0_x1991_x1755_287896630}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1346641185}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066543180}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_2107519835}[终端模板的连接类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_1145450748}[：流接入方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_x1206434994}[：]{style="font-family:宋体"}[FCM]{lang="EN-US"}[拨号接入方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x123289937}[：]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066608716}

[[接入的端口，]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_666785743}[接入方式下显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[SrcIP]{lang="EN-US"}]{#struct_0_x1991_x1755_296106088}

[[连接的源地址，非]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x732186814}[接入方式下显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[SrcPort]{lang="EN-US"}]{#struct_0_x1991_x1755_1725823192}

[[连接的源端口，非]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1402376369}[接入方式下显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[DstIP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066674252}

[[连接目的地址，非]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1842953045}[接入方式下显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[DstPort]{lang="EN-US"}]{#struct_0_x1991_x1755_x972485311}

[[连接目的端口，非]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x732645565}[接入方式下显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Trades ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1065691212}

[[链接的当前并发交易数]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x928212886}

[]{#_Toc193529380}[]{#_Toc336625618}[[ ]{lang="EN-US"}]{#_Toc194748107}

::: {#699748431 .myid}
[]{#_Toc404785982}[]{#struct_0_x1991_x1755_x1618901461}[]{#_Toc358227433}

**POS终端接入 \-- POS终端接入配置命令 \-- display posa statistics app**

------------------------------------------------------------------------

[**[display posa statistics app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x782215526}[命令用来显示]{style="font-family:
宋体"}[POS]{lang="EN-US"}[应用模板的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329151668}

[**[display posa statistics app]{lang="EN-US"}**[ \[ *app-id* \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x941525654}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x15420573}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x732711101}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x290689510}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1641549043}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x1955439455}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_567868884}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_2037415924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_492421657}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_1934964208}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。如果不指定该参数，则显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1414315640}

[[删除应用模板、设备重启、执行]{style="font-family:宋体"}**[reset posa statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x732776637}[命令会删除该统计值。]{style="font-family:宋体"}

[[对某一应用模板进行报文统计指的是该应用模板下所有应用实例接收发送的报文数目。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1456604804}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1018887344}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_946146436}[显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa statistics app]{lang="EN-US"}]{#struct_0_x1991_x1755_x732842173}

[ID  Received     Sent       PktErr      DisErr    InDiscarded    OutDiscarded]{lang="EN-US"}

[1   100          100        0           0         0              3]{lang="EN-US"}

[2   60           70         0           0         0              0]{lang="EN-US"}

[3   100          10         0           0         0              0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display posa statistics app]{lang="EN-US"}]{#struct_0_x1991_x1755_x696005557}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1463858984}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2092729102}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1465109862}

[[ID]{lang="EN-US"}]{#struct_0_x1991_x1755_1403209549}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x732383421}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Received]{lang="EN-US"}]{#struct_0_x1991_x1755_2087540458}

[[从前置机接收到的报文数目（含]{style="font-family:宋体"}[PktErr]{lang="EN-US"}]{#struct_0_x1991_x1755_x732448957}[和]{style="font-family:宋体"}[DisErr]{lang="EN-US"}[错误的报文数目，不含]{style="font-family:宋体"}[InDiscarded]{lang="EN-US"}[报文数目）]{style="font-family:宋体"}

[[Sent]{lang="EN-US"}]{#struct_0_x1991_x1755_x732514493}

[[发送给前置机的报文数目（不包含链路不通丢弃的报文数目）]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x732580029}

[[PktErr]{lang="EN-US"}]{#struct_0_x1991_x1755_122806901}

[[格式错误的报文数目]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x786412206}

[[DisErr]{lang="EN-US"}]{#struct_0_x1991_x1755_1387420595}

[[分发处理错误的报文数目，即找不到对应]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x732121277}[终端接入的报文数目]{style="font-family:宋体"}

[[InDiscarded]{lang="EN-US"}]{#struct_0_x1991_x1755_2050256241}

[[接收缓冲区满丢弃的报文数目，是指从前置机接收报文时，因接收缓冲区满而丢弃的报文数目]{style="font-family:宋体"}]{#struct_0_x1991_x1755_607476904}

[[OutDiscarded]{lang="EN-US"}]{#struct_0_x1991_x1755_1640824068}

[[链路不通丢弃的报文数目，是指应用发送报文时因链路不通丢弃报文数目]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x732186813}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1726281944}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset posa statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1402165056}

::: {#-1222988493 .myid}
[]{#_Toc404785983}[]{#struct_0_x1991_x1755_570717361}[]{#_Toc358227434}[]{#_Toc336625619}[]{#_Toc193529376}

**POS终端接入 \-- POS终端接入配置命令 \-- display posa statistics terminal**

------------------------------------------------------------------------

[**[display posa statistics terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_804691498}[命令用来查看]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1824027630}

[**[display posa statistics terminal]{lang="EN-US"}**[ \[ *terminal-id* \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x1348268725}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833438379}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1793696679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_987054491}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x758569735}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x243195225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x199118088}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_630292674}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1813516218}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x708355777}[：终端]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果不指定该参数，则显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833372843}

[[若指定的终端不存在，则无输出也不提示错误信息。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x2006068362}

[[删除终端模板、设备重启、执行]{style="font-family:宋体"}**[reset posa statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x687553134}[命令会删除该统计值。]{style="font-family:宋体"}

[[对某一终端进行报文统计指的是该终端下所有终端实例接收发送的报文数目。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1892757456}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2038664302}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1949710888}[显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa statistics terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_x216640848}

[ID  Received   Sent      PktErr    MapErr     InDiscarded   OutDiscarded  Notified]{lang="EN-US"}

[1   100        50        2         2          0             5             2]{lang="EN-US"}

[2   60         70        0         10         1             6             0]{lang="EN-US"}

[3   100        100       0         0          1             3             0]{lang="EN-US"}

[4   3          0         0         0          0             3             0]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display posa statistics terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_833307307}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1450083976}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x391601342}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x940854832}

[[ID]{lang="EN-US"}]{#struct_0_x1991_x1755_x388808857}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x63725423}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Received]{lang="EN-US"}]{#struct_0_x1991_x1755_833241771}

[[从]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833700523}[机接收到的报文数目（含]{style="font-family:宋体"}[PktErr]{lang="EN-US"}[和]{style="font-family:宋体"}[MapErr]{lang="EN-US"}[错误的报文数目，不含]{style="font-family:宋体"}[InDiscarded]{lang="EN-US"}[的报文数目）]{style="font-family:宋体"}

[[Sent]{lang="EN-US"}]{#struct_0_x1991_x1755_566028188}

[[发送给]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833634987}[应用模板的报文数目的报文数目（不包含]{style="font-family:宋体"}[OutDiscarded]{lang="EN-US"}[和]{style="font-family:宋体"}[Notified]{lang="EN-US"}[的报文数目）]{style="font-family:宋体"}

[[PktErr]{lang="EN-US"}]{#struct_0_x1991_x1755_1325489987}

[[从]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833569451}[机收到的格式错误的报文数目]{style="font-family:宋体"}

[[MapErr]{lang="EN-US"}]{#struct_0_x1991_x1755_1816026103}

[[应用映射失败，即查找不到应用对应关系的报文数目]{style="font-family:宋体"}]{#struct_0_x1991_x1755_833503915}

[[InDiscarded]{lang="EN-US"}]{#struct_0_x1991_x1755_1017274086}

[[从]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_361093067}[机接收报文时，因接收缓冲区满或因获取交易号失败而丢弃的报文数目]{style="font-family:宋体"}

[[OutDiscarded]{lang="EN-US"}]{#struct_0_x1991_x1755_x813368428}

[[终端发送报文时，因链路不通而丢弃的报文数目]{style="font-family:宋体"}]{#struct_0_x1991_x1755_833962667}

[[Notified]{lang="EN-US"}]{#struct_0_x1991_x1755_756499763}

[[设备向]{style="font-family:宋体"}]{#struct_0_x1991_x1755_833897131}[POS]{lang="EN-US"}[机发送的通告报文数目，是指当设备处理]{style="font-family:宋体"}[POS]{lang="EN-US"}[机报文应用映射失败、获取交易号失败或者向前置机转发]{style="font-family:宋体"}[POS]{lang="EN-US"}[机报文失败时，设备向]{style="font-family:宋体"}[POS]{lang="EN-US"}[机发送的通告报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_751549231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset posa statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1558904443}

::: {#1281349381 .myid}
[]{#_Toc404785984}[]{#struct_0_x1991_x1755_1415764964}[]{#_Toc358227435}[]{#_Toc336625620}[]{#_Toc193529377}

**POS终端接入 \-- POS终端接入配置命令 \-- display posa status app**

------------------------------------------------------------------------

[**[display posa status app]{lang="EN-US"}**]{#struct_0_x1991_x1755_254793526}[命令用来显示]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x1991_x1755_1955892}

[**[display posa status app]{lang="EN-US"}**[ \[ *app-id* \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x1278792682}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833438380}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1838326688}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_59452416}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x603477966}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_112611128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1423267756}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_560035065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2113006845}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_540887300}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。如果不指定该参数，则显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的状态信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833372844}

[[通过该显示命令查看到的]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x2006068363}[信息项主要包括：应用]{style="font-family:宋体"}[ID]{lang="EN-US"}[、应用类型、模式、应用接口]{style="font-family:宋体"}[/]{lang="EN-US"}[应用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号、连接状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_878530807}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1963987834}[显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa status app]{lang="EN-US"}]{#struct_0_x1991_x1755_x617969708}

[AppID  Type  Mode       Interface       IPAddr:Port           State]{lang="EN-US"}

[1      TCP   Temporary  -               192.168.7.254:1000    linked]{lang="EN-US"}

[2      TCP   Temporary  -               192.168.7.224:1000    Error]{lang="EN-US"}

[3      Flow  -          Asy2/1/0        -                     Down]{lang="EN-US"}

[9      TCP   Permanent  -               192.168.4.1:20        Unlinked]{lang="EN-US"}

[11     TCP   Permanent  -               192.4.5.5:111         Unlinked]{lang="EN-US"}

[30     TCP   Temporary  -               192.168.7.52:4000     Multilink(10)]{lang="EN-US"}

[31     Flow  -          -                -                    -]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display posa status app]{lang="EN-US"}]{#struct_0_x1991_x1755_366740286}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1429744432}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1839254267}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833307308}

[[AppID]{lang="EN-US"}]{#struct_0_x1991_x1755_x391601337}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x940527159}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1991_x1755_759613997}

[[应用的连接类型：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1344021909}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_x1687570319}[：流连接方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_833241772}[：]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式]{lang="EN-US" style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x1991_x1755_x1549217683}

[[应用模板的模式：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x232826791}

[[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_1398995432}[：显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1122978474}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permanent]{lang="EN-US"}]{#struct_0_x1991_x1755_1377764055}[：]{style="font-family:宋体"}[长连接模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Temporary]{lang="EN-US"}]{#struct_0_x1991_x1755_x818346217}[：短连接模式]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1991_x1755_833700524}

[[应用模板的接口（未配置或者]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_566028193}[方式下该项为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[IPAddr]{lang="EN-US"}]{#struct_0_x1991_x1755_1697101731}[：]{style="font-family:宋体"}[Port]{lang="EN-US"}

[[应用模板的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1742740493}[地址和端口号（未配置或者]{style="font-family:宋体"}[Flow]{lang="EN-US"}[方式下该项为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1991_x1755_1309936263}

[[应用模板的连接状态：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_833634988}

[[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_1325489994}[方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1991_x1755_x660648746}[：连接建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1991_x1755_x976192335}[：连接断开]{lang="EN-US" style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_608889649}[方式：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlinked]{lang="EN-US"}]{#struct_0_x1991_x1755_833569452}[：连接未建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linking]{lang="EN-US"}]{#struct_0_x1991_x1755_1816026104}[：连接正在建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linked]{lang="EN-US"}]{#struct_0_x1991_x1755_1259728475}[：连接已建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multilink(N)]{lang="EN-US"}]{#struct_0_x1991_x1755_1832634767}[：标识该应用下建立了]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[条]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Blocked]{lang="EN-US"}]{#struct_0_x1991_x1755_872366695}[：标识该应用故障，被静默]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x1991_x1755_833962668}[：应用模板表项不可用，原因为该表项使能失败（]{style="font-family:宋体"}[TCP]{lang="EN-US"}[绑定源端口失败）]{style="font-family:宋体"}

[[未配置]{style="font-family:宋体"}[Interface]{lang="EN-US"}]{#struct_0_x1991_x1755_756499764}[／]{style="font-family:宋体"}[IPAddr]{lang="EN-US"}[：]{style="font-family:宋体"}[Port]{lang="EN-US"}[时，该项为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1727582650 .myid}
[]{#_Toc404785985}[]{#struct_0_x1991_x1755_929917807}[]{#_Toc358227436}[]{#_Toc336625621}[]{#_Toc194748110}

**POS终端接入 \-- POS终端接入配置命令 \-- display posa status terminal**

------------------------------------------------------------------------

[**[display posa status terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_698929601}[命令用来显示]{style="font-family:
宋体"}[POS]{lang="EN-US"}[终端模板的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1365983970}

[**[display posa status terminal]{lang="EN-US"}**[ \[ *terminal-id* \]]{lang="EN-US"}]{#struct_0_x1991_x1755_833897132}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_751549234}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1558904448}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_656250077}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_333264252}

[[network-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x1161234925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_2019937341}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1991_x1755_x584750094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2051622163}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_1767124894}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。如果不指定该参数，则显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833438377}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1793696673}[显示所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display posa status terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_833372841}

[TerminalID  Type  Interface       ListenPort  State]{lang="EN-US"}

[1           TCP   -               2000        Unlinked]{lang="EN-US"}

[2           TCP   -               2000        Error]{lang="EN-US"}

[3           FCM   Fcm2/10/0:0.0   -           Down]{lang="EN-US"}

[254         TCP   -               3000        Multilink(2)]{lang="EN-US"}

[255         Flow  Asy2/1/0        -           Up]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display posa status terminal]{lang="EN-US"}]{#struct_0_x1991_x1755_x2006068360}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1430731544}[[字段]{style="font-family:黑体"}]{#struct_0_x1991_x1755_475246280}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1410344795}

[[TerminalID]{lang="EN-US"}]{#struct_0_x1991_x1755_x295839827}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x122680008}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Type]{lang="EN-US"}]{#struct_0_x1991_x1755_x786562662}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833307305}[终端模板的连接类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Flow]{lang="EN-US"}]{#struct_0_x1991_x1755_x391601340}[：流接入方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_x940985904}[：]{style="font-family:宋体"}[FCM]{lang="EN-US"}[拨号接入方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_405713890}[：]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式]{lang="EN-US" style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1991_x1755_1322824837}

[[接入的端口（]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x477142931}[接入方式下该项为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[ListenPort]{lang="EN-US"}]{#struct_0_x1991_x1755_833241769}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_407097448}[终端的监听端口（]{style="font-family:宋体"}[FCM/Flow]{lang="EN-US"}[接入方式下该项为"]{style="font-family:宋体"}[-]{lang="EN-US"}["）]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1991_x1755_1458499871}

[[终端的连接状态：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_447239367}

[[Flow/FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_x2072865671}[接入：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1991_x1755_2061866775}[：连接建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1991_x1755_833700521}[：连接断开]{lang="EN-US" style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_566028190}[接入：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlinked]{lang="EN-US"}]{#struct_0_x1991_x1755_1697101732}[：连接未建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linked]{lang="EN-US"}]{#struct_0_x1991_x1755_x1742543885}[：连接已建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Multilink(N)]{lang="EN-US"}]{#struct_0_x1991_x1755_x1692601415}[：标识该终端下建立了]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[条]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Error]{lang="EN-US"}]{#struct_0_x1991_x1755_833634985}[：表项不可用，该表项使能失败]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-943806969 .myid}
[]{#_Toc404785986}[]{#struct_0_x1991_x1755_1325489989}[]{#_Toc358227437}[]{#_Toc336625606}

**POS终端接入 \-- POS终端接入配置命令 \-- hello enable**

------------------------------------------------------------------------

[**[hello]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1991_x1755_x660321065}[命令用来开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板握手功能。]{style="font-family:宋体"}

[**[undo ]{lang="PT-BR"}[hello enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_912233879}[用来关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板握手功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1541797612}

[**[hello]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1991_x1755_x1984627604}

[**[undo ]{lang="PT-BR"}[hello enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x11058310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1024756563}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x462325598}[应用模板握手功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833569449}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x140289025}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1748249117}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_773938571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1442728917}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1920566495}

[[只有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1917118603}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板支持此命令。]{style="font-family:宋体"}

[[缺省情况下，设备只有在存在]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1842850270}[业务的情况下才会和前置机通信，并发现前置机是否故障，这样可能会使当前交易业务处理失败或者导致业务处理的时延较长。为了提前发现故障并做容错处理，尽量降低前置机故障对]{style="font-family:宋体"}[POS]{lang="EN-US"}[业务的影响，可通过开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板周期性握手功能来主动探测前置机的状态。前置机也可以通过此功能来判断设备的可达性。]{style="font-family:宋体"}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833503913}[应用模板握手功能的流程为：设备以指定的间隔（可以通过]{style="font-family:宋体"}**[timer hello]{lang="EN-US"}**[命令设置）向当前]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立后，设备还会向前置机发送]{style="font-family:宋体"}[DATA]{lang="EN-US"}[字段为空的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文（报文内容固定为]{style="font-family:宋体"}[00056000000000]{lang="EN-US"}[，前置机并不会回应此报文）。]{style="font-family:宋体"}

[[对于短连接应用，设备会新建一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1017274080}[连接发报文，对于长连接应用，设备使用已经存在的长连接发送报文，若长连接不存在则创建，并在握手后继续保持。]{style="font-family:宋体"}

[[握手功能会影响当前应用的静默状态：若处于静默状态的]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_361486283}[应用模板握手成功，则退出静默状态；若处于非静默状态的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板握手失败，则进入静默状态。]{style="font-family:宋体"}

[[对于短连接应用，握手时发起连接成功不会发送前置机状态变化的告警信息。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1816456701}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_393609184}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_833962665}[开启应用]{style="font-family:宋体"}[1]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_756499761}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] hello enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_929917802}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer hello]{lang="EN-US"}**]{#struct_0_x1991_x1755_698929596}
:::

::: {#-839206969 .myid}
[]{#_Toc404785987}[]{#struct_0_x1991_x1755_833897129}[]{#_Toc358227438}[]{#_Toc336625595}[]{#_Toc193529379}

**POS终端接入 \-- POS终端接入配置命令 \-- ip**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1587102937}[命令用来配置当前]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号。]{style="font-family:宋体"}

[**[undo ip]{lang="PT-BR"}**]{#struct_0_x1991_x1755_1401954967}[命令用来取消应用模板对应前置机的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833438378}

[**[ip]{lang="EN-US"}**[ *ip-address* **port** *port-number*]{lang="EN-US"}]{#struct_0_x1991_x1755_1793696680}

[**[undo ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_987644328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_21087934}

[[未定义当前]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1247977266}[应用模板对应的前置机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[和端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x813302870}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x386406131}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1666133537}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_833372842}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x2006068361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2041330221}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1991_x1755_49952436}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板银行前置机的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为非环回的单播]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_x1991_x1755_1493756542}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板银行前置机服务的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833307306}

[[同一个]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x391601343}[应用模板下只能配置一个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口，修改]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者端口号将会删除现有的该]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x940789296}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1895770861}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x701015982}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] ip 1.1.1.1 port 3000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_780547964}[修改]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口。]{style="font-family:宋体"}

[[\[Sysname-posa-app1\] ip 1.1.1.2 port 3001]{lang="EN-US"}]{#struct_0_x1991_x1755_833241770}

[Connections for the application have been reset.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1549217681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1395626205}
:::

::: {#1985170617 .myid}
[]{#_Toc404785988}[]{#struct_0_x1991_x1755_x1181348672}[]{#_Toc358227439}[]{#_Toc336625598}

**POS终端接入 \-- POS终端接入配置命令 \-- mode**

------------------------------------------------------------------------

[**[mode]{lang="EN-US"}**]{#struct_0_x1991_x1755_196795739}[命令用来配置当前]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的连接模式。]{style="font-family:宋体"}

[**[undo mode]{lang="EN-US"}**]{#struct_0_x1991_x1755_833700522}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_566028187}

[**[mode]{lang="EN-US"}**[ { **permanent** \| **temporary** }]{lang="EN-US"}]{#struct_0_x1991_x1755_833569450}

[**[undo mode]{lang="EN-US"}**]{#struct_0_x1991_x1755_1816026102}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1259597403}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x469830607}[应用模板的连接模式为长连接模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_118497736}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x417016802}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_455654127}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_833503914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1017274085}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_361289675}

[**[permanent]{lang="EN-US"}**]{#struct_0_x1991_x1755_x596056979}[：设置连接模式为长连接模式。]{style="font-family:宋体"}

[**[temporary]{lang="EN-US"}**]{#struct_0_x1991_x1755_1299648117}[：]{style="font-family:宋体"}[设置连接模式为短连接模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833962666}

[[该配置只对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_756499762}[连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板有效。]{style="font-family:宋体"}

[[修改]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833897130}[应用模板的连接模式会断开该模板的已建立的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[短连接模式下，每次]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_751549232}[业务结束时（终端挂机或者断开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时），设备都会断开与前置机应用的连接。长连接模式下，当第一次]{style="font-family:宋体"}[POS]{lang="EN-US"}[业务传送完毕后，这个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接会一直保持用来传送后续的]{style="font-family:宋体"}[POS]{lang="EN-US"}[业务，即这个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接一经建立就不会主动断开。将长连接修改为短连接时，会删除该模板下已经存在的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[长连接。]{style="font-family:宋体"}

[[在短连接模式下，终端每发起一次新的交易，设备都会向前置机创建一个新的连接，可并发多个与前置机的连接。在长连接模式下，非透传终端每发起一次新的连接，只会使用设备与前置机之间现有的一条长连接不会创建新的连接，所以只创建一条与前置机的连接；有个例外情况：若终端配置透传]{style="font-family:宋体"}[APP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1558904446}[，则无论该]{style="font-family:宋体"}[APP]{lang="EN-US"}[为长连接或者短连接，设备都会为该终端创建一条与前置机专用的连接，此时设备与前置机之间可并发多个连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2119687445}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_833438375}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的连接模式为短连接，现有已经建立的长连接被删除。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1793696675}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] mode temporary]{lang="EN-US"}

[Connections for the application have been reset.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_987840923}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1655883591}
:::

::: {#805885208 .myid}
[]{#_Toc193529382}[]{#_Toc404785989}[]{#struct_0_x1991_x1755_176190457}[]{#_Toc358227440}[]{#_Toc343694226}[]{#_Toc342660222}[]{#_Toc336617632}

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation hookoff**

------------------------------------------------------------------------

[**[negotiation hookoff]{lang="FR"}**]{#struct_0_x1991_x1755_x2027281131}[命令用来设置]{style="font-family:宋体"}[FCM]{lang="FR"}[接口接收到铃流后]{style="font-family:宋体"}[FCM]{lang="FR"}[卡延时摘机时间。]{style="font-family:宋体"}

[**[undo negotiation hookoff]{lang="FR"}**]{#struct_0_x1991_x1755_239888884}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1219339856}

[**[negotiation hookoff ]{lang="FR"}**]{#struct_0_x1991_x1755_833372839}*[delaytime]{lang="FR"}*

[**[undo negotiation hookoff]{lang="FR"}**]{#struct_0_x1991_x1755_x1196764304}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1372948943}

[[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_288722700}[接口接收到铃流后延时摘机时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833307303}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x391601346}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x940592688}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1179527169}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_311917413}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1583493389}

[*[d]{lang="EN-US"}*]{#struct_0_x1991_x1755_x266354762}*[elaytime]{lang="FR"}*[：]{style="font-family:宋体"}[FCM]{lang="FR"}[接口]{style="font-family:
宋体"}[收到铃流后]{style="font-family:宋体"}[FCM]{lang="NO-BOK"}[卡延时摘机时间，取值范围是]{style="font-family:宋体"}[100]{lang="NO-BOK"}[～]{style="font-family:宋体"}[6000]{lang="NO-BOK"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_773649237}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_242344929}[设置]{style="font-family:宋体"}[FCM2/4/0]{lang="NO-BOK"}[接口接收到铃流后]{style="font-family:宋体"}[FCM]{lang="NO-BOK"}[卡延时摘机时间。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_833241767}

[\[Sysname\] interface fcm 2/4/0]{lang="NO-BOK"}

[\[Sysname-Fcm2/4/0\] negotiation hookoff 2000]{lang="NO-BOK"}
:::

::: {#-1268917353 .myid}
[]{#_Toc404785990}[]{#struct_0_x1991_x1755_407097450}[]{#_Toc358227441}[]{#_Toc343694227}[]{#_Toc342660223}

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation no-carrier-detect retry**

------------------------------------------------------------------------

[**[negotiation no-carrier-detect retry]{lang="EN-US"}**]{#struct_0_x1991_x1755_x497815257}[命令用来配置连续检测到线路为无载波状态的次数。]{style="font-family:宋体"}

[**[undo negotiation no-carrier-detect retry]{lang="EN-US"}**]{#struct_0_x1991_x1755_x467565451}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x91461583}

[**[negotiation no-carrier-detect retry ]{lang="EN-US"}***[n-retrytime]{lang="EN-US"}*]{#struct_0_x1991_x1755_x351915859}

[**[undo negotiation no-carrier-detect retry]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1669420060}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_616583083}

[[连续检测到线路为无载波状态的次数为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_x1991_x1755_833700519}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1390286938}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1852003271}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1742653253}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_455003893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_863155430}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_852712434}

[*[n-retrytime]{lang="EN-US"}*]{#struct_0_x1991_x1755_x486114529}[：]{style="font-family:宋体"}[连续检测到线路为无载波状态的次数]{style="font-family:宋体"}[，取值范围是]{style="font-family:宋体"}[1]{lang="NO-BOK"}[～]{style="font-family:宋体"}[1000]{lang="NO-BOK"}[。当]{style="font-family:宋体"}[FCM]{lang="NO-BOK"}[卡连续检测到线路为无载波状态的次数为]{style="font-family:宋体"}*[n-retrytime]{lang="EN-US"}*[时，将挂机。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x636873007}

[[\# ]{lang="NO-BOK"}]{#struct_0_x1991_x1755_833634983}[设置]{style="font-family:宋体"}[FCM2/4/0]{lang="NO-BOK"}[接口]{style="font-family:宋体"}[连续检测到线路为无载波状态的次数]{style="font-family:宋体"}[为]{style="font-family:宋体"}[20]{lang="NO-BOK"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1325489983}

[\[Sysname\] interface fcm 2/4/0]{lang="NO-BOK"}

[\[Sysname-Fcm2/4/0\] negotiation no-carrier-detect retry 20]{lang="NO-BOK"}
:::

::: {#1888481936 .myid}
[]{#_Toc404785991}[]{#struct_0_x1991_x1755_x660714281}[]{#_Toc358227442}[]{#_Toc343694223}[]{#_Toc342660219}

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation scramble-binary1**

------------------------------------------------------------------------

[**[negotiation scramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_120648666}[命令用来设置]{style="font-family:
宋体"}[Modem]{lang="EN-US"}[协商发送扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[的持续时间。]{style="font-family:宋体"}

[**[undo negotiation scramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1890448230}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1680955163}

[**[negotiation scramble-binary1 ]{lang="EN-US"}**]{#struct_0_x1991_x1755_1430119144}*[scramble-binary1time]{lang="NO-BOK"}*

[**[undo negotiation scramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_154944829}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833569447}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x140289027}[协商发送扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[的持续时间为]{style="font-family:宋体"}[250]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1748118045}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_3401874}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_916973135}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1354819091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x2002168755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x286365991}

[*[scramble-binary1time]{lang="NO-BOK"}*]{#struct_0_x1991_x1755_x61174887}[：设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商发送扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[的持续时间，取值范围是]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833503911}

[[\# ]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1017274082}[设置]{style="font-family:宋体"}[Modem]{lang="NO-BOK"}[协商发送扰码]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的持续时间为]{style="font-family:宋体"}[200]{lang="NO-BOK"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_361355211}

[\[Sysname\] interface fcm 2/4/0]{lang="NO-BOK"}

[\[Sysname-Fcm2/4/0\] negotiation scramble-binary1 200]{lang="NO-BOK"}
:::

::: {#242712294 .myid}
[]{#_Toc404785992}[]{#struct_0_x1991_x1755_x2111695920}[]{#_Toc358227443}[]{#_Toc343694225}[]{#_Toc342660221}

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation silence**

------------------------------------------------------------------------

[**[negotiation silence]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1898707647}[命令用来设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的静默时间。]{style="font-family:宋体"}

[**[undo negotiation silence]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2112503828}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_81087324}

[**[negotiation silence ]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1480250435}*[silencetime]{lang="NO-BOK"}*

[**[undo negotiation silence]{lang="EN-US"}**]{#struct_0_x1991_x1755_848849941}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833962663}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_756499759}[协商的]{style="font-family:宋体"}[静默时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x644060318}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_966004842}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1358941309}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_478392143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_833897127}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1587102923}

[*[silencetime]{lang="NO-BOK"}*]{#struct_0_x1991_x1755_x923578325}[：设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的静默时间，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3000]{lang="EN-US"}[，单位为毫秒。静默时间是指]{style="font-family:宋体"}[FCM]{lang="EN-US"}[卡从摘机到发送数据之间的时间。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833438376}

[[静默时间主要是应用于]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_1793696674}[卡和]{style="font-family:宋体"}[POS]{lang="EN-US"}[机握手，静默时间必须大于]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的摘机响应时间小于]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的最大等待时间。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果静默时间大于]{style="font-family:宋体"}]{#struct_0_x1991_x1755_420284433}[POS]{lang="EN-US"}[机的最大等待时间，]{style="font-family:宋体"}[POS]{lang="EN-US"}[机会以为没有数据而挂机；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果静默时间小于]{style="font-family:宋体"}]{#struct_0_x1991_x1755_319414250}[POS]{lang="EN-US"}[机的摘机响应时间，因]{style="font-family:宋体"}[POS]{lang="EN-US"}[机检测到]{style="font-family:宋体"}[FCM]{lang="EN-US"}[卡摘机需要一段时间，此时]{style="font-family:宋体"}[POS]{lang="EN-US"}[机还未检测到]{style="font-family:宋体"}[FCM]{lang="EN-US"}[卡摘机就已将数据发出，从而导致数据丢失。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_987906459}

[[\# ]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1804870914}[设置]{style="font-family:宋体"}[Modem]{lang="NO-BOK"}[协商的静默时间为]{style="font-family:宋体"}[100]{lang="NO-BOK"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1290085089}

[\[Sysname\] interface fcm 2/4/0]{lang="NO-BOK"}

[\[Sysname-Fcm2/4/0\] negotiation silence 100]{lang="NO-BOK"}
:::

::: {#-1672486388 .myid}
[]{#_Toc193529387}[]{#_Toc404785993}[]{#struct_0_x1991_x1755_x1545095562}[]{#_Toc358227444}[]{#_Toc343694224}[]{#_Toc342660220}

**POS终端接入 \-- POS终端接入配置命令 \-- negotiation unscramble-binary1**

------------------------------------------------------------------------

[**[negotiation unscramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329615117}[命令用来设置]{style="font-family:
宋体"}[Modem]{lang="EN-US"}[协商发送非扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[的持续时间。]{style="font-family:宋体"}

[**[undo negotiation unscramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_x937057336}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_26837983}

[**[negotiation unscramble-binary1 ]{lang="EN-US"}**]{#struct_0_x1991_x1755_833372840}*[unscramble-binary1time]{lang="NO-BOK"}*

[**[undo negotiation  unscramble-binary1]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2006068359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1897603323}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x315715076}[协商发送非扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[的持续时间为]{style="font-family:宋体"}[400]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1315516560}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1308028338}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1482766141}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_373167839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x996167253}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833307304}

[*[unscramble-binary1time]{lang="NO-BOK"}*]{#struct_0_x1991_x1755_x391601341}[：设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商发送非扰码]{style="font-family:宋体"}[1]{lang="EN-US"}[持续时间，取值范围是]{style="font-family:宋体"}[300]{lang="EN-US"}[～]{style="font-family:宋体"}[1500]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x940920368}

[[\# ]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1136726445}[设置]{style="font-family:宋体"}[Modem]{lang="NO-BOK"}[协商发送非扰码]{style="font-family:宋体"}[1]{lang="NO-BOK"}[的持续时间为]{style="font-family:宋体"}[900]{lang="NO-BOK"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_675752840}

[\[Sysname\] interface fcm 2/4/0]{lang="NO-BOK"}

[\[Sysname-Fcm2/4/0\] negotiation unscramble-binary1 900]{lang="NO-BOK"}
:::

::: {#-1001704081 .myid}
[]{#_Toc404785994}[]{#struct_0_x1991_x1755_727296926}[]{#_Toc358227445}[]{#_Toc336625594}

**POS终端接入 \-- POS终端接入配置命令 \-- posa app**

------------------------------------------------------------------------

[**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_1621295861}[命令用来创建]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板并进入]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板视图。]{style="font-family:宋体"}

[**[undo posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1615210926}[用来删除配置的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833241768}

[**[posa app]{lang="EN-US"}**[ *app-id* **type** { **flow** \| **tcp** }]{lang="EN-US"}]{#struct_0_x1991_x1755_407097447}

[**[undo posa app]{lang="PT-BR"}**]{#struct_0_x1991_x1755_1458499876}[ *app-id*]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_447567047}

[[不存在]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1713643721}[应用模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x389306609}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_326708671}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_34473707}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_875639766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x404091201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833700520}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_566028189}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**]{#struct_0_x1991_x1755_x641550419}[：]{style="font-family:宋体"}[设备与银行前置机之间的连接方式。]{style="font-family:宋体"}

[**[flow]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1512828627}[：表示流连接方式。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_x1991_x1755_1607263289}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1809821576}

[[不能重复配置相同应用]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1991_x1755_833634984}[，并且不能更改已有的设备与前置机之间的连接方式。]{style="font-family:宋体"}

[[创建流方式]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833569448}[应用模板之后应将其绑定到接口（]{style="font-family:宋体"}[Async]{lang="EN-US"}[、]{style="font-family:宋体"}[Serial]{lang="EN-US"}[和]{style="font-family:宋体"}[Aux]{lang="EN-US"}[接口）上方可生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x140289026}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_833503912}[创建流连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，并绑定到]{style="font-family:宋体"}[Async2/7/0]{lang="EN-US"}[接口上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1017274079}

[\[Sysname\] posa app 1 type flow]{lang="EN-US"}

[\[Sysname-posa-app1\] quit]{lang="EN-US"}

[\[Sysname\] interface Async 2/7/0]{lang="EN-US"}

[\[Sysname-Async2/7/0\] posa bind app 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_362076116}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x473587679}

[\[Sysname\] posa app 2 type tcp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1795508586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa bind app]{lang="EN-US"}**]{#struct_0_x1991_x1755_2063971129}
:::

::: {#641105727 .myid}
[]{#_Toc404785995}[]{#struct_0_x1991_x1755_x643413484}[]{#_Toc364340122}[]{#_Toc361152883}

**POS终端接入 \-- POS终端接入配置命令 \-- posa auto-stop-service enable**

------------------------------------------------------------------------

[**[posa auto-stop-service enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_1841929402}[命令用来开启当所有的前置机状态为不可达时，主动关闭]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[类型终端模板的监听端口功能。]{style="font-family:宋体"}

[**[undo posa auto-stop-service enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1809359838}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1405603769}

[**[posa auto-stop-service enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_1278835281}

[**[undo posa auto-stop-service enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_386961880}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1828084044}

[[主动关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1870072699}[类型终端模板的监听端口功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_417799732}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x287248660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1941479274}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x868393790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1316454077}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x757672182}

[[当所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1853332601}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机状态为不可达时，]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入设备将主动关闭所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型终端模板的监听端口。]{style="font-family:宋体"}

[[当任意一个前置机状态变为可达时，则主动打开所有]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x98701787}[类型终端模板的监听端口。]{style="font-family:宋体"}

[[前置机状态不可达是指]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_713859540}[终端接入设备与前置机发起连接失败（包含发起连接超时），或在连接过程中]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文保活失败导致连接断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_121025515}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1753455813}[开启主动关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型终端模板的监听端口功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_875550754}

[\[Sysname\] posa auto-stop-service enable]{lang="EN-US"}
:::

::: {#-1309291413 .myid}
[]{#_Toc404785996}[]{#struct_0_x1991_x1755_35175067}[]{#_Toc358227446}[]{#_Toc336625608}

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind app**

------------------------------------------------------------------------

[**[posa bind app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x394469791}[命令用来绑定]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[**[undo posa bind app]{lang="EN-US"}**]{#struct_0_x1991_x1755_833962664}[命令用来取消该接口下绑定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_756499760}

[**[posa bind app]{lang="EN-US"}**[ *app-id*]{lang="EN-US"}]{#struct_0_x1991_x1755_929917803}

[**[undo posa bind app]{lang="EN-US"}**]{#struct_0_x1991_x1755_698929597}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_153395381}

[[接口下未绑定任何]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x2059368307}[应用模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1429427141}

[[异步接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1991_x1755_295222973}[同异步接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_338446474}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_833897128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1587102936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1326928388}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x370466495}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2007581144}

[[通过异步接口连接前置机的方式下，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_381291555}[应用模板是通过异步接口来标识的，即一个接口对应一个应用，本命令用来将异步接口与对应的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板绑定。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895444976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在接口下绑定]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x881105581}[POS]{lang="EN-US"}[应用模板之前，必须先在系统视图下创建该应用，且该应用的类型必须为]{style="font-family:宋体"}[Flow]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口下只能绑定一个]{style="font-family:宋体"}]{#struct_0_x1991_x1755_944343910}[POS]{lang="EN-US"}[应用模板，若要修改绑定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板，则必须首先取消与当前]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的绑定，再绑定新的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的接口上必须绑定不同的]{style="font-family:宋体"}]{#struct_0_x1991_x1755_397376109}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一接口不能同时配置为接入]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1481066490}[POS]{lang="EN-US"}[终端模板的接口和绑定]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同异步接口绑定]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1182430314}[POS]{lang="EN-US"}[应用模板时，该接口必须工作在异步模式下。若接口不为异步模式则配置可以成功但是该模板的状态为]{style="font-family:宋体"}[error]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口必须工作在流模式下]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895510512}[POS]{lang="EN-US"}[终端接入设备才能正常工作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1514542374}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1601248072}[配置]{style="font-family:宋体"}[Flow]{lang="EN-US"}[类型的应用]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_175360262}

[\[Sysname\] posa app 2 type flow]{lang="EN-US"}

[\[Sysname-posa-app2\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x175948906}[配置异步接口]{style="font-family:宋体"}[Async2/1/0]{lang="EN-US"}[与应用]{style="font-family:宋体"}[2]{lang="EN-US"}[相连。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895576048}

[\[Sysname\] interface async2/1/0]{lang="EN-US"}

[\[Sysname-Async2/1/0\] posa bind app 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1593909189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1553908198}
:::

::: {#-1521386680 .myid}
[]{#_Toc404785997}[]{#struct_0_x1991_x1755_x2031840259}[]{#_Toc358227447}[]{#_Toc336625612}

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind terminal**

------------------------------------------------------------------------

[**[posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_663397511}[命令用来指定当前接口为某]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口。]{style="font-family:宋体"}

[**[undo posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895641584}[命令用来取消该接口为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1853520921}

[**[posa bind terminal]{lang="NO-BOK"}**]{#struct_0_x1991_x1755_x2131286932}[ *terminal-id* \[ **app** *app-id* \]]{lang="NO-BOK"}

[**[undo posa bind terminal]{lang="NO-BOK"}**]{#struct_0_x1991_x1755_1855585606}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1881154201}

[[当前接口未配置为任何]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x436469992}[终端模板的接入接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1895182832}

[[异步接口视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x888486270}[/]{lang="NO-BOK"}[同异步接口视图]{style="font-family:宋体"}[/]{lang="NO-BOK"}[物理]{style="font-family:宋体"}[AM]{lang="NO-BOK"}[接口视图]{style="font-family:宋体"}[/]{lang="NO-BOK"}[物理]{style="font-family:宋体"}[FCM]{lang="NO-BOK"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_408432165}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1353111270}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_2070523994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x849306309}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_421483851}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[app]{lang="NO-BOK"}**]{#struct_0_x1991_x1755_319263635}[ ]{lang="NO-BOK"}*[app-id]{lang="EN-US"}*[：指定该]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板工作在透传模式下，并指定其对应的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}*[app-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。指定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板必须为已经存在的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。若不指定该参数，则表示该]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板工作在非透传模式下。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1336395354}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同异步串口需要工作在异步方式下，才能配置该命令；若接口不为异步模式则配置可以成功但是该模板的状态为]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895248368}[error]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个接口只能指定为一个]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1311814017}[POS]{lang="EN-US"}[终端模板的接入接口；不同的接口必须指定为不同的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一接口不能同时配置为接入]{style="font-family:宋体"}]{#struct_0_x1991_x1755_662741993}[POS]{lang="EN-US"}[终端模板的接口和绑定]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的接口；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口下配置的]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1688785178}[POS]{lang="EN-US"}[终端模板不能在非透传模式与非透传模式之间的转换，也不能修改对应的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板，必须先取消该接口为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口，再重新配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1683017672}[POS]{lang="EN-US"}[终端模板可以指定一个相同的透传应用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若指定的透传应用不存在或者不是]{style="font-family:宋体"}]{#struct_0_x1991_x1755_982049355}[TCP]{lang="EN-US"}[类型允许配置，但不生效，终端交易时会失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_860991184}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1174057784}[配置]{style="font-family:宋体"}[Async2/1/0]{lang="EN-US"}[为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的接入接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895313904}

[\[Sysname\] interface async 2/1/0]{lang="EN-US"}

[\[Sysname-Async2/1/0\] posa bind terminal 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_230894580}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1497146073}
:::

::::: {#831743750 .myid}
[]{#_Toc404785998}[]{#struct_0_x1991_x1755_1541445747}[]{#_Toc387769740}[]{#_Toc385338774}

**POS终端接入 \-- POS终端接入配置命令 \-- posa bind terminal first-terminal-id**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](POS终端接入命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1991_x1755_x24638194}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备支持的接口类型有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1991_x1755_x1226734196}
:::

**[ ]{lang="EN-US"}**

[**[posa bind terminal first-terminal-id]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1041443471}[命令用来]{style="font-family:宋体"}[批量指定当前接口的子接口为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板接入接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_1238976861}[命令用来]{style="font-family:宋体"}[取消当前接口的子接口为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2095131328}

[**[posa bind terminal]{lang="EN-US"}[ first-terminal-id]{lang="EN-US"}**[ *first-terminal-id* \[ **app-list** *app-list* \[ **reassemble** \] \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x59779282}

[**[undo posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_453786895}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1125032834}

[[当前接口的子接口未配置为任何]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x86303465}[终端模板的接入接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1431244089}

[[通道化]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1897741643}[AM]{lang="NO-BOK"}[接口视图]{style="font-family:宋体"}[/]{lang="NO-BOK"}[通道化]{style="font-family:宋体"}[FCM]{lang="NO-BOK"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1512891317}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_501387138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_641433110}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_613053026}

[*[first-terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x116918581}[：起始终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。从起始终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[开始到]{style="font-family:宋体"}[255]{lang="EN-US"}[之间的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[依次用来与]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口或]{style="font-family:宋体"}[AM]{lang="EN-US"}[子接口进行绑定。]{style="font-family:宋体"}

[**[app-list]{lang="EN-US"}***[ app-list]{lang="EN-US"}*]{#struct_0_x1991_x1755_510228450}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板工作在透传模式下，并指定]{style="font-family:宋体"}[自起始终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[开始到终端模]{style="font-family:宋体"}[板]{style="font-family:宋体"}[ID 255]{lang="EN-US"}[连续递]{style="font-family:宋体"}[增的一组终端]{style="font-family:宋体"}[对应的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板。]{style="font-family:宋体"}*[app-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[列表。]{style="font-family:宋体"}*[app-list]{lang="EN-US"}*[取值包括数字、逗号"[,]{lang="EN-US"}"、连字符"[-]{lang="EN-US"}"和冒号"[:]{lang="EN-US"}"，不能包含空格。其中，]{style="font-family:宋体"}[逗号用来分隔单个数字或一组数字；连字符用来连接两个应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，表示从起始应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[到结束应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[之间连续的一串应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，且要求起始应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[要小于结束应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[；冒号用来连接两个数字，表示多次重复指定某一个应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，前面的数字表示应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，后面的数字表示重复的次数。应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[；重复次数的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。例如"]{style="font-family:宋体"}[1-14,15,16:13,127-128]{lang="EN-US"}["表示]{style="font-family:宋体"}[前]{style="font-family:宋体"}[14]{lang="EN-US"}[个子接口对应的应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[依次为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[14]{lang="EN-US"}[，第]{style="font-family:宋体"}[15]{lang="EN-US"}[个子接口对应的应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[15]{lang="EN-US"}[，第]{style="font-family:宋体"}[16]{lang="EN-US"}[到第]{style="font-family:宋体"}[28]{lang="EN-US"}[个子接口对应的应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[均为]{style="font-family:宋体"}[16]{lang="EN-US"}[，第]{style="font-family:宋体"}[29]{lang="EN-US"}[和]{style="font-family:宋体"}[30]{lang="EN-US"}[个子接口对应的应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[分别为]{style="font-family:宋体"}[127]{lang="EN-US"}[和]{style="font-family:宋体"}[128]{lang="EN-US"}[。如果不指定本参数，则表示]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板工作在非透传模式下。]{style="font-family:宋体"}

[**[reassemble]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1913503294}[：指定透传模式下，]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入设备对从]{style="font-family:宋体"}[POS]{lang="EN-US"}[机接收到的分片报文进行重组后，再发送给前置机。如果不指定本参数，则]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入设备直接将接收到的分片报文发送给前置机。只有通道化]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口视图下支持本参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x903289452}

[[一个物理类型为]{style="font-family:宋体"}[E1POS]{lang="EN-US"}]{#struct_0_x1991_x1755_363989550}[的]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口会生成多个]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口，一个物理类型为]{style="font-family:宋体"}[E1DM]{lang="EN-US"}[的]{style="font-family:宋体"}[CE1/PRI]{lang="EN-US"}[接口会生成多个]{style="font-family:宋体"}[AM]{lang="EN-US"}[子接口，本命令用来指定与各个子接口绑定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[和应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[。指定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板数目必须大于或等于子接口数目，指定的应用模板数目必须与子接口的数目一致，否则本命令执行失败。例如，指定了起始]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[251]{lang="EN-US"}[，若当前接口下的]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口数目大于]{style="font-family:宋体"}[5]{lang="EN-US"}[，则由于绑定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板只有]{style="font-family:宋体"}[5]{lang="EN-US"}[个（]{style="font-family:宋体"}[251]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[），]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板数不足导致批量配置失败。]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口和]{style="font-family:宋体"}[AM]{lang="EN-US"}[子接口生成方式的详细介绍，请参见"接口管理配置指导"中的"]{style="font-family:宋体"}[WAN]{lang="EN-US"}[接口"。]{style="font-family:宋体"}

[[如果要绑定的]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1647721431}[终端模板中存在非]{style="font-family:宋体"}[FCM/AM]{lang="EN-US"}[类型终端模板或已经与其它接口绑定的终端模板，则本命令执行失败。]{style="font-family:宋体"}

[[如果指定的应用模板不存在或者不是]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x928750033}[类型，则允许执行本命令，但配置不会生效，终端交易时会失败。]{style="font-family:宋体"}

[[如果前置机不支持对]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x6794485}[交易报文进行分片重组，那么在透传模式下，需要指定]{style="font-family:宋体"}**[reassemble]{lang="EN-US"}**[参数，由]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入设备对]{style="font-family:宋体"}[POS]{lang="EN-US"}[交易报文进行分片重组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_331657702}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x357731931}[接口]{style="font-family:宋体"}[FCM2/4/0:15]{lang="EN-US"}[下存在]{style="font-family:宋体"}[30]{lang="EN-US"}[个子接口，批量将这些接口指定为]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[的接入接口，并指定与其绑定的应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x2120253932}

[\[sysname\] interface fcm 2/4/0:15]{lang="EN-US"}

[\[sysname-Fcm2/4/0:15\] posa bind terminal first-terminal-id 1 app-list 1-30 ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1089417688}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app ]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1947438459}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1590768175}
:::::

::: {#-46871483 .myid}
[]{#_Toc404785999}[]{#struct_0_x1991_x1755_x1066281031}[]{#_Toc373766251}

**POS终端接入 \-- POS终端接入配置命令 \-- posa connection-threshold terminal**

------------------------------------------------------------------------

[**[posa connection-threshold terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_263571427}[命令用来设置终端并发连接数阈值。]{style="font-family:宋体"}

[**[undo posa connection-threshold terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_x576702955}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2103448614}

[**[posa connection-threshold]{lang="EN-US"}**[ **terminal** { **fcm** *fcm-threshold-value* \| **tcp** *tcp-threshold-value* }]{lang="EN-US"}]{#struct_0_x1991_x1755_x1704486613}

[**[undo posa connection-threshold terminal ]{lang="EN-US"}**[{ **fcm** \| **tcp** }]{lang="EN-US"}]{#struct_0_x1991_x1755_x959516337}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1517565639}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_312828499}[接入方式的并]{style="font-family:宋体"}[发连接数阈值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[4096]{lang="EN-US"}[，]{style="font-family:宋体"}[FCM]{lang="EN-US"}[拨号接入方式]{style="font-family:宋体"}[的并发连接数阈值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1885821111}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x85333244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1343949046}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1612162010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_694662165}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x432694845}

[**[fcm]{lang="SV"}**]{#struct_0_x1991_x1755_x1066346567}*[ fcm-threshold-value]{lang="SV"}*[：设置]{style="font-family:宋体"}[FCM]{lang="SV"}[拨号接入方式的并发连接数阈值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[255]{lang="SV"}[。]{style="font-family:
宋体"}

[**[tcp]{lang="SV"}**]{#struct_0_x1991_x1755_1315148080}*[ tcp-threshold-value]{lang="SV"}*[：设置]{style="font-family:宋体"}[TCP]{lang="SV"}[接入方式的并发连接数阈值，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[4096]{lang="SV"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2090445270}

[[如果开启了相应的]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1776506240}[终端接入告警功能，则当设备上的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[FCM]{lang="EN-US"}[拨号接入方式的终端并发连接数超过指定的阈值时，会生成相应的告警信息。]{style="font-family:宋体"}

[[需要注意的是，终端并发连接数达到指定的阈值后，不会影响后续连接的建立。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1879525419}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1420595766}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_462738790}[设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式的并发连接数阈值为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1067690530}

[\[Sysname\] posa connection-threshold terminal tcp 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1367233415}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap enable posa]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1336561186}
:::

::: {#865334202 .myid}
[]{#_Toc404786000}[]{#struct_0_x1991_x1755_825430225}[]{#_Toc358227448}[]{#_Toc336625613}[]{#_Toc193529384}[]{#_Toc336617640}[]{#_Toc336617641}[]{#_Toc336617642}[]{#_Toc336617643}[]{#_Toc336617644}[]{#_Toc336617646}[]{#_Toc336617647}[]{#_Toc336617648}[]{#_Toc336617649}[]{#_Toc336617650}[]{#_Toc336617651}[]{#_Toc336617652}[]{#_Toc336617653}[]{#_Toc336617654}[]{#_Toc336617655}[]{#_Toc336617656}[]{#_Toc336617657}[]{#_Toc336617658}[]{#_Toc336617659}[]{#_Toc336617660}[]{#_Toc336617666}[]{#_Toc336617667}[]{#_Toc336617668}[]{#_Toc336617669}[]{#_Toc336617670}[]{#_Toc336617671}[]{#_Toc336617672}[]{#_Toc336617673}[]{#_Toc336617674}[]{#_Toc336617676}[]{#_Toc336617677}[]{#_Toc336617679}[]{#_Toc336617680}[]{#_Toc336617681}[]{#_Toc336617682}[]{#_Toc336617683}[]{#_Toc336617684}[]{#_Toc336617685}[]{#_Toc336617686}

**POS终端接入 \-- POS终端接入配置命令 \-- posa fcm**

------------------------------------------------------------------------

[**[posa fcm]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895379440}[命令用来设置在]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商过程中的]{style="font-family:宋体"}[FCM]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[**[undo posa fcm]{lang="EN-US"}**]{#struct_0_x1991_x1755_46168817}[命令用来恢复参数的缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1902673954}

[**[posa fcm]{lang="EN-US"}**[ { **answer-time** *time1* \| **idle-time** *time2* \| **trade-time** *time3* }]{lang="EN-US"}]{#struct_0_x1991_x1755_x1894920688}

[**[undo posa fcm]{lang="EN-US"}**[ { **answer-time** \| **trade-time** \| **idle-time** }]{lang="EN-US"}]{#struct_0_x1991_x1755_1291413619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x322504105}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x1894986224}[协商过程中，应答音时间为]{style="font-family:宋体"}[2000]{lang="EN-US"}[毫秒，空闲时间为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，交易时间为]{style="font-family:宋体"}[12000000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_436407033}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_745946824}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1461407877}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_285248992}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x585807533}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_855745345}

[**[answer-time]{lang="EN-US"}**[ *time1*]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895444975}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商时向]{style="font-family:宋体"}[POS]{lang="EN-US"}[机发送应答音的时间，取值范围为]{style="font-family:宋体"}[500]{lang="EN-US"}[～]{style="font-family:宋体"}[2000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[idle-time]{lang="EN-US"}**[ *time2*]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895510511}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[机拨号后，链路上空闲最大时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[12000]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[180]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[trade-time]{lang="EN-US"}**[ *time3*]{lang="EN-US"}]{#struct_0_x1991_x1755_x338968309}[：单笔]{style="font-family:宋体"}[POS]{lang="EN-US"}[交易的持续时间，取值范围为]{style="font-family:宋体"}[30000]{lang="EN-US"}[～]{style="font-family:宋体"}[12000000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[12000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1111257847}

[[在]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895248367}[接入应用中，设备上的]{style="font-family:宋体"}[Modem]{lang="EN-US"}[通常都是作为应答端，而]{style="font-family:宋体"}[POS]{lang="EN-US"}[机内嵌的]{style="font-family:宋体"}[Modem]{lang="EN-US"}[做主叫方。]{style="font-family:宋体"}[Modem]{lang="EN-US"}[通信的基本过程为]{style="font-family:宋体"}[POS]{lang="EN-US"}[机发起呼叫，应答端检测到呼叫信号时会摘机并发送应答音给]{style="font-family:宋体"}[POS]{lang="EN-US"}[机，]{style="font-family:宋体"}[POS]{lang="EN-US"}[机收到该应答音后双方同步开始]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商（]{style="font-family:宋体"}[V.22]{lang="EN-US"}[）过程。由于电话网络比较复杂，信号质量及延迟也不尽相同，对于网络质量较差的系统，应答音设置太短可能会造成]{style="font-family:宋体"}[Modem]{lang="EN-US"}[无法协商通过，在设备上将只能看到]{style="font-family:宋体"}[Modem]{lang="EN-US"}[端口不断的]{style="font-family:宋体"}[up]{lang="EN-US"}[、]{style="font-family:宋体"}[down]{lang="EN-US"}[，而没有数据包的收发，这时候可以适当增大]{style="font-family:宋体"}**[answer-time]{lang="EN-US"}**[参数时间值。]{style="font-family:宋体"}

[[为了提高接入端口的利用效率，需要避免一台]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895313903}[机拨号接入设备之后长时间占用系统资源，若一台]{style="font-family:宋体"}[POS]{lang="EN-US"}[机拨入后单笔交易时间超过设置的]{style="font-family:宋体"}**[trade-time]{lang="EN-US"}**[值]{style="font-family:宋体"}[，或空闲时间超过设置的]{style="font-family:宋体"}**[idle-time]{lang="EN-US"}**[值]{style="font-family:宋体"}[，则设备会主动挂机以释放链路资源。]{style="font-family:宋体"}

[[一般情况下，各]{style="font-family:宋体"}[FCM]{lang="EN-US"}]{#struct_0_x1991_x1755_x172389947}[参数的缺省值基本上都可以满足应用，但在通信出现异常的情况下需要根据上述说明修改各个参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1971579055}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x2104419602}[配置]{style="font-family:宋体"}[answer-time]{lang="EN-US"}[为]{style="font-family:宋体"}[800]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[trade-time]{lang="EN-US"}[为]{style="font-family:宋体"}[20]{lang="EN-US"}[分钟（]{style="font-family:宋体"}[1200000]{lang="EN-US"}[毫秒），]{style="font-family:宋体"}[idle-time]{lang="EN-US"}[为]{style="font-family:宋体"}[6]{lang="EN-US"}[秒。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895379439}

[\[Sysname\] posa fcm answer-time 800]{lang="EN-US"}

[\[Sysname\] posa fcm trade-time 1200000]{lang="EN-US"}

[\[Sysname\] posa idle-time 6]{lang="EN-US"}
:::

::: {#1276054148 .myid}
[]{#_Toc275956210}[]{#_Toc404786001}[]{#struct_0_x1991_x1755_x1164143516}[]{#_Toc358227449}[]{#_Toc336625609}

**POS终端接入 \-- POS终端接入配置命令 \-- posa map**

------------------------------------------------------------------------

[**[posa]{lang="FR"}[ ]{lang="FR"}[map]{lang="EN-US"}**]{#struct_0_x1991_x1755_x935516946}[命令用来配置多应用的]{style="font-family:
宋体"}[POS]{lang="EN-US"}[接入映射表项。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1991_x1755_1348008258}**[posa]{lang="FR"}[ ]{lang="FR"}[map]{lang="EN-US"}**[命令用来删除多应用]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x87824207}

[**[posa map ]{lang="FR"}**]{#struct_0_x1991_x1755_x1894920687}[{ ]{lang="FR"}[{ ]{lang="DE"}**[default]{lang="FR"}**[ ]{lang="FR"}[\| **destination** *des-code* ]{lang="FR"}[\| ]{lang="DE"}**[source ]{lang="FR"}***[src-code]{lang="FR"}*[ ]{lang="FR"}[} \*]{lang="DE"}[ ]{lang="DE"}[} **app** *app-id*]{lang="FR"}

[**[undo posa map]{lang="FR"}**]{#struct_0_x1991_x1755_x1894986223}[ { ]{lang="FR"}[{ ]{lang="DE"}**[default]{lang="FR"}**[ ]{lang="FR"}[\|**destination** *des-code* ]{lang="FR"}[\| ]{lang="DE"}**[source ]{lang="FR"}***[src-code]{lang="FR"}*[ ]{lang="FR"}[} \*]{lang="DE"}[ ]{lang="DE"}[}]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1195921920}

[[无]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_2124931817}[接入映射表项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_695573168}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_222532066}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1497245370}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1498986177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895444978}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_281693833}

[**[default]{lang="EN-US"}**]{#struct_0_x1991_x1755_840539184}[：指定缺省的接入映射表项，即所有未找到匹配项的报文将被发送给指定的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板处理。]{style="font-family:宋体"}

[**[destination]{lang="FR"}**]{#struct_0_x1991_x1755_1669902963}*[ des-code]{lang="FR"}*[：]{style="font-family:宋体"}[POS]{lang="FR"}[报文的]{style="font-family:宋体"}[TPDU]{lang="FR"}[头中的目的地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[是由四个十六进制数字表示的字符]{style="font-family:宋体"}[（]{style="font-family:宋体"}[如]{style="font-family:宋体"}[：]{style="font-family:宋体"}[FFFF]{lang="FR"}[），]{style="font-family:宋体"}[一般用来区分不同的银行。它一般是由业务中心统一分配的。]{style="font-family:宋体"}

[**[source]{lang="FR"}**]{#struct_0_x1991_x1755_718355424}*[ src-code]{lang="FR"}*[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的源地址，是由四个十六进制数字表示的字符（如：]{style="font-family:宋体"}[0001]{lang="EN-US"}[），一般用来区分不同的]{style="font-family:宋体"}[POS]{lang="EN-US"}[机。]{style="font-family:宋体"}

[**[app]{lang="FR"}**]{#struct_0_x1991_x1755_x1895510514}[ ]{lang="FR"}*[app-id]{lang="EN-US"}*[：]{style="font-family:
宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_351742960}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1667879581}[接入设备通过将收到的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的源地址和目的地址与配置的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射关系表项进行匹配，来决定将该报文发送到哪个]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板上去处理。若]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文的源地址、目的地址或者源地址和目的地址的组合与某一个映射关系表项对应，则该报文就被发送给该表项所对应的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板处理；若该报文未找到任何匹配项，则将被发送给缺省的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板处理。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x463694318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1040321551}[POS]{lang="EN-US"}[应用模板可对应多个]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[匹配时其中指定了源地址和目的地址的组合表项匹配优先级最高，缺省映射的优先级最低。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895576050}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[包括缺省]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1237613293}[POS]{lang="EN-US"}[接入映射表项在内，系统最多支持]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895641586}[POS]{lang="EN-US"}[交易过程中修改]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项的目的前置机，不会删除正在使用中的连接，但可能会影响正在进行的]{style="font-family:宋体"}[POS]{lang="EN-US"}[交易。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若应用模板]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1278646961}[ID]{lang="EN-US"}[不存在，可以配置，但不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2033027298}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_539374358}[配置一个]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项，将]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址为]{style="font-family:宋体"}[01f1]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文都发送给应用]{style="font-family:宋体"}[2]{lang="EN-US"}[去处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895182834}

[\[Sysname\] posa map destination 01f1 app 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x81917216}[配置一个缺省的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项，将未能匹配到任何]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入映射表项的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文都发送给]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[去处理。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x69736226}

[\[Sysname\] posa map default app 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1358414681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1115505055}
:::

::: {#-62264939 .myid}
[]{#_Toc404786002}[]{#struct_0_x1991_x1755_859916606}[]{#_Toc358227450}[]{#_Toc336625593}[]{#_Toc193529385}

**POS终端接入 \-- POS终端接入配置命令 \-- posa server enable**

------------------------------------------------------------------------

[**[posa server enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895313906}[命令用来开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入服务。]{style="font-family:宋体"}

[**[undo posa server enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x931904834}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1986138251}

[**[posa server enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1164782976}

[**[undo posa server enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1727225850}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2110004367}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1894920690}[终端接入服务处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1647578443}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x348264442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1147682364}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_661609048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1880024999}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1340295637}

[[要实现]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895444977}[接入，必须先启动]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入服务。若开启服务时部分功能可以配置但不生效（如]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口不可用），管理员通过]{style="font-family:宋体"}**[display posa status]{lang="EN-US"}**[查看状态为]{style="font-family:宋体"}[Error]{lang="EN-US"}[，此时将问题修改后重新使能即可。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_684978360}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895576049}[开启]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_27825248}

[\[Sysname\] posa server enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1895641585}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display posa status]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895182833}
:::

::: {#-39499134 .myid}
[]{#_Toc404786003}[]{#struct_0_x1991_x1755_677597671}[]{#_Toc358227451}[]{#_Toc336625614}[]{#_Toc275956213}

**POS终端接入 \-- POS终端接入配置命令 \-- posa statistics caller-id**

------------------------------------------------------------------------

[**[posa statistics caller-id]{lang="FR"}**]{#struct_0_x1991_x1755_x1423387701}[命令用来创建一个主叫号码统计项，设备将根据该统计项中指定的终端主叫号码对]{style="font-family:宋体"}[POS]{lang="FR"}[机与前置机之间交互的终端报文数进行统计。]{style="font-family:宋体"}

[**[undo posa statistics caller-id]{lang="FR"}**]{#struct_0_x1991_x1755_x1039318782}[命令用来取消指定主叫号码统计项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1712266120}

[**[posa statistics caller-id]{lang="EN-US"}**[ *caller-number*]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895248369}

[**[undo posa statistics caller-id]{lang="EN-US"}***[ caller-number]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1895313905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1335189361}

[[无主叫号码统计项。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_2100962391}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_34024673}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895379441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1519915124}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_16496177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1474424080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1812068617}

[*[caller-number]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1894920689}[：终端主叫号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，仅可以为数字和字母，如]{style="font-family:宋体"}[01012345678]{lang="EN-US"}[。通常意义上的主叫号码都是由数字组成，但是不排除特殊情况使用字母。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1437469736}

[[该统计方式仅适用于通过拨号方式接入的]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1894986225}[终端模板。]{style="font-family:宋体"}

[[重复配置相同则主叫号码统计项不提示错误。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_2002490974}

[[最多支持配置]{style="font-family:宋体"}[64]{lang="EN-US"}]{#struct_0_x1991_x1755_512038892}[条统计项。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1895444980}

[[\# ]{lang="FR"}]{#struct_0_x1991_x1755_x73684559}[创建一个主叫号码统计项，统计主叫号码为]{style="font-family:宋体"}[01012345678]{lang="FR"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[机报文数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1321427944}

[\[Sysname\] posa statistics caller-id 01012345678]{lang="EN-US"}
:::

::: {#-39499122 .myid}
[]{#_Toc404786004}[]{#struct_0_x1991_x1755_1388353468}[]{#_Toc358227452}[]{#_Toc336625615}

**POS终端接入 \-- POS终端接入配置命令 \-- posa statistics caller-ip**

------------------------------------------------------------------------

[**[posa statistics caller-ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895510516}[命令用来创建一个源]{style="font-family:
宋体"}[IP]{lang="EN-US"}[统计项，该统计项中指定了一个终端源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者一个源]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段，设备将根据指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者源]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段对]{style="font-family:宋体"}[POS]{lang="EN-US"}[机与前置机之间交互的终端报文数进行统计。]{style="font-family:宋体"}

[**[undo posa statistics caller-ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_x811056454}[命令用来删除指定的源]{style="font-family:
宋体"}[IP]{lang="EN-US"}[统计项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1860912406}

[**[posa statistics caller-ip ]{lang="EN-US"}***[group-id]{lang="EN-US"}*[ *ip-address ip-mask*]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895576052}

[**[undo posa statistics caller-ip]{lang="EN-US"}***[ group-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1895641588}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x115847547}

[[无源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1280751688}[统计项。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1380016138}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_856907945}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1895182836}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1080882198}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1127117509}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_692778576}

[*[group-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x2016692351}[：统计项编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1991_x1755_x470646272}[：终端源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或源]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段地址，为点分十进制格式。]{style="font-family:宋体"}

[*[ip-mask]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1554334108}[：终端源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或源]{style="font-family:宋体"}[IP]{lang="EN-US"}[网段的子网掩码，为点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x344022229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该统计方式只适用于]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1819027254}[TCP]{lang="EN-US"}[接入方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各源]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1895248372}[IP]{lang="EN-US"}[统计项网段之间可以相互重叠，甚至相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交易时，只要是源]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x505179427}[IP]{lang="EN-US"}[地址与统计项中指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或者源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段匹配的]{style="font-family:宋体"}[POS]{lang="EN-US"}[机交易报文，都会被统计到该统计项，所以一个报文可能会被统计到多个表项中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x159643053}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1730898691}[创建源]{style="font-family:宋体"}[IP]{lang="EN-US"}[统计项]{style="font-family:宋体"}[1]{lang="EN-US"}[，统计源]{style="font-family:宋体"}[IP]{lang="FR"}[地址为]{style="font-family:宋体"}[10.0.1.0/24]{lang="FR"}[网段内的]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的交易报文数。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_314784956}

[\[Sysname\] posa statistics caller-ip 1 10.0.1.0 255.255.255.0]{lang="EN-US"}
:::

::: {#-1906610611 .myid}
[]{#_Toc404786005}[]{#struct_0_x1991_x1755_237458265}[]{#_Toc358227453}[]{#_Toc336625611}

**POS终端接入 \-- POS终端接入配置命令 \-- posa terminal**

------------------------------------------------------------------------

[**[posa terminal]{lang="FR"}**]{#struct_0_x1991_x1755_x1895313908}[命令用来创建]{style="font-family:宋体"}[TCP]{lang="FR"}[接入方式的]{style="font-family:宋体"}[POS]{lang="FR"}[终端模板。]{style="font-family:宋体"}

[**[undo posa terminal]{lang="FR"}**]{#struct_0_x1991_x1755_x1895379444}[命令用来删除指定的]{style="font-family:宋体"}[POS]{lang="FR"}[接入终端模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1923199651}

[**[posa terminal ]{lang="FR"}**]{#struct_0_x1991_x1755_x1894986228}*[terminal-id]{lang="FR"}*[ **type tcp listen-port** *port* ]{lang="FR"}[\[ ]{lang="EN-US"}**[idle-time]{lang="FR"}**[ ]{lang="FR"}*[time]{lang="EN-US"}*[ \]]{lang="EN-US"}

[**[undo posa terminal]{lang="FR"}**]{#struct_0_x1991_x1755_x1895444979}[ *terminal-id*]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1847777774}

[[未配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1017707637}[方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x367167134}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x569356035}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x506340191}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895510515}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1214340981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1122834633}

[*[terminal-id]{lang="FR"}*]{#struct_0_x1991_x1755_815030381}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="FR"}[，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[。]{style="font-family:
宋体"}

[**[type]{lang="FR"}**]{#struct_0_x1991_x1755_x1145118423}[ **tcp**]{lang="FR"}[：创建]{style="font-family:宋体"}[TCP]{lang="FR"}[接入方式的]{style="font-family:宋体"}[POS]{lang="FR"}[终端模板。]{style="font-family:宋体"}

[**[listen-port]{lang="FR"}**]{#struct_0_x1991_x1755_x1611449741}*[ port]{lang="FR"}*[：]{style="font-family:宋体"}[指定监听端口号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。]{style="font-family:宋体"}

[**[idle-time]{lang="FR"}**]{#struct_0_x1991_x1755_1278704209}[ *time*]{lang="FR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[POS]{lang="FR"}[终端模板的空闲超时时间]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:
宋体"}[1440]{lang="FR"}[，]{style="font-family:宋体"}[单位为分钟]{style="font-family:宋体"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0]{lang="FR"}[分钟。]{style="font-family:
宋体"}[0]{lang="EN-US"}[表示对]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的空闲时间没有限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x261393026}

[[POS]{lang="FR"}]{#struct_0_x1991_x1755_x1895182835}[终端模板用于保存]{style="font-family:宋体"}[POS]{lang="FR"}[接入设备与每一个]{style="font-family:宋体"}[POS]{lang="FR"}[终端交互的相关配置信息的的配置信息。对于]{style="font-family:宋体"}[流接入方式或者拨号接入方式的]{style="font-family:
宋体"}[POS]{lang="FR"}[终端模板，在指定]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的接入接口时，系统会自动创建对应的]{style="font-family:宋体"}[POS]{lang="FR"}[终端模板]{style="font-family:宋体"}[。]{style="font-family:宋体"}[对于]{style="font-family:宋体"}[TCP]{lang="FR"}[接入方式，需要手工配置]{style="font-family:宋体"}[POS]{lang="FR"}[终端模板。]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1895248371}[接入方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板上指定的监听端口唯一，不能相互冲突。并且不能修改]{style="font-family:宋体"}[TCP]{lang="EN-US"}[终端的监听端口。]{style="font-family:宋体"}

[[在指定的空闲超时时间内，如果]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1182071022}[机与]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板之间没有报文的交互，则]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板将断开与]{style="font-family:宋体"}[POS]{lang="EN-US"}[机之间的连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x101894900}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1537293230}[创建]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[1]{lang="EN-US"}[，且指定监听端口号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x561278980}

[\[Sysname\] posa terminal 1 type tcp listen-port 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1895313907}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa bind terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_1796978521}
:::

::: {#954384183 .myid}
[]{#_Toc404786006}[]{#struct_0_x1991_x1755_1912910511}[]{#_Toc358227454}[]{#_Toc336625610}

**POS终端接入 \-- POS终端接入配置命令 \-- posa terminal description**

------------------------------------------------------------------------

[**[posa terminal description]{lang="PT-BR"}**]{#struct_0_x1991_x1755_x1407056897}[命令用来配置]{style="font-family:
宋体"}[POS]{lang="PT-BR"}[终端模板的描述信息。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1895379443}**[posa terminal description]{lang="PT-BR"}**[命令用来删除]{style="font-family:宋体"}[POS]{lang="PT-BR"}[终端模板的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x357115710}

[**[posa terminal ]{lang="PT-BR"}**]{#struct_0_x1991_x1755_1472113408}*[terminal-id ]{lang="PT-BR"}***[description ]{lang="PT-BR"}***[text]{lang="FR"}*

[**[undo posa terminal ]{lang="PT-BR"}**]{#struct_0_x1991_x1755_1855498627}*[terminal-id]{lang="PT-BR"}***[ description]{lang="PT-BR"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1894920691}

[[未配置]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1081304912}[POS]{lang="PT-BR"}[终端模板的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_317556543}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1375242942}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1817829757}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x2004516350}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1107767985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_836566615}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_725559482}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[text]{lang="FR"}*]{#struct_0_x1991_x1755_x329361035}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板的描述信息，为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[32]{lang="PT-BR"}[个字符的字符串，区分大小写，合法字符是不为'？'的可打印字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x556305003}

[[允许先配置]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x257643712}[终端模板的描述信息再创建该]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1452436231}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_940431904}[为]{style="font-family:宋体"}[POS]{lang="PT-BR"}[终端模板]{style="font-family:宋体"}[1]{lang="PT-BR"}[配置描述信息为"]{style="font-family:宋体"}[Shopping1]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1506190460}

[\[Sysname\] posa terminal 1 description shopping1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1322676195}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_1996913929}
:::

::: {#1588575456 .myid}
[]{#_Toc404786007}[]{#struct_0_x1991_x1755_x690664259}[]{#_Toc361152884}

**POS终端接入 \-- POS终端接入配置命令 \-- posa tpdu-replace**

------------------------------------------------------------------------

[**[posa]{lang="EN-US"}**[ **tpdu-replace**]{lang="EN-US"}]{#struct_0_x1991_x1755_545192151}[命令用来配置]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[地址替换策略，即将符合匹配条件的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址替换成指定的目的地址，并按新的目的地址查找映射表。]{style="font-family:宋体"}

[**[undo posa tpdu-replace]{lang="EN-US"}**]{#struct_0_x1991_x1755_x852320660}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_570421806}

[**[posa]{lang="EN-US"}**[ **tpdu-replace match terminal** { *terminal-id* \| **any** } **destination** { *des-code* \| **any** } **to** *des-code*]{lang="EN-US"}]{#struct_0_x1991_x1755_x296962055}

[**[undo posa tpdu-replace match terminal]{lang="EN-US"}**[ { *terminal-id* \| **any** } \[ **destination** { *des-code* \| **any** } \]]{lang="EN-US"}]{#struct_0_x1991_x1755_2038219096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x497207138}

[[不对]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_710384155}[报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址进行替换。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_472135155}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1070165163}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1126334448}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1093948786}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_553220551}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1060027730}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_1717208074}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[。将该终端发送的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址替换成指定的目的地址。]{style="font-family:宋体"}

[**[terminal any]{lang="EN-US"}**]{#struct_0_x1991_x1755_922473849}[：任意]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[。配置该参数表示，所有终端发送的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文，都将进行地址替换。]{style="font-family:宋体"}

[**[destination ]{lang="EN-US"}***[des-code]{lang="EN-US"}*]{#struct_0_x1991_x1755_689305192}**[：]{style="font-family:宋体"}**[POS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址。如果]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址跟所配置的]{style="font-family:宋体"}*[des-code]{lang="EN-US"}*[相匹配，则将此地址替换成所需的目的地址。]{style="font-family:宋体"}

[**[destination any]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1740257649}**[：]{style="font-family:宋体"}**[任意的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址]{style="font-family:宋体"}[。配置该参数表示，所有符合]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[匹配条件的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址将替换成指定的目的地址。]{style="font-family:宋体"}

[**[to]{lang="EN-US"}***[ des-code]{lang="EN-US"}*]{#struct_0_x1991_x1755_x643610092}**[：]{style="font-family:宋体"}**[需要替换成的目的地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x488697448}

[[通过多次执行本命令可以配置多条]{style="font-family:宋体"}[TPDU]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066281032}[地址替换策略。按照优先级由高到低的顺序，]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[地址替换策略的匹配顺序为：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置了]{style="font-family:宋体"}*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_666855954}[和]{style="font-family:宋体"}*[des-code]{lang="EN-US"}*[的策略；]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置了]{style="font-family:宋体"}*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x759888576}[和]{style="font-family:宋体"}**[destination any]{lang="EN-US"}**[的策略；]{style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置了]{style="font-family:宋体"}**[terminal any]{lang="EN-US"}**]{#struct_0_x1991_x1755_x988637213}[和]{style="font-family:宋体"}*[des-code]{lang="EN-US"}*[的策略；]{style="font-family:宋体"}

[[(4)[      ]{style="font:7.0pt "}]{lang="EN-US"}[配置了]{style="font-family:宋体"}**[terminal any]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1378573572}[和]{style="font-family:宋体"}**[destination any]{lang="EN-US"}**[的策略。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x769024163}[终端模板给]{style="font-family:宋体"}[POS]{lang="EN-US"}[机返回回应消息时，会恢复原始的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[头中的目的地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1278638673}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x330526746}[将终端]{style="font-family:宋体"}[1]{lang="EN-US"}[发送的目的地址为]{style="font-family:宋体"}[0002]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[报文中的目的地址替换为]{style="font-family:宋体"}[0003]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_147781954}

[\[Sysname\] posa tpdu-replace match terminal 1 destination 0002 to 0003]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x287445268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tpdu-change]{lang="EN-US"}**]{#struct_0_x1991_x1755_x472544265}
:::

::: {#71128767 .myid}
[]{#_Toc404786008}[]{#struct_0_x1991_x1755_x1066346568}[]{#_Toc373766259}[]{#_Toc371586362}

**POS终端接入 \-- POS终端接入配置命令 \-- posa trade-limit tcp**

------------------------------------------------------------------------

[**[posa trade-limit tcp]{lang="EN-US"}**]{#struct_0_x1991_x1755_1362202247}[命令用来设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[并发交易数上限。]{style="font-family:宋体"}

[**[undo posa trade-limit tcp]{lang="EN-US"}**]{#struct_0_x1991_x1755_68435272}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1587549144}

[**[posa trade-limit tcp ]{lang="FR"}**]{#struct_0_x1991_x1755_x1437478298}*[limit-value]{lang="FR"}*

[**[undo posa trade-limit tcp]{lang="FR"}**]{#struct_0_x1991_x1755_x805347371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1096659239}

[[不对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1995915971}[连接]{style="font-family:宋体"}[的并发交易数做限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_973046378}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x552360239}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_361230916}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_560934012}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1066412104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1099993154}

[*[limit-value]{lang="SV"}*]{#struct_0_x1991_x1755_2115124000}[：每条]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的]{style="font-family:宋体"}[并发交易数上限值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不对]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接的并发交易数做限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x96744785}

[[配置了]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x368225916}[连接的并发交易数上限后，当设备收到的某个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接上的并发交易数超过指定的上限时，会将超出限制的交易报文丢弃。同时，如果设备开启了关于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接并发交易数超过上限的告警功能，还会生成相应的告警信息。]{style="font-family:宋体"}

[[需要注意的是，为了避免在大交易流量时频繁生成告警信息，]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x15702104}[终端接入模块只在某个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接上的并发交易数达到上限后第一次收到新交易报文时生成告警信息。此后，在并发交易数低于上限的]{style="font-family:宋体"}[90%]{lang="EN-US"}[前不再生成告警信息，当并发交易数低于上限的]{style="font-family:宋体"}[90%]{lang="EN-US"}[后又重新超出上限时才会再次生成告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1156285178}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1142077194}[配置每条]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接]{style="font-family:宋体"}[的并发交易数上限为]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_516095174}

[\[Sysname\] posa trade-limit tcp 1024]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1990609320}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap enable posa]{lang="EN-US"}**]{#struct_0_x1991_x1755_528098547}
:::

::: {#-1640501184 .myid}
[]{#_Toc404786009}[]{#struct_0_x1991_x1755_1840426089}[]{#_Toc373766260}[]{#_Toc371586363}

**POS终端接入 \-- POS终端接入配置命令 \-- posa trade-timeout**

------------------------------------------------------------------------

[**[posa trade-timeout]{lang="EN-US"}**]{#struct_0_x1991_x1755_188057528}[命令用来设定每笔交易的超时时间。]{style="font-family:宋体"}

[**[undo posa trade-timeout]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1421230626}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1066477640}

[**[posa]{lang="FR"}**]{#struct_0_x1991_x1755_273568291}**[ ]{lang="FR"}[trade-timeout ]{lang="FR"}***[timeout-value]{lang="FR"}*

[**[undo posa trade-timeout]{lang="FR"}**]{#struct_0_x1991_x1755_x1533283824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_177967269}

[[每笔交易的超时时间为]{style="font-family:宋体"}[240]{lang="EN-US"}]{#struct_0_x1991_x1755_x2073813501}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x673002254}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1315302093}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_562961419}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_559173934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1440928032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1173896721}

[*[timeout-value]{lang="SV"}*]{#struct_0_x1991_x1755_58388135}[：每笔交易的超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1498315117}

[[设备从]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_2067510946}[终端收到交易报文后，如果在指定的时间内没有收到银行前置机的应答，则认为交易超时。超时之后再收到此交易的应答，设备会将报文丢弃。]{style="font-family:宋体"}

[[需要注意的是，在网络拥塞的情况下，不能将交易超时时间配置的太小，否则可能会出现内部交易号串号的情况，即设备将已超时交易的内部交易号分配给了新交易，之后收到已超时交易的应答会被误认为是对新交易的应答。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x616544398}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1066543176}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1025368943}[配置每笔交易的超时时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1056133282}

[\[Sysname\] posa trade-timeout 120]{lang="EN-US"}
:::

::: {#686121758 .myid}
[]{#_Toc404786010}[]{#struct_0_x1991_x1755_1321859507}[]{#_Toc358227455}[]{#_Toc336625623}

**POS终端接入 \-- POS终端接入配置命令 \-- reset fcm statistics**

------------------------------------------------------------------------

[**[reset fcm statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329426571}[命令用来清除指定]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1029707815}

[**[reset fcm statistics]{lang="EN-US"}**[ \[ **interface** **fcm** { *interface-number* \| *interface-number:setnumber*.*subnumber* } \]]{lang="EN-US"}]{#struct_0_x1991_x1755_158318309}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x184024402}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1134302834}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329492107}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x192746866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1299837060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_807791711}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[fcm ]{lang="EN-US"}**[{ *interface-number* \| *interface-number:setnumber*.*subnumber* }]{lang="EN-US"}]{#struct_0_x1991_x1755_x81226051}[：清除指定接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[表示物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口编号，用来清除物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息；]{style="font-family:宋体"}*[interface-number:setnumber]{lang="EN-US"}*[.*subnumber*]{lang="EN-US"}[表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[子接口的编号，用来]{style="font-family:宋体"}[清除指定通道化]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口下子接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息]{style="font-family:宋体"}[。如果不指定该参数，则清除所有物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口、通道化]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的子接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1209085446}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1028574752}[清除所有物理]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口、通道化]{style="font-family:宋体"}[FCM]{lang="EN-US"}[接口的子接口的]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset fcm statistics]{lang="EN-US"}]{#struct_0_x1991_x1755_x319764741}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2094553816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display fcm statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_1953093240}
:::

::: {#-139626728 .myid}
[]{#_Toc404786011}[]{#struct_0_x1991_x1755_x329557643}[]{#_Toc358227456}[]{#_Toc336625624}

**POS终端接入 \-- POS终端接入配置命令 \-- reset posa connection terminal**

------------------------------------------------------------------------

[**[reset posa connection terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329098891}[命令用来断开设备与]{style="font-family:
宋体"}[POS]{lang="EN-US"}[机之间的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1425889981}

[**[reset posa connection]{lang="EN-US"}[ terminal]{lang="EN-US"}**[ { **all** \| **destination-ip** *ip-addr2* \| **destination-port** *port-number* \| **source-ip** *ip-addr1* }]{lang="EN-US"}]{#struct_0_x1991_x1755_x329164427}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2080625049}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1290059254}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x308396227}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x329229963}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1018422749}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1649393499}

[**[all]{lang="EN-US"}**]{#struct_0_x1991_x1755_1430835028}[：断开设备与所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[机之间的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[destination-ip]{lang="EN-US"}**[ *ip-addr2*]{lang="EN-US"}]{#struct_0_x1991_x1755_x574632690}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[destination-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x1991_x1755_x329295499}[：目的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source-ip]{lang="EN-US"}**[ *ip-addr1*]{lang="EN-US"}]{#struct_0_x1991_x1755_621585116}[：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1153135627}

[[本命令可以根据用户指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1991_x1755_x328902283}[地址、目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和目的端口号断开指定的单条或多条符合条件的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[执行此命令行后会显示已断开的匹配的连接数。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1001777915}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_247038299}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x329361034}[断开所有]{style="font-family:宋体"}[POS]{lang="EN-US"}[机的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[\<Sysname\> reset posa connection terminal all]{lang="EN-US"}]{#struct_0_x1991_x1755_x556370539}

[100 connections have been deleted.]{lang="EN-US"}
:::

::: {#1942734773 .myid}
[]{#_Toc404786012}[]{#struct_0_x1991_x1755_x683675068}[]{#_Toc358227457}[]{#_Toc336625625}[]{#_Toc194748121}

**POS终端接入 \-- POS终端接入配置命令 \-- reset posa statistics**

------------------------------------------------------------------------

[**[reset posa statistics]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329426570}[命令用来清空]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板或]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的相关统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1029642279}

[**[reset posa statistics]{lang="EN-US"}**[ \[ **app** \[ *app-id* \] \| **terminal** \[ *terminal-id* \] \]]{lang="EN-US"}]{#struct_0_x1991_x1755_x1400365875}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x991172350}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_1263090793}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1835881411}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_344235895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_45408200}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1527434386}

[*[app-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x329492106}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[terminal-id]{lang="EN-US"}*]{#struct_0_x1991_x1755_x329557642}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端模板]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2103931742}

[[本命令用来将]{style="font-family:宋体"}**[display posa statistics app]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329164426}[和]{style="font-family:宋体"}**[display posa statistics terminal]{lang="EN-US"}**[两条命令显示的统计信息清理，从零开始重新对报文进行记数。]{style="font-family:宋体"}

[[复位不存在的应用的统计信息或者复位不存在的终端的统计信息不提示错误。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x2080690585}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_667201132}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x329229962}[将显示信息记数器清零。]{style="font-family:宋体"}

[[\<Sysname\> reset posa statistics]{lang="EN-US"}]{#struct_0_x1991_x1755_x1018488285}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1104373782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display posa statistics app]{lang="EN-US"}**]{#struct_0_x1991_x1755_1377299640}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display posa statistics terminal]{lang="EN-US"}**]{#struct_0_x1991_x1755_1187650522}
:::

::: {#-1342011675 .myid}
[]{#_Toc404786013}[]{#struct_0_x1991_x1755_268138286}[]{#_Toc358227458}[]{#_Toc336625616}[]{#_Toc275956214}

**POS终端接入 \-- POS终端接入配置命令 \-- snmp-agent trap enable posa**

------------------------------------------------------------------------

[**[snmp-agent trap enable posa]{lang="EN-US"}**]{#struct_0_x1991_x1755_x328836746}[命令用来在全局下开启]{style="font-family:
宋体"}[POS]{lang="EN-US"}[终端接入的告警功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[snmp-agent trap enable posa]{lang="EN-US"}**]{#struct_0_x1991_x1755_x328902282}[命令用来在全局下关闭]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1001712379}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable posa** \[ **app-state-change** \| **fcm-connection-exceed** \| **fcm-link-failure** \| **fcm-physical-failure** \| **server-state-change** \| **tcp-connection-exceed** ]{lang="EN-US"}]{#struct_0_x1991_x1755_1411922522}[｜]{style="font-family:宋体"} **[tcp-trade-exceed]{lang="EN-US"}**[ \| **terminal-hangup** \] \*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable posa** \[ **app-state-change** \| **fcm-connection-exceed** \| **fcm-link-failure** \| **fcm-physical-failure** \| **server-state-change** \| **tcp-connection-exceed** ]{lang="EN-US"}]{#struct_0_x1991_x1755_1281694406}[｜]{style="font-family:宋体"} **[tcp-trade-exceed]{lang="EN-US"}**[ \| **terminal-hangup** \] \*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329361037}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x556436075}[终端接入告警功能在全局下处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1306146541}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x114750203}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_687002304}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1160279015}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1010724697}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1036975534}

[**[app-state-change]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329426573}[：表示]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板状态切换的告警信息。]{style="font-family:宋体"}

[**[fcm-connection-exceed]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1065691208}[：表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[拨号接入方式并发连接数超过阈值的告警信息。]{style="font-family:宋体"}

[**[fcm-link-failure]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329492109}[：表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[链路层协商失败的告警信息。]{style="font-family:宋体"}

[**[fcm-physical-failure]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329557645}[：表示]{style="font-family:宋体"}[FCM]{lang="EN-US"}[物理层协商失败的告警信息。]{style="font-family:宋体"}

[**[server-state-change]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2103604062}[：表示]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入服务状态切换的告警信息。]{style="font-family:宋体"}

[**[tcp-connection-exceed]{lang="EN-US"}**]{#struct_0_x1991_x1755_x121709368}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入方式并发连接数超过阈值的告警信息。]{style="font-family:宋体"}

[**[tcp-trade-exceed]{lang="FR"}**]{#struct_0_x1991_x1755_874715884}[：表示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的并发交易数超过上限的告警信息。]{style="font-family:宋体"}

[**[terminal-hangup]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329098893}[：表示终端自动挂机的告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1426021053}

[[开启]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1035710854}[终端接入模块告警功能后，系统触发相应事件后会生成指定类型的告警信息。通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。]{style="font-family:宋体"}

[[有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x1991_x1755_340327115}["。]{style="font-family:宋体"}

[[不指定可选参数时，表示开启]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1991_x1755_x329164429}[关闭所有类型的告警功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2081280409}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1226783631}[关闭]{style="font-family:宋体"}[FCM]{lang="EN-US"}[物理层协商失败的]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x329229965}

[\[Sysname\] undo snmp-agent trap enable posa fcm-physical-failure]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1065756744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa connection-threshold]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1846266843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[posa trade-limit tcp]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1660366934}
:::

::: {#2050190574 .myid}
[]{#_Toc404786014}[]{#struct_0_x1991_x1755_x1018553821}[]{#_Toc358227459}[]{#_Toc336625599}[]{#_Toc193529390}

**POS终端接入 \-- POS终端接入配置命令 \-- source ip**

------------------------------------------------------------------------

[**[source ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_150626913}[命令用来配置绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源地址。]{style="font-family:宋体"}

[**[undo source ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_901266845}[命令用来取消对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_601737054}

[**[source ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1991_x1755_x771430655}

[**[undo source ip]{lang="EN-US"}**]{#struct_0_x1991_x1755_x335281533}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1418227027}

[[未配置绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_303856128}[连接的源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329295501}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1716542747}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1323442724}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1477559090}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1865082118}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1619069256}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1991_x1755_1367634108}[：]{style="font-family:宋体"}[与]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接绑定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须与前置机之间路由可达，且为非环回的单播]{style="font-family:宋体"}[IPV4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x180804106}

[[对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x2126571558}[方式连接的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板，缺省情况下设备以]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板接入的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。这样会暴露设备上]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板接入的接口的真实]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，为了满足一定的安全需求，可以通过在]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板上配置源地址绑定功能，指定一个特殊的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[修改绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x328836749}[连接的源地址会导致该模板下已经建立的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_239736994}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_654324242}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，删除现有的长连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x946193190}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] source ip 1.1.1.1]{lang="EN-US"}

[Connections for the application have been reset.]{lang="EN-US"}
:::

::: {#-1015706045 .myid}
[]{#_Toc404786015}[]{#struct_0_x1991_x1755_x391996375}[]{#_Toc358227460}[]{#_Toc336625600}

**POS终端接入 \-- POS终端接入配置命令 \-- source port**

------------------------------------------------------------------------

[**[source port]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1366159429}[命令用来配置绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源端口号，即与前置机建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时，只能使用指定的源端口号。]{style="font-family:宋体"}

[**[undo source port]{lang="EN-US"}**]{#struct_0_x1991_x1755_1424442129}[命令用来取消对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源端口号的绑定。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1363141484}

[**[source port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x1991_x1755_540882890}

[**[undo source port]{lang="EN-US"}**]{#struct_0_x1991_x1755_x328902285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1001908987}

[[未绑定源端口号，与前置机建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1021822883}[连接时将使用系统随机分配的一个未被占用的端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x414573546}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_222655665}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x192594353}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x196216713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x41480520}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_219820274}

[*[port-number]{lang="EN-US"}*]{#struct_0_x1991_x1755_x329361036}[：与]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接绑定的源端口号，取值范围为]{style="font-family:宋体"}[4000]{lang="EN-US"}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x556501611}

[[有些前置机要求设备必须以一个特定的源端口发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1079870003}[连接，可通过本命令指定一个特殊的端口号作为向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的源端口号。]{style="font-family:宋体"}

[[短连接模式下，也支持配置绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x261241121}[连接的源端口号，但此时，此]{style="font-family:宋体"}[APP]{lang="EN-US"}[最多创建一条与前置机的连接，所以使用该]{style="font-family:宋体"}[APP]{lang="EN-US"}[并发的交易会失败。]{style="font-family:宋体"}

[[修改绑定]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x369650373}[连接的源端口号会删除该模板下已经建立的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[指定的源端口不能和终端的监听端口重复，不能和其它应用绑定的源端口重复。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x1513741945}

[[若指定源端口与系统其它进程端口重复，可配置，但该应用不生效，通过]{style="font-family:宋体"}**[display posa status]{lang="EN-US"}**]{#struct_0_x1991_x1755_x560183675}[可看到当前系统已经占用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_833191566}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x239474486}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的源端口号为]{style="font-family:宋体"}[4001]{lang="EN-US"}[，删除已经存在的连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x329426572}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] source port 4001]{lang="EN-US"}

[Connections for the application have been reset.]{lang="EN-US"}
:::

::: {#1132039522 .myid}
[]{#_Toc193529374}[]{#_Toc404786016}[]{#struct_0_x1991_x1755_1029511207}[]{#_Toc358227461}[]{#_Toc336625601}[]{#_Toc193529392}

**POS终端接入 \-- POS终端接入配置命令 \-- tcp keepalive**

------------------------------------------------------------------------

[**[tcp keepalive]{lang="EN-US"}**]{#struct_0_x1991_x1755_x329492108}[命令用来设置发送]{style="font-family:宋体"}[TCP]{lang="EN-US"}[协议栈]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文的相关参数。]{style="font-family:宋体"}

[**[undo tcp keepalive]{lang="EN-US"}**]{#struct_0_x1991_x1755_x192812402}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1437023603}

[**[tcp]{lang="EN-US"}**[ **keepalive** **interval** *time* **count** *counts*]{lang="EN-US"}]{#struct_0_x1991_x1755_x329557644}

[**[undo tcp]{lang="EN-US"}**[ **keepalive**]{lang="EN-US"}]{#struct_0_x1991_x1755_x2103538526}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_968597207}

[[设备通过向前置机发送]{style="font-family:宋体"}[keepalive]{lang="EN-US"}]{#struct_0_x1991_x1755_1749331249}[报文，来保持该]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应连接的连通性。]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[TCP keepalive]{lang="EN-US"}]{#struct_0_x1991_x1755_x756631401}[报文的周期为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，当连续发送]{style="font-family:宋体"}[3]{lang="EN-US"}[次]{style="font-family:宋体"}[TCP keepalive]{lang="EN-US"}[报文没有得到回应时设备断开与该]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的银行前置机的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1615757777}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_573027869}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x970872519}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1361777608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x329098892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1425955517}

[**[interval]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1991_x1755_1304003501}[：表示]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[7200]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**[ *counts*]{lang="EN-US"}]{#struct_0_x1991_x1755_12103503}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送次数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1987119765}

[[修改后参数会立刻生效。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_982888502}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1492841633}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_192275211}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[keepalive]{lang="EN-US"}[报文发送间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒，发送次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1075503946}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] tcp keepalive interval 100 count 4]{lang="EN-US"}
:::

::: {#1624519445 .myid}
[]{#_Toc404786017}[]{#struct_0_x1991_x1755_x329164428}[]{#_Toc358227462}[]{#_Toc336625602}

**POS终端接入 \-- POS终端接入配置命令 \-- tcp linking-time**

------------------------------------------------------------------------

[**[tcp linking-time]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2081345945}[命令用来设置向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求的超时时间，即该]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的连接发起时处于]{style="font-family:宋体"}[Linking]{lang="EN-US"}[状态的最大时间。]{style="font-family:宋体"}

[**[undo tcp linking-time]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1875895354}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1974312787}

[**[tcp linking-time]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1991_x1755_x1561385804}

[**[undo tcp linking-time]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2074540786}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x449176491}

[[允许向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_834098466}[连接的超时时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x660698080}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_2100853941}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329229964}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1018619357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1423341876}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1973203588}

[*[time]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1890539044}[：允许]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板处于]{style="font-family:宋体"}[Linking]{lang="EN-US"}[状态的最大时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x303359184}

[[设备向前置机发起]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_902826620}[连接的时间若超过设置的最大值，则取消此次]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接请求，此次交易失败。]{style="font-family:宋体"}

[[修改后的配置仅对新发起的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x987600780}[连接生效。]{style="font-family:宋体"}

[[该配置同样用于设备等待银行前置机应答]{style="font-family:宋体"}[AM POS]{lang="EN-US"}]{#struct_0_x1991_x1755_396117300}[机的主叫号码协商报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x729372420}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x329295500}[配置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接状态时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1716477211}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] tcp linking-time 10]{lang="EN-US"}
:::

::: {#-985790281 .myid}
[]{#_Toc404786018}[]{#struct_0_x1991_x1755_300423740}[]{#_Toc358227463}[]{#_Toc343694228}[]{#_Toc342660224}

**POS终端接入 \-- POS终端接入配置命令 \-- threshold answer-tone**

------------------------------------------------------------------------

[**[threshold answer-tone]{lang="EN-US"}**]{#struct_0_x1991_x1755_x328836748}[命令用来设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[发送应答音能量增益。]{style="font-family:宋体"}

[**[undo threshold answer-tone]{lang="EN-US"}**]{#struct_0_x1991_x1755_239802530}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1612229117}

[**[threshold answer-tone]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1991_x1755_x328902284}*[answertonetime]{lang="NO-BOK"}*

[**[undo threshold answer-tone]{lang="EN-US"}**]{#struct_0_x1991_x1755_1001843451}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1031253578}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x329361039}[发送应答音的能量增益缺省值的取值情况与设备型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x557091435}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_2065464588}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_666311219}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1945690332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x1857249191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1033071839}

[*[answertometime]{lang="NO-BOK"}*]{#struct_0_x1991_x1755_606121134}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[发送应答音的能量增益]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围是]{style="font-family:宋体"}[1]{lang="NO-BOK"}[～]{style="font-family:宋体"}[42]{lang="NO-BOK"}[，]{style="font-family:宋体"}[单位为]{style="font-family:宋体"}[-dBm]{lang="NO-BOK"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_163162788}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x292899057}[设置]{style="font-family:宋体"}[FCM2/1/0]{lang="EN-US"}[下]{style="font-family:宋体"}[Modem]{lang="EN-US"}[发送应答音能量增益为]{style="font-family:宋体"}[-41dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x329426575}

[\[Sysname\] interface fcm 2/1/0]{lang="NO-BOK"}

[\[Sysname--Fcm2/1/0\] threshold answer-tone 41]{lang="EN-US"}
:::

::: {#352863825 .myid}
[]{#_Toc404786019}[]{#struct_0_x1991_x1755_1029445671}[]{#_Toc358227464}[]{#_Toc343694229}[]{#_Toc342660225}

**POS终端接入 \-- POS终端接入配置命令 \-- threshold rlsdoff**

------------------------------------------------------------------------

[**[threshold rlsdoff]{lang="EN-US"}**]{#struct_0_x1991_x1755_1369888136}[命令用来设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的接收信号门限值下限。]{style="font-family:宋体"}

[**[undo threshold rlsdoff]{lang="EN-US"}**]{#struct_0_x1991_x1755_2023665133}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1724266033}

[**[threshold rlsdoff ]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1262270281}*[rlsdofftime]{lang="NO-BOK"}*

[**[undo threshold rlsdoff]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1667511446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1990294284}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x1896094731}[协商的接收信号门限值下限值为]{style="font-family:宋体"}[-48dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329492111}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x192353651}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x918370312}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_106615357}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_2101326209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1577779196}

[*[rlsdofftime]{lang="EN-US"}*]{#struct_0_x1991_x1755_x118416583}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[接收信号门限值下限，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[75]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[-dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_385661915}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1463962897}[设置]{style="font-family:宋体"}[FCM2/1/0]{lang="EN-US"}[接口下]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的接收信号门限值下限为]{style="font-family:宋体"}[-74dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x329557647}

[\[Sysname\] interface fcm 2/1/0]{lang="NO-BOK"}

[\[Sysname--Fcm2/1/0\] threshold rlsdoff 74]{lang="NO-BOK"}
:::

::: {#-1478378763 .myid}
[]{#_Toc404786020}[]{#struct_0_x1991_x1755_x2103735134}[]{#_Toc358227465}[]{#_Toc343694230}[]{#_Toc342660226}

**POS终端接入 \-- POS终端接入配置命令 \-- threshold rlsdon**

------------------------------------------------------------------------

[**[threshold rlsdon]{lang="EN-US"}**]{#struct_0_x1991_x1755_1466599433}[命令用来设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的接收信号门限值上限。]{style="font-family:宋体"}

[**[undo threshold rlsdon]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2051333397}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1978258334}

[**[threshold rlsdon ]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1101033362}*[rlsdontime]{lang="NO-BOK"}*

[**[undo threshold rlsdon]{lang="EN-US"}**]{#struct_0_x1991_x1755_1944636483}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1288538106}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_957075959}[协商的接收信号门限值上限值为]{style="font-family:宋体"}[-43dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2091501231}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x329098895}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1426152125}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1814850878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_258409506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1508986383}

[*[rlsdontime]{lang="EN-US"}*]{#struct_0_x1991_x1755_x556709252}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[接收信号门限值上限，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[75]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[-dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1488510229}

[[\# ]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x2060797181}[设置]{style="font-family:宋体"}[FCM2/1/0]{lang="NO-BOK"}[协商的接收信号门限值上限为]{style="font-family:宋体"}[-73dBm]{lang="NO-BOK"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_1061751873}

[\[Sysname\] interface fcm 2/1/0]{lang="NO-BOK"}

[\[Sysname--Fcm2/1/0\] threshold rlsdon 73]{lang="NO-BOK"}
:::

::: {#-1684615878 .myid}
[]{#_Toc404786021}[]{#struct_0_x1991_x1755_x329164431}[]{#_Toc358227466}[]{#_Toc343694231}[]{#_Toc342660227}

**POS终端接入 \-- POS终端接入配置命令 \-- threshold txpower**

------------------------------------------------------------------------

[**[threshold txpower]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2080756120}[命令用来设置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[协商的发送能量增益的大小。]{style="font-family:宋体"}

[**[undo threshold txpower]{lang="EN-US"}**]{#struct_0_x1991_x1755_1629482069}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2068061327}

[**[threshold txpower ]{lang="EN-US"}**]{#struct_0_x1991_x1755_386055144}*[txpowertime]{lang="NO-BOK"}*

[**[undo threshold txpower]{lang="EN-US"}**]{#struct_0_x1991_x1755_1063895110}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1939105334}

[[Modem]{lang="EN-US"}]{#struct_0_x1991_x1755_x19508274}[协商的发送能量增益值为]{style="font-family:宋体"}[-10dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_2047622151}

[[FCM]{lang="NO-BOK"}]{#struct_0_x1991_x1755_x329229967}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1018684893}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1851806610}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1897556070}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x2033893061}

[*[txpowertime]{lang="EN-US"}*]{#struct_0_x1991_x1755_433357152}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[信号发送的能量增益，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[42]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[-dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1166576546}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_1486819015}[设置]{style="font-family:宋体"}[FCM2/1/0]{lang="EN-US"}[协商的发送能量增益的大小为]{style="font-family:宋体"}[-40dBm]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x1991_x1755_602621484}

[\[Sysname\] interface fcm 2/1/0]{lang="NO-BOK"}

[\[Sysname--Fcm2/1/0\] threshold txpower 40]{lang="EN-US"}
:::

::: {#-1802642453 .myid}
[]{#_Toc404786022}[]{#struct_0_x1991_x1755_x1719377017}

**POS终端接入 \-- POS终端接入配置命令 \-- timer auto-connect**

------------------------------------------------------------------------

[**[timer auto-connect]{lang="EN-US"}**]{#struct_0_x1991_x1755_x499657213}[命令用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板自动建立连接的时间间隔。]{style="font-family:宋体"}

[**[undo timer auto-connect]{lang="EN-US"}**]{#struct_0_x1991_x1755_1009506338}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_845941884}

[**[timer auto-connect ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x1991_x1755_x316546294}

[**[undo timer auto-connect]{lang="EN-US"}**]{#struct_0_x1991_x1755_x556577603}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x266943956}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x2122661544}[应用模板自动建立连接的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1918732521}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x1431889008}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_606221811}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_856789294}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_30562198}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x959862130}

[*[interval]{lang="EN-US"}*]{#struct_0_x1991_x1755_x840824360}[：]{style="font-family:宋体"}[长连接模式的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板自动建立连接的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x988266652}

[[只有长连接模式的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_1056560505}[类型的]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板才支持该配置。]{style="font-family:宋体"}

[[配置该命令后，当]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x207739794}[应用模板与前置机之间没有建立可复用的长连接前，设备会以]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[为时间间隔，周期性地向前置机主动发起连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_500632321}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x2096128401}[设置自动建立连接的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x509523436}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] timer auto-connect 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1950842024}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-connect enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x690079019}
:::

::: {#-1788350490 .myid}
[]{#_Toc404786023}[]{#struct_0_x1991_x1755_x329295503}[]{#_Toc358227467}[]{#_Toc336625605}

**POS终端接入 \-- POS终端接入配置命令 \-- timer hello**

------------------------------------------------------------------------

[**[timer hello]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1716673819}[用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板发送握手报文的间隔时间。]{style="font-family:宋体"}

[**[undo timer hello]{lang="EN-US"}**]{#struct_0_x1991_x1755_125419294}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_214907840}

[**[timer hello]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1991_x1755_447470637}

[**[undo timer hello]{lang="EN-US"}**]{#struct_0_x1991_x1755_1308220428}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x265018326}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1764916106}[应用模板发送握手报文间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_31002182}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x980436799}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x328836751}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_239212705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_1654440033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_309929103}

[*[interval]{lang="EN-US"}*]{#struct_0_x1991_x1755_x1543972017}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板发送握手报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1256073143}

[[当开启]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x704723132}[应用模板握手功能时，设备以]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[为]{style="font-family:宋体"}[时间间隔周期性地向前置机发送握手报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1042580250}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x1032004153}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板发送握手报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x328902287}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] timer hello 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1002040059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello enable]{lang="EN-US"}**]{#struct_0_x1991_x1755_x285858835}
:::

::: {#1166776051 .myid}
[]{#_Toc404786024}[]{#struct_0_x1991_x1755_1289134231}[]{#_Toc358227468}[]{#_Toc336625604}

**POS终端接入 \-- POS终端接入配置命令 \-- timer quiet**

------------------------------------------------------------------------

[**[timer quiet]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1828173378}[用来设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的静默时间。]{style="font-family:宋体"}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_x1991_x1755_2075795561}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x765426114}

[**[timer quiet]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x1991_x1755_434822374}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1605911938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x366390142}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_x329361038}[应用模板的静默时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x557156971}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_1285437024}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1510615871}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x723358248}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x453532182}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1747192124}

[*[interval]{lang="EN-US"}*]{#struct_0_x1991_x1755_643979906}[：]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的静默时间，范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x14801206}

[[对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1991_x1755_x1086576846}[类型的前置机，当]{style="font-family:宋体"}[POS]{lang="EN-US"}[机发起交易时，若设备尝试连接的前置机无响应，则将此前置机设置为]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[状态，并开启静默定时器，在此期间，此前置机保持]{style="font-family:宋体"}[Blocked]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[修改后的配置会立即生效，对已经处于静默状态的前置机重新计时。]{style="font-family:宋体"}]{#struct_0_x1991_x1755_x329426574}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1029380135}

[[\#]{lang="EN-US"}]{#struct_0_x1991_x1755_x998099962}[设置]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板的静默时间为]{style="font-family:宋体"}[500]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_1507199948}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] timer quiet 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1494598335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[backup app]{lang="EN-US"}**]{#struct_0_x1991_x1755_1393024570}
:::

::: {#5127582 .myid}
[]{#_Toc404786025}[]{#struct_0_x1991_x1755_464333598}[]{#_Toc358227469}[]{#_Toc336625603}

**POS终端接入 \-- POS终端接入配置命令 \-- tpdu-change**

------------------------------------------------------------------------

[**[tpdu-change]{lang="EN-US"}**]{#struct_0_x1991_x1755_347066602}[命令用来配置]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[地址的更改策略，即设备向该]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板对应的前置机转发终端报文时，对报文]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[地址的更改策略。]{style="font-family:宋体"}

[**[undo tpdu-change]{lang="EN-US"}**]{#struct_0_x1991_x1755_x1179326357}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329492110}

[**[tpdu-change]{lang="FR"}**]{#struct_0_x1991_x1755_x192288115}[ { **destination** \| **source** }]{lang="FR"}

[**[undo tpdu-change]{lang="FR"}**]{#struct_0_x1991_x1755_1041203370}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x716320898}

[[仅允许修改]{style="font-family:宋体"}[TPDU]{lang="EN-US"}]{#struct_0_x1991_x1755_x609299886}[源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_1513622058}

[[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_156048297}[应用模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_63978620}

[[network-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x970694947}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1991_x1755_x943205071}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x329557646}

[**[destination]{lang="EN-US"}**]{#struct_0_x1991_x1755_x2103669598}[：修改转发给前置机的终端报文的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[目的地址。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_x1991_x1755_61936112}[：修改转发给前置机的终端报文的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[源地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_844419946}

[[不同的前置机对可更改的]{style="font-family:宋体"}[TPDU]{lang="EN-US"}]{#struct_0_x1991_x1755_x1323469065}[地址字段的要求不同，要么仅允许更改]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[源地址，要么仅允许更改]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[目的地，因此需要根据前置机的要求来配置设备对于]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[地址的更改策略。]{style="font-family:宋体"}

[[对于非透传长连接，修改地址更改策略会删除该]{style="font-family:宋体"}[POS]{lang="EN-US"}]{#struct_0_x1991_x1755_833898428}[应用模板下的所有连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1991_x1755_x1203282601}

[[\# ]{lang="EN-US"}]{#struct_0_x1991_x1755_x398886869}[指定向]{style="font-family:宋体"}[POS]{lang="EN-US"}[应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的前置机转发终端报文时，修改其]{style="font-family:宋体"}[TPDU]{lang="EN-US"}[目的地址，应用模板]{style="font-family:宋体"}[1]{lang="EN-US"}[为非透传长连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1991_x1755_x1552871459}

[\[Sysname\] posa app 1 type tcp]{lang="EN-US"}

[\[Sysname-posa-app1\] tpdu-change destination]{lang="EN-US"}

[Connections for the application have been reset.]{lang="EN-US"}
:::
