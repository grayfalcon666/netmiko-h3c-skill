::: {#-32210999 .myid}
[]{#_Toc357599128}[]{#_Toc352311297}[]{#_Toc185927307}[]{#_Toc123026767}[]{#_Toc29974884}[]{#_Toc25576880}[]{#_Toc15724192}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc404788342}[]{#struct_0_x1984_13510_x613430857}

**IS-IS \-- IS-IS配置命令 \-- address-family ipv4**

------------------------------------------------------------------------

[**[address-family ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_x613234249}[命令用来创建并进入]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[**[undo address-family ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_x967793566}[命令用来删除]{style="font-family:
宋体"}[IS-IS IPv4]{lang="EN-US"}[地址族视图。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1288666934}

[**[address-family]{lang="EN-US"}**[ **ipv4** \[ **unicast** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x296263581}

[**[undo address-family]{lang="EN-US"}**[ **ipv4** \[ **unicast** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1114388566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_549006183}

[[没有创建]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x1229794545}[地址族视图。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_577621989}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x247919910}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1686688985}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_385935607}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x616996729}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x613299785}

[**[unicast]{lang="EN-US"}**]{#struct_0_x1984_13510_1330643503}[：表示单播地址族。缺省为单播地址族。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_140413300}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1265413936}[创建并进入]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[单播地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x193810150}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-100-ipv4\]]{lang="EN-US"}
:::

::: {#-1541660845 .myid}
[]{#_Toc404788343}[]{#struct_0_x1984_13510_1809720996}[]{#_Toc353884860}

**IS-IS \-- IS-IS配置命令 \-- area-authentication send-only**

------------------------------------------------------------------------

[**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_1322197890}[命令用来配置对收到的]{style="font-family:
宋体"}[Level-1]{lang="EN-US"}[报文（包括]{style="font-family:
宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）忽略认证信息检查。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x897335521}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1891009431}

[**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_742342459}

[**[undo area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x613758536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_171079572}

[[如果配置了区域验证方式和验证密码，对收到的报文执行认证信息检查。]{style="font-family:宋体"}]{#struct_0_x1984_13510_920871570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1631549288}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1942469308}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1858976097}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_843396914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_827351052}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x754364851}

[[配置区域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x613824072}[报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中，并对收到的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[报文进行验证密码的检查]{style="font-family:宋体"}[。当需要更改密码时由于密码不匹配可能导致业务发生中断。通过命令配置对]{style="font-family:宋体"}[收到的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[报文]{style="font-family:宋体"}[忽略认证信息检查可保证业务不中断，报文正常接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x583096949}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x162058953}[对收到报文忽略认证信息检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x896304253}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] area-authentication send-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1270679499}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area]{lang="EN-US"}[-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_2140303358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x2092973550}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_1064230045}
:::

::: {#702106844 .myid}
[]{#_Toc163546241}[]{#_Toc50204088}[]{#_Toc33866087}[]{#_Toc404788344}[]{#struct_0_x1984_13510_x603260711}[]{#_Toc297189165}[]{#_Toc290886750}[]{#_Toc252200729}[]{#_Toc163546232}[]{#_Toc50204086}[]{#_Toc33866085}[]{#_Toc132011605}[]{#_Toc131910394}[]{#_Toc132011600}[]{#_Toc132011606}[]{#_Toc131910395}[]{#_Toc132011601}[]{#_Toc132011607}

**IS-IS \-- IS-IS配置命令 \-- area-authentication-mode**

------------------------------------------------------------------------

[**[area-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_x1865289536}[命令用来配置区域验证方式和验证密码。]{style="font-family:
宋体"}

[**[undo area-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_40736322}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1341263331}

[**[area-authentication-mode ]{lang="EN-US"}**[{ **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } \[ **ip** \| **osi** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x613627464}

[**[undo]{lang="EN-US"}**[ **area-authentication-mode**]{lang="EN-US"}]{#struct_0_x1984_13510_x309962379}[]{#_Hlt7610771}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1827796852}

[[系统没有配置区域验证方式和验证密码。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x237185645}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2843899}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1024013807}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2068025777}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1956154969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x238529912}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1060564302}

[**[gca]{lang="EN-US"}**]{#struct_0_x1984_13510_584730491}[：]{style="font-family:宋体"}[GCA]{lang="EN-US"}[验证模式（]{style="font-family:宋体"}[Generic Cryptographic Authentication]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x1984_13510_2135908490}[：唯一标识一个认证项（]{style="font-family:宋体"}[SA]{lang="EN-US"}[），取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。发送方将]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[放入认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中，接收方根据报文中提取的]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[选择]{style="font-family:宋体"}[SA]{lang="EN-US"}[对报文进行认证。]{style="font-family:宋体"}

[**[hmac-sha-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x613693000}[：支持]{style="font-family:宋体"}[HMAC-SHA-1]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-224]{lang="EN-US"}**]{#struct_0_x1984_13510_1768125709}[：支持]{style="font-family:宋体"}[HMAC-SHA-224]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-256]{lang="EN-US"}**]{#struct_0_x1984_13510_1318427315}[：支持]{style="font-family:宋体"}[HMAC-SHA-256]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-384]{lang="EN-US"}**]{#struct_0_x1984_13510_x2101839557}[：支持]{style="font-family:宋体"}[HMAC-SHA-384]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-512]{lang="EN-US"}**]{#struct_0_x1984_13510_x1900467694}[：支持]{style="font-family:宋体"}[HMAC-SHA-512]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_x1984_13510_1711275156}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x1984_13510_x1854774468}[：简单验证模式。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1984_13510_x1625811739}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x1984_13510_x1679439593}[：表示设置的密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x1984_13510_x1400233838}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x1984_13510_938620160}[：表示设置的明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[]{#_Hlt9932887}[**[ip]{lang="EN-US"}**]{#struct_0_x1984_13510_2037385687}[：检查]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[IP]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[**[osi]{lang="EN-US"}**]{#struct_0_x1984_13510_139772152}[：检查]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[]{#struct_0_x1984_13510_x1292115021}[]{#_Hlt7610887}[【使用指导】]{style="font-family:黑体"}

[[配置区域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x309569163}[报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中，并对收到的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[报文进行验证密码的检查。]{style="font-family:宋体"}

[[通过配置区域验证，可防止将从不可信任的路由器学习到的路由信息加入到本地]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1984_13510_2038172344}[中。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_686485867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一区域内的路由器必须配置相同的验证方式和验证密码。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x338652554}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_x30553074}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[参数，将检查]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x779685561}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[认证密码选用]{style="font-family:宋体"}]{#struct_0_x1984_13510_x2030280557}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[不受实际的网络环境影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x686194767}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x412346672}[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下配置区域采用简单明文验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x310027914}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] area-authentication-mode simple plain 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x355383725}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x613496392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_355570777}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_x2098926471}**[isis]{lang="EN-US"}[ authentication-mode]{lang="EN-US"}**
:::

::: {#-275634315 .myid}
[]{#_Toc404788345}[]{#struct_0_x1984_13510_887822978}[]{#_Toc303839426}[]{#_Toc252200730}[]{#_Toc163546233}

**IS-IS \-- IS-IS配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

[**[auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x86231705}[命令用来使能自动计算接口链路开销值功能。]{style="font-family:宋体"}

[**[undo auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_1298420005}[命令用来关闭自动计算接口链路开销值功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_280975401}

[**[auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x310093450}

[**[undo auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_23032803}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1666651082}

[[自动计算接口链路开销值功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1718077484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x826312265}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_2022304307}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x164539312}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1034817303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x203138892}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x310158986}

[[使能自动计算接口链路开销值功能后，将根据带宽参考值自动计算接口的链路度量值。当开销值的类型为]{style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_x1984_13510_1573943018}[或]{style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时，可以根据公式"开销]{style="font-family:宋体"}[=]{lang="EN-US"}[（参考值÷带宽）×]{style="font-family:宋体"}[10]{lang="EN-US"}["]{style="font-family:宋体"}[计算接口的链路度量值。当开销值类型为其他类型时，具体情况如下：接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[10Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[60]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[50]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[40]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[30]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[2500Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[20]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[\>2500Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1089886087}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1318158081}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的自动计算接口链路开销值功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_966738086}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] auto-cost enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1275621880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_x1984_13510_1129431090}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_x420239362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_x310224522}
:::

::: {#1475841160 .myid}
[]{#_Toc404788346}[]{#struct_0_x1984_13510_6136933}[]{#_Toc303839427}[]{#_Toc252200731}[]{#_Toc163546234}

**IS-IS \-- IS-IS配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

[**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_x1984_13510_x1281459941}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[自动计算链路开销值时依据的带宽参考值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bandwidth-reference**]{lang="EN-US"}]{#struct_0_x1984_13510_x1612173271}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_566823401}

[**[bandwidth-reference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1984_13510_1909724534}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_x1984_13510_1151989240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1239526357}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x564460374}[自动计算链路度量值时依据的带宽参考值为]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x309765770}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x669697909}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1460097474}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x539327474}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1809548409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1719846943}

[*[value]{lang="EN-US"}*]{#struct_0_x1984_13510_x1643975338}[：带宽参考值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483648]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1967768980}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_892868403}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的带宽参考值为]{style="font-family:宋体"}[200Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x309831306}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] bandwidth-reference 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2049205889}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x1287595702}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_x401575468}
:::

::: {#188490618 .myid}
[]{#_Toc404788347}[]{#struct_0_x1984_13510_x50317236}[]{#_Toc303839428}[]{#_Toc252200732}[]{#_Toc163546235}

**IS-IS \-- IS-IS配置命令 \-- circuit-cost**

------------------------------------------------------------------------

[**[circuit-cost]{lang="EN-US"}**]{#struct_0_x1984_13510_429918118}[命令用来全局配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的链路开销值。]{style="font-family:宋体"}

[**[undo circuit-cost]{lang="EN-US"}**]{#struct_0_x1984_13510_267439798}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1569418993}

[**[circuit-cost]{lang="EN-US"}**[ *value* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x309896842}

[**[undo circuit-cost]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x337061096}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1013420789}

[[没有全局配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1917959808}[的链路开销值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1783182395}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1444114925}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1585459656}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_2060469933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1776621461}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x309962378}

[*[value]{lang="EN-US"}*]{#struct_0_x1984_13510_x1827862388}[：链路开销值，当指定的路径开销值类型不同时，取值范围也不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定的路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[narrow]{lang="EN-US"}**]{#struct_0_x1984_13510_1607436415}[、]{lang="EN-US" style="font-family:宋体"}**[narrow-compatibl]{lang="EN-US"}**[e]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}**[compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定的路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_x1984_13510_1014434972}[或]{lang="EN-US" style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_127522570}[：配置在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x505375974}[：配置在计算]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1472215072}

[[如果不指定级别，将同时配置计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x511339749}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_247005844}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x309503626}[全局配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下所有接口在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时的链路开销值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1823376218}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] circuit-cost 11 level-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1545789563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_82856413}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_x601105129}
:::

::: {#-1846795298 .myid}
[]{#_Toc404788348}[]{#struct_0_x1984_13510_x1768343577}[]{#_Toc303839429}[]{#_Toc252200733}[]{#_Toc163546236}[]{#_Toc65038638}[]{#_Toc58333218}[]{#_Toc58294863}[]{#_Toc42309485}

**IS-IS \-- IS-IS配置命令 \-- cost-style**

------------------------------------------------------------------------

[**[cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_760047997}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[开销值的类型，即]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接收和发送的报文中到达目的地路径开销值的类型。]{style="font-family:宋体"}

[**[undo cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_x1362222355}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x309569162}

[**[cost-style]{lang="EN-US"}**[ { **narrow** \| **wide** \| **wide-compatible** \| { **compatible** \| **narrow-compatible** } \[ **relax-spf-limit** \] }]{lang="EN-US"}]{#struct_0_x1984_13510_2038106808}

[**[undo cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_x2051334397}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1576588190}

[[只接收和发送采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**]{#struct_0_x1984_13510_x2116513902}[方式表示路径开销值的报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x416174222}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x308501372}[视图]{style="font-family:宋体"}[]{#_Hlt24184665}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_893806049}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1397436077}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x310027917}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x355449261}

[**[narrow]{lang="EN-US"}**]{#struct_0_x1984_13510_x820698420}[：表示只可以接收和发送采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[方式（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[）表示到达目的地路径开销的报文。]{style="font-family:宋体"}

[**[wide]{lang="EN-US"}**]{#struct_0_x1984_13510_x717117840}[：表示只可以接收和发送采用]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式（取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[）表示到达目的地路径开销的报文。]{style="font-family:宋体"}

[**[compatible]{lang="EN-US"}**]{#struct_0_x1984_13510_1664763568}[：表示可以接收和发送采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[和]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式表示到达目的地路径开销的报文。]{style="font-family:宋体"}

[**[narrow-compatible]{lang="EN-US"}**]{#struct_0_x1984_13510_1427419445}[：表示可以接收采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[和]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式表示到达目的地路径开销的报文，却只能发送采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[方式表示到达目的地路径开销的报文。]{style="font-family:宋体"}

[**[wide-compatible]{lang="EN-US"}**]{#struct_0_x1984_13510_x1502130997}[：表示可以接收采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[和]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式表示到达目的地路径开销的报文，却只能发送采用]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式表示到达目的地路径开销的报文。]{style="font-family:宋体"}

[**[relax-spf-limit]{lang="EN-US"}**]{#struct_0_x1984_13510_x409427327}[：表示允许接收到达目的地路径开销值大于]{style="font-family:宋体"}[1023]{lang="EN-US"}[的报文。如果不指定该参数，则在收到开销值大于]{style="font-family:宋体"}[1023]{lang="EN-US"}[的报文时，将丢弃。只有当指定了]{style="font-family:宋体"}**[compatible]{lang="EN-US"}**[或]{style="font-family:宋体"}**[narrow-compatible]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1009627339}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x310093453}[配置路由器可以接收采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[或]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[方式表示路由开销值的报文，却只能发送采用]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[方式表示路由开销值的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_22836195}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] cost-style narrow-compatible]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x842451175}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[circuit-cost]{lang="EN-US"}**]{#struct_0_x1984_13510_423724526}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_767146329}
:::

::: {#225668895 .myid}
[]{#_Toc404788349}[]{#struct_0_x1984_13510_x906588368}[]{#_Toc290886755}[]{#_Toc252200734}[]{#_Toc163546237}

**IS-IS \-- IS-IS配置命令 \-- default-route-advertise**

------------------------------------------------------------------------

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_x1984_13510_x657418723}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由，即在指定级别的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中宣告目的地为]{style="font-family:宋体"}[0.0.0]{lang="EN-US"}[.0/0]{lang="EN-US"}[的路径信息。]{style="font-family:
宋体"}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_x1984_13510_x1778542750}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x310158989}

[**[default-route-advertise ]{lang="EN-US"}**[\[ **avoid-learning** \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **route-policy** *route-policy-name* \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_1573222122}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_x1984_13510_x703324548}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_616153992}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1980433731}[不发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_763494996}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x974312260}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1515252570}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1151656909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x310224525}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x1984_13510_6071397}

[**[avoid-learning]{lang="EN-US"}**]{#struct_0_x1984_13510_1896974953}[：禁止学习通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发过来的缺省路由和]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位产生的缺省路由，防止出现环路。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x184128663}[：发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1929797751}[：同时发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1573764344}[：发布]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_x1984_13510_864237193}[：指定路由策略名。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_1896974952}[：配置缺省路由]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2015309223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定级别，则默认发布]{style="font-family:宋体"}]{#struct_0_x1984_13510_x570158323}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1018715429}[缺省路由只发布给本区域的其他路由器，]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[缺省路由发布给所有]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[路由器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x309765773}[，则可以在]{lang="EN-US" style="font-family:
宋体"}[L1 LSP]{lang="EN-US"}[中生成缺省路由；如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-2]{lang="EN-US"}**[，则可以在]{lang="EN-US" style="font-family:宋体"}[L2 LSP]{lang="EN-US"}[中生成缺省路由；如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-1-2]{lang="EN-US"}**[，可以在]{lang="EN-US" style="font-family:
宋体"}[L1 LSP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:
宋体"}[L2 LSP]{lang="EN-US"}[中各自生成缺省路由。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在路由策略中指定了]{lang="EN-US" style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_x1984_13510_x848156169}[值，则本命令中的]{lang="EN-US" style="font-family:宋体"}[Tag]{lang="EN-US"}[值不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x669763445}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x790003909}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发布]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x407058577}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] default-route-advertise]{lang="EN-US"}
:::

::::: {#-499535309 .myid}
[]{#_Toc303839431}[]{#_Toc81626540}[]{#_Toc404788350}[]{#struct_0_x1984_13510_x1984129709}[]{#_Toc318209355}

**IS-IS \-- IS-IS配置命令 \-- display isis**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x1484266072}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1954456295}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display isis]{lang="EN-US"}**]{#struct_0_x1984_13510_x309831309}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的进程信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2049795713}

[**[display isis ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_135965507}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1455401650}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x309896845}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x337257704}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1368816608}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x38230802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1564647347}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1759607870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_171329624}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_1964764832}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的进程信息。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[进程]{style="font-family:宋体"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_297529287}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1168511349}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的进程信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis]{lang="EN-US"}]{#struct_0_x1984_13510_x613693003}

[ ]{lang="EN-US"}

[          IS-IS(1) Protocol Information]{lang="EN-US"}

[ ]{lang="EN-US"}

[Network-entity                 : 10.0000.0000.0001.00]{lang="EN-US"}

[IS-level                       : level-1-2]{lang="EN-US"}

[Cost-style                     : Wide]{lang="EN-US"}

[Fast reroute                   : Disabled]{lang="EN-US"}

[Preference                     : 15]{lang="EN-US"}

[LSP-length receive             : 1497]{lang="EN-US"}

[LSP-length originate]{lang="EN-US"}

[    level-1                    : 1497]{lang="EN-US"}

[    level-2                    : 1497]{lang="EN-US"}

[Maximum imported routes        : 1000]{lang="EN-US"}

[Timers]{lang="EN-US"}

[    LSP-max-age                : 1200]{lang="EN-US"}

[    LSP-refresh                : 900]{lang="EN-US"}

[    SPF intervals              : 5 50 200]{lang="EN-US"}

[IPv6 enabled]{lang="EN-US"}

[    Multi-topology             : Standard]{lang="EN-US"}

[    Preference                 : 15]{lang="EN-US"}

[    Maximum imported routes    : 1000]{lang="EN-US"}

[    SPF intervals              : 5 50 200]{lang="EN-US"}

[IPv4-Unicast                   :]{lang="EN-US"}

[  Topology red]{lang="EN-US"}

[    Topology ID                : 6]{lang="EN-US"}

[    Preference                 : 15]{lang="EN-US"}

[    Maximum imported routes    : 1000000]{lang="EN-US"}

[    SPF intervals              : 5 50 200]{lang="EN-US"}

[[    Overload status            : Overloaded manually]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1768060173}

[[表1-1 ]{lang="EN-US"}[display isis]{lang="EN-US"}]{#struct_0_x1984_13510_x1824228186}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1781451229}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x613496395}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x613561931}

[[Network-entity]{lang="EN-US"}]{#struct_0_x1984_13510_x906928669}

[[网络实体名称]{style="font-family:宋体"}]{#struct_0_x1984_13510_2051708569}

[[IS-level]{lang="EN-US"}]{#struct_0_x1984_13510_x613365323}

[[路由器类型]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1729417174}

[[Cost-style]{lang="EN-US"}]{#struct_0_x1984_13510_x1086929689}

[[开销类型]{style="font-family:宋体"}]{#struct_0_x1984_13510_x402211042}

[[Fast reroute]{lang="EN-US"}]{#struct_0_x1984_13510_x613430859}

[[是否使能快速重路由功能：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x145435999}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isable]{lang="EN-US"}]{#struct_0_x1984_13510_827306884}[d]{lang="EN-US"}[：表示未使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Auto]{lang="EN-US"}]{#struct_0_x1984_13510_x613234251}[：表示自动选取备份下一跳]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Route-policy]{lang="EN-US"}]{#struct_0_x1984_13510_x613299787}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[通过路由]{style="font-family:宋体"}[策略]{lang="EN-US" style="font-family:宋体"}[来指定备份下一跳]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_x1984_13510_1330512431}

[[路由优先级]{style="font-family:宋体"}]{#struct_0_x1984_13510_515374509}

[[LSP-length receive]{lang="EN-US"}]{#struct_0_x1984_13510_x613758538}

[[可以接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_170424212}[的最大长度]{style="font-family:宋体"}

[[LSP-length originate]{lang="EN-US"}]{#struct_0_x1984_13510_516176627}

[[生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1249902832}[的最大长度]{style="font-family:宋体"}

[[Maximum imported routes]{lang="EN-US"}]{#struct_0_x1984_13510_x613824074}

[[引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}]{#struct_0_x1984_13510_x583228021}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由]{style="font-family:宋体"}[/IPv6]{lang="EN-US"}[路由最大]{style="font-family:宋体"}[条数]{style="font-family:宋体"}

[[Timers]{lang="EN-US"}]{#struct_0_x1984_13510_x2081513619}

[[LSP-max-age]{lang="EN-US"}]{#struct_0_x1984_13510_x613627466}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_584599419}[的最大生存时间]{style="font-family:宋体"}

[[LSP-refresh]{lang="EN-US"}]{#struct_0_x1984_13510_358244184}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x613693002}[的刷新周期]{style="font-family:宋体"}

[[SPF intervals]{lang="EN-US"}]{#struct_0_x1984_13510_1767994637}

[[SPF]{lang="EN-US"}]{#struct_0_x1984_13510_746530065}[的计算时间间隔]{style="font-family:宋体"}

[[IPv6 enabled]{lang="EN-US"}]{#struct_0_x1984_13510_x613496394}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x193610789}[进程支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[功能]{style="font-family:宋体"}

[[Multi-topology]{lang="EN-US"}]{#struct_0_x1984_13510_x2103499153}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x613561930}[进程支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播拓扑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Standard]{lang="EN-US"}]{#struct_0_x1984_13510_x906863133}[：]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播拓扑标准模式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Compatible]{lang="EN-US"}]{#struct_0_x1984_13510_149192012}[：]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播拓扑兼容模式]{lang="EN-US" style="font-family:宋体"}

[[IPv4-Unicast]{lang="EN-US"}]{#struct_0_x1984_13510_x613365322}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1729351638}[进程支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑]{style="font-family:宋体"}

[[Topology ID]{lang="EN-US"}]{#struct_0_x1984_13510_x299471480}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x613430858}[单播拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[Topology]{lang="EN-US"}]{#struct_0_x1984_13510_x145501535}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_1154909641}[单播拓扑名称]{style="font-family:宋体"}

[[Overload status]{lang="EN-US"}]{#struct_0_x1984_13510_x613234250}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded manually]{lang="EN-US"}]{#struct_0_x1984_13510_x967334813}[：]{lang="EN-US" style="font-family:宋体"}[手动设置过载标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded on startup]{lang="EN-US"}]{#struct_0_x1984_13510_x613299786}[：]{lang="EN-US" style="font-family:宋体"}[系统启动时设置过载标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded on startup waiting for nbr]{lang="EN-US"}]{#struct_0_x1984_13510_1330446895}[ ]{lang="EN-US"}*[system]{lang="EN-US"}[-id]{lang="EN-US"}[ ]{lang="EN-US"}*[up]{lang="EN-US"}[　]{style="font-family:
  宋体"}*[ timeout1]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[系统启动后在]{style="font-family:宋体"}*[timeout1]{lang="EN-US"}*[时长内等待邻居]{style="font-family:宋体"}[up]{lang="EN-US"}[时设置过载标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded on startup after nbr]{lang="EN-US"}]{#struct_0_x1984_13510_1734945640}[ ]{lang="EN-US"}*[system]{lang="EN-US"}[-id]{lang="EN-US"}[ ]{lang="EN-US"}*[up]{lang="EN-US"}[　]{style="font-family:
  宋体"}*[ timeout1]{lang="EN-US"}*[：]{lang="EN-US" style="font-family:宋体"}[系统启动邻居]{style="font-family:宋体"}[up]{lang="EN-US"}[后在]{style="font-family:宋体"}*[timeout1]{lang="EN-US"}*[时长内设置过载标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded for memory shortage]{lang="EN-US"}]{#struct_0_x1984_13510_1752537468}[：]{lang="EN-US" style="font-family:宋体"}[在内存不足时设置过载标志位]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Overloaded for graceful starting]{lang="EN-US"}]{#struct_0_x1984_13510_1421472814}[：]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[GR starting]{lang="EN-US"}[阶段设置过载标志位]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-374837253 .myid}
[]{#_Toc404788351}[]{#struct_0_x1984_13510_176205293}[]{#_Toc332962773}

**IS-IS \-- IS-IS配置命令 \-- display isis graceful-restart event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_195509508}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x309765772}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display isis graceful-restart event-log]{lang="EN-US"}**]{#struct_0_x1984_13510_x669828981}[命令用来显示]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x796492553}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1984_13510_66153271}

[**[display isis ]{lang="EN-US"}**]{#struct_0_x1984_13510_2053007643}**[graceful-restart]{lang="EN-US"}[ event-log]{lang="EN-US"}**

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x1984_13510_1134378227}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display isis ]{lang="EN-US"}**]{#struct_0_x1984_13510_764721688}**[graceful-restart]{lang="EN-US"}[ event-log slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_x1911001485}[模式：]{style="font-family:宋体"}

[**[display isis ]{lang="EN-US"}**]{#struct_0_x1984_13510_x1291073666}**[graceful-restart]{lang="EN-US"}[ event-log chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1660751843}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x309831308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2049861249}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x120935700}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_555328492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1168686624}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1093039689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x432875920}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_510565394}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_x309896844}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x1984_13510_x337192168}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_x59340187}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_513067840}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x151672395}[显示]{style="font-family:宋体"}[0]{lang="EN-US"}[号板上]{style="font-family:宋体"}[GR]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis graceful-restart event-log slot 0]{lang="EN-US"}]{#struct_0_x1984_13510_x59340188}

[IS-IS loginfo :]{lang="EN-US"}

[Jul 18 20:44:33 2012 -Slot=0 Enter HA Block status]{lang="EN-US"}

[Jul 18 10:44:33 2012 -Slot=0 Exit HA Block status]{lang="EN-US"}

[Jul 18 20:46:13 2012 -Slot=0 Process 1 enter GR restarting phase(Initialization).]{lang="EN-US"}

[Jul 18 20:46:13 2012 -Slot=0 Prcoess 1 enter GR phase (LSDB synchronization).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (First SPF computation).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Redistribution).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Second SPF computation).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (LSP stability).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (LSP generation).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 enter GR phase (Finish).]{lang="EN-US"}

[Jul 18 20:46:40 2012 -Slot=0 Process 1 GR complete.]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display isis graceful-restart event-log]{lang="EN-US"}]{#struct_0_x1984_13510_1739707739}[显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1364728755}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x309503628}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1824293722}

[[GR phase]{lang="EN-US"}]{#struct_0_x1984_13510_x891169427}

[[GR]{lang="EN-US"}]{#struct_0_x1984_13510_731319341}[阶段：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initializa]{lang="EN-US"}]{#struct_0_x1984_13510_x1691841104}[tion]{lang="EN-US"}[：初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_x1984_13510_x1935337549}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[First SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_x309569164}[：第一次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_x1984_13510_2038500024}[：引入路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Second SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_1877870779}[：第二次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_x1984_13510_x1496304636}[：准备生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1984_13510_1291876325}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成和泛洪]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1984_13510_x1140506403}[：完成]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-901490768 .myid}
[]{#_Toc404788352}[]{#struct_0_x1984_13510_1476997547}

**IS-IS \-- IS-IS配置命令 \-- display isis graceful-restart status**

------------------------------------------------------------------------

[**[display isis graceful-restart]{lang="EN-US"}**[ **status**]{lang="EN-US"}]{#struct_0_x1984_13510_x310027919}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x354531757}

[**[display isis graceful-restart]{lang="EN-US"}**[ **status** \[ **level-1** \| **level-2** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_358120916}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1966588306}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_236166966}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1030559570}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x333167440}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1947237317}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1531290650}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x310093455}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_22705123}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1671033310}[：表示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[级别的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x456491651}[：表示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x889422351}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1566137271}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1218216942}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display isis graceful-restart status]{lang="EN-US"}]{#struct_0_x1984_13510_x310158991}

[ ]{lang="EN-US"}

[                        Restart information for IS-IS(1)]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Restart status: COMPLETE]{lang="EN-US"}

[Restart phase: Finish]{lang="EN-US"}

[Restart t1: 3, count 10; Restart t2: 60; Restart t3: 300]{lang="EN-US"}

[SA Bit: supported]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Level-1 restart information]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Total number of interfaces: 1]{lang="EN-US"}

[Number of waiting LSPs: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Level-2 restart information]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Total number of interfaces: 1]{lang="EN-US"}

[Number of waiting LSPs: 0]{lang="EN-US"}

[]{#struct_0_x1984_13510_1573746411}[]{#_Toc86639912}[]{#_Toc138043182}[]{#_Toc94590060}[表1-3 ]{lang="EN-US"}[display isis graceful-restart status]{lang="EN-US"}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1363733296}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_434892870}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1479201378}

[[Restart status]{lang="EN-US"}]{#struct_0_x1984_13510_x310224527}

[[当前设备的]{style="font-family:宋体"}]{#struct_0_x1984_13510_5940325}[Restarter]{lang="EN-US"}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RESTARTING]{lang="EN-US"}]{#struct_0_x1984_13510_x1686448697}[：保证能进行转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STARTING]{lang="EN-US"}]{#struct_0_x1984_13510_1464711848}[：不能保证转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[COMPLETE]{lang="EN-US"}]{#struct_0_x1984_13510_54642698}[：完成]{style="font-family:宋体"}[GR]{lang="EN-US"}

[[Restart phase]{lang="EN-US"}]{#struct_0_x1984_13510_x424537264}

[[当前设备的]{style="font-family:宋体"}]{#struct_0_x1984_13510_599428256}[Restart]{lang="EN-US"}[阶段：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initializa]{lang="EN-US"}]{#struct_0_x1984_13510_x309765775}[tion]{lang="EN-US"}[：初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSDB synchronization]{lang="EN-US"}]{#struct_0_x1984_13510_x669370229}[：]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[First SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_757604608}[：第一次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_x1984_13510_x581445846}[：引入路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Second SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_1536461812}[：第二次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_x1984_13510_x309831311}[：准备生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1984_13510_2049271424}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成和泛洪]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1984_13510_x1270699092}[：完成]{style="font-family:宋体"}

[[Restart t1]{lang="EN-US"}]{#struct_0_x1984_13510_x1455757975}

[[T1]{lang="EN-US"}]{#struct_0_x1984_13510_x971376564}[定时器的超时值]{style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[count]{lang="EN-US"}]{#struct_0_x1984_13510_x309896847}

[[T1]{lang="EN-US"}]{#struct_0_x1984_13510_x337388776}[定时器的超时次数]{style="font-family:宋体"}

[[Restart t2]{lang="EN-US"}]{#struct_0_x1984_13510_x1435334895}

[[T2]{lang="EN-US"}]{#struct_0_x1984_13510_1727013300}[定时器的超时值]{style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[Restart t3]{lang="EN-US"}]{#struct_0_x1984_13510_1285919152}

[[T3]{lang="EN-US"}]{#struct_0_x1984_13510_x309962383}[定时器的超时值]{style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[SA Bit]{lang="EN-US"}]{#struct_0_x1984_13510_x1827403623}

[[路由器是否支持]{style="font-family:宋体"}]{#struct_0_x1984_13510_554013175}[SA]{lang="EN-US"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[supported]{lang="EN-US"}]{#struct_0_x1984_13510_x1980782776}[：支持]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not supported]{lang="EN-US"}]{#struct_0_x1984_13510_x309503631}[：不支持]{style="font-family:宋体"}

[[Total number of interfaces]{lang="EN-US"}]{#struct_0_x1984_13510_x1823703897}

[[当前]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1773027567}[Level]{lang="EN-US"}[使能的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口数]{style="font-family:宋体"}

[[Number of waiting LSPs]{lang="EN-US"}]{#struct_0_x1984_13510_x175823032}

[[GR Restarter]{lang="EN-US"}]{#struct_0_x1984_13510_x540313697}[从]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步时，当前]{style="font-family:宋体"}[Level]{lang="EN-US"}[未完成同步的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1625073209 .myid}
[]{#_Toc404788353}[]{#struct_0_x1984_13510_x309569167}

**IS-IS \-- IS-IS配置命令 \-- display isis interface**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_2038434488}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1219545430}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display isis interface]{lang="EN-US"}**]{#struct_0_x1984_13510_213814718}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_103000688}

[**[display]{lang="EN-US"}**[ **isis** **interface** \[ \[ *interface-type interface-number* \] \[ **verbose** \] \| **statistics** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x750781972}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x534775938}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_572365739}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1582846209}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1684585853}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1322761680}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1438361618}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x310093454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_22770659}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1984_13510_x120618310}[：显示指定接口的信息。如果未指定本参数，将显示所有接口的信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1984_13510_1268622961}[：显示接口的详细信息。如果未指定该参数，将显示接口的概要信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_606354618}[：显示接口的统计信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_797307164}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示与指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程相关联接口的信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的接口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1573811947}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1840398489}[显示使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis interface]{lang="EN-US"}]{#struct_0_x1984_13510_x59340184}

[ ]{lang="EN-US"}

[                       Interface information for IS-IS(1)]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface:  GigabitEthernet1/0/2]{lang="EN-US"}

[  Index     IPv4.State      IPv6.State     CircuitID   MTU   Type   DIS]{lang="EN-US"}

[  00001     Up              Down           1           1497  L1/L2  No/No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1998996125}[显示使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能接口的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis interface verbose]{lang="EN-US"}]{#struct_0_x1984_13510_x392121971}

[ ]{lang="EN-US"}

[                       Interface information for IS-IS(1)]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Interface:  GigabitEthernet1/0/2]{lang="EN-US"}

[  Index     IPv4.State      IPv6.State     CircuitID   MTU   Type   DIS]{lang="EN-US"}

[  00001     Up              Down           1           1497  L1/L2  No/No]{lang="EN-US"}

[  SNPA address                 : 000c-29e8-1bd5]{lang="EN-US"}

[  IP address                   : 192.168.220.10]{lang="EN-US"}

[  Secondary IP address(es)     :]{lang="EN-US"}

[  IPv6 link-local address      :]{lang="EN-US"}

[  Extended circuit ID          : 1]{lang="EN-US"}

[  CSNP timer value             : L1        10   L2        10]{lang="EN-US"}

[  Hello timer value            :           10]{lang="EN-US"}

[  Hello multiplier value       :            3]{lang="EN-US"}

[  LSP timer value              : L12       33]{lang="EN-US"}

[  LSP transmit-Throttle count  : L12        5]{lang="EN-US"}

[  Cost                         : L1       100   L2        100]{lang="EN-US"}

[  IPv6 cost                    : L1        10   L2        10]{lang="EN-US"}

[  Priority                     : L1        64   L2        64]{lang="EN-US"}

[  Retransmit timer value       : L12        5]{lang="EN-US"}

[[  LDP state                    : L1      ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1304146178}[Init]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}[   L2      No-LDP]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[  LDP sync state               : L1      Init   L2    Achieved]{lang="EN-US"}]{#struct_0_x1984_13510_1752865149}

[  ]{lang="EN-US"}[MPLS TE status               : L1  Disabled   L2    Disabled]{lang="EN-US"}

[  IPv4 BFD                     : Disabled]{lang="EN-US"}

[  IPv6 BFD                     : Disabled]{lang="EN-US"}

[  FRR LFA backup               : Enabled]{lang="EN-US"}

[  IPv4 prefix-suppression      : Disabled]{lang="EN-US"}

[  IPv6 prefix-suppression      : Disabled]{lang="EN-US"}

[  IPv4 tag                     : 1]{lang="EN-US"}

[  IPv6 tag                     : 4294967295]{lang="EN-US"}

[  IPv4-Unicast                 :]{lang="EN-US"}

[    Topology ipv4_unicast_multopo]{lang="EN-US"}

[      Topology ID              : 6]{lang="EN-US"}

[      Cost                     : L1       444  L2       444]{lang="EN-US"}

[      FRR LFA backup           : Disabled]{lang="EN-US"}

[      Prefix-suppression       : Enabled]{lang="EN-US"}

[      Tag                      : 44444444]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display isis interface]{lang="EN-US"}]{#struct_0_x1984_13510_5874789}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1360714151}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x309765774}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x669435765}

[[Interface]{lang="EN-US"}]{#struct_0_x1984_13510_x1594070960}

[[接口类型和接口编号]{style="font-family:宋体"}]{#struct_0_x1984_13510_1189327748}

[[Index]{lang="EN-US"}]{#struct_0_x1984_13510_1753061757}

[[接口索引]{style="font-family:宋体"}]{#struct_0_x1984_13510_197832826}

[[IPv4.State]{lang="EN-US"}]{#struct_0_x1984_13510_1066236686}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x254865496}[状态：]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[IPv6.State]{lang="EN-US"}]{#struct_0_x1984_13510_587115533}

[[IPv6]{lang="EN-US"}]{#struct_0_x1984_13510_x1171947084}[状态：]{style="font-family:宋体"}[Up]{lang="EN-US"}[和]{style="font-family:宋体"}[Down]{lang="EN-US"}

[[CircuitID]{lang="EN-US"}]{#struct_0_x1984_13510_1753127293}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_1752537466}

[[MTU]{lang="EN-US"}]{#struct_0_x1984_13510_x309896846}

[[接口]{style="font-family:宋体"}]{#struct_0_x1984_13510_x337323240}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_x241740079}

[[接口的链路邻接关系类型]{style="font-family:宋体"}]{#struct_0_x1984_13510_x477032080}

[[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_x1925125431}

[[是否被选举为]{style="font-family:宋体"}]{#struct_0_x1984_13510_1723239008}[DIS]{lang="EN-US"}[，"]{style="font-family:宋体"}[\--]{lang="EN-US"}["表示不进行]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举（]{style="font-family:宋体"}[P2P]{lang="EN-US"}[网络）]{style="font-family:宋体"}

[[SNPA address]{lang="EN-US"}]{#struct_0_x1984_13510_x309962382}

[[子网连接点地址]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1827469159}

[[IP address]{lang="EN-US"}]{#struct_0_x1984_13510_x309503630}

[[主]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1823769433}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Secondary IP address(es)]{lang="EN-US"}]{#struct_0_x1984_13510_x309569166}

[[从]{style="font-family:宋体"}]{#struct_0_x1984_13510_2038368952}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPv6 link-local address]{lang="EN-US"}]{#struct_0_x1984_13510_1612286386}

[[IPv6]{lang="EN-US"}]{#struct_0_x1984_13510_163180180}[链路本地地址]{style="font-family:宋体"}

[[Extended circuit ID]{lang="EN-US"}]{#struct_0_x1984_13510_1752603002}

[[扩展链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_227067645}[，点对点链路存在该项]{style="font-family:宋体"}

[[CSNP timer value]{lang="EN-US"}]{#struct_0_x1984_13510_1612220850}

[[CSNP]{lang="EN-US"}]{#struct_0_x1984_13510_x926939797}[报文发送时间间隔]{style="font-family:宋体"}

[[Hello timer value]{lang="EN-US"}]{#struct_0_x1984_13510_1612155314}

[[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1372298539}[报文发送时间间隔]{style="font-family:宋体"}

[[Hello multiplier value]{lang="EN-US"}]{#struct_0_x1984_13510_1612548530}

[[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1758025382}[报文失效数目]{style="font-family:宋体"}

[[LSP timer value]{lang="EN-US"}]{#struct_0_x1984_13510_1612482994}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_220732275}[的最小时间间隔]{style="font-family:宋体"}

[[LSP transmit-Throttle count]{lang="EN-US"}]{#struct_0_x1984_13510_1612417458}

[[每次发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1612351922}[的数目]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x1984_13510_x1315008342}

[[接口的链路开销值]{style="font-family:宋体"}]{#struct_0_x1984_13510_1309908730}

[[IPv6 cost]{lang="EN-US"}]{#struct_0_x1984_13510_1752668538}

[[接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1984_13510_1752734074}[链路开销值]{style="font-family:宋体"}

[[Priority]{lang="EN-US"}]{#struct_0_x1984_13510_x1077295206}

[[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_1955513924}[优先级]{style="font-family:宋体"}

[[Retransmit timer value]{lang="EN-US"}]{#struct_0_x1984_13510_1752799610}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1374573803}[在点到点链路上的重传时间间隔]{style="font-family:宋体"}

[[MPLS TE status]{lang="EN-US"}]{#struct_0_x1984_13510_1752865146}

[[是否使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1383128325}[的]{style="font-family:宋体"}[MPLS TE]{lang="EN-US"}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_1752930682}[：]{style="font-family:宋体"}[表示使能]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_1752996218}[：]{style="font-family:宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}[MPLS TE]{lang="EN-US"}

[[LDP state]{lang="EN-US"}]{#struct_0_x1984_13510_1022978118}

[[LDP]{lang="EN-US"}]{#struct_0_x1984_13510_1753061754}[状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x1984_13510_197898362}[：表示处于初始化状态，]{style="font-family:宋体"}[LDP]{lang="EN-US"}[还没有上报状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-LDP]{lang="EN-US"}]{#struct_0_x1984_13510_1753127290}[：]{style="font-family:宋体"}[表示未配置]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not ready]{lang="EN-US"}]{#struct_0_x1984_13510_1752537467}[：]{style="font-family:宋体"}[表示未建立]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ready]{lang="EN-US"}]{#struct_0_x1984_13510_1421276206}[：]{style="font-family:宋体"}[表示已建立]{lang="EN-US" style="font-family:宋体"}[LDP]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}

[[LDP sync state]{lang="EN-US"}]{#struct_0_x1984_13510_1752603003}

[[LDP]{lang="EN-US"}]{#struct_0_x1984_13510_1752668539}[同步状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_x1984_13510_1734134181}[：]{style="font-family:宋体"}[表示初始化]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Achieved]{lang="EN-US"}]{#struct_0_x1984_13510_1752734075}[：]{style="font-family:宋体"}[表示已同步]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max cost]{lang="EN-US"}]{#struct_0_x1984_13510_1752799611}[：]{style="font-family:宋体"}[表示保持]{lang="EN-US" style="font-family:宋体"}[最大开销值]{style="font-family:宋体"}

[[IPv4 BFD]{lang="EN-US"}]{#struct_0_x1984_13510_1612810674}

[[是否使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_213451811}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_x803426924}[：表示未使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_1612745138}[：表示使能]{style="font-family:宋体"}

[[IPv6 BFD]{lang="EN-US"}]{#struct_0_x1984_13510_x1753390447}

[[是否使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x2060668448}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_x711623324}[：表示未使能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_1612286387}[：表示使能]{style="font-family:宋体"}

[[FRR LFA backup]{lang="EN-US"}]{#struct_0_x1984_13510_x59340180}

[[是否使能]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x1984_13510_x392121975}[计算功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_1514637925}[：]{style="font-family:宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_39680379}[：]{style="font-family:宋体"}[表示使能]{lang="EN-US" style="font-family:宋体"}

[[IPv4 prefix-suppression]{lang="EN-US"}]{#struct_0_x1984_13510_1110799370}

[[是否使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1514637924}[的前缀抑制功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_39745915}[：]{style="font-family:宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_428388466}[：]{style="font-family:宋体"}[表示使能]{lang="EN-US" style="font-family:宋体"}

[[IPv6 prefix-suppression]{lang="EN-US"}]{#struct_0_x1984_13510_1310339949}

[[是否使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1514637923}[的前缀抑制功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x1984_13510_39811451}[：]{style="font-family:宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x1984_13510_819768955}[：]{style="font-family:宋体"}[表示使能]{lang="EN-US" style="font-family:宋体"}

[[IPv4 tag]{lang="EN-US"}]{#struct_0_x1984_13510_1514637922}

[[接口]{style="font-family:宋体"}[IPv4 tag]{lang="EN-US"}]{#struct_0_x1984_13510_39876987}[值]{style="font-family:宋体"}

[[IPv6 tag]{lang="EN-US"}]{#struct_0_x1984_13510_x638926179}

[[接口]{style="font-family:宋体"}[IPv6 tag]{lang="EN-US"}]{#struct_0_x1984_13510_1514637929}[值]{style="font-family:宋体"}

[[IPv4-Unicast]{lang="EN-US"}]{#struct_0_x1984_13510_1752865147}

[[接口支持的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_1752930683}[单播拓扑]{style="font-family:宋体"}

[[Topology]{lang="EN-US"}]{#struct_0_x1984_13510_x569302031}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_1752996219}[单播拓扑名称]{style="font-family:宋体"}

[[Topology ID]{lang="EN-US"}]{#struct_0_x1984_13510_1753061755}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_197963898}[单播拓扑]{style="font-family:宋体"}[ID]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_163114644}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis interface statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x1089983543}

[ ]{lang="EN-US"}

[                  Interface Statistics information for IS-IS(1)]{lang="EN-US"}

[                  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Type            IPv4 Up/Down           IPv6 Up/Down]{lang="EN-US"}

[  LAN                   1/0                    0/0]{lang="EN-US"}

[  P2P                   0/0                    0/0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display isis interface statistics]{lang="EN-US"}]{#struct_0_x1984_13510_331371368}[显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1393470572}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2056872211}

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1871651452}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_1612220851}

[[接口类型，取值为：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x927005333}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAN]{lang="EN-US"}]{#struct_0_x1984_13510_x1272536412}[：表示接口的网络类型为广播]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_x1984_13510_220821177}[：表示接口的网络类型为点对点]{style="font-family:宋体"}

[[IPv4 Up]{lang="EN-US"}]{#struct_0_x1984_13510_337808317}

[[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1712562457}[功能且状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[的接口数]{style="font-family:宋体"}

[[IPv4 Down]{lang="EN-US"}]{#struct_0_x1984_13510_x1558766778}

[[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1612155315}[功能且状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口数]{style="font-family:宋体"}

[[IPv6 Up]{lang="EN-US"}]{#struct_0_x1984_13510_x1372233003}

[[使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1364139011}[功能且状态为]{style="font-family:宋体"}[up]{lang="EN-US"}[的接口数]{style="font-family:宋体"}

[[IPv6 Down]{lang="EN-US"}]{#struct_0_x1984_13510_221040085}

[[使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x916719323}[功能且状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1482300807 .myid}
[]{#_Toc404788354}[]{#struct_0_x1984_13510_x2097020161}[]{#_Toc163546243}[]{#_Toc50204089}[]{#_Toc33866088}[]{#_Toc209857781}[]{#_Toc209857782}[]{#_Toc209857783}[]{#_Toc209857784}[]{#_Toc209857785}[]{#_Toc209857786}[]{#_Toc209857787}[]{#_Toc209857788}[]{#_Toc209857789}[]{#_Toc209857790}[]{#_Toc209857791}[]{#_Toc209857792}[]{#_Toc209857793}[]{#_Toc209857795}[]{#_Toc209857798}[]{#_Toc209857805}[]{#_Toc209857811}[]{#_Toc209857814}[]{#_Toc209857821}[]{#_Toc209857826}[]{#_Toc209857827}[]{#_Toc209857885}

**IS-IS \-- IS-IS配置命令 \-- display isis lsdb**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1612089779}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_157562216}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display isis lsdb]{lang="EN-US"}**]{#struct_0_x1984_13510_x438821388}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_815754884}

[**[display isis lsdb]{lang="EN-US"}**[ \[ \[ **level-1** \| **level-2** \] \| **local** \| \[ **lsp-id** *lspid* \| **lsp-name** *lspname* \] \| **verbose** \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1534539161}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1233308638}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_666587590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_697400917}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x10551794}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_582700824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1232062384}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1612482995}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_220666739}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1869580939}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[链路状态数据库。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1362586591}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[链路状态数据库。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_x1984_13510_x726987052}[：显示当前路由器产生的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[**[lsp-id]{lang="EN-US"}***[ lspid]{lang="EN-US"}*]{#struct_0_x1984_13510_921079068}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[标识，形式为]{style="font-family:宋体"}[SYSID*.*Pseudonode ID-fragment num]{lang="EN-US"}[，其中，]{style="font-family:宋体"}[SYSID]{lang="EN-US"}[是]{style="font-family:宋体"}[产生该]{style="font-family:宋体"}[LSP]{lang="EN-GB"}[的节点或伪节点的]{style="font-family:宋体"}[SystemID]{lang="EN-US"}[，]{style="font-family:宋体"}[Pseudonode ID]{lang="EN-US"}[是伪节点]{style="font-family:宋体"}[ID]{lang="EN-US"}[，]{style="font-family:宋体"}[fragment num]{lang="EN-US"}[是该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的分片号。]{style="font-family:宋体"}

[**[lsp-name]{lang="EN-US"}***[ lspname]{lang="EN-US"}*]{#struct_0_x1984_13510_x549510444}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[名称，形式为]{style="font-family:宋体"}[Symbolic name.\[Pseudo ID\]-fragment num]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1984_13510_x191229646}[：显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的详细信息。如果未指定该参数，将显示链路状态数据库中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_423693324}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的链路状态数据库信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的链路状态数据库信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1625943473}

[[如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1394052277}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的链路状态数据库信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1953001340}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_376418426}[显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[链路状态数据库的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis lsdb level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1514637926}

[ ]{lang="EN-US"}

[                        Database information for IS-IS(1)]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Level-1 Link State Database]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSPID                 Seq Num      Checksum      Holdtime      Length  ATT/P/OL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0000.0000.0001.00-00\* 0x00000087   0xf846        1152          183     0/0/0]{lang="EN-US"}

[0000.0000.0003.00-00  0x00000005   0x4bee        520           177     0/0/0]{lang="EN-US"}

[0000.0000.0003.00-01  0x00000004   0x7245        520           45      0/0/0]{lang="EN-US"}

[0000.0000.0011.00-00  0x0000000b   0xcdf6        815           183     0/0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[    \*-Self LSP, +-Self LSP(Extended), ATT-Attached, P-Partition, OL-Overload]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1314942806}[显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[链路状态数据库的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis lsdb level-1 verbose]{lang="EN-US"}]{#struct_0_x1984_13510_1514637933}

[ ]{lang="EN-US"}

[                        Database information for IS-IS(1)]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                          Level-1 Link State Database]{lang="EN-US"}

[                          \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[LSPID                 Seq Num      Checksum      Holdtime      Length  ATT/P/OL]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0000.0000.0001.00-00\* 0x00000080   0x73f         1185          183     0/0/0]{lang="EN-US"}

[ Source       0000.0000.0001.00]{lang="EN-US"}

[ NLPID        IPv4]{lang="EN-US"}

[ Area address 10]{lang="EN-US"}

[ IPv4 address 192.168.220.10]{lang="EN-US"}

[ MT ID        0000   (-/-)]{lang="EN-US"}

[ MT ID        0002   (-/-)]{lang="EN-US"}

[ MT ID        0006   (-/-)]{lang="EN-US"}

[ +NBR  ID]{lang="EN-US"}

[     0000.0000.0011.00                Cost: 100]{lang="EN-US"}

[     Admin group: 0x00000000]{lang="EN-US"}

[     Physical bandwidth: 12500000 bytes/sec]{lang="EN-US"}

[     Reservable bandwidth: 0 bytes/sec]{lang="EN-US"}

[     Unreserved bandwidth for each TE class:]{lang="EN-US"}

[       TE class  0: 0 bytes/sec             TE class  1: 0 bytes/sec]{lang="EN-US"}

[       TE class  2: 0 bytes/sec             TE class  3: 0 bytes/sec]{lang="EN-US"}

[       TE class  4: 0 bytes/sec             TE class  5: 0 bytes/sec]{lang="EN-US"}

[       TE class  6: 0 bytes/sec             TE class  7: 0 bytes/sec]{lang="EN-US"}

[       TE class  8: 0 bytes/sec             TE class  9: 0 bytes/sec]{lang="EN-US"}

[       TE class 10: 0 bytes/sec             TE class 11: 0 bytes/sec]{lang="EN-US"}

[       TE class 12: 0 bytes/sec             TE class 13: 0 bytes/sec]{lang="EN-US"}

[       TE class 14: 0 bytes/sec             TE class 15: 0 bytes/sec]{lang="EN-US"}

[     TE cost: 10]{lang="EN-US"}

[     Bandwidth constraint model: Prestandard DS-TE RDM]{lang="EN-US"}

[     Bandwidth constraints:]{lang="EN-US"}

[       BC\[0\]      : 0 bytes/sec             BC\[1\]      : 0 bytes/sec]{lang="EN-US"}

[     Neighbor IP address: 192.168.220.30]{lang="EN-US"}

[     Interface IP address: 192.168.220.10]{lang="EN-US"}

[ IPv6 unicast NBR ID]{lang="EN-US"}

[     6464.6464.6464.01                Cost: 10         MT ID: 2]{lang="EN-US"}

[ MT NBR ID]{lang="EN-US"}

[     6464.6464.6464.01                Cost: 10         MT ID: 6]{lang="EN-US"}

[ +IP-Extended]{lang="EN-US"}

[     192.168.220.0   255.255.255.0    Cost: 100]{lang="EN-US"}

[ IPv4 unicast]{lang="EN-US"}

[     1.1.1.1         255.255.255.255  Cost: 0          MT ID: 6]{lang="EN-US"}

[ IPv4 unicast]{lang="EN-US"}

[     10.10.10.0      255.255.255.0    Cost: 10         MT ID: 6]{lang="EN-US"}

[ IPv6 unicast]{lang="EN-US"}

[     1:1:1::1/128                     Cost: 0          MT ID: 2]{lang="EN-US"}

[ IPv6 unicast]{lang="EN-US"}

[     10:10:10::/64                    Cost: 10         MT ID: 2]{lang="EN-US"}

[ Router ID    1.1.1.1]{lang="EN-US"}

[ ]{lang="EN-US"}

[0000.0000.0003.00-00  0x00000005   0x4bee        887           177     0/0/0]{lang="EN-US"}

[ Source       0000.0000.0003.00]{lang="EN-US"}

[ NLPID        IPv4]{lang="EN-US"}

[ Area address 10]{lang="EN-US"}

[ IPv4 address 10.10.10.10]{lang="EN-US"}

[ IPv4 address 192.168.220.20]{lang="EN-US"}

[ +NBR  ID]{lang="EN-US"}

[     0000.0000.0001.00                Cost: 10]{lang="EN-US"}

[     Admin group: 0x00000000]{lang="EN-US"}

[     Physical bandwidth: 12500000 bytes/sec]{lang="EN-US"}

[     Reservable bandwidth: 0 bytes/sec]{lang="EN-US"}

[     Unreserved bandwidth for each TE class:]{lang="EN-US"}

[       TE class  0: 0 bytes/sec             TE class  1: 0 bytes/sec]{lang="EN-US"}

[       TE class  2: 0 bytes/sec             TE class  3: 0 bytes/sec]{lang="EN-US"}

[       TE class  4: 0 bytes/sec             TE class  5: 0 bytes/sec]{lang="EN-US"}

[       TE class  6: 0 bytes/sec             TE class  7: 0 bytes/sec]{lang="EN-US"}

[       TE class  8: 0 bytes/sec             TE class  9: 0 bytes/sec]{lang="EN-US"}

[       TE class 10: 0 bytes/sec             TE class 11: 0 bytes/sec]{lang="EN-US"}

[       TE class 12: 0 bytes/sec             TE class 13: 0 bytes/sec]{lang="EN-US"}

[       TE class 14: 0 bytes/sec             TE class 15: 0 bytes/sec]{lang="EN-US"}

[     TE cost: 10]{lang="EN-US"}

[     Bandwidth constraint model: Prestandard DS-TE RDM]{lang="EN-US"}

[     Bandwidth constraints:]{lang="EN-US"}

[       BC\[0\]: 0 bytes/sec                   BC\[1\]: 0 bytes/sec]{lang="EN-US"}

[     Interface IP address: 192.168.220.20]{lang="EN-US"}

[     Neighbor IP address: 192.168.220.10]{lang="EN-US"}

[ Router ID    3.3.3.3]{lang="EN-US"}

[                                                                                ]{lang="EN-US"}

[0000.0000.0003.00-01  0x00000004   0x7245        887           45      0/0/0]{lang="EN-US"}

[ Source       0000.0000.0003.00]{lang="EN-US"}

[ +IP-Extended]{lang="EN-US"}

[         10.10.10.0      255.255.255.0    Cost: 10]{lang="EN-US"}

[ +IP-Extended]{lang="EN-US"}

[         192.168.220.0   255.255.255.0    Cost: 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[\*-Self LSP, +-Self LSP(Extended), ATT-Attached, P-Partition, OL-Overload]{lang="EN-US"}

[]{#struct_0_x1984_13510_1612745139}[]{#_Toc94753867}[]{#_Toc94671193}[]{#_Toc73952270}[[表1-6 ]{lang="EN-US"}[display isis lsdb]{lang="EN-US"}]{#_Toc68319403}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1395641190}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1753455983}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1032999093}

[[LSPID]{lang="EN-US"}]{#struct_0_x1984_13510_x1647819718}

[[链路状态报文]{style="font-family:宋体"}]{#struct_0_x1984_13510_1204704442}[ID]{lang="EN-US"}

[[Seq Num]{lang="EN-US"}]{#struct_0_x1984_13510_x1357187591}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1612286384}[序列号]{style="font-family:宋体"}

[[Checksum]{lang="EN-US"}]{#struct_0_x1984_13510_163049108}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1595777027}[校验和]{style="font-family:宋体"}

[[Holdtime]{lang="EN-US"}]{#struct_0_x1984_13510_x1717318428}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1325878620}[生存时间，随着时间推移递减]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x1984_13510_1640486834}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1612220848}[长度]{style="font-family:宋体"}

[[ATT/P/OL]{lang="EN-US"}]{#struct_0_x1984_13510_x926415510}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x525098106}[中]{style="font-family:宋体"}[ATT]{lang="EN-US"}[（]{style="font-family:宋体"}[Attach bit]{lang="EN-US"}[）、]{style="font-family:宋体"}[P]{lang="EN-US"}[（]{style="font-family:宋体"}[Partition bit]{lang="EN-US"}[）、]{style="font-family:宋体"}[OL]{lang="EN-US"}[（]{style="font-family:宋体"}[Overload bit]{lang="EN-US"}[）的置位情况，]{style="font-family:宋体"}[1]{lang="EN-US"}[表示置位，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示没有置位]{style="font-family:宋体"}

[[Source]{lang="EN-US"}]{#struct_0_x1984_13510_x2007587509}

[[LSP]{lang="SV"}]{#struct_0_x1984_13510_425379096}[生成路由器的]{style="font-family:宋体"}[System ID]{lang="SV"}

[[HOST NAME]{lang="EN-US"}]{#struct_0_x1984_13510_x1690352741}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1038530614}[生成路由器的动态主机名]{style="font-family:宋体"}

[[ORG ID]{lang="EN-US"}]{#struct_0_x1984_13510_x883783687}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1845099668}[生成路由器配置的虚拟系统所对应的原始系统]{style="font-family:宋体"}[ID]{lang="EN-US"}

[[NLPID]{lang="EN-US"}]{#struct_0_x1984_13510_1612155312}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1372691755}[生成路由器运行的网络层协议]{style="font-family:宋体"}

[[Area address]{lang="EN-US"}]{#struct_0_x1984_13510_x423740390}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1521156484}[生成路由器的区域地址]{style="font-family:宋体"}

[[IPv4 address]{lang="EN-US"}]{#struct_0_x1984_13510_1831029378}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1612089776}[生成路由器使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_x1984_13510_158020968}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1558952082}[生成路由器使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[功能接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[MT ID        0000     (-/-)]{lang="EN-US"}]{#struct_0_x1984_13510_1752537465}

[[MT ID        0002     (-/-)]{lang="EN-US"}]{#struct_0_x1984_13510_1752603001}

[[MT ID        0006     (-/-)]{lang="EN-US"}]{#struct_0_x1984_13510_1752668537}

[[LSP]{lang="EN-US" style="font-size:
  9.0pt"}]{#struct_0_x1984_13510_1752734073}[生成路由器支持的拓扑信息]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[0000]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1984_13510_1752799609}[表示标准拓扑，]{style="font-size:9.0pt;font-family:宋体"}[0002]{lang="EN-US" style="font-size:9.0pt"}[表示]{style="font-size:9.0pt;font-family:
  宋体"}[IPv6]{lang="EN-US" style="font-size:9.0pt"}[单播拓扑，]{style="font-size:9.0pt;font-family:宋体"}[0006]{lang="EN-US" style="font-size:9.0pt"}[表示]{style="font-size:9.0pt;font-family:
  宋体"}[IPv4]{lang="EN-US" style="font-size:9.0pt"}[单播拓扑]{style="font-size:9.0pt;font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[(-/-)]{lang="EN-US" style="font-size:9.0pt"}]{#struct_0_x1984_13510_1373983980}[，即]{style="font-size:9.0pt;font-family:宋体"}[ATT/OL]{lang="EN-US" style="font-size:9.0pt"}

[[NBR ID]{lang="EN-US"}]{#struct_0_x1984_13510_x621588644}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x521951724}[生成路由器邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}

[[MT NBR ID]{lang="EN-US"}]{#struct_0_x1984_13510_1752865145}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1752930681}[生成路由器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑邻居信息]{style="font-family:宋体"}

[[IPv6 unicast NBR ID]{lang="EN-US"}]{#struct_0_x1984_13510_1752996217}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1753061753}[生成路由器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播邻居信息]{style="font-family:宋体"}

[[Admin group]{lang="EN-US"}]{#struct_0_x1984_13510_198094970}

[[链路管理组属性]{style="font-family:宋体"}]{#struct_0_x1984_13510_1753127289}

[[Interface IP address]{lang="EN-US"}]{#struct_0_x1984_13510_x976345887}

[[与对端相连的本地接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1984_13510_x976280351}[地址]{style="font-family:宋体"}

[[Neighbor IP address]{lang="EN-US"}]{#struct_0_x1984_13510_x976214815}

[[邻居的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1984_13510_x976149279}[地址]{style="font-family:宋体"}

[[Physical bandwidth]{lang="EN-US"}]{#struct_0_x1984_13510_x976083743}

[[物理带宽]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1357613518}

[[Reservable bandwidth]{lang="EN-US"}]{#struct_0_x1984_13510_x976018207}

[[预留带宽]{style="font-family:宋体"}]{#struct_0_x1984_13510_x975952671}

[[Unreserved bandwidth for each TE class]{lang="EN-US"}]{#struct_0_x1984_13510_x975887135}

[[每个]{style="font-family:宋体"}[TE class]{lang="EN-US"}]{#struct_0_x1984_13510_x975821599}[的可预留带宽]{style="font-family:宋体"}

[[TE class]{lang="EN-US"}]{#struct_0_x1984_13510_x975756063}

[[8]{lang="EN-US"}]{#struct_0_x1984_13510_x976345886}[个或]{style="font-family:宋体"}[16]{lang="EN-US"}[个]{style="font-family:宋体"}[TE class]{lang="EN-US"}[各自的可用带宽]{style="font-family:宋体"}

[[TE cost]{lang="EN-US"}]{#struct_0_x1984_13510_x939040777}

[[TE]{lang="EN-US"}]{#struct_0_x1984_13510_x976280350}[开销]{style="font-family:宋体"}

[[Bandwidth constraint model]{lang="EN-US"}]{#struct_0_x1984_13510_x976214814}

[[带宽约束模型，取值包括：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x976149278}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Prestandard DS-TE RDM]{lang="EN-US"}]{#struct_0_x1984_13510_x976083742}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IETF DS-TE RDM]{lang="EN-US"}]{#struct_0_x1984_13510_x976018206}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IETF DS-TE MAM]{lang="EN-US"}]{#struct_0_x1984_13510_x975952670}

[[BC]{lang="EN-US"}]{#struct_0_x1984_13510_x975887134}

[[各个带宽约束值（]{style="font-family:宋体"}[Prestandard]{lang="EN-US"}]{#struct_0_x1984_13510_x975821598}[模式支持]{style="font-family:宋体"}[2]{lang="EN-US"}[个]{style="font-family:宋体"}[BC]{lang="EN-US"}[，]{style="font-family:宋体"}[IETF]{lang="EN-US"}[模式支持至多]{style="font-family:宋体"}[8]{lang="EN-US"}[个]{style="font-family:宋体"}[BC]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Router ID]{lang="EN-US"}]{#struct_0_x1984_13510_1513721455}

[[路由器]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_x975756062}

[[IP-Internal]{lang="EN-US"}]{#struct_0_x1984_13510_1612548528}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1758549669}[生成路由器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[内部可达地址和掩码信息]{style="font-family:宋体"}

[[IP-External]{lang="EN-US"}]{#struct_0_x1984_13510_x922987850}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x220295905}[生成路由器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[外部可达地址和掩码信息]{style="font-family:宋体"}

[[IP-Extended]{lang="EN-US"}]{#struct_0_x1984_13510_1612482992}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_221125491}[生成路由器的扩展]{style="font-family:宋体"}[IP]{lang="EN-US"}[可达地址和掩码信息]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x1984_13510_x152253745}

[[开销值]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1698851822}

[[Auth]{lang="EN-US"}]{#struct_0_x1984_13510_1612417456}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1735100104}[生成路由器的认证信息]{style="font-family:宋体"}

[[IPV6]{lang="EN-US"}]{#struct_0_x1984_13510_x168034106}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_166589132}[生成路由器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[内部可达]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀信息]{style="font-family:宋体"}

[[IPV6-Ext]{lang="EN-US"}]{#struct_0_x1984_13510_1612351920}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1314877270}[生成路由器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[外部可达]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址和前缀信息]{style="font-family:宋体"}

[[IPv4 unicast]{lang="EN-US"}]{#struct_0_x1984_13510_x976149281}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1708726143}[生成路由器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播可达信息]{style="font-family:宋体"}

[[IPv6 unicast]{lang="EN-US"}]{#struct_0_x1984_13510_x976083745}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x976018209}[生成路由器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播内部可达信息]{style="font-family:宋体"}

[[IPv6 unicast-ext]{lang="EN-US"}]{#struct_0_x1984_13510_x975952673}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x975887137}[生成路由器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[单播外部可达信息]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-297665974 .myid}
[]{#_Toc163546246}[]{#_Toc50204091}[]{#_Toc33866090}[]{#_Toc404788355}[]{#struct_0_x1984_13510_x1561344843}[]{#_Toc310604324}[]{#_Toc290886761}[]{#_Toc252200740}[]{#_Toc163546244}[]{#_Toc50204090}[]{#_Toc33866089}

**IS-IS \-- IS-IS配置命令 \-- display isis mesh-group**

------------------------------------------------------------------------

[**[display isis mesh-group]{lang="EN-US"}**]{#struct_0_x1984_13510_2146417389}[命令用来显示]{style="font-family:宋体"}[IS-IS Mesh-Group]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1437987018}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x2137737692}**[isis]{lang="EN-US"}**[ **mesh-group** \[ *process-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612810672}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_213582883}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_414035053}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_240135857}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1508621211}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1583310781}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1803316842}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_641731903}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_1612745136}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[的配置信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1752472943}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1441821204}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_759552280}[配置路由器上运行]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口和]{style="font-family:宋体"}[Serial2/1/1]{lang="EN-US"}[接口属于]{style="font-family:宋体"}[Mesh-Group 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1446073709}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] isis mesh-group 100]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/1]{lang="EN-US"}

[\[Sysname-Serial2/1/1\] isis mesh-group 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_166383419}[显示配置的]{style="font-family:宋体"}[IS-IS Mesh-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\[Sysname-Serial2/1/1\] display isis mesh-group]{lang="EN-US"}]{#struct_0_x1984_13510_1612286385}

[               Mesh Group information for IS-IS(1)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Interface          Status]{lang="EN-US"}

[ Serial2/1/0         Blocked]{lang="EN-US"}

[ Serial2/1/1          100]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_162983572}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1384917752}[配置交换机上运行]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接口和]{style="font-family:宋体"}[Vlan-interface20]{lang="EN-US"}[接口属于]{style="font-family:宋体"}[Mesh-Group 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_449768312}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis mesh-group 100]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] interface vlan-interface 20]{lang="EN-US"}

[\[Sysname-Vlan-interface20\] isis mesh-group 100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1636178271}[显示配置的]{style="font-family:宋体"}[IS-IS Mesh-Group]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\[Sysname-Vlan-interface20\] display isis mesh-group]{lang="EN-US"}]{#struct_0_x1984_13510_1612220849}

[ ]{lang="EN-US"}

[                       Mesh Group information for IS-IS(1)]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Interface          Status]{lang="EN-US"}

[ Vlan10              Blocked]{lang="EN-US"}

[ Vlan20              100]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display isis mesh-group]{lang="EN-US"}]{#struct_0_x1984_13510_x926481046}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1420921593}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1287424521}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x294958908}

[[Interface]{lang="EN-US"}]{#struct_0_x1984_13510_x146505294}

[[接口名称]{style="font-family:宋体"}]{#struct_0_x1984_13510_269333351}

[[Status]{lang="EN-US"}]{#struct_0_x1984_13510_1612155313}

[[接口所属的]{style="font-family:宋体"}[Mesh-Group/]{lang="EN-US"}]{#struct_0_x1984_13510_x1372626219}[是否配置了接口阻塞]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#461322032 .myid}
[]{#_Toc404788356}[]{#struct_0_x1984_13510_x23322530}[]{#_Toc310604325}[]{#_Toc290886762}[]{#_Toc252200741}[]{#_Toc163546245}[]{#_Toc94930836}[]{#_Toc94586568}

**IS-IS \-- IS-IS配置命令 \-- display isis name-table**

------------------------------------------------------------------------

[**[display isis name-table]{lang="EN-US"}**]{#struct_0_x1984_13510_x2094097686}[命令用来显示系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[到主机名称的映射关系表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1577865610}

[**[display ]{lang="EN-US"}**]{#struct_0_x1984_13510_x533687856}**[isis]{lang="EN-US"}[ name-table ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x117340920}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1318113854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612089777}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_157955432}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1974339281}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1566579631}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1853086996}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1849190908}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_1265525732}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[到主机名称的映射关系表。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[到主机名称的映射关系表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x643524049}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x294692268}[显示系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[到主机名称的映射关系表。]{style="font-family:宋体"}

[[\<Sysname\> display isis name-table]{lang="EN-US"}]{#struct_0_x1984_13510_x441677207}

[                      Name table information for IS-IS(1)]{lang="EN-US"}

[                      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ System ID           Hostname                            Type       Level]{lang="EN-US"}

[ 6789.0000.0001      RUTA                                DYNAMIC    Level-1]{lang="EN-US"}

[ 6789.0000.0001      RUTA                                DYNAMIC    Level-2]{lang="EN-US"}

[ 0000.0000.0041      RUTB                                STATIC     Level-1]{lang="EN-US"}

[ 0000.0000.0041      RUTB                                STATIC     Level-2]{lang="EN-US"}

[ 6789.0000.0001.01   DIS-A                               DYNAMIC    Level-1]{lang="EN-US"}

[ 0000.0000.0041.01   DIS-B                               DYNAMIC    Level-2]{lang="EN-US"}

[]{#struct_0_x1984_13510_x2101629899}[]{#_Toc94753869}[]{#_Toc94671195}[]{#_Toc73952272}[[表1-8 ]{lang="EN-US"}[display isis name-table]{lang="EN-US"}]{#_Toc68319405}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1420232108}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612482993}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_221059955}

[[System ID]{lang="EN-US"}]{#struct_0_x1984_13510_x201185017}

[[系统]{style="font-family:宋体"}]{#struct_0_x1984_13510_838350823}[ID]{lang="EN-US"}

[[Hostname]{lang="EN-US"}]{#struct_0_x1984_13510_1966336991}

[[主机名称]{style="font-family:宋体"}]{#struct_0_x1984_13510_x294383734}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_1612417457}

[[系统]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1735034568}[ID]{lang="EN-US"}[与主机名称映射关系的生成方式，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DYNAMIC]{lang="EN-US"}]{#struct_0_x1984_13510_x314024679}[：]{style="font-family:宋体"}[表示映射关系是动态生成的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STATIC]{lang="EN-US"}]{#struct_0_x1984_13510_x649223134}[：]{style="font-family:宋体"}[表示映射关系是通过静态配置的]{lang="EN-US" style="font-family:宋体"}

[[Level]{lang="EN-US"}]{#struct_0_x1984_13510_x976149280}

[[系统]{style="font-family:宋体"}]{#struct_0_x1984_13510_x976083744}[ID]{lang="EN-US"}[与主机名称映射关系生效的]{style="font-family:宋体"}[Level]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x1357285838}[：表示该映射关系在]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[生效]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x976018208}[：表示该映射关系在]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[生效]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-1159071170 .myid}
[]{#_Toc404788357}[]{#struct_0_x1984_13510_x121398257}[]{#_Toc332962779}

**IS-IS \-- IS-IS配置命令 \-- display isis non-stop-routing event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_461678036}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x460787576}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display isis non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_x1984_13510_1612351921}[命令用来显示]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1314811734}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x1984_13510_x142343614}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display isis non-stop-routing event-log slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1984_13510_122723411}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_250896821}[模式：]{style="font-family:宋体"}

[**[display isis non-stop-routing event-log chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1984_13510_344439544}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_289660190}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1599875117}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612810673}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_213648419}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1062352555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1601781026}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1779460063}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_618517633}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_x1979563329}*[ slot-number]{lang="EN-US"}*[：显示指定单板的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_x2051520600}*[ slot-number]{lang="EN-US"}*[：显示指定成员设备的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x1984_13510_x1012333905}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_x441677208}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612745137}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1752538479}[显示]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis non-stop-routing event-log slot 0]{lang="EN-US"}]{#struct_0_x1984_13510_x441677209}

[IS-IS loginfo :]{lang="EN-US"}

[Jul 20 08:34:05 2012 -Slot=0 Enter HA Block status]{lang="EN-US"}

[Jul 19 22:34:05 2012 -Slot=0 Exit HA Block status]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Initialization).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Smooth).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (First SPF computation).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Redistribution).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Second SPF computation).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (LSP stability).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (LSP generation).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 enter NSR phase (Finish).]{lang="EN-US"}

[Jul 19 22:37:53 2012 -Slot=0 Process 1 NSR complete.]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display isis graceful-restart event-log]{lang="EN-US"}]{#struct_0_x1984_13510_1571252500}[显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1413569493}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1737941378}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612220846}

[[NSR phase]{lang="EN-US"}]{#struct_0_x1984_13510_x927333014}

[[NSR]{lang="EN-US"}]{#struct_0_x1984_13510_648568521}[阶段]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initializa]{lang="EN-US"}]{#struct_0_x1984_13510_x130703409}[tion]{lang="EN-US"}[：初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_x1984_13510_x2064820399}[：平滑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[First SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_x2083971924}[：第一次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_x1984_13510_1612155310}[：引入路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Second SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_x1372560683}[：第二次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_x1984_13510_x1078805488}[：准备生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1984_13510_x95307642}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成和泛洪]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1984_13510_x1195756027}[：完成]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-2003583750 .myid}
[]{#_Toc404788358}[]{#struct_0_x1984_13510_x2047333177}[]{#_Toc332962780}

**IS-IS \-- IS-IS配置命令 \-- display isis non-stop-routing status**

------------------------------------------------------------------------

[**[display isis non-stop-routing status]{lang="EN-US"}**]{#struct_0_x1984_13510_1612089774}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_157889896}

[**[display isis non-stop-routing status]{lang="EN-US"}**]{#struct_0_x1984_13510_11898668}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2112532253}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1027451000}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1867312477}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1094794532}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_668084923}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x718591308}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1612548526}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1757632165}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x610068231}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态。]{style="font-family:宋体"}

[[\<Sysname\> display isis non-stop-routing status]{lang="EN-US"}]{#struct_0_x1984_13510_x441677203}

[ ]{lang="EN-US"}

[                        Nonstop Routing information for IS-IS(1)]{lang="EN-US"}

[                    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[NSR phase: Finish]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display isis non-stop-routing status]{lang="EN-US"}]{#struct_0_x1984_13510_x880577268}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1416768338}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612482990}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_220994419}

[[NSR phase]{lang="EN-US"}]{#struct_0_x1984_13510_1472391299}

[[NSR]{lang="EN-US"}]{#struct_0_x1984_13510_1823522952}[阶段]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initializa]{lang="EN-US"}]{#struct_0_x1984_13510_x1989927824}[tion]{lang="EN-US"}[：初始化]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_x1984_13510_x30260255}[：平滑]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[First SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_x222164879}[：第一次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_x1984_13510_1612417454}[：引入路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Second SPF computation]{lang="EN-US"}]{#struct_0_x1984_13510_x1734969032}[：第二次路由计算]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP stability]{lang="EN-US"}]{#struct_0_x1984_13510_1315361820}[：准备生成]{style="font-family:宋体"}[LSP]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP generation]{lang="EN-US"}]{#struct_0_x1984_13510_1766625455}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成和泛洪]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_x1984_13510_293116557}[：完成]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#-975655005 .myid}
[]{#_Toc404788359}[]{#struct_0_x1984_13510_1976811819}

**IS-IS \-- IS-IS配置命令 \-- display isis peer**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1612351918}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1315401557}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[display isis peer]{lang="EN-US"}**]{#struct_0_x1984_13510_1123083783}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1932235177}

[**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x408009933}**[isis]{lang="EN-US"}**[ **peer** \[ **statistics** \| **verbose** \] \[ *process-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_671758449}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1012025025}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_269806540}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1167152644}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x942461689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1786152433}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1762889245}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612745134}

[**[statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_x1752604015}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1984_13510_x454688702}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的详细信息。如果未指定该参数，将显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x797534301}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的邻居信息。如果未指定本参数，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1525918165}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1612286383}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis peer]{lang="EN-US"}]{#struct_0_x1984_13510_163376788}

[ ]{lang="EN-US"}

[                         Peer information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ System Id: 0000.0000.0001]{lang="EN-US"}

[ Interface: GE1/0/2                  Circuit Id:  0000.0000.0001.01]{lang="EN-US"}

[ State: Up     HoldTime:  27s       Type: L1(L1L2)     PRI: 64]{lang="EN-US"}

[ ]{lang="EN-US"}

[ System Id: 0000.0000.0001]{lang="EN-US"}

[ Interface: GE1/0/2                  Circuit Id:  0000.0000.0001.01]{lang="EN-US"}

[ State: Up     HoldTime:  27s       Type: L2(L1L2)     PRI: 64]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x16468240}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis peer verbose]{lang="EN-US"}]{#struct_0_x1984_13510_x1633318302}

[ ]{lang="EN-US"}

[                         Peer information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ System ID: 0000.1111.2222]{lang="EN-US"}

[ Interface: GE1/0/2                  Circuit Id:  0000.1111.2222.01]{lang="EN-US"}

[ State: Up     Holdtime:   6s       Type: L1(L1L2)     PRI: 64]{lang="EN-US"}

[ Area address(es): 49]{lang="EN-US"}

[ Peer IP address(es): 12.0.0.2]{lang="EN-US"}

[ Peer local circuit ID: 1]{lang="EN-US"}

[ Peer circuit SNPA address: 000c-293b-c4be]{lang="EN-US"}

[ Uptime: 00:05:07]{lang="EN-US"}

[ Adj protocol:  IPv4]{lang="EN-US"}

[ Adj P2P three-way handshake: No]{lang="EN-US"}

[Graceful Restart capable]{lang="EN-US"}

[   Restarting signal: No]{lang="EN-US"}

[   Suppress adjacency advertisement: No]{lang="EN-US"}

[ Local topology:]{lang="EN-US"}

[   0    2]{lang="EN-US"}

[ Remote topology:]{lang="EN-US"}

[   0    2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ System ID: 0000.0000.0002]{lang="EN-US"}

[ Interface: GE1/0/3                  Circuit Id:  001]{lang="EN-US"}

[ State: Up     HoldTime: 27s        Type: L1L2         PRI: \--]{lang="EN-US"}

[ Area address(es): 49]{lang="EN-US"}

[ Peer IP address(es): 192.168.220.30]{lang="EN-US"}

[ Peer local circuit ID: 1]{lang="EN-US"}

[ Peer circuit SNPA address: 000c-29fd-ed69]{lang="EN-US"}

[ Uptime: 00:05:07]{lang="EN-US"}

[ Adj protocol:  IPv4]{lang="EN-US"}

[ Adj P2P three-way handshake: Yes]{lang="EN-US"}

[   Peer extended circuit ID: 2]{lang="EN-US"}

[Graceful Restart capable]{lang="EN-US"}

[   Restarting signal: No]{lang="EN-US"}

[   Suppress adjacency advertisement: No]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display isis peer]{lang="EN-US"}]{#struct_0_x1984_13510_x927398550}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1415911530}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1682528812}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1612155311}

[[System Id]{lang="EN-US"}]{#struct_0_x1984_13510_x1372495147}

[[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_x1984_13510_1269704022}

[[Interface]{lang="EN-US"}]{#struct_0_x1984_13510_x1318967847}

[[与对端相连的本地]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1023189133}[IS-IS]{lang="EN-US"}[接口]{style="font-family:宋体"}

[[Circuit Id]{lang="EN-US"}]{#struct_0_x1984_13510_x1898622298}

[[链路]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_1041983731}

[[State]{lang="EN-US"}]{#struct_0_x1984_13510_1612089775}

[[链路状态]{style="font-family:宋体"}]{#struct_0_x1984_13510_157824360}

[[HoldTime]{lang="EN-US"}]{#struct_0_x1984_13510_x1889883677}

[[抑制时间，随着时间推移递减，如果在抑制时间内还没有收到邻居发送的]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1359577103}[Hello]{lang="EN-US"}[报文，则认为邻居已经失效，如果收到了]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文，则抑制时间将重置为初始值]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_x2136750823}

[[链路关系类型，其中：]{style="font-family:宋体"}]{#struct_0_x1984_13510_970414788}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1]{lang="EN-US"}]{#struct_0_x1984_13510_1612548527}[：表示与邻居建立的链路类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，邻居路由器类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2]{lang="EN-US"}]{#struct_0_x1984_13510_x1757697701}[：表示与邻居建立的链路类型为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，邻居路由器类型为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L1(L]{lang="EN-US"}]{#struct_0_x1984_13510_x1569875051}[1L]{lang="EN-US"}[2)]{lang="EN-US"}[：表示与邻居建立的链路类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，邻居路由器类型为]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L2(L]{lang="EN-US"}]{#struct_0_x1984_13510_x993682152}[1L]{lang="EN-US"}[2)]{lang="EN-US"}[：表示与邻居建立的链路类型为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，邻居路由器类型为]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}

[[PRI]{lang="EN-US"}]{#struct_0_x1984_13510_1165901108}

[[邻居接口]{style="font-family:宋体"}]{#struct_0_x1984_13510_1612482991}[DIS]{lang="EN-US"}[优先级]{style="font-family:宋体"}

[[Area Address(es)]{lang="EN-US"}]{#struct_0_x1984_13510_220928883}

[[邻居所在区域地址]{style="font-family:宋体"}]{#struct_0_x1984_13510_x932594690}

[[Peer IP Address(es)]{lang="EN-US"}]{#struct_0_x1984_13510_x1658974191}

[[邻居接口的]{style="font-family:宋体"}]{#struct_0_x1984_13510_1612417455}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Uptime]{lang="EN-US"}]{#struct_0_x1984_13510_x1734903496}

[[邻居关系保持时间]{style="font-family:宋体"}]{#struct_0_x1984_13510_1379592734}

[[Adj Protocol]{lang="EN-US"}]{#struct_0_x1984_13510_164437401}

[[邻接协议：]{style="font-family:宋体"}]{#struct_0_x1984_13510_978612619}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}

[[Peer local circuit ID]{lang="EN-US"}]{#struct_0_x1984_13510_1612351919}

[[邻居链路]{style="font-family:宋体"}[ID ]{lang="EN-US"}]{#struct_0_x1984_13510_x1315336021}

[[Peer circuit SNPA address]{lang="EN-US"}]{#struct_0_x1984_13510_x678858779}

[[邻居子网连接点地址]{style="font-family:宋体"}]{#struct_0_x1984_13510_1726307881}

[[Adj P2P three-way handshake]{lang="EN-US"}]{#struct_0_x1984_13510_x975952675}

[[邻居是否支持]{style="font-family:宋体"}]{#struct_0_x1984_13510_x975887139}[P2P]{lang="EN-US"}[三次握手]{style="font-family:宋体"}

[[Peer extended circuit ID]{lang="EN-US"}]{#struct_0_x1984_13510_x975821603}

[[邻居接口的扩展链路]{style="font-family:宋体"}]{#struct_0_x1984_13510_x975756067}[ID]{lang="EN-US"}[，邻居支持三次握手时存在该项]{style="font-family:宋体"}

[[Graceful Restart capable]{lang="EN-US"}]{#struct_0_x1984_13510_1612810671}

[[GR Helper]{lang="EN-US"}]{#struct_0_x1984_13510_213779491}[能力]{style="font-family:宋体"}

[[Restarting signal]{lang="EN-US"}]{#struct_0_x1984_13510_x1303759346}

[[RR]{lang="EN-US"}]{#struct_0_x1984_13510_323067285}[标记]{style="font-family:宋体"}

[[Suppress adjacency advertisement]{lang="EN-US"}]{#struct_0_x1984_13510_1612745135}

[[SA]{lang="EN-US"}]{#struct_0_x1984_13510_x1752669551}[标记]{style="font-family:宋体"}

[[Local topology]{lang="EN-US"}]{#struct_0_x1984_13510_x976149282}

[[本端接口支持的拓扑列表]{style="font-family:宋体"}]{#struct_0_x1984_13510_x976083746}

[[Remote topology]{lang="EN-US"}]{#struct_0_x1984_13510_x975952674}

[[邻居接口支持的拓扑列表]{style="font-family:宋体"}]{#struct_0_x1984_13510_x975887138}

[]{#_Toc50204092}[[ ]{lang="EN-US"}]{#_Toc33866091}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1550402389}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis peer statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x1789583649}

[ ]{lang="EN-US"}

[                    Peer Statistics information for IS-IS(1)]{lang="EN-US"}

[                    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Type              IPv4 Up/Init              IPv6 Up/Init]{lang="EN-US"}

[  LAN Level-1             1/0                       0/0]{lang="EN-US"}

[  LAN Level-2             1/0                       0/0]{lang="EN-US"}

[  P2P                     0/0                       0/0]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display isis peer statistics]{lang="EN-US"}]{#struct_0_x1984_13510_855027018}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1440257563}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1116596969}

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1168249695}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_x1152411128}

[[邻居类型，取值为：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x2092572989}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAN Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x983126948}[：]{style="font-family:宋体"}[表示网络类型为广播的]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[邻居个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LAN Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_645868953}[：]{style="font-family:宋体"}[表示网络类型为广播的]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[邻居个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[P2P]{lang="EN-US"}]{#struct_0_x1984_13510_x1116662505}[：表示网络类型为点对点的邻居个数]{style="font-family:宋体"}

[[IPv4 Up]{lang="EN-US"}]{#struct_0_x1984_13510_7601776}

[[状态为]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1984_13510_x249889640}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻居个数]{style="font-family:宋体"}

[[IPv4 Init]{lang="EN-US"}]{#struct_0_x1984_13510_x676910271}

[[状态为]{style="font-family:宋体"}[init]{lang="EN-US"}]{#struct_0_x1984_13510_667026144}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[邻居个数]{style="font-family:宋体"}

[[IPv6 Up]{lang="EN-US"}]{#struct_0_x1984_13510_294560424}

[[状态为]{style="font-family:宋体"}[up]{lang="EN-US"}]{#struct_0_x1984_13510_x1116728041}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居个数]{style="font-family:宋体"}

[[IPv6 Init]{lang="EN-US"}]{#struct_0_x1984_13510_x421065707}

[[状态为]{style="font-family:宋体"}[init]{lang="EN-US"}]{#struct_0_x1984_13510_1652662947}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[邻居个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1828480212 .myid}
[]{#_Toc163546247}[]{#_Toc404788360}[]{#struct_0_x1984_13510_x307020908}[]{#_Toc303839435}

**IS-IS \-- IS-IS配置命令 \-- display isis redistribute**

------------------------------------------------------------------------

[**[display isis redistribute]{lang="EN-US"}**]{#struct_0_x1984_13510_x123735938}[命令用来显示]{style="font-family:
宋体"}[IS-IS]{lang="EN-US"}[引入路由的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_841917357}

[**[display isis redistribute ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *topo-name* \] \[ *ip-address mask-lengh* ]{lang="EN-US"}[\] \] \[ **level-1** \| **level-2** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x38223615}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1116793577}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1922476095}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1437644243}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1268584659}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1028007314}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x198656188}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x598601819}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1275022900}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_x1845546556}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由信息。缺省情况下，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由信息。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x975756066}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address mask-lengh]{lang="EN-US"}*]{#struct_0_x1984_13510_x1116334825}[：显示指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码长度的引入路由。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x1089006568}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x219003955}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1899596829}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1430202242}

[[如果不指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x50682797}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_169824181}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1203051436}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[引入路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis redistribute 1]{lang="EN-US"}]{#struct_0_x1984_13510_x1116400361}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                        Level-1 IPv4 Redistribute Table]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Type IPv4 Destination     IntCost    ExtCost    Tag        State]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ D    192.168.30.0/24      0          0                     Active]{lang="EN-US"}

[ D    11.11.11.11/32       0          0]{lang="EN-US"}

[ D    10.10.10.0/24        0          0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Type: D -Direct, I -ISIS, S -Static, O -OSPF, B -BGP, R --RIP]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display isis redistribute]{lang="EN-US"}]{#struct_0_x1984_13510_x1772610552}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1442599600}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_946294591}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_164215237}

[[Route information for IS-IS(1)]{lang="EN-US"}]{#struct_0_x1984_13510_295328389}

[[指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465897}[进程引入路由信息]{style="font-family:宋体"}

[[Level-1 IPv4 Redistribute Table]{lang="EN-US"}]{#struct_0_x1984_13510_2103895979}

[[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1459838319}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[引入路由信息]{style="font-family:宋体"}

[[Level-2  IPv4 Redistribute  Table]{lang="EN-US"}]{#struct_0_x1984_13510_487966944}

[[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x1267202221}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[引入路由信息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_532125348}

[[引入的路由类型，包括直连、]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1116531433}[、静态、]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[、]{style="font-family:宋体"}[BGP]{lang="EN-US"}[、]{style="font-family:宋体"}[RIP]{lang="EN-US"}

[[IPV4 Destination]{lang="EN-US"}]{#struct_0_x1984_13510_x696887182}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_141990731}[目的地址]{style="font-family:宋体"}

[[IntCost]{lang="EN-US"}]{#struct_0_x1984_13510_x867075942}

[[路由内部]{style="font-family:宋体"}]{#struct_0_x1984_13510_635922275}[Cost]{lang="EN-US"}

[[ExtCost]{lang="EN-US"}]{#struct_0_x1984_13510_x1116072681}

[[路由外部]{style="font-family:宋体"}]{#struct_0_x1984_13510_x485989998}[Cost]{lang="EN-US"}

[[Tag]{lang="EN-US"}]{#struct_0_x1984_13510_1523389723}

[[引入路由发布时的]{style="font-family:宋体"}]{#struct_0_x1984_13510_833899891}[Tag]{lang="EN-US"}[值]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1984_13510_1431753890}

[[引入路由是否为最终生效路由]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116138217}

[ ]{lang="EN-US"}

::: {#-535663809 .myid}
[]{#_Toc404788361}[]{#struct_0_x1984_13510_x1720505640}

**IS-IS \-- IS-IS配置命令 \-- display isis route**

------------------------------------------------------------------------

[**[display isis route]{lang="EN-US"}**]{#struct_0_x1984_13510_x1847078294}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1475366301}

[**[display isis route]{lang="EN-US"}**[ \[ **ipv4** \[ **topology** *topo-name* \] \[ ]{lang="EN-US"}*[ip-address mask-length]{lang="EN-US"}*[ \] \] \[ \[ **level-1** \| **level-2** \] \| **verbose** \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1812991796}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1441727059}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1374946189}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1517238991}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1116596968}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1560633660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_854962516}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1354104987}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1779666547}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_x542529814}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。缺省情况下，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x1379433806}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[ip-address ]{lang="EN-US"}[mask-length]{lang="EN-US"}*]{#struct_0_x1984_13510_222767776}[：显示指定目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和掩码长度的路由。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1984_13510_x1308052728}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[详细的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。如果未指定该参数，将显示路由信息的概要信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x1116662504}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1573685717}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1915448682}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_377866511}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定级别，将同时显示]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1700754792}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[路由信息]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_x691394588}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1421936569}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x274552319}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis route]{lang="EN-US"}]{#struct_0_x1984_13510_x1116793576}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-1 IPv4 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPv4 Destination     IntCost    ExtCost ExitInterface   NextHop         Flags]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 8.8.8.0/24           10         NULL    GE1/0/2         Direct          D/L/-]{lang="EN-US"}

[ 9.9.9.0/24           20         NULL    GE1/0/2         8.8.8.5         R/L/-]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-2 IPv4 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPv4 Destination     IntCost    ExtCost ExitInterface   NextHop         Flags]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 8.8.8.0/24           10         NULL                                    D/L/-]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display isis route]{lang="EN-US"}]{#struct_0_x1984_13510_356392154}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1437658818}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_320192217}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_890515730}

[[Route information for IS-IS(1)]{lang="EN-US"}]{#struct_0_x1984_13510_x1116334824}

[[指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1639876787}[进程路由信息]{style="font-family:宋体"}

[[Level-1 IPv4 Forwarding Table]{lang="EN-US"}]{#struct_0_x1984_13510_x1639503132}

[[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1306780133}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[路由信息]{style="font-family:宋体"}

[[Level-2 IPv4 Forwarding Table]{lang="EN-US"}]{#struct_0_x1984_13510_x2068044916}

[[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x1077076773}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[路由信息]{style="font-family:宋体"}

[[IPv4 Destination]{lang="EN-US"}]{#struct_0_x1984_13510_x1116400360}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x206526611}[目的地址]{style="font-family:宋体"}

[[IntCost]{lang="EN-US"}]{#struct_0_x1984_13510_x1865753990}

[[路由内部]{style="font-family:宋体"}]{#struct_0_x1984_13510_360578951}[Cost]{lang="EN-US"}

[[ExtCost]{lang="EN-US"}]{#struct_0_x1984_13510_1836594428}

[[路由外部]{style="font-family:宋体"}]{#struct_0_x1984_13510_237191690}[Cost]{lang="EN-US"}

[[ExitInterface]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465896}

[[出接口]{style="font-family:宋体"}]{#struct_0_x1984_13510_x624987376}

[[NextHop]{lang="EN-US"}]{#struct_0_x1984_13510_x1516729058}

[[下一跳]{style="font-family:宋体"}]{#struct_0_x1984_13510_x530968562}

[[Flags]{lang="EN-US"}]{#struct_0_x1984_13510_1924237261}

[[路由状态标志]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116531432}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1984_13510_2031996173}[：直连路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1984_13510_2034572820}[：该路由是否已放到路由表中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x1984_13510_630190577}[：是否已经通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1984_13510_x1116072680}[：路由渗透状态标识。设置为"]{style="font-family:宋体"}[Up]{lang="EN-US"}["表示可以避免由]{style="font-family:宋体"}[L2]{lang="EN-US"}[发送到]{style="font-family:宋体"}[L1]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[又返回给]{style="font-family:宋体"}[L2]{lang="EN-US"}[，设置为"]{style="font-family:宋体"}[Down]{lang="EN-US"}["表示不可以]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x2052073939}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis route verbose]{lang="EN-US"}]{#struct_0_x1984_13510_x1116138216}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-1 IPv4 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV4 Dest : 8.8.8.0/24          Int. Cost : 10               Ext. Cost : NULL]{lang="EN-US"}

[ Admin Tag : -                   Src Count : 2                Flag      : D/L/-]{lang="EN-US"}

[ NextHop   :                     Interface :                  ExitIndex :]{lang="EN-US"}

[    Direct                             GE1/0/2                     0x00000000]{lang="EN-US"}

[ Nib ID    : 0x0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV4 Dest : 9.9.9.0/24          Int. Cost : 20               Ext. Cost : NULL]{lang="EN-US"}

[ Admin Tag : -                   Src Count : 1                Flag      : R/L/-]{lang="EN-US"}

[ NextHop   :                     Interface :                  ExitIndex :]{lang="EN-US"}

[    8.8.8.5                            GE1/0/2                     0x00000003]{lang="EN-US"}

[ Nib ID    : 0x0]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-2 IPv4 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV4 Dest : 8.8.8.0/24          Int. Cost : 10               Ext. Cost : NULL]{lang="EN-US"}

[ Admin Tag : -                   Src Count : 2                Flag      : D/L/-]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display isis route verbose]{lang="EN-US"}]{#struct_0_x1984_13510_1008377715}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1430616852}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_1629127135}

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_160874278}

[[Route information for IS-IS(1)]{lang="EN-US"}]{#struct_0_x1984_13510_462109274}

[[指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x2048456690}[进程的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息]{style="font-family:宋体"}

[[Level-1 IPv4 Forwarding Table]{lang="EN-US"}]{#struct_0_x1984_13510_x1116596971}

[[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x812084871}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[路由信息]{style="font-family:宋体"}

[[Level-2 IPv4 Forwarding Table]{lang="EN-US"}]{#struct_0_x1984_13510_x1959746526}

[[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x246148971}[的]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[路由信息]{style="font-family:宋体"}

[[IPV4 Dest]{lang="EN-US"}]{#struct_0_x1984_13510_707311006}

[[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_962337632}[目的地址]{style="font-family:宋体"}

[[Int. Cost]{lang="EN-US"}]{#struct_0_x1984_13510_x1116662507}

[[路由内部]{style="font-family:宋体"}]{#struct_0_x1984_13510_1170401190}[Cost]{lang="EN-US"}

[[Ext. Cost]{lang="EN-US"}]{#struct_0_x1984_13510_x688472081}

[[路由外部]{style="font-family:宋体"}]{#struct_0_x1984_13510_1830181819}[Cost]{lang="EN-US"}

[[Admin Tag]{lang="EN-US"}]{#struct_0_x1984_13510_1025089634}

[[Tag]{lang="EN-US"}]{#struct_0_x1984_13510_x1116728043}[值]{style="font-family:宋体"}

[[Src Count]{lang="EN-US"}]{#struct_0_x1984_13510_741733707}

[[发布源个数]{style="font-family:宋体"}]{#struct_0_x1984_13510_488988636}

[[Flag]{lang="EN-US"}]{#struct_0_x1984_13510_x378385865}

[[路由状态标志]{style="font-family:宋体"}]{#struct_0_x1984_13510_2069520373}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1984_13510_x1116793579}[：该路由是否已放到路由表中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x1984_13510_x1565922147}[：是否已经通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1984_13510_x1828491224}[：路由渗透状态标识。设置为"]{style="font-family:宋体"}[Up]{lang="EN-US"}["表示可以避免由]{style="font-family:宋体"}[L2]{lang="EN-US"}[发送到]{style="font-family:宋体"}[L1]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[又返回给]{style="font-family:宋体"}[L2]{lang="EN-US"}[，设置为"]{style="font-family:宋体"}[Down]{lang="EN-US"}["表示不可以]{style="font-family:宋体"}

[[Next Hop]{lang="EN-US"}]{#struct_0_x1984_13510_x1799426888}

[[下一跳]{style="font-family:宋体"}]{#struct_0_x1984_13510_540491483}

[[Interface]{lang="EN-US"}]{#struct_0_x1984_13510_x1116334827}

[[出接口]{style="font-family:宋体"}]{#struct_0_x1984_13510_2043161314}

[[ExitIndex]{lang="EN-US"}]{#struct_0_x1984_13510_x63657074}

[[出接口索引]{style="font-family:宋体"}]{#struct_0_x1984_13510_53994103}

[[Nib ID]{lang="EN-US"}]{#struct_0_x1984_13510_x1379040590}

[[路由管理分配的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_x1379630413}[，即下一跳索引]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1484573961 .myid}
[]{#_Toc163546249}[]{#_Toc404788362}[]{#struct_0_x1984_13510_x1116400363}[]{#_Toc341967378}[]{#_Toc341285953}[]{#_Toc163546333}[]{#_Toc166583084}[]{#_Toc163546358}[]{#_Toc166583109}

**IS-IS \-- IS-IS配置命令 \-- display isis spf-tree**

------------------------------------------------------------------------

[**[display isis spf-tree]{lang="EN-US"}**]{#struct_0_x1984_13510_1359557330}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1849560016}

[**[display isis spf-tree ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *topo-name* \] \] \[ \[ **level-1** \| **level-2** \] \| **verbose** \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1008438796}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1784687453}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x2086538931}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x968609220}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x2009992889}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x407904938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465899}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1740732623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x587106880}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_1498033556}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑信息。如果未指定该参数，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x1379499341}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_2104228575}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[拓扑信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1050952710}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[拓扑信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_x1984_13510_501506286}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的详细拓扑信息。如果未指定该参数，显示概要拓扑信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x630191383}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的拓扑信息。如果未指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的拓扑信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x741905044}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1116531435}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis spf-tree]{lang="EN-US"}]{#struct_0_x1984_13510_x1116072683}

[ ]{lang="EN-US"}

[                        Shortest Path Tree for IS-IS(1)]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: S-Node is on SPF tree       T-Node is on tent list]{lang="EN-US"}

[             O-Node is overload          R-Node is directly reachable]{lang="EN-US"}

[             I-Node or Link is isolated  D-Node or Link is to be deleted]{lang="EN-US"}

[             C-Neighbor is child         P-Neighbor is parent]{lang="EN-US"}

[             V-Link is involved          N-Link is a new path]{lang="EN-US"}

[             L-Link is on change list    U-Protocol usage is changed]{lang="EN-US"}

[             H-Nexthop is changed]{lang="EN-US"}

[ ]{lang="EN-US"}

[                           Level-1 Shortest Path Tree]{lang="EN-US"}

[                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[SpfNode            NodeFlag       SpfLink            LinkCost LinkFlag]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0000.0000.0032.00  S/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0032.01  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  0        -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  0        -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0064.00  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[ ]{lang="EN-US"}

[                           Level-2 Shortest Path Tree]{lang="EN-US"}

[                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[SpfNode            NodeFlag       SpfLink            LinkCost LinkFlag]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0000.0000.0032.00  S/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0032.01  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  0        -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  0        -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0064.00  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1648789412}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[详细拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis spf-tree verbose]{lang="EN-US"}]{#struct_0_x1984_13510_1903463012}

[ ]{lang="EN-US"}

[                        Shortest Path Tree for IS-IS(1)]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: S-Node is on SPF tree       T-Node is on tent list]{lang="EN-US"}

[             O-Node is overload          R-Node is directly reachable]{lang="EN-US"}

[             I-Node or Link is isolated  D-Node or Link is to be deleted]{lang="EN-US"}

[             C-Neighbor is child         P-Neighbor is parent]{lang="EN-US"}

[             V-Link is involved          N-Link is a new path]{lang="EN-US"}

[             L-Link is on change list    U-Protocol usage is changed]{lang="EN-US"}

[             H-Nexthop is changed]{lang="EN-US"}

[ ]{lang="EN-US"}

[                           Level-1 Shortest Path Tree]{lang="EN-US"}

[                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0001.00]{lang="EN-US"}

[ Distance       : 0]{lang="EN-US"}

[ TE distance    : 0]{lang="EN-US"}

[ NodeFlag       : S/-/-/-/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 1]{lang="EN-US"}

[ \--\>0000.0000.0004.04]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Adjacent       Interface: N/A]{lang="EN-US"}

[        Cost: 10             Nexthop  : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0004.00]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ Te Distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/-/-/-]{lang="EN-US"}

[ RelayNibID     : 0x14000000]{lang="EN-US"}

[ TE tunnel count: 1]{lang="EN-US"}

[     Destination: 4.4.4.4                  Interface  : Tun0]{lang="EN-US"}

[     TE cost    : 10                       Final cost : 10]{lang="EN-US"}

[     Add nexthop: YES                      Add TLV    : YES]{lang="EN-US"}

[ Nexthop count  : 2]{lang="EN-US"}

[     Neighbor   : 0000.0000.0004.00        Interface  : Tun0]{lang="EN-US"}

[     Nexthop    : 4.4.4.4]{lang="EN-US"}

[     BkNeighbor : N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNexthop  : N/A]{lang="EN-US"}

[     Neighbor   : 0000.0000.0004.00        Interface  : Vlan50]{lang="EN-US"}

[     Nexthop    : 1.1.1.3]{lang="EN-US"}

[     BkNeighbor : N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNexthop  : N/A]{lang="EN-US"}

[ SpfLink count  : 1]{lang="EN-US"}

[ \--\>0000.0000.0004.04]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: N/A]{lang="EN-US"}

[        Cost: 10             Nexthop  : N/A]{lang="EN-US"}

[        AdvMtID: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0004.04]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ TE distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/R/-/-]{lang="EN-US"}

[ RelayNibID     : 0x14000001]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 2]{lang="EN-US"}

[ \--\>0000.0000.0001.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: N/A]{lang="EN-US"}

[        Cost: 0              Nexthop  : N/A]{lang="EN-US"}

[ \--\>0000.0000.0004.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: Vlan50]{lang="EN-US"}

[        Cost: 0              Nexthop  : 1.1.1.3]{lang="EN-US"}

[ ]{lang="EN-US"}

[                           Level-2 Shortest Path Tree]{lang="EN-US"}

[                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0001.00]{lang="EN-US"}

[ Distance       : 0]{lang="EN-US"}

[ TE distance    : 0]{lang="EN-US"}

[ NodeFlag       : S/-/-/-/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 1]{lang="EN-US"}

[ \--\>0000.0000.0004.04]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Adjacent       Interface: N/A]{lang="EN-US"}

[        Cost: 10             Nexthop  : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0004.00]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ TE distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/-/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 1]{lang="EN-US"}

[     Destination: 4.4.4.4                  Interface  : Tun0]{lang="EN-US"}

[     TE cost    : 10                       Final cost : 10]{lang="EN-US"}

[     Add nexthop: YES                      Add TLV    : YES]{lang="EN-US"}

[ Nexthop count  : 2]{lang="EN-US"}

[     Neighbor   : 0000.0000.0004.00        Interface  : Tun0]{lang="EN-US"}

[     Nexthop    : 4.4.4.4]{lang="EN-US"}

[     BkNeighbor : N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNexthop  : N/A]{lang="EN-US"}

[     Neighbor   : 0000.0000.0004.00        Interface  : Vlan50]{lang="EN-US"}

[     Nexthop    : 1.1.1.3]{lang="EN-US"}

[     BkNeighbor : N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNexthop  : N/A]{lang="EN-US"}

[ SpfLink count  : 1]{lang="EN-US"}

[ \--\>0000.0000.0004.04]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: N/A]{lang="EN-US"}

[        Cost: 10             Nexthop  : N/A]{lang="EN-US"}

[        AdvMtID: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0004.04]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ TE distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/R/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 2]{lang="EN-US"}

[ \--\>0000.0000.0001.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: N/A]{lang="EN-US"}

[        Cost: 0              Nexthop  : N/A]{lang="EN-US"}

[ \--\>0000.0000.0004.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type: Remote         Interface: Vlan50]{lang="EN-US"}

[        Cost: 0              Nexthop  : 1.1.1.3]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display isis spf-tree]{lang="EN-US"}]{#struct_0_x1984_13510_477077373}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1426430829}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1119185662}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1826095569}

[[SpfNode]{lang="EN-US"}]{#struct_0_x1984_13510_x139208618}

[[拓扑节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_x1869773112}

[[Distance]{lang="EN-US"}]{#struct_0_x1984_13510_x1116400362}

[[根节点到该节点的最短距离]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1369326025}

[[TE distance]{lang="EN-US"}]{#struct_0_x1984_13510_x1379040592}

[[根节点到该节点的最短距离（包含隧道]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1984_13510_x1379630415}[），如果未配置隧道，则与]{style="font-family:宋体"}[Distance]{lang="EN-US"}[值相等]{style="font-family:宋体"}

[[NodeFlag]{lang="EN-US"}]{#struct_0_x1984_13510_951490731}

[[节点状态标记：]{style="font-family:宋体"}]{#struct_0_x1984_13510_1185913007}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_x1984_13510_383648176}[：节点在]{lang="EN-US" style="font-family:
  宋体"}[SPF]{lang="EN-US"}[树上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465898}[：节点在候选列表上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_x1984_13510_x174648682}[：节点处于]{lang="EN-US" style="font-family:
  宋体"}[OverLoad]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_x1984_13510_254631409}[：节点是直连的]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x1984_13510_1162044494}[：孤立节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1984_13510_217589295}[：节点待删除]{lang="EN-US" style="font-family:
  宋体"}

[[RelayNibID]{lang="EN-US"}]{#struct_0_x1984_13510_x1379499343}

[[节点的迭代下一跳]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_x1379433807}

[[TE tunnel count]{lang="EN-US"}]{#struct_0_x1984_13510_x1379302735}

[[D]{lang="EN-US"}[estination]{lang="EN-US"}]{#struct_0_x1984_13510_x1379237199}[为该节点的隧道条数]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_x1984_13510_x1379171663}

[[目的路由器]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1379040591}

[[TE cost]{lang="EN-US"}]{#struct_0_x1984_13510_x1379630418}

[[TE]{lang="EN-US"}]{#struct_0_x1984_13510_x1379499346}[隧道配置的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[开销值]{style="font-family:宋体"}

[[Final cost]{lang="EN-US"}]{#struct_0_x1984_13510_x1379433810}

[[T]{lang="EN-US"}[E]{lang="EN-US"}]{#struct_0_x1984_13510_x1379368274}[隧道的最终生效开销值]{style="font-family:宋体"}

[[Nexthop count]{lang="EN-US"}]{#struct_0_x1984_13510_x1706487623}

[[节点的下一跳个数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116531434}

[[Nexthop]{lang="EN-US"}]{#struct_0_x1984_13510_1225427119}

[[节点的主用下一跳地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_x419774784}[链路发布源下一跳地址]{style="font-family:宋体"}

[[AdvMtID]{lang="EN-US"}]{#struct_0_x1984_13510_x1379630417}

[[从哪个拓扑学到的路由：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1379499345}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_x1984_13510_x1379433809}[：标准拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[6-4094]{lang="EN-US"}]{#struct_0_x1984_13510_x1379302737}[：其它拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_x1984_13510_x2029345484}

[[节点的主用下一跳出接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_2097254732}[链路发布源下一跳出接口]{style="font-family:宋体"}

[[BkNexthop]{lang="EN-US"}]{#struct_0_x1984_13510_x1116072682}

[[节点的备份下一跳地址]{style="font-family:宋体"}]{#struct_0_x1984_13510_1080093943}

[[BkInterface]{lang="EN-US"}]{#struct_0_x1984_13510_70058715}

[[节点的备份下一跳出接口]{style="font-family:宋体"}]{#struct_0_x1984_13510_1526237194}

[[Neighbor]{lang="EN-US"}]{#struct_0_x1984_13510_x1116138218}

[[节点主用下一跳邻居节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_201808661}

[[BkNeighbor]{lang="EN-US"}]{#struct_0_x1984_13510_x2139692581}

[[节点备份下一跳邻居节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_x1984_13510_x486829678}

[[SpfLink]{lang="EN-US"}]{#struct_0_x1984_13510_1747522862}

[[拓扑链路]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116596973}

[[SpfLink count]{lang="EN-US"}]{#struct_0_x1984_13510_350714543}

[[拓扑链路个数]{style="font-family:宋体"}]{#struct_0_x1984_13510_546988620}

[[LinkCost]{lang="EN-US"}]{#struct_0_x1984_13510_62848258}

[[链路开销]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116662509}

[[LinkNewCost]{lang="EN-US"}]{#struct_0_x1984_13510_1620739884}

[[链路新开销]{style="font-family:宋体"}]{#struct_0_x1984_13510_302337273}

[[LinkFlag]{lang="EN-US"}]{#struct_0_x1984_13510_x583461838}

[[链路状态标记：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116728045}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_x1984_13510_1548302761}[：孤立链路]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_x1984_13510_x175023420}[：链路待删除]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_x1984_13510_224228920}[：目的节点是源节点的子节点]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_x1984_13510_x1116793581}[：目的节点是源节点的父节点]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_x1984_13510_x1208708747}[：链路受到影响]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_x1984_13510_x1969914483}[：新增链路]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_x1984_13510_x1116334829}[：链路在变化链表上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_x1984_13510_1236592260}[：链路协议类型发生变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_x1984_13510_x1632371288}[：链表下一跳发生变化]{style="font-family:宋体"}

[[LinkSrcCnt]{lang="EN-US"}]{#struct_0_x1984_13510_x1287767514}

[[链路发布源个数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1116400365}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_196757916}

[[链路发布源类型：]{style="font-family:宋体"}]{#struct_0_x1984_13510_511255270}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Adjacent]{lang="EN-US"}]{#struct_0_x1984_13510_1596066640}[：本地邻居维护产生]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465901}[：其它节点]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[产生]{lang="EN-US" style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_x1984_13510_x1385092088}

[[链路发布源开销]{style="font-family:宋体"}]{#struct_0_x1984_13510_x251695222}

[ ]{lang="EN-US"}

::: {#1426816344 .myid}
[]{#_Toc404788363}[]{#struct_0_x1984_13510_438479810}

**IS-IS \-- IS-IS配置命令 \-- display isis statistics**

------------------------------------------------------------------------

[**[display isis statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_x143344132}[命令用来显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1116531437}

[**[display ]{lang="EN-US"}**]{#struct_0_x1984_13510_1628711646}**[isis]{lang="EN-US"}[ statistics ]{lang="EN-US"}**[\[ **ipv4** \[ **topology** *topo-name* \] \] \[ **level-1** \| **level-1-2** \| **level-2** \] \[ *process-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1724885013}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x509422329}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1970534355}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_138738956}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1802483882}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_406636015}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1733443237}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1116072685}

[**[ipv4]{lang="EN-US"}**]{#struct_0_x1984_13510_186846743}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[统计信息。如果未指定该参数，显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[**[topology]{lang="EN-US"}**[ *topo-name*]{lang="EN-US"}]{#struct_0_x1984_13510_1652261766}[：显示指定拓扑的信息。]{style="font-family:宋体"}*[topo-name]{lang="EN-US"}*[表示拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}**[base]{lang="EN-US"}**[为公网拓扑。如果未指定本参数，则显示公网的信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1483378470}[：显示]{style="font-family:宋体"}[IS-IS Level-1]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1109142852}[：显示]{style="font-family:宋体"}[IS-IS Level-1-2]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1765745071}[：显示]{style="font-family:宋体"}[IS-IS Level-2]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_1289661757}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x240391226}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定级别，将同时显示]{style="font-family:宋体"}]{#struct_0_x1984_13510_1074496906}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_430370853}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1067076575}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_13283280}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x1116596972}

[ ]{lang="EN-US"}

[                       Statistics information for IS-IS(1)]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                               Level-1 Statistics]{lang="EN-US"}

[                               \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[MTR(base)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Learnt routes information:]{lang="EN-US"}

[         Total IPv4 Learnt Routes in IPv4 Routing Table: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Imported routes information:]{lang="EN-US"}

[         IPv4 Imported Routes:]{lang="EN-US"}

[                         Static: 0       Direct: 0]{lang="EN-US"}

[                         ISIS:   0       BGP:    0]{lang="EN-US"}

[                         RIP:    0       OSPF:   0]{lang="EN-US"}

[                         Total Number:   0]{lang="EN-US"}

[ ]{lang="EN-US"}

[MTR(base)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Learnt routes information:]{lang="EN-US"}

[         Total IPv6 Learnt Routes in IPv6 Routing Table: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Imported routes information:]{lang="EN-US"}

[         IPv6 Imported Routes:]{lang="EN-US"}

[                         Static: 0       Direct: 0]{lang="EN-US"}

[                         ISISv6: 0       BGP4+:  0]{lang="EN-US"}

[                         RIPng:  0       OSPFv3: 0]{lang="EN-US"}

[                         Total Number:   0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Lsp information:]{lang="EN-US"}

[                  LSP Source ID:          No. of used LSPs]{lang="EN-US"}

[                  7777.8888.1111                  001]{lang="EN-US"}

[ ]{lang="EN-US"}

[                               Level-2 Statistics]{lang="EN-US"}

[                               \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[MTR(base)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Learnt routes information:]{lang="EN-US"}

[         Total IPv4 Learnt Routes in IPv4 Routing Table: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Imported routes information:]{lang="EN-US"}

[         IPv4 Imported Routes:]{lang="EN-US"}

[                         Static: 0       Direct: 0]{lang="EN-US"}

[                         ISIS:   0       BGP:    0]{lang="EN-US"}

[                         RIP:    0       OSPF:   0]{lang="EN-US"}

[                         Total Number:   0]{lang="EN-US"}

[ ]{lang="EN-US"}

[MTR(base)]{lang="EN-US"}

[ ]{lang="EN-US"}

[Learnt routes information:]{lang="EN-US"}

[         Total IPv6 Learnt Routes in IPv6 Routing Table: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Imported routes information:]{lang="EN-US"}

[         IPv6 Imported Routes:]{lang="EN-US"}

[                         Static: 0       Direct: 0]{lang="EN-US"}

[                         ISISv6: 0       BGP4+:  0]{lang="EN-US"}

[                         RIPng:  0       OSPFv3: 0]{lang="EN-US"}

[                         Total Number:   0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Lsp information:]{lang="EN-US"}

[                  LSP Source ID:          No. of used LSPs]{lang="EN-US"}

[                  7777.8888.1111                  001]{lang="EN-US"}

[]{#struct_0_x1984_13510_x1215369398}[]{#_Toc94753874}[]{#_Toc94671200}[[表1-16 ]{lang="EN-US"}[display isis statistics]{lang="EN-US"}]{#_Toc73952276}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1457692554}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_835600907}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1731105062}

[[Statistics information for IS-IS(*processid*)]{lang="EN-US"}]{#struct_0_x1984_13510_x1116662508}

[[指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1108143471}[进程的统计信息]{style="font-family:宋体"}

[[Level-1 Statistics]{lang="EN-US"}]{#struct_0_x1984_13510_1992178741}

[[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1171043258}[路由统计信息]{style="font-family:宋体"}

[[Level-2 Statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x706106971}

[[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_1592056337}[路由统计信息]{style="font-family:宋体"}

[[MTR(*topo-name*)]{lang="EN-US"}]{#struct_0_x1984_13510_412774703}

[[指定某个拓扑，拓扑名为]{style="font-family:宋体"}[base]{lang="EN-US"}]{#struct_0_x1984_13510_x1153309238}[则为公网拓扑]{style="font-family:宋体"}

[[Learnt routes information]{lang="EN-US"}]{#struct_0_x1984_13510_x1116728044}

[[学习到的路由信息：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1180580594}

[[Total IPv4 Learnt Routes in IPv4 Routing Table]{lang="EN-US"}]{#struct_0_x1984_13510_x472116303}[：学习到的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息的总数]{style="font-family:宋体"}

[[Total IPv6 Learnt Routes in IPv6 Routing Table]{lang="EN-US"}]{#struct_0_x1984_13510_1806417310}[：学习到的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息的总数]{style="font-family:宋体"}

[[Imported routes information]{lang="EN-US"}]{#struct_0_x1984_13510_x1217560266}

[[IPv4 Imported Routes]{lang="EN-US"}]{#struct_0_x1984_13510_x1116793580}

[[引入]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_1520174608}[路由]{style="font-family:宋体"}[数量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x1984_13510_x494575276}[：引入的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[静态路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1984_13510_x1515355174}[：引入的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[直连路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISIS]{lang="EN-US"}]{#struct_0_x1984_13510_246477033}[：从其它]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程引入的路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP]{lang="EN-US"}]{#struct_0_x1984_13510_817317677}[：从]{style="font-family:宋体"}[BGP]{lang="EN-US"}[引入的路由数量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIP]{lang="EN-US"}]{#struct_0_x1984_13510_x1116334828}[：从]{style="font-family:宋体"}[RIP]{lang="EN-US"}[引入的路由数量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPF]{lang="EN-US"}]{#struct_0_x1984_13510_x329491681}[：从]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[引入的路由数量]{style="font-family:宋体"}

[[IPv6 Imported Routes]{lang="EN-US"}]{#struct_0_x1984_13510_x964921861}

[[引入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1984_13510_632723006}[路由数量：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Static]{lang="EN-US"}]{#struct_0_x1984_13510_397415963}[：引入的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[静态路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direct]{lang="EN-US"}]{#struct_0_x1984_13510_x1116400364}[：引入的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[直连路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISISv6]{lang="EN-US"}]{#struct_0_x1984_13510_1762841857}[：从其它]{lang="EN-US" style="font-family:宋体"}[IS-ISv6]{lang="EN-US"}[进程引入的路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[BGP4+]{lang="EN-US"}]{#struct_0_x1984_13510_x571291805}[：从]{style="font-family:宋体"}[BGP4+]{lang="EN-US"}[引入的路由数量]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIPng]{lang="EN-US"}]{#struct_0_x1984_13510_215125313}[：从]{lang="EN-US" style="font-family:宋体"}[RIPng]{lang="EN-US"}[引入的路由数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[OSPFv3]{lang="EN-US"}]{#struct_0_x1984_13510_x1116465900}[：从]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[引入的路由数量]{lang="EN-US" style="font-family:宋体"}

[[Lsp information]{lang="EN-US"}]{#struct_0_x1984_13510_180991853}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x606353510}[信息：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LSP Source ID]{lang="EN-US"}]{#struct_0_x1984_13510_210730116}[：本地生成的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No. of used LSPs]{lang="EN-US"}]{#struct_0_x1984_13510_x1116531436}[：本地生成的]{lang="EN-US" style="font-family:
  宋体"}[LSP]{lang="EN-US"}[已使用的分片数量]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1984253387 .myid}
[]{#_Toc163546276}[]{#_Toc297189171}[]{#_Toc290886767}[]{#_Toc252200746}[]{#_Toc163546250}[]{#_Toc50204094}[]{#_Toc33866093}[]{#_Toc404788364}[]{#struct_0_x1984_13510_62627705}[]{#_Toc340564365}

**IS-IS \-- IS-IS配置命令 \-- display osi**

------------------------------------------------------------------------

[**[display osi]{lang="EN-US"}**]{#struct_0_x1984_13510_42484515}[命令用来显示]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息，包括]{style="font-family:宋体"}[socket]{lang="EN-US"}[的状态、选项等，以及接收报文时需要匹配的入接口和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x107763691}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1984_13510_1246919923}

[[display osi]{lang="EN-US"}]{#struct_0_x1984_13510_x852141024}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_x1778614935}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[[display osi]{lang="EN-US"}]{#struct_0_x1984_13510_x1116072684}[ \[ ]{lang="EN-US" style="font-weight:normal"}[slot ]{lang="EN-US"}[[slot-number]{lang="EN-US" style="font-weight:normal"}]{.commandparameterChar}[ \[ ]{lang="EN-US" style="font-weight:normal"}[cpu]{lang="EN-US"}[ *cpu-number* \] \]]{lang="EN-US" style="font-weight:normal"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_x82705471}[模式：]{style="font-family:宋体"}

[**[display osi ]{lang="EN-US"}**[\[ **chassis** ]{lang="EN-US"}]{#struct_0_x1984_13510_x264622585}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}**[ slot]{lang="EN-US"}**[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1023931708}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1239457322}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x760044110}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1669795124}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_1740069933}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1116138220}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x154225091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x235492649}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x350893107}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号[，]{style="color:black"}取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的连接信息。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x1733716676}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有成员设备的连接信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_1030075098}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的连接信息。（集中式设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_1743837936}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有成员设备所有单板的连接信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x297808373}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的连接信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_x52852124}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1039139895}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_265641972}[显示所有]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的信息。]{style="font-family:宋体"}

[[\<Sysname\> display osi]{lang="EN-US"}]{#struct_0_x1984_13510_1262413018}

[Total OSI socket number: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Location: chassis 1 slot 0 cpu 0]{lang="EN-US"}

[ Creator: isisd\[1539\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: SO_FILTER]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 1048576 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 262144 / 512 / N/A]{lang="EN-US"}

[ Type: 2]{lang="EN-US"}

[ Enabled interfaces:]{lang="EN-US"}

[  GigabitEthernet0/0]{lang="EN-US"}

[   MAC address: 0180-c200-0014]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Location: chassis 1 slot 0 cpu 0]{lang="EN-US"}

[ Creator: isisd\[1539\]]{lang="EN-US"}

[ State: N/A]{lang="EN-US"}

[ Options: SO_FILTER]{lang="EN-US"}

[ Error: 0]{lang="EN-US"}

[ Receiving buffer(cc/hiwat/lowat/state): 0 / 1048576 / 1 / N/A]{lang="EN-US"}

[ Sending buffer(cc/hiwat/lowat/state): 0 / 262144 / 512 / N/A]{lang="EN-US"}

[ Type: 2]{lang="EN-US"}

[ Enabled interfaces:]{lang="EN-US"}

[  GigabitEthernet0/0]{lang="EN-US"}

[   MAC address: 0180-c200-0014]{lang="EN-US"}

[[表1-17 ]{lang="EN-US"}[display osi]{lang="EN-US"}]{#struct_0_x1984_13510_x1673219816}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1452262091}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_1623426172}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262478554}

[[Total OSI socket number]{lang="EN-US"}]{#struct_0_x1984_13510_x55726485}

[[OSI socket]{lang="EN-US"}]{#struct_0_x1984_13510_499523447}[的总数]{style="font-family:宋体"}

[[Chassis]{lang="EN-US"}]{#struct_0_x1984_13510_x576383393}

[[设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_1350858447}[中的成员编号]{style="font-family:宋体"}

[[Slot]{lang="EN-US"}]{#struct_0_x1984_13510_x564737819}

[[单板的槽位号]{style="font-family:宋体"}]{#struct_0_x1984_13510_x960736862}

[[Cpu]{lang="EN-US"}]{#struct_0_x1984_13510_412709167}

[[CPU]{lang="EN-US"}]{#struct_0_x1984_13510_x1153374774}[编号]{style="font-family:宋体"}

[[Creator]{lang="EN-US"}]{#struct_0_x1984_13510_1262544090}

[[创建]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1984_13510_1049568670}[的任务名称，括号中为创建者的进程号]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x1984_13510_1036249094}

[[OSI socket]{lang="EN-US"}]{#struct_0_x1984_13510_x1102035567}[无状态，始终显示为]{style="font-family:宋体"}[N/A]{lang="EN-US"}

[[Options]{lang="EN-US"}]{#struct_0_x1984_13510_1809132017}

[[socket]{lang="EN-US"}]{#struct_0_x1984_13510_1262609626}[的选项，]{style="font-family:宋体"}[OSI socket]{lang="EN-US"}[支持以下两种：]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[SO_FILTER]{lang="EN-US"}]{#struct_0_x1984_13510_723329867}[：设置了过滤选项]{lang="EN-US" style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N/A]{lang="EN-US"}]{#struct_0_x1984_13510_2105516080}[：没有设置选项]{lang="EN-US" style="font-family:宋体"}

[[Error]{lang="EN-US"}]{#struct_0_x1984_13510_1720778938}

[[影响]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1984_13510_x317990829}[连接的错误]{style="font-family:宋体"}

[[Receiving buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_x1984_13510_1262150874}

[[接收缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_x1984_13510_1487295408}

[[Sending buffer(cc/hiwat/lowat/state)]{lang="EN-US"}]{#struct_0_x1984_13510_x1008288069}

[[发送缓冲区信息，括号中分别为：当前使用空间、最大空间、最小空间、状态]{style="font-family:宋体"}]{#struct_0_x1984_13510_774882684}

[[Type]{lang="EN-US"}]{#struct_0_x1984_13510_1981771705}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1262216410}[使用的]{style="font-family:宋体"}[socket]{lang="EN-US"}[类型为]{style="font-family:宋体"}[2]{lang="EN-US"}[，对应无连接的、不可靠的运输层数据包协议]{style="font-family:宋体"}

[[Enabled interfaces]{lang="EN-US"}]{#struct_0_x1984_13510_1454313391}

[[接收报文时需要匹配的入接口和组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1984_13510_x1493383332}[地址信息，仅以太链路层接口上收到的报文需要匹配组播]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US" style="color:blue"}

::: {#-1775481170 .myid}
[]{#_Toc404788365}[]{#struct_0_x1984_13510_1442291407}[]{#_Toc340564366}

**IS-IS \-- IS-IS配置命令 \-- display osi statistics**

------------------------------------------------------------------------

[**[display osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_817543347}[命令用来显示]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息，包括接收报文、中继转发报文、丢弃报文和发送报文等统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_218940098}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x1984_13510_1262281946}

[**[display osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_x2041067347}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_1868594632}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display osi statistics]{lang="EN-US"}**[ \[ **slot** ]{lang="EN-US"}]{#struct_0_x1984_13510_1706829204}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_x1211679660}[模式：]{style="font-family:宋体"}

[**[display osi statistics]{lang="EN-US"}**[ \[ **chassis** ]{lang="EN-US"}]{#struct_0_x1984_13510_x1108227195}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ **slot** ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[ \[ **cpu** *cpu-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1059011050}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x351620999}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1048572626}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1262347482}

[[network-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x118258652}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1144485582}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1984_13510_x1590106743}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x821014760}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x293589498}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号[，]{style="color:black"}取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的报文统计信息之和。（分布式－独立运行模式）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_1884556444}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有成员设备的报文统计信息之和。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备]{style="font-family:宋体"}[）]{style="font-family:宋体"}

[[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x939358906}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：]{style="font-family:宋体;color:black"}[显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息[。]{style="color:black"}]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号]{style="font-family:宋体"}[。如果未指定本参数，则显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[的报文统计信息之和。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_670261249}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定成员设备上指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有成员设备所有单板的报文统计信息之和。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[[chassis]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US" style="color:black"}]{#struct_0_x1984_13510_x1805416694}[[chassis-number]{lang="EN-US"}]{.commandparameterChar}[ ]{lang="EN-US" style="color:black"}[[slot]{lang="EN-US"}]{.commandkeywordsChar}[ ]{lang="EN-US"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[：显示指定单板的]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息。]{style="font-family:宋体"}[[chassis-numbe]{lang="EN-US"}]{.commandparameterChar}[r]{lang="EN-US"}[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}[[slot-number]{lang="EN-US"}]{.commandparameterChar}[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号，取值范围请以设备的实际情况为准。如果未指定本参数，则显示所有单板的报文统计信息之和。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_x52852121}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的编号。只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1446517759}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1262937306}[显示]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display osi statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x916880670}

[Received packets:]{lang="EN-US"}

[     Total: 35]{lang="EN-US"}

[     Relay received: 35]{lang="EN-US"}

[     Relay forwarded: 35]{lang="EN-US"}

[     Invalid service slot: 0]{lang="EN-US"}

[     No matched socket: 0]{lang="EN-US"}

[     Not delivered, input socket full: 0]{lang="EN-US"}

[Sent packets:]{lang="EN-US"}

[     Total: 19]{lang="EN-US"}

[     Relay forwarded: 19]{lang="EN-US"}

[     Relay received: 19]{lang="EN-US"}

[     Failed: 0]{lang="EN-US"}

[[表1-18 ]{lang="EN-US"}[display osi statistics]{lang="EN-US"}]{#struct_0_x1984_13510_x1283140834}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1447631443}[[字段]{style="font-family:黑体"}]{#struct_0_x1984_13510_778461040}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1984_13510_1263002842}

[[Received packets]{lang="EN-US"}]{#struct_0_x1984_13510_x849789690}

[[Total]{lang="EN-US"}]{#struct_0_x1984_13510_x4117779}

[[从链路层接收的报文总数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x7509890}

[[Relay received]{lang="EN-US"}]{#struct_0_x1984_13510_1694909454}

[[业务板从其他板中继接收的入方向报文总数，该计数不计入]{style="font-family:宋体"}[Total]{lang="EN-US"}]{#struct_0_x1984_13510_1099382293}[中]{style="font-family:宋体"}

[[Relay forwarded]{lang="EN-US"}]{#struct_0_x1984_13510_1262413019}

[[中继转发给业务板的入方向报文数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1673154280}

[[Invalid service slot]{lang="EN-US"}]{#struct_0_x1984_13510_x2036794824}

[[因为业务板不可用而被丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1252705532}

[[No matched socket]{lang="EN-US"}]{#struct_0_x1984_13510_x1327560077}

[[因为未匹配报文入接口、或者未匹配]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1984_13510_1262478555}[地址、或者不满足连接的过滤条件而被丢弃的报文数]{style="font-family:宋体"}

[[Not delivered, input socket full]{lang="EN-US"}]{#struct_0_x1984_13510_x55660949}

[[因为]{style="font-family:宋体"}[socket]{lang="EN-US"}]{#struct_0_x1984_13510_x1109187824}[接收缓冲区已满而没有向上层传送的报文数]{style="font-family:宋体"}

[[Sent packets]{lang="EN-US"}]{#struct_0_x1984_13510_1203377415}

[[Total]{lang="EN-US"}]{#struct_0_x1984_13510_718963167}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1262544091}[通过]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接发送的报文总数]{style="font-family:宋体"}

[[Relay forwarded]{lang="EN-US"}]{#struct_0_x1984_13510_1049503134}

[[中继转发给出接口所在板的出方向报文数，该计数不计入]{style="font-family:宋体"}[Total]{lang="EN-US"}]{#struct_0_x1984_13510_303025815}[中]{style="font-family:宋体"}

[[Relay received]{lang="EN-US"}]{#struct_0_x1984_13510_x1133530838}

[[出接口所在板从其他板中继接收的出方向报文总数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x631022980}

[[Failed]{lang="EN-US"}]{#struct_0_x1984_13510_1262609627}

[[发送失败的报文个数]{style="font-family:宋体"}]{#struct_0_x1984_13510_723264331}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1744334601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}[ osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_1128427916}

::: {#1382834416 .myid}
[]{#_Toc404788366}[]{#struct_0_x1984_13510_187043352}[]{#_Toc353884883}

**IS-IS \-- IS-IS配置命令 \-- domain-authentication send-only**

------------------------------------------------------------------------

[**[domain-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_415869216}[命令用来配置对收到的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）忽略认证信息检查。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ domain-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_186453525}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_186519061}

[**[domain-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_186584597}

[**[undo domain-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_186650133}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1064421315}

[[如果配置了路由域验证方式和验证密码，对收到的报文执行认证信息检查。]{style="font-family:宋体"}]{#struct_0_x1984_13510_186715669}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_186781205}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_1858485245}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_186846741}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_186912277}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_186977813}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_187043349}

[[配置路由域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x1922782939}[报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中，并对收到的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[报文进行验证密码的检查]{style="font-family:宋体"}[。当需要更改密码时由于密码不匹配可能导致业务发生中断。通过命令配置对]{style="font-family:宋体"}[收到的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[报文]{style="font-family:宋体"}[忽略认证信息检查可保证业务不中断，报文正常接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_186453526}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_186519062}[对收到报文忽略认证信息检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_186584598}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] domain-authentication send-only]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1603574227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication]{lang="EN-US"}**]{#struct_0_x1984_13510_186650134}**[ send-only]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_186715670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_689770319}
:::

::: {#-1067944521 .myid}
[]{#_Toc404788367}[]{#struct_0_x1984_13510_1507180224}

**IS-IS \-- IS-IS配置命令 \-- domain-authentication-mode**

------------------------------------------------------------------------

[**[domain-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_140452812}[命令用来配置路由域验证方式和验证密码。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **domain-authentication-mode**]{lang="EN-US"}]{#struct_0_x1984_13510_x1902917603}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262150875}

[**[domain-authentication-mode ]{lang="EN-US"}**[{ **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } \[ **ip** \| **osi** \]]{lang="EN-US"}]{#struct_0_x1984_13510_186781206}

[**[undo]{lang="FR"}**]{#struct_0_x1984_13510_x1789036655}[ **domain-authentication-mode**]{lang="FR"}[]{#_Hlt9932878}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x725173405}

[[系统没有配置路由域验证方式和验证密码。]{style="font-family:宋体"}]{#struct_0_x1984_13510_197615269}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x992272873}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_1173634118}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262216411}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_1454378927}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_1611975182}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1616551466}

[**[gca]{lang="FR"}**]{#struct_0_x1984_13510_186912278}[：]{style="font-family:宋体"}[GCA]{lang="FR"}[验证模式]{style="font-family:
宋体"}[（]{style="font-family:宋体"}[Generic Cryptographic Authentication]{lang="FR"}[）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[key-id]{lang="FR"}*]{#struct_0_x1984_13510_186977814}[：]{style="font-family:宋体"}[唯一标识一个认证项]{style="font-family:宋体"}[（]{style="font-family:宋体"}[SA]{lang="FR"}[），]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。发送方将]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[放入认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中，接收方根据报文中提取的]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[选择]{style="font-family:宋体"}[SA]{lang="EN-US"}[对报文进行认证。]{style="font-family:宋体"}

[**[hmac-sha-1]{lang="EN-US"}**]{#struct_0_x1984_13510_187043350}[：支持]{style="font-family:宋体"}[HMAC-SHA-1]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-224]{lang="EN-US"}**]{#struct_0_x1984_13510_415869214}[：支持]{style="font-family:宋体"}[HMAC-SHA-224]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-256]{lang="EN-US"}**]{#struct_0_x1984_13510_186453523}[：支持]{style="font-family:宋体"}[HMAC-SHA-256]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-384]{lang="EN-US"}**]{#struct_0_x1984_13510_186519059}[：支持]{style="font-family:宋体"}[HMAC-SHA-384]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-512]{lang="EN-US"}**]{#struct_0_x1984_13510_186584595}[：支持]{style="font-family:宋体"}[HMAC-SHA-512]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[md5]{lang="FR"}**]{#struct_0_x1984_13510_365589464}[：]{style="font-family:宋体"}[MD5]{lang="FR"}[验证模式]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[simple]{lang="FR"}**]{#struct_0_x1984_13510_1709660773}[：]{style="font-family:宋体"}[简单验证模式。]{style="font-family:宋体"}

[**[cipher]{lang="FR"}**]{#struct_0_x1984_13510_x720618457}[：]{style="font-family:宋体"}[表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="FR"}*]{#struct_0_x1984_13510_x1880512906}[：]{style="font-family:宋体"}[表示设置的密文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[33]{lang="FR"}[～]{style="font-family:宋体"}[53]{lang="FR"}[个字符的字符串。]{style="font-family:宋体"}

[**[plain]{lang="FR"}**]{#struct_0_x1984_13510_1262281947}[：]{style="font-family:宋体"}[表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="FR"}*]{#struct_0_x1984_13510_x2041132883}[：]{style="font-family:宋体"}[表示设置的明文密码]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[16]{lang="FR"}[个字符的字符串。]{style="font-family:宋体"}

[**[ip]{lang="FR"}**]{#struct_0_x1984_13510_x1262347618}[：]{style="font-family:宋体"}[检查]{style="font-family:宋体"}[LSP]{lang="FR"}[中]{style="font-family:宋体"}[IP]{lang="FR"}[的相应字段的配置内容。]{style="font-family:宋体"}

[**[osi]{lang="EN-US"}**]{#struct_0_x1984_13510_x1951881688}[：检查]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1297547544}

[[配置路由域验证方式和验证密码后，验证密码将按照设定的方式插入到发送的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_1273585641}[报文（包括]{style="font-family:宋体"}[LSP]{lang="EN-US"}[、]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[、]{style="font-family:宋体"}[PSNP]{lang="EN-US"}[）中并对收到的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[报文进行验证密码的检查。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_782275121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有骨干层（]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1251635663}[Level-2]{lang="EN-US"}[）路由器必须配置相同的验证方式和验证密码。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_1262347483}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[参数，将检查]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x118324188}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[认证密码选用]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1971739472}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[不受实际的网络环境影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x570342289}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_204925803}[配置路由域采用简单明文验证模式，认证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1421925354}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] domain-authentication-mode simple plain 123456]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1886858003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_1078073001}

[]{#struct_0_x1984_13510_186715667}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-authentication send-only]{lang="EN-US"}**]{#_Toc349293880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_1262937307}**[isis]{lang="EN-US"}[ authentication-mode]{lang="EN-US"}**
:::

::::: {#1745414037 .myid}
[]{#_Toc404788368}[]{#struct_0_x1984_13510_x916815134}[]{#_Toc303839439}

**IS-IS \-- IS-IS配置命令 \-- fast-reroute**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x509792013}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x39581619}
:::

[ ]{lang="EN-US"}

[**[fast-reroute]{lang="EN-US"}**]{#struct_0_x1984_13510_x1196355610}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持快速重路由功能。]{style="font-family:宋体"}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_x1984_13510_1898505763}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1702802901}

[**[fast-reroute]{lang="EN-US"}**[ { **lfa** \| **route-policy** *route-policy-name* }]{lang="EN-US"}]{#struct_0_x1984_13510_1263002843}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_x1984_13510_x849855226}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1940474877}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1695536616}[支持快速重路由功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2073345730}

[[IS-IS IPv4]{lang="FR"}]{#struct_0_x1984_13510_x929877312}[单播地址族]{style="font-family:宋体"}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1252756800}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_x414553842}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_1262413016}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1672564456}

[**[lfa]{lang="FR"}**]{#struct_0_x1984_13510_1826230754}[：]{style="font-family:宋体"}[为所有路由通过]{style="font-family:宋体"}[LFA]{lang="FR"}[（]{style="font-family:宋体"}[Loop Free Alternate]{lang="FR"}[）]{style="font-family:宋体"}[算法选取备份下一跳信息]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="FR"}**]{#struct_0_x1984_13510_x335989723}[ *route-policy-name*]{lang="FR"}[：]{style="font-family:宋体"}[指定路由策略名]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[route-policy-name]{lang="FR"}*[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[63]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。为通过策略的路由指定备份下一跳信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2138172621}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_361783760}[支持快速重路由功能不能与]{style="font-family:宋体"}[IS-IS]{lang="FR"}[的]{style="font-family:宋体"}[BFD]{lang="FR"}[功能同时使用]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[否则可能导致快速重路由功能失效。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x792105003}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1755544718}[为所有路由]{style="font-family:宋体"}[通过]{style="font-family:
宋体"}[LFA]{lang="EN-US"}[算法]{style="font-family:宋体"}[选取备份下一跳信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1521125992}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\]]{lang="EN-US"}[ address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] fast-reroute lfa]{lang="EN-US"}
:::::

::: {#1247311243 .myid}
[]{#_Toc303839440}[]{#_Toc252200750}[]{#_Toc163546253}[]{#_Toc131667486}[]{#_Toc404788369}[]{#struct_0_x1984_13510_1922149223}[]{#_Toc310604336}[]{#_Toc252200748}[]{#_Toc370737431}[]{#_Toc370737432}[]{#_Toc370737433}

**IS-IS \-- IS-IS配置命令 \-- filter-policy export**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_x1984_13510_x1108456142}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[对引入的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_x1984_13510_x211300456}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_635490881}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_x1984_13510_x799363830}

[**[undo]{lang="EN-US"}**[ **filter-policy** **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1816410097}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262544088}

[[没有配置该过滤功能。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1050092957}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x179029026}

[[IS-IS IPv4]{lang="FR"}]{#struct_0_x1984_13510_x1193744342}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="FR"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1896930694}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_1465866127}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_796069480}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x292222068}

[*[acl-number]{lang="FR"}*]{#struct_0_x1984_13510_1262609624}[：]{style="font-family:宋体"}[指定访问控制列表序号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="FR"}[～]{style="font-family:宋体"}[3999]{lang="FR"}[，]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[ACL]{lang="FR"}[对引入的路由信息进行过滤。]{style="font-family:宋体"}

[**[prefix-list]{lang="FR"}**]{#struct_0_x1984_13510_723198795}[ *prefix-list-name*]{lang="FR"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv4]{lang="FR"}[地址前缀列表名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[基于目的地址对引入的路由信息进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_1927257770}[：指定路由策略名，基于路由策略对引入的路由信息进行过滤。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_x1984_13510_x878854264}[：路由协议名称，指定过滤从哪种路由协议引入的路由信息。目前可包括：]{style="font-family:宋体"}**[bgp]{lang="EN-US"}[、]{style="font-family:宋体"}[direct]{lang="EN-US"}[、]{style="font-family:宋体"}[isis]{lang="EN-US"}[、]{style="font-family:宋体"}[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。如果不指定该参数，将对所有引入的路由进行过滤。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x545335955}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时，该参数可选，若未指定，缺省进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_542094134}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1984_13510_x717515156}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1040306095}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1262150872}[使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1487426480}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\]]{lang="EN-US"}[ address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] filter-policy 2000 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x590520276}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1855117814}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis 1\]]{lang="EN-US"}[ address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] filter-policy 3000 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x383803250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isis route]{lang="EN-US"}**]{#struct_0_x1984_13510_1262216408}
:::

::: {#632247711 .myid}
[]{#_Toc404788370}[]{#struct_0_x1984_13510_1453789104}[]{#_Toc310604337}[]{#_Toc17101066}

**IS-IS \-- IS-IS配置命令 \-- filter-policy import**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_x1984_13510_519984365}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[对接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_x1984_13510_1002563691}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_893038261}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]{lang="EN-US"}]{#struct_0_x1984_13510_798103610}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_x1984_13510_1907902242}

[[【]{style="font-family:黑体"}]{#struct_0_x1984_13510_x217695855}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有配置该过滤功能。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1262281944}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2041198419}

[[IS-IS IPv4]{lang="FR"}]{#struct_0_x1984_13510_905895010}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="FR"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x370654206}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1504695597}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x959026505}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_372323843}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x1984_13510_697290742}[：指定访问控制列表序号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[，基于]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1984_13510_462970670}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名，基于目的地址对接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_1262347480}[：指定路由策略名，基于路由策略对]{style="font-family:宋体"}[接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x118389724}

[[当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1984_13510_752091771}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1429382822}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x554361541}[基于编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_621641128}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\]]{lang="EN-US"}[ address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] filter-policy 2000 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x928419191}[基于编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由是否加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[加入]{style="font-family:宋体"}[IP]{lang="EN-US"}[路由表。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1262937304}

[\[Sysname\] acl number 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis 1\]]{lang="EN-US"}[ address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] filter-policy 3000 import]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x917011742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip routing-table]{lang="EN-US"}**]{#struct_0_x1984_13510_714104090}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1202717567 .myid}
[]{#_Toc404788371}[]{#struct_0_x1984_13510_x120706480}

**IS-IS \-- IS-IS配置命令 \-- flash-flood**

------------------------------------------------------------------------

[**[flash-flood]{lang="EN-US"}**]{#struct_0_x1984_13510_1329928269}[命令用来使能]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能。]{style="font-family:宋体"}

[**[undo flash-flood]{lang="EN-US"}**]{#struct_0_x1984_13510_1739970451}[命令用来关闭]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1263002840}

[**[flash-flood]{lang="EN-US"}**[ \[ **flood-count** *flooding-count* \| **max-timer-interval** *flooding-interval* \| \[ **level-1** \| **level-2** \] \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_x849920762}

[**[undo flash-flood]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1154412115}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1847975100}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x967187234}[快速扩散功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2038124797}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_739653076}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1350353270}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1423059062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1262413017}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1672498920}

[**[flood-count]{lang="EN-US"}***[ flooding-count]{lang="EN-US"}*]{#struct_0_x1984_13510_x526504568}[：在]{style="font-family:宋体"}[SPF]{lang="EN-US"}[重新计算前快速扩散]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[max-timer-interval]{lang="EN-US"}***[ flooding-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_258551506}[：在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散之前的等待时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[，单位为毫秒，缺省值为]{style="font-family:宋体"}[10]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x707677668}[：使能在]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**[级别的快速扩散功能。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1164161162}[：使能在]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[级别的快速扩散功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x384953100}

[[如果不指定级别，将同时使能]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1803866292}[和]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[级别的快速扩散功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262478553}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x55792021}[使能]{style="font-family:宋体"}[LSP]{lang="EN-US"}[快速扩散功能，配置发送个数]{style="font-family:宋体"}[10]{lang="EN-US"}[个，发送延时]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_904786668}

[\[Sysname\] isis 1]{lang="EN-US"}

[[\[Sysname-isis-1\] flash-flood flood-count 10 max-timer-interval 100]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_120694460}
:::

::::: {#63544256 .myid}
[]{#_Toc303839444}[]{#_Toc404788372}[]{#struct_0_x1984_13510_1506965467}[]{#_Toc303839441}[]{#_Toc163546251}[]{#_Toc50204095}[]{#_Toc33866094}[]{#_Toc17101067}[]{#_Toc302996860}[]{#_Toc252200747}[]{#_Toc199911156}[]{#_Toc193268606}[]{#_Toc193268506}[]{#_Toc193260336}[]{#_Toc131910356}[]{#_Toc132011562}

**IS-IS \-- IS-IS配置命令 \-- graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1299737039}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1262544089}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_1050027421}[命令用来使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_1797453014}[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_357235288}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x679144095}

[**[undo ]{lang="FR"}[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x291777442}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1617009375}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1118647656}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262609625}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_723133259}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x819731341}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1243718111}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1588809791}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2110634443}

[[IS-IS GR]{lang="EN-US"}]{#struct_0_x1984_13510_x217819324}[特性与]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[和]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1402667872}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1262150873}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1487492016}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_2128907703}

[[\[Sysname-isis-1\] graceful-restart]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_x1173442181}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_237946554}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_x1984_13510_x1760983337}
:::::

::::: {#1056335496 .myid}
[]{#_Toc404788373}[]{#struct_0_x1984_13510_2096343391}[]{#_Toc303839443}[]{#_Toc328662275}[]{#_Toc328662276}[]{#_Toc328662277}[]{#_Toc328662278}[]{#_Toc328662279}[]{#_Toc328662280}[]{#_Toc328662281}[]{#_Toc328662282}[]{#_Toc328662283}[]{#_Toc328662284}[]{#_Toc328662285}[]{#_Toc328662286}[]{#_Toc328662287}[]{#_Toc328662288}[]{#_Toc328662289}[]{#_Toc328662290}[]{#_Toc328662291}[]{#_Toc328662292}[]{#_Toc328662293}[]{#_Toc328662294}[]{#_Toc328662295}[]{#_Toc328662296}[]{#_Toc328662297}[]{#_Toc328662298}[]{#_Toc328662299}[]{#_Toc328662300}

**IS-IS \-- IS-IS配置命令 \-- graceful-restart suppress-sa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x1358303809}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1262216409}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_x1984_13510_1453854640}[命令用来配置重启时抑制]{style="font-family:
宋体"}[SA]{lang="EN-US"}[（]{style="font-family:宋体"}[Suppress-Advertisement]{lang="EN-US"}[）位置位。]{style="font-family:宋体"}**[undo graceful-restart suppress-sa]{lang="EN-US"}**[命令用来取消重启时抑制]{style="font-family:
宋体"}[SA]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x976465503}

[**[graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_x1984_13510_x598515632}

[**[undo graceful-restart suppress-sa]{lang="EN-US"}**]{#struct_0_x1984_13510_x1632599081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1250307473}

[[SA]{lang="EN-US"}]{#struct_0_x1984_13510_1659172086}[位处于置位状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_799095731}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_1262281945}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2041263955}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x723753224}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1212784823}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1206612314}

[[SA]{lang="EN-US"}]{#struct_0_x1984_13510_x104943953}[表示抑制邻接标志位，其主要目的是为了避免出现路由黑洞，例如在启动或者重启时没有保留本地转发表，此时如果]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[将报文送到设备来进行转发将会造成严重的丢包现象，在这种情况下]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中必须将]{style="font-family:宋体"}[SA]{lang="EN-US"}[位置]{style="font-family:宋体"}[1]{lang="EN-US"}[，而]{style="font-family:宋体"}[GR Helper]{lang="EN-US"}[接收到这种]{style="font-family:宋体"}[SA]{lang="EN-US"}[位被置]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文后就不会将发送该]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的]{style="font-family:宋体"}[GR Restarter]{lang="EN-US"}[放入]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散出去。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2146991401}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1341674841}[配置重启时对]{style="font-family:宋体"}[SA]{lang="EN-US"}[位进行抑制。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1262347481}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_x118455260}

[[\[Sysname-isis-1\] graceful-restart suppress-sa]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1149513844}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x340078956}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x298732227}
:::::

::::: {#-725244767 .myid}
[]{#_Toc404788374}[]{#struct_0_x1984_13510_x1266467564}

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t1**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x628015161}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1409572192}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart t1]{lang="EN-US"}**]{#struct_0_x1984_13510_1262937305}[命令用来配置]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo graceful-restart t1]{lang="EN-US"}**]{#struct_0_x1984_13510_x916946206}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x909263816}

[**[graceful-restart ]{lang="EN-US"}[t1]{lang="EN-US"}**[ *seconds* **count** *count*]{lang="EN-US"}]{#struct_0_x1984_13510_722172964}

[**[undo graceful-restart t1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1777519868}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1521106429}

[[T1]{lang="EN-US"}]{#struct_0_x1984_13510_1127519190}[定时器的超时值为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒，超时次数为]{style="font-family:宋体"}[10]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1289899193}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_1263002841}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x849986298}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_x1518512614}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_x912279987}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x252050896}

[*[seconds]{lang="FR"}*]{#struct_0_x1984_13510_x1221529188}[：]{style="font-family:宋体"}[T1]{lang="SV"}[定时器的超时值，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[3]{lang="FR"}[～]{style="font-family:宋体"}[10]{lang="SV"}[，]{style="font-family:
宋体"}[单位为秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_x1984_13510_x576776219}[：]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时次数，取值范围为]{style="font-family:宋体"}[1]{lang="DE"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x198590910}

[[T1]{lang="EN-US"}]{#struct_0_x1984_13510_1262413014}[定时器用来控制发送带有]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Restart TLV]{lang="EN-US"}[的次数。重启路由器发送带有]{style="font-family:宋体"}[RR]{lang="EN-US"}[标志位的]{style="font-family:宋体"}[Restart TLV]{lang="EN-US"}[，如果在超时时间内收到对端回复的带有]{style="font-family:宋体"}[RA]{lang="EN-US"}[标志的]{style="font-family:宋体"}[Restart TLV]{lang="EN-US"}[，才能正常进入]{style="font-family:宋体"}[GR]{lang="EN-US"}[流程；否则]{style="font-family:宋体"}[GR]{lang="EN-US"}[流程失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1672433384}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1504684784}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[T1]{lang="EN-US"}[定时器超时值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，超时次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_222623259}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_x192671652}

[[\[Sysname-isis-1\] graceful-restart t1 5 count 5]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_248689103}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_942268039}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_1855082813}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_1262478550}**[ t2]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart ]{lang="EN-US"}**]{#struct_0_x1984_13510_x55988629}**[t3]{lang="EN-US"}**
:::::

::::: {#2003638588 .myid}
[]{#_Toc404788375}[]{#struct_0_x1984_13510_x1242482829}

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t2**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x274607356}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1274394165}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart t2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1546167577}[命令用来配置]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo graceful-restart t2]{lang="EN-US"}**]{#struct_0_x1984_13510_745480290}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_87303005}

[**[graceful-restart ]{lang="EN-US"}[t2]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x1984_13510_1262544086}

[**[undo graceful-restart t2]{lang="EN-US"}**]{#struct_0_x1984_13510_1049437597}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1501297746}

[[T2]{lang="EN-US"}]{#struct_0_x1984_13510_892305920}[定时器的超时值为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1090165028}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_x539143555}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1800885925}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_1536322027}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_1262609622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_723067723}

[*[seconds]{lang="FR"}*]{#struct_0_x1984_13510_349084831}[：]{style="font-family:宋体"}[T2]{lang="SV"}[定时器的超时值，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[30]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="SV"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_337881578}

[[T2]{lang="FR"}]{#struct_0_x1984_13510_1743489254}[定时器用来控制]{style="font-family:宋体"}[LSDB]{lang="FR"}[同步时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}[每个]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[都有一个]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，对于]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[路由器来说，就需要有两个]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器，一个为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="FR"}[定时器，另外一个为]{style="font-family:
宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:
宋体"}[T2]{lang="FR"}[定时器。如果]{style="font-family:宋体"}[Level-1]{lang="FR"}[和]{style="font-family:宋体"}[Level-2]{lang="FR"}[的]{style="font-family:宋体"}[T2]{lang="FR"}[定时器都超时后]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[LSDB]{lang="FR"}[同步还没有完成，]{style="font-family:宋体"}[则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2023513281}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x563575477}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[T2]{lang="EN-US"}[定时器超时值为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_694970416}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1262150870}

[[\[Sysname-isis-1\] graceful-restart t]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_1487557552}[2]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[ 5]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[0]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x189213539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x1854746710}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x1489953177}**[ t1]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart ]{lang="EN-US"}**]{#struct_0_x1984_13510_x207911891}**[t3]{lang="EN-US"}**
:::::

::::: {#437554647 .myid}
[]{#_Toc404788376}[]{#struct_0_x1984_13510_860448363}

**IS-IS \-- IS-IS配置命令 \-- graceful-restart t3**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1489881204}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1262216406}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart t3]{lang="EN-US"}**]{#struct_0_x1984_13510_1454444464}[命令用来配置]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器。]{style="font-family:宋体"}

[**[undo graceful-restart t3]{lang="EN-US"}**]{#struct_0_x1984_13510_x1108061665}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_43515565}

[**[graceful-restart ]{lang="EN-US"}[t3 ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_x1731831534}

[**[undo graceful-restart t3]{lang="EN-US"}**]{#struct_0_x1984_13510_x1631441127}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x279004702}

[[T3]{lang="EN-US"}]{#struct_0_x1984_13510_1558959111}[定时器的超时值为]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1068258341}

[[IS-IS]{lang="FR"}]{#struct_0_x1984_13510_1262281942}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2041329491}

[[network-admin]{lang="FR"}]{#struct_0_x1984_13510_x1327818373}

[[mdc-admin]{lang="FR"}]{#struct_0_x1984_13510_x626559234}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1273292116}

[*[seconds]{lang="FR"}*]{#struct_0_x1984_13510_2084026457}[：]{style="font-family:宋体"}[T3]{lang="SV"}[定时器的超时值，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[300]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="SV"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_172839980}

[[T3]{lang="EN-US"}]{#struct_0_x1984_13510_267144565}[定时器用来控制路由器的重启时间间隔。重启时间间隔在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello PDU]{lang="EN-US"}[中设置为保持时间，这样在该路由器重启的时间内邻居不会断掉与其的邻接关系。如果]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器超时后]{style="font-family:宋体"}[GR]{lang="EN-US"}[还没有完成，则]{style="font-family:宋体"}[GR]{lang="EN-US"}[失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262347478}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x117865429}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[T3]{lang="EN-US"}[定时器超时值为]{style="font-family:宋体"}[500]{lang="EN-US"}[秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_963326196}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_x1192313269}

[[\[Sysname-isis-1\] graceful-restart t]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_x712641140}[3]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[ 5]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}[00]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x10592697}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x2139694344}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_x887671869}**[ t1]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[graceful-restart ]{lang="EN-US"}**]{#struct_0_x1984_13510_1262937302}**[t2]{lang="EN-US"}**
:::::

::: {#1224972849 .myid}
[]{#_Toc404788377}[]{#struct_0_x1984_13510_x435189140}[]{#_Toc366163926}[]{#_Toc364753108}

**IS-IS \-- IS-IS配置命令 \-- ignore-att**

------------------------------------------------------------------------

[**[ignore-att]{lang="EN-US"}**]{#struct_0_x1984_13510_1070338633}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[不采用]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位计算缺省路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ignore-att]{lang="EN-US"}**]{#struct_0_x1984_13510_x1626830235}[命令用来取消该配置]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_497724373}

[**[ignore-att]{lang="EN-US"}**]{#struct_0_x1984_13510_1022268644}

[**[undo ignore-att]{lang="EN-US"}**]{#struct_0_x1984_13510_x1626830236}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_901008900}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1634577686}[采用]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位计算缺省路由]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x760905938}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1626830237}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x665075041}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_269444962}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x1984_13510_x1626830238}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x261790514}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_421405032}[配置不采用]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位计算缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1626830231}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] ignore-att]{lang="EN-US"}
:::

::: {#29262825 .myid}
[]{#_Toc404788378}[]{#struct_0_x1984_13510_x916618526}

**IS-IS \-- IS-IS配置命令 \-- import-route**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_x1984_13510_1014527925}[命令用来从其它路由协议或其它]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程引入路由信息。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_x1984_13510_533166363}[命令用来取消从其它路由协议或其它]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程引入路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1039566475}

[**[import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \| **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| **cost-type** { **external** \| **internal** } \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **route-policy** *route-policy-name* \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_x1356568605}

[**[undo import-route]{lang="EN-US"}**[ *protocol* \[ *process-id* \| **all-processes** \]]{lang="EN-US"}]{#struct_0_x1984_13510_1263002838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x850445053}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x76960891}[不引入其它协议的路由信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1013678930}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x1080173332}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1956919913}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1433466724}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1872024733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1975049992}

[*[protocol]{lang="EN-US"}*]{#struct_0_x1984_13510_1262413015}[：指定引入的路由协议，可以是]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x1672367848}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[**[all-processes]{lang="EN-US"}**]{#struct_0_x1984_13510_1434897792}[：引入指定路由协议所有进程的路由，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[时可以指定该参数。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_x1984_13510_x463620535}[：允许引入]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[时该参数可选。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_x1984_13510_2090213763}[：]{style="font-family:宋体"}[在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[路由时不会包含使能了]{style="font-family:宋体"}[该]{style="font-family:宋体"}[协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}**[ *cost*]{lang="EN-US"}]{#struct_0_x1984_13510_610856467}[：引入的路由的路径开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4261412864]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[narrow]{lang="EN-US"}**]{#struct_0_x1984_13510_1262478551}[、]{lang="EN-US" style="font-family:宋体"}**[narrow-compatible]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:
宋体"}**[compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_x1984_13510_x55923093}[或]{lang="EN-US" style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[4261412864]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[cost-type ]{lang="EN-US"}**[{ **external** \| **internal** }]{lang="EN-US"}]{#struct_0_x1984_13510_1073738213}[：表示路径开销类型：]{style="font-family:宋体"}**[internal]{lang="EN-US"}**[表示内部路由；]{style="font-family:宋体"}**[external]{lang="EN-US"}**[表示外部路由，配置路径开销类型为]{style="font-family:宋体"}**[external]{lang="EN-US"}**[后，通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发布路由时路径开销会在配置的]{style="font-family:宋体"}[cost]{lang="EN-US"}[值的基础上加上]{style="font-family:宋体"}[64]{lang="EN-US"}[，从而保证内部路由优于外部路由。缺省情况下为]{style="font-family:宋体"}**[external]{lang="EN-US"}**[类型。只有当开销类型为]{style="font-family:宋体"}**[narrow]{lang="EN-US"}**[、]{style="font-family:宋体"}**[narrow-compatible]{lang="EN-US"}**[或者]{style="font-family:宋体"}**[compatible]{lang="EN-US"}**[时，该参数有效。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_218337231}[：引入路由到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的路由表中。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1042644713}[：同时引入路由到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由表中。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1737044593}[：引入路由到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由表中。如果不指定引入的级别，默认为引入路由到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[]{#struct_0_x1984_13510_283132583}[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#_Hlt24449614}[：路由策略名称，]{style="font-family:宋体"}[只有满足指定路由策略匹配条件的路由才被引入。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_x534396687}[：为引入路由配置]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262544087}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1049372061}[将所有引入路由域中的路由当作外部路由，它们描述了应该如何选择到路由域以外目的地的路由。]{style="font-family:宋体"}

[[真正生效的开销值受当前开销类型的影响。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x102409535}[当路径开销值类型为]{style="font-family:
宋体"}**[narrow]{lang="EN-US"}**[、]{style="font-family:宋体"}**[narrow-compatible]{lang="EN-US"}**[或]{style="font-family:宋体"}**[compatible]{lang="EN-US"}**[时，生效的开销值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，超过]{style="font-family:宋体"}[63]{lang="EN-US"}[的也取值为]{style="font-family:宋体"}[63]{lang="EN-US"}[；]{style="font-family:宋体"}[当路径开销值类型为]{style="font-family:宋体"}**[wide]{lang="EN-US"}**[或]{style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时]{style="font-family:宋体"}[，配置值即为生效值。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x123008298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令不能引入缺省路由。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x12409533}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route bgp]{lang="EN-US"}**]{#struct_0_x1984_13510_1834984100}[表示只引入]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由]{lang="EN-US" style="font-family:宋体"}[；]{lang="EN-US" style="font-family:
宋体"}**[import-route bgp allow-ibgp]{lang="EN-US"}**[表示将]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由也引入]{lang="EN-US" style="font-family:宋体"}[，容易引起路由环路，]{lang="EN-US" style="font-family:宋体"}[请慎用]{lang="EN-US" style="font-family:
宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只能引入路由表中状态为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_x1984_13510_1537556872}[的路由，是否为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[状态可以通过]{lang="EN-US" style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**[ **protocol**]{lang="EN-US"}[命令来查看。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo import-route]{lang="EN-US"}**[ *protocol* **all-processes**]{lang="EN-US"}]{#struct_0_x1984_13510_1937255230}[命令只能取消]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**[ *protocol* **all-processes**]{lang="EN-US"}[命令的配置，不能取消]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**[ *protocol* *process-id*]{lang="EN-US"}[命令的配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262609623}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_723002187}[引入静态路由，]{style="font-family:宋体"}[cost]{lang="EN-US"}[值为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x216830999}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] import-route static cost 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x311813383}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route limit]{lang="EN-US"}**]{#struct_0_x1984_13510_x369593000}
:::

::: {#1163395432 .myid}
[]{#_Toc303839445}[]{#_Toc42309484}[]{#_Toc404788379}[]{#struct_0_x1984_13510_15630070}[]{#_Toc310604339}

**IS-IS \-- IS-IS配置命令 \-- import-route isis level-1 into level-2**

------------------------------------------------------------------------

[**[import-route isis level-1 into level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1164211276}[命令用来]{style="font-family:宋体"}[配置将]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由信息引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo import-route isis level-1 into level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1262150871}[命令用来取消此功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1487623088}

[**[import-route isis level-1 into level-2]{lang="EN-US"}**[ \[ **filter-policy** { *acl-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_577962653}

[**[undo import-route isis level-1 into level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1836572777}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2123627945}

[[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_2011411210}[区域的路由信息]{style="font-family:宋体"}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域发布。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x806058866}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x421685932}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262216407}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1454510000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_441918574}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x486257266}

[**[filter-policy]{lang="EN-US"}**]{#struct_0_x1984_13510_x1782799853}[：过滤策略。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x1984_13510_x170437694}[：指定访问控制列表序号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[，过滤从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由信息。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x687519347}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名，基于目的地址对从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由信息进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x1477765999}[：指定路由策略名，基于路由策略从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由信息进行过滤。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_1262281943}[：为引入路由配置]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2041395027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要通过路由策略对从]{lang="EN-US" style="font-family:宋体"}[Level-]{lang="EN-US"}]{#struct_0_x1984_13510_332514716}[1]{lang="EN-US"}[区域引入到]{lang="EN-US" style="font-family:宋体"}[Level-]{lang="EN-US"}[2]{lang="EN-US"}[区域的路由信息进行过滤，必须在]{lang="EN-US" style="font-family:宋体"}**[import-route isis level-]{lang="EN-US"}[1]{lang="EN-US"}[ into level-]{lang="EN-US"}[2]{lang="EN-US"}**[命令中]{lang="EN-US" style="font-family:宋体"}[同时指定要应用的路由策略，否则路由过滤将不会生效；其它路由策略，如在接收或引入路由时指定的路由策略对路由渗透无效。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了过滤策略，则只有通过过滤的路由才能够被发布到]{style="font-family:宋体"}]{#struct_0_x1984_13510_x627788118}[Level-2]{lang="EN-US"}[区域中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1675188655}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1465688458}[配置路由器从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_25996973}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] import-route isis level-1 into level-2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1557708076}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x1984_13510_1262347479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route isis level-1 into level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x117930965}
:::

::: {#1163494859 .myid}
[]{#_Toc404788380}[]{#struct_0_x1984_13510_1324929788}

**IS-IS \-- IS-IS配置命令 \-- import-route isis level-2 into level-1**

------------------------------------------------------------------------

[**[import-route isis level-2 into level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_862604340}[命令用来]{style="font-family:宋体"}[配置将]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由信息引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[undo import-route isis level-2 into level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x85742791}[命令用来取消此功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x456146357}

[**[import-route isis level-2 into level-1 ]{lang="EN-US"}**[\[ **filter-policy** { ]{lang="EN-US"}*[acl-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **prefix-list** ]{lang="EN-US"}*[prefix-list-name ]{lang="EN-US"}*[\| **route-policy** *route-policy-name* } \| **tag** ]{lang="EN-US"}*[tag]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \*]{lang="EN-US"}]{#struct_0_x1984_13510_x46975391}

[**[undo import-route ]{lang="EN-US"}**]{#struct_0_x1984_13510_x697401543}**[isis]{lang="EN-US"}[ level-2 into level-1]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1262937303}

[[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_x916552990}[区域的路由信息不]{style="font-family:宋体"}[向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域发布。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1489496401}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x7380956}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x450249525}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x881450462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1773583120}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1687418957}

[**[filter-policy]{lang="EN-US"}**]{#struct_0_x1984_13510_1263002839}[：过滤策略。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x1984_13510_x850510589}[：指定访问控制列表序号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[，过滤从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x2024738190}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名，基于目的地址对从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x306791081}[：指定路由策略名，基于路由策略从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由信息进行过滤]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[route-]{lang="EN-US"}[policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_x1682348504}[：为引入路由配置]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1067456398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要通过路由策略对从]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}]{#struct_0_x1984_13510_951127793}[区域引入到]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由信息进行过滤，必须在]{lang="EN-US" style="font-family:宋体"}**[import-route isis level-2 into level-1]{lang="EN-US"}**[命令中]{lang="EN-US" style="font-family:宋体"}[同时指定要应用的路由策略，否则路由过滤将不会生效；其它路由策略，如在接收或引入路由时指定的路由策略对路由渗透无效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了过滤策略，则只有通过过滤的路由才能够被发布到]{style="font-family:宋体"}]{#struct_0_x1984_13510_x84174968}[Level-1]{lang="EN-US"}[区域中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466470337}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1289998817}[配置路由器从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_910479732}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] import-route isis level-2 into level-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1310760804}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x1984_13510_x1118763836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route isis level-1 into level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1431145646}
:::

::: {#-900064531 .myid}
[]{#_Toc404788381}[]{#struct_0_x1984_13510_1803727444}[]{#_Toc303839446}[]{#_Toc180403842}

**IS-IS \-- IS-IS配置命令 \-- import-route limit**

------------------------------------------------------------------------

[**[import-route limit]{lang="EN-US"}**]{#struct_0_x1984_13510_1359118686}[命令用来配置引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由最大条数。]{style="font-family:宋体"}

[**[undo import-route limit]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466404801}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x475552385}

[**[import-route limit ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1984_13510_158526366}

[**[undo import-route limit]{lang="EN-US"}**]{#struct_0_x1984_13510_1261044506}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1537661384}

[[本命令的缺省情况和设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x1984_13510_1541128818}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1990662003}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x913113255}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466339265}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_862825840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x255331710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1747418510}

[*[number]{lang="EN-US"}*]{#struct_0_x1984_13510_1380771882}[：引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由最大条数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1441076316}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_784191774}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由最大条数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_711821928}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] import-route limit 1000]{lang="EN-US"}

[]{#struct_0_x1984_13510_x1874436109}[]{#_Toc302996870}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_x1984_13510_856377767}
:::

::: {#1179077140 .myid}
[]{#_Toc404788382}[]{#struct_0_x1984_13510_1476435337}

**IS-IS \-- IS-IS配置命令 \-- isis**

------------------------------------------------------------------------

[**[isis]{lang="EN-US"}**]{#struct_0_x1984_13510_x1554541995}[命令用来创建一个]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，并进入]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo isis]{lang="EN-US"}**]{#struct_0_x1984_13510_1495913033}[命令用来删除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_453310900}

[**[isis]{lang="EN-US"}**[ \[ *process-id* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1343082509}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466732481}**[isis]{lang="EN-US"}[ ]{lang="EN-US"}**[\[ *process-id* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1618926346}

[[系统没有运行任何]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_559803703}[进程。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1643135930}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x317126386}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_430422856}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1205292025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_78434148}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466666945}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_2077598512}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x1979874352}[：指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[位于公网中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1092955674}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x455491842}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，配置网络实体名称，其中系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0000.0000.0002]{lang="EN-US"}[，区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[01.0001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1245478386}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 01.0001.0000.0000.0002.00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1539315662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_x1466601409}**[isis]{lang="EN-US"}[ enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network-entity]{lang="EN-US"}**]{#struct_0_x1984_13510_x425787229}
:::

::: {#1285146241 .myid}
[]{#_Toc404788383}[]{#struct_0_x1984_13510_x216437786}[]{#_Toc353884899}

**IS-IS \-- IS-IS配置命令 \-- isis authentication send-only**

------------------------------------------------------------------------

[**[isis authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x216372250}[命令用来配置对收到的]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文忽略认证信息检查。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}[ isis authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x216306714}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216241178}

[**[isis authentication send-only]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x216831001}

[**[undo isis authentication send-only]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x216765465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1775841423}

[[如果配置了接口验证方式和验证密码，对收到的报文执行认证信息检查。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x216699929}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216634393}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x216568857}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216503321}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x216437785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x954185920}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216372249}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x216306713}[：]{style="font-family:宋体"}[对收到的]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文忽略认证信息检查。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x216241177}[：对收到的]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文忽略认证信息检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216831004}

[[配置邻居关系验证方式和验证密码后，验证密码将会按照设定的方式封装到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x216765468}[报文中，并对接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文进行验证密码的检查，通过检查才会形成邻居关系]{style="font-family:宋体"}[。当需要更改密码时由于密码不匹配可能导致邻居关系中断。通过命令配置对]{style="font-family:宋体"}[收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文]{style="font-family:宋体"}[忽略认证信息检查可保证邻居关系不中断，报文正常接收。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216699932}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x216634396}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置]{style="font-family:宋体"}[对收到]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文忽略认证信息检查]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x216568860}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis authentication send-only level-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x216503324}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[area-authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_248673451}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[domain-authentication]{lang="EN-US"}**]{#struct_0_x1984_13510_x216437788}**[ send-only]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[isis authentication]{lang="EN-US"}**]{#struct_0_x1984_13510_x216372252}**[-mode]{lang="EN-US"}**
:::

::: {#-1066909690 .myid}
[]{#_Toc163546280}[]{#_Toc50204102}[]{#_Toc33866101}[]{#_Toc290886781}[]{#_Toc252200760}[]{#_Toc404788384}[]{#struct_0_x1984_13510_2130545890}[]{#_Toc297189173}[]{#_Toc290886779}[]{#_Toc252200758}[]{#_Toc163546277}[]{#_Toc50204100}[]{#_Toc33866099}[]{#_Toc290911758}

**IS-IS \-- IS-IS配置命令 \-- isis authentication-mode**

------------------------------------------------------------------------

[**[isis authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_x2031107667}[命令用来配置邻居关系验证方式和验证密码。]{style="font-family:
宋体"}

[**[undo isis authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_302792761}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1171174813}

[**[isis authentication-mode]{lang="EN-US"}**[ { **gca** *key-id* { **hmac-sha-1** \| **hmac-sha-224** \| **hmac-sha-256** \| **hmac-sha-384** \| **hmac-sha-512** } \| **md5** \| **simple** } { **cipher** *cipher-string* \| **plain** *plain-string* } \[ **level-1** \| **level-2** \] \[ **ip** \| **osi** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x216306716}

[**[undo isis authentication-mode]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x2139582449}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1616557866}

[[接口没有配置邻居关系验证方式和验证密码。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1466535873}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1919957948}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1496504083}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_520106204}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1074452052}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_135952543}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_495115622}

[**[gca]{lang="EN-US"}**]{#struct_0_x1984_13510_x216831003}[：]{style="font-family:宋体"}[GCA]{lang="EN-US"}[验证模式（]{style="font-family:宋体"}[Generic Cryptographic Authentication]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x216765467}[：唯一标识一个认证项（]{style="font-family:宋体"}[SA]{lang="EN-US"}[），取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。发送方将]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[放入认证]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中，接收方根据报文中提取的]{style="font-family:宋体"}[Key ID]{lang="EN-US"}[选择]{style="font-family:宋体"}[SA]{lang="EN-US"}[对报文进行认证。]{style="font-family:宋体"}

[**[hmac-sha-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x216699931}[：支持]{style="font-family:宋体"}[HMAC-SHA-1]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-224]{lang="EN-US"}**]{#struct_0_x1984_13510_x216634395}[：支持]{style="font-family:宋体"}[HMAC-SHA-224]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-256]{lang="EN-US"}**]{#struct_0_x1984_13510_x216568859}[：支持]{style="font-family:宋体"}[HMAC-SHA-256]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-384]{lang="EN-US"}**]{#struct_0_x1984_13510_242120539}[：支持]{style="font-family:宋体"}[HMAC-SHA-384]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[hmac-sha-512]{lang="EN-US"}**]{#struct_0_x1984_13510_x216503323}[：支持]{style="font-family:宋体"}[HMAC-SHA-512]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[**[md5]{lang="FR"}**]{#struct_0_x1984_13510_x616265735}[：]{style="font-family:宋体"}[MD5]{lang="FR"}[验证模式]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[simple]{lang="FR"}**]{#struct_0_x1984_13510_2112617620}[：]{style="font-family:宋体"}[简单验证模式。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x1984_13510_162802178}[：表示输入的密码为密文。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_x1984_13510_x227825550}[：表示设置的密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_x1984_13510_x2078891002}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_x1984_13510_x503998193}[：表示设置的明文密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1992845659}[：为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[配置认证密码。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1077425363}[：为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[配置认证密码。]{style="font-family:宋体"}

[]{#_Hlt7610787}[**[ip]{lang="EN-US"}**]{#struct_0_x1984_13510_x564764369}[：检查]{style="font-family:宋体"}[SNP]{lang="EN-US"}[、]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[IP]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[**[osi]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465880513}[：检查]{style="font-family:宋体"}[SNP]{lang="EN-US"}[、]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2034087389}

[[配置邻居关系验证方式和验证密码后，验证密码将会按照设定的方式封装到]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x940463423}[报文中，并对接收到的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文进行验证密码的检查，通过检查才会形成邻居关系，否则将不会形成邻居关系。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x27157323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[两台路由器要形成邻居关系必须配置相同的验证方式和验证密码。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x636258566}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x1984_13510_22644418}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{lang="EN-US" style="font-family:宋体"}**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x64374707}[或]{lang="EN-US" style="font-family:宋体"}**[level-2]{lang="EN-US"}**[参数，将同时为]{lang="EN-US" style="font-family:宋体"}**[level-1]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文配置验证方式及验证密码。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1240544662}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[参数，将检查]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中]{style="font-family:宋体"}[OSI]{lang="EN-US"}[的相应字段的配置内容。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[认证密码选用]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1763007679}**[ip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[osi]{lang="EN-US"}**[不受实际的网络环境影响。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1466470336}**[level-1]{lang="EN-US"}**[和]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的支持情况和产品相关，具体请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先使用]{lang="EN-US" style="font-family:宋体"}**[isis enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x276085124}[命令]{lang="EN-US" style="font-family:宋体"}[在接口上使能]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能才能进行参数]{lang="EN-US" style="font-family:宋体"}**[level-1]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的配置]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1804509330}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1088938692}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1680779024}[为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置邻居关系采用简单明文验证模式，验证密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x331069743}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis authentication-mode simple plain 123456]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_113250792}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1466404800}[为]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接口配置邻居关系采用简单明文验证模式，验证[]{#_Hlt9926332}密码为]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1090531556}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis authentication-mode simple plain 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2143362196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[area-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_x558534042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain-authentication-mode]{lang="EN-US"}**]{#struct_0_x1984_13510_x1227743231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[isis authentication send-only]{lang="EN-US"}**]{#struct_0_x1984_13510_x216306715}
:::

::::: {#1835630031 .myid}
[]{#_Toc297189174}[]{#_Toc404788385}[]{#struct_0_x1984_13510_857217255}[]{#_Toc303839449}[]{#_Toc252200759}[]{#_Toc209857742}

**IS-IS \-- IS-IS配置命令 \-- isis bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x1866450967}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x802655103}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[isis bfd enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466339264}[命令用来使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **isis** **bfd enable**]{lang="EN-US"}]{#struct_0_x1984_13510_x703258101}[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2127063657}

[**[isis bfd enable]{lang="EN-US"}**]{#struct_0_x1984_13510_1252452226}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x472630439}**[isis]{lang="EN-US"}[ bfd enable]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x876608834}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x674996762}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1915928195}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1466273728}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_854447246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1460243518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x2136623971}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x770503652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_855537405}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1299747693}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466732480}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_52842405}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_945645363}[使能接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x2025266075}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis enable]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis bfd enable]{lang="EN-US"}
:::::

::: {#-1226687879 .myid}
[]{#_Toc404788386}[]{#struct_0_x1984_13510_x836802717}

**IS-IS \-- IS-IS配置命令 \-- isis circuit-level**

------------------------------------------------------------------------

[**[isis circuit-level]{lang="EN-US"}**]{#struct_0_x1984_13510_2128530508}[命令用来配置接口的链路邻接关系类型。]{style="font-family:宋体"}

[**[undo isis circuit-level]{lang="EN-US"}**]{#struct_0_x1984_13510_1935288194}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_116570668}

[**[isis circuit-level]{lang="EN-US"}**[ \[ **level-1** \| **level-1-2** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1466666944}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x651284843}**[isis]{lang="EN-US"}[ circuit-level]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_966139766}

[[接口既可以建立]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_485073461}[的邻接关系，也可以建立]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的邻接关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1512652294}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x246867019}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1212888374}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_888740368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1466601408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1140296712}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_654805109}[：配置本接口链路邻接关系类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1766679822}[：配置本接口链路邻接关系类型为]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1478367814}[：配置本接口链路邻接关系类型为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x974029774}

[[如果路由器类型是]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_372697125}[（]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[），接口的链路类型只能为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[（]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[），因此仅当路由器类型是]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[时，才需要通过配置接口的链路邻接关系类型来限制接口上所能建立的邻接关系，让接口只发送和接收]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[（]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[）类型的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1864458516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1466535872}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_808925407}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[和同一区域内的非骨干路由器相连，配置接口的链路邻接关系类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，禁止发送和接收]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x2079759448}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis circuit-level level-1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x192692898}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_655441208}[接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[和同一区域内的非骨干路由器相连，配置接口的链路邻接关系类型为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，禁止发送和接收]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x933946007}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis enable]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis circuit-level level-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_643955138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[is-level]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465946048}
:::

::: {#982519246 .myid}
[]{#_Toc404788387}[]{#struct_0_x1984_13510_1728886119}[]{#_Toc290886782}[]{#_Toc252200761}[]{#_Toc163546279}[]{#_Toc94930862}[]{#_Toc94586594}

**IS-IS \-- IS-IS配置命令 \-- isis circuit-type p2p**

------------------------------------------------------------------------

[**[isis circuit-type p2p]{lang="EN-US"}**]{#struct_0_x1984_13510_1128352162}[命令用来配置接口的网络类型为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo isis circuit-type]{lang="EN-US"}**]{#struct_0_x1984_13510_x444523209}[命令用来取消配置接口的网络类型为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_319855764}

[**[isis circuit-type p2p]{lang="EN-US"}**]{#struct_0_x1984_13510_1777321255}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_2040643729}**[isis]{lang="EN-US"}[ circuit-type]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1639432954}

[[接口网络类型根据物理接口决定。（]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1984_13510_x1465880512}[接口网络类型为]{style="font-family:宋体"}[Broadcast]{lang="EN-US"}[。）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x694795966}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x486505446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x244544554}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_51527368}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x669886155}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1490607462}

[[接口网络类型不同，其工作机制也略微不同，如：当网络类型为广播网时，需要选举]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_696372480}[、通过泛洪]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来实现]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步，当网络类型为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[时不需要选举]{style="font-family:宋体"}[DIS]{lang="EN-US"}[，]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步机制也不同。]{style="font-family:宋体"}

[[当只有两台路由器接入到同一个广播网时，通过将接口网络类型配置为]{style="font-family:宋体"}[P2P]{lang="EN-US"}]{#struct_0_x1984_13510_x1466470339}[可以使]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[按照]{style="font-family:宋体"}[P2P]{lang="EN-US"}[而不是广播网的工作机制运行，避免]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举以及]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[的泛洪，既可以节省网络带宽，又可以加快网络的收敛速度。]{style="font-family:宋体"}

[[需要注意的是，仅当接口的网络类型为广播网且只有两台路由器接入该广播网时才需要进行该项配置且两台路由器都要进行此项配置。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1485938705}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x176545361}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1480761293}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1726141078}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1692947062}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis enable]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis circuit-type p2p]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1595001894}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x121445366}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[为]{style="font-family:宋体"}[P2P]{lang="EN-US"}[类型。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466404803}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis enable]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis circuit-type p2p]{lang="EN-US"}
:::

::: {#-951638787 .myid}
[]{#_Toc404788388}[]{#struct_0_x1984_13510_x1638351799}

**IS-IS \-- IS-IS配置命令 \-- isis cost**

------------------------------------------------------------------------

[**[isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_1723375600}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口的链路开销值。]{style="font-family:宋体"}

[**[undo isis cost]{lang="EN-US"}**]{#struct_0_x1984_13510_354407985}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_493638851}

[**[isis cost]{lang="EN-US"}**[ *value* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_750232784}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_1590585303}**[isis]{lang="EN-US"}[ cost]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_51885530}

[[没有配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1466339267}[接口的链路开销值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2025625254}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_1273350613}[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1192178987}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x482298962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1870028950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_772047091}

[*[value]{lang="EN-US"}*]{#struct_0_x1984_13510_x674752138}[：链路开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466273731}[：配置在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_2064366363}[：配置在计算]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_279970376}

[[如果没有指定]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1755648447}[或者]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[，将同时配置计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2086365411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_28291412}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x213608356}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的链路开销值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466732483}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis cost 5 level-2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1513241536}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x141432656}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的链路开销值为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x2082920421}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis cost 5 level-2]{lang="EN-US"}

[]{#_Toc163546282}[]{#_Toc50204103}[]{#_Toc33866102}[]{#_Toc310604347}[]{#_Toc290886784}[]{#_Toc252200763}[]{#_Toc163546281}[]{#_Toc94930864}[]{#_Toc94586596}[]{#_Toc60036214}[]{#_Toc53707158}[]{#_Toc53487853}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_517282140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-cost enable]{lang="EN-US"}**]{#struct_0_x1984_13510_772124160}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_x1984_13510_1652985522}
:::

::: {#-1251407350 .myid}
[]{#_Toc404788389}[]{#struct_0_x1984_13510_824433892}

**IS-IS \-- IS-IS配置命令 \-- isis dis-name**

------------------------------------------------------------------------

[**[isis dis-name]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466666947}[命令用来在]{style="font-family:宋体"}[DIS]{lang="EN-US"}[上配置局域网名称来代表这个广播网中的伪节点。]{style="font-family:宋体"}

[**[undo isis dis-name]{lang="EN-US"}**]{#struct_0_x1984_13510_x1054569370}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x443538651}

[**[isis dis-name]{lang="EN-US"}**[ *symbolic-name*]{lang="EN-US"}]{#struct_0_x1984_13510_388478476}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x483114623}**[isis]{lang="EN-US"}[ dis-name]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1186207441}

[[没有配置本地局域网名称。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1331178103}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2094545100}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1480043040}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466601411}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x69491333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1483720889}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1241872137}

[*[symbolic-name]{lang="EN-US"}*]{#struct_0_x1984_13510_318790041}[：本地局域网的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1676448310}

[[该命令只有在使能了动态主机名映射功能的路由器上配置才能有效，在点到点链路的接口上配置无效。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x654173797}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x858614741}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1466535875}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x757158534}[配置本地局域网的名称为"]{style="font-family:宋体"}[LOCALAREA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1617062178}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis dis-name LOCALAREA]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1057511859}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_579186640}[配置本地局域网的名称为"]{style="font-family:宋体"}[LOCALAREA]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x454217866}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis dis-name LOCALAREA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1285603748}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465946051}**[isis]{lang="EN-US"}[ name-table]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[is-name]{lang="EN-US"}**]{#struct_0_x1984_13510_x193493718}
:::

::: {#-829126747 .myid}
[]{#_Toc404788390}[]{#struct_0_x1984_13510_x1716402093}

**IS-IS \-- IS-IS配置命令 \-- isis dis-priority**

------------------------------------------------------------------------

[**[isis dis-priority]{lang="EN-US"}**]{#struct_0_x1984_13510_1237987683}[命令用来配置接口在不同层次的]{style="font-family:宋体"}[DIS]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo isis dis-priority]{lang="EN-US"}**]{#struct_0_x1984_13510_1159837227}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_627569614}

[**[isis dis-priority]{lang="EN-US"}**[ *value* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x2075143686}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x39904205}**[isis]{lang="EN-US"}[ dis-priority]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1465880515}

[[接口]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1227518335}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别]{style="font-family:宋体"}[DIS]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1749624812}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_323353213}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_212727351}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1328514287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1801347289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_705921494}

[*[value]{lang="EN-US"}*]{#struct_0_x1984_13510_x756598559}[：配置接口]{style="font-family:宋体"}[DIS]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466470338}[：配置]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[级别]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举优先级。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1242944650}[：配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_593326152}

[[如果不指定级别，将同时配置]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_1804570556}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举优先级。]{style="font-family:宋体"}

[[当网络类型为广播网时，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x710991036}[需要选举]{style="font-family:宋体"}[DIS]{lang="EN-US"}[，]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[DIS]{lang="EN-US"}[是分别选举的，用户可以为不同级别的]{style="font-family:宋体"}[DIS]{lang="EN-US"}[选举配置不同的优先级，]{style="font-family:宋体"}[DIS]{lang="EN-US"}[优先级数值越高，被选中的可能性就越大；如果两台路由器]{style="font-family:宋体"}[DIS]{lang="EN-US"}[优先级相同，则]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[（]{style="font-family:宋体"}[Subnetwork Point of Attachment]{lang="EN-US"}[，子网连接点）地址（广播网络中的]{style="font-family:宋体"}[SNPA]{lang="EN-US"}[地址是]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址）最大的路由器会被选中。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1697668711}[中并没有备份]{style="font-family:宋体"}[DIS]{lang="EN-US"}[的概念，优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[的路由器也可以参与选举]{style="font-family:宋体"}[DIS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_642888595}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_244038031}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_540292785}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2 DIS]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466404802}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis dis-priority 127 level-2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x72267858}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_713926265}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2 DIS]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[127]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1070144372}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis dis-priority 127 level-2]{lang="EN-US"}
:::

::: {#-1913845503 .myid}
[]{#_Toc404788391}[]{#struct_0_x1984_13510_1992837377}[]{#_Toc163546283}[]{#_Toc50204104}[]{#_Toc33866103}[]{#_Toc131842023}[]{#_Toc131842774}[]{#_Toc131842024}[]{#_Toc131842775}[]{#_Toc131842025}[]{#_Toc131842776}

**IS-IS \-- IS-IS配置命令 \-- isis enable**

------------------------------------------------------------------------

[**[isis enable]{lang="EN-US"}**]{#struct_0_x1984_13510_732548165}[命令用来在指定接口上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能，并配置与该接口关联的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[**[undo isis enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x300249588}[命令用来在指定接口上关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466339266}

[**[isis enable]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_x1984_13510_459541313}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x2098600355}**[isis]{lang="EN-US"}[ enable]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1973397487}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_237364346}[功能在接口上处于关闭状态，且没有任何]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程与其关联。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x185098907}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1129013458}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1402180820}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1304671565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1466273730}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_498282422}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_982659953}[：指定与该接口关联的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，]{style="font-family:宋体"}*[process-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1907856681}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_19205933}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_332104177}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x382885902}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis enable 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x819295115}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1466732482}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，并在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1215641819}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis enable 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1963888711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_1944825323}**[isis]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network-entity]{lang="EN-US"}**]{#struct_0_x1984_13510_2075256063}
:::

::::: {#1700014286 .myid}
[]{#_Toc404788392}[]{#struct_0_x1984_13510_x437351836}[]{#_Toc366163941}[]{#_Toc364753104}

**IS-IS \-- IS-IS配置命令 \-- isis fast-reroute lfa-backup exclude**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_585002394}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x437351837}
:::

[ ]{lang="EN-US"}

[**[isis fast-reroute lfa-backup exclude]{lang="EN-US"}**]{#struct_0_x1984_13510_585067930}[命令用来]{style="font-family:宋体"}[去使能接口]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[**[undo isis fast-reroute lfa-backup exclude]{lang="EN-US"}**]{#struct_0_x1984_13510_265307408}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x437351838}

[**[isis fast-reroute lfa-backup exclude]{lang="EN-US"}**]{#struct_0_x1984_13510_584609178}

[**[undo isis fast-reroute lfa-backup exclude]{lang="EN-US"}**]{#struct_0_x1984_13510_x437351831}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_585199002}

[[接口参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x1984_13510_1495929604}[计算]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x437351832}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_585264538}[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1381904956}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x437351833}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x1984_13510_585330074}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x437351834}

[[接口缺省参与]{style="font-family:宋体"}[LFA]{lang="EN-US"}]{#struct_0_x1984_13510_584871322}[计算，有资格成为备份接口。配置本功能后，接口不会被选为备份接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1975828192}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x437351827}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_585067929}[去使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x437351828}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis enable 1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ]{lang="EN-US"}[isis fast-reroute lfa-backup exclude]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_584609177}

[[\#]{lang="EN-US"}]{#struct_0_x1984_13510_2130880362}[去使能接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[的]{style="font-family:宋体"}[LFA]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1628992923}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis enable 1]{lang="EN-US"}

[[\[Sysname-Vlan-interface10\] isis fast-reroute lfa-backup exclude]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}]{#struct_0_x1984_13510_828839924}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1628992924}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fast-reroute]{lang="EN-US"}**]{#struct_0_x1984_13510_x1093474377}
:::::

::: {#-1799458523 .myid}
[]{#_Toc163546293}[]{#_Toc50204111}[]{#_Toc33866110}[]{#_Toc290886791}[]{#_Toc252200769}[]{#_Toc163546286}[]{#_Toc290886793}[]{#_Toc252200771}[]{#_Toc163546288}[]{#_Toc50204106}[]{#_Toc33866105}[]{#_Toc297189179}[]{#_Toc404788393}[]{#struct_0_x1984_13510_414049248}[]{#_Toc310604350}[]{#_Toc290886787}[]{#_Toc252200766}[]{#_Toc163546284}[]{#_Toc50204105}[]{#_Toc33866104}[]{#_Toc17101076}[]{#_Toc290911762}[]{#_Toc167021737}[]{#_Toc167021738}

**IS-IS \-- IS-IS配置命令 \-- isis mesh-group**

------------------------------------------------------------------------

[**[isis mesh-group]{lang="EN-US"}**]{#struct_0_x1984_13510_1025000985}[命令用来配置接口属于]{style="font-family:宋体"}[Mesh group]{lang="EN-US"}[或配置接口阻塞。]{style="font-family:宋体"}

[**[undo isis mesh-group]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466666946}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_511514571}

[**[isis mesh-group ]{lang="EN-US"}**[{ *mesh-group-number* \| **mesh-blocked** }]{lang="EN-US"}]{#struct_0_x1984_13510_261575124}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x689011731}**[isis]{lang="EN-US"}[ mesh-group]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x523061085}

[[接口不属于任何]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}]{#struct_0_x1984_13510_x1824557818}[且接口不阻塞。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1974980638}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1191444617}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466601410}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1496592608}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x498962732}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_167001427}

[*[mesh-group-number]{lang="EN-US"}*]{#struct_0_x1984_13510_1425606521}[：]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[mesh-blocked]{lang="EN-US"}**]{#struct_0_x1984_13510_1764444774}[：配置接口阻塞，接口只有在收到邻居路由器要求发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的请求时才会发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，否则不会主动向外发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x751622734}

[]{#struct_0_x1984_13510_746981779}[]{#_Hlt9930022}[对于不属于]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[的接口，当收到]{style="font-family:宋体"}[LSP]{lang="EN-US"}[时，接口将按照正常流程将]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散到所有其它接口。对于连通程度比较高，有多条点到点链路的]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[网络，这种处理会造成]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的重复扩散，浪费带宽。]{style="font-family:宋体"}

[[把接口配置属于一个]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}]{#struct_0_x1984_13510_x292131966}[后，当接收到一个新的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[时，只把]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散到其它]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[的接口以及没有配置]{style="font-family:宋体"}[Mesh group]{lang="EN-US"}[的接口，而不会扩散到到同]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[中的其它接口。]{style="font-family:宋体"}

[[若配置某个接口阻塞，则该接口只有在收到邻居路由器要求发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1466535874}[的请求时才会发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[，否则不会主动向外发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}]{#struct_0_x1984_13510_1971724821}[只对点到点类型链路的接口起作用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1781860116}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x203524502}[将帧中继子接口]{style="font-family:宋体"}[Serial2/1/1.1]{lang="EN-US"}[加入组号为]{style="font-family:宋体"}[3]{lang="EN-US"}[的]{style="font-family:宋体"}[Mesh-Group]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1119404975}

[\[Sysname\] interface serial 2/1/1]{lang="EN-US"}

[\[Sysname-Serial2/1/1\] link-protocol fr]{lang="EN-US"}

[\[Sysname-Serial2/1/1\] quit]{lang="EN-US"}

[\[Sysname\] interface serial 2/1/1.1]{lang="EN-US"}

[\[Sysname-Serial2/1/1.1\] isis mesh-group 3]{lang="EN-US"}
:::

::: {#170545295 .myid}
[]{#_Toc310604353}[]{#_Toc404788394}[]{#struct_0_x1984_13510_x44181750}[]{#_Toc327790393}[]{#_Toc319940292}[]{#_Toc308430274}[]{#_Toc252200778}

**IS-IS \-- IS-IS配置命令 \-- isis mib-binding**

------------------------------------------------------------------------

[**[isis mib-binding]{lang="EN-US"}**]{#struct_0_x1984_13510_x180434229}[命令]{style="font-family:宋体"}[用来配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo isis mib-binding]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465946050}[命令]{style="font-family:宋体"}[用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1372590223}

[**[isis mib-binding]{lang="EN-US"}***[ process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_187380834}

[**[undo isis mib-binding]{lang="EN-US"}**]{#struct_0_x1984_13510_x1615294677}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x810007328}

[[MIB]{lang="EN-US"}]{#struct_0_x1984_13510_1644709462}[绑定在进程号最小的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1447797535}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x839524775}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1893658613}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1465880514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1501365020}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x507014091}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x1429159198}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1322881012}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x917727120}*[process-id]{lang="FR"}*[不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:
宋体"}[IS-IS]{lang="FR"}[进程绑定命令时将会提示]{lang="EN-US" style="font-family:
宋体"}[IS-IS]{lang="FR"}[进程不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[无法完成配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1268889763}[IS-IS]{lang="FR"}[进程绑定]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="FR"}[，]{lang="EN-US" style="font-family:宋体"}[若删除]{lang="EN-US" style="font-family:宋体"}*[process-id]{lang="FR"}*[对应的]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="FR"}[进程]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:
宋体"}[则同时删除]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="FR"}[进程绑定]{lang="EN-US" style="font-family:宋体"}[MIB]{lang="FR"}[配置]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[MIB]{lang="FR"}[绑定]{lang="EN-US" style="font-family:宋体"}[到]{style="font-family:宋体"}[进程号最小的]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="FR"}[进程上。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1728805422}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x425601784}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466470341}

[\[Sysname\] isis mib-binding 100]{lang="EN-US"}
:::

::::: {#-1720857105 .myid}
[]{#_Toc404788395}[]{#struct_0_x1984_13510_x1842365673}

**IS-IS \-- IS-IS配置命令 \-- isis peer-ip-check**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x2068066632}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1062400804}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[isis peer-ip-check]{lang="EN-US"}**]{#struct_0_x1984_13510_754073624}[命令用来配置在]{style="font-family:宋体"}[PPP]{lang="EN-US"}[接口上建立邻接关系必须在同一网段的检查功能，即在接收]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时，对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与当前接口必须在同一网段。]{style="font-family:宋体"}

[**[undo isis peer-ip-check]{lang="EN-US"}**]{#struct_0_x1984_13510_x1182110236}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_524278809}

[**[isis peer-ip-check]{lang="EN-US"}**]{#struct_0_x1984_13510_1349580619}

[**[undo isis peer-ip-check]{lang="EN-US"}**]{#struct_0_x1984_13510_1349646155}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_724461939}

[[协议类型为]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_x1984_13510_28197524}[的接口要与对端路由器建立邻接关系，双方可以不在同一网段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_629017554}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_40409244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x307994367}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_271959085}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1466339269}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1819003348}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1896315079}[配置在]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[接口上与对端路由器建立邻接关系必须在同一网段的检查功能，即在]{style="font-family:宋体"}[Serial2/1/0]{lang="EN-US"}[上接收]{style="font-family:宋体"}[IS-IS Hello]{lang="EN-US"}[报文时，对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与当前接口必须在同一网段才可以建立邻接关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x79776096}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] isis peer-ip-check]{lang="EN-US"}
:::::

::: {#-271487563 .myid}
[]{#_Toc404788396}[]{#struct_0_x1984_13510_x1628992916}[]{#_Toc366163946}[]{#_Toc364753100}

**IS-IS \-- IS-IS配置命令 \-- isis prefix-suppression**

------------------------------------------------------------------------

[**[isis prefix-suppression]{lang="EN-US"}**]{#struct_0_x1984_13510_709659237}[命令用来配置接口的前缀抑制功能。]{style="font-family:宋体"}

[**[undo isis prefix-suppression]{lang="EN-US"}**]{#struct_0_x1984_13510_1361007957}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_709659236}

[**[isis prefix-suppression]{lang="EN-US"}**]{#struct_0_x1984_13510_1361007956}

[**[undo isis prefix-suppression]{lang="EN-US"}**]{#struct_0_x1984_13510_709659235}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1361007955}

[[未配置接口的前缀抑制功能。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1388676108}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_709659234}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_1361007954}[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_709659241}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x595307185}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_232102518}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_709659240}

[[接口使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x595307186}[时，有时候不希望在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中发布此接口的前缀，可以通过在接口上配置本命令，减少此接口的前缀在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中携带，屏蔽内部节点被发布，提高安全性，加快路由收敛。]{style="font-family:宋体"}

[[本命令对接口从地址同样生效。]{style="font-family:宋体"}]{#struct_0_x1984_13510_709659239}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1361007959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_709659238}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1361007958}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能前缀抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_709659245}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis prefix-suppression]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x595307181}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_709659244}[接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[使能前缀抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x595307182}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis prefix-suppression]{lang="EN-US"}
:::

::::: {#-110867320 .myid}
[]{#_Toc404788397}[]{#struct_0_x1984_13510_1349252937}[]{#_Toc363978778}

**IS-IS \-- IS-IS配置命令 \-- isis primary-path-detect bfd echo**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1349318473}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1349384009}
:::

**[ ]{lang="EN-US"}**

[**[isis primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x1984_13510_1349449545}[命令用来使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[**[undo isis primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x1984_13510_1349515081}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349580617}

[**[isis primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_x1984_13510_1349646153}

[**[undo isis primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_x1984_13510_1349711689}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349777225}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1349842761}[协议中主用链路的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349252938}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1349318474}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349384010}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1349449546}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1349515082}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349580618}

[[配置本功能后，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1349646154}[协议的快速重路由特性和]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中的主用链路将使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）进行检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1349711690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1349777226}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1349842762}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_945968414}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] ]{lang="EN-US"}[fast-reroute lfa]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] quit]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis primary-path-detect bfd echo]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_946033950}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_946099486}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] pic additional-path-always]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] isis primary-path-detect bfd echo]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_946165022}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_946230558}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_946361630}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] ]{lang="EN-US"}[fast-reroute lfa]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\] quit]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis primary-path-detect bfd echo]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_140324052}[在接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[上配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议]{style="font-family:宋体"}[PIC]{lang="EN-US"}[特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_946492702}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] pic additional-path-always]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis primary-path-detect bfd echo]{lang="EN-US"}
:::::

::: {#-470447966 .myid}
[]{#_Toc404788398}[]{#struct_0_x1984_13510_x858315191}

**IS-IS \-- IS-IS配置命令 \-- isis silent**

------------------------------------------------------------------------

[**[isis silent]{lang="EN-US"}**]{#struct_0_x1984_13510_x618681558}[命令用来禁止接口发送和接收]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo isis silent]{lang="EN-US"}**]{#struct_0_x1984_13510_552689224}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1002834597}

[**[isis silent]{lang="EN-US"}**]{#struct_0_x1984_13510_x679217835}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466273733}**[isis]{lang="EN-US"}[ silent]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1067801519}

[[接口既发送也接收]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1727343809}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1239585235}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_2124598640}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_212913246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1545015342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1845041656}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x152345268}

[[Loopback]{lang="EN-US"}]{#struct_0_x1984_13510_x1466732485}[接口视图下不支持此命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x350442122}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1025968469}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1600182163}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送和接收]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_178666138}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis silent]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x982062126}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x560833838}[禁止接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送和接收]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466666949}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis silent]{lang="EN-US"}
:::

::: {#-1733297603 .myid}
[]{#_Toc404788399}[]{#struct_0_x1984_13510_464460404}[]{#_Toc297189180}

**IS-IS \-- IS-IS配置命令 \-- isis small-hello**

------------------------------------------------------------------------

[**[isis small-hello]{lang="EN-US"}**]{#struct_0_x1984_13510_963468592}[命令用来配置接口发送不加入填充]{style="font-family:宋体"}[CLV]{lang="EN-US"}[的小型]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo isis small-hello]{lang="EN-US"}**]{#struct_0_x1984_13510_612887415}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_367281396}

[**[isis small-hello]{lang="EN-US"}**]{#struct_0_x1984_13510_x1006657615}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x1107217275}**[isis]{lang="EN-US"}[ small-hello]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1689682159}

[[接口发送标准]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1466601413}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1232290747}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1322301456}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1052092571}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_853556192}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x991577659}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1861772634}

[[Loopback]{lang="EN-US"}]{#struct_0_x1984_13510_x1193229942}[接口视图下不支持此命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x683245546}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1466535877}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_405640880}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送小型]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x179063446}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis small-hello]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x447515086}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_593408870}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送小型]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_100116719}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis small-hello]{lang="EN-US"}
:::

::: {#226552829 .myid}
[]{#_Toc404788400}[]{#struct_0_x1984_13510_x83129752}[]{#_Toc366163957}[]{#_Toc364753102}

**IS-IS \-- IS-IS配置命令 \-- isis tag**

------------------------------------------------------------------------

[**[isis tag]{lang="EN-US"}**]{#struct_0_x1984_13510_x921795554}[命令用来配置接口的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isis tag]{lang="EN-US"}**]{#struct_0_x1984_13510_1856414631}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x83129753}

[**[isis tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_x921795555}

[**[undo isis tag]{lang="EN-US"}**]{#struct_0_x1984_13510_x83129754}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x921795556}

[[没有配置接口的]{style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_x1984_13510_x83129747}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1416856601}

[[接口视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x1984_13510_x702091949}[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x83129748}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1416856600}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1490848357}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_341095120}

[*[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_1490848356}[：管理标记值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_341160656}

[[当]{style="font-family:宋体"}[cost-sytle]{lang="EN-US"}]{#struct_0_x1984_13510_x686627295}[为]{style="font-family:宋体"}[wide]{lang="EN-US"}[、]{style="font-family:宋体"}[wide-compatible ]{lang="EN-US"}[或]{style="font-family:宋体"}[compatible]{lang="EN-US"}[时，如果发布可达的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀具有]{style="font-family:宋体"}[Tag]{lang="EN-US"}[属性，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[会将]{style="font-family:宋体"}[Tag]{lang="EN-US"}[加入到该前缀的]{style="font-family:宋体"}[IP]{lang="EN-US"}[可达信息]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1490848355}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_341226192}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1490848354}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_341291728}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ]{lang="EN-US"}[tag 4294967295]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1490848361}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_340964051}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1490848360}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis ]{lang="EN-US"}[tag 4294967295]{lang="EN-US"}
:::

::: {#1594687059 .myid}
[]{#_Toc404788401}[]{#struct_0_x1984_13510_1775468949}[]{#_Toc297189181}

**IS-IS \-- IS-IS配置命令 \-- isis timer csnp**

------------------------------------------------------------------------

[**[isis timer csnp]{lang="EN-US"}**]{#struct_0_x1984_13510_644124582}[命令用来配置]{style="font-family:宋体"}[DIS]{lang="EN-US"}[在广播网络上发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo isis timer csnp]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465946053}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1356293132}

[**[isis timer csnp]{lang="EN-US"}**[ *seconds* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x526524621}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x1693897010}**[isis]{lang="EN-US"}[ timer csnp]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_765770039}

[[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_x1371141444}[在广播网络上发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_911882144}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1542213858}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1512914397}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1465880517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_64718921}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x891875933}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_316310651}[：]{style="font-family:宋体"}[DIS]{lang="EN-US"}[在广播网络上发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1360856782}[：配置]{style="font-family:宋体"}[DIS]{lang="EN-US"}[在]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1357705618}[：配置]{style="font-family:宋体"}[DIS]{lang="EN-US"}[在]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1529578952}

[[如果不指定级别，将同时配置]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_415815695}[在]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[发送]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[当网络类型为广播网时，]{style="font-family:宋体"}[DIS]{lang="EN-US"}]{#struct_0_x1984_13510_1751143430}[使用]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文来进行]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[同步，因此只有在被选举为]{style="font-family:宋体"}[DIS]{lang="EN-US"}[的路由器上进行该项配置才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466470340}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_886517682}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1920980712}[配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的发送时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1740571679}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis timer csnp 15 level-2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_505658862}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1814972088}[配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[报文在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接口上的发送时间间隔为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_2048204772}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis timer csnp 15 level-2]{lang="EN-US"}
:::

::: {#-962323879 .myid}
[]{#_Toc404788402}[]{#struct_0_x1984_13510_x1466404804}[]{#_Toc297189182}

**IS-IS \-- IS-IS配置命令 \-- isis timer hello**

------------------------------------------------------------------------

[**[isis timer hello]{lang="EN-US"}**]{#struct_0_x1984_13510_x878836912}[命令用来配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo isis timer hello]{lang="EN-US"}**]{#struct_0_x1984_13510_576765604}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1263599821}

[**[isis timer hello]{lang="EN-US"}**[ *seconds* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_709462051}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_x1645789696}**[isis]{lang="EN-US"}[ timer hello]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1151366134}

[[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x768054891}[报文的发送时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1082002748}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1466339268}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_909880007}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_416053058}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x29212956}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1927810089}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_1047737056}[：配置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x288490381}[：配置]{style="font-family:宋体"}[Level-1 Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_909526258}[：配置]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文的发送时间间隔。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1879412041}

[[如果路由器在邻居关系保持时间内（即]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1466273732}[报文失效数目与]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送时间间隔的乘积）没有收到来自邻居路由器的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时将宣告邻居关系失效。通过设置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目和]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻居关系保持时间，即邻居路由器要花多长时间能够监测到链路已经失效并重新进行路由计算。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_1661081836}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在广播链路上，]{style="font-family:宋体"}]{#struct_0_x1984_13510_139184233}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文会分别发送，其时间间隔也要分别配置；在点到点链路中，]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文是在同一个点到点]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中发送，不需要分别配置发送时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_x1984_13510_630615664}[和]{lang="EN-US" style="font-family:宋体"}[level-2]{lang="EN-US"}[仅在广播接口上是可配置的，而且必须先在接口上使能]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送时间间隔越短，网络收敛更快，但也需要占用更多的系统资源；因此，需要根据实际情况指定。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x2076446914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定级别，将同时配置]{style="font-family:宋体"}]{#struct_0_x1984_13510_1518405071}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送时间间隔。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1261462128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1930806144}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_103633541}[配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上的发送时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1466732484}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis timer hello 20 level-2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1916526063}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1696041997}[配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接口上的发送时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1515210067}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis timer hello 20 level-2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2103650887}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1984_13510_x1247995997}
:::

::: {#-512477566 .myid}
[]{#_Toc404788403}[]{#struct_0_x1984_13510_769964261}[]{#_Toc297189183}

**IS-IS \-- IS-IS配置命令 \-- isis timer holding-multiplier**

------------------------------------------------------------------------

[**[isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1984_13510_x1466666948}[命令用来配置]{style="font-family:
宋体"}[Hello]{lang="EN-US"}[报文失效数目。]{style="font-family:宋体"}

[**[undo isis timer holding-multiplier]{lang="EN-US"}**]{#struct_0_x1984_13510_2030544345}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_97924693}

[**[isis timer holding-multiplier]{lang="EN-US"}**[ *value* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1500762015}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_x246204925}**[isis]{lang="EN-US"}[ timer holding-multiplier]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1965605314}

[[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1460156443}[报文失效数目为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_206954672}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1548616462}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1466601412}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_333793194}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1836804389}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1004469241}

[*[value]{lang="EN-US"}*]{#struct_0_x1984_13510_1831090672}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1397101856}[：]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x946543624}[：]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1609786222}

[[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1802329590}[报文失效数目，即宣告邻居失效前]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[没有收到的邻居]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的数目。]{style="font-family:宋体"}

[[如果路由器在邻居关系保持时间内（即]{style="font-family:宋体"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_x1466535876}[报文失效数目与]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送时间间隔的乘积）没有收到来自邻居路由器的]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文时将宣告邻居关系失效。通过设置]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目和]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文的发送时间间隔，可以调整邻居关系保持时间，即邻居路由器要花多长时间能够监测到链路已经失效并重新进行路由计算。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1160443061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在广播链路上，]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x534854090}[和]{lang="EN-US" style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文会分别发送，]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目需要分别设置；在点到点链路中，]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文是在同一个点到点]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文中发送，因此不需要指定]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[参数]{lang="EN-US" style="font-family:宋体"}[level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x1806823245}[和]{lang="EN-US" style="font-family:宋体"}[level-2]{lang="EN-US"}[仅在广播接口上是可配置的，而且必须先在接口上使能]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定级别，将同时配置]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x2015335594}[和]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Hello]{lang="EN-US"}[报文失效数目。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hello]{lang="EN-US"}]{#struct_0_x1984_13510_1125182162}[报文失效数目与]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文发送时间间隔的乘积不能超过]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x911270663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_1445450229}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_312492884}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上标志邻居失效的]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文数目为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1465946052}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis timer holding-multiplier 6 level-2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_209790809}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_245736962}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上标志邻居失效的]{style="font-family:宋体"}[Level-2 Hello]{lang="EN-US"}[报文数目为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x2022750164}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis timer holding-multiplier 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_101564163}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis timer hello]{lang="EN-US"}**]{#struct_0_x1984_13510_484413509}
:::

::: {#1203487485 .myid}
[]{#_Toc404788404}[]{#struct_0_x1984_13510_325177512}[]{#_Toc297189184}

**IS-IS \-- IS-IS配置命令 \-- isis timer lsp**

------------------------------------------------------------------------

[**[isis timer lsp]{lang="EN-US"}**]{#struct_0_x1984_13510_x1465880516}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[在接口上发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小时间间隔以及一次最多可以发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文数目。]{style="font-family:宋体"}

[**[undo isis timer lsp]{lang="EN-US"}**]{#struct_0_x1984_13510_1630802862}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x318440114}

[**[isis timer lsp ]{lang="EN-US"}***[time ]{lang="EN-US"}*[\[ **count** *count* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x140520804}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1984_13510_1449791791}**[isis]{lang="EN-US"}[ timer lsp]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_778483721}

[[发送]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1111080133}[的最小时间间隔为]{style="font-family:宋体"}[33]{lang="EN-US"}[毫秒，一次最多可以发送]{style="font-family:宋体"}[5]{lang="EN-US"}[个]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1023277786}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1623300236}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x586664961}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99613604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1766832902}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2045145671}

[*[time]{lang="EN-US"}*]{#struct_0_x1984_13510_509823431}[：发送链路状态报文的最小时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_x1984_13510_400824918}[：一次最多发送的链路状态报文的数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1972971668}

[[当]{style="font-family:宋体"}[LSDB]{lang="EN-US"}]{#struct_0_x1984_13510_1648017223}[的内容发生变化时，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[将把发生变化的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[扩散出去，用户可以对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最小发送时间间隔进行调节。]{style="font-family:宋体"}

[[请合理配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1280836400}[发送时间间隔，当存在大量]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[接口或大量路由时，会发送大量的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文，导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[风暴的出现。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99679140}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_2126845804}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1369192314}[配置在]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接口]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的发送时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_635816076}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis timer lsp 500]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1859385555}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1852181361}[配置在]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接口]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的发送时间间隔为]{style="font-family:宋体"}[500]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1004848628}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis timer lsp 500]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_720553916}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis timer retransmit]{lang="EN-US"}**]{#struct_0_x1984_13510_99744676}
:::

::: {#1595350185 .myid}
[]{#_Toc297189185}[]{#_Toc294861138}[]{#_Toc264877107}[]{#_Toc404788405}[]{#struct_0_x1984_13510_1195207989}

**IS-IS \-- IS-IS配置命令 \-- isis timer retransmit**

------------------------------------------------------------------------

[**[isis timer retransmit]{lang="EN-US"}**]{#struct_0_x1984_13510_x1012019838}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在点到点链路上的重传时间间隔。]{style="font-family:宋体"}

[**[undo isis timer retransmit]{lang="EN-US"}**]{#struct_0_x1984_13510_x303664772}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_527287313}

[**[isis timer retransmit ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_803837751}

[**[undo isis timer retransmit]{lang="EN-US"}**]{#struct_0_x1984_13510_x454045389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1648798358}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x2137069497}[在点到点链路上的重传时间间隔]{style="font-family:宋体"}[为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99810212}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1215552824}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x767747254}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1088508326}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_715444725}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1796810139}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_807917795}[：表示]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文的重传时间间隔，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2033227193}

[[在点到点链路上，发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x411653488}[需要得到对端的应答，否则将在重传时间间隔内重新发送该]{style="font-family:宋体"}[LSP]{lang="EN-US"}[；在广播链路上，]{style="font-family:宋体"}[DIS]{lang="EN-US"}[周期性广播]{style="font-family:宋体"}[CSNP]{lang="EN-US"}[来实现]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的同步，不需要进行此项配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99351460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_239082769}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_239648712}[在接口]{style="font-family:宋体"}[Serial2/1/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在点到点链路上的重传时间间隔]{style="font-family:宋体"}[为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_220709197}

[\[Sysname\] interface serial 2/1/1]{lang="EN-US"}

[\[Sysname-Serial2]{lang="NO-BOK"}[/1]{lang="EN-US"}[/1\] isis timer retransmit 50]{lang="NO-BOK"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1984_13510_x1494512629}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_2068822659}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在点到点链路上的重传时间间隔]{style="font-family:宋体"}[为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_99416996}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] ]{lang="NO-BOK"}[isis circuit-type p2p]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis timer retransmit 50]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1983532658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis circuit-type p2p]{lang="EN-US"}**]{#struct_0_x1984_13510_x1722315370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis timer ]{lang="EN-US"}**]{#struct_0_x1984_13510_1157230960}**[lsp]{lang="EN-US"}**
:::

::: {#1045460818 .myid}
[]{#_Toc404788406}[]{#struct_0_x1984_13510_946099484}[]{#_Toc357599184}[]{#_Toc352311299}

**IS-IS \-- IS-IS配置命令 \-- isis topology enable**

------------------------------------------------------------------------

[**[isis topology enable]{lang="EN-US"}**]{#struct_0_x1984_13510_946165020}[命令用来在接口使能拓扑的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo isis topology enable]{lang="EN-US"}**]{#struct_0_x1984_13510_946230556}[命令用来关闭此拓扑的]{style="font-family:
宋体"}[IS-IS]{lang="EN-US"}[功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_920238332}

[**[isis topology enable]{lang="EN-US"}**]{#struct_0_x1984_13510_946296092}

[**[undo isis topology enable]{lang="EN-US"}**]{#struct_0_x1984_13510_946361628}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_946427164}

[[没有使能拓扑的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_946492700}[功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_946558236}

[[接口]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_945968413}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_946033949}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_946099485}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_946165021}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_946230557}

[[本命令必须满足下面条件才能进行配置：]{style="font-family:宋体"}]{#struct_0_x1984_13510_946361629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[接口使能了]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_946427165}[；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[创建了]{lang="EN-US" style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_946492701}[单播]{style="font-family:宋体"}[拓扑。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_772514555}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_946558237}[在接口上]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[单播拓扑]{style="font-family:宋体"}[voice]{lang="EN-US"}[中使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_946099482}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-100-ipv4\] topology voice tid 4000]{lang="EN-US"}

[\[Sysname-isis-100-ipv4-topo-voice\] quit]{lang="EN-US"}

[\[Sysname-isis-100-ipv4\] quit]{lang="EN-US"}

[\[Sysname-isis-100\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="NO-BOK"}[Ethernet1/0/1\] isis enable 100]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="NO-BOK"}[Ethernet1/0/1\] topology ipv4 voice]{lang="EN-US"}

[\[Sysname-]{lang="EN-US"}[Gigabit]{lang="NO-BOK"}[Ethernet1/0/1-topo-voice\] isis topology enable]{lang="EN-US"}
:::

::::: {#-835536423 .myid}
[]{#_Toc404788407}[]{#struct_0_x1984_13510_760096085}

**IS-IS \-- IS-IS配置命令 \-- ispf enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){#图片 18 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1801784143}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_738063865}
:::

[ ]{lang="EN-US"}

[**[ispf enable]{lang="EN-US"}**]{#struct_0_x1984_13510_143374313}[命令用来使能]{style="font-family:宋体"}[IS-IS ISPF]{lang="EN-US"}[功能，即增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_x1984_13510_1638238552}[命令用来关闭]{style="font-family:宋体"}[IS-IS ISPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99482532}

[**[ispf enable]{lang="EN-US"}**]{#struct_0_x1984_13510_1081131112}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_x1984_13510_x1118442513}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_527586046}

[[使能]{style="font-family:宋体"}[IS-IS ISPF]{lang="EN-US"}]{#struct_0_x1984_13510_1845568153}[功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1288312824}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1100566788}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x149614235}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1083883743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99548068}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x386966878}

[[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_x1984_13510_2096836224}[计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1360147548}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1759478766}[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x640824990}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] ispf enable]{lang="EN-US"}
:::::

::: {#-1193310726 .myid}
[]{#_Toc404788408}[]{#struct_0_x1984_13510_1244675950}

**IS-IS \-- IS-IS配置命令 \-- is-level**

------------------------------------------------------------------------

[**[is-level]{lang="EN-US"}**]{#struct_0_x1984_13510_488957374}[命令用来配置路由器的]{style="font-family:宋体"}[Level]{lang="EN-US"}[级别。]{style="font-family:宋体"}

[**[undo is-level]{lang="EN-US"}**]{#struct_0_x1984_13510_100137892}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1007798503}

[**[is-level]{lang="EN-US"}**[ { **level-1** \| **level-1-2** \| **level-2** }]{lang="EN-US"}]{#struct_0_x1984_13510_x1724331935}

[**[undo]{lang="EN-US"}**[ **is-level**]{lang="EN-US"}]{#struct_0_x1984_13510_x420431093}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1609201146}

[[路由器的的]{style="font-family:宋体"}[Level]{lang="EN-US"}]{#struct_0_x1984_13510_1601870026}[级别为]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x178838813}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x2020909526}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100203428}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1870006706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1124543155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x275247584}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_264980700}[：配置路由器工作在]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[，它只计算区域内路由，维护]{style="font-family:宋体"}[L1]{lang="EN-US"}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x115544347}[：配置路由器工作在]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[，同时参与]{style="font-family:宋体"}[L1]{lang="EN-US"}[和]{style="font-family:宋体"}[L2]{lang="EN-US"}[的路由计算，维护]{style="font-family:宋体"}[L1]{lang="EN-US"}[和]{style="font-family:宋体"}[L2]{lang="EN-US"}[两个]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x2066373394}[：配置路由器工作在]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，只参加]{style="font-family:宋体"}[L2]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[交换和]{style="font-family:宋体"}[L2]{lang="EN-US"}[的路由计算，维护]{style="font-family:宋体"}[L2]{lang="EN-US"}[的]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1082448758}

[[如果只有一个区域，建议用户将所有路由器的]{style="font-family:宋体"}[Level]{lang="EN-US"}]{#struct_0_x1984_13510_915413246}[配置为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[或者]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，因为没有必要让所有路由器同时维护两个完全相同的数据库。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1984_13510_99613605}[网络中使用时，建议将所有的路由器都配置为]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，这[]{#_Hlt9930802}样有利于以后的扩展。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_189482234}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_841117299}[配置路由器的]{style="font-family:宋体"}[Level]{lang="EN-US"}[级别为]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_524563870}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] is-level level-1]{lang="EN-US"}
:::

::: {#-1398635010 .myid}
[]{#_Toc163546297}[]{#_Toc50204112}[]{#_Toc33866111}[]{#_Toc404788409}[]{#struct_0_x1984_13510_x765339536}[]{#_Toc310604351}[]{#_Toc53487862}

**IS-IS \-- IS-IS配置命令 \-- is-name**

------------------------------------------------------------------------

[**[is-name]{lang="EN-US"}**]{#struct_0_x1984_13510_77525186}[命令用来使能动态主机名映射功能并为当前路由器配置主机名称。]{style="font-family:宋体"}

[**[undo is-name]{lang="EN-US"}**]{#struct_0_x1984_13510_13678947}[命令用来关闭动态主机名映射功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99679141}

[**[is-name ]{lang="EN-US"}***[sys-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x211806356}

[**[undo is-name]{lang="EN-US"}**]{#struct_0_x1984_13510_606649426}

[[【]{style="font-family:黑体"}]{#struct_0_x1984_13510_2100561973}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[动态主机名映射功能处于关闭状态且没有为当前路由器配置主机名称。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1516139480}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1474571345}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_356968557}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2066509159}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1423102750}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99744677}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x761107147}

[*[sys-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x1662824199}[：为本地]{style="font-family:宋体"}[IS]{lang="EN-US"}[配置的主机名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1848959386}

[[只有使能动态主机名映射功能后，使用]{style="font-family:宋体"}**[display isis lsdb]{lang="EN-US"}**]{#struct_0_x1984_13510_x126323523}[等命令才可以看到路由器的主机名而不是]{style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1824629046}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_613873275}[为本地]{style="font-family:宋体"}[IS]{lang="EN-US"}[配置主机名称。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x273686592}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] is-name RUTA]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99810213}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isis name-table]{lang="EN-US"}**]{#struct_0_x1984_13510_x1123099336}
:::

::: {#2119776104 .myid}
[]{#_Toc404788410}[]{#struct_0_x1984_13510_1582963767}[]{#_Toc310604352}[]{#_Toc163546295}

**IS-IS \-- IS-IS配置命令 \-- is-name map**

------------------------------------------------------------------------

[**[is-name map]{lang="EN-US"}**]{#struct_0_x1984_13510_1021641141}[命令用来为远端]{style="font-family:宋体"}[IS]{lang="EN-US"}[配置]{style="font-family:宋体"}[System ID]{lang="EN-US"}[与主机名称的映射关系。]{style="font-family:宋体"}

[**[undo is-name map]{lang="EN-US"}**]{#struct_0_x1984_13510_337750069}[命令用来取消此配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x3789597}

[**[is-name map]{lang="EN-US"}**[ *sys-id* *map-sys-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x993457580}

[**[undo]{lang="EN-US"}**[ **is-name map** *sys-id*]{lang="EN-US"}]{#struct_0_x1984_13510_1505598152}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1724987367}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_99351461}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2099569391}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x872793518}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_705787710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1801247830}

[*[sys-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x1205173766}[：远端]{style="font-family:宋体"}[IS]{lang="EN-US"}[的系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[或伪系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[map-sys-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x1477242800}[：为远端]{style="font-family:宋体"}[IS]{lang="EN-US"}[配置的主机名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1721036583}

[[每个]{style="font-family:宋体"}[System ID]{lang="EN-US"}]{#struct_0_x1984_13510_x823626208}[只能对应一个主机名称。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99416997}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x355119502}[为远端]{style="font-family:宋体"}[IS]{lang="EN-US"}[配置静态主机名映射，远端]{style="font-family:宋体"}[IS]{lang="EN-US"}[的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[为"]{style="font-family:宋体"}[0000.0000.0041]{lang="EN-US"}["，为其配置的主机名称为"]{style="font-family:宋体"}[RUTB]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1502749251}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] is-name map 0000.0000.0041 RUTB]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1591722762}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display isis name-table]{lang="EN-US"}**]{#struct_0_x1984_13510_x1482515118}
:::

::: {#-1110888516 .myid}
[]{#_Toc404788411}[]{#struct_0_x1984_13510_x93240001}

**IS-IS \-- IS-IS配置命令 \-- log-peer-change**

------------------------------------------------------------------------

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_x1984_13510_1032774290}[命令用来打开邻接状态变化的输出开关。]{style="font-family:宋体"}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_x1984_13510_x1214299577}[命令用来关闭邻接状态变化的输出开关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99482533}

[**[log-peer-change]{lang="EN-US"}**]{#struct_0_x1984_13510_x875184024}

[**[undo log-peer-change]{lang="EN-US"}**]{#struct_0_x1984_13510_x225258394}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1261984379}

[[邻接状态变化的输出开关处于打开状态。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x556714805}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_935272511}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1680800690}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_433550962}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_214446202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99548069}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1951685282}

[[打开邻接状态输出开关后，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_903536080}[邻接状态变化]{style="font-family:宋体"}[时会生成日志信息发送到设备的信息中心，通过设置信息中心的参数，最终决定]{style="font-family:宋体"}[日志信息]{style="font-family:宋体"}[的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_250295110}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_2984634}[关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻接状态变化的输出开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x404735550}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] undo log-peer-change]{lang="EN-US"}
:::

::: {#-1316377163 .myid}
[]{#_Toc163546302}[]{#_Toc50204113}[]{#_Toc33866112}[]{#_Toc290886806}[]{#_Toc252200784}[]{#_Toc163546301}[]{#_Toc303839460}[]{#_Toc252200782}[]{#_Toc163546299}[]{#_Toc94930881}[]{#_Toc94586613}[]{#_Toc60036225}[]{#_Toc53707169}[]{#_Toc53487865}[]{#_Toc404788412}[]{#struct_0_x1984_13510_x733857655}[]{#_Toc310604363}[]{#_Toc290886803}[]{#_Toc252200781}[]{#_Toc163546298}[]{#_Toc94930880}[]{#_Toc94586612}[]{#_Toc60036224}[]{#_Toc53707168}[]{#_Toc53487864}

**IS-IS \-- IS-IS配置命令 \-- lsp-fragments-extend**

------------------------------------------------------------------------

[**[lsp-fragments--extend]{lang="EN-US"}**]{#struct_0_x1984_13510_1662354754}[命令用来在指定]{style="font-family:宋体"}[Level]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片扩展功能。]{style="font-family:宋体"}

[**[undo lsp-fragments--extend]{lang="EN-US"}**]{#struct_0_x1984_13510_100137893}[命令用来关闭该功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1007798504}

[**[lsp-fragments-extend]{lang="EN-US"}**[ \[ **level-1** \| **level-1-2** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1724790687}

[**[undo lsp-fragments-extend]{lang="EN-US"}**]{#struct_0_x1984_13510_310585054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1023600132}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1024493417}[分片扩展功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_49778988}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x2016116793}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_33577206}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_100203429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1870006707}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1604340200}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x811785204}[：只对]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[进行分片扩展。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_2034577553}[：对]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[都进行分片扩展。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_208317167}[：只对]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[进行分片扩展。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1862852388}

[[如果配置时没有指定]{style="font-family:宋体"}**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_x1042138110}[、]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[或]{style="font-family:宋体"}**[level-1-2]{lang="EN-US"}**[参数，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程运行]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片扩展功能时，将同时对]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[都进行分片扩展。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x126632779}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_99613602}[使能]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[分片扩展功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x619821830}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] lsp-fragments-extend level-2]{lang="EN-US"}
:::

::: {#-446381553 .myid}
[]{#_Toc404788413}[]{#struct_0_x1984_13510_1320509064}

**IS-IS \-- IS-IS配置命令 \-- lsp-length originate**

------------------------------------------------------------------------

[**[lsp-length originate]{lang="EN-US"}**]{#struct_0_x1984_13510_1905085610}[命令用来配置当前路由器生成的]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[的最大长度。]{style="font-family:宋体"}

[**[undo lsp-length originate]{lang="EN-US"}**]{#struct_0_x1984_13510_x1311347984}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2008859394}

[**[lsp-length originate ]{lang="EN-US"}***[size]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_1592012765}

[**[undo lsp-length originate]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x422875268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99679138}

[[生成的]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1984_13510_927310545}[和]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[的最大长度均为]{style="font-family:宋体"}[1497]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1178841286}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x2017083540}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1474437493}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x203701250}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1584830947}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1417239757}

[*[size]{lang="EN-US"}*]{#struct_0_x1984_13510_99744674}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大长度，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1577545013}[：配置]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[长度。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_608932403}[：配置]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[长度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2077611081}

[[如果命令中没有指定]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_x1984_13510_x927281807}[或]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[，则默认为对当前]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[系统进行配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1025996113}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1266174340}[配置生成的]{style="font-family:宋体"}[Level-2 LSP]{lang="EN-US"}[最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_13444637}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] lsp-length originate 1024 level-2]{lang="EN-US"}
:::

::: {#-1321064373 .myid}
[]{#_Toc404788414}[]{#struct_0_x1984_13510_99810210}[]{#_Toc303839461}[]{#_Toc252200783}[]{#_Toc163546300}

**IS-IS \-- IS-IS配置命令 \-- lsp-length receive**

------------------------------------------------------------------------

[**[lsp-length receive]{lang="EN-US"}**]{#struct_0_x1984_13510_833215800}[命令用来配置当前路由器可以接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大长度。]{style="font-family:宋体"}

[**[undo lsp-length receive]{lang="EN-US"}**]{#struct_0_x1984_13510_751031195}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1661634907}

[**[lsp-length receive ]{lang="EN-US"}***[size]{lang="EN-US"}*]{#struct_0_x1984_13510_872107322}

[**[undo lsp-length receive]{lang="EN-US"}**]{#struct_0_x1984_13510_x720983237}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2060803982}

[[可以接收的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x986536932}[的最大长度为]{style="font-family:宋体"}[1497]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_781135360}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_99351458}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x886980800}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1795507535}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_854052005}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1604166378}

[*[size]{lang="EN-US"}*]{#struct_0_x1984_13510_2019973520}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大长度，取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[16384]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_228891016}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1310157218}[配置接收]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_99416994}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] lsp-length receive 1024]{lang="EN-US"}
:::

::::: {#1012649285 .myid}
[]{#_Toc404788415}[]{#struct_0_x1984_13510_1601195634}

**IS-IS \-- IS-IS配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_170027730}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_351306236}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[maximum load]{lang="EN-US"}**[-**balancing**]{lang="EN-US"}]{#struct_0_x1984_13510_1736053606}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持的等价路由的最大条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_x1984_13510_209160629}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1343763869}

[**[maximum load-balancing ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1984_13510_x370225440}

[**[undo]{lang="EN-US"}**[ **maximum load-balancing**]{lang="EN-US"}]{#struct_0_x1984_13510_x1613275222}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99482530}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1463468136}[支持的等价路由的最大条数与]{style="font-family:宋体"}[系统支持最大等价路由的条数相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_978693745}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x1769081802}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1147735626}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x345399468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x610325914}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_740372523}

[*[number]{lang="EN-US"}*]{#struct_0_x1984_13510_590565541}[：等价路由的最大条数]{style="font-family:宋体"}[。不同设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99548066}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x1984_13510_1524718242}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x1984_13510_x1154792549}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x819799982}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_281215749}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持的等价路由的最大条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x812356379}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\]]{lang="EN-US"}[ maximum load-balancing 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1108851577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_x1984_13510_638883714}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::::

::: {#-1364991054 .myid}
[]{#_Toc404788416}[]{#struct_0_x1984_13510_688437442}

**IS-IS \-- IS-IS配置命令 \-- network-entity**

------------------------------------------------------------------------

[**[network-entity]{lang="EN-US"}**]{#struct_0_x1984_13510_100137890}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的网络实体名称（]{style="font-family:宋体"}[Network Entity Title]{lang="EN-US"}[，简称]{style="font-family:宋体"}[NET]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo network-entity]{lang="EN-US"}**]{#struct_0_x1984_13510_1007798501}[命令用来删除网络实体名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1724463007}

[**[network-entity]{lang="EN-US"}**[ *net*]{lang="EN-US"}]{#struct_0_x1984_13510_380705571}

[**[undo]{lang="EN-US"}**[ **network-entity** *net*]{lang="EN-US"}]{#struct_0_x1984_13510_x1192140178}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2122112609}

[[没有配置]{style="font-family:宋体"}[NET]{lang="EN-US"}]{#struct_0_x1984_13510_362476936}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_35865849}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1234057700}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100203426}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1870006692}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1200596922}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1264454779}

[*[net]{lang="EN-US"}*]{#struct_0_x1984_13510_x258071119}[：格式为]{style="font-family:宋体"}[X...X.XXXX\....XXXX.00]{lang="EN-US"}[，为十六进制数。前面的"]{style="font-family:宋体"}[X...X]{lang="EN-US"}["是区域地址，中间的]{style="font-family:宋体"}[12]{lang="EN-US"}[个"]{style="font-family:宋体"}[X]{lang="EN-US"}["是路由器的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[，最后的"]{style="font-family:宋体"}[00]{lang="EN-US"}["]{style="font-family:宋体"}[是]{style="font-family:宋体"}[SEL]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Hlt9849512}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1055489289}

[[NET]{lang="EN-US"}]{#struct_0_x1984_13510_x493726510}[可以看作是一类特殊的]{style="font-family:宋体"}[NSAP]{lang="EN-US"}[，即]{style="font-family:宋体"}[SEL]{lang="EN-US"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[的]{style="font-family:
宋体"}[NSAP]{lang="EN-US"}[地址，长度为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[NET]{lang="EN-US"}]{#struct_0_x1984_13510_x631435393}[由三部分组成：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[区域]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1881367660}[ID]{lang="EN-US"}[：它的长度可变的，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[13]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[System ID]{lang="EN-US"}]{#struct_0_x1984_13510_99613603}[：用来在区域内唯一标识主机或路由器，它的长度固定为]{style="font-family:
宋体"}[6]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SEL]{lang="EN-US"}]{#struct_0_x1984_13510_1336493306}[：为]{style="font-family:宋体"}[0]{lang="EN-US"}[，它的长度固定为]{style="font-family:宋体"}[1]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[]{#struct_0_x1984_13510_2059962674}[]{#_Hlt9848777}[例如]{style="font-family:宋体"}[NET]{lang="EN-US"}[为：]{style="font-family:宋体"}[ab.cdef.1234.5678.9abc.00]{lang="EN-US"}[，则其中区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[ab.cdef]{lang="EN-US"}[，]{style="font-family:宋体"}[System ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1234.5678.9abc]{lang="EN-US"}[，]{style="font-family:宋体"}[SEL]{lang="EN-US"}[为]{style="font-family:宋体"}[00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_820915722}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1466669925}[指定]{style="font-family:宋体"}[NET]{lang="EN-US"}[为]{style="font-family:宋体"}[10.0001.1010.1020.1030.00]{lang="EN-US"}[。其中区域]{style="font-family:宋体"}[ID]{lang="EN-US"}[是]{style="font-family:宋体"}[10.0001]{lang="EN-US"}[，]{style="font-family:宋体"}[System ID]{lang="EN-US"}[是]{style="font-family:宋体"}[1010.1020.1030]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1983044789}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1297298565}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_2138951587}**[isis]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}]{#struct_0_x1984_13510_99679139}**[isis]{lang="EN-US"}[ enable]{lang="EN-US"}**
:::

::::: {#-1554088180 .myid}
[]{#_Toc163546304}[]{#_Toc50204115}[]{#_Toc33866114}[]{#_Toc404788417}[]{#struct_0_x1984_13510_x1411341615}[]{#_Toc332962826}

**IS-IS \-- IS-IS配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image002.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x1795206013}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_788279554}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_x1984_13510_833135658}[命令用来使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x1984_13510_939869655}**[non-stop-routing]{lang="EN-US"}**[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1514119356}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_x1984_13510_1732222722}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_x1984_13510_x1074332016}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99744675}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x378770123}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x997850460}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_121579175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x2003464146}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_736948871}

[[IS-IS NSR]{lang="EN-US"}]{#struct_0_x1984_13510_1637782665}[特性与]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[和]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1627192809}

[[\#]{lang="EN-US"}]{#struct_0_x1984_13510_99810211}[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[中使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1984_13510_x1505436360}

[[\[Sysname\] isis 1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1984_13510_x1980837047}

[[\[Sysname-isis-1\] non-stop-routing]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1984_13510_x1972938020}
:::::

::::: {#537581611 .myid}
[]{#_Toc404788418}[]{#struct_0_x1984_13510_x1782587261}[]{#_Toc356910955}

**IS-IS \-- IS-IS配置命令 \-- pic**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image002.png){#图片 6 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_x1782521725}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_x1782456189}
:::

**[ ]{lang="EN-US"}**

[**[pic]{lang="EN-US"}**]{#struct_0_x1984_13510_x1782390653}[命令用来使能前缀无关收敛功能。]{style="font-family:宋体"}

[**[undo pic]{lang="EN-US"}**]{#struct_0_x1984_13510_x1782325117}[命令用来]{style="font-family:宋体"}[关闭]{style="font-family:宋体"}[前缀无关收敛功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782914940}

[**[pic]{lang="EN-US" style="color:black"}**[ \[ **[additional-path-always]{style="color:black"}** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1782849404}

[**[undo ]{lang="EN-US" style="color:black"}[pic]{lang="EN-US" style="color:black"}**]{#struct_0_x1984_13510_x1782783868}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1869662298}

[[前缀无关收敛]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1782718332}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782652796}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1782587260}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782521724}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1782456188}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1782390652}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782325116}

[**[additional-path-always]{lang="EN-US"}**]{#struct_0_x1984_13510_x1782914943}[：支持非直连的次优路由作为备份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782849407}

[[PIC]{lang="EN-US"}]{#struct_0_x1984_13510_x1782783871}[（]{style="font-family:宋体"}[Prefix Independent Convergence]{lang="EN-US"}[，前缀无关收敛），即收敛时间与前缀数量无关，加快收敛速度。传统的路由计算快速收敛都与前缀数量相关，收敛时间与前缀数量成正比。只有邻居发送的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[才会进行]{style="font-family:宋体"}[PIC]{lang="EN-US"}[。]{style="font-family:宋体"}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1782718335}[快速重路由功能和]{style="font-family:宋体"}[PIC]{lang="EN-US"}[同时配置时，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[快速重路由功能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1782652799}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1782587263}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的]{style="font-family:宋体"}[PIC]{lang="EN-US"}[支持非直连次优路由做备份功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1782456191}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] pic additional-path-always]{lang="EN-US"}
:::::

::: {#830408614 .myid}
[]{#_Toc404788419}[]{#struct_0_x1984_13510_x1879418082}

**IS-IS \-- IS-IS配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_x1984_13510_622430784}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_x1984_13510_x401366751}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1600857540}

[**[preference]{lang="EN-US"}**[ { *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_x1984_13510_x1189837549}

[**[undo preference]{lang="EN-US"}**]{#struct_0_x1984_13510_99351459}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1069334336}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1156064862}[路由的优先级为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1223250603}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_452867106}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1480027073}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1477030572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1596209333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1038336134}

[*[preference]{lang="EN-US"}*]{#struct_0_x1984_13510_99416995}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由]{style="font-family:宋体"}[优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x737456526}[：指定路由策略，对通过该路由策略过滤的路由指定优先级。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1441069406}

[[配置了]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**]{#struct_0_x1984_13510_1713593673}[参数后，如果]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[中对某些匹配的路由优先级进行了修改，则这些匹配的路由取]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[修改的优先级，其它路由的优先级均取]{style="font-family:宋体"}**[preference]{lang="EN-US"}**[命令所设的值。]{style="font-family:宋体"}

[[由于在一台路由器上可能同时运行多种动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题。系统为每一种路由协议配置一个优先级，当不同协议都发现了到同一目的地的路由时，优先级高的协议将起决定作用。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1968678573}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1512025771}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_2088461052}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的优先级为]{style="font-family:宋体"}[25]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1831264269}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\]]{lang="EN-US"}[ preference 25]{lang="EN-US"}
:::

::: {#-330683803 .myid}
[]{#_Toc404788420}[]{#struct_0_x1984_13510_x199081229}[]{#_Toc290886812}[]{#_Toc280710927}[]{#_Toc280362185}

**IS-IS \-- IS-IS配置命令 \-- prefix-priority**

------------------------------------------------------------------------

[**[prefix-priority]{lang="EN-US"}**]{#struct_0_x1984_13510_99482531}[命令用来配置指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由收敛的优先级。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[prefix-priority]{lang="EN-US"}**]{#struct_0_x1984_13510_x492847000}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1737595716}

[**[prefix-priority]{lang="EN-US"}**[ { **critical** \| **high** \| **medium** } { **prefix-list** *prefix-list-name* \| **tag** *tag-value* }]{lang="EN-US"}]{#struct_0_x1984_13510_1486409071}

[**[prefix-priority]{lang="EN-US"}**[ **route-policy** *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x1782521726}

[**[undo prefix-priority]{lang="EN-US"}**[ { **critical** \| **high** \| **medium** } \[ **prefix-list** \| **tag** \]]{lang="EN-US"}]{#struct_0_x1984_13510_604260014}

[**[undo prefix-priority]{lang="EN-US"}**[ **route-policy**]{lang="EN-US"}]{#struct_0_x1984_13510_x1782390654}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1493181735}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x630070286}[路由收敛的优先级为低优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x323559002}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_x1336206676}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99548067}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x431596894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1736509113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1344392862}

[**[critical]{lang="EN-US"}**]{#struct_0_x1984_13510_431696723}[：最高优先级。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_x1984_13510_26764149}[：高优先级。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_x1984_13510_x860555431}[：中优先级。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_x1984_13510_x904370133}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名，唯一标识一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}***[ tag-value]{lang="EN-US"}*]{#struct_0_x1984_13510_x1680936700}[：指定要求的标记值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1984_13510_x1782783873}[：指定路由策略名，]{style="font-family:宋体"}[配置路由收敛的优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100137891}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1007798502}[路由的优先级越高收敛的速度越快。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1724397471}[主机路由的优先级为中优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x710132314}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_903604450}[配置前缀列表]{style="font-family:宋体"}[standtest]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由收敛的优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_2045468727}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\]]{lang="EN-US"}[ prefix-priority high prefix-list standtest]{lang="EN-US"}
:::

::: {#-1821009193 .myid}
[]{#_Toc404788421}[]{#struct_0_x1984_13510_x639116109}

**IS-IS \-- IS-IS配置命令 \-- reset isis all**

------------------------------------------------------------------------

[**[reset isis all]{lang="EN-US"}**]{#struct_0_x1984_13510_x1269499687}[命令用来清除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程所有的数据结构信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100203427}

[**[reset isis all ]{lang="EN-US"}**[\[ ]{lang="EN-US"}*[process-id]{lang="EN-US"}***[ ]{lang="EN-US"}**[\] \[ **graceful-restart** \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1870006693}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x365487019}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1480216960}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x601595668}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_169752655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1762442950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_127541580}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_x845245868}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，清除该]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程所有的数据结构信息。]{style="font-family:宋体"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_x1984_13510_99613600}[：清除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[数据之后，通过]{style="font-family:宋体"}[GR]{lang="EN-US"}[方式来恢复。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1002158854}

[[如果未指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_858636028}[进程号，将清除所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的数据结构信息。]{style="font-family:宋体"}

[[本命令用在某些需要立即刷新]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1585933981}[的情况下。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2096013640}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1365822866}[清除所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的数据结构信息。]{style="font-family:宋体"}

[[\<Sysname\> reset isis all]{lang="EN-US"}]{#struct_0_x1984_13510_x796640256}
:::

::::: {#-1340509168 .myid}
[]{#_Toc297189189}[]{#_Toc290886818}[]{#_Toc252200794}[]{#_Toc163546310}[]{#_Toc50204122}[]{#_Toc33866121}[]{#_Toc310604370}[]{#_Toc290886814}[]{#_Toc252200790}[]{#_Toc163546305}[]{#_Toc50204116}[]{#_Toc33866115}[]{#_Toc404788422}[]{#struct_0_x1984_13510_x442816917}[]{#_Toc332962830}

**IS-IS \-- IS-IS配置命令 \-- reset isis graceful-restart event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_486495791}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_99679136}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[reset isis ]{lang="EN-US"}[graceful-restart event-log]{lang="EN-US"}**]{#struct_0_x1984_13510_x1749048623}[命令用来清除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1903817844}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x1984_13510_x2017057706}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ]{lang="EN-US"}[isis ]{lang="EN-US"}**]{#struct_0_x1984_13510_x797976942}**[graceful-restart]{lang="EN-US"}[ event-log slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_303501243}[模式：]{style="font-family:宋体"}

[**[reset ]{lang="EN-US"}[isis ]{lang="EN-US"}**]{#struct_0_x1984_13510_x572721716}**[graceful-restart]{lang="EN-US"}[ event-log chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1083798011}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_1847689568}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99744672}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_430533941}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x33216454}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x359002208}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_1245775983}*[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_890824092}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x1984_13510_709180855}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS GR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_x85292442}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_634035034}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_497034674}[清除]{style="font-family:宋体"}[1]{lang="EN-US"}[号板上]{style="font-family:宋体"}[GR]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> reset isis graceful-restart event-log slot 1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1984_13510_99810208}
:::::

::::: {#-955252832 .myid}
[]{#_Toc404788423}[]{#struct_0_x1984_13510_869951645}[]{#_Toc332962831}

**IS-IS \-- IS-IS配置命令 \-- reset isis non-stop-routing event-log**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IS-IS命令.files/image001.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1984_13510_1172134691}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1984_13510_1910703949}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[reset isis ]{lang="EN-US"}[non-stop-routing event-log]{lang="EN-US"}**]{#struct_0_x1984_13510_x2037602569}[命令用来清除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2074292496}

[[分布式设备－独立运行模式]{style="font-family:宋体"}]{#struct_0_x1984_13510_1620297251}[/]{lang="EN-US"}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[reset ]{lang="EN-US"}[isis non-stop-routing event-log slot]{lang="EN-US"}**[ *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x89407605}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x1984_13510_99351456}[模式：]{style="font-family:宋体"}

[**[reset ]{lang="EN-US"}[isis non-stop-routing event-log chassis]{lang="EN-US"}**[ *chassis-number* **slot** *slot-number* \[ **cpu** *cpu-number* \]]{lang="EN-US"}]{#struct_0_x1984_13510_1789378368}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1225904830}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_789078092}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_342965856}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1667248002}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1733623115}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1612675819}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_99416992}*[ slot-number]{lang="EN-US"}*[：清除指定单板的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**]{#struct_0_x1984_13510_x1546760590}*[ slot-number]{lang="EN-US"}*[：清除指定成员设备的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**]{#struct_0_x1984_13510_x423127811}[ *chassis-number* **slot** *slot-number*]{lang="EN-US"}[：清除指定成员设备上指定单板的]{style="font-family:宋体"}[IS-IS NSR]{lang="EN-US"}[日志信息]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）]{style="font-family:宋体"}

[**[cpu]{lang="EN-US"}**[ *cpu-number*]{lang="EN-US"}]{#struct_0_x1984_13510_1488685669}[：清除指定]{style="font-family:宋体"}[CPU]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[cpu-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[CPU]{lang="EN-US"}[编号。]{style="font-family:宋体"}[只有指定的]{style="font-family:宋体"}**[slot]{lang="EN-US"}**[支持多]{style="font-family:宋体"}[CPU]{lang="EN-US"}[时，才能配置该参数。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x29127621}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1198853816}[清除]{style="font-family:宋体"}[1]{lang="EN-US"}[号板上]{style="font-family:宋体"}[NSR]{lang="EN-US"}[的日志信息。]{style="font-family:宋体"}

[[\<Sysname\> reset isis non-stop-routing event-log slot 1]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x1984_13510_2126903763}
:::::

::: {#942553127 .myid}
[]{#_Toc404788424}[]{#struct_0_x1984_13510_x1446870047}

**IS-IS \-- IS-IS配置命令 \-- reset isis peer**

------------------------------------------------------------------------

[**[reset isis peer]{lang="EN-US"}**]{#struct_0_x1984_13510_x531216769}[命令用来清除]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[指定邻居的数据结构信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1170208948}

[**[reset ]{lang="EN-US"}**]{#struct_0_x1984_13510_99482528}**[isis]{lang="EN-US"}[ peer]{lang="EN-US"}**[ *system-id* \[ *process-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_263932877}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x130175795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_687512322}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_541625274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x688059607}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x80538680}

[*[system-id]{lang="EN-US"}*]{#struct_0_x1984_13510_923458103}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_x1984_13510_99548064}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，清除指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程邻居的数据结构信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1907055266}

[[本命令用在需要重建某个特定邻居的情况下使用。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1700096759}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1181355300}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_1371192988}[清除系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[0000.0c]{lang="EN-US"}[11.1111]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居的数据结构信息。]{style="font-family:宋体"}

[[\<Sysname\> reset isis peer ]{lang="EN-US"}]{#struct_0_x1984_13510_1910709782}[0000.0c]{lang="EN-US"}[11.1111]{lang="EN-US"}
:::

::: {#654289525 .myid}
[]{#_Toc310604371}[]{#_Toc290886815}[]{#_Toc252200791}[]{#_Toc163546306}[]{#_Toc50204117}[]{#_Toc404788425}[]{#struct_0_x1984_13510_x136956679}[]{#_Toc340564367}

**IS-IS \-- IS-IS配置命令 \-- reset osi statistics**

------------------------------------------------------------------------

[**[reset osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_1039399357}[命令用来清除]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100137888}

[**[reset osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_x948516643}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_238638481}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1059570503}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x505755940}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1467627663}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_680494017}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1476262131}

[[在某些情况下，需要统计从某个时刻开始的报文统计信息，这时必须在统计开始前清除原有的统计信息，重新进行统计。]{style="font-family:宋体"}]{#struct_0_x1984_13510_1290368404}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_100203424}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1870006694}[清除]{style="font-family:宋体"}[OSI]{lang="EN-US"}[连接的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset osi statistics]{lang="EN-US"}]{#struct_0_x1984_13510_37797508}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1090771701}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display osi statistics]{lang="EN-US"}**]{#struct_0_x1984_13510_x292794120}
:::

::: {#-698792996 .myid}
[]{#_Toc404788426}[]{#struct_0_x1984_13510_1488685667}[]{#_Toc366163989}[]{#_Toc364753106}

**IS-IS \-- IS-IS配置命令 \-- set-att**

------------------------------------------------------------------------

[**[set-att]{lang="EN-US"}**]{#struct_0_x1984_13510_1488685666}[命令用来设置系统自身发布的]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[的]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[undo set-att]{lang="EN-US"}**]{#struct_0_x1984_13510_x1581728207}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1488685673}

[**[set-att]{lang="EN-US"}**[ { **always** \| **never** }]{lang="EN-US"}]{#struct_0_x1984_13510_x1581531600}

[**[undo set-att]{lang="EN-US"}**]{#struct_0_x1984_13510_1488685672}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1581466064}

[[没有设置系统自身发布的]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1488685671}[的]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1581400528}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1488685670}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1581334992}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1488685677}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1581793744}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1488685676}

[**[always]{lang="SV"}**]{#struct_0_x1984_13510_x1581728208}[：]{style="font-family:宋体"}[保持对]{style="font-family:宋体"}[Level-1 LSP]{lang="SV"}[的]{style="font-family:宋体"}[ATT]{lang="SV"}[位置位。]{style="font-family:宋体"}

[**[never]{lang="SV"}**]{#struct_0_x1984_13510_x467629467}[：保持对]{style="font-family:宋体"}[Lev]{lang="EN-US"}[el-1 LSP]{lang="SV"}[的]{style="font-family:宋体"}[ATT]{lang="SV"}[位不置位。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1512894795}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x467629468}[设置]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位置位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1513615691}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] set-att always]{lang="EN-US"}
:::

::: {#116059579 .myid}
[]{#_Toc404788427}[]{#struct_0_x1984_13510_x507250506}

**IS-IS \-- IS-IS配置命令 \-- set-overload**

------------------------------------------------------------------------

[**[set-overload]{lang="EN-US"}**]{#struct_0_x1984_13510_1740959935}[命令用来为当前路由器配置过载标志位。]{style="font-family:宋体"}

[**[undo set-overload]{lang="EN-US"}**]{#struct_0_x1984_13510_2133089314}[命令用来清除过载标志位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99613601}

[**[set-overload]{lang="EN-US"}**[ \[ **on-startup** \[ \[ **start-from-nbr**]{lang="EN-US"}[ *system-id* \[ *timeout1* \[ *nbr-timeout* \] \] \] \| *timeout2* \| **wait-for-bgp** \[ *timeout3* \]]{lang="EN-US"}]{#struct_0_x1984_13510_954156282}[ ]{lang="EN-US" style="font-size:10.0pt;font-family:,\"serif\""}[\] \] ]{lang="EN-US"}[\[ **allow** { **external** \| **interlevel** } \* \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **set-overload**]{lang="EN-US"}]{#struct_0_x1984_13510_791312422}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x248267282}

[[不配置过载标志位。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x997733987}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_491178111}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1076067307}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x112755698}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99679137}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_207266513}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2098562712}

[**[on-startup]{lang="EN-US"}**]{#struct_0_x1984_13510_435184408}[：系统启动时将过载标志位置位。]{style="font-family:宋体"}

[**[start-from-nbr]{lang="EN-US"}**[ *system-id* \[ *timeout1* \[ *nbr-timeout* \] \]]{lang="EN-US"}]{#struct_0_x1984_13510_x1694745550}[：从系统启动时开始计算，如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内仍未与指定邻居建立邻接关系完毕，过载标志位将结束置位状态；如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内与指定邻居建立邻接关系完毕，过载标志位将继续保持置位状态，]{style="font-family:宋体"}[且从与指定邻居建立邻接关系时重新计时，在]{style="font-family:宋体"}*[timeout1]{lang="EN-US"}*[参数配置的时长内保持置位状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_x1984_13510_932113060}[：指定邻居的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timeout1]{lang="EN-US"}*]{#struct_0_x1984_13510_x788246071}[：]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-timeout]{lang="EN-US"}*]{#struct_0_x1984_13510_x368562824}[：取值范围为]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{lang="EN-US" style="font-family:宋体"}[1200]{lang="EN-US"}[秒（]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[分钟）。]{lang="EN-US" style="font-family:宋体"}

[*[timeout2]{lang="EN-US"}*]{#struct_0_x1984_13510_x1941763495}[：]{style="font-family:宋体"}[从系统启动时开始计算，过载标志位保持置位状态的时间长度，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒。缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[**[wait-for-bgp]{lang="EN-US"}**[ \[ *timeout3* \]]{lang="EN-US"}]{#struct_0_x1984_13510_x467629463}[：]{style="font-family:宋体"}[从系统启动时开始计算，如果在]{style="font-family:宋体"}*[timeout3]{lang="EN-US"}*[参数指定的时长内]{style="font-family:宋体"}[BGP]{lang="EN-US"}[仍未收敛，过载标志位将结束置位状态。]{style="font-family:宋体"}*[timeout3]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}[（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[allow]{lang="EN-US"}**]{#struct_0_x1984_13510_99744673}[：允许发布地址前缀。缺省情况下，当系统进入过载状态时不允许发布地址前缀。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_x1984_13510_x1525781195}[：当配置]{style="font-family:宋体"}**[allow]{lang="EN-US"}**[时，允许发布从其它协议学来的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀。]{style="font-family:宋体"}

[**[interlevel]{lang="EN-US"}**]{#struct_0_x1984_13510_x2040789637}[：当配置]{style="font-family:宋体"}**[allow]{lang="EN-US"}**[时，允许发布从不同层次学来的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_384729012}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{lang="EN-US" style="font-family:宋体"}**[on-startup]{lang="EN-US"}**]{#struct_0_x1984_13510_x1343341804}[参数，]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[将立即把过载标志位置位且一直保持置位状态直到用户通过]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **set-overload**]{lang="EN-US"}[清除过载标志位。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定]{style="font-family:宋体"}]{#struct_0_x1984_13510_1865007923}**[on-startup]{lang="EN-US"}**[参数，过载标志位将在系统启动时开始置位，并且在]{style="font-family:宋体"}*[timeout2]{lang="EN-US"}*[参数]{style="font-family:宋体"}[指定的时长内保持置位状态。]{style="font-family:宋体"}

[]{#struct_0_x1984_13510_x1523284981}[]{#_Hlt9934657}[【举例】]{style="font-family:黑体"}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_612053717}[在当前路由器上配置过载标志位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_99810209}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] set-overload]{lang="EN-US"}
:::

::: {#870763228 .myid}
[]{#_Toc310604372}[]{#_Toc290886816}[]{#_Toc252200792}[]{#_Toc163546308}[]{#_Toc50204121}[]{#_Toc33866120}[]{#_Toc327790416}[]{#_Toc319940294}[]{#_Toc404788428}[]{#struct_0_x1984_13510_x1468700515}[]{#_Toc350155037}[]{#_Toc344302280}[]{#_Toc370737493}[]{#_Toc370737494}[]{#_Toc370737495}[]{#_Toc370737496}[]{#_Toc269462885}

**IS-IS \-- IS-IS配置命令 \-- snmp context-name**

------------------------------------------------------------------------

[**[snmp]{lang="EN-US"}**]{#struct_0_x1984_13510_x1911457760}[ **context-name**]{lang="EN-US"}[命令用来配置管理]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp** ]{lang="EN-US"}]{#struct_0_x1984_13510_x1838382305}**[context-name]{lang="EN-US"}**[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1026451743}

[**[snmp]{lang="EN-US"}**]{#struct_0_x1984_13510_x861832990}[ **context-name**]{lang="EN-US"}[ *context-name*]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ **snmp** ]{lang="EN-US"}]{#struct_0_x1984_13510_1478822661}**[context-name]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1038884155}

[[没有配置]{style="font-family:宋体"}]{#struct_0_x1984_13510_99351457}[管理]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x549273792}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x568353783}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_304447179}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_566407274}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1684263943}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1559418535}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1984_13510_2089394019}[：上下文的名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_99416993}

[[TRILL]{lang="EN-US"}]{#struct_0_x1984_13510_409554546}[使用]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[（]{style="font-family:宋体"}[Management Information Base]{lang="EN-US"}[，管理信息库）对]{style="font-family:宋体"}[NMS]{lang="EN-US"}[（]{style="font-family:宋体"}[Network Management System]{lang="EN-US"}[，网络管理系统）提供]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[对象的管理，但标准]{style="font-family:宋体"}[IS-IS MIB]{lang="EN-US"}[中定义的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[为单实例管理对象，无法同时对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[和]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进行管理]{style="font-family:宋体"}[。因此，参考]{style="font-family:宋体"}[RFC 4750]{lang="EN-US"}[中对]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[多实例的管理方法，为管理]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[定义一个上下文名称，以区分来自]{style="font-family:宋体"}[NMS]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[请求是要对]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[还是]{style="font-family:宋体"}[TRILL]{lang="EN-US"}[进行管理。需要注意的是，由于上下文名称只是]{style="font-family:宋体"}[SNMPv3]{lang="EN-US"}[独有的概念，因此对于]{style="font-family:宋体"}[SNMPv1/v2c]{lang="EN-US"}[，会将团体名映射为上下文名称以对不同协议进行区分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_686924196}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1092441438}[配置管理]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[实体所使用的上下文名称为]{style="font-family:宋体"}[isis]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x2071979775}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] snmp context-name isis]{lang="EN-US"}
:::

::: {#140071955 .myid}
[]{#_Toc404788429}[]{#struct_0_x1984_13510_29536040}

**IS-IS \-- IS-IS配置命令 \-- snmp-agent trap enable isis**

------------------------------------------------------------------------

[**[snmp-agent trap enable isis]{lang="EN-US"}**]{#struct_0_x1984_13510_x1473559927}[命令用来开启]{style="font-family:
宋体"}[IS-IS]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable isis]{lang="EN-US"}**]{#struct_0_x1984_13510_99482529}[命令用来关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1692382259}

[**[snmp-agent trap enable isis]{lang="EN-US"}**[ \[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-corrupt** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **manual-address-drop** \| **max-seq-exceeded** \| **maxarea-mismatch** \| **own-lsp-purge** \| **protocol-support**  \| **rejected-adjacency** \| **skip-sequence-number** \| **version-skew** \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_x674645386}

[**[undo snmp-agent trap enable isis]{lang="EN-US"}**[ \[ **adjacency-state-change** \| **area-mismatch** \| **authentication** \| **authentication-type** \| **buffsize-mismatch** \| **id-length-mismatch** \| **lsdboverload-state-change** \| **lsp-corrupt** \| **lsp-parse-error** \| **lsp-size-exceeded** \| **manual-address-drop** \| **max-seq-exceeded** \| **maxarea-mismatch** \| **own-lsp-purge** \| **protocol-support**  \| **rejected-adjacency** \| **skip-sequence-number** \| **version-skew** \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_1580949657}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1546959344}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_884011334}[的告警功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1381898009}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1984_13510_x41289077}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1616129250}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_99548065}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x49259870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_581861678}

[**[adjacency-state-change]{lang="EN-US"}**]{#struct_0_x1984_13510_720166421}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[邻居状态变化。]{style="font-family:宋体"}

[**[area-mismatch]{lang="EN-US"}**]{#struct_0_x1984_13510_x1498686551}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文区域地址不匹配。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_x1984_13510_x2049490469}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文认证失败。]{style="font-family:宋体"}

[**[authentication-type]{lang="EN-US"}**]{#struct_0_x1984_13510_x172040886}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文认证类型错误。]{style="font-family:宋体"}

[**[buffsize-mismatch]{lang="EN-US"}**]{#struct_0_x1984_13510_x1568865901}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文长度和产生缓冲区大小不匹配。]{style="font-family:宋体"}

[**[id-length-mismatch]{lang="EN-US"}**]{#struct_0_x1984_13510_100137889}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[报文中]{style="font-family:宋体"}[System ID]{lang="EN-US"}[长度不匹配。]{style="font-family:宋体"}

[**[lsdboverload-state-change]{lang="EN-US"}**]{#struct_0_x1984_13510_x948516642}[：]{style="font-family:
宋体"}[LSDB]{lang="EN-US"}[过载状态变化。]{style="font-family:宋体"}

[**[lsp-corrupt]{lang="EN-US"}**]{#struct_0_x1984_13510_238704017}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[中校验和错误。]{style="font-family:宋体"}

[**[lsp-parse-error]{lang="EN-US"}**]{#struct_0_x1984_13510_910453496}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文解析错误。]{style="font-family:宋体"}

[**[lsp-size-exceeded]{lang="EN-US"}**]{#struct_0_x1984_13510_x1380707371}[：超大的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[报文导致泛洪失败。]{style="font-family:宋体"}

[**[manual-address-drop]{lang="EN-US"}**]{#struct_0_x1984_13510_1362766236}[：手动配置区域地址丢弃。]{style="font-family:宋体"}

[**[max-seq-exceeded]{lang="EN-US"}**]{#struct_0_x1984_13510_x1896935664}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号超过最大序列号。]{style="font-family:宋体"}

[**[maxarea-mismatch]{lang="EN-US"}**]{#struct_0_x1984_13510_1295326296}[：最大配置区域地址数不匹配。]{style="font-family:宋体"}

[**[own-lsp-purge]{lang="EN-US"}**]{#struct_0_x1984_13510_1744191999}[：尝试清除本地]{style="font-family:宋体"}[LSP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[protocol-support]{lang="EN-US"}**]{#struct_0_x1984_13510_100203425}[：报文协议支持类型不匹配。]{style="font-family:宋体"}

[**[rejected-adjacency]{lang="EN-US"}**]{#struct_0_x1984_13510_x1870006695}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文邻接不匹配丢弃。]{style="font-family:宋体"}

[**[skip-sequence-number]{lang="EN-US"}**]{#struct_0_x1984_13510_x1528286433}[：跳过已经产生过的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[序列号。]{style="font-family:宋体"}

[**[version-skew]{lang="EN-US"}**]{#struct_0_x1984_13510_x817804681}[：]{style="font-family:宋体"}[Hello]{lang="EN-US"}[报文版本号不匹配。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x275143275}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定任何参数，将开启]{style="font-family:宋体"}]{#struct_0_x1984_13510_x104368494}[IS-IS]{lang="EN-US"}[所有类型的告警功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置时不存在任何]{style="font-family:宋体"}]{#struct_0_x1984_13510_897160674}[IS-IS]{lang="EN-US"}[进程，将会提示无]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程，并不允许配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果删除了所有配置的]{style="font-family:宋体"}]{#struct_0_x1984_13510_1751779828}[IS-IS]{lang="EN-US"}[进程，则本功能不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1665697545}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x170163262}[关闭]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_2044098193}

[\[Sysname\] undo snmp-agent trap enable isis]{lang="EN-US"}
:::

::: {#-1230299672 .myid}
[]{#_Toc404788430}[]{#struct_0_x1984_13510_2101206054}

**IS-IS \-- IS-IS配置命令 \-- summary**

------------------------------------------------------------------------

[**[summary]{lang="EN-US"}**]{#struct_0_x1984_13510_1191837786}[命令用来配置一条聚合路由。]{style="font-family:宋体"}

[**[undo summary]{lang="EN-US"}**]{#struct_0_x1984_13510_x402011064}[命令用来删除指定的聚合路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2131008233}

[**[summary ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[{ *mask-length* \| *mask* } \[ **avoid-feedback** \| **generate_null0_route** \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_x1984_13510_x1541328370}

[**[undo summary ]{lang="EN-US"}***[ip-address ]{lang="EN-US"}*[{ *mask-length* \| *mask* } \[ **level-1** \| **level-1-2** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_1665763081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x891440829}

[[没有对路由进行聚合。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1239275993}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x894216223}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_835784375}[单播地址族视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1648172586}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x207257689}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x661238135}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_566066120}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1984_13510_1665828617}[：聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1984_13510_293580268}[：聚合路由的网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x1984_13510_99414224}[：聚合路由的网络掩码，点分十进制格式。]{style="font-family:宋体"}

[**[avoid-feedback]{lang="EN-US"}**]{#struct_0_x1984_13510_1647922119}[：避免通过路由计算学习到聚合路由。]{style="font-family:宋体"}

[**[generate_null0_route]{lang="EN-US"}**]{#struct_0_x1984_13510_847337847}[：为防止路由循环而生成]{style="font-family:宋体"}[NULL0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_1089645082}[：只对引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由进行聚合。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1984_13510_649969215}[：对引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由都进行聚合。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_1692946633}[：只对[]{#_Hlt9934357}引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由进行聚合。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_x1984_13510_1665894153}[：管理标记，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x531421900}

[[如果不输入]{style="font-family:宋体"}**[level]{lang="EN-US"}**]{#struct_0_x1984_13510_x1532662281}[参数，则默认只对]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[的路由进行聚合。]{style="font-family:宋体"}

[[如果没有指定拓扑名，则只对标准拓扑的路由进行聚合。]{style="font-family:宋体"}]{#struct_0_x1984_13510_x1860433745}

[[通过路由聚合，一方面可以减小路由表规模，还可以减少本路由器生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1874271021}[报文大小和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的规模。其中，被聚合的路由可以是]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议发现的路由，也可以是引入的外部路由。另外，聚合后路由的开销值取所有被聚合路由中最小的开销值。]{style="font-family:宋体"}

[[需要注意的是，路由器只对本地生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1790787412}[中的路由进行聚合。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x692552762}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x342672171}[配置一条]{style="font-family:宋体"}[202.0.0.0/8]{lang="EN-US"}[的聚合路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1665435401}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-1-ipv4\]]{lang="EN-US"}[ summary 202.0.0.0 255.0.0.0]{lang="EN-US"}[]{#_Hlt12072832}
:::

::: {#408390348 .myid}
[]{#_Toc404788431}[]{#struct_0_x1984_13510_1025481294}[]{#_Toc310604373}[]{#_Toc290886817}[]{#_Toc252200793}[]{#_Toc163546309}

**IS-IS \-- IS-IS配置命令 \-- timer lsp-generation**

------------------------------------------------------------------------

[**[timer lsp-generation]{lang="EN-US"}**]{#struct_0_x1984_13510_x708990978}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成的时间间隔。]{style="font-family:宋体"}

[**[undo timer lsp-generation]{lang="EN-US"}**]{#struct_0_x1984_13510_x198577725}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x176055649}

[**[timer lsp-generation ]{lang="EN-US"}***[maximum-interval]{lang="EN-US"}*[ \[ *minimum-interval* \[ *incremental-interval* \] \] \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_1234263912}

[**[undo timer lsp-generation]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_x1984_13510_107776503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1079480954}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_1665500937}[重新生成的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x74296535}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1627829212}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1256633269}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1420576610}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_874203656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_890610114}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_1319285297}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_1665566473}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_x530182457}[：网络拓扑变化导致]{style="font-family:宋体"}[LSP]{lang="EN-US"}[重新生成时，]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成的]{style="font-family:宋体"}[时间间隔惩罚增量]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1984_13510_355126080}[：配置]{style="font-family:宋体"}[Level-1 LSP]{lang="EN-US"}[生成时间间隔。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1984_13510_x1036903348}[：配置]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[生成时间间隔，默认不配置级别时对]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[同时起作用。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_702759850}

[[通过调节]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x2005811569}[重新生成的时间间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。在网络变化不频繁的情况下，将]{style="font-family:宋体"}[LSA]{lang="EN-US"}[重新生成时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_1034086055}[和]{style="font-family:宋体"}*[incremental-interva]{lang="EN-US"}*[l]{lang="EN-US"}[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x168154136}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_153350956}[配置]{style="font-family:宋体"}[IS-IS LSP]{lang="EN-US"}[重新生成的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_1665632009}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] timer lsp-generation 10 100 200]{lang="EN-US"}
:::

::: {#490996559 .myid}
[]{#_Toc404788432}[]{#struct_0_x1984_13510_663567551}

**IS-IS \-- IS-IS配置命令 \-- timer lsp-max-age**

------------------------------------------------------------------------

[**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1984_13510_x953962649}[命令用来配置当前路由器生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间。]{style="font-family:宋体"}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1984_13510_747112884}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1482983802}

[**[timer lsp-max-age ]{lang="EN-US"}***[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1984_13510_1586208387}

[**[undo timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1984_13510_386323155}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1666221833}

[[当前路由器生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_186370215}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[1200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1017889626}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x1383074474}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x540937750}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x1175270746}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_883033610}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2146482737}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1984_13510_x1368874942}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1666287369}

[[每个]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x693140404}[都有一个最大生存时间，随着时间的推移最大生存时间将逐渐减小，当]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[时，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[将启动清除过期]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的过程。用户可根据网络规模对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间进行调整。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_414918049}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_80424569}[配置当前路由器生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[在]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[里的最大生存时间为]{style="font-family:宋体"}[25]{lang="EN-US"}[分钟，即]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_370899260}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] timer lsp-max-age 1500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2079837910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1984_13510_x1421266335}
:::

::: {#-1091829735 .myid}
[]{#_Toc404788433}[]{#struct_0_x1984_13510_1665697546}[]{#_Toc297189190}[]{#_Toc290886819}[]{#_Toc252200795}[]{#_Toc163546311}[]{#_Toc50204123}[]{#_Toc33866122}

**IS-IS \-- IS-IS配置命令 \-- timer lsp-refresh**

------------------------------------------------------------------------

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1984_13510_x170359870}[命令用来配置]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期。]{style="font-family:宋体"}

[**[undo timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1984_13510_x632756046}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x840304253}

[**[timer lsp-refresh ]{lang="EN-US"}***[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1984_13510_972177030}

[**[undo]{lang="EN-US"}**[ **timer lsp-refresh**]{lang="EN-US"}]{#struct_0_x1984_13510_1638617510}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x870336760}

[[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_794082758}[刷新周期为]{style="font-family:宋体"}[900]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2497463}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1665763082}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x891506365}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x496103618}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1086441426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2001660811}

[*[second]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_x1984_13510_x1303832660}[：]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65534]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1932584004}

[[路由器必须定时刷新自己生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_x1984_13510_x1278393844}[，防止]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的最大生存时间减小为]{style="font-family:宋体"}[0]{lang="EN-US"}[。另外，通过定时刷新]{style="font-family:宋体"}[LSP]{lang="EN-US"}[可以使整个区域中的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[保持同步。用户可对]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新周期进行配置，提高]{style="font-family:宋体"}[LSP]{lang="EN-US"}[的刷新频率可以加快网络收敛速度，但是将占用更多的带宽。]{style="font-family:宋体"}

[**[timer lsp-refresh]{lang="EN-US"}**]{#struct_0_x1984_13510_1048956943}[命令配置的时间必须小于]{style="font-family:宋体"}**[timer lsp-max-age]{lang="EN-US"}**[命令配置的时间，以保证在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[失效前进行刷新。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1665828618}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_294563308}[配置当前系统的]{style="font-family:宋体"}[LSP]{lang="EN-US"}[刷新周期为]{style="font-family:宋体"}[1500]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_2066531060}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] timer lsp-refresh 1500]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2133441547}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer lsp-max-age]{lang="EN-US"}**]{#struct_0_x1984_13510_1301320831}
:::

::: {#1171776781 .myid}
[]{#_Toc404788434}[]{#struct_0_x1984_13510_x1647565808}[]{#_Toc297189191}[]{#_Toc290886820}[]{#_Toc252200796}[]{#_Toc163546312}[]{#_Toc50204124}[]{#_Toc33866123}

**IS-IS \-- IS-IS配置命令 \-- timer spf**

------------------------------------------------------------------------

[**[timer spf]{lang="EN-US"}**]{#struct_0_x1984_13510_1031821754}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算[的时间间隔]{#_Hlt23147082}。]{style="font-family:宋体"}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_x1984_13510_101228411}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1665894154}

[**[timer spf ]{lang="EN-US"}***[maximum-interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_x1984_13510_x531618508}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_x1984_13510_x1987999828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x1084597178}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_498690125}[路由计算的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1917179324}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_1832400193}[视图]{style="font-family:宋体"}[/IS-IS IPv4]{lang="EN-US"}[单播拓扑视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x717089634}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1665435402}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_1025546830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2085964294}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_1728068619}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_x874850120}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_x1016069371}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2084554195}

[[根据本地维护的]{style="font-family:宋体"}]{#struct_0_x1984_13510_2117350464}[LSDB]{lang="EN-US"}[，运行]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的路由器通过]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节]{style="font-family:宋体"}[SPF]{lang="EN-US"}[的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。]{style="font-family:宋体"}

[[本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到]{style="font-family:宋体"}]{#struct_0_x1984_13510_1356134399}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_x1984_13510_1665500938}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x73575639}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_x1975322234}[配置路由器]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x136136722}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] timer spf 10 100 300]{lang="EN-US"}
:::

::: {#-1660379657 .myid}
[]{#_Toc404788435}[]{#struct_0_x1984_13510_2109029973}[]{#_Toc357599211}[]{#_Toc352311298}

**IS-IS \-- IS-IS配置命令 \-- topology**

------------------------------------------------------------------------

[**[topology]{lang="EN-US"}**]{#struct_0_x1984_13510_2109095509}[命令用来创建并进入]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[单播拓扑视图。]{style="font-family:宋体"}

[**[undo topology]{lang="EN-US"}**]{#struct_0_x1984_13510_2109161045}[命令用来删除该视图下的所有配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2109226581}

[**[topology ]{lang="EN-US"}***[topo-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **tid** *tid* \]]{lang="EN-US"}]{#struct_0_x1984_13510_2109292117}

[**[undo topology ]{lang="EN-US"}***[topo-name]{lang="EN-US"}*]{#struct_0_x1984_13510_2109357653}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2108767826}

[[没有创建]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_2108833362}[单播拓扑视图。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2108898898}

[[IS-IS IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_2108964434}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2109029970}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_2109095506}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_2109161042}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2109226578}

[*[topo-name]{lang="EN-US"}*]{#struct_0_x1984_13510_2109292114}[：拓扑名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[tid]{lang="EN-US"}*]{#struct_0_x1984_13510_2109357650}[：拓扑号，取值范围为]{style="font-family:宋体"}[6]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2108767827}

[[拓扑名]{style="font-family:宋体"}**[base]{lang="EN-US"}**]{#struct_0_x1984_13510_2108833363}[已经为标准拓扑保留，在此处不能配置。]{style="font-family:宋体"}

[[本命令必须在配置了对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1984_13510_2108898899}[子拓扑后才能生效。]{style="font-family:宋体"}

[[本命令必须在链路开销值类型为]{style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_x1984_13510_2108964435}**[、]{style="font-family:宋体"}[compatible]{lang="EN-US"}**[或]{style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时才能配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2109029971}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_2109161043}[创建并进入]{style="font-family:宋体"}[IS-IS IPv4]{lang="EN-US"}[单播拓扑]{style="font-family:宋体"}[voice]{lang="EN-US"}[（]{style="font-family:宋体"}[4000]{lang="EN-US"}[）视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_2109226579}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv4]{lang="EN-US"}

[\[Sysname-isis-100-ipv4\] topology voice tid 4000]{lang="EN-US"}

[\[Sysname-isis-100-ipv4-topo-voice\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2109292115}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_x1984_13510_2109357651}
:::

::: {#1347731002 .myid}
[]{#_Toc404788436}[]{#struct_0_x1984_13510_x904529704}[]{#_Toc310604377}[]{#_Toc290886821}[]{#_Toc252200797}[]{#_Toc163546313}[]{#_Toc94930894}[]{#_Toc94586626}[]{#_Toc60036242}[]{#_Toc53707186}[]{#_Toc53487882}

**IS-IS \-- IS-IS配置命令 \-- virtual-system**

------------------------------------------------------------------------

[**[virtual-system]{lang="EN-US"}**]{#struct_0_x1984_13510_1790970550}[命令用来配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的虚拟系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo virtual-system]{lang="EN-US"}**]{#struct_0_x1984_13510_x63481976}[命令用来删除虚拟系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1984_13510_930878289}

[**[virtual-system]{lang="EN-US"}**[ *virtual-system-id*]{lang="EN-US"}]{#struct_0_x1984_13510_1665566474}

[**[undo virtual-system]{lang="EN-US"}**[ *virtual-system-id*]{lang="EN-US"}]{#struct_0_x1984_13510_x529723705}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1984_13510_2037735243}

[[没有配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_915259768}[进程的虚拟系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1984_13510_x2075389359}

[[IS-IS]{lang="EN-US"}]{#struct_0_x1984_13510_x728948055}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1984_13510_283551375}

[[network-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x461210277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1984_13510_x513138533}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1984_13510_1665632010}

[*[virtual-system-id]{lang="EN-US"}*]{#struct_0_x1984_13510_664026304}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的虚拟系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1984_13510_37597559}

[[\# ]{lang="EN-US"}]{#struct_0_x1984_13510_388353550}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的虚拟系统]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[2222.2222.2222]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1984_13510_x1552435620}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] virtual-system 2222.2222.2222]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
