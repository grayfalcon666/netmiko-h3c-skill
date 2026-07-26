::: {#-2117340609 .myid}
[]{#_Toc261870594}[]{#_Toc138041266}[]{#_Toc94931024}[]{#_Toc94586756}[]{#_Toc77992909}[]{#_Toc404789228}[]{#struct_0_x1483_x6986_1949653097}[]{#_Toc263865721}[]{#_Toc261870593}[]{#_Toc138041265}

**路由策略 \-- 路由策略公共配置命令 \-- apply as-path**

------------------------------------------------------------------------

[**[apply as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1372598528}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo apply as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x2042914323}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x395552754}

[**[apply as-path ]{lang="EN-US"}**]{#struct_0_x1483_x6986_1927888085}[]{#_Hlt535029898}*[as-number]{lang="EN-US"}*[&\<1-32\> \[ **replace** \]]{lang="EN-US"}

[**[undo apply as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1419106232}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x91492805}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x303474318}[路由信息的]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x244137011}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1474442811}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_994936145}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x970926439}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1369129339}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x1483_x6986_6103398}

[*[as-number]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x783108067}[：自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[replace]{lang="EN-US"}**]{#struct_0_x1483_x6986_2066259852}[：替换原有]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。如果未指定本参数，则在原]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径前加入]{style="font-family:宋体"}[AS]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x303933070}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1709210919}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果路由信息匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么在原]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径前加入]{style="font-family:宋体"}[AS]{lang="EN-US"}[号]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_186786860}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply as-path 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x822694420}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1163800364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match ]{lang="EN-US"}[as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1023824586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_615473268}
:::

::: {#557632803 .myid}
[]{#_Toc404789229}[]{#struct_0_x1483_x6986_x261808825}

**路由策略 \-- 路由策略公共配置命令 \-- apply comm-list delete**

------------------------------------------------------------------------

[**[apply comm-list delete]{lang="EN-US"}**]{#struct_0_x1483_x6986_1658420466}[命令用来删除]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的团体属性。]{style="font-family:宋体"}

[**[undo apply comm-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x303867534}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1818865736}

[**[apply comm-list]{lang="EN-US"}**[ { *comm-list-number* \| *comm-list-name* } **delete**]{lang="EN-US"}]{#struct_0_x1483_x6986_x732466672}

[**[undo apply comm-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1458570909}

[[【]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1636605893}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有删除]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_2079681838}[路由信息的团体属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_880653356}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1128777873}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x846545173}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1371098271}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x303801998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x985831800}

[*[comm-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_524925449}[：团体属性列表号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[基本团体属性列表号的取值范围为]{style="font-family:宋体"}]{#struct_0_x1483_x6986_2127650991}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[高级团体属性列表号的取值范围为]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x274585702}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1690083279}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个不全为数字的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x538723784}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1012488024}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。删除已存在的团体属性列表]{style="font-family:宋体"}[1]{lang="EN-US"}[中指定的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x303736462}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply comm-list 1 delete]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2070731449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_706130896}
:::

::: {#1205185035 .myid}
[]{#_Toc404789230}[]{#struct_0_x1483_x6986_x540830449}[]{#_Toc261870595}[]{#_Toc138041267}

**路由策略 \-- 路由策略公共配置命令 \-- apply community**

------------------------------------------------------------------------

[**[apply community]{lang="EN-US"}**]{#struct_0_x1483_x6986_1923355085}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的团体属性。]{style="font-family:宋体"}

[**[undo apply community]{lang="EN-US"}**]{#struct_0_x1483_x6986_908121642}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1105035664}

[**[apply community ]{lang="EN-US"}**[{ **none** \| **additive** \| { *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \| **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** } \* \[ **additive** \] }]{lang="EN-US"}]{#struct_0_x1483_x6986_1405847628}

[**[undo apply community ]{lang="EN-US"}**[\[ **none** \| **additive** \| { *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \| **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** } **\*** \[ **additive** \] \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1240498357}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1040574501}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x303146638}[路由信息的团体属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1707072020}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x776127819}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x696694527}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_509278416}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x365618502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1932885166}

[**[none]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1668756206}[：删除路由的团体属性。]{style="font-family:宋体"}

[*[community-number]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_6469311}[：团体序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[aa:nn]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x303081102}[：团体号，]{style="font-family:宋体"}*[aa]{lang="EN-US"}*[和]{style="font-family:宋体"}*[nn]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[internet]{lang="EN-US"}**]{#struct_0_x1483_x6986_526869785}[：预定义的团体属性。缺省情况下，所有的路由都具有]{style="font-family:宋体"}**[internet]{lang="EN-US"}**[团体属性，可以被通告给所有的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[no-advertise]{lang="EN-US"}**]{#struct_0_x1483_x6986_x995331122}[：具有此属性的路由在收到后，不能被通告给任何其他的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[no-export]{lang="EN-US"}**]{#struct_0_x1483_x6986_x143347413}[：具有此属性的路由在收到后，不能被发布到本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[之外。如果使用了联盟，则不能被发布到联盟之外，但可以发布给联盟中的其他子]{style="font-family:宋体"}[AS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-export-subconfed]{lang="EN-US"}**]{#struct_0_x1483_x6986_x271660569}[：具有此属性的路由在收到后，不能被发布到本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[之外，也不能发布到联盟中的其他子]{style="font-family:宋体"}[AS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[additive]{lang="EN-US"}**]{#struct_0_x1483_x6986_1740571331}[：附加至原有路由的团体属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1375160370}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1473635735}[创建一个名为]{style="font-family:宋体"}[setcommunity]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[16]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的团体属性为]{style="font-family:宋体"}[no-export]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_695250134}

[\[Sysname\] route-policy setcommunity permit node 16]{lang="EN-US"}

[\[Sysname-route-policy-setcommunity-16\] apply community no-export]{lang="EN-US"}

[]{#_Toc261870602}[]{#_Toc138041273}[]{#_Toc94931033}[]{#_Toc94586765}[]{#_Toc77992907}[]{#struct_0_x1483_x6986_1618643378}[]{#_Toc136509557}[]{#_Toc136509558}[]{#_Toc136509559}[]{#_Toc136509560}[]{#_Toc136509561}[]{#_Toc136509562}[]{#_Toc136509563}[]{#_Toc136509564}[]{#_Toc136509565}[]{#_Toc136509566}[]{#_Toc136509567}[]{#_Hlt6736039}[]{#_Toc136509568}[]{#_Toc136509569}[]{#_Toc136509570}[]{#_Toc136509571}[【相关命令】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match community]{lang="EN-US"}**]{#struct_0_x1483_x6986_x195516660}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1863971010}
:::

::: {#-1262122490 .myid}
[]{#_Toc404789231}[]{#struct_0_x1483_x6986_897183558}[]{#_Toc263865724}[]{#_Toc261870596}[]{#_Toc138041268}

**路由策略 \-- 路由策略公共配置命令 \-- apply cost**

------------------------------------------------------------------------

[**[apply cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_1774890337}[命令用来配置路由信息的路由开销。]{style="font-family:宋体"}

[**[undo apply cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_1776432129}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x726852166}

[**[apply cost]{lang="EN-US"}**[ \[ **+** \| **-** \] *value*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1469256945}

[**[undo apply cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_x945686320}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x637315604}

[[没有配置路由信息的路由开销。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1618708914}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1660725658}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_2091686508}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2139436452}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_522199013}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1751523796}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1982019933}

[**[+]{lang="EN-US"}**]{#struct_0_x1483_x6986_182217483}[：增加开销值。]{style="font-family:宋体"}

[**[-]{lang="EN-US"}**]{#struct_0_x1483_x6986_367812948}[：减少开销值。]{style="font-family:宋体"}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_1618774450}[：指定路由信息的路由开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x991373526}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1681770485}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[外部路由，那么设置该路由的路由开销为]{style="font-family:宋体"}[120]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1610643224}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match route-type external-type1or2]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply cost 120]{lang="EN-US"}
:::

::: {#731282721 .myid}
[]{#_Toc404789232}[]{#struct_0_x1483_x6986_360163087}[]{#_Toc263865725}[]{#_Toc261870597}[]{#_Toc138041269}[]{#_Toc17101183}

**路由策略 \-- 路由策略公共配置命令 \-- apply cost-type**

------------------------------------------------------------------------

[**[apply cost-type]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1715659856}[命令用来配置路由信息的路由开销类型。]{style="font-family:宋体"}

[**[undo apply cost-type]{lang="EN-US"}**]{#struct_0_x1483_x6986_2056083016}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1383316160}

[**[apply cost-type]{lang="EN-US"}**[ ]{lang="EN-US"}[{ **external** \| **internal** \| **type-1** \| **type**-**2** }]{lang="EN-US"}]{#struct_0_x1483_x6986_1618839986}

[**[undo]{lang="EN-US"}**[ **apply cost-type**]{lang="EN-US"}]{#struct_0_x1483_x6986_x1065208735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_272282945}

[[没有配置路由开销类型。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1114980196}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x889191417}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1912489725}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_901089156}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x414666976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1309557738}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x755279371}

[**[external]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618381234}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[外部路由。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1403350871}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[内部路由或者设置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的]{style="font-family:宋体"}[MED]{lang="EN-US"}[值为下一跳的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[度量值。]{style="font-family:宋体"}

[**[type-1]{lang="EN-US"}**]{#struct_0_x1483_x6986_x129286384}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的外部]{style="font-family:宋体"}[Type-1]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[type-2]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1988290696}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[的外部]{style="font-family:宋体"}[Type-2]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1371222385}

[**[apply cost-type ]{lang="EN-US"}[internal]{lang="EN-US"}**]{#struct_0_x1483_x6986_2131007426}[命令的作用：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[应用于]{style="font-family:宋体"}]{#struct_0_x1483_x6986_689154763}[IS-IS]{lang="EN-US"}[路由：设置路由类型为]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[内部路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[应用于]{lang="EN-US" style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1656705285}[路由：路由器从]{lang="EN-US" style="font-family:宋体"}[IBGP]{lang="EN-US"}[对等体学到的路由在通告给]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体时，如果配置]{lang="EN-US" style="font-family:宋体"}**[apply cost-type internal]{lang="EN-US"}**[命令，则路由器会将向]{lang="EN-US" style="font-family:宋体"}[EBGP]{lang="EN-US"}[对等体通告的路由的]{lang="EN-US" style="font-family:宋体"}[MED]{lang="EN-US"}[值设置为该路由的下一跳的]{lang="EN-US" style="font-family:宋体"}[IGP]{lang="EN-US"}[度量值。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_755032511}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1618446770}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match tag 8]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply cost-type internal]{lang="EN-US"}
:::

::: {#556000168 .myid}
[]{#_Toc404789233}[]{#struct_0_x1483_x6986_x200151595}[]{#_Toc263865726}[]{#_Toc261870598}[]{#_Toc138041270}[]{#_Toc94931028}[]{#_Toc94586760}[]{#_Toc77992905}[]{#_Toc61239908}[]{#_Toc53707324}

**路由策略 \-- 路由策略公共配置命令 \-- apply extcommunity**

------------------------------------------------------------------------

[**[apply extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_x691182221}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的扩展团体属性。]{style="font-family:宋体"}

[**[undo apply extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1430569875}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_148171010}

[**[apply extcommunity]{lang="EN-US"}**[ { **rt** *route-target* }&\<1-32\> \[ **additive** \]]{lang="EN-US"}]{#struct_0_x1483_x6986_167671569}

[**[undo apply extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_1029411453}

[[【]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x974936078}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有配]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x66929023}[置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的扩展团体属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618512306}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1772151989}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1010043908}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1962977108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x873692446}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x885199877}

[[{ **rt** *route-target* }&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_395711525}[：指定的]{style="font-family:宋体"}[RT]{lang="EN-US"}[（]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[，路由目标）扩展团体属性，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[route-target]{lang="EN-US"}*]{#struct_0_x1483_x6986_926012782}[有三种形式，分别如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x1483_x6986_x1141005840}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。其中，自治系统号取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1483_x6986_1618577842}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。其中，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1483_x6986_1706064152}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[70000:3]{lang="EN-US"}[。其中，自治系统号取值范围为]{style="font-family:宋体"}[65536]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[additive]{lang="EN-US"}**]{#struct_0_x1483_x6986_x30214566}[：允许增加到已有的扩展团体中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x247515168}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1603423392}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么为]{style="font-family:宋体"}[BGP]{lang="EN-US"}[指定]{style="font-family:宋体"}[RT]{lang="EN-US"}[扩展团体属性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1555053693}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply extcommunity rt 100:2 additive]{lang="EN-US"}
:::

::: {#1328571453 .myid}
[]{#_Toc404789234}[]{#struct_0_x1483_x6986_1228887148}[]{#_Toc349825472}[]{#_Toc349221865}[]{#_Toc349054547}

**路由策略 \-- 路由策略公共配置命令 \-- apply ip-precedence**

------------------------------------------------------------------------

[**[apply ip-precedence]{lang="EN-US"}**]{#struct_0_x1483_x6986_23903809}[命令用来配置路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo apply ip-precedence]{lang="EN-US"}**]{#struct_0_x1483_x6986_x586594164}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1630660804}

[**[apply ip-precedence ]{lang="EN-US"}**[{ *value* \| **clear** }]{lang="EN-US"}]{#struct_0_x1483_x6986_x758020553}

[**[undo]{lang="EN-US"}**[ **apply ip-precedence**]{lang="EN-US"}]{#struct_0_x1483_x6986_x1768099423}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1348175145}

[[没有配置路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1616058902}[优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_494104443}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1158765670}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1229083756}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1926262348}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_996886403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1675868983}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_621393057}[：路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级，取值范围是]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[clear]{lang="EN-US"}**]{#struct_0_x1483_x6986_96921672}[：清除路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1981726324}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x2005966775}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。]{style="font-family:宋体"}[如果匹配扩展团体列表号]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由，那么配置路由的]{style="font-family:宋体"}[IP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x571578522}

[\[Sysname\] ip extcommunity-list 100 permit rt 100:100]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match extcommunity 100]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply ip-precedence 3]{lang="EN-US"}
:::

::: {#1022040110 .myid}
[]{#_Toc404789235}[]{#struct_0_x1483_x6986_x2031107242}[]{#_Toc263865728}[]{#_Toc261870600}[]{#_Toc138041271}[]{#_Toc65038751}[]{#_Toc58333353}[]{#_Toc324406132}[]{#_Toc324406133}[]{#_Toc324406134}[]{#_Toc324406135}[]{#_Toc324406136}[]{#_Toc324406137}[]{#_Toc324406138}[]{#_Toc324406139}[]{#_Toc324406140}[]{#_Toc324406141}[]{#_Toc324406142}[]{#_Toc324406143}[]{#_Toc324406144}[]{#_Toc324406145}[]{#_Toc324406146}[]{#_Toc324406147}[]{#_Toc324406148}[]{#_Toc324406149}[]{#_Toc324406150}[]{#_Toc324406151}[]{#_Toc324406152}[]{#_Toc324406153}

**路由策略 \-- 路由策略公共配置命令 \-- apply isis**

------------------------------------------------------------------------

[**[apply isis]{lang="EN-US"}**]{#struct_0_x1483_x6986_1062438724}[命令用来配置引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[某个级别的区域。]{style="font-family:宋体"}

[**[undo apply isis]{lang="EN-US"}**]{#struct_0_x1483_x6986_469347954}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619167666}

[**[apply isis ]{lang="EN-US"}**[{ **level-1** \| **level-1-2** \| **level-2** }]{lang="EN-US"}]{#struct_0_x1483_x6986_580417958}

[**[undo apply isis]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1923601342}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1310866498}

[[没有配置引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_x1483_x6986_807923034}[某个级别的区域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_135352014}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1452989334}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x447087527}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_599837029}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1619233202}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x991189099}

[**[level-1]{lang="EN-US"}**]{#struct_0_x1483_x6986_1314130984}[：引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_x1483_x6986_1739916542}[：引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_x1483_x6986_2045979329}[：引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1323847549}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x128205247}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配标记域为]{style="font-family:宋体"}[8]{lang="EN-US"}[的路由，那么引入路由到]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_385000161}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match tag 8]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply isis level-2]{lang="EN-US"}
:::

::: {#-945525407 .myid}
[]{#_Toc404789236}[]{#struct_0_x1483_x6986_1111533555}[]{#_Toc263865729}[]{#_Toc261870601}[]{#_Toc138041272}

**路由策略 \-- 路由策略公共配置命令 \-- apply local-preference**

------------------------------------------------------------------------

[**[apply local-preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618643379}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级。]{style="font-family:宋体"}

[**[undo apply local-preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_x195582196}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_903888089}

[**[apply local-preference]{lang="EN-US"}**[ *preference*]{lang="EN-US"}]{#struct_0_x1483_x6986_x908446814}

[**[undo apply local-preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_x468002153}

[[【]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1070200431}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有配]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1629193953}[置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x300445292}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x512018320}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618708915}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1660660122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_530862983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_815475996}

[*[preference]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1057657138}[：]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x236798687}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1674082410}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么配置该]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的本地优先级为]{style="font-family:宋体"}[130]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1887436932}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply local-preference 130]{lang="EN-US"}
:::

::::: {#122592316 .myid}
[]{#_Toc404789237}[]{#struct_0_x1483_x6986_1618774451}

**路由策略 \-- 路由策略公共配置命令 \-- apply mpls-label**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](路由策略命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1483_x6986_x991307990}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令支持的情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x1483_x6986_x1051682200}
:::

[ ]{lang="EN-US"}

[**[apply mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_1542541953}[命令用来为路由分配]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签。]{style="font-family:宋体"}

[**[undo apply mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_x2085767224}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1038605308}

[**[apply mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1221079598}

[**[undo apply mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_x871927712}

[[【]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x774682132}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x966988811}[为路由分配]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618839987}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1065143199}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_192742079}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1862021987}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1389967265}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x692631424}

[[如果]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x1483_x6986_x338710071}[标签分配失败，路由信息将不会被发布。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1518658229}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1640278456}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。为路由分配]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1618381235}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply mpls-label]{lang="EN-US"}
:::::

::: {#994821656 .myid}
[]{#_Toc261870607}[]{#_Toc138041277}[]{#_Toc404789238}[]{#struct_0_x1483_x6986_x1403416407}[]{#_Toc263865731}[]{#_Toc261870603}[]{#_Toc138041274}

**路由策略 \-- 路由策略公共配置命令 \-- apply origin**

------------------------------------------------------------------------

[**[apply origin]{lang="EN-US"}**]{#struct_0_x1483_x6986_1265518638}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[undo apply origin]{lang="EN-US"}**]{#struct_0_x1483_x6986_572632656}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1270626754}

[**[apply origin]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1483_x6986_158462050}[]{#_Hlt6736036}[{ **egp** *as-number* \| **igp** \| **incomplete** }]{lang="EN-US"}

[**[undo apply origin]{lang="EN-US"}**]{#struct_0_x1483_x6986_858617647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x42960298}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_1422519000}[路由信息的]{style="font-family:宋体"}[ORIGIN]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618446771}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x200217131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1245204110}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x302550613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1010437820}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1189626772}

[**[egp]{lang="EN-US"}***[ as-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_946962638}[：设定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的来源为外部路由。]{style="font-family:宋体"}*[as-number]{lang="EN-US"}*[表示指定外部路由的自治系统号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[igp]{lang="EN-US"}**]{#struct_0_x1483_x6986_2032151756}[：设定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的来源为内部路由。]{style="font-family:宋体"}

[**[incomplete]{lang="EN-US"}**]{#struct_0_x1483_x6986_x38890599}[：设定]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的来源为未知来源。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x907899809}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1618512307}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么设置该]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的路由源为]{style="font-family:宋体"}[IGP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1772086453}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply origin igp]{lang="EN-US"}[]{#_Toc77992910}[]{#_Toc65741000}[]{#_Toc61239911}[]{#_Toc53707327}
:::

::: {#-867638460 .myid}
[]{#_Toc404789239}[]{#struct_0_x1483_x6986_1458338824}[]{#_Toc263865732}[]{#_Toc261870604}[]{#_Toc138041275}[]{#_Toc94931036}[]{#_Toc94586768}

**路由策略 \-- 路由策略公共配置命令 \-- apply preference**

------------------------------------------------------------------------

[**[apply preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1106195954}[命令用来配置路由协议的优先级。]{style="font-family:宋体"}

[**[undo apply preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_x368299096}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2007167068}

[**[apply preference]{lang="EN-US"}**[ *preference*]{lang="EN-US"}]{#struct_0_x1483_x6986_626160851}

[**[undo apply preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_81104970}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1216976184}

[[没有配置路由协议的优先级。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1618577843}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1706129688}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x446743243}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1364630738}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1501451143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_135895036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1092541460}

[*[preference]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1722171943}[：路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1074528903}

[[如果路由协议已经用命令]{style="font-family:宋体"}**[preference]{lang="EN-US"}**]{#struct_0_x1483_x6986_895913868}[配置了优先级，再用]{style="font-family:宋体"}**[apply preference]{lang="EN-US"}**[命令修改路由协议的优先级，则这些匹配策略的路由采用]{style="font-family:宋体"}**[apply preference]{lang="EN-US"}**[命令修改的优先级，其它路由的优先级均采用]{style="font-family:宋体"}**[preference]{lang="EN-US"}**[命令所设的值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619167667}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_580352422}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[外部路由，那么设置该路由协议的优先级为]{style="font-family:宋体"}[90]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1351096907}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match route-type external-type1or2]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply preference 90]{lang="EN-US"}
:::

::: {#747950111 .myid}
[]{#_Toc404789240}[]{#struct_0_x1483_x6986_x440982161}[]{#_Toc263865733}[]{#_Toc261870605}[]{#_Toc138041276}[]{#_Toc94931037}[]{#_Toc94586769}[]{#_Toc77992911}[]{#_Toc65741001}[]{#_Toc61239912}[]{#_Toc53707328}

**路由策略 \-- 路由策略公共配置命令 \-- apply preferred-value**

------------------------------------------------------------------------

[**[apply preferred-value]{lang="EN-US"}**]{#struct_0_x1483_x6986_x243390345}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的首选值。]{style="font-family:宋体"}

[**[undo apply preferred-value]{lang="EN-US"}**]{#struct_0_x1483_x6986_1353912561}[命令恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1850066250}

[**[apply preferred-value]{lang="EN-US"}**[ *preferred-value*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1196552822}

[**[undo apply preferred-value]{lang="EN-US"}**]{#struct_0_x1483_x6986_2111295327}

[[【]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619233203}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x991123563}[路由信息的首选值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1686882251}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1579781432}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1915568121}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_250156777}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_923825503}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_965733339}

[*[preferred-value]{lang="EN-US"}*]{#struct_0_x1483_x6986_x961354383}[：首选值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618643376}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x194599156}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么设置该]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由的首选值为]{style="font-family:宋体"}[66]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1426191208}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply preferred-value 66]{lang="EN-US"}
:::

::: {#737727210 .myid}
[]{#_Toc404789241}[]{#struct_0_x1483_x6986_x1217315766}[]{#_Toc331755153}[]{#_Toc329939924}[]{#_Toc324406160}[]{#_Toc324406161}[]{#_Toc324406162}[]{#_Toc324406163}[]{#_Toc324406164}[]{#_Toc324406165}[]{#_Toc324406166}[]{#_Toc324406167}[]{#_Toc324406168}[]{#_Toc324406169}[]{#_Toc324406170}[]{#_Toc324406171}[]{#_Toc324406172}[]{#_Toc324406173}[]{#_Toc324406174}[]{#_Toc324406175}[]{#_Toc324406176}[]{#_Toc324406177}[]{#_Toc324406178}[]{#_Toc324406179}[]{#_Toc324406180}[]{#_Toc324406181}

**路由策略 \-- 路由策略公共配置命令 \-- apply prefix-priority**

------------------------------------------------------------------------

[**[apply prefix-priority]{lang="EN-US"}**]{#struct_0_x1483_x6986_1564317640}[命令用来配置]{style="font-family:宋体"}[路由的收敛优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo apply prefix-priority]{lang="EN-US"}**]{#struct_0_x1483_x6986_946177071}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_683438452}

[**[apply prefix-priority]{lang="EN-US"}**[ { **critical** \| **high** \| **medium** }]{lang="EN-US"}]{#struct_0_x1483_x6986_x1989598071}

[**[undo apply prefix-priority]{lang="EN-US"}**]{#struct_0_x1483_x6986_267469581}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618708912}

[[没有配置]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1661118874}[路由的收敛优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1370468057}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x792686682}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x554561628}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x2099937840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x2130592315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1475722721}

[**[critical]{lang="EN-US"}**]{#struct_0_x1483_x6986_912399838}[：路由的收敛优先级为关键。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618774448}[：路由的收敛优先级为高。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_x1483_x6986_x991897813}[：路由的收敛优先级中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1306368835}

[[未配置时，路由的收敛优先级为低（]{style="font-family:宋体"}[Low]{lang="EN-US"}]{#struct_0_x1483_x6986_x1263089432}**[）]{style="font-family:宋体"}**[。]{style="font-family:宋体"}

[[路由的收敛优先级由高到低为关键、高、中、低。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x982973259}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_214880433}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x290888732}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的地址前缀列表]{style="font-family:宋体"}[abc]{lang="EN-US"}[，那么设置该路由的收敛优先级为关键。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x306740782}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ip address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply prefix-priority critical]{lang="EN-US"}
:::

::: {#-1222325402 .myid}
[]{#_Toc404789242}[]{#struct_0_x1483_x6986_1229083755}[]{#_Toc349825480}[]{#_Toc349221866}[]{#_Toc349054548}

**路由策略 \-- 路由策略公共配置命令 \-- apply qos-local-id**

------------------------------------------------------------------------

[**[apply qos-local-id]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1926458956}[命令用来配置路由的]{style="font-family:宋体"} [QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **apply qos-local-id**]{lang="EN-US"}]{#struct_0_x1483_x6986_1229018219}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1950996663}

[**[apply qos-local-id ]{lang="EN-US"}**[{ *value* \| **clear** }]{lang="EN-US"}]{#struct_0_x1483_x6986_158492746}

[**[undo]{lang="EN-US"}**[ **apply qos-local-id**]{lang="EN-US"}]{#struct_0_x1483_x6986_x1883319263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1345812100}

[[没有配置路由的]{style="font-family:宋体"}[QoS]{lang="EN-US"}]{#struct_0_x1483_x6986_x1586572149}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1033378821}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1897484678}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1999033710}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1090656379}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1229214827}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_416833972}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_x932442517}[：路由的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[，取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[clear]{lang="EN-US"}**]{#struct_0_x1483_x6986_x535442488}[：清除路由的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1058878512}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1002947692}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。]{style="font-family:宋体"}[如果匹配扩展团体列表号]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由，那么配置路由的]{style="font-family:宋体"}[QoS]{lang="EN-US"}[本地]{style="font-family:宋体"}[ID]{lang="EN-US"}[值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1229149291}

[\[Sysname\] ip extcommunity-list 100 permit rt 100:100]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match extcommunity 100]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply qos-local-id 100]{lang="EN-US"}
:::

::: {#1167427441 .myid}
[]{#_Toc404789243}[]{#struct_0_x1483_x6986_x895159923}

**路由策略 \-- 路由策略公共配置命令 \-- apply tag**

------------------------------------------------------------------------

[**[apply tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618839984}[命令用来配置]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由信息的标记。]{style="font-family:宋体"}

[**[undo apply tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1065339807}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1172122613}

[**[apply tag]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1483_x6986_x2045542458}

[**[undo apply tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_x484304500}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x902162699}

[[没有配置]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1540880478}[路由信息的标记。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2070257022}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_885487547}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618381232}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1402957655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1806930859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1924251277}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1959679810}[：指定路由信息的标记值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1820399431}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_37761617}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。配置]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由信息的标记为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1049473134}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[]{#_Hlt6628826}[\[Sysname-route-policy-policy1-10\] apply tag 100]{lang="EN-US"}
:::

::: {#1009082544 .myid}
[]{#_Toc404789244}[]{#struct_0_x1483_x6986_x1531886329}

**路由策略 \-- 路由策略公共配置命令 \-- apply traffic-index**

------------------------------------------------------------------------

[**[apply traffic-index]{lang="EN-US"}**]{#struct_0_x1483_x6986_246142849}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的流量索引。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **apply traffic-index**]{lang="EN-US"}]{#struct_0_x1483_x6986_x2022268176}[命令用来恢复缺省情况]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1532082937}

[**[apply traffic-index ]{lang="EN-US"}**[{ *value* \| **clear** }]{lang="EN-US"}]{#struct_0_x1483_x6986_1605639096}

[**[undo]{lang="EN-US"}**[ **apply traffic-index**]{lang="EN-US"}]{#struct_0_x1483_x6986_x861258461}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1236108348}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_662721120}[路由信息的流量索引。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1532017401}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1276023266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x548725936}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x222907492}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_98798891}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1532214009}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_x2029598390}[：]{style="font-family:宋体"}[流量索引值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[clear]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1721692790}[：清除路由的]{style="font-family:宋体"}[流量索引值]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1614262709}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1858528208}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。]{style="font-family:宋体"}[如果匹配扩展团体列表号]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由，那么配置路由的]{style="font-family:宋体"}[流量索引值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1532148473}

[\[Sysname\] ip extcommunity-list 100 permit rt 100:100]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match extcommunity 100]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply traffic-index 6]{lang="EN-US"}
:::

::: {#1055810917 .myid}
[]{#_Toc138041278}[]{#_Toc404789245}[]{#struct_0_x1483_x6986_287493816}[]{#_Toc261870608}[]{#_Toc259780321}[]{#_Toc216757384}[]{#_Toc216757393}[]{#_Toc216757394}

**路由策略 \-- 路由策略公共配置命令 \-- continue**

------------------------------------------------------------------------

[**[continue]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618446768}[命令用来配置下一个执行节点。]{style="font-family:宋体"}

[**[undo continue]{lang="EN-US"}**]{#struct_0_x1483_x6986_x200675884}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1464125261}

[**[continue]{lang="EN-US"}**[ \[ ]{lang="EN-US"}*[node-number]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x324430527}

[**[undo continue]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1847262886}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x721784390}

[[没有配置下一个执行节点。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x651415787}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1361750921}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x531737747}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618512304}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1772020917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1113118983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2003289546}

[*[node-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1664224039}[：标识本命令会跳转到同一路由策略中的节点索引，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1827725559}

[[下一个执行节点序列号必须大于当前节点序列号。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_118420466}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_744376866}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_395955805}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义]{style="font-family:宋体"}[continue]{lang="EN-US"}[子句，配置下一个执行节点序列号为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1618577840}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] continue 20]{lang="EN-US"}
:::

::: {#1901292918 .myid}
[]{#_Toc261870610}[]{#_Toc138041279}[]{#_Toc404789246}[]{#struct_0_x1483_x6986_1705933080}[]{#_Toc263865737}[]{#_Toc261870609}

**路由策略 \-- 路由策略公共配置命令 \-- display ip as-path**

------------------------------------------------------------------------

[**[display ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1691528751}[命令用来显示]{style="font-family:宋体"}[BGP AS]{lang="EN-US"}[路径过滤列表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_595571500}

[**[display ip as-path]{lang="EN-US"}**[ \[ *as-path-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1040567725}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x691274710}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1010894865}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2072465815}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_100755841}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_623822880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1619167664}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_580549030}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x664136854}

[*[as-path-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_676519005}[：]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。如果未指定本参数，将显示所有已配置的]{style="font-family:宋体"}[BGP AS]{lang="EN-US"}[路径过滤列表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x698862102}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1179663730}[显示列表号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP AS]{lang="EN-US"}[路径列表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip as-path 1]{lang="EN-US"}]{#struct_0_x1483_x6986_1890756957}

[ListID    Mode      Expression]{lang="EN-US"}

[1         permit    2]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip as-path]{lang="EN-US"}]{#struct_0_x1483_x6986_1483489671}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x701083337}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1211451054}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619233200}

[[ListID]{lang="EN-US"}]{#struct_0_x1483_x6986_x991320171}

[[AS]{lang="EN-US"}]{#struct_0_x1483_x6986_2048140747}[路径列表号]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x1483_x6986_1473853168}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1074178208}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x305950704}[：]{style="font-family:宋体"}[表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_x767495737}[：]{style="font-family:宋体"}[表示拒绝]{lang="EN-US" style="font-family:宋体"}

[[Expression]{lang="EN-US"}]{#struct_0_x1483_x6986_1618643377}

[[匹配的]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_x1483_x6986_x194664692}[路径正则表达式]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1160076853 .myid}
[]{#_Toc404789247}[]{#struct_0_x1483_x6986_2047277274}

**路由策略 \-- 路由策略公共配置命令 \-- display ip community-list**

------------------------------------------------------------------------

[**[display ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x679874553}[命令用来显示]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[团体属性列表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_902157675}

[**[display ip community-list]{lang="EN-US"}**[ \[ *basic-community-list-number* \| *adv-community-list-number* \| **name** *comm-list-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_353462316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1290240379}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_823154928}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x884646252}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1618708913}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_1661053338}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_904835487}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_x514551916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1118085663}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_908882669}[：为基本团体属性列表号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x876445905}[：为高级团体属性列表号，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *comm-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_1609457744}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个不全为数字的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1905622734}

[[如果未指定团体属性列表号或团体属性列表名，将显示所有已配置的]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_1618774449}[团体属性列表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x991832277}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x686604944}[显示所有的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[团体属性列表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip community-list]{lang="EN-US"}]{#struct_0_x1483_x6986_1223563163}

[Community List Basic aaa]{lang="EN-US"}

[        permit]{lang="EN-US"}

[Community List Advanced bbb]{lang="EN-US"}

[        permit  3333]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display ip community-list]{lang="EN-US"}]{#struct_0_x1483_x6986_1629786376}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x674195689}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2081573441}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x715721091}

[[Community List Basic]{lang="EN-US"}]{#struct_0_x1483_x6986_1618839985}

[[基本团体属性列表]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1065274271}

[[Community List Advanced]{lang="EN-US"}]{#struct_0_x1483_x6986_x2040472285}

[[高级团体属性列表]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x669768855}

[[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_1551072401}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1438303270}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x1085621115}[：表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_1618381233}[：表示拒绝]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1531165524 .myid}
[]{#_Toc261870612}[]{#_Toc138041281}[]{#_Toc404789248}[]{#struct_0_x1483_x6986_x1403023191}[]{#_Toc263865739}[]{#_Toc261870611}[]{#_Toc138041280}[]{#_Toc136509583}[]{#_Toc136509585}[]{#_Toc136509586}[]{#_Toc136509587}[]{#_Toc136509588}[]{#_Toc136509589}[]{#_Toc136509590}[]{#_Toc136509591}[]{#_Toc136509592}[]{#_Toc136509593}[]{#_Toc136509598}[]{#_Toc136509599}[]{#_Toc136509627}

**路由策略 \-- 路由策略公共配置命令 \-- display ip extcommunity-list**

------------------------------------------------------------------------

[**[display ip extcommunity-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_147273486}[命令用来显示]{style="font-family:
宋体"}[BGP]{lang="EN-US"}[扩展团体属性列表信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_684787480}

[**[display ip extcommunity-list]{lang="EN-US"}**[ \[ *ext-comm-list-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_168776941}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_490751698}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1682044984}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_697190869}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_245789512}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_1618446769}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x200741420}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_1267361314}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_55494795}

[*[ext-comm-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_639978764}[：扩展团体属性列表号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。如果未指定本参数，将显示所有已配置的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[扩展团体属性列表信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1118196040}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1925908047}[显示列表号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[扩展团体属性列表信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip extcommunity-list 1]{lang="EN-US"}]{#struct_0_x1483_x6986_1133893525}

[Extended Community List Number 1]{lang="EN-US"}

[         permit rt : 9:6]{lang="EN-US"}

[         Permit soo: 9:6]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ip extcommunity-list]{lang="EN-US"}]{#struct_0_x1483_x6986_x1845327696}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x674738345}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618512305}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1771955381}

[[Extended Community List Number]{lang="EN-US"}]{#struct_0_x1483_x6986_1173120851}

[[扩展团体属性列表]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x771410707}

[[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_1625227902}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_2060828550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_1618577841}[：表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_1705998616}[：表示拒绝]{lang="EN-US" style="font-family:宋体"}

[[rt]{lang="EN-US"}]{#struct_0_x1483_x6986_1650444185}

[[RT]{lang="EN-US"}]{#struct_0_x1483_x6986_x212446680}[（]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[，路由目标）扩展团体属性]{style="font-family:宋体"}

[[soo]{lang="EN-US"}]{#struct_0_x1483_x6986_1229018218}

[[SoO]{lang="EN-US"}]{#struct_0_x1483_x6986_1950931127}[（]{style="font-family:宋体"}[Site of Origin]{lang="EN-US"}[，源站点]{style="font-family:宋体"}[）扩展团体属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-122265648 .myid}
[]{#_Toc404789249}[]{#struct_0_x1483_x6986_1655356379}[]{#_Toc343692468}[]{#_Toc340065888}

**路由策略 \-- 路由策略公共配置命令 \-- display mac-list**

------------------------------------------------------------------------

[**[display mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x58365550}[命令用来显示]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1754172466}

[**[display mac-list ]{lang="EN-US"}**[\[ ]{lang="EN-US"}**[name]{lang="EN-US"}**[ *mac-list-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x324060223}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619167665}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_580483494}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x673520666}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_921371237}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_2077768093}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1129743238}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_1118802259}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619233201}

[**[name]{lang="EN-US"}**[ *mac-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_x991254635}*[：]{style="font-family:宋体"}*[指定显示的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[如果未指定]{style="font-family:宋体"}[本参数，将显]{style="font-family:宋体"}[示所有已配置]{style="font-family:宋体"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2025846764}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1871561433}[显示名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的地址前缀列表的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display mac-list name abc]{lang="EN-US"}]{#struct_0_x1483_x6986_x431068234}

[MAC address list: abc]{lang="EN-US"}

[ Permitted 0]{lang="EN-US"}

[ Denied 0]{lang="EN-US"}

[  Index: 1  Permit: 001b-2188-946c/32]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display mac-list]{lang="EN-US"}]{#struct_0_x1483_x6986_1717864072}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x673159273}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x280897905}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618643374}

[[MAC address list]{lang="EN-US"}]{#struct_0_x1483_x6986_x194730228}

[[MAC]{lang="EN-US"}]{#struct_0_x1483_x6986_x1041357238}[地址列表名]{style="font-family:宋体"}

[[Permitted]{lang="EN-US"}]{#struct_0_x1483_x6986_1496532957}

[[允许通过的报文个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x824545583}

[[Denied 0]{lang="EN-US"}]{#struct_0_x1483_x6986_x591879312}

[[拒绝通过的报文个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1433465546}

[[Index]{lang="EN-US"}]{#struct_0_x1483_x6986_1618708910}

[[标识]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1483_x6986_1660987802}[地址前缀列表中的一条表项]{style="font-family:宋体"}

[[Permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x1451130143}

[[允许通过的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1483_x6986_x1385774216}[地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-503739789 .myid}
[]{#_Toc404789250}[]{#struct_0_x1483_x6986_610917212}

**路由策略 \-- 路由策略公共配置命令 \-- display route-policy**

------------------------------------------------------------------------

[**[display route-policy]{lang="EN-US"}**]{#struct_0_x1483_x6986_x2080891700}[命令用来显示配置的路由策略信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_116526143}

[**[display route-policy]{lang="EN-US"}**[ \[ **name** *route-policy-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1091516250}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618774446}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x991504597}[]{#_Hlt6988486}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x690096005}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x265089418}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_x1390022622}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_659938238}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_1863340374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1721979886}

[**[name]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_856640563}[：指定显示的路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有已配置的路由策略信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618839982}

[]{#_Hlt8892635}[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1065470879}[显示名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略信息。]{style="font-family:宋体"}

[[\<Sysname\> display route-policy ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1874380715}[]{#_Hlt2496302}[name policy1]{lang="EN-US"}

[Route-policy: policy1]{lang="EN-US"}

[  permit : 1]{lang="EN-US"}

[          if-match cost 10]{lang="EN-US"}

[          continue: next node 11]{lang="EN-US"}

[          apply comm-list a delete]{lang="EN-US"}

[]{#struct_0_x1483_x6986_x1203964878}[]{#_Toc99255043}[[表1-4 ]{lang="EN-US"}[display route-policy]{lang="EN-US"}]{#_Toc81210270}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x679377321}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_43008466}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x942539592}

[[Route-policy]{lang="EN-US"}]{#struct_0_x1483_x6986_x186307925}

[[路由策略名称]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1618381230}

[[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x1403088727}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1153565532}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x806087527}[表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_x824226223}[表示拒绝]{lang="EN-US" style="font-family:宋体"}

[[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_x1346168962}

[[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_x348406527}[子句，配置的匹配条件]{style="font-family:宋体"}

[[continue]{lang="EN-US"}]{#struct_0_x1483_x6986_1618446766}

[[continue]{lang="EN-US"}]{#struct_0_x1483_x6986_x199758380}[字句，配置下一个执行节点]{style="font-family:宋体"}

[[apply]{lang="EN-US"}]{#struct_0_x1483_x6986_x1334148744}

[[apply]{lang="EN-US"}]{#struct_0_x1483_x6986_x1373387887}[子句，如满足匹配条件，则要执行的动作]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1138633959 .myid}
[]{#_Toc261870614}[]{#_Toc138041283}[]{#_Toc17101170}[]{#_Toc404789251}[]{#struct_0_x1483_x6986_x1205245147}[]{#_Toc263865741}[]{#_Toc261870613}[]{#_Toc138041282}[]{#_Toc17101169}

**路由策略 \-- 路由策略公共配置命令 \-- if-match as-path**

------------------------------------------------------------------------

[**[if-match as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1703476774}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径域的匹配条件。]{style="font-family:宋体"}

[**[undo if-match as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1358782633}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618512302}

[**[if-match as-path]{lang="EN-US"}**[ *as-path-number*&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x1771889845}

[**[undo if-match as-path]{lang="EN-US"}**[ \[ *as-path-number*&\<1-32\> \]]{lang="EN-US"}]{#struct_0_x1483_x6986_506970241}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1187982502}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x897217259}[路由信息的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径域的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x840918503}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1322104459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_291725658}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_683336096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1618577838}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1705408797}

[*[as-path-number]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x699348922}[：为]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x381779703}

[[路由策略的]{style="font-family:宋体"}[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_2089948368}[子句之一，用于过滤]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息，根据路由信息的自治系统路径属性指定匹配条件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1873528010}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1098223501}[首先定义一个编号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的]{style="font-family:宋体"}[as-path]{lang="EN-US"}[，允许自治系统号包含]{style="font-family:宋体"}[200]{lang="EN-US"}[和]{style="font-family:宋体"}[300]{lang="EN-US"}[的路由信息通过。然后定义名为]{style="font-family:宋体"}[test]{lang="EN-US"}[的路由策略，该路由策略编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[的节点定义了一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，它引用的是先前定义的]{style="font-family:宋体"}[as-path]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1902904546}

[\[Sysname\] ip as-path 2 permit \_\*200.\*300]{lang="EN-US"}

[\[Sysname\] route-policy test permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619167662}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_580155814}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1251755993}
:::

::: {#1621162625 .myid}
[]{#_Toc404789252}[]{#struct_0_x1483_x6986_x782457660}

**路由策略 \-- 路由策略公共配置命令 \-- if-match community**

------------------------------------------------------------------------

[**[if-match community]{lang="EN-US"}**]{#struct_0_x1483_x6986_840016576}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的团体属性的匹配条件。]{style="font-family:宋体"}

[**[undo if-match community]{lang="EN-US"}**]{#struct_0_x1483_x6986_1121420447}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1013959848}

[**[if-match community]{lang="EN-US"}**[ { { *basic-community-list-number* \| **name** *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* }&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x1604106231}

[**[undo if-match community ]{lang="EN-US"}**[\[ { *basic-community-list-number* \| **name** *comm-list-name* } \[ **whole-match** \] \| *adv-community-list-number* \]&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x198224356}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619233198}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_582133646}[路由信息的团体属性的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1474807345}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x878086238}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_636271934}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x683801345}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1655064060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x639030989}

[*[basic-community-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_1425924518}[：为基本团体属性列表号，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[adv-community-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_1618643375}[：为高级团体属性列表号，取值范围为]{style="font-family:
宋体"}[100]{lang="EN-US"}[～]{style="font-family:
宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[comm-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x194795764}[：团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个不全为数字的字符串，区分大小写。]{style="font-family:宋体"}

[**[whole-match]{lang="EN-US"}**]{#struct_0_x1483_x6986_1637843991}[：为确切匹配，即所有团体而且仅有这些团体必须出现。]{style="font-family:宋体"}

[[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x731477834}[：表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x521370428}

[[路由策略的]{style="font-family:宋体"}[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_x1297612524}[子句之一，用于过滤]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息，根据路由信息的团体属性指定匹配条件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1535725936}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1953919024}[首先定义一个编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[community-list]{lang="EN-US"}[，允许包含团体号]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[200]{lang="EN-US"}[的路由信息。然后定义名为]{style="font-family:宋体"}[test]{lang="EN-US"}[的路由策略，该路由策略编号为]{style="font-family:宋体"}[10]{lang="EN-US"}[的节点定义了一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，它引用的是先前定义的]{style="font-family:宋体"}[community-list]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x839035867}

[\[Sysname\] ip community-list 1 permit 100 200]{lang="EN-US"}

[\[Sysname\] route-policy test permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-test-10\] if-match community[]{#_Hlt6734710} 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618708911}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply]{lang="EN-US"}[ community]{lang="EN-US"}**]{#struct_0_x1483_x6986_1660922266}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1036239904}
:::

::: {#917336220 .myid}
[]{#_Toc404789253}[]{#struct_0_x1483_x6986_1842998069}[]{#_Toc261870615}[]{#_Toc138041284}

**路由策略 \-- 路由策略公共配置命令 \-- if-match cost**

------------------------------------------------------------------------

[**[if-match cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_32565129}[命令用来配置路由信息的路由开销的匹配条件。]{style="font-family:宋体"}

[**[undo if-match cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_236989409}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1551492936}

[**[if-match cost]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1400443618}

[**[undo if-match cost]{lang="EN-US"}**]{#struct_0_x1483_x6986_x788381691}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_76462394}

[[没有配置路由信息的路由开销的匹配条件。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1618774447}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x991439061}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1303579832}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1707687097}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_17858945}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x636339687}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x371584378}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_695522511}[：路由开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1291599804}

[[路由策略的]{style="font-family:宋体"}[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_x475243939}[子句之一，指定满足条件的路由信息的路由开销。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618839983}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1065405343}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许路由开销为]{style="font-family:宋体"}[8]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x318923149}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match cost 8]{lang="EN-US"}
:::

::: {#-1845878106 .myid}
[]{#_Toc261870618}[]{#_Toc138041287}[]{#_Toc94931051}[]{#_Toc94586783}[]{#_Toc77992915}[]{#_Toc65741005}[]{#_Toc61239916}[]{#_Toc53707332}[]{#_Toc404789254}[]{#struct_0_x1483_x6986_250639661}[]{#_Toc263865744}[]{#_Toc261870616}[]{#_Toc138041285}[]{#_Toc94931046}[]{#_Toc94586778}[]{#_Toc77992913}[]{#_Toc136509635}[]{#_Toc136509636}[]{#_Toc136509637}[]{#_Toc136509638}[]{#_Toc136509639}[]{#_Toc136509640}[]{#_Toc136509641}[]{#_Toc136509642}[]{#_Toc136509643}[]{#_Toc136509644}[]{#_Toc136509645}[]{#_Toc136509646}[]{#_Toc136509647}[]{#_Toc136509648}[]{#_Toc136509649}[]{#_Toc136509650}[]{#_Toc136509651}[]{#_Toc136509652}

**路由策略 \-- 路由策略公共配置命令 \-- if-match extcommunity**

------------------------------------------------------------------------

[**[if-match]{lang="EN-US"}**[ **extcommunity**]{lang="EN-US"}]{#struct_0_x1483_x6986_2049835004}[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的扩展团体属性的匹配条件。]{style="font-family:宋体"}

[**[undo if-match extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_1472518268}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x82604154}

[**[if-match extcommunity]{lang="EN-US"}**[ *ext-comm-list-number*&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_2002744587}

[**[undo if-match extcommunity]{lang="EN-US"}**[ \[ *ext-comm-list-number*&\<1-32\> \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x682169938}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618381231}

[[没有配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1403154263}[路由信息的扩展团体属性的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x760523308}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x481198347}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_175873931}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_531322091}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1877275746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1899523298}

[*[ext-comm-list-number]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_1166108880}[：扩展团体属性列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1618446767}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x199823916}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配已存在的扩展团体列表号]{style="font-family:宋体"}[100]{lang="EN-US"}[和]{style="font-family:宋体"}[150]{lang="EN-US"}[定义的扩展团体属性的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_591579351}

[\[Sysname\] ip extcommunity-list 100 permit rt 100:100]{lang="EN-US"}

[\[Sysname\] ip extcommunity-list 150 permit rt 150:150]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match extcommunity 100 150]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1211340536}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1712323253}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip extcommunity-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1229820409}
:::

::: {#-2017696899 .myid}
[]{#_Toc404789255}[]{#struct_0_x1483_x6986_49259565}[]{#_Toc263865745}[]{#_Toc261870617}[]{#_Toc138041286}[]{#_Toc17101171}

**路由策略 \-- 路由策略公共配置命令 \-- if-match interface**

------------------------------------------------------------------------

[**[if-match interface]{lang="EN-US"}**]{#struct_0_x1483_x6986_1656044097}[命令用来配置路由信息的出接口的匹配条件。]{style="font-family:宋体"}

[**[undo if-match interface]{lang="EN-US"}**]{#struct_0_x1483_x6986_1618512303}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1771824309}

[**[if-match interface ]{lang="EN-US"}**[{ *interface-type interface-number* }&\<1-16\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x1757725206}

[**[undo if-match interface ]{lang="EN-US"}**[\[ *interface-type interface-number* \]]{lang="EN-US"}[&\<1-16\>]{lang="EN-US"}]{#struct_0_x1483_x6986_956537956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_238240187}

[[没有配置路由信息的出接口的匹配条件。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1174544369}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_142484035}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1384133339}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1409024695}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1618577839}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1705474333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_488240596}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_48998908}[：指定接口类型和编号。]{style="font-family:宋体"}

[[&\<1-16\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x1949087675}[：表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x305428340}

[[将路由策略应用到]{style="font-family:宋体"}[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1182820802}[时，]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议不支持配置路由信息的出接口的匹配条件。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_130187204}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1483_x6986_x1277740624}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_692203437}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1619167663}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match interface gigabitethernet 1/0/1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1483_x6986_580090278}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x18011999}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配出接口为]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_680662051}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match interface vlan-interface 1]{lang="EN-US"}
:::

::: {#-344921165 .myid}
[]{#_Toc404789256}[]{#struct_0_x1483_x6986_x439483072}[]{#_Toc263865757}[]{#_Toc261870629}[]{#_Toc138041297}

**路由策略 \-- 路由策略公共配置命令 \-- if-match local-preference**

------------------------------------------------------------------------

[**[if-match ]{lang="EN-US"}**]{#struct_0_x1483_x6986_786323251}**[local-preference]{lang="EN-US"}**[命令用来配置]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级]{style="font-family:宋体"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ]{lang="EN-US"}**]{#struct_0_x1483_x6986_x255384775}**[local-preference]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1619233199}

[**[if-match]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1483_x6986_582199182}**[local-preference ]{lang="EN-US"}***[preference]{lang="EN-US"}*

[**[undo if-match]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x1483_x6986_1673827950}**[local-preference]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1725922058}

[[没有配置]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1012800497}[BGP]{lang="EN-US"}[路由信息的本地优先级]{style="font-family:宋体"}[的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_261686308}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1546754402}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1934455048}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_532860300}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x185302669}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110239977}

[*[preference]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1575933525}[：]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1934266097}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_130755614}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[BGP]{lang="EN-US"}[路由信息的本地优先级]{style="font-family:宋体"}[为]{style="font-family:宋体"}[2]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x483128199}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match preference 2]{lang="EN-US"}
:::

::: {#-778603946 .myid}
[]{#_Toc404789257}[]{#struct_0_x1483_x6986_76324744}[]{#_Toc343692476}[]{#_Toc340065886}

**路由策略 \-- 路由策略公共配置命令 \-- if-match mac-list**

------------------------------------------------------------------------

[**[if-match mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1533686312}[命令用来配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址]{style="font-family:宋体"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1420176291}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110174441}

[**[if-match mac-list ]{lang="EN-US"}***[mac-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_311779430}

[**[undo if-match mac-list]{lang="EN-US"}**[ *mac-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_1718079282}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1250151079}

[[没有配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1483_x6986_x1049272308}[地址的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1840105264}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x223655443}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1238475725}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x2133996142}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1440944479}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110108905}

[*[mac-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_1270564976}[：指定用于过滤]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63 ]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1395980597}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1172381697}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一个]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址匹配已存在的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表]{style="font-family:宋体"}[p1]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysnam]{lang="EN-US"}[e\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_351480508}

[\[Sysname\] route-policy policy1 permit node 10 ]{lang="EN-US"}

[\[Sysname-route-policy-polic]{lang="EN-US"}[y1-10\]]{lang="EN-US"}[ ]{lang="EN-US"}[if-match mac-list p1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1331446175}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1709648734}
:::

::::: {#1537121915 .myid}
[]{#_Toc404789258}[]{#struct_0_x1483_x6986_392386819}

**路由策略 \-- 路由策略公共配置命令 \-- if-match mpls-label**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](路由策略命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1483_x6986_x1473917243}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令支持的情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x1483_x6986_1468006693}
:::

[ ]{lang="EN-US"}

[**[if-match mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_2064715621}[命令用来配置路由信息的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签的匹配条件。]{style="font-family:宋体"}

[**[undo if-match mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_283020853}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110043369}

[**[if-match mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_1476761082}

[**[undo if-match mpls-label]{lang="EN-US"}**]{#struct_0_x1483_x6986_1999945731}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1641892522}

[[没有配置路由信息的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}]{#struct_0_x1483_x6986_x1111580088}[标签的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1697496661}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x926011820}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1462793489}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1698148660}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110502121}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2046223644}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1368891059}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配路由信息的]{style="font-family:宋体"}[MPLS]{lang="EN-US"}[标签。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1518669747}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match mpls-label]{lang="EN-US"}
:::::

::: {#-180185554 .myid}
[]{#_Toc261870620}[]{#_Toc138041289}[]{#_Toc17101175}[]{#_Toc404789259}[]{#struct_0_x1483_x6986_496579867}[]{#_Toc263865747}[]{#_Toc261870619}[]{#_Toc138041288}[]{#_Toc94931052}[]{#_Toc94586784}[]{#_Toc77992916}[]{#_Toc65741006}[]{#_Toc61239917}[]{#_Toc53707333}

**路由策略 \-- 路由策略公共配置命令 \-- if-match route-type**

------------------------------------------------------------------------

[**[if-match route-type]{lang="EN-US"}**]{#struct_0_x1483_x6986_1021876823}[命令用来配置路由信息类型的匹配条件]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo if-match route-type]{lang="EN-US"}**]{#struct_0_x1483_x6986_1543981476}[命令用来取消该配置。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1378961586}

[**[if-match route-type]{lang="EN-US"}**[ { **external**-**type1** \| **external-type1or2** \| **external-type2** \| **internal** \| **is-is-level-1** \| **is-is-level-2** \| **nssa-external-type1** \| **nssa-external-type1or2** \| **nssa-external-type2** } \*]{lang="EN-US"}]{#struct_0_x1483_x6986_x550281370}

[**[undo if-match route-type]{lang="EN-US"}**[ \[ **external**-**type1** \| **external-type1or2** \| **external-type2** \| **internal** \| **is-is-level-1** \| **is-is-level-2** \| **nssa-external-type1** \| **nssa-external-type1or2** \| **nssa-external-type2** \] \*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110436585}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1362750747}

[[没有配置路由信息的类型的匹配条件。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1036536812}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x455760168}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1106906454}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1845635832}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_557897631}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1975115420}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1880199863}

[**[external-type1]{lang="EN-US"}**]{#struct_0_x1483_x6986_x923580648}[：]{style="font-family:宋体"}[OSPF Type1]{lang="EN-US"}[的外部路由。]{style="font-family:宋体"}

[**[external-type1or2]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110371049}[：]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[外部路由。]{style="font-family:宋体"}

[**[external-type2]{lang="EN-US"}**]{#struct_0_x1483_x6986_270665026}[：]{style="font-family:宋体"}[OSPF Type2]{lang="EN-US"}[的外部路由。]{style="font-family:宋体"}

[**[internal]{lang="EN-US"}**]{#struct_0_x1483_x6986_x11724880}[：内部路由（包括]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[区域间和区域内路由）。]{style="font-family:宋体"}

[**[is-is-level-1]{lang="EN-US"}**]{#struct_0_x1483_x6986_x285116717}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[is-is-level-2]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1140052578}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[nssa-external-type1]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1763164130}[：]{style="font-family:宋体"}[OSPF NSSA Type1]{lang="EN-US"}[的外部路由。]{style="font-family:宋体"}

[**[nssa-external-type1or2]{lang="EN-US"}**]{#struct_0_x1483_x6986_x420007539}[：]{style="font-family:宋体"}[OSPF NSSA]{lang="EN-US"}[的外部路由。]{style="font-family:宋体"}

[**[nssa-external-type2]{lang="EN-US"}**]{#struct_0_x1483_x6986_2027260890}[：]{style="font-family:宋体"}[OSPF NSSA Type2]{lang="EN-US"}[的外部路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2019023066}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110305513}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配]{style="font-family:宋体"}[internal]{lang="EN-US"}[类型的路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_2035954090}

[\[Sysname\] route-policy policy1 permit node 10 ]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match route-type internal]{lang="EN-US"}
:::

::: {#-1252443321 .myid}
[]{#_Toc404789260}[]{#struct_0_x1483_x6986_x540527396}

**路由策略 \-- 路由策略公共配置命令 \-- if-match tag**

------------------------------------------------------------------------

[**[if-match tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_x403846610}[命令用来配置]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由信息标记的匹配条件。]{style="font-family:宋体"}

[**[undo if-match tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_1774639899}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x520610982}

[**[if-match tag]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x1483_x6986_x519962207}

[**[undo if-match tag]{lang="EN-US"}**]{#struct_0_x1483_x6986_1681123787}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1213530799}

[[没有配置]{style="font-family:宋体"}[IGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109715689}[路由信息标记的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_709949071}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1536082366}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1123047417}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x887085938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x236418290}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1873315698}

[*[value]{lang="EN-US"}*]{#struct_0_x1483_x6986_1444713204}[：指定要求的标记值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_321965786}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109650153}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，匹配标记为]{style="font-family:宋体"}[8]{lang="EN-US"}[的]{style="font-family:宋体"}[IGP]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_556358368}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match tag 8]{lang="EN-US"}
:::

::: {#-367997305 .myid}
[]{#_Toc261870622}[]{#_Toc138041291}[]{#_Toc263865749}[]{#_Toc261870621}[]{#_Toc138041290}[]{#_Toc135642939}[]{#_Toc94930933}[]{#_Toc94586665}[]{#_Toc404789261}[]{#struct_0_x1483_x6986_x877289227}[]{#_Toc343692480}[]{#_Toc340065887}

**路由策略 \-- 路由策略公共配置命令 \-- if-match vlan**

------------------------------------------------------------------------

[**[if-match vlan]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1455757208}[命令用来配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match vlan]{lang="EN-US"}**]{#struct_0_x1483_x6986_144827424}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1596223920}

[**[if-match vlan ]{lang="EN-US"}***[vlan-list]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1110239976}

[**[undo if-match vlan ]{lang="EN-US"}**[\[ *vlan-list* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1152949830}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_636179494}

[[没有配置]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_x1483_x6986_1769015208}[的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1291033298}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_446429907}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1212026581}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x670372269}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110174440}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1254304511}

[*[vlan-list]{lang="EN-US"}*]{#struct_0_x1483_x6986_113415810}[：]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[列表，表示多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号。表示方式为]{style="font-family:宋体"}*[vlan-list]{lang="EN-US"}*[ = { *vlan-id* \[ to *vlan-id* \] }&\<1-16\>]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-16\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[16]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110108904}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1458318379}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一个]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许]{style="font-family:宋体"}[VLAN 10]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN 100]{lang="EN-US"}[到]{style="font-family:宋体"}[200]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> syste]{lang="EN-US"}[m-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x2111879577}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match vlan 10 ]{lang="EN-US"}[100 to 200]{lang="EN-US"}
:::

::: {#-624939694 .myid}
[]{#_Toc404789262}[]{#struct_0_x1483_x6986_1843963174}

**路由策略 \-- 路由策略公共配置命令 \-- ip as-path**

------------------------------------------------------------------------

[**[ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x346567145}[命令用来配置一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表。]{style="font-family:宋体"}

[**[undo ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_924502572}[命令用来删除指定的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x720436337}

[**[ip as-path]{lang="EN-US"}**[ *as-path-number* { **deny** \| **permit** } *regular-expression*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110043368}

[**[undo ip as-path]{lang="EN-US"}**[ *as-path-number* \[ *regular-expression* \| **deny** \| **permit** \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1252122273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1067860837}

[[没有配置]{style="font-family:宋体"}[AS]{lang="EN-US"}]{#struct_0_x1483_x6986_415978380}[路径过滤列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x213273950}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1803520987}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_985497992}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x346131395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_484607327}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2129443379}

[*[as-path-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1110502120}[：指定的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_x480139703}[：指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的匹配模式为拒绝模式。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_986190890}[：指定]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表的匹配模式为允许模式。]{style="font-family:宋体"}

[*[regular-expression]{lang="EN-US"}*]{#struct_0_x1483_x6986_x39072283}[：]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_260586773}

[[BGP]{lang="EN-US"}]{#struct_0_x1483_x6986_x1239190578}[协议的路由信息中，包含一个]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径域，在]{style="font-family:宋体"}[BGP]{lang="EN-US"}[协议交换路由信息的过程中，该路由所经过的所有]{style="font-family:宋体"}[AS]{lang="EN-US"}[都会记录在这个域中。试图识别]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径列表就是要把其与一个正则表达式进行比较。一个正则表达式就是用一个公式代表的字符组合。例如]{style="font-family:宋体"}[\^200. \*100\$]{lang="EN-US"}[，表示匹配所有]{style="font-family:宋体"}[AS 200]{lang="EN-US"}[开始、以]{style="font-family:宋体"}[AS 100]{lang="EN-US"}[结束的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径域。]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径正则表达式所用到的特殊字符及其含义，请参见"基础配置指导"中的"]{style="font-family:宋体"}[CLI]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x253874762}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1109729439}[配置序号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径过滤列表，允许]{style="font-family:宋体"}[AS_PATH]{lang="EN-US"}[以]{style="font-family:宋体"}[10]{lang="EN-US"}[开头的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x540459777}

[\[Sysname\] ip as-path 1 permit \^10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1620956473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110436584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1366132608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match ]{lang="EN-US"}[as-path]{lang="EN-US"}**]{#struct_0_x1483_x6986_1358052579}
:::

::: {#-288209310 .myid}
[]{#_Toc404789263}[]{#struct_0_x1483_x6986_1655651296}

**路由策略 \-- 路由策略公共配置命令 \-- ip community-list**

------------------------------------------------------------------------

[**[ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1254576068}[命令用来配置一个团体属性列表表项。]{style="font-family:宋体"}

[**[undo ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_450946433}[命令用来删除指定的团体属性列表或其某个表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1523835351}

[**[ip community-list]{lang="EN-US"}**[ { *basic-comm-list-num* \| **basic** *basic-comm-list-name* } { **deny** \| **permit** } \[ *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \] \[ **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** \] \*]{lang="EN-US"}]{#struct_0_x1483_x6986_1703925003}

[**[undo ip community-list ]{lang="EN-US"}**[{ *basic-comm-list-num* \| **basic** *basic-comm-list-name* } \[ **deny** \| **permit** \] \[ *community-number*&\<1-32\> \| *aa:nn*&\<1-32\> \] \[ **internet** \| **no-advertise** \| **no-export** \| **no-export-subconfed** \] \*]{lang="EN-US"}]{#struct_0_x1483_x6986_623471049}

[**[ip community-list]{lang="EN-US"}**[ { *adv-comm-list-num* \| **advanced** *adv-comm-list-name* } { **deny** \| **permit** } *regular-expression*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110371048}

[**[undo ip community-list ]{lang="EN-US"}**[{ *adv-comm-list-num* \| **advanced** *adv-comm-list-name* } \[ **deny** \| **permit** \] \[ *regular-expression* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1295418915}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_385426165}

[[没有配置团体属性列表。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1131501651}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1398203584}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_273516751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x29054360}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1880504267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x2085241208}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1932859782}

[*[basic-comm-list-num]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1110305512}[：基本团体属性列表号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[basic]{lang="EN-US"}**]{#struct_0_x1483_x6986_x692929265}[：标识基本团体属性名字。]{style="font-family:宋体"}

[**[advanced]{lang="EN-US"}**]{#struct_0_x1483_x6986_453512468}[：标识]{style="font-family:宋体"}[高级团体属性名字。]{style="font-family:宋体"}

[*[basic-comm-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_123088210}[：基本团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个不全为数字的字符串，区分大小写。]{style="font-family:宋体"}

[*[adv-comm-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x480510647}[：高级团体属性列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个不全为数字的字符串，区分大小写。]{style="font-family:宋体"}

[*[adv-comm-list-num]{lang="EN-US"}*]{#struct_0_x1483_x6986_574702799}[：高级团体属性列表号，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[regular-expression]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1737036845}[：指定高级团体属性的正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。有关正则表达式的详细介绍，请参见"基础配置指导"中的"]{style="font-family:宋体"}[CLI]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_x449397969}[：指定团体属性列表的匹配模式为拒绝模式。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_x797718036}[：指定团体属性列表的匹配模式为允许模式。]{style="font-family:宋体"}

[*[community-number]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x395345556}[：团体序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[*[aa:nn]{lang="EN-US"}*[&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109715688}[：团体号，]{style="font-family:宋体"}*[aa]{lang="EN-US"}*[和]{style="font-family:宋体"}*[nn]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[internet]{lang="EN-US"}**]{#struct_0_x1483_x6986_x856134870}[：预定义的团体属性。缺省情况下，所有的路由都具有]{style="font-family:宋体"}**[internet]{lang="EN-US"}**[团体属性，可以被通告给所有的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[no-advertise]{lang="EN-US"}**]{#struct_0_x1483_x6986_1934696341}[：具有此属性的路由在收到后，不能被通告给任何其他的]{style="font-family:宋体"}[BGP]{lang="EN-US"}[对等体。]{style="font-family:宋体"}

[**[no-export]{lang="EN-US"}**]{#struct_0_x1483_x6986_2110204831}[：具有此属性的路由在收到后，不能被发布到本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[之外。如果使用了联盟，则不能被发布到联盟之外，但可以发布给联盟中的其他子]{style="font-family:宋体"}[AS]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[no-export-subconfed]{lang="EN-US"}**]{#struct_0_x1483_x6986_1345047245}[：具有此属性的路由在收到后，不能被发布到本地]{style="font-family:宋体"}[AS]{lang="EN-US"}[之外，也不能发布到联盟中的其他子]{style="font-family:宋体"}[AS]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x511771437}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1855348257}[配置序号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的基本团体属性列表，允许]{style="font-family:宋体"}**[internet]{lang="EN-US"}**[团体]{style="font-family:宋体"}[属性的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1554527735}

[\[Sysname\] ip community-list 1 permit internet]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_766084885}[创建序号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的高级团体属性列表，允许团体属性内容以"]{style="font-family:宋体"}[10]{lang="EN-US"}["开头的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109650152}

[\[Sysname\] ip community-list 100 permit \^10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1009725573}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply comm-list delete]{lang="EN-US"}**]{#struct_0_x1483_x6986_695152942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply]{lang="EN-US"}[ community]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1866320126}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip community-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_575445227}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match community]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1467667615}
:::

::: {#613304486 .myid}
[]{#_Toc261870624}[]{#_Toc138041293}[]{#_Toc404789264}[]{#struct_0_x1483_x6986_1943511816}[]{#_Toc263865751}[]{#_Toc261870623}[]{#_Toc138041292}[]{#_Toc94931054}[]{#_Toc94586786}[]{#_Toc73872531}[]{#_Toc73872533}[]{#_Toc73872534}[]{#_Toc73872535}[]{#_Hlt8895559}[]{#_Toc73872536}[]{#_Toc73872537}[]{#_Toc73872538}[]{#_Toc73872539}[]{#_Toc73872540}[]{#_Toc73872541}[]{#_Toc136509661}[]{#_Toc136509662}[]{#_Toc136509663}[]{#_Toc136509664}[]{#_Toc136509665}[]{#_Toc136509666}[]{#_Toc136509667}[]{#_Toc136509668}[]{#_Toc136509669}[]{#_Toc136509670}[]{#_Toc136509671}[]{#_Toc136509672}[]{#_Toc136509673}[]{#_Toc136509674}[]{#_Toc136509675}[]{#_Toc136509676}[]{#_Toc136509677}[]{#_Toc136509678}[]{#_Toc136509679}[]{#_Toc136509680}[]{#_Toc136509681}[]{#_Toc136509683}[]{#_Toc136509684}[]{#_Toc136509685}[]{#_Toc136509686}[]{#_Toc136509687}[]{#_Toc136509688}[]{#_Toc136509689}[]{#_Toc136509690}[]{#_Toc136509691}[]{#_Toc136509692}[]{#_Toc136509693}[]{#_Toc136509694}[]{#_Toc136509695}

**路由策略 \-- 路由策略公共配置命令 \-- ip extcommunity-list**

------------------------------------------------------------------------

[**[ip extcommunity-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1429321679}[命令用来配置一个扩展团体属性列表表项。]{style="font-family:宋体"}

[**[undo ip extcommunity-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x880105315}[命令用来删除指定的扩展团体属性列表。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110239979}

[**[ip extcommunity-list]{lang="EN-US"}**[ *ext-comm-list-number* { **deny** \| **permit** } { **rt** *route-target* \| **soo** *site-of-origin* }&\<1-32\>]{lang="EN-US"}]{#struct_0_x1483_x6986_1912464717}

[**[undo ip extcommunity-list]{lang="EN-US"}**[ *ext-comm-list-number* \[ { **deny** \| **permit** } \[ **rt** *route-target* \| **soo** *site-of-origin* \]&\<1-32\> \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1295046412}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2113552866}

[[没有配置扩展团体属性列表。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1106767981}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1489032184}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1543393898}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x335596458}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1023015235}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110174443}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x851019984}

[*[ext-comm-list-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x466279974}[：扩展团体属性列表号，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[199]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1985023906}[：指定扩展团体属性列表的匹配模式为拒绝模式。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_620506260}[：指定扩展团体属性列表的匹配模式为允许模式。]{style="font-family:宋体"}

[**[rt]{lang="EN-US"}**[ ]{lang="EN-US"}*[route-target]{lang="EN-US"}*]{#struct_0_x1483_x6986_608116015}[：指定的]{style="font-family:宋体"}[RT]{lang="EN-US"}[（]{style="font-family:宋体"}[Route Target]{lang="EN-US"}[，路由目标）扩展团体属性，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次。]{style="font-family:宋体"}

[**[soo]{lang="EN-US"}**[ *site-of-origin*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1143372629}[：指定的]{style="font-family:宋体"}[SoO]{lang="EN-US"}[（]{style="font-family:宋体"}[Site of Origin]{lang="EN-US"}[，源站点）扩展团体属性，为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[21]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[。]{style="font-family:宋体"}[&\<1-32\>]{lang="EN-US"}[表示前面的参数可以输入]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[次]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[route-target]{lang="EN-US"}*]{#struct_0_x1483_x6986_438000015}[和]{style="font-family:宋体"}*[site-of-origin]{lang="EN-US"}*[有三种形式，分别如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[16]{lang="EN-US"}]{#struct_0_x1483_x6986_x303209876}[位自治系统号]{style="font-family:宋体"}[:32]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[101:3]{lang="EN-US"}[。其中，自治系统号取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1483_x6986_1709967916}[位]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[192.168.122.15:1]{lang="EN-US"}[。其中，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[32]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110108907}[位自治系统号]{style="font-family:宋体"}[:16]{lang="EN-US"}[位用户自定义数，例如：]{style="font-family:宋体"}[70000:3]{lang="EN-US"}[。其中，自治系统号取值范围为]{style="font-family:宋体"}[65536]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，用户自定义数取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_107765562}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x61042028}[配置序号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的扩展团体属性列表，允许]{style="font-family:宋体"}[RT]{lang="EN-US"}[为]{style="font-family:宋体"}[200:200]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x50867548}

[\[Sysname\] ip extcommunity-list 1 permit rt 200:200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x2141402007}[配置序号为]{style="font-family:宋体"}[2]{lang="EN-US"}[的扩展团体属性列表，允许]{style="font-family:宋体"}[SoO]{lang="EN-US"}[为]{style="font-family:宋体"}[100:100]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x239640668}

[\[Sysname\] ip extcommunity-list 2 permit soo 100:100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_363215026}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply extcommunity]{lang="EN-US"}**]{#struct_0_x1483_x6986_705760371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip extcommunity-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1304318829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match]{lang="EN-US"}**[ **extcommunity**]{lang="EN-US"}]{#struct_0_x1483_x6986_660604142}
:::

::: {#2028115257 .myid}
[]{#_Toc404789265}[]{#struct_0_x1483_x6986_x966231299}[]{#_Toc343692484}[]{#_Toc340065884}

**路由策略 \-- 路由策略公共配置命令 \-- mac-list**

------------------------------------------------------------------------

[**[mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110043371}[命令用来配置一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表。]{style="font-family:宋体"}

[**[undo mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1833056978}[命令用来删除一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表或其某个表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1285827562}

[**[mac-list]{lang="EN-US"}**[ *mac-list-name* \[ **index** *index-number* \] { **deny** \| **permit** } *mac-address* \[ *mask-length* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1212535873}

[**[undo mac-list ]{lang="EN-US"}***[mac-list-name]{lang="EN-US"}*[ \[ **index** *index-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1046584754}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_401804354}

[[没有配置]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_x1483_x6986_x169569715}[地址列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_230879465}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1659431353}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1563340782}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110502123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1085944238}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1733183670}

[*[mac-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x276461157}[：指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表名，唯一标识一个]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，区分大小写]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[index-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_177114599}[：标识]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表中的一条表项，]{style="font-family:宋体"}*[index-number]{lang="EN-US"}*[小的表项先被测试，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_69440175}[：指定所定义的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在该表项指定的前缀范围内时，则该]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不能通过该表项的过滤，并且不会进行下一个表项的测试，否则进入下一表项的测试。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_1375595565}[：指定所定义的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个结点的测试；如待过滤的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址不在该表项指定的前缀范围内，则进行下一表项测试。]{style="font-family:宋体"}

[*[mac-address mask-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1120562641}[：指定]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀和前缀长度，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[48]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2110401241}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110436587}[定义一条名为]{style="font-family:宋体"}[wxy]{lang="EN-US"}[的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表，只允许]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址范围是]{style="font-family:宋体"}[001b-2188-0000]{lang="EN-US"}[～]{style="font-family:宋体"}[001b-2188-ffff]{lang="EN-US"}[的通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1769417135}

[\[Sysname\] mac-list wxy permit 001b-2188-946c 32]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1331118493}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[if-match mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_492681677}
:::

::: {#1282310782 .myid}
[]{#_Toc404789266}[]{#struct_0_x1483_x6986_x267484281}[]{#_Toc343692485}[]{#_Toc340065885}

**路由策略 \-- 路由策略公共配置命令 \-- reset mac-list**

------------------------------------------------------------------------

[**[reset mac-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1978069944}[命令用来清除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1917510760}

[**[reset mac-list]{lang="EN-US"}**[ \[ *mac-list-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x256575683}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1235790699}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1513679693}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x504539823}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110371051}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x85630870}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1042716416}

[*[mac-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x802584620}[：]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2116631635}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1425992686}[清除]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址列表]{style="font-family:宋体"}[abc]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset mac-list abc]{lang="EN-US"}]{#struct_0_x1483_x6986_x561414069}
:::

::: {#261570064 .myid}
[]{#_Toc404789267}[]{#struct_0_x1483_x6986_1216017333}

**路由策略 \-- 路由策略公共配置命令 \-- route-policy**

------------------------------------------------------------------------

[**[route-policy]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1723041343}[命令用来创建路由策略，并进入该路由策略视图。]{style="font-family:宋体"}

[**[undo route-policy]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110305515}[命令用来删除指定的路由策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_873154676}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name* { **deny** \| **permit** } **node** *node-number*]{lang="EN-US"}]{#struct_0_x1483_x6986_1021592870}

[**[undo route-policy]{lang="EN-US"}**[ *route-policy-name* \[ **deny** \| **permit** \] \[ **node** *node-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x429646738}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1491474529}

[[没有配置路由策略。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1259591017}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1045019517}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1295874515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1909550627}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109715691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_353653175}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1540069477}

[*[route-policy-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_727997775}[：指定路由策略名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_x12557458}[：指定所定义的路由策略节点的匹配模式为拒绝模式，当路由项满足该节点的所有]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句时被拒绝通过该节点的过滤，并且不会进行下一个节点的匹配；如果路由项不满足该节点的]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，将进入下一个节点继续匹配。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_667758293}[：指定所定义的路由策略节点的匹配模式为允许模式。当路由项满足该节点的所有]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句时被允许通过该节点的过滤并执行该节点的]{style="font-family:宋体"}[apply]{lang="EN-US"}[子句，如路由项不满足该节点的]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，将继续匹配该路由策略的下一个节点。]{style="font-family:宋体"}

[**[node]{lang="EN-US"}***[ node-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_1403715569}[：标识路由策略中的一个节点索引，当该路由策略用于路由信息过滤时，]{style="font-family:宋体"}*[node-number]{lang="EN-US"}*[小的节点先被匹配，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x596088170}

[[路由策略用于路由信息过滤。一个路由策略由若干节点组成，每一节点由一些]{style="font-family:宋体"}[if-match]{lang="EN-US"}]{#struct_0_x1483_x6986_1284669543}[子句和]{style="font-family:宋体"}[apply]{lang="EN-US"}[子句组成。]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句定义该节点的匹配规则，]{style="font-family:宋体"}[apply]{lang="EN-US"}[子句定义通过该节点过滤后进行的动作。节点的]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句之间的过滤关系是"与"的关系，即必须满足该节点的所有]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句。路由策略节点之间的过滤关系是"或"的关系，即通过一个节点的过滤就意味着通过该路由策略的过滤。若没有通过任一节点的过滤，则表示没有通过该路由策略的过滤。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x716880145}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109650155}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[，并进入路由策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1719157782}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1994163816}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display route-policy]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1184604650}
:::

::::: {#-832266460 .myid}
[]{#_Toc138041295}[]{#_Toc404789269}[]{#struct_0_x1483_x6986_x1647739341}[]{#_Toc261870626}[]{#_Toc192320386}[]{#_Toc189305430}

**路由策略 \-- IPv4路由策略配置命令 \-- apply fast-reroute**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](路由策略命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1483_x6986_x281182681}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x1483_x6986_1087527721}
:::

[ ]{lang="EN-US"}

[**[apply]{lang="EN-US"}**[ **fast-reroute**]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110239978}[命令用来配置快速重路由备份。]{style="font-family:宋体"}

[**[undo apply]{lang="EN-US"}**[ **fast-reroute**]{lang="EN-US"}]{#struct_0_x1483_x6986_346380776}[命令用来取消快速重路由配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x663258599}

[**[apply]{lang="EN-US"}**[ **fast-reroute** { **backup-interface** *interface-type interface-number* \[ **backup-nexthop** *ip-address* \] \| **backup-nexthop** *ip-address* }]{lang="EN-US"}]{#struct_0_x1483_x6986_1331708317}

[**[undo apply fast-reroute]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1526907556}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x233460203}

[[没有配置快速重路由。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_998367891}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x881332225}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1784849579}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110174442}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1877863371}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1991288991}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_175551502}

[**[backup-interface]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_110615912}[：备份出接口。对于备份出接口为非]{style="font-family:宋体"}[P2P]{lang="EN-US"}[类型的接口时（包括]{style="font-family:宋体"}[NBMA]{lang="EN-US"}[类型接口或广播类型接口，如以太网接口、]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口等），必须同时指定其对应的备份下一跳地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[为指定的接口类型和编号。]{style="font-family:
宋体"}

[**[backup-nexthop]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x1483_x6986_1162951996}[：备份下一跳地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2106341559}

[[当网络中的链路或某台路由器发生故障时，需要通过故障链路或故障路由器传输才能到达目的地的报文将会丢失或产生路由环路，数据流量将会被中断，直到路由协议根据新的拓扑网络路由收敛完毕后，被中断的流量才能恢复正常的传输。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1443338018}

[[网络管理员可以为路由协议配置快速重路由功能，路由协议将通过路由策略为路由指定备份下一跳，当路由器探测到网络故障时，路由协议会使用事先指定好的备份下一跳替换失效下一跳，通过备份下一跳来指导报文的转发，从而大大缩短了流量中断时间。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_6613202}

[[网络管理员可以在路由策略中配置快速重路由功能的指定备份下一跳，为符合过滤条件的路由指定备份下一跳。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1110108906}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1673849503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1483_x6986_179706507}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x452282748}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，为到达目的地]{style="font-family:宋体"}[100.1.1.0/24]{lang="EN-US"}[的路由配置备份出接口为]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[，备份下一跳地址为]{style="font-family:宋体"}[193.1.1.8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_945555629}

[\[Sysname\] ip prefix-list abc index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ip address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply fast-reroute backup-interface gigabitethernet 1/0/1 backup-nexthop 193.1.1.8]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1483_x6986_x1870428435}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1166287655}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，为到达目的地]{style="font-family:宋体"}[100.1.1.0/24]{lang="EN-US"}[的路由配置备份出接口为]{style="font-family:宋体"}[Vlan-interface1]{lang="EN-US"}[，备份下一跳地址为]{style="font-family:宋体"}[193.1.1.8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110043370}

[\[Sysname\] ip prefix-list abc index 10 permit 100.1.1.0 24]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ip address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply fast-reroute backup-interface vlan-interface 1 backup-nexthop 193.1.1.8]{lang="EN-US"}
:::::

::: {#660868751 .myid}
[]{#_Toc261870628}[]{#_Toc138041296}[]{#_Toc404789270}[]{#struct_0_x1483_x6986_x895826377}[]{#_Toc263865755}[]{#_Toc261870627}

**路由策略 \-- IPv4路由策略配置命令 \-- apply ip-address next-hop**

------------------------------------------------------------------------

[**[apply ip-address next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_35262428}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息的下一跳地址。]{style="font-family:宋体"}

[**[undo apply ip-address next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_x808186603}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1384307221}

[**[apply ip-address next-hop]{lang="EN-US"}**[ *ip-address* \[ **public** \| **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_1406260584}

[**[undo apply ip-address]{lang="EN-US"}**[ **next-hop**]{lang="EN-US"}]{#struct_0_x1483_x6986_x1214634972}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_789906123}

[[没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110502122}[路由信息的下一跳地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1642939117}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_512606652}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1698838952}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x789794095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1597970303}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1690261381}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1483_x6986_2124866635}[：下一跳]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[public]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1286456028}[：指定公网。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1976344270}[：指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的信息。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110436586}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当引入路由时，使用本命令设置下一跳地址无效。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_203333194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果未指定参数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x779250856}**[public]{lang="EN-US"}**[或]{style="font-family:宋体"}**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*[，则表示下一跳地址为公网地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1319960103}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_900477369}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[AS]{lang="EN-US"}[路径访问列表，那么设置路由信息的下一跳地址为]{style="font-family:宋体"}[193.1.1.8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1924582655}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply ip-address next-hop 193.1.1.8]{lang="EN-US"}
:::

::: {#144798656 .myid}
[]{#_Toc404789271}[]{#struct_0_x1483_x6986_1556225136}

**路由策略 \-- IPv4路由策略配置命令 \-- display ip prefix-list**

------------------------------------------------------------------------

[**[display ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_2085805642}[命令用来显示]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110371050}

[**[display ip prefix-list]{lang="EN-US"}**[ \[ **name** *prefix-list-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1651714811}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_197064933}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x937092273}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1145910558}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x777491791}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_x1047818772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1582439366}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_114628386}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110305514}

[**[name]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1855728679}[：指定显示的地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有已配置的地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_733696390}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_171405593}[显示名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的地址前缀列表的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ip prefix-list name abc]{lang="EN-US"}]{#struct_0_x1483_x6986_1048142584}

[Prefix-list: abc]{lang="EN-US"}

[ Permitted 0]{lang="EN-US"}

[ Denied 0]{lang="EN-US"}

[         index: 10        deny   6.6.6.0/24              ge  26  le  28]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display ip prefix-list]{lang="EN-US"}]{#struct_0_x1483_x6986_693590649}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x677345417}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1686441726}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1109715690}

[[Prefix-list]{lang="EN-US"}]{#struct_0_x1483_x6986_x1212430766}

[[地址前缀列表的名称]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1720200057}

[[Permitted]{lang="EN-US"}]{#struct_0_x1483_x6986_x663265839}

[[符合匹配条件的路由个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1526306905}

[[Denied]{lang="EN-US"}]{#struct_0_x1483_x6986_x481424406}

[[不符合匹配条件的路由个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x231205034}

[[index]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109650154}

[[地址前缀列表的内部序列号]{style="font-family:宋体"}]{#struct_0_x1483_x6986_153073841}

[[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_x428492400}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_666954382}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_1496355664}[：表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_285718175}[：表示拒绝]{lang="EN-US" style="font-family:宋体"}

[[6.6.6.0/24]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110239981}

[[匹配的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1483_x6986_1555775605}[地址和掩码长度]{style="font-family:宋体"}

[[ge]{lang="EN-US"}]{#struct_0_x1483_x6986_1412488616}

[[即]{style="font-family:宋体"}[greater-equal]{lang="EN-US"}]{#struct_0_x1483_x6986_690727288}[，匹配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码长度的下限值]{style="font-family:宋体"}

[[le]{lang="EN-US"}]{#struct_0_x1483_x6986_1690770677}

[[即]{style="font-family:宋体"}[less-equal]{lang="EN-US"}]{#struct_0_x1483_x6986_1748392004}[，匹配的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址掩码长度的上限值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110174445}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x2013819398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x253398584}

::: {#-2125071982 .myid}
[]{#_Toc404789272}[]{#struct_0_x1483_x6986_x133916920}[]{#_Toc261870630}[]{#_Toc138041298}

**路由策略 \-- IPv4路由策略配置命令 \-- if-match ip**

------------------------------------------------------------------------

[**[if-match ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_575994304}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[的路由信息的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_2132784432}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1721447952}

[**[if-match ip]{lang="EN-US"}**[ { **address** \| **next-hop** \| **route-source** } { **acl** *acl-number* \| **prefix-list** *prefix-list-name* }]{lang="EN-US"}]{#struct_0_x1483_x6986_1302773437}

[**[undo if-match ip ]{lang="EN-US"}**[{ ]{lang="EN-US"}**[address]{lang="EN-US"}**[ \| **next-hop** \| **route-source** } \[ **acl** \| **prefix-list** \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110108909}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x342573132}

[[没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1483_x6986_x1586979693}[的路由信息的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_261838320}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1732221487}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_903258297}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1599333423}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_891778553}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x854623111}

[**[address]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110043373}[：匹配]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[路由信息的目的地址。]{style="font-family:宋体"}

[**[next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_670257564}[：匹配下一跳地址。]{style="font-family:宋体"}

[**[route-source]{lang="EN-US"}**]{#struct_0_x1483_x6986_x556774238}[：匹配路由发布的源地址。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1435230148}[：指定用于过滤的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[号]{style="font-family:宋体"}[。对于]{style="font-family:宋体"}**[address]{lang="EN-US"}**[，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[；对于]{style="font-family:宋体"}**[next-hop]{lang="EN-US"}**[和]{style="font-family:宋体"}**[route-source]{lang="EN-US"}**[，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_1153512910}[：指定用于过滤的地址前缀列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_293681977}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1615775786}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一个]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许下一跳地址匹配已存在的地址前缀列表]{style="font-family:宋体"}[p1]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x200048884}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ip next-hop prefix-list p1]{lang="EN-US"}
:::

::: {#-299152360 .myid}
[]{#_Toc404789273}[]{#struct_0_x1483_x6986_x1870228146}[]{#_Toc261870632}[]{#_Toc138041300}

**路由策略 \-- IPv4路由策略配置命令 \-- ip prefix-list**

------------------------------------------------------------------------

[**[ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110502125}[命令用来配置一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表表项。]{style="font-family:宋体"}

[**[undo ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x76855176}[命令用来删除一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表或其某个表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1017408059}

[**[ip prefix-list]{lang="EN-US"}**[ *prefix-list-name* \[ **index** *index-number* \] { **deny** \| **permit** } *ip-address mask-length* \[ **greater-equal** *min-mask-length* \] \[ **less-equal** *max-mask-length* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1588932877}

[**[undo ip prefix-list]{lang="EN-US"}**[ *prefix-list-name* \[ **index** *index-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1155750984}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x823120688}

[[没有配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x1483_x6986_1097990349}[地址前缀列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2134616182}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x296374488}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110436589}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_962848081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1654345988}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_359128612}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1889781472}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[index-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x861878534}[：标识]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表中的一条表项，]{style="font-family:宋体"}*[index-number]{lang="EN-US"}*[小的表项先被匹配，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_717651185}[：指定所定义的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址在该表项指定的前缀范围内时，则该]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址不能通过该表项的过滤，并且不会进行下一个表项的匹配，否则进入下一表项的匹配。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_536520264}[：指定所定义的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个节点的匹配；如待过滤的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址不在该表项指定的前缀范围内，则进行下一表项匹配。]{style="font-family:宋体"}

[*[ip-address mask-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_1881287740}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀和前缀长度，]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[min-mask-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1110371053}[、]{style="font-family:宋体"}*[max-mask-length]{lang="EN-US"}*[：如果]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址和前缀长度都已匹配，则使用该参数来指定地址前缀长度范围。]{style="font-family:宋体"}**[greater-equal]{lang="EN-US"}**[的含义为"大于等于"，]{style="font-family:宋体"}**[less-equal]{lang="EN-US"}**[的含义为"小于等于"，其取值范围为]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[ \<= *min-mask-length* \<= *max-mask-length* \<= 32]{lang="EN-US"}[。如果只指定]{style="font-family:宋体"}*[min-mask-length]{lang="EN-US"}*[时，则前缀长度范围为]{style="font-family:宋体"}[\[ *min-mask-length*]{lang="EN-US"}[，]{style="font-family:宋体"}[32 \]]{lang="EN-US"}[；如果只指定]{style="font-family:宋体"}*[max-mask-length]{lang="EN-US"}*[时，则前缀长度范围为]{style="font-family:宋体"}[\[ *mask-length*]{lang="EN-US"}[，]{style="font-family:宋体"}*[max-mask-length ]{lang="EN-US"}*[\]]{lang="EN-US"}[；如果二者都指定，则前缀长度范围为]{style="font-family:宋体"}[\[ *min-mask-length*]{lang="EN-US"}[，]{style="font-family:宋体"}*[max-mask-length ]{lang="EN-US"}*[\]]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1248430284}

[[IPv4]{lang="EN-US"}]{#struct_0_x1483_x6986_x165298452}[地址前缀列表用于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的过滤。一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表可以有若干条表项，每一表项指定一个地址前缀范围。表项之间的过滤关系是"或"的关系，即通过一条表项的过滤就意味着通过该]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的过滤。若没有通过任一表项的过滤，则不能通过该]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的过滤。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_102267845}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将]{lang="EN-US" style="font-family:宋体"}*[ip-address mask-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_x982394767}[指定为]{lang="EN-US" style="font-family:宋体"}[0.0.0.0 0]{lang="EN-US"}[，则只匹配缺省路由。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果需要匹配所有路由，则应配置为]{lang="EN-US" style="font-family:宋体"}[0.0.0.0 0 **less-equal** 32]{lang="EN-US"}]{#struct_0_x1483_x6986_x1726146821}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_172106305}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1101164107}[定义一条名为]{style="font-family:宋体"}[p1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表，只允许]{style="font-family:宋体"}[10.0.0.0/8]{lang="EN-US"}[网段的，掩码长度为]{style="font-family:宋体"}[17]{lang="EN-US"}[或]{style="font-family:宋体"}[18]{lang="EN-US"}[的路由通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1869276895}

[\[Sysname\] ip prefix-list p1 permit 10.0.0.0 8 greater-equal 17 less-equal 18]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110305517}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x289644738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x647030891}
:::

::: {#-996266294 .myid}
[]{#_Toc404789274}[]{#struct_0_x1483_x6986_1580732514}[]{#_Toc261870633}[]{#_Toc138041301}

**路由策略 \-- IPv4路由策略配置命令 \-- reset ip prefix-list**

------------------------------------------------------------------------

[**[reset ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_1922403801}[命令用来清除指定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2088079661}

[**[reset ip prefix]{lang="EN-US"}[-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_325925562}**[ ]{lang="EN-US"}**[\[]{lang="EN-US"}[ *prefix-list-name* ]{lang="EN-US"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1085068616}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x188951911}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1192278507}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1109715693}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1516452589}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1286136974}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x851198289}[：指定地址前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2059888938}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1715622244}[清除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[abc]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ip prefix-list abc]{lang="EN-US"}]{#struct_0_x1483_x6986_x962654023}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1482159088}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_74860302}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1109650157}
:::

::::: {#-1011138047 .myid}
[]{#_Toc404789276}[]{#struct_0_x1483_x6986_1331118491}[]{#_Toc352055006}[]{#_Toc351995626}

**路由策略 \-- IPv6路由策略配置命令 \-- apply ipv6 fast-reroute**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](路由策略命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x1483_x6986_492812749}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:\"KaiTi_GB2312\",\"serif\""}]{#struct_0_x1483_x6986_1668196840}
:::

[ ]{lang="EN-US"}

[**[apply]{lang="EN-US"}**[ **ipv6** **fast-reroute**]{lang="EN-US"}]{#struct_0_x1483_x6986_1331446171}[命令用来配置快速重路由备份。]{style="font-family:宋体"}

[**[undo apply]{lang="EN-US"}**[ ]{lang="EN-US"}**[ipv6 fast-reroute]{lang="EN-US"}**]{#struct_0_x1483_x6986_1709910878}[命令用来取消快速重路由配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1769463097}

[**[apply]{lang="EN-US"}**[ **ipv6** **fast-reroute backup-nexthop** *ipv6-address*]{lang="EN-US"}]{#struct_0_x1483_x6986_x1853970707}

[**[undo apply ipv6]{lang="EN-US"}**[ **fast-reroute**]{lang="EN-US"}]{#struct_0_x1483_x6986_1646278228}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1331511707}

[[没有配置快速重路由。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x254042147}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1753679979}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1355852538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1629998614}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1331315099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_142265904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x2047652595}

[**[backup-nexthop]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_x1483_x6986_x947833759}[：备份下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1149854414}

[[当网络中的链路或某台路由器发生故障时，需要通过故障链路或故障路由器传输才能到达目的地的报文将会丢失或产生路由环路，数据流量将会被中断，直到路由协议根据新的拓扑网络路由收敛完毕后，被中断的流量才能恢复正常的传输。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1331380635}

[[网络管理员可以为路由协议配置快速重路由功能，路由协议将通过路由策略为路由指定备份下一跳，当路由器探测到网络故障时，路由协议会使用事先指定好的备份下一跳替换失效下一跳，通过备份下一跳来指导报文的转发，从而大大缩短了流量中断时间。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_508368193}

[[网络管理员可以在路由策略中配置快速重路由功能的指定备份下一跳，为符合过滤条件的路由指定备份下一跳。]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1900993484}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_561229360}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_600741521}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，为到达目的地]{style="font-family:宋体"}[100::1/64]{lang="EN-US"}[的路由配置备份下一跳地址为]{style="font-family:宋体"}[1::1/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_1331708315}

[\[Sysname\] ipv6 prefix-list abc index 10 permit 100::1 64]{lang="EN-US"}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ipv6 address prefix-list abc]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply ipv6 fast-reroute backup-nexthop 1::1]{lang="EN-US"}
:::::

::: {#-67960453 .myid}
[]{#_Toc261870636}[]{#_Toc138041304}[]{#_Toc134936986}[]{#_Toc113267976}[]{#_Toc110768972}[]{#_Toc90810124}[]{#_Toc90809385}[]{#_Toc86724128}[]{#_Toc85873643}[]{#_Toc77992912}[]{#_Toc65741003}[]{#_Toc61239914}[]{#_Toc53707330}[]{#_Toc404789277}[]{#struct_0_x1483_x6986_976546394}[]{#_Toc263865763}[]{#_Toc261870635}[]{#_Toc138041303}[]{#_Toc134936975}[]{#_Toc113267968}[]{#_Toc110768964}[]{#_Toc90810114}[]{#_Toc90809375}[]{#_Toc86724118}[]{#_Toc85873633}[]{#_Toc77992906}

**路由策略 \-- IPv6路由策略配置命令 \-- apply ipv6 next-hop**

------------------------------------------------------------------------

[**[apply ipv6 next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_x703279428}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息的下一跳地址。]{style="font-family:宋体"}

[**[undo apply ipv6 next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_x594605520}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1758102581}

[**[apply ipv6 next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_1368538035}[ *ipv6-address*]{lang="EN-US"}

[**[undo apply ipv6 next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_x710758832}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1065650284}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110239980}[路由信息的下一跳地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x10308336}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x878806047}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1001897633}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x566198092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1462010913}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_451805401}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x1483_x6986_x301350260}[：指定下一跳]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_270659847}

[[引入路由时，使用]{style="font-family:宋体"}]{#struct_0_x1483_x6986_752794726}**[apply ipv6 next-hop]{lang="EN-US"}**[命令设置下一跳地址无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1110174444}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_715063957}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。如果匹配已存在的编号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[as-path]{lang="EN-US"}[，那么配置路由的下一跳地址为]{style="font-family:宋体"}[3ffe:506::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x815580513}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match as-path 1]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] apply ipv6 next-hop 3ffe:506::1]{lang="EN-US"}
:::

::: {#-1271555824 .myid}
[]{#_Toc404789278}[]{#struct_0_x1483_x6986_1016648319}

**路由策略 \-- IPv6路由策略配置命令 \-- display ipv6 prefix-list**

------------------------------------------------------------------------

[**[display ipv6 prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_335915450}[命令用来显示]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_896158212}

[**[display ipv6 prefix-list]{lang="EN-US"}**[ \[ **name** *prefix-list-name* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1478142392}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1399859197}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1110108908}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1223510809}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1450560707}

[[network-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_x406549706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x2037970250}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1483_x6986_x1852318359}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_601839865}

[**[name]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_1350863832}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的名称]{style="font-family:宋体"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将显示所有配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1280522695}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110043372}[显示所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipv6 prefix-list]{lang="EN-US"}]{#struct_0_x1483_x6986_x2058625791}

[Prefix-list6: 666]{lang="EN-US"}

[ Permitted 0]{lang="EN-US"}

[ Denied 0]{lang="EN-US"}

[         index: 10        permit 6::/64                  ge  66  le  88]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display ipv6 prefix-list]{lang="EN-US"}]{#struct_0_x1483_x6986_1321695316}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x682767785}[[字段]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1971268148}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x776488099}

[[Prefix-list6]{lang="EN-US"}]{#struct_0_x1483_x6986_x262513233}

[[IPv6]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110502124}[地址前缀列表的名字]{style="font-family:宋体"}

[[Permitted]{lang="EN-US"}]{#struct_0_x1483_x6986_1489228765}

[[符合匹配条件的路由个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_826856158}

[[Denied]{lang="EN-US"}]{#struct_0_x1483_x6986_x133307997}

[[不符合匹配条件的路由个数]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x2146335638}

[[index]{lang="EN-US"}]{#struct_0_x1483_x6986_x1071621351}

[[地址前缀列表的内部序列号]{style="font-family:宋体"}]{#struct_0_x1483_x6986_2036889423}

[[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110436588}

[[匹配模式，有两种取值：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x603235860}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[permit]{lang="EN-US"}]{#struct_0_x1483_x6986_x689424448}[：表示允许]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[deny]{lang="EN-US"}]{#struct_0_x1483_x6986_1036785497}[：表示拒绝]{lang="EN-US" style="font-family:宋体"}

[[6::/64]{lang="EN-US"}]{#struct_0_x1483_x6986_1267453356}

[[匹配的]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}]{#struct_0_x1483_x6986_1211805972}[地址和前缀长度]{style="font-family:宋体"}

[[ge]{lang="EN-US"}]{#struct_0_x1483_x6986_x1110371052}

[[即]{style="font-family:宋体"}[greater-equal]{lang="EN-US"}]{#struct_0_x1483_x6986_1480453071}[，匹配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀长度的下限值]{style="font-family:宋体"}

[[le]{lang="EN-US"}]{#struct_0_x1483_x6986_x998899120}

[[即]{style="font-family:宋体"}[less-equal]{lang="EN-US"}]{#struct_0_x1483_x6986_x22278856}[，匹配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀长度的上限值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1207019089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_x313180843}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1110305516}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**

::: {#792039331 .myid}
[]{#_Toc404789279}[]{#struct_0_x1483_x6986_1276439203}[]{#_Toc261870637}[]{#_Toc138041305}[]{#_Toc134936993}[]{#_Toc113267983}[]{#_Toc110768979}[]{#_Toc90810134}[]{#_Toc90809395}[]{#_Toc86724138}[]{#_Toc85873653}[]{#_Toc77992914}

**路由策略 \-- IPv6路由策略配置命令 \-- if-match ipv6**

------------------------------------------------------------------------

[**[if-match]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}]{#struct_0_x1483_x6986_x2128143600}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[的路由信息]{style="font-family:宋体"}[的匹配条件。]{style="font-family:宋体"}

[**[undo if-match ipv6]{lang="EN-US"}**]{#struct_0_x1483_x6986_x954415204}[命令用来恢复取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x124474494}

[**[if-match ipv6]{lang="EN-US"}**[ { **address** \| **next-hop** \| **route-source** } { **acl** *acl6-number* \| **prefix-list** *prefix-list-name* }]{lang="EN-US"}]{#struct_0_x1483_x6986_x2073874701}

[**[undo if-match ipv6]{lang="EN-US"}**[ { **address** \| **next-hop** \| **route-source** } \[ **acl** \| **prefix-list** \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x821437206}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1892709187}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1483_x6986_844349127}[的路由信息的匹配条件。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1109715692}

[[路由策略视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x49631352}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1253718027}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1844275387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x664229046}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1091498080}

[**[address]{lang="EN-US"}**]{#struct_0_x1483_x6986_x573787303}[：匹配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息的目的地址。]{style="font-family:宋体"}

[**[next-hop]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1517074008}[：匹配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息的下一跳。]{style="font-family:宋体"}

[**[route-source]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1216259976}[：匹配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息的源地址。]{style="font-family:宋体"}

[**[acl ]{lang="EN-US"}***[acl6-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1109650156}[：指定用于过滤的]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[号]{style="font-family:宋体"}[。对于]{style="font-family:宋体"}**[address]{lang="EN-US"}**[，]{style="font-family:宋体"}*[acl6-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[；对于]{style="font-family:宋体"}**[next-hop]{lang="EN-US"}**[和]{style="font-family:宋体"}**[route-source]{lang="EN-US"}**[，]{style="font-family:宋体"}*[acl6-number]{lang="EN-US"}*[的]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[2999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}**[ *prefix-list-name*]{lang="EN-US"}]{#struct_0_x1483_x6986_1315873255}[：指定用于过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1785616817}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x1254005095}[创建一个名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的路由策略，其节点序列号为]{style="font-family:宋体"}[10]{lang="EN-US"}[，匹配模式为]{style="font-family:宋体"}[permit]{lang="EN-US"}[。定义一条]{style="font-family:宋体"}[if-match]{lang="EN-US"}[子句，允许下一跳地址匹配已存在的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表]{style="font-family:宋体"}[p1]{lang="EN-US"}[的路由信息通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x1720424213}

[\[Sysname\] route-policy policy1 permit node 10]{lang="EN-US"}

[\[Sysname-route-policy-policy1-10\] if-match ipv6 next-hop prefix-list p1]{lang="EN-US"}
:::

::: {#-1606344260 .myid}
[]{#_Toc404789280}[]{#struct_0_x1483_x6986_x422744631}[]{#_Toc261870638}[]{#_Toc138041306}[]{#_Toc134936999}[]{#_Toc113267990}[]{#_Toc110768986}[]{#_Toc90810140}[]{#_Toc90809401}[]{#_Toc86724144}[]{#_Toc85873659}[]{#_Toc77992917}[]{#_Toc65741007}[]{#_Toc61239919}[]{#_Toc53707335}

**路由策略 \-- IPv6路由策略配置命令 \-- ipv6 prefix-list**

------------------------------------------------------------------------

[**[ipv6 prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_750137106}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表表项。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}[ ipv6 prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1815118173}[命令用来删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表或其中某个表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1251730650}

[**[ipv6 prefix-list ]{lang="EN-US"}***[prefix-list-name ]{lang="EN-US"}*[\[ **index** *index-number* \] { **deny** \| **permit** } *ipv6-address prefix-length* \[ **greater-equal** *min-prefix-length* \] \[ **less-equal** *max-prefix-length* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_455091381}

[**[undo ipv6 prefix-list]{lang="EN-US"}**[ ]{lang="EN-US"}*[prefix-list-name]{lang="EN-US"}*[ \[ **index** *index-number* \]]{lang="EN-US"}]{#struct_0_x1483_x6986_x1432768268}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_777924689}

[[没有配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x1483_x6986_x2125015319}[地址前缀列表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1033893392}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1516669109}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1045116191}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1324578802}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1251665114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_2027347399}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_x403525080}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[index-number]{lang="EN-US"}*]{#struct_0_x1483_x6986_976042066}[：标识]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表中的一条表项，]{style="font-family:宋体"}*[index-number]{lang="EN-US"}*[小的表项先被匹配，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_x1483_x6986_1110077677}[：指定所定义的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表表项的匹配模式为拒绝模式。当指定为拒绝模式并且待过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址在该表项指定的前缀范围内时，则该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不能通过该表项的过滤，并且不会进行下一个表项的匹配，否则进入下一表项的匹配。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_x1483_x6986_2119465413}[：指定所定义的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表表项的匹配模式为允许模式。当指定为允许模式并且待过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址在该表项指定的前缀范围内时，通过该表项的过滤不进入下一个节点的匹配；如待过滤的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不在该表项指定的前缀范围内，则进行下一表项匹配。]{style="font-family:宋体"}

[*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_1562072826}[：指定]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[地址前缀和前缀长度，当指定为]{style="font-family:宋体"}[:: 0]{lang="EN-US"}[时匹配缺省路由，]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[greater-equal ]{lang="EN-US"}***[min-prefix-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_x1979695869}[：大于等于最小前缀长度。]{style="font-family:宋体"}

[**[less-equal]{lang="EN-US"}**[ *max-prefix-length*]{lang="EN-US"}]{#struct_0_x1483_x6986_x482130498}[：小于等于最大前缀长度。]{style="font-family:宋体"}

[[前缀长度范围可以表达为]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[ \<= *min-prefix-length* \<= *max-prefix-length* \<= 128]{lang="EN-US"}]{#struct_0_x1483_x6986_1251861722}[。如果只指定了]{style="font-family:宋体"}*[min-prefix-length]{lang="EN-US"}*[，则前缀范围为]{style="font-family:宋体"}[\[ *min-prefix-length*]{lang="EN-US"}[，]{style="font-family:宋体"}[128 \]]{lang="EN-US"}[；如果只指定了]{style="font-family:宋体"}*[max-prefix-length]{lang="EN-US"}*[，则前缀范围为]{style="font-family:宋体"}[\[ *prefix-length*]{lang="EN-US"}[，]{style="font-family:宋体"}*[max-prefix-length ]{lang="EN-US"}*[\]]{lang="EN-US"}[；如果二者都指定，则前缀范围为]{style="font-family:宋体"}[\[ *min-prefix-length*]{lang="EN-US"}[，]{style="font-family:宋体"}*[max-prefix-length]{lang="EN-US"}*[ \]]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x324227216}

[[IPv6]{lang="EN-US"}]{#struct_0_x1483_x6986_534285338}[地址前缀列表用于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址过滤。一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表可包含多个表项，一个表项指定一个地址前缀范围。表项之间的过滤关系是"或"，即通过一个表项就可通过该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的过滤。没有通过任何一个表项的过滤就意味着没有通过该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的过滤。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1483_x6986_x1199391545}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将]{lang="EN-US" style="font-family:宋体"}*[ipv6-address prefix-length]{lang="EN-US"}*]{#struct_0_x1483_x6986_39108390}[指定为]{lang="EN-US" style="font-family:宋体"}[:: 0]{lang="EN-US"}[，则只匹配缺省路由。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果需要匹配所有路由，则应配置为]{lang="EN-US" style="font-family:宋体"}[:: 0 **less-equal** 128]{lang="EN-US"}]{#struct_0_x1483_x6986_x2007685797}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x642154308}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_x869056930}[配置一条]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表，允许前缀长度在]{style="font-family:宋体"}[32]{lang="EN-US"}[位到]{style="font-family:宋体"}[64]{lang="EN-US"}[位之间的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x329720829}

[\[Sysname\] ipv6 prefix-list abc permit :: 0 greater-equal 32 less-equal 64]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1251796186}[配置一条]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表，拒绝地址前缀为]{style="font-family:宋体"}[3FFE:D00::/32]{lang="EN-US"}[，前缀长度大于等于]{style="font-family:宋体"}[32]{lang="EN-US"}[位的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1483_x6986_x716150522}

[\[Sysname\] ipv6 prefix-list abc deny 3FFE:D00:: 32 less-equal 128]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x280833509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_712954067}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_753736126}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**
:::

::: {#-1406402473 .myid}
[]{#_Toc404789281}[]{#struct_0_x1483_x6986_x1533114722}[]{#_Toc261870639}[]{#_Toc138041307}[]{#_Toc134937000}[]{#_Toc113267992}[]{#_Toc110768988}[]{#_Toc90810142}[]{#_Toc90809403}[]{#_Toc86724146}[]{#_Toc85873661}

**路由策略 \-- IPv6路由策略配置命令 \-- reset ipv6 prefix-list**

------------------------------------------------------------------------

[**[reset ipv6 prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x2087203781}[命令用来清除指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_392112666}

[**[reset ipv6 prefix-list]{lang="EN-US"}**]{#struct_0_x1483_x6986_x1295760881}**[ ]{lang="EN-US"}**[\[]{lang="EN-US"}[ *prefix-list-name* ]{lang="EN-US"}[\]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1251992794}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1483_x6986_1227242173}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x567599783}

[[network-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_x1434849041}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1483_x6986_1833379704}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_1984644475}

[*[prefix-list-name]{lang="EN-US"}*]{#struct_0_x1483_x6986_1618561429}[：指定地址前缀列表的名称。该名称必须唯一，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，将清除所有的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x1749446680}

[[\# ]{lang="EN-US"}]{#struct_0_x1483_x6986_1447538107}[清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipv6 prefix-list abc]{lang="EN-US"}]{#struct_0_x1483_x6986_1251927258}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1483_x6986_x701041742}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_x400071404}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip]{lang="EN-US"}**]{#struct_0_x1483_x6986_1135830297}**[v6]{lang="EN-US"}[ prefix-list]{lang="EN-US"}**

**[ ]{lang="EN-US"}**
:::
