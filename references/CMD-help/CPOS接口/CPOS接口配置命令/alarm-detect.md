::::: {#1725110147 .myid}
[]{#_Toc296086815}[]{#_Toc295480285}[]{#_Toc295465879}[]{#_Toc404783841}[]{#struct_0_x1849_14381_x1846575615}[]{#_Toc345232201}

**CPOS接口 \-- CPOS接口配置命令 \-- alarm-detect**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){#图片 15 width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1845902761}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_292989060}
:::

**[ ]{lang="EN-US"}**

[**[alarm-detect]{lang="EN-US"}**]{#struct_0_x1849_14381_1279272535}[命令用来设置当前接口的告警联动动作。]{style="font-family:宋体"}

[**[undo alarm-detect]{lang="EN-US"}**]{#struct_0_x1849_14381_7675516}[命令用来取消告警联动动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1227104221}

[**[alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** } **action** **link-down**]{lang="EN-US"}]{#struct_0_x1849_14381_1234450643}

[**[undo alarm-detect]{lang="EN-US"}**[ { **rdi** \| **sd** \| **sf** }]{lang="EN-US"}]{#struct_0_x1849_14381_x1846510079}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2143800955}

[[接口不执行任何告警联动动作。]{style="font-family:宋体"}]{#struct_0_x1849_14381_159200850}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x1849_14381_4895700}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1286191022}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x928353804}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1980587720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1846444543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1322770777}

[**[rdi]{lang="EN-US"}**]{#struct_0_x1849_14381_x1409391047}[：表示]{style="font-family:宋体"}[RDI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Defect Indication]{lang="EN-US"}[，远端失效指示）告警。]{style="font-family:宋体"}

[**[sd]{lang="EN-US"}**]{#struct_0_x1849_14381_2075915624}[：表示]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x1849_14381_1972536588}[：表示]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警。]{style="font-family:宋体"}

[**[action]{lang="EN-US"}**]{#struct_0_x1849_14381_1239281678}[：设置当接口检测到告警时的联动动作。]{style="font-family:宋体"}

[**[link-down]{lang="EN-US"}**]{#struct_0_x1849_14381_x609115965}[：表示自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1846379007}

[[当设备收到对端发送的]{style="font-family:宋体"}[MS-RDI]{lang="EN-US"}]{#struct_0_x1849_14381_936618891}[信号时，则认为发生了]{style="font-family:宋体"}[RDI]{lang="EN-US"}[告警。当设备收到的报文的误码率达到或超过设置的门限时，则生成]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警或]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警的门限可通过]{style="font-family:宋体"}**[threshold]{lang="EN-US"}**[命令设置。]{style="font-family:宋体"}

[[配置本命令后，当设备检测到告警时，会自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1849_14381_x508965666}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x13944629}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1659566436}[配置当]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口检测到]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警时，自动将接口的物理状态设置为]{style="font-family:宋体"}[down]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1846837759}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] alarm-detect sd action link-down]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2022686342}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[threshold]{lang="EN-US"}**]{#struct_0_x1849_14381_980762223}
:::::

::: {#424787513 .myid}
[]{#_Toc255917473}[]{#_Toc136937619}[]{#_Toc404783842}[]{#struct_0_x1849_14381_1226030748}

**CPOS接口 \-- CPOS接口配置命令 \-- clock**

------------------------------------------------------------------------

[**[clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x974703644}[命令用来设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的时钟模式。]{style="font-family:宋体"}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x450726087}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_710424338}

[**[clock]{lang="EN-US"}**[ { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1849_14381_x1004038769}

[**[undo clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x1823549744}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_616728326}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x820931624}[接口的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1251833430}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_476038713}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2050265371}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_765302492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1080018660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_258985064}

[**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_x975017596}[：设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_616662790}[：设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1933927774}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_264680998}[接口支持两种时钟模式：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_x1138667689}[：主时钟模式，使用内部时钟信号；]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_2000914281}[：从时钟模式，使用线路提供的时钟信号。]{style="font-family:
宋体"}

[[与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}]{#struct_0_x1849_14381_1395845252}[设备相连时，由于]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[网络的时钟精度高于]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[本身内部时钟源的精度，应配置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[使用从时钟模式。如果]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x27347591}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_838950991}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448954}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] clock master]{lang="EN-US"}
:::

::: {#-1998942572 .myid}
[]{#_Toc404783843}[]{#struct_0_x1849_14381_x647301972}[]{#_Toc255917474}[]{#_Toc136937620}

**CPOS接口 \-- CPOS接口配置命令 \-- controller cpos**

------------------------------------------------------------------------

[**[controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_1968735648}[命令用来进入]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x85943690}

[**[controller cpos]{lang="EN-US"}**[ *cpos-number*]{lang="EN-US"}]{#struct_0_x1849_14381_x1421986073}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_236071439}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1763305073}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1248478171}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1872904492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1756514490}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1009424650}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_428052220}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_322074972}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1000520462}[进入]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的接口视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1276599169}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\]]{lang="EN-US"}
:::

::: {#1948332219 .myid}
[]{#_Toc275183039}[]{#_Toc272413471}[]{#_Toc261965075}[]{#_Toc205607679}[]{#_Toc404783844}[]{#struct_0_x1849_14381_x706597483}[]{#_Toc329007815}[]{#_Toc309912009}

**CPOS接口 \-- CPOS接口配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x1849_14381_x7975141}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_170203605}

[**[default]{lang="EN-US"}**]{#struct_0_x1849_14381_x1756580026}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_796270367}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1621452979}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1212915429}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x286891571}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x107628026}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1192531578}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2081692822}

[[您可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x1849_14381_x631757979}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1756645562}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1016990578}[将]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_351405057}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] default]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404783845}[]{#struct_0_x1849_14381_x389481315}

**CPOS接口 \-- CPOS接口配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1849_14381_302299524}[命令用来设置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1849_14381_207342698}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_576251044}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1849_14381_1762345776}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x1849_14381_x1756711098}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x691879398}

[[接口的描述信息为"*该接口的接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x1849_14381_x1362490050}["，比如：]{style="font-family:宋体"}[Cpos2/4/0 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1424427750}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1180390386}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x601285710}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_2120234951}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1739019438}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1119533734}

[*[text]{lang="EN-US"}*]{#struct_0_x1849_14381_x1756776634}[：接口描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1219832350}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1136258142}[配置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[CPOS-interface]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x545211847}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] description CPOS-interface]{lang="EN-US"}
:::

::: {#-790475304 .myid}
[]{#_Toc404783846}[]{#struct_0_x1849_14381_907183426}[]{#_Toc255917498}[]{#_Toc136937621}[]{#_Toc255917476}[]{#_Toc255917478}[]{#_Toc255917479}[]{#_Toc255917480}[]{#_Toc255917481}[]{#_Toc255917482}[]{#_Toc255917483}[]{#_Toc255917484}[]{#_Toc255917485}[]{#_Toc255917486}[]{#_Toc255917487}[]{#_Toc255917488}[]{#_Toc255917489}[]{#_Toc255917490}[]{#_Toc255917491}

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos**

------------------------------------------------------------------------

[**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_x896784887}[命令用来显示]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[物理接口状态信息，以及再生段、复用段和高阶通道的告警及错误信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1130166460}

[**[display controller cpos]{lang="EN-US"}**[ \[ *cpos-number* \]]{lang="EN-US"}]{#struct_0_x1849_14381_x1665389624}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1756842170}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x25091528}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1091720209}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_917683797}

[[network-operator]{lang="EN-US"}]{#struct_0_x1849_14381_2072943267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1013539886}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x1554787383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_145610077}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x100719371}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的编号。如果不指定]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的编号，则显示所有]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的所有通道信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1756907706}

[[显示信息中可能出现的错误类型如]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1011261704}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-1]{lang="EN-US"}](?-790475304#_Ref196800432)[所示。]{style="font-family:宋体"}

[]{#struct_0_x1849_14381_1546705813}[]{#_Ref196800432}[]{#_Toc95307567}[]{#_Toc85599410}[]{#_Toc81465853}[[表1-1 ]{lang="EN-US"}[display controller cpos]{lang="EN-US"}]{#_Toc81465258}[命令可能出现的错误类型]{style="font-family:黑体"}

[]{#table_struct_0_1427668980}[[字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1928141406}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_1644600344}

[[FRED]{lang="EN-US"}]{#struct_0_x1849_14381_953303951}

[[Receive Loss of Basic Frame Alignment]{lang="EN-US"}]{#struct_0_x1849_14381_1380082400}[，接收到基本帧失位。也可以认为是收到有红色告警错误的帧]{style="font-family:宋体"}

[[COFA]{lang="EN-US"}]{#struct_0_x1849_14381_x288518596}

[[Change of Frame Alignment]{lang="EN-US"}]{#struct_0_x1849_14381_x1755924666}[，帧对齐改变]{style="font-family:宋体"}

[[SEF]{lang="EN-US"}]{#struct_0_x1849_14381_810064930}

[[Severely Errored Frame]{lang="EN-US"}]{#struct_0_x1849_14381_x20556124}[，严重错帧，连续]{style="font-family:宋体"}[4]{lang="EN-US"}[个帧同步错误将产生一个]{style="font-family:宋体"}[SEF]{lang="EN-US"}

[[FERR]{lang="EN-US"}]{#struct_0_x1849_14381_x559847966}

[[Framing Bit Error]{lang="EN-US"}]{#struct_0_x1849_14381_x838810931}[，指有]{style="font-family:宋体"}[Ft/Fs/FPS/FAS]{lang="EN-US"}[错误的帧]{style="font-family:宋体"}

[[CERR]{lang="EN-US"}]{#struct_0_x1849_14381_1952506648}

[[CRC Error]{lang="EN-US"}]{#struct_0_x1849_14381_x1755990202}[，循环冗余校验错]{style="font-family:宋体"}

[[FEBE]{lang="EN-US"}]{#struct_0_x1849_14381_1809125357}

[[Far End Block Error]{lang="EN-US"}]{#struct_0_x1849_14381_934636247}[，远端块错。这种错误只有在]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道采用]{style="font-family:宋体"}[CRC4]{lang="EN-US"}[的帧格式时才可能出现。]{style="font-family:宋体"}

[[BERR]{lang="EN-US"}]{#struct_0_x1849_14381_x1056212790}

[[PRBS Bit Error]{lang="EN-US"}]{#struct_0_x1849_14381_1093747244}[（随机码测试位错，只用于测试）]{style="font-family:宋体"}

[[BIP]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448953}

[[Bit-Interleaved Parity]{lang="EN-US"}]{#struct_0_x1849_14381_x244017445}[，比特交叉奇偶校验]{style="font-family:宋体"}

[[REI]{lang="EN-US"}]{#struct_0_x1849_14381_x713832097}

[[Remote Error Indication]{lang="EN-US"}]{#struct_0_x1849_14381_x857613}[，远端错误指示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[在上表中，前三种错误（]{style="font-family:宋体"}[FRED]{lang="EN-US"}]{#struct_0_x1849_14381_561034749}[、]{style="font-family:宋体"}[COFA]{lang="EN-US"}[、]{style="font-family:宋体"}[SEF]{lang="EN-US"}[）统称为]{style="font-family:宋体"}[Alarm Error]{lang="EN-US"}[，简写为]{style="font-family:宋体"}[AERR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[相关配置可参考命令]{style="font-family:宋体"}**[display controller cpos e1]{lang="EN-US"}**]{#struct_0_x1849_14381_x1994954523}[和]{style="font-family:宋体"}**[display controller cpos t1]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_12187717}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1756514489}[查看]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的所有通道信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller cpos 2/4/0]{lang="EN-US"}]{#struct_0_x1849_14381_x1756580025}

[Cpos2/4/0 current state: DOWN]{lang="EN-US"}

[Description : Cpos2/4/0 Interface]{lang="EN-US"}

[Frame-format SDH,multiplex AU-4,clock master,loopback none]{lang="EN-US"}

[SD threshold: 6, SF threshold: 3]{lang="EN-US"}

[Optical:Absent]{lang="EN-US"}

[ ]{lang="EN-US"}

[Regenerator section:]{lang="EN-US"}

[  Tx: J0:\"\"  (HEX: )]{lang="EN-US"}

[  ]{lang="EN-US"}[Rx: J0:\"\"  (HEX: )]{lang="PT-BR"}

[  Alarm: ]{lang="EN-US"}[LOS  LOF  OOF]{lang="PT-BR"}

[  Error:  0 RS_BIP]{lang="EN-US"}

[ ]{lang="EN-US"}

[Multiplex section:]{lang="EN-US"}

[  Alarm: MS_AIS  MS_SF  MS_SD]{lang="EN-US"}

[  Error:  0 MS_BIP , 0 MS_REI]{lang="EN-US"}

[ ]{lang="EN-US"}

[Higher order Path (VC-4-1):]{lang="EN-US"}

[  Tx: J1:\"\", C2:0x02, S1S0:0x02]{lang="EN-US"}

[  Rx: J1:\"\", C2:0x6d, S1S0:0x02]{lang="EN-US"}

[  Alarm:   HP_TIU  HP_RDI  HP_ERDI  HP_PLM]{lang="EN-US"}

[  Error:  0 HP_BIP, 0 HP_REI, 0 HP_PJE, 0 HP_NJE]{lang="EN-US"}

[ ]{lang="EN-US"}

[CT1 1 is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[CT1 2 is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[CT1 3 is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[（此处省略部分]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的显示信息）]{style="font-family:宋体"}

[CT1 83 is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[CT1 84 is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[]{#struct_0_x1849_14381_2093102702}[]{#_Toc95307568}[]{#_Toc85599411}[]{#_Toc81465854}[[表1-2 ]{lang="EN-US"}[display controller cpos]{lang="EN-US"}]{#_Toc81465259}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1428982514}[[字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_1245274773}

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_838300077}

[[Cpos2/4/0 current state]{lang="EN-US"}]{#struct_0_x1849_14381_748589310}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x2042959271}[接口当前的物理状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1849_14381_x1756645561}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1849_14381_1420275105}

[[Frame-format SDH, multiplex AU-4, clock master, loopback none]{lang="EN-US"}]{#struct_0_x1849_14381_1631311441}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1631428774}[接口的物理层信息：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[、采用]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[的复用路径、主时钟模式（使用内部时钟信号）、没有使能环回]{style="font-family:宋体"}

[[SD threshold: 6 , SF threshold: 3]{lang="EN-US"}]{#struct_0_x1849_14381_x1528710803}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x92448634}[接口的]{style="font-family:宋体"}[SD]{lang="EN-US"}[（信号衰减）和]{style="font-family:宋体"}[SF]{lang="EN-US"}[（信号失败）的门限值]{style="font-family:宋体"}

[[Optical:]{lang="EN-US"}]{#struct_0_x1849_14381_x1756711097}

[[传输介质的模块]{style="font-family:宋体"}]{#struct_0_x1849_14381_1230434903}

[[Regenerator section]{lang="EN-US"}]{#struct_0_x1849_14381_x1756776633}

[[再生段的告警和错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1979347237}

[[Tx: J0]{lang="NL-BE"}]{#struct_0_x1849_14381_x2054248513}

[[发送的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2053920833}

[[Rx: J0]{lang="NL-BE"}]{#struct_0_x1849_14381_x1424334672}

[[接收的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2053855297}

[[Alarm]{lang="EN-US"}]{#struct_0_x1849_14381_x2054051905}

[[对应支路的告警统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2053986369}

[[Error]{lang="EN-US"}]{#struct_0_x1849_14381_x863165845}

[[错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2054707265}

[[Multiplex section]{lang="EN-US"}]{#struct_0_x1849_14381_x979067909}

[[复用段的告警和错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1965864798}

[[Higher order Path(VC-4-1)]{lang="EN-US"}]{#struct_0_x1849_14381_x364135485}

[[高阶通道的告警和错误统计。]{style="font-family:宋体"}[VC-4-1]{lang="EN-US"}]{#struct_0_x1849_14381_x1756842169}[表示采用]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[的复用路径，只有一个高阶通道]{style="font-family:宋体"}[VC-4]{lang="EN-US"}

[[CT1 1 is down]{lang="EN-US"}]{#struct_0_x1849_14381_x1756907705}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_x607977177}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[当前的物理状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}]{#struct_0_x1849_14381_x2117382252}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_1606745589}[通道的物理层信息：帧格式为]{style="font-family:宋体"}[ESF]{lang="EN-US"}[、从时钟模式、没有使能环回]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x594384233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos]{lang="ES-AR"}**]{#struct_0_x1849_14381_977664076}**[ e1]{lang="ES-AR"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos]{lang="ES-AR"}**]{#struct_0_x1849_14381_x1755924665}**[ t1]{lang="ES-AR"}**

::: {#1374130991 .myid}
[]{#_Toc404783847}[]{#struct_0_x1849_14381_x756019011}[]{#_Toc255917499}[]{#_Toc136937622}

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos e1**

------------------------------------------------------------------------

[**[display controller cpos e1]{lang="EN-US"}**]{#struct_0_x1849_14381_x2019876382}[命令用来显示指定]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x666319138}

[**[display controller cpos ]{lang="ES-AR"}***[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x602476350}[ ]{lang="EN-US"}**[e1]{lang="ES-AR"}**[ ]{lang="ES-AR"}*[e1-number]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1106126180}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_778868601}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x345815556}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1320504324}

[[network-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x1755990201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x919757998}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1849_14381_849168228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1284601658}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1887153625}[：显示指定接口编号的]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的物理层配置信息。]{style="font-family:宋体"}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1487589930}[：显示指定]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号的]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的物理层配置信息，]{style="font-family:宋体"}*[e1-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_555435665}

[[与]{style="font-family:宋体"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_1426413704}[命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及]{style="font-family:宋体"}[E1]{lang="EN-US"}[帧的错误和告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1524264659}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448956}[查看]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:
宋体"}[E1]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller cpos 2/4/0 e1 1]{lang="EN-US"}]{#struct_0_x1849_14381_515497442}

[Cpos2/4/0 current state: DOWN]{lang="EN-US"}

[Description: Cpos2/4/0 Interface]{lang="EN-US"}

[ ]{lang="EN-US"}

[Lower order path:]{lang="EN-US"}

[  TxFlag: J2: \"\"    LP-C2: 2]{lang="EN-US"}

[  RxFlag: J2: \"\"    LP-C2: 7]{lang="EN-US"}

[  Alarm:  LP-AIS  LP-RDI  LP-RFI  LP-C2-Mismatched  LP-J2-Unstable]{lang="EN-US"}

[  Error:  1164 BIP2,  2047 FEBE]{lang="EN-US"}

[CE1  1 (1-1-1-1) is down]{lang="EN-US"}

[  Frame-format: NO-CRC4,  clock: slave,  loopback: none]{lang="EN-US"}

[  Alarm:  AIS  LFA  Red]{lang="EN-US"}

[  Error:  0 Fer]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display controller cpos e1]{lang="EN-US"}]{#struct_0_x1849_14381_x1756514492}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1452397807}[[主要字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_153374764}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_1823848164}

[[Cpos2/4/0 current state]{lang="EN-US"}]{#struct_0_x1849_14381_x1269770314}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1278775647}[接口当前的物理状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1849_14381_x2054051908}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2053986372}

[[Lower order path]{lang="EN-US"}]{#struct_0_x1849_14381_x2054707268}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x2054641732}[低阶通道的告警和错误统计]{style="font-family:宋体"}

[[Tx]{lang="NL-BE"}[Flag]{lang="EN-US"}]{#struct_0_x1849_14381_x2054182981}

[[发送的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2054117445}

[[Rx]{lang="NL-BE"}[Flag]{lang="EN-US"}]{#struct_0_x1849_14381_x2054314053}

[[接收的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2054248517}

[[当收到的]{style="font-family:宋体"}[J2]{lang="EN-US"}]{#struct_0_x1849_14381_x2053920837}[为不可见字符时，显示为：]{style="font-family:宋体"}[RxFlag: J2: unknow]{lang="EN-US"}

[[Alarm]{lang="EN-US"}]{#struct_0_x1849_14381_x1756711100}

[[对应支路的告警统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x336107791}

[[Error]{lang="EN-US"}]{#struct_0_x1849_14381_521045048}

[[错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x158534499}

[[CE1 1 (1-1-1-1) is down ]{lang="EN-US"}]{#struct_0_x1849_14381_x1707401209}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x1756776636}[通道当前的物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，]{style="font-family:宋体"}[1-1-1-1]{lang="EN-US"}[依次表示此]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道所属的]{style="font-family:宋体"}[VC-4]{lang="EN-US"}[编号、]{style="font-family:宋体"}[TUG-3]{lang="EN-US"}[编号、]{style="font-family:宋体"}[TUG-2]{lang="EN-US"}[编号和]{style="font-family:宋体"}[TU-12]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Frame-format: NO-CRC4,  clock: slave,  loopback: none]{lang="EN-US"}]{#struct_0_x1849_14381_1912335532}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x1806081252}[通道的物理层信息：帧格式为]{style="font-family:宋体"}[no-CRC4]{lang="PT-BR"}[，]{style="font-family:宋体"}[从时钟模式、没有使能环回]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1374262063 .myid}
[]{#_Toc404783848}[]{#struct_0_x1849_14381_1137707886}[]{#_Toc255917500}[]{#_Toc194725117}[]{#_Toc171825210}[]{#_Toc175800416}[]{#_Toc175800481}[]{#_Toc197678728}[]{#_Toc197678729}[]{#_Toc197678730}[]{#_Toc197678731}[]{#_Toc197678732}[]{#_Toc197678733}[]{#_Toc197678734}[]{#_Toc197678735}[]{#_Toc197678736}[]{#_Toc197678737}[]{#_Toc197678738}[]{#_Toc197678739}[]{#_Toc197678740}[]{#_Toc197678741}[]{#_Toc197678763}[]{#_Toc197678806}

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos e3**

------------------------------------------------------------------------

[**[display controller cpos e3]{lang="EN-US"}**]{#struct_0_x1849_14381_x508447007}[命令用来显示指定]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x33730766}

[**[display controller cpos ]{lang="ES-AR"}***[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_964133991}[ ]{lang="EN-US"}**[e3]{lang="ES-AR"}**[ ]{lang="ES-AR"}*[e3-number]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1533838478}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1015646236}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1386120704}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1756907708}

[[network-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x204692650}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x952432527}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1849_14381_1164904789}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x315480807}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_179360413}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口编号。]{style="font-family:宋体"}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x584635691}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1106146245}

[[与]{style="font-family:宋体"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_692194913}[命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及]{style="font-family:宋体"}[E3]{lang="EN-US"}[帧的错误和告警信息。显示信息中可能出现的错误类型如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-4]{lang="EN-US"}](?1374262063#_Ref194484615)[所示。]{style="font-family:宋体"}

[]{#struct_0_x1849_14381_x1755924668}[[表1-4 ]{lang="EN-US"}[display controller cpos e3/t3]{lang="EN-US"}]{#_Ref194484615}[命令可能出现的错误类型]{style="font-family:黑体"}

[]{#table_struct_0_1448558276}[[字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_x352734484}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_1302863944}

[[OOF]{lang="EN-US"}]{#struct_0_x1849_14381_1749790283}

[[Out Of Frame]{lang="EN-US"}]{#struct_0_x1849_14381_830423932}[，接收到基本帧失位，也就是收到]{style="font-family:宋体"}[E3/T3]{lang="EN-US"}[帧定位比特出错]{style="font-family:宋体"}

[[LOS]{lang="EN-US"}]{#struct_0_x1849_14381_374429482}

[[Loss Of Signal]{lang="EN-US"}]{#struct_0_x1849_14381_x760518489}[，信号丢失，检测到输入信号丢失产生的]{style="font-family:宋体"}

[[LOF]{lang="EN-US"}]{#struct_0_x1849_14381_x1755990204}

[[Loss Of Frame]{lang="EN-US"}]{#struct_0_x1849_14381_x1679272885}[，帧丢失，连续多次检测到]{style="font-family:宋体"}[OOF]{lang="EN-US"}[时产生的。]{style="font-family:宋体"}

[[AIS]{lang="EN-US"}]{#struct_0_x1849_14381_1315465419}

[[Alarm Indication Signal]{lang="EN-US"}]{#struct_0_x1849_14381_2090820209}[，告警指示信号，本端检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[等严重告警时产生，并会传到下游，因此它也可能是上游设备传来的]{style="font-family:宋体"}

[[RAI]{lang="EN-US"}]{#struct_0_x1849_14381_x1369486556}

[[Remote Alarm Indication]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448955}[，远端告警指示，是下游设备检测到告警传来的]{style="font-family:宋体"}

[[MS_AIS]{lang="EN-US"}]{#struct_0_x1849_14381_918781969}

[[Multiplex  Section Alarm Indication Signal]{lang="EN-US"}]{#struct_0_x1849_14381_311715260}[，复用段告警指示信号]{style="font-family:宋体"}[(AIS)]{lang="EN-US"}

[[FERR]{lang="EN-US"}]{#struct_0_x1849_14381_x187690162}

[[Framing Bit Error Event]{lang="EN-US"}]{#struct_0_x1849_14381_1024148782}[，帧定位比特错误计数]{style="font-family:宋体"}

[[LCV]{lang="EN-US"}]{#struct_0_x1849_14381_x1518741359}

[[Line code Violation]{lang="EN-US"}]{#struct_0_x1849_14381_x1756514491}[，线路编码不符]{style="font-family:宋体"}[HDB3]{lang="EN-US"}[（]{style="font-family:宋体"}[E3]{lang="EN-US"}[）或]{style="font-family:宋体"}[B3ZS]{lang="EN-US"}[（]{style="font-family:宋体"}[T3]{lang="EN-US"}[）的计数]{style="font-family:宋体"}

[[PERR]{lang="EN-US"}]{#struct_0_x1849_14381_1719458705}

[[Parity Error Event]{lang="EN-US"}]{#struct_0_x1849_14381_x72046216}[，奇偶校验错误计数，]{style="font-family:宋体"}[T3]{lang="EN-US"}[帧]{style="font-family:宋体"}[P1]{lang="EN-US"}[和]{style="font-family:宋体"}[P2]{lang="EN-US"}[比特不等产生，只用于]{style="font-family:宋体"}[T3]{lang="EN-US"}

[[FEBE]{lang="EN-US"}]{#struct_0_x1849_14381_2019551891}

[[Far Error Block Event]{lang="EN-US"}]{#struct_0_x1849_14381_1733788707}[，远端错误块计数，下游传上来的，只用于]{style="font-family:宋体"}[T3]{lang="EN-US"}

[[HCS]{lang="EN-US"}]{#struct_0_x1849_14381_x1756580027}

[[Header Check Sequence]{lang="EN-US"}]{#struct_0_x1849_14381_x1932612988}[，]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[帧]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误计数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x87928424}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1025823813}[查看]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:
宋体"}[E3]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller cpos 2/4/0 e3 1]{lang="EN-US"}]{#struct_0_x1849_14381_x1445097304}

[Cpos2/4/0 current state: UP]{lang="EN-US"}

[Description: Cpos2/4/0 Interface]{lang="EN-US"}

[E3 1: up]{lang="EN-US"}

[  Frame-format: G.751, Clock: slave, Loopback: none]{lang="EN-US"}

[  national-bit: 1]{lang="EN-US"}

[  Alarm: NONE]{lang="EN-US"}

[  Error: 0 FERR, 0 LCV, 0 HCS]{lang="EN-US"}

[]{#struct_0_x1849_14381_x1756645563}[[表1-5 ]{lang="EN-US"}[display controller cpos e3/t3]{lang="EN-US"}]{#_Ref194484623}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1443919148}[[字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1711892777}

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_x108517808}

[[Cpos2/4/0 current state]{lang="EN-US"}]{#struct_0_x1849_14381_1765363476}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x369118784}[接口当前的物理状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1849_14381_1651604449}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1849_14381_1754813022}

[[E3 1]{lang="EN-US"}]{#struct_0_x1849_14381_x1756711099}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_2037003957}[通道的状态]{style="font-family:宋体"}

[[Frame-format]{lang="EN-US"}]{#struct_0_x1849_14381_x311788230}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_1911256987}[帧格式]{style="font-family:宋体"}

[[Clock]{lang="EN-US"}]{#struct_0_x1849_14381_x881725803}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_x1780839404}[通道时钟模式]{style="font-family:宋体"}

[[Loopback]{lang="EN-US"}]{#struct_0_x1849_14381_x1756776635}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_1509051005}[通道的环回模式]{style="font-family:宋体"}

[[national-bit]{lang="EN-US"}]{#struct_0_x1849_14381_x418867068}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_312166330}[国际（内）通信码值]{style="font-family:宋体"}

[[Alarm]{lang="EN-US"}]{#struct_0_x1849_14381_1674348913}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_x1756842171}[通道告警]{style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_x1849_14381_1540992413}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_740645239}[通道错误计数]{style="font-family:宋体"}

[ ]{lang="DE"}

::: {#1374130974 .myid}
[]{#_Toc404783849}[]{#struct_0_x1849_14381_1538269249}[]{#_Toc255917501}

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos t1**

------------------------------------------------------------------------

[**[display controller cpos t1]{lang="EN-US"}**]{#struct_0_x1849_14381_x1360116323}[命令用来显示指定]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x74209742}

[**[display controller cpos ]{lang="EN-US"}***[cpos-number]{lang="EN-US"}*[ **t1** *t1-number*]{lang="EN-US"}]{#struct_0_x1849_14381_1302448484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1030240186}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1756907707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_554822237}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_590760408}

[[network-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x638654960}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1296560022}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x572815669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1107468079}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1442412790}[：显示指定接口编号的]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的物理层配置信息。]{style="font-family:宋体"}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1755924667}[：显示指定]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号的]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的物理层配置信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1918818425}

[[与]{style="font-family:宋体"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_52736148}[命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及]{style="font-family:宋体"}[T1]{lang="EN-US"}[帧的错误和告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1352857400}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1719399372}[查看]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:
宋体"}[T1]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display controller cpos 2/4/0 t1 1]{lang="EN-US"}]{#struct_0_x1849_14381_x1755990203}

[Cpos2/4/0 current state: DOWN]{lang="EN-US"}

[Description : Cpos2/4/0 Interface]{lang="EN-US"}

[ ]{lang="EN-US"}

[Lower order path:]{lang="EN-US"}

[  TxFlag: J2: \"\"    LP-C2: 2]{lang="EN-US"}

[  RxFlag: J2: \"\"    LP-C2: 7]{lang="EN-US"}

[  Alarm:  LP-AIS  LP-RDI  LP-RFI  LP-C2-Mismatched  LP-J2-Unstable]{lang="EN-US"}

[  Error:  1080 BIP2,  2047 FEBE]{lang="EN-US"}

[CT1  1 (1-1-1-1) is down]{lang="EN-US"}

[  Frame-format: ESF,  clock: slave,  loopback: none]{lang="EN-US"}

[  Alarm:  ]{lang="DE"}[AIS  LFA  Red]{lang="EN-US"}

[  Error:  ]{lang="DE"}[0 Bit Error,  0 Fer,  0 OOF]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display controller cpos t1]{lang="EN-US"}]{#struct_0_x1849_14381_243041416}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1445094065}[[主要字段]{style="font-family:黑体"}]{#struct_0_x1849_14381_202782384}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1849_14381_1878164524}

[[Cpos2/4/0 current state]{lang="EN-US"}]{#struct_0_x1849_14381_1401882450}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448958}[接口当前的物理状态]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1849_14381_x488230112}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1849_14381_x487836896}

[[Lower order path]{lang="EN-US"}]{#struct_0_x1849_14381_1959004245}

[[低阶通道的告警和错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_722031273}

[[Tx]{lang="NL-BE"}[Flag]{lang="EN-US"}]{#struct_0_x1849_14381_1078247050}[: ]{lang="NL-BE"}

[[发送的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_1078312586}

[[Rx]{lang="NL-BE"}[Flag]{lang="EN-US"}]{#struct_0_x1849_14381_1078181514}[: ]{lang="NL-BE"}

[[接收的开销字节]{style="font-family:宋体"}]{#struct_0_x1849_14381_1077460618}[]{#_Toc281733540}

[[当收到的]{style="font-family:宋体"}[J2]{lang="EN-US"}]{#struct_0_x1849_14381_1077984905}[为不可见字符时，显示为：]{style="font-family:宋体"}[RxFlag: J2: unknow]{lang="EN-US"}

[[Alarm]{lang="EN-US"}]{#struct_0_x1849_14381_1382941486}

[[对应支路的告警统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x398202130}

[[Error]{lang="EN-US"}]{#struct_0_x1849_14381_x1756645566}

[[错误统计]{style="font-family:宋体"}]{#struct_0_x1849_14381_x952377890}

[[CT1  1 (1-1-1-1) is down]{lang="EN-US"}]{#struct_0_x1849_14381_1590411764}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_1273619339}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[当前的物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[，]{style="font-family:宋体"}[1-1-1-1]{lang="EN-US"}[依次表示此]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道所属的]{style="font-family:宋体"}[VC-3]{lang="EN-US"}[编号、]{style="font-family:宋体"}[TUG-3]{lang="EN-US"}[编号、]{style="font-family:宋体"}[TUG-2]{lang="EN-US"}[编号和]{style="font-family:宋体"}[TU-11]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[Frame-format: ESF,  clock: slave,  loopback: nonet]{lang="EN-US"}]{#struct_0_x1849_14381_x693036209}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_x1756711102}[通道的物理层信息：帧格式为]{style="font-family:宋体"}[ESF]{lang="EN-US"}[、从时钟模式、没有使能环回]{style="font-family:宋体"}

[ ]{lang="DE"}

::: {#1374262046 .myid}
[]{#_Toc404783850}[]{#struct_0_x1849_14381_x1254248921}[]{#_Toc255917502}[]{#_Toc194725118}[]{#_Toc171825211}

**CPOS接口 \-- CPOS接口配置命令 \-- display controller cpos t3**

------------------------------------------------------------------------

[**[display controller cpos t3]{lang="EN-US"}**]{#struct_0_x1849_14381_x2003667302}[命令用来显示指定]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1093942027}[]{#_Toc171825212}

[**[display controller]{lang="EN-US"}**[ **cpos** *cpos-number* **t3** *t3-number*]{lang="EN-US"}]{#struct_0_x1849_14381_x1756776638}[]{#_Toc171825213}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1105766478}[]{#_Toc171825214}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1808003898}[]{#_Toc171825215}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2060941551}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1393247592}

[[network-operator]{lang="EN-US"}]{#struct_0_x1849_14381_210992850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1315718408}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1849_14381_x811566746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_468761528}[]{#_Toc171825218}

[*[cpos-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1756842174}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口[]{#_Toc171825219}编号。]{style="font-family:宋体"}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1994459996}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}[]{#_Toc171825220}

[]{#struct_0_x1849_14381_x685621424}[]{#_Toc171825221}[【使用指导】]{style="font-family:黑体"}

[[与]{style="font-family:宋体"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_2102770116}[命令相比，本命令可以显示对应的低阶通道的错误和告警信息以及]{style="font-family:宋体"}[T3]{lang="EN-US"}[帧的错误和告警信息[]{#_Toc171825222}，具体告警如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-4]{lang="EN-US"}](?1374262063#_Ref194484615)[所示。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1840125769}[]{#_Toc171825223}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_976414184}[查看]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[1]{lang="EN-US"}[号]{style="font-family:
宋体"}[T3]{lang="EN-US"}[通道的状态信息，状态信息含义如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-5]{lang="EN-US"}](?1374262063#_Ref194484623)[所示[]{#_Toc171825224}。]{style="font-family:
宋体"}

[]{#struct_0_x1849_14381_x1756907710}[]{#_Toc171825245}[\<Sysname\> display controller cpos 2/4/0 t3 1]{lang="EN-US"}

[Cpos2/4/0 current state: UP]{lang="EN-US"}

[Description: Cpos2/4/0 Interface]{lang="EN-US"}

[T3 1: down]{lang="EN-US"}

[  Frame-format: C-bit ,Clock: slave ,Loopback: none]{lang="EN-US"}

[  Alarm: NONE]{lang="EN-US"}

[  Error: 0 FERR, 0 LCV, 0 PERR, 0 FEBE, 0 PARITY_P, 0 HCS]{lang="EN-US"}
:::

::: {#-1027784191 .myid}
[]{#_Toc404783851}[]{#struct_0_x1849_14381_151472174}[]{#_Toc255917503}[]{#_Toc136937624}[]{#_Toc171825247}[]{#_Toc171825289}[]{#_Toc194808739}[]{#_Toc195414771}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 channel-set**

------------------------------------------------------------------------

[**[e1 channel-set]{lang="EN-US"}**]{#struct_0_x1849_14381_792104996}[命令用来对]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时隙进行捆绑。]{style="font-family:宋体"}

[**[undo e1 channel-set]{lang="EN-US"}**]{#struct_0_x1849_14381_x546491441}[命令用来取消指定的捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1625061908}

[**[e1]{lang="EN-US"}**[ *e1-number* **channel-set** *set-number* **timeslot-list** *range*]{lang="EN-US"}]{#struct_0_x1849_14381_1335581049}

[**[undo e1]{lang="EN-US"}**[ *e1-number* **channel-set** *set-number*]{lang="EN-US"}]{#struct_0_x1849_14381_x1302356007}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1764174006}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_813377048}[不进行通道化。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1755924670}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_3430340}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x520813285}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x2115346508}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x781245912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x962229425}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_773124195}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[set-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1691515204}[：捆绑集的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}***[ range]{lang="EN-US"}*]{#struct_0_x1849_14381_1875846783}[：用于捆绑的时隙列表，时隙编号的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[。在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[-*number2*]{lang="EN-US"}[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[，]{style="font-family:宋体"}*[number2]{lang="EN-US"}*[-*number3*]{lang="EN-US"}[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1755990206}

[[当]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x516473471}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[应用在通道化模式（]{style="font-family:宋体"}[Channelized]{lang="EN-US"}[）时，除时隙]{style="font-family:宋体"}[0]{lang="EN-US"}[用于同步外，其它]{style="font-family:宋体"}[31]{lang="EN-US"}[个时隙可任意捆绑为一个或多个串口。]{style="font-family:宋体"}

[[捆绑形成的串口编号形式为"接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1849_14381_x2053868334}[通道号]{style="font-family:宋体"}[:channel-set]{lang="EN-US"}[号"。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1813181746}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1932955759}[对]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[63]{lang="EN-US"}[进行捆绑。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x2073637646}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 63 channel-set 1 timeslot-list 1-31]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1723680866}[进入捆绑后形成的串口的视图。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0\] quit]{lang="EN-US"}]{#struct_0_x1849_14381_x1756448957}

[\[Sysname\] interface serial 2/4/0/63:1]{lang="EN-US"}

[\[Sysname-Serial2/4/0/63:1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2081581383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[e1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_x747118681}
:::

::: {#-739348982 .myid}
[]{#_Toc404783852}[]{#struct_0_x1849_14381_x957958758}[]{#_Toc255917504}[]{#_Toc136937625}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 clock**

------------------------------------------------------------------------

[**[e1 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x1067608125}[命令用来设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo e1 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_263566721}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2131973367}

[**[e1]{lang="EN-US"}**[ *e1-number* **clock** { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1849_14381_1285203240}

[**[undo e1]{lang="EN-US"}**[ *e1-number* **clock**]{lang="EN-US"}]{#struct_0_x1849_14381_839058205}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1756514493}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x1412709177}[通道的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_221250147}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1681818669}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1624560023}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x707644610}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1573831696}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1880899732}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1334105217}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_x1756580029}[：设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_x413583214}[：设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1521906862}

[[可以为不同的]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_x1849_14381_1063668104}[通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。]{style="font-family:宋体"}

[[需要注意的是，同一]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1246211762}[物理接口的不同]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的时钟模式是相互独立的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1467922613}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x79021092}[设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x816241280}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 1 clock master]{lang="EN-US"}
:::

::: {#-528596874 .myid}
[]{#_Toc136937626}[]{#_Toc404783853}[]{#struct_0_x1849_14381_x295805608}[]{#_Toc255917505}[]{#_Toc168471851}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 flag**

------------------------------------------------------------------------

[**[e1 flag]{lang="EN-US"}**]{#struct_0_x1849_14381_x1756645565}[命令用来设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道开销。]{style="font-family:宋体"}

[**[undo e1 flag]{lang="EN-US"}**]{#struct_0_x1849_14381_x549093363}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_168336332}

[**[e1]{lang="EN-US"}[ ]{lang="EN-US"}***[e1-number]{lang="EN-US"}*[ **flag** **c2** *c2-value*]{lang="EN-US"}]{#struct_0_x1849_14381_1487274743}

[**[undo e1 ]{lang="PT-BR"}**]{#struct_0_x1849_14381_x2142156252}*[e1-number]{lang="PT-BR"}*[ **flag** **c2**]{lang="PT-BR"}

[**[e1]{lang="PT-BR"}**]{#struct_0_x1849_14381_x714551695}**[ ]{lang="PT-BR"}***[e1-number]{lang="PT-BR"}*[ **flag** **j2** { **sdh** \| **sonet** } *j2-string*]{lang="PT-BR"}

[**[undo e1 ]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1703715351}*[e1-number]{lang="PT-BR"}*[ **flag** **j2** { **sdh** \| **sonet** }]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1827504868}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x1756711101}[取值为]{style="font-family:宋体"}[02]{lang="EN-US"}[（十六进制），]{style="font-family:宋体"}**[j2]{lang="EN-US"}**[循环发送空字符""。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1902191732}

[[CPOS]{lang="DA"}]{#struct_0_x1849_14381_1808048080}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1701103802}

[[network-admin]{lang="DA"}]{#struct_0_x1849_14381_x362565841}

[[mdc-admin]{lang="DA"}]{#struct_0_x1849_14381_2052352048}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x712364365}

[*[e1-number]{lang="DA"}*]{#struct_0_x1849_14381_1120445633}[：]{style="font-family:宋体"}[CPOS]{lang="DA"}[接口的]{style="font-family:
宋体"}[E1]{lang="DA"}[通道号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[63]{lang="DA"}[。]{style="font-family:宋体"}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x1789995636}[：低阶通道信号标签字节。]{style="font-family:宋体"}

[*[c2-value]{lang="EN-US"}*]{#struct_0_x1849_14381_x1756776637}[：]{style="font-family:宋体"}[c2]{lang="EN-US"}[字节的开销的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。协议不支持该值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j2]{lang="EN-US"}**]{#struct_0_x1849_14381_346251591}[：低阶通道踪迹字节]{style="font-family:宋体"}[J2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1849_14381_157717175}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[格式的跟踪字节。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1849_14381_x908279729}[：]{style="font-family:宋体"}[SONET]{lang="EN-US"}[格式的跟踪字节。]{style="font-family:宋体"}

[*[j2-string]{lang="EN-US"}*]{#struct_0_x1849_14381_1122634289}[：踪迹字节，对于]{style="font-family:宋体"}[SDH]{lang="EN-US"}[格式取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符，对于]{style="font-family:宋体"}[SONET]{lang="EN-US"}[格式取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1579311418}

[[\# CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1897676659}[接口下配置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[c2]{lang="EN-US"}[开销为]{style="font-family:宋体"}[0x7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_39097504}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 3 flag c2 7]{lang="PT-BR"}
:::

::: {#-1552622764 .myid}
[]{#_Toc404783854}[]{#struct_0_x1849_14381_x1756842173}[]{#_Toc255917506}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 frame-format**

------------------------------------------------------------------------

[**[e1 frame-format]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1591175469}[命令用来设置]{style="font-family:宋体"}[E1]{lang="PT-BR"}[通道的帧格式。]{style="font-family:宋体"}

[**[undo e1 frame-format]{lang="PT-BR"}**]{#struct_0_x1849_14381_x519969997}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x720370875}

[**[e1 ]{lang="PT-BR"}**]{#struct_0_x1849_14381_1282277647}*[e1-number]{lang="PT-BR"}***[ frame-format ]{lang="PT-BR"}**[{ **crc4** \| **no-crc4** }]{lang="PT-BR"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x1849_14381_1342297481}[ **e1** *e1-number* **frame-format**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1554316553}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x157193836}[通道的帧格式为]{style="font-family:宋体"}**[no-crc4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x814181324}

[[CPOS]{lang="PT-BR"}]{#struct_0_x1849_14381_x1756907709}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1361391291}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_2128660611}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x787404894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1777133730}

[*[e1-number]{lang="PT-BR"}*]{#struct_0_x1849_14381_x99453240}[：]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口]{style="font-family:宋体"}[的]{style="font-family:宋体"}[E1]{lang="PT-BR"}[通道号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[63]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[crc4]{lang="PT-BR"}**]{#struct_0_x1849_14381_x553829168}[：]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[。]{style="font-family:宋体"}

[**[no-crc4]{lang="PT-BR"}**]{#struct_0_x1849_14381_337847111}[：]{style="font-family:宋体"}[帧格式为]{style="font-family:宋体"}[no-CRC4]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_569227373}

[[\# ]{lang="PT-BR"}]{#struct_0_x1849_14381_x1755924669}[设置]{style="font-family:宋体"}[E1]{lang="PT-BR"}[通道]{style="font-family:宋体"}[1]{lang="PT-BR"}[使用带]{style="font-family:宋体"}[CRC4]{lang="PT-BR"}[检验的帧格式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1849_14381_1213349457}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 1 frame-format crc4]{lang="EN-US"}
:::

::: {#295073978 .myid}
[]{#_Toc404783855}[]{#struct_0_x1849_14381_50738562}[]{#_Toc255917507}[]{#_Toc136937627}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 loopback**

------------------------------------------------------------------------

[**[e1 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x628236192}[命令用来设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道的环回模式。]{style="font-family:宋体"}

[**[undo e1 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_1323702136}[命令用来取消环回。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1303962440}

[**[e1]{lang="EN-US"}**[ *e1-number* **loopback** { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1849_14381_x499997295}

[**[undo e1]{lang="EN-US"}**[ *e1-number* **loopback**]{lang="EN-US"}]{#struct_0_x1849_14381_x285041874}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1755990205}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_1049610470}[通道不进行任何形式的环回。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_308626317}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1889207792}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1172830511}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_666869388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_688558825}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x424627125}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x972583683}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1849_14381_x190365013}[：使能]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1849_14381_x1599437930}[：使能]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对外载荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1849_14381_1017500631}[：使能]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道对外远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1198785665}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x1357859293}[通道提供丰富的环回功能，可用于不同层次的测试。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对内自环模式下，发端的数据直接被环回到收端。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1951037618}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对外载荷环回模式下，收端接收的数据经过]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2057193889}[E1]{lang="EN-US"}[成帧器，生成载荷后再进行环回。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对外远端环回模式下，收端接收的数据不经过]{style="font-family:宋体"}]{#struct_0_x1849_14381_1368811641}[E1]{lang="EN-US"}[成帧器，未生成载荷即进行环回。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1231931235}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x190430549}[设置]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[进行对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_379332137}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 1 loopback payload]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1730815189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos e1]{lang="EN-US"}**]{#struct_0_x1849_14381_1651365821}
:::

::: {#-539090833 .myid}
[]{#_Toc404783856}[]{#struct_0_x1849_14381_x1726292438}[]{#_Toc255917508}[]{#_Toc136937628}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 shutdown**

------------------------------------------------------------------------

[**[e1 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1979799387}[命令用来关闭]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo e1 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1655839531}[命令用来打开]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1435915336}

[**[e1 ]{lang="EN-US"}***[e1-number ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x190496085}

[**[undo e1 ]{lang="EN-US"}***[e1-number ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x52687005}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x512032296}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x251860869}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x698092789}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_2112514}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1938110602}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1161814227}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1883710770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190561621}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x777211543}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x682914499}

[[关闭]{style="font-family:宋体"}[E1]{lang="EN-US"}]{#struct_0_x1849_14381_x887154751}[通道后，如果有捆绑形成的串口，则串口也被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1365698864}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1977206801}[关闭]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1787563797}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 1 shutdown]{lang="EN-US"}
:::

::: {#-982229301 .myid}
[]{#_Toc404783857}[]{#struct_0_x1849_14381_x334161083}[]{#_Toc255917509}[]{#_Toc136937629}

**CPOS接口 \-- CPOS接口配置命令 \-- e1 unframed**

------------------------------------------------------------------------

[**[e1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_x190627157}[命令用来设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[工作在非成帧模式。]{style="font-family:宋体"}

[**[undo e1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_x415196411}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x594166959}

[**[e1]{lang="EN-US"}**[ *e1-number* **unframed**]{lang="EN-US"}]{#struct_0_x1849_14381_1042681554}

[**[undo e1]{lang="EN-US"}**[ *e1-number* **unframed**]{lang="EN-US"}]{#struct_0_x1849_14381_x851462102}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2038888109}

[[E1]{lang="EN-US"}]{#struct_0_x1849_14381_1169671547}[工作在成帧模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_197642273}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1361518010}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190692693}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_769539384}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1235230472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_509280937}

[*[e1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1081725749}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1216659026}

[[在目前的实现中，]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x964610786}[通道化生成的]{style="font-family:宋体"}[E1]{lang="EN-US"}[支持净通道（]{style="font-family:宋体"}[clear channel]{lang="EN-US"}[，又称为非成帧模式，]{style="font-family:宋体"}[unframed]{lang="EN-US"}[）和通道（]{style="font-family:宋体"}[channelized]{lang="EN-US"}[，又称为成帧模式）两种工作模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非成帧模式下，]{style="font-family:宋体"}]{#struct_0_x1849_14381_x2142756466}[E1]{lang="EN-US"}[通道不分时隙，形成一个速率为]{style="font-family:宋体"}[2.048Mbps]{lang="EN-US"}[的串口，名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在成帧模式下，]{style="font-family:宋体"}]{#struct_0_x1849_14381_1606787291}[E1]{lang="EN-US"}[通道除时隙]{style="font-family:宋体"}[0]{lang="EN-US"}[以外的]{style="font-family:宋体"}[31]{lang="EN-US"}[个时隙可以任意捆绑为串口使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190758229}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1945140878}[将]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的第]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[E1]{lang="EN-US"}[通道设置为非成帧模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1219057443}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e1 3 unframed]{lang="EN-US"}
:::

::::: {#-735023606 .myid}
[]{#_Toc404783858}[]{#struct_0_x1849_14381_459700676}

**CPOS接口 \-- CPOS接口配置命令 \-- e3 clock**

------------------------------------------------------------------------

[**[e3 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_2078813405}[命令用来配置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo e3 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x1020027879}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2090418706}

[**[e3]{lang="EN-US"}**[ *e3-number* **clock** { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1849_14381_1226248389}

[**[undo e3]{lang="EN-US"}**[ *e3-number* **clock**]{lang="EN-US"}]{#struct_0_x1849_14381_x190823765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_407029974}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_x2000222505}[通道的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x162796667}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1748294919}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1206088108}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1501706046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_201698637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1130225802}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x189840725}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_1254573424}[：设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_1748551323}[：设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_30455759}

[[可以为不同的]{style="font-family:宋体"}[E3]{lang="EN-US"}]{#struct_0_x1849_14381_636933643}[通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image003.png){#图片 4 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1140395705}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[在同一]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_624410077}[CPOS]{lang="EN-US"}[物理接口的不同]{style="font-family:KaiTi_GB2312"}[E3]{lang="EN-US"}[通道的时钟模式是相互独立。]{style="font-family:KaiTi_GB2312"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[建议将全局下]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_2000561649}**[clock]{lang="EN-US"}**[时钟模式和]{style="font-family:KaiTi_GB2312"}[E3]{lang="EN-US"}[通道的时钟模式配置一致。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1023904811}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x189906261}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1234644607}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e3 1 clock master]{lang="EN-US"}
:::::

::: {#-1213366365 .myid}
[]{#_Toc404783859}[]{#struct_0_x1849_14381_x1083096467}

**CPOS接口 \-- CPOS接口配置命令 \-- e3 framed**

------------------------------------------------------------------------

[**[e3 framed]{lang="EN-US"}**]{#struct_0_x1849_14381_244630978}[命令用来创建成帧模式下，]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对应的串口。]{style="font-family:宋体"}

[**[undo e3 framed]{lang="EN-US"}**]{#struct_0_x1849_14381_1680429101}[命令用来删除该串口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2001159856}

[**[e3]{lang="PT-BR"}**]{#struct_0_x1849_14381_1784033398}[ *e3-number* **framed**]{lang="PT-BR"}

[**[undo e3]{lang="PT-BR"}**]{#struct_0_x1849_14381_x190365012}[ *e3-number* **framed**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1599503466}

[[未创建串口。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1635013071}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x667652628}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x211416391}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_604290010}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1493182200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1784647848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1253724732}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x190430548}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_379397673}

[[在将]{style="font-family:宋体"}[E3]{lang="EN-US"}]{#struct_0_x1849_14381_x1380239274}[通道设置为成帧方式后，系统会自动创建一个串口，名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1809102377}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x983614824}[将]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的第]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道设置为成帧模式，并创建对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x150202474}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e3 3 framed]{lang="EN-US"}
:::

::: {#437549242 .myid}
[]{#_Toc404783860}[]{#struct_0_x1849_14381_x1943140182}[]{#_Toc255917511}[]{#_Toc194725122}[]{#_Toc171825294}

**CPOS接口 \-- CPOS接口配置命令 \-- e3 loopback**

------------------------------------------------------------------------

[**[e3 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x300824372}[命令用来配置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的环回模式。]{style="font-family:宋体"}

[**[undo e3 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x190496084}[命令用来取消环回。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x52621469}

[**[e3]{lang="EN-US"}**[ *e3-number* **loopback** { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1849_14381_x1703596478}

[**[undo e3]{lang="EN-US"}**[ *e3-number* **loopback**]{lang="EN-US"}]{#struct_0_x1849_14381_x1510582600}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1211612588}

[[未进行任何形式的环回。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1426070453}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_456995811}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1901172904}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x212059499}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x190561620}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x777277079}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1602570462}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1459477692}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1849_14381_1236343048}[：使能]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1849_14381_x437417515}[：使能]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对外载荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1849_14381_x923695935}[：使能]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对外远端环回，目前暂不支持该命令。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1359455174}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_x1068835453}[通道提供丰富的环回功能，可用于不同层次的测试。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对内自环模式下，发端的数据直接被环回到收端。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x190627156}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对外载荷环回模式下，收端接收的数据经过]{style="font-family:宋体"}]{#struct_0_x1849_14381_x415261947}[E3]{lang="EN-US"}[成帧器，生成载荷后再进行环回。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在对外远端环回模式下，收端接收的数据不经过]{style="font-family:宋体"}]{#struct_0_x1849_14381_x504668836}[E3]{lang="EN-US"}[成帧器，未生成载荷即进行环回。]{style="font-family:宋体"}

[[相关配置可参考命令]{style="font-family:宋体"}**[display controller cpos e3]{lang="EN-US"}**]{#struct_0_x1849_14381_x1665427846}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_486052749}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_259485472}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[进行对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x186966739}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e3 1 loopback payload]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1343934844}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos e3]{lang="EN-US"}**]{#struct_0_x1849_14381_x190692692}
:::

::: {#585217328 .myid}
[]{#_Toc171825295}[]{#_Toc404783861}[]{#struct_0_x1849_14381_769604920}[]{#_Toc255917512}[]{#_Toc194725123}

**CPOS接口 \-- CPOS接口配置命令 \-- e3 national-bit**

------------------------------------------------------------------------

[**[e3 national-bit]{lang="EN-US"}**]{#struct_0_x1849_14381_990586291}[命令用来设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的]{style="font-family:宋体"}[national bit]{lang="EN-US"}[通信码。]{style="font-family:宋体"}

[**[undo e3 national-bit]{lang="EN-US"}**]{#struct_0_x1849_14381_322787651}[命令用来恢复]{style="font-family:宋体"}[national bit]{lang="EN-US"}[为缺省状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_640368831}

[**[e3]{lang="EN-US"}**[ *e3-number* **national-bit** { **0** \| **1** }]{lang="EN-US"}]{#struct_0_x1849_14381_2130618904}

[**[undo e3]{lang="EN-US"}**[ *e3-number* **national-bit**]{lang="EN-US"}]{#struct_0_x1849_14381_1425845684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1765528847}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_1694412364}[通道的]{style="font-family:宋体"}[national bit]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190758228}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1945075342}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1964565061}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_713400940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x809161774}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2132174197}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_536098260}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[0]{lang="EN-US"}**]{#struct_0_x1849_14381_x1749603593}[：设置]{style="font-family:宋体"}[national-bit]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[1]{lang="EN-US"}**]{#struct_0_x1849_14381_2034119043}[：设置]{style="font-family:宋体"}[national-bit]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190823764}

[[national-bit]{lang="EN-US"}]{#struct_0_x1849_14381_406964438}[是一种]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道内使用的通信码。当用于国内通信时设置为]{style="font-family:宋体"}[0]{lang="EN-US"}[，用于国际通信时设置为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1150489075}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1889424583}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道的]{style="font-family:宋体"}[national-bit]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x387298974}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e3 1 national-bit 1]{lang="EN-US"}
:::

::: {#-387440529 .myid}
[]{#_Toc404783862}[]{#struct_0_x1849_14381_2056232809}[]{#_Toc255917513}[]{#_Toc194725120}

**CPOS接口 \-- CPOS接口配置命令 \-- e3 shutdown**

------------------------------------------------------------------------

[**[e3 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x1701761256}[命令用来关闭]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo e3 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1965401603}[命令用来打开]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x206321693}

[**[e3]{lang="EN-US"}**[ *e3-number* **shutdown**]{lang="EN-US"}]{#struct_0_x1849_14381_x189840724}

[**[undo e3]{lang="EN-US"}**[ *e3-number* **shutdown**]{lang="EN-US"}]{#struct_0_x1849_14381_1254507888}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1429468217}

[[E3]{lang="EN-US"}]{#struct_0_x1849_14381_1815402547}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x163177625}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1743212796}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_473324250}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_467003791}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1055483657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x189906260}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1234579071}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1509931856}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x2125916108}[关闭]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x685348179}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] e3 1 shutdown]{lang="EN-US"}
:::

::: {#-1620789979 .myid}
[]{#_Toc404783863}[]{#struct_0_x1849_14381_213295049}[]{#_Toc255917514}

**CPOS接口 \-- CPOS接口配置命令 \-- fe3**

------------------------------------------------------------------------

[**[fe3]{lang="EN-US"}**]{#struct_0_x1849_14381_x244447416}[命令用来配置指定的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道工作在]{style="font-family:宋体"}[FE3]{lang="EN-US"}[模式，并配置]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式或子速率。]{style="font-family:宋体"}

[**[undo fe3]{lang="EN-US"}**]{#struct_0_x1849_14381_x720909754}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190365015}

[**[fe3]{lang="EN-US"}**[ *e3-number* { **dsu-mode** { **0** \| **1** } \| **subrate** *sub-number* }]{lang="EN-US"}]{#struct_0_x1849_14381_x1599306858}

[**[undo fe3]{lang="EN-US"}**[ *e3-number* { **dsu-mode** \| **subrate** }]{lang="EN-US"}]{#struct_0_x1849_14381_1555898415}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2117191905}

[[DSU]{lang="EN-US"}]{#struct_0_x1849_14381_x1425570904}[模式为]{style="font-family:宋体"}[1]{lang="EN-US"}[，即]{style="font-family:宋体"}[Kentrox]{lang="EN-US"}[模式；子速率为]{style="font-family:宋体"}[34010kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x372709290}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1418979640}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1642908609}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_189575322}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x190430551}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_379856424}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1708335871}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[dsu-mode]{lang="EN-US"}**]{#struct_0_x1849_14381_x1798870252}[：设置]{style="font-family:宋体"}[FE3]{lang="EN-US"}[的]{style="font-family:宋体"}[DSU]{lang="EN-US"}[（]{style="font-family:宋体"}[Data Service Units]{lang="EN-US"}[）模式，目前支持的]{style="font-family:宋体"}[FE3 DSU]{lang="EN-US"}[模式，如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[0]{lang="EN-US"}**]{#struct_0_x1849_14381_x1510639533}[：]{lang="EN-US" style="font-family:宋体"}[Digital Link]{lang="EN-US"}[，子速率范围为]{lang="EN-US" style="font-family:宋体"}[358kbps]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[34010kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[95]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[358kbps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[1]{lang="EN-US"}**]{#struct_0_x1849_14381_x1068534609}[：]{lang="EN-US" style="font-family:宋体"}[Kentrox]{lang="EN-US"}[，子速率范围为]{lang="EN-US" style="font-family:宋体"}[500kbps]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[24500kbps]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[34010kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[50]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[500kbps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[subrate]{lang="EN-US"}***[ sub-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1138859342}[：设置]{style="font-family:宋体"}[FE3]{lang="EN-US"}[的子速率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[34010]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_531484570}

[[FE3]{lang="EN-US"}]{#struct_0_x1849_14381_x1030205302}[（]{style="font-family:宋体"}[Fractional E3]{lang="EN-US"}[，或称]{style="font-family:宋体"}[Subrate E3]{lang="EN-US"}[）是]{style="font-family:宋体"}[E3]{lang="EN-US"}[的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用]{style="font-family:宋体"}**[fe3]{lang="EN-US"}**[命令可以使我们的设备和其他厂家设备的]{style="font-family:宋体"}[FE3 DSU]{lang="EN-US"}[模式兼容，实现互通。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1849_14381_x190496087}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[fe3 subrate]{lang="EN-US"}**]{#struct_0_x1849_14381_x52555933}[设置的速率值是一个大概值。由于通过]{lang="EN-US" style="font-family:宋体"}**[fe3 dsu-mode]{lang="EN-US"}**[命令配置的各]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[的子速率值是离散的，因此，当再通过]{lang="EN-US" style="font-family:宋体"}**[fe3 subrate]{lang="EN-US"}**[命令指定子速率后，]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[接口会根据当前配置的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式计算出与这个指定子速率最匹配的精确速率（精确到]{lang="EN-US" style="font-family:宋体"}[bps]{lang="EN-US"}[），并设置硬件电路支持该速率。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[display interface serial ]{lang="EN-US"}***[interface-number]{lang="EN-US"}*[:**0**]{lang="EN-US"}]{#struct_0_x1849_14381_1128667820}[命令可以查看]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（]{lang="EN-US" style="font-family:宋体"}[34368kbps]{lang="EN-US"}[）为]{lang="EN-US" style="font-family:宋体"}[E3]{lang="EN-US"}[线路的实际速率（含开销位在内）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x839991551}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1643540058}[设置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式]{style="font-family:宋体"}[1]{lang="EN-US"}[，速率]{style="font-family:宋体"}[500kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x478395603}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] fe3 1 dsu-mode 1]{lang="FR"}

[\[Sysname-Cpos2/4/0\] fe3 1 subrate 500]{lang="EN-US"}
:::

::: {#2006314719 .myid}
[]{#_Toc404783864}[]{#struct_0_x1849_14381_x541958161}[]{#_Toc255917515}[]{#_Toc136937630}

**CPOS接口 \-- CPOS接口配置命令 \-- flag**

------------------------------------------------------------------------

[**[flag]{lang="EN-US"}**]{#struct_0_x1849_14381_1493415560}[命令用来设置]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[帧的开销字节。]{style="font-family:宋体"}

[**[undo flag]{lang="EN-US"}**]{#struct_0_x1849_14381_x190561623}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x777080471}

[**[flag ]{lang="EN-US"}**[{ **c2** *path-number c2-value* \| **s1** *s1-value \|* **s1s0** *path-number s1s0-value* }]{lang="EN-US"}]{#struct_0_x1849_14381_113574297}

[**[undo]{lang="EN-US"}**[ **flag** { **c2** *path-number* \| **s1 \| s1s0** *path-number* }]{lang="EN-US"}]{#struct_0_x1849_14381_x1131020809}

[**[flag]{lang="EN-US"}**[ { **j0** \| **j1** *path-number* } { **sdh** \| **sonet** } *flag-value*]{lang="EN-US"}]{#struct_0_x1849_14381_x878202848}

[**[undo flag ]{lang="EN-US"}**[{ **j0** \| **j1** *path-number* } { **sdh** \| **sonet** }]{lang="EN-US"}]{#struct_0_x1849_14381_206105359}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_170304789}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x2076081741}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[s1]{lang="EN-US"}**]{#struct_0_x1849_14381_696567780}[取值为]{style="font-family:宋体"}[0x0f]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[s1s0]{lang="EN-US"}**]{#struct_0_x1849_14381_x190627159}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[，]{style="font-family:宋体"}**[s1s0]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j0]{lang="EN-US"}**]{#struct_0_x1849_14381_x415589627}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x01]{lang="EN-US"}[，]{style="font-family:宋体"}**[j0]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节空字符""。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_542900921}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[64]{lang="EN-US"}[字节空字符""，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节空字符""。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_241515598}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1823954460}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x843751345}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_443057672}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_222893831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1548170515}

[**[c2]{lang="EN-US"}***[ path-number c2-value]{lang="EN-US"}*]{#struct_0_x1849_14381_x190692695}[：]{style="font-family:宋体"}*[path-number]{lang="EN-US"}*[通道编号、]{style="font-family:宋体"}*[c2-value]{lang="EN-US"}*[信号标记字节，取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[s1]{lang="EN-US"}**[ *s1-value*]{lang="EN-US"}]{#struct_0_x1849_14381_769670456}[：同步状态字节。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s1s0]{lang="EN-US"}***[ path-number s1s0-value]{lang="EN-US"}*]{#struct_0_x1849_14381_523702475}[：]{style="font-family:宋体"}*[path-number]{lang="EN-US"}*[通道编号、]{style="font-family:宋体"}*[s1s0-value]{lang="EN-US"}*[指示]{style="font-family:宋体"}[AU]{lang="EN-US"}[，]{style="font-family:宋体"}[TU]{lang="EN-US"}[类型。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[j0]{lang="EN-US"}***[ flag-value]{lang="EN-US"}*]{#struct_0_x1849_14381_405680550}[：再生段踪迹字节，属于段开销字节（]{style="font-family:宋体"}[Section Overhead]{lang="EN-US"}[），用于检测两个端口之间的连接在段层次上的连续性。]{style="font-family:宋体"}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}***[ path-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x957102177}[：通道踪迹字节，属于高阶通道开销字节，用于检测两个端口之间的连接在通道层次上的连续性。]{style="font-family:宋体"}[]{#_Hlt12766582}[SDH]{lang="EN-US"}[帧格式下]{style="font-family:
宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[SONET]{lang="EN-US"}[帧格式下]{style="font-family:宋体"}*[flag-value]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1849_14381_x1434384181}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Digital Hierarchy]{lang="EN-US"}[，同步数字系列）。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1849_14381_x1606860453}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[（]{style="font-family:宋体"}[Synchronous Optical Network]{lang="EN-US"}[，同步光网络）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x716625512}

[[SONET/SDH]{lang="EN-US"}]{#struct_0_x1849_14381_x675532624}[帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能（]{style="font-family:宋体"}[OAM]{lang="EN-US"}[，]{style="font-family:宋体"}[Operation and Maintenance]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j0]{lang="EN-US"}**]{#struct_0_x1849_14381_x190758231}[、]{style="font-family:
宋体"}**[j1]{lang="EN-US"}**[和]{style="font-family:宋体"}**[c2]{lang="EN-US"}**[主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j0]{lang="EN-US"}**]{#struct_0_x1849_14381_x1945665165}[属于段开销字节，用于检测两个接口之间的连接在段层次上的连续性。]{style="font-family:
宋体"}**[j1]{lang="EN-US"}**[和]{style="font-family:宋体"}**[c2]{lang="EN-US"}**[属于高阶通道开销字节，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[用于检测两个接口之间的连接在通道层次上的连续性，]{style="font-family:宋体"}**[c2]{lang="EN-US"}**[用来指示]{style="font-family:宋体"}[VC]{lang="EN-US"}[帧的复接结构和信息净负荷的性质。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[S1]{lang="EN-US"}**]{#struct_0_x1849_14381_1237313877}[是同步状态字节，不同的值表示]{style="font-family:
宋体"}[ITU-T]{lang="EN-US"}[的不同时钟质量级别，使设备能据此判定接收的时钟信号的质量以此决定是否切换时钟源即切换到较高质量的时钟源上。]{style="font-family:
宋体"}[值越小，时钟精度越高。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[S1S0]{lang="EN-US"}**]{#struct_0_x1849_14381_1882229208}[是]{lang="EN-US" style="font-family:宋体"}[H1]{lang="EN-US"}[字节中的两个比特，在]{lang="EN-US" style="font-family:宋体"}[ITU]{lang="EN-US"}[标准里用于指示]{lang="EN-US" style="font-family:宋体"}[AU-n/TU-n]{lang="EN-US"}[的类型。当处理]{lang="EN-US" style="font-family:宋体"}[AU-4]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[AU-3]{lang="EN-US"}[，]{lang="EN-US" style="font-family:宋体"}[TU-3]{lang="EN-US"}[时要求必须设置为]{lang="EN-US" style="font-family:宋体"}[2]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1228228471}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_26728699}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的再生段跟踪字节]{style="font-family:宋体"}**[j0]{lang="EN-US"}**[为字符串]{style="font-family:宋体"}[aa]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1783434094}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] flag j0 sdh aa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_442780002}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_x190823767}
:::

::: {#-788368366 .myid}
[]{#_Toc404783865}[]{#struct_0_x1849_14381_407161046}[]{#_Toc255917516}[]{#_Toc194725126}

**CPOS接口 \-- CPOS接口配置命令 \-- flag vc-3**

------------------------------------------------------------------------

[**[flag vc-3]{lang="EN-US"}**]{#struct_0_x1849_14381_x70115128}[命令用来设置]{style="font-family:宋体"}[vc-3]{lang="EN-US"}[帧的开销字节。]{style="font-family:宋体"}

[**[undo flag vc-3]{lang="EN-US"}**]{#struct_0_x1849_14381_x1597151887}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1437165005}

[**[flag]{lang="EN-US"}**[ **vc-3** ]{lang="EN-US"}*[path-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **c2** ]{lang="EN-US"}*[c2-value ]{lang="EN-US"}*[\| **j1** { **sdh** ]{lang="EN-US"}*[sdh-string ]{lang="EN-US"}*[\| **sonet** ]{lang="EN-US"}*[sonet-string]{lang="EN-US"}***[ ]{lang="EN-US"}**[} \| **s1s0** ]{lang="EN-US"}*[s1s0-value ]{lang="EN-US"}*[}]{lang="EN-US"}]{#struct_0_x1849_14381_1023069685}

[**[undo flag vc-3 ]{lang="EN-US"}***[path-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **c2** \| **j1** { **sdh** \| **sonet** } \| **s1s0** }]{lang="EN-US"}]{#struct_0_x1849_14381_x616805045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_730018029}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x1300755890}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_x189840727}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[64]{lang="EN-US"}[字节空字符""，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节空字符""。]{style="font-family:宋体"}

[**[s1s0]{lang="EN-US"}**]{#struct_0_x1849_14381_1254442352}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[，]{style="font-family:宋体"}**[s1s0]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1371683666}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1622300326}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1153911994}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x493852726}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_966409589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2073184157}

[*[path-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1902840735}[：]{style="font-family:宋体"}[vc3]{lang="EN-US"}[通道编号。]{style="font-family:宋体"}

[**[c2 ]{lang="EN-US"}***[c2-value]{lang="EN-US"}*]{#struct_0_x1849_14381_x189906263}[：信号标记字节，取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**[ **sdh** ]{lang="EN-US"}*[sdh-string]{lang="EN-US"}*]{#struct_0_x1849_14381_1234513535}[：高阶通道追踪字节，]{style="font-family:宋体"}*[sdh-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**[ **sonet** ]{lang="EN-US"}*[sonet-string]{lang="EN-US"}*]{#struct_0_x1849_14381_x1890416366}[：高阶通道追踪字节，]{style="font-family:宋体"}*[sonet-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s1s0 ]{lang="EN-US"}***[s1s0-value]{lang="EN-US"}*]{#struct_0_x1849_14381_x537247247}[：]{style="font-family:宋体"}[AU/TU]{lang="EN-US"}[类型指示值。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1598063643}

[[SONET/SDH]{lang="EN-US"}]{#struct_0_x1849_14381_x806618401}[帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_1880659580}[和]{style="font-family:
宋体"}**[c2]{lang="EN-US"}**[主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_x2141370629}[和]{style="font-family:
宋体"}**[c2]{lang="EN-US"}**[属于高阶通道开销字节，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[用于检测两个接口之间的连接在通道层次上的连续性，]{style="font-family:宋体"}**[c2]{lang="EN-US"}**[用来指示]{style="font-family:宋体"}[VC]{lang="EN-US"}[帧的复接结构和信息净负荷的性质。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190365014}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1599372394}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[vc-3]{lang="EN-US"}[的]{style="font-family:宋体"}[2]{lang="EN-US"}[号通道的]{style="font-family:
宋体"}[c2]{lang="EN-US"}[的开销值为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1050573235}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] flag vc-3 2 c2 2]{lang="EN-US"}
:::

::: {#-788368373 .myid}
[]{#_Toc404783866}[]{#struct_0_x1849_14381_523218638}[]{#_Toc255917517}[]{#_Toc194725127}

**CPOS接口 \-- CPOS接口配置命令 \-- flag vc-4**

------------------------------------------------------------------------

[**[flag vc-4]{lang="EN-US"}**]{#struct_0_x1849_14381_2138970826}[命令用来设置]{style="font-family:宋体"}[vc-4]{lang="EN-US"}[帧的开销字节。]{style="font-family:宋体"}

[**[undo flag vc-4]{lang="EN-US"}**]{#struct_0_x1849_14381_x1108867249}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1852143763}

[**[flag]{lang="EN-US"}**[ **vc-4** ]{lang="EN-US"}*[path-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **c2** ]{lang="EN-US"}*[c2-value ]{lang="EN-US"}*[\| **j1** { **sdh** ]{lang="EN-US"}*[sdh-string ]{lang="EN-US"}*[\| **sonet** ]{lang="EN-US"}*[sonet-string]{lang="EN-US"}***[ ]{lang="EN-US"}**[} \| **s1s0** ]{lang="EN-US"}*[s1s0-value ]{lang="EN-US"}*[}]{lang="EN-US"}]{#struct_0_x1849_14381_750364958}

[**[undo flag vc-4 ]{lang="EN-US"}***[path-number]{lang="EN-US"}*[ { **c2** \| **j1** { **sdh** \| **sonet** } \| **s1s0** }]{lang="EN-US"}]{#struct_0_x1849_14381_1527718568}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190430550}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_379921960}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_1387411061}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[64]{lang="EN-US"}[字节空字符""，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节空字符""。]{style="font-family:宋体"}

[**[s1s0]{lang="EN-US"}**]{#struct_0_x1849_14381_1671097223}[的]{style="font-family:宋体"}[SONET]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[，]{style="font-family:宋体"}**[s1s0]{lang="EN-US"}**[的]{style="font-family:宋体"}[SDH]{lang="EN-US"}[取值为]{style="font-family:宋体"}[0x02]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1391885327}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1367782776}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1797602472}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1960218833}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1472198191}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190496086}

[*[path-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x52490397}[：]{style="font-family:宋体"}[vc4]{lang="EN-US"}[通道编号。]{style="font-family:宋体"}

[**[c2 ]{lang="EN-US"}***[c2-value]{lang="EN-US"}*]{#struct_0_x1849_14381_x384606326}[：信号标记字节，取值范围为]{style="font-family:宋体"}[0x00]{lang="EN-US"}[～]{style="font-family:宋体"}[0xFF]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**[ **sdh** ]{lang="EN-US"}*[sdh-string]{lang="EN-US"}*]{#struct_0_x1849_14381_1016344160}[：高阶通道追踪字节，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[j1]{lang="EN-US"}**[ **sonet** ]{lang="EN-US"}*[sonet-string]{lang="EN-US"}*]{#struct_0_x1849_14381_1922488242}[：高阶通道追踪字节，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[s1s0 ]{lang="EN-US"}***[s1s0-value]{lang="EN-US"}*]{#struct_0_x1849_14381_481417264}[：]{style="font-family:宋体"}[AU/TU]{lang="EN-US"}[类型指示值。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1001391751}

[[SONET/SDH]{lang="EN-US"}]{#struct_0_x1849_14381_227186853}[帧具有丰富的开销字节，可完成对传输网的分层管理等运行维护功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_1380745897}[和]{style="font-family:
宋体"}**[c2]{lang="EN-US"}**[主要用于在不同国家、不同地区、或不同厂商的设备之间提供互通支持。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[j1]{lang="EN-US"}**]{#struct_0_x1849_14381_x190561622}[和]{style="font-family:
宋体"}**[c2]{lang="EN-US"}**[属于高阶通道开销字节，]{style="font-family:宋体"}**[j1]{lang="EN-US"}**[用于检测两个接口之间的连接在通道层次上的连续性，]{style="font-family:宋体"}**[c2]{lang="EN-US"}**[用来指示]{style="font-family:宋体"}[VC]{lang="EN-US"}[帧的复接结构和信息净负荷的性质。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x777146007}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_46120349}[设置]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[vc-4 1]{lang="EN-US"}[号通道]{style="font-family:宋体"}[j1]{lang="EN-US"}[的]{style="font-family:宋体"}[sdh]{lang="EN-US"}[开销字节为]{style="font-family:宋体"}[abcd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x549009615}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] flag vc-4 1 j1 sdh abcd]{lang="EN-US"}
:::

::: {#1701559760 .myid}
[]{#_Toc404783867}[]{#struct_0_x1849_14381_x1012323875}[]{#_Toc255917518}[]{#_Toc136937631}[]{#_Toc196800713}[]{#_Toc197678825}[]{#_Toc196800714}[]{#_Toc197678826}[]{#_Toc196800716}[]{#_Toc197678828}[]{#_Toc196800717}[]{#_Toc197678829}[]{#_Toc196800718}[]{#_Toc197678830}[]{#_Toc196800719}[]{#_Toc197678831}[]{#_Toc196800720}[]{#_Toc197678832}[]{#_Toc196800721}[]{#_Toc197678833}[]{#_Toc196800722}[]{#_Toc197678834}[]{#_Toc196800723}[]{#_Toc197678835}[]{#_Toc196800724}[]{#_Toc197678836}[]{#_Toc196800725}[]{#_Toc197678837}[]{#_Toc196800726}[]{#_Toc197678838}[]{#_Toc196800727}[]{#_Toc197678839}[]{#_Toc196800728}[]{#_Toc197678840}[]{#_Toc196800729}[]{#_Toc197678841}[]{#_Toc196800730}[]{#_Toc197678842}[]{#_Toc196800731}[]{#_Toc197678843}[]{#_Toc196800732}[]{#_Toc197678844}[]{#_Toc196800733}[]{#_Toc197678845}[]{#_Toc196800734}[]{#_Toc197678846}[]{#_Toc196800735}[]{#_Toc197678847}[]{#_Toc196800739}[]{#_Toc197678851}

**CPOS接口 \-- CPOS接口配置命令 \-- frame-format**

------------------------------------------------------------------------

[**[frame-format]{lang="EN-US"}**]{#struct_0_x1849_14381_x535368764}[命令用来设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的帧格式。]{style="font-family:宋体"}

[**[undo frame-format]{lang="EN-US"}**]{#struct_0_x1849_14381_477792035}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1867571529}

[**[frame-format]{lang="EN-US"}**[ { **sdh** \| **sonet** }]{lang="EN-US"}]{#struct_0_x1849_14381_x190627158}

[**[undo]{lang="EN-US"}**[ **frame-format**]{lang="EN-US"}]{#struct_0_x1849_14381_x415655163}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x942526286}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_636442005}[接口的帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1216858680}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x972637092}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1230719439}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1488602362}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x376861196}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190692694}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1849_14381_769735992}[：帧格式为]{style="font-family:宋体"}[SDH]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1849_14381_585114964}[：帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1287175129}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_71099813}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[接口的帧格式为]{style="font-family:宋体"}[SONET]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_2003208203}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] frame-format sonet]{lang="EN-US"}
:::

::: {#-1619675867 .myid}
[]{#_Toc404783868}[]{#struct_0_x1849_14381_480033791}[]{#_Toc255917519}[]{#_Toc194725142}

**CPOS接口 \-- CPOS接口配置命令 \-- ft3**

------------------------------------------------------------------------

[**[ft3]{lang="EN-US"}**]{#struct_0_x1849_14381_357002392}[命令用于配置]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道工作在]{style="font-family:宋体"}[FT3]{lang="EN-US"}[模式，并配置]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式或子速率。]{style="font-family:宋体"}

[**[undo ft3]{lang="EN-US"}**]{#struct_0_x1849_14381_x190758230}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1945599629}

[**[ft3]{lang="EN-US"}**[ *t3-number* { **dsu-mode** { **0** \| **1** \| **2** \| **3** \| **4** } \| **subrate** *sub-number* }]{lang="EN-US"}]{#struct_0_x1849_14381_x171251869}

[**[undo ft3]{lang="EN-US"}**[ *t3-number* { **dsu-mode** \| **subrate** }]{lang="EN-US"}]{#struct_0_x1849_14381_507940156}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_556576754}

[[DSU]{lang="EN-US"}]{#struct_0_x1849_14381_x209947729}[模式为]{style="font-family:宋体"}[0]{lang="EN-US"}[，即]{style="font-family:宋体"}[Digital Link]{lang="EN-US"}[模式；子速率为]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1635233898}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_263545975}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2105882973}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x190823766}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_407095510}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1837268108}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_565164597}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[dsu-mode]{lang="EN-US"}**]{#struct_0_x1849_14381_222612942}[：设置]{style="font-family:宋体"}[FT3]{lang="EN-US"}[的]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式，支持常用的几家厂商的]{style="font-family:宋体"}[FT3 DSU]{lang="EN-US"}[模式，如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[0]{lang="PT-BR"}**]{#struct_0_x1849_14381_x611172241}[：]{lang="EN-US" style="font-family:宋体"}[Digital Link]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[支持子速率范围为]{lang="EN-US" style="font-family:
宋体"}[300]{lang="PT-BR"}[～]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[共]{lang="EN-US" style="font-family:
宋体"}[147]{lang="PT-BR"}[个速率等级]{lang="EN-US" style="font-family:
宋体"}[，]{lang="EN-US" style="font-family:宋体"}[级差]{lang="EN-US" style="font-family:宋体"}[300746bps]{lang="PT-BR"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}**[1]{lang="PT-BR"}**]{#struct_0_x1849_14381_344844511}[：]{lang="EN-US" style="font-family:宋体"}[Kentrox]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[1500]{lang="PT-BR"}[～]{lang="EN-US" style="font-family:宋体"}[35000kbps]{lang="PT-BR"}[及]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="PT-BR"}[，]{lang="EN-US" style="font-family:宋体"}[共]{lang="EN-US" style="font-family:宋体"}[69]{lang="PT-BR"}[个速率等级]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[级差]{lang="EN-US" style="font-family:宋体"}[500000bps]{lang="PT-BR"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2]{lang="EN-US"}**]{#struct_0_x1849_14381_x1541677562}[：]{style="font-family:
宋体"}[Larscom]{lang="EN-US"}[，支持子速率范围为]{style="font-family:宋体"}[3100]{lang="EN-US"}[～]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{style="font-family:宋体"}[14]{lang="EN-US"}[个速率等级，级差]{style="font-family:宋体"}[3157835bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[3]{lang="EN-US"}**]{#struct_0_x1849_14381_1009699265}[：]{style="font-family:
宋体"}[Adtran]{lang="EN-US"}[，支持子速率范围为]{style="font-family:宋体"}[75]{lang="EN-US"}[～]{style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{style="font-family:宋体"}[588]{lang="EN-US"}[个速率等级，级差]{style="font-family:宋体"}[75187bps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[4]{lang="EN-US"}**]{#struct_0_x1849_14381_x189840726}[：]{lang="EN-US" style="font-family:宋体"}[Verilink]{lang="EN-US"}[，支持子速率范围为]{lang="EN-US" style="font-family:宋体"}[1500]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[44210kbps]{lang="EN-US"}[，共]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[个速率等级，级差]{lang="EN-US" style="font-family:宋体"}[1578918bps]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[subrate ]{lang="EN-US"}***[sub-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1254376816}[：设置]{style="font-family:宋体"}[FT3]{lang="EN-US"}[的子速率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[44210]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x142055021}

[[FT3]{lang="EN-US"}]{#struct_0_x1849_14381_x663899493}[（]{style="font-family:宋体"}[Fractional T3]{lang="EN-US"}[，或称]{style="font-family:宋体"}[Subrate T3]{lang="EN-US"}[）是]{style="font-family:宋体"}[T3]{lang="EN-US"}[的一种非标准应用模式。目前各厂商支持的速率等级均不一样，使用]{style="font-family:宋体"}**[ft3]{lang="EN-US"}**[命令可以使我们的设备和其他厂家设备的]{style="font-family:宋体"}[FT3 DSU]{lang="EN-US"}[模式兼容，实现互通。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1943801453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[ft3 subrate]{lang="EN-US"}**]{#struct_0_x1849_14381_x21319458}[设置的速率值是一个大概值。由于通过]{lang="EN-US" style="font-family:宋体"}**[ft3 dsu-mode]{lang="EN-US"}**[命令配置的各]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[的子速率值是离散的，因此，当再通过]{lang="EN-US" style="font-family:宋体"}**[ft3 subrate]{lang="EN-US"}**[命令指定子速率后，]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[接口会根据当前配置的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式计算出与这个指定子速率最匹配的精确速率（精确到]{lang="EN-US" style="font-family:宋体"}[bps]{lang="EN-US"}[），并设置硬件电路支持该速率。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}**[display interface serial ]{lang="EN-US"}***[interface-number]{lang="EN-US"}***[:0]{lang="EN-US"}**]{#struct_0_x1849_14381_x1894079362}[命令可以查看]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[DSU]{lang="EN-US"}[模式、子速率设置值、接口实际速率和接口的波特率。接口实际速率为不含开销在内的纯数据带宽，接口波特率（]{lang="EN-US" style="font-family:宋体"}[44736kbps]{lang="EN-US"}[）为]{lang="EN-US" style="font-family:宋体"}[T3]{lang="EN-US"}[线路的实际速率（含开销位在内）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1210868803}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x561862411}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[工作在]{style="font-family:宋体"}[DSU]{lang="EN-US"}[模式]{style="font-family:宋体"}[3]{lang="EN-US"}[，速率]{style="font-family:宋体"}[3000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x189906262}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] ft3 1 dsu-mode 3]{lang="FR"}

[\[]{lang="EN-US"}[Sysname]{lang="PT-BR"}[-Cpos2/4/0\] ft3 1 subrate 3000]{lang="EN-US"}
:::

::::: {#1002176090 .myid}
[]{#_Toc255917520}[]{#_Toc136937632}[]{#_Toc404783869}[]{#struct_0_x1849_14381_1234447999}[]{#_Toc194808757}[]{#_Toc195414789}

**CPOS接口 \-- CPOS接口配置命令 \-- link-delay**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image004.png){#图片 6 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1849_14381_2073409229}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_1790250905}
:::

[ ]{lang="EN-US"}

[**[link-delay]{lang="EN-US"}**]{#struct_0_x1849_14381_x824157970}[命令用来配置当前接口的物理连接状态抑制时间。]{style="font-family:宋体"}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x1849_14381_x1718645707}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x375267814}

[**[link-delay]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1849_14381_113330403}

[**[undo link-delay]{lang="EN-US"}**]{#struct_0_x1849_14381_x190365017}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1599175786}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1280402157}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_526089255}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1183328913}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1368927554}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x769782432}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_570559129}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1035630628}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1849_14381_x190430553}[：表示物理连接状态的抑制时间，单位为秒。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_379725352}

[[通常情况下，当接口的物理连接状态（]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1849_14381_1548087833}[和]{style="font-family:宋体"}[down]{lang="EN-US"}[）改变时，系统会立即通知上层协议模块并生成]{style="font-family:宋体"}[Trap]{lang="EN-US"}[和]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。为了避免接口物理连接状态在短时间内的频繁改变带来额外的系统开销，可通过本命令配置接口的物理连接状态抑制时间，接口在此时间内产生的物理连接状态变化将被系统忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_542244049}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1604639913}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的物理连接状态抑制时间为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1930914606}

[[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}]{#struct_0_x1849_14381_x1716646657}

[\[Sysname-Cpos2/4/0\] link-delay 8]{lang="EN-US"}
:::::

::: {#405613428 .myid}
[]{#_Toc404783870}[]{#struct_0_x1849_14381_x776610339}

**CPOS接口 \-- CPOS接口配置命令 \-- loopback**

------------------------------------------------------------------------

[**[loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x190496089}[命令用来开启]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的环回功能。]{style="font-family:宋体"}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x52424861}[命令用来取消环回设置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x43407986}

[**[loopback]{lang="EN-US"}**[ { **local** \| **remote** }]{lang="EN-US"}]{#struct_0_x1849_14381_1122570730}

[**[undo loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_1175860028}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1016476673}

[[环回功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x438374956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1158017077}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_292287499}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190561625}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x776949399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x295310985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_619849164}

[**[local]{lang="EN-US"}**]{#struct_0_x1849_14381_605865485}[：设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口进行对内自环。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1849_14381_789394423}[：设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口进行对外远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1792208257}

[[环回主要用于一些特殊功能的测试。对内自环也称为本地环回，用于对物理接口本身进行检测。对外环回则可用于对接口连接的线缆进行检测。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1418485265}

[[正常情况下，不要设置环回功能。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1064919664}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190627161}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x415065340}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[进行远端线路环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x562679930}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] loopback remote]{lang="EN-US"}
:::

::: {#-1279369240 .myid}
[]{#_Toc404783871}[]{#struct_0_x1849_14381_1568665927}[]{#_Toc255917521}[]{#_Toc136937633}

**CPOS接口 \-- CPOS接口配置命令 \-- multiplex mode**

------------------------------------------------------------------------

[**[multiplex mode]{lang="EN-US"}**]{#struct_0_x1849_14381_x140797298}[命令用来设置]{style="font-family:宋体"}[AUG]{lang="EN-US"}[的复用路径。]{style="font-family:宋体"}

[**[undo multiplex mode]{lang="EN-US"}**]{#struct_0_x1849_14381_1810090611}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_130680100}

[**[multiplex mode ]{lang="EN-US"}**[{ **au-3** \| **au-4** }]{lang="EN-US"}]{#struct_0_x1849_14381_x1663854723}

[**[undo]{lang="EN-US"}**[ **multiplex mode**]{lang="EN-US"}]{#struct_0_x1849_14381_x190692697}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_769801528}

[[AUG]{lang="EN-US"}]{#struct_0_x1849_14381_x795632385}[的复用路径为]{style="font-family:宋体"}**[au-4]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_864697656}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1108040983}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_700994314}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_855611054}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x694993220}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x871184198}

[**[au-3]{lang="EN-US"}**]{#struct_0_x1849_14381_x190758233}[：配置]{style="font-family:宋体"}[AUG]{lang="EN-US"}[通过]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[得到。]{style="font-family:宋体"}

[**[au-4]{lang="EN-US"}**]{#struct_0_x1849_14381_x1945534093}[：配置]{style="font-family:宋体"}[AUG]{lang="EN-US"}[通过]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[得到。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_285247797}

[[当]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x163583786}[应用在]{style="font-family:宋体"}[SDH]{lang="EN-US"}[模式下时，可使用]{style="font-family:宋体"}**[multiplex mode]{lang="EN-US"}**[命令选择设置]{style="font-family:宋体"}[AUG]{lang="EN-US"}[复用到]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[还是]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[，如果]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[应用在]{style="font-family:宋体"}[SONET]{lang="EN-US"}[模式下，则只能复用到]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[，不能使用]{style="font-family:宋体"}**[multiplex mode]{lang="EN-US"}**[命令。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SDH]{lang="EN-US"}]{#struct_0_x1849_14381_1367768830}[中，载荷有两种映射]{style="font-family:宋体"}[/]{lang="EN-US"}[复用的方案：]{style="font-family:宋体"}[ANSI]{lang="EN-US"}[和]{style="font-family:宋体"}[ETSI]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ANSI]{lang="EN-US"}]{#struct_0_x1849_14381_1019850390}[的复用方案为]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[复用（]{style="font-family:宋体"}**[au-3]{lang="EN-US"}**[），低阶载荷被聚合进]{style="font-family:宋体"}[VC-3]{lang="EN-US"}[高阶通道，]{style="font-family:宋体"}[VC-3]{lang="EN-US"}[加上一个]{style="font-family:宋体"}[AU]{lang="EN-US"}[指针后成为管理单元]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[，再由三个这样的]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[同步复用成一个管理单元组]{style="font-family:宋体"}[AUG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ETSI]{lang="EN-US"}]{#struct_0_x1849_14381_976946212}[的复用方案为]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[复用（]{style="font-family:宋体"}**[au-4]{lang="EN-US"}**[），低阶载荷被聚合进]{style="font-family:宋体"}[VC-4]{lang="EN-US"}[高阶通道，]{style="font-family:宋体"}[VC-4]{lang="EN-US"}[加上一个]{style="font-family:宋体"}[AU]{lang="EN-US"}[指针后成为管理单元]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[，再由一个这样的]{style="font-family:宋体"}[AU-4]{lang="EN-US"}[同步复用成一个管理单元组]{style="font-family:宋体"}[AUG]{lang="EN-US"}[。]{style="font-family:宋体"}

[[实际应用中，不同的国家和地区可能采用不同的复用路径，为保证互通，请用户根据实际情况选择合适的复用路径（我国光同步传输网技术体制选用的是]{style="font-family:宋体"}[AU-4]{lang="EN-US"}]{#struct_0_x1849_14381_75607610}[的复用路径）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1036953049}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_568245567}[在]{style="font-family:宋体"}[SDH]{lang="EN-US"}[模式下，设置]{style="font-family:宋体"}[AUG]{lang="EN-US"}[复用到]{style="font-family:宋体"}[AU-3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x190823769}

[\[Sysname\] controller cpos 2/4/0]{lang="FR"}

[\[Sysname-Cpos2/4/0\] frame-format sdh]{lang="FR"}

[\[Sysname-Cpos2/4/0\] multiplex mode au-3]{lang="FR"}

[]{#_Toc255917522}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_406767830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[frame-format]{lang="EN-US"}**]{#struct_0_x1849_14381_1398708919}
:::

::::: {#1892875262 .myid}
[]{#_Toc296086935}[]{#_Toc205801702}[]{#_Toc404783872}[]{#struct_0_x1849_14381_75673146}[]{#_Toc345232199}

**CPOS接口 \-- CPOS接口配置命令 \-- oc-12**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_76262970}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_1125756608}
:::

[ ]{lang="PT-BR"}

[**[oc-12]{lang="PT-BR"}**]{#struct_0_x1849_14381_251742793}[命令用来在]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图下创建指定通道号的]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道，并且进入指定]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道视图；如果已经创建了此]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道，直接进入指定]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道视图。]{style="font-family:宋体"}

[**[undo oc-12]{lang="EN-US"}**]{#struct_0_x1849_14381_x523604545}[命令用来删除指定通道号的]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道及其派生的低阶通道（包括]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道和]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道下的]{style="font-family:宋体"}[E3/T3]{lang="EN-US"}[通道）及]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_76328506}

[**[oc-12 ]{lang="ES-AR"}**]{#struct_0_x1849_14381_x53476192}*[oc-12-number]{lang="ES-AR"}*

[**[undo oc-12 ]{lang="ES-AR"}**]{#struct_0_x1849_14381_x1393267176}*[oc-12-number]{lang="ES-AR"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x427169300}

[[2.5Gbps]{lang="ES-AR"}]{#struct_0_x1849_14381_1641822628}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口下无]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2000378265}

[[2.5Gbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x586761316}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x810370650}

[[network-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_1641888164}

[[mdc-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_1534388139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1107641838}

[*[oc-12-number]{lang="ES-AR"}*]{#struct_0_x1849_14381_x1358814611}[：]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[4]{lang="ES-AR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1641953700}

[[2.5Gbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x1902588397}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口工作在通道模式时]{style="font-family:宋体"}[，最多]{style="font-family:宋体"}[支持创建]{style="font-family:宋体"}[4]{lang="ES-AR"}[个]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x503800238}

[[\# ]{lang="ES-AR"}]{#struct_0_x1849_14381_x370740760}[在]{style="font-family:宋体"}[2.5Gbps]{lang="ES-AR"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="ES-AR"}[接口下创建]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES-AR"}]{#struct_0_x1849_14381_1642019236}

[\[Sysname\] controller cpos 2/4/0]{lang="ES-AR"}

[\[Sysname-Cpos2/4/0\] oc-12 2]{lang="ES-AR"}

[\[Sysname-Cpos2/4/0-oc-12-2\]]{lang="ES-AR"}
:::::

::::: {#-1586347206 .myid}
[]{#_Toc404783873}[]{#struct_0_x1849_14381_x2100470453}[]{#_Toc345232200}

**CPOS接口 \-- CPOS接口配置命令 \-- oc-3**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){#图片 13 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1424853200}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_1641560484}
:::

[ ]{lang="PT-BR"}

[**[oc-3]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1505737926}[命令用来在]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图下或]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道视图下创建指定通道号的]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道，并且进入指定]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道视图；如果已经创建了此]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道，直接进入指定]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道视图。]{style="font-family:宋体"}

[**[undo oc-3]{lang="EN-US"}**]{#struct_0_x1849_14381_x1309927503}[命令用来删除指定通道号的]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道及其派生的低阶通道（包括]{style="font-family:宋体"}[E3/T3]{lang="EN-US"}[通道）及]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_902844833}

[**[oc-3 ]{lang="ES-AR"}**]{#struct_0_x1849_14381_1641626020}*[oc-3-number]{lang="ES-AR"}*

[**[undo oc-3 ]{lang="ES-AR"}**]{#struct_0_x1849_14381_56592367}*[oc-3-number]{lang="ES-AR"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_49633584}

[[622Mbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x326132075}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口或]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道下无]{style="font-family:宋体"}[155Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_774826502}

[[622Mbps]{lang="EN-US"}]{#struct_0_x1849_14381_1641691556}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/622Mbps]{lang="EN-US"}[通道视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1146374101}

[[network-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_x364093041}

[[mdc-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_x1634304467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1641757092}

[*[oc-3-number]{lang="ES-AR"}*]{#struct_0_x1849_14381_x1507328908}[：]{style="font-family:宋体"}[155Mbps]{lang="ES-AR"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="ES-AR"}[～]{style="font-family:宋体"}[4]{lang="ES-AR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x758312968}

[[622Mbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x638318325}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口或]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[通道工作在通道模式时]{style="font-family:宋体"}[，]{style="font-family:宋体"}[最多支持创建]{style="font-family:宋体"}[4]{lang="ES-AR"}[个]{style="font-family:宋体"}[155Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[622Mbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x535263449}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口或]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道创建]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道时，如果]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道不支持通道模式，则自动配置为级联模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1642346916}

[[\# ]{lang="ES-AR"}]{#struct_0_x1849_14381_354388053}[在]{style="font-family:宋体"}[622Mbps]{lang="ES-AR"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="ES-AR"}[接口下创建]{style="font-family:宋体"}[155Mbps]{lang="ES-AR"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES-AR"}]{#struct_0_x1849_14381_2146974186}

[\[Sysname\] controller cpos 2/4/0]{lang="ES-AR"}

[\[Sysname-Cpos2/4/0\] oc-3 2]{lang="ES-AR"}

[\[Sysname-Cpos]{lang="PT-BR"}[2/4/0]{lang="ES-AR"}[-oc-3-2\]]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x1849_14381_1642412452}[在]{style="font-family:宋体"}[2.5Gbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[2/4/0]{lang="ES-AR"}[接口的]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[通道下创建]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x1849_14381_1094801944}

[\[Sysname\] controller cpos 2/4/0]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0\] oc-12 1]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-12-1\] oc-3 1]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-12-1-oc-3-1\]]{lang="PT-BR"}
:::::

::: {#-1696976163 .myid}
[]{#_Toc404783874}[]{#struct_0_x1849_14381_x716983435}

**CPOS接口 \-- CPOS接口配置命令 \-- reset counters controller cpos**

------------------------------------------------------------------------

[**[reset counters controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_2108912945}[命令用来清除]{style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x949736218}

[**[reset counters controller cpos]{lang="EN-US"}**[ \[ *interface-number* \]]{lang="EN-US"}]{#struct_0_x1849_14381_x1738189360}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_197301245}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1849_14381_x189840729}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1255359856}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1752585582}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_655547758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1824511586}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1746708448}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_176678984}

[[在某些情况下，需要统计一定时间内某接口的流量，这就需要在统计开始前清除该接口原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x369614039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1534790673}[，则清除所有]{lang="EN-US" style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:
宋体"}[的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x189906265}[，则清除指定]{lang="EN-US" style="font-family:
宋体"}[CPOS]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:
宋体"}[的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[统计信息可以用]{style="font-family:宋体"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_1234906751}[命令来查看。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1867830589}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x57521720}[清除]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters controller cpos 2/4/0]{lang="EN-US"}]{#struct_0_x1849_14381_1872382179}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x102031777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos]{lang="EN-US"}**]{#struct_0_x1849_14381_x99195626}
:::

::: {#1170655049 .myid}
[]{#_Toc404783875}[]{#struct_0_x1849_14381_1624903610}[]{#_Toc255917523}[]{#_Toc136937634}

**CPOS接口 \-- CPOS接口配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x741371768}[命令用来关闭接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x1849_14381_x190365016}[命令用来打开接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1599241322}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1186380764}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1775990675}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1751266276}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1509124531}[接口处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_371390007}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1169161108}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_968607816}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x190430552}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_379790888}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1137093187}

[[对]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x2074310226}[物理接口执行]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[操作后，该]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[的所有]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[通道及捆绑形成的串口将全部被禁用，停止收发数据。如果执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[操作，则所有]{style="font-family:宋体"}[E1/T1]{lang="EN-US"}[通道和捆绑形成的串口将恢复为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1814460855}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1335486002}[关闭]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_263269217}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] shutdown]{lang="EN-US"}
:::

::: {#-1029661762 .myid}
[]{#_Toc404783876}[]{#struct_0_x1849_14381_x496045546}[]{#_Toc255917524}[]{#_Toc136937635}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 channel-set**

------------------------------------------------------------------------

[**[t1 channel-set]{lang="EN-US"}**]{#struct_0_x1849_14381_x190496088}[命令用来对]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时隙进行捆绑。]{style="font-family:宋体"}

[**[undo t1 channel-set]{lang="EN-US"}**]{#struct_0_x1849_14381_x52359325}[命令用来取消指定的捆绑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1079484660}

[**[t1]{lang="EN-US"}**[ *t1-number* **channel-set** *set-number* **timeslot-list** *range* \[ **speed** { **56k** \| **64k** } \]]{lang="EN-US"}]{#struct_0_x1849_14381_x1706994843}

[**[undo t1]{lang="EN-US"}**[ *t1-number* **channel-set** *set-number*]{lang="EN-US"}]{#struct_0_x1849_14381_x1739500362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x983384854}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_x134932742}[不进行通道化。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_388615210}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_185107867}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190561624}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x777014935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1923951607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1484666285}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1590105616}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[set-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x822956822}[：捆绑集的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[timeslot-list]{lang="EN-US"}***[ range]{lang="EN-US"}*]{#struct_0_x1849_14381_1536104581}[：用于捆绑的时隙列表。]{style="font-family:宋体"}*[range]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[，在指定捆绑的时隙时，可以用]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的形式指定单个时隙，也可以用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[～]{style="font-family:宋体"}*[number2]{lang="EN-US"}*[的形式指定一个范围内的时隙，还可以使用]{style="font-family:宋体"}*[number1]{lang="EN-US"}*[、]{style="font-family:宋体"}*[number2]{lang="EN-US"}*[～]{style="font-family:宋体"}*[number3]{lang="EN-US"}*[的形式，同时指定多个时隙。]{style="font-family:宋体"}

[**[speed]{lang="EN-US"}**[ { **56k** \| **64k** }]{lang="EN-US"}]{#struct_0_x1849_14381_1562067591}[：配置时隙捆绑的方式。选用参数]{style="font-family:宋体"}**[56k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[56kbps]{lang="EN-US"}[；选用参数]{style="font-family:宋体"}**[64k]{lang="EN-US"}**[时，捆绑方式为]{style="font-family:宋体"}[N]{lang="EN-US"}[×]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。如果不指定速率，缺省采用]{style="font-family:宋体"}[64kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1889436673}

[[捆绑形成的串口编号形式为：接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1849_14381_x190627160}[通道号]{style="font-family:宋体"}[:channel-set]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x415130876}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_256496149}[对]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[进行捆绑。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x2143700331}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 1 channel-set 1 timeslot-list 1-23]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1311499413}[进入捆绑后形成的串口的视图。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0\] quit]{lang="EN-US"}]{#struct_0_x1849_14381_x1757825495}

[\[Sysname\] interface serial 2/4/0/1:1]{lang="EN-US"}

[\[Sysname-Serial2/4/0/1:1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x615575303}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[t]{lang="EN-US"}[1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_x698601394}
:::

::: {#-739348293 .myid}
[]{#_Toc404783877}[]{#struct_0_x1849_14381_x190692696}[]{#_Toc255917525}[]{#_Toc136937636}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 clock**

------------------------------------------------------------------------

[**[t1 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_769867064}[命令用来设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo t1 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_x1144046084}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1686346118}

[**[t1]{lang="EN-US"}**[ *t1-number* **clock** { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1849_14381_1598513353}

[**[undo t1]{lang="EN-US"}**[ *t1-number* **clock**]{lang="EN-US"}]{#struct_0_x1849_14381_x2017723853}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_334180599}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_148495378}[通道的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x190758232}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1945468557}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x159198577}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x600926503}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1767234300}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x849140103}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x774631221}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_982093347}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_x1499287387}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1580596578}

[[可以为不同的]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1849_14381_x190823768}[通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。]{style="font-family:宋体"}

[[同一]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_406702294}[物理接口的不同]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的时钟模式是相互独立的。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_540944379}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_205102790}[设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x524949421}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 1 clock master]{lang="EN-US"}
:::

::: {#-528596185 .myid}
[]{#_Toc136937637}[]{#_Toc404783878}[]{#struct_0_x1849_14381_x1223943375}[]{#_Toc255917526}[]{#_Toc168471852}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 flag**

------------------------------------------------------------------------

[**[t1 flag]{lang="EN-US"}**]{#struct_0_x1849_14381_x1124603184}[命令用来设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道开销。]{style="font-family:宋体"}

[**[undo t1 flag]{lang="EN-US"}**]{#struct_0_x1849_14381_1509741761}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x189840728}

[**[t1]{lang="EN-US"}[ ]{lang="EN-US"}***[t1-number]{lang="EN-US"}*[ **flag** **c2** *c2-value*]{lang="EN-US"}]{#struct_0_x1849_14381_1255294320}

[**[undo t1 ]{lang="DE"}**]{#struct_0_x1849_14381_1364415205}*[t1-number]{lang="DE"}*[ **flag** **c2**]{lang="DE"}

[**[t1]{lang="DA"}**]{#struct_0_x1849_14381_x838886833}**[ ]{lang="DA"}***[t1-number]{lang="DE"}*[ ]{lang="DE"}**[flag ]{lang="DA"}[j2 ]{lang="DA"}**[{ **sdh** \| **sonet** } ]{lang="DA"}*[j2-string]{lang="DE"}*

[**[undo t1 ]{lang="DA"}**]{#struct_0_x1849_14381_x1538262558}*[t1-number]{lang="DE"}*[ ]{lang="DE"}**[flag ]{lang="DA"}[j2]{lang="DA"}**[ { **sdh** \| **sonet** }]{lang="DA"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_70859279}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x1345534775}[取值为]{style="font-family:宋体"}[02]{lang="EN-US"}[（十六进制），]{style="font-family:宋体"}**[j2]{lang="EN-US"}**[循环发送空字符""。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1221542484}

[[CPOS]{lang="DA"}]{#struct_0_x1849_14381_202710139}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x189906264}

[[network-admin]{lang="DA"}]{#struct_0_x1849_14381_1234841215}

[[mdc-admin]{lang="DA"}]{#struct_0_x1849_14381_2043780983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_351156014}

[*[t1-number]{lang="DA"}*]{#struct_0_x1849_14381_x1281557237}[：]{style="font-family:宋体"}[CPOS]{lang="DA"}[接口的]{style="font-family:
宋体"}[T1]{lang="DA"}[通道号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[84]{lang="DA"}[。]{style="font-family:宋体"}

[**[c2]{lang="EN-US"}**]{#struct_0_x1849_14381_x906541320}[：低阶通道信号标签字节。]{style="font-family:宋体"}

[*[c2-value]{lang="EN-US"}*]{#struct_0_x1849_14381_1691903452}[：一个字节的开销的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。协议不支持该值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[j2]{lang="EN-US"}**]{#struct_0_x1849_14381_x987694665}[：低阶通道踪迹字节]{style="font-family:宋体"}[J2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sdh]{lang="EN-US"}**]{#struct_0_x1849_14381_784930714}[：]{style="font-family:宋体"}[SDH]{lang="EN-US"}[格式的跟踪字节。]{style="font-family:宋体"}

[**[sonet]{lang="EN-US"}**]{#struct_0_x1849_14381_1375718928}[：]{style="font-family:宋体"}[SONET]{lang="EN-US"}[格式的跟踪字节。]{style="font-family:宋体"}

[*[j2-string]{lang="EN-US"}*]{#struct_0_x1849_14381_943493072}[：踪迹字节，对于]{style="font-family:宋体"}[SDH]{lang="EN-US"}[格式取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符，对于]{style="font-family:宋体"}[SONET]{lang="EN-US"}[格式取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x853003254}

[[\# CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1762300879}[接口下配置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[c2]{lang="EN-US"}[开销为]{style="font-family:宋体"}[0x7]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1003574255}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 3 flag c2 7]{lang="DA"}
:::

::: {#-1539254743 .myid}
[]{#_Toc404783879}[]{#struct_0_x1849_14381_x1860569680}[]{#_Toc255917527}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 frame-format**

------------------------------------------------------------------------

[**[t1 frame-format]{lang="EN-US"}**]{#struct_0_x1849_14381_673582470}[命令用来设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的帧格式。]{style="font-family:宋体"}

[**[undo t1 frame-format]{lang="EN-US"}**]{#struct_0_x1849_14381_1928013361}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375653392}

[**[t1]{lang="EN-US"}***[ t1-number]{lang="EN-US"}***[ frame-format ]{lang="EN-US"}**[{ **esf** \| **sf** }]{lang="EN-US"}]{#struct_0_x1849_14381_1653320039}

[**[undo]{lang="EN-US"}**[ **t1** *t1-number* **frame-format**]{lang="EN-US"}]{#struct_0_x1849_14381_822224176}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x324287932}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_1713474584}[通道的帧格式为]{style="font-family:宋体"}[ESF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1906431764}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1825204225}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1983916525}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1321291848}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1375587856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_91847528}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x556957850}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[esf]{lang="EN-US"}**]{#struct_0_x1849_14381_1347535531}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道使用]{style="font-family:宋体"}[ESF]{lang="EN-US"}[（]{style="font-family:宋体"}[Extended Super Frame]{lang="EN-US"}[，扩展超帧）格式。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x1849_14381_1708909921}[：设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道使用]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Super Frame]{lang="EN-US"}[，超帧）格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1418773449}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_468833483}[设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的帧格式为]{style="font-family:宋体"}[SF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1749666630}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 1 frame-format sf]{lang="EN-US"}
:::

::: {#295096647 .myid}
[]{#_Toc404783880}[]{#struct_0_x1849_14381_1375522320}[]{#_Toc255917528}[]{#_Toc136937638}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 loopback**

------------------------------------------------------------------------

[**[t1 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_80747928}[命令用来设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道的环回模式。]{style="font-family:宋体"}

[**[undo t1 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x322367674}[命令用来取消环回。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_275811427}

[**[t1]{lang="EN-US"}**[ *t1-number* **loopback** { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1849_14381_x1755953731}

[**[undo t1]{lang="EN-US"}**[ *t1-number* **loopback**]{lang="EN-US"}]{#struct_0_x1849_14381_122513339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2007199349}

[[未进行任何形式的环回。]{style="font-family:宋体"}]{#struct_0_x1849_14381_278584591}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x429936498}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1375456784}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1117065171}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1376244765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1405041713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1325142162}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1027793671}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1849_14381_x533691934}[：使能]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1849_14381_x1291030984}[：使能]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对外载荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1849_14381_x1546600996}[：使能]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道对外远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375391248}

[[环回功能通常用于进行某些特殊测试，正常工作时不要启动环回。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1490042741}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x866638191}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1890876597}[设置]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[进行对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x2049818398}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 1 loopback payload]{lang="EN-US"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_x1849_14381_3895946}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos t1]{lang="EN-US"}**]{#struct_0_x1849_14381_x123653667}
:::

::: {#-539068290 .myid}
[]{#_Toc404783881}[]{#struct_0_x1849_14381_x21930131}[]{#_Toc255917529}[]{#_Toc136937639}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 shutdown**

------------------------------------------------------------------------

[**[t1 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x1887150686}[命令用来关闭]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo t1 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_1375325712}[命令用来打开]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x720792836}

[**[t1 ]{lang="EN-US"}***[t1-number ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x1821250899}

[**[undo t1 ]{lang="EN-US"}***[t1-number ]{lang="EN-US"}***[shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_638952426}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2047792242}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_857941013}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x742240724}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_467603625}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375260176}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1455606454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1286339861}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1842831583}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x337004687}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1761145029}

[[关闭]{style="font-family:宋体"}[T1]{lang="EN-US"}]{#struct_0_x1849_14381_1650807217}[通道后，如果有捆绑形成的串口，则串口也被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1755771852}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_895070223}[关闭]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1376243216}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 1 shutdown]{lang="EN-US"}
:::

::: {#-982206442 .myid}
[]{#_Toc404783882}[]{#struct_0_x1849_14381_x812865053}[]{#_Toc255917530}[]{#_Toc136937640}

**CPOS接口 \-- CPOS接口配置命令 \-- t1 unframed**

------------------------------------------------------------------------

[**[t1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_1107636461}[命令用来设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道工作在非成帧模式。]{style="font-family:宋体"}

[**[undo t1 unframed]{lang="EN-US"}**]{#struct_0_x1849_14381_1228147928}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1561902884}

[**[t1]{lang="EN-US"}**[ *t1-number* **unframed**]{lang="EN-US"}]{#struct_0_x1849_14381_x1470481438}

[**[undo t1]{lang="EN-US"}**[ *t1-number* **unframed**]{lang="EN-US"}]{#struct_0_x1849_14381_1069076098}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x28045467}

[[T1]{lang="EN-US"}]{#struct_0_x1849_14381_x1259989157}[工作在成帧模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1376177680}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x2028110873}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x89171649}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_700649351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_614044900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1753431872}

[*[t1-number]{lang="EN-US"}*]{#struct_0_x1849_14381_633843696}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[84]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x74314270}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1375718929}[通道化生成的]{style="font-family:宋体"}[T1]{lang="EN-US"}[支持非成帧和成帧两种工作模式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在非成帧模式下，]{style="font-family:宋体"}]{#struct_0_x1849_14381_943427536}[T1]{lang="EN-US"}[通道不分时隙，形成一个速率为]{style="font-family:宋体"}[1.544Mbps]{lang="EN-US"}[的串口，名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在成帧模式下，]{style="font-family:宋体"}]{#struct_0_x1849_14381_1926425568}[T1]{lang="EN-US"}[通道的]{style="font-family:宋体"}[24]{lang="EN-US"}[个时隙可以任意捆绑为串口使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x522267255}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_905939991}[将]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的第]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[T1]{lang="EN-US"}[通道设置为非成帧模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x820939910}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t1 3 unframed]{lang="EN-US"}
:::

::: {#-406436400 .myid}
[]{#_Toc404783883}[]{#struct_0_x1849_14381_x730850511}[]{#_Toc255917531}[]{#_Toc194725135}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 alarm**

------------------------------------------------------------------------

[**[t3]{lang="EN-US"}**[ **alarm**]{lang="EN-US"}]{#struct_0_x1849_14381_1399186199}[命令用来配置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的告警信号检测与发送功能。用户可打开或关闭告警信号的检测开关，也可发送某种告警信号以测试线路状态等。]{style="font-family:宋体"}

[**[undo t3]{lang="EN-US"}**[ **alarm**]{lang="EN-US"}]{#struct_0_x1849_14381_1375653393}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1653254503}

[**[t3]{lang="EN-US"}**[ *t3-number* **alarm** { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]{lang="EN-US"}]{#struct_0_x1849_14381_1219384038}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **alarm** { **detect** \| **generate** { **ais** \| **febe** \| **idle** \| **rai** } }]{lang="EN-US"}]{#struct_0_x1849_14381_815060919}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x53055842}

[[T3]{lang="EN-US"}]{#struct_0_x1849_14381_x424179891}[通道的告警信号检测功能处于打开状态，发送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_980425281}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_2085050493}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x212440342}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1375587857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_91913064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x208915695}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_324024535}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_x1849_14381_1094966588}[：]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的定时检测各种告警的功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_x1849_14381_x487964476}[：发送某种告警信号，如]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[、]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[和]{style="font-family:宋体"}[FEBE]{lang="EN-US"}[。可用于线路状态测试。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ais]{lang="EN-US"}**]{#struct_0_x1849_14381_581310390}[：]{lang="EN-US" style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，即告警指示信号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[febe]{lang="EN-US"}**]{#struct_0_x1849_14381_x1155819983}[：]{lang="EN-US" style="font-family:宋体"}[Far End Block Error]{lang="EN-US"}[，即远端块错误。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[idle]{lang="EN-US"}**]{#struct_0_x1849_14381_180405725}[：空闲信号。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rai]{lang="EN-US"}**]{#struct_0_x1849_14381_x303398466}[：]{lang="EN-US" style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，即远端告警指示信号。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375522321}

[[上电后，]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1849_14381_80813464}[通道的告警信号检测功能是打开的，并能通过通道显示实时报告通道告警状态，如]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[等。当检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警信号后，会向对方发送]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[主要的告警信号包括：]{style="font-family:宋体"}[LOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1506782795}[（]{style="font-family:宋体"}[Loss Of Signal]{lang="EN-US"}[，信号丢失）、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[（]{style="font-family:宋体"}[Loss Of Frame]{lang="EN-US"}[，帧同步丢失）、]{style="font-family:宋体"}[AIS]{lang="EN-US"}[（]{style="font-family:宋体"}[Alarm Indication Signal]{lang="EN-US"}[，告警指示信号）、]{style="font-family:宋体"}[RAI]{lang="EN-US"}[（]{style="font-family:宋体"}[Remote Alarm Indication]{lang="EN-US"}[，远端告警指示信号）、]{style="font-family:宋体"}[FEBE]{lang="EN-US"}[（]{style="font-family:宋体"}[Far End Block Error]{lang="EN-US"}[，远端块错误）、]{style="font-family:宋体"}[IDLE]{lang="EN-US"}[为空闲信号。各信号具体格式遵循]{style="font-family:宋体"}[T3]{lang="EN-US"}[规范]{style="font-family:宋体"}[ANSI T1.107-1995]{lang="EN-US"}[。]{style="font-family:宋体"}

[[通道一次只能发送一种告警信号（包括在使用]{style="font-family:宋体"}**[detect]{lang="EN-US"}**]{#struct_0_x1849_14381_x1885927972}[功能时检测到]{style="font-family:宋体"}[LOS]{lang="EN-US"}[、]{style="font-family:宋体"}[LOF]{lang="EN-US"}[或]{style="font-family:宋体"}[AIS]{lang="EN-US"}[后而产生的]{style="font-family:宋体"}[RAI]{lang="EN-US"}[告警信号），发送另一种告警信号前必须使用]{style="font-family:宋体"}**[undo t3 alarm generate]{lang="EN-US"}**[命令取消前一种告警信号。]{style="font-family:宋体"}**[detect]{lang="EN-US"}**[功能产生的告警信号（]{style="font-family:宋体"}[RAI]{lang="EN-US"}[）必须通过]{style="font-family:宋体"}**[undo t3 alarm detect]{lang="EN-US"}**[命令取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1051665401}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x559358520}[打开]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[通道]{style="font-family:宋体"}[2]{lang="EN-US"}[的告警检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x860776675}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 2 alarm detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1439685896}[在]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[通道]{style="font-family:宋体"}[2]{lang="EN-US"}[上发送]{style="font-family:宋体"}[AIS]{lang="EN-US"}[告警信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1375456785}

[\[Sysname\] controller CPOS 2/4/0]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="PT-BR"}[-Cpos2/4/0\] t3 2 alarm generate ais]{lang="EN-US"}
:::

::: {#-1912733319 .myid}
[]{#_Toc404783884}[]{#struct_0_x1849_14381_x1117130707}[]{#_Toc255917532}[]{#_Toc194725136}[]{#_Toc196130687}[]{#_Toc196622229}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 bert**

------------------------------------------------------------------------

[**[t3]{lang="EN-US"}***[ ]{lang="EN-US"}***[bert]{lang="EN-US"}**]{#struct_0_x1849_14381_1503406778}[命令用来进行线路位（]{style="font-family:宋体"}[Bit]{lang="EN-US"}[）错误率的测试。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **t3** **bert**]{lang="EN-US"}]{#struct_0_x1849_14381_x781906790}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_596586123}

[**[t3]{lang="EN-US"}**[ *t3-number* **bert** **pattern** { **2\^7** \| **2\^11** \| **2\^15** \| **qrss** } **time** *time-number*]{lang="EN-US"}]{#struct_0_x1849_14381_x972114436}

[**[undo t3]{lang="DE"}**]{#struct_0_x1849_14381_2028328039}[ *t3-number* **bert**]{lang="DE"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_924961685}

[[不进行线路位错误率的测试。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1375391249}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1490108277}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1247478308}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2037127126}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1344370679}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x547339272}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1612371336}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x727679357}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[pattern]{lang="EN-US"}**]{#struct_0_x1849_14381_468261649}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，包括]{style="font-family:宋体"}**[2\^7]{lang="EN-US"}**[，]{style="font-family:宋体"}**[2\^11]{lang="EN-US"}**[，]{style="font-family:宋体"}**[2\^15]{lang="EN-US"}**[和]{style="font-family:宋体"}**[qrss]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2\^7]{lang="EN-US"}**]{#struct_0_x1849_14381_1375325713}[：发送的码流长度为]{style="font-family:
宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[7]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2\^11]{lang="EN-US"}**]{#struct_0_x1849_14381_x720727300}[：发送的码流长度为]{style="font-family:
宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[11]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[2\^15]{lang="EN-US"}**]{#struct_0_x1849_14381_2052295903}[：发送的码流长度为]{style="font-family:
宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[15]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[qrss]{lang="EN-US"}**]{#struct_0_x1849_14381_492294471}[：发送码流长度为]{style="font-family:
宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[20]{lang="EN-US"}[次方个]{style="font-family:宋体"}[bit]{lang="EN-US"}[，且码流中不允许连续]{style="font-family:宋体"}[14]{lang="EN-US"}[个以上的]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[time-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x649114841}[：设置]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试的持续时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x151110054}

[[ITU O.151]{lang="EN-US"}]{#struct_0_x1849_14381_761983491}[、]{style="font-family:宋体"}[ITU O.153]{lang="EN-US"}[及]{style="font-family:宋体"}[ANSI T1.403-1999]{lang="EN-US"}[定义了各种]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试模式，目前]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道支持]{style="font-family:宋体"}**[2\^7]{lang="EN-US"}**[，]{style="font-family:宋体"}**[2\^11]{lang="EN-US"}**[，]{style="font-family:宋体"}**[2\^15]{lang="EN-US"}**[和]{style="font-family:宋体"}**[qrss]{lang="EN-US"}**[这几种测试模式。]{style="font-family:宋体"}

[[BERT]{lang="EN-US"}]{#struct_0_x1849_14381_x259604717}[测试方式为，本端发出测试数据流，经过线路某处环回回来，本端检测收到的测试数据流与发出的测试数据流是否一致，位错误率达到多少，从而为用户判断线路状态提供依据。因此，要求线路中某处能环回发出的数据流，如将对端设置为远端环回等。]{style="font-family:宋体"}

[[利用]{style="font-family:宋体"}**[t3]{lang="EN-US"}***[ ]{lang="EN-US"}***[bert]{lang="EN-US"}**]{#struct_0_x1849_14381_1485250654}[命令配置好测试模式，指定测试持续时间，开始测试后，可以查看接口状态中的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果。]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试状态和测试结果的说明详见]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375260177}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1455540918}[在]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[2]{lang="EN-US"}[号通道上执行]{style="font-family:
宋体"}[QRSS]{lang="EN-US"}[格式的]{style="font-family:宋体"}[BERT]{lang="EN-US"}[测试]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1898793616}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 2 bert pattern qrss time 10]{lang="EN-US"}
:::

::::: {#-735022917 .myid}
[]{#_Toc404783885}[]{#struct_0_x1849_14381_188679038}[]{#_Toc255917533}[]{#_Toc194725137}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 clock**

------------------------------------------------------------------------

[**[t3 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_1756198665}[命令用来设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的时钟模式。]{style="font-family:宋体"}

[**[undo t3 clock]{lang="EN-US"}**]{#struct_0_x1849_14381_1873594831}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2016213297}

[**[t3]{lang="EN-US"}**[ *t3-number* **clock** { **master** \| **slave** }]{lang="EN-US"}]{#struct_0_x1849_14381_1607501447}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **clock**]{lang="EN-US"}]{#struct_0_x1849_14381_1376243217}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x812799517}

[[T3]{lang="EN-US"}]{#struct_0_x1849_14381_746652414}[通道的时钟模式为从时钟模式（]{style="font-family:宋体"}**[slave]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x512750573}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_2107364032}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1141446349}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1725011545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1002547326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2030993686}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1376177681}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[master]{lang="EN-US"}**]{#struct_0_x1849_14381_x2028176409}[：设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的时钟模式为主时钟模式。]{style="font-family:宋体"}

[**[slave]{lang="EN-US"}**]{#struct_0_x1849_14381_702655879}[：设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的时钟模式为从时钟模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x487145832}

[[可以为不同的]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1849_14381_1313049453}[通道单独配置时钟模式，使用主时钟模式还是从时钟模式应根据连接的设备确定。例如，与]{style="font-family:宋体"}[SONET/SDH]{lang="EN-US"}[设备连接时，应使用从时钟模式，而如果是设备之间通过光纤直连，则应配置一端使用主时钟模式，另一端使用从时钟模式。]{style="font-family:宋体"}

[[同一]{style="font-family:宋体"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x141347483}[物理接口的不同]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的时钟模式是相互独立的。]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image004.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1849_14381_x2068788754}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[建议将全局下]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_765559067}**[clock]{lang="EN-US"}**[时钟模式和]{style="font-family:KaiTi_GB2312"}[T3]{lang="EN-US"}[通道的时钟模式配置一致。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2081027328}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1375718926}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[3]{lang="EN-US"}[使用主时钟模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_942575568}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 clock master]{lang="EN-US"}
:::::

::::: {#1444835522 .myid}
[]{#_Toc404783886}[]{#struct_0_x1849_14381_1764291518}[]{#_Toc255917534}[]{#_Toc194725138}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 feac**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image004.png){#图片 10 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1849_14381_52807849}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号相关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_441399716}
:::

[ ]{lang="EN-US"}

[**[t3]{lang="EN-US"}**[ **feac**]{lang="EN-US"}]{#struct_0_x1849_14381_1896768370}[命令用来配置]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路信号的检测和传输功能。]{style="font-family:宋体"}

[**[undo t3]{lang="EN-US"}**[ **feac**]{lang="EN-US"}]{#struct_0_x1849_14381_x1624525957}[命令用来取消已有的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1807254303}

[**[t3]{lang="EN-US"}**[ *t3-number* **feac** { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]{lang="EN-US"}]{#struct_0_x1849_14381_1375653390}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **feac** { **detect** \| **generate** { **ds3-los** \| **ds3-ais** \| **ds3-oof** \| **ds3-idle** \| **ds3-eqptfail** \| **loopback** { **ds3-line** \| **ds3-payload** } } }]{lang="EN-US"}]{#struct_0_x1849_14381_1653451111}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_51556338}

[[T3]{lang="EN-US"}]{#struct_0_x1849_14381_x21383419}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路信号检测功能处于打开状态，传输功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1657841044}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1366970511}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x168841682}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1372296811}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1764225258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375587854}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_91716456}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_x1849_14381_x499153919}[：]{style="font-family:宋体"}[T3]{lang="EN-US"}[接口上的定时检测]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路信号功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_x1849_14381_517851090}[：发送]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[信号，包括]{style="font-family:宋体"}**[ds3-los]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-ais]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-oof]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-idle]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ds3-eqptfail]{lang="EN-US"}**[。]{style="font-family:宋体"}

[**[loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_670901352}[：发送环回码，用于激活对端的线路环回（]{style="font-family:宋体"}**[ds3-line]{lang="EN-US"}**[）或者净荷环回（]{style="font-family:宋体"}**[ds3-payload]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x540569145}

[[FEAC]{lang="EN-US"}]{#struct_0_x1849_14381_x463787355}[（]{style="font-family:宋体"}[Far End Alarm and Control signal]{lang="EN-US"}[，远端告警与控制信号）是利用]{style="font-family:宋体"}[C-bit]{lang="EN-US"}[帧格式中第一个子帧中的第三个]{style="font-family:宋体"}[C]{lang="EN-US"}[比特组成的一条数据链路，可用于传输各种告警状态信号，也可用于传输环回控制码，用来激活或者取消对端的环回，进行环回测试。]{style="font-family:宋体"}[ANSI T1.107a]{lang="EN-US"}[中规定，]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[可用于传输多种告警信号，并规定这条链路的数据帧为基于位的]{style="font-family:宋体"}[BOP]{lang="EN-US"}[（]{style="font-family:宋体"}[Bit Oriented Protocol]{lang="EN-US"}[）协议格式。]{style="font-family:宋体"}

[[上电后，]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1849_14381_x1448717919}[接口的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[定时检测功能是打开的，但不发送任何]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[当利用该命令配置远端环回前，最好禁止本端的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}]{#struct_0_x1849_14381_x967001336}[检测，以免发出的环回码在对方配好环回后被返回来，造成本端也配置为环回，引起线路上的环路死锁。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375522318}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_81272219}[打开]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[链路数据检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x2024498807}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 feac detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1815201319}[在]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[上发送]{style="font-family:宋体"}[ds3-los]{lang="EN-US"}[信号。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x2111205173}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 feac generate ds3-los]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_2109485585}[在]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[上发送环回码给对端，设置对端为线路环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x930586900}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 feac generate loopback ds3-line]{lang="EN-US"}
:::::

::: {#-1213342564 .myid}
[]{#_Toc404783887}[]{#struct_0_x1849_14381_1375456782}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 framed**

------------------------------------------------------------------------

[**[t3 framed]{lang="EN-US"}**]{#struct_0_x1849_14381_x1117458387}[命令用来创建成帧模式下，]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对应的串口。]{style="font-family:宋体"}

[**[undo t3 framed]{lang="EN-US"}**]{#struct_0_x1849_14381_x243585780}[命令用来删除该串口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1771392154}

[**[t3]{lang="DE"}**]{#struct_0_x1849_14381_x1142860822}[ *t3-number* **framed**]{lang="DE"}

[**[undo t3]{lang="DE"}**]{#struct_0_x1849_14381_1056743344}[ *t3-number* **framed**]{lang="DE"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x182401309}

[[未创建串口。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1073759867}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1474570729}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1375391246}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1489911669}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_2091891420}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_583849611}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x723444892}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_17510132}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1341634435}

[[在将]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1849_14381_515076389}[通道设置为成帧方式后，系统会自动创建一个串口，名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1149454628}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1375325710}[将]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的第]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道设置为成帧模式，并创建对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x720661764}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 3 framed]{lang="EN-US"}
:::

::: {#-1409100248 .myid}
[]{#_Toc404783888}[]{#struct_0_x1849_14381_x1859750346}[]{#_Toc255917535}[]{#_Toc194725139}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 frame-format**

------------------------------------------------------------------------

[**[t3 ]{lang="SV"}**]{#struct_0_x1849_14381_1779951927}**[frame-format]{lang="SV"}**[命令用来配置]{style="font-family:
宋体"}[T3]{lang="SV"}[接口所使用的帧格式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo t3 frame-format]{lang="SV"}**]{#struct_0_x1849_14381_x2092581050}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_2079448521}

[**[t3]{lang="EN-US"}***[ t3-number]{lang="EN-US"}***[ ]{lang="EN-US"}**]{#struct_0_x1849_14381_x1371306956}**[frame-format ]{lang="SV"}**[{ **c-bit** \| **m23** }]{lang="SV"}

[**[undo]{lang="EN-US"}**[ **t3** *t3-number* **frame-format**]{lang="EN-US"}]{#struct_0_x1849_14381_x1754995305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375260174}

[[T3]{lang="SV"}]{#struct_0_x1849_14381_x1455475382}[接口的帧格式为]{style="font-family:宋体"}[C-bit Parity]{lang="SV"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1504057481}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x141524558}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1666040120}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_322967965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x382581482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x423904914}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1960366254}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[c-bit]{lang="EN-US"}**]{#struct_0_x1849_14381_1376243214}[：设置帧格式为]{style="font-family:宋体"}[C-bit Parity]{lang="EN-US"}[（]{style="font-family:宋体"}[G.704]{lang="EN-US"}[）携带可维护信息（如]{style="font-family:宋体"}[FEAC]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[m23]{lang="SV"}**]{#struct_0_x1849_14381_x812996125}[：]{style="font-family:宋体"}[设置帧格式为]{style="font-family:宋体"}[M23]{lang="SV"}[（]{style="font-family:宋体"}[G.752]{lang="SV"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_751680566}

[[\# ]{lang="SV"}]{#struct_0_x1849_14381_1807174265}[设置]{style="font-family:宋体"}[T3]{lang="SV"}[通道]{style="font-family:
宋体"}[1]{lang="SV"}[的帧格式为]{style="font-family:宋体"}[m23]{lang="SV"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x819071431}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="PT-BR"}[-Cpos2/4/0\] t3 1 frame-format m23]{lang="EN-US"}
:::

::: {#437571911 .myid}
[]{#_Toc404783889}[]{#struct_0_x1849_14381_x58630881}[]{#_Toc255917536}[]{#_Toc194725140}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 loopback**

------------------------------------------------------------------------

[**[t3 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_428122063}[命令用来设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的环回模式。]{style="font-family:宋体"}

[**[undo t3 loopback]{lang="EN-US"}**]{#struct_0_x1849_14381_x2026085708}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1376177678}

[**[t3]{lang="EN-US"}**[ *t3-number* **loopback** { **local** \| **payload** \| **remote** }]{lang="EN-US"}]{#struct_0_x1849_14381_x2028635150}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **loopback**]{lang="EN-US"}]{#struct_0_x1849_14381_x974078501}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x815375165}

[[不进行任何形式的环回。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x173133805}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1951233687}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1290913658}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1871251014}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x956182138}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1375718927}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_942510032}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1753132601}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1849_14381_1713105638}[：使能]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对内自环。]{style="font-family:宋体"}

[**[payload]{lang="EN-US"}**]{#struct_0_x1849_14381_1151886039}[：使能]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对外载荷环回。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x1849_14381_1557948520}[：使能]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对外远端环回。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1452488509}

[[环回功能通常用于进行某些特殊测试，正常工作时不要启动环回。]{style="font-family:宋体"}]{#struct_0_x1849_14381_193479518}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1400123989}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1375653391}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[进行对外载荷环回。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1653385575}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 loopback payload]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1539973587}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display controller cpos t]{lang="EN-US"}**]{#struct_0_x1849_14381_1246177402}**[3]{lang="EN-US"}**
:::

::: {#-1556522096 .myid}
[]{#_Toc404783890}[]{#struct_0_x1849_14381_x450560848}[]{#_Toc255917537}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 mdl**

------------------------------------------------------------------------

[**[t3 mdl]{lang="EN-US"}**]{#struct_0_x1849_14381_x1617169810}[命令用来配置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[链路消息检测与传输功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[t3 mdl]{lang="EN-US"}**]{#struct_0_x1849_14381_x2127514398}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x408327439}

[**[t3]{lang="EN-US"}**[ *t3-number* **mdl** { **data** { **eic** *string* \| **fic** *string* \| **gen-no** *string* \| **lic** *string* \| **pfi** *string* \| **port-no** *string* \| **unit** *string* } \| **detect** \| **generate** { **idle-signal** \| **path** \| **test-signal** } }]{lang="EN-US"}]{#struct_0_x1849_14381_x601338155}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **mdl** \[ **data** \[ **eic** \| **fic** \| **gen-no** \| **lic** \| **pfi** \| **port-no** \| **unit** \] \| **detect** \| **generate** \[ **idle-signal** \| **path** \| **test-signal** \] \]]{lang="EN-US"}]{#struct_0_x1849_14381_1375587855}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_91781992}

[[上电后，]{style="font-family:宋体"}[T3]{lang="EN-US"}]{#struct_0_x1849_14381_1731071168}[通道的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[定时检测功能处于关闭状态，不发送任何消息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x168124283}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1746989861}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_628382759}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_941734079}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1419762855}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1567233445}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1375522319}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[data]{lang="EN-US"}**]{#struct_0_x1849_14381_81337755}[：设置]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息参数，其中]{style="font-family:宋体"}[eic]{lang="EN-US"}[、]{style="font-family:宋体"}[lic]{lang="EN-US"}[、]{style="font-family:宋体"}[fic]{lang="EN-US"}[和]{style="font-family:宋体"}[unit]{lang="EN-US"}[为三类]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息的公有参数，]{style="font-family:宋体"}[pfi]{lang="EN-US"}[、]{style="font-family:宋体"}[port-no]{lang="EN-US"}[和]{style="font-family:宋体"}[gen-no]{lang="EN-US"}[分别为消息]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[的私有参数。]{style="font-family:宋体"}

[**[eic ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_x1214529763}[：]{style="font-family:宋体"}[Equipment ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[fic ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_x1663880737}[：]{style="font-family:宋体"}[Frame ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[gen-no ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_x708998525}[：]{style="font-family:宋体"}[Generator number in test signal message]{lang="EN-US"}[，]{style="font-family:宋体"}[test signal]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lic ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_x2135648608}[：]{style="font-family:宋体"}[Location ID]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[11]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pfi ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_262283813}[：]{style="font-family:宋体"}[Facility ID in path message]{lang="EN-US"}[，]{style="font-family:宋体"}[path]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[port-no ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_1710017227}[：]{style="font-family:宋体"}[Port number in idle signal message]{lang="EN-US"}[，]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[消息的私有参数，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[38]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:宋体"}[line]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[unit ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_x1849_14381_x1834190399}[：]{style="font-family:宋体"}[Unit]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[个字符的字符串，缺省值为]{style="font-family:
宋体"}[line]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[detect]{lang="EN-US"}**]{#struct_0_x1849_14381_1375456783}[：]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道上的定时检测]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息功能。]{style="font-family:宋体"}

[**[generate]{lang="EN-US"}**]{#struct_0_x1849_14381_x1117523923}[：按照]{style="font-family:宋体"}[data]{lang="EN-US"}[中配置的参数定时发送]{style="font-family:宋体"}[MDL]{lang="EN-US"}[消息，包括]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle sig]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[，可以同时发送。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x467208907}

[[MDL]{lang="EN-US"}]{#struct_0_x1849_14381_x1256555574}[（]{style="font-family:宋体"}[Maintenance Data Link]{lang="EN-US"}[，维护数据链路）是利用]{style="font-family:宋体"}[C-bit]{lang="EN-US"}[帧格式中第五个子帧中的]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[C]{lang="EN-US"}[比特组成的一条数据链路，可用于传输一些维护性的消息。]{style="font-family:
宋体"}[ANSI T1.107a]{lang="EN-US"}[中规定，]{style="font-family:宋体"}[MDL]{lang="EN-US"}[可用于传输三种消息：]{style="font-family:宋体"}[path]{lang="EN-US"}[、]{style="font-family:宋体"}[idle signal]{lang="EN-US"}[和]{style="font-family:宋体"}[test signal]{lang="EN-US"}[，并规定这条链路的数据帧为]{style="font-family:宋体"}[LAPD]{lang="EN-US"}[协议格式。]{style="font-family:宋体"}

[[MDL]{lang="EN-US"}]{#struct_0_x1849_14381_x1546953076}[链路的收发状态详见]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道显示部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1243535999}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_631039339}[打开]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1551988429}

[\[Sysname\] controller Cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 mdl detect]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1375391247}[配置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[MDL]{lang="EN-US"}[的]{style="font-family:宋体"}[lic]{lang="EN-US"}[参数为字符串"]{style="font-family:宋体"}[hello]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1489977205}

[\[Sysname\] controller Cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 mdl data lic hello]{lang="EN-US"}

[[\# ]{lang="DE"}]{#struct_0_x1849_14381_1772445034}[设置]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[发送]{style="font-family:宋体"}[path]{lang="DE"}[消息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x870346154}

[\[Sysname\] controller Cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 mdl generate path]{lang="EN-US"}
:::

::: {#-387417986 .myid}
[]{#_Toc255917538}[]{#_Toc173120900}[]{#_Toc130049687}[]{#_Toc129668368}[]{#_Toc129527974}[]{#_Toc82589828}[]{#_Toc74652476}[]{#_Toc404783891}[]{#struct_0_x1849_14381_1932246469}

**CPOS接口 \-- CPOS接口配置命令 \-- t3 shutdown**

------------------------------------------------------------------------

[**[t3 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x904844247}[命令用来关闭]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[**[undo t3 shutdown]{lang="EN-US"}**]{#struct_0_x1849_14381_x2082814898}[命令用来打开]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375325711}

[**[t3]{lang="EN-US"}**[ *t3-number* **shutdown**]{lang="EN-US"}]{#struct_0_x1849_14381_x720596228}

[**[undo t3]{lang="EN-US"}**[ *t3-number* **shutdown**]{lang="EN-US"}]{#struct_0_x1849_14381_1294473220}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x574817702}

[[T3]{lang="EN-US"}]{#struct_0_x1849_14381_x868857335}[通道处于打开状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_86135302}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1012725292}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1001153166}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x544297166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_487639454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1375260175}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x1455409846}[：]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x445703751}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_298360019}[关闭]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1010723628}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] t3 1 shutdown]{lang="EN-US"}
:::

::::: {#-1291593385 .myid}
[]{#_Toc404783892}[]{#struct_0_x1849_14381_9938677}

**CPOS接口 \-- CPOS接口配置命令 \-- threshold**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image005.jpg){#图片 9 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1171609485}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_1570231355}
:::

[ ]{lang="EN-US"}

[**[threshold]{lang="EN-US"}**]{#struct_0_x1849_14381_1376243215}[命令用来设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限和]{style="font-family:宋体"}[（]{style="font-family:宋体"}[或]{style="font-family:宋体"}[）]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限。]{style="font-family:宋体"}

[**[undo threshold]{lang="EN-US"}**]{#struct_0_x1849_14381_x812930589}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1196633334}

[**[threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1849_14381_x29259608}[{ **sd** *sdvalue* \| **sf** *sfvalue* } \*]{lang="FR"}

[**[undo threshold]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1849_14381_287313732}[\[ **sd** \| **sf** \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x501715158}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x1841678194}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1471040758}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_1992176906}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1376177679}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x2028700686}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1236814369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x524899322}

[**[sd]{lang="EN-US"}**]{#struct_0_x1849_14381_x62448816}[：表示配置]{style="font-family:宋体"}[SD]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Degrade]{lang="EN-US"}[，信号衰减）告警门限。]{style="font-family:宋体"}

[*[sd]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x1849_14381_1953998389}[：以]{style="font-family:宋体"}[10e-sd*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sd]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SD]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[**[sf]{lang="EN-US"}**]{#struct_0_x1849_14381_x814692150}[：表示配置]{style="font-family:宋体"}[SF]{lang="EN-US"}[（]{style="font-family:宋体"}[Signal Fail]{lang="EN-US"}[，信号失败）告警门限。]{style="font-family:宋体"}

[*[sf]{lang="FR"}[value]{lang="EN-US"}*]{#struct_0_x1849_14381_x1305941588}[：以]{style="font-family:宋体"}[10e-sf*value*]{lang="EN-US"}[的形式表示的]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警门限值，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}*[sf]{lang="FR"}[value]{lang="EN-US"}*[值越大表示]{style="font-family:
宋体"}[SF]{lang="FR"}[告警门限越小。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x262849866}

[[SD]{lang="EN-US"}]{#struct_0_x1849_14381_1375718924}[告警和]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警都是用于指示当前线路性能的，相比较而言，]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警比]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警更为严重，]{style="font-family:宋体"}[SF]{lang="EN-US"}[的误码率门限一般会比]{style="font-family:宋体"}[SD]{lang="EN-US"}[的误码率门限高，也就是说，当出现少量误码时，设备产生]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警，当误码率增大到一定程度时，说明线路质量严重下降，此时设备才产生]{style="font-family:宋体"}[SF]{lang="EN-US"}[告警。因此，应使]{style="font-family:宋体"}[SD]{lang="EN-US"}[的告警门限小于]{style="font-family:宋体"}[SF]{lang="EN-US"}[的告警门限，]{style="font-family:宋体"}*[sdvalue]{lang="EN-US"}*[的值应大于]{style="font-family:宋体"}*[sfvalue]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_942706640}

[[\#]{lang="EN-US"}]{#struct_0_x1849_14381_x1452185550}[[ ]{lang="EN-US"}]{#_Toc74621539}[设置]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[SD]{lang="EN-US"}[告警门限]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10e-4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x66967061}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] threshold sd 4]{lang="EN-US"}
:::::

::: {#1873657652 .myid}
[]{#_Toc404783893}[]{#struct_0_x1849_14381_x5561978}[]{#_Toc255917539}[]{#_Toc194725119}

**CPOS接口 \-- CPOS接口配置命令 \-- using e3**

------------------------------------------------------------------------

[**[using e3]{lang="EN-US"}**]{#struct_0_x1849_14381_1422451596}[命令用来创建非成帧模式的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对应的串口。]{style="font-family:宋体"}

[**[undo using e3]{lang="EN-US"}**]{#struct_0_x1849_14381_x831084546}[命令用来删除该串口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_639110975}

[**[using e3 ]{lang="EN-US"}***[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1375653388}

[**[undo using e3 ]{lang="EN-US"}***[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1652926824}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x685283255}

[[未创建串口。]{style="font-family:宋体"}]{#struct_0_x1849_14381_529649577}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1552505341}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x1574386699}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[155Mbps]{lang="PT-BR"}[通道视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x903191696}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x372021901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x2097050368}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_578963592}

[*[e3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1375587852}[：]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_91585384}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_778091281}[接口视图下，创建非成帧模式的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对应的串口名称]{style="font-family:宋体"}[为]{lang="EN-US" style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/E3]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:]{lang="EN-US"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[155Mbps]{lang="PT-BR"}]{#struct_0_x1849_14381_x1087191799}[通道视图下，创建非成帧模式的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道对应的串口名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/155Mbps]{lang="EN-US"}[通道号]{style="font-family:宋体"}[/E3]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1326680675}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1173752025}[在]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[下创建非成帧模式的]{style="font-family:宋体"}[E3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1875271392}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] using e3 1]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0\] interface serial 2/4/0/1:0]{lang="PT-BR"}

[\[Sysname-Serial2/4/0/1:0\]]{lang="PT-BR"}

[[\# ]{lang="PT-BR"}]{#struct_0_x1849_14381_x1087126263}[在]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口]{style="font-family:宋体"}[2/4/0]{lang="PT-BR"}[的]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道下创建非成帧模式的]{style="font-family:宋体"}[E3]{lang="PT-BR"}[通道]{style="font-family:宋体"}[1]{lang="PT-BR"}[对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1086536439}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] oc-3 2]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-3-2\] using e3 1]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-3-2\] interface serial 2/4/0/2/1:0]{lang="PT-BR"}

[\[Sysname-Serial2/4/0]{lang="EN-US"}[/2]{lang="PT-BR"}[/1:0\]]{lang="EN-US"}
:::

::::: {#-963958829 .myid}
[]{#_Toc404783894}[]{#struct_0_x1849_14381_1190844177}

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-12/using oc-12c**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){#图片 5 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1086470903}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_635714398}
:::

**[ ]{lang="PT-BR"}**

[**[using oc-12]{lang="PT-BR"}**]{#struct_0_x1849_14381_1028172130}[命令用来配置]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[通道的工作模式为通道模式。]{style="font-family:宋体"}

[**[using oc-12c]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1087060728}[命令用来配置]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[622Mbps]{lang="PT-BR"}[通道的工作模式为级联模式。]{style="font-family:宋体"}

[**[undo using]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1304931453}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x41461442}

[**[using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x1086995192}[ { **oc-12** \| **oc-12c** }]{lang="ES-AR"}

[**[undo using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x583654351}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2122836068}

[[接口或通道工作在通道模式。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x400598477}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1086929656}

[[622Mbps]{lang="EN-US"}]{#struct_0_x1849_14381_x1162053609}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/622Mbps]{lang="EN-US"}[通道视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1023202923}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1086864120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1142903094}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x2021207008}

[[在]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}]{#struct_0_x1849_14381_x1087322872}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图或者]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道视图下通过]{style="font-family:宋体"}**[using oc-12c]{lang="EN-US"}**[命令设置接口或通道为级联模式后，系统会自动创建一个]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的名称为：]{style="font-family:宋体"}[Pos]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[\[/622Mbps]{lang="EN-US"}[通道号]{style="font-family:宋体"}[\]:0]{lang="EN-US"}

[[配置]{style="font-family:宋体"}**[using oc-12]{lang="EN-US"}**]{#struct_0_x1849_14381_x1993366126}[或者]{style="font-family:宋体"}**[undo using]{lang="EN-US"}**[命令会设置接口为通道模式，并删除级联模式下创建的]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x778674770}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x120007377}[配置]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为级联模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1087257336}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] using oc-12c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1692871018}[配置]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为通道模式。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0\] using oc-12]{lang="EN-US"}]{#struct_0_x1849_14381_x1087191800}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_60427601}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道的工作模式为级联模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1093481261}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] oc-12 1]{lang="EN-US"}

[\[Sysname-Cpos2/4/0-oc-12-1\] using oc-12c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1235936140}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[通道的工作模式为通道模式。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0-oc-12-1\] undo using]{lang="EN-US"}]{#struct_0_x1849_14381_x1087126264}
:::::

::::: {#-95869877 .myid}
[]{#_Toc404783895}[]{#struct_0_x1849_14381_2026594606}

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-3/using oc-3c**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){#图片 7 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1222486762}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_x1086536440}
:::

[ ]{lang="PT-BR"}

[**[using oc-3]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1894597218}[命令用来配置]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道的工作模式为通道模式。]{style="font-family:宋体"}

[**[using oc-3c]{lang="PT-BR"}**]{#struct_0_x1849_14381_269575032}[命令用来配置]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口或]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道的工作模式为级联模式。]{style="font-family:宋体"}

[**[undo using]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1086470904}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x930369543}

[**[using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x40955277}[ { **oc-3** \| **oc-3c** }]{lang="ES-AR"}

[**[undo using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x1087060729}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_261152488}

[[接口或通道工作在通道模式。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1911737130}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1086995193}

[[155Mbps]{lang="EN-US"}]{#struct_0_x1849_14381_2145229004}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[155Mbps]{lang="PT-BR"}[通道视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1206103930}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x980177518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1086929657}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_404030332}

[[在]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}]{#struct_0_x1849_14381_x1885816297}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口视图或者]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道视图下通过]{style="font-family:宋体"}**[using oc-3c]{lang="EN-US"}**[命令设置接口为级联模式后，系统会自动创建一个]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[的]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的名称为：]{style="font-family:宋体"}[Pos]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[\[ \[/622Mbps]{lang="EN-US"}[通道号]{style="font-family:宋体"}[\]/155Mbps]{lang="EN-US"}[通道号]{style="font-family:宋体"}[\]:0]{lang="EN-US"}

[[配置]{style="font-family:宋体"}**[using oc-3]{lang="EN-US"}**]{#struct_0_x1849_14381_x1086864121}[或者]{style="font-family:宋体"}**[undo using]{lang="EN-US"}**[命令会设置接口为通道模式，并删除级联模式下创建的]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_423180847}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_705864579}[配置]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为级联模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1087322873}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] using oc-3c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x427282185}[配置]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为通道模式。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0\] using oc-3]{lang="EN-US"}]{#struct_0_x1849_14381_x725685788}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1087257337}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道的工作模式为级联模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1036012337}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] oc-12 1]{lang="EN-US"}

[\[Sysname-Cpos2/4/0-oc-12-1\] oc-3 1]{lang="EN-US"}

[\[Sysname-Cpos2/4/0-oc-12-1-oc-3-1\] using oc-3c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_866254418}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[通道的工作模式为通道模式。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0-oc-12-1-oc-3-1\] undo using]{lang="EN-US"}]{#struct_0_x1849_14381_x1087191801}
:::::

::::: {#-1250670394 .myid}
[]{#_Toc296086943}[]{#_Toc205801707}[]{#_Toc404783896}[]{#struct_0_x1849_14381_x1505656340}

**CPOS接口 \-- CPOS接口配置命令 \-- using oc-48/using oc-48c**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](CPOS接口命令.files/image002.png){#图片 1 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x1849_14381_x1693531309}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1849_14381_x1087126265}
:::

[ ]{lang="EN-US"}

[**[using oc-48]{lang="PT-BR"}**]{#struct_0_x1849_14381_x702288749}[命令用来配置]{style="font-family:宋体"}[2.5Gbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口的工作模式为通道模式。]{style="font-family:宋体"}

[**[using oc-48c]{lang="PT-BR"}**]{#struct_0_x1849_14381_1413715347}[命令用来配置]{style="font-family:宋体"}[2.5Gbps]{lang="PT-BR"}[高速]{style="font-family:宋体"}[CPOS]{lang="PT-BR"}[接口的工作模式为级联模式。]{style="font-family:宋体"}

[**[undo using]{lang="PT-BR"}**]{#struct_0_x1849_14381_x1086536441}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_834286137}

[**[using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x38743291}[ { **oc-48** \| **oc-48c** }]{lang="ES-AR"}

[**[undo using]{lang="ES-AR"}**]{#struct_0_x1849_14381_x1086470905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1798513812}

[[接口工作在通道模式。]{style="font-family:宋体"}]{#struct_0_x1849_14381_1707342391}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_806501069}

[[2.5Gbps]{lang="ES-AR"}]{#struct_0_x1849_14381_x1087060730}[高速]{style="font-family:宋体"}[CPOS]{lang="ES-AR"}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1661096277}

[[network-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_51105757}

[[mdc-admin]{lang="ES-AR"}]{#struct_0_x1849_14381_x1086995194}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1746453765}

[[通过]{style="font-family:宋体"}]{#struct_0_x1849_14381_x194983107}**[using oc-48c]{lang="ES-AR"}**[命令设置接口为级联模式后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[系统会自动创建一个]{style="font-family:宋体"}[2.5G]{lang="ES-AR"}[bps]{lang="PT-BR"}[的]{style="font-family:宋体"}[POS]{lang="ES-AR"}[通道接口。]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口的名称为：]{style="font-family:宋体"}[Pos]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[using oc-48]{lang="EN-US"}**]{#struct_0_x1849_14381_x1086929658}[或者]{style="font-family:宋体"}**[undo using]{lang="EN-US"}**[命令会设置接口为通道模式，并删除级联模式下创建的]{style="font-family:宋体"}[POS]{lang="EN-US"}[通道接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1968622663}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x16318568}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为级联模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1086864122}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] using oc-48c]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1989264788}[配置]{style="font-family:宋体"}[2.5Gbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS2/4/0]{lang="EN-US"}[接口的工作模式为通道模式。]{style="font-family:宋体"}

[[\[Sysname-Cpos2/4/0\] using oc-48]{lang="EN-US"}]{#struct_0_x1849_14381_x214283752}
:::::

::: {#-404887009 .myid}
[]{#_Toc404783897}[]{#struct_0_x1849_14381_x1837180739}[]{#_Toc255917540}[]{#_Toc194725133}

**CPOS接口 \-- CPOS接口配置命令 \-- using t3**

------------------------------------------------------------------------

[**[using t3]{lang="EN-US"}**]{#struct_0_x1849_14381_1383337410}[命令用来创建非成帧模式的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对应的串口。]{style="font-family:宋体"}

[**[undo using t3]{lang="EN-US"}**]{#struct_0_x1849_14381_1375522316}[命令用来删除该串口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1849_14381_80354715}

[**[using t3 ]{lang="EN-US"}***[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_1385075080}

[**[undo using ]{lang="EN-US"}***[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x561660303}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1248141701}

[[未创建串口。]{style="font-family:宋体"}]{#struct_0_x1849_14381_x234571694}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x1483641374}

[[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x436025015}[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}[155Mbps]{lang="PT-BR"}[通道视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1849_14381_229874343}

[[network-admin]{lang="EN-US"}]{#struct_0_x1849_14381_1375456780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1849_14381_x1117327315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1849_14381_887699853}

[*[t3-number]{lang="EN-US"}*]{#struct_0_x1849_14381_x314922272}[：]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1849_14381_x608048697}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CPOS]{lang="EN-US"}]{#struct_0_x1849_14381_x354052786}[接口视图下，创建非成帧模式的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对应的串口名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/T3]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:]{lang="EN-US"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[155Mbps]{lang="PT-BR"}]{#struct_0_x1849_14381_x1087126266}[通道视图下，创建非成帧模式的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道对应的串口名称为]{style="font-family:宋体"}[Serial]{lang="EN-US"}[接口编号]{style="font-family:宋体"}[/155Mbps]{lang="EN-US"}[通道号]{style="font-family:宋体"}[/T3]{lang="EN-US"}[通道号]{style="font-family:宋体"}[:0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1849_14381_1937508455}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_1941092685}[在]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[下创建非成帧模式的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_1375391244}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] using t3 1]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] interface serial 2/4/0/1:0]{lang="EN-US"}

[]{#_Toc171825216}[]{#_Toc171825217}[\[Sysname-Serial2/4/0/1:0\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1849_14381_x1086536442}[在]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[高速]{style="font-family:宋体"}[CPOS]{lang="EN-US"}[接口]{style="font-family:宋体"}[2/4/0]{lang="EN-US"}[的]{style="font-family:宋体"}[155Mbps]{lang="PT-BR"}[通道下创建非成帧模式的]{style="font-family:宋体"}[T3]{lang="EN-US"}[通道]{style="font-family:宋体"}[1]{lang="EN-US"}[对应的串口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1849_14381_x1086470906}

[\[Sysname\] controller cpos 2/4/0]{lang="EN-US"}

[\[Sysname-Cpos2/4/0\] oc-3 2]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-3-2\] using t3 1]{lang="PT-BR"}

[\[Sysname-Cpos2/4/0-oc-3-2\] interface serial 2/4/0/2/1:0]{lang="PT-BR"}

[\[Sysname-Serial2/4/0]{lang="EN-US"}[/2]{lang="PT-BR"}[/1:0\]]{lang="EN-US"}
:::
