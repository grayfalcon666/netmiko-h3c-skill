::: {#953489913 .myid}
[]{#_Toc404794492}[]{#struct_0_39052_x1280_1005108659}[]{#_Toc247446504}[]{#_Toc156115228}[]{#_Toc137986347}[]{#_Toc129160920}[]{#_Toc61260437}[]{#_Toc37216690}

**语音业务 \-- 语音业务配置命令 \-- call-forwarding**

------------------------------------------------------------------------

[**[call-forwarding]{lang="EN-US"}**]{#struct_0_39052_x1280_x2018195288}[命令用来配置呼叫前转功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **call-forwarding**]{lang="EN-US"}]{#struct_0_39052_x1280_1678534868}[命令用来关闭呼叫前转功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_446498509}

[**[call-forwarding]{lang="EN-US"}**[ { **on-busy** \| **no-reply** \| **unavailable** \| **unconditional** } **number** *number*]{lang="EN-US"}]{#struct_0_39052_x1280_x403274626}

[**[undo]{lang="EN-US"}**[ **call-forwarding** { **on-busy** \| **no-reply** \| **unavailable** \| **unconditional** }]{lang="EN-US"}]{#struct_0_39052_x1280_334214980}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39052_x1280_366433448}

[[呼叫前转功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_39052_x1280_1808538972}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1282590746}

[[POTS]{lang="EN-US"}]{#struct_0_39052_x1280_x224037173}[语音实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x822703146}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1870946120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1932521344}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1025810393}

[**[on-busy]{lang="EN-US"}**]{#struct_0_39052_x1280_x1842175462}[：遇忙呼叫前转。]{style="font-family:宋体"}

[**[no-reply]{lang="EN-US"}**]{#struct_0_39052_x1280_x1466354977}[：]{style="font-family:宋体"}[无应答呼叫前转。]{style="font-family:宋体"}

[**[unavailable]{lang="EN-US"}**]{#struct_0_39052_x1280_1543953429}[：线路]{style="font-family:宋体"}[不可用呼叫前转。]{style="font-family:宋体"}

[**[unconditional]{lang="EN-US"}**]{#struct_0_39052_x1280_1778896405}[：]{style="font-family:宋体"}[无条件呼叫前转。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}***[ number]{lang="EN-US"}*]{#struct_0_39052_x1280_x885133408}[：呼叫前转的目的号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1862127564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[四种前转类型可以同时配置，按优先级从高到底分别是]{lang="EN-US" style="font-family:宋体"}**[unconditional]{lang="EN-US"}**]{#struct_0_39052_x1280_x1431927828}[、]{lang="EN-US" style="font-family:
宋体"}**[unavailable]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[on-busy]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[no-reply]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置该功能时，需要保证前转发起方必须有到前转目的方的呼叫路由。]{style="font-family:宋体"}]{#struct_0_39052_x1280_x1004187562}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置在]{style="font-family:宋体"}]{#struct_0_39052_x1280_316000164}[POTS]{lang="EN-US"}[语音实体下，且只有该]{style="font-family:宋体"}[POTS]{lang="EN-US"}[语音实体上绑定的语音用户线为]{style="font-family:宋体"}[FXS]{lang="EN-US"}[语音用户线时，配置才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[实际应用时，为了保证该功能能够正常使用，请用户合理、有效地规划前转目的号码，避免出现错号、循环呼叫。]{style="font-family:宋体"}]{#struct_0_39052_x1280_334346052}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目前，一个呼叫最多可以前转]{style="font-family:宋体"}]{#struct_0_39052_x1280_x1842372070}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1983628330}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_574166402}[配置无应答呼叫前转功能，使呼叫前转到目的号码]{style="font-family:宋体"}[12345678]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_989159721}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] call-forwarding no-reply number 12345678]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_x863900978}[配置遇忙呼叫前转业务，使呼叫前转到目的号码]{style="font-family:宋体"}[12345678]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view    ]{lang="EN-US"}]{#struct_0_39052_x1280_582295972}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] call-forwarding on-busy number 12345678]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_334411588}[配置不可用呼叫前转功能，使呼叫前转到目的号码]{style="font-family:宋体"}[12345678]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_x2058429092}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] call-forwarding unavailable number 12345678]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_1357966578}[配置无条件呼叫前转功能，使呼叫前转到目的号码]{style="font-family:宋体"}[12345678]{lang="EN-US"}[上。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_x864262069}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] dial-program]{lang="EN-US"}

[\[Sysname-voice-dial\] entity 10 pots]{lang="EN-US"}

[\[Sysname-voice-dial-entity10\] call-forwarding unconditional number 12345678]{lang="EN-US"}
:::

::: {#-897939527 .myid}
[]{#_Toc37216693}[]{#_Toc404794493}[]{#struct_0_39052_x1280_789907922}[]{#_Toc247446510}[]{#_Toc346024507}[]{#_Toc346026709}[]{#_Toc346024508}[]{#_Toc346026710}[]{#_Toc346024509}[]{#_Toc346026711}[]{#_Toc346024510}[]{#_Toc346026712}[]{#_Toc346024511}[]{#_Toc346026713}[]{#_Toc346024512}[]{#_Toc346026714}[]{#_Toc346024513}[]{#_Toc346026715}[]{#_Toc346024514}[]{#_Toc346026716}[]{#_Toc346024515}[]{#_Toc346026717}[]{#_Toc346024516}[]{#_Toc346026718}[]{#_Toc346024517}[]{#_Toc346026719}[]{#_Toc346024518}[]{#_Toc346026720}[]{#_Toc346024519}[]{#_Toc346026721}[]{#_Toc346024520}[]{#_Toc346026722}[]{#_Toc346024521}[]{#_Toc346026723}[]{#_Toc346024522}[]{#_Toc346026724}[]{#_Toc346024523}[]{#_Toc346026725}[]{#_Toc346024524}[]{#_Toc346026726}[]{#_Toc346024525}[]{#_Toc346026727}[]{#_Toc346024526}[]{#_Toc346026728}[]{#_Toc346024527}[]{#_Toc346026729}[]{#_Toc346024528}[]{#_Toc346026730}[]{#_Toc157933245}[]{#_Toc346024529}[]{#_Toc346026731}[]{#_Toc346024530}[]{#_Toc346026732}[]{#_Toc346024531}[]{#_Toc346026733}[]{#_Toc346024532}[]{#_Toc346026734}[]{#_Toc346024533}[]{#_Toc346026735}[]{#_Toc346024534}[]{#_Toc346026736}[]{#_Toc346024535}[]{#_Toc346026737}[]{#_Toc346024536}[]{#_Toc346026738}[]{#_Toc346024537}[]{#_Toc346026739}[]{#_Toc346024538}[]{#_Toc346026740}[]{#_Toc346024539}[]{#_Toc346026741}[]{#_Toc346024540}[]{#_Toc346026742}[]{#_Toc346024541}[]{#_Toc346026743}[]{#_Toc346024542}[]{#_Toc346026744}[]{#_Toc346024543}[]{#_Toc346026745}[]{#_Toc346024544}[]{#_Toc346026746}[]{#_Toc346024545}[]{#_Toc346026747}[]{#_Toc346024546}[]{#_Toc346026748}[]{#_Toc346024547}[]{#_Toc346026749}[]{#_Toc346024548}[]{#_Toc346026750}[]{#_Toc346024549}[]{#_Toc346026751}[]{#_Toc346024550}[]{#_Toc346026752}[]{#_Toc346024551}[]{#_Toc346026753}[]{#_Toc346024552}[]{#_Toc346026754}[]{#_Toc346024553}[]{#_Toc346026755}[]{#_Toc346024554}[]{#_Toc346026756}[]{#_Toc346024555}[]{#_Toc346026757}[]{#_Toc346024556}[]{#_Toc346026758}[]{#_Toc346024557}[]{#_Toc346026759}[]{#_Toc346024558}[]{#_Toc346026760}[]{#_Toc346024559}[]{#_Toc346026761}[]{#_Toc346024560}[]{#_Toc346026762}[]{#_Toc346024561}[]{#_Toc346026763}[]{#_Toc346024562}[]{#_Toc346026764}[]{#_Toc346024563}[]{#_Toc346026765}[]{#_Toc346024564}[]{#_Toc346026766}[]{#_Toc346024565}[]{#_Toc346026767}[]{#_Toc346024566}[]{#_Toc346026768}[]{#_Toc346024567}[]{#_Toc346026769}[]{#_Toc346024568}[]{#_Toc346026770}[]{#_Toc346024569}[]{#_Toc346026771}[]{#_Toc346024570}[]{#_Toc346026772}[]{#_Toc346024571}[]{#_Toc346026773}[]{#_Toc346024572}[]{#_Toc346026774}[]{#_Toc157933248}[]{#_Toc157933249}[]{#_Toc157933250}[]{#_Toc157933251}[]{#_Toc157933252}[]{#_Toc157933253}[]{#_Toc157933254}[]{#_Toc157933255}[]{#_Toc157933256}[]{#_Toc157933257}[]{#_Toc157933258}[]{#_Toc157933259}[]{#_Toc157933260}[]{#_Toc157933261}[]{#_Toc157933262}[]{#_Toc157933263}[]{#_Toc157933264}[]{#_Toc157933265}[]{#_Toc238371840}[]{#_Toc243829633}[]{#_Toc238371841}[]{#_Toc243829634}[]{#_Toc238371842}[]{#_Toc243829635}[]{#_Toc238371843}[]{#_Toc243829636}[]{#_Toc238371844}[]{#_Toc243829637}[]{#_Toc238371845}[]{#_Toc243829638}[]{#_Toc238371846}[]{#_Toc243829639}[]{#_Toc238371847}[]{#_Toc243829640}[]{#_Toc238371848}[]{#_Toc243829641}[]{#_Toc238371849}[]{#_Toc243829642}[]{#_Toc238371850}[]{#_Toc243829643}[]{#_Toc238371851}[]{#_Toc243829644}[]{#_Toc238371852}[]{#_Toc243829645}[]{#_Toc238371853}[]{#_Toc243829646}[]{#_Toc238371854}[]{#_Toc243829647}[]{#_Toc238371855}[]{#_Toc243829648}[]{#_Toc238371856}[]{#_Toc243829649}[]{#_Toc238371857}[]{#_Toc243829650}[]{#_Toc238371858}[]{#_Toc243829651}[]{#_Toc238371860}[]{#_Toc243829653}[]{#_Toc238371861}[]{#_Toc243829654}

**语音业务 \-- 语音业务配置命令 \-- call-hold-format**

------------------------------------------------------------------------

[**[call-hold-format]{lang="EN-US"}**]{#struct_0_39052_x1280_x1011800654}[命令用来配置呼叫保持模式。]{style="font-family:宋体"}

[**[undo call-hold-format]{lang="EN-US"}**]{#struct_0_39052_x1280_334477124}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1418506262}

[**[call-hold-format]{lang="EN-US"}**[ { **inactive** \| **sendonly** \[ **moh-number** *string* \] }]{lang="EN-US"}]{#struct_0_39052_x1280_x1640174158}

[**[undo]{lang="EN-US"}**[ **call-hold-format**]{lang="EN-US"}]{#struct_0_39052_x1280_x1816446491}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x2072562318}

[[呼叫保持采用]{style="font-family:宋体"}**[inactive]{lang="EN-US"}**]{#struct_0_39052_x1280_x1418560089}[模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1022672094}

[[语音视图]{style="font-family:宋体"}]{#struct_0_39052_x1280_587537627}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1294655439}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_x238111175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_334542660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1803059254}

[**[inactive]{lang="EN-US"}**]{#struct_0_39052_x1280_x592429728}[：表示呼叫保持的模式为静音模式，用来指示被保持方关闭其发送和接收媒体通道。]{style="font-family:宋体"}

[**[sendonly]{lang="EN-US"}**]{#struct_0_39052_x1280_1960250547}[：表示呼叫保持的模式为单向放音模式，用来表示呼叫保持发起方开启发送媒体通道，关闭接收媒体通道。]{style="font-family:宋体"}

[**[moh-number]{lang="EN-US"}**[ *string*]{lang="EN-US"}]{#struct_0_39052_x1280_462509074}[：播放保持音乐的接入服务号码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1146347816}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_388083866}[配置呼叫保持功能采用]{style="font-family:宋体"}**[sendonly]{lang="EN-US"}**[模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_1001965738}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] call-hold-format sendonly]{lang="EN-US"}
:::

::: {#-1766427876 .myid}
[]{#_Toc404794494}[]{#struct_0_39052_x1280_x1842503142}[]{#_Toc355442037}[]{#_Toc354067132}[]{#_Toc346888917}

**语音业务 \-- 语音业务配置命令 \-- display voice mwi**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **voice** **mwi**]{lang="EN-US"}]{#struct_0_39052_x1280_x236190258}[命令用来显示消息等待指示功能的配置信息和从语音信箱服务器接收到的订阅信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1500307981}

[**[display]{lang="EN-US"}**[ **voice** **mwi** { **all** \| **number** *number* }]{lang="EN-US"}]{#struct_0_39052_x1280_x1842437606}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1504443230}

[[任意视图]{style="font-family:宋体"}]{#struct_0_39052_x1280_x1063672656}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_141364518}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_x1211604292}

[[network-operator]{lang="EN-US"}]{#struct_0_39052_x1280_x1637366898}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1301502394}

[[mdc-operator]{lang="EN-US"}]{#struct_0_39052_x1280_1062156826}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39052_x1280_259098780}

[**[all]{lang="EN-US"}**]{#struct_0_39052_x1280_x298401923}[：显示所有号码的订阅状态信息。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_39052_x1280_1415623052}[：显示指定号码的订阅状态信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，取值范围为数字]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和]{style="font-family:
宋体"}[+]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1842634214}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_1498225520}[显示消息等待指示功能的配置信息和从语音信箱服务器接收到的订阅信息。]{style="font-family:宋体"}

[[\<Sysname\> display voice mwi all]{lang="EN-US"}]{#struct_0_39052_x1280_1300084414}

[Message Waiting Indication ]{lang="EN-US"}[Information:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[MWI type: ]{lang="EN-US"}[Solicited]{lang="EN-US"}

[MWI server: 192.168.4.8 port: 5060]{lang="EN-US"}

[MWI expires: 200]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Number: 1515]{lang="EN-US"}

[Messages-Waiting: Yes]{lang="EN-US"}

[Voicemail: 1/3(1/2)]{lang="EN-US"}

[Total: 4(3)]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display voice mwi]{lang="EN-US"}]{#struct_0_39052_x1280_645920341}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_91957901}[[字段]{style="font-family:黑体"}]{#struct_0_39052_x1280_1729276282}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1842568678}

[[MWI type]{lang="EN-US"}]{#struct_0_39052_x1280_x1100249167}

[[消息等待指示的类型：]{style="font-family:宋体"}]{#struct_0_39052_x1280_x326425594}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unsolicited]{lang="EN-US"}]{#struct_0_39052_x1280_x1169906802}[：非请求模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Solicited]{lang="EN-US"}]{#struct_0_39052_x1280_x1841716710}[：请求模式]{lang="EN-US" style="font-family:宋体"}

[[MWI server]{lang="FR"}]{#struct_0_39052_x1280_x492175890}

[[语音信箱服务器地址，采用]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_39052_x1280_1364689772}[地址加端口号或域名的方式表示]{style="font-family:宋体"}

[[MWI expires]{lang="FR"}]{#struct_0_39052_x1280_x427875514}

[[订阅的老化时长]{style="font-family:宋体"}]{#struct_0_39052_x1280_2071569418}

[[Number]{lang="FR"}]{#struct_0_39052_x1280_x1841651174}

[[发起订阅的号码]{style="font-family:宋体"}]{#struct_0_39052_x1280_x15377172}

[[Messages-Waiting]{lang="FR"}]{#struct_0_39052_x1280_635993619}

[[消息等待标志：]{style="font-family:宋体"}]{#struct_0_39052_x1280_485051528}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Yes]{lang="EN-US"}]{#struct_0_39052_x1280_x1842241001}[：语音信箱服务器上有新消息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_39052_x1280_x2070662006}[：语音信箱服务器上没有新消息]{style="font-family:宋体"}

[[如上面例子中的]{style="font-family:宋体"}[Messages-Waiting: Yes]{lang="EN-US"}]{#struct_0_39052_x1280_x1862607390}[，说明当前语音信箱服务器上有号码]{style="font-family:宋体"}[1515]{lang="EN-US"}[的新消息]{style="font-family:宋体"}

[[Voicemail]{lang="FR"}]{#struct_0_39052_x1280_516067633}

[[消息类型：新消息数]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_39052_x1280_x1842175465}[旧消息数（新的紧急消息数]{style="font-family:宋体"}[/]{lang="EN-US"}[旧的紧急消息数）]{style="font-family:宋体"}

[[如上面例子中的]{style="font-family:宋体"}[Voicemail: 1/3(1/2)]{lang="EN-US"}]{#struct_0_39052_x1280_x2058364869}[，说明号码]{style="font-family:宋体"}[1515]{lang="EN-US"}[当前有]{style="font-family:宋体"}[1]{lang="EN-US"}[个新消息，]{style="font-family:宋体"}[3]{lang="EN-US"}[个旧消息，]{style="font-family:宋体"}[1]{lang="EN-US"}[个新的紧急消息，]{style="font-family:宋体"}[2]{lang="EN-US"}[个旧的紧急消息]{style="font-family:宋体"}

[[Total]{lang="FR"}]{#struct_0_39052_x1280_272954227}

[[普通消息数（紧急消息数）]{style="font-family:宋体"}]{#struct_0_39052_x1280_x2041966406}

[[例如上面例子中的]{style="font-family:宋体"}[Total: 4(3)]{lang="EN-US"}]{#struct_0_39052_x1280_x1842306537}[，说明号码]{style="font-family:宋体"}[1515]{lang="EN-US"}[当前共有普通消息]{style="font-family:宋体"}[4]{lang="EN-US"}[个，紧急消息]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1067851694 .myid}
[]{#_Toc404794495}[]{#struct_0_39052_x1280_x1384333629}[]{#_Toc355442038}

**语音业务 \-- 语音业务配置命令 \-- display voice sip subscribe-state**

------------------------------------------------------------------------

[**[display voice sip subscribe-state]{lang="EN-US"}**]{#struct_0_39052_x1280_2025835314}[命令用来显示号码的订阅状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1067333497}

[**[display voice sip subscribe-state]{lang="EN-US"}**]{#struct_0_39052_x1280_1783354433}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1204767229}

[[任意视图]{style="font-family:宋体"}]{#struct_0_39052_x1280_x942112420}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1812866963}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_x811930279}

[[network-operator]{lang="EN-US"}]{#struct_0_39052_x1280_x1842503145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_2136462737}

[[mdc-operator]{lang="EN-US"}]{#struct_0_39052_x1280_1419375191}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_39052_x1280_416687345}

[[只有在使用请求模式的情况下，才能使用该命令查看号码的订阅状态。]{style="font-family:宋体"}]{#struct_0_39052_x1280_x447112401}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x81108206}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_895608961}[显示号码的订阅状态。]{style="font-family:宋体"}

[[\<Sysname\> display voice sip subscribe-state ]{lang="EN-US"}]{#struct_0_39052_x1280_77688536}

[Number                          Server Address             Expires Status ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[2233                            192.168.4.8:5060           146     online]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display voice sip subscribe-state]{lang="EN-US"}]{#struct_0_39052_x1280_x1963417310}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_109564773}[[字段]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1842437609}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_39052_x1280_2031009179}

[[Number]{lang="EN-US"}]{#struct_0_39052_x1280_843266270}

[[使用订阅功能的号码]{style="font-family:宋体"}]{#struct_0_39052_x1280_x716171368}

[[Server Address]{lang="EN-US"}]{#struct_0_39052_x1280_898194812}

[[语音信箱服务器地址，采用]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_39052_x1280_x1842634217}[地址加端口号或域名的方式表示]{style="font-family:宋体"}

[[Expires]{lang="EN-US"}]{#struct_0_39052_x1280_1094940993}

[[订阅的老化时长]{style="font-family:宋体"}]{#struct_0_39052_x1280_353785743}

[[Status]{lang="EN-US"}]{#struct_0_39052_x1280_1210232158}

[[号码所处的订阅状态：]{style="font-family:宋体"}]{#struct_0_39052_x1280_1793399860}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_39052_x1280_x1842568681}[：表示订阅失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_39052_x1280_822786030}[：表示订阅成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Logging in]{lang="EN-US"}]{#struct_0_39052_x1280_x2111615375}[：表示正在订阅]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Logging out]{lang="EN-US"}]{#struct_0_39052_x1280_x1529250200}[：表示正在取消订阅]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-981317104 .myid}
[]{#_Toc404794496}[]{#struct_0_39052_x1280_2053293014}[]{#_Toc355442039}

**语音业务 \-- 语音业务配置命令 \-- mwi**

------------------------------------------------------------------------

[**[mwi]{lang="EN-US"}**]{#struct_0_39052_x1280_1629338238}[命令用来开启消息等待指示功能。]{style="font-family:宋体"}

[**[undo mwi]{lang="EN-US"}**]{#struct_0_39052_x1280_x1841716713}[命令用来关闭消息等待指示功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1073908051}

[**[mwi]{lang="EN-US"}**]{#struct_0_39052_x1280_607031053}

[**[undo mwi]{lang="EN-US"}**]{#struct_0_39052_x1280_1484527328}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x486878050}

[[消息等待指示功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_39052_x1280_x2122276719}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_622003581}

[[FXS]{lang="EN-US"}]{#struct_0_39052_x1280_x2093238133}[语音用户线视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1841651177}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1550706769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1697409287}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1004224189}

[[只有在语音用户线下配置]{style="font-family:宋体"}**[mwi]{lang="EN-US"}**]{#struct_0_39052_x1280_354481808}[命令后，与该语音用户线绑定的语音实体才有能力去发起订阅。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x718872901}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_x85136918}[开启消息等待指示功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_x1842241000}

[\[Sysname\] subscriber-line 2/1/1]{lang="EN-US"}

[\[Sysname-subscriber-line2/1/1\] mwi]{lang="EN-US"}
:::

::: {#-306439277 .myid}
[]{#_Toc404794497}[]{#struct_0_39052_x1280_658221349}[]{#_Toc355442040}

**语音业务 \-- 语音业务配置命令 \-- mwi-server**

------------------------------------------------------------------------

[**[mwi-server]{lang="EN-US"}**]{#struct_0_39052_x1280_x1717574378}[命令用来配置语音信箱服务器的信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **mwi-server**]{lang="EN-US"}]{#struct_0_39052_x1280_x782158955}[命令用来取消已配置的语音信箱服务器信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_39052_x1280_2078384009}

[**[mwi-server]{lang="EN-US"}**[ { **dns** *domain-name* \| **ip** *ip-address* } \[ **port** *port-number* \] \[ **expires** *seconds* \] \[ **transport** { **tcp** \[ **tls** \] \| **udp** } \] \[ **scheme** { **sip** \| **sips** } \] \[ **unsolicited** \]]{lang="EN-US"}]{#struct_0_39052_x1280_x673252785}

[**[undo mwi-server]{lang="EN-US"}**]{#struct_0_39052_x1280_x251466998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_39052_x1280_2064856814}

[[没有配置语音信箱服务器的信息。]{style="font-family:宋体"}]{#struct_0_39052_x1280_1091764710}

[[【视图】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1842175464}

[[SIP]{lang="EN-US"}]{#struct_0_39052_x1280_x270709550}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1742345940}

[[network-admin]{lang="EN-US"}]{#struct_0_39052_x1280_1052224689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_39052_x1280_2043761375}

[[【参数】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x63722538}

[**[dns]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_39052_x1280_x1844012319}[：语音信箱服务器的域名，由"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成（如]{style="font-family:宋体"}[aabbcc.com]{lang="EN-US"}[），每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符。不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["及"]{style="font-family:宋体"}[\_]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_39052_x1280_x1868116422}[：语音信箱服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_39052_x1280_x342827542}[：语音信箱服务器的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，如果选择配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[参数，在]{style="font-family:宋体"}[MWI]{lang="EN-US"}[功能使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[和]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输协议的情况下，缺省值为]{style="font-family:宋体"}[5060]{lang="EN-US"}[，在]{style="font-family:宋体"}[MWI]{lang="EN-US"}[功能使用]{style="font-family:宋体"}[TLS]{lang="EN-US"}[传输协议的情况下，缺省值为]{style="font-family:宋体"}[5061]{lang="EN-US"}[。如果选择配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[参数，则必须配置端口号。]{style="font-family:宋体"}

[**[expires]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_39052_x1280_x1842372072}[：订阅的老化时长，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[72000]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[transport]{lang="EN-US"}**]{#struct_0_39052_x1280_x1346402221}[：订阅时使用的传输协议。缺省情况下，订阅时使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[传输协议。]{style="font-family:宋体"}

[**[tcp]{lang="EN-US"}**]{#struct_0_39052_x1280_x1840174401}[：订阅时使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输协议，缺省情况下，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[传输协议。如果不选择]{style="font-family:宋体"}**[tls]{lang="EN-US"}**[参数，表示订阅时使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[传输协议。]{style="font-family:宋体"}

[**[tls]{lang="EN-US"}**]{#struct_0_39052_x1280_266071743}[：订阅时使用]{style="font-family:宋体"}[TLS]{lang="EN-US"}[传输协议。]{style="font-family:宋体"}

[**[udp]{lang="EN-US"}**]{#struct_0_39052_x1280_x389881709}[：订阅时使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[传输协议。]{style="font-family:宋体"}

[**[scheme]{lang="EN-US"}**]{#struct_0_39052_x1280_x462112247}[：订阅时使用的]{style="font-family:宋体"}[URL]{lang="EN-US"}[方案类型。缺省情况下，使用]{style="font-family:宋体"}[SIP]{lang="EN-US"}[格式的]{style="font-family:宋体"}[URL]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[**[sip]{lang="EN-US"}**]{#struct_0_39052_x1280_1176202232}[：订阅时使用]{style="font-family:宋体"}[SIP]{lang="EN-US"}[格式的]{style="font-family:宋体"}[URL]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[**[sips]{lang="EN-US"}**]{#struct_0_39052_x1280_2050104956}[：订阅时使用]{style="font-family:宋体"}[SIPS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[URL]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[**[unsolicited]{lang="EN-US"}**]{#struct_0_39052_x1280_x1322302018}[：非请求模式，表示]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[已经通过注册过程与语音信箱服务器建立订阅关系，]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[不需要向语音信箱服务器发送]{style="font-family:宋体"}[SUBSCRIBE]{lang="EN-US"}[消息即可接收到语音信箱服务器发送的]{style="font-family:宋体"}[NOTIFY]{lang="EN-US"}[消息。缺省情况下为请求模式，表示]{style="font-family:宋体"}[SIP UA]{lang="EN-US"}[需要通过发起]{style="font-family:宋体"}[SUBSCRIBE]{lang="EN-US"}[消息来与语音信箱服务器建立订阅关系后，才能够接收到语音信箱服务器发送的]{style="font-family:宋体"}[NOTIFY]{lang="EN-US"}[消息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_39052_x1280_x1842306536}

[[如果订阅时使用]{style="font-family:宋体"}[TLS]{lang="EN-US"}]{#struct_0_39052_x1280_592600228}[传输协议，那么该命令的目的端口号应该和语音信箱服务器上配置的端口号保持一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_39052_x1280_1809517594}

[[\# ]{lang="EN-US"}]{#struct_0_39052_x1280_x1365081823}[配置语音信箱服务器地址为]{style="font-family:宋体"}[100.1.1.101]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[5060]{lang="EN-US"}[，订阅的老化时长是]{style="font-family:宋体"}[7200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_39052_x1280_x407004933}

[\[Sysname\] voice-setup]{lang="EN-US"}

[\[Sysname-voice\] sip]{lang="EN-US"}

[\[Sysname-voice-sip\] mwi-server ip 100.1.1.101 port 5060 expires 7200]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[]{#_Toc125337639}[]{#_Toc125337640}[]{#_Toc125337641}[]{#_Toc125337642}[]{#_Toc125337643}[]{#_Toc125337644}[]{#_Toc125337645}[]{#_Toc125337646}[]{#_Toc125337647}[]{#_Toc125337648}[]{#_Toc125337649}[]{#_Toc150670799}[]{#_Toc150670860}[]{#_Toc150670800}[]{#_Toc150670861}[]{#_Toc150670801}[]{#_Toc150670862}[]{#_Toc150670802}[]{#_Toc150670863}[]{#_Toc150670803}[]{#_Toc150670864}[]{#_Toc150670804}[]{#_Toc150670865}[]{#_Toc150670805}[]{#_Toc150670866}[]{#_Toc150670806}[]{#_Toc150670867}[]{#_Toc150670807}[]{#_Toc150670868}[]{#_Toc150670808}[]{#_Toc150670869}[]{#_Toc150670809}[]{#_Toc150670870}[]{#_Toc150670810}[]{#_Toc150670871}[]{#_Toc150670811}[]{#_Toc150670872}[]{#_Toc150670812}[]{#_Toc150670873}[]{#_Toc150670813}[]{#_Toc150670874}[]{#_Toc150670814}[]{#_Toc150670875}[]{#_Toc150670815}[]{#_Toc150670876}[]{#_Toc150670816}[]{#_Toc150670877}[]{#_Toc150670819}[]{#_Toc150670880}[]{#_Toc150670820}[]{#_Toc150670881}[]{#_Toc125337655}[]{#_Toc125337656}[]{#_Toc125337657}[]{#_Toc125337658}[]{#_Toc125337659}[]{#_Toc125337660}[]{#_Toc125337661}[]{#_Toc125337662}[]{#_Toc125337663}[]{#_Toc125337664}[]{#_Toc125337665}[]{#_Toc125337666}[]{#_Toc125337667}[]{#_Toc125337679}[]{#_Toc125337687}[]{#_Toc125337736}[]{#_Toc157933269}[]{#_Toc37216704}[]{#_Toc157933272}[ ]{lang="EN-US"}
:::
