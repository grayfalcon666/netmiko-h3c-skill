::: {#-947553691 .myid}
[]{#_Toc404795175}[]{#struct_0_79555_16151_x1175187535}[]{#_Toc399680964}[]{#_Toc396222834}

**漫游 \-- 漫游配置命令 \-- authentication-mode**

------------------------------------------------------------------------

[**[authentication-mode]{lang="IT"}**]{#struct_0_79555_16151_x1981016960}[命令用来配置漫游组认证模式。]{style="font-family:宋体"}

[**[undo authentication-mode]{lang="IT"}**]{#struct_0_79555_16151_x538118511}**[ ]{lang="IT"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x988838170}

[**[authentication-mode ]{lang="IT"}**]{#struct_0_79555_16151_1389666451}*[authentication-mode ]{lang="IT"}*[\[ **cipher** \| **simple** \] *authentication-key*]{lang="IT"}

[**[undo authentication-mode]{lang="IT"}**]{#struct_0_79555_16151_x50765727}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_79555_16151_x235647113}

[[未配置认证模式]{style="font-family:宋体"}]{#struct_0_79555_16151_x290945789}[，]{style="font-family:宋体"}[即]{style="font-family:宋体"}[不对]{style="font-family:宋体"}[IACTP]{lang="IT"}[控制消息进行完整性校验]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_x344816541}

[[本地漫游组视图]{style="font-family:宋体"}]{#struct_0_79555_16151_x1318562260}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_586029308}

[[network-admin]{lang="IT"}]{#struct_0_79555_16151_x1277648669}

[[mdc-admin]{lang="IT"}]{#struct_0_79555_16151_743709580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1765362546}

[**[cipher]{lang="IT"}**]{#struct_0_79555_16151_89184147}**[：]{style="font-family:宋体"}**[以密文方式设置密钥。]{style="font-family:宋体"}

[**[simple]{lang="IT"}**]{#struct_0_79555_16151_988530841}**[：]{style="font-family:宋体"}**[以明文方式设置密钥。]{style="font-family:宋体"}

[*[authentication-key]{lang="IT"}*]{#struct_0_79555_16151_x59576122}**[：]{style="font-family:宋体"}**[设置明文密钥或密文密钥]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。明文密钥的长度范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[；密文密钥的长度范围是]{style="font-family:宋体"}[24]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_1800319402}

[[配置认证模式后，所有在]{style="font-family:宋体;color:windowtext"}]{#struct_0_79555_16151_x2018034304}[IACTP]{lang="EN-US" style="color:windowtext"}[隧道中传输的控制消息都会附带一个摘要（完整性代码），该代码用来与消息内容进行计算。当]{style="font-family:宋体;
color:windowtext"}[AC]{lang="EN-US" style="color:windowtext"}[接收到该消息后会重新计算并与消息中携带的摘要进行比较来确认收到的消息的完整性。]{style="font-family:宋体;
color:windowtext"}

[[以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体;color:windowtext"}]{#struct_0_79555_16151_989457265}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_x739341063}

[[\# ]{lang="IT"}]{#struct_0_79555_16151_x713724496}[配置]{style="font-family:宋体"}[IACTP]{lang="IT"}[控制消息完整性认证模式为]{style="font-family:宋体"}[MD5]{lang="IT"}[认证模式，以明文方式设置密钥]{style="font-family:宋体"}[12345]{lang="IT"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_79555_16151_x36592334}

[\[Sysname\] wlan mobility group aaa]{lang="IT"}

[\[Sysname-wlan-mg-aaa\] authentication-mode md5 plain 12345]{lang="EN-US"}
:::

::: {#-591617093 .myid}
[]{#_Toc404795176}[]{#struct_0_79555_16151_1502510966}

**漫游 \-- 漫游配置命令 \-- display wlan mobility**

------------------------------------------------------------------------

[**[display wlan mobility]{lang="EN-US"}**]{#struct_0_79555_16151_x980054633}[命令用来显示客户端漫入或漫出的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x826403213}

[**[display wlan mobility ]{lang="IT"}**[{ **roam-in** \| **roam-out** } \[ **member** { **ip** *ipv4-address* \| **ipv6** *ipv6-address* } \]]{lang="EN-US"}]{#struct_0_79555_16151_449863464}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_1306990296}

[[任意视图]{style="font-family:宋体"}]{#struct_0_79555_16151_265757388}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x997344551}

[[network-admin]{lang="EN-US"}]{#struct_0_79555_16151_106559541}

[[network-operator]{lang="EN-US"}]{#struct_0_79555_16151_1433049649}

[[mdc-admin]{lang="EN-US"}]{#struct_0_79555_16151_x739752612}

[[mdc-operator]{lang="EN-US"}]{#struct_0_79555_16151_x1503933462}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_467659222}

[**[roam-in]{lang="EN-US"}**]{#struct_0_79555_16151_1813514590}[：显示漫入客户端的信息，即从其它]{style="font-family:宋体"}[AC]{lang="EN-US"}[漫游到本]{style="font-family:宋体"}[AC]{lang="EN-US"}[的客户端信息。]{style="font-family:宋体"}

[**[roam-out]{lang="EN-US"}**]{#struct_0_79555_16151_x1231235337}[：显示漫出客户端的信息，即从本]{style="font-family:宋体"}[AC]{lang="EN-US"}[漫游到其它]{style="font-family:宋体"}[AC]{lang="EN-US"}[的客户端信息。]{style="font-family:宋体"}

[**[member ip ]{lang="EN-US"}***[ipv4-address]{lang="EN-US"}*]{#struct_0_79555_16151_867387719}[：]{style="font-family:宋体"}[漫游组成员]{style="font-family:宋体"}[AC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[member ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_79555_16151_x1032022379}[：]{style="font-family:宋体"}[漫游组成员]{style="font-family:宋体"}[AC]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1854095819}

[[如果不指定]{style="font-family:宋体"}]{#struct_0_79555_16151_1748828722}**[member]{lang="EN-US"}**[参数，则显示所有客户端漫入或漫出的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_1196746663}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_1912422792}[显示所有]{style="font-family:宋体"}[漫入客户端的]{style="font-family:
宋体"}[信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan mobility roam-in]{lang="EN-US"}]{#struct_0_79555_16151_2109938546}

[Total entries: 1]{lang="EN-US"}

[MAC address     BSSID           VLAN ID  HA IP address]{lang="EN-US"}

[5250-0012-0411  cbab-abab-abab  1        192.168.0.101]{lang="EN-US"}

[[\# ]{lang="EN-US" style="font-family:宋体"}]{#struct_0_79555_16151_x1318798604}[显示从指定成员]{style="font-family:宋体"}[AC]{lang="EN-US"}[漫]{style="font-family:宋体"}[入]{style="font-family:宋体"}[的]{style="font-family:宋体"}[客户端信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan mobility roam-in member ip 192.168.0.101]{lang="EN-US"}]{#struct_0_79555_16151_x327728489}

[Total entries: 1]{lang="EN-US"}

[MAC address     BSSID           VLAN ID]{lang="EN-US"}

[5250-0012-0411  cbab-abab-abab  1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_x5134757}[显示所有漫出客户端的信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan mobility roam-out]{lang="EN-US"}]{#struct_0_79555_16151_x966438479}

[Total entries: 1]{lang="EN-US"}

[MAC address     BSSID           VLAN ID  Online time       FA IP address]{lang="EN-US"}

[5250-0012-0411  cbab-abab-abab  1        00hr 01min 39sec  192.168.0.102]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_111836273}[显示从指定成员]{style="font-family:宋体"}[AC]{lang="EN-US"}[漫出的客户端信息。]{style="font-family:宋体"}

[[\[Sysname\] display wlan mobility roam-out member ip 192.168.0.102]{lang="EN-US"}]{#struct_0_79555_16151_1971526677}

[Total entries: 1]{lang="EN-US"}

[MAC address     BSSID           VLAN ID  Online time]{lang="EN-US"}

[5250-0012-0411  cbab-abab-abab  1        00hr 03min 02sec]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display wlan mobility]{lang="EN-US"}]{#struct_0_79555_16151_x203427839}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_159284470}[[字段]{style="font-family:黑体"}]{#struct_0_79555_16151_x1565307084}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_79555_16151_182744781}

[[Total entries]{lang="EN-US"}]{#struct_0_79555_16151_49987264}

[[客户端总数目]{style="font-family:宋体"}]{#struct_0_79555_16151_423833992}

[[MAC address]{lang="EN-US"}]{#struct_0_79555_16151_x1061408716}

[[客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_79555_16151_662460164}[地址]{style="font-family:宋体"}

[[BSSID]{lang="EN-US"}]{#struct_0_79555_16151_x1907324469}

[[客户端关联的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_79555_16151_1258481090}[的]{style="font-family:宋体"}[BSSID]{lang="EN-US"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_79555_16151_x1293635591}

[[客户端所在的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_79555_16151_x478126023}

[[HA IP address]{lang="EN-US"}]{#struct_0_79555_16151_216645020}

[[HA]{lang="EN-US"}]{#struct_0_79555_16151_x430487601}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[FA IP address]{lang="EN-US"}]{#struct_0_79555_16151_x1383339160}

[[FA]{lang="EN-US"}]{#struct_0_79555_16151_x522656705}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Online time]{lang="EN-US"}]{#struct_0_79555_16151_x259254173}

[[客户端的累积在线时长]{style="font-family:宋体"}]{#struct_0_79555_16151_1856511860}

[ ]{lang="EN-US"}

::: {#31478898 .myid}
[]{#_Toc31535694}[]{#_Toc404795177}[]{#struct_0_79555_16151_1535750093}[]{#_Toc135538258}[]{#_Toc135538259}[]{#_Toc135538261}[]{#_Toc135538262}[]{#_Toc135538263}[]{#_Toc135538264}[]{#_Toc135538265}[]{#_Toc135538266}[]{#_Toc135538267}[]{#_Toc135538268}[]{#_Toc135538269}[]{#_Toc135538270}[]{#_Toc135538271}[]{#_Toc135538272}[]{#_Toc135538273}[]{#_Toc135538274}[]{#_Toc135538275}[]{#_Toc135538276}[]{#_Toc135538277}[]{#_Toc135538278}[]{#_Toc135538279}[]{#_Toc135538280}[]{#_Toc135538282}[]{#_Toc135538283}[]{#_Toc135538286}[]{#_Toc135538287}[]{#_Toc135538288}[]{#_Toc135538289}[]{#_Toc135538290}[]{#_Toc135538291}[]{#_Toc135538292}[]{#_Toc135538293}[]{#_Toc135538294}[]{#_Toc135538295}[]{#_Toc135538296}[]{#_Toc135538297}[]{#_Toc135538298}[]{#_Toc60064281}[]{#_Toc60649243}[]{#_Toc76002874}[]{#_Toc76444799}[]{#_Toc60064283}[]{#_Toc60649245}[]{#_Toc76002876}[]{#_Toc76444801}[]{#_Toc60064284}[]{#_Toc60649246}[]{#_Toc76002877}[]{#_Toc76444802}[]{#_Toc60064285}[]{#_Toc60649247}[]{#_Toc76002878}[]{#_Toc76444803}[]{#_Toc60064286}[]{#_Toc60649248}[]{#_Toc76002879}[]{#_Toc76444804}[]{#_Toc60064287}[]{#_Toc60649249}[]{#_Toc76002880}[]{#_Toc76444805}[]{#_Toc60064288}[]{#_Toc60649250}[]{#_Toc76002881}[]{#_Toc76444806}[]{#_Toc60064289}[]{#_Toc60649251}[]{#_Toc76002882}[]{#_Toc76444807}[]{#_Toc60064290}[]{#_Toc60649252}[]{#_Toc76002883}[]{#_Toc76444808}[]{#_Toc60064291}[]{#_Toc60649253}[]{#_Toc76002884}[]{#_Toc76444809}[]{#_Toc60064292}[]{#_Toc60649254}[]{#_Toc76002885}[]{#_Toc76444810}[]{#_Toc35952971}[]{#_Toc35953374}[]{#_Toc35954258}[]{#_Toc35955135}[]{#_Toc60064295}[]{#_Toc60649257}[]{#_Toc76002888}[]{#_Toc76444813}[]{#_Toc60064296}[]{#_Toc60649258}[]{#_Toc76002889}[]{#_Toc76444814}[]{#_Toc60064297}[]{#_Toc60649259}[]{#_Toc76002890}[]{#_Toc76444815}[]{#_Toc60064298}[]{#_Toc60649260}[]{#_Toc76002891}[]{#_Toc76444816}[]{#_Toc60064299}[]{#_Toc60649261}[]{#_Toc76002892}[]{#_Toc76444817}[]{#_Toc60064300}[]{#_Toc60649262}[]{#_Toc76002893}[]{#_Toc76444818}[]{#_Toc60064301}[]{#_Toc60649263}[]{#_Toc76002894}[]{#_Toc76444819}[]{#_Toc60064302}[]{#_Toc60649264}[]{#_Toc76002895}[]{#_Toc76444820}[]{#_Toc60064303}[]{#_Toc60649265}[]{#_Toc76002896}[]{#_Toc76444821}[]{#_Toc60064304}[]{#_Toc60649266}[]{#_Toc76002897}[]{#_Toc76444822}[]{#_Toc60064305}[]{#_Toc60649267}[]{#_Toc76002898}[]{#_Toc76444823}[]{#_Toc60064306}[]{#_Toc60649268}[]{#_Toc76002899}[]{#_Toc76444824}[]{#_Toc60064307}[]{#_Toc60649269}[]{#_Toc76002900}[]{#_Toc76444825}[]{#_Toc60064309}[]{#_Toc60649271}[]{#_Toc76002902}[]{#_Toc76444827}[]{#_Toc60064312}[]{#_Toc60649274}[]{#_Toc76002905}[]{#_Toc76444830}[]{#_Toc60064313}[]{#_Toc60649275}[]{#_Toc76002906}[]{#_Toc76444831}[]{#_Toc60064314}[]{#_Toc60649276}[]{#_Toc76002907}[]{#_Toc76444832}[]{#_Toc60064315}[]{#_Toc60649277}[]{#_Toc76002908}[]{#_Toc76444833}[]{#_Toc60064316}[]{#_Toc60649278}[]{#_Toc76002909}[]{#_Toc76444834}[]{#_Toc60064317}[]{#_Toc60649279}[]{#_Toc76002910}[]{#_Toc76444835}[]{#_Toc60064318}[]{#_Toc60649280}[]{#_Toc76002911}[]{#_Toc76444836}[]{#_Toc60064319}[]{#_Toc60649281}[]{#_Toc76002912}[]{#_Toc76444837}[]{#_Toc60064320}[]{#_Toc60649282}[]{#_Toc76002913}[]{#_Toc76444838}[]{#_Toc60064321}[]{#_Toc60649283}[]{#_Toc76002914}[]{#_Toc76444839}[]{#_Toc239838245}[]{#_Toc239838246}[]{#_Toc239838247}[]{#_Toc239838248}[]{#_Toc239838249}[]{#_Toc239838250}[]{#_Toc239838251}[]{#_Toc239838252}[]{#_Toc239838253}[]{#_Toc239838254}[]{#_Toc239838255}[]{#_Toc239838256}[]{#_Toc239838257}[]{#_Toc239838258}[]{#_Toc239838259}[]{#_Toc239838261}[]{#_Toc239838263}[]{#_Toc239838264}[]{#_Toc239838265}[]{#_Toc239838266}[]{#_Toc239838267}[]{#_Toc239838268}[]{#_Toc239838269}[]{#_Toc239838270}[]{#_Toc239838271}[]{#_Toc239838272}[]{#_Toc239838273}[]{#_Toc239838274}[]{#_Toc239838275}[]{#_Toc239838276}[]{#_Toc239838277}[]{#_Toc239838278}[]{#_Toc239838279}[]{#_Toc239838280}[]{#_Toc239838281}[]{#_Toc239838282}[]{#_Toc239838283}[]{#_Toc239838284}[]{#_Toc239838290}[]{#_Toc239838291}[]{#_Toc239838292}[]{#_Toc239838293}[]{#_Toc239838317}[]{#_Toc239838319}[]{#_Toc239838320}[]{#_Toc239838321}[]{#_Toc239838322}[]{#_Toc239838323}[]{#_Toc239838324}[]{#_Toc239838325}[]{#_Toc239838326}[]{#_Toc239838327}[]{#_Toc239838328}[]{#_Toc239838329}[]{#_Toc239838330}[]{#_Toc239838331}[]{#_Toc239838332}[]{#_Toc239838333}[]{#_Toc239838334}[]{#_Toc239838335}[]{#_Toc239838336}[]{#_Toc239838337}[]{#_Toc239838338}[]{#_Toc239838339}[]{#_Toc239838341}[]{#_Toc239838342}[]{#_Toc239838343}[]{#_Toc239838356}

**漫游 \-- 漫游配置命令 \-- display wlan mobility roam-track mac-address**

------------------------------------------------------------------------

[**[display wlan mobility ]{lang="IT"}[roam-track mac-address]{lang="EN-US"}**]{#struct_0_79555_16151_1302860992}[命令用来]{style="font-family:宋体"}[在]{style="font-family:宋体"}[HA]{lang="EN-US"}[上显示客户端的漫游跟踪信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_183313129}

[**[display wlan mobility ]{lang="IT"}[roam-track mac-address ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_79555_16151_x1086807974}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_1243008112}

[[任意视图]{style="font-family:宋体"}]{#struct_0_79555_16151_2111629485}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1800460005}

[[network-admin]{lang="EN-US"}]{#struct_0_79555_16151_1233249606}

[[network-operator]{lang="EN-US"}]{#struct_0_79555_16151_x613857894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_79555_16151_x1706473532}

[[mdc-operator]{lang="EN-US"}]{#struct_0_79555_16151_x473204718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_1345544195}

[*[mac-address]{lang="EN-US"}*]{#struct_0_79555_16151_x503877424}[：客户端的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址，格式为[H-H-H]{lang="EN-US"}。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_379342776}

[[在显示信息中，漫游跟踪信息以漫游到达]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_79555_16151_196658507}[的先后依次排序，最近的轨迹排在第一行。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_476551723}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_1588490027}[显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址为]{style="font-family:宋体"}[5250-0012-0411]{lang="EN-US"}[的客户端的漫游跟踪信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan mobility roam-track mac-address 5250-0012-0411]{lang="EN-US"}]{#struct_0_79555_16151_x1401784593}

[Total entries: 2]{lang="EN-US"}

[BSSID           Online time       AC IP address]{lang="EN-US"}

[3ce5-a68d-2280  00hr 48min 46sec  192.168.0.2]{lang="EN-US"}

[0026-3e08-1150  00hr 40min 46sec  127.0.0.1]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display wlan mobility roam-track mac-address]{lang="EN-US"}]{#struct_0_79555_16151_270150156}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_151051746}[[字段]{style="font-family:黑体"}]{#struct_0_79555_16151_x777024472}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_79555_16151_x1877617659}

[[BSSID]{lang="EN-US"}]{#struct_0_79555_16151_712595903}

[[客户端关联的]{style="font-family:宋体"}[AP]{lang="EN-US"}]{#struct_0_79555_16151_x941804359}[的]{style="font-family:宋体"}[BSSID]{lang="EN-US"}

[[Online time]{lang="EN-US"}]{#struct_0_79555_16151_x220539746}

[[客户端]{style="font-family:宋体"}]{#struct_0_79555_16151_x986572112}[的累积在线时长]{style="font-family:宋体"}

[[AC IP address]{lang="EN-US"}]{#struct_0_79555_16151_x21668970}

[[客户端上线所在]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_79555_16151_x1783299300}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。当客户端在]{style="font-family:宋体"}[HA]{lang="EN-US"}[上时，显示的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}

[ ]{lang="EN-US"}

::: {#636545731 .myid}
[]{#_Toc94588348}[]{#_Toc80176767}[]{#_Toc30075865}[]{#_Toc404795178}[]{#struct_0_79555_16151_x558386721}[]{#_Toc87442250}[]{#_Toc87786890}[]{#_Toc87851752}[]{#_Toc87852533}[]{#_Toc87853312}[]{#_Toc87867351}[]{#_Toc87442257}[]{#_Toc87786897}[]{#_Toc87851759}[]{#_Toc87852540}[]{#_Toc87853319}[]{#_Toc87867358}[]{#_Toc87442265}[]{#_Toc87786905}[]{#_Toc87851767}[]{#_Toc87852548}[]{#_Toc87853327}[]{#_Toc87867366}[]{#_Toc76002916}[]{#_Toc76444841}

**漫游 \-- 漫游配置命令 \-- display wlan mobility group**

------------------------------------------------------------------------

[**[display wlan mobility group]{lang="EN-US"}**]{#struct_0_79555_16151_x1220266333}[命令用来显示本地漫游组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1872424693}

[**[display wlan mobility group ]{lang="EN-US"}**[\[*group-name* \]]{lang="EN-US"}]{#struct_0_79555_16151_1967054601}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_1654597176}

[[任意视图]{style="font-family:宋体"}]{#struct_0_79555_16151_699921453}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_712117585}

[[network-admin]{lang="EN-US"}]{#struct_0_79555_16151_x1389249433}

[[network-operator]{lang="EN-US"}]{#struct_0_79555_16151_1231418410}

[[mdc-admin]{lang="EN-US"}]{#struct_0_79555_16151_706984302}

[[mdc-operator]{lang="EN-US"}]{#struct_0_79555_16151_x1786623687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_x95839101}

[*[group-name]{lang="IT"}*]{#struct_0_79555_16151_x829653618}[：本地漫游组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_1065705322}

[[如果]{style="font-family:宋体"}]{#struct_0_79555_16151_x1269785996}[不指定本地漫游组名，则显示所有本地漫游组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_x274212884}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_x63968501}[显示指定本地漫游组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display wlan mobility group aaa]{lang="EN-US"}]{#struct_0_79555_16151_1453431758}

[Mobility group name: aaa]{lang="EN-US"}

[ Tunnel type: IPv4]{lang="EN-US"}

[ Source IPv4: 172.16.220.101]{lang="EN-US"}

[ Source IPv6: Not configured]{lang="EN-US"}

[Authentication mode  : Not configured]{lang="EN-US"}

[ Mobility group status: Enabled]{lang="EN-US"}

[ Member entries: 2]{lang="EN-US"}

[ IP address                              State          Online time]{lang="EN-US"}

[ 172.16.220.102                          Down           00hr 00min 00sec]{lang="EN-US"}

[ 172.16.220.105                          Up             00hr 36min 27sec]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display wlan mobility group]{lang="EN-US"}]{#struct_0_79555_16151_564113389}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_154520370}[[字段]{style="font-family:黑体"}]{#struct_0_79555_16151_x714228194}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_79555_16151_x948078901}

[[Mobility group name]{lang="EN-US"}]{#struct_0_79555_16151_229798948}

[[本地漫游组的名称]{style="font-family:宋体"}]{#struct_0_79555_16151_887107944}

[[Tunnel type]{lang="EN-US"}]{#struct_0_79555_16151_1628517665}

[[本地漫游组的]{style="font-family:宋体"}]{#struct_0_79555_16151_562282143}[隧道]{style="font-family:宋体"}[类型，有未配置，]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[三种隧道类型]{style="font-family:宋体"}

[[Source IPv4]{lang="EN-US"}]{#struct_0_79555_16151_977180177}

[[源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_79555_16151_x1100488958}[地址]{style="font-family:宋体"}

[[Source IPv6]{lang="EN-US"}]{#struct_0_79555_16151_x723173055}

[[源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_79555_16151_x834838880}[地址]{style="font-family:宋体"}

[[Authentication method]{lang="EN-US"}]{#struct_0_79555_16151_336103415}

[[本地漫游组的认证方式]{style="font-family:宋体"}]{#struct_0_79555_16151_x983622223}

[[Mobility group status]{lang="EN-US"}]{#struct_0_79555_16151_x1336284993}

[[本地漫游组的状态：]{style="font-family:宋体"}]{#struct_0_79555_16151_1533021686}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_79555_16151_x1309106057}[：本地漫游组处于开启状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_79555_16151_1692788358}[：本地漫游组处于关闭状态]{lang="EN-US" style="font-family:宋体"}

[[Member entries]{lang="EN-US"}]{#struct_0_79555_16151_1197978478}

[[成员]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_79555_16151_x735726927}[的数量]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_79555_16151_417790333}

[[成员]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#struct_0_79555_16151_1293849431}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_79555_16151_1892630067}

[[隧道]{style="font-family:宋体"}]{#struct_0_79555_16151_x216770459}[状态]{style="font-family:宋体"}

[[Up]{lang="EN-US"}]{#struct_0_79555_16151_586094844}[：已建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Down]{lang="EN-US"}]{#struct_0_79555_16151_x2023383835}[：未建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Online time]{lang="EN-US"}]{#struct_0_79555_16151_1939838731}

[[成员的累计在线时长]{style="font-family:宋体"}]{#struct_0_79555_16151_588822764}

[ ]{lang="EN-US"}

::: {#-385909106 .myid}
[]{#_Toc288742142}[]{#_Toc271292515}[]{#_Toc94588347}[]{#_Toc80176766}[]{#_Toc404795179}[]{#struct_0_79555_16151_x1940798339}[]{#_Toc309025272}[]{#_Toc307250849}[]{#_Toc309025273}[]{#_Toc307250850}[]{#_Toc309025274}[]{#_Toc307250851}[]{#_Toc309025275}[]{#_Toc307250852}[]{#_Toc309025276}[]{#_Toc307250853}[]{#_Toc309025277}[]{#_Toc307250854}[]{#_Toc309025278}[]{#_Toc307250855}[]{#_Toc309025279}[]{#_Toc307250856}[]{#_Toc309025280}[]{#_Toc307250857}[]{#_Toc309025281}[]{#_Toc307250858}[]{#_Toc309025282}[]{#_Toc307250859}[]{#_Toc309025283}[]{#_Toc307250860}[]{#_Toc309025284}[]{#_Toc307250861}[]{#_Toc309025285}[]{#_Toc307250862}[]{#_Toc309025286}[]{#_Toc307250863}[]{#_Toc309025287}[]{#_Toc307250864}[]{#_Toc309025288}[]{#_Toc307250865}[]{#_Toc309025289}[]{#_Toc307250866}[]{#_Toc309025290}[]{#_Toc307250867}[]{#_Toc309025291}[]{#_Toc307250868}[]{#_Toc309025292}[]{#_Toc307250869}[]{#_Toc309025293}[]{#_Toc307250870}[]{#_Toc309025294}[]{#_Toc307250871}[]{#_Toc309025295}[]{#_Toc307250872}[]{#_Toc309025296}[]{#_Toc307250873}[]{#_Toc309025297}[]{#_Toc307250874}[]{#_Toc309025298}[]{#_Toc307250875}[]{#_Toc309025299}[]{#_Toc307250876}[]{#_Toc309025300}[]{#_Toc307250877}[]{#_Toc309025301}[]{#_Toc307250878}[]{#_Toc309025302}

**漫游 \-- 漫游配置命令 \-- group enable**

------------------------------------------------------------------------

[**[group enable]{lang="IT"}**]{#struct_0_79555_16151_x33364323}[命令用来开启漫游组功能。]{style="font-family:宋体"}

[**[undo group enable]{lang="IT"}**]{#struct_0_79555_16151_x767469715}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1575554809}

[**[group enable]{lang="IT"}**]{#struct_0_79555_16151_389632362}

[**[undo group enable]{lang="IT"}**]{#struct_0_79555_16151_1865675255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_79555_16151_1559730828}

[[漫游组功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_79555_16151_x883088211}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_x979989097}

[[本地漫游组视图]{style="font-family:宋体"}]{#struct_0_79555_16151_x684988038}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_1735762039}

[[network-admin]{lang="IT"}]{#struct_0_79555_16151_x1994129940}

[[mdc-admin]{lang="IT"}]{#struct_0_79555_16151_808523239}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_203925520}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[只有配置了与隧道类型相同的]{style="font-family:宋体"}]{#struct_0_79555_16151_x2020163247}[源]{style="font-family:宋体"}[IP]{lang="IT"}[地址和成员]{style="font-family:
宋体"}[AC]{lang="IT"}[的]{style="font-family:宋体"}[IP]{lang="IT"}[地址后，]{style="font-family:宋体"}[才可以开启漫游组功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[开启漫游组功能后，]{style="font-family:宋体"}]{#struct_0_79555_16151_1619754346}[AC]{lang="IT"}[会使用]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="IT"}[地址]{style="font-family:宋体"}[与组内其他成员]{style="font-family:
宋体"}[AC]{lang="EN-US"}[建立]{style="font-family:宋体"}[IACTP]{lang="IT"}[隧道，并同步漫游表项信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_79555_16151_x1403201749}[漫游组功能后，]{style="font-family:
宋体"}[AC]{lang="IT"}[会断开同组内其他成员]{style="font-family:宋体"}[AC]{lang="EN-US"}[的]{style="font-family:宋体"}[IACTP]{lang="IT"}[隧道连接，并删除漫游表项信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_x754539982}

[[\# ]{lang="IT"}]{#struct_0_79555_16151_x1482480978}[开启漫游组功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_79555_16151_660429348}

[\[Sysname\] wlan mobility group floor1]{lang="IT"}

[\[]{lang="IT"}[Sysname-wlan-mg-floor1\] tunnel-type ipv4]{lang="IT"}

[\[Sysname-wlan-mg-floor1\] source ip 192.168.0.1]{lang="EN-US"}

[\[Sysname-wlan-mg-floor1\] member ip 192.168.0.2]{lang="EN-US"}

[\[Sysname-wlan-mg-floor1\] group enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_1874366863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[wlan mobility group]{lang="IT"}**]{#struct_0_79555_16151_x1404178230}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member]{lang="IT"}**]{#struct_0_79555_16151_1748894258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[source]{lang="IT"}**]{#struct_0_79555_16151_1250783334}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[tunnel-type]{lang="IT"}**]{#struct_0_79555_16151_x1901279518}
:::

::: {#1586550295 .myid}
[]{#_Toc404795180}[]{#struct_0_79555_16151_x40803917}[]{#_Toc374532797}

**漫游 \-- 漫游配置命令 \-- member**

------------------------------------------------------------------------

[**[member]{lang="IT"}**]{#struct_0_79555_16151_1693977070}[命令用来添加漫游组内]{style="font-family:宋体"}[的]{style="font-family:宋体"}[AC]{lang="IT"}[成员。]{style="font-family:宋体"}

[**[undo member]{lang="IT"}**]{#struct_0_79555_16151_x1913795547}[命令用来删除漫游组内的]{style="font-family:宋体"}[AC]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_1949653270}

[**[member ]{lang="IT"}**]{#struct_0_79555_16151_x990064910}[{ **ip** *ip-address \|* **ipv6** *ipv6-address* }]{lang="IT"}

[**[undo member ]{lang="IT"}**]{#struct_0_79555_16151_x1860962388}[\[ **ip** *ip-address \|* **ipv6** *ipv6-address* \]]{lang="IT"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_79555_16151_x183848351}

[]{#struct_0_79555_16151_x235036527}[]{#OLE_LINK35}[]{#OLE_LINK34}[[漫游组内不存在]{style="font-family:宋体"}[AC]{lang="EN-US"}]{#OLE_LINK33}[成员]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1081542533}

[[本地漫游组视图]{style="font-family:宋体"}]{#struct_0_79555_16151_1038365332}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1233400262}

[[network-admin]{lang="EN-US"}]{#struct_0_79555_16151_x1930378316}

[[mdc-admin]{lang="EN-US"}]{#struct_0_79555_16151_182810317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1287351915}

[**[ip ]{lang="IT"}**]{#struct_0_79555_16151_1435131507}*[ip-address]{lang="IT"}*[：漫游组内]{style="font-family:
宋体"}[AC]{lang="IT"}[成员的]{style="font-family:宋体"}[IPv4]{lang="IT"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="IT"}**]{#struct_0_79555_16151_1495703649}*[ ipv6-address]{lang="IT"}*[：漫游组内]{style="font-family:宋体"}[AC]{lang="IT"}[成员的]{style="font-family:宋体"}[IPv6]{lang="IT"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_1602615935}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[漫游组内]{style="font-family:宋体"}]{#struct_0_79555_16151_860711597}[的]{style="font-family:宋体"}[AC]{lang="IT"}[成员通过]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址标识，该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[AC]{lang="EN-US"}[成员建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，]{style="font-family:宋体"}[一个成员只能属于一个漫游组。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[删除漫游组成员时，如果不指定]{style="font-family:宋体"}]{#struct_0_79555_16151_562922655}[IP]{lang="IT"}[地址，则删除漫游组内所有成员。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[可以使用该命令]{style="font-family:宋体"}]{#struct_0_79555_16151_959461860}[添加]{style="font-family:宋体"}[IPv4]{lang="IT"}[和]{style="font-family:宋体"}[IP]{lang="IT"}[v6]{lang="IT"}[类型的成员地址，但是只有与隧道类型相同的成员地址才能]{style="font-family:宋体"}[生效。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[member]{lang="IT"}**]{#struct_0_79555_16151_x921120454}[命令和]{style="font-family:
宋体"}**[undo member]{lang="IT"}**[命令]{lang="EN-US" style="font-family:宋体"}[只能在漫游组处于关闭的情况下使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_x518717230}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_x290109609}[为漫游组添加一个]{style="font-family:宋体"}[AC]{lang="EN-US"}[成员。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_79555_16151_x1062728657}

[\[Sysname\] wlan mobility group abc]{lang="EN-US"}

[\[Sysname-wlan-mg-abc\] member ip 192.168.1.55]{lang="EN-US"}
:::

::: {#-773629 .myid}
[]{#_Toc404795181}[]{#struct_0_79555_16151_1701875189}

**漫游 \-- 漫游配置命令 \-- source**

------------------------------------------------------------------------

[**[source]{lang="IT"}**]{#struct_0_79555_16151_x1996396048}[命令用来[]{#OLE_LINK26}[]{#OLE_LINK25}[配置]{#OLE_LINK24}]{style="font-family:宋体"}[AC]{lang="EN-US"}[加入本地漫游组时建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo source]{lang="IT"}**]{#struct_0_79555_16151_512384093}[命令用来删除建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1383273624}

[**[source ]{lang="IT"}**]{#struct_0_79555_16151_x938348052}[{ **ip** *ip-address \|* **ipv6** *ipv6-address* }]{lang="IT"}

[**[undo source ]{lang="IT"}**]{#struct_0_79555_16151_x1782151409}[\[**ip** *\|* **ipv6**\]]{lang="IT"}

[[【]{style="font-family:黑体"}]{#struct_0_79555_16151_17954792}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[未配置]{style="font-family:宋体"}]{#struct_0_79555_16151_1507274617}[建立]{style="font-family:宋体"}[IACTP]{lang="IT"}[隧道的源]{style="font-family:宋体"}[IP]{lang="IT"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_1731917464}

[[本地漫游组视图]{style="font-family:宋体"}]{#struct_0_79555_16151_254719528}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x19670742}

[[network-admin]{lang="IT"}]{#struct_0_79555_16151_x1193239835}

[[mdc-admin]{lang="IT"}]{#struct_0_79555_16151_742134645}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_2043752648}

[**[ip ]{lang="IT"}**]{#struct_0_79555_16151_x849981948}*[ip-address]{lang="IT"}*[：]{style="font-family:宋体"}[AC]{lang="IT"}[加入漫游组时建立]{style="font-family:宋体"}[IACTP]{lang="IT"}[隧道的源]{style="font-family:宋体"}[IPv4]{lang="IT"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="IT"}**]{#struct_0_79555_16151_x787839414}*[ ipv6-address]{lang="IT"}*[：]{lang="EN-US" style="font-family:宋体"}[AC]{lang="IT"}[加入漫游组时建立]{lang="EN-US" style="font-family:宋体"}[IACTP]{lang="IT"}[隧道的源]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="IT"}[6]{lang="IT"}[地址。]{lang="EN-US" style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_260707633}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[AC]{lang="EN-US"}]{#struct_0_79555_16151_x932511589}[在加入漫游组后需要使用]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和同一漫游组内]{style="font-family:宋体"}[AC]{lang="EN-US"}[成员建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[只有与]{style="font-family:宋体"}]{#struct_0_79555_16151_x122786335}[漫游组隧道]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型相同的源地址才能生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除建立]{style="font-family:宋体"}]{#struct_0_79555_16151_771430472}[IACTP]{lang="EN-US"}[隧道的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址时，如果指定地址类型]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则删除指定类型的源]{style="font-family:宋体"}[IP]{lang="IT"}[地址。如果没有指定地址类型，则删除所有源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}**[source]{lang="IT"}**]{#struct_0_79555_16151_1345609731}[命令和]{style="font-family:
宋体"}**[undo source]{lang="IT"}**[命令]{lang="EN-US" style="font-family:宋体"}[只能在漫游组处于关闭的情况下使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_1750490372}

[[\# ]{lang="IT"}]{#struct_0_79555_16151_1523000459}[配置]{style="font-family:宋体"}[AC]{lang="EN-US"}[加入漫游组时建立]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="IT"}]{#struct_0_79555_16151_494023652}

[\[Sysname\] wlan mobility group abc]{lang="IT"}

[\[Sysname-wlan-mg-abc\] source ip 192.168.1.55]{lang="IT"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_1561424757}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}**[group enable]{lang="IT"}**]{#struct_0_79555_16151_x1494276688}

[[·[              ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}**[member]{lang="IT"}**]{#struct_0_79555_16151_1453612982}
:::

::: {#408673317 .myid}
[]{#_Toc404795182}[]{#struct_0_79555_16151_222444449}

**漫游 \-- 漫游配置命令 \-- tunnel-type**

------------------------------------------------------------------------

[**[tunnel-type]{lang="IT"}**]{#struct_0_79555_16151_x2007673488}[命令用来[]{#OLE_LINK23}[]{#OLE_LINK22}[配置漫游组]{#OLE_LINK21}]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型。]{style="font-family:宋体"}

[**[undo tunnel-type]{lang="IT"}**]{#struct_0_79555_16151_1886271627}[命令用来删除配置的漫游组隧道]{style="font-family:宋体"}[IP]{lang="IT" style="font-family:Consolas"}[地址类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1411322803}

[**[tunnel-type ]{lang="IT"}**]{#struct_0_79555_16151_x1316336211}[{ **ipv4 \| ipv6** }]{lang="IT"}

[**[undo tunnel-type ]{lang="IT"}**]{#struct_0_79555_16151_x678793148}[{ **ipv4 \| ipv6** }]{lang="IT"}

[[【]{style="font-family:黑体"}]{#struct_0_79555_16151_1639544640}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[]{#struct_0_79555_16151_x220474210}[]{#OLE_LINK39}[]{#OLE_LINK38}[]{#OLE_LINK37}[[未配置漫游组]{style="font-family:宋体"}[IACTP]{lang="EN-US"}]{#OLE_LINK36}[隧道]{style="font-family:宋体"}[IP]{lang="IT"}[地址类型]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_610152171}

[[本地漫游组视图]{style="font-family:宋体"}]{#struct_0_79555_16151_37845562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1392291666}

[[network-admin]{lang="EN-US"}]{#struct_0_79555_16151_884365367}

[[mdc-admin]{lang="EN-US"}]{#struct_0_79555_16151_x1912739703}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_1638500523}

[**[ipv4]{lang="IT"}**]{#struct_0_79555_16151_x1271524231}[:]{lang="EN-US" style="font-family:Consolas"}[指定漫游组使]{style="font-family:宋体"}[用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[类型的隧道]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="IT"}**]{#struct_0_79555_16151_1136174576}[:]{lang="IT" style="font-family:Consolas"}[指定漫游组使用]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[类型的隧道]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_1836401299}

[**[tunnel-type]{lang="IT"}**]{#struct_0_79555_16151_x571105277}[命令和]{style="font-family:宋体"}**[undo tunnel-type]{lang="IT"}**[命令]{style="font-family:宋体"}[只能在漫游组未使能的情况下使用并且]{style="font-family:宋体"}[不能同时配置两种隧道]{style="font-family:宋体"}[IP]{lang="IT" style="font-family:Consolas"}[地址]{style="font-family:宋体"}[类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_179003337}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_729742050}[配置漫游组]{style="font-family:宋体"}[IACTP]{lang="EN-US"}[隧道]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_79555_16151_1655193155}

[\[Sysname\] wlan mobility group aaa]{lang="EN-US"}

[\[Sysname-wlan-mg-aaa\] tunnel-type ipv6]{lang="EN-US"}
:::

::: {#-327349981 .myid}
[]{#_Toc404795183}[]{#struct_0_79555_16151_x867580125}[]{#_Toc374532794}

**漫游 \-- 漫游配置命令 \-- wlan mobility group**

------------------------------------------------------------------------

[**[wlan mobility group]{lang="IT"}**]{#struct_0_79555_16151_x1630789341}[命令用来创建本地漫游组。]{style="font-family:宋体"}

[**[undo wlan mobility group]{lang="IT"}**]{#struct_0_79555_16151_x1786558151}[命令用来删除本地漫游组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_79555_16151_x572023385}

[**[wlan mobility group ]{lang="IT"}**]{#struct_0_79555_16151_843609645}*[group-name]{lang="IT"}*

[**[undo wlan mobility group ]{lang="IT"}**]{#struct_0_79555_16151_577652083}*[group-name]{lang="IT"}*

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_79555_16151_x1459936152}

[[不存在本地漫游组。]{style="font-family:宋体"}]{#struct_0_79555_16151_522402043}

[[【视图】]{style="font-family:黑体"}]{#struct_0_79555_16151_330900189}

[[系统视图]{style="font-family:宋体"}]{#struct_0_79555_16151_1247580170}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_79555_16151_x2021440722}

[[network-admin]{lang="IT"}]{#struct_0_79555_16151_522495789}

[[mdc-admin]{lang="IT"}]{#struct_0_79555_16151_x407851725}

[[【参数】]{style="font-family:黑体"}]{#struct_0_79555_16151_6055555}

[*[group-name]{lang="IT"}*]{#struct_0_79555_16151_x885011101}[：]{style="font-family:宋体"}[本地漫游组名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="IT"}[～]{style="font-family:宋体"}[15]{lang="IT"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_79555_16151_x74532703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一本地漫游组内的成员的本地漫游组名应该保持一致。]{style="font-family:宋体"}]{#struct_0_79555_16151_x1195521534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个设备只允许创建一个本地漫游组。]{style="font-family:宋体"}]{#struct_0_79555_16151_1175438514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地漫游组只在水平组网中的]{style="font-family:宋体"}]{#struct_0_79555_16151_229864484}[AC]{lang="EN-US"}[上生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_79555_16151_x175366434}

[[\# ]{lang="EN-US"}]{#struct_0_79555_16151_975355331}[创建本地漫游组。]{style="font-family:宋体"}

[[\<Sysname\> sysname-view]{lang="EN-US"}]{#struct_0_79555_16151_x1723996989}

[\[Sysname\] wlan mobility group aaa]{lang="EN-US"}

[\[Sysname-wlan-mg-aaa\]]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
