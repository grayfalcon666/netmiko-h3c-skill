::: {#-1707208934 .myid}
[]{#_Toc404785242}[]{#struct_0_x1668_46560_x924669184}[]{#_Toc324238744}

**Modem管理 \-- Modem管理配置命令 \-- country-code**

------------------------------------------------------------------------

[**[country-code]{lang="EN-US"}**]{#struct_0_x1668_46560_1118182165}[命令用来配置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的]{style="font-family:宋体"}[Modem]{lang="EN-US"}[编码格式。]{style="font-family:宋体"}

[**[undo country-code]{lang="EN-US"}**]{#struct_0_x1668_46560_x1185932334}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_250513481}

[**[country-code]{lang="EN-US"}**[ *area-name*]{lang="EN-US"}]{#struct_0_x1668_46560_1074129268}

[**[undo country-code]{lang="EN-US"}**]{#struct_0_x1668_46560_1269767031}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_193747316}

[[地区编码格式为]{style="font-family:宋体"}[united-states]{lang="EN-US"}]{#struct_0_x1668_46560_x1558869712}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_474018570}

[[AM]{lang="EN-US"}]{#struct_0_x1668_46560_x139013984}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_70342210}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x2119725061}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x750711752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1987871213}

[*[area-name]{lang="EN-US"}*]{#struct_0_x1668_46560_x1371756187}[：地区名称，包括：]{style="font-family:宋体"}[australia]{lang="EN-US"}[、]{style="font-family:宋体"}[austria]{lang="EN-US"}[、]{style="font-family:宋体"}[belgium]{lang="EN-US"}[、]{style="font-family:宋体"}[brazil]{lang="EN-US"}[、]{style="font-family:宋体"}[bulgaria]{lang="EN-US"}[、]{style="font-family:宋体"}[canada]{lang="EN-US"}[、]{style="font-family:宋体"}[china]{lang="EN-US"}[、]{style="font-family:宋体"}[czechoslovakia]{lang="EN-US"}[、]{style="font-family:宋体"}[denmark]{lang="EN-US"}[、]{style="font-family:宋体"}[finland]{lang="EN-US"}[、]{style="font-family:宋体"}[france]{lang="EN-US"}[、]{style="font-family:宋体"}[germany]{lang="EN-US"}[、]{style="font-family:宋体"}[greece]{lang="EN-US"}[、]{style="font-family:宋体"}[hongkong]{lang="EN-US"}[、]{style="font-family:宋体"}[hungary]{lang="EN-US"}[、]{style="font-family:宋体"}[india]{lang="EN-US"}[、]{style="font-family:宋体"}[ireland]{lang="EN-US"}[、]{style="font-family:宋体"}[israel]{lang="EN-US"}[、]{style="font-family:宋体"}[italy]{lang="EN-US"}[、]{style="font-family:宋体"}[japan]{lang="EN-US"}[、]{style="font-family:宋体"}[korea]{lang="EN-US"}[、]{style="font-family:宋体"}[luxembourg]{lang="EN-US"}[、]{style="font-family:宋体"}[malaysia]{lang="EN-US"}[、]{style="font-family:宋体"}[mexico]{lang="EN-US"}[、]{style="font-family:宋体"}[netherlands]{lang="EN-US"}[、]{style="font-family:宋体"}[new-zealand]{lang="EN-US"}[、]{style="font-family:宋体"}[norway]{lang="EN-US"}[、]{style="font-family:宋体"}[philippines]{lang="EN-US"}[、]{style="font-family:宋体"}[poland]{lang="EN-US"}[、]{style="font-family:宋体"}[portugal]{lang="EN-US"}[、]{style="font-family:宋体"}[russia]{lang="EN-US"}[、]{style="font-family:宋体"}[singapore]{lang="EN-US"}[、]{style="font-family:宋体"}[southafrica]{lang="EN-US"}[、]{style="font-family:宋体"}[spain]{lang="EN-US"}[、]{style="font-family:宋体"}[sweden]{lang="EN-US"}[、]{style="font-family:宋体"}[switzerland]{lang="EN-US"}[、]{style="font-family:宋体"}[taiwan]{lang="EN-US"}[、]{style="font-family:宋体"}[united-kingdom]{lang="EN-US"}[、]{style="font-family:宋体"}[united-states]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x129977285}

[[在不同的地区，]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_193812852}[的编码格式有所不同，为了适应不同地区的编码格式，可以配置此命令。]{style="font-family:宋体"}

[[需要注意的是，当]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_x194004526}[处于连接状态时，配置本命令会使]{style="font-family:宋体"}[Modem]{lang="EN-US"}[连接断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_477624239}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_x346093182}[配置]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口的编码格式为]{style="font-family:宋体"}[china]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x1071211577}

[\[Sysname\] interface analogmodem 2/4/0]{lang="EN-US"}

[\[Sysname-Analogmodem2/4/0\] country-code china]{lang="EN-US"}
:::

::: {#1079177676 .myid}
[]{#_Toc404785243}[]{#struct_0_x1668_46560_x179695322}[]{#_Toc324238741}

**Modem管理 \-- Modem管理配置命令 \-- modem answer-timer**

------------------------------------------------------------------------

[**[modem answer-timer]{lang="EN-US"}**]{#struct_0_x1668_46560_x495951728}[命令用来配置]{style="font-family:宋体"}[[Modem]{lang="EN-US"}]{#OLE_LINK4}[等待链路建立的有效时间间隔。]{style="font-family:
宋体"}

[**[undo modem answer-timer]{lang="EN-US"}**]{#struct_0_x1668_46560_432386541}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1040629669}

[**[modem answer-timer]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_x1668_46560_193223025}

[**[undo modem answer-timer]{lang="EN-US"}**]{#struct_0_x1668_46560_1417287008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_470186498}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_x1957961758}[等待链路建立的有效时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_154188801}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_x485562458}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1646437478}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x408263468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_1375697951}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1668_46560_193288561}

[*[time]{lang="SV"}*]{#struct_0_x1668_46560_x91763445}[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[等待链路建立的有效时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x97213106}

[[当]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_2036370779}[等待链路建立的时间间隔超过配置的有效时间间隔后，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[将拆除本次呼叫。]{style="font-family:宋体"}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_455804916}[作为主叫侧设备或被叫侧设备时，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[等待链路建立的时间间隔的含义不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_1071530056}[作为主叫侧设备时，该间隔是指从拨号到通话的时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_689321057}[作为被叫侧设备时，该间隔是指从摘机到通话的时间间隔。]{lang="EN-US" style="font-family:宋体"}

[[本命令仅在异步串口、工作在异步方式的同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1668_46560_193354097}[异步串口、]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线视图下可以配置，在]{style="font-family:宋体"}[Console]{lang="EN-US"}[、]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线视图下无法配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x2059856781}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_1606020506}[将]{style="font-family:宋体"}[Modem]{lang="EN-US"}[等待链路建立的有效时间配置为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x1358027799}

[\[Sysname\] line aux 0]{lang="EN-US"}

[\[Sysname-line-aux0\] modem answer-timer 50]{lang="EN-US"}
:::

::: {#-1921217210 .myid}
[]{#_Toc404785244}[]{#struct_0_x1668_46560_x1739120253}[]{#_Toc324238739}

**Modem管理 \-- Modem管理配置命令 \-- modem auto-answer**

------------------------------------------------------------------------

[**[modem auto-answer]{lang="EN-US"}**]{#struct_0_x1668_46560_x853446898}[命令用来配置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的应答方式为自动应答方式。]{style="font-family:宋体"}

[**[undo modem auto-answer]{lang="EN-US"}**]{#struct_0_x1668_46560_193419633}[命令用来配置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的应答方式为非自动应答方式，即路由器通过发]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令给]{style="font-family:宋体"}[Modem]{lang="EN-US"}[来应答。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_2109221829}

[**[modem auto-answer]{lang="EN-US"}**]{#struct_0_x1668_46560_1397328832}

[**[undo modem auto-answer]{lang="EN-US"}**]{#struct_0_x1668_46560_1421259771}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_41569686}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_192960881}[为非自动应答方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x762914699}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_174715931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_189422888}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x1837976561}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_372568007}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x132043866}

[[本命令仅在异步串口、工作在异步方式的同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1668_46560_1724667464}[异步串口、]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线视图下可以配置，在通道化生成的同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口对应的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图和]{style="font-family:宋体"}[Console]{lang="EN-US"}[、]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线视图下无法配置。]{style="font-family:宋体"}

[[建议根据路由器外接]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_193026417}[的当前应答状态配置本命令，使得用户接口的状态与]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的状态一致。当]{style="font-family:宋体"}[Modem]{lang="EN-US"}[状态为自动应答（]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的]{style="font-family:宋体"}[AA]{lang="EN-US"}[灯亮）时，配置]{style="font-family:宋体"}**[modem auto-answer]{lang="EN-US"}**[（以避免]{style="font-family:宋体"}[Modem]{lang="EN-US"}[自动应答后，路由器又发出应答指令）；如果外接]{style="font-family:宋体"}[Modem]{lang="EN-US"}[为非自动应答方式，则可配置]{style="font-family:宋体"}**[undo modem auto-answer]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[需要注意的是，当本命令的配置与]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_773735154}[当前的应答状态不一致时，对于某些]{style="font-family:宋体"}[Modem]{lang="EN-US"}[可能会造成应答不正常，请谨慎配置此命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x125663588}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_x1700110477}[在]{style="font-family:宋体"}[TTY1]{lang="EN-US"}[用户线视图下，配置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[为自动应答方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x1061395000}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] modem auto-answer]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x298745538}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[modem caller-number resolve]{lang="EN-US"}**]{#struct_0_x1668_46560_1439007772}
:::

::: {#993129845 .myid}
[]{#_Toc404785245}[]{#struct_0_x1668_46560_193091953}[]{#_Toc324238743}[]{#_Toc329711813}[]{#_Toc329711814}

**Modem管理 \-- Modem管理配置命令 \-- modem callback**

------------------------------------------------------------------------

[**[modem callback]{lang="EN-US"}**]{#struct_0_x1668_46560_x35830736}[命令用来开启]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的回呼功能。]{style="font-family:宋体"}

[**[undo modem callback]{lang="EN-US"}**]{#struct_0_x1668_46560_1273610737}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1137560382}

[**[modem callback]{lang="EN-US"}**]{#struct_0_x1668_46560_915316864}

[**[undo modem callback]{lang="EN-US"}**]{#struct_0_x1668_46560_1766975446}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_279746991}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_351548219}[的回呼功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1939074071}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_753767131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_193157489}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_1982546453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x1341235198}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1153777477}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_x132909958}[回呼功能是指]{style="font-family:宋体"}[Modem]{lang="EN-US"}[作为被叫侧设备和主叫方用户建立连接之后，对于需要回呼的主叫方用户，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[断开当前连接并主动呼出。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1029696718}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_193747313}[开启]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的回呼功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x1558869709}

[\[Sysname\] modem callback]{lang="EN-US"}
:::

::: {#-1250773171 .myid}
[]{#_Toc404785246}[]{#struct_0_x1668_46560_1233467921}[]{#_Toc324238740}

**Modem管理 \-- Modem管理配置命令 \-- modem caller-number resolve**

------------------------------------------------------------------------

[**[modem caller-number resolve]{lang="EN-US"}**]{#struct_0_x1668_46560_x2083866936}[命令用来开启]{style="font-family:
宋体"}[Modem]{lang="EN-US"}[模块获取终端主叫号码功能，即在]{style="font-family:宋体"}[Modem]{lang="EN-US"}[模块接受终端呼叫时，获取其主叫号码。]{style="font-family:宋体"}

[**[undo modem caller-number resolve]{lang="EN-US"}**]{#struct_0_x1668_46560_x1314161}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1644829344}

[**[modem caller-number resolve]{lang="EN-US"}**[ \[ **ata-waiting-time** *time* \]]{lang="EN-US"}]{#struct_0_x1668_46560_x252224444}

[**[undo modem caller-number resolve]{lang="EN-US"}**]{#struct_0_x1668_46560_1528176503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_495995530}

[[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_x58538050}[模块接受终端呼叫时，不获取其主叫号码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_193812849}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_1762310605}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_2143835118}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_2088949885}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x1286719133}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1015989738}

[**[ata-waiting-time ]{lang="EN-US"}**]{#struct_0_x1668_46560_x582665865}*[time]{lang="SV"}*[：]{style="font-family:宋体"}[Modem]{lang="EN-US"}[模块等待接收主叫方号码的时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[10000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。超过该时间之后，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[模块将不再接收[]{#OLE_LINK2}[主叫方]{#OLE_LINK1}号码。该参数取值与主叫方和主叫方接入设备之间的连接速率有关，若主叫方与主叫方接入设备之间的连接速率较低，则该参数配置的大一些，会增加]{style="font-family:宋体"}[Modem]{lang="EN-US"}[模块获取终端主叫号码的成功几率。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1024232500}

[[本命令仅在]{style="font-family:宋体"}[AM]{lang="EN-US"}]{#struct_0_x1668_46560_x327410344}[接口对应的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图下可以配置，在其它用户线视图下无法配置。]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}[AM]{lang="EN-US"}]{#struct_0_x1668_46560_193223026}[接口接入的]{style="font-family:宋体"}[POS]{lang="EN-US"}[（]{style="font-family:宋体"}[Point of Sale]{lang="EN-US"}[，销售点）终端，若前置机需要获取]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端的主叫号码，则]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入设备在向前置机转发终端的数据前，首先等待获取]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端的主叫号码，然后将获取到的终端的主叫号码发送给前置机，并等待前置机响应之后，再转发该终端的数据。本功能用于配合]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入终端实现主叫号码发送功能，关于]{style="font-family:宋体"}[POS]{lang="EN-US"}[接入终端主叫号码功能的相关介绍请参考"终端接入配置指导"中的"]{style="font-family:宋体"}[POS]{lang="EN-US"}[终端接入"。]{style="font-family:宋体"}

[[需要注意的是，当]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_1417287007}[处于连接状态时，配置本命令会使]{style="font-family:宋体"}[Modem]{lang="EN-US"}[连接断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_470252034}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_1797852941}[在]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图下，开启]{style="font-family:宋体"}[Modem]{lang="EN-US"}[模块获取终端主叫号码功能，并设置获取终端主叫号码的最长等待时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x2017956238}

[\[Sysname\] line tty 81]{lang="EN-US"}

[\[Sysname-line-tty81\] modem caller-number resolve ata-waiting-time 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1824671879}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[modem auto-answer]{lang="EN-US"}**]{#struct_0_x1668_46560_1397794866}
:::

::: {#-1522478508 .myid}
[]{#_Toc404785247}[]{#struct_0_x1668_46560_x209376578}[]{#_Toc324238738}[]{#_Toc329711817}[]{#_Toc329711818}[]{#_Toc329711819}[]{#_Toc329711820}

**Modem管理 \-- Modem管理配置命令 \-- modem enable**

------------------------------------------------------------------------

[**[modem enable]{lang="EN-US"}**]{#struct_0_x1668_46560_193288562}[命令用来开启]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的呼入]{style="font-family:宋体"}[/]{lang="EN-US"}[呼出权限。]{style="font-family:宋体"}

[**[undo modem enable]{lang="EN-US"}**]{#struct_0_x1668_46560_x91763442}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x97213111}

[**[modem enable]{lang="EN-US"}**[ { **both** \| **call-in** \| **call-out** }]{lang="EN-US"}]{#struct_0_x1668_46560_80055650}

[**[undo modem enable]{lang="EN-US"}**]{#struct_0_x1668_46560_1130781688}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1668_46560_668704791}

[[禁止]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_1960818620}[呼入和呼出。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_1687006702}

[[用户线视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_845176999}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1252102453}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_1539931919}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_193354098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x2059856768}

[**[both]{lang="EN-US"}**]{#struct_0_x1668_46560_x316424867}[：同时允许]{style="font-family:宋体"}[Modem]{lang="EN-US"}[呼入和呼出。]{style="font-family:宋体"}

[**[call-in]{lang="EN-US"}**]{#struct_0_x1668_46560_2000921871}[：仅允许]{style="font-family:宋体"}[Modem]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[**[call-out]{lang="EN-US"}**]{#struct_0_x1668_46560_649693876}[：仅允许]{style="font-family:宋体"}[Modem]{lang="EN-US"}[呼出。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1635215623}

[[本命令仅在异步串口、工作在异步方式的同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1668_46560_x303933660}[异步串口、]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[用户线视图和]{style="font-family:宋体"}[AUX]{lang="EN-US"}[接口对应的]{style="font-family:宋体"}[AUX]{lang="EN-US"}[用户线视图下可以配置，在]{style="font-family:宋体"}[Console]{lang="EN-US"}[、]{style="font-family:宋体"}[VTY]{lang="EN-US"}[用户线视图下无法配置。]{style="font-family:宋体"}

[[需要注意的是，当]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_2091547942}[处于连接状态时，配置本命令会使]{style="font-family:宋体"}[Modem]{lang="EN-US"}[连接断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1346125586}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_193419634}[在]{style="font-family:宋体"}[TTY1]{lang="EN-US"}[用户线上，配置仅允许]{style="font-family:宋体"}[Modem]{lang="EN-US"}[呼入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_2109221834}

[\[Sysname\] line tty 1]{lang="EN-US"}

[\[Sysname-line-tty1\] modem enable call-in]{lang="EN-US"}
:::

::::: {#-361739400 .myid}
[]{#_Toc404785248}[]{#struct_0_x1668_46560_1397525441}[]{#_Toc324238742}[]{#_Toc329711822}[]{#_Toc329711823}[]{#_Toc329711824}[]{#_Toc329711825}

**Modem管理 \-- Modem管理配置命令 \-- sendat**

------------------------------------------------------------------------

[**[sendat]{lang="EN-US"}**]{#struct_0_x1668_46560_x919620137}[命令用来手工向]{style="font-family:宋体"}[Modem]{lang="EN-US"}[发送]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1668_46560_895210204}

[**[sendat]{lang="EN-US"}**[ *at-string*]{lang="EN-US"}]{#struct_0_x1668_46560_x412330617}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1668_46560_351785533}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1668_46560_192960882}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x762914700}

[[network-admin]{lang="EN-US"}]{#struct_0_x1668_46560_x1782057964}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1668_46560_1587298026}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1572023591}

[*[at-string]{lang="SV"}*]{#struct_0_x1668_46560_x227101699}[：]{style="font-family:宋体"}[AT]{lang="SV"}[指令字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="SV"}[～]{style="font-family:宋体"}[300]{lang="SV"}[个字符的字符串]{style="font-family:宋体"}[，对于]{style="font-family:宋体"}[Modem]{lang="SV"}[而言，]{style="font-family:宋体"}[AT]{lang="SV"}[指令指的是"]{style="font-family:
宋体"}[+++]{lang="SV"}["]{style="font-family:宋体"}[和]{style="font-family:宋体"}["]{style="font-family:宋体"}[A/]{lang="SV"}["]{style="font-family:宋体"}[以及任意以]{style="font-family:
宋体"}[AT]{lang="SV"}[开头的字符串。]{style="font-family:宋体"}[AT]{lang="SV"}[指令的详细解释请参见]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-1]{lang="EN-US"}](?-361739400#_Ref329712072)[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x2096859799}

[**[sendat]{lang="EN-US"}**]{#struct_0_x1668_46560_x1941586624}[命令不检查]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令的合法性，直接将用户输入的字符串作为]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令送至]{style="font-family:宋体"}[Modem]{lang="EN-US"}[（遇到小写字母自动转化为大写字母）。若打开该接口的]{style="font-family:宋体"}[Modem]{lang="EN-US"}[调试信息开关，则可以看到]{style="font-family:宋体"}[Modem]{lang="EN-US"}[返回的结果码，若]{style="font-family:宋体"}[Modem]{lang="EN-US"}[通过]{style="font-family:宋体"}[E*n*]{lang="EN-US"}[指令设置了命令回显，还可以看到回显的]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1668_46560_1379472137}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令可以在异步串口、工作在异步方式的同]{style="font-family:宋体"}]{#struct_0_x1668_46560_193026418}[/]{lang="EN-US"}[异步串口、]{style="font-family:宋体"}[AUX]{lang="EN-US"}[接口、]{style="font-family:宋体"}[AM]{lang="EN-US"}[接口下执行。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_773735145}[处于]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令模式下才能接受]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令，若处于数据传输状态，使用该命令发送的]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令无效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}**[sendat]{lang="EN-US"}**]{#struct_0_x1668_46560_x2081978725}[命令]{lang="EN-US" style="font-family:宋体"}[一次只能]{style="font-family:宋体"}[发送]{lang="EN-US" style="font-family:宋体"}[一条]{style="font-family:宋体"}[AT]{lang="EN-US"}[指令。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1668_46560_783623107}[AT]{lang="EN-US"}[指令配置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[后，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的工作状态会被改变，有可能导致]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的状态混乱从而影响到拨号等基本功能。请在专业人员的指导下慎重使用本功能。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](Modem管理命令.files/image001.png){#图片 16 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1668_46560_193091954}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[AT]{lang="EN-US"}**]{#struct_0_x1668_46560_x35830731}[是命令行的字首，告诉]{style="font-family:
KaiTi_GB2312"}[Modem]{lang="EN-US"}[要输入命令。它执行除]{style="font-family:KaiTi_GB2312"}**[A/]{lang="EN-US"}**[（重复）和]{style="font-family:KaiTi_GB2312"}**[+++]{lang="EN-US"}**[（换码）之外的所有命令。单独输入]{style="font-family:KaiTi_GB2312"}**[AT]{lang="EN-US"}**[，如果]{style="font-family:KaiTi_GB2312"}[Modem]{lang="EN-US"}[准备接收命令，则]{style="font-family:KaiTi_GB2312"}[Modem]{lang="EN-US"}[返回]{style="font-family:KaiTi_GB2312"}[OK]{lang="EN-US"}[或]{style="font-family:KaiTi_GB2312"}[0]{lang="EN-US"}[信息。]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}]{#struct_0_x1668_46560_1273610732}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:KaiTi_GB2312"}1-1]{lang="EN-US"}](?-361739400#_Ref329712072)[提供了常用]{style="font-family:KaiTi_GB2312"}[AT]{lang="EN-US"}[指令的说明，表格中所有的命令均以]{style="font-family:KaiTi_GB2312"}[AT]{lang="EN-US"}[字符开头，用户可以参考。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[]{#struct_0_x1668_46560_x1137888062}[[表1-1 ]{lang="EN-US"}[常用]{style="font-family:
黑体"}[AT]{lang="EN-US"}]{#_Ref329712072}[指令描述表]{style="font-family:黑体"}

[]{#table_struct_0_468122739}[[指令]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1188823565}
:::::

[[说明]{style="font-family:黑体"}]{#struct_0_x1668_46560_x495306266}

[**[A]{lang="EN-US"}**]{#struct_0_x1668_46560_1596591872}

[[应答命令。]{style="font-family:宋体"}**[A]{lang="EN-US"}**]{#struct_0_x1668_46560_x658840725}[命令使]{style="font-family:宋体"}[Modem]{lang="EN-US"}[无需等待响铃即可应答呼叫。此命令在手动应答呼叫时有用。同一命令行中]{style="font-family:宋体"}**[A]{lang="EN-US"}**[之后的所有命令将被忽略]{style="font-family:宋体"}

[**[B]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_193157490}

[[通信标准选项，在]{style="font-family:宋体"}[ITU]{lang="EN-US"}]{#struct_0_x1668_46560_x356105716}[与]{style="font-family:宋体"}[Bell]{lang="EN-US"}[标准之间作出选择]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x923751680}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_x678595042}[，]{lang="EN-US" style="font-family:宋体"}[ITU V.22]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}[1200bps]{lang="EN-US"}[的传输速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 1]{lang="EN-US"}]{#struct_0_x1668_46560_464085044}[，]{lang="EN-US" style="font-family:宋体"}[Bell 212]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}[1200bps]{lang="EN-US"}[的传输速率（缺省值）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="PT-BR"}*]{#struct_0_x1668_46560_1999646054}[ = 2]{lang="PT-BR"}[或]{lang="EN-US" style="font-family:宋体"}[3]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[撤消]{lang="EN-US" style="font-family:宋体"}[ITU V]{lang="PT-BR"}[.]{lang="PT-BR"}[23]{lang="PT-BR"}[反向通道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 15]{lang="EN-US"}]{#struct_0_x1668_46560_193747314}[，]{lang="EN-US" style="font-family:宋体"}[ITU V.21]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}[300bps]{lang="EN-US"}[的传输速率]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 16]{lang="EN-US"}]{#struct_0_x1668_46560_x1558869714}[，]{lang="EN-US" style="font-family:宋体"}[103J]{lang="EN-US"}[使用]{lang="EN-US" style="font-family:宋体"}[300bps]{lang="EN-US"}[的传输速率（]{lang="EN-US" style="font-family:宋体"}[Compaq Presario 192-VS]{lang="EN-US"}[型和]{lang="EN-US" style="font-family:宋体"}[Compaq Presario 288-VS]{lang="EN-US"}[型调制解调器的缺省值）]{lang="EN-US" style="font-family:
  宋体"}

[**[E]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1280587624}

[[命令回应。]{style="font-family:宋体"}**[E]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_298701982}[命令确定当]{style="font-family:宋体"}[Modem]{lang="EN-US"}[在命令方式时，用户在键盘上输入的字符是否回显到屏幕上（本地回显）]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x805160266}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_1640886489}[，关闭本地回显功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_193812850}[ = 1]{lang="EN-US"}[，启用本地回显功能（缺省值）]{style="font-family:宋体"}

[**[D]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x194004524}

[[拨号命令。]{style="font-family:宋体"}**[D]{lang="EN-US"}**]{#struct_0_x1668_46560_477755311}[命令使]{style="font-family:宋体"}[Modem]{lang="EN-US"}[拨命令行中]{style="font-family:宋体"}[D]{lang="EN-US"}[后面的号码。在脉冲拨号方式下，非数字字符不起作用]{style="font-family:宋体"}

[**[H]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1237161154}

[[挂断控制。]{style="font-family:宋体"}**[H]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1143644262}[命令配置]{style="font-family:宋体"}[Modem]{lang="EN-US"}[挂断是以断开呼叫还是以摘机占用电话线方式]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1310159138}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_2115537330}[，]{lang="EN-US" style="font-family:宋体"}[Modem]{lang="EN-US"}[挂断（缺省值）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 1]{lang="EN-US"}]{#struct_0_x1668_46560_x1656132257}[，]{lang="EN-US" style="font-family:宋体"}[Modem]{lang="EN-US"}[摘机]{lang="EN-US" style="font-family:宋体"}

[**[I]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_993676804}

[[要求]{style="font-family:宋体"}[Modem]{lang="EN-US"}]{#struct_0_x1668_46560_1920259998}[的识别号（]{style="font-family:宋体"}[ID]{lang="EN-US"}[）。]{style="font-family:宋体"}**[I]{lang="EN-US"}***[n]{lang="EN-US"}*[命令询问]{style="font-family:宋体"}[Modem]{lang="EN-US"}[的产品识别号、]{style="font-family:宋体"}[ROM]{lang="EN-US"}[校验和或]{style="font-family:宋体"}[ROM ]{lang="EN-US"}[校验和的状态]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x947696244}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_2115602866}[或]{lang="EN-US" style="font-family:宋体"}[3]{lang="EN-US"}[，返回]{lang="EN-US" style="font-family:宋体"}[Modem]{lang="EN-US"}[默认的速率和控制器的硬件版本]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x823717966}[ = 1]{lang="EN-US"}[，计算]{style="font-family:宋体"}[ROM]{lang="EN-US"}[校验和并显示校验和]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1576235810}[ = 2]{lang="EN-US"}[，检查]{style="font-family:宋体"}[ROM]{lang="EN-US"}[、计算并验证校验和及显示]{style="font-family:宋体"}[OK]{lang="EN-US"}[或]{style="font-family:宋体"}[ERROR]{lang="EN-US"}[（错误）信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1470449742}[ = 4]{lang="EN-US"}[，返回数据泵的硬件版本]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2036079372}[ = 5]{lang="EN-US"}[，返回]{style="font-family:宋体"}[Modem]{lang="EN-US"}[板的]{style="font-family:宋体"}[ID]{lang="EN-US"}[、软件版本、硬件版本和国家代码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 9]{lang="EN-US"}]{#struct_0_x1668_46560_2115668402}[，返回国家代码]{lang="EN-US" style="font-family:宋体"}

[**[L]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1309958722}

[[配置扬声器音量。]{style="font-family:宋体"}**[L]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1881224217}[命令在传真和数据通信时配置扬声器的音量为低、中或高]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_542212443}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_2115733938}[或]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[，低音量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 2]{lang="EN-US"}]{#struct_0_x1668_46560_x1598973259}[，中音量（缺省配置）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 3]{lang="EN-US"}]{#struct_0_x1668_46560_x1340808128}[，高音量]{lang="EN-US" style="font-family:宋体"}

[**[M]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_164368423}

[[扬声器音量控制选项。]{style="font-family:宋体"}**[M]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1080062246}[命令控制传真和数据通信时扬声器是打开还是关闭]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115275186}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_x884713925}[，扬声器一直关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1126355060}[ = 1]{lang="EN-US"}[，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[在检测到载波信号之前，扬声器始终打开（缺省值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_154064432}[ = 2]{lang="EN-US"}[，在]{style="font-family:宋体"}[Modem]{lang="EN-US"}[摘机时，扬声器始终打开]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115340722}[ = 3]{lang="EN-US"}[，在拨号后扬声器始终打开，直到]{style="font-family:宋体"}[Modem]{lang="EN-US"}[检测到载波信号为止，拨号时除外]{style="font-family:宋体"}

[**[N]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_667875331}

[[调制握手。]{style="font-family:宋体"}**[N]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1282640662}[命令控制本地]{style="font-family:宋体"}[Modem]{lang="EN-US"}[在与速率不同的远程]{style="font-family:宋体"}[Modem]{lang="EN-US"}[连接时是否执行协商的握手]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1742960426}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115406258}[ = 0]{lang="EN-US"}[，在始发呼叫或应答呼叫时，仅以]{style="font-family:宋体"}[S37]{lang="EN-US"}[寄存器和]{style="font-family:宋体"}**[ATB]{lang="EN-US"}**[命令指定的通信标准下进行数字交换]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x882056613}[ = 1]{lang="EN-US"}[，在始发呼叫或应答呼叫时，仅以]{style="font-family:宋体"}[S37]{lang="EN-US"}[寄存器和]{style="font-family:宋体"}**[ATB]{lang="EN-US"}**[命令指定的速率开始握手，在握手期间，速率可能会回落（缺省值）]{style="font-family:宋体"}

[**[O]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x744608453}

[[在线数据方式。]{style="font-family:宋体"}**[O]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x91441556}[命令强迫]{style="font-family:宋体"}[Modem]{lang="EN-US"}[进入在线数据方式]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115471794}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 0]{lang="EN-US"}]{#struct_0_x1668_46560_x2063170426}[，进入在线数据方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_478022948}[ = 1]{lang="EN-US"}[，在返回在线数据方式前初始化均衡，重新排定序列]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1323683205}[ = 3]{lang="EN-US"}[，在返回在线数据方式前，进行速率的重新协商]{style="font-family:宋体"}

[[注意：在使用]{style="font-family:宋体"} **[+++]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1668_46560_2116061618}[换码命令换至在线命令方式后执行该命令将返回在线数据方式]{style="font-family:宋体"}

[**[Q]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x234650614}

[[抑制结果码。]{style="font-family:宋体"}**[Q]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1240392404}[命令启用]{style="font-family:宋体"}[Modem]{lang="EN-US"}[发送结果码]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1095588547}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2116127154}[ = 0]{lang="EN-US"}[，启用结果码（缺省值）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*[ = 1]{lang="EN-US"}]{#struct_0_x1668_46560_2128702681}[，禁用返回结果码]{lang="EN-US" style="font-family:宋体"}

[**[S]{lang="EN-US"}***[r]{lang="EN-US"}*[=*n*]{lang="EN-US"}]{#struct_0_x1668_46560_379719790}

[[写入]{style="font-family:宋体"}[S]{lang="EN-US"}]{#struct_0_x1668_46560_2115537331}[寄存器。]{style="font-family:宋体"}**[S]{lang="EN-US"}***[r]{lang="EN-US"}*[=*n*]{lang="EN-US"}[将]{style="font-family:宋体"}*[r]{lang="EN-US"}*[寄存器的值配置为]{style="font-family:宋体"}*[n]{lang="EN-US"}*[。用此命令可修改某些寄存器中的内容]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[r]{lang="EN-US"}*]{#struct_0_x1668_46560_x1656197793}[表示寄存器号，取值范围：]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[27, 29, 31]{lang="EN-US"}[～]{style="font-family:宋体"}[33, 35, 37, 89]{lang="EN-US"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1935891695}[表示赋值，取值范围：]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[**[T]{lang="EN-US"}**]{#struct_0_x1668_46560_2115602867}

[[音频拨号。]{style="font-family:宋体"}**[T]{lang="EN-US"}**]{#struct_0_x1668_46560_x823652430}[命令将拨号方式设为音频拨号。缺省情况下，]{style="font-family:宋体"}[Modem]{lang="EN-US"}[配置为音频拨号。此命令也可用作拨号修正符]{style="font-family:宋体"}

[**[P]{lang="EN-US"}**]{#struct_0_x1668_46560_x1650332979}

[[脉冲拨号。]{style="font-family:宋体"}**[P]{lang="EN-US"}**]{#struct_0_x1668_46560_x164928607}[命令配置脉冲拨号方式。所有的呼叫将停留在脉冲方式，直到使用]{style="font-family:宋体"}**[T]{lang="EN-US"}**[命令选择音频拨号为止。此命令也可用作拨号修正符]{style="font-family:宋体"}

[**[V]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115668403}

[[结果码的形式。]{style="font-family:宋体"}**[V]{lang="EN-US"}***[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1309893186}[命令确定]{style="font-family:宋体"}[Modem]{lang="EN-US"}[返回的结果码的类型]{style="font-family:宋体"}

[[参数]{style="font-family:宋体"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_1758681413}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_2115733939}[ = 0]{lang="EN-US"}[，以数字形式发送结果码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[n]{lang="EN-US"}*]{#struct_0_x1668_46560_x1599038795}[ = 1]{lang="EN-US"}[，以文本的形式发送结果码（缺省值）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1668_46560_x1206547262}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_x1051614105}[在异步串口下发送拨号命令，呼叫号码]{style="font-family:宋体"}[169]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_58260064}

[\[Sysname\] interface async 2/4/0]{lang="EN-US"}

[\[Sysname-Async2/4/0\] sendat ATD169]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1668_46560_2115275187}[在工作在异步方式的同]{style="font-family:宋体"}[/]{lang="EN-US"}[异步串口下发送拨号命令，呼叫号码]{style="font-family:宋体"}[169]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1668_46560_x884779461}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] physical-mode async]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] sendat ATD169]{lang="EN-US"}
