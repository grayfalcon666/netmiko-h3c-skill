::::: {#1083034321 .myid}
[]{#_Toc404791876}[]{#struct_0_x4306_x6993_x997131183}[]{#_Toc384729417}

**ACL \-- ACL配置命令 \-- accelerate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x997196719}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1413345575}
:::

**[ ]{lang="EN-US"}**

[**[accelerate]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1259514704}[命令用来开启]{style="font-family:宋体"}[ACL]{lang="EN-US"}[加速功能。]{style="font-family:宋体"}

[**[undo accelerate]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1889066133}[命令用来关闭]{style="font-family:宋体"}[ACL]{lang="EN-US"}[加速功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2084712506}

[**[accelerate]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1829957201}

[**[undo accelerate ]{lang="EN-US"}**]{#struct_0_x4306_x6993_389087232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_299066763}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_884130056}[加速功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x997655470}

[[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x281705415}[视图]{style="font-family:宋体"}[/IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1649898475}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1067426776}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1395530276}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_356341765}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1595421686}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1247703081}[开启]{style="font-family:宋体"}[ACL]{lang="EN-US"}[加速功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x997721006}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl]{lang="EN-US"}[-ipv4-basic-2000\] accelerate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1833913939}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x4306_x6993_x1902260767}[**[display acl accelerate]{lang="EN-US" style="color:windowtext;text-decoration:none"}**](?1615842176#_Toc303849088)
:::::

::: {#-1385388067 .myid}
[]{#_Toc404791877}[]{#struct_0_x4306_x6993_x474436175}

**ACL \-- ACL配置命令 \-- acl**

------------------------------------------------------------------------

[**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_1687141926}[命令用来创建一个]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入相应的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_801565679}[命令用来删除指定或全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x847524340}

[**[acl]{lang="EN-US"}**[ \[ **ipv6** \] { **advanced** \| **basic** } { *acl-number* \| **name** *acl-name* } \[ **match-order** { **auto** \| **config** } \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1204747404}

[**[acl]{lang="EN-US"}**[ **mac** { *acl-number* \| **name** *acl-name* } \[ **match-order** { **auto** \| **config** } \]]{lang="EN-US"}]{#struct_0_x4306_x6993_1198000345}

[**[acl]{lang="EN-US"}**[ **user-defined** { *acl-number* \| **name** *acl-name* } ]{lang="EN-US"}]{#struct_0_x4306_x6993_x2128914255}

[**[undo]{lang="EN-US"}**[ **acl** \[ **ipv6** \] { **all** \| { **advanced** \| **basic** } { *acl-number* \| **name** *acl-name* } }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1532985486}

[**[undo]{lang="EN-US"}**[ **acl** **mac** { **all** \| *acl-number* \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1815763166}

[**[undo]{lang="EN-US"}**[ **acl** **user-defined** { **all** \| *acl-number* \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1529515663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1853726771}

[[不存在任何]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x784533983}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x23867337}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2119784305}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1208497423}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x695933235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_697354425}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x847983091}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_304765017}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[basic]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1871037541}[：指定创建基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[advanced]{lang="EN-US"}**]{#struct_0_x4306_x6993_1355410938}[：指定创建高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_1078242012}[：指定创建二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x844072289}[：指定创建用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[number]{lang="EN-US"}**[ *acl-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1738957535}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x621687943}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[：表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_1497533698}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x429917630}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_x2041082591}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_883648842}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[match-order]{lang="EN-US"}**[ { **auto** \| **config** }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1378626794}[：指定规则的匹配顺序，]{style="font-family:宋体"}**[auto]{lang="EN-US"}**[表示按照自动排序（即"深度优先"原则）的顺序进行规则匹配，]{style="font-family:宋体"}**[config]{lang="EN-US"}**[表示按照配置顺序进行规则匹配。缺省情况下，规则的匹配顺序为配置顺序。用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不支持本参数，其规则匹配顺序只能为配置顺序。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4306_x6993_1091898722}[：指定类型中全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x848048627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x11029180}**[acl]{lang="EN-US"}**[命令时，如果指定编号或名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[不存在，则创建该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[并进入其视图，否则直接进入其视图。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1349067617}[ACL]{lang="EN-US"}[内不存在任何规则时，用户可以使用本命令对该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序进行修改，否则不允许进行修改。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1174587114}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x414516018}

[]{#_Toc86742803}[]{#_Toc80178009}[]{#_Toc80177403}[]{#_Toc58993697}[]{#_Toc145489037}[]{#_Toc155337055}[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x2126136395}[创建一个编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[]{#struct_0_x4306_x6993_x1145695219}[]{#_Toc120681079}[]{#_Toc120681080}[]{#_Toc120681087}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1703416777}[创建一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，指定其名称为]{style="font-family:宋体"}[flow]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x847852019}

[\[Sysname\] acl basic name flow]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-flow\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x305564318}[创建一个编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_794674096}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1554296241}[创建一个编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_636774836}

[[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}]{#struct_0_x4306_x6993_1065652326}

[[\[Sysname-acl-ipv6-basic-2000\]]{lang="EN-US"}]{#struct_0_x4306_x6993_x876659522}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1226369356}[创建一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，其名称为]{style="font-family:宋体"}[flow]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1339247987}

[[\[Sysname\] acl ipv6 basic name flow]{lang="EN-US"}]{#struct_0_x4306_x6993_1911666564}

[[\[Sysname-acl-ipv6-basic-flow\]]{lang="EN-US"}]{#struct_0_x4306_x6993_x116396525}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1871648259}[创建一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，其名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1580939088}

[\[Sysname\] acl ipv6 advanced name abc]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-abc\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1299757940}[创建一个编号为]{style="font-family:宋体"}[4000]{lang="EN-US"}[的二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1325609749}

[[\[Sysname\] acl mac 4000]{lang="EN-US"}]{#struct_0_x4306_x6993_1957580768}

[[\[Sysname-acl-mac-4000\]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1402002328}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1923148158}[创建一个二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，其名称为]{style="font-family:宋体"}[flow]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_2043238106}

[[\[Sysname\] acl mac name flow]{lang="EN-US"}]{#struct_0_x4306_x6993_x2046960661}

[[\[Sysname-acl-mac-flow\]]{lang="EN-US"}]{#struct_0_x4306_x6993_1444231730}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1515876651}[创建一个编号为]{style="font-family:宋体"}[5000]{lang="EN-US"}[的用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x291160379}

[\[Sysname\] acl user-defined 5000]{lang="EN-US"}

[\[Sysname-acl-user-5000\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1993811357}[创建一个用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，其名称为]{style="font-family:宋体"}[flow]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x797318387}

[\[Sysname\] acl user-defined name flow]{lang="EN-US"}

[\[Sysname-acl-user-flow\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x191813477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x775436075}
:::

::::: {#1768707092 .myid}
[]{#_Toc404791878}[]{#struct_0_x4306_x6993_x223953369}

**ACL \-- ACL配置命令 \-- acl copy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 1 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_1241866120}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x2005235922}
:::

[ ]{lang="EN-US"}

[**[acl]{lang="EN-US"}**[ **copy**]{lang="EN-US"}]{#struct_0_x4306_x6993_x49240456}[命令用来复制并生成一个新的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1398474601}

[**[acl]{lang="EN-US"}**[ \[ **ipv6** \| **mac** \| **user-defined** \] **copy** { *source-acl-number* \| **name** *source-acl-name* } **to** { *dest-acl-number* \| **name** *dest-acl-name* }]{lang="EN-US"}]{#struct_0_x4306_x6993_x850636646}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x847917555}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1410976425}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_873786674}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1055934073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x818589311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2038693188}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_391496827}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_1552457819}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_811398224}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[source-acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_1656318161}[：指定源]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[必须存在。本参数的取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1033057779}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_56278179}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x847720947}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_159388013}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *source-acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1510168487}[：指定源]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[必须存在。]{style="font-family:宋体"}*[source-acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[dest-acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_x132273707}[：指定目的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[必须不存在。本参数的取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_913266316}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_1299293974}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_635370271}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_2065833294}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *dest-acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x99900387}[：指定目的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[必须不存在。]{style="font-family:宋体"}*[dest-acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:
宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x847786483}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[目的]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1031689687}[ACL]{lang="EN-US"}[的类型要与源]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的类型相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[除了]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x654307550}[ACL]{lang="EN-US"}[的编号或名称不同外，新生成的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[（即目的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[）的匹配顺序、规则匹配统计功能的使能情况、规则编号的步长、所包含的规则、规则的描述信息以及]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的描述信息等都与源]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1151011714}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1482211845}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1106056109}[通过复制已存在的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[，来生成一个新的编号为]{style="font-family:宋体"}[2002]{lang="EN-US"}[的同类型]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x155333459}

[\[Sysname\] acl copy 2001 to 2002]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x392908683}[通过复制已存在的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL test]{lang="EN-US"}[，来生成名为]{style="font-family:宋体"}[paste]{lang="EN-US"}[的同类型]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<]{lang="EN-US" style="font-size:10.0pt;font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x1805352518}[Sysname]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[\> ]{lang="EN-US" style="font-size:10.0pt;font-family:\"Courier New\""}[system]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[-]{lang="EN-US" style="font-size:10.0pt;font-family:\"Courier New\""}[view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\[]{lang="EN-US" style="font-size:10.0pt"}[Sysname]{lang="EN-US"}]{#struct_0_x4306_x6993_x2074923072}[\] ]{lang="EN-US" style="font-size:10.0pt"}[acl copy name test to name paste]{lang="EN-US"}
:::::

::::: {#-947221733 .myid}
[]{#_Toc404791879}[]{#struct_0_x4306_x6993_x1825991588}[]{#_Toc303848435}[]{#_Toc303849003}[]{#_Toc303849942}[]{#_Toc303857542}[]{#_Toc303848436}[]{#_Toc303849004}[]{#_Toc303849943}[]{#_Toc303857543}[]{#_Toc303848437}[]{#_Toc303849005}[]{#_Toc303849944}[]{#_Toc303857544}[]{#_Toc303848438}[]{#_Toc303849006}[]{#_Toc303849945}[]{#_Toc303857545}[]{#_Toc303848439}[]{#_Toc303849007}[]{#_Toc303849946}[]{#_Toc303857546}[]{#_Toc303848440}[]{#_Toc303849008}[]{#_Toc303849947}[]{#_Toc303857547}[]{#_Toc303848441}[]{#_Toc303849009}[]{#_Toc303849948}[]{#_Toc303857548}[]{#_Toc303848442}[]{#_Toc303849010}[]{#_Toc303849949}[]{#_Toc303857549}[]{#_Toc303848443}[]{#_Toc303849011}[]{#_Toc303849950}[]{#_Toc303857550}[]{#_Toc303848444}[]{#_Toc303849012}[]{#_Toc303849951}[]{#_Toc303857551}[]{#_Toc303848445}[]{#_Toc303849013}[]{#_Toc303849952}[]{#_Toc303857552}[]{#_Toc303848446}[]{#_Toc303849014}[]{#_Toc303849953}[]{#_Toc303857553}[]{#_Toc303848447}[]{#_Toc303849015}[]{#_Toc303849954}[]{#_Toc303857554}[]{#_Toc303848448}[]{#_Toc303849016}[]{#_Toc303849955}[]{#_Toc303857555}[]{#_Toc303848449}[]{#_Toc303849017}[]{#_Toc303849956}[]{#_Toc303857556}[]{#_Toc303848450}[]{#_Toc303849018}[]{#_Toc303849957}[]{#_Toc303857557}[]{#_Toc303848451}[]{#_Toc303849019}[]{#_Toc303849958}[]{#_Toc303857558}[]{#_Toc303848452}[]{#_Toc303849020}[]{#_Toc303849959}[]{#_Toc303857559}[]{#_Toc303848453}[]{#_Toc303849021}[]{#_Toc303849960}[]{#_Toc303857560}[]{#_Toc303848454}[]{#_Toc303849022}[]{#_Toc303849961}[]{#_Toc303857561}[]{#_Toc303848455}[]{#_Toc303849023}[]{#_Toc303849962}[]{#_Toc303857562}[]{#_Toc303848456}[]{#_Toc303849024}[]{#_Toc303849963}[]{#_Toc303857563}[]{#_Toc303848457}[]{#_Toc303849025}[]{#_Toc303849964}[]{#_Toc303857564}[]{#_Toc303848458}[]{#_Toc303849026}[]{#_Toc303849965}[]{#_Toc303857565}[]{#_Toc303848459}[]{#_Toc303849027}[]{#_Toc303849966}[]{#_Toc303857566}[]{#_Toc303848460}[]{#_Toc303849028}[]{#_Toc303849967}[]{#_Toc303857567}[]{#_Toc303848461}[]{#_Toc303849029}[]{#_Toc303849968}[]{#_Toc303857568}[]{#_Toc120681108}[]{#_Toc120681109}[]{#_Toc120681116}[]{#_Toc303848462}[]{#_Toc303849030}[]{#_Toc303849969}[]{#_Toc303857569}[]{#_Toc303848463}[]{#_Toc303849031}[]{#_Toc303849970}[]{#_Toc303857570}[]{#_Toc303848464}[]{#_Toc303849032}[]{#_Toc303849971}[]{#_Toc303857571}[]{#_Toc303848465}[]{#_Toc303849033}[]{#_Toc303849972}[]{#_Toc303857572}[]{#_Toc303848466}[]{#_Toc303849034}[]{#_Toc303849973}[]{#_Toc303857573}[]{#_Toc303848467}[]{#_Toc303849035}[]{#_Toc303849974}[]{#_Toc303857574}[]{#_Toc303848468}[]{#_Toc303849036}[]{#_Toc303849975}[]{#_Toc303857575}[]{#_Toc303848469}[]{#_Toc303849037}[]{#_Toc303849976}[]{#_Toc303857576}[]{#_Toc303848470}[]{#_Toc303849038}[]{#_Toc303849977}[]{#_Toc303857577}[]{#_Toc303848471}[]{#_Toc303849039}[]{#_Toc303849978}[]{#_Toc303857578}[]{#_Toc303848472}[]{#_Toc303849040}[]{#_Toc303849979}[]{#_Toc303857579}[]{#_Toc303848473}[]{#_Toc303849041}[]{#_Toc303849980}[]{#_Toc303857580}[]{#_Toc303848474}[]{#_Toc303849042}[]{#_Toc303849981}[]{#_Toc303857581}[]{#_Toc303848475}[]{#_Toc303849043}[]{#_Toc303849982}[]{#_Toc303857582}[]{#_Toc303848476}[]{#_Toc303849044}[]{#_Toc303849983}[]{#_Toc303857583}[]{#_Toc303848477}[]{#_Toc303849045}[]{#_Toc303849984}[]{#_Toc303857584}[]{#_Toc303848478}[]{#_Toc303849046}[]{#_Toc303849985}[]{#_Toc303857585}[]{#_Toc303848479}[]{#_Toc303849047}[]{#_Toc303849986}[]{#_Toc303857586}[]{#_Toc303848480}[]{#_Toc303849048}[]{#_Toc303849987}[]{#_Toc303857587}[]{#_Toc303848481}[]{#_Toc303849049}[]{#_Toc303849988}[]{#_Toc303857588}[]{#_Toc303848482}[]{#_Toc303849050}[]{#_Toc303849989}[]{#_Toc303857589}[]{#_Toc303848483}[]{#_Toc303849051}[]{#_Toc303849990}[]{#_Toc303857590}[]{#_Toc303848484}[]{#_Toc303849052}[]{#_Toc303849991}[]{#_Toc303857591}[]{#_Toc303848485}[]{#_Toc303849053}[]{#_Toc303849992}[]{#_Toc303857592}[]{#_Toc303848486}[]{#_Toc303849054}[]{#_Toc303849993}[]{#_Toc303857593}[]{#_Toc303848487}[]{#_Toc303849055}[]{#_Toc303849994}[]{#_Toc303857594}[]{#_Toc303848488}[]{#_Toc303849056}[]{#_Toc303849995}[]{#_Toc303857595}[]{#_Toc303848489}[]{#_Toc303849057}[]{#_Toc303849996}[]{#_Toc303857596}[]{#_Toc303848490}[]{#_Toc303849058}[]{#_Toc303849997}[]{#_Toc303857597}[]{#_Toc303848491}[]{#_Toc303849059}[]{#_Toc303849998}[]{#_Toc303857598}[]{#_Toc303848492}[]{#_Toc303849060}[]{#_Toc303849999}[]{#_Toc303857599}[]{#_Toc303848493}[]{#_Toc303849061}[]{#_Toc303850000}[]{#_Toc303857600}[]{#_Toc303848494}[]{#_Toc303849062}[]{#_Toc303850001}[]{#_Toc303857601}[]{#_Toc303848495}[]{#_Toc303849063}[]{#_Toc303850002}[]{#_Toc303857602}[]{#_Toc303848496}[]{#_Toc303849064}[]{#_Toc303850003}[]{#_Toc303857603}[]{#_Toc303848497}[]{#_Toc303849065}[]{#_Toc303850004}[]{#_Toc303857604}[]{#_Toc303848498}[]{#_Toc303849066}[]{#_Toc303850005}[]{#_Toc303857605}[]{#_Toc303848499}[]{#_Toc303849067}[]{#_Toc303850006}[]{#_Toc303857606}[]{#_Toc303848500}[]{#_Toc303849068}[]{#_Toc303850007}[]{#_Toc303857607}[]{#_Toc303848501}[]{#_Toc303849069}[]{#_Toc303850008}[]{#_Toc303857608}[]{#_Toc303848502}[]{#_Toc303849070}[]{#_Toc303850009}[]{#_Toc303857609}[]{#_Toc303848503}[]{#_Toc303849071}[]{#_Toc303850010}[]{#_Toc303857610}[]{#_Toc303848504}[]{#_Toc303849072}[]{#_Toc303850011}[]{#_Toc303857611}[]{#_Toc303848505}[]{#_Toc303849073}[]{#_Toc303850012}[]{#_Toc303857612}[]{#_Toc303848506}[]{#_Toc303849074}[]{#_Toc303850013}[]{#_Toc303857613}[]{#_Toc303848507}[]{#_Toc303849075}[]{#_Toc303850014}[]{#_Toc303857614}[]{#_Toc303848508}[]{#_Toc303849076}[]{#_Toc303850015}[]{#_Toc303857615}[]{#_Toc303848509}[]{#_Toc303849077}[]{#_Toc303850016}[]{#_Toc303857616}[]{#_Toc303848510}[]{#_Toc303849078}[]{#_Toc303850017}[]{#_Toc303857617}[]{#_Toc303848511}[]{#_Toc303849079}[]{#_Toc303850018}[]{#_Toc303857618}[]{#_Toc303848512}[]{#_Toc303849080}[]{#_Toc303850019}[]{#_Toc303857619}[]{#_Toc303848513}[]{#_Toc303849081}[]{#_Toc303850020}[]{#_Toc303857620}[]{#_Toc303848514}[]{#_Toc303849082}[]{#_Toc303850021}[]{#_Toc303857621}[]{#_Toc303848515}[]{#_Toc303849083}[]{#_Toc303850022}[]{#_Toc303857622}

**ACL \-- ACL配置命令 \-- acl hardware-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x847589875}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1309682341}
:::

**[ ]{lang="EN-US"}**

[**[acl]{lang="EN-US"}**[ **hardware-mode** **basic**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1848886674}[命令用来指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的硬件模式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1296173945}

[**[acl]{lang="EN-US"}**[ **hardware-mode** { **advanced** \| **basic** }]{lang="EN-US"}]{#struct_0_x4306_x6993_884931265}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_30962829}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x935370890}[的硬件模式为高级模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_551871035}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x679283510}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x847655411}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_609072062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x2136720861}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1173353443}

[**[advanced]{lang="EN-US"}**]{#struct_0_x4306_x6993_x925768318}[：表示高级模式。在高级模式下，单板除了支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[外，还支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[basic]{lang="EN-US"}**]{#struct_0_x4306_x6993_x826431916}[：表示基本模式。在基本模式下，单板仅支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x283609614}

[[本命令不会立即生效，必须在保存配置后待系统下次启动时才生效。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1378096366}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2088235183}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x847458803}[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的硬件模式为基本模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1438796250}

[\[Sysname\] acl hardware-mode basic]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1609656392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_119107478}**[ ]{lang="EN-US"}[hardware-mode]{lang="EN-US"}**
:::::

::::: {#176574094 .myid}
[]{#_Toc404791880}[]{#struct_0_x4306_x6993_x813028591}

**ACL \-- ACL配置命令 \-- acl hardware-mode ipv6**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_1083602568}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_323259892}
:::

[ ]{lang="EN-US"}

[**[acl]{lang="EN-US"}**[ **hardware-mode** **ipv6**]{lang="EN-US"}]{#struct_0_x4306_x6993_1748480472}[命令用来开启或关闭]{style="font-family:宋体"}[ACL]{lang="EN-US"}[硬件模式下的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1093909680}

[**[acl]{lang="EN-US"}**[ **hardware-mode** **ipv6** { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_x4306_x6993_x847524339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_217202370}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_360946977}[硬件模式下的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1585722721}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_483036632}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1755322049}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x291095551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_428114701}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718100853}

[**[disable]{lang="EN-US"}**]{#struct_0_x4306_x6993_x879707887}[：表示关闭]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能。当]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能关闭时，单板仅支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[enable]{lang="EN-US"}**]{#struct_0_x4306_x6993_586369457}[：表示开启]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能。当]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能开启时，单板除了支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[外，还支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_929043963}

[[本命令不会立即生效，必须在保存配置后待系统下次启动时才生效。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1058775969}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1872443639}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1280792289}[开启]{style="font-family:宋体"}[ACL]{lang="EN-US"}[硬件模式下的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1391698189}

[\[Sysname\] acl hardware-mode ipv6 enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1027191707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_718035317}**[ ]{lang="EN-US"}[hardware-mode]{lang="EN-US"}**
:::::

::::: {#891549840 .myid}
[]{#_Toc404791881}[]{#struct_0_x4306_x6993_1394796787}

**ACL \-- ACL配置命令 \-- acl interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1232387718}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1914914720}
:::

[ ]{lang="EN-US"}

[**[acl ]{lang="EN-US"}**[{ **logging** \| **trap** } **interval**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1961568664}[命令用来配置报文过滤日志信息或告警信息的生成与发送周期，同时使能报文的首包上送功能。]{style="font-family:宋体"}

[**[undo acl ]{lang="EN-US"}**[{ **logging** \| **trap** } **interval**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1081480982}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1353332969}

[**[acl ]{lang="EN-US"}**[{ **logging** \| **trap** } **interval** *interval*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1480054619}

[**[undo acl ]{lang="EN-US"}**[{ **logging** \| **trap** } **interval**]{lang="EN-US"}]{#struct_0_x4306_x6993_x233184421}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718231925}

[[报文过滤日志信息或告警信息的生成与发送周期为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4306_x6993_521481555}[分钟，即不记录报文过滤的日志。报文首包上送功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x444575611}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x72043681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_127408162}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x2062630802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1285088641}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1555396713}

[**[logging]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1577871641}[：指定周期性地生成报文过滤日志信息并发送到信息中心。有关信息中心的详细介绍请参见"网络管理和监控配置指导"中的"信息中心"。]{style="font-family:宋体"}

[**[trap]{lang="EN-US"}**]{#struct_0_x4306_x6993_x87974700}[：指定周期性地生成告警信息并发送到]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[模块。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x4306_x6993_611608976}[：报文过滤日志信息或告警信息的生成与发送周期，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1440]{lang="EN-US"}[，且必须为]{style="font-family:宋体"}[5]{lang="EN-US"}[的整数倍，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不进行记录，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718166389}

[[系统只支持对应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1682708446}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[或二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤的报文过滤日志信息或告警信息进行记录，且在上述]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中配置规则时必须指定]{style="font-family:宋体"}**[logging]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_816624453}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_323305478}[配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文过滤日志的生成与发送周期为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1388657205}

[\[Sysname\] acl logging interval 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2020420351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_1772296479}[ (IPv4 advanced ACL view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2019561235}[ (IPv4 basic ACL view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1130207259}[ (IPv6 advanced ACL view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_718362997}[ (IPv6 basic ACL view)]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1530817474}[ (MAC ACL view)]{lang="EN-US"}
:::::

::: {#-1461383778 .myid}
[]{#_Toc404791882}[]{#struct_0_x4306_x6993_x813135919}

**ACL \-- ACL配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1962922004}[命令用来配置]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x4306_x6993_x795560083}[命令用来删除]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x320002547}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x4306_x6993_1556933030}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x4306_x6993_903202329}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718428533}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_734962866}[没有任何描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_689229312}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1749426925}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2142272029}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_868746628}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x336758332}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x288585839}

[*[text]{lang="EN-US"}*]{#struct_0_x4306_x6993_1244498897}[：表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718625141}

[]{#_Toc86742804}[]{#_Toc80178010}[]{#_Toc80177404}[]{#_Toc33096860}[]{#struct_0_x4306_x6993_1786958404}[]{#_Toc252888206}[]{#_Toc253213276}[]{#_Toc253213622}[]{#_Toc252888207}[]{#_Toc253213277}[]{#_Toc253213623}[]{#_Toc252888210}[]{#_Toc253213280}[]{#_Toc253213626}[]{#_Toc252888212}[]{#_Toc253213282}[]{#_Toc253213628}[]{#_Toc252888213}[]{#_Toc253213283}[]{#_Toc253213629}[]{#_Toc139096874}[]{#_Toc139101656}[]{#_Toc139112024}[]{#_Toc140415830}[]{#_Toc140757796}[\# ]{lang="EN-US"}[为]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[配置描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1725574798}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] description This is an IPv4 basic ACL.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x637127853}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x722893767}
:::

::: {#1552247588 .myid}
[]{#_Toc404791883}[]{#struct_0_x4306_x6993_366043050}[]{#_Toc303849086}[]{#_Toc303850025}[]{#_Toc303857625}

**ACL \-- ACL配置命令 \-- display acl**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x243315763}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1756187870}

[**[display]{lang="EN-US"}**[ **acl** \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **all** \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_x4306_x6993_718559605}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x36223356}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x316113299}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1989047362}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_2113590601}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1959131335}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x2013679530}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_x879633176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1310165155}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1553837489}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x408816685}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_584571684}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_718100854}[：显示指定编号的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x879707880}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[：表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_586303921}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_2146112138}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_652430779}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4306_x6993_x798514907}[：显示指定类型中全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1673525361}[：显示指定名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1710068274}

[[本命令将按照实际匹配顺序来排列]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_74885635}[内的规则，即：当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，各规则将按照编号由小到大排列；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，各规则将按照"深度优先"原则由深到浅排列。]{style="font-family:宋体"}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x12552237}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718035318}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1394796792}[显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[的配置和运行情况。]{style="font-family:宋体"}

[[\<Sysname\> display acl 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x1232060037}

[Basic IPv4 ACL 2001, 2 rules, match-order is auto,]{lang="EN-US"}

[This is an IPv4 basic ACL.]{lang="EN-US"}

[ACL\'s step is 5]{lang="EN-US"}

[ACL accelerated]{lang="EN-US"}

[ rule 5 permit source 1.1.1.1 0 (5 times matched)]{lang="EN-US"}

[ rule 5 comment This rule is used on GigabitEthernet 1/0/1. ]{lang="EN-US"}

[ rule 10 permit source object-group permit (5 times matched)]{lang="EN-US"}

[]{#struct_0_x4306_x6993_x72991008}[[表1-1 ]{lang="EN-US"}[display acl]{lang="EN-US"}]{#_Toc138129447}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x671942178}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_714342852}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1484665278}

[[Basic IPv4 ACL 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x1231277833}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718231926}[的类型和编号，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的类型包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Basic IPv4 ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_521481552}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advanced IPv4 ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x444575604}[：表示]{lang="EN-US" style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:
  宋体"}[ACL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Basic IPv6 ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x71847074}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advanced IPv6 ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1599679840}[：表示]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:
  宋体"}[ACL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MAC]{lang="EN-US"}[ ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_247903210}[：表示二层]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User defined ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718166390}[：表示用户自定义]{lang="EN-US" style="font-family:
  宋体"}[ACL]{lang="EN-US"}

[[2 rules]{lang="EN-US"}]{#struct_0_x4306_x6993_x82827143}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1269336754}[内包含的规则数量]{style="font-family:宋体"}

[[match-order is auto]{lang="EN-US"}]{#struct_0_x4306_x6993_2013344609}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718362998}[的规则匹配顺序为自动排序（匹配顺序为配置顺序时不显示本字段）]{style="font-family:宋体"}

[[This is an IPv4 basic ACL.]{lang="EN-US"}]{#struct_0_x4306_x6993_1356606593}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_259811636}[的描述信息]{style="font-family:宋体"}

[[ACL\'s step is 5]{lang="EN-US"}]{#struct_0_x4306_x6993_x1257229062}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1981237447}[的规则编号的步长值为]{style="font-family:宋体"}[5]{lang="EN-US"}

[[ACL accelerated]{lang="EN-US"}]{#struct_0_x4306_x6993_x1401005529}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x223174138}[使能了加速功能]{style="font-family:宋体"}

[[rule 5 permit source 1.1.1.1 0]{lang="EN-US"}]{#struct_0_x4306_x6993_718297462}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_x294571709}[的具体内容，源地址为具体地址]{style="font-family:宋体"}

[[rule 10 permit source object-group permit]{lang="EN-US"}]{#struct_0_x4306_x6993_735493768}

[[规则]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x4306_x6993_x1172710353}[的具体内容，源地址为对象组]{style="font-family:宋体"}

[[5 times matched]{lang="EN-US"}]{#struct_0_x4306_x6993_x604130965}

[[该规则匹配的次数为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_373813468}[（仅统计软件]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的匹配次数，当匹配次数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时不显示本字段）]{style="font-family:宋体"}

[[rule 5 comment This rule is used on GigabitEthernet 1/0/1.]{lang="EN-US"}]{#struct_0_x4306_x6993_2052340245}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_718494070}[的描述信息]{style="font-family:宋体"}

[]{#_Toc86742806}[]{#_Toc80178012}[]{#_Toc80177406}[]{#_Toc120681090}[]{#_Toc120681091}[]{#_Toc120681098}[ ]{lang="EN-US"}

::::: {#1286425299 .myid}
[]{#_Toc404791884}[]{#struct_0_x4306_x6993_x1401071065}[]{#_Toc384729420}[]{#_Toc374456825}[]{#_Toc374454047}[]{#_Toc373832988}

**ACL \-- ACL配置命令 \-- display acl accelerate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_1990614148}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x324719917}
:::

[ ]{lang="EN-US"}

[**[display acl]{lang="EN-US"}**[ **accelerate**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1052108049}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的加速状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1495847937}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1377616340}

[**[display acl]{lang="EN-US"}**[ **accelerate** { **summary** \[ **ipv6** \| **mac** \] \| **verbose** \[ **ipv6** \| **mac** \] { *acl-number* \| **name** *acl-name* } }]{lang="EN-US"}]{#struct_0_x4306_x6993_2040351082}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4306_x6993_1608231765}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display acl]{lang="EN-US"}**[ **accelerate** { **summary** \[ **ipv6** \| **mac** \] \| **verbose** \[ **ipv6** \| **mac** \] { *acl-number* \| **name** *acl-name* } **slot** *slot-number* \[]{lang="EN-US"}]{#struct_0_x4306_x6993_x1401136601}[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}**[cpu]{lang="EN-US"}**[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}*[cpu-number ]{lang="EN-US"}*[\] }]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4306_x6993_387337942}[模式]{style="font-family:宋体"}[：]{style="font-family:宋体"}

[**[display acl]{lang="EN-US"}**[ **accelerate** { **summary** \[ **ipv6** \| **mac** \] \| **verbose** \[ **ipv6** \| **mac** \] { *acl-number* \| **name** *acl-name* } **chassis** *chassis-number* **slot** *slot-number* \[]{lang="EN-US"}]{#struct_0_x4306_x6993_x869330257}[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}**[cpu]{lang="EN-US"}**[[ ]{lang="EN-US" style="font-size:8.5pt;color:black"}]{.apple-converted-space}*[cpu-number ]{lang="EN-US"}*[\] }]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1673011432}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1431256978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1880715036}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1024999909}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_436460784}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x819564600}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1076798698}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1401202137}

[**[summary]{lang="EN-US"}**]{#struct_0_x4306_x6993_x802749820}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[加速的概要信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4306_x6993_1766984442}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[加速的详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1880630548}[：显示]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的加速状态。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x415530979}[：显示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的加速状态。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_x214206676}[：]{style="font-family:宋体"}[显示指定编号的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的加速状态。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1598112982}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_1230359840}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_715736439}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x2081172863}[：显示指定名称的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的加速状态。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x4306_x6993_x1401267673}[：显示指定单板的]{style="font-family:宋体;
color:black"}[ACL]{lang="EN-US"}[加速[信息，该单板必须为加速芯片所在单板，]{style="color:black"}]{style="font-family:
宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:
宋体;color:black"}

[**[slot]{lang="EN-US" style="color:black"}***[ slot-number]{lang="EN-US" style="color:black"}*]{#struct_0_x4306_x6993_89402819}[：显示指定成员设备的]{style="font-family:宋体;color:black"}[ACL]{lang="EN-US"}[加速[信息，该设备必须为加速芯片所在成员设备，]{style="color:black"}]{style="font-family:宋体"}*[slot-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号。（集中式]{style="font-family:宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[设备）]{style="font-family:宋体;color:black"}

[**[chassis]{lang="EN-US" style="color:black"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US" style="color:black"}]{#struct_0_x4306_x6993_2035001727}[：显示指定成员设备上指定单板的]{style="font-family:宋体;color:black"}[ACL]{lang="EN-US"}[加速[信息，该单板必须为加速芯片所在单板，]{style="color:black"}]{style="font-family:宋体"}*[chassis-number]{lang="EN-US" style="color:black"}*[表示设备在]{style="font-family:
宋体;color:black"}[IRF]{lang="EN-US" style="color:black"}[中的成员编号，]{style="font-family:宋体;color:black"}*[slot-number]{lang="EN-US" style="color:black"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体;
color:black"}[IRF]{lang="EN-US" style="color:black"}[模式）]{style="font-family:宋体;color:black"}

[**[cpu]{lang="EN-US" style="color:black"}**[ *cpu-number*]{lang="EN-US" style="color:
black"}]{#struct_0_x4306_x6993_x2124704767}[：显示指定]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[上]{style="font-family:宋体;
color:black"}[ACL]{lang="EN-US"}[加速[信息，]{style="color:black"}]{style="font-family:宋体"}*[cpu-number]{lang="EN-US" style="color:black"}*[表示]{style="font-family:宋体;color:black"}[CPU]{lang="EN-US" style="color:black"}[的编号。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_977287818}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1505472182}[或]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x215982036}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x587842908}[显示加速概要信息。]{style="font-family:宋体"}

[[\<Sysname\>display acl accelerate summary]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x12246452}

[[Basic IPv4 ACL 2000]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x1528877330}

[[ACL named acl.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x1847151614}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x17932913}[显示加速详细信息。]{style="font-family:宋体"}

[[\<Sysname\>display acl accelerate verbose 2000]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x1578330393}

[[Basic IPv4 ACL 2000.]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_390702682}

[[ rule 0 permit]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x267778916}

[[ rule 1 deny (failed)]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x4306_x6993_x1119322992}

[[表1-2 ]{lang="EN-US"}[display acl accelerate verbose]{lang="EN-US"}]{#struct_0_x4306_x6993_1136876599}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x900119287}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1401398745}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_148757937}

[[failed]{lang="EN-US"}]{#struct_0_x4306_x6993_x1329314163}

[[表示此规则加速失败，匹配不生效]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1400415705}

[ ]{lang="EN-US"}

::::::: {#1180303557 .myid}
[]{#_Toc404791885}[]{#struct_0_x4306_x6993_1140393862}

**ACL \-- ACL配置命令 \-- display acl hardware-mode**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1306669220}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_188655150}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **acl** **hardware-mode**]{lang="EN-US"}]{#struct_0_x4306_x6993_546499434}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的硬件模式及其]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1173679063}

[**[display]{lang="EN-US"}**[ **acl** **hardware-mode**]{lang="EN-US"}]{#struct_0_x4306_x6993_341092340}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_104177067}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x722386052}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1951602651}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x281527404}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_x1588489493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_747260535}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_x2086569945}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_725510091}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1794509677}[显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的硬件模式及其]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display acl hardware-mode]{lang="EN-US"}]{#struct_0_x4306_x6993_507461267}

[Current ACL hardware mode:]{lang="EN-US"}

[ Mode: Advanced]{lang="EN-US"}

[ IPv6 status: Disabled]{lang="EN-US"}

[Next startup ACL hardware mode:]{lang="EN-US"}

[ Mode: Basic]{lang="EN-US"}

[ IPv6 status: Enabled]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_1991249408}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x378635912}
:::

[ ]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display acl hardware-mode]{lang="EN-US"}]{#struct_0_x4306_x6993_119627921}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x593543666}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1193885563}
:::::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2134854276}

[[Current ACL hardware mode]{lang="EN-US"}]{#struct_0_x4306_x6993_1187448029}

[[当前的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1272917480}[硬件模式及其]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Next startup ACL hardware mode]{lang="EN-US"}]{#struct_0_x4306_x6993_1791774713}

[[下次启动后的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1248777546}[硬件模式及其]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[状态]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x4306_x6993_x22340016}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_2034434398}[的硬件模式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Basic]{lang="EN-US"}]{#struct_0_x4306_x6993_635582123}[：表示基本模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advanced]{lang="EN-US"}]{#struct_0_x4306_x6993_x1193110532}[：表示高级模式]{lang="EN-US" style="font-family:宋体"}

[[IPv6 status]{lang="EN-US"}]{#struct_0_x4306_x6993_1543743925}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1448464087}[硬件模式下的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4306_x6993_1979871470}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[已开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4306_x6993_x1111113879}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能已关闭]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1615842176 .myid}
[]{#_Toc291080246}[]{#_Toc404791886}[]{#struct_0_x4306_x6993_x1051456360}[]{#_Toc291080245}[]{#_Toc303849088}[]{#_Toc303850027}[]{#_Toc303857627}[]{#_Toc303849089}[]{#_Toc303850028}[]{#_Toc303857628}[]{#_Toc303849090}[]{#_Toc303850029}[]{#_Toc303857629}[]{#_Toc303849091}[]{#_Toc303850030}[]{#_Toc303857630}[]{#_Toc303849092}[]{#_Toc303850031}[]{#_Toc303857631}[]{#_Toc303849093}[]{#_Toc303850032}[]{#_Toc303857632}[]{#_Toc303849094}[]{#_Toc303850033}[]{#_Toc303857633}[]{#_Toc303849095}[]{#_Toc303850034}[]{#_Toc303857634}[]{#_Toc303849096}[]{#_Toc303850035}[]{#_Toc303857635}[]{#_Toc303849097}[]{#_Toc303850036}[]{#_Toc303857636}[]{#_Toc303849098}[]{#_Toc303850037}[]{#_Toc303857637}[]{#_Toc303849099}[]{#_Toc303850038}[]{#_Toc303857638}[]{#_Toc303849100}[]{#_Toc303850039}[]{#_Toc303857639}[]{#_Toc303849101}[]{#_Toc303850040}[]{#_Toc303857640}[]{#_Toc303849102}[]{#_Toc303850041}[]{#_Toc303857641}[]{#_Toc303849103}[]{#_Toc303850042}[]{#_Toc303857642}[]{#_Toc303849104}[]{#_Toc303850043}[]{#_Toc303857643}[]{#_Toc303849105}[]{#_Toc303850044}[]{#_Toc303857644}[]{#_Toc303849106}[]{#_Toc303850045}[]{#_Toc303857645}[]{#_Toc303849107}[]{#_Toc303850046}[]{#_Toc303857646}[]{#_Toc303849108}[]{#_Toc303850047}[]{#_Toc303857647}[]{#_Toc303849109}[]{#_Toc303850048}[]{#_Toc303857648}[]{#_Toc303849110}[]{#_Toc303850049}[]{#_Toc303857649}[]{#_Toc303849111}[]{#_Toc303850050}[]{#_Toc303857650}[]{#_Toc303849112}[]{#_Toc303850051}[]{#_Toc303857651}[]{#_Toc303849113}[]{#_Toc303850052}[]{#_Toc303857652}[]{#_Toc303849114}[]{#_Toc303850053}[]{#_Toc303857653}[]{#_Toc303849115}[]{#_Toc303850054}[]{#_Toc303857654}[]{#_Toc303849148}[]{#_Toc303850087}[]{#_Toc303857687}

**ACL \-- ACL配置命令 \-- display packet-filter**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 3 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x19373743}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_718035315}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_1394796789}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1232518790}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1288250533}

[**[display]{lang="EN-US"}**[ **packet-filter** { { **global** \| **interface** \[ *interface-type* *interface-number* \] \| **vlan** \[ *vlan-id* \] } \[ **inbound** \| **outbound** \] \| **zone-pair security** \[ **source** *source-zone-name* **destination** *destination-zone-name* \] }]{lang="EN-US"}]{#struct_0_x4306_x6993_769071720}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4306_x6993_935113468}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **packet-filter** { **interface** \[ *interface-type* *interface-number* \] \[ **inbound** \| **outbound** \] \| { { **global** \| **interface** **vlan-interface** *vlan-interface-number* \| **vlan** \[ *vlan-id* \] } \[ **inbound** \| **outbound** \] \| **zone-pair security** \[ **source** *source-zone-name* **destination** *destination-zone-name* \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \] }]{lang="EN-US"}]{#struct_0_x4306_x6993_x2092207978}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4306_x6993_x446938432}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **packet-filter** { **interface** \[ *interface-type* *interface-number* \] \[ **inbound** \| **outbound** \] \| { { **global** \| **interface** **vlan-interface** *vlan-interface-number* \| **vlan** \[ *vlan-id* \] } \[ **inbound** \| **outbound** \] \| **zone-pair security** \[ **source** *source-zone-name* **destination** *destination-zone-name* \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \] }]{lang="EN-US"}]{#struct_0_x4306_x6993_522172042}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718231923}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_521481549}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1511739521}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x135842562}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1166003275}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x819482206}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_x1618613913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x291678260}

[**[global]{lang="EN-US"}**]{#struct_0_x4306_x6993_x321224303}[：显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的全局（即所有物理接口）应用情况。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_718166387}[：显示指定接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。若未指定接口类型和接口编号，将显示所有接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（集中式设备）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1682708440}[：显示指定接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号，这里的接口类型不包括]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口。若未指定接口类型和接口编号，将显示除]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口以外的所有接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（分布式设备－独立运行模式、集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备和分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ **vlan-interface** *vlan-interface-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x346174961}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}*[vlan-interface-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_2117287513}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。若未指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，将显示所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[**[zone-pair security ]{lang="EN-US"}**[\[ **source** *source-zone-name* **destination** *destination-zone-name* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_735362695}[：显示指定安全域间实例上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}*[source-zone-name]{lang="EN-US"}*[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_1744268542}[：显示入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2067339021}[：显示出方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_62176635}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x761096532}[：]{style="font-family:宋体"}[显示指定成员设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若未指定本参数，将显示主用设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x12180916}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若未指定本参数，将显示主用设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x850535420}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示全局主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_489757517}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若未指定本参数，将显示全局主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_735166087}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718362995}

[[显示安全域间实例上的应用情况时不区分方向，其他情况，若未指定]{style="font-family:宋体"}**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_1356606596}[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[参数，将同时显示出、入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_260008244}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1373384238}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中出、入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter vlan 2]{lang="EN-US"}]{#struct_0_x4306_x6993_x1757673575}

[VLAN: 2]{lang="EN-US"}

[In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[  IPv6 ACL 2001]{lang="EN-US"}

[  MAC ACL 4001]{lang="EN-US"}

[  IPv4 default action: Deny]{lang="EN-US"}

[  IPv6 default action: Deny]{lang="EN-US"}

[  MAC default action: Deny]{lang="EN-US"}

[Out-bound policy:]{lang="EN-US"}

[  IPv6 ACL 2001 (Failed)]{lang="EN-US"}

[  IPv6 default action: Deny (Failed)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_718297459}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter interface gigabitethernet 1/0/1 inbound]{lang="EN-US"}]{#struct_0_x4306_x6993_1661743418}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[  IPv6 ACL 2002 (Failed)]{lang="EN-US"}

[  MAC ACL 4003 (Failed), Hardware-count (Failed)]{lang="EN-US"}

[  IPv4 ACL 2004, Hardware-count (Failed)]{lang="EN-US"}

[  IPv4 default action: Deny, Hardware-count]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_2098508090}[显示出、入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的全局应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter global]{lang="EN-US"}]{#struct_0_x4306_x6993_718494067}

[Global:]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[  IPv6 ACL 2001]{lang="EN-US"}

[  MAC ACL 4001]{lang="EN-US"}

[  IPv4 default action: Deny (Failed)]{lang="EN-US"}

[  IPv6 default action: Deny (Failed)]{lang="EN-US"}

[  MAC default action: Deny]{lang="EN-US"}

[ Out-bound policy:]{lang="EN-US"}

[  MAC ACL 4001, Hardware-count]{lang="EN-US"}

[  MAC default action: Deny]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_735624838}[显示安全域间实例]{style="font-family:宋体"}[源域]{style="font-family:宋体"}[office]{lang="EN-US"}[到目的域]{style="font-family:宋体"}[library]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter zone-pair security source office destination library]{lang="EN-US"}]{#struct_0_x4306_x6993_x567562199}

[Zone-pair: source office destination library]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[  IPv4 ACL 2002]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display packet-filter]{lang="EN-US"}]{#struct_0_x4306_x6993_x1589879084}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x675650914}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2104392114}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x426626210}

[[Interface]{lang="EN-US"}]{#struct_0_x4306_x6993_x1094707101}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_680798711}[在指定接口上的应用情况]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x4306_x6993_x1184144164}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718428531}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的应用情况]{style="font-family:宋体"}

[[Zone-pair]{lang="EN-US"}]{#struct_0_x4306_x6993_735493766}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1172710347}[在指定安全域间实例上的应用情况]{style="font-family:宋体"}

[[Global]{lang="EN-US"}]{#struct_0_x4306_x6993_734962864}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_689229310}[的全局（即所有物理接口）应用情况]{style="font-family:宋体"}

[[In-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_x1749426923}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x979472615}[在入方向上的应用情况]{style="font-family:宋体"}

[[Out-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_x1132401740}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718625139}[在出方向上的应用情况]{style="font-family:宋体"}

[[IPv4 ACL 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x551693748}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1857186563}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[IPv6 ACL 2002 (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1095180925}

[[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_1123653454}[基本]{style="font-family:宋体"}[ACL 2002]{lang="EN-US"}[应用失败]{style="font-family:宋体"}

[[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_360354154}

[[规则匹配统计功能应用成功]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718559603}

[[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x36223358}

[[规则匹配统计功能应用失败]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x316113301}

[[IPv4 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_32207945}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1986637448}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_718100852}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x879707886}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_586434993}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x1479929167}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_718035316}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[IPv6 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_1394796786}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1232322182}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_387163602}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_385411179}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_718231924}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_521481554}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x444575610}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[MAC default action]{lang="EN-US"}]{#struct_0_x4306_x6993_x72109217}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718166388}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_x1682708445}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x749459488}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x1550636344}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_718362996}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1356606599}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1995941246 .myid}
[]{#_Toc404791887}[]{#struct_0_x4306_x6993_259156276}

**ACL \-- ACL配置命令 \-- display packet-filter statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x272473318}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1184593689}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_x35192260}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718297460}

[**[display]{lang="EN-US"}**[ **packet-filter** **statistics** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } \[ **default** \| \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \] \| **zone-pair security** **source** *source-zone-name* **destination** *destination-zone-name* \[ \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \] } \[ **brief** \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x294571711}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x603606676}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1623120604}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_182203328}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x84504151}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1854309636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x765307532}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_718494068}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1589879091}

[**[global]{lang="EN-US"}**]{#struct_0_x4306_x6993_1431125831}[：显示全局（即所有物理接口）统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1318531596}[：显示指定接口上的统计信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x4306_x6993_1097179328}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的统计信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[**[zone-pair security source ]{lang="EN-US"}***[source-zone-name ]{lang="EN-US"}***[destination ]{lang="EN-US"}***[destination-zone-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_735100550}[：显示指定安全域间实例上的统计信息。]{style="font-family:宋体"}*[source-zone-name]{lang="EN-US"}*[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x920502503}[：显示入方向上的统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2100368785}[：显示出方向上的统计信息。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x4306_x6993_1317207364}[：显示报文过滤缺省动作的统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1955769777}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1769057036}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_246591299}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_2001500676}[：显示指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_718428532}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_734962867}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_689229311}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1749426922}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_586611326}[：显示指定名称]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x4306_x6993_x109272972}[：显示简要统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x552728701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2011654269}[、]{lang="EN-US" style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[、]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型（]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[、]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[）]{style="font-family:宋体"}[参数，将显示全部]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[显示安全域间实例统计信息时不区分方向。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_735624837}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[若未指定]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1935912992}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_541047928}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_718625140}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[入方向上全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter statistics interface gigabitethernet 1/0/1 inbound]{lang="EN-US"}]{#struct_0_x4306_x6993_718559604}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001, Hardware-count]{lang="EN-US"}

[   From 2011-06-04 10:25:21 to 2011-06-04 10:35:57]{lang="EN-US"}

[   rule 0 permit source 2.2.2.2 0 (2 packets)]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (No resource)]{lang="EN-US"}

[   Totally 2 packets permitted, 0 packets denied]{lang="EN-US"}

[   Totally 100% permitted, 0% denied]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 ACL 2002 (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC ACL 4000]{lang="EN-US"}

[   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 ACL 2000]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 default action: Deny, Hardware-count]{lang="EN-US"}

[   From 2011-06-04 10:25:21 to 2011-06-04 10:35:57]{lang="EN-US"}

[   Totally 7 packets]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 default action: Deny, Hardware-count]{lang="EN-US"}

[   From 2011-06-04 10:25:41 to 2011-06-04 10:35:57]{lang="EN-US"}

[   Totally 0 packets]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC default action: Deny, Hardware-count]{lang="EN-US"}

[   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57]{lang="EN-US"}

[   Totally 0 packets]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x36223357}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中入方向上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter statistics vlan 2 inbound 3000]{lang="EN-US"}]{#struct_0_x4306_x6993_x316113300}

[VLAN: 2]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 3000, Hardware-count (Failed)]{lang="EN-US"}

[   From 2011-06-04 10:25:34 to 2011-06-04 10:35:57]{lang="EN-US"}

[   rule 0 permit source 2.2.2.2 0]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 counting (2 packets)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (Failed)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_735166085}[显示安全]{style="font-family:宋体"}[域间实例源域]{style="font-family:宋体"}[office]{lang="EN-US"}[到目的域]{style="font-family:宋体"}[library]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter statistics zone-pair security source office destination library 3001]{lang="EN-US"}]{#struct_0_x4306_x6993_735231621}

[Zone-pair: source office destination library]{lang="EN-US"}

[IPv4 ACL 3001]{lang="EN-US"}

[   rule 0 permit source 2.2.2.2 0]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 counting (2 packets)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (Failed)]{lang="EN-US"}

[   Totally 2 packets permitted, 0 packets denied]{lang="EN-US"}

[   Totally 100% permitted, 0% denied]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display packet-filter statistics]{lang="EN-US"}]{#struct_0_x4306_x6993_32273481}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x680453122}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1629894472}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1090280657}

[[Interface]{lang="EN-US"}]{#struct_0_x4306_x6993_718100849}

[[在指定接口上应用的统计信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1458944283}

[[VLAN]{lang="EN-US"}]{#struct_0_x4306_x6993_x1389670010}

[[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x4306_x6993_1244644632}[中应用的统计信息]{style="font-family:宋体"}

[[Zone-pair]{lang="EN-US"}]{#struct_0_x4306_x6993_735100549}

[[在指定安全域间实例上应用的统计信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1280863329}

[[In-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_1625911589}

[[在入方向上应用的统计信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1217046363}

[[Out-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_636350049}

[[在出方向上应用的统计信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718035313}

[[IPv4 ACL 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_1394796783}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1232125574}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[IPv4 ACL 2002 (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_877039364}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_867419023}[基本]{style="font-family:宋体"}[ACL 2002]{lang="EN-US"}[应用失败]{style="font-family:宋体"}

[[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_718231921}

[[规则匹配统计功能应用成功]{style="font-family:宋体"}]{#struct_0_x4306_x6993_521481551}

[[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x444575607}

[[规则匹配统计功能应用失败]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x71912610}

[[From 2011-06-04 10:25:21 to 2011-06-04 10:35:57]{lang="EN-US"}]{#struct_0_x4306_x6993_1122614095}

[[该统计的起始和终止时间]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718166385}

[[2 packets]{lang="EN-US"}]{#struct_0_x4306_x6993_x1682708442}

[[该规则匹配了]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x4306_x6993_x1508974375}[个包（当匹配的包个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时不显示本字段）]{style="font-family:宋体"}

[[No resource]{lang="EN-US"}]{#struct_0_x4306_x6993_x2101538349}

[[该规则对应的统计资源不足。在显示统计信息时，若该规则的统计资源不足，便会显示本字段（本字段的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1727980982}

[[rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_718362993}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_1356606602}[应用失败]{style="font-family:宋体"}

[[Totally 2 packets permitted, 0 packets denied]{lang="EN-US"}]{#struct_0_x4306_x6993_x1696569043}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1747528084}[允许和拒绝符合条件报文的个数]{style="font-family:宋体"}

[[Totally 100% permitted, 0% denied]{lang="EN-US"}]{#struct_0_x4306_x6993_191424530}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718297457}[允许符合条件报文的通过率和拒绝符合条件报文的丢弃率]{style="font-family:宋体"}

[[IPv4 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_1661743424}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2099294521}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_406199892}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_718494065}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x1589879086}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_1027775768}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1957680564}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[IPv6 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_718428529}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1603689288}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_x143446186}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1809230412}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_718625137}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x551693750}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1856662274}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[MAC default action]{lang="EN-US"}]{#struct_0_x4306_x6993_1660412184}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718559601}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_x36223360}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_2022538867}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x1739273124}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_718100850}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x879707884}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[Totally 7 packets]{lang="EN-US"}]{#struct_0_x4306_x6993_586566065}

[[报文过滤缺省动作的执行次数]{style="font-family:宋体"}]{#struct_0_x4306_x6993_718035314}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1394796788}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1232453254}

::::: {#2042109914 .myid}
[]{#_Toc404791888}[]{#struct_0_x4306_x6993_582019336}[]{#_Toc303847613}[]{#_Toc303848522}[]{#_Toc303849151}[]{#_Toc303850090}[]{#_Toc303857690}[]{#_Toc303847614}[]{#_Toc303848523}[]{#_Toc303849152}[]{#_Toc303850091}[]{#_Toc303857691}[]{#_Toc303847615}[]{#_Toc303848524}[]{#_Toc303849153}[]{#_Toc303850092}[]{#_Toc303857692}[]{#_Toc303847616}[]{#_Toc303848525}[]{#_Toc303849154}[]{#_Toc303850093}[]{#_Toc303857693}[]{#_Toc303847617}[]{#_Toc303848526}[]{#_Toc303849155}[]{#_Toc303850094}[]{#_Toc303857694}[]{#_Toc303847618}[]{#_Toc303848527}[]{#_Toc303849156}[]{#_Toc303850095}[]{#_Toc303857695}[]{#_Toc303847619}[]{#_Toc303848528}[]{#_Toc303849157}[]{#_Toc303850096}[]{#_Toc303857696}[]{#_Toc303847620}[]{#_Toc303848529}[]{#_Toc303849158}[]{#_Toc303850097}[]{#_Toc303857697}[]{#_Toc303847621}[]{#_Toc303848530}[]{#_Toc303849159}[]{#_Toc303850098}[]{#_Toc303857698}[]{#_Toc303847622}[]{#_Toc303848531}[]{#_Toc303849160}[]{#_Toc303850099}[]{#_Toc303857699}[]{#_Toc303847623}[]{#_Toc303848532}[]{#_Toc303849161}[]{#_Toc303850100}[]{#_Toc303857700}[]{#_Toc303847624}[]{#_Toc303848533}[]{#_Toc303849162}[]{#_Toc303850101}[]{#_Toc303857701}[]{#_Toc303847625}[]{#_Toc303848534}[]{#_Toc303849163}[]{#_Toc303850102}[]{#_Toc303857702}[]{#_Toc303847626}[]{#_Toc303848535}[]{#_Toc303849164}[]{#_Toc303850103}[]{#_Toc303857703}[]{#_Toc303847627}[]{#_Toc303848536}[]{#_Toc303849165}[]{#_Toc303850104}[]{#_Toc303857704}[]{#_Toc303847628}[]{#_Toc303848537}[]{#_Toc303849166}[]{#_Toc303850105}[]{#_Toc303857705}[]{#_Toc303847629}[]{#_Toc303848538}[]{#_Toc303849167}[]{#_Toc303850106}[]{#_Toc303857706}[]{#_Toc303847630}[]{#_Toc303848539}[]{#_Toc303849168}[]{#_Toc303850107}[]{#_Toc303857707}[]{#_Toc303847631}[]{#_Toc303848540}[]{#_Toc303849169}[]{#_Toc303850108}[]{#_Toc303857708}[]{#_Toc303847632}[]{#_Toc303848541}[]{#_Toc303849170}[]{#_Toc303850109}[]{#_Toc303857709}[]{#_Toc303847633}[]{#_Toc303848542}[]{#_Toc303849171}[]{#_Toc303850110}[]{#_Toc303857710}[]{#_Toc303847634}[]{#_Toc303848543}[]{#_Toc303849172}[]{#_Toc303850111}[]{#_Toc303857711}[]{#_Toc303847635}[]{#_Toc303848544}[]{#_Toc303849173}[]{#_Toc303850112}[]{#_Toc303857712}[]{#_Toc303847636}[]{#_Toc303848545}[]{#_Toc303849174}[]{#_Toc303850113}[]{#_Toc303857713}[]{#_Toc303847637}[]{#_Toc303848546}[]{#_Toc303849175}[]{#_Toc303850114}[]{#_Toc303857714}[]{#_Toc303847638}[]{#_Toc303848547}[]{#_Toc303849176}[]{#_Toc303850115}[]{#_Toc303857715}[]{#_Toc303847639}[]{#_Toc303848548}[]{#_Toc303849177}[]{#_Toc303850116}[]{#_Toc303857716}[]{#_Toc303847640}[]{#_Toc303848549}[]{#_Toc303849178}[]{#_Toc303850117}[]{#_Toc303857717}[]{#_Toc303847641}[]{#_Toc303848550}[]{#_Toc303849179}[]{#_Toc303850118}[]{#_Toc303857718}[]{#_Toc303847642}[]{#_Toc303848551}[]{#_Toc303849180}[]{#_Toc303850119}[]{#_Toc303857719}[]{#_Toc303847643}[]{#_Toc303848552}[]{#_Toc303849181}[]{#_Toc303850120}[]{#_Toc303857720}[]{#_Toc303847644}[]{#_Toc303848553}[]{#_Toc303849182}[]{#_Toc303850121}[]{#_Toc303857721}[]{#_Toc303847645}[]{#_Toc303848554}[]{#_Toc303849183}[]{#_Toc303850122}[]{#_Toc303857722}[]{#_Toc303847646}[]{#_Toc303848555}[]{#_Toc303849184}[]{#_Toc303850123}[]{#_Toc303857723}[]{#_Toc303847647}[]{#_Toc303848556}[]{#_Toc303849185}[]{#_Toc303850124}[]{#_Toc303857724}[]{#_Toc303847648}[]{#_Toc303848557}[]{#_Toc303849186}[]{#_Toc303850125}[]{#_Toc303857725}[]{#_Toc303847649}[]{#_Toc303848558}[]{#_Toc303849187}[]{#_Toc303850126}[]{#_Toc303857726}[]{#_Toc303847650}[]{#_Toc303848559}[]{#_Toc303849188}[]{#_Toc303850127}[]{#_Toc303857727}[]{#_Toc303847651}[]{#_Toc303848560}[]{#_Toc303849189}[]{#_Toc303850128}[]{#_Toc303857728}[]{#_Toc303847652}[]{#_Toc303848561}[]{#_Toc303849190}[]{#_Toc303850129}[]{#_Toc303857729}[]{#_Toc303847653}[]{#_Toc303848562}[]{#_Toc303849191}[]{#_Toc303850130}[]{#_Toc303857730}[]{#_Toc303847654}[]{#_Toc303848563}[]{#_Toc303849192}[]{#_Toc303850131}[]{#_Toc303857731}[]{#_Toc303847655}[]{#_Toc303848564}[]{#_Toc303849193}[]{#_Toc303850132}[]{#_Toc303857732}[]{#_Toc303847656}[]{#_Toc303848565}[]{#_Toc303849194}[]{#_Toc303850133}[]{#_Toc303857733}[]{#_Toc303847657}[]{#_Toc303848566}[]{#_Toc303849195}[]{#_Toc303850134}[]{#_Toc303857734}[]{#_Toc303847694}[]{#_Toc303848603}[]{#_Toc303849232}[]{#_Toc303850171}[]{#_Toc303857771}[]{#_Toc303847695}[]{#_Toc303848604}[]{#_Toc303849233}[]{#_Toc303850172}[]{#_Toc303857772}[]{#_Toc303847696}[]{#_Toc303848605}[]{#_Toc303849234}[]{#_Toc303850173}[]{#_Toc303857773}

**ACL \-- ACL配置命令 \-- display packet-filter statistics sum**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 4 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_1243316360}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x2117498795}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **packet-filter** **statistics sum**]{lang="EN-US"}]{#struct_0_x4306_x6993_2034679526}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1727019287}

[**[display]{lang="EN-US"}**[ **packet-filter** **statistics** **sum** { **inbound** \| **outbound** } \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \[ **brief** \]]{lang="EN-US"}]{#struct_0_x4306_x6993_718231922}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_521481548}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1511739522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x135908098}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1941669849}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1511611651}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x2070376380}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_x2100670212}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1308617681}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_718166386}[：显示入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1682708439}[：显示出方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1176398105}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_168697046}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1134397872}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_863744156}[：显示指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_103594402}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_x541638266}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x85215639}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_186332765}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1836678103}[：显示指定名称]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x4306_x6993_718362994}[：显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的简要累加统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1356992759}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1233915762}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1356606597}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_260073780}[显示入方向上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[在报文过滤中应用的累加统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter statistics sum inbound 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_1392014618}

[Sum:]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[   rule 0 permit source 2.2.2.2 0 (2 packets)]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0]{lang="EN-US"}

[   rule 10 permit vpn-instance test]{lang="EN-US"}

[   Totally 2 packets permitted, 0 packets denied ]{lang="EN-US"}

[   Totally 100% permitted, 0% denied]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1129343938}[显示入方向上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[在报文过滤中应用的简要累加统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter statistics sum inbound 2000 brief]{lang="EN-US"}]{#struct_0_x4306_x6993_x1377885520}

[Sum:]{lang="EN-US"}

[ Inbound policy:]{lang="EN-US"}

[  IPv4 ACL 2000]{lang="EN-US"}

[   Totally 2 packets permitted, 0 packets denied ]{lang="EN-US"}

[   Totally 100% permitted, 0% denied]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display packet-filter statistics sum]{lang="EN-US"}]{#struct_0_x4306_x6993_870460184}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x683847682}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_548516327}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718297458}

[[Sum]{lang="EN-US"}]{#struct_0_x4306_x6993_1661743417}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_2099360058}[在报文过滤中应用的累加统计信息]{style="font-family:宋体"}

[[In-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_1190742916}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1554551017}[在入方向上应用的累加统计信息]{style="font-family:宋体"}

[[Out-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_191426823}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1552460348}[在出方向上应用的累加统计信息]{style="font-family:宋体"}

[[IPv4 ACL 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_718494066}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1589879085}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[应用的累加统计信息]{style="font-family:宋体"}

[[2 packets]{lang="EN-US"}]{#struct_0_x4306_x6993_x538308173}

[[该规则匹配了]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_x4306_x6993_x217807070}[个包（当匹配的包个数为]{style="font-family:宋体"}[0]{lang="EN-US"}[时不显示本字段）]{style="font-family:宋体"}

[[Totally 2 packets permitted, 0 packets denied]{lang="EN-US"}]{#struct_0_x4306_x6993_637028281}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_718428530}[允许和拒绝符合条件报文的个数]{style="font-family:宋体"}

[[Totally 100% permitted, 0% denied]{lang="EN-US"}]{#struct_0_x4306_x6993_734962865}

[[该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_689229309}[允许符合条件报文的通过率和拒绝符合条件报文的丢弃率]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_206888222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_769011579}

::::: {#666991317 .myid}
[]{#_Toc404791889}[]{#struct_0_x4306_x6993_x623076129}

**ACL \-- ACL配置命令 \-- display packet-filter verbose**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 6 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_599791423}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1459939059}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **packet-filter** **verbose**]{lang="EN-US"}]{#struct_0_x4306_x6993_718625138}[命令用来显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x551693747}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1856858883}

[**[display]{lang="EN-US"}**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } \[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \] \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* } \[ \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \] }]{lang="EN-US"}]{#struct_0_x4306_x6993_2085724694}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4306_x6993_x1793049291}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } \[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \]  \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* } \[ \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \] } \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4306_x6993_2125734296}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4306_x6993_x1663150901}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **packet-filter** **verbose** { { **global** \| **interface** *interface-type* *interface-number* \| **vlan** *vlan-id* } { **inbound** \| **outbound** } \[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \] \| **zone-pair security source** *source-zone-name* **destination** *destination-zone-name* } \[ \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \] } \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1108179548}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_718559602}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x36223359}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x316113302}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_32142409}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_1696331044}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_961537080}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_132522831}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1468278535}

[**[global]{lang="EN-US"}**]{#struct_0_x4306_x6993_1211558123}[：显示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的全局（即所有物理接口）详细应用情况。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654552142}[：显示指定接口上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1932532788}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。]{style="font-family:宋体"}

[**[zone-pair security source ]{lang="EN-US"}***[source-zone-name ]{lang="EN-US"}***[destination ]{lang="EN-US"}***[destination-zone-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1281256546}[：显示指定安全域间实例上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}*[source-zone-name]{lang="EN-US"}*[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_184762788}[：显示入方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_1741356181}[：显示出方向上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x773048042}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x39428930}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1948447728}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_1785825358}[：显示指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_1489747317}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_1557845219}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_152296706}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_520666659}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654617678}[：显示指定名称]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1852257991}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_1528597079}[：]{style="font-family:宋体"}[显示指定成员设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若未指定本参数，将显示主用设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_1955835313}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若未指定本参数，将显示主用设备上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_1622326942}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示全局主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x910566143}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若未指定本参数，将显示全局主用主控板上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281191010}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1337505072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x4306_x6993_68460349}[、]{lang="EN-US" style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[、]{style="font-family:宋体"}**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型（]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[、]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[）]{style="font-family:宋体"}[参数，将显示全部]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息以及报文过滤缺省动作的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[显示安全域间实例详细应用情况时不区分方向。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1281387618}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[若未指定]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1935847456}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2084593864}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1733495173}[显示]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中入方向上全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter verbose vlan 2 inbound]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654421070}

[VLAN: 2]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001, Hardware-count]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 ACL 2002 (Failed)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_606162758}[显示接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[入方向上全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter verbose interface gigabitethernet 1/0/1 inbound]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654486606}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001, Hardware-count (Failed)]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 ACL 2002 (Failed), Hardware-count (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 ACL 2000, Hardware-count]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC ACL 4000, Hardware-count]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 default action: Deny, Hardware-count (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 default action: Deny, Hardware-count (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC default action: Deny, Hardware-count]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x81914296}[显示入方向上全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的全局详细应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter verbose global inbound]{lang="EN-US"}]{#struct_0_x4306_x6993_1461774558}

[Global:]{lang="EN-US"}

[ In-bound policy:]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[   rule 0 permit ]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}

[   rule 10 permit vpn-instance test (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 ACL 2002 (Failed)]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 ACL 2000, Hardware-count]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC ACL 4000, Hardware-count]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv4 default action: Deny]{lang="EN-US"}

[ ]{lang="EN-US"}

[  IPv6 default action: Deny]{lang="EN-US"}

[ ]{lang="EN-US"}

[  MAC default action: Deny]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281256547}[显示安全]{style="font-family:宋体"}[域间实例源域]{style="font-family:宋体"}[office]{lang="EN-US"}[到目的域]{style="font-family:宋体"}[library]{lang="EN-US"}[上全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中的详细应用情况。]{style="font-family:宋体"}

[[\<Sysname\> display packet-filter verbose zone-pair security source office destination library]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281191011}

[Zone-pair: source office destination library]{lang="EN-US"}

[  IPv4 ACL 2001]{lang="EN-US"}

[   rule 0 permit]{lang="EN-US"}

[   rule 5 permit source 1.1.1.1 0]{lang="EN-US"}

[   rule 10 permit vpn-instance test ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display packet-filter verbose]{lang="EN-US"}]{#struct_0_x4306_x6993_x1669847588}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x389830146}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x274678122}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654289998}

[[Interface]{lang="EN-US"}]{#struct_0_x4306_x6993_x836983721}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x583182447}[在指定接口上的详细应用情况]{style="font-family:宋体"}

[[VLAN]{lang="EN-US"}]{#struct_0_x4306_x6993_2143247148}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_920580104}[在指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的详细应用情况]{style="font-family:宋体"}

[[Zone-pair]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281322083}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1280863332}[在指定安全域间实例上的详细应用情况]{style="font-family:宋体"}

[[Global]{lang="EN-US"}]{#struct_0_x4306_x6993_x937838823}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654355534}[的全局（即所有物理接口）详细应用情况]{style="font-family:宋体"}

[[In-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_x890581754}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x2006470288}[在入方向上的详细应用情况]{style="font-family:宋体"}

[[Out-bound policy]{lang="EN-US"}]{#struct_0_x4306_x6993_1748056236}

[[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_64260150}[在出方向上的详细应用情况]{style="font-family:宋体"}

[[IPv4 ACL 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x32193171}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654158926}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[IPv4 ACL 2002 (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1741010496}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1734982706}[基本]{style="font-family:宋体"}[ACL 2002]{lang="EN-US"}[应用失败]{style="font-family:宋体"}

[[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x1920423353}

[[规则匹配统计功能应用成功]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2080142030}

[[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654224462}

[[规则匹配统计功能应用失败]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1212914156}

[[rule 5 permit source 1.1.1.1 0 (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1408866051}

[[规则]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_1737559067}[应用失败]{style="font-family:宋体"}

[[IPv4 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_x960478030}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654027854}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_1781497058}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1761924283}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_1457136920}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654093390}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_172240436}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[IPv6 default action]{lang="EN-US"}]{#struct_0_x4306_x6993_x805740307}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x693767803}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_853646050}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654552141}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x1529248261}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x1432806996}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_1718580982}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[[MAC default action]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654617677}

[[报文过滤的缺省动作，包括：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1092743104}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_x4306_x6993_340103240}[：报文过滤缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_x1979698638}[：报文过滤缺省动作为]{lang="EN-US" style="font-family:宋体"}[D]{lang="EN-US"}[eny]{lang="EN-US"}[应用失败，实际动作仍为]{lang="EN-US" style="font-family:宋体"}[P]{lang="EN-US"}[ermit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654421069}[：]{lang="EN-US" style="font-family:宋体"}[报文过滤缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count]{lang="EN-US"}]{#struct_0_x4306_x6993_x1316217079}[：报文过滤缺省动作统计功能应用成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hardware-count (Failed)]{lang="EN-US"}]{#struct_0_x4306_x6993_100009256}[：报文过滤缺省动作统计功能应用失败]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1702921313 .myid}
[]{#_Toc404791890}[]{#struct_0_x4306_x6993_x152552774}[]{#_Toc303847698}[]{#_Toc303848607}[]{#_Toc303849236}[]{#_Toc303850175}[]{#_Toc303857775}[]{#_Toc303847699}[]{#_Toc303848608}[]{#_Toc303849237}[]{#_Toc303850176}[]{#_Toc303857776}[]{#_Toc303847700}[]{#_Toc303848609}[]{#_Toc303849238}[]{#_Toc303850177}[]{#_Toc303857777}[]{#_Toc303847701}[]{#_Toc303848610}[]{#_Toc303849239}[]{#_Toc303850178}[]{#_Toc303857778}[]{#_Toc303847702}[]{#_Toc303848611}[]{#_Toc303849240}[]{#_Toc303850179}[]{#_Toc303857779}[]{#_Toc303847703}[]{#_Toc303848612}[]{#_Toc303849241}[]{#_Toc303850180}[]{#_Toc303857780}[]{#_Toc303847704}[]{#_Toc303848613}[]{#_Toc303849242}[]{#_Toc303850181}[]{#_Toc303857781}[]{#_Toc303847705}[]{#_Toc303848614}[]{#_Toc303849243}[]{#_Toc303850182}[]{#_Toc303857782}[]{#_Toc303847706}[]{#_Toc303848615}[]{#_Toc303849244}[]{#_Toc303850183}[]{#_Toc303857783}[]{#_Toc303847707}[]{#_Toc303848616}[]{#_Toc303849245}[]{#_Toc303850184}[]{#_Toc303857784}[]{#_Toc303847708}[]{#_Toc303848617}[]{#_Toc303849246}[]{#_Toc303850185}[]{#_Toc303857785}[]{#_Toc303847709}[]{#_Toc303848618}[]{#_Toc303849247}[]{#_Toc303850186}[]{#_Toc303857786}[]{#_Toc303847710}[]{#_Toc303848619}[]{#_Toc303849248}[]{#_Toc303850187}[]{#_Toc303857787}[]{#_Toc303847711}[]{#_Toc303848620}[]{#_Toc303849249}[]{#_Toc303850188}[]{#_Toc303857788}[]{#_Toc303847712}[]{#_Toc303848621}[]{#_Toc303849250}[]{#_Toc303850189}[]{#_Toc303857789}[]{#_Toc303847713}[]{#_Toc303848622}[]{#_Toc303849251}[]{#_Toc303850190}[]{#_Toc303857790}[]{#_Toc303847714}[]{#_Toc303848623}[]{#_Toc303849252}[]{#_Toc303850191}[]{#_Toc303857791}[]{#_Toc303847715}[]{#_Toc303848624}[]{#_Toc303849253}[]{#_Toc303850192}[]{#_Toc303857792}[]{#_Toc303847716}[]{#_Toc303848625}[]{#_Toc303849254}[]{#_Toc303850193}[]{#_Toc303857793}[]{#_Toc303847717}[]{#_Toc303848626}[]{#_Toc303849255}[]{#_Toc303850194}[]{#_Toc303857794}[]{#_Toc303847718}[]{#_Toc303848627}[]{#_Toc303849256}[]{#_Toc303850195}[]{#_Toc303857795}[]{#_Toc303847719}[]{#_Toc303848628}[]{#_Toc303849257}[]{#_Toc303850196}[]{#_Toc303857796}[]{#_Toc303847720}[]{#_Toc303848629}[]{#_Toc303849258}[]{#_Toc303850197}[]{#_Toc303857797}[]{#_Toc303847721}[]{#_Toc303848630}[]{#_Toc303849259}[]{#_Toc303850198}[]{#_Toc303857798}[]{#_Toc303847722}[]{#_Toc303848631}[]{#_Toc303849260}[]{#_Toc303850199}[]{#_Toc303857799}[]{#_Toc303847723}[]{#_Toc303848632}[]{#_Toc303849261}[]{#_Toc303850200}[]{#_Toc303857800}[]{#_Toc303847724}[]{#_Toc303848633}[]{#_Toc303849262}[]{#_Toc303850201}[]{#_Toc303857801}[]{#_Toc303847725}[]{#_Toc303848634}[]{#_Toc303849263}[]{#_Toc303850202}[]{#_Toc303857802}[]{#_Toc303847726}[]{#_Toc303848635}[]{#_Toc303849264}[]{#_Toc303850203}[]{#_Toc303857803}[]{#_Toc303847727}[]{#_Toc303848636}[]{#_Toc303849265}[]{#_Toc303850204}[]{#_Toc303857804}[]{#_Toc303847728}[]{#_Toc303848637}[]{#_Toc303849266}[]{#_Toc303850205}[]{#_Toc303857805}[]{#_Toc303847729}[]{#_Toc303848638}[]{#_Toc303849267}[]{#_Toc303850206}[]{#_Toc303857806}[]{#_Toc303847730}[]{#_Toc303848639}[]{#_Toc303849268}[]{#_Toc303850207}[]{#_Toc303857807}[]{#_Toc303847731}[]{#_Toc303848640}[]{#_Toc303849269}[]{#_Toc303850208}[]{#_Toc303857808}[]{#_Toc303847732}[]{#_Toc303848641}[]{#_Toc303849270}[]{#_Toc303850209}[]{#_Toc303857809}[]{#_Toc303847733}[]{#_Toc303848642}[]{#_Toc303849271}[]{#_Toc303850210}[]{#_Toc303857810}[]{#_Toc303847734}[]{#_Toc303848643}[]{#_Toc303849272}[]{#_Toc303850211}[]{#_Toc303857811}[]{#_Toc303847735}[]{#_Toc303848644}[]{#_Toc303849273}[]{#_Toc303850212}[]{#_Toc303857812}[]{#_Toc303847736}[]{#_Toc303848645}[]{#_Toc303849274}[]{#_Toc303850213}[]{#_Toc303857813}[]{#_Toc303847737}[]{#_Toc303848646}[]{#_Toc303849275}[]{#_Toc303850214}[]{#_Toc303857814}[]{#_Toc303847738}[]{#_Toc303848647}[]{#_Toc303849276}[]{#_Toc303850215}[]{#_Toc303857815}[]{#_Toc303847739}[]{#_Toc303848648}[]{#_Toc303849277}[]{#_Toc303850216}[]{#_Toc303857816}[]{#_Toc303847740}[]{#_Toc303848649}[]{#_Toc303849278}[]{#_Toc303850217}[]{#_Toc303857817}[]{#_Toc303847741}[]{#_Toc303848650}[]{#_Toc303849279}[]{#_Toc303850218}[]{#_Toc303857818}[]{#_Toc303847742}[]{#_Toc303848651}[]{#_Toc303849280}[]{#_Toc303850219}[]{#_Toc303857819}[]{#_Toc303847743}[]{#_Toc303848652}[]{#_Toc303849281}[]{#_Toc303850220}[]{#_Toc303857820}[]{#_Toc303847744}[]{#_Toc303848653}[]{#_Toc303849282}[]{#_Toc303850221}[]{#_Toc303857821}[]{#_Toc303847745}[]{#_Toc303848654}[]{#_Toc303849283}[]{#_Toc303850222}[]{#_Toc303857822}[]{#_Toc303847746}[]{#_Toc303848655}[]{#_Toc303849284}[]{#_Toc303850223}[]{#_Toc303857823}[]{#_Toc303847747}[]{#_Toc303848656}[]{#_Toc303849285}[]{#_Toc303850224}[]{#_Toc303857824}[]{#_Toc303847748}[]{#_Toc303848657}[]{#_Toc303849286}[]{#_Toc303850225}[]{#_Toc303857825}[]{#_Toc303847749}[]{#_Toc303848658}[]{#_Toc303849287}[]{#_Toc303850226}[]{#_Toc303857826}[]{#_Toc303847750}[]{#_Toc303848659}[]{#_Toc303849288}[]{#_Toc303850227}[]{#_Toc303857827}[]{#_Toc303847751}[]{#_Toc303848660}[]{#_Toc303849289}[]{#_Toc303850228}[]{#_Toc303857828}[]{#_Toc303847752}[]{#_Toc303848661}[]{#_Toc303849290}[]{#_Toc303850229}[]{#_Toc303857829}[]{#_Toc303847753}[]{#_Toc303848662}[]{#_Toc303849291}[]{#_Toc303850230}[]{#_Toc303857830}[]{#_Toc303847754}[]{#_Toc303848663}[]{#_Toc303849292}[]{#_Toc303850231}[]{#_Toc303857831}[]{#_Toc303847755}[]{#_Toc303848664}[]{#_Toc303849293}[]{#_Toc303850232}[]{#_Toc303857832}[]{#_Toc303847756}[]{#_Toc303848665}[]{#_Toc303849294}[]{#_Toc303850233}[]{#_Toc303857833}[]{#_Toc303847757}[]{#_Toc303848666}[]{#_Toc303849295}[]{#_Toc303850234}[]{#_Toc303857834}[]{#_Toc303847758}[]{#_Toc303848667}[]{#_Toc303849296}[]{#_Toc303850235}[]{#_Toc303857835}[]{#_Toc303847759}[]{#_Toc303848668}[]{#_Toc303849297}[]{#_Toc303850236}[]{#_Toc303857836}[]{#_Toc303847760}[]{#_Toc303848669}[]{#_Toc303849298}[]{#_Toc303850237}[]{#_Toc303857837}[]{#_Toc303847761}[]{#_Toc303848670}[]{#_Toc303849299}[]{#_Toc303850238}[]{#_Toc303857838}[]{#_Toc303847762}[]{#_Toc303848671}[]{#_Toc303849300}[]{#_Toc303850239}[]{#_Toc303857839}[]{#_Toc303847796}[]{#_Toc303848705}[]{#_Toc303849334}[]{#_Toc303850273}[]{#_Toc303857873}

**ACL \-- ACL配置命令 \-- display qos-acl resource**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **qos-acl** **resource**]{lang="EN-US"}]{#struct_0_x4306_x6993_1030097207}[命令用来显示]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_477738826}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654486605}

[**[display]{lang="EN-US"}**[ **qos-acl** **resource**]{lang="EN-US"}]{#struct_0_x4306_x6993_1484169645}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4306_x6993_723404570}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **qos-acl** **resource** \[ **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1476283250}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x4306_x6993_993471186}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **qos-acl** **resource** \[ **chassis** *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}]{#struct_0_x4306_x6993_1335148077}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1808054743}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_571602522}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_895439347}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654289997}

[[network-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_372869860}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x843132809}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4306_x6993_2042570645}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1239861380}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x359096905}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示所有单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_2002138627}[：]{style="font-family:宋体"}[显示指定成员设备上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。若未指定本参数，将显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有成员设备上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_389751372}[：]{style="font-family:宋体"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。若未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x309937186}[：显示指定成员设备指定单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。若未指定本参数，将显示]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中所有成员设备的所有单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1976503615}[：]{style="font-family:宋体"}[显示指定单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。若未指定本参数，将显示所有单板上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1280863333}[：显示指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况，]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。（分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备]{style="font-family:宋体"}[/]{lang="EN-US"}[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654355533}

[[如果指定的单板]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x4306_x6993_x487297227}[成员设备不支持统计]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源，将不会显示该单板]{style="font-family:宋体"}[/]{lang="EN-US"}[成员设备上]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1788829161}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_2041337956}[显示]{style="font-family:宋体"}[QoS]{lang="EN-US"}[和]{style="font-family:宋体"}[ACL]{lang="EN-US"}[资源的使用情况。]{style="font-family:宋体"}

[[\<Sysname\> display qos-acl resource]{lang="EN-US"}]{#struct_0_x4306_x6993_x664866906}

[Interfaces: GE1/0/1 to GE1/0/2]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Type             Total      Reserved   Configured Remaining  Usage]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ IPv4 ACL         2048       512        0          1536       25%]{lang="EN-US"}

[ IPv6 ACL         8192       1536       6656       0          100%]{lang="EN-US"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1269244567}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的显示信息与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x334066241}
:::

[ ]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display qos-acl resource]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654158925}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x392371970}[[字段]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2144295023}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x404629184}

[[Interfaces]{lang="EN-US"}]{#struct_0_x4306_x6993_828836639}

[[资源对应的接口范围]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2084141721}

[[Type]{lang="EN-US"}]{#struct_0_x4306_x6993_x604446935}

[[资源类型]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1542838938}

[[Total]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654224461}

[[资源总数]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1616198683}

[[Reserved]{lang="EN-US"}]{#struct_0_x4306_x6993_2040010669}

[[预留的资源数]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2035365723}

[[Configured]{lang="EN-US"}]{#struct_0_x4306_x6993_x168312590}

[[已经配置的资源数]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1765340638}

[[Remaining]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654027853}

[[剩余可用的资源数]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1378212531}

[[Usage]{lang="EN-US"}]{#struct_0_x4306_x6993_x604168580}

[[预留的资源数与已配置的资源数之和占资源总数的百分比，分子按实际计算结果的整数部分显示，例如实际计算结果为]{style="font-family:宋体"}[50.8%]{lang="EN-US"}]{#struct_0_x4306_x6993_x1260546642}[，此处显示为]{style="font-family:宋体"}[50%]{lang="EN-US"}[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1895196118 .myid}
[]{#_Toc404791891}[]{#struct_0_x4306_x6993_x1024595384}[]{#_Toc291080251}

**ACL \-- ACL配置命令 \-- packet-filter(Interface view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x493208901}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1654093389}
:::

[ ]{lang="EN-US"}

[**[packet-filter]{lang="EN-US"}**]{#struct_0_x4306_x6993_2094489201}[命令用来在接口上应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_363475773}[命令用来取消在接口上应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x579490069}

[**[packet-filter]{lang="EN-US"}**[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } { **inbound** \[ **extension** \] \| **outbound** } \[ **hardware-count** \]]{lang="EN-US"}]{#struct_0_x4306_x6993_1579549316}

[**[undo]{lang="EN-US"}**[ **packet-filter** \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x4306_x6993_864033519}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1206976503}

[[接口不对报文进行过滤。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_80153593}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1641424495}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654552144}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x769733374}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_2079948600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1349747301}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1984299922}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1599604953}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2070795565}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_446183889}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_x250044288}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_1630019377}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_x370719394}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654617680}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1497010671}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1587060874}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_65323639}[：对收到的报文进行过滤。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_x4306_x6993_1510185090}[：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x429885167}[：对发出的报文进行过滤。]{style="font-family:宋体"}

[**[hardware-count]{lang="EN-US"}**]{#struct_0_x4306_x6993_x887249911}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能，而]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[counting]{lang="EN-US"}**[参数则用于使能当前规则的匹配统计功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x163618099}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x772982506}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[关键字，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1353323530}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x281884826}[应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收到的报文进行过滤，并对过滤的报文进行统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654421072}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] packet-filter 2001 inbound hardware-count]{lang="EN-US"}

[]{#_Toc223269549}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x556636656}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1841875155}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1847803503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **verbose**]{lang="EN-US"}]{#struct_0_x4306_x6993_1327862262}
:::::

::::: {#-2029220924 .myid}
[]{#_Toc404791892}[]{#struct_0_x4306_x6993_x1280928870}[]{#_Toc362080664}[]{#_Toc357591537}

**ACL \-- ACL配置命令 \-- packet-filter(Zone-pair security view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 8 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281125478}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1281059942}
:::

[ ]{lang="EN-US"}

[**[packet-filter]{lang="EN-US"}**]{#struct_0_x4306_x6993_1125885124}[命令用来在安全域间实例上应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281256550}[命令用来取消在安全域间实例上应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1281191014}

[**[packet-filter]{lang="EN-US"}**[ \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1281387622}

[**[undo]{lang="EN-US"}**[ **packet-filter** \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } ]{lang="EN-US"}]{#struct_0_x4306_x6993_564659042}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1281322086}

[[安全]{style="font-family:宋体"}]{#struct_0_x4306_x6993_285220612}[域间实例不对报文进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_285286148}

[[安全]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1748673269}[域间实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_285089540}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_285155076}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1251010379}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_284958468}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1955900849}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。若未指定本参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_285024004}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_683808842}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：表示基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_284827396}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_284892932}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_284696324}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_2127282541}[应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2002]{lang="EN-US"}[对安全域间实例]{style="font-family:宋体"}[source office destination library]{lang="EN-US"}[收到的报文进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_284761860}

[\[Sysname\] zone-pair security source office destination library]{lang="EN-US"}

[\[Sysname-zone-pair-security-office-library\] packet-filter 2002]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_285220611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_285286147}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_1748673268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display packet-filter verbose]{lang="EN-US"}**]{#struct_0_x4306_x6993_285089539}
:::::

::::: {#-1043926206 .myid}
[]{#_Toc291080252}[]{#_Toc404791893}[]{#struct_0_x4306_x6993_1191713812}

**ACL \-- ACL配置命令 \-- packet-filter default deny**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1540294020}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1354199309}
:::

[ ]{lang="EN-US"}

[**[packet-filter]{lang="EN-US"}**[ **default** **deny**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1571156176}[命令用来配置报文过滤的缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[，即禁止未匹配上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的报文通过。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter** **default** **deny**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654486608}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1437115478}

[**[packet-filter]{lang="EN-US"}**[ **default** **deny**]{lang="EN-US"}]{#struct_0_x4306_x6993_251317752}

[**[undo]{lang="EN-US"}**[ **packet-filter** **default** **deny**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1817350949}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_488940705}

[[报文过滤的缺省动作为]{style="font-family:宋体"}[Permit]{lang="EN-US"}]{#struct_0_x4306_x6993_x5455671}[，即允许未匹配上]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的报文通过。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_989195147}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1095303942}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1167457019}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654290000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_310914611}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_242549888}

[[配置报文过滤的缺省动作会在所有的应用对象下添加一个缺省动作应用，该应用也会像其它应用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x985084749}[一样显示。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_469833326}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_15263155}[配置报文过滤的缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1230322091}

[\[Sysname\] packet-filter default deny]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_790382528}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654355536}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_272217660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **verbose**]{lang="EN-US"}]{#struct_0_x4306_x6993_1533558215}
:::::

::::: {#2144871022 .myid}
[]{#_Toc404791894}[]{#struct_0_x4306_x6993_1009105230}[]{#_Toc303846685}[]{#_Toc303847800}[]{#_Toc303848709}[]{#_Toc303849338}[]{#_Toc303850277}[]{#_Toc303857877}

**ACL \-- ACL配置命令 \-- packet-filter default hardware-count**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 9 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1513133359}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x890436792}
:::

[ ]{lang="EN-US"}

[**[packet-filter]{lang="EN-US"}**[ **default** **hardware-count**]{lang="EN-US"}]{#struct_0_x4306_x6993_1869549410}[命令用来在接口上使能报文过滤缺省动作统计功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter** **default** **hardware-count**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1405082899}[命令用来在接口上关闭报文过滤缺省动作统计功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x794434019}

[**[packet-filter]{lang="EN-US"}**[ **default** { **inbound** \| **outbound** } **hardware-count**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654158928}

[**[undo]{lang="EN-US"}**[ **packet-filter** **default** { **inbound** \| **outbound** } **hardware-count**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1391157386}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1103717009}

[[报文过滤缺省动作统计功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_977204687}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1488588343}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_406049267}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1394923386}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1198543087}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1983456623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654224464}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_1919253726}[：表示收到的报文。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_907257748}[：表示发出的报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_160209291}

[[在接口上只有应用了]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1077658956}[进行报文过滤，才允许使能报文过滤缺省动作统计功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1127500599}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_1740976966}[配置报文过滤的缺省动作为]{style="font-family:宋体"}[Deny]{lang="EN-US"}[，在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上对收到的报文应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[进行过滤，并使能报文过滤缺省动作统计功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654027856}

[\[Sysname\] packet-filter default deny]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] packet-filter 2001 inbound]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] packet-filter default inbound hardware-count]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_618697644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet-filter]{lang="EN-US"}**]{#struct_0_x4306_x6993_225199054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[packet-filter]{lang="EN-US"}**[ **default** **deny**]{lang="EN-US"}]{#struct_0_x4306_x6993_2008487747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_1627092410}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_712252694}
:::::

::::: {#-1239422629 .myid}
[]{#_Toc404791895}[]{#struct_0_x4306_x6993_x1122094971}

**ACL \-- ACL配置命令 \-- packet-filter global**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 10 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x384528251}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1448976376}
:::

**[ ]{lang="EN-US"}**

[**[packet-filter]{lang="EN-US"}**[ **global**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654093392}[命令用来全局应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter** **global**]{lang="EN-US"}]{#struct_0_x4306_x6993_1335039850}[命令用来取消全局应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1825523035}

[**[packet-filter]{lang="EN-US"}**[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } **global** { **inbound** \[ **extension** \] \| **outbound** } \[ **hardware-count** \]]{lang="EN-US"}]{#struct_0_x4306_x6993_579834125}

[**[undo]{lang="EN-US"}**[ **packet-filter** \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } **global** { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x4306_x6993_953144107}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1958429278}

[[全局不对报文进行过滤。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1778063831}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2103001634}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1602671719}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654552143}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x366448847}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1476361328}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_425312401}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x13467619}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_1968175526}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1667392846}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1221509824}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_2030754386}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_96613895}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1755048771}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654617679}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x286174050}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_x4306_x6993_693638864}[：表示全局（即所有物理接口）配置。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1206084657}[：对收到的报文进行过滤。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_x4306_x6993_389816908}[：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_671464744}[：对发出的报文进行过滤。]{style="font-family:宋体"}

[**[hardware-count]{lang="EN-US"}**]{#struct_0_x4306_x6993_x157132016}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能，而]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[counting]{lang="EN-US"}**[参数则用于使能当前规则的匹配统计功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2114664081}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x889337014}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_406718673}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_177207819}[全局应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[对收到的报文进行过滤，并对过滤的报文进行统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654421071}

[\[Sysname\] packet-filter 2001 global inbound hardware-count]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x959921183}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_1896906331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_x94682949}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **verbose**]{lang="EN-US"}]{#struct_0_x4306_x6993_x458806452}
:::::

::::: {#-1985638818 .myid}
[]{#_Toc404791896}[]{#struct_0_x4306_x6993_1351563110}

**ACL \-- ACL配置命令 \-- packet-filter vlan**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 11 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x1305688418}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x753118055}
:::

**[ ]{lang="EN-US"}**

[**[packet-filter]{lang="EN-US"}**[ **vlan**]{lang="EN-US"}]{#struct_0_x4306_x6993_957716184}[命令用来在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **packet-filter** **vlan**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654486607}[命令用来取消在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中应用]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行报文过滤。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1647998237}

[**[packet-filter]{lang="EN-US"}**[ \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } **vlan** *vlan-list* { **inbound** \[ **extension** \] \| **outbound** } \[ **hardware-count** \]]{lang="EN-US"}]{#struct_0_x4306_x6993_88884514}

[**[undo]{lang="EN-US"}**[ **packet-filter** \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } **vlan** *vlan-list* { **inbound** \| **outbound** }]{lang="EN-US"}]{#struct_0_x4306_x6993_691985685}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1619120603}

[[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x4306_x6993_2137523461}[中不对报文进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x472613542}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x100173984}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1609202748}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654289999}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1891899634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1148141107}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1176267033}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1929797476}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x7811474}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_845133906}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1685557446}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_1302610307}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_2083988392}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_x34093881}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1649587852}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[vlan]{lang="NL"}**]{#struct_0_x4306_x6993_x1654355535}[ *vlan-list*]{lang="NL"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[VLAN]{lang="NL"}[。]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ **to** *vlan-id* \] }&\<1-10\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号，不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}[&\<1-10\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_675502187}[：对收到的报文进行过滤。]{style="font-family:宋体"}

[**[extension]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1129212866}[：对报文过滤进行扩展应用。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_904696561}[：对发出的报文进行过滤。]{style="font-family:宋体"}

[**[hardware-count]{lang="EN-US"}**]{#struct_0_x4306_x6993_1227425015}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能，而]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[counting]{lang="EN-US"}**[参数则用于使能当前规则的匹配统计功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1511513386}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x512252232}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1024644490}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1861787335}[在]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中应用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[对收到的报文进行过滤，并对过滤的报文进行统计。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_2042557353}

[\[Sysname\] packet-filter 2001 vlan 2 inbound hardware-count]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1108668532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1722759043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654158927}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **verbose**]{lang="EN-US"}]{#struct_0_x4306_x6993_x987872859}
:::::

::: {#-827398710 .myid}
[]{#_Toc404791897}[]{#struct_0_x4306_x6993_x47424461}[]{#_Toc303846688}[]{#_Toc303847803}[]{#_Toc303848712}[]{#_Toc303849341}[]{#_Toc303850280}[]{#_Toc303857880}[]{#_Toc303846689}[]{#_Toc303847804}[]{#_Toc303848713}[]{#_Toc303849342}[]{#_Toc303850281}[]{#_Toc303857881}[]{#_Toc303846690}[]{#_Toc303847805}[]{#_Toc303848714}[]{#_Toc303849343}[]{#_Toc303850282}[]{#_Toc303857882}[]{#_Toc303846691}[]{#_Toc303847806}[]{#_Toc303848715}[]{#_Toc303849344}[]{#_Toc303850283}[]{#_Toc303857883}[]{#_Toc303846692}[]{#_Toc303847807}[]{#_Toc303848716}[]{#_Toc303849345}[]{#_Toc303850284}[]{#_Toc303857884}[]{#_Toc303846693}[]{#_Toc303847808}[]{#_Toc303848717}[]{#_Toc303849346}[]{#_Toc303850285}[]{#_Toc303857885}[]{#_Toc303846694}[]{#_Toc303847809}[]{#_Toc303848718}[]{#_Toc303849347}[]{#_Toc303850286}[]{#_Toc303857886}[]{#_Toc303846695}[]{#_Toc303847810}[]{#_Toc303848719}[]{#_Toc303849348}[]{#_Toc303850287}[]{#_Toc303857887}[]{#_Toc303846696}[]{#_Toc303847811}[]{#_Toc303848720}[]{#_Toc303849349}[]{#_Toc303850288}[]{#_Toc303857888}[]{#_Toc303846697}[]{#_Toc303847812}[]{#_Toc303848721}[]{#_Toc303849350}[]{#_Toc303850289}[]{#_Toc303857889}[]{#_Toc303846698}[]{#_Toc303847813}[]{#_Toc303848722}[]{#_Toc303849351}[]{#_Toc303850290}[]{#_Toc303857890}[]{#_Toc303846699}[]{#_Toc303847814}[]{#_Toc303848723}[]{#_Toc303849352}[]{#_Toc303850291}[]{#_Toc303857891}[]{#_Toc303846700}[]{#_Toc303847815}[]{#_Toc303848724}[]{#_Toc303849353}[]{#_Toc303850292}[]{#_Toc303857892}[]{#_Toc303846701}[]{#_Toc303847816}[]{#_Toc303848725}[]{#_Toc303849354}[]{#_Toc303850293}[]{#_Toc303857893}[]{#_Toc303846702}[]{#_Toc303847817}[]{#_Toc303848726}[]{#_Toc303849355}[]{#_Toc303850294}[]{#_Toc303857894}[]{#_Toc303846703}[]{#_Toc303847818}[]{#_Toc303848727}[]{#_Toc303849356}[]{#_Toc303850295}[]{#_Toc303857895}[]{#_Toc303846704}[]{#_Toc303847819}[]{#_Toc303848728}[]{#_Toc303849357}[]{#_Toc303850296}[]{#_Toc303857896}[]{#_Toc303846705}[]{#_Toc303847820}[]{#_Toc303848729}[]{#_Toc303849358}[]{#_Toc303850297}[]{#_Toc303857897}[]{#_Toc303846706}[]{#_Toc303847821}[]{#_Toc303848730}[]{#_Toc303849359}[]{#_Toc303850298}[]{#_Toc303857898}[]{#_Toc303846707}[]{#_Toc303847822}[]{#_Toc303848731}[]{#_Toc303849360}[]{#_Toc303850299}[]{#_Toc303857899}[]{#_Toc303846708}[]{#_Toc303847823}[]{#_Toc303848732}[]{#_Toc303849361}[]{#_Toc303850300}[]{#_Toc303857900}[]{#_Toc303846709}[]{#_Toc303847824}[]{#_Toc303848733}[]{#_Toc303849362}[]{#_Toc303850301}[]{#_Toc303857901}[]{#_Toc303846710}[]{#_Toc303847825}[]{#_Toc303848734}[]{#_Toc303849363}[]{#_Toc303850302}[]{#_Toc303857902}[]{#_Toc303846711}[]{#_Toc303847826}[]{#_Toc303848735}[]{#_Toc303849364}[]{#_Toc303850303}[]{#_Toc303857903}[]{#_Toc303846712}[]{#_Toc303847827}[]{#_Toc303848736}[]{#_Toc303849365}[]{#_Toc303850304}[]{#_Toc303857904}[]{#_Toc303846713}[]{#_Toc303847828}[]{#_Toc303848737}[]{#_Toc303849366}[]{#_Toc303850305}[]{#_Toc303857905}[]{#_Toc303846714}[]{#_Toc303847829}[]{#_Toc303848738}[]{#_Toc303849367}[]{#_Toc303850306}[]{#_Toc303857906}[]{#_Toc303846715}[]{#_Toc303847830}[]{#_Toc303848739}[]{#_Toc303849368}[]{#_Toc303850307}[]{#_Toc303857907}[]{#_Toc303846716}[]{#_Toc303847831}[]{#_Toc303848740}[]{#_Toc303849369}[]{#_Toc303850308}[]{#_Toc303857908}[]{#_Toc303846717}[]{#_Toc303847832}[]{#_Toc303848741}[]{#_Toc303849370}[]{#_Toc303850309}[]{#_Toc303857909}[]{#_Toc303846718}[]{#_Toc303847833}[]{#_Toc303848742}[]{#_Toc303849371}[]{#_Toc303850310}[]{#_Toc303857910}[]{#_Toc303846719}[]{#_Toc303847834}[]{#_Toc303848743}[]{#_Toc303849372}[]{#_Toc303850311}[]{#_Toc303857911}[]{#_Toc303846720}[]{#_Toc303847835}[]{#_Toc303848744}[]{#_Toc303849373}[]{#_Toc303850312}[]{#_Toc303857912}[]{#_Toc303846721}[]{#_Toc303847836}[]{#_Toc303848745}[]{#_Toc303849374}[]{#_Toc303850313}[]{#_Toc303857913}[]{#_Toc303846722}[]{#_Toc303847837}[]{#_Toc303848746}[]{#_Toc303849375}[]{#_Toc303850314}[]{#_Toc303857914}[]{#_Toc303846723}[]{#_Toc303847838}[]{#_Toc303848747}[]{#_Toc303849376}[]{#_Toc303850315}[]{#_Toc303857915}[]{#_Toc303846724}[]{#_Toc303847839}[]{#_Toc303848748}[]{#_Toc303849377}[]{#_Toc303850316}[]{#_Toc303857916}[]{#_Toc303846725}[]{#_Toc303847840}[]{#_Toc303848749}[]{#_Toc303849378}[]{#_Toc303850317}[]{#_Toc303857917}[]{#_Toc303846726}[]{#_Toc303847841}[]{#_Toc303848750}[]{#_Toc303849379}[]{#_Toc303850318}[]{#_Toc303857918}[]{#_Toc303846727}[]{#_Toc303847842}[]{#_Toc303848751}[]{#_Toc303849380}[]{#_Toc303850319}[]{#_Toc303857919}[]{#_Toc303846728}[]{#_Toc303847843}[]{#_Toc303848752}[]{#_Toc303849381}[]{#_Toc303850320}[]{#_Toc303857920}[]{#_Toc303846729}[]{#_Toc303847844}[]{#_Toc303848753}[]{#_Toc303849382}[]{#_Toc303850321}[]{#_Toc303857921}[]{#_Toc303846730}[]{#_Toc303847845}[]{#_Toc303848754}[]{#_Toc303849383}[]{#_Toc303850322}[]{#_Toc303857922}[]{#_Toc303846731}[]{#_Toc303847846}[]{#_Toc303848755}[]{#_Toc303849384}[]{#_Toc303850323}[]{#_Toc303857923}[]{#_Toc303846732}[]{#_Toc303847847}[]{#_Toc303848756}[]{#_Toc303849385}[]{#_Toc303850324}[]{#_Toc303857924}[]{#_Toc303846733}[]{#_Toc303847848}[]{#_Toc303848757}[]{#_Toc303849386}[]{#_Toc303850325}[]{#_Toc303857925}[]{#_Toc303846734}[]{#_Toc303847849}[]{#_Toc303848758}[]{#_Toc303849387}[]{#_Toc303850326}[]{#_Toc303857926}[]{#_Toc303846735}[]{#_Toc303847850}[]{#_Toc303848759}[]{#_Toc303849388}[]{#_Toc303850327}[]{#_Toc303857927}[]{#_Toc303846736}[]{#_Toc303847851}[]{#_Toc303848760}[]{#_Toc303849389}[]{#_Toc303850328}[]{#_Toc303857928}[]{#_Toc303846737}[]{#_Toc303847852}[]{#_Toc303848761}[]{#_Toc303849390}[]{#_Toc303850329}[]{#_Toc303857929}[]{#_Toc303846738}[]{#_Toc303847853}[]{#_Toc303848762}[]{#_Toc303849391}[]{#_Toc303850330}[]{#_Toc303857930}[]{#_Toc303846739}[]{#_Toc303847854}[]{#_Toc303848763}[]{#_Toc303849392}[]{#_Toc303850331}[]{#_Toc303857931}[]{#_Toc303846740}[]{#_Toc303847855}[]{#_Toc303848764}[]{#_Toc303849393}[]{#_Toc303850332}[]{#_Toc303857932}[]{#_Toc303846741}[]{#_Toc303847856}[]{#_Toc303848765}[]{#_Toc303849394}[]{#_Toc303850333}[]{#_Toc303857933}[]{#_Toc303846742}[]{#_Toc303847857}[]{#_Toc303848766}[]{#_Toc303849395}[]{#_Toc303850334}[]{#_Toc303857934}[]{#_Toc303846743}[]{#_Toc303847858}[]{#_Toc303848767}[]{#_Toc303849396}[]{#_Toc303850335}[]{#_Toc303857935}[]{#_Toc303846744}[]{#_Toc303847859}[]{#_Toc303848768}[]{#_Toc303849397}[]{#_Toc303850336}[]{#_Toc303857936}[]{#_Toc303846745}[]{#_Toc303847860}[]{#_Toc303848769}[]{#_Toc303849398}[]{#_Toc303850337}[]{#_Toc303857937}[]{#_Toc303846746}[]{#_Toc303847861}[]{#_Toc303848770}[]{#_Toc303849399}[]{#_Toc303850338}[]{#_Toc303857938}[]{#_Toc303846747}[]{#_Toc303847862}[]{#_Toc303848771}[]{#_Toc303849400}[]{#_Toc303850339}[]{#_Toc303857939}[]{#_Toc303846748}[]{#_Toc303847863}[]{#_Toc303848772}[]{#_Toc303849401}[]{#_Toc303850340}[]{#_Toc303857940}[]{#_Toc303846749}[]{#_Toc303847864}[]{#_Toc303848773}[]{#_Toc303849402}[]{#_Toc303850341}[]{#_Toc303857941}[]{#_Toc303846750}[]{#_Toc303847865}[]{#_Toc303848774}[]{#_Toc303849403}[]{#_Toc303850342}[]{#_Toc303857942}[]{#_Toc303846751}[]{#_Toc303847866}[]{#_Toc303848775}[]{#_Toc303849404}[]{#_Toc303850343}[]{#_Toc303857943}[]{#_Toc303846752}[]{#_Toc303847867}[]{#_Toc303848776}[]{#_Toc303849405}[]{#_Toc303850344}[]{#_Toc303857944}[]{#_Toc303846753}[]{#_Toc303847868}[]{#_Toc303848777}[]{#_Toc303849406}[]{#_Toc303850345}[]{#_Toc303857945}[]{#_Toc303846754}[]{#_Toc303847869}[]{#_Toc303848778}[]{#_Toc303849407}[]{#_Toc303850346}[]{#_Toc303857946}[]{#_Toc303846755}[]{#_Toc303847870}[]{#_Toc303848779}[]{#_Toc303849408}[]{#_Toc303850347}[]{#_Toc303857947}[]{#_Toc303846756}[]{#_Toc303847871}[]{#_Toc303848780}[]{#_Toc303849409}[]{#_Toc303850348}[]{#_Toc303857948}[]{#_Toc303846757}[]{#_Toc303847872}[]{#_Toc303848781}[]{#_Toc303849410}[]{#_Toc303850349}[]{#_Toc303857949}[]{#_Toc303846758}[]{#_Toc303847873}[]{#_Toc303848782}[]{#_Toc303849411}[]{#_Toc303850350}[]{#_Toc303857950}[]{#_Toc303846759}[]{#_Toc303847874}[]{#_Toc303848783}[]{#_Toc303849412}[]{#_Toc303850351}[]{#_Toc303857951}[]{#_Toc303846760}[]{#_Toc303847875}[]{#_Toc303848784}[]{#_Toc303849413}[]{#_Toc303850352}[]{#_Toc303857952}[]{#_Toc303846761}[]{#_Toc303847876}[]{#_Toc303848785}[]{#_Toc303849414}[]{#_Toc303850353}[]{#_Toc303857953}[]{#_Toc303846762}[]{#_Toc303847877}[]{#_Toc303848786}[]{#_Toc303849415}[]{#_Toc303850354}[]{#_Toc303857954}[]{#_Toc303846763}[]{#_Toc303847878}[]{#_Toc303848787}[]{#_Toc303849416}[]{#_Toc303850355}[]{#_Toc303857955}[]{#_Toc303846764}[]{#_Toc303847879}[]{#_Toc303848788}[]{#_Toc303849417}[]{#_Toc303850356}[]{#_Toc303857956}[]{#_Toc303846765}[]{#_Toc303847880}[]{#_Toc303848789}[]{#_Toc303849418}[]{#_Toc303850357}[]{#_Toc303857957}[]{#_Toc303846766}[]{#_Toc303847881}[]{#_Toc303848790}[]{#_Toc303849419}[]{#_Toc303850358}[]{#_Toc303857958}[]{#_Toc303846767}[]{#_Toc303847882}[]{#_Toc303848791}[]{#_Toc303849420}[]{#_Toc303850359}[]{#_Toc303857959}[]{#_Toc303846768}[]{#_Toc303847883}[]{#_Toc303848792}[]{#_Toc303849421}[]{#_Toc303850360}[]{#_Toc303857960}[]{#_Toc303846769}[]{#_Toc303847884}[]{#_Toc303848793}[]{#_Toc303849422}[]{#_Toc303850361}[]{#_Toc303857961}[]{#_Toc303846770}[]{#_Toc303847885}[]{#_Toc303848794}[]{#_Toc303849423}[]{#_Toc303850362}[]{#_Toc303857962}[]{#_Toc303846771}[]{#_Toc303847886}[]{#_Toc303848795}[]{#_Toc303849424}[]{#_Toc303850363}[]{#_Toc303857963}[]{#_Toc303846772}[]{#_Toc303847887}[]{#_Toc303848796}[]{#_Toc303849425}[]{#_Toc303850364}[]{#_Toc303857964}[]{#_Toc303846773}[]{#_Toc303847888}[]{#_Toc303848797}[]{#_Toc303849426}[]{#_Toc303850365}[]{#_Toc303857965}[]{#_Toc303846774}[]{#_Toc303847889}[]{#_Toc303848798}[]{#_Toc303849427}[]{#_Toc303850366}[]{#_Toc303857966}[]{#_Toc303846775}[]{#_Toc303847890}[]{#_Toc303848799}[]{#_Toc303849428}[]{#_Toc303850367}[]{#_Toc303857967}[]{#_Toc303846776}[]{#_Toc303847891}[]{#_Toc303848800}[]{#_Toc303849429}[]{#_Toc303850368}[]{#_Toc303857968}[]{#_Toc303846777}[]{#_Toc303847892}[]{#_Toc303848801}[]{#_Toc303849430}[]{#_Toc303850369}[]{#_Toc303857969}[]{#_Toc303846778}[]{#_Toc303847893}[]{#_Toc303848802}[]{#_Toc303849431}[]{#_Toc303850370}[]{#_Toc303857970}[]{#_Toc303846779}[]{#_Toc303847894}[]{#_Toc303848803}[]{#_Toc303849432}[]{#_Toc303850371}[]{#_Toc303857971}[]{#_Toc303846780}[]{#_Toc303847895}[]{#_Toc303848804}[]{#_Toc303849433}[]{#_Toc303850372}[]{#_Toc303857972}[]{#_Toc303846781}[]{#_Toc303847896}[]{#_Toc303848805}[]{#_Toc303849434}[]{#_Toc303850373}[]{#_Toc303857973}[]{#_Toc303846782}[]{#_Toc303847897}[]{#_Toc303848806}[]{#_Toc303849435}[]{#_Toc303850374}[]{#_Toc303857974}[]{#_Toc303846783}[]{#_Toc303847898}[]{#_Toc303848807}[]{#_Toc303849436}[]{#_Toc303850375}[]{#_Toc303857975}[]{#_Toc303846784}[]{#_Toc303847899}[]{#_Toc303848808}[]{#_Toc303849437}[]{#_Toc303850376}[]{#_Toc303857976}[]{#_Toc303846785}[]{#_Toc303847900}[]{#_Toc303848809}[]{#_Toc303849438}[]{#_Toc303850377}[]{#_Toc303857977}[]{#_Toc303846786}[]{#_Toc303847901}[]{#_Toc303848810}[]{#_Toc303849439}[]{#_Toc303850378}[]{#_Toc303857978}

**ACL \-- ACL配置命令 \-- reset acl counter**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **acl** **counter**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1419914168}[命令用来清除]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1132611144}

[**[reset]{lang="EN-US"}**[ **acl** \[ **ipv6** \| **mac** \| **user-defined** \] **counter** { *acl-number* \| **all** \| **name** *acl-name* }]{lang="EN-US"}]{#struct_0_x4306_x6993_137863226}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1731272181}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x570950006}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x581041437}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654224463}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1515969199}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1179006017}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1599670489}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_x50702222}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x997324983}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_1080815784}[：清除指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x337330823}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1065229772}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_1179970642}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_1494037476}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1540305587}[：清除指定类型中全部]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654027855}[：清除指定名称]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x772916970}

[[若未指定]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x462307710}[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_215413117}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_128426893}[清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset acl counter 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x1447767335}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1309808108}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x329117326}
:::

::::: {#925175543 .myid}
[]{#_Toc291080257}[]{#_Toc404791898}[]{#struct_0_x4306_x6993_608144440}[]{#_Toc303850380}[]{#_Toc303857980}[]{#_Toc303850381}[]{#_Toc303857981}[]{#_Toc303850382}[]{#_Toc303857982}[]{#_Toc303850383}[]{#_Toc303857983}[]{#_Toc303850384}[]{#_Toc303857984}[]{#_Toc303850385}[]{#_Toc303857985}[]{#_Toc303850386}[]{#_Toc303857986}[]{#_Toc303850387}[]{#_Toc303857987}[]{#_Toc303850388}[]{#_Toc303857988}[]{#_Toc303850389}[]{#_Toc303857989}[]{#_Toc303850390}[]{#_Toc303857990}[]{#_Toc303850391}[]{#_Toc303857991}[]{#_Toc303850392}[]{#_Toc303857992}[]{#_Toc303850393}[]{#_Toc303857993}[]{#_Toc303850394}[]{#_Toc303857994}[]{#_Toc303850395}[]{#_Toc303857995}[]{#_Toc303850396}[]{#_Toc303857996}[]{#_Toc303850397}[]{#_Toc303857997}[]{#_Toc303850398}[]{#_Toc303857998}[]{#_Toc303850399}[]{#_Toc303857999}

**ACL \-- ACL配置命令 \-- reset packet-filter statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image001.jpg){#图片 15 border="0" width="62" height="24"}]{lang="EN-US"}]{#struct_0_x4306_x6993_46934997}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1654093391}
:::

[ ]{lang="EN-US"}

[**[reset]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_1738324377}[命令用来清除]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息（包括累加统计信息）以及报文过滤缺省动作的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_866206418}

[**[reset]{lang="EN-US"}**[ **packet-filter** **statistics** { { **global** \| **interface** \[ *interface-type* *interface-number* \] \| **vlan** \[ *vlan-id* \] } { **inbound** \| **outbound** } \[ **default** \| \[ **ipv6** \| **mac** \| **user-defined** \] { *acl-number* \| **name** *acl-name* } \] \| **zone-pair security** \[ **source** *source-zone-name* **destination** *destination-zone-name* \] \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \] }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1173733432}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x491187343}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4306_x6993_265067065}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1369368364}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1468549249}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1721901800}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654552146}

[**[global]{lang="EN-US"}**]{#struct_0_x4306_x6993_393066040}[：清除全局（即所有物理接口）统计信息。]{style="font-family:宋体"}

[**[interface]{lang="EN-US"}**[ \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x3994405}[：清除指定接口上的统计信息。]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[表示接口类型和接口编号。若未指定接口类型和接口编号，将清除所有接口上的统计信息。]{style="font-family:宋体"}

[**[zone-pair security ]{lang="EN-US"}**[\[ **source** *source-zone-name* **destination** *destination-zone-name* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_284892929}[：清除指定接口上的统计信息。]{style="font-family:宋体"}*[source-zone-name]{lang="EN-US"}*[：表示安全域间实例源安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}*[destination-zone-name]{lang="FR"}*[：表示安全域间实例目的安全域的名称，为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串，不区分大小写。]{style="font-family:
宋体"}

[**[vlan]{lang="EN-US"}**[ \[ *vlan-id* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_1981957992}[：清除指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的统计信息。]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的编号。若未指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，将清除所有]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中的统计信息。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1197222875}[：清除入方向上的统计信息。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x4306_x6993_x773113454}[：清除出方向上的统计信息。]{style="font-family:宋体"}

[**[default]{lang="EN-US"}**]{#struct_0_x4306_x6993_x482183535}[：清除缺省动作在报文过滤中应用的统计信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_1955966385}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x4306_x6993_645359696}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[user-defined]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2119546081}[：指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4306_x6993_812240843}[：清除指定编号]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下（不同型号的设备支持的取值范围不同，请以设备的实际情况为准）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1181355556}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：]{lang="EN-US" style="font-family:宋体"}[表示基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654617682}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[：表示高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[4000]{lang="EN-US"}]{#struct_0_x4306_x6993_x334211257}[～]{style="font-family:宋体"}[4999]{lang="EN-US"}[：表示二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[5000]{lang="EN-US"}]{#struct_0_x4306_x6993_1836150097}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[：表示用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1773147381}[：清除指定名称]{style="font-family:宋体"}[ACL]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1644725274}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{lang="EN-US" style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1061287871}[、]{lang="EN-US" style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[和]{lang="EN-US" style="font-family:宋体"}**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}[参数，将清除全部]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[（若指定]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[关键字，表示全部]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[；若指定]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[关键字，表示全部二层]{style="font-family:宋体"}[ ACL]{lang="EN-US"}[；若指定]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[关键字，则表示全部用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[；否则，表示全部]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[4]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[4]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[）和缺省动作在报文过滤中应用的统计信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[清除安全域间实例统计信息时不区分方向且不支持]{style="font-family:宋体"}]{#struct_0_x4306_x6993_285286144}**[default]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若未指定]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1935716384}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[mac]{lang="EN-US"}**[或]{style="font-family:宋体"}**[user-defined]{lang="EN-US"}**[参数]{lang="EN-US" style="font-family:宋体"}[，则表示]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x540031210}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_739149061}[清除]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[中入方向上]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2001]{lang="EN-US"}[在报文过滤中应用的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset packet-filter statistics vlan 2 inbound 2001]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654421074}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1719436070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics**]{lang="EN-US"}]{#struct_0_x4306_x6993_589628016}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **packet-filter** **statistics sum**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1619310619}
:::::

::::: {#-1948660696 .myid}
[]{#_Toc404791899}[]{#struct_0_x4306_x6993_x1674655342}[]{#_Toc303847905}[]{#_Toc303848814}[]{#_Toc303849443}[]{#_Toc303850401}[]{#_Toc303858001}[]{#_Toc303847906}[]{#_Toc303848815}[]{#_Toc303849444}[]{#_Toc303850402}[]{#_Toc303858002}[]{#_Toc303847907}[]{#_Toc303848816}[]{#_Toc303849445}[]{#_Toc303850403}[]{#_Toc303858003}[]{#_Toc303847908}[]{#_Toc303848817}[]{#_Toc303849446}[]{#_Toc303850404}[]{#_Toc303858004}[]{#_Toc303847909}[]{#_Toc303848818}[]{#_Toc303849447}[]{#_Toc303850405}[]{#_Toc303858005}[]{#_Toc303847910}[]{#_Toc303848819}[]{#_Toc303849448}[]{#_Toc303850406}[]{#_Toc303858006}[]{#_Toc303847911}[]{#_Toc303848820}[]{#_Toc303849449}[]{#_Toc303850407}[]{#_Toc303858007}[]{#_Toc303847912}[]{#_Toc303848821}[]{#_Toc303849450}[]{#_Toc303850408}[]{#_Toc303858008}[]{#_Toc303847913}[]{#_Toc303848822}[]{#_Toc303849451}[]{#_Toc303850409}[]{#_Toc303858009}[]{#_Toc303847914}[]{#_Toc303848823}[]{#_Toc303849452}[]{#_Toc303850410}[]{#_Toc303858010}[]{#_Toc303847915}[]{#_Toc303848824}[]{#_Toc303849453}[]{#_Toc303850411}[]{#_Toc303858011}[]{#_Toc303847916}[]{#_Toc303848825}[]{#_Toc303849454}[]{#_Toc303850412}[]{#_Toc303858012}[]{#_Toc303847917}[]{#_Toc303848826}[]{#_Toc303849455}[]{#_Toc303850413}[]{#_Toc303858013}[]{#_Toc303847918}[]{#_Toc303848827}[]{#_Toc303849456}[]{#_Toc303850414}[]{#_Toc303858014}[]{#_Toc303847919}[]{#_Toc303848828}[]{#_Toc303849457}[]{#_Toc303850415}[]{#_Toc303858015}[]{#_Toc303847920}[]{#_Toc303848829}[]{#_Toc303849458}[]{#_Toc303850416}[]{#_Toc303858016}[]{#_Toc303847921}[]{#_Toc303848830}[]{#_Toc303849459}[]{#_Toc303850417}[]{#_Toc303858017}[]{#_Toc303847922}[]{#_Toc303848831}[]{#_Toc303849460}[]{#_Toc303850418}[]{#_Toc303858018}[]{#_Toc303847923}[]{#_Toc303848832}[]{#_Toc303849461}[]{#_Toc303850419}[]{#_Toc303858019}[]{#_Toc303847924}[]{#_Toc303848833}[]{#_Toc303849462}[]{#_Toc303850420}[]{#_Toc303858020}[]{#_Toc303847925}[]{#_Toc303848834}[]{#_Toc303849463}[]{#_Toc303850421}[]{#_Toc303858021}[]{#_Toc303847926}[]{#_Toc303848835}[]{#_Toc303849464}[]{#_Toc303850422}[]{#_Toc303858022}[]{#_Toc303847927}[]{#_Toc303848836}[]{#_Toc303849465}[]{#_Toc303850423}[]{#_Toc303858023}[]{#_Toc303847928}[]{#_Toc303848837}[]{#_Toc303849466}[]{#_Toc303850424}[]{#_Toc303858024}[]{#_Toc303847929}[]{#_Toc303848838}[]{#_Toc303849467}[]{#_Toc303850425}[]{#_Toc303858025}[]{#_Toc303847930}[]{#_Toc303848839}[]{#_Toc303849468}[]{#_Toc303850426}[]{#_Toc303858026}[]{#_Toc303847931}[]{#_Toc303848840}[]{#_Toc303849469}[]{#_Toc303850427}[]{#_Toc303858027}[]{#_Toc303847932}[]{#_Toc303848841}[]{#_Toc303849470}[]{#_Toc303850428}[]{#_Toc303858028}

**ACL \-- ACL配置命令 \-- rule (MAC ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 17 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x737287218}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1463256096}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1426190425}[命令用来为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x680010113}[命令用来为二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1654486610}

[**[rule]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ *rule-id* \] { **deny** \| **permit** } \[ **cos** *vlan-pri* \| **counting** \| **dest-mac** *dest-address* *dest-mask* \| { **lsap** *lsap-type* *lsap-type-mask* \| **type** *protocol-type* *protocol-type-mask* } \| **source-mac** *source-address* *source-mask* \| **time-range** *time-range-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_1080950654}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ **counting** \| **time-range** \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_851342928}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1438757250}

[[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1643105108}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1873602021}

[[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1673454087}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1278525123}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_107331010}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654290002}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1473714025}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1293220076}[：指定二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_1207269504}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_876363167}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[cos]{lang="EN-US"}**[ *vlan-pri*]{lang="EN-US"}]{#struct_0_x4306_x6993_2122965446}[：指定]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级。]{style="font-family:宋体"}*[vlan-pri]{lang="EN-US"}*[表示]{style="font-family:宋体"}[802.1p]{lang="EN-US"}[优先级，可输入的形式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x1135097791}[～]{lang="EN-US" style="font-family:宋体"}[7]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[名称：]{lang="EN-US" style="font-family:宋体"}**[best-effort]{lang="EN-US"}**]{#struct_0_x4306_x6993_x952200940}[、]{lang="EN-US" style="font-family:宋体"}**[background]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[spare]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[excellent-effort]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[controlled-load]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[video]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[voice]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[network-management]{lang="EN-US"}**[，依次对应于数字]{lang="EN-US" style="font-family:
宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:
宋体"}[7]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_1556607459}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能。]{style="font-family:宋体"}

[**[dest-mac]{lang="EN-US"}**[ *dest-address* *dest-mask*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654355538}[：指定目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}*[dest-address]{lang="EN-US"}*[表示目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}*[dest-mask]{lang="EN-US"}*[表示目的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的掩码，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsap]{lang="EN-US"}**[ ]{lang="EN-US"}*[lsap-type]{lang="EN-US"}*[ *lsap-type-mask*]{lang="EN-US"}]{#struct_0_x4306_x6993_1435017074}[：指定]{style="font-family:宋体"}[LLC]{lang="EN-US"}[封装中的]{style="font-family:宋体"}[DSAP]{lang="EN-US"}[字段和]{style="font-family:宋体"}[SSAP]{lang="EN-US"}[字段。]{style="font-family:宋体"}*[lsap-type]{lang="EN-US"}*[表示数据帧的封装格式，为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特的十六进制数。]{style="font-family:宋体"}*[lsap-type-mask]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LSAP]{lang="EN-US"}[的类型掩码，为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特的十六进制数，用于指定屏蔽位。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ *protocol-type* *protocol-type-mask*]{lang="EN-US"}]{#struct_0_x4306_x6993_1911797583}[：指定链路层协议类型。]{style="font-family:宋体"}*[protocol-type]{lang="EN-US"}*[表示]{style="font-family:宋体"}[16]{lang="EN-US"}[比特的十六进制数表征的数据帧类型，对应]{style="font-family:宋体"}[Ethernet_II]{lang="EN-US"}[类型和]{style="font-family:宋体"}[Ethernet_SNAP]{lang="EN-US"}[类型帧中的]{style="font-family:宋体"}[type]{lang="EN-US"}[域。]{style="font-family:宋体"}*[protocol-type-mask]{lang="EN-US"}*[表示类型掩码，为]{style="font-family:宋体"}[16]{lang="EN-US"}[比特的十六进制数，用于指定屏蔽位。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[source-mac]{lang="EN-US"}**[ *source-address* *source-mask*]{lang="EN-US"}]{#struct_0_x4306_x6993_1473149271}[：指定源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}*[source-address]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}*[source-mask]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的掩码，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1513954168}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1303762543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1716271703}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1663471819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654158930}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的任意一条已有规则；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，不允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的已有规则，否则将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1747453282}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x597350160}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2068456925}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1234893965}[为二层]{style="font-family:宋体"}[ACL 4000]{lang="EN-US"}[创建规则如下：允许]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文通过，但拒绝]{style="font-family:宋体"}[RARP]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_539938698}

[\[Sysname\] acl mac 4000]{lang="EN-US"}

[\[Sysname-acl-mac-4000\] rule permit type 0806 ffff]{lang="EN-US"}

[\[Sysname-acl-mac-4000\] rule deny type 8035 ffff]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1183723770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1830092163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654224466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_756454312}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_588748689}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#-233529961 .myid}
[]{#_Toc404791900}[]{#struct_0_x4306_x6993_x1785769953}

**ACL \-- ACL配置命令 \-- rule (IPv4 advanced ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 18 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_299845793}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1295859378}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_672162000}[命令用来为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x689236684}[命令用来为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_254029173}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } *protocol* \[ { { **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \* \| **established** } \| **counting** \| **destination** { **object-group** *addr-group-name* \| *dest-address* *dest-wildcard* \| **any** } \| **destination-port** { **object-group** *port-group-name* \| *operator* *port1* \[ *port2* \] } \| { **dscp** *dscp* \| { **precedence** *precedence* \| **tos** *tos* } \* } \| **fragment** \| **icmp-type** { *icmp-type* \[ *icmp-code* \] \| *icmp-message* } \| **logging** \| **source** { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** } \| **source-port** { **object-group** *port-group-name* \| *operator* *port1* \[ *port2* \] } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654027858}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ { { **ack** \| **fin** \| **psh** \| **rst** \| **syn** \| **urg** } \* \| **established** } \| **counting** \| **destination** \| **destination-port** \| { **dscp** \| { **precedence** \| **tos** } \* } \| **fragment** \| **icmp-type** \| **logging** \| **source** \| **source-port** \| **time-range** \| **vpn-instance** \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x544101770}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_85099874}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_54031054}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1619417777}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1773700806}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x82026916}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_786635299}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654093394}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2141608904}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_247585903}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2131816946}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_1659755571}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1905074783}[：表示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[承载的协议类型，可输入的形式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4306_x6993_312125732}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[名称（括号内为对应的数字）：可选取]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x657738109}**[gre]{lang="EN-US"}**[（]{style="font-family:宋体"}[47]{lang="EN-US"}[）、]{style="font-family:宋体"}**[icmp]{lang="EN-US"}**[（]{style="font-family:宋体"}[1]{lang="EN-US"}[）、]{style="font-family:
宋体"}**[igmp]{lang="EN-US"}**[（]{style="font-family:宋体"}[2]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ipinip]{lang="EN-US"}**[（]{style="font-family:宋体"}[4]{lang="EN-US"}[）、]{style="font-family:
宋体"}**[ospf]{lang="EN-US"}**[（]{style="font-family:宋体"}[89]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）或]{style="font-family:
宋体"}**[udp]{lang="EN-US"}**[（]{style="font-family:宋体"}[17]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_x627599485}[之后可配置如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-9]{lang="EN-US"}](?-233529961#_Ref295383134)[所示的规则信息参数。]{style="font-family:
宋体"}

[]{#struct_0_x4306_x6993_x1654552145}[]{#_Ref295383134}[[表1-9 ]{lang="EN-US"}[规则]{style="font-family:黑体"}]{#_Ref259115771}[[信息]{style="font-family:黑体"}]{#_Toc138129449}[参数]{style="font-family:黑体"}

[]{#table_struct_0_x390197314}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_796350567}
:::::

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1090027697}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_595643711}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1704518739}

[**[source]{lang="EN-US"}**[ { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1871525857}

[[源地址信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654617681}

[[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_69073270}[规则的源地址信息]{style="font-family:宋体"}

[*[addr-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_354537702}[：源地址对象组的名称]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1643450681}[：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[source-wildcard]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1643319609}[：源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的通配符掩码（为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示主机地址）]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1037634579}[：任意源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**[ { **object-group** *addr-group-name* \| *dest-address* *dest-wildcard* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_1209980651}

[[目的地址信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654421073}

[[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x2122720597}[规则的目的地址信息]{style="font-family:宋体"}

[*[addr-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_396711077}[：目的地址对象组的名称]{style="font-family:宋体"}

[*[dest-address]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1643450682}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[dest-wildcard]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1643319610}[：目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的通配符掩码（为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示主机地址）]{style="font-family:宋体"}

[**[any]{lang="EN-US"}**]{#struct_0_x4306_x6993_1290881842}[：任意目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1105403122}

[[统计]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654486609}

[[使能规则匹配统计功能，缺省为关闭]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x128968463}

[[本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter]{lang="EN-US"}**]{#struct_0_x4306_x6993_x48716145}[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能]{style="font-family:宋体"}

[**[precedence]{lang="EN-US"}**[ *precedence*]{lang="EN-US"}]{#struct_0_x4306_x6993_981055743}

[[报文优先级]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1080125628}

[[IP]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654290001}[优先级]{style="font-family:宋体"}

[*[precedence]{lang="EN-US"}*]{#struct_0_x4306_x6993_1876998552}[用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[；用文字表示时，分别对应]{style="font-family:宋体"}**[routine]{lang="EN-US"}**[、]{style="font-family:宋体"}**[priority]{lang="EN-US"}**[、]{style="font-family:宋体"}**[immediate]{lang="EN-US"}**[、]{style="font-family:宋体"}**[flash]{lang="EN-US"}**[、]{style="font-family:宋体"}**[flash-override]{lang="EN-US"}**[、]{style="font-family:宋体"}**[critical]{lang="EN-US"}**[、]{style="font-family:宋体"}**[internet]{lang="EN-US"}**[、]{style="font-family:宋体"}**[network]{lang="EN-US"}**

[**[tos]{lang="EN-US"}**[ *tos*]{lang="EN-US"}]{#struct_0_x4306_x6993_x313749747}

[[报文优先级]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1432355577}

[[ToS]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654355537}[优先级]{style="font-family:宋体"}

[*[tos]{lang="EN-US"}*]{#struct_0_x4306_x6993_1838301601}[用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[；用文字表示时，可以选取]{style="font-family:宋体"}**[max-reliability]{lang="EN-US"}**[（]{style="font-family:宋体"}[2]{lang="EN-US"}[）、]{style="font-family:宋体"}**[max-throughput]{lang="EN-US"}**[（]{style="font-family:宋体"}[4]{lang="EN-US"}[）、]{style="font-family:宋体"}**[min-delay]{lang="EN-US"}**[（]{style="font-family:宋体"}[8]{lang="EN-US"}[）、]{style="font-family:宋体"}**[min-monetary-cost]{lang="EN-US"}**[（]{style="font-family:宋体"}[1]{lang="EN-US"}[）、]{style="font-family:宋体"}**[normal]{lang="EN-US"}**[（]{style="font-family:宋体"}[0]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}**[ *dscp*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1502895965}

[[报文优先级]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1335497475}

[[DSCP]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654158929}[优先级]{style="font-family:宋体"}

[*[dscp]{lang="EN-US"}*]{#struct_0_x4306_x6993_174926555}[用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；用文字表示时，可以选取]{style="font-family:宋体"}**[af11]{lang="EN-US"}**[（]{style="font-family:宋体"}[10]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af12]{lang="EN-US"}**[（]{style="font-family:宋体"}[12]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af13]{lang="EN-US"}**[（]{style="font-family:宋体"}[14]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af21]{lang="EN-US"}**[（]{style="font-family:宋体"}[18]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af22]{lang="EN-US"}**[（]{style="font-family:宋体"}[20]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af23]{lang="EN-US"}**[（]{style="font-family:宋体"}[22]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af31]{lang="EN-US"}**[（]{style="font-family:宋体"}[26]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af32]{lang="EN-US"}**[（]{style="font-family:宋体"}[28]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af33]{lang="EN-US"}**[（]{style="font-family:宋体"}[30]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af41]{lang="EN-US"}**[（]{style="font-family:宋体"}[34]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af42]{lang="EN-US"}**[（]{style="font-family:宋体"}[36]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af43]{lang="EN-US"}**[（]{style="font-family:宋体"}[38]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs1]{lang="EN-US"}**[（]{style="font-family:宋体"}[8]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs2]{lang="EN-US"}**[（]{style="font-family:宋体"}[16]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs3]{lang="EN-US"}**[（]{style="font-family:宋体"}[24]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs4]{lang="EN-US"}**[（]{style="font-family:宋体"}[32]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs5]{lang="EN-US"}**[（]{style="font-family:宋体"}[40]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs6]{lang="EN-US"}**[（]{style="font-family:宋体"}[48]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs7]{lang="EN-US"}**[（]{style="font-family:宋体"}[56]{lang="EN-US"}[）、]{style="font-family:宋体"}**[default]{lang="EN-US"}**[（]{style="font-family:宋体"}[0]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ef]{lang="EN-US"}**[（]{style="font-family:宋体"}[46]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[fragment]{lang="EN-US"}**]{#struct_0_x4306_x6993_2016142923}

[[分片信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1199509259}

[[仅对分片报文的非首个分片有效，而对非分片报文和分片报文的首个分片无效]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654224465}

[[若未指定该参数，则表示该规则对所有报文（包括非分片报文和分片报文的每个分片）均有效]{style="font-family:宋体"}]{#struct_0_x4306_x6993_353169785}

[**[logging]{lang="EN-US"}**]{#struct_0_x4306_x6993_x383734002}

[[日志操作]{style="font-family:宋体"}]{#struct_0_x4306_x6993_728110969}

[[对符合条件的报文可记录日志信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_342240665}

[[该功能需要使用该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1654027857}[的模块支持日志记录功能，例如报文过滤]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x947386297}

[[时间段]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1204639060}

[[指定本规则生效的时间段]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1654093393}

[*[time-range-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1393843505}[：时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1105250357}

[[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_x1404883770}[实例]{style="font-family:宋体"}

[[对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_x88468201}[实例中的报文有效]{style="font-family:宋体"}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_1897421813}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}

[[若未指定本参数，表示该规则仅对非]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_x103226483}[报文有效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc138129450}[[当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_x2066425362}[为]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）或]{style="font-family:宋体"}**[udp]{lang="EN-US"}**[（]{style="font-family:宋体"}[17]{lang="EN-US"}[）时，用户还可配置如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-10]{lang="EN-US"}](?-233529961#_Ref259115846)[所示的规则信息参数。]{style="font-family:宋体"}

[]{#struct_0_x4306_x6993_x372708179}[[表1-10 ]{lang="EN-US"}[TCP/UDP]{lang="EN-US"}]{#_Ref259115846}[特有的规则信息参数]{style="font-family:黑体"}

[]{#table_struct_0_x400568738}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88533737}

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1465164385}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_15476241}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x309370453}

[**[source-port]{lang="FR"}**]{#struct_0_x4306_x6993_520810758}[ ]{lang="FR"}[{ **object-group** *port-group-name* \| ]{lang="EN-US"}*[operator]{lang="FR"}*[ *port1* \[ *port2* \] }]{lang="FR"}

[[源端口]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1880780960}

[[定义]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}]{#struct_0_x4306_x6993_x964135145}[报文的源端口信息]{style="font-family:宋体"}

[*[port-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88337129}[：端口对象组的名称]{style="font-family:宋体"}

[*[operator]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1643581755}[为操作符，取值可以为]{style="font-family:宋体"}**[lt]{lang="EN-US"}**[（小于）、]{style="font-family:宋体"}**[gt]{lang="EN-US"}**[（大于）、]{style="font-family:宋体"}**[eq]{lang="EN-US"}**[（等于）、]{style="font-family:宋体"}**[neq]{lang="EN-US"}**[（不等于）或者]{style="font-family:宋体"}**[range]{lang="EN-US"}**[（在范围内，包括边界值）。只有操作符]{style="font-family:宋体"}**[range]{lang="EN-US"}**[需要两个端口号做操作数，其它的只需要一个端口号做操作数]{style="font-family:宋体"}

[*[port1]{lang="EN-US"}*]{#struct_0_x4306_x6993_1599912237}[、]{style="font-family:宋体"}*[port2]{lang="EN-US"}*[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[的端口号，用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[；用文字表示时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号可以选取]{style="font-family:宋体"}**[chargen]{lang="EN-US"}**[（]{style="font-family:宋体"}[19]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[（]{style="font-family:宋体"}[179]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cmd]{lang="EN-US"}**[（]{style="font-family:宋体"}[514]{lang="EN-US"}[）、]{style="font-family:宋体"}**[daytime]{lang="EN-US"}**[（]{style="font-family:宋体"}[13]{lang="EN-US"}[）、]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[（]{style="font-family:宋体"}[9]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dns]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[domain]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[echo]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）、]{style="font-family:宋体"}**[exec]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[512]{lang="EN-US"}[）、]{style="font-family:宋体"}**[finger]{lang="EN-US"}**[（]{style="font-family:宋体"}[79]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ftp]{lang="EN-US"}**[（]{style="font-family:宋体"}[21]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ftp-data]{lang="EN-US"}**[（]{style="font-family:宋体"}[20]{lang="EN-US"}[）、]{style="font-family:宋体"}**[gopher]{lang="EN-US"}**[（]{style="font-family:宋体"}[70]{lang="EN-US"}[）、]{style="font-family:宋体"}**[hostname]{lang="EN-US"}**[（]{style="font-family:宋体"}[101]{lang="EN-US"}[）、]{style="font-family:宋体"}**[irc]{lang="EN-US"}**[（]{style="font-family:宋体"}[194]{lang="EN-US"}[）、]{style="font-family:宋体"}**[klogin]{lang="EN-US"}**[（]{style="font-family:宋体"}[543]{lang="EN-US"}[）、]{style="font-family:宋体"}**[kshell]{lang="EN-US"}**[（]{style="font-family:宋体"}[544]{lang="EN-US"}[）、]{style="font-family:宋体"}**[login]{lang="EN-US"}**[（]{style="font-family:宋体"}[513]{lang="EN-US"}[）、]{style="font-family:宋体"}**[lpd]{lang="EN-US"}**[（]{style="font-family:宋体"}[515]{lang="EN-US"}[）、]{style="font-family:宋体"}**[nntp]{lang="EN-US"}**[（]{style="font-family:宋体"}[119]{lang="EN-US"}[）、]{style="font-family:宋体"}**[pop2]{lang="EN-US"}**[（]{style="font-family:宋体"}[109]{lang="EN-US"}[）、]{style="font-family:宋体"}**[pop3]{lang="EN-US"}**[（]{style="font-family:宋体"}[110]{lang="EN-US"}[）、]{style="font-family:宋体"}**[smtp]{lang="EN-US"}**[（]{style="font-family:宋体"}[25]{lang="EN-US"}[）、]{style="font-family:宋体"}**[sunrpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[111]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tacacs]{lang="EN-US"}**[（]{style="font-family:宋体"}[49]{lang="EN-US"}[）、]{style="font-family:宋体"}**[talk]{lang="EN-US"}**[（]{style="font-family:宋体"}[517]{lang="EN-US"}[）、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[（]{style="font-family:宋体"}[23]{lang="EN-US"}[）、]{style="font-family:宋体"}**[time]{lang="EN-US"}**[（]{style="font-family:宋体"}[37]{lang="EN-US"}[）、]{style="font-family:宋体"}**[uucp]{lang="EN-US"}**[（]{style="font-family:宋体"}[540]{lang="EN-US"}[）、]{style="font-family:宋体"}**[whois]{lang="EN-US"}**[（]{style="font-family:宋体"}[43]{lang="EN-US"}[）、]{style="font-family:宋体"}**[www]{lang="EN-US"}**[（]{style="font-family:宋体"}[80]{lang="EN-US"}[）；]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号可以选取]{style="font-family:宋体"}**[biff]{lang="EN-US"}**[（]{style="font-family:宋体"}[512]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bootpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[68]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bootps]{lang="EN-US"}**[（]{style="font-family:宋体"}[67]{lang="EN-US"}[）、]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[（]{style="font-family:宋体"}[9]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dns]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dnsix]{lang="EN-US"}**[（]{style="font-family:宋体"}[90]{lang="EN-US"}[）、]{style="font-family:宋体"}**[echo]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）、]{style="font-family:宋体"}**[mobilip-ag]{lang="EN-US"}**[（]{style="font-family:宋体"}[434]{lang="EN-US"}[）、]{style="font-family:宋体"}**[mobilip-mn]{lang="EN-US"}**[（]{style="font-family:宋体"}[435]{lang="EN-US"}[）、]{style="font-family:宋体"}**[nameserver]{lang="EN-US"}**[（]{style="font-family:宋体"}[42]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-dgm]{lang="EN-US"}**[（]{style="font-family:宋体"}[138]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-ns]{lang="EN-US"}**[（]{style="font-family:宋体"}[137]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-ssn]{lang="EN-US"}**[（]{style="font-family:宋体"}[139]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ntp]{lang="EN-US"}**[（]{style="font-family:宋体"}[123]{lang="EN-US"}[）、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[（]{style="font-family:宋体"}[520]{lang="EN-US"}[）、]{style="font-family:宋体"}**[snmp]{lang="EN-US"}**[（]{style="font-family:宋体"}[161]{lang="EN-US"}[）、]{style="font-family:宋体"}**[snmptrap]{lang="EN-US"}**[（]{style="font-family:宋体"}[162]{lang="EN-US"}[）、]{style="font-family:宋体"}**[sunrpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[111]{lang="EN-US"}[）、]{style="font-family:宋体"}**[syslog]{lang="EN-US"}**[（]{style="font-family:宋体"}[514]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tacacs-ds]{lang="EN-US"}**[（]{style="font-family:宋体"}[65]{lang="EN-US"}[）、]{style="font-family:宋体"}**[talk]{lang="EN-US"}**[（]{style="font-family:宋体"}[517]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tftp]{lang="EN-US"}**[（]{style="font-family:宋体"}[69]{lang="EN-US"}[）、]{style="font-family:宋体"}**[time]{lang="EN-US"}**[（]{style="font-family:宋体"}[37]{lang="EN-US"}[）、]{style="font-family:宋体"}**[who]{lang="EN-US"}**[（]{style="font-family:宋体"}[513]{lang="EN-US"}[）、]{style="font-family:宋体"}**[xdmcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[177]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[destination-port]{lang="FR"}**]{#struct_0_x4306_x6993_x79073712}[ ]{lang="FR"}[{ **object-group** *port-group-name* \| ]{lang="EN-US"}*[operator]{lang="FR"}*[ *port1* \[ *port2* \] }]{lang="FR"}

[[目的端口]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x857302304}

[[定义]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}]{#struct_0_x4306_x6993_x1606874894}[报文的目的端口信息]{style="font-family:宋体"}

[[{ **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88402665}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_288763191}[报文标识]{style="font-family:宋体"}

[[定义对携带不同标志位（包括]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x4306_x6993_1717166031}[、]{style="font-family:宋体"}[FIN]{lang="EN-US"}[、]{style="font-family:宋体"}[PSH]{lang="EN-US"}[、]{style="font-family:宋体"}[RST]{lang="EN-US"}[、]{style="font-family:宋体"}[SYN]{lang="EN-US"}[和]{style="font-family:宋体"}[URG]{lang="EN-US"}[六种）的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的处理规则]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_x1443500484}[协议特有的参数。表示匹配携带不同标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，各]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值可为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不携带此标志位，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示携带此标志位）]{style="font-family:宋体"}

[[对于一条]{style="font-family:宋体"}]{#struct_0_x4306_x6993_970165774}[规则中各标志位的配置组合，不同产品的处理方式（"与"或"或"）不同，请以设备的实际情况为准。譬如：当配置为]{style="font-family:宋体"}**[ack]{lang="EN-US"}**[ 0 **psh** 1]{lang="EN-US"}[时，有些产品将匹配不携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[标志位且携带]{style="font-family:宋体"}[PSH]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，而有些产品则匹配不携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[或携带]{style="font-family:宋体"}[PSH]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[**[established]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88206057}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_41174019}[连接建立标识]{style="font-family:宋体"}

[[定义对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_x1601142738}[连接报文的处理规则]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_1074218305}[协议特有的参数。对于路由器，表示匹配携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[或]{style="font-family:宋体"}[RST]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接报文；对于交换机，请以各产品实际情况为准]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc138129451}[[当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_2044956785}[为]{style="font-family:宋体"}**[icmp]{lang="EN-US"}**[（]{style="font-family:宋体"}[1]{lang="EN-US"}[）时，用户还可配置如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:
宋体"}1-11]{lang="EN-US"}](?-233529961#_Ref295383166)[所示的规则信息参数。]{style="font-family:
宋体"}

[]{#struct_0_x4306_x6993_x1352304030}[]{#_Ref295383166}[[表1-11 ]{lang="EN-US"}[ICMP]{lang="EN-US"}]{#_Ref259115911}[特有的规则信息]{style="font-family:黑体"}[参数]{style="font-family:黑体"}

[]{#table_struct_0_x399846498}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88271593}

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_51153943}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2037958483}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1644604449}

[**[icmp-type]{lang="EN-US"}**[ { *icmp-type* *icmp-code* \| *icmp-message* }]{lang="EN-US"}]{#struct_0_x4306_x6993_1731752227}

[[ICMP]{lang="EN-US"}]{#struct_0_x4306_x6993_x2140996115}[报文的消息类型和消息码信息]{style="font-family:宋体"}

[[指定本规则中]{style="font-family:宋体"}[ICMP]{lang="EN-US"}]{#struct_0_x4306_x6993_1075887583}[报文的消息类型和消息码信息]{style="font-family:宋体"}

[*[icmp-type]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88074985}[：]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[消息类型，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[*[icmp-code]{lang="EN-US"}*]{#struct_0_x4306_x6993_x952953651}[：]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[消息码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[*[icmp-message]{lang="FR"}*]{#struct_0_x4306_x6993_763663642}[：]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[消息名称。可以输入的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[消息名称，及其与消息类型和消息码的对应关系如]{style="font-family:宋体"}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-12]{lang="EN-US"}](?-233529961#_Ref144979012)[所示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x4306_x6993_456528186}[[表1-12 ]{lang="EN-US"}[ICMP]{lang="EN-US"}]{#_Ref144979012}[消息名称与消息类型和消息码的对应关系]{style="font-family:黑体"}

[]{#table_struct_0_x373264834}[[ICMP]{lang="EN-US"}]{#struct_0_x4306_x6993_610972575}[消息名称]{style="font-family:黑体"}

[[ICMP]{lang="EN-US"}]{#struct_0_x4306_x6993_x530101152}[消息类型]{style="font-family:黑体"}

[[ICMP]{lang="EN-US"}]{#struct_0_x4306_x6993_x409440913}[消息码]{style="font-family:黑体"}

[[echo]{lang="EN-US"}]{#struct_0_x4306_x6993_x88140521}

[[8]{lang="EN-US"}]{#struct_0_x4306_x6993_138251248}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x8745567}

[[echo-reply]{lang="EN-US"}]{#struct_0_x4306_x6993_1974067045}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1488288786}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x358821164}

[[fragmentneed-DFset]{lang="EN-US"}]{#struct_0_x4306_x6993_x87943913}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_1464592653}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_383663196}

[[host-redirect]{lang="EN-US"}]{#struct_0_x4306_x6993_x143615930}

[[5]{lang="EN-US"}]{#struct_0_x4306_x6993_555791292}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x691459631}

[[host-tos-redirect]{lang="EN-US"}]{#struct_0_x4306_x6993_x88009449}

[[5]{lang="EN-US"}]{#struct_0_x4306_x6993_x207219095}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_x312407510}

[[host-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_681658167}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_495874617}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x88468200}

[[information-reply]{lang="EN-US"}]{#struct_0_x4306_x6993_1897421814}

[[16]{lang="EN-US"}]{#struct_0_x4306_x6993_x103029875}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1856440814}

[[information-request]{lang="EN-US"}]{#struct_0_x4306_x6993_x43506548}

[[15]{lang="EN-US"}]{#struct_0_x4306_x6993_x88533736}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1465164384}

[[net-redirect]{lang="EN-US"}]{#struct_0_x4306_x6993_15541777}

[[5]{lang="EN-US"}]{#struct_0_x4306_x6993_1110959384}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x88337128}

[[net-tos-redirect]{lang="EN-US"}]{#struct_0_x4306_x6993_1599912236}

[[5]{lang="EN-US"}]{#struct_0_x4306_x6993_x79008176}

[[2]{lang="EN-US"}]{#struct_0_x4306_x6993_1151643811}

[[net-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_x366557443}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_x88402664}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_288763192}

[[parameter-problem]{lang="EN-US"}]{#struct_0_x4306_x6993_1717166028}

[[12]{lang="EN-US"}]{#struct_0_x4306_x6993_x1444090307}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x88206056}

[[port-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_41174020}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_774245267}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_1255555120}

[[protocol-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_x88271592}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_51153942}

[[2]{lang="EN-US"}]{#struct_0_x4306_x6993_81643347}

[[reassembly-timeout]{lang="EN-US"}]{#struct_0_x4306_x6993_x88074984}

[[11]{lang="EN-US"}]{#struct_0_x4306_x6993_x952953652}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_763860250}

[[source-quench]{lang="EN-US"}]{#struct_0_x4306_x6993_x111942748}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_x88140520}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_138251249}

[[source-route-failed]{lang="EN-US"}]{#struct_0_x4306_x6993_x8745566}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_x87943912}

[[5]{lang="EN-US"}]{#struct_0_x4306_x6993_1464592654}

[[timestamp-reply]{lang="EN-US"}]{#struct_0_x4306_x6993_383728732}

[[14]{lang="EN-US"}]{#struct_0_x4306_x6993_x88009448}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x207219094}

[[timestamp-request]{lang="EN-US"}]{#struct_0_x4306_x6993_x312473046}

[[13]{lang="EN-US"}]{#struct_0_x4306_x6993_x88468203}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1897421811}

[[ttl-exceeded]{lang="EN-US"}]{#struct_0_x4306_x6993_x103357555}

[[11]{lang="EN-US"}]{#struct_0_x4306_x6993_x88533739}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1465164387}

[ ]{lang="EN-US"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_15607313}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1419593559}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1358213383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1644040508}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x699152518}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的任意一条已有规则；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，不允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的已有规则，否则将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_809909354}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1515121559}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88337131}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x738739931}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[创建规则如下：允许]{style="font-family:宋体"}[129.9.0.0/16]{lang="EN-US"}[网段内的主机与]{style="font-family:宋体"}[202.38.160.0/24]{lang="EN-US"}[网段内主机的]{style="font-family:宋体"}[WWW]{lang="EN-US"}[端口（端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[）建立连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x1570762001}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl]{lang="FR"}[-ipv4]{lang="EN-US"}[-adv-3000\] rule permit tcp source 129.9.0.0 0.0.255.255 destination 202.38.160.0 0.0.0.255 destination-port eq 80]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_193434580}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3001]{lang="EN-US"}[创建规则如下：允许]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文通过，但拒绝发往]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[网段的]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x996946377}

[\[Sysname\] acl advanced 3001]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3001\] rule deny icmp destination 192.168.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3001\] rule permit ip]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x311291973}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3002]{lang="EN-US"}[创建规则如下：在出、入双方向上都允许建立]{style="font-family:宋体"}[FTP]{lang="EN-US"}[连接并传输]{style="font-family:宋体"}[FTP]{lang="EN-US"}[数据。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x88402667}

[\[Sysname\] acl advanced 3002]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule permit tcp source-port eq ftp]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule permit tcp source-port eq ftp-data]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule permit tcp destination-port eq ftp]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule permit tcp destination-port eq ftp-data]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_288763193}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3003]{lang="EN-US"}[创建规则如下：在出、入双方向上都允许]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文和]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1717166029}

[\[Sysname\] acl advanced 3003]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3003\] rule permit udp source-port eq snmp]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3003\] rule permit udp source-port eq snmptrap]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3003\] rule permit udp destination-port eq snmp]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3003\] rule permit udp destination-port eq snmptrap]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1444024771}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x27904141}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1551135489}[ **logging** **interval**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1781065920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88206059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_41174013}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}

::::: {#463580177 .myid}
[]{#_Toc404791901}[]{#struct_0_x4306_x6993_782139438}

**ACL \-- ACL配置命令 \-- rule (IPv4 basic ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 19 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_487344021}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_1070932105}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x888005354}[命令用来为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1968207096}[命令用来为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1412357971}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } \[ **counting** \| **fragment** \| **logging** \| **source** { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88271595}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ **counting** \| **fragment** \| **logging** \| **source** \| **time-range** \| **vpn-instance** \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_51153937}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_880318230}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_1433424988}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x659930573}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1149766934}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1958316542}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x31299186}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_687890017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88074987}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_x952953649}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_763139353}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_439250895}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_x617046280}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能。]{style="font-family:宋体"}

[**[fragment]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1588217114}[：表示仅对非首片分片报文有效，而对非分片报文和首片分片报文无效。若未指定本参数，表示该规则对非分片报文和分片报文均有效。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1055738290}[：表示对符合条件的报文可记录日志信息。该功能需要使用该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的模块支持日志记录功能，例如报文过滤。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ { **object-group** *addr-group-name* \| *source-address* *source-wildcard* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_x1594084910}[：指定规则的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[addr-group-name]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称，]{style="font-family:宋体"}*[source-address]{lang="EN-US"}*[表示报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[source-wildcard]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的通配符掩码（为]{style="font-family:宋体"}[0]{lang="EN-US"}[表示主机地址），]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1032306329}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88140523}[：表示对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中的报文有效。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对非]{style="font-family:宋体"}[VPN]{lang="EN-US"}[报文有效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_138251250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1965060711}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1398055504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1643974973}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1239922302}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的任意一条已有规则；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，不允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的已有规则，否则将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1729559850}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_1026247850}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x4306_x6993_3653514}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x87943915}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[创建规则如下：仅允许来自]{style="font-family:宋体"}[10.0.0.0/8]{lang="EN-US"}[、]{style="font-family:宋体"}[172.17.0.0/16]{lang="EN-US"}[和]{style="font-family:宋体"}[192.168.1.0/24]{lang="EN-US"}[网段的报文通过，而拒绝来自所有其它网段的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1464592655}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 10.0.0.0 0.255.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 172.17.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule permit source 192.168.1.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source any]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_383794268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1725696848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1788193026}[ **logging** **interval**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_1932762103}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_231996912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2118703210}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#872051014 .myid}
[]{#_Toc404791902}[]{#struct_0_x4306_x6993_x88009451}[]{#_Toc291080260}

**ACL \-- ACL配置命令 \-- rule (IPv6 advanced ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 20 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_2131433073}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x517898824}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x580618246}[命令用来为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_768450647}[命令用来为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x254523753}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } *protocol* \[ { { **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \* \| **established** } \| **counting** \| **destination** { **object-group** *addr-group-name* \|*dest-address* *dest-prefix* \| *dest-address/dest-prefix* \| **any** } \| **destination-port** { **object-group** *port-group-name* \| *operator* *port1* \[ *port2* \] } \| **dscp** *dscp* \| **flow-label** *flow-label-value* \| **fragment** \| **icmp6-type** { *icmp6-type* *icmp6-code* \| *icmp6-message* } \| **logging** \| **routing** \[ **type** *routing-type* \] \| **hop-by-hop** \[ **type** *hop-type* \] \| **source** { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address/source-prefix* \| **any** } \| **source-port** { **object-group** *port-group-name* \| *operator* *port1* \[ *port2* \] } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88468202}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ { { **ack** \| **fin** \| **psh** \| **rst** \| **syn** \| **urg** } \* \| **established** } \| **counting** \| **destination** \| **destination-port** \| **dscp** \| **flow-label** \| **fragment** \| **icmp6-type** \| **logging** \| **routing** \| **hop-by-hop** \| **source** \| **source-port** \| **time-range** \| **vpn-instance** \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_1897421812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x103160947}

[[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_719646939}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x760273721}

[[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x1259372944}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88533738}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1465164386}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_15672849}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1293227645}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1252405874}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_x162860122}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_1000022474}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_1817983673}[：表示]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[承载的协议类型，可输入的形式如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[数字：取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x88337130}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[名称（括号内为对应的数字）：可选取]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x738739932}**[gre]{lang="EN-US"}**[（]{style="font-family:宋体"}[47]{lang="EN-US"}[）、]{style="font-family:宋体"}**[icmpv6]{lang="EN-US"}**[（]{style="font-family:宋体"}[58]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ipv6-ah]{lang="EN-US"}**[（]{style="font-family:宋体"}[51]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ipv6-esp]{lang="EN-US"}**[（]{style="font-family:宋体"}[50]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[（]{style="font-family:宋体"}[89]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）或]{style="font-family:
宋体"}**[udp]{lang="EN-US"}**[（]{style="font-family:宋体"}[17]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1570565393}[之后可配置如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-13]{lang="EN-US"}](?872051014#_Ref259116285)[所示的规则信息参数。]{style="font-family:宋体"}

[]{#struct_0_x4306_x6993_1754037515}[]{#_Ref259116285}[[表1-13 ]{lang="EN-US"}[规则信息]{style="font-family:黑体"}]{#_Toc138129456}[参数]{style="font-family:黑体"}

[]{#table_struct_0_x379992802}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1261958356}
:::::

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1220193746}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x201354858}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88402666}

[**[source]{lang="EN-US"}**[ { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address/source-prefix* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_288763194}

[[源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_1717166034}[地址]{style="font-family:宋体"}

[[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1443828164}[规则的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[*[addr-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_1964693821}[：源地址对象组的名称]{style="font-family:宋体"}

[*[source-address]{lang="EN-US"}*]{#struct_0_x4306_x6993_x77891028}[：源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[source-prefix]{lang="EN-US"}*]{#struct_0_x4306_x6993_1810411865}[：源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}

[**[any]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88206058}[：任意源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**[ { **object-group** addr-group-name \| *dest-address* *dest-prefix* \| *dest-address/dest-prefix* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_41174014}

[[目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x1556512722}[地址]{style="font-family:宋体"}

[[指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1177981177}[规则的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息]{style="font-family:宋体"}

[*[addr-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_330771336}[：目的地址对象组的名称]{style="font-family:宋体"}

[*[dest-address]{lang="EN-US"}*]{#struct_0_x4306_x6993_x77563349}[：目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[dest]{lang="EN-US"}*[-*prefix*]{lang="EN-US"}]{#struct_0_x4306_x6993_x470833422}[：目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}

[**[any]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88271594}[：任意目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_51153936}

[[统计]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1075996906}

[[使能规则匹配统计功能，缺省为关闭]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2061420041}

[[本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x612808757}[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能]{style="font-family:宋体"}

[**[dscp]{lang="EN-US"}**[ *dscp*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88074986}

[[报文优先级]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x952953650}

[[DSCP]{lang="EN-US"}]{#struct_0_x4306_x6993_763729178}[优先级]{style="font-family:宋体"}

[*[dscp]{lang="EN-US"}*]{#struct_0_x4306_x6993_x302545217}[：用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；用名称表示时，可选取]{style="font-family:宋体"}**[af11]{lang="EN-US"}**[（]{style="font-family:宋体"}[10]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af12]{lang="EN-US"}**[（]{style="font-family:宋体"}[12]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af13]{lang="EN-US"}**[（]{style="font-family:宋体"}[14]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af21]{lang="EN-US"}**[（]{style="font-family:宋体"}[18]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af22]{lang="EN-US"}**[（]{style="font-family:宋体"}[20]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af23]{lang="EN-US"}**[（]{style="font-family:宋体"}[22]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af31]{lang="EN-US"}**[（]{style="font-family:宋体"}[26]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af32]{lang="EN-US"}**[（]{style="font-family:宋体"}[28]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af33]{lang="EN-US"}**[（]{style="font-family:宋体"}[30]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af41]{lang="EN-US"}**[（]{style="font-family:宋体"}[34]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af42]{lang="EN-US"}**[（]{style="font-family:宋体"}[36]{lang="EN-US"}[）、]{style="font-family:宋体"}**[af43]{lang="EN-US"}**[（]{style="font-family:宋体"}[38]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs1]{lang="EN-US"}**[（]{style="font-family:宋体"}[8]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs2]{lang="EN-US"}**[（]{style="font-family:宋体"}[16]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs3]{lang="EN-US"}**[（]{style="font-family:宋体"}[24]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs4]{lang="EN-US"}**[（]{style="font-family:宋体"}[32]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs5]{lang="EN-US"}**[（]{style="font-family:宋体"}[40]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs6]{lang="EN-US"}**[（]{style="font-family:宋体"}[48]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cs7]{lang="EN-US"}**[（]{style="font-family:宋体"}[56]{lang="EN-US"}[）、]{style="font-family:宋体"}**[default]{lang="EN-US"}**[（]{style="font-family:宋体"}[0]{lang="EN-US"}[）或]{style="font-family:宋体"}**[ef]{lang="EN-US"}**[（]{style="font-family:宋体"}[46]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[flow-label]{lang="EN-US"}**[ *flow-label-value*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88140522}

[[流标签字段]{style="font-family:宋体"}]{#struct_0_x4306_x6993_138251251}

[[指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x1965060710}[基本报文头中流标签字段的值]{style="font-family:宋体"}

[*[flow-label-value]{lang="EN-US"}*]{#struct_0_x4306_x6993_x168028437}[：流标签字段的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}

[**[fragment]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1317438583}

[[报文分片]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x87943914}

[[仅对分片报文的非首个分片有效，而对非分片报文和分片报文的首个分片无效]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1464592656}

[[若未指定本参数，表示该规则对所有报文（包括非分片报文和分片报文的每个分片）均有效]{style="font-family:宋体"}]{#struct_0_x4306_x6993_383859804}

[**[logging]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88009450}

[[日志操作]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2131433074}

[[对符合条件的报文可记录日志信息]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x517440072}

[[该功能需要使用该]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_1859113635}[的模块支持日志记录功能，例如报文过滤]{style="font-family:宋体"}

[**[routing]{lang="EN-US"}**[ \[ **type** *routing-type* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x88468205}

[[路由头]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1897421817}

[[指定路由头的类型]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x102964339}

[*[routing-type]{lang="EN-US"}*]{#struct_0_x4306_x6993_259376178}[：路由头类型的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[[若指定了]{style="font-family:宋体"}**[type]{lang="EN-US"}**[ *routing-type*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88533741}[参数，表示仅对指定类型的路由头有效；否则，表示对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[所有类型的路由头都有效]{style="font-family:宋体"}

[**[hop-by-hop]{lang="EN-US"}**[ \[ **type** *hop-type* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x108813733}

[[逐跳头]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x88337133}

[[指定逐跳头的类型]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x738739929}

[*[hop-type]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88402669}[：逐跳头类型的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[[若指定了]{style="font-family:宋体"}**[type]{lang="EN-US"}**[ *hop-type*]{lang="EN-US"}]{#struct_0_x4306_x6993_288763187}[参数，表示仅对指定类型的逐跳头有效；否则，表示对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[所有类型的逐跳头都有效]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88206061}

[[时间段]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1915141115}

[[指定本规则生效的时间段]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1364654411}

[*[time-range-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88271597}[：时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_51153939}

[[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_x1796040938}[实例]{style="font-family:宋体"}

[[对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_690705021}[实例中的报文有效]{style="font-family:宋体"}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88074989}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}

[[若未指定本参数，表示该规则仅对非]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x4306_x6993_x952953639}[报文有效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_763139356}[为]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[6]{lang="EN-US"}[）或]{style="font-family:
宋体"}**[udp]{lang="EN-US"}**[（]{style="font-family:宋体"}[17]{lang="EN-US"}[）时，用户还可配置如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-14]{lang="EN-US"}](?872051014#_Ref259116335)[所示的规则信息参数。]{style="font-family:宋体"}

[]{#struct_0_x4306_x6993_439250900}[]{#_Ref259116335}[[表1-14 ]{lang="EN-US"}[TCP/UDP]{lang="EN-US"}]{#_Toc138129457}[特有的规则信息]{style="font-family:黑体"}[参数]{style="font-family:黑体"}

[]{#table_struct_0_x360098178}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_139733594}

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88140525}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_138251252}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1965060713}

[**[source-port]{lang="FR"}**]{#struct_0_x4306_x6993_x1734112378}[ ]{lang="FR"}[{ **object-group** *port-group-name* \| ]{lang="EN-US"}*[operator]{lang="FR"}*[ *port1* \[ *port2* \] }]{lang="FR"}

[[源端口]{style="font-family:宋体"}]{#struct_0_x4306_x6993_765480254}

[[定义]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}]{#struct_0_x4306_x6993_x2056379552}[报文的源端口信息]{style="font-family:宋体"}

[*[port-group-name]{lang="EN-US"}*]{#struct_0_x4306_x6993_x87943917}[：端口对象组的名称]{style="font-family:宋体"}

[*[operator]{lang="EN-US"}*]{#struct_0_x4306_x6993_x77628887}[：操作符，取值可以为]{style="font-family:宋体"}**[lt]{lang="EN-US"}**[（小于）、]{style="font-family:宋体"}**[gt]{lang="EN-US"}**[（大于）、]{style="font-family:宋体"}**[eq]{lang="EN-US"}**[（等于）、]{style="font-family:宋体"}**[neq]{lang="EN-US"}**[（不等于）或者]{style="font-family:宋体"}**[range]{lang="EN-US"}**[（在范围内，包括边界值）。只有]{style="font-family:宋体"}**[range]{lang="EN-US"}**[操作符需要两个端口号做操作数，其它操作符只需要一个端口号做操作数]{style="font-family:宋体"}

[*[port1]{lang="EN-US"}*[/*port2*]{lang="EN-US"}]{#struct_0_x4306_x6993_1464592657}[：]{style="font-family:宋体"}[TCP]{lang="EN-US"}[或]{style="font-family:宋体"}[UDP]{lang="EN-US"}[的端口号，用数字表示时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[；用名称表示时，]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号可选取]{style="font-family:宋体"}**[chargen]{lang="EN-US"}**[（]{style="font-family:宋体"}[19]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[（]{style="font-family:宋体"}[179]{lang="EN-US"}[）、]{style="font-family:宋体"}**[cmd]{lang="EN-US"}**[（]{style="font-family:宋体"}[514]{lang="EN-US"}[）、]{style="font-family:宋体"}**[daytime]{lang="EN-US"}**[（]{style="font-family:宋体"}[13]{lang="EN-US"}[）、]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[（]{style="font-family:宋体"}[9]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dns]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[domain]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[echo]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）、]{style="font-family:宋体"}**[exec]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[512]{lang="EN-US"}[）、]{style="font-family:宋体"}**[finger]{lang="EN-US"}**[（]{style="font-family:宋体"}[79]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ftp]{lang="EN-US"}**[（]{style="font-family:宋体"}[21]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ftp-data]{lang="EN-US"}**[（]{style="font-family:宋体"}[20]{lang="EN-US"}[）、]{style="font-family:宋体"}**[gopher]{lang="EN-US"}**[（]{style="font-family:宋体"}[70]{lang="EN-US"}[）、]{style="font-family:宋体"}**[hostname]{lang="EN-US"}**[（]{style="font-family:宋体"}[101]{lang="EN-US"}[）、]{style="font-family:宋体"}**[irc]{lang="EN-US"}**[（]{style="font-family:宋体"}[194]{lang="EN-US"}[）、]{style="font-family:宋体"}**[klogin]{lang="EN-US"}**[（]{style="font-family:宋体"}[543]{lang="EN-US"}[）、]{style="font-family:宋体"}**[kshell]{lang="EN-US"}**[（]{style="font-family:宋体"}[544]{lang="EN-US"}[）、]{style="font-family:宋体"}**[login]{lang="EN-US"}**[（]{style="font-family:宋体"}[513]{lang="EN-US"}[）、]{style="font-family:宋体"}**[lpd]{lang="EN-US"}**[（]{style="font-family:宋体"}[515]{lang="EN-US"}[）、]{style="font-family:宋体"}**[nntp]{lang="EN-US"}**[（]{style="font-family:宋体"}[119]{lang="EN-US"}[）、]{style="font-family:宋体"}**[pop2]{lang="EN-US"}**[（]{style="font-family:宋体"}[109]{lang="EN-US"}[）、]{style="font-family:宋体"}**[pop3]{lang="EN-US"}**[（]{style="font-family:宋体"}[110]{lang="EN-US"}[）、]{style="font-family:宋体"}**[smtp]{lang="EN-US"}**[（]{style="font-family:宋体"}[25]{lang="EN-US"}[）、]{style="font-family:宋体"}**[sunrpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[111]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tacacs]{lang="EN-US"}**[（]{style="font-family:宋体"}[49]{lang="EN-US"}[）、]{style="font-family:宋体"}**[talk]{lang="EN-US"}**[（]{style="font-family:宋体"}[517]{lang="EN-US"}[）、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[（]{style="font-family:宋体"}[23]{lang="EN-US"}[）、]{style="font-family:宋体"}**[time]{lang="EN-US"}**[（]{style="font-family:宋体"}[37]{lang="EN-US"}[）、]{style="font-family:宋体"}**[uucp]{lang="EN-US"}**[（]{style="font-family:宋体"}[540]{lang="EN-US"}[）、]{style="font-family:宋体"}**[whois]{lang="EN-US"}**[（]{style="font-family:宋体"}[43]{lang="EN-US"}[）或]{style="font-family:宋体"}**[www]{lang="EN-US"}**[（]{style="font-family:宋体"}[80]{lang="EN-US"}[）；]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号可选取]{style="font-family:宋体"}**[biff]{lang="EN-US"}**[（]{style="font-family:宋体"}[512]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bootpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[68]{lang="EN-US"}[）、]{style="font-family:宋体"}**[bootps]{lang="EN-US"}**[（]{style="font-family:宋体"}[67]{lang="EN-US"}[）、]{style="font-family:宋体"}**[discard]{lang="EN-US"}**[（]{style="font-family:宋体"}[9]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dns]{lang="EN-US"}**[（]{style="font-family:宋体"}[53]{lang="EN-US"}[）、]{style="font-family:宋体"}**[dnsix]{lang="EN-US"}**[（]{style="font-family:宋体"}[90]{lang="EN-US"}[）、]{style="font-family:宋体"}**[echo]{lang="EN-US"}**[ ]{lang="EN-US"}[（]{style="font-family:宋体"}[7]{lang="EN-US"}[）、]{style="font-family:宋体"}**[mobilip-ag]{lang="EN-US"}**[（]{style="font-family:宋体"}[434]{lang="EN-US"}[）、]{style="font-family:宋体"}**[mobilip-mn]{lang="EN-US"}**[（]{style="font-family:宋体"}[435]{lang="EN-US"}[）、]{style="font-family:宋体"}**[nameserver]{lang="EN-US"}**[（]{style="font-family:宋体"}[42]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-dgm]{lang="EN-US"}**[（]{style="font-family:宋体"}[138]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-ns]{lang="EN-US"}**[（]{style="font-family:宋体"}[137]{lang="EN-US"}[）、]{style="font-family:宋体"}**[netbios-ssn]{lang="EN-US"}**[（]{style="font-family:宋体"}[139]{lang="EN-US"}[）、]{style="font-family:宋体"}**[ntp]{lang="EN-US"}**[（]{style="font-family:宋体"}[123]{lang="EN-US"}[）、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[（]{style="font-family:宋体"}[520]{lang="EN-US"}[）、]{style="font-family:宋体"}**[snmp]{lang="EN-US"}**[（]{style="font-family:宋体"}[161]{lang="EN-US"}[）、]{style="font-family:宋体"}**[snmptrap]{lang="EN-US"}**[（]{style="font-family:宋体"}[162]{lang="EN-US"}[）、]{style="font-family:宋体"}**[sunrpc]{lang="EN-US"}**[（]{style="font-family:宋体"}[111]{lang="EN-US"}[）、]{style="font-family:宋体"}**[syslog]{lang="EN-US"}**[（]{style="font-family:宋体"}[514]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tacacs-ds]{lang="EN-US"}**[（]{style="font-family:宋体"}[65]{lang="EN-US"}[）、]{style="font-family:宋体"}**[talk]{lang="EN-US"}**[（]{style="font-family:宋体"}[517]{lang="EN-US"}[）、]{style="font-family:宋体"}**[tftp]{lang="EN-US"}**[（]{style="font-family:宋体"}[69]{lang="EN-US"}[）、]{style="font-family:宋体"}**[time]{lang="EN-US"}**[（]{style="font-family:宋体"}[37]{lang="EN-US"}[）、]{style="font-family:宋体"}**[who]{lang="EN-US"}**[（]{style="font-family:宋体"}[513]{lang="EN-US"}[）或]{style="font-family:宋体"}**[xdmcp]{lang="EN-US"}**[（]{style="font-family:宋体"}[177]{lang="EN-US"}[）]{style="font-family:宋体"}

[**[destination-port]{lang="FR"}**]{#struct_0_x4306_x6993_383925340}[ ]{lang="FR"}[{ **object-group** *port-group-name* \| ]{lang="EN-US"}*[operator]{lang="FR"}*[ *port1* \[ *port2* \] }]{lang="FR"}

[[目的端口]{style="font-family:宋体"}]{#struct_0_x4306_x6993_822968562}

[[定义]{style="font-family:宋体"}[TCP/UDP]{lang="EN-US"}]{#struct_0_x4306_x6993_1215426392}[报文的目的端口信息]{style="font-family:宋体"}

[[{ **ack** *ack-value* \| **fin** *fin-value* \| **psh** *psh-value* \| **rst** *rst-value* \| **syn** *syn-value* \| **urg** *urg-value* } \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x88009453}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_2131433075}[报文标识]{style="font-family:宋体"}

[[定义对携带不同标志位（包括]{style="font-family:宋体"}[ACK]{lang="EN-US"}]{#struct_0_x4306_x6993_x517505608}[、]{style="font-family:宋体"}[FIN]{lang="EN-US"}[、]{style="font-family:宋体"}[PSH]{lang="EN-US"}[、]{style="font-family:宋体"}[RST]{lang="EN-US"}[、]{style="font-family:宋体"}[SYN]{lang="EN-US"}[和]{style="font-family:宋体"}[URG]{lang="EN-US"}[六种）的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文的处理规则]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_300822606}[协议特有的参数。表示匹配携带不同标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，各]{style="font-family:宋体"}*[value]{lang="EN-US"}*[的取值可为]{style="font-family:宋体"}[0]{lang="EN-US"}[或]{style="font-family:宋体"}[1]{lang="EN-US"}[（]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不携带此标志位，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示携带此标志位）]{style="font-family:宋体"}

[[对于一条]{style="font-family:宋体"}]{#struct_0_x4306_x6993_2011300954}[规则中各标志位的配置组合，不同产品的处理方式（"与"或"或"）不同，请以设备的实际情况为准。譬如：当配置为]{style="font-family:宋体"}**[ack]{lang="EN-US"}**[ 0 **psh** 1]{lang="EN-US"}[时，有些产品将匹配不携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[标志位且携带]{style="font-family:宋体"}[PSH]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，而有些产品则匹配不携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[或携带]{style="font-family:宋体"}[PSH]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文]{style="font-family:宋体"}

[**[established]{lang="EN-US"}**]{#struct_0_x4306_x6993_x88468204}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_1897421818}[连接建立标识]{style="font-family:宋体"}

[[定义对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_x102767731}[连接报文的处理规则]{style="font-family:宋体"}

[[TCP]{lang="EN-US"}]{#struct_0_x4306_x6993_1061310297}[协议特有的参数。对于路由器，表示匹配携带]{style="font-family:宋体"}[ACK]{lang="EN-US"}[或]{style="font-family:宋体"}[RST]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接报文；对于交换机，请以各产品实际情况为准]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*]{#struct_0_x4306_x6993_x228174872}[为]{style="font-family:宋体"}**[icmpv6]{lang="EN-US"}**[（]{style="font-family:宋体"}[58]{lang="EN-US"}[）时，用户还可配置如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-15]{lang="EN-US"}](?872051014#_Ref259116368)[所示的规则信息参数。]{style="font-family:宋体"}

[]{#struct_0_x4306_x6993_x371577244}[]{#_Ref259116368}[[表1-15 ]{lang="EN-US"}[ICMPv6]{lang="EN-US"}]{#_Toc138129458}[特有的规则信息]{style="font-family:黑体"}[参数]{style="font-family:黑体"}

[]{#table_struct_0_x363562050}[[参数]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1483098475}

[[类别]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x88533740}

[[作用]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x108813734}

[[说明]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x897155764}

[**[icmp6-type]{lang="EN-US"}**[ { *icmp6-type* *icmp6-code* \| *icmp6-message* }]{lang="EN-US"}]{#struct_0_x4306_x6993_1504543597}

[[ICMPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x121852238}[报文的消息类型和消息码]{style="font-family:宋体"}

[[指定本规则中]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_1277094675}[报文的消息类型和消息码信息]{style="font-family:宋体"}

[*[icmp6-type]{lang="EN-US"}*]{#struct_0_x4306_x6993_x88337132}[：]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[消息类型，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[*[icmp6-code]{lang="EN-US"}*]{#struct_0_x4306_x6993_x738739930}[：]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[消息码，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}

[*[icmp6-message]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1570696465}[：]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[消息名称。可以输入的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[消息名称，及其与消息类型和消息码的对应关系如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[1-16]{lang="EN-US"}](?872051014#_Ref139034904)[所示]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#struct_0_x4306_x6993_x481015151}[]{#_Ref139034904}[[表1-16 ]{lang="EN-US"}[ICMPv6]{lang="EN-US"}]{#_Toc138129459}[消息名称与消息类型和消息码的对应关系]{style="font-family:黑体"}

[]{#table_struct_0_x364251554}[[ICMPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_926190344}[消息名称]{style="font-family:黑体"}

[[ICMPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x1922248558}[消息类型]{style="font-family:黑体"}

[[ICMPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_2053527187}[消息码]{style="font-family:黑体"}

[[echo-reply]{lang="EN-US"}]{#struct_0_x4306_x6993_x88402668}

[[129]{lang="EN-US"}]{#struct_0_x4306_x6993_288763188}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x239149114}

[[echo-request]{lang="EN-US"}]{#struct_0_x4306_x6993_2093617742}

[[128]{lang="EN-US"}]{#struct_0_x4306_x6993_840220941}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1754158889}

[[err-Header-field]{lang="EN-US"}]{#struct_0_x4306_x6993_x88206060}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_x1915141114}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x1364228944}

[[frag-time-exceeded]{lang="EN-US"}]{#struct_0_x4306_x6993_1266093288}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_x771575403}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x88271596}

[[hop-limit-exceeded]{lang="EN-US"}]{#struct_0_x4306_x6993_51153938}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_542611222}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_1234242545}

[[host-admin-prohib]{lang="EN-US"}]{#struct_0_x4306_x6993_831192727}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x88074988}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x952953640}

[[host-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_763729177}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x302545218}

[[3]{lang="EN-US"}]{#struct_0_x4306_x6993_519780427}

[[neighbor-advertisement]{lang="EN-US"}]{#struct_0_x4306_x6993_x88140524}

[[136]{lang="EN-US"}]{#struct_0_x4306_x6993_138251253}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x1965060712}

[[neighbor-solicitation]{lang="EN-US"}]{#struct_0_x4306_x6993_994770977}

[[135]{lang="EN-US"}]{#struct_0_x4306_x6993_365525751}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x87943916}

[[network-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_1464592658}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_383990876}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_795455568}

[[packet-too-big]{lang="EN-US"}]{#struct_0_x4306_x6993_x88009452}

[[2]{lang="EN-US"}]{#struct_0_x4306_x6993_2131433076}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x517571144}

[[port-unreachable]{lang="EN-US"}]{#struct_0_x4306_x6993_1084906982}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004425510}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_361336480}

[[redirect]{lang="EN-US"}]{#struct_0_x4306_x6993_x2106798419}

[[137]{lang="EN-US"}]{#struct_0_x4306_x6993_x391451490}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004359974}

[[router-advertisement]{lang="EN-US"}]{#struct_0_x4306_x6993_800178093}

[[134]{lang="EN-US"}]{#struct_0_x4306_x6993_645086573}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004556582}

[[router-solicitation]{lang="EN-US"}]{#struct_0_x4306_x6993_1460470791}

[[133]{lang="EN-US"}]{#struct_0_x4306_x6993_x483896497}

[[0]{lang="EN-US"}]{#struct_0_x4306_x6993_388705963}

[[unknown-ipv6-opt]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004491046}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_1929204100}

[[2]{lang="EN-US"}]{#struct_0_x4306_x6993_1274044854}

[[unknown-next-hdr]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004163366}

[[4]{lang="EN-US"}]{#struct_0_x4306_x6993_342291176}

[[1]{lang="EN-US"}]{#struct_0_x4306_x6993_x456220968}

**[ ]{lang="EN-US"}**

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1517220321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x865991324}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x2004097830}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1934953774}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的任意一条已有规则；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，不允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的已有规则，否则将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x77891032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1847424878}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x2136053608}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **ipv6** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1706802869}

[]{#_Toc291080261}[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_142975837}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[创建规则如下：允许]{style="font-family:宋体"}[2030:5060::]{lang="EN-US"}[/64]{lang="FR"}[网段内的主机与]{style="font-family:宋体"}[FE80:5060::/96]{lang="EN-US"}[网段内主机的]{style="font-family:宋体"}[WWW]{lang="EN-US"}[端口（端口号为]{style="font-family:宋体"}[80]{lang="EN-US"}[）建立连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x520234914}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl]{lang="FR"}[-ipv6]{lang="EN-US"}[-adv-3000\] rule permit tcp source 2030:5060::/64 destination fe80:5060::/96 destination-port eq 80]{lang="FR"}

[]{#struct_0_x4306_x6993_x2004294438}[]{#_Toc156106574}[]{#_Toc120681178}[]{#_Toc120681179}[]{#_Toc156106575}[\# ]{lang="EN-US"}[为]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3001]{lang="EN-US"}[创建规则如下：允许]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文通过，但拒绝发往]{style="font-family:宋体"}[FE80:5060:1001::/48]{lang="EN-US"}[网段的]{style="font-family:宋体"}[ICMPv6]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1448896594}

[\[Sysname\] acl ipv6 advanced 3001]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3001\] rule deny icmpv6 destination fe80:5060:1001:: 48]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3001\] rule permit ipv6]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x1927641293}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3002]{lang="EN-US"}[创建规则如下：在出、入双方向上都允许建立]{style="font-family:宋体"}[FTP]{lang="EN-US"}[连接并传输]{style="font-family:宋体"}[FTP]{lang="EN-US"}[数据。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_2049457644}

[\[Sysname\] acl ipv6 advanced 3002]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3002\] rule permit tcp source-port eq ftp]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3002\] rule permit tcp source-port eq ftp-data]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3002\] rule permit tcp destination-port eq ftp]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3002\] rule permit tcp destination-port eq ftp-data]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x76943154}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3003]{lang="EN-US"}[创建规则如下：在出、入双方向上都允许]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[报文和]{style="font-family:宋体"}[SNMP Trap]{lang="EN-US"}[报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004228902}

[\[Sysname\] acl ipv6 advanced 3003]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3003\] rule permit udp source-port eq snmp]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3003\] rule permit udp source-port eq snmptrap]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3003\] rule permit udp destination-port eq snmp]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3003\] rule permit udp destination-port eq snmptrap]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_x118971026}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3004]{lang="EN-US"}[创建规则如下：在含有逐跳头的报文中，只允许转发含有]{style="font-family:宋体"}[MLD]{lang="EN-US"}[选项（]{style="font-family:宋体"}[Type]{lang="EN-US"}[＝]{style="font-family:宋体"}[5]{lang="EN-US"}[）的报文，丢弃其他报文。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x789815707}

[\[Sysname\] acl ipv6 advanced 3004]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3004\] rule permit ipv6 hop-by-hop type 5]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3004\] rule deny ipv6 hop-by-hop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2003901222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_695502698}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1254863886}[ **logging** **interval**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1139583404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_1276056827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1774784341}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}

::::: {#-592467063 .myid}
[]{#_Toc404791903}[]{#struct_0_x4306_x6993_16487289}

**ACL \-- ACL配置命令 \-- rule (IPv6 basic ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 21 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x194717456}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x2003835686}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_1899156423}[命令用来为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_2094678466}[命令用来为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则或删除规则中的部分内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x53631080}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } \[ **counting** \| **fragment** \| **logging** \| **routing** \[ **type** *routing-type* \] \| **source** { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address*/*source-prefix* \| **any** } \| **time-range** *time-range-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x750394799}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* \[ **counting** \| **fragment** \| **logging** \| **routing** \| **source** \| **time-range** \| **vpn-instance** \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1567744046}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1754440246}

[[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x555688549}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x223635546}

[[IPv6]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004425509}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2011250979}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_14597235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x731990142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1705647373}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_1492126477}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_x606322233}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_x946665497}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2004359973}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter ipv6]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能。]{style="font-family:宋体"}

[**[fragment]{lang="EN-US"}**]{#struct_0_x4306_x6993_40663206}[：表示仅对非首片分片报文有效，而对非分片报文和首片分片报文无效。若未指定本参数，表示该规则对非分片报文和分片报文均有效。]{style="font-family:宋体"}

[**[logging]{lang="EN-US"}**]{#struct_0_x4306_x6993_155337581}[：表示对符合条件的报文可记录日志信息。该功能需要使用该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的模块支持日志记录功能，例如报文过滤。]{style="font-family:宋体"}

[**[routing]{lang="EN-US"}**[ \[ **type** *routing-type* \]]{lang="EN-US"}]{#struct_0_x4306_x6993_x1530798549}[：表示对所有或指定类型的路由头有效，]{style="font-family:宋体"}*[routing-type]{lang="EN-US"}*[表示路由头类型的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。若指定了]{style="font-family:宋体"}**[type]{lang="EN-US"}**[ *routing-type*]{lang="EN-US"}[参数，表示仅对指定类型的路由头有效；否则，表示对所有类型的路由头都有效。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**[ { **object-group** *addr-group-name* \| *source-address* *source-prefix* \| *source-address*/*source-prefix* \| **any** }]{lang="EN-US"}]{#struct_0_x4306_x6993_2015018795}[：指定规则的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[addr-group-name]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址对象组的名称，]{style="font-family:宋体"}*[source-address]{lang="EN-US"}*[表示报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[source-prefix]{lang="EN-US"}*[表示源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，]{style="font-family:宋体"}**[any]{lang="EN-US"}**[表示任意源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1240440181}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_1077101402}[：表示对指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中的报文有效。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，表示该规则仅对非]{style="font-family:宋体"}[VPN]{lang="EN-US"}[报文有效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x1994801075}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1989593093}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建或修改的规则不能与已有规则的内容完全相同，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x2004556581}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[新创建或修改的规则若指定对象组，则该对象组必须存在，否则将提示出错，并导致该操作失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x77956569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x4306_x6993_1057186264}[ACL]{lang="EN-US"}[的规则匹配顺序为配置顺序时，允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的任意一条已有规则；当]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的规则匹配顺序为自动排序时，不允许修改该]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内的已有规则，否则将提示出错。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x2106562222}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}[命令时，如果没有指定任何可选参数，则删除整条规则；如果指定了可选参数，则只删除该参数所对应的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_904568986}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **ipv6** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1744796329}

[]{#struct_0_x4306_x6993_1560709072}[]{#_Toc120681189}[]{#_Toc120681190}[]{#_Toc120681197}[\# ]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[创建规则如下：仅允许来自]{style="font-family:宋体"}[1001::/16]{lang="EN-US"}[、]{style="font-family:宋体"}[3124:1123::/32]{lang="EN-US"}[和]{style="font-family:宋体"}[FE80:5060:1001::/48]{lang="EN-US"}[网段的报文通过，而拒绝来自所有其它网段的报文通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_484844326}

[\[Sysname\] acl ipv6 basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source 1001:: 16]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source 3124:1123:: 32]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule permit source fe80:5060:1001:: 48]{lang="EN-US"}

[\[Sysname-acl-ipv6-basic-2000\] rule deny source any]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004491045}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_1525919573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_1501383728}[ **logging** **interval**]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1435717777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_675039343}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_x793532134}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#-1327497841 .myid}
[]{#_Toc404791904}[]{#struct_0_x4306_x6993_214645968}[]{#_Toc291080263}

**ACL \-- ACL配置命令 \-- rule (user-defined ACL view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x593342140}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_376454313}
:::

[ ]{lang="EN-US"}

[**[rule]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2004163365}[命令用来为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[创建一条规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1223792765}[命令用来为用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[删除一条规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x225849559}

[**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } \[ { { **ipv4** \| **ipv6** \| **l2** \| **l4** } *rule-string* *rule-mask* *offset* }&\<1-8\> \] \[ **counting** \| **time-range** *time-range-name* \] \*]{lang="EN-US"}]{#struct_0_x4306_x6993_1851988810}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id*]{lang="EN-US"}]{#struct_0_x4306_x6993_317507779}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_579564435}

[[用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_56826591}[内不存在任何规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2017184006}

[[用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4306_x6993_x1970080424}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004097829}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_12705009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_314058055}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_233651126}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1424845788}[：指定用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的编号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。若未指定本参数，系统将按照步长从]{style="font-family:宋体"}[0]{lang="EN-US"}[开始，自动分配一个大于现有最大编号的最小编号。譬如现有规则的最大编号为]{style="font-family:宋体"}[28]{lang="EN-US"}[，步长为]{style="font-family:宋体"}[5]{lang="EN-US"}[，那么自动分配的新编号将是]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x4306_x6993_x281984784}[：表示拒绝符合条件的报文。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2057365565}[：表示允许符合条件的报文。]{style="font-family:宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1206293941}[：表示从]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2004294437}[：表示从]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[l2]{lang="EN-US"}**]{#struct_0_x4306_x6993_1045612067}[：表示从]{style="font-family:宋体"}[L2]{lang="EN-US"}[帧头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[l4]{lang="EN-US"}**]{#struct_0_x4306_x6993_x955426216}[：表示从]{style="font-family:宋体"}[L4]{lang="EN-US"}[报文头开始偏移（具体的偏移开始位与设备的型号有关，请以设备的实际情况为准）。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[rule-string]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1302776090}[：指定用户自定义的规则字符串，必须是]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数组成，字符长度必须是偶数。]{style="font-family:宋体"}

[*[rule-mask]{lang="EN-US"}*]{#struct_0_x4306_x6993_x1255226351}[：指定规则字符串的掩码，用于和报文作"与"操作，必须是]{style="font-family:宋体"}[16]{lang="EN-US"}[进制数组成，字符长度必须是偶数，且必须与]{style="font-family:宋体"}*[rule-string]{lang="EN-US"}*[的长度相同。]{style="font-family:宋体"}

[*[offset]{lang="EN-US"}*]{#struct_0_x4306_x6993_x430463403}[：指定偏移量，它以用户指定的报文头部为基准，指定从第几个字节开始进行比较。]{style="font-family:宋体"}

[[&\<1-8\>]{lang="EN-US"}]{#struct_0_x4306_x6993_x2135664850}[：表示前面的参数最多可以输入]{style="font-family:宋体"}[8]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[counting]{lang="EN-US"}**]{#struct_0_x4306_x6993_x706169075}[：表示使能规则匹配统计功能，缺省为关闭。本参数用于使能本规则的匹配统计功能，而]{style="font-family:宋体"}**[packet-filter]{lang="EN-US"}**[命令中的]{style="font-family:宋体"}**[hardware-count]{lang="EN-US"}**[参数则用于使能指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[内所有规则的匹配统计功能。]{style="font-family:宋体"}

[**[time-range]{lang="EN-US"}**[ *time-range-name*]{lang="EN-US"}]{#struct_0_x4306_x6993_x1609430450}[：指定本规则生效的时间段。]{style="font-family:宋体"}*[time-range-name]{lang="EN-US"}*[表示时间段的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。若该时间段尚未配置，该规则仍会成功创建但系统将给出提示信息，并在该时间段的配置完成后此规则才会生效。有关时间段的详细介绍和具体配置过程，请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"时间段"。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004228901}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x1685054967}**[rule]{lang="EN-US"}**[命令时，如果指定编号的规则不存在，则创建一条新的规则；如果指定编号的规则已存在，则对旧规则进行修改，即在其原有内容的基础上叠加新的内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[新创建的规则不能与已有规则的内容完全相同，否则将提示出错，并导致创建失败。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x381962717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[使用]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **rule**]{lang="EN-US"}]{#struct_0_x4306_x6993_x1439015910}[命令时必须指定一个已存在规则的编号，可以使用]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}**[ **acl** **all**]{lang="EN-US"}[命令来查看所有已存在的规则。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_821750568}

[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_649690162}[为用户自定义]{style="font-family:宋体"}[ACL 5005]{lang="EN-US"}[创建规则如下：允许从]{style="font-family:宋体"}[L2]{lang="EN-US"}[帧头开始算起第]{style="font-family:宋体"}[13]{lang="EN-US"}[、]{style="font-family:宋体"}[14]{lang="EN-US"}[两字节的内容为]{style="font-family:宋体"}[0x0806]{lang="EN-US"}[的报文（即]{style="font-family:宋体"}[ARP]{lang="EN-US"}[报文）通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_x2049390798}

[\[Sysname\] acl user-defined 5005]{lang="EN-US"}

[\[Sysname-acl-user-5005\] rule permit l2 0806 ffff 12]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_1404659886}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_x4306_x6993_x2003901221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_1098787225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[time-range]{lang="EN-US"}**]{#struct_0_x4306_x6993_x1546334999}[（]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[时间段）]{lang="EN-US" style="font-family:宋体"}
:::::

::::: {#1031359485 .myid}
[]{#_Toc404791905}[]{#struct_0_x4306_x6993_x897383441}

**ACL \-- ACL配置命令 \-- rule comment**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**[ **comment**]{lang="EN-US"}]{#struct_0_x4306_x6993_756402167}[命令用来为指定规则配置描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rule** **comment**]{lang="EN-US"}]{#struct_0_x4306_x6993_1760276195}[命令用来删除指定规则的描述信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x515895384}

[**[rule]{lang="EN-US"}**[ *rule-id* **comment** *text*]{lang="EN-US"}]{#struct_0_x4306_x6993_x798609159}

[**[undo]{lang="EN-US"}**[ **rule** *rule-id* **comment**]{lang="EN-US"}]{#struct_0_x4306_x6993_x964686600}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2003835685}

[[规则没有任何描述信息。]{style="font-family:宋体"}]{#struct_0_x4306_x6993_x829726932}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x123201464}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_x786926261}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[用户自定义]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 23 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_x579981694}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x1533374897}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_329459647}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1319778757}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_224962977}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004425512}

[*[rule-id]{lang="EN-US"}*]{#struct_0_x4306_x6993_x801462934}[：指定规则的编号，该规则必须存在。取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[text]{lang="EN-US"}*]{#struct_0_x4306_x6993_x12974035}[：表示规则的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x820248200}

[[使用]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ **comment**]{lang="EN-US"}]{#struct_0_x4306_x6993_x364993138}[命令时，如果指定的规则没有描述信息，则为其添加描述信息，否则修改其描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_703889273}

[]{#struct_0_x4306_x6993_x81205808}[]{#_Toc252888219}[]{#_Toc253213289}[]{#_Toc253213635}[]{#_Toc252888220}[]{#_Toc253213290}[]{#_Toc253213636}[]{#_Toc252888222}[]{#_Toc253213292}[]{#_Toc253213638}[]{#_Toc252888223}[]{#_Toc253213293}[]{#_Toc253213639}[]{#_Toc252888224}[]{#_Toc253213294}[]{#_Toc253213640}[]{#_Toc252888226}[]{#_Toc253213296}[]{#_Toc253213642}[]{#_Toc252888227}[]{#_Toc253213297}[]{#_Toc253213643}[]{#_Toc252888228}[]{#_Toc253213298}[]{#_Toc253213644}[\# ]{lang="EN-US"}[为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[配置规则]{style="font-family:宋体"}[0]{lang="EN-US"}[，并为该规则配置描述信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_1874622089}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule 0 deny source 1.1.1.1 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule 0 comment This rule is used on GigabitEthernet 1/0/1.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_2101485059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_x2004359976}
:::::

::::: {#-2008104610 .myid}
[]{#_Toc404791906}[]{#struct_0_x4306_x6993_x362621321}[]{#_Toc303850436}[]{#_Toc303858036}

**ACL \-- ACL配置命令 \-- step**

------------------------------------------------------------------------

[**[step]{lang="EN-US"}**]{#struct_0_x4306_x6993_x326527457}[命令用来配置规则编号的步长。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **step**]{lang="EN-US"}]{#struct_0_x4306_x6993_1949142179}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2147460476}

[**[step]{lang="EN-US"}**[ *step-value*]{lang="EN-US"}]{#struct_0_x4306_x6993_x836996379}

[**[undo]{lang="EN-US"}**[ **step**]{lang="EN-US"}]{#struct_0_x4306_x6993_x938608195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_563513268}

[[规则编号的步长为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_x4306_x6993_x614273739}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004556584}

[[IPv4]{lang="EN-US"}]{#struct_0_x4306_x6993_653901737}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}[/]{lang="EN-US"}[二层]{style="font-family:宋体"}[ACL]{lang="EN-US"}[视图]{style="font-family:宋体"}

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](ACL命令.files/image002.png){#图片 24 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4306_x6993_608016837}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[不同型号的设备支持的视图不同，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4306_x6993_x702237515}
:::

[ ]{lang="EN-US"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_244534929}

[[network-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_x898019284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4306_x6993_1748241350}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_34912439}

[*[step-value]{lang="EN-US"}*]{#struct_0_x4306_x6993_221178587}[：表示规则编号的步长值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_x2004491048}

[]{#_Toc291080268}[[\# ]{lang="EN-US"}]{#struct_0_x4306_x6993_766404686}[将]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL 2000]{lang="EN-US"}[的规则编号的步长配置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4306_x6993_679474665}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] step 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4306_x6993_448668499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x4306_x6993_1346123162}

[ ]{lang="EN-US"}
:::::
