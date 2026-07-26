::::: {#549640137 .myid}
[]{#_Toc252801287}[]{#_Toc140491850}[]{#_Toc140491148}[]{#_Toc404796198}[]{#struct_0_x1819_x1365_x565938901}[]{#_Toc304794688}

**BFD \-- BFD配置命令 \-- bfd authentication-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BFD命令.files/image001.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1819_x1365_x499483440}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_x1365_532727896}
:::

[ ]{lang="EN-US"}

[**[bfd authentication-mode]{lang="EN-US"}**]{#struct_0_x1819_x1365_x47003664}[命令用来配置单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文进行认证的方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd authentication-mode**]{lang="EN-US"}]{#struct_0_x1819_x1365_1962130745}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1713819149}

[**[bfd ]{lang="EN-US"}[authentication-mode]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ **m-md5** \| **m-sha1** \| **md5** \| **sha1** \| **simple** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]{lang="EN-US"}]{#struct_0_x1819_x1365_750072925}

[**[undo]{lang="EN-US"}[ bfd authentication-mode]{lang="EN-US"}**]{#struct_0_x1819_x1365_1663247116}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1176140725}

[[单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1997301303}[控制报文不进行认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1127501471}

[[接口视图]{style="font-family:宋体"}[/BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1768285208}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1809427825}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1037598407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1713753613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1944823537}

[**[m-md5]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1904148428}[：采用]{style="font-family:宋体"}[Meticulous MD5]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[m-sha1]{lang="EN-US"}**]{#struct_0_x1819_x1365_1796364094}[：采用]{style="font-family:宋体"}[Meticulous SHA1]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x1819_x1365_1489185586}[：采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行]{style="font-family:宋体"}[认证。]{style="font-family:宋体"}

[**[sha1]{lang="EN-US"}**]{#struct_0_x1819_x1365_1540931154}[：采用]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1819_x1365_89837108}**[：]{style="font-family:宋体"}**[采用简单认证。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x1819_x1365_1137535099}[：认证字标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1819_x1365_1091620218}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x1819_x1365_179263594}[：表示设置的密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x1819_x1365_x956058057}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x1819_x1365_1634375288}[：表示设置的明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x547893714}

[[本命令主要为了提高]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_1713950221}[会话的安全性。]{style="font-family:宋体"}

[[以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_776995839}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x103464394}[版本]{style="font-family:宋体"}[0]{lang="EN-US"}[不支持本命令，配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2123470413}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_768026596}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1135762250}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[对单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文进行简单明文认证，认证字标识符为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_23770883}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd authentication-mode simple 1 plain 123456]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_x1991999471}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_495665697}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[对单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文进行简单明文认证，认证字标识符为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1713884685}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd authentication-mode simple 1 plain 123456]{lang="EN-US"}
:::::

::: {#-2125051496 .myid}
[]{#_Toc404796199}[]{#struct_0_x1819_x1365_x397617520}[]{#_Toc304794689}

**BFD \-- BFD配置命令 \-- bfd demand enable**

------------------------------------------------------------------------

[**[bfd demand enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_x128214272}[命令用来配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话为查询模式。]{style="font-family:宋体"}

[**[undo bfd demand enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_1944661571}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1244117032}

[**[bfd demand ]{lang="EN-US"}[enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1478951761}

[**[undo]{lang="EN-US"}**[ **bfd demand enable**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1902720177}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x92888926}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x712434867}[会话为异步模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1714081293}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1857327234}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x32049926}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1499863761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1395721766}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x918704396}

[[在查询模式下，设备周期性发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1862294219}[控制报文，但是对端（缺省为异步模式）会停止周期性发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文。如果通信双方都是查询模式，则双方都停止周期性发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文。当需要验证连接性的时候，设备会以协商的周期连续发送几个]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位置]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文。如果在检测时间内没有收到返回的报文，就认为会话]{style="font-family:宋体"}[down]{lang="EN-US"}[；如果收到对方的回应]{style="font-family:宋体"}[F]{lang="EN-US"}[比特位置]{style="font-family:宋体"}[1]{lang="EN-US"}[的报文，就认为连通，停止发送报文，等待下一次触发查询。]{style="font-family:宋体"}

[[在异步模式下，设备周期性地发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_987521746}[控制报文，如果在检测时间内对端没有收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文，则认为会话]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x103464395}[版本]{style="font-family:宋体"}[0]{lang="EN-US"}[不支持本命令，配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1038902822}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_1714015757}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1327471878}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话为查询模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1588172362}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd demand enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_185780940}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x857516986}[在接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[上配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话为查询模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x2014824752}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd demand enable]{lang="EN-US"}
:::

::::: {#-1190273097 .myid}
[]{#_Toc350333359}[]{#_Toc404796200}[]{#struct_0_x1819_x1365_x1621130752}

**BFD \-- BFD配置命令 \-- bfd detect-interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BFD命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_x1365_x1057153112}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_x1365_x1621065216}
:::

[ ]{lang="EN-US"}

[**[bfd detect-interface source-ip]{lang="EN-US"}**]{#struct_0_x1819_x1365_708407252}[命令用来]{style="font-family:
宋体"}[创建一个检测本接口状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo bfd]{lang="EN-US"}**[ **detect-interface**]{lang="EN-US"}]{#struct_0_x1819_x1365_175928500}[命令用来]{style="font-family:宋体"}[删除创建的检测本接口状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_995941963}

[**[bfd detect-interface source-ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_x1819_x1365_x89034125}

[**[undo bfd]{lang="EN-US"}**[ **detect-interface**]{lang="EN-US"}]{#struct_0_x1819_x1365_691450158}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1957327416}

[[没有创建检测本接口状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x615910152}[会话]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x690957572}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1396073695}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1621655041}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1531050516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1959269659}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x93760109}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1819_x1365_x376541631}[：]{style="font-family:宋体;color:black"}[BFD]{lang="SV" style="color:black"}[控制报文的源]{style="font-family:宋体;color:black"}[IP]{lang="SV" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1210806844}

[[三层聚合接口的成员端口上没有]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1819_x1365_1214765553}[地址，没有可以支持的快速检测机制。通过本功能可以快速检测成员链路的故障，帮助快速找出故障成员接口；本功能同时支持普通三层以太网接口故障快速检测，实现接口状态与]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话状态的快速联动，帮助上层路由协议实现快速收敛。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x448109926}[会话采用控制报文方式，两端都必须配置；报文目的地址固定为]{style="font-family:宋体"}[224.0.0.184]{lang="EN-US"}[，不支持配置。]{style="font-family:宋体"}

[[源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1819_x1365_x1631376836}[地址建议配置为接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，如果接口没有]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，建议配置一个单播地址（]{style="font-family:宋体"}[0.0.0.0]{lang="EN-US"}[除外）。]{style="font-family:宋体"}

[[在同一接口下，同时配置]{style="font-family:宋体"}**[bfd detect-interface]{lang="EN-US"}**]{#struct_0_x1819_x1365_x103464398}[和]{style="font-family:宋体"}**[bfd echo enable]{lang="EN-US"}**[命令，只有]{style="font-family:宋体"}**[bfd detect-interface]{lang="EN-US"}**[命令生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1621589505}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x666310616}[配置检测]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口状态的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话，其源地址为接口地址]{style="font-family:宋体"}[20.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_127279361}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd detect-interface source-ip 20.1.1.1]{lang="EN-US"}
:::::

::: {#350550895 .myid}
[]{#_Toc404796201}[]{#struct_0_x1819_x1365_x573528724}

**BFD \-- BFD配置命令 \-- bfd detect-multiplier**

------------------------------------------------------------------------

[**[bfd detect-multiplier]{lang="EN-US"}**]{#struct_0_x1819_x1365_1714212365}[命令用来配置[单跳]{#OLE_LINK2}]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测时间倍数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd detect-multiplier**]{lang="EN-US"}]{#struct_0_x1819_x1365_1443437618}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x726795190}

[**[bfd detect-multiplier ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_2090443696}

[**[undo]{lang="EN-US"}**[ **bfd detect-multiplier**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1735004456}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_465889791}

[[单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1200497049}[检测时间倍数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1502633717}

[[接口视图]{style="font-family:宋体"}[/BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x272850301}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1714146829}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_281472573}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x188918185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_881696895}

[*[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_x1081949008}[：]{style="font-family:宋体"}[单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测时间倍数，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_766712100}

[[检测时间倍数，即允许发送方发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1798197567}[报文（包括]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文和控制报文）的最大连续丢包数。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_x425646249}[报文方式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积；对于控制报文方式的异步模式，实际检测时间为接收方的检测时间倍数和接收方的实际发送时间的乘积；对于控制报文方式的查询模式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x566093720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_1714343437}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x942300656}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测时间倍数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1393273076}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd detect-multiplier 6]{lang="EN-US"}

[]{#struct_0_x1819_x1365_118684447}[]{#_Toc67196012}[]{#_Toc67145837}[]{#_Toc60630698}[]{#_Toc60303556}[]{#_Toc59250700}[]{#_Toc49376399}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_1385842907}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测时间倍数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x2046390988}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd detect-multiplier 6]{lang="EN-US"}
:::

::: {#-175072770 .myid}
[]{#_Toc252801290}[]{#_Toc140491849}[]{#_Toc140491147}[]{#_Toc300235905}[]{#_Toc300235909}[]{#_Toc404796202}[]{#struct_0_x1819_x1365_1404594327}[]{#_Toc304794691}

**BFD \-- BFD配置命令 \-- bfd echo enable**

------------------------------------------------------------------------

[**[bfd echo enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_x327289423}[命令用来使能]{style="font-family:宋体"}[echo]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd echo enable**]{lang="EN-US"}]{#struct_0_x1819_x1365_1714277901}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x117999103}

[**[bfd echo enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_1696138047}

[**[undo bfd echo enable]{lang="EN-US"}**]{#struct_0_x1819_x1365_x960580679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2058035496}

[[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_64868738}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1857031619}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x51164727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x130988164}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1015064203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_377966743}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1437692880}

[[本功能在发送控制报文的]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_155909655}[会话时使用。使能]{style="font-family:宋体"}[echo]{lang="EN-US"}[功能并且会话]{style="font-family:宋体"}[up]{lang="EN-US"}[后，设备周期性发送]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文检测链路连通性，同时降低控制报文的接收速率。]{style="font-family:宋体"}

[[在同一接口下，同时配置]{style="font-family:宋体"}**[bfd detect-interface]{lang="EN-US"}**]{#struct_0_x1819_x1365_x103464401}[和]{style="font-family:宋体"}**[bfd echo enable]{lang="EN-US"}**[命令，只有]{style="font-family:宋体"}**[bfd detect-interface]{lang="EN-US"}**[命令生效。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x912407602}[版本]{style="font-family:宋体"}[0]{lang="EN-US"}[不支持本命令，配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x435328653}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_x1285716209}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x526472282}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[echo]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1031924373}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd echo enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_x1015129739}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1170161986}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[使能]{style="font-family:宋体"}[echo]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1985026444}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd echo enable]{lang="EN-US"}
:::

::: {#-1105503451 .myid}
[]{#_Toc404796203}[]{#struct_0_x1819_x1365_127419225}

**BFD \-- BFD配置命令 \-- bfd echo-source-ip**

------------------------------------------------------------------------

[**[bfd echo-source-ip]{lang="EN-US"}**]{#struct_0_x1819_x1365_1066540579}[命令用来配置]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd echo-source-ip**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1788914908}[命令用来删除]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x331330104}

[**[bfd echo-source-ip]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x1819_x1365_x1441930702}

[**[undo]{lang="EN-US"}**[ **bfd** **echo-source-ip**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014933131}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_988885490}

[[没有配置]{style="font-family:宋体"}[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_1505978478}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1405863839}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_529116744}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1615772705}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x693822579}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1204305265}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_224750354}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1819_x1365_x1014998667}[：]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1589167653}

[[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_x1368468186}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址用户可以任意指定。为了避免对端发送大量的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[重定向报文造成网络]{style="font-family:宋体"}[拥塞，建议配置]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不属于该设备任何一个接口所在网段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_299523946}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1692126607}[配置]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[8.8.8.8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1220705330}

[\[Sysname\] bfd echo-source-ip 8.8.8.8]{lang="EN-US"}
:::

::: {#1570578097 .myid}
[]{#_Toc404796204}[]{#struct_0_x1819_x1365_1389090225}[]{#_Toc300235910}

**BFD \-- BFD配置命令 \-- bfd echo-source-ipv6**

------------------------------------------------------------------------

[**[bfd echo-source-ipv6]{lang="EN-US"}**]{#struct_0_x1819_x1365_x92833932}[命令用来配置]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd echo-source-ipv6**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014802059}[命令用来删除]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1359007440}

[**[bfd echo-source-ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1819_x1365_x660212520}

[**[undo]{lang="EN-US"}**[ **bfd** **echo-source-ipv6**]{lang="EN-US"}]{#struct_0_x1819_x1365_914098645}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1298421974}

[[没有配置]{style="font-family:宋体"}[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_165122102}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2116923573}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_568236419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x2067515133}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014867595}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x935434363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2100629549}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1819_x1365_x387239646}[：]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_163451911}

[[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_548553907}[报文源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址仅支持全球单播地址。]{style="font-family:宋体"}

[[为了避免对端发送大量的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_x1819_x1365_1115240089}[重定向报文造成网络拥塞，建议不要将]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址配置为属于该设备任何一个接口所在网段。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1860240735}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_287790091}[配置]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[80::2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014670987}

[\[Sysname\] bfd echo-source-ipv6 80::2]{lang="EN-US"}
:::

::: {#-673537694 .myid}
[]{#_Toc404796205}[]{#struct_0_x1819_x1365_x229700216}

**BFD \-- BFD配置命令 \-- bfd min-echo-receive-interval**

------------------------------------------------------------------------

[**[bfd min-echo-receive-interval]{lang="EN-US"}**]{#struct_0_x1819_x1365_1597636988}[命令用来配置接收]{style="font-family:
宋体"}[echo]{lang="EN-US"}[报文的最小时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd min-echo-receive-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_461849000}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1713434789}

[**[bfd min-echo-receive-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_1531369236}

[**[undo]{lang="EN-US"}**[ **bfd min-echo-receive-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1212529289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1112711976}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1109028816}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1014736523}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1728832724}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x2135609312}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_154189272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x432776807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2063792512}

[*[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_x771018655}[：]{style="font-family:宋体"}[接收]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x687186753}

[[使用本命令，设备能够控制接收两个]{style="font-family:宋体"}[echo]{lang="EN-US"}]{#struct_0_x1819_x1365_821505431}[报文之间的时间间隔，即]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文实际发送时间间隔。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1014539915}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_10706830}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x2057528861}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1507690498}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd min-echo-receive-interval 500]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_x965266226}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x215360446}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[接收]{style="font-family:宋体"}[echo]{lang="EN-US"}[报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1599679936}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd min-echo-receive-interval 500]{lang="EN-US"}
:::

::: {#1307779661 .myid}
[]{#_Toc404796206}[]{#struct_0_x1819_x1365_x1014605451}

**BFD \-- BFD配置命令 \-- bfd min-receive-interval**

------------------------------------------------------------------------

[**[bfd min-receive-interval]{lang="EN-US"}**]{#struct_0_x1819_x1365_1952983548}[命令用来配置接收单跳]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd min-receive-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1553611235}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1156751010}

[**[bfd min-receive-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_x1956466666}

[**[undo]{lang="EN-US"}**[ **bfd min-receive-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1931422995}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x635586683}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1328216389}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1008749284}

[[接口视图]{style="font-family:宋体"}[/BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1015064202}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1188117198}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1582863538}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1431488279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_349627823}

[*[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_x434918638}[：]{style="font-family:宋体"}[接收单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1462273999}

[[本命令主要为了防止对端发送控制报文的速度超过本地接收控制报文的速度。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1002262058}

[[对端的控制报文实际发送时间为对端发送控制报文的最小时间间隔和本地接收控制报文的最小时间间隔之间的较大值。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x35171649}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1015129738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_1558721369}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_331329550}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x542090702}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd min-receive-interval 500]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_597299305}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1082812524}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[接收单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x745276869}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd min-receive-interval 500]{lang="EN-US"}
:::

::: {#-1962483141 .myid}
[]{#_Toc404796207}[]{#struct_0_x1819_x1365_x1014933130}[]{#_Toc252801291}[]{#_Toc140491848}[]{#_Toc140491146}

**BFD \-- BFD配置命令 \-- bfd min-transmit-interval**

------------------------------------------------------------------------

[**[bfd min-transmit-interval]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1739997865}[命令用来配置发送单跳]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd min-transmit-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_1428820091}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_283783903}

[**[bfd min-transmit-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_187316178}

[**[undo]{lang="EN-US"}**[ **bfd min-transmit-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_1058717765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_862385273}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x990038105}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1292402793}

[[接口视图]{style="font-family:宋体"}[/BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014998666}[模板视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1139715702}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x504189047}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1738929587}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1991009090}

[*[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_531834195}[：发送单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1342931026}

[[本命令主要是为了保证发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_1211604895}[控制报文的速度不能超过设备发送报文的能力。本地实际发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的时间间隔，为本地配置的发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔和对端接收]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔的最大值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x2098735274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014802058}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x207076501}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1047668300}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] bfd min-transmit-interval 500]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1819_x1365_897101487}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_1778458879}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[发送单跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1834586025}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] bfd min-transmit-interval 500]{lang="EN-US"}
:::

::::: {#-651592812 .myid}
[]{#_Toc252801296}[]{#_Toc140491858}[]{#_Toc140491156}[]{#_Toc300235911}[]{#_Toc404796208}[]{#struct_0_x1819_x1365_361900864}[]{#_Toc304794697}[]{#_Toc166928488}[]{#_Toc156128455}[]{#_Toc156187248}[]{#_Toc156128456}[]{#_Toc156187249}[]{#_Toc156128457}[]{#_Toc156187250}[]{#_Toc156128458}[]{#_Toc156187251}[]{#_Toc156128459}[]{#_Toc156187252}[]{#_Toc156128460}[]{#_Toc156187253}[]{#_Toc156128461}[]{#_Toc156187254}[]{#_Toc156128462}[]{#_Toc156187255}[]{#_Toc156128463}[]{#_Toc156187256}[]{#_Toc156128464}[]{#_Toc156187257}[]{#_Toc156128465}[]{#_Toc156187258}[]{#_Toc156128466}[]{#_Toc156187259}[]{#_Toc156128474}[]{#_Toc156187267}[]{#_Toc209857708}[]{#_Toc209857709}[]{#_Toc209857710}[]{#_Toc209857711}[]{#_Toc209857712}[]{#_Toc209857713}[]{#_Toc209857714}[]{#_Toc209857715}[]{#_Toc209857716}[]{#_Toc209857717}[]{#_Toc209857718}[]{#_Toc209857719}[]{#_Toc209857720}[]{#_Toc209857721}[]{#_Toc209857726}[]{#_Toc209857727}[]{#_Toc209857740}

**BFD \-- BFD配置命令 \-- bfd multi-hop authentication-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BFD命令.files/image001.png){#图片 3 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014867594}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_x1365_1793448992}
:::

[ ]{lang="EN-US"}

[**[bfd ]{lang="EN-US"}**]{#struct_0_x1819_x1365_x506219687}**[multi-hop]{lang="PT-BR"}[ authentication-mode]{lang="EN-US"}**[命令用来配置多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文进行认证的方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ bfd ]{lang="EN-US"}**]{#struct_0_x1819_x1365_x306771414}**[multi-hop]{lang="PT-BR"}[ ]{lang="PT-BR"}[authentication-mode]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x897817055}

[**[bfd ]{lang="EN-US"}**]{#struct_0_x1819_x1365_x459367617}**[multi-hop]{lang="PT-BR"}[ authentication-mode ]{lang="EN-US"}**[{ **m-md5** \| **m-sha1** \| **md5** \| **sha1** \| **simple** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **bfd** ]{lang="EN-US"}]{#struct_0_x1819_x1365_x206192148}**[multi-hop]{lang="PT-BR"}[ authentication-mode]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1272186789}

[[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014670986}[控制报文不进行认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1336383725}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1465349669}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1924868612}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_727832495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1224938095}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x922143999}

[**[m-md5]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1904213962}[：采用]{style="font-family:宋体"}[Meticulous MD5]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[m-sha1]{lang="EN-US"}**]{#struct_0_x1819_x1365_957014104}[：采用]{style="font-family:宋体"}[Meticulous SHA1]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x1819_x1365_987881048}[：采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[算法进行]{style="font-family:宋体"}[认证。]{style="font-family:宋体"}

[**[sha1]{lang="EN-US"}**]{#struct_0_x1819_x1365_1049056143}[：采用]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[算法进行认证。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1819_x1365_124673695}**[：]{style="font-family:宋体"}**[采用简单认证。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x1819_x1365_1169721304}[：认证字标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1014736522}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x1819_x1365_x162748783}[：表示设置的密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x1819_x1365_256933015}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x1819_x1365_x2041887068}[：表示设置的明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1724434160}

[[本命令主要为了提高]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_1001718282}[会话的安全性。]{style="font-family:宋体"}

[[以明文或密文方式设置的密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_975226969}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x2059779538}[版本]{style="font-family:宋体"}[0]{lang="EN-US"}[不支持本命令，配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1347515168}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1816468132}[配置多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文进行简单明文认证，认证字标识符为]{style="font-family:宋体"}[1]{lang="EN-US"}[，密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014539914}

[\[Sysname\] bfd ]{lang="EN-US"}[multi-hop]{lang="PT-BR"}[ authentication-mode]{lang="EN-US"}[ simple 1 plain 123456]{lang="EN-US"}
:::::

::: {#-115043934 .myid}
[]{#_Toc404796209}[]{#struct_0_x1819_x1365_1576790771}

**BFD \-- BFD配置命令 \-- bfd multi-hop destination-port**

------------------------------------------------------------------------

[**[bfd multi-hop destination-port]{lang="EN-US"}**]{#struct_0_x1819_x1365_x611306338}[命令用来配置]{style="font-family:
宋体"}[多]{style="font-family:宋体"}[跳]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[控制报文的]{style="font-family:宋体"}[目的端口号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop destination-port**]{lang="EN-US"}]{#struct_0_x1819_x1365_321305486}[命令用来恢复]{style="font-family:宋体"}[缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1840787703}

[**[bfd multi-hop destination-port]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1819_x1365_1928220951}*[port-number]{lang="FR"}*

[**[undo]{lang="EN-US"}**[ **bfd multi-hop destination-port**]{lang="EN-US"}]{#struct_0_x1819_x1365_436745253}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x2094782334}

[[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014605450}[控制报文的目的端口号为]{style="font-family:宋体"}[4784]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_386899607}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x279509556}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_61139186}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_2139986274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1654332948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x50512895}

[*[port-number]{lang="FR"}*]{#struct_0_x1819_x1365_1063228849}[：多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的目的端口号，取值可以为]{style="font-family:宋体"}[3784]{lang="EN-US"}[或者]{style="font-family:宋体"}[4784]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2063839034}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1015064205}[配置多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的目的端口号为]{style="font-family:宋体"}[3784]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x1819_x1365_x784832671}

[\[Sysname\] bfd multi-hop destination-port 3784]{lang="FR"}
:::

::: {#1283453381 .myid}
[]{#_Toc404796210}[]{#struct_0_x1819_x1365_1115118646}[]{#_Toc304794699}

**BFD \-- BFD配置命令 \-- bfd multi-hop detect-multiplier**

------------------------------------------------------------------------

[**[bfd ]{lang="EN-US" style="color:windowtext"}**]{#struct_0_x1819_x1365_x929388062}**[multi-hop]{lang="PT-BR" style="color:windowtext"}[ detect-multiplier]{lang="EN-US" style="color:windowtext"}**[命令用来配置多跳]{style="font-family:宋体;color:windowtext"}[BFD]{lang="EN-US" style="color:windowtext"}[检测时间倍数。]{style="font-family:宋体;color:windowtext"}

[**[undo bfd ]{lang="EN-US" style="color:windowtext"}**]{#struct_0_x1819_x1365_2016716245}**[multi-hop]{lang="PT-BR" style="color:windowtext"}[ detect-multiplier]{lang="EN-US" style="color:windowtext"}**[命令用来恢复缺省情况。]{style="font-family:宋体;color:windowtext"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1190207041}

[**[bfd multi-hop detect-multiplier ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_1939413733}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop detect-multiplier**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1337685709}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_852150641}

[[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1015129741}[检测时间倍数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1526195738}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x318294798}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1007592542}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1051539981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x974105421}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1094213579}

[*[value]{lang="FR"}*]{#struct_0_x1819_x1365_x1237517537}[：]{style="font-family:宋体"}[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检]{style="font-family:宋体"}[测时间倍数，取值范围为]{style="font-family:宋体"}[3]{lang="FR"}[～]{style="font-family:宋体"}[50]{lang="FR"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x571339679}

[[检测时间倍数，即接收方允许发送方发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014933133}[控制报文的最大连续丢包数。]{style="font-family:宋体"}

[[对于控制报文方式的异步模式，实际检测时间为接收方的检测时间倍数和接收方的实际发送时间的乘积；对于控制报文方式的查询模式，实际检测时间为发送方的检测时间倍数和发送方的实际发送时间的乘积。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x2143282392}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1759838862}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x850489891}[配置多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测时间倍数为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x1819_x1365_1099506381}

[\[Sysname\] bfd ]{lang="FR"}[multi-hop]{lang="EN-US"}[ detect-multiplier 6]{lang="FR"}
:::

::: {#-974002177 .myid}
[]{#_Toc404796211}[]{#struct_0_x1819_x1365_409616712}[]{#_Toc304794700}

**BFD \-- BFD配置命令 \-- bfd multi-hop min-receive-interval**

------------------------------------------------------------------------

[**[bfd multi-hop ]{lang="EN-US"}**]{#struct_0_x1819_x1365_577550310}**[min-receive-interval]{lang="PT-BR"}**[命令用来配置接收]{style="font-family:宋体"}[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop**]{lang="EN-US"}]{#struct_0_x1819_x1365_980195586}**[ min-receive-interval]{lang="PT-BR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1014998669}

[**[bfd multi-hop min-receive-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_426368239}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop min-receive-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_x2062014274}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1291751719}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_183555331}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1234532076}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1211771600}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2108869509}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1005531092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014802061}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1002580472}

[[value]{lang="FR"}]{#struct_0_x1819_x1365_x1059773630}[：接收]{style="font-family:宋体"}[BFD]{lang="FR"}[控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_930566718}

[[本命令主要为了防止对端设备发送报文的速度超出本地接收报文的能力（接收]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_1975820057}[控制报文的最小时间间隔），若超出，则对端设备将发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的时间间隔动态调整为本地接收]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1521038338}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x2140612422}[配置接收多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x1819_x1365_382905921}

[\[Sysname\] bfd ]{lang="FR"}[multi-hop]{lang="EN-US"}[ min-receive-interval 500]{lang="FR"}
:::

::: {#-1714035235 .myid}
[]{#_Toc404796212}[]{#struct_0_x1819_x1365_x1014867597}[]{#_Toc304794701}

**BFD \-- BFD配置命令 \-- bfd multi-hop min-transmit-interval**

------------------------------------------------------------------------

[**[bfd multi-hop ]{lang="EN-US"}**]{#struct_0_x1819_x1365_x2098233777}**[min-transmit-interval]{lang="PT-BR"}**[命令用来配置发送]{style="font-family:宋体"}[多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1076606658}**[ ]{lang="EN-US"}[min-transmit-interval]{lang="PT-BR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_51361866}

[**[bfd multi-hop min-transmit-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_854399909}

[**[undo]{lang="EN-US"}**[ **bfd multi-hop min-transmit-interval**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1786021903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1966829300}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1819_x1365_499589767}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_222213848}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014670989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_220638478}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1611000122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1224211162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1414150855}

[*[value]{lang="FR"}*]{#struct_0_x1819_x1365_1938320645}[：发送]{style="font-family:宋体"}[BFD]{lang="FR"}[控制报文的最小时间间隔，单位为毫秒。不同设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1020400954}

[[本命令主要是为了保证发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x18205865}[控制报文的速度不能超过设备发送报文的能力。本地实际发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的时间间隔，为本地配置的发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔和对端接收]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔的最大值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1314234153}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014736525}[配置发送多跳]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文的最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x1819_x1365_x922263670}

[\[Sysname\] bfd ]{lang="FR"}[multi-hop]{lang="EN-US"}[ min-transmit-interval 500]{lang="FR"}
:::

::: {#1557985073 .myid}
[]{#_Toc404796213}[]{#struct_0_x1819_x1365_x1064280448}[]{#_Toc304794702}

**BFD \-- BFD配置命令 \-- bfd session init-mode**

------------------------------------------------------------------------

[**[bfd session init-mode]{lang="EN-US"}**]{#struct_0_x1819_x1365_1606856242}[命令用来配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话建立前的运行模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bfd session init-mode**]{lang="EN-US"}]{#struct_0_x1819_x1365_1381305371}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1243528859}

[**[bfd session init-mode ]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1370429432}[{ **active** ]{lang="FR"}[\| ]{lang="EN-US"}**[passive]{lang="FR"}***[ ]{lang="FR"}*[}]{lang="FR"}

[**[undo]{lang="EN-US"}**[ **bfd session init-mode**]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014539917}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1173506244}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x435097598}[会话建立前的运行模式为]{style="font-family:宋体"}[主动模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_320766933}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1255814430}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x192261730}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1701138203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x272927199}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1156494860}

[**[active]{lang="FR"}**]{#struct_0_x1819_x1365_x1014605453}[：主动模式。]{style="font-family:宋体"}[在建立会话前不管是否收到对端发来的]{style="font-family:宋体"}[BFD]{lang="FR"}[控制报文，都会]{style="font-family:宋体"}[主动向会话的对端发送]{style="font-family:宋体"}[BFD]{lang="FR"}[控制报文。]{style="font-family:宋体"}

[**[passive]{lang="FR"}**]{#struct_0_x1819_x1365_x1179184334}[：被动模式。]{style="font-family:宋体"}[在建立会话前]{style="font-family:宋体"}[不会主动向会话的对端发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文，只有等收到]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文后才会向对端发送]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_346196377}

[[通信双方至少要有一方运行在主动模式才能成功建立起]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_277981179}[会话。]{style="font-family:宋体"}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_278872625}[版本]{style="font-family:宋体"}[0]{lang="EN-US"}[不支持本命令，配置不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_298758777}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_13289702}[配置]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话建立前的运行模式为]{style="font-family:宋体"}[被动模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x1819_x1365_x221764580}

[\[Sysname\] bfd ]{lang="FR"}[session init-mode passive]{lang="EN-US"}
:::

::::: {#-1518506188 .myid}
[]{#_Toc404796214}[]{#struct_0_x1819_x1365_x1903820747}[]{#_Toc366143764}[]{#_Toc365986721}[]{#_Toc361649473}

**BFD \-- BFD配置命令 \-- bfd template**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](BFD命令.files/image003.png){#图片 8 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1819_x1365_x98787093}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1819_x1365_x1225833105}
:::

[ ]{lang="EN-US"}

[**[bfd template]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1903755211}[命令用来创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模板，并进入]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[**[undo bfd template]{lang="EN-US"}**]{#struct_0_x1819_x1365_x376435027}[命令用来删除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x51814318}

[**[bfd template]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_x1819_x1365_117142592}

[**[undo bfd template]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_x1819_x1365_510628438}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_779281820}

[[没有创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1904213963}[模板。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1771869251}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_836156621}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1383978831}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1720274879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1043570248}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1904148427}

[*[template-name]{lang="EN-US"}*]{#struct_0_x1819_x1365_1036849207}[：]{style="font-family:宋体;color:black"}[BFD]{lang="SV" style="color:black"}[模板名称，为]{style="font-family:宋体;color:black"}[1]{lang="SV" style="color:black"}[～]{style="font-family:宋体;color:black"}[63]{lang="SV" style="color:black"}[个字符的字符串，区分大小写。]{style="font-family:宋体;color:black"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x719895472}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_1148793072}[创建]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模板]{style="font-family:宋体"}[bfd1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[BFD]{lang="EN-US"}[模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_1624100577}

[\[Sysname\] bfd template bfd1]{lang="EN-US"}

[\[Sysname-bfd-template-bfd1\]]{lang="EN-US"}
:::::

::: {#827567293 .myid}
[]{#_Toc404796215}[]{#struct_0_x1819_x1365_x1324798185}

**BFD \-- BFD配置命令 \-- display bfd session**

------------------------------------------------------------------------

[**[display bfd session]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1015064204}[命令用来显示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1944050684}

[**[display bfd session ]{lang="EN-US"}**[\[ **discriminator** *value* \| **verbose** \]]{lang="EN-US"}]{#struct_0_x1819_x1365_88687566}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1962934391}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x81058534}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1467535277}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_405640843}

[[network-operator]{lang="EN-US"}]{#struct_0_x1819_x1365_2114958697}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1807653930}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1819_x1365_x1015129740}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1202687617}

[**[discriminator ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x1819_x1365_x1222999688}[：显示指定本地标识符的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}*[value]{lang="EN-US"}*[为本地标识符的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话概要信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1819_x1365_563817644}[：显示会话的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x466085187}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_x2095421601}[显示所有]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的信息（]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[\<Sysname\> display]{lang="EN-US"}]{#struct_0_x1819_x1365_764418533}[ bfd session]{lang="IT"}

[ ]{lang="IT"}

[ Total Session Num: 1     Up Session Num: 1     Init Mode: Active]{lang="IT"}

[ ]{lang="IT"}

[ IPv4 Session Working Under Ctrl Mode:]{lang="IT"}

[ ]{lang="IT"}

[ LD/RD          SourceAddr      DestAddr        State    Holdtime    Interface]{lang="IT"}

[ 513/513        1.1.1.1         1.1.1.2         Up       2297ms      GE1/0/1]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_x1819_x1365_1336396892}[显示所有]{style="font-family:宋体"}[BFD]{lang="IT"}[会话的信息]{style="font-family:宋体"}[（]{style="font-family:宋体"}[IPv6]{lang="IT"}[）]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[\<Sysname\> display bfd session]{lang="IT"}]{#struct_0_x1819_x1365_x1014933132}

[ ]{lang="IT"}

[ Total Session Num: 1     Up Session Num: 1     Init Mode: Active]{lang="IT"}

[ ]{lang="IT"}

[ IPv6 Session Working Under Ctrl Mode:]{lang="IT"}

[ ]{lang="IT"}

[       Local Discr: 513                  Remote Discr: 513]{lang="IT"}

[         Source IP: FE80::20C:29FF:FED4:7171]{lang="IT"}

[    Destination IP: FE80::20C:29FF:FE72:AC4D]{lang="IT"}

[     Session State: Up                      Interface: GE1/0/2]{lang="IT"}

[         Hold Time: 2142ms]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_x1819_x1365_x577198451}[显示]{style="font-family:宋体"}[BFD]{lang="IT"}[会话的详细信息]{style="font-family:
宋体"}[（]{style="font-family:宋体"}[IPv4]{lang="IT"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display bfd session verbose]{lang="IT"}]{#struct_0_x1819_x1365_x1014998668}

[ ]{lang="IT"}

[ Total Session Num: 1     Up Session Num: 1     Init Mode: Active]{lang="IT"}

[ ]{lang="IT"}

[ IPv4 Session Working Under Ctrl Mode:]{lang="IT"}

[ ]{lang="IT"}

[       Local Discr: 513                  Remote Discr: 513]{lang="IT"}

[         Source IP: 1.1.1.1            Destination IP: 1.1.1.2]{lang="IT"}

[     Session State: Up                      Interface: GigabitEthernet1/0/1]{lang="IT"}

[      Min Tx Inter: 500ms                Act Tx Inter: 500ms]{lang="IT"}

[      Min Rx Inter: 500ms                Detect Inter: 2500ms]{lang="IT"}

[          Rx Count: 42                       Tx Count: 43]{lang="IT"}

[      Connect Type: Direct             Running Up for: 00:00:20]{lang="IT"}

[         Hold Time: 2078ms                  Auth mode: None]{lang="IT"}

[       Detect Mode: Async                        Slot: 0]{lang="IT"}

[          Protocol: OSPF]{lang="IT"}

[          Version:1]{lang="IT"}

[         Diag Info: No Diagnostic]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_x1819_x1365_1992452180}[显示]{style="font-family:宋体"}[BFD]{lang="IT"}[会话的详细信息]{style="font-family:
宋体"}[（]{style="font-family:宋体"}[IPv6]{lang="IT"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display bfd session verbose]{lang="IT"}]{#struct_0_x1819_x1365_742551291}

[ ]{lang="IT"}

[ Total Session Num: 1     Up Session Num: 1     Init Mode: Active]{lang="IT"}

[ ]{lang="IT"}

[ IPv6 Session Working Under Ctrl Mode:]{lang="IT"}

[ ]{lang="IT"}

[       Local Discr: 513                  Remote Discr: 513]{lang="IT"}

[         Source IP: FE80::20C:29FF:FED4:7171]{lang="IT"}

[    Destination IP: FE80::20C:29FF:FE72:AC4D]{lang="IT"}

[     Session State: Up                      Interface: GigabitEthernet1/0/2]{lang="IT"}

[      Min Tx Inter: 500ms                Act Tx Inter: 500ms]{lang="IT"}

[      Min Rx Inter: 500ms                Detect Inter: 2500ms]{lang="IT"}

[          Rx Count: 38                       Tx Count: 38]{lang="IT"}

[      Connect Type: Direct             Running Up for: 00:00:15]{lang="IT"}

[         Hold Time: 2211ms                  Auth mode: None]{lang="IT"}

[       Detect Mode: Async                        Slot: 0]{lang="IT"}

[          Protocol: OSPFv3]{lang="IT"}

[          Version:1]{lang="IT"}

[         Diag Info: No Diagnostic]{lang="IT"}

[[表1-1 ]{lang="EN-US"}[display bfd session]{lang="EN-US"}]{#struct_0_x1819_x1365_1795097326}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1370420343}[[字段]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1014802060}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x563503469}

[[Total Session Num]{lang="IT"}]{#struct_0_x1819_x1365_x473923845}

[[所有]{style="font-family:宋体"}[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_1872721787}[会话的数目]{style="font-family:宋体"}

[[Up Session Num]{lang="IT"}]{#struct_0_x1819_x1365_x101793789}

[[up]{lang="EN-US"}]{#struct_0_x1819_x1365_x1149338382}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的数目]{style="font-family:宋体"}

[[Init Mode]{lang="FR"}]{#struct_0_x1819_x1365_x1014867596}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_630649578}[运行模式：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Active]{lang="FR"}]{#struct_0_x1819_x1365_x167031568}[：]{style="font-family:宋体"}[主动模式]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Passive]{lang="EN-US"}]{#struct_0_x1819_x1365_x391867143}[：]{style="font-family:
  宋体"}[被动模式]{lang="EN-US" style="font-family:宋体"}

[[Session Working Under Ctrl Mode]{lang="IT"}]{#struct_0_x1819_x1365_x156263616}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1961192427}[会话（有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[两种）的工作方式：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Ctrl]{lang="FR"}]{#struct_0_x1819_x1365_x1014670988}[：]{style="font-family:宋体"}[控制报文方式]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Echo]{lang="FR"}]{#struct_0_x1819_x1365_1786722419}[：]{style="font-family:宋体"}[e]{lang="FR"}[cho]{lang="FR"}[报文方式]{lang="EN-US" style="font-family:
  宋体"}

[[Local Discr/LD]{lang="EN-US"}]{#struct_0_x1819_x1365_1772260825}

[[会话的本地标识符]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x2007485114}

[[Remote Discr/RD]{lang="EN-US"}]{#struct_0_x1819_x1365_919079971}

[[会话的远端标识符]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014736524}

[[Source IP/SourceAddr]{lang="EN-US"}]{#struct_0_x1819_x1365_643820271}

[[会话的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1819_x1365_x351543157}[地址]{style="font-family:宋体"}

[[Destination IP/DestAddr]{lang="EN-US"}]{#struct_0_x1819_x1365_x1301441378}

[[会话的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1819_x1365_x248694196}[地址]{style="font-family:宋体"}

[[Session State/State]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014539916}

[[会话状态：]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x1819_x1365_x1555377111}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x1819_x1365_x1123181419}

[[会话所在的接口名]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1049933420}

[[Min Tx Inter]{lang="EN-US"}]{#struct_0_x1819_x1365_1870384658}

[[最小发送时间间隔]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014605452}

[[Min Rx Inter]{lang="EN-US"}]{#struct_0_x1819_x1365_1549699021}

[[最小接收时间间隔]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x651404028}

[[Act Tx Inter]{lang="EN-US"}]{#struct_0_x1819_x1365_x1775427554}

[[实际发送间隔]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1015064207}

[[Detect Inter]{lang="EN-US"}]{#struct_0_x1819_x1365_x1947632085}

[[实际检测间隔]{style="font-family:宋体"}]{#struct_0_x1819_x1365_291718425}

[[Rx Count]{lang="EN-US"}]{#struct_0_x1819_x1365_300272298}

[[接收的报文数]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1015129743}

[[Tx Count]{lang="EN-US"}]{#struct_0_x1819_x1365_1605972144}

[[发送的报文数]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1150106000}

[[Hold Time/Holdtime]{lang="EN-US"}]{#struct_0_x1819_x1365_790653264}

[[离会话检测时间超时的剩余时间]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014933135}

[[Auth mode]{lang="EN-US"}]{#struct_0_x1819_x1365_x1336713338}

[[会话的认证模式，目前只支持]{style="font-family:宋体"}[Simple]{lang="EN-US"}]{#struct_0_x1819_x1365_x1234404928}

[[Connect Type]{lang="EN-US"}]{#struct_0_x1819_x1365_x946646488}

[[接口的连接类型：]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014998671}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Direct]{lang="FR"}]{#struct_0_x1819_x1365_782533063}[：直连]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Indirect]{lang="FR"}]{#struct_0_x1819_x1365_2135235064}[：非直连]{style="font-family:宋体"}

[[Running up for]{lang="EN-US"}]{#struct_0_x1819_x1365_x1014802063}

[[会话持续]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1819_x1365_x2129587410}[的时间]{style="font-family:宋体"}

[[Detect Mode]{lang="EN-US"}]{#struct_0_x1819_x1365_x992090265}

[[检测模式：]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x26925761}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Async]{lang="FR"}]{#struct_0_x1819_x1365_x1014867599}[：异步模式]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Demand]{lang="FR"}]{#struct_0_x1819_x1365_1746394825}[：查询模式]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x1819_x1365_x493588086}

[[槽号]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1014670991}

[[Protocol]{lang="EN-US"}]{#struct_0_x1819_x1365_576934374}

[[协议名]{style="font-family:宋体"}]{#struct_0_x1819_x1365_1313906871}

[[Version]{lang="EN-US"}]{#struct_0_x1819_x1365_x1677442511}

[[版本号]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1677442512}

[[Diag Info]{lang="EN-US"}]{#struct_0_x1819_x1365_1847526066}

[[会话的诊断信息]{style="font-family:宋体"}]{#struct_0_x1819_x1365_240535744}

[ ]{lang="EN-US"}

::: {#1625973675 .myid}
[]{#_Toc404796216}[]{#struct_0_x1819_x1365_857699475}[]{#_Toc252801297}[]{#_Toc216757302}[]{#_Toc216757304}[]{#_Toc216757305}[]{#_Toc216757306}[]{#_Toc216757307}[]{#_Toc216757308}[]{#_Toc216757309}[]{#_Toc216757310}[]{#_Toc216757311}[]{#_Toc216757312}[]{#_Toc216757313}[]{#_Toc216757314}[]{#_Toc216757315}[]{#_Toc216757316}[]{#_Toc216757318}[]{#_Toc216757319}[]{#_Toc216757320}[]{#_Toc216757321}[]{#_Toc216757322}[]{#_Toc216757324}[]{#_Toc216757325}[]{#_Toc216757326}[]{#_Toc156030344}[]{#_Toc156128479}[]{#_Toc156187272}[]{#_Toc156030346}[]{#_Toc156128481}[]{#_Toc156187274}[]{#_Toc156030347}[]{#_Toc156128482}[]{#_Toc156187275}[]{#_Toc216757328}[]{#_Toc216757330}[]{#_Toc216757331}[]{#_Toc216757332}[]{#_Toc216757333}[]{#_Toc216757334}[]{#_Toc216757335}[]{#_Toc216757337}[]{#_Toc216757338}[]{#_Toc216757339}[]{#_Toc216757340}[]{#_Toc216757341}[]{#_Toc216757342}[]{#_Toc216757344}[]{#_Toc216757347}[]{#_Toc216757348}[]{#_Toc216757349}[]{#_Toc216757350}[]{#_Toc216757352}[]{#_Toc216757353}[]{#_Toc216757354}[]{#_Toc216757355}[]{#_Toc216757356}[]{#_Toc168729230}[]{#_Toc168729250}[]{#_Toc216757357}[]{#_Toc216757358}[]{#_Toc216757361}[]{#_Toc216757362}[]{#_Toc216757363}[]{#_Toc216757364}[]{#_Toc216757365}[]{#_Toc216757366}[]{#_Toc216757367}[]{#_Toc216757368}[]{#_Toc216757369}[]{#_Toc216757370}[]{#_Toc216757371}[]{#_Toc216757372}[]{#_Toc216757373}[]{#_Toc216757375}[]{#_Toc216757376}[]{#_Toc216757377}[]{#_Toc216757378}[]{#_Toc216757380}[]{#_Toc216757381}[]{#_Toc216757383}[]{#_Toc216757384}[]{#_Toc216757386}[]{#_Toc216757387}[]{#_Toc216757388}[]{#_Toc216757389}[]{#_Toc216757390}[]{#_Toc216757391}[]{#_Toc216757392}[]{#_Toc216757393}[]{#_Toc216757394}[]{#_Toc216757395}[]{#_Toc216757396}[]{#_Toc216757397}[]{#_Toc216757398}[]{#_Toc216757401}[]{#_Toc216757402}[]{#_Toc216757404}[]{#_Toc216757405}[]{#_Toc216757406}[]{#_Toc216757407}[]{#_Toc216757408}[]{#_Toc216757409}[]{#_Toc216757410}[]{#_Toc216757411}[]{#_Toc216757412}[]{#_Toc216757413}[]{#_Toc216757414}[]{#_Toc216757415}[]{#_Toc216757417}[]{#_Toc216757418}[]{#_Toc171737042}[]{#_Toc172357889}[]{#_Toc164674382}[]{#_Toc164674495}[]{#_Toc164674514}[]{#_Toc164674534}[]{#_Toc164674945}[]{#_Toc165084980}[]{#_Toc164674383}[]{#_Toc164674496}[]{#_Toc164674515}[]{#_Toc164674535}[]{#_Toc164674946}[]{#_Toc165084981}

**BFD \-- BFD配置命令 \-- reset bfd session statistics**

------------------------------------------------------------------------

[**[reset bfd session statistics]{lang="EN-US"}**]{#struct_0_x1819_x1365_1713316391}[命令用来清除所有]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[会话的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x392302988}

[**[reset bfd session statistics]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1421001578}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1014539919}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1602431278}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x634100758}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x989928950}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x976314252}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x584330097}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_2046575775}[清除所有]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset bfd session statistics]{lang="EN-US"}]{#struct_0_x1819_x1365_x727983704}
:::

::: {#-1326495703 .myid}
[]{#_Toc404796217}[]{#struct_0_x1819_x1365_x1533691492}[]{#_Toc381174034}[]{#_Toc376523170}[]{#_Toc327365449}

**BFD \-- BFD配置命令 \-- snmp-agent trap enable bfd**

------------------------------------------------------------------------

[**[snmp-agent trap enable bfd]{lang="EN-US"}**]{#struct_0_x1819_x1365_324434096}[命令用来开启]{style="font-family:
宋体"}[BFD]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable bfd]{lang="EN-US"}**]{#struct_0_x1819_x1365_80231149}[命令用来关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x2077011329}

[**[snmp-agent trap enable bfd]{lang="EN-US"}**]{#struct_0_x1819_x1365_x567119284}

[**[undo snmp-agent trap enable bfd]{lang="EN-US"}**]{#struct_0_x1819_x1365_x1533625956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1960800238}

[[BFD]{lang="EN-US"}]{#struct_0_x1819_x1365_x1488563515}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_2025187949}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1819_x1365_x1826966945}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_1733092979}

[[network-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_x1804861865}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1819_x1365_1090840114}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1534215775}

[[开启]{style="font-family:宋体"}]{#struct_0_x1819_x1365_786055477}[BFD]{lang="EN-US"}[模块的告警功能后，该模块会生成告警信息，用于报告该模块的重要事件。生成的告警信息将发送到设备的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。（有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1819_x1365_x1678046186}

[[\# ]{lang="EN-US"}]{#struct_0_x1819_x1365_421778817}[关闭]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1819_x1365_200250720}

[\[Sysname\] undo snmp-agent trap enable bfd]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
