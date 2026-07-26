::: {#-867717149 .myid}
[]{#_Toc404795036}[]{#struct_0_x2098_10749_1152023010}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security accounting-start-fail offline**

------------------------------------------------------------------------

[**[client-security accounting-start-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_659474239}[命令用来开启计费请求失败用户下线功能，即计费开始请求发送失败后，强制用户下线。]{style="font-family:宋体"}

[**[undo client-security accounting-start-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_x142913309}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1066951400}

[**[client-security accounting-start-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_779837979}

[**[undo client-security accounting-start-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_x2130565799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1794934272}

[[计费开始请求发送失败后，用户保持在线。]{style="font-family:宋体"}]{#struct_0_x2098_10749_848046582}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_954652572}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1206844533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1855013497}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1111832777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1224878608}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_296736688}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_1202192978}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1488595565}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x1531781448}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下开启计费请求失败用户下线功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x2074582301}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security accounting-start-fail offline]{lang="EN-US"}
:::

::: {#-1817813899 .myid}
[]{#_Toc404795037}[]{#struct_0_x2098_10749_x1771666350}[]{#_Toc376188458}[]{#_Toc370976429}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authentication fail-vlan**

------------------------------------------------------------------------

[**[client-security authentication fail-vlan]{lang="EN-US"}**]{#struct_0_x2098_10749_x1368381823}[命令用来配置指定服务模板下的认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo client-security authentication fail-vlan]{lang="EN-US"}**]{#struct_0_x2098_10749_x409036386}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_554228140}

[**[client-security authentication fail-vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_x2098_10749_606185390}

[**[undo client-security authentication fail-vlan]{lang="EN-US"}**]{#struct_0_x2098_10749_x594373344}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1424541710}

[[没有配置认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2098_10749_585869273}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_2142186394}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1836549287}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1701514994}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x937638921}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1360501532}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1736915005}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_x2098_10749_31346728}[：认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_236187220}

[[该配置为服务模板下的配置，只能在服务模板去使能的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_583217017}

[[这里的认证失败是认证服务器因某种原因明确拒绝用户认证通过，比如用户密码错误，而不是认证超时或网络连接等原因造成的认证失败。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x724565005}

[[如果配置了认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2098_10749_x546397337}[，则认证失败的用户将被加入该]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，同时设备会启动一个]{style="font-family:宋体"}[30]{lang="EN-US"}[秒的定时器，定期对用户进行重新认证：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果是]{style="font-family:宋体"}]{#struct_0_x2098_10749_1137691138}[802.1X]{lang="EN-US"}[认证用户，设备将向用户发送单播]{style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}[报文进行重新认证。另外，]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户也可以主动再次发起认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果是]{style="font-family:宋体"}]{#struct_0_x2098_10749_1058054203}[MAC]{lang="EN-US"}[地址认证用户，设备将直接向认证服务器发起重新认证。]{style="font-family:宋体"}

[[如果用户重认证通过，则设备将根据认证服务器或设备是否给用户下发]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x2098_10749_x1123134811}[来重新指定该用户所在]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[：如果认证服务器或设备给用户下发了]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，则用户将被加入该下发的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，否则用户将被加入初始]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[；如果用户重认证仍然失败，则用户仍然留在认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1020477705}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_1914748609}[在无线服务模板]{style="font-family:宋体"}[1]{lang="EN-US"}[下配置认证失败]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_x2098_10749_1407555699}

[\[Sysname\] wlan service-template 1]{lang="EN-US"}

[\[Sysname-wlan-st-1\] client-security authentication fail-vlan 10]{lang="EN-US"}
:::

::: {#-1251624133 .myid}
[]{#_Toc404795038}[]{#struct_0_x2098_10749_206980814}[]{#_Toc370976409}[]{#_Toc185927308}[]{#_Toc123026768}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authentication-mode**

------------------------------------------------------------------------

[**[client-security authentication-mode]{lang="EN-US"}**]{#struct_0_x2098_10749_x1905024657}[命令用来配置无线用户接入认证模式。]{style="font-family:宋体"}

[**[undo client-security authentication-mode]{lang="EN-US"}**]{#struct_0_x2098_10749_454140200}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1855013498}

[**[client-security authentication-mode]{lang="EN-US"}**[ { **dot1x** \| **dot1x-then-mac** \| **mac** \| **mac-then-dot1x** \| **oui-then-dot1x** }]{lang="EN-US"}]{#struct_0_x2098_10749_x1111242953}

[**[undo client-security authentication-mode]{lang="EN-US"}**]{#struct_0_x2098_10749_540299765}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1367052371}

[[不对用户进行认证即]{style="font-family:宋体"}[Bypass]{lang="EN-US"}]{#struct_0_x2098_10749_x130376167}[认证，直接接入。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1431107842}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x151472337}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1932790100}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x907340614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_173732098}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_608769333}

[**[dot1x]{lang="EN-US"}**]{#struct_0_x2098_10749_x1872042965}[：表示只进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[dot1x-then-mac]{lang="EN-US"}**]{#struct_0_x2098_10749_598369470}[：表示先进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证，如果失败，再进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。如果认证成功，则不进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[**[mac]{lang="EN-US"}**]{#struct_0_x2098_10749_x561170016}[：表示只进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[**[mac-then-dot1x]{lang="EN-US"}**]{#struct_0_x2098_10749_x1096933185}[：表示先进行]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证，如果失败，再进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。如果认证成功，则不进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[oui-then-dot1x]{lang="EN-US"}**]{#struct_0_x2098_10749_1855013499}[：表示先进行]{style="font-family:宋体"}[OUI]{lang="EN-US"}[认证，如果失败，再进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。如果认证成功，则不进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1111177417}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_984130853}

[[以上各模式下，每个无线服务模板上均允许接入多个认证通过的用户。]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x496723168}[用户的数目由]{style="font-family:宋体"}**[dot1x max-user]{lang="EN-US"}**[命令配置，]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户的数目由]{style="font-family:宋体"}**[mac-authentication max-user]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x2021209995}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_114317058}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下配置无线用户接入认证模式为]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证模式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x1851702353}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security authentication-mode mac]{lang="EN-US"}
:::

::: {#776367387 .myid}
[]{#_Toc404795039}[]{#struct_0_x2098_10749_x1282509206}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security authorization-fail offline**

------------------------------------------------------------------------

[**[client-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_1776021763}[命令用来开启授权失败后的用户下线功能，即授权信息下发失败后，强制用户下线。]{style="font-family:宋体"}

[**[undo client-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_829276273}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x71137030}

[**[client-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_x1070083493}

[**[undo client-security authorization-fail offline]{lang="EN-US"}**]{#struct_0_x2098_10749_x266216061}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1540367298}

[[设置授权信息下发失败后，用户保持在线。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x460965714}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_277833905}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_1875185260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1722913467}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1922732175}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1061282628}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1855013501}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_844613440}

[[如果开启了授权失败后的用户下线功能，当下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x2098_10749_2136509202}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[不存在、已授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[被删除，或者]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发失败时，将强制用户下线；]{style="font-family:宋体"}

[[如果没有开启授权失败后的用户下线功能，当下发的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x2098_10749_x920700678}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[不存在、已授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[被删除，或者]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[下发失败时，用户保持在线，授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[、]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[不生效，设备打印]{style="font-family:宋体"}[Log]{lang="EN-US"}[信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1688600198}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_374875744}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下开启授权失败用户下线功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x1884818317}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security authorization-fail offline]{lang="EN-US"}
:::

::: {#670070371 .myid}
[]{#_Toc404795040}[]{#struct_0_x2098_10749_985282321}[]{#_Toc370976410}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security ignore-authorization**

------------------------------------------------------------------------

[**[client-security ignore-authorization]{lang="EN-US"}**]{#struct_0_x2098_10749_1741546959}[命令用来配置忽略]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[**[undo client-security]{lang="EN-US"}**[ **ignore-authorization**]{lang="EN-US"}]{#struct_0_x2098_10749_261392267}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_602803743}

[**[client-security ignore-authorization]{lang="EN-US"}**]{#struct_0_x2098_10749_1369743811}

[**[undo client-security ignore-authorization]{lang="EN-US"}**]{#struct_0_x2098_10749_1575268669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1855013502}

[[应用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x2098_10749_844678976}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1663137481}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_1920500705}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_649868093}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x313705983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1481650329}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_557152046}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x563207059}

[[当用户通过]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_x2098_10749_1087000795}[认证或本地认证后，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备会根据用户帐号配置的相关属性进行授权，比如动态下发]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[等。若不希望接受这类动态下发的授权属性，则可通过配置本命令来忽略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_110655337}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_26259111}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下配置忽略]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器或设备本地下发的授权信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_466655316}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security ignore-authorization]{lang="EN-US"}
:::

::: {#-195028892 .myid}
[]{#_Toc404795041}[]{#struct_0_x2098_10749_844744512}[]{#_Toc370976412}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection action**

------------------------------------------------------------------------

[**[client-security]{lang="EN-US"}**[ **intrusion-protection action**]{lang="EN-US"}]{#struct_0_x2098_10749_x1738080472}[命令用来配置当接收到非法报文时采取的入侵保护措施。]{style="font-family:宋体"}

[**[undo client-security]{lang="EN-US"}**[ **intrusion-protection action**]{lang="EN-US"}]{#struct_0_x2098_10749_161250606}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1757736373}

[**[client-security intrusion-protection action]{lang="EN-US"}**[ { **service-stop** \| **temporary-block** \| **temporary-service-stop** }]{lang="EN-US"}]{#struct_0_x2098_10749_x781817594}

[**[undo client-security intrusion-protection action]{lang="EN-US"}**]{#struct_0_x2098_10749_x1357929657}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1631366961}

[[默认入侵检测模式为临时将用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_109063177}[加入阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[列表中，即源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为此非法]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的用户将不能和]{style="font-family:宋体"}[AP]{lang="EN-US"}[建立连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1770185673}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_2035716797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x560783556}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x740982982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x2084165500}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1194348916}

[**[service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_x1670270889}[：直接关闭收到非法报文的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[提供的所有服务。]{style="font-family:宋体"}

[**[temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_1433451337}[：临时将用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}[加入阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[列表中。]{style="font-family:宋体"}

[**[temporary-service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_1855013504}[：临时将收到非法报文的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[所提供的所有服务关闭。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_844285760}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_2032998240}

[[只有开启入侵保护功能后，入侵保护措施才生效。开启入侵保护功能由]{style="font-family:宋体"}**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_1463200805}[命令配置。]{style="font-family:宋体"}

[[临时阻止非法用户上线的时间由]{style="font-family:宋体"}**[client-security intrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_2139182094}[命令配置。]{style="font-family:宋体"}

[[临时关闭收到非法报文的]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x2098_10749_x697372298}[所提供服务的时间由]{style="font-family:宋体"}**[client-security intrusion-protection timer temporary-service-stop]{lang="EN-US"}**[命令配置。]{style="font-family:宋体"}

[[用户所属]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x2098_10749_x1357824860}[提供的服务已关闭的情况下，用户可以手工在]{style="font-family:宋体"}[Radio]{lang="EN-US"}[口上重新生成该]{style="font-family:宋体"}[BSS]{lang="EN-US"}[使得用户正常接入。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1463171744}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_149014604}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下配置入侵保护措施为]{style="font-family:宋体"}**[service-stop]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x99401272}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection enable]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection action service-stop]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1398160397}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_1079263468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection temporary-block timer]{lang="EN-US"}**]{#struct_0_x2098_10749_x246240794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection temporary-service-stop timer]{lang="EN-US"}**]{#struct_0_x2098_10749_x1267724125}
:::

::: {#-77309109 .myid}
[]{#_Toc404795042}[]{#struct_0_x2098_10749_1855013505}[]{#_Toc370976411}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection enable**

------------------------------------------------------------------------

[**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_844351296}[命令用来开启入侵保护功能。]{style="font-family:宋体"}

[**[undo client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1080593438}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x36608154}

[**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_575182071}

[**[undo client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_1906381477}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x240346969}

[[入侵保护功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x2098_10749_354833745}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1729104922}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x541344524}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1946403170}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1311627753}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_757158071}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1753815804}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1687298815}

[[当设备检测到一个认证失败的用户试图通过该无线服务模板绑定的]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x2098_10749_x101301640}[（基本服务集）接入时，如果入侵保护功能处于开启状态，则设备将对其所在的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[采取相应的安全措施。具体的安全措施由]{style="font-family:宋体"}**[client-security]{lang="EN-US"}**[ **intrusion-protection action**]{lang="EN-US"}[命令指定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1919654496}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_1788166058}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下开启入侵保护功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x379756405}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_175685188}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security]{lang="EN-US"}**[ **intrusion-protection action**]{lang="EN-US"}]{#struct_0_x2098_10749_x2018873391}
:::

::: {#1407566861 .myid}
[]{#_Toc404795043}[]{#struct_0_x2098_10749_498029156}[]{#_Toc370976413}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection timer temporary-block**

------------------------------------------------------------------------

[**[client-security intrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_x1974347950}[命令用来配置临时阻塞非法入侵用户的时长。]{style="font-family:宋体"}

[**[undo client-security intrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_587409156}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1339600742}

[**[client-security intrusion-protection timer temporary-block]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x2098_10749_x411757355}

[**[undo client-security intrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_2036025176}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1440235110}

[[临时阻塞非法入侵用户时间为]{style="font-family:宋体"}[180]{lang="EN-US"}]{#struct_0_x2098_10749_984996319}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x101301639}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1920113249}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_705027270}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_208740883}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_471123616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x280962669}

[*[value]{lang="EN-US"}*]{#struct_0_x2098_10749_x447652845}[：阻塞非法入侵用户时长，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_564734046}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x710135058}

[[当入侵检测功能处于使能状态且入侵保护措施为临时阻塞非法用户（]{style="font-family:宋体"}**[temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_x292933659}[）时，如果用户认证失败，则在该配置所指定的时间范围内，源]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为此非法]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址的用户将无法认证成功，在这段时间之后恢复正常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x834418506}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_678004587}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下配置临时阻塞非法入侵用户时长为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_589144308}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection enable]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection action temporary-block]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection temporary-block timer 120]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_695003732}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1920178785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection action]{lang="EN-US"}**]{#struct_0_x2098_10749_x74662109}
:::

::: {#1024625273 .myid}
[]{#struct_0_x2098_10749_1776649779}[]{#_Toc370976428}[]{#_Toc404795044}[]{#_Toc397088577}[]{#_Toc397088578}[]{#_Toc397088579}[]{#_Toc397088580}[]{#_Toc397088581}[]{#_Toc397088582}[]{#_Toc397088583}[]{#_Toc397088584}[]{#_Toc397088585}[]{#_Toc397088586}[]{#_Toc397088587}[]{#_Toc397088588}[]{#_Toc397088589}[]{#_Toc397088590}[]{#_Toc397088591}[]{#_Toc397088592}[]{#_Toc397088593}[]{#_Toc397088594}[]{#_Toc397088595}[]{#_Toc397088596}[]{#_Toc397088597}[]{#_Toc397088598}[]{#_Toc397088599}[]{#_Toc397088600}[]{#_Toc397088601}[]{#_Toc397088602}[]{#_Toc397088603}[]{#_Toc397088604}[]{#_Toc397088605}[]{#_Toc397088606}[]{#_Toc397088607}[]{#_Toc397088608}[]{#_Toc397088609}[]{#_Toc397088610}[]{#_Toc397088611}[]{#_Toc397088612}[]{#_Toc397088613}[]{#_Toc397088671}[]{#_Toc397088672}[]{#_Toc397088673}[]{#_Toc397088674}[]{#_Toc397088675}[]{#_Toc397088676}[]{#_Toc397088677}[]{#_Toc397088678}[]{#_Toc397088679}[]{#_Toc397088680}[]{#_Toc397088681}[]{#_Toc397088682}[]{#_Toc397088683}[]{#_Toc397088684}[]{#_Toc397088685}[]{#_Toc397088686}[]{#_Toc397088687}[]{#_Toc397088688}[]{#_Toc397088689}[]{#_Toc397088690}[]{#_Toc397088691}[]{#_Toc397088692}[]{#_Toc397088693}[]{#_Toc397088694}[]{#_Toc397088695}[]{#_Toc397088696}[]{#_Toc397088697}[]{#_Toc397088698}[]{#_Toc397088699}[]{#_Toc397088700}[]{#_Toc397088701}[]{#_Toc397088702}[]{#_Toc397088703}[]{#_Toc397088704}[]{#_Toc397088705}[]{#_Toc397088751}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- client-security intrusion-protection timer temporary-service-stop**

------------------------------------------------------------------------

[**[client-security intrusion-protection timer temporary-service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_469375820}[命令用来配置临时关闭]{style="font-family:宋体"}[BSS]{lang="EN-US"}[服务的时长。]{style="font-family:宋体"}

[**[undo client-security intrusion-protection timer temporary-service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_x1089560778}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1320004671}

[**[client-security intrusion-protection timer]{lang="EN-US"}***[ ]{lang="EN-US"}***[temporary-service-stop ]{lang="EN-US"}***[value ]{lang="EN-US"}*]{#struct_0_x2098_10749_x1810224743}

[**[undo client-security intrusion-protection timer temporary-service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_x683561331}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1641825946}

[[临时关闭]{style="font-family:宋体"}[BSS]{lang="EN-US"}]{#struct_0_x2098_10749_95613163}[服务时长为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_506134684}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_1338834577}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_762593708}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1633003167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1489799611}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x101301637}

[*[value]{lang="EN-US"}*]{#struct_0_x2098_10749_x1919457889}[：无线服务临时关闭时长，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_84849745}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1027589391}

[[当入侵保护功能处于使能状态，且入侵保护措施为临时关闭服务（]{style="font-family:宋体"}**[temporary-service-stop]{lang="EN-US"}**]{#struct_0_x2098_10749_1225288182}[）时，如果设备检测到非法报文，则在该配置指定的时间段内关闭用户所在的]{style="font-family:宋体"}[BSS]{lang="EN-US"}[所提供的所有服务，在此期间用户将无法通过该服务接入网络，这段时间之后恢复正常。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1650534158}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x2012161980}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下配置临时关闭]{style="font-family:宋体"}[BSS]{lang="EN-US"}[服务的时长为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x362500642}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection enable]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection action temporary-service-stop]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] client-security intrusion-protection temporary-service-stop timer 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1859378903}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection enable]{lang="EN-US"}**]{#struct_0_x2098_10749_413426864}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security intrusion-protection action]{lang="EN-US"}**]{#struct_0_x2098_10749_1533060406}
:::

::::: {#267779654 .myid}
[]{#_Toc404795045}[]{#struct_0_x2098_10749_x2112303760}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- display wlan client-security block-mac （仅AC）**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](WLAN用户接入认证命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2098_10749_184490236}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2098_10749_717576571}
:::

[ ]{lang="EN-US"}

[**[display wlan client-security block-mac]{lang="EN-US"}**]{#struct_0_x2098_10749_x262166907}[命令用来显示阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1269441437}

[**[display wlan client-security block-mac]{lang="EN-US"}**[ \[ **ap** *ap-name* \[ **radio** *radio-id* \] \]]{lang="EN-US"}]{#struct_0_x2098_10749_54693310}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1184253911}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1461882549}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1009433729}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1525274411}

[[network-operator]{lang="EN-US"}]{#struct_0_x2098_10749_x1557831242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1829450079}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2098_10749_1851405145}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1624646270}

[**[ap]{lang="EN-US"}**[ *ap-name*]{lang="EN-US"}]{#struct_0_x2098_10749_1679682211}[：显示接入指定]{style="font-family:宋体"}[AP]{lang="EN-US"}[的所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，]{style="font-family:宋体"}*[ap-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AP]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，则显示所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[**[radio]{lang="EN-US"}**[ *radio-id*]{lang="EN-US"}]{#struct_0_x2098_10749_x1104732677}[：显示接入指定]{style="font-family:宋体"}[Radio]{lang="EN-US"}[的所有阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息，]{style="font-family:宋体"}*[radio-id]{lang="EN-US"}*[表示]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号，取值范围与设备型号有关。如果未指定本参数，则显示]{style="font-family:宋体"}[AP]{lang="EN-US"}[下所有]{style="font-family:宋体"}[Radio]{lang="EN-US"}[下的阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x2057616770}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_616579595}[是指入侵检测模式为]{style="font-family:宋体"}**[temporary-block]{lang="EN-US"}**[时，被加入到阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[列表中的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_881228866}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_1516094406}[显示所有阻塞]{style="font-family:宋体"}[ MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan client-security block mac-address]{lang="EN-US"}]{#struct_0_x2098_10749_x159787120}

[MAC address         AP ID       RADIO ID     BSSID]{lang="EN-US"}

[0002-0002-0002      1           1            00AB-0DE1-0001]{lang="EN-US"}

[000d-88f8-0577      1           1            0EF1-0001-02C1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries: 2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan client-security block mac-address]{lang="EN-US"}]{#struct_0_x2098_10749_x2108767631}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1095567516}[[字段]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1417991103}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2098_10749_98640571}

[[MAC address]{lang="EN-US"}]{#struct_0_x2098_10749_x1278315212}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1587135909}[地址，格式为"]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}["]{style="font-family:宋体"}

[[AP ID]{lang="EN-US"}]{#struct_0_x2098_10749_x1455225902}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1756821052}[地址所在]{style="font-family:宋体"}[AP]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[RADIO ID]{lang="EN-US"}]{#struct_0_x2098_10749_x2057616769}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1756007864}[地址所在的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[BSSID]{lang="EN-US"}]{#struct_0_x2098_10749_2144695753}

[[基本服务集标识符，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}]{#struct_0_x2098_10749_x1978607157}

[[Total entries]{lang="EN-US"}]{#struct_0_x2098_10749_652503735}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x394681918}[地址表项条数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x218794291}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security instrusion-protection action]{lang="EN-US"}**]{#struct_0_x2098_10749_x353786571}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security instrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_108476169}

::::: {#1686734038 .myid}
[]{#_Toc404795046}[]{#struct_0_x2098_10749_x964966224}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- display wlan client-security block-mac（仅FAT AP）**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![](WLAN用户接入认证命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x2098_10749_1344465829}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x2049251965}
:::

[ ]{lang="EN-US"}

[**[display wlan client-security block-mac]{lang="EN-US"}**]{#struct_0_x2098_10749_x1764172471}[命令用来显示阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x131762223}

[**[display wlan client-security block-mac]{lang="EN-US"}**]{#struct_0_x2098_10749_x1703556114}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1591263435}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x205451337}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1392928254}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1045450061}

[[network-operator]{lang="EN-US"}]{#struct_0_x2098_10749_681533878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1739099101}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x2098_10749_1618167127}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1777632862}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1393783397}[是指入侵检测模式为]{style="font-family:宋体"}**[temporary-block]{lang="EN-US"}**[时，被加入到阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}[列表中的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1293295685}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x415838424}[显示所有阻塞]{style="font-family:宋体"}[ MAC]{lang="EN-US"}[地址信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan client-security block mac-address]{lang="EN-US"}]{#struct_0_x2098_10749_x1771535278}

[MAC address         AP ID       RADIO ID     BSSID]{lang="EN-US"}

[0002-0002-0002      1           1            00AB-0DE1-0001]{lang="EN-US"}

[000d-88f8-0577      1           1            0EF1-0001-02C1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total entries: 2]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display wlan client-security block mac-address]{lang="EN-US"}]{#struct_0_x2098_10749_x196816567}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1317261285}[[字段]{style="font-family:黑体"}]{#struct_0_x2098_10749_x423555107}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1990286488}

[[MAC address]{lang="EN-US"}]{#struct_0_x2098_10749_x1068332562}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1368250751}[地址，格式为"]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}["]{style="font-family:宋体"}

[[AP ID]{lang="EN-US"}]{#struct_0_x2098_10749_141336180}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_1562742957}[地址所在]{style="font-family:宋体"}[AP]{lang="EN-US"}[的编号]{style="font-family:宋体"}

[[RADIO ID]{lang="EN-US"}]{#struct_0_x2098_10749_361053339}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_1360632604}[地址所在的]{style="font-family:宋体"}[Radio]{lang="EN-US"}[编号]{style="font-family:宋体"}

[[BSSID]{lang="EN-US"}]{#struct_0_x2098_10749_x1740096320}

[[基本服务集标识符，格式为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}]{#struct_0_x2098_10749_1865724250}

[[Total entries]{lang="EN-US"}]{#struct_0_x2098_10749_1407686771}

[[阻塞]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1590096681}[地址表项条数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_944005123}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security instrusion-protection action]{lang="EN-US"}**]{#struct_0_x2098_10749_958649850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-security instrusion-protection timer temporary-block]{lang="EN-US"}**]{#struct_0_x2098_10749_746385341}

::: {#-1933770014 .myid}
[]{#_Toc404795047}[]{#struct_0_x2098_10749_1559409099}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x domain**

------------------------------------------------------------------------

[**[dot1x domain]{lang="EN-US"}**]{#struct_0_x2098_10749_x488024878}[命令用来指定无线服务模板下]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户的认证域。]{style="font-family:宋体"}

[**[undo dot1x domain]{lang="EN-US"}**]{#struct_0_x2098_10749_x1614080401}[命令用来删除该无线服务模板下]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户的认证域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_236459590}

[**[dot1x domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_x2098_10749_336825973}

[**[undo dot1x domain]{lang="EN-US"}**]{#struct_0_x2098_10749_x1070851380}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x2057616768}

[[未指定无线服务模板下的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_972875491}[用户的认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1464106809}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_817172303}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1079131355}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1255009104}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_954619214}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_351238284}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x2098_10749_2113409799}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1566058846}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_1327738615}

[[从无线服务模板上接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x394733480}[用户将按照如下先后顺序进行选择认证域：无线服务模板下指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[用户名中指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统缺省的认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_358074495}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_358957441}[配置无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户使用认证域为]{style="font-family:宋体"}[my-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x2057616767}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] dot1x domain my-domain]{lang="EN-US"}
:::

::: {#607202358 .myid}
[]{#_Toc404795048}[]{#struct_0_x2098_10749_x1966091199}[]{#_Toc370972446}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x handshake enable**

------------------------------------------------------------------------

[**[dot1x handshake enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1384430190}[命令用来使能指定无线服务模板下的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户握手功能。]{style="font-family:宋体"}

[**[undo dot1x handshake enable]{lang="EN-US"}**]{#struct_0_x2098_10749_676193438}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x886765231}

[**[dot1x handshake enable]{lang="EN-US"}**]{#struct_0_x2098_10749_143494167}

[**[undo dot1x handshake enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1614766244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x743667931}

[[无线服务模板下的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x1048065401}[在线用户握手功能处于关闭状态，即不与]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户进行握手。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_726940270}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x911072616}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_282454146}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x603677665}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_67915638}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_281035384}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_124557868}

[[该命令只对进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_1564665875}[接入认证且成功上线的用户有效。]{style="font-family:宋体"}

[[使能]{style="font-family:宋体"}]{#struct_0_x2098_10749_x2109171061}[802.1X]{lang="EN-US"}[握手功能之后，设备将定期向通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证的在线用户发送握手报文，即单播]{style="font-family:宋体"}[EAP-Request/Identity]{lang="EN-US"}[报文，来检测用户的在线状态。握手报文发送的时间间隔由]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[握手定时器控制（时间间隔通过命令]{style="font-family:宋体"}**[dot1x timer handshake-period]{lang="EN-US"}**[设置）。如果连续发送握手报文的次数达到]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[报文最大重发次数，而还没有收到用户响应，则强制该用户下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x388865613}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x1620538252}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_4792142}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] ]{lang="EN-US"}[dot1x handshake enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1409507094}

[]{#struct_0_x2098_10749_950960417}[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x handshake secure]{lang="EN-US"}**]{#_Toc232302548}**[ ]{lang="EN-US"}[enable]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x retry]{lang="EN-US"}**]{#struct_0_x2098_10749_x1737824065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer handshake-period]{lang="EN-US"}**]{#struct_0_x2098_10749_1732150680}
:::

::: {#-1511250361 .myid}
[]{#_Toc404795049}[]{#struct_0_x2098_10749_1904369867}[]{#_Toc370972447}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x handshake secure enable**

------------------------------------------------------------------------

[**[dot1x handshake secure enable]{lang="EN-US"}**]{#struct_0_x2098_10749_1827683710}[命令用来使能]{style="font-family:
宋体"}[802.1X]{lang="EN-US"}[的在线用户的安全握手功能。]{style="font-family:宋体"}

[**[undo dot1x handshake secure enable]{lang="EN-US"}**]{#struct_0_x2098_10749_1678348654}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x609578924}

[**[dot1x handshake secure enable]{lang="EN-US"}**]{#struct_0_x2098_10749_281035385}

[**[undo dot1x handshake secure enable]{lang="EN-US"}**]{#struct_0_x2098_10749_124557867}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1564665862}

[[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x2108843382}[的在线用户的安全握手功能处于关闭状态，即不对]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[在线用户进行安全握手检查。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1843208599}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_767230828}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x225937841}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_388140318}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1776157999}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1813318904}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1199920608}

[[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x580305809}[安全握手功能只有在开启了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[握手功能的前提下才生效。]{style="font-family:宋体"}

[[该命令只对进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_744262575}[接入认证且成功上线的用户有效。]{style="font-family:宋体"}

[[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_1224330068}[安全握手是指在握手报文中加入验证信息，以防止非法用户仿冒正常用户在线的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[的客户端与设备进行握手报文的交互。使能]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[安全握手功能后，支持安全握手的客户端需要在每次向设备发送的握手应答报文中携带验证信息，设备将其与认证服务器下发的验证信息进行对比，如果不一致，则强制用户下线。]{style="font-family:宋体"}

[[验证信息由认证服务器下发，当用户上线认证成功时，服务器在认证回复报文中携带验证密钥和验证信息。设备保存验证信息，而将验证密钥通过发送给客户端。之后，当用户需要响应设备的握手报文时，首先使用验证密钥计算出一个验证信息，然后将该验证信息携带在握手回应报文]{style="font-family:宋体"}[EAPOL EAP-Response Identity]{lang="EN-US"}]{#struct_0_x2098_10749_x433179647}[中发给设备。]{style="font-family:宋体"}

[[服务器会周期性地更新验证密钥与验证信息，并通过计费响应报文下发给设备。设备同样会将验证密钥发送给客户端，而保存验证信息用于校验客户端响应报文的合法性。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x745336247}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_281035386}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_124557870}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下使能]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[安全握手功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x773986293}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] dot1x handshake enable]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] dot1x handshake secure enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x846086516}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x handshake enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x178957113}
:::

::: {#-1061994866 .myid}
[]{#_Toc404795050}[]{#struct_0_x2098_10749_x1715682387}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x max-user**

------------------------------------------------------------------------

[**[dot1x max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_44900029}[命令用来配置无线服务模板上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[最大用户数。当接入此无线服务模板的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户数超过最大值后，新的用户将被拒绝。]{style="font-family:宋体"}

[**[undo dot1x max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_x1746837737}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_706258045}

[**[dot1x max-user]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_x2098_10749_x1909769816}

[**[undo dot1x max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_777477755}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x641310275}

[[当前无线服务模板上允许同时接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_281035387}[用户数为]{style="font-family:宋体"}[4096]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_124557869}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_1564665876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x2109105525}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_569919935}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_10235409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_248259616}

[*[count]{lang="EN-US"}*]{#struct_0_x2098_10749_1179276364}[：无线服务模板上最多允许同时接入的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x886640403}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_x229489364}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1968301359}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x1681686141}[配置无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[最大用户数为]{style="font-family:宋体"}[500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x64416320}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] dot1x max-user 500]{lang="EN-US"}
:::

::: {#14458242 .myid}
[]{#_Toc404795051}[]{#struct_0_x2098_10749_x1111693301}[]{#_Toc370976460}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- dot1x re-authenticate enable**

------------------------------------------------------------------------

[**[dot1x re-authenticate enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1202876244}[命令用来开启无线服务模板上的]{style="font-family:
宋体"}[802.1X]{lang="EN-US"}[周期性重认证功能。]{style="font-family:
宋体"}

[**[undo dot1x re-authenticate enable]{lang="EN-US"}**]{#struct_0_x2098_10749_343931134}[命令用来关闭无线服务模板上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[周期性重认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1984927641}

[**[dot1x re-authenticate enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1481518048}

[**[undo dot1x re-authenticate enable]{lang="EN-US"}**]{#struct_0_x2098_10749_x1566227105}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_661948241}

[[无线服务模板上的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_567803268}[周期性重认证功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_903875904}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x504667389}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_281035389}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_124557879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x773986284}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x846545267}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_967291744}

[[无线服务模板启动了]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x255026430}[的周期性重认证功能后，设备会根据系统视图下配置的周期性重认证定时器（]{style="font-family:宋体"}**[dot1x timer reauth-period]{lang="EN-US"}**[）时间间隔对在线]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户启动认证，以检测用户连接状态的变化，更新服务器下发的授权属性（例如]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[，]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[用户进行]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_x2098_10749_x1348717052}[认证成功后，如果服务器下发了]{style="font-family:宋体"}[Termination action]{lang="EN-US"}[和]{style="font-family:宋体"}[Session timeout]{lang="EN-US"}[属性，且]{style="font-family:宋体"}[Termination action]{lang="EN-US"}[取值为]{style="font-family:宋体"}[Radius-Request]{lang="EN-US"}[，]{style="font-family:宋体"}[Session timeout]{lang="EN-US"}[取值不为]{style="font-family:宋体"}[0]{lang="EN-US"}[，设备将以]{style="font-family:宋体"}[Session timeout]{lang="EN-US"}[为周期对用户进行重认证，以检测用户在线状态，并更新授权信息。]{style="font-family:宋体"}

[[在认证服务器没有下发]{style="font-family:宋体"}[Terminal action]{lang="EN-US"}]{#struct_0_x2098_10749_882437111}[和]{style="font-family:宋体"}[Session timeout]{lang="EN-US"}[属性或下发的]{style="font-family:宋体"}[Terminal action]{lang="EN-US"}[取值不为]{style="font-family:宋体"}[Request]{lang="EN-US"}[的情况下，如果使能]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[重认证功能，设备也会定期向已经在线的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户发起重认证，此时重认证周期由]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[重认证定时器配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_968147556}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_32758682}[在无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[上开启]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[重认证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_850296872}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] dot1x re-authenticate enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_281035390}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dot1x timer]{lang="EN-US"}**]{#struct_0_x2098_10749_x166961943}
:::

::: {#1131898116 .myid}
[]{#_Toc404795052}[]{#struct_0_x2098_10749_x1559783872}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- mac-authentication domain**

------------------------------------------------------------------------

[**[mac-authentication domain]{lang="EN-US"}**]{#struct_0_x2098_10749_x885896604}[命令用来指定无线服务模板下]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证用户的认证域。]{style="font-family:
宋体"}

[**[undo mac-authentication domain]{lang="EN-US"}**]{#struct_0_x2098_10749_1862020772}[命令用来删除该无线服务模板下的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证用户的认证域。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1322931153}

[**[mac-authentication domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_x2098_10749_x150558887}

[**[undo mac-authentication domain]{lang="EN-US"}**]{#struct_0_x2098_10749_x1204250806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1007080170}

[[未指定无线服务模板下的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_x1314053137}[地址认证用户的认证域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_931342679}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_281035391}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1831757265}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x1733045884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_x792494225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1366620306}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x2098_10749_1774670730}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1\~255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x1782106941}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_48121664}

[[从无线服务模板上接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_1036770810}[地址认证用户将按照如下先后顺序进行选择认证域：无线服务模板下指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[全局]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统缺省的认证域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x264825669}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_145975501}[配置无线服务模板]{style="font-family:宋体"}[service1]{lang="EN-US"}[下]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户使用的认证域为]{style="font-family:宋体"}[my-domain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_281035392}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] mac-authentication domain my-domain]{lang="EN-US"}
:::

::: {#273853227 .myid}
[]{#_Toc404795053}[]{#struct_0_x2098_10749_x922630514}

**WLAN用户接入认证 \-- WLAN用户接入认证配置命令 \-- mac-authentication max-user**

------------------------------------------------------------------------

[**[mac-authentication max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_1306263961}[命令用来配置无线服务模板上的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证最大用户数。当接入此无线服务模板的]{style="font-family:
宋体"}[MAC]{lang="EN-US"}[地址认证用户数超过最大值后，新接入的用户将被拒绝。]{style="font-family:宋体"}

[**[undo mac-authentication max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_x2009813101}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x2098_10749_945242703}

[**[mac-authentication max-user]{lang="EN-US"}**[ *count*]{lang="EN-US"}]{#struct_0_x2098_10749_x1753607687}

[**[undo mac-authentication max-user]{lang="EN-US"}**]{#struct_0_x2098_10749_573630911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x2098_10749_604386421}

[[当前无线服务模板上允许同时接入的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x2098_10749_1512592622}[地址认证用户数为]{style="font-family:宋体"}[4096]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x2098_10749_281035393}

[[无线服务模板视图]{style="font-family:宋体"}]{#struct_0_x2098_10749_x1831757263}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x926476830}

[[network-admin]{lang="EN-US"}]{#struct_0_x2098_10749_1863850019}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x2098_10749_153113283}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x2098_10749_397409842}

[*[count]{lang="EN-US"}*]{#struct_0_x2098_10749_1159497643}[：可接入无线服务模板的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x2098_10749_x158731188}

[[该命令只能在无线服务模板处于关闭的状态下进行配置。]{style="font-family:宋体"}]{#struct_0_x2098_10749_992706073}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x2098_10749_1853378921}

[[\# ]{lang="EN-US"}]{#struct_0_x2098_10749_x1775121906}[配置最大接入]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户数为]{style="font-family:宋体"}[32]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x2098_10749_x1675279752}

[\[Sysname\] wlan service-template service1]{lang="EN-US"}

[\[Sysname-wlan-st-service1\] mac-authentication max-user 32]{lang="EN-US"}
:::
