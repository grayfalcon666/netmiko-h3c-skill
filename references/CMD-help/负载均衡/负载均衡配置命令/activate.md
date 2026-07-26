::: {#1797341627 .myid}
[]{#_Toc311899208}[]{#_Toc311899217}[]{#_Toc311899219}[]{#_Toc404796555}[]{#struct_0_x7280_11703_1117404874}[]{#_Toc334536486}[]{#_Toc329869230}[]{#_Toc329781856}

**负载均衡 \-- 负载均衡配置命令 \-- activate**

------------------------------------------------------------------------

[**[activate]{lang="EN-US"}**]{#struct_0_x7280_11703_1696323338}[命令用来配置实服务组的可用条件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **activate**]{lang="EN-US"}]{#struct_0_x7280_11703_2123329598}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1529167926}

[**[activate]{lang="EN-US"}**[ **lower** *lower-percentage* **upper** *upper-percentage*]{lang="EN-US"}]{#struct_0_x7280_11703_1632026407}

[**[undo]{lang="EN-US"}**[ **activate**]{lang="EN-US"}]{#struct_0_x7280_11703_x1607848988}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1867073013}

[[实服务组中只要有一个实服务器可用，该实服务组就被认为可用。]{style="font-family:宋体"}]{#struct_0_x7280_11703_282505628}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_203439649}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_595336904}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x842513295}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2123395134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1944532756}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1847316576}

[**[lower]{lang="EN-US"}**[ *lower-percentage*]{lang="EN-US"}]{#struct_0_x7280_11703_x1317828522}[：]{style="font-family:宋体"}[最小可用百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[。当主用实服务组中可用的实服务器数量占实服务器总数量的百分比低于此值时，该实服务组将被认为不可用，从而切换到备用实服务组。]{style="font-family:宋体"}

[**[upper]{lang="EN-US"}**[ *upper-percentage*]{lang="EN-US"}]{#struct_0_x7280_11703_x1315709756}[：]{style="font-family:宋体"}[最大可用百分比，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[99]{lang="EN-US"}[，且必须大于等于最小可用百分比。当主用实服务组中可用的实服务器数量占实服务器总数量的百分比高于此值时，将从备用实服务组切换回主用实服务组。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x536841878}

[[需要注意的是，当虚服务器上未配置备用实服务组时，本配置无效。]{style="font-family:宋体"}]{#struct_0_x7280_11703_829124218}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_440764746}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x406033028}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的最小可用百分比为]{style="font-family:宋体"}[20]{lang="EN-US"}[，最大可用百分比为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2123722814}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] activate lower 20 upper 80]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x348254091}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default]{lang="EN-US"}**[ ]{lang="EN-US"}**[server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_1910390327}
:::

::: {#-1510627815 .myid}
[]{#_Toc404796556}[]{#struct_0_x7280_11703_x1144371398}[]{#_Toc380504911}[]{#_Toc364842540}[]{#_Toc362006270}[]{#_Toc347413202}[]{#_Toc318725268}

**负载均衡 \-- 负载均衡配置命令 \-- case-insensitive**

------------------------------------------------------------------------

[**[case-insensitive]{lang="EN-US"}**]{#struct_0_x7280_11703_x1172866366}[命令用来配置匹配字符串时对大小写不敏感。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[case-insensitive]{lang="EN-US"}**]{#struct_0_x7280_11703_x1325865284}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1856688993}

[**[case-insensitive]{lang="EN-US"}**]{#struct_0_x7280_11703_x1144305862}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[case-insensitive]{lang="EN-US"}**]{#struct_0_x7280_11703_x1640448512}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1562312834}

[[匹配字符串时对大小写敏感。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1993065183}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_27918301}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1336100999}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1735857397}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x408635830}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1144240326}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_796307537}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2019786418}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[本命令将影响以下内容：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1435551244}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于类]{style="font-family:宋体"}]{#struct_0_x7280_11703_x418973631}[匹配，]{lang="EN-US" style="font-family:宋体"}[影响]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部的]{lang="EN-US" style="font-family:宋体"}[取值]{style="font-family:宋体"}[、]{lang="EN-US" style="font-family:宋体"}[HTTP C]{lang="EN-US"}[ookie]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[名称和取值]{style="font-family:宋体"}[、]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x7280_11703_1133081904}[HTTP]{lang="EN-US"}[首部持续性方法，影响首部的取值、]{style="font-family:宋体"}[URL]{lang="EN-US"}[以及用于生成持续性表项的]{style="font-family:宋体"}[Key]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1000759168}[Cookie]{lang="FR"}[截取持续性方法，影响]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[的名称和取值的匹配以及用于生成持续性表项的]{style="font-family:宋体"}[Key]{lang="EN-US"}[值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1961998467}

[]{#_Toc362006256}[]{#_Toc347413195}[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_248112208}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="EN-US"}[中，配置匹配字符串时对大小写不敏感。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1144699078}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] case-insensitive]{lang="EN-US"}
:::

::: {#-1301312999 .myid}
[]{#_Toc404796557}[]{#struct_0_x7280_11703_x1662426893}[]{#_Toc380504912}[]{#_Toc364842541}

**负载均衡 \-- 负载均衡配置命令 \-- check all-packet**

------------------------------------------------------------------------

[**[check]{lang="EN-US"}**[ **all-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_1380309505}[命令用来配置检查所有报文。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **check** **all-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_1308247896}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1638040052}

[**[check]{lang="EN-US"}**[ **all-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_1458181407}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[check]{lang="EN-US"}**[ **all-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_2087170135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1242262157}

[[不检查所有报文。]{style="font-family:宋体"}]{#struct_0_x7280_11703_186014437}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1144633542}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1860907830}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_497258730}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x329029842}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1320163811}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1186435475}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x170279438}[HTTP Cookie]{lang="FR"}[类型的持续性组视图下支持。]{style="font-family:宋体"}

[[需要注意的是]{style="font-family:宋体"}]{#struct_0_x7280_11703_136767591}[：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当持续性方法为]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1144568006}[Cookie]{lang="FR"}[截取时]{style="font-family:宋体"}[，本命令用来配置]{style="font-family:宋体"}[是否从所有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中截取]{style="font-family:宋体"}[Cookie]{lang="FR"}[。如果未配置]{style="font-family:宋体"}[本命令]{style="font-family:宋体"}[，则在一次连接中只从首个应答报文中截取一次]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[信息，后续应答报文不再截取。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当持续性方法为]{style="font-family:宋体"}]{#struct_0_x7280_11703_160920262}[Cookie]{lang="EN-US"}[重写时，]{style="font-family:宋体"}[本命令用来配置]{style="font-family:宋体"}[是否在所有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中重写]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[。如果未配置]{style="font-family:宋体"}[本命令]{style="font-family:宋体"}[，则在一次连接中只在首个应答报文中重写]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[信息，后续应答报文不再重写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当持续性方法为]{style="font-family:宋体"}]{#struct_0_x7280_11703_x336512269}[Cookie]{lang="EN-US"}[插入时，]{style="font-family:宋体"}[本命令用来配置]{style="font-family:宋体"}[是否向所有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中插入]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[。如果未配置]{style="font-family:宋体"}[本命令]{style="font-family:宋体"}[，则在一次连接中只向首个应答报文中插入]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[信息，后续应答报文不再插入。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1828729940}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x555807280}[在]{style="font-family:宋体"}[HTTP Cookie]{lang="FR"}[类型的持续性组]{style="font-family:宋体"}[sg3]{lang="EN-US"}[中，配置检查所有报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x521813289}

[\[Sysname\] sticky-group sg3 type http-cookie]{lang="EN-US"}

[\[Sysname-sticky-http-cookie-sg3\] check all-packet]{lang="EN-US"}
:::

::: {#351315815 .myid}
[]{#_Toc404796558}[]{#struct_0_x7280_11703_x1274804918}[]{#_Toc334536507}[]{#_Toc329869248}[]{#_Toc327781460}

**负载均衡 \-- 负载均衡配置命令 \-- class**

------------------------------------------------------------------------

[**[class]{lang="EN-US"}**]{#struct_0_x7280_11703_x1668907757}[命令用来为负载均衡类指定负载均衡动作。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **class**]{lang="EN-US"}]{#struct_0_x7280_11703_1513343798}[命令用来删除指定的负载均衡类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x229857427}

[**[class]{lang="EN-US"}**[ *class-name* \[ **insert-before** *before-class-name* \] **action** *action-name*]{lang="EN-US"}]{#struct_0_x7280_11703_2005306691}

[**[undo]{lang="EN-US"}**[ **class** *class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_2123788350}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1927138331}

[[没有为任何负载均衡类指定负载均衡动作。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1313220456}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x39670093}

[[负载均衡策略视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_274736715}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1019932583}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1328604464}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2077329616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1557794415}

[*[class-name]{lang="EN-US"}*]{#struct_0_x7280_11703_2123591742}[：负载均衡类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[insert-before]{lang="EN-US"}**[ *before-class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1143912646}[：表示插入到]{style="font-family:宋体"}[指定的负载均衡类之前（该负载均衡类必须已被当前负载均衡策略引用）。]{style="font-family:宋体"}*[before-class-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[action-name]{lang="EN-US"}*]{#struct_0_x7280_11703_763272225}[：负载均衡动作的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1862067200}

[[通过本命令可以为匹配特定负载均衡类的报文指定其执行的负载均衡动作。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1664582665}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1143847110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的负载均衡类可以与同一负载均衡动作组成匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x789854534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通用类型的负载均衡策略只能引用通用类型的负载均衡类和负载均衡动作，]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1529669668}[HTTP]{lang="EN-US"}[类型的负载均衡策略则无此限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_236141660}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_2139816817}[在通用类型的负载均衡策略]{style="font-family:宋体"}[lbp1]{lang="EN-US"}[中，为负载均衡类]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[指定负载均衡动作为]{style="font-family:宋体"}[lba1]{lang="EN-US"}[，并将]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[插入到负载均衡类]{style="font-family:宋体"}[lbc0]{lang="EN-US"}[之前。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1482613155}

[\[Sysname\] loadbalance policy lbp1 type generic]{lang="EN-US"}

[\[Sysname-lbp-generic-lbp1\] class lbc1 insert-before lbc0 action lba1]{lang="EN-US"}
:::

::: {#1235190941 .myid}
[]{#_Toc404796559}[]{#struct_0_x7280_11703_765800734}[]{#_Toc334536520}[]{#_Toc329869261}[]{#_Toc329241946}[]{#_Toc324941103}[]{#_Toc318725185}

**负载均衡 \-- 负载均衡配置命令 \-- connection-limit (real server view)**

------------------------------------------------------------------------

[**[connection-limit]{lang="EN-US"}**]{#struct_0_x7280_11703_2123657278}[命令用来配置实服务器所允许的最大连接数。]{style="font-family:宋体"}

[**[undo]{lang="SV"}**]{#struct_0_x7280_11703_1183494921}[ ]{lang="SV"}**[connection-limit]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1284655452}

[**[connection-limit]{lang="EN-US"}**[ **max** *max-number*]{lang="EN-US"}]{#struct_0_x7280_11703_x379994574}

[**[undo]{lang="SV"}**]{#struct_0_x7280_11703_944887115}[ **connection-limit**]{lang="SV"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_781768452}

[[实服务器所允许的最大连接数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_2084027623}[，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1775843132}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2123984958}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901177947}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1885153718}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1084108734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_614388346}

[*[max-number]{lang="EN-US"}*]{#struct_0_x7280_11703_2042213052}[：最大连接数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示实服务器所允许的最大连接数不受限制。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_721863285}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1907883714}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[所允许的最大连接数为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2124050494}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] connection-limit max 10000]{lang="EN-US"}
:::

::: {#1753459168 .myid}
[]{#_Toc404796560}[]{#struct_0_x7280_11703_247408472}[]{#_Toc334536537}[]{#_Toc329869276}[]{#_Toc329242049}

**负载均衡 \-- 负载均衡配置命令 \-- connection-limit (virtual server view)**

------------------------------------------------------------------------

[**[connection-limit]{lang="EN-US"}**]{#struct_0_x7280_11703_892795636}[命令用来配置虚服务器所允许的最大连接数。]{style="font-family:宋体"}

[**[undo]{lang="SV"}**]{#struct_0_x7280_11703_1448764768}[ ]{lang="SV"}**[connection-limit]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1124306673}

[**[connection-limit]{lang="EN-US"}**[ **max** *max-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1778791065}

[**[undo]{lang="SV"}**]{#struct_0_x7280_11703_x2042773500}[ ]{lang="SV"}**[connection-limit]{lang="EN-US"}**

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1561404259}

[[虚服务器所允许的最大连接数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_2123460667}[，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_392701921}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x545962800}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1329997948}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1739832866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_410516814}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1425558694}

[*[max-number]{lang="EN-US"}*]{#struct_0_x7280_11703_416544837}[：最大连接数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示虚服务器所允许的最大连接数不受限制。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1687984760}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_2123526203}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所允许的最大连接数为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1526383028}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] connection-limit max 10000]{lang="EN-US"}
:::

::::: {#-747790595 .myid}
[]{#_Toc404796561}[]{#struct_0_x7280_11703_x512460370}[]{#_Toc400807508}[]{#_Toc396740866}

**负载均衡 \-- 负载均衡配置命令 \-- connection-sync enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](负载均衡命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7280_11703_x1029975389}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[集中式设备不支持本命令，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7280_11703_748399979}
:::

**[ ]{lang="EN-US"}**

[**[connection-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1053623571}[命令用来]{style="font-family:宋体"}[开启虚服务器的会话扩展信息备份功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[connection-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_70567671}[命令用来关闭虚服务器的会话扩展信息备份功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1010689100}

[**[connection-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_707212576}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[connection-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1724873009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1351315288}

[[虚服务器的会话扩展信息备份功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_233808871}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1242452621}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1352085515}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x156164474}[]{#_GoBack}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x777576555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1228389892}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_733236591}

[[本命令在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_442414126}[类型的虚服务器视图下不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1774359317}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1333060683}[开启]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的会话扩展信息备份功能。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1170419960}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] connection-sync enable]{lang="EN-US"}
:::::

::: {#1340993750 .myid}
[]{#_Toc404796562}[]{#struct_0_x7280_11703_x1144699075}[]{#_Toc380504917}[]{#_Toc364842548}[]{#_Toc362006253}[]{#_Toc347413192}

**负载均衡 \-- 负载均衡配置命令 \-- content**

------------------------------------------------------------------------

[**[content]{lang="EN-US"}**]{#struct_0_x7280_11703_x2065711420}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[content]{lang="EN-US"}**]{#struct_0_x7280_11703_x1144633539}[命令用来删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1224140349}

[**[content]{lang="EN-US"}**[ \[ **offset** *offset* \] \[ **start** *start-string* \] \[ **end** *end-string* \| **length** *length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1513173957}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[content]{lang="EN-US"}**]{#struct_0_x7280_11703_x2142984393}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_143225286}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1144568003}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_564204789}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_741075923}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2020678422}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1251357577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1144502467}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x313171925}

[**[offset]{lang="EN-US"}**[ *offset*]{lang="EN-US"}]{#struct_0_x7280_11703_x845980291}[：实体基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[start]{lang="EN-US"}**[ *start-string*]{lang="EN-US"}]{#struct_0_x7280_11703_1104482748}[：实体开始标记的正则表达式，即从]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[起到本标记为开始，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[字符的字符串。]{style="font-family:宋体"}

[**[end]{lang="EN-US"}**[ *end-string*]{lang="EN-US"}]{#struct_0_x7280_11703_1321744940}[：实体结束标记的正则表达式，即从]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[起到本标记为结束，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[字符的字符串。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *length*]{lang="EN-US"}]{#struct_0_x7280_11703_x1143912643}[：实体的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示所有长度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1863006771}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1686835059}[实体类型的持续性组视图下支持。]{style="font-family:宋体"}

[[本命令用来根据]{style="font-family:宋体"}*[offset]{lang="EN-US"}*]{#struct_0_x7280_11703_x1149715083}[、]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[、]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[及]{style="font-family:宋体"}*[length]{lang="EN-US"}*[获取生成持续性表项的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体信息。]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[将不计入持续性表项信息中。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_939014899}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1143847107}[实体持续性只能对实体内的所有内容进行持续性处理，对于]{style="font-family:宋体"}[chunk]{lang="EN-US"}[及]{style="font-family:宋体"}[multipart]{lang="EN-US"}[形式的实体内容，]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体持续性不能根据具体内容进行明确的持续性处理。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[快速]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1193204597}[HTTP]{lang="EN-US"}[类型的虚服务器不支持引用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体持续性方法。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1415290933}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x7069055}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体类型的持续性组]{style="font-family:宋体"}[sg2]{lang="EN-US"}[中，配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体持续性方法为：从]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的第]{style="font-family:宋体"}[30]{lang="EN-US"}[个字节起，以]{style="font-family:宋体"}[abc]{lang="EN-US"}[为开始、长度为]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体来生成持续性表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1144436932}

[\[Sysname\] sticky-group sg2 type http-content]{lang="EN-US"}

[\[Sysname-sticky-http-content-sg2\] content offset 30 start abc length 20]{lang="EN-US"}
:::

::: {#-804945037 .myid}
[]{#_Toc404796563}[]{#struct_0_x7280_11703_2027736270}[]{#_Toc380504918}[]{#_Toc364842549}[]{#_Toc362006271}[]{#_Toc347413204}[]{#_Toc318725270}

**负载均衡 \-- 负载均衡配置命令 \-- content maxparse-length**

------------------------------------------------------------------------

[**[content]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_x791921137}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体的最大解析长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[content]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_x1612926481}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x930519702}

[**[content]{lang="EN-US"}**[ **maxparse-length** *length*]{lang="EN-US"}]{#struct_0_x7280_11703_x1144371396}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[content]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_x722527672}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x18707294}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1404590796}[实体的最大解析长度为]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1888279728}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1144305860}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x477649098}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1863587499}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_425749268}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x689625260}

[*[length]{lang="FR"}*]{#struct_0_x7280_11703_x1144240324}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[实体的]{style="font-family:
宋体"}[最大解析长度]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1959106951}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1632671403}[HTTP]{lang="FR"}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x79683407}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1499068691}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1144699076}[在]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，配置]{style="font-family:宋体"}[HTTP]{lang="DE"}[实体的最大解析长度为]{style="font-family:宋体"}[8192]{lang="DE"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1825971349}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] content maxparse-length 8192]{lang="EN-US"}
:::

::: {#1945222715 .myid}
[]{#_Toc404796564}[]{#struct_0_x7280_11703_1754834776}[]{#_Toc380504914}[]{#_Toc364842543}[]{#_Toc362006254}[]{#_Toc347413193}

**负载均衡 \-- 负载均衡配置命令 \-- cookie**

------------------------------------------------------------------------

[**[cookie]{lang="EN-US"}**]{#struct_0_x7280_11703_476533155}[命令用来配置]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **cookie**]{lang="EN-US"}]{#struct_0_x7280_11703_x1144633540}[命令用来删除]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x698108416}

[**[cookie]{lang="EN-US"}**[ { **get** **name** *cookie-name* \[ **offset** *offset* \] \[ **start** *start-string*\] \[ **end** *end-string* \| **length** *length* \] \| { **insert** \| **rewrite** } \[ **name** *cookie-name* \] }]{lang="EN-US"}]{#struct_0_x7280_11703_x1130069816}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[cookie]{lang="EN-US"}**[ { **get** \| **insert** \| **rewrite** }]{lang="EN-US"}]{#struct_0_x7280_11703_165507546}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1102372367}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1144568004}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1001879152}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x166541832}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_391878079}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1144502468}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_802573322}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_465546037}

[**[get]{lang="EN-US"}**]{#struct_0_x7280_11703_x861269866}[：表示持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[截取，即在服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中截取]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[字段用于持续性处理。]{style="font-family:宋体"}

[*[cookie-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1143912644}[：]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[offset]{lang="EN-US"}**[ *offset*]{lang="EN-US"}]{#struct_0_x7280_11703_1103491884}[：]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[start]{lang="EN-US"}**[ *start-string*]{lang="EN-US"}]{#struct_0_x7280_11703_1472698377}[：]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[开始标记的正则表达式，即从]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[起到本标记为开始，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[字符的字符串。]{style="font-family:宋体"}

[**[end]{lang="EN-US"}**[ *end-string*]{lang="EN-US"}]{#struct_0_x7280_11703_x2055237658}[：]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[结束标记的正则表达式，即从]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[起到本标记为结束，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[字符的字符串。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *length*]{lang="EN-US"}]{#struct_0_x7280_11703_1398331054}[：]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示所有长度。]{style="font-family:宋体"}

[**[insert]{lang="EN-US"}**]{#struct_0_x7280_11703_x1143847108}[：表示持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入，即在服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中插入]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[字段用于持续性处理。]{style="font-family:宋体"}

[**[rewrite]{lang="EN-US"}**]{#struct_0_x7280_11703_x1146150430}[：表示持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[重写，即改写服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文所携带的]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[字段用于持续性处理。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *cookie-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1681201627}[：]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，缺省值为]{style="font-family:宋体"}[X-LB]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x959627577}

[[本命令只在]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x1144436937}[类型的持续性组视图下支持。]{style="font-family:宋体"}

[**[cookie]{lang="EN-US"}**[ **get**]{lang="EN-US"}]{#struct_0_x7280_11703_1624451743}[命令用来根据]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[、]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[、]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[及]{style="font-family:宋体"}*[length]{lang="EN-US"}*[获取生成持续性表项的]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[信息。]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[将不计入持续性表项信息中。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_441034738}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x7280_11703_868770982}[持续性方法]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[重写时，需要与]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器配合，即服务器]{lang="EN-US" style="font-family:宋体"}[发送]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文中应携带指定名称]{lang="EN-US" style="font-family:宋体"}[Cookie]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[首部]{style="font-family:宋体"}[信息；此外]{lang="EN-US" style="font-family:宋体"}[，系统]{style="font-family:宋体"}[仅修改]{lang="EN-US" style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[中]{lang="EN-US" style="font-family:宋体"}[Cookie]{lang="EN-US"}[的]{style="font-family:宋体"}[名称和值，不会修改其它属性（如]{lang="EN-US" style="font-family:宋体"}[Expires]{lang="EN-US"}[等）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当持续性方法为]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1144371401}[Cookie]{lang="EN-US"}[插入或]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[重写时，所配置的持续性老化时间不为会话老化（持续性表项的超时时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[时），会在对应插入或重写的]{style="font-family:宋体"}[Value]{lang="EN-US"}[值后加入]{style="font-family:宋体"}[Expires]{lang="EN-US"}[字段。如果服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文也携带此属性，负载均衡模块不会修改服务器所携带的该属性，而是在]{style="font-family:宋体"}[Value]{lang="EN-US"}[值后新增用户配置的]{style="font-family:宋体"}[Expires]{lang="EN-US"}[信息。因此在与服务器配合设置]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[重写持续性方法时，建议服务器对于被负载均衡模块重写的]{style="font-family:宋体"}[Set-Cookie]{lang="EN-US"}[首部不要携带任何表征超时的属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_37577042}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1348517207}[在]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的持续性组]{style="font-family:宋体"}[sg3]{lang="EN-US"}[中，配置持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[截取，即：截取从]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的第]{style="font-family:宋体"}[10]{lang="EN-US"}[个字节起，长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[个字节的名为]{style="font-family:宋体"}[user]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[来生成持续性表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x7280_11703_118924530}

[\[Sysname\] sticky-group sg3 type http-cookie]{lang="DE"}

[\[Sysname-sticky-http-cookie-sg3\] cookie get name user offset 10 length 32]{lang="DE"}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_x1519141189}[在]{style="font-family:宋体"}[HTTP Cookie]{lang="DE"}[类型的持续性组]{style="font-family:宋体"}[sg3]{lang="DE"}[中]{style="font-family:宋体"}[，]{style="font-family:宋体"}[配置持续性方法为]{style="font-family:宋体"}[Cookie]{lang="DE"}[插入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x7280_11703_x1144305865}

[\[Sysname\] sticky-group sg3 type http-cookie]{lang="DE"}

[\[Sysname-sticky-http-cookie-sg3\] cookie insert]{lang="EN-US"}
:::

::: {#-367274965 .myid}
[]{#_Toc311899218}[]{#_Toc404796565}[]{#struct_0_x7280_11703_x74364571}[]{#_Toc380504916}[]{#_Toc364842545}[]{#_Toc362006259}

**负载均衡 \-- 负载均衡配置命令 \-- cookie secondary name**

------------------------------------------------------------------------

[**[cookie]{lang="EN-US"}**[ **secondary** **name**]{lang="EN-US"}]{#struct_0_x7280_11703_x1144240329}[命令用来指定需在]{style="font-family:宋体"}[URI]{lang="EN-US"}[中查找的]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[cookie]{lang="EN-US"}**[ **secondary** **name**]{lang="EN-US"}]{#struct_0_x7280_11703_2006161118}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1018006434}

[**[cookie]{lang="EN-US"}**[ **secondary** **name** *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1736642980}

[**[undo]{lang="EN-US"}**[ **cookie** **secondary** **name**]{lang="EN-US"}]{#struct_0_x7280_11703_x1144699081}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_258904368}

[[未指定需在]{style="font-family:宋体"}]{#struct_0_x7280_11703_593229405}[URI]{lang="FR"}[中查找的]{style="font-family:宋体"}[Secondary Cookie]{lang="FR"}[名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1277677080}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2092384460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1144633545}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1101392943}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_261716444}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x806565206}

[*[value]{lang="FR"}*]{#struct_0_x7280_11703_1884174410}[：]{style="font-family:宋体"}[Secondary Cookie]{lang="FR"}[的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[63]{lang="FR"}[个]{style="font-family:宋体"}[Token]{lang="FR"}[字符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[区分大小写]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不包括]{style="font-family:宋体"}[(]{lang="FR"}[、]{style="font-family:宋体"}[)]{lang="FR"}[、]{style="font-family:宋体"}[\<]{lang="FR"}[、]{style="font-family:
宋体"}[\>]{lang="FR"}[、]{style="font-family:宋体"}[@]{lang="FR"}[、]{style="font-family:宋体"}[,]{lang="FR"}[、]{style="font-family:宋体"}[;]{lang="FR"}[、]{style="font-family:
宋体"}[:]{lang="FR"}[、]{style="font-family:宋体"}[\\]{lang="FR"}[、]{style="font-family:宋体"}[\"]{lang="FR"}[、]{style="font-family:宋体"}[/]{lang="FR"}[、]{style="font-family:
宋体"}[\[]{lang="FR"}[、]{style="font-family:宋体"}[\]]{lang="FR"}[、]{style="font-family:宋体"}[?]{lang="FR"}[、]{style="font-family:宋体"}[=]{lang="FR"}[、]{style="font-family:
宋体"}[{]{lang="FR"}[、]{style="font-family:宋体"}[}]{lang="FR"}[、]{style="font-family:宋体"}[SP]{lang="FR"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）]{style="font-family:宋体"}[、]{style="font-family:宋体"}[HT]{lang="FR"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:
宋体"}[），]{style="font-family:宋体"}[以及]{style="font-family:
宋体"}[ASCII]{lang="FR"}[码小于或等于]{style="font-family:宋体"}[31]{lang="FR"}[，]{style="font-family:宋体"}[大于或等于]{style="font-family:
宋体"}[127]{lang="FR"}[的字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1144568009}

[[本命令只在]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x954824985}[类型的持续性组视图下支持。]{style="font-family:宋体"}

[[需要注意的是，本命令只对]{style="font-family:宋体"}[Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x497082199}[截取持续性方法生效。即：当配置了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[截取持续性方法时，如果也配置了本命令，此时系统如果未能在]{style="font-family:宋体"}[HTPP]{lang="EN-US"}[请求报文首部找到指定名称的]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[，便会查找出现在]{style="font-family:宋体"}[URI]{lang="EN-US"}[中的]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1088961538}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1144502473}[在]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的持续性组]{style="font-family:宋体"}[sg3]{lang="EN-US"}[中，指定需在]{style="font-family:宋体"}[URI]{lang="EN-US"}[中查找的]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[名称为]{style="font-family:宋体"}[sid]{lang="DE"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2012361367}

[\[Sysname\] sticky-group sg3 type http-cookie]{lang="EN-US"}

[\[Sysname-sticky-http-cookie-sg3\] ]{lang="EN-US"}[cookie secondary name sid]{lang="DE"}
:::

::: {#-354887862 .myid}
[]{#_Toc404796566}[]{#struct_0_x7280_11703_1591174060}[]{#_Toc334536534}[]{#_Toc329869273}[]{#_Toc329242045}

**负载均衡 \-- 负载均衡配置命令 \-- default server-farm**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**[ ]{lang="EN-US"}**[server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_1638738687}[命令用来指定]{style="font-family:宋体"}[默认的实服务组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **default** **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_661371289}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1311048357}

[**[default]{lang="EN-US"}**[ **server-farm** *server-farm-name* \[ **backup** *backup-server-farm-name* \] \[ **sticky** *sticky-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x2017058599}

[**[undo]{lang="EN-US"}**[ **default** **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_1080737053}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2123329595}

[[没有指定默认的实服务组。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1529495606}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_861656458}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2017529652}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_102147464}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1529307372}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_472039272}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_900663281}

[*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1855412249}[：主用实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**[ *backup-*]{lang="EN-US"}*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_2123395131}[：备用实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[sticky]{lang="EN-US"}**[ ]{lang="EN-US"}*[sticky-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1944860436}[：持续性组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1199338138}

[[当主用实服务组可用（该实服务组存在且有可用的实服务器）时，虚服务器通过主用实服务组进行转发；当主用实服务组不可用而备用实服务组可用时，虚服务器通过备用实服务组进行转发。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1704020997}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_327245330}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1181852068}[为]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[指定默认的主用实服务组为]{style="font-family:宋体"}[sf]{lang="EN-US"}[，备用实服务组为]{style="font-family:宋体"}[sfb]{lang="EN-US"}[，持续性组名称为]{style="font-family:宋体"}[sg1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1405717818}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] default server-farm sf backup sfb sticky sg1]{lang="EN-US"}
:::

::: {#-522330810 .myid}
[]{#_Toc404796567}[]{#struct_0_x7280_11703_x1446543013}[]{#_Toc334536508}[]{#_Toc329869249}

**负载均衡 \-- 负载均衡配置命令 \-- default-class action**

------------------------------------------------------------------------

[**[default-class]{lang="EN-US"}**[ **action**]{lang="EN-US"}]{#struct_0_x7280_11703_2071400688}[命令]{style="font-family:宋体"}[用来配置默认的负载均衡动作。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **default-class**]{lang="EN-US"}]{#struct_0_x7280_11703_2123722811}[命令]{style="font-family:宋体"}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x347926411}

[**[default-class]{lang="EN-US"}**[ **action** *action-name*]{lang="EN-US"}]{#struct_0_x7280_11703_162354706}

[**[undo]{lang="EN-US"}**[ **default-class**]{lang="EN-US"}]{#struct_0_x7280_11703_1367391903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1740228746}

[[未指定默认的负载均衡动作。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x204412685}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x934803404}

[[负载均衡策略视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_496261042}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2123788347}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1927334940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x2083298925}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x395923715}

[*[action-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x808073030}[：负载均衡动作的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1381991452}

[[通过本命令可以为未匹配任何负载均衡类的报文指定其执行的默认动作。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1482872124}

[[需要注意的是，通用类型的负载均衡策略只能用通用类型的负载均衡动作作为其默认的负载均衡动作，]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1144699082}[类型的负载均衡策略则无此限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1351882807}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1623157491}[在通用类型的负载均衡策略]{style="font-family:宋体"}[lbp1]{lang="EN-US"}[中，配置默认的负载均衡动作为]{style="font-family:宋体"}[lba1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2123591739}

[\[Sysname\] loadbalance policy lbp1 type generic]{lang="EN-US"}

[\[Sysname-lbp-generic-lbp1\] default-class action lba1]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404796568}[]{#struct_0_x7280_11703_763599898}[]{#_Toc334536499}[]{#_Toc329869240}[]{#_Toc326931113}

**负载均衡 \-- 负载均衡配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x7280_11703_2132451661}[命令用来配置描述信息。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x7280_11703_1702859905}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1329447852}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x7280_11703_1072594843}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x7280_11703_956434124}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_999941781}

[[不存在任何描述信息。]{style="font-family:宋体"}]{#struct_0_x7280_11703_2123657275}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1182642953}

[[负载均衡动作视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1704562165}[负载均衡类视图]{style="font-family:宋体"}[/]{lang="EN-US"}[负载均衡策略视图]{style="font-family:宋体"}[/]{lang="EN-US"}[参数模板视图]{style="font-family:宋体"}[/]{lang="EN-US"}[实服务器视图]{style="font-family:宋体"}[/]{lang="EN-US"}[实服务组视图]{style="font-family:宋体"}[/SNAT]{lang="EN-US"}[地址池视图]{style="font-family:宋体"}[/]{lang="EN-US"}[持续性组视图]{style="font-family:宋体"}[/]{lang="EN-US"}[虚服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_508508686}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1353625694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x359920506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1081281810}

[*[text]{lang="EN-US"}*]{#struct_0_x7280_11703_1657462240}[：描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2123984955}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1901374555}[配置通用类型的负载均衡动作]{style="font-family:宋体"}[lba1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[LB action LBA1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x851984508}

[\[Sysname\] loadbalance action lba1 type generic]{lang="EN-US"}

[\[Sysname-lba-generic-lba1\] description LB action LBA1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_967845393}[配置通用类型的负载均衡类]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[LB class LBC1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1100626232}

[\[Sysname\] loadbalance class lbc1 type generic]{lang="EN-US"}

[\[Sysname-lbc-generic-lbc1\] description LB class LBC1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x882989589}[配置通用类型的负载均衡策略]{style="font-family:宋体"}[lbp1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[LB policy LBP1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1854597862}

[\[Sysname\] loadbalance policy lbp1 type generic]{lang="EN-US"}

[\[Sysname-lbp-generic-lbp1\] description LB policy LBP1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x2041083635}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp2]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Parameter profile PP2]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2123788348}

[\[Sysname\] parameter-profile pp2 type ip]{lang="EN-US"}

[\[Sysname-para-ip-pp2\] description Parameter profile PP2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1182839561}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Real server RS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1716340275}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] description Real server RS]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1756065690}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Server farm SF]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_727440898}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] description Server farm SF]{lang="EN-US"}

[[\# ]{lang="PT-BR"}]{#struct_0_x7280_11703_173167245}[配置]{style="font-family:宋体"}[SNAT]{lang="PT-BR"}[地址池]{style="font-family:宋体"}[lbsp]{lang="PT-BR"}[的描述信息为"]{style="font-family:宋体"}[SNAT pool LBSP]{lang="EN-US"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1002044939}

[\[Sysname\] loadbalance snat-pool lbsp]{lang="EN-US"}

[\[Sysname-lbsnat-pool-lbsp\] description SNAT pool LBSP]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_685379177}[配置持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Sticky group SG1]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1373475303}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] description Sticky group SG1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1719130230}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[Virtual server VS]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x605291612}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] description Virtual server VS]{lang="EN-US"}
:::

::: {#443049948 .myid}
[]{#_Toc404796569}[]{#struct_0_x7280_11703_x90544805}[]{#_Toc334536503}[]{#_Toc329869244}[]{#_Toc324248603}

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance action**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **loadbalance** **action**]{lang="EN-US"}]{#struct_0_x7280_11703_1410504253}[命令用来]{style="font-family:宋体"}[显示负载均衡动作的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1878862101}

[**[display]{lang="EN-US"}**[ **loadbalance** **action** \[ **name** *action-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1462336630}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x474788169}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2119851464}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x774667513}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x605226076}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1512626672}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1315958291}

[**[name]{lang="EN-US"}**[ *action-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1828607777}[：显示指定负载均衡动作的信息。]{style="font-family:宋体"}*[action-name]{lang="EN-US"}*[为负载均衡动作的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡动作的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1231110165}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1591270775}[显示所有负载均衡动作的信息。]{style="font-family:宋体"}

[[\<Sysname\> display loadbalance action]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466311}

[LB action: lba1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: Generic]{lang="EN-US"}

[  State: Inactive]{lang="EN-US"}

[  Forward type: Drop]{lang="EN-US"}

[  IP ToS:]{lang="EN-US"}

[ ]{lang="EN-US"}

[LB action: lba2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: HTTP]{lang="EN-US"}

[  State: Active]{lang="EN-US"}

[  Forward type: Server farm]{lang="EN-US"}

[  Server farm: sf (in use)]{lang="EN-US"}

[  Backup server farm: sfb]{lang="EN-US"}

[  Sticky: sg3]{lang="EN-US"}

[  IP ToS: 20]{lang="EN-US"}

[  SSL client policy:]{lang="EN-US"}

[  Header delete:]{lang="EN-US"}

[    Name: ww]{lang="EN-US"}

[    Direction: Request]{lang="EN-US"}

[  Header insert:]{lang="EN-US"}

[    Name: aa]{lang="EN-US"}

[    Value: 1234567890123456789012345678901234567890123456789012345678901234567890]{lang="EN-US"}

[    Direction: Both]{lang="EN-US"}

[  Header insert:]{lang="EN-US"}

[    Name: cc]{lang="EN-US"}

[    Value: dd]{lang="EN-US"}

[    Direction: Request]{lang="EN-US"}

[  Header rewrite:]{lang="EN-US"}

[    Name: ee]{lang="EN-US"}

[    Value: dd]{lang="EN-US"}

[    Replacement: ff]{lang="EN-US"}

[    Direction: Response]{lang="EN-US"}

[  SSL URL rewrite:]{lang="EN-US"}

[    Value: 12]{lang="EN-US"}

[    Clear port: 12]{lang="EN-US"}

[    SSL port: 123]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display loadbalance action]{lang="EN-US"}]{#struct_0_x7280_11703_1856804550}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1168505288}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2024582752}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_x312293466}

[[LB action]{lang="EN-US"}]{#struct_0_x7280_11703_290419748}

[[负载均衡动作的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_655455457}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x604832860}

[[负载均衡动作的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_1167001773}

[[Type]{lang="EN-US"}]{#struct_0_x7280_11703_421450402}

[[负载均衡动作的类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_421515938}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic]{lang="EN-US"}]{#struct_0_x7280_11703_1891704838}[：表示通用类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_421581474}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x7280_11703_x771700628}

[[负载均衡动作的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x324271457}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x7280_11703_x1447856820}[：]{lang="EN-US" style="font-family:宋体"}[可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x7280_11703_x605422683}[：]{lang="EN-US" style="font-family:宋体"}[不可用]{style="font-family:宋体"}

[[Forward]{lang="EN-US"}]{#struct_0_x7280_11703_334235699}[ t]{lang="EN-US"}[ype]{lang="EN-US"}

[[负载均衡动作中的报文转发模式，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_424378202}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[D]{lang="EN-US"}[rop]{lang="EN-US"}]{#struct_0_x7280_11703_x1384299008}[：]{lang="EN-US" style="font-family:宋体"}[丢弃]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Forward]{lang="EN-US"}]{#struct_0_x7280_11703_x1719636055}[：正常转发]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S]{lang="EN-US"}[erver farm]{lang="EN-US"}]{#struct_0_x7280_11703_x605357147}[：]{lang="EN-US" style="font-family:宋体"}[通过实服务组指导转发]{style="font-family:宋体"}

[[Server farm]{lang="EN-US"}]{#struct_0_x7280_11703_1905741549}

[[指导转发的主用实服务组名称，]{style="font-family:宋体"}[(in use)]{lang="EN-US"}]{#struct_0_x7280_11703_x2087282648}[表示该实服务组正被使用。只有当报文转发模式为]{style="font-family:宋体"}[server farm]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Backup server farm]{lang="EN-US"}]{#struct_0_x7280_11703_1770142132}

[[指导转发的备用实服务组名称，]{style="font-family:宋体"}[(in use)]{lang="EN-US"}]{#struct_0_x7280_11703_x1528488418}[表示该实服务组正被使用。只有当报文转发模式为]{style="font-family:宋体"}[server farm]{lang="EN-US"}[时才会显示本字段]{style="font-family:宋体"}

[[Sticky]{lang="EN-US"}]{#struct_0_x7280_11703_x605553755}

[[指导转发的持续性组名称，只有当报文转发模式为]{style="font-family:宋体"}[server farm]{lang="EN-US"}]{#struct_0_x7280_11703_727284906}[时才会显示本字段]{style="font-family:宋体"}

[[IP ToS]{lang="EN-US"}]{#struct_0_x7280_11703_1234633496}

[[IP]{lang="EN-US"}]{#struct_0_x7280_11703_69765499}[报文的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段值]{style="font-family:宋体"}

[[SSL client policy]{lang="EN-US"}]{#struct_0_x7280_11703_x2060892358}

[[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_x201335802}[客户端策略的名称，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡动作才会显示本字段]{style="font-family:宋体"}

[[Header delete]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466307}

[[删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1174501596}[首部的配置，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Name]{lang="EN-US"}]{#struct_0_x7280_11703_x97230806}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{lang="EN-US" style="font-family:宋体"}[首部的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direction]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466306}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文的]{style="font-family:宋体"}[方向，包括]{lang="EN-US" style="font-family:宋体"}[Both]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Request]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Response]{lang="EN-US"}

[[只有配置了]{style="font-family:宋体"}**[header]{lang="EN-US"}**[ **delete**]{lang="EN-US"}]{#struct_0_x7280_11703_391582345}[命令才会显示本字段]{style="font-family:宋体"}

[[Header insert]{lang="EN-US"}]{#struct_0_x7280_11703_x755786395}

[[插入]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466305}[首部的配置，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Name]{lang="EN-US"}]{#struct_0_x7280_11703_x11702182}[：要插入]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文中]{lang="EN-US" style="font-family:宋体"}[的首部名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Value]{lang="EN-US"}]{#struct_0_x7280_11703_937712928}[：要插入]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文中的]{lang="EN-US" style="font-family:宋体"}[首部内容]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direction]{lang="EN-US"}]{#struct_0_x7280_11703_1966422405}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文的]{style="font-family:宋体"}[方向，包括]{lang="EN-US" style="font-family:宋体"}[Both]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Request]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Response]{lang="EN-US"}

[[只有配置了]{style="font-family:宋体"}**[header]{lang="EN-US"}**[ **insert**]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466304}[命令才会显示本字段]{style="font-family:宋体"}

[[Header rewrite]{lang="EN-US"}]{#struct_0_x7280_11703_1554381759}

[[重写]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_202223771}[首部的配置，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Name]{lang="EN-US"}]{#struct_0_x7280_11703_x1337871741}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{lang="EN-US" style="font-family:宋体"}[首部的名称]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Value]{lang="EN-US"}]{#struct_0_x7280_11703_x1664466303}[：要被重写的]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{lang="EN-US" style="font-family:宋体"}[首部的内容]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Replacement]{lang="EN-US"}]{#struct_0_x7280_11703_794866872}[：重写后的内容]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Direction]{lang="EN-US"}]{#struct_0_x7280_11703_674185848}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[报文的]{style="font-family:宋体"}[方向，包括]{lang="EN-US" style="font-family:宋体"}[Both]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Request]{lang="EN-US"}[和]{lang="EN-US" style="font-family:宋体"}[Response]{lang="EN-US"}

[[只有配置了]{style="font-family:宋体"}**[header]{lang="EN-US"}**[ **rewrite**]{lang="EN-US"}]{#struct_0_x7280_11703_x1386492888}[命令才会显示本字段]{style="font-family:宋体"}

[[SSL URL rewrite]{lang="EN-US"}]{#struct_0_x7280_11703_x259297293}

[[重写服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_674185849}[应答报文]{style="font-family:宋体"}[Location]{lang="EN-US"}[首部的]{style="font-family:宋体"}[URL]{lang="EN-US"}[的配置，其中：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Value]{lang="EN-US"}]{#struct_0_x7280_11703_x1386492889}[：]{lang="EN-US" style="font-family:宋体"}[Location]{lang="FR"}[首部]{lang="EN-US" style="font-family:宋体"}[URL]{lang="FR"}[的正则表达式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Clear port]{lang="EN-US"}]{#struct_0_x7280_11703_1306786648}[：]{lang="EN-US" style="font-family:宋体"}[原]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL port]{lang="EN-US"}]{#struct_0_x7280_11703_x2096558909}[：]{lang="EN-US" style="font-family:宋体"}[重写后]{lang="EN-US" style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="FR"}[端口号]{lang="EN-US" style="font-family:宋体"}

[[只有配置了]{style="font-family:宋体"}**[ssl]{lang="EN-US"}**[ **url** **rewrite**]{lang="EN-US"}]{#struct_0_x7280_11703_674185850}[命令才会显示本字段]{style="font-family:
  宋体"}

[[ ]{lang="EN-US"}]{#_Toc334536526}

::: {#806555679 .myid}
[]{#_Toc404796570}[]{#struct_0_x7280_11703_569822256}

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance class**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **loadbalance** **class**]{lang="EN-US"}]{#struct_0_x7280_11703_403332782}[命令用来显示负载均衡类的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_394437158}

[**[display]{lang="EN-US"}**[ **loadbalance** **class** \[ **name** *class-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1245032342}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1245010596}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_674185851}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_569822255}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_403332785}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_394437155}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1245032331}

[**[name]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1244945057}[：显示指定负载均衡类的信息。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[为负载均衡类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡类的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x322837277}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_674185852}[显示所有负载均衡类的信息。]{style="font-family:宋体"}

[[\<Sysname\> display loadbalance class]{lang="EN-US"}]{#struct_0_x7280_11703_569822254}

[LB class: lbc1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: HTTP]{lang="EN-US"}

[  Match type: Match-all]{lang="EN-US"}

[  Match rule:]{lang="EN-US"}

[    match 1 source ip address 1.2.3.0 24]{lang="EN-US"}

[    match 2 source ipv6 address 1::2]{lang="EN-US"}

[    match 3 cookie abc value 123]{lang="EN-US"}

[    match 4 header def value 12]{lang="EN-US"}

[    match 5 method ext xde]{lang="EN-US"}

[    match 6 method rfc CONNECT]{lang="EN-US"}

[    match 7 class cla2]{lang="EN-US"}

[    match 8 url 2q3]{lang="EN-US"}

[ ]{lang="EN-US"}

[LB class: lbc2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: Generic]{lang="EN-US"}

[  Match type: Match-any]{lang="EN-US"}

[  Match rule:]{lang="EN-US"}

[    match 1 class cla2]{lang="EN-US"}

[    match 2 source ip address 1.2.23.0 24]{lang="EN-US"}

[    match 3 source ipv6 address 1::12]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display loadbalance class]{lang="EN-US"}]{#struct_0_x7280_11703_403332784}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2031837583}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_674185853}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_569822253}

[[LB class]{lang="EN-US"}]{#struct_0_x7280_11703_674185854}

[[负载均衡类的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_569822260}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_674185855}

[[负载均衡类的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_569822259}

[[Type]{lang="EN-US"}]{#struct_0_x7280_11703_403332797}

[[负载均衡类的类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_674185856}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic]{lang="EN-US"}]{#struct_0_x7280_11703_569822258}[：表示通用类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_674185857}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Match type]{lang="EN-US"}]{#struct_0_x7280_11703_569822257}

[[负载均衡类的匹配类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1863664248}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Match-all]{lang="EN-US"}]{#struct_0_x7280_11703_2086675954}[：]{style="font-family:宋体"}[表示需要匹配所有规则才算匹配该类]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Match-any]{lang="EN-US"}]{#struct_0_x7280_11703_1863664249}[：]{style="font-family:宋体"}[表示只需匹配任一规则就算匹配该类]{lang="EN-US" style="font-family:宋体"}

[[Match rule]{lang="EN-US"}]{#struct_0_x7280_11703_2086610418}

[[负载均衡类包含的匹配规则]{style="font-family:宋体"}]{#struct_0_x7280_11703_x720737484}

[ ]{lang="EN-US"}

::::: {#-1139154600 .myid}
[]{#_Toc404796571}[]{#struct_0_x7280_11703_1410050539}[]{#_Toc400807518}[]{#_Toc396740868}[]{#_Toc393891091}

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance hot-backup statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](负载均衡命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7280_11703_2053178662}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[集中式设备不支持本命令，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7280_11703_x1318832816}
:::

**[ ]{lang="EN-US"}**

[**[display]{lang="EN-US"}**[ **loadbalance** **hot-backup** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_692822221}[命令用来]{style="font-family:宋体"}[显示负载均衡双机热备的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1647247184}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1254751496}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **loadbalance** **hot-backup** **statistics**]{lang="EN-US"}[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1388597234}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7280_11703_x1833811301}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **loadbalance** **hot-backup** **statistics**]{lang="EN-US"}[ \[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1807519053}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1780713982}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_247251125}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1841280017}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_186729495}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x2065684867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_726273000}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1264043647}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x204108445}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_968463795}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x2125401870}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x128801001}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1202162057}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x160547104}[显示负载均衡双机热备的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display loadbalance hot-backup statistics]{lang="EN-US"}]{#struct_0_x7280_11703_x559317929}

[Slot 2:]{lang="EN-US"}

[               TryAdd    TryDel    AckDel    AckOK     AckNO     NotSpt]{lang="EN-US"}

[  StiSnd       1         0         0         0         0         0]{lang="EN-US"}

[  StiRcv       0         0         0         0         0         0]{lang="EN-US"}

[  StiSndFail   0         0         0         0         0         0]{lang="EN-US"}

[  StiRcvFail   0         0         0         0         0         0]{lang="EN-US"}

[  MsgSnd       1         0         0         0         0         0]{lang="EN-US"}

[  MsgRcv       0         0         0         0         0         0]{lang="EN-US"}

[  MsgSndFail   0         0         0         0         0         0]{lang="EN-US"}

[  MsgRcvFail   0         0         0         0         0         0]{lang="EN-US"}

[ ]{lang="EN-US"}

[  SesBkTotal : 0]{lang="EN-US"}

[  SesBkFail  : 0]{lang="EN-US"}

[  SesResTotal: 0]{lang="EN-US"}

[  SesResFail : 0]{lang="EN-US"}

[  SesUpdate  : 0]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display loadbalance hotbackup statistics]{lang="EN-US"}]{#struct_0_x7280_11703_x853491192}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1281717746}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_992312821}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_491058850}

[[TryAdd]{lang="EN-US"}]{#struct_0_x7280_11703_x1300130531}

[[持续性表项添加消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_1006766012}

[[TryDel]{lang="EN-US"}]{#struct_0_x7280_11703_1407847616}

[[持续性表项删除消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x785088334}

[[AckDel]{lang="EN-US"}]{#struct_0_x7280_11703_x1722117343}

[[持续性表项确认删除消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_1288606623}

[[AckOK]{lang="EN-US"}]{#struct_0_x7280_11703_x1011654556}

[[持续性表项可以删除消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x512263762}

[[AckNO]{lang="EN-US"}]{#struct_0_x7280_11703_x1391234013}

[[持续性表项不能删除消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x239445833}

[[NotSpt]{lang="EN-US"}]{#struct_0_x7280_11703_1053820179}

[[不支持的持续性表项消息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1097915378}

[[StiSnd]{lang="EN-US"}]{#struct_0_x7280_11703_x1860210100}

[[发送条数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x155967866}

[[StiRcv]{lang="EN-US"}]{#struct_0_x7280_11703_2143011499}

[[接收条数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1076450327}

[[StiSndFail]{lang="EN-US"}]{#struct_0_x7280_11703_1410116075}

[[发送失败条数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1634135615}

[[StiRcvFail]{lang="EN-US"}]{#struct_0_x7280_11703_208981491}

[[接收失败条数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1414544470}

[[MsgSnd]{lang="EN-US"}]{#struct_0_x7280_11703_x1318767280}

[[报文发送次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x250435980}

[[MsgRcv]{lang="EN-US"}]{#struct_0_x7280_11703_103197578}

[[报文接收次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_247316661}

[[MsgSndFail]{lang="EN-US"}]{#struct_0_x7280_11703_254796742}

[[报文发送失败次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1532367102}

[[MsgRcvFail]{lang="EN-US"}]{#struct_0_x7280_11703_x2125336334}

[[报文发送失败次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1588168777}

[[SesBkTotal]{lang="EN-US"}]{#struct_0_x7280_11703_x531705217}

[[会话备份次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x559252393}

[[SesBkFail]{lang="EN-US"}]{#struct_0_x7280_11703_x1232729943}

[[会话备份失败次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1412878033}

[[SesResTotal]{lang="EN-US"}]{#struct_0_x7280_11703_1006831548}

[[会话恢复次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1788254081}

[[SesResFail]{lang="EN-US"}]{#struct_0_x7280_11703_789858839}

[[会话恢复失败次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1722051807}

[[SesUpdate]{lang="EN-US"}]{#struct_0_x7280_11703_x1863327462}

[[会话更新次数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x512198226}

[ ]{lang="EN-US"}

::: {#773393145 .myid}
[]{#_Toc404796572}[]{#struct_0_x7280_11703_1863664250}

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance policy**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **loadbalance** **policy**]{lang="EN-US"}]{#struct_0_x7280_11703_2087200241}[命令用来显示负载均衡策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1081251157}

[**[display]{lang="EN-US"}**[ **loadbalance** **policy** \[ **name** *policy-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_232278665}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1816870413}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1477573604}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x941073112}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1863664251}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_2087134705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1864942340}

[**[name]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x822665629}[：显示指定负载均衡策略的信息。]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[为负载均衡策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有负载均衡策略的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x55073849}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x710830198}[显示所有负载均衡策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display loadbalance policy]{lang="EN-US"}]{#struct_0_x7280_11703_1863664252}

[LB policy: lbp1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: Generic]{lang="EN-US"}

[  Class: lbc1]{lang="EN-US"}

[   Action: lba1]{lang="EN-US"}

[  Default class action: lba0]{lang="EN-US"}

[ ]{lang="EN-US"}

[LB policy: lbp2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: HTTP]{lang="EN-US"}

[  Default class action:]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display loadbalance policy]{lang="EN-US"}]{#struct_0_x7280_11703_2087331313}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2042885233}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x697377048}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_1863664253}

[[LB policy]{lang="EN-US"}]{#struct_0_x7280_11703_2087265777}

[[负载均衡策略的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_856797617}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_1863664254}

[[负载均衡策略的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_2086938097}

[[Type]{lang="EN-US"}]{#struct_0_x7280_11703_1863664255}

[[负载均衡策略的类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_2086872561}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Generic]{lang="EN-US"}]{#struct_0_x7280_11703_1863664256}[：表示通用类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_2087069169}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[Class]{lang="EN-US"}]{#struct_0_x7280_11703_x677365062}

[[负载均衡策略包含的负载均衡类]{style="font-family:宋体"}]{#struct_0_x7280_11703_1863664257}

[[Action]{lang="EN-US"}]{#struct_0_x7280_11703_2087003633}

[[负载均衡类对应的负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_x92650888}

[[Default class action ]{lang="EN-US"}]{#struct_0_x7280_11703_x908745191}

[[默认的负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_x92650887}

[ ]{lang="EN-US"}

::: {#1017093602 .myid}
[]{#_Toc404796573}[]{#struct_0_x7280_11703_x908745196}

**负载均衡 \-- 负载均衡配置命令 \-- display loadbalance snat-pool**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **loadbalance** **snat-pool**]{lang="EN-US"}]{#struct_0_x7280_11703_x62113643}[命令用来显示]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1898846111}

[**[display]{lang="EN-US"}**[ **loadbalance** **snat-pool** \[ **name** *pool-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_114507994}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x792830643}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1745410396}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x92650886}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x908745197}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x62048107}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1452439033}

[**[name]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_x7280_11703_2092061899}[：显示指定]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x690235510}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x237468844}[显示所有]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的信息。]{style="font-family:宋体"}

[[\<Sysname\> display loadbalance snat-pool]{lang="EN-US"}]{#struct_0_x7280_11703_x92650885}

[SNAT pool: lbsp1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  IPv4 range]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Start address                       End address]{lang="EN-US"}

[    202.110.10.10                       202.110.10.15]{lang="EN-US"}

[  IPv6 range]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Start address                       End address]{lang="EN-US"}

[    2002::2                             2002::100]{lang="EN-US"}

[ ]{lang="EN-US"}

[SNAT pool: lbsp2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  IPv4 range]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Start address                       End address]{lang="EN-US"}

[    203.110.10.10                       203.110.10.15]{lang="EN-US"}

[  IPv6 range]{lang="EN-US"}[：]{style="font-family:宋体"}

[    Start address                       End address]{lang="EN-US"}

[    2003::2                             2003::100]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display loadbalancesnat-pool]{lang="EN-US"}]{#struct_0_x7280_11703_x908745194}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x2022411107}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x92650884}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_x908745195}

[[SNAT pool]{lang="EN-US"}]{#struct_0_x7280_11703_x92650883}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x908745200}[地址池的名称]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x92650882}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x908745201}[地址池的描述信息]{style="font-family:宋体"}

[[IPv4 range]{lang="EN-US"}]{#struct_0_x7280_11703_x92650881}

[[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x908745198}[地址段]{style="font-family:宋体"}

[[IPv6 range]{lang="EN-US"}]{#struct_0_x7280_11703_x92650880}

[[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x908745199}[地址段]{style="font-family:宋体"}

[[Start address]{lang="EN-US"}]{#struct_0_x7280_11703_x62179179}

[[起始地址]{style="font-family:宋体"}]{#struct_0_x7280_11703_x92650879}

[[End address]{lang="EN-US"}]{#struct_0_x7280_11703_x188701158}

[[结束地址]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2048966024}

[ ]{lang="EN-US"}

::: {#2070564070 .myid}
[]{#_Toc404796574}[]{#struct_0_x7280_11703_1579474081}

**负载均衡 \-- 负载均衡配置命令 \-- display parameter-profile**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **parameter-profile**]{lang="EN-US"}]{#struct_0_x7280_11703_x361101578}[命令用来显示参数模板的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1335913129}

[**[display]{lang="EN-US"}**[ **parameter-profile** \[ **name** *parameter-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_319030472}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1972886988}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2048966023}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_13390140}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x77188366}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x1876723813}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1830477819}

[**[name]{lang="EN-US"}**[ *parameter-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x159402299}[：显示指定参数模板的信息。]{style="font-family:宋体"}*[parameter-name]{lang="EN-US"}*[为参数模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有参数模板的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1388579162}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x822851956}[显示所有参数模板的信息。]{style="font-family:宋体"}

[[\<Sysname\> display parameter-profile]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966022}

[Parameter profile: pp1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: IP]{lang="EN-US"}

[  ]{lang="EN-US"}[IP ToS: 20]{lang="EN-US"}

[ ]{lang="EN-US"}

[Parameter profile: pp2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: TCP]{lang="EN-US"}

[  ]{lang="EN-US"}[Exceed MSS: Allow]{lang="EN-US"}

[  TCP window size]{lang="EN-US"}[：]{style="font-family:宋体"}[65535]{lang="EN-US"}

[ ]{lang="EN-US"}

[Parameter profile: pp3]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Type: HTTP]{lang="EN-US"}

[  Rebalance per request: Enabled]{lang="EN-US"}

[  Server connection reuse: Enabled]{lang="EN-US"}

[  Case insensitive: Enabled]{lang="EN-US"}

[  ]{lang="EN-US"}[Header modify per request: Enabled]{lang="EN-US"}

[  ]{lang="EN-US"}[Content maximum parse length: 8192]{lang="EN-US"}

[  ]{lang="EN-US"}[Header maximum parse length: 8192]{lang="EN-US"}

[  ]{lang="EN-US"}[Secondary cookie delimiters: !@#\$]{lang="EN-US"}

[  ]{lang="EN-US"}[Secondary cookie start: ?]{lang="EN-US"}

[  ]{lang="EN-US"}[Header exceed length: Drop]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display parameter-profile]{lang="EN-US"}]{#struct_0_x7280_11703_x1552693801}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1736284093}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2048966021}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_1176189554}

[[Parameter profile]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966020}

[[参数模板的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x389894387}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x106031134}

[[参数模板的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2048966019}

[[Type]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966018}

[[参数模板的类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x33467419}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IP]{lang="EN-US"}]{#struct_0_x7280_11703_671289456}[：表示]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966017}[：表示]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TCP]{lang="EN-US"}]{#struct_0_x7280_11703_1982955216}[：表示]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[类型]{lang="EN-US" style="font-family:宋体"}

[[IP ToS]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966016}

[[发往服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7280_11703_416871275}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段]{style="font-family:宋体"}

[[Exceed MSS]{lang="EN-US"}]{#struct_0_x7280_11703_x2048966015}

[[对客户端发来的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1149212666}[请求报文中超出]{style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段的处理方式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Allow]{lang="EN-US"}]{#struct_0_x7280_11703_x2001085156}[：表示允许超出]{lang="EN-US" style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_x7280_11703_289686136}[：表示丢弃超出]{style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段]{style="font-family:宋体"}

[[Rebalance per request]{lang="EN-US"}]{#struct_0_x7280_11703_298833551}

[[是否开启对每个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_289686137}[请求报文都进行负载均衡的功能，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_298833552}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_289686138}[：开启]{lang="EN-US" style="font-family:宋体"}

[[Server connection reuse]{lang="EN-US"}]{#struct_0_x7280_11703_298833553}

[[是否开启允许负载均衡设备与服务器的连接复用的功能，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1739698518}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_289686139}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_298833554}[：开启]{lang="EN-US" style="font-family:宋体"}

[[Header modify per request]{lang="EN-US"}]{#struct_0_x7280_11703_289686140}

[[是否开启对每个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1657481591}[请求或应答报文的首部都执行插入、删除或修改操作的功能，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_289686141}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_x1657481590}[：开启]{lang="EN-US" style="font-family:宋体"}

[[Case insensitive]{lang="EN-US"}]{#struct_0_x7280_11703_289686142}

[[是否开启匹配字符串时对大小写不敏感的功能，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1657481589}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_289686143}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_x1657481588}[：开启]{lang="EN-US" style="font-family:宋体"}

[[Content maximum parse length]{lang="EN-US"}]{#struct_0_x7280_11703_289686144}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1657481587}[实体的最大解析长度]{style="font-family:宋体"}

[[Header maximum parse length]{lang="EN-US"}]{#struct_0_x7280_11703_289686145}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1657481586}[首部的最大解析长度]{style="font-family:宋体"}

[[Secondary cookie delimiters]{lang="EN-US"}]{#struct_0_x7280_11703_x1666629000}

[[URL]{lang="EN-US"}]{#struct_0_x7280_11703_1558531976}[中分隔]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[的字符]{style="font-family:宋体"}

[[Secondary cookie start]{lang="EN-US"}]{#struct_0_x7280_11703_x1666628999}

[[URL]{lang="EN-US"}]{#struct_0_x7280_11703_x230351022}[中]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[的起始位置标示字符]{style="font-family:宋体"}

[[Header exceed length]{lang="EN-US"}]{#struct_0_x7280_11703_x1666628998}

[[当]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1335732919}[请求或应答报文首部超出最大长度时的处理方式，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Continue]{lang="EN-US"}]{#struct_0_x7280_11703_x1666628997}[：表示继续执行负载均衡操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Drop]{lang="EN-US"}]{#struct_0_x7280_11703_932448392}[：表示停止执行负载均衡操作，丢弃该报文并关闭连接]{style="font-family:宋体"}

[[TCP window size]{lang="EN-US"}]{#struct_0_x7280_11703_x1666628996}

[[TCP]{lang="EN-US"}]{#struct_0_x7280_11703_x1796434963}[连接中的本地最大窗口值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1903666550 .myid}
[]{#_Toc404796575}[]{#struct_0_x7280_11703_x1954805011}

**负载均衡 \-- 负载均衡配置命令 \-- display real-server**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **real-server**]{lang="EN-US"}]{#struct_0_x7280_11703_x1753012778}[命令用来]{style="font-family:宋体"}[显示实服务器的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x605488219}

[**[display]{lang="EN-US"}**[ **real-server** \[ **brief** \| **name** *real-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1060279866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x564517933}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1373196642}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_164884622}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_292849453}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_125982074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x483253235}

[**[brief]{lang="EN-US"}**]{#struct_0_x7280_11703_x605160539}[：显示实服务器的简要信息。如果未指定本参数，将显示实服务器的详细信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *real-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1215696673}[：显示指定实服务器的信息。]{style="font-family:宋体"}*[real-server-name]{lang="EN-US"}*[为实服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有实服务器的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x990255568}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_469074766}[显示所有实服务器的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display real-server brief]{lang="EN-US"}]{#struct_0_x7280_11703_176928939}

[Real server      Address              Port  State          Server farm]{lang="EN-US"}

[rs1              192.168.1.1          0     Active         sf]{lang="EN-US"}

[rs2              192.168.1.2          0     Active         sf]{lang="EN-US"}

[rs3              192.168.1.3          0     Active         sf]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_585507785}[显示实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display real-server name rs]{lang="EN-US"}]{#struct_0_x7280_11703_x605095003}

[Real server: rs]{lang="EN-US"}

[  Description:]{lang="EN-US"}[ Real server RS]{lang="EN-US"}

[  State: Active]{lang="EN-US"}

[  IPv4 address: 1.1.1.1]{lang="EN-US"}

[  IPv6 address: 1001::1]{lang="EN-US"}

[  Port: 8080]{lang="EN-US"}

[  Server farm: sf]{lang="EN-US"}

[  Weight: 150]{lang="EN-US"}

[  Priority: 3]{lang="EN-US"}

[  Slow shutdown: Enabled]{lang="EN-US"}

[  Connection limit: 10000]{lang="EN-US"}

[  Rate limit:]{lang="EN-US"}

[    Connections: 10000]{lang="EN-US"}

[    Bandwidth: 10000 Kbytes/s]{lang="EN-US"}

[    Inbound bandwidth: 5000 Kbytes/s]{lang="EN-US"}

[    Outbound bandwidth: 5000 Kbytes/s]{lang="EN-US"}

[  Probe information:]{lang="EN-US"}

[    Probe success criteria: All]{lang="EN-US"}

[    Probe method      State]{lang="EN-US"}

[    t4                Succeeded]{lang="EN-US"}

[]{#_Toc334536527}[]{#_Toc329869266}[]{#_Toc329241945}[]{#_Toc323399354}[[表1-7 ]{lang="EN-US"}[display real-server]{lang="EN-US"}]{#struct_0_x7280_11703_1088108420}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1165487016}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2005675399}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_587902183}

[[Real server]{lang="EN-US"}]{#struct_0_x7280_11703_x605291611}

[[实服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x90348197}

[[Address]{lang="EN-US"}]{#struct_0_x7280_11703_x326670846}

[[实服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x1907949154}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x7280_11703_x680360718}

[[实服务器的端口号]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1510325081}

[[State]{lang="EN-US"}]{#struct_0_x7280_11703_x605226075}

[[实服务器的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1512692208}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x7280_11703_x271508564}[：可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x7280_11703_1388469642}[：不可用（由于]{style="font-family:宋体"}[配置不完全]{lang="EN-US" style="font-family:宋体"}[、未]{style="font-family:宋体"}[被引用或虚服务]{lang="EN-US" style="font-family:宋体"}[器尚未开启）]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Probe-failed]{lang="EN-US"}]{#struct_0_x7280_11703_x7453011}[：]{style="font-family:宋体"}[健康检测失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ramp]{lang="EN-US"}]{#struct_0_x7280_11703_177907499}[：温暖上线的爬升阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown]{lang="EN-US"}]{#struct_0_x7280_11703_x604898395}[：关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_x7280_11703_1857001158}[：温暖上线的]{style="font-family:宋体"}[准备阶段]{lang="EN-US" style="font-family:宋体"}

[[Server farm]{lang="EN-US"}]{#struct_0_x7280_11703_1504620665}

[[实服务器所属的实服务组]{style="font-family:宋体"}]{#struct_0_x7280_11703_x118152287}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x604832859}

[[实服务器的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_1166543020}

[[IPv4 address]{lang="EN-US"}]{#struct_0_x7280_11703_x1210797832}

[[实服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_702705862}[地址]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_x7280_11703_x40845520}

[[实服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x605422686}[地址]{style="font-family:宋体"}

[[Weight]{lang="EN-US"}]{#struct_0_x7280_11703_334039091}

[[实服务器的权值]{style="font-family:宋体"}]{#struct_0_x7280_11703_x675923212}

[[Priority]{lang="EN-US"}]{#struct_0_x7280_11703_x376670339}

[[实服务器的调用优先级]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1214250306}

[[Slow shutdown]{lang="EN-US"}]{#struct_0_x7280_11703_x605357150}

[[实服务器慢宕功能的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1905544940}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_x489163345}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_x771960888}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[Connection limit]{lang="EN-US"}]{#struct_0_x7280_11703_x605553758}

[[实服务器所允许的最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_726432938}

[[Rate limit]{lang="EN-US"}]{#struct_0_x7280_11703_672023164}

[[实服务器的速率限制]{style="font-family:宋体"}]{#struct_0_x7280_11703_106465975}

[[Connections]{lang="EN-US"}]{#struct_0_x7280_11703_x964425296}

[[实服务器所允许的每秒最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x189831086}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_x605488222}

[[实服务器所允许的最大总带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1061000763}[秒]{style="font-family:宋体"}

[[Inbound bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_x2060564678}

[[实服务器所允许的最大入带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x2060499142}[秒]{style="font-family:宋体"}

[[Outbound bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_205297574}

[[实服务器所允许的最大出带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1644482620}[秒]{style="font-family:宋体"}

[[Probe success criteria]{lang="EN-US"}]{#struct_0_x7280_11703_965366738}

[[实服务器健康检测的成功条件：]{style="font-family:宋体"}]{#struct_0_x7280_11703_478941745}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[All]{lang="EN-US"}]{#struct_0_x7280_11703_x605160542}[：只有全部方法都通过检测才认为健康检测成功]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[At least]{lang="EN-US"}]{#struct_0_x7280_11703_x1215237926}[ 3]{lang="EN-US"}[：]{style="font-family:宋体"}[健康检测成功所需通过检测的最少方法数]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}[3]{lang="EN-US"}

[[Probe method]{lang="EN-US"}]{#struct_0_x7280_11703_x1305029350}

[[健康检测方法所使用的]{style="font-family:宋体"}[NQA]{lang="EN-US"}]{#struct_0_x7280_11703_x605095006}[模板名称]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x7280_11703_1087780740}

[[健康检测方法的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_93157141}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Failed]{lang="EN-US"}]{#struct_0_x7280_11703_1651820731}[：]{style="font-family:宋体"}[健康检测失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[In progress]{lang="EN-US"}]{#struct_0_x7280_11703_x605291614}[：]{style="font-family:宋体"}[正在进行健康检测]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_x7280_11703_x90675877}[：]{style="font-family:宋体"}[健康检测]{lang="EN-US" style="font-family:宋体"}[不可用（因其]{style="font-family:宋体"}[所使用的]{lang="EN-US" style="font-family:宋体"}[NQA]{lang="EN-US"}[模板配置不完全]{lang="EN-US" style="font-family:宋体"}[），或者实服务器不可用]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Succeeded]{lang="EN-US"}]{#struct_0_x7280_11703_x605226078}[：]{style="font-family:宋体"}[健康检测成功]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-600607166 .myid}
[]{#_Toc404796576}[]{#struct_0_x7280_11703_1513544176}

**负载均衡 \-- 负载均衡配置命令 \-- display real-server statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **real-server** **statistic**]{lang="EN-US"}]{#struct_0_x7280_11703_1310775018}[命令用来]{style="font-family:宋体"}[显示实服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:
黑体"}]{#struct_0_x7280_11703_156310}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x520960590}

[**[display]{lang="EN-US"}**[ **real-server** **statistics** \[ **name** *real-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_263913923}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_246429812}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **real-server** **statistics** \[ **name** *real-server-name* \]]{lang="EN-US"}[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x7280_11703_821797423}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7280_11703_x153882046}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **real-server** **statistics** \[ **name** *real-server-name* \] \[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x604898398}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1856673478}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1639397641}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x75878766}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x2097888656}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x294587050}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2122160806}

[**[name]{lang="EN-US"}**[ *real-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1991911166}[：显示指定实服务器的统计信息。]{style="font-family:宋体"}*[real-server-name]{lang="EN-US"}*[为实服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有实服务器的统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x682695955}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x604832862}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1609504874}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1167132845}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_771487151}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1619510041}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1331597712}[显示实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display real-server statistics name rs]{lang="EN-US"}]{#struct_0_x7280_11703_x605422685}

[Real server: rs]{lang="EN-US"}

[  Total connections: 1798]{lang="EN-US"}

[  Active connections: 788]{lang="EN-US"}

[  Max connections: 803]{lang="EN-US"}

[  Connections per second: 157]{lang="EN-US"}

[  Max connections per second: 163]{lang="EN-US"}

[  Server input: 333332 bytes]{lang="EN-US"}

[  Server output: 472054 bytes]{lang="EN-US"}

[  Throughput: 4396 bytes/s]{lang="EN-US"}

[  Inbound throughput: 1214 bytes/s]{lang="EN-US"}

[  Outbound throughput: 3128 bytes/s]{lang="EN-US"}

[  Max throughput: 4564 bytes/s]{lang="EN-US"}

[  Max inbound throughput: 1214 bytes/s]{lang="EN-US"}

[  Max outbound throughput: 3320 bytes/s]{lang="EN-US"}

[  Received packets: 1798]{lang="EN-US"}

[  Sent packets: 0]{lang="EN-US"}

[  Dropped packets: 0]{lang="EN-US"}

[  Received requests: 0]{lang="EN-US"}

[  Dropped requests: 0]{lang="EN-US"}

[  Sent responses: 0]{lang="EN-US"}

[  Dropped responses: 0]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display real-server statistics]{lang="EN-US"}]{#struct_0_x7280_11703_334104627}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x914394727}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_421450396}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_1380193294}

[[Real server]{lang="EN-US"}]{#struct_0_x7280_11703_x1476787535}

[[实服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2021428770}

[[Total ]{lang="EN-US"}]{#struct_0_x7280_11703_1277464085}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[总连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x617871625}

[[Active ]{lang="EN-US"}]{#struct_0_x7280_11703_x605357149}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[当前活动的连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1905086189}

[[Max ]{lang="EN-US"}]{#struct_0_x7280_11703_x99218152}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1563250427}

[[Connections per second]{lang="EN-US"}]{#struct_0_x7280_11703_221442218}

[[每秒连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1966600214}

[[Max ]{lang="EN-US"}]{#struct_0_x7280_11703_x605553757}[c]{lang="EN-US"}[onnection]{lang="EN-US"}[s per second]{lang="EN-US"}

[[最大每秒连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_727153834}

[[Server input]{lang="EN-US"}]{#struct_0_x7280_11703_421581468}

[[从服务器收到的流量，单位为字节]{style="font-family:宋体"}]{#struct_0_x7280_11703_422171292}

[[Server output]{lang="EN-US"}]{#struct_0_x7280_11703_422236828}

[[向服务器发出的流量，单位为字节]{style="font-family:宋体"}]{#struct_0_x7280_11703_421647003}

[[Throughput]{lang="EN-US"}]{#struct_0_x7280_11703_421712539}

[[报文的总吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_421778075}[秒]{style="font-family:宋体"}

[[Inbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x2060826821}

[[报文的入吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1051096807}[秒]{style="font-family:宋体"}

[[Outbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x2060761285}

[[报文的出吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x803182263}[秒]{style="font-family:宋体"}

[[Max throughput]{lang="EN-US"}]{#struct_0_x7280_11703_421843611}

[[报文的最大总吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_421384859}[秒]{style="font-family:宋体"}

[[Max inbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x526252125}

[[报文的最大入吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x2060695749}[秒]{style="font-family:宋体"}

[[Max outbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_975595367}

[[报文的最大出吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x1883183563}[秒]{style="font-family:宋体"}

[[Received ]{lang="EN-US"}]{#struct_0_x7280_11703_x1756400118}[p]{lang="EN-US"}[ackets]{lang="EN-US"}

[[收到的报文数]{style="font-family:宋体"}]{#struct_0_x7280_11703_479830868}

[[Sen]{lang="EN-US"}]{#struct_0_x7280_11703_x1725194566}[t]{lang="EN-US"}[ ]{lang="EN-US"}[p]{lang="EN-US"}[ackets]{lang="EN-US"}

[[发出的报文数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x605488221}

[[Dropped packets]{lang="EN-US"}]{#struct_0_x7280_11703_1060804155}

[[丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1022941901}

[[Received requests]{lang="EN-US"}]{#struct_0_x7280_11703_421450395}

[[接收的]{style="font-family:宋体"}]{#struct_0_x7280_11703_421515931}[HTTP]{lang="EN-US"}[请求报文数量，只有七层实服务器才会显示本字段]{style="font-family:宋体"}

[[Dropped requests]{lang="EN-US"}]{#struct_0_x7280_11703_421581467}

[[丢弃的]{style="font-family:宋体"}]{#struct_0_x7280_11703_422171291}[HTTP]{lang="EN-US"}[请求报文数量，只有七层实服务器才会显示本字段]{style="font-family:宋体"}

[[Sent responses]{lang="EN-US"}]{#struct_0_x7280_11703_422236827}

[[发出的]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498635677}[HTTP]{lang="EN-US"}[应答报文数量，只有七层实服务器才会显示本字段]{style="font-family:宋体"}

[[Dropped responses]{lang="EN-US"}]{#struct_0_x7280_11703_x1498701213}

[[丢弃的]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498766749}[HTTP]{lang="EN-US"}[应答报文数量，只有七层实服务器才会显示本字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1710935022}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **real-server** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_x293314096}

::: {#2121617872 .myid}
[]{#_Toc404796577}[]{#struct_0_x7280_11703_x2044463047}[]{#_Toc334536491}

**负载均衡 \-- 负载均衡配置命令 \-- display server-farm**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_x1899987380}[命令用来]{style="font-family:宋体"}[显示实服务组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1398678073}

[**[display]{lang="EN-US"}**[ **server-farm** \[ **brief** \| **name** *server-farm-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x605095005}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2026602136}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x817819434}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x289930401}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1005828785}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_552397906}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1473430715}

[**[brief]{lang="EN-US"}**]{#struct_0_x7280_11703_x605291613}[：显示实服务组的简要信息。如果未指定本参数，将显示实服务组的详细信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ ]{lang="EN-US"}*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x90479269}[：显示指定实服务组的信息。]{style="font-family:宋体"}*[server-farm-name]{lang="EN-US"}*[为实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串]{style="font-family:宋体"}[，不区分大小写。如果未指定本参数，将显示所有实服务组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x486406056}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x605934045}[显示所有实服务组的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display server-farm brief]{lang="EN-US"}]{#struct_0_x7280_11703_x1620851666}

[Predictor: RR - round robin, RD - random, LC - least connection,]{lang="EN-US"}

[           HASH(SIP) - hash address source IP,]{lang="EN-US"}

[           HASH(DIP) - hash address destination IP,]{lang="EN-US"}

[           HASH(SIP-PORT) - hash address source IP-port]{lang="EN-US"}

[NAT/SNAT: Y - enabled, N - disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[Server farm       Predictor       NAT  SNAT  Total  Active]{lang="EN-US"}

[sf                RR              Y    N     3      3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x605226077}[显示所有实服务组的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display server-farm]{lang="EN-US"}]{#struct_0_x7280_11703_1512561136}

[Server farm: sf1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Predictor: Hash address]{lang="EN-US"}

[  NAT: Enbaled]{lang="EN-US"}

[  SNAT pool:]{lang="EN-US"}

[  Failed action: Keep]{lang="EN-US"}

[  Active threshold: Enabled]{lang="EN-US"}

[    Lower: 80]{lang="EN-US"}

[    Upper: 90]{lang="EN-US"}

[  Slow-online: Enabled]{lang="EN-US"}

[  Standby time: 5s]{lang="EN-US"}

[  Ramp-up time: 10s]{lang="EN-US"}

[  Selected server: Enbaled]{lang="EN-US"}

[    Min server: 100]{lang="EN-US"}

[    Max server: 600]{lang="EN-US"}

[  Total real server: 2]{lang="EN-US"}

[  Active real server: 1]{lang="EN-US"}

[  Real server list:]{lang="EN-US"}

[  Name             State         Address              Port  Weight Priority]{lang="EN-US"}

[  rs1              Inactive      1.2.3.4              0     4      100]{lang="EN-US"}

[Server farm: sf2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Predictor: Hash address]{lang="EN-US"}

[  NAT: Enbaled]{lang="EN-US"}

[  SNAT pool:]{lang="EN-US"}

[  Failed action: Keep]{lang="EN-US"}

[  Active threshold: Enabled]{lang="EN-US"}

[    Lower: 80]{lang="EN-US"}

[    Upper: 90]{lang="EN-US"}

[  Slow-online: Enabled]{lang="EN-US"}

[  Standby time: 5s]{lang="EN-US"}

[  Ramp-up time: 10s]{lang="EN-US"}

[  Selected server: Enbaled]{lang="EN-US"}

[    Min server: 100]{lang="EN-US"}

[    Max server: 600]{lang="EN-US"}

[  Total real server: 2]{lang="EN-US"}

[  Active real server: 1]{lang="EN-US"}

[  Real server list:]{lang="EN-US"}

[  Name             State         Address              Port  Weight Priority]{lang="EN-US"}

[  rs2              Inactive      1.2.3.4              0     4      100]{lang="EN-US"}

[                                 1111:2222:3333:4444:]{lang="EN-US"}

[                                 5555:6666:7777:888]{lang="EN-US"}

[  rs3              Inactive      1111:2222:3333:4444: 0     4      100]{lang="EN-US"}

[                                 5555:6666:7777:888]{lang="EN-US"}

[  rs4              Inactive      \--                   0     4      100]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display server-farm]{lang="EN-US"}]{#struct_0_x7280_11703_x604898397}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1184036360}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_1856870086}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_1487741969}

[[Server farm]{lang="EN-US"}]{#struct_0_x7280_11703_943319986}

[[实服务组的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_1617191747}

[[Predictor]{lang="EN-US"}]{#struct_0_x7280_11703_x19492754}

[[实服务组的调度算法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_881957665}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RR]{lang="EN-US"}]{#struct_0_x7280_11703_2099821890}[：加权轮转算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_x7280_11703_533737949}[：随机算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[LC]{lang="EN-US"}]{#struct_0_x7280_11703_x1427295120}[：加权最小连接算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HASH(SIP)]{lang="EN-US"}]{#struct_0_x7280_11703_x1032345992}[：根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HASH(DIP)]{lang="EN-US"}]{#struct_0_x7280_11703_1340307003}[：根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号进行的哈希算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HASH(SIP-PORT)]{lang="EN-US"}]{#struct_0_x7280_11703_x225776938}[：根据目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_x1791860879}

[[实服务组中]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_937022476}[功能的状态，]{style="font-family:宋体"}[Y]{lang="EN-US"}[表示开启，]{style="font-family:宋体"}[N]{lang="EN-US"}[表示关闭]{style="font-family:宋体"}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x985291825}

[[实服务组中]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_1743591530}[功能的状态，]{style="font-family:宋体"}[Y]{lang="EN-US"}[表示开启，]{style="font-family:宋体"}[N]{lang="EN-US"}[表示关闭]{style="font-family:宋体"}

[[Total]{lang="EN-US"}]{#struct_0_x7280_11703_x772262987}

[[包含的实服务器数量]{style="font-family:宋体"}]{#struct_0_x7280_11703_x605422688}

[[Active]{lang="EN-US"}]{#struct_0_x7280_11703_334956595}

[[活跃的实服务器数量]{style="font-family:宋体"}]{#struct_0_x7280_11703_317971941}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x1967910090}

[[实服务组的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1192727591}

[[Predictor]{lang="EN-US"}]{#struct_0_x7280_11703_533672413}

[[实服务组的调度算法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1032411528}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Round robin]{lang="EN-US"}]{#struct_0_x7280_11703_1340241467}[：加权轮转算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Random]{lang="EN-US"}]{#struct_0_x7280_11703_x225842474}[：随机算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Least connection]{lang="EN-US"}]{#struct_0_x7280_11703_x1791926415}[：加权最小连接算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hash address source IP]{lang="EN-US"}]{#struct_0_x7280_11703_936956940}[：根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hash address source IP-port]{lang="EN-US"}]{#struct_0_x7280_11703_x985357361}[：根据源]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址和端口号进行的哈希算法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hash address destination IP]{lang="EN-US"}]{#struct_0_x7280_11703_1743525994}[：根据目的]{style="font-family:
  宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_x2087515348}

[[实服务组中]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_x605357152}[功能的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_1905413868}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_1099083465}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[SNAT pool]{lang="EN-US"}]{#struct_0_x7280_11703_824703714}

[[实服务组引用的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x605553760}[地址池名称]{style="font-family:宋体"}

[[Failed action]{lang="EN-US"}]{#struct_0_x7280_11703_726957229}

[[实服务组的故障处理方式，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2104876318}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[K]{lang="EN-US"}[eep]{lang="EN-US"}]{#struct_0_x7280_11703_x676955454}[：保持已有连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[R]{lang="EN-US"}[eschedule]{lang="EN-US"}]{#struct_0_x7280_11703_654925999}[：]{lang="EN-US" style="font-family:宋体"}[重定向]{style="font-family:宋体"}[连接]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reset]{lang="EN-US"}]{#struct_0_x7280_11703_x605488224}[：断开已有连接]{style="font-family:宋体"}

[[Active threshold]{lang="EN-US"}]{#struct_0_x7280_11703_1060607547}

[[实服务组可用条件的状态，包括]{style="font-family:宋体"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_2103935939}[（关闭）和]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[（开启）两种。在开启状态下还会显示：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Lower]{lang="EN-US"}]{#struct_0_x7280_11703_1480416548}[：]{style="font-family:宋体"}[最小可用百分比]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Upper]{lang="EN-US"}]{#struct_0_x7280_11703_x605160544}[：]{style="font-family:宋体"}[最大可用百分比]{lang="EN-US" style="font-family:宋体"}

[[Slow-online]{lang="EN-US"}]{#struct_0_x7280_11703_x1214844710}

[[实服务组中实服务器温暖上线功能的状态，包括]{style="font-family:宋体"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_77630818}[（关闭）和]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[（开启）两种。在开启状态下还会显示：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby time]{lang="EN-US"}]{#struct_0_x7280_11703_437630948}[：]{style="font-family:宋体"}[准备时间]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ramp-up time]{lang="EN-US"}]{#struct_0_x7280_11703_x605095008}[：]{style="font-family:宋体"}[爬升时间]{style="font-family:宋体"}

[[Selected server]{lang="EN-US"}]{#struct_0_x7280_11703_1087649668}

[[实服务组中可被调度算法调用的实服务器数量限制功能的状态，包括]{style="font-family:宋体"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_518670061}[（关闭）和]{style="font-family:宋体"}[Enabled]{lang="EN-US"}[（开启）两种。在开启状态下还会显示：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Min server]{lang="EN-US"}]{#struct_0_x7280_11703_x548772074}[：]{style="font-family:宋体"}[可被调度算法调用的]{lang="EN-US" style="font-family:宋体"}[实服务器]{style="font-family:
  宋体"}[最小数量]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Max server]{lang="EN-US"}]{#struct_0_x7280_11703_x605291616}[：]{style="font-family:宋体"}[可被调度算法调用的]{lang="EN-US" style="font-family:宋体"}[实服务器]{style="font-family:
  宋体"}[最]{lang="EN-US" style="font-family:宋体"}[大]{style="font-family:宋体"}[数量]{lang="EN-US" style="font-family:宋体"}

[[Total real server]{lang="EN-US"}]{#struct_0_x7280_11703_x90806949}

[[包含的实服务器数量]{style="font-family:宋体"}]{#struct_0_x7280_11703_x834074136}

[[Active real server]{lang="EN-US"}]{#struct_0_x7280_11703_x605226080}

[[活跃的实服务器数量]{style="font-family:宋体"}]{#struct_0_x7280_11703_1513019885}

[[Real server list]{lang="EN-US"}]{#struct_0_x7280_11703_1701328217}

[[实服务器列表]{style="font-family:宋体"}]{#struct_0_x7280_11703_335005923}

[[Name]{lang="EN-US"}]{#struct_0_x7280_11703_x604898400}

[[实服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_665556669}

[[State]{lang="EN-US"}]{#struct_0_x7280_11703_x1246344419}

[[实服务器的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1335148000}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x7280_11703_x604832864}[：可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x7280_11703_1167263917}[：不可用（由于]{style="font-family:宋体"}[配置不完全]{lang="EN-US" style="font-family:宋体"}[、未]{style="font-family:宋体"}[被引用或虚服务]{lang="EN-US" style="font-family:宋体"}[器尚未开启）]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Probe-failed]{lang="EN-US"}]{#struct_0_x7280_11703_x1231310370}[：]{style="font-family:宋体"}[健康检测失败]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Ramp]{lang="EN-US"}]{#struct_0_x7280_11703_x605422687}[：温暖上线的爬升阶段]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Shutdown]{lang="EN-US"}]{#struct_0_x7280_11703_333973555}[：关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standby]{lang="EN-US"}]{#struct_0_x7280_11703_x1563376198}[：温暖上线的]{style="font-family:宋体"}[准备阶段]{lang="EN-US" style="font-family:宋体"}

[[Address]{lang="EN-US"}]{#struct_0_x7280_11703_x605357151}

[[实服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_1905610476}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x7280_11703_1826890657}

[[实服务器的端口号]{style="font-family:宋体"}]{#struct_0_x7280_11703_x605553759}

[[Weight]{lang="EN-US"}]{#struct_0_x7280_11703_726498474}

[[实服务器的权值]{style="font-family:宋体"}]{#struct_0_x7280_11703_x268431977}

[[Priority]{lang="EN-US"}]{#struct_0_x7280_11703_x605488223}

[[实服务器的调用优先级]{style="font-family:宋体"}]{#struct_0_x7280_11703_1060935227}

[]{#_Toc334536543}[]{#_Toc329869282}[[ ]{lang="EN-US"}]{#_Toc329242052}

::: {#-1661117443 .myid}
[]{#_Toc404796578}[]{#struct_0_x7280_11703_x1498766750}[]{#_Toc380504936}[]{#_Toc364842565}[]{#_Toc362006260}

**负载均衡 \-- 负载均衡配置命令 \-- display sticky**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **sticky**]{lang="EN-US"}]{#struct_0_x7280_11703_x1498832286}[命令用来显示持续性表项的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498373534}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1635915541}

[**[display]{lang="EN-US"}**[ **sticky** \[ **virtual-server** *virtual-server-name* \[ **class** *class-name* \| **default-class** \| **default-server-farm** \] \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1498439070}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x685057208}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **sticky** \[ **virtual-server** *virtual-server-name* \[ **class** *class-name* \| **default-class** \| **default-server-farm** \] \] \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1498504606}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7280_11703_x1498570142}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **sticky** \[ **virtual-server** *virtual-server-name* \[ **class** *class-name* \| **default-class** \| **default-server-farm** \] \] \[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1973331089}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498111390}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_105769791}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498176926}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x75443667}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1498635675}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498701211}

[**[virtual-server]{lang="EN-US"}**[ *virtual-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1040627734}[：显示指定虚服务器的信息。]{style="font-family:宋体"}*[virtual-server-name]{lang="EN-US"}*[为虚服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的信息。]{style="font-family:宋体"}

[**[class]{lang="EN-US"}**[ *class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1498766747}[：]{style="font-family:宋体"}[显示指定负载均衡类的信息。]{style="font-family:宋体"}*[class-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[负载均衡类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[default-class]{lang="EN-US"}**]{#struct_0_x7280_11703_1102840121}[：显示默认负载均衡动作的信息。]{style="font-family:宋体"}

[**[default-server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_x1498832283}[：显示默认的实服务组的信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1498373531}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x876400654}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_936825868}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1498439067}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x985488433}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1237191557}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1498504603}[显示所有虚服务的持续性表项信息。]{style="font-family:宋体"}

[[\<Sysname\> display sticky]{lang="EN-US"}]{#struct_0_x7280_11703_x1498570139}

[Virtual server name: vs1]{lang="EN-US"}

[  Sticky zone type: Class]{lang="EN-US"}

[  Class name: lbc1]{lang="EN-US"}

[  Sticky group name: sg1]{lang="EN-US"}

[  Sticky method: Source IP and port]{lang="EN-US"}

[  Timeout: 60]{lang="EN-US"}

[Sticky entry                     Real server           Expired time Count]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[192.168.6.206/1566               192.168.6.206/0       53           0]{lang="EN-US"}

[192.168.6.206/1567               192.168.6.206/0       56           0]{lang="EN-US"}

[Virtual server name: vs2]{lang="EN-US"}

[  Sticky zone type: Default class]{lang="EN-US"}

[  Class name:]{lang="EN-US"}

[  Sticky group name: sg2]{lang="EN-US"}

[  Sticky method: HTTP URL]{lang="EN-US"}

[  Timeout: 60]{lang="EN-US"}

[Sticky entry                     Real server           Expired time Count]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[e251273eb74a8ee3f661a7af0915af1  192.168.6.206/0       54           0]{lang="EN-US"}

[                                 2000::100/0]{lang="EN-US"}

[Virtual server name: vs3]{lang="EN-US"}

[  Sticky zone type: Default sever farm]{lang="EN-US"}

[  Class name:]{lang="EN-US"}

[  Sticky group name: sg3]{lang="EN-US"}

[  Sticky method: Both IP and port]{lang="EN-US"}

[  Timeout: 60]{lang="EN-US"}

[Sticky entry                     Real server           Expired time Count]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[192.168.6.206/2606               192.168.6.206/0       57           0]{lang="EN-US"}

[192.168.6.40/80]{lang="EN-US"}

[192.168.6.206/2605               192.168.6.206/0       55           0]{lang="EN-US"}

[192.168.6.40/80]{lang="EN-US"}

[192.168.6.206/2604               192.168.6.206/0       52           0]{lang="EN-US"}

[192.168.6.40/80]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display sticky]{lang="EN-US"}]{#struct_0_x7280_11703_x1498111387}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x904313977}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498176923}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1498635676}

[[Virtual server name]{lang="EN-US"}]{#struct_0_x7280_11703_x1498701212}

[[虚服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498766748}

[[Sticky zone type]{lang="EN-US"}]{#struct_0_x7280_11703_x1498832284}

[[持续性表项的来源，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498439068}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Class]{lang="EN-US"}]{#struct_0_x7280_11703_x1498504604}[：由虚服务所引用策略中的类和动作生成]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default class]{lang="EN-US"}]{#struct_0_x7280_11703_x1498570140}[：由虚服务]{lang="EN-US" style="font-family:宋体"}[所引用策略]{style="font-family:宋体"}[中的]{lang="EN-US" style="font-family:宋体"}[默认动作]{style="font-family:宋体"}[生成]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Default server farm]{lang="EN-US"}]{#struct_0_x7280_11703_x1498111388}[：由虚服务下]{lang="EN-US" style="font-family:
  宋体"}[默认]{lang="EN-US" style="font-family:宋体"}[的主用]{style="font-family:宋体"}[或]{lang="EN-US" style="font-family:宋体"}[备用]{style="font-family:宋体"}[实服务组生成]{lang="EN-US" style="font-family:宋体"}

[[Class name]{lang="EN-US"}]{#struct_0_x7280_11703_x1498176924}

[[如果该持续性由类和动作生成，显示对应负载均衡类的名称；否则显示为空]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498635681}

[[Sticky group name]{lang="EN-US"}]{#struct_0_x7280_11703_x1498701217}

[[生成该持续性表项的持续性组名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498766753}

[[Sticky method]{lang="EN-US"}]{#struct_0_x7280_11703_x1498832289}

[[该持续性表项对应的持续性方法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1498439073}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IP]{lang="EN-US"}]{#struct_0_x7280_11703_x1498504609}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x1498570145}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498111393}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋源端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498176929}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋源端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IP]{lang="EN-US"}]{#struct_0_x7280_11703_x1498635682}[：目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x1498701218}[：目的]{style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498766754}[：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498373538}[：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址＋]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IP]{lang="EN-US"}]{#struct_0_x7280_11703_x1498439074}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x1498504610}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址＋目的]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498570146}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋源端口＋目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_x1498111394}[：]{style="font-family:宋体"}[源]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址＋源端口＋目的]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[地址＋目的端口]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP URL]{lang="EN-US"}]{#struct_0_x7280_11703_x1498176930}[：]{style="font-family:宋体"}[基于]{lang="EN-US" style="font-family:宋体"}[HTTP URL]{lang="FR"}[的]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP header name]{lang="EN-US"}]{#struct_0_x7280_11703_67448264}[：]{style="font-family:宋体"}[基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[首部]{lang="EN-US" style="font-family:宋体"}[名称的]{lang="EN-US" style="font-family:
  宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP version]{lang="EN-US"}]{#struct_0_x7280_11703_67317192}[：]{style="font-family:宋体"}[基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[版本]{lang="EN-US" style="font-family:宋体"}[的]{lang="EN-US" style="font-family:
  宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP host]{lang="EN-US"}]{#struct_0_x7280_11703_67251656}[：]{style="font-family:宋体"}[基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="FR"}[主机]{lang="EN-US" style="font-family:宋体"}[的]{lang="EN-US" style="font-family:
  宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP method]{lang="EN-US"}]{#struct_0_x7280_11703_67710408}[：]{style="font-family:宋体"}[基于]{lang="EN-US" style="font-family:宋体"}[HTTP ]{lang="FR"}[Request-Method]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP content]{lang="EN-US"}]{#struct_0_x7280_11703_67644872}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP cookie]{lang="EN-US"}]{#struct_0_x7280_11703_67579336}[：]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Payload]{lang="EN-US"}]{#struct_0_x7280_11703_67513800}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷]{lang="EN-US" style="font-family:宋体"}[持续性方法]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL session ID]{lang="EN-US"}]{#struct_0_x7280_11703_x2061023427}[：]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[持续性方法为基于]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[会话]{lang="EN-US" style="font-family:宋体"}[ID]{lang="EN-US"}

[[Timeout]{lang="EN-US"}]{#struct_0_x7280_11703_67907016}

[[持续性表项的超时时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x7280_11703_67448263}

[[Sticky entry]{lang="EN-US"}]{#struct_0_x7280_11703_67382727}

[[持续性表项对应的]{style="font-family:宋体"}[Key]{lang="EN-US"}]{#struct_0_x7280_11703_67317191}[值]{style="font-family:宋体"}

[[Real server]{lang="EN-US"}]{#struct_0_x7280_11703_67251655}

[[实服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7280_11703_67710407}[地址和端口号。对于七层持续性方法，如果实服务器同时配置了]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，则不论该持续性表项由哪种连接生成，都会同时显示这两个地址]{style="font-family:宋体"}

[[Expired time]{lang="EN-US"}]{#struct_0_x7280_11703_67644871}

[[持续性表项的老化剩余时间，如果引用计数不为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_67579335}[，则显示为配置值]{style="font-family:宋体"}

[[Count]{lang="EN-US"}]{#struct_0_x7280_11703_67972551}

[[持续性表项的引用计数]{style="font-family:宋体"}]{#struct_0_x7280_11703_67907015}

[ ]{lang="EN-US"}

::: {#-1867804460 .myid}
[]{#_Toc404796579}[]{#struct_0_x7280_11703_287523455}

**负载均衡 \-- 负载均衡配置命令 \-- display sticky-group**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **sticky-group**]{lang="EN-US"}]{#struct_0_x7280_11703_x1815807315}[命令用来显示持续性组的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2011092500}

[**[display]{lang="EN-US"}**[ **sticky-group** \[ **name** *group-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1552027502}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x377490221}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_742392449}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_287523456}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1815807318}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x1880590269}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1800677585}

[**[name]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x990396118}[：显示指定持续性组的信息。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[为持续性组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有持续性组的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1471279365}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_287523457}[显示所有持续性组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display sticky-group]{lang="EN-US"}]{#struct_0_x7280_11703_x1815807317}

[Sticky group: sg1]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Timeout: 60]{lang="EN-US"}

[  Sticky group type: Address-port]{lang="EN-US"}

[    Method: Both IP and port]{lang="EN-US"}

[      Mask: 32]{lang="EN-US"}

[ ]{lang="EN-US"}

[Sticky group: sg2]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Timeout: 60]{lang="EN-US"}

[  Sticky group type: HTTP header]{lang="EN-US"}

[    Method: HTTP header name]{lang="EN-US"}

[      Name: accept-encoding]{lang="EN-US"}

[      Offset: 4]{lang="EN-US"}

[      Start: gzip]{lang="EN-US"}

[      Length: 10]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display sticky-group]{lang="EN-US"}]{#struct_0_x7280_11703_x1121075382}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x1610832125}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1668791688}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1668791687}

[[Sticky group]{lang="EN-US"}]{#struct_0_x7280_11703_x1668791686}

[[持续性组的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1668791685}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x1668791684}

[[持续性组的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1668791683}

[[Timeout]{lang="EN-US"}]{#struct_0_x7280_11703_x1668791682}

[[持续性表项的超时时间，单位为秒]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1668791681}

[[Sticky group type]{lang="EN-US"}]{#struct_0_x7280_11703_x1668791680}

[[持续性组的类型，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1668791679}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Address-port]{lang="EN-US"}]{#struct_0_x7280_11703_669860472}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[地址端口]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP content]{lang="EN-US"}]{#struct_0_x7280_11703_669860473}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP cookie]{lang="EN-US"}]{#struct_0_x7280_11703_669860475}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP header]{lang="EN-US"}]{#struct_0_x7280_11703_669860476}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部]{lang="EN-US" style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Payload]{lang="EN-US"}]{#struct_0_x7280_11703_669860477}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷类型]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_669860478}[：]{lang="EN-US" style="font-family:宋体"}[表示]{style="font-family:宋体"}[SSL]{lang="EN-US"}[类型]{style="font-family:宋体"}

[[各类型持续性组的具体内容，请参见]{style="font-family:宋体"}]{#struct_0_x7280_11703_669860479}[[[[表]{lang="EN-US"}]{lang="EN-US" style="font-family:宋体"}1-12]{lang="EN-US"}](?-1867804460#_Ref393378952)

[ ]{lang="EN-US"}

[]{#struct_0_x7280_11703_x789902236}[[表1-12 ]{lang="EN-US"}[各类型持续性组的具体内容]{style="font-family:
黑体"}]{#_Ref393378952}

[]{#table_struct_0_x1623332061}[[持续性组类型]{style="font-family:黑体"}]{#struct_0_x7280_11703_669860480}

[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_669860481}

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_1859338872}

[[Address-port]{lang="EN-US"}]{#struct_0_x7280_11703_1859338873}

[[Method]{lang="EN-US"}]{#struct_0_x7280_11703_1859338874}

[[持续性方法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1859338875}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IP]{lang="EN-US"}]{#struct_0_x7280_11703_1859338876}[：源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_1859338877}[：源]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_1859338878}[：源]{lang="EN-US" style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[地址＋源端口持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Source IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_1859338879}[：源]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址＋源端口持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IP]{lang="EN-US"}]{#struct_0_x7280_11703_1859338880}[：目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_1859338881}[：目的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_x96976264}[：目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[端口持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Destination IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_x96976263}[：目的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋]{lang="EN-US" style="font-family:宋体"}[目的]{style="font-family:宋体"}[端口持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IP]{lang="EN-US"}]{#struct_0_x7280_11703_x96976262}[：源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x96976261}[：源]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋目的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IP and port]{lang="EN-US"}]{#struct_0_x7280_11703_x96976260}[：源]{lang="EN-US" style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[地址＋源端口＋目的]{lang="EN-US" style="font-family:
  宋体"}[IPv4]{lang="EN-US"}[地址＋目的端口持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Both IPv6 and port]{lang="EN-US"}]{#struct_0_x7280_11703_x96976258}[：源]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址＋源端口＋目的]{lang="EN-US" style="font-family:
  宋体"}[IPv6]{lang="EN-US"}[地址＋目的端口持续性方法]{lang="EN-US" style="font-family:宋体"}

[[Mask]{lang="EN-US"}]{#struct_0_x7280_11703_x96976257}

[[持续性方法的掩码长度，只有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x96976256}[持续性方法才会显示本字段]{style="font-family:宋体"}

[[Prefix]{lang="EN-US"}]{#struct_0_x7280_11703_x96976255}

[[持续性方法的前缀长度，只有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291400}[持续性方法才会显示本字段]{style="font-family:宋体"}

[[HTTP content]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291399}

[[Offset]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291398}

[[实体基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291397}[报文起始位置的偏移量]{style="font-family:宋体"}

[[Start]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291396}

[[实体开始标记的正则表达式]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2053291394}

[[End]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291393}

[[实体结束标记的正则表达式，不会与]{style="font-family:宋体"}[Length]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291392}[字段同时显示]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x7280_11703_x2053291391}

[[实体的长度，不会与]{style="font-family:宋体"}[End]{lang="EN-US"}]{#struct_0_x7280_11703_285360760}[字段同时显示]{style="font-family:宋体"}

[[HTTP cookie]{lang="EN-US"}]{#struct_0_x7280_11703_285360761}

[[Method]{lang="EN-US"}]{#struct_0_x7280_11703_285360762}

[[持续性方法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_285360763}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP cookie insert]{lang="EN-US"}]{#struct_0_x7280_11703_285360764}[：]{lang="EN-US" style="font-family:
  宋体"}[Cookie]{lang="EN-US"}[截取持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP cookie rewrite]{lang="EN-US"}]{#struct_0_x7280_11703_285360765}[：]{lang="EN-US" style="font-family:
  宋体"}[Cookie]{lang="EN-US"}[重写持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP cookie get]{lang="EN-US"}]{#struct_0_x7280_11703_285360766}[：]{lang="EN-US" style="font-family:
  宋体"}[Cookie]{lang="EN-US"}[插入持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[只有指定了]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_285360767}[持续性方法才会显示本字段]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x7280_11703_285360768}

[[HTTP cookie]{lang="EN-US"}]{#struct_0_x7280_11703_285360769}[的名称。只有指定了]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[持续性方法才会显示本字段]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954375}

[[Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954374}[基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量。只有指定了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入持续性方法才会显示本字段]{style="font-family:宋体"}

[[Start]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954373}

[[Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954372}[开始标记的正则表达式。只有指定了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入持续性方法才会显示本字段]{style="font-family:宋体"}

[[End]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954371}

[[Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954370}[结束标记的正则表达式，不会与]{style="font-family:宋体"}[Length]{lang="EN-US"}[字段同时显示。只有指定了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入持续性方法才会显示本字段]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954369}

[[Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_x1670954368}[的长度，不会与]{style="font-family:宋体"}[End]{lang="EN-US"}[字段同时显示。只有指定了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入持续性方法才会显示本字段]{style="font-family:宋体"}

[[Cookie secondary name]{lang="EN-US"}]{#struct_0_x7280_11703_667697784}

[[需在]{style="font-family:宋体"}[URI]{lang="EN-US"}]{#struct_0_x7280_11703_667697785}[中查找的]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[名称。只有指定了]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入持续性方法才会显示本字段]{style="font-family:宋体"}

[[Check all packets]{lang="EN-US"}]{#struct_0_x7280_11703_667697786}

[[是否开启检查所有报文的功能，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_667697787}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_667697788}[：关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_667697789}[：开启]{lang="EN-US" style="font-family:宋体"}

[[HTTP header]{lang="EN-US"}]{#struct_0_x7280_11703_667697790}

[[Method]{lang="EN-US"}]{#struct_0_x7280_11703_667697791}

[[持续性方法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_667697792}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP host]{lang="EN-US"}]{#struct_0_x7280_11703_667697793}[：基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[主机的持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP header name]{lang="EN-US"}]{#struct_0_x7280_11703_1857176184}[：基于]{lang="EN-US" style="font-family:
  宋体"}[HTTP]{lang="EN-US"}[首部名称的持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP method]{lang="EN-US"}]{#struct_0_x7280_11703_1857176185}[：基于]{lang="EN-US" style="font-family:宋体"}[HTTP Request-Method]{lang="EN-US"}[的持续性方法]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP URL]{lang="EN-US"}]{#struct_0_x7280_11703_1857176186}[：基于]{lang="EN-US" style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[的持续性方法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HTTP version]{lang="EN-US"}]{#struct_0_x7280_11703_1857176187}[：基于]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[版本的持续性方法]{lang="EN-US" style="font-family:宋体"}

[[只有指定了]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1857176188}[首部持续性方法才会显示本字段]{style="font-family:宋体"}

[[Name]{lang="EN-US"}]{#struct_0_x7280_11703_1857176189}

[[HTTP]{lang="FR"}]{#struct_0_x7280_11703_1857176190}[首部的]{style="font-family:宋体"}[名称。只有指定了基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部名称的持续性方法才会显示本字段]{style="font-family:宋体"}

[[Offset]{lang="EN-US"}]{#struct_0_x7280_11703_1857176191}

[[HTTP]{lang="FR"}]{#struct_0_x7280_11703_1857176192}[首部基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文起始位置的偏移量。只有指定了基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[主机或]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[的持续性方法才会显示本字段]{style="font-family:宋体"}

[[Start]{lang="EN-US"}]{#struct_0_x7280_11703_x99138952}

[[HTTP]{lang="FR"}]{#struct_0_x7280_11703_x99138951}[首部开始标记的正则表达式。只有指定了基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[主机或]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[的持续性方法才会显示本字段]{style="font-family:宋体"}

[[End]{lang="EN-US"}]{#struct_0_x7280_11703_x99138950}

[[HTTP]{lang="FR"}]{#struct_0_x7280_11703_x99138949}[首部结束标记的正则表达式，不会与]{style="font-family:宋体"}[Length]{lang="EN-US"}[字段同时显示。只有指定了基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[主机或]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[的持续性方法才会显示本字段]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x7280_11703_x99138948}

[[HTTP]{lang="FR"}]{#struct_0_x7280_11703_x99138947}[首部的长度，不会与]{style="font-family:宋体"}[End]{lang="EN-US"}[字段同时显示。只有指定了基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[主机或]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[的持续性方法才会显示本字段]{style="font-family:宋体"}

[[Payload]{lang="EN-US"}]{#struct_0_x7280_11703_x99138946}

[[Offset]{lang="EN-US"}]{#struct_0_x7280_11703_x99138945}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x99138944}[载荷基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量]{style="font-family:宋体"}

[[Start]{lang="EN-US"}]{#struct_0_x7280_11703_x99138943}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454088}[载荷开始标记的正则表达式]{style="font-family:宋体"}

[[End]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454087}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454086}[载荷结束标记的正则表达式，不会与]{style="font-family:宋体"}[Length]{lang="EN-US"}[字段同时显示]{style="font-family:宋体"}

[[Length]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454084}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454083}[载荷的长度，不会与]{style="font-family:宋体"}[End]{lang="EN-US"}[字段同时显示]{style="font-family:宋体"}

[[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454082}

[[Method]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454081}

[[持续性方法，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2055454080}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SSL session ID]{lang="EN-US"}]{#struct_0_x7280_11703_x2055454079}[：基于]{lang="EN-US" style="font-family:宋体"}[SSL session ID]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[持续性方法]{lang="EN-US" style="font-family:宋体"}

[[只有指定了基于]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_283198072}[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[持续性方法才会显示本字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1457518584 .myid}
[]{#_Toc404796580}[]{#struct_0_x7280_11703_x1021404758}

**负载均衡 \-- 负载均衡配置命令 \-- display virtual-server**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **virtual-server**]{lang="EN-US"}]{#struct_0_x7280_11703_748765923}[命令用来显示虚服务器的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1013656714}

[**[display]{lang="EN-US"}**[ **virtual-server** \[ **brief** \| **name** *virtual-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1006366232}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1790184774}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x605160543}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1215303462}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1991033848}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1031734560}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1882342190}

[**[brief]{lang="EN-US"}**]{#struct_0_x7280_11703_x438392540}[：显示虚服务器的简要信息。如果未指定本参数，将显示虚服务器的详细信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *virtual-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_14601068}[：显示指定虚服务器的信息。]{style="font-family:宋体"}*[virtual-server-name]{lang="EN-US"}*[为虚服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_155516850}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x189740599}[显示所有虚服务器的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display virtual-server brief]{lang="EN-US"}]{#struct_0_x7280_11703_x605095007}

[Virtual server   State    Type      VPN instance     Virtual address     Port]{lang="EN-US"}

[vs1              Inactive IP        vpn1             192.168.21.148/32   80]{lang="EN-US"}

[                                                     1111:2222:3333:4444]{lang="EN-US"}

[                                                     :5555:6666:7777:888]{lang="EN-US"}

[                                                     8/128]{lang="EN-US"}

[vs2              Active   HTTP                       61.159.4.100/32     8080]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1087846276}[显示虚服务器]{style="font-family:宋体"}[vs]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display virtual-server name vs]{lang="EN-US"}]{#struct_0_x7280_11703_x605291615}

[Virtual server: vs]{lang="EN-US"}

[  Description: Virtual server VS]{lang="EN-US"}

[  Type: HTTP]{lang="EN-US"}

[  State: Active]{lang="EN-US"}

[  VPN instance: vpn1]{lang="EN-US"}

[  Virtual IPv4 address: 1.1.1.1/32]{lang="EN-US"}

[  Virtual IPv6 address: 1001::1/128]{lang="EN-US"}

[  Port: 8080]{lang="EN-US"}

[  Default server farm: sf (in use)]{lang="EN-US"}

[  Backup server farm: sfb]{lang="EN-US"}

[  Sticky: sg3]{lang="EN-US"}

[  LB policy: lbp2]{lang="EN-US"}

[  HTTP parameter profile: pp1]{lang="EN-US"}

[  UDP per-packet: Enabled]{lang="EN-US"}

[  Connection limit: 10000]{lang="EN-US"}

[  Rate limit:]{lang="EN-US"}

[    Connections: 10000]{lang="EN-US"}

[    Bandwidth: 10000 Kbytes/s]{lang="EN-US"}

[    Inbound bandwidth: 5000 Kbytes/s]{lang="EN-US"}

[    Outbound bandwidth: 5000 Kbytes/s]{lang="EN-US"}

[  SSL server policy: ssl-server]{lang="EN-US"}

[  SSL client policy: ssl-client]{lang="EN-US"}

[  Redirect relocation:]{lang="EN-US"}

[  Redirect return-code: 302]{lang="EN-US"}

[  Sticky synchronization: Disabled]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display virtual-server]{lang="EN-US"}]{#struct_0_x7280_11703_x90610341}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1182671080}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1417511867}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_692013238}

[[Virtual server]{lang="EN-US"}]{#struct_0_x7280_11703_x1712652488}

[[虚服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x580359037}

[[State]{lang="EN-US"}]{#struct_0_x7280_11703_x406186904}

[[虚服务器的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x605226079}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x7280_11703_1513478640}[：]{lang="EN-US" style="font-family:宋体"}[可用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x7280_11703_2060233076}[：]{lang="EN-US" style="font-family:宋体"}[不可用（由于配置不完全或虚服务器尚未开启）]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_x7280_11703_x1801935659}

[[虚服务器的类型，包括]{style="font-family:宋体"}[Fast HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1969046086}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}

[[VPN instance]{lang="EN-US"}]{#struct_0_x7280_11703_x110593618}

[[虚服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x7280_11703_x218139474}[实例名称]{style="font-family:宋体"}

[[Virtual address]{lang="EN-US"}]{#struct_0_x7280_11703_x91484008}

[[虚服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x604898399}[地址和掩码]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_x7280_11703_1856739014}

[[虚服务器的端口号]{style="font-family:宋体"}]{#struct_0_x7280_11703_x877701906}

[[Description]{lang="EN-US"}]{#struct_0_x7280_11703_x1543729657}

[[虚服务器的描述信息]{style="font-family:宋体"}]{#struct_0_x7280_11703_1870980230}

[[Virtual IPv4 address]{lang="EN-US"}]{#struct_0_x7280_11703_x604832863}

[[虚服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_1167198381}[地址和掩码]{style="font-family:宋体"}

[[Virtual IPv6 address]{lang="EN-US"}]{#struct_0_x7280_11703_1179168461}

[[虚服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_762023954}[地址和前缀]{style="font-family:宋体"}

[[Default server farm]{lang="EN-US"}]{#struct_0_x7280_11703_x888523890}

[[默认的主用实服务组名称，]{style="font-family:宋体"}[(in use)]{lang="EN-US"}]{#struct_0_x7280_11703_960661257}[表示该实服务组正被使用]{style="font-family:宋体"}

[[Backup server farm]{lang="EN-US"}]{#struct_0_x7280_11703_1769232404}

[[默认的备用实服务组名称，]{style="font-family:宋体"}[(in use)]{lang="EN-US"}]{#struct_0_x7280_11703_542719299}[表示该实服务组正被使用]{style="font-family:宋体"}

[[Sticky]{lang="EN-US"}]{#struct_0_x7280_11703_809307132}

[[默认的持续性组名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1099301479}

[[LB policy]{lang="EN-US"}]{#struct_0_x7280_11703_960726793}

[[虚服务器引用的负载均衡策略]{style="font-family:宋体"}]{#struct_0_x7280_11703_x589062269}

[[HTTP parameter profile]{lang="EN-US"}]{#struct_0_x7280_11703_67644868}

[[虚服务器引用的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_67579332}[类型参数模板，只有配置了]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的参数模板才会显示本字段]{style="font-family:宋体"}

[[IP parameter profile]{lang="EN-US"}]{#struct_0_x7280_11703_67513796}

[[虚服务器引用的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7280_11703_67907012}[类型参数模板，只有配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的参数模板才会显示本字段]{style="font-family:宋体"}

[[TCP parameter profile]{lang="EN-US"}]{#struct_0_x7280_11703_67448259}

[[虚服务器引用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x7280_11703_67382723}[类型参数模板，只有配置了]{style="font-family:宋体"}[TCP]{lang="EN-US"}[类型的参数模板才会显示本字段]{style="font-family:宋体"}

[[UDP per-packet]{lang="EN-US"}]{#struct_0_x7280_11703_960530185}

[[虚服务器]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_1542305458}[强制负载均衡功能的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_x1698437590}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_x636679707}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_960595721}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Connection limit]{lang="EN-US"}]{#struct_0_x7280_11703_332636330}

[[虚服务器所允许的最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_1941932238}

[[Rate limit]{lang="EN-US"}]{#struct_0_x7280_11703_x1673117062}

[[虚服务器的速率限制]{style="font-family:宋体"}]{#struct_0_x7280_11703_1518163680}

[[Connections]{lang="EN-US"}]{#struct_0_x7280_11703_x813999752}

[[虚服务器所允许的每秒最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_960923401}

[[Bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_x754248672}

[[虚服务器所允许的最大总带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_821466809}[秒]{style="font-family:宋体"}

[[Inbound bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_x2060564675}

[[虚服务器所允许的最大入带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x1208981179}[秒]{style="font-family:宋体"}

[[Outbound bandwidth]{lang="EN-US"}]{#struct_0_x7280_11703_x1184443343}

[[虚服务器所允许的最大出带宽，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x171224448}[秒]{style="font-family:宋体"}

[[SSL server policy]{lang="EN-US"}]{#struct_0_x7280_11703_x2060499139}

[[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_x1716689047}[服务器端策略的名称，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[SSL client policy]{lang="EN-US"}]{#struct_0_x7280_11703_1518477087}

[[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_105281859}[客户端策略的名称，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Redirect relocation]{lang="EN-US"}]{#struct_0_x7280_11703_67579331}

[[重定向的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_x7280_11703_67513795}[，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Redirect return-code]{lang="EN-US"}]{#struct_0_x7280_11703_67907011}

[[重定向报文中的状态码，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x335836263}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Connection synchronization]{lang="EN-US"}]{#struct_0_x7280_11703_x917097136}

[[虚服务器会话扩展信息备份功能的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1253489067}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_x109032520}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_648986805}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x741296614}[类型的虚服务器不会显示本字段]{style="font-family:宋体"}

[[集中式设备不支持本字段，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x7280_11703_x528657142}

[[Sticky synchronization]{lang="EN-US"}]{#struct_0_x7280_11703_x309424894}

[[虚服务器持续性表项备份功能的状态，包括：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1723666190}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_x7280_11703_1457306866}[：]{lang="EN-US" style="font-family:宋体"}[关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_x7280_11703_x463705712}[：]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}

[[集中式设备不支持本字段，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x7280_11703_x157582249}

[]{#_Toc334536544}[]{#_Toc329869283}[[ ]{lang="EN-US"}]{#_Toc329242053}

::: {#-918539515 .myid}
[]{#_Toc404796581}[]{#struct_0_x7280_11703_1500103501}

**负载均衡 \-- 负载均衡配置命令 \-- display virtual-server statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **virtual-server** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_2099425071}[命令用来]{style="font-family:宋体"}[显示虚服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960988937}

[[集中式设备：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1974838285}

[**[display]{lang="EN-US"}**[ **virtual-server** **statistics** \[ **name** *virtual-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1469383183}

[[分布式设备－独立运行模式]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1647097437}[集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **virtual-server** **statistics** \[ **name** *virtual-server-name* \]]{lang="EN-US"}[ \[ **slot** *slot-number* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1492714287}

[[分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}]{#struct_0_x7280_11703_100943847}[模式：]{style="font-family:宋体"}

[**[display]{lang="EN-US"}**[ **virtual-server** **statistics** \[ **name** *virtual-server-name* \]]{lang="EN-US"}[ \[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1226229819}**[chassis]{lang="SV"}**[ *chassis-number*]{lang="SV"}[ ]{lang="SV"}**[slot]{lang="EN-US"}**[ *slot-number* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1392332180}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_98201490}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960792329}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1798622774}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x194023633}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_133678961}

[**[name]{lang="EN-US"}**[ *virtual-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x319077128}[：显示指定虚服务器的统计信息。]{style="font-family:宋体"}*[virtual-server-name]{lang="EN-US"}*[为虚服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将显示所有虚服务器的统计信息。]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1315879338}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－独立运行模式）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x402036373}*[slot-number]{lang="EN-US"}*[：显示指定成员设备上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号。如果未指定本参数，将显示所有成员设备上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[slot]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_935408093}*[slot-number]{lang="EN-US"}*[：显示指定成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[的虚拟槽位号。如果未指定本参数，将显示所有成员设备]{style="font-family:宋体"}[/PEX]{lang="EN-US"}[上的信息。（集中式]{style="font-family:宋体"}[IRF]{lang="EN-US"}[设备）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x980756047}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定成员设备指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（不支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[**[chassis]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x630675848}*[chassis-number]{lang="EN-US"}*[ **slot** ]{lang="EN-US"}*[slot-number]{lang="EN-US"}*[：显示指定单板上的信息，]{style="font-family:宋体"}*[chassis-number]{lang="EN-US"}*[表示设备在]{style="font-family:宋体"}[IRF]{lang="EN-US"}[中的成员编号或者]{style="font-family:宋体"}[PEX]{lang="EN-US"}[对应的虚拟框号，]{style="font-family:宋体"}*[slot-number]{lang="EN-US"}*[表示单板或]{style="font-family:宋体"}[PEX]{lang="EN-US"}[所在的槽位号。如果未指定本参数，将显示所有单板上的信息。（分布式设备－]{style="font-family:宋体"}[IRF]{lang="EN-US"}[模式）（支持]{style="font-family:宋体"}[IRF3]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x842453441}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_960857865}[显示虚服务器]{style="font-family:宋体"}[vs]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display virtual-server statistics name vs]{lang="EN-US"}]{#struct_0_x7280_11703_x351017407}

[Virtual server: vs]{lang="EN-US"}

[  Total connections: 979]{lang="EN-US"}

[  Active connections: 618]{lang="EN-US"}

[  Max connections: 661]{lang="EN-US"}

[  Connections per second: 146]{lang="EN-US"}

[  Max connections per second: 156]{lang="EN-US"}

[  ]{lang="EN-US"}[Client input: 333332 bytes]{lang="EN-US"}

[  ]{lang="EN-US"}[Client output: 472054 bytes]{lang="EN-US"}

[  Throughput: 4088 bytes/s]{lang="EN-US"}

[  Inbound throughput: 1214 bytes/s]{lang="EN-US"}

[  Outbound throughput: 2874 bytes/s]{lang="EN-US"}

[  Max throughput: 4368 bytes/s]{lang="EN-US"}

[  Max inbound throughput: 1214 bytes/s]{lang="EN-US"}

[  Max outbound throughput: 3154 bytes/s]{lang="EN-US"}

[  Received packets: 979]{lang="EN-US"}

[  Sent packets: 0]{lang="EN-US"}

[  Dropped packets: 0]{lang="EN-US"}

[  Received requests: 0]{lang="EN-US"}

[  Dropped requests: 0]{lang="EN-US"}

[  Sent responses: 0]{lang="EN-US"}

[  Dropped responses: 0]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display virtual-server staistics]{lang="EN-US"}]{#struct_0_x7280_11703_x2068463256}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1205854792}[[字段]{style="font-family:黑体"}]{#struct_0_x7280_11703_1655824204}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x7280_11703_961185545}

[[Virtual server]{lang="EN-US"}]{#struct_0_x7280_11703_x45973110}

[[虚服务器的名称]{style="font-family:宋体"}]{#struct_0_x7280_11703_1315929617}

[[Total ]{lang="EN-US"}]{#struct_0_x7280_11703_495268924}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[总连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1222557427}

[[Active ]{lang="EN-US"}]{#struct_0_x7280_11703_x197507369}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[当前活动的连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_961251081}

[[Max ]{lang="EN-US"}]{#struct_0_x7280_11703_x932240728}[c]{lang="EN-US"}[onnections]{lang="EN-US"}

[[最大连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1316101649}

[[Connections per second]{lang="EN-US"}]{#struct_0_x7280_11703_1576175083}

[[每秒连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x177237328}

[[Max ]{lang="EN-US"}]{#struct_0_x7280_11703_x674936606}[c]{lang="EN-US"}[onnection]{lang="EN-US"}[s per second]{lang="EN-US"}

[[最大每秒连接数]{style="font-family:宋体"}]{#struct_0_x7280_11703_960661258}

[[Client input]{lang="EN-US"}]{#struct_0_x7280_11703_x335836264}

[[从客户端收到的流量，单位为字节]{style="font-family:宋体"}]{#struct_0_x7280_11703_x335967336}

[[Client output]{lang="EN-US"}]{#struct_0_x7280_11703_x336032872}

[[向客户端发出的流量，单位为字节]{style="font-family:宋体"}]{#struct_0_x7280_11703_x335639656}

[[T]{lang="EN-US"}[hroughput]{lang="EN-US"}]{#struct_0_x7280_11703_x335705192}

[[报文的总吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x335311976}[秒]{style="font-family:宋体"}

[[Inbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x2060826826}

[[报文的入吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_1454381334}[秒]{style="font-family:宋体"}

[[Outbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x352472932}

[[报文的出吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x246281900}[秒]{style="font-family:宋体"}

[[Max throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x335377512}

[[报文的最大总吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x335836261}[秒]{style="font-family:宋体"}

[[Max inbound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x2060761290}

[[报文的最大入吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x1562631614}[秒]{style="font-family:宋体"}

[[Max oubound throughput]{lang="EN-US"}]{#struct_0_x7280_11703_x1413342776}

[[报文的最大出吞吐量，单位为字节]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x7280_11703_x2060695754}[秒]{style="font-family:宋体"}

[[Received ]{lang="EN-US"}]{#struct_0_x7280_11703_1769232401}[p]{lang="EN-US"}[ackets]{lang="EN-US"}

[[收到的报文数]{style="font-family:宋体"}]{#struct_0_x7280_11703_542391619}

[[Sen]{lang="EN-US"}]{#struct_0_x7280_11703_731068568}[t]{lang="EN-US"}[ ]{lang="EN-US"}[p]{lang="EN-US"}[ackets]{lang="EN-US"}

[[发出的报文数（虚服务器发给客户端的）]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1164752830}

[[Dropped packets]{lang="EN-US"}]{#struct_0_x7280_11703_960726794}

[[丢弃的报文数]{style="font-family:宋体"}]{#struct_0_x7280_11703_x589062264}

[[Received requests]{lang="EN-US"}]{#struct_0_x7280_11703_x335967333}

[[收到的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x335574117}[请求报文数量，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Dropped requests]{lang="EN-US"}]{#struct_0_x7280_11703_x335639653}

[[丢弃的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x335770725}[请求报文数量，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Sent responses]{lang="EN-US"}]{#struct_0_x7280_11703_x335311973}

[[发出的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x335836262}[应答报文数量，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[[Dropped responses]{lang="EN-US"}]{#struct_0_x7280_11703_x335901798}

[[丢弃的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x336032870}[应答报文数量，只有]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器才会显示本字段]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[]{#_Toc334536490}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1542305457}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1699289558}**[virtual]{lang="EN-US"}[-server]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}

::: {#-1492054709 .myid}
[]{#_Toc404796582}[]{#struct_0_x7280_11703_x335770726}[]{#_Toc380504939}[]{#_Toc364842568}[]{#_Toc362006265}

**负载均衡 \-- 负载均衡配置命令 \-- exceed-mss**

------------------------------------------------------------------------

[**[exceed-mss]{lang="EN-US"}**]{#struct_0_x7280_11703_249946808}[命令用来配置对客户端发来的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文中超出]{style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段的处理方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[exceed-mss]{lang="EN-US"}**]{#struct_0_x7280_11703_x335311974}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x335377510}

[**[exceed-mss]{lang="EN-US"}**[ { **allow** \| **drop** }]{lang="EN-US"}]{#struct_0_x7280_11703_x335836267}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[exceed-mss]{lang="EN-US"}**]{#struct_0_x7280_11703_651885023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x335901803}

[[对客户端发来的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x335967339}[请求报文中超出]{style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段的处理方式为允许超出]{style="font-family:宋体"}[MSS]{lang="FR"}[的数据段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x336032875}

[[参数模板]{style="font-family:宋体"}]{#struct_0_x7280_11703_x335574123}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1071976454}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x335639659}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x335705195}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x335770731}

[**[allow]{lang="FR"}**]{#struct_0_x7280_11703_249488057}[：]{style="font-family:宋体"}[允许超出]{style="font-family:宋体"}[MSS]{lang="FR"}[的数据段。]{style="font-family:宋体"}

[**[drop]{lang="FR"}**]{#struct_0_x7280_11703_x335311979}[：]{style="font-family:宋体"}[丢弃超出]{style="font-family:宋体"}[MSS]{lang="FR"}[的数据段。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x335377515}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x335836268}[TCP]{lang="FR"}[类型的参数模板]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_652605919}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_x335901804}[在]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[类型的]{style="font-family:宋体"}[参数模板]{style="font-family:宋体"}[pp3]{lang="FR"}[中，配置]{style="font-family:宋体"}[对客户端发来的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文中超出]{style="font-family:宋体"}[MSS]{lang="EN-US"}[的数据段的处理方式为]{style="font-family:宋体"}[丢弃超出]{style="font-family:宋体"}[MSS]{lang="DE"}[的数据段]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_x335967340}

[\[Sysname\] parameter-profile pp3 type tcp]{lang="FR"}

[\[Sysname-para-tcp-pp3\] exceed-mss drop]{lang="FR"}
:::

::: {#-1751314288 .myid}
[]{#_Toc404796583}[]{#struct_0_x7280_11703_1390751767}

**负载均衡 \-- 负载均衡配置命令 \-- fail-action**

------------------------------------------------------------------------

[**[fail-action]{lang="EN-US"}**]{#struct_0_x7280_11703_1425335223}[命令用来配置实服务组的故障处理方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **fail-action**]{lang="EN-US"}]{#struct_0_x7280_11703_985519668}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x309885088}

[**[fail-action]{lang="EN-US"}**[ { **keep** \| **reschedule** \| **reset** }]{lang="EN-US"}]{#struct_0_x7280_11703_2030188789}

[**[undo]{lang="EN-US"}**[ **fail-action**]{lang="EN-US"}]{#struct_0_x7280_11703_960595722}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_332636333}

[[实服务组的故障处理方式为保持已有连接。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1941932237}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x814458504}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_952072053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_252137891}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_251841428}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x692335733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960923402}

[**[keep]{lang="EN-US"}**]{#struct_0_x7280_11703_x754248675}[：]{style="font-family:宋体"}[保持已有连接，即不主动断开与故障实服务器的连接，连接继续保持还是断开将由协议自身的超时机制决定。]{style="font-family:宋体"}

[**[reschedule]{lang="EN-US"}**]{#struct_0_x7280_11703_821663417}[：重定向连接，即把连接重定向到实服务组中其它可用的实服务器上。]{style="font-family:宋体"}

[**[reset]{lang="EN-US"}**]{#struct_0_x7280_11703_1791750367}[：断开已有连接，即主动断开与故障实服务器的连接。对于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[报文，将发送]{style="font-family:宋体"}[RST]{lang="EN-US"}[报文；对于其它类型的报文，将发送]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[不可达报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1489066053}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_780951723}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的故障处理方式为重定向连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2119788437}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] fail-action reschedule]{lang="EN-US"}
:::

::: {#1911956146 .myid}
[]{#_Toc404796584}[]{#struct_0_x7280_11703_960988938}[]{#_Toc334536500}[]{#_Toc329869241}[]{#_Toc326931114}[]{#_Toc317490850}

**负载均衡 \-- 负载均衡配置命令 \-- forward all**

------------------------------------------------------------------------

[**[forward]{lang="EN-US"}**[ **all**]{lang="EN-US"}]{#struct_0_x7280_11703_x1974838300}[命令用来配置报文的转发模式为转发。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **forward**]{lang="EN-US"}]{#struct_0_x7280_11703_x1873191999}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1748067102}

[**[forward]{lang="EN-US"}**[ **all**]{lang="EN-US"}]{#struct_0_x7280_11703_1213070542}

[**[undo]{lang="EN-US"}**[ **forward**]{lang="EN-US"}]{#struct_0_x7280_11703_87360809}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1667565095}

[[报文的转发模式为丢弃。]{style="font-family:宋体"}]{#struct_0_x7280_11703_539400758}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_734903372}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_960792330}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x540029377}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x854119973}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x331931074}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1832161704}

[[本命令只在通用类型的负载均衡]{style="font-family:宋体"}]{#struct_0_x7280_11703_x335770732}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[需要注意的是，本命令]{style="font-family:宋体"}]{#struct_0_x7280_11703_152590876}[与]{style="font-family:宋体"}**[server-farm]{lang="FR"}**[命令互斥]{style="font-family:宋体"}[，当]{style="font-family:宋体"}[配置了其中一条后]{style="font-family:宋体"}[，]{style="font-family:宋体"}[另一条的配置将被自动取消。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x842016874}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_x1063562043}[在通用类型的]{style="font-family:宋体"}[负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[lba]{lang="EN-US"}[1]{lang="FR"}[中，配置]{style="font-family:宋体"}[报文的转发模式为]{style="font-family:宋体"}[转发]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_960857866}

[\[Sysname\] loadbalance action lba1 type generic]{lang="FR"}

[\[Sysname-lba-generic-lba1\] forward all]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x351017404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server-farm]{lang="EN-US"}**[ (LB action view)]{lang="EN-US"}]{#struct_0_x7280_11703_x2068266648}
:::

::: {#-765155106 .myid}
[]{#_Toc404796585}[]{#struct_0_x7280_11703_1230509822}[]{#_Toc380504942}[]{#_Toc364842572}[]{#_Toc362006257}

**负载均衡 \-- 负载均衡配置命令 \-- header**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**]{#struct_0_x7280_11703_1230444286}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**]{#struct_0_x7280_11703_1230378750}[命令用来删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1874967059}

[**[header]{lang="EN-US"}**[ { { **host** \| **name** *header-name* \| **url** } \[ **offset** *offset* \] \[ **start** *start-string*\] \[ **end** *end-string* \| **length** *length* \] } \| **request-method** **\|** **version** }]{lang="EN-US"}]{#struct_0_x7280_11703_1230313214}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**]{#struct_0_x7280_11703_1230771966}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230706430}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230247677}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x419121267}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230182141}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230116605}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1230051069}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1230509821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_726353075}

[**[host]{lang="FR"}**]{#struct_0_x7280_11703_1230444285}[：]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[主机]{style="font-family:宋体"}[的持续性方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[name]{lang="FR"}**]{#struct_0_x7280_11703_1230378749}[ *header-name*]{lang="FR"}[：基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部]{style="font-family:宋体"}[名称的持续性方法]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[63]{lang="FR"}[个字符的字符串。]{style="font-family:宋体"}

[**[url]{lang="FR"}**]{#struct_0_x7280_11703_1230313213}[：]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[HTTP URL]{lang="FR"}[的持续性方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[offset]{lang="FR"}**]{#struct_0_x7280_11703_1230771965}[ *offset*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文起始位置的偏移量]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[1000]{lang="FR"}[，]{style="font-family:
宋体"}[缺省值为]{style="font-family:宋体"}[0]{lang="FR"}[。]{style="font-family:宋体"}

[**[start]{lang="FR"}**]{#struct_0_x7280_11703_x1592156123}[ *start-string*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部开始标记的正则表达式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即从]{style="font-family:宋体"}*[offset]{lang="FR"}*[起到本标记为开始]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[127]{lang="FR"}[字符的字符串。]{style="font-family:宋体"}

[**[end]{lang="FR"}**]{#struct_0_x7280_11703_1230706429}[ *end-string*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部结束标记的正则表达式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[即从]{style="font-family:宋体"}*[start-string]{lang="FR"}*[起到本标记为结束]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[127]{lang="FR"}[字符的字符串。]{style="font-family:宋体"}

[**[length]{lang="FR"}**]{#struct_0_x7280_11703_1230247680}[ *length*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部的长度]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[1000]{lang="FR"}[，]{style="font-family:宋体"}[缺省值为]{style="font-family:宋体"}[0]{lang="FR"}[，]{style="font-family:宋体"}[表示所有长度。]{style="font-family:
宋体"}

[**[request-method]{lang="FR"}**]{#struct_0_x7280_11703_1230182144}[：]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[HTTP Request-Method]{lang="FR"}[的持续性方法]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[version]{lang="FR"}**]{#struct_0_x7280_11703_1230116608}[：]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[版本]{style="font-family:宋体"}[的持续性方法。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1978913850}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230051072}[HTTP]{lang="FR"}[首部类型的持续性组视图下支持。]{style="font-family:宋体"}

[[本命令用来根据]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230509824}*[offset]{lang="FR"}*[、]{style="font-family:宋体"}*[start-string]{lang="FR"}*[、]{style="font-family:宋体"}*[end-string]{lang="FR"}*[及]{style="font-family:宋体"}*[length]{lang="FR"}*[获取生成持续性表项的]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部信息。]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[将不计入持续性表项信息中。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230444288}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_1230378752}[在]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部类型的]{style="font-family:
宋体"}[持续性组]{style="font-family:宋体"}[sg4]{lang="FR"}[中，配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部持续性方法为]{style="font-family:宋体"}[：]{style="font-family:宋体"}[基于]{style="font-family:宋体"}[HTTP]{lang="FR"}[主机]{style="font-family:宋体"}[来生成持续性表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DE"}]{#struct_0_x7280_11703_1230313216}

[\[Sysname\] sticky-group sg4 type http-header]{lang="DE"}

[\[Sysname-sticky-http-header-sg4\] header host]{lang="DE"}
:::

::: {#1116738822 .myid}
[]{#_Toc362006272}[]{#_Toc362006275}[]{#_Toc354047349}[]{#_Toc404796586}[]{#struct_0_x7280_11703_x1616868902}[]{#_Toc380504943}[]{#_Toc364842573}[]{#_Toc362006311}[]{#_Toc347413254}

**负载均衡 \-- 负载均衡配置命令 \-- header delete**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **delete**]{lang="EN-US"}]{#struct_0_x7280_11703_1230771968}[命令用来删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **header** **delete**]{lang="EN-US"}]{#struct_0_x7280_11703_1230706432}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230247679}

[**[header]{lang="EN-US"}**[ **delete** { **both** \| **request** \| **response** } **name** *header-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1230182143}

[**[undo]{lang="EN-US"}**[ **header** **delete** { **both** \| **request** \| **response** } **name** *header-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x477299146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230116607}

[[不删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1230051071}[首部。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230509823}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230444287}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1911636531}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1230378751}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1230313215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230706431}

[**[both]{lang="FR"}**]{#struct_0_x7280_11703_x1594086521}[：]{style="font-family:宋体"}[请求和应答两个方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[request]{lang="FR"}**]{#struct_0_x7280_11703_1230247674}[：]{style="font-family:宋体"}[请求方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[response]{lang="FR"}**]{#struct_0_x7280_11703_1230116602}[：]{style="font-family:宋体"}[应答方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[name]{lang="FR"}**]{#struct_0_x7280_11703_x1978520634}[ *header-name*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{style="font-family:宋体"}[首部的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括标准和自定义的首部]{style="font-family:宋体"}[，]{style="font-family:宋体"}[需要与报文中的首部完全匹配。为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[63]{lang="FR"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[不区分大小写。不包括]{style="font-family:
宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:
宋体"}[,]{lang="EN-US"}[、]{style="font-family:宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:
宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:
宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:
宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:宋体"}[），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230051066}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1230509818}[类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果指定方向的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1230444282}[报文中携带有指定名称的首部，系统会将该首部从报文中删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230378746}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_1230313210}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡动作]{style="font-family:宋体"}[lb]{lang="EN-US"}[a2]{lang="DE"}[中，]{style="font-family:宋体"}[删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文中名为]{style="font-family:宋体"}[host]{lang="EN-US"}[的首部。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1230771962}

[\[Sysname\] loadbalance action lba2 type http]{lang="EN-US"}

[\[Sysname-lba-http-lba2\] header delete request name host]{lang="EN-US"}
:::

::: {#870954114 .myid}
[]{#_Toc404796587}[]{#struct_0_x7280_11703_1230706426}[]{#_Toc380504944}[]{#_Toc364842574}

**负载均衡 \-- 负载均衡配置命令 \-- header exceed-length**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **exceed-length**]{lang="EN-US"}]{#struct_0_x7280_11703_1230247673}[命令用来配置当]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求或应答报文首部超出最大长度时的处理方式。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **header** ]{lang="EN-US"}**[exceed-length]{lang="EN-US"}**]{#struct_0_x7280_11703_x418859123}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230182137}

[**[header]{lang="EN-US"}**[ **exceed-length** { **continue** \| **drop** }]{lang="EN-US"}]{#struct_0_x7280_11703_1230116601}

[**[undo]{lang="EN-US"}**[ **header** ]{lang="EN-US"}**[exceed-length]{lang="EN-US"}**]{#struct_0_x7280_11703_1230051065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1888657542}

[[当]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1230509817}[请求或应答报文首部超出最大长度时，继续进行负载均衡处理。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230444281}

[[参数模板]{style="font-family:宋体"}]{#struct_0_x7280_11703_1230378745}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230313209}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1617458727}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1230771961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1230706425}

[**[continue]{lang="FR"}**]{#struct_0_x7280_11703_826963151}[：]{style="font-family:宋体"}[继续执行负载均衡操作。]{style="font-family:宋体"}

[**[drop]{lang="FR"}**]{#struct_0_x7280_11703_826897615}[：]{style="font-family:宋体"}[停止执行负载均衡操作]{style="font-family:宋体"}[，]{style="font-family:宋体"}[丢弃该报文并关闭连接。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826832079}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_826766543}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_827225295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_x7280_11703_1999058949}[HTTP]{lang="EN-US"}[报文首部的长度超过负载均衡的处理能力时，系统将无条件使用]{style="font-family:宋体"}**[drop]{lang="FR"}**[方式处理该报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[快速]{style="font-family:宋体"}]{#struct_0_x7280_11703_827159759}[HTTP]{lang="EN-US"}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827094223}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_827028687}[在]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，配置]{style="font-family:宋体"}[当]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求或应答报文首部超出最大长度时的处理方式为：停止执行负载均衡操作，丢弃该报文并关闭连接。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_827487439}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] header exceed-length drop]{lang="EN-US"}
:::

::: {#67900602 .myid}
[]{#_Toc404796588}[]{#struct_0_x7280_11703_827421903}[]{#_Toc380504945}[]{#_Toc364842575}[]{#_Toc362006313}

**负载均衡 \-- 负载均衡配置命令 \-- header insert**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **insert**]{lang="EN-US"}]{#struct_0_x7280_11703_826963150}[命令用来插入]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **header** **insert**]{lang="EN-US"}]{#struct_0_x7280_11703_826897614}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826832078}

[**[header]{lang="EN-US"}**[ **insert** { **both** \| **request** \| **response** } **name** *header-name* **value** *value*]{lang="EN-US"}]{#struct_0_x7280_11703_826766542}

[**[undo]{lang="EN-US"}**[ **header** **insert** { **both** \| **request** \| **response** } **name** *header-name*]{lang="EN-US"}]{#struct_0_x7280_11703_827225294}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827159758}

[[不插入]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_827094222}[首部。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827028686}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_827487438}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827421902}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_826963153}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_279175601}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826897617}

[**[both]{lang="FR"}**]{#struct_0_x7280_11703_826832081}[：]{style="font-family:宋体"}[请求和应答两个方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[request]{lang="FR"}**]{#struct_0_x7280_11703_826766545}[：]{style="font-family:宋体"}[请求方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[response]{lang="FR"}**]{#struct_0_x7280_11703_827225297}[：]{style="font-family:宋体"}[应答方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[name]{lang="FR"}**]{#struct_0_x7280_11703_827159761}[ *header-name*]{lang="FR"}[：]{style="font-family:宋体"}[要插入]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文中]{style="font-family:宋体"}[的首部名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括标准和自定义的首部。为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[63]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。不包括]{style="font-family:宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:
宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:宋体"}[,]{lang="EN-US"}[、]{style="font-family:
宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:
宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:
宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:宋体"}[），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[value]{lang="FR"}**]{#struct_0_x7280_11703_827094225}[ *value*]{lang="FR"}[：]{style="font-family:宋体"}[要插入]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文中的]{style="font-family:宋体"}[首部内容]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[个字符的字符串，也可以使用以下特定含义的字符串]{style="font-family:宋体"}[：]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[%is]{lang="FR"}]{#struct_0_x7280_11703_827028689}[：]{style="font-family:宋体"}[源]{style="font-family:宋体"}[IP]{lang="FR"}[地址或源]{style="font-family:
宋体"}[IPv6]{lang="FR"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[%ps]{lang="FR"}]{#struct_0_x7280_11703_1707412093}[：]{style="font-family:宋体"}[源端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[%id]{lang="FR"}]{#struct_0_x7280_11703_827487441}[：]{style="font-family:宋体"}[目的]{style="font-family:宋体"}[IP]{lang="FR"}[地址或目的]{style="font-family:
宋体"}[IPv6]{lang="FR"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[%pd]{lang="EN-US"}]{#struct_0_x7280_11703_827421905}[：]{style="font-family:宋体"}[目的端口号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826963152}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_826897616}[类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，系统将在指定方向的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_826832080}[报文中插入指定名称和内容的首部。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826766544}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_827225296}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡动作]{style="font-family:宋体"}[lba2]{lang="EN-US"}[中，将名为]{style="font-family:宋体"}[source]{lang="EN-US"}[、内容为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[和源端口号的首部插入到]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文中。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_827159760}

[\[Sysname\] loadbalance action lba2 type http]{lang="EN-US"}

[\[Sysname-lba-http-lba2\] header insert request name source value %is:%ps]{lang="EN-US"}
:::

::: {#-939469936 .myid}
[]{#_Toc404796589}[]{#struct_0_x7280_11703_827094224}[]{#_Toc380504946}[]{#_Toc364842576}

**负载均衡 \-- 负载均衡配置命令 \-- header maxparse-length**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_537475313}[命令用来配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部的最大解析长度。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_827028688}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827487440}

[**[header]{lang="EN-US"}**[ **maxparse-length** *length*]{lang="EN-US"}]{#struct_0_x7280_11703_827421904}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**[ **maxparse-length**]{lang="EN-US"}]{#struct_0_x7280_11703_826963147}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826897611}

[[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_826832075}[首部的最大解析长度为]{style="font-family:宋体"}[4096]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826766539}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_827225291}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827159755}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1809279667}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_827094219}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827028683}

[*[length]{lang="FR"}*]{#struct_0_x7280_11703_827487435}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[首部的最大解析长度]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827421899}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_826963146}[HTTP]{lang="FR"}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1677139532}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_826897610}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_826832074}[在]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，配]{style="font-family:宋体"}[置]{style="font-family:宋体"}[HTTP]{lang="DE"}[首部的最大解析长度为]{style="font-family:宋体"}[8192]{lang="DE"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_826766538}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] header maxparse-length 8192]{lang="EN-US"}
:::

::: {#1206346198 .myid}
[]{#_Toc404796590}[]{#struct_0_x7280_11703_827225290}[]{#_Toc380504947}[]{#_Toc364842577}[]{#_Toc362006269}[]{#_Toc347413209}

**负载均衡 \-- 负载均衡配置命令 \-- header modify per-request**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **modify** **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_827159754}[命令用来配置对每个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求或应答报文的首部都执行插入、删除或修改操作。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**[ **modify** **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_827094218}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1036502811}

[**[header]{lang="EN-US"}**[ **modify** **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_827028682}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[header]{lang="EN-US"}**[ **modify** **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_827487434}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_827421898}

[[只对每个连接的第一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1901920204}[请求或应答报文的首部执行插入、删除或修改操作。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901985740}

[[参数模板]{style="font-family:宋体"}]{#struct_0_x7280_11703_x422582922}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1902051276}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1902116812}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x1901658060}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901723596}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1901789132}[HTTP]{lang="FR"}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1037304762}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_x1901854668}[在]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，]{style="font-family:宋体"}[配置对每个]{style="font-family:宋体"}[HTTP]{lang="FR"}[请求或应答报文的首部都执行插入、删除或修改操作。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_x1901395916}

[\[Sysname\] parameter-profile pp1 type http]{lang="FR"}

[\[Sysname-para-http-pp1\] header modify per-request]{lang="EN-US"}
:::

::: {#-308330494 .myid}
[]{#_Toc404796591}[]{#struct_0_x7280_11703_x1901461452}[]{#_Toc380504948}[]{#_Toc364842578}[]{#_Toc362006312}

**负载均衡 \-- 负载均衡配置命令 \-- header rewrite**

------------------------------------------------------------------------

[**[header]{lang="EN-US"}**[ **rewrite**]{lang="EN-US"}]{#struct_0_x7280_11703_x1901920205}[命令用来重写]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **header** **rewrite**]{lang="EN-US"}]{#struct_0_x7280_11703_x1901985741}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1988666863}

[**[header]{lang="EN-US"}**[ **rewrite** { **both** \| **request** \| **response** } **name** *header-name* **value** *value* **replace** *replace*]{lang="EN-US"}]{#struct_0_x7280_11703_x1902051277}

[**[undo]{lang="EN-US"}**[ **header** **rewrite** { **both** \| **request** \| **response** } **name** *header-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1902116813}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901658061}

[[不重写]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1901723597}[首部。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_41918655}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1901789133}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901854669}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1901395917}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x1901461453}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_111542198}

[**[both]{lang="FR"}**]{#struct_0_x7280_11703_x1901920202}[：]{style="font-family:宋体"}[请求和应答两个方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[request]{lang="FR"}**]{#struct_0_x7280_11703_x1901985738}[：]{style="font-family:宋体"}[请求方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[response]{lang="FR"}**]{#struct_0_x7280_11703_x1902051274}[：]{style="font-family:宋体"}[应答方向的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文。]{style="font-family:宋体"}

[**[name]{lang="FR"}**]{#struct_0_x7280_11703_x1902116810}[ *header-name*]{lang="FR"}[：]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{style="font-family:宋体"}[首部的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括标准和自定义的首部]{style="font-family:宋体"}[，]{style="font-family:宋体"}[需要与报文中的首部完全匹配。为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[63]{lang="FR"}[个字符的字符串]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[不区分大小写。不包括]{style="font-family:
宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:
宋体"}[,]{lang="EN-US"}[、]{style="font-family:宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:
宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:
宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:
宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:宋体"}[），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1901658058}[：要被重写的]{style="font-family:宋体"}[HTTP]{lang="FR"}[报文]{style="font-family:宋体"}[首部的内容]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[127]{lang="FR"}[个字符的字符串。]{style="font-family:宋体"}

[**[replace]{lang="EN-US"}**[ *replace*]{lang="EN-US"}]{#struct_0_x7280_11703_x910088196}[：重写后的内容，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901723594}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1901789130}[类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果指定方向的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1901854666}[报文中携带有指定名称的首部，系统会将该首部中的内容]{style="font-family:宋体"}*[value]{lang="EN-US"}*[重写为]{style="font-family:宋体"}*[replace]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1901395914}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1901461450}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡动作]{style="font-family:宋体"}[lba2]{lang="EN-US"}[中，将]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文名中为]{style="font-family:宋体"}[host]{lang="EN-US"}[的首部中的内容，由]{style="font-family:宋体"}[www\\.(h3c)\\.com]{lang="EN-US"}[重写为]{style="font-family:宋体"}[www.%1.com.cn]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1901920203}

[\[Sysname\] loadbalance action lba2 type http]{lang="EN-US"}

[\[Sysname-lba-http-lba2\] header rewrite request name host value www\\.(h3c)\\.com replace www.%1.com.cn]{lang="EN-US"}
:::

::: {#-839206969 .myid}
[]{#_Toc311899221}[]{#_Toc404796592}[]{#struct_0_x7280_11703_1718058702}[]{#_Toc334536468}[]{#_Toc329869213}[]{#_Toc325557605}

**负载均衡 \-- 负载均衡配置命令 \-- ip**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**]{#struct_0_x7280_11703_x1238193668}[命令用来配置]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip**]{lang="EN-US"}]{#struct_0_x7280_11703_147860950}[命令用来删除]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x486794414}

[**[ip]{lang="EN-US"}**[ \[ **port** \] { **both** \| **destination** \| **source** } \[ **mask** *mask-length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1302861690}

[**[undo]{lang="EN-US"}**[ **ip**]{lang="EN-US"}]{#struct_0_x7280_11703_1720686468}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_961185546}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x45973109}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x640385510}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_415347514}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2071934577}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1421421668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1092136872}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1155684892}

[**[port]{lang="EN-US"}**]{#struct_0_x7280_11703_961251082}[：表示持续性方法为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋端口。如果未指定本参数，表示持续性方法为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x7280_11703_x932240725}[：当未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址；当指定了]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋源端口＋目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的端口。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_x7280_11703_x1315773969}[：当未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址；当指定了]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为目的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋目的端口。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_x7280_11703_x168561446}[：当未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址；当指定了]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时，表示持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋源端口。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ *mask-length*]{lang="EN-US"}]{#struct_0_x7280_11703_1759483332}[：持续性方法的掩码长度，仅对]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1652021634}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1710523342}[在地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[中，配置持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_960661255}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] ip source]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1769232406}[在地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[中，配置持续性方法为源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址＋源端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_542850371}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] ip port source]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1073381651}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sticky-group]{lang="EN-US"}**]{#struct_0_x7280_11703_x1400586100}
:::

::: {#1613709608 .myid}
[]{#_Toc404796593}[]{#struct_0_x7280_11703_2099229970}[]{#_Toc334536512}[]{#_Toc329869253}[]{#_Toc329241935}

**负载均衡 \-- 负载均衡配置命令 \-- ip address**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_x7280_11703_1599418994}[命令用来配置实服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_960726791}[命令用来删除实服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x589062267}

[**[ip]{lang="EN-US"}**[ **address** *ipv4-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x1363584307}

[**[undo]{lang="EN-US"}**[ **ip** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_1502047008}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1168080454}

[[实服务器没有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x285177419}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x754802119}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1267861975}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1967114084}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_960530183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1542305452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1699092950}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x7280_11703_113883654}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，不能为环回地址、组播地址、广播地址和]{style="font-family:宋体"}[0.X.X.X]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2078026465}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x262413266}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1290240229}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] ip address 1.1.1.1]{lang="EN-US"}
:::

::: {#-316194105 .myid}
[]{#_Toc404796594}[]{#struct_0_x7280_11703_488357048}[]{#_Toc334536477}[]{#_Toc329875708}[]{#_Toc329869221}[]{#_Toc329773995}

**负载均衡 \-- 负载均衡配置命令 \-- ip range**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **range**]{lang="EN-US"}]{#struct_0_x7280_11703_960595719}[命令用来配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **range**]{lang="EN-US"}]{#struct_0_x7280_11703_1906614434}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x658835951}

[**[ip]{lang="EN-US"}**[ **range** **start** *start-ipv4-address* **end** *end-ipv4-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x17060862}

[**[undo]{lang="EN-US"}**[ **ip** **range**]{lang="EN-US"}]{#struct_0_x7280_11703_x1804640793}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1276699033}

[[没有配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_110981620}[地址池的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1324938216}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_960923399}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1971899681}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1828002452}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1467096345}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_657854322}

[**[start]{lang="EN-US"}**[ *start-ipv4-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x1125217451}[：起始]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[end]{lang="EN-US"}**[ *end-ipv4-address*]{lang="EN-US"}]{#struct_0_x7280_11703_347033917}[：结束]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，必须大于等于起始]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1125707092}

[[需要注意的是，一个]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x1092239911}[地址池中最多允许有]{style="font-family:宋体"}[256]{lang="EN-US"}[个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，且不同]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址不允许重叠。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960988935}

[[\# ]{lang="PT-BR"}]{#struct_0_x7280_11703_x1974838287}[配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池]{style="font-family:宋体"}[lb]{lang="EN-US"}[sp]{lang="PT-BR"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址范围]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1.1.1.1]{lang="PT-BR"}[～]{style="font-family:宋体"}[1.1.1.100]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x306583769}

[\[Sysname\] loadbalance snat-pool lbsp]{lang="EN-US"}

[\[Sysname-lbsnat-pool-lbsp\] ip range start 1.1.1.1 end 1.1.1.100]{lang="EN-US"}
:::

::: {#-488313789 .myid}
[]{#_Toc404796595}[]{#struct_0_x7280_11703_645430442}[]{#_Toc334536469}[]{#_Toc329869214}[]{#_Toc325557606}

**负载均衡 \-- 负载均衡配置命令 \-- ipv6**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**]{#struct_0_x7280_11703_x1120127873}[命令用来配置]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}]{#struct_0_x7280_11703_x46205923}[命令用来删除]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1352527908}

[**[ipv6]{lang="EN-US"}**[ \[ **port** \] { **both** \| **destination** \| **source** } \[ **prefix** *prefix-length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1007684559}

[**[undo]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}]{#struct_0_x7280_11703_960792327}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1798622788}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x193761476}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2108378708}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x389514430}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1101272886}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1620523758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x462778104}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960857863}

[**[port]{lang="EN-US"}**]{#struct_0_x7280_11703_x351017401}[：表示持续性方法为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋端口。如果未指定本参数，表示持续性方法为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[both]{lang="EN-US"}**]{#struct_0_x7280_11703_x2068070040}[：表示持续性方法为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时），或源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋源端口＋目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋目的端口（指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时）。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_x7280_11703_1287017059}[：表示持续性方法为目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时），或目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋目的端口（指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时）。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_x7280_11703_x1247357626}[：表示持续性方法为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（未指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时），或源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋源端口（指定]{style="font-family:宋体"}**[port]{lang="EN-US"}**[参数时）。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix-length*]{lang="EN-US"}]{#struct_0_x7280_11703_1092539139}[：持续性方法的前缀长度，仅对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_268247747}

[]{#_Toc334536513}[]{#_Toc329869254}[]{#_Toc329241936}[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_961185543}[在地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[中，配置持续性方法为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x45973112}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] ipv6 source]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1315929619}[在地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[中，配置持续性方法为源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址＋源端口。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_496186428}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] ipv6 port source]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1910960187}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sticky-group]{lang="EN-US"}**]{#struct_0_x7280_11703_x1635790396}
:::

::: {#-1250635572 .myid}
[]{#_Toc404796596}[]{#struct_0_x7280_11703_452841538}

**负载均衡 \-- 负载均衡配置命令 \-- ipv6 address**

------------------------------------------------------------------------

[**[ipv6]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_x7280_11703_961251079}[命令用来配置实服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipv6** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x1741544800}[命令用来删除实服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1172876497}

[**[ipv6]{lang="EN-US"}**[ **address** *ipv6-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x1612845144}

[**[undo]{lang="EN-US"}**[ **ipv6** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x401795182}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1645266796}

[[实服务器没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_289566781}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2022490378}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2142185442}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960661256}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1769232403}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_542522691}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x536987161}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x7280_11703_x792296156}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不能为环回地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址、链路本地地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2134896971}

[]{#_Toc334536478}[]{#_Toc329875709}[]{#_Toc329869222}[]{#_Toc329773996}[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1035562697}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1001::1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_960726792}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] ipv6 address 1001::1]{lang="EN-US"}
:::

::: {#-814275021 .myid}
[]{#_Toc404796597}[]{#struct_0_x7280_11703_x589062270}

**负载均衡 \-- 负载均衡配置命令 \-- ipv6 range**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**[ **range**]{lang="EN-US"}]{#struct_0_x7280_11703_x1363518770}[命令用来配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ip** **range**]{lang="EN-US"}]{#struct_0_x7280_11703_x2100410134}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423948962}

[**[ipv6]{lang="EN-US"}**[ **range** **start** *start-ipv6-address* **end** *end-ipv6-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x256560937}

[**[undo]{lang="EN-US"}**[ **ipv6** **range**]{lang="EN-US"}]{#struct_0_x7280_11703_1658974825}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_381571455}

[[没有配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x964505801}[地址池的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960530184}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_1542305459}[地址池视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1698372054}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x963876638}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x479928981}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_641555988}

[**[start]{lang="EN-US"}**[ *start-ipv6-address*]{lang="EN-US"}]{#struct_0_x7280_11703_x2101733616}[：起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[end]{lang="EN-US"}**[ *end-ipv6-address*]{lang="EN-US"}]{#struct_0_x7280_11703_35888810}[：结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，必须大于等于起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1426119686}

[[需要注意的是，一个]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_960595720}[地址池中最多允许有]{style="font-family:宋体"}[65536]{lang="EN-US"}[个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，且不同]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址不允许重叠。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_332636331}

[[\# ]{lang="PT-BR"}]{#struct_0_x7280_11703_1941932239}[配置]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池]{style="font-family:宋体"}[lb]{lang="EN-US"}[sp]{lang="PT-BR"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1001::1]{lang="PT-BR"}[～]{style="font-family:宋体"}[1001::100]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x814065288}

[\[Sysname\] loadbalance snat-pool lbsp]{lang="EN-US"}

[\[Sysname-lbsnat-pool-lbsp\] ipv6 range start ]{lang="EN-US"}[1001::1]{lang="PT-BR"}[ end ]{lang="EN-US"}[1001::100]{lang="PT-BR"}
:::

::: {#2052955407 .myid}
[]{#_Toc404796598}[]{#struct_0_x7280_11703_992489346}[]{#_Toc334536540}[]{#_Toc329869279}[]{#_Toc329242054}

**负载均衡 \-- 负载均衡配置命令 \-- lb-policy**

------------------------------------------------------------------------

[**[lb-policy]{lang="EN-US"}**]{#struct_0_x7280_11703_373141575}[命令]{style="font-family:宋体"}[用来指定虚服务器引用的负载均衡策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **lb-poilcy**]{lang="EN-US"}]{#struct_0_x7280_11703_1431356954}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_245246981}

[**[lb-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_960923400}

[**[undo]{lang="EN-US"}**[ **lb-poilcy**]{lang="EN-US"}]{#struct_0_x7280_11703_x754248673}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_821532345}

[[虚服务器没有引用任何负载均衡策略。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1190477503}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1985186001}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1727289978}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1880797801}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1483001267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_960988936}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1974838286}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1259500172}[：]{style="font-family:宋体"}[负载均衡策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1989959175}

[[虚服务器引用负载均衡策略，能够细化虚服务器负载均衡的粒度。根据策略中的匹配规则，使命中虚服务器的报文根据不同的报文内容进行不同的负载均衡处理，从而有效地丰富了负载均衡的负载功能。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1989893639}

[[需要注意的是，虚服务器只能引用与自身类型相关的策略模板，如：快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1989828103}[和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器，可以引用通用或]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的策略模板；]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[类型的虚服务器，只能引用通用类型的策略模板。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x101964695}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1968030780}[指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[引用的负载均衡策略为]{style="font-family:宋体"}[lbp1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1492669380}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] lb-policy lbp1]{lang="EN-US"}
:::

::: {#99067163 .myid}
[]{#_Toc404796599}[]{#struct_0_x7280_11703_x1359724800}[]{#_Toc334536498}[]{#_Toc329869239}[]{#_Toc326931112}[]{#_Toc317490847}

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance action**

------------------------------------------------------------------------

[**[loadbalance]{lang="EN-US"}**[ **action**]{lang="EN-US"}]{#struct_0_x7280_11703_1469659874}[命令用来创建负载均衡动作，并进入负载均衡动作视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **loadbalance** **action**]{lang="EN-US"}]{#struct_0_x7280_11703_960792328}[命令用来删除指定的负载均衡动作。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1798622775}

[**[loadbalance]{lang="EN-US"}**[ **action** *action-name* \[ **type** { **generic** \| **http** } \]]{lang="EN-US"}]{#struct_0_x7280_11703_x193958097}

[**[undo]{lang="EN-US"}**[ **loadbalance** **action** *action-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x511671877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1090674246}

[[不存在任何负载均衡动作。]{style="font-family:宋体"}]{#struct_0_x7280_11703_945629907}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1679199463}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1955880145}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960857864}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x351017406}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x2068397720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x495025598}

[*[action-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1929215223}[：负载均衡动作的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **generic** \| **http** }]{lang="EN-US"}]{#struct_0_x7280_11703_x1257018343}[：负载均衡动作的类型，包括通用和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[两种类型。创建负载均衡动作时必须指定本参数；而在进入已创建的负载均衡动作视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_136168800}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1337610574}[创建通用类型的负载均衡动作]{style="font-family:宋体"}[lba1]{lang="EN-US"}[，并进入负载均衡动作视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_961185544}

[\[Sysname\] loadbalance action lba1 type generic]{lang="EN-US"}

[\[Sysname-lba-generic-lba1\]]{lang="EN-US"}
:::

::: {#-300221200 .myid}
[]{#_Toc404796600}[]{#struct_0_x7280_11703_x45973111}[]{#_Toc334536493}[]{#_Toc329869234}[]{#_Toc327781453}

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance class**

------------------------------------------------------------------------

[**[loadbalance]{lang="EN-US"}**[ **class**]{lang="EN-US"}]{#struct_0_x7280_11703_1315929618}[命令用来创建负载均衡类，并进入负载均衡类视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **loadbalance** **class**]{lang="EN-US"}]{#struct_0_x7280_11703_496120892}[命令用来删除指定的负载均衡类。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x248866251}

[**[loadbalance]{lang="EN-US"}**[ **class** *class-name* \[ **type** { **generic** **\|** **http** } \[ **match-all** \| **match-any** \] \]]{lang="EN-US"}]{#struct_0_x7280_11703_568415787}

[**[undo]{lang="EN-US"}**[ **loadbalance** **class** *class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_191153180}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1870237671}

[[不存在任何负载均衡类。]{style="font-family:宋体"}]{#struct_0_x7280_11703_21593169}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_961251080}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x932240727}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1315905041}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1844303264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_583748305}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1013348665}

[*[class-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1755076066}[：负载均衡类的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **generic** **\|** **http** }]{lang="EN-US"}]{#struct_0_x7280_11703_1923345481}[：负载均衡类的类型，包括通用和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[两种类型。创建负载均衡类时必须指定本参数；而在进入已创建的负载均衡类视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[\[ **match-all** \| **match-any** \]]{lang="EN-US"}]{#struct_0_x7280_11703_1671157290}[：]{style="font-family:宋体"}**[match-all]{lang="EN-US"}**[表示需要匹配所有规则才算匹配该类，]{style="font-family:宋体"}**[match-any]{lang="EN-US"}**[表示只需匹配任一规则就算匹配该类。缺省值为]{style="font-family:宋体"}**[match-all]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960661253}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1769232408}[创建通用类型的负载均衡类]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[，并进入负载均衡类视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_542981443}

[\[Sysname\] loadblance class lbc1 type generic]{lang="EN-US"}

[\[Sysname-lbc-generic-lbc1\]]{lang="EN-US"}
:::

::: {#-263912840 .myid}
[]{#_Toc404796601}[]{#struct_0_x7280_11703_x2019078391}[]{#_Toc334536505}[]{#_Toc329869246}[]{#_Toc327781458}[]{#_Toc317490860}

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance policy**

------------------------------------------------------------------------

[**[loadbalance]{lang="EN-US"}**[ **poliy** ]{lang="EN-US"}]{#struct_0_x7280_11703_1719292483}[命令用来创建负载均衡策略，并进入负载均衡策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **loadbalance** **policy**]{lang="EN-US"}]{#struct_0_x7280_11703_389225512}[命令用来删除指定的负载均衡策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1713024444}

[**[loadbalance]{lang="EN-US"}**[ **policy** *policy-name* \[ **type** { **generic** \| **http** } \]]{lang="EN-US"}]{#struct_0_x7280_11703_x36448364}

[**[undo]{lang="EN-US"}**[ **loadbalance** **policy** *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_960726789}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1749589901}

[[不存在任何负载均衡策略。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1564451675}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1236916803}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1557452098}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_912514313}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1823256473}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_319245037}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960530181}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1542305454}[：负载均衡策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **generic** \| **http** }]{lang="EN-US"}]{#struct_0_x7280_11703_x1699224022}[：负载均衡策略的类型，包括通用和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[两种类型。创建负载均衡策略时必须指定本参数；而在进入已创建的负载均衡策略视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2036153274}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_609796070}[创建通用类型的负载均衡策略]{style="font-family:宋体"}[lbp1]{lang="EN-US"}[，并进入负载均衡策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1398291407}

[\[Sysname\] loadbalance policy lbp1 type generic]{lang="EN-US"}

[\[Sysname-lbp-generic-lbp1\]]{lang="EN-US"}
:::

::: {#624383830 .myid}
[]{#_Toc404796602}[]{#struct_0_x7280_11703_846062676}[]{#_Toc334536475}[]{#_Toc329875707}[]{#_Toc329869220}[]{#_Toc329773994}

**负载均衡 \-- 负载均衡配置命令 \-- loadbalance snat-pool**

------------------------------------------------------------------------

[**[loadbalance]{lang="EN-US"}**[ **snat-pool**]{lang="EN-US"}]{#struct_0_x7280_11703_x1300289349}[命令用来创建]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池，并进入]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **loadbalance** ]{lang="EN-US"}**[snat-pool]{lang="EN-US"}**]{#struct_0_x7280_11703_960595717}[命令用来删除指定的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1906614448}

[**[loadbalance]{lang="EN-US"}**[ **snat-pool** *pool-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x658573808}

[**[undo]{lang="EN-US"}**[ **loadbalance** ]{lang="EN-US"}**[snat-pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1184852840}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1379460583}

[[不存在任何]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1354615669}[SNAT]{lang="FR"}[地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1333651187}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1441147128}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_593362094}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_960923397}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1971899675}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1828264593}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x7280_11703_306667949}[：]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1760683194}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x613731134}[创建]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池]{style="font-family:宋体"}[lbsp]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_612064801}

[\[Sysname\] loadbalance snat-pool lbsp]{lang="EN-US"}

[\[Sysname-lbsnat-pool-lbsp\]]{lang="EN-US"}
:::

::: {#1366310664 .myid}
[]{#_Toc404796603}[]{#struct_0_x7280_11703_x738924183}[]{#_Toc380504993}[]{#_Toc364842592}

**负载均衡 \-- 负载均衡配置命令 \-- match class**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **class**]{lang="EN-US"}]{#struct_0_x7280_11703_x738989719}[命令用来创建嵌套类的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x739055255}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738596503}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **class** *class-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x739120788}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x739186324}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x739251860}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x739317396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738858644}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x738924180}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738989716}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x739055252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x738596500}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738662036}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_x739120789}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[*[class-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x739186325}[：要嵌套的负载均衡类名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。不允许嵌套当前的负载均衡类。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x739317397}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x738858645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果嵌套的负载均衡类]{style="font-family:宋体"}]{#struct_0_x7280_11703_x738924181}[lbc1]{lang="EN-US"}[中已嵌套负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[，则]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[在此嵌套中将不会生效。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个负载均衡类中最多允许创建]{style="font-family:宋体"}]{#struct_0_x7280_11703_x738989717}[65535]{lang="EN-US"}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x739055253}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x738596501}[在通用类型的负载均衡类]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[中，创建嵌套类的匹配规则为：嵌套负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x738662037}

[\[Sysname\] loadbalance class lbc1 type generic]{lang="EN-US"}

[\[Sysname-lbc-generic-lbc1\] match class lbc2]{lang="EN-US"}
:::

::: {#1300062833 .myid}
[]{#_Toc362006297}[]{#_Toc404796604}[]{#struct_0_x7280_11703_x739120794}[]{#_Toc380504994}

**负载均衡 \-- 负载均衡配置命令 \-- match content**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **content**]{lang="EN-US"}]{#struct_0_x7280_11703_x739186330}[命令用来创建]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体类型的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x739317402}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738858650}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **content** *content* \[ **offset** *offset* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x738924186}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x738989722}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x739055258}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x738596506}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738662042}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x739120795}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x739186331}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x739251867}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x739317403}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738858651}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_x738989723}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[content]{lang="EN-US"}**[ *content*]{lang="EN-US"}]{#struct_0_x7280_11703_x739055259}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体的]{style="font-family:宋体"}[正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[offset]{lang="EN-US"}**[ *offset*]{lang="EN-US"}]{#struct_0_x7280_11703_x738596507}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x738662043}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1142405317}[类型的负载均衡类视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1142470853}[报文的实体部分在偏移了]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[后能够匹配指定的正则表达式，便认为此报文匹配了该规则。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1142536389}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[快速]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1142601925}[HTTP]{lang="EN-US"}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个负载均衡类中最多允许创建]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1142208709}[65535]{lang="EN-US"}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142274245}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1142339781}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中，创建]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体]{style="font-family:宋体"}[类型的匹配规则为：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文的实体部分偏移了]{style="font-family:宋体"}[10]{lang="EN-US"}[之后，包含字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1141881029}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match content abc.\* offset 10]{lang="EN-US"}
:::

::: {#815818576 .myid}
[]{#_Toc404796605}[]{#struct_0_x7280_11703_x1141946565}

**负载均衡 \-- 负载均衡配置命令 \-- match cookie**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **cookie**]{lang="EN-US"}]{#struct_0_x7280_11703_x1142405318}[命令用来创建]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x1142536390}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142601926}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **cookie** *cookie-name* **value** *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142143174}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142208710}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142274246}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1142339782}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1141881030}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1141946566}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142405315}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1142470851}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x1142536387}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142601923}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_x1142143171}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[cookie]{lang="EN-US"}**[ *cookie-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142274243}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文的]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。不包括]{style="font-family:宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:
宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:宋体"}[,]{lang="EN-US"}[、]{style="font-family:
宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:
宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:
宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:宋体"}[），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142339779}[：]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[值的正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1141881027}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1141946563}[类型的负载均衡类视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1142405316}[报文中携带有指定名称的]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[，且]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[值匹配了指定的正则表达式，便认为此报文匹配了该规则。]{style="font-family:宋体"}

[[需要注意的是，一个负载均衡类中最多允许创建]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x7280_11703_x1142470852}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142536388}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1142601924}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中，创建]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的匹配规则为：名为]{style="font-family:宋体"}[JSession-id]{lang="EN-US"}[的]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[，其值中包含字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1142208708}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match cookie JSeesion-id value abc.\*]{lang="EN-US"}
:::

::: {#-1276464789 .myid}
[]{#_Toc404796606}[]{#struct_0_x7280_11703_x1142274244}[]{#_Toc380504995}[]{#_Toc364842597}[]{#_Toc362006300}

**负载均衡 \-- 负载均衡配置命令 \-- match header**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **header**]{lang="EN-US"}]{#struct_0_x7280_11703_x1142339780}[命令用来创建]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部类型的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x1142405321}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142470857}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **header** *header-name* **value** *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142536393}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x1142601929}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142208713}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1142274249}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1141881033}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1141946569}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142405322}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1142536394}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x1142601930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1142143178}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_x1142339786}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[header]{lang="EN-US"}**[ *header-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1141881034}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文首部的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。不包括]{style="font-family:宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:
宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:宋体"}[,]{lang="EN-US"}[、]{style="font-family:
宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:
宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:
宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:宋体"}[SP]{lang="EN-US"}[（]{style="font-family:宋体"}[空格符]{style="font-family:宋体"}[）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（]{style="font-family:宋体"}[水平制表符]{style="font-family:宋体"}[），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[value]{lang="EN-US"}**[ *value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1141946570}[：首部值的正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423613088}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_423547552}[类型的负载均衡类视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_423482016}[报文中携带有指定名称的首部，且首部值匹配了指定的正则表达式，便认为此报文匹配了该规则。]{style="font-family:宋体"}

[[需要注意的是，一个负载均衡类中最多允许创建]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x7280_11703_423940768}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423875232}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_423744160}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中，创建]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部类型的匹配规则为：名为]{style="font-family:宋体"}[user-agent]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文首部，其值为]{style="font-family:宋体"}[abcd]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_424202912}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match header user-agent value abcd]{lang="EN-US"}
:::

::: {#-31840009 .myid}
[]{#_Toc404796607}[]{#struct_0_x7280_11703_424137376}[]{#_Toc380504996}[]{#_Toc364842599}[]{#_Toc362006301}

**负载均衡 \-- 负载均衡配置命令 \-- match method**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **method**]{lang="EN-US"}]{#struct_0_x7280_11703_423613087}[命令用来创建匹配报文方法类型的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_423547551}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423482015}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **method** { **ext** *ext-type* \| **rfc** *rfc-type* }]{lang="EN-US"}]{#struct_0_x7280_11703_423940767}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_423809695}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423744159}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_424202911}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423678626}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_423613090}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423547554}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_423482018}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_423875234}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423809698}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_423744162}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[ext]{lang="EN-US"}**[ *ext-type*]{lang="EN-US"}]{#struct_0_x7280_11703_424202914}[：]{style="font-family:宋体"}[扩展类型，即用户可以输入指定的字符串作为方法名。]{style="font-family:宋体"}*[ext-type]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符，区分大小写。不包括]{style="font-family:宋体"}[(]{lang="EN-US"}[、]{style="font-family:宋体"}[)]{lang="EN-US"}[、]{style="font-family:宋体"}[\<]{lang="EN-US"}[、]{style="font-family:宋体"}[\>]{lang="EN-US"}[、]{style="font-family:宋体"}[@]{lang="EN-US"}[、]{style="font-family:
宋体"}[,]{lang="EN-US"}[、]{style="font-family:宋体"}[;]{lang="EN-US"}[、]{style="font-family:宋体"}[:]{lang="EN-US"}[、]{style="font-family:宋体"}[\\]{lang="EN-US"}[、]{style="font-family:
宋体"}[\"]{lang="EN-US"}[、]{style="font-family:宋体"}[/]{lang="EN-US"}[、]{style="font-family:宋体"}[\[]{lang="EN-US"}[、]{style="font-family:宋体"}[\]]{lang="EN-US"}[、]{style="font-family:
宋体"}[?]{lang="EN-US"}[、]{style="font-family:宋体"}[=]{lang="EN-US"}[、]{style="font-family:宋体"}[{]{lang="EN-US"}[、]{style="font-family:宋体"}[}]{lang="EN-US"}[、]{style="font-family:
宋体"}[SP]{lang="EN-US"}[（空格符）、]{style="font-family:宋体"}[HT]{lang="EN-US"}[（水平制表符），以及]{style="font-family:宋体"}[ASCII]{lang="EN-US"}[码中小于等于]{style="font-family:宋体"}[31]{lang="EN-US"}[、大于等于]{style="font-family:宋体"}[127]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[rfc]{lang="EN-US"}**[ *rfc-type*]{lang="EN-US"}]{#struct_0_x7280_11703_423678625}[：]{style="font-family:宋体"}[RFC]{lang="EN-US"}[类型，即对]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文中]{style="font-family:宋体"}[URI]{lang="EN-US"}[所标识资源的执行方法。]{style="font-family:宋体"}*[rfc-type]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[CONNECET]{lang="EN-US"}**]{#struct_0_x7280_11703_423613089}[：]{lang="EN-US" style="font-family:宋体"}[保留。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[DELETE]{lang="EN-US"}**]{#struct_0_x7280_11703_423547553}[：请求删除]{style="font-family:
宋体"}[URI]{lang="EN-US"}[所标识的资源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[GET]{lang="EN-US"}**]{#struct_0_x7280_11703_423940769}[：请求获取]{style="font-family:
宋体"}[URI]{lang="EN-US"}[所标识的资源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[HEAD]{lang="EN-US"}**]{#struct_0_x7280_11703_423875233}[：请求获取]{style="font-family:
宋体"}[URI]{lang="EN-US"}[所标识资源的响应消息首部。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[OPTIONS]{lang="EN-US"}**]{#struct_0_x7280_11703_423809697}[：请求查询服务器支持的功能，即查询与]{style="font-family:
宋体"}[URI]{lang="EN-US"}[所标识资源相关的选项和需求。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[POST]{lang="EN-US"}**]{#struct_0_x7280_11703_423744161}[：在]{style="font-family:
宋体"}[URI]{lang="EN-US"}[所标识的资源后附加新数据。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[PUT]{lang="EN-US"}**]{#struct_0_x7280_11703_424137377}[：请求服务器存储一个资源，并用]{style="font-family:
宋体"}[URI]{lang="EN-US"}[作为其标识。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[TRACE]{lang="EN-US"}**]{#struct_0_x7280_11703_423678620}[：请求服务器回送收到的请求消息，主要用于测试或诊断。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423613084}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_423482012}[类型的负载均衡类视图下支持。]{style="font-family:宋体"}

[[需要注意的是，一个负载均衡类中最多允许创建]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x7280_11703_423940764}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_423875228}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_423809692}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中，创建匹配报文方法类型的匹配规则为扩展类型的]{style="font-family:宋体"}[user]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_424202908}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match method ext user]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_424137372}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中创建匹配报文方法类型的匹配规则为]{style="font-family:宋体"}[RFC]{lang="EN-US"}[类型的]{style="font-family:宋体"}**[CONNECT]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_423678619}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match method rfc CONNECT]{lang="EN-US"}
:::

::: {#-1145004972 .myid}
[]{#_Toc404796608}[]{#struct_0_x7280_11703_x693126642}[]{#_Toc334536495}[]{#_Toc329869236}[]{#_Toc327781455}[]{#_Toc317490832}[]{#_Toc382920927}

**负载均衡 \-- 负载均衡配置命令 \-- match source**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **source**]{lang="EN-US"}]{#struct_0_x7280_11703_960988933}[命令用来创建源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型的匹配规则。]{style="font-family:宋体"}[]{#_Toc382920928}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x1974838289}[命令用来删除指定的匹配规则。]{style="font-family:宋体"}[]{#_Toc382920929}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_499985285}[]{#_Toc382920930}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **source** { **ip** **address** *ipv4-address* \[ *mask-length* \| *mask* \] \| **ipv6** **address** *ipv6-address* \[ *prefix-length* \] }]{lang="EN-US"}]{#struct_0_x7280_11703_1847744777}[]{#_Toc382920931}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x550604528}[]{#_Toc382920932}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1052499876}[]{#_Toc382920933}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2064005771}[]{#_Toc382920934}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_920160206}[]{#_Toc382920935}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_960792325}[]{#_Toc382920936}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1798622786}[]{#_Toc382920937}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x194154692}[]{#_Toc382920938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2036594695}[]{#_Toc382920939}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_81409608}[]{#_Toc382920940}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_1246573801}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}[]{#_Toc382920941}

[]{#struct_0_x7280_11703_x1241566313}[]{#_Toc382920942}[]{#_Toc382920943}**[ip]{lang="EN-US"}**[ **address** ]{lang="EN-US"}*[ipv4-address]{lang="EN-US"}*[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}[]{#_Toc382920944}

[*[mask-lengh]{lang="EN-US"}*]{#struct_0_x7280_11703_960857861}[：子网]{style="font-family:宋体"}[掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc382920945}

[*[mask]{lang="EN-US"}*]{#struct_0_x7280_11703_x351017403}[：子网]{style="font-family:宋体"}[掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc382920946}

[**[ipv6]{lang="EN-US"}**[ **address** ]{lang="EN-US"}*[ipv6-address]{lang="EN-US"}*]{#struct_0_x7280_11703_x2068201112}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}[]{#_Toc382920947}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x7280_11703_1862937211}[：]{style="font-family:宋体"}[前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc382920948}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1677558499}[]{#_Toc382920949}

[[需要注意的是，一个负载均衡类中最多允许创建]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x7280_11703_x44068974}[条匹配规则。]{style="font-family:宋体"}[]{#_Toc382920950}

[]{#struct_0_x7280_11703_2083280141}[]{#_Toc382920951}[]{#_Toc382920952}[【举例】]{style="font-family:
黑体"}[]{#_Toc382920953}

[]{#_Toc334536496}[]{#_Toc329869237}[]{#_Toc327781456}[]{#_Toc317490831}[]{#struct_0_x7280_11703_1315929613}[]{#_Toc382920954}[]{#_Toc382920955}[]{#_Toc382920956}[]{#_Toc382920957}[\# ]{lang="EN-US"}[在通用类型的负载均衡类]{style="font-family:宋体"}[lbc1]{lang="EN-US"}[中，创建源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型的匹配规则为：匹配]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1/32]{lang="EN-US"}[。]{style="font-family:宋体"}[]{#_Toc382920958}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_495531068}[]{#_Toc382920959}

[\[Sysname\] loadbalance class lbc1 type generic[]{#_Toc382920960}]{lang="EN-US"}

[\[Sysname-lbc-generic-lbc1\] match source ip address 1.1.1.1]{lang="EN-US"}[]{#_Toc364842601}[]{#_Toc362006303}[]{#_Toc364794911}[]{#_Toc364842593}[]{#_Toc366144901}[]{#_Toc366152772}[]{#_Toc364794913}[]{#_Toc364842595}[]{#_Toc366144903}[]{#_Toc366152774}[]{#_Toc364794914}[]{#_Toc364842596}[]{#_Toc366144904}[]{#_Toc366152775}
:::

::: {#1214686309 .myid}
[]{#_Toc404796609}[]{#struct_0_x7280_11703_x1504992667}[]{#_Toc380504998}

**负载均衡 \-- 负载均衡配置命令 \-- match url**

------------------------------------------------------------------------

[**[match]{lang="EN-US"}**[ **url**]{lang="EN-US"}]{#struct_0_x7280_11703_x1504927131}[命令用来创建]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[类型的匹配规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **match**]{lang="EN-US"}]{#struct_0_x7280_11703_x1505058203}[命令用来在删除指定的匹配规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504730523}

[**[match]{lang="EN-US"}**[ \[ *match-id* \] **url** *url*]{lang="EN-US"}]{#struct_0_x7280_11703_x1504664987}

[**[undo]{lang="EN-US"}**[ **match** *match-id*]{lang="EN-US"}]{#struct_0_x7280_11703_x1504861595}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504468379}

[[负载均衡类中不存在任何匹配规则。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1504402843}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504992668}

[[负载均衡类视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1505123740}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1505058204}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1504730524}

[[mdc-admin ]{lang="EN-US"}]{#struct_0_x7280_11703_x1504861596}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504796060}

[*[match-id]{lang="EN-US"}*]{#struct_0_x7280_11703_x1504468380}[：匹配规则的编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果指定编号的匹配规则不存在，则创建一条新的匹配规则；如果指定编号的匹配规则已存在，则对其进行修改。如果未指定本参数，系统将自动分配一个可用的最小编号。]{style="font-family:宋体"}

[**[url]{lang="EN-US"}**[ *url*]{lang="EN-US"}]{#struct_0_x7280_11703_x1504992673}[：]{style="font-family:宋体"}[URL]{lang="EN-US"}[的正则表达式，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504927137}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1505123745}[类型的负载均衡类视图下支持。]{style="font-family:宋体"}

[[需要注意的是，一个负载均衡类中最多允许创建]{style="font-family:宋体"}[65535]{lang="EN-US"}]{#struct_0_x7280_11703_x1504730529}[条匹配规则。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1504664993}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1504861601}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡类]{style="font-family:宋体"}[lbc2]{lang="EN-US"}[中，创建]{style="font-family:宋体"}[HTTP URL]{lang="EN-US"}[类型的匹配规则为：]{style="font-family:宋体"}[.\*.html]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1504468385}

[\[Sysname\] loadbalance class lbc2 type http]{lang="EN-US"}

[\[Sysname-lbc-http-lbc2\] match url .\*.html]{lang="EN-US"}
:::

::: {#-929850886 .myid}
[]{#_Toc404796610}[]{#struct_0_x7280_11703_x1347874825}[]{#_Toc334536541}[]{#_Toc329869280}[]{#_Toc329242055}

**负载均衡 \-- 负载均衡配置命令 \-- parameter**

------------------------------------------------------------------------

[**[parameter]{lang="EN-US"}**]{#struct_0_x7280_11703_1427733975}[命令用来指定虚服务器引用的参数模板。]{style="font-family:宋体"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x7280_11703_x745041577}[ ]{lang="PT-BR"}**[parameter]{lang="PT-BR"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_718177539}

[**[parameter]{lang="PT-BR"}**]{#struct_0_x7280_11703_961251077}[ ]{lang="PT-BR"}[{ **http** \| ]{lang="EN-US"}**[ip]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **tcp** }]{lang="EN-US"}[ ]{lang="EN-US"}*[profile-name]{lang="PT-BR"}*

[**[undo]{lang="PT-BR"}**]{#struct_0_x7280_11703_x1741544794}[ ]{lang="PT-BR"}**[parameter]{lang="PT-BR"}**[ ]{lang="PT-BR"}[{ **http** \| ]{lang="EN-US"}**[ip]{lang="PT-BR"}**[ ]{lang="PT-BR"}[\| **tcp** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x796033216}

[[虚服务器没有引用任何参数模板。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x41564304}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2093583086}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_649589972}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_51782335}

[[network-admin]{lang="PT-BR"}]{#struct_0_x7280_11703_912103779}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x7280_11703_960661254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1769232405}

[[{ **http** \| **ip**\| **tcp** }]{lang="PT-BR"}]{#struct_0_x7280_11703_61091272}[：]{style="font-family:宋体"}[参数模板的类型]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[、]{style="font-family:宋体"}[IP]{lang="PT-BR"}[和]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[三种]{style="font-family:宋体"}[类型。其中，]{style="font-family:宋体"}**[http]{lang="PT-BR"}**[和]{style="font-family:宋体"}**[tcp]{lang="EN-US"}**[参数只在快速]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[和]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[类型的]{style="font-family:宋体"}[虚服务器视图下支持。]{style="font-family:宋体"}

[*[profile-name]{lang="PT-BR"}*]{#struct_0_x7280_11703_542653763}[：]{style="font-family:宋体"}[参数模板的名称]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:
宋体"}[63]{lang="PT-BR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1897091419}

[[参数模板用来对虚服务器上的流量进行比较深入的解析、处理和优化。虚服务器引用了参数模板后，就要根据该参数模板的配置对匹配流量进行相应的处理。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1549150160}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1171508182}

[[\# ]{lang="PT-BR"}]{#struct_0_x7280_11703_1023422993}[指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[引用]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_x7280_11703_960726790}

[\[Sysname\] virtual-server vs3 type ip]{lang="PT-BR"}

[\[Sysname-vs-ip-vs3\] parameter ip pp2]{lang="PT-BR"}
:::

::: {#950148200 .myid}
[]{#_Toc404796611}[]{#struct_0_x7280_11703_x589062268}[]{#_Toc334536471}[]{#_Toc329875703}[]{#_Toc329869216}[]{#_Toc326936441}

**负载均衡 \-- 负载均衡配置命令 \-- parameter-profile**

------------------------------------------------------------------------

[**[parameter-profile]{lang="EN-US"}**]{#struct_0_x7280_11703_x1364043059}[命令用来创建参数模板，并进入参数模板视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[parameter-profile]{lang="EN-US"}**]{#struct_0_x7280_11703_233257680}[命令用来删除指定的参数模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1993285511}

[**[parameter-profile]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_x1604667713}*[profile-name]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\[ **type** { **http** \| **ip** \| **tcp** } \]]{lang="EN-US"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[parameter-profile]{lang="EN-US"}**[ *profile-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x34461353}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x557933326}

[[不存在任何参数模板。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1034185442}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960530182}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1542305453}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1699027414}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1367865184}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x286898111}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_337551509}

[*[profile-name]{lang="PT-BR"}*]{#struct_0_x7280_11703_469994164}[：参数模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **http** \| **ip** \| **tcp** }]{lang="EN-US"}]{#struct_0_x7280_11703_1964232129}[：参数模板的类型，包括]{style="font-family:宋体"}[HTTP]{lang="PT-BR"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[和]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[三种]{style="font-family:宋体"}[类型。创建参数模板时必须指定本参数；而在进入已创建的参数模板视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1357890238}

[[通过配置参数模板可以进行一些高级参数的配置。这样，当参数模板被虚服务器引用之后，可以对虚服务器的业务流量进行更深入的解析、处理和优化。]{style="font-family:宋体"}]{#struct_0_x7280_11703_960595718}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1906614435}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x658901487}[创建]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp2]{lang="EN-US"}[，并进入参数模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1968275034}

[\[Sysname\] parameter-profile pp2 type ip]{lang="EN-US"}

[\[Sysname-para-ip-pp2\]]{lang="EN-US"}
:::

::: {#-1030704014 .myid}
[]{#_Toc404796612}[]{#struct_0_x7280_11703_61353417}[]{#_Toc380505001}[]{#_Toc364842607}[]{#_Toc362006252}

**负载均衡 \-- 负载均衡配置命令 \-- payload**

------------------------------------------------------------------------

[**[payload]{lang="EN-US"}**]{#struct_0_x7280_11703_61418953}[命令用于配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷持续性方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[payload]{lang="EN-US"}**]{#struct_0_x7280_11703_61287881}[命令用来删除]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷持续性方法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_61615561}

[**[payload]{lang="EN-US"}**[ \[ **offset** *offset* \] \[ **start** *start-string* \] \[ **end** *end-string* \| **length** *length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_61091268}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[payload]{lang="EN-US"}**]{#struct_0_x7280_11703_61156804}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_60960196}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_61353412}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_61418948}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_61287876}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_61615556}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_61091267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_61156803}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_60960195}

[**[offset]{lang="EN-US"}**[ *offset*]{lang="EN-US"}]{#struct_0_x7280_11703_61353411}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷基于]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的偏移量，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[start]{lang="EN-US"}**[ *start-string*]{lang="EN-US"}]{#struct_0_x7280_11703_61418947}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷开始标记的正则表达式，即从]{style="font-family:宋体"}*[offset]{lang="EN-US"}*[起到本标记为开始，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[end]{lang="EN-US"}**[ *end-string*]{lang="EN-US"}]{#struct_0_x7280_11703_61287875}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷结束标记的正则表达式，即从]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[起到本标记为结束，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *length*]{lang="EN-US"}]{#struct_0_x7280_11703_61615555}[：]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷的长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示所有长度。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_61681091}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x342127719}[载荷类型的持续性组视图下支持。]{style="font-family:宋体"}

[[本命令用来根据]{style="font-family:宋体"}*[offset]{lang="EN-US"}*]{#struct_0_x7280_11703_x342324327}[、]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[、]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[及]{style="font-family:宋体"}*[length]{lang="EN-US"}*[获取生成持续性表项的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷信息。]{style="font-family:宋体"}*[start-string]{lang="EN-US"}*[和]{style="font-family:宋体"}*[end-string]{lang="EN-US"}*[将不计入持续性表项信息中。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x341931111}[类型的虚服务器不支持引用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷持续性方法。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x341865575}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x341996647}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷类型的持续性组]{style="font-family:宋体"}[sg5]{lang="EN-US"}[中，配置]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷持续性方法为：从]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[报文起始位置的第]{style="font-family:宋体"}[10]{lang="EN-US"}[个字节起，长度为]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷来生成持续性表项。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x341668967}

[\[Sysname\] sticky-group sg5 type payload]{lang="EN-US"}

[\[Sysname-sticky-payload-sg5\] payload offset 10 length 20]{lang="EN-US"}
:::

::: {#749718499 .myid}
[]{#_Toc334536506}[]{#_Toc329869247}[]{#_Toc327781459}[]{#_Toc317490861}[]{#_Toc404796613}[]{#struct_0_x7280_11703_1053727506}[]{#_Toc334536514}[]{#_Toc329869255}[]{#_Toc329241937}

**负载均衡 \-- 负载均衡配置命令 \-- port (real server view)**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_x7280_11703_2040394867}[命令用来配置实服务器的端口号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_x7280_11703_x689478588}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_316842009}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x7280_11703_960923398}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_x7280_11703_1971899680}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1828067988}

[[实服务器的端口号为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_x2098151619}[（表示继续使用原报文携带的端口号）。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x855589505}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1920261465}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1534191755}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_486711395}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_960988934}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1974838288}

[*[port-number]{lang="EN-US"}*]{#struct_0_x7280_11703_2066069226}[：端口号，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示继续使用原报文携带的端口号。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2142169328}

[[需要注意的是，只有当实服务组开启了]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_557257127}[功能后，本配置才有效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1640148945}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x363927406}[配置]{style="font-family:宋体"}[实服务器]{style="font-family:宋体"}[rs]{lang="PT-BR"}[的端口号为]{style="font-family:宋体"}[8080]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1989104102}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] port 8080]{lang="EN-US"}

[]{#_Toc334536533}[]{#_Toc329869272}[]{#_Toc329242044}[]{#_Toc320886174}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_960792326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[transparent]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1798622789}
:::

::: {#376782950 .myid}
[]{#_Toc404796614}[]{#struct_0_x7280_11703_x193695940}

**负载均衡 \-- 负载均衡配置命令 \-- port (virtual server view)**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_x7280_11703_x140213188}[命令用来配置虚服务器的端口号。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_x7280_11703_x1717003255}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2108131932}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1741671762}

[**[undo]{lang="EN-US"}**[ **port**]{lang="EN-US"}]{#struct_0_x7280_11703_x973293528}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1872267658}

[[IP/TCP/UDP]{lang="EN-US"}]{#struct_0_x7280_11703_960857862}[类型]{style="font-family:宋体"}[虚服务器的端口号为]{style="font-family:宋体"}[0]{lang="EN-US"}[（]{style="font-family:宋体"}[表示任意端口号），快速]{style="font-family:
宋体"}[HTTP/HTTP]{lang="EN-US"}[类型虚服务器的端口号为]{style="font-family:
宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x351017400}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2068004504}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_294207809}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x203760602}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_741470597}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1411467430}

[*[port-number]{lang="EN-US"}*]{#struct_0_x7280_11703_x1069385411}[：端口号。对于]{style="font-family:宋体"}[IP/TCP/UDP]{lang="EN-US"}[类型的虚服务器，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示任意端口号；对于快速]{style="font-family:
宋体"}[HTTP/HTTP]{lang="EN-US"}[类型的虚服务器，取值范围为]{style="font-family:
宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x494480741}

[[需要注意的是，如果虚服务器引用了]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_x494415205}[策略，则必须为其配置一个非缺省端口号（通常用]{style="font-family:宋体"}[443]{lang="EN-US"}[）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x278607870}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_961185542}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的端口号为]{style="font-family:宋体"}[8080]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x45973113}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] port 8080]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1519483914}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssl-server-policy]{lang="EN-US"}**]{#struct_0_x7280_11703_x617442964}
:::

::: {#-47397540 .myid}
[]{#_Toc404796615}[]{#struct_0_x7280_11703_1315929620}[]{#_Toc334536482}

**负载均衡 \-- 负载均衡配置命令 \-- predictor**

------------------------------------------------------------------------

[**[predictor]{lang="EN-US"}**]{#struct_0_x7280_11703_495596601}[命令用来配置实服务组的调度算法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **predictor**]{lang="EN-US"}]{#struct_0_x7280_11703_x1690479838}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_685390302}

[**[predictor]{lang="EN-US"}**[ **hash** **address** { **destination** \| **source** \| **source-ip-port** } \[ **mask** *mask-length* \] \[ **prefix** *prefix-length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x2147440032}

[**[predictor]{lang="EN-US"}**[ { **least-connection** \| **random** \| **round-robin** }]{lang="EN-US"}]{#struct_0_x7280_11703_961251078}

[**[undo]{lang="EN-US"}**[ **predictor**]{lang="EN-US"}]{#struct_0_x7280_11703_x1741544799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x36518329}

[[实服务组的调度算法为加权轮转算法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x466780533}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2090000022}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x46299419}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1059130338}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1989924655}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2132297916}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411991738}

[**[hash]{lang="EN-US"}**[ **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x1111147646}[：根据]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法。]{style="font-family:宋体"}

[**[destination]{lang="EN-US"}**]{#struct_0_x7280_11703_796241863}[：根据目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法。]{style="font-family:宋体"}

[**[source]{lang="EN-US"}**]{#struct_0_x7280_11703_x1576561529}[：根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址进行的哈希算法。]{style="font-family:宋体"}

[**[source-ip-port]{lang="EN-US"}**]{#struct_0_x7280_11703_411580885}[：根据源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号进行的哈希算法。]{style="font-family:宋体"}

[**[mask]{lang="EN-US"}**[ *mask-length*]{lang="EN-US"}]{#struct_0_x7280_11703_692032399}[：哈希算法中]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix-length*]{lang="EN-US"}]{#struct_0_x7280_11703_x342324332}[：哈希算法中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[least-connection]{lang="EN-US"}**]{#struct_0_x7280_11703_x128617584}[：加权最小连接算法，即总是把新连接分发给加权活动连接数（当前活动连接数]{style="font-family:宋体"}[/]{lang="EN-US"}[权值）最小的实服务。]{style="font-family:宋体"}

[**[random]{lang="EN-US"}**]{#struct_0_x7280_11703_x797143801}[：随机算法，即把新连接随机分发给每个实服务器。]{style="font-family:宋体"}

[**[round-robin]{lang="EN-US"}**]{#struct_0_x7280_11703_1891157968}[：加权轮转算法，即根据实服务权值的大小把新连接依次分发给每个实服务器，权值越大，分配的新连接越多。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411926202}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1926480462}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的调度算法为随机算法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1043084122}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] predictor random]{lang="EN-US"}
:::

::: {#567732879 .myid}
[]{#_Toc404796616}[]{#struct_0_x7280_11703_x445025940}[]{#_Toc334536516}[]{#_Toc329869257}[]{#_Toc329241939}

**负载均衡 \-- 负载均衡配置命令 \-- priority**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_x7280_11703_749908629}[命令用来配置实服务器的调用优先级。]{style="font-family:宋体"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x7280_11703_x1852561308}[ **priority**]{lang="PT-BR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_81572511}

[**[priority]{lang="PT-BR"}**]{#struct_0_x7280_11703_x1412122810}[ *priority-value*]{lang="PT-BR"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x7280_11703_x1724011681}[ **priority**]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2105770624}

[[实服务器的调用优先级为]{style="font-family:宋体"}]{#struct_0_x7280_11703_143983456}[4]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1236877741}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_724481606}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_88305592}

[[network-admin]{lang="PT-BR"}]{#struct_0_x7280_11703_1628714591}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x7280_11703_x608149223}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1412057274}

[*[priority-value]{lang="PT-BR"}*]{#struct_0_x7280_11703_x382535746}[：]{style="font-family:宋体"}[优先级]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[8]{lang="PT-BR"}[。]{style="font-family:
宋体"}[数值越大]{style="font-family:宋体"}[，越被优先调用]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_334072790}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1420299152}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的调用优先级为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1654739689}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] priority 3]{lang="EN-US"}
:::

::: {#52830313 .myid}
[]{#_Toc404796617}[]{#struct_0_x7280_11703_1299670164}[]{#_Toc334536524}

**负载均衡 \-- 负载均衡配置命令 \-- probe (real server view)**

------------------------------------------------------------------------

[**[probe]{lang="EN-US"}**]{#struct_0_x7280_11703_x1284286363}[命令用来指定实服务器的健康检测方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **probe**]{lang="EN-US"}]{#struct_0_x7280_11703_x2023977135}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411729594}

[**[probe]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1714346263}

[**[undo]{lang="EN-US"}**[ **probe** *template-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1428090495}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x495504425}

[[没有指定实服务器的健康检测方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1153173392}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1834273956}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1828927157}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_674872867}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1144927712}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411664058}

[[【参数】]{style="font-family:
黑体"}]{#struct_0_x7280_11703_2633842}

[*[template-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1039330859}[：健康检测方法所使用的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x110815941}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x341668972}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请使用]{style="font-family:宋体"}]{#struct_0_x7280_11703_948318446}**[nqa]{lang="EN-US"}**[ **template**]{lang="EN-US"}[命令创建健康检测方法所使用的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，通过健康检测可以对实服务器进行检测，保证其能够提供有效的服务。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1390323330}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1954530551}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1411860666}[创建]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板]{style="font-family:宋体"}[t4]{lang="EN-US"}[，并将其指定为实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的健康检测方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_260469962}

[\[Sysname\] nqa template icmp t4]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-t4\] quit]{lang="EN-US"}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] [probe t4]{.TerminalDisplayChar}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1283903201}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa]{lang="EN-US"}**[ **template**]{lang="EN-US"}]{#struct_0_x7280_11703_x429180849}[（网络管理和监控命令参考]{lang="EN-US" style="font-family:宋体"}[/NQA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[success-criteria]{lang="EN-US"}**]{#struct_0_x7280_11703_x1717632815}[ ]{lang="EN-US"}[(real server view)]{lang="EN-US"}
:::

::: {#1648602270 .myid}
[]{#_Toc404796618}[]{#struct_0_x7280_11703_x700728529}[]{#_Toc334536488}

**负载均衡 \-- 负载均衡配置命令 \-- probe (server farm view)**

------------------------------------------------------------------------

[**[probe]{lang="EN-US"}**]{#struct_0_x7280_11703_743020122}[命令用来指定实服务组的健康检测方法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **probe**]{lang="EN-US"}]{#struct_0_x7280_11703_1371309754}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411795130}

[**[probe]{lang="EN-US"}**[ *template-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x919103824}

[**[undo]{lang="EN-US"}**[ **probe** *template-name*]{lang="EN-US"}]{#struct_0_x7280_11703_867529799}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1971099103}

[[没有指定实服务组的健康检测方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x128181356}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_736916845}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x679242420}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2075519760}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1247285048}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411467450}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x492336234}

[*[template-name]{lang="EN-US"}*]{#struct_0_x7280_11703_538578685}[：健康检测方法所使用的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1706143672}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1224152829}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[请使用]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1774479658}**[nqa]{lang="EN-US"}**[ **template**]{lang="EN-US"}[命令创建健康检测方法所使用的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板，通过健康检测可以对实服务器进行检测，保证其能够提供有效的服务。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x561362353}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1884026317}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1411401914}[创建]{style="font-family:宋体"}[ICMP]{lang="EN-US"}[类型的]{style="font-family:宋体"}[NQA]{lang="EN-US"}[模板]{style="font-family:宋体"}[t4]{lang="EN-US"}[，并将其指定为实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的健康检测方法。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x7280_11703_718769633}

[\[Sysname\] nqa template icmp t4]{lang="EN-US"}

[\[Sysname-nqatplt-icmp-t4\] quit]{lang="EN-US"}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] [probe t4]{.TerminalDisplayChar}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1805534717}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nqa]{lang="EN-US"}**[ **template**]{lang="EN-US"}]{#struct_0_x7280_11703_x1889208908}[（网络管理和监控命令参考]{lang="EN-US" style="font-family:宋体"}[/NQA]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:
Symbol"}]{.TerminalDisplayChar}**[success-criteria]{lang="EN-US"}**]{#struct_0_x7280_11703_x137004847}[ ]{lang="EN-US"}[(server farm view)]{lang="EN-US"}
:::

::: {#-981046846 .myid}
[]{#_Toc323399352}[]{#_Toc404796619}[]{#struct_0_x7280_11703_148262322}[]{#_Toc334536522}[]{#_Toc329869263}[]{#_Toc329241948}[]{#_Toc370375624}[]{#_Toc370383888}[]{#_Toc370375625}[]{#_Toc370383889}[]{#_Toc370375626}[]{#_Toc370383890}[]{#_Toc370375627}[]{#_Toc370383891}[]{#_Toc370375628}[]{#_Toc370383892}[]{#_Toc370375629}[]{#_Toc370383893}[]{#_Toc370375630}[]{#_Toc370383894}[]{#_Toc370375631}[]{#_Toc370383895}[]{#_Toc370375632}[]{#_Toc370383896}[]{#_Toc370375633}[]{#_Toc370383897}[]{#_Toc370375634}[]{#_Toc370383898}[]{#_Toc370375635}[]{#_Toc370383899}[]{#_Toc370375636}[]{#_Toc370383900}[]{#_Toc370375637}[]{#_Toc370383901}[]{#_Toc370375638}[]{#_Toc370383902}[]{#_Toc370375639}[]{#_Toc370383903}[]{#_Toc370375640}[]{#_Toc370383904}[]{#_Toc370375641}[]{#_Toc370383905}[]{#_Toc370375642}[]{#_Toc370383906}[]{#_Toc370375643}[]{#_Toc370383907}[]{#_Toc370375644}[]{#_Toc370383908}[]{#_Toc370375645}[]{#_Toc370383909}[]{#_Toc370375646}[]{#_Toc370383910}[]{#_Toc370375647}[]{#_Toc370383911}[]{#_Toc370375648}[]{#_Toc370383912}[]{#_Toc370375649}[]{#_Toc370383913}[]{#_Toc370375650}[]{#_Toc370383914}[]{#_Toc370375651}[]{#_Toc370383915}[]{#_Toc370375652}[]{#_Toc370383916}[]{#_Toc370375653}[]{#_Toc370383917}[]{#_Toc370375654}[]{#_Toc370383918}[]{#_Toc370375655}[]{#_Toc370383919}[]{#_Toc370375656}[]{#_Toc370383920}[]{#_Toc370375657}[]{#_Toc370383921}[]{#_Toc370375658}[]{#_Toc370383922}[]{#_Toc370375659}[]{#_Toc370383923}[]{#_Toc370375660}[]{#_Toc370383924}[]{#_Toc370375661}[]{#_Toc370383925}[]{#_Toc370375662}[]{#_Toc370383926}[]{#_Toc370375663}[]{#_Toc370383927}[]{#_Toc370375664}[]{#_Toc370383928}[]{#_Toc370375665}[]{#_Toc370383929}

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit bandwidth (real server view)**

------------------------------------------------------------------------

[**[rate-limit]{lang="EN-US"}**[ **bandwidth**]{lang="EN-US"}]{#struct_0_x7280_11703_x362937709}[命令用来配置实服务器所允许的最大带宽。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rate-limit** **bandwidth**]{lang="EN-US"}]{#struct_0_x7280_11703_x1903734298}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_107561454}

[**[rate-limit]{lang="EN-US"}**[ **bandwidth** \[ **inbound** \| **outbound** \] *bandwidth-value*]{lang="EN-US"}]{#struct_0_x7280_11703_1981744941}

[**[undo]{lang="EN-US"}**[ **rate-limit** **bandwidth** \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_x7280_11703_1529563521}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411664057}

[[实服务器所允许的最大总带宽、最大入带宽和最大出带宽均为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_x1919680459}[千]{style="font-family:宋体"}[字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1912274990}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_15664742}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1701713527}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1942966549}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x349848776}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1633438041}

[**[inbound]{lang="EN-US"}**]{#struct_0_x7280_11703_x494415204}[：配置最大入带宽。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x7280_11703_x1519549450}[：配置最大出带宽。]{style="font-family:宋体"}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x7280_11703_x289636960}[：最大带宽值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒，]{style="font-family:宋体"}[0]{lang="EN-US"}[千]{style="font-family:宋体"}[字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒表示最大带宽不受限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_103261455}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[inbound]{lang="EN-US"}**]{#struct_0_x7280_11703_x8633752}[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[参数，则配置最大总带宽，总带宽等于入带宽与出带宽之和。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411860665}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1305613979}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[所允许的最大总带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x278330160}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] rate-limit bandwidth 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x494349668}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[所允许的最大入带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_868158551}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] rate-limit bandwidth inbound 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_317373}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[所允许的最大出带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x2078328307}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] rate-limit bandwidth outbound 1]{lang="EN-US"}
:::

::: {#1822919729 .myid}
[]{#_Toc404796620}[]{#struct_0_x7280_11703_x783810012}[]{#_Toc334536539}[]{#_Toc329869278}[]{#_Toc329242051}

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit bandwidth (virtual server view)**

------------------------------------------------------------------------

[**[rate-limit]{lang="EN-US"}**[ **bandwidth**]{lang="EN-US"}]{#struct_0_x7280_11703_x1878899346}[命令用来配置虚服务器所允许的最大带宽。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rate-limit** **bandwidth**]{lang="EN-US"}]{#struct_0_x7280_11703_x448890852}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1515983309}

[**[rate-limit]{lang="EN-US"}**[ **bandwidth** \[ **inbound** \| **outbound** \] *bandwidth-value*]{lang="EN-US"}]{#struct_0_x7280_11703_5744172}

[**[undo]{lang="EN-US"}**[ **rate-limit** **bandwidth** \[ **inbound** \| **outbound** \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1411795129}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2128891869}

[[虚服务器所允许的最大总带宽、最大入带宽和最大出带宽均为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_x1360270108}[千]{style="font-family:宋体"}[字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1781521729}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2136020117}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1964712670}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_975977640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1764919093}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_871244398}

[**[inbound]{lang="EN-US"}**]{#struct_0_x7280_11703_2141102690}[：最大入带宽。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x7280_11703_x2081010235}[：最大出带宽。]{style="font-family:宋体"}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x7280_11703_x1411467449}[：最大带宽值，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒，]{style="font-family:宋体"}[0]{lang="EN-US"}[千]{style="font-family:宋体"}[字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒表示最大带宽不受限制。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1800367864}

[[需要注意的是，如果未指定]{style="font-family:宋体"}**[inbound]{lang="EN-US"}**]{#struct_0_x7280_11703_x1993768484}[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[参数，则配置最大总带宽，总带宽等于入带宽与出带宽之和。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1429912531}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x870310930}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所允许的最大总带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千]{style="font-family:宋体"}[字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1222640161}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] rate-limit bandwidth 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_2141299298}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所允许的最大入带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1386524529}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] rate-limit bandwidth inbound 1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_586585570}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所允许的最大出带宽为]{style="font-family:宋体"}[1]{lang="EN-US"}[千字节]{style="font-family:宋体"}[/]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x12875673}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] rate-limit bandwidth outbound 1]{lang="EN-US"}
:::

::: {#-947195117 .myid}
[]{#_Toc404796621}[]{#struct_0_x7280_11703_1627206552}[]{#_Toc334536521}[]{#_Toc329869262}[]{#_Toc329241947}[]{#_Toc324941104}[]{#_Toc318725186}

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit connection (real server view)**

------------------------------------------------------------------------

[**[rate-limit]{lang="EN-US"}**[ **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_360336112}[命令用来配置实服务器所允许的每秒最大连接数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rate-limit** **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_478187427}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411401913}

[**[rate-limit]{lang="EN-US"}**[ **connection** *connection-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1122054160}

[**[undo]{lang="EN-US"}**[ **rate-limit** **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_x771726982}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x326517173}

[[实服务器所允许的每秒最大连接数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_x773747551}[，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x497727061}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1250845983}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1960074972}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2027824701}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411991740}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1467181398}

[*[connection-number]{lang="EN-US"}*]{#struct_0_x7280_11703_700632976}[：每秒最大连接数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示实服务器所允许的每秒最大连接数不受限制。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1768742024}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1843792665}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[所允许的每秒最大连接数为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1575641202}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] rate-limit connection 10000]{lang="EN-US"}
:::

::: {#-1034202522 .myid}
[]{#_Toc404796622}[]{#struct_0_x7280_11703_x1602174935}[]{#_Toc334536538}[]{#_Toc329869277}[]{#_Toc329242050}

**负载均衡 \-- 负载均衡配置命令 \-- rate-limit connection (virtual server view)**

------------------------------------------------------------------------

[**[rate-limit]{lang="EN-US"}**[ **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_x835789746}[命令用来配置虚服务器所允许的每秒最大连接数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **rate-limit** **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_x1411926204}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_763681048}

[**[rate-limit]{lang="EN-US"}**[ **connection** *connection-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1615002772}

[**[undo]{lang="EN-US"}**[ **rate-limit** **connection**]{lang="EN-US"}]{#struct_0_x7280_11703_x704439307}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_88214228}

[[虚服务器所允许的每秒最大连接数为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x7280_11703_x797700578}[，即不受限制。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1159276104}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_626485681}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_949809906}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1412122812}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1408156201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1357647105}

[*[connection-number]{lang="EN-US"}*]{#struct_0_x7280_11703_1471149202}[：每秒最大连接数，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示虚服务器所允许的每秒最大连接数不受限制。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2010782581}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1152323399}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所允许的每秒最大连接数为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x914962596}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] rate-limit connection 10000]{lang="EN-US"}
:::

::: {#1878925033 .myid}
[]{#_Toc404796623}[]{#struct_0_x7280_11703_x778638891}[]{#_Toc334536510}[]{#_Toc329869251}[]{#_Toc329241933}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc318725173}

**负载均衡 \-- 负载均衡配置命令 \-- real-server**

------------------------------------------------------------------------

[**[real-server]{lang="EN-US"}**]{#struct_0_x7280_11703_x1412057276}[命令用来创建实服务器，并进入实服务器视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **real-server**]{lang="EN-US"}]{#struct_0_x7280_11703_x1545335160}[命令用来删除指定的实服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1342100299}

[**[real-server]{lang="EN-US"}**[ *real-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x812956752}

[**[undo]{lang="EN-US"}**[ **real-server** *real-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_343718965}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1762050884}

[[不存在任何实服务器。]{style="font-family:宋体"}]{#struct_0_x7280_11703_20563198}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_987776301}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_418432842}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411729596}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_551546849}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1581409931}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1236059989}

[*[real-server-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1785539116}[：实服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1142757559}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x252183437}[创建实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[，并进入实服务器视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1411664060}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\]]{lang="EN-US"}
:::

::: {#894045468 .myid}
[]{#_Toc404796624}[]{#struct_0_x7280_11703_820737230}[]{#_Toc380505013}[]{#_Toc364842622}[]{#_Toc362006267}[]{#_Toc347413210}

**负载均衡 \-- 负载均衡配置命令 \-- rebalance per-request**

------------------------------------------------------------------------

[**[rebalance]{lang="EN-US"}**[ **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_821130446}[命令用来配置对每个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文都进行负载均衡。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[rebalance]{lang="EN-US"}**[ **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_821195982}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820671697}

[**[rebalance]{lang="EN-US"}**[ **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_820540625}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[rebalance]{lang="EN-US"}**[ **per-request**]{lang="EN-US"}]{#struct_0_x7280_11703_820868305}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820802769}

[[只对一条连接的第一个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_821130449}[请求报文进行负载均衡，其余请求报文的处理方式与第一个相同。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820606160}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_820475088}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820540624}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_820933840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_820737232}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_821130448}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_820606155}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820671691}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_820540619}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，配]{style="font-family:宋体"}[置对每个]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[请求报文]{style="font-family:宋体"}[都]{style="font-family:宋体"}[进行负载均衡]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_820933835}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] rebalance per-request]{lang="EN-US"}
:::

::: {#-2078257291 .myid}
[]{#_Toc404796625}[]{#struct_0_x7280_11703_820737227}[]{#_Toc380505014}[]{#_Toc364842623}[]{#_Toc362006355}[]{#_Toc347413293}[]{#_Toc318725399}

**负载均衡 \-- 负载均衡配置命令 \-- redirect relocation**

------------------------------------------------------------------------

[**[redirect]{lang="EN-US"}**[ **relocation**]{lang="EN-US"}]{#struct_0_x7280_11703_821130443}[命令]{style="font-family:宋体"}[用来开启虚服务器的重定向功能并指定重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **redirect** **relocation**]{lang="EN-US"}]{#struct_0_x7280_11703_820606154}[命令]{style="font-family:宋体"}[用来关闭虚服务器的重定向功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820671690}

[**[redirect]{lang="EN-US"}**[ **relocation** ]{lang="EN-US"}*[relocation]{lang="EN-US"}*]{#struct_0_x7280_11703_820540618}

[**[undo]{lang="EN-US"}**[ **redirect** **relocation**]{lang="EN-US"}]{#struct_0_x7280_11703_820868298}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_820737226}

[[虚服务器的重定向功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_821130442}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_821195978}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1908211660}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908342732}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1907949516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1908146124}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907752908}

[*[relocation]{lang="EN-US"}*]{#struct_0_x7280_11703_x1908277197}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[，开启了虚服务器的重定向功能后，所有匹配该虚服务器的请求报文都将被重定向到该]{style="font-family:宋体"}[URL]{lang="EN-US"}[。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。也可以使用以下特定含义的字符串（各自只允许使用一次）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[%h]{lang="EN-US"}]{#struct_0_x7280_11703_x1908211661}[：使用客户端请求报文中的主机名。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[%p]{lang="EN-US"}]{#struct_0_x7280_11703_x1908342733}[：使用客户端请求报文中的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908015053}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1908146125}[类型的虚服务器视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907752909}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1907687373}[开启]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs2]{lang="EN-US"}[的重定向功能，并指定重定向]{style="font-family:宋体"}[URL]{lang="EN-US"}[为客户端请求报文中的主机名和]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1908211658}

[\[Sysname\] virtual-server vs2 type http]{lang="EN-US"}

[\[Sysname-vs-http-vs2\] redirect relocation %h%p]{lang="EN-US"}
:::

::: {#-1698586902 .myid}
[]{#_Toc404796626}[]{#struct_0_x7280_11703_x1908342730}[]{#_Toc380505015}[]{#_Toc364842624}[]{#_Toc362006356}

**负载均衡 \-- 负载均衡配置命令 \-- redirect return-code**

------------------------------------------------------------------------

[**[redirect]{lang="EN-US"}**[ **return-code**]{lang="EN-US"}]{#struct_0_x7280_11703_x1908015050}[命令用来配置负载均衡设备返回给客户端的重定向报文中的状态码。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **redirect** **return-code**]{lang="EN-US"}]{#struct_0_x7280_11703_x1908146122}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907752906}

[**[redirect]{lang="EN-US"}**[ **return-code** {]{lang="EN-US"}[ **301** \| **302** }]{lang="EN-US"}]{#struct_0_x7280_11703_x1907687370}

[**[undo]{lang="EN-US"}**[ **redirect** **return-code**]{lang="EN-US"}]{#struct_0_x7280_11703_x1908211659}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908342731}

[[负载均衡设备返回给客户端的重定向报文中的状态码为]{style="font-family:宋体"}[302]{lang="EN-US"}]{#struct_0_x7280_11703_x1908015051}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908146123}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1908080587}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907687371}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1908211664}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1908408272}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908015056}

[**[301]{lang="EN-US"}**]{#struct_0_x7280_11703_x1908146128}[：]{style="font-family:宋体"}[状态码为]{style="font-family:宋体"}[301]{lang="EN-US"}[，表示永久删除被请求的资源。]{style="font-family:宋体"}

[**[302]{lang="EN-US"}**]{#struct_0_x7280_11703_x1908080592}[：]{style="font-family:宋体"}[状态码为]{style="font-family:宋体"}[302]{lang="EN-US"}[，表示临时删除被请求的资源。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907687376}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1908211665}[类型的虚服务器视图下支持。]{style="font-family:宋体"}

[[需要注意的是，本命令只有在开启了虚服务器的重定向功能后才会生效。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1908408273}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1908015057}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1908146129}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs2]{lang="EN-US"}[上，配置负载均衡设备返回给客户端的重定向报文中的状态码为]{style="font-family:宋体"}[301]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1908080593}

[\[Sysname\] virtual-server vs2 type http]{lang="EN-US"}

[\[Sysname-vs-http-vs2\] redirect return-code 301]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1907687377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redirect]{lang="EN-US"}**[ **relocation**]{lang="EN-US"}]{#struct_0_x7280_11703_1983471109}
:::

::::: {#-680229659 .myid}
[]{#_Toc404796627}[]{#struct_0_x7280_11703_1008249323}[]{#_Toc400807574}[]{#_Toc396740869}

**负载均衡 \-- 负载均衡配置命令 \-- reset loadbalance hot-backup statistics**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](负载均衡命令.files/image001.png){border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7280_11703_x1720634032}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[集中式设备不支持本命令，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7280_11703_x2125534627}
:::

**[ ]{lang="EN-US"}**

[**[reset]{lang="EN-US"}**[ **loadbalance** **hot-backup** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_x2049037701}[命令用来]{style="font-family:宋体"}[清除负载均衡双机热备的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1202926163}

[**[reset]{lang="EN-US"}**[ **loadbalance** **hot-backup** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_x1209791493}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1500715346}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_821665310}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x143540069}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x276164303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x154550091}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_504558195}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x950097961}[清除负载均衡双机热备的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset loadbalance hot-backup statistics]{lang="EN-US"}]{#struct_0_x7280_11703_x614219418}
:::::

::: {#-1595624442 .myid}
[]{#_Toc404796628}[]{#struct_0_x7280_11703_x353530982}[]{#_Toc334536523}[]{#_Toc329869264}[]{#_Toc329241943}

**负载均衡 \-- 负载均衡配置命令 \-- reset real-server statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **real-server** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_1309536882}[命令用来]{style="font-family:宋体"}[清除实服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x325907323}

[**[reset]{lang="EN-US"}**[ **real-server** **statistics** \[ *real-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x250770144}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1911295320}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1561769663}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_899818279}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_754157862}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411860668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x546099092}

[*[real-server-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x2033309227}[：清除指定实服务器的统计信息。]{style="font-family:宋体"}*[real-server-name]{lang="EN-US"}*[为实服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将清除所有实服务器的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1646018659}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_766830770}[清除所有实服务器的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset real-server statistics]{lang="EN-US"}]{#struct_0_x7280_11703_x1603376607}

[]{#_Toc329869265}[]{#_Toc329241944}[]{#_Toc334536542}[]{#_Toc329869281}[]{#_Toc329242048}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1726549144}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **real-server** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_429228041}
:::

::: {#1457733096 .myid}
[]{#_Toc404796629}[]{#struct_0_x7280_11703_x1642314771}

**负载均衡 \-- 负载均衡配置命令 \-- reset virtual-server statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **virtual-server** **statistics**]{lang="EN-US"}]{#struct_0_x7280_11703_x1411795132}[命令用来]{style="font-family:宋体"}[清除虚服务器的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2081903238}

[**[reset]{lang="EN-US"}**[ **virtual-server** **statistics** \[ *virtual-server-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x840940826}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2144014769}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x395877137}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_373332805}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1238741258}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1384472540}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1507771574}

[*[virtual-server-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1411467452}[：清除指定虚服务器的统计信息。]{style="font-family:宋体"}*[virtual-server-name]{lang="EN-US"}*[为虚服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。如果未指定本参数，将清除所有虚服务器的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1655135648}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1869031156}[清除所有虚服务器的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset virtual-server statistics]{lang="EN-US"}]{#struct_0_x7280_11703_1748007499}

[]{#_Toc334536483}[]{#_Toc329869227}[]{#_Toc329781853}[]{#_Toc318725160}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1870267193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_391080792}**[virtual]{lang="EN-US"}[-server]{lang="EN-US"}**[ **statistics**]{lang="EN-US"}
:::

::: {#1825081227 .myid}
[]{#_Toc404796630}[]{#struct_0_x7280_11703_1983274500}[]{#_Toc380505018}[]{#_Toc364842627}[]{#_Toc362006273}[]{#_Toc354047347}[]{#_Toc318725271}

**负载均衡 \-- 负载均衡配置命令 \-- secondary-cookie delimiters**

------------------------------------------------------------------------

[**[secondary-cookie]{lang="EN-US"}**[ **delimiters**]{lang="EN-US"}]{#struct_0_x7280_11703_1983667716}[命令用来配置]{style="font-family:宋体"}[URL]{lang="EN-US"}[中分隔]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[的字符。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[secondary-cookie]{lang="EN-US"}**[ **delimiters**]{lang="EN-US"}]{#struct_0_x7280_11703_1983733252}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983602180}

[**[secondary-cookie]{lang="EN-US"}**[ **delimiters** *text*]{lang="EN-US"}]{#struct_0_x7280_11703_1983995396}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[secondary-cookie]{lang="EN-US"}**[ **delimiters**]{lang="EN-US"}]{#struct_0_x7280_11703_1983471111}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983274503}

[[URL]{lang="FR"}]{#struct_0_x7280_11703_1983667719}[中分隔]{style="font-family:宋体"}[Secondary Cookie]{lang="FR"}[的字符为]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="FR"}["、"]{style="font-family:宋体"}[&]{lang="FR"}["、"]{style="font-family:宋体"}[\#]{lang="FR"}["或"]{style="font-family:
宋体"}[+]{lang="FR"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983536647}

[[参数模板]{style="font-family:宋体"}]{#struct_0_x7280_11703_1983602183}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983995399}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1983471110}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1983274502}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983667718}

[*[text]{lang="FR"}*]{#struct_0_x7280_11703_1983536646}[：]{style="font-family:宋体"}[分隔字符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[4]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}[!]{lang="FR"}[、]{style="font-family:宋体"}[\"]{lang="FR"}[、]{style="font-family:宋体"}[\#]{lang="FR"}[、]{style="font-family:
宋体"}[;]{lang="FR"}[、]{style="font-family:宋体"}[\<]{lang="FR"}[、]{style="font-family:宋体"}[\>]{lang="FR"}[、]{style="font-family:宋体"}[?]{lang="FR"}[、]{style="font-family:
宋体"}[\[]{lang="FR"}[、]{style="font-family:宋体"}[\\]{lang="FR"}[、]{style="font-family:宋体"}[\]]{lang="FR"}[、]{style="font-family:宋体"}[\^]{lang="FR"}[、]{style="font-family:
宋体"}[\`]{lang="FR"}[、]{style="font-family:宋体"}[\|]{lang="FR"}[、]{style="font-family:宋体"}[:]{lang="FR"}[、]{style="font-family:宋体"}[@]{lang="FR"}[、]{style="font-family:
宋体"}[&]{lang="FR"}[、]{style="font-family:宋体"}[\$]{lang="FR"}[、]{style="font-family:宋体"}[+]{lang="FR"}[、]{style="font-family:宋体"}[\*]{lang="FR"}[、]{style="font-family:
宋体"}[\']{lang="FR"}[、]{style="font-family:宋体"}[(]{lang="FR"}[、]{style="font-family:宋体"}[)]{lang="FR"}[、]{style="font-family:宋体"}[,]{lang="FR"}[、]{style="font-family:
宋体"}[/]{lang="FR"}[。]{style="font-family:宋体"}[该字符串中的每个字符都被认为是分隔字符。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983602182}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1983995398}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983471105}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1983340033}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的参数]{style="font-family:宋体"}[模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[URL]{lang="EN-US"}[中分隔]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[的字符]{style="font-family:宋体"}[为]{style="font-family:宋体"}["]{style="font-family:宋体"}[/]{lang="FR"}["、"]{style="font-family:
宋体"}[@]{lang="DE"}["、"]{style="font-family:宋体"}[\#]{lang="FR"}["或"]{style="font-family:宋体"}[\$]{lang="DE"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1983667713}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] secondary-cookie delimiters !@#\$]{lang="EN-US"}
:::

::: {#1219849070 .myid}
[]{#_Toc404796631}[]{#struct_0_x7280_11703_1983536641}[]{#_Toc380505019}[]{#_Toc364842628}[]{#_Toc362006274}[]{#_Toc354047348}

**负载均衡 \-- 负载均衡配置命令 \-- secondary-cookie start**

------------------------------------------------------------------------

[**[secondary-cookie]{lang="EN-US"}**[ **start**]{lang="EN-US"}]{#struct_0_x7280_11703_1983929857}[命令用来配置]{style="font-family:宋体"}[URL]{lang="EN-US"}[中]{style="font-family:宋体"}[Secondary Cookie]{lang="EN-US"}[的起始位置标示字符。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[secondary-cookie]{lang="EN-US"}**[ **start**]{lang="EN-US"}]{#struct_0_x7280_11703_1983995393}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983471104}

[**[secondary-cookie]{lang="EN-US"}**[ **start** *text*]{lang="EN-US"}]{#struct_0_x7280_11703_1983340032}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[secondary-cookie]{lang="EN-US"}**[ **start**]{lang="EN-US"}]{#struct_0_x7280_11703_1983667712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983536640}

[[URL]{lang="FR"}]{#struct_0_x7280_11703_1983929856}[中]{style="font-family:宋体"}[Secondary Cookie]{lang="FR"}[的起始位置标示字符为]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="FR"}["]{style="font-family:宋体"}[。]{style="font-family:
宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1983995392}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x745412246}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745543318}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x745215638}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x745346710}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x744953494}

[*[text]{lang="FR"}*]{#struct_0_x7280_11703_x744887958}[：]{style="font-family:宋体"}[标示字符]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[2]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[包括]{style="font-family:宋体"}[：]{style="font-family:宋体"}[!]{lang="FR"}[、]{style="font-family:宋体"}[\"]{lang="FR"}[、]{style="font-family:宋体"}[\#]{lang="FR"}[、]{style="font-family:
宋体"}[;]{lang="FR"}[、]{style="font-family:宋体"}[\<]{lang="FR"}[、]{style="font-family:宋体"}[\>]{lang="FR"}[、]{style="font-family:宋体"}[?]{lang="FR"}[、]{style="font-family:
宋体"}[\[]{lang="FR"}[、]{style="font-family:宋体"}[\\]{lang="FR"}[、]{style="font-family:宋体"}[\]]{lang="FR"}[、]{style="font-family:宋体"}[\^]{lang="FR"}[、]{style="font-family:
宋体"}[\`]{lang="FR"}[、]{style="font-family:宋体"}[\|]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745412247}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x745608855}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745215639}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_x745346711}[在]{style="font-family:宋体"}[HTTP]{lang="FR"}[类型的参数]{style="font-family:
宋体"}[模板]{style="font-family:宋体"}[pp1]{lang="PT-BR"}[中，]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[URL]{lang="FR"}[中]{style="font-family:宋体"}[Secondary Cookie]{lang="FR"}[的起始位置标示字符为]{style="font-family:宋体"}["]{style="font-family:宋体"}[?]{lang="FR"}["或"]{style="font-family:宋体"}[!]{lang="FR"}["]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_x744887959}

[\[Sysname\] parameter-profile pp1 type http]{lang="FR"}

[\[Sysname-para-http-pp1\] secondary-cookie start ?!]{lang="EN-US"}
:::

::: {#-824268191 .myid}
[]{#_Toc404796632}[]{#struct_0_x7280_11703_290549716}

**负载均衡 \-- 负载均衡配置命令 \-- selected-server**

------------------------------------------------------------------------

[**[selected-server]{lang="EN-US"}**]{#struct_0_x7280_11703_x1663863364}[命令用来配置实服务组中可被调度算法调用的实服务器数量限制。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **selected-server**]{lang="EN-US"}]{#struct_0_x7280_11703_x1411401916}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1881569047}

[**[selected-server]{lang="EN-US"}**[ **min**]{lang="EN-US"}[ *min-number* **max** *max-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1354843790}

[**[undo]{lang="EN-US"}**[ **selected-server**]{lang="EN-US"}]{#struct_0_x7280_11703_x785136065}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x452317798}

[[实服务组中调用优先级最高的实服务器全部被调度算法调用。]{style="font-family:宋体"}]{#struct_0_x7280_11703_207602164}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x874466321}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2081340963}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1084069300}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411991739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1617735709}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1969462636}

[**[min]{lang="EN-US"}**[ *min-number*]{lang="EN-US"}]{#struct_0_x7280_11703_x1251159288}[：可被调度算法调用的实服务器最小数量，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[max]{lang="EN-US"}**[ *max-number*]{lang="EN-US"}]{#struct_0_x7280_11703_x1545087738}[：]{style="font-family:宋体"}[可被调度算法调用的实服务器最大数量，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，且必须大于等于]{style="font-family:宋体"}*[min-number]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1931977782}

[[缺省情况下，一个实服务组中调用优先级最高的实服务器全部被调度算法调用。用户通过本命令可以限制可被调度算法调用的实服务器数量：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1596777133}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果调用优先级最高的可用实服务器数量大于]{style="font-family:宋体"}]{#struct_0_x7280_11703_1983272429}*[max-number]{lang="EN-US"}*[时，则只选用]{style="font-family:宋体"}*[max-number]{lang="EN-US"}*[个实服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果调用优先级最高的可用实服务器数量小于]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1931912246}*[min-number]{lang="EN-US"}*[时，除了调用全部优先级最高的可用实服务器外，还会调用优先级次高的可用实服务器，直至调用的可用实服务器数量达到]{style="font-family:宋体"}*[min-number]{lang="EN-US"}*[，或者没有可用的实服务器可调用为止。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1840079694}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1318673728}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[中可被调度算法调用的实服务器最小数量为]{style="font-family:宋体"}[20]{lang="EN-US"}[，最大数量为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x895178992}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] selected-server min 20 max 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x913044128}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[predictor]{lang="EN-US"}**]{#struct_0_x7280_11703_2075829287}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[priority]{lang="EN-US"}**]{#struct_0_x7280_11703_x1475670509}
:::

::: {#-1886420663 .myid}
[]{#_Toc404796633}[]{#struct_0_x7280_11703_x744887956}[]{#_Toc380505021}[]{#_Toc364842633}[]{#_Toc362006268}[]{#_Toc347413211}[]{#_Toc318725277}

**负载均衡 \-- 负载均衡配置命令 \-- server-connection reuse**

------------------------------------------------------------------------

[**[server-connection]{lang="EN-US"}**[ **reuse**]{lang="EN-US"}]{#struct_0_x7280_11703_x745412245}[命令用来配置允许负载均衡设备与服务器的连接复用。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[server-connection]{lang="EN-US"}**[ **reuse**]{lang="EN-US"}]{#struct_0_x7280_11703_x745543317}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745150101}

[**[server-connection]{lang="EN-US"}**[ **reuse**]{lang="EN-US"}]{#struct_0_x7280_11703_x745346709}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[server-connection]{lang="EN-US"}**[ **reuse**]{lang="EN-US"}]{#struct_0_x7280_11703_x744953493}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745477786}

[[不允许负载均衡设备与服务器的连接复用。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x745412250}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745543322}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x745150106}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745281178}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x744887962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x745412251}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x745608859}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x745215643}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[允许负载均衡设备与服务器的连接复用，即允许负载均衡设备与服务器建立长连接，使多个客户端复用同一条与服务器的连接，以减少客户端与服务器之间打开的连接数。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x745346715}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x744953499}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x744887963}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1148696773}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp1]{lang="EN-US"}[中，配置允许负载均衡设备与服务器的连接复用。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1148500165}

[\[Sysname\] parameter-profile pp1 type http]{lang="EN-US"}

[\[Sysname-para-http-pp1\] server-connection reuse]{lang="EN-US"}
:::

::: {#-263515494 .myid}
[]{#_Toc404796634}[]{#struct_0_x7280_11703_x1411926203}[]{#_Toc334536501}[]{#_Toc329869242}[]{#_Toc326931115}

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (LB action view)**

------------------------------------------------------------------------

[**[server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_x802402893}[命令用来指定指导转发的实服务组。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_1820395571}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1668666929}

[**[server-farm]{lang="EN-US"}**[ *server-farm-name* \[ **backup** *backup-server-farm-name* \] \[ **sticky** *sticky-name* \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1640362199}

[**[undo]{lang="EN-US"}**[ **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_x747445233}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x148262017}

[[没有指定]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1085134987}[指导转发的实服务组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x587904857}

[[负载均衡动作视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1412122811}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x157927740}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_462733997}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1684457429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_905813875}

[*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1157109801}[：主用实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[backup]{lang="EN-US"}**[ *backup-*]{lang="EN-US"}*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1494787929}[：备用实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[sticky]{lang="EN-US"}**[ ]{lang="EN-US"}*[sticky-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1513108247}[：实服务组所对应持续性组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x989322740}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1148696771}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x7280_11703_x1412057275}[与]{lang="EN-US" style="font-family:宋体"}**[forward]{lang="EN-US"}**[ **all**]{lang="EN-US"}[命令互斥]{lang="EN-US" style="font-family:宋体"}[，当]{lang="EN-US" style="font-family:宋体"}[配置了其中一条后]{lang="EN-US" style="font-family:
宋体"}[，]{lang="EN-US" style="font-family:宋体"}[另一条的配置将被自动取消。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}[当主用实服务组可用（该实服务组存在且有可用的实服务器）时，使用主用实服务组指导转发；当主用实服务组不可用而备用实服务组可用时，使用备用实服务组指导转发。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1932436527}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1948619687}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_1485412812}[在通用类型的负载均衡动作]{style="font-family:宋体"}[lb]{lang="EN-US"}[a1]{lang="DE"}[中，]{style="font-family:宋体"}[指定]{style="font-family:
宋体"}[指导转发]{style="font-family:宋体"}[的主用实服务组为]{style="font-family:
宋体"}[sf]{lang="DE"}[，]{style="font-family:宋体"}[备用实服务组为]{style="font-family:宋体"}[sfb]{lang="EN-US"}[，]{style="font-family:宋体"}[持续性组为]{style="font-family:宋体"}[sg1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_348818871}

[\[Sysname\] loadbalance action lba1 type generic]{lang="EN-US"}

[\[Sysname-lba-generic-lba1\] server-farm sf backup sfb sticky sg1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x355284486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[forward]{lang="EN-US"}**[ **all**]{lang="EN-US"}]{#struct_0_x7280_11703_x416931981}
:::

::: {#1909281990 .myid}
[]{#_Toc404796635}[]{#struct_0_x7280_11703_x649503121}[]{#_Toc334536517}[]{#_Toc329869258}[]{#_Toc329241940}[]{#_Toc323399280}

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (real server view)**

------------------------------------------------------------------------

[**[server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_x125526891}[命令用来指定实服务器所属的实服务组。]{style="font-family:宋体"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x7280_11703_x1411729595}[ **server-farm**]{lang="PT-BR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1014537092}

[**[server-farm]{lang="EN-US"}**[ ]{lang="EN-US"}*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x32594290}

[**[undo]{lang="EN-US"}**[ **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_1734535923}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_412929394}

[[实服务器不属于任何实服务组。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x87327500}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1047814062}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1850249112}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x629263289}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411664059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1568717783}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1673559121}

[*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1951496804}[：实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。可以是尚未创建的实服务组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_972773607}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1050843031}[指定实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[属于实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_661956305}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-]{lang="EN-US"}[rs]{lang="PT-BR"}[\] server-farm sf]{lang="EN-US"}
:::

::: {#629950037 .myid}
[]{#_Toc404796636}[]{#struct_0_x7280_11703_x1366128378}[]{#_Toc334536480}[]{#_Toc329869224}[]{#_Toc329781850}[]{#_Toc318980984}[]{#_Toc318725152}[]{#_Toc296587164}

**负载均衡 \-- 负载均衡配置命令 \-- server-farm (system view)**

------------------------------------------------------------------------

[**[server-farm]{lang="EN-US"}**]{#struct_0_x7280_11703_x1411860667}[命令用来创建实服务组，并进入实服务组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **server-farm**]{lang="EN-US"}]{#struct_0_x7280_11703_1826553903}[命令用来删除指定的实服务组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_874942734}

[**[server-farm]{lang="EN-US"}**[ *server-farm-name*]{lang="EN-US"}]{#struct_0_x7280_11703_2009011695}

[**[undo]{lang="EN-US"}**[ **server-farm** *server-farm-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x310670339}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1935289636}

[[不存在任何实服务组。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1564486207}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1730023145}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1411795131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1809779531}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_2112765183}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1547217330}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1333977989}

[*[server-farm-name]{lang="EN-US"}*]{#struct_0_x7280_11703_2003088939}[：实服务组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1932764207}

[[为了便于对多台服务器进行管理，可以依据这些服务器的共有属性划分成不同的组，称为实服务组。比如，可按存储内容的不同划分为歌曲服务器组、视频服务器组或图片服务器组等。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1912090107}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1272691780}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x755318734}[创建实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[，并进入实服务组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1411467451}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\]]{lang="EN-US"}
:::

::: {#-669347199 .myid}
[]{#_Toc404796637}[]{#struct_0_x7280_11703_1073747707}[]{#_Toc334536535}[]{#_Toc329869274}[]{#_Toc329242046}

**负载均衡 \-- 负载均衡配置命令 \-- service enable**

------------------------------------------------------------------------

[**[service]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x242582611}[命令用来]{style="font-family:宋体"}[开启虚服务器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **service** **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1747396602}[命令用来关闭虚服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x490370986}

[**[service]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x455989812}

[**[undo]{lang="EN-US"}**[ **service** **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1597186860}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1516551735}

[[虚服务器处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1264024751}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411401915}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2010113722}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1198318385}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1803334640}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x583207307}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x559308264}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1672636647}[开启]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1981264612}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] service enable]{lang="EN-US"}
:::

::: {#790462187 .myid}
[]{#_Toc404796638}[]{#struct_0_x7280_11703_x1411991742}[]{#_Toc334536502}[]{#_Toc329869243}[]{#_Toc326931116}[]{#_Toc317490852}[]{#_Toc317090616}

**负载均衡 \-- 负载均衡配置命令 \-- set ip tos (LB action view)**

------------------------------------------------------------------------

[**[set]{lang="EN-US"}**[ **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_1664986484}[命令用来配置发往服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[set]{lang="EN-US"}**[ **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_x1350824370}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1463237010}

[**[set]{lang="EN-US"}**[ **ip** **tos** *tos-number*]{lang="EN-US"}]{#struct_0_x7280_11703_1289847882}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[set]{lang="EN-US"}**[ **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_874042435}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2124838263}

[[不改变]{style="font-family:宋体"}]{#struct_0_x7280_11703_449796142}[发往服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1122225608}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1411926206}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x399118366}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1468628796}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x2118132537}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1306929943}

[*[tos-number]{lang="FR"}*]{#struct_0_x7280_11703_x499565510}[：]{style="font-family:宋体"}[ToS]{lang="FR"}[字段值]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:
宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1710392280}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_x1413669879}[在通用类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[lb]{lang="FR"}[a1]{lang="DE"}[中，]{style="font-family:宋体"}[配置发往服务器的]{style="font-family:宋体"}[IP]{lang="FR"}[报文中的]{style="font-family:宋体"}[ToS]{lang="FR"}[字段值为]{style="font-family:宋体"}[20]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_x1412122814}

[\[Sysname\] loadbalance action lba1 type generic]{lang="FR"}

[\[Sysname-lba-generic-lba1\] set ip tos 20]{lang="EN-US"}
:::

::: {#-1563254214 .myid}
[]{#_Toc404796639}[]{#struct_0_x7280_11703_245356787}[]{#_Toc334536473}[]{#_Toc329875705}[]{#_Toc329869218}[]{#_Toc326936443}[]{#_Toc326934485}

**负载均衡 \-- 负载均衡配置命令 \-- set ip tos (parameter profile view)**

------------------------------------------------------------------------

[**[set]{lang="EN-US"}**[ **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_1804658807}[命令用来配置发往客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[set]{lang="EN-US"}**[ **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_x689387392}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1382916720}

[**[set]{lang="EN-US"}**[ **ip** **tos** *tos-number*]{lang="EN-US"}]{#struct_0_x7280_11703_741826431}

[**[undo]{lang="EN-US"}**[ **set** **ip** **tos**]{lang="EN-US"}]{#struct_0_x7280_11703_1862581704}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x221395004}

[[不改变发往客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x7280_11703_197698342}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1412057278}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1995673854}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_309998734}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1955316643}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x540186226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1205119702}

[*[tos-number]{lang="FR"}*]{#struct_0_x7280_11703_x600390370}[：]{style="font-family:宋体"}[ToS]{lang="FR"}[字段值]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[取值范围]{style="font-family:
宋体"}[0]{lang="FR"}[～]{style="font-family:宋体"}[255]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_417911455}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_417387170}[IP]{lang="FR"}[类型的参数模板视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_965407001}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_313213593}[在]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的参数模板]{style="font-family:宋体"}[pp2]{lang="FR"}[中，配置发往客户端的]{style="font-family:宋体"}[IP]{lang="FR"}[报文中的]{style="font-family:宋体"}[ToS]{lang="FR"}[字段值为]{style="font-family:宋体"}[20]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_x1411729598}

[\[Sysname\] parameter-profile pp2 type ip]{lang="EN-US"}

[\[Sysname-para-ip-pp2\] set ip tos 20]{lang="EN-US"}
:::

::: {#1170655049 .myid}
[]{#_Toc404796640}[]{#struct_0_x7280_11703_101208155}[]{#_Toc334536518}[]{#_Toc329869259}[]{#_Toc329241941}[]{#_Toc323399281}[]{#_Toc323112434}

**负载均衡 \-- 负载均衡配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_x149057395}[命令用来关闭实服务器。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x7280_11703_x1865627302}[命令用来开启实服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1961650934}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_99439495}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x7280_11703_1058950781}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411664062}

[[实服务器处于开启状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1516330396}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1868752890}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_494469161}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1454332875}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x486625992}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x203715526}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x452773746}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1756785449}[关闭实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1411860670}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] shutdown]{lang="EN-US"}
:::

::: {#-926214699 .myid}
[]{#_Toc404796641}[]{#struct_0_x7280_11703_x902263916}[]{#_Toc334536484}[]{#_Toc329869228}[]{#_Toc329781854}[]{#_Toc318725156}

**负载均衡 \-- 负载均衡配置命令 \-- slow-online**

------------------------------------------------------------------------

[**[slow-online]{lang="EN-US"}**]{#struct_0_x7280_11703_x1915519964}[命令用来在实服务组中开启实服务器温暖上线功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **slow-online**]{lang="EN-US"}]{#struct_0_x7280_11703_x1377164135}[命令用来在实服务组中关闭实服务器温暖上线功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1697852506}

[**[slow-online]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[standby-time]{lang="EN-US"}**[ *standby-time* **ramp-up-time** *ramp-up-time* \]]{lang="EN-US"}]{#struct_0_x7280_11703_465781182}

[**[undo]{lang="EN-US"}**[ **slow-online**]{lang="EN-US"}]{#struct_0_x7280_11703_152476172}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_377268247}

[[实服务组中的实服务器温暖上线功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x46393853}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411795134}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1406495004}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_712862317}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1994557694}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x516008423}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2107541870}

[**[standby-time]{lang="EN-US"}**[ *standby-time*]{lang="EN-US"}]{#struct_0_x7280_11703_x942422203}[：准备时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒，缺省为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[ramp-up-time]{lang="EN-US"}**[ *ramp-up-time*]{lang="EN-US"}]{#struct_0_x7280_11703_x1332598760}[：爬升时间，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒，缺省为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2054745128}

[[当向实服务组中添加实服务器时，某些新增的实服务器无法立即承担大量业务，此时可以开启温暖上线功能。这样，当实服务器上线后，在准备时间内，负载均衡设备不会向其分配任何业务；准备时间超时后，负载均衡设备在爬升时间内会逐步增加向其分配的业务量；爬升时间超时后，负载均衡设备开始向其正常分配业务。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1411467454}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1833262594}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1601109642}[在实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[中开启实服务器温暖上线功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1781711551}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] slow-online]{lang="EN-US"}
:::

::: {#-440443663 .myid}
[]{#_Toc404796642}[]{#struct_0_x7280_11703_934182132}[]{#_Toc334536519}[]{#_Toc329869260}[]{#_Toc329241942}[]{#_Toc323399282}[]{#_Toc323284859}

**负载均衡 \-- 负载均衡配置命令 \-- slow-shutdown enable**

------------------------------------------------------------------------

[**[slow-shutdown]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_86497027}[命令用来开启实服务器的慢宕功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **slow-**]{lang="EN-US"}**[shutdown]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_1071074217}[命令用来关闭实服务器的慢宕功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411401918}

[**[slow-shutdown]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x1963059555}

[**[undo]{lang="EN-US"}**[ **slow-shutdown** **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x1462026515}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1873307396}

[[实服务器的慢宕功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x502563798}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1533051730}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x2009742567}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_142738920}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1138537098}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1411991741}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1261701957}

[[通过]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_x1889941493}[命令可以立即中断实服务器的已有连接，而慢宕则不会立即中断实服务器的已有连接，而是让其自然老化，并且不再建立新的连接。]{style="font-family:宋体"}

[[本命令需要与]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_1868242627}[命令配合使用，即在开启了慢宕功能之后再关闭实服务器，该实服务器才会开始慢宕。]{style="font-family:宋体"}

[[需要注意的是，本命令不会对之前执行的]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_513228098}[命令生效。比如：开启慢宕功能并关闭实服务器之后，如果再关闭慢宕功能，则该实服务器将保持慢宕状态，而不会立即中断已有连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1323041889}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1079224435}[开启实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的慢宕功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x641202254}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] slow-shutdown enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411926205}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[shutdown]{lang="EN-US"}**]{#struct_0_x7280_11703_x1965202307}
:::

::: {#-1399899209 .myid}
[]{#_Toc404796643}[]{#struct_0_x7280_11703_x646616556}[]{#_Toc334536487}[]{#_Toc329869231}[]{#_Toc329781858}

**负载均衡 \-- 负载均衡配置命令 \-- snat-pool**

------------------------------------------------------------------------

[**[snat-pool]{lang="EN-US"}**]{#struct_0_x7280_11703_x1122478606}[命令用来指定实服务组引用的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snat-pool**]{lang="EN-US"}]{#struct_0_x7280_11703_229644703}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1899511474}

[**[snat-pool]{lang="EN-US"}**[ *pool-name*]{lang="EN-US"}]{#struct_0_x7280_11703_485502059}

[**[undo]{lang="EN-US"}**[ **snat-pool**]{lang="EN-US"}]{#struct_0_x7280_11703_433721367}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1007389444}

[[实服务组没有引用任何]{style="font-family:宋体"}[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x1412122813}[地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1320727154}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1386256225}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x287743768}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1525665904}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_839505356}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1182526361}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1793193170}[：]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_604811741}

[[SNAT]{lang="EN-US"}]{#struct_0_x7280_11703_x1412057277}[地址池是一个地址范围，它被实服务组引用之后，负载均衡设备将把收到报文的源地址修改为]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池中的地址后再转发出去。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1183548195}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_147051008}[指定实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[引用的]{style="font-family:宋体"}[SNAT]{lang="EN-US"}[地址池为]{style="font-family:宋体"}[lbsp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x374918036}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] snat-pool lbsp]{lang="EN-US"}
:::

::: {#2061614382 .myid}
[]{#_Toc404796644}[]{#struct_0_x7280_11703_417518236}[]{#_Toc374350908}[]{#_Toc344302281}

**负载均衡 \-- 负载均衡配置命令 \-- snmp-agent trap enable loadbalance**

------------------------------------------------------------------------

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **loadbalance**]{lang="EN-US"}]{#struct_0_x7280_11703_417845916}[命令用来开启负载均衡的告警功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **loadbalance**]{lang="EN-US"}]{#struct_0_x7280_11703_417321627}[命令用来关闭负载均衡的告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_417190555}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **loadbalance**]{lang="EN-US"}]{#struct_0_x7280_11703_417583771}

[**[undo]{lang="EN-US"}**[ **snmp-agent** **trap** **enable** **loadbalance**]{lang="EN-US"}]{#struct_0_x7280_11703_417452699}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_417518235}

[[负载均衡的告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_417911451}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1524015715}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1523884643}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523753571}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1523622499}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1524540003}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1524081250}

[[开启了负载均衡的告警功能之后，负载均衡会生成告警信息，以向网管软件报告本模块的重要事件。该信息将发送至]{style="font-family:宋体"}[SNMP]{lang="EN-US"}]{#struct_0_x7280_11703_1523950178}[模块，通过设置]{style="font-family:宋体"}[SNMP]{lang="EN-US"}[中告警信息的发送参数，来决定告警信息输出的相关属性。有关告警信息的详细介绍，请参见"网络管理和监控配置指导"中的"]{style="font-family:宋体"}[SNMP]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523819106}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1523688034}[关闭负载均衡的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1524605538}

[\[Sysname\] undo snmp-agent trap enable loadbalance]{lang="EN-US"}
:::

::: {#65872997 .myid}
[]{#_Toc404796645}[]{#struct_0_x7280_11703_2141233758}

**负载均衡 \-- 负载均衡配置命令 \-- ssl session-id**

------------------------------------------------------------------------

[**[ssl]{lang="EN-US"}**[ **session-id**]{lang="EN-US"}]{#struct_0_x7280_11703_x1693334923}[命令用来配置]{style="font-family:宋体"}[SSL]{lang="EN-US"}[持续性方法为基于]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssl** **session-id**]{lang="EN-US"}]{#struct_0_x7280_11703_1069192307}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x19907357}

[**[ssl]{lang="EN-US"}**[ **session-id**]{lang="EN-US"}]{#struct_0_x7280_11703_x1716271251}

[**[undo]{lang="EN-US"}**[ **ssl** **session-id**]{lang="EN-US"}]{#struct_0_x7280_11703_45357628}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1012133366}

[[不存在任何持续性方法。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x150624457}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1193025634}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_2140906078}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x513836445}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1054819246}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x942766519}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1820153296}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1119841909}[SSL]{lang="FR"}[类型的持续性组视图下支持。]{style="font-family:宋体"}

[[基于]{style="font-family:宋体"}]{#struct_0_x7280_11703_1727108939}[SSL]{lang="FR"}[会话]{style="font-family:宋体"}[ID]{lang="FR"}[的]{style="font-family:
宋体"}[SSL]{lang="FR"}[持续性方法对]{style="font-family:宋体"}[HTTPS]{lang="FR"}[请求报文有效]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并且需要指定虚服务器引用的]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x330901351}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x648843686}[在]{style="font-family:宋体"}[SSL]{lang="EN-US"}[类型的持续性组]{style="font-family:宋体"}[sg6]{lang="EN-US"}[中，指定]{style="font-family:宋体"}[SSL]{lang="EN-US"}[的持续性方法为基于]{style="font-family:宋体"}[SSL]{lang="EN-US"}[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2140840542}

[\[Sysname\] sticky-group sg6 type ssl]{lang="EN-US"}

[\[Sysname-sticky-ssl-sg6\] ]{lang="EN-US"}[ssl session-id]{lang="DE"}
:::

::: {#1742537849 .myid}
[]{#_Toc404796646}[]{#struct_0_x7280_11703_1524081253}[]{#_Toc380505032}[]{#_Toc364842646}[]{#_Toc362006315}[]{#_Toc317490857}

**负载均衡 \-- 负载均衡配置命令 \-- ssl url rewrite**

------------------------------------------------------------------------

[**[ssl]{lang="EN-US"}**[ **url** **rewrite**]{lang="EN-US"}]{#struct_0_x7280_11703_1523950181}[命令用来重写服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文]{style="font-family:宋体"}[Location]{lang="EN-US"}[首部的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1523884645}**[ssl]{lang="FR"}**[ **url** **rewrite**]{lang="FR"}[命令用来取消该配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523753573}

[**[ssl]{lang="FR"}**]{#struct_0_x7280_11703_1523622501}[ **url** **rewrite** **location** *location* \[ **clearport** *clear-port* \] \[ **sslport** *ssl-port* \]]{lang="FR"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x7280_11703_1524540005}**[ssl]{lang="FR"}**[ **url** **rewrite** **location** *location* \[ **clearport** *clear-port* \]]{lang="FR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1524015716}

[[不]{style="font-family:宋体"}]{#struct_0_x7280_11703_1523884644}[重写服务器发送的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[应答报文]{style="font-family:宋体"}[Location]{lang="EN-US"}[首部的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523819108}

[[负载均衡动作]{style="font-family:宋体"}]{#struct_0_x7280_11703_1523688036}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1524605540}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1524081247}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1524015711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523884639}

[**[location]{lang="FR"}**]{#struct_0_x7280_11703_1523753567}[ *location*]{lang="FR"}[：]{style="font-family:宋体"}[Location]{lang="FR"}[首部]{style="font-family:宋体"}[URL]{lang="FR"}[的正则表达式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[255]{lang="FR"}[个字符的字符串。]{style="font-family:宋体"}

[**[clearport]{lang="FR"}**]{#struct_0_x7280_11703_1523622495}[ *clear-port*]{lang="FR"}[：原]{style="font-family:宋体"}[HTTP]{lang="FR"}[端口号]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[，缺省值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[80]{lang="FR"}[。]{style="font-family:宋体"}

[**[sslport]{lang="FR"}**]{#struct_0_x7280_11703_1524539999}[ *ssl-port*]{lang="FR"}[：重写后]{style="font-family:宋体"}[的]{style="font-family:宋体"}[SSL]{lang="FR"}[端口号]{style="font-family:
宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[，缺省值]{style="font-family:宋体"}[为]{style="font-family:宋体"}[443]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1524015710}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1523884638}[类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[配置了本命令后，如果]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_1523819102}[应答报文]{style="font-family:宋体"}[Location]{lang="EN-US"}[首部匹配了指定的]{style="font-family:宋体"}*[location]{lang="FR"}*[和]{style="font-family:宋体"}*[clear-port]{lang="FR"}*[，系统会将]{style="font-family:宋体"}[Location]{lang="EN-US"}[首部的]{style="font-family:宋体"}[URL]{lang="EN-US"}[由]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[重写为]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[，并将]{style="font-family:宋体"}*[clear-port]{lang="FR"}*[重写为]{style="font-family:宋体"}*[ssl-port]{lang="FR"}*[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1523688030}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_1524605534}[在]{style="font-family:宋体"}[HTTP]{lang="DE"}[类型的负载均衡动作]{style="font-family:
宋体"}[lba2]{lang="DE"}[中，将]{style="font-family:宋体"}[服务器发送的]{style="font-family:宋体"}[HTTP]{lang="FR"}[应答报文]{style="font-family:宋体"}[Location]{lang="FR"}[首部的]{style="font-family:宋体"}[URL]{lang="FR"}[，]{style="font-family:宋体"}[由]{style="font-family:宋体"}[[http://www.ss.com:8080]{lang="DE" style="color:windowtext;text-decoration:
none"}](http://www.ss.com:8080)[重写为]{style="font-family:宋体"}[[https://www.ss.com:443]{lang="DE" style="color:windowtext;text-decoration:
none"}](https://www.ss.com:443)[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1204802104}

[\[Sysname\] loadbalance action lba2 type http]{lang="EN-US"}

[\[Sysname-lba-http-lba2\] ssl url rewrite www.ss.com clearport 8080 sslport 443]{lang="EN-US"}
:::

::: {#122930484 .myid}
[]{#_Toc404796647}[]{#struct_0_x7280_11703_2140971614}

**负载均衡 \-- 负载均衡配置命令 \-- ssl-client-policy (LB action view)**

------------------------------------------------------------------------

[**[ssl-client-policy]{lang="EN-US"}**]{#struct_0_x7280_11703_251046566}[命令用来引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略，以便对负载均衡设备（作为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端）与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器之间传输的流量进行加密传输。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy**]{lang="EN-US"}]{#struct_0_x7280_11703_x1277208838}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1041136951}

[**[ssl-client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_901154842}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy** *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1122289536}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x422818414}

[[没有引用任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_x1255692621}[客户端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x629241761}

[[负载均衡动作视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_945911114}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2141692510}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x530690462}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x805182762}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1067710557}

[*[policy-name]{lang="FR"}*]{#struct_0_x7280_11703_x431287860}[：]{style="font-family:宋体"}[SSL]{lang="FR"}[客户端策略的名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x174947302}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x1350612501}[类型的负载均衡]{style="font-family:宋体"}[动作]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x843924234}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2020097862}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_x810241334}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的负载均衡动作]{style="font-family:宋体"}[lb]{lang="EN-US"}[a2]{lang="DE"}[中，]{style="font-family:宋体"}[引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[scp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_2141626974}

[\[Sysname\] loadbalance action lba2 type http]{lang="EN-US"}

[\[Sysname-lba-http-lba2\] ssl-client-policy scp]{lang="EN-US"}
:::

::: {#614276909 .myid}
[]{#_Toc404796648}[]{#struct_0_x7280_11703_701725688}

**负载均衡 \-- 负载均衡配置命令 \-- ssl-client-policy (virtual server view)**

------------------------------------------------------------------------

[**[ssl-client-policy]{lang="EN-US"}**]{#struct_0_x7280_11703_733402267}[命令用来指定虚服务器引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略，以便对负载均衡设备（作为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端）与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器之间传输的流量进行加密传输。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy**]{lang="EN-US"}]{#struct_0_x7280_11703_x2098076468}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1129068780}

[**[ssl-client-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x1221207888}

[**[undo]{lang="EN-US"}**[ **ssl-client-policy** *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x367046250}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1337861123}

[[虚服务器没有引用任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_1287401847}[客户端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2141168223}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_198564810}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_913625688}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_x1636349513}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_x1170567915}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x786593629}

[*[policy-name]{lang="FR"}*]{#struct_0_x7280_11703_602591281}[：]{style="font-family:宋体"}[SSL]{lang="FR"}[客户端策略的名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:
宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[31]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_124256311}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_2141102687}[类型的虚服务器视图下支持。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x2080813626}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1974660922}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_1092943940}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs2]{lang="EN-US"}[上，引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端策略]{style="font-family:宋体"}[scp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_489486777}

[\[Sysname\] virtual-server vs2 type http]{lang="EN-US"}

[\[Sysname-vs-http-vs2\] ssl-client-policy scp]{lang="EN-US"}
:::

::: {#1337650138 .myid}
[]{#_Toc404796649}[]{#struct_0_x7280_11703_1193850584}

**负载均衡 \-- 负载均衡配置命令 \-- ssl-server-policy**

------------------------------------------------------------------------

[**[ssl-server-policy]{lang="EN-US"}**]{#struct_0_x7280_11703_x1729472595}[命令用来指定虚服务器引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略，以便对负载均衡设备（作为]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器）与]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端之间传输的流量进行加密传输。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ssl-server-policy**]{lang="EN-US"}]{#struct_0_x7280_11703_2141299295}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1386852209}

[**[ssl-server-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x590944966}

[**[undo]{lang="EN-US"}**[ **ssl-server-policy**]{lang="EN-US"}]{#struct_0_x7280_11703_1666185459}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_482712246}

[[虚服务器没有引用任何]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x7280_11703_1651967920}[服务器端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x932711506}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x122851813}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_414807670}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_2070115121}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_2141233759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1693400459}

[*[name]{lang="FR"}*]{#struct_0_x7280_11703_2039328997}[：]{style="font-family:宋体"}[SSL]{lang="FR"}[服务器端策略的名称]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:
宋体"}[31]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2090423082}

[[本命令只在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_2063246467}[类型的虚服务器视图下支持。]{style="font-family:宋体"}

[[需要注意的是，快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x7280_11703_x391642459}[类型的虚服务器不支持本功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1824931124}

[[\# ]{lang="DE"}]{#struct_0_x7280_11703_978102098}[在]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs2]{lang="EN-US"}[上，引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略]{style="font-family:宋体"}[ssp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1720675071}

[\[Sysname\] virtual-server vs2 type http]{lang="EN-US"}

[\[Sysname-vs-http-vs2\] ssl-server-policy ssp]{lang="EN-US"}
:::

::: {#-1392203380 .myid}
[]{#_Toc311899220}[]{#_Toc404796650}[]{#struct_0_x7280_11703_x268411381}[]{#_Toc334536465}[]{#_Toc329869210}[]{#_Toc317532977}

**负载均衡 \-- 负载均衡配置命令 \-- sticky-group**

------------------------------------------------------------------------

[**[sticky-group]{lang="EN-US"}**]{#struct_0_x7280_11703_254514663}[命令用来创建持续性组，并进入持续性组视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sticky-group**]{lang="EN-US"}]{#struct_0_x7280_11703_1673296720}[命令用来删除指定的持续性组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2049962216}

[**[sticky-group]{lang="EN-US"}**[ *group-name* \[ **type** { **address-port** \| **http-content** \| **http-cookie** \| **http-header** \| **payload** \| **ssl** } \]]{lang="EN-US"}]{#struct_0_x7280_11703_x1411729597}

[**[undo]{lang="EN-US"}**[ **sticky-group** *group-name*]{lang="EN-US"}]{#struct_0_x7280_11703_2117630790}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1351616289}

[[不存在任何持续性组。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1736238974}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x672583704}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_117470970}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x129950925}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_323223995}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x958776177}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411664061}

[*[group-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1212552959}[：持续性组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **address-port** \| **http-content** \| **http-cookie** \| **http-header** \| **payload** \| **ssl** }]{lang="EN-US"}]{#struct_0_x7280_11703_519969609}[：持续性组的类型，包括地址端口、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[实体、]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[首部、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[载荷和]{style="font-family:宋体"}[SSL]{lang="EN-US"}[六种类型。创建持续性组时必须指定本参数；而在进入已创建的持续性组视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2133602716}

[[持续性组的作用是根据某种持续性方法将具有一定相关性的会话都分配给同一个实服务器处理。在一个会话中，当其首包通过持续性方法选择了实服务器之后，后续包都会沿用这个选择结果。]{style="font-family:宋体"}]{#struct_0_x7280_11703_524808723}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1607873299}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_1077718922}[创建地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1411860669}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\]]{lang="EN-US"}
:::

::::: {#-579730487 .myid}
[]{#_Toc404796651}[]{#struct_0_x7280_11703_652215571}[]{#_Toc400807598}[]{#_Toc396740867}

**负载均衡 \-- 负载均衡配置命令 \-- sticky-sync enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](负载均衡命令.files/image002.png){#图片 4 border="0" width="62" height="25"}]{lang="EN-US"}]{#struct_0_x7280_11703_1307686953}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[集中式设备不支持本命令，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x7280_11703_1025772761}
:::

**[ ]{lang="EN-US"}**

[**[sticky-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_448011451}[命令用来开启]{style="font-family:宋体"}[虚服务器的持续性表项备份功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[sticky-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x691855738}[命令用来关闭虚服务器的持续性表项备份功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_550339708}

[**[sticky-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x414813983}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[sticky-sync]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x2075626152}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1206643792}

[[虚服务器的持续性表项备份功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x7280_11703_863416084}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x935973178}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1824041074}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1562084301}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1596833261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_874228203}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1666020455}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x248622128}[开启]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的持续性表项备份。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1328228440}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] sticky-sync enable]{lang="EN-US"}
:::::

::: {#-104995503 .myid}
[]{#_Toc404796652}[]{#struct_0_x7280_11703_x1298399945}

**负载均衡 \-- 负载均衡配置命令 \-- success-criteria (real server view)**

------------------------------------------------------------------------

[**[success-criteria]{lang="EN-US"}**]{#struct_0_x7280_11703_x1298596553}[命令用来配置实服务器健康检测的成功条件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **success-criteria**]{lang="EN-US"}]{#struct_0_x7280_11703_x1999444276}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1169333243}

[**[success-criteria]{lang="EN-US"}**[ { **all** \| **at-least** *min-number* }]{lang="EN-US"}]{#struct_0_x7280_11703_560050620}

[**[undo]{lang="EN-US"}**[ **success-criteria**]{lang="EN-US"}]{#struct_0_x7280_11703_x196346752}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1298531017}

[[只有全部方法都通过检测才认为健康检测成功。]{style="font-family:宋体"}]{#struct_0_x7280_11703_138824271}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1202942339}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1623375093}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1298727625}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1997151122}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_113828849}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1238940204}

[**[all]{lang="EN-US"}**]{#struct_0_x7280_11703_1343624180}[：只有全部方法都通过检测才认为健康检测成功。]{style="font-family:宋体"}

[**[at-least]{lang="EN-US"}**[ *min-number*]{lang="EN-US"}]{#struct_0_x7280_11703_x1298662089}[：健康检测成功所需通过检测的最少方法数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1932895280}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1204867644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户指定的最少方法数大于设备上实际存在的方法数量时，系统也将认为健康检测成功。]{style="font-family:宋体"}]{#struct_0_x7280_11703_716224159}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1932829744}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x71053804}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_467105625}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的健康检测成功所需通过检测的最少方法数为]{style="font-family:宋体"}[2]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x149234784}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] [success-criteria at-least 2]{.TerminalDisplayChar}]{lang="EN-US"}
:::

::: {#-1207358641 .myid}
[]{#_Toc404796653}[]{#struct_0_x7280_11703_x1298203338}

**负载均衡 \-- 负载均衡配置命令 \-- success-criteria (server farm view)**

------------------------------------------------------------------------

[**[success-criteria]{lang="EN-US"}**]{#struct_0_x7280_11703_x1776201050}[命令用来配置实服务组健康检测的成功条件。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **success-criteria**]{lang="EN-US"}]{#struct_0_x7280_11703_1229473837}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1959882450}

[**[success-criteria]{lang="EN-US"}**[ { **all** \| **at-least** *min-number* }]{lang="EN-US"}]{#struct_0_x7280_11703_x2055644422}

[**[undo]{lang="EN-US"}**[ **success-criteria**]{lang="EN-US"}]{#struct_0_x7280_11703_x1298137802}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x344194224}

[[只有全部方法都通过检测才认为健康检测成功。]{style="font-family:宋体"}]{#struct_0_x7280_11703_638139997}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_922298642}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1298334410}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_956755066}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1443991218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x987874389}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x809363486}

[**[all]{lang="EN-US"}**]{#struct_0_x7280_11703_x1298268874}[：只有全部方法都通过检测才认为健康检测成功。]{style="font-family:宋体"}

[**[at-least]{lang="EN-US"}**[ *min-number*]{lang="EN-US"}]{#struct_0_x7280_11703_x818230413}[：健康检测成功所需通过检测的最少方法数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1931977776}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1204277820}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户指定的最少方法数大于设备上实际存在的方法数量时，系统也将认为健康检测成功。]{style="font-family:宋体"}]{#struct_0_x7280_11703_372394727}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户既可在实服务组视图下对组内的所有实服务器进行配置，也可在实服务器视图下只对当前实服务器进行配置，后者的配置优先级较高。]{style="font-family:宋体"}]{#struct_0_x7280_11703_757970356}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1892667898}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_969133325}[配置实服务组]{style="font-family:宋体"}[sf]{lang="EN-US"}[的健康检测成功所需通过检测的最少方法数为]{style="font-family:宋体"}[2]{lang="EN-US"}[个。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1298465482}

[\[Sysname\] server-farm sf]{lang="EN-US"}

[\[Sysname-sfarm-sf\] success-criteria at-least 2]{lang="EN-US"}
:::

::: {#-459197171 .myid}
[]{#_Toc404796654}[]{#struct_0_x7280_11703_x587715129}

**负载均衡 \-- 负载均衡配置命令 \-- tcp window-size**

------------------------------------------------------------------------

[**[tcp]{lang="EN-US"}**[ **window-size**]{lang="EN-US"}]{#struct_0_x7280_11703_1515818001}[命令用来配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接中的本地最大窗口值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **tcp** **window-size**]{lang="EN-US"}]{#struct_0_x7280_11703_1932634356}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1431519848}

[**[tcp]{lang="EN-US"}**[ **window-size** *size*]{lang="EN-US"}]{#struct_0_x7280_11703_1365132465}

[**[undo]{lang="EN-US"}**[ **tcp** **window-size**]{lang="EN-US"}]{#struct_0_x7280_11703_1491090661}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x885303117}

[[TCP]{lang="EN-US"}]{#struct_0_x7280_11703_x587780665}[连接中的本地最大窗口值为]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1930052878}

[[参数模板视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_390266454}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x388567526}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x62152038}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1867841856}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_646694754}

[*[size]{lang="EN-US"}*]{#struct_0_x7280_11703_x138385617}[：]{style="font-family:宋体"}[窗口值]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[8192]{lang="FR"}[～]{style="font-family:宋体"}[65535]{lang="FR"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x255812820}

[[本命令只在]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1323496999}[TCP]{lang="FR"}[类型的参数模板]{style="font-family:宋体"}[视图下支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x587584057}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_1107564345}[在]{style="font-family:宋体"}[TCP]{lang="PT-BR"}[类型的]{style="font-family:宋体"}[参数模板]{style="font-family:宋体"}[pp3]{lang="FR"}[中，配置]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接中的本地最大窗口值为]{style="font-family:宋体"}[8192]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_432731567}

[\[Sysname\] parameter-profile pp3 type tcp]{lang="FR"}

[\[Sysname-para-tcp-pp3\] ]{lang="FR"}[tcp window-size 8192]{lang="EN-US"}
:::

::: {#591226122 .myid}
[]{#_Toc404796655}[]{#struct_0_x7280_11703_1019984849}[]{#_Toc334536467}[]{#_Toc329869212}[]{#_Toc325557604}[]{#_Toc317532979}

**负载均衡 \-- 负载均衡配置命令 \-- timeout**

------------------------------------------------------------------------

[**[timeout]{lang="EN-US"}**]{#struct_0_x7280_11703_x1807886738}[命令用来配置持续性表项的超时时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **timeout**]{lang="EN-US"}]{#struct_0_x7280_11703_260276829}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_42515482}

[**[timeout]{lang="EN-US"}**[ *timeout-value*]{lang="EN-US"}]{#struct_0_x7280_11703_1309391244}

[**[undo]{lang="EN-US"}**[ **timeout**]{lang="EN-US"}]{#struct_0_x7280_11703_81893540}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1815689963}

[[对于]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}]{#struct_0_x7280_11703_644953370}[类型的持续性组，持续性表项的超时时间为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒；对于其它类型的持续性组，持续性表项的超时时间为]{style="font-family:宋体"}[60]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411795133}

[[持续性组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_646980117}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_894610409}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1951435545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1702223234}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1028697999}

[*[timeout-value]{lang="EN-US"}*]{#struct_0_x7280_11703_1694023434}[：超时时间。对于]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的持续性组，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[31536000]{lang="EN-US"}[，单位为秒；对于其它类型的持续性组，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。对于]{style="font-family:宋体"}[HTTP Cookie]{lang="EN-US"}[类型的持续性组，当其持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[插入或]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[重写时，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示该持续性为会话持续性；当其持续性方法为]{style="font-family:宋体"}[Cookie]{lang="EN-US"}[截取时，]{style="font-family:宋体"}[0]{lang="EN-US"}[表示此持续性表项的超时时间为]{style="font-family:宋体"}[0]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_297138910}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x127136144}[在地址端口类型的持续性组]{style="font-family:宋体"}[sg1]{lang="EN-US"}[中，配置持续性表项的超时时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1411467453}

[\[Sysname\] sticky-group sg1 type address-port]{lang="EN-US"}

[\[Sysname-sticky-address-port-sg1\] timeout 100]{lang="EN-US"}
:::

::: {#-147301237 .myid}
[]{#_Toc404796656}[]{#struct_0_x7280_11703_x89051707}[]{#_Toc334536485}[]{#_Toc329869229}[]{#_Toc329781855}

**负载均衡 \-- 负载均衡配置命令 \-- transparent enable**

------------------------------------------------------------------------

[**[transparent]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x2047567196}[命令用来在实服务组中关闭]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **transparent** **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_292156171}[命令用来在实服务组中开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_248618012}

[**[transparent]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_549874318}

[**[undo]{lang="EN-US"}**[ **transparent** **enable**]{lang="EN-US"}]{#struct_0_x7280_11703_x1413813641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1411401917}

[[实服务组中的]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x7280_11703_x847314308}[功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_227950209}

[[实服务组视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1181085226}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1218827553}

[[network-admin]{lang="FR"}]{#struct_0_x7280_11703_1825911385}

[[mdc-admin]{lang="FR"}]{#struct_0_x7280_11703_1765975900}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1608414312}

[[需要注意的是]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1608545384}[，]{style="font-family:宋体"}[实服务组被快速]{style="font-family:宋体"}[HTTP]{lang="FR"}[或]{style="font-family:宋体"}[HTTP]{lang="FR"}[类型的虚服务器引用时]{style="font-family:
宋体"}[，]{style="font-family:宋体"}[即使关闭了]{style="font-family:宋体"}[NAT]{lang="FR"}[功能也将仍按照]{style="font-family:宋体"}[NAT]{lang="FR"}[模]{style="font-family:宋体"}[式处理。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_458398123}

[[\# ]{lang="FR"}]{#struct_0_x7280_11703_596432323}[在实服务组]{style="font-family:宋体"}[sf]{lang="FR"}[中关闭]{style="font-family:宋体"}[NAT]{lang="FR"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="FR"}]{#struct_0_x7280_11703_154092203}

[\[Sysname\] server-farm sf]{lang="FR"}

[\[Sysname-sfarm-sf\] transparent enable]{lang="EN-US"}
:::

::: {#-1355729599 .myid}
[]{#_Toc404796657}[]{#struct_0_x7280_11703_1527994745}[]{#_Toc334536536}[]{#_Toc329869275}[]{#_Toc329242047}

**负载均衡 \-- 负载均衡配置命令 \-- udp per-packet**

------------------------------------------------------------------------

[**[udp]{lang="EN-US"}**[ **per-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_x1273864112}[命令用来开启虚服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡功能。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **udp** **per-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_2101815384}[命令用来关闭虚服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1174119056}

[**[udp]{lang="EN-US"}**[ **per-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_1831042796}

[**[undo]{lang="EN-US"}**[ **udp** **per-packet**]{lang="EN-US"}]{#struct_0_x7280_11703_190512712}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1674673766}

[[虚服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_154157739}[强制负载均衡功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_765459506}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x476593158}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1183151872}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x259527695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x63585738}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x177830579}

[[本命令只在]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_x1608086629}[类型的虚服务器视图下支持。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_x1816853760}[强制负载均衡功能关闭时，匹配虚服务器的流量按照数据流来进行负载均衡，即一个应用的流量会被负载均衡到同一个实服务器上；而当]{style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡功能开启后，匹配虚服务器的流量不再按照流来进行负载均衡，而是按照每报文来进行负载均衡。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x7280_11703_1549503301}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_1770823742}[强制负载均衡功能开启后，虚服务器以及实服务器上与连接数相关的数据将不会被统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_x1105352547}[强制负载均衡功能开启后，如果引用的实服务组未开启]{style="font-family:宋体"}[NAT]{lang="EN-US"}[功能，虚服务器以及实服务器上的发出的报文数量将不会被统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_x7280_11703_x1143001908}[强制负载均衡功能开启后，以下配置项仍将生效：虚服务器所引用实服务组上配置的调度算法、虚服务器引用实服务组时所配置的持续性组中的持续性方法。例如，实服务组的调度算法为哈希算法或者持续性方法为源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址持续性时，由于同一会话的五元组相同，哈希计算结果和持续性表项匹配结果都是相同的实服务器，因此属于同一会话的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文仍将被送至同一个实服务器进行处理，而无法按照每报文进行负载均衡。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_416041902}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_765136654}[开启]{style="font-family:宋体"}[UDP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs5]{lang="EN-US"}[的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[强制负载均衡功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x1737273461}

[\[Sysname\] virtual-server vs5 type udp]{lang="EN-US"}

[\[Sysname-vs-udp-vs5\] udp per-packet]{lang="EN-US"}
:::

::: {#-1918992459 .myid}
[]{#_Toc404796658}[]{#struct_0_x7280_11703_x1935964040}[]{#_Toc334536531}[]{#_Toc329869270}[]{#_Toc329242042}[]{#_Toc320886169}[]{#_Toc382921009}[]{#_Toc383272929}[]{#_Toc383273035}[]{#_Toc383273141}[]{#_Toc383523555}[]{#_Toc383523660}[]{#_Toc383523765}[]{#_Toc382921010}[]{#_Toc383272930}[]{#_Toc383273036}[]{#_Toc383273142}[]{#_Toc383523556}[]{#_Toc383523661}[]{#_Toc383523766}

**负载均衡 \-- 负载均衡配置命令 \-- virtual ip address**

------------------------------------------------------------------------

[**[virtual]{lang="EN-US"}**[ **ip** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_447849037}[命令用来配置虚服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址（即]{style="font-family:宋体"}[VSIP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **virtual** **ip** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x1329454965}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1395977476}

[**[virtual]{lang="EN-US"}**[ **ip** **address** *ipv4-address* \[ *mask-length* \| *mask* \]]{lang="EN-US"}]{#struct_0_x7280_11703_566877026}

[**[undo]{lang="EN-US"}**[ **virtual** **ip** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x789560464}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1522973488}

[[虚服务器没有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_x7280_11703_x2032248913}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_154354347}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1782697620}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_863884542}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x69277530}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1187021848}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x941560815}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x7280_11703_x1573777104}[：]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，不能为环回地址、组播地址、广播地址和]{style="font-family:宋体"}[0.X.X.X]{lang="EN-US"}[（如果掩码长度不是]{style="font-family:宋体"}[32]{lang="EN-US"}[，则可以配置]{style="font-family:宋体"}[0.X.X.X]{lang="EN-US"}[）。]{style="font-family:宋体"}

[*[mask-lengh]{lang="EN-US"}*]{#struct_0_x7280_11703_x37792436}[：子网]{style="font-family:宋体"}[掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。本参数在快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器视图下不支持。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x7280_11703_743494986}[：子网]{style="font-family:宋体"}[掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。本参数在快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器视图下不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_154419883}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_2029447311}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_958706505}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] virtual ip address 1.1.1.1 24]{lang="EN-US"}
:::

::: {#714044458 .myid}
[]{#_Toc404796659}[]{#struct_0_x7280_11703_x424748027}[]{#_Toc334536532}[]{#_Toc329869271}[]{#_Toc329242043}[]{#_Toc320886170}

**负载均衡 \-- 负载均衡配置命令 \-- virtual ipv6 address**

------------------------------------------------------------------------

[**[virtual]{lang="EN-US"}**[ **ipv6** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x212752811}[命令用来配置虚服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址（即]{style="font-family:宋体"}[VSIP]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **virtual** **ipv6** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_x1819219573}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x2124445123}

[**[virtual]{lang="EN-US"}**[ **ipv6** **address** *ipv6-address* \[ *prefix-length* \]]{lang="EN-US"}]{#struct_0_x7280_11703_1408520830}

[**[undo]{lang="EN-US"}**[ **virtual** **ipv6** **address**]{lang="EN-US"}]{#struct_0_x7280_11703_154223275}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x545039642}

[[虚服务器没有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x7280_11703_x350803496}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x519662269}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1680730538}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1138657523}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_771513081}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x98899074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_610813259}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x7280_11703_154288811}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，不能为环回地址、]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[组播地址、链路本地地址和全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址（如果前缀长度为]{style="font-family:宋体"}[0]{lang="EN-US"}[，则可以配置全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址）。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x7280_11703_1336862630}[：]{style="font-family:宋体"}[前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。本参数在快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[和]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[类型的虚服务器视图下不支持。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1053819574}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_219967265}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1001::1/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_x561355971}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] virtual ipv6 address 1001::1 64]{lang="EN-US"}
:::

::: {#-976336481 .myid}
[]{#_Toc404796660}[]{#struct_0_x7280_11703_85026818}[]{#_Toc334536529}[]{#_Toc329869268}[]{#_Toc329242040}

**负载均衡 \-- 负载均衡配置命令 \-- virtual-server**

------------------------------------------------------------------------

[**[virtual-server]{lang="EN-US"}**]{#struct_0_x7280_11703_503875983}[命令用来创建虚服务器，并进入虚服务器视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **virtual-server**]{lang="EN-US"}]{#struct_0_x7280_11703_1024668926}[命令用来删除指定的虚服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_154616491}

[**[virtual-server]{lang="EN-US"}**[ *vritual-server-name* \[ **type** { **fast-http** \| **http** \| **ip** \| **tcp** \| **udp** } \]]{lang="EN-US"}]{#struct_0_x7280_11703_1986490697}

[**[undo]{lang="EN-US"}**[ **virtual-server** *vritual-server-name*]{lang="EN-US"}]{#struct_0_x7280_11703_x30509323}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1947567132}

[[不存在任何虚服务器。]{style="font-family:宋体"}]{#struct_0_x7280_11703_1897368518}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1924576249}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1552463357}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1616008483}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x985043670}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_154682027}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x418495788}

[*[vritual-server-name]{lang="EN-US"}*]{#struct_0_x7280_11703_x1650970506}[：虚服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[type]{lang="EN-US"}**[ { **fast-http** \| **http** \| **ip** \| **tcp** \| **udp** }]{lang="EN-US"}]{#struct_0_x7280_11703_x1955466534}[：虚服务器的类型，包括快速]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[、]{style="font-family:宋体"}[TCP]{lang="EN-US"}[和]{style="font-family:宋体"}[UDP]{lang="EN-US"}[五种类型。创建虚服务器时必须指定本参数；而在进入已创建的虚服务器视图时可以不指定本参数，但若要指定本参数，则必须与创建时的类型一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1201072473}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1837811015}[创建]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[，并进入虚服务器视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_161915080}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\]]{lang="EN-US"}
:::

::: {#1715388964 .myid}
[]{#_Toc404796661}[]{#struct_0_x7280_11703_x1095074729}[]{#_Toc400807608}[]{#_Toc396740871}

**负载均衡 \-- 负载均衡配置命令 \-- vpn-instance**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_x7280_11703_x236802837}[命令用来指定虚服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **vpn-instance**]{lang="EN-US"}]{#struct_0_x7280_11703_770559054}[命令来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_471009212}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_x7280_11703_1308362477}

[**[undo]{lang="EN-US"}**[ **vpn-instance**]{lang="EN-US"}]{#struct_0_x7280_11703_x1419494698}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x693945239}

[[虚服务器属于公网。]{style="font-family:宋体"}]{#struct_0_x7280_11703_x1136229285}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1943746983}

[[虚服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1454278603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_1184746027}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x806592439}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_378406924}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x414433618}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x7280_11703_1788376267}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_2037093153}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x1860338374}[指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[类型的虚服务器]{style="font-family:宋体"}[vs3]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1787924428}

[\[Sysname\] virtual-server vs3 type ip]{lang="EN-US"}

[\[Sysname-vs-ip-vs3\] vpn-instance vpn1]{lang="EN-US"}
:::

::: {#452723700 .myid}
[]{#_Toc404796662}[]{#struct_0_x7280_11703_x242219771}[]{#_Toc334536515}[]{#_Toc329869256}[]{#_Toc329241938}

**负载均衡 \-- 负载均衡配置命令 \-- weight**

------------------------------------------------------------------------

[**[weight]{lang="EN-US"}**]{#struct_0_x7280_11703_154092204}[命令用来配置实服务器的权值，即加权轮转和加权最小连接这两种调度算法所使用的权值。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **weight**]{lang="EN-US"}]{#struct_0_x7280_11703_1527994748}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1274060720}

[**[weight]{lang="EN-US"}**[ *weight-value*]{lang="EN-US"}]{#struct_0_x7280_11703_x1548807693}

[**[undo]{lang="EN-US"}**[ **weight**]{lang="EN-US"}]{#struct_0_x7280_11703_x112177023}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x760461645}

[[实服务器的权值为]{style="font-family:宋体"}[100]{lang="EN-US"}]{#struct_0_x7280_11703_x468019742}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x1009061857}

[[实服务器视图]{style="font-family:宋体"}]{#struct_0_x7280_11703_1575780025}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x7280_11703_154157740}

[[network-admin]{lang="EN-US"}]{#struct_0_x7280_11703_1957100587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x7280_11703_x1036245782}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x7280_11703_168536056}

[*[weight-value]{lang="EN-US"}*]{#struct_0_x7280_11703_1335981974}[：权值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。在加权轮转和加权最小连接调度时，该数值越大，实服务器越被优先调用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x7280_11703_x875716772}

[[\# ]{lang="EN-US"}]{#struct_0_x7280_11703_x265175485}[配置实服务器]{style="font-family:宋体"}[rs]{lang="EN-US"}[的权值为]{style="font-family:宋体"}[150]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x7280_11703_1302554560}

[\[Sysname\] real-server rs]{lang="EN-US"}

[\[Sysname-rserver-rs\] weight 150]{lang="EN-US"}
:::
