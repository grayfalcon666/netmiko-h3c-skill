::: {#651077146 .myid}
[]{#_Toc404787369}[]{#struct_0_49241_76394_x227762404}[]{#_Toc151282199}

**ADVPN \-- VAM Server配置命令 \-- authentication-algorithm**

------------------------------------------------------------------------

[**[authentication-algorithm]{lang="EN-US"}**]{#struct_0_49241_76394_1010363057}[命令用来设置]{style="font-family:
宋体"}[VAM]{lang="EN-US"}[协议报文的验证算法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **authentication-algorithm**]{lang="EN-US"}]{#struct_0_49241_76394_1148626804}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1873442830}

[**[authentication-algorithm]{lang="EN-US"}**[ { **aes-xcbc-mac** \| **md5** \| **none** \| **sha-1** \| **sha-256** } \*]{lang="EN-US"}]{#struct_0_49241_76394_x169992695}

[**[undo authentication-algorithm]{lang="EN-US"}**]{#struct_0_49241_76394_1340213992}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_906284916}

[[VAM]{lang="EN-US"}]{#struct_0_49241_76394_x720092635}[协议报文的验证算法为]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1438848596}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1029065892}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1178090048}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_482596370}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x594567552}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_608410275}

[**[aes-xcbc-mac]{lang="EN-US"}**]{#struct_0_49241_76394_x195596199}[：表示采用]{style="font-family:宋体"}[AES-XCBC-MAC]{lang="EN-US"}[验证算法。]{style="font-family:宋体"}

[**[md5]{lang="EN-US"}**]{#struct_0_49241_76394_x1071509691}[：表示采用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[验证算法。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_49241_76394_672892736}[：表示不对]{style="font-family:宋体"}[VAM]{lang="EN-US"}[协议报文进行验证。]{style="font-family:宋体"}

[**[sha-1]{lang="EN-US"}**]{#struct_0_49241_76394_x844389784}[：表示采用]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[验证算法。]{style="font-family:宋体"}

[**[sha-256]{lang="EN-US"}**]{#struct_0_49241_76394_1449601640}[：表示采用]{style="font-family:宋体"}[SHA-256]{lang="EN-US"}[验证算法。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1158563797}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x941198521}[与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[固定使用]{style="font-family:宋体"}[SHA-1]{lang="EN-US"}[验证算法对连接初始化请求和响应报文进行完整性验证；使用协商出来的验证算法对其他]{style="font-family:宋体"}[VAM]{lang="EN-US"}[协议报文进行完整性验证。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_1526707617}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[验证算法在配置中的出现顺序决定其使用优先级。配置中越靠前的验证算法，其优先级越高。]{style="font-family:宋体"}]{#struct_0_49241_76394_x2101887262}[VAM Server]{lang="EN-US"}[在与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[协商时，从]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[支持的验证算法列表中选择]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上配置最靠前的算法作为协商结果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改本配置对已经注册的]{style="font-family:宋体"}]{#struct_0_49241_76394_x1872429749}[VAM Client]{lang="EN-US"}[没有影响，新注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[将采用修改后的验证算法进行协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1025617670}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1590440655}[设置在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中使用的验证算法优先级从高到低依次为]{style="font-family:
宋体"}[MD5]{lang="EN-US"}[、]{style="font-family:
宋体"}[SHA-1]{lang="EN-US"}[和]{style="font-family:宋体"}[SHA-256]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1689696777}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] authentication-algorithm md5]{lang="EN-US"}[ sha-1 sha-256]{lang="EN-US"}
:::

::: {#-1695505525 .myid}
[]{#_Toc404787370}[]{#struct_0_49241_76394_x594633088}[]{#_Toc151282200}[]{#_Toc375152366}[]{#_Toc375152367}

**ADVPN \-- VAM Server配置命令 \-- authentication-method**

------------------------------------------------------------------------

[**[authentication-method]{lang="EN-US"}**]{#struct_0_49241_76394_x540161891}[命令用来配置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[对]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的身份认证方式。]{style="font-family:宋体"}

[**[undo authentication-method]{lang="EN-US"}**]{#struct_0_49241_76394_x392788644}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1822588564}

[**[authentication-method]{lang="EN-US"}**[ { **none** \| { **chap** \| **pap** } \[ **domain** *isp-name* \] }]{lang="EN-US"}]{#struct_0_49241_76394_x1904735664}

[**[undo authentication-method]{lang="EN-US"}**]{#struct_0_49241_76394_x1640318569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x212154294}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x714431361}[使用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[方式对]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[进行身份认证，认证使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域为用户配置的系统默认域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x127246841}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_907745148}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2004296312}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_910238705}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x911171613}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1283433088}

[**[none]{lang="EN-US"}**]{#struct_0_49241_76394_90392257}[：表示不对]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[进行认证。]{style="font-family:宋体"}

[**[chap]{lang="EN-US"}**]{#struct_0_49241_76394_x1221476543}[：表示使用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[pap]{lang="EN-US"}**]{#struct_0_49241_76394_x594698624}[：表示使用]{style="font-family:宋体"}[PAP]{lang="EN-US"}[认证方式。]{style="font-family:宋体"}

[**[domain ]{lang="EN-US"}***[isp-name]{lang="EN-US"}*]{#struct_0_49241_76394_x937655924}[：指定认证使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}*[isp-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符。如果未指定本参数，则认证使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域为用户配置的系统默认域。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_775592908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}]{#struct_0_49241_76394_x1504691032}[指定]{style="font-family:宋体"}[的]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}[域不存在，]{lang="EN-US" style="font-family:宋体"}[则]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[对]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的身份认证会失败。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改本配置对已经注册的]{style="font-family:宋体"}]{#struct_0_49241_76394_x291931891}[VAM Client]{lang="EN-US"}[没有影响，新注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[将按照修改后的认证方式进行身份认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x301878792}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1814337221}[配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[对]{style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[采用]{style="font-family:宋体"}[CHAP]{lang="EN-US"}[方式进行身份认证，认证使用的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域为用户配置的系统默认域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x156796443}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] authentication-method chap]{lang="EN-US"}
:::

::: {#1796119369 .myid}
[]{#_Toc404787371}[]{#struct_0_49241_76394_x1959905530}[]{#_Toc375152369}[]{#_Toc375152370}[]{#_Toc349205126}[]{#_Toc349205127}[]{#_Toc349205128}[]{#_Toc349205129}[]{#_Toc349205130}[]{#_Toc349205131}[]{#_Toc349205132}[]{#_Toc349205133}[]{#_Toc349205134}[]{#_Toc349205135}[]{#_Toc349205136}[]{#_Toc349205137}[]{#_Toc349205138}[]{#_Toc349205139}[]{#_Toc349205140}[]{#_Toc349205141}[]{#_Toc349205142}[]{#_Toc349205143}[]{#_Toc349205144}[]{#_Toc349205145}[]{#_Toc349205146}[]{#_Toc349205147}[]{#_Toc349205148}[]{#_Toc349205149}[]{#_Toc349205150}[]{#_Toc349205151}[]{#_Toc349205152}[]{#_Toc349205153}[]{#_Toc349205154}[]{#_Toc349205155}[]{#_Toc349205156}[]{#_Toc349205157}[]{#_Toc349205158}[]{#_Toc349205159}[]{#_Toc349205160}[]{#_Toc349205161}[]{#_Toc349205162}[]{#_Toc349205163}[]{#_Toc349205164}[]{#_Toc349205165}[]{#_Toc349205166}[]{#_Toc349205167}[]{#_Toc349205168}[]{#_Toc349205169}[]{#_Toc349205170}[]{#_Toc349205171}[]{#_Toc349205172}[]{#_Toc349205173}[]{#_Toc349205174}[]{#_Toc349205175}

**ADVPN \-- VAM Server配置命令 \-- display vam server address-map**

------------------------------------------------------------------------

[**[display vam server address-map]{lang="EN-US"}**]{#struct_0_49241_76394_969513683}[命令用来显示注册到]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x454074420}

[**[display]{lang="EN-US"}**[ **vam** **server** **address-map** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ip-address* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_49241_76394_x1114693829}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1558975392}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_1852379603}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1802480271}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x594764160}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x559679307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1856709383}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_1840796901}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1024952275}

[**[advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_477895666}[：显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x1292576166}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的映射信息。]{style="font-family:宋体"}*[private-ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_49241_76394_2047152073}[：显示]{style="font-family:宋体"}[地址映射的详细信息。如果未指定本参数，则显示地址映射的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x696037961}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1361536551}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map]{lang="EN-US"}]{#struct_0_49241_76394_x594829696}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private address mappings: 2]{lang="EN-US"}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S]{lang="EN-US"}

[1          10.0.0.3         74.125.128.102              Spoke  Yes  0H 4M 21S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Total private address mappings: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 3]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          30.0.0.1         113.124.136.1               Hub    No   0H 0M 2S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 4]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          40.0.0.1         4001::1                     Hub    No   1H 8M 22S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 5]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          50.0.0.1         115.194.156.1               Hub    No   132H 41M 29S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_654970174}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_584817120}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private address mappings: 2]{lang="EN-US"}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S]{lang="EN-US"}

[1          10.0.0.3         74.125.128.102              Spoke  Yes  0H 4M 21S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1169316018}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[10.0.0.1]{lang="EN-US"}[的地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map advpn-domain 1 private-address 10.0.0.1]{lang="EN-US"}]{#struct_0_49241_76394_1416224715}

[Group      Private address  Public address              Type   NAT  Holding time]{lang="EN-US"}

[1          10.0.0.1         2001::1                     Hub    No   0H 13M 34S]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display vam server address-map]{lang="EN-US"}]{#struct_0_49241_76394_x1506945070}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_92472174}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x810507024}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x311867625}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x753776706}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x559466743}[域的名称]{style="font-family:宋体"}

[[Total private address mappings]{lang="EN-US"}]{#struct_0_49241_76394_x17221910}

[[IPv4]{lang="EN-US"}]{#struct_0_49241_76394_x593846656}[私网地址和公网地址映射总数]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_49241_76394_1128206299}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1181725981}[所属的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_2105084745}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1681320409}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_1604679572}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1466449173}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的公网地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_x449764600}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1913766139}[类型，有]{style="font-family:宋体"}[Hub]{lang="EN-US"}[和]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[两种类型]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_49241_76394_x192955521}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_231375961}[是否穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_x593912192}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_361577818}[的存活时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分钟]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x320560747}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map verbose]{lang="EN-US"}]{#struct_0_49241_76394_x594370943}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 10.0.0.1]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 10018]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 10018]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 10.0.0.3]{lang="EN-US"}

[Type              : Spoke]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 4M 21S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 74.125.128.102]{lang="EN-US"}

[Public port       : 11297]{lang="EN-US"}

[Registered address: 192.168.23.6]{lang="EN-US"}

[Registered port   : 2158]{lang="EN-US"}

[Behind NAT        : Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 3]{lang="EN-US"}

[Private address   : 30.0.0.1]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 0M 2S]{lang="EN-US"}

[Link protocol     : GRE]{lang="EN-US"}

[Public address    : 113.124.136.1]{lang="EN-US"}

[Registered address: 113.124.136.1]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 4]{lang="EN-US"}

[Private address   : 40.0.0.1]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 1H 8M 22S]{lang="EN-US"}

[Link protocol     : IPsec-UDP]{lang="EN-US"}

[Public address    : 4001::1]{lang="EN-US"}

[Registered address: 4001::1]{lang="EN-US"}

[Registered port   : 4072]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 5]{lang="EN-US"}

[Private address   : 50.0.0.1]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 132H 41M 29S]{lang="EN-US"}

[Link protocol     : IPsec-GRE]{lang="EN-US"}

[Public address    : 115.194.156.1]{lang="EN-US"}

[Registered address: 115.194.156.1]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x126212641}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map advpn-domain 1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_x594436479}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 10.0.0.1]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 10018]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 10018]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 10.0.0.3]{lang="EN-US"}

[Type              : Spoke]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 4M 21S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 74.125.128.102]{lang="EN-US"}

[Public port       : 11297]{lang="EN-US"}

[Registered address: 192.168.23.6]{lang="EN-US"}

[Registered port   : 2158]{lang="EN-US"}

[Behind NAT        : Yes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_983961441}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[10.0.0.1]{lang="EN-US"}[的地址映射详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server address-map advpn-domain 1 private-address 10.0.0.1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_72114196}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 10.0.0.1]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 10018]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 10018]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display vam server address-map verbose]{lang="EN-US"}]{#struct_0_49241_76394_x1619188517}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_95342528}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x1831010342}

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x1520560964}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x594502015}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2104935218}[域的名称]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_x515876137}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_413645913}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_1021784280}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x2004328181}[类型，有]{style="font-family:宋体"}[Hub]{lang="EN-US"}[和]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[两种类型]{style="font-family:宋体"}

[[Hub group]{lang="EN-US"}]{#struct_0_49241_76394_x1687610879}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1518389598}[所属的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_841889147}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1637373154}[的存活时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分钟]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_950102146}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x594567551}[建立]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道使用的链路层协议，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_49241_76394_608344739}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRE]{lang="EN-US"}]{#struct_0_49241_76394_x75516093}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-UDP]{lang="EN-US"}]{#struct_0_49241_76394_1286271494}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-GRE]{lang="EN-US"}]{#struct_0_49241_76394_1861872710}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_x1675674631}

[[NAT]{lang="EN-US"}]{#struct_0_49241_76394_x750283307}[转换后的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的公网地址]{style="font-family:宋体"}

[[Public port]{lang="EN-US"}]{#struct_0_49241_76394_1932694549}

[[NAT]{lang="EN-US"}]{#struct_0_49241_76394_x594633087}[转换后的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x541144931}[为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[Registered address]{lang="EN-US"}]{#struct_0_49241_76394_1583693407}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_579338900}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的公网地址]{style="font-family:宋体"}

[[Registered port]{lang="EN-US"}]{#struct_0_49241_76394_655568472}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1775449083}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_1794513687}[为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[IPsec address]{lang="EN-US"}]{#struct_0_49241_76394_x305333696}

[[建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_49241_76394_x1171096465}[隧道时，本]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[使用的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x594698623}[为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[IPsec port]{lang="EN-US"}]{#struct_0_49241_76394_x937328244}

[[建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_49241_76394_x1967814898}[隧道时，本]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x2078030071}[为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[Behind NAT]{lang="EN-US"}]{#struct_0_49241_76394_x774717988}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1372080560}[是否穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1383478541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **vam** **server** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_775737874}

::: {#-2117217591 .myid}
[]{#_Toc404787372}[]{#struct_0_49241_76394_x594764159}

**ADVPN \-- VAM Server配置命令 \-- display vam server ipv6 address-map**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vam server ipv6** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_x560138058}[命令用来显示注册到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_2049539043}

[**[display]{lang="EN-US"}**[ **vam** **server** **ipv6** **address-map** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ipv6-address* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_49241_76394_x140947217}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1824246445}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x201766160}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1084368199}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x812458299}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x2036369540}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_960016078}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_227819994}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1934823086}

[**[advpn-domain]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_x264468298}[：显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x1741980557}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的映射信息。]{style="font-family:宋体"}*[private-ipv6-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_49241_76394_685252183}[：显示]{style="font-family:宋体"}[地址映射的详细信息。如果未指定本参数，则显示地址映射的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_992645673}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1718523953}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 address-map]{lang="EN-US"}]{#struct_0_49241_76394_x594829695}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private address mappings: 2]{lang="EN-US"}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S]{lang="EN-US"}

[2          1000::2:0:0:1         220.181.111.85         Spoke  Yes  0H 4M 21S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Total private address mappings: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 3]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1003::1:0:0:1         3001::1                Hub    No   0H 0M 2S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 4]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1004::1:0:0:1         202.108.231.125        Hub    No   1H 8M 22S]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 5]{lang="EN-US"}

[Total private address mappings: 1]{lang="EN-US"}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1005::1:0:0:1         5001::1                Hub    No   132H 41M 29S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_654904638}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 address-map advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_x564172106}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private address mappings: 2]{lang="EN-US"}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S]{lang="EN-US"}

[2          1000::2:0:0:1         220.181.111.85         Spoke  Yes  0H 4M 21S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x2138895882}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[1000::1:0:0:1]{lang="EN-US"}[的地址映射信息。]{style="font-family:
宋体"}

[[\<Sysname\> display vam server ipv6 address-map advpn-domain 1 private-address 1000::1:0:0:1]{lang="EN-US"}]{#struct_0_49241_76394_x593846655}

[Group      Private address       Public address         Type   NAT  Holding time]{lang="EN-US"}

[1          1000::1:0:0:1         2001::1                Hub    No   0H 13M 34S]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display vam server ipv6 address-map]{lang="EN-US"}]{#struct_0_49241_76394_1128402907}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_90843894}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_1099898002}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_827765453}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_568795325}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_64352454}[域的名称]{style="font-family:宋体"}

[[Total private address mappings]{lang="EN-US"}]{#struct_0_49241_76394_1390067056}

[[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_1398590795}[私网地址和公网地址映射总数]{style="font-family:宋体"}

[[Group]{lang="EN-US"}]{#struct_0_49241_76394_1236424723}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1993981395}[所属的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_x1182169137}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x868948290}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_x593912191}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_361381210}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的公网地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_x2120347132}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1577132801}[类型，有]{style="font-family:宋体"}[Hub]{lang="EN-US"}[和]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[两种类型]{style="font-family:宋体"}

[[NAT]{lang="EN-US"}]{#struct_0_49241_76394_x508052278}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1182660794}[是否穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_740853991}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1071635659}[的存活时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分钟]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_179593639}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 address-map verbose]{lang="EN-US"}]{#struct_0_49241_76394_971647465}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 1000::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::50:4 ]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 2098]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 2098]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 1000::2:0:0:1]{lang="EN-US"}

[Link local address: FE80::60:4 ]{lang="EN-US"}

[Type              : Spoke]{lang="EN-US"}

[Hub group         : 2]{lang="EN-US"}

[Holding time      : 0H 4M 21S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 220.181.111.85]{lang="EN-US"}

[Public port       : 10018]{lang="EN-US"}

[Registered address: 10.158.26.14]{lang="EN-US"}

[Registered port   : 2694]{lang="EN-US"}

[Behind NAT        : Yes]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 3]{lang="EN-US"}

[Private address   : 1003::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::70:4 ]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 0M 2S]{lang="EN-US"}

[Link protocol     : GRE]{lang="EN-US"}

[Public address    : 3001::1]{lang="EN-US"}

[Registered address: 3001::1]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 4]{lang="EN-US"}

[Private address   : 1004::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::80:4 ]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 1H 8M 22S]{lang="EN-US"}

[Link protocol     : IPsec-UDP]{lang="EN-US"}

[Public address    : 202.108.231.125]{lang="EN-US"}

[Registered address: 202.108.231.125]{lang="EN-US"}

[Registered port   : 4072]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 5]{lang="EN-US"}

[Private address   : 1005::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::90:4 ]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 132H 41M 29S]{lang="EN-US"}

[Link protocol     : IPsec-GRE]{lang="EN-US"}

[Public address    : 5001::1]{lang="EN-US"}

[Registered address: 5001::1]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_83227825}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 address-map advpn-domain 1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_971581929}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 1000::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::50:4 ]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 2098]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 2098]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 1000::2:0:0:1]{lang="EN-US"}

[Link local address: FE80::60:4 ]{lang="EN-US"}

[Type              : Spoke]{lang="EN-US"}

[Hub group         : 2]{lang="EN-US"}

[Holding time      : 0H 4M 21S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 220.181.111.85]{lang="EN-US"}

[Public port       : 10018]{lang="EN-US"}

[Registered address: 10.158.26.14]{lang="EN-US"}

[Registered port   : 2694]{lang="EN-US"}

[Behind NAT        : Yes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x555527190}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[1000::1:0:0:1]{lang="EN-US"}[的地址映射详细信息。]{style="font-family:
宋体"}

[[\<Sysname\> display vam server ipv6 address-map advpn-domain 1 ipv6 private-address 1000::1:0:0:1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_1056490035}

[ADVPN domain name : 1]{lang="EN-US"}

[Private address   : 1000::1:0:0:1]{lang="EN-US"}

[Link local address: FE80::50:4 ]{lang="EN-US"}

[Type              : Hub]{lang="EN-US"}

[Hub group         : 1]{lang="EN-US"}

[Holding time      : 0H 13M 34S]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Public address    : 2001::1]{lang="EN-US"}

[Public port       : 2098]{lang="EN-US"}

[Registered address: 2001::1]{lang="EN-US"}

[Registered port   : 2098]{lang="EN-US"}

[Behind NAT        : No]{lang="EN-US"}

[[表1-4 ]{lang="EN-US"}[display vam server ipv6 address-map verbose]{lang="EN-US"}]{#struct_0_49241_76394_977675406}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_87512354}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x1906432717}

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x1368433661}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x1120481705}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x921663410}[域的名称]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_x930390166}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_971516393}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Link local address]{lang="EN-US"}]{#struct_0_49241_76394_x2040740547}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_368444573}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网链路本地地址]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_1307162233}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x851494252}[类型，有]{style="font-family:宋体"}[Hub]{lang="EN-US"}[和]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[两种类型]{style="font-family:宋体"}

[[Hub group]{lang="EN-US"}]{#struct_0_49241_76394_x446160864}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_971450857}[所属的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_x182466690}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1452069337}[的存活时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分钟]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_813403000}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_800992932}[建立]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道使用的链路层协议，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_49241_76394_x1533650929}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRE]{lang="EN-US"}]{#struct_0_49241_76394_x225447080}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-UDP]{lang="EN-US"}]{#struct_0_49241_76394_1906478277}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-GRE]{lang="EN-US"}]{#struct_0_49241_76394_971385321}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_1179305444}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_719491831}[的真实公网地址]{style="font-family:宋体"}

[[Public port]{lang="EN-US"}]{#struct_0_49241_76394_938318649}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_320110234}[的真实]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_1268527639}[为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[Registered address]{lang="EN-US"}]{#struct_0_49241_76394_645301093}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1386153871}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的公网地址]{style="font-family:宋体"}

[[Registered port]{lang="EN-US"}]{#struct_0_49241_76394_971319785}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1911122005}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x1416251508}[为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[IPsec address]{lang="EN-US"}]{#struct_0_49241_76394_2035642347}

[[IPsec]{lang="EN-US"}]{#struct_0_49241_76394_993128982}[链路使用的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_1959289632}[为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[IPsec port]{lang="EN-US"}]{#struct_0_49241_76394_x72854131}

[[IPsec]{lang="EN-US"}]{#struct_0_49241_76394_314078674}[链路使用的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[本字段仅在]{style="font-family:宋体"}[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_971254249}[为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时显示]{style="font-family:宋体"}

[[Behind NAT]{lang="EN-US"}]{#struct_0_49241_76394_x1550960278}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1543656119}[是否穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x348916912}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset]{lang="EN-US"}**[ **vam** **server** **ipv6** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_311907858}

::: {#-1209867406 .myid}
[]{#_Toc404787373}[]{#struct_0_49241_76394_x22568573}

**ADVPN \-- VAM Server配置命令 \-- display vam server ipv6 private-network**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vam server ipv6** **private-network**]{lang="EN-US"}]{#struct_0_49241_76394_x459758650}[命令用来显示注册到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_2074318721}

[**[display]{lang="EN-US"}**[ **vam** **server** **ipv6** **private-network** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ipv6-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_x1485077747}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1335802335}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_332463307}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_972237289}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1582810297}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_982591938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_2121362492}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_140382201}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x949405269}

[**[advpn-domain]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_2147201923}[：显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x2107987028}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的私网信息。]{style="font-family:宋体"}*[private-ipv6-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1068416431}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x2038903346}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 private-network]{lang="EN-US"}]{#struct_0_49241_76394_972171753}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private networks: 5]{lang="EN-US"}

[Network/Prefix                     Private address                    Preference]{lang="EN-US"}

[1000::1:0:0:0/96                   1000::1:0:0:2                      80]{lang="EN-US"}

[1000::1:0:0:0/100                  1000::1:0:0:1                      80]{lang="EN-US"}

[1000::1:1:0:0/96                   1000::1:0:0:1                      80]{lang="EN-US"}

[1000::2:0:0:0/96                   1000::1:0:0:2                      80]{lang="EN-US"}

[1000::2:0:0:0/96                   1000::2:0:0:2                      80]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Total private networks: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 3]{lang="EN-US"}

[Total private networks: 1]{lang="EN-US"}

[Network/Prefix                     Private address                    Preference]{lang="EN-US"}

[1001::1:0:0:0/100                  1001::1:0:0:1                      80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_2070666504}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server ipv6 private-network advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_665707626}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private networks: 5]{lang="EN-US"}

[Network/Prefix                     Private address                    Preference]{lang="EN-US"}

[1000::1:0:0:0/96                   1000::1:0:0:2                      80]{lang="EN-US"}

[1000::1:0:0:0/100                  1000::1:0:0:1                      80]{lang="EN-US"}

[1000::1:1:0:0/96                   1000::1:0:0:1                      80]{lang="EN-US"}

[1000::2:0:0:0/96                   1000::1:0:0:2                      80]{lang="EN-US"}

[1000::2:0:0:0/96                   1000::2:0:0:2                      80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1789217771}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[1000::1:0:0:1]{lang="EN-US"}[的私网信息。]{style="font-family:
宋体"}

[[\<Sysname\> display vam server ipv6 private-network advpn-domain 1 private-address 1000::1:0:0:1]{lang="EN-US"}]{#struct_0_49241_76394_425514375}

[Total private networks: 2]{lang="EN-US"}

[Network/Prefix                     Private address                    Preference]{lang="EN-US"}

[1000::1:0:0:0/100                  1000::1:0:0:1                      80]{lang="EN-US"}

[1000::1:1:0:0/96                   1000::1:0:0:1                      80]{lang="EN-US"}

[[表1-5 ]{lang="EN-US"}[display vam server ipv6 address-map]{lang="EN-US"}]{#struct_0_49241_76394_570536407}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_117020362}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x1849367187}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_168492378}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_2109407671}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_644642237}[域的名称]{style="font-family:宋体"}

[[Total private networks]{lang="EN-US"}]{#struct_0_49241_76394_971713002}

[[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_1698243343}[私网总数]{style="font-family:宋体"}

[[Network/Prefix]{lang="EN-US"}]{#struct_0_49241_76394_x1935672543}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_390048038}[接口下配置的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网网络地址]{style="font-family:宋体"}[/]{lang="EN-US"}[前缀长度]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_1716984804}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1737152105}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_49241_76394_236453425}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_724244957}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网路由优先级]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1114149038 .myid}
[]{#_Toc323022581}[]{#_Toc404787374}[]{#struct_0_49241_76394_x632732968}

**ADVPN \-- VAM Server配置命令 \-- display vam server private-network**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vam** **server** **private-network**]{lang="EN-US"}]{#struct_0_49241_76394_x2005349395}[命令用来显示注册到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x342811600}

[**[display]{lang="EN-US"}**[ **vam** **server** **private-network** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ip-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_1145341549}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1146534032}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_971647466}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_83227826}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x193196513}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x575009063}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1945626661}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_x1841854484}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x429957913}

[**[advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_1835765027}[：显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有注册]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_1520618933}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的私网信息。]{style="font-family:宋体"}*[private-ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x163784588}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_184415195}[显示所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server private-network]{lang="EN-US"}]{#struct_0_49241_76394_971581930}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private networks: 5]{lang="EN-US"}

[Network/Mask              Private address        Preference]{lang="EN-US"}

[192.168.0.0/24            10.0.0.2               80]{lang="EN-US"}

[192.168.0.0/28            10.0.0.1               80]{lang="EN-US"}

[192.168.1.0/24            10.0.0.1               80]{lang="EN-US"}

[192.168.100.0/24          10.0.0.2               80]{lang="EN-US"}

[192.168.100.0/24          10.0.0.3               80]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Total private networks: 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name: 3]{lang="EN-US"}

[Total private networks: 1]{lang="EN-US"}

[Network/Mask              Private address        Preference]{lang="EN-US"}

[192.168.200.0/24          20.0.0.1               80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1400787953}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中的]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server private-network advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_x448691873}

[ADVPN domain name: 1]{lang="EN-US"}

[Total private networks: 5]{lang="EN-US"}

[Network/Mask              Private address        Preference]{lang="EN-US"}

[192.168.0.0/24            10.0.0.2               80]{lang="EN-US"}

[192.168.0.0/28            10.0.0.1               80]{lang="EN-US"}

[192.168.1.0/24            10.0.0.1               80]{lang="EN-US"}

[192.168.100.0/24          10.0.0.2               80]{lang="EN-US"}

[192.168.100.0/24          10.0.0.3               80]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x50035156}[显示]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[10.0.0.1]{lang="EN-US"}[的私网信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server private-network advpn-domain 1 private-address 10.0.0.1]{lang="EN-US"}]{#struct_0_49241_76394_x1029478987}

[Total private networks: 5]{lang="EN-US"}

[Network/Mask              Private address        Preference]{lang="EN-US"}

[192.168.0.0/28            10.0.0.1               80]{lang="EN-US"}

[192.168.1.0/24            10.0.0.1               80]{lang="EN-US"}

[[表1-6 ]{lang="EN-US"}[display vam server address-map]{lang="EN-US"}]{#struct_0_49241_76394_982519279}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_110532024}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_981023496}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_94893405}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_680028320}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971516394}[域的名称]{style="font-family:宋体"}

[[Total private network number]{lang="EN-US"}]{#struct_0_49241_76394_x2040740544}

[[IPv4]{lang="EN-US"}]{#struct_0_49241_76394_1934528514}[私网总数]{style="font-family:宋体"}

[[Network/Mask]{lang="EN-US"}]{#struct_0_49241_76394_466073937}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_x1783296269}[接口下配置的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网网络地址]{style="font-family:宋体"}[/]{lang="EN-US"}[子网掩码长度]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_x922820069}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x269418022}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网地址]{style="font-family:宋体"}

[[Preference]{lang="EN-US"}]{#struct_0_49241_76394_291863662}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1828265446}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册的私网路由优先级]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1467840257 .myid}
[]{#_Toc404787375}[]{#struct_0_49241_76394_x834440689}

**ADVPN \-- VAM Server配置命令 \-- display vam server statistics**

------------------------------------------------------------------------

[**[display vam server statistic]{lang="EN-US"}**]{#struct_0_49241_76394_1882383003}[命令用来显示]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[上]{style="font-family:
宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_60228346}

[**[display]{lang="EN-US"}**[ **vam** **server** **statistics** \[ **advpn-domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_971450858}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x182466695}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1451741657}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1418381598}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_695439526}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x108478488}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_227579458}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_1821702859}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_85597370}

[**[advpn-domain]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_39577053}[：]{style="font-family:宋体"}[显示指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2092904946}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1855540046}[显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam server statistics]{lang="EN-US"}]{#struct_0_49241_76394_971319786}

[Total ADVPN number: 3]{lang="EN-US"}

[Total spoke number: 121]{lang="EN-US"}

[Total hub number  : 3]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name      : 1]{lang="EN-US"}

[Server status          : Enabled]{lang="EN-US"}

[Holding time           : 0H 1M 47S]{lang="EN-US"}

[Registered spoke number: 98]{lang="EN-US"}

[Registered hub number  : 2]{lang="EN-US"}

[Packets received:]{lang="EN-US"}

[  Initialization request        : 100]{lang="EN-US"}

[  Initialization complete       : 100]{lang="EN-US"}

[  Register request              : 100]{lang="EN-US"}

[  Authentication information    : 100]{lang="EN-US"}

[  Address resolution request    : 203]{lang="EN-US"}

[  Network registration request  : 59]{lang="EN-US"}

[  Update request                : 196]{lang="EN-US"}

[  Logout request                : 0]{lang="EN-US"}

[  Hub information response      : 2]{lang="EN-US"}

[  Data flow information response: 0]{lang="EN-US"}

[  Keepalive                     : 642]{lang="EN-US"}

[  Error notification            : 0]{lang="EN-US"}

[  Unkonwn                       : 0]{lang="EN-US"}

[Packets sent:]{lang="EN-US"}

[  Initialization response      : 100]{lang="EN-US"}

[  Initialization complete      : 100]{lang="EN-US"}

[  Authentication request       : 100]{lang="EN-US"}

[  Register response            : 100]{lang="EN-US"}

[  Address resolution response  : 203]{lang="EN-US"}

[  Network registration response: 59]{lang="EN-US"}

[  Update response              : 196]{lang="EN-US"}

[  Hub information request      : 2]{lang="EN-US"}

[  Data flow information request: 0]{lang="EN-US"}

[  Logout response              : 0]{lang="EN-US"}

[  Keepalive                    : 642]{lang="EN-US"}

[  Error notification           : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name      : 2]{lang="EN-US"}

[Server status          : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[ADVPN domain name      : 3]{lang="EN-US"}

[Server status          : Enabled]{lang="EN-US"}

[Holding time           : 0H 33M 53S]{lang="EN-US"}

[Registered spoke number: 23]{lang="EN-US"}

[Registered hub number  : 1]{lang="EN-US"}

[Packets received:]{lang="EN-US"}

[  Initialization request        : 24]{lang="EN-US"}

[  Initialization complete       : 24]{lang="EN-US"}

[  Register request              : 24]{lang="EN-US"}

[  Authentication information    : 24]{lang="EN-US"}

[  Address resolution request    : 23]{lang="EN-US"}

[  Network registration request  : 0]{lang="EN-US"}

[  Update request                : 5]{lang="EN-US"}

[  Logout request                : 0]{lang="EN-US"}

[  Hub information response      : 2]{lang="EN-US"}

[  Data flow information response: 0]{lang="EN-US"}

[  Keepalive                     : 362]{lang="EN-US"}

[  Error notification            : 0]{lang="EN-US"}

[  Unkonwn                       : 0]{lang="EN-US"}

[Packets sent:]{lang="EN-US"}

[  Initialization response      : 24]{lang="EN-US"}

[  Initialization complete      : 24]{lang="EN-US"}

[  Authentication request       : 24]{lang="EN-US"}

[  Register response            : 24]{lang="EN-US"}

[  Address resolution response  : 23]{lang="EN-US"}

[  Network registration response: 0]{lang="EN-US"}

[  Update response              : 0]{lang="EN-US"}

[  Hub information request      : 2]{lang="EN-US"}

[  Data flow information request: 0]{lang="EN-US"}

[  Logout response              : 0]{lang="EN-US"}

[  Keepalive                    : 362]{lang="EN-US"}

[  Error notification           : 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1911122002}[显示]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的统计信息。]{style="font-family:
宋体"}

[[\<Sysname\> display vam server statistics advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_971254250}

[ADVPN domain name      : 1]{lang="EN-US"}

[Server status          : Enabled]{lang="EN-US"}

[Holding time           : 0H 1M 47S]{lang="EN-US"}

[Registered spoke number: 98]{lang="EN-US"}

[Registered hub number  : 2]{lang="EN-US"}

[Packets received:]{lang="EN-US"}

[  Initialization request        : 100]{lang="EN-US"}

[  Initialization complete       : 100]{lang="EN-US"}

[  Register request              : 100]{lang="EN-US"}

[  Authentication information    : 100]{lang="EN-US"}

[  Address resolution request    : 203]{lang="EN-US"}

[  Network registration request  : 59]{lang="EN-US"}

[  Update request                : 196]{lang="EN-US"}

[  Logout request                : 0]{lang="EN-US"}

[  Hub information response      : 2]{lang="EN-US"}

[  Data flow information response: 0]{lang="EN-US"}

[  Keepalive                     : 642]{lang="EN-US"}

[  Error notification            : 0]{lang="EN-US"}

[  Unkonwn                       : 0]{lang="EN-US"}

[Packets sent:]{lang="EN-US"}

[  Initialization response      : 100]{lang="EN-US"}

[  Initialization complete      : 100]{lang="EN-US"}

[  Authentication request       : 100]{lang="EN-US"}

[  Register response            : 100]{lang="EN-US"}

[  Address resolution response  : 203]{lang="EN-US"}

[  Network registration response: 59]{lang="EN-US"}

[  Update response              : 196]{lang="EN-US"}

[  Hub information request      : 2]{lang="EN-US"}

[  Data flow information request: 0]{lang="EN-US"}

[  Logout response              : 0]{lang="EN-US"}

[  Keepalive                    : 642]{lang="EN-US"}

[  Error notification           : 0]{lang="EN-US"}

[[表1-7 ]{lang="EN-US"}[display vam server statistics]{lang="EN-US"}]{#struct_0_49241_76394_787691891}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_112694310}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_1668708243}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x1157714290}

[[Total ADVPN number]{lang="EN-US"}]{#struct_0_49241_76394_1175272115}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x165536130}[上]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的数目]{style="font-family:宋体"}

[[Total spoke number]{lang="EN-US"}]{#struct_0_49241_76394_972237290}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_755841856}[上所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[类型客户端数目]{style="font-family:宋体"}

[[Total hub number]{lang="EN-US"}]{#struct_0_49241_76394_x1270042760}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x998440687}[上所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中]{style="font-family:宋体"}[Hub]{lang="EN-US"}[类型客户端数目]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x449042899}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1164453675}[域的名称]{style="font-family:宋体"}

[[Server status]{lang="EN-US"}]{#struct_0_49241_76394_x1102925546}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x802116261}[域中]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能的启用情况：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_49241_76394_1769331215}[：表示启用]{lang="EN-US" style="font-family:宋体"}[VAM ]{lang="EN-US"}[S]{lang="EN-US"}[erver]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_49241_76394_x1039218552}[：表示关闭]{lang="EN-US" style="font-family:宋体"}[VAM ]{lang="EN-US"}[S]{lang="EN-US"}[erver]{lang="EN-US"}[功能]{lang="EN-US" style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_972171754}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2070666503}[域的存活时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分钟]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Registered spoke number]{lang="EN-US"}]{#struct_0_49241_76394_666035306}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2078708602}[域中注册的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Registered hub number]{lang="EN-US"}]{#struct_0_49241_76394_x190413937}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_14534741}[域中注册的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[数目]{style="font-family:宋体"}

[[Packets received]{lang="EN-US"}]{#struct_0_49241_76394_465453796}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x808460295}[域中接收的报文数目]{style="font-family:宋体"}

[[Initialization request]{lang="EN-US"}]{#struct_0_49241_76394_957870441}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971712999}[域中接收的初始化请求报文数目]{style="font-family:宋体"}

[[Initialization complete]{lang="EN-US"}]{#struct_0_49241_76394_x1481551023}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1858360752}[域中接收的初始化完成报文数目]{style="font-family:宋体"}

[[Register request]{lang="EN-US"}]{#struct_0_49241_76394_x1023335119}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2046547563}[域中接收的注册请求报文数目]{style="font-family:宋体"}

[[Authentication information]{lang="EN-US"}]{#struct_0_49241_76394_2028204147}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_586765485}[域中接收的认证信息报文数目]{style="font-family:宋体"}

[[Address resolution request]{lang="EN-US"}]{#struct_0_49241_76394_247010813}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971647463}[域中接收的地址解析请求报文数目]{style="font-family:宋体"}

[[Network registration request]{lang="EN-US"}]{#struct_0_49241_76394_83227831}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_961708730}[域中接收的私网注册请求报文数目]{style="font-family:宋体"}

[[Update request]{lang="EN-US"}]{#struct_0_49241_76394_1905104711}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2101152200}[域中接收的节点更新请求报文数目]{style="font-family:宋体"}

[[Logout request]{lang="EN-US"}]{#struct_0_49241_76394_x1835735718}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x844346996}[域中接收的清除请求报文数目]{style="font-family:宋体"}

[[Hub information response]{lang="EN-US"}]{#struct_0_49241_76394_1529828692}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971581927}[域中接收的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[信息响应报文数目]{style="font-family:宋体"}

[[Data flow information response]{lang="EN-US"}]{#struct_0_49241_76394_x555527176}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1056883249}[域中接收的数据流信息响应报文数目]{style="font-family:宋体"}

[[Keepalive]{lang="EN-US"}]{#struct_0_49241_76394_1765983804}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1668526197}[域中接收的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文数目]{style="font-family:宋体"}

[[Error notification]{lang="EN-US"}]{#struct_0_49241_76394_971516391}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2040740549}[域中接收的错误通知报文数目]{style="font-family:宋体"}

[[Unkonwn]{lang="EN-US"}]{#struct_0_49241_76394_818783267}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1075554512}[域中接收的未知报文或错误报文数目]{style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_49241_76394_1972176593}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971450855}[域中发送的报文数目]{style="font-family:宋体"}

[[Initialization response]{lang="EN-US"}]{#struct_0_49241_76394_x182466692}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1451938265}[域中发送的初始化响应报文数目]{style="font-family:宋体"}

[[Initialization complete]{lang="EN-US"}]{#struct_0_49241_76394_830975147}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1039945212}[域中发送的初始化完成报文数目]{style="font-family:宋体"}

[[Authentication request]{lang="EN-US"}]{#struct_0_49241_76394_141010968}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971385319}[域中发送的认证请求报文数目]{style="font-family:宋体"}

[[Register response]{lang="EN-US"}]{#struct_0_49241_76394_x777009700}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1414928345}[域中发送的注册响应报文数目]{style="font-family:宋体"}

[[Address resolution response]{lang="EN-US"}]{#struct_0_49241_76394_x1161599741}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_92008057}[域中发送的地址解析响应报文数目]{style="font-family:宋体"}

[[Network registration response]{lang="EN-US"}]{#struct_0_49241_76394_971319783}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1911122007}[域中发送的子网注册响应报文数目]{style="font-family:宋体"}

[[Update response]{lang="EN-US"}]{#struct_0_49241_76394_x253452094}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x70842022}[域中发送的节点更新响应报文数目]{style="font-family:宋体"}

[[Hub information request]{lang="EN-US"}]{#struct_0_49241_76394_x171839133}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x645273199}[域中发送的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[信息请求报文数目]{style="font-family:宋体"}

[[Data flow information request]{lang="EN-US"}]{#struct_0_49241_76394_971254247}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1550960272}[域中发送的数据流信息请求报文数目]{style="font-family:宋体"}

[[Logout response]{lang="EN-US"}]{#struct_0_49241_76394_x737087065}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1845920731}[域中发送的清除响应报文数目]{style="font-family:宋体"}

[[Keepalive]{lang="EN-US"}]{#struct_0_49241_76394_x491109714}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_972237287}[域中发送的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文数目]{style="font-family:宋体"}

[[Error notification]{lang="EN-US"}]{#struct_0_49241_76394_x1582810303}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1343596715}[域中发送的错误通知报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_286248224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ]{lang="EN-US"}[vam server statistic]{lang="EN-US"}**]{#struct_0_49241_76394_936390913}

::: {#711665932 .myid}
[]{#_Toc404787376}[]{#struct_0_49241_76394_x662289793}[]{#_Toc323022582}

**ADVPN \-- VAM Server配置命令 \-- encryption-algorithm**

------------------------------------------------------------------------

[**[encryption-algorithm]{lang="EN-US"}**]{#struct_0_49241_76394_x1542393763}[命令用来配置]{style="font-family:宋体"}[VAM]{lang="EN-US"}[协议报文的加密算法。]{style="font-family:宋体"}

[**[undo encryption-algorithm]{lang="EN-US"}**]{#struct_0_49241_76394_2037777353}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x269243731}

[**[encryption-algorithm]{lang="EN-US"}**[ { **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **aes-ctr-128** \| **aes-ctr-192** \| **aes-ctr-256** \| **des-cbc** \| **none** } \*]{lang="EN-US"}]{#struct_0_49241_76394_972171751}

[**[undo encryption-algorithm]{lang="EN-US"}**]{#struct_0_49241_76394_2070666506}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_665838698}

[[按照优先级由高到低依次使用]{style="font-family:宋体"}[AES-CBC-256]{lang="EN-US"}]{#struct_0_49241_76394_1526221646}[、]{style="font-family:宋体"}[AES-CBC-192]{lang="EN-US"}[、]{style="font-family:宋体"}[AES-CBC-128]{lang="EN-US"}[、]{style="font-family:宋体"}[AES-CTR-256]{lang="EN-US"}[、]{style="font-family:宋体"}[AES-CTR-192]{lang="EN-US"}[、]{style="font-family:宋体"}[AES-CTR-128]{lang="EN-US"}[、]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}[、]{style="font-family:宋体"}[DES-CBC]{lang="EN-US"}[算法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x934041408}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x673878764}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1766760920}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_111030838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1436833256}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1083807398}

[**[3des-cbc]{lang="EN-US"}**]{#struct_0_49241_76394_x64236478}[：表示采用]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}[加密算法。]{style="font-family:宋体"}

[**[aes-cbc-128]{lang="EN-US"}**]{#struct_0_49241_76394_x1629995368}[：表示采用]{style="font-family:宋体"}[AES-CBC]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[128]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[aes-cbc-192]{lang="EN-US"}**]{#struct_0_49241_76394_x2036900140}[：表示采用]{style="font-family:宋体"}[AES-CBC]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[192]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[aes-cbc-256]{lang="EN-US"}**]{#struct_0_49241_76394_16228052}[：表示采用]{style="font-family:宋体"}[AES-CBC]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[256]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[aes-ctr-128]{lang="EN-US"}**]{#struct_0_49241_76394_x189807030}[：表示采用]{style="font-family:宋体"}[AES-CTR]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[128]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[aes-ctr-192]{lang="EN-US"}**]{#struct_0_49241_76394_971713000}[：表示采用]{style="font-family:宋体"}[AES-CTR]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[192]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[aes-ctr-256]{lang="EN-US"}**]{#struct_0_49241_76394_1698243341}[：表示采用]{style="font-family:宋体"}[AES-CTR]{lang="EN-US"}[加密算法，密钥长度]{style="font-family:宋体"}[256]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[des-cbc]{lang="EN-US"}**]{#struct_0_49241_76394_x1935803615}[：表示采用]{style="font-family:宋体"}[DES-CBC]{lang="EN-US"}[加密算法。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_49241_76394_x793196568}[：表示不对]{style="font-family:宋体"}[VAM]{lang="EN-US"}[协议报文进行加密。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x969208107}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1616020534}[与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[固定使用]{style="font-family:宋体"}[AES-CBC-128]{lang="EN-US"}[加密算法对连接初始化请求和响应报文进行加密；使用协商出来的加密算法对其他]{style="font-family:宋体"}[VAM]{lang="EN-US"}[协议报文进行加密。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_x771946364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[加密算法在配置中的出现顺序决定其使用优先级。配置中越靠前的加密算法，其优先级越高。]{style="font-family:宋体"}]{#struct_0_49241_76394_1581235843}[VAM Server]{lang="EN-US"}[在与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[协商时，从]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[支持的加密算法列表中选择配置最靠前的算法作为协商结果。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改本配置对已经注册的]{style="font-family:宋体"}]{#struct_0_49241_76394_1525464766}[VAM Client]{lang="EN-US"}[没有影响，新注册的]{style="font-family:宋体"}[VAM ]{lang="EN-US"}[Client]{lang="EN-US"}[将采用修改后的加密算法进行协商。]{style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_787112173}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_34907850}[配置在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中按照优先级由高到低的顺序使用]{style="font-family:
宋体"}[AES-CBC-128]{lang="EN-US"}[和]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}[加密算法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1797151102}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] encryption-algorithm aes-cbc-128 3des-cbc ]{lang="EN-US"}
:::

::: {#1376722660 .myid}
[]{#_Toc404787377}[]{#struct_0_49241_76394_x1984485137}[]{#_Toc375152377}[]{#_Toc375152378}

**ADVPN \-- VAM Server配置命令 \-- hub-group**

------------------------------------------------------------------------

[**[hub-group]{lang="EN-US"}**]{#struct_0_49241_76394_971647464}[命令用来创建]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组，并进入]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组视图。如果]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组已经存在，则直接进入该]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[**[undo hub-group]{lang="EN-US"}**]{#struct_0_49241_76394_83227824}[命令用来删除指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x575533537}

[**[hub-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_49241_76394_1888253691}

[**[undo hub-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_49241_76394_27525904}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x724364042}

[[不存在]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1019752102}[组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x568058994}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1266910336}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x54915968}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1008784843}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1743213458}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1628622721}

[*[group-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1790829359}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_2055516710}

[[在大规模组网情况下，将]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_971581928}[域划分为多个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组可以方便管理。创建]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组后，可以按照]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的私网地址网段或地址范围，将]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[划分到不同的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组中，并为每个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组指定一个或多个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[当]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x555527191}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册时，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[根据]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的私网地址将]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[划分到对应的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组中：]{style="font-family:宋体"}

[[(1)[      ]{style="font:7.0pt "}]{lang="EN-US"}[根据]{style="font-family:宋体"}]{#struct_0_49241_76394_1056555571}[Hub]{lang="EN-US"}[组名称字典序依次匹配各]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内配置的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[(2)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果匹配上，则]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x964567710}[为]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[并被划分到该]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组；如果]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}[不是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，再根据]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组名称字典序依次匹配各]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组内配置的]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[私网地址范围。]{lang="EN-US" style="font-family:宋体"}

[[(3)[      ]{style="font:7.0pt "}]{lang="EN-US"}[如果匹配上，则]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x227192477}[为]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[poke]{lang="EN-US"}[，]{style="font-family:宋体"}[并被划分到该]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[；否则，]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[既]{style="font-family:宋体"}[不是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[也不是]{lang="EN-US" style="font-family:宋体"}[S]{lang="EN-US"}[poke]{lang="EN-US"}[，注册失败。]{lang="EN-US" style="font-family:宋体"}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_995813894}[只向]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[下发其所属的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[信息。]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[只与本]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[建立永久]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1815537622}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x2138605285}[在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[内创建]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_114182627}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\]]{lang="EN-US"}
:::

::: {#-652071768 .myid}
[]{#_Toc151282205}[]{#_Toc404787378}[]{#struct_0_49241_76394_654214961}[]{#_Toc375152380}[]{#_Toc375152381}

**ADVPN \-- VAM Server配置命令 \-- hub ipv6 private-address**

------------------------------------------------------------------------

[**[hub ipv6 private-address]{lang="EN-US"}**]{#struct_0_49241_76394_1370701667}[命令用来添加]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[undo hub ipv6 private-address]{lang="EN-US"}**]{#struct_0_49241_76394_x21446639}[命令用来删除]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x31999014}

[**[hub]{lang="EN-US"}**[ **ipv6 private-address**]{lang="EN-US"}[ *private-ipv6-address* \[ **public-address** { *public-ip-address* \| *public-ipv6-address* } \[ **advpn-port** *port-number* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_230150910}

[**[undo]{lang="EN-US"}**[ **hub** **ipv6** **private-address**]{lang="EN-US"}[ *private-ipv6-address*]{lang="EN-US"}]{#struct_0_49241_76394_971516392}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2040740546}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1197639368}[组内没有配置]{style="font-family:宋体"}[Hub IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1493195515}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_2082780768}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x78877992}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_404624589}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1444622019}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1127210054}

[*[private-ipv6-addres]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_49241_76394_543700005}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址，该地址必须是全球单播地址。]{style="font-family:宋体"}

[**[public-address]{lang="EN-US"}**]{#struct_0_49241_76394_1774912530}[：指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的公网地址。如果未指定本参数，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[使用该]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的公网地址。]{style="font-family:宋体"}

[*[public-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x226091754}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网地址，该地址必须是单播地址。]{style="font-family:宋体"}

[*[public-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_1733326090}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[公网地址，该地址必须是]{style="font-family:宋体"}[全球单播地址。]{style="font-family:宋体"}

[**[advpn-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_49241_76394_x277140482}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[使用该]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_582943220}

[[一般情况下，不需要指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x895742826}[的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号。只有当]{style="font-family:宋体"}[Hub]{lang="EN-US"}[要穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}[时，由于]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号是经过]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换前的，需要在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关上为]{style="font-family:宋体"}[Hub]{lang="EN-US"}[配置一个固定的地址和端口号的转换关系。此时，需要指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关上配置的转换后的地址和端口号。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_971450856}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_49241_76394_x182466689}[Hub]{lang="EN-US"}[组内可以配置多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址不同的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_49241_76394_x1452528088}[IPv6]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[已经存在，新配置将覆盖原有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1821869270}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1126617940}[向]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[中添加]{style="font-family:宋体"}[Hub]{lang="EN-US"}[，其]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址为]{style="font-family:宋体"}[1000::1:0:0:1]{lang="EN-US"}[，公网地址为]{style="font-family:宋体"}[2001::1]{lang="EN-US"}[，]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1227241924}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] hub ipv6 private-address 1000::1:0:0:1 public-address 2001::1 advpn-port 8000]{lang="EN-US"}
:::

::: {#1221697046 .myid}
[]{#_Toc404787379}[]{#struct_0_49241_76394_1899847669}[]{#_Toc375152383}[]{#_Toc375152384}[]{#_Toc375152385}[]{#_Toc375152386}[]{#_Toc375152387}[]{#_Toc375152388}[]{#_Toc375152389}[]{#_Toc375152390}

**ADVPN \-- VAM Server配置命令 \-- hub private-address**

------------------------------------------------------------------------

[**[hub private-address]{lang="EN-US"}**]{#struct_0_49241_76394_x256914362}[命令用来添加]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[undo hub private-address]{lang="EN-US"}**]{#struct_0_49241_76394_1247682684}[命令用来删除]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组内的]{style="font-family:宋体"}[Hub IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1992336794}

[**[hub]{lang="EN-US"}**[ **private-address**]{lang="EN-US"}[ *private-ip-address* \[ **public-address** { *public-ip-address* \| *public-ipv6-address* } \[ **advpn-port** *port-number* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_1633925352}

[**[undo]{lang="EN-US"}**[ **hub** **private-address**]{lang="EN-US"}[ *private-ip-address*]{lang="EN-US"}]{#struct_0_49241_76394_1918422255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_904600422}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_2041810676}[组内没有配置]{style="font-family:宋体"}[Hub IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_971385320}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1179305443}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_719164151}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1957050011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x574526208}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1233273343}

[*[private-ip-addres]{lang="EN-US"}*[s]{lang="EN-US"}]{#struct_0_49241_76394_x90679531}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址，该地址必须是单播地址。]{style="font-family:宋体"}

[**[public-address]{lang="EN-US"}**]{#struct_0_49241_76394_x252626803}[：指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的公网地址。如果未指定本参数，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[使用该]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的公网地址。]{style="font-family:宋体"}

[*[public-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x399755479}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网地址，该地址必须是单播地址。]{style="font-family:宋体"}

[*[public-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x315587560}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[公网地址，该地址必须是]{style="font-family:宋体"}[全球单播地址。]{style="font-family:宋体"}

[**[advpn-port]{lang="EN-US"}***[ port-number]{lang="EN-US"}*]{#struct_0_49241_76394_x1431812325}[：]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。如果未指定本参数，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[使用该]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2061749955}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一般情况下，不需要指定]{style="font-family:宋体"}]{#struct_0_49241_76394_x13534825}[Hub]{lang="EN-US"}[的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号。只有当]{style="font-family:宋体"}[Hub]{lang="EN-US"}[要穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}[时，由于]{style="font-family:宋体"}[Hub]{lang="EN-US"}[注册的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号是经过]{style="font-family:宋体"}[NAT]{lang="EN-US"}[转换前的，需要在]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关上为]{style="font-family:宋体"}[Hub]{lang="EN-US"}[配置一个固定的地址和端口号的转换关系。此时，需要指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[的公网地址和]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[NAT]{lang="EN-US"}[网关上配置的转换后的地址和端口号。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_49241_76394_x1982232817}[Hub]{lang="EN-US"}[组内可以配置多个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址不同的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定]{style="font-family:宋体"}]{#struct_0_49241_76394_971319784}[IPv4]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[已经存在，新配置将覆盖原有配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1911122004}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_149832433}[向]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[中添加]{style="font-family:宋体"}[Hub]{lang="EN-US"}[，其]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[，公网地址为]{style="font-family:宋体"}[123.0.0.1]{lang="EN-US"}[，]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[8000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_113191743}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] hub private-address 10.1.1.1 public-address 123.0.0.1 advpn-port 8000]{lang="EN-US"}
:::

::: {#809257258 .myid}
[]{#_Toc404787380}[]{#struct_0_49241_76394_683718178}[]{#_Toc316630023}[]{#_Toc151287004}[]{#_Toc151286460}[]{#_Toc151282206}[]{#_Toc375152392}[]{#_Toc375152393}[]{#_Toc375152394}[]{#_Toc375152395}[]{#_Toc375152396}[]{#_Toc375152397}[]{#_Toc375152398}[]{#_Toc375152399}

**ADVPN \-- VAM Server配置命令 \-- keepalive**

------------------------------------------------------------------------

[**[keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_659849890}[命令用来配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔和重发次数。]{style="font-family:宋体"}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_x881879701}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1359538895}

[**[keepalive interval]{lang="EN-US"}***[ time-interval]{lang="EN-US"}***[ retry ]{lang="EN-US"}***[retry-times]{lang="EN-US"}*]{#struct_0_49241_76394_x1766940498}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_737199893}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_391149461}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x505229422}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，重发次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x161871312}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x56453534}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_971254248}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1550960277}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1496601952}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1437162114}

[**[interval]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_1948606125}[：]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[retry ]{lang="EN-US"}***[retry-times]{lang="EN-US"}*]{#struct_0_49241_76394_x572422160}[：]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的重发次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1105138758}

[[配置的时间间隔和重发次数值由]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_99637945}[在注册响应报文中下发给]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[，同一个]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文参数都是相同的。但是，如果]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[改变]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文参数，则修改后的参数只对新注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[生效，已经注册的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[不受影响。]{style="font-family:宋体"}

[]{#_Toc151282212}[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_17831778}[和]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[之间通过]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文保持联系。]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[按照]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[指定的时间间隔向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[收到]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文后回复响应报文。当]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的重发次数达到指定的值仍没有收到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的响应时，]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[认为与]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的连接中断，不再发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文。当]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[在时间间隔×重发次数的时间内没有收到]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，则认为与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的连接中断，会删除该]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的信息并将其下线。]{style="font-family:宋体"}

[[需要注意的是，如果]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_705676679}[与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[间存在配置了动态]{style="font-family:宋体"}[NAT]{lang="EN-US"}[的设备，则]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送时间间隔应小于]{style="font-family:宋体"}[NAT]{lang="EN-US"}[表项的老化时间，从而保证]{style="font-family:宋体"}[NAT]{lang="EN-US"}[表项不会老化。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_978341661}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x332562996}[配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒，重发次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1926968397}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] keepalive interval 30 retry 5]{lang="EN-US"}
:::

::: {#-1288098765 .myid}
[]{#_Toc404787381}[]{#struct_0_49241_76394_x420359448}[]{#_Toc185927308}[]{#_Toc123026768}[]{#_Toc151282208}[]{#_Toc375152401}[]{#_Toc375152402}

**ADVPN \-- VAM Server配置命令 \-- pre-shared-key (ADVPN domain view)**

------------------------------------------------------------------------

[**[pre-shared-key]{lang="EN-US"}**]{#struct_0_49241_76394_972237288}[命令用来配置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的预共享密钥。]{style="font-family:宋体"}

[**[undo pre-shared-key]{lang="EN-US"}**]{#struct_0_49241_76394_x1582810296}[命令用来删除配置的预共享密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x583492003}

[**[pre-shared-key ]{lang="EN-US"}**[{ **cipher** *cipher-string* \| **simple** *simple-string* }]{lang="EN-US"}]{#struct_0_49241_76394_1380998067}

[**[undo]{lang="EN-US"}**[ **pre-shared-key**]{lang="EN-US"}]{#struct_0_49241_76394_1278005621}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x380136742}

[[未配置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x294834791}[的预共享密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_164559132}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_535541711}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1189602387}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_865504770}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2023223716}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_980580217}

[**[cipher]{lang="EN-US"}***[ cipher-string]{lang="EN-US"}*]{#struct_0_49241_76394_2066241865}[：以密文方式设置预共享密钥。]{style="font-family:宋体"}*[cipher-string]{lang="EN-US"}*[为密文预共享密钥，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}***[ simple-string]{lang="EN-US"}*]{#struct_0_49241_76394_601471902}[：以明文方式设置预共享密钥。]{style="font-family:宋体"}*[simple-string]{lang="EN-US"}*[为明文预共享密钥，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的明文字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_972171752}

[[预共享密钥是]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_2070666505}[用来和]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[建立安全通道的公共密钥材料。在连接初始化阶段预共享密钥用来生成验证和加密连接请求、连接响应报文的初始密钥；如果选择对后续的报文进行加密和验证，则预共享密钥还用来生成验证和加密后续报文的连接密钥。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_665642090}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的预共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_49241_76394_1379468967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个]{lang="EN-US" style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_583438249}[域内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[和]{style="font-family:宋体"}[VAM ]{lang="EN-US"}[Server]{lang="EN-US"}[上配置的预共享密钥必须一致。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x839848599}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_402819062}[以明文方式配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[的预共享密钥为]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x591651202}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] pre-shared-key simple 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1257353675}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pre-shared-key]{lang="EN-US"}**[ (VAM client view)]{lang="EN-US"}]{#struct_0_49241_76394_883869538}
:::

::: {#-168641636 .myid}
[]{#_Toc151282209}[]{#_Toc404787382}[]{#struct_0_49241_76394_x702486685}

**ADVPN \-- VAM Server配置命令 \-- retry interval**

------------------------------------------------------------------------

[**[retry interval]{lang="EN-US"}**]{#struct_0_49241_76394_x118105441}[命令用来设置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[重发请求报文的时间间隔。]{style="font-family:宋体"}

[**[undo retry interval]{lang="EN-US"}**]{#struct_0_49241_76394_782249959}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_322188000}

[**[retry interval]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_x206951946}

[**[undo retry interval]{lang="EN-US"}**]{#struct_0_49241_76394_971712997}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1481551025}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_695561338}[重发请求报文的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_247048333}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x4153944}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_461817419}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_2112995893}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1139714781}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x234270280}

[*[time-interval]{lang="EN-US"}*]{#struct_0_49241_76394_480305641}[：]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[重发请求报文的时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1369049058}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_6074320}[向]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送请求报文后，如果在指定的时间间隔内没有收到响应报文，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[将重新发送请求报文，直到收到响应报文或者]{style="font-family:宋体"}[VAM Client Keepalive]{lang="EN-US"}[超时（即]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[在]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送时间间隔×重发次数的时间内没有收到]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文）为止。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x541645726}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1164686268}[设置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[向]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[重发请求报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_971647461}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] retry interval 20]{lang="EN-US"}
:::

::: {#-1562655142 .myid}
[]{#_Toc404787383}[]{#struct_0_49241_76394_83227829}[]{#_Toc375152405}[]{#_Toc375152406}

**ADVPN \-- VAM Server配置命令 \-- reset vam server address-map**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **vam** **server** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_998444575}[命令用来清除注册到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_2010045336}

[**[reset]{lang="EN-US"}**[ **vam** **server** **address-map** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ip-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_x1992468872}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x155022600}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_1292175471}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2031438238}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_150102443}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1305409112}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1168194776}

[**[advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1001773540}[：清除指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中注册的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上注册的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x2126652226}[：清除]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的映射信息。]{style="font-family:宋体"}*[private-ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。如果未指定本参数，则清除指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域或所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_1361486273}

[[执行本命令除了会清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1402269977}[上注册的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息外，还会清除该]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址相关的私网信息，并向注册该]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送错误通知报文，要求]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1612185587}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_971581925}[清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上注册的所有]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server address-map]{lang="EN-US"}]{#struct_0_49241_76394_x555527178}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1055965745}[清除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中注册的所有]{style="font-family:
宋体"}[IPv4]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server address-map advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_x451027737}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_339525993}[清除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[10.0.0.1]{lang="EN-US"}[的地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server address-map advpn-domain 1 private-address 10.0.0.1]{lang="EN-US"}]{#struct_0_49241_76394_1624979063}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1919136719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **vam** **server** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_1512099346}
:::

::: {#233344949 .myid}
[]{#_Toc404787384}[]{#struct_0_49241_76394_857683301}

**ADVPN \-- VAM Server配置命令 \-- reset vam server ipv6 address-map**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **vam** **server** **ipv6** **address-map**]{lang="EN-US"}]{#struct_0_49241_76394_x1347435471}[命令用来清除注册到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1231720413}

[**[reset]{lang="EN-US"}**[ **vam** **server** **ipv6** **address-map** \[ **advpn-domain** *domain-name* \[ **private-address** *private-ipv6-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_1677275475}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x86535396}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_442924730}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_687450756}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_971516389}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_297911619}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x761601074}

[**[advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_1482200611}[：清除指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中注册的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上注册的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[**[private-address ]{lang="EN-US"}***[private-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_1608677299}[：]{style="font-family:宋体"}[清除指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的映射信息。]{style="font-family:宋体"}*[private-ipv6-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。如果未指定本参数，则清除指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域或所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域中的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x347373183}

[[执行本命令除了会清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x649814950}[上注册的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息外，还会清除该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址相关的私网信息，并向注册该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[发送错误通知报文，要求]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[下线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1805139810}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1467597505}[清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上注册的所有]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server ipv6 address-map]{lang="EN-US"}]{#struct_0_49241_76394_433678782}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x219503958}[清除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中注册的所有]{style="font-family:
宋体"}[IPv6]{lang="EN-US"}[私网地址和公网地址映射信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server ipv6 address-map advpn-domain 1]{lang="EN-US"}]{#struct_0_49241_76394_x1900317518}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x32747174}[清除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[中私网地址]{style="font-family:
宋体"}[1000::1:0:0:1]{lang="EN-US"}[的地址映射信息。]{style="font-family:
宋体"}

[[\<Sysname\> reset vam server ipv6 address-map advpn-domain 1 private-address 1000::1:0:0:1]{lang="EN-US"}]{#struct_0_49241_76394_971450853}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x182466686}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ vam server ]{lang="EN-US"}**]{#struct_0_49241_76394_x1451676120}**[ipv6 ]{lang="EN-US"}[address-map]{lang="EN-US"}**
:::

::: {#-105279259 .myid}
[]{#_Toc404787385}[]{#struct_0_49241_76394_x56480015}

**ADVPN \-- VAM Server配置命令 \-- reset vam server statistics**

------------------------------------------------------------------------

[**[reset ]{lang="EN-US"}[vam server statistics]{lang="EN-US"}**]{#struct_0_49241_76394_983376324}[命令用来清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_65185633}

[**[reset]{lang="EN-US"}**[ **vam** **server** **statistics** \[ **advpn-domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_x192506195}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1717432507}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_457679962}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1741093133}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1624222742}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1697791002}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1667343089}

[**[advpn-domain]{lang="EN-US"}***[ domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_x628510281}[：]{style="font-family:宋体"}[清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符为]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则清除]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x238878400}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1320060911}[清除名为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server statistics advpn-domain abc]{lang="EN-US"}]{#struct_0_49241_76394_971385317}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x777009686}[清除所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam server statistics]{lang="EN-US"}]{#struct_0_49241_76394_923592735}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_101176896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ vam server statistics]{lang="EN-US"}**]{#struct_0_49241_76394_x1985369694}
:::

::: {#-379829949 .myid}
[]{#_Toc404787386}[]{#struct_0_49241_76394_777811131}

**ADVPN \-- VAM Server配置命令 \-- server enable**

------------------------------------------------------------------------

[**[server enable]{lang="EN-US"}**]{#struct_0_49241_76394_x102914363}[命令用来启动指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo server enable]{lang="EN-US"}**]{#struct_0_49241_76394_257868845}[命令用来关闭指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x323648526}

[**[server enable]{lang="EN-US"}**]{#struct_0_49241_76394_x1337743760}

[**[undo server enable]{lang="EN-US"}**]{#struct_0_49241_76394_277779994}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_1273433847}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2022353178}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1364165770}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2019517769}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_971319781}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1911122009}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_553116960}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1980222412}

[[除了执行本命令外，还可以在系统视图下通过]{style="font-family:宋体"}**[vam]{lang="EN-US"}**[ **server** **enable**]{lang="EN-US"}]{#struct_0_49241_76394_x1210581458}[命令来启动所有或指定]{style="font-family:
宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1922647905}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_2094317315}[启动]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x58671069}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] server enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x836418285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam server enable]{lang="EN-US"}**]{#struct_0_49241_76394_x1775270029}
:::

::: {#332291415 .myid}
[]{#_Toc404787387}[]{#struct_0_49241_76394_605166726}

**ADVPN \-- VAM Server配置命令 \-- shortcut interest**

------------------------------------------------------------------------

[**[shortcut interest]{lang="EN-US"}**]{#struct_0_49241_76394_x578234845}[命令用来配置跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shortcut interest**]{lang="EN-US"}]{#struct_0_49241_76394_375313476}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_611076605}

[**[shortcut interest]{lang="EN-US"}**[ { **acl**]{lang="EN-US"}[ { *acl-number* \| **name** *acl-name* } \| **all** }]{lang="EN-US"}]{#struct_0_49241_76394_971254245}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}**[shortcut interest]{lang="EN-US"}**]{#struct_0_49241_76394_x1550960274}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_69481989}

[[没有配置跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x172566517}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则，不允许跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_733068803}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_459448136}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1734946920}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1287761251}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1500572593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x623101417}

[**[acl]{lang="EN-US"}**]{#struct_0_49241_76394_x1005816466}[：表示只允许匹配指定]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间建立跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_49241_76394_x374533743}[：]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_49241_76394_1238857471}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_49241_76394_1362867783}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *acl-name*]{lang="EN-US"}]{#struct_0_49241_76394_x1889238263}[：指定]{style="font-family:宋体"}[IPv4 ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_49241_76394_972237285}[：表示所有跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间均可建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1582810301}

[[如果配置了跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1788571167}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则，则在]{style="font-family:宋体"}[Hub]{lang="EN-US"}[上线后，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[将指定的规则下发到]{style="font-family:宋体"}[Hub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则指定为]{style="font-family:宋体"}]{#struct_0_49241_76394_x767628441}**[all]{lang="EN-US"}**[，则]{style="font-family:宋体"}[Hub]{lang="EN-US"}[在转发任意跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[Spoke-Spoke]{lang="EN-US"}[私网数据报文的同时，会向相应]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则指定为匹配]{style="font-family:宋体"}]{#struct_0_49241_76394_x1568244559}[ACL]{lang="EN-US"}[，则]{style="font-family:宋体"}[Hub]{lang="EN-US"}[在转发跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[私网数据报文的同时，会将报文与指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行匹配。如果匹配成功，]{style="font-family:宋体"}[Hub]{lang="EN-US"}[会向相应的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文；否则，不会发送重定向报文。]{style="font-family:宋体"}

[[Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x623621627}[收到重定向报文后，将被重定向的数据报文的目的地址发送给]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[，向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[查询连接该目的地址所在私网网段的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[节点的信息，并与该]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[建立直连隧道。]{style="font-family:宋体"}

[[跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1384090062}[组]{style="font-family:宋体"}[Spoke-Spoke]{lang="EN-US"}[直连隧道建立前，数据报文仍由]{style="font-family:宋体"}[Hub]{lang="EN-US"}[进行转发。直连隧道建立后，数据报文将直接发送到直连路由下一跳所对应的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[，而不再经过]{style="font-family:宋体"}[Hub]{lang="EN-US"}[中转。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_x1325388981}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_49241_76394_1868047457}[ACL]{lang="EN-US"}[不存在，则配置不生效。任何私网数据报文都不会触发]{style="font-family:宋体"}[Hub]{lang="EN-US"}[向]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_49241_76394_1655079948}[IPv4]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，本命令仅支持匹配源地址信息的规则；对于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，仅支持匹配协议类型、源地址、目的地址、源端口和目的端口信息的规则，并且不支持排除某个源]{style="font-family:宋体"}[/]{lang="EN-US"}[目的端口号的规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本命令指定的]{style="font-family:宋体"}]{#struct_0_49241_76394_x850045615}[ACL]{lang="EN-US"}[中包含不支持的规则，则该条]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则将不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1224103267}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1104051470}[配置如果]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间的报文匹配]{style="font-family:宋体"}[ACL 3000]{lang="EN-US"}[，则允许建立跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1036085110}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] shortcut interest acl 3000]{lang="EN-US"}
:::

::: {#-1133845384 .myid}
[]{#_Toc404787388}[]{#struct_0_49241_76394_972171749}[]{#_Toc375152412}[]{#_Toc375152413}[]{#_Toc375152414}

**ADVPN \-- VAM Server配置命令 \-- shortcut ipv6 interest**

------------------------------------------------------------------------

[**[shortcut ipv6 interest]{lang="EN-US"}**]{#struct_0_49241_76394_114351362}[命令用来配置跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **shortcut ipv6 interest**]{lang="EN-US"}]{#struct_0_49241_76394_1675021974}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1494957966}

[**[shortcut]{lang="EN-US"}**[ **ipv6**]{lang="EN-US"}[ **interest** { **acl** { *ipv6-acl-number* \| **name** *ipv6-acl-name* } \| **all** }]{lang="EN-US"}]{#struct_0_49241_76394_1728450355}

[**[undo]{lang="EN-US"}**[ **shortcut** **ipv6** **interest**]{lang="EN-US"}]{#struct_0_49241_76394_1878733656}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x902518458}

[[没有配置跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x397896160}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则，不允许跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x944828451}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_836417189}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x10821098}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_213905592}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_971712998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1481551022}

[**[acl]{lang="EN-US"}**]{#struct_0_49241_76394_x870522603}[：表示只允许匹配指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间建立跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[*[ipv6-acl-number]{lang="EN-US"}*]{#struct_0_49241_76394_418507670}[：]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的编号，取值范围及其代表的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[类型如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2000]{lang="EN-US"}]{#struct_0_49241_76394_x1214887003}[～]{lang="EN-US" style="font-family:宋体"}[2999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[基本]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3000]{lang="EN-US"}]{#struct_0_49241_76394_x1346990256}[～]{lang="EN-US" style="font-family:宋体"}[3999]{lang="EN-US"}[：表示]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{lang="EN-US" style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *ipv6-acl-name*]{lang="EN-US"}]{#struct_0_49241_76394_2111723807}[：指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[的名称。]{style="font-family:宋体"}*[ipv6-acl-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，必须以英文字母]{style="font-family:宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[或]{style="font-family:
宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[开头。为避免混淆，]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的名称不允许使用英文单词]{style="font-family:宋体"}[all]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_49241_76394_210934452}[：表示所有跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间均可建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_640674100}

[[配置了跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1588168199}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则，在]{style="font-family:宋体"}[Hub]{lang="EN-US"}[上线后，]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[通过数据流信息报文将指定的规则下发到]{style="font-family:宋体"}[Hub]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则指定为]{style="font-family:宋体"}]{#struct_0_49241_76394_102805166}**[all]{lang="EN-US"}**[，则]{style="font-family:宋体"}[Hub]{lang="EN-US"}[在转发任意跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv6 ]{lang="EN-US"}[Spoke-Spoke]{lang="EN-US"}[私网数据报文的同时，会向相应]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果规则指定为匹配]{style="font-family:宋体"}]{#struct_0_49241_76394_2145888385}[ACL]{lang="EN-US"}[，则]{style="font-family:宋体"}[Hub]{lang="EN-US"}[在转发跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[私网数据报文的同时，会将报文与指定的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[进行匹配。如果匹配成功，]{style="font-family:宋体"}[Hub]{lang="EN-US"}[会向相应的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文；否则，不会发送重定向报文。]{style="font-family:宋体"}

[[Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x1617372371}[收到重定向报文后，将被重定向的数据报文的目的地址发送给]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[，向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[查询连接该目的地址所在私网网段的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[节点的信息，并与该]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[建立直连隧道。]{style="font-family:宋体"}

[[跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_436996787}[组]{style="font-family:宋体"}[Spoke-Spoke]{lang="EN-US"}[直连隧道建立前，数据报文仍由]{style="font-family:宋体"}[Hub]{lang="EN-US"}[进行转发。直连隧道建立后，数据报文将直接发送到直连路由下一跳所对应的]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[，而不再经过]{style="font-family:宋体"}[Hub]{lang="EN-US"}[中转。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_971647462}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定的]{style="font-family:宋体"}]{#struct_0_49241_76394_83227830}[ACL]{lang="EN-US"}[不存在，则配置不生效。任何私网数据报文都不会触发]{style="font-family:宋体"}[Hub]{lang="EN-US"}[向]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[发送重定向报文。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_49241_76394_x1376943430}[IPv6]{lang="EN-US"}[基本]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，本命令仅支持匹配源地址信息的规则；对于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL]{lang="EN-US"}[，仅支持匹配协议类型、源地址、目的地址、源端口和目的端口信息的规则，并且不支持排除某个源]{style="font-family:宋体"}[/]{lang="EN-US"}[目的端口号的规则。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本命令指定的]{style="font-family:宋体"}]{#struct_0_49241_76394_x807204135}[ACL]{lang="EN-US"}[中包含不支持的规则，则该条]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则将不生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1524482857}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1177936754}[配置如果]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[之间的报文匹配]{style="font-family:宋体"}[IPv6 ACL 3000]{lang="EN-US"}[，则允许建立跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组的]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_704469070}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] shortcut ipv6 interest acl 3000]{lang="EN-US"}
:::

::: {#24578254 .myid}
[]{#_Toc404787389}[]{#struct_0_49241_76394_2128161066}[]{#_Toc375152416}[]{#_Toc375152417}[]{#_Toc375152418}

**ADVPN \-- VAM Server配置命令 \-- spoke ipv6 private-address**

------------------------------------------------------------------------

[**[spoke ipv6 private-address]{lang="EN-US"}**]{#struct_0_49241_76394_x1206150253}[命令用来配置]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[**[undo spoke ipv6 private-address]{lang="EN-US"}**]{#struct_0_49241_76394_1756109353}[命令用来删除]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_707745073}

[**[spoke]{lang="EN-US"}**[ **ipv6 private-address** ]{lang="EN-US"}[{ **network** *prefix prefix-length* \| **range** *start-ipv6-address end-ipv6-address* }]{lang="EN-US"}]{#struct_0_49241_76394_x1996416358}

[**[undo]{lang="EN-US"}**[ **spoke** **ipv6** **private-address** ]{lang="EN-US"}[{ **network** *prefix prefix-length* \| **range** *start-ipv6-address end-ipv6-address* }]{lang="EN-US"}]{#struct_0_49241_76394_x1336454526}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x798319048}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_971581926}[组内没有配置]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x555527177}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1056948785}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_535152842}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_209434952}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x440258024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1032997502}

[**[network]{lang="EN-US"}***[ prefix prefix-length]{lang="EN-US"}*]{#struct_0_49241_76394_227287881}[：指定子网网段形式的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}*[prefix]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀，]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[range]{lang="EN-US"}***[ start-ipv6-address end-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x1854307673}[：指定地址段形式的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}*[start-ipv6-address]{lang="EN-US"}*[为地址段的起始]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-ipv6-address]{lang="EN-US"}*[为地址段的结束]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2086593215}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_794275733}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围可以指定为地址段形式或子网网段形式。以子网网段形式指定的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围，系统会自动将其转换为地址段形式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_49241_76394_1397154435}[Hub]{lang="EN-US"}[组可以配置多个]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围，将按照地址从低到高的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除的私网地址范围必须和配置时的一致。]{style="font-family:宋体"}]{#struct_0_49241_76394_1816013561}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1275373402}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_280734149}[指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:
宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址范围为]{style="font-family:宋体"}[1000::/64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_971516390}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] spoke ipv6 private-address network 1000:: 64]{lang="EN-US"}
:::

::: {#-1873383622 .myid}
[]{#_Toc404787390}[]{#struct_0_49241_76394_x2040740548}[]{#_Toc375152420}[]{#_Toc375152421}[]{#_Toc375152422}[]{#_Toc375152423}[]{#_Toc375152424}[]{#_Toc375152425}[]{#_Toc375152426}[]{#_Toc375152427}

**ADVPN \-- VAM Server配置命令 \-- spoke private-address**

------------------------------------------------------------------------

[**[spoke private-address]{lang="EN-US"}**]{#struct_0_49241_76394_x747300674}[命令用来配置]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[**[undo spoke private-address]{lang="EN-US"}**]{#struct_0_49241_76394_x1308028667}[命令用来删除]{style="font-family:
宋体"}[Hub]{lang="EN-US"}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x641063891}

[**[spoke private-address ]{lang="EN-US"}**[{ **network** *ip-address* { *mask-length* \| *mask* } \| **range** *start-address end-address* }]{lang="EN-US"}]{#struct_0_49241_76394_x704668729}

[**[undo spoke private-address ]{lang="EN-US"}**[{ **network** *ip-address* { *mask-length* \| *mask* } \| **range** *start-address end-address* }]{lang="EN-US"}]{#struct_0_49241_76394_x1885366663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2086547645}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1621091180}[组内没有配置]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1389017366}

[[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1475335497}[组视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1300337396}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_644252119}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x362702306}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1887958371}

[**[network]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*[ { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_49241_76394_971450854}[：指定子网网段形式的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}*[ip-address]{lang="EN-US"}*[为子网网段]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址；]{style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为子网掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[；]{style="font-family:宋体"}*[mask]{lang="EN-US"}*[为子网掩码。]{style="font-family:宋体"}

[**[range]{lang="EN-US"}***[ start-address end-address]{lang="EN-US"}*]{#struct_0_49241_76394_x182466691}[：指定地址段形式的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围。]{style="font-family:宋体"}*[start-address]{lang="EN-US"}*[为地址段的起始]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[end-address]{lang="EN-US"}*[为地址段的结束]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1452003801}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x209607541}[组内]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围可以指定为地址段形式或子网网段形式。以子网网段形式指定的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围，系统会自动将其转换为地址段形式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}]{#struct_0_49241_76394_x2009444487}[Hub]{lang="EN-US"}[组可以配置多个]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围，将按照地址从低到高的顺序排列。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除的私网地址范围必须和配置时的一致。]{style="font-family:宋体"}]{#struct_0_49241_76394_408356327}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x66785796}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_887378434}[指定]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[1]{lang="EN-US"}[内]{style="font-family:
宋体"}[Spoke]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址范围为]{style="font-family:宋体"}[1.1.1.0/24]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1083842805}

[\[Sysname\] vam server advpn-domain 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\] hub-group 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1-hub-group-1\] spoke private-address network 1.1.1.0 255.255.255.0]{lang="EN-US"}
:::

::: {#-2028312158 .myid}
[]{#_Toc151282210}[]{#_Toc404787391}[]{#struct_0_49241_76394_359435572}[]{#_Toc375152429}[]{#_Toc375152430}[]{#_Toc375152431}[]{#_Toc375152432}[]{#_Toc375152433}[]{#_Toc375152434}[]{#_Toc375152435}[]{#_Toc375152436}[]{#_Toc349205200}[]{#_Toc349205201}[]{#_Toc349205202}[]{#_Toc349205203}[]{#_Toc349205204}[]{#_Toc349205205}[]{#_Toc349205206}[]{#_Toc349205207}[]{#_Toc349205208}[]{#_Toc349205209}[]{#_Toc349205210}[]{#_Toc349205211}[]{#_Toc349205212}[]{#_Toc349205213}[]{#_Toc349205214}[]{#_Toc349205215}[]{#_Toc349205216}[]{#_Toc349205217}[]{#_Toc349205218}[]{#_Toc349205219}[]{#_Toc349205220}[]{#_Toc349205221}[]{#_Toc349205222}[]{#_Toc349205223}[]{#_Toc349205224}[]{#_Toc349205225}[]{#_Toc349205226}[]{#_Toc349205227}[]{#_Toc349205228}[]{#_Toc349205229}[]{#_Toc349205230}[]{#_Toc349205231}[]{#_Toc349205232}[]{#_Toc349205233}[]{#_Toc349205234}[]{#_Toc349205235}[]{#_Toc349205236}[]{#_Toc349205237}[]{#_Toc349205238}[]{#_Toc349205239}[]{#_Toc349205240}[]{#_Toc349205241}[]{#_Toc349205242}[]{#_Toc349205243}

**ADVPN \-- VAM Server配置命令 \-- vam server advpn-domain**

------------------------------------------------------------------------

[**[vam server advpn-domain]{lang="SV"}**]{#struct_0_49241_76394_1379118492}[命令用来创建]{style="font-family:宋体"}[ADVPN]{lang="SV"}[域]{style="font-family:宋体"}[，并进入]{style="font-family:宋体"}[ADVPN]{lang="SV"}[域]{style="font-family:宋体"}[视图。如果]{style="font-family:宋体"}[ADVPN]{lang="SV"}[域]{style="font-family:宋体"}[已经存在，则直接进入该]{style="font-family:宋体"}[ADVPN]{lang="SV"}[域]{style="font-family:宋体"}[视图。]{style="font-family:宋体"}

[**[undo vam server advpn-domain]{lang="SV"}**]{#struct_0_49241_76394_617058313}[命令用来删除指定]{style="font-family:宋体"}[ADVPN]{lang="SV"}[域]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_453872469}

[**[vam server advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*[ \[ **id** *domain-id* \]]{lang="EN-US"}]{#struct_0_49241_76394_x2089079287}

[**[undo vam server advpn-domain]{lang="PT-BR"}**]{#struct_0_49241_76394_971385318}[ *domain-name*]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x777009701}

[[设备上不存在任何]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1414862809}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_752073826}

[[系统视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1350123926}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1256381762}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1932524203}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_2042524429}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_357459210}

[*[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_x864283105}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[id]{lang="EN-US"}**[ *domain-id*]{lang="EN-US"}]{#struct_0_49241_76394_1591443059}[：指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}*[domain-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x282002860}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_49241_76394_x558343474}[ADVPN]{lang="EN-US"}[域时必须指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[ID]{lang="EN-US"}[。若要进入已存在的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的视图，可以不指定其域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不同的]{style="font-family:宋体"}]{#struct_0_49241_76394_747541615}[ADVPN]{lang="EN-US"}[域必须使用不同的域]{style="font-family:宋体"}[ID]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_2094388794}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_971319782}[创建]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[，]{style="font-family:
宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1911122006}

[\[Sysname\] vam server advpn-domain 1 id 1]{lang="EN-US"}

[\[Sysname-vam-server-domain-1\]]{lang="EN-US"}
:::

::: {#1803007075 .myid}
[]{#_Toc404787392}[]{#struct_0_49241_76394_1312631847}[]{#_Toc375152438}[]{#_Toc375152439}[]{#_Toc375152440}[]{#_Toc375152441}[]{#_Toc375152442}[]{#_Toc375152443}

**ADVPN \-- VAM Server配置命令 \-- vam server enable**

------------------------------------------------------------------------

[**[vam server enable]{lang="EN-US"}**]{#struct_0_49241_76394_699633732}[命令用来启动所有或指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo vam server enable]{lang="EN-US"}**]{#struct_0_49241_76394_1266986786}[命令用来关闭所有或指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1930366543}

[**[vam]{lang="EN-US"}**[ **server** **enable** \[ **advpn-domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_1168911364}

[**[undo]{lang="EN-US"}**[ **vam** **server** **enable** \[ **advpn-domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_183355202}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1112080980}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1327307173}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1051257895}

[[系统视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x275857637}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1311094261}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1255760031}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_922519146}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_971254246}

[**[advpn-domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1550960271}[：启动指定]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}*[domain-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A]{lang="EN-US"}[～]{style="font-family:宋体"}[Z]{lang="EN-US"}[、]{style="font-family:
宋体"}[a]{lang="EN-US"}[～]{style="font-family:宋体"}[z]{lang="EN-US"}[、]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[9]{lang="EN-US"}[和"]{style="font-family:
宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则启动所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x333802538}

[[除了执行本命令外，还可以在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_763743310}[域视图下通过]{style="font-family:宋体"}**[server]{lang="EN-US"}**[ **enable**]{lang="EN-US"}[命令来启动相应]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_2028891979}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1438147847}[启动所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x657375538}

[\[Sysname\] vam server enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1795533629}[启动]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[VAM Server]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1239415354}

[\[Sysname\] vam server enable advpn-domain 1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x198718069}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server ]{lang="EN-US"}**]{#struct_0_49241_76394_x153779858}**[enable]{lang="EN-US"}**
:::

::: {#-1717272232 .myid}
[]{#_Toc404787393}[]{#struct_0_49241_76394_972237286}[]{#_Toc151282211}

**ADVPN \-- VAM Server配置命令 \-- vam server listen-port**

------------------------------------------------------------------------

[**[vam server listen-port]{lang="EN-US"}**]{#struct_0_49241_76394_x1582810302}[命令用来配置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的监听端口号。]{style="font-family:宋体"}

[**[undo vam server listen-port]{lang="PT-BR"}**]{#struct_0_49241_76394_1385286640}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_973365486}

[**[vam server listen-]{lang="EN-US"}[port]{lang="EN-US"}**[ *port-number* ]{lang="EN-US"}]{#struct_0_49241_76394_1316053006}

[**[undo vam server listen-port]{lang="EN-US"}**]{#struct_0_49241_76394_1615046484}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x708710830}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1740960129}[的监听端口号为]{style="font-family:宋体"}[18000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_570835632}

[[系统视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x971834308}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1357370735}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2058803913}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_130850590}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_832858702}

[*[port-number]{lang="EN-US"}*]{#struct_0_49241_76394_1766774923}[：]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[监听的端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_972171750}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_2070666507}[的监听端口号与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[上指定的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的端口号必须一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_665773162}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1775407595}[配置]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的监听端口号为]{style="font-family:宋体"}[10000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x221545582}

[\[Sysname\] vam server listen-port 10000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1399890800}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server primary]{lang="EN-US"}**]{#struct_0_49241_76394_x1936500827}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server secondary]{lang="EN-US"}**]{#struct_0_49241_76394_1939660569}
:::

::: {#943091498 .myid}
[]{#_Toc151282214}[]{#_Toc404787395}[]{#struct_0_49241_76394_x1335198188}

**ADVPN \-- VAM Client配置命令 \-- advpn-domain**

------------------------------------------------------------------------

[**[advpn-domain]{lang="EN-US"}**]{#struct_0_49241_76394_1892249483}[命令用来配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[所属的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo advpn-domain]{lang="EN-US"}**]{#struct_0_49241_76394_219430772}[命令用来删除]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[所属的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_495304742}

[**[advpn-domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_49241_76394_368173007}

[**[undo advpn-domain]{lang="EN-US"}**]{#struct_0_49241_76394_x1927057641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_568428474}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1447675625}[不属于任何]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1944345896}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1421875679}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1142608834}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_2070014057}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2059928841}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1515685824}

[*[domain-name]{lang="EN-US"}*]{#struct_0_49241_76394_190288103}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1537632386}

[[多个]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1356392467}[可以属于同一个]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_92677695}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x942664519}[配置]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[属于]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1312014557}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] advpn-domain 100]{lang="EN-US"}
:::

::: {#-42799141 .myid}
[]{#_Toc404787396}[]{#struct_0_49241_76394_680305605}[]{#_Toc375152448}[]{#_Toc375152449}

**ADVPN \-- VAM Client配置命令 \-- client enable**

------------------------------------------------------------------------

[**[client enable]{lang="EN-US"}**]{#struct_0_49241_76394_568362938}[命令用来启动指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo client enable]{lang="EN-US"}**]{#struct_0_49241_76394_x2009778450}[命令用来关闭指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1117463131}

[**[client enable]{lang="EN-US"}**]{#struct_0_49241_76394_2106469347}

[**[undo client enable]{lang="EN-US"}**]{#struct_0_49241_76394_1555378524}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x192689655}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x113701641}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x745972191}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_347678851}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1138915375}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1855815537}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x318317309}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2103228713}

[[还可以在系统视图下通过]{style="font-family:宋体"}**[vam client enable]{lang="EN-US"}**]{#struct_0_49241_76394_721548463}[命令来启动所有或指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1092533540}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_568297402}[启动]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x109037612}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] client enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_642403918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam client enable]{lang="EN-US"}**]{#struct_0_49241_76394_545796054}
:::

::: {#-1645225607 .myid}
[]{#_Toc404787397}[]{#struct_0_49241_76394_x1606413566}

**ADVPN \-- VAM Client配置命令 \-- display vam client fsm**

------------------------------------------------------------------------

[**[display vam client fsm]{lang="EN-US"}**]{#struct_0_49241_76394_x890630017}[命令用来显示]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x484563354}

[**[display]{lang="EN-US"}**[ **vam** **client** **fsm** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_1490866229}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x483508003}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1876320269}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x81374749}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1498826596}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x1428930334}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x589713995}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_154062968}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_568231866}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_1108787634}[：显示指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机信息。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x921140899}

[[需要注意的是，一些没有配置的命令参数，或者未能动态获取的信息将不会出现在本命令的显示信息中。]{style="font-family:宋体"}]{#struct_0_49241_76394_x1294466866}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1670165541}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_666931900}[显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam client fsm]{lang="EN-US"}]{#struct_0_49241_76394_568100794}

[Client name      : abc]{lang="EN-US"}

[Status           : Enabled]{lang="EN-US"}

[ADVPN domain name: 1]{lang="EN-US"}

[  Primary server: abc.com (28.1.1.23)]{lang="EN-US"}

[    Private address: 10.0.0.12]{lang="EN-US"}

[    Interface      : Tunnel1]{lang="EN-US"}

[      Current state           : Online (active)]{lang="EN-US"}

[      Client type             : Hub]{lang="EN-US"}

[      Holding time            : 9H 20M 30S]{lang="EN-US"}

[      Encryption algorithm    : AES-CBC-128]{lang="EN-US"}

[      Authentication algorithm: SHA1]{lang="EN-US"}

[      Keepalive               : 30 seconds, 3 times]{lang="EN-US"}

[      Number of hubs          : 1]{lang="EN-US"}

[    Private address: 1000::22]{lang="EN-US"}

[    Interface      : Tunnel2]{lang="EN-US"}

[      Current state           : Online (active)]{lang="EN-US"}

[      Client type             : Spoke]{lang="EN-US"}

[      Holding time            : 9H 20M 30S]{lang="EN-US"}

[      Encryption algorithm    : AES-CBC-128]{lang="EN-US"}

[      Authentication algorithm: SHA1]{lang="EN-US"}

[      Keepalive               : 30 seconds, 3 times]{lang="EN-US"}

[      Number of hubs          : 1]{lang="EN-US"}

[  Secondary server: 2811::24]{lang="EN-US"}

[    Private address: 10.0.0.12]{lang="EN-US"}

[    Interface      : Tunnel1]{lang="EN-US"}

[      Current state           : Offline]{lang="EN-US"}

[      Client type             : Unknown]{lang="EN-US"}

[      Holding time            : 0H 0M 0S]{lang="EN-US"}

[      Encryption algorithm    : AES-CBC-128]{lang="EN-US"}

[      Authentication algorithm: SHA1]{lang="EN-US"}

[      Keepalive               : 0 seconds, 0 times]{lang="EN-US"}

[      Number of hubs          : 0]{lang="EN-US"}

[    Private address: 1000::22]{lang="EN-US"}

[    Interface      : Tunnel2]{lang="EN-US"}

[      Current state           : Offline]{lang="EN-US"}

[      Client type             : Unknown]{lang="EN-US"}

[      Holding time            : 0H 0M 0S]{lang="EN-US"}

[      Encryption algorithm    : AES-CBC-128]{lang="EN-US"}

[      Authentication algorithm: SHA1]{lang="EN-US"}

[      Keepalive               : 0 seconds, 0 times]{lang="EN-US"}

[      Number of hubs          : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : hub]{lang="EN-US"}

[Status           : Enabled]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[  Primary server: 202.159.36.24 ]{lang="EN-US"}

[    Private address: 10.0.0.12]{lang="EN-US"}

[    Interface      : Tunnel20]{lang="EN-US"}

[      Current state           : Online (active)]{lang="EN-US"}

[      Client type             : Hub]{lang="EN-US"}

[      Holding time            : 0H 0M 47S]{lang="EN-US"}

[      Encryption algorithm    : AES-CBC-128]{lang="EN-US"}

[      Authentication algorithm: SHA1]{lang="EN-US"}

[      Keepalive               : 30 seconds, 3 times]{lang="EN-US"}

[      Number of hubs          : 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : spoke]{lang="EN-US"}

[Status           : Disabled]{lang="EN-US"}

[ADVPN domain name:]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display vam client fsm]{lang="EN-US"}]{#struct_0_49241_76394_x1909865414}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_103565312}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x927369927}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x977790356}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_x916716897}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1483324415}[的名称]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_49241_76394_1565739522}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_228401963}[的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_49241_76394_860633783}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_49241_76394_x2099602525}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_2053986286}

[[该]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_568035258}[所在的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域名]{style="font-family:宋体"}

[[Primary server]{lang="EN-US"}]{#struct_0_49241_76394_1999404386}

[[主]{style="font-family:宋体"}]{#struct_0_49241_76394_1858284189}[VAM Server]{lang="PT-BR"}[的公网地址]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_2120504031}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_931878163}[注册的私网地址]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_49241_76394_x2088915404}

[[与该]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x546243742}[绑定的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}

[[Current state]{lang="EN-US"}]{#struct_0_49241_76394_x36725748}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1003376855}[当前状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_49241_76394_567969722}[：离线状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Init]{lang="EN-US"}]{#struct_0_49241_76394_x1502647347}[：连接初始化阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Reg]{lang="EN-US"}]{#struct_0_49241_76394_x1282974462}[：注册阶段]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_49241_76394_235004466}[：在线状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dumb]{lang="EN-US"}]{#struct_0_49241_76394_669206058}[：静默状态]{lang="EN-US" style="font-family:宋体"}

[[Client type]{lang="EN-US"}]{#struct_0_49241_76394_441137967}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1494605767}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1304820981}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke]{lang="EN-US"}]{#struct_0_49241_76394_1403075196}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_49241_76394_568952762}

[[Holding time]{lang="PT-BR"}]{#struct_0_49241_76394_x1313422171}

[[VAM Client]{lang="PT-BR"}]{#struct_0_49241_76394_1245526549}[维持当前状态的时间，为]{style="font-family:宋体"}[x]{lang="PT-BR"}[小时]{style="font-family:宋体"}[y]{lang="PT-BR"}[分]{style="font-family:宋体"}[z]{lang="PT-BR"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="PT-BR"}[）]{style="font-family:宋体"}

[[Encryption algorithm]{lang="PT-BR"}]{#struct_0_49241_76394_x696940659}

[[协商使用的加密算法]{style="font-family:宋体"}]{#struct_0_49241_76394_547956356}

[[Authentication algorithm]{lang="PT-BR"}]{#struct_0_49241_76394_1438226693}

[[协商使用的认证算法]{style="font-family:宋体"}]{#struct_0_49241_76394_x721933282}

[[Keepalive]{lang="EN-US"}]{#struct_0_49241_76394_568887226}

[[VAM Server]{lang="PT-BR"}]{#struct_0_49241_76394_1448836045}[下发的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[时间间隔（单位为秒）和重发次数]{style="font-family:宋体"}

[[Number of hubs]{lang="EN-US"}]{#struct_0_49241_76394_805865264}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x724151002}[下发的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[数量]{style="font-family:宋体"}

[[Secondary server]{lang="EN-US"}]{#struct_0_49241_76394_1785623919}

[[备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_384696981}[的公网地址]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1734628257}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset vam client fsm]{lang="EN-US"}**]{#struct_0_49241_76394_343521709}

::: {#1383155245 .myid}
[]{#_Toc404787398}[]{#struct_0_49241_76394_1912581773}

**ADVPN \-- VAM Client配置命令 \-- display vam client shortcut interest**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vam** **client** **shortcut** **interest**]{lang="EN-US"}]{#struct_0_49241_76394_568428475}[命令用来显示]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[下发的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1447675624}

[**[display]{lang="EN-US"}**[ **vam** **client** **shortcut** **interest** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_x784537459}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2037472610}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1574249115}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_690541121}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x122979715}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x34333903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1630328221}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_140600622}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1514409250}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1956170534}[：显示指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的规则。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x701842691}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1953167176}[仅给]{style="font-family:宋体"}[Hub]{lang="EN-US"}[下发跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。如果指定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[为]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[，则下发的规则数为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1794518455}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_568362939}[显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[\<Sysname\> display vam client shortcut interest]{lang="EN-US"}]{#struct_0_49241_76394_x2009778449}

[Client name      : abc]{lang="EN-US"}

[ADVPN domain name: 1]{lang="EN-US"}

[Client type      : Spoke]{lang="EN-US"}

[ACL rules        : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : hub]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Client type      : Hub]{lang="EN-US"}

[ACL rules        : 2]{lang="EN-US"}

[  Rule 1: Permit]{lang="EN-US"}

[    Protocol   : 6 (TCP)]{lang="EN-US"}

[    Source     : Address 0.0.0.0-255.255.255.255, port 0-65535]{lang="EN-US"}

[    Destination: Address 192.168.114.100-192.168.114.200, port 10000-20000]{lang="EN-US"}

[  Rule 2: Deny]{lang="EN-US"}

[    Protocol   : 0 (IP)]{lang="EN-US"}

[    Source     : Address 0.0.0.0-255.255.255.255, port 0-65535]{lang="EN-US"}

[    Destination: Address 0.0.0.0-255.255.255.255, port 0-65535]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : spoke]{lang="EN-US"}

[ADVPN domain name: 3]{lang="EN-US"}

[Client type      : Unknown]{lang="EN-US"}

[ACL rules        : 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1255124328}[显示]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[收到的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[\<Sysname\> display vam client shortcut interest name abc]{lang="EN-US"}]{#struct_0_49241_76394_1387549316}

[Client name      : abc]{lang="EN-US"}

[ADVPN domain name: 1]{lang="EN-US"}

[Client type      : Spoke]{lang="EN-US"}

[ACL rules        : 0]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display vam client shortcut interest]{lang="EN-US"}]{#struct_0_49241_76394_x1391180141}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_133073448}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x348707851}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_568297403}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_x109037613}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_642338382}[的名称]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x2014547061}

[[该]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1180518884}[所在的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域名]{style="font-family:宋体"}

[[Client type]{lang="EN-US"}]{#struct_0_49241_76394_x92679681}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1882331206}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1590422576}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x1061589263}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_49241_76394_152231398}

[[ACL rules]{lang="EN-US"}]{#struct_0_49241_76394_x654536245}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_568231867}[收到的匹配规则计数]{style="font-family:宋体"}

[[Rule *n*: Operation]{lang="EN-US"}]{#struct_0_49241_76394_1108787633}

[[ACL]{lang="EN-US"}]{#struct_0_49241_76394_x921468579}[规则的编号（]{style="font-family:宋体"}*[n]{lang="EN-US"}*[）和动作（]{style="font-family:宋体"}*[Operation]{lang="EN-US"}*[）。]{style="font-family:宋体"}*[Operation]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_49241_76394_1786029621}[：]{style="font-family:宋体"}[允许建立跨]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_49241_76394_1394558774}[：不允许建立跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{style="font-family:宋体"}[IPv4 Spoke-Spoke]{lang="EN-US"}[直连隧道]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Discard]{lang="EN-US"}]{#struct_0_49241_76394_1568125741}[：丢弃该报文]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_49241_76394_1469291191}

[[匹配指定的协议类型]{style="font-family:宋体"}]{#struct_0_49241_76394_878495904}

[[Source]{lang="EN-US"}]{#struct_0_49241_76394_x29924888}

[[匹配指定范围的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_49241_76394_568166331}[地址和源端口号]{style="font-family:宋体"}

[[Destination]{lang="EN-US"}]{#struct_0_49241_76394_1984164505}

[[匹配指定范围的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_49241_76394_x335001153}[地址和目的端口号]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-929415846 .myid}
[]{#_Toc323022594}[]{#_Toc404787399}[]{#struct_0_49241_76394_670854415}

**ADVPN \-- VAM Client配置命令 \-- display vam client shortcut ipv6 interest**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **vam** **client** **shortcut** **ipv6** **interest**]{lang="EN-US"}]{#struct_0_49241_76394_575461384}[命令用来显示]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[下发的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1039943931}

[**[display]{lang="EN-US"}**[ **vam** **client** **shortcut** **ipv6** **interest** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_1347766866}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1829861415}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_1337583243}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x254506737}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x180406585}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_241118760}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x711824162}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_887006602}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_568100795}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1909865413}[：显示指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的规则。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的规则。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_638714014}

[[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_910449040}[仅给]{style="font-family:宋体"}[Hub]{lang="EN-US"}[下发跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。如果指定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[为]{style="font-family:宋体"}[Spoke]{lang="EN-US"}[，则下发的规则数为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_522404110}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_325818231}[显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[收到的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[\<Sysname\> display vam client shortcut ipv6 interest]{lang="EN-US"}]{#struct_0_49241_76394_568035259}

[Client name      : abc]{lang="EN-US"}

[ADVPN domain name: 1]{lang="EN-US"}

[Client type      : Spoke]{lang="EN-US"}

[ACL rules         : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : hub]{lang="EN-US"}

[ADVPN domain name: 2]{lang="EN-US"}

[Client type      : Hub]{lang="EN-US"}

[ACL rules        : 2]{lang="EN-US"}

[  Rule 1: Permit]{lang="EN-US"}

[    Protocol                 : TCP]{lang="EN-US"}

[    Start source address     : 0::0]{lang="EN-US"}

[    End source address       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF]{lang="EN-US"}

[    Start source port        : 0]{lang="EN-US"}

[    End source port          : 65535]{lang="EN-US"}

[    Start destination address: 2000::0]{lang="EN-US"}

[    End destination address  : 2000:1::0]{lang="EN-US"}

[    Start destination port   : 0]{lang="EN-US"}

[    End destination port     : 65535]{lang="EN-US"}

[  Rule 2: Deny]{lang="EN-US"}

[    Protocol                 : All]{lang="EN-US"}

[    Start source address     : 0::0]{lang="EN-US"}

[    End source address       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF]{lang="EN-US"}

[    Start source port        : 0]{lang="EN-US"}

[    End source port          : 65535]{lang="EN-US"}

[    Start destination address: 0::0]{lang="EN-US"}

[    End destination address  : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF]{lang="EN-US"}

[    Start destination port   : 0]{lang="EN-US"}

[    End destination port     : 65535]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name      : spoke]{lang="EN-US"}

[ADVPN domain name: ]{lang="EN-US"}

[Client type      : Unknown]{lang="EN-US"}

[ACL rules        : 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1999404385}[显示]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[收到的跨]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组建立]{style="font-family:宋体"}[IPv6 Spoke-Spoke]{lang="EN-US"}[直连隧道的规则。]{style="font-family:宋体"}

[[\<Sysname\> display vam client shortcut ipv6 interest name abc]{lang="EN-US"}]{#struct_0_49241_76394_1858480797}

[Client name      : spoke]{lang="EN-US"}

[ADVPN domain name: ]{lang="EN-US"}

[Client type      : Unknown]{lang="EN-US"}

[ACL rules        : 0]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display vam client shortcut ipv6 interest]{lang="EN-US"}]{#struct_0_49241_76394_x995220332}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_129956128}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x1328863872}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x2079146684}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_1524565477}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_567969723}[的名称]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_x1502647346}

[[该]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_283109479}[所在的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[域名]{style="font-family:宋体"}

[[Client type]{lang="EN-US"}]{#struct_0_49241_76394_1026635303}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1201547827}[类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1454636691}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke]{lang="EN-US"}]{#struct_0_49241_76394_944364234}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_49241_76394_72906754}

[[ACL rules]{lang="EN-US"}]{#struct_0_49241_76394_1737926133}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x2080298306}[收到的匹配规则计数]{style="font-family:宋体"}

[[Rule *n*: operation]{lang="EN-US"}]{#struct_0_49241_76394_7491745}

[[ACL]{lang="EN-US"}]{#struct_0_49241_76394_568952763}[规则的编号（]{style="font-family:宋体"}*[n]{lang="EN-US"}*[）和动作（]{style="font-family:宋体"}*[Operation]{lang="EN-US"}*[）。]{style="font-family:宋体"}*[Operation]{lang="EN-US"}*[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Permit]{lang="EN-US"}]{#struct_0_49241_76394_x1313422172}[：]{style="font-family:宋体"}[允许建立跨]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[ Spoke-Spoke]{lang="EN-US"}[直连隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Deny]{lang="EN-US"}]{#struct_0_49241_76394_1648811076}[：不]{style="font-family:宋体"}[允许建立跨]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[组]{lang="EN-US" style="font-family:宋体"}[IPv]{lang="EN-US"}[6]{lang="EN-US"}[ Spoke-Spoke]{lang="EN-US"}[直连隧道]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Discard]{lang="EN-US"}]{#struct_0_49241_76394_x1705396369}[：丢弃该报文]{style="font-family:宋体"}

[[Protocol]{lang="EN-US"}]{#struct_0_49241_76394_68805210}

[[匹配指定的协议类型]{style="font-family:宋体"}]{#struct_0_49241_76394_55303014}

[[Start source address]{lang="EN-US"}]{#struct_0_49241_76394_860131394}

[[匹配的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_1802422588}[地址范围的起始地址]{style="font-family:宋体"}

[[End source address]{lang="EN-US"}]{#struct_0_49241_76394_568887227}

[[匹配的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_1448836046}[地址范围的结束地址]{style="font-family:宋体"}

[[Start source port]{lang="EN-US"}]{#struct_0_49241_76394_805668656}

[[匹配的源端口范围的起始端口号]{style="font-family:宋体"}]{#struct_0_49241_76394_591692476}

[[End source port]{lang="EN-US"}]{#struct_0_49241_76394_x923679360}

[[匹配的源端口范围的结束端口号]{style="font-family:宋体"}]{#struct_0_49241_76394_873601807}

[[Start destination address]{lang="EN-US"}]{#struct_0_49241_76394_992465792}

[[匹配的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_x1933779799}[地址范围的起始地址]{style="font-family:宋体"}

[[End destination address]{lang="EN-US"}]{#struct_0_49241_76394_568428472}

[[匹配的目的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_49241_76394_x1447675623}[地址范围的结束地址]{style="font-family:宋体"}

[[Start destination port]{lang="EN-US"}]{#struct_0_49241_76394_1137776842}

[[匹配的目的端口范围的起始端口号]{style="font-family:宋体"}]{#struct_0_49241_76394_x2085475448}

[[End destination port]{lang="EN-US"}]{#struct_0_49241_76394_1151219793}

[[匹配的目的端口范围的结束端口号]{style="font-family:宋体"}]{#struct_0_49241_76394_x36874873}

[ ]{lang="EN-US"}

::: {#-745876304 .myid}
[]{#_Toc404787400}[]{#struct_0_49241_76394_497384594}

**ADVPN \-- VAM Client配置命令 \-- display vam client statistics**

------------------------------------------------------------------------

[**[display vam client statistics]{lang="EN-US"}**]{#struct_0_49241_76394_1267170409}[命令用来显示]{style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x719301715}

[**[display]{lang="EN-US"}**[ **vam** **client** **statistics** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_1150836159}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_568362936}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x2009778440}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1117528667}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1588059458}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x44013365}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x981820371}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_1126516075}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1403172350}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_1982708346}[：显示指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_632148541}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x778127353}[显示所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam client statistics]{lang="EN-US"}]{#struct_0_49241_76394_568166328}

[Client name: abc]{lang="EN-US"}

[ Status     : Enabled]{lang="EN-US"}

[  Primary server: abc.com]{lang="EN-US"}

[    Packets sent:]{lang="EN-US"}

[      Initialization request        : 1]{lang="EN-US"}

[      Initialization complete       : 1]{lang="EN-US"}

[      Register request              : 1]{lang="EN-US"}

[      Authentication information    : 1]{lang="EN-US"}

[      Address resolution request    : 9]{lang="EN-US"}

[      Network registration request  : 0]{lang="EN-US"}

[      Update request                : 0]{lang="EN-US"}

[      Logout request                : 0]{lang="EN-US"}

[      Hub information response      : 0]{lang="EN-US"}

[      Data flow information response: 0]{lang="EN-US"}

[      Keepalive                     : 35]{lang="EN-US"}

[      Error notification            : 0]{lang="EN-US"}

[    Packets received:]{lang="EN-US"}

[      Initialization response      : 1]{lang="EN-US"}

[      Initialization complete      : 1]{lang="EN-US"}

[      Authentication request       : 1]{lang="EN-US"}

[      Register response            : 1]{lang="EN-US"}

[      Address resolution response  : 9]{lang="EN-US"}

[      Network registration response: 0]{lang="EN-US"}

[      Update response              : 0]{lang="EN-US"}

[      Hub information request      : 0]{lang="EN-US"}

[      Data flow information request: 0]{lang="EN-US"}

[      Logout response              : 0]{lang="EN-US"}

[      Keepalive                    : 35]{lang="EN-US"}

[      Error notification           : 0]{lang="EN-US"}

[      Unkonwn                      : 0]{lang="EN-US"}

[  Secondary server: 28.1.1.24]{lang="EN-US"}

[    Packets sent:]{lang="EN-US"}

[      Initialization request        : 15]{lang="EN-US"}

[      Initialization complete       : 0]{lang="EN-US"}

[      Register request              : 0]{lang="EN-US"}

[      Authentication information    : 0]{lang="EN-US"}

[      Address resolution request    : 0]{lang="EN-US"}

[      Network registration request  : 0]{lang="EN-US"}

[      Update request                : 0]{lang="EN-US"}

[      Logout request                : 0]{lang="EN-US"}

[      Hub information response      : 0]{lang="EN-US"}

[      Data flow information response: 0]{lang="EN-US"}

[      Keepalive                     : 0]{lang="EN-US"}

[      Error notification            : 0]{lang="EN-US"}

[    Packets received:]{lang="EN-US"}

[      Initialization response      : 0]{lang="EN-US"}

[      Initialization complete      : 0]{lang="EN-US"}

[      Register response            : 0]{lang="EN-US"}

[      Authentication request       : 0]{lang="EN-US"}

[      Address resolution response  : 0]{lang="EN-US"}

[      Network registration response: 0]{lang="EN-US"}

[      Update response              : 0]{lang="EN-US"}

[      Hub information request      : 0]{lang="EN-US"}

[      Data flow information request: 0]{lang="EN-US"}

[      Logout response              : 0]{lang="EN-US"}

[      Keepalive                    : 0]{lang="EN-US"}

[      Error notification           : 0]{lang="EN-US"}

[      Unkonwn                      : 0]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name: hub]{lang="EN-US"}

[Status     : Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[Client name: spoke]{lang="EN-US"}

[Status     : Enabled]{lang="EN-US"}

[  Primary server: test.com]{lang="EN-US"}

[    Packets sent:]{lang="EN-US"}

[      Initialization request        : 3]{lang="EN-US"}

[      Initialization complete       : 3]{lang="EN-US"}

[      Register request              : 3]{lang="EN-US"}

[      Authentication information    : 3]{lang="EN-US"}

[      Address resolution request    : 0]{lang="EN-US"}

[      Network registration request  : 0]{lang="EN-US"}

[      Update request                : 0]{lang="EN-US"}

[      Logout request                : 0]{lang="EN-US"}

[      Hub information response      : 0]{lang="EN-US"}

[      Data flow information response: 0]{lang="EN-US"}

[      Keepalive                     : 124]{lang="EN-US"}

[      Error notification            : 0]{lang="EN-US"}

[    Packets received:]{lang="EN-US"}

[      Initialization response      : 3]{lang="EN-US"}

[      Initialization complete      : 3]{lang="EN-US"}

[      Authentication request       : 3]{lang="EN-US"}

[      Register response            : 3]{lang="EN-US"}

[      Address resolution response  : 0]{lang="EN-US"}

[      Network registration response: 0]{lang="EN-US"}

[      Update response              : 0]{lang="EN-US"}

[      Hub information request      : 0]{lang="EN-US"}

[      Data flow information request: 0]{lang="EN-US"}

[      Logout response              : 0]{lang="EN-US"}

[      Keepalive                    : 114]{lang="EN-US"}

[      Error notification           : 0]{lang="EN-US"}

[      Unkonwn                      : 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_27849360}[显示]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display vam client statistics name abc]{lang="EN-US"}]{#struct_0_49241_76394_568100792}

[Client name: abc]{lang="EN-US"}

[Status     : Enabled]{lang="EN-US"}

[  Primary server: abc.com]{lang="EN-US"}

[    Packets sent:]{lang="EN-US"}

[      Initialization request        : 1]{lang="EN-US"}

[      Initialization complete       : 1]{lang="EN-US"}

[      Register request              : 1]{lang="EN-US"}

[      Authentication information    : 1]{lang="EN-US"}

[      Address resolution request    : 9]{lang="EN-US"}

[      Network registration request  : 0]{lang="EN-US"}

[      Update request                : 0]{lang="EN-US"}

[      Logout request                : 0]{lang="EN-US"}

[      Hub information response      : 0]{lang="EN-US"}

[      Data flow information response: 0]{lang="EN-US"}

[      Keepalive                     : 35]{lang="EN-US"}

[      Error notification            : 0]{lang="EN-US"}

[    Packets received:]{lang="EN-US"}

[      Initialization response      : 1]{lang="EN-US"}

[      Initialization complete      : 1]{lang="EN-US"}

[      Authentication request       : 1]{lang="EN-US"}

[      Register response            : 1]{lang="EN-US"}

[      Address resolution response  : 9]{lang="EN-US"}

[      Network registration response: 0]{lang="EN-US"}

[      Update response              : 0]{lang="EN-US"}

[      Hub information request      : 0]{lang="EN-US"}

[      Data flow information request: 0]{lang="EN-US"}

[      Logout response              : 0]{lang="EN-US"}

[      Keepalive                    : 35]{lang="EN-US"}

[      Error notification           : 0]{lang="EN-US"}

[      Unkonwn                      : 0]{lang="EN-US"}

[  Secondary server: 28.1.1.24]{lang="EN-US"}

[    Packets sent:]{lang="EN-US"}

[      Initialization request        : 15]{lang="EN-US"}

[      Initialization complete       : 0]{lang="EN-US"}

[      Register request              : 0]{lang="EN-US"}

[      Authentication information    : 0]{lang="EN-US"}

[      Address resolution request    : 0]{lang="EN-US"}

[      Network registration request  : 0]{lang="EN-US"}

[      Update request                : 0]{lang="EN-US"}

[      Logout request                : 0]{lang="EN-US"}

[      Hub information response      : 0]{lang="EN-US"}

[      Data flow information response: 0]{lang="EN-US"}

[      Keepalive                     : 0]{lang="EN-US"}

[      Error notification            : 0]{lang="EN-US"}

[    Packets received:]{lang="EN-US"}

[      Initialization response      : 0]{lang="EN-US"}

[      Initialization complete      : 0]{lang="EN-US"}

[      Register response            : 0]{lang="EN-US"}

[      Authentication request       : 0]{lang="EN-US"}

[      Address resolution response  : 0]{lang="EN-US"}

[      Network registration response: 0]{lang="EN-US"}

[      Update response              : 0]{lang="EN-US"}

[      Hub information request      : 0]{lang="EN-US"}

[      Data flow information request: 0]{lang="EN-US"}

[      Logout response              : 0]{lang="EN-US"}

[      Keepalive                    : 0]{lang="EN-US"}

[      Error notification           : 0]{lang="EN-US"}

[      Unkonwn                      : 0]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display vam client statistic]{lang="EN-US"}]{#struct_0_49241_76394_x1909865408}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_123943624}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_1398163365}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_568035256}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_1999404372}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1858022034}[的名称]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_49241_76394_923876316}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1794988189}[的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_49241_76394_x255415062}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_49241_76394_609004424}

[[Primary server]{lang="EN-US"}]{#struct_0_49241_76394_949226896}

[[主]{style="font-family:宋体"}]{#struct_0_49241_76394_x545664607}[VAM Server]{lang="PT-BR"}[的公网地址或域名]{style="font-family:宋体"}

[[Secondary server]{lang="EN-US"}]{#struct_0_49241_76394_x1451475165}

[[备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_567969720}[的公网地址或域名]{style="font-family:宋体"}

[[Packets sent]{lang="EN-US"}]{#struct_0_49241_76394_x1502647345}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x120175048}[发送的报文数目]{style="font-family:宋体"}

[[Initialization request]{lang="EN-US"}]{#struct_0_49241_76394_x644439296}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1702701769}[发送的初始化请求报文数目]{style="font-family:宋体"}

[[Initialization complete]{lang="EN-US"}]{#struct_0_49241_76394_x524838883}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1962826053}[发送的初始化完成报文数目]{style="font-family:宋体"}

[[Register request]{lang="EN-US"}]{#struct_0_49241_76394_x564920716}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1373577639}[发送的注册请求报文数目]{style="font-family:宋体"}

[[Authentication information]{lang="EN-US"}]{#struct_0_49241_76394_568952760}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1313422173}[发送的认证信息报文数目]{style="font-family:宋体"}

[[Address resolution request]{lang="EN-US"}]{#struct_0_49241_76394_82727135}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x219506005}[发送的地址解析请求报文数目]{style="font-family:宋体"}

[[Network registration request]{lang="EN-US"}]{#struct_0_49241_76394_x330777676}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x621706012}[发送的私网注册请求报文数目]{style="font-family:宋体"}

[[Update request]{lang="EN-US"}]{#struct_0_49241_76394_x1634658237}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1496299067}[发送的节点更新请求报文数目]{style="font-family:宋体"}

[[Logout request]{lang="EN-US"}]{#struct_0_49241_76394_568887224}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1448836043}[发送的清除请求报文数目]{style="font-family:宋体"}

[[Hub information response]{lang="EN-US"}]{#struct_0_49241_76394_805996336}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_810148342}[发送的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[信息响应报文数目]{style="font-family:宋体"}

[[Data flow information response]{lang="EN-US"}]{#struct_0_49241_76394_809748594}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x627912801}[发送的数据流信息响应报文数目]{style="font-family:宋体"}

[[Keepalive]{lang="EN-US"}]{#struct_0_49241_76394_568428473}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1447675622}[发送的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文数目]{style="font-family:宋体"}

[[Error notification]{lang="EN-US"}]{#struct_0_49241_76394_x1591106513}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x821342343}[发送的错误通知报文数目]{style="font-family:宋体"}

[[Unkonwn]{lang="EN-US"}]{#struct_0_49241_76394_x348591567}

[[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x75332148}[发送的未知报文或错误报文数目]{style="font-family:宋体"}

[[Packets received]{lang="EN-US"}]{#struct_0_49241_76394_x1364034140}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_568362937}[接收的报文数目]{style="font-family:宋体"}

[[Initialization response]{lang="EN-US"}]{#struct_0_49241_76394_x2009778439}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1255058792}[接收的初始化响应报文数目]{style="font-family:宋体"}

[[Initialization complete]{lang="EN-US"}]{#struct_0_49241_76394_524470752}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1623387252}[接收的初始化完成报文数目]{style="font-family:宋体"}

[[Authentication request]{lang="EN-US"}]{#struct_0_49241_76394_956088170}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_568297401}[接收的认证请求报文数目]{style="font-family:宋体"}

[[Register response]{lang="EN-US"}]{#struct_0_49241_76394_x109037615}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_642731598}[接收的注册响应报文数目]{style="font-family:宋体"}

[[Address resolution response]{lang="EN-US"}]{#struct_0_49241_76394_67090415}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_843483107}[接收的地址解析响应报文数目]{style="font-family:宋体"}

[[Network registration response]{lang="EN-US"}]{#struct_0_49241_76394_568231865}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1108787635}[接收的私网注册响应报文数目]{style="font-family:宋体"}

[[Update response]{lang="EN-US"}]{#struct_0_49241_76394_x921075363}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1311530335}[接收的节点更新响应报文数目]{style="font-family:宋体"}

[[Hub information request]{lang="EN-US"}]{#struct_0_49241_76394_1366180332}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_568166329}[接收的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[信息请求报文数目]{style="font-family:宋体"}

[[Data flow information request]{lang="EN-US"}]{#struct_0_49241_76394_27849361}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1328828545}[接收的数据流信息请求报文数目]{style="font-family:宋体"}

[[Logout response]{lang="EN-US"}]{#struct_0_49241_76394_2146817972}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x472977587}[接收的清除响应报文数目]{style="font-family:宋体"}

[[Keepalive]{lang="EN-US"}]{#struct_0_49241_76394_568100793}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x1909865407}[接收的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文数目]{style="font-family:宋体"}

[[Error notification]{lang="EN-US"}]{#struct_0_49241_76394_x1330719990}

[[从]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x786639940}[接收的错误通知报文数目]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1050416370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset vam client ]{lang="EN-US"}**]{#struct_0_49241_76394_x1340249880}**[statistics]{lang="EN-US"}**

::: {#-779998188 .myid}
[]{#_Toc404787401}[]{#struct_0_49241_76394_972592396}

**ADVPN \-- VAM Client配置命令 \-- dumb-time**

------------------------------------------------------------------------

[**[dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_x129978201}[命令用来配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[连接超时的静默时间。]{style="font-family:宋体"}

[**[undo dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_568035257}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1999404371}

[**[dumb-time]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_1858218642}

[**[undo dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_1306446383}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x496956252}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1087508413}[连接超时的静默时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1819946504}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1328644971}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1249637602}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_243401507}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x34225766}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1961609631}

[*[time-interval]{lang="EN-US"}*]{#struct_0_49241_76394_1667638090}[：]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[连接超时的静默时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x587223366}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1950666662}[在与]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[连接超时后，会进入静默状态，此时]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[不处理任何报文。当静默时间到达后，]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[将重新上线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_567969721}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1502647344}[配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的静默时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1445908893}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] dumb-time 100]{lang="EN-US"}
:::

::: {#2031336047 .myid}
[]{#_Toc404787402}[]{#struct_0_49241_76394_x1249319024}[]{#_Toc375152456}[]{#_Toc375152457}

**ADVPN \-- VAM Client配置命令 \-- pre-shared-key (VAM Client view)**

------------------------------------------------------------------------

[**[pre-shared-key]{lang="EN-US"}**]{#struct_0_49241_76394_1060220629}[命令用来配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的预共享密钥。]{style="font-family:宋体"}

[**[undo pre-shared-key]{lang="EN-US"}**]{#struct_0_49241_76394_1750619148}[命令用来删除]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的预共享密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x483961593}

[**[pre-shared-key]{lang="EN-US"}**[ { **cipher** *cipher-string* \| **simple** *simple-string* }]{lang="EN-US"}]{#struct_0_49241_76394_x360597005}

[**[undo pre-shared-key]{lang="EN-US"}**]{#struct_0_49241_76394_155472226}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1309787277}

[[未配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_404414588}[的预共享密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1712402263}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1237004413}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1169407314}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_568952761}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1313422174}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_842242022}

[**[cipher]{lang="EN-US"}***[ cipher-string]{lang="EN-US"}*]{#struct_0_49241_76394_x470594301}[：以密文方式设置预共享密钥。]{style="font-family:宋体"}*[cipher-string]{lang="EN-US"}*[为密文预共享密钥，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}***[ simple-string]{lang="EN-US"}*]{#struct_0_49241_76394_x406268724}[：以明文方式设置预共享密钥。]{style="font-family:宋体"}*[simple-string]{lang="EN-US"}*[为明文预共享密钥，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的明文字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x476080746}

[[预共享密钥是]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_x403897961}[用来和]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[建立安全通道的公共密钥材料。在连接初始化阶段预共享密钥用来生成验证和加密连接请求、连接响应报文的初始密钥；如果选择对后续的报文进行加密和验证，则预共享密钥还用来生成验证和加密后续报文的连接密钥。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_225267637}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个]{style="font-family:宋体"}]{#struct_0_49241_76394_x453812941}[ADVPN]{lang="EN-US"}[域]{style="font-family:宋体"}[内]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[和]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上配置]{lang="EN-US" style="font-family:宋体"}[的预共享密钥必须]{style="font-family:宋体"}[一致]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的预共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_49241_76394_222366163}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1109943237}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1157552818}[以明文方式配置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的预共享密钥为]{style="font-family:宋体"}[123]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_517322189}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] pre-shared-key simple 123]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_791457713}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam client name]{lang="EN-US"}**]{#struct_0_49241_76394_x1946001510}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pre-shared-key]{lang="EN-US"}**[ (ADVPN domain view)]{lang="EN-US"}]{#struct_0_49241_76394_568887225}
:::

::: {#-2021510486 .myid}
[]{#_Toc151282219}[]{#_Toc404787403}[]{#struct_0_49241_76394_1448836044}

**ADVPN \-- VAM Client配置命令 \-- reset vam client fsm**

------------------------------------------------------------------------

[**[reset vam client fsm]{lang="EN-US"}**]{#struct_0_49241_76394_805799728}[命令用来重置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x541716612}

[**[reset]{lang="EN-US"}**[ **vam** **client** **fsm** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_x403352115}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1020790732}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_344667010}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1749760918}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x391756941}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1041239930}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1115333240}[：重置指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则重置所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1354779172}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1307660311}[的状态机重置后，会立刻尝试重新上线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2027215961}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_568428470}[重置]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client fsm name abc]{lang="EN-US"}]{#struct_0_49241_76394_x1447675621}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x25022572}[重置所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client fsm]{lang="EN-US"}]{#struct_0_49241_76394_484420318}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x466175374}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ vam client fsm]{lang="EN-US"}**]{#struct_0_49241_76394_x1686476861}
:::

::: {#1856219129 .myid}
[]{#_Toc404787404}[]{#struct_0_49241_76394_400886487}

**ADVPN \-- VAM Client配置命令 \-- reset vam client ipv6 fsm**

------------------------------------------------------------------------

[**[reset vam client ipv6 fsm]{lang="EN-US"}**]{#struct_0_49241_76394_399826918}[命令用来重置]{style="font-family:
宋体"}[IPv6 VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x42781058}

[**[reset]{lang="EN-US"}**[ **vam** **client** **ipv6** **fsm** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_1664745956}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_292788844}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_657247027}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_74061462}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1392180382}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1636849798}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_568362934}[：重置指定]{style="font-family:宋体"}[IPv6 VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则重置所有]{style="font-family:宋体"}[IPv6 VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2009778438}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1473824563}[的状态机重置后，会立刻尝试重新上线。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_2134605337}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1998963156}[重置]{style="font-family:宋体"}[IPv6 VAM Client abc]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client ipv6 fsm name abc]{lang="EN-US"}]{#struct_0_49241_76394_x852100678}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_575271425}[重置所有]{style="font-family:宋体"}[IPv6 VAM Client]{lang="EN-US"}[的状态机。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client ipv6 fsm]{lang="EN-US"}]{#struct_0_49241_76394_x2124922294}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1979106510}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ vam client fsm]{lang="EN-US"}**]{#struct_0_49241_76394_x1527254901}
:::

::: {#903306171 .myid}
[]{#_Toc404787405}[]{#struct_0_49241_76394_x140030204}

**ADVPN \-- VAM Client配置命令 \-- reset vam client statistics**

------------------------------------------------------------------------

[**[reset vam client statistic]{lang="EN-US"}**]{#struct_0_49241_76394_x1703997334}[命令用来清除]{style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_316507211}

[**[reset]{lang="EN-US"}**[ **vam** **client** **statistics** \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_568297398}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x59248445}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_330758293}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1303170406}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1077467936}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1435990923}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1918112754}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1818223659}[：清除指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="EN-US"}[、]{style="font-family:宋体"}[a-z]{lang="EN-US"}[、]{style="font-family:宋体"}[0-9]{lang="EN-US"}[和"]{style="font-family:宋体"}[.]{lang="EN-US"}["。如果未指定本参数，则清除所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x546376620}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1158174056}[清除]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client statistics name abc]{lang="EN-US"}]{#struct_0_49241_76394_x951168373}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x340683047}[清除所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset vam client statistics]{lang="EN-US"}]{#struct_0_49241_76394_86613241}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1036773563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ vam client ]{lang="EN-US"}**]{#struct_0_49241_76394_x1913046182}**[statistics]{lang="EN-US"}**
:::

::: {#1554758993 .myid}
[]{#_Toc404787406}[]{#struct_0_49241_76394_568231862}

**ADVPN \-- VAM Client配置命令 \-- retry**

------------------------------------------------------------------------

[**[retry]{lang="EN-US"}**]{#struct_0_49241_76394_1108787638}[命令用来设置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[重发请求报文的时间间隔和重发次数。]{style="font-family:宋体"}

[**[undo retry]{lang="EN-US"}**]{#struct_0_49241_76394_x920878755}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1005233839}

[**[retry interval]{lang="EN-US"}**[ *time-interval* **count** *retry-times*]{lang="EN-US"}]{#struct_0_49241_76394_804040590}

[**[undo retry]{lang="EN-US"}**]{#struct_0_49241_76394_99352362}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_621747474}

[[请求报文的重发时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_49241_76394_1037744524}[秒，重发次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_920666704}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x295592163}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_968703186}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1160443494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_225643833}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x359940625}

[**[interval]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_1652880108}[：请求报文的重发时间间隔，取值范围为]{style="font-family:宋体"}[3]{lang="EN-US"}[～]{style="font-family:宋体"}[30]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**[ *retry-times*]{lang="EN-US"}]{#struct_0_49241_76394_568166326}[：请求报文的重发次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[6]{lang="EN-US"}[。]{style="font-family:
宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_27849370}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1719059740}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[发送请求报文后，如果在指定的时间间隔内没有收到响应报文，]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[将重新发送请求报文。如果重新发送请求报文的次数超过指定的重发次数，则]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[认为]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[不可达。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_1494365541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[私网注册请求报文和节点信息更新请求报文不受重发次数的限制，将会按照指定的时间间隔一直发送，直至]{style="font-family:宋体"}]{#struct_0_49241_76394_1972156061}[VAM Client]{lang="EN-US"}[下线。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x346165108}[发送]{style="font-family:
宋体"}[Keepalive]{lang="EN-US"}[报文]{style="font-family:宋体"}[的时间间隔和]{lang="EN-US" style="font-family:宋体"}[重发]{style="font-family:宋体"}[次数由]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的]{style="font-family:宋体"}[配置决定。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_2086449914}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1690188601}[设置]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[重发请求报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，重发次数为]{style="font-family:宋体"}[4]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1357624245}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] retry interval 20 count 4]{lang="EN-US"}
:::

::: {#-1138790165 .myid}
[]{#_Toc404787407}[]{#struct_0_49241_76394_x1283763617}

**ADVPN \-- VAM Client配置命令 \-- server primary**

------------------------------------------------------------------------

[**[server primary]{lang="EN-US"}**]{#struct_0_49241_76394_x1296744665}[命令用来配置主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的地址。]{style="font-family:宋体"}

[**[undo server primary]{lang="EN-US"}**]{#struct_0_49241_76394_x1317213326}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1551099603}

[**[server primary]{lang="EN-US"}**[ { **ip-address**]{lang="EN-US"}[ *ip-address* \| **ipv6-address** *ipv6-address* \| **name** *host-name* } \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_49241_76394_484347726}

[**[undo server primary]{lang="EN-US"}**]{#struct_0_49241_76394_568100790}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1909865410}

[[没有配置主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1041998541}[的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1202513803}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x385765716}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1746826219}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x181357751}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x556359073}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1868356995}

[**[ip-address]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_49241_76394_x436773383}[：主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，该地址必须是单播地址。]{style="font-family:宋体"}

[**[ipv6-address]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_49241_76394_x2143791271}[：主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，该地址必须是全球单播地址。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *host-name*]{lang="EN-US"}]{#struct_0_49241_76394_x746221359}[：主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的域名，由以"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成，每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["及"]{style="font-family:宋体"}[\_]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_49241_76394_206406979}[：主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[18000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x74311929}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新的配置将覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_49241_76394_2001152564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_568035254}[上]{style="font-family:
宋体"}[指定]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的端口号，则必须和]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}**[vam server listen-port]{lang="EN-US"}**[命令配置的监听端口号一致。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1999404374}[和备]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的地址相同（配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[相同的地址或通过域名解析到相同的地址），则只有主]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[有效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1858415250}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_955243905}[指定主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的域名为]{style="font-family:宋体"}[abc.com]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1887728238}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server primary name abc.com port 2000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x945761732}[指定主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_2028176911}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server primary ip-address 1.1.1.1 port 2000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1031062073}[指定主]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1001::1]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_357191733}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server primary ipv6-address 1001::1 port 2000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1001819519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server secondary]{lang="EN-US"}**]{#struct_0_49241_76394_2037835323}
:::

::: {#-1246536809 .myid}
[]{#_Toc404787408}[]{#struct_0_49241_76394_x1423392627}[]{#_Toc151282220}[]{#_Toc151282221}[]{#_Toc375152463}[]{#_Toc375152464}[]{#_Toc375152465}

**ADVPN \-- VAM Client配置命令 \-- server secondary**

------------------------------------------------------------------------

[**[server secondary]{lang="EN-US"}**]{#struct_0_49241_76394_x2106526552}[命令用来配置备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的地址。]{style="font-family:宋体"}

[**[undo server secondary]{lang="EN-US"}**]{#struct_0_49241_76394_567969718}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_71330759}

[**[server secondary]{lang="EN-US"}**[ { **ip-address**]{lang="EN-US"}[ *ip-address* \| **ipv6-address** *ipv6-address* \| **name** *host-name* } \[ **port** *port-number* \]]{lang="EN-US"}]{#struct_0_49241_76394_786414993}

[**[undo server secondary]{lang="EN-US"}**]{#struct_0_49241_76394_x1479931411}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_2109463333}

[[没有配置备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_1035838293}[的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1767065358}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x191047957}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1556112937}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x409881068}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x235706753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x701367939}

[**[ip-address]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x395489554}[：备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，该地址必须是单播地址。]{style="font-family:宋体"}

[**[ipv6-address]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x396358475}[：备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，该地址必须是全球单播地址。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}**[ *host-name*]{lang="EN-US"}]{#struct_0_49241_76394_568952758}[：备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的域名，由以"]{style="font-family:宋体"}[.]{lang="EN-US"}["分隔的字符串组成，每个字符串的长度不超过]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符，包括"]{style="font-family:宋体"}[.]{lang="EN-US"}["在内的总长度不超过]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符，不区分大小写，字符串中可以包含字母、数字、"]{style="font-family:宋体"}[-]{lang="EN-US"}["及"]{style="font-family:宋体"}[\_]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_49241_76394_260555931}[：备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[18000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_1482371327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[重复执行本命令，新的配置将覆盖原有配置。]{style="font-family:宋体"}]{#struct_0_49241_76394_x1146491854}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x412929111}[上]{style="font-family:
宋体"}[指定]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的端口号，则必须和]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[上]{lang="EN-US" style="font-family:宋体"}[通过]{style="font-family:宋体"}**[vam server listen-port]{lang="EN-US"}**[命令]{style="font-family:宋体"}[配置的监听端口号一致。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果主]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}]{#struct_0_49241_76394_702415680}[和备]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的地址相同（配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[相同的地址或通过域名解析到相同的地址），则只有主]{lang="EN-US" style="font-family:宋体"}[VAM Server]{lang="EN-US"}[有效。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1300967685}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1851359388}[指定备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的域名为]{style="font-family:宋体"}[abc.com]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[2000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1437554025}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server secondary name abc.com port 2000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x541113846}[指定备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x791110613}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server secondary ip-address 1.1.1.2 port 3000]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1225120352}[指定备]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[的公网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1001::2]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[3000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_13346389}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] server secondary ipv6-address 1001::2 port 3000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_568887222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[server primary]{lang="EN-US"}**]{#struct_0_49241_76394_1448836049}
:::

::: {#1904591196 .myid}
[]{#_Toc404787409}[]{#struct_0_49241_76394_806651696}[]{#_Toc375152467}[]{#_Toc375152468}

**ADVPN \-- VAM Client配置命令 \-- user**

------------------------------------------------------------------------

[**[user]{lang="EN-US"}**]{#struct_0_49241_76394_x587323216}[命令用来配置认证用户名和密码。]{style="font-family:宋体"}

[**[undo user]{lang="EN-US"}**]{#struct_0_49241_76394_x5648372}[命令用来取消配置的认证用户名和密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_265712328}

[**[user]{lang="EN-US"}**[ *username* **password** { **cipher** *cipher-string* \| **simple** *simple-string* }]{lang="EN-US"}]{#struct_0_49241_76394_1375124069}

[**[undo user]{lang="EN-US"}**]{#struct_0_49241_76394_x1094514858}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1986104786}

[[没有配置认证用户名和密码。]{style="font-family:宋体"}]{#struct_0_49241_76394_x1592628617}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1519524807}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1074128206}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x295399408}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2144662447}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2131040411}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_568428471}

[*[username]{lang="DA"}*]{#struct_0_49241_76394_x1447675620}[：]{style="font-family:宋体"}[认证]{style="font-family:宋体"}[用户名，为]{style="font-family:宋体"}[1]{lang="DA"}[～]{style="font-family:宋体"}[253]{lang="DA"}[个字符的字符串，区分大小写，不能包括"]{style="font-family:
宋体"}[/]{lang="EN-US"}["、"]{style="font-family:
宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符。]{style="font-family:宋体"}

[**[password]{lang="DA"}**]{#struct_0_49241_76394_1541061369}[：设置用户密码。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}***[ cipher-string]{lang="EN-US"}*]{#struct_0_49241_76394_x36259722}[：以密文方式设置用户密码。]{style="font-family:宋体"}*[cipher-string]{lang="EN-US"}*[为密文用户密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}***[ simple-string]{lang="EN-US"}*]{#struct_0_49241_76394_804868448}[：以明文方式设置用户密码。]{style="font-family:宋体"}*[simple-string]{lang="EN-US"}*[为明文用户密码，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的明文字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_1475578553}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x982347895}[的用户名和密码，用于向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[进行身份认证。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_622830179}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_49241_76394_53316186}[VAM Client]{lang="EN-US"}[下只允许配置一个认证用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文形式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_49241_76394_820881848}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_303817547}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_339461498}[设置]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的认证用户名为]{style="font-family:宋体"}[user]{lang="EN-US"}[，以明文方式设置用户密码为]{style="font-family:宋体"}[user]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1964563759}

[\[Sysname\] vam client name abc]{lang="EN-US"}

[\[Sysname-vam-client-abc\] user user password simple user]{lang="EN-US"}
:::

::: {#534433208 .myid}
[]{#_Toc404787410}[]{#struct_0_49241_76394_1337214793}[]{#_Toc375152470}[]{#_Toc375152471}

**ADVPN \-- VAM Client配置命令 \-- vam client enable**

------------------------------------------------------------------------

[**[vam client enable]{lang="EN-US"}**]{#struct_0_49241_76394_568362935}[命令用来启动所有或指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo vam client enable]{lang="EN-US"}**]{#struct_0_49241_76394_x2009778437}[命令用来关闭所有或指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_804720098}

[**[vam client enable]{lang="EN-US"}**[ \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_x335192663}

[**[undo vam client enable]{lang="EN-US"}**[ \[ **name** *client-name* \]]{lang="EN-US"}]{#struct_0_49241_76394_x563688640}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x833389391}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1241977464}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1999111254}

[[系统视图]{style="font-family:宋体"}]{#struct_0_49241_76394_857941266}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1918093473}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x811914146}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_2031134058}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1072286264}

[**[name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_543391734}[：启动指定]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}*[client-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="PT-BR"}[、]{style="font-family:宋体"}[a-z]{lang="PT-BR"}[、]{style="font-family:宋体"}[0-9]{lang="PT-BR"}[和"]{style="font-family:宋体"}[.]{lang="PT-BR"}["。如果未指定本参数，启动所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1076189893}

[[还可以在]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_568297399}[视图下通过]{style="font-family:宋体"}**[client]{lang="EN-US"}**[ **enable**]{lang="EN-US"}[命令来启动相应]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x59248446}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_330758294}[启动所有]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1303170413}

[\[Sysname\] vam client enable]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_674117873}[启动]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_947833542}

[\[Sysname\] vam client enable name abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x145772283}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client enable]{lang="EN-US"}**]{#struct_0_49241_76394_x791664573}
:::

::: {#-1766875932 .myid}
[]{#_Toc404787411}[]{#struct_0_49241_76394_x1633290027}[]{#_Toc151282223}

**ADVPN \-- VAM Client配置命令 \-- vam client name**

------------------------------------------------------------------------

[**[vam client ]{lang="PT-BR"}[name]{lang="EN-US"}**]{#struct_0_49241_76394_x1098562404}[命令用来创建]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[，并进入]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[视图。如果]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[已经存在，则直接进入该]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[视图。]{style="font-family:宋体"}

[**[undo vam client name]{lang="EN-US"}**]{#struct_0_49241_76394_127982749}[命令用来删除指定的]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1950251789}

[**[vam client name ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_x1062817616}

[**[undo vam client name]{lang="EN-US"}**[ *client-name*]{lang="EN-US"}]{#struct_0_49241_76394_1354139039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_568231863}

[[没有配置]{style="font-family:宋体"}]{#struct_0_49241_76394_1108787637}[VAM Client]{lang="PT-BR"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x921206435}

[[系统视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1685252227}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x645417448}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x215102902}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1199630564}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2111678363}

[*[client-name]{lang="PT-BR"}*]{#struct_0_49241_76394_x247040108}[：]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[的]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[63]{lang="PT-BR"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="PT-BR"}[、]{style="font-family:宋体"}[a-z]{lang="PT-BR"}[、]{style="font-family:宋体"}[0-9]{lang="PT-BR"}[和"]{style="font-family:宋体"}[.]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2012278678}

[[\# ]{lang="PT-BR"}]{#struct_0_49241_76394_x1360840764}[创建一个名为]{style="font-family:宋体"}[abc]{lang="PT-BR"}[的]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[，并进入]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="PT-BR"}]{#struct_0_49241_76394_664483648}

[\[Sysname\] vam client name abc]{lang="PT-BR"}

[\[Sysname-vam-client-abc\]]{lang="EN-US"}
:::

::: {#2056225993 .myid}
[]{#_Toc404787413}[]{#struct_0_49241_76394_1953005505}

**ADVPN \-- ADVPN隧道配置命令 \-- advpn ipv6 network**

------------------------------------------------------------------------

[**[advpn ipv6 network]{lang="EN-US"}**]{#struct_0_49241_76394_x801841654}[命令用来添加]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[**[undo advpn ipv6 network]{lang="EN-US"}**]{#struct_0_49241_76394_568166327}[命令用来删除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_27849371}

[**[advpn ipv6 network]{lang="EN-US"}**[ *prefix prefix-length* \[ **preference** *preference-value* \]]{lang="EN-US"}]{#struct_0_49241_76394_x237255396}

[**[undo advpn ipv6 network]{lang="EN-US"}**[ *prefix prefix-length*]{lang="EN-US"}]{#struct_0_49241_76394_x1570792735}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1023522158}

[[没有配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_221262613}[隧道的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_91218459}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_377407298}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1762923970}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1360940934}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_658061114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2014196387}

[*[prefix prefix-length]{lang="EN-US"}*]{#struct_0_49241_76394_873580064}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀及前缀长度。]{style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[preference]{lang="EN-US"}**[ *preference-value*]{lang="EN-US"}]{#struct_0_49241_76394_x1993330769}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道私网路由优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_251120984}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_568100791}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网信息。其他]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[解析私网报文目的地址时，如果解析的地址属于注册私网，则]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[将注册]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的节点信息返回给查询方。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_x1909865409}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只有在]{style="font-family:宋体"}]{#struct_0_49241_76394_x167920576}[IPv6 ]{lang="EN-US"}[ADVPN]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_1180967332}[接口]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}[并通过]{style="font-family:宋体"}**[vam]{lang="EN-US"}**[ **ipv6** **client**]{lang="EN-US"}[命令指定了接口引用的]{lang="EN-US" style="font-family:
宋体"}[VAM Client]{lang="EN-US"}[后，本命令才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_x947137509}[接口]{lang="EN-US" style="font-family:宋体"}[下可以配置多个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[私网路由的优先级建议高于其他动态路由协议，且低于静态路由。优先级数值越大，优先级越低。]{style="font-family:宋体"}]{#struct_0_49241_76394_1201850820}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1444207900}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1738294266}[给接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[增加]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息]{style="font-family:宋体"}[1001::/64]{lang="EN-US"}[，私网路由优先级为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1674273799}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv6]{lang="EN-US"}

[\[Sysname-Tunnel1\] advpn ipv6 network 1001:: 64 preference 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x519947569}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam ipv6 client]{lang="EN-US"}**]{#struct_0_49241_76394_2082424730}
:::

::: {#1832366898 .myid}
[]{#_Toc404787414}[]{#struct_0_49241_76394_x2035794460}

**ADVPN \-- ADVPN隧道配置命令 \-- advpn network**

------------------------------------------------------------------------

[**[advpn network]{lang="EN-US"}**]{#struct_0_49241_76394_1073155339}[命令用来添加]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[**[undo advpn network]{lang="EN-US"}**]{#struct_0_49241_76394_2122879672}[命令用来删除]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_568035255}

[**[advpn network]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* } \[ **preference** *preference-value* \]]{lang="EN-US"}]{#struct_0_49241_76394_1999404373}

[**[undo advpn network]{lang="EN-US"}**[ *ip-address* { *mask-length* \| *mask* }]{lang="EN-US"}]{#struct_0_49241_76394_1858087570}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_1759704281}

[[没有配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x201895349}[隧道的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1119733527}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_1365060346}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_1917735888}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x530488691}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x833386637}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1260321023}

[*[ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_1197852812}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网网段地址。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_49241_76394_747007598}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网网段掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_49241_76394_35420506}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网网段掩码。]{style="font-family:宋体"}

[**[preference]{lang="EN-US"}**[ *preference-value*]{lang="EN-US"}]{#struct_0_49241_76394_x1641925673}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网路由优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x313962819}

[[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_567969719}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的私网信息。其他]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[解析私网报文目的地址时，如果解析的地址属于注册私网，则]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[将注册]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[的节点信息返回给查询方。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_71330760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只有在]{style="font-family:宋体"}]{#struct_0_49241_76394_x43836574}[IPv4 ]{lang="EN-US"}[ADVPN]{lang="EN-US"}[类型的]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在]{lang="EN-US" style="font-family:宋体"}]{#struct_0_49241_76394_2025429807}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[上]{style="font-family:宋体"}[配置]{lang="EN-US" style="font-family:宋体"}[了]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}[并通过]{style="font-family:宋体"}**[vam]{lang="EN-US"}**[ **client**]{lang="EN-US"}[命令指定了接口引用的]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}[后，本命令才会生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[每个]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_2043560278}[接口]{lang="EN-US" style="font-family:宋体"}[下可以配置多个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[私网路由的优先级建议高于其他动态路由协议，且低于静态路由。优先级数值越大，优先级越低。]{style="font-family:宋体"}]{#struct_0_49241_76394_x453101703}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_569736555}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_975086999}[给接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[增加]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息]{style="font-family:宋体"}[10.0.5.0 255.255.255.0]{lang="EN-US"}[，私网路由优先级为]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x2023590954}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-Tunnel1\] advpn network 10.0.5.0 255.255.255.0 preference 20]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x824231326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam client]{lang="EN-US"}**]{#struct_0_49241_76394_595621199}
:::

::: {#1882224383 .myid}
[]{#_Toc404787415}[]{#struct_0_49241_76394_x635723845}

**ADVPN \-- ADVPN隧道配置命令 \-- advpn session dumb-time**

------------------------------------------------------------------------

[**[advpn session dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_x1723902124}[命令用来配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道建立失败的静默时间。]{style="font-family:宋体"}

[**[undo advpn session dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_x555417468}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_568952759}

[**[advpn session dumb-time]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_260555930}

[**[undo advpn session dumb-time]{lang="EN-US"}**]{#struct_0_49241_76394_1482371326}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1146557390}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2091129314}[隧道建立失败的的静默时间为]{style="font-family:宋体"}[120]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_459497605}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_228535187}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_80535270}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1079253541}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1283330660}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_318958495}

[*[time-interval]{lang="EN-US"}*]{#struct_0_49241_76394_1185300926}[：]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道建立失败的的静默时间，取值范围为]{style="font-family:宋体"}[10]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x749308009}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只有在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_794146276}[类型的]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[修改此参数对已经建立的]{style="font-family:宋体"}]{#struct_0_49241_76394_369573936}[ADPVN]{lang="EN-US"}[隧道没有影响，之后建立的]{style="font-family:宋体"}[ADPVN]{lang="EN-US"}[隧道会使用修改后的参数值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_568887223}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1448836050}[配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道建立失败的的静默时间为]{style="font-family:宋体"}[100]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_806061871}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-Tunnel1\] advpn session dumb-time 100]{lang="EN-US"}
:::

::: {#-1354631497 .myid}
[]{#_Toc404787416}[]{#struct_0_49241_76394_x557987780}[]{#_Toc375152478}[]{#_Toc375152479}

**ADVPN \-- ADVPN隧道配置命令 \-- advpn session idle-time**

------------------------------------------------------------------------

[**[advpn session idle-time]{lang="EN-US"}**]{#struct_0_49241_76394_149340856}[命令用来配置]{style="font-family:宋体"}[Spoke-Spoke]{lang="EN-US"}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的空闲超时时间。]{style="font-family:宋体"}

[**[undo advpn session idle-time]{lang="EN-US"}**]{#struct_0_49241_76394_2145694543}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_371483951}

[**[advpn session idle-time]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_49241_76394_1377119096}

[**[undo advpn session idle-time]{lang="EN-US"}**]{#struct_0_49241_76394_x1945494674}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1591089990}

[[Spoke-Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x441008632}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的空闲超时时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x637815485}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_108895255}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x483226342}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_2134512415}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1571687950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1601974947}

[*[time-interval]{lang="EN-US"}*]{#struct_0_49241_76394_x1721174734}[：]{style="font-family:宋体"}[Spoke-Spoke]{lang="EN-US"}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的空闲超时时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_1340498043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只有在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1128142810}[类型的]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果修改此参数，已经建立的]{style="font-family:宋体"}]{#struct_0_49241_76394_x891959386}[Spoke-Spoke]{lang="EN-US"}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道会使用修改后的参数值重新开始计时。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在空闲超时时间内，]{style="font-family:宋体"}]{#struct_0_49241_76394_x451146465}[Spoke-Spoke]{lang="EN-US"}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道上没有数据传输，则断开该隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_743126622}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_195432991}[配置]{style="font-family:宋体"}[Spoke-Spoke]{lang="EN-US"}[类型]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的空闲超时时间为]{style="font-family:宋体"}[800]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x540781198}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-tunnel1\] advpn session idle-time 800]{lang="EN-US"}
:::

::: {#-80890391 .myid}
[]{#_Toc404787417}[]{#struct_0_49241_76394_x856914414}[]{#_Toc375152481}[]{#_Toc375152482}

**ADVPN \-- ADVPN隧道配置命令 \-- advpn source-port**

------------------------------------------------------------------------

[**[advpn source-port]{lang="EN-US"}**]{#struct_0_49241_76394_x62185341}[命令用来配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号。]{style="font-family:宋体"}

[**[undo advpn source-port]{lang="EN-US"}**]{#struct_0_49241_76394_x1632280659}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_843627122}

[**[advpn source-port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_49241_76394_2134446879}

[**[undo advpn sourc-port]{lang="EN-US"}**]{#struct_0_49241_76394_x1898242073}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_1864244966}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1528420740}[报文的源]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[18001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1233275611}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_269107278}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x203267331}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1529892494}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1238703126}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1787131561}

[*[port-number]{lang="EN-US"}*]{#struct_0_49241_76394_656903568}[：端口号，取值范围为]{style="font-family:宋体"}[1025]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_673938773}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令只有在]{style="font-family:宋体"}]{#struct_0_49241_76394_x279930588}[UDP]{lang="EN-US"}[封装模式的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口下才能配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_x1147338004}[接口]{lang="EN-US" style="font-family:宋体"}[下]{style="font-family:宋体"}[通过]{lang="EN-US" style="font-family:宋体"}**[vam client]{lang="EN-US"}**[命令配置了]{lang="EN-US" style="font-family:宋体"}**[compatible]{lang="EN-US"}**[参数，则该]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口配置的源端口号不能和其他]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的源端口号相同。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1728214900}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_2134381343}[配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[6000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_12030808}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-Tunnel1\] advpn source-port 6000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1430318035}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam client]{lang="EN-US"}**]{#struct_0_49241_76394_x1243205411}
:::

::: {#616815840 .myid}
[]{#_Toc404787418}[]{#struct_0_49241_76394_286865489}

**ADVPN \-- ADVPN隧道配置命令 \-- display advpn ipv6 session**

------------------------------------------------------------------------

[**[display advpn ipv6 session]{lang="EN-US"}**]{#struct_0_49241_76394_61086194}[命令用来显示]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1527436107}

[**[display]{lang="EN-US"}**[ **advpn** **ipv6** **session** \[ **interface** ]{lang="EN-US"}**[tunnel]{lang="EN-US"}**[ *number* \[ **private-address** *private-ipv6-address* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_49241_76394_103457616}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x2121323716}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x1265848966}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1477633876}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_24447788}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_2136397969}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x2035832284}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_951708363}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_2134315807}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ ]{lang="EN-US"}*[number]{lang="EN-US"}*]{#struct_0_49241_76394_x1492926224}[：显示指定]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}[如果未指定本参数，则显示所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ private-]{lang="EN-US"}[ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x233907975}[：显示指定对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}*[private-]{lang="EN-US"}[ipv6-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[隧道对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_49241_76394_x2079292126}[：显示]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的详细信息。如果未指定本参数，则显示]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1620756101}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x73446840}[显示所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session]{lang="EN-US"}]{#struct_0_49241_76394_1478526826}

[Interface         : Tunnel1]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[1001::4               2000::180:137         3546  H-S   Dumb       0H 0M 27S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel2]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1002::4               202.0.180.137         \--    S-H   Establish  0H 0M 2S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel3]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1003::4               2003::180:137         2057  S-S   Success    1H 12M 26S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel4]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1004::4               204.1.181:157         \--    H-H   Success    10H 48M 19S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel5]{lang="EN-US"}

[Number of sessions: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1745809412}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_2134250271}

[Interface         : Tunnel1]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[1001::4               2000::180:137         3546  H-S   Dumb       0H 0M 27S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_404555859}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[1001::3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session interface tunnel 1 private-address 1001::3]{lang="EN-US"}]{#struct_0_49241_76394_x1017916475}

[Private address       Public address        Port  Type  State      Holding time]{lang="EN-US"}

[1001::3               2000::180:136         1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[[表1-12 ]{lang="EN-US"}[display advpn ipv6 session]{lang="EN-US"}]{#struct_0_49241_76394_x1217106020}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_419378432}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x743789204}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_2023500515}

[[Interface]{lang="EN-US"}]{#struct_0_49241_76394_x1349769343}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2053361225}[隧道接口]{style="font-family:宋体"}

[[Number of seesions]{lang="EN-US"}]{#struct_0_49241_76394_x670471732}

[[隧道接口下建立的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x2042851866}[隧道总数]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_2134184735}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1180382666}[隧道对端的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_x527987107}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x532181727}[隧道对端的公网地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_49241_76394_x547787402}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1565930903}[隧道对端的端口号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_267232703}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_511799020}[隧道的类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H-H]{lang="EN-US"}]{#struct_0_49241_76394_1731130138}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H-S]{lang="EN-US"}]{#struct_0_49241_76394_2134119199}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S-H]{lang="EN-US"}]{#struct_0_49241_76394_761018493}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S-S]{lang="EN-US"}]{#struct_0_49241_76394_x850215448}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_49241_76394_x828003620}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x481206713}[隧道的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Success]{lang="EN-US"}]{#struct_0_49241_76394_948907389}[：]{style="font-family:宋体"}[表示隧道]{lang="EN-US" style="font-family:宋体"}[建立]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Establish]{lang="EN-US"}]{#struct_0_49241_76394_x1582423962}[ing]{lang="EN-US"}[：]{style="font-family:宋体"}[表示隧道正在建立中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dumb]{lang="EN-US"}]{#struct_0_49241_76394_x1181246161}[：表示隧道建立失败后处于静默状态]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_2134053663}

[[当前]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x396722885}[隧道状态的持续时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1066876186}[显示所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session verbose]{lang="EN-US"}]{#struct_0_49241_76394_2134971167}

[Interface         : Tunnel1]{lang="EN-US"}

[Client name       : vpn1]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[  Private address: 1001::3]{lang="EN-US"}

[  Public address : 2000::180:136]{lang="EN-US"}

[  ADVPN port     : 1139 ]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 2198 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 216 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Private address: 1001::4]{lang="EN-US"}

[  Public address : 2000::180:137]{lang="EN-US"}

[  ADVPN port     : 3546]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Dumb]{lang="EN-US"}

[  Holding time   : 0H 0M 27S]{lang="EN-US"}

[  Input : 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 16 packets, 0 data packets, 16 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel2]{lang="EN-US"}

[Client name       : vpn2]{lang="EN-US"}

[ADVPN domain name : 2]{lang="EN-US"}

[Link protocol     : GRE]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 1002::4]{lang="EN-US"}

[  Public address : 202.0.180.137]{lang="EN-US"}

[  Session type   : Spoke-Hub]{lang="EN-US"}

[  State          : Establish ]{lang="EN-US"}

[  Holding time   : 0H 0M 2S]{lang="EN-US"}

[  Input:  0 packets, 0 data packets, 0 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel3]{lang="EN-US"}

[Client name       : vpn3]{lang="EN-US"}

[ADVPN domain name : 3]{lang="EN-US"}

[Link protocol     : IPsec-UDP]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 1003::4]{lang="EN-US"}

[  Public address : 2003::180:137]{lang="EN-US"}

[  ADVPN port     : 2057]{lang="EN-US"}

[  SA\'s SPI       : ]{lang="EN-US"}

[    Inbound : 187199087 (0xb286e6f) \[ESP\]]{lang="EN-US"}

[    Outbound: 3562274487 (0xd453feb7) \[ESP\]]{lang="EN-US"}

[  Session type   : Spoke-Spoke]{lang="EN-US"}

[  State          : Establish]{lang="EN-US"}

[  Holding time   : 0H 0M 2S]{lang="EN-US"}

[  Input:  0 packets, 0 data packets, 0 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel4]{lang="EN-US"}

[Client name       : vpn4]{lang="EN-US"}

[ADVPN domain name : 4]{lang="EN-US"}

[Link protocol     : IPsec-GRE]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 1004::4]{lang="EN-US"}

[  Public address : 204.1.181:157]{lang="EN-US"}

[  SA\'s SPI       :]{lang="EN-US"}

[    Inbound:  187199087 (0xb286e6f) \[ESP\] ]{lang="EN-US"}

[    Outbound: 3562274487 (0xd453feb7) \[ESP\]]{lang="EN-US"}

[  Session type   : Hub-Hub]{lang="EN-US"}

[  State          : Success ]{lang="EN-US"}

[  Holding time   : 10H 48M 19S]{lang="EN-US"}

[  Input : 2201 packets, 2198 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 2168 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel5]{lang="EN-US"}

[Client name       : vpn5]{lang="EN-US"}

[ADVPN domain name : 5]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Number of sessions: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_400593584}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session interface tunnel 1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_x1026911}

[Interface         : Tunnel1]{lang="EN-US"}

[Client name       : vpn1]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[  Private address: 1001::3]{lang="EN-US"}

[  Public address : 2000::180:136]{lang="EN-US"}

[  ADVPN port     : 1139 ]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 2198 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 216 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Private address: 1001::4]{lang="EN-US"}

[  Public address : 2000::180:137]{lang="EN-US"}

[  ADVPN port     : 3546]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Dumb]{lang="EN-US"}

[  Holding time   : 0H 0M 27S]{lang="EN-US"}

[  Input : 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 16 packets, 0 data packets, 16 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_85493570}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[1001::3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn ipv6 session interface tunnel 1 private-address 1001::3 verbose]{lang="EN-US"}]{#struct_0_49241_76394_2134512416}

[  Private address: 1001::3]{lang="EN-US"}

[  Public address : 2000::180:136]{lang="EN-US"}

[  ADVPN port     : 1139 ]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 2198 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 216 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[[表1-13 ]{lang="EN-US"}[display advpn ipv6 session verbose]{lang="EN-US"}]{#struct_0_49241_76394_x1571491342}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_411590572}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_1217206968}

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x1738871137}

[[Interface]{lang="EN-US"}]{#struct_0_49241_76394_x535898591}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_61114359}[隧道接口]{style="font-family:宋体"}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_1157452368}

[[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_1968126805}[名称]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_1021579087}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2134446880}[域的名称]{style="font-family:宋体"}

[[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x1898831904}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_765729951}[隧道使用的承载链路层协议：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_49241_76394_153697158}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRE]{lang="EN-US"}]{#struct_0_49241_76394_1166384992}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-UDP]{lang="EN-US"}]{#struct_0_49241_76394_x1976359340}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-GRE]{lang="EN-US"}]{#struct_0_49241_76394_299300993}

[[Number of sessions]{lang="EN-US"}]{#struct_0_49241_76394_1995190972}

[[隧道接口下建立的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1069439121}[隧道总数]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_2134381344}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_12358488}[隧道对端的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_215591470}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2076067035}[隧道对端的公网地址]{style="font-family:宋体"}

[[ADVPN port]{lang="EN-US"}]{#struct_0_49241_76394_1461088144}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_682340088}[隧道使用的承载链路层协议为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时，隧道的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[SA\'s SPI]{lang="EN-US"}]{#struct_0_49241_76394_x806742561}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1607727027}[隧道使用的承载链路层协议为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时，出方向和入方向的安全策略索引]{style="font-family:宋体"}

[[Session type]{lang="EN-US"}]{#struct_0_49241_76394_x1781760771}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2134315808}[隧道的类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub-Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1493778192}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub-Spoke]{lang="EN-US"}]{#struct_0_49241_76394_907256750}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke-Hub]{lang="EN-US"}]{#struct_0_49241_76394_x1798268525}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke-Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x254933800}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_49241_76394_x537094883}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_750522170}[隧道的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Success]{lang="EN-US"}]{#struct_0_49241_76394_2134250272}[：]{style="font-family:宋体"}[表示隧道]{lang="EN-US" style="font-family:宋体"}[建立]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Establish]{lang="EN-US"}]{#struct_0_49241_76394_404752467}[ing]{lang="EN-US"}[：]{style="font-family:宋体"}[表示隧道正在建立中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dumb]{lang="EN-US"}]{#struct_0_49241_76394_1292131471}[：表示隧道建立失败后处于静默状态]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_x53419018}

[[当前隧道状态的持续时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}]{#struct_0_49241_76394_x1462443513}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_49241_76394_x939746452}

[[接收的报文统计信息，包括：]{style="font-family:宋体"}]{#struct_0_49241_76394_1013119357}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_49241_76394_2134184736}[：报文总个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[data packets]{lang="EN-US"}]{#struct_0_49241_76394_1180186058}[：数据报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control packets]{lang="EN-US"}]{#struct_0_49241_76394_x1349951346}[：控制报文个数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_49241_76394_x266887593}[：组播报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_49241_76394_x18394612}[：错误报文个数]{style="font-family:宋体"}

[[Output]{lang="EN-US"}]{#struct_0_49241_76394_1663118979}

[[发送的报文统计信息，包括：]{style="font-family:宋体"}]{#struct_0_49241_76394_x699552039}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_49241_76394_2134119200}[：报文总个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[data packets]{lang="EN-US"}]{#struct_0_49241_76394_x1959380874}[：数据报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control packets]{lang="EN-US"}]{#struct_0_49241_76394_196511898}[：控制报文个数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_49241_76394_284536525}[：组播报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_49241_76394_1480710364}[：错误报文个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x617122025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset advpn ipv6 session]{lang="EN-US"}**]{#struct_0_49241_76394_758835429}

::: {#-1158580844 .myid}
[]{#_Toc404787419}[]{#struct_0_49241_76394_2134053664}

**ADVPN \-- ADVPN隧道配置命令 \-- display advpn session**

------------------------------------------------------------------------

[**[display advpn session]{lang="EN-US"}**]{#struct_0_49241_76394_x397050565}[命令用来显示]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1446716735}

[**[display]{lang="EN-US"}**[ **advpn** **session** \[ **interface** **tunnel** *number* \[ **private-address** *private-ip-address* \] \] \[ **verbose** \]]{lang="EN-US"}]{#struct_0_49241_76394_x596670506}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1859049882}

[[任意视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x634178151}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1005549854}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1993109292}

[[network-operator]{lang="EN-US"}]{#struct_0_49241_76394_x637453247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x306292943}

[[mdc-operator]{lang="EN-US"}]{#struct_0_49241_76394_x469891194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_878679658}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_49241_76394_x2137687515}[：显示指定]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。]{style="font-family:宋体"}[如果未指定本参数，则显示所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ ]{lang="EN-US"}[private-ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_x747927211}[：显示指定对端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道信息。]{style="font-family:宋体"}*[private-ip-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[对到对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_49241_76394_x1306867030}[：显示]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的详细信息。如果未指定本参数，则显示]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x92297680}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_2135036704}[显示所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session]{lang="EN-US"}]{#struct_0_49241_76394_x770236572}

[Interface         : Tunnel1]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[10.0.1.4         192.168.180.137             3546  H-S   Dumb       0H 0M 27S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel2]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[20.0.0.3         200::3                      \--     S-H   Establish  0H 0M 2S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel3]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[30.0.0.3         192.168.200.22              2057  S-S   Success    1H 12M 26S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel4]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[40.0.0.3         4::4                        \--    H-H   Success    10H 48M 19S]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel5]{lang="EN-US"}

[Number of sessions: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_30391673}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_705734476}

[Interface         : Tunnel1]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[10.0.1.4         192.168.180.137             3546  H-S   Dumb       0H 0M 27S]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_253114560}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[10.0.1.3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session interface tunnel 1 private-address 10.0.1.3]{lang="EN-US"}]{#struct_0_49241_76394_2134971168}

[Private address  Public address              Port  Type  State      Holding time]{lang="EN-US"}

[10.0.0.3         192.168.180.136             1139  H-S   Success    5H 38M 8S]{lang="EN-US"}

[[表1-14 ]{lang="EN-US"}[display advpn session]{lang="EN-US"}]{#struct_0_49241_76394_401576624}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_406943126}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_x687875647}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x1503687568}

[[Interface]{lang="EN-US"}]{#struct_0_49241_76394_x1881251058}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_826879831}[隧道接口]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_1448069241}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1582080691}[域的名称]{style="font-family:宋体"}

[[Number of sessions]{lang="EN-US"}]{#struct_0_49241_76394_x1172295035}

[[隧道接口下建立的]{style="font-family:宋体"}[A]{lang="EN-US"}]{#struct_0_49241_76394_1915821043}[DVPN]{lang="FR"}[隧道总数]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_x360607866}

[[ADVPN]{lang="FR"}]{#struct_0_49241_76394_2134512413}[隧道对端的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_x1571819022}

[[ADVPN]{lang="FR"}]{#struct_0_49241_76394_x1603178943}[隧道对端的公网地址]{style="font-family:宋体"}

[[Port]{lang="EN-US"}]{#struct_0_49241_76394_506536191}

[[ADVPN]{lang="FR"}]{#struct_0_49241_76394_x1228097657}[隧道对端的端口号]{style="font-family:宋体"}

[[Type]{lang="EN-US"}]{#struct_0_49241_76394_1350023483}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x524433608}[隧道的类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H-H]{lang="EN-US"}]{#struct_0_49241_76394_x809935064}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[H-S]{lang="EN-US"}]{#struct_0_49241_76394_x1397737272}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S-H]{lang="EN-US"}]{#struct_0_49241_76394_2134446877}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[S-S]{lang="EN-US"}]{#struct_0_49241_76394_x1899159577}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_49241_76394_x643700427}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_277942638}[隧道的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Success]{lang="EN-US"}]{#struct_0_49241_76394_x1311382365}[：]{style="font-family:宋体"}[表示隧道]{lang="EN-US" style="font-family:宋体"}[建立]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Establish]{lang="EN-US"}]{#struct_0_49241_76394_x1583942049}[ing]{lang="EN-US"}[：]{style="font-family:宋体"}[表示]{lang="EN-US" style="font-family:宋体"}[隧道]{style="font-family:宋体"}[正在建立中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dumb]{lang="EN-US"}]{#struct_0_49241_76394_1142930880}[：表示隧道建立失败后处于静默状态]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_1711489719}

[[当前隧道状态的持续时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}]{#struct_0_49241_76394_2134381341}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS)]{lang="EN-US"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_12161880}[显示所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session verbose]{lang="EN-US"}]{#struct_0_49241_76394_2134250269}

[Interface         : Tunnel1]{lang="EN-US"}

[Client name       : vpn1]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Link Protocol     : UDP]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[  Private address: 10.0.1.3]{lang="EN-US"}

[  Public address : 192.168.180.136]{lang="EN-US"}

[  ADVPN Port     : 1139]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 218 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 2168 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Private address: 10.0.1.4]{lang="EN-US"}

[  Public address : 192.168.180.137]{lang="EN-US"}

[  ADVPN port     : 3546]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Dumb]{lang="EN-US"}

[  Holding time   : 0H 0M 27S]{lang="EN-US"}

[  Input : 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 16 packets, 0 data packets, 16 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel2]{lang="EN-US"}

[Client name       : vpn2]{lang="EN-US"}

[ADVPN domain name : 2]{lang="EN-US"}

[Link protocol     : GRE]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 20.0.0.3]{lang="EN-US"}

[  Public address : 200::3]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Spoke-Hub]{lang="EN-US"}

[  State          : Establish]{lang="EN-US"}

[  Holding time   : 0H  0M 2S]{lang="EN-US"}

[  Input:  0 packets, 0 data packets, 0 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel3]{lang="EN-US"}

[Client name       : vpn3]{lang="EN-US"}

[ADVPN domain name : 3]{lang="EN-US"}

[Link Protocol     : IPsec-UDP]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 30.0.0.3]{lang="EN-US"}

[  Public address : 192.168.200.32]{lang="EN-US"}

[  ADVPN port     : 2057]{lang="EN-US"}

[  SA\'s SPI       : ]{lang="EN-US"}

[    Inbound:  187199087 (0xb286e6f) \[ESP\]]{lang="EN-US"}

[    Outbound: 3562274487 (0xd453feb7) \[ESP\]]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Spoke-Spoke]{lang="EN-US"}

[  State          : Establish]{lang="EN-US"}

[  Holding time   : 0H  0M 2S]{lang="EN-US"}

[  Input:  0 packets, 0 data packets, 0 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel4]{lang="EN-US"}

[Client name       : vpn4]{lang="EN-US"}

[ADVPN domain name : 4]{lang="EN-US"}

[Link protocol     : IPsec-GRE]{lang="EN-US"}

[Number of sessions: 1]{lang="EN-US"}

[  Private address: 40.0.0.3]{lang="EN-US"}

[  Public address : 4::4]{lang="EN-US"}

[  SA\'s SPI       :]{lang="EN-US"}

[    Inbound:  187199087 (0xb286e6f) \[ESP\]]{lang="EN-US"}

[    Outbound: 3562274487 (0xd453feb7) \[ESP\]]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Hub]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 10H 48M 19S]{lang="EN-US"}

[  Input : 2201 packets, 2198 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 2168 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[Interface         : Tunnel5]{lang="EN-US"}

[Client name       : vpn5]{lang="EN-US"}

[ADVPN domain name : 5]{lang="EN-US"}

[Link protocol     : UDP]{lang="EN-US"}

[Number of sessions: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_405080146}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session interface tunnel 1 verbose]{lang="EN-US"}]{#struct_0_49241_76394_2134184733}

[Interface         : Tunnel1]{lang="EN-US"}

[Client name       : vpn1]{lang="EN-US"}

[ADVPN domain name : 1]{lang="EN-US"}

[Link Protocol     : UDP]{lang="EN-US"}

[Number of sessions: 2]{lang="EN-US"}

[  Private address: 10.0.1.3]{lang="EN-US"}

[  Public address : 192.168.180.136]{lang="EN-US"}

[  ADVPN Port     : 1139 ]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 218 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 2168 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Private address: 10.0.1.4]{lang="EN-US"}

[  Public address : 192.168.180.137]{lang="EN-US"}

[  ADVPN port     : 3546]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Dumb]{lang="EN-US"}

[  Holding time   : 0H 0M 27S]{lang="EN-US"}

[  Input : 1 packets, 0 data packets, 1 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[  Output: 16 packets, 0 data packets, 16 control packets]{lang="EN-US"}

[          0 multicasts, 0 errors]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1179989450}[显示接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[10.0.1.3]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display advpn session verbose interface tunnel 1 private-address 10.0.1.3]{lang="EN-US"}]{#struct_0_49241_76394_x1979901326}

[  Private address: 10.0.1.3]{lang="EN-US"}

[  Public address : 192.168.180.136]{lang="EN-US"}

[  ADVPN Port     : 1139 ]{lang="EN-US"}

[  Behind NAT     : No]{lang="EN-US"}

[  Session type   : Hub-Spoke]{lang="EN-US"}

[  State          : Success]{lang="EN-US"}

[  Holding time   : 5H 38M 8S]{lang="EN-US"}

[  Input : 2201 packets, 218 data packets, 3 control packets]{lang="EN-US"}

[          2191 multicasts, 0 errors]{lang="EN-US"}

[  Output: 2169 packets, 2168 data packets, 1 control packets]{lang="EN-US"}

[          2163 multicasts, 0 errors]{lang="EN-US"}

[[表1-15 ]{lang="EN-US"}[display advpn session verbose]{lang="EN-US"}]{#struct_0_49241_76394_x1736450253}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_409904270}[[字段]{style="font-family:黑体"}]{#struct_0_49241_76394_689747056}

[[描述]{style="font-family:黑体"}]{#struct_0_49241_76394_x2010432854}

[[Interface]{lang="EN-US"}]{#struct_0_49241_76394_177138176}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1083195248}[隧道接口]{style="font-family:宋体"}

[[Client name]{lang="EN-US"}]{#struct_0_49241_76394_240019439}

[[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_2134119197}[名称]{style="font-family:宋体"}

[[ADVPN domain name]{lang="EN-US"}]{#struct_0_49241_76394_761935997}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x658564225}[域的名称]{style="font-family:宋体"}

[[Link protocol]{lang="EN-US"}]{#struct_0_49241_76394_x1527701505}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x891745343}[隧道使用的承载链路层协议：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[UDP]{lang="EN-US"}]{#struct_0_49241_76394_x2069134315}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[GRE]{lang="EN-US"}]{#struct_0_49241_76394_554363728}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-UDP]{lang="EN-US"}]{#struct_0_49241_76394_x1696404344}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec-GRE]{lang="EN-US"}]{#struct_0_49241_76394_x604398240}

[[Number of sessions]{lang="EN-US"}]{#struct_0_49241_76394_2134053661}

[[隧道接口下建立的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x396853957}[隧道总数]{style="font-family:宋体"}

[[Private address]{lang="EN-US"}]{#struct_0_49241_76394_683526355}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x858690572}[隧道对端的私网地址]{style="font-family:宋体"}

[[Public address]{lang="EN-US"}]{#struct_0_49241_76394_x606473524}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_214793416}[隧道对端的公网地址]{style="font-family:宋体"}

[[ADVPN port]{lang="EN-US"}]{#struct_0_49241_76394_x102800486}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1252003346}[隧道使用的承载链路层协议为]{style="font-family:宋体"}[UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[时，隧道的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号]{style="font-family:宋体"}

[[SA\'s SPI]{lang="EN-US"}]{#struct_0_49241_76394_2135036701}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x770564252}[隧道使用的承载链路层协议为]{style="font-family:宋体"}[IPsec-UDP]{lang="EN-US"}[或]{style="font-family:宋体"}[IPsec-GRE]{lang="EN-US"}[时，出方向和入方向的安全策略索引]{style="font-family:宋体"}

[[Behind NAT]{lang="EN-US"}]{#struct_0_49241_76394_1197397198}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_762432868}[隧道对端是否穿越]{style="font-family:宋体"}[NAT]{lang="EN-US"}

[[Session type]{lang="EN-US"}]{#struct_0_49241_76394_19316440}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1459277072}[隧道的类型，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub-Hub]{lang="EN-US"}]{#struct_0_49241_76394_1248663822}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Hub-Spoke]{lang="EN-US"}]{#struct_0_49241_76394_x1055404297}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke-Hub]{lang="EN-US"}]{#struct_0_49241_76394_2134971165}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端是]{lang="EN-US" style="font-family:宋体"}[Hub]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Spoke-Spoke]{lang="EN-US"}]{#struct_0_49241_76394_400724656}[：]{style="font-family:宋体"}[本端是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}[，]{style="font-family:宋体"}[对端也是]{lang="EN-US" style="font-family:宋体"}[Spoke]{lang="EN-US"}

[[State]{lang="EN-US"}]{#struct_0_49241_76394_x910428059}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1405319032}[隧道的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Success]{lang="EN-US"}]{#struct_0_49241_76394_x723108477}[：]{style="font-family:宋体"}[表示隧道]{lang="EN-US" style="font-family:宋体"}[建立]{style="font-family:宋体"}[成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Establish]{lang="EN-US"}]{#struct_0_49241_76394_706848169}[ing]{lang="EN-US"}[：]{style="font-family:宋体"}[表示隧道正在建立中]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Dumb]{lang="EN-US"}]{#struct_0_49241_76394_1570418164}[：表示隧道建立失败后处于静默状态]{style="font-family:宋体"}

[[Holding time]{lang="EN-US"}]{#struct_0_49241_76394_2134512414}

[[当前隧道状态的持续时间，为]{style="font-family:宋体"}[x]{lang="EN-US"}]{#struct_0_49241_76394_x1571622414}[小时]{style="font-family:宋体"}[y]{lang="EN-US"}[分]{style="font-family:宋体"}[z]{lang="EN-US"}[秒（]{style="font-family:宋体"}[xH yM zS]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Input]{lang="EN-US"}]{#struct_0_49241_76394_394722084}

[[接收的报文统计信息，包括：]{style="font-family:宋体"}]{#struct_0_49241_76394_x1995228402}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_49241_76394_1847852795}[：报文总个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[data packets]{lang="EN-US"}]{#struct_0_49241_76394_617240991}[：数据报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control packets]{lang="EN-US"}]{#struct_0_49241_76394_2134446878}[：控制报文个数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_49241_76394_x1898307609}[：组播报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_49241_76394_x1297021878}[：错误报文个数]{style="font-family:宋体"}

[[Output]{lang="EN-US"}]{#struct_0_49241_76394_1787435154}

[[发送的报文统计信息，包括：]{style="font-family:宋体"}]{#struct_0_49241_76394_1368571377}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[packets]{lang="EN-US"}]{#struct_0_49241_76394_45008831}[：报文总个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[data packets]{lang="EN-US"}]{#struct_0_49241_76394_2134381342}[；数据报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[control packets]{lang="EN-US"}]{#struct_0_49241_76394_11965272}[：控制报文个数]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[multicasts]{lang="EN-US"}]{#struct_0_49241_76394_x1771324024}[：组播报文个数]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[errors]{lang="EN-US"}]{#struct_0_49241_76394_x983071502}[：错误报文个数]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_205830305}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset advpn session]{lang="EN-US"}**]{#struct_0_49241_76394_1995422231}

::: {#-317224781 .myid}
[]{#_Toc404787420}[]{#struct_0_49241_76394_x153063692}

**ADVPN \-- ADVPN隧道配置命令 \-- keepalive**

------------------------------------------------------------------------

[**[keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_1817285579}[命令用来配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期及最大发送次数。]{style="font-family:宋体"}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_x648584391}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x529842487}

[**[keepalive ]{lang="EN-US"}[interval]{lang="EN-US"}***[ time-interval]{lang="EN-US"}***[ retry ]{lang="EN-US"}***[retry-times]{lang="EN-US"}*]{#struct_0_49241_76394_1269361433}

[**[undo keepalive]{lang="EN-US"}**]{#struct_0_49241_76394_2134315806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1492860688}

[[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1543425971}[隧道的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期为]{style="font-family:宋体"}[180]{lang="EN-US"}[秒，最大发送次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1072900327}

[[Tunnel]{lang="EN-US"}]{#struct_0_49241_76394_x1394592802}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1505875117}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_902834170}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_187418278}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_551820822}

[**[interval]{lang="EN-US"}***[ time-interval]{lang="EN-US"}*]{#struct_0_49241_76394_1635424568}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的发送周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32767]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[retry ]{lang="EN-US"}***[retry-times]{lang="EN-US"}*]{#struct_0_49241_76394_1767785000}[：]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的最大发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_333748849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_49241_76394_1282126316}[命令只有]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道]{lang="EN-US" style="font-family:宋体"}[类型的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[下]{style="font-family:宋体"}[才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在]{style="font-family:宋体"}]{#struct_0_49241_76394_1727094922}[Keepalive]{lang="EN-US"}[报文发送周期×最大发送次数时间内没有收到]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文，则断开该隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个]{lang="EN-US" style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_2134250270}[域中，所有]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的]{lang="EN-US" style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期及最大发送次数必须一致]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本命令配置之后，]{style="font-family:宋体"}]{#struct_0_49241_76394_404621395}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[定时器并不立即启动，直到]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道建立成功之后才启动。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_2067643007}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x217471650}[配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文发送周期为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒，最大发送次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1679139323}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-Tunnel1\] keepalive interval 20 retry 5]{lang="EN-US"}
:::

::: {#-889780094 .myid}
[]{#_Toc404787421}[]{#struct_0_49241_76394_x1398398828}[]{#_Toc375152487}[]{#_Toc375152488}

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn ipv6 session**

------------------------------------------------------------------------

[**[reset advpn ipv6 session]{lang="EN-US"}**]{#struct_0_49241_76394_x1489801163}[命令用来拆除]{style="font-family:
宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x254463744}

[**[reset]{lang="EN-US"}**[ **advpn** **ipv6** **session** \[ **interface** ]{lang="EN-US"}**[tunnel]{lang="EN-US"}**[ *number* \[ **private-address** *private-ipv6-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_x588606276}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x599970204}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_1097148041}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_240169914}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_681259298}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_1190854045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_2134184734}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ ]{lang="EN-US"}*[number]{lang="EN-US"}*]{#struct_0_49241_76394_1180317130}[：拆除指定]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。如果未指定本参数，则拆除所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ private-ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_x566962839}[：拆除指定对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[private-ipv6-address]{lang="EN-US"}*[为隧道对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。如未指定本参数，则拆除指定或所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的所有]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1438381345}

[[如果隧道对端是]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1388975181}[，且与本端在同一个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内，隧道拆除后将重新建立隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1858780506}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x612817744}[拆除所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session]{lang="EN-US"}]{#struct_0_49241_76394_986007479}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1682357305}[拆除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上的所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_x1413034914}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x174871336}[拆除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[1000::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session interface tunnel 1 private-address 1000::1]{lang="EN-US"}]{#struct_0_49241_76394_x546337175}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_774752766}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ advpn ]{lang="EN-US"}**]{#struct_0_49241_76394_x2074746177}**[ipv6 ]{lang="EN-US"}[session]{lang="EN-US"}**
:::

::: {#1806720111 .myid}
[]{#_Toc404787422}[]{#struct_0_49241_76394_2134119198}

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn ipv6 session statistics**

------------------------------------------------------------------------

[**[reset advpn ipv6 session statistic]{lang="EN-US"}**]{#struct_0_49241_76394_761084029}[命令用来清除]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x46535521}

[**[reset]{lang="EN-US"}**[ **advpn** **ipv6** **session** **statistics** \[ **interface** **tunnel** *number* \[ **private-address** *private-ipv6-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_791177195}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_x477071812}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_16026879}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x287608324}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_376414290}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_465450080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1231286224}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ ]{lang="EN-US"}*[number]{lang="EN-US"}*]{#struct_0_49241_76394_x181790160}[：清除指定]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。如果未指定本参数，则清除所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ private-]{lang="EN-US"}[ipv6-address]{lang="EN-US"}*]{#struct_0_49241_76394_220677387}[：清除指定对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}*[private-]{lang="EN-US"}[ipv6-address]{lang="EN-US"}*[为隧道对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网地址。如果未指定本参数，则清除指定或所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_146580148}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1162885273}[清除所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session statistics]{lang="EN-US"}]{#struct_0_49241_76394_1756822828}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_2134053662}[清除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session statistics interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_x396657349}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_625187590}[清除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[1::1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn ipv6 session statistics interface tunnel 1 private-address 1::1]{lang="EN-US"}]{#struct_0_49241_76394_497271181}
:::

::: {#-504997130 .myid}
[]{#_Toc404787423}[]{#struct_0_49241_76394_502705101}

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn session**

------------------------------------------------------------------------

[**[reset advpn session]{lang="EN-US"}**]{#struct_0_49241_76394_x816146570}[命令用来删除]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_2021899083}

[**[reset]{lang="EN-US"}**[ **advpn** **session** \[ **interface** ]{lang="EN-US"}**[tunnel]{lang="EN-US"}**[ *number* \[ **private-address** *private-ip-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_x1272758318}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_716690662}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x461572397}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1684927900}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1099356850}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x410303997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1685156980}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_49241_76394_201547904}[：删除指定]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。如果未指定本参数，则删除所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ private-]{lang="EN-US"}[ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_2135036702}[：删除指定对端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}*[private-]{lang="EN-US"}[ip-address]{lang="EN-US"}*[为隧道对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。如果未指定本参数，则删除指定或所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上的所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_x770629788}

[[如果隧道对端是]{style="font-family:宋体"}[Hub]{lang="EN-US"}]{#struct_0_49241_76394_1671227733}[，且与本端在同一个]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内，隧道删除后将重新建立。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1690010546}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1910501551}[删除所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session]{lang="EN-US"}]{#struct_0_49241_76394_1019713928}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x1759598859}[删除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_515915960}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x599440341}[删除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[169.254.0.1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session interface tunnel 1 private-address 169.254.0.1]{lang="EN-US"}]{#struct_0_49241_76394_x1239669208}

[]{#_Toc323022609}[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1080705678}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ advpn session]{lang="EN-US"}**]{#struct_0_49241_76394_1620753951}
:::

::: {#399921363 .myid}
[]{#_Toc404787424}[]{#struct_0_49241_76394_x843280054}

**ADVPN \-- ADVPN隧道配置命令 \-- reset advpn session statistics**

------------------------------------------------------------------------

[**[reset advpn session statistic]{lang="EN-US"}**]{#struct_0_49241_76394_454693031}[命令用来清除]{style="font-family:
宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_1917988234}

[**[reset]{lang="EN-US"}**[ **advpn** **session** **statistics** \[ **interface** **tunnel** *number* \[ **private-address** *private-ip-address* \] \]]{lang="EN-US"}]{#struct_0_49241_76394_2134971166}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_400659120}

[[用户视图]{style="font-family:宋体"}]{#struct_0_49241_76394_x944143451}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_2035391533}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1768723293}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x1419005630}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1062749090}

[**[interface]{lang="EN-US"}***[ ]{lang="EN-US"}***[tunnel]{lang="EN-US"}**[ ]{lang="EN-US"}*[number]{lang="EN-US"}*]{#struct_0_49241_76394_x844287368}[：清除指定]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[类型]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}*[number]{lang="EN-US"}*[为]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口的编号。如果未指定本参数，则清除所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[**[private-address]{lang="EN-US"}***[ private-]{lang="EN-US"}[ip-address]{lang="EN-US"}*]{#struct_0_49241_76394_1134479775}[：清除指定对端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}*[private-]{lang="EN-US"}[ip-address]{lang="EN-US"}*[为隧道对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网地址。如果未指定本参数，则清除指定或所有]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1139295441}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_903925338}[清除所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session statistics]{lang="EN-US"}]{#struct_0_49241_76394_x870406264}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x781664729}[清除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上所有]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session statistics interface tunnel 1]{lang="EN-US"}]{#struct_0_49241_76394_1739659157}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_1593918738}[清除接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[上对端私网地址为]{style="font-family:宋体"}[169.254.0.1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset advpn session statistics interface tunnel 1 private-address 169.254.0.1]{lang="EN-US"}]{#struct_0_49241_76394_2134512411}
:::

::: {#-321628180 .myid}
[]{#_Toc404787425}[]{#struct_0_49241_76394_x1571950094}

**ADVPN \-- ADVPN隧道配置命令 \-- vam client**

------------------------------------------------------------------------

[**[vam client]{lang="EN-US"}**]{#struct_0_49241_76394_x1269865185}[命令用来配置]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vam client]{lang="EN-US"}**]{#struct_0_49241_76394_x1934052221}[命令用来取消]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x150466802}

[**[vam client ]{lang="EN-US"}***[client-name]{lang="EN-US"}*[ \[ ]{lang="EN-US"}**[compatible]{lang="EN-US"}**[ **advpn0** \]]{lang="EN-US"}]{#struct_0_49241_76394_x742902041}

[**[undo vam client]{lang="EN-US"}**]{#struct_0_49241_76394_1651910776}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_2121212910}

[[IPv4 ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1329860692}[隧道接口没有绑定任何]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_626995935}

[[Tunnel]{lang="FR"}]{#struct_0_49241_76394_1056966324}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_216557638}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1239810824}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x248507371}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1345309227}

[*[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_2134446875}[：绑定的]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[的]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[63]{lang="PT-BR"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="PT-BR"}[、]{style="font-family:宋体"}[a-z]{lang="PT-BR"}[、]{style="font-family:宋体"}[0-9]{lang="PT-BR"}[和"]{style="font-family:宋体"}[.]{lang="PT-BR"}["。]{style="font-family:宋体"}

[**[compatible]{lang="EN-US"}**[ **advpn0**]{lang="EN-US"}]{#struct_0_49241_76394_x1899028505}[：兼容]{style="font-family:宋体"}[ADVPN V0]{lang="EN-US"}[版本报文格式。如果未指定本参数，则不兼容]{style="font-family:宋体"}[ADVPN V0]{lang="EN-US"}[版本报文格式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_196373368}

[[对于]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x70602444}[隧道，需要配置此命令将隧道接口与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[绑定。绑定后，]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[会向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册相应隧道接口的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_x1592278299}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_49241_76394_2044257046}[命令只有]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[ADVPN]{lang="EN-US"}[类型的]{style="font-family:
宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:
宋体"}[下]{style="font-family:宋体"}[才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x1344344056}[只能]{lang="EN-US" style="font-family:宋体"}[与]{style="font-family:宋体"}[一个]{lang="EN-US" style="font-family:宋体"}[IPv4 ]{lang="EN-US"}[ADVPN]{lang="EN-US"}[类型的]{style="font-family:
宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:
宋体"}[绑定]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果]{style="font-family:宋体"}]{#struct_0_49241_76394_x1668633406}[Tunnel]{lang="EN-US"}[接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[所在的]{style="font-family:宋体"}[Hub]{lang="EN-US"}[组内中有仅支持]{style="font-family:宋体"}[ADVPN V0]{lang="EN-US"}[版本报文格式的设备，则必须配置]{style="font-family:宋体"}**[compatible]{lang="EN-US"}**[参数。配置了]{style="font-family:宋体"}**[compatible]{lang="EN-US"}**[参数后，]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口上配置的]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[报文源]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号必须和其他]{lang="EN-US" style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口不同。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_x560086305}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x761734143}[配置]{style="font-family:宋体"}[IPv4 ADVPN]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[与]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_x1270090794}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv4]{lang="EN-US"}

[\[Sysname-Tunnel1\] vam client abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_648597148}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam ipv6 client]{lang="EN-US"}**]{#struct_0_49241_76394_x2050175193}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[advpn source-port]{lang="EN-US"}**]{#struct_0_49241_76394_x827865707}
:::

::: {#-1105075772 .myid}
[]{#_Toc404787426}[]{#struct_0_49241_76394_2134381339}

**ADVPN \-- ADVPN隧道配置命令 \-- vam ipv6 client**

------------------------------------------------------------------------

[**[vam ipv6 client]{lang="EN-US"}**]{#struct_0_49241_76394_12686173}[命令用来配置]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vam ipv6 client]{lang="EN-US"}**]{#struct_0_49241_76394_x814058422}[命令用来取消]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道接口绑定的]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1386711405}

[**[vam ipv6 client ]{lang="EN-US"}***[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_62492136}

[**[undo vam ipv6 client]{lang="EN-US"}**]{#struct_0_49241_76394_1852358295}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_49241_76394_1693698565}

[[IPv6 ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_1988670348}[隧道接口没有绑定任何]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_49241_76394_1356494636}

[[Tunnel]{lang="FR"}]{#struct_0_49241_76394_x555855326}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_49241_76394_x1694979065}

[[network-admin]{lang="EN-US"}]{#struct_0_49241_76394_1074126073}

[[mdc-admin]{lang="EN-US"}]{#struct_0_49241_76394_x363728755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_49241_76394_1284734092}

[*[client-name]{lang="EN-US"}*]{#struct_0_49241_76394_434653558}[：绑定的]{style="font-family:宋体"}[VAM Client]{lang="PT-BR"}[的]{style="font-family:宋体"}[名称，为]{style="font-family:宋体"}[1]{lang="PT-BR"}[～]{style="font-family:宋体"}[63]{lang="PT-BR"}[个字符的字符串，不区分大小写，只能包含字符]{style="font-family:宋体"}[A-Z]{lang="PT-BR"}[、]{style="font-family:宋体"}[a-z]{lang="PT-BR"}[、]{style="font-family:宋体"}[0-9]{lang="PT-BR"}[和"]{style="font-family:宋体"}[.]{lang="PT-BR"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_49241_76394_2134315803}

[[对于]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}]{#struct_0_49241_76394_x1493188368}[隧道，需要配置此命令将隧道接口与]{style="font-family:宋体"}[VAM Client]{lang="EN-US"}[绑定。绑定之后，]{style="font-family:宋体"} [VAM Client]{lang="EN-US"}[会向]{style="font-family:宋体"}[VAM Server]{lang="EN-US"}[注册相应隧道接口的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网信息。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_49241_76394_x305243535}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本]{style="font-family:宋体"}]{#struct_0_49241_76394_422149154}[命令只有]{lang="EN-US" style="font-family:宋体"}[在]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[下]{style="font-family:宋体"}[才能配置。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{lang="EN-US" style="font-family:宋体"}[VAM Client]{lang="EN-US"}]{#struct_0_49241_76394_x579234816}[只能]{lang="EN-US" style="font-family:宋体"}[与]{style="font-family:宋体"}[一个]{lang="EN-US" style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[类型的]{style="font-family:宋体"}[Tunnel]{lang="EN-US"}[接口]{lang="EN-US" style="font-family:宋体"}[绑定]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_49241_76394_1159255113}

[[\# ]{lang="EN-US"}]{#struct_0_49241_76394_x943595957}[配置]{style="font-family:宋体"}[IPv6 ADVPN]{lang="EN-US"}[隧道接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[与]{style="font-family:宋体"}[VAM Client abc]{lang="EN-US"}[绑定。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_49241_76394_1077261155}

[\[Sysname\] interface tunnel 1 mode advpn udp ipv6]{lang="EN-US"}

[\[Sysname-Tunnel1\] vam ipv6 client abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_49241_76394_713015473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vam client]{lang="EN-US"}**]{#struct_0_49241_76394_x881514227}
:::
