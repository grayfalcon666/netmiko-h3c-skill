::: {#-1689847227 .myid}
[]{#_Toc404786042}[]{#struct_0_25005_14002_x1439538451}[]{#_Toc353818121}

**RTC终端接入 \-- RTC终端接入命令 \-- auto-close**

------------------------------------------------------------------------

[**[auto-close]{lang="EN-US"}**]{#struct_0_25005_14002_995381184}[命令用来配置自动断链时间。]{style="font-family:宋体"}

[**[undo auto-close]{lang="EN-US"}**]{#struct_0_25005_14002_1569050378}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1656794158}

[**[auto-close]{lang="EN-US"}**[ *time*]{lang="EN-US"}]{#struct_0_25005_14002_116249420}

[**[undo auto-close]{lang="EN-US"}**]{#struct_0_25005_14002_1350903220}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x137705961}

[[自动断链时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_25005_14002_x556839747}[，即不自动断链。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1612456773}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x571216427}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1377518212}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1317679775}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_428160281}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x45254144}

[*[time]{lang="EN-US"}*]{#struct_0_25005_14002_983072211}[：自动断链时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_176954361}

[[终端接入具有终端自动断链功能，用户可以在终端模板视图下启用并配置该终端的自动断链时间。当用户终端设备和终端接入设备断开连接后，终端处于]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_25005_14002_x642404104}[状态，在经过设定的时间后，]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[自动与]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[断开]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果不配置终端自动断链功能，该]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接将被一直保持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1257750815}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_425257431}[配置自动断链时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_708984260}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] auto-close 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1657702978}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-link]{lang="EN-US"}**]{#struct_0_25005_14002_x2122923688}
:::

::: {#1390887252 .myid}
[]{#_Toc404786043}[]{#struct_0_25005_14002_232012648}[]{#_Toc353818122}

**RTC终端接入 \-- RTC终端接入命令 \-- auto-link**

------------------------------------------------------------------------

[**[auto-link]{lang="EN-US"}**]{#struct_0_25005_14002_1179729360}[命令用来配置自动建链的时间。]{style="font-family:宋体"}

[**[undo auto-link]{lang="EN-US"}**]{#struct_0_25005_14002_1145051961}[命令用来恢复缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1154500489}

[**[auto-link ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_25005_14002_637881354}

[**[undo auto-link]{lang="EN-US"}**]{#struct_0_25005_14002_963022113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x341066168}

[[自动建链时间为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_25005_14002_2088064198}[，即需要手动建链。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x527942314}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1284969743}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x322694669}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_652357424}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1323451173}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_605959667}

[*[time]{lang="EN-US"}*]{#struct_0_25005_14002_x1509733602}[：自动建链时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[，单位为秒*。*]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_480242322}

[[终端接入具有终端自动建链功能，用户可以在终端模板视图下启用并配置终端的自动建链时间。当终端的物理连接完好时，经过指定时间后，]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}]{#struct_0_25005_14002_x2129945906}[将自动与远端的]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果没有配置终端自动建链时间，则终端需要通过手动方式建链，等待用户在终端上输入字符（除热键、终端的特殊字符外，特殊字符即终端直接处理的字符，如]{style="font-family:宋体"}[\<Shift+F2\>]{lang="EN-US"}[），]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[才会与]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_994422974}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1229749015}[配置自动建链时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x3912461}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] auto-link 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1786957668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-close]{lang="EN-US"}**]{#struct_0_25005_14002_x761696915}
:::

::: {#-1142840015 .myid}
[]{#_Toc404786044}[]{#struct_0_25005_14002_x1614881496}[]{#_Toc353818123}

**RTC终端接入 \-- RTC终端接入命令 \-- bind vpn-instance**

------------------------------------------------------------------------

[**[bind vpn-instance]{lang="EN-US"}**]{#struct_0_25005_14002_x49646569}[命令用来配置终端模板绑定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo bind vpn-instance]{lang="EN-US"}**]{#struct_0_25005_14002_280527869}[命令用来取消绑定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x960124274}

[**[bind vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_25005_14002_840561448}

[**[undo bind vpn-instance]{lang="EN-US"}**]{#struct_0_25005_14002_x717025371}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1420677240}

[[终端模板没有绑定]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_25005_14002_2097723894}[实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1761284557}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1990175164}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1238349409}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1410644613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_2092699592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_2050175732}

[*[vpn-name]{lang="EN-US"}*]{#struct_0_25005_14002_610849061}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写*。*]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x523434526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置用于]{style="font-family:宋体"}]{#struct_0_25005_14002_1056298361}[RTC Client]{lang="DE"}[同时做]{style="font-family:宋体"}[MPLS PE]{lang="EN-US"}[的情况。将配置了本命令的终端模板应用到异步串口下，则该异步串口所对应的终端也就绑定了该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，这样]{style="font-family:宋体"}[RTC Client]{lang="DE"}[就能将不同的终端划分到不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[域里。]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[如果不配置本命令，它能够接受来自任何]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[的连接请求。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个模板只能绑定一个实例，如果多次使用该命令绑定实例，最新的配置有效。]{style="font-family:宋体"}]{#struct_0_25005_14002_x239810003}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1778195689}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_369508557}[配置终端模板绑定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x2088587786}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] bind vpn-instance vpn1]{lang="EN-US"}
:::

::: {#-1627695344 .myid}
[]{#_Toc404786045}[]{#struct_0_25005_14002_1350497718}[]{#_Toc353818136}

**RTC终端接入 \-- RTC终端接入命令 \-- display rta**

------------------------------------------------------------------------

[**[display rta]{lang="EN-US"}**]{#struct_0_25005_14002_x911412145}[命令用来显示终端接入相关的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1671042709}

[**[display rta ]{lang="EN-US"}**[{ **all** \| **statistics** \| *terminal-number* { *vty-number* \| **brief** \| **detail** \| **statistics** } }]{lang="EN-US"}]{#struct_0_25005_14002_x516541881}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1112038890}

[[任意视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x358635020}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_472558530}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1685077714}

[[network-operator]{lang="EN-US"}]{#struct_0_25005_14002_x509785580}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1222690669}

[[mdc-operator]{lang="EN-US"}]{#struct_0_25005_14002_x1920294585}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_812085075}

[**[all]{lang="EN-US"}**]{#struct_0_25005_14002_140136054}[：显示所有终端的信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_25005_14002_1145906185}[：显示终端的统计信息。]{style="font-family:宋体"}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1532066027}[：显示指定终端的信息。终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_740892539}[：显示指定虚终端的信息。虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_25005_14002_x1016114611}[：显示指定终端的简要信息。]{style="font-family:宋体"}

[**[detail]{lang="EN-US"}**]{#struct_0_25005_14002_1393181229}[：显示指定终端的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_884073457}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1365275927}[显示终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[VTY1]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta 1 1]{lang="EN-US"}]{#struct_0_25005_14002_1412463185}

[VTY 1]{lang="EN-US"}

[    APP index: 0]{lang="EN-US"}

[    APP type: RTC Client]{lang="EN-US"}

[    APP state: Unlinked]{lang="EN-US"}

[    Remote IP: 192.168.0.110]{lang="EN-US"}

[    Source IP: Not configured]{lang="EN-US"}

[    Actual source IP: \--]{lang="EN-US"}

[    Remote port: 9010]{lang="EN-US"}

[    Local port: Not configured]{lang="EN-US"}

[    Connection duration: 00:00:00]{lang="EN-US"}

[]{#struct_0_25005_14002_x807688488}[[表1-1 ]{lang="EN-US"}[display rta terminal-number vty-number]{lang="EN-US"}]{#_Toc353120935}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1424316738}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_1145673348}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_x400699659}

[[APP index]{lang="EN-US"}]{#struct_0_25005_14002_1088424730}

[[应用的索引]{style="font-family:宋体"}]{#struct_0_25005_14002_x1666823845}

[[APP type]{lang="EN-US"}]{#struct_0_25005_14002_610202047}

[[应用的类型，取值包括]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}]{#struct_0_25005_14002_x1250949532}[、]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}

[[APP state]{lang="EN-US"}]{#struct_0_25005_14002_831056453}

[[应用的状态，取值为：]{style="font-family:宋体"}]{#struct_0_25005_14002_x153620756}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unlinked]{lang="EN-US"}]{#struct_0_25005_14002_x916262194}[：]{lang="EN-US" style="font-family:宋体"}[表示连接未建立]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linking]{lang="EN-US"}]{#struct_0_25005_14002_x1275664196}[：]{lang="EN-US" style="font-family:宋体"}[表示连接建立中（此状态只有]{style="font-family:宋体"}[TCP Client]{lang="EN-US"}[存在）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linked]{lang="EN-US"}]{#struct_0_25005_14002_x211331538}[：]{lang="EN-US" style="font-family:宋体"}[表示连接已建立]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\--]{lang="EN-US"}]{#struct_0_25005_14002_x135701084}[：表示当模板不存在]{style="font-family:宋体"}[APP]{lang="EN-US"}

[[Remote IP]{lang="EN-US"}]{#struct_0_25005_14002_x1142657501}

[[远端终端接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_25005_14002_x514821987}[地址]{style="font-family:宋体"}

[[Source IP]{lang="EN-US"}]{#struct_0_25005_14002_x1115988339}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_25005_14002_2093397673}[地址，即在终端模板下为]{style="font-family:宋体"}[VTY]{lang="EN-US"}[配置的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Actual source IP]{lang="EN-US"}]{#struct_0_25005_14002_x1719704697}

[[实际源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_25005_14002_x286433516}[地址，即建立连接时使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示连接还未建立。]{style="font-family:宋体"}

[[Remote port]{lang="EN-US"}]{#struct_0_25005_14002_x1248997298}

[[远端终端接入设备的监听端口]{style="font-family:宋体"}]{#struct_0_25005_14002_x528339494}

[[Local port]{lang="EN-US"}]{#struct_0_25005_14002_x1898440064}

[[本端终端接入设备的监听端口]{style="font-family:宋体"}]{#struct_0_25005_14002_1715436727}

[[Connection duration]{lang="EN-US"}]{#struct_0_25005_14002_1400892888}

[[应用连接保持时间（时：分：秒）]{style="font-family:宋体"}]{#struct_0_25005_14002_753088948}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1009178658}[显示]{style="font-family:宋体"}[1]{lang="EN-US"}[号终端的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta 1 brief]{lang="EN-US"}]{#struct_0_25005_14002_1599391912}

[TTY 1]{lang="EN-US"}

[    Interface used         :  Async2/2/0]{lang="EN-US"}

[    Current state          :  Up]{lang="EN-US"}

[    Current APP            :  0]{lang="EN-US"}

[    APP type               :  RTC client]{lang="EN-US"}

[    APP name               :  Not configured]{lang="EN-US"}

[    APP state              :  Unlinked]{lang="EN-US"}

[    Socket recvBuf Size    :  2048 bytes]{lang="EN-US"}

[    Socket sendBuf Size    :  2048 bytes]{lang="EN-US"}

[    TTY auto-link          :  10 seconds]{lang="EN-US"}

[    TTY close-link         :  10 seconds]{lang="EN-US"}

[    TTY receive bytes      :  1371 bytes]{lang="EN-US"}

[    TTY send bytes         :  63696 bytes]{lang="EN-US"}

[    Last receive time      :  19:39:33]{lang="EN-US"}

[    Last send time         :  03:39:34]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Current APP recveive   :  55280 bytes]{lang="EN-US"}

[    Current APP send       :  1524 bytes]{lang="EN-US"}

[    Time from APP is linked: 00:00:00]{lang="EN-US"}

[    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    VTY       APP       Type       State]{lang="EN-US"}

[    0         0         RTC client Unlinked]{lang="EN-US"}

[]{#struct_0_25005_14002_1443292211}[[表1-2 ]{lang="EN-US"}[表]{style="font-family:
黑体"}[1-2 display rta terminal-number brief]{lang="EN-US"}]{#_Toc353120936}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1418081910}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_x1908188447}

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_x495345801}

[[TTY 1]{lang="EN-US"}]{#struct_0_25005_14002_x1872198763}

[[终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_25005_14002_x556905283}[的]{style="font-family:宋体"}[TTY]{lang="EN-US"}[终端]{style="font-family:宋体"}

[[Interface used]{lang="EN-US"}]{#struct_0_25005_14002_124693486}

[[终端]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_25005_14002_x6131643}[对应的物理接口]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_25005_14002_999867977}

[[终端的当前状态，取值为：]{style="font-family:宋体"}]{#struct_0_25005_14002_x1191945063}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_25005_14002_452415996}[：物理]{lang="EN-US" style="font-family:宋体"}[Down]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_25005_14002_x1184679956}[：物理]{lang="EN-US" style="font-family:宋体"}[Up]{lang="EN-US"}

[[Current APP]{lang="EN-US"}]{#struct_0_25005_14002_1008605774}

[[当前应用]{style="font-family:宋体"}]{#struct_0_25005_14002_x2122989224}

[[APP type]{lang="EN-US"}]{#struct_0_25005_14002_1771770870}

[[应用类型]{style="font-family:宋体"}]{#struct_0_25005_14002_x1489029986}

[[APP name]{lang="EN-US"}]{#struct_0_25005_14002_1346040021}

[[应用名称]{style="font-family:宋体"}]{#struct_0_25005_14002_x650558504}

[[APP state]{lang="EN-US"}]{#struct_0_25005_14002_1702729537}

[[应用状态]{style="font-family:宋体"}]{#struct_0_25005_14002_x555664136}

[[Socket recvBuf size]{lang="EN-US"}]{#struct_0_25005_14002_661725277}

[[TCP]{lang="EN-US"}]{#struct_0_25005_14002_605894131}[接收缓存大小]{style="font-family:宋体"}

[[Socket sendBuf size]{lang="EN-US"}]{#struct_0_25005_14002_810914711}

[[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x1323525278}[发送缓存大小]{style="font-family:宋体"}

[[TTY auto-link]{lang="EN-US"}]{#struct_0_25005_14002_x1031987037}

[[自动建链时间]{style="font-family:宋体"}]{#struct_0_25005_14002_x915242985}

[[TTY close-link]{lang="EN-US"}]{#struct_0_25005_14002_1621158077}

[[自动断链时间]{style="font-family:宋体"}]{#struct_0_25005_14002_x108930915}

[[TTY recieve bytes]{lang="EN-US"}]{#struct_0_25005_14002_x960189810}

[[接收数据的字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_x246157179}

[[TTY send bytes]{lang="EN-US"}]{#struct_0_25005_14002_1119537599}

[[发送数据的字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_x1937868506}

[[Last receivev time]{lang="EN-US"}]{#struct_0_25005_14002_1254055470}

[[上一次接收数据的时间]{style="font-family:宋体"}]{#struct_0_25005_14002_581164559}

[[Last send time]{lang="EN-US"}]{#struct_0_25005_14002_1056232825}

[[上一次发送数据的时间]{style="font-family:宋体"}]{#struct_0_25005_14002_x1700971493}

[[Current APP receive]{lang="EN-US"}]{#struct_0_25005_14002_810615370}

[[当前应用接收的数据字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_790939895}

[[Current APP send]{lang="EN-US"}]{#struct_0_25005_14002_1490857696}

[[当前应用发送的数据字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_320654407}

[[Time from APP is linked]{lang="EN-US"}]{#struct_0_25005_14002_x1866011080}

[[应用连接保持时间]{style="font-family:宋体"}]{#struct_0_25005_14002_x509851116}

[[VTY       APP       Type       State]{lang="EN-US"}]{#struct_0_25005_14002_1537631873}

[[终端配置的虚终端列表，其中：]{style="font-family:宋体"}]{#struct_0_25005_14002_366518328}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VTY]{lang="EN-US"}]{#struct_0_25005_14002_x542463741}[：]{style="font-family:宋体"}[表示虚终端号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[APP]{lang="EN-US"}]{#struct_0_25005_14002_x2097111882}[：]{style="font-family:宋体"}[表示应用]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_25005_14002_467985475}[：]{style="font-family:宋体"}[表示应用类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[State]{lang="EN-US"}]{#struct_0_25005_14002_1546680913}[：]{style="font-family:宋体"}[表示应用状态]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x16366700}[显示终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的终端的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta 1 statistics]{lang="EN-US"}]{#struct_0_25005_14002_1364414915}

[TTY 1]{lang="EN-US"}

[  Received from terminal: 1231]{lang="EN-US"}

[  Send to terminal:       348]{lang="EN-US"}

[  Received from remote:   8342]{lang="EN-US"}

[  Send to remote:         7342]{lang="EN-US"}

[ ]{lang="EN-US"}

[  VTY 0]{lang="EN-US"}

[    Receive from terminal: 1231            Last receive time: 03:08:29]{lang="EN-US"}

[    Send to terminal:      348             Last send time:    01:10:30]{lang="EN-US"}

[    Receive from remote:   8342            Last receive time: 17:21:25]{lang="EN-US"}

[    Send to remote:        7342            Last send time:    09:44:43]{lang="EN-US"}

[]{#struct_0_25005_14002_1918838195}[[表1-3 ]{lang="EN-US"}[display rta terminal-number statistics]{lang="EN-US"}]{#_Toc353120937}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1413757778}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_852076796}

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_1062197444}

[[Receive from terminal]{lang="EN-US"}]{#struct_0_25005_14002_13403118}

[[从终端接收的数据大小（单位为字节）]{style="font-family:宋体"}]{#struct_0_25005_14002_x323770185}

[[Send to terminal]{lang="EN-US"}]{#struct_0_25005_14002_1825964419}

[[发送到终端的数据大小（单位为字节）]{style="font-family:宋体"}]{#struct_0_25005_14002_x19403028}

[[Receive from remote]{lang="EN-US"}]{#struct_0_25005_14002_x1039784647}

[[从远端接收的数据大小（单位为字节）]{style="font-family:宋体"}]{#struct_0_25005_14002_x1304264455}

[[Send to remote]{lang="EN-US"}]{#struct_0_25005_14002_198592545}

[[发送到远端的数据大小（单位为字节）]{style="font-family:宋体"}]{#struct_0_25005_14002_850705751}

[[Last receive time]{lang="EN-US"}]{#struct_0_25005_14002_1338350402}

[[最近一次接收时间（时：分：秒），"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_25005_14002_762582334}["表示未收到过数据]{style="font-family:宋体"}

[[Last send time]{lang="EN-US"}]{#struct_0_25005_14002_2000124214}

[[最近一次发送时间（时：分：秒），"]{style="font-family:宋体"}[\--]{lang="EN-US"}]{#struct_0_25005_14002_1393748339}["表示未发送过数据]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_942977911}[显示终端接入的所有信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta all]{lang="EN-US"}]{#struct_0_25005_14002_x1585486969}

[TTYID    TTY State     Current APP    APP Type    APP State]{lang="EN-US"}

[1        Up            0              RTC client  Unlinked]{lang="EN-US"}

[]{#struct_0_25005_14002_x21309457}[[表1-4 ]{lang="EN-US"}[display rta all]{lang="EN-US"}]{#_Toc353120938}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1417413422}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_x1894079454}

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_x1921102468}

[[TTYID]{lang="EN-US"}]{#struct_0_25005_14002_1981644919}

[[终端号]{style="font-family:宋体"}]{#struct_0_25005_14002_1529039259}

[[TTY State]{lang="EN-US"}]{#struct_0_25005_14002_33312087}

[[终端状态]{style="font-family:宋体"}]{#struct_0_25005_14002_x1517704718}

[[Current APP]{lang="EN-US"}]{#struct_0_25005_14002_x1482481692}

[[当前应用]{style="font-family:宋体"}]{#struct_0_25005_14002_1334025861}

[[APP Type]{lang="EN-US"}]{#struct_0_25005_14002_x1633890790}

[[应用类型]{style="font-family:宋体"}]{#struct_0_25005_14002_1609152830}

[[APP State]{lang="EN-US"}]{#struct_0_25005_14002_1143396386}

[[应用状态]{style="font-family:宋体"}]{#struct_0_25005_14002_2089191503}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x494346453}[显示终端接入的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta statistics]{lang="EN-US"}]{#struct_0_25005_14002_1203769087}

[    RTA template number: 2]{lang="EN-US"}

[    RTA TTY number: 1]{lang="EN-US"}

[    RTA APP number: 1]{lang="EN-US"}

[    RTA listen port number: 0]{lang="EN-US"}

[]{#struct_0_25005_14002_x851034892}[[表1-5 ]{lang="EN-US"}[display rta statistics]{lang="EN-US"}]{#_Toc353120939}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1416572670}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_1915232048}

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_1207835701}

[[RTA template number]{lang="EN-US"}]{#struct_0_25005_14002_x1824626199}

[[终端接入设备上配置的终端模板数]{style="font-family:宋体"}]{#struct_0_25005_14002_x9243695}

[[RTA TTY number]{lang="EN-US"}]{#struct_0_25005_14002_1207516173}

[[终端接入设备上配置的终端数]{style="font-family:宋体"}]{#struct_0_25005_14002_x278786952}

[[RTA APP number]{lang="EN-US"}]{#struct_0_25005_14002_x422687555}

[[配置终端后生成的应用数]{style="font-family:宋体"}]{#struct_0_25005_14002_x2024305406}

[[RTA listen port number]{lang="EN-US"}]{#struct_0_25005_14002_x825969311}

[[终端接入设备正在侦听的端口数]{style="font-family:宋体"}]{#struct_0_25005_14002_2105088817}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x625886142}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_833624225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta relay status]{lang="EN-US"}**]{#struct_0_25005_14002_x1817307111}

::: {#-504548869 .myid}
[]{#_Toc404786046}[]{#struct_0_25005_14002_56862916}[]{#_Toc353818137}

**RTC终端接入 \-- RTC终端接入命令 \-- display rta relay statistics**

------------------------------------------------------------------------

[**[display rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_1977146318}[命令用来显示中继透传的数据转发统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1750077301}

[**[display rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_x671779094}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1487857973}

[[任意视图]{style="font-family:宋体"}]{#struct_0_25005_14002_2104874048}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_2095769809}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1988771496}

[[network-operator]{lang="EN-US"}]{#struct_0_25005_14002_x961459217}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1867452154}

[[mdc-operator]{lang="EN-US"}]{#struct_0_25005_14002_x1473523155}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1129617589}

[[中继服务器在向客户端转发数据时会实时统计转发的字节数和发送的报文数。]{style="font-family:宋体"}]{#struct_0_25005_14002_694285970}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_182141132}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1229563897}[显示中继透传的数据转发统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rta relay statistics]{lang="EN-US"}]{#struct_0_25005_14002_x1958768361}

[Server   Port    Client-IP    Recv-Packets Recv-Bytes Sent-Packets Sent-Bytes]{lang="EN-US"}

[0        1026    1.1.1.2      15           190        30           370]{lang="EN-US"}

[0        1026    1.1.1.3      15           110        35           421]{lang="EN-US"}

[1        1027    1.1.1.4      0            0          0            0]{lang="EN-US"}

[]{#struct_0_25005_14002_x1981308175}[[表]{style="font-family:黑体"}[1-6 ]{lang="EN-US"}]{#_Toc353120940}[display rta relay statistics]{lang="FR"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1409310312}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_697288579}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_2038462036}

[[Server]{lang="EN-US"}]{#struct_0_25005_14002_x1267666345}

[[转发组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_25005_14002_740111859}

[[Port]{lang="EN-US"}]{#struct_0_25005_14002_1499967270}

[[转发组监听端口]{style="font-family:宋体"}]{#struct_0_25005_14002_x261698524}

[[Client-IP]{lang="EN-US"}]{#struct_0_25005_14002_65174700}

[[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_25005_14002_1928721535}[地址]{style="font-family:宋体"}

[[Recv-Packets]{lang="EN-US"}]{#struct_0_25005_14002_871344157}

[[从该客户端收到的报文数]{style="font-family:宋体"}]{#struct_0_25005_14002_1152625067}

[[Recv-Bytes]{lang="EN-US"}]{#struct_0_25005_14002_x503390782}

[[从该客户端收到的数据字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_x1966673640}

[[Sent-Packets]{lang="EN-US"}]{#struct_0_25005_14002_1012459664}

[[发向该客户端报文数]{style="font-family:宋体"}]{#struct_0_25005_14002_x825972082}

[[Sent-Bytes]{lang="EN-US"}]{#struct_0_25005_14002_2145381115}

[[发向该客户端数据字节数]{style="font-family:宋体"}]{#struct_0_25005_14002_372943692}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1262075223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta]{lang="EN-US"}**]{#struct_0_25005_14002_791274036}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta relay status]{lang="EN-US"}**]{#struct_0_25005_14002_x267523372}

::: {#1254026727 .myid}
[]{#_Toc404786047}[]{#struct_0_25005_14002_1227063033}[]{#_Toc353818138}

**RTC终端接入 \-- RTC终端接入命令 \-- display rta relay status**

------------------------------------------------------------------------

[**[display rta relay status]{lang="EN-US"}**]{#struct_0_25005_14002_209031602}[命令用来显示中继服务接受的所有客户端的连接状态。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_179582145}

[**[display rta relay status]{lang="EN-US"}**]{#struct_0_25005_14002_2022630158}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1771775910}

[[任意视图]{style="font-family:宋体"}]{#struct_0_25005_14002_64000629}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1190450553}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_367024164}

[[network-operator]{lang="EN-US"}]{#struct_0_25005_14002_x92096605}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1706092412}

[[mdc-operator]{lang="EN-US"}]{#struct_0_25005_14002_745064781}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_757193255}

[[对于每个转发组（以端口区分）最多可以接受]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_25005_14002_x1741224542}[个客户端的连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_331676042}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1975188676}[显示中继服务接受的客户端的连接状态。]{style="font-family:宋体"}

[[\<Sysname\> display rta relay status]{lang="EN-US"}]{#struct_0_25005_14002_x1969975277}

[Server-ID   Port   Client-ID    Client-IP        State]{lang="EN-US"}

[0           1026   0            1.1.1.2          Linked]{lang="EN-US"}

[0           1026   1            1.1.1.3          Linked]{lang="EN-US"}

[1           1027   0            1.1.1.4          Linking]{lang="EN-US"}

[1           1027   2            1.1.1.6          Linked]{lang="EN-US"}

[]{#struct_0_25005_14002_x1647240980}[[表]{style="font-family:黑体"}[1-7 ]{lang="EN-US"}]{#_Toc353120941}[display rta relay status]{lang="FR"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1413431798}[[字段]{style="font-family:黑体"}]{#struct_0_25005_14002_1666378445}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_25005_14002_x375633388}

[[Server-ID]{lang="EN-US"}]{#struct_0_25005_14002_1640986468}

[[转发组]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_25005_14002_x1520531694}

[[Port]{lang="EN-US"}]{#struct_0_25005_14002_x707395561}

[[转发组监听端口]{style="font-family:宋体"}]{#struct_0_25005_14002_x1929037791}

[[Client-ID]{lang="EN-US"}]{#struct_0_25005_14002_1884779242}

[[客户端在转发组内的标识]{style="font-family:宋体"}]{#struct_0_25005_14002_730482392}

[[Client-IP]{lang="EN-US"}]{#struct_0_25005_14002_2005505743}

[[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_25005_14002_341794455}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_25005_14002_1546615377}

[[客户端协商状态：]{style="font-family:宋体"}]{#struct_0_25005_14002_x1979259459}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linking]{lang="EN-US"}]{#struct_0_25005_14002_x904654314}[：客户端还未发送协商字段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Linked]{lang="EN-US"}]{#struct_0_25005_14002_257934351}[：客户端已完成协商过程]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1232772222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta]{lang="EN-US"}**]{#struct_0_25005_14002_2140143090}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_237552224}

::: {#1676018475 .myid}
[]{#_Toc404786048}[]{#struct_0_25005_14002_x1878715933}[]{#_Toc353818124}

**RTC终端接入 \-- RTC终端接入命令 \-- driverbuf save**

------------------------------------------------------------------------

[**[driverbuf save]{lang="EN-US"}**]{#struct_0_25005_14002_x368634421}[命令用来配置终端接入设备在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立后不清空终端接收缓存。]{style="font-family:宋体"}

[**[undo driverbuf save]{lang="EN-US"}**]{#struct_0_25005_14002_1206645744}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_56453803}

[**[driverbuf save]{lang="EN-US"}**]{#struct_0_25005_14002_x19468564}

[**[undo driverbuf save]{lang="EN-US"}**]{#struct_0_25005_14002_x697859012}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_1393233206}

[[终端接入设备在]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x272827618}[连接建立后清空终端接收缓存。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_417548809}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_644643753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1746263753}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x207302783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_545720275}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1139092244}

[[终端接收缓存是指在终端接入设备上用于存放终端数据的缓存。]{style="font-family:宋体"}]{#struct_0_25005_14002_x321388971}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_369665494}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1759501604}[配置在]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接建立后不清空终端接收缓存。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1585552505}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] driverbuf save]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_297696338}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[drive]{lang="EN-US"}**]{#struct_0_25005_14002_x2140693552}**[r]{lang="EN-US"}[buf size]{lang="EN-US"}**
:::

::: {#146670375 .myid}
[]{#_Toc404786049}[]{#struct_0_25005_14002_x880480744}[]{#_Toc353818125}

**RTC终端接入 \-- RTC终端接入命令 \-- driverbuf size**

------------------------------------------------------------------------

[**[driverbuf size]{lang="EN-US"}**]{#struct_0_25005_14002_x581548818}[命令用来配置终端接收缓存的大小。]{style="font-family:宋体"}

[**[undo driverbuf size]{lang="EN-US"}**]{#struct_0_25005_14002_420061169}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_892699713}

[**[driverbuf size]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_25005_14002_x110700042}

[**[undo driverbuf size]{lang="EN-US"}**]{#struct_0_25005_14002_548590268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1271038935}

[[终端接收缓存大小为]{style="font-family:宋体"}[8KB]{lang="EN-US"}]{#struct_0_25005_14002_x879116836}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x973554275}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1107569457}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2032998528}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1143330850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1799470090}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1630441212}

[*[size]{lang="EN-US"}*]{#struct_0_25005_14002_1240506364}[：缓存大小，取值范围为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}*[。]{style="font-family:宋体"}*

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1510311819}

[[只有将模板重新应用到接口下，该命令配置才能生效。]{style="font-family:宋体"}]{#struct_0_25005_14002_294097067}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1974782459}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_655002330}[配置终端缓存大小为]{style="font-family:宋体"}[8KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_2059381178}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] driverbuf size 8]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1589945167}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[drivebuf save]{lang="EN-US"}**]{#struct_0_25005_14002_2128657751}
:::

::: {#-1526888109 .myid}
[]{#_Toc404786050}[]{#struct_0_25005_14002_x1188449525}[]{#_Toc353818126}

**RTC终端接入 \-- RTC终端接入命令 \-- idle-timeout**

------------------------------------------------------------------------

[**[idle-timeout]{lang="EN-US"}**]{#struct_0_25005_14002_1978404512}[命令用来设置终端接入]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的空闲超时时间。]{style="font-family:宋体"}

[**[undo idle-timeout]{lang="EN-US"}**]{#struct_0_25005_14002_x422753091}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1242079403}

[**[idle-timeout ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_25005_14002_585193165}

[**[undo idle-timeout]{lang="EN-US"}**]{#struct_0_25005_14002_x1636917656}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x823586690}

[[连接永不超时。]{style="font-family:宋体"}]{#struct_0_25005_14002_x43706356}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1404786248}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_460983491}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1563566103}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_178355598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x699875875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1911784568}

[*[seconds]{lang="EN-US"}*]{#struct_0_25005_14002_1067243318}[：空闲超时时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1988837032}

[[如果设置了空闲超时时间，终端接入连接在设置的时间内没有接收到任何数据，则断开当前的连接。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1569980813}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_945870281}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1673222531}[配置终端接入的空闲超时时间为]{style="font-family:宋体"}[1000]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_128196221}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] idle-timeout 1000]{lang="EN-US"}
:::

::: {#-1991042285 .myid}
[]{#_Toc404786051}[]{#struct_0_25005_14002_1862110486}[]{#_Toc356809981}

**RTC终端接入 \-- RTC终端接入命令 \-- link-protocol stlp**

------------------------------------------------------------------------

[**[link-protocol stlp]{lang="EN-US"}**]{#struct_0_25005_14002_x1387637851}[命令用来配置接口封装的链路层协议为]{style="font-family:宋体"}[STLP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo link-protocol stlp]{lang="EN-US"}**]{#struct_0_25005_14002_x1379176401}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_754298442}

[**[link-protocol stlp]{lang="EN-US"}**]{#struct_0_25005_14002_x153331510}

[**[undo link-protocol stlp]{lang="EN-US"}**]{#struct_0_25005_14002_1025932686}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1499587593}

[[除以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_25005_14002_x763352332}[接口外，其它接口封装的链路层协议均为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1745095221}

[[接口视图]{style="font-family:宋体"}]{#struct_0_25005_14002_740046323}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_353998050}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x957412463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_141494617}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_220589367}

[[STLP]{lang="EN-US"}]{#struct_0_25005_14002_x968777267}[为链路层协议，用于远程终端连接同步透传功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1833980322}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x680389646}[配置接口]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[封装]{style="font-family:宋体"}[STLP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1512500121}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] link-protocol stlp]{lang="EN-US"}
:::

::: {#-91211862 .myid}
[]{#_Toc404786052}[]{#struct_0_25005_14002_1062942866}[]{#_Toc353818132}

**RTC终端接入 \-- RTC终端接入命令 \-- resetkey**

------------------------------------------------------------------------

[**[resetkey]{lang="EN-US"}**]{#struct_0_25005_14002_x1500234787}[命令用来设置终端复位的热键。]{style="font-family:宋体"}

[**[undo resetkey]{lang="EN-US"}**]{#struct_0_25005_14002_136880709}[用来取消配置的热键。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x826037618}

[**[resetkey ]{lang="EN-US"}***[ascii-code&\<1-3\>]{lang="EN-US"}*]{#struct_0_25005_14002_x1108309032}

[**[undo resetkey]{lang="EN-US"}**]{#struct_0_25005_14002_x527712644}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_273476276}

[[没有设置终端复位热键。]{style="font-family:宋体"}]{#struct_0_25005_14002_x53546570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x640836725}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_462509617}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_838808995}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_687956163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x528637409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_878218494}

[*[ascii-code&\<1-3\>]{lang="EN-US"}*]{#struct_0_25005_14002_492659593}[：热键的]{style="font-family:
宋体"}[ASCII]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-3\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1492107568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果设置了终端复位热键，当终端出现异常时，在终端上按终端复位热键后，]{style="font-family:宋体"}]{#struct_0_25005_14002_x991507157}[RTC Client]{lang="EN-US"}[断开并重新建立与]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要注意的是，热键的]{style="font-family:宋体"}]{#struct_0_25005_14002_1190385017}[ASCII]{lang="EN-US"}[值不能与设备上已设置的别的功能热键的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[值相同，否则，热键的功能将冲突。另外，在终端显示大量数据时使用热键，会影响热键的响应速度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1612400990}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1827981834}[配置终端复位的热键为]{style="font-family:宋体"}[\<Ctrl+A\>]{lang="EN-US"}[，其对应的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1235855187}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] resetkey 1]{lang="EN-US"}
:::

::: {#1821402706 .myid}
[]{#_Toc404786053}[]{#struct_0_25005_14002_x1456157420}[]{#_Toc353818133}

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta connection**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **rta** **connection**]{lang="EN-US"}]{#struct_0_25005_14002_x206946385}[命令用来强制断开指定终端的虚终端对应的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x305014011}

[**[reset rta connection ]{lang="EN-US"}***[terminal-number vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1554201879}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1375526966}

[[用户视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x81255531}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x458870704}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1790971123}

[[network-operator]{lang="EN-US"}]{#struct_0_25005_14002_182780493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x375698924}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_927489511}[：终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x2073513625}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1302854279}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_2079454547}[断开终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[\<Sysname\> reset rta connection 1 1]{lang="EN-US"}]{#struct_0_25005_14002_1309014898}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_841610829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_2011808684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta statistics]{lang="EN-US"}**]{#struct_0_25005_14002_1516674172}
:::

::: {#814050154 .myid}
[]{#_Toc404786054}[]{#struct_0_25005_14002_1442371401}[]{#_Toc353818134}

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta relay statistics**

------------------------------------------------------------------------

[**[reset rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_838776980}[命令用来清除连接到中继服务器的所有客户端的报文统计信息**。**]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1443143493}

[**[reset rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_2079526993}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1546549841}

[[用户视图]{style="font-family:宋体"}]{#struct_0_25005_14002_762469537}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1620884321}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1648926611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1075485038}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1929007601}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1179425488}[清除客户端的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rta relay statistics]{lang="EN-US"}]{#struct_0_25005_14002_723030620}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1214836226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta connection]{lang="EN-US"}**]{#struct_0_25005_14002_x1460808398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta statistics]{lang="EN-US"}**]{#struct_0_25005_14002_x1962046753}
:::

::: {#-943749569 .myid}
[]{#_Toc404786055}[]{#struct_0_25005_14002_x850147197}[]{#_Toc353818135}

**RTC终端接入 \-- RTC终端接入命令 \-- reset rta statistics**

------------------------------------------------------------------------

[**[reset rta statistics]{lang="EN-US"}**]{#struct_0_25005_14002_1098629570}[命令用来清除指定终端的统计信息*。*]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x19534100}

[**[reset rta statistics ]{lang="EN-US"}***[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_1681830185}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_28538481}

[[用户视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1124288061}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1673176159}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x128304534}

[[network-operator]{lang="EN-US"}]{#struct_0_25005_14002_x387502450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1316117402}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_401439137}[：终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_503216993}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x835505100}[清除终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的终端的所有统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rta statistics 1]{lang="EN-US"}]{#struct_0_25005_14002_x806970515}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x443027000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta connection]{lang="EN-US"}**]{#struct_0_25005_14002_x1585618041}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset rta relay statistics]{lang="EN-US"}**]{#struct_0_25005_14002_730689189}
:::

::: {#-1754979832 .myid}
[]{#_Toc404786056}[]{#struct_0_25005_14002_1082294270}[]{#_Toc353818139}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay buffer-size**

------------------------------------------------------------------------

[**[rta relay buffer-size]{lang="EN-US"}**]{#struct_0_25005_14002_670190113}[命令用来配置中继透传服务客户端转发缓存大小。]{style="font-family:宋体"}

[**[undo rta relay buffer-size]{lang="EN-US"}**]{#struct_0_25005_14002_x12354651}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1560614916}

[**[rta relay buffer-size]{lang="EN-US"}**[ *buffer-size*]{lang="EN-US"}]{#struct_0_25005_14002_1240737270}

[**[undo rta relay buffer-size]{lang="EN-US"}**]{#struct_0_25005_14002_1902574709}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x5835341}

[[客户端转发缓存大小为]{style="font-family:宋体"}[8KB]{lang="EN-US"}]{#struct_0_25005_14002_x1664862054}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_2081618878}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_904644190}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1075325547}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1143265314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1705109062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1073595069}

[*[buffer-size]{lang="EN-US"}*]{#struct_0_25005_14002_x1955633171}[：客户端转发缓存大小，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1559547965}

[[如果客户端待发送报文数达到配置的缓存大小，则新增数据会覆盖旧的数据。该配置和]{style="font-family:宋体"}**[rta relay tcp sendbuf-size]{lang="EN-US"}**]{#struct_0_25005_14002_x838601682}[不同之处在于后者设置的是传输层报文发送缓冲区的大小，如果后者设置的值过小，会影响发送效率但不会丢包。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1502974398}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1341892688}[配置中继透传服务客户端转发缓存大小为]{style="font-family:宋体"}[2KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1223388960}

[\[Sysname\] rta relay buffer-size 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_847173849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp sendbuf-size]{lang="EN-US"}**]{#struct_0_25005_14002_x716133972}
:::

::: {#-887426505 .myid}
[]{#_Toc404786057}[]{#struct_0_25005_14002_2125886533}[]{#_Toc353818140}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay disconnect**

------------------------------------------------------------------------

[**[rta relay disconnect]{lang="EN-US"}**]{#struct_0_25005_14002_1822833956}[命令用来强制断开全部或者指定的客户端连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_343642284}

[**[rta relay disconnect ]{lang="EN-US"}**[{ *server-id client-id* \| **all** }]{lang="EN-US"}]{#struct_0_25005_14002_x422818627}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x873158986}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1527602460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_662445261}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_832372395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x112284878}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1595974752}

[*[server-id]{lang="EN-US"}*]{#struct_0_25005_14002_982526452}[：转发组]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[client-id]{lang="EN-US"}*]{#struct_0_25005_14002_1372815164}[：转发组内某一客户端的标识，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1755550166}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1476516757}[断开所有客户端连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x627190733}

[\[Sysname\] rta relay disconnect all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1123352789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display rta relay status]{lang="EN-US"}**]{#struct_0_25005_14002_x1988902568}
:::

::: {#2070379495 .myid}
[]{#_Toc404786058}[]{#struct_0_25005_14002_1255375229}[]{#_Toc353818141}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay enable**

------------------------------------------------------------------------

[**[rta relay enable]{lang="EN-US"}**]{#struct_0_25005_14002_986701359}[命令用来开启中继服务器中继转发功能。]{style="font-family:宋体"}

[**[undo rta relay enable]{lang="EN-US"}**]{#struct_0_25005_14002_1484050220}[命令用来关闭中继服务器中继转发功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1883142004}

[**[rta relay enable]{lang="EN-US"}**]{#struct_0_25005_14002_x1908568547}

[**[undo rta relay enable]{lang="EN-US"}**]{#struct_0_25005_14002_x659238104}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x28797250}

[[中继转发功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_25005_14002_x818062311}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x857020286}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1890382237}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2014548067}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1043400070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x58309809}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2108514522}

[[中继服务器仅应用于]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_739980787}[的多（]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[）对一（中继服务器）方式透传。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_810792139}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_841200428}[开启中继服务器中继转发功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x849350366}

[\[Sysname\] rta relay enable]{lang="EN-US"}
:::

::: {#35667058 .myid}
[]{#_Toc404786059}[]{#struct_0_25005_14002_x387444493}[]{#_Toc353818142}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay listen-port**

------------------------------------------------------------------------

[**[rta relay listen-port]{lang="EN-US"}**]{#struct_0_25005_14002_518395741}[命令用来设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听端口。]{style="font-family:宋体"}

[**[undo rta relay listen-port]{lang="EN-US"}**]{#struct_0_25005_14002_x1096760519}[命令用来删除]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[监听端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_352968459}

[**[rta relay listen-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_25005_14002_x292005588}

[**[undo rta relay]{lang="EN-US"}**[ **listen-port** *port-number*]{lang="EN-US"}]{#struct_0_25005_14002_312967946}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x836287207}

[[不存在]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x1717009376}[监听端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1959520832}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x96197523}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x826103154}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1888330077}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_141458025}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_605815935}

[*[port-number]{lang="EN-US"}*]{#struct_0_25005_14002_1169307499}[：本端]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1740407845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个转发组最多可以接受]{style="font-family:宋体"}]{#struct_0_25005_14002_257817670}[10]{lang="EN-US"}[个客户端的连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统最多支持]{style="font-family:宋体"}]{#struct_0_25005_14002_1210442694}[64]{lang="EN-US"}[个端口，每个端口上建立的连接会组成一个转发组，该群组内某终端数据会在组内广播转发。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除监听端口时如果此端口存在客户端连接，则断开连接到此端口的所有客户端连接。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1702945934}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x361464035}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1369306033}[设置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听端口]{style="font-family:宋体"}[1026]{lang="EN-US"}[和]{style="font-family:宋体"}[1027]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x365883500}

[\[Sysname\] rta relay listen-port 1026]{lang="EN-US"}

[\[Sysname\] rta relay listen-port 1027]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1190319481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay enable]{lang="EN-US"}**]{#struct_0_25005_14002_x753254571}
:::

::: {#997026948 .myid}
[]{#_Toc404786060}[]{#struct_0_25005_14002_990060405}[]{#_Toc353818143}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp**

------------------------------------------------------------------------

[**[rta relay tcp]{lang="EN-US"}**]{#struct_0_25005_14002_2068976567}[命令用于配置中继透传服务器和客户端之间]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的发送和接收缓冲区大小。]{style="font-family:宋体"}

[**[undo rta relay tcp]{lang="EN-US"}**]{#struct_0_25005_14002_761069982}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_704977591}

[**[rta relay tcp]{lang="EN-US"}**[ { **recvbuf-size** *recvbuff-size \|* **sendbuf-size** *sendbuff-size* }]{lang="EN-US"}]{#struct_0_25005_14002_655346619}

[**[undo rta relay tcp]{lang="EN-US"}**[ { **recvbuf-size** \| **sendbuf-size** }]{lang="EN-US"}]{#struct_0_25005_14002_x771863812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_1237677982}

[[中继透传服务器和客户端之间]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_1508554512}[连接的发送和接收缓冲区大小为]{style="font-family:宋体"}[2048]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x32246351}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_259350312}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1930751611}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1176346656}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x375764460}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x321792756}

[*[recvbuff-size]{lang="EN-US"}*]{#struct_0_25005_14002_x1976440146}[：]{style="font-family:宋体"}[socket]{lang="EN-US"}[接收缓冲区的大小，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[*[sendbuff-size]{lang="EN-US"}*]{#struct_0_25005_14002_805900404}[：]{style="font-family:宋体"}[socket]{lang="EN-US"}[发送缓冲区的大小，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_50555954}

[[如果过大会影响数据转发的及时性，如果过小，会造成系统负担过大，不建议更改此值。]{style="font-family:宋体"}]{#struct_0_25005_14002_1115672014}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_694557612}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1040291352}[配置中继透传服务]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的发送缓冲区和接受缓冲区大小分别为]{style="font-family:宋体"}[8194]{lang="EN-US"}[字节和]{style="font-family:宋体"}[2046]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_399450893}

[\[Sysname\] rta relay tcp sendbuf-size 8194]{lang="EN-US"}

[\[Sysname\] rta relay tcp recvbuf-size 2046]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_295218107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp keepalive]{lang="EN-US"}**]{#struct_0_25005_14002_x1961122931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_x1181477546}
:::

::: {#-338132750 .myid}
[]{#_Toc404786061}[]{#struct_0_25005_14002_1546484305}[]{#_Toc353818144}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp keepalive**

------------------------------------------------------------------------

[**[rta relay tcp keepalive]{lang="EN-US"}**]{#struct_0_25005_14002_x430411547}[命令用来配置中继服务器和客户端之间]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的保活属性。]{style="font-family:宋体"}

[**[undo rta relay tcp keepalive]{lang="EN-US"}**]{#struct_0_25005_14002_x965775876}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x557619091}

[**[rta relay tcp keepalive ]{lang="EN-US"}***[time count]{lang="EN-US"}*]{#struct_0_25005_14002_x1093131504}

[**[undo rta relay tcp keepalive]{lang="EN-US"}**]{#struct_0_25005_14002_x483333488}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_805031926}

[[中继透传服务器和客户端之间]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_1732865850}[连接的保活报文发送间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒、发送次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_2092813584}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1260514651}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x358537838}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_839631404}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1788888327}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_94556563}

[*[time]{lang="EN-US"}*]{#struct_0_25005_14002_x19599636}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接保活报文发送间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[7200]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_25005_14002_x688582726}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接保活报文发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1307878506}

[[这里使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_2137643933}[本身的保活功能探测客户端可达性，若探测失败则断开对应的客户端。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x530350730}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1174856270}[配置中继透传服务]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接的保活报文发送间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒、发送次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x966594650}

[\[Sysname\] rta relay tcp keepalive 100 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1106447466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp]{lang="EN-US"}**]{#struct_0_25005_14002_958640278}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_341617495}
:::

::: {#-1401864430 .myid}
[]{#_Toc404786062}[]{#struct_0_25005_14002_119656181}[]{#_Toc353818145}

**RTC终端接入 \-- RTC终端接入命令 \-- rta relay tcp nodelay**

------------------------------------------------------------------------

[**[rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_x359406736}[命令用来开启中继服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[无延时功能。]{style="font-family:宋体"}

[**[undo rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_x1585683577}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_120986697}

[**[rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_1843268637}

[**[undo rta relay tcp nodelay]{lang="EN-US"}**]{#struct_0_25005_14002_1164634349}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1082317326}

[[中继服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x1491136249}[无延时功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1399477758}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_2100390379}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1177884355}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_876742254}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1903908386}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1572616285}

[[通过开启中继服务器的]{style="font-family:宋体"}[TCP ]{lang="EN-US"}]{#struct_0_25005_14002_2072288861}[无延时功能来关闭]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的]{style="font-family:宋体"}[Nagle]{lang="EN-US"}[算法，可减少]{style="font-family:宋体"}[Nagle]{lang="EN-US"}[算法对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文收发造成的时延，以提高中继服务器转发性能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1723628698}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1805697517}[开启中继服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[无延时功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1143199778}

[\[Sysname\] rta relay tcp nodelay]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_837573933}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp]{lang="EN-US"}**]{#struct_0_25005_14002_122500375}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta relay tcp keepalive]{lang="EN-US"}**]{#struct_0_25005_14002_x1249013324}
:::

::: {#16662440 .myid}
[]{#_Toc404786063}[]{#struct_0_25005_14002_258911956}[]{#_Toc353818163}

**RTC终端接入 \-- RTC终端接入命令 \-- rta rtc compatibility**

------------------------------------------------------------------------

[**[rta rtc compatibility enable]{lang="EN-US"}**]{#struct_0_25005_14002_x1332004276}[命令用来开启终端接入兼容模式。]{style="font-family:
宋体"}

[**[undo rta rtc compatibility enable]{lang="EN-US"}**]{#struct_0_25005_14002_x2019397406}[命令用来关闭终端接入兼容模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1716563483}

[**[rta rtc compatibility enable]{lang="EN-US"}**]{#struct_0_25005_14002_x1827321603}

[**[undo rta rtc compatibility enable]{lang="EN-US"}**]{#struct_0_25005_14002_x1214730347}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_1006782924}

[[终端接入兼容模式处于关闭状态。]{style="font-family:宋体"}]{#struct_0_25005_14002_x112641451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1609326151}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_40176965}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_25005_14002_2416129}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x422884163}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x856215698}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1887021783}

[[对于]{style="font-family:宋体"}[Comware V3]{lang="EN-US"}]{#struct_0_25005_14002_x964432891}[、]{style="font-family:宋体"}[Comware V5]{lang="EN-US"}[设备，有的版本上]{style="font-family:宋体"}[RTC]{lang="EN-US"}[数据传输机制工作在特性模式，有的版本工作在兼容模式。只有当]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[与]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[两端都工作在同一模式下时才能正常数据传输。]{style="font-family:宋体"}[Comware V7]{lang="EN-US"}[设备缺省工作在特性模式下，对于工作在兼容模式的]{style="font-family:宋体"}[Comware V3]{lang="EN-US"}[、]{style="font-family:宋体"}[Comware V5]{lang="EN-US"}[设备，需要开启兼容模式才能与之互通。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x931460479}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_777446040}[开启终端接入兼容模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_557652636}

[\[Sysname\] rta rtc compatible enable]{lang="EN-US"}
:::

::: {#-1942046267 .myid}
[]{#_Toc404786064}[]{#struct_0_25005_14002_2135220239}[]{#_Toc353818146}

**RTC终端接入 \-- RTC终端接入命令 \-- rta rtc-server listen-port**

------------------------------------------------------------------------

[**[rta rtc-server listen-port]{lang="EN-US"}**]{#struct_0_25005_14002_1972176983}[命令用来配置]{style="font-family:
宋体"}[RTC Server]{lang="EN-US"}[的监听端口。]{style="font-family:
宋体"}

[**[undo rta rtc-server listen-port]{lang="EN-US"}**]{#struct_0_25005_14002_467333250}[命令用来取消配置的监听端口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_127273242}

[**[rta rtc-server listen-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_25005_14002_438050270}

[**[undo rta rtc-server listen-port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_25005_14002_1681946972}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1988968104}

[[没有指定专门的]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}]{#struct_0_25005_14002_890664283}[监听端口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_2140886014}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x530351444}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_784887218}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1954955802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1278157597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1519070367}

[*[port-number]{lang="EN-US"}*]{#struct_0_25005_14002_620963964}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[服务器端的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[监听端口号，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x91611474}

[[只支持开启一个监听端口。]{style="font-family:宋体"}]{#struct_0_25005_14002_x930175870}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1527211260}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1354621828}[配置]{style="font-family:宋体"}[RTC-server]{lang="EN-US"}[监听端口号为]{style="font-family:宋体"}[9010]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_409841714}

[\[Sysname\] rta rtc-server listen-port 9010]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_739915251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta server enable]{lang="EN-US"}**]{#struct_0_25005_14002_882857427}
:::

::: {#1890253550 .myid}
[]{#_Toc404786065}[]{#struct_0_25005_14002_x1646495051}[]{#_Toc353818147}

**RTC终端接入 \-- RTC终端接入命令 \-- rta server enable**

------------------------------------------------------------------------

[**[rta server enable]{lang="EN-US"}**]{#struct_0_25005_14002_x474141067}[命令用来开启路由器的终端接入功能。]{style="font-family:宋体"}

[**[undo rta server enable]{lang="EN-US"}**]{#struct_0_25005_14002_1736412507}[命令用来关闭终端接入功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_606404044}

[**[rta server enable]{lang="EN-US"}**]{#struct_0_25005_14002_x103991741}

[**[undo rta server enable]{lang="EN-US"}**]{#struct_0_25005_14002_1045390942}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_617235445}

[[路由器的终端接入功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_25005_14002_1516497230}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x138708674}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_877299597}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x40653426}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1619934287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x826168690}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1963369894}

[[关闭终端接入功能后，对模板、终端及虚终端的设置将会被保留，不会自动取消。]{style="font-family:宋体"}]{#struct_0_25005_14002_784278443}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_878270238}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1101355079}[开启终端接入功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x558969879}

[\[Sysname\] rta server enable]{lang="EN-US"}
:::

::: {#-1052215301 .myid}
[]{#_Toc404786066}[]{#struct_0_25005_14002_269230887}[]{#_Toc353818148}

**RTC终端接入 \-- RTC终端接入命令 \-- rta source-ip**

------------------------------------------------------------------------

[**[rta source-ip]{lang="EN-US"}**]{#struct_0_25005_14002_1263576751}[命令用来配置全局的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址。]{style="font-family:宋体"}

[**[undo rta source-ip]{lang="EN-US"}**]{#struct_0_25005_14002_1042419400}[命令用来取消配置的源地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1476091077}

[**[rta source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_25005_14002_1976615025}

[**[undo rta source-ip]{lang="EN-US"}**]{#struct_0_25005_14002_599495316}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1721702197}

[[全局范围内没有配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x945398221}[连接的源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1190253945}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_5241634}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_25005_14002_418095}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1636277109}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1180217254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1007277448}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_x140541439}[：建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接使用的源地址，该地址不能是环回地址（如]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_636257737}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不采用发起方终端接入设备的出接口地址作为]{style="font-family:宋体"}]{#struct_0_25005_14002_x1129814600}[TCP]{lang="EN-US"}[连接源地址，可使用本命令另外指定源地址。一般借用终端接入设备]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[口或]{style="font-family:宋体"}[Dialer]{lang="EN-US"}[口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址，用于拨号备份和地址隐藏。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在终端模板下也配置了源地址，则应用该终端模板的终端在建立]{style="font-family:宋体"}]{#struct_0_25005_14002_x838810030}[TCP]{lang="EN-US"}[连接时，优先使用终端模板下配置的源地址作为]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置了全局的]{style="font-family:宋体"}]{#struct_0_25005_14002_x1915559144}[TCP]{lang="EN-US"}[连接源地址后，必须重新建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接，该地址才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1284330997}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1081837682}[设置全局的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接源地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x375829996}

[\[Sysname\] rta source-ip 1.1.1.1]{lang="EN-US"}
:::

::: {#-841210834 .myid}
[]{#_Toc404786067}[]{#struct_0_25005_14002_x1784288873}[]{#_Toc353818149}

**RTC终端接入 \-- RTC终端接入命令 \-- rta template**

------------------------------------------------------------------------

[**[rta template]{lang="EN-US"}**]{#struct_0_25005_14002_476115281}[命令用来创建终端模板，并进入终端模板视图。]{style="font-family:宋体"}

[**[undo rta template]{lang="EN-US"}**]{#struct_0_25005_14002_x1626921058}[命令用来删除终端模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1184511509}

[**[rta template]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_25005_14002_x430118038}

[**[undo rta template]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_25005_14002_544376551}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1513302615}

[[没有配置终端模板。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1161426106}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1476928027}

[[系统视图]{style="font-family:宋体"}]{#struct_0_25005_14002_68652806}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_687424296}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1385824136}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1546418769}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1260984281}

[*[template-name]{lang="EN-US"}*]{#struct_0_25005_14002_x912748651}[：终端模板名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1279358869}

[[如果指定的模板已创建，则直接进入该终端模板视图。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1177710512}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_794317176}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_996581066}[创建终端模板]{style="font-family:宋体"}[abc]{lang="EN-US"}[，并进入该模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1360818786}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\]]{lang="EN-US"}
:::

::: {#-1137061333 .myid}
[]{#_Toc404786068}[]{#struct_0_25005_14002_x916279820}[]{#_Toc353818150}

**RTC终端接入 \-- RTC终端接入命令 \-- rta terminal**

------------------------------------------------------------------------

[**[rta terminal]{lang="EN-US"}**]{#struct_0_25005_14002_x2054684106}[命令用来将模板应用到接口。]{style="font-family:宋体"}

[**[undo rta terminal]{lang="EN-US"}**]{#struct_0_25005_14002_x2146592925}[命令用来取消该应用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1619902221}

[**[rta terminal ]{lang="EN-US"}***[template-name terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_1735203529}

[**[undo rta terminal]{lang="EN-US"}**]{#struct_0_25005_14002_x1981707787}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x19665172}

[[接口下没有应用任何模板。]{style="font-family:宋体"}]{#struct_0_25005_14002_354136522}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x25895645}

[[异步串口视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1484797769}

[[同]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_25005_14002_262853864}[异步串口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x642003875}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1234134067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_723012043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x430048391}

[*[template-name]{lang="EN-US"}*]{#struct_0_25005_14002_x1783134594}[：终端模板名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_1728655171}[：终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1630349881}

[[模板配置完成后需要应用到相应接口上才可以创建相应的终端，实现终端接入的功能，其终端号由配置的]{style="font-family:宋体"}*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_x8227558}[决定。一个接口只能连接一个物理终端，不同的物理终端通过终端号来标识。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2073508659}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_965946438}[在接口应用终端模板]{style="font-family:宋体"}[abc]{lang="EN-US"}[，终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1585749113}

[\[Sysname\] interface async 2/2/1]{lang="EN-US"}

[\[Sysname-rta-async2/2/1\] rta terminal abc 1]{lang="PT-BR"}
:::

::: {#-1100045490 .myid}
[]{#_Toc404786069}[]{#struct_0_25005_14002_x1836240907}[]{#_Toc353818151}

**RTC终端接入 \-- RTC终端接入命令 \-- rta terminal backup**

------------------------------------------------------------------------

[**[rta terminal backup]{lang="EN-US"}**]{#struct_0_25005_14002_1407250711}[命令用来将终端模板应用到备份接口。]{style="font-family:宋体"}

[**[undo rta terminal backup]{lang="EN-US"}**]{#struct_0_25005_14002_1572414507}[命令用来在备份接口下取消终端模板应用。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x717879570}

[**[rta terminal ]{lang="EN-US"}***[template-name terminal-number]{lang="EN-US"}*[ **backup**]{lang="EN-US"}]{#struct_0_25005_14002_509608796}

[**[undo rta terminal backup]{lang="EN-US"}**]{#struct_0_25005_14002_x956122046}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_124258508}

[[没有将终端模板应用到备份接口。]{style="font-family:宋体"}]{#struct_0_25005_14002_x602217110}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1227443857}

[[接口视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1734054184}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_373637798}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1835839086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x79281064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1143134242}

[*[template-name]{lang="EN-US"}*]{#struct_0_25005_14002_1316778319}[：终端模板名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_x11032163}[：终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_968973732}

[[当主链路在恢复稳定后，备份链路重新切回到主链路上处理业务。]{style="font-family:宋体"}]{#struct_0_25005_14002_1409741575}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_988911659}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1540522342}[在接口应用终端模板]{style="font-family:宋体"}[abc]{lang="EN-US"}[，终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[，该接口为备份链路的接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_437755127}

[\[Sysname\] interface async 2/2/1]{lang="EN-US"}

[\[Sysname-rta-async2/2/1\] rta terminal abc 1 backup]{lang="PT-BR"}
:::

::: {#974378914 .myid}
[]{#_Toc404786070}[]{#struct_0_25005_14002_x1961514095}[]{#_Toc353818131}

**RTC终端接入 \-- RTC终端接入命令 \-- rtc-multipeer remote**

------------------------------------------------------------------------

[**[rtc-multipeer remote]{lang="EN-US"}**]{#struct_0_25005_14002_x1316352670}[命令用来在接收一对多连接的]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}[类型的虚终端上配置客户端列表。]{style="font-family:宋体"}

[**[undo rtc-multipeer remote]{lang="EN-US"}**]{#struct_0_25005_14002_x1933331199}[命令用来删除指定虚终端的客户端列表。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x422949699}

[**[rtc-multipeer ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **remote** *ip-address port-number*]{lang="EN-US"}]{#struct_0_25005_14002_1865358137}

[**[undo rtc-multipeer]{lang="EN-US"}***[ vty-number]{lang="EN-US"}***[ remote ]{lang="EN-US"}***[ip-address port-number]{lang="EN-US"}*]{#struct_0_25005_14002_2020847386}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1609387580}

[[没有配置虚终端上客户端列表。]{style="font-family:宋体"}]{#struct_0_25005_14002_x765162689}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1579223534}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1231858146}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x876037905}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1513469790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_392860766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1281537803}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_719901856}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_1823513169}[：客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1989033640}[：客户端]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x925112444}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需先创建]{style="font-family:宋体"}]{#struct_0_25005_14002_x1587746297}[UDP_1N_Server]{lang="EN-US"}[类型的虚终端才可以配置客户端列表，同一个虚终端下最多可以配置]{style="font-family:宋体"}[10]{lang="EN-US"}[个客户端。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除]{style="font-family:宋体"}]{#struct_0_25005_14002_2142002636}[UDP_1N_Server]{lang="EN-US"}[类型的虚终端时，该虚终端下配置的客户端列表也会被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP_1N_Server]{lang="EN-US"}]{#struct_0_25005_14002_1697861154}[类型的虚终端的配置可参考命令]{lang="EN-US" style="font-family:宋体"}**[vty rtc-multipeer]{lang="EN-US"}**[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x582425842}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1015909364}[在接收一对多连接的]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}[类型的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[上配置客户端列表。]{style="font-family:宋体"}

[[客户端]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_25005_14002_2044343357}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口为]{style="font-family:宋体"}[1024]{lang="EN-US"}

[[客户端]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_25005_14002_x1356217838}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.3]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口为]{style="font-family:宋体"}[1025]{lang="EN-US"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x26893130}

[\[Sysname\] rta template temp3]{lang="EN-US"}

[\[Sysname-rta-template-temp3\] vty 1 rtc-multipeer 1.1.1.1 1024]{lang="EN-US"}

[\[Sysname-rta-template-temp3\] rtc-multipeer 1 remote 1.1.1.2 1024]{lang="EN-US"}

[\[Sysname-rta-template-temp3\] rtc-multipeer 1 remote 1.1.1.3 1025]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_259823172}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-multipeer]{lang="EN-US"}**]{#struct_0_25005_14002_x1614293168}
:::

::: {#-1466014746 .myid}
[]{#_Toc404786071}[]{#struct_0_25005_14002_739849715}[]{#_Toc353818127}

**RTC终端接入 \-- RTC终端接入命令 \-- sendbuf bufsize**

------------------------------------------------------------------------

[**[sendbuf bufsize]{lang="EN-US"}**]{#struct_0_25005_14002_816624345}[命令用来配置向终端一次性发送的最大数据包的大小。]{style="font-family:宋体"}

[**[undo sendbuf bufsize]{lang="EN-US"}**]{#struct_0_25005_14002_x449262747}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1205675890}

[**[sendbuf bufsize]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_25005_14002_x144807242}

[**[undo sendbuf bufsize]{lang="EN-US"}**]{#struct_0_25005_14002_x1926313273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2066781194}

[[向终端一次性发送的最大数据包的大小为]{style="font-family:宋体"}[500]{lang="EN-US"}]{#struct_0_25005_14002_x440237861}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_604227999}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1256833141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_1763699771}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x551410873}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1053035889}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x826234226}

[*[size]{lang="EN-US"}*]{#struct_0_25005_14002_x1470091704}[：向终端一次性发送的最大包的大小，取值范围]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[500]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_56155474}

[[终端接入设备把数据打成包发给终端，根据实际情况，每次发送的包的大小可能不同。]{style="font-family:宋体"}]{#struct_0_25005_14002_861497732}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1268094065}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x2122111426}[配置一次性发送的最大数据包的大小为]{style="font-family:宋体"}[200]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1706089495}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] sendbuf bufsize 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x808174251}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sendbuf threshold]{lang="EN-US"}**]{#struct_0_25005_14002_x1004747960}
:::

::: {#1372278077 .myid}
[]{#_Toc404786072}[]{#struct_0_25005_14002_x287261050}[]{#_Toc353818128}

**RTC终端接入 \-- RTC终端接入命令 \-- sendbuf threshold**

------------------------------------------------------------------------

[**[sendbuf threshold]{lang="EN-US"}**]{#struct_0_25005_14002_1882962142}[命令用来配置终端发送缓存的阈值。]{style="font-family:宋体"}

[**[undo sendbuf threshold]{lang="EN-US"}**]{#struct_0_25005_14002_x357855975}[命令用来取消配置的发送缓存阈值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1190188409}

[**[sendbuf threshold ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_25005_14002_1965339574}

[**[undo sendbuf threshold]{lang="EN-US"}**]{#struct_0_25005_14002_1018110897}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x607779585}

[[没有设置终端发送缓存的阈值。]{style="font-family:宋体"}]{#struct_0_25005_14002_606210815}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_854626577}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1198194736}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_32972054}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x969628035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_726564011}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1728919839}

[*[value]{lang="EN-US"}*]{#struct_0_25005_14002_249252908}[：终端发送缓存的阈值，取值范围为]{style="font-family:宋体"}[50]{lang="EN-US"}[～]{style="font-family:宋体"}[2048]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_202453716}

[[该发送缓存用于存放路由器准备向终端发送的数据，该阈值是指该发送缓存的最多可存储的数据的字节数。]{style="font-family:宋体"}]{#struct_0_25005_14002_x687754519}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x375895532}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1120378667}[配置终端发送缓存阈值为]{style="font-family:宋体"}[1000]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1802478790}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] sendbuf threshold 1000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1769158587}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sendbuf bufsize]{lang="EN-US"}**]{#struct_0_25005_14002_682042331}
:::

::: {#227750054 .myid}
[]{#_Toc404786073}[]{#struct_0_25005_14002_1219523497}[]{#_Toc353818129}

**RTC终端接入 \-- RTC终端接入命令 \-- tcp**

------------------------------------------------------------------------

[**[tcp]{lang="EN-US"}**]{#struct_0_25005_14002_x1850759494}[命令用来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的相关参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **tcp**]{lang="EN-US"}]{#struct_0_25005_14002_x146484959}[命令用来恢复]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2049556763}

[**[tcp]{lang="EN-US"}**[ { **keepalive** *time count* \| **nodelay** \| **recvbuf-size** *recvsize* \| **sendbuf-size** *sendsize* }]{lang="EN-US"}]{#struct_0_25005_14002_x684033793}

[**[undo tcp]{lang="EN-US"}**[ { **keepalive** \| **nodelay** \| **recvbuf-size** \| **sendbuf-size** }]{lang="EN-US"}]{#struct_0_25005_14002_2110705507}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_1719621206}

[[接收缓存大小为]{style="font-family:宋体"}[2048]{lang="EN-US"}]{#struct_0_25005_14002_1546353233}[字节，发送缓存大小为]{style="font-family:宋体"}[2048]{lang="EN-US"}[字节，有延迟，保活报文发送时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒，保活报文重发次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1148768090}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_433449030}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1702035300}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_630063462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_270981033}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x959638019}

[**[keepalive ]{lang="DE"}***[time count]{lang="EN-US"}*]{#struct_0_25005_14002_x1266968670}[：设置]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[保活报文发送参数，]{style="font-family:宋体"}*[time]{lang="EN-US"}*[表示保活报文发送时间间隔，取值范围]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[7200]{lang="EN-US"}[，单位为秒；]{style="font-family:宋体"}*[count]{lang="EN-US"}*[表示保活报文重发次数，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nodelay]{lang="DE"}**]{#struct_0_25005_14002_x603319758}[：不采用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的]{style="font-family:宋体"}[Nagle]{lang="EN-US"}[算法，即不延迟。]{style="font-family:宋体"}

[**[recvbuf-size]{lang="DE"}***[ ]{lang="DE"}[recvsize]{lang="EN-US"}*]{#struct_0_25005_14002_1205406350}[：]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[接收缓冲区大小，取值范围]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[sendbuf-size]{lang="DE"}***[ ]{lang="DE"}[sendsize]{lang="EN-US"}*]{#struct_0_25005_14002_x162132841}[：]{style="font-family:
宋体"}[TCP]{lang="EN-US"}[发送缓冲区大小，取值范围]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1703081485}

[[TCP]{lang="EN-US"}]{#struct_0_25005_14002_x1082116790}[的相关参数需要重新建立连接才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x19730708}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1173906841}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接收缓冲区大小为]{style="font-family:宋体"}[512]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1322886869}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] tcp recvbuf-size 512]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_673597864}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[发送缓冲区大小为]{style="font-family:宋体"}[512]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1652253416}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] tcp sendbuf-size 512]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_546616723}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[不延迟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1431270117}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] tcp nodelay]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1361439396}[配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[保活报文的时间间隔为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒，发送次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1346682388}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] tcp keepalive 1800 2]{lang="EN-US"}
:::

::: {#-793710155 .myid}
[]{#_Toc404786074}[]{#struct_0_25005_14002_x1063430925}[]{#_Toc353818130}

**RTC终端接入 \-- RTC终端接入命令 \-- update changed-config**

------------------------------------------------------------------------

[**[update changed-config]{lang="EN-US"}**]{#struct_0_25005_14002_1016064660}[命令用来使模板下新修改的配置生效。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1585814649}

[**[update changed-config]{lang="EN-US"}**]{#struct_0_25005_14002_1968163279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x494685823}

[[模板下新修改的配置不会立即生效。]{style="font-family:宋体"}]{#struct_0_25005_14002_1606386742}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_159714630}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1442823741}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_624309957}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_1291796419}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_38420867}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1533835317}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果模板已经被应用到相应接口，则在模板视图下修改配置后使用]{lang="EN-US" style="font-family:宋体"}**[update changed-config]{lang="EN-US"}**]{#struct_0_25005_14002_1844694284}[命令进行更新即可使配置生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[更新配置会断开当前连接，然后进行重新连接，因此使用本命令前，请确认当前连接是否允许出现短暂中断。]{style="font-family:宋体"}]{#struct_0_25005_14002_1531343152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于某些配置，如配置源]{style="font-family:宋体"}]{#struct_0_25005_14002_1163692507}[IP]{lang="EN-US"}[，不仅要更新配置，而且要重新建立连接，才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x984924992}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1143068706}[在模板下增加自动断链的设置并且使新配置立即生效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x1872107346}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] auto-close 10 ]{lang="EN-US"}

[\[Sysname-rta-template-abc\] update changed-config]{lang="EN-US"}
:::

::: {#-1720416042 .myid}
[]{#_Toc404786075}[]{#struct_0_25005_14002_x996747889}[]{#_Toc353818152}

**RTC终端接入 \-- RTC终端接入命令 \-- vty description**

------------------------------------------------------------------------

[**[vty description]{lang="EN-US"}**]{#struct_0_25005_14002_1299290859}[命令用来配置虚终端的描述信息。]{style="font-family:宋体"}

[**[undo vty description]{lang="EN-US"}**]{#struct_0_25005_14002_x1723901710}[命令用来取消虚终端的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1903874806}

[**[vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **description** *string*]{lang="EN-US"}]{#struct_0_25005_14002_1587672398}

[**[undo vty]{lang="EN-US"}**[ *vty-number* **description**]{lang="EN-US"}]{#struct_0_25005_14002_x776827390}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x741914094}

[[没有配置虚终端的描述信息。]{style="font-family:宋体"}]{#struct_0_25005_14002_999178061}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x274434475}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x898247440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x423015235}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x42229084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1901854898}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1315435861}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x217816464}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_25005_14002_x1695499179}[：虚终端的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1774726419}

[[当某个虚终端用于某种业务时，推荐直接用业务名描述这个虚终端，便于操作。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1483391374}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x488085184}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_1904052997}[设置虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[chuxu]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x82429269}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] vty 1 description chuxu]{lang="EN-US"}
:::

::: {#-453710216 .myid}
[]{#_Toc404786076}[]{#struct_0_25005_14002_1770973667}[]{#_Toc353818153}[]{#_Toc351017650}

**RTC终端接入 \-- RTC终端接入命令 \-- vty hotkey**

------------------------------------------------------------------------

[**[vty hotkey]{lang="EN-US"}**]{#struct_0_25005_14002_837986432}[命令用来设置虚终端快速切换的热键。]{style="font-family:宋体"}

[**[undo vty hotkey]{lang="EN-US"}**]{#struct_0_25005_14002_x1989099176}[命令用来取消配置的热键。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1715064435}

[**[vty]{lang="EN-US"}**[ *vty-number* **hotkey** *ascii-code&\<1-3\>*]{lang="EN-US"}]{#struct_0_25005_14002_215930771}

[**[undo vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **hotkey**]{lang="EN-US"}]{#struct_0_25005_14002_1818027951}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_657947075}

[[没有配置虚终端快速切换的热键。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1111615848}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x479827392}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_610486801}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_129084486}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x340514281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_117980875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1193177302}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_745991253}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ascii-code&\<1-3\>]{lang="EN-US"}*]{#struct_0_25005_14002_739784179}[：热键的]{style="font-family:
宋体"}[ASCII]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，]{style="font-family:宋体"}[&\<1-3\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1661482101}

[[终端接入具有虚终端切换的功能，可以在各应用之间进行切换。终端接入把每个终端从逻辑上划分为]{style="font-family:宋体"}[8]{lang="EN-US"}]{#struct_0_25005_14002_194737041}[个虚终端，每个虚终端与一个应用相对应。当在某个终端上配置了多个虚终端和相应快速切换热键后，可以在终端上敲入对应不同虚终端的热键进入相应的应用界面，而不用通过菜单选择就可以完成虚终端之间的快速切换。切换前原来虚终端应用的连接状态将被保留，并不断开，从而实现了终端在不同的虚终端间动态切换，也就是在不同的应用间动态切换。]{style="font-family:宋体"}

[[需要注意的是，热键的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}]{#struct_0_25005_14002_x5094406}[值不能与设备上已设置的别的功能热键的]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[值相同，否则，热键的功能将冲突。比如，热键的值不能设置为]{style="font-family:宋体"}[17]{lang="EN-US"}[和]{style="font-family:宋体"}[19]{lang="EN-US"}[，因为这两个值对应了流量控制的快捷键。另外，在终端显示大量数据时使用热键，会影响热键的响应速度。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_840438437}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x328855487}[配置虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[的热键为]{style="font-family:宋体"}[\<Ctrl+A\>]{lang="EN-US"}[，即]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x137911277}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] vty 1 hotkey 1]{lang="EN-US"}
:::

::: {#694137719 .myid}
[]{#_Toc404786077}[]{#struct_0_25005_14002_x1263505832}[]{#_Toc353818154}

**RTC终端接入 \-- RTC终端接入命令 \-- vty password**

------------------------------------------------------------------------

[**[vty password]{lang="EN-US"}**]{#struct_0_25005_14002_x1455027519}[命令用来配置虚终端的认证密码。]{style="font-family:宋体"}

[**[undo vty password]{lang="EN-US"}**]{#struct_0_25005_14002_x819007411}[命令用来取消配置的密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1108559443}

[**[vty]{lang="EN-US"}**[ *vty-number* **password** { **simple** \| **cipher** } *string*]{lang="EN-US"}]{#struct_0_25005_14002_x1343275850}

[**[undo vty]{lang="EN-US"}**[ ]{lang="EN-US"}*[vty-number]{lang="EN-US"}***[ ]{lang="EN-US"}[password]{lang="EN-US"}**]{#struct_0_25005_14002_2074920026}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_443164475}

[[没有配置虚终端的认证密码。]{style="font-family:宋体"}]{#struct_0_25005_14002_x826299762}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1524360669}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1871466959}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x562092203}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x96269931}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x22023864}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1757960822}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1208858398}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_25005_14002_x718773899}[：以明文方式设置认证密码。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_25005_14002_x858229515}[：以密文方式设置认证密码。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_25005_14002_1287922211}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_1912507670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文的方式设置的认证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_25005_14002_x636454632}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果需要支持认证功能，则服务端和客户端都必须配置密码，密码相同时认证才能通过；如果不需要支持认证功能，则服务端和客户端都不能配置密码。]{style="font-family:宋体"}]{#struct_0_25005_14002_x320794583}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1190122873}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_415330139}[配置虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[的密码为明文]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x122184869}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] vty 1 password simple abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x346476957}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-client remote]{lang="EN-US"}**]{#struct_0_25005_14002_954881455}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-server remote]{lang="EN-US"}**]{#struct_0_25005_14002_x960851970}
:::

::: {#-79296412 .myid}
[]{#_Toc404786078}[]{#struct_0_25005_14002_x1868065184}[]{#_Toc353818155}

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-client remote**

------------------------------------------------------------------------

[**[vty rtc-client remote]{lang="EN-US"}**]{#struct_0_25005_14002_1406460251}[命令用来创建]{style="font-family:宋体"}[TCP RTC Client]{lang="EN-US"}[终端接入类型的虚终端。]{style="font-family:宋体"}

[**[undo vty]{lang="EN-US"}**]{#struct_0_25005_14002_359015265}[用来删除指定的虚终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_511010512}

[**[vty]{lang="EN-US"}**[ *vty-number* **rtc-client remote** *ip-address port-number* \[ **source** *source-ip* \]]{lang="EN-US"}]{#struct_0_25005_14002_x1814015535}

[**[undo vty]{lang="EN-US"}**[ *vty-number*]{lang="EN-US"}]{#struct_0_25005_14002_467837096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x375961068}

[[没有创建虚终端。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1846505917}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1798848589}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1963210930}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1165005986}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x988979183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x183167718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_486318649}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_133364241}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_x1186529778}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[服务器端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1879294893}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[服务器端的监听端口号，取值范围]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[source ]{lang="EN-US"}***[source-ip]{lang="EN-US"}*]{#struct_0_25005_14002_641521109}[：绑定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x937266484}

[[配置该功能后，该]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_25005_14002_417659059}[所在的模板不能再配置其他类型的]{style="font-family:宋体"}[VTY]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1680570961}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1894091060}[创建]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[终端接入类型的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[，它的]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[侦听的端口为]{style="font-family:宋体"}[9010]{lang="EN-US"}[，建立]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接时是使用]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[作为源地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x339231074}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] vty 1 rtc-client remote 1.1.1.1 9010 source 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x430740145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rta rtc-server listen-port]{lang="EN-US"}**]{#struct_0_25005_14002_x1756765518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-server remote]{lang="EN-US"}**]{#struct_0_25005_14002_x78719222}
:::

::: {#832901846 .myid}
[]{#_Toc404786079}[]{#struct_0_25005_14002_1424972594}[]{#_Toc353818156}

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-client remote remote-port**

------------------------------------------------------------------------

[**[vty rtc-client remote remote-port]{lang="FR"}**]{#struct_0_25005_14002_x603972616}[命令用来创建]{style="font-family:宋体"}[UDP RTC Client]{lang="FR"}[终端接入类型的虚终端。]{style="font-family:宋体"}

[**[undo vty]{lang="FR"}**]{#struct_0_25005_14002_x691533681}[命令用来删除指定的虚终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x603142084}

[**[vty]{lang="EN-US"}**]{#struct_0_25005_14002_x1075771488}**[ ]{lang="EN-US"}***[vty-number]{lang="EN-US"}***[ ]{lang="EN-US"}[rtc-client remote]{lang="EN-US"}[ ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*[ ]{lang="EN-US"}**[remote-port]{lang="EN-US"}[ ]{lang="EN-US"}***[remote-port-number ]{lang="EN-US"}***[udp ]{lang="EN-US"}**[\[ **local-port**]{lang="EN-US"}**[ ]{lang="EN-US"}***[local-port-number ]{lang="EN-US"}*[\] \[ ]{lang="FR"}**[source]{lang="EN-US"}[ ]{lang="EN-US"}***[source-ip-address]{lang="EN-US"}*[ ]{lang="EN-US"}[\]]{lang="FR"}

[**[undo vty]{lang="EN-US"}**[ *vty-number*]{lang="EN-US"}]{#struct_0_25005_14002_1089645804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2115781065}

[[没有创建该类型的虚终端。]{style="font-family:宋体"}]{#struct_0_25005_14002_x728528618}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_114487020}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_x1176288562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x87199056}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1889729826}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_1515321064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1141469010}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_840021665}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_x816109848}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[remote-port-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1844182445}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[服务器]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_x886139296}[：本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[local-port-number]{lang="EN-US"}*]{#struct_0_25005_14002_1769739299}[：本端]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1395186892}

[[配置该功能后，该]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_25005_14002_x1647863557}[所在的模板不能再配置其他类型的]{style="font-family:宋体"}[VTY]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1451596921}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x1902274904}[创建]{style="font-family:宋体"}[UDP RTC Client]{lang="EN-US"}[终端接入类型的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[，它的对端（]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[）地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口为]{style="font-family:宋体"}[1024]{lang="EN-US"}[，本端地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口为]{style="font-family:宋体"}[1025]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1883059194}

[\[Sysname\] rta template temp2]{lang="EN-US"}

[\[Sysname-rta-template-temp2\] vty 1 rtc-client remote 1.1.1.1 remote-port 1024 udp local-port 1025 source 1.1.1.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x706984148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-server remote udp]{lang="EN-US"}**]{#struct_0_25005_14002_5948462}
:::

::: {#339466950 .myid}
[]{#_Toc404786080}[]{#struct_0_25005_14002_x28947869}[]{#_Toc353818157}

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-multipeer**

------------------------------------------------------------------------

[**[vty rtc-multipeer]{lang="EN-US"}**]{#struct_0_25005_14002_x987389927}[命令用来创建接收一对多连接的]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}[终端接入类型的虚终端。]{style="font-family:宋体"}

[**[undo vty]{lang="EN-US"}**]{#struct_0_25005_14002_1167660110}[命令用来删除指定的虚终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1937134473}

[**[vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **rtc-multipeer** \[ *ip-address* \] *port-number*]{lang="EN-US"}]{#struct_0_25005_14002_x734903661}

[**[undo vty]{lang="EN-US"}***[ vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x809937008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_1734692760}

[[没有创建该类型的虚终端。]{style="font-family:宋体"}]{#struct_0_25005_14002_1277286434}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x232132376}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_192203585}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1395075566}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_858119011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x63729382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_1580291721}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_1117449292}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_x627690267}[：本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_25005_14002_x68550245}[：本端]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1796121705}

[[删除接收一对多连接的]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}]{#struct_0_25005_14002_1167885752}[终端接入类型的虚终端后，会删除该虚终端下的客户端列表配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1536530894}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x747367298}[创建接收一对多连接的]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}[终端接入类型的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[，它的本端监听端口为]{style="font-family:宋体"}[1024]{lang="EN-US"}[，本端地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_x288797507}

[\[Sysname\] rta template temp3]{lang="EN-US"}

[\[Sysname-rta-template-temp3\] vty 1 rtc-multipeer 1.1.1.1 1024]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_124035806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-client remote remote-port]{lang="EN-US"}**]{#struct_0_25005_14002_x906237745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rtc-multipeer remote]{lang="EN-US"}**]{#struct_0_25005_14002_x662483315}
:::

::: {#-927190782 .myid}
[]{#_Toc404786081}[]{#struct_0_25005_14002_740917013}[]{#_Toc353818158}

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-server remote**

------------------------------------------------------------------------

[**[vty rtc-server remote]{lang="EN-US"}**]{#struct_0_25005_14002_x980809144}[命令用来创建]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[终端接入类型的虚终端。]{style="font-family:宋体"}

[**[undo vty]{lang="EN-US"}**]{#struct_0_25005_14002_x1583934163}[用来删除指定的虚终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_1437693240}

[**[vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **rtc-server remote** *ip-address terminal-number*]{lang="EN-US"}]{#struct_0_25005_14002_x189691536}

[**[undo vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x708265532}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1762904123}

[[没有配置该类型的虚终端。]{style="font-family:宋体"}]{#struct_0_25005_14002_x1136149533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_x2045488444}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_2081950692}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1854881448}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1378879782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x593407847}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_773495491}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1156503024}[：虚终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_550652319}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[terminal-number]{lang="EN-US"}*]{#struct_0_25005_14002_x626418010}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[客户端对应的终端号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x98458064}

[[配置该功能后，该]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_25005_14002_x1062189873}[所在的模板不能再配置其他类型的]{style="font-family:宋体"}[VTY]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_161340865}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_2117511541}[添加]{style="font-family:宋体"}[RTC Server]{lang="EN-US"}[终端接入类型的虚终端，]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，终端号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_592413744}

[\[Sysname\] rta template abc]{lang="EN-US"}

[\[Sysname-rta-template-abc\] vty 1 rtc-server remote 2.2.2.2 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1965445602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-client remote]{lang="EN-US"}**]{#struct_0_25005_14002_2003647914}
:::

::: {#72938646 .myid}
[]{#_Toc404786082}[]{#struct_0_25005_14002_874001907}[]{#_Toc353818159}

**RTC终端接入 \-- RTC终端接入命令 \-- vty rtc-server remote udp**

------------------------------------------------------------------------

[**[vty rtc-server remote udp]{lang="EN-US"}**]{#struct_0_25005_14002_1331721942}[命令用来创建]{style="font-family:
宋体"}[UDP RTC Server]{lang="EN-US"}[终端接入类型的虚终端。]{style="font-family:
宋体"}

[**[undo vty]{lang="EN-US"}**]{#struct_0_25005_14002_x1398693853}[命令用来删除指定的虚终端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_205109052}

[**[vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*[ **rtc-server remote** \[ *ip-address* **remote-port** *remote-port-number* \] **udp local-port** *local-port-number* \[ **source** *source-ip-address* \]]{lang="EN-US"}]{#struct_0_25005_14002_x2143741806}

[**[undo vty ]{lang="EN-US"}***[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_718647287}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_25005_14002_x99454005}

[[没有创建该类型的虚终端。]{style="font-family:宋体"}]{#struct_0_25005_14002_x166517237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_25005_14002_1499746657}

[[终端模板视图]{style="font-family:宋体"}]{#struct_0_25005_14002_1706901895}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_25005_14002_819238756}

[[network-admin]{lang="EN-US"}]{#struct_0_25005_14002_x936777932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_25005_14002_x1517517592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_25005_14002_x692082034}

[*[vty-number]{lang="EN-US"}*]{#struct_0_25005_14002_1965636621}[：虚拟终端号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_559550250}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[remote-port-number]{lang="EN-US"}*]{#struct_0_25005_14002_1397120727}[：]{style="font-family:宋体"}[RTC]{lang="EN-US"}[客户端]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-ip-address]{lang="EN-US"}*]{#struct_0_25005_14002_1057249420}[：本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[local-port-number]{lang="EN-US"}*]{#struct_0_25005_14002_x1364765298}[：本端]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口，取值范围为]{style="font-family:宋体"}[1024]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_25005_14002_x1893482653}

[[配置该功能后，该]{style="font-family:宋体"}[VTY]{lang="EN-US"}]{#struct_0_25005_14002_675041699}[所在的模板不能再配置其他类型的]{style="font-family:宋体"}[VTY]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_25005_14002_1166428924}

[[\# ]{lang="EN-US"}]{#struct_0_25005_14002_x341725582}[创建]{style="font-family:宋体"}[UDP RTC Server]{lang="EN-US"}[终端接入类型的虚终端]{style="font-family:宋体"}[1]{lang="EN-US"}[，它的本端地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[、]{style="font-family:宋体"}[UDP]{lang="EN-US"}[监听端口为]{style="font-family:宋体"}[1024]{lang="EN-US"}[，对端（]{style="font-family:宋体"}[RTC Client]{lang="EN-US"}[）地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[1025]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_25005_14002_1324340601}

[\[Sysname\] rta template temp1]{lang="EN-US"}

[\[Sysname-rta-template-temp1\] vty 1 rtc-server remote 1.1.1.2 remote-port 1025 udp local-port 1024 source 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_25005_14002_x253676541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vty rtc-client remote remote-port]{lang="EN-US"}**]{#struct_0_25005_14002_329201453}
:::
