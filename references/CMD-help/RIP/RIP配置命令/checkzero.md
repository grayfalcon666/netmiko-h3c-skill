::: {#320779778 .myid}
[]{#_Toc216497575}[]{#_Toc137543097}[]{#_Toc33866010}[]{#_Toc33866008}[]{#_Toc404787689}[]{#struct_0_17903_10256_x750618855}[]{#_Toc313007758}[]{#_Toc286220949}[]{#_Toc286220951}[]{#_Toc286220952}[]{#_Toc286220953}[]{#_Toc286220954}[]{#_Toc286220955}[]{#_Toc286220956}[]{#_Toc286220957}[]{#_Toc286220958}[]{#_Toc286220959}[]{#_Toc286220960}[]{#_Toc286220961}[]{#_Toc286220962}[]{#_Toc286220963}[]{#_Toc286220964}[]{#_Toc286220965}[]{#_Toc286220967}[]{#_Toc135620324}[]{#_Toc135620327}[]{#_Toc135620328}[]{#_Toc135620329}[]{#_Toc135620330}[]{#_Toc135620331}[]{#_Toc135620332}[]{#_Toc135620333}[]{#_Toc135620334}[]{#_Toc135620335}[]{#_Toc135620336}[]{#_Toc135620337}[]{#_Toc135620338}[]{#_Toc135620339}[]{#_Toc135620340}[]{#_Toc135620341}[]{#_Toc135620342}[]{#_Toc135620343}[]{#_Toc135620345}[]{#_Toc135620346}[]{#_Toc135620347}[]{#_Toc135620348}[]{#_Toc135620349}[]{#_Toc135620350}[]{#_Toc135620351}[]{#_Toc135620352}[]{#_Toc135620354}[]{#_Toc135620355}[]{#_Toc135620356}[]{#_Toc135620357}[]{#_Toc135620358}[]{#_Toc135620359}[]{#_Hlt5077351}[]{#_Toc135620360}[]{#_Toc135620361}[]{#_Toc135620362}[]{#_Toc135620363}[]{#_Toc135620364}[]{#_Toc135620365}[]{#_Toc135620366}[]{#_Toc135620367}[]{#_Toc135620368}[]{#_Toc135620369}[]{#_Toc286220969}[]{#_Toc286220970}[]{#_Toc286220971}[]{#_Toc286220972}[]{#_Toc286220973}[]{#_Toc286220974}[]{#_Toc286220975}[]{#_Toc286220976}[]{#_Toc286220977}[]{#_Toc286220978}[]{#_Toc286220979}[]{#_Toc286220980}[]{#_Toc286220981}[]{#_Toc286220982}[]{#_Toc286220983}[]{#_Toc286220984}[]{#_Toc286220985}[]{#_Toc286220987}[]{#_Toc286220990}[]{#_Toc286220991}[]{#_Toc286220992}[]{#_Toc286220993}[]{#_Toc286220994}[]{#_Toc286220995}[]{#_Toc286220996}[]{#_Toc286220997}[]{#_Toc286220998}[]{#_Toc286220999}[]{#_Toc286221000}[]{#_Toc286221001}[]{#_Toc286221002}[]{#_Toc286221003}[]{#_Toc286221004}[]{#_Toc286221005}[]{#_Toc286221006}[]{#_Toc286221007}[]{#_Toc286221008}[]{#_Toc286221009}[]{#_Toc286221011}[]{#_Toc185153148}[]{#_Toc185153317}[]{#_Toc185153358}[]{#_Toc185153149}[]{#_Toc185153318}[]{#_Toc185153359}

**RIP \-- RIP配置命令 \-- checkzero**

------------------------------------------------------------------------

[**[checkzero]{lang="EN-US"}**]{#struct_0_17903_10256_x1623418969}[命令用来使能]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[报文的零域检查功能。]{style="font-family:宋体"}

[**[undo checkzero]{lang="EN-US"}**]{#struct_0_17903_10256_x466106149}[命令用来关闭零域检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_657972319}

[**[checkzero]{lang="EN-US"}**]{#struct_0_17903_10256_1993116430}

[**[undo checkzero]{lang="EN-US"}**]{#struct_0_17903_10256_x2010234429}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_2109396451}

[[RIP-1]{lang="EN-US"}]{#struct_0_17903_10256_1804599287}[报文的零域检查功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1476956101}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1233663217}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_324484899}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_436461243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_712779976}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_126628610}

[[使能零域检查功能后，零域中包含非零位的]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}]{#struct_0_17903_10256_779816880}[报文将被拒绝处理。如果用户能确保所有报文都是可信任的，则可以不进行该项检查，以节省]{style="font-family:宋体"}[CPU]{lang="EN-US"}[处理时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_938187311}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1666720102}[关闭进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程对]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[报文的零域检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1476890565}

[\[Sysname\] rip]{lang="EN-US"}

[\[Sysname-rip-1\] undo checkzero]{lang="EN-US"}
:::

::: {#-1740075607 .myid}
[]{#_Toc404787690}[]{#struct_0_17903_10256_1471179235}[]{#_Toc313007759}

**RIP \-- RIP配置命令 \-- default cost**

------------------------------------------------------------------------

[**[default cost]{lang="EN-US"}**]{#struct_0_17903_10256_2004884340}[命令用来配置引入路由的缺省度量值。]{style="font-family:宋体"}

[**[undo default cost]{lang="EN-US"}**]{#struct_0_17903_10256_x40245039}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2129464983}

[**[default cost ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_17903_10256_x144239261}

[**[undo default cost]{lang="EN-US"}**]{#struct_0_17903_10256_1916348953}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1288525283}

[[引入路由的缺省度量值为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_17903_10256_x1476825029}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_749203625}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_539895904}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1279864107}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1936393835}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1510700580}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1661221967}

[*[value]{lang="EN-US"}*]{#struct_0_17903_10256_x263583819}[：引入路由的缺省度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1862106871}

[[当使用]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1476759493}[命令从其它协议引入路由时，如果不指定具体的度量值，则引入路由的度量值为]{style="font-family:宋体"}**[default cost]{lang="EN-US"}**[所指定的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_171368926}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1568525031}[配置从其它路由协议引入路由的缺省度量值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1415138008}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] default cost 3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1967404493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_17903_10256_2041456059}
:::

::: {#1324881264 .myid}
[]{#_Toc404787691}[]{#struct_0_17903_10256_469335092}[]{#_Toc313007760}

**RIP \-- RIP配置命令 \-- default-route**

------------------------------------------------------------------------

[**[default-route]{lang="EN-US"}**]{#struct_0_17903_10256_75973512}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程下的所有接口以指定度量值向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布一条缺省路由。]{style="font-family:宋体"}

[**[undo default-route]{lang="EN-US"}**]{#struct_0_17903_10256_1371591566}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1216167997}

[**[default-route]{lang="EN-US"}**[ { **only** \| **originate** } \[ **cost** *cost* \| **route-policy** *route-policy-name* \] \*]{lang="EN-US"}]{#struct_0_17903_10256_x1476693957}

[**[undo default-route]{lang="EN-US"}**]{#struct_0_17903_10256_723222705}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1005690245}

[[不向]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1136927652}[邻居发送缺省路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1670466008}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1294126406}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1342521796}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x809322537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x2134702130}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_377988909}

[**[only]{lang="EN-US"}**]{#struct_0_17903_10256_x1477676997}[：]{style="font-family:宋体"}[配置只发送缺省路由，不发送普通路由。]{style="font-family:宋体"}

[**[originate]{lang="EN-US"}**]{#struct_0_17903_10256_x2095263282}[：]{style="font-family:宋体"}[配置既发送普通路由，又发送缺省路由。]{style="font-family:宋体"}

[*[cost]{lang="EN-US"}*]{#struct_0_17903_10256_1510524210}[：]{style="font-family:宋体"}[缺省路由的度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_17903_10256_191197851}[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有当前路由器的路由表中有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略时，才发送缺省路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2084120852}

[[配置了发布缺省路由的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_2101126511}[路由器不接收来自]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居的缺省路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1907359683}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1330116707}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[的所有接口向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布一条度量值为]{style="font-family:宋体"}[2]{lang="EN-US"}[的缺省路由，而且只发送缺省路由，不发送普通路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_145697734}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] default-route only cost 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1513747377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rip default-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1477611461}
:::

::: {#-772695867 .myid}
[]{#_Toc404787692}[]{#struct_0_17903_10256_1846930137}

**RIP \-- RIP配置命令 \-- display rip**

------------------------------------------------------------------------

[**[display rip]{lang="EN-US"}**]{#struct_0_17903_10256_x1765391698}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的当前运行状态及配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1034079123}

[**[display rip]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17903_10256_962676058}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1634446946}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_2048077574}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1090515029}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1388005927}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_x1477152708}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1333191779}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_763076708}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_461085942}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_1495604984}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，则显示所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的当前运行状态及配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1490801953}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_115945389}[显示所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的当前运行状态及配置信息。]{style="font-family:宋体"}

[]{#_Toc216497576}[]{#_Toc137543098}[]{#_Toc94930673}[]{#_Toc93984708}[[\<Sysname\> display rip]{lang="EN-US"}]{#struct_0_17903_10256_x1477087172}

[  Public VPN-instance name:]{lang="EN-US"}

[    RIP process: 1]{lang="EN-US"}

[       RIP version: 1]{lang="EN-US"}

[       Preference: 100]{lang="EN-US"}

[           Routing policy: abc]{lang="EN-US"}

[       Fast-reroute:]{lang="EN-US"}

[           Routing policy: frr]{lang="EN-US"}

[       Checkzero: Enabled]{lang="EN-US"}

[       Default cost: 0]{lang="EN-US"}

[       Summary: Enabled]{lang="EN-US"}

[       Host routes: Enabled]{lang="EN-US"}

[       Maximum number of load balanced routes: 8]{lang="EN-US"}

[       Update time   :   30 secs  Timeout time         :  180 secs]{lang="EN-US"}

[       Suppress time :  120 secs  Garbage-collect time :  120 secs]{lang="EN-US"}

[       Update output delay:   20(ms)  Output count:    3]{lang="EN-US"}

[       Silent interfaces: None]{lang="EN-US"}

[       Default routes: Originate  Default routes cost: 3]{lang="EN-US"}

[       Verify-source: Enabled]{lang="EN-US"}

[       Networks:]{lang="EN-US"}

[           1.0.0.0]{lang="EN-US"}

[       Configured peers:]{lang="EN-US"}

[           197.168.6.2]{lang="EN-US"}

[       Triggered updates sent: 0]{lang="EN-US"}

[       Number of routes changes: 1]{lang="EN-US"}

[       Number of replies to queries: 0]{lang="EN-US"}

[]{#struct_0_17903_10256_362299776}[]{#_Toc99255016}[[表1-1 ]{lang="EN-US"}[display rip]{lang="EN-US"}]{#_Toc81210244}[命令显示信息]{style="font-family:黑体"}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_1048860866}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1477021636}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_1346755687}

[[Public VPN-instance name/Private VPN-instance name]{lang="EN-US"}]{#struct_0_17903_10256_893379996}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x113746216}[进程运行在公网实例下]{style="font-family:宋体"}[/RIP]{lang="EN-US"}[进程应用于指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[RIP process]{lang="EN-US"}]{#struct_0_17903_10256_x1923040265}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1381693706}[进程号]{style="font-family:宋体"}

[[RIP version ]{lang="EN-US"}]{#struct_0_17903_10256_1263403669}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1476956100}[版本]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_17903_10256_1495220138}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_2004375788}[路由优先级]{style="font-family:宋体"}

[[Fast-reroute]{lang="EN-US"}]{#struct_0_17903_10256_x838836779}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1890453026}[快速重路由]{style="font-family:宋体"}

[[Routing policy]{lang="EN-US"}]{#struct_0_17903_10256_1722970964}

[[路由策略]{style="font-family:宋体"}]{#struct_0_17903_10256_x1476890564}

[[Checkzero]{lang="EN-US"}]{#struct_0_17903_10256_x94904706}

[[是否使能对]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}]{#struct_0_17903_10256_595970401}[报文的零域进行检查的功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_17903_10256_342508105}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_x1380212748}[表示关闭]{lang="EN-US" style="font-family:宋体"}

[[Default cost]{lang="EN-US"}]{#struct_0_17903_10256_x1476825028}

[[引入路由的缺省度量值]{style="font-family:宋体"}]{#struct_0_17903_10256_x1979679730}

[[Summary]{lang="EN-US"}]{#struct_0_17903_10256_579266732}

[[路由聚合功能是否使能]{style="font-family:宋体"}]{#struct_0_17903_10256_x213664505}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17903_10256_x1880447669}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_x1476759492}[表示关闭]{lang="EN-US" style="font-family:宋体"}

[[Host routes]{lang="EN-US"}]{#struct_0_17903_10256_x1394715015}

[[是否允许接收主机路由]{style="font-family:宋体"}]{#struct_0_17903_10256_968199586}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17903_10256_1576459631}[表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_x1476693956}[表示不允许]{lang="EN-US" style="font-family:宋体"}

[[Maximum number of load balanced routes]{lang="EN-US"}]{#struct_0_17903_10256_x842861236}

[[等价路由的最大数目]{style="font-family:宋体"}]{#struct_0_17903_10256_x1541634450}

[[Update time]{lang="EN-US"}]{#struct_0_17903_10256_1473893090}

[[Update]{lang="EN-US"}]{#struct_0_17903_10256_x907564895}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Timeout time]{lang="EN-US"}]{#struct_0_17903_10256_x1477676996}

[[Timeout]{lang="EN-US"}]{#struct_0_17903_10256_633620073}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Suppress time]{lang="EN-US"}]{#struct_0_17903_10256_114554707}

[[Suppress]{lang="EN-US"}]{#struct_0_17903_10256_x771621849}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Update output delay]{lang="EN-US"}]{#struct_0_17903_10256_x1477611460}

[[接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_280846196}[报文的时间间隔]{style="font-family:宋体"}

[[Output count]{lang="EN-US"}]{#struct_0_17903_10256_x651457402}

[[接口一次发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x2130853301}[报文的最大个数]{style="font-family:宋体"}

[[Garbage-collect time]{lang="EN-US"}]{#struct_0_17903_10256_88931236}

[[Garbage-Collect]{lang="EN-US"}]{#struct_0_17903_10256_467790823}[定时器的值，单位为秒]{style="font-family:宋体"}

[[Silent interfaces]{lang="EN-US"}]{#struct_0_17903_10256_328956389}

[[工作在抑制状态的接口（这些接口不发送周期更新报文）]{style="font-family:宋体"}]{#struct_0_17903_10256_x1450509645}

[[Default routes]{lang="EN-US"}]{#struct_0_17903_10256_88996772}

[[是否向]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x368132526}[邻居发布一条缺省路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Only]{lang="EN-US"}]{#struct_0_17903_10256_x1912534539}[：表示只发布缺省路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Originate]{lang="EN-US"}]{#struct_0_17903_10256_89062308}[：表示同时发布缺省路由和普通路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_x1665002248}[：表示不发布缺省路由]{lang="EN-US" style="font-family:宋体"}

[[Default routes cost]{lang="EN-US"}]{#struct_0_17903_10256_284203607}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_460684218}[进程下发布缺省路由的度量值]{style="font-family:宋体"}

[[Verify-source]{lang="EN-US"}]{#struct_0_17903_10256_89127844}

[[是否使能对接收到的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x2100836198}[路由更新报文进行源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查的功能]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enable]{lang="EN-US"}]{#struct_0_17903_10256_x111781392}[表示已使能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_89193380}[表示关闭]{lang="EN-US" style="font-family:宋体"}

[[Networks]{lang="EN-US"}]{#struct_0_17903_10256_x1388340470}

[[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1461741960}[的网段地址]{style="font-family:宋体"}

[[Configured peers]{lang="EN-US"}]{#struct_0_17903_10256_89258916}

[[配置的邻居]{style="font-family:宋体"}]{#struct_0_17903_10256_x320431729}

[[Triggered updates sent]{lang="EN-US"}]{#struct_0_17903_10256_x1564969483}

[[发送的触发更新报文数]{style="font-family:宋体"}]{#struct_0_17903_10256_89324452}

[[Number of routes changes]{lang="EN-US"}]{#struct_0_17903_10256_x27082980}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x549525104}[进程改变路由数据库的统计数据]{style="font-family:宋体"}

[[Number of replies to queries]{lang="EN-US"}]{#struct_0_17903_10256_89389988}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x924931322}[请求的响应报文数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1979703623 .myid}
[]{#_Toc404787693}[]{#struct_0_17903_10256_389903958}

**RIP \-- RIP配置命令 \-- display rip database**

------------------------------------------------------------------------

[**[display rip]{lang="EN-US"}**[ **database**]{lang="EN-US"}]{#struct_0_17903_10256_x193841472}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[数据库的激活路由，这些路由以常规]{style="font-family:宋体"}[RIP]{lang="EN-US"}[更新报文的形式发送。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2113228277}

[**[display rip]{lang="EN-US"}**[ *process-id* **database** \[ *ip-address* { *mask-length* \| *mask* } \]]{lang="EN-US"}]{#struct_0_17903_10256_x1501486530}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2108375540}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1415457176}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_88406948}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1056742796}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_x1030873965}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x756341922}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_x1568899670}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1222245132}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_x1052925052}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_17903_10256_x331027508}[：显示指定目的地址和掩码的激活路由信息。]{style="font-family:宋体"}[如果未指定本参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的所有激活路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1796176930}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_88472484}[显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[数据库的所有激活路由。]{style="font-family:宋体"}

[[\<Sysname\> display rip 100 database]{lang="EN-US"}]{#struct_0_17903_10256_x318711364}

[   1.0.0.0/8, auto-summary]{lang="EN-US"}

[       1.1.1.0/24, cost 16, interface summary]{lang="EN-US"}

[       1.1.1.0/24, cost 0, nexthop 1.1.1.1, RIP-interface]{lang="EN-US"}

[       1.1.2.0/24, cost 0, imported]{lang="EN-US"}

[   2.0.0.0/8, auto-summary]{lang="EN-US"}

[   2.0.0.0/8, cost 1, nexthop 1.1.1.2]{lang="EN-US"}

[]{#_Toc94753847}[]{#_Toc94671173}[]{#_Toc73952254}[]{#_Toc68319386}[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1028218403}[显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[数据库中指定地址和掩码为]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[的激活路由。]{style="font-family:宋体"}

[[\<Sysname\> display rip 100 database 1.1.1.0 24]{lang="EN-US"}]{#struct_0_17903_10256_163371258}

[   1.1.1.0/24, cost 16, interface summary]{lang="EN-US"}

[   1.1.1.0/24, cost 0, nexthop 1.1.1.1, RIP-interface]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display rip database]{lang="EN-US"}]{#struct_0_17903_10256_687603191}[命令显示]{style="font-family:黑体"}[信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1040382703}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x708271384}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_590701906}

[[cost]{lang="EN-US"}]{#struct_0_17903_10256_88931237}

[[度量值]{style="font-family:宋体"}]{#struct_0_17903_10256_x1870861337}

[[auto-summary]{lang="EN-US"}]{#struct_0_17903_10256_1892105670}

[[表示该条路由是]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1004620190}[的自动聚合路由]{style="font-family:宋体"}

[[interface summary]{lang="EN-US"}]{#struct_0_17903_10256_x103444836}

[[表示该条路由是]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1083753423}[的接口聚合路由]{style="font-family:宋体"}

[[nexthop]{lang="EN-US"}]{#struct_0_17903_10256_88996773}

[[下一跳地址]{style="font-family:宋体"}]{#struct_0_17903_10256_1588182610}

[[RIP-interface]{lang="EN-US"}]{#struct_0_17903_10256_581537307}

[[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1325820294}[协议的接口的直连路由]{style="font-family:宋体"}

[[imported]{lang="EN-US"}]{#struct_0_17903_10256_1246664741}

[[表示该条路由是从其它路由协议引入的]{style="font-family:宋体"}]{#struct_0_17903_10256_706179364}

[ ]{lang="EN-US"}

::::: {#323263383 .myid}
[]{#_Toc404787694}[]{#struct_0_17903_10256_1757281787}[]{#_Toc375235975}

**RIP \-- RIP配置命令 \-- display rip graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_x759123793}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x580807637}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display rip graceful-restart]{lang="EN-US"}**]{#struct_0_17903_10256_x37117119}[命令用来显示]{style="font-family:
宋体"}[RIP]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x430535334}

[**[display rip]{lang="EN-US"}**[ \[ *process-id* \] **graceful-restart**]{lang="EN-US"}]{#struct_0_17903_10256_1380883308}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1756954107}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_358895997}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_568999332}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x937496371}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_x1515325086}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1508413401}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_1756888571}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x458831641}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_1722580590}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，则显示所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_393294659}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1435312709}[显示]{style="font-family:宋体"}[RIP 1]{lang="EN-US"}[进程的]{style="font-family:宋体"}[GR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 graceful-restart]{lang="EN-US"}]{#struct_0_17903_10256_1757085179}

[ RIP process: 1]{lang="EN-US"}

[ Graceful Restart capability     : Enabled]{lang="EN-US"}

[ Current GR state                : Normal]{lang="EN-US"}

[ Graceful Restart period         : 60  seconds]{lang="EN-US"}

[ Graceful Restart remaining time : 0   seconds]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display rip graceful-restart]{lang="EN-US"}]{#struct_0_17903_10256_x1938104816}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x938664825}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1316328768}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_x493608635}

[[Graceful Restart capability]{lang="EN-US"}]{#struct_0_17903_10256_x190152308}

[[GR]{lang="EN-US"}]{#struct_0_17903_10256_1757019643}[使能状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17903_10256_1911969105}[：]{lang="EN-US" style="font-family:宋体"}[使能了]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_1407857723}[：]{lang="EN-US" style="font-family:宋体"}[关闭了]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}[能力]{lang="EN-US" style="font-family:宋体"}

[[Current GR state]{lang="EN-US"}]{#struct_0_17903_10256_1169260725}

[[当前]{style="font-family:宋体"}[GR]{lang="EN-US"}]{#struct_0_17903_10256_1757740539}[所处状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Under GR]{lang="EN-US"}]{#struct_0_17903_10256_x1968167764}[：进程正在]{lang="EN-US" style="font-family:宋体"}[GR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Normal]{lang="EN-US"}]{#struct_0_17903_10256_1214310900}[：普通状态]{lang="EN-US" style="font-family:宋体"}

[[Graceful Restart period]{lang="EN-US"}]{#struct_0_17903_10256_1958610248}

[[GR]{lang="EN-US"}]{#struct_0_17903_10256_1757675003}[重启间隔时间]{style="font-family:宋体"}

[[Graceful Restart remaining time]{lang="EN-US"}]{#struct_0_17903_10256_366534087}

[[GR]{lang="EN-US"}]{#struct_0_17903_10256_x2024912155}[结束剩余时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1232980620 .myid}
[]{#_Toc404787695}[]{#struct_0_17903_10256_89062309}[]{#_Toc216497577}[]{#_Toc137543099}[]{#_Toc97787989}

**RIP \-- RIP配置命令 \-- display rip interface**

------------------------------------------------------------------------

[**[display rip interface]{lang="EN-US"}**]{#struct_0_17903_10256_673649912}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_619521772}

[**[display rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_1659481983}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1610633223}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1395430377}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1982375898}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1581096561}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_55122614}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_89127845}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_237815962}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1026625200}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_756864461}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17903_10256_697830284}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的所有接口信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1048551}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1615832656}[显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的接口信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 interface]{lang="EN-US"}]{#struct_0_17903_10256_89193381}

[ Interface: GigabitEthernet1/0/2]{lang="EN-US"}

[    Address/Mask: 1.1.1.1/24          Version: RIPv1]{lang="EN-US"}

[    MetricIn: 0                       MetricIn route policy: Not designated]{lang="EN-US"}

[    MetricOut: 1                      MetricOut route policy: Not designated]{lang="EN-US"}

[    Split-horizon/Poison-reverse: On/Off  Input/Output: On/On]{lang="EN-US"}

[    Default route: Off]{lang="EN-US"}

[    Update output delay:  20(ms)      Output count: 3]{lang="EN-US"}

[    Current number of packets/Maximum number of packets: 0/2000]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display rip interface]{lang="EN-US"}]{#struct_0_17903_10256_567974666}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1042859167}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_485351501}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_986892585}

[[Interface]{lang="EN-US"}]{#struct_0_17903_10256_x1502823991}

[[运行]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1374890132}[协议的接口的名称]{style="font-family:宋体"}

[[Address/Mask]{lang="EN-US"}]{#struct_0_17903_10256_x1883425792}

[[运行]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_89258917}[协议的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[/]{lang="EN-US"}[掩码]{style="font-family:宋体"}

[[Version]{lang="EN-US"}]{#struct_0_17903_10256_1635883407}

[[接口上运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_542345389}[协议的版本]{style="font-family:宋体"}

[[MetricIn]{lang="EN-US"}]{#struct_0_17903_10256_x1986428632}

[[接收路由的附加度量值]{style="font-family:宋体"}]{#struct_0_17903_10256_1732378458}

[[MetricIn route policy]{lang="EN-US"}]{#struct_0_17903_10256_x320226792}

[[接收路由的附加度量值应用的路由策略，取值为]{style="font-family:宋体"}[Not designated]{lang="EN-US"}]{#struct_0_17903_10256_89324453}[表示没有对接收路由的附加度量值使用路由策略，如果对接收路由的附加度量值使用了路由策略，取值为使用的路由策略名称]{style="font-family:宋体"}

[[MetricOut]{lang="EN-US"}]{#struct_0_17903_10256_x1983398116}

[[发送路由的附加度量值]{style="font-family:宋体"}]{#struct_0_17903_10256_1846660525}

[[MetricOut route policy]{lang="EN-US"}]{#struct_0_17903_10256_x1014152302}

[[发送路由的附加度量值应用的路由策略，取值为]{style="font-family:宋体"}[Not designated]{lang="EN-US"}]{#struct_0_17903_10256_428540933}[表示没有对发送路由的附加度量值使用路由策略，如果对发送路由的附加度量值使用了路由策略，取值为使用的路由策略名称]{style="font-family:宋体"}

[[Split-horizon]{lang="EN-US"}]{#struct_0_17903_10256_89389989}

[[是否使能了水平分割（]{style="font-family:宋体"}[On]{lang="EN-US"}]{#struct_0_17903_10256_1413720838}[表示使能，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示关闭）]{style="font-family:宋体"}

[[Poison-reverse]{lang="EN-US"}]{#struct_0_17903_10256_x8321849}

[[是否使能了毒性逆转（]{style="font-family:宋体"}[On]{lang="EN-US"}]{#struct_0_17903_10256_x1159057049}[表示使能，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示关闭）]{style="font-family:宋体"}

[[Input/Output]{lang="EN-US"}]{#struct_0_17903_10256_x1435096414}

[[是否允许接口接收（]{style="font-family:宋体"}[Input]{lang="EN-US"}]{#struct_0_17903_10256_727017859}[）]{style="font-family:宋体"}[/]{lang="EN-US"}[发送（]{style="font-family:宋体"}[Output]{lang="EN-US"}[）]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文（]{style="font-family:宋体"}[On]{lang="EN-US"}[表示允许，]{style="font-family:宋体"}[Off]{lang="EN-US"}[表示不允许）]{style="font-family:宋体"}

[[Default route]{lang="EN-US"}]{#struct_0_17903_10256_88406949}

[[是否允许向]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1281909364}[邻居发送缺省路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Only]{lang="EN-US"}]{#struct_0_17903_10256_x1228323312}[：表示只发布缺省路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Originate]{lang="EN-US"}]{#struct_0_17903_10256_x384260358}[：表示同时发布缺省路由和普通路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No-originate]{lang="EN-US"}]{#struct_0_17903_10256_x143047613}[：表示]{lang="EN-US" style="font-family:宋体"}[只]{style="font-family:宋体"}[发布]{lang="EN-US" style="font-family:宋体"}[普通]{style="font-family:宋体"}[路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Off]{lang="EN-US"}]{#struct_0_17903_10256_88472485}[：表示不发布缺省路由]{lang="EN-US" style="font-family:宋体"}

[[Default route cost]{lang="EN-US"}]{#struct_0_17903_10256_1637603772}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_878676334}[接口下配置发布缺省路由的]{style="font-family:宋体"}[度量]{style="font-family:宋体"}[值]{style="font-family:宋体"}

[[Update output delay]{lang="EN-US"}]{#struct_0_17903_10256_x307226882}

[[接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x307161346}[报文的时间间隔]{style="font-family:宋体"}

[[Output count]{lang="EN-US"}]{#struct_0_17903_10256_701719926}

[[接口一次发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x427418693}[报文的最大个数]{style="font-family:宋体"}

[[Current number of packets /Maximum number of packets]{lang="EN-US"}]{#struct_0_17903_10256_x2144854952}

[[显示当前接口待发送的报文数量和最多可以发送的报文数量]{style="font-family:宋体"}]{#struct_0_17903_10256_x997732580}

[ ]{lang="EN-US"}

::: {#633263808 .myid}
[]{#_Toc404787696}[]{#struct_0_17903_10256_1757281788}

**RIP \-- RIP配置命令 \-- display rip neighbor**

------------------------------------------------------------------------

[**[display rip neighbor]{lang="EN-US"}**]{#struct_0_17903_10256_x759582545}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的邻居信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1756954108}

[**[display rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ neighbor ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_358830461}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x204586759}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x580658562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1561288619}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x730832159}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_1756888572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x458766105}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_164574986}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1342528737}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_1113057290}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17903_10256_1757085180}[：接口类型和编号。如果未指定本参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的所有邻居信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1937646079}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x757019656}[显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的邻居信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 neighbor]{lang="EN-US"}]{#struct_0_17903_10256_1757019644}

[ Neighbor address: 197.168.2.3 (TRIP)]{lang="EN-US"}

[     Interface  : Serial3/0/3]{lang="EN-US"}

[     Version    : RIPv2     Last update: 00h00m02s]{lang="EN-US"}

[     Relay nbr  : N/A       BFD session: N/A]{lang="EN-US"}

[     Bad packets: 0         Bad routes : 0]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display rip neighbor]{lang="EN-US"}]{#struct_0_17903_10256_1912427857}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x917734143}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1779205833}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_199343347}

[[Neighbor address]{lang="EN-US"}]{#struct_0_17903_10256_1757740540}

[[邻居地址]{style="font-family:宋体"}]{#struct_0_17903_10256_x1968757589}

[[Interface]{lang="EN-US"}]{#struct_0_17903_10256_x1021373900}

[[出接口]{style="font-family:宋体"}]{#struct_0_17903_10256_1757675004}

[[Version]{lang="EN-US"}]{#struct_0_17903_10256_366206407}

[[收到邻居]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_782572976}[报文的版本]{style="font-family:宋体"}

[[Last update]{lang="EN-US"}]{#struct_0_17903_10256_1757216249}

[[上次收到邻居更新报文距离现在时间]{style="font-family:宋体"}]{#struct_0_17903_10256_1561553332}

[[Relay nbr]{lang="EN-US"}]{#struct_0_17903_10256_834121978}

[[是否是非直连邻居]{style="font-family:宋体"}]{#struct_0_17903_10256_x319785188}

[[BFD session]{lang="EN-US"}]{#struct_0_17903_10256_1757150713}

[[BFD]{lang="EN-US"}]{#struct_0_17903_10256_1939416304}[会话类型]{style="font-family:宋体"}

[[Bad packets]{lang="EN-US"}]{#struct_0_17903_10256_x169530527}

[[接口收到的错误报文数目]{style="font-family:宋体"}]{#struct_0_17903_10256_1757347321}

[[Bad routes]{lang="EN-US"}]{#struct_0_17903_10256_786298100}

[[接口收到的错误路由数目]{style="font-family:宋体"}]{#struct_0_17903_10256_2120134602}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_x217361262}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_1757281785}[邻居]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1747235826 .myid}
[]{#_Toc404787697}[]{#struct_0_17903_10256_x759254865}[]{#_Toc375235979}

**RIP \-- RIP配置命令 \-- display rip non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_931798900}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x399748013}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[display rip]{lang="EN-US"}**[ **non-stop-routing**]{lang="EN-US"}]{#struct_0_17903_10256_503284081}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1756954105}

[**[display rip]{lang="EN-US"}**[ \[ *process-id* \] **non-stop-routing**]{lang="EN-US"}]{#struct_0_17903_10256_359027069}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1678135281}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_101487280}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1412031769}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x529421858}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_1756888569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x459355930}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_531606308}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1613796952}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_x1340477964}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[如果未指定本参数，则显示所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:
黑体"}]{#struct_0_17903_10256_3928410}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1757085177}[显示]{style="font-family:宋体"}[RIP 1]{lang="EN-US"}[进程的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[状态信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 non-stop-routing]{lang="EN-US"}]{#struct_0_17903_10256_x1937711600}

[RIP process: 1]{lang="EN-US"}

[ Nonstop Routing capability: Enabled]{lang="EN-US"}

[ Current NSR state         : Finish]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display rip non-stop-routing]{lang="EN-US"}]{#struct_0_17903_10256_128579388}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x894305195}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1090911634}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_1757019641}

[[Nonstop Routing capability]{lang="EN-US"}]{#struct_0_17903_10256_1912100177}

[[NSR]{lang="EN-US"}]{#struct_0_17903_10256_x644152055}[使能状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_17903_10256_2136352655}[：]{lang="EN-US" style="font-family:宋体"}[使能]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_17903_10256_1757740537}[：]{lang="EN-US" style="font-family:宋体"}[不使能]{lang="EN-US" style="font-family:宋体"}[NSR]{lang="EN-US"}

[[Current NSR state]{lang="EN-US"}]{#struct_0_17903_10256_x1968298836}

[[当前]{style="font-family:宋体"}[NSR]{lang="EN-US"}]{#struct_0_17903_10256_1841983688}[所处状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initialization]{lang="EN-US"}]{#struct_0_17903_10256_1757675001}[：初始准备]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Smooth]{lang="EN-US"}]{#struct_0_17903_10256_366403015}[：数据平滑]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Advertising]{lang="EN-US"}]{#struct_0_17903_10256_1056918342}[：发布路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Redistribution]{lang="EN-US"}]{#struct_0_17903_10256_x222443322}[：路由引入处理]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Finish]{lang="EN-US"}]{#struct_0_17903_10256_1757216250}[：完成]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1999661556 .myid}
[]{#_Toc404787698}[]{#struct_0_17903_10256_88931234}[]{#_Toc216497578}[]{#_Toc137543151}[]{#_Toc137261554}[]{#_Toc137543101}[]{#_Toc137261556}[]{#_Toc137543103}[]{#_Toc137261557}[]{#_Toc137543104}[]{#_Toc137261558}[]{#_Toc137543105}[]{#_Toc137261559}[]{#_Toc137543106}[]{#_Toc137261560}[]{#_Toc137543107}[]{#_Toc137261561}[]{#_Toc137543108}[]{#_Toc137261562}[]{#_Toc137543109}[]{#_Toc137261563}[]{#_Toc137543110}[]{#_Toc137261568}[]{#_Toc137543115}[]{#_Toc137261572}[]{#_Toc137543119}[]{#_Toc137261603}[]{#_Toc137543150}

**RIP \-- RIP配置命令 \-- display rip route**

------------------------------------------------------------------------

[**[display rip route]{lang="EN-US"}**]{#struct_0_17903_10256_850127847}[命令用来显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x657464691}

[**[display rip ]{lang="EN-US"}***[process-id]{lang="EN-US"}***[ route ]{lang="EN-US"}**[\[ *ip-address* { *mask-length* \| *mask* } \[ **verbose** \] \| **peer** *ip-address* \| **statistics** \]]{lang="EN-US"}]{#struct_0_17903_10256_x2106712027}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x871995292}

[[任意视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1193828542}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2065976623}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1102133667}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_1535257072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1706211214}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_88996770}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x750469550}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_x1262083382}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_17903_10256_1972634733}[：显示指定目的地址和掩码的路由信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_17903_10256_458098478}[：显示当前]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由表中指定目的地址和掩码的所有路由信息。如果未指定本参数，则只显示指定目的地址和掩码的最优]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_715338633}[：显示从指定邻居学到的所有路由信息。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_17903_10256_x899002489}[：显示路由的统计信息。路由的统计信息包括路由总数目，各个邻居的路由数目。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x228377597}

[[如果未指定任何参数，将显示]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x729904027}[的所有路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_89062306}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1011356920}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程所有的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 route]{lang="EN-US"}]{#struct_0_17903_10256_x1173361024}

[ Route Flags: R -- RIP]{lang="EN-US"}

[              A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct]{lang="EN-US"}

[              O - Optimal, F - Flush to RIB]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Peer 1.1.1.1 on GigabitEthernet1/0/2]{lang="EN-US"}

[      Destination/Mask        Nexthop           Cost    Tag     Flags   Sec]{lang="EN-US"}

[      3.0.0.0/8               1.1.1.1           1       0       RAOF    24]{lang="EN-US"}

[ Local route]{lang="EN-US"}

[      Destination/Mask        Nexthop           Cost    Tag     Flags   Sec]{lang="EN-US"}

[      4.4.4.4/32              0.0.0.0           0       0       RDOF    -]{lang="EN-US"}

[      1.1.1.0/24              0.0.0.0           0       0       RDOF    -]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1151860170}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程指定路由的全部路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 route 3.0.0.0 8 verbose]{lang="EN-US"}]{#struct_0_17903_10256_89127842}

[ Route Flags: R -- RIP]{lang="EN-US"}

[              A - Aging, S - Suppressed, G - Garbage-collect, D -- Direct]{lang="EN-US"}

[              O - Optimal, F - Flush to RIB]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ Peer 1.1.1.1 on GigabitEthernet1/0/2]{lang="EN-US"}

[  Destination/Mask    OrigNexthop/RealNexthop          Cost  Tag   Flags Sec]{lang="EN-US"}

[  3.0.0.0/8           1.1.1.1/1.1.1.1                  1     0     RAOF  16]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display rip route]{lang="EN-US"}]{#struct_0_17903_10256_x953825126}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1072398851}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1562661880}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_89193378}

[[Route Flags]{lang="EN-US"}]{#struct_0_17903_10256_x1781306675}

[[路由标志：]{style="font-family:宋体"}]{#struct_0_17903_10256_2021618934}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="PT-BR"}]{#struct_0_17903_10256_737135736}[：]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="PT-BR"}[生成的路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[A]{lang="PT-BR"}]{#struct_0_17903_10256_x850435543}[：]{style="font-family:宋体"}[该路由处于老化时期]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="PT-BR"}]{#struct_0_17903_10256_1505733510}[：]{style="font-family:宋体"}[该路由处于抑制时期]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[G]{lang="PT-BR"}]{#struct_0_17903_10256_89258914}[：]{lang="EN-US" style="font-family:宋体"}[该路由处于]{lang="EN-US" style="font-family:宋体"}[Garbage-collect]{lang="PT-BR"}[时期]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_17903_10256_x702768753}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[生成的直连路由]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[O]{lang="PT-BR"}]{#struct_0_17903_10256_1377539679}[：]{style="font-family:宋体"}[该路由处于最优路由状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="PT-BR" style="font-size:10.0pt;font-family:Symbol"}[F]{lang="PT-BR"}]{#struct_0_17903_10256_1198988012}[：]{style="font-family:宋体"}[该路由已经被下刷到]{style="font-family:宋体"}[RIB]{lang="EN-US"}

[[Peer *X.X.X.X* on ]{lang="PT-BR"}*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17903_10256_x164253009}

[[在]{style="font-family:宋体"}]{#struct_0_17903_10256_89324450}[RIP]{lang="PT-BR"}[接口上从指定邻居学到的路由信息]{style="font-family:宋体"}

[[Local route]{lang="PT-BR"}]{#struct_0_17903_10256_x409420004}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1349906786}[本地生成的直连路由]{style="font-family:宋体"}

[[Destination/Mask]{lang="PT-BR"}]{#struct_0_17903_10256_89389986}

[[目的]{style="font-family:宋体"}]{#struct_0_17903_10256_693676806}[IP]{lang="PT-BR"}[地址]{style="font-family:宋体"}[/]{lang="PT-BR"}[掩码]{style="font-family:宋体"}

[[Nexthop]{lang="PT-BR"}]{#struct_0_17903_10256_1920244581}

[[路由的下一跳地址]{style="font-family:宋体"}]{#struct_0_17903_10256_x1300209234}

[[OrigNexthop/RealNexthop]{lang="EN-US"}]{#struct_0_17903_10256_x2054322322}

[[如果路由来自直连邻居，那么路由的真实下一跳就是原始下一跳；如果路由来自非直连邻居，对于成功迭代的路由]{style="font-family:宋体"}[RealNexthop]{lang="EN-US"}]{#struct_0_17903_10256_88406946}[则显示迭代出来的下一跳，否则不显示]{style="font-family:宋体"}

[[Cost]{lang="PT-BR"}]{#struct_0_17903_10256_x674405772}

[[度量值]{style="font-family:宋体"}]{#struct_0_17903_10256_x1958256554}

[[Tag]{lang="PT-BR"}]{#struct_0_17903_10256_x1777087699}

[[路由标记]{style="font-family:宋体"}]{#struct_0_17903_10256_784873585}

[[Flags]{lang="PT-BR"}]{#struct_0_17903_10256_88472482}

[[路由信息所处状态]{style="font-family:宋体"}]{#struct_0_17903_10256_63625660}

[[Sec]{lang="PT-BR"}]{#struct_0_17903_10256_1950744263}

[[路由信息所处状态对应的定时器时间]{style="font-family:宋体"}]{#struct_0_17903_10256_2059948618}

[ ]{lang="PT-BR"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1949909986}[显示进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的路由统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display rip 1 route statistics]{lang="EN-US"}]{#struct_0_17903_10256_88931235}

[ Peer              Optimal/Aging        Garbage]{lang="EN-US"}

[ 1.1.1.1           1/1                  0]{lang="EN-US"}

[ Local             2/0                  0]{lang="EN-US"}

[ Total             3/1                  0]{lang="EN-US"}

[]{#struct_0_17903_10256_x1488524313}[]{#_Toc79394769}[[表1-8 ]{lang="EN-US"}[display rip route statistics]{lang="EN-US"}]{#_Toc75056666}[命令显示信息]{style="font-family:
黑体"}[描述表]{style="font-family:黑体"}

[]{#table_struct_0_1064777524}[[字段]{style="font-family:黑体"}]{#struct_0_17903_10256_x1626190147}

[[描述]{style="font-family:黑体"}]{#struct_0_17903_10256_x1211546306}

[[Peer]{lang="EN-US"}]{#struct_0_17903_10256_88996771}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1205845586}[邻居]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Optimal]{lang="EN-US"}]{#struct_0_17903_10256_x191862287}

[[路由信息中处于最优路由状态的路由条数]{style="font-family:宋体"}]{#struct_0_17903_10256_x1192346245}

[[Aging]{lang="EN-US"}]{#struct_0_17903_10256_x734327427}

[[路由信息中处于老化状态的路由条数]{style="font-family:宋体"}]{#struct_0_17903_10256_1537574014}

[[Garbage]{lang="EN-US"}]{#struct_0_17903_10256_x750435830}

[[路由信息中处于]{style="font-family:宋体"}[Garbage-collection]{lang="EN-US"}]{#struct_0_17903_10256_89062307}[状态的路由条数]{style="font-family:宋体"}

[[Local]{lang="EN-US"}]{#struct_0_17903_10256_x944958216}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x319637876}[本地生成的直连路由条数的总和]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_17903_10256_89127843}

[[从所有]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1384827034}[邻居学习到的路由条数的总和]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::::: {#1745414037 .myid}
[]{#_Toc216497585}[]{#_Toc137543160}[]{#_Toc33866017}[]{#_Toc404787699}[]{#struct_0_17903_10256_1783944252}[]{#_Toc306797772}[]{#_Toc305059803}[]{#_Toc189305424}[]{#_Toc286221018}[]{#_Toc286221019}[]{#_Toc286221020}[]{#_Toc286221021}[]{#_Toc286221022}[]{#_Toc286221023}[]{#_Toc286221024}[]{#_Toc286221025}[]{#_Toc286221026}[]{#_Toc286221027}[]{#_Toc286221028}[]{#_Toc286221029}[]{#_Toc286221030}[]{#_Toc286221031}[]{#_Toc286221032}[]{#_Toc286221033}[]{#_Toc286221034}[]{#_Toc286221035}[]{#_Toc286221036}[]{#_Toc286221037}[]{#_Toc286221040}[]{#_Toc286221043}[]{#_Toc286221046}[]{#_Toc286221047}[]{#_Toc286221050}[]{#_Toc286221053}[]{#_Toc286221057}[]{#_Toc286221058}[]{#_Toc286221059}[]{#_Toc286221060}[]{#_Toc286221061}[]{#_Toc286221062}[]{#_Toc286221063}[]{#_Toc286221064}[]{#_Toc286221065}[]{#_Toc286221066}[]{#_Toc286221067}[]{#_Toc286221068}[]{#_Toc286221069}[]{#_Toc286221070}[]{#_Toc286221071}[]{#_Toc286221072}[]{#_Toc286221073}[]{#_Toc286221074}[]{#_Toc286221075}[]{#_Toc286221076}[]{#_Toc286221077}[]{#_Toc286221078}[]{#_Toc286221079}[]{#_Toc286221080}[]{#_Toc286221081}[]{#_Toc286221087}[]{#_Toc286221088}[]{#_Toc286221089}[]{#_Toc286221090}[]{#_Toc286221095}[]{#_Toc286221096}[]{#_Toc286221097}[]{#_Toc286221098}[]{#_Toc286221099}[]{#_Toc286221100}[]{#_Toc286221101}[]{#_Toc286221102}[]{#_Toc286221103}[]{#_Toc286221104}[]{#_Toc286221105}[]{#_Toc286221106}[]{#_Toc286221107}[]{#_Toc286221108}[]{#_Toc286221109}[]{#_Toc286221110}[]{#_Toc286221111}[]{#_Toc286221112}[]{#_Toc286221113}[]{#_Toc286221114}[]{#_Toc286221115}[]{#_Toc286221116}[]{#_Toc286221117}[]{#_Toc286221123}[]{#_Toc286221124}[]{#_Toc286221125}[]{#_Toc286221126}[]{#_Toc286221131}[]{#_Toc286221132}[]{#_Toc286221134}[]{#_Toc286221135}[]{#_Toc286221136}[]{#_Toc286221137}[]{#_Toc286221138}[]{#_Toc286221139}[]{#_Toc286221140}[]{#_Toc286221141}[]{#_Toc286221142}[]{#_Toc286221143}[]{#_Toc286221144}[]{#_Toc286221145}[]{#_Toc286221146}[]{#_Toc286221147}[]{#_Toc286221148}[]{#_Toc286221149}[]{#_Toc286221150}[]{#_Toc286221151}[]{#_Toc286221155}[]{#_Toc286221156}[]{#_Toc286221158}[]{#_Toc286221159}[]{#_Toc286221160}[]{#_Toc286221161}[]{#_Toc286221162}[]{#_Toc286221163}[]{#_Toc286221164}[]{#_Toc286221165}[]{#_Toc286221166}[]{#_Toc286221167}[]{#_Toc286221168}[]{#_Toc286221169}[]{#_Toc286221170}[]{#_Toc286221171}[]{#_Toc286221172}[]{#_Toc286221173}[]{#_Toc286221174}[]{#_Toc286221175}[]{#_Toc286221176}[]{#_Toc286221177}[]{#_Toc286221178}[]{#_Toc286221179}[]{#_Toc286221180}[]{#_Toc286221182}[]{#_Toc286221184}[]{#_Toc286221186}[]{#_Toc137261609}[]{#_Toc137543156}[]{#_Toc137261610}[]{#_Toc137543157}[]{#_Toc137261611}[]{#_Toc137543158}[]{#_Toc286221188}[]{#_Toc286221189}[]{#_Toc286221190}[]{#_Toc286221191}[]{#_Toc286221192}[]{#_Toc286221193}[]{#_Toc286221194}[]{#_Toc286221195}[]{#_Toc286221196}[]{#_Toc286221197}[]{#_Toc286221198}[]{#_Toc286221199}[]{#_Toc286221200}[]{#_Toc286221201}[]{#_Toc286221202}

**RIP \-- RIP配置命令 \-- fast-reroute**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_62343353}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_1801960815}
:::

[ ]{lang="EN-US"}

[**[fast-reroute]{lang="EN-US"}**]{#struct_0_17903_10256_x806542652}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_17903_10256_730859538}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[快速重路由功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1098297136}

[**[fast-reroute route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_17903_10256_89193379}

[**[undo fast-reroute]{lang="EN-US"}**]{#struct_0_17903_10256_175008461}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_392385189}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1701551752}[快速重路由功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x404580388}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1636823371}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_2010482868}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1950412816}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x783700184}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_89258915}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_17903_10256_1253546383}[：为通过策略的路由指定备份下一跳。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x820090668}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1456209806}[快速重路由功能只适合在主链路三层接口]{style="font-family:宋体"}[up]{lang="EN-US"}[，主链路由双通变为单通或者不通的情况下使用。在主链路三层接口]{style="font-family:宋体"}[down]{lang="EN-US"}[的情况下，本功能不可用。单通现象，即一条链路上的两端，有且只有一端可以收到另一端发来的报文，此链路称为单向链路。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x432465382}[快速重路由功能仅对非迭代]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由（即从直连邻居学到]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由）有效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1870554220}[快速重路由功能不能与]{style="font-family:宋体"}[RIP]{lang="EN-US"}[支持]{style="font-family:宋体"}[BFD]{lang="EN-US"}[检测功能同时使用，否则可能导致快速重路由功能失效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[等价路由不支持快速重路由功能，当备份信息与主路由信息相同时该功能不生效。]{style="font-family:宋体"}]{#struct_0_17903_10256_1395588795}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1580027077}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_123069437}[配置对通过策略]{style="font-family:宋体"}[frr]{lang="EN-US"}[的路由指定备份下一跳信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{style="font-family:宋体"}]{#struct_0_17903_10256_89324451}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1929232156}

[\[Sysname\] ip prefix-list abc index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy frr permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] if-match ip address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] apply fast-reroute backup-interface gigabitethernet 1/0/1 backup-nexthop 193.1.1.8]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] quit]{lang="EN-US"}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] fast-reroute route-policy frr]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{style="font-family:宋体"}]{#struct_0_17903_10256_473963867}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_89389987}

[\[Sysname\] ip prefix-list abc index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy frr permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] if-match ip address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] apply fast-reroute backup-interface vlan-interface 1 backup-nexthop 193.1.1.8]{lang="EN-US"}

[\[Sysname-route-policy-frr-10\] quit]{lang="EN-US"}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] fast-reroute route-policy frr]{lang="EN-US"}
:::::

::: {#1247311243 .myid}
[]{#struct_0_17903_10256_x1262638330}[]{#_Toc404787700}[]{#_Toc306797773}[]{#_Toc305059804}[]{#_Toc216497580}

**RIP \-- RIP配置命令 \-- filter-policy export**

------------------------------------------------------------------------

[**[filter-policy]{lang="EN-US"}[ export]{lang="EN-US"}**]{#struct_0_17903_10256_1559912432}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[对发布的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_17903_10256_x49661260}[命令用来取消对发布路由信息的过滤。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x481149647}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **prefix-list** *prefix-list-name* } **export** \[ *protocol* \[ *process-id* \] \| *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_211358758}

[**[undo filter-policy]{lang="EN-US"}**[ **export** \[ *protocol* \[ *process-id* \] \| *interface-type interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_x1559990950}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_1984759008}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_88406947}[不对发布的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_1664246388}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x127201369}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_557217099}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_501031914}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_723526789}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_519478665}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17903_10256_868233603}[：用]{style="font-family:宋体"}[于过滤发布的路由信息的访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_17903_10256_x1280476528}[：指定用于过滤发布路由信息的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名称。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_17903_10256_88472483}[：过滤]{style="font-family:宋体"}[指定路由协议发布的]{style="font-family:宋体"}[路由信息，]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[可以选择]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_2019940796}[：被过滤路由信息的路由协议的进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。仅当路由协议为]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[时需要指定进程号，若未指定，缺省进程号为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}]{#struct_0_17903_10256_213907282}[：过滤]{style="font-family:宋体"}[指定接口发布的路由信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为]{style="font-family:宋体"}[接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_839381458}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个协议或接口只能配置一个过滤策略。如果未指定协议或接口，就认为是配置全局过滤策略，同样每次只能配置一个。如果重复配置，新的策略将覆盖之前的策略。]{style="font-family:宋体"}]{#struct_0_17903_10256_310342875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果已经配置了基于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1757347327}[协议或]{style="font-family:宋体"}[接口的]{lang="EN-US" style="font-family:宋体"}[过滤]{style="font-family:宋体"}[策略，删除时必须指定]{lang="EN-US" style="font-family:宋体"}*[protocol]{lang="EN-US"}*[或]{lang="EN-US" style="font-family:宋体"}[*[interface-type]{lang="EN-US"}*]{.varname}[ [*interface-number*]{.varname}]{lang="EN-US"}[[。]{style="font-family:宋体"}]{.varname}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[当配置的是高级]{style="font-family:宋体"}]{#struct_0_17903_10256_x1302347577}[ACL]{lang="EN-US"}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_1771511990}

[]{#_Toc306797774}[]{#_Toc305059805}[]{#_Toc33866013}[]{#struct_0_17903_10256_2044248015}[]{#_Toc292815525}[]{#_Toc216497581}[]{#_Toc137543153}[\# ]{lang="EN-US"}[配置使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[来对发布的路由信息进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_88931232}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] filter-policy 2000 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x296883225}[配置按照地址前缀列表来过滤发布的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_446875866}

[\[Sysname\] ip prefix-list abc index 10 permit 11.0.0.0 8]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] filter-policy prefix-list abc export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1772053928}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对发布的路由进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_88996768}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip 1\] filter-policy 3000 export]{lang="EN-US"}

[[【命令参考】]{style="font-family:黑体"}]{#struct_0_17903_10256_x787205395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_17903_10256_996444999}[（]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:
宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:
宋体"}[/ACL]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[import-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1689698134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip prefix]{lang="EN-US"}**]{#struct_0_17903_10256_1173022610}**[-list]{lang="EN-US"}**[（]{lang="EN-US" style="font-family:宋体"}[三层技术]{lang="EN-US" style="font-family:
宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:
宋体"}[/]{lang="EN-US"}[路由策略]{lang="EN-US" style="font-family:
宋体"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#632247711 .myid}
[]{#_Toc404787701}[]{#struct_0_17903_10256_x1991958980}

**RIP \-- RIP配置命令 \-- filter-policy import**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_17903_10256_x28015843}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[对接收的路由信息进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_17903_10256_735485838}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1602178717}

[**[filter-policy]{lang="EN-US"}**[ { *acl-number* \| **gateway** *prefix-list-name* \| **prefix-list** *prefix-list-name* \[ **gateway** *prefix-list-name* \] } **import** \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_x1463160038}

[**[undo filter-policy]{lang="EN-US"}**[ **import** \[ *interface-type* *interface-number* \]]{lang="EN-US"}]{#struct_0_17903_10256_89062304}

[[【缺省情况】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_629019896}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x690186767}[不对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_920194773}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1254727851}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1434252408}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1635123565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1436717962}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x2090223889}

[*[acl-number]{lang="EN-US"}*]{#struct_0_17903_10256_89127840}[：]{style="font-family:宋体"}[用于过滤发布的路由信息的访问控制列表号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_17903_10256_x1336162150}[：指定用于过滤接收路由信息的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名称。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[gateway]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_17903_10256_x133519825}[：基于要加入到路由表的路由信息的下一跳进行过滤。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17903_10256_1704989359}[：]{style="font-family:宋体"}[过滤]{style="font-family:宋体"}[指定接口接收的路由信息，]{style="font-family:宋体"}*[interface-type]{lang="EN-US"}*[ *interface-number*]{lang="EN-US"}[为]{style="font-family:宋体"}[接口类型和编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_115424312}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个接口只能配置一个过滤策略。如果未指定接口，就认为是配置全局过滤策略，同样每次只能配置一个。如果重复配置，新的策略将覆盖之前的策略。]{style="font-family:宋体"}]{#struct_0_17903_10256_1756888575}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果已经配置了基于接口的过滤策略，删除时必须指定]{lang="EN-US" style="font-family:宋体"}[*[interface-type]{lang="EN-US"}*]{.varname}[ [*interface-number*]{.varname}]{lang="EN-US"}]{#struct_0_17903_10256_x459093785}[[。]{style="font-family:宋体"}]{.varname}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当配置的是高级]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1045182592}[ACL]{lang="EN-US"}[（]{lang="EN-US" style="font-family:宋体"}[3000]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[）时，]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{lang="EN-US" style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ip source** *sour-addr sour-wildcard* **destination** *dest-addr dest-wildcard*]{lang="EN-US"}[来过滤指定目的地址和掩码的路由，其中]{lang="EN-US" style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{lang="EN-US" style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由掩码，配置的掩码应该是连续的（当配置的掩码不连续时该过滤掩码的条件不生效）。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_406964103}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x784878547}[配置使用编号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[的基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[来对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_89193376}

[\[Sysname\] acl basic 2000]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] rule deny source 192.168.10.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-basic-2000\] quit]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] filter-policy 2000 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_601975501}[配置按照]{style="font-family:宋体"}[地址前缀列表]{style="font-family:宋体"}[来过滤接收的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1763949463}

[\[Sysname\] ip prefix-list abc index 10 permit 11.0.0.0 8]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] filter-policy prefix-list abc import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x247949771}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许]{style="font-family:宋体"}[113.0.0.0/16]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x74765535}

[\[Sysname\] acl advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 10 permit ip source 113.0.0.0 0 destination 255.255.0.0 0]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] rule 100 deny ip]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] filter-policy 3000 import]{lang="EN-US"}

[[【命令参考】]{style="font-family:黑体"}]{#struct_0_17903_10256_89258912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[acl]{lang="EN-US"}**]{#struct_0_17903_10256_x1085105777}[（]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[和]{lang="EN-US" style="font-family:
宋体"}[QoS]{lang="EN-US"}[命令参考]{lang="EN-US" style="font-family:
宋体"}[/ACL]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip prefix]{lang="EN-US"}**]{#struct_0_17903_10256_x579780442}**[-list]{lang="EN-US"}**[（]{lang="EN-US" style="font-family:宋体"}[三层技术]{lang="EN-US" style="font-family:
宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:
宋体"}[/]{lang="EN-US"}[路由策略]{lang="EN-US" style="font-family:
宋体"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#63544256 .myid}
[]{#_Toc306797775}[]{#_Toc305059806}[]{#_Toc33866015}[]{#_Toc313007768}[]{#_Toc404787702}[]{#struct_0_17903_10256_813302437}[]{#_Toc321837765}[]{#_Toc303839441}

**RIP \-- RIP配置命令 \-- graceful-restart**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_567761979}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x1206121650}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_17903_10256_x1530151549}[命令用来使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo graceful-restart]{lang="EN-US"}**]{#struct_0_17903_10256_x93457721}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1315013796}

[**[graceful-restart]{lang="EN-US"}**]{#struct_0_17903_10256_89324448}

[**[undo ]{lang="FR"}[graceful-restart]{lang="EN-US"}**]{#struct_0_17903_10256_790115255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_545399052}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x632089852}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_685249000}

[[RIP]{lang="FR"}]{#struct_0_17903_10256_979699464}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1627239923}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1675389705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1603707275}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1757740543}

[[RIP GR]{lang="EN-US"}]{#struct_0_17903_10256_1757675007}[特性与]{style="font-family:宋体"}[RIP NSR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[和]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_89389984}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1076013830}[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> syste]{lang="EN-US"}[m-view]{lang="EN-US"}]{#struct_0_17903_10256_1912383907}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] graceful-restart]{lang="EN-US"}
:::::

::::: {#16863910 .myid}
[]{#_Toc404787703}[]{#struct_0_17903_10256_366271943}[]{#_Toc375235985}[]{#_Toc328746895}[]{#_Toc322698687}

**RIP \-- RIP配置命令 \-- graceful-restart interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_54139696}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_1757216256}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[graceful-restart interval]{lang="EN-US"}**]{#struct_0_17903_10256_1561225653}[命令用来配置]{style="font-family:
宋体"}[RIP]{lang="EN-US"}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_17903_10256_x721970407}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1463877188}

[**[graceful-restart interval ]{lang="EN-US"}***[interval-value]{lang="EN-US"}*]{#struct_0_17903_10256_1757150720}

[**[undo graceful-restart interval]{lang="EN-US"}**]{#struct_0_17903_10256_1939612915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x991953394}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1470379838}[协议的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1757347328}

[[RIP]{lang="FR"}]{#struct_0_17903_10256_786756852}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1515951309}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1194299234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1757281792}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x758927184}

[*[interval-value]{lang="EN-US"}*]{#struct_0_17903_10256_1369555640}[：]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间，取值范围是]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[360]{lang="EN-US"}[，单位是秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1756954112}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_359223676}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[GR]{lang="EN-US"}[重启间隔时间为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1908422940}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] graceful-restart interval 200]{lang="EN-US"}
:::::

::: {#-52316550 .myid}
[]{#_Toc404787704}[]{#struct_0_17903_10256_x1752914057}

**RIP \-- RIP配置命令 \-- host-route**

------------------------------------------------------------------------

[**[host-route]{lang="EN-US"}**]{#struct_0_17903_10256_547746163}[命令用来允许]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接收主机路由。]{style="font-family:宋体"}

[**[undo host-route]{lang="EN-US"}**]{#struct_0_17903_10256_1633660909}[命令用来禁止]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接收主机路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1539118296}

[**[host-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1396524598}

[**[undo host-route]{lang="EN-US"}**]{#struct_0_17903_10256_88406944}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x292068748}

[[允许]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_739082341}[接收主机路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1703615907}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x658020776}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1932332637}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1012835560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x930235215}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x373450007}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[在某些特殊情况下，路由器会收到大量来自同一网段的主机路由。这些路由对于路由寻址没有多少作用，却占用了大量的资源；此时可以使用]{style="font-family:宋体"}]{#struct_0_17903_10256_88472480}**[undo host-route]{lang="EN-US"}**[命令禁止接收主机路由，以节省网络资源。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[该命令仅对]{style="font-family:宋体"}]{#struct_0_17903_10256_445962684}[RIPv2]{lang="EN-US"}[报文携带的路由]{style="font-family:宋体"}[有效，对]{style="font-family:宋体"}[RIPv1]{lang="EN-US"}[报文携带的路由]{style="font-family:宋体"}[无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_127292718}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1159038225}[禁止]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接收主机路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x817312470}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] undo host-route]{lang="EN-US"}
:::

::: {#29262825 .myid}
[]{#_Toc404787705}[]{#struct_0_17903_10256_920185101}

**RIP \-- RIP配置命令 \-- import-route**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1479887084}[命令用来从其它路由协议引入路由。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_17903_10256_x461243037}[命令用来取消引入外部路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_88931233}

[**[import-route ]{lang="EN-US"}***[protocol]{lang="EN-US"}*[ \[ *process-id* \| **all-processes** \| **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| **route-policy** *route-policy-name* ]{lang="EN-US"}]{#struct_0_17903_10256_1659431911}[[\| **tag** *tag* \]]{lang="EN-US"}]{#_Hlt24451966}[ \*]{lang="EN-US"}

[**[undo import-route ]{lang="PT-BR"}**]{#struct_0_17903_10256_x1584746510}*[protocol]{lang="PT-BR"}*[ \[ *process-id* ]{lang="PT-BR"}[\| **all-processes** \]]{lang="EN-US"}

[[【缺省]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1393974095}[情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-family:黑体;
color:#0096d6"}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1104182603}[不引入其它路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1017496939}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_88996769}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1169109741}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_234955636}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x423593000}

[[【参数】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x484090102}

[*[protocol]{lang="EN-US"}*]{#struct_0_17903_10256_283329542}[：指定引入的路由协议，]{style="font-family:宋体"}[可以是]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[、]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[或]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[proces]{lang="EN-US"}*[s-*id*]{lang="EN-US"}]{#struct_0_17903_10256_2051195215}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[时该参数]{style="font-family:宋体"}[可选。]{style="font-family:宋体"}

[**[all-processes]{lang="EN-US"}**]{#struct_0_17903_10256_581161255}[：引入指定路由协议所有进程的路由，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[rip]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospf]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isis]{lang="EN-US"}**[时可以指定该参]{style="font-family:宋体"}[数。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_17903_10256_89062305}[：当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}**[bgp]{lang="EN-US"}**[时，]{style="font-family:宋体"}**[allow-ibgp]{lang="EN-US"}**[为可选关键字]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_17903_10256_x1327295240}[：在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入协议路由时不会包含使能了该协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ cost]{lang="EN-US"}*]{#struct_0_17903_10256_1487541414}[：所要引入路由的度量]{style="font-family:宋体"}[值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}**]{#struct_0_17903_10256_988801899}*[route-policy-name]{lang="EN-US"}*[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}***[ tag]{lang="EN-US"}*]{#struct_0_17903_10256_x1167200215}[：所要引入路由的标记值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_x1880697625}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[import-route]{lang="EN-US"}**]{#struct_0_17903_10256_492855271}[ ]{lang="EN-US" style="font-family:宋体"}*[bgp]{lang="EN-US"}*[表示只引入]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由；]{lang="EN-US" style="font-family:宋体"}**[import-route ]{lang="EN-US"}***[bgp]{lang="EN-US"}***[ allow-ibgp]{lang="EN-US"}**[表示将]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由也引入，容易引起路由环路，请慎用]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[只能引入路由表中状态为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}]{#struct_0_17903_10256_x1088878539}[的路由，是否为]{lang="EN-US" style="font-family:宋体"}[active]{lang="EN-US"}[状态可以通过]{lang="EN-US" style="font-family:宋体"}**[display]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[ip]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[routing-table protocol]{lang="EN-US"}**[命令来查看。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[undo import-route]{lang="EN-US"}**[ *protocol* **all-processes**]{lang="EN-US"}]{#struct_0_17903_10256_89127841}[命令只能取消]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**[ *protocol* **all-processes**]{lang="EN-US"}[命令的配置，不能取消]{lang="EN-US" style="font-family:宋体"}**[import-route]{lang="EN-US"}**[ *protocol* *process-id*]{lang="EN-US"}[命令的配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_1002490010}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x297000091}[引入静态路由，并将其度量值设置为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_462300472}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] import-route static cost 4]{lang="EN-US"}

[[【命令参考】]{style="font-family:黑体"}]{#struct_0_17903_10256_x194294670}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default cost]{lang="EN-US"}**]{#struct_0_17903_10256_2027812840}
:::

::::: {#1012649285 .myid}
[]{#_Toc404787706}[]{#struct_0_17903_10256_x845279343}[]{#_Toc313007770}

**RIP \-- RIP配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_1829120539}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_89193377}
:::

**[ ]{lang="EN-US"}**

[**[maximum load-balancing]{lang="EN-US"}**]{#struct_0_17903_10256_x1736676659}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[最大等价路由条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_17903_10256_238599960}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2117060245}

[**[maximum load-balancing]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_17903_10256_347012688}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_17903_10256_1577641984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1769324593}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x627104175}[支持的等价路由的最大条数与]{style="font-family:宋体"}[系统支持最大等价路由的条数相同]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x38261147}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_89258913}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_871209359}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1917402909}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_268498373}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_2087777547}

[*[number]{lang="EN-US"}*]{#struct_0_17903_10256_74172583}[：等价路由的最大条数。不同型号的设备支持的取值范围不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x429680264}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_17903_10256_1430651292}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_17903_10256_1716802154}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1381212229}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_89324449}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[最大等价路由条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1166199881}

[\[Sysname\] rip ]{lang="EN-US"}

[\[Sysname-rip-1\] maximum load-balancing 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_100396875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_17903_10256_x1109866592}[（三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{style="font-family:宋体"}
:::::

::: {#-815886662 .myid}
[]{#_Toc404787707}[]{#struct_0_17903_10256_1367187644}

**RIP \-- RIP配置命令 \-- network**

------------------------------------------------------------------------

[**[network]{lang="EN-US"}**]{#struct_0_17903_10256_600671214}[命令用来在指定网段上使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo network]{lang="EN-US"}**]{#struct_0_17903_10256_1432755236}[命令用来在指定网段上禁用]{style="font-family:宋体"}[RIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_87805366}

[**[network ]{lang="EN-US"}***[network-address ]{lang="EN-US"}*[\[ *wildcard-mask* \]]{lang="EN-US"}]{#struct_0_17903_10256_89389985}

[**[undo]{lang="EN-US"}**[ **network** *network-address*]{lang="EN-US"}]{#struct_0_17903_10256_x880301306}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1400391388}

[[没有网段使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1460323545}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2021824830}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_733515282}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1080026286}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1509662560}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x642673382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1267360516}

[*[network-address]{lang="EN-US"}*]{#struct_0_17903_10256_88406945}[：指定网段的地址，其取值可以为各个接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[网络地址。]{style="font-family:宋体"}

[*[wildcard-mask]{lang="EN-US"}*]{#struct_0_17903_10256_2046583412}[：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码的反码，相当于将]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的掩码取反（]{style="font-family:宋体"}[0]{lang="EN-US"}[变]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:宋体"}[1]{lang="EN-US"}[变]{style="font-family:
宋体"}[0]{lang="EN-US"}[）。其中，"]{style="font-family:宋体"}[1]{lang="EN-US"}["表示忽略]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址中对应的位，"]{style="font-family:宋体"}[0]{lang="EN-US"}["表示必须保留此位。（例如：子网掩码]{style="font-family:宋体"}[255.0.0.0]{lang="EN-US"}[，该掩码的反码为]{style="font-family:宋体"}[0.255.255.255]{lang="EN-US"}[）。如果未指定本参数，将按照自然网段进行。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_2006565596}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x187343222}[只在指定网段的接口上运行，指定网段可以配置掩码；对于不在指定网段上的接口，]{style="font-family:宋体"}[RIP]{lang="EN-US"}[既不在它上面接收和发送路由，也不将它的接口路由发布出去。因此，]{style="font-family:宋体"}[RIP]{lang="EN-US"}[启动后必须指定其工作网段。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在单进程情况下，可以使用]{lang="EN-US" style="font-family:宋体"}**[network ]{lang="EN-US"}**[0.0.0.0]{lang="EN-US"}]{#struct_0_17903_10256_266326000}[命令在所有接口上使能]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="EN-US"}[；在多进程情况下，无法使用]{lang="EN-US" style="font-family:宋体"}**[network ]{lang="EN-US"}**[0.0.0.0]{lang="EN-US"}[命令。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x759019768}[不支持将同一物理接口下的不同网段使能到不同的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_936780255}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x2101257323}[在指定网段]{style="font-family:宋体"}[129.102.0.0]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_88472481}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] network 129.102.0.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1892689476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[rip enable]{lang="EN-US"}**]{#struct_0_17903_10256_413856647}
:::

::::: {#-1554088180 .myid}
[]{#_Toc404787708}[]{#struct_0_17903_10256_1353604044}[]{#_Toc375235990}[]{#_Toc328746897}[]{#_Toc322698689}

**RIP \-- RIP配置命令 \-- non-stop-routing**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_x1432202657}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_1353800652}[。]{style="font-family:KaiTi_GB2312"}
:::

[ ]{lang="EN-US"}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_17903_10256_1275601932}[命令用来使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协]{style="font-family:宋体"}[议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功]{style="font-family:宋体"}[能。]{style="font-family:宋体"}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_17903_10256_x1213415385}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议]{style="font-family:宋体"}[的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1170791763}

[**[non-stop-routing]{lang="EN-US"}**]{#struct_0_17903_10256_1353735116}

[**[undo non-stop-routing]{lang="EN-US"}**]{#struct_0_17903_10256_2079120810}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x672978908}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1354456012}[协议的]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1185638634}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x387394987}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1354390476}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1119626547}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_797896213}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1353931725}

[[RIP NSR]{lang="EN-US"}]{#struct_0_17903_10256_491892557}[特性与]{style="font-family:宋体"}[RIP GR]{lang="EN-US"}[特性互斥，即]{style="font-family:宋体"}**[non-stop-routing]{lang="EN-US"}**[和]{style="font-family:宋体"}**[graceful-restart]{lang="EN-US"}**[命令互斥，不能同时配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x671200089}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_267780564}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[使能]{style="font-family:宋体"}[NSR]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1353866189}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] non-stop-routing]{lang="EN-US"}
:::::

::: {#-1957377733 .myid}
[]{#_Toc137543161}[]{#_Toc33866018}[]{#_Toc404787709}[]{#struct_0_17903_10256_x267118838}[]{#_Toc216497586}

**RIP \-- RIP配置命令 \-- output-delay**

------------------------------------------------------------------------

[**[output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_1222736872}[用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的发送速率。]{style="font-family:宋体"}

[**[undo output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_902515280}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_115620607}

[**[output-delay]{lang="EN-US"}***[ time ]{lang="EN-US"}***[count ]{lang="EN-US"}***[count]{lang="EN-US"}*]{#struct_0_17903_10256_1590847922}

[**[undo output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_2069220417}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_24332042}

[[接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1655015177}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[3]{lang="EN-US"}[个]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2015306224}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_2028063750}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1349027125}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1915092177}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1118037004}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1508149485}

[*[time]{lang="EN-US"}*]{#struct_0_17903_10256_x1604829899}[：接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_17903_10256_1655080713}[：接口一次发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x129948399}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x460282210}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的所有接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[60]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[10]{lang="EN-US"}[个]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x921040425}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] output-delay 60 count 10]{lang="EN-US"}
:::

::: {#1903411553 .myid}
[]{#_Toc216497591}[]{#_Toc137543192}[]{#_Toc33866021}[]{#_Toc306797778}[]{#_Toc305059808}[]{#_Toc33866019}[]{#_Toc404787710}[]{#struct_0_17903_10256_x529530762}[]{#_Toc331171739}[]{#_Toc328746898}[]{#_Toc322698690}[]{#_Toc286221208}[]{#_Toc286221209}[]{#_Toc286221210}[]{#_Toc286221211}[]{#_Toc286221212}[]{#_Toc286221213}[]{#_Toc286221214}[]{#_Toc286221215}[]{#_Toc286221216}[]{#_Toc286221217}[]{#_Toc286221218}[]{#_Toc286221219}[]{#_Toc286221220}[]{#_Toc286221221}[]{#_Toc286221222}[]{#_Toc286221223}[]{#_Toc286221228}[]{#_Toc286221230}[]{#_Toc286221231}[]{#_Toc286221232}[]{#_Toc286221233}[]{#_Toc286221234}[]{#_Toc286221235}[]{#_Toc286221236}[]{#_Toc286221237}[]{#_Toc286221238}[]{#_Toc286221239}[]{#_Toc286221240}[]{#_Toc286221241}[]{#_Toc286221242}[]{#_Toc286221243}[]{#_Toc286221244}[]{#_Toc286221245}[]{#_Toc286221247}[]{#_Toc286221248}[]{#_Toc137543164}[]{#_Toc137543165}[]{#_Toc137543166}[]{#_Toc137543167}[]{#_Toc137543168}[]{#_Toc137543169}[]{#_Toc137543170}[]{#_Toc137543171}[]{#_Toc137543172}[]{#_Toc137543173}[]{#_Toc137543174}[]{#_Toc137543175}[]{#_Toc137543176}[]{#_Toc137543177}[]{#_Toc137543178}[]{#_Toc137543179}[]{#_Toc137543180}[]{#_Toc137543181}[]{#_Toc137543182}[]{#_Toc137543183}[]{#_Toc137543184}[]{#_Toc137543185}[]{#_Toc137543186}[]{#_Toc137543187}[]{#_Toc137543188}[]{#_Toc137543189}[]{#_Toc137543190}[]{#_Toc286221249}[]{#_Toc286221250}[]{#_Toc286221251}[]{#_Toc286221252}[]{#_Toc286221253}[]{#_Toc286221254}[]{#_Toc286221255}[]{#_Toc286221256}[]{#_Toc286221257}[]{#_Toc286221258}[]{#_Toc286221259}[]{#_Toc286221260}[]{#_Toc286221261}[]{#_Toc286221262}[]{#_Toc286221263}[]{#_Toc286221264}[]{#_Toc286221266}[]{#_Toc286221267}[]{#_Toc286221268}[]{#_Toc286221269}[]{#_Toc286221270}[]{#_Toc286221271}[]{#_Toc286221272}[]{#_Toc286221273}[]{#_Toc286221274}[]{#_Toc286221275}[]{#_Toc286221276}[]{#_Toc286221277}[]{#_Toc286221278}

**RIP \-- RIP配置命令 \-- peer**

------------------------------------------------------------------------

[**[peer]{lang="EN-US"}**]{#struct_0_17903_10256_x1860763330}[命令用来配置]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[（]{style="font-family:宋体"}[Non-Broadcast Multi-Access]{lang="EN-US"}[，非广播多路访问）网络中]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并使更新报文以单播形式发送到对端，而不采用正常的组播或广播的形式。]{style="font-family:宋体"}

[**[undo peer]{lang="EN-US"}**]{#struct_0_17903_10256_x661713527}[命令用来取消指定邻居]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x250642635}

[**[peer]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_1655146249}

[**[undo peer ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_x2012780205}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2106681664}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_468587742}[不向任何定点地址发送单播更新报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1021460775}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1184995590}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_942540238}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x590333390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_880068617}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655211785}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_1457434799}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，用点分十进制格式表示。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x26324440}

[[当]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1699876082}[邻居与当前设备直连时不推荐使用该命令，因为这样可能会造成对端同时收到同一路由信息的组播（或广播）和单播两种形式的报文。]{style="font-family:宋体"}

[[配置本命令时，必须同时配置]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **validate-source-address**]{lang="EN-US"}]{#struct_0_17903_10256_363310369}[命令，即取消对接收到的]{style="font-family:
宋体"}[RIP]{lang="EN-US"}[路由更新报文进行源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x87129829}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1239702780}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[为]{style="font-family:宋体"}[202.38.165.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_960691688}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] peer 202.38.165.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655277321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[validate-source-address]{lang="EN-US"}**]{#struct_0_17903_10256_1512568083}
:::

::: {#830408614 .myid}
[]{#_Toc404787711}[]{#struct_0_17903_10256_900442465}

**RIP \-- RIP配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_17903_10256_x1604381835}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_17903_10256_x1971459914}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1676883420}

[**[preference]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_17903_10256_x1771044930}

[**[undo preference]{lang="EN-US"}**]{#struct_0_17903_10256_1042096493}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x819558357}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1655342857}[路由的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1597948928}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1472416178}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1423372322}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1617486533}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x667275988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x272668768}

[*[preference]{lang="EN-US"}*]{#struct_0_17903_10256_364939192}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由优先级的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，取值越小，优先级越高。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}**]{#struct_0_17903_10256_1632853483}*[route-policy-name]{lang="EN-US"}*[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。对满足特定条件的路由设置优先级。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655408393}

[[通过指定]{style="font-family:宋体"}]{#struct_0_17903_10256_x514799251}**[route-policy]{lang="EN-US"}**[参数，可应用路由策略对特定的路由设置优先级：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在路由策略中已经设置了匹配路由的优先级，则匹配路由取路由策略设置的优先级，其它路由取]{style="font-family:宋体"}]{#struct_0_17903_10256_x1977810177}**[preference]{lang="EN-US"}**[命令所设优先级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在路由策略中没有设置匹配路由的优先级，则所有路由都取]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1843714861}**[preference]{lang="EN-US"}**[命令所设优先级。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1968599736}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x416275733}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的优先级为]{style="font-family:宋体"}[120]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_66006985}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] preference 120]{lang="EN-US"}
:::

::: {#756940664 .myid}
[]{#_Toc404787712}[]{#struct_0_17903_10256_968865818}[]{#_Toc313007774}

**RIP \-- RIP配置命令 \-- reset rip process**

------------------------------------------------------------------------

[**[reset rip process]{lang="EN-US"}**]{#struct_0_17903_10256_1655473929}[命令用来重启指定]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1925957309}

[**[reset rip ]{lang="EN-US"}**]{#struct_0_17903_10256_382123550}*[process-id]{lang="EN-US"}*[ ]{lang="EN-US"}**[process]{lang="EN-US"}**

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_2047593803}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x741424419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_236863202}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_809644225}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x971143015}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x591628648}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_x1428258414}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1654490889}

[[执行该命令后，系统提示用户确认是否重启]{style="font-family:宋体"}]{#struct_0_17903_10256_x1245829996}[RIP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x782534453}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1106110663}[重启进程号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程。]{style="font-family:宋体"}

[[\<Sysname\> reset rip 100 process   ]{lang="EN-US"}]{#struct_0_17903_10256_1119042258}

[Reset RIP process? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#2123596242 .myid}
[]{#_Toc404787713}[]{#struct_0_17903_10256_1945574386}[]{#_Toc313007775}

**RIP \-- RIP配置命令 \-- reset rip statistics**

------------------------------------------------------------------------

[**[reset rip statistics]{lang="EN-US"}**]{#struct_0_17903_10256_507605199}[命令用来清除指定]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的统计信息，便于在调试时重新记录统计数据。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1214337169}

[**[reset rip ]{lang="EN-US"}**]{#struct_0_17903_10256_1654556425}*[process-id]{lang="EN-US"}*[ **statistics**]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1879402701}

[[用户视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1034165689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_622054893}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_183220843}

[[network-operator]{lang="EN-US"}]{#struct_0_17903_10256_834124338}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1063327474}

[[mdc-operator]{lang="EN-US"}]{#struct_0_17903_10256_105853039}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x748673929}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_774610162}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655015178}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x2014454256}[清除进程号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset rip 100 statistics]{lang="EN-US"}]{#struct_0_17903_10256_x673065358}
:::

::: {#228405416 .myid}
[]{#_Toc404787714}[]{#struct_0_17903_10256_1718247272}

**RIP \-- RIP配置命令 \-- rip**

------------------------------------------------------------------------

[**[rip]{lang="EN-US"}**]{#struct_0_17903_10256_x434996732}[命令用来启动]{style="font-family:宋体"}[RIP]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[RIP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo rip]{lang="EN-US"}**]{#struct_0_17903_10256_x2029717055}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1122275358}

[**[rip]{lang="EN-US"}**[ \[ *process-id* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_17903_10256_x877364708}

[**[undo rip]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_17903_10256_822858890}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655080714}

[[系统没有运行]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x130276079}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x906626892}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17903_10256_181459681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1445588409}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1020717067}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_736214762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_68315750}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_113098093}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_17903_10256_1055265779}[：指定]{style="font-family:宋体"}[RIP]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[RIP]{lang="EN-US"}[位于公网中。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655146250}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须先启动]{style="font-family:宋体"}]{#struct_0_17903_10256_x2012190382}[RIP]{lang="EN-US"}[进程，才能配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的各种全局性参数，而配置与接口相关的参数时，可以不受这个限制。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[关闭]{style="font-family:宋体"}]{#struct_0_17903_10256_202515275}[RIP]{lang="EN-US"}[进程后，原来配置的接口参数也同时失效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_453316655}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1694230915}[启动]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[RIP]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x622613604}

[\[Sysname\] rip]{lang="EN-US"}

[\[Sysname-rip-1\]]{lang="EN-US"}
:::

::: {#-2086704271 .myid}
[]{#_Toc216497600}[]{#_Toc137543217}[]{#_Toc94930694}[]{#_Toc93984729}[]{#_Toc306797780}[]{#_Toc305059811}[]{#_Toc191726847}[]{#_Toc404787715}[]{#struct_0_17903_10256_x1776132246}[]{#_Toc313007777}[]{#_Toc33866022}[]{#_Toc286221281}[]{#_Toc286221283}[]{#_Toc286221284}[]{#_Toc286221285}[]{#_Toc286221286}[]{#_Toc286221287}[]{#_Toc286221288}[]{#_Toc286221289}[]{#_Toc286221290}[]{#_Toc286221291}[]{#_Toc286221292}[]{#_Toc286221293}[]{#_Toc286221294}[]{#_Toc286221295}[]{#_Toc286221296}[]{#_Toc286221297}[]{#_Toc286221298}[]{#_Toc286221299}[]{#_Toc286221300}[]{#_Toc286221301}[]{#_Toc286221302}[]{#_Toc286221303}[]{#_Toc286221304}[]{#_Toc286221305}[]{#_Toc286221307}[]{#_Toc286221310}[]{#_Toc286221311}[]{#_Toc286221316}[]{#_Toc286221317}[]{#_Toc286221320}[]{#_Toc286221321}[]{#_Toc286221322}[]{#_Toc286221323}[]{#_Toc286221324}[]{#_Toc286221325}[]{#_Toc286221326}[]{#_Toc286221327}[]{#_Toc286221328}[]{#_Toc286221329}[]{#_Toc286221330}[]{#_Toc286221331}[]{#_Toc286221332}[]{#_Toc286221333}[]{#_Toc286221334}[]{#_Toc286221335}[]{#_Toc286221337}[]{#_Toc286221338}[]{#_Toc286221339}[]{#_Toc286221340}[]{#_Toc286221342}[]{#_Toc286221343}[]{#_Toc286221344}[]{#_Toc286221345}[]{#_Toc286221346}[]{#_Toc286221347}[]{#_Toc286221348}[]{#_Toc286221349}[]{#_Toc286221350}[]{#_Toc286221351}[]{#_Toc286221352}[]{#_Toc286221353}[]{#_Toc286221354}[]{#_Toc286221355}[]{#_Toc286221356}[]{#_Toc286221357}[]{#_Toc286221358}[]{#_Toc286221359}[]{#_Toc286221360}[]{#_Toc286221361}[]{#_Toc286221362}[]{#_Toc286221363}[]{#_Toc286221364}[]{#_Toc286221365}[]{#_Toc286221366}[]{#_Toc286221368}[]{#_Toc286221369}[]{#_Toc286221370}[]{#_Toc286221371}[]{#_Toc286221374}[]{#_Toc286221376}[]{#_Toc286221377}[]{#_Toc286221378}[]{#_Toc286221379}[]{#_Toc286221380}[]{#_Toc286221381}[]{#_Toc286221382}[]{#_Toc286221383}[]{#_Toc286221384}[]{#_Toc286221385}[]{#_Toc286221386}[]{#_Toc286221387}[]{#_Toc286221388}[]{#_Toc286221389}[]{#_Toc286221390}[]{#_Toc286221392}[]{#_Toc286221393}[]{#_Toc286221394}[]{#_Toc286221395}[]{#_Toc286221400}[]{#_Toc286221401}[]{#_Toc286221402}[]{#_Toc286221403}[]{#_Toc286221404}[]{#_Toc286221405}[]{#_Toc286221406}[]{#_Toc286221407}[]{#_Toc286221408}[]{#_Toc286221409}[]{#_Toc286221410}[]{#_Toc286221411}[]{#_Toc286221412}[]{#_Toc286221413}[]{#_Toc286221414}[]{#_Toc286221415}[]{#_Toc286221416}[]{#_Toc286221417}[]{#_Toc286221418}[]{#_Toc286221419}[]{#_Toc286221420}[]{#_Toc286221421}[]{#_Toc286221422}[]{#_Toc286221423}[]{#_Toc286221425}[]{#_Toc286221426}[]{#_Toc286221427}[]{#_Toc286221428}[]{#_Toc286221429}[]{#_Toc286221430}[]{#_Toc286221431}[]{#_Toc286221432}[]{#_Toc286221433}[]{#_Toc286221434}[]{#_Toc286221435}[]{#_Toc286221437}[]{#_Toc286221438}[]{#_Toc286221439}[]{#_Toc286221440}[]{#_Toc286221441}[]{#_Toc286221442}[]{#_Toc286221443}[]{#_Toc286221444}[]{#_Toc286221445}[]{#_Toc286221446}[]{#_Toc286221447}[]{#_Toc286221448}[]{#_Toc286221449}[]{#_Toc286221450}[]{#_Toc286221451}[]{#_Toc286221452}[]{#_Toc286221453}[]{#_Toc286221454}[]{#_Toc286221455}[]{#_Toc286221456}[]{#_Toc286221457}[]{#_Toc286221458}[]{#_Toc286221459}[]{#_Toc286221460}[]{#_Toc286221462}[]{#_Toc286221463}[]{#_Toc286221464}[]{#_Toc286221465}[]{#_Toc286221466}[]{#_Toc286221467}[]{#_Toc286221468}[]{#_Toc286221469}[]{#_Toc286221470}[]{#_Toc286221472}[]{#_Toc286221474}[]{#_Toc286221475}[]{#_Toc286221476}[]{#_Toc286221477}[]{#_Toc286221478}[]{#_Toc286221479}[]{#_Toc286221480}[]{#_Toc286221481}[]{#_Toc286221482}[]{#_Toc286221483}[]{#_Toc286221484}[]{#_Toc286221485}[]{#_Toc286221486}[]{#_Toc286221487}[]{#_Toc286221490}[]{#_Toc286221491}[]{#_Toc137261626}[]{#_Toc137543199}[]{#_Toc137261627}[]{#_Toc137543200}[]{#_Toc137261628}[]{#_Toc137543201}[]{#_Toc137261629}[]{#_Toc137543202}[]{#_Toc137261630}[]{#_Toc137543203}[]{#_Toc137261631}[]{#_Toc137543204}[]{#_Toc137261632}[]{#_Toc137543205}[]{#_Toc137261633}[]{#_Toc137543206}[]{#_Toc137261634}[]{#_Toc137543207}[]{#_Toc137261635}[]{#_Toc137543208}[]{#_Toc137261636}[]{#_Toc137543209}[]{#_Toc137261637}[]{#_Toc137543210}[]{#_Toc137261638}[]{#_Toc137543211}[]{#_Toc137261639}[]{#_Toc137543212}[]{#_Toc137261640}[]{#_Toc137543213}[]{#_Toc137261641}[]{#_Toc137543214}[]{#_Toc137261642}[]{#_Toc137543215}[]{#_Toc286221493}[]{#_Toc286221494}[]{#_Toc286221495}[]{#_Toc286221496}[]{#_Toc286221497}[]{#_Toc286221498}[]{#_Toc286221499}[]{#_Toc286221500}[]{#_Toc286221501}[]{#_Toc286221502}[]{#_Toc286221503}[]{#_Toc286221504}[]{#_Toc286221505}[]{#_Toc286221506}[]{#_Toc286221507}[]{#_Toc286221511}[]{#_Toc286221512}

**RIP \-- RIP配置命令 \-- rip authentication-mode**

------------------------------------------------------------------------

[**[rip authentication-mode]{lang="EN-US"}**]{#struct_0_17903_10256_573422404}[命令用来配置]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[的验证方式及验证参数。]{style="font-family:宋体"}

[**[undo rip authentication-mode]{lang="EN-US"}**]{#struct_0_17903_10256_1655211786}[命令用来取消所有验证。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1457238191}

[**[rip authentication-mode]{lang="EN-US"}**]{#struct_0_17903_10256_x492975582}[ ]{lang="EN-US"}[{ ]{lang="EN-US" style="font-size:10.0pt"}**[md5]{lang="EN-US"}**[ { **rfc2082** ]{lang="EN-US"}[{ ]{lang="EN-US" style="font-size:10.0pt"}**[cipher]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:
10.0pt"}*[cipher-string]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **plain** *plain-string* ]{lang="EN-US"}[}]{lang="EN-US" style="font-size:10.0pt"}[ *key-id* \| **rfc2453** ]{lang="EN-US"}[{ ]{lang="EN-US" style="font-size:10.0pt"}**[cipher]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt"}*[cipher-string]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **plain** *plain-string* ]{lang="EN-US"}[}]{lang="EN-US" style="font-size:10.0pt"}[ } \| ]{lang="EN-US"}**[simple ]{lang="EN-US"}**[{ ]{lang="EN-US" style="font-size:10.0pt"}**[cipher]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt"}*[cipher-string]{lang="EN-US"}***[ ]{lang="EN-US"}**[\| **plain** *plain-string* ]{lang="EN-US"}[}]{lang="EN-US" style="font-size:10.0pt"}**[ ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo rip authentication-mode]{lang="EN-US"}**]{#struct_0_17903_10256_172917859}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2045716337}

[[接口没有配置]{style="font-family:宋体"}]{#struct_0_17903_10256_1854899751}[RIP-2]{lang="EN-US"}[的]{style="font-family:宋体"}[认证方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1596937289}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1859466200}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1205530929}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1655277322}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1512633619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_550414098}

[**[md5]{lang="EN-US"}**]{#struct_0_17903_10256_309662414}[：]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证方式。]{style="font-family:宋体"}

[**[rfc2082]{lang="EN-US"}**]{#struct_0_17903_10256_182919901}[：指定]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证报文使用]{style="font-family:宋体"}[RFC 2082]{lang="EN-US"}[规定的报文格式。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_17903_10256_665865525}[：]{style="font-family:宋体"}[表示输入的密码为密文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[cipher-string]{lang="EN-US"}*]{#struct_0_17903_10256_32882521}[：]{style="font-family:宋体"}[表示设置的密文密码，为]{style="font-family:宋体"}[33]{lang="EN-US"}[～]{style="font-family:宋体"}[53]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[plain]{lang="EN-US"}**]{#struct_0_17903_10256_x115900869}[：表示输入的密码为明文。]{style="font-family:宋体"}

[*[plain-string]{lang="EN-US"}*]{#struct_0_17903_10256_338481916}[：]{style="font-family:宋体"}[表示设置的明文密码]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[key-id]{lang="EN-US"}*]{#struct_0_17903_10256_1655342858}[：]{style="font-family:宋体"}[MD5 **rfc2082**]{lang="EN-US"}[验证标识符，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[rfc2453]{lang="EN-US"}**]{#struct_0_17903_10256_x1598800896}[：指定]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证报文使用]{style="font-family:宋体"}[RFC 2453]{lang="EN-US"}[规定的报文格式（]{style="font-family:宋体"}[IETF]{lang="EN-US"}[标准）。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_17903_10256_x1502695844}[：简单验证方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1406493081}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每次验证只支持一个验证字，新输入的验证字将覆盖旧验证字。]{style="font-family:宋体"}]{#struct_0_17903_10256_1519234771}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_17903_10256_2051200981}[RIP]{lang="EN-US"}[的版本为]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[时，虽然在接口视图下仍然可以配置验证方式，但由于]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[不支持认证，因此该配置不会生效]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的验证密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_17903_10256_1404770390}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1663247234}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_780043337}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1655408394}[在接口]{lang="EN-US" style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{lang="EN-US" style="font-family:宋体"}[RFC 2453]{lang="EN-US"}[格式的]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[明文验证，验证字为]{lang="EN-US" style="font-family:宋体"}[rose]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x515126931}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip version 2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip authentication-mode md5 rfc2453 plain rose]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1117996208}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1552113944}[在接口]{lang="EN-US" style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{lang="EN-US" style="font-family:宋体"}[RFC 2453]{lang="EN-US"}[格式的]{lang="EN-US" style="font-family:宋体"}[MD5]{lang="EN-US"}[明文验证，验证字为]{lang="EN-US" style="font-family:宋体"}[rose]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1172358948}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip version 2]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip authentication-mode md5 rfc2453 plain rose]{lang="EN-US"}

[[【命令参考】]{style="font-family:黑体"}]{#struct_0_17903_10256_408129614}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rip version]{lang="EN-US"}**]{#struct_0_17903_10256_1655473930}
:::

::::: {#12074768 .myid}
[]{#_Toc404787716}[]{#struct_0_17903_10256_1926416062}

**RIP \-- RIP配置命令 \-- rip bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image002.png){width="63" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_x899397084}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_155949671}
:::

[ ]{lang="EN-US"}

[**[rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_x52991765}[命令用来使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_2040827164}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_464973644}

[**[rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_692351897}

[**[undo rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_1293859431}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1654490890}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1245371243}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x487696558}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1351298661}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_577620525}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_52789778}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1099994170}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_815336844}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x2145655849}[支持采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的直连]{style="font-family:宋体"}[echo]{lang="EN-US"}[检测方式和非直连]{style="font-family:宋体"}[control]{lang="EN-US"}[检测方式。]{style="font-family:宋体"}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1654556426}[的邻居是单跳的概念，适合采用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[的]{style="font-family:宋体"}[echo]{lang="EN-US"}[单向检测方式，但是，经过多跳到达邻居时]{style="font-family:宋体"}[echo]{lang="EN-US"}[方式则会失效。]{style="font-family:宋体"}

[[由于]{style="font-family:宋体"}**[peer]{lang="EN-US"}**]{#struct_0_17903_10256_1879206093}[命令与邻居之间没有对应关系，]{style="font-family:宋体"}**[undo peer]{lang="EN-US"}**[操作并不能立刻删除邻居，因此不能立刻删除]{style="font-family:宋体"}[BFD]{lang="EN-US"}[会话。]{style="font-family:宋体"}

[[本命令与]{style="font-family:宋体"}**[rip bfd enable]{lang="EN-US"}**]{#struct_0_17903_10256_1785655522}**[ destination]{lang="ES"}**[命令互斥，不能同时使用。]{style="font-family:宋体"}[ ]{style="font-size:7.0pt"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1862843956}

[]{#struct_0_17903_10256_x230117224}[]{#_Toc292815538}[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_352617533}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1682715286}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1621684330}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1655015175}[在接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x2015175152}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] rip bfd enable]{lang="EN-US"}
:::::

::::: {#-1204928371 .myid}
[]{#_Toc313007779}[]{#_Toc404787717}[]{#struct_0_17903_10256_x249575844}[]{#_Toc331171746}

**RIP \-- RIP配置命令 \-- rip bfd enable destination**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image002.png){#图片 3 width="63" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_x1435847838}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x715702060}
:::

[ ]{lang="EN-US"}

[**[rip bfd enable]{lang="ES"}[ destination]{lang="EN-US"}**]{#struct_0_17903_10256_277277067}[命令用来使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[指定目的地址的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_x859297683}[命令用来关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体;color:#0096d6"}]{#struct_0_17903_10256_593936802}

[**[rip bfd enable destination ]{lang="ES"}***[ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_1655080711}

[**[undo rip bfd enable]{lang="ES"}**]{#struct_0_17903_10256_x130079471}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1413288425}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1673156035}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_2123257863}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_36024956}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x316384522}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1968855894}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1519662278}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655146247}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令只支持采用]{style="font-family:宋体"}]{#struct_0_17903_10256_x2011862701}[BFD]{lang="EN-US"}[的直连]{style="font-family:宋体"}[echo]{lang="EN-US"}[检测方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令与]{lang="EN-US" style="font-family:宋体"}**[rip bfd enable]{lang="EN-US"}**]{#struct_0_17903_10256_787167590}[命令互斥，不能同时使用。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[该命令指定了链路检测的目的地址，当到该目的地址的链路出现故障时，便不再从该接口收发任何]{style="font-family:宋体"}]{#struct_0_17903_10256_1207007276}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_113934784}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_77707113}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1282887708}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[指定目的地址]{style="font-family:宋体"}[202.38.165.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1356089248}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip bfd enable destination 202.38.165.1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1362406062}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1501949165}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[指定目的地址]{style="font-family:宋体"}[202.38.165.1]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1655211783}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip bfd enable destination 202.38.165.1]{lang="EN-US"}
:::::

::: {#-6935544 .myid}
[]{#_Toc404787718}[]{#struct_0_17903_10256_1457565871}

**RIP \-- RIP配置命令 \-- rip default-route**

------------------------------------------------------------------------

[**[rip default-route]{lang="EN-US"}**]{#struct_0_17903_10256_x2025136798}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口以指定度量值向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布一条缺省路由。]{style="font-family:宋体"}

[**[undo rip default-route]{lang="EN-US"}**]{#struct_0_17903_10256_x749575660}[命令用来取消配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[接口向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布缺省路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_441037667}

[**[rip default-route]{lang="EN-US"}**[ { { **only** \| **originate** } \[ **cost** *cost* \| **route-policy** *route-policy-name* \] \* \| **no-originate** }]{lang="EN-US"}]{#struct_0_17903_10256_492165426}

[**[undo rip default-route]{lang="EN-US"}**]{#struct_0_17903_10256_x1709028043}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655277319}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1512043798}[接口是否发布缺省路由以]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程配置为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1396201652}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x621174946}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1935158884}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_903526860}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1012082755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1860146875}

[**[only]{lang="EN-US"}**]{#struct_0_17903_10256_1055199058}[：配置只发送缺省路由，不发送普通路由。]{style="font-family:宋体"}

[**[originate]{lang="EN-US"}**]{#struct_0_17903_10256_1655342855}[：配置既发送普通路由，又发送缺省路由。]{style="font-family:宋体"}

[*[cost]{lang="EN-US"}*]{#struct_0_17903_10256_x1598080000}[：缺省路由的度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy ]{lang="EN-US"}***[route-policy-name]{lang="EN-US"}*]{#struct_0_17903_10256_1353604043}[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。只有当前路由器的路由表中有路由匹配]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[指定的路由策略时，才发送缺省路由。]{style="font-family:宋体"}

[**[no-originate]{lang="EN-US"}**]{#struct_0_17903_10256_496680726}[：配置只发送普通路由，不发布缺省路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_2004381080}

[[配置了发布缺省路由的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1593275543}[路由器不接收来自]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居的缺省路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2028972720}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_2071977413}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_675311171}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[以指定度量值]{style="font-family:宋体"}[2]{lang="EN-US"}[向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布一条缺省路由，而且只发送缺省路由，不发送普通路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_212112016}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip default-route only cost 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1703945976}[指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[以指定度量值]{style="font-family:宋体"}[4]{lang="EN-US"}[向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居既发布缺省路由，而且发送普通路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1655408391}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip default-route originate cost 4]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x514930323}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1542073597}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[以指定度量值]{style="font-family:宋体"}[2]{lang="EN-US"}[向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居发布一条缺省路由，而且只发送缺省路由，不发送普通路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1145448305}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip default-route only cost 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1609242582}[指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[以指定度量值]{style="font-family:宋体"}[2]{lang="EN-US"}[向]{style="font-family:宋体"}[RIP]{lang="EN-US"}[邻居既发布缺省路由，而且发送普通路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_277742029}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip default-route originate cost 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_471083264}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[default-route]{lang="EN-US"}**]{#struct_0_17903_10256_1655473927}
:::

::: {#99857971 .myid}
[]{#_Toc313007780}[]{#_Toc404787719}[]{#struct_0_17903_10256_1926350525}[]{#_Toc331171748}

**RIP \-- RIP配置命令 \-- rip enable**

------------------------------------------------------------------------

[**[rip]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_17903_10256_x935250939}[命令用来在接口上使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo rip enable]{lang="EN-US"}**]{#struct_0_17903_10256_x1791696402}[命令用来在接口上关闭]{style="font-family:宋体"}[RIP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x154613632}

[**[rip]{lang="EN-US"}**[ *process-id* **enable** \[ **exclude-subip** \]]{lang="EN-US"}]{#struct_0_17903_10256_1299027191}

[**[undo rip enable]{lang="EN-US"}**]{#struct_0_17903_10256_1454951743}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_442871635}

[[接口上没有使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1080702479}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_80711138}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1654490887}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1245698924}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1362142510}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1561916948}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x771116392}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_1583136148}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[exclude-subip]{lang="EN-US"}**]{#struct_0_17903_10256_1387946124}[：不包括接口的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果未指定本参数，将包括接口的从]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_2076139391}

[[本命令的优先级高于]{style="font-family:宋体"}**[network]{lang="EN-US"}**]{#struct_0_17903_10256_344460985}[命令。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_692606220}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1654556423}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1879009485}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1257170036}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip 100 enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1713472810}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1537074325}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1494749556}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip 100 enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x705151266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_17903_10256_x1060936329}
:::

::: {#-151194004 .myid}
[]{#_Toc404787720}[]{#struct_0_17903_10256_1655015176}

**RIP \-- RIP配置命令 \-- rip input**

------------------------------------------------------------------------

[**[rip input]{lang="EN-US"}**]{#struct_0_17903_10256_x2015371760}[命令用来允许接口接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo rip input]{lang="EN-US"}**]{#struct_0_17903_10256_x1944068824}[命令用来禁止接口接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_252802272}

[**[rip input]{lang="EN-US"}**]{#struct_0_17903_10256_x1860956014}

[**[undo ]{lang="EN-US"}**]{#struct_0_17903_10256_x2023960283}**[rip input]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_35016793}

[[允许接口接收]{style="font-family:宋体"}]{#struct_0_17903_10256_950218080}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655080712}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x129882863}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x472323312}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1044543162}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x973549934}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1415976724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x257824688}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1830346583}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1193009799}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo rip input]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1655146248}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x2012714669}[禁止接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1816913433}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] undo rip input]{lang="EN-US"}
:::

::: {#394322698 .myid}
[]{#_Toc313007781}[]{#_Toc404787721}[]{#struct_0_17903_10256_x1063147988}[]{#_Toc331171750}[]{#_Toc328746902}[]{#_Toc322698694}

**RIP \-- RIP配置命令 \-- rip max-packet-length**

------------------------------------------------------------------------

[**[rip max-packet-length]{lang="EN-US"}**]{#struct_0_17903_10256_1223331306}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度。]{style="font-family:宋体"}

[**[undo rip max-packet-length]{lang="EN-US"}**]{#struct_0_17903_10256_91334814}[命令用来恢复]{style="font-family:宋体"}[缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x845573721}

[**[rip max-packet-length ]{lang="EN-US"}***[value]{lang="EN-US"}*]{#struct_0_17903_10256_1074896018}

[**[undo rip max-packet-length]{lang="EN-US"}**]{#struct_0_17903_10256_1655211784}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1457369263}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1254861457}[报文的最大长度为]{style="font-family:宋体"}[512]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1856883435}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1616853447}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_31569535}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x200296646}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x691611150}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1401048624}

[*[value]{lang="EN-US"}*]{#struct_0_17903_10256_1655277320}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度，取值范围为]{style="font-family:宋体"}[32]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1512502547}

[[如果配置值大于接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_17903_10256_941890375}[，则报文的最大长度为接口]{style="font-family:宋体"}[MTU]{lang="EN-US"}[。]{style="font-family:宋体"}

[[由于不同厂商对]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x828717494}[报文最大长度的支持情况不同，要谨慎使用本特性，以免出现不兼容的情况。]{style="font-family:宋体"}

[[在配置认证的情况下，如果配置不当可能会造成报文无法发送，建议用户按照下面进行配置：]{style="font-family:宋体"}]{#struct_0_17903_10256_1876593897}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[简单验证方式时，]{style="font-family:宋体"}]{#struct_0_17903_10256_x1861506808}[RIP]{lang="EN-US"}[报文的最大长度不小于]{style="font-family:宋体"}[52]{lang="EN-US"}[字节；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_17903_10256_283503731}[验证方式（使用]{style="font-family:宋体"}[RFC 2453]{lang="EN-US"}[规定的报文格式）时，]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度不小于]{style="font-family:宋体"}[56]{lang="EN-US"}[字节；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_17903_10256_739158730}[验证方式（使用]{style="font-family:宋体"}[RFC 2082]{lang="EN-US"}[规定的报文格式）时，]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度不小于]{style="font-family:宋体"}[72]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_201372447}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1655342856}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1597883392}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x816720510}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip max-packet-length 1024]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_861328065}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1743986418}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大长度为]{style="font-family:宋体"}[1024]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_891717387}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip max-packet-length 1024]{lang="EN-US"}
:::

::: {#1955035990 .myid}
[]{#_Toc404787722}[]{#struct_0_17903_10256_265863425}

**RIP \-- RIP配置命令 \-- rip metricin**

------------------------------------------------------------------------

[**[rip metricin]{lang="EN-US"}**]{#struct_0_17903_10256_x1537522072}[命令用来配置接口接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由时的附加度量值。]{style="font-family:宋体"}

[**[undo rip metricin]{lang="EN-US"}**]{#struct_0_17903_10256_1655408392}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x514733715}

[**[rip metricin ]{lang="EN-US"}**]{#struct_0_17903_10256_x374246163}[\[ **route-policy** *route-policy-name* \] *value*]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_17903_10256_1635499385}**[rip metricin]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1316111579}

[[接口接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1577881710}[路由时的附加度量值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x939540636}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1736973709}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_888389399}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1655473928}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1925891773}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1960859784}

[**[route-policy ]{lang="EN-US"}**]{#struct_0_17903_10256_86952391}*[route-policy-name]{lang="EN-US"}*[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。对满足特定条件的路由设置附加度量值。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_17903_10256_x1206702008}[：接收附加度量值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x494448029}

[[当接口收到一条合法的]{style="font-family:宋体"}]{#struct_0_17903_10256_x1080327857}[RIP]{lang="EN-US"}[路由，在将其加入路由表前，附加度量值会被加到该路由上。因此，增加接口的接收附加度量值，该接口收到的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的度量值也会相应增加，当附加度量值与原路由度量值之和大于]{style="font-family:宋体"}[16]{lang="EN-US"}[，该条路由的度量值取]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[通过指定]{style="font-family:宋体"}]{#struct_0_17903_10256_x1994849716}**[route-policy]{lang="EN-US"}**[参数，可应用路由策略对接口接收的特定路由设置附加度量值：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x311714915}[]{#_Toc138041268}[]{#_Toc157826816}**[apply cost]{lang="EN-US"}**[命令设置了匹配路由的附加度量值，则匹配路由的附加度量值取]{lang="EN-US" style="font-family:宋体"}**[apply cost]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数设置的值，不匹配路由的附加度量值取本命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数所设的值。需要注意的是，本命令不支持通过]{lang="EN-US" style="font-family:宋体"}**[apply cost]{lang="EN-US"}**[命令中的]{lang="EN-US" style="font-family:宋体"}**[+]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-]{lang="EN-US"}**[关键字对接口接收]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的附加度量值进行增加、减少的设置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1654490888}**[apply cost]{lang="EN-US"}**[命令设置路由的附加度量值，则所有接收路由的附加度量值都取本命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数所设的值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1245895532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_16282008}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1687561253}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[接收的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由附加度量值进行设置。其中，]{style="font-family:宋体"}[1.0.0.0/8]{lang="EN-US"}[网段路由的附加度量值设置为]{style="font-family:宋体"}[6]{lang="EN-US"}[，其它网段路由的附加度量值设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1232268132}

[\[Sysname\] ip prefix-list 123 permit 1.0.0.0 8]{lang="EN-US"}

[\[Sysname\] route-policy abc permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] if-match ip address prefix-list 123]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] apply cost 6]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip metricin route-policy abc 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1003308494}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1638085686}[对接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[接收的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由附加度量值进行设置。其中，]{style="font-family:宋体"}[1.0.0.0/8]{lang="EN-US"}[网段路由的附加度量值设置为]{style="font-family:宋体"}[6]{lang="EN-US"}[，其它网段路由的附加度量值设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1654556424}

[\[Sysname\] ip prefix-list 123 permit 1.0.0.0 8]{lang="EN-US"}

[\[Sysname\] route-policy abc permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] if-match ip address prefix-list 123]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] apply cost 6]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip metricin route-policy abc 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1879337165}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply cost]{lang="EN-US" style="font-size:10.0pt"}**]{#struct_0_17903_10256_1015643183}[（]{style="font-family:宋体"}[三层技术]{lang="EN-US" style="font-size:10.0pt;
font-family:宋体"}[-IP]{lang="EN-US" style="font-size:10.0pt"}[路由命令参考]{lang="EN-US" style="font-size:10.0pt;font-family:宋体"}[/]{lang="EN-US"}[路由策略]{lang="EN-US" style="font-size:10.0pt;font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#-158630844 .myid}
[]{#_Toc404787723}[]{#struct_0_17903_10256_133867290}[]{#_Toc313007782}

**RIP \-- RIP配置命令 \-- rip metricout**

------------------------------------------------------------------------

[**[rip metricout]{lang="EN-US"}**]{#struct_0_17903_10256_x2035024369}[命令用来配置接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由时的附加度量值。]{style="font-family:宋体"}

[**[undo rip metricout]{lang="EN-US"}**]{#struct_0_17903_10256_1704771258}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1680906270}

[**[rip metricout ]{lang="EN-US"}**]{#struct_0_17903_10256_1655015173}[\[ **route-policy** *route-policy-name* \] *value*]{lang="EN-US"}

[**[undo ]{lang="EN-US"}**]{#struct_0_17903_10256_x2015044080}**[rip metricout]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x241123744}

[[接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1619157972}[路由时的附加度量值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x181375072}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x963277929}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2001448739}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1393796228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_475414916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655080709}

[**[route-policy ]{lang="EN-US"}**]{#struct_0_17903_10256_x130603760}*[route-policy-name]{lang="EN-US"}*[：路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。对满足特定条件的路由设置附加度量值。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_17903_10256_x108046478}[：发送附加度量值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_1036179889}

[[当发布一条]{style="font-family:宋体"}]{#struct_0_17903_10256_1658078513}[RIP]{lang="EN-US"}[路由时，附加度量值会在发布该路由之前附加在这条路由上。因此，增加一个接口的发送附加度量值，该接口发送的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的度量值也会相应增加。]{style="font-family:宋体"}

[[通过指定]{style="font-family:宋体"}]{#struct_0_17903_10256_x1186543127}**[route-policy]{lang="EN-US"}**[参数，可应用路由策略对接口发布的特定路由设置附加度量值：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x2146556628}**[apply cost]{lang="EN-US"}**[命令设置了匹配路由的附加度量值，则匹配路由的附加度量值取]{lang="EN-US" style="font-family:宋体"}**[apply cost]{lang="EN-US"}**[命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数设置的值，不匹配路由的附加度量值取本命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数所设的值。需要注意的是，本命令不支持通过]{lang="EN-US" style="font-family:宋体"}**[apply cost]{lang="EN-US"}**[命令中的]{lang="EN-US" style="font-family:宋体"}**[+]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[-]{lang="EN-US"}**[关键字对接口发布]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="EN-US"}[路由的附加度量值进行增加、减少的设置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有通过]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_2052276555}**[apply cost]{lang="EN-US"}**[命令设置路由的附加度量值，则所有发布路由的附加度量值都取本命令]{lang="EN-US" style="font-family:宋体"}*[value]{lang="EN-US"}*[参数所设的值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1655146245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x2011993773}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1514039293}[对接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由附加度量值进行设置。其中，]{style="font-family:宋体"}[1.0.0.0/8]{lang="EN-US"}[网段路由的附加度量值设置为]{style="font-family:宋体"}[6]{lang="EN-US"}[，其它网段路由的附加度量值设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1064864358}

[\[Sysname\] ip prefix-list 123 permit 1.0.0.0 8]{lang="EN-US"}

[\[Sysname\] route-policy abc permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] if-match ip address prefix-list 123]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] apply cost 6]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip metricout route-policy abc 2]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1897233997}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_696777493}[对接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由附加度量值进行设置。其中，]{style="font-family:宋体"}[1.0.0.0/8]{lang="EN-US"}[网段路由的附加度量值设置为]{style="font-family:宋体"}[6]{lang="EN-US"}[，其它网段路由的附加度量值设置为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1655211781}

[\[Sysname\] ip prefix-list 123 permit 1.0.0.0 8]{lang="EN-US"}

[\[Sysname\] route-policy abc permit node 0]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] if-match ip address prefix-list 123]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] apply cost 6]{lang="EN-US"}

[\[Sysname-route-policy-abc-10\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip metricout route-policy abc 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1457696943}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply cost]{lang="EN-US"}**]{#struct_0_17903_10256_1473866025}[（]{style="font-family:宋体"}[三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[路由策略]{lang="EN-US" style="font-family:宋体"}[）]{style="font-family:宋体"}
:::

::: {#119414467 .myid}
[]{#_Toc313007783}[]{#_Toc404787724}[]{#struct_0_17903_10256_x124194909}[]{#_Toc331171753}[]{#_Toc328746903}[]{#_Toc322698695}

**RIP \-- RIP配置命令 \-- rip mib-binding**

------------------------------------------------------------------------

[**[rip mib-binding]{lang="EN-US"}**]{#struct_0_17903_10256_x2041500055}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo rip mib-binding]{lang="EN-US"}**]{#struct_0_17903_10256_x590719223}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x656274222}

[**[rip mib-binding]{lang="EN-US"}**[ *process-id*]{lang="EN-US"}]{#struct_0_17903_10256_x1363206280}

[**[undo rip mib-binding]{lang="EN-US"}**]{#struct_0_17903_10256_1655277317}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1512437014}

[[MIB]{lang="EN-US"}]{#struct_0_17903_10256_x1037338308}[绑定在进程号最小的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_89612886}

[[系统视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1740070910}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1267495510}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1837956407}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_629680830}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_2039977816}

[*[process-id]{lang="EN-US"}*]{#struct_0_17903_10256_1655342853}[：]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1598211072}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1643171097}*[process-id]{lang="FR"}*[不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:
宋体"}[RIP]{lang="FR"}[进程绑定命令时将会提示]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="EN-US"}[进程不存在]{lang="EN-US" style="font-family:宋体"}[，]{lang="EN-US" style="font-family:宋体"}[无法完成配置。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[如果配置了]{style="font-family:宋体"}]{#struct_0_17903_10256_x2041726904}[RIP]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[，]{style="font-family:宋体"}[若删除]{style="font-family:宋体"}*[process-id]{lang="FR"}*[对应的]{style="font-family:宋体"}[RIP]{lang="FR"}[进程]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[则同时删除]{style="font-family:宋体"}[RIP]{lang="FR"}[进程绑定]{style="font-family:宋体"}[MIB]{lang="FR"}[配置，]{style="font-family:宋体"}[MIB]{lang="EN-US"}[绑定到进程号最小的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1781505921}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x362330271}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[进程]{style="font-family:宋体"}[100]{lang="EN-US"}[绑定]{style="font-family:宋体"}[MIB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1105583894}

[\[Sysname\] rip mib-binding 100]{lang="EN-US"}
:::

::: {#607832449 .myid}
[]{#_Toc404787725}[]{#struct_0_17903_10256_659494019}

**RIP \-- RIP配置命令 \-- rip output**

------------------------------------------------------------------------

[**[rip output]{lang="EN-US"}**]{#struct_0_17903_10256_1402223559}[命令用来允许接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo rip output]{lang="EN-US"}**]{#struct_0_17903_10256_1655408389}[命令用来禁止接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x514406036}

[**[rip output]{lang="EN-US"}**]{#struct_0_17903_10256_1961212885}

[**[undo rip output]{lang="EN-US"}**]{#struct_0_17903_10256_x687063748}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1260769126}

[[允许接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1123540176}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_529838064}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x891009072}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1506937803}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1655473925}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1926219453}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x181842536}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1692181447}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_529333970}[禁止接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x816304551}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] undo rip output]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1103780691}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1289444166}[禁止接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1654490885}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] undo rip output]{lang="EN-US"}
:::

::: {#-518574219 .myid}
[]{#_Toc404787726}[]{#struct_0_17903_10256_1354456017}[]{#_Toc375236008}[]{#_Toc328746904}[]{#_Toc322698696}

**RIP \-- RIP配置命令 \-- rip output-delay**

------------------------------------------------------------------------

[**[rip output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_1354390481}[命令用来配置接口下]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的发送速率。]{style="font-family:宋体"}

[**[undo rip output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_1119954220}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1132123752}

[**[rip output-delay]{lang="EN-US"}***[ time]{lang="EN-US"}***[ count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_17903_10256_x1374951631}

[**[undo rip output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_349937145}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1722473260}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1375017167}[报文的发包速率由进程全局的配置决定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x194217629}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1847158244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1187405203}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1374820559}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x839376635}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_1607203071}

[*[time]{lang="EN-US"}*]{#struct_0_17903_10256_x1374886095}[：接口发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[count]{lang="EN-US"}*]{#struct_0_17903_10256_1778877000}[：接口一次发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的最大个数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1417247493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1375213775}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1888448465}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[配置发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[6]{lang="EN-US"}[个]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1375279311}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip output-delay 30 count 6]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x975524407}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_316331212}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[配置发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[毫秒，一次最多发送]{style="font-family:宋体"}[6]{lang="EN-US"}[个]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1375082703}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip output-delay 30 count 6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_97229046}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[output-delay]{lang="EN-US"}**]{#struct_0_17903_10256_605246120}
:::

::: {#350030475 .myid}
[]{#_Toc404787727}[]{#struct_0_17903_10256_x1245567852}

**RIP \-- RIP配置命令 \-- rip poison-reverse**

------------------------------------------------------------------------

[**[rip poison-reverse]{lang="EN-US"}**]{#struct_0_17903_10256_413959794}[命令用来使能毒性逆转功能。]{style="font-family:宋体"}

[**[undo rip poison-reverse]{lang="EN-US"}**]{#struct_0_17903_10256_2023203438}[命令用来关闭毒性逆转功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_584877293}

[**[rip poison-reverse]{lang="EN-US"}**]{#struct_0_17903_10256_x810661306}

[**[undo rip poison-reverse]{lang="EN-US"}**]{#struct_0_17903_10256_470376004}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x147779761}

[[毒性逆转功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_17903_10256_1654556421}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1879140557}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x517917459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x486062185}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x587965752}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_387812432}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1794178772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1262990266}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x904244569}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置对]{style="font-family:宋体"}[RIP]{lang="EN-US"}[更新报文进行毒性逆转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1655015174}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip poison-reverse]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x2015240688}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1128588918}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置对]{style="font-family:宋体"}[RIP]{lang="EN-US"}[更新报文进行毒性逆转。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x482590023}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip poison-reverse]{lang="EN-US"}
:::

::::: {#1597262024 .myid}
[]{#_Toc404787728}[]{#struct_0_17903_10256_x1388707861}[]{#_Toc363978470}[]{#_Toc356288300}[]{#_Toc356229217}

**RIP \-- RIP配置命令 \-- rip primary-path-detect bfd echo**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image002.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_1362832139}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x1388773397}
:::

**[ ]{lang="EN-US"}**

[**[rip primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_17903_10256_1775855463}[命令用来使能]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[**[undo rip primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_17903_10256_941396437}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1388838933}

[**[rip primary-path-detect bfd echo]{lang="EN-US"}**]{#struct_0_17903_10256_x1970316859}

[**[undo rip primary-path-detect bfd]{lang="EN-US"}**]{#struct_0_17903_10256_x1388380181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x447601414}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x2139257302}[协议中主用链路的]{style="font-family:宋体"}[BFD Echo]{lang="EN-US"}[检测功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1388445717}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_499392990}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1999513838}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1388904472}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x349397094}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x58537489}

[[配置本功能后，]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1388970008}[协议的快速重路由特性中的主用链路将使用]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）进行检测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1581476367}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1389035544}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x883181715}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1389101080}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] fast-reroute route-policy frr]{lang="EN-US"}

[\[Sysname-rip-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip primary-path-detect bfd echo]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_2129770057}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1388642328}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议快速重路由特性中主用链路使能]{style="font-family:宋体"}[BFD]{lang="EN-US"}[（]{style="font-family:宋体"}[Echo]{lang="EN-US"}[方式）检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1388707864}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] fast-reroute route-policy frr]{lang="EN-US"}

[\[Sysname-rip-1\] quit]{lang="EN-US"}

[\[Sysname\] bfd echo-source-ip 1.1.1.1]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip primary-path-detect bfd echo]{lang="EN-US"}
:::::

::: {#930114426 .myid}
[]{#_Toc404787729}[]{#struct_0_17903_10256_1971930313}[]{#_Toc216497601}[]{#_Toc137543218}[]{#_Toc33866027}

**RIP \-- RIP配置命令 \-- rip split-horizon**

------------------------------------------------------------------------

[**[rip split-horizon]{lang="EN-US"}**]{#struct_0_17903_10256_x968936479}[命令用来使能水平分割功能。]{style="font-family:宋体"}

[**[undo rip split-horizon]{lang="EN-US"}**]{#struct_0_17903_10256_x1269768890}[命令用来关闭水平分割功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x590212517}

[**[rip split-horizon]{lang="EN-US"}**]{#struct_0_17903_10256_1655080710}

[**[undo]{lang="EN-US"}[ rip split-horizon]{lang="EN-US"}**]{#struct_0_17903_10256_x130013935}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x496544181}

[[水平分割功能处于使能状态。]{style="font-family:宋体"}]{#struct_0_17903_10256_x86509446}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x759500086}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1741156977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_256083993}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1293292962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x828477509}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x90796867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，为了防止路由环路的出现，水平分割是必要的，因此，建议不要关闭水平分割。当因为特殊需要，如为保证协议的正确执行，需要关闭水平分割时，请一定要确认是否必要。]{style="font-family:宋体"}]{#struct_0_17903_10256_1655146246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在帧中继和]{style="font-family:宋体"}]{#struct_0_17903_10256_x2011797165}[X.25]{lang="EN-US"}[等]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[（]{style="font-family:宋体"}[Non-Broadcast Multi-Access]{lang="EN-US"}[，非广播多路访问）网络中，当主接口和点到多点子接口配置了多条虚电路时，为了保证路由信息的正确传播，需要关闭水平分割功能。关于帧中继和]{style="font-family:宋体"}[X.25]{lang="EN-US"}[的详细信息，请参见"二层技术]{style="font-family:宋体"}[-]{lang="EN-US"}[广域网接入配置指导"中的"帧中继"和"]{style="font-family:宋体"}[LAPB]{lang="EN-US"}[和]{style="font-family:宋体"}[X.25]{lang="EN-US"}["。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时使能了水平分割和毒性逆转，则只有毒性逆转功能生效。]{style="font-family:宋体"}]{#struct_0_17903_10256_x2128105773}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1979855636}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1592365521}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x25971042}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上配置水平分割。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1470886574}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip split-horizon]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_369618854}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1655211782}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[上配置水平分割。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1457500335}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip split-horizon]{lang="EN-US"}
:::

::: {#-418720428 .myid}
[]{#_Toc404787730}[]{#struct_0_17903_10256_x1225579411}[]{#_Toc216497602}[]{#_Toc137543219}[]{#_Toc94930696}[]{#_Toc93984731}[]{#_Toc60036163}[]{#_Toc53707107}[]{#_Toc52063188}[]{#_Toc50413975}[]{#_Toc50413895}[]{#_Toc50413794}

**RIP \-- RIP配置命令 \-- rip summary-address**

------------------------------------------------------------------------

[**[rip summary-address]{lang="EN-US"}**]{#struct_0_17903_10256_1486110862}[命令用来配置发布一条聚合路由。]{style="font-family:宋体"}

[**[undo rip summary-address]{lang="EN-US"}**]{#struct_0_17903_10256_995391317}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x403053004}

[**[rip summary-address]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_17903_10256_1793293283}

[**[undo rip summary-address]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_17903_10256_x536741099}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1936429535}

[[没有配置发布一条聚合路由。]{style="font-family:宋体"}]{#struct_0_17903_10256_1655277318}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1511978262}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_1792321755}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2129009609}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x258686720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x861522137}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1292826022}

[*[ip-address]{lang="EN-US"}*]{#struct_0_17903_10256_x872241709}[：聚合路由的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_17903_10256_x104952510}[：聚合路由的网络掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_17903_10256_1655342854}[：聚合路由的网络掩码，点分十进制格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1598014464}

[[该功能仅在自动路由聚合功能被关闭时才能生效。]{style="font-family:宋体"}]{#struct_0_17903_10256_x1091455413}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1200261096}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x2118274247}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1196074546}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[发布一个聚合本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_734210845}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip summary-address 10.0.0.0 255.255.255.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1606430970}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1655408390}[配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[在接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[发布一个聚合本地]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x514864787}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip summary-address 10.0.0.0 255.255.255.0]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1563338132}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[summary]{lang="EN-US"}**]{#struct_0_17903_10256_762031891}
:::

::::: {#930386470 .myid}
[]{#_Toc404787731}[]{#struct_0_17903_10256_x1375279310}[]{#_Toc375236014}[]{#_Toc328746905}[]{#_Toc322698697}

**RIP \-- RIP配置命令 \-- rip triggered**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_590559534}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x1375082702}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[rip triggered]{lang="EN-US"}**]{#struct_0_17903_10256_x1468854895}[命令用来使能]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo rip triggered]{lang="EN-US"}**]{#struct_0_17903_10256_x698681106}[命令用来关闭]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x422989365}

[**[rip triggered]{lang="EN-US"}**]{#struct_0_17903_10256_x1375148238}

[**[undo rip triggered]{lang="EN-US"}**]{#struct_0_17903_10256_x1906462902}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_2079493099}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_x1374427342}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_2028228928}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_498060275}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1968539140}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1374492878}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x698115428}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1178500236}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_x1374951633}[功能只能运行在]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、帧中继、]{style="font-family:宋体"}[X.25]{lang="EN-US"}[链路层协议上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1512736559}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1028723212}[使能]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1375017169}

[\[Sysname\] interface serial 2/1/0]{lang="EN-US"}

[\[Sysname-Serial2/1/0\] rip triggered]{lang="EN-US"}
:::::

::: {#867534780 .myid}
[]{#_Toc404787732}[]{#struct_0_17903_10256_x91439409}[]{#_Toc216497604}[]{#_Toc137543221}[]{#_Toc33866028}[]{#_Toc286221520}[]{#_Toc286221523}[]{#_Toc286221524}[]{#_Toc286221525}[]{#_Toc286221526}[]{#_Toc286221527}[]{#_Toc286221528}[]{#_Toc286221529}[]{#_Toc286221530}[]{#_Toc286221531}[]{#_Toc286221532}[]{#_Toc286221533}[]{#_Toc286221534}[]{#_Toc286221535}[]{#_Toc286221536}[]{#_Toc286221537}[]{#_Toc286221540}

**RIP \-- RIP配置命令 \-- rip version**

------------------------------------------------------------------------

[**[rip version]{lang="EN-US"}**]{#struct_0_17903_10256_x371350351}[命令用来配置接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[undo rip version]{lang="EN-US"}**]{#struct_0_17903_10256_x1611070941}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_707004931}

[**[rip version ]{lang="EN-US"}**[{ **1** \| **2** \[ **broadcast** \| **multicast** \] }]{lang="EN-US"}]{#struct_0_17903_10256_1655473926}

[**[undo]{lang="EN-US"}[ rip version]{lang="EN-US"}**]{#struct_0_17903_10256_1926284989}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1238212178}

[[没有配置接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1865955247}[版本。接口只能发送]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播报文，可以接收]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文、]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_1562614192}

[[接口视图]{style="font-family:宋体"}]{#struct_0_17903_10256_x1256839682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_373979043}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1270942908}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1732779286}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1901705986}

[**[1]{lang="EN-US"}**]{#struct_0_17903_10256_1654490886}[：接口运行]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议的版本为]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_17903_10256_x1245764460}[：接口运行]{style="font-family:宋体"}[RIP]{lang="EN-US"}[协议的版本为]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[ **broadcast** \| **multicast** \]]{lang="EN-US"}]{#struct_0_17903_10256_x878469832}[：]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[报文的发送方式为广播方式（]{style="font-family:宋体"}**[broadcast]{lang="EN-US"}**[）还是组播方式（]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[），缺省为组播方式（]{style="font-family:宋体"}**[multicast]{lang="EN-US"}**[）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_241887501}

[[如果接口上配置了]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1474516334}[版本，以接口配置的为准；如果接口上没有配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本，接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本以全局配置的为准。]{style="font-family:宋体"}

[[当接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1309601797}[版本为]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{lang="EN-US" style="font-family:宋体"}[RIP-1]{lang="EN-US"}]{#struct_0_17903_10256_1295816778}[广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收]{style="font-family:宋体"}]{#struct_0_17903_10256_163201248}[RIP-1]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文]{style="font-family:宋体"}

[[当接口运行在]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_712900168}[广播方式时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{lang="EN-US" style="font-family:宋体"}[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_1654556422}[广播报文]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收]{style="font-family:宋体"}]{#struct_0_17903_10256_1878943949}[RIP-1]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文、]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文]{style="font-family:宋体"}

[[当接口运行在]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_x191780737}[组播方式时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[发送]{lang="EN-US" style="font-family:宋体"}[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_1148855883}[组播报文]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[接收]{style="font-family:宋体"}]{#struct_0_17903_10256_1999234309}[RIP-2]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1864969051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_2000298605}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1355760641}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[以广播方式发送]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x717637818}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] rip version 2 broadcast]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1660962682}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1792001054}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[以广播方式发送]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1271988158}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] rip version 2 broadcast]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_576110642}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[version]{lang="EN-US"}**]{#struct_0_17903_10256_1474166348}
:::

::: {#-420464374 .myid}
[]{#_Toc216497606}[]{#_Toc137543223}[]{#_Toc33866030}[]{#_Toc404787733}[]{#struct_0_17903_10256_1315172494}[]{#_Toc313007788}[]{#_Toc50413797}[]{#_Toc286221542}[]{#_Toc286221543}[]{#_Toc286221544}[]{#_Toc286221545}[]{#_Toc286221546}[]{#_Toc286221547}[]{#_Toc286221548}[]{#_Toc286221549}[]{#_Toc286221550}[]{#_Toc286221551}[]{#_Toc286221552}[]{#_Toc286221553}[]{#_Toc286221554}[]{#_Toc286221555}[]{#_Toc286221556}[]{#_Toc286221557}[]{#_Toc286221558}[]{#_Toc286221562}[]{#_Toc286221563}[]{#_Toc286221564}[]{#_Toc286221565}[]{#_Toc286221570}

**RIP \-- RIP配置命令 \-- silent-interface**

------------------------------------------------------------------------

[**[silent-interface]{lang="EN-US"}**]{#struct_0_17903_10256_1325669321}[命令用来配置接口工作在抑制状态，即接]{style="font-family:宋体"}[口只接收]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文而不发送]{style="font-family:宋体"}[RIP]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[**[undo silent-interface]{lang="EN-US"}**]{#struct_0_17903_10256_1272466703}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x717572282}

[**[silent-interface]{lang="EN-US"}**]{#struct_0_17903_10256_145615183}[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}

[**[undo silent-interface]{lang="EN-US"}**]{#struct_0_17903_10256_756133974}[ { *interface-type interface-number* \| **all** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1452996181}

[[允许所有接口发送]{style="font-family:宋体"}]{#struct_0_17903_10256_x1910532465}[RIP]{lang="EN-US"}[报文]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x645315570}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1391480012}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1917282161}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1766873789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x717506746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x615138377}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_17903_10256_52524782}[：接口类型和编号。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_17903_10256_793360812}[：抑制所有接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x165634231}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_x1871776785}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_1547128048}[将所有接口设置为抑制状态，随后激活指定接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_342026386}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] silent-interface all]{lang="EN-US"}

[\[Sysname-rip-100\] undo silent-interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-rip-100\] network 131.108.0.0]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_17903_10256_1250265323}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x717441210}[将所有接口设置为抑制状态，随后激活指定接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1412014590}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] silent-interface all]{lang="EN-US"}

[\[Sysname-rip-100\] undo silent-interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-rip-100\] network 131.108.0.0]{lang="EN-US"}
:::

::: {#-1230299672 .myid}
[]{#_Toc404787734}[]{#struct_0_17903_10256_1511647763}

**RIP \-- RIP配置命令 \-- summary**

------------------------------------------------------------------------

[**[summary]{lang="EN-US"}**]{#struct_0_17903_10256_1063745911}[命令用来使能]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[自动路由聚合功能，聚合后的路由以使用自然掩码的路由形式发布，减小了路由表的规模。]{style="font-family:宋体"}

[**[undo summary]{lang="EN-US"}**]{#struct_0_17903_10256_837130867}[命令用来关闭自动路由聚合功能，以便将所有子网路由广播出去。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x398677478}

[**[summary]{lang="EN-US"}**]{#struct_0_17903_10256_2028313347}

[**[undo summary]{lang="EN-US"}**]{#struct_0_17903_10256_2124579977}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x717375674}

[[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_140062757}[自动路由聚合功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_332300658}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1426539056}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1526510419}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1615869390}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x2137803625}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_904153470}

[[使能]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}]{#struct_0_17903_10256_x1083011345}[自动路由聚合功能可以减小路由表规模，提高大型网络的可扩展性和效率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1599631135}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x717310138}[关闭]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[自动路由聚合功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x636628392}

[\[Sysname\] rip]{lang="EN-US"}

[\[Sysname-rip-1\] undo summary]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x362248267}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rip summary-address]{lang="EN-US"}**]{#struct_0_17903_10256_x1442481212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rip version]{lang="EN-US"}**]{#struct_0_17903_10256_x1470128503}
:::

::: {#-1147623796 .myid}
[]{#_Toc404787735}[]{#struct_0_17903_10256_x1374427345}[]{#_Toc375236018}[]{#_Toc328746906}[]{#_Toc322698698}

**RIP \-- RIP配置命令 \-- timer triggered**

------------------------------------------------------------------------

[**[timer triggered]{lang="EN-US"}**]{#struct_0_17903_10256_x1507223481}[命令用来配置]{style="font-family:宋体"}[触发更新]{style="font-family:宋体"}[的时间间隔。]{style="font-family:宋体"}

[**[undo timer triggered]{lang="EN-US"}**]{#struct_0_17903_10256_1395403102}[命令]{style="font-family:宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1950418344}

[**[timer triggered ]{lang="EN-US"}***[maximum-interval]{lang="EN-US"}*[ \[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_17903_10256_x1374492881}

[**[undo timer triggered]{lang="EN-US"}**]{#struct_0_17903_10256_1675389535}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_414849971}

[[发送触发更新的]{style="font-family:宋体"}]{#struct_0_17903_10256_x1374951632}[最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，增量惩罚间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1216146796}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_982939350}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1630883876}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1375017168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1822205006}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_338875985}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_17903_10256_x1374820560}[[：触发更新的最大间隔时间。取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[5]{lang="EN-US"}]{.varname}[[，单位是秒。]{style="font-family:宋体"}]{.varname}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_17903_10256_x2049426824}[[：触发更新的最小间隔时间。取值范围是]{style="font-family:宋体"}[10]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[5000]{lang="EN-US"}]{.varname}[[，单位是毫秒。]{style="font-family:宋体"}]{.varname}

[[*[incremental-interval]{lang="EN-US"}*]{.varname}]{#struct_0_17903_10256_x1783668362}[[：触发更新间隔的增加时间。取值范围是]{style="font-family:宋体"}[100]{lang="EN-US"}]{.varname}[[～]{style="font-family:宋体"}[1000]{lang="EN-US"}]{.varname}[[，单位是毫秒。]{style="font-family:宋体"}]{.varname}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1374886096}

[[本命令在网络变化不频繁的情况下将触发更新的时间间隔缩小到]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_17903_10256_1375592473}[，而在网络变化频繁的情况下可以进行相应惩罚，将时间间隔按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_17903_10256_x1510662763}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1479085662}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1375213776}[配置发送触发更新的最大时间间隔为]{style="font-family:宋体"}[2]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_840434890}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] timer triggered 2 100 100]{lang="EN-US"}
:::

::: {#-1110649075 .myid}
[]{#_Toc404787736}[]{#struct_0_17903_10256_538738060}[]{#_Toc216497607}[]{#_Toc137543224}[]{#_Toc94930701}[]{#_Toc93984736}

**RIP \-- RIP配置命令 \-- timers**

------------------------------------------------------------------------

[**[timers]{lang="EN-US"}**]{#struct_0_17903_10256_2076141201}[命令用来配置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[各个定时器的值，可通过调节]{style="font-family:宋体"}[RIP]{lang="EN-US"}[定时器来调整路由协议的性能，以满足网络需要。]{style="font-family:宋体"}

[**[undo timers]{lang="EN-US"}**]{#struct_0_17903_10256_x1640385654}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_715873379}

[**[timers ]{lang="EN-US"}**[{ **garbage-collect** *garbage-collect-value* \| **suppress** *suppress-value* \| **timeout** *timeout-value* \| **update** *update-value* } \*]{lang="EN-US"}]{#struct_0_17903_10256_x1315525394}

[**[undo timers ]{lang="EN-US"}**[{ **garbage-collect** \| **suppress** \| **timeout** \| **update** } \*]{lang="EN-US"}]{#struct_0_17903_10256_x717244602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1417042842}

[[Garbage-collect]{lang="EN-US"}]{#struct_0_17903_10256_x272202380}[定时器的值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x374609141}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x651826862}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x168937624}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_572740068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1028578473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x717179066}

[*[garbage-collect-value]{lang="EN-US"}*]{#struct_0_17903_10256_x682163628}[：]{style="font-family:宋体"}[Garbage-collect]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[suppress-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1250439219}[：]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[timeout-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1540143552}[：]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[update-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1730299249}[：]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_825680280}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1840818580}[受四个定时器的控制，分别是]{style="font-family:宋体"}[Update]{lang="EN-US"}[、]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[、]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[和]{style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[，其中：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Update]{lang="EN-US"}]{#struct_0_17903_10256_840695181}[定时器，定义了发送更新报文的时间间隔。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Timeout]{lang="EN-US"}]{#struct_0_17903_10256_1179628340}[定时器，定义了路由老化时间。如果在老化时间内没有收到关于某条路由的更新报文，则该条路由在路由表中的度量值将会被设置为]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Suppress]{lang="EN-US"}]{#struct_0_17903_10256_x421031959}[定时器，定义了]{style="font-family:
宋体"}[RIP]{lang="EN-US"}[路由处于抑制状态的时间段长度。当一条路由的度量值变为]{style="font-family:宋体"}[16]{lang="EN-US"}[时，该路由将进入被抑制状态。在被抑制状态，只有来自同一邻居，且度量值小于]{style="font-family:宋体"}[16]{lang="EN-US"}[的路由更新才会被路由器接收，取代不可达路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Garbage-Collect]{lang="EN-US"}]{#struct_0_17903_10256_x718162106}[定时器，定义了一条路由从度量值变为]{style="font-family:宋体"}[16]{lang="EN-US"}[开始，直到它从路由表里被删除所经过的时间。]{style="font-family:宋体"}[在]{lang="EN-US" style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[时间内，]{lang="EN-US" style="font-family:宋体"}[RIP]{lang="EN-US"}[以]{lang="EN-US" style="font-family:宋体"}[16]{lang="EN-US"}[作为度量值向外发送这条路由的更新，如果]{lang="EN-US" style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[超时，该路由仍没有得到更新，则该路由将从路由表中被彻底删除。]{lang="EN-US" style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_17903_10256_x1616844573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通常情况下，无需改变各定时器的缺省值，该命令须谨慎使用。]{style="font-family:宋体"}]{#struct_0_17903_10256_x2101834475}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[各个定时器的值在网络中所有的路由器上必须保持一致。]{style="font-family:宋体"}]{#struct_0_17903_10256_x1139207353}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Timeout]{lang="EN-US"}]{#struct_0_17903_10256_1485648631}[定时器的值]{lang="EN-US" style="font-family:宋体"}[要大于]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x452734379}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_565780543}[分别设置]{style="font-family:宋体"}[RIP]{lang="EN-US"}[各定时器的值：其中，]{style="font-family:宋体"}[Update]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Timeout]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Suppress]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒、]{style="font-family:宋体"}[Garbage-Collect]{lang="EN-US"}[定时器的值为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x174339168}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] timers update 5 timeout 15 suppress 15 garbage-collect 30]{lang="EN-US"}
:::

::::: {#-96249297 .myid}
[]{#_Toc404787737}[]{#struct_0_17903_10256_x1375148240}[]{#_Toc375236020}[]{#_Toc328746907}[]{#_Toc322698699}[]{#_Toc145238452}

**RIP \-- RIP配置命令 \-- trip retransmit count**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_2032470642}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_x1374427344}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[trip retransmit count]{lang="EN-US"}**]{#struct_0_17903_10256_1221659874}[命令用来配置]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[中]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的最大重传次数。]{style="font-family:宋体"}

[**[undo trip retransmit count]{lang="EN-US"}**]{#struct_0_17903_10256_1358318858}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1172452855}

[**[trip retransmit count ]{lang="EN-US"}***[retransmit-count-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1374492880}

[**[undo trip retransmit count]{lang="EN-US"}**]{#struct_0_17903_10256_x1053493820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_85688680}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_x1374951627}[中]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的最大重传次数为]{style="font-family:宋体"}[36]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x812796733}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_369736697}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1375017163}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1775150839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x949734168}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_998588163}

[*[retransmit-count-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1374820555}[：]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[中]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的最大重传次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_1842452553}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_62216727}[配置]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[中]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的最大重传次数为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1374886091}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] trip retransmit count 20]{lang="EN-US"}
:::::

::::: {#361150110 .myid}
[]{#_Toc404787738}[]{#struct_0_17903_10256_x546721828}[]{#_Toc375236021}[]{#_Toc328746908}[]{#_Toc322698700}[]{#_Toc145238451}

**RIP \-- RIP配置命令 \-- trip retransmit timer**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](RIP命令.files/image001.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_17903_10256_401311241}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:KaiTi_GB2312"}]{#struct_0_17903_10256_1411188362}[。]{style="font-family:KaiTi_GB2312"}
:::

**[ ]{lang="EN-US"}**

[**[trip retransmit timer]{lang="EN-US"}**]{#struct_0_17903_10256_x1375213771}[命令用来配置]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[重传]{style="font-family:宋体"}[Update Request]{lang="EN-US"}[、]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo trip retransmit timer]{lang="EN-US"}**]{#struct_0_17903_10256_80920003}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_1604078009}

[**[trip retransmit timer ]{lang="EN-US"}***[retransmit-time-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1375279307}

[**[undo trip retransmit timer]{lang="EN-US"}**]{#struct_0_17903_10256_x169020889}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_2116427864}

[[TRIP]{lang="EN-US"}]{#struct_0_17903_10256_x1375082699}[重传]{style="font-family:宋体"}[Update Request]{lang="EN-US"}[报文、]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x709798761}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x1351903650}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_2140875254}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x1375148235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1272759147}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x720889033}

[*[retransmit-time-value]{lang="EN-US"}*]{#struct_0_17903_10256_x1374427339}[：]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[重传]{style="font-family:宋体"}[Update Request]{lang="EN-US"}[、]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_106111235}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1402913560}[配置]{style="font-family:宋体"}[TRIP]{lang="EN-US"}[重传]{style="font-family:宋体"}[Update Request]{lang="EN-US"}[、]{style="font-family:宋体"}[Update Response]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[80]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_x1374492875}

[\[Sysname\] rip 1]{lang="EN-US"}

[\[Sysname-rip-1\] trip retransmit timer 80]{lang="EN-US"}
:::::

::: {#57451019 .myid}
[]{#_Toc216497611}[]{#_Toc137543226}[]{#_Toc94930703}[]{#_Toc93984738}[]{#_Toc404787739}[]{#struct_0_17903_10256_x718096570}[]{#_Toc313007791}[]{#_Toc216497610}[]{#_Toc286221573}[]{#_Toc286221574}[]{#_Toc286221576}[]{#_Toc286221577}[]{#_Toc286221578}[]{#_Toc286221579}[]{#_Toc286221580}[]{#_Toc286221581}[]{#_Toc286221582}[]{#_Toc286221583}[]{#_Toc286221584}[]{#_Toc286221585}[]{#_Toc286221586}[]{#_Toc286221587}[]{#_Toc286221588}[]{#_Toc286221589}[]{#_Toc286221590}[]{#_Toc286221595}[]{#_Toc286221597}[]{#_Toc286221598}[]{#_Toc286221599}[]{#_Toc286221600}[]{#_Toc286221601}[]{#_Toc286221602}[]{#_Toc286221603}[]{#_Toc286221604}[]{#_Toc286221605}[]{#_Toc286221606}[]{#_Toc286221607}[]{#_Toc286221608}[]{#_Toc286221609}[]{#_Toc286221610}[]{#_Toc286221611}[]{#_Toc286221612}[]{#_Toc286221615}[]{#_Toc286221617}[]{#_Toc286221618}[]{#_Toc286221620}[]{#_Toc286221621}[]{#_Toc286221622}[]{#_Toc286221623}[]{#_Toc286221624}[]{#_Toc286221625}[]{#_Toc286221626}[]{#_Toc286221627}[]{#_Toc286221628}[]{#_Toc286221629}[]{#_Toc286221630}[]{#_Toc286221631}

**RIP \-- RIP配置命令 \-- validate-source-address**

------------------------------------------------------------------------

[**[validate-source-address]{lang="EN-US"}**]{#struct_0_17903_10256_x25314579}[命令用来使能对接收到的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由更新报文进行源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查的功能。]{style="font-family:宋体"}

[**[undo validate-source-address]{lang="EN-US"}**]{#struct_0_17903_10256_x1624724744}[命令用来关闭该项功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x102889404}

[**[validate-source-address]{lang="EN-US"}**]{#struct_0_17903_10256_1815939929}

[**[undo validate-source-address]{lang="EN-US"}**]{#struct_0_17903_10256_630469689}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_x751571346}

[[对接收到的]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x67732014}[路由更新报文进行源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查的功能处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1266810311}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_x717637817}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_1660766074}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_1681002245}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_1583779391}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x2071443750}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1209126254}[关闭对接收到的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[路由更新报文进行源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址检查的功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1732677646}

[\[Sysname-rip\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] undo validate-source-address]{lang="EN-US"}
:::

::: {#1902401671 .myid}
[]{#_Toc404787740}[]{#struct_0_17903_10256_109557507}

**RIP \-- RIP配置命令 \-- version**

------------------------------------------------------------------------

[**[version]{lang="EN-US"}**]{#struct_0_17903_10256_x717572281}[命令用来配置全局]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[undo version]{lang="EN-US"}**]{#struct_0_17903_10256_145418575}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1909989904}

[**[version]{lang="EN-US"}**[ { **1** \| **2** }]{lang="EN-US"}]{#struct_0_17903_10256_2082083840}

[**[undo version]{lang="EN-US"}**]{#struct_0_17903_10256_x1998981542}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_17903_10256_1546517831}

[[没有配置全局]{style="font-family:宋体"}[RIP]{lang="EN-US"}]{#struct_0_17903_10256_1197669420}[版本。接口只能发送]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播报文，可以接收]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文、]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_17903_10256_836189942}

[[RIP]{lang="EN-US"}]{#struct_0_17903_10256_624442910}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_17903_10256_412696384}

[[network-admin]{lang="EN-US"}]{#struct_0_17903_10256_x717506745}

[[mdc-admin]{lang="EN-US"}]{#struct_0_17903_10256_x615203913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1814793174}

[**[1]{lang="EN-US"}**]{#struct_0_17903_10256_x1946162127}[：指定为]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[版本。]{style="font-family:宋体"}

[**[2]{lang="EN-US"}**]{#struct_0_17903_10256_x959917334}[：指定为]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[版本，]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[报文的发送方式为组播方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1211383120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口上配置了]{style="font-family:宋体"}]{#struct_0_17903_10256_2024271007}[RIP]{lang="EN-US"}[版本，以接口配置的为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口没有配置]{style="font-family:宋体"}]{#struct_0_17903_10256_x1873634376}[RIP]{lang="EN-US"}[版本，将全局]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本配置为]{style="font-family:宋体"}[1]{lang="EN-US"}[时，接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本为]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[，发送]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播报文，可以接收]{style="font-family:宋体"}[RIP-1]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果接口没有配置]{style="font-family:宋体"}]{#struct_0_17903_10256_x1779271289}[RIP]{lang="EN-US"}[版本，将全局]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本配置为]{style="font-family:宋体"}[2]{lang="EN-US"}[时，接口运行的]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本为]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[且工作在组播方式，发送]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[组播报文，可以接收]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[广播]{style="font-family:宋体"}[/]{lang="EN-US"}[组播]{style="font-family:宋体"}[/]{lang="EN-US"}[单播。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_17903_10256_x717441209}

[[\# ]{lang="EN-US"}]{#struct_0_17903_10256_x1411424767}[指定全局]{style="font-family:宋体"}[RIP]{lang="EN-US"}[版本为]{style="font-family:宋体"}[RIP-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_17903_10256_1449360196}

[\[Sysname\] rip 100]{lang="EN-US"}

[\[Sysname-rip-100\] version 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_17903_10256_x1544076302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rip version]{lang="EN-US"}**]{#struct_0_17903_10256_1147521608}

[ ]{lang="EN-US"}
:::
