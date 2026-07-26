::: {#-1385181916 .myid}
[]{#_Toc404787986}[]{#struct_0_x4702_18917_534118862}[]{#_Toc138212535}[]{#_Toc93984760}[]{#_Toc61236300}[]{#_Toc61093047}[]{#_Toc58812024}[]{#_Toc56887153}[]{#_Toc45164769}

**OSPF \-- OSPF配置命令 \-- abr-summary (OSPF area view)**

------------------------------------------------------------------------

[**[abr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x725166199}[命令用来配置]{style="font-family:宋体"}[ABR]{lang="EN-US"}[路由聚合。]{style="font-family:宋体"}

[**[undo abr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_627578773}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_635788675}

[**[abr-summary]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* } \[ **advertise** \| **not-advertise** \] \[ **cost** *cost* \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1270854417}

[**[undo]{lang="EN-US"}**[ **abr-summary** *ip-address* { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_x4702_18917_x1931030022}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x875233940}

[[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_x322479758}[不对路由进行聚合。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x168617266}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1333219781}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1135035794}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x366948853}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1476623566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1962191194}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x46806975}[：聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4702_18917_x1005981666}[：聚合路由的网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4702_18917_x322414222}[：聚合路由的网络掩码，点分十进制形式。]{style="font-family:宋体"}

[**[advertise ]{lang="EN-US"}**[\| **not-advertise**]{lang="EN-US"}]{#struct_0_x4702_18917_1432694510}[：是否发布这条聚合路由。缺省时发布聚合路由。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x4702_18917_x312458644}[：聚合路由的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为所有被聚合的路由中最大的开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_650213241}

[[本命令只适用于区域边界路由器（]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_1593580750}[），用来对某一个区域内的路由信息进行聚合。对于属于该聚合网段范围的路由，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向其它区域只发送一条聚合后的路由。一个区域可配置多条聚合网段，这样]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[可对多个网段进行聚合。]{style="font-family:宋体"}

[[当配置了]{style="font-family:宋体"}**[undo abr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_1889359876}[命令后，原来被聚合的路由又重新被发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_x4702_18917_x178345}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1736868242}[将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[中两个网段]{style="font-family:宋体"}[36.42.10.0/24]{lang="EN-US"}[和]{style="font-family:宋体"}[36.42.110.0/24]{lang="EN-US"}[的路由聚合成一条聚合路由]{style="font-family:宋体"}[36.42.0.0/16]{lang="EN-US"}[向其它区域发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1599310258}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 1]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] network 36.42.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] network 36.42.110.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] abr-summary 36.42.0.0 255.255.0.0]{lang="EN-US"}
:::

::: {#1478641573 .myid}
[]{#_Toc404787987}[]{#struct_0_x4702_18917_1084446930}[]{#_Toc138212536}[]{#_Toc93984761}[]{#_Toc61236301}[]{#_Toc61093048}[]{#_Toc58812025}[]{#_Toc56887154}

**OSPF \-- OSPF配置命令 \-- area (OSPF view)**

------------------------------------------------------------------------

[**[area]{lang="EN-US"}**]{#struct_0_x4702_18917_212820005}[命令用来创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域，并进入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域视图。]{style="font-family:宋体"}

[**[undo area]{lang="EN-US"}**]{#struct_0_x4702_18917_360720154}[命令用来删除指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_236097468}

[**[area]{lang="EN-US"}**[ *area-id*]{lang="EN-US"}]{#struct_0_x4702_18917_x567338906}

[**[undo area ]{lang="EN-US"}***[area-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1468302294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599375794}

[[没有配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1885517463}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x103230310}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1868492991}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1264008325}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_600682230}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1808604727}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_573765138}

[*[area-id]{lang="EN-US"}*]{#struct_0_x4702_18917_256675897}[：]{style="font-family:宋体"}[区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599441330}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_326362000}[创建]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[并进入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x482194548}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 0]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.0\]]{lang="EN-US"}
:::

::: {#-1078482664 .myid}
[]{#_Toc404787988}[]{#struct_0_x4702_18917_1576867535}[]{#_Toc138212537}[]{#_Toc93984762}[]{#_Toc61236302}[]{#_Toc61093049}[]{#_Toc58812026}[]{#_Toc56887155}[]{#_Toc45164771}

**OSPF \-- OSPF配置命令 \-- asbr-summary**

------------------------------------------------------------------------

[**[asbr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x199722232}[命令用来配置]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由聚合。]{style="font-family:宋体"}

[**[undo asbr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_217398549}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1094485253}

[**[asbr-summary]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* } \[ **cost** *cost* \| **not-advertise** \| **nssa-only** \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_x1249790475}

[**[undo asbr-summary ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[{ *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_x4702_18917_1599506866}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x895270595}

[[ASBR]{lang="EN-US"}]{#struct_0_x4702_18917_x745921158}[不对路由进行聚合。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x42105272}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1879774804}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x287260032}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x846052283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x593877204}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599048114}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x1978027051}[：聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4702_18917_132585060}[：聚合路由的网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4702_18917_1289630424}[：聚合路由的网络掩码，点分十进制格式。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x4702_18917_x1006143698}[：聚合路由的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。如果未指定本参数，对于]{style="font-family:宋体"}[Type-1]{lang="EN-US"}[外部路由，]{style="font-family:宋体"}*[cost]{lang="EN-US"}*[取所有被聚合的路由中最大的开销值作为聚合路由的开销；对于]{style="font-family:宋体"}[Type-2]{lang="EN-US"}[外部路由，]{style="font-family:宋体"}*[cost]{lang="EN-US"}*[取所有被聚合的路由中最大的开销值加]{style="font-family:宋体"}[1]{lang="EN-US"}[作为聚合路由的开销。]{style="font-family:宋体"}

[**[not-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_x1174922773}[：不通告聚合路由。如果未指定本参数，将通告聚合路由。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_x4702_18917_x2062450573}[：设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位为不置位，即在对端路由器上不能转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[。缺省时，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}***[ tag]{lang="EN-US"}*]{#struct_0_x4702_18917_1398866781}[：聚合路由的标识，可以通过路由策略控制聚合路由的发布，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1869463325}

[[如果本地路由器是]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_x4702_18917_1599113650}[，对引入的聚合地址范围内的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[描述的路由进行聚合；当配置了]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域时，对引入的聚合地址范围内的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[描述的路由进行聚合。]{style="font-family:宋体"}

[[如果本地路由器同时是]{style="font-family:宋体"}[ASBR]{lang="EN-US"}]{#struct_0_x4702_18917_722533055}[和]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，并且是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的转换路由器，将对由]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转化成的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[进行聚合处理；如果不是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的转换路由器，则[]{#_Hlt15702645}不进行聚合处理。]{style="font-family:宋体"}

[[配置]{style="font-family:宋体"}**[asbr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x1221584386}[命令后，对处于聚合地址范围内的外部路由，本地路由器只向邻居路由器发布一条聚合后的路由；配置]{style="font-family:宋体"}**[undo asbr-summary]{lang="EN-US"}**[命令后，原来被聚合的外部路由将重新被发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x662621957}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1989187109}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[对引入的路由进行聚合，聚合路由的标识为]{style="font-family:宋体"}[2]{lang="EN-US"}[，开销值为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1754780964}

[\[Sysname\] ip route-static 10.2.1.0 24 null 0]{lang="EN-US"}

[\[Sysname\] ip route-static 10.2.2.0 24 null 0]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] import-route static]{lang="EN-US"}

[\[Sysname-ospf-100\] asbr-summary 10.2.0.0 255.255.0.0 tag 2 cost 100]{lang="EN-US"}
:::

::: {#-947553691 .myid}
[]{#_Toc404787989}[]{#struct_0_x4702_18917_x414105838}[]{#_Toc138212538}[]{#_Toc93984763}[]{#_Toc61236303}[]{#_Toc61093050}[]{#_Toc58812027}[]{#_Toc56887156}[]{#_Toc45164772}

**OSPF \-- OSPF配置命令 \-- authentication-mode**

------------------------------------------------------------------------

[**[authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_x923521046}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域所使用的验证模式。]{style="font-family:宋体"}

[**[undo authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_x1052215848}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1316283927}

[[MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x1889884268}[验证模式：]{style="font-family:宋体"}

[**[authentication-mode]{lang="EN-US"}**[ { **hmac-md5** \| **md5** } *key-id* { **cipher** \| **plain** } *password*]{lang="EN-US"}]{#struct_0_x4702_18917_x1005026658}

[**[undo authentication-mode]{lang="EN-US"}**[ \[ { **hmac-md5** \| **md5** } *key-id* \]]{lang="EN-US"}]{#struct_0_x4702_18917_1061237592}

[[简单验证模式：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1795914686}

[**[authentication-mode simple]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ **cipher** \| **plain** } *password*]{lang="EN-US"}]{#struct_0_x4702_18917_1599244722}

[**[undo authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_321071960}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1390095619}

[[没有配置区域验证模式。]{style="font-family:宋体"}]{#struct_0_x4702_18917_1387771517}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1427510355}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1865101799}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1960298561}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_130264888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1797797752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599834546}

[**[hmac-md5]{lang="EN-US"}**]{#struct_0_x4702_18917_x72209900}[：]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x4702_18917_1899108838}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x4702_18917_x1422675019}[：简单验证模式。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1155453865}[：验证字标识符，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x4702_18917_162252474}[：以密文形式设置密码。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x4702_18917_x1356308276}[：以明文形式设置密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_x4702_18917_x1734154655}[：验证密码，区分大小写。对于简单验证模式，如果以明文形式键入，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[个字符的字符串；如果以密文形式键入，则为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[41]{lang="EN-US"}[个字符的字符串；对于]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证模式，如果以明文形式键入，则为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串；如果以密文形式键入，则为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599900082}

[[一个区域中所有路由器的验证模式和验证密码必须一致。]{style="font-family:宋体"}]{#struct_0_x4702_18917_707811213}

[[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x4702_18917_518456475}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1216267964}[可指定区域下使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证或简单验证两种方式，但不能同时指定；使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证方式时，可配置多条]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证命令，但]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[是唯一的，同一]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[只能配置一个验证字。]{style="font-family:宋体"}

[[修改]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1652214576}[区域的]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字的步骤如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[首先在该区域配置新的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x720612631}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；此时若邻居设备尚未配置新的]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，便会触发]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。在这个过程中，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[会发送分别携带各个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字的多份报文，使得已配置新验证字的邻居设备、和尚未配置新验证字的邻居设备都能验证通过，保持邻居关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[然后在各个邻居设备上也都配置相同的新]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1456411954}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；当本设备上收到所有邻居的携带新验证字的报文后，便会退出]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最后在本设备和所有邻居上都删除旧的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1940246006}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；建议区域下不要保留多个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，每次]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1768200884}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1599310259}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[明文验证模式，]{style="font-family:宋体"}[验证字标识符为]{style="font-family:宋体"}[15]{lang="EN-US"}[，验证密码为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1084381394}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 0]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.0\] authentication-mode md5 15 plain abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1377440727}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_x790778652}
:::

::: {#-1500420296 .myid}
[]{#_Toc45164773}[]{#_Toc404787990}[]{#struct_0_x4702_18917_1154384242}[]{#_Toc138212539}[]{#_Toc93984764}[]{#_Toc61236304}[]{#_Toc61093051}[]{#_Toc58812028}[]{#_Toc56887157}[]{#_Toc45164828}

**OSPF \-- OSPF配置命令 \-- bandwidth-reference (OSPF view)**

------------------------------------------------------------------------

[**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_x4702_18917_2089243332}[命令用来配置计算链路开销时所依据的带宽参考值。]{style="font-family:宋体"}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_x4702_18917_x499780077}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599375795}

[**[bandwidth-reference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x4702_18917_1885451927}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_x4702_18917_x1612125301}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x512072341}

[[计算链路开销时所依据的带宽参考值为]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}]{#struct_0_x4702_18917_2095769726}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_342438556}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1386492634}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2065711705}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1462156231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1599441331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_326427536}

[*[value]{lang="EN-US"}*]{#struct_0_x4702_18917_1710920205}[：计算链路开销时所依据的带宽参考值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x265812995}

[[如果没有配置链路的开销值，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1372457733}[根据链路带宽来计算开销值，接口开销＝带宽参考值÷接口期望带宽（接口期望带宽通过命令]{style="font-family:宋体"}**[bandwidth]{lang="EN-US"}**[进行配置，具体情况请参见接口分册命令参考中的介绍）。当计算出来的开销值大于]{style="font-family:宋体"}[65535]{lang="EN-US"}[时，开销取最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[；当计算出来的开销值小于]{style="font-family:宋体"}[1]{lang="EN-US"}[时，开销取最小值]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[常见接口开销的缺省值，如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1750238325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[56kbps]{lang="EN-US"}]{#struct_0_x4702_18917_737220594}[串口：缺省值为]{style="font-family:宋体"}[1785]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[64kbps]{lang="EN-US"}]{#struct_0_x4702_18917_229669140}[串口：缺省值为]{style="font-family:宋体"}[1562]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E1]{lang="EN-US"}]{#struct_0_x4702_18917_1990842323}[（]{style="font-family:宋体"}[2.048Mbps]{lang="EN-US"}[）：缺省值为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ethernet]{lang="EN-US"}]{#struct_0_x4702_18917_1599506867}[（]{lang="EN-US" style="font-family:宋体"}[100Mbps]{lang="EN-US"}[）：缺省值为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loopback]{lang="EN-US"}]{#struct_0_x4702_18917_x895205059}[接口]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}[缺省值为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_429949775}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1050065102}[配置链路的带宽参考值为]{style="font-family:宋体"}[1000Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1760157194}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] bandwidth-reference 1000]{lang="EN-US"}

[]{#_Toc138212540}[]{#_Toc93984769}[]{#_Toc61236305}[]{#_Toc61093052}[]{#_Toc58812029}[]{#_Toc56887158}[]{#struct_0_x4702_18917_x2077588512}[]{#_Toc135105100}[]{#_Toc135105250}[]{#_Toc135105103}[]{#_Toc135105253}[]{#_Toc135105104}[]{#_Toc135105254}[]{#_Toc135105105}[]{#_Toc135105255}[]{#_Toc135105106}[]{#_Toc135105256}[]{#_Toc135105107}[]{#_Toc135105257}[]{#_Toc135105108}[]{#_Toc135105258}[]{#_Toc135105109}[]{#_Toc135105259}[]{#_Toc135105110}[]{#_Toc135105260}[]{#_Toc135105111}[]{#_Toc135105261}[]{#_Toc135105112}[]{#_Toc135105262}[]{#_Toc135105114}[]{#_Toc135105264}[]{#_Toc135105115}[]{#_Toc135105265}[]{#_Toc72032325}[]{#_Toc72050006}[]{#_Toc72052887}[]{#_Toc72054958}[]{#_Toc72151564}[]{#_Toc72032326}[]{#_Toc72050007}[]{#_Toc72052888}[]{#_Toc72054959}[]{#_Toc72151565}[]{#_Toc72032327}[]{#_Toc72050008}[]{#_Toc72052889}[]{#_Toc72054960}[]{#_Toc72151566}[]{#_Toc72032328}[]{#_Toc72050009}[]{#_Toc72052890}[]{#_Toc72054961}[]{#_Toc72151567}[]{#_Toc72032329}[]{#_Toc72050010}[]{#_Toc72052891}[]{#_Toc72054962}[]{#_Toc72151568}[]{#_Toc72032330}[]{#_Toc72050011}[]{#_Toc72052892}[]{#_Toc72054963}[]{#_Toc72151569}[]{#_Toc72032331}[]{#_Toc72050012}[]{#_Toc72052893}[]{#_Toc72054964}[]{#_Toc72151570}[]{#_Toc72032332}[]{#_Toc72050013}[]{#_Toc72052894}[]{#_Toc72054965}[]{#_Toc72151571}[]{#_Toc72032333}[]{#_Toc72050014}[]{#_Toc72052895}[]{#_Toc72054966}[]{#_Toc72151572}[]{#_Toc72032334}[]{#_Toc72050015}[]{#_Toc72052896}[]{#_Toc72054967}[]{#_Toc72151573}[]{#_Toc72032335}[]{#_Toc72050016}[]{#_Toc72052897}[]{#_Toc72054968}[]{#_Toc72151574}[]{#_Toc72032336}[]{#_Toc72050017}[]{#_Toc72052898}[]{#_Toc72054969}[]{#_Toc72151575}[]{#_Toc72032337}[]{#_Toc72050018}[]{#_Toc72052899}[]{#_Toc72054970}[]{#_Toc72151576}[]{#_Toc72032338}[]{#_Toc72050019}[]{#_Toc72052900}[]{#_Toc72054971}[]{#_Toc72151577}[]{#_Toc72032339}[]{#_Toc72050020}[]{#_Toc72052901}[]{#_Toc72054972}[]{#_Toc72151578}[]{#_Toc135105117}[]{#_Toc135105267}[]{#_Toc135105120}[]{#_Toc135105270}[]{#_Toc135105121}[]{#_Toc135105271}[]{#_Toc135105122}[]{#_Toc135105272}[]{#_Toc135105123}[]{#_Toc135105273}[]{#_Toc135105124}[]{#_Toc135105274}[]{#_Toc135105125}[]{#_Toc135105275}[]{#_Toc135105126}[]{#_Toc135105276}[]{#_Toc135105127}[]{#_Toc135105277}[]{#_Toc135105128}[]{#_Toc135105278}[]{#_Toc135105129}[]{#_Toc135105279}[]{#_Toc135105131}[]{#_Toc135105281}[]{#_Toc135105134}[]{#_Toc135105284}[]{#_Toc135105137}[]{#_Toc135105287}[]{#_Toc135105138}[]{#_Toc135105288}[]{#_Toc135105139}[]{#_Toc135105289}[]{#_Toc135105140}[]{#_Toc135105290}[]{#_Toc135105141}[]{#_Toc135105291}[]{#_Toc135105142}[]{#_Toc135105292}[]{#_Toc135105143}[]{#_Toc135105293}[]{#_Toc135105144}[]{#_Toc135105294}[]{#_Toc135105145}[]{#_Toc135105295}[]{#_Toc135105146}[]{#_Toc135105296}[]{#_Toc135105147}[]{#_Toc135105297}[]{#_Toc135105148}[]{#_Toc135105298}[]{#_Toc135105149}[]{#_Toc135105299}[]{#_Toc135105150}[]{#_Toc135105300}[]{#_Toc135105151}[]{#_Toc135105301}[]{#_Toc135105152}[]{#_Toc135105302}[]{#_Toc135105153}[]{#_Toc135105303}[]{#_Toc135105154}[]{#_Toc135105304}[]{#_Toc135105155}[]{#_Toc135105305}[]{#_Toc135105156}[]{#_Toc135105306}[]{#_Toc135105157}[]{#_Toc135105307}[]{#_Toc135105159}[]{#_Toc135105309}[]{#_Toc135105162}[]{#_Toc135105312}[]{#_Toc135105163}[]{#_Toc135105313}[]{#_Toc135105164}[]{#_Toc135105314}[]{#_Toc135105165}[]{#_Toc135105315}[]{#_Toc135105166}[]{#_Toc135105316}[]{#_Toc135105167}[]{#_Toc135105317}[]{#_Toc135105168}[]{#_Toc135105318}[]{#_Toc135105169}[]{#_Toc135105319}[]{#_Toc135105170}[]{#_Toc135105320}[]{#_Toc135105171}[]{#_Toc135105321}[]{#_Toc135105172}[]{#_Toc135105322}[]{#_Toc135105173}[]{#_Toc135105323}[]{#_Toc135105174}[]{#_Toc135105324}[]{#_Toc135105175}[]{#_Toc135105325}[]{#_Toc135105176}[]{#_Toc135105326}[]{#_Toc135105177}[]{#_Toc135105327}[]{#_Toc135105178}[]{#_Toc135105328}[]{#_Toc135105179}[]{#_Toc135105329}[]{#_Toc135105180}[]{#_Toc135105330}[]{#_Toc135105181}[]{#_Toc135105331}[]{#_Toc135105182}[]{#_Toc135105332}[]{#_Toc135105183}[]{#_Toc135105333}[]{#_Toc135105184}[]{#_Toc135105334}[]{#_Toc135105185}[]{#_Toc135105335}[]{#_Toc135105186}[]{#_Toc135105336}[【相关命令】]{style="font-family:
黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf ]{lang="EN-US"}**]{#struct_0_x4702_18917_x116037136}**[cost]{lang="EN-US"}**
:::

::: {#1948332219 .myid}
[]{#_Toc404787991}[]{#struct_0_x4702_18917_2122729045}

**OSPF \-- OSPF配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x4702_18917_1599048115}[命令用来配置引入外部路由时的缺省参数，包括]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[引入外部路由的开销、类型和标记。]{style="font-family:宋体"}

[**[undo default]{lang="EN-US"}**]{#struct_0_x4702_18917_x1977961515}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x358779656}

[**[default ]{lang="EN-US"}**[{ **cost** *cost* \| **tag** *tag* \| **type** *type* } \*]{lang="EN-US"}]{#struct_0_x4702_18917_2016420582}

[**[undo]{lang="EN-US"}[ default]{lang="EN-US"}**[ { **cost** \| **tag** \| **type** } \*]{lang="EN-US"}]{#struct_0_x4702_18917_366016800}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2127930962}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x261675504}[引入的外部路由的度量值为]{style="font-family:宋体"}[1]{lang="EN-US"}[，引入的外部路由的标记为]{style="font-family:宋体"}[1]{lang="EN-US"}[，引入的外部路由类型为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1193896077}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1599113651}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_722467519}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1993295014}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1761614730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x854628824}

[**[cost]{lang="EN-US"}***[ cost]{lang="EN-US"}*]{#struct_0_x4702_18917_47683489}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[引入的外部路由的缺省度量值，]{style="font-family:宋体"}*[cost]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_x4702_18917_x1196253547}[：外部路由的标记，]{style="font-family:宋体"}*[tag]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type ]{lang="EN-US"}***[type]{lang="EN-US"}*]{#struct_0_x4702_18917_1860840747}[：外部路由类型，]{style="font-family:宋体"}*[type]{lang="EN-US"}*[的取值]{style="font-family:宋体"}[范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_287658696}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1599179187}[配置外部路由开销、标记和类型的缺省值分别为]{style="font-family:宋体"}[10]{lang="EN-US"}[、]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x414171374}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] default cost 10 tag 100 type 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_238574970}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_x132629867}
:::

::: {#-1460079941 .myid}
[]{#_Toc404787992}[]{#struct_0_x4702_18917_931402516}[]{#_Toc138212541}[]{#_Toc93984770}[]{#_Toc61236306}[]{#_Toc61093053}[]{#_Toc58812030}[]{#_Toc56887159}[]{#_Toc45164774}

**OSPF \-- OSPF配置命令 \-- default-cost (OSPF area view)**

------------------------------------------------------------------------

[**[default-cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x1425506172}[命令用来配置发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销。]{style="font-family:宋体"}

[**[undo default-cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x172382953}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1924262745}

[**[default-cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x4702_18917_1599244723}

[**[undo default-cost]{lang="EN-US"}**]{#struct_0_x4702_18917_321137496}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x147927384}

[[发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_1085983412}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1346699697}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x744137458}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1217541698}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_34878038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1985475280}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599834547}

[*[cost]{lang="EN-US"}*]{#struct_0_x4702_18917_x72275436}[：发送到]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的缺省路由的开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x816566512}

[[该命令只有在]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_2017704885}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[或]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR/ASBR]{lang="EN-US"}[上配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1906035433}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2073914098}[将区域]{style="font-family:宋体"}[1]{lang="EN-US"}[设置成]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域，配置发送到该]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域的缺省路由的开销为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1008600672}

[\[Sysname\] ospf 100 ]{lang="EN-US"}

[\[Sysname-ospf-100\] area 1]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] stub]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] default-cost 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599900083}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nssa]{lang="EN-US"}**]{#struct_0_x4702_18917_707876749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[stub]{lang="EN-US"}**]{#struct_0_x4702_18917_1291674044}
:::

::: {#114692368 .myid}
[]{#_Toc404787993}[]{#struct_0_x4702_18917_1978542803}[]{#_Toc138212542}[]{#_Toc93984771}[]{#_Toc61236307}[]{#_Toc61093054}[]{#_Toc58812031}[]{#_Toc56887160}[]{#_Toc45164775}

**OSPF \-- OSPF配置命令 \-- default-route-advertise (OSPF view)**

------------------------------------------------------------------------

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_x10805862}[命令用来将缺省路由引入到]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由区域。]{style="font-family:宋体"}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_x158558888}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1038379190}

[**[default-route-advertise]{lang="EN-US"}**[ \[ \[ \[ **always** \| **permit-calculate-other** \] \| **cost** *cost* \| **route-policy** *route-policy-name* \| **type** *type* \] \* \| **summary cost** *cost* \]]{lang="EN-US"}]{#struct_0_x4702_18917_x697967161}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_580033314}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599310256}

[[没有引入缺省路由。]{style="font-family:宋体"}]{#struct_0_x4702_18917_1083791570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x98833485}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1033824518}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_54014745}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x950082023}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x666040207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x625991585}

[**[always]{lang="EN-US"}**]{#struct_0_x4702_18917_1201043039}[：]{style="font-family:宋体"}[如果当前路由器的路由表中没有缺省路由，使用此参数可产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[发布出去。如果没有指定该关键字，仅当本地路由器的路由表中存在缺省路由时，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[发布出去。]{style="font-family:宋体"}

[**[permit-calculate-other]{lang="EN-US"}**]{#struct_0_x4702_18917_1599375792}[：当路由器产生并发布了一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[时，指定此参数的路由器仍然会计算来自于其他路由器的缺省路由，未指定此参数的路由器不再计算来自其他路由器的缺省路由。当路由器没有产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[时，无论是否指定此参数，路由器都会计算来自其他路由器的缺省路由。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x4702_18917_1885124247}[：该缺省路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[，如果没有指定，缺省路由的度量值将取]{style="font-family:宋体"}**[default cost]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x4702_18917_x2062202429}[：路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[中的值。如果同时指定]{style="font-family:宋体"}**[always]{lang="EN-US"}**[参数，不论当前路由器的路由表中是否有缺省路由，只要有路由匹配指定的路由策略，就将产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[中的值。]{style="font-family:宋体"}

[**[type ]{lang="EN-US"}***[type]{lang="EN-US"}*]{#struct_0_x4702_18917_1681927163}[：]{style="font-family:宋体"}[该]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，如果没有指定，]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的缺省类型将取]{style="font-family:宋体"}**[default type]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x373238751}[：发布指定缺省路由的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[。在选用该参数时，必须首先使能]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，否则路由不能发布。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1712497408}

[[使用]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_x1803266449}[命令不能引入缺省路由，如果要引入缺省路由，必须使用该命令。当本地路由器的路由表中没有缺省路由时，要产生一个描述缺省路由的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[应使用]{style="font-family:宋体"}**[always]{lang="EN-US"}**[关键字。]{style="font-family:宋体"}

[**[default-route-advertise summary cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x276294815}[命令仅在]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中应用，以]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[引入缺省路由，]{style="font-family:宋体"}[PE]{lang="EN-US"}[路由器会将引入的缺省路由发布给]{style="font-family:宋体"}[CE]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599441328}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_325837711}[不管本地路由器的路由表中是否存在缺省路由，将产生的缺省路由引入到]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由区域（本地路由器没有缺省路由）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1863576562}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] default-route-advertise always]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2064584389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default]{lang="EN-US"}**]{#struct_0_x4702_18917_x886761006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_1730460072}
:::

::: {#850687879 .myid}
[]{#_Toc404787994}[]{#struct_0_x4702_18917_824734928}[]{#_Toc371422250}[]{#_Toc366565712}

**OSPF \-- OSPF配置命令 \-- discard-route**

------------------------------------------------------------------------

[**[discard-route]{lang="EN-US"}**]{#struct_0_x4702_18917_x1269467333}[命令用来配置]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由以及]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由的优先级。]{style="font-family:宋体"}

[**[undo discard-route]{lang="EN-US"}**]{#struct_0_x4702_18917_x1030971977}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_132517012}

[**[discard-route]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4702_18917_824800464}[{ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[external]{lang="EN-US"}**[ {]{lang="EN-US" style="font-size:10.0pt;color:black"}[ ]{lang="EN-US" style="font-size:10.0pt"}*[preference]{lang="EN-US"}*[ \| ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[suppression]{lang="EN-US"}**[ ]{lang="EN-US"}[}[ \| ]{style="color:black"}]{lang="EN-US" style="font-size:10.0pt"}**[internal]{lang="EN-US"}**[ { ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[preference]{lang="EN-US"}*[ \| ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[suppression]{lang="EN-US"}**[ ]{lang="EN-US"}[} }]{lang="EN-US" style="font-size:10.0pt;color:black"}[ \*]{lang="EN-US"}

[**[undo discard-route]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x4702_18917_967805687}[\[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[external]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[internal]{lang="EN-US"}**[ \] ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1615203895}

[[产生引入聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}]{#struct_0_x4702_18917_523478926}[路由和区域间聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由，且]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由优先级为]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1906428679}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1786963431}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_190710192}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1044670364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_565686193}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1340760564}

[**[external]{lang="EN-US"}**]{#struct_0_x4702_18917_824866000}[：引入聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[*[preference]{lang="EN-US"}*]{#struct_0_x4702_18917_141122845}[：引入聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_841132610}[：抑制产生引入聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_x4702_18917_73730117}[：区域间聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[*[preference]{lang="EN-US"}*]{#struct_0_x4702_18917_159887337}[：区域间聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x2003764774}[：抑制产生区域间聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1902762947}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x349357481}[配置引入聚合路由的]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，区域间聚合]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_825455824}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] discard-route external 100 internal 200]{lang="EN-US"}
:::

::: {#2106472467 .myid}
[]{#_Toc404787995}[]{#struct_0_x4702_18917_x181201771}[]{#_Toc138212543}[]{#_Toc92622983}

**OSPF \-- OSPF配置命令 \-- description (OSPF/OSPF area view)**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x4702_18917_x1704019748}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[/OSPF]{lang="EN-US"}[区域的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x4702_18917_1091980610}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1599506864}

[**[description]{lang="EN-US"}**[ *description*]{lang="EN-US"}]{#struct_0_x4702_18917_x895139523}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x4702_18917_470617133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_756515619}

[[没有配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_584971727}[进程和区域的描述信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1198910577}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1777358729}[视图]{style="font-family:宋体"}[/OSPF]{lang="EN-US"}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1300467791}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1599048112}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1978420267}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1976816336}

[*[description]{lang="EN-US"}*]{#struct_0_x4702_18917_525447251}[：在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[视图下，该参数用来描述]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程；在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域视图下，该参数用来描述]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1773065382}

[[本命令仅仅用于标识某]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x269596583}[进程]{style="font-family:宋体"}[/OSPF]{lang="EN-US"}[区域，并无特别的意义和用途。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1015930063}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2071659520}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[abc]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1599113648}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] description abc]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_723057344}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[0]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[bone area]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x2002620527}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 0]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.0\] description bone area]{lang="EN-US"}
:::

::: {#665688258 .myid}
[]{#_Toc138212544}[]{#_Toc404787996}[]{#struct_0_x4702_18917_x1602157935}[]{#_Toc138212546}[]{#_Toc93984774}[]{#_Toc61236310}

**OSPF \-- OSPF配置命令 \-- display ospf**

------------------------------------------------------------------------

[**[display ospf]{lang="EN-US"}**]{#struct_0_x4702_18917_x419574696}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的进程信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_309175539}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_878493352}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1766640127}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1103385479}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1804036883}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_120982808}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1854654402}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1599244720}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_321203032}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x687080287}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1533197315}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的进程信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x1511068342}[：显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1726506439}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1599834544}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1599310257}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.2]{lang="EN-US"}

[                  OSPF Protocol Information]{lang="EN-US"}

[ ]{lang="EN-US"}

[ RouterID: 192.168.1.2      Router type:  NSSA]{lang="EN-US"}

[ Route tag: 0]{lang="EN-US"}

[ Multi-VPN-Instance is not enabled]{lang="EN-US"}

[ Ext-community type: domain ID 0x105, route type 0x8000, router ID 0x8001]{lang="EN-US"}

[ Domain ID: 0.0.0.0:23]{lang="EN-US"}

[ Opaque capable]{lang="EN-US"}

[ Originating router-LSAs with maximum metric]{lang="EN-US"}

[    Condition: On startup while BGP is converging, State: Inactive]{lang="EN-US"}

[    Advertise stub links with maximum metric in router-LSAs]{lang="EN-US"}

[    Advertise summary-LSAs with metric 16711680]{lang="EN-US"}

[    Advertise external-LSAs with metric 16711680]{lang="EN-US"}

[ ISPF is enabled]{lang="EN-US"}

[ SPF-schedule-interval: 5 50 200]{lang="EN-US"}

[ LSA generation interval: 5]{lang="EN-US"}

[ LSA arrival interval: 1000]{lang="EN-US"}

[ Transmit pacing: Interval: 20 Count: 3]{lang="EN-US"}

[ Default ASE parameters: Metric: 1 Tag: 1 Type: 2]{lang="EN-US"}

[ Route preference: 10]{lang="EN-US"}

[ ASE route preference: 150]{lang="EN-US"}

[ SPF computation count: 22]{lang="EN-US"}

[ RFC 1583 compatible]{lang="EN-US"}

[ Graceful restart interval: 120]{lang="EN-US"}

[ SNMP trap rate limit interval: 2  Count: 300]{lang="EN-US"}

[ This process is currently bound to MIB]{lang="EN-US"}

[ Area count: 1   NSSA area count: 1]{lang="EN-US"}

[ Normal areas with up interfaces: 0]{lang="EN-US"}

[ NSSA areas with up interfaces: 1]{lang="EN-US"}

[ Up interfaces: 1]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ Full neighbors:3]{lang="EN-US"}

[ Calculation trigger type: Full]{lang="EN-US"}

[ Current calculation type: SPF calculation]{lang="EN-US"}

[ Current calculation phase: Calculation area topology]{lang="EN-US"}

[ Process reset state: N/A]{lang="EN-US"}

[ Current reset type: N/A]{lang="EN-US"}

[ Next reset type: N/A]{lang="EN-US"}

[ Reset prepare message replied: -/-/-/-]{lang="EN-US"}

[ Reset process message replied: -/-/-/-]{lang="EN-US"}

[ Reset phase of module]{lang="EN-US"}[：]{style="font-family:宋体"}

[   M-N/A, P-N/A, L-N/A, C-N/A, R-N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1          (MPLS TE  not enabled)]{lang="EN-US"}

[ Authtype: None    Area flag: NSSA]{lang="EN-US"}

[ 7/5 translator state: Disabled]{lang="EN-US"}

[ 7/5 translate stability timer interval: 0]{lang="EN-US"}

[ SPF scheduled count: 5]{lang="EN-US"}

[ ExChange/Loading neighbors: 0]{lang="EN-US"}

[ Up interfaces: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Interface: 192.168.1.2 (GigabitEthernet1/0/1)]{lang="EN-US"}

[ Cost: 1       State: DR        Type: Broadcast    MTU: 1500]{lang="EN-US"}

[ Priority: 1]{lang="EN-US"}

[ Designated router: 192.168.1.2]{lang="EN-US"}

[ Backup designated router: 192.168.1.1]{lang="EN-US"}

[ Timers: Hello 10 , Dead 40 , Poll  40 , Retransmit 5 , Transmit Delay 1]{lang="EN-US"}

[ FRR backup: Enabled]{lang="EN-US"}

[]{#_Toc94753855}[]{#_Toc94671181}[]{#_Toc73952258}[[ Enabled by network configuration]{lang="EN-US"}]{#_Toc68319391}

[[表1-1 ]{lang="EN-US"}[display ospf verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1083726034}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1904271097}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x75669430}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_766582878}

[[OSPF Process 1 with Router ID 192.168.1.2]{lang="EN-US"}]{#struct_0_x4702_18917_x2047764883}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1599375793}[进程号以及]{style="font-family:宋体"}[OSPF Router ID]{lang="EN-US"}

[[RouterID]{lang="EN-US"}]{#struct_0_x4702_18917_1885058711}

[[本路由器的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2021272935}[Router ID]{lang="FR"}

[[Router type]{lang="EN-US"}]{#struct_0_x4702_18917_x1439882303}

[[路由器类型，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_344533750}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_1880159212}[表示区域边界路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ASBR]{lang="EN-US"}]{#struct_0_x4702_18917_1599441329}[表示自治系统边界路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_325903247}[表示支持]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为空表示非上面三种情况]{style="font-family:宋体"}]{#struct_0_x4702_18917_312423250}

[[Route tag]{lang="EN-US"}]{#struct_0_x4702_18917_x531819438}

[[与外部路由相关联的标记]{style="font-family:宋体"}]{#struct_0_x4702_18917_1916736342}

[[Multi-VPN-Instance is not enabled]{lang="EN-US"}]{#struct_0_x4702_18917_1442573822}

[[当前进程不支持多]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x4702_18917_1599506865}[实例]{style="font-family:宋体"}

[[Ext-community type]{lang="EN-US"}]{#struct_0_x4702_18917_59360826}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_59426362}[扩展团体属性类型编码。其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[domain ID]{lang="EN-US"}]{#struct_0_x4702_18917_58836541}[代表]{style="font-family:宋体"}[domain ID]{lang="EN-US"}[属性编码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[route type]{lang="EN-US"}]{#struct_0_x4702_18917_58902077}[代表]{style="font-family:宋体"}[route type]{lang="EN-US"}[属性编码]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[router ID]{lang="EN-US"}]{#struct_0_x4702_18917_58967613}[代表]{style="font-family:宋体"}[router ID]{lang="EN-US"}[属性编码]{style="font-family:宋体"}

[[Domain ID]{lang="EN-US"}]{#struct_0_x4702_18917_59033149}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_58574397}[域标识符（主标识符）]{style="font-family:宋体"}

[[Opaque capable]{lang="EN-US"}]{#struct_0_x4702_18917_x895073987}

[[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1658177384}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力]{style="font-family:宋体"}

[[Originating router-LSAs with maximum metric]{lang="EN-US"}]{#struct_0_x4702_18917_1211757740}

[[Router LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1396996451}[中除]{style="font-family:宋体"}[Stublink]{lang="EN-US"}[外使用最大开销值发布]{style="font-family:宋体"}

[[Condition]{lang="EN-US"}]{#struct_0_x4702_18917_1599048113}

[[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x1978354731}[路由器的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Always]{lang="EN-US"}]{#struct_0_x4702_18917_205548894}[代表始终生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On startup while BGP is converging]{lang="EN-US"}]{#struct_0_x4702_18917_x2018787864}[代表]{style="font-family:宋体"}[BGP]{lang="EN-US"}[收敛前生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On startup while BGP is converging for XXX seconds]{lang="EN-US"}]{#struct_0_x4702_18917_1599113649}[代表]{style="font-family:宋体"}[BGP]{lang="EN-US"}[收敛超时时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[On startup for XXX seconds]{lang="EN-US"}]{#struct_0_x4702_18917_722991808}[代表重启后生效时间]{style="font-family:
  宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_1570160659}

[[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x1718209302}[路由器是否生效：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x4702_18917_x5718773}[表示生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x4702_18917_1599179185}[表示不生效]{style="font-family:宋体"}

[[Advertise stub links with maximum metric in router-LSAs]{lang="EN-US"}]{#struct_0_x4702_18917_x414040302}

[[Router LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1321545287}[使用最大开销值发布]{style="font-family:宋体"}

[[Advertise summary-LSAs with metric]{lang="EN-US"}]{#struct_0_x4702_18917_1738023128}

[[Summary LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1599244721}[发布使用的开销值]{style="font-family:宋体"}

[[Advertise external-LSAs with metric]{lang="EN-US"}]{#struct_0_x4702_18917_321268568}

[[外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_77486766}[发布使用的开销值]{style="font-family:宋体"}

[[ISPF is enabled]{lang="EN-US"}]{#struct_0_x4702_18917_x471369813}

[[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_1599834545}[计算功能]{style="font-family:宋体"}

[[SPF-schedule-interval]{lang="EN-US"}]{#struct_0_x4702_18917_x72144364}

[[进行]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1479188692}[计算的时间间隔]{style="font-family:宋体"}

[[LSA generation interval]{lang="EN-US"}]{#struct_0_x4702_18917_x1653194309}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1599900081}[生成时间间隔]{style="font-family:宋体"}

[[LSA arrival interval]{lang="EN-US"}]{#struct_0_x4702_18917_708007821}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1256241427}[重复到达的最小时间间隔]{style="font-family:宋体"}

[[Transmit pacing]{lang="EN-US"}]{#struct_0_x4702_18917_x1118588746}

[[接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_1599310254}[报文的速率，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Interval]{lang="EN-US"}]{#struct_0_x4702_18917_1083660498}[表示接口发送]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Count]{lang="EN-US"}]{#struct_0_x4702_18917_x482183369}[表示接口一次发送]{lang="EN-US" style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数]{lang="EN-US" style="font-family:宋体"}

[[Default ASE parameters]{lang="EN-US"}]{#struct_0_x4702_18917_1599375790}

[[引入外部路由的缺省参数值，其中：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1885255319}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Metric]{lang="EN-US"}]{#struct_0_x4702_18917_x1669677382}[代表度量值]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Tag]{lang="EN-US"}]{#struct_0_x4702_18917_x760143429}[代表路由标记]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1599441326}[代表路由类型]{lang="EN-US" style="font-family:宋体"}

[[Route preference]{lang="EN-US"}]{#struct_0_x4702_18917_326493071}

[[内部路由优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_1724729892}

[[ASE route preference]{lang="EN-US"}]{#struct_0_x4702_18917_1599506862}

[[外部路由优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_x895008451}

[[SPF computation count]{lang="EN-US"}]{#struct_0_x4702_18917_1241153636}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1599048110}[进程的路由计算总数]{style="font-family:宋体"}

[[RFC1583 compatible]{lang="EN-US"}]{#struct_0_x4702_18917_x1978289195}

[[兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}]{#struct_0_x4702_18917_1078006805}[路由选择优先规则]{style="font-family:宋体"}

[[Graceful restart interval]{lang="EN-US"}]{#struct_0_x4702_18917_1599113646}

[[GR]{lang="EN-US"}]{#struct_0_x4702_18917_722401984}[重启间隔时间]{style="font-family:宋体"}

[[SNMP trap rate limit interval]{lang="EN-US"}]{#struct_0_x4702_18917_1119826897}

[[TRAP]{lang="EN-US"}]{#struct_0_x4702_18917_1599179182}[发送间隔]{style="font-family:宋体"}

[[Count]{lang="EN-US"}]{#struct_0_x4702_18917_x414367982}

[[TRAP]{lang="EN-US"}]{#struct_0_x4702_18917_256263903}[发送个数]{style="font-family:宋体"}

[[This process is currently bound to MIB]{lang="EN-US"}]{#struct_0_x4702_18917_1599244718}

[[当前进程绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}]{#struct_0_x4702_18917_320678747}

[[Area count]{lang="EN-US"}]{#struct_0_x4702_18917_456096095}

[[当前进程中的区域数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1599834542}

[[NSSA area count]{lang="EN-US"}]{#struct_0_x4702_18917_x71947756}

[[当前进程中的]{style="font-family:宋体"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_1913210685}[区域数]{style="font-family:宋体"}

[[Normal areas with up interfaces]{lang="EN-US"}]{#struct_0_x4702_18917_1599900078}

[[有]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4702_18917_708466570}[接口的外部能力区域个数]{style="font-family:宋体"}

[[NSSA areas with up interfaces]{lang="EN-US"}]{#struct_0_x4702_18917_1599310255}

[[有]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4702_18917_1083594962}[接口的]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域个数]{style="font-family:宋体"}

[[Up interfaces]{lang="EN-US"}]{#struct_0_x4702_18917_1498958133}

[[处于]{style="font-family:宋体"}[Up]{lang="EN-US"}]{#struct_0_x4702_18917_1599375791}[状态的接口计数]{style="font-family:宋体"}

[[ExChange/Loading neighbors]{lang="EN-US"}]{#struct_0_x4702_18917_1885189783}

[[处于]{style="font-family:宋体"}[ExChange/Loading]{lang="EN-US"}]{#struct_0_x4702_18917_726943502}[状态的邻居数]{style="font-family:宋体"}

[[Full neighbors]{lang="EN-US"}]{#struct_0_x4702_18917_1599441327}

[[处于]{style="font-family:宋体"}[Full]{lang="EN-US"}]{#struct_0_x4702_18917_326558607}[状态的邻居数]{style="font-family:宋体"}

[[Calculation trigger type]{lang="EN-US"}]{#struct_0_x4702_18917_1599506863}

[[触发路由计算的类型，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x894942915}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full]{lang="EN-US"}]{#struct_0_x4702_18917_1599048111}[：触发全部路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Area topology change]{lang="EN-US"}]{#struct_0_x4702_18917_x1978223659}[：区域拓扑改变触发路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Intra router change]{lang="EN-US"}]{#struct_0_x4702_18917_x755404406}[：增量的区域内路由器路由变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ASBR change]{lang="EN-US"}]{#struct_0_x4702_18917_1599113647}[：增量的]{style="font-family:
  宋体"}[ASBR]{lang="EN-US"}[路由变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[7to5 translator]{lang="EN-US"}]{#struct_0_x4702_18917_722336448}[：]{style="font-family:宋体"}[7]{lang="EN-US"}[转]{style="font-family:宋体"}[5]{lang="EN-US"}[角色变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full IP prefix]{lang="EN-US"}]{#struct_0_x4702_18917_1599179183}[：触发全部]{style="font-family:宋体"}[IP]{lang="EN-US"}[前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_x414433518}[：触发全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_214398155}[：触发增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_1599244719}[：触发全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_320744283}[：触发增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_1599834543}[：未触发计算]{style="font-family:宋体"}

[[Current calculation type]{lang="EN-US"}]{#struct_0_x4702_18917_x72013292}

[[当前路由计算的类型，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1599900079}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[SPF calculation]{lang="EN-US"}]{#struct_0_x4702_18917_708532106}[：进行区域]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Intra router calculation]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573097}[：区域内路由器路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ASBR calculation]{lang="EN-US"}]{#struct_0_x4702_18917_317040145}[：区域间]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc intra router]{lang="EN-US"}]{#struct_0_x4702_18917_500021361}[：增量区域内路由器路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc ASBR calculation]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507561}[：增量区域间]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[7to5 translator]{lang="EN-US"}]{#struct_0_x4702_18917_x1500439509}[：]{style="font-family:宋体"}[7]{lang="EN-US"}[转]{style="font-family:宋体"}[5]{lang="EN-US"}[角色路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442025}[：进行全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Inc intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_x134803834}[：进行增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[内部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Full inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1129376489}[：进行全部]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inc inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_548144775}[：进行增量]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[外部前缀计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Forward address]{lang="EN-US"}]{#struct_0_x4702_18917_x1129835241}[：转发地址计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_875971013}[：未触发计算]{style="font-family:宋体"}

[[Current calculation phase]{lang="EN-US"}]{#struct_0_x4702_18917_x1129769705}

[[当前路由计算调度运行到的阶段，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1350631051}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation area topology]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704169}[：计算区域拓扑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation router]{lang="EN-US"}]{#struct_0_x4702_18917_x738475769}[：计算路由器路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1129638633}[：计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[7to5 translator]{lang="EN-US"}]{#struct_0_x4702_18917_395532427}[：计算]{style="font-family:宋体"}[7]{lang="EN-US"}[转]{style="font-family:宋体"}[5]{lang="EN-US"}[角色路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Forward address]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048809}[：计算转发地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1468950710}[：计算]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Calculation end]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983273}[：计算收尾阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x41323791}[：未触发计算]{style="font-family:宋体"}

[[Process reset state]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573096}

[[进程重启状态状态，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1249043796}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507560}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Under reset]{lang="EN-US"}]{#struct_0_x4702_18917_65644432}[：进程重启过程中]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under RIB smooth]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442024}[：进程正在同步]{style="font-family:宋体"}[RIB]{lang="EN-US"}[路由]{style="font-family:宋体"}

[[Current reset type]{lang="EN-US"}]{#struct_0_x4702_18917_1431280107}

[[当前进程重启类型，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1129376488}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1017939166}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_x1129835240}[：普通重启]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[GR quit]{lang="EN-US"}]{#struct_0_x4702_18917_x690112928}[：]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[异常退出进行普通重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x4702_18917_x1129769704}[：删除]{style="font-family:
  宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VPN delete]{lang="EN-US"}]{#struct_0_x4702_18917_x1378252304}[：删除]{style="font-family:
  宋体"}[VPN]{lang="EN-US"}

[[Next reset type]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704168}

[[即将调度进程重启类型，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1129638632}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1170551514}[：进程未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048808}[：普通重启]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[GR quit]{lang="EN-US"}]{#struct_0_x4702_18917_97133231}[：]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[异常退出进行普通重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983272}[：删除]{style="font-family:
  宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VPN delete]{lang="EN-US"}]{#struct_0_x4702_18917_1524760150}[：删除]{style="font-family:
  宋体"}[VPN ]{lang="EN-US"}

[[Reset prepare message replied]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573099}

[[响应准备重启消息的模块，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x133298549}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507563}[代表邻居维护模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442027}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x4702_18917_x1297603248}[代表路由计算模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x4702_18917_x1129376491}[代表路由引入模块]{style="font-family:宋体"}

[[Reset process message replied]{lang="EN-US"}]{#struct_0_x4702_18917_191848879}

[[响应进程重启消息的模块，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1129835243}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_x1129769707}[代表邻居维护模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x4702_18917_x1781536831}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704171}[代表路由计算模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x4702_18917_x1094771665}[代表路由引入模块]{style="font-family:宋体"}

[[Reset phase of module]{lang="EN-US"}]{#struct_0_x4702_18917_x1129638635}

[[各模块所处重启阶段。其中]{style="font-family:宋体"}[M]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048811}[代表主控制模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1112654814}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete area]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983275}[：删除区域]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete process]{lang="EN-US"}]{#struct_0_x4702_18917_x1204123205}[：删除进程]{style="font-family:宋体"}

[[P]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573098}[代表邻居维护模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507562}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete neighbor]{lang="EN-US"}]{#struct_0_x4702_18917_x1097154982}[：删除邻居]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442026}[：删除接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete vlink]{lang="EN-US"}]{#struct_0_x4702_18917_268480693}[：删除虚连接]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete shamlink]{lang="EN-US"}]{#struct_0_x4702_18917_x1129376490}[：删除伪连接]{style="font-family:宋体"}

[[L]{lang="EN-US"}]{#struct_0_x4702_18917_x1129835242}[代表]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1852912342}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Stop timer]{lang="EN-US"}]{#struct_0_x4702_18917_x1129769706}[：停止计时器]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete ASE]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704170}[：删除所有]{style="font-family:
  宋体"}[ASE LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete ASE maps]{lang="EN-US"}]{#struct_0_x4702_18917_471312276}[：删除]{style="font-family:宋体"}[ASE LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[map]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Clear process data]{lang="EN-US"}]{#struct_0_x4702_18917_x1129638634}[：清除进程数据]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete area LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048810}[：删除区域相关]{style="font-family:宋体"}[LSA]{lang="EN-US"}[及其]{style="font-family:宋体"}[map]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Delete area interface]{lang="EN-US"}]{#struct_0_x4702_18917_453429127}[：删除区域下接口]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete process]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983274}[：删除进程相关资源]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Restart]{lang="EN-US"}]{#struct_0_x4702_18917_361960736}[：重启进程相关资源]{style="font-family:
  宋体"}

[[C]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573101}[代表路由计算模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507565}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete topology]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442029}[：删除区域拓扑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete router]{lang="EN-US"}]{#struct_0_x4702_18917_1478334274}[：删除路由器路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete intra AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1129376493}[：删除]{style="font-family:宋体"}[AS]{lang="EN-US"}[内部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete inter AS]{lang="EN-US"}]{#struct_0_x4702_18917_x1129835245}[：删除]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete forward address]{lang="EN-US"}]{#struct_0_x4702_18917_x1093397455}[：删除转发地址列表]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete advertise]{lang="EN-US"}]{#struct_0_x4702_18917_x1129769709}[：删除发布源列表]{style="font-family:宋体"}

[[R]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704173}[代表路由引入模块，其阶段有：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x4702_18917_2037396217}[：未重启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete ABR summary]{lang="EN-US"}]{#struct_0_x4702_18917_x1129638637}[：删除]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete ASBR summary]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048813}[：删除]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete import]{lang="EN-US"}]{#struct_0_x4702_18917_2019513068}[：删除引入路由]{style="font-family:宋体"}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983277}

[[开始列举当前进程中各区域的信息。显示当前区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1129573100}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式]{style="font-family:宋体"}

[[Authtype]{lang="EN-US"}]{#struct_0_x4702_18917_x1129507564}

[[区域验证模式，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_2035012900}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x4702_18917_x1129442028}[表示无验证]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_x4702_18917_x1129376492}[表示简单验证模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x1129835244}[表示]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式]{style="font-family:宋体"}

[[Area flag]{lang="EN-US"}]{#struct_0_x4702_18917_1635485900}

[[区域类型：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1129769708}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x4702_18917_x1129704172}[rmal]{lang="EN-US"}[：普通区域]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x691487138}[：]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StubNoSummary]{lang="EN-US"}]{#struct_0_x4702_18917_x1129638636}[：完全]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1129048812}[：]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSANoSummary]{lang="EN-US"}]{#struct_0_x4702_18917_x709370287}[：完全]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[7/5 translator state]{lang="EN-US"}]{#struct_0_x4702_18917_x1128983276}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1232397530}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者状态，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4702_18917_1232331994}[表示通过命令指定]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Elected]{lang="EN-US"}]{#struct_0_x4702_18917_1232528602}[表示通过选举指定]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_579320144}[表示不是]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换者]{lang="EN-US" style="font-family:宋体"}

[[7/5 translate stability timer interval]{lang="EN-US"}]{#struct_0_x4702_18917_1232463066}

[[Type-7 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1232659674}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[转换稳定定时器超时时间间隔]{style="font-family:宋体"}

[[SPF scheduled Count]{lang="EN-US"}]{#struct_0_x4702_18917_1232594138}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1232790746}[区域的路由计算总数]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1756621634}

[[区域内的接口信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232725210}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_1232921818}

[[接口的开销值]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232856282}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_1232397531}

[[接口状态]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1735739536}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1232331995}

[[接口的网络类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232528603}

[[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_1232463067}

[[接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_1232659675}[值]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x4702_18917_1232594139}

[[路由器优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_595542539}

[[Designated router]{lang="EN-US"}]{#struct_0_x4702_18917_1232790747}

[[接口所属网段的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_1232725211}

[[Backup designated router]{lang="EN-US"}]{#struct_0_x4702_18917_1232921819}

[[接口所属网段的]{style="font-family:宋体"}[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_1232856283}

[[Timers]{lang="EN-US"}]{#struct_0_x4702_18917_1232397528}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1735280785}[定时器的值，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_1232331992}[表示接口发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dead]{lang="EN-US"}]{#struct_0_x4702_18917_1232528600}[表示邻居的失效时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Poll]{lang="EN-US"}]{#struct_0_x4702_18917_1232463064}[表示接口发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Retransmit]{lang="EN-US"}]{#struct_0_x4702_18917_1232659672}[表示定接口重传]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[时间间隔]{lang="EN-US" style="font-family:宋体"}

[[Transmit Delay]{lang="EN-US"}]{#struct_0_x4702_18917_1232594136}

[[接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1232790744}[的传输延迟时间]{style="font-family:宋体"}

[[FRR backup]{lang="EN-US"}]{#struct_0_x4702_18917_x1756490562}

[[是否使能接口参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x4702_18917_1232725208}[（]{style="font-family:宋体"}[Loop Free Alternate]{lang="EN-US"}[）计算：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4702_18917_1232921816}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_1232856280}[：关闭]{style="font-family:宋体"}

[[Enabled by network configuration]{lang="EN-US"}]{#struct_0_x4702_18917_1232397529}

[[接口由网络配置使能到该区域]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232331993}

[ ]{lang="EN-US"}

::: {#1006842224 .myid}
[]{#_Toc404787997}[]{#struct_0_x4702_18917_x1315856228}

**OSPF \-- OSPF配置命令 \-- display ospf abr-asbr**

------------------------------------------------------------------------

[**[display ospf abr-asbr]{lang="EN-US"}**]{#struct_0_x4702_18917_x1057007244}[命令用来显示到]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的区域边界路由器和自治系统边界路由器的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x50839321}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **abr-asbr** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_1521843332}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232528601}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_579385680}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x948949130}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1699228453}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x341789669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_2007444194}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1019931218}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_590516068}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1232463065}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程下到区域边界路由器和自治系统边界路由器的路由信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x969504464}[：显示详细信息。如果未指定本参数，将显示概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1655114861}

[[如果在]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_201849177}[区域的路由器上执行此命令，不显示有关]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_604406924}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2112110528}[显示到]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的区域边界路由器和自治系统边界路由器的路由概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf abr-asbr]{lang="EN-US"}]{#struct_0_x4702_18917_1232659673}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.112]{lang="EN-US"}

[                  Routing Table to ABR and ASBR]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Type    Destination     Area            Cost     Nexthop         RtType]{lang="EN-US"}

[ Inter   3.3.3.3         0.0.0.0         3124     10.1.1.2        ASBR]{lang="EN-US"}

[ Intra   2.2.2.2         0.0.0.0         1562     10.1.1.2        ABR]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2130461967}[显示到]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的区域边界路由器和自治系统边界路由器的路由详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf abr-asbr verbose]{lang="EN-US"}]{#struct_0_x4702_18917_x1657039743}

[ ]{lang="EN-US"}

[          OSPF Process 10 with Router ID 101.1.1.11]{lang="EN-US"}

[                  Routing Table to ABR and ASBR]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 1.1.1.1             RtType     : ASBR]{lang="EN-US"}

[ Area       : 0.0.0.1             Type       : Intra]{lang="EN-US"}

[ Nexthop    : 150.0.1.12          BkNexthop  : 0.0.0.0]{lang="EN-US"}

[ Interface  : GE1/0/1             BkInterface: N/A]{lang="EN-US"}

[ Cost       : 1000]{lang="EN-US"}

[]{#struct_0_x4702_18917_503521362}[]{#_Toc94753853}[]{#_Toc94671179}[]{#_Toc73952256}[[表1-2 ]{lang="EN-US"}[display ospf abr-asbr]{lang="EN-US"}]{#_Toc68319389}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1918298429}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1375697138}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x722633783}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1232594137}

[[到]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_595149323}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由类型，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra]{lang="EN-US"}]{#struct_0_x4702_18917_2067445441}[表示区域内路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inter]{lang="EN-US"}]{#struct_0_x4702_18917_181046994}[表示区域间路由]{lang="EN-US" style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_x4702_18917_x319212326}

[[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_x534452029}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_1232790745}

[[下一跳地址所在的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1756425026}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_958438529}

[[从本路由器到达]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_x1889149782}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销]{style="font-family:宋体"}

[[Nexthop]{lang="EN-US"}]{#struct_0_x4702_18917_x752643235}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_600937720}

[[BkNexthop]{lang="EN-US"}]{#struct_0_x4702_18917_1232725209}

[[备份下一跳地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_227790259}

[[RtType]{lang="EN-US"}]{#struct_0_x4702_18917_x587526038}

[[路由器类型，包括]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_x27513343}[和]{style="font-family:宋体"}[ASBR]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1376458955}

[[路由出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1376393419}

[[BkInterface]{lang="EN-US"}]{#struct_0_x4702_18917_x2123427979}

[[路由备份出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1376983242}

[ ]{lang="EN-US"}

::: {#1420562353 .myid}
[]{#_Toc138212545}[]{#_Toc93984773}[]{#_Toc61236309}[]{#_Toc61093058}[]{#_Toc58812033}[]{#_Toc56887162}[]{#_Toc45164777}[]{#_Toc404787998}[]{#struct_0_x4702_18917_290289302}[]{#_Toc340827293}[]{#_Toc339959824}

**OSPF \-- OSPF配置命令 \-- display ospf abr-summary**

------------------------------------------------------------------------

[**[display ospf abr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_1232921817}[命令用来显示]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_642359130}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] \[ **area** *area-id* \] **abr-summary** \[ *ip-address* { *mask-length* \| *mask* } \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x71857615}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_710130614}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1150225603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1343913864}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x380711402}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x681002584}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1232856281}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x189846811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1921962333}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_209715129}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**]{#struct_0_x4702_18917_1779226423}*[ area-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合相关信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将显示所有区域的信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x116657944}[：指定的聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4702_18917_580011902}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4702_18917_x1254544328}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x1707366703}[：显示]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合的概要信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232397526}

[[如果未指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1735674001}[地址和掩码，将显示所有的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x385738275}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1304059852}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospf abr-summary]{lang="EN-US"}]{#struct_0_x4702_18917_x1991259249}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[                  ABR Summary Addresses]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Area: 0.0.0.1]{lang="EN-US"}

[ Total summary addresses: 1]{lang="EN-US"}

[ Net             Mask            Status        Count      Cost]{lang="EN-US"}

[ 100.0.0.0       255.0.0.0       Advertise     1          (Not Configured)]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ospf abr-summary]{lang="EN-US"}]{#struct_0_x4702_18917_2055385951}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1919163379}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232331990}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1316052836}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x768631235}

[[聚合路由所在的区域]{style="font-family:宋体"}]{#struct_0_x4702_18917_1707054623}

[[Total summary addresses]{lang="EN-US"}]{#struct_0_x4702_18917_1569388119}

[[聚合路由的路由数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1873784597}

[[Net]{lang="EN-US"}]{#struct_0_x4702_18917_1232528598}

[[聚合路由的网络地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1759725223}

[[Mask]{lang="EN-US"}]{#struct_0_x4702_18917_553122419}

[[聚合路由的网络掩码]{style="font-family:宋体"}]{#struct_0_x4702_18917_396833269}

[[Status]{lang="EN-US"}]{#struct_0_x4702_18917_315765800}

[[聚合路由的状态：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1913700777}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Advertise]{lang="EN-US"}]{#struct_0_x4702_18917_1232463062}[：已发布]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Not-Advertise]{lang="EN-US"}]{#struct_0_x4702_18917_x969307856}[：未发布]{style="font-family:宋体"}

[[Count]{lang="EN-US"}]{#struct_0_x4702_18917_235491621}

[[被聚合的路由数]{style="font-family:宋体"}]{#struct_0_x4702_18917_795827108}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_x851274058}

[[聚合路由的开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232659670}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2130527503}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf abr-summary verbose]{lang="EN-US"}]{#struct_0_x4702_18917_x2046776596}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[                  ABR Summary Addresses]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Area: 0.0.0.1]{lang="EN-US"}

[ Total summary addresses: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Net         : 100.0.0.0]{lang="EN-US"}

[ Mask        : 255.0.0.0]{lang="EN-US"}

[ Status      : Advertise]{lang="EN-US"}

[ Cost        : (Not Configured)]{lang="EN-US"}

[ Routes count: 1]{lang="EN-US"}

[   Destination            NetMask                 Metric]{lang="EN-US"}

[   100.1.1.0              255.255.255.0           1000]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ospf [abr-summary]{style="color:black"}[ ]{style="color:red"}verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1524865323}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1915834025}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232594134}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_595214859}

[[Destination]{lang="EN-US"}]{#struct_0_x4702_18917_x1622951729}

[[被聚合路由的网络地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_1332256454}

[[NetMask]{lang="EN-US"}]{#struct_0_x4702_18917_x1533465558}

[[被聚合路由的网络掩码]{style="font-family:宋体"}]{#struct_0_x4702_18917_x611567308}

[[Metric]{lang="EN-US"}]{#struct_0_x4702_18917_1899317016}

[[路由的开销值]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232790742}

[ ]{lang="EN-US"}

::: {#-1664097566 .myid}
[]{#_Toc404787999}[]{#struct_0_x4702_18917_x1756883778}

**OSPF \-- OSPF配置命令 \-- display ospf asbr-summary**

------------------------------------------------------------------------

[**[display ospf asbr-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x2115785426}[命令用来显示]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_210053961}

[**[display ospf ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[\]]{lang="EN-US"}**[ asbr-summary]{lang="EN-US"}**[ \[ *ip-address* { *mask-length* \| *mask* } \]]{lang="EN-US"}]{#struct_0_x4702_18917_1181888766}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x511389288}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x967179632}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1705898115}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1232725206}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_228511155}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_44556070}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x819993478}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1193839316}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x2008506667}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_881606980}[：指定的聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4702_18917_x1854517525}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4702_18917_1232921814}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_642555738}

[[如果未指定]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x176250637}[地址和掩码，将显示所有的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1636893146}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1606256817}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[聚合信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 asbr-summary]{lang="EN-US"}]{#struct_0_x4702_18917_1232856278}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[                  Summary Addresses]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total Summary Address Count: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Summary Address]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Net         : 30.1.0.0]{lang="EN-US"}

[ Mask        : 255.255.0.0]{lang="EN-US"}

[ Tag         : 20]{lang="EN-US"}

[ Status      : Advertise]{lang="EN-US"}

[ Cost        : 10 (Configured)]{lang="EN-US"}

[ The Count of Route is : 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination     Net Mask        Proto      Process   Type     Metric]{lang="EN-US"}

[ ]{lang="EN-US"}

[ 30.1.2.0        255.255.255.0   OSPF       2         2        1]{lang="EN-US"}

[ 30.1.1.0        255.255.255.0   OSPF       2         2        1]{lang="EN-US"}

[]{#struct_0_x4702_18917_x189388062}[]{#_Toc94753854}[]{#_Toc94671180}[]{#_Toc73952257}[[表1-5 ]{lang="EN-US"}[display ospf asbr-summary]{lang="EN-US"}]{#_Toc68319390}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1915315869}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x684220489}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1409399745}

[[Total Summary Address Count]{lang="EN-US"}]{#struct_0_x4702_18917_14868121}

[[聚合路由的路由数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232397527}

[[Net]{lang="EN-US"}]{#struct_0_x4702_18917_x1735608465}

[[聚合路由的网络地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_x660572828}

[[Mask]{lang="EN-US"}]{#struct_0_x4702_18917_2118191708}

[[聚合路由的网络掩码]{style="font-family:宋体"}]{#struct_0_x4702_18917_389776296}

[[Tag]{lang="EN-US"}]{#struct_0_x4702_18917_x881367270}

[[聚合路由的标记字段]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232331991}

[[Status]{lang="EN-US"}]{#struct_0_x4702_18917_x1315987300}

[[聚合路由的发布状态]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1695764548}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_851990901}

[[聚合路由的开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_72896530}

[[The Count of Route]{lang="EN-US"}]{#struct_0_x4702_18917_1232528599}

[[被聚合的路由数]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1759790759}

[[Destination]{lang="EN-US"}]{#struct_0_x4702_18917_x550879061}

[[被聚合路由的网络地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_1627464519}

[[Net Mask]{lang="EN-US"}]{#struct_0_x4702_18917_x790208272}

[[被聚合路由的网络掩码]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232463063}

[[Proto]{lang="EN-US"}]{#struct_0_x4702_18917_x969373392}

[[引入路由的协议类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1281261891}

[[Process]{lang="EN-US"}]{#struct_0_x4702_18917_x387110867}

[[引入路由的协议进程号]{style="font-family:宋体"}]{#struct_0_x4702_18917_471155809}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1232659671}

[[外部路由类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_2130593039}

[[Metric]{lang="EN-US"}]{#struct_0_x4702_18917_x1322877611}

[[路由的开销值]{style="font-family:宋体"}]{#struct_0_x4702_18917_x118796432}

[ ]{lang="EN-US"}

::: {#-1451187516 .myid}
[]{#_Toc138212549}[]{#_Toc93984777}[]{#_Toc61236313}[]{#_Toc307238195}[]{#_Toc404788000}[]{#struct_0_x4702_18917_1963046095}[]{#_Toc332297385}[]{#_Toc351474182}[]{#_Toc352750745}[]{#_Toc351474183}[]{#_Toc352750746}[]{#_Toc351474184}[]{#_Toc352750747}[]{#_Toc351474185}[]{#_Toc352750748}[]{#_Toc351474186}[]{#_Toc352750749}[]{#_Toc351474187}[]{#_Toc352750750}[]{#_Toc351474188}[]{#_Toc352750751}[]{#_Toc351474189}[]{#_Toc352750752}[]{#_Toc351474190}[]{#_Toc352750753}[]{#_Toc351474191}[]{#_Toc352750754}[]{#_Toc351474192}[]{#_Toc352750755}[]{#_Toc351474193}[]{#_Toc352750756}[]{#_Toc351474194}[]{#_Toc352750757}[]{#_Toc351474195}[]{#_Toc352750758}[]{#_Toc351474196}[]{#_Toc352750759}[]{#_Toc351474197}[]{#_Toc352750760}[]{#_Toc351474198}[]{#_Toc352750761}[]{#_Toc351474199}[]{#_Toc352750762}[]{#_Toc351474200}[]{#_Toc352750763}[]{#_Toc351474201}[]{#_Toc352750764}[]{#_Toc351474202}[]{#_Toc352750765}[]{#_Toc351474203}[]{#_Toc352750766}[]{#_Toc351474204}[]{#_Toc352750767}[]{#_Toc351474205}[]{#_Toc352750768}[]{#_Toc351474206}[]{#_Toc352750769}[]{#_Toc351474207}[]{#_Toc352750770}[]{#_Toc351474208}[]{#_Toc352750771}[]{#_Toc351474209}[]{#_Toc352750772}[]{#_Toc351474210}[]{#_Toc352750773}[]{#_Toc351474211}[]{#_Toc352750774}[]{#_Toc351474212}[]{#_Toc352750775}[]{#_Toc351474213}[]{#_Toc352750776}[]{#_Toc351474214}[]{#_Toc352750777}[]{#_Toc351474215}[]{#_Toc352750778}[]{#_Toc351474216}[]{#_Toc352750779}[]{#_Toc351474217}[]{#_Toc352750780}[]{#_Toc351474218}[]{#_Toc352750781}[]{#_Toc351474219}[]{#_Toc352750782}[]{#_Toc351474220}[]{#_Toc352750783}[]{#_Toc351474221}[]{#_Toc352750784}[]{#_Toc351474222}[]{#_Toc352750785}[]{#_Toc351474223}[]{#_Toc352750786}[]{#_Toc351474224}[]{#_Toc352750787}[]{#_Toc351474225}[]{#_Toc352750788}[]{#_Toc351474304}[]{#_Toc352750867}[]{#_Toc351474305}[]{#_Toc352750868}[]{#_Toc351474306}[]{#_Toc352750869}[]{#_Toc351474307}[]{#_Toc352750870}[]{#_Toc351474308}[]{#_Toc352750871}[]{#_Toc351474309}[]{#_Toc352750872}[]{#_Toc351474310}[]{#_Toc352750873}[]{#_Toc351474311}[]{#_Toc352750874}[]{#_Toc351474312}[]{#_Toc352750875}[]{#_Toc351474313}[]{#_Toc352750876}[]{#_Toc351474314}[]{#_Toc352750877}[]{#_Toc351474315}[]{#_Toc352750878}[]{#_Toc351474316}[]{#_Toc352750879}[]{#_Toc351474317}[]{#_Toc352750880}[]{#_Toc351474318}[]{#_Toc352750881}[]{#_Toc351474319}[]{#_Toc352750882}[]{#_Toc351474320}[]{#_Toc352750883}[]{#_Toc351474321}[]{#_Toc352750884}[]{#_Toc351474322}[]{#_Toc352750885}[]{#_Toc351474323}[]{#_Toc352750886}[]{#_Toc351474324}[]{#_Toc352750887}[]{#_Toc351474325}[]{#_Toc352750888}[]{#_Toc351474326}[]{#_Toc352750889}[]{#_Toc351474327}[]{#_Toc352750890}[]{#_Toc351474328}[]{#_Toc352750891}[]{#_Toc351474329}[]{#_Toc352750892}[]{#_Toc351474330}[]{#_Toc352750893}[]{#_Toc351474331}[]{#_Toc352750894}[]{#_Toc351474332}[]{#_Toc352750895}[]{#_Toc351474333}[]{#_Toc352750896}[]{#_Toc351474334}[]{#_Toc352750897}[]{#_Toc351474335}[]{#_Toc352750898}[]{#_Toc351474336}[]{#_Toc352750899}[]{#_Toc351474337}[]{#_Toc352750900}[]{#_Toc351474338}[]{#_Toc352750901}[]{#_Toc351474339}[]{#_Toc352750902}[]{#_Toc351474427}[]{#_Toc352750990}

**OSPF \-- OSPF配置命令 \-- display ospf event-log**

------------------------------------------------------------------------

[**[display ospf event-log]{lang="EN-US"}**]{#struct_0_x4702_18917_x868282523}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1036645930}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **event-log** { **lsa-flush** \| **peer** \| **spf** }]{lang="EN-US"}]{#struct_0_x4702_18917_x1002193208}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_969697194}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1780286214}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2126683926}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1232790743}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1756818242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1757564966}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x2011344385}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x642114612}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_314326621}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有进程的日志信息。]{style="font-family:宋体"}

[**[lsa-flush]{lang="EN-US"}**]{#struct_0_x4702_18917_x1903755213}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[老化的日志信息。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_x4702_18917_1624920479}[：邻居的日志信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_x4702_18917_1624986015}[：]{style="font-family:宋体"}[路由计算的]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_148668271}

[[路由计算的]{style="font-family:宋体"}]{#struct_0_x4702_18917_534089209}[日志]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[是指更新到]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表的路由计数信息。]{style="font-family:宋体"}

[[邻居的日志信息包括]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1907144319}[邻居状态倒退到]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[，以及收到]{style="font-family:宋体"}[BadLSReq]{lang="EN-US"}[、]{style="font-family:宋体"}[SeqNumberMismatch]{lang="EN-US"}[和]{style="font-family:宋体"}[1-Way]{lang="EN-US"}[事件导致邻居状态倒退的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1646938155}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1904213965}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[LSA ]{lang="EN-US"}[老化日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf event-log lsa-flush]{lang="EN-US"}]{#struct_0_x4702_18917_x1904148429}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[                  LSA Flush Log]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Date: 2013-09-22 Time: 14:47:33 Received MaxAge LSA from 10.1.1.1]{lang="EN-US"}

[ Type: 1   LSID: 2.2.2.2         AdvRtr: 2.2.2.2           Seq#: 80000001]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Date: 2013-09-22 Time: 14:47:33 Flushed]{lang="EN-US"}[ MaxAge LSA]{lang="EN-US"}[ by the self]{lang="EN-US"}

[ Type: 1   LSID: 1.1.1.1         AdvRtr: 1.1.1.1           Seq#: 80000001]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Date: 2013-09-22 Time: 14:47:33 Received]{lang="EN-US"}[ MaxAge LSA]{lang="EN-US"}[ from 10.1.2.2]{lang="EN-US"}

[ Type: 1   LSID: 2.2.2.2         AdvRtr: 2.2.2.2           Seq#: 80000001]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Date: 2013-09-22 Time: 14:47:33 Flushed]{lang="EN-US"}[ MaxAge LSA]{lang="EN-US"}[ by the self]{lang="EN-US"}

[ Type: 1   LSID: 1.1.1.1         AdvRtr: 1.1.1.1           Seq#: 80000001]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ospf lsdb lsa-flush]{lang="EN-US"}]{#struct_0_x4702_18917_230280153}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1052141729}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x625440001}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_72155479}

[[Date &Time]{lang="EN-US"}]{#struct_0_x4702_18917_x1904082893}

[[收到]{style="font-family:宋体"}[MaxAge LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1032548715}[的时间]{style="font-family:宋体"}

[[Received MaxAge LSA from X.X.X.X]{lang="EN-US"}]{#struct_0_x4702_18917_x1247430319}

[[从源地址收到]{style="font-family:宋体"}[MaxAge LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x118703133}

[[Flushed MaxAge LSA by the self]{lang="EN-US"}]{#struct_0_x4702_18917_x1904017357}

[[由自己发起老化，洪泛]{style="font-family:宋体"}[MaxAge LSA]{lang="EN-US"}]{#struct_0_x4702_18917_729192779}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x331893596}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1903427533}[类型]{style="font-family:宋体"}

[[LSID]{lang="EN-US"}]{#struct_0_x4702_18917_x1390382251}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x612228203}[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[AdvRtr]{lang="EN-US"}]{#struct_0_x4702_18917_x1903361997}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1851600303}[发布路由器]{style="font-family:宋体"}

[[Seg#]{lang="EN-US"}]{#struct_0_x4702_18917_x1419502409}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1903951818}[序列号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1232725207}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf event-log spf]{lang="EN-US"}]{#struct_0_x4702_18917_228445619}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.2]{lang="EN-US"}

[                  SPF log]{lang="EN-US"}

[ ]{lang="EN-US"}

[Date       Time     Duration   Intra Inter External Reason]{lang="EN-US"}

[2012-06-27 15:28:26 0.95       1     1     10000    Intra-area LSA]{lang="EN-US"}

[2012-06-27 15:28:23 0.2        0     0     0        Area 0 full neighbor]{lang="EN-US"}

[2012-06-27 15:28:19 0          0     0     0        Intra-area LSA]{lang="EN-US"}

[2012-06-27 15:28:19 0          0     0     0        external LSA]{lang="EN-US"}

[2012-06-27 15:28:19 0.3        0     0     0        Intra-area LSA]{lang="EN-US"}

[2012-06-27 15:28:12 0          1     0     0        Intra-area LSA]{lang="EN-US"}

[2012-06-27 15:28:11 0          0     0     0        Routing policy]{lang="EN-US"}

[2012-06-27 15:28:11 0          0     0     0        Intra-area LSA]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display ospf event-log spf]{lang="EN-US"}]{#struct_0_x4702_18917_1598444708}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1939016955}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x845665644}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232921815}

[[Date/Time]{lang="EN-US"}]{#struct_0_x4702_18917_642490202}

[[路由计算开始的时间]{style="font-family:宋体"}]{#struct_0_x4702_18917_581959734}

[[Duration]{lang="EN-US"}]{#struct_0_x4702_18917_x60397275}

[[路由计算持续时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x4702_18917_1265961099}

[[Intra]{lang="EN-US"}]{#struct_0_x4702_18917_x1785542839}

[[区域内路由变化的个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1232856279}

[[Inter]{lang="EN-US"}]{#struct_0_x4702_18917_x189322526}

[[区域间路由变化的个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_x277521579}

[[External]{lang="EN-US"}]{#struct_0_x4702_18917_x177369656}

[[外部路由变化的个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1348004016}

[[Reason]{lang="EN-US"}]{#struct_0_x4702_18917_1908568425}

[[路由计算的原因：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1496485825}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Intra-area LSA]{lang="EN-US"}]{#struct_0_x4702_18917_672994322}[：区域内]{style="font-family:宋体"}[LSA]{lang="EN-US"}[变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Inter-area LSA]{lang="EN-US"}]{#struct_0_x4702_18917_686912720}[：区域间]{style="font-family:宋体"}[LSA]{lang="EN-US"}[变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[External LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x703044061}[：外部]{style="font-family:
  宋体"}[LSA]{lang="EN-US"}[变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Configuration]{lang="EN-US"}]{#struct_0_x4702_18917_x2109619481}[：配置变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Area 0 full neighbor]{lang="EN-US"}]{#struct_0_x4702_18917_x1496551361}[：区域]{style="font-family:宋体"}[0FULL]{lang="EN-US"}[邻居个数变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Area 0 up interface]{lang="EN-US"}]{#struct_0_x4702_18917_x903856216}[：区域]{style="font-family:宋体"}[0UP]{lang="EN-US"}[接口个数变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[LSDB overflow state]{lang="EN-US"}]{#struct_0_x4702_18917_1567808283}[：]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AS number]{lang="EN-US"}]{#struct_0_x4702_18917_x1038963213}[：]{style="font-family:
  宋体"}[AS]{lang="EN-US"}[号变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[ABR summarization]{lang="EN-US"}]{#struct_0_x4702_18917_467161406}[：]{style="font-family:宋体"}[ABR]{lang="EN-US"}[聚合变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[GR end]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354753}[：]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[结束]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Routing policy]{lang="EN-US"}]{#struct_0_x4702_18917_x1651681674}[：路由策略变化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Intra-area tunnel]{lang="EN-US"}]{#struct_0_x4702_18917_1624789407}[：区域内隧道变化]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Others]{lang="EN-US"}]{#struct_0_x4702_18917_x302699389}[：除上述原因之外的其他原因]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1189393167}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居]{style="font-family:宋体"}[的]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 event-log peer]{lang="EN-US"}]{#struct_0_x4702_18917_1624854943}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[                  Neighbors log]{lang="EN-US"}

[ ]{lang="EN-US"}

[Date       Time     Local Address   Remote Address  Router ID       Reason]{lang="EN-US"}

[2012-12-31 12:35:45 197.168.1.1     197.168.1.2     2.2.2.2         IntPhyChange]{lang="EN-US"}

[2012-12-31 12:35:19 197.168.1.1     197.168.1.2     2.2.2.2         ConfNssaArea]{lang="EN-US"}

[2012-12-31 12:34:59 197.168.1.1     197.168.1.2     2.2.2.2         SilentInt]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ospf event-log peer]{lang="EN-US"}]{#struct_0_x4702_18917_2064801903}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_418703046}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1625444767}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1625510303}

[[Date &Time]{lang="EN-US"}]{#struct_0_x4702_18917_x1894829252}

[[邻居]{style="font-family:宋体"}]{#struct_0_x4702_18917_1624920482}[状态变化]{style="font-family:宋体"}[的时间]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_x4702_18917_48444096}

[[建立邻居关系的本端地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_1624986018}

[[Remote Address]{lang="EN-US"}]{#struct_0_x4702_18917_1625051554}

[[建立邻居关系的对端地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_1225369727}

[[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1625117090}

[[邻居的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1624658338}

[[Reason]{lang="EN-US"}]{#struct_0_x4702_18917_1598216308}

[[邻居状态变化的原因：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1624723874}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ResetConnect]{lang="EN-US"}]{#struct_0_x4702_18917_1624789410}[：内存不足断连接]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IntChange]{lang="EN-US" style="color:black"}]{#struct_0_x4702_18917_x1189196560}[：接口参数改变]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VlinkChange]{lang="EN-US"}]{#struct_0_x4702_18917_1624854946}[：虚连接参数改变]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ShamlinkChange]{lang="EN-US"}]{#struct_0_x4702_18917_2064998511}[：]{lang="EN-US" style="font-family:宋体"}[伪连接]{style="font-family:宋体"}[参数改变]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ResetOspf]{lang="EN-US"}]{#struct_0_x4702_18917_1625444770}[：]{lang="EN-US" style="font-family:宋体"}[重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UndoOspf]{lang="EN-US"}]{#struct_0_x4702_18917_1625510306}[：删除]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UndoArea]{lang="EN-US"}]{#struct_0_x4702_18917_x1895156932}[：删除]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[UndoNetwork]{lang="EN-US"}]{#struct_0_x4702_18917_1624920481}[：接口去使能]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SilentInt]{lang="EN-US"}]{#struct_0_x4702_18917_1624986017}[：配置抑制接口]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IntLogChange]{lang="EN-US"}]{#struct_0_x4702_18917_x1907013247}[：接口逻辑属性变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IntPhyChange]{lang="EN-US"}]{#struct_0_x4702_18917_1625051553}[：接口物理属性变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[IntVliChange]{lang="EN-US" style="color:black"}]{#struct_0_x4702_18917_1625117089}[：接口]{lang="EN-US" style="font-family:宋体"}[虚连接]{style="font-family:宋体"}[属性变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[VlinkDown]{lang="EN-US"}]{#struct_0_x4702_18917_1628225309}[：]{lang="EN-US" style="font-family:宋体"}[虚连接]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ShamlinkDown]{lang="EN-US"}]{#struct_0_x4702_18917_1624658337}[：]{lang="EN-US" style="font-family:宋体"}[伪连接]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[DeadExpired]{lang="EN-US"}]{#struct_0_x4702_18917_1624723873}[：]{lang="EN-US" style="font-family:宋体"}[Dead Timer]{lang="EN-US"}[超时]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ConfStubArea]{lang="EN-US"}]{#struct_0_x4702_18917_1646039368}[：配置]{lang="EN-US" style="font-family:宋体"}[Stub]{lang="EN-US"}[区域参数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[ConfNssaArea]{lang="EN-US"}]{#struct_0_x4702_18917_1624789409}[：配置]{lang="EN-US" style="font-family:宋体"}[N]{lang="EN-US"}[SSA]{lang="EN-US"}[区域参数]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[AuthChange]{lang="EN-US" style="color:black"}]{#struct_0_x4702_18917_1624854945}[：认证类型变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[OpaqueChange]{lang="EN-US"}]{#struct_0_x4702_18917_2065195119}[：]{lang="EN-US" style="font-family:宋体"}[Opaque]{lang="EN-US"}[能力改变]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Retrans]{lang="EN-US"}]{#struct_0_x4702_18917_1625444769}[：重传过多]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[LLSChange]{lang="EN-US"}]{#struct_0_x4702_18917_1625510305}[：]{lang="EN-US" style="font-family:宋体"}[LLS]{lang="EN-US"}[能力变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[OOBChange]{lang="EN-US"}]{#struct_0_x4702_18917_x1103962877}[：]{lang="EN-US" style="font-family:宋体"}[OOB]{lang="EN-US"}[能力变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[GRChange]{lang="EN-US"}]{#struct_0_x4702_18917_1584523016}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力变化]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BFDDown]{lang="EN-US"}]{#struct_0_x4702_18917_x1103897341}[：]{lang="EN-US" style="font-family:宋体"}[BFD Down]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[BadLSReq]{lang="EN-US"}]{#struct_0_x4702_18917_x1103831805}[：收到]{lang="EN-US" style="font-family:宋体"}[BadLSReq]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[SeqMismatch]{lang="EN-US"}]{#struct_0_x4702_18917_x1876028555}[：]{style="font-family:
  宋体"}[收到]{lang="EN-US" style="font-family:宋体"}[SeqNumberMismatch]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[1-Way]{lang="EN-US"}]{#struct_0_x4702_18917_x1103766269}[：]{style="font-size:10.0pt;
  font-family:宋体;color:black"}[收到]{lang="EN-US" style="font-family:宋体"}[1-Way]{lang="EN-US"}[事件]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1712290168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ospf event-log]{lang="EN-US"}**]{#struct_0_x4702_18917_x1104225021}

::::: {#1196695539 .myid}
[]{#_Toc404788001}[]{#struct_0_x4702_18917_858786591}[]{#_Toc340827299}[]{#_Toc338927728}

**OSPF \-- OSPF配置命令 \-- display ospf fast-reroute lfa-candidate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_x1234052856}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_x1496420289}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display ospf fast-reroute lfa-candidate]{lang="EN-US"}**]{#struct_0_x4702_18917_x533341050}[命令用来显示区域中]{style="font-family:宋体"}[FRR]{lang="EN-US"}[备份下一跳候选列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1687523919}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] \[ **area** *area-id* \] **fast-reroute lfa-candidate**]{lang="EN-US"}]{#struct_0_x4702_18917_1782235492}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1622851251}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_2129700727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1572919486}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_716718218}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1496223681}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1011533902}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x568613372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1060536153}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_133238472}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有进程的备份下一跳候选列表。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**]{#struct_0_x4702_18917_1721044}*[ area-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定区域]{style="font-family:宋体"}[FRR]{lang="EN-US"}[备份下一跳候选列表]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将显示所有区域的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_267276727}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_902786932}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[FRR]{lang="EN-US"}[备份下一跳候选列表]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 area 0 fast-reroute lfa-candidate]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289217}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[                  LFA Candidate List]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[ Candidate nexthop count: 2]{lang="EN-US"}

[ NextHop          IntIP            Interface]{lang="EN-US"}

[ 10.0.1.1         10.0.1.2         Vlan10]{lang="EN-US"}

[ 10.0.11.1        10.0.11.2        Vlan20]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ospf fast-reroute lfa-candidate]{lang="EN-US"}]{#struct_0_x4702_18917_242285886}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1941358905}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2010920139}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1973730805}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x273795930}

[[显示该区域的备份下一跳信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1496092609}

[[Candidate nexthop count]{lang="EN-US"}]{#struct_0_x4702_18917_241938665}

[[备份下一跳个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_x876486350}

[[NextHop]{lang="EN-US"}]{#struct_0_x4702_18917_x1152926172}

[[备份下一跳地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_x651496346}

[[IntIP]{lang="EN-US"}]{#struct_0_x4702_18917_x617728278}

[[出接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158145}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x130454210}

[[出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_1838420006}

[ ]{lang="EN-US"}

::::: {#-693401877 .myid}
[]{#_Toc404788002}[]{#struct_0_x4702_18917_x1925835625}

**OSPF \-- OSPF配置命令 \-- display ospf graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_166216921}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_1211966318}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display ospf graceful-restart]{lang="EN-US"}**]{#struct_0_x4702_18917_x1495961537}[命令用来查看]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_956301470}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **graceful-restart** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x471907393}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x786937356}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_186557210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x760923041}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1856995189}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1199973141}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1496027073}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1642377606}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x871858560}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_2024103465}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_69371081}[：显示]{style="font-family:宋体"}[GR]{lang="EN-US"}[详细状态信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x312497840}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1851737916}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[详细]{style="font-family:宋体"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf graceful-restart verbose]{lang="EN-US"}]{#struct_0_x4702_18917_x1496551360}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[              Graceful Restart information]{lang="EN-US"}

[ ]{lang="EN-US"}

[Graceful Restart capability     : Enable(IETF)]{lang="EN-US"}

[Graceful Restart support        : Planned and un-planned,Partial]{lang="EN-US"}

[Helper capability                  : Enable(IETF)]{lang="EN-US"}

[Helper support                  : Planned and un-planned(IETF),Strict LSA check]{lang="EN-US"}

[Current GR state                : Normal]{lang="EN-US"}

[Graceful Restart period         : 40 seconds]{lang="EN-US"}

[Number of neighbors under Helper: 0]{lang="EN-US"}

[Number of restarting neighbors  : 0]{lang="EN-US"}

[Last exit reason:]{lang="EN-US"}

[  Restarter  : None]{lang="EN-US"}

[  Helper     : None]{lang="EN-US"}

[ ]{lang="EN-US"}

[Area: 0.0.0.0]{lang="EN-US"}

[Authtype: None Area flag: Normal]{lang="EN-US"}

[Area up Interface count: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface: 40.4.0.1 (Vlan-interface40)]{lang="EN-US"}

[Restarter state: Normal  State: P-2-P     Type: PTP]{lang="EN-US"}

[Last exit reason:]{lang="EN-US"}

[  Restarter  : None]{lang="EN-US"}

[  Helper     : None]{lang="EN-US"}

[Neighbor count of this interface: 1]{lang="EN-US"}

[Number of neighbors under Helper]{lang="EN-US"}[：]{style="font-family:宋体"}[0]{lang="EN-US"}

[Neighbor        IP address      GR state     Last Helper exit reason]{lang="EN-US"}

[3.3.3.3         40.4.0.3        Normal       None]{lang="EN-US"}

[ ]{lang="EN-US"}

[Virtual-link Neighbor-ID  -\> 4.4.4.4, Neighbor-State: Full]{lang="EN-US"}

[Restarter state: Normal]{lang="EN-US"}

[Interface: 20.2.0.1 (Vlink)]{lang="EN-US"}

[Transit Area]{lang="EN-US"}[：]{style="font-family:宋体"}[0.0.0.1]{lang="EN-US"}

[Last exit reason:]{lang="EN-US"}

[  Restarter  : None]{lang="EN-US"}

[  Helper     : None]{lang="EN-US"}

[Neighbor        IP address      GR state     Last Helper exit reason]{lang="EN-US"}

[4.4.4.4         20.2.0.4        Normal       Reset neighbor]{lang="EN-US"}

[]{#struct_0_x4702_18917_662227725}[]{#display_ospf_graceful-restart__display_o}[]{#display_ospf_graceful-restart__tb_01}[表1-10 ]{lang="EN-US"}[display ospf graceful-restart]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1935340871}[[字段]{style="font-size:9.0pt;
   font-family:黑体"}]{#struct_0_x4702_18917_972202368}
:::::

[[描述]{style="font-size:9.0pt;font-family:黑体"}]{#struct_0_x4702_18917_x1991069888}

[[OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}]{#struct_0_x4702_18917_x819247431}

[[Graceful Restart information]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354752}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x85597733}[进程是]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息]{style="font-family:宋体"}

[[Graceful Restart capability]{lang="EN-US"}]{#struct_0_x4702_18917_x1877425488}

[[进程]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x4702_18917_x2147033817}[能力配置：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enable(IETF)]{lang="EN-US"}]{#struct_0_x4702_18917_2101816003}[：使能]{style="font-family:
  宋体"}[IETF GR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enable(Nonstandard)]{lang="EN-US"}]{#struct_0_x4702_18917_1185283991}[：使能非]{style="font-family:宋体"}[IETF GR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disable]{lang="EN-US"}]{#struct_0_x4702_18917_x1496420288}[：关闭了]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[能力]{style="font-family:宋体"}

[[Graceful Restart support]{lang="EN-US"}]{#struct_0_x4702_18917_x2099424991}

[[进程]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x4702_18917_1166547568}[支持模式（]{style="font-family:宋体"}[GR]{lang="EN-US"}[使能时才显示）：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Planned and un-planned]{lang="EN-US"}]{#struct_0_x4702_18917_x76315808}[：支持计划和非计划]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Planned only]{lang="EN-US"}]{#struct_0_x4702_18917_x1348830240}[：只支持计划性]{style="font-family:
  宋体"}[GR]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Partial]{lang="EN-US"}]{#struct_0_x4702_18917_x1496223680}[：支持接口级]{style="font-family:
  宋体"}[GR]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Global]{lang="EN-US"}]{#struct_0_x4702_18917_1717349453}[：不支持接口级]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[，支持全局]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[Helper capability]{lang="EN-US"}]{#struct_0_x4702_18917_x1437911673}

[[进程]{style="font-family:宋体"}[Help]{lang="EN-US"}]{#struct_0_x4702_18917_x1394969024}[能力配置：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled (IETF)]{lang="EN-US"}]{#struct_0_x4702_18917_x631057534}[：支持作为标准]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[的能力]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled (Nonstandard)]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289216}[：支持作为非标准]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[的能力]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled (IETF and nonstandard)]{lang="EN-US"}]{#struct_0_x4702_18917_x1323798055}[：同时支持作为标准和非标准]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[的能力]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_1382403353}[：不支持作为]{style="font-family:
  宋体"}[GR Helper]{lang="EN-US"}[的能力]{style="font-family:
  宋体"}

[[Helper support]{lang="EN-US"}]{#struct_0_x4702_18917_1916338766}

[[显示支持]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_x1496092608}[的策略（]{style="font-family:宋体"}[Helper]{lang="EN-US"}[使能时才显示）：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Strict LSA check]{lang="EN-US"}]{#struct_0_x4702_18917_1808022606}[：]{style="font-family:宋体"}[Helper]{lang="EN-US"}[端支持严格的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查；]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Planned and un-planned]{lang="EN-US"}]{#struct_0_x4702_18917_x962315596}[：支持作为计划和非计划重启的]{style="font-family:宋体"}[Helper]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Planned only]{lang="EN-US"}]{#struct_0_x4702_18917_1496934387}[：只支持作为计划]{style="font-family:
  宋体"}[GR]{lang="EN-US"}[的]{style="font-family:宋体"}[ Helper]{lang="EN-US"}

[[Current GR state]{lang="EN-US"}]{#struct_0_x4702_18917_280570362}

[[当前]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158144}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_1435629731}[：普通状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_x4702_18917_x2058402541}[：进程正在]{style="font-family:
  宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1168214088}[：进程正在作为]{lang="EN-US" style="font-family:宋体"}[GR Helper]{lang="EN-US"}

[[Graceful-restart period]{lang="EN-US"}]{#struct_0_x4702_18917_x1495961536}

[[GR]{lang="EN-US"}]{#struct_0_x4702_18917_x609782471}[周期]{style="font-family:宋体"}

[[Number of neighbors under helper]{lang="EN-US"}]{#struct_0_x4702_18917_x739375025}

[[处于]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1246534472}[状态的邻居数量]{style="font-family:宋体"}

[[Number of restarting neighbors]{lang="EN-US"}]{#struct_0_x4702_18917_x1496027072}

[[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1086505749}[端显示的处于重启路由器的数量]{style="font-family:宋体"}

[[Last exit reason]{lang="EN-US"}]{#struct_0_x4702_18917_x1533231662}

[[上次退出原因，其中：]{style="font-family:宋体"}]{#struct_0_x4702_18917_844360152}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarter]{lang="EN-US"}]{#struct_0_x4702_18917_x1496485827}[：表示退出]{style="font-family:宋体"}[Restarter]{lang="EN-US"}[的原因]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1835793736}[：表示退出]{style="font-family:宋体"}[Helper]{lang="EN-US"}[的原因]{style="font-family:宋体"}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x442988200}

[[开始列举当前进程中各区域的信息。显示当前区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1496551363}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式]{style="font-family:宋体"}

[[Authtype]{lang="EN-US"}]{#struct_0_x4702_18917_x2066655630}

[[区域验证模式，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_330457625}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_x4702_18917_417072384}[：表示无验证]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Simple]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354755}[：表示简单验证模式]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_1480486208}[：表示]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式]{style="font-family:宋体"}

[[Area flag]{lang="EN-US"}]{#struct_0_x4702_18917_x1815322588}

[[区域类型：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1496420291}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No]{lang="EN-US"}]{#struct_0_x4702_18917_x889505874}[rmal]{lang="EN-US"}[：普通区域]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x1611166763}[：]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[StubNoSummary]{lang="EN-US"}]{#struct_0_x4702_18917_x1496223683}[：完全]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_2120633980}[：]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NSSANoSummary]{lang="EN-US"}]{#struct_0_x4702_18917_x633567894}[：完全]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{style="font-family:宋体"}

[[Area up Interface count]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289219}

[[区域下]{style="font-family:宋体"}[UP]{lang="EN-US"}]{#struct_0_x4702_18917_1405085300}[的接口计数]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x731747599}

[[区域内的接口信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1496092611}

[[Restarter state]{lang="EN-US"}]{#struct_0_x4702_18917_x114226159}

[[作为]{style="font-family:宋体"}[Restarter]{lang="EN-US"}]{#struct_0_x4702_18917_294632236}[的状态]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158147}

[[接口状态]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1293253624}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x1184765615}

[[接口的网络类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1495961539}

[[Neighbor count of this interface]{lang="EN-US"}]{#struct_0_x4702_18917_149732416}

[[接口下的邻居]{style="font-family:宋体"}]{#struct_0_x4702_18917_299117370}

[[Neighbor]{lang="EN-US"}]{#struct_0_x4702_18917_x1496027075}

[[邻居]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1489790276}

[[IP address]{lang="EN-US"}]{#struct_0_x4702_18917_x22841576}

[[邻居]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1496485826}[地址]{style="font-family:宋体"}

[[GR state]{lang="EN-US"}]{#struct_0_x4702_18917_269709795}

[[邻居的]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_x4702_18917_2078195905}[状态：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_x1496551362}[：普通状态]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_x4702_18917_x500571689}[：进程正在]{style="font-family:
  宋体"}[GR]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Under Helper]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354754}[：进程正在作为]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[ Helper]{lang="EN-US"}

[[Last Helper exit reason]{lang="EN-US"}]{#struct_0_x4702_18917_x1248397147}

[[上一次作为该邻居]{style="font-family:宋体"}[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1059174716}[退出的原因]{style="font-family:宋体"}

[[Virtual-link Neighbor-ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1496420290}

[[Vlink]{lang="EN-US"}]{#struct_0_x4702_18917_1839377481}[的邻居]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[[Neighbor-State]{lang="EN-US"}]{#struct_0_x4702_18917_x1496223682}

[[Vlink]{lang="EN-US"}]{#struct_0_x4702_18917_554550039}[和邻居的状态，包括]{style="font-family:宋体"}[Down]{lang="EN-US"}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{style="font-family:宋体"}[ExStart]{lang="EN-US"}[、]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{style="font-family:宋体"}[Loading]{lang="EN-US"}[和]{style="font-family:宋体"}[Full]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_2049717037}

[[Vlink]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289218}[接口所属的出接口]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2111316994 .myid}
[]{#_Toc404788003}[]{#struct_0_x4702_18917_x160998641}

**OSPF \-- OSPF配置命令 \-- display ospf interface**

------------------------------------------------------------------------

[**[display ospf interface]{lang="EN-US"}**]{#struct_0_x4702_18917_1165786317}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1232342798}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **interface** ]{lang="EN-US"}[\[ *interface-type* *interface-number* \| **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_232074817}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x71558330}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x98798420}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1550522299}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1842660546}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x997429016}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_2104822961}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158146}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_272830317}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1867875467}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的接口信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_680368593}[：接口类型和编号]{style="font-family:宋体"}[。显示指定接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x2086253499}[：显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[详细信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1495961538}

[[如果未指定接口或参数]{style="font-family:宋体"}**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x1416351525}[，将显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2076208450}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1123320681}[显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf interface]{lang="EN-US"}]{#struct_0_x4702_18917_400962555}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.1]{lang="EN-US"}

[                  Interfaces]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[ IP Address      Type         State    Cost  Pri   DR              BDR]{lang="EN-US"}

[ 192.168.1.1     PTP          P-2-P    1562  1     0.0.0.0         0.0.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1]{lang="EN-US"}

[ IP Address      Type         State    Cost  Pri   DR              BDR]{lang="EN-US"}

[ 172.16.0.1      Broadcast    DR       1     1     172.16.0.1      0.0.0.0]{lang="EN-US"}

[]{#struct_0_x4702_18917_x1496027074}[]{#_Toc94753857}[]{#_Toc94671183}[]{#_Toc73952261}[[表1-11 ]{lang="EN-US"}[display ospf interface]{lang="EN-US"}]{#_Toc68319394}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1958772695}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x76293665}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1333779781}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_1139361007}

[[接口所属的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x280911709}

[[IP address]{lang="EN-US"}]{#struct_0_x4702_18917_1489091050}

[[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1496485829}[地址（不管是否使能了流量工程）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x1296374146}

[[接口的网络类型，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1966665555}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PTP]{lang="EN-US"}]{#struct_0_x4702_18917_x1244826339}[表示网络类型为点对点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PTMP]{lang="EN-US"}]{#struct_0_x4702_18917_28222413}[表示网络类型为点对多点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Broadcast]{lang="EN-US"}]{#struct_0_x4702_18917_207394907}[表示网络类型为广播]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[NBMA]{lang="EN-US"}]{#struct_0_x4702_18917_x1496551365}[表示网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_1065512252}

[[根据]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1470381148}[接口状态机确定的当前接口状态，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x4702_18917_x788283253}[表示在接口上没有发送和接收任何路由协议的报文]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loopback]{lang="EN-US"}]{#struct_0_x4702_18917_x1104225019}[表示路由器到网络的接口处于环回状态，不能用于正常的数据传输]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Waiting]{lang="EN-US"}]{#struct_0_x4702_18917_x321531991}[表示接口开始发送和接收]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，并试图去识别网络上的]{style="font-family:宋体"}[DR]{lang="EN-US"}[和]{style="font-family:宋体"}[BDR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P-2-P]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354757}[表示接口将每隔]{style="font-family:宋体"}[HelloInterval]{lang="EN-US"}[的时间间隔发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，并尝试和接口链路另一端相连的路由器建立邻接关系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_317686794}[表示路由器是所连网络的指定路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_2066444832}[表示路由器是所连网络的备份指定路由器]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DROther]{lang="EN-US"}]{#struct_0_x4702_18917_198384190}[表示路由器既不是所连网络的指定路由器，也不是所连网络的备份指定路由器]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_x1496420293}

[[接口开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2052305288}

[[Pri]{lang="EN-US"}]{#struct_0_x4702_18917_x1327646878}

[[路由器优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_404896507}

[[DR]{lang="EN-US"}]{#struct_0_x4702_18917_678481846}

[[接口所属网段的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_x1496223685}

[[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_957834566}

[[接口所属网段的]{style="font-family:宋体"}[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_x727076604}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2089228093}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf interface gigabitethernet 1/0/1]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289221}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.1]{lang="EN-US"}

[                  Interfaces]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Interface: 172.16.0.1 (GigabitEthernet1/0/1)]{lang="EN-US"}

[ Cost: 1       State: DR        Type: Broadcast    MTU: 1500]{lang="EN-US"}

[ Priority: 1]{lang="EN-US"}

[ Designated router: 172.16.0.1]{lang="EN-US"}

[ Backup designated router: 0.0.0.0]{lang="EN-US"}

[ Timers: Hello 10, Dead 40, Poll  40, Retransmit 5, Transmit Delay 1]{lang="EN-US"}

[ FRR backup: Enabled]{lang="EN-US"}

[ Enabled by interface configuration (including secondary IP addresses)]{lang="EN-US"}

[ MD5 authentication enabled.]{lang="EN-US"}

[    The last key is 3.]{lang="EN-US"}

[    The rollover is in progress, 2 neighbor(s) left.]{lang="EN-US"}

[ LDP state: No-LDP]{lang="EN-US"}

[ LDP sync state: Achieved]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display ospf interface verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1048920476}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1955753409}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x477281614}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1608617281}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1496092613}

[[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1277025573}[地址等信息]{style="font-family:宋体"}

[[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_122404191}

[[最大传输单元]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1203525510}

[[Timers]{lang="EN-US"}]{#struct_0_x4702_18917_x1003504413}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1426582831}[定时器的值，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158149}[表示接口发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dead]{lang="EN-US"}]{#struct_0_x4702_18917_x1743592318}[表示邻居的失效时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Poll]{lang="EN-US"}]{#struct_0_x4702_18917_x1552394569}[表示接口发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Retransmit]{lang="EN-US"}]{#struct_0_x4702_18917_260906302}[表示定接口重传]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[时间间隔]{lang="EN-US" style="font-family:宋体"}

[[FRR backup]{lang="EN-US"}]{#struct_0_x4702_18917_x1507286325}

[[是否使能接口参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x4702_18917_x1495961541}[（]{style="font-family:宋体"}[Loop Free Alternate]{lang="EN-US"}[）计算：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4702_18917_x206301336}[：]{lang="EN-US" style="font-family:宋体"}[使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_1270441375}[：关闭]{style="font-family:宋体"}

[[Enabled by interface configuration (including secondary IP addresses)]{lang="EN-US"}]{#struct_0_x4702_18917_x1012744219}

[[接口使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_891462760}[，包括接口从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MD5 authentication enabled]{lang="EN-US"}]{#struct_0_x4702_18917_x1496027077}

[[验证模式]{style="font-family:宋体"}]{#struct_0_x4702_18917_326990862}

[[The last key]{lang="EN-US"}]{#struct_0_x4702_18917_x91445939}

[[最新的]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_1155728097}[验证字标识符]{style="font-family:宋体"}

[[neighbor(s)]{lang="EN-US"}]{#struct_0_x4702_18917_x1496485828}

[[尚未完成]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_1432509209}[验证平滑迁移的邻居个数]{style="font-family:宋体"}

[[LDP state]{lang="EN-US"}]{#struct_0_x4702_18917_855769140}

[[LDP]{lang="EN-US"}]{#struct_0_x4702_18917_2064763356}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x4702_18917_855834676}[：表示处于初始化状态，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[还没有上报状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-LDP]{lang="EN-US"}]{#struct_0_x4702_18917_x1191214246}[：]{style="font-family:宋体"}[表示未配置]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_x4702_18917_1172626488}[：]{style="font-family:宋体"}[表示未建立]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x4702_18917_x1597902737}[：]{style="font-family:宋体"}[表示已建立]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}

[[LDP sync state]{lang="EN-US"}]{#struct_0_x4702_18917_951526029}

[[LDP IGP]{lang="EN-US"}]{#struct_0_x4702_18917_855900212}[同步状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x4702_18917_x1620552347}[：]{style="font-family:宋体"}[表示初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Achieved]{lang="EN-US"}]{#struct_0_x4702_18917_43824470}[：]{style="font-family:宋体"}[表示已同步]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max cost]{lang="EN-US"}]{#struct_0_x4702_18917_855965748}[：]{style="font-family:宋体"}[表示保持]{lang="EN-US" style="font-family:宋体"}[最大开销值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#987317882 .myid}
[]{#_Toc404788004}[]{#struct_0_x4702_18917_x1531362123}[]{#_Toc138212550}[]{#_Toc93984778}[]{#_Toc61236314}

**OSPF \-- OSPF配置命令 \-- display ospf lsdb**

------------------------------------------------------------------------

[**[display ospf lsdb]{lang="EN-US"}**]{#struct_0_x4702_18917_x694947321}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x476079322}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **lsdb** \[ **brief** ]{lang="EN-US"}]{#struct_0_x4702_18917_1106665672}[\| ]{lang="EN-US" style="font-size:10.0pt;
color:black"}**[originate-router]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}*[advertising-router-id]{lang="EN-US"}*[ \| ]{lang="EN-US" style="font-size:10.0pt;color:black"}**[self-originate]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;color:black"}[\]]{lang="EN-US"}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **lsdb** { **opaque-as** \| **ase** } \[ *link-state-id* \] \[ **originate-router** *advertising-router-id* \| **self-originate** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1904213968}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] \[ **area** *area-id* \] **lsdb** { **asbr** \| **network** \| **nssa** \| **opaque-area** \| **opaque-link** \| **router** \| **summary** } \[ *link-state-id* \] \[ **originate-router** *advertising-router-id* \| **self-originate** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x562015670}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_712615791}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_2127209889}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_868827288}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x934434802}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1496354756}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1883770735}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1594980116}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1372739460}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_261299001}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的链路状态数据库信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}***[ area-id]{lang="EN-US"}*]{#struct_0_x4702_18917_579794779}[：显示数据库中指定区域的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将显示所有区域的信息。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x4702_18917_x801457357}[：显示数据库的概要信息。]{style="font-family:宋体"}

[**[asbr]{lang="EN-US"}**]{#struct_0_x4702_18917_x1627435210}[：显示数据库中]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[ASBR Summary LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[ase]{lang="EN-US"}**]{#struct_0_x4702_18917_x1496420292}[：显示数据库中]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[AS External LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[network]{lang="EN-US"}**]{#struct_0_x4702_18917_676578067}[：显示数据库中]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[nssa]{lang="EN-US"}**]{#struct_0_x4702_18917_450311486}[：显示数据库中]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[NSSA External LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-area]{lang="EN-US"}**]{#struct_0_x4702_18917_802021615}[：显示数据库中]{style="font-family:宋体"}[Type-10 LSA ]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-area LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-as]{lang="EN-US"}**]{#struct_0_x4702_18917_347104370}[：显示数据库中]{style="font-family:宋体"}[Type-11 LSA ]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-AS LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[opaque-link]{lang="EN-US"}**]{#struct_0_x4702_18917_423469344}[：显示数据库中]{style="font-family:宋体"}[Type-9 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Opaque-link LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[router]{lang="EN-US"}**]{#struct_0_x4702_18917_49313141}[：显示数据库中]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Router LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[**[summary]{lang="EN-US"}**]{#struct_0_x4702_18917_497234512}[：显示数据库中]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Summary LSA]{lang="EN-US"}[）的信息。]{style="font-family:宋体"}

[*[link-state-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1900118604}[：链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式。]{style="font-family:宋体"}

[**[originate-router ]{lang="EN-US"}***[advertising-router-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1496223684}[：发布]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[self-originate]{lang="EN-US"}**]{#struct_0_x4702_18917_x608249375}[：显示本地路由器自己产生的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的数据库信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1399216825}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x758824413}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf lsdb]{lang="EN-US"}]{#struct_0_x4702_18917_x1496289220}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.0.1]{lang="EN-US"}

[                  Link State Database]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Area: 0.0.0.0]{lang="EN-US"}

[ Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric]{lang="EN-US"}

[ Router    192.168.0.2     192.168.0.2        474  36    80000004   0]{lang="EN-US"}

[ Router    192.168.0.1     192.168.0.1        21   36    80000009   0]{lang="EN-US"}

[ Network   192.168.0.1     192.168.0.1        321  32    80000003   0]{lang="EN-US"}

[ Sum-Net   192.168.1.0     192.168.0.1        321  28    80000002   1]{lang="EN-US"}

[ Sum-Net   192.168.2.0     192.168.0.2        474  28    80000002   1]{lang="EN-US"}

[                         Area: 0.0.0.1]{lang="EN-US"}

[ Type      LinkState ID    AdvRouter          Age  Len   Sequence   Metric]{lang="EN-US"}

[ ]{lang="EN-US"}[Router    192.168.0.1     192.168.0.1        21   36    80000005   0]{lang="NL"}

[ Sum-Net   192.168.2.0     192.168.0.1        321  28    80000002   2]{lang="NL"}

[ Sum-Net   192.168.0.0     192.168.0.1        321  28    80000002   1]{lang="NL"}

[Type 9 Opaque (Link-Local Scope) Database]{lang="NL"}

[ Flags: \* -Vlink interface LSA]{lang="NL"}

[ Type      LinkState ID    AdvRouter          Age  Len   Sequence   Interfaces]{lang="NL"}

[\*Opq-Link  3.0.0.0         7.2.2.1            8    14    80000001   10.1.1.2]{lang="NL"}

[\*Opq-Link  3.0.0.0         7.2.2.2            8    14    80000001   20.1.1.2]{lang="NL"}

[[表1-13 ]{lang="EN-US"}[display ospf lsdb]{lang="EN-US"}]{#struct_0_x4702_18917_x517163465}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1956928507}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1501983814}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1496092612}

 

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_289058368}

[[显示该区域的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x4702_18917_x1210061194}[信息]{style="font-family:宋体"}

 

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1379781122}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_954712077}[类型]{style="font-family:宋体"}

 

[[LinkState ID]{lang="EN-US"}]{#struct_0_x4702_18917_792486339}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1496158148}[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}

 

[[AdvRouter]{lang="EN-US"}]{#struct_0_x4702_18917_x177508377}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1787929205}[发布路由器]{style="font-family:宋体"}

 

[[Age]{lang="EN-US"}]{#struct_0_x4702_18917_x290749030}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_76221656}[的老化时间]{style="font-family:宋体"}

 

[[Len]{lang="EN-US"}]{#struct_0_x4702_18917_x1495961540}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1772385277}[的长度]{style="font-family:宋体"}

 

[[Sequence]{lang="EN-US"}]{#struct_0_x4702_18917_x1003443810}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x820330970}[序列号]{style="font-family:宋体"}

 

[[Metric]{lang="EN-US"}]{#struct_0_x4702_18917_479002878}

[[度量值]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1496027076}

 

[[\*Opq-Link]{lang="NL"}]{#struct_0_x4702_18917_x1239093079}

[[表示]{style="font-family:宋体"}[Vlink]{lang="EN-US"}]{#struct_0_x4702_18917_x1412062636}[接口产生的]{style="font-family:宋体"}[Opequa LSA]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_9794731}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的链路状态数据库中网络]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 lsdb network]{lang="EN-US"}]{#struct_0_x4702_18917_69598116}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.1]{lang="EN-US"}

[                          Area: 0.0.0.0]{lang="EN-US"}

[                  Link State Database]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Type      : Network]{lang="EN-US"}

[    LS ID     : 192.168.0.2]{lang="EN-US"}

[    Adv Rtr   : 192.168.2.1]{lang="EN-US"}

[    LS Age    : 922]{lang="EN-US"}

[    Len       : 32]{lang="EN-US"}

[    Options   :  E]{lang="EN-US"}

[    Seq#      : 80000003]{lang="EN-US"}

[    Checksum  : 0x8d1b]{lang="EN-US"}

[    Net Mask  : 255.255.255.0]{lang="EN-US"}

[       Attached Router    192.168.1.1]{lang="EN-US"}

[       Attached Router    192.168.2.1]{lang="EN-US"}

[                          Area: 0.0.0.1]{lang="EN-US"}

[                  Link State Database]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Type      : Network]{lang="EN-US"}

[    LS ID     : 192.168.1.2]{lang="EN-US"}

[    Adv Rtr   : 192.168.1.2]{lang="EN-US"}

[    LS Age    : 782]{lang="EN-US"}

[    Len       : 32]{lang="EN-US"}

[    Options   :  NP]{lang="EN-US"}

[    Seq#      : 80000003]{lang="EN-US"}

[    Checksum  : 0x2a77]{lang="EN-US"}

[    Net Mask  : 255.255.255.0]{lang="EN-US"}

[       Attached Router    192.168.1.1]{lang="EN-US"}

[       Attached Router    192.168.1.2]{lang="EN-US"}

[]{#struct_0_x4702_18917_x1125605412}[]{#_Toc94753858}[]{#_Toc94671184}[]{#_Toc73952262}[[表1-14 ]{lang="EN-US"}[display ospf lsdb network]{lang="EN-US"}]{#_Toc68319395}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1953909237}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_69532580}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1207941445}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x1440573598}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1604690233}[类型]{style="font-family:宋体"}

[[LS ID]{lang="EN-US"}]{#struct_0_x4702_18917_869209963}

[[DR]{lang="EN-US"}]{#struct_0_x4702_18917_69729188}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Adv Rtr]{lang="EN-US"}]{#struct_0_x4702_18917_x2099937388}

[[发布路由器]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1774099820}

[[LS Age]{lang="EN-US"}]{#struct_0_x4702_18917_x20568352}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_603028743}[的老化时间]{style="font-family:宋体"}

[[Len]{lang="EN-US"}]{#struct_0_x4702_18917_94345602}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_69663652}[的长度]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_x4702_18917_159025710}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x701575799}[选项，各选项含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x4702_18917_1916221520}[：]{lang="EN-US" style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接受能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x4702_18917_x2068672310}[：]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的接受能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EA]{lang="EN-US"}]{#struct_0_x4702_18917_69860260}[：外部扩展属性]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的接受和转发能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC]{lang="EN-US"}]{#struct_0_x4702_18917_x713535482}[：支持按需链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x4702_18917_1523134550}[：是否支持]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_122118487}[：非纯末稍区域中的]{lang="EN-US" style="font-family:宋体"}[ABR]{lang="EN-US"}[路由器将]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的能力]{lang="EN-US" style="font-family:宋体"}

[[Seq#]{lang="EN-US"}]{#struct_0_x4702_18917_69794724}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_2101284247}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_x4702_18917_x1575360113}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1097039312}[校验和]{style="font-family:宋体"}

[[Net Mask]{lang="EN-US"}]{#struct_0_x4702_18917_69991332}

[[网络掩码]{style="font-family:宋体"}]{#struct_0_x4702_18917_1595271737}

[[Attached Router]{lang="EN-US"}]{#struct_0_x4702_18917_223208530}

[[与]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_x1752710765}[形成了完全邻接关系的路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，也包括]{style="font-family:宋体"}[DR]{lang="EN-US"}[自身的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#1475001082 .myid}
[]{#_Toc138212552}[]{#_Toc93984780}[]{#_Toc61236316}[]{#_Toc404788005}[]{#struct_0_x4702_18917_x67106762}[]{#_Toc340827303}[]{#_Toc338927729}[]{#_Toc256676608}[]{#_Toc256676609}[]{#_Toc256676610}[]{#_Toc256676611}[]{#_Toc256676612}[]{#_Toc256676613}[]{#_Toc256676614}[]{#_Toc256676615}[]{#_Toc256676616}[]{#_Toc256676617}[]{#_Toc256676618}[]{#_Toc256676619}[]{#_Toc256676620}[]{#_Toc256676624}[]{#_Toc256676628}[]{#_Toc256676629}[]{#_Toc256676630}[]{#_Toc256676631}[]{#_Toc256676650}

**OSPF \-- OSPF配置命令 \-- display ospf nexthop**

------------------------------------------------------------------------

[**[display ospf nexthop]{lang="EN-US"}**]{#struct_0_x4702_18917_69925796}[命令用来显示进程中的下一跳信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x280744301}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **nexthop**]{lang="EN-US"}]{#struct_0_x4702_18917_1844254585}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_696676772}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_808412543}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x233908190}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x597194791}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1071843324}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_70122404}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x141101920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1675000476}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x152218113}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有进程的下一跳信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1354524994}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x503575320}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由下一跳信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ospf nexthop]{lang="EN-US"}]{#struct_0_x4702_18917_70056868}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.2]{lang="EN-US"}

[                  Neighbor Nexthop Information]{lang="EN-US"}

[ ]{lang="EN-US"}

[ NbrID           Nexthop         Interface                RefCount   Status]{lang="EN-US"}

[ 1.1.1.2         4.4.4.4         Loop1                    1          Valid]{lang="EN-US"}

[ 1.1.1.1         1.1.1.1         GE1/0/2                 3          Valid]{lang="EN-US"}

[ 1.1.1.2         1.1.1.2         GE1/0/2                 4          Valid]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display ospf nexthop]{lang="EN-US"}]{#struct_0_x4702_18917_4586647}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1949445735}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1405469929}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x290505509}

[[NbrID]{lang="EN-US"}]{#struct_0_x4702_18917_45122519}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1310556116}

[[Nexthop]{lang="EN-US"}]{#struct_0_x4702_18917_x248079090}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_69598117}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_830709724}

[[出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_x118842552}

[[RefCount]{lang="EN-US"}]{#struct_0_x4702_18917_x1942427162}

[[该下一跳被引用次数]{style="font-family:宋体"}]{#struct_0_x4702_18917_x402129293}

[[Status]{lang="EN-US"}]{#struct_0_x4702_18917_69532581}

[[该下一跳状态：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1130710715}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Valid]{lang="EN-US"}]{#struct_0_x4702_18917_x2024899067}[：生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x4702_18917_1673053727}[：未生效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#966037150 .myid}
[]{#_Toc404788006}[]{#struct_0_x4702_18917_1314498979}[]{#_Toc343688429}

**OSPF \-- OSPF配置命令 \-- display ospf non-stop-routing status**

------------------------------------------------------------------------

[**[display ospf non-stop-routing status]{lang="EN-US"}**]{#struct_0_x4702_18917_2084940150}[命令用来]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[阶段信息。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x4702_18917_69729189}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **non-stop-routing status**]{lang="EN-US"}]{#struct_0_x4702_18917_238714772}

[[【视图】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x4702_18917_x639842209}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x508375988}

[[【缺省用户角色】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x4702_18917_699349023}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x8832345}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x870106985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_409910678}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_69663653}

[[【参数】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x4702_18917_x1797289426}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x46880159}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[阶段信息。]{style="font-family:宋体"}

[[【举例】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x4702_18917_x271739286}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2147150135}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[阶段信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf non-stop-routing status ]{lang="EN-US"}]{#struct_0_x4702_18917_x2086521103}

[ ]{lang="EN-US"}

[                   OSPF Process 1 with Router ID 192.168.33.12]{lang="EN-US"}

[                          Non Stop Routing information]{lang="EN-US"}

[                   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Non Stop Routing capability : Enabled]{lang="EN-US"}

[Upgrade phase : Normal]{lang="EN-US"}

[[表1-16 ]{lang="EN-US"}[display ospf non-stop-routing status]{lang="EN-US"}]{#struct_0_x4702_18917_69860261}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1976953509}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1625116678}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_46287503}

[[Non Stop Routing capability]{lang="EN-US"}]{#struct_0_x4702_18917_2114855813}

[[是否使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_x4702_18917_x863283858}[功能，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x4702_18917_x1761051026}[：使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_69794725}[：不使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}

[[Upgrade phase]{lang="EN-US"}]{#struct_0_x4702_18917_x237367913}

[[升级的各个阶段：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1510245474}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Prepare]{lang="EN-US"}]{#struct_0_x4702_18917_x895786182}[：升级准备阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restore Smooth]{lang="EN-US"}]{#struct_0_x4702_18917_x325906554}[：升级数据平滑阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Preroute]{lang="EN-US"}]{#struct_0_x4702_18917_1697716356}[：路由计算预处理阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Calculating]{lang="EN-US"}]{#struct_0_x4702_18917_69991333}[：路由计算阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redisting]{lang="EN-US"}]{#struct_0_x4702_18917_x743380423}[：路由引入阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Original and age]{lang="EN-US"}]{#struct_0_x4702_18917_85856522}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[生成和老化阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_2130607942}[：普通状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#210949272 .myid}
[]{#_Toc404788007}[]{#struct_0_x4702_18917_1478863631}

**OSPF \-- OSPF配置命令 \-- display ospf peer**

------------------------------------------------------------------------

[**[display ospf peer]{lang="EN-US"}**]{#struct_0_x4702_18917_69925797}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[中各区域邻居的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2057907859}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **peer** \[ **verbose** \] \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_x4702_18917_x683110924}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_70122405}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2097417056}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1596255793}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_14104657}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1135891253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x784162949}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1533106988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_297413565}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_70056869}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的各区域邻居的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_1960901783}[：显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[各区域邻居的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程各区域邻居的概要信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_x1481259192}[：接口类型和编号。如果未指定本参数，将显示所有接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1922899690}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果未指定本参数，将显示所有邻居路由器的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1128552025}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_69598114}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf peer verbose]{lang="EN-US"}]{#struct_0_x4702_18917_69532578}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[                  Neighbors]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area 0.0.0.0 interface 1.1.1.1(GigabitEthernet1/0/1)\'s neighbors]{lang="EN-US"}

[ Router ID: 1.1.1.2          Address: 1.1.1.2          GR state: Normal]{lang="EN-US"}

[   State: Full  Mode: Nbr is master  Priority: 1]{lang="EN-US"}

[   DR: 1.1.1.2  BDR: 1.1.1.1  MTU: 0]{lang="EN-US"}

[   Options is 0x02 (-\|-\|-\|-\|-\|-\|E\|-)]{lang="EN-US"}

[   Dead timer due in 33  sec]{lang="EN-US"}

[   Neighbor is up for 02:03:35]{lang="EN-US"}

[   Authentication Sequence: \[ 0 \]]{lang="EN-US"}

[   Neighbor state change count: 6]{lang="EN-US"}

[   BFD status: Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Last Neighbor Down Event:]{lang="EN-US"}

[ Router ID: 22.22.22.22]{lang="EN-US"}

[ Local Address: 11.11.11.11]{lang="EN-US"}

[ Remote Address: 22.22.22.22]{lang="EN-US"}

[ Time: Apr  9 03:18:19 2014]{lang="EN-US"}

[ Reason: Ospf_ifachange]{lang="EN-US"}[]{#_Toc94753860}[]{#_Toc94671186}[]{#_Toc73952264}[]{#_Toc68319397}

[[表1-17 ]{lang="EN-US"}[display ospf peer verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1695015984}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1976092501}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x69486987}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1184559820}

[[Area *areaID* interface *IPAddress*(*InterfaceName*)\'s neighbors]{lang="EN-US"}]{#struct_0_x4702_18917_x91167257}

[[显示接口在指定区域邻居信息，其中：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1853680042}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[areaID]{lang="EN-US"}*]{#struct_0_x4702_18917_69729186}[表示邻居所属的区域]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[IPAddress]{lang="EN-US"}*]{#struct_0_x4702_18917_x952926316}[表示接口]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[InterfaceName]{lang="EN-US"}*]{#struct_0_x4702_18917_x15911091}[表示接口名称]{lang="EN-US" style="font-family:
  宋体"}

[[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1354887687}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1179913260}

[[Address]{lang="EN-US"}]{#struct_0_x4702_18917_69663650}

[[邻居接口地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_x223311314}

[[GR State]{lang="EN-US"}]{#struct_0_x4702_18917_87389587}

[[GR]{lang="EN-US"}]{#struct_0_x4702_18917_x1291605242}[状态]{style="font-family:宋体"}[，取值为：]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_69860258}[：普通状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Restarter]{lang="EN-US"}]{#struct_0_x4702_18917_1648799191}[：正在作为]{lang="EN-US" style="font-family:宋体"}[GR ]{lang="EN-US"}[Restarter]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Complete]{lang="EN-US"}]{#struct_0_x4702_18917_974740718}[：]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[完成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Helper]{lang="EN-US"}]{#struct_0_x4702_18917_1032919530}[：]{lang="EN-US" style="font-family:宋体"}[正在作为]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_x56736720}

[[邻居状态，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_69794722}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x4702_18917_x1046671977}[表示邻居关系的初始状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x4702_18917_28577226}[表示在邻居失效时间内收到来自邻居路由器的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，但该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[数据包内没有包含自己的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，双向通信还没有建立起来]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Attempt]{lang="EN-US"}]{#struct_0_x4702_18917_x915985474}[该状态仅对]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[网络上的邻居有效，表示最近没有从邻居收到信息，但仍需作出进一步的尝试，用以与邻居联系]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2-Way]{lang="EN-US"}]{#struct_0_x4702_18917_69991330}[表示双向通信已经建立，在从邻居路由器收到的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中看到了自己的]{lang="EN-US" style="font-family:宋体"}[RouterID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exstart]{lang="EN-US"}]{#struct_0_x4702_18917_1212934713}[表示路由器和邻居建立主]{style="font-family:宋体"}[/]{lang="EN-US"}[从关系、确定初始]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文的序列号，为交换]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文做好准备]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exchange]{lang="EN-US"}]{#struct_0_x4702_18917_872994411}[表示路由器向其邻居发送描述自己]{lang="EN-US" style="font-family:宋体"}[LSDB]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loading]{lang="EN-US"}]{#struct_0_x4702_18917_338590756}[表示路由器向邻居发送链路状态请求报文，请求最新的]{style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Full]{lang="EN-US"}]{#struct_0_x4702_18917_69925794}[表示路由器与邻居路由器之间建立起完全邻接关系]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x4702_18917_x663081325}

[[路由器在数据库同步阶段，路由器与邻居协商的主从关系，取值为：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x784886532}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nbr is Master]{lang="EN-US"}]{#struct_0_x4702_18917_1894919846}[表示邻居路由器为主路由器]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Nbr is ]{lang="EN-US"}]{#struct_0_x4702_18917_70122402}[standby]{lang="EN-US"}[表示邻居路由器为从路由器]{lang="EN-US" style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x4702_18917_1005909152}

[[邻居路由器优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_1520450619}

[[DR]{lang="EN-US"}]{#struct_0_x4702_18917_1826632540}

[[接口所属网段的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_70056866}

[[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_x1614021481}

[[接口所属网段的]{style="font-family:宋体"}[BDR]{lang="EN-US"}]{#struct_0_x4702_18917_x1041799660}

[[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_x1676800867}

[[接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_69598115}[的值]{style="font-family:宋体"}

[[Options]{lang="EN-US"}]{#struct_0_x4702_18917_448372700}

[[邻居的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1930641243}[选项，各选项含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x4702_18917_69532579}[：]{lang="EN-US" style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接受能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}]{#struct_0_x4702_18917_x643636176}[：]{lang="EN-US" style="font-family:宋体"}[AS]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[的接受能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[EA]{lang="EN-US"}]{#struct_0_x4702_18917_x2015930896}[：外部扩展属性]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的接受和转发能力]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DC]{lang="EN-US"}]{#struct_0_x4702_18917_69729187}[：支持按需链路]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x4702_18917_1385725844}[：是否支持]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[外部]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_x2093564388}[：非纯末稍区域中的]{lang="EN-US" style="font-family:宋体"}[ABR]{lang="EN-US"}[路由器将]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{lang="EN-US" style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的能力]{lang="EN-US" style="font-family:宋体"}

[[Dead timer due in 33  sec]{lang="EN-US"}]{#struct_0_x4702_18917_69663651}

[[邻居将在]{style="font-family:宋体"}[33]{lang="EN-US"}]{#struct_0_x4702_18917_2115340846}[秒后被认为不可达]{style="font-family:宋体"}

[[Neighbor is up for 02:03:35]{lang="EN-US"}]{#struct_0_x4702_18917_329906173}

[[与邻居建立的时长]{style="font-family:宋体"}[02:03:35]{lang="EN-US"}]{#struct_0_x4702_18917_x101917811}

[[Authentication Sequence]{lang="EN-US"}]{#struct_0_x4702_18917_69860259}

[[验证序列号]{style="font-family:宋体"}]{#struct_0_x4702_18917_x307515945}

[[Neighbor state change count]{lang="EN-US"}]{#struct_0_x4702_18917_632895566}

[[邻居状态发生改变的次数]{style="font-family:宋体"}]{#struct_0_x4702_18917_69794723}

[[BFD status]{lang="EN-US"}]{#struct_0_x4702_18917_69991331}

[[BFD]{lang="EN-US"}]{#struct_0_x4702_18917_x1125717447}[状态，各状态含义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x4702_18917_x830838777}[：未使能]{style="font-family:
  宋体"}[BFD]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Enabled (Control mode)]{lang="EN-US"}]{#struct_0_x4702_18917_69925795}[：已使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[，并处于控制模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled (Echo mode)]{lang="EN-US"}]{#struct_0_x4702_18917_1675570835}[：已使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[，并处于回应模式]{style="font-family:宋体"}

[[Last Neighbor Down Event]{lang="EN-US"}]{#struct_0_x4702_18917_x214118299}

[[最后一次邻居]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4702_18917_1122727659}[事件]{style="font-family:宋体"}

[[Local Address]{lang="EN-US"}]{#struct_0_x4702_18917_x214314907}

[[本端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x214249371}[地址]{style="font-family:宋体"}

[[Remote Address]{lang="EN-US"}]{#struct_0_x4702_18917_x214445979}

[[对端]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x214380443}[地址]{style="font-family:宋体"}

[[Time]{lang="EN-US"}]{#struct_0_x4702_18917_x214577051}

[[邻居]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4702_18917_x214511515}[的时间]{style="font-family:宋体"}

[[Reason]{lang="EN-US"}]{#struct_0_x4702_18917_x213659547}

[[邻居]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4702_18917_x213594011}[的原因]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x715705244}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf peer]{lang="EN-US"}]{#struct_0_x4702_18917_70056867}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 1.1.1.1]{lang="EN-US"}

[               Neighbor Brief Information]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.0]{lang="EN-US"}

[ Router ID       Address         Pri Dead-Time  State             Interface]{lang="EN-US"}

[ []{#OLE_LINK4}[]{#OLE_LINK3}[1.1.1.2         1.1.1.2         1   40         Full/DR           GE1/0/1]{#OLE_LINK2}]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Sham link: 11.11.11.11 -\> 22.22.22.22 ]{lang="EN-US"}

[ Router ID       Address         Pri Dead-Time  State]{lang="EN-US"}

[ 22.22.22.22     22.22.22.22     1   36         Full]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display ospf peer]{lang="EN-US"}]{#struct_0_x4702_18917_342293655}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1968063013}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x439598842}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x52459696}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_69598112}

[[邻居所属的区域]{style="font-family:宋体"}]{#struct_0_x4702_18917_x360931364}

[[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1365666242}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_754725170}

[[Address]{lang="EN-US"}]{#struct_0_x4702_18917_x771449176}

[[邻居接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x1079514862}[地址]{style="font-family:宋体"}

[[Pri]{lang="EN-US"}]{#struct_0_x4702_18917_69532576}

[[邻居路由器优先级]{style="font-family:宋体"}]{#struct_0_x4702_18917_x688266192}

[[Dead-Time]{lang="EN-US"}]{#struct_0_x4702_18917_x2093666954}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_69729184}[的邻居失效时间]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1335263340}

[[与邻居相连的接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_10593742}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_33243883}

[[邻居状态（]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_x4702_18917_1606666424}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[Attempt]{lang="EN-US"}[、]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{style="font-family:宋体"}[Exstart]{lang="EN-US"}[、]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{style="font-family:宋体"}[Loading]{lang="EN-US"}[、]{style="font-family:宋体"}[Full]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Sham link 11.11.11.11 -\> 22.22.22.22]{lang="EN-US"}]{#struct_0_x4702_18917_69663648}

[[源地址为]{style="font-family:宋体"}[11.11.11.11]{lang="EN-US"}]{#struct_0_x4702_18917_x186575469}[、目的地址为]{style="font-family:宋体"}[22.22.22.22]{lang="EN-US"}[的伪连接]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-367869039 .myid}
[]{#_Toc93984781}[]{#_Toc61236317}[]{#_Toc404788008}[]{#struct_0_x4702_18917_x178680876}[]{#_Toc138212553}[]{#_Toc119307763}[]{#_Toc118170392}

**OSPF \-- OSPF配置命令 \-- display ospf peer statistics**

------------------------------------------------------------------------

[**[display ospf peer statistics]{lang="EN-US"}**]{#struct_0_x4702_18917_x1679621438}[命令用来显示本地路由器所有]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[邻居的统计信息，即处于各种状态的邻居数目。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_501590735}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **peer** **statistics**]{lang="EN-US"}]{#struct_0_x4702_18917_259028342}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1807373191}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_760328043}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_822348324}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_69794720}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1429009001}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_915556297}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_560355675}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x707724157}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_386712563}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的邻居统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1176198868}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1403613166}[显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf peer statistics]{lang="EN-US"}]{#struct_0_x4702_18917_x2128096368}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.112]{lang="EN-US"}

[                    Neighbor Statistics]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Area ID         Down Attempt Init 2-Way ExStart Exchange Loading Full Total]{lang="EN-US"}

[  0.0.0.0         0    0       0    0     0       0        0       1    1]{lang="EN-US"}

[  0.0.0.2         0    0       0    0     0       0        0       1    1]{lang="EN-US"}

[  Total           0    0       0    0     0       0        0       2    2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Sham links\' neighbors (Total: 1):]{lang="EN-US"}

[    Down: 0, Init: 0, 2-Way: 0, ExStart: 0, Exchange: 0, Loading: 0, Full: 1]{lang="EN-US"}

[]{#struct_0_x4702_18917_1787584888}[[表1-19 ]{lang="EN-US"}[display ospf peer statistics]{lang="EN-US"}]{#_Ref118114389}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1993343095}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1760081598}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_69925792}

[[Area ID]{lang="EN-US"}]{#struct_0_x4702_18917_483929747}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1476681072}[，显示当前路由器位于该区域所有邻居路由器的状态统计信息]{style="font-family:宋体"}

[[Down]{lang="EN-US"}]{#struct_0_x4702_18917_x445103714}

[[同一个区域内状态为]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_x4702_18917_298163249}[的邻居路由器数目]{style="font-family:宋体"}

[[Attempt]{lang="EN-US"}]{#struct_0_x4702_18917_70122400}

[[同一个区域内状态为]{style="font-family:宋体"}[Attempt]{lang="EN-US"}]{#struct_0_x4702_18917_623572128}[的邻居路由器数目]{style="font-family:宋体"}

[[Init]{lang="EN-US"}]{#struct_0_x4702_18917_x692354580}

[[同一个区域内状态为]{style="font-family:宋体"}[Init]{lang="EN-US"}]{#struct_0_x4702_18917_x1531447225}[的邻居路由器数目]{style="font-family:宋体"}

[[2-Way]{lang="EN-US"}]{#struct_0_x4702_18917_x578992552}

[[同一个区域内状态为]{style="font-family:宋体"}[2-Way]{lang="EN-US"}]{#struct_0_x4702_18917_70056864}[的邻居路由器数目]{style="font-family:宋体"}

[[ExStart]{lang="EN-US"}]{#struct_0_x4702_18917_x1996358505}

[[同一个区域内状态为]{style="font-family:宋体"}[ExStart]{lang="EN-US"}]{#struct_0_x4702_18917_x410197571}[的邻居路由器数目]{style="font-family:宋体"}

[[Exchange]{lang="EN-US"}]{#struct_0_x4702_18917_461653680}

[[同一个区域内状态为]{style="font-family:宋体"}[Exchange]{lang="EN-US"}]{#struct_0_x4702_18917_770431354}[的邻居路由器数目]{style="font-family:宋体"}

[[Loading]{lang="EN-US"}]{#struct_0_x4702_18917_69598113}

[[同一个区域内状态为]{style="font-family:宋体"}[Loading]{lang="EN-US"}]{#struct_0_x4702_18917_1595383772}[的邻居路由器数目]{style="font-family:宋体"}

[[Full]{lang="EN-US"}]{#struct_0_x4702_18917_x969999617}

[[同一个区域内状态为]{style="font-family:宋体"}[Full]{lang="EN-US"}]{#struct_0_x4702_18917_x1206324883}[的邻居路由器数目]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_x4702_18917_1871786532}

[[处于各种状态（]{style="font-family:宋体"}[Down/Attempt/Init/2-Way/ExStart/Exchange/Loading/Full]{lang="EN-US"}]{#struct_0_x4702_18917_69532577}[）邻居路由器的总和]{style="font-family:宋体"}

[[Sham links\' neighbors]{lang="EN-US"}]{#struct_0_x4702_18917_1268048944}

[[sham-link]{lang="EN-US"}]{#struct_0_x4702_18917_x925847816}[邻居统计信息]{style="font-family:宋体"}

[[ ]{lang="EN-US"}]{#_Toc138212554}

::: {#1857749862 .myid}
[]{#_Toc404788009}[]{#struct_0_x4702_18917_807243072}

**OSPF \-- OSPF配置命令 \-- display ospf request-queue**

------------------------------------------------------------------------

[**[display ospf request-queue]{lang="EN-US"}**]{#struct_0_x4702_18917_2130333226}[命令用来显示]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[的请求列表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1683915628}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}[ **request-queue** \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_x4702_18917_69729185}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1003388820}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x684078873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_241671980}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1668360386}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1550210022}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x307616432}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1081006807}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1868668760}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_69663649}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的请求列表信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_x2142890605}[：接口类型和编号。如果未指定本参数，将显示所有接口的请求列表信息。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1345633820}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果未指定本参数，将显示所有邻居路由器的请求列表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x116994313}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2080089455}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[请求列表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf request-queue]{lang="EN-US"}]{#struct_0_x4702_18917_69860257}

[ ]{lang="EN-US"}

[          OSPF Process 100 with Router ID 192.168.1.59]{lang="EN-US"}

[                  Link State Request List]{lang="EN-US"}

[ ]{lang="EN-US"}

[  The Router\'s Neighbor is Router ID 2.2.2.2         Address 10.1.1.2]{lang="EN-US"}

[  Interface 10.1.1.1         Area 0.0.0.0]{lang="EN-US"}

[  Request list:]{lang="EN-US"}

[       Type       LinkState ID      AdvRouter         Sequence   Age]{lang="EN-US"}

[       Router     2.2.2.2           1.1.1.1           80000004   1]{lang="EN-US"}

[       Network    192.168.0.1       1.1.1.1           80000003   1]{lang="EN-US"}

[       Sum-Net    192.168.1.0       1.1.1.1           80000002   2]{lang="EN-US"}

[[表1-20 ]{lang="EN-US"}[d]{lang="EN-US"}]{#struct_0_x4702_18917_x1926124073}[]{#_Toc94753861}[]{#_Toc94671187}[]{#_Toc73952265}[[isplay ospf request-queue]{lang="EN-US"}]{#_Toc68319398}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1989193693}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1274776589}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x419467031}

[[The Router\'s Neighbor is Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1096632121}

[[邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_990670643}

[[Address]{lang="EN-US"}]{#struct_0_x4702_18917_x1820775734}

[[邻居接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_69794721}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_527306135}

[[本地接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_x341790877}[地址]{style="font-family:宋体"}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_2064978288}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1609916126}

[[Request list]{lang="EN-US"}]{#struct_0_x4702_18917_69991329}

[[请求列表信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1162453292}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x271748960}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_614882760}[类型]{style="font-family:宋体"}

[[LinkState ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1823809454}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_69925793}

[[AdvRouter]{lang="EN-US"}]{#struct_0_x4702_18917_x1472385389}

[[发布路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_44712800}

[[Sequence]{lang="EN-US"}]{#struct_0_x4702_18917_283911337}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_70122401}[的序列号]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_x4702_18917_x1332743008}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_634403374}[的老化时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1738531442 .myid}
[]{#_Toc404788010}[]{#struct_0_x4702_18917_x944590414}[]{#_Toc138212555}[]{#_Toc93984782}[]{#_Toc61236318}

**OSPF \-- OSPF配置命令 \-- display ospf retrans-queue**

------------------------------------------------------------------------

[**[display ospf retrans-queue]{lang="EN-US"}**]{#struct_0_x4702_18917_495391024}[命令用来显示]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[的重传列表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1149963969}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}[ **retrans-queue** \[ *interface-type interface-number* \] \[ *neighbor-id* \]]{lang="EN-US"}]{#struct_0_x4702_18917_70056865}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x40043369}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x417170226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1680462360}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1907913291}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1332904613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1978679689}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1660689242}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_146219848}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1635682057}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的重传列表信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_x1788412405}[：接口类型和编号。如果未指定本参数，将显示所有接口的重传列表信息。]{style="font-family:宋体"}

[*[neighbor-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x631156634}[：邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果未指定本参数，将显示所有邻居路由器的重传列表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x706283302}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x370574300}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[重传列表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf retrans-queue]{lang="EN-US"}]{#struct_0_x4702_18917_1635616521}

[ ]{lang="EN-US"}

[          OSPF Process 100 with Router ID 192.168.1.59]{lang="EN-US"}

[                  Link State Retransmission List]{lang="EN-US"}

[ ]{lang="EN-US"}

[  The Router\'s Neighbor is Router ID 192.168.1.111   Address 111.1.1.1]{lang="EN-US"}

[  Interface 111.1.1.2        Area 0.0.0.1]{lang="EN-US"}

[  Retransmit list:]{lang="EN-US"}

[       Type       LinkState ID      AdvRouter         Sequence   Age]{lang="EN-US"}

[       Router     2.2.2.2           2.2.2.2           80000004   1]{lang="EN-US"}

[       Network    12.18.0.1         2.2.2.2           80000003   1]{lang="EN-US"}

[       Sum-Net    12.18.1.0         2.2.2.2           80000002   2]{lang="EN-US"}

[]{#struct_0_x4702_18917_x1371198560}[]{#_Toc94753862}[]{#_Toc94671188}[]{#_Toc73952266}[[表1-21 ]{lang="EN-US"}[display ospf retrans-queue]{lang="EN-US"}]{#_Toc68319399}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1990984783}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1904735542}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x150115692}

[[The Router\'s Neighbor is Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1928680712}

[[邻居路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1721107127}

[[Address]{lang="EN-US"}]{#struct_0_x4702_18917_1635813129}

[[邻居接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_1756334255}[地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1594535222}

[[本地接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_116320821}[地址]{style="font-family:宋体"}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x1292128459}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_2142151462}

[[Retransmit List]{lang="EN-US"}]{#struct_0_x4702_18917_1635747593}

[[重传列表信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_205567727}

[[Type ]{lang="EN-US"}]{#struct_0_x4702_18917_x40507240}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_93849416}[类型]{style="font-family:宋体"}

[[LinkState ID]{lang="EN-US"}]{#struct_0_x4702_18917_1635944201}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x567131769}

[[AdvRouter]{lang="EN-US"}]{#struct_0_x4702_18917_x1058695847}

[[发布路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_x2099686896}

[[Sequence]{lang="EN-US"}]{#struct_0_x4702_18917_1057551778}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1635878665}[的序列号]{style="font-family:宋体"}

[[Age]{lang="EN-US"}]{#struct_0_x4702_18917_x1413433104}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x853037872}[的老化时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#558770551 .myid}
[]{#_Toc404788011}[]{#struct_0_x4702_18917_x1708670619}[]{#_Toc138212556}[]{#_Toc93984783}[]{#_Toc61236319}

**OSPF \-- OSPF配置命令 \-- display ospf routing**

------------------------------------------------------------------------

[**[display ospf routing]{lang="EN-US"}**]{#struct_0_x4702_18917_156876630}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_673320716}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **routing** ]{lang="EN-US"}]{#struct_0_x4702_18917_1636075273}[[\[ *ip-address* { *mask-length* \| *mask* } \] ]{lang="EN-US"}]{#OLE_LINK1}[\[ ]{lang="EN-US"}**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*[ \]]{lang="EN-US"}[ \[ **nexthop** *nexthop-address* \] \[ **verbose** \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_485281306}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1365684431}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1647303181}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x370321858}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x408056440}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_975231408}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1787719895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1636009737}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1964131674}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的路由表信息。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x1748318133}[：路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x4702_18917_x1818454841}[：网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x4702_18917_661127209}[：网络掩码，点分十进制格式。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_x36504018}[：显示指定出接口的路由信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为接口类型和编号。如果未指定本参数，将显示所有接口的路由表信息。]{style="font-family:
宋体"}

[**[nexthop ]{lang="EN-US"}***[nexthop-address]{lang="EN-US"}*]{#struct_0_x4702_18917_1536434264}[：显示指定下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的路由信息。如果未指定本参数，将显示所有的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由表信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x1161280984}[：显示路由表详细信息。]{style="font-family:宋体"}[如果未指定本参数，将显示路由表的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1636206345}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1885787094}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由表的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf routing]{lang="EN-US"}]{#struct_0_x4702_18917_748948184}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.112]{lang="EN-US"}

[                   Routing Tables]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing for Network]{lang="EN-US"}

[ Destination        Cost     Type    NextHop         AdvRouter       Area]{lang="EN-US"}

[ 192.168.1.0/24     1562     Stub    192.168.1.2     192.168.1.2     0.0.0.0]{lang="EN-US"}

[ 172.16.0.0/16      1563     Inter   192.168.1.1     192.168.1.1     0.0.0.0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total nets: 2]{lang="EN-US"}

[ Intra area: 1  Inter area: 1  ASE: 0  NSSA: 0]{lang="EN-US"}

[]{#struct_0_x4702_18917_x443428449}[]{#_Toc94753863}[]{#_Toc94671189}[]{#_Toc73952267}[[表1-22 ]{lang="EN-US"}[display ospf routing]{lang="EN-US"}]{#_Toc68319400}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1986525425}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_773240362}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1636140809}

[[Destination]{lang="EN-US"}]{#struct_0_x4702_18917_x669969157}

[[目的网络]{style="font-family:宋体"}]{#struct_0_x4702_18917_411824486}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_1498333910}

[[到达目的地址的开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_103676672}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_1635682058}

[[路由类型（]{style="font-family:宋体"}[Intra-area]{lang="EN-US"}]{#struct_0_x4702_18917_x1788740085}[、]{style="font-family:宋体"}[Transit]{lang="EN-US"}[、]{style="font-family:宋体"}[Stub]{lang="EN-US"}[、]{style="font-family:宋体"}[Inter-Area]{lang="EN-US"}[、]{style="font-family:宋体"}[ Type1 External]{lang="EN-US"}[和]{style="font-family:宋体"}[Type2 External]{lang="EN-US"}[）]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x4702_18917_981464295}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_x4702_18917_1430534480}

[[AdvRouter]{lang="EN-US"}]{#struct_0_x4702_18917_1389052436}

[[发布路由器]{style="font-family:宋体"}]{#struct_0_x4702_18917_1635616522}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_x1371395168}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x289367534}

[[Total nets]{lang="EN-US"}]{#struct_0_x4702_18917_540254813}

[[区域内部、区域间、]{style="font-family:宋体"}[ASE]{lang="EN-US"}]{#struct_0_x4702_18917_2137241634}[和]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的路由总数]{style="font-family:宋体"}

[[Intra area]{lang="EN-US"}]{#struct_0_x4702_18917_1635813130}

[[区域内部路由总数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1755744432}

[[Inter area]{lang="EN-US"}]{#struct_0_x4702_18917_x694005184}

[[区域间路由总数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1060209417}

[[ASE]{lang="EN-US"}]{#struct_0_x4702_18917_1635747594}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_205764335}[区域外路由总数]{style="font-family:宋体"}

[[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_x548291834}

[[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_x262503099}[区域路由总数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1671266561}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由表的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf routing verbose]{lang="EN-US"}]{#struct_0_x4702_18917_1635944202}

[ ]{lang="EN-US"}

[          OSPF Process 2 with Router ID 192.168.1.112]{lang="EN-US"}

[                   Routing Tables]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing for Network]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: 192.168.1.0/24]{lang="EN-US"}

[    Priority: Low                     Type: Stub]{lang="EN-US"}

[   AdvRouter: 192.168.1.2             Area: 0.0.0.0]{lang="EN-US"}

[  SubProtoID: 0x1               Preference: 10]{lang="EN-US"}

[     NextHop: 192.168.1.2        BkNextHop: N/A]{lang="EN-US"}

[      IfType: Broadcast           BkIfType: N/A]{lang="EN-US"}

[   Interface: GE1/0/2          BkInterface: N/A]{lang="EN-US"}

[       NibID: 0x1300000c            Status: Normal]{lang="EN-US"}

[        Cost: 1562]{lang="EN-US"}

[ ]{lang="EN-US"}

[Destination: 172.16.0.0/16]{lang="EN-US"}

[    Priority: Low                     Type: Inter]{lang="EN-US"}

[   AdvRouter: 192.168.1.1             Area: 0.0.0.0]{lang="EN-US"}

[  SubProtoID: 0x1               Preference: 10]{lang="EN-US"}

[     NextHop: 192.168.1.1        BkNextHop: N/A]{lang="EN-US"}

[      IfType: Broadcast           BkIfType: N/A]{lang="EN-US"}

[   Interface: GE1/0/3          BkInterface: N/A]{lang="EN-US"}

[       NibID: 0x1300000c            Status: Normal]{lang="EN-US"}

[        Cost: 1563                 SpfCost: 65535]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Total nets: 2]{lang="EN-US"}

[ Intra area: 2  Inter Area: 0  ASE: 0  NSSA: 0]{lang="EN-US"}

[[表1-23 ]{lang="EN-US"}[display ospf routing verbose]{lang="EN-US"}]{#struct_0_x4702_18917_x566935161}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1982506553}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1635878666}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1413367568}

[[Priority]{lang="EN-US"}]{#struct_0_x4702_18917_x129159015}

[[前缀优先级，取值为：]{style="font-family:宋体"}[Critical]{lang="EN-US"}]{#struct_0_x4702_18917_x77325751}[、]{style="font-family:宋体"}[High]{lang="EN-US"}[、]{style="font-family:宋体"}[Medium]{lang="EN-US"}[和]{style="font-family:宋体"}[Low]{lang="EN-US"}

 

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_462252138}

[[路由类型（]{style="font-family:宋体"}[Intra-area]{lang="EN-US"}]{#struct_0_x4702_18917_462317674}[、]{style="font-family:宋体"}[Transit]{lang="EN-US"}[、]{style="font-family:宋体"}[Stub]{lang="EN-US"}[、]{style="font-family:宋体"}[Inter-Area]{lang="EN-US"}[、]{style="font-family:宋体"}[ Type1 External]{lang="EN-US"}[和]{style="font-family:宋体"}[Type2 External]{lang="EN-US"}[）]{style="font-family:宋体"}

 

[[AdvRouter]{lang="EN-US"}]{#struct_0_x4702_18917_461858922}

[[发布路由器]{style="font-family:宋体"}]{#struct_0_x4702_18917_461924458}

 

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_461989994}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_462055530}

 

[[SubProtoID]{lang="EN-US"}]{#struct_0_x4702_18917_x503101212}

[[子协议]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_1636075274}

[[Preference]{lang="EN-US"}]{#struct_0_x4702_18917_484822554}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1532112568}[路由优先级]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x4702_18917_1492336096}

[[主下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_156123647}[地址]{style="font-family:宋体"}

[[BkNextHop]{lang="EN-US"}]{#struct_0_x4702_18917_1636009738}

[[备份下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_1964852570}[地址]{style="font-family:宋体"}

[[IfType]{lang="EN-US"}]{#struct_0_x4702_18917_x604554241}

[[路由主下一跳网络类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_1511834546}

[[BkIfType]{lang="EN-US"}]{#struct_0_x4702_18917_267114124}

[[路由备份下一跳网络类型]{style="font-family:宋体"}]{#struct_0_x4702_18917_1636206346}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_x1885590486}

[[路由出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_216400609}

[[BkInterface]{lang="EN-US"}]{#struct_0_x4702_18917_x1876360474}

[[路由备份出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2118065890}

[[NibID]{lang="EN-US"}]{#struct_0_x4702_18917_1636140810}

[[路由下一跳信息的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x669379334}[值]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x4702_18917_791802050}

[[路由状态，具体如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x267916385}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Local]{lang="EN-US"}]{#struct_0_x4702_18917_1635682055}[：该条路由在本地，未发送给路由管理模块]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x4702_18917_x1788543477}[：路由下一跳无效]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Stale]{lang="EN-US"}]{#struct_0_x4702_18917_x2021859815}[：该路由下一跳较旧]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_x4702_18917_x538692682}[：正常可用状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Delete]{lang="EN-US"}]{#struct_0_x4702_18917_1635616519}[：处于删除状态]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Host-Adv]{lang="EN-US"}]{#struct_0_x4702_18917_x1370674269}[：该条路由为主机路由]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Rely]{lang="EN-US"}]{#struct_0_x4702_18917_845173215}[：该条路由为迭代路由]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_462121065}

[[到达目的地址的开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_462186601}

[[SpfCost]{lang="EN-US"}]{#struct_0_x4702_18917_462252137}

[[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_462317673}[开销]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2082217874 .myid}
[]{#_Toc138212557}[]{#_Toc93984784}[]{#_Toc61236320}[]{#_Toc61093111}[]{#_Toc58812044}[]{#_Toc56887173}[]{#_Toc45164788}[]{#_Toc404788012}[]{#struct_0_x4702_18917_1480611164}[]{#_Toc348020469}[]{#_Toc340222299}

**OSPF \-- OSPF配置命令 \-- display ospf spf-tree**

------------------------------------------------------------------------

[**[display ospf spf-tree]{lang="EN-US"}**]{#struct_0_x4702_18917_x1800868923}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域中的拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1635813127}

[**[display]{lang="EN-US"}**[ **ospf** \[ *process-id* \] \[ **area** *area-id* \] **spf-tree** \[ **verbose** \]]{lang="EN-US"}]{#struct_0_x4702_18917_1755416751}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_483944679}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x732227745}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1833401317}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1133396212}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1491013982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1318387462}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_1635747591}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_205436655}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_328227910}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的区域拓扑信息。]{style="font-family:宋体"}

[**[area]{lang="EN-US"}**]{#struct_0_x4702_18917_x1750122895}*[ area-id]{lang="EN-US"}*[：]{style="font-family:宋体"}[显示指定区域]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[拓扑信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[area-id]{lang="EN-US"}*[表示区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*如果未指定本参数，将显示所有区域的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x4702_18917_x471920658}[：显示]{style="font-family:宋体"}[spf-tree]{lang="EN-US"}[的详细信息。如果未指定本参数，将显示]{style="font-family:宋体"}[spf-tree]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_23921377}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x737559255}[显示进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下区域]{style="font-family:宋体"}[0]{lang="EN-US"}[内的最短路径树。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 area 0 spf-tree]{lang="EN-US"}]{#struct_0_x4702_18917_x450327964}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 100.0.0.4]{lang="EN-US"}

[ ]{lang="EN-US"}

[        Flags: S-Node is on SPF tree       R-Node is directly reachable]{lang="EN-US"}

[               I-Node or Link is init      D-Node or Link is to be deleted]{lang="EN-US"}

[               P-Neighbor is parent        A-Node is in candidate list]{lang="EN-US"}

[               C-Neighbor is child         T-Node is tunnel destination]{lang="EN-US"}

[               H-Nexthop changed           N-Link is a new path]{lang="EN-US"}

[               V-Link is involved          G-Link is in change list]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Area: 0.0.0.0  Shortest Path Tree]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode         Type    Flag      SpfLink         Type   Cost  Flag]{lang="EN-US"}

[\>192.168.119.130 Network S R]{lang="EN-US"}

[                                \--\>114.114.114.111 NET2RT 0     C]{lang="EN-US"}

[                                \--\>100.0.0.4       NET2RT 0     P]{lang="EN-US"}

[\>114.114.114.111 Router  S]{lang="EN-US"}

[                                \--\>192.168.119.130 RT2NET 65535 P]{lang="EN-US"}

[\>100.0.0.4       Router  S]{lang="EN-US"}

[                                \--\>192.168.119.130 RT2NET 10    C]{lang="EN-US"}

[[表1-24 ]{lang="EN-US"}[display ospf spf-tree]{lang="EN-US"}]{#struct_0_x4702_18917_485150234}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2011568811}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1642649857}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_673495482}

[[SpfNode]{lang="EN-US"}]{#struct_0_x4702_18917_799811022}

[[spf]{lang="EN-US"}]{#struct_0_x4702_18917_323501834}[节点，若节点类型为路由器，则为路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[；若节点类型为网络，则为该网络]{style="font-family:宋体"}[DR]{lang="EN-US"}[接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。其中，]{style="font-family:宋体"}[Type]{lang="EN-US"}[为节点类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Network]{lang="EN-US"}]{#struct_0_x4702_18917_1636009735}[：表示网络节点]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x4702_18917_1964000602}[：表示路由器节点]{style="font-family:
  宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_x4702_18917_x188984372}[为节点标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x4702_18917_x1125050442}[：节点处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x4702_18917_x758657286}[：节点在候选列表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x4702_18917_x1360674155}[：节点在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x4702_18917_1636206343}[：该节点与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x4702_18917_x1885393878}[：该节点将被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x4702_18917_1307794021}[：该节点为隧道的终点]{style="font-family:宋体"}

[[SpfLink]{lang="EN-US"}]{#struct_0_x4702_18917_x87530657}

[[spf]{lang="EN-US"}]{#struct_0_x4702_18917_x650854969}[链路，其值表示对端节点。其中，]{style="font-family:宋体"}[Cost]{lang="EN-US"}[为链路开销，]{style="font-family:宋体"}[Type]{lang="EN-US"}[为链路类型：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RT2RT]{lang="EN-US"}]{#struct_0_x4702_18917_x1744494434}[：表示路由器到路由器链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[NET2RT]{lang="EN-US"}]{#struct_0_x4702_18917_1636140807}[：表示网络到路由器链路]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RT2NET]{lang="EN-US"}]{#struct_0_x4702_18917_x669051653}[：表示路由器到网络链路]{style="font-family:
  宋体"}

[[Flag]{lang="EN-US"}]{#struct_0_x4702_18917_x1577085705}[为链路标志：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x4702_18917_934908192}[：链路处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_1635682056}[：目的节点是父节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x4702_18917_x1788346869}[：目的节点是子节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x4702_18917_x176306341}[：链路将要被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x4702_18917_x1875395132}[：下一跳发生改变]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_x4702_18917_x796767771}[：目的节点删除或者是新增节点时，链路的目的节点不在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上或处于删除状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x4702_18917_1635616520}[：新增链路，并且源节点和目的节点都在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_x4702_18917_x1371264096}[：链路在区域变化列表中]{style="font-family:宋体"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x121610652}[显示进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下区域]{style="font-family:宋体"}[0]{lang="EN-US"}[内的最短路径树详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf 1 area 0 spf-tree verbose]{lang="EN-US"}]{#struct_0_x4702_18917_x450327959}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 100.0.0.4]{lang="EN-US"}

[ ]{lang="EN-US"}

[        Flags: S-Node is on SPF tree       R-Node is directly reachable]{lang="EN-US"}

[               I-Node or Link is init      D-Node or Link is to be deleted]{lang="EN-US"}

[               P-Neighbor is parent        A-Node is in candidate list]{lang="EN-US"}

[               C-Neighbor is child         T-Node is tunnel destination]{lang="EN-US"}

[               H-Nexthop changed           N-Link is a new path]{lang="EN-US"}

[               V-Link is involved          G-Link is in change list]{lang="EN-US"}

[ ]{lang="EN-US"}

[                  Area: 0.0.0.0  Shortest Path Tree]{lang="EN-US"}

[ ]{lang="EN-US"}

[\>LsId(192.168.119.130)]{lang="EN-US"}

[ AdvId    : 100.0.0.4       NodeType     : Network]{lang="EN-US"}

[ Mask     : 255.255.255.0   SPFLinkCnt   : 2]{lang="EN-US"}

[ Distance : 10]{lang="EN-US"}

[ VlinkData: 0.0.0.0         ParentLinkCnt: 1           NodeFlag: S R]{lang="EN-US"}

[ NextHop  : 1]{lang="EN-US"}

[   192.168.119.130    Interface: GE1/0/2]{lang="EN-US"}

[ BkNextHop: 1]{lang="EN-US"}

[   0.0.0.0            Interface: GE1/0/2]{lang="EN-US"}

[ \--\>LinkId(114.114.114.111)]{lang="EN-US"}

[    AdvId   : 100.0.0.4       LinkType   : NET2RT]{lang="EN-US"}

[    LsId    : 192.168.119.130 LinkCost   : 0           NextHopCnt: 1]{lang="EN-US"}

[    LinkData: 0.0.0.0         LinkNewCost: 0           LinkFlag  : C]{lang="EN-US"}

[ \--\>LinkId(100.0.0.4)]{lang="EN-US"}

[    AdvId   : 100.0.0.4       LinkType   : NET2RT]{lang="EN-US"}

[    LsId    : 192.168.119.130 LinkCost   : 0           NextHopCnt: 1]{lang="EN-US"}

[    LinkData: 0.0.0.0         LinkNewCost: 0           LinkFlag  : P]{lang="EN-US"}

[[表1-25 ]{lang="EN-US"}[display ospf spf-tree verbose]{lang="EN-US"}]{#struct_0_x4702_18917_2011725199}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2006684989}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1204332979}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_x337921084}

[[LsId]{lang="EN-US"}]{#struct_0_x4702_18917_1635878664}

[[链路状态]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1413498640}

[[AdvId]{lang="EN-US"}]{#struct_0_x4702_18917_x515467561}

[[通告路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1544206531}

[[NodeType]{lang="EN-US"}]{#struct_0_x4702_18917_1205745976}

[[节点类型，其中：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1636075272}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Network]{lang="EN-US"}]{#struct_0_x4702_18917_485215770}[：表示网络节点]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Router]{lang="EN-US"}]{#struct_0_x4702_18917_987750256}[：表示路由器节点]{style="font-family:
  宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_x4702_18917_56966076}

[[网络掩码，若为路由器节点掩码为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4702_18917_x1013400307}

[[SPFLinkCnt]{lang="EN-US"}]{#struct_0_x4702_18917_1636009736}

[[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_1964197210}[链路个数]{style="font-family:宋体"}

[[Distance]{lang="EN-US"}]{#struct_0_x4702_18917_988120043}

[[表示到根节点的开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1768254151}

[[VlinkData]{lang="EN-US"}]{#struct_0_x4702_18917_x107059110}

[[Vlink]{lang="EN-US"}]{#struct_0_x4702_18917_1636206344}[报文的目的地址]{style="font-family:宋体"}

[[ParentLinkCnt]{lang="EN-US"}]{#struct_0_x4702_18917_x1885721558}

[[父链路个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1067214931}

[[NodeFlag]{lang="EN-US"}]{#struct_0_x4702_18917_1709254263}

[[节点标志：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1636140808}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x4702_18917_x669903621}[：节点处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[A]{lang="EN-US"}]{#struct_0_x4702_18917_x420905093}[：节点在候选列表上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x4702_18917_x710171659}[：节点在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x4702_18917_521756025}[：该节点与根节点直连]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x4702_18917_1635682053}[：该节点将被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x4702_18917_144994607}[：该节点为隧道的终点]{style="font-family:宋体"}

[[NextHop]{lang="EN-US"}]{#struct_0_x4702_18917_x1788150261}

[[下一跳信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_508468716}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_164283655}

[[出接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_1635616517}

[[BkNextHop]{lang="EN-US"}]{#struct_0_x4702_18917_x1371591773}

[[备份下一跳信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1597746427}

[[LinkId]{lang="EN-US"}]{#struct_0_x4702_18917_1635813125}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_1755547823}

[[LinkType]{lang="EN-US"}]{#struct_0_x4702_18917_1710289970}

[[链路类型，其中：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1425525338}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RT2RT]{lang="EN-US"}]{#struct_0_x4702_18917_1635747589}[：表示路由器到路由器链路]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[NET2RT]{lang="EN-US"}]{#struct_0_x4702_18917_204912368}[：表示网络到路由器链路]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[RT2NET]{lang="EN-US"}]{#struct_0_x4702_18917_x2043362719}[：表示路由器到网络链路]{style="font-family:
  宋体"}

[[LinkCost]{lang="EN-US"}]{#struct_0_x4702_18917_2089803372}

[[当前链路开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_1635944197}

[[NextHopCnt]{lang="EN-US"}]{#struct_0_x4702_18917_1007239566}

[[下一跳个数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1017462177}

[[LinkData]{lang="EN-US"}]{#struct_0_x4702_18917_1635878661}

[[链路数据]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1413170960}

[[LinkNewCost]{lang="EN-US"}]{#struct_0_x4702_18917_1817557632}

[[新的链路开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_1636075269}

[[LinkFlag]{lang="EN-US"}]{#struct_0_x4702_18917_484625945}

[[链路标志：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x259831667}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x4702_18917_x872448400}[：链路处于初始化状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x4702_18917_1636009733}[：目的节点是父节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x4702_18917_1964393818}[：目的节点是子节点]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x4702_18917_1809953217}[：链路将要被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x4702_18917_1636206341}[：下一跳发生改变]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_x4702_18917_x1885524950}[：目的节点删除或者是新增节点时，链路的目的节点不在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上或处于删除状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x4702_18917_2088570159}[：新增链路，并且源节点和目的节点都在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[树上]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[G]{lang="EN-US"}]{#struct_0_x4702_18917_1636140805}[：链路在区域变化列表中]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#329218817 .myid}
[]{#_Toc404788013}[]{#struct_0_x4702_18917_x669182725}[]{#_Toc348020470}[]{#_Toc343703154}

**OSPF \-- OSPF配置命令 \-- display ospf statistics**

------------------------------------------------------------------------

[**[display ospf statistics]{lang="EN-US"}**]{#struct_0_x4702_18917_x1217328648}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x574547832}

[**[display ospf ]{lang="EN-US"}**[\[ *process-id* \] **statistics** \[ **error** \| **packet** \[ *interface-type* *interface-number* \] \]]{lang="EN-US"}]{#struct_0_x4702_18917_x809481881}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2115921413}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1635682054}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1788477941}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x532276601}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x1289881414}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1416553706}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x2096099473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_999332049}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1127380705}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[**[error]{lang="EN-US"}**]{#struct_0_x4702_18917_1635616518}[：显示错误统计信息。如果未指定本参数，将显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的报文、]{style="font-family:宋体"}[LSA]{lang="EN-US"}[和路由的统计信息。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_x4702_18917_1987468806}[：]{style="font-family:宋体"}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_756011542}[：接口类型和编号]{style="font-family:宋体"}[。显示指定接口的统计信息。如果未指定本参数，将显示所有接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1370739805}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_770350933}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf statistics]{lang="EN-US"}]{#struct_0_x4702_18917_1635813126}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 2.2.2.2]{lang="EN-US"}

[                  Statistics]{lang="EN-US"}

[ ]{lang="EN-US"}

[ I/O statistics]{lang="EN-US"}

[  Type                      Input     Output]{lang="EN-US"}

[  Hello                     61        122]{lang="EN-US"}

[  DB Description            2          3]{lang="EN-US"}

[  Link-State Req            1          1]{lang="EN-US"}

[  Link-State Update         3          3]{lang="EN-US"}

[  Link-State Ack            3          2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ LSAs originated by this router]{lang="EN-US"}

[  Router  : 4]{lang="EN-US"}

[  ]{lang="EN-US"}[Network : 0]{lang="PT-BR"}

[  Sum-Net : 0]{lang="PT-BR"}

[  Sum-Asbr: 0]{lang="PT-BR"}

[  External: 0]{lang="PT-BR"}

[  NSSA    : 0]{lang="PT-BR"}

[  ]{lang="PT-BR"}[Opq-Link: 0]{lang="EN-US"}

[  Opq-Area: 0]{lang="EN-US"}

[  Opq-As  : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ LSAs originated: 4  LSAs received: 7]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Routing table:]{lang="EN-US"}

[   Intra area: 2  Inter area: 3  ASE/NSSA: 0]{lang="EN-US"}

[[表1-26 ]{lang="EN-US"}[display ospf statistics]{lang="EN-US"}]{#struct_0_x4702_18917_1755351215}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_2004563437}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1484345193}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_860295341}

[[I/O statistics]{lang="EN-US"}]{#struct_0_x4702_18917_103205375}

[[收发的报文和]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1635747590}[的详细统计信息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_205502191}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x795958282}[报文类型]{style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_x4702_18917_x287604295}

[[接收报文数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1101862815}

[[Output]{lang="EN-US"}]{#struct_0_x4702_18917_1635944198}

[[发送报文数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1006387598}

[[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x1353809449}

[[OSPF Hello]{lang="EN-US"}]{#struct_0_x4702_18917_401084591}[报文]{style="font-family:宋体"}

[[DB Description]{lang="EN-US"}]{#struct_0_x4702_18917_1152732300}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1635878662}[数据库描述报文]{style="font-family:宋体"}

[[Link-State Req]{lang="EN-US"}]{#struct_0_x4702_18917_x1413105424}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1256689166}[链路状态请求报文]{style="font-family:宋体"}

[[Link-State Update]{lang="EN-US"}]{#struct_0_x4702_18917_803558662}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1759528235}[链路状态更新报文]{style="font-family:宋体"}

[[Link-State Ack]{lang="EN-US"}]{#struct_0_x4702_18917_1636075270}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_485084698}[链路状态确认报文]{style="font-family:宋体"}

[[LSAs originated by this router]{lang="EN-US"}]{#struct_0_x4702_18917_x1995287812}

[[本路由器发布]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1842085041}[的详细统计信息]{style="font-family:宋体"}

[[Router]{lang="EN-US"}]{#struct_0_x4702_18917_1636009734}

[[生成]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1964066138}[的数目]{style="font-family:宋体"}

[[Network]{lang="EN-US"}]{#struct_0_x4702_18917_957091695}

[[生成]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x586281060}[的数目]{style="font-family:宋体"}

[[Sum-Net]{lang="EN-US"}]{#struct_0_x4702_18917_1636206342}

[[生成]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1885328342}[的数目]{style="font-family:宋体"}

[[Sum-Asbr]{lang="EN-US"}]{#struct_0_x4702_18917_x667343889}

[[生成]{style="font-family:宋体"}[Type-4 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_900824779}[的数目]{style="font-family:宋体"}

[[External]{lang="PT-BR"}]{#struct_0_x4702_18917_1636140806}

[[生成]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x668986117}[的数目]{style="font-family:宋体"}

[[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_1089068361}

[[生成]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1868616352}[的数目]{style="font-family:宋体"}

[[Opq-Link]{lang="PT-BR"}]{#struct_0_x4702_18917_x736970938}

[[生成]{style="font-family:宋体"}[Type-]{lang="EN-US"}]{#struct_0_x4702_18917_1433068280}[9]{lang="PT-BR"}[ LSA]{lang="EN-US"}[的数目]{style="font-family:宋体"}

[[Opq-Area]{lang="PT-BR"}]{#struct_0_x4702_18917_1220721131}

[[生成]{style="font-family:宋体"}[Type-]{lang="EN-US"}]{#struct_0_x4702_18917_x193681379}[10]{lang="PT-BR"}[ LSA]{lang="EN-US"}[的数目]{style="font-family:
  宋体"}

[[Opq-As]{lang="PT-BR"}]{#struct_0_x4702_18917_x737036474}

[[生成]{style="font-family:宋体"}[Type-]{lang="EN-US"}]{#struct_0_x4702_18917_x512362377}[11 LSA]{lang="PT-BR"}[的数目]{style="font-family:宋体"}

[[LSA originated]{lang="EN-US"}]{#struct_0_x4702_18917_2102126878}

[[生成的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x736839866}[的总数]{style="font-family:宋体"}

[[LSA received]{lang="EN-US"}]{#struct_0_x4702_18917_1024201553}

[[接收的]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1244833984}[的总数]{style="font-family:宋体"}

[[Routing table]{lang="EN-US"}]{#struct_0_x4702_18917_1660145211}

[[路由表信息]{style="font-family:宋体"}]{#struct_0_x4702_18917_x736905402}

[[Intra area]{lang="EN-US"}]{#struct_0_x4702_18917_646814704}

[[区域内路由的数量]{style="font-family:宋体"}]{#struct_0_x4702_18917_1651336743}

[[Inter area]{lang="EN-US"}]{#struct_0_x4702_18917_x736708794}

[[区域间路由的数量]{style="font-family:宋体"}]{#struct_0_x4702_18917_188188564}

[[ASE]{lang="EN-US"}]{#struct_0_x4702_18917_x609108619}

[[ASE]{lang="EN-US"}]{#struct_0_x4702_18917_x736774330}[路由的数量]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1019678790}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的错误统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf statistics error]{lang="EN-US"}]{#struct_0_x4702_18917_x736577722}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 192.168.1.112]{lang="EN-US"}

[                  OSPF Packet Error Statistics]{lang="EN-US"}

[ ]{lang="EN-US"}

[0         : Router ID confusion        0         : Bad packet]{lang="EN-US"}

[ 0         : Bad version                0         : Bad checksum]{lang="EN-US"}

[ 0         : Bad area ID                0         : Drop on unnumbered link]{lang="EN-US"}

[ 0         : Bad virtual link           0         : Bad authentication type]{lang="EN-US"}

[ 0         : Bad authentication key     0         : Packet too small]{lang="EN-US"}

[ 0         : Neighbor state low         0         : Transmit error]{lang="EN-US"}

[ 0         : Interface down             0         : Unknown neighbor]{lang="EN-US"}

[ 0         : HELLO: Netmask mismatch    0         : HELLO: Hello-time mismatch]{lang="EN-US"}

[ 0         : HELLO: Dead-time mismatch  0         : HELLO: Ebit option mismatch]{lang="EN-US"}

[ 0         : DD: MTU option mismatch    0         : DD: Unknown LSA type]{lang="EN-US"}

[ 0         : DD: Ebit option mismatch   0         : ACK: Bad ack]{lang="EN-US"}

[ 0         : ACK: Unknown LSA type      0         : REQ: Empty request]{lang="EN-US"}

[ 0         : REQ: Bad request           0         : UPD: LSA checksum bad]{lang="EN-US"}

[ 0         : UPD: Unknown LSA type      0         : UPD: Less recent LSA]{lang="EN-US"}

[[表1-27 ]{lang="EN-US"}[display ospf statistics error]{lang="EN-US"}]{#struct_0_x4702_18917_218399908}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1999642321}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_905853283}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1956534623}

[[Router ID confusion]{lang="EN-US"}]{#struct_0_x4702_18917_110449152}

[[含有重复路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x736643258}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Bad packet]{lang="EN-US"}]{#struct_0_x4702_18917_x550348940}

[[非法的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_872781595}[报文数]{style="font-family:宋体"}

[[Bad version]{lang="EN-US"}]{#struct_0_x4702_18917_x289738590}

[[错误版本号的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_594190398}[报文数]{style="font-family:宋体"}

[[Bad checksum]{lang="EN-US"}]{#struct_0_x4702_18917_x736446650}

[[校验和出错的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_617085281}[报文数]{style="font-family:宋体"}

[[Bad area ID]{lang="EN-US"}]{#struct_0_x4702_18917_x678755903}

[[非法的区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_61038706}[的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[Drop on unnumbered link]{lang="EN-US"}]{#struct_0_x4702_18917_479662928}

[[在地址借用链路上丢弃的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736512186}[报文数]{style="font-family:宋体"}

[[Bad virtual link]{lang="EN-US"}]{#struct_0_x4702_18917_x158217295}

[[错误的虚链路的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x925318751}[报文数]{style="font-family:宋体"}

[[Bad authentication type]{lang="EN-US"}]{#struct_0_x4702_18917_x55990828}

[[含有非法验证类型的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736970937}[报文数]{style="font-family:宋体"}

[[Bad authentication key]{lang="EN-US"}]{#struct_0_x4702_18917_1433395960}

[[含有错误验证码的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_890621493}[报文数]{style="font-family:宋体"}

[[Packet too small]{lang="EN-US"}]{#struct_0_x4702_18917_x615509980}

[[报文长度太小的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x295828798}[报文数]{style="font-family:宋体"}

[[Neighbor state low]{lang="EN-US"}]{#struct_0_x4702_18917_x737036473}

[[在低邻居状态收到的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x512558985}[报文数]{style="font-family:宋体"}

[[Transmit error]{lang="EN-US"}]{#struct_0_x4702_18917_1699051357}

[[传输出错的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_391570454}[报文数]{style="font-family:宋体"}

[[Interface down]{lang="EN-US"}]{#struct_0_x4702_18917_x736839865}

[[接口]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x4702_18917_1024004945}[的计数]{style="font-family:宋体"}

[[Unknown neighbor]{lang="EN-US"}]{#struct_0_x4702_18917_x1808309896}

[[未知的邻居发来的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736905401}[报文数]{style="font-family:宋体"}

[[HELLO: Netmask mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_646749168}

[[网络掩码不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_1473030758}[报文数]{style="font-family:宋体"}

[[HELLO: Hello-time mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_x1284295414}

[[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x736708793}[定时器不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[HELLO: Dead-time mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_188647316}

[[Dead]{lang="EN-US"}]{#struct_0_x4702_18917_x1385299375}[定时器不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[HELLO: Ebit option mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_x2122986150}

[[Option]{lang="EN-US"}]{#struct_0_x4702_18917_x736774329}[字段]{style="font-family:宋体"}[E]{lang="EN-US"}[位不匹配的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DD: MTU option mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_1019088967}

[[MTU]{lang="EN-US"}]{#struct_0_x4702_18917_x1821332989}[不匹配的]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[DD: Unknown LSA type]{lang="EN-US"}]{#struct_0_x4702_18917_x736577721}

[[DD]{lang="EN-US"}]{#struct_0_x4702_18917_218203300}[报文中描述未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[DD: Ebit option mismatch]{lang="EN-US"}]{#struct_0_x4702_18917_x663095722}

[[Option]{lang="EN-US"}]{#struct_0_x4702_18917_x736643257}[字段]{style="font-family:宋体"}[E]{lang="EN-US"}[位不匹配的]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[ACK: Bad ack]{lang="EN-US"}]{#struct_0_x4702_18917_x550414476}

[[收到不匹配的]{style="font-family:宋体"}[ack]{lang="EN-US"}]{#struct_0_x4702_18917_896802851}[数目]{style="font-family:宋体"}

[[ACK: Unknown LSA type]{lang="EN-US"}]{#struct_0_x4702_18917_x736446649}

[[收到]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_617675104}[类型未知的]{style="font-family:宋体"}[ack]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[REQ: Empty request]{lang="EN-US"}]{#struct_0_x4702_18917_2057216476}

[[不含有任何请求信息的]{style="font-family:宋体"}[LSR]{lang="EN-US"}]{#struct_0_x4702_18917_1820941479}[报文数]{style="font-family:宋体"}

[[REQ: Bad request]{lang="EN-US"}]{#struct_0_x4702_18917_x736512185}

[[请求错误]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x158151759}[的]{style="font-family:宋体"}[LSR]{lang="EN-US"}[报文数]{style="font-family:宋体"}

[[UPD: LSA checksum bad]{lang="EN-US"}]{#struct_0_x4702_18917_x166298264}

[[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_x736970940}[报文中]{style="font-family:宋体"}[LSA]{lang="EN-US"}[校验和出错的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[UPD: Unknown LSA type]{lang="EN-US"}]{#struct_0_x4702_18917_1433592563}

[[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_x737036476}[报文中含有未知类型]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[UPD: Less recent LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x512231305}

[[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_520772959}[报文中含有不是最新的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1987534337}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程和接口的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf statistics packet]{lang="EN-US"}]{#struct_0_x4702_18917_x802141894}

[ ]{lang="EN-US"}

[          OSPF Process 100 with Router ID 192.168.1.59]{lang="EN-US"}

[                  Packet Statistics]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Waiting to send packet count: 0]{lang="EN-US"}

[         Hello      DD         LSR        LSU        ACK        Total]{lang="EN-US"}

[ Input : 489        6          2          44         40         581]{lang="EN-US"}

[ Output: 492        8          2          45         40         587]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Area: 0.0.0.1]{lang="EN-US"}

[ Interface: 20.1.1.1 (GigabitEthernet1/0/1)]{lang="EN-US"}

[         DD         LSR        LSU        ACK        Total]{lang="EN-US"}

[ Input : 0          0          0          0          0]{lang="EN-US"}

[ Output: 0          0          0          0          0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Interface: 100.1.1.1 (GigabitEthernet1/0/9)]{lang="EN-US"}

[         DD         LSR        LSU        ACK        Total]{lang="EN-US"}

[ Input : 3          1          22         16         42]{lang="EN-US"}

[ Output: 2          1          19         20         42]{lang="EN-US"}

[[表1-28 ]{lang="EN-US"}[display ospf statistics packet]{lang="EN-US"}]{#struct_0_x4702_18917_1410491763}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_897668112}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_1987599873}

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_1987665409}

[[Waiting to send packet count]{lang="EN-US"}]{#struct_0_x4702_18917_x422068681}

[[等待发送报文数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1988255233}

[[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x226378056}

[[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_1988320769}[报文]{style="font-family:宋体"}

[[DD]{lang="EN-US"}]{#struct_0_x4702_18917_597456787}

[[数据库描述报文]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987730944}

[[LSR]{lang="EN-US"}]{#struct_0_x4702_18917_x1215858923}

[[链路状态请求报文]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987796480}

[[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_4284479}

[[链路状态更新报文]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987862016}

[[ACK]{lang="EN-US"}]{#struct_0_x4702_18917_x1579905741}

[[链路状态确认报文]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987927552}

[[Total]{lang="EN-US"}]{#struct_0_x4702_18917_379638817}

[[报文总数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987468800}

[[Input]{lang="EN-US"}]{#struct_0_x4702_18917_755618326}

[[接收报文数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987534336}

[[Output]{lang="EN-US"}]{#struct_0_x4702_18917_x802076358}

[[发送报文数]{style="font-family:宋体"}]{#struct_0_x4702_18917_1987599872}

[[Area]{lang="EN-US"}]{#struct_0_x4702_18917_1987665408}

[[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x422134217}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_1988255232}

[[接口地址和接口名]{style="font-family:宋体"}]{#struct_0_x4702_18917_x226312520}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1910531932}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ospf statistics]{lang="EN-US"}**]{#struct_0_x4702_18917_x1910466396}

::: {#308126799 .myid}
[]{#_Toc404788014}[]{#struct_0_x4702_18917_882126073}

**OSPF \-- OSPF配置命令 \-- display ospf vlink**

------------------------------------------------------------------------

[**[display ospf vlink]{lang="EN-US"}**]{#struct_0_x4702_18917_x736839868}[命令用来显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的虚连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1024332625}

[**[display ospf]{lang="EN-US"}**[ \[ *process-id* \] **vlink**]{lang="EN-US"}]{#struct_0_x4702_18917_699720956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_646421488}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x347076487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_164910272}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1055152770}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x851690561}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1606290739}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_71291726}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736708796}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_188319636}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，将显示所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的虚连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_167110962}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1091705718}[显示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的虚连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display ospf vlink]{lang="EN-US"}]{#struct_0_x4702_18917_x736774332}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[          OSPF Process 1 with Router ID 3.3.3.3]{lang="EN-US"}

[                  Virtual Links]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Virtual-link Neighbor-ID  -\> 2.2.2.2, Neighbor-State: Full]{lang="EN-US"}

[ Interface: 10.1.2.1 (GigabitEthernet1/0/1)]{lang="EN-US"}

[ Cost: 1562  State: P-2-P  Type: Virtual]{lang="EN-US"}

[ Transit Area: 0.0.0.1]{lang="EN-US"}

[ Timers: Hello 10 , Dead 40 , Retransmit 5 , Transmit Delay 1]{lang="EN-US"}

[ MD5 authentication enabled.]{lang="EN-US"}

[    The last key is 3.]{lang="EN-US"}

[    The rollover is in progress, 2 neighbor(s) left.]{lang="EN-US"}

[]{#struct_0_x4702_18917_1019809862}[]{#_Toc94753864}[]{#_Toc94671190}[]{#_Toc73952268}[[表1-29 ]{lang="EN-US"}[display ospf vlink]{lang="EN-US"}]{#_Toc68319401}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2005093291}[[字段]{style="font-family:黑体"}]{#struct_0_x4702_18917_2100507744}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x4702_18917_33387873}

[[Virtual-link Neighbor-id]{lang="EN-US"}]{#struct_0_x4702_18917_x471423154}

[[通过虚连接相连的邻居路由器的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_x736577724}

[[Neighbor-State]{lang="EN-US"}]{#struct_0_x4702_18917_218006692}

[[邻居状态，包括]{style="font-family:宋体"}[Down]{lang="EN-US"}]{#struct_0_x4702_18917_x531344343}[、]{style="font-family:宋体"}[Init]{lang="EN-US"}[、]{style="font-family:宋体"}[2-Way]{lang="EN-US"}[、]{style="font-family:宋体"}[ExStart]{lang="EN-US"}[、]{style="font-family:宋体"}[Exchange]{lang="EN-US"}[、]{style="font-family:宋体"}[Loading]{lang="EN-US"}[和]{style="font-family:宋体"}[Full]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x4702_18917_786567137}

[[此虚连接的本端接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_1187491256}[地址和名称]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x4702_18917_x736643260}

[[接口的路由开销]{style="font-family:宋体"}]{#struct_0_x4702_18917_x550873231}

[[State]{lang="EN-US"}]{#struct_0_x4702_18917_x273902274}

[[接口状态]{style="font-family:宋体"}]{#struct_0_x4702_18917_1601301525}

[[Type]{lang="EN-US"}]{#struct_0_x4702_18917_x564422491}

[[类型：虚连接]{style="font-family:宋体"}]{#struct_0_x4702_18917_x736446652}

[[Transit Area]{lang="EN-US"}]{#struct_0_x4702_18917_617216353}

[[传输区域]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_x30045255}[（如果当前接口为虚连接，则显示）]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_x4702_18917_x483456977}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_76426789}[定时器，分别定义如下：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x736512188}[：接口发送]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dead]{lang="EN-US"}]{#struct_0_x4702_18917_x157824079}[：邻居的失效时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Retransmit]{lang="EN-US"}]{#struct_0_x4702_18917_x750313314}[：接口重传]{lang="EN-US" style="font-family:宋体"}[LSA]{lang="EN-US"}[时间间隔]{lang="EN-US" style="font-family:宋体"}

[[Transmit Delay]{lang="EN-US"}]{#struct_0_x4702_18917_1909363829}

[[接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x736970939}[的传输延迟时间]{style="font-family:宋体"}

[[MD5 authentication enabled]{lang="EN-US"}]{#struct_0_x4702_18917_1433002744}

[[验证模式]{style="font-family:宋体"}]{#struct_0_x4702_18917_448724565}

[[The last key]{lang="EN-US"}]{#struct_0_x4702_18917_x1366316611}

[[最新的]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x737036475}[验证字标识符]{style="font-family:宋体"}

[[neighbor(s)]{lang="EN-US"}]{#struct_0_x4702_18917_x512427913}

[[尚未完成]{style="font-family:宋体"}[MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x221231304}[验证平滑迁移的邻居个数]{style="font-family:宋体"}

[]{#_Toc138212558}[]{#_Toc93984786}[]{#_Toc61236333}[]{#_Toc61093132}[]{#_Toc58812055}[[ ]{lang="EN-US"}]{#_Toc56887184}

::: {#1383318010 .myid}
[]{#_Toc138212562}[]{#_Toc93984790}[]{#_Toc61236341}[]{#_Toc61093142}[]{#_Toc58812065}[]{#_Toc56887194}[]{#_Toc307238204}[]{#_Toc404788015}[]{#struct_0_x4702_18917_588084561}[]{#_Toc293665254}[]{#_Toc256676658}[]{#_Toc256676661}[]{#_Toc256676662}[]{#_Toc256676663}[]{#_Toc256676664}[]{#_Toc256676665}[]{#_Toc256676666}[]{#_Toc256676667}[]{#_Toc256676668}[]{#_Toc256676669}[]{#_Toc256676670}[]{#_Toc256676671}[]{#_Toc256676675}[]{#_Toc256676676}[]{#_Toc256676677}[]{#_Toc256676679}[]{#_Toc256676680}[]{#_Toc256676681}[]{#_Toc256676682}[]{#_Toc256676683}[]{#_Toc256676684}[]{#_Toc256676685}[]{#_Toc256676686}[]{#_Toc256676687}[]{#_Toc256676688}[]{#_Toc256676689}[]{#_Toc256676690}[]{#_Toc256676691}[]{#_Toc256676692}[]{#_Toc256676695}[]{#_Toc256676697}[]{#_Toc256676698}[]{#_Toc256676699}[]{#_Toc256676700}[]{#_Toc256676701}[]{#_Toc256676702}[]{#_Toc256676703}[]{#_Toc256676704}[]{#_Toc256676705}[]{#_Toc256676706}[]{#_Toc256676707}[]{#_Toc256676708}[]{#_Toc256676709}[]{#_Toc256676710}[]{#_Toc256676714}[]{#_Toc256676715}[]{#_Toc256676716}[]{#_Toc256676717}[]{#_Toc256676718}[]{#_Toc256676719}[]{#_Toc256676720}[]{#_Toc256676721}[]{#_Toc256676722}[]{#_Toc256676723}[]{#_Toc256676724}[]{#_Toc256676725}[]{#_Toc256676726}[]{#_Toc256676727}[]{#_Toc256676728}[]{#_Toc256676729}[]{#_Toc256676730}[]{#_Toc256676731}[]{#_Toc256676732}[]{#_Toc256676733}[]{#_Toc256676734}[]{#_Toc256676735}[]{#_Toc256676736}[]{#_Toc256676737}[]{#_Toc256676742}[]{#_Toc256676743}[]{#_Toc256676744}[]{#_Toc256676749}[]{#_Toc256676751}[]{#_Toc256676753}[]{#_Toc256676754}[]{#_Toc256676759}[]{#_Toc256676761}[]{#_Toc256676762}[]{#_Toc256676764}[]{#_Toc256676766}[]{#_Toc256676767}[]{#_Toc256676768}[]{#_Toc256676769}[]{#_Toc256676770}[]{#_Toc256676771}[]{#_Toc256676772}[]{#_Toc256676773}[]{#_Toc256676774}[]{#_Toc256676775}[]{#_Toc256676776}[]{#_Toc256676777}[]{#_Toc256676778}[]{#_Toc256676779}[]{#_Toc256676780}[]{#_Toc256676781}[]{#_Toc256676787}[]{#_Toc256676788}[]{#_Toc256676790}[]{#_Toc256676791}[]{#_Toc256676792}[]{#_Toc256676793}[]{#_Toc256676794}[]{#_Toc256676795}[]{#_Toc256676796}[]{#_Toc256676797}[]{#_Toc256676798}[]{#_Toc256676799}[]{#_Toc256676800}[]{#_Toc256676801}[]{#_Toc256676802}[]{#_Toc256676803}[]{#_Toc256676804}[]{#_Toc256676805}[]{#_Toc256676806}[]{#_Toc256676807}[]{#_Toc256676812}[]{#_Toc256676813}[]{#_Toc256676814}[]{#_Toc256676820}[]{#_Toc256676821}[]{#_Toc256676822}[]{#_Toc256676824}[]{#_Toc256676825}[]{#_Toc256676826}[]{#_Toc256676827}[]{#_Toc256676828}[]{#_Toc256676829}[]{#_Toc256676830}[]{#_Toc256676831}[]{#_Toc256676832}[]{#_Toc256676833}[]{#_Toc256676834}[]{#_Toc256676835}[]{#_Toc256676836}[]{#_Toc256676837}[]{#_Toc256676838}[]{#_Toc256676839}[]{#_Toc256676844}[]{#_Toc256676845}[]{#_Toc256676846}[]{#_Toc256676847}[]{#_Toc256676853}[]{#_Toc256676854}[]{#_Toc256676855}[]{#_Toc256676856}[]{#_Toc256676858}[]{#_Toc256676859}[]{#_Toc256676860}[]{#_Toc256676861}[]{#_Toc256676862}[]{#_Toc256676863}[]{#_Toc256676864}[]{#_Toc256676865}[]{#_Toc256676866}[]{#_Toc256676867}[]{#_Toc256676868}[]{#_Toc256676869}[]{#_Toc256676870}[]{#_Toc256676871}[]{#_Toc256676872}[]{#_Toc256676873}[]{#_Toc256676874}[]{#_Toc256676876}[]{#_Toc256676879}[]{#_Toc256676881}[]{#_Toc256676884}[]{#_Toc256676886}[]{#_Toc256676887}[]{#_Toc256676888}[]{#_Toc256676889}[]{#_Toc256676890}[]{#_Toc256676891}[]{#_Toc256676892}[]{#_Toc256676893}[]{#_Toc256676894}[]{#_Toc256676895}[]{#_Toc256676896}[]{#_Toc256676897}[]{#_Toc256676898}[]{#_Toc256676899}[]{#_Toc256676900}[]{#_Toc256676902}[]{#_Toc256676903}[]{#_Toc256676905}[]{#_Toc256676907}[]{#_Toc256676908}[]{#_Toc256676909}[]{#_Toc256676911}[]{#_Toc256676912}[]{#_Toc256676913}[]{#_Toc256676915}[]{#_Toc256676916}[]{#_Toc256676917}[]{#_Toc256676918}[]{#_Toc256676919}[]{#_Toc256676920}[]{#_Toc256676921}[]{#_Toc256676922}[]{#_Toc256676923}[]{#_Toc256676924}[]{#_Toc256676925}[]{#_Toc256676926}[]{#_Toc256676927}[]{#_Toc256676930}

**OSPF \-- OSPF配置命令 \-- display router id**

------------------------------------------------------------------------

[**[display router id]{lang="EN-US"}**]{#struct_0_x4702_18917_2111220748}[命令用来显示全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736839867}

[**[display router id]{lang="EN-US"}**]{#struct_0_x4702_18917_1024136017}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1461171572}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1918310435}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1683162443}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x2047963616}

[[network-operator]{lang="EN-US"}]{#struct_0_x4702_18917_818541320}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_766712828}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x4702_18917_x736905403}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_646880240}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_118497413}[显示已配置的]{style="font-family:宋体"}[全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display router id]{lang="EN-US"}]{#struct_0_x4702_18917_x1600763722}

[         Configured router ID is 1.1.1.1]{lang="EN-US"}
:::

::: {#1124128791 .myid}
[]{#_Toc404788016}[]{#struct_0_x4702_18917_x2142659322}[]{#_Toc332297396}[]{#_Toc329939886}[]{#_Toc324863559}

**OSPF \-- OSPF配置命令 \-- dscp**

------------------------------------------------------------------------

[**[dscp]{lang="EN-US"}**]{#struct_0_x4702_18917_487706224}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[发送协议报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo dscp]{lang="EN-US"}**]{#struct_0_x4702_18917_x1530001098}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1627054370}

[**[dscp]{lang="EN-US"}**[ *dscp-value*]{lang="EN-US"}]{#struct_0_x4702_18917_x736708795}

[**[undo dscp]{lang="EN-US"}**]{#struct_0_x4702_18917_188254100}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1200417642}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_2054324531}[发送协议报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1502758274}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x31799207}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_807922119}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x736774331}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1019613254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x567695603}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_x4702_18917_x709334900}[：]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1787378804}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1506451154}[配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发送协议报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x666177208}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] dscp 63]{lang="EN-US"}
:::

::::: {#230388801 .myid}
[]{#_Toc404788017}[]{#struct_0_x4702_18917_x736577723}

**OSPF \-- OSPF配置命令 \-- enable link-local-signaling**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_218334372}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_x1846217291}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_2117432145}[命令用来使能]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[本地链路的信令能力。]{style="font-family:宋体"}

[**[undo enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_x1367207954}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[本地链路的信令能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x459866857}

[**[enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_139409254}

[**[undo enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_x736643259}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x550283404}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x686648299}[本地链路的信令能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1876909988}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_243920199}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1165192250}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_462191173}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x465071567}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736446651}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_617150817}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的本地链路的信令能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_2082697694}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] enable link-local-signaling]{lang="EN-US"}
:::::

::::: {#-1279037032 .myid}
[]{#_Toc404788018}[]{#struct_0_x4702_18917_1471334653}[]{#_Toc307238205}[]{#_Toc81626543}[]{#_Toc138212559}[]{#_Toc93984787}[]{#_Toc61236337}[]{#_Toc61093138}[]{#_Toc58812061}[]{#_Toc56887190}[]{#_Toc45164792}[]{#_Toc305920783}[]{#_Toc252194533}[]{#_Toc157660523}[]{#_Toc94761545}[]{#_Toc81993296}

**OSPF \-- OSPF配置命令 \-- enable out-of-band-resynchronization**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_x1948055661}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_x943059058}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[enable out-of-band-resynchronization]{lang="EN-US"}**]{#struct_0_x4702_18917_x736512187}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[带外同步能力。]{style="font-family:宋体"}

[**[undo enable out-of-band-resynchronization]{lang="EN-US"}**]{#struct_0_x4702_18917_x158282831}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[带外同步能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1734805678}

[**[enable out-of-band-resynchronization]{lang="EN-US"}**]{#struct_0_x4702_18917_x2896622}

[**[undo enable out-of-band-resynchronization]{lang="EN-US"}**]{#struct_0_x4702_18917_x1288143623}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1009897458}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1494640815}[带外同步能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2042321002}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736970942}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1433723635}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_54102360}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1510137372}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_651327909}

[[在配置本命令之前，必须先使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1049946207}[本地链路的信令能力。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_16057833}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x32071791}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的带外同步能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x737036478}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] enable link-local-signaling]{lang="EN-US"}

[\[Sysname-ospf-1\] enable out-of-band-resynchronization]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x512100233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_913297946}
:::::

::: {#1529394913 .myid}
[]{#_Toc404788019}[]{#struct_0_x4702_18917_x1910663001}[]{#_Toc352328944}[]{#_Toc345073432}

**OSPF \-- OSPF配置命令 \-- event-log**

------------------------------------------------------------------------

[**[event-log]{lang="EN-US"}**]{#struct_0_x4702_18917_x1910597465}[命令用来配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的日志]{style="font-family:宋体"}[信息个数。]{style="font-family:宋体"}

[**[undo event-log]{lang="EN-US"}**]{#struct_0_x4702_18917_x1910007641}[命令用来恢复缺省]{style="font-family:宋体"}[情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1303091595}

[**[event-log]{lang="EN-US"}**[ { **lsa-flush** \| **peer** \| **spf** } **size** *count*]{lang="EN-US"}]{#struct_0_x4702_18917_x1909942105}

[**[undo event-log]{lang="EN-US"}**[ { **lsa-flush** \| **peer** \| **spf** } **size**]{lang="EN-US"}]{#struct_0_x4702_18917_1378875855}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1910531930}

[[路由计算和邻居的日志信息个数为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_x4702_18917_159835704}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1910466394}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1910400858}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2102165522}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1910335322}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x454623988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1910794074}

[**[lsa-flush]{lang="EN-US"}**]{#struct_0_x4702_18917_x741086871}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[老化日志信息个数。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_x4702_18917_x913316877}[：]{style="font-family:宋体"}[邻居日志信息个数。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_x4702_18917_x1910728538}[：]{style="font-family:宋体"}[SPF]{lang="EN-US"}[日志信息个数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_x4702_18917_x841388001}[：日志信息个数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1910663002}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1910597466}[配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[路由计算日志]{style="font-family:宋体"}[信息个数为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_111594789}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] event-log spf size 50]{lang="EN-US"}
:::

::::: {#-1417285816 .myid}
[]{#_Toc307238206}[]{#_Toc81626545}[]{#_Toc404788020}[]{#struct_0_x4702_18917_1682203723}[]{#_Toc304551801}[]{#_Toc305920788}[]{#_Toc252194538}[]{#_Toc157660527}[]{#_Toc94761547}[]{#_Toc81993298}

**OSPF \-- OSPF配置命令 \-- fast-reroute (OSPF view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_1075839766}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_1243093650}
:::

[ ]{lang="EN-US"}

[**[fast-reroute]{lang="EN-US"}**]{#struct_0_x4702_18917_1728040766}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_x4702_18917_x736839870}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1023808338}

[**[fast-reroute ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[lfa ]{lang="EN-US"}**[\[ **abr-only** \] \| **route-policy** *route-policy-name* }]{lang="EN-US"}]{#struct_0_x4702_18917_x2141268047}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_x4702_18917_x1318525218}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x908451448}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1194170879}[快速重路由功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x865204690}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736905406}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_646552560}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1540717705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1179911059}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_868439142}

[**[lfa]{lang="EN-US"}**]{#struct_0_x4702_18917_1296434676}**[：]{style="font-family:宋体"}**[为所有路由通过]{style="font-family:宋体"}[LFA]{lang="EN-US"}[（]{style="font-family:宋体"}[Loop Free Alternate]{lang="EN-US"}[）算法选取备份下一跳信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[abr-only]{lang="EN-US"}**]{#struct_0_x4702_18917_x1141822830}[：仅选取到]{style="font-family:宋体"}[ABR]{lang="EN-US"}[设备的路由作为备份下一跳。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_x4702_18917_726439597}[：为通过策略的路由指定备份下一跳，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736708798}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_188974996}[快速重路由功能不能与]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能同时使用，否则可能导致快速重路由功能失效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1952532186}[快速重路由功能（]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}[LFA]{lang="EN-US"}[算法选取备份下一跳信息]{style="font-family:宋体"}[）不能与]{lang="EN-US" style="font-family:宋体"}**[vlink-peer]{lang="EN-US"}**[命令同时使用。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1929657152}[快速重路由功能和前缀无关收敛功能同时配置时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[快速重路由功能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_866369278}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1580640672}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的快速重路由功能，为所有路由]{style="font-family:宋体"}[通过]{style="font-family:宋体"}[LFA]{lang="EN-US"}[算法]{style="font-family:宋体"}[选取备份下一跳信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_941734546}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] fast-reroute lfa]{lang="EN-US"}
:::::

::: {#-1659583266 .myid}
[]{#_Toc404788021}[]{#struct_0_x4702_18917_x736774334}[]{#_Toc312662925}[]{#_Toc311562095}

**OSPF \-- OSPF配置命令 \-- filter (OSPF area View)**

------------------------------------------------------------------------

[**[filter]{lang="EN-US"}**]{#struct_0_x4702_18917_1019416646}[命令用来配置对]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[**[undo filter]{lang="EN-US"}**]{#struct_0_x4702_18917_x572723757}[命令用来]{style="font-family:宋体"}[取消对]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[的过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_79066943}

[**[filter]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } { **export** \| **import** }]{lang="EN-US"}]{#struct_0_x4702_18917_616359373}

[**[undo filter]{lang="EN-US"}**[ { **export** \| **import** }]{lang="EN-US"}]{#struct_0_x4702_18917_1362334544}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1883494825}

[[不对]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}]{#struct_0_x4702_18917_354377844}[进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736577726}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_218137764}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1787742235}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1404669399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_454835490}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1341807687}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4702_18917_x1820001329}[：指定的基本或高级访问控制列表，对进出本区域的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x736643262}[：指定的地址前缀列表，对进出本区域的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[route-policy-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x550742159}[：指定的路由策略，对进出本区域的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[export]{lang="EN-US"}**]{#struct_0_x4702_18917_882641272}[：对]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向其它区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[**[import]{lang="EN-US"}**]{#struct_0_x4702_18917_829830713}[：对]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向本区域发布的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1045882671}

[[此命令只在]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_176314781}[路由器上有效，对区域内部路由器无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x597457944}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2031983299}[根据地址前缀列表]{style="font-family:宋体"}[my-prefix-list]{lang="EN-US"}[和编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[分别对进出]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x736446654}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 1]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] filter prefix-list my-prefix-list import]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] filter 2000 export]{lang="EN-US"}
:::

::: {#-1606312080 .myid}
[]{#_Toc404788022}[]{#struct_0_x4702_18917_617347425}[]{#_Toc312662926}[]{#_Toc311562096}[]{#_Toc45164793}

**OSPF \-- OSPF配置命令 \-- filter-policy export (OSPF View)**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_x4702_18917_x1607800465}[命令用来配置对引入的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_x4702_18917_1313155237}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_674521814}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* } **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_x4702_18917_1878706922}

[**[undo filter]{lang="EN-US"}[-policy export]{lang="EN-US"}**[ \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_x4702_18917_x736512190}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x158348368}

[[不对引入的路由信息进行过滤。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x605055226}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1494497158}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_21613759}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_169052850}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x191515855}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x4702_18917_1948156892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736970941}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4702_18917_1433527027}[：用于过滤路由信息目的地址的基本或高级访问控制列表编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x4702_18917_1641264805}[：用于过滤路由信息目的地址的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4702_18917_x301108821}[：路由协议名称，指定何种路由协议的路由信息将被过滤。目前可包括：]{style="font-family:宋体"}**[bgp]{lang="EN-US"}[、]{style="font-family:宋体"}[direct]{lang="EN-US"}[、]{style="font-family:宋体"}[isis]{lang="EN-US"}[、]{style="font-family:宋体"}[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。如果没有指定]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[参数，对引入的任何一个协议产生的路由都要进行过滤。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1287023179}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时，支持该参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1043880976}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4702_18917_2098394333}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_386997750}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x737036477}[使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[引入的路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x512296841}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] filter-policy 2000 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_142850860}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x505751531}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] filter-policy 3000 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736839869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_1024267089}
:::

::: {#-259086966 .myid}
[]{#_Toc404788023}[]{#struct_0_x4702_18917_1261354879}[]{#_Toc312662927}[]{#_Toc311562097}[]{#_Toc45164794}

**OSPF \-- OSPF配置命令 \-- filter-policy import (OSPF View)**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_x4702_18917_35006042}[命令用来过滤通过接收到的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[计算出来的路由信息。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_x4702_18917_980346457}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1743590263}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \[ **gateway** *prefix-list-name* \] \| **gateway** *prefix-list-name* \| **prefix-list** *prefix-list-name* \[ **gateway** *prefix-list-name* \] \| **route-policy** *route-policy-name* } **import**]{lang="EN-US"}]{#struct_0_x4702_18917_x1067891920}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_x4702_18917_221413869}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736905405}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_646487024}[不对通过接收到的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[计算出来的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1521338549}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_463340320}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x851806922}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1588250771}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x4702_18917_x1920184487}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736708797}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x4702_18917_188385172}[：用于过滤路由信息目的地址的基本或高级访问控制列表编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[gateway ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_x4702_18917_30272263}[：指定的地址前缀列表，基于要加入到路由表的路由信息的下一跳进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_x4702_18917_768162473}[：指定的地址前缀列表，基于目的地址对接收的路由信息进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x4702_18917_1970351924}[：指定路由策略名，基于路由策略对接收的路由信息进行过滤。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1727151983}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x4702_18917_455390300}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1150529779}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x736774333}[使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1019744326}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] filter-policy 2000 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x990783694}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1422735232}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] filter-policy 3000 import]{lang="EN-US"}
:::

::::: {#-1325960729 .myid}
[]{#_Toc404788024}[]{#struct_0_x4702_18917_x736577725}

**OSPF \-- OSPF配置命令 \-- graceful-restart (OSPF view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_217941156}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_344634477}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x4702_18917_573335682}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x4702_18917_x1816126719}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x155257835}

[**[graceful-restart]{lang="EN-US"}**[ \[ **ietf** \| **nonstandard** \] \[ **global** \| **planned-only** \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_2131607975}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x4702_18917_1880992526}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736643261}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x550807695}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_924041944}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1066629737}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_970269514}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x2100459438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1529069537}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x736446653}

[**[ietf]{lang="EN-US"}**]{#struct_0_x4702_18917_617281889}[：]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力选项。]{style="font-family:宋体"}

[**[nonstandard]{lang="EN-US"}**]{#struct_0_x4702_18917_x1921354837}[：非]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力选项。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_x4702_18917_x793785821}[：]{style="font-family:宋体"}[全局]{style="font-family:宋体"}[GR]{lang="EN-US"}[，必须保证所有的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[都存在，整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[才会完成，如果有一个]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[失效（比如，接口]{style="font-family:宋体"}[down]{lang="EN-US"}[），则整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。如果未指定本参数，表示支持接口级]{style="font-family:宋体"}[GR]{lang="EN-US"}[，即只要有一个]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[存在，则整个]{style="font-family:宋体"}[GR]{lang="EN-US"}[会完成。]{style="font-family:宋体"}

[**[planned-only]{lang="EN-US"}**]{#struct_0_x4702_18917_1811252246}[：表示只]{style="font-family:宋体"}[支持计划重启。如果未指定本参数，表示计划重启和非计划重启都支持。计划重启指的是手动通过命令执行重启或主备倒换，在进行重启或主备倒换前]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[会先发送]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}[；非计划]{style="font-family:宋体"}[GR]{lang="EN-US"}[指的是由于设备故障等原因进行重启或主备倒换，在进行重启或主备倒换前]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[不会事先发送]{style="font-family:宋体"}[Grace-LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1255611445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使能]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x595218384}[协议的]{lang="EN-US" style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力前，需要先使能]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[不透明链路状态发布接收能力（]{lang="EN-US" style="font-family:宋体"}**[opaque-capability enable]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在使能]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x736512189}[协议的非]{lang="EN-US" style="font-family:宋体"}[IETF]{lang="EN-US"}[标准的]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力前，需要先使能]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[本地链路的信令能力（]{lang="EN-US" style="font-family:宋体"}**[enable link-local-signaling]{lang="EN-US"}**[）和]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[带外同步能力（]{lang="EN-US" style="font-family:宋体"}**[enable out-of-band-resynchronization]{lang="EN-US"}**[）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在使能]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x157889615}[协议的]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力时不指定可选参数]{lang="EN-US" style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[ietf]{lang="EN-US"}**[，则]{lang="EN-US" style="font-family:宋体"}**[nonstandard]{lang="EN-US"}**[为缺省配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPF GR]{lang="EN-US"}]{#struct_0_x4702_18917_x1965218999}[特性与]{lang="EN-US" style="font-family:宋体"}[OSPF NSR]{lang="EN-US"}[特性互斥，即]{lang="EN-US" style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[命令互斥，不能同时配置]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2016855197}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x2113123508}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_372194228}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] opaque-capability enable]{lang="EN-US"}

[\[Sysname-ospf-1\] graceful-restart ietf]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_851579780}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的非]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829113003}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] enable link-local-signaling]{lang="EN-US"}

[\[Sysname-ospf-1\] enable out-of-band-resynchronization]{lang="EN-US"}

[\[Sysname-ospf-1\] graceful-restart nonstandard]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x337612202}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable link-local-signaling]{lang="EN-US"}**]{#struct_0_x4702_18917_x1809986549}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[enable out-of-band-resynchronization]{lang="EN-US"}**]{#struct_0_x4702_18917_1820331522}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[opaque-capability enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x322525024}
:::::

::::: {#939141431 .myid}
[]{#_Toc404788025}[]{#struct_0_x4702_18917_x513825946}[]{#_Toc307238207}[]{#_Toc295378025}[]{#_Toc196967850}

**OSPF \-- OSPF配置命令 \-- graceful-restart helper enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_829047467}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_48317497}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_x4702_18917_74003709}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x147057818}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1022806370}

[**[graceful-restart helper enable]{lang="EN-US"}**[ \[ **planned-only** \]]{lang="EN-US"}]{#struct_0_x4702_18917_998197671}

[**[undo graceful-restart helper enable]{lang="EN-US"}**]{#struct_0_x4702_18917_1516928922}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2058377001}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_829244075}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1087336911}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x351641396}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_243629623}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_195305249}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1125530578}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1294519496}

[**[planned-only]{lang="EN-US"}**]{#struct_0_x4702_18917_x1052731478}[：表示只支持计划重启。]{style="font-family:宋体"}[如果未指定本参数，表示计划重启和非计划重启（即异常重启）都支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829178539}

[[参数]{style="font-family:宋体"}**[planned-only]{lang="EN-US"}**]{#struct_0_x4702_18917_1573965819}[只有在]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准]{style="font-family:宋体"}[GR Helper]{lang="DE"}[的时候使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1452043857}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1161939197}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x786161039}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] graceful-restart helper enable]{lang="EN-US"}
:::::

::::: {#-914000413 .myid}
[]{#_Toc404788026}[]{#struct_0_x4702_18917_588298498}[]{#_Toc307238208}[]{#_Toc157660528}[]{#_Toc305920789}[]{#_Toc252194539}

**OSPF \-- OSPF配置命令 \-- graceful-restart helper strict-lsa-checking**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_829375147}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_x2047017583}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_x4702_18917_x242722605}[命令用来使能]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[**[undo graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_x4702_18917_1769285691}[命令用来关闭]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_549559053}

[**[graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_x4702_18917_x1540405235}

[**[undo graceful-restart helper strict-lsa-checking]{lang="EN-US"}**]{#struct_0_x4702_18917_x1178531137}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x359745920}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_829309611}[协议的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1267311763}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x926628516}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x569989519}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x456986262}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1876899654}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x704374129}

[[当检查到]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}]{#struct_0_x4702_18917_829506219}[设备的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[发生变化时候，]{style="font-family:宋体"}[Helper]{lang="EN-US"}[设备退出]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_980650249}

[]{#_Toc157660530}[]{#struct_0_x4702_18917_358373426}[]{#_Toc305920790}[]{#_Toc252194540}[\# ]{lang="EN-US"}[使能]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[严格]{style="font-family:宋体"}[LSA]{lang="EN-US"}[检查能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_212615556}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] graceful-restart helper strict-lsa-checking]{lang="EN-US"}
:::::

::::: {#-140005437 .myid}
[]{#_Toc404788027}[]{#struct_0_x4702_18917_x1036531417}[]{#_Toc307238209}[]{#_Toc295378027}

**OSPF \-- OSPF配置命令 \-- graceful-restart interval (OSPF view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_349194499}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_x2020597383}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_x4702_18917_829440683}[命令用来配置]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x959096057}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x803785218}

[**[graceful-restart interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_x4702_18917_1395734669}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x847762754}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_608053304}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x725425015}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829637291}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x680425120}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_388074482}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x999997059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x58483934}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2082084140}

[*[interval-value]{lang="EN-US"}*]{#struct_0_x4702_18917_x1666433695}[：指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间（期望重启时间），取值范围为]{style="font-family:宋体"}[40]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2129905858}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_752831603}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间不能小于]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[所有接口中邻居失效时间的最大值，否则可能会造成]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829571755}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1348527817}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_703986733}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] graceful-restart interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1092460233}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf timer dead]{lang="EN-US"}**]{#struct_0_x4702_18917_x345024470}
:::::

::: {#-373443277 .myid}
[]{#_Toc404788028}[]{#struct_0_x4702_18917_x1708311045}

**OSPF \-- OSPF配置命令 \-- host-advertise**

------------------------------------------------------------------------

[**[host-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_x28225430}[命令用来配置并发布一条主机路由。]{style="font-family:宋体"}

[**[undo host-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_829113004}[命令用来恢复删除一条主机路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x337612199}

[**[host-advertise]{lang="EN-US"}**[ *ip-address cost*]{lang="EN-US"}]{#struct_0_x4702_18917_529255442}

[**[undo host-advertise ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_694098552}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1173276965}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_362934509}[不发布主机路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1338232114}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_720633490}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829047468}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_48317494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_2030318845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x699159349}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_34671658}[：主机]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[cost]{lang="EN-US"}*]{#struct_0_x4702_18917_2072808149}[：主机路由的开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2133818710}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_829244076}[配置发布一条路由]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，并设置其开销为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1087336908}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 0]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.0\] host-advertise 1.1.1.1 100]{lang="EN-US"}
:::

::: {#991457240 .myid}
[]{#_Toc404788029}[]{#struct_0_x4702_18917_x352231221}

**OSPF \-- OSPF配置命令 \-- import-route (OSPF view)**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_2046786890}[命令用来配置引入外部路由信息。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_x1046840437}[命令用来取消引入外部路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_290129356}

[]{#struct_0_x4702_18917_829178540}[]{#_Hlt24451984}**[import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \| **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **tag** *tag* \| **type** *type* \] \*]{lang="EN-US"}

[**[undo import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1529360380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x662268644}

[[不引入外部路由信息。]{style="font-family:宋体"}]{#struct_0_x4702_18917_2016771013}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1182104599}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_829375148}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2047017584}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_160561922}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x482591464}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x358762136}

[*[protocol]{lang="EN-US"}*]{#struct_0_x4702_18917_x1871902343}[：指定引入的路由协议，可以是]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x923984713}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all-processes]{lang="EN-US"}**]{#struct_0_x4702_18917_539963218}[：引入指定路由协议所有进程的路由，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[时可以指定该参数。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_x4702_18917_829309612}[：允许引入]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_x4702_18917_x1267311766}[：]{style="font-family:宋体"}[在引入的路由中包含使能了该协议的接口网段路由，]{style="font-family:宋体"}[只有当]{style="font-family:
宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:
宋体"}**[rip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[时可以指定该参数。]{style="font-family:宋体"}[如果未指定本参数，在引入]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[路由时不会包含使能了]{style="font-family:宋体"}[该]{style="font-family:宋体"}[协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost ]{lang="EN-US"}***[cost]{lang="EN-US"}*]{#struct_0_x4702_18917_x167113629}[：路由开销值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_x4702_18917_x1572110704}[：设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位，即在对端路由器上不能转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x1461442115}[：配置只能引入符合指定路由策略的路由。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_x4702_18917_x1968655781}[：外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}[中的标记，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ *type*]{lang="EN-US"}]{#struct_0_x4702_18917_829506220}[：度量值类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，缺省值为]{style="font-family:
宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_x4702_18917_x593327872}[]{#_Hlt24613685}[【使用指导】]{style="font-family:黑体"}

[[外部路由是指到达自治系统外部的路由，有两类：]{style="font-family:宋体"}]{#struct_0_x4702_18917_778279543}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[第一类外部路由（]{style="font-family:宋体"}]{#struct_0_x4702_18917_1645388846}[Type1 External]{lang="EN-US"}[）：这类路由的可信程度较高，并且和]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[自身路由的开销具有可比性，所以到第一类外部路由的开销等于本路由器到相应的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销与]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到该路由目的地址的开销之和。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[第二类外部路由（]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1415583532}[Type2 External]{lang="EN-US"}[）：这类路由的可信度比较低，所以]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议认为从]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到自治系统之外的开销远远大于在自治系统之内到达]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销。所以计算路由开销时将主要考虑前者，即到第二类外部路由的开销等于]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[到该路由目的地址的开销。如果计算出开销值相等的两条路由，再考虑本路由器到相应的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的开销。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1867669741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不能引入缺省路由。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x882080983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route bgp]{lang="EN-US"}**]{#struct_0_x4702_18917_829440684}[命令]{style="font-family:宋体"}[表示只引入]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[；]{lang="EN-US" style="font-family:宋体"}**[import-route bgp allow-ibgp]{lang="EN-US"}**[命令]{style="font-family:宋体"}[表示将]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由也引入]{lang="EN-US" style="font-family:宋体"}[，容易引起路由环路，]{lang="EN-US" style="font-family:宋体"}[请慎用]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能引入路由表中状态为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_x4702_18917_x959096060}[的路由，是否为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[状态可以通过]{lang="EN-US" style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**[ **protocol**]{lang="EN-US"}[命令来查看。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo import-route]{lang="EN-US"}**[ *protocol* **all-processes**]{lang="EN-US"}]{#struct_0_x4702_18917_x804112895}[命令只能取消]{lang="EN-US" style="font-family:宋体"}**[import-route ]{lang="EN-US"}***[protocol ]{lang="EN-US"}***[all-processes]{lang="EN-US"}**[命令的配置，不能取消]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**[ *protocol* *process-id*]{lang="EN-US"}[命令的配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import]{lang="EN-US"}**]{#struct_0_x4702_18917_2094532514}**[-route ]{lang="EN-US"}[nssa-only]{lang="EN-US"}**[命令]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[后]{style="font-family:宋体"}[，引入的路由只在]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域产生]{lang="EN-US" style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[，不]{lang="EN-US" style="font-family:宋体"}[会]{style="font-family:宋体"}[在非]{lang="EN-US" style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域]{style="font-family:宋体"}[产生]{lang="EN-US" style="font-family:宋体"}[Type-5]{lang="EN-US"}[ ]{lang="EN-US"}[LSA]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1487758104}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_622121529}[指定引入的进程号为]{style="font-family:宋体"}[40]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由为]{style="font-family:宋体"}[Type-2]{lang="EN-US"}[外部路由，路由标记为]{style="font-family:宋体"}[33]{lang="EN-US"}[，度量值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_598128721}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] import-route rip 40 type 2 tag 33 cost 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829637292}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-route-advertise]{lang="EN-US"}**[ (OSPF view)]{lang="EN-US"}]{#struct_0_x4702_18917_x680425121}
:::

::: {#904212641 .myid}
[]{#_Toc138212563}[]{#_Toc125947680}[]{#_Toc404788030}[]{#struct_0_x4702_18917_388008946}

**OSPF \-- OSPF配置命令 \-- ispf**

------------------------------------------------------------------------

[**[ispf enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x162316627}[命令用来使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_x4702_18917_1765596295}[命令用来关闭增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1123938607}

[**[ispf enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x1593365955}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x730909041}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829571756}

[[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_1348527816}[计算功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_703921197}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x877558083}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1635999120}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_933970994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x875994365}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2119292234}

[[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x4702_18917_829113001}[计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x337612204}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1810117621}[关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1775472085}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] undo ispf enable]{lang="EN-US"}
:::

::: {#-1110888516 .myid}
[]{#_Toc404788031}[]{#struct_0_x4702_18917_x1465234918}

**OSPF \-- OSPF配置命令 \-- log-peer-change**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_x4702_18917_x556619151}[命令用来打开]{style="font-family:宋体"}[邻居状态变化的输出开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_x4702_18917_829047465}[命令]{style="font-family:宋体"}[用来关闭]{style="font-family:宋体"}[邻居状态变化的输出开关]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_48317499}

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_x4702_18917_x1073007363}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_x4702_18917_1399234101}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_826878811}

[[邻居状态变化的输出开关处于打开状态]{style="font-family:宋体"}]{#struct_0_x4702_18917_1828243577}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2062183948}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1266396547}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829244073}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1087336913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x351772468}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1304688268}

[[打开邻接状态输出开关后，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x752790346}[邻居状态变化]{style="font-family:宋体"}[时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[日志信息]{style="font-family:宋体"}[的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1739263313}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1026078437}[关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的邻居状态变化的输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829178537}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] undo log-peer-change]{lang="EN-US"}
:::

::: {#1925707287 .myid}
[]{#_Toc93984791}[]{#_Toc70390402}[]{#_Toc56887226}[]{#_Toc45164830}[]{#_Toc404788032}[]{#struct_0_x4702_18917_1573965821}[]{#_Toc138212564}[]{#_Toc136160351}

**OSPF \-- OSPF配置命令 \-- lsa-arrival-interval**

------------------------------------------------------------------------

[**[lsa-arrival-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x1451519566}[命令用来配置]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重复到达的最小时间间隔。]{style="font-family:宋体"}

[**[undo lsa-arrival-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x2038216699}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1270081347}

[**[lsa-arrival-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x1020739472}

[**[undo lsa-arrival-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_650749350}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1013215003}

[[OSPF LSA]{lang="EN-US"}]{#struct_0_x4702_18917_829375145}[重复到达的最小时间间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2047017581}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_920076809}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x339417486}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1940948170}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1863903114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1708109943}

[*[interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x1418642111}[：]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重复到达的最小时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829309609}

[[如果在]{style="font-family:宋体"}*[interval]{lang="EN-US"}*]{#struct_0_x4702_18917_1071340405}[的时间间隔内又收到一条]{style="font-family:宋体"}[LSA]{lang="EN-US"}[类型、]{style="font-family:宋体"}[LS ID]{lang="EN-US"}[、生成路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[均相同的]{style="font-family:宋体"}[LSA]{lang="EN-US"}[则直接丢弃，这样就可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。]{style="font-family:宋体"}

[[建议]{style="font-family:宋体"}*[interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x78105302}[小于或等于]{style="font-family:宋体"}**[lsa-generation-interval]{lang="EN-US"}**[命令所配置的]{style="font-family:宋体"}*[initial-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x588066964}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x631493319}[设置]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重复到达的最小时间间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1586845486}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] lsa-arrival-interval 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x445137544}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lsa-generation-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_829506217}
:::

::: {#125214695 .myid}
[]{#_Toc404788033}[]{#struct_0_x4702_18917_980650243}[]{#_Toc138212565}[]{#_Toc136160352}

**OSPF \-- OSPF配置命令 \-- lsa-generation-interval**

------------------------------------------------------------------------

[**[lsa-generation-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_358373432}[命令用来配置]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重新生成的时间间隔。]{style="font-family:宋体"}

[**[undo lsa-generation-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x2126036608}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x383689959}

[**[lsa-generation-interval ]{lang="EN-US"}***[maximum-interval ]{lang="EN-US"}*[\[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_x4702_18917_1195971826}

[**[undo lsa-generation-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_153215721}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1037678377}

[[OSPF LSA]{lang="EN-US"}]{#struct_0_x4702_18917_829440681}[重新生成的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x959096055}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x803916290}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1788599046}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_860964493}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1561391175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1518712073}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x505063298}[：]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重新生成的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_829637289}[：]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重新生成的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_1275890024}[：]{style="font-family:宋体"}[OSPF LSA]{lang="EN-US"}[重新生成的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1069298689}

[[通过调节]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_35696430}[重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将]{style="font-family:宋体"}[LSA]{lang="EN-US"}[重新生成时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x27483744}[和]{style="font-family:宋体"}*[incremental-interva]{lang="EN-US"}*[l]{lang="EN-US"}[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1831881222}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x573726854}[设置]{style="font-family:宋体"}[LSA]{lang="EN-US"}[重新生成的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829571753}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] lsa-generation-interval 2 100 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1348527819}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lsa-arrival-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_704904237}
:::

::: {#1745846555 .myid}
[]{#_Toc138212566}[]{#_Toc404788034}[]{#struct_0_x4702_18917_x2055585509}

**OSPF \-- OSPF配置命令 \-- lsdb-overflow-interval**

------------------------------------------------------------------------

[**[lsdb-overflow-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x452975953}[命令用来配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[OSPF ]{lang="EN-US"}[尝试退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态的定时器时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lsdb-overflow-interval**]{lang="EN-US"}]{#struct_0_x4702_18917_228174820}[命令用]{style="font-family:
宋体"}[来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1630616070}

[**[lsdb-overflow-interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_x4702_18917_224917644}

[[undo **lsdb-overflow-interval**]{lang="EN-US"}]{#struct_0_x4702_18917_829113002}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x337612201}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1809921013}[尝试退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态的定时器时间间隔是]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1483231271}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1536995584}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_933323400}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1159765895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1927514621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829047466}

[*[interval]{lang="EN-US"}*]{#struct_0_x4702_18917_48317496}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[尝试退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态的定时器时间间隔]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1882311427}

[[网络中出现过多]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_1694414537}[，会占用大量系统资源。当设置的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[的最大数量达到上限时，]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[会进入]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态，在]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态中，不再接收]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[，同时删除自己生成的]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[，对于已经收到的]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[则不会删除。这样就可以减少]{style="font-family:宋体"}[LSA]{lang="EN-US"}[从而节省系统资源。]{style="font-family:宋体"}

[[通过调整定时器间隔，可以调整]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_256715415}[退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态的时间。]{style="font-family:宋体"}

[[配置为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x4702_18917_x310044334}[秒表示不启动定时器，不退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_401318950}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_2138185726}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[尝试退出]{style="font-family:宋体"}[overflow]{lang="EN-US"}[的定时器间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829244074}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] lsdb-overflow-interval 10]{lang="EN-US"}
:::

::: {#-320306929 .myid}
[]{#_Toc404788035}[]{#struct_0_x4702_18917_1087336910}

**OSPF \-- OSPF配置命令 \-- lsdb-overflow-limit**

------------------------------------------------------------------------

[**[lsdb-overflow-limit]{lang="EN-US"}**]{#struct_0_x4702_18917_x351706932}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[的最大条目数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lsdb-overflow-limit**]{lang="EN-US"}]{#struct_0_x4702_18917_1859008269}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x681195025}

[**[lsdb-overflow-limit]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x4702_18917_x1188328593}

[**[undo lsdb-overflow-limit]{lang="EN-US"}**]{#struct_0_x4702_18917_1802630536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829178538}

[[不对]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x4702_18917_1573965820}[中]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[的最大条目数进行限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1451585102}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1238613798}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1990801325}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1468800244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x351665268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829375146}

[*[number]{lang="EN-US"}*]{#struct_0_x4702_18917_x2047017582}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[的最大条目数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1323361336}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x116152159}[设置]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中]{style="font-family:宋体"}[External LSA]{lang="EN-US"}[的最大条目数为]{style="font-family:宋体"}[400000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1781602079}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] lsdb-overflow-limit 400000]{lang="EN-US"}
:::

::::: {#-468300945 .myid}
[]{#_Toc45164796}[]{#_Toc404788036}[]{#struct_0_x4702_18917_x841440624}[]{#_Toc138212567}[]{#_Toc93984792}

**OSPF \-- OSPF配置命令 \-- maximum load-balancing (OSPF view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_x219803312}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_829309610}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[maximum load-balancing]{lang="EN-US"}**]{#struct_0_x4702_18917_x1267311764}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[支持的等价路由的最大条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_x4702_18917_x1329913043}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2105641155}

[**[maximum load-balancing]{lang="EN-US"}**[ *maximum*]{lang="EN-US"}]{#struct_0_x4702_18917_x176550397}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_x4702_18917_x1084095895}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1005170525}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x815062071}[支持的等价路由的最大条数与]{style="font-family:宋体"}[系统支持最大等价路由的条数相同]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829506218}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_980650248}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_358373425}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_212615553}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1036531414}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_752479026}

[*[maximum]{lang="EN-US"}*]{#struct_0_x4702_18917_x1192420974}[：等价路由的最大条数，当]{style="font-family:宋体"}*[maximum]{lang="EN-US"}*[取值为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，相当于不进行负载分担。不同型号的设备支持的取值范围与缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1047512097}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x4702_18917_829440682}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x4702_18917_278884655}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x959096058}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x804637186}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[支持的]{style="font-family:宋体"}[等价路由的最大条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1871884419}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] maximum load-balancing 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1998285546}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x4702_18917_1892988612}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::::

::: {#733012995 .myid}
[]{#_Toc404788037}[]{#struct_0_x4702_18917_829637290}[]{#_Toc138212569}[]{#_Toc93984794}[]{#_Toc61236343}[]{#_Toc61093144}[]{#_Toc58812067}[]{#_Toc56887196}[]{#_Toc256676940}[]{#_Toc256676943}[]{#_Toc256676944}[]{#_Toc256676945}[]{#_Toc256676946}[]{#_Toc256676947}[]{#_Toc256676948}[]{#_Toc256676949}[]{#_Toc256676950}[]{#_Toc256676951}[]{#_Toc256676952}[]{#_Toc256676953}[]{#_Toc256676954}[]{#_Toc256676955}[]{#_Toc330546457}[]{#_Toc330546458}[]{#_Toc330546459}[]{#_Toc330546460}[]{#_Toc330546461}[]{#_Toc330546462}[]{#_Toc330546463}[]{#_Toc330546464}[]{#_Toc330546465}[]{#_Toc330546466}[]{#_Toc330546467}[]{#_Toc330546468}[]{#_Toc330546469}[]{#_Toc330546470}[]{#_Toc330546471}[]{#_Toc330546472}[]{#_Toc330546473}[]{#_Toc330546474}[]{#_Toc330546475}[]{#_Toc330546476}

**OSPF \-- OSPF配置命令 \-- network (OSPF area view)**

------------------------------------------------------------------------

[**[network]{lang="EN-US"}**]{#struct_0_x4702_18917_x680425119}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域所包含的网段并在指定网段的接口上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo network]{lang="EN-US"}**]{#struct_0_x4702_18917_388533233}[命令用来删除区域所包含的网段并关闭指定网段接口上的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_705660248}

[**[network ]{lang="EN-US"}***[ip-]{lang="EN-US"}[address wildcard-mask]{lang="EN-US"}*]{#struct_0_x4702_18917_595927335}

[**[undo]{lang="EN-US"}**[ **network** *ip-address wildcard-mask*]{lang="EN-US"}]{#struct_0_x4702_18917_1108588153}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x971257828}

[[接口不属于任何区域且]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_206325986}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829571754}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1348527818}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_704838701}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x488643863}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1933627539}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_647870213}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_230817714}[：接口所在的网段地址。]{style="font-family:宋体"}

[*[wildcard-mask]{lang="EN-US"}*]{#struct_0_x4702_18917_x1857129259}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码的反码，相当于将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码取反（]{style="font-family:宋体"}[0]{lang="EN-US"}[变]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变]{style="font-family:
宋体"}[0]{lang="EN-US"}[）。其中，"]{style="font-family:宋体"}[1]{lang="EN-US"}["表示忽略]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址中对应的位，"]{style="font-family:宋体"}[0]{lang="EN-US"}["表示必须保留此位。（例如：子网掩码]{style="font-family:宋体"}[255.0.0.0]{lang="EN-US"}[，该掩码的通配符掩码为]{style="font-family:宋体"}[0.255.255.255]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829112999}

[[该命令可以在一个区域内配置一个或多个接口。在接口上运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1297045737}[协议，此接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须在]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的网段范围之内。]{style="font-family:宋体"}[如果此接口只有从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址在]{style="font-family:宋体"}**[network]{lang="EN-US"}**[命令指定的网段范围之内，接口不运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_859551359}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1333914600}[指定运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址位于网段]{style="font-family:宋体"}[131.108.20.0/24]{lang="EN-US"}[，接口所在的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1754321998}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 2]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.2\] network 131.108.20.0 0.0.0.255]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1831948145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf]{lang="EN-US"}**]{#struct_0_x4702_18917_829047463}
:::

::: {#-1554088180 .myid}
[]{#_Toc138212570}[]{#_Toc93984795}[]{#_Toc61236344}[]{#_Toc61093145}[]{#_Toc58812068}[]{#_Toc56887197}[]{#_Toc45164797}[]{#_Toc404788038}[]{#struct_0_x4702_18917_48317501}[]{#_Toc343688458}[]{#_Toc328986018}[]{#_Toc322442504}

**OSPF \-- OSPF配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_x4702_18917_x1465908032}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_x4702_18917_1519470405}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1690829984}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_x4702_18917_612777529}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_x4702_18917_561100666}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1891622228}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_829244071}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1087336915}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x351379252}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1366875542}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x428322723}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1656624593}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1506990832}

[[OSPF NSR]{lang="EN-US"}]{#struct_0_x4702_18917_x1788140861}[特性与]{style="font-family:宋体"}[OSPF GR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[和]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829178535}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1573965823}[在]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[中使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1451388494}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] non-stop-routing]{lang="EN-US"}
:::

::: {#-690712979 .myid}
[]{#_Toc404788039}[]{#struct_0_x4702_18917_x560006025}

**OSPF \-- OSPF配置命令 \-- nssa**

------------------------------------------------------------------------

[**[nssa]{lang="EN-US"}**]{#struct_0_x4702_18917_1600510979}[命令用来配置一个区域为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo nssa]{lang="EN-US"}**]{#struct_0_x4702_18917_x165797053}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1616073121}

[**[nssa ]{lang="EN-US"}**[\[ **default-route-advertise**]{lang="EN-US"}[ \[ **cost** *cost* \| **nssa-only** \| **route-policy** *route-policy-name* \| **type** *type* \] \* \| **no-import-route** \| **no-summary** \| **suppress-fa** \| \[ **translate-always** \| **translate-never** \] \| **translator-stability-interval** *value* \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_829375143}

[**[undo nssa]{lang="EN-US"}**]{#struct_0_x4702_18917_x2047017579}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1277159137}

[[没有区域被配置为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_216341364}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x576674404}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x978201300}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_826051906}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_836517073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_829309607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1071340399}

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_x4702_18917_x1268959965}[：该参数只用于]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[或]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[，配置后，对于]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，不论本地是否存在缺省路由，都将生成一条]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[向区域内发布缺省路由；对于]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[，只有当本地存在缺省路由时，才产生]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[向区域内发布缺省路由。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x4702_18917_1494346295}[：该缺省路由的度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777214]{lang="EN-US"}[。如果未指定本参数，缺省路由的度量值将取]{style="font-family:宋体"}**[default cost]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[**[nssa-only]{lang="EN-US"}**]{#struct_0_x4702_18917_57164287}[：设置]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位，即在对端路由器上不能转为]{style="font-family:
宋体"}[Type-5 LSA]{lang="EN-US"}[。缺省时，]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位被置位，即在对端路由器上可以转为]{style="font-family:
宋体"}[Type-5 LSA]{lang="EN-US"}[（如果本地路由器是]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，则会检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，当]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居存在时，产生的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中]{style="font-family:宋体"}[P]{lang="EN-US"}[比特位不置位）。]{style="font-family:
宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x4702_18917_686856640}[：路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有当前路由器的路由表中存在缺省路由，并且有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略，才可以产生一个描述缺省路由的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[发布出去，指定的路由策略会影响]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[中的值。]{style="font-family:宋体"}

[**[type ]{lang="EN-US"}***[type]{lang="EN-US"}*]{#struct_0_x4702_18917_x1076629212}[：该]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的类型，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2]{lang="EN-US"}[，如果未指定指定本参数，]{style="font-family:
宋体"}[Type-7 LSA]{lang="EN-US"}[的缺省类型将取]{style="font-family:宋体"}**[default type]{lang="EN-US"}**[命令配置的值。]{style="font-family:宋体"}

[**[no-import-route]{lang="EN-US"}**]{#struct_0_x4702_18917_829506215}[：该参数用于禁止将]{style="font-family:宋体"}[AS]{lang="EN-US"}[外部路由以]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[的形式引入到]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域中，这个参数通常只用在既是]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，也是]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[自治系统的]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由器上，以保证所有外部路由信息能正确地进入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由域。]{style="font-family:宋体"}

[**[no-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_980650245}[：该参数只用于]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，配置后，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[只通过]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[向区域内发布一条缺省路由，不再向区域内发布任何其它]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（这种区域又称为]{style="font-family:宋体"}[Totally NSSA]{lang="EN-US"}[区域）。]{style="font-family:宋体"}

[**[suppress-fa]{lang="EN-US"}**]{#struct_0_x4702_18917_358373430}[：指定当]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[时，生成的]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[中的]{style="font-family:宋体"}[Forwarding Address]{lang="EN-US"}[不生效。]{style="font-family:宋体"}

[**[translate-always]{lang="EN-US"}**]{#struct_0_x4702_18917_x2126036610}[：指定]{style="font-family:宋体"}[ABR]{lang="EN-US"}[为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器。]{style="font-family:宋体"}

[**[translate-never]{lang="EN-US"}**]{#struct_0_x4702_18917_x739985855}[：指定]{style="font-family:宋体"}[ABR]{lang="EN-US"}[不能将]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[translator-stability-interval ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x4702_18917_x1484416021}[：当有新的设备成为]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域的]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器后，原]{style="font-family:宋体"}[Type-7 LSA]{lang="EN-US"}[转换为]{style="font-family:宋体"}[Type-5 LSA]{lang="EN-US"}[的转换路由器保持转换能力的时间。]{style="font-family:宋体"}*[value]{lang="EN-US"}*[为保持时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[900]{lang="EN-US"}[，单位为秒。缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒，即不保持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x895131819}

[[如果要将一个区域配置成]{style="font-family:宋体"}[NSSA]{lang="EN-US"}]{#struct_0_x4702_18917_872132872}[区域，则该区域中的所有路由器都必须配置命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829440679}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1003726079}[将区域]{style="font-family:宋体"}[1]{lang="EN-US"}[配置成]{style="font-family:宋体"}[NSSA]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[]{#struct_0_x4702_18917_x1679114631}[]{#_Hlt535131393}[\<Sysname\> system-view]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 1]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] nssa]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1519450575}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-cost]{lang="EN-US"}**[ (OSPF ]{lang="EN-US"}]{#struct_0_x4702_18917_x652147553}[area ]{lang="EN-US"}[view)]{lang="EN-US"}
:::

::: {#1952989943 .myid}
[]{#_Toc138212571}[]{#_Toc93984797}[]{#_Toc61236345}[]{#_Toc61093146}[]{#_Toc58812069}[]{#_Toc56887198}[]{#_Toc45164798}[]{#_Toc404788040}[]{#struct_0_x4702_18917_x306200125}[]{#_Toc312662943}[]{#_Toc311562102}[]{#_Toc307407349}[]{#_Toc295378023}[]{#_Toc252194551}[]{#_Toc256676961}[]{#_Toc256676962}[]{#_Toc256676965}[]{#_Toc256676966}[]{#_Toc256676967}[]{#_Toc256676968}[]{#_Toc256676969}[]{#_Toc256676970}[]{#_Toc256676971}[]{#_Toc256676972}[]{#_Toc256676973}[]{#_Toc256676974}[]{#_Toc256676975}[]{#_Toc256676978}

**OSPF \-- OSPF配置命令 \-- opaque-capability enable**

------------------------------------------------------------------------

[**[opaque-capability enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x2050625346}[命令用来使能]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力。]{style="font-family:宋体"}

[**[undo opaque-capability]{lang="EN-US"}**]{#struct_0_x4702_18917_829637287}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1275890018}

[**[opaque-capability enable]{lang="EN-US"}**]{#struct_0_x4702_18917_1069560830}

[**[undo opaque-capability]{lang="EN-US"}**]{#struct_0_x4702_18917_x1985588440}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1410000355}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1865939672}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_826100788}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x361325158}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829571751}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1348527821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_704379946}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x521780488}

[[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1327824510}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力后，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[可以发布接收]{style="font-family:宋体"}[Type9]{lang="EN-US"}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[，接收]{style="font-family:宋体"}[Type10]{lang="EN-US"}[和]{style="font-family:宋体"}[Type11]{lang="EN-US"}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x543898118}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1736881834}[关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[Opaque LSA]{lang="EN-US"}[发布接收能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829113000}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] undo opaque-capability]{lang="EN-US"}
:::

::: {#904212635 .myid}
[]{#_Toc404788041}[]{#struct_0_x4702_18917_x337612203}

**OSPF \-- OSPF配置命令 \-- ospf**

------------------------------------------------------------------------

[**[ospf]{lang="FR"}**]{#struct_0_x4702_18917_x1810052085}[命令用来启动]{style="font-family:宋体"}[OSPF]{lang="FR"}[，并进入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo ospf]{lang="EN-US"}**]{#struct_0_x4702_18917_x2103193307}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2130991204}

[**[ospf ]{lang="EN-US"}**[\[ *process-id* \| **router-id** *router-id* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_x232967555}

[**[undo ]{lang="EN-US"}[ospf ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[process-id]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1721137884}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829047464}

[[系统没有运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_48317498}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1265644797}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_909518333}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1236133692}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_899744520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_99667875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x251497165}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_829244072}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[router-id]{lang="EN-US"}***[ router-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1087336912}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程使用的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，]{style="font-family:宋体"}[点分十进制形式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x351838004}[：指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_970627045}

[[通过指定不同的进程号，可以在一台路由器上运行多个]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_366297528}[进程。这种情况下，建议使用命令中的]{style="font-family:宋体"}*[router-id]{lang="EN-US"}*[为不同进程指定不同的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[必须先启动]{style="font-family:宋体"}]{#struct_0_x4702_18917_x399011519}[OSPF]{lang="FR"}[进程才能配置相关参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x692473691}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1110718372}[启动]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[并配置]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[10.10.10.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_829178536}

[\[Sysname\] ospf 100 router-id 10.10.10.1]{lang="EN-US"}

[\[Sysname-ospf-100\]]{lang="EN-US"}
:::

::: {#-60367096 .myid}
[]{#_Toc138212572}[]{#_Toc93984798}[]{#_Toc404788042}[]{#struct_0_x4702_18917_1573965822}[]{#_Toc329939888}[]{#_Toc332297420}

**OSPF \-- OSPF配置命令 \-- ospf area**

------------------------------------------------------------------------

[**[ospf area]{lang="EN-US"}**]{#struct_0_x4702_18917_x1451454030}[命令用来在接口上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ospf area]{lang="EN-US"}**]{#struct_0_x4702_18917_x75546906}[命令用]{style="font-family:宋体"}[来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1513348405}

[**[ospf]{lang="EN-US"}**[ *process-id* **area** *area-id* \[ **exclude-subip** \]]{lang="EN-US"}]{#struct_0_x4702_18917_385959552}

[**[undo ospf]{lang="EN-US"}**[ *process-id* **area** \[ **exclude-subip** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x965487121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_829375144}

[[接口上未使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x2047017580}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1808806546}

[[接口]{style="font-family:宋体"}]{#struct_0_x4702_18917_1907242116}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2114140917}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1884616770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1660002209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1282142671}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_829309608}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[area-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1071340404}[：区域的标识，可以是十进制整数（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，系统会将其转换成]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式）或者是]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址格式*。*]{style="font-family:宋体"}

[**[exclude-subip]{lang="EN-US"}**]{#struct_0_x4702_18917_x78039766}[：不包含从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果未指定本参数，则会包含从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x167533965}

[[接口配置优先，接口使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1229291784}[优于命令]{style="font-family:宋体"}**[network]{lang="EN-US"}**[的配置。]{style="font-family:宋体"}

[[接口使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1489001288}[时，如果不存在进程和区域，则创建对应的进程和区域；接口去使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[时，不删除已经创建的进程和区域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1569461243}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_x4702_18917_829506216}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_980650242}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，接口所在的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，不包含从]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_358373431}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname- GigabitEthernet1/0/2\] ospf 1 area 2 exclude-subip]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2126036611}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_826098086}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，接口所在的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[，不包含从]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1210019458}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf 1 area 2 exclude-subip]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1441552997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_x4702_18917_x1340843514}
:::

::: {#1447358721 .myid}
[]{#_Toc404788043}[]{#struct_0_x4702_18917_1770861925}

**OSPF \-- OSPF配置命令 \-- ospf authentication-mode**

------------------------------------------------------------------------

[**[ospf authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_829440680}[命令用来设置接口对]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[报文进行验证的验证模式及验证字。]{style="font-family:宋体"}

[**[undo ospf authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_x959096056}[命令用来删除接口下已设置的验证模式。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x803719682}

[[MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_180751104}[验证模式：]{style="font-family:宋体"}

[**[ospf authentication-mode]{lang="EN-US"}**[ { **hmac-md5** \| **md5** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* }]{lang="EN-US"}]{#struct_0_x4702_18917_x23423010}

[**[undo ospf authentication-mode ]{lang="EN-US"}**[{ **hmac-md5** \| **md5** } *key-id*]{lang="EN-US"}]{#struct_0_x4702_18917_x1083973135}

[[简单验证模式：]{style="font-family:宋体"}]{#struct_0_x4702_18917_1917461483}

[**[ospf authentication-mode simple]{lang="EN-US"}**[ { **cipher** *cipher-string* \| **plain** *plain-string* }]{lang="EN-US"}]{#struct_0_x4702_18917_829637288}

[**[undo ospf authentication-mode simple]{lang="EN-US"}**]{#struct_0_x4702_18917_1275890025}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1069364225}

[[接口不对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x807328163}[报文进行验证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x449341985}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1576696432}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1891441538}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1247091825}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_829571752}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1348527820}

[**[hmac-md5]{lang="EN-US"}**]{#struct_0_x4702_18917_704314410}[：]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x4702_18917_x439396411}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x4702_18917_429390077}[：简单验证模式。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x2032647586}[：验证字标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x4702_18917_x1473611398}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x4702_18917_x76236257}[：表示设置的密文密码，区分大小写。对于简单验证模式，可以是长度为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[41]{lang="EN-US"}[个字符的字符串，对于]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证模式，可以是长度为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899770352}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x4702_18917_2136958118}[：表示设置的明文密码，区分大小写。对于简单验证模式，可以是长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[个字符的字符串，对于]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证模式，可以是长度为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x544822232}

[[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x4702_18917_1684482206}

[[同一网段的接口的验证字口令必须相同，可指定使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_547261879}[验证或简单验证两种方式，但不能同时指定；使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证方式时，可配置多条]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证命令，但]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[是唯一的，同一]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[只能配置一个验证字。]{style="font-family:宋体"}

[[修改接口的]{style="font-family:宋体"}[OSPF MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_1492942824}[验证字的步骤如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[首先在该接口配置新的]{style="font-family:宋体"}]{#struct_0_x4702_18917_611806798}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；此时若邻居设备尚未配置新的]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，便会触发]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。在这个过程中，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[会发送分别携带各个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字的多份报文，使得已配置新验证字的邻居设备、和尚未配置新验证字的邻居设备都能验证通过，保持邻居关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[然后在各个邻居设备上也都配置相同的新]{style="font-family:宋体"}]{#struct_0_x4702_18917_x50373565}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；当设备上收到所有邻居的携带新验证字的报文后，便会退出]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最后在本设备和所有邻居上都删除旧的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899835888}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；建议接口下不要保留多个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，每次]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1023784427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1119132559}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1344799238}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[明文验证模式，验证字标识符为]{style="font-family:宋体"}[15]{lang="EN-US"}[，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1534583851}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ospf authentication-mode md5 15 plain 123456]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x1899639280}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1344995846}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[明文验证模式，验证字标识符为]{style="font-family:宋体"}[15]{lang="EN-US"}[，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_2032660195}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf authentication-mode md5 15 plain 123456]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_574238868}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1442339047}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[采用简单明文验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899704816}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\]]{lang="NO-BOK"}[ ]{lang="NO-BOK"}[ospf authentication-mode simple plain 123456]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_750466162}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1344930310}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[采用简单明文验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1679065638}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf authentication-mode simple plain 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1168821897}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_x233257114}
:::

::::: {#655014867 .myid}
[]{#_Toc138212573}[]{#_Toc93984799}[]{#_Toc61236348}[]{#_Toc61093149}[]{#_Toc58812072}[]{#_Toc56887201}[]{#_Toc45164801}[]{#_Toc404788044}[]{#struct_0_x4702_18917_x1899508208}[]{#_Toc304551815}[]{#_Toc256676982}[]{#_Toc256676983}[]{#_Toc256676984}[]{#_Toc256676985}[]{#_Toc256676986}[]{#_Toc256676987}[]{#_Toc256676988}[]{#_Toc256676989}[]{#_Toc256676990}[]{#_Toc256676991}[]{#_Toc256676992}[]{#_Toc256676993}[]{#_Toc256676994}[]{#_Toc256676995}[]{#_Toc256676996}[]{#_Toc256676998}[]{#_Toc256677001}[]{#_Toc256677002}[]{#_Toc256677003}[]{#_Toc256677004}[]{#_Toc256677006}[]{#_Toc256677007}[]{#_Toc256677008}[]{#_Toc256677009}[]{#_Toc256677010}

**OSPF \-- OSPF配置命令 \-- ospf bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_x53905210}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_993839844}
:::

[ ]{lang="EN-US"}

[**[ospf bfd enable]{lang="EN-US"}**]{#struct_0_x4702_18917_1773131802}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ospf** **bfd enable**]{lang="EN-US"}]{#struct_0_x4702_18917_351518796}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_423260440}

[**[ospf bfd enable ]{lang="EN-US"}**]{#struct_0_x4702_18917_1802776178}[\[ **echo** \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**]{#struct_0_x4702_18917_x580776762}[ **ospf bfd enable**]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899573744}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1133359656}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1422679770}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1393706449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_707495242}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1930033758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_333463910}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899377136}

[**[echo]{lang="EN-US"}**]{#struct_0_x4702_18917_578041620}[：通过]{style="font-family:宋体"}[BFD echo]{lang="EN-US"}[报文方式实现]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。如果不指定本参数，表示通过]{style="font-family:宋体"}[BFD]{lang="EN-US"}[控制报文方式实现]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2145931303}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_770026151}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能不能与]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[快速重路由功能同时使用，否则可能导致快速重路由功能失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1191674179}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x327481948}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1985120777}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899442672}

[\[Sysname\] ospf]{lang="EN-US"}

[\[Sysname-ospf-1\] area 0]{lang="EN-US"}

[\[Sysname-ospf-1-area-0.0.0.0\] network 192.168.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname-ospf-1-area-0.0.0.0\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_284922716}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1528565754}[使能接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的]{style="font-family:宋体"}[OSPF BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1695990477}

[\[Sysname\] ospf]{lang="EN-US"}

[\[Sysname-ospf-1\] area 0]{lang="EN-US"}

[\[Sysname-ospf-1-area-0.0.0.0\] network 192.168.0.0 0.0.255.255]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] ospf bfd enable]{lang="EN-US"}
:::::

::: {#-1677519710 .myid}
[]{#_Toc404788045}[]{#struct_0_x4702_18917_656234378}

**OSPF \-- OSPF配置命令 \-- ospf cost**

------------------------------------------------------------------------

[**[ospf cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x61369476}[命令用来配置接口运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议所需的开销。]{style="font-family:宋体"}

[**[undo ospf cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899246064}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1996455064}

[**[ospf cost ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_x4702_18917_x301287944}

[**[undo ospf cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x107327859}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1962036951}

[[接口按照当前的带宽自动计算接口运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x829943951}[协议所需的开销。对于]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_633888651}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1915817833}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899311600}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1470693675}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1886152888}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_613649941}

[*[value]{lang="EN-US"}*]{#struct_0_x4702_18917_x560847024}[：接口运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议所需的开销，]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，其他接口的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_43536902}

[[本命令可用来手动设置接口的开销值，否则]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_449582263}[会按照当前的带宽自动计算接口运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议所需的开销。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899770351}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x591925237}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x709655461}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的开销为]{style="font-family:宋体"}[65]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_983840940}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="NO-BOK"}[ospf cost 65]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x761109892}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x402984838}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的开销为]{style="font-family:宋体"}[65]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_208978994}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf cost 65]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899835887}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_x4702_18917_898529874}
:::

::: {#374033742 .myid}
[]{#_Toc404788046}[]{#struct_0_x4702_18917_2084432993}[]{#_Toc138212574}[]{#_Toc93984800}[]{#_Toc61236349}[]{#_Toc61093150}[]{#_Toc58812073}[]{#_Toc56887202}[]{#_Toc45164802}

**OSPF \-- OSPF配置命令 \-- ospf dr-priority**

------------------------------------------------------------------------

[**[ospf dr-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_x2110553544}[命令用来设置接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ospf dr-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_181712738}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1446938215}

[**[ospf dr-priority]{lang="EN-US"}***[ priority]{lang="EN-US"}*]{#struct_0_x4702_18917_x838000117}

[**[undo ospf dr-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_416801198}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899639279}

[[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_111328934}[优先级为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_781399464}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_741326576}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x833599180}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1630737081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_453621488}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1218981365}

[*[priority]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899704815}[：]{style="font-family:宋体"}[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1153750689}

[[接口的]{style="font-family:宋体"}[DR]{lang="EN-US"}]{#struct_0_x4702_18917_1403659432}[优先级决定了该接口在选举]{style="font-family:宋体"}[DR/BDR]{lang="EN-US"}[时所具有的资格，数值越大，优先级越高。优先级高的在选举权发生冲突时被首先考虑。如果一台设备的优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则它不会被选举为]{style="font-family:宋体"}[DR]{lang="EN-US"}[或]{style="font-family:宋体"}[BDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x217563880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x163547979}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1790792037}[设置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在选举]{style="font-family:宋体"}[DR]{lang="EN-US"}[时的优先级为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899508207}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf dr-priority 8]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_705609677}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_976179178}[设置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在选举]{style="font-family:宋体"}[DR]{lang="EN-US"}[时的优先级为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1226512859}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf dr-priority 8]{lang="EN-US"}
:::

::::: {#-1907742742 .myid}
[]{#_Toc138212576}[]{#_Toc93984802}[]{#_Toc61236352}[]{#_Toc61093151}[]{#_Toc58812074}[]{#_Toc56887203}[]{#_Toc45164803}[]{#_Toc404788047}[]{#struct_0_x4702_18917_x357716975}[]{#_Toc304551818}[]{#_Toc256677014}[]{#_Toc256677017}[]{#_Toc256677018}[]{#_Toc256677019}[]{#_Toc256677020}[]{#_Toc256677021}[]{#_Toc256677022}[]{#_Toc256677023}[]{#_Toc256677024}[]{#_Toc256677025}[]{#_Toc256677026}[]{#_Toc256677027}[]{#_Toc256677029}[]{#_Toc256677030}

**OSPF \-- OSPF配置命令 \-- ospf fast-reroute lfa-backup**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_1419261705}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_1508085964}
:::

[ ]{lang="EN-US"}

[**[ospf fast-reroute lfa-backup]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899573743}[命令用来使能接口参与]{style="font-family:
宋体"}[LFA]{lang="EN-US"}[（]{style="font-family:宋体"}[Loop Free Alternate]{lang="EN-US"}[）计算。]{style="font-family:宋体"}

[**[undo ospf fast-reroute lfa-backup]{lang="EN-US"}**]{#struct_0_x4702_18917_432724285}[命令用来禁止接口参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1190262694}

[**[ospf fast-reroute lfa-backup]{lang="EN-US"}**]{#struct_0_x4702_18917_584157354}

[**[undo ospf fast-reroute lfa-backup]{lang="EN-US"}**]{#struct_0_x4702_18917_x1375551840}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1924344129}

[[使能接口参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x4702_18917_x499303}[计算。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1781524886}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899377135}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2144125561}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1568286435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x635793026}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x216180914}

[[接口使能]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x4702_18917_x2083597797}[计算，使其有资格成为备份接口。去使能此配置后，则接口不会被选为备份接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_167560645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_757854307}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1899442671}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_688207243}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo ospf fast-reroute lfa-backup]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_836858042}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1128633070}[禁止接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1480280447}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] undo ospf fast-reroute lfa-backup]{lang="EN-US"}
:::::

::: {#-986079131 .myid}
[]{#_Toc404788048}[]{#struct_0_x4702_18917_1076755478}[]{#_Toc319594430}

**OSPF \-- OSPF配置命令 \-- ospf mib-binding**

------------------------------------------------------------------------

[**[ospf mib-binding]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899246063}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ospf mib-binding]{lang="EN-US"}**]{#struct_0_x4702_18917_x1895227705}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1673489146}

[**[ospf mib-binding]{lang="EN-US"}**[ *process-id*]{lang="EN-US"}]{#struct_0_x4702_18917_x617407733}

[**[undo ospf mib-binding]{lang="EN-US"}**]{#struct_0_x4702_18917_1160922938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_373701594}

[[MIB]{lang="EN-US"}]{#struct_0_x4702_18917_x148585075}[绑定在进程号最小的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_467841889}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899311599}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_901369499}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_249623790}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1226456955}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1220387184}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_110434768}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x252411434}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1118535151}*[process-id]{lang="FR"}*[不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:
宋体"}[OSPF]{lang="FR"}[进程绑定命令时将会提示]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[无法完成配置。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899770354}[OSPF]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[，]{style="font-family:宋体"}[若删除]{style="font-family:宋体"}*[process-id]{lang="FR"}*[对应的]{style="font-family:宋体"}[OSPF]{lang="FR"}[进程]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则同时删除]{style="font-family:宋体"}[OSPF]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[配置，]{style="font-family:宋体"}[MIB]{lang="EN-US"}[绑定到进程号最小的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x995209764}

[[\#]{lang="EN-US"}]{#struct_0_x4702_18917_641469450}[ ]{lang="EN-US" style="font-family:宋体"}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_2124265702}

[\[Sysname\] ospf mib-binding 100]{lang="EN-US"}
:::

::: {#-519698797 .myid}
[]{#_Toc404788049}[]{#struct_0_x4702_18917_x1676883636}

**OSPF \-- OSPF配置命令 \-- ospf mtu-enable**

------------------------------------------------------------------------

[**[ospf mtu-enable]{lang="EN-US"}**]{#struct_0_x4702_18917_1361188486}[命令用来配置]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文中]{style="font-family:宋体"}[MTU]{lang="EN-US"}[域的值为发送该报文接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo ospf mtu-enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x2098745651}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899835890}

[**[ospf mtu-enable]{lang="EN-US"}**]{#struct_0_x4702_18917_x667488531}

[**[undo ospf mtu-enable]{lang="EN-US"}**]{#struct_0_x4702_18917_578452590}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x827281959}

[[接口发送的]{style="font-family:宋体"}[DD]{lang="EN-US"}]{#struct_0_x4702_18917_x1103661748}[报文中]{style="font-family:宋体"}[MTU]{lang="EN-US"}[域的值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1076424206}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1457776062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1099438284}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1899639282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1099507687}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x485801695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{lang="EN-US" style="font-family:宋体"}[Virtual-Template]{lang="EN-US"}]{#struct_0_x4702_18917_x1671513584}[或]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[建立虚连接后，不同厂商的设备接口发送的]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文中]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[域的缺省值可能不同，为了保证一致，应该将接口发送的]{lang="EN-US" style="font-family:宋体"}[DD]{lang="EN-US"}[报文中]{lang="EN-US" style="font-family:宋体"}[MTU]{lang="EN-US"}[域的值恢复为缺省值]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置了该命令后，接收到]{style="font-family:宋体"}]{#struct_0_x4702_18917_1780652825}[DD]{lang="EN-US"}[报文时会检查报文中的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值是否大于接收接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，如果大于则将报文丢弃。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1334604297}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_704505379}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_574272956}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[在发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文时，填写]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899704818}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\][]{#_Hlt581565} ospf mtu-enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1557035216}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_141680138}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[在发送]{style="font-family:宋体"}[DD]{lang="EN-US"}[报文时，填写]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1265340298}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf mtu-enable]{lang="EN-US"}
:::

::: {#-629374641 .myid}
[]{#_Toc404788050}[]{#struct_0_x4702_18917_158618600}[]{#_Toc138212577}[]{#_Toc93984803}[]{#_Toc61236353}[]{#_Toc61093152}[]{#_Toc58812075}[]{#_Toc56887204}[]{#_Toc45164804}

**OSPF \-- OSPF配置命令 \-- ospf network-type**

------------------------------------------------------------------------

[**[ospf network-type]{lang="EN-US"}**]{#struct_0_x4702_18917_x835755896}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口的网络类型。]{style="font-family:宋体"}

[**[undo ospf network-type]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899508210}[命令用来将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口网络类型恢复为缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_302259614}

[**[ospf network-type]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **broadcast** \| **nbma** \| **p2mp** \[ **unicast** \] \| **p2p** \[ **peer-address-check** \] }]{lang="EN-US"}]{#struct_0_x4702_18917_597574281}

[**[undo ospf network-type]{lang="EN-US"}**]{#struct_0_x4702_18917_1144720865}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1985430395}

[[当接口封装的链路层协议不同时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1664251637}[接口网络类型的缺省值也不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_x4702_18917_1832962215}[Ethernet]{lang="EN-US"}[、]{style="font-family:宋体"}[FDDI]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口网络类型的缺省值为广播类型；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1521615573}[ATM]{lang="EN-US"}[、帧中继或]{style="font-family:宋体"}[X.25]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口网络类型的缺省值为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当接口封装的链路层协议是]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899573746}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[LAPB]{lang="EN-US"}[、]{style="font-family:宋体"}[HDLC]{lang="EN-US"}[或]{style="font-family:宋体"}[POS]{lang="EN-US"}[时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口网络类型的缺省值为点对点。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_29439758}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1578183202}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x98743683}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x2010698207}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1675150653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1956459754}

[**[broadcast]{lang="EN-US"}**]{#struct_0_x4702_18917_x1903864635}[：配置]{style="font-family:宋体"}[接口的网络类型为广播类型。]{style="font-family:宋体"}

[**[nbma]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899377138}[：配置接口的网络类型为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[**[p2mp]{lang="EN-US"}**]{#struct_0_x4702_18917_1740841034}[：配置接口的网络类型为点到多点类型。]{style="font-family:宋体"}

[**[unicast]{lang="EN-US"}**]{#struct_0_x4702_18917_972404587}[：]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[类型支持单播发送报文，缺省情况下是组播方式发送报文。]{style="font-family:宋体"}

[**[p2p]{lang="EN-US"}**]{#struct_0_x4702_18917_x2068057187}[：配置接口的网络类型为点到点类型。]{style="font-family:宋体"}

[**[peer-address-check]{lang="EN-US"}**]{#struct_0_x4702_18917_1618325055}[：配置建立邻接关系必须在同一网段的检查功能，即在接收]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时，对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与当前接口必须在同一网段。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1499408653}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在广播网络上有不支持组播地址的路由器，可以将接口的网络类型改为]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1080938247}[NBMA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x4702_18917_2083866587}[NBMA]{lang="EN-US"}[网络中，如果任意两台路由器之间都有一条虚电路直接可达，或者说，这个网络是全连通的，那么可以把]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口的网路类型配置为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[；否则，需要把]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口的网络类型配置为点到多点，这样，两台不能直接可达的路由器之间可以通过一台与两者都直接可达的路由器来交换路由信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口的网络类型为]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899442674}[NBMA]{lang="EN-US"}[或]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[（]{style="font-family:宋体"}[unicast]{lang="EN-US"}[）时，必须使用]{style="font-family:宋体"}**[peer]{lang="EN-US"}**[命令来配置邻接点。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果一网段内只有两台路由器运行]{style="font-family:宋体"}]{#struct_0_x4702_18917_1447722130}[OSPF]{lang="EN-US"}[协议，也可以将接口的网络类型改为点到点。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接口的网络类型为]{style="font-family:宋体"}]{#struct_0_x4702_18917_980965954}[P2MP]{lang="EN-US"}[（]{style="font-family:宋体"}[unicast]{lang="EN-US"}[）时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议在该接口上发送的报文均为单播报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2113886911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x1121918765}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1068728732}[将接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[设置为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1298722031}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf network-type nbma]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x882086119}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1899246066}[将接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[设置为]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1135712818}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf network-type nbma]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x641373516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf dr-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_2014223472}
:::

::: {#-1079391663 .myid}
[]{#_Toc138212578}[]{#_Toc93984804}[]{#_Toc61236354}[]{#_Toc61093153}[]{#_Toc58812076}[]{#_Toc56887205}[]{#_Toc45164805}[]{#_Toc404788051}[]{#struct_0_x4702_18917_x1837131124}[]{#_Toc332297430}[]{#_Toc329939882}[]{#_Toc326055192}[]{#_Toc256677035}[]{#_Toc256677036}[]{#_Toc256677037}[]{#_Toc256677038}[]{#_Toc256677039}[]{#_Toc256677040}[]{#_Toc256677041}[]{#_Toc256677042}[]{#_Toc256677043}[]{#_Toc256677044}[]{#_Toc256677045}[]{#_Toc256677046}[]{#_Toc256677047}[]{#_Toc256677048}[]{#_Toc256677049}[]{#_Toc256677051}

**OSPF \-- OSPF配置命令 \-- ospf prefix-suppression**

------------------------------------------------------------------------

[**[ospf prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_2021334072}[命令用来抑制接口进行前缀发布。]{style="font-family:宋体"}

[**[undo ospf prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_1919112269}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899311602}

[**[ospf prefix-suppression]{lang="EN-US"}**[ \[ **disable** \]]{lang="EN-US"}]{#struct_0_x4702_18917_1661474207}

[**[undo ospf prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_1682187699}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1038538010}

[[不抑制接口进行前缀发布。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x2067482287}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_990645284}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_2138724308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899770353}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_570874177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x168261592}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x197094092}

[**[disable]{lang="EN-US"}**]{#struct_0_x4702_18917_x1597573212}[：不抑制接口进行前缀发布。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x122566036}

[[接口配置不能抑制从地址对应的前缀。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1936517118}

[[如果]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x499821948}[进程配置了抑制前缀发布，但某个接口不想进行抑制，此时可以配置本命令并指定]{style="font-family:宋体"}**[disable]{lang="EN-US"}**[参数。]{style="font-family:宋体"}

[[具体内容请参见命令]{style="font-family:宋体"}**[prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899835889}[中的使用指导。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1705098928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_x4702_18917_929745091}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x356551216}[抑制接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[进行前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1699447344}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ospf prefix-suppression]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1659168615}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1720611000}[抑制接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[进行前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899639281}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf prefix-suppression]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_466576254}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x902420377}
:::

::::: {#1538163757 .myid}
[]{#_Toc404788052}[]{#struct_0_x4702_18917_1618062910}[]{#_Toc364260695}[]{#_Toc363978692}[]{#_Toc356229217}

**OSPF \-- OSPF配置命令 \-- ospf primary-path-detect bfd echo**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](OSPF命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x4702_18917_154934255}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x4702_18917_1617997374}
:::

**[ ]{lang="EN-US"}**

[**[ospf primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x4702_18917_1617931838}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[**[undo ospf primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x4702_18917_719884131}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1617866302}

[**[ospf primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x4702_18917_372305234}

[**[undo ospf primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x4702_18917_1618325054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1332503323}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1618259518}[协议中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1618193982}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1690674988}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1618128446}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1327213025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1618587198}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1814791901}

[[配置本功能后，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1618521662}[协议的快速重路由特性和]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中的主用链路将使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）进行检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1618062909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_154344430}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1617997373}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1617931837}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] fast-reroute lfa]{lang="EN-US"}

[\[Sysname-ospf-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf primary-path-detect bfd echo]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_720867171}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1617866301}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] pic additional-path-always]{lang="EN-US"}

[\[Sysname-ospf-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ospf primary-path-detect bfd echo]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1618325053}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1332568859}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1618259517}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] fast-reroute lfa]{lang="EN-US"}

[\[Sysname-ospf-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf primary-path-detect bfd echo]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1618193981}[在接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[上配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1618128445}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] pic additional-path-always]{lang="EN-US"}

[\[Sysname-ospf-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] ospf primary-path-detect bfd echo]{lang="EN-US"}
:::::

::: {#-629215129 .myid}
[]{#_Toc404788053}[]{#struct_0_x4702_18917_x1561726617}

**OSPF \-- OSPF配置命令 \-- ospf timer dead**

------------------------------------------------------------------------

[**[ospf timer dead]{lang="EN-US"}**]{#struct_0_x4702_18917_1943564221}[命令用来设置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的邻居失效时间。]{style="font-family:宋体"}

[**[undo ospf timer dead]{lang="EN-US"}**]{#struct_0_x4702_18917_1810133189}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x296442067}

[**[ospf timer dead ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899704817}

[**[undo ospf timer dead]{lang="EN-US"}**]{#struct_0_x4702_18917_x1978417193}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1428158366}

[[P2P]{lang="EN-US"}]{#struct_0_x4702_18917_x1687758693}[、]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[类型接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居失效的时间为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒；]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[、]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口的]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居失效的时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x29629458}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_794032103}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1911922313}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1286399287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1899508209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1512178731}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x1444828706}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居失效的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_801763436}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1945170142}[邻居的失效时间是指：在该时间间隔内，若未收到邻居的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，就认为该邻居已失效。]{style="font-family:宋体"}**[dead]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值至少应为]{style="font-family:宋体"}**[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍，同一网段上的接口的]{style="font-family:宋体"}**[dead ]{lang="EN-US"}***[seconds]{lang="EN-US"}*[也必须相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1843838021}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x443718982}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_437499473}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的邻居失效时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899573745}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf timer dead 60]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1595523699}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1396243007}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上的邻居失效时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x119538914}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf timer dead 60]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2015660201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf timer hello]{lang="EN-US"}**]{#struct_0_x4702_18917_1067923917}
:::

::: {#78597007 .myid}
[]{#_Toc404788054}[]{#struct_0_x4702_18917_x1021661065}[]{#_Toc138212579}[]{#_Toc93984805}[]{#_Toc61236355}[]{#_Toc61093154}[]{#_Toc58812077}[]{#_Toc56887206}[]{#_Toc45164806}

**OSPF \-- OSPF配置命令 \-- ospf timer hello**

------------------------------------------------------------------------

[**[ospf timer hello]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899377137}[命令用来配置接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ospf timer hello]{lang="EN-US"}**]{#struct_0_x4702_18917_x988042321}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_187914962}

[**[ospf timer hello ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x880534669}

[**[undo ospf timer hello]{lang="EN-US"}**]{#struct_0_x4702_18917_x609544391}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1589625781}

[[P2P]{lang="EN-US"}]{#struct_0_x4702_18917_1741864510}[、]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[类型接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒；]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[、]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2117308318}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899442673}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1851006657}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1897621874}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x103029815}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1856440816}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x43637620}[：接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_216922364}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899246065}[的值越小，发现网络拓扑改变的速度越快，对系统资源的开销也就越大。同一网段上的接口的]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[必须相同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x732428291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_840271731}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1753586496}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x2098894638}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf timer hello 20]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_532244688}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_695810594}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899311601}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf timer hello 20]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1258189680}

[[·[              ]{style="font:7.0pt "}]{lang="NO-BOK" style="font-size:10.0pt;font-family:Symbol"}**[ospf timer dead]{lang="EN-US"}**]{#struct_0_x4702_18917_x2084416217}
:::

::: {#1703168917 .myid}
[]{#_Toc404788055}[]{#struct_0_x4702_18917_1432127049}[]{#_Toc138212580}[]{#_Toc93984806}[]{#_Toc61236356}[]{#_Toc61093155}[]{#_Toc58812078}[]{#_Toc56887207}[]{#_Toc45164807}

**OSPF \-- OSPF配置命令 \-- ospf timer poll**

------------------------------------------------------------------------

[**[ospf timer poll]{lang="EN-US"}**]{#struct_0_x4702_18917_857913135}[命令用来配置在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[接口上向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ospf timer poll]{lang="EN-US"}**]{#struct_0_x4702_18917_1210505752}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1404265040}

[**[ospf timer poll]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x4702_18917_468478775}

[**[undo ospf timer poll]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899770356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_167589650}

[[在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}]{#struct_0_x4702_18917_x1595936864}[接口上向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1456537370}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x498249826}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1413280754}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x551909367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1899835892}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_495310883}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_361346182}[：]{style="font-family:宋体"}[向状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的邻居路由器发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483647]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1428654217}

[[在]{style="font-family:宋体"}[NBMA]{lang="EN-US"}]{#struct_0_x4702_18917_1881760049}[的网络上，当邻居失效后，将按轮询时间间隔定期地发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。用户可配置轮询时间间隔以指定该接口在与相邻路由器构成邻居关系之前发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x1018202347}[报文的时间间隔至少应为发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时间间隔的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x138985145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x1064985619}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1899639284}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[130]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x292938633}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf timer poll 130]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x1593278031}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1688682113}[配置接口上]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送轮询]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[130]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x160657926}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf timer poll 130]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1114264001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf timer hello]{lang="EN-US"}**]{#struct_0_x4702_18917_x889333805}
:::

::: {#1157305494 .myid}
[]{#_Toc45164810}[]{#_Toc404788056}[]{#struct_0_x4702_18917_x1899704820}[]{#_Toc138212581}[]{#_Toc93984807}[]{#_Toc61236357}[]{#_Toc61093156}[]{#_Toc58812079}[]{#_Toc56887208}[]{#_Toc45164808}

**OSPF \-- OSPF配置命令 \-- ospf timer retransmit**

------------------------------------------------------------------------

[**[ospf timer retransmit]{lang="EN-US"}**]{#struct_0_x4702_18917_1913200040}[命令用来配置接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔。]{style="font-family:宋体"}

[**[undo ospf timer retransmit]{lang="EN-US"}**]{#struct_0_x4702_18917_2095973739}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x465441521}

[**[ospf timer retransmit ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_805148129}

[**[undo ospf timer retransmit]{lang="EN-US"}**]{#struct_0_x4702_18917_x1389114988}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1851488751}

[[接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x874198688}[的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899508212}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1465059028}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2020418449}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1238709065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x324114746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x256102811}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x1837758255}[：]{style="font-family:宋体"}[接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x527969746}

[[当一台路由器向它的邻居发送一条]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1899573748}[后，需要等到对方的确认报文。若在该重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时间间隔内未收到对方的确认报文，就会重传这条]{style="font-family:宋体"}[LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[请合理配置接口重传]{style="font-family:宋体"}]{#struct_0_x4702_18917_1192239172}[LSA]{lang="EN-US"}[的时间间隔，避免引起不必要的重传。比如，对于低速链路，可以适当把这个时间间隔值设置大一点。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1672855683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_816082570}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_350139748}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[与邻接路由器之间传送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的重传间隔为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1447266081}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ospf timer retransmit 8]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_808130469}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1899377140}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[与邻接路由器之间传送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的重传间隔为]{style="font-family:宋体"}[8]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1385069426}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf timer retransmit 8]{lang="NO-BOK"}
:::

::: {#1622155945 .myid}
[]{#_Toc404788057}[]{#struct_0_x4702_18917_1822639927}[]{#_Toc138212582}[]{#_Toc93984808}[]{#_Toc61236358}[]{#_Toc61093157}[]{#_Toc58812080}[]{#_Toc56887209}[]{#_Toc45164809}

**OSPF \-- OSPF配置命令 \-- ospf trans-delay**

------------------------------------------------------------------------

[**[ospf trans-delay]{lang="EN-US"}**]{#struct_0_x4702_18917_x462861041}[命令用来配置接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的传输延迟时间。]{style="font-family:宋体"}

[**[undo ospf trans-delay]{lang="EN-US"}**]{#struct_0_x4702_18917_1323013727}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1800049075}

[**[ospf trans-delay ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x1266729630}

[**[undo ospf trans-delay]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899442676}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1684445752}

[[接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x598736528}[的传输延迟时间为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1635774597}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1570567081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_188840818}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1596248606}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_125416470}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1899246068}

[*[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_27086596}[：接口对]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的传输延迟时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1923011263}

[[LSA]{lang="EN-US"}]{#struct_0_x4702_18917_x1796904105}[在本路由器的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中会随时间老化（]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的老化时间每秒钟加]{style="font-family:宋体"}[1]{lang="EN-US"}[），但在网络的传输过程中却不会，所以有必要在发送之前在]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的老化时间上增加一定的延迟时间。此配置对低速率的网络尤其重要。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1834579392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_1086211262}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1626467409}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上传送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时延值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1899311604}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="NO-BOK"}[ospf trans-delay 3]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_498674793}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x796671838}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上传送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的时延值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x797920822}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ospf trans-delay 3]{lang="EN-US"}
:::

::: {#1903411553 .myid}
[]{#_Toc404788058}[]{#struct_0_x4702_18917_1492002443}[]{#_Toc138212583}[]{#_Toc93984809}[]{#_Toc61236359}[]{#_Toc61093160}[]{#_Toc58812083}[]{#_Toc56887212}

**OSPF \-- OSPF配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_x4702_18917_x1899770355}[命令用来配置]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[网络或]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[单播网络的邻居。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**]{#struct_0_x4702_18917_1733673591}[命令用来取消该操作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2027587964}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[ \[ **cost** *value* \| **dr-priority** *dr-priority* \]]{lang="EN-US"}]{#struct_0_x4702_18917_1499312873}

[**[undo peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899835891}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2061394824}

[[没有配置邻居。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1899639283}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1629375668}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_960812595}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_761497820}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_851743071}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1636032952}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x680451975}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899704819}[：邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ value]{lang="EN-US"}*]{#struct_0_x4702_18917_x1171848139}[：邻居的开销，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dr-priority ]{lang="EN-US"}***[dr-priority]{lang="EN-US"}*]{#struct_0_x4702_18917_x1899508211}[：邻居的优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1868343555}

[[NBMA]{lang="EN-US"}]{#struct_0_x4702_18917_x1899377139}[网络或]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[单播网络采用单播形式发送协议报文，必须手工指定邻居。]{style="font-family:宋体"}

[[本命令设置的开销值仅用于]{style="font-family:宋体"}[P2MP]{lang="EN-US"}]{#struct_0_x4702_18917_x1899442675}[链路上建立的邻居，如果没有配置开销值，去往该邻居的花费等于接口的开销值。]{style="font-family:宋体"}

[[本命令设置的优先级仅用于表示路由器是否主动向该邻居发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x4702_18917_x1899246067}[报文，并不用于实际的]{style="font-family:宋体"}[DR]{lang="EN-US"}[选举，]{style="font-family:宋体"}**[ospf dr-priority]{lang="EN-US"}**[命令设置的优先级用于实际的]{style="font-family:宋体"}[DR]{lang="EN-US"}[选举。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_430371123}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1899311603}[指定邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_95390266}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] peer 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_699145488}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf dr-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_876023064}
:::

::: {#537581611 .myid}
[]{#_Toc138212584}[]{#_Toc93984810}[]{#_Toc61236360}[]{#_Toc61093161}[]{#_Toc58812084}[]{#_Toc56887213}[]{#_Toc45164811}[]{#_Toc404788059}[]{#struct_0_x4702_18917_x333686411}[]{#_Toc332297437}[]{#_Toc329939884}

**OSPF \-- OSPF配置命令 \-- pic**

------------------------------------------------------------------------

[**[pic]{lang="EN-US"}**]{#struct_0_x4702_18917_760084894}[命令用来使能前缀无关收敛功能。]{style="font-family:宋体"}

[**[undo pic]{lang="EN-US"}**]{#struct_0_x4702_18917_197374023}[命令用来]{style="font-family:宋体"}[关闭前缀无关收敛功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_861156521}

[**[pic]{lang="EN-US"}**[ \[ **additional-path-always** \]]{lang="EN-US"}]{#struct_0_x4702_18917_1103199290}

[**[undo pic]{lang="EN-US"}**]{#struct_0_x4702_18917_x1319289545}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x105187515}

[[使能前缀无关收敛功能。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1429909839}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333751947}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1124110825}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2122809612}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x228999856}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_731192109}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1546356762}

[**[additional-path-always]{lang="EN-US"}**]{#struct_0_x4702_18917_x1106072340}[：支持非直连的次优路由作为备份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333555339}

[[PIC]{lang="EN-US"}]{#struct_0_x4702_18917_1991613292}[（]{style="font-family:宋体"}[Prefix Independent Convergence]{lang="EN-US"}[，前缀无关收敛），即收敛时间与前缀数量无关，加快收敛速度。传统的路由计算快速收敛都与前缀数量相关，收敛时间与前缀数量成正比。]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[只实现区域间路由以及外部路由的前缀无关收敛。]{style="font-family:宋体"}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_875231905}[快速重路由功能和]{style="font-family:宋体"}[PIC]{lang="EN-US"}[同时配置时，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[快速重路由功能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1740664636}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x945393370}[使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的]{style="font-family:宋体"}[PIC]{lang="EN-US"}[支持非直连次优路由做备份功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_124230745}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] pic additional-path-always]{lang="EN-US"}
:::

::: {#830408614 .myid}
[]{#_Toc404788060}[]{#struct_0_x4702_18917_1782578415}

**OSPF \-- OSPF配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_x4702_18917_x333620875}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议路由的优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_x4702_18917_x358423850}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1123904325}

[**[preference]{lang="EN-US"}**[ \[ **ase** \] { *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_x4702_18917_862210303}

[**[undo preference]{lang="EN-US"}**[ \[ **ase** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1394627749}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_565941666}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1920640780}[内部路由的优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[外部路由的优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_617197947}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x333424267}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1537142739}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1787969981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1450521113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x486101036}

[**[ase]{lang="EN-US"}**]{#struct_0_x4702_18917_960149761}[：配置外部路由的优先级。如果未指定该参数，配置内部路由优先级。]{style="font-family:宋体"}

[*[preference]{lang="EN-US"}*]{#struct_0_x4702_18917_1124519617}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。优先级的值越小，其实际的优先程度越高。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x993550625}[：应用路由策略，对特定的路由设置优先级。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[是路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333489803}

[[配置了]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1747428403}**[route-policy]{lang="EN-US"}**[参数后，如果]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[中对某些匹配的路由优先级进行了修改，则这些匹配的路由取]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[修改的优先级，其它路由的优先级均取]{style="font-family:宋体"}**[preference]{lang="EN-US"}**[命令所设的值。]{style="font-family:宋体"}

[[由于路由器上可能同时运行多个动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题，所以为每一种路由协议指定了一个缺省的优先级。在不同的路由协议发现去往同一目的地的多条路由时，优先级高的协议发现的路由将被选中以转发]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_1551307472}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2090464503}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1390534884}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议外部路由的优先级为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x661604833}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] preference ase 200]{lang="EN-US"}

[]{#_Toc138212585}[]{#_Toc93984811}[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x240323600}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议内部路由的优先级，]{style="font-family:宋体"}[匹配路由策]{style="font-family:宋体"}[略]{style="font-family:宋体"}[pre]{lang="EN-US"}[的路由优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[，未匹配的路由优先级为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x333293195}

[\[Sysname\] ip prefix-list test index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy pre permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] if-match ip address prefix-list test]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] apply preference 100]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] preference route-policy pre 150]{lang="EN-US"}
:::

::: {#-330683803 .myid}
[]{#_Toc404788061}[]{#struct_0_x4702_18917_1543788163}[]{#_Toc332297440}

**OSPF \-- OSPF配置命令 \-- prefix-priority**

------------------------------------------------------------------------

[**[prefix-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_1735321670}[命令用来使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的前缀按优先权快速收敛功能。]{style="font-family:宋体"}

[**[undo prefix-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_x428433245}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的前缀按优先权快速收敛功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x504013011}

[**[prefix-priority route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x4702_18917_1054505955}

[**[undo prefix-priority]{lang="EN-US"}**]{#struct_0_x4702_18917_779410788}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333358731}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x422410483}[的]{style="font-family:宋体"}[前缀按优先权快速收敛]{style="font-family:宋体"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1611988640}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x281900460}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1885357385}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1462228318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_950841141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1975339607}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_x4702_18917_x333162123}[：应用路由策略，对特定的路由前缀设置]{style="font-family:宋体"}[优先]{style="font-family:宋体"}[权]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[是路由策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:
黑体"}]{#struct_0_x4702_18917_3853124}

[[通过策略指定优先权，不同前缀按优先权顺序下发，由高到低分为]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_x4702_18917_1591362215}[个优先权（]{style="font-family:宋体"}[Critical]{lang="EN-US"}[、]{style="font-family:宋体"}[High]{lang="EN-US"}[、]{style="font-family:宋体"}[Medium]{lang="EN-US"}[和]{style="font-family:宋体"}[Low]{lang="EN-US"}[），如果一条路由符合多个收敛优先权的匹配规则，则这些收敛优先权中最高者当选为路由的收敛优先权。]{style="font-family:宋体"}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1461162088}[路由的]{style="font-family:宋体"}[32]{lang="EN-US"}[位主机路由为]{style="font-family:宋体"}[Medium]{lang="EN-US"}[优先权，其它为]{style="font-family:宋体"}[Low]{lang="EN-US"}[优先权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1731681011}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1856767888}[配置通过路由策略]{style="font-family:宋体"}[pre]{lang="EN-US"}[修改特定路由前缀的优先权为]{style="font-family:宋体"}[Medium]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x333227659}

[\[Sysname\] ip prefix-list test index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy pre permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] if-match ip address prefix-list test]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] apply prefix-priority medium]{lang="EN-US"}

[\[Sysname-route-policy-pre-10\] quit]{lang="EN-US"}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] prefix-priority route-policy pre]{lang="EN-US"}
:::

::: {#56918495 .myid}
[]{#_Toc404788062}[]{#struct_0_x4702_18917_1957331995}[]{#_Toc332297441}[]{#_Toc329939880}[]{#_Toc326055191}

**OSPF \-- OSPF配置命令 \-- prefix-suppression**

------------------------------------------------------------------------

[**[prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x1464749934}[命令用来抑制]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程进行前缀发布。]{style="font-family:宋体"}

[**[undo prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_800144969}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1365420421}

[**[prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x577387073}

[**[undo prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_1739475261}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1629146509}

[[不抑制]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x333686410}[进程进行前缀发布。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_760019358}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x2146855503}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_434264767}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1963780241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x419933329}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1099658543}

[[如果需要抑制前缀发布，建议整个]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x333751946}[网络都配置本命令。]{style="font-family:宋体"}

[[全局配置不能抑制从地址、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}]{#struct_0_x4702_18917_x1124045289}[接口以及处于抑制状态的接口对应的前缀。如果想对]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[接口或处于抑制状态的接口进行抑制，可以通过配置接口前缀抑制（]{style="font-family:宋体"}**[ospf prefix-suppression]{lang="EN-US"}**[命令）来实现。]{style="font-family:宋体"}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x2138925345}[使能网段时会将接口上匹配该网段的所有网段路由与主机路由都通过]{style="font-family:宋体"}[LSA]{lang="EN-US"}[发布，但有时候主机路由或网段路由是不希望被发布的。通过前缀抑制配置，可以减少]{style="font-family:宋体"}[LSA]{lang="EN-US"}[中携带不需要的前缀，即不发布某些网段路由和主机路由，从而提高网络安全性，加快路由收敛。]{style="font-family:宋体"}

[[当使能前缀抑制时，具体情况如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_381237740}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_x4702_18917_x816680739}[或]{style="font-family:宋体"}[P2MP]{lang="EN-US"}[类型网络：]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中不发布接口的主地址，即]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中链路类型为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[Stub]{lang="EN-US"}[链路被抑制]{style="font-family:宋体"}[，不生成接口路由，但其他路由信息可以正常计算，不会影响流量转发]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[广播类型或者]{style="font-family:宋体"}]{#struct_0_x4702_18917_1264702172}[NBMA]{lang="EN-US"}[网络：]{style="font-family:宋体"}[DR]{lang="EN-US"}[发布的]{style="font-family:宋体"}[Type-2 LSA]{lang="EN-US"}[的掩码字段会填成]{style="font-family:宋体"}[32]{lang="EN-US"}[位，即不生成网段路由]{style="font-family:宋体"}[，但其他路由信息可以正常计算，不会影响流量转发]{style="font-family:宋体"}[。另外，如果没有邻居，发布的]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中也不发布接口的主地址，即]{style="font-family:宋体"}[Type-1 LSA]{lang="EN-US"}[中链路类型为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[Stub]{lang="EN-US"}[链路被抑制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1792983896}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_728803736}[抑制]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的前缀发布。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x333555338}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] prefix-suppression]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1991678828}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ospf ]{lang="EN-US"}[prefix-suppression]{lang="EN-US"}**]{#struct_0_x4702_18917_x1798851695}
:::

::: {#-1771697101 .myid}
[]{#_Toc404788063}[]{#struct_0_x4702_18917_x1591555204}

**OSPF \-- OSPF配置命令 \-- reset ospf statistics**

------------------------------------------------------------------------

[**[reset ospf statistics]{lang="EN-US"}**]{#struct_0_x4702_18917_x764284798}[命令用来清除]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x726469882}

[**[reset ospf]{lang="EN-US"}**[ \[ *process-id* \] **statistics**]{lang="EN-US"}]{#struct_0_x4702_18917_873929426}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333620874}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x358489386}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_809509582}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1613574139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1583591173}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1360925850}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_1467365769}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1482005236}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333424266}[清除所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ospf statistics]{lang="EN-US"}]{#struct_0_x4702_18917_x1537208275}

[【相关命令】]{style="font-family:黑体"}

[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ospf statistics]{lang="EN-US"}**
:::

::: {#1878669517 .myid}
[]{#_Toc404788064}[]{#struct_0_x4702_18917_2026042320}[]{#_Toc352328988}[]{#_Toc345073435}

**OSPF \-- OSPF配置命令 \-- reset ospf event-log**

------------------------------------------------------------------------

[**[reset ospf event-log]{lang="EN-US"}**]{#struct_0_x4702_18917_2025976784}[命令用于清]{style="font-family:宋体"}[除]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的]{style="font-family:宋体"}[日志]{style="font-family:宋体"}[信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2026697680}

[**[reset ospf]{lang="EN-US"}**[ \[ *process-id* \] **event-log** \[ **lsa-flush** \| **peer** \| **spf** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1625640194}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_2026632144}

[[用户]{style="font-family:宋体"}]{#struct_0_x4702_18917_x824045349}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x702709966}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x702775502}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1400715403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x702578894}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x2106288607}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果]{style="font-family:宋体"}[未指定本参数，]{style="font-family:宋体"}[则清除所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程的日志信息。]{style="font-family:宋体"}

[**[lsa-flush]{lang="EN-US"}**]{#struct_0_x4702_18917_x1143912649}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[老化日志信息个数。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_x4702_18917_x702644430}[：]{style="font-family:宋体"}[清除邻居的日志信息。]{style="font-family:宋体"}

[**[spf]{lang="EN-US"}**]{#struct_0_x4702_18917_x702972110}[：]{style="font-family:宋体"}[清除路由计算的日志信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_242944143}

[[如果未指定日志类型，则所有日志信息都被清除。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x703037646}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x162902454}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x702841038}[清除所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程路由计算的日志]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ospf event-log spf]{lang="EN-US"}]{#struct_0_x4702_18917_x702906574}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1820842745}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_x4702_18917_x702185678}**[ ospf event-log]{lang="EN-US"}**
:::

::: {#-721415525 .myid}
[]{#_Toc45164814}[]{#_Toc61236363}[]{#_Toc61093165}[]{#_Toc58812088}[]{#_Toc56887217}[]{#_Toc45164824}[]{#_Toc404788065}[]{#struct_0_x4702_18917_430640070}[]{#_Toc138212586}[]{#_Toc93984812}

**OSPF \-- OSPF配置命令 \-- reset ospf process**

------------------------------------------------------------------------

[**[reset ospf process]{lang="EN-US"}**]{#struct_0_x4702_18917_x907079829}[命令用来重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1646266867}

[**[reset ospf]{lang="EN-US"}**[ \[ *process-id* \] **process** \[ **graceful-restart** \]]{lang="EN-US"}]{#struct_0_x4702_18917_x1444706185}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x2022172209}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_167095395}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333489802}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1551241936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1810517834}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1751264030}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x2004987163}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x4702_18917_1935889157}[：以]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1682588755}

[[如果未指定]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x870460943}[，]{style="font-family:宋体"}[则重启所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}**[reset ospf process]{lang="EN-US"}**]{#struct_0_x4702_18917_x333293194}[命令重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[，可以获得如下结果：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以立即清除无效的]{style="font-family:宋体"}]{#struct_0_x4702_18917_1543853699}[LSA]{lang="EN-US"}[，而不必等到]{style="font-family:宋体"}[LSA]{lang="EN-US"}[超时。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果改变了]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_1396559419}[，该命令的执行会导致新的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[方便重新选举]{style="font-family:宋体"}]{#struct_0_x4702_18917_1444822680}[DR]{lang="EN-US"}[、]{style="font-family:宋体"}[BDR]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重启前的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1644799584}[OSPF]{lang="EN-US"}[配置不会丢失。]{style="font-family:宋体"}

[[执行该命令后，系统提示用户确认是否重启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_371713839}[协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x666525342}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333358730}[重启所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[\<Sysname\> reset ospf process]{lang="EN-US"}]{#struct_0_x4702_18917_x422344947}

[Reset OSPF process? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#137726923 .myid}
[]{#_Toc404788066}[]{#struct_0_x4702_18917_1941909135}[]{#_Toc138212587}[]{#_Toc93984813}[]{#_Toc61236362}[]{#_Toc61093163}[]{#_Toc58812086}[]{#_Toc56887215}[]{#_Toc45164813}

**OSPF \-- OSPF配置命令 \-- reset ospf redistribution**

------------------------------------------------------------------------

[**[reset ospf redistribution]{lang="EN-US"}**]{#struct_0_x4702_18917_706370593}[命令用来重新向]{style="font-family:
宋体"}[OSPF]{lang="EN-US"}[引入外部路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_842694791}

[**[reset ospf]{lang="EN-US"}**[ \[ *process-id* \] **redistribution**]{lang="EN-US"}]{#struct_0_x4702_18917_2070993396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_282303439}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x31173396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333162122}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_3787588}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1582351008}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_216984623}

[*[process-id]{lang="EN-US"}*]{#struct_0_x4702_18917_147194344}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1915180929}

[[如果未指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1914503333}[进程号，所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程都将重新引入外部路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x410472132}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333227658}[重新向]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[引入外部路由。]{style="font-family:宋体"}

[[\<Sysname\> reset ospf redistribution]{lang="EN-US"}]{#struct_0_x4702_18917_1957266459}
:::

::: {#1486818244 .myid}
[]{#_Toc404788067}[]{#struct_0_x4702_18917_2105043380}[]{#_Toc138212588}[]{#_Toc93984814}

**OSPF \-- OSPF配置命令 \-- rfc1583 compatible**

------------------------------------------------------------------------

[**[rfc1583 compatible]{lang="EN-US"}**]{#struct_0_x4702_18917_165454534}[命令用来使能兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[的路由选择优先规则。]{style="font-family:宋体"}

[**[undo rfc1583 compatible]{lang="EN-US"}**]{#struct_0_x4702_18917_1503518050}[命令用来禁止此方式。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_360957977}

[**[rfc1583 compatible]{lang="EN-US"}**]{#struct_0_x4702_18917_1587885376}

[**[undo rfc1583 compatible]{lang="EN-US"}**]{#struct_0_x4702_18917_x333686413}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_760215966}

[[使能兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}]{#struct_0_x4702_18917_2004558777}[的路由选择优先规则。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1237861275}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1118939535}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x440986547}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_960910861}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1182525097}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333751949}

[[当有多条路径可以到达同一个外部路由时，在选择最优路由的问题上，]{style="font-family:宋体"}[RFC 2328]{lang="EN-US"}]{#struct_0_x4702_18917_x1124766185}[中定义的选路规则与]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[的有所不同，进行此配置可以兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[中定义的规则。]{style="font-family:宋体"}

[[具体的选路规则如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_681705002}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[当]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1457002590}[RFC 2328]{lang="EN-US"}[兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[时，所有到达]{style="font-family:宋体"}[ASBR]{lang="EN-US"}[的路由优先级相同。当]{style="font-family:宋体"}[RFC 2328]{lang="EN-US"}[不兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[时，非骨干区的区域内路由优先级最高，区域间路由与骨干区区域内路由优先级相同，优选非骨干区的区域内路由，尽量减少骨干区的负担；]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[若存在多条优先级相同的路由时，按开销值优选，优选开销值小的路由；]{style="font-family:宋体"}]{#struct_0_x4702_18917_1222127802}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[若存在多条开销值相同路由时，按路由来源区域的区域]{style="font-family:宋体"}]{#struct_0_x4702_18917_x661799130}[ID]{lang="EN-US"}[选择，优选区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[大的路由。]{style="font-family:宋体"}

[[为了避免路由环路，同一路由域内的路由器建议统一配置相同规则。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1019875034}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_830517269}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333555341}[禁止兼容]{style="font-family:宋体"}[RFC 1583]{lang="EN-US"}[的路由选择规则。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1992137585}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] undo rfc1583 compatible]{lang="EN-US"}
:::

::: {#-704878201 .myid}
[]{#_Toc138212589}[]{#_Toc93984815}[]{#_Toc61236366}[]{#_Toc61093166}[]{#_Toc58812089}[]{#_Toc56887218}[]{#_Toc404788068}[]{#struct_0_x4702_18917_x414331615}[]{#_Toc293665257}[]{#_Toc251058600}

**OSPF \-- OSPF配置命令 \-- router id**

------------------------------------------------------------------------

[**[router id]{lang="EN-US"}**]{#struct_0_x4702_18917_x1344512606}[命令用来配置]{style="font-family:宋体"}[全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo router id]{lang="EN-US"}**]{#struct_0_x4702_18917_x777709299}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1688987957}

[**[router id ]{lang="EN-US"}***[router-id]{lang="EN-US"}*]{#struct_0_x4702_18917_2127942686}

[**[undo router id]{lang="EN-US"}**]{#struct_0_x4702_18917_x333620877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x358554922}

[[未配置]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1507647492}[全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1686979689}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1265324119}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x380763777}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_123523185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1693098181}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333424269}

[*[router-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x1536225235}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址形式的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x759563285}

[[一些动态路由协议要求使用]{style="font-family:宋体"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_x1787521888}[，如果在启动这些路由协议时没有指定]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[，则缺省使用全局路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[如果配置了全局路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x4702_18917_30031513}[，则使用配置的值作为]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[。如果没有配置全局路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[，则按照下面的规则进行选择：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果存在配置]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_111577223}[地址的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，则选择]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址中最大的作为]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果没有配置]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x4702_18917_1078205329}[地址的]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口，则从其他接口的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址中选择最大的作为]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[（不考虑接口的]{lang="EN-US" style="font-family:宋体"}[up/down]{lang="EN-US"}[状态）。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x4702_18917_x333489805}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[存在主备的情况下]{style="font-family:宋体"}]{#struct_0_x4702_18917_1551438544}[，]{style="font-family:宋体"}[系统将备份命令行配置的]{style="font-family:宋体"}[Router ID]{lang="FR"}[或从接口地址中选择出来的]{style="font-family:宋体"}[Router ID]{lang="FR"}[。主备倒换后，系统将检查从地址中选出的]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[的有效性，如果无效将重新进行选择。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当且仅当被选为]{style="font-family:宋体"}]{#struct_0_x4702_18917_2028194144}[Router ID]{lang="EN-US"}[的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址被删除或被修改时，才触发重新选择过程，其他情况（例如：接口]{style="font-family:宋体"}[down]{lang="EN-US"}[；已经选取了一个非]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址后又配置了一个]{style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址；配置一个更大的接口地址等）不触发重新选择的过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Router ID]{lang="EN-US"}]{#struct_0_x4702_18917_567104654}[改变之后，各协议需要通过手工执行]{lang="EN-US" style="font-family:宋体"}**[reset]{lang="EN-US"}**[命令才会获取新的]{lang="EN-US" style="font-family:宋体"}[Router ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_657907616}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1535847643}[配置]{style="font-family:宋体"}[全局]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_575549430}

[\[Sysname\] router id 1.1.1.1]{lang="EN-US"}
:::

::: {#886285542 .myid}
[]{#_Toc404788069}[]{#struct_0_x4702_18917_900481572}

**OSPF \-- OSPF配置命令 \-- silent-interface (OSPF view)**

------------------------------------------------------------------------

[**[silent-interface]{lang="EN-US"}**]{#struct_0_x4702_18917_x333293197}[命令用来禁止接口收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo silent-interface]{lang="EN-US"}**]{#struct_0_x4702_18917_1543657091}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1310851947}

[**[silent-interface]{lang="EN-US"}**[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}]{#struct_0_x4702_18917_1182148715}

[**[undo silent-interface]{lang="EN-US"}**[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}]{#struct_0_x4702_18917_x636956036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x304743998}

[[允许接口收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_2021096691}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333358733}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x422541555}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x828738087}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1427547739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x1437417823}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1648200118}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x4702_18917_1875388000}[：接口类型和接口号，]{style="font-family:宋体"}[禁止指定]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_x4702_18917_1387630674}[：禁止所有]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[接口收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333162125}

[[如果要使]{style="font-family:宋体"}[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1299958921}[路由信息不被某一网络中的路由器获得，可使用本命令禁止在此接口上收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1390464735}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x709540042}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_993456454}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_2073976880}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] silent-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x4702_18917_x333227661}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1956807706}[禁止接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[收发]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1448610868}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] silent-interface vlan-interface 10]{lang="EN-US"}
:::

::: {#896947900 .myid}
[]{#_Toc138212591}[]{#_Toc93984817}[]{#_Toc61236368}[]{#_Toc61093167}[]{#_Toc58812090}[]{#_Toc56887219}[]{#_Toc45164815}[]{#_Toc30906018}[]{#_Toc14516707}[]{#_Toc13738149}[]{#_Toc12073427}[]{#_Toc10449486}[]{#_Toc404788070}[]{#struct_0_x4702_18917_1007568494}[]{#_Toc319594446}[]{#_Toc256677065}[]{#_Toc256677067}[]{#_Toc256677068}[]{#_Toc256677069}[]{#_Toc256677070}[]{#_Toc256677071}[]{#_Toc256677072}[]{#_Toc256677073}[]{#_Toc256677074}[]{#_Toc256677075}[]{#_Toc256677076}[]{#_Toc256677077}[]{#_Toc256677078}[]{#_Toc256677079}[]{#_Toc256677080}[]{#_Toc256677081}[]{#_Toc256677082}[]{#_Toc256677083}[]{#_Toc256677084}[]{#_Toc256677085}[]{#_Toc256677086}[]{#_Toc256677087}[]{#_Toc256677088}[]{#_Toc256677089}[]{#_Toc256677090}[]{#_Toc256677091}[]{#_Toc256677092}[]{#_Toc256677093}[]{#_Toc256677094}[]{#_Toc256677095}[]{#_Toc256677097}

**OSPF \-- OSPF配置命令 \-- snmp-agent trap enable ospf**

------------------------------------------------------------------------

[**[snmp-agent trap enable ospf]{lang="EN-US"}**]{#struct_0_x4702_18917_620218408}[命令用来]{style="font-family:
宋体"}[开启]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable ospf**]{lang="EN-US"}]{#struct_0_x4702_18917_1884739704}[命令用来关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x454211884}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable ospf** \[ **authentication-failure** \| **bad-packet** \| **config-error** \| **grhelper-status-change** \| **grrestarter-status-change** \| **if-state-change** \| **lsa-maxage** \| **lsa-originate** \| **lsdb-approaching-overflow** \| **lsdb-overflow** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **retransmit** \| **virt-authentication-failure** \| **virt-bad-packet** \| **virt-config-error** \| **virt-retransmit** \| **virtgrhelper-status-change** \| **virtif-state-change** \| **virtneighbor-state-change** \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_x333686412}

[**[undo snmp-agent]{lang="EN-US"}**[ **trap** **enable ospf** \[ **authentication-failure** \| **bad-packet** \| **config-error** \| **grhelper-status-change** \| **grrestarter-status-change** \| **if-state-change** \| **lsa-maxage** \| **lsa-originate** \| **lsdb-approaching-overflow** \| **lsdb-overflow** \| **neighbor-state-change** \| **nssatranslator-status-change** \| **retransmit** \| **virt-authentication-failure** \| **virt-bad-packet** \| **virt-config-error** \| **virt-retransmit** \| **virtgrhelper-status-change** \| **virtif-state-change** \| **virtneighbor-state-change** \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_760150430}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_176479308}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1886146237}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_853012750}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x4702_18917_1959383281}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x827013285}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_475553341}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x333751948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1124700649}

[**[authentication-failure]{lang="EN-US"}**]{#struct_0_x4702_18917_x1273904985}[：接口认证失败。]{style="font-family:宋体"}

[**[bad-packet]{lang="EN-US"}**]{#struct_0_x4702_18917_x559060845}[：接收了错误报文。]{style="font-family:宋体"}

[**[config-error]{lang="EN-US"}**]{#struct_0_x4702_18917_x868814432}[：接口配置错误。]{style="font-family:宋体"}

[**[grhelper-status-change]{lang="EN-US"}**]{#struct_0_x4702_18917_2071852085}[：邻居]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[状态变化]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[grrestarter-status-change]{lang="EN-US"}**]{#struct_0_x4702_18917_1847988412}[：]{style="font-family:
宋体"}[GR Restarter]{lang="EN-US"}[状态变化]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[if-state-change]{lang="EN-US"}**]{#struct_0_x4702_18917_581429128}[：接口状态变化。]{style="font-family:宋体"}

[**[lsa-maxage]{lang="EN-US"}**]{#struct_0_x4702_18917_x333555340}[：]{style="font-family:宋体"}[LSA]{lang="EN-US"}[的]{style="font-family:宋体"}[max age]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsa-originate]{lang="EN-US"}**]{#struct_0_x4702_18917_1992203121}[：本地生成]{style="font-family:宋体"}[LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[lsdb-approaching-overflow]{lang="EN-US"}**]{#struct_0_x4702_18917_x1981744356}[：]{style="font-family:
宋体"}[LSDB]{lang="EN-US"}[接近溢出。]{style="font-family:宋体"}

[**[lsdb-overflow]{lang="EN-US"}**]{#struct_0_x4702_18917_1064868628}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[溢出。]{style="font-family:宋体"}

[**[neighbor-state-change]{lang="EN-US"}**]{#struct_0_x4702_18917_x843207186}[：邻居状态变化。]{style="font-family:宋体"}

[**[nssatranslator-status-change]{lang="EN-US"}**]{#struct_0_x4702_18917_1634060701}[：]{style="font-family:
宋体"}[NSSA]{lang="EN-US"}[转换路由器状态变化]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[retransmit]{lang="EN-US"}**]{#struct_0_x4702_18917_x977529574}[：接口接收和转发报文。]{style="font-family:宋体"}

[**[virt-authentication-failure]{lang="EN-US"}**]{#struct_0_x4702_18917_x104863504}[：虚接口认证失败。]{style="font-family:
宋体"}

[**[virt-bad-packet]{lang="EN-US"}**]{#struct_0_x4702_18917_x333620876}[：虚接口接收错误报文。]{style="font-family:宋体"}

[**[virt-config-error]{lang="EN-US"}**]{#struct_0_x4702_18917_x358620458}[：虚接口配置错误。]{style="font-family:宋体"}

[**[virt-retransmit]{lang="EN-US"}**]{#struct_0_x4702_18917_474280654}[：虚接口接收和转发报文。]{style="font-family:宋体"}

[**[virtgrhelper-status-change]{lang="EN-US"}**]{#struct_0_x4702_18917_897085892}[：虚接口邻居]{style="font-family:
宋体"}[GR Helper]{lang="EN-US"}[状态变化]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[virtif-state-change]{lang="EN-US"}**]{#struct_0_x4702_18917_642624190}[：虚接口状态变化。]{style="font-family:宋体"}

[**[virtneighbor-state-change]{lang="EN-US"}**]{#struct_0_x4702_18917_x1061188940}[：虚接口邻居状态变化。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1270918532}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333424268}[关闭]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1536290771}

[\[Sysname\] undo snmp-agent trap enable ospf]{lang="EN-US"}
:::

::: {#-132773443 .myid}
[]{#_Toc404788071}[]{#struct_0_x4702_18917_602872703}[]{#_Toc319594447}

**OSPF \-- OSPF配置命令 \-- snmp trap rate-limit**

------------------------------------------------------------------------

[**[snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_x4702_18917_2132254906}[命]{style="font-family:宋体"}[令用来配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[在指定时间间隔内允许输出的告警信息条数]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_x4702_18917_x997247508}[命令用]{style="font-family:宋体"}[来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_509254174}

[**[snmp trap rate-limit interval]{lang="EN-US"}***[ trap-interval ]{lang="EN-US"}***[count]{lang="EN-US"}**[ *trap-number*]{lang="EN-US"}]{#struct_0_x4702_18917_x1498819721}

[**[undo snmp trap rate-limit]{lang="EN-US"}**]{#struct_0_x4702_18917_1753046998}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333489804}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1551373008}[在]{style="font-family:宋体"}[10]{lang="EN-US"}[秒内]{style="font-family:宋体"}[允许输出]{style="font-family:宋体"}[7]{lang="EN-US"}[条告警信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_891996002}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1066524713}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1878236852}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_822103261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_597309088}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x262069237}

[*[trap-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x333293196}[：指定时间间隔，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[trap-number]{lang="EN-US"}*]{#struct_0_x4702_18917_1543722627}[：在指定时间间隔内允许输出的告警信息条数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1329243588}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x256885966}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[在]{style="font-family:宋体"}[5]{lang="EN-US"}[秒内允许输出]{style="font-family:
宋体"}[10]{lang="EN-US"}[条告警信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_887335940}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] snmp trap rate-limit interval 5 count 10]{lang="EN-US"}
:::

::: {#-940476118 .myid}
[]{#_Toc404788072}[]{#struct_0_x4702_18917_x864995970}

**OSPF \-- OSPF配置命令 \-- spf-schedule-interval**

------------------------------------------------------------------------

[**[spf-schedule-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_1231055019}[命令用来配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算的时间间隔。]{style="font-family:宋体"}

[**[undo spf-schedule-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_x333358732}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x422476019}

[**[spf-schedule-interval]{lang="EN-US"}**[ *maximum-interval* \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_x4702_18917_x2006443999}

[**[undo spf-schedule-interval]{lang="EN-US"}**]{#struct_0_x4702_18917_456959317}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1828166851}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1424706192}[路由计算的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_598035010}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_330458769}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333162124}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_4180804}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x955565706}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x155997341}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_1696252589}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_1339584432}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x798342645}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1758018729}

[]{#struct_0_x4702_18917_x333227660}[]{#_Hlt21141603}[根据本地维护的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[，运行]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[协议的路由器通过]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节]{style="font-family:宋体"}[SPF]{lang="EN-US"}[的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。]{style="font-family:宋体"}

[[本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_1956742170}[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x4702_18917_x1842791551}[和]{style="font-family:宋体"}*[incremental-interva]{lang="EN-US"}*[l]{lang="EN-US"}[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x795331950}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_1681699139}[设置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[路由计算最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1914091791}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] spf-schedule-interval 10 500 300]{lang="EN-US"}
:::

::: {#-994179705 .myid}
[]{#_Toc404788073}[]{#struct_0_x4702_18917_x1707588947}[]{#_Toc138212592}[]{#_Toc93984818}[]{#_Toc61236369}[]{#_Toc61093168}[]{#_Toc58812091}[]{#_Toc56887220}[]{#_Toc45164816}

**OSPF \-- OSPF配置命令 \-- stub (OSPF area view)**

------------------------------------------------------------------------

[**[stub]{lang="EN-US"}**]{#struct_0_x4702_18917_x333686415}[命令用来配置一个区域为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo stub]{lang="EN-US"}**]{#struct_0_x4702_18917_760347038}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1664092535}

[**[stub]{lang="EN-US"}**[ \[ **default-route-advertise-always** \| **no-summary** \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_x1331348220}

[**[undo stub]{lang="EN-US"}**]{#struct_0_x4702_18917_956142963}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_887832757}

[[没有区域被设置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x154233351}[区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1417833455}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x333751951}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1124241896}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_415019096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_770772907}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x813423858}

[**[default-route-advertise-always]{lang="EN-US"}**]{#struct_0_x4702_18917_1175876815}[：该参数只用于]{style="font-family:
宋体"}[Stub]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，配置后，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域内发布缺省路由的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[时不检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居。如果未指定本参数，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[向]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域内发布缺省路由的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[时需要检查骨干区域是否存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，如果不存在]{style="font-family:宋体"}[FULL]{lang="EN-US"}[状态的邻居，则]{style="font-family:宋体"}[ABR]{lang="EN-US"}[不会向]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域内发布缺省路由的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-summary]{lang="EN-US"}**]{#struct_0_x4702_18917_x1325600864}[：]{style="font-family:宋体"}[该参数只用于]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域的]{style="font-family:宋体"}[ABR]{lang="EN-US"}[，配置后，]{style="font-family:宋体"}[ABR]{lang="EN-US"}[只向]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域内发布一条缺省路由的]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[，不生成任何其它]{style="font-family:宋体"}[Type-3 LSA]{lang="EN-US"}[（这种区域又称为]{style="font-family:宋体"}[Totally Stub]{lang="EN-US"}[区域）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333555343}

[[如果需要在]{style="font-family:宋体"}[ABR]{lang="EN-US"}]{#struct_0_x4702_18917_1992006513}[上取消配置]{style="font-family:宋体"}**[default-route-advertise-always]{lang="EN-US"}**[或]{style="font-family:宋体"}**[no-summary]{lang="EN-US"}**[参数，可以通过重新执行]{style="font-family:宋体"}**[stub]{lang="EN-US"}**[命令覆盖之前配置即可。]{style="font-family:宋体"}

[[如果要将一个区域配置成]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x1987034654}[区域，则该区域中的所有路由器都必须配置此属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1802222002}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x949208330}[将]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域]{style="font-family:宋体"}[1]{lang="EN-US"}[设置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x239094399}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 1]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.1\] stub]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1781788870}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-cost]{lang="EN-US"}**]{#struct_0_x4702_18917_x333620879}**[ ]{lang="EN-US"}**[(OSPF area view)]{lang="EN-US"}
:::

::: {#202080031 .myid}
[]{#_Toc404788074}[]{#struct_0_x4702_18917_x357637418}[]{#_Toc138212593}[]{#_Toc93984819}[]{#_Toc61236370}[]{#_Toc61093169}[]{#_Toc58812092}[]{#_Toc56887221}[]{#_Toc283903315}[]{#_Toc290904241}

**OSPF \-- OSPF配置命令 \-- stub-router**

------------------------------------------------------------------------

[**[stub-router]{lang="EN-US"}**]{#struct_0_x4702_18917_x1268465011}[命令用来配置当前路由器为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[**[undo stub-router]{lang="EN-US"}**]{#struct_0_x4702_18917_399738637}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x646956805}

[**[stub-router ]{lang="EN-US"}**[\[ **external-lsa** \[ *max-metric-value* \] \| **include-stub** \| **on-startup** { *seconds* \| **wait-for-bgp** \[ *seconds* \] } \| **summary-lsa** \[ *max-metric-value* \] \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_x1450813936}

[**[undo stub-router]{lang="EN-US"}**]{#struct_0_x4702_18917_915621790}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x330886498}

[[当前路由器没有被配置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x333424271}[路由器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1536749524}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x1971006841}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x283695797}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1701874746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_x812190383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x28388846}

[**[external-lsa ]{lang="EN-US"}***[max-metric-value]{lang="EN-US"}*]{#struct_0_x4702_18917_x989159276}[：路由器发布的外部]{style="font-family:宋体"}[LSA]{lang="EN-US"}[链路度量值。]{style="font-family:宋体"}*[max-metric-value]{lang="EN-US"}*[表示链路度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16711680]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[include-stub]{lang="EN-US"}**]{#struct_0_x4702_18917_x333489807}[：路由器发布的]{style="font-family:宋体"}[Router-LSA]{lang="EN-US"}[中，链路类型为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[Stub]{lang="EN-US"}[链路度量值将设置为最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[on-startup]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_1551569616}[：在路由器重启期间，路由器做为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[表示超时时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[wait-for-bgp]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_2035438761}[：在路由器重启后，等待]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由收敛期间，路由器做为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}*[seconds]{lang="EN-US"}*[表示超时时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[summary-lsa]{lang="EN-US"}***[ max-metric-value]{lang="EN-US"}*]{#struct_0_x4702_18917_954052084}[：路由器发布的]{style="font-family:宋体"}[3]{lang="EN-US"}[类]{style="font-family:宋体"}[LSA]{lang="EN-US"}[链路度量值。]{style="font-family:宋体"}*[max-metric-value]{lang="EN-US"}*[表示链路度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[16711680]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1161453910}

[[通过将当前路由器配置为]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x809520872}[路由器，在该路由器发布的]{style="font-family:宋体"}[Router-LSA]{lang="EN-US"}[中，当链路类型取值为]{style="font-family:宋体"}[3]{lang="EN-US"}[表示连接到]{style="font-family:宋体"}[Stub]{lang="EN-US"}[网络时，链路度量值不变；当链路类型为]{style="font-family:宋体"}[1]{lang="EN-US"}[、]{style="font-family:宋体"}[2]{lang="EN-US"}[、]{style="font-family:
宋体"}[4]{lang="EN-US"}[分别表示通过]{style="font-family:宋体"}[P2P]{lang="EN-US"}[链路与另一路由器相连、连接到传送网络、虚连接时，链路度量值将设置为最大值]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[这样其邻居计算出这条路由的开销就会很大，如果邻居上有到这个目的地址开销更小的路由，则数据不会通过这个]{style="font-family:宋体"}[Stub]{lang="EN-US"}]{#struct_0_x4702_18917_x634392250}[路由器转发。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1346751362}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x333293199}[配置当前路由器为]{style="font-family:宋体"}[Stub]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_1543526019}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] stub-router]{lang="EN-US"}
:::

::: {#2015842796 .myid}
[]{#_Toc138212594}[]{#_Toc93984820}[]{#_Toc61236372}[]{#_Toc61093173}[]{#_Toc58812096}[]{#_Toc56887225}[]{#_Toc45164817}[]{#_Toc404788075}[]{#struct_0_x4702_18917_256870287}

**OSPF \-- OSPF配置命令 \-- transmit-pacing**

------------------------------------------------------------------------

[**[transmit-pacing]{lang="EN-US"}**]{#struct_0_x4702_18917_x2092224408}[命令用来配置接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔和一次发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数。]{style="font-family:宋体"}

[**[undo transmit-pacing]{lang="EN-US"}**]{#struct_0_x4702_18917_x30788913}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1415383898}

[**[transmit-pacing interval]{lang="EN-US"}***[ interval ]{lang="EN-US"}***[count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_x4702_18917_642426736}

[**[undo transmit-pacing]{lang="EN-US"}**]{#struct_0_x4702_18917_x333358735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x422148339}

[[接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}]{#struct_0_x4702_18917_x2055166548}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1567325746}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_1273207545}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:
黑体"}]{#struct_0_x4702_18917_6323284}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_543445200}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1896738257}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x333162127}

[**[interval]{lang="EN-US"}***[ interval]{lang="EN-US"}*]{#struct_0_x4702_18917_4115268}[：接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔，]{style="font-family:宋体"}*[interval]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。当路由器上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能的接口数比较多时，建议增大该值，以控制路由器每秒钟发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的总数。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x4702_18917_789092767}[：接口一次发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的最大个数，]{style="font-family:宋体"}*[count]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[200]{lang="EN-US"}[。当路由器上使能]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[功能的接口数比较多时，建议减小该值，以控制路由器每秒钟发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的总数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_1093907626}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1114059745}[配置]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的所有接口发送]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[LSU]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x1264106571}

[\[Sysname\] ospf 1]{lang="EN-US"}

[\[Sysname-ospf-1\] transmit-pacing interval 30 count 10]{lang="EN-US"}
:::

::: {#1860185017 .myid}
[]{#_Toc404788076}[]{#struct_0_x4702_18917_x13920638}

**OSPF \-- OSPF配置命令 \-- vlink-peer (OSPF area view)**

------------------------------------------------------------------------

[**[vlink-peer]{lang="EN-US"}**]{#struct_0_x4702_18917_x333227663}[命令用来创建并配置一条虚连接。]{style="font-family:宋体"}

[**[undo vlink-peer]{lang="EN-US"}**]{#struct_0_x4702_18917_1956676634}[命令用来删除一条已有的虚连接。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1058969302}

[**[vlink-peer]{lang="EN-US"}**[ *router-id* \[ **dead** *seconds* \| **hello** *seconds* \| { { **hmac-md5** \| **md5** } *key-id* { **cipher** *cipher-string* \| **plain** *plain-string* } \| **simple** { **cipher** *cipher-string* \| **plain** *plain-string* } } \| **retransmit** *seconds* \| **trans-delay** *seconds* \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_710806751}

[**[undo]{lang="EN-US"}**[ **vlink-peer** *router-id* \[ **dead** \| **hello** \| { **hmac-md5** \| **md5** } *key-id* \| **retransmit** \| **simple** \| **trans-delay** \] \*]{lang="EN-US"}]{#struct_0_x4702_18917_1809410100}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x196861082}

[[没有虚链接。]{style="font-family:宋体"}]{#struct_0_x4702_18917_1173205526}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1223585000}

[[OSPF]{lang="EN-US"}]{#struct_0_x4702_18917_x333686414}[区域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x4702_18917_760281502}

[[network-admin]{lang="EN-US"}]{#struct_0_x4702_18917_52646512}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x4702_18917_1082701868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x819401806}

[*[router-id]{lang="EN-US"}*]{#struct_0_x4702_18917_x2054988286}[：虚连接邻居的路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[dead]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x4702_18917_x554395802}[：失效时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32768]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[40]{lang="EN-US"}[秒。该值必须和与其建立虚连接路由器的]{style="font-family:宋体"}**[dead]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值相等，并至少为]{style="font-family:宋体"}**[hello ]{lang="EN-US"}***[seconds]{lang="EN-US"}*[值的]{style="font-family:宋体"}[4]{lang="EN-US"}[倍。]{style="font-family:宋体"}

[**[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x4702_18917_x2076136640}[：接口发送]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8192]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。该值必须和与其建立虚连接路由器上的]{style="font-family:宋体"}**[hello]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}[值相等。]{style="font-family:宋体"}

[**[hmac-md5]{lang="EN-US"}**]{#struct_0_x4702_18917_x333751950}[：]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x4702_18917_x1124176360}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x4702_18917_x1377577494}[：简单验证模式。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x4702_18917_120481537}[：]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x4702_18917_x1732744722}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x4702_18917_x2099472919}[：表示设置的密文密码，对于简单验证模式，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[41]{lang="EN-US"}[个字符的字符串，对于]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证模式，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x4702_18917_x981684875}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x4702_18917_x402647143}[：表示设置的明文密码，对于简单验证模式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[个字符的字符串，对于]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证模式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[retransmit ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_x333555342}[：接口重传]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[trans-delay ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x4702_18917_1992072049}[：接口延迟发送]{style="font-family:宋体"}[LSA]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1592365189}

[[根据]{style="font-family:宋体"}[RFC 2328]{lang="EN-US"}]{#struct_0_x4702_18917_1950199176}[的规定，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的所有非骨干区域必须是和骨干区域保持连通的，可以使用]{style="font-family:宋体"}**[vlink-peer]{lang="EN-US"}**[命令建立逻辑上的连通性。]{style="font-family:宋体"}

[[各参数取值规则如下：]{style="font-family:宋体"}]{#struct_0_x4702_18917_465261874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hello]{lang="EN-US"}**]{#struct_0_x4702_18917_x1949977169}[值越小，发现网络变化的速度越快，消耗的网络资源也就越多。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能将]{style="font-family:宋体"}]{#struct_0_x4702_18917_652340740}**[retransmit]{lang="EN-US"}**[值设置的太小，否则将会引起不必要的重传。网络速度相对较慢的时候应把该值设的更大一些。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设置]{lang="EN-US" style="font-family:宋体"}**[trans-delay]{lang="EN-US"}**]{#struct_0_x4702_18917_2056364251}[值时必须考虑接口的发送延迟。]{lang="EN-US" style="font-family:宋体"}

[[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x4702_18917_x333620878}

[[虚连接可指定使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x357702954}[验证或简单验证两种方式，但不能同时指定；使用]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证方式时，可配置多条]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证命令，但]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[是唯一的，同一]{style="font-family:宋体"}*[key-id]{lang="EN-US"}*[只能配置一个验证字。]{style="font-family:宋体"}

[[修改虚连接的]{style="font-family:宋体"}[OSPF MD5/HMAC-MD5]{lang="EN-US"}]{#struct_0_x4702_18917_x543159949}[验证字的步骤如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[首先为该虚连接配置新的]{style="font-family:宋体"}]{#struct_0_x4702_18917_x1334760903}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；此时若邻居设备尚未配置新的]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，便会触发]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。在这个过程中，]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[会发送分别携带各个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字的多份报文，使得无论邻居设备上是否配置了新验证字都能验证通过，保持邻居关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[然后在邻居设备上也都配置相同的新]{style="font-family:宋体"}]{#struct_0_x4702_18917_1160261978}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；当本设备上收到邻居的携带新验证字的报文后，便会退出]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证平滑迁移过程。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[最后在本设备和邻居上都删除旧的]{style="font-family:宋体"}]{#struct_0_x4702_18917_1931135146}[MD5/HMAC-MD5]{lang="EN-US"}[验证字；建议不要为虚连接保留多个]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字，每次]{style="font-family:宋体"}[MD5/HMAC-MD5]{lang="EN-US"}[验证字修改完毕后，应当及时删除旧的验证字，这样可以防止与持有旧验证字的系统继续通信、减少被攻击的可能，还可以减少验证迁移过程对系统、带宽的消耗。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1545810439}

[[\# ]{lang="EN-US"}]{#struct_0_x4702_18917_x1371354671}[配置虚连接，对端路由器]{style="font-family:宋体"}[Router ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x4702_18917_x333424270}

[\[Sysname\] ospf 100]{lang="EN-US"}

[\[Sysname-ospf-100\] area 2]{lang="EN-US"}

[\[Sysname-ospf-100-area-0.0.0.2\] vlink-peer 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x4702_18917_x1536815060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication-mode]{lang="EN-US"}**]{#struct_0_x4702_18917_1167909793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ospf vlink]{lang="EN-US"}**]{#struct_0_x4702_18917_x1127931279}

[ ]{lang="EN-US"}
:::
