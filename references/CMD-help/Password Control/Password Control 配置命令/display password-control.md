::: {#-852354309 .myid}
[]{#_Toc404792916}[]{#struct_0_44025_14098_x1360015856}

**Password Control \-- Password Control 配置命令 \-- display password-control**

------------------------------------------------------------------------

[**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x337050630}[命令用来显示密码管理的配置信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_566288816}

[**[display password-control ]{lang="EN-US"}**[\[ **super** \]]{lang="EN-US"}]{#struct_0_44025_14098_409115781}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_991672291}

[[任意视图]{style="font-family:宋体"}]{#struct_0_44025_14098_1501510039}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x262593721}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_266370804}

[[network-operator]{lang="EN-US"}]{#struct_0_44025_14098_x1128226217}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1360081392}

[[mdc-operator]{lang="EN-US"}]{#struct_0_44025_14098_x1973416758}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x628832636}

[**[super]{lang="EN-US"}**]{#struct_0_44025_14098_163900180}[：显示]{style="font-family:宋体"}[super]{lang="EN-US"}[密码管理的配置信息。如果不指定该参数，将显示全局密码管理的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_1030725759}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_903400888}[显示全局密码管理的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display password-control]{lang="EN-US"}]{#struct_0_44025_14098_x1359622640}

[ Global password control configurations:]{lang="EN-US"}

[ Password control:                     Disabled]{lang="EN-US"}

[ Password aging:                       Enabled (90 days)]{lang="EN-US"}

[ Password length:                      Enabled (10 characters)]{lang="EN-US"}

[ Password composition:                 Enabled (1 types, 1 characters per type)]{lang="EN-US"}

[ Password history:                     Enabled (max history records:4)]{lang="EN-US"}

[ Early notice on password expiration:  7 days]{lang="EN-US"}

[ Maximum login attempts:               3]{lang="EN-US"}

[ Action for exceeding login attempts:  Lock user for 1 minutes]{lang="EN-US"}

[ Minimum interval between two updates: 24 hours]{lang="EN-US"}

[ User account idle time:               90 days]{lang="EN-US"}

[ Logins with aged password:            3 times in 30 days]{lang="EN-US"}

[ Password complexity:                  Disabled (username checking)]{lang="EN-US"}

[                                       Disabled (repeated characters checking)]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1744059092}[显示]{style="font-family:宋体"}[super]{lang="EN-US"}[密码管理的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display password-control super]{lang="EN-US"}]{#struct_0_44025_14098_1859542337}

[ Super password control configurations:]{lang="EN-US"}

[ Password aging:                       Enabled (90 days)]{lang="EN-US"}

[ Password length:                      Enabled (10 characters)]{lang="EN-US"}

[ Password composition:                 Enabled (1 types, 1 characters per type)]{lang="EN-US"}

[]{#struct_0_44025_14098_x251380937}[[表1-1 ]{lang="EN-US"}[display password-control]{lang="EN-US"}]{#_Toc138134210}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1440597870}[[字段]{style="font-family:黑体"}]{#struct_0_44025_14098_1245114923}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359688176}

[[Global password control configurations]{lang="EN-US"}]{#struct_0_44025_14098_1409409151}

[[全局密码管理配置]{style="font-family:宋体"}]{#struct_0_44025_14098_2100903124}

[[Super password control configurations]{lang="EN-US"}]{#struct_0_44025_14098_x1145200253}

[[Super]{lang="EN-US"}]{#struct_0_44025_14098_1763914354}[密码管理配置]{style="font-family:宋体"}

[[Password control]{lang="EN-US"}]{#struct_0_44025_14098_x1380113133}

[[全局密码管理功能的开启状态]{style="font-family:宋体"}]{#struct_0_44025_14098_1497462259}

[[Password aging]{lang="EN-US"}]{#struct_0_44025_14098_x1359753712}

[[密码老化功能的开启状态（密码的老化时间）]{style="font-family:宋体"}]{#struct_0_44025_14098_x1717890322}

[[Password length]{lang="EN-US"}]{#struct_0_44025_14098_562219309}

[[密码最小长度功能的开启状态（密码的最小长度）]{style="font-family:宋体"}]{#struct_0_44025_14098_x1409777516}

[[Password composition]{lang="EN-US"}]{#struct_0_44025_14098_1216991748}

[[密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）]{style="font-family:宋体"}]{#struct_0_44025_14098_x2137878681}

[[Password history]{lang="EN-US"}]{#struct_0_44025_14098_x1359819248}

[[密码历史记录功能的开启状态（密码历史记录的最大条数）]{style="font-family:宋体"}]{#struct_0_44025_14098_1826006223}

[[Early notice on password expiration]{lang="EN-US"}]{#struct_0_44025_14098_x309638484}

[[密码过期前的提醒时间]{style="font-family:宋体"}]{#struct_0_44025_14098_868062852}

[[Maximum login attempts]{lang="EN-US"}]{#struct_0_44025_14098_x1495471106}

[[用户最大登录尝试次数]{style="font-family:宋体"}]{#struct_0_44025_14098_x1359360496}

[[Action for exceeding login attempts]{lang="EN-US"}]{#struct_0_44025_14098_x910467256}

[[登录尝试次数达到设定次数后的用户帐户锁定行为]{style="font-family:宋体"}]{#struct_0_44025_14098_x908179653}

[[Minimum interval between two updates]{lang="EN-US"}]{#struct_0_44025_14098_x1215624625}

[[密码更新的最小时间间隔]{style="font-family:宋体"}]{#struct_0_44025_14098_x1159587085}

[[User account idle time]{lang="EN-US"}]{#struct_0_44025_14098_x1359426032}

[[用户帐号闲置时间]{style="font-family:宋体"}]{#struct_0_44025_14098_41046436}

[[Login with aged password]{lang="EN-US"}]{#struct_0_44025_14098_1529454325}

[[密码过期后允许用户登录的次数和时间]{style="font-family:宋体"}]{#struct_0_44025_14098_877945073}

[[Password complexity]{lang="EN-US"}]{#struct_0_44025_14098_x1359884783}

[[密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）]{style="font-family:宋体"}]{#struct_0_44025_14098_x969696910}

[]{#_Toc133045164}[]{#_Toc133554881}[]{#_Toc133554924}[]{#_Toc133986001}[]{#_Toc133996380}[]{#_Toc133045167}[]{#_Toc133554884}[]{#_Toc133554927}[]{#_Toc133986004}[]{#_Toc133996383}[ ]{lang="EN-US"}

::: {#-1578525123 .myid}
[]{#_Toc404792917}[]{#struct_0_44025_14098_x517874393}

**Password Control \-- Password Control 配置命令 \-- display password-control blacklist**

------------------------------------------------------------------------

[**[display password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_1461626261}[命令用来显示用户认证失败后，被加入密码管理黑名单中的用户信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1322512602}

[**[display password-control blacklist ]{lang="EN-US"}**[\[ **user-name** *name* \| **ip** *ipv4-address* \| **ipv6** *ipv6-address* \] ]{lang="EN-US"}]{#struct_0_44025_14098_765520587}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1206795192}

[[任意视图]{style="font-family:宋体"}]{#struct_0_44025_14098_600928755}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359950319}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_325337903}

[[network-operator]{lang="EN-US"}]{#struct_0_44025_14098_x1275048854}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x367775883}

[[mdc-operator]{lang="EN-US"}]{#struct_0_44025_14098_2129291382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1896913856}

[**[user-name]{lang="EN-US"}***[ name]{lang="EN-US"}*]{#struct_0_44025_14098_x803276358}[：显示密码管理黑名单中指定用户名的用户信息。其中，]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示本地用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ipv4-address]{lang="EN-US"}*]{#struct_0_44025_14098_x561456655}[：显示密码管理黑名单中指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的用户信息。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_44025_14098_x1360015855}[：显示密码管理黑名单中指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的用户信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_1229033311}

[[如果不指定任何参数，则显示密码管理黑名单中的所有用户信息。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1142320720}

[[FTP]{lang="EN-US"}]{#struct_0_44025_14098_473863823}[用户和通过]{style="font-family:宋体"}[VTY]{lang="EN-US"}[方式访问设备的用户在认证失败后，会被加入密码管理的黑名单，可通过本命令查看；]{style="font-family:宋体"}[Web]{lang="EN-US"}[用户认证失败不会加入密码管理黑名单；通过]{style="font-family:宋体"}[Console]{lang="EN-US"}[口或]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口连接到设备的用户，由于系统无法获得其]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，且通过这两种方式访问设备的用户已经具备了一定的权限和安全性，所以认证失败后也不会被加入密码管理的黑名单。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_1203873202}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1541123655}[显示用户认证失败后，被加入密码管理黑名单中的用户信息。]{style="font-family:宋体"}

[[\<Sysname\> display password-control blacklist]{lang="EN-US"}]{#struct_0_44025_14098_367054622}

[ Blacklist items matched: 2.]{lang="EN-US"}

[ Username: test]{lang="EN-US"}

[    IP: 192.168.44.1        Login failures: 1      Lock flag: unlock]{lang="EN-US"}

[ Username: jj]{lang="EN-US"}

[    IP: 192.168.44.3        Login failures: 3      Lock flag: lock]{lang="EN-US"}[]{#_Toc133045169}[]{#_Toc133554886}[]{#_Toc133554929}

[]{#struct_0_44025_14098_x1700075383}[[表1-2 ]{lang="EN-US"}[display password-control blacklist]{lang="EN-US"}]{#_Toc138134211}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1435281773}[[字段]{style="font-family:黑体"}]{#struct_0_44025_14098_x1360081391}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_44025_14098_x1570132231}

[[Blacklist items matched]{lang="EN-US"}]{#struct_0_44025_14098_2044854248}

[[匹配的黑名单表项数目]{style="font-family:宋体"}]{#struct_0_44025_14098_1001284581}

[[Username]{lang="EN-US"}]{#struct_0_44025_14098_2044919784}

[[用户名]{style="font-family:宋体"}]{#struct_0_44025_14098_934301559}

[[IP]{lang="EN-US"}]{#struct_0_44025_14098_x993270702}

[[用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_44025_14098_x1601428093}[地址]{style="font-family:宋体"}

[[Login failures]{lang="EN-US"}]{#struct_0_44025_14098_948260547}

[[用户登录失败的次数]{style="font-family:宋体"}]{#struct_0_44025_14098_x1359622639}

[[Lock flag]{lang="EN-US"}]{#struct_0_44025_14098_x1341120159}

[[该用户是否被锁定]{style="font-family:宋体"}]{#struct_0_44025_14098_1551078683}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[unlock]{lang="EN-US"}]{#struct_0_44025_14098_462932448}[：表示未锁定，允许用户再次尝试登录]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[lock]{lang="EN-US"}]{#struct_0_44025_14098_2135313497}[：表示锁定，暂时或永久禁止用户尝试登录（具体由]{lang="EN-US" style="font-family:宋体"}**[password-control login-attempt]{lang="EN-US"}**[命令的配置情况决定）]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#370026937 .myid}
[]{#_Toc404792918}[]{#struct_0_44025_14098_1812693678}[]{#_Toc320720924}[]{#_Toc320720925}[]{#_Toc320720926}[]{#_Toc320720927}[]{#_Toc320720928}[]{#_Toc320720929}[]{#_Toc320720930}[]{#_Toc320720931}[]{#_Toc320720932}[]{#_Toc320720933}[]{#_Toc320720934}[]{#_Toc320720935}[]{#_Toc320720936}[]{#_Toc320720937}[]{#_Toc320720938}[]{#_Toc320720939}[]{#_Toc320720940}[]{#_Toc320720941}[]{#_Toc320720942}[]{#_Toc320720943}[]{#_Toc320720944}[]{#_Toc320720945}[]{#_Toc320720946}

**Password Control \-- Password Control 配置命令 \-- password-control { aging \| composition \| history \| length } enable**

------------------------------------------------------------------------

[**[password-control ]{lang="EN-US"}**[{ **aging** \| **composition** \| **history** \| **length** } **enable**]{lang="EN-US"}]{#struct_0_44025_14098_1565828875}[命令用来使能指定的密码管理功能。]{style="font-family:宋体"}

[**[undo password-control ]{lang="EN-US"}**[{ **aging** \| **composition** \| **history** \| **length** } **enable**]{lang="EN-US"}]{#struct_0_44025_14098_1845931506}[命令用来关闭指定的密码管理功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1861990218}

[**[password-control ]{lang="EN-US"}**[{ **aging** \| **composition** \| **history** \| **length** } **enable**]{lang="EN-US"}]{#struct_0_44025_14098_292508326}

[**[undo password-control ]{lang="EN-US"}**[{ **aging** \| **composition** \| **history** \| **length** } **enable**]{lang="EN-US"}]{#struct_0_44025_14098_776963382}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_1271437042}

[[各密码管理功能均处于使能状态。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1359753711}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x151806381}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x381601933}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_1301330372}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x2080824308}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x154848622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1249417191}

[**[aging]{lang="EN-US"}**]{#struct_0_44025_14098_2127428690}[：使能密码老化管理功能。]{style="font-family:宋体"}

[**[composition]{lang="EN-US"}**]{#struct_0_44025_14098_x236663628}[：使能密码的组合检测管理功能。]{style="font-family:宋体"}

[**[history]{lang="EN-US"}**]{#struct_0_44025_14098_x1359819247}[：使能密码历史记录管理功能。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**]{#struct_0_44025_14098_x190416412}[：使能密码最小长度管理功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x800125094}

[[要使指定的密码管理功能生效，首先必须保证全局密码管理功能处于使能状态，其次要保证对应的密码管理功能处于使能状态。例如，若全局密码管理功能或密码最小长度管理功能处于未使能状态，则]{style="font-family:宋体"}**[password-control length]{lang="EN-US"}**]{#struct_0_44025_14098_705443807}[命令配置的具体长度限制就不会生效。]{style="font-family:宋体"}

[[密码历史记录管理功能关闭后，系统将不再记录历史密码，但之前已经存在的密码历史记录依然保存。]{style="font-family:宋体"}]{#struct_0_44025_14098_1080340344}

[[需要注意的是，使能了全局密码管理功能，未使能密码最小长度管理功能时，密码的最小长度为]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_44025_14098_x338790511}[个字符，且至少要有四个字符不同。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1217535305}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x1459997913}[使能全局密码管理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1359360495}

[\[Sysname\] password-control enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1818416099}[使能密码组合检测管理功能。]{style="font-family:宋体"}

[[\[Sysname\] password-control composition enable]{lang="EN-US"}]{#struct_0_44025_14098_x469832226}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_2045905664}[使能密码老化功能。]{style="font-family:宋体"}

[[\[Sysname\] password-control aging enable]{lang="EN-US"}]{#struct_0_44025_14098_1760024629}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x855562695}[使能密码最小长度功能。]{style="font-family:宋体"}

[[\[Sysname\] password-control length enable]{lang="EN-US"}]{#struct_0_44025_14098_1981876541}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1137663908}[使能密码历史记录功能。]{style="font-family:宋体"}

[[\[Sysname\] password-control history enable]{lang="EN-US"}]{#struct_0_44025_14098_x526481036}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359426031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x1525037505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control enable]{lang="EN-US"}**]{#struct_0_44025_14098_1141017672}
:::

::: {#701783099 .myid}
[]{#_Toc404792919}[]{#struct_0_44025_14098_x1683948332}[]{#_Toc300926425}[]{#_Toc259634089}

**Password Control \-- Password Control 配置命令 \-- password-control aging**

------------------------------------------------------------------------

[**[password-control aging]{lang="EN-US"}**]{#struct_0_44025_14098_x2086272755}[命令用来配置密码的老化时间。]{style="font-family:宋体"}

[**[undo password-control aging]{lang="EN-US"}**]{#struct_0_44025_14098_2146509966}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x916958995}

[**[password-control aging ]{lang="EN-US"}***[aging-time]{lang="EN-US"}*]{#struct_0_44025_14098_x1286768669}

[**[undo password-control aging]{lang="EN-US"}**]{#struct_0_44025_14098_x983052844}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359884786}

[[全局的密码老化时间为]{style="font-family:宋体"}[90]{lang="EN-US"}]{#struct_0_44025_14098_x210182023}[天；用户组的密码老化时间为全局配置的密码老化时间；本地用户的密码老化时间为所属用户组的密码老化时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x564270878}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_44025_14098_1419583644}[用户组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[本地用户视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1639405907}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_106446782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x480017529}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1403477543}

[*[aging-time]{lang="EN-US"}*]{#struct_0_44025_14098_1978341453}[：密码的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[365]{lang="EN-US"}[，单位为天。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359950322}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1596779790}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。]{style="font-family:宋体"}]{#struct_0_44025_14098_241742784}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_2016177599}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x1210290971}[配置全局的密码老化时间为]{style="font-family:宋体"}[80]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_1882258474}

[\[Sysname\] password-control aging 80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1649070813}[配置用户组]{style="font-family:宋体"}[test]{lang="EN-US"}[的密码老化时间为]{style="font-family:宋体"}[90]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\[Sysname\] user-group test]{lang="EN-US"}]{#struct_0_44025_14098_x1360015858}

[\[Sysname-ugroup-test\] password-control aging 90]{lang="EN-US"}

[\[Sysname-ugroup-test\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_113288064}[配置设备管理类本地用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的密码老化时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\[Sysname\] local-user abc class manage]{lang="EN-US"}]{#struct_0_44025_14098_131404823}

[\[Sysname-luser-]{lang="EN-US"}[manage-]{lang="FR"}[abc\] password-control aging 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_920955390}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[local-user]{lang="EN-US"}**]{#struct_0_44025_14098_x2050569004}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_1953625260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_44025_14098_393797058}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control aging enable]{lang="EN-US"}**]{#struct_0_44025_14098_x757462150}
:::

::: {#1810780389 .myid}
[]{#_Toc404792920}[]{#struct_0_44025_14098_1917454679}[]{#_Toc300926426}[]{#_Toc259634090}

**Password Control \-- Password Control 配置命令 \-- password-control alert-before-expire**

------------------------------------------------------------------------

[**[password-control alert-before-expire]{lang="EN-US"}**]{#struct_0_44025_14098_x1360081394}[命令用来配置密码过期前的提醒时间。]{style="font-family:宋体"}

[**[undo password-control alert-before-expire]{lang="EN-US"}**]{#struct_0_44025_14098_x810617344}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1650280318}

[**[password-control alert-before-expire]{lang="EN-US"}***[ alert-time]{lang="EN-US"}*]{#struct_0_44025_14098_1697850707}

[**[undo password-control alert-before-expire]{lang="EN-US"}**]{#struct_0_44025_14098_993023908}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1605475542}

[[密码过期前的提醒时间为]{style="font-family:宋体"}[7]{lang="EN-US"}]{#struct_0_44025_14098_1400351906}[天，表示在密码过期之前]{style="font-family:宋体"}[7]{lang="EN-US"}[天内，系统会在用户登录时提醒其密码即将过期。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1581213528}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_21904897}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359622642}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_581259678}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_368500148}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_2095571858}

[*[alert-time]{lang="EN-US"}*]{#struct_0_44025_14098_359585719}[：密码过期前的提醒时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为天。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_235651926}

[[不允许]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_44025_14098_x1350940430}[用户更改密码，只能由管理员修改]{style="font-family:宋体"}[FTP]{lang="EN-US"}[用户的密码，因此本命令配置的过期提醒时间仅对非]{style="font-family:宋体"}[FTP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1455683157}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x200308667}[设定密码过期前的提醒时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1359688178}

[\[Sysname\] password-control alert-before-expire 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1722758731}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x1475765059}
:::

::: {#616172029 .myid}
[]{#_Toc404792921}[]{#struct_0_44025_14098_2032736780}

**Password Control \-- Password Control 配置命令 \-- password-control complexity**

------------------------------------------------------------------------

[**[password-control complexity]{lang="SV"}**]{#struct_0_44025_14098_1531125565}[命令用来配置用户密码的复杂度检查策略。]{style="font-family:宋体"}

[**[undo password-control complexity]{lang="SV"}**]{#struct_0_44025_14098_1201720826}[命令用来取消指定的密码复杂度检查策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1429068917}

[**[password-control complexity ]{lang="EN-US"}**[{ **same-character** \| **user-name** } **check**]{lang="EN-US"}]{#struct_0_44025_14098_x1235680986}

[**[undo password-control complexity ]{lang="EN-US"}**[{ **same-character** \| **user-name** } **check**]{lang="EN-US"}]{#struct_0_44025_14098_x1086115479}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359753714}

[[全局的密码复杂度检查策略为：不对用户密码进行复杂度检查，允许密码中包含用户名或者字符顺序颠倒的用户名，也允许包含连续三个或以上的相同字符；用户组的密码复杂度检查策略为全局的的密码复杂度检查策略；本地用户的密码复杂度检查策略为所属用户组的密码复杂度检查策略。]{style="font-family:宋体"}]{#struct_0_44025_14098_x911321268}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x513516121}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_44025_14098_132758453}[用户组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[本地用户视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x747347760}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x119617025}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_1161906040}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1624764853}

[**[same-character]{lang="EN-US"}**]{#struct_0_44025_14098_71706970}[：指定检查密码中是否包含连续三个或以上相同的字符。例如，密码]{style="font-family:宋体"}[aaabc]{lang="EN-US"}[就不符合该项复杂度检查。]{style="font-family:宋体"}

[**[user-name]{lang="EN-US"}**]{#struct_0_44025_14098_x1359819250}[：指定检查密码中是否包含用户名或者字符顺序颠倒的用户名。例如，用户名为]{style="font-family:宋体"}[123]{lang="EN-US"}[，则密码]{style="font-family:宋体"}[abc123]{lang="EN-US"}[、]{style="font-family:宋体"}[321df]{lang="EN-US"}[就不符合该项复杂度检查。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x2112665177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x2120751426}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。]{style="font-family:宋体"}]{#struct_0_44025_14098_1493606553}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[可以通过多次执行本命令同时打开用户名检查以及连续字符检查功能。]{style="font-family:宋体"}]{#struct_0_44025_14098_x627293796}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_719740543}

[[\# ]{lang="SV"}]{#struct_0_44025_14098_x775775215}[配置密码复杂度检测策略为]{style="font-family:宋体"}[，]{style="font-family:宋体"}[检查配置的密码中是否包含用户名或者字符顺序颠倒的用户名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1359360498}

[\[Sysname\] password-control complexity user-name check]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1360805950}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[local-user]{lang="EN-US"}**]{#struct_0_44025_14098_1756178834}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x831403574}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_44025_14098_1381455667}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-1971229140 .myid}
[]{#_Toc404792922}[]{#struct_0_44025_14098_x1475166733}

**Password Control \-- Password Control 配置命令 \-- password-control composition**

------------------------------------------------------------------------

[**[password-control composition]{lang="EN-US"}**]{#struct_0_44025_14098_x1317052819}[命令用来配置用户密码的组合策略。]{style="font-family:
宋体"}

[**[undo password-control composition]{lang="EN-US"}**]{#struct_0_44025_14098_x8985307}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1223509865}

[**[password-control composition type-number ]{lang="EN-US"}***[type-number]{lang="EN-US"}*[ \[ **type-length** *type-length* \]]{lang="EN-US"}]{#struct_0_44025_14098_1637239978}

[**[undo password-control composition]{lang="EN-US"}**]{#struct_0_44025_14098_x1359426034}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x765522618}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_1595148889}[模式下：]{style="font-family:宋体"}

[[全局的密码元素的最少组合类型为]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_44025_14098_x2035305555}[种，至少要包含每种元素的个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[个；用户组的密码组合策略为全局配置的密码组合策略；本地用户的密码组合策略为所属用户组的密码组合策略。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x1123788942}[模式下：]{style="font-family:宋体"}

[[全局的密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_44025_14098_x1285030536}[种，至少要包含每种元素的个数为]{style="font-family:宋体"}[1]{lang="EN-US"}[个；用户组的密码组合策略为全局配置的密码组合策略；本地用户的密码组合策略为所属用户组的密码组合策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_1483592982}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_44025_14098_2020052385}[用户组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[本地用户视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x2013982579}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1359884785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_193102504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_793824792}

[**[type-number]{lang="EN-US"}***[ type-number]{lang="EN-US"}*]{#struct_0_44025_14098_2134089092}[：密码元素的最少组合类型。其中，]{style="font-family:宋体"}*[type-number]{lang="EN-US"}*[表示组合类型的个数，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[；]{style="font-family:
宋体"}[FIPS]{lang="EN-US"}[模式下，取值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type-length]{lang="EN-US"}***[ type-length]{lang="EN-US"}*]{#struct_0_44025_14098_x1588119344}[：密码中至少要包含每种元素的个数。其中，]{style="font-family:宋体"}*[type-length]{lang="EN-US"}*[表示元素个数，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_1354282576}

[[系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1994441698}

[[该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。]{style="font-family:宋体"}]{#struct_0_44025_14098_x37988544}

[[密码元素的最少组合类型数以及每种元素的最小个数的乘积应该小于允许的最大密码长度。]{style="font-family:宋体"}]{#struct_0_44025_14098_556032208}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359950321}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x30695849}[配置全局的密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[种，至少要包含每种元素的个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_1029609128}

[\[Sysname\] password-control composition type-number 4 type-length 5]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_2103594255}[配置用户组]{style="font-family:宋体"}[test]{lang="EN-US"}[的密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[种，至少要包含每种元素的个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\[Sysname\] user-group test]{lang="EN-US"}]{#struct_0_44025_14098_x2078610949}

[\[Sysname-ugroup-test\] password-control composition type-number 4 type-length 5]{lang="EN-US"}

[\[Sysname-ugroup-test\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x705727823}[配置设备管理类本地用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[种，至少要包含每种元素的个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\[Sysname\] local-user abc class manage]{lang="EN-US"}]{#struct_0_44025_14098_x1800908973}

[\[Sysname-luser-manage-abc\] password-control composition type-number 4 type-length 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1360015857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[local-user]{lang="EN-US"}**]{#struct_0_44025_14098_x1903134571}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_2034070062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_44025_14098_996608160}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control composition enable]{lang="EN-US"}**]{#struct_0_44025_14098_x702028305}
:::

::: {#1711839785 .myid}
[]{#_Toc404792923}[]{#struct_0_44025_14098_x2137418411}

**Password Control \-- Password Control 配置命令 \-- password-control enable**

------------------------------------------------------------------------

[**[password-control enable]{lang="EN-US"}**]{#struct_0_44025_14098_1440895351}[命令用来使能全局密码管理功能。]{style="font-family:宋体"}

[**[undo password-control enable]{lang="EN-US"}**]{#struct_0_44025_14098_944760064}[命令用来关闭全局密码管理功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x958373576}

[**[password-control enable]{lang="EN-US"}**]{#struct_0_44025_14098_x1360081393}

[[ **undo password-control enable**]{lang="EN-US"}]{#struct_0_44025_14098_x407332817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_1116276684}

[[[非]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_44025_14098_1731841517}[[FIPS]{lang="EN-US"}]{.ItemStepChar}[[模式下：]{style="font-family:宋体"}]{.ItemStepChar}

[[[全局密码管理功能处于关闭状态]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_44025_14098_x644026731}[。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x923230344}[模式下：]{style="font-family:宋体"}

[[[全局密码管理功能处于开启状态，切不能关闭。]{style="font-family:宋体"}]{.ItemStepChar}]{#struct_0_44025_14098_2090270898}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1765911350}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x472291696}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_1058639161}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_1554994438}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1348841090}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359622641}

[[只有在使能了全局密码管理功能的情况下，其它指定的密码管理功能才能生效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x984824263}

[[需要注意的是，使能全局密码管理功能后：]{style="font-family:宋体"}]{#struct_0_44025_14098_482809816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备管理类本地用户密码以及]{style="font-family:宋体"}]{#struct_0_44025_14098_x508378193}[super]{lang="EN-US"}[密码的配置将不被显示，即无法通过相应的]{style="font-family:宋体"}**[display]{lang="EN-US"}**[命令查看到设备管理类本地用户密码以及]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的配置。网络接入类本地用户密码不受密码管理功能控制，其配置显示也不受影响。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[首次设置的设备管理类本地用户密码必须至少由四个不同的字符组成。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1232955921}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_523513864}[模式下，不能关闭全局]{lang="EN-US" style="font-family:宋体"}[Password Control]{lang="EN-US"}[功能，即]{lang="EN-US" style="font-family:宋体"}**[undo password control enable]{lang="EN-US"}**[命令执行后不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1135367988}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x725675466}[使能全局密码管理功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_1004381130}

[\[Sysname\] password-control enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359688177}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x1319474204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control ]{lang="EN-US"}**[{ **aging** \| **composition** \| **history** \| **length** } **enable**]{lang="EN-US"}]{#struct_0_44025_14098_550367914}
:::

::: {#85356808 .myid}
[]{#_Toc404792924}[]{#struct_0_44025_14098_765209890}

**Password Control \-- Password Control 配置命令 \-- password-control expired-user-login**

------------------------------------------------------------------------

[**[password-control ]{lang="SV"}[expired-user-login]{lang="EN-US"}**]{#struct_0_44025_14098_1180676194}[命令用来配置密码过期后允许用户登录的时间和次数。]{style="font-family:宋体"}

[**[undo password-control ]{lang="SV"}[expired-user-login]{lang="EN-US"}**]{#struct_0_44025_14098_994533485}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_940478354}

[**[password-control expired-user-login delay ]{lang="EN-US"}***[delay]{lang="EN-US"}***[ times ]{lang="EN-US"}***[times]{lang="EN-US"}*]{#struct_0_44025_14098_58641658}

[[ **undo password-control expired-user-login**]{lang="EN-US"}]{#struct_0_44025_14098_x2014344557}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359753713}

[[密码过期后允许登录的时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_44025_14098_1010993033}[天，允许登录的次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次，即密码过期后系统还允许用户在]{style="font-family:宋体"}[30]{lang="EN-US"}[天内登录]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_1142662700}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x262907298}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_1036734959}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x243580333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_1355682094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x18924640}

[**[delay ]{lang="EN-US"}***[delay]{lang="EN-US"}*]{#struct_0_44025_14098_75771262}[：]{style="font-family:
宋体"}[密码过期后允许用户登录的时长，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[90]{lang="EN-US"}[，单位为天。]{style="font-family:宋体"}

[**[times ]{lang="EN-US"}***[times]{lang="EN-US"}*]{#struct_0_44025_14098_x1359819249}[：]{style="font-family:宋体"}[密码过期后允许用户登录的最大次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示密码过期后不允许用户登录。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_259922282}

[[该配置仅对非]{style="font-family:宋体"}]{#struct_0_44025_14098_1075667637}[FTP]{lang="SV"}[类型的]{style="font-family:宋体"}[Login]{lang="SV"}[用户生效。对于]{style="font-family:宋体"}[FTP]{lang="SV"}[用户，密码过期后，系统不允许其继续登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1170506807}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_2137844384}[设定允许用户在密码过期之后的]{style="font-family:宋体"}[60]{lang="EN-US"}[天内登录]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_1093219630}

[\[Sysname\] password-control expired-user-login delay 60 times 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1659715449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_425450916}
:::

::: {#640802075 .myid}
[]{#_Toc404792925}[]{#struct_0_44025_14098_549535860}

**Password Control \-- Password Control 配置命令 \-- password-control history**

------------------------------------------------------------------------

[**[password-control history]{lang="EN-US"}**]{#struct_0_44025_14098_x1359360497}[命令用来配置每个用户密码历史记录的最大条数。]{style="font-family:
宋体"}

[**[undo password-control history]{lang="EN-US"}**]{#struct_0_44025_14098_655616685}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x211006579}

[**[password-control history ]{lang="EN-US"}***[max-record-num]{lang="EN-US"}*]{#struct_0_44025_14098_x541345044}

[**[undo password-control history]{lang="EN-US"}**]{#struct_0_44025_14098_x409160905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_549712095}

[[每个用户密码历史记录的最大条数为]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_44025_14098_x497137785}[条。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x443704779}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x330285308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359426033}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_1607130377}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x2104548401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1303168071}

[*[max-record-num]{lang="EN-US"}*]{#struct_0_44025_14098_x1245373912}[：每个用户密码历史记录的最大条数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_1345839810}

[[当记录的某用户的历史密码条数达到最大值后，该用户的后续新密码历史记录将覆盖最老的一条密码历史记录。]{style="font-family:宋体"}]{#struct_0_44025_14098_1402035264}

[[密码历史记录管理功能关闭后，系统将不再记录历史密码，但之前已经存在的密码历史记录依然保存。只有当关闭全局密码管理功能（]{style="font-family:宋体"}**[undo password-control enable]{lang="EN-US"}**]{#struct_0_44025_14098_572091127}[）或手动清除历史密码记录时（]{style="font-family:
宋体"}**[reset password-control history-record]{lang="EN-US"}**[），历史密码记录才会被清除掉。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_875468396}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x1359884788}[配置每个用户密码历史记录的最大条数为]{style="font-family:宋体"}[10]{lang="EN-US"}[条。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_952617391}

[\[Sysname\] password-control history 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x105992296}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x239400806}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control history enable]{lang="EN-US"}**]{#struct_0_44025_14098_x246357357}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_1500957163}
:::

::: {#-398409104 .myid}
[]{#_Toc404792926}[]{#struct_0_44025_14098_897024153}

**Password Control \-- Password Control 配置命令 \-- password-control length**

------------------------------------------------------------------------

[**[password-control length]{lang="EN-US"}**]{#struct_0_44025_14098_x963192262}[命令用来配置密码的最小长度。]{style="font-family:宋体"}

[**[undo password-control length]{lang="EN-US"}**]{#struct_0_44025_14098_x1359950324}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x790210736}

[**[password-control length ]{lang="EN-US"}***[length]{lang="EN-US"}*]{#struct_0_44025_14098_x434821759}

[**[undo password-control length]{lang="EN-US"}**]{#struct_0_44025_14098_714501751}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_1955849032}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x580234169}[模式下：]{style="font-family:宋体"}

[[全局的密码最小长度为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_44025_14098_1881216685}[个字符；用户组的密码最小长度为全局配置的密码最小长度；本地用户的密码最小长度为所属用户组的密码最小长度。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x220110622}[模式下：]{style="font-family:宋体"}

[[全局的密码最小长度为]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_44025_14098_x2119696173}[个字符；用户组的密码最小长度为全局配置的密码最小长度；本地用户的密码最小长度为所属用户组的密码最小长度。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1360015860}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_44025_14098_469321816}[用户组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[本地用户视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_1240440589}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_312951642}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x784907633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1885578016}

[*[length]{lang="EN-US"}*]{#struct_0_44025_14098_x832318984}[：密码的最小长度，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1883928814}

[[系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1495867560}

[[该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1360081396}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_352182070}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1036134901}[配置全局的密码最小长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x243055984}

[\[Sysname\] password-control length 16]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_618246801}[配置用户组]{style="font-family:宋体"}[test]{lang="EN-US"}[的密码最小长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[\[Sysname\] user-group test]{lang="EN-US"}]{#struct_0_44025_14098_1703064722}

[\[Sysname-ugroup-test\] password-control length 16]{lang="EN-US"}

[\[Sysname-ugroup-test\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_218232407}[配置设备管理类本地用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的密码最小长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[\[Sysname\] local-user abc class manage]{lang="EN-US"}]{#struct_0_44025_14098_98581687}

[\[Sysname-luser-manage-abc\] password-control length 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359622644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[local-user]{lang="EN-US"}**]{#struct_0_44025_14098_x225309376}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_1478236785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_44025_14098_1406005475}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control length enable]{lang="EN-US"}**]{#struct_0_44025_14098_1496279798}
:::

::: {#-1294342697 .myid}
[]{#_Toc404792927}[]{#struct_0_44025_14098_x62046349}

**Password Control \-- Password Control 配置命令 \-- password-control login idle-time**

------------------------------------------------------------------------

[**[password-control login idle-time]{lang="SV"}**]{#struct_0_44025_14098_1880842033}[命令用来配置用户帐号的闲置时间。]{style="font-family:宋体"}

[**[undo password-control login idle-time]{lang="SV"}**]{#struct_0_44025_14098_1334676789}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x2080166997}

[**[password-control login idle-time ]{lang="EN-US"}***[idle-time]{lang="EN-US"}*]{#struct_0_44025_14098_x1359688180}

[**[undo password-control login idle-time]{lang="EN-US"}**]{#struct_0_44025_14098_x2079972131}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1091314262}

[[用户帐号的闲置时间为]{style="font-family:宋体"}[90]{lang="EN-US"}]{#struct_0_44025_14098_803267475}[天。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_360733691}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_970523707}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x276783225}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x628721857}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_112555544}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359753716}

[*[idle-time]{lang="EN-US"}*]{#struct_0_44025_14098_251478146}[：]{style="font-family:宋体"}[用户帐号的闲置时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[365]{lang="EN-US"}[，单位为天。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示对用户帐号闲置时间无限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1185840145}

[[如果用户自最后一次成功登录后，在指定的闲置时间内再未成功登录过设备，那么该用户帐号将会失效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1119810045}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_2016968529}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_713923633}[设定用户帐号的闲置时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[天，表示自最后一次成功登录后，若用户在]{style="font-family:宋体"}[30]{lang="EN-US"}[天内再未成功登录过设备，那么该用户帐号将会失效。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x668265954}

[\[Sysname\] password-control login idle-time 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x73439323}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x1562683671}
:::

::: {#610903714 .myid}
[]{#_Toc404792928}[]{#struct_0_44025_14098_x1359819252}

**Password Control \-- Password Control 配置命令 \-- password-control login-attempt**

------------------------------------------------------------------------

[**[password-control login-attempt]{lang="EN-US"}**]{#struct_0_44025_14098_x949865763}[命令用来配置允许用户登录的最大尝试次数以及登录尝试失败后的处理措施。]{style="font-family:
宋体"}

[**[undo password-control login-attempt]{lang="EN-US"}**]{#struct_0_44025_14098_x960842753}[命令用来恢复缺省情况]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1241058041}

[**[password-control login-attempt]{lang="EN-US"}***[ login-times]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **exceed** { **lock** \| **lock-time** *time* \| **unlock** } \]]{lang="EN-US"}]{#struct_0_44025_14098_x123213646}

[[ **undo password-control login-attempt**]{lang="EN-US"}]{#struct_0_44025_14098_x12689789}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x220099256}

[[全局的用户登录尝试次数限制策略为：用户登录尝试的最大次数为]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_44025_14098_1713052130}[次。如果某用户登录尝试失败，则]{style="font-family:宋体"}[1]{lang="EN-US"}[分钟后再允许该用户重新登录；用户组的用户登录尝试次数限制策略为全局配置的用户登录尝试次数限制策略；本地用户的登录尝试次数限制策略为所属用户组的用户登录尝试次数限制策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_1952914417}

[[系统视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_44025_14098_x1359360500}[用户组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[本地用户视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1716446485}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1943538519}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1596994218}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1343933201}

[*[login-times]{lang="EN-US"}*]{#struct_0_44025_14098_x443060315}[：用户登录尝试的最大次数，取值范围为]{style="font-family:宋体"}[2]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exceed]{lang="EN-US"}**]{#struct_0_44025_14098_1234702441}[：对登录尝试失败次数超过最大值的用户所采取的处理措施。]{style="font-family:宋体"}

[**[lock]{lang="EN-US"}**]{#struct_0_44025_14098_x1498546700}[：表示永久禁止该用户登录。]{style="font-family:宋体"}

[**[lock-time ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_44025_14098_x1912431468}[：表示禁止该用户一段时间后，再允许该用户重新登录。其中，]{style="font-family:宋体"}*[time]{lang="EN-US"}*[为禁止该用户的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[360]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[**[unlock]{lang="EN-US"}**]{#struct_0_44025_14098_x1359426036}[：表示不禁止该用户，允许其继续登录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1928322032}

[[系统视图下配置具有全局性，对所有用户组有效，用户组视图下的配置对用户组内所有本地用户有效，本地用户视图下的配置只对当前本地用户有效。]{style="font-family:宋体"}]{#struct_0_44025_14098_x508231782}

[[该配置的生效优先级顺序由高到低依次为本地用户视图、用户组视图、全局视图。即，系统优先采用本地用户视图下的配置，若本地用户视图下未配置，则采用用户组视图下的配置，若用户组视图下也未配置，则采用全局视图下的配置。]{style="font-family:宋体"}]{#struct_0_44025_14098_x15899310}

[[用户登录认证失败后，系统会将其加入密码管理的黑名单，当登录失败次数超过指定值后，系统将会根据此处配置的处理措施对其之后的登录行为进行相应的限制，并且该用户只能在满足相应的条件后才可重新登录：]{style="font-family:宋体"}]{#struct_0_44025_14098_x190147299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于被永久禁止登录的用户，只有管理员使用]{lang="EN-US" style="font-family:宋体"}**[reset password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_1146460726}[命令把该用户从密码管理的黑名单中删除后，该用户才能重新登录。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于被禁止一段时间内登录的用户，当配置的禁止时间超时或者管理员使用]{lang="EN-US" style="font-family:宋体"}**[reset password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_x1329773740}[命令将其从密码管理的黑名单中删除，该用户才可以重新登录。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于不禁止登录的用户，只要用户登录成功后，该用户就会从该黑名单中删除。]{style="font-family:宋体"}]{#struct_0_44025_14098_2080818451}

[[本命令生效后，会立即影响密码管理黑名单中当前用户的锁定状态以及这些用户后续的登录。]{style="font-family:宋体"}]{#struct_0_44025_14098_885900566}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1359884787}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1355901918}[管理员设定用户登录尝试次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[次，并且永久禁止该用户登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1141526704}

[\[Sysname\] password-control login-attempt 4 exceed lock]{lang="EN-US"}

[[之后，若有用户连续尝试认证的失败累加次数达到]{style="font-family:宋体"}[4]{lang="EN-US"}]{#struct_0_44025_14098_x2132360124}[次，管理员可通过命令查看到被加入密码管理黑名单中的用户锁定状态由之前的]{style="font-family:宋体"}**[unlock]{lang="EN-US"}**[切换为]{style="font-family:宋体"}**[lock]{lang="EN-US"}**[，且该用户无法再次成功登录。]{style="font-family:宋体"}

[[\[Sysname\] display password-control blacklist]{lang="EN-US"}]{#struct_0_44025_14098_x2132899603}

[ ]{lang="EN-US"}

[ Username: test]{lang="EN-US"}

[    IP: 192.168.44.1        Login failures: 4      [[[Lock flag: lock]{style="border:none"}]{style="border:none"}]{.TerminalDisplayshading}]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Blacklist items matched: 1.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1599699390}[管理员设定用户登录尝试次数为]{style="font-family:宋体"}[2]{lang="EN-US"}[次，并且限制该用户在]{style="font-family:宋体"}[3]{lang="EN-US"}[分钟后才能重新登录。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x60080384}

[\[Sysname\] password-control login-attempt 2 exceed lock-time 3]{lang="EN-US"}

[[之后，若有用户连续尝试认证的失败累加次数达到]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_44025_14098_x1359950323}[次，管理员可通过命令查看到被加入密码管理黑名单中的用户锁定状态由之前的]{style="font-family:宋体"}**[unlock]{lang="EN-US"}**[切换为]{style="font-family:宋体"}**[lock]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\[Sysname\] display password-control blacklist]{lang="EN-US"}]{#struct_0_44025_14098_1132103565}

[ ]{lang="EN-US"}

[ Username: test]{lang="EN-US"}

[    IP: 192.168.44.1        Login failures: 2      [[[Lock flag: lock]{style="border:none"}]{style="border:none"}]{.TerminalDisplayshading}]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Blacklist items matched: 1.]{lang="EN-US"}

[[用户被禁止登录]{style="font-family:宋体"}[3]{lang="EN-US"}]{#struct_0_44025_14098_542411161}[分钟后，将被从密码管理黑名单中删除，且可以重新登录。]{style="font-family:宋体"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1762420903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[local-user]{lang="EN-US"}**]{#struct_0_44025_14098_1101330789}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_1600136197}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_x1764422409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_44025_14098_1640119922}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/AAA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_x1360015859}
:::

::: {#1773370248 .myid}
[]{#_Toc404792929}[]{#struct_0_44025_14098_x1452795877}

**Password Control \-- Password Control 配置命令 \-- password-control super aging**

------------------------------------------------------------------------

[**[password-control super aging]{lang="EN-US"}**]{#struct_0_44025_14098_x334069826}[命令用来配置]{style="font-family:
宋体"}[super]{lang="EN-US"}[密码的老化时间。]{style="font-family:宋体"}

[**[undo password-control super aging]{lang="EN-US"}**]{#struct_0_44025_14098_1056641518}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1363521587}

[**[password-control super aging ]{lang="EN-US"}***[aging-time]{lang="EN-US"}*]{#struct_0_44025_14098_457099212}

[[ **undo password-control super aging**]{lang="EN-US"}]{#struct_0_44025_14098_x1399846926}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_2025172272}

[[密码的老化时间为]{style="font-family:宋体"}[90]{lang="EN-US"}]{#struct_0_44025_14098_2021789741}[天。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1360081395}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_755466597}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_293782364}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x356418511}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x197159072}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1590299690}

[*[aging-time]{lang="EN-US"}*]{#struct_0_44025_14098_x1436205196}[：]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的老化时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[365]{lang="EN-US"}[，单位为天。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_1605269474}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x86032991}[设定]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的老化时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[天。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1359622643}

[\[Sysname\] password-control super aging 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_2147343619}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_678478358}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control aging]{lang="EN-US"}**]{#struct_0_44025_14098_x2000034750}
:::

::: {#-968270914 .myid}
[]{#_Toc404792930}[]{#struct_0_44025_14098_x1082147727}

**Password Control \-- Password Control 配置命令 \-- password-control super composition**

------------------------------------------------------------------------

[**[password-control super composition]{lang="EN-US"}**]{#struct_0_44025_14098_x520616739}[命令用来配置]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的组合策略。]{style="font-family:宋体"}

[**[undo password-control super composition]{lang="EN-US"}**]{#struct_0_44025_14098_x1300096926}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1850189838}

[**[password-control super composition type-number ]{lang="EN-US"}***[type-number]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **type-length** *type-length* \]]{lang="EN-US"}]{#struct_0_44025_14098_x297011734}

[[ **undo password-control super composition**]{lang="EN-US"}]{#struct_0_44025_14098_x1359688179}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x156674790}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_1936793702}[模式下：]{style="font-family:宋体"}

[[super]{lang="EN-US"}]{#struct_0_44025_14098_x790722219}[密码的最少组合类型为]{style="font-family:宋体"}[1]{lang="EN-US"}[种，每种类型至少包含]{style="font-family:宋体"}[1]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_1125858576}[模式下：]{style="font-family:宋体"}

[[super]{lang="EN-US"}]{#struct_0_44025_14098_x950872139}[密码的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[种，每种类型至少包含]{style="font-family:宋体"}[1]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_1654589912}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x1285598039}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_48013776}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1359753715}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_1817562087}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1667439444}

[**[type-number]{lang="EN-US"}***[ type-number]{lang="EN-US"}*]{#struct_0_44025_14098_1377248006}[：]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的最少组合类型。其中，]{style="font-family:宋体"}*[type-number]{lang="EN-US"}*[表示组合类型，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4]{lang="EN-US"}[；]{style="font-family:
宋体"}[FIPS]{lang="EN-US"}[模式下，取值为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[type-length]{lang="EN-US"}***[ type-length]{lang="EN-US"}*]{#struct_0_44025_14098_798658673}[：]{style="font-family:宋体"}[super]{lang="EN-US"}[密码中每种类型的最少字符个数。其中，]{style="font-family:宋体"}*[type-length]{lang="EN-US"}*[表示字符个数，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x823245182}

[[密码元素的最少组合类型数以及每种元素的最小个数的乘积应该小于密码允许的最大长度。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1222597923}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x990779998}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1321864414}[配置]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[种，每种类型的最少字符个数为]{style="font-family:宋体"}[5]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x1359819251}

[\[Sysname\] password-control super composition type-number 4 type-length 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_616218178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x964646263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control composition]{lang="EN-US"}**]{#struct_0_44025_14098_x1766728406}
:::

::: {#-1411580040 .myid}
[]{#_Toc404792931}[]{#struct_0_44025_14098_x1721262971}

**Password Control \-- Password Control 配置命令 \-- password-control super length**

------------------------------------------------------------------------

[**[password-control super length]{lang="EN-US"}**]{#struct_0_44025_14098_x635293341}[命令用来配置]{style="font-family:
宋体"}[super]{lang="EN-US"}[密码的最小长度。]{style="font-family:宋体"}

[**[undo password-control super length]{lang="EN-US"}**]{#struct_0_44025_14098_2122929799}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x19447936}

[**[password-control super length ]{lang="EN-US"}***[length]{lang="EN-US"}*]{#struct_0_44025_14098_x1794896712}

[[ **undo password-control super length**]{lang="EN-US"}]{#struct_0_44025_14098_x1359360499}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_205277991}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x1115666259}[模式下：]{style="font-family:宋体"}

[[super]{lang="EN-US"}]{#struct_0_44025_14098_x2138339642}[密码的最小长度为]{style="font-family:宋体"}[10]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_44025_14098_x861024951}[模式下：]{style="font-family:宋体"}

[[super]{lang="EN-US"}]{#struct_0_44025_14098_x1659768121}[密码的最小长度为]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_x609378733}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x1141860875}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_653786528}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1359426035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_800561323}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1573402471}

[*[length]{lang="EN-US"}*]{#struct_0_44025_14098_x651836355}[：]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的最小字符长度，非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[4]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，取值范围为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x597477529}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x258565439}[设定]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的最小长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x75519134}

[\[Sysname\] password-control super length 16]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_497188198}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x1300256263}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control length]{lang="EN-US"}**]{#struct_0_44025_14098_206199157}
:::

::: {#858021343 .myid}
[]{#_Toc404792932}[]{#struct_0_44025_14098_x1001145706}

**Password Control \-- Password Control 配置命令 \-- password-control update-interval**

------------------------------------------------------------------------

[**[password-control ]{lang="SV"}[update-interval]{lang="EN-US"}**]{#struct_0_44025_14098_x1356891751}[命令用来配置密码更新的最小时间间隔。]{style="font-family:
宋体"}

[**[undo password-control ]{lang="SV"}[update-interval]{lang="EN-US"}**]{#struct_0_44025_14098_1285843610}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1595081166}

[**[password-control update-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_44025_14098_x954473449}

[[ **undo password-control update-interval** ]{lang="EN-US"}]{#struct_0_44025_14098_x2112711492}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_44025_14098_x144527741}

[[密码更新的最小时间间隔为]{style="font-family:宋体"}[24]{lang="EN-US"}]{#struct_0_44025_14098_1181534764}[小时。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_206133621}

[[系统视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x1037958583}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_431388863}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x2119068783}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_254547285}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_1324699301}

[*[interval]{lang="EN-US"}*]{#struct_0_44025_14098_80104721}[：]{style="font-family:宋体"}[密码更新的最小时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[168]{lang="EN-US"}[，单位为小时。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示对密码更新的时间间隔无限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_1531579639}

[[有两种情况下的密码更新并不受该功能的约束：用户首次登录设备时系统要求用户修改密码；密码老化后系统要求用户修改密码。]{style="font-family:宋体"}]{#struct_0_44025_14098_x1984019275}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_206068085}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_1352746898}[设定密码更新的最小时间间隔为]{style="font-family:宋体"}[36]{lang="EN-US"}[小时。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_44025_14098_x605525753}

[\[Sysname\] password-control update-interval 36]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x82102196}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control]{lang="EN-US"}**]{#struct_0_44025_14098_x688622323}
:::

::: {#1361757489 .myid}
[]{#_Toc404792933}[]{#struct_0_44025_14098_x515351565}[]{#_Toc300926441}[]{#_Toc259634105}

**Password Control \-- Password Control 配置命令 \-- reset password-control blacklist**

------------------------------------------------------------------------

[**[reset password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_1577409978}[命令用来清除密码管理黑名单中的用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1404705550}

[**[reset password-control blacklist ]{lang="EN-US"}**[\[ **user-name** *name* \]]{lang="EN-US"}]{#struct_0_44025_14098_x727487851}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_206002549}

[[用户视图]{style="font-family:宋体"}]{#struct_0_44025_14098_x1405055413}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_x888383976}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_767217653}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_530503424}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1175067314}

[**[user-name]{lang="EN-US"}***[ name]{lang="EN-US"}*]{#struct_0_44025_14098_1957428747}[：清除密码管理黑名单中指定的用户。其中，]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1058289311}

[[对于因为登录认证时密码尝试的失败次数超过最大值而被禁止登录的用户，管理员可以使用本命令将其从黑名单中删除，使其可以重新登录。]{style="font-family:宋体"}]{#struct_0_44025_14098_1457965094}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_206461301}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x1261132449}[清除密码管理黑名单中的用户]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset password-control blacklist user-name test]{lang="EN-US"}]{#struct_0_44025_14098_1428899483}

[Are you sure to delete the specified user in blacklist? \[Y/N\]:]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1705489325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display password-control blacklist]{lang="EN-US"}**]{#struct_0_44025_14098_x19253881}
:::

::: {#-2117827540 .myid}
[]{#_Toc404792934}[]{#struct_0_44025_14098_1484161327}

**Password Control \-- Password Control 配置命令 \-- reset password-control history-record**

------------------------------------------------------------------------

[**[reset password-control history-record]{lang="EN-US"}**]{#struct_0_44025_14098_x1641223188}[命令用来清除用户的密码历史记录。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_1726362961}

[**[reset password-control history-record ]{lang="EN-US"}**[\[ **super** \[ **role** *role-name* \] \| **user-name** *name* \]]{lang="EN-US"}]{#struct_0_44025_14098_1290476858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_44025_14098_206395765}

[[用户视图]{style="font-family:宋体"}]{#struct_0_44025_14098_1954379322}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_44025_14098_598431091}

[[network-admin]{lang="EN-US"}]{#struct_0_44025_14098_x654678382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_44025_14098_x1670146134}

[[【参数】]{style="font-family:黑体"}]{#struct_0_44025_14098_x746788125}

[**[super]{lang="EN-US"}**]{#struct_0_44025_14098_1767224902}[：删除]{style="font-family:宋体"}[super]{lang="EN-US"}[密码的历史记录。]{style="font-family:宋体"}

[**[role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_44025_14098_1068770937}[：删除指定用户角色的用户密码历史记录。其中，]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[表示用户角色，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[user-name]{lang="EN-US"}***[ name]{lang="EN-US"}*]{#struct_0_44025_14098_x433302674}[：删除指定用户名的密码历史记录。其中，]{style="font-family:宋体"}*[name]{lang="EN-US"}*[表示用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_44025_14098_206330229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，将删除所有本地用户的密码历史记录。]{style="font-family:宋体"}]{#struct_0_44025_14098_436678629}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定参数]{lang="EN-US" style="font-family:宋体"}*[role-name]{lang="EN-US"}*]{#struct_0_44025_14098_x1386284345}[，将删除所有]{lang="EN-US" style="font-family:宋体"}[super]{lang="EN-US"}[密码的历史记录。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1874790622}

[[\# ]{lang="EN-US"}]{#struct_0_44025_14098_x1474803191}[清除所有本地用户的密码历史记录。当用户输入]{style="font-family:宋体"}[Y]{lang="EN-US"}[，系统将删除所有本地用户的密码历史记录。]{style="font-family:宋体"}

[[\<Sysname\> reset password-control history-record]{lang="EN-US"}]{#struct_0_44025_14098_556049716}

[Are you sure to delete all local user's history records? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_44025_14098_x1944292466}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[password-control history]{lang="EN-US"}**]{#struct_0_44025_14098_388222481}
:::
