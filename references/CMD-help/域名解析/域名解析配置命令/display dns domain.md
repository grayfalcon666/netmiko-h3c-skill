::: {#2055245683 .myid}
[]{#_Toc404786327}[]{#struct_0_13682_x1065_x838232389}[]{#_Toc297536641}

**域名解析 \-- 域名解析配置命令 \-- display dns domain**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dns** **domain**]{lang="EN-US"}]{#struct_0_13682_x1065_1199819551}[命令用来显示域名后缀信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x906478027}

[**[display]{lang="EN-US"}**[ **dns** **domain** \[ **dynamic** \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_899126844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1034629732}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232397530}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1735805072}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1387021209}

[[network-operator]{lang="EN-US"}]{#struct_0_13682_x1065_x67988030}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x308018430}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13682_x1065_88642903}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_712787162}

[**[dynamic]{lang="EN-US"}**]{#struct_0_13682_x1065_2122027003}[：显示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名后缀信息。如果不指定本参数，则显示静态配置和动态获得的域名后缀信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_800830148}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的域名后缀信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名后缀信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232331994}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1316314980}[显示公网静态配置和动态获得的域名后缀信息。]{style="font-family:宋体"}

[[\<Sysname\> display dns domain]{lang="EN-US"}]{#struct_0_13682_x1065_x1695230734}

[Type:]{lang="EN-US"}

[  D: Dynamic    S: Static]{lang="EN-US"}

[ ]{lang="EN-US"}

[No.    Type   Domain suffix]{lang="EN-US"}

[1      S      com]{lang="EN-US"}

[2      D      net]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display dns domain]{lang="EN-US"}]{#struct_0_13682_x1065_943601374}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1069662880}[[字段]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1382308030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13682_x1065_1197192514}

[[No.]{lang="EN-US"}]{#struct_0_13682_x1065_400781145}

[[序号]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232528602}

[[Type]{lang="EN-US"}]{#struct_0_13682_x1065_579320144}

[[域名后缀类型：]{style="font-family:宋体"}]{#struct_0_13682_x1065_1759171403}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_13682_x1065_x1769426858}[：表示静态配置的域名后缀]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_13682_x1065_x461720714}[：表示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名后缀]{style="font-family:宋体"}

[[Domain suffix]{lang="EN-US"}]{#struct_0_13682_x1065_675488104}

[[域名后缀]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232463066}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x969570000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_13682_x1065_1078468901}

::: {#-1358964821 .myid}
[]{#_Toc404786328}[]{#struct_0_13682_x1065_516722603}[]{#_Toc297536642}

**域名解析 \-- 域名解析配置命令 \-- display dns host**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dns** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x820248919}[命令用来显示域名解析信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_826058125}

[**[display]{lang="EN-US"}**[ **dns** **host** \[ **ip** \| **ipv6** \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_790946214}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1576984506}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1951523672}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232659674}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_2130265359}

[[network-operator]{lang="EN-US"}]{#struct_0_13682_x1065_1458422094}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_142424926}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13682_x1065_2130595223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x899038796}

[**[ip]{lang="EN-US"}**]{#struct_0_13682_x1065_x1376419744}[：显示]{style="font-family:宋体"}[A]{lang="EN-US"}[类查询的信息。]{style="font-family:宋体"}[A]{lang="EN-US"}[类查询用来解析域名对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_13682_x1065_x1674437645}[：显示]{style="font-family:宋体"}[AAAA]{lang="EN-US"}[类查询的信息。]{style="font-family:宋体"}[AAAA]{lang="EN-US"}[类查询用来解析域名对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x689424640}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的域名解析信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名解析信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232594138}

[[如果不指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**]{#struct_0_13682_x1065_595477003}[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则显示所有查询类型的域名解析信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1011750071}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1531905227}[显示所有查询类型的域名解析信息。]{style="font-family:宋体"}

[[\<Sysname\> display dns host]{lang="EN-US"}]{#struct_0_13682_x1065_387435758}

[Type:]{lang="EN-US"}

[  D: Dynamic    S: Static]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total number: 3]{lang="EN-US"}

[No.  Host name         Type  TTL        Query type   IP addresses]{lang="EN-US"}

[1    sample.com        D     3132       A            192.168.10.1]{lang="PT-BR"}

[                                                     192.168.10.2]{lang="PT-BR"}

[                                                     192.168.10.3]{lang="PT-BR"}

[2    zig.sample.com    S     -          A            192.168.1.1]{lang="PT-BR"}

[3    sample.net        S     -          AAAA         FE80::4904:4448]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display dns host]{lang="EN-US"}]{#struct_0_13682_x1065_507081523}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1042779357}[[字段]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232790746}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1756621634}

[[No.]{lang="EN-US"}]{#struct_0_13682_x1065_x1633516103}

[[序号]{style="font-family:宋体"}]{#struct_0_13682_x1065_x189507871}

[[Host name]{lang="EN-US"}]{#struct_0_13682_x1065_815571615}

[[查询名称]{style="font-family:宋体"}]{#struct_0_13682_x1065_x233733392}

[[Type]{lang="EN-US"}]{#struct_0_13682_x1065_1395545946}

[[域名解析信息的类型：]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232725210}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_13682_x1065_228380084}[：表示静态配置的域名解析信息，即通过]{style="font-family:宋体"}**[ip host]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ipv6 host]{lang="EN-US"}**[命令配置的]{style="font-family:宋体"}[主机名及其对应的主机]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[/IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_13682_x1065_1385327085}[：表示通过动态域名解析获得的域名解析信息]{style="font-family:宋体"}

[[TTL]{lang="EN-US"}]{#struct_0_13682_x1065_x1726950050}

[[域名解析信息的剩余有效时间，单位为秒]{style="font-family:宋体"}]{#struct_0_13682_x1065_169415235}

[[静态信息的]{style="font-family:宋体"}[TTL]{lang="EN-US"}]{#struct_0_13682_x1065_x73699494}[值显示为"]{style="font-family:宋体"}[-]{lang="EN-US"}["]{style="font-family:宋体"}

[[Query type]{lang="EN-US"}]{#struct_0_13682_x1065_1232921818}

[[查询类型，取值包括]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_13682_x1065_641769306}[和]{style="font-family:宋体"}[AAAA]{lang="EN-US"}

[[IP addresses]{lang="EN-US"}]{#struct_0_13682_x1065_x1849587549}

[[主机名对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_13682_x1065_1117064706}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13682_x1065_972085137}[A]{lang="EN-US"}[类查询类型，为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1089485039}[AAAA]{lang="EN-US"}[类查询类型，为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232856282}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **dns** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x190043419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**[ **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x1561475217}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**[ **host**]{lang="EN-US"}]{#struct_0_13682_x1065_2146874104}

::: {#-355258723 .myid}
[]{#_Toc205698750}[]{#_Toc135535816}[]{#_Toc78335384}[]{#_Toc37741852}[]{#_Toc404786329}[]{#struct_0_13682_x1065_x514432031}[]{#_Toc297536659}

**域名解析 \-- 域名解析配置命令 \-- display dns server**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x366089879}[命令用来显示域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x115019744}

[**[display]{lang="EN-US"}**[ **dns** **server** \[ **dynamic** \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1702100494}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232397531}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1735739536}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_608966843}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1237797906}

[[network-operator]{lang="EN-US"}]{#struct_0_13682_x1065_x1555217334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1928145478}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13682_x1065_490853875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1600146459}

[**[dynamic]{lang="EN-US"}**]{#struct_0_13682_x1065_x1118973882}[：显示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。如果不指定本参数，则显示静态配置和动态获得的域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_1232331995}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1316249444}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1476148270}[显示公网的域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display dns server]{lang="EN-US"}]{#struct_0_13682_x1065_1224675566}

[Type:]{lang="EN-US"}

[  D: Dynamic    S: Static]{lang="EN-US"}

[ ]{lang="EN-US"}

[No. Type  IP address]{lang="EN-US"}

[1   S     202.114.0.124]{lang="EN-US"}

[2   S     169.254.65.125]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display dns server]{lang="EN-US"}]{#struct_0_13682_x1065_x1229269561}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1040433378}[[字段]{style="font-family:黑体"}]{#struct_0_13682_x1065_1928866074}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13682_x1065_x307541593}

[[No.]{lang="EN-US"}]{#struct_0_13682_x1065_1232528603}

[[域名服务器的序号，系统自动给所配置的服务器编号，从]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_13682_x1065_579254608}[开始]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_13682_x1065_x201445061}

[[域名服务器类型]{style="font-family:宋体"}]{#struct_0_13682_x1065_846608495}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_13682_x1065_x2055061562}[表示静态指定的域名服务器信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_13682_x1065_x269218752}[表示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名服务器信息]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_13682_x1065_1232463067}

[[域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_x969635536}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1258657654}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**[ **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x1803526455}

::: {#1408131088 .myid}
[]{#_Toc404786330}[]{#struct_0_13682_x1065_x1344181575}[]{#_Toc297536665}[]{#_Toc296694482}[]{#_Toc297536644}[]{#_Toc296694483}[]{#_Toc297536645}

**域名解析 \-- 域名解析配置命令 \-- display ipv6 dns server**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipv6** **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x1062996250}[命令用来显示域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x454065891}

[**[display]{lang="EN-US"}**[ **ipv6** **dns** **server** \[ **dynamic** \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1840665963}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232659675}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_2130330895}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1264777218}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_465823107}

[[network-operator]{lang="EN-US"}]{#struct_0_13682_x1065_x1558471763}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_836011626}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13682_x1065_1355819292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x835890099}

[**[dynamic]{lang="EN-US"}**]{#struct_0_13682_x1065_x1980570850}[：显示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。如果不指定本参数，则显示静态配置和动态获得的域名服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_1232594139}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的域名服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则显示公网的域名服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_595542539}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x909259391}[显示公网域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 dns server]{lang="EN-US"}]{#struct_0_13682_x1065_x1245115862}

[Type:]{lang="EN-US"}

[  D: Dynamic    S: Static]{lang="EN-US"}

[ ]{lang="EN-US"}

[No. Type  IPv6 address                             Outgoing Interface]{lang="EN-US"}

[1   S     2::2]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display ipv6 dns server]{lang="EN-US"}]{#struct_0_13682_x1065_x1713060573}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1047275652}[[字段]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1678751653}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13682_x1065_286289844}

[[No.]{lang="EN-US"}]{#struct_0_13682_x1065_1232790747}

[[域名服务器的序号]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1756556098}

[[Type]{lang="EN-US"}]{#struct_0_13682_x1065_1384421462}

[[域名服务器类型]{style="font-family:宋体"}]{#struct_0_13682_x1065_1385950087}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_13682_x1065_x1316784557}[表示静态指定的域名服务器信息]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_13682_x1065_373088350}[表示通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[等协议动态获得的域名服务器信息]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_13682_x1065_x139755573}

[[域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13682_x1065_1232725211}[地址]{style="font-family:宋体"}

[[Outgoing Interface]{lang="EN-US"}]{#struct_0_13682_x1065_228314548}

[[出接口名]{style="font-family:宋体"}]{#struct_0_13682_x1065_135246239}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1668496222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x1625485589}

::: {#1911007910 .myid}
[]{#_Toc404786331}[]{#struct_0_13682_x1065_1130609408}[]{#_Toc297536646}

**域名解析 \-- 域名解析配置命令 \-- dns domain**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **domain**]{lang="EN-US"}]{#struct_0_13682_x1065_1423525142}[命令用来添加域名后缀。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **domain**]{lang="EN-US"}]{#struct_0_13682_x1065_1232921819}[命令用来删除指定的域名后缀。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_641703770}

[**[dns]{lang="EN-US"}**[ **domain** *domain-name* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1298291771}

[**[undo]{lang="EN-US"}**[ **dns** **domain** *domain-name* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1280056235}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1920574107}

[[没有配置域名后缀，即只根据用户输入的域名信息进行解析。]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1781148177}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1077271831}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_284410027}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x458279187}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1232856283}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x189977883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_804627240}

[*[domain-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x718834581}[：域名后缀，由"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成（如]{style="font-family:宋体"}[aabbcc.com]{lang="EN-US"}[），每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符。不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["或"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_1115792788}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[添加或删除域名后缀。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网添加或删除域名后缀。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x509273210}

[[域名解析时，用户只需要输入域名的部分字段，系统会按照域名后缀配置的先后顺序，依次将输入的域名加上不同的域名后缀进行解析。]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1195213787}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_2068998150}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置的域名后缀同时用于]{style="font-family:宋体"}]{#struct_0_13682_x1065_1972085029}[IPv4]{lang="EN-US"}[域名解析和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[域名解析。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或每个]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232397528}[VPN]{lang="EN-US"}[内最多可以配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个域名后缀。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置域名后缀。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1735280785}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x594659957}[为公网添加一个域名后缀]{style="font-family:宋体"}[com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1079839992}

[\[Sysname\] dns domain com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1803937133}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dns** **domain**]{lang="EN-US"}]{#struct_0_13682_x1065_x182367247}
:::

::: {#-47976022 .myid}
[]{#_Toc404786332}[]{#struct_0_13682_x1065_2041946718}

**域名解析 \-- 域名解析配置命令 \-- dns dscp**

------------------------------------------------------------------------

[**[dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_2046327401}[命令用来配置发送]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_1232331992}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1315921764}

[**[dns dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_1229625386}

[**[undo dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_x333654571}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1573064810}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1277298547}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2122542987}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1231936448}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1020413595}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232528600}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_579451216}[：]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_85876445}

[[DSCP]{lang="EN-US"}]{#struct_0_13682_x1065_x1893778712}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。]{style="font-family:宋体"}

[[通过本命令可以指定]{style="font-family:宋体"}]{#struct_0_13682_x1065_1066099688}[DNS]{lang="EN-US"}[客户端或]{style="font-family:宋体"}[DNS proxy]{lang="EN-US"}[发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1383193721}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1531027340}[配置发送的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x783763635}

[\[Sysname\] dns dscp 30]{lang="EN-US"}
:::

::: {#-1926443553 .myid}
[]{#_Toc135535819}[]{#_Toc78335387}[]{#_Toc37741855}[]{#_Toc404786333}[]{#struct_0_13682_x1065_56545390}[]{#_Ref316055378}[]{#_Ref316055368}[]{#_Toc297536647}[]{#_Toc205698753}[]{#_Toc165380090}[]{#_Toc296694486}[]{#_Toc297536648}[]{#_Toc296694487}[]{#_Toc297536649}[]{#_Toc291089810}[]{#_Toc291089811}[]{#_Toc291089812}[]{#_Toc291089813}[]{#_Toc291089814}[]{#_Toc291089815}[]{#_Toc291089816}[]{#_Toc291089817}[]{#_Toc291089818}[]{#_Toc291089819}[]{#_Toc291089820}[]{#_Toc291089821}[]{#_Toc291089822}[]{#_Toc291089823}[]{#_Toc291089824}[]{#_Toc291089825}[]{#_Toc291089826}[]{#_Toc291089827}[]{#_Toc291089828}[]{#_Toc291089829}[]{#_Toc291089830}[]{#_Toc291089831}[]{#_Toc291089832}[]{#_Toc291089833}[]{#_Toc291089834}[]{#_Toc291089835}[]{#_Toc291089836}[]{#_Toc291089837}[]{#_Toc291089838}

**域名解析 \-- 域名解析配置命令 \-- dns proxy enable**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_1232463064}[命令用来开启]{style="font-family:宋体"}[DNS proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_x969438928}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x79987602}

[**[dns]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_1709707232}

[**[undo]{lang="EN-US"}**[ **dns** **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_981172566}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1251180707}

[[DNS proxy]{lang="EN-US"}]{#struct_0_13682_x1065_x1902828302}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_568786545}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1122391031}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232659672}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_2130396431}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1684791614}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_2103633714}

[[本命令的配置同时用于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_x95444207}[域名解析和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[域名解析。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x153220776}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x916262432}[开启]{style="font-family:宋体"}[DNS proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1445193922}

[\[Sysname\] dns proxy enable]{lang="EN-US"}
:::

::: {#501475818 .myid}
[]{#_Toc404786334}[]{#struct_0_13682_x1065_1897844506}[]{#_Toc297536660}[]{#_Toc205698755}[]{#_Toc135535820}[]{#_Toc78335388}[]{#_Toc37741856}[]{#_Toc296694489}[]{#_Toc297536651}[]{#_Toc296694490}[]{#_Toc297536652}[]{#_Toc309120017}[]{#_Toc309120235}[]{#_Toc309120018}[]{#_Toc309120236}[]{#_Toc309120019}[]{#_Toc309120237}[]{#_Toc309120020}[]{#_Toc309120238}[]{#_Toc309120021}[]{#_Toc309120239}[]{#_Toc309120022}[]{#_Toc309120240}[]{#_Toc309120023}[]{#_Toc309120241}[]{#_Toc309120024}[]{#_Toc309120242}[]{#_Toc309120025}[]{#_Toc309120243}[]{#_Toc309120026}[]{#_Toc309120244}[]{#_Toc309120027}[]{#_Toc309120245}[]{#_Toc309120028}[]{#_Toc309120246}[]{#_Toc309120029}[]{#_Toc309120247}[]{#_Toc309120030}[]{#_Toc309120248}[]{#_Toc309120031}[]{#_Toc309120249}[]{#_Toc309120032}[]{#_Toc309120250}[]{#_Toc309120033}[]{#_Toc309120251}[]{#_Toc309120034}[]{#_Toc309120252}[]{#_Toc309120035}[]{#_Toc309120253}[]{#_Toc309120036}[]{#_Toc309120254}[]{#_Toc309120037}[]{#_Toc309120255}[]{#_Toc309120038}[]{#_Toc309120256}[]{#_Toc309120039}[]{#_Toc309120257}[]{#_Toc309120040}[]{#_Toc309120258}[]{#_Toc309120041}[]{#_Toc309120259}[]{#_Toc309120042}[]{#_Toc309120260}[]{#_Toc309120043}[]{#_Toc309120261}[]{#_Toc296694492}[]{#_Toc297536654}[]{#_Toc296694493}[]{#_Toc297536655}

**域名解析 \-- 域名解析配置命令 \-- dns server**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **server**]{lang="EN-US"}]{#struct_0_13682_x1065_1232594136}[命令用来配置域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_595083787}[命令用来删除域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1328144997}

[**[dns]{lang="EN-US"}**[ **server** *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1772118350}

[**[undo]{lang="EN-US"}**[ **dns** **server** \[ *ip-address* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1899728914}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_529052533}

[[没有配置域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_429237726}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2046248928}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_334109168}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232790744}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1756490562}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1823739987}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x61190934}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13682_x1065_1077150522}[：域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x1614990106}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置或删除域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置或删除域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_192598113}

[[在进行动态域名解析时，系统按照域名服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_1188144979}[地址配置的先后顺序，依次向各个域名服务器发送查询请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_796019138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或单个]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232725208}[VPN]{lang="EN-US"}[内最多可以配置]{style="font-family:宋体"}[6]{lang="EN-US"}[个域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_13682_x1065_227855795}**[undo]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}[命令时如果不指定]{style="font-family:宋体"}*[ip-ad]{lang="EN-US"}[dress]{lang="EN-US"}*[参数]{style="font-family:
宋体"}[，则删除公网或指定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[中的所有域名服务器]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1493135283}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1007962537}[配置域名服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[172.16.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1953529452}

[\[Sysname\] dns server 172.16.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x72199000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x669777476}
:::

::: {#605696231 .myid}
[]{#_Toc404786335}[]{#struct_0_13682_x1065_1533235620}[]{#_Toc297536650}[]{#_Hlt26066436}[]{#_Toc135132382}[]{#_Toc135132383}[]{#_Toc135132385}[]{#_Toc135132386}[]{#_Toc135132387}[]{#_Toc135132388}[]{#_Toc135132389}[]{#_Toc135132390}[]{#_Toc135132391}[]{#_Toc135132392}[]{#_Toc135132393}[]{#_Toc135132394}[]{#_Toc135132395}[]{#_Toc135132397}[]{#_Hlt26780462}[]{#_Toc135132398}[]{#_Toc135132399}[]{#_Toc135132401}[]{#_Toc135132403}[]{#_Toc200958118}[]{#_Toc200958283}[]{#_Toc202082409}[]{#_Toc202082458}[]{#_Toc200958119}[]{#_Toc200958284}[]{#_Toc202082410}[]{#_Toc202082459}[]{#_Toc200958120}[]{#_Toc200958285}[]{#_Toc202082411}[]{#_Toc202082460}[]{#_Toc200958121}[]{#_Toc200958286}[]{#_Toc202082412}[]{#_Toc202082461}[]{#_Toc200958122}[]{#_Toc200958287}[]{#_Toc202082413}[]{#_Toc202082462}[]{#_Toc200958123}[]{#_Toc200958288}[]{#_Toc202082414}[]{#_Toc202082463}[]{#_Toc200958124}[]{#_Toc200958289}[]{#_Toc202082415}[]{#_Toc202082464}[]{#_Toc200958125}[]{#_Toc200958290}[]{#_Toc202082416}[]{#_Toc202082465}[]{#_Toc200958126}[]{#_Toc200958291}[]{#_Toc202082417}[]{#_Toc202082466}[]{#_Toc200958127}[]{#_Toc200958292}[]{#_Toc202082418}[]{#_Toc202082467}[]{#_Toc200958128}[]{#_Toc200958293}[]{#_Toc202082419}[]{#_Toc202082468}[]{#_Toc200958129}[]{#_Toc200958294}[]{#_Toc202082420}[]{#_Toc202082469}[]{#_Toc200958130}[]{#_Toc200958295}[]{#_Toc202082421}[]{#_Toc202082470}[]{#_Toc200958131}[]{#_Toc200958296}[]{#_Toc202082422}[]{#_Toc202082471}[]{#_Toc200958134}[]{#_Toc200958299}[]{#_Toc202082425}[]{#_Toc202082474}[]{#_Toc200958135}[]{#_Toc200958300}[]{#_Toc202082426}[]{#_Toc202082475}[]{#_Toc200958154}[]{#_Toc200958319}[]{#_Toc202082445}[]{#_Toc202082494}

**域名解析 \-- 域名解析配置命令 \-- dns source-interface**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **source-interface**]{lang="EN-US"}]{#struct_0_13682_x1065_1232921816}[命令用来指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的源接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **source-interface**]{lang="EN-US"}]{#struct_0_13682_x1065_642424666}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1352651547}

[**[dns]{lang="EN-US"}**[ **source-interface** *interface-type* *interface-number* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1040141290}

[**[undo]{lang="EN-US"}**[ **dns** **source-interface** *interface-type* *interface-number* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x592855651}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1993112458}

[[设备根据]{style="font-family:宋体"}[DNS server]{lang="EN-US"}]{#struct_0_13682_x1065_x1869327898}[的地址，通过路由表查找报文的出接口，并将该出接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为发送到该服务器的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[查询报文的源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_444325237}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_75056614}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232856280}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x189912347}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_859266069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1582206454}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_13682_x1065_381851232}[：源接口的接口类型和接口编号。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x840756268}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的源接口。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的源接口。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x192195123}

[[通过本命令指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_13682_x1065_987530097}[报文的源接口后，系统将选择指定接口的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或根据]{style="font-family:宋体"}[RFC 3484]{lang="EN-US"}[中定义的规则选择指定接口的某个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，作为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[查询报文的源地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x2138287311}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13682_x1065_1232397529}[的]{style="font-family:宋体"}[配置同时用于]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[域名解析和]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[域名解析。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或每个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1735215249}[VPN]{lang="EN-US"}[内只能配置]{style="font-family:宋体"}[1]{lang="EN-US"}[个源接口。重复配置时，新的配置会覆盖原有配置。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置源接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[无论配置的源接口是否属于指定的]{style="font-family:宋体"}]{#struct_0_13682_x1065_1672206465}[VPN]{lang="EN-US"}[，该配置都会生效。不建议将不属于]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的接口配置为该]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的源接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1820462868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_1615169389}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1628255546}[指定公网]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_2129450580}

[\[Sysname\] dns source-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1970460709}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1232331993}[指定公网]{style="font-family:宋体"}[DNS]{lang="EN-US"}[报文的源接口为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1315856228}

[\[Sysname\] dns source-interface vlan-interface 2]{lang="EN-US"}
:::

::: {#-737607636 .myid}
[]{#_Toc404786336}[]{#struct_0_13682_x1065_x1057007244}[]{#_Toc297536661}

**域名解析 \-- 域名解析配置命令 \-- dns spoofing**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **spoofing**]{lang="EN-US"}]{#struct_0_13682_x1065_x50839321}[命令用来开启欺骗性应答域名解析请求（]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[）功能，并指定应答的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **spoofing**]{lang="EN-US"}]{#struct_0_13682_x1065_1521843332}[命令关闭]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1404866731}

[**[dns]{lang="EN-US"}**[ **spoofing** *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x702280679}

[**[undo]{lang="EN-US"}**[ **dns** **spoofing** *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1281167174}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_809618021}

[[DNS spoofing]{lang="EN-US"}]{#struct_0_13682_x1065_1232528601}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_579385680}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x948949130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1699228453}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x341789669}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_2007444194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1019931218}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13682_x1065_590516068}[：用来欺骗性应答域名解析请求的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x2089348401}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232463065}

[[配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}]{#struct_0_13682_x1065_x969504464}[前，需要先开启]{style="font-family:宋体"}[DNS proxy]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[公网或每个]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_13682_x1065_201849177}[内只能配置]{style="font-family:宋体"}[1]{lang="EN-US"}[个]{style="font-family:宋体"}[DNS spoofing]{lang="FR"}[应答的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。重复配置时，新的配置会覆盖原有配置。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_604406924}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_2112110528}[开启公网的]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能，并指定应答的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1911359423}

[\[Sysname\] dns proxy enable]{lang="EN-US"}

[\[Sysname\] dns spoofing 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1700722619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_797981265}
:::

::::: {#-2106215514 .myid}
[]{#_Toc404786337}[]{#struct_0_13682_x1065_938309179}

**域名解析 \-- 域名解析配置命令 \-- dns spoofing track**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](域名解析命令.files/image001.png){#图片 4 width="63" height="25"}]{lang="EN-US"}]{#struct_0_13682_x1065_x836957796}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况和设备型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13682_x1065_1367049520}
:::

[ ]{lang="EN-US"}

[**[dns spoofing track]{lang="EN-US"}**]{#struct_0_13682_x1065_x879615087}[命令用来配置监视指定出接口的网络制式。]{style="font-family:宋体"}

[**[undo dns spoofing track]{lang="EN-US"}**]{#struct_0_13682_x1065_x2099552102}[命令用来取消对指定出接口的监视。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x506461078}

[**[dns spoofing track controller ]{lang="EN-US"}***[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_13682_x1065_x1791007229}

[**[undo dns spoofing track]{lang="EN-US"}**]{#struct_0_13682_x1065_x601382258}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x994244635}

[[未指定被监视的出接口。]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1754794004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_2093110380}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1641499603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x627774762}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1173868784}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x67764783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x929936954}

[**[controller ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13682_x1065_x322168700}[：指定被监视的出接口。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1404347821}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置监视指定出接口的网络制式]{lang="EN-US" style="font-family:宋体"}]{#struct_0_13682_x1065_2075558368}[时，需要先开启]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[DNS spoofing]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次配置该命令，新的配置会覆盖已有配置。]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1092647981}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_121981241}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_872749798}[配置监视指定出接口]{style="font-family:宋体"}[Cellular0/1]{lang="EN-US"}[的网络制式。如果该接口网络制式为]{style="font-family:宋体"}[2G]{lang="EN-US"}[，则以]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[192.168.1.10]{lang="EN-US"}[进行欺骗应答；如果该接口网络制式为]{style="font-family:宋体"}[3G/4G]{lang="EN-US"}[，则不进行欺骗应答。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_2101108593}

[\[Sysname\] dns proxy enable]{lang="EN-US"}

[\[Sysname\] dns spoofing 192.168.1.10]{lang="EN-US"}

[\[Sysname\] dns spoofing track controller cellular 0/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1576582119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns spoofing]{lang="EN-US"}**]{#struct_0_13682_x1065_x597942888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6 dns spoofing]{lang="EN-US"}**]{#struct_0_13682_x1065_484523355}
:::::

::: {#-2137155326 .myid}
[]{#_Toc404786338}[]{#struct_0_13682_x1065_1232659673}[]{#_Toc297536653}

**域名解析 \-- 域名解析配置命令 \-- dns trust-interface**

------------------------------------------------------------------------

[**[dns]{lang="EN-US"}**[ **trust-interface**]{lang="EN-US"}]{#struct_0_13682_x1065_2130461967}[命令用来指定]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dns** **trust-interface**]{lang="EN-US"}]{#struct_0_13682_x1065_x1657039743}[命令用来删除指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_503521362}

[**[dns]{lang="EN-US"}**[ **trust-interface** *interface-type* *interface-number*]{lang="EN-US"}]{#struct_0_13682_x1065_1375697138}

[**[undo]{lang="EN-US"}**[ **dns** **trust-interface** \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x722633783}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_344416114}

[[没有指定任何接口为信任接口。]{style="font-family:宋体"}]{#struct_0_13682_x1065_x86265900}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1740108105}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232594137}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_595149323}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_2067445441}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_181046994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x319212326}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_13682_x1065_x534452029}[：]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任接口的接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1680985034}

[[缺省情况下，任意接口通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}]{#struct_0_13682_x1065_x1978745518}[等协议动态获得的域名后缀和域名服务器信息都将作为有效信息，用于域名解析。如果网络攻击者通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器为设备分配错误的域名后缀和域名服务器地址，则会导致设备域名解析失败，或解析到错误的结果。通过本配置指定信任接口后，域名解析时只采用信任接口动态获得的域名后缀和域名服务器信息，非信任接口获得的信息不能用于域名解析，从而在一定程度上避免这类攻击。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_666946644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令同时用于]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_1232790745}[域名解析和]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[域名解析。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备最多可以配置]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1756425026}[128]{lang="EN-US"}[个信任接口。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **dns** **trust-interface**]{lang="EN-US"}]{#struct_0_13682_x1065_958438529}[命令时，]{style="font-family:
宋体"}[如果不指定]{lang="EN-US" style="font-family:宋体"}[任何]{style="font-family:宋体"}[接口，则删除]{lang="EN-US" style="font-family:宋体"}[所有的]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任]{style="font-family:宋体"}[接口]{lang="EN-US" style="font-family:宋体"}[，恢复到缺省状态]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1889149782}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_x752643235}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_600937720}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1605067667}

[\[Sysname\] dns trust-interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_1102676416}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x100397859}[指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[为]{style="font-family:宋体"}[DNS]{lang="EN-US"}[信任接口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1232725209}

[\[Sysname\] dns trust-interface vlan-interface 2]{lang="EN-US"}
:::

::: {#1184104728 .myid}
[]{#_Toc404786339}[]{#struct_0_13682_x1065_227790259}[]{#_Toc297536662}[]{#_Toc345157412}[]{#_Toc345157847}

**域名解析 \-- 域名解析配置命令 \-- ip host**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x587526038}[命令用来配置主机名及其对应的主机]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x27513343}[命令用来删除主机名及其对应的主机]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_290289302}

[**[ip]{lang="EN-US"}**[ **host** *host-name* *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1592369608}

[**[undo]{lang="EN-US"}**[ **ip** **host** *host-name* *ip-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x369737892}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x413380179}

[[静态域名解析表中不存在主机名及]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_13682_x1065_x838020541}[地址的对应关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232921817}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_642359130}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x71857615}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_710130614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1150225603}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1343913864}

[*[host-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x380711402}[：主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_13682_x1065_x681002584}[：与主机名对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x1901831481}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置主机名和]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置主机名和]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232856281}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或单个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x189846811}[VPN]{lang="EN-US"}[内最多可以配置]{style="font-family:宋体"}[1024]{lang="EN-US"}[个主机名和]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的对应关系。可以同时在公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内配置主机名和]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在公网或单个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1921962333}[VPN]{lang="EN-US"}[内，一个主机名只能对应一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。重复配置时，新的配置会覆盖原有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_13682_x1065_x1679457110}[、]{lang="EN-US" style="font-family:宋体"}**[-a]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-c]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-f]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-h]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-i]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-m]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-n]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-p]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-q]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-r]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-s]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-t]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-tos]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-v]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[-vpn-instance]{lang="EN-US"}**[已被系统用作]{lang="EN-US" style="font-family:宋体"}**[ping]{lang="EN-US"}**[命令的参数关键字，在配置主机名时，请避免使用相同的字符串作为主机名。]{lang="EN-US" style="font-family:宋体"}**[ping]{lang="EN-US"}**[命令支持的参数形式，请参考"网络管理和监控"中的"]{style="font-family:宋体"}**[ping]{lang="EN-US"}**["命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_209715129}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1779226423}[配置公网内主机名]{style="font-family:宋体"}[aaa]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x116657944}

[\[Sysname\] ip host aaa 10.110.0.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_580011902}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display dns host]{lang="EN-US"}**]{#struct_0_13682_x1065_x1254544328}
:::

::: {#1713149520 .myid}
[]{#_Toc404786340}[]{#struct_0_13682_x1065_x1707366703}

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns dscp**

------------------------------------------------------------------------

[**[ipv6 dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_1232397526}[命令用来配置发送]{style="font-family:宋体"}[IPv6 DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ipv6 dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_x1735674001}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x385738275}

[**[ipv6 dns dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_x1304059852}

[**[undo ipv6 dns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_x1991259249}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_2055385951}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1163514081}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1768760733}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_543314791}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1232331990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1316052836}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_x768631235}[：]{style="font-family:宋体"}[IPv6 DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1707054623}

[[DSCP]{lang="EN-US"}]{#struct_0_13682_x1065_1569388119}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。]{style="font-family:宋体"}

[[通过本命令可以指定]{style="font-family:宋体"}]{#struct_0_13682_x1065_1873784597}[IPv6 DNS]{lang="EN-US"}[客户端或]{style="font-family:宋体"}[DNS proxy]{lang="EN-US"}[发送的]{style="font-family:宋体"}[IPv6 DNS]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2067200245}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x731728510}[配置发送的]{style="font-family:宋体"}[IPv6 DNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x2129229940}

[\[Sysname\] ipv6 dns dscp 30]{lang="EN-US"}
:::

::: {#-1778905631 .myid}
[]{#struct_0_13682_x1065_1232528598}[]{#_Toc404786341}[]{#_Toc297536666}

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns server**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_x1759725223}[命令用来配置域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **dns** **server**]{lang="EN-US"}]{#struct_0_13682_x1065_553122419}[命令用来删除域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_396833269}

[**[ipv6]{lang="EN-US"}**[ **dns** **server** *ipv6-address* \[ *interface-type* *interface-number* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_315765800}

[**[undo]{lang="EN-US"}**[ **ipv6** **dns** **server** \[ *ipv6-address* \[ *interface-type* *interface-number* \] \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1913700777}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_139855051}

[[没有配置域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13682_x1065_1643993099}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1061867034}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232463062}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x969307856}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_235491621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_795827108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x851274058}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13682_x1065_x857333898}[：域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_13682_x1065_x83127200}[：指定报文的出接口的接口类型和接口编号。如果不指定本参数，则根据路由表查找报文的出接口。域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为链路本地地址时，必须指定本参数。域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为全球单播地址时，无法指定本参数。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x1384199385}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置或删除域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置或删除域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2134127237}

[[在进行动态域名解析时，系统按照域名服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13682_x1065_1828790943}[地址配置的先后顺序，依次向各个域名服务器发送查询请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232659670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或单个]{style="font-family:宋体"}]{#struct_0_13682_x1065_2130527503}[VPN]{lang="EN-US"}[内最多可以配置]{style="font-family:宋体"}[6]{lang="EN-US"}[个域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行]{style="font-family:宋体"}]{#struct_0_13682_x1065_x2046776596}**[undo]{lang="EN-US"}**[ **ipv6** **dns** **server**]{lang="EN-US"}[命令时如果不指定]{style="font-family:
宋体"}*[ipv6-address]{lang="EN-US"}*[参数]{style="font-family:宋体"}[，则删除公网或指定]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[中的所有域名服务器]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1524865323}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1585304840}[配置公网内域名服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2002::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x665630204}

[\[Sysname\] ipv6 dns server 2002::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x116186747}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipv6 dns server]{lang="EN-US"}**]{#struct_0_13682_x1065_1688451916}
:::

::: {#-314374767 .myid}
[]{#_Toc404786342}[]{#struct_0_13682_x1065_1232594134}[]{#_Toc297536667}

**域名解析 \-- 域名解析配置命令 \-- ipv6 dns spoofing**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **dns** **spoofing**]{lang="EN-US"}]{#struct_0_13682_x1065_595214859}[命令用来开启]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能，并指定应答的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **dns** **spoofing**]{lang="EN-US"}]{#struct_0_13682_x1065_x1622951729}[命令用来关闭]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1332256454}

[**[ipv6]{lang="EN-US"}**[ **dns** **spoofing** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1533465558}

[**[undo]{lang="EN-US"}**[ **ipv6** **dns** **spoofing** *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x611567308}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1899317016}

[[DNS spoofing]{lang="EN-US"}]{#struct_0_13682_x1065_138792300}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_507249072}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_2117346441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232790742}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1756883778}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x2115785426}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_210053961}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13682_x1065_1181888766}[：用来欺骗性应答域名解析请求的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x511389288}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x967179632}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1835153478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或每个]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232725206}[VPN]{lang="EN-US"}[内只能配置]{style="font-family:宋体"}[1]{lang="EN-US"}[个]{style="font-family:宋体"}[DNS spoofing]{lang="FR"}[应答]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。重复配置时，新的配置会覆盖原有配置。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令必须和]{style="font-family:宋体"}]{#struct_0_13682_x1065_228511155}**[dns proxy enable]{lang="EN-US"}**[命令一起使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_44556070}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x819993478}[为公网开启]{style="font-family:宋体"}[DNS spoofing]{lang="EN-US"}[功能，并指定应答的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1193839316}

[\[Sysname\] dns proxy enable]{lang="EN-US"}

[\[Sysname\] ipv6 dns spoofing 2001::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2008506667}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dns]{lang="EN-US"}**[ **proxy** **enable**]{lang="EN-US"}]{#struct_0_13682_x1065_881606980}
:::

::: {#-155829010 .myid}
[]{#_Toc404786343}[]{#struct_0_13682_x1065_x1854517525}[]{#_Toc297536668}

**域名解析 \-- 域名解析配置命令 \-- ipv6 host**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **host**]{lang="EN-US"}]{#struct_0_13682_x1065_1173826573}[命令用来配置主机名及其对应的主机]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_1232921814}[命令用来删除主机名及其对应的主机]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_642555738}

[**[ipv6]{lang="EN-US"}**[ **host** *host-name* *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x176250637}

[**[undo]{lang="EN-US"}**[ **ipv6** **host** *host-name* *ipv6-address* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_1636893146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1606256817}

[[静态域名解析表中不存在主机名及]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_13682_x1065_x530051742}[地址的对应关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1553896177}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_784490979}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1435190437}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1232856278}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x189388062}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x684220489}

[*[host-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x1409399745}[：主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_13682_x1065_14868121}[：与主机名对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x718045577}[：为指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置主机名和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示为公网配置主机名和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1610535032}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[公网或每个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x540860596}[VPN]{lang="EN-US"}[内最多可以配置]{style="font-family:宋体"}[1024]{lang="EN-US"}[个主机名和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的对应关系。可以为公网和最多]{style="font-family:宋体"}[1024]{lang="EN-US"}[个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[配置主机名和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的对应关系。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在公网或同一个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x18542118}[VPN]{lang="EN-US"}[内，一个主机名只能对应一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。重复配置时，新的配置会覆盖原有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[-a]{lang="EN-US"}**]{#struct_0_13682_x1065_x1678932824}[、]{lang="EN-US" style="font-family:宋体"}**[-c]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-i]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-m]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-q]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-s]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-t]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-tc]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-v]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[-vpn-instance]{lang="EN-US"}**[已被系统用作]{lang="EN-US" style="font-family:宋体"}**[ping ipv6]{lang="EN-US"}**[命令的参数关键字，在配置主机名时，请避免使用相同的字符串作为主机名。]{lang="EN-US" style="font-family:宋体"}**[ping ipv6]{lang="EN-US"}**[命令支持的参数形式，请参考"网络管理和监控"中的"]{style="font-family:宋体"}**[ping ipv6]{lang="EN-US"}**["命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232397527}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1735608465}[配置公网内主机名]{style="font-family:宋体"}[aaa]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x660572828}

[\[Sysname\] ipv6 host aaa 2001::1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_2118191708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**[ **host**]{lang="EN-US"}]{#struct_0_13682_x1065_389776296}
:::

::: {#1925265429 .myid}
[]{#_Toc404786344}[]{#struct_0_13682_x1065_x881367270}[]{#_Toc297536656}

**域名解析 \-- 域名解析配置命令 \-- reset dns host**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **dns** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x1038572959}[命令用来清除动态域名解析缓存信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_724741522}

[**[reset]{lang="EN-US"}**[ **dns** **host** \[ **ip** \| **ipv6** \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_354470809}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232331991}

[[用户视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1315987300}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1695764548}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_851990901}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_72896530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1058337358}

[**[ip]{lang="EN-US"}**]{#struct_0_13682_x1065_1622406388}[：清除]{style="font-family:宋体"}[A]{lang="EN-US"}[类查询的动态缓存信息。]{style="font-family:宋体"}[A]{lang="EN-US"}[类查询用来解析域名对应的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_13682_x1065_570509869}[：清除]{style="font-family:宋体"}[AAAA]{lang="EN-US"}[类查询的动态缓存信息。]{style="font-family:宋体"}[AAAA]{lang="EN-US"}[类查询用来解析域名对应的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_13682_x1065_1651357638}[：清除指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的动态域名解析缓存信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则清除公网的动态域名解析缓存信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1232528599}

[[如果不指定]{style="font-family:宋体"}**[ip]{lang="EN-US"}**]{#struct_0_13682_x1065_x1759790759}[和]{style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[参数，则清除所有查询类型的动态域名解析缓存信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x550879061}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1627464519}[清除公网所有查询类型的动态域名解析缓存信息。]{style="font-family:宋体"}

[[\<Sysname\> reset dns host]{lang="EN-US"}]{#struct_0_13682_x1065_x790208272}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1936294053}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **dns** **host**]{lang="EN-US"}]{#struct_0_13682_x1065_x740998412}

**[ ]{lang="EN-US"}**
:::

**[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}**

::: {.Section3 style="layout-grid:15.85pt"}
:::

::: {#213614908 .myid}
[]{#_Toc404786347}[]{#struct_0_13682_x1065_x1281261891}[]{#_Toc297536671}

**DDNS \-- DDNS配置命令 \-- ddns apply policy**

------------------------------------------------------------------------

[**[ddns]{lang="EN-US"}**[ **apply** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x387110867}[命令用来在接口上应用指定的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略来更新指定的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系，并启动]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ddns** **apply** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_471155809}[命令用来在接口上取消应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略，停止]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1246795029}

[**[ddns]{lang="EN-US"}**[ **apply** **policy** *policy-name* \[ **fqdn** *domain-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x64952922}

[**[undo]{lang="EN-US"}**[ **ddns** **apply** **policy** *policy-name*]{lang="EN-US"}]{#struct_0_13682_x1065_x179230045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1885340121}

[[没有为接口指定任何]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_1232659671}[策略和需要更新的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[，且未启动]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_2130593039}

[[接口视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1322877611}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x118796432}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1970226183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1164967473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1616216805}

[*[policy-name]{lang="EN-US"}*]{#struct_0_13682_x1065_764866204}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[fqdn]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_13682_x1065_x1289863185}[：指定需要更新该]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系，用于替换]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求]{style="font-family:宋体"}[URL]{lang="EN-US"}[中的]{style="font-family:宋体"}[\<h\>]{lang="EN-US"}[。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为主机名，主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["、"]{style="font-family:宋体"}[\_]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1829394098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口上最多可以应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_1232594135}[4]{lang="EN-US"}[个]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复应用名称相同的]{style="font-family:宋体"}]{#struct_0_13682_x1065_595280395}[DDNS]{lang="EN-US"}[策略，并指定不同的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[时，新的配置会覆盖原有配置，同时发起一次]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1963046095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_x868282523}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1036645930}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[下指定应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[来更新合格域名]{style="font-family:宋体"}[www.whatever.com]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系，并启动]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1002193208}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ddns apply policy steven_policy fqdn www.whatever.com]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_13682_x1065_969697194}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1780286214}[在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口]{style="font-family:宋体"}[2]{lang="EN-US"}[下指定应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[来更新合格域名]{style="font-family:宋体"}[www.whatever.com]{lang="EN-US"}[与]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的对应关系，并启动]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1232790743}

[\[Sysname\] interface vlan-interface 2]{lang="EN-US"}

[\[Sysname-Vlan-interface2\] ddns apply policy steven_policy fqdn www.whatever.com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1756818242}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}]{.MsoCommentReference}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_1757564966}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x2011344385}
:::

::: {#-2001255694 .myid}
[]{#_Toc404786348}[]{#struct_0_13682_x1065_x642114612}[]{#_Toc337719085}

**DDNS \-- DDNS配置命令 \-- ddns dscp**

------------------------------------------------------------------------

[**[ddns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_314326621}[命令用来配置发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo ddns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_148668271}[命令用来恢复缺省值。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_534089209}

[**[ddns dscp ]{lang="EN-US"}***[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_1646938155}

[**[undo ddns dscp]{lang="EN-US"}**]{#struct_0_13682_x1065_1232725207}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_228445619}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1598444708}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x845665644}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x2050903101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1291683556}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1237056149}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_13682_x1065_x1590744087}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1976720579}

[[DSCP]{lang="EN-US"}]{#struct_0_13682_x1065_1232921815}[优先级用来体现报文自身的优先等级，决定报文传输的优先程度。配置的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值越大，报文的优先级越高。通过本命令可以指定发送的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[报文中携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_642490202}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_581959734}[配置发送的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x60397275}

[\[Sysname\] ddns dscp 30]{lang="EN-US"}
:::

::: {#-461413230 .myid}
[]{#_Toc404786349}[]{#struct_0_13682_x1065_1265961099}[]{#_Toc297536672}

**DDNS \-- DDNS配置命令 \-- ddns policy**

------------------------------------------------------------------------

[**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1785542839}[命令用来创建]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略，并进入]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x724908360}[命令用来删除]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1382327954}

[**[ddns]{lang="EN-US"}**[ **policy** *policy-name*]{lang="EN-US"}]{#struct_0_13682_x1065_x1969498781}

[**[undo]{lang="EN-US"}**[ **ddns** **policy** *policy-name*]{lang="EN-US"}]{#struct_0_13682_x1065_1232856279}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x189322526}

[[设备上不存在任何]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x277521579}[策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x177369656}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_1348004016}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1908568425}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_729204765}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1477555141}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1521839567}

[*[policy-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x1496485825}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_672994322}

[[设备上最多可以创建]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_13682_x1065_686912720}[个]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x703044061}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x2109619481}[创建名称为]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略，并进入]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_962679225}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1074215639}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_423662359}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **apply** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1619757710}
:::

::: {#-1391410302 .myid}
[]{#_Toc404786350}[]{#struct_0_13682_x1065_x1496551361}[]{#_Toc297536673}

**DDNS \-- DDNS配置命令 \-- display ddns policy**

------------------------------------------------------------------------

[**[display ddns policy]{lang="EN-US"}**]{#struct_0_13682_x1065_x903856216}[命令用来显示]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1567808283}

[**[display]{lang="EN-US"}**[ **ddns** **policy** \[ *policy-name* \]]{lang="EN-US"}]{#struct_0_13682_x1065_x1038963213}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_467161406}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1703021769}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x523717969}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1715899617}

[[network-operator]{lang="EN-US"}]{#struct_0_13682_x1065_225457242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1496354753}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13682_x1065_x1651681674}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x302699389}

[*[policy-name]{lang="EN-US"}*]{#struct_0_13682_x1065_858786591}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1234052856}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1620103914}[显示名称为]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ddns policy steven_policy]{lang="EN-US"}]{#struct_0_13682_x1065_x850226800}

[DDNS policy: steven_policy]{lang="EN-US"}

[  URL              : http://members.3322.org/dyndns/update?]{lang="EN-US"}

[                     system=dyndns&hostname=\<h\>&myip=\<a\>]{lang="EN-US"}

[  Username         : steven]{lang="EN-US"}

[  Password         : \*\*\*\*\*\*]{lang="EN-US"}

[  Method           : GET]{lang="EN-US"}

[  SSL client policy: ]{lang="EN-US"}

[  Interval         : 1 days 0 hours 1 minutes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x1496420289}[显示所有]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ddns policy]{lang="EN-US"}]{#struct_0_13682_x1065_x1496223681}

[DDNS policy: steven_policy]{lang="EN-US"}

[  URL              : http://members.3322.org/dyndns/update?system=]{lang="EN-US"}

[                     dyndns&hostname=\<h\>&myip=\<a\>]{lang="EN-US"}

[  Username         : steven]{lang="EN-US"}

[  Password         : \*\*\*\*\*\*]{lang="EN-US"}

[  Method           : GET]{lang="EN-US"}

[  SSL client policy:]{lang="EN-US"}

[  Interval         : 0 days 0 hours 30 minutes  ]{lang="EN-US"}

[ ]{lang="EN-US"}

[DDNS policy: tom-policy]{lang="EN-US"}

[  URL              : http://members.3322.org/dyndns/update?system=]{lang="EN-US"}

[                     dyndns&hostname=\<h\>&myip=\<a\>]{lang="EN-US"}

[  Username         : ]{lang="EN-US"}

[  Password         : ]{lang="EN-US"}

[  Method           : GET]{lang="EN-US"}

[  SSL client policy:]{lang="EN-US"}

[  Interval         : 0 days 0 hours 15 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[DDNS policy: u-policy]{lang="EN-US"}

[  URL              : oray://phservice2.oray.net]{lang="EN-US"}

[  Username         : username]{lang="EN-US"}

[  Password         : ]{lang="EN-US"}

[  Method           : -]{lang="EN-US"}

[  SSL client policy:]{lang="EN-US"}

[  Interval         : 0 days 0 hours 15 minutes]{lang="EN-US"}

[ ]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display ddns policy]{lang="EN-US"}]{#struct_0_13682_x1065_x1011533902}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1045239691}[[字段]{style="font-family:黑体"}]{#struct_0_13682_x1065_x568613372}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13682_x1065_1060536153}

[[DDNS policy]{lang="EN-US"}]{#struct_0_13682_x1065_133238472}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_1721044}[策略名称]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_13682_x1065_267276727}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_902786932}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址。未配置时显示为空]{style="font-family:宋体"}

[[Username]{lang="EN-US"}]{#struct_0_13682_x1065_x1496289217}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_242285886}[更新请求]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的用户名。未配置时显示为空]{style="font-family:宋体"}

[[Password]{lang="EN-US"}]{#struct_0_13682_x1065_x2010920139}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_1973730805}[更新请求]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的密码。未配置时显示为空，]{style="font-family:宋体"}[有配置时显示为]{style="font-family:宋体"}["]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}["]{style="font-family:宋体"}

[[Method]{lang="EN-US"}]{#struct_0_13682_x1065_x273795930}

[[采用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_13682_x1065_824926326}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求时，使用的参数传输方式]{style="font-family:宋体"}

[[取值包括：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1496092609}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GET]{lang="EN-US"}]{#struct_0_13682_x1065_241938665}[：表示使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求，且参数传输方式为]{style="font-family:宋体"}[GET]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[POST]{lang="EN-US"}]{#struct_0_13682_x1065_x876486350}[：表示使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求，且参数传输方式为]{style="font-family:宋体"}[POST]{lang="EN-US"}[方式]{style="font-family:宋体"}

[[SSL client policy]{lang="EN-US"}]{#struct_0_13682_x1065_x1152926172}

[[关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_13682_x1065_x651496346}[客户端策略名称。未配置时显示为空]{style="font-family:宋体"}

[[Interval]{lang="EN-US"}]{#struct_0_13682_x1065_x617728278}

[[定时发起]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x1496158145}[更新请求的时间间隔]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x130454210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_1838420006}

::: {#-2004691874 .myid}
[]{#_Toc404786351}[]{#struct_0_13682_x1065_x1925835625}[]{#_Toc297536674}

**DDNS \-- DDNS配置命令 \-- interval**

------------------------------------------------------------------------

[**[interval]{lang="EN-US"}**]{#struct_0_13682_x1065_166216921}[命令用来指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新启动后，定时发起更新请求的时间间隔。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_13682_x1065_1211966318}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_602467637}

[**[interval]{lang="EN-US"}**[ *days* \[ *hours* \[ *minutes* \] \]]{lang="EN-US"}]{#struct_0_13682_x1065_487336954}

[**[undo]{lang="EN-US"}**[ **interval**]{lang="EN-US"}]{#struct_0_13682_x1065_1084819054}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1495961537}

[[定时发起]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_956301470}[更新请求的时间间隔是]{style="font-family:宋体"}[1]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x471907393}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x786937356}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_186557210}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x760923041}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1856995189}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1199973141}

[*[days]{lang="EN-US"}*]{#struct_0_13682_x1065_x1372692044}[：天，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[365]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[hours]{lang="EN-US"}*]{#struct_0_13682_x1065_x1496027073}[：小时，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[23]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[minutes]{lang="EN-US"}*]{#struct_0_13682_x1065_x1642377606}[：分钟，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[59]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x871858560}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不论是否到达定时发起更新请求的时间，只要对应接口的主]{style="font-family:宋体"}]{#struct_0_13682_x1065_2024103465}[IP]{lang="EN-US"}[地址发生改变或接口的链路状态由]{style="font-family:宋体"}[down]{lang="EN-US"}[变为]{style="font-family:宋体"}[up]{lang="EN-US"}[，都会立即发起更新请求。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果配置时间间隔为]{style="font-family:宋体"}]{#struct_0_13682_x1065_69371081}[0]{lang="EN-US"}[，则不会定时发起更新，除非对应接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址发生改变或接口的链路状态由]{style="font-family:宋体"}[down]{lang="EN-US"}[变为]{style="font-family:宋体"}[up]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，配置不同的时间间隔时，只有最后一次配置的时间间隔生效。如果]{style="font-family:宋体"}]{#struct_0_13682_x1065_x312497840}[DDNS]{lang="EN-US"}[策略已经应用到接口上，则立即触发一次]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新，并以最后一次配置的时间间隔为更新周期。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1851737916}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x19860364}[为]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[指定定时发起更新请求的时间间隔为]{style="font-family:宋体"}[1]{lang="EN-US"}[天零]{style="font-family:宋体"}[1]{lang="EN-US"}[分。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1496485824}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] interval 1 0 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x893089619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x2121069619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1253538210}
:::

::: {#414301358 .myid}
[]{#_Toc404786352}[]{#struct_0_13682_x1065_1404592182}

**DDNS \-- DDNS配置命令 \-- method**

------------------------------------------------------------------------

[**[method]{lang="EN-US"}**]{#struct_0_13682_x1065_861288985}[命令用来配置采用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求时，使用的参数传输方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **method**]{lang="EN-US"}]{#struct_0_13682_x1065_970608629}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1179200176}

[**[method]{lang="EN-US"}**[ { **http-get** *\|* **http-post** }]{lang="EN-US"}]{#struct_0_13682_x1065_x451332790}

[**[undo]{lang="EN-US"}**[ **method**]{lang="EN-US"}]{#struct_0_13682_x1065_x1496551360}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_662227725}

[[采用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_13682_x1065_972202368}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求时，参数的传输方式为]{style="font-family:宋体"}[http-get]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1991069888}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x819247431}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1102005907}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1081567985}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1491807064}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x19755544}

[**[http-get]{lang="EN-US"}**]{#struct_0_13682_x1065_x786594853}[：参数的传输方式为]{style="font-family:宋体"}[http-get]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[http-post]{lang="EN-US"}**]{#struct_0_13682_x1065_x1496354752}[：参数的传输方式为]{style="font-family:宋体"}[http-post]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x85597733}

[[采用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_13682_x1065_x1877425488}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求时，不同的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器要求使用的参数传输方式可能不同。例如]{style="font-family:宋体"}[DHS]{lang="EN-US"}[服务器，需要使用]{style="font-family:宋体"}[http-post]{lang="EN-US"}[参数传输方式。通过本配置可以修改参数传输方式，以满足]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器的要求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x2147033817}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令仅在基于]{style="font-family:宋体"}]{#struct_0_13682_x1065_2101816003}[HTTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器通信时生效。基于其他协议与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器通信时，本命令不生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过本命令修改]{style="font-family:宋体"}]{#struct_0_13682_x1065_1185283991}[DDNS]{lang="EN-US"}[策略的参数传输方式时，如果该]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略已经应用到接口上，则立即触发一次]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_799408912}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_x887020110}[配置]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[采用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[或]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[报文发送]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求时，使用的参数传输方式为]{style="font-family:宋体"}[post]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1496420288}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] method http-post]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2099424991}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_1166547568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x76315808}
:::

::: {#-231203086 .myid}
[]{#_Toc404786353}[]{#struct_0_13682_x1065_x1348830240}

**DDNS \-- DDNS配置命令 \-- password**

------------------------------------------------------------------------

[**[password]{lang="EN-US"}**]{#struct_0_13682_x1065_x2136414939}[命令用来指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的密码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **password**]{lang="EN-US"}]{#struct_0_13682_x1065_190576249}[命令用来删除]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_660486732}

[**[password]{lang="EN-US"}**[ { **cipher** \| **simple** } *password*]{lang="EN-US"}]{#struct_0_13682_x1065_1124754747}

[**[undo password]{lang="EN-US"}**]{#struct_0_13682_x1065_x1496223680}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1717349453}

[[未指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x1437911673}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1394969024}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x631057534}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1861188640}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x642559627}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_1439050403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1618285851}

[**[cipher]{lang="EN-US"}**]{#struct_0_13682_x1065_x1460837572}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13682_x1065_x1496289216}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_13682_x1065_x1323798055}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1382403353}

[[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_13682_x1065_1916338766}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1400941086}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1906743142}[为]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中登录密码为]{style="font-family:宋体"}[nevets]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_146648818}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] password simple nevets]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1087417976}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ddns policy]{lang="EN-US"}**]{#struct_0_13682_x1065_x1496092608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns policy]{lang="EN-US"}**]{#struct_0_13682_x1065_1808022606}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[url]{lang="EN-US"}**]{#struct_0_13682_x1065_x962315596}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[username]{lang="EN-US"}**]{#struct_0_13682_x1065_1496934387}
:::

::::: {#-372166001 .myid}
[]{#_Toc404786354}[]{#struct_0_13682_x1065_280570362}[]{#_Toc297536675}

**DDNS \-- DDNS配置命令 \-- ssl-client-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](域名解析命令.files/image002.png){width="61" height="24"}]{lang="EN-US"}]{#struct_0_13682_x1065_x309157199}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_13682_x1065_x1452781911}
:::

[ ]{lang="EN-US"}

[**[ssl-client-policy]{lang="EN-US"}**]{#struct_0_13682_x1065_x1102078334}[命令用来指定与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy**]{lang="EN-US"}]{#struct_0_13682_x1065_1154220760}[命令用来取消与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1496158144}

[**[ssl-client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_13682_x1065_1435629731}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x2058402541}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1168214088}

[[未指定与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_2117936754}[策略关联的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x188555124}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_1988332496}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1774882392}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1349313219}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_217056585}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1495961536}

[*[policy-name]{lang="EN-US"}*]{#struct_0_13682_x1065_x609782471}[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x739375025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL]{lang="EN-US"}]{#struct_0_13682_x1065_1246534472}[客户端策略只对]{lang="EN-US" style="font-family:
宋体"}[URL]{lang="EN-US"}[为]{lang="EN-US" style="font-family:
宋体"}[HTTPS]{lang="EN-US"}[地址的]{lang="EN-US" style="font-family:
宋体"}[DDNS]{lang="EN-US"}[更新请求有效。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，为同一个]{style="font-family:宋体"}]{#struct_0_13682_x1065_x2007994174}[DDNS]{lang="EN-US"}[策略关联不同的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略时，]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略将只与最后配置的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略关联。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x543737122}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_641059431}[将]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[ssl_policy]{lang="EN-US"}[与]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[关联。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_441694534}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] ssl-client-policy ssl_policy]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1496027072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_1086505749}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1533231662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssl-client-policy]{lang="EN-US"}**]{#struct_0_13682_x1065_844360152}[（]{style="font-family:宋体"}[安全命令参考]{lang="EN-US" style="font-family:宋体"}[/SSL]{lang="EN-US"}[）]{style="font-family:宋体"}
:::::

::: {#-1384273943 .myid}
[]{#_Toc404786355}[]{#struct_0_13682_x1065_807981498}[]{#_Toc297536676}

**DDNS \-- DDNS配置命令 \-- url**

------------------------------------------------------------------------

[**[url]{lang="EN-US"}**]{#struct_0_13682_x1065_x682679812}[命令用来指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **url**]{lang="EN-US"}]{#struct_0_13682_x1065_x1592257297}[命令用来删除]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1715692798}

[**[url]{lang="EN-US"}**[ *request-url*]{lang="EN-US"}]{#struct_0_13682_x1065_x903930955}

[**[undo]{lang="EN-US"}**[ **url**]{lang="EN-US"}]{#struct_0_13682_x1065_x1496485827}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1835793736}

[[未指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x442988200}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x412830069}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_735040287}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1441014122}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x982748820}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_670081079}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_13682_x1065_2885475}

[*[request-url]{lang="EN-US"}*]{#struct_0_13682_x1065_x1496551363}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[240]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x2066655630}

[[不同]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_330457625}[服务器的请求更新]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址有所不同。常见的]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址格式如]{style="font-family:宋体"}[[表]{style="font-family:宋体"}[2-2]{lang="EN-US"}](?-1384273943#_Ref309136168)[所示。]{style="font-family:宋体"}

[]{#struct_0_13682_x1065_417072384}[]{#_Ref309136168}[[表2-2 ]{lang="EN-US"}[常见的]{style="font-family:黑体"}[DDNS]{lang="EN-US"}]{#_Ref309117506}[更新请求]{style="font-family:黑体"}[URL]{lang="EN-US"}[地址格式列表]{style="font-family:黑体"}

[]{#table_struct_0_x1050804869}[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_902468872}[服务器]{style="font-family:黑体"}
:::

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x1530399204}[更新请求的]{style="font-family:黑体"}[URL]{lang="EN-US"}[地址格式]{style="font-family:黑体"}

[[www.3322.org]{lang="EN-US"}]{#struct_0_13682_x1065_x1496354755}

[[http://members.3322.org/dyndns/update?system=dyndns&hostname=\<h\>&myip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_1480486208}

[[DYNDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x1815322588}

[[http://members.dyndns.org/nic/update?system=dyndns&hostname=\<h\>&myip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_2041931859}

[[DYNS]{lang="EN-US"}]{#struct_0_13682_x1065_866626210}

[[http://www.dyns.cx/postscript.php?host=\<h\>&ip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_x1800972596}

[[ZONEEDIT]{lang="EN-US"}]{#struct_0_13682_x1065_1318467013}

[[http://dynamic.zoneedit.com/auth/dynamic.html?host=\<h\>&dnsto=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_x1496420291}

[[TZO]{lang="EN-US"}]{#struct_0_13682_x1065_x889505874}

[[http://cgi.tzo.com/webclient/signedon.html?TZOName=\<h\>IPAddress=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_x1611166763}

[[EASYDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x335402806}

[[http://members.easydns.com/dyn/ez-ipupdate.php?action=edit&myip=\<a\>&host_id=\<h\>]{lang="EN-US"}]{#struct_0_13682_x1065_1077070793}

[[HEIPV6TB]{lang="EN-US"}]{#struct_0_13682_x1065_x1496223683}

[[http://dyn.dns.he.net/nic/update?hostname=\<h\>&myip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_2120633980}

[[CHANGE-IP]{lang="EN-US"}]{#struct_0_13682_x1065_x633567894}

[[http://nic.changeip.com/nic/update?hostname=\<h\>&offline=1]{lang="EN-US"}]{#struct_0_13682_x1065_x13073239}

[[NO-IP]{lang="EN-US"}]{#struct_0_13682_x1065_x910439435}

[[http://dynupdate.no-ip.com/nic/update?hostname=\<h\>&myip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_x2086599973}

[[DHS]{lang="EN-US"}]{#struct_0_13682_x1065_x1496289219}

[[http://members.dhs.org/nic/hosts?domain=dyn.dhs.org&hostname=\<h\>&hostscmd=edit&hostscmdstage=2&type=1&ip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_1405085300}

[[HP]{lang="EN-US"}]{#struct_0_13682_x1065_x731747599}

[[https://*server-name*/nic/update?group=*group-name*&myip=\<a\>]{lang="EN-US"}]{#struct_0_13682_x1065_x2085911317}

[[ODS]{lang="EN-US"}]{#struct_0_13682_x1065_x1496092611}

[[ods://update.ods.org]{lang="EN-US"}]{#struct_0_13682_x1065_x114226159}

[[GNUDIP]{lang="EN-US"}]{#struct_0_13682_x1065_294632236}

[[gnudip://*server-name*]{lang="EN-US"}]{#struct_0_13682_x1065_1544572282}

[[花生壳]{style="font-family:宋体"}]{#struct_0_13682_x1065_1686526468}

[[oray://phservice2.oray.net]{lang="EN-US"}]{#struct_0_13682_x1065_x1496158147}

[ ]{lang="EN-US"}

[[其中：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1293253624}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[URL]{lang="EN-US"}]{#struct_0_13682_x1065_x1184765615}[地址中不支持携带用户名和密码，配置用户名和密码请配合]{style="font-family:宋体"}**[username]{lang="EN-US"}**[和]{style="font-family:宋体"}**[password]{lang="EN-US"}**[命令使用，请根据实际情况修改。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HP]{lang="EN-US"}]{#struct_0_13682_x1065_x429523407}[和]{lang="EN-US" style="font-family:
宋体"}[GNUDIP]{lang="EN-US"}[是通用的]{lang="EN-US" style="font-family:
宋体"}[DDNS]{lang="EN-US"}[更新协议，]{lang="EN-US" style="font-family:
宋体"}*[server-name]{lang="EN-US"}*[是]{style="font-family:宋体"}[使用对应]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新协议的服务提供商的服务器域名或地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x100311286}[更新请求的]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[地址可以以"]{lang="EN-US" style="font-family:宋体"}[http://]{lang="EN-US"}["开头，表示基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器通信；以"]{lang="EN-US" style="font-family:宋体"}[https://]{lang="EN-US"}["开头，表示基于]{lang="EN-US" style="font-family:宋体"}[HTTPS]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器通信；以"]{lang="EN-US" style="font-family:宋体"}[ods://]{lang="EN-US"}["开头，表示基于]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[ODS]{lang="EN-US"}[服务器通信；以"]{lang="EN-US" style="font-family:宋体"}[gnudip://]{lang="EN-US"}["开头，表示基于]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[与]{lang="EN-US" style="font-family:宋体"}[GNUDIP]{lang="EN-US"}[服务器通信；以"]{lang="EN-US" style="font-family:宋体"}[oray://]{lang="EN-US"}["开头，表示基于]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[与花生壳]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器通信。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[members.3322.org]{lang="EN-US"}]{#struct_0_13682_x1065_x1495961539}[和]{lang="EN-US" style="font-family:宋体"}[phservice2.oray.net]{lang="EN-US"}[是]{style="font-family:宋体"}[服务提供商提供]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务的域名。花生壳提供]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务的域名可能]{lang="EN-US" style="font-family:宋体"}[是]{style="font-family:宋体"}[phservice2.oray.net]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[phddns60.oray.net]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[client.oray.net]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[ph031.oray.net]{lang="EN-US"}[等，请根据实际情况修改域名。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[URL]{lang="EN-US"}]{#struct_0_13682_x1065_x1496027075}[地址中的端口号是可选项，如果不包含端口号则使用缺省端口号：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[是]{style="font-family:宋体"}[80]{lang="EN-US"}[，]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[是]{style="font-family:宋体"}[443]{lang="EN-US"}[，花生壳]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务器是]{style="font-family:宋体"}[6060]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[\<h\>]{lang="EN-US"}]{#struct_0_13682_x1065_1489790276}[由系统根据接口上应用]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略时指定的]{lang="EN-US" style="font-family:宋体"}[FQDN]{lang="EN-US"}[自动填写，]{lang="EN-US" style="font-family:宋体"}[\<a\>]{lang="EN-US"}[由系统根据应用]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的接口的主]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址自动填写，用户可以不更改]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[中的]{lang="EN-US" style="font-family:宋体"}[\<h\>]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[\<a\>]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}[用户也可以手工输入需要更新的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，代替]{style="font-family:宋体"}[URL]{lang="EN-US"}[中的]{style="font-family:宋体"}[\<h\>]{lang="EN-US"}[和]{style="font-family:宋体"}[\<a\>]{lang="EN-US"}[，此时，应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略时指定的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[将不会生效。为了避免配置错误，建议用户不要修改]{style="font-family:宋体"}[URL]{lang="EN-US"}[中的]{style="font-family:宋体"}[\<h\>]{lang="EN-US"}[和]{style="font-family:宋体"}[\<a\>]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[花生壳]{style="font-family:宋体"}]{#struct_0_13682_x1065_x22841576}[DDNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中不能指定用于更新的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。用户可在接口上应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略时指定]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[；用于更新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是应用]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略的接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_13682_x1065_x1496485826}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为避免歧义，请尽量不要在]{lang="EN-US" style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_269709795}[服务器上申请含有"]{lang="EN-US" style="font-family:宋体"}[:]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[@]{lang="EN-US"}["或"]{lang="EN-US" style="font-family:宋体"}[?]{lang="EN-US"}["字符的用户名和密码。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，配置不同的]{style="font-family:宋体"}]{#struct_0_13682_x1065_2078195905}[URL]{lang="EN-US"}[地址时，新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_463177206}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_2006772148}[为]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址。]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[服务提供商为]{style="font-family:宋体"}[www.3322.org]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_1419259416}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] url http:// members.3322.org/dyndns/update?system=dyndns&hostname=\<h\>&myip=\<a\> ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x472369757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **ddns** **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1230313296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns]{lang="EN-US"}**[ **policy**]{lang="EN-US"}]{#struct_0_13682_x1065_x1496551362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password]{lang="EN-US"}**]{#struct_0_13682_x1065_x500571689}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[username]{lang="EN-US"}**]{#struct_0_13682_x1065_547186149}

::: {#-2032495825 .myid}
[]{#_Toc404786356}[]{#struct_0_13682_x1065_1212657143}

**DDNS \-- DDNS配置命令 \-- username**

------------------------------------------------------------------------

[**[username]{lang="EN-US"}**]{#struct_0_13682_x1065_1645377914}[命令用来指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的用户名。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **username**]{lang="EN-US"}]{#struct_0_13682_x1065_x540607248}[命令用来删除]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的用户名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1548274316}

[**[username]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13682_x1065_x566464084}*[username]{lang="EN-US"}*

[**[undo]{lang="EN-US"}**[ **username**]{lang="EN-US"}]{#struct_0_13682_x1065_1253962679}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1496354754}

[[未指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_x1248397147}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13682_x1065_1059174716}

[[DDNS]{lang="EN-US"}]{#struct_0_13682_x1065_1612272263}[策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x171238350}

[[network-admin]{lang="EN-US"}]{#struct_0_13682_x1065_x1828823808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13682_x1065_2037672185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13682_x1065_872477194}

[*[username]{lang="EN-US"}*]{#struct_0_13682_x1065_x1705262596}[：]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1496420290}

[[\# ]{lang="EN-US"}]{#struct_0_13682_x1065_1839377481}[为]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[策略]{style="font-family:宋体"}[steven_policy]{lang="EN-US"}[指定]{style="font-family:宋体"}[DDNS]{lang="EN-US"}[更新请求的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址中的登录用户名为]{style="font-family:宋体"}[steven]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13682_x1065_x1503742107}

[\[Sysname\] ddns policy steven_policy]{lang="EN-US"}

[\[Sysname-ddns-policy-steven_policy\] username steven]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13682_x1065_x1691263673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ddns policy]{lang="EN-US"}**]{#struct_0_13682_x1065_x1724569399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ddns policy]{lang="EN-US"}**]{#struct_0_13682_x1065_907138758}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password]{lang="EN-US"}**]{#struct_0_13682_x1065_x1668703679}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[url]{lang="EN-US"}**]{#struct_0_13682_x1065_x1427173483}
:::
