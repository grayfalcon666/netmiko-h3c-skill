::: {#-1195010413 .myid}
[]{#_Toc404789066}[]{#struct_0_15908_44860_983472504}[]{#_Toc357603575}[]{#_Toc352311320}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- address-family ipv6**

------------------------------------------------------------------------

[**[address-family ipv6]{lang="EN-US"}**]{#struct_0_15908_44860_746515391}[命令用来创建并进入]{style="font-family:宋体"}[IS-IS IPv6]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[**[undo address-family ipv6]{lang="EN-US"}**]{#struct_0_15908_44860_983669112}[命令用来删除]{style="font-family:
宋体"}[IS-IS IPv6]{lang="EN-US"}[地址族视图。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1407368676}

[**[address-family ipv6 ]{lang="EN-US"}**[\[ **unicast** \]]{lang="EN-US"}]{#struct_0_15908_44860_x29636380}

[**[undo address-family ipv6 ]{lang="EN-US"}**[\[ **unicast** \]]{lang="EN-US"}]{#struct_0_15908_44860_x1455175693}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1223646223}

[[没有创建]{style="font-family:宋体"}[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_370552621}[地址族视图。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1673790721}

[[IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1438370653}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1665210667}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_643585039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_983603576}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_207154082}

[**[unicast]{lang="EN-US"}**]{#struct_0_15908_44860_x845600601}[：表示单播地址族。缺省为单播地址族。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x251017254}

[[配置本命令后，进程的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_x706625181}[被使能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_1851855248}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1094376710}[在]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[视图下，创建并进入]{style="font-family:宋体"}[IS-IS IPv6]{lang="EN-US"}[地址族视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x872857081}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-100-ipv6\]]{lang="EN-US"}
:::

::: {#-275634315 .myid}
[]{#_Toc404789067}[]{#struct_0_15908_44860_1432046098}[]{#_Toc357603576}[]{#_Toc352311324}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- auto-cost enable**

------------------------------------------------------------------------

[**[auto-cost enable]{lang="EN-US"}**]{#struct_0_15908_44860_x696177700}[命令用来使能自动计算接口链路开销值功能。]{style="font-family:宋体"}

[**[undo auto-cost enable]{lang="EN-US"}**]{#struct_0_15908_44860_983275896}[命令用来关闭自动计算接口链路开销值功能。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_15908_44860_x1893345376}

[**[auto-cost enable]{lang="EN-US"}**]{#struct_0_15908_44860_x740203253}

[**[undo auto-cost enable]{lang="EN-US"}**]{#struct_0_15908_44860_x564159475}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1787687040}

[[自动计算接口链路开销值功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_15908_44860_x1722821380}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1628496545}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_983210360}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x705845345}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1069008664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1833976097}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_855780039}

[[使能自动计算接口链路开销值功能后，将根据带宽参考值自动计算接口的链路度量值。当开销值的类型为]{style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_15908_44860_x1438171240}[或]{style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时，可以根据公式"开销]{style="font-family:宋体"}[=]{lang="EN-US"}[（参考值÷带宽）×]{style="font-family:宋体"}[10]{lang="EN-US"}["]{style="font-family:宋体"}[计算接口的链路度量值。当开销值类型为其他类型时，具体情况如下：接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[10Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[60]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[50]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[155Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[40]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[622Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[30]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[≤]{style="font-family:宋体"}[2500Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[20]{lang="EN-US"}[；接口带宽]{style="font-family:宋体"}[\>2500Mbps]{lang="EN-US"}[时，值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x2096841890}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1656832311}[使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[自动计算接口链路开销值功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_176032165}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] auto-cost enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x456013684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_15908_44860_983406968}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_15908_44860_x492936472}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis ]{lang="EN-US"}**]{#struct_0_15908_44860_x608301125}**[ipv6 ]{lang="EN-US"}[cost]{lang="EN-US"}**
:::

::: {#1475841160 .myid}
[]{#_Toc404789068}[]{#struct_0_15908_44860_1199990201}[]{#_Toc357603577}[]{#_Toc352311325}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- bandwidth-reference**

------------------------------------------------------------------------

[**[bandwidth-reference]{lang="EN-US"}**]{#struct_0_15908_44860_1352030086}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[自动计算链路开销值时依据的带宽参考值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **bandwidth-reference**]{lang="EN-US"}]{#struct_0_15908_44860_98313481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_15908_44860_x1109742815}

[**[bandwidth-reference]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_15908_44860_151981710}

[**[undo bandwidth-reference]{lang="EN-US"}**]{#struct_0_15908_44860_x1461356361}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_983341432}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_1277124565}[自动计算链路度量值时依据的带宽参考值为]{style="font-family:宋体"}[100Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_582944598}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1441580423}[单播地址族视图]{style="font-family:宋体"}*[ ]{style="color:blue"}*

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1400028367}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_1891662569}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_314601263}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x537636325}

[*[value]{lang="EN-US"}*]{#struct_0_15908_44860_1977088412}[：带宽参考值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2147483648]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_680824878}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_984062328}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[带宽参考值为]{style="font-family:宋体"}[200Mbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_567930009}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] bandwidth-reference 200]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1665606700}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[auto-cost enable]{lang="EN-US"}**]{#struct_0_15908_44860_1795690283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_15908_44860_92428402}
:::

::: {#188490618 .myid}
[]{#_Toc404789069}[]{#struct_0_15908_44860_x867027703}[]{#_Toc357603578}[]{#_Toc352311326}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- circuit-cost**

------------------------------------------------------------------------

[**[circuit-cost]{lang="EN-US"}**]{#struct_0_15908_44860_x877244259}[命令用来全局配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[的链路开销值。]{style="font-family:宋体"}

[**[undo circuit-cost]{lang="EN-US"}**]{#struct_0_15908_44860_x364522428}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_15908_44860_983996792}

[**[circuit-cost]{lang="EN-US"}**[ *value* \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_15908_44860_x1553738183}

[**[undo circuit-cost]{lang="EN-US"}**[ \[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_15908_44860_1207477621}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x657424071}

[[没有全局配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x968351709}[的链路开销值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x84896386}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_x422601454}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1118467640}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x767264456}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1098183434}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_983538041}

[*[value]{lang="EN-US"}*]{#struct_0_15908_44860_x1218628793}[：链路开销值，当指定的路径开销值类型不同时，取值范围也不同：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定的路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[narrow]{lang="EN-US"}**]{#struct_0_15908_44860_x1787415973}[、]{lang="EN-US" style="font-family:宋体"}**[narrow-compatibl]{lang="EN-US"}**[e]{lang="EN-US"}[或]{lang="EN-US" style="font-family:宋体"}**[compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当指定的路径开销值类型为]{lang="EN-US" style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_15908_44860_308974704}[或]{lang="EN-US" style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x515846936}[：配置在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x1113605031}[：配置在计算]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1098245272}

[[如果不指定级别，将同时配置计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_x4413381}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_1575278440}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1150914676}[全局配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[下]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[所有接口在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时的链路开销值为]{style="font-family:宋体"}[11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_983472505}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] circuit-cost 11 level-1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_746515392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_15908_44860_x326985734}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[isis cost]{lang="EN-US"}**]{#struct_0_15908_44860_x800021525}
:::

::: {#225668895 .myid}
[]{#_Toc404789070}[]{#struct_0_15908_44860_x46242533}[]{#_Toc357603579}[]{#_Toc352311327}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- default-route-advertise**

------------------------------------------------------------------------

[**[default-route-advertise]{lang="EN-US"}**]{#struct_0_15908_44860_2062903372}[命令用来配置路由器生成]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[缺省路由。]{style="font-family:宋体"}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_15908_44860_1192928204}[命令用来取消此项功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_15908_44860_x894061906}

[**[default-route-advertise]{lang="EN-US"}**[ \[ **avoid-learning** \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **route-policy** *route-policy-name* \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_15908_44860_x1881821018}

[**[undo default-route-advertise]{lang="EN-US"}**]{#struct_0_15908_44860_983669113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1407368675}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x29832988}[不发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[或]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1278145447}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_963087837}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1922443127}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x191688816}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1984201102}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x692523953}

[**[avoid-learning]{lang="EN-US"}**]{#struct_0_15908_44860_667753563}[：禁止学习通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发过来的缺省路由和]{style="font-family:宋体"}[ATT]{lang="EN-US"}[位产生的缺省路由，防止出现环路。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_983603577}[：发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_15908_44860_207154081}[：同时发布]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x845600600}[：发布]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_1851920784}[：指定路由策略名。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_15908_44860_x476285812}[：配置缺省路由]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1251728398}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定级别，则默认发布]{style="font-family:宋体"}]{#struct_0_15908_44860_x1655468930}[Level-2]{lang="EN-US"}[级别的缺省路由。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_958802236}[缺省路由只发布给本区域的其他路由器，]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[缺省路由发布给所有]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[路由器。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过使用路由策略，可以强制]{lang="EN-US" style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x585323575}[只在路由表中有匹配的路由项时才生成缺省路由。如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-1]{lang="EN-US"}**[，则可以在]{lang="EN-US" style="font-family:
宋体"}[L1 LSP]{lang="EN-US"}[中生成缺省路由；如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-2]{lang="EN-US"}**[，则可以在]{lang="EN-US" style="font-family:宋体"}[L2 LSP]{lang="EN-US"}[中生成缺省路由；如果在路由策略视图中]{lang="EN-US" style="font-family:宋体"}**[apply isis level-1-2]{lang="EN-US"}**[，可以在]{lang="EN-US" style="font-family:
宋体"}[L1 LSP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:
宋体"}[L2 LSP]{lang="EN-US"}[中各自生成缺省路由。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在路由策略中指定了]{lang="EN-US" style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_15908_44860_x1526964307}[值，则本命令中的]{lang="EN-US" style="font-family:宋体"}[Tag]{lang="EN-US"}[值不生效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1465135098}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_983275897}[配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[发布]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级别缺省路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1893345375}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] default-route-advertise]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x336918726}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[apply isis]{lang="EN-US"}**]{#struct_0_15908_44860_467175374}
:::

::: {#-765249180 .myid}
[]{#_Toc245204060}[]{#_Toc86723936}[]{#_Toc85873450}[]{#_Toc77992843}[]{#_Toc65740915}[]{#_Toc61239727}[]{#_Toc404789071}[]{#struct_0_15908_44860_x970029962}[]{#_Toc303846170}[]{#_Toc156184347}[]{#_Toc156184348}[]{#_Hlt7610887}[]{#_Hlt24184665}[]{#_Hlt536417594}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis redistribute ipv6**

------------------------------------------------------------------------

[**[display isis redistribute ipv6]{lang="EN-US"}**]{#struct_0_15908_44860_x2074154970}[命令用来显示]{style="font-family:
宋体"}[IPv6 IS-IS]{lang="EN-US"}[引入路由信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1640587740}

[**[display isis redistribute ipv6 ]{lang="EN-US"}**[\[ *ipv6-address mask-length* \] \[ **level-1** \| **level-2** \] \[ *process-id* \]]{lang="EN-US"}]{#struct_0_15908_44860_x1129776089}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_540542603}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15908_44860_1643969697}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x300852878}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_706611373}

[[network-operator]{lang="EN-US"}]{#struct_0_15908_44860_x1802659845}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1004154529}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15908_44860_370064640}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x797113121}

[*[ipv6-address mask-length]{lang="EN-US"}*]{#struct_0_15908_44860_x1974679598}[：显示指定目的]{style="font-family:
宋体"}[IP]{lang="EN-US"}[地址和掩码长度的引入路由。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_934841639}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x1598577329}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x300918414}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1313040736}

[[如果不指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_x1522488216}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x430856412}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1730020896}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[引入路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis redistribute ipv6 1]{lang="EN-US"}]{#struct_0_15908_44860_1620937138}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                        Level-1 IPv6 Redistribute Table]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Type       : direct     Destination: 12:1::/64]{lang="EN-US"}

[IntCost    : 0          Tag        :]{lang="EN-US"}

[State      : Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[                        Level-2 IPv6 Redistribute Table]{lang="EN-US"}

[                        \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Type       : direct     Destination: 12:1::/64]{lang="EN-US"}

[IntCost    : 0          Tag        :]{lang="EN-US"}

[State      : Active]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display isis redistribute ipv6]{lang="EN-US"}]{#struct_0_15908_44860_x1644446178}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_442944632}[[字段]{style="font-family:黑体"}]{#struct_0_15908_44860_1029588424}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15908_44860_932173843}

[[Route information for IS-IS(1)]{lang="EN-US"}]{#struct_0_15908_44860_x814352798}

[[指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x949032689}[进程引入路由信息]{style="font-family:宋体"}

[[Level-1 IPv6 Redistribute Table]{lang="EN-US"}]{#struct_0_15908_44860_x177330388}

[[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_1620871602}[的]{style="font-family:宋体"}[IS-IS IPv6]{lang="EN-US"}[引入路由信息]{style="font-family:宋体"}

[[Level-2 IPv6 Redistribute Table]{lang="EN-US"}]{#struct_0_15908_44860_336963442}

[[Level-2]{lang="EN-US"}]{#struct_0_15908_44860_1991777786}[的]{style="font-family:宋体"}[IS-IS IPv6]{lang="EN-US"}[引入路由信息]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_15908_44860_94751967}

[[引入的路由类型，包括直连、]{style="font-family:宋体"}[ISISv6]{lang="EN-US"}]{#struct_0_15908_44860_x1178672683}[、静态、]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[、]{style="font-family:宋体"}[BGP4+]{lang="EN-US"}[、]{style="font-family:宋体"}[RIPng]{lang="EN-US"}

[[Destination]{lang="EN-US"}]{#struct_0_15908_44860_1545185495}

[[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1620806066}[目的地址]{style="font-family:宋体"}

[[IntCost]{lang="EN-US"}]{#struct_0_15908_44860_1876052391}

[[内部路由]{style="font-family:宋体"}]{#struct_0_15908_44860_796925492}[Cost]{lang="EN-US"}

[[Tag]{lang="EN-US"}]{#struct_0_15908_44860_x1707668366}

[[引入路由发布时的]{style="font-family:宋体"}]{#struct_0_15908_44860_x1117477202}[Tag]{lang="EN-US"}[值]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_15908_44860_1741417688}

[[引入路由是否为最终生效路由]{style="font-family:宋体"}]{#struct_0_15908_44860_1620740530}

[ ]{lang="EN-US"}

::: {#-928487688 .myid}
[]{#_Toc404789072}[]{#struct_0_15908_44860_326644603}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis route ipv6**

------------------------------------------------------------------------

[**[display isis route ipv6]{lang="EN-US"}**]{#struct_0_15908_44860_x1550186643}[命令用来显示]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_15783030}

[**[display isis route ipv6]{lang="EN-US"}**[ \[ *ipv6-address* \] \[ \[ **level-1** \| **level-2** \] \| **verbose** \] \* \[ ]{lang="EN-US"}*[process-id ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_15908_44860_x670590488}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1299119513}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x641320393}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1588465923}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1034306058}

[[network-operator]{lang="EN-US"}]{#struct_0_15908_44860_1620674994}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1533370682}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15908_44860_1421546805}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_1282427399}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_15908_44860_160289990}[：显示指定目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的路由。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x1124713388}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x1412666676}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_15908_44860_541553835}[：显示]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由的详细信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_187210083}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_1620609458}

[[如果不指定级别，默认为显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_1064979725}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由信息，即]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x73391514}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_2081463276}[显示]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[的路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis route ipv6]{lang="EN-US"}]{#struct_0_15908_44860_1620543922}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-1 IPv6 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 2001:1::                                PrefixLen: 64]{lang="EN-US"}

[ Flag       : R/L/-                                   Cost     : 20]{lang="EN-US"}

[ Next Hop   : FE80::200:5EFF:FE64:8905                Interface: GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 2001:2::                                PrefixLen: 64]{lang="EN-US"}

[ Flag       : D/L/-                                   Cost     : 10]{lang="EN-US"}

[ Next Hop   : Direct                                  Interface: GE1/0/1]{lang="EN-US"}

[ ]{lang="EN-US"}

[       Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-2 IPv6 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 2001:1::                                PrefixLen: 64]{lang="EN-US"}

[ Flag       : -/-/-                                   Cost     : 20]{lang="EN-US"}

[ ]{lang="EN-US"}

[ ]{lang="EN-US"}

[ Destination: 2001:2::                                PrefixLen: 64]{lang="EN-US"}

[ Flag       : D/L/-                                   Cost     : 10]{lang="EN-US"}

[ ]{lang="EN-US"}

[       Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display isis route ipv6]{lang="EN-US"}]{#struct_0_15908_44860_x841182961}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_440096852}[[字段]{style="font-family:黑体"}]{#struct_0_15908_44860_x549247089}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15908_44860_x171259492}

[[Destination]{lang="EN-US"}]{#struct_0_15908_44860_916056161}

[[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1620478386}[目的地址前缀]{style="font-family:宋体"}

[[PrefixLen]{lang="EN-US"}]{#struct_0_15908_44860_1067374651}

[[前缀长度]{style="font-family:宋体"}]{#struct_0_15908_44860_1358571096}

[[Flag/Flags]{lang="EN-US"}]{#struct_0_15908_44860_x1487753252}

[[路由信息状态标志位]{style="font-family:宋体"}]{#struct_0_15908_44860_x598875715}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_15908_44860_719094906}[：直连路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_15908_44860_6039195}[：该路由是否已放到路由表中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_15908_44860_1621461426}[：是否已经通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_15908_44860_1505339384}[：路由渗透状态标识，标识]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由是否来自]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[。]{style="font-family:宋体"}[如果配置为"]{lang="EN-US" style="font-family:宋体"}[U]{lang="EN-US"}["则可避免由]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[发送到]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[又返回给]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[Cost]{lang="EN-US"}]{#struct_0_15908_44860_1405369719}

[[开销值]{style="font-family:宋体"}]{#struct_0_15908_44860_x1909113471}

[[Next Hop]{lang="EN-US"}]{#struct_0_15908_44860_1350075105}

[[下一跳]{style="font-family:宋体"}]{#struct_0_15908_44860_1621395890}

[[Interface]{lang="EN-US"}]{#struct_0_15908_44860_x1615276504}

[[出接口]{style="font-family:宋体"}]{#struct_0_15908_44860_575563844}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1986705838}[显示]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[的详细路由信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis route ipv6 verbose]{lang="EN-US"}]{#struct_0_15908_44860_1620937139}

[ ]{lang="EN-US"}

[                         Route information for IS-IS(1)]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-1 IPv6 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV6 Dest  : 2001:1::/64                    Cost : 20            Flag : R/L/-]{lang="EN-US"}

[ Admin Tag  : -                         Src Count : 1]{lang="EN-US"}

[ NextHop    :                           Interface :          ExitIndex :]{lang="EN-US"}

[    FE80::200:5EFF:FE64:8905                GE1/0/1             0x00000003]{lang="EN-US"}

[ Nib ID    : 0x24000002]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV6 Dest  : 2001:2::/64                    Cost : 10            Flag : D/L/-]{lang="EN-US"}

[ Admin Tag  : -                         Src Count : 2]{lang="EN-US"}

[ NextHop    :                           Interface :          ExitIndex :]{lang="EN-US"}

[    Direct                                  GE1/0/1             0x00000000]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[ ]{lang="EN-US"}

[                         Level-2 IPv6 Forwarding Table]{lang="EN-US"}

[                         \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV6 Dest  : 2001:1::/64                    Cost : 20            Flag : -/-/-]{lang="EN-US"}

[ Admin Tag  : -                         Src Count : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[ IPV6 Dest  : 2001:2::/64                    Cost : 10            Flag : D/L/-]{lang="EN-US"}

[ Admin Tag  : -                         Src Count : 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[      Flags: D-Direct, R-Added to Rib, L-Advertised in LSPs, U-Up/Down Bit Set]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display isis route ipv6 verbose]{lang="EN-US"}]{#struct_0_15908_44860_x1644380642}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_467600594}[[字段]{style="font-family:黑体"}]{#struct_0_15908_44860_x2103008851}

[[描述]{style="font-family:黑体"}]{#struct_0_15908_44860_1620871603}

[[IPV6 Dest]{lang="EN-US"}]{#struct_0_15908_44860_337028978}

[[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1940067032}[目的地址和前缀信息]{style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_15908_44860_x1588134704}

[[开销值]{style="font-family:宋体"}]{#struct_0_15908_44860_x1274281602}

[[Flag/Flags]{lang="EN-US"}]{#struct_0_15908_44860_x1679489768}

[[路由信息状态标志位]{style="font-family:宋体"}]{#struct_0_15908_44860_1549640880}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_15908_44860_1620806067}[：直连路由]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_15908_44860_1875986855}[：该路由是否已放到路由表中]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_15908_44860_x591859833}[：是否已经通过]{style="font-family:宋体"}[LSP]{lang="EN-US"}[发布]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_15908_44860_x1010627272}[：路由渗透状态标识，标识]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由是否来自]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[。]{style="font-family:宋体"}[如果配置为"]{lang="EN-US" style="font-family:宋体"}[U]{lang="EN-US"}["则可避免由]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}[发送到]{lang="EN-US" style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[又返回给]{lang="EN-US" style="font-family:宋体"}[Level-2]{lang="EN-US"}

[[Admin Tag]{lang="EN-US"}]{#struct_0_15908_44860_x761224059}

[[管理标记]{style="font-family:宋体"}]{#struct_0_15908_44860_1075442442}

[[Src Count]{lang="EN-US"}]{#struct_0_15908_44860_1620740531}

[[发布源个数]{style="font-family:宋体"}]{#struct_0_15908_44860_326579067}

[[Next Hop]{lang="EN-US"}]{#struct_0_15908_44860_913132400}

[[下一跳]{style="font-family:宋体"}]{#struct_0_15908_44860_x1273995046}

[[Interface]{lang="EN-US"}]{#struct_0_15908_44860_x1837057960}

[[出接口]{style="font-family:宋体"}]{#struct_0_15908_44860_1620674995}

[[ExitIndex]{lang="EN-US"}]{#struct_0_15908_44860_1533436218}

[[出接口索引]{style="font-family:宋体"}]{#struct_0_15908_44860_x513922207}

[[Nib ID]{lang="EN-US"}]{#struct_0_15908_44860_x654367317}

[[路由管理分配的]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_15908_44860_348242441}[，即下一跳索引]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#154106903 .myid}
[]{#_Toc245204061}[]{#_Toc86723945}[]{#_Toc85873459}[]{#_Toc77992844}[]{#_Toc65740917}[]{#_Toc61239720}[]{#_Toc404789073}[]{#struct_0_15908_44860_x225318453}[]{#_Toc341967693}[]{#_Toc341782289}[]{#_Toc341285953}[]{#_Hlt9932878}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- display isis spf-tree ipv6**

------------------------------------------------------------------------

[**[display isis spf-tree ipv6]{lang="EN-US"}**]{#struct_0_15908_44860_1467852244}[命令用来显示]{style="font-family:
宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_696269822}

[**[display isis spf-tree ipv6]{lang="EN-US"}**[ \[ \[ **level-1** \| **level-2** \] \| **verbose** \] \* \[ *process-id* \]]{lang="EN-US"}]{#struct_0_15908_44860_x794587065}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1620609459}

[[任意视图]{style="font-family:宋体"}]{#struct_0_15908_44860_1064914189}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x490068711}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x428048280}

[[network-operator]{lang="EN-US"}]{#struct_0_15908_44860_270705988}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_709439715}

[[mdc-operator]{lang="EN-US"}]{#struct_0_15908_44860_307606374}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1676631780}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x729186748}[：显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[拓扑信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_1620543923}[：显示]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[拓扑信息。如果未指定级别，将同时显示]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的拓扑信息。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_15908_44860_x841248497}[：显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的详细拓扑信息。如果未指定该参数，显示摘要拓扑信息。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_x246106757}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，显示指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的拓扑信息。如果未指定]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，将显示所有]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程的拓扑信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x451914458}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1894523007}[显示]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis spf-tree ipv6]{lang="EN-US"}]{#struct_0_15908_44860_1620478387}

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

[                       Level-1 Shortest Path Tree]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[SpfNode            NodeFlag       SpfLink            LinkCost LinkFlag]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0000.0000.0032.00  S/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  10       -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0032.01  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0064.00  0        -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  0        -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[0000.0000.0064.00  S/-/-/R/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.00  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[                               \--\>0000.0000.0032.01  10       -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[ ]{lang="EN-US"}

[                       Level-2 Shortest Path Tree]{lang="EN-US"}

[                       \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

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

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1621461427}[显示]{style="font-family:宋体"}[IS-IS Level-1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[详细拓扑信息。]{style="font-family:宋体"}

[[\<Sysname\> display isis spf-tree ipv6 level-1 verbose]{lang="EN-US"}]{#struct_0_15908_44860_1620740528}

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

[                           Level-1 Shortest Path Tree]{lang="EN-US"}

[                           \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[ SpfNode        : 0000.0000.0032.00]{lang="EN-US"}

[ Distance       : 0]{lang="EN-US"}

[ TE distance    : 0]{lang="EN-US"}

[ NodeFlag       : S/-/-/-/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 2]{lang="EN-US"}

[ \--\>0000.0000.0032.01]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Adjacent   Interface: N/A]{lang="EN-US"}

[        Cost    : 10         Nexthop  : N/A]{lang="EN-US"}

[\--\>0000.0000.0064.00]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Adjacent   Interface: Tun1]{lang="EN-US"}

[        Cost    : 10         Nexthop  : FE80::A0A:A40]{lang="EN-US"}

[ ]{lang="EN-US"}

[SpfNode        : 0000.0000.0032.01]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ TE distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/R/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 0]{lang="EN-US"}

[ SpfLink count  : 2]{lang="EN-US"}

[ \--\>0000.0000.0064.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Adjacent   Interface: Vlan2]{lang="EN-US"}

[        Cost    : 10         Nexthop  : FE80::200:12FF:FE34:1]{lang="EN-US"}

[\--\>0000.0000.0032.00]{lang="EN-US"}

[    LinkCost    : 0]{lang="EN-US"}

[    LinkNewCost : 0]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Adjacent   Interface: N/A]{lang="EN-US"}

[        Cost    : 0           Nexthop  : N/A]{lang="EN-US"}

[ ]{lang="EN-US"}

[SpfNode        : 0000.0000.0064.00]{lang="EN-US"}

[ Distance       : 10]{lang="EN-US"}

[ TE distance    : 10]{lang="EN-US"}

[ NodeFlag       : S/-/-/R/-/-]{lang="EN-US"}

[ RelayNibID     : 0x0]{lang="EN-US"}

[ TE tunnel count: 0]{lang="EN-US"}

[ Nexthop count  : 2]{lang="EN-US"}

[     Neighbor  : 0000.0000.0064.00        Interface  : Vlan2]{lang="EN-US"}

[     NextHop   : FE80::200:12FF:FE34:1]{lang="EN-US"}

[     BkNeighbor: N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNextHop : N/A]{lang="EN-US"}

[     Neighbor  : 0000.0000.0064.00        Interface  : Tun1]{lang="EN-US"}

[     NextHop   : FE80::A0A:A40]{lang="EN-US"}

[     BkNeighbor: N/A                      BkInterface: N/A]{lang="EN-US"}

[     BkNextHop : N/A]{lang="EN-US"}

[ SpfLink count  : 2]{lang="EN-US"}

[ \--\>0000.0000.0032.00]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/-/P/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Remote     Interface: N/A]{lang="EN-US"}

[        Cost    : 10         Nexthop  : N/A]{lang="EN-US"}

[        AdvMtID : 0]{lang="EN-US"}

[\--\>0000.0000.0064.00]{lang="EN-US"}

[    LinkCost    : 10]{lang="EN-US"}

[    LinkNewCost : 10]{lang="EN-US"}

[    LinkFlag    : -/-/C/-/-/-/-/-/-]{lang="EN-US"}

[    LinkSrcCnt  : 1]{lang="EN-US"}

[        Type    : Remote     Interface: Tun1]{lang="EN-US"}

[        Cost    : 10         Nexthop  : FE80::A0A:A40]{lang="EN-US"}

[        AdvMtID : 0]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display isis spf-tree ipv6]{lang="EN-US"}]{#struct_0_15908_44860_326120316}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_468498376}[[字段]{style="font-family:黑体"}]{#struct_0_15908_44860_798730455}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_15908_44860_x1187762180}

[[SpfNode]{lang="EN-US"}]{#struct_0_15908_44860_x1322338488}

[[拓扑节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_15908_44860_1620674992}

[[Distance]{lang="EN-US"}]{#struct_0_15908_44860_1533763898}

[[根节点到该节点的最短距离]{style="font-family:宋体"}]{#struct_0_15908_44860_x2050258597}

[[TE distance]{lang="EN-US"}]{#struct_0_15908_44860_x1817232267}

[[根节点到该节点的最短距离（包含隧道]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_15908_44860_x251148326}[），如果未配置隧道，则与]{style="font-family:宋体"}[Distance]{lang="EN-US"}[值相等]{style="font-family:宋体"}

[[NodeFlag]{lang="EN-US"}]{#struct_0_15908_44860_368825735}

[[节点状态标记：]{style="font-family:宋体"}]{#struct_0_15908_44860_247712891}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[S]{lang="EN-US"}]{#struct_0_15908_44860_40403788}[：节点在]{lang="EN-US" style="font-family:
  宋体"}[SPF]{lang="EN-US"}[树上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[T]{lang="EN-US"}]{#struct_0_15908_44860_1620609456}[：节点在候选列表上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[O]{lang="EN-US"}]{#struct_0_15908_44860_1064324365}[：节点处于]{lang="EN-US" style="font-family:
  宋体"}[OverLoad]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[R]{lang="EN-US"}]{#struct_0_15908_44860_x874043815}[：节点是直连的]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_15908_44860_2135193141}[：孤立节点]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_15908_44860_1952480464}[：节点待删除]{lang="EN-US" style="font-family:
  宋体"}

[[TE tunnel count]{lang="EN-US"}]{#struct_0_15908_44860_x773744932}

[[Destination]{lang="EN-US"}]{#struct_0_15908_44860_x1225599734}[为该节点的隧道条数]{style="font-family:宋体"}

[[Nexthop count]{lang="EN-US"}]{#struct_0_15908_44860_205963}

[[节点的下一跳个数]{style="font-family:宋体"}]{#struct_0_15908_44860_1620543920}

[[NextHop]{lang="EN-US"}]{#struct_0_15908_44860_x841314033}

[[节点的主用下一跳地址]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15908_44860_2145271428}[链路发布源下一跳地址]{style="font-family:宋体"}

[[AdvMtID]{lang="EN-US"}]{#struct_0_15908_44860_x654432853}

[[从哪个拓扑学到的路由：]{style="font-family:宋体"}]{#struct_0_15908_44860_1906510167}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[0]{lang="EN-US"}]{#struct_0_15908_44860_x1410391231}[：标准拓扑]{lang="EN-US" style="font-family:
  宋体"}[ID]{lang="EN-US"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[6]{lang="EN-US"}]{#struct_0_15908_44860_1282869995}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[：其它拓扑]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Interface]{lang="EN-US"}]{#struct_0_15908_44860_x811881556}

[[节点的主用下一跳出接口]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_15908_44860_518151809}[链路发布源下一跳出接口]{style="font-family:宋体"}

[[BkNextHop]{lang="EN-US"}]{#struct_0_15908_44860_1620478384}

[[节点的备份下一跳地址]{style="font-family:宋体"}]{#struct_0_15908_44860_1067243579}

[[BkInterface]{lang="EN-US"}]{#struct_0_15908_44860_975090144}

[[节点的备份下一跳出接口]{style="font-family:宋体"}]{#struct_0_15908_44860_354144106}

[[Neighbor]{lang="EN-US"}]{#struct_0_15908_44860_1913041012}

[[节点主用下一跳邻居节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_15908_44860_1621461424}

[[BkNeighbor]{lang="EN-US"}]{#struct_0_15908_44860_1505470456}

[[节点备份下一跳邻居节点]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_15908_44860_1050288994}

[[SpfLink]{lang="EN-US"}]{#struct_0_15908_44860_1342360098}

[[拓扑链路]{style="font-family:宋体"}]{#struct_0_15908_44860_1621395888}

[[SpfLink count]{lang="EN-US"}]{#struct_0_15908_44860_x1615800791}

[[拓扑链路个数]{style="font-family:宋体"}]{#struct_0_15908_44860_x909552130}

[[LinkCost]{lang="EN-US"}]{#struct_0_15908_44860_x1580333044}

[[链路开销]{style="font-family:宋体"}]{#struct_0_15908_44860_x1671364583}

[[LinkNewCost]{lang="EN-US"}]{#struct_0_15908_44860_1620937137}

[[链路新开销]{style="font-family:宋体"}]{#struct_0_15908_44860_x1643463138}

[[LinkFlag]{lang="EN-US"}]{#struct_0_15908_44860_1841453359}

[[链路状态标记：]{style="font-family:宋体"}]{#struct_0_15908_44860_x222572878}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[I]{lang="EN-US"}]{#struct_0_15908_44860_1620871601}[：孤立链路]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[D]{lang="EN-US"}]{#struct_0_15908_44860_336897906}[：链路待删除]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[C]{lang="EN-US"}]{#struct_0_15908_44860_2028149228}[：目的节点是源节点的子节点]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[P]{lang="EN-US"}]{#struct_0_15908_44860_x1026670481}[：目的节点是源节点的父节点]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[V]{lang="EN-US"}]{#struct_0_15908_44860_1620806065}[：链路受到影响]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[N]{lang="EN-US"}]{#struct_0_15908_44860_1875855783}[：新增链路]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[L]{lang="EN-US"}]{#struct_0_15908_44860_129536472}[：链路在变化链表上]{lang="EN-US" style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[U]{lang="EN-US"}]{#struct_0_15908_44860_1620740529}[：链路协议类型发生变化]{style="font-family:宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[H]{lang="EN-US"}]{#struct_0_15908_44860_326054780}[：链表下一跳发生变化]{style="font-family:宋体"}

[[LinkSrcCnt]{lang="EN-US"}]{#struct_0_15908_44860_x1153991700}

[[链路发布源个数]{style="font-family:宋体"}]{#struct_0_15908_44860_701987340}

[[Type]{lang="EN-US"}]{#struct_0_15908_44860_1620674993}

[[链路发布源类型：]{style="font-family:宋体"}]{#struct_0_15908_44860_1533829434}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Adjacent]{lang="EN-US"}]{#struct_0_15908_44860_x570669998}[：本地邻居维护产生]{style="font-family:
  宋体"}

[[·[      ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Remote]{lang="EN-US"}]{#struct_0_15908_44860_1447881046}[：其它节点]{lang="EN-US" style="font-family:宋体"}[LSP]{lang="EN-US"}[产生]{lang="EN-US" style="font-family:宋体"}

[[Cost]{lang="EN-US"}]{#struct_0_15908_44860_1620609457}

[[链路发布源开销]{style="font-family:宋体"}]{#struct_0_15908_44860_1064258829}

[ ]{lang="EN-US"}

::: {#1247311243 .myid}
[]{#_Toc245204065}[]{#_Toc86723949}[]{#_Toc85873463}[]{#_Toc77992848}[]{#_Toc65740921}[]{#_Toc61239734}[]{#_Toc404789074}[]{#struct_0_15908_44860_x806175292}[]{#_Toc310607874}[]{#_Toc290886941}[]{#_Toc245204063}[]{#_Toc86723947}[]{#_Toc85873461}[]{#_Toc77992846}[]{#_Toc65740919}[]{#_Toc367622347}[]{#_Toc367622348}[]{#_Toc367622349}[]{#_Toc367622350}[]{#_Toc367622351}[]{#_Toc367622352}[]{#_Toc367622353}[]{#_Toc367622354}[]{#_Toc367622355}[]{#_Toc367622356}[]{#_Toc367622357}[]{#_Toc367622358}[]{#_Toc367622359}[]{#_Toc367622360}[]{#_Toc367622361}[]{#_Toc367622362}[]{#_Toc367622363}[]{#_Toc367622364}[]{#_Toc367622365}[]{#_Toc367622366}[]{#_Toc367622367}[]{#_Toc367622368}[]{#_Toc367622369}[]{#_Toc367622370}[]{#_Toc367622371}[]{#_Toc367622372}[]{#_Toc367622373}[]{#_Toc367622374}[]{#_Toc367622375}[]{#_Toc367622376}[]{#_Toc367622377}[]{#_Toc367622378}[]{#_Toc367622379}[]{#_Toc367622380}[]{#_Toc367622381}[]{#_Toc367622382}[]{#_Toc367622383}[]{#_Toc367622384}[]{#_Toc367622385}[]{#_Toc367622386}[]{#_Toc367622387}[]{#_Toc367622388}[]{#_Toc367622389}[]{#_Toc367622390}[]{#_Toc367622391}[]{#_Toc367622392}[]{#_Toc367622393}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- filter-policy export**

------------------------------------------------------------------------

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_15908_44860_1890531295}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[对引入的路由进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy export]{lang="EN-US"}**]{#struct_0_15908_44860_699327352}[命令用来取消对引入的路由进行过滤。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x818815725}

[**[filter-policy]{lang="EN-US"}**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_15908_44860_x845074188}

[**[undo filter-policy]{lang="EN-US"}**[ **export** \[ *protocol* \[ *process-id* \] \]]{lang="EN-US"}]{#struct_0_15908_44860_1620871598}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1237670021}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_662192332}[不对引入的路由进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1464562896}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_x1504166808}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_246692248}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_1045442352}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1376541207}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1975599159}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_15908_44860_1620806062}[：用来过滤引入路由的基本或高级]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}***[ prefix-list-name]{lang="EN-US"}*]{#struct_0_15908_44860_1876314535}[：用来过滤引入路由的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_x1944516711}[：用来过滤引入路由的路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[protocol]{lang="EN-US"}*]{#struct_0_15908_44860_1432978053}[：路由协议名称，指定过滤从哪种路由协议引入的路由信息。目前可包括：]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[、]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[和]{style="font-family:宋体"}**[static]{lang="EN-US"}**[。如果不指定该参数，将对所有引入的路由进行过滤。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_816953553}[：路由协议进程号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[时，支持该参数。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1761561576}

[[某些情况下，可能要求只发布某些满足条件的路由信息，此时，可以定义]{style="font-family:宋体"}**[filter-policy]{lang="EN-US"}**]{#struct_0_15908_44860_1135549085}[配置所发布路由信息的过滤条件，只有通过了过滤的路由信息才能被发布。]{style="font-family:宋体"}

[**[filter-policy export]{lang="EN-US"}**]{#struct_0_15908_44860_x795523907}[命令一般和]{style="font-family:宋体"}**[import-route]{lang="EN-US"}**[命令结合使用，它只对已引入的路由在发布给其他路由器时进行过滤。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{style="font-family:宋体"}]{#struct_0_15908_44860_525453364}*[protocol]{lang="EN-US"}*[参数，将对所有协议引入的路由进行过滤；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{style="font-family:宋体"}]{#struct_0_15908_44860_1620740526}*[protocol]{lang="EN-US"}*[参数，则只对特定协议引入的路由进行过滤。]{style="font-family:宋体"}

[[需要注意的是，当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_15908_44860_327037820}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和前缀的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x975075508}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x461217940}[配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[使用编号为]{style="font-family:宋体"}[2006]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1453347035}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] filter-policy 2006 export]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x953289478}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对引入的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1620674990}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] filter-policy 3000 export]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1533632826}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy import]{lang="EN-US"}**]{#struct_0_15908_44860_663748108}
:::

::: {#632247711 .myid}
[]{#_Toc404789075}[]{#struct_0_15908_44860_x1114013170}[]{#_Toc310607875}[]{#_Toc290886942}[]{#_Toc245204064}[]{#_Toc86723948}[]{#_Toc85873462}[]{#_Toc77992847}[]{#_Toc65740920}[]{#_Toc61239732}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- filter-policy import**

------------------------------------------------------------------------

[**[filter-policy import]{lang="EN-US"}**]{#struct_0_15908_44860_x1635138062}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[对接收的路由进行过滤。]{style="font-family:宋体"}

[**[undo filter-policy import]{lang="EN-US"}**]{#struct_0_15908_44860_116596753}[命令用来取消对接收的路由进行过滤。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_58229473}

[**[filter-policy]{lang="EN-US"}**[ { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } **import**]{lang="EN-US"}]{#struct_0_15908_44860_x955404547}

[**[undo filter-policy]{lang="EN-US"}**[ **import**]{lang="EN-US"}]{#struct_0_15908_44860_x2100289503}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1620609454}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_1064193293}[不对接收的路由信息进行过滤。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1661619849}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_1464685581}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1598121319}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_133661932}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1270039828}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x548922474}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_15908_44860_x2126829447}[：用来过滤接收的路由的基本或高级]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}***[ prefix-list-name]{lang="EN-US"}*]{#struct_0_15908_44860_1620543918}[：用来过滤接收的路由的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_x841838324}[：用来过滤接收的路由的路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1428441428}

[[某些情况下，可能要求只接收某些满足条件的路由信息，此时，可以定义]{style="font-family:宋体"}**[filter-policy]{lang="EN-US"}**]{#struct_0_15908_44860_x809549461}[配置接收路由信息的过滤条件，只有通过了过滤的路由信息才能被加入路由表。]{style="font-family:宋体"}

[[需要注意的是，当配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_15908_44860_154274488}[（]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[）或者指定的路由策略中配置的是高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[时，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的规则需要使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix*]{lang="EN-US"}[来过滤指定目的地址的路由；使用命令]{style="font-family:宋体"}**[rule]{lang="EN-US"}**[ \[ *rule-id* \] { **deny** \| **permit** } **ipv6 source** *sour sour-prefix* **destination** *dest dest-prefix*]{lang="EN-US"}[来过滤指定目的地址和前缀的路由，其中]{style="font-family:宋体"}**[source]{lang="EN-US"}**[用来过滤路由目的地址，]{style="font-family:宋体"}**[destination]{lang="EN-US"}**[用来过滤路由前缀，配置的前缀应该是连续的（当配置的前缀不连续时该过滤前缀的条件不生效）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x892047088}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1792173612}[使用编号为]{style="font-family:宋体"}[2003]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1633978587}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] filter-policy 2003 import]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1130630297}[使用编号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[对接收的路由进行过滤，只允许]{style="font-family:宋体"}[2001::1/128]{lang="EN-US"}[通过。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1620478382}

[\[Sysname\] acl ipv6 advanced 3000]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 10 permit ipv6 source 2001::1 128 destination ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff 128]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] rule 100 deny ipv6]{lang="EN-US"}

[\[Sysname-acl-ipv6-adv-3000\] quit]{lang="EN-US"}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] filter-policy 3000 import]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1067636795}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[filter-policy export]{lang="EN-US"}**]{#struct_0_15908_44860_191631155}
:::

::: {#29262825 .myid}
[]{#_Toc404789076}[]{#struct_0_15908_44860_x2072014678}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route**

------------------------------------------------------------------------

[**[import-route]{lang="EN-US"}**]{#struct_0_15908_44860_x1731336679}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[引入其他协议的路由信息。]{style="font-family:宋体"}

[**[undo import-route]{lang="EN-US"}**]{#struct_0_15908_44860_1517742095}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[不引入其它协议的路由信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_696785812}

[**[import-route ]{lang="EN-US"}***[protocol]{lang="EN-US"}*[ \[ *process-id* \] \[ **allow-ibgp** \] \[ **allow-direct** \| **cost** *cost* \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **route-policy** *route-policy-name* \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_15908_44860_1621461422}

[**[undo import-route ]{lang="EN-US"}***[protocol ]{lang="EN-US"}*[\[]{lang="EN-US"}*[ process-id ]{lang="EN-US"}*[\]]{lang="EN-US"}]{#struct_0_15908_44860_1505077240}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_264536510}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x2144282400}[不引入其它协议的路由信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x596449526}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_x647164749}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1454883238}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_1621395886}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1615669719}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x203037480}

[*[protocol]{lang="EN-US"}*]{#struct_0_15908_44860_727273031}[：要引入的路由协议，可以是]{style="font-family:宋体"}**[direct]{lang="EN-US"}**[、]{style="font-family:宋体"}**[static]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ripng]{lang="EN-US"}**[、]{style="font-family:宋体"}**[isisv6]{lang="EN-US"}**[、]{style="font-family:宋体"}**[bgp4+]{lang="EN-US"}**[及]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[。]{style="font-family:宋体"}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_x1534059843}[：引入路由的源路由协议号]{style="font-family:宋体"}[，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[是]{style="font-family:宋体"}**[ripng]{lang="EN-US"}[、]{style="font-family:宋体"}[isisv6]{lang="EN-US"}**[及]{style="font-family:宋体"}**[ospfv3]{lang="EN-US"}**[时，该参数可选。]{style="font-family:宋体"}

[**[allow-direct]{lang="EN-US"}**]{#struct_0_15908_44860_1790588950}[：]{style="font-family:宋体"}[在引入的路由中包含使能了该协议的接口网段路由。缺省情况下，在引入]{style="font-family:宋体"}[协议]{style="font-family:宋体"}[路由时不会包含使能了]{style="font-family:宋体"}[该]{style="font-family:宋体"}[协议的接口网段路由。当]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[与]{style="font-family:宋体"}**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}[参数一起使用时，需要注意路由策略中配置的匹配规则不要与接口路由信息存在冲突，否则会导致]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[配置失效。例如，当配置]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数引入]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[直连时，在路由策略中不要配置]{style="font-family:宋体"}**[if-match]{lang="EN-US"}**[ **route-type**]{lang="EN-US"}[匹配条件，否则，]{style="font-family:宋体"}**[allow-direct]{lang="EN-US"}**[参数失效。]{style="font-family:宋体"}

[**[cost]{lang="EN-US"}***[ cost]{lang="EN-US"}*]{#struct_0_15908_44860_x1149848788}[：引入路由的路由开销，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4261412864]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_327164578}[：引入路由到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[的路由表中。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_15908_44860_1711704720}[：引入路由到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由表中。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_1620937135}[：引入路由到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[的路由表中。如果不指定引入的级别，默认为引入路由到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由表中。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_x1643594210}[：用来过滤引入的路由的路由策略名称，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_15908_44860_1219606841}[：为引入的路由分配管理标签号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[allow-ibgp]{lang="EN-US"}**]{#struct_0_15908_44860_1198321173}[：允许引入]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由，只有当]{style="font-family:宋体"}*[protocol]{lang="EN-US"}*[为]{style="font-family:宋体"}[bgp4+]{lang="EN-US"}[时，该参数可选。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x176298956}

[[对]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_934894848}[而言，其它路由协议发现的路由总被当作路由域外部的路由来处理。从其它协议引入]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由时，还可指定引入路由的缺省开销]{style="font-family:宋体"}[cost]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x464124009}[引入路由时，可以指定将路由引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[级、]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[级或者]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[级路由表中。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}**[import-route bgp4+]{lang="EN-US"}**]{#struct_0_15908_44860_1179382573}[表示只引入]{style="font-family:宋体"}[EBGP]{lang="EN-US"}[路由，]{style="font-family:宋体"}**[import-route bgp4+ allow-ibgp]{lang="EN-US"}**[表示将]{style="font-family:宋体"}[IBGP]{lang="EN-US"}[路由也引入，容易引起路由环路，请慎用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x70705569}

[[\# IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_1620871599}[引入静态路由，并配置]{style="font-family:宋体"}[cost]{lang="EN-US"}[值为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1237604485}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] import-route static cost 15]{lang="EN-US"}
:::

::: {#1540786921 .myid}
[]{#_Toc245204066}[]{#_Toc86723950}[]{#_Toc85873464}[]{#_Toc77992849}[]{#_Toc65740922}[]{#_Toc61239735}[]{#_Toc404789077}[]{#struct_0_15908_44860_x2058459551}[]{#_Toc310607877}[]{#_Toc290886944}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route isisv6 level-1 into level-2**

------------------------------------------------------------------------

[**[import-route isisv6 level-1 into level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x672797255}[命令用来配置]{style="font-family:宋体"}[从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[**[undo import-route isisv6 level-1 into level-2]{lang="EN-US"}**]{#struct_0_15908_44860_875514283}[命令用来配置不]{style="font-family:宋体"}[从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1828498043}

[**[import-route isisv6 level-1 into level-2]{lang="EN-US"}**[ \[ **filter-policy** { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_15908_44860_1620806063}

[**[undo import-route isisv6 level-1 into level-2]{lang="EN-US"}**]{#struct_0_15908_44860_1876248999}

[[【]{style="font-family:黑体"}]{#struct_0_15908_44860_1656262760}[缺省情况]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}]{#struct_0_15908_44860_x1390134242}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1816015629}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_x1857827203}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_505995222}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_1589193166}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1390280003}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_1620740527}

[**[filter-policy]{lang="EN-US"}**]{#struct_0_15908_44860_326972284}[：过滤策略。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_15908_44860_x951372633}[：]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的编号，取值范围]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}***[ prefix-list-name]{lang="EN-US"}*]{#struct_0_15908_44860_x281999115}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_x1629940461}[：路由策略名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_15908_44860_x1336379801}[：为引入的路由分配管理标签号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_1069961314}

[[Level-1-2]{lang="EN-US"}]{#struct_0_15908_44860_1552336705}[路由器可以将它所知道的其他区域的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域路由信息发布给本区域的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1568052847}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1620674991}[设定路由器从]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1533698362}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] import-route isisv6 level-1 into level-2]{lang="EN-US"}
:::

::: {#-474252976 .myid}
[]{#_Toc404789078}[]{#struct_0_15908_44860_x1353467478}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route isisv6 level-2 into level-1**

------------------------------------------------------------------------

[**[import-route isisv6 level-2 into level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x2036613372}[命令用来配置]{style="font-family:宋体"}[从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[**[undo import-route isisv6 level-2 into level-1]{lang="EN-US"}**]{#struct_0_15908_44860_1978066007}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_788197545}

[**[import-route isisv6 level-2 into level-1]{lang="EN-US"}**[ \[ **filter-policy** { *acl6-number* \| **prefix-list** *prefix-list-name* \| **route-policy** *route-policy-name* } \| **tag** *tag* \] \*]{lang="EN-US"}]{#struct_0_15908_44860_x1019566631}

[**[undo import-route isisv6 level-2 into level-1]{lang="EN-US"}**]{#struct_0_15908_44860_1258043981}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1620609455}

[[不]{style="font-family:宋体"}]{#struct_0_15908_44860_1064127757}[从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x512523281}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_1321039028}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1616294571}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_352792184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_228761325}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_341178013}

[**[filter-policy]{lang="EN-US"}**]{#struct_0_15908_44860_x1102054203}[：过滤策略。]{style="font-family:宋体"}

[*[acl6-number]{lang="EN-US"}*]{#struct_0_15908_44860_1620543919}[：]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的编号，取值范围]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix-list]{lang="EN-US"}***[ prefix-list-name]{lang="EN-US"}*]{#struct_0_15908_44860_x841903860}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名称，]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_206085394}[：路由策略名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}**[ *tag*]{lang="EN-US"}]{#struct_0_15908_44860_x996039656}[：为引入的路由分配管理标签号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1824846903}

[[Level-1-2]{lang="EN-US"}]{#struct_0_15908_44860_x774627735}[路由器可以将它所知道的其他区域的]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域路由信息发布给本区域的]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[和]{style="font-family:宋体"}[Level-1-2]{lang="EN-US"}[路由器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1009366586}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_944042825}[设定路由器从]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[进行路由渗透。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1620478383}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] import-route isisv6 level-2 into level-1]{lang="EN-US"}
:::

::: {#-900064531 .myid}
[]{#_Toc86723951}[]{#_Toc85873465}[]{#_Toc77992850}[]{#_Toc72055069}[]{#_Toc404789079}[]{#struct_0_15908_44860_1067702331}[]{#_Toc245204067}[]{#_Toc180404167}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- import-route limit**

------------------------------------------------------------------------

[**[import-route limit]{lang="EN-US"}**]{#struct_0_15908_44860_x1363329884}[命令用来配置引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由最大条数。]{style="font-family:宋体"}

[**[undo import-route limit]{lang="EN-US"}**]{#struct_0_15908_44860_1125584008}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x2060361519}

[**[import-route limit ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_15908_44860_819196414}

[**[undo import-route limit]{lang="EN-US"}**]{#struct_0_15908_44860_x428522035}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1446308462}

[[引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}]{#struct_0_15908_44860_528541903}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由最大条数与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1621461423}

[[IS-IS IPv6]{lang="FR"}]{#struct_0_15908_44860_1505011704}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1809488004}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1785739202}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x822220000}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x68878154}

[*[number]{lang="EN-US"}*]{#struct_0_15908_44860_x1325549141}[：引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由最大条数。不同型号的设备支持的取值范围和缺省值不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x859370891}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_104657457}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[引入]{style="font-family:宋体"}[Level1/Level2]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由最大条数为]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1621395887}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] import-route limit 1000]{lang="EN-US"}
:::

::::: {#-982480200 .myid}
[]{#_Toc404789080}[]{#struct_0_15908_44860_x1744886560}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 bfd enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6%20IS-IS命令.files/image001.png){#图片 22 width="62" height="25"}]{lang="EN-US"}]{#struct_0_15908_44860_x1745345315}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:楷体_GB2312"}]{#struct_0_15908_44860_1811412035}[。]{style="font-family:楷体_GB2312"}
:::

[ ]{lang="EN-US"}

[**[isis ipv6 bfd enable]{lang="EN-US"}**]{#struct_0_15908_44860_x1745410851}[命令用来在使能]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **isis ipv6** **bfd enable**]{lang="EN-US"}]{#struct_0_15908_44860_x1733395101}[命令用来关闭]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1745214243}

[**[isis ipv6 bfd enable]{lang="EN-US"}**]{#struct_0_15908_44860_876123171}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_15908_44860_x1248140752}**[isis]{lang="EN-US"}[ ipv6 bfd enable]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1745279779}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_1596243640}[的]{style="font-family:宋体"}[BFD]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_884800289}

[[接口视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x1745607459}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x19684616}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1745672995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1407849390}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x349397959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_x1745476387}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x783952514}[使能接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1745541923}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ipv6 bfd enable]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_1171393303}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1234741701}[使能接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS BFD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1744821027}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis ipv6 bfd enable]{lang="EN-US"}
:::::

::: {#1081396902 .myid}
[]{#_Toc404789081}[]{#struct_0_15908_44860_1115135039}[]{#_Toc357603593}[]{#_Toc352311322}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 cost**

------------------------------------------------------------------------

[**[isis ipv6 cost]{lang="EN-US"}**]{#struct_0_15908_44860_x1744886563}[命令用来配置接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路开销值。]{style="font-family:宋体"}

[**[undo isis ipv6 cost]{lang="EN-US"}**]{#struct_0_15908_44860_x1545604788}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_2138447782}

[**[isis ipv6 cost ]{lang="EN-US"}***[value]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_15908_44860_x1745345314}

[**[undo isis ipv6 cost ]{lang="EN-US"}**[\[ **level-1** \| **level-2** \]]{lang="EN-US"}]{#struct_0_15908_44860_x917471320}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1476419076}

[[没有配置接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_x1745410850}[链路开销值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_995488254}

[[接口视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x1318888849}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1745214242}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x689960770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1745279778}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_668605527}

[*[value]{lang="EN-US"}*]{#struct_0_15908_44860_x761552652}[：链路开销值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16777215]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_x478999971}[：配置在计算]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_668539991}[：配置在计算]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[路由时使用的链路开销值。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_30159699}

[[接口必须使能]{style="font-family:宋体"}]{#struct_0_15908_44860_x270457508}[IPv6 IS-IS]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}]{#struct_0_15908_44860_x1745607458}[IS-IS]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑标准模式的情况下，接口中配置的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路开销值才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_1546399325}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_x1613919333}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_687234409}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路开销值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x1745672994}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-isis-100-ipv6\] quit]{lang="EN-US"}

[\[Sysname-isis-100\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ipv6 enable 100]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ipv6 cost 10]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_x1613853797}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_31897055}[配置接口]{style="font-family:宋体"}[Vlan-interface11]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[链路开销值为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1441574525}

[\[Sysname\] isis 100]{lang="EN-US"}

[\[Sysname-isis-100\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-isis-100-ipv6\] quit]{lang="EN-US"}

[\[Sysname-isis-100\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 11]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis ipv6 enable 100]{lang="EN-US"}

[\[Sysname-Vlan-interface11\] isis ipv6 cost 10]{lang="EN-US"}
:::

::: {#-750766096 .myid}
[]{#_Toc404789082}[]{#struct_0_15908_44860_1321033965}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 enable**

------------------------------------------------------------------------

[**[isis ipv6 enable]{lang="EN-US"}**]{#struct_0_15908_44860_x1745476386}[命令用来使能接口]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[**[undo isis ipv6 enable]{lang="EN-US"}**]{#struct_0_15908_44860_1944930841}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1811922253}

[**[isis ipv6 enable]{lang="EN-US"}**[ \[ *process-id* \]]{lang="EN-US"}]{#struct_0_15908_44860_x1745541922}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_15908_44860_x1557490052}**[isis]{lang="EN-US"}[ ipv6 enable]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_836574047}

[[没有使能接口]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1744821026}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1613748316}

[[接口视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x1744886562}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_20479153}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_2052117982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_2146337458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x513937498}

[*[process-id]{lang="EN-US"}*]{#struct_0_15908_44860_512116643}[：]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146271922}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_x1284133972}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x714079541}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力，并在接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_2146468530}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] quit]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] ipv6 address 2002::1/64]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ipv6 enable 1]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_x1356276556}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_2146402994}[创建]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[进程]{style="font-family:宋体"}[1]{lang="EN-US"}[，使能]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力，并在接口]{style="font-family:宋体"}[Vlan-interface100]{lang="EN-US"}[上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[能力。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x869773668}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] network-entity 10.0001.1010.1020.1030.00]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6 unicast]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] quit]{lang="EN-US"}

[\[Sysname-isis-1\] quit]{lang="EN-US"}

[\[Sysname\] interface vlan-interface 100]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] ipv6 address 2002::1/64]{lang="EN-US"}

[\[Sysname-Vlan-interface100\] isis ipv6 enable 1]{lang="EN-US"}
:::

::: {#903357565 .myid}
[]{#_Toc404789083}[]{#struct_0_15908_44860_668343382}[]{#_Toc366163116}[]{#_Toc364753100}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 prefix-suppression**

------------------------------------------------------------------------

[**[isis ipv6 prefix-suppression]{lang="EN-US"}**]{#struct_0_15908_44860_x1622547349}[命令用来配置接口的前缀抑制功能。]{style="font-family:
宋体"}

[**[undo isis ipv6 prefix-suppression]{lang="EN-US"}**]{#struct_0_15908_44860_x1550724983}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x258040595}

[**[isis ipv6 prefix-suppression ]{lang="EN-US"}**]{#struct_0_15908_44860_x1277431396}

[**[undo isis ipv6 prefix-suppression ]{lang="EN-US"}**]{#struct_0_15908_44860_668277846}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_739423243}

[[未配置接口的前缀抑制功能。]{style="font-family:宋体"}]{#struct_0_15908_44860_x1206954576}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1514984231}

[[接口视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x1576413590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_907892799}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_668474454}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1039389875}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x717514799}

[[接口上使能]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_541893872}[时，有时候不希望在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中发布此接口的前缀，可以通过在接口上配置此命令，减少此接口的前缀在]{style="font-family:宋体"}[LSP]{lang="EN-US"}[中携带，屏蔽内部节点被发布，提高安全性，加快路由收敛。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x877946896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_668408918}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1782961737}[接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[使能前缀抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x610985350}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}[prefix-suppression]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_1859727565}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_2139944057}[接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[使能前缀抑制功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_668605526}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis ]{lang="EN-US"}[ipv6 ]{lang="EN-US"}[prefix-suppression]{lang="EN-US"}
:::

::: {#764034563 .myid}
[]{#_Toc404789084}[]{#struct_0_15908_44860_x761552651}[]{#_Toc366163123}[]{#_Toc364753102}[]{#_Toc366163117}[]{#_Toc366163118}[]{#_Toc366163119}[]{#_Toc366163120}[]{#_Toc366163121}[]{#_Toc366163122}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- isis ipv6 tag**

------------------------------------------------------------------------

[**[isis ipv6 tag]{lang="EN-US"}**]{#struct_0_15908_44860_x478934435}[命令用来配置接口的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo isis ipv6 tag]{lang="EN-US"}**]{#struct_0_15908_44860_x1713121969}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x159599951}

[**[isis ipv6 tag ]{lang="EN-US"}***[tag]{lang="EN-US"}*]{#struct_0_15908_44860_x1036180820}

[**[undo isis ipv6 tag]{lang="EN-US"}**]{#struct_0_15908_44860_668539990}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_1386490124}

[[没有配置接口的]{style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_15908_44860_481457904}[值。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x590798714}

[[接口视图]{style="font-family:宋体"}]{#struct_0_15908_44860_x663912082}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_391776998}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_668736598}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1167024040}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1378546698}

[*[tag]{lang="EN-US"}*]{#struct_0_15908_44860_x40259603}[：管理标记值]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_581360248}

[[当]{style="font-family:宋体"}[cost-sytle]{lang="EN-US"}]{#struct_0_15908_44860_668671062}[为]{style="font-family:宋体"}[wide]{lang="EN-US"}[、]{style="font-family:宋体"}[wide-compatible ]{lang="EN-US"}[或]{style="font-family:宋体"}[compatible]{lang="EN-US"}[时，如果发布可达的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀具有]{style="font-family:宋体"}[Tag]{lang="EN-US"}[属性，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[会将]{style="font-family:宋体"}[Tag]{lang="EN-US"}[加入到该前缀的]{style="font-family:宋体"}[IP]{lang="EN-US"}[可达信息]{style="font-family:宋体"}[TLV]{lang="EN-US"}[中]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x765044505}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[路由应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_32436939}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1527496510}[配置接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_271600166}

[\[Sysname\] interface gigabitethernet 1/0/1]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/1\] isis ipv6 ]{lang="EN-US"}[tag 4294967295]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[交换应用]{lang="EN-US" style="font-family:宋体"}]{#struct_0_15908_44860_667819094}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_439490340}[配置接口]{style="font-family:宋体"}[Vlan-interface10]{lang="EN-US"}[的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_365618320}

[\[Sysname\] interface vlan-interface 10]{lang="EN-US"}

[\[Sysname-Vlan-interface10\] isis ipv6 ]{lang="EN-US"}[tag 4294967295]{lang="EN-US"}
:::

::::: {#-835536423 .myid}
[]{#_Toc404789085}[]{#struct_0_15908_44860_2146075314}[]{#_Toc357603595}[]{#_Toc357412668}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- ispf enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPv6%20IS-IS命令.files/image001.png){#图片 18 width="62" height="25"}]{lang="EN-US"}]{#struct_0_15908_44860_x1698178683}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:楷体_GB2312"}]{#struct_0_15908_44860_1763189209}
:::

[ ]{lang="EN-US"}

[**[ispf enable]{lang="EN-US"}**]{#struct_0_15908_44860_2146009778}[命令用来使能]{style="font-family:宋体"}[IPv6 IS-IS ISPF]{lang="EN-US"}[功能，即增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_15908_44860_1758744783}[命令用来关闭]{style="font-family:宋体"}[IPv6 IS-IS ISPF]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146206386}

[**[ispf enable]{lang="EN-US"}**]{#struct_0_15908_44860_x1283818631}

[**[undo ispf enable]{lang="EN-US"}**]{#struct_0_15908_44860_x2051387324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146140850}

[[使能]{style="font-family:宋体"}[IPv6 IS-IS ISPF]{lang="EN-US"}]{#struct_0_15908_44860_x2054539537}[功能。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x990391259}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_2146861746}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1399106284}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1898888772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_2146796210}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_648706963}

[[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}]{#struct_0_15908_44860_2146337459}[计算功能后，当网络的拓扑结构发生变化影响到最短路径树的结构时，只将受影响的部分节点进行修正，而不重建整棵最短路径树。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x514003034}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_1201828842}[使能增量]{style="font-family:宋体"}[SPF]{lang="EN-US"}[计算功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_2146271923}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] ]{lang="EN-US"}[ispf enable]{lang="EN-US"}
:::::

::: {#1012649285 .myid}
[]{#_Toc404789086}[]{#struct_0_15908_44860_x1615604183}[]{#_Toc245204068}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- maximum load-balancing**

------------------------------------------------------------------------

[**[maximum load]{lang="EN-US"}**[-**balancing**]{lang="EN-US"}]{#struct_0_15908_44860_x1524929338}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[支持的等]{style="font-family:宋体"}[价路由的最大条数。]{style="font-family:宋体"}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_15908_44860_x666955827}[命令用来恢复缺省]{style="font-family:
宋体"}[情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1780324175}

[**[maximum load-balancing ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_15908_44860_1471513744}

[**[undo maximum load-balancing]{lang="EN-US"}**]{#struct_0_15908_44860_416196859}

[[【缺省情况】]{style="font-family:
黑体"}]{#struct_0_15908_44860_9738399}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1107946217}[支持的]{style="font-family:宋体"}[等价路由的最大条数与与]{style="font-family:
宋体"}[系统支持最大等价路由的条数相同]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x488233712}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1580978092}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1163776377}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_205852436}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_1218528841}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x387929770}

[*[number]{lang="EN-US"}*]{#struct_0_15908_44860_2126255373}[：等价路由的最大条数，不同型号的设备支持的取值范围和缺省值不同，请以设备的情况为准]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x116996134}

[[如果通过]{style="font-family:宋体"}**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_15908_44860_535149623}[命令配置系统支持最大等价路由的条数为]{style="font-family:宋体"}[m]{lang="EN-US"}[，则本命令的缺省值为]{style="font-family:宋体"}[m]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[m]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[max-ecmp-num]{lang="EN-US"}**]{#struct_0_15908_44860_1791645936}[命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1419851449}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x1108011753}[配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[支持的]{style="font-family:宋体"}[等价路由的最大条数为]{style="font-family:宋体"}[2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_991443727}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] maximum load-balancing 2]{lang="EN-US"}
:::

::: {#1298394237 .myid}
[]{#_Toc404789087}[]{#struct_0_15908_44860_2146009779}[]{#_Toc357603597}[]{#_Toc352311321}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- multi-topology**

------------------------------------------------------------------------

[**[multi-topology]{lang="EN-US"}**]{#struct_0_15908_44860_2146206387}[命令用来]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo multiple-topology]{lang="EN-US"}**]{#struct_0_15908_44860_x1283753095}[命令用来取消]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1694784998}

[**[multi-topology]{lang="EN-US"}**[ \[ **compatible** \]]{lang="EN-US"}]{#struct_0_15908_44860_2146140851}

[**[undo multi-topology]{lang="EN-US"}**]{#struct_0_15908_44860_x2054474001}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146861747}

[[没有配置支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1399171820}[拓扑。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x350886927}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_2146796211}[地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_648641427}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_938617820}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_2146337456}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x513282138}

[**[compatible]{lang="EN-US"}**]{#struct_0_15908_44860_2146271920}[：支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑兼容模式，发布]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀时，会向]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[拓扑和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑中分别发布一份。如果未指定本参数，表示不支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑兼容模式，发布]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀时，只会向]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑中发布一份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1284002900}

[[配置此命令之后，]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1837716144}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[将分拓扑进行计算。]{style="font-family:宋体"}

[[本命令必须在链路开销值类型为]{lang="EN-US" style="font-family:宋体"}**[wide]{lang="EN-US"}**]{#struct_0_15908_44860_2146468528}[、]{lang="EN-US" style="font-family:宋体"}**[compatible]{lang="EN-US"}**[或]{lang="EN-US" style="font-family:宋体"}**[wide-compatible]{lang="EN-US"}**[时才能配置。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1356800845}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_2146402992}[配置]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[支持]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x870166884}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] multi-topology]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1940079210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cost-style]{lang="EN-US"}**]{#struct_0_15908_44860_2146075312}
:::

::: {#830408614 .myid}
[]{#_Toc404789088}[]{#struct_0_15908_44860_x363358495}[]{#_Toc245204069}[]{#_Toc86723952}[]{#_Toc85873466}[]{#_Toc77992851}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- preference**

------------------------------------------------------------------------

[**[preference]{lang="EN-US"}**]{#struct_0_15908_44860_x282231788}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由优先级。]{style="font-family:宋体"}

[**[undo preference]{lang="EN-US"}**]{#struct_0_15908_44860_x1769162533}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_251057278}

[**[preference ]{lang="EN-US"}**[{ *preference* \| **route-policy** *route-policy-name* } \*]{lang="EN-US"}]{#struct_0_15908_44860_299765640}

[**[undo preference]{lang="EN-US"}**]{#struct_0_15908_44860_1281242532}

[[【缺省情况下】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1624600965}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1108077289}[路由优先级为]{style="font-family:宋体"}[15]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_705037996}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_x1383449751}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_55249465}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_1231108706}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1246905900}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1307267694}

[*[preference]{lang="EN-US"}*]{#struct_0_15908_44860_1898304419}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[协议]{style="font-family:宋体"}[优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}***[ route-policy-name]{lang="EN-US"}*]{#struct_0_15908_44860_x1818940611}[：指定路由策略名。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1108142825}

[[由于在一台路由器上可能同时运行多种动态路由协议，就存在各个路由协议之间路由信息共享和选择的问题。系统为每一种路由协议配置一个优先级，当不同协议都发现了到同一目的地址的路由时，优先级高的协议将起决定作用。]{style="font-family:宋体"}]{#struct_0_15908_44860_156503725}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_1735558157}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x838026934}[配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由优先级为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_779221114}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] preference 20]{lang="EN-US"}
:::

::: {#-330683803 .myid}
[]{#_Toc352311337}[]{#_Toc404789089}[]{#struct_0_15908_44860_2146796208}[]{#_Toc357603600}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- prefix-priority**

------------------------------------------------------------------------

[**[prefix-priority]{lang="EN-US"}**]{#struct_0_15908_44860_649231252}[命令用来配置指定]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由收敛的优先级。]{style="font-family:宋体"}

[**[undo prefix-]{lang="EN-US"}[priority]{lang="EN-US"}**]{#struct_0_15908_44860_2146337457}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x513347674}

[**[prefix-priority]{lang="EN-US"}**[ { **critical** \| **high** \| **medium** } { **prefix-list** *prefix-list-name* \| **tag** *tag-value* }]{lang="EN-US"}]{#struct_0_15908_44860_2146271921}

[**[prefix-priority]{lang="EN-US"}[ route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_15908_44860_x1284068436}

[**[undo prefix-priority]{lang="EN-US"}**[ { **critical** \| **high** \| **medium** } \[ **prefix-list** \| **tag** \]]{lang="EN-US"}]{#struct_0_15908_44860_237810721}

[**[undo prefix-priority route-policy]{lang="EN-US"}**]{#struct_0_15908_44860_2146468529}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1356735309}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_2146402993}[路由收敛的优先级为低优先级。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x870101348}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_2146075313}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1698113147}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_678135128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_2146009777}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_1759465679}

[**[critical]{lang="EN-US"}**]{#struct_0_15908_44860_2146206385}[：最高优先级。]{style="font-family:宋体"}

[**[high]{lang="EN-US"}**]{#struct_0_15908_44860_x1283622023}[：高优先级。]{style="font-family:宋体"}

[**[medium]{lang="EN-US"}**]{#struct_0_15908_44860_2146140849}[：中优先级。]{style="font-family:宋体"}

[**[route-policy]{lang="EN-US"}**[ *route-policy-name*]{lang="EN-US"}]{#struct_0_15908_44860_x2053949712}[：指]{style="font-family:宋体"}[定路由策略名，]{style="font-family:宋体"}[配置路由收敛的优先级]{style="font-family:宋体"}[。]{style="font-family:宋体"}*[route-policy-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的]{style="font-family:宋体"}[字符串，区分]{style="font-family:宋体"}[大小写。]{style="font-family:宋体"}

[**[prefix-list ]{lang="EN-US"}***[prefix-list-name]{lang="EN-US"}*]{#struct_0_15908_44860_x1825683062}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表名，唯一标识一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀列表。]{style="font-family:宋体"}*[prefix-list-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[tag]{lang="EN-US"}***[ tag-value]{lang="EN-US"}*]{#struct_0_15908_44860_2146861745}[：指定要求的标记值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_1399040748}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_2146796209}[路由的优先级越高收敛的速度越快。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_649165716}[主机路由的优先级为中优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146337454}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x513151066}[配置前缀列表]{style="font-family:宋体"}[standtest]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由收敛的优先级为高优先级。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_2146271918}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] prefix-priority high prefix-list standtest]{lang="EN-US"}
:::

::: {#116059579 .myid}
[]{#_Toc404789090}[]{#struct_0_15908_44860_x1283478609}[]{#_Toc357603601}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- set-overload**

------------------------------------------------------------------------

[**[set-overload]{lang="EN-US"}**]{#struct_0_15908_44860_2146468526}[命令用来为当前路由器配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑的过载标志位。]{style="font-family:宋体"}

[**[undo set-overload]{lang="EN-US"}**]{#struct_0_15908_44860_x1355883341}[命令用来清除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[拓扑的过载标志位。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1731088452}

[**[set-overload]{lang="EN-US"}**[ \[ **on-startup** \[ \[ **start-from-nbr** *system-id* \[ *timeout1* \[ *nbr-timeout* \] \] \] \| *timeout2* \| **wait-for-bgp4+** \[ *timeout3* \] \] \] \[ **allow** { **external** \| **interlevel** } \* \]]{lang="EN-US"}]{#struct_0_15908_44860_2146402990}

[**[undo set-overload]{lang="EN-US"}**]{#struct_0_15908_44860_x870035812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146075310}

[[没有配置过载标志位。]{style="font-family:宋体"}]{#struct_0_15908_44860_x1697916539}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1868876115}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_2146009774}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1759531215}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_2146206382}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x1284080775}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_2146140846}

[**[on-startup]{lang="EN-US"}**]{#struct_0_15908_44860_x2054932752}[：系统启动时将过载标志位置位。]{style="font-family:宋体"}

[**[start-from-nbr]{lang="EN-US"}**[ *system-id* \[ *timeout1* \[ *nbr-timeout* \] \]]{lang="EN-US"}]{#struct_0_15908_44860_2146861742}[：从系统启动时开始计算，如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内仍未与指定邻居建立邻接关系完毕，过载标志位将结束置位状态；如果在]{style="font-family:宋体"}*[nbr-timeout]{lang="EN-US"}*[参数指定的时长内与指定邻居建立邻接关系完毕，过载标志位将继续保持置位状态，]{style="font-family:宋体"}[且从与指定邻居建立邻接关系时重新计时，在]{style="font-family:宋体"}*[timeout1]{lang="EN-US"}*[参数配置的时长内保持置位状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[system-id]{lang="EN-US"}*]{#struct_0_15908_44860_1398844140}[：指定邻居的]{lang="EN-US" style="font-family:宋体"}[System ID]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[timeout1]{lang="EN-US"}*]{#struct_0_15908_44860_444606997}[：]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[nbr-timeout]{lang="EN-US"}*]{#struct_0_15908_44860_2146796206}[：取值范围为]{lang="EN-US" style="font-family:宋体"}[5]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{lang="EN-US" style="font-family:宋体"}[1200]{lang="EN-US"}[秒（]{lang="EN-US" style="font-family:宋体"}[20]{lang="EN-US"}[分钟）。]{lang="EN-US" style="font-family:宋体"}

[*[timeout2]{lang="EN-US"}*]{#struct_0_15908_44860_649100180}[：]{style="font-family:宋体"}[从系统启动时开始计算，过载标志位保持置位状态的时间长度，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒。缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[**[wait-for-bgp4+]{lang="EN-US"}**[ \[ *timeout3* \]]{lang="EN-US"}]{#struct_0_15908_44860_x2048546215}[：]{style="font-family:宋体"}[从系统启动时开始计算，如果在]{style="font-family:宋体"}*[timeout3]{lang="EN-US"}*[参数指定的时长内]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[仍未收敛，过载标志位将结束置位状态。]{style="font-family:宋体"}*[timeout3]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒，缺省值为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒]{style="font-family:宋体"}[（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[allow]{lang="EN-US"}**]{#struct_0_15908_44860_2146337455}[：允许发布地址前缀。缺省情况下，当系统进入过载状态时不允许发布地址前缀。]{style="font-family:宋体"}

[**[external]{lang="EN-US"}**]{#struct_0_15908_44860_x513216602}[：当配置]{style="font-family:宋体"}**[allow]{lang="EN-US"}**[时，允许发布从其它协议学来的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀。]{style="font-family:宋体"}

[**[interlevel]{lang="EN-US"}**]{#struct_0_15908_44860_2146271919}[：当配置]{style="font-family:宋体"}**[allow]{lang="EN-US"}**[时，允许发布从不同层次学来的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址前缀。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1283544145}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果没有指定]{lang="EN-US" style="font-family:宋体"}**[on-startup]{lang="EN-US"}**]{#struct_0_15908_44860_x1423840562}[参数，]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[将立即把过载标志位置位且一直保持置位状态直到用户通过]{lang="EN-US" style="font-family:宋体"}**[undo]{lang="EN-US"}**[ **set-overload**]{lang="EN-US"}[清除过载标志位。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果只指定]{style="font-family:宋体"}]{#struct_0_15908_44860_2146468527}**[on-startup]{lang="EN-US"}**[参数，过载标志位将在系统启动时开始置位，并且在]{style="font-family:宋体"}*[timeout2]{lang="EN-US"}*[参数]{style="font-family:宋体"}[指定的时长内保持置位状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1355817805}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_2146402991}[在当前路由器上配置过载标志位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_x869970276}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] ]{lang="EN-US"}[set-overload]{lang="EN-US"}
:::

::: {#-1230299672 .myid}
[]{#_Toc86723962}[]{#_Toc85873476}[]{#_Toc77992853}[]{#_Toc65740925}[]{#_Toc61239741}[]{#_Toc245204071}[]{#_Toc237920074}[]{#_Toc60036216}[]{#_Toc53707160}[]{#_Toc53487855}[]{#_Toc404789091}[]{#struct_0_15908_44860_x1842644707}[]{#_Toc310607882}[]{#_Toc290886948}[]{#_Toc245204070}[]{#_Toc86723953}[]{#_Toc85873467}[]{#_Toc77992852}[]{#_Toc65740924}[]{#_Toc61239765}[]{#_Toc50980001}[]{#_Toc50984564}[]{#_Toc50988873}[]{#_Toc51059013}[]{#_Toc51059074}[]{#_Toc51068451}[]{#_Toc51069325}[]{#_Toc51073230}[]{#_Toc51074588}[]{#_Toc51074658}[]{#_Toc51076177}[]{#_Toc51077624}[]{#_Toc51139297}[]{#_Toc51146419}[]{#_Toc51147135}[]{#_Toc51148149}[]{#_Toc51148961}[]{#_Toc51149521}[]{#_Toc51109198}[]{#_Toc51356139}[]{#_Toc51870973}[]{#_Toc53375380}[]{#_Toc53384916}[]{#_Toc53465718}[]{#_Toc53485127}[]{#_Toc53485185}[]{#_Toc367622409}[]{#_Toc367622410}[]{#_Toc367622411}[]{#_Toc367622412}[]{#_Toc367622413}[]{#_Toc367622414}[]{#_Toc367622415}[]{#_Toc367622416}[]{#_Toc367622417}[]{#_Toc367622418}[]{#_Toc367622419}[]{#_Toc367622420}[]{#_Toc367622421}[]{#_Toc367622422}[]{#_Toc367622423}[]{#_Toc367622424}[]{#_Toc367622425}[]{#_Toc367622426}[]{#_Toc367622427}[]{#_Toc367622428}[]{#_Toc367622429}[]{#_Toc367622430}[]{#_Toc367622431}[]{#_Toc367622432}[]{#_Toc367622433}[]{#_Toc367622434}[]{#_Toc367622435}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- summary**

------------------------------------------------------------------------

[**[summary]{lang="EN-US"}**]{#struct_0_15908_44860_1007415333}[命令用来配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[聚合路由。]{style="font-family:宋体"}

[**[undo summary]{lang="EN-US"}**]{#struct_0_15908_44860_x921408914}[命令用来删除该聚合路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_1025353263}

[**[summary ]{lang="EN-US"}***[ipv6-prefix prefix-length]{lang="EN-US"}*[ \[ **avoid-feedback** \| **generate_null0_route** \| \[ **level-1** \| **level-1-2** \| **level-2** \] \| **tag** ]{lang="EN-US"}*[tag ]{lang="EN-US"}*[\] \*]{lang="EN-US"}]{#struct_0_15908_44860_460362194}

[**[undo summary ]{lang="EN-US"}***[ipv6-prefix prefix-length ]{lang="EN-US"}*[\[ **level-1** \| **level-1-2** \| **level-2** \]]{lang="EN-US"}]{#struct_0_15908_44860_x1108404969}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x983252692}

[[没有配置]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x1733600503}[聚合路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_1756311749}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_1110093980}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_1737664332}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_654525035}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_2056201745}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_1754178479}

[*[ipv6-prefix]{lang="EN-US"}*]{#struct_0_15908_44860_x1107421929}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[聚合路由前缀。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_15908_44860_x1370115881}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[聚合路由前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[avoid-feedback]{lang="EN-US"}**]{#struct_0_15908_44860_337558771}[：避免通过路由计算学习到聚合路由。]{style="font-family:宋体"}

[**[generate_null0_route]{lang="EN-US"}**]{#struct_0_15908_44860_426013682}[：为防止路由循环而生成]{style="font-family:宋体"}[NULL 0]{lang="EN-US"}[路由。]{style="font-family:宋体"}

[**[level-1]{lang="EN-US"}**]{#struct_0_15908_44860_427227660}[：只对引入到]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域的路由进行聚合。]{style="font-family:宋体"}

[**[level-1-2]{lang="EN-US"}**]{#struct_0_15908_44860_x1157637144}[：对向]{style="font-family:宋体"}[Level-1]{lang="EN-US"}[区域和]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域引入的路由都进行聚合。]{style="font-family:宋体"}

[**[level-2]{lang="EN-US"}**]{#struct_0_15908_44860_x995731376}[：只对引入到]{style="font-family:宋体"}[Level-2]{lang="EN-US"}[区域的路由进行聚合。]{style="font-family:宋体"}

[*[tag]{lang="EN-US"}*]{#struct_0_15908_44860_239251884}[：管理标签号，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_1337108347}

[[如果命令中没有指定]{style="font-family:宋体"}[Level]{lang="EN-US"}]{#struct_0_15908_44860_x1107487465}[，缺省为]{style="font-family:宋体"}**[level-2]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[可以将有相同下一跳的路由聚合为一条路由，这样一方面可以减小路由表规模，另一方面可以减少本路由器生成的]{style="font-family:宋体"}[LSP]{lang="EN-US"}]{#struct_0_15908_44860_x365524652}[报文和]{style="font-family:宋体"}[LSDB]{lang="EN-US"}[的规模。其中，被聚合的路由可以是]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议发现的路由，也可以是被引入的路由。另外，聚合后路由的开销取所有被聚合路由中最小的开销值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_x1252199530}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x724632464}[配置一条]{style="font-family:宋体"}[2002::/32]{lang="EN-US"}[的聚合路由。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_986835665}

[\[Sysname\] isis]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\]]{lang="EN-US"}[ summary 2002:: 32]{lang="EN-US"}
:::

::: {#1171776781 .myid}
[]{#_Toc404789092}[]{#struct_0_15908_44860_x582808041}[]{#_Toc357603603}[]{#_Toc367622437}[]{#_Toc367622438}[]{#_Toc367622439}[]{#_Toc367622440}[]{#_Toc367622441}[]{#_Toc367622442}[]{#_Toc367622443}[]{#_Toc367622444}[]{#_Toc367622445}[]{#_Toc367622446}[]{#_Toc367622447}[]{#_Toc367622448}[]{#_Toc367622449}[]{#_Toc367622450}[]{#_Toc367622451}[]{#_Toc367622452}[]{#_Toc367622453}[]{#_Toc367622454}[]{#_Toc367622455}[]{#_Toc367622456}[]{#_Toc367622457}[]{#_Toc367622458}[]{#_Toc367622459}[]{#_Toc367622460}[]{#_Toc367622461}[]{#_Toc367622462}[]{#_Toc367622463}[]{#_Toc367622464}[]{#_Toc367622465}[]{#_Toc367622466}[]{#_Toc367622467}[]{#_Toc367622468}[]{#_Toc367622469}[]{#_Toc367622470}[]{#_Toc367622471}[]{#_Toc367622472}[]{#_Toc367622473}[]{#_Toc367622474}[]{#_Toc367622475}[]{#_Toc367622476}[]{#_Toc367622477}[]{#_Toc367622478}[]{#_Toc367622479}[]{#_Toc367622480}[]{#_Toc367622481}[]{#_Toc367622482}[]{#_Toc367622483}[]{#_Toc367622484}[]{#_Toc367622485}[]{#_Toc367622486}[]{#_Toc367622487}[]{#_Toc367622488}[]{#_Hlt9934657}[]{#_Toc50980019}[]{#_Toc50984582}[]{#_Toc50988891}[]{#_Toc51059031}[]{#_Toc51059092}[]{#_Toc51068469}[]{#_Toc51069343}[]{#_Toc51073248}[]{#_Toc51074606}[]{#_Toc51074676}[]{#_Toc51076195}[]{#_Toc51077642}[]{#_Toc51139315}[]{#_Toc51146437}[]{#_Toc51147153}[]{#_Toc51148167}[]{#_Toc51148979}[]{#_Toc51149539}[]{#_Toc51109216}[]{#_Toc51356157}[]{#_Toc51870991}[]{#_Hlt12072832}[]{#_Toc58396797}[]{#_Toc58396798}[]{#_Toc58396799}[]{#_Toc58396800}[]{#_Toc58396801}[]{#_Toc58396802}[]{#_Toc58396803}[]{#_Toc58396804}[]{#_Toc58396805}[]{#_Toc58396806}[]{#_Toc58396807}[]{#_Toc58396808}[]{#_Toc58396809}[]{#_Toc58396810}[]{#_Toc58396811}[]{#_Toc58396812}[]{#_Toc367622489}[]{#_Toc367622490}[]{#_Toc367622491}[]{#_Toc367622492}[]{#_Toc367622493}[]{#_Toc367622494}[]{#_Toc367622495}[]{#_Toc367622496}[]{#_Toc367622497}[]{#_Toc367622498}[]{#_Toc367622499}

**IPv6 IS-IS \-- IPv6 IS-IS配置命令 \-- timer spf**

------------------------------------------------------------------------

[**[timer spf]{lang="EN-US"}**]{#struct_0_15908_44860_1425121425}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[ ]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}[路由计算的时间间隔。]{style="font-family:宋体"}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_15908_44860_x582873577}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_15908_44860_633065681}

[**[timer spf ]{lang="EN-US"}***[maximum-interval]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ *minimum-interval* \[ *incremental-interval* \] \]]{lang="EN-US"}]{#struct_0_15908_44860_1729826107}

[**[undo timer spf]{lang="EN-US"}**]{#struct_0_15908_44860_x582676969}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_15908_44860_x535548317}

[[IPv6 IS-IS]{lang="EN-US"}]{#struct_0_15908_44860_x582742505}[路由计算的最大时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[毫秒，]{style="font-family:宋体"}[时间间隔惩罚增量为]{style="font-family:宋体"}[200]{lang="EN-US"}[毫秒]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_15908_44860_x2093524010}

[[IS-IS IPv6]{lang="EN-US"}]{#struct_0_15908_44860_x582021609}[单播地址族视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_15908_44860_x163268448}

[[network-admin]{lang="EN-US"}]{#struct_0_15908_44860_x582087145}

[[mdc-admin]{lang="EN-US"}]{#struct_0_15908_44860_x602103342}

[[【参数】]{style="font-family:黑体"}]{#struct_0_15908_44860_x582545896}

[*[maximum-interval]{lang="EN-US"}*]{#struct_0_15908_44860_1020234712}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由计算的最大时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[*[minimum-interval]{lang="EN-US"}*]{#struct_0_15908_44860_x582611432}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由计算的最小时间间隔，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[*[incremental-interval]{lang="EN-US"}*]{#struct_0_15908_44860_x555697723}[：]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由计算的时间间隔惩罚增量，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[60000]{lang="EN-US"}[，单位为毫秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_15908_44860_x582414824}

[[根据本地维护的]{style="font-family:宋体"}]{#struct_0_15908_44860_x1724049577}[LSDB]{lang="EN-US"}[，运行]{style="font-family:宋体"}[IS-IS]{lang="EN-US"}[协议的路由器通过]{style="font-family:宋体"}[SPF]{lang="EN-US"}[算法计算出以自己为根的最短路径树，并根据这一最短路径树决定到目的网络的下一跳。通过调节]{style="font-family:宋体"}[SPF]{lang="EN-US"}[的计算间隔，可以抑制网络频繁变化可能导致的占用过多带宽资源和路由器资源。]{style="font-family:宋体"}

[[本命令在网络变化不频繁的情况下将连续路由计算的时间间隔缩小到]{style="font-family:宋体"}]{#struct_0_15908_44860_41409948}*[minimum-interval]{lang="EN-US"}*[，而在网络变化频繁的情况下可以进行相应惩罚，将等待时间按照配置的惩罚增量延长，最大不超过]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[需要注意的是，]{style="font-family:宋体"}*[minimum-interval]{lang="EN-US"}*]{#struct_0_15908_44860_x582480360}[和]{style="font-family:宋体"}*[incremental-interval]{lang="EN-US"}*[配置值不允许大于]{style="font-family:宋体"}*[maximum-interval]{lang="EN-US"}*[配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_15908_44860_183715055}

[[\# ]{lang="EN-US"}]{#struct_0_15908_44860_x582808040}[配置路由器]{style="font-family:宋体"}[Sysname]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 IS-IS]{lang="EN-US"}[路由计算的最大时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，最小时间间隔为]{style="font-family:宋体"}[100]{lang="EN-US"}[毫秒，惩罚增量为]{style="font-family:宋体"}[300]{lang="EN-US"}[毫秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_15908_44860_1425055889}

[\[Sysname\] isis 1]{lang="EN-US"}

[\[Sysname-isis-1\] address-family ipv6]{lang="EN-US"}

[\[Sysname-isis-1-ipv6\] ]{lang="EN-US"}[timer spf 10 100 300]{lang="EN-US"}

[ ]{lang="EN-US"}
:::
