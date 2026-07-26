::: {#-1422927615 .myid}
[]{#_Toc404793443}[]{#struct_0_x1617_x7307_2124470196}[]{#_Toc394323281}[]{#_Toc387742426}

**SSL VPN \-- SSL VPN配置命令 \-- aaa domain**

------------------------------------------------------------------------

[**[aaa domain]{lang="EN-US"}**]{#struct_0_x1617_x7307_1825581020}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例使用指定的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域进行]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[**[undo aaa domain]{lang="EN-US"}**]{#struct_0_x1617_x7307_x561535018}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2038642097}

[**[aaa domain]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1263668725}

[**[undo aaa domain]{lang="EN-US"}**]{#struct_0_x1617_x7307_x180898877}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x109928301}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x165505377}[访问实例使用缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域进行认证。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1479251921}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1874998468}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1039345643}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1729049465}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1263186600}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_402332545}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1384497384}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符，且不能为字符串"]{style="font-family:宋体"}[d]{lang="EN-US"}["、"]{style="font-family:宋体"}[de]{lang="EN-US"}["、"]{style="font-family:宋体"}[def]{lang="EN-US"}["、"]{style="font-family:宋体"}[defa]{lang="EN-US"}["、"]{style="font-family:宋体"}[defau]{lang="EN-US"}["、"]{style="font-family:宋体"}[defaul]{lang="EN-US"}["、"]{style="font-family:宋体"}[default]{lang="EN-US"}["、"]{style="font-family:宋体"}[i]{lang="EN-US"}["、"]{style="font-family:宋体"}[if]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-u]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-un]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unk]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkn]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkno]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unknow]{lang="EN-US"}["和"]{style="font-family:宋体"}[if-unknown]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x571943737}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_217020287}[用户的用户名中不能携带所属]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域信息。配置本命令后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户将采用指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域内的认证、授权、计费方案对]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户进行认证、授权和计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x667938443}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1351713588}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例使用]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[myserver]{lang="EN-US"}[进行]{style="font-family:宋体"}[AAA]{lang="EN-US"}[认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x690241258}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] aaa domain myserver]{lang="EN-US"}
:::

::::: {#1742433432 .myid}
[]{#_Toc404793444}[]{#struct_0_x1617_x7307_x218582812}[]{#_Toc375835896}[]{#_Toc290542288}

**SSL VPN \-- SSL VPN配置命令 \-- bandwidth**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](SSL%20VPN命令.files/image001.png){#图片 1 width="63" height="25"}]{lang="EN-US"}]{#struct_0_x1617_x7307_x1928402615}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x1617_x7307_x1556428665}
:::

[ ]{lang="EN-US"}

[**[bandwidth]{lang="DA"}**]{#struct_0_x1617_x7307_x1782413484}[命令用来配置接口的期望带宽。]{style="font-family:宋体"}

[**[undo bandwidth]{lang="DA"}**]{#struct_0_x1617_x7307_1964360667}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x192719891}

[**[bandwidth]{lang="EN-US"}**[ *bandwidth-value*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1250161442}

[**[undo bandwidth]{lang="EN-US"}**]{#struct_0_x1617_x7307_1464477648}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1164084097}

[[接口的期望带宽为]{style="font-family:宋体"}[64kbps]{lang="EN-US"}]{#struct_0_x1617_x7307_1241851439}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1485289322}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_x859486347}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1742354155}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1480494705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1232073043}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x971011654}

[*[bandwidth-value]{lang="EN-US"}*]{#struct_0_x1617_x7307_x2127721221}[：]{style="font-family:宋体"}[接口的期望带宽]{style="font-family:宋体"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[400000000]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1409938440}

[[接口的期望带宽会对下列内容有影响：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x2090804443}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CBQ]{lang="EN-US"}]{#struct_0_x1617_x7307_2038174278}[队列带宽。具体介绍请参见"]{style="font-family:宋体"}[ACL]{lang="EN-US"}[和]{style="font-family:宋体"}[QoS]{lang="EN-US"}[配置指导"中的"[拥塞管理]{#_Toc263760148}"。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[链路开销值。具体介绍请参见"三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x844810810}[路由配置指导"中的"]{lang="EN-US" style="font-family:宋体"}[OSPF]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:宋体"}[OSPFv3]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:宋体"}[IS-IS]{lang="EN-US"}["。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1602088495}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x764680184}[配置接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的]{style="font-family:宋体"}[期望带宽]{style="font-family:宋体"}[为]{style="font-family:宋体"}[10000kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_860823949}

[\[Sysname\] interface sslvpn-ac 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\] bandwidth 10000]{lang="EN-US"}
:::::

::: {#-1010598644 .myid}
[]{#_Toc404793445}[]{#struct_0_x1617_x7307_x1543416018}[]{#_Toc398037178}[]{#_Toc397327761}[]{#_Toc398198365}[]{#_Toc398198366}

**SSL VPN \-- SSL VPN配置命令 \-- certificate-authentication enable**

------------------------------------------------------------------------

[**[certificate-authentication enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_1098530342}[命令用来开启证书认证功能。]{style="font-family:宋体"}

[**[undo certificate-authentication enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1925949434}[命令用来关闭证书认证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x433683277}

[**[certificate-authentication]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1617_x7307_x729983119}

[**[undo certificate-authentication enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1496810312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1201208893}

[[证书认证功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_370495213}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_514011431}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1694474168}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2137113911}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_778195332}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1750592055}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1595786446}

[[开启证书认证功能后，需要同时在]{style="font-family:宋体"}[SSL]{lang="EN-US"}]{#struct_0_x1617_x7307_1916315565}[服务器端策略视图下执行]{style="font-family:宋体"}**[client-verify enable]{lang="EN-US"}**[命令。]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关会对]{style="font-family:宋体"}[SSL]{lang="EN-US"}[客户端（]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户）进行基于数字证书的身份验证，并检查]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户的用户名是否与]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户的数字证书中的用户名信息一致。若不一致，则认证不通过，不允许]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_254829335}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x999112078}[开启]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的证书认证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_328612967}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] certificate-authencation enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1895251611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client-verify enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x751311789}[（安全命令参考]{style="font-family:宋体"}[/SSL]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#1948332219 .myid}
[]{#_Toc404793446}[]{#struct_0_x1617_x7307_x820937308}[]{#_Toc375835897}[]{#_Toc290542290}[]{#_Toc398198368}[]{#_Toc398198369}

**SSL VPN \-- SSL VPN配置命令 \-- default**

------------------------------------------------------------------------

[**[default]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1102344926}[命令用来恢复当前接口的缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_831631269}

[**[default]{lang="EN-US"}**]{#struct_0_x1617_x7307_69273629}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_719326321}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_x126754541}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_528428811}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_68600279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_951808871}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1102854267}

[[接口下的某些配置恢复到缺省情况后，会对设备上当前运行的业务产生影响。建议您在执行该命令前，完全了解其对网络产生的影响。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x890622910}

[[可以在执行]{style="font-family:宋体"}**[default]{lang="EN-US"}**]{#struct_0_x1617_x7307_x844612304}[命令后通过]{style="font-family:宋体"}**[display this]{lang="EN-US"}**[命令确认执行效果。对于未能成功恢复缺省的配置，建议您查阅相关功能的命令手册，手工执行恢复该配置缺省情况的命令。如果操作仍然不能成功，您可以通过设备的提示信息定位原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_720513114}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1024949980}[将接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[恢复为缺省配置。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x701412300}

[\[Sysname\] interface sslvpn-ac 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\] default]{lang="EN-US"}

[This command will restore the default settings. Continue? \[Y/N\]:y]{lang="EN-US"}
:::

::: {#1967728818 .myid}
[]{#_Toc404793447}[]{#struct_0_x1617_x7307_770050091}[]{#_Toc394323279}[]{#_Toc387742424}[]{#_Toc398198371}[]{#_Toc398198372}

**SSL VPN \-- SSL VPN配置命令 \-- default-policy-group**

------------------------------------------------------------------------

[**[default-policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x377288225}[命令用来指定某个策略组为缺省策略组。]{style="font-family:宋体"}

[**[undo default-policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_1635357570}[命令用来取消缺省策略组。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_203470701}

[**[default-policy-group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1411885737}

[**[undo default-policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1891278353}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x485107623}

[[没有指定缺省策略组。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x508583370}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x435454804}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1956646951}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1402705624}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_881888707}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1109759060}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_205339906}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1145288664}[：策略组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2109084797}

[[一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1017702862}[访问实例下可以配置多个策略组。远端接入用户访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例时，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器将授权给该用户的策略组信息下发给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。该用户可以访问的资源由授权的策略组决定。如果]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器没有为该用户进行授权，则用户可以访问的资源由缺省策略组决定。]{style="font-family:宋体"}

[[本命令中指定的策略组必须为已经通过]{style="font-family:宋体"}**[policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1582687340}[命令创建的策略组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1059634669}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1449756145}[指定名为]{style="font-family:宋体"}[pg1]{lang="EN-US"}[的策略组为缺省策略组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_2056940899}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\] quit]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] default-policy-group pg1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x540338370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_705148381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x168645419}
:::

::: {#-1461383778 .myid}
[]{#_Toc404793448}[]{#struct_0_x1617_x7307_x214013812}[]{#_Toc375835898}[]{#_Toc398739067}[]{#_Toc398739165}

**SSL VPN \-- SSL VPN配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x1617_x7307_23098343}[命令用来配置当前接口的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x1617_x7307_1595926064}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1009467585}

[**[description]{lang="EN-US"}**[ *text*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1879932609}

[**[undo]{lang="EN-US"}**[ **description**]{lang="EN-US"}]{#struct_0_x1617_x7307_305809927}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1177989947}

[[接口的描述信息为"*接口名*]{style="font-family:宋体"}[ Interface]{lang="EN-US"}]{#struct_0_x1617_x7307_x740414576}["，例如：]{style="font-family:宋体"}[SSLVPN-AC1000 Interface]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1789017832}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_116327796}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1789232205}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1529704835}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x222491634}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1624733172}

[*[text]{lang="EN-US"}*]{#struct_0_x1617_x7307_1217368392}[：接口的描述字符串，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x166090215}

[[当设备上存在多个接口时，可以根据接口的连接信息或用途来配置接口的描述信息，以便区别和管理各接口。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x440000417}

[[本命令仅用于标识某接口，并无特别的功能。使用]{style="font-family:宋体"}**[display interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_2134249577}[等命令可以看到设置的描述信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1523660944}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_168440729}[配置接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的描述信息为"]{style="font-family:宋体"}[SSL VPN A]{lang="EN-US"}["。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1327355079}

[\[Sysname\] interface sslvpn-ac 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\] description SSL VPN A]{lang="EN-US"}
:::

::: {#-1782221145 .myid}
[]{#_Toc404793449}[]{#struct_0_x1617_x7307_812045873}[]{#_Toc375835899}[]{#_Toc398198376}[]{#_Toc398198377}[]{#_Toc398198378}[]{#_Toc398198379}

**SSL VPN \-- SSL VPN配置命令 \-- display interface sslvpn-ac**

------------------------------------------------------------------------

[**[display interface ]{lang="EN-US"}**]{#struct_0_x1617_x7307_496366044}**[sslvpn-ac]{lang="DE"}**[命令用来显示]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_708525963}

[**[display interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1093460249}**[sslvpn-ac]{lang="DE"}**[ \[ *interface-number* \] \] \[ **brief** \[ **description** \| **down** \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_354803303}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1361168055}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1312510246}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1436936093}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_811415767}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x113405075}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_1197551731}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1539316882}

[*[interface-number]{lang="DE"}*]{#struct_0_x1617_x7307_x1815753470}[：]{style="font-family:宋体"}[SSL VPN AC]{lang="DE"}[接口的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[brief]{lang="EN-US"}**]{#struct_0_x1617_x7307_1555532519}[：显示接口的概要信息。如果不指定该参数，则显示接口的详细信息。]{style="font-family:宋体"}

[**[description]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1720173770}[：用来显示用户配置的接口的全部描述信息。如果某接口的描述信息超过]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，不指定该参数时，只显示描述信息中的前]{style="font-family:宋体"}[27]{lang="EN-US"}[个字符，超出部分不显示；指定该参数时，可以显示全部描述信息。]{style="font-family:宋体"}

[**[down]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1922069072}[：显示当前物理状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[down]{lang="EN-US"}[的原因。如果不指定该参数，则不会根据接口物理状态来过滤显示信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1290368256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型]{style="font-family:宋体"}]{#struct_0_x1617_x7307_338473787}**[sslvpn-ac]{lang="DE"}**[，将显示设备支持的所有接口的相关信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型，不指定接口编号]{lang="EN-US" style="font-family:宋体"}*[interface-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_249548007}[，则显示所有]{lang="EN-US" style="font-family:
宋体"}[SSL VPN AC]{lang="DE"}[接口的信息。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则显示指定]{style="font-family:宋体"}]{#struct_0_x1617_x7307_472623692}[SSL VPN AC]{lang="DE"}[接口的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1025559066}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x200223151}[显示接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1074168800}[display interface sslvpn-ac 1000]{lang="NL-BE"}

[SSLVPN-AC1000]{lang="NL-BE"}

[Current state: UP]{lang="NL-BE"}

[Line protocol state: DOWN]{lang="NL-BE"}

[Description: SSLVPN-AC1000 Interface]{lang="NL-BE"}

[Bandwidth: 64kbps]{lang="NL-BE"}

[Maximum Transmit Unit: 1500]{lang="NL-BE"}

[Internet protocol processing: disabled]{lang="NL-BE"}

[Link layer protocol is SSLVPN]{lang="NL-BE"}

[Last clearing of counters: Never]{lang="NL-BE"}

[Last 300 seconds input rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="NL-BE"}

[Last 300 seconds output rate: 0 bytes/sec, 0 bits/sec, 0 packets/sec]{lang="NL-BE"}

[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}

[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}

[[表1-1 ]{lang="EN-US"}[display interface]{lang="EN-US"}]{#struct_0_x1617_x7307_1830953772}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x706740044}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_595036306}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_881636965}

[[SSLVPN-AC1000]{lang="NL-BE"}]{#struct_0_x1617_x7307_821841743}

[[接口]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x314535196}[SSL VPN AC 1000]{lang="NL-BE"}[的相关信息]{style="font-family:宋体"}

[[C]{lang="NL-BE"}[urrent state]{lang="EN-US"}]{#struct_0_x1617_x7307_2038707633}

[[接口的物理状态和管理状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1133685419}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administr]{lang="EN-US"}]{#struct_0_x1617_x7307_1306643921}[a]{lang="EN-US"}[t]{lang="EN-US"}[ive]{lang="EN-US"}[ly DOWN]{lang="EN-US"}[：表示该接口已经通过]{lang="EN-US" style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令被关闭，即管理状态为关闭]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2005487861}[：该接口的管理状态为开启，但物理状态为关闭]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1617_x7307_783509945}[：该接口的管理状态和物理状态均为开启]{style="font-family:宋体"}

[[Line protocol state]{lang="EN-US"}]{#struct_0_x1617_x7307_705833941}

[[接口的链路层协议状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1547355288}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1617_x7307_1980000368}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (spoofing)]{lang="EN-US"}]{#struct_0_x1617_x7307_x43681928}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1617_x7307_x997256356}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1617_x7307_x672067916}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x690175722}

[[Bandwidth]{lang="NL-BE"}]{#struct_0_x1617_x7307_x611024012}

[[接口的期望带宽，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}]{#struct_0_x1617_x7307_x850877403}

[[Maximum Transmit Unit]{lang="EN-US"}]{#struct_0_x1617_x7307_x2002271536}

[[接口的最大传输单元]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1176082495}

[[Internet protocol processing]{lang="EN-US"}]{#struct_0_x1617_x7307_x1879368140}

[[接口的]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1219621166}[IP]{lang="NO-BOK"}[地址。如果没有为接口配置]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[地址，则该字段显示为]{style="font-family:宋体"}[Internet protocol processing: disabled]{lang="EN-US"}[，表示不能处理]{style="font-family:宋体"}[IP]{lang="NO-BOK"}[报文]{style="font-family:宋体"}

[[Primary]{lang="EN-US"}]{#struct_0_x1617_x7307_x1964279481}[表示该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Link layer protocol]{lang="NL-BE"}]{#struct_0_x1617_x7307_793140459}

[[链路层协议类型]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1232138579}

[[Last clearing of counters]{lang="EN-US"}]{#struct_0_x1617_x7307_x1761691177}

[[最近一次使用]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2052279877}[命令清除接口下的统计信息的时间（如果从设备启动一直没有执行]{style="font-family:宋体"}**[reset counters interface]{lang="EN-US"}**[命令清除过该接口下的统计信息，则显示]{style="font-family:宋体"}[Never]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Last 300 seconds input rate]{lang="EN-US"}]{#struct_0_x1617_x7307_x1183672260}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1617_x7307_1674892682}[秒钟的平均输入速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输入的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输入的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输入的包数]{style="font-family:宋体"}

[[Last 300 seconds output rate]{lang="EN-US"}]{#struct_0_x1617_x7307_1546657084}

[[最近]{style="font-family:宋体"}[300]{lang="EN-US"}]{#struct_0_x1617_x7307_x1558971244}[秒钟的平均输出速率：]{style="font-family:宋体"}[bytes/sec]{lang="EN-US"}[表示平均每秒输出的字节数，]{style="font-family:宋体"}[bits/sec]{lang="EN-US"}[表示平均每秒输出的比特数，]{style="font-family:宋体"}[packets/sec]{lang="EN-US"}[表示平均每秒输出的包数]{style="font-family:宋体"}

[[Input: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_x1617_x7307_x1100655054}

[[总计输入的报文数，总计输入的字节，总计丢弃的输入报文数]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1496744776}

[[Output: 0 packets, 0 bytes, 0 drops]{lang="NL-BE"}]{#struct_0_x1617_x7307_1491383072}

[[总计输出的报文数，总计输出的字节，总计丢弃的输出报文数]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x104137986}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_184438440}[显示所有]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[类型接口的概要信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface sslvpn-ac brief]{lang="EN-US"}]{#struct_0_x1617_x7307_x1619562099}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[SSLVPN-AC1000        DOWN DOWN     \--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1686117031}[显示接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的概要信息，包括用户配置的全部描述信息。]{style="font-family:宋体"}

[[\<Sysname\> display interface sslvpn-ac 1000 brief description]{lang="EN-US"}]{#struct_0_x1617_x7307_x1753321907}

[Brief information of interface(s) under route mode:]{lang="EN-US"}

[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}

[Protocol: (s) - spoofing]{lang="EN-US"}

[Interface            Link Protocol Main IP         Description]{lang="EN-US"}

[SSLVPN-AC1000        UP    UP      1.1.1.1         SSLVPN-AC1000 Interface]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1228134580}[显示当前状态为]{style="font-family:宋体"}[down]{lang="EN-US"}[的接口的信息以及]{style="font-family:宋体"}[DOWN]{lang="EN-US"}[的原因。]{style="font-family:宋体"}

[[\<Sysname\> display interface brief down]{lang="EN-US"}]{#struct_0_x1617_x7307_69339165}

[Brief information of interface(s) under route mode:]{lang="NL-BE"}

[Link: ADM - administratively down; Stby - standby]{lang="NL-BE"}

[Interface            Link Cause]{lang="NL-BE"}

[SSLVPN-AC1000]{lang="EN-US"}[        DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[SSLVPN-AC1001]{lang="EN-US"}[        DOWN ]{lang="NL-BE"}[Administratively]{lang="EN-US"}

[]{#struct_0_x1617_x7307_x1602479286}[[表1-2 ]{lang="EN-US"}[display interface brief]{lang="EN-US"}]{#_Ref129008332}[命令显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_x710589796}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x32670076}

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1189412487}

[[Brief information of interface(s) under route mode:]{lang="EN-US"}]{#struct_0_x1617_x7307_x1938659197}

[[三层模式下（]{style="font-family:宋体"}[route]{lang="EN-US"}]{#struct_0_x1617_x7307_x24458447}[）的接口的概要信息，即三层接口的概要信息]{style="font-family:宋体"}

[[Link: ADM - administratively down; Stby - standby]{lang="EN-US"}]{#struct_0_x1617_x7307_1996308166}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1617_x7307_2089333750}[属性值为"]{style="font-family:宋体"}[ADM]{lang="EN-US"}["，则表示该接口被管理员手工关闭了，需要在该接口下执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复接口本身的物理状态]{style="font-family:宋体"}

[[如果某接口的]{style="font-family:宋体"}[Link]{lang="EN-US"}]{#struct_0_x1617_x7307_x1262029394}[属性值为"]{style="font-family:宋体"}[Stby]{lang="EN-US"}["，则表示该接口是一个备份接口，使用]{style="font-family:宋体"}**[display interface-backup state]{lang="EN-US"}**[命令可以查看该备份接口对应的主接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol: (s) - spoofing]{lang="EN-US"}]{#struct_0_x1617_x7307_1046610849}

[[如果某接口的]{style="font-family:宋体"}[Protocol]{lang="EN-US"}]{#struct_0_x1617_x7307_x1838595184}[属性值中带有"]{style="font-family:宋体"}[(s)]{lang="EN-US"}["字符串，则表示该接口的网络层协议状态显示是]{style="font-family:宋体"}[UP]{lang="EN-US"}[的，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x1617_x7307_x1970475851}

[[接口名称缩写]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1635423106}

[[Link]{lang="EN-US"}]{#struct_0_x1617_x7307_1761708337}

[[接口物理连接状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_735948431}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1617_x7307_2019375162}[：表示本链路物理上是连通的]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1617_x7307_186865104}[：表示本链路物理上]{lang="EN-US" style="font-family:宋体"}[是]{style="font-family:宋体"}[不通的]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ADM]{lang="EN-US"}]{#struct_0_x1617_x7307_x1064974303}[：表示本链路被手工关闭了，需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Stby]{lang="EN-US"}]{#struct_0_x1617_x7307_x905591173}[：表示该接口是一个备份接口。本状态的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_x1617_x7307_1469408737}

[[接口的链路层协议状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1724821105}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP]{lang="EN-US"}]{#struct_0_x1617_x7307_x161634446}[：表示该接口的链路层协议状态为开启]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UP (s)]{lang="EN-US"}]{#struct_0_x1617_x7307_x1449690609}[：表示该接口的链路层协议状态为开启，但实际可能没有对应的链路，或者所对应的链路不是永久存在而是按需建立。通常]{style="font-family:宋体"}[NULL]{lang="EN-US"}[、]{style="font-family:宋体"}[LoopBack]{lang="EN-US"}[等接口会具有该属性]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DOWN]{lang="EN-US"}]{#struct_0_x1617_x7307_1894297860}[：表示该接口的链路层协议状态为关闭]{style="font-family:宋体"}

[[Main IP]{lang="EN-US"}]{#struct_0_x1617_x7307_1271975308}

[[接口主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x1813671503}[地址]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x1617_x7307_1709168769}

[[接口的描述信息]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1382496088}

[[Cause]{lang="EN-US"}]{#struct_0_x1617_x7307_276262663}

[[接口物理连接状态为]{style="font-family:宋体"}[down]{lang="EN-US"}]{#struct_0_x1617_x7307_1335952175}[的原因，取值为：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively]{lang="EN-US"}]{#struct_0_x1617_x7307_116393332}[：表示本链路被手工关闭了（配置了]{style="font-family:宋体"}**[shutdown]{lang="EN-US"}**[命令），需要执行]{style="font-family:宋体"}**[undo shutdown]{lang="EN-US"}**[命令才能恢复真实的物理状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Not connected]{lang="EN-US"}]{#struct_0_x1617_x7307_619294836}[：]{lang="EN-US" style="font-family:宋体"}[表示物理层不通]{style="font-family:宋体"}

[ ]{lang="NL-BE"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1428723449}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset counters interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_x883650220}

::: {#-370668251 .myid}
[]{#_Toc404793450}[]{#struct_0_x1617_x7307_x1123597014}[]{#_Toc394323276}[]{#_Toc387742421}[]{#_Toc383884621}[]{#_Toc398198381}[]{#_Toc398198382}[]{#_Toc398198383}

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn context**

------------------------------------------------------------------------

[**[display ]{lang="NO-BOK"}[sslvpn ]{lang="EN-US"}[context]{lang="EN-US"}**]{#struct_0_x1617_x7307_x398183682}[命令用来显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x694237239}

[**[display sslvpn context ]{lang="EN-US"}**[\[ **brief** \| **name** *context-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_1473485340}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1824952912}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x2121786384}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1114903574}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_296199728}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_2000188983}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_602586088}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_x1053681829}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1093394713}

[**[brief]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1892313039}[：显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的简要信息。如果不指定本参数，则显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的详细信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_633982359}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的详细信息。]{style="font-family:宋体"}*[context-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1927179570}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1026837815}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn context]{lang="EN-US"}]{#struct_0_x1617_x7307_6274620}

[Context name: ctx1]{lang="EN-US"}

[  Operation status: Down]{lang="EN-US"}

[  Down reason: Administratively down]{lang="EN-US"}

[  AAA domain: domain1]{lang="EN-US"}

[  Certificate authentication: Enabled]{lang="EN-US"}

[  Dynamic password: Enabled]{lang="EN-US"}

[  Verify code validation: Enabled]{lang="EN-US"}

[  Default policy group not configured]{lang="EN-US"}

[  Domain name and virtual host not configured]{lang="EN-US"}

[  Maximum users allowed: 200]{lang="EN-US"}

[  VPN-instance]{lang="EN-US"}[：]{style="font-family:宋体"}[vpn1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Context name: ctx2]{lang="EN-US"}

[  Operation status: Up]{lang="EN-US"}

[  AAA domain not specified]{lang="EN-US"}

[  Certificate authentication: Disabled]{lang="EN-US"}

[  Dynamic password: Disabled]{lang="EN-US"}

[  Verify code validation: Disabled]{lang="EN-US"}

[  Default group policy: gp]{lang="EN-US"}

[  Associated SSL VPN gateway: gw2]{lang="EN-US"}

[  Virtual host: abc.com]{lang="EN-US"}

[  Maximum users allowed: 200]{lang="EN-US"}

[  VPN-instance not configured]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display sslvpn context]{lang="EN-US"}]{#struct_0_x1617_x7307_x545708961}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x714076626}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_472689228}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_894699170}

[[Context name]{lang="EN-US"}]{#struct_0_x1617_x7307_1916785441}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2068684135}[访问实例的名称]{style="font-family:宋体"}

[[Operation status]{lang="EN-US"}]{#struct_0_x1617_x7307_1889269176}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_417679224}[访问实例的操作状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1617_x7307_2027620771}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例处于运行状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1617_x7307_1564485540}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例未处于运行状态]{style="font-family:宋体"}

[[Down reason]{lang="EN-US"}]{#struct_0_x1617_x7307_x1807836598}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_5458376}[访问实例处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的原因，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_x1617_x7307_x1067755215}[：管理]{lang="EN-US" style="font-family:
  宋体"}[down]{lang="EN-US"}[，即未通过]{lang="EN-US" style="font-family:
  宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No gateway associated]{lang="EN-US"}]{#struct_0_x1617_x7307_x146096181}[：]{lang="EN-US" style="font-family:
  宋体"}[SSL VPN]{lang="EN-US"}[访问实例未引用]{lang="EN-US" style="font-family:
  宋体"}[SSL VPN]{lang="EN-US"}[网关]{lang="EN-US" style="font-family:宋体"}

[[AAA domain]{lang="EN-US"}]{#struct_0_x1617_x7307_2038773169}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1659208420}[访问实例使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}

[[Certificate authentication]{lang="EN-US"}]{#struct_0_x1617_x7307_1839153073}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1588890010}[访问实例是否开启证书认证功能]{style="font-family:宋体"}

[[Dynamic password]{lang="EN-US"}]{#struct_0_x1617_x7307_x1401588118}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1571792307}[访问实例是否开启动态口令验证功能]{style="font-family:宋体"}

[[Verify code validation]{lang="EN-US"}]{#struct_0_x1617_x7307_2108842431}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1289867986}[访问实例是否开启验证码验证功能]{style="font-family:宋体"}

[[Default policy group]{lang="EN-US"}]{#struct_0_x1617_x7307_1961669771}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x690110186}[访问实例使用的缺省策略组]{style="font-family:宋体"}

[[Associated SSL VPN gateway]{lang="EN-US"}]{#struct_0_x1617_x7307_925771161}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2056572446}[访问实例引用的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_x1617_x7307_583675777}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1365616364}[访问实例的域名]{style="font-family:宋体"}

[[Virtual host]{lang="EN-US"}]{#struct_0_x1617_x7307_1100091174}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x6055798}[访问实例的虚拟主机名称]{style="font-family:宋体"}

[[Maximum users allowed]{lang="EN-US"}]{#struct_0_x1617_x7307_1914907673}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_395933852}[访问实例的最大用户会话数]{style="font-family:宋体"}

[[VPN-instance]{lang="EN-US"}]{#struct_0_x1617_x7307_1232204115}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_614482672}[访问实例关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1550554183}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn context brief]{lang="EN-US"}]{#struct_0_x1617_x7307_1848165006}

[Context name      Gateway       Domain/VHost      VRF       Admin  Operation]{lang="EN-US"}

[ctx1              -             -                 -         Down   Down]{lang="EN-US"}

[ctx2              gw2           abc.com           -         Up     Up]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display sslvpn context brief]{lang="EN-US"}]{#struct_0_x1617_x7307_1179051494}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x718016848}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1621639069}

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x877209434}

[[Context name]{lang="EN-US"}]{#struct_0_x1617_x7307_x1855199129}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1721867432}[访问实例的名称]{style="font-family:宋体"}

[[Gateway]{lang="EN-US"}]{#struct_0_x1617_x7307_148034453}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1333414404}[访问实例引用的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}

[[Domain/VHost]{lang="EN-US"}]{#struct_0_x1617_x7307_x1496679240}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x115492072}[访问实例的域名或虚拟主机名称]{style="font-family:宋体"}

[[VRF]{lang="EN-US"}]{#struct_0_x1617_x7307_681961836}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1844611916}[访问实例关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}

[[Admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x829638610}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1829021297}[访问实例的管理状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_x1617_x7307_665364594}[：已通过]{lang="EN-US" style="font-family:宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_x1617_x7307_490389338}[：未通过]{lang="EN-US" style="font-family:宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN ]{lang="EN-US"}[访问实例]{lang="EN-US" style="font-family:宋体"}

[[Operation]{lang="EN-US"}]{#struct_0_x1617_x7307_x344614692}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1418149675}[访问实例的操作状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[up]{lang="EN-US"}]{#struct_0_x1617_x7307_69404701}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例处于运行状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[down]{lang="EN-US"}]{#struct_0_x1617_x7307_834745136}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例未处于运行状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1072444481 .myid}
[]{#_Toc404793451}[]{#struct_0_x1617_x7307_135975312}[]{#_Toc394323271}[]{#_Toc387742416}[]{#_Toc383884622}

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn gateway**

------------------------------------------------------------------------

[**[display ]{lang="NO-BOK"}[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_94750433}[命令用来显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1592826573}

[**[display sslvpn gateway ]{lang="EN-US"}**[\[ **brief** \| **name** *gateway-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_1531592929}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1962410577}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1938021368}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1520799347}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_615896571}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_1810153771}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1448302792}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_87008694}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1352806001}

[**[brief]{lang="EN-US"}**]{#struct_0_x1617_x7307_1635488642}[：显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的简要信息。如果不指定本参数，则显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的详细信息。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *gateway-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1447642774}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的详细信息。]{style="font-family:宋体"}*[gateway-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1456982473}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_289815223}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn gateway]{lang="EN-US"}]{#struct_0_x1617_x7307_x633838958}

[Gateway name: gw1]{lang="EN-US"}

[  Operation status: Up]{lang="EN-US"}

[  IP: 192.168.10.75, port: 443]{lang="EN-US"}

[  HTTP redirect port: 80]{lang="EN-US"}

[  SSL server-policy: ssl]{lang="EN-US"}

[  Front VPN-instance: vpn1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Gateway name: gw2]{lang="EN-US"}

[  Operation status: Down]{lang="EN-US"}

[  Down reason: Administratively down]{lang="EN-US"}

[  Gateway IP address not configured]{lang="EN-US"}

[  SSL server-policy: ssl1]{lang="EN-US"}

[  Front VPN-instance not configured]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display sslvpn gateway]{lang="EN-US"}]{#struct_0_x1617_x7307_1884719083}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x690859644}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1124026060}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1660466512}

[[Gateway name]{lang="EN-US"}]{#struct_0_x1617_x7307_x1933951181}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x307360084}[网关的名称]{style="font-family:宋体"}

[[Operation status]{lang="EN-US"}]{#struct_0_x1617_x7307_x1449625073}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1328656739}[网关的操作状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1617_x7307_666756475}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关处于运行状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1617_x7307_x1383528470}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关未处于运行状态]{style="font-family:宋体"}

[[Down reason]{lang="EN-US"}]{#struct_0_x1617_x7307_901891453}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1763571329}[网关处于]{style="font-family:宋体"}[down]{lang="EN-US"}[状态的原因，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Administratively down]{lang="EN-US"}]{#struct_0_x1617_x7307_x988559419}[：管理]{lang="EN-US" style="font-family:
  宋体"}[down]{lang="EN-US"}[，即没有通过]{lang="EN-US" style="font-family:
  宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[No gateway IP]{lang="EN-US"}]{#struct_0_x1617_x7307_1003754639}[：未配置]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VPN instance not exist]{lang="EN-US"}]{#struct_0_x1617_x7307_x1091832328}[：]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关所属的]{lang="EN-US" style="font-family:宋体"}[VPN]{lang="EN-US"}[实例不存在]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Applying SSL server-policy failed]{lang="EN-US"}]{#struct_0_x1617_x7307_1785749932}[：为]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关应用]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略失败]{lang="EN-US" style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_116458868}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1060983207}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[port]{lang="EN-US"}]{#struct_0_x1617_x7307_774179613}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1810787817}[网关的端口号]{style="font-family:宋体"}

[[HTTP redirect port]{lang="EN-US"}]{#struct_0_x1617_x7307_x1824097952}

[[HTTP]{lang="EN-US"}]{#struct_0_x1617_x7307_x359738001}[重定向端口号]{style="font-family:宋体"}

[[SSL server-policy]{lang="EN-US"}]{#struct_0_x1617_x7307_x1922721916}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1586506751}[网关引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略名称]{style="font-family:宋体"}

[[Front VPN-instance]{lang="EN-US"}]{#struct_0_x1617_x7307_x1624547329}

[[前端]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1093329177}[实例名称，即]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_795738840}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn gateway brief]{lang="EN-US"}]{#struct_0_x1617_x7307_1678880770}

[Gateway name                    Admin  Operation]{lang="EN-US"}

[gw1                             Up     Up]{lang="EN-US"}

[gw2                             Down   Down (Administratively down)]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display sslvpn gateway brief]{lang="EN-US"}]{#struct_0_x1617_x7307_2052797445}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x688006774}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2050091064}

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1740350459}

[[Gateway name]{lang="EN-US"}]{#struct_0_x1617_x7307_1768702971}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_106904729}[网关的名称]{style="font-family:宋体"}

[[Admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1209105408}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x356232574}[网关的管理状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1617_x7307_x1720710998}[：已通过]{lang="EN-US" style="font-family:宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1617_x7307_391072848}[：未通过]{lang="EN-US" style="font-family:宋体"}**[service enable]{lang="EN-US"}**[命令开启]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{lang="EN-US" style="font-family:宋体"}

[[Operation]{lang="EN-US"}]{#struct_0_x1617_x7307_472754764}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_528853608}[网关的操作状态，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Up]{lang="EN-US"}]{#struct_0_x1617_x7307_138629121}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关处于运行状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Down]{lang="EN-US"}]{#struct_0_x1617_x7307_1253239886}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关未处于运行状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#435703138 .myid}
[]{#_Toc404793452}[]{#struct_0_x1617_x7307_1498043784}[]{#_Toc394323284}[]{#_Toc387742429}[]{#_Toc383884625}[]{#_Toc398739072}[]{#_Toc398739170}

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn policy-group**

------------------------------------------------------------------------

[**[display sslvpn policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_1737554644}[命令用来显示指定策略组的信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2060238329}

[**[display sslvpn policy-group ]{lang="EN-US"}***[group-name ]{lang="EN-US"}*[\[ **context** *context-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_554066253}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1184347552}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1937497575}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x331303229}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x276539697}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_x1363744522}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x671288467}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_2038838705}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x875516822}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x602882560}[：策略组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[**[context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x318306131}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的指定策略组的信息。]{style="font-family:宋体"}*[context-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的指定名称的策略组信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1013955445}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x2133630509}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下名称为]{style="font-family:宋体"}[pg1]{lang="EN-US"}[的策略组的信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn policy-group pg1]{lang="EN-US"}]{#struct_0_x1617_x7307_1012721118}

[Group policy: pg1]{lang="EN-US"}

[  Context: context1]{lang="EN-US"}

[   Idle timeout: 2100 sec ]{lang="EN-US"}

[  Context: context2]{lang="EN-US"}

[   Idle timeout: 4000 sec ]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display sslvpn policy-group]{lang="EN-US"}]{#struct_0_x1617_x7307_631214122}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x688985222}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1667272030}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1081477808}

[[Group policy]{lang="EN-US"}]{#struct_0_x1617_x7307_845665471}

[[策略组名称]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1879469037}

[[Context]{lang="EN-US"}]{#struct_0_x1617_x7307_x690044650}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x223217751}[访问实例名称]{style="font-family:宋体"}

[[Idle timeout]{lang="EN-US"}]{#struct_0_x1617_x7307_x310932458}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1531647543}[会话可以保持空闲状态的最长时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-123752958 .myid}
[]{#_Toc404793453}[]{#struct_0_x1617_x7307_588525453}[]{#_Toc394323290}[]{#_Toc392947642}[]{#_Toc392688533}

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn port-forward connection**

------------------------------------------------------------------------

[**[display sslvpn port-forward connection]{lang="EN-US"}**]{#struct_0_x1617_x7307_277100825}[命令用来显示]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口转发的连接信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_80511912}

[**[display sslvpn port-forward connection]{lang="EN-US"}**[ \[ **context** *context-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_x1771593343}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_899908645}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1907448689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_529778758}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_67484899}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_x1766765405}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x961572860}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_1232269651}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2136819101}

[**[context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1029322703}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口转发连接信息。]{style="font-family:宋体"}*[context-name]{lang="EN-US"}*[ ]{lang="EN-US"}[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口转发连接信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x204792519}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1769146448}[显示名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口转发的连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn port-forward connection context ctx1]{lang="EN-US"}]{#struct_0_x1617_x7307_x1424355502}

[SSL VPN context: ctx1]{lang="EN-US"}

[Client IP   Client port      Server IP       Server port  Status]{lang="EN-US"}

[192.0.2.1   1025             192.168.0.39    80           Connected]{lang="EN-US"}

[192.0.2.2   1026             192.168.0.35    23           Connecting]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_922411419}[显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口转发的连接信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn port-forward connection]{lang="EN-US"}]{#struct_0_x1617_x7307_x422871194}

[SSL VPN context: ctx1]{lang="EN-US"}

[Client IP   Client port      Server IP       Server port  Status]{lang="EN-US"}

[192.0.2.1   1025             192.168.0.39    80           Connected]{lang="EN-US"}

[192.0.2.2   1026             192.168.0.35    23           Connecting]{lang="EN-US"}

[ ]{lang="EN-US"}

[SSL VPN context: ctx2]{lang="EN-US"}

[Client IP   Client port      Server IP       Server port  Status]{lang="EN-US"}

[192.0.2.3   1025             192.168.0.39    80           Connected]{lang="EN-US"}

[192.0.2.4   1026             192.168.0.35    23           Connected]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display sslvpn port-forward connection]{lang="EN-US"}]{#struct_0_x1617_x7307_x70355330}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x695901808}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1300530009}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1496613704}

[[Client IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x2128757399}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x517747471}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Client port]{lang="EN-US"}]{#struct_0_x1617_x7307_x471447717}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1542698619}[客户端的本地端口号]{style="font-family:宋体"}

[[Server IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x2128887956}

[[企业网内服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x192009233}[地址]{style="font-family:宋体"}

[[Server port]{lang="EN-US"}]{#struct_0_x1617_x7307_667880399}

[[企业网内服务器的端口号]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1111454437}

[[Status]{lang="EN-US"}]{#struct_0_x1617_x7307_x779735969}

[[连接状态，取值包括：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_236150900}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connected]{lang="EN-US"}]{#struct_0_x1617_x7307_69470237}[：连接成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Connecting]{lang="EN-US"}]{#struct_0_x1617_x7307_x1835811175}[：正在连接]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1052589611 .myid}
[]{#_Toc404793454}[]{#struct_0_x1617_x7307_162046087}[]{#_Toc394323285}[]{#_Toc387742430}[]{#_Toc398739075}[]{#_Toc398739173}

**SSL VPN \-- SSL VPN配置命令 \-- display sslvpn session**

------------------------------------------------------------------------

[**[display sslvpn session]{lang="EN-US"}**]{#struct_0_x1617_x7307_1519465306}[命令用来显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_101933681}

[**[display sslvpn session]{lang="EN-US"}**[ \[ **context** *context-name* \] \[ **user** *user-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_1335815807}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x852439796}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_542909133}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1826461560}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1997383669}

[[network-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_163904253}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_298384979}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x1617_x7307_x537904715}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_51777674}

[**[context ]{lang="EN-US"}***[context-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1084779476}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}*[context-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。如果不指定本参数，则显示所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话信息。]{style="font-family:宋体"}

[**[user ]{lang="EN-US"}***[user-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1635554178}[：显示指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户对应的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话的详细信息。]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。如果不指定本参数，则显示指定或所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1004356104}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x813822653}[显示名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn session context ctx1]{lang="EN-US"}]{#struct_0_x1617_x7307_1521019366}

[SSL VPN context: ctx1]{lang="EN-US"}

[Login name  User IP address Connections Created  Idle time]{lang="EN-US"}

[user1       192.0.2.1       2           04:47:16 00:01:26]{lang="EN-US"}

[user2       192.0.2.2       2           04:48:36 00:01:56]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display sslvpn session]{lang="EN-US"}]{#struct_0_x1617_x7307_583290200}[命令简要显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x694001858}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1889604538}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1461221573}

[[SSL VPN context]{lang="EN-US"}]{#struct_0_x1617_x7307_x1272592214}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_901762783}[访问实例名称]{style="font-family:宋体"}

[[Login name]{lang="EN-US"}]{#struct_0_x1617_x7307_x1993304285}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1889155162}[会话的登录用户名称]{style="font-family:宋体"}

[[User IP address]{lang="EN-US"}]{#struct_0_x1617_x7307_x1449559537}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2095154217}[会话使用的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Connections]{lang="EN-US"}]{#struct_0_x1617_x7307_x1259921866}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1086710915}[会话对应的连接数目]{style="font-family:宋体"}

[[Created]{lang="EN-US"}]{#struct_0_x1617_x7307_1722511302}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x49567785}[会话的创建时间]{style="font-family:宋体"}

[[Idle time]{lang="EN-US"}]{#struct_0_x1617_x7307_1254726405}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2132514546}[会话的空闲时间]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1398070294}[显示]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户]{style="font-family:宋体"}[user1]{lang="EN-US"}[对应的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display sslvpn session user user1]{lang="EN-US"}]{#struct_0_x1617_x7307_116524404}

[User        : user1 ]{lang="EN-US"}

[Context     : context1 ]{lang="EN-US"}

[Policy group: Default]{lang="EN-US"}

[Connections : 1                 User IP address: 192.168.56.1]{lang="EN-US"}

[Idle time   : 00:00:02          Created        : 13:49:27 UTC Wed 05/14/2014]{lang="EN-US"}

[Idle timeout: 2100 sec]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display sslvpn session]{lang="EN-US"}]{#struct_0_x1617_x7307_2031167102}[命令详细显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x700014472}[[字段]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x688018840}

[[描述]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x141910231}

[[User]{lang="EN-US"}]{#struct_0_x1617_x7307_x159968846}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x243820606}[用户的名称]{style="font-family:宋体"}

[[Context]{lang="EN-US"}]{#struct_0_x1617_x7307_185733586}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1247486421}[用户所属的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例]{style="font-family:宋体"}

[[Policy group]{lang="EN-US"}]{#struct_0_x1617_x7307_x453936987}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2107951276}[用户使用的策略组]{style="font-family:宋体"}

[[Connections]{lang="EN-US"}]{#struct_0_x1617_x7307_1233887654}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2141145531}[会话对应的连接数目]{style="font-family:宋体"}

[[User IP Address]{lang="EN-US"}]{#struct_0_x1617_x7307_x1093263641}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x122340973}[会话使用的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Idle time]{lang="EN-US"}]{#struct_0_x1617_x7307_30802174}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_438420802}[会话的空闲时间]{style="font-family:宋体"}

[[Created]{lang="EN-US"}]{#struct_0_x1617_x7307_1832435163}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1474441842}[会话的创建时间]{style="font-family:宋体"}

[[Idle timeout]{lang="EN-US"}]{#struct_0_x1617_x7307_1264002944}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_972766470}[会话保持空闲状态的最长时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-88975771 .myid}
[]{#_Toc404793455}[]{#struct_0_x1617_x7307_x1410826535}[]{#_Toc394323315}[]{#_Toc392947640}[]{#_Toc398198391}[]{#_Toc398198392}

**SSL VPN \-- SSL VPN配置命令 \-- dynamic-password enable**

------------------------------------------------------------------------

[**[dynamic-password enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1958910951}[命令用来开启动态口令验证功能。]{style="font-family:宋体"}

[**[undo dynamic-password enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_1391517916}[命令用来关闭动态口令验证功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_472820300}

[**[dynamic-password]{lang="EN-US"}**[ **enable**]{lang="EN-US"}]{#struct_0_x1617_x7307_x470778641}

[**[undo dynamic-password enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1874829882}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2051631902}

[[动态口令验证功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1330535369}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1470707127}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2034659962}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2078145525}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x175015264}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_994271082}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2085002881}

[[开启动态口令验证功能后，用户登录]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_521677281}[页面时，需要输入动态口令进行验证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1278342253}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1403690929}[开启动态口令验证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_2038904241}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] dynamic-password enable]{lang="EN-US"}
:::

::: {#1017616665 .myid}
[]{#_Toc387742413}[]{#_Toc383884562}[]{#_Toc404793456}[]{#struct_0_x1617_x7307_x830393119}[]{#_Toc394323309}[]{#_Toc390680540}

**SSL VPN \-- SSL VPN配置命令 \-- emo-server**

------------------------------------------------------------------------

[**[emo-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_1767397070}[命令用来配置为客户端指定的]{style="font-family:宋体"}[EMO]{lang="EN-US"}[（]{style="font-family:宋体"}[Endpoint Mobile Office]{lang="EN-US"}[，终端移动办公）服务器。]{style="font-family:宋体"}

[**[undo emo-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_1490191404}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x485366797}

[**[emo-server ]{lang="EN-US"}**[{ **host-name** *host-name* \| **ip** *ip-address* } **port** *port-number* ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1276301880}

[**[undo emo-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1699667410}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_368555288}

[[没有配置为客户端指定的]{style="font-family:宋体"}[EMO]{lang="EN-US"}]{#struct_0_x1617_x7307_215647766}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:
黑体"}]{#struct_0_x1617_x7307_2484437}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1143719209}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1867227928}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_451403060}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1180168225}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1056428665}

[**[host-name]{lang="EN-US"}***[ host-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x689979114}[：指定]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器的主机名。]{style="font-family:宋体"}*[host-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[127]{lang="EN-US"}[个字符的字符串，可以包含字母、数字、下划线、"]{style="font-family:宋体"}[-]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_x484305648}[：指定]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为点分十进制格式，不能是组播、广播、环回地址。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_x893744236}[：指定]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器使用的端口号。]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1793656649}

[[EMO]{lang="EN-US"}]{#struct_0_x1617_x7307_524351539}[服务器用来为移动客户端提供服务。执行本命令后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关会将配置的]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器信息下发给客户端，以便客户端访问]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1775228255}[访问实例视图下，重复执行本命令，则新的配置会覆盖已有的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_615223413}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_263927005}[在名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下配置]{style="font-family:宋体"}[EMO]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[10.10.1.1]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x2049570734}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] emo-server ip 10.10.1.1 port 8000]{lang="EN-US"}
:::

::: {#1516183278 .myid}
[]{#_Toc404793457}[]{#struct_0_x1617_x7307_625913872}[]{#_Toc398198395}

**SSL VPN \-- SSL VPN配置命令 \-- filter ip-tunnel**

------------------------------------------------------------------------

[**[filter ip-tunnel]{lang="EN-US"}**]{#struct_0_x1617_x7307_x124867583}[命令用来配置对]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入进行过滤。]{style="font-family:宋体"}

[**[undo filter ip-tunnel]{lang="EN-US"}**]{#struct_0_x1617_x7307_x131691191}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_254111297}

[**[filter ip-tunnel]{lang="EN-US"}**[ *advanced-acl-number*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1562489416}

[**[undo filter ip-tunnel]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1637213251}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1232335187}

[[不会对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x2112369105}[接入进行过滤，允许所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入报文通过。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1554054536}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1014583975}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1805408596}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x2110966805}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_595197247}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x667276853}

[*[advance-acl-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_500620352}[：用来过滤]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入报文的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_629186187}

[[执行本命令后，如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x311703660}[客户端使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入方式访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关，则只有通过]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查的报文才可以访问]{style="font-family:宋体"}[IP]{lang="EN-US"}[资源。]{style="font-family:宋体"}

[[如果引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1617_x7307_1210938605}[不存在，则]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关拒绝所有]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入方式的访问。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x172906282}[策略组视图下重复执行本命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x454836594}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_52246386}[配置策略组]{style="font-family:宋体"}[pg1]{lang="EN-US"}[通过]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[过滤]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入方式访问。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1496548168}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\] filter ip-tunnel 3000]{lang="EN-US"}
:::

::: {#1905613941 .myid}
[]{#_Toc404793458}[]{#struct_0_x1617_x7307_1399734572}[]{#_Toc395620358}

**SSL VPN \-- SSL VPN配置命令 \-- filter tcp-access**

------------------------------------------------------------------------

[**[filter tcp-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_62401215}[命令用来配置对]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入进行过滤。]{style="font-family:宋体"}

[**[undo filter tcp-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1508857906}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1291508424}

[**[filter tcp-access]{lang="EN-US"}**[ *advanced-acl-number*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1461603536}

[**[undo filter tcp-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1903224502}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_54853306}

[[不会对]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1617_x7307_x230791372}[接入进行过滤，允许所有客户端访问]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x458592742}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1319438648}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1739806347}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x849780967}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_778834287}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_69535773}

[*[advanced-acl-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_503505965}[：用来过滤]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_560477263}

[[执行本命令后，如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1206572461}[客户端访问]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务]{style="font-family:宋体"}[，则只有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端发送的报文通过了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查，才允许其访问]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务。]{style="font-family:宋体"}

[[如果引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1617_x7307_569786607}[不存在，则]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关拒绝所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端访问]{style="font-family:宋体"}[TCP]{lang="EN-US"}[应用。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1349529461}[策略组视图下重复执行本命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1255973728}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1112008037}[配置策略组]{style="font-family:宋体"}[pg1]{lang="EN-US"}[通过]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[过滤]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1172941310}

[\[Sysname\]sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy-group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] filter tcp-access 3000]{lang="EN-US"}
:::

::: {#1221250417 .myid}
[]{#_Toc404793459}[]{#struct_0_x1617_x7307_x47005882}

**SSL VPN \-- SSL VPN配置命令 \-- filter web-access**

------------------------------------------------------------------------

[**[filter web-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_2043108549}[命令用来配置对]{style="font-family:宋体"}[Web]{lang="EN-US"}[接入进行过滤。]{style="font-family:宋体"}

[**[undo filter web-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1276650552}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1693836754}

[**[filter web-access]{lang="EN-US"}**[ *advanced-acl-number*]{lang="EN-US"}]{#struct_0_x1617_x7307_1189885600}

[**[undo filter web-access]{lang="EN-US"}**]{#struct_0_x1617_x7307_1635619714}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2095924502}

[[不会对]{style="font-family:宋体"}[Web]{lang="EN-US"}]{#struct_0_x1617_x7307_1084759375}[接入进行过滤，允许所有客户端访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[接入资源。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1726986533}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1263275634}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1932956190}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_2019787524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1742508766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2093487759}

[*[advanced-acl-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_x735984482}[：用来过滤]{style="font-family:宋体"}[Web]{lang="EN-US"}[接入的高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x385740653}

[[执行本命令后，如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x163298038}[客户端访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[资源，则只有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端发送的报文通过了]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查，才允许其访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[资源。]{style="font-family:宋体"}

[[如果引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x1617_x7307_x929793081}[不存在，则]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关拒绝所有]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端访问]{style="font-family:宋体"}[Web]{lang="EN-US"}[资源。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1259298644}[策略组视图下重复执行本命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2103588305}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1449494001}[配置策略组]{style="font-family:宋体"}[pg1]{lang="EN-US"}[通过]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[过滤]{style="font-family:宋体"}[Web]{lang="EN-US"}[接入。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_998181938}

[\[Sysname\]sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy-group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] filter web-access 3000]{lang="EN-US"}
:::

::: {#1518415185 .myid}
[]{#_Toc334859959}[]{#_Toc404793460}[]{#struct_0_x1617_x7307_x799185475}[]{#_Toc394323274}[]{#_Toc387742419}[]{#_Toc383884567}[]{#_Toc398739082}[]{#_Toc398739180}[]{#_Toc398739083}[]{#_Toc398739181}[]{#_Toc398739084}[]{#_Toc398739182}[]{#_Toc398739086}[]{#_Toc398739184}[]{#_Toc398739087}[]{#_Toc398739185}[]{#_Toc398739088}[]{#_Toc398739186}[]{#_Toc398739089}[]{#_Toc398739187}[]{#_Toc398739090}[]{#_Toc398739188}[]{#_Toc398739091}[]{#_Toc398739189}[]{#_Toc398739092}[]{#_Toc398739190}[]{#_Toc398739093}[]{#_Toc398739191}[]{#_Toc398739094}[]{#_Toc398739192}[]{#_Toc398739095}[]{#_Toc398739193}[]{#_Toc398739096}[]{#_Toc398739194}

**SSL VPN \-- SSL VPN配置命令 \-- gateway**

------------------------------------------------------------------------

[**[gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_x585661585}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例引用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[undo gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_x294209074}[命令用来取消]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例引用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_620694537}

[**[gateway ]{lang="EN-US"}***[gateway-name ]{lang="EN-US"}*[\[ **domain** *domain-name* \| **virtual-host** *virtual-host-name* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_x711111148}

[**[undo gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_126115194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1899902900}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1097014697}[访问实例没有引用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1781607184}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x587410168}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_756368623}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x2045250364}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_358793094}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_116589940}

[*[gateway-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1462885753}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关名称。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[**[domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1364899150}[：域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线、"]{style="font-family:宋体"}[-]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[virtual-host ]{lang="EN-US"}***[virtual-host-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x814603638}[：虚拟主机名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线、"]{style="font-family:宋体"}[-]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1719306997}

[[多个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x546611421}[访问实例引用同一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，可以通过以下方法判断远端接入用户所属的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为不同的]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1609857496}[SSL VPN]{lang="EN-US"}[访问实例指定不同的域名。远端用户登录]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，指定自己所在的域，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关根据用户指定的域判断该用户所属的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为不同的]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1996078593}[SSL VPN]{lang="EN-US"}[访问实例指定不同的虚拟主机名称。远端用户访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，输入虚拟主机名称，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关根据虚拟主机名称判断该用户所属的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_2105190789}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x650504432}[SSL VPN]{lang="EN-US"}[访问实例引用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时没有指定域名和虚拟主机名称，那么其他的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例就不能再引用该]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个]{style="font-family:宋体"}]{#struct_0_x1617_x7307_970465278}[SSL VPN]{lang="EN-US"}[访问实例视图下，重复配置本命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_896358417}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x47562887}[配置名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例引用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}[gw1]{lang="EN-US"}[，域名为]{style="font-family:宋体"}[domain1]{lang="EN-US"}[、虚拟主机名称为]{style="font-family:宋体"}[abc.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1093198105}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] gateway gw1 domain domain1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] gateway gw1 virtual-host abc.com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x371085579}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_1114660713}
:::

::: {#-1143325196 .myid}
[]{#_Toc404793461}[]{#struct_0_x1617_x7307_x493812510}[]{#_Toc394323295}[]{#_Toc398198400}[]{#_Toc398198401}[]{#_Toc398198402}[]{#_Toc398198403}

**SSL VPN \-- SSL VPN配置命令 \-- http-redirect**

------------------------------------------------------------------------

[**[http-redirect]{lang="EN-US"}**]{#struct_0_x1617_x7307_1340226930}[命令用来开启]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[流量的重定向功能。]{style="font-family:宋体"}

[**[undo http-redirect]{lang="EN-US"}**]{#struct_0_x1617_x7307_148932723}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x414657175}

[**[http-redirect ]{lang="EN-US"}**[\[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_1787578235}

[**[undo http-redirect]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2092969481}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x881510072}

[[未开启]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_x1617_x7307_x1000258354}[流量的重定向功能，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关不会处理]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[流量。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_868925123}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1705048620}[网关视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1994150593}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x506791867}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_940402209}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_472885836}

[*[port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_x2060729782}[：需要重定向的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[流量的端口号，取值范围为]{style="font-family:宋体"}[80]{lang="EN-US"}[、]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[80]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1235872647}

[[配置该命令后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x338035379}[网关将监听指定的端口号，并把指定端口号的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[流量重定向到]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[的]{style="font-family:宋体"}[443]{lang="EN-US"}[端口，向客户端发送重定向报文，让客户端重新以]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[方式登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1583310171}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1803906660}[为端口号为]{style="font-family:宋体"}[1025]{lang="EN-US"}[的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[流量开启重定向功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1748038661}

[\[Sysname\] sslvpn gateway gateway1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gateway1\] http-redirect port 1025]{lang="EN-US"}
:::

::: {#-634417044 .myid}
[]{#_Toc404793462}[]{#struct_0_x1617_x7307_x935621134}[]{#_Toc394323306}[]{#_Toc389662651}[]{#_Toc398198405}[]{#_Toc398198406}[]{#_Toc398198407}[]{#_Toc398198408}

**SSL VPN \-- SSL VPN配置命令 \-- include**

------------------------------------------------------------------------

[**[include]{lang="EN-US"}**]{#struct_0_x1617_x7307_1312910903}[命令用来在路由列表中添加路由。]{style="font-family:宋体"}

[**[undo include]{lang="EN-US"}**]{#struct_0_x1617_x7307_1476527102}[命令用来删除路由列表中的路由。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x771589269}

[**[include]{lang="EN-US"}**[ *ip-address* { *mask-length \| mask* }]{lang="EN-US"}]{#struct_0_x1617_x7307_1666574578}

[**[undo include]{lang="EN-US"}**[ *ip-address* { *mask-length \| mask* }]{lang="EN-US"}]{#struct_0_x1617_x7307_127083921}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_599661195}

[[路由列表中不存在任何路由。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1811819561}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2038969777}

[[路由列表视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_683423623}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x36958691}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1195844408}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1597824473}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2043679380}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_290803970}[：路由的目的地址，不能是组播、广播、环回地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x1617_x7307_1128739036}[：路由的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x1617_x7307_x847885067}[：路由的掩码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1393341439}

[[本命令指定的目的网段需要是企业内部服务器所在的网络。策略组引用路由列表后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2055988280}[网关将路由列表中的路由表项下发给客户端。客户端在本地添加这些路由表项，以便客户端将访问企业网络内部服务器的报文通过虚拟网卡发送给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关，防止这些报文进入]{style="font-family:宋体"}[Internet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在路由列表视图下，通过重复执行本命令，可以在该路由列表中添加多条路由。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x2060272617}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1782749184}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_2046510811}[在路由列表]{style="font-family:宋体"}[rtlist]{lang="EN-US"}[下添加路由]{style="font-family:宋体"}[10.0.0.0/8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x689913578}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] ip-route-list rtlist]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-route-list-rtlist\] include 10.0.0.0 8]{lang="EN-US"}
:::

::: {#1644201549 .myid}
[]{#_Toc404793463}[]{#struct_0_x1617_x7307_x2067738448}

**SSL VPN \-- SSL VPN配置命令 \-- interface sslvpn-ac**

------------------------------------------------------------------------

[**[interface sslvpn-ac]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1022306582}[命令用来创建]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口，并进入]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[**[undo interface sslvpn-ac]{lang="EN-US"}**]{#struct_0_x1617_x7307_1293846306}[命令用来删除指定的]{style="font-family:
宋体"}[SSL VPN AC]{lang="EN-US"}[接口。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1640152869}

[**[interface sslvpn-ac ]{lang="EN-US"}***[interface]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1998298755}

[**[undo interface sslvpn-ac ]{lang="EN-US"}***[interface]{lang="EN-US"}[--number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1559802906}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x88458542}

[[设备上不存在任何]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_289442768}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1136148157}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_146351404}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1698506129}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x802078399}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1004956339}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_620477694}

[*[interface-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1232400723}[：]{lang="EN-US" style="font-family:
宋体"}[SSL VPN AC]{lang="EN-US"}[接口的编号，]{lang="EN-US" style="font-family:宋体"}[取值]{style="font-family:宋体"}[范围]{lang="EN-US" style="font-family:宋体"}[为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1737354087}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_2129846759}[创建]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口]{style="font-family:宋体"}[1000]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口视图。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1550990630}

[\[Sysname\]interface SSLVPN-AC 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\]]{lang="EN-US"}
:::

::: {#1035762823 .myid}
[]{#_Toc404793464}[]{#struct_0_x1617_x7307_x1469963286}[]{#_Toc394323268}[]{#_Toc398198411}[]{#_Toc398198412}[]{#_Toc398198413}[]{#_Toc398198414}[]{#_Toc398198415}[]{#_Toc398198416}[]{#_Toc398198417}[]{#_Toc398198418}[]{#_Toc398198419}[]{#_Toc398198420}[]{#_Toc398198421}[]{#_Toc398739101}[]{#_Toc398739199}

**SSL VPN \-- SSL VPN配置命令 \-- ip address (SSL VPN gateway view)**

------------------------------------------------------------------------

[**[ip address]{lang="EN-US"}**]{#struct_0_x1617_x7307_894113765}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号。]{style="font-family:宋体"}

[**[undo ip address]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1176955270}[命令用来删除]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2049333946}

[**[ip address ]{lang="EN-US"}***[ip-address]{lang="EN-US"}[ ]{lang="EN-US"}*[\[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_1825882643}

[**[undo ip address]{lang="EN-US"}**]{#struct_0_x1617_x7307_x980804590}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1899042785}

[[没有指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2102947695}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1281920024}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x85749976}[网关视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_735912652}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1496482632}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1301913457}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_680635949}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_304815932}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，为点分十进制格式。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1028150442}[：指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的端口号。]{style="font-family:宋体"}*[port-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[443]{lang="EN-US"}[、]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[443]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x201575483}

[[远端接入用户可以通过本命令配置的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_84490322}[地址和端口号访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。本命令指定的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址应为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关上接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并需要保证该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址路由可达。]{style="font-family:宋体"}

[[在同一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x116307028}[网关视图下，重复执行]{style="font-family:宋体"}**[ip address]{lang="EN-US"}**[命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x214546727}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_731298738}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.10.1.1]{lang="EN-US"}[、端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1808228635}

[\[Sysname\] sslvpn gateway gw1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gw1\] ip address 10.10.1.1 port 8000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_556517633}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_971636299}
:::

::: {#1558353544 .myid}
[]{#_Toc404793465}[]{#struct_0_x1617_x7307_554252832}[]{#_Toc394323305}[]{#_Toc389662650}[]{#_Toc398198424}[]{#_Toc398198425}

**SSL VPN \-- SSL VPN配置命令 \-- ip-route-list**

------------------------------------------------------------------------

[**[ip-route-list]{lang="EN-US"}**]{#struct_0_x1617_x7307_69601309}[命令用来创建路由列表，并进入路由列表视图。]{style="font-family:宋体"}

[**[undo ip-route-list]{lang="EN-US"}**]{#struct_0_x1617_x7307_x976665815}[命令用来删除指定的路由列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x936091503}

[**[ip-route-list]{lang="EN-US"}**[ *list-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_1959030036}

[**[undo ip-route-list ]{lang="EN-US"}***[list-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1623513838}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x378710977}

[[设备上不存在任何路由列表。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_526647969}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1512434938}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1789626474}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x991489733}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1406464845}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x864228808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2044165066}

[*[list-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x184362723}[：路由列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由字母、数字、下划线组成，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x406365355}

[[在路由列表视图下，通过]{style="font-family:宋体"}**[include]{lang="EN-US"}**]{#struct_0_x1617_x7307_1635685250}[命令可以添加路由表项，路由表项的目的网段为企业内部服务器所在的网段。策略组引用路由列表后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关将路由列表中的路由表项下发给客户端，客户端在本地添加这些路由表项，路由表项的出接口为客户端的虚拟网卡，以便客户端通过这些路由表项访问企业网络内部的服务器。]{style="font-family:宋体"}

[[需要注意的是，若路由列表被策略组引用，则不允许删除该路由列表。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_966774222}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_552688326}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x561086654}[在名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例下，创建路由列表]{style="font-family:宋体"}[rtlist]{lang="EN-US"}[，并进入路由列表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1978522622}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] ip-route-list rtlist]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-route-list-rtlist\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1618877848}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip-tunnel access-route]{lang="EN-US"}**]{#struct_0_x1617_x7307_1705408699}
:::

::: {#-1706886615 .myid}
[]{#_Toc404793466}[]{#struct_0_x1617_x7307_1639958598}[]{#_Toc394323307}[]{#_Toc389662652}[]{#_Toc398198427}[]{#_Toc398198428}[]{#_Toc398739104}[]{#_Toc398739202}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel access-route**

------------------------------------------------------------------------

[**[ip-tunnel access-route]{lang="EN-US"}**]{#struct_0_x1617_x7307_x507594542}[命令用来配置下发给客户端的路由表项。]{style="font-family:宋体"}

[**[undo ip-tunnel access-route]{lang="EN-US"}**]{#struct_0_x1617_x7307_x252525646}[命令用来取消下发给客户端的路由表项。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x818500761}

[**[ip-tunnel access-route ]{lang="EN-US"}**[{ *ip-address* { *mask-length \| mask* } \| **force-all** \| **ip-route-list** *list-name* }]{lang="EN-US"}]{#struct_0_x1617_x7307_x448015744}

[**[undo ip-tunnel access-route]{lang="EN-US"}**]{#struct_0_x1617_x7307_1598993045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_305330616}

[[未指定下发给客户端的路由表项。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x289578874}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1449428465}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x756062877}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1942423661}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_631492277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1802698990}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1488371187}

[*[ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *mask-length \| mask* }]{lang="EN-US"}]{#struct_0_x1617_x7307_x395187160}[：将指定路由下发给客户端。]{style="font-family:
宋体"}*[ip-address]{lang="EN-US"}*[为路由的目的地址，不能是组播、广播、环回地址；]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[路由的掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为路由的掩码。]{style="font-family:宋体"}

[**[force-all]{lang="EN-US"}**]{#struct_0_x1617_x7307_357734967}[：强制将客户端的流量转发给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[ip-route-list]{lang="EN-US"}***[ list-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1071977133}[：将指定路由列表中的路由表项下发给客户端。]{style="font-family:宋体"}*[list-name]{lang="EN-US"}*[表示路由列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由字母、数字、下划线组成，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x898663706}

[[客户端通过]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x1796421482}[接入方式访问网关时，网关将指定的路由下发给客户端。客户端若访问该网段内的服务器，报文就会通过虚拟网卡发送给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关，防止报文进入]{style="font-family:宋体"}[Internet]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令中指定的路由列表必须先通过]{style="font-family:宋体"}**[ip-route-list]{lang="EN-US"}**]{#struct_0_x1617_x7307_x399967658}[命令创建。通过指定路由列表，可以同时将路由列表中的多条路由下发给客户端。若只需要为客户端下发一条路由，则可以直接配置]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ *mask-length \| mask* }]{lang="EN-US"}[参数，无需指定路由列表。]{style="font-family:宋体"}

[[执行本命令时如果指定了]{style="font-family:宋体"}**[force-all]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1093952734}[参数，则]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关将在客户端上添加优先级最高的缺省路由，路由的出接口为虚拟网卡，从而使得所有没有匹配到路由表项的流量都通过虚拟网卡发送给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关还会实时监控]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端，不允许]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端删除此缺省路由，且不允许]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端添加优先级高于此路由的缺省路由。]{style="font-family:宋体"}

[[若重复执行本命令，则新的配置会覆盖已有的配置。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1392984244}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x233733724}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_116655476}[在策略组]{style="font-family:宋体"}[pg1]{lang="EN-US"}[下，配置将路由列表]{style="font-family:宋体"}[rtlist]{lang="EN-US"}[中的路由下发给客户端。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_703473039}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] ip-route-list rtlist]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-route-list-rtlist\] include 10.0.0.0 8]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-route-list-rtlist\] include 20.0.0.0 8]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-route-list-rtlist\] quit]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\] ip-tunnel access-route ip-route-list rtlist]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1332217143}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip-route-list]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1707968971}
:::

::: {#1750580920 .myid}
[]{#_Toc404793467}[]{#struct_0_x1617_x7307_429208089}[]{#_Toc394323300}[]{#_Toc398198431}[]{#_Toc398198432}[]{#_Toc398739106}[]{#_Toc398739204}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel address-pool**

------------------------------------------------------------------------

[**[ip-tunnel address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_1887978419}[命令用来配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入引用地址池。]{style="font-family:宋体"}

[**[undo ip-tunnel address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1329278604}[命令用来取消]{style="font-family:
宋体"}[IP]{lang="EN-US"}[接入引用地址池。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1243280038}

[**[ip-tunnel address-pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}*[ **mask** { *mask-length \| mask* }]{lang="EN-US"}]{#struct_0_x1617_x7307_x217824235}

[**[undo ip-tunnel address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_x144071282}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1551402237}

[[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x298173607}[接入未引用地址池。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x473184303}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1227415833}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1837382144}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1400700528}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_743580555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x826362471}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1907430860}[：引用的地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由字母、数字、下划线组成，不区分大小写。]{style="font-family:宋体"}

[**[mask ]{lang="EN-US"}**[{ *mask-length \| mask* }]{lang="EN-US"}]{#struct_0_x1617_x7307_x70588592}[：指定地址池的掩码或掩码长度。]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[表示地址池的掩码长度，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[表示地址池的掩码。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1336752366}

[[客户端使用]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_518258166}[接入方式访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，网关需要为客户端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。本命令指定了分配的地址所属的地址池，即从地址池中选取地址分配给客户端。本命令还可以指定分配的地址的掩码或掩码长度。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_97901424}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令可以引用不存在的地址池。但此时]{style="font-family:宋体"}]{#struct_0_x1617_x7307_963207331}[SSL VPN]{lang="EN-US"}[网关无法为客户端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。只有创建地址池后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关才可以为客户端分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1482663742}[SSL VPN]{lang="EN-US"}[策略组视图下只能引用一个地址池。若重复执行本命令，则新的配置会覆盖已有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1222967953}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1668136483}[配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入引用地址池]{style="font-family:宋体"}[pool1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_338668108}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] policy-group pgroup]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx-policy-group-pgroup\] ip-tunnel address-pool pool mask 24]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_873063365}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sslvpn ip address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_1410442007}
:::

::: {#1776632760 .myid}
[]{#_Toc404793468}[]{#struct_0_x1617_x7307_x681043093}[]{#_Toc394323301}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel dns-server**

------------------------------------------------------------------------

[**[ip-tunnel dns-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_x355610781}[命令用来配置为客户端指定的内网]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo ip-tunnel dns-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_x37162285}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x31003654}

[**[ip-tunnel dns-server ]{lang="EN-US"}**[{ **primary** \| **secondary** } *ip-address*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1161839893}

[**[undo ip-tunnel dns-server ]{lang="EN-US"}**[{ **primary** \| **secondary** }]{lang="EN-US"}]{#struct_0_x1617_x7307_x1629976610}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1633708463}

[[没有配置为客户端指定的]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_x1617_x7307_x748786553}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2051364305}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_977618305}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1475033203}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x731200551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1904752049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x892126633}

[**[primary]{lang="EN-US"}**]{#struct_0_x1617_x7307_557190871}[：指定主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[secondary]{lang="EN-US"}**]{#struct_0_x1617_x7307_1414888994}[：指定备]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_x2144687876}[：]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，不能是组播、广播、环回地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x468440212}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x650305213}[配置为客户端指定的主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1376146625}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] policy-group pgroup]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx-policy-group-pgroup\] ip-tunnel dns-server primary 1.1.1.1]{lang="EN-US"}
:::

::: {#208901668 .myid}
[]{#_Toc404793469}[]{#struct_0_x1617_x7307_x1147681840}[]{#_Toc394323298}[]{#_Toc398198436}[]{#_Toc398198437}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel interface**

------------------------------------------------------------------------

[**[ip-tunnel interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1073551567}[命令用来配置]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入引用的]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[**[undo ip-tunnel interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_x407513580}[命令用来取消]{style="font-family:
宋体"}[IP]{lang="EN-US"}[接入引用]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x782861136}

[**[ip-tunnel interface sslvpn-ac]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1903511029}

[**[undo ip-tunnel interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_717217095}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_769203039}

[[IP]{lang="EN-US"}]{#struct_0_x1617_x7307_x824131306}[接入未引用]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_595621232}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1452922089}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x440537147}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_176867884}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_525840045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_684725396}

[**[sslvpn-ac]{lang="EN-US"}**[ *interface-number*]{lang="EN-US"}]{#struct_0_x1617_x7307_1726132598}[：引用的]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口。]{style="font-family:宋体"}*[interface-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口编号，取值范围为设备上已创建的]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x701424403}

[[当]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1157088205}[用户使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入方式访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关时，网关使用指定的]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口与客户端通信。网关从]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口接收到客户端发送的报文后，将报文转发到远端服务器；服务器做出响应后，网关会把应答报文通过]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口发给客户端。]{style="font-family:宋体"}

[[指定的]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_1528351209}[接口必须已经通过]{style="font-family:宋体"}**[interface sslvpn-ac]{lang="EN-US"}**[命令创建。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1868322659}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x451522011}[指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入引用的接口为]{style="font-family:宋体"}[SSL VPN AC 100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x474805963}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] ip-tunnel interface sslvpn-ac 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1098182995}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[interface sslvpn-ac]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1187680431}
:::

::: {#62447886 .myid}
[]{#_Toc404793470}[]{#struct_0_x1617_x7307_297819072}[]{#_Toc394323303}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel keepalive**

------------------------------------------------------------------------

[**[ip-tunnel keepalive]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1486411741}[命令用来配置保活报文的发送时间间隔。]{style="font-family:宋体"}

[**[undo ip-tunnel keepalive]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1832493160}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1163902459}

[**[ip-tunnel keepalive ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_x1617_x7307_1376599008}

[**[undo ip-tunnel keepalive]{lang="EN-US"}**]{#struct_0_x1617_x7307_1550129905}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1860086482}

[[保活报文的发送时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}]{#struct_0_x1617_x7307_620718048}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_114034188}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x132138868}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x641497374}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_807324237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x606652409}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1630700360}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1617_x7307_2071775698}[：保活报文的发送间隔时间，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x104561105}

[[保活报文由客户端发送给网关，用于维持客户端和网关之间的会话。如果保活报文发送时间间隔配置为]{style="font-family:宋体"}[0]{lang="EN-US"}]{#struct_0_x1617_x7307_548890078}[，则客户端不会发送保活报文。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_18244959}[会话的空闲时间超过]{style="font-family:宋体"}**[timeout idle]{lang="EN-US"}**[命令指定的时间，即在该命令指定的时间内，既没有收到客户端发送的数据报文，也没有收到保活报文，则会断开客户端与网关之间的会话。]{style="font-family:宋体"}

[[通常情况下，配置的保活报文发送时间间隔应该小于]{style="font-family:宋体"}**[timeout idle]{lang="EN-US"}**]{#struct_0_x1617_x7307_533710414}[命令配置的最大空闲时间。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1338585480}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x16396935}[在策略组]{style="font-family:宋体"}[pgroup]{lang="EN-US"}[下配置保活报文的发送时间间隔为]{style="font-family:宋体"}[50]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x906235543}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] policy-group pgroup]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx-policy-group-pgroup\] ip-tunnel keepalive 50]{lang="EN-US"}
:::

::: {#-72660183 .myid}
[]{#_Toc404793471}[]{#struct_0_x1617_x7307_117585859}[]{#_Toc394323302}[]{#_Toc398198440}[]{#_Toc398198441}

**SSL VPN \-- SSL VPN配置命令 \-- ip-tunnel wins-server**

------------------------------------------------------------------------

[**[ip-tunnel wins-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_x922841298}[命令用来配置为客户端指定的内网]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址。]{style="font-family:宋体"}

[**[undo ip-tunnel wins-server]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1465158018}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2034033698}

[**[ip-tunnel wins-server ]{lang="EN-US"}**[{ **primary** \| **secondary** } *ip-address*]{lang="EN-US"}]{#struct_0_x1617_x7307_x178881234}

[**[undo ip-tunnel wins-server ]{lang="EN-US"}**[{ **primary** \| **secondary** }]{lang="EN-US"}]{#struct_0_x1617_x7307_x64616419}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x712098219}

[[没有配置为客户端指定的]{style="font-family:宋体"}[WINS]{lang="EN-US"}]{#struct_0_x1617_x7307_1137211025}[服务器地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x881286976}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_600452471}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_734255115}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x418931123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1477795429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_26710649}

[**[primary]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1261897899}[：配置主]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[secondary]{lang="EN-US"}**]{#struct_0_x1617_x7307_x810603319}[：配置备]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[*[ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_x680954611}[：]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，不能是组播、广播、环回地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1529145415}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x143505602}[配置为客户端指定的内网主]{style="font-family:宋体"}[WINS]{lang="EN-US"}[服务器地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1501467522}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] policy-group pgroup]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx-policy-group-pgroup\] ip-tunnel wins-server primary 1.1.1.1]{lang="EN-US"}
:::

::: {#-2144597574 .myid}
[]{#_Toc404793472}[]{#struct_0_x1617_x7307_544768312}[]{#_Toc394323288}[]{#_Toc387742433}

**SSL VPN \-- SSL VPN配置命令 \-- local-port**

------------------------------------------------------------------------

[**[local-port]{lang="EN-US"}**]{#struct_0_x1617_x7307_x601243909}[命令用来添加一个端口转发实例。]{style="font-family:宋体"}

[**[undo local-port]{lang="EN-US"}**]{#struct_0_x1617_x7307_1811446820}[命令用来删除指定的端口转发实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1664871897}

[**[local-port]{lang="EN-US"}**[ *local-port-number* **local-name** *local-name* **remote-server** *remote-server* **remote-port** *remote-port-number* \[ **description** *description-string* \]]{lang="EN-US"}]{#struct_0_x1617_x7307_x74659993}

[**[undo local-port ]{lang="EN-US"}***[local-port-number ]{lang="EN-US"}***[local-name ]{lang="EN-US"}***[local-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1333319006}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_28121254}

[[设备上不存在任何端口转发实例。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x529050921}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_55312501}

[[端口转发列表视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1495726884}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x220538490}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1376672230}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1787050382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_224098153}

[*[local-port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1265390940}[：企业网内的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[服务映射的本地端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[local-name ]{lang="EN-US"}***[local-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1583646193}[：指定企业网内的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[服务映射的本地地址或本地主机名称。]{style="font-family:宋体"}*[local-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[253]{lang="EN-US"}[个字符的字符串，可以包含字母、数字、下划线、"]{style="font-family:宋体"}[-]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[remote-server ]{lang="EN-US"}***[remote-server]{lang="EN-US"}*]{#struct_0_x1617_x7307_178073523}[：指定企业网内]{style="font-family:宋体"}[TCP]{lang="EN-US"}[服务的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或完整域名。]{style="font-family:宋体"}*[remote-server]{lang="EN-US"}*[为为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，可以包含字母、数字、下划线、"]{style="font-family:宋体"}[-]{lang="EN-US"}["和"]{style="font-family:宋体"}[.]{lang="EN-US"}["，不区分大小写。]{style="font-family:宋体"}

[**[remote-port ]{lang="EN-US"}***[remote-port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1738325524}[：指定企业网内]{style="font-family:宋体"}[TCP]{lang="EN-US"}[服务的端口号。]{style="font-family:宋体"}*[remote-port-number]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[description ]{lang="EN-US"}***[description-string]{lang="EN-US"}*]{#struct_0_x1617_x7307_2050018868}[：指定端口转发实例的描述信息。]{style="font-family:宋体"}*[description-string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x981811858}

[[本命令用来将企业网内的基于]{style="font-family:宋体"}[TCP]{lang="EN-US"}]{#struct_0_x1617_x7307_x14435836}[的服务（如]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[POP3]{lang="EN-US"}[）映射为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端上的本地地址和本地端口，以便]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端通过本地地址和本地端口访问企业网内的服务器。例如，执行如下命令，表示在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端上通过]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[、端口]{style="font-family:宋体"}[80]{lang="EN-US"}[可以访问企业网内的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.0.213]{lang="EN-US"}[。]{style="font-family:宋体"}

[[local-port 80 local-name 127.0.0.1 remote-server 192.168.0.213 remote-port 80]{lang="EN-US"}]{#struct_0_x1617_x7307_1514255819}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1132109000}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置的]{style="font-family:宋体"}*[local-port-number]{lang="EN-US"}*]{#struct_0_x1617_x7307_1247979148}[不能与本地已有服务的端口号相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果将企业网内的]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1074093094}[TCP]{lang="EN-US"}[服务映射为本地地址，则建议将本地地址配置为]{style="font-family:宋体"}[127.0.0.0/8]{lang="EN-US"}[网段的地址；如果映射为本地主机名，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入客户端软件会在主机文件]{style="font-family:宋体"}[hosts]{lang="EN-US"}[（]{style="font-family:宋体"}[C:\\Windows\\System32\\drivers\\etc\\hosts]{lang="EN-US"}[）中添加主机名对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，并在用户退出时恢复原来的主机文件]{style="font-family:宋体"}[hosts]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1138579047}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_2025432624}[配置端口转发实例：将企业网内的]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[192.168.0.213]{lang="EN-US"}[映射为本地地址]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[、本地端口]{style="font-family:宋体"}[80]{lang="EN-US"}[；将企业网内的]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务器]{style="font-family:宋体"}[100.100.100.101]{lang="EN-US"}[映射为本地地址]{style="font-family:宋体"}[127.0.0.1]{lang="EN-US"}[、本地端口]{style="font-family:宋体"}[2323]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1499459301}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] port-forward pflist1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-port-forward-pflist1\] local-port 80 local-name 127.0.0.1 remote-server 192.168.0.213 remote-port 80 description http]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-port-forward-pflist1\] local-port 2323 local-name 127.0.0.1 remote-server 100.100.100.101 remote-port 23 description telnet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x17562252}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_611314677}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[resources port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_795201654}
:::

::: {#604885378 .myid}
[]{#_Toc395620356}[]{#_Toc404793473}[]{#struct_0_x1617_x7307_x1166127123}[]{#_Toc398037212}[]{#_Toc397615897}[]{#_Toc398739113}[]{#_Toc398739211}

**SSL VPN \-- SSL VPN配置命令 \-- log enable user-log**

------------------------------------------------------------------------

[**[log enable user-log]{lang="EN-US"}**]{#struct_0_x1617_x7307_942178479}[命令用来开启用户上下线信息的日志开关。]{style="font-family:宋体"}

[**[undo log enable user-log]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1101299932}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x628625801}

[**[log enable user-log]{lang="EN-US"}**]{#struct_0_x1617_x7307_2082317256}

[**[undo log enable user-log]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2041526246}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1346074446}

[[用户上下线信息的日志开关处于关闭状态。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_2073129326}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x551743824}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x634546984}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_238942533}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1657556353}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1227350297}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x319141982}

[[开启本功能后，用户上线和下线时，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x937992841}[网关会记录日志]{style="font-family:宋体"}[信息。生成的日志信息将被发送到设备的信息中心，通过设置信息中心的参数，决定日志信息的输出规则（即是否允许输出以及输出方向）。（有关信息中心参数的配置请参见"网络管理和监控配置指导"中的"信息中心"。）]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_765643818}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1027756170}[开启用户上下线信息的日志开关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x2028475042}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] log enable user-log]{lang="EN-US"}
:::

::: {#-1110637686 .myid}
[]{#_Toc404793474}[]{#struct_0_x1617_x7307_x380188930}[]{#_Toc394323311}[]{#_Toc398198446}

**SSL VPN \-- SSL VPN配置命令 \-- login-message**

------------------------------------------------------------------------

[**[login-message]{lang="EN-US"}**]{#struct_0_x1617_x7307_2092015502}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[登录页面的欢迎信息。]{style="font-family:宋体"}

[**[undo login-message]{lang="EN-US"}**]{#struct_0_x1617_x7307_454339069}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x193843524}

[**[login-message]{lang="EN-US"}**[ { **chinese** *chinese-message* \| **english** *english-message* }]{lang="EN-US"}]{#struct_0_x1617_x7307_x1319843622}

[**[undo login-message ]{lang="EN-US"}**[{ **chinese** \| **english** }]{lang="EN-US"}]{#struct_0_x1617_x7307_651853709}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_97606510}

[[英文登录页面的欢迎信息为"]{style="font-family:宋体"}[Welcome to SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_914340240}["，中文登录页面的欢迎信息为"欢迎进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x669354044}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_338733644}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x662874175}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1172835278}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1036202292}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1402701833}

[**[chinese]{lang="EN-US"}**[ *chinese-message*]{lang="EN-US"}]{#struct_0_x1617_x7307_636196903}[：指定中文页面的欢迎信息。]{style="font-family:宋体"}*[chinese-message]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[english]{lang="EN-US"}**[ *english-message*]{lang="EN-US"}]{#struct_0_x1617_x7307_1412892334}[：指定英文页面的欢迎信息。]{style="font-family:宋体"}*[english-message]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2015028504}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x827432721}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[英文页面的欢迎信息为"]{style="font-family:宋体"}[hello]{lang="EN-US"}["，中文页面的欢迎信息为"你好"。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1065751920}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] login-message english hello]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] login-message chinese ]{lang="EN-US"}[你好]{style="font-family:宋体"}
:::

::: {#-1566070133 .myid}
[]{#_Toc404793475}[]{#struct_0_x1617_x7307_792682943}[]{#_Toc394323312}[]{#_Toc398198448}[]{#_Toc398198449}[]{#_Toc398198450}

**SSL VPN \-- SSL VPN配置命令 \-- logo**

------------------------------------------------------------------------

[**[logo]{lang="EN-US"}**]{#struct_0_x1617_x7307_x176474926}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[页面上显示的]{style="font-family:宋体"}[logo]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo logo]{lang="EN-US"}**]{#struct_0_x1617_x7307_x666053395}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1307344425}

[**[logo]{lang="EN-US"}**[ { **file** *file-name* \| **none** }]{lang="EN-US"}]{#struct_0_x1617_x7307_1904817585}

[**[undo logo]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1316912965}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1016172011}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_384113617}[页面上显示"]{style="font-family:宋体"}[H3C]{lang="EN-US"}["]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1361739878}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1426174935}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1823579820}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1245349197}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x680984102}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1926371258}

[**[file]{lang="EN-US"}**[ *file-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x923228005}[：指定]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标文件。]{style="font-family:宋体"}*[file-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[字符的字符串，不区分大小写。]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[指定的]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标文件必须为]{style="font-family:宋体"}[gif]{lang="EN-US"}[、]{style="font-family:宋体"}[jpg]{lang="EN-US"}[或]{style="font-family:宋体"}[png]{lang="EN-US"}[格式，且不能超过]{style="font-family:宋体"}[100KB]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_x1617_x7307_870032782}[：不显示]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1171430306}

[[指定的]{style="font-family:宋体"}[logo]{lang="EN-US"}]{#struct_0_x1617_x7307_x1472449405}[图标文件必须是本地已经存在的文件。]{style="font-family:宋体"}

[[如果指定]{style="font-family:宋体"}[logo]{lang="EN-US"}]{#struct_0_x1617_x7307_1759228471}[图标文件后，删除该文件，则仍然会显示该文件对应的]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x824065770}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x978345312}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[页面上显示的]{style="font-family:宋体"}[logo]{lang="EN-US"}[为]{style="font-family:宋体"}[flash:/mylogo.gif]{lang="EN-US"}[文件对应的]{style="font-family:宋体"}[logo]{lang="EN-US"}[图标。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1150001168}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] logo flash:/mylogo.gif]{lang="EN-US"}
:::

::: {#-2093730463 .myid}
[]{#_Toc404793476}[]{#struct_0_x1617_x7307_x779698244}[]{#_Toc394323282}[]{#_Toc387742427}[]{#_Toc398198452}

**SSL VPN \-- SSL VPN配置命令 \-- max-users**

------------------------------------------------------------------------

[**[max-users]{lang="EN-US"}**]{#struct_0_x1617_x7307_1496276460}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的最大会话数。]{style="font-family:宋体"}

[**[undo max-users]{lang="EN-US"}**]{#struct_0_x1617_x7307_1465401895}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_840878058}

[**[max-users ]{lang="EN-US"}***[number]{lang="EN-US"}*]{#struct_0_x1617_x7307_2124037480}

[**[undo max-users]{lang="EN-US"}**]{#struct_0_x1617_x7307_1826730684}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1620325239}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1230252498}[访问实例的最大会话数为]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1152294904}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2029889359}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1825357873}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x752019888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1098248531}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1628222484}

[*[number]{lang="EN-US"}*]{#struct_0_x1617_x7307_547626319}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的最大会话数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1048575]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1203149031}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x854966979}[访问实例下的会话数目达到本命令配置的值后，新的用户将无法登录。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1465698489}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_482819055}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例的最大会话数为]{style="font-family:宋体"}[500]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1629282697}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] max-users 500]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1279721431}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1535066098}
:::

::: {#988247972 .myid}
[]{#_Toc404793477}[]{#struct_0_x1617_x7307_x469288591}[]{#_Toc375835902}[]{#_Toc398198454}[]{#_Toc398198455}[]{#_Toc398739118}[]{#_Toc398739216}

**SSL VPN \-- SSL VPN配置命令 \-- mtu**

------------------------------------------------------------------------

[**[mtu]{lang="EN-US"}**]{#struct_0_x1617_x7307_1319271361}[命令用来配置接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值。]{style="font-family:宋体"}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2095869746}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1639255349}

[**[mtu]{lang="EN-US"}**[ *size*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1630634824}

[**[undo mtu]{lang="EN-US"}**]{#struct_0_x1617_x7307_1643853326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1634677196}

[[本命令的缺省情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x751206617}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_764032581}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_1631767580}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1855080720}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1852091934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1555193890}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x129448169}

[*[size]{lang="EN-US"}*]{#struct_0_x1617_x7307_x842619338}[：接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[100]{lang="EN-US"}[～]{style="font-family:宋体"}[64000]{lang="EN-US"}[，单位为字节。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1171139328}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x263251085}[配置接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值为]{style="font-family:宋体"}[1430]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x2060348107}

[\[Sysname\] interface sslvpn-ac 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\] mtu 1430]{lang="EN-US"}
:::

::: {#1244371973 .myid}
[]{#_Toc404793478}[]{#struct_0_x1617_x7307_x1034121210}[]{#_Toc394323278}[]{#_Toc387742423}

**SSL VPN \-- SSL VPN配置命令 \-- policy-group**

------------------------------------------------------------------------

[**[policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x64550883}[命令用来创建策略组，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[策略组视图。]{style="font-family:宋体"}

[**[undo policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1395018233}[命令用来删除指定的策略组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_401110711}

[**[policy-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_1929602139}

[**[undo policy-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_468065489}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1910491753}

[[设备上不存在任何策略组。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x553178377}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1607690534}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1053104308}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1536706648}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x2039209978}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1600930777}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_220734151}

[*[group-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_512920416}[：策略组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_775442604}

[[策略组包含一系列规则，这些规则为用户定义了资源的访问权限。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_890523392}

[[一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1501533058}[访问实例下可以配置多个策略组。远端接入用户访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例时，]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器将授权给该用户的策略组信息下发给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。该用户可以访问的资源由授权的策略组决定。如果]{style="font-family:宋体"}[AAA]{lang="EN-US"}[服务器没有为该用户进行授权，则用户可以访问的资源由缺省策略组决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1307881126}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1062705023}[创建名为]{style="font-family:宋体"}[pg1]{lang="EN-US"}[的策略组，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[策略组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x365323660}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy-group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_314015418}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[default-policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1320785727}
:::

::: {#644262234 .myid}
[]{#_Toc404793479}[]{#struct_0_x1617_x7307_383770418}[]{#_Toc394323287}[]{#_Toc387742432}

**SSL VPN \-- SSL VPN配置命令 \-- port-forward**

------------------------------------------------------------------------

[**[port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2102117816}[命令用来创建端口转发列表，并进入端口转发列表视图。]{style="font-family:宋体"}

[**[undo port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2032149485}[命令用来删除指定的端口转发列表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_269818794}

[**[port-forward]{lang="EN-US"}**[ *port-forward-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x2022522783}

[**[undo port-forward ]{lang="EN-US"}***[port-forward-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_340537379}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_866428533}

[[设备上不存在任何端口转发列表。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1410315418}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1583580657}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x24372216}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_593635385}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1537902374}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1165793068}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x709054142}

[*[port-forward-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_975880933}[：端口转发列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_537818080}

[[端口转发列表用来为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1825627164}[用户提供]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务。]{style="font-family:宋体"}

[[在转发列表视图下，通过]{style="font-family:宋体"}**[local-port]{lang="EN-US"}**]{#struct_0_x1617_x7307_973463443}[命令可以创建端口转发实例。端口转发实例将企业网内的基于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[的服务（如]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[POP3]{lang="EN-US"}[）映射为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端上的本地地址和本地端口，以便]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[客户端通过本地地址和本地端口访问企业网内的服务器。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1196793837}[策略组视图下，通过]{style="font-family:宋体"}**[resources port-forward]{lang="EN-US"}**[命令可以配置策略组引用的端口转发列表。]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户被授权访问某个策略组后，该策略组引用的端口转发列表指定的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务将同时授权给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户可以访问这些]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_925018180}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_67423839}[创建端口转发列表]{style="font-family:宋体"}[pflist1]{lang="EN-US"}[，并进入端口转发列表视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1111801494}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-ctx1\] port-forward pflist1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-port-forward-pflist1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2134413193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-port]{lang="EN-US"}**]{#struct_0_x1617_x7307_x17496716}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[resources port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x966964763}
:::

::: {#1533770432 .myid}
[]{#_Toc404793480}[]{#struct_0_x1617_x7307_1208742927}[]{#_Toc375835903}[]{#_Toc290542313}[]{#_Toc263067840}

**SSL VPN \-- SSL VPN配置命令 \-- reset counters interface sslvpn-ac**

------------------------------------------------------------------------

[**[reset counters interface sslvpn-ac]{lang="DE"}**]{#struct_0_x1617_x7307_x885376427}[命令用来清除]{style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1451437505}

[**[reset counters interface]{lang="EN-US"}**[ \[ ]{lang="EN-US"}]{#struct_0_x1617_x7307_x44829616}**[sslvpn-ac]{lang="DE"}**[ \[ *interface-number* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1162193660}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_328497598}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x329861928}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1366460807}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_793963158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1415349708}

[*[interface-number]{lang="DE"}*]{#struct_0_x1617_x7307_x1763560059}[：]{style="font-family:宋体"}[SSL VPN AC]{lang="DE"}[接口的编号]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[4095]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2028822985}

[[在某些情况下]{style="font-family:宋体"}]{#struct_0_x1617_x7307_1305350037}[，]{style="font-family:宋体"}[需要统计一定时间内某接口的流量]{style="font-family:宋体"}[，]{style="font-family:宋体"}[这就需要在统计开始前清除该接口原有的统计信息]{style="font-family:宋体"}[，]{style="font-family:
宋体"}[重新进行统计。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定接口类型]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1227284761}**[sslvpn-ac]{lang="DE"}**[，则清除所有接口的统计信息；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定接口类型]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x1617_x7307_115570856}[，]{lang="EN-US" style="font-family:宋体"}[不指定接口编号]{lang="EN-US" style="font-family:
宋体"}*[interface-number]{lang="EN-US"}*[，则清除所有]{lang="EN-US" style="font-family:宋体"}[SSL VPN AC]{lang="EN-US"}[接口的统计信息；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果同时指定接口类型和接口编号，则清除指定]{style="font-family:宋体"}]{#struct_0_x1617_x7307_82758030}[SSL VPN AC]{lang="EN-US"}[接口的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x741762378}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_191965243}[清除接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset counters interface sslvpn-ac 1000]{lang="EN-US"}]{#struct_0_x1617_x7307_1294474154}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x226219376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display interface]{lang="EN-US"}**]{#struct_0_x1617_x7307_1342052898}**[ ]{lang="EN-US"}[sslvpn-ac]{lang="DE"}**
:::

::: {#2147246743 .myid}
[]{#_Toc404793481}[]{#struct_0_x1617_x7307_409754263}[]{#_Toc394323289}[]{#_Toc387742434}[]{#_Toc398198461}[]{#_Toc398198462}

**SSL VPN \-- SSL VPN配置命令 \-- resources port-forward**

------------------------------------------------------------------------

[**[resources port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1716495720}[命令用来配置策略组引用端口转发列表。]{style="font-family:宋体"}

[**[undo resources port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1891847552}[命令用来取消策略组引用端口转发列表。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_946377335}

[**[resources port-forward]{lang="EN-US"}**[ *port-forward-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_547934025}

[**[undo resources port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2095635413}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2043550478}

[[策略组没有引用任何端口转发列表。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_695154553}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_338799180}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1110711708}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1022006812}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1296467743}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1593429184}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1549910339}

[*[port-forward-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1377580464}[：端口转发列表名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x588974334}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1386211397}[用户被授权访问某个策略组后，该策略组引用的端口转发列表指定的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务将同时授权给]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户可以访问这些]{style="font-family:宋体"}[TCP]{lang="EN-US"}[接入服务。]{style="font-family:宋体"}

[[需要注意的是，本命令引用的端口转发列表必须先通过]{style="font-family:宋体"}**[port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1085758293}[命令创建。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1250064510}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x704818524}[配置策略组]{style="font-family:宋体"}[pg1]{lang="EN-US"}[引用端口转发列表]{style="font-family:宋体"}[pflist1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1489398081}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy-group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\] resources port-forward pflist1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1022620622}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-port]{lang="EN-US"}**]{#struct_0_x1617_x7307_1904883121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-forward]{lang="EN-US"}**]{#struct_0_x1617_x7307_x97079735}
:::

::: {#1036757862 .myid}
[]{#_Toc404793482}[]{#struct_0_x1617_x7307_x1363654234}[]{#_Toc394323275}[]{#_Toc387742420}[]{#_Toc383884568}[]{#_Toc398198464}[]{#_Toc398198465}[]{#_Toc398739124}[]{#_Toc398739222}

**SSL VPN \-- SSL VPN配置命令 \-- service enable (SSL VPN context view)**

------------------------------------------------------------------------

[**[service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1161996659}[命令用来开启当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[**[undo service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2012984928}[命令用来关闭当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1180944152}

[**[service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_1781980415}

[**[undo service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_1407219273}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x837599840}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1739330229}[访问实例处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1899227845}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1673227139}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1039238066}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1423190905}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x680141343}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1979496701}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x824000234}[开启名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x178847627}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] service enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_706693644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_x636291379}
:::

::: {#678267115 .myid}
[]{#_Toc404793483}[]{#struct_0_x1617_x7307_825716048}[]{#_Toc394323270}[]{#_Toc387742415}[]{#_Toc383884564}[]{#_Toc398739126}[]{#_Toc398739224}[]{#_Toc398739127}[]{#_Toc398739225}[]{#_Toc398739128}[]{#_Toc398739226}[]{#_Toc398739129}[]{#_Toc398739227}[]{#_Toc398739130}[]{#_Toc398739228}[]{#_Toc398739132}[]{#_Toc398739230}[]{#_Toc398739133}[]{#_Toc398739231}[]{#_Toc398739134}[]{#_Toc398739232}[]{#_Toc398739135}[]{#_Toc398739233}[]{#_Toc398739136}[]{#_Toc398739234}[]{#_Toc398739137}[]{#_Toc398739235}[]{#_Toc398739138}[]{#_Toc398739236}[]{#_Toc398739139}[]{#_Toc398739237}[]{#_Toc398739140}[]{#_Toc398739238}[]{#_Toc398739141}[]{#_Toc398739239}[]{#_Toc398739142}[]{#_Toc398739240}[]{#_Toc398739143}[]{#_Toc398739241}[]{#_Toc398739144}[]{#_Toc398739242}

**SSL VPN \-- SSL VPN配置命令 \-- service enable (SSL VPN gateway view)**

------------------------------------------------------------------------

[**[service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_866336449}[命令用来开启当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[**[undo service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1963704278}[命令用来关闭当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_636220730}

[**[service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1131977150}

[**[undo service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1694313113}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1287235776}

[[当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1889588562}[网关处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1247269361}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1098314067}[网关视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1552274630}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_583411568}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1135328505}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_372357654}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1125925520}[开启当前的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x884353818}

[\[Sysname\] sslvpn gateway gw1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gw1\] service enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1220227089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_204251880}
:::

::: {#1170655049 .myid}
[]{#_Toc404793484}[]{#struct_0_x1617_x7307_x2016420784}[]{#_Toc375835904}[]{#_Toc398198468}[]{#_Toc398198469}[]{#_Toc398198470}[]{#_Toc398198471}

**SSL VPN \-- SSL VPN配置命令 \-- shutdown**

------------------------------------------------------------------------

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1906679476}[命令用来关闭当前接口。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shutdown**]{lang="EN-US"}]{#struct_0_x1617_x7307_1113738165}[命令用来开启当前接口。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x383735390}

[**[shutdown]{lang="EN-US"}**]{#struct_0_x1617_x7307_735874077}

[**[undo shutdown]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1630569288}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1532536659}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_x786693378}[接口均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2118332269}

[[SSL VPN AC]{lang="EN-US"}]{#struct_0_x1617_x7307_504620736}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1651567623}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1742212046}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1855989079}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1880134830}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x893391468}[关闭接口]{style="font-family:宋体"}[SSL VPN AC 1000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1376079569}

[\[Sysname\] interface sslvpn-ac 1000]{lang="EN-US"}

[\[Sysname-SSLVPN-AC1000\] shutdown]{lang="EN-US"}
:::

::: {#-866773307 .myid}
[]{#_Toc404793485}[]{#struct_0_x1617_x7307_x623553786}[]{#_Toc394323269}[]{#_Toc387742414}[]{#_Toc383884580}[]{#_Toc398198473}[]{#_Toc398198474}[]{#_Toc398198475}[]{#_Toc398198476}

**SSL VPN \-- SSL VPN配置命令 \-- ssl server-policy**

------------------------------------------------------------------------

[**[ssl server-policy]{lang="EN-US"}**]{#struct_0_x1617_x7307_1737907985}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略。]{style="font-family:宋体"}

[**[undo ssl server-policy]{lang="EN-US"}**]{#struct_0_x1617_x7307_1019328042}[命令用来取消]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x998987236}

[**[ssl server-policy]{lang="EN-US"}**[ *policy-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x64485347}

[**[undo ssl server-policy]{lang="EN-US"}**]{#struct_0_x1617_x7307_1335663925}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_308775282}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x341932581}[网关没有引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x660526971}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1813652277}[网关视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1025632372}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x308208435}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_95327637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_717126368}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1470132254}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1274535703}

[[通过本命令指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1653080777}[网关引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关将采用该策略下的参数与远端接入用户建立]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1162664681}[网关只能引用一个]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略。在同一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关视图下，重复执行本命令，新的配置会覆盖已有配置，但新的配置不会立即生效。只有执行]{style="font-family:宋体"}**[undo service enable]{lang="EN-US"}**[命令关闭]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关，并执行]{style="font-family:宋体"}**[service enable]{lang="EN-US"}**[命令开启]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关后，新的配置才会生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x382224772}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1501598594}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}[gw1]{lang="EN-US"}[引用]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略]{style="font-family:宋体"}[CA_CERT]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1269352485}

[\[Sysname\] sslvpn gateway gw1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gw1\] ssl server-policy CA_CERT]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1037516061}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_898771772}
:::

::: {#-1113445228 .myid}
[]{#_Toc404793486}[]{#struct_0_x1617_x7307_x6164793}[]{#_Toc394323273}[]{#_Toc387742418}[]{#_Toc383884566}

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn context**

------------------------------------------------------------------------

[**[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_1495213085}[命令用来创建]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例视图。]{style="font-family:宋体"}

[**[undo sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_453442326}[命令用来删除指定的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1430751940}

[**[sslvpn context]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_1910950369}

[**[undo sslvpn context]{lang="EN-US"}**[ *context-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1299577856}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2114121511}

[[设备上不存在任何]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1282274346}[访问实例。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2063265849}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_285864590}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_898748875}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1583515121}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x2102301084}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1604375584}

[*[context-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x859542773}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1015805641}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1939941851}[访问实例用来管理用户会话、用户可以访问的资源、用户认证方式等。一个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关可以被多个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例引用，不同]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例对应不同的资源。远端接入用户登录]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关后可以访问的资源，由该用户所属的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例决定。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1741266782}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1397065837}[创建名为]{style="font-family:宋体"}[ctx1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1383183999}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_389415601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn context]{lang="EN-US"}**]{#struct_0_x1617_x7307_1208236355}
:::

::: {#1828580264 .myid}
[]{#_Toc290542294}[]{#_Toc263067821}[]{#_Toc207010297}[]{#_Toc207010030}[]{#_Toc139515319}[]{#_Toc137103152}[]{#_Toc404793487}[]{#struct_0_x1617_x7307_x460518043}[]{#_Toc394323267}[]{#_Toc387742412}[]{#_Toc383884561}

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn gateway**

------------------------------------------------------------------------

[**[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_x2035975087}[命令用来创建]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关视图。]{style="font-family:宋体"}

[**[undo sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_x331477662}[命令用来删除指定的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x17431180}

[**[sslvpn gateway]{lang="EN-US"}**[ *gateway-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_268733827}

[**[undo sslvpn gateway]{lang="EN-US"}**[ *gateway-name*]{lang="EN-US"}]{#struct_0_x1617_x7307_x1862285964}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x403472665}

[[设备上不存在任何]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x556988366}[网关。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x739797053}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1857321753}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1324802003}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_518265870}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x642071972}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x2016246525}

[*[gateway-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x907469675}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含字母、数字、下划线，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1033303334}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1957901367}[网关位于远端接入用户和企业内部网络之间，负责在二者之间转发报文。]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关与远端接入用户建立]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接，并对接入用户进行身份认证。远端接入用户的访问请求只有通过]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的安全检查和认证后，才会被]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关转发到企业网络内部，从而实现对企业内部资源的保护。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x416912806}[网关视图下，需要进行以下配置：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x1417418292}**[ip address]{lang="EN-US"}**[命令指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号，以便远端接入用户通过该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和端口号访问]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}**[ssl server-policy]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1227219225}[命令指定]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关引用的]{style="font-family:宋体"}[SSL]{lang="EN-US"}[服务器端策略，以便]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关采用该策略下的参数与远端接入用户建立]{style="font-family:宋体"}[SSL]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}**[service enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x746052816}[命令]{lang="EN-US" style="font-family:宋体"}[开启]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关。]{style="font-family:宋体"}

[[需要注意的是，如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_644753204}[网关被]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例引用，则该]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关不能被删除。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x976339886}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_687532211}[创建]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}[gw1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_549519380}

[\[Sysname\] sslvpn gateway gw1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gw1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1092490823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[sslvpn gateway]{lang="EN-US"}**]{#struct_0_x1617_x7307_1860409313}
:::

::: {#-156506905 .myid}
[]{#_Toc404793488}[]{#struct_0_x1617_x7307_x863165686}[]{#_Toc394323299}

**SSL VPN \-- SSL VPN配置命令 \-- sslvpn ip address-pool**

------------------------------------------------------------------------

[**[sslvpn ip address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_1285646272}[命令用来创建地址池。]{style="font-family:宋体"}

[**[undo sslvpn ip address-pool]{lang="EN-US"}**]{#struct_0_x1617_x7307_427253855}[命令用来删除指定的地址池。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1257667410}

[**[sslvpn ip address-pool ]{lang="EN-US"}***[pool-name start-ip-address end-ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1052838767}

[**[undo sslvpn ip address-pool]{lang="EN-US"}***[ pool-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x1197747335}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x609546681}

[[设备上不存在任何地址池。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_338864716}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_703581449}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x1617_x7307_233843240}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1913582164}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1387914426}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x2009786074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1323568228}

[*[pool-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_x150808557}[：地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，由字母、数字、下划线组成，不区分大小写。]{style="font-family:宋体"}

[*[start-ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_1914476512}[：地址池的起始地址。]{style="font-family:宋体"}

[*[end-ip-address]{lang="EN-US"}*]{#struct_0_x1617_x7307_1550577110}[：地址池的结束地址。结束地址必须大于起始地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_121566255}

[[在策略组中引用本命令创建的地址池后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x808903768}[网关将从引用的地址池中选择地址、分配给]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入方式的客户端。]{style="font-family:宋体"}

[[需要注意的是，本命令中指定的起始地址和结束地址不能是组播、广播、环回地址。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_x185303770}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x801976331}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x63972612}[创建地址池]{style="font-family:宋体"}[pool1]{lang="EN-US"}[，指定地址范围为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[～]{style="font-family:宋体"}[10.1.1.254]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1904948657}

[\[Sysname\] sslvpn ip address-pool pool1 10.1.1.1 10.1.1.254]{lang="EN-US"}
:::

::: {#-1419318917 .myid}
[]{#_Toc404793489}[]{#struct_0_x1617_x7307_1007470496}[]{#_Toc394323283}[]{#_Toc387742428}

**SSL VPN \-- SSL VPN配置命令 \-- timeout idle**

------------------------------------------------------------------------

[**[timeout idle]{lang="EN-US"}**]{#struct_0_x1617_x7307_261825389}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话保持空闲状态的最长时间。]{style="font-family:宋体"}

[**[undo timeout idle]{lang="EN-US"}**]{#struct_0_x1617_x7307_x622945641}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x958684185}

[**[timeout]{lang="EN-US"}**[ **idle** *seconds*]{lang="EN-US"}]{#struct_0_x1617_x7307_1911627879}

[**[undo timeout idle]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1262323337}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1272024838}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_836634484}[会话保持空闲状态的最长时间为]{style="font-family:宋体"}[2100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x139837402}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_2088273222}[策略组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_283833874}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x373052213}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_1393355472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_80590496}

[*[seconds]{lang="EN-US"}*]{#struct_0_x1617_x7307_x778418598}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话保持空闲状态的最长时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x823934698}

[[如果]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1221251238}[会话保持空闲状态的时间超过本命令配置的值，则将断开该会话。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1655742357}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1822247289}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[会话保持空闲状态的最长时间为]{style="font-family:宋体"}[1800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1876737919}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] policy group pg1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1-policy-group-pg1\] timeout idle 1800]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1513194578}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display sslvpn policy-group]{lang="EN-US"}**]{#struct_0_x1617_x7307_x328518573}
:::

::: {#-330973813 .myid}
[]{#_Toc404793490}[]{#struct_0_x1617_x7307_2144773652}[]{#_Toc394323313}

**SSL VPN \-- SSL VPN配置命令 \-- title**

------------------------------------------------------------------------

[**[title]{lang="EN-US"}**]{#struct_0_x1617_x7307_1153286814}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[页面的标题信息。]{style="font-family:宋体"}

[**[undo title]{lang="EN-US"}**]{#struct_0_x1617_x7307_296053168}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_480427009}

[**[title]{lang="EN-US"}**[ { **chinese** *chinese-title* \| **english** *english-title* }]{lang="EN-US"}]{#struct_0_x1617_x7307_477892386}

[**[undo title ]{lang="EN-US"}**[{ **chinese** \| **english** }]{lang="EN-US"}]{#struct_0_x1617_x7307_630756179}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x66225614}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1098379603}[页面的标题为"]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_466960221}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1906780355}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1012784242}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_279561981}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x625462535}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x334435696}

[**[chinese]{lang="EN-US"}**[ *chinese-title*]{lang="EN-US"}]{#struct_0_x1617_x7307_271227795}[：指定中文页面的标题信息。]{style="font-family:宋体"}*[chinese-title]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[english]{lang="EN-US"}**[ *english-title*]{lang="EN-US"}]{#struct_0_x1617_x7307_x386765577}[：指定英文页面的标题信息。]{style="font-family:宋体"}*[english-title]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_2031979539}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_64763787}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[英文页面的标题信息为"]{style="font-family:宋体"}[SSL VPN service for company A]{lang="EN-US"}["，中文页面的标题信息为"公司]{style="font-family:宋体"}[A]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务"。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x861569142}

[\[Sysname\] sslvpn context ctx1]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] title english SSL VPN service for company A]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx1\] title chinese]{lang="EN-US"}[公司]{style="font-family:宋体"}[A]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务]{style="font-family:宋体"}
:::

::: {#-1188995761 .myid}
[]{#_Toc404793491}[]{#struct_0_x1617_x7307_x89722644}[]{#_Toc394323314}

**SSL VPN \-- SSL VPN配置命令 \-- verify-code**

------------------------------------------------------------------------

[**[verify-code enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_1497501365}[命令用来开启验证码验证功能。]{style="font-family:宋体"}

[**[undo verify-code enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1630503752}[命令用来关闭验证码验证功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1306386584}

[**[verify-code enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_x140505797}

[**[undo verify-code enable]{lang="EN-US"}**]{#struct_0_x1617_x7307_275231591}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x131870490}

[[验证码验证功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_x1617_x7307_275047198}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1912972400}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x615703864}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_523531504}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_892517687}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1918016425}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x733302636}

[[开启验证码验证后，用户登录时需要输入验证码。只有验证码验证成功后，才允许用户登录]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1859990652}[页面。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1734260126}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_x1830967673}[开启验证码验证功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x64419811}

[\[Sysname\] sslvpn context ctx]{lang="EN-US"}

[\[Sysname-sslvpn-context-ctx\] verify-code enable]{lang="EN-US"}
:::

::: {#1006503935 .myid}
[]{#_Toc404793492}[]{#struct_0_x1617_x7307_1673835937}[]{#_Toc394323292}

**SSL VPN \-- SSL VPN配置命令 \-- vpn-instance (SSL VPN context View)**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_561549778}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1126143689}[命令用来取消]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例关联]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1346344737}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_509374864}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_83862388}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_513196968}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1712049339}[访问实例关联公网。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1327351338}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_416721057}[访问实例视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1171472146}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x701162059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x1581971549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1443175628}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1501664130}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x256772590}

[[执行本命令后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1506342529}[访问实例包含的资源将属于关联的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[每个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x2133082522}[访问实例只能关联一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1907819148}[访问实例可以关联不存在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，但该]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例会处于未生效的状态。待]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例创建后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例进入生效状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_220090983}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_864432016}[配置名为]{style="font-family:宋体"}[contex1]{lang="EN-US"}[的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[访问实例关联]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> System-view]{lang="EN-US"}]{#struct_0_x1617_x7307_1337089473}

[\[Sysname\] sslvpn context context1]{lang="EN-US"}

[\[Sysname-sslvpn-context-context1\] vpn-instance vpn1]{lang="EN-US"}
:::

::: {#820411648 .myid}
[]{#_Toc404793493}[]{#struct_0_x1617_x7307_x1443412643}[]{#_Toc394323293}

**SSL VPN \-- SSL VPN配置命令 \-- vpn-instance (SSL VPN gateway view)**

------------------------------------------------------------------------

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_x1102285372}[命令用来配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_2108882219}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x915657428}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_1557284728}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_x1617_x7307_x254455068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x1583449585}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1298548353}[网关属于公网。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1867952943}

[[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1041775583}[网关视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1253762460}

[[network-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_700464000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x1617_x7307_x21690050}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_224318210}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_x1617_x7307_572018110}[：]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_x679045289}

[[每个]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_1655856995}[网关只能属于一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例又称为]{style="font-family:宋体"}[front VPN instance]{lang="EN-US"}[。]{style="font-family:宋体"}

[[本命令指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_x1617_x7307_x1969264529}[实例可以不存在，但此时]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关处于不生效的状态。待]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例创建后，]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关进入生效状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x1617_x7307_1223116710}

[[\# ]{lang="EN-US"}]{#struct_0_x1617_x7307_1255099020}[配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[网关]{style="font-family:宋体"}[gateway1]{lang="EN-US"}[属于]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x1617_x7307_x1021291184}

[\[Sysname\] sslvpn gateway gateway1]{lang="EN-US"}

[\[Sysname-sslvpn-gateway-gateway1\] vpn-instance vpn1]{lang="EN-US"}
:::
