::: {#1930435702 .myid}
[]{#_Toc404797073}[]{#struct_0_13006_x2365_x1955111915}[]{#_Toc257625602}

**CWMP \-- CWMP配置命令 \-- cwmp**

------------------------------------------------------------------------

[**[cwmp]{lang="EN-US"}**]{#struct_0_13006_x2365_x783151665}[命令用来进入]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1225570559}

[**[cwmp]{lang="EN-US"}**]{#struct_0_13006_x2365_x1231736006}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1742809939}

[[系统视图]{style="font-family:宋体"}]{#struct_0_13006_x2365_1305846376}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x363394019}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1610281808}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_342921419}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_701913271}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x911677156}[进入]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x2077145219}

[\[Sysname\] cwmp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1438319362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp enable]{lang="EN-US"}**]{#struct_0_13006_x2365_1173898617}
:::

::: {#-2020123647 .myid}
[]{#_Toc404797074}[]{#struct_0_13006_x2365_756322086}

**CWMP \-- CWMP配置命令 \-- cwmp acs default password**

------------------------------------------------------------------------

[**[cwmp acs default password]{lang="EN-US"}**]{#struct_0_13006_x2365_1930902025}[命令用来配置]{style="font-family:
宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省密码。]{style="font-family:宋体"}

[**[undo cwmp acs default password]{lang="EN-US"}**]{#struct_0_13006_x2365_1924988200}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x15345775}

[**[cwmp acs ]{lang="EN-US"}[default password ]{lang="EN-US"}**]{#struct_0_13006_x2365_1438237263}[{ **cipher** \| **simple** }]{lang="EN-US"}[ *password*]{lang="EN-US"}

[**[undo cwmp acs ]{lang="EN-US"}[default password]{lang="EN-US"}**]{#struct_0_13006_x2365_1606662030}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1320142224}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1480114858}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1777972796}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1077023606}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1583015389}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x911742692}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_276359571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_2131529333}

[**[cipher]{lang="EN-US"}**]{#struct_0_13006_x2365_1020934391}[：表示以密文方式设置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省密码，并以密文形式保存到配置文件。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13006_x2365_x1203347370}[：表示以明文方式设置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省密码，并以密文方式保存到配置文件。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_13006_x2365_124357887}[：设备向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[发送连接请求时携带的缺省密码，区分大小写。当以明文方式配置时，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串；以密文方式配置时，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1379473402}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当设备和]{style="font-family:宋体"}]{#struct_0_13006_x2365_753619065}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接且通过用户名和密码进行认证时，会将缺省用户名和该密码发送给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[，以便]{style="font-family:宋体"}[ACS]{lang="EN-US"}[对设备的身份进行认证。]{style="font-family:宋体"}[ACS]{lang="EN-US"}[根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用该命令配置不同的密码时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_1908669304}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置为可选配置，可以只用用户名验证，但]{style="font-family:宋体"}]{#struct_0_13006_x2365_1884044571}[ACS]{lang="EN-US"}[和]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上的配置必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x127841821}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_504460921}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省密码为]{style="font-family:宋体"}[newpsw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_2125090058}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs default password simple newpsw]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_258877284}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default url]{lang="EN-US"}**]{#struct_0_13006_x2365_x1005813345}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default username]{lang="EN-US"}**]{#struct_0_13006_x2365_x911546084}
:::

::: {#129766278 .myid}
[]{#_Toc404797075}[]{#struct_0_13006_x2365_x1310803012}

**CWMP \-- CWMP配置命令 \-- cwmp acs default url**

------------------------------------------------------------------------

[**[cwmp acs default url]{lang="EN-US"}**]{#struct_0_13006_x2365_87399990}[命令]{style="font-family:宋体"}[用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cwmp acs default url]{lang="EN-US"}**]{#struct_0_13006_x2365_x132368789}[命令用来]{style="font-family:
宋体"}[恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1453029614}

[**[cwmp acs default url ]{lang="EN-US"}***[url]{lang="EN-US"}*]{#struct_0_13006_x2365_1008399029}

[**[undo cwmp acs default url]{lang="EN-US"}**]{#struct_0_13006_x2365_x372621950}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x2097115607}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1407354472}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1970866568}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1076738806}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1176924210}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x228979693}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x1932125383}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x2110426356}

[*[url]{lang="EN-US"}*]{#struct_0_13006_x2365_x911611620}[：]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，格式必须为：]{style="font-family:宋体"}[http://*host*\[:*port*\]/*path*]{lang="EN-US"}[或者]{style="font-family:宋体"}[https://*host*\[:*port*\]/*path*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1281008062}

[[当用户没有为]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_x44317808}[配置]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址，也没有通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获取到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[地址时，设备会尝试和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_15775131}[建立连接时，使用的]{style="font-family:宋体"}[用户名和密码必须和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[上创建的用户名和密码一致，否则，连接建立失败。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1471584738}[只能配置一个连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[和缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[。多次使用该命令配置不同的]{style="font-family:宋体"}[URL]{lang="EN-US"}[时，以最新的配置为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x9435441}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x821469146}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://www.acs.com:80/acs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_1187125967}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs default url http://www.acs.com:80/acs]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x954155428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default password]{lang="EN-US"}**]{#struct_0_13006_x2365_1015196413}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default username]{lang="EN-US"}**]{#struct_0_13006_x2365_x308548035}
:::

::: {#-644757481 .myid}
[]{#_Toc404797076}[]{#struct_0_13006_x2365_868128282}

**CWMP \-- CWMP配置命令 \-- cwmp acs default username**

------------------------------------------------------------------------

[**[cwmp acs default username]{lang="EN-US"}**]{#struct_0_13006_x2365_x348018684}[命令用来配置]{style="font-family:
宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省用户名。]{style="font-family:宋体"}

[**[undo cwmp acs default username]{lang="EN-US"}**]{#struct_0_13006_x2365_x858606278}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1779484886}

[**[cwmp acs default username ]{lang="EN-US"}***[username]{lang="EN-US"}*]{#struct_0_13006_x2365_x911415012}

[**[undo cwmp acs default username]{lang="EN-US"}**]{#struct_0_13006_x2365_1427058797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1646188719}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1212225395}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1017636245}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x915513428}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x760712021}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x874050918}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1750073754}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1133299524}

[*[username]{lang="EN-US"}*]{#struct_0_13006_x2365_1643136408}[：]{style="font-family:宋体"}[CPE]{lang="EN-US"}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[发送连接请求时携带的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1086490644}

[[当]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x355436822}[和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接且通过用户名和密码进行认证时，会将该用户名和缺省密码发送给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[，以便]{style="font-family:宋体"}[ACS]{lang="EN-US"}[对设备的身份进行认证。]{style="font-family:宋体"}[ACS]{lang="EN-US"}[根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[多次使用该命令配置不同的用户名时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_427570921}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x911480548}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x1258368351}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省用户名为]{style="font-family:宋体"}[newname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_2002683662}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs default username newname]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_888644370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default password]{lang="EN-US"}**]{#struct_0_13006_x2365_x236119044}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs default url]{lang="EN-US"}**]{#struct_0_13006_x2365_x1237642679}[]{#_Toc257625603}
:::

::: {#1502298734 .myid}
[]{#_Toc404797077}[]{#struct_0_13006_x2365_1992342971}

**CWMP \-- CWMP配置命令 \-- cwmp acs password**

------------------------------------------------------------------------

[**[cwmp acs password]{lang="EN-US"}**]{#struct_0_13006_x2365_x788762727}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的密码。]{style="font-family:宋体"}

[**[undo cwmp acs password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1513530412}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_444393942}

[**[cwmp acs password]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13006_x2365_x794278145}[{ **cipher** \| **simple** } ]{lang="EN-US"}*[password]{lang="EN-US"}*

[**[undo cwmp acs password]{lang="EN-US"}**]{#struct_0_13006_x2365_880181414}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_726274283}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1645731146}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1020349862}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x911283940}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1619233754}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1807038298}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1513801913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x986935422}

[**[cipher]{lang="EN-US"}**]{#struct_0_13006_x2365_333220948}[：表示以密文方式设置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的密码，并以密文形式保存到配置文件。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13006_x2365_1545944220}[：表示以明文方式设置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的密码，并以密文方式保存到配置文件。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_13006_x2365_2074570820}[：设备向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[发送连接请求时携带的密码，区分大小写。当以明文方式配置时，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串；以密文方式配置时，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1097258841}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_13006_x2365_x1765383680}[CPE]{lang="EN-US"}[和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接且通过用户名和密码进行认证时，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[会将用户名和该密码发送给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[，以便]{style="font-family:宋体"}[ACS]{lang="EN-US"}[对设备的身份进行认证。]{style="font-family:宋体"}[ACS]{lang="EN-US"}[根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用该命令配置密码时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_1714096118}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置为可选配置，可以只用用户名验证，但]{style="font-family:宋体"}]{#struct_0_13006_x2365_x127013285}[ACS]{lang="EN-US"}[和]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上的配置必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x242000323}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_1735987308}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的密码为]{style="font-family:宋体"}[newpsw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x911349476}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs password simple newpsw]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1316093312}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs url]{lang="EN-US"}**]{#struct_0_13006_x2365_x359191670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs username]{lang="EN-US"}**]{#struct_0_13006_x2365_x1106018970}
:::

::: {#-1059989098 .myid}
[]{#_Toc404797078}[]{#struct_0_13006_x2365_x532560324}

**CWMP \-- CWMP配置命令 \-- cwmp acs url**

------------------------------------------------------------------------

[**[cwmp acs url]{lang="EN-US"}**]{#struct_0_13006_x2365_x1312562571}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo cwmp acs url]{lang="EN-US"}**]{#struct_0_13006_x2365_1803950562}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x574348603}

[**[cwmp acs url ]{lang="EN-US"}***[url]{lang="EN-US"}*]{#struct_0_13006_x2365_x13476507}

[**[undo cwmp acs url]{lang="EN-US"}**]{#struct_0_13006_x2365_34970542}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_2137594650}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1642514860}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_90241222}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_85659202}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x107854625}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1995359316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x911808227}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1728022533}

[*[url]{lang="EN-US"}*]{#struct_0_13006_x2365_x1217564886}[：指定]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[8]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，格式必须为：]{style="font-family:宋体"}[http://*host*\[:*port*\]/*path*]{lang="EN-US"}[或者]{style="font-family:宋体"}[https://*host*\[:*port*\]/*path*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1364741048}

[[配置该命令后，如果有连接需求，则设备会向该命令指定的]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_x1076318357}[发起]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接请求。]{style="font-family:宋体"}

[[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_x1390800405}[有三种指定方式，按照优先级从高到底依次为：通过该命令指定，通过]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[协议从]{style="font-family:宋体"}[DHCP]{lang="EN-US"}[服务器获取，通过]{style="font-family:宋体"}**[cwmp acs default url]{lang="EN-US"}**[命令指定。当通过优先级高的方式获取不到]{style="font-family:宋体"}[URL]{lang="EN-US"}[时，再尝试优先级低的方式。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1179780093}[只能配置一个连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[和缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[。当多次使用该命令配置不同的]{style="font-family:宋体"}[URL]{lang="EN-US"}[时，以最新的配置为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1759379915}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x768783705}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://www.acs.com:80/acs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_176455479}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs url http://www.acs.com:80/acs]{lang="EN-US"}
:::

::: {#2040543554 .myid}
[]{#_Toc404797079}[]{#struct_0_13006_x2365_x757193317}

**CWMP \-- CWMP配置命令 \-- cwmp acs username**

------------------------------------------------------------------------

[**[cwmp acs username]{lang="EN-US"}**]{#struct_0_13006_x2365_x1163488205}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的用户名。]{style="font-family:宋体"}

[**[undo cwmp acs username]{lang="EN-US"}**]{#struct_0_13006_x2365_x1951919045}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_270994786}

[**[cwmp acs username ]{lang="EN-US"}***[username]{lang="EN-US"}*]{#struct_0_13006_x2365_x911873763}

[**[undo cwmp acs username]{lang="EN-US"}**]{#struct_0_13006_x2365_x489917106}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1165140768}

[[未配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1482402897}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1813052836}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1699449889}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_538169755}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x1088961272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1313916377}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x107221705}

[*[username]{lang="EN-US"}*]{#struct_0_13006_x2365_79455579}[：]{style="font-family:宋体"}[CPE]{lang="EN-US"}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[发送连接请求时携带的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x517018551}

[[当]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x902924659}[和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接且通过用户名和密码进行认证时，会将用户名和该密码发送给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[，以便]{style="font-family:宋体"}[ACS]{lang="EN-US"}[对设备的身份进行认证。]{style="font-family:宋体"}[ACS]{lang="EN-US"}[根据本地配置的用户名和密码验证设备是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[当多次使用该命令配置不同的用户名时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_1956168752}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_825608655}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_448955133}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的用户名为]{style="font-family:宋体"}[newname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x911677155}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp acs username newname]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x2077079683}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp acs password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1114650981}
:::

::: {#-440410283 .myid}
[]{#_Toc257625606}[]{#_Toc404797080}[]{#struct_0_13006_x2365_x504860341}

**CWMP \-- CWMP配置命令 \-- cwmp cpe connect interface**

------------------------------------------------------------------------

[**[cwmp cpe connect interface]{lang="EN-US"}**]{#struct_0_13006_x2365_1464201697}[命令用来设置]{style="font-family:
宋体"}[CPE]{lang="EN-US"}[上用于连接]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的接口。]{style="font-family:宋体"}

[**[undo cwmp cpe connect interface]{lang="EN-US"}**]{#struct_0_13006_x2365_1968425120}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x897803695}

[**[cwmp cpe connect interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13006_x2365_357026015}

[**[undo cwmp cpe connect interface]{lang="EN-US"}**]{#struct_0_13006_x2365_1764764735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x762698285}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_x1725399883}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1070181291}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_622315199}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1067480420}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1950241573}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x911742691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_276556179}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_13006_x2365_810269697}[：指定]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上用于连接]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1462052462}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1005241080}[连接接口指的是]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上用于连接]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的接口。]{style="font-family:宋体"}[CPE]{lang="EN-US"}[会在]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文中携带]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，要求]{style="font-family:宋体"}[ACS]{lang="EN-US"}[通过此]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和自己建立连接；相应的，]{style="font-family:宋体"}[ACS]{lang="EN-US"}[会向该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址回复]{style="font-family:宋体"}[Inform]{lang="EN-US"}[响应报文。]{style="font-family:宋体"}

[[通常情况下，系统会采用一定的机制去自动获取一个]{style="font-family:宋体"}[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1075724704}[连接接口，但如果获取的]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接接口不是]{style="font-family:宋体"}[CPE]{lang="EN-US"}[和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[实际相连的接口时，就会导致]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接建立失败。因此，在这种情况下需要手工指定]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1672360112}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_2102605096}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[连接的接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_272195243}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe connect interface gigabitethernet 1/0/1]{lang="EN-US"}
:::

::: {#249982190 .myid}
[]{#_Toc404797081}[]{#struct_0_13006_x2365_x297595062}

**CWMP \-- CWMP配置命令 \-- cwmp cpe connect retry**

------------------------------------------------------------------------

[**[cwmp cpe connect retry]{lang="EN-US"}**]{#struct_0_13006_x2365_39617497}[命令用来配置建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接时，连接失败后自动重新连接的次数。]{style="font-family:宋体"}

[**[undo cwmp cpe connect retry]{lang="EN-US"}**]{#struct_0_13006_x2365_x1350626413}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1611586492}

[**[cwmp cpe connect retry ]{lang="EN-US"}***[times]{lang="EN-US"}*]{#struct_0_13006_x2365_1488973246}

[**[undo cwmp cpe connect retry]{lang="EN-US"}**]{#struct_0_13006_x2365_x911546083}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1310606404}

[[重发次数为无限次，即设备会一直按照一定周期向]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_1664780136}[发送连接请求。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1029854055}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x978296721}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_2002959741}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_458174351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_765783609}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x2132061975}

[*[times]{lang="EN-US"}*]{#struct_0_13006_x2365_727776640}[：重发次数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示不重发。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x222570914}

[[当]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_100467002}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[请求建立连接失败，或者在会话过程中连接异常中止（]{style="font-family:宋体"}[CPE]{lang="EN-US"}[没有收到表示会话正常结束的报文）时，设备可以自动重新发起连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x23845978}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_544215768}[配置建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接时，连接失败后自动重新连接为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_2032987060}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe connect retry 5]{lang="EN-US"}
:::

::: {#-345333279 .myid}
[]{#_Toc404797082}[]{#struct_0_13006_x2365_x911611619}[]{#_Toc257625608}

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform interval**

------------------------------------------------------------------------

[**[cwmp cpe inform interval]{lang="EN-US"}**]{#struct_0_13006_x2365_x1280549309}[命令用来配置周期发送]{style="font-family:
宋体"}[Inform]{lang="EN-US"}[报文的时间间隔。]{style="font-family:
宋体"}

[**[undo cwmp cpe inform interval]{lang="EN-US"}**]{#struct_0_13006_x2365_x838550345}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_32432760}

[**[cwmp cpe inform interval ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_13006_x2365_341407795}

[**[undo cwmp cpe inform interval]{lang="EN-US"}**]{#struct_0_13006_x2365_255160633}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x670278352}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1094475009}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x864373254}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1151828295}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x692730809}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1624778311}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1603131477}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x720529302}

[*[seconds]{lang="EN-US"}*]{#struct_0_13006_x2365_x723772757}[：周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x911415011}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1426862189}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间连接的建立过程需要发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文。通过设置]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文发送参数，可以触发]{style="font-family:宋体"}[CPE]{lang="EN-US"}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[自动发起连接。]{style="font-family:宋体"}

[[该命令用于设置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1099686890}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[[只有在配置了]{style="font-family:宋体"}**[cwmp cpe inform interval enable ]{lang="EN-US"}**]{#struct_0_13006_x2365_x2142576936}[命令时，该命令才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x797501028}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_1533718892}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x146622056}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe inform interval enable]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe inform interval 3600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1675155363}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp cpe inform interval enable]{lang="EN-US"}**]{#struct_0_13006_x2365_826896146}
:::

::: {#-293758437 .myid}
[]{#_Toc404797083}[]{#struct_0_13006_x2365_1823007517}[]{#_Toc257625609}

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform interval enable**

------------------------------------------------------------------------

[**[cwmp cpe inform interval enable]{lang="EN-US"}**]{#struct_0_13006_x2365_711638852}[命令用来使能]{style="font-family:宋体"}[CPE]{lang="EN-US"}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[**[undo cwmp cpe inform interval enable]{lang="EN-US"}**]{#struct_0_13006_x2365_496209940}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_787287692}

[**[cwmp cpe inform interval enable]{lang="EN-US"}**]{#struct_0_13006_x2365_669833257}

[**[undo cwmp cpe inform interval enable]{lang="EN-US"}**]{#struct_0_13006_x2365_405492053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x911480547}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1257647455}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1783323578}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_310328850}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x941637634}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x1175663994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1417018901}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1605347837}

[[使能]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1577745958}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文功能，当设定的周期达到时，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[会自动发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[建立连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x897401267}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x2010599024}[使能]{style="font-family:宋体"}[CPE]{lang="EN-US"}[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_236468694}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe inform interval enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1227095245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp cpe inform interval]{lang="EN-US"}**]{#struct_0_13006_x2365_454938536}
:::

::: {#-931031873 .myid}
[]{#_Toc404797084}[]{#struct_0_13006_x2365_x911283939}[]{#_Toc257625610}

**CWMP \-- CWMP配置命令 \-- cwmp cpe inform time**

------------------------------------------------------------------------

[**[cwmp cpe inform time]{lang="EN-US"}**]{#struct_0_13006_x2365_x1619692505}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[在指定时刻发送一次]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo cwmp cpe inform time]{lang="EN-US"}**]{#struct_0_13006_x2365_1510235177}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x2098830534}

[**[cwmp cpe inform time ]{lang="EN-US"}***[time]{lang="EN-US"}*]{#struct_0_13006_x2365_x561058965}

[**[undo cwmp cpe inform time]{lang="EN-US"}**]{#struct_0_13006_x2365_x1030456443}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x893290569}

[[没有配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x985782915}[定时发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1399170088}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1700686320}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1952976091}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x911349475}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x1315896704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1137688071}

[*[time]{lang="EN-US"}*]{#struct_0_13006_x2365_x1578804284}[：指定]{style="font-family:宋体"}[CPE]{lang="EN-US"}[发送一次]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的日期和时间，格式为：]{style="font-family:宋体"}*[yyyy]{lang="EN-US"}*[-*mm*-*dd*T*hh*:*mm*:*ss*]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1970-01-01T00:00:00]{lang="EN-US"}[～]{style="font-family:宋体"}[2035-12-31T23:59:59]{lang="EN-US"}[，该时间必须大于系统当前时间。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_367660071}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x525783865}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间连接的建立过程需要发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文。通过设置]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文发送参数，可以触发]{style="font-family:宋体"}[CPE]{lang="EN-US"}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[自动发起连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1959895219}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x1813363276}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文的日期和时间为]{style="font-family:宋体"}[2012-12-01T20:00:00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x1520406224}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe inform time 2012-12-01T20:00:00]{lang="EN-US"}
:::

::: {#761549993 .myid}
[]{#_Toc404797085}[]{#struct_0_13006_x2365_1077909028}[]{#_Toc257625611}

**CWMP \-- CWMP配置命令 \-- cwmp cpe password**

------------------------------------------------------------------------

[**[cwmp cpe password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1586750869}[命令用来配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[时的认证密码。]{style="font-family:宋体"}

[**[undo cwmp cpe password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1579289606}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_898636994}

[**[cwmp cpe password]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_13006_x2365_1983602979}[{ **cipher** \| **simple** } ]{lang="EN-US"}*[password]{lang="EN-US"}*

[**[undo cwmp cpe password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1683976717}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_654275717}

[[未配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_244899393}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的密码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1126678894}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1418274691}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_796864501}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1048674342}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x93097692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_405010880}

[**[cipher]{lang="EN-US"}**]{#struct_0_13006_x2365_x982403963}[：表示以密文方式设置连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的密码，并以密文形式保存到配置文件。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_13006_x2365_642568277}[：表示以明文方式设置连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的密码，并以密文方式保存到配置文件。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_13006_x2365_157023846}[：]{style="font-family:宋体"}[ACS]{lang="EN-US"}[请求连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[时用来认证的密码，区分大小写。当以明文方式配置时，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串；以密文方式配置时，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1705602958}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_13006_x2365_1722232418}[ACS]{lang="EN-US"}[与]{style="font-family:宋体"}[CPE]{lang="EN-US"}[建立]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[连接且通过用户名和密码进行认证时，]{style="font-family:宋体"}[ACS]{lang="EN-US"}[会将用户名和密码发送给]{style="font-family:宋体"}[CPE]{lang="EN-US"}[，以便设备对]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的身份进行认证。设备根据本地配置的用户名和该密码验证]{style="font-family:宋体"}[ACS]{lang="EN-US"}[是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多次使用该命令配置不同的密码时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_x810017448}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该配置为可选配置，可以只用用户名验证，但]{style="font-family:宋体"}]{#struct_0_13006_x2365_x1069922736}[ACS]{lang="EN-US"}[和]{style="font-family:宋体"}[CPE]{lang="EN-US"}[上的配置必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1916476002}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_654210181}[配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[密码为]{style="font-family:宋体"}[newpsw]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_x141190517}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe password simple newpsw]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_632426700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp cpe username]{lang="EN-US"}**]{#struct_0_13006_x2365_922526078}
:::

::: {#922140576 .myid}
[]{#_Toc404797086}[]{#struct_0_13006_x2365_x850046542}

**CWMP \-- CWMP配置命令 \-- cwmp cpe provision-code**

------------------------------------------------------------------------

[**[cwmp cpe provision-code]{lang="EN-US"}**]{#struct_0_13006_x2365_x1231800833}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的业务代码。]{style="font-family:宋体"}

[**[undo cwmp cpe provision-code]{lang="EN-US"}**]{#struct_0_13006_x2365_x372617491}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x184792625}

[**[cwmp cpe provision-code ]{lang="EN-US"}***[provision-code]{lang="EN-US"}*]{#struct_0_13006_x2365_1530616793}

[**[undo cwmp cpe provision-code]{lang="EN-US"}**]{#struct_0_13006_x2365_3484587}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1143260489}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_491799568}[向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[发送的]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文中携带的业务代码为"]{style="font-family:宋体"}[PROVISIONCODE]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1099517090}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x364917586}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x485469714}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x66513748}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_654406789}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_946134864}

[*[provision-code]{lang="EN-US"}*]{#struct_0_13006_x2365_x1626944229}[：设备向]{style="font-family:宋体"}[ACS]{lang="EN-US"}[发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文中携带的设备代码。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，必须为大写字母、数字或者"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1157312146}

[[当]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x2036891888}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间建立连接时，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[需要在]{style="font-family:宋体"}[Inform]{lang="EN-US"}[报文中携带]{style="font-family:宋体"}[provision-code]{lang="EN-US"}[信息，]{style="font-family:宋体"}[ACS]{lang="EN-US"}[根据此信息可以识别设备定制的业务以及相应的参数，以便更好地管理]{style="font-family:宋体"}[CPE]{lang="EN-US"}[设备。]{style="font-family:宋体"}

[[多次使用该命令配置设备代码时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_1375561880}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_919650257}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_1548717303}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的业务代码为]{style="font-family:宋体"}[H3C20130525]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_13006_x2365_986578029}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe provision-code H3C20130525]{lang="EN-US"}
:::

::: {#-639205884 .myid}
[]{#_Toc257625612}[]{#_Toc404797087}[]{#struct_0_13006_x2365_825389436}

**CWMP \-- CWMP配置命令 \-- cwmp cpe stun enable**

------------------------------------------------------------------------

[**[cwmp cpe stun enable]{lang="EN-US"}**]{#struct_0_13006_x2365_333016376}[命令用来使能]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[穿越功能。]{style="font-family:宋体"}

[**[undo cwmp]{lang="EN-US"}[ cpe stun enable]{lang="EN-US"}**]{#struct_0_13006_x2365_x249593573}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x624059241}

[**[cwmp cpe stun enable]{lang="EN-US"}**]{#struct_0_13006_x2365_1989024226}

[**[undo ]{lang="EN-US"}[cwmp cpe stun enable]{lang="EN-US"}**]{#struct_0_13006_x2365_x1397929504}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_654341253}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_999308339}[的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[穿越功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1942022037}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_679583907}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_899556029}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1004171752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1129879659}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x454538162}

[[无论]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1162635452}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间是否存在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的主动连接请求都能到达]{style="font-family:宋体"}[ACS]{lang="EN-US"}[。而当]{style="font-family:宋体"}[CPE]{lang="EN-US"}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间存在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关时，]{style="font-family:宋体"}[ACS]{lang="EN-US"}[主动发起的连接请求不能到达]{style="font-family:宋体"}[CPE]{lang="EN-US"}[。此时，可以在设备上开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[穿越功能，使得]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的请求能够穿越网关。本特性的实现遵循]{style="font-family:宋体"}[RFC 3489]{lang="EN-US"}[定义的]{style="font-family:宋体"}[STUN]{lang="EN-US"}[（]{style="font-family:宋体"}[Simple Traversal of User Datagram Protocol (UDP) Through Network Address Translators (NATs)]{lang="EN-US"}[，]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[简单穿越）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1657859288}[在主动给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[发连接请求的过程中，如果发现与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[之间存在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关，则会将获取到的经]{style="font-family:宋体"}[NAT]{lang="EN-US"}[绑定的公网的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号发送给]{style="font-family:宋体"}[ACS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了保证]{style="font-family:宋体"}]{#struct_0_13006_x2365_x1267818604}[ACS]{lang="EN-US"}[任意时刻主动发起的连接请求能够穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关到达]{style="font-family:宋体"}[CPE]{lang="EN-US"}[，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[必须维持]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关上的地址映射关系。]{style="font-family:宋体"}

[[有关]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_13006_x2365_x140303572}[的详细描述，请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务配置指导"中的"]{style="font-family:宋体"}[NAT]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1820040281}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x721275944}[使能]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的]{style="font-family:宋体"}[NAT]{lang="EN-US"}[穿越功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_130982624}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe stun enable]{lang="EN-US"}
:::

::: {#1960316791 .myid}
[]{#_Toc404797088}[]{#struct_0_13006_x2365_654537861}

**CWMP \-- CWMP配置命令 \-- cwmp cpe username**

------------------------------------------------------------------------

[**[cwmp cpe username]{lang="EN-US"}**]{#struct_0_13006_x2365_1225116294}[命令用来配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[时的认证用户名。]{style="font-family:宋体"}

[**[undo cwmp cpe username]{lang="EN-US"}**]{#struct_0_13006_x2365_x433173884}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1850386781}

[**[cwmp cpe username ]{lang="EN-US"}***[username]{lang="EN-US"}*]{#struct_0_13006_x2365_71026098}

[**[undo cwmp cpe username]{lang="EN-US"}**]{#struct_0_13006_x2365_654472325}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_115126443}

[[未配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_1965314788}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的用户名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1349330515}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1903444986}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x757336614}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_792344228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1284637348}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x338569987}

[*[username]{lang="EN-US"}*]{#struct_0_13006_x2365_x1270017351}[：]{style="font-family:宋体"}[ACS]{lang="EN-US"}[请求连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[时的认证用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x913646815}

[[当]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_1722661908}[向]{style="font-family:宋体"}[CPE]{lang="EN-US"}[发送连接请求且通过用户名和密码认证时，]{style="font-family:宋体"}[ACS]{lang="EN-US"}[会将用户名和密码发送给设备，以便设备对]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的身份进行认证。设备根据本地配置的用户名和该密码验证]{style="font-family:宋体"}[ACS]{lang="EN-US"}[是否合法，如果验证成功，则建立连接，否则，不能建立连接。]{style="font-family:宋体"}

[[多次使用该命令配置用户名时，以最新的配置为准。]{style="font-family:宋体"}]{#struct_0_13006_x2365_x1974556616}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1105600130}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x304044272}[配置]{style="font-family:宋体"}[ACS]{lang="EN-US"}[连接到]{style="font-family:宋体"}[CPE]{lang="EN-US"}[的用户名为]{style="font-family:宋体"}[newname]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_654668933}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe username newname]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_688668318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp cpe password]{lang="EN-US"}**]{#struct_0_13006_x2365_x1357192156}
:::

::: {#-55203359 .myid}
[]{#_Toc404797089}[]{#struct_0_13006_x2365_1654501762}[]{#_Toc257625613}

**CWMP \-- CWMP配置命令 \-- cwmp cpe wait timeout**

------------------------------------------------------------------------

[**[cwmp cpe wait timeout]{lang="EN-US"}**]{#struct_0_13006_x2365_293449680}[命令用来配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[无数据传输超时时间。]{style="font-family:宋体"}

[**[undo cwmp cpe wait timeout]{lang="EN-US"}**]{#struct_0_13006_x2365_x1376444440}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x658634023}

[**[cwmp cpe wait timeout ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_13006_x2365_x1156046756}

[**[undo cwmp cpe wait timeout]{lang="EN-US"}**]{#struct_0_13006_x2365_x1474812626}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1564035217}

[[无数据传输超时时间为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_13006_x2365_x977429805}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_232909068}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_600188759}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1006462263}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x535479762}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_654603397}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1572385206}

[*[seconds]{lang="EN-US"}*]{#struct_0_13006_x2365_x360869126}[：无数据传输超时时间，取值范围为]{style="font-family:宋体"}[30]{lang="EN-US"}[～]{style="font-family:宋体"}[1800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1324158579}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1468196093}[连接建立后，如果]{style="font-family:宋体"}[CPE]{lang="EN-US"}[与]{style="font-family:宋体"}[ACS]{lang="EN-US"}[在无数据传输超时时间内一直没有报文的交互，]{style="font-family:宋体"}[CPE]{lang="EN-US"}[将认为连接失效，并断开连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1102180536}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x628938051}[配置]{style="font-family:宋体"}[CPE]{lang="EN-US"}[无数据传输超时时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_504014479}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp cpe wait timeout 60]{lang="EN-US"}
:::

::: {#1494833186 .myid}
[]{#_Toc404797090}[]{#struct_0_13006_x2365_2039111760}[]{#_Toc257625614}

**CWMP \-- CWMP配置命令 \-- cwmp enable**

------------------------------------------------------------------------

[**[cwmp enable]{lang="EN-US"}**]{#struct_0_13006_x2365_1504678808}[命令用来使能]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo cwmp enable]{lang="EN-US"}**]{#struct_0_13006_x2365_x1672165249}[命令用来关闭]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x403291615}

[**[cwmp enable]{lang="EN-US"}**]{#struct_0_13006_x2365_x981899942}

[**[undo cwmp enable]{lang="EN-US"}**]{#struct_0_13006_x2365_1602557229}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x720666343}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_654800005}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x207083949}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1639087071}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1681934512}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x1783685206}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1180805603}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1411431793}

[[使能]{style="font-family:宋体"}[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_95719437}[后，]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[的其它配置才能生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_286235350}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_538158201}[使能]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_13006_x2365_1257012638}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] cwmp enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x673891364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cwmp]{lang="EN-US"}**]{#struct_0_13006_x2365_x637301147}
:::

::: {#-1485744438 .myid}
[]{#_Toc404797091}[]{#struct_0_13006_x2365_862547378}[]{#_Toc257625615}

**CWMP \-- CWMP配置命令 \-- display cwmp configuration**

------------------------------------------------------------------------

[**[display cwmp configuration]{lang="EN-US"}**]{#struct_0_13006_x2365_x1519342899}[命令用来显示]{style="font-family:
宋体"}[CWMP]{lang="EN-US"}[的当前配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_654734469}

[**[display cwmp configuration]{lang="EN-US"}**]{#struct_0_13006_x2365_809849674}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1539613948}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13006_x2365_1628126965}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1440331120}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1514002911}

[[network-operator]{lang="EN-US"}]{#struct_0_13006_x2365_445389807}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_1298117497}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13006_x2365_x2056139486}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1746684163}

[[\# CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x914198239}[使能，显示]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<sysname\> display cwmp configuration]{lang="EN-US"}]{#struct_0_13006_x2365_654275718}

[CWMP state                          : Enabled]{lang="EN-US"}

[ACS URL                             : http://www.acs.com:80/acs]{lang="EN-US"}

[ACS username                        : newname]{lang="EN-US"}

[ACS default URL                     : Null]{lang="EN-US"}

[ACS default username                : defname]{lang="EN-US"}

[Periodic inform                     : Disabled]{lang="EN-US"}

[Inform interval                     : 600s]{lang="EN-US"}

[Inform time                         : None]{lang="EN-US"}

[Wait timeout                        : 30s]{lang="EN-US"}

[Connection retries                  : Unlimited]{lang="EN-US"}

[Source IP interface                 : None]{lang="EN-US"}

[STUN state                          : Disabled]{lang="EN-US"}

[SSL policy name                     : Null]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display cwmp configuration]{lang="EN-US"}]{#struct_0_13006_x2365_244899386}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x240435632}[[字段]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1211973269}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13006_x2365_618652924}

[[CWMP state]{lang="EN-US"}]{#struct_0_13006_x2365_1063528679}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x319443380}[的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nabled]{lang="EN-US"}]{#struct_0_13006_x2365_1047033044}[：]{style="font-family:
  宋体"}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isabled]{lang="EN-US"}]{#struct_0_13006_x2365_2037239615}[：]{style="font-family:
  宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[ACS default URL]{lang="EN-US"}]{#struct_0_13006_x2365_x1462159210}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1543913157}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省]{style="font-family:宋体"}[URL]{lang="EN-US"}[，没有配置时显示为]{style="font-family:宋体"}[Null]{lang="EN-US"}

[[ACS default username]{lang="EN-US"}]{#struct_0_13006_x2365_x1332687338}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1608756209}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的缺省用户名，没有配置时显示为空]{style="font-family:宋体"}

[[ACS URL]{lang="EN-US"}]{#struct_0_13006_x2365_654210182}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x141190520}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，没有配置时显示为]{style="font-family:宋体"}[Null]{lang="EN-US"}

[[ACS username]{lang="EN-US"}]{#struct_0_13006_x2365_632099017}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1135744771}[连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的用户名，没有配置时显示为空]{style="font-family:宋体"}

[[Periodic inform]{lang="EN-US"}]{#struct_0_13006_x2365_x1939848619}

[[周期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}]{#struct_0_13006_x2365_568511540}[报文的使能情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nabled]{lang="EN-US"}]{#struct_0_13006_x2365_128363861}[：]{style="font-family:
  宋体"}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isabled]{lang="EN-US"}]{#struct_0_13006_x2365_x1347693993}[：]{style="font-family:
  宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[Inform interval]{lang="EN-US"}]{#struct_0_13006_x2365_1861007068}

[[发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}]{#struct_0_13006_x2365_1809875983}[报文的周期，没有配置时显示为]{style="font-family:宋体"}[None]{lang="EN-US"}

[[Inform time]{lang="EN-US"}]{#struct_0_13006_x2365_654406790}

[[定期发送]{style="font-family:宋体"}[Inform]{lang="EN-US"}]{#struct_0_13006_x2365_x1010180279}[报文的日期和时间，没有配置时显示为]{style="font-family:宋体"}[None]{lang="EN-US"}

[[Wait timeout]{lang="EN-US"}]{#struct_0_13006_x2365_x204028906}

[[无数据传输超时的时间]{style="font-family:宋体"}]{#struct_0_13006_x2365_1017353558}

[[Connection retries]{lang="EN-US"}]{#struct_0_13006_x2365_x365385868}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1211996176}[连接失败后自动重新连接的次数，没有配置时显示为]{style="font-family:宋体"}[Unlimited]{lang="EN-US"}

[[Source IP interface]{lang="EN-US"}]{#struct_0_13006_x2365_x1413004388}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1553328439}[上用于连接]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的接口]{style="font-family:宋体"}

[[STUN state]{lang="EN-US"}]{#struct_0_13006_x2365_x162459793}

[[NAT]{lang="EN-US"}]{#struct_0_13006_x2365_654341254}[穿越功能的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[E]{lang="EN-US"}[nabled]{lang="EN-US"}]{#struct_0_13006_x2365_999308338}[：]{style="font-family:
  宋体"}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isabled]{lang="EN-US"}]{#struct_0_13006_x2365_x1942022036}[：]{style="font-family:
  宋体"}[表示未使能]{lang="EN-US" style="font-family:宋体"}

[[SSL policy name]{lang="EN-US"}]{#struct_0_13006_x2365_x2049299448}

[[连接]{style="font-family:宋体"}[ACS]{lang="EN-US"}]{#struct_0_13006_x2365_x1950324561}[采用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[策略名，没有配置时显示为]{style="font-family:宋体"}[Null]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1589242633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cwmp status]{lang="EN-US"}**]{#struct_0_13006_x2365_x348180366}

::: {#1259234664 .myid}
[]{#_Toc404797092}[]{#struct_0_13006_x2365_1878200517}[]{#_Toc257625616}

**CWMP \-- CWMP配置命令 \-- display cwmp status**

------------------------------------------------------------------------

[**[display cwmp status]{lang="EN-US"}**]{#struct_0_13006_x2365_x912509624}[命令用来显示]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[的当前状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1442774343}

[**[display cwmp status]{lang="EN-US"}**]{#struct_0_13006_x2365_654537862}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1225116295}

[[任意视图]{style="font-family:宋体"}]{#struct_0_13006_x2365_x433108348}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1121745180}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x226244968}

[[network-operator]{lang="EN-US"}]{#struct_0_13006_x2365_x1691603388}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_343352665}

[[mdc-operator]{lang="EN-US"}]{#struct_0_13006_x2365_454566853}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1493707667}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x1579744597}[显示]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[的当前状态信息。]{style="font-family:宋体"}

[[\<sysname\> display cwmp status]{lang="EN-US"}]{#struct_0_13006_x2365_985917806}

[CWMP state                                    : Enabled]{lang="EN-US"}

[ACS URL of most recent connection             : http://www.acs.com:80/acs]{lang="EN-US"}

[ACS information source                        : User]{lang="EN-US"}

[ACS username of most recent connection        : newname]{lang="EN-US"}

[Connection status                             : Disconnected]{lang="EN-US"}

[Data transfer status                          : None]{lang="EN-US"}

[Most recent successful connection attempt     : None]{lang="EN-US"}

[Length of time before next connection attempt : 1096832s]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display cwmp status]{lang="EN-US"}]{#struct_0_13006_x2365_x1071650860}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x244762466}[[字段]{style="font-family:黑体"}]{#struct_0_13006_x2365_1035886922}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_13006_x2365_654472326}

[[CWMP state]{lang="EN-US"}]{#struct_0_13006_x2365_115126444}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1965314795}[的使能状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_13006_x2365_1349002836}[：表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_13006_x2365_1089755809}[：表示未使能]{lang="EN-US" style="font-family:宋体"}

[[ACS URL of most recent connection]{lang="EN-US"}]{#struct_0_13006_x2365_x2118009320}

[[最近一次]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1074702259}[使用的连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，没有配置时显示为]{style="font-family:宋体"}[Null]{lang="EN-US"}

[[ACS information source]{lang="EN-US"}]{#struct_0_13006_x2365_1226972641}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_2136349683}[获得]{style="font-family:宋体"}[ACS URL]{lang="EN-US"}[的方式，没有配置]{style="font-family:宋体"}[ACS URL]{lang="EN-US"}[时显示为]{style="font-family:宋体"}[None]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[User]{lang="EN-US"}]{#struct_0_13006_x2365_x164612036}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[ACS URL]{lang="EN-US"}[为命令行配置]{lang="EN-US" style="font-family:宋体"}[或者]{style="font-family:宋体"}[ACS]{lang="EN-US"}[配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DHCP]{lang="EN-US"}]{#struct_0_13006_x2365_90180281}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[ACS URL]{lang="EN-US"}[为]{lang="EN-US" style="font-family:宋体"}[DHCP]{lang="EN-US"}[下发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default]{lang="EN-US"}]{#struct_0_13006_x2365_654668934}[：表示]{style="font-family:宋体"}[ACS URL]{lang="EN-US"}[为缺省配置]{style="font-family:宋体"}

[[ACS username of most recent connection]{lang="EN-US"}]{#struct_0_13006_x2365_688668313}

[[最近一次]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x1357192149}[使用的连接到]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的用户名，没有配置时显示为空]{style="font-family:宋体"}

[[Connection status]{lang="EN-US"}]{#struct_0_13006_x2365_1251282771}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_1228946462}[的连接状态，包含：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[C]{lang="EN-US"}[onnected]{lang="EN-US"}]{#struct_0_13006_x2365_x1505080955}[：]{style="font-family:宋体"}[表示连接已建立]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[isconnected]{lang="EN-US"}]{#struct_0_13006_x2365_x2143156861}[：]{style="font-family:宋体"}[表示没有建立连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[W]{lang="EN-US"}[aiting response]{lang="EN-US"}]{#struct_0_13006_x2365_x311463701}[：]{style="font-family:宋体"}[表示正在等待响应报文]{lang="EN-US" style="font-family:宋体"}

[[Data transfer status]{lang="EN-US"}]{#struct_0_13006_x2365_x1123322676}

[[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_654603398}[的数据传输的状态，包含：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}[ploading]{lang="EN-US"}]{#struct_0_13006_x2365_1572385213}[：]{style="font-family:宋体"}[表示正在上传数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[ownloading]{lang="EN-US"}]{#struct_0_13006_x2365_x360541447}[：]{style="font-family:宋体"}[表示正在下载数据]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[None]{lang="EN-US"}]{#struct_0_13006_x2365_227841476}[：表示没有数据在传输]{style="font-family:宋体"}

[[Most recent successful connection attempt]{lang="EN-US"}]{#struct_0_13006_x2365_391510900}

[[最近一次]{style="font-family:宋体"}[CPE]{lang="EN-US"}]{#struct_0_13006_x2365_x5755711}[和]{style="font-family:宋体"}[ACS]{lang="EN-US"}[成功连接的时间，最近没有成功连接时显示为]{style="font-family:宋体"}[None]{lang="EN-US"}

[[Length of time before next connection attempt]{lang="EN-US"}]{#struct_0_13006_x2365_41398056}

[[距离下一次发起连接的时间，单位为秒。如果目前没有发起会话需求则显示为]{style="font-family:宋体"}[None]{lang="EN-US"}]{#struct_0_13006_x2365_1110949292}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_2079929412}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display cwmp configuration]{lang="EN-US"}**]{#struct_0_13006_x2365_x1757016631}

::: {#1659289076 .myid}
[]{#_Toc404797093}[]{#struct_0_13006_x2365_654800006}[]{#_Toc124237095}

**CWMP \-- CWMP配置命令 \-- ssl client-policy**

------------------------------------------------------------------------

[**[ssl client-policy]{lang="EN-US"}**]{#struct_0_13006_x2365_x207083950}[命令用来配置]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ssl client-policy]{lang="EN-US"}**]{#struct_0_13006_x2365_1638628318}[命令用来删除对该]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略的引用。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x528172623}

[**[ssl client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_13006_x2365_100592140}

[**[undo ssl client-policy]{lang="EN-US"}**]{#struct_0_13006_x2365_x34760866}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x669206934}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1251353534}[没有引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x1266197055}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_1169316650}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_13006_x2365_x612036722}

[[network-admin]{lang="EN-US"}]{#struct_0_13006_x2365_x575358224}

[[mdc-admin]{lang="EN-US"}]{#struct_0_13006_x2365_764501347}

[[【参数】]{style="font-family:黑体"}]{#struct_0_13006_x2365_2111026615}

[*[policy-name]{lang="EN-US"}*]{#struct_0_13006_x2365_2117329371}[：]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_13006_x2365_654734470}

[[CWMP]{lang="EN-US"}]{#struct_0_13006_x2365_x1528802495}[是基于]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[协议的，]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[报文作为]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[报文的数据部分封装在]{style="font-family:宋体"}[HTTP/HTTPS]{lang="EN-US"}[报文中。如果]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[以]{style="font-family:宋体"}[http://]{lang="EN-US"}[开头，则使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[协议，如果]{style="font-family:宋体"}[ACS]{lang="EN-US"}[的]{style="font-family:宋体"}[URL]{lang="EN-US"}[以]{style="font-family:宋体"}[https://]{lang="EN-US"}[开头，则使用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[使用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}]{#struct_0_13006_x2365_x1031664607}[协议时，为了对]{style="font-family:宋体"}[ACS]{lang="EN-US"}[身份进行认证，需要配置]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略。关于]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略的详细介绍和配置请参见"安全配置指导"中的"]{style="font-family:宋体"}[SSL]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_13006_x2365_1518697923}

[[\# ]{lang="EN-US"}]{#struct_0_13006_x2365_x349865605}[设置]{style="font-family:宋体"}[CWMP]{lang="EN-US"}[引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system]{lang="EN-US"}]{#struct_0_13006_x2365_748401665}

[\[Sysname\] cwmp]{lang="EN-US"}

[\[Sysname-cwmp\] ssl client-policy test]{lang="EN-US"}
:::
