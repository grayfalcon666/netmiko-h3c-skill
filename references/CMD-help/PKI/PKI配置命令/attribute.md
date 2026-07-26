::: {#-136546062 .myid}
[]{#_Toc279163110}[]{#_Toc404793057}[]{#struct_0_18308_19795_x994418565}

**PKI \-- PKI配置命令 \-- attribute**

------------------------------------------------------------------------

[[[attribute]{lang="EN-US"}]{.commandkeywordsCharChar}]{#struct_0_18308_19795_x84273901}[命令用来配置属性规则，用于根据证书的颁发者名、主题名以及备用主题名来过滤证书。]{style="font-family:宋体"}

[**[undo attribute]{lang="EN-US"}**]{#struct_0_18308_19795_x1555748123}[命令用来删除证书属性规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x695288998}

[**[attribute]{lang="EN-US"}**[ *id* { **alt-subject-name** { **fqdn** \| **ip** } \| { **issuer-name** \| **subject-name** } { **dn** \| **fqdn** \| **ip** } } { **ctn** \| **equ** \| **nctn** \| **nequ** } *attribute-value*]{lang="EN-US"}]{#struct_0_18308_19795_x44269405}

[**[undo]{lang="EN-US"}**[ **attribute** *id*]{lang="EN-US"}]{#struct_0_18308_19795_823279399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x173825229}

[[不存在属性规则，即对证书的颁发者名、主题名以及备用主题名没有限制。]{style="font-family:宋体"}]{#struct_0_18308_19795_x28221226}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1352358668}

[[证书属性组视图]{style="font-family:宋体"}]{#struct_0_18308_19795_84789770}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1661562145}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x84339437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x291881336}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x748113393}

[*[id]{lang="EN-US"}*]{#struct_0_18308_19795_x1125802970}[：证书属性规则序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[alt-subject-name]{lang="EN-US"}**]{#struct_0_18308_19795_x337991912}[：表示证书备用主题名（]{style="font-family:宋体"}[Subject Alternative Name]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[fqdn]{lang="EN-US"}**]{#struct_0_18308_19795_x1848873378}[：指定实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ip]{lang="EN-US"}**]{#struct_0_18308_19795_x1447878551}[：指定实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[dn]{lang="EN-US"}**]{#struct_0_18308_19795_1702768531}[：指定实体的]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[issuer-name]{lang="EN-US"}**]{#struct_0_18308_19795_995346525}[：表示证书颁发者名（]{style="font-family:宋体"}[Issuer Name]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[subject-name]{lang="EN-US"}**]{#struct_0_18308_19795_x83880685}[：表示证书主题名（]{style="font-family:宋体"}[Subject Name]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[ctn]{lang="EN-US"}**]{#struct_0_18308_19795_x1552221732}[：表示包含操作。]{style="font-family:宋体"}

[**[equ]{lang="EN-US"}**]{#struct_0_18308_19795_x1139994164}[：表示相等操作。]{style="font-family:宋体"}

[**[nctn]{lang="EN-US"}**]{#struct_0_18308_19795_x973392955}[：表示不包含操作。]{style="font-family:宋体"}

[**[nequ]{lang="EN-US"}**]{#struct_0_18308_19795_x1436685479}[：表示不等操作。]{style="font-family:宋体"}

[*[attribute-value]{lang="EN-US"}*]{#struct_0_18308_19795_x1118050694}[：指定证书属性值，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_259045581}

[[各证书属性中可包含的属性域个数有所不同：]{style="font-family:宋体"}]{#struct_0_18308_19795_888187519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主题名和颁发者名中均只能包含一个]{style="font-family:宋体"}]{#struct_0_18308_19795_1701435651}[DN]{lang="EN-US"}[，但是均可以同时包含多个]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[备用主题名中不能包含]{style="font-family:宋体"}]{#struct_0_18308_19795_x33002903}[DN]{lang="EN-US"}[，但是可以同时包含多个]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[和]{style="font-family:宋体"}[IP]{lang="EN-US"}[。]{style="font-family:宋体"}

[[不同类型的证书属性域与操作关键字的组合代表了不同的匹配条件，具体如下表所示：]{style="font-family:宋体"}]{#struct_0_18308_19795_x83946221}

[[表1-1 ]{lang="EN-US"}[对证书属性域的操作涵义]{style="font-family:黑体"}]{#struct_0_18308_19795_397396936}

[]{#table_struct_0_1967601276}[[操作]{style="font-family:黑体"}]{#struct_0_18308_19795_x263319055}
:::

[[DN]{lang="EN-US"}]{#struct_0_18308_19795_1887563947}

[[FQDN/IP]{lang="EN-US"}]{#struct_0_18308_19795_542310960}

[**[ctn]{lang="EN-US"}**]{#struct_0_18308_19795_x892126160}

[[DN]{lang="EN-US"}]{#struct_0_18308_19795_x1016852782}[中包含指定的属性值]{style="font-family:宋体"}

[[任意一个]{style="font-family:宋体"}[FQDN/IP]{lang="EN-US"}]{#struct_0_18308_19795_418120775}[中包含了指定的属性值]{style="font-family:宋体"}

[**[nctn]{lang="EN-US"}**]{#struct_0_18308_19795_x84011757}

[[DN]{lang="EN-US"}]{#struct_0_18308_19795_205113791}[中不包含指定的属性值]{style="font-family:宋体"}

[[所有]{style="font-family:宋体"}[FQDN/IP]{lang="EN-US"}]{#struct_0_18308_19795_x522786831}[中均不包含指定的属性值]{style="font-family:宋体"}

[**[equ]{lang="EN-US"}**]{#struct_0_18308_19795_524032065}

[[DN]{lang="EN-US"}]{#struct_0_18308_19795_1896297210}[等于指定的属性值]{style="font-family:宋体"}

[[任意一个]{style="font-family:宋体"}[FQDN/IP]{lang="EN-US"}]{#struct_0_18308_19795_x843526775}[等于指定的属性值]{style="font-family:宋体"}

[**[nequ]{lang="EN-US"}**]{#struct_0_18308_19795_x84077293}

[[DN]{lang="EN-US"}]{#struct_0_18308_19795_x975820738}[不等于指定的属性值]{style="font-family:宋体"}

[[所有]{style="font-family:宋体"}[FQDN/IP]{lang="EN-US"}]{#struct_0_18308_19795_329974532}[均不等于指定的属性值]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[如果证书的相应属性中包含了属性规则里指定的属性域，且满足属性规则中定义的匹配条件，则认为该属性与属性规则相匹配。例如：属性规则]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_18308_19795_x1310937571}[中定义，证书的主题名]{style="font-family:宋体"}[DN]{lang="EN-US"}[中包含字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[。如果某证书的主题名的]{style="font-family:宋体"}[DN]{lang="EN-US"}[中确实包含了字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[，则认为该证书的主题名与属性规则]{style="font-family:宋体"}[2]{lang="EN-US"}[匹配。]{style="font-family:宋体"}

[[只有证书中的相应属性与某属性组中的所有属性规则都匹配上，才认为该证书与此属性组匹配。如果证书中的某属性中没有包含属性规则中指定的属性域，或者不满足属性规则中的匹配条件，则认为该证书与此属性组不匹配。]{style="font-family:宋体"}]{#struct_0_18308_19795_x566137061}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_835866875}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1503141067}

[\[Sysname\] pki certificate attribute-group mygroup]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x2088215226}[创建证书属性规则]{style="font-family:宋体"}[1]{lang="EN-US"}[，定义证书主题名中的]{style="font-family:宋体"}[DN]{lang="EN-US"}[包含字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-pki-cert-attribute-group-mygroup\] attribute 1 subject-name dn ctn abc]{lang="EN-US"}]{#struct_0_18308_19795_x83618541}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1800575754}[创建证书属性规则]{style="font-family:宋体"}[2]{lang="EN-US"}[，定义证书颁发者名中的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[不等于字符串]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-pki-cert-attribute-group-mygroup\] attribute 2 issuer-name fqdn nequ abc]{lang="EN-US"}]{#struct_0_18308_19795_1896376907}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x2011151866}[创建证书属性规则]{style="font-family:宋体"}[3]{lang="EN-US"}[，定义证书主题备用名中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不等于]{style="font-family:宋体"}[10.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-pki-cert-attribute-group-mygroup\] attribute 3 alt-subject-name ip nequ 10.0.0.1]{lang="EN-US"}]{#struct_0_18308_19795_x1067657755}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x407126072}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_1915017744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_18308_19795_x391677500}

::: {#1879658822 .myid}
[]{#_Toc404793058}[]{#struct_0_18308_19795_x927229182}

**PKI \-- PKI配置命令 \-- ca identifier**

------------------------------------------------------------------------

[**[ca identifier]{lang="EN-US"}**]{#struct_0_18308_19795_x83684077}[命令用来指定设备信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}[的名称。]{style="font-family:宋体"}

[**[undo ca identifier]{lang="EN-US"}**]{#struct_0_18308_19795_960160532}[命令用来删除设备信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1389590444}

[**[ca identifier]{lang="EN-US"}**[ *name*]{lang="EN-US"}]{#struct_0_18308_19795_1791378038}

[**[undo ca identifier]{lang="EN-US"}**]{#struct_0_18308_19795_x1210207244}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1369758203}

[[未指定设备信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_468692627}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x364754342}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1220283441}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x821790818}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x84142828}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_906737198}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_2100553370}

[*[name]{lang="EN-US"}*]{#struct_0_18308_19795_x1542806798}[：设备信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1900601575}

[[获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x1664628964}[证书时，必须指定信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}[的名称，这个名称会被作为]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[消息的一部分发送给]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器。但是一般情况下，]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器会忽略收到的]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[消息中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[名称的具体内容。但是如果在同一台服务器上配置了两个]{style="font-family:宋体"}[CA]{lang="EN-US"}[，且它们的]{style="font-family:宋体"}[URL]{lang="EN-US"}[是相同的，则服务器将根据]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[消息中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[名称选择对应的]{style="font-family:宋体"}[CA]{lang="EN-US"}[。因此，使用此命令指定的]{style="font-family:宋体"}[CA]{lang="EN-US"}[名称必须与希望获取的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书对应的]{style="font-family:宋体"}[CA]{lang="EN-US"}[名称一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x632783647}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1656465580}[指定设备信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}[的名称为]{style="font-family:宋体"}[new-ca]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x84208364}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] ca identifier new-ca]{lang="EN-US"}
:::

::: {#783013567 .myid}
[]{#_Toc404793059}[]{#struct_0_18308_19795_857316299}[]{#_Toc279490418}[]{#_Toc265512448}

**PKI \-- PKI配置命令 \-- certificate request entity**

------------------------------------------------------------------------

[**[certificate request entity]{lang="EN-US"}**]{#struct_0_18308_19795_2067675117}[命令用来指定用于申请证书]{style="font-family:
宋体"}[的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实]{style="font-family:宋体"}[体名称。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **certificate request entity**]{lang="EN-US"}]{#struct_0_18308_19795_x1399550315}[命令用来取消用于申请证书的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1215304434}

[**[certificate request entity]{lang="EN-US"}**[ *entity-name*]{lang="EN-US"}]{#struct_0_18308_19795_730912695}

[**[undo]{lang="EN-US"}**[ **certificate request entity**]{lang="EN-US"}]{#struct_0_18308_19795_1633481592}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1068408836}

[[未指定设备申请证书所使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1182248561}[实体名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1019030818}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x84273900}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1555748124}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_870794943}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1582409713}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1896238934}

[*[entity-name]{lang="EN-US"}*]{#struct_0_18308_19795_771929108}[：用于申请证书的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x410945847}

[[本命令用于在]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1450889009}[域中指定申请证书的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体。]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体描述了申请证书的实体的各种属性（通用名、组织部门、组织、地理区域、省、国家、]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[），这些属性用于描述]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的身份信息。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_318718753}[域中只能指定一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体名，新配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体名会覆盖已有的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体名。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x84339436}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x291881337}[指定申请证书的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的名称为]{style="font-family:宋体"}[en1]{lang="FR"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x748178929}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request entity en1]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x435243612}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki entity]{lang="EN-US"}**]{#struct_0_18308_19795_1099716235}
:::

::: {#475422690 .myid}
[]{#_Toc404793060}[]{#struct_0_18308_19795_x1548861051}

**PKI \-- PKI配置命令 \-- certificate request from**

------------------------------------------------------------------------

[**[certificate request from]{lang="EN-US"}**]{#struct_0_18308_19795_x2129851945}[命令用来配置证书申请的注册受理机构。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **certificate request from**]{lang="EN-US"}]{#struct_0_18308_19795_1886077982}[命令用来删除指定的证书申请注册受理机构。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x586033861}

[**[certificate request from ]{lang="EN-US"}**[{ **ca** \| **ra** }]{lang="EN-US"}]{#struct_0_18308_19795_x83880684}

[**[undo certificate request from]{lang="EN-US"}**]{#struct_0_18308_19795_x1552221731}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x736709637}

[[未指定证书申请的注册受理机构。]{style="font-family:宋体"}]{#struct_0_18308_19795_x584183057}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x703737914}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x118403244}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1971352784}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x581755304}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1103268883}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x83946220}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_397396937}[：表示实体从]{style="font-family:宋体"}[CA]{lang="EN-US"}[申请证书。]{style="font-family:宋体"}

[**[ra]{lang="EN-US"}**]{#struct_0_18308_19795_x263319054}[：表示实体从]{style="font-family:宋体"}[RA]{lang="EN-US"}[申请证书。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1887498411}

[[选择从]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x1300573675}[还是]{style="font-family:宋体"}[RA]{lang="EN-US"}[申请证书，由]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器决定，需要了解]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器上由什么机构来受理证书申请。]{style="font-family:宋体"}

[[推荐使用独立运行的]{style="font-family:宋体"}[RA]{lang="EN-US"}]{#struct_0_18308_19795_1605795014}[作为注册受理机构。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1087924878}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1143715654}[指定实体从]{style="font-family:宋体"}[RA]{lang="EN-US"}[申请证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_178647852}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request from ra]{lang="EN-US"}
:::

::: {#-367030232 .myid}
[]{#_Toc404793061}[]{#struct_0_18308_19795_x84011756}

**PKI \-- PKI配置命令 \-- certificate request mode**

------------------------------------------------------------------------

[**[certificate request mode]{lang="EN-US"}**]{#struct_0_18308_19795_205113790}[命令用来配置证书申请方式]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[**[undo certificate request mode]{lang="EN-US"}**]{#struct_0_18308_19795_x522786830}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_523966529}

[**[certificate request mode]{lang="EN-US"}**[ { **auto** \[ **password** { **cipher** \| **simple** } *password* \] \| **manual** }]{lang="EN-US"}]{#struct_0_18308_19795_2134228429}

[**[undo certificate request mode]{lang="EN-US"}**]{#struct_0_18308_19795_1926737198}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x122110243}

[[证书申请方式为手工方式。]{style="font-family:宋体"}]{#struct_0_18308_19795_x393740079}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x274782649}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1832643540}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x84077292}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x975820739}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_330040068}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2048123932}

[**[auto]{lang="EN-US"}**]{#struct_0_18308_19795_x569006606}[：表示用自动方式申请证书。]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**]{#struct_0_18308_19795_x891560959}[：指定吊销证书时使用的口令。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_18308_19795_712713739}[：表示以密文方式设置口令。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_18308_19795_x606100055}[：表示以明文方式设置口令。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_18308_19795_x170659623}[：设置的明文或密文口令，区分大小写。明文口令为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，密文口令为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[73]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_18308_19795_x83618540}[：表示用手工方式申请证书。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1800575753}

[[两种申请方式都属于在线申请，具体情况如下：]{style="font-family:宋体"}]{#struct_0_18308_19795_1896573515}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果是自动方式，则设备会在与]{style="font-family:宋体"}]{#struct_0_18308_19795_x476513734}[PKI]{lang="EN-US"}[域关联的应用（例如]{style="font-family:宋体"}[IKE]{lang="EN-US"}[）需要做身份认证时，自动向证书注册机构发起获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书和申请本地证书的操作。自动方式下，可以指定吊销证书时使用的口令，是否需要指定口令是由]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器的策略决定的。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果为手工方式，则需要手工完成获取]{style="font-family:宋体"}]{#struct_0_18308_19795_x1947764998}[CA]{lang="EN-US"}[证书、申请本地证书的操作。]{style="font-family:宋体"}

[[以明文或密文方式设置的口令，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_18308_19795_961628016}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x843111696}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x740391585}[指定证书申请方式为自动方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x83684076}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request mode auto]{lang="FR"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_960160533}[指定证书申请方式为自动方式，并设置吊销证书时使用的口令为明文]{style="font-family:宋体"}[123456]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1389590443}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request mode auto password simple 123456]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_225294097}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki request-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1116411712}
:::

::: {#-362160121 .myid}
[]{#_Toc404793062}[]{#struct_0_18308_19795_2102628357}

**PKI \-- PKI配置命令 \-- certificate request polling**

------------------------------------------------------------------------

[**[certificate request polling]{lang="EN-US"}**]{#struct_0_18308_19795_x1700938616}[命令用来配置证书申请状态的查询周期和最大次数。]{style="font-family:
宋体"}

[**[undo certificate request polling]{lang="EN-US"}**]{#struct_0_18308_19795_112990191}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1230657707}

[**[certificate request polling ]{lang="EN-US"}**[{ **count** *count* \| **interval** *minutes* }]{lang="EN-US"}]{#struct_0_18308_19795_x2000100134}

[**[undo certificate request ]{lang="EN-US"}[polling]{lang="EN-US"}**[ { **count** \| **interval** }]{lang="EN-US"}]{#struct_0_18308_19795_1653328706}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x778712565}

[[证书申请状态的查询周期为]{style="font-family:宋体"}[20]{lang="EN-US"}]{#struct_0_18308_19795_x889394215}[分钟，最多查询]{style="font-family:宋体"}[50]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1168894218}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x172894700}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x67185297}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1864756279}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1552019692}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_309227036}

[**[count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_18308_19795_x2000034598}[：表示证书申请状态的查询次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}***[ minutes]{lang="EN-US"}*]{#struct_0_18308_19795_x726703801}[：表示证书申请状态的查询周期，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[168]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1699962699}

[[设备发送证书申请后，如果]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x757764522}[服务器采用手工方式来签发证书申请，则不会立刻响应设备的申请。这种情况下，设备通过定期向]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器发送状态查询消息，能够及时获取到被]{style="font-family:宋体"}[CA]{lang="EN-US"}[签发的证书。]{style="font-family:宋体"}[CA]{lang="EN-US"}[签发证书后，设备将通过发送状态查询得到证书，之后停止发送状态查询消息。如果达到最大查询次数时，]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器仍未签发证书，则设备停止发送状态查询消息，本次证书申请失败。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x10149827}[服务器采用自动签发证书的方式，则设备可以立刻得到证书，这种情况下设备不会向]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器发送状态查询消息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_744724031}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1771252237}[指定证书申请状态的查询周期为]{style="font-family:宋体"}[15]{lang="EN-US"}[分钟，最多查询]{style="font-family:宋体"}[40]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1589321341}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request polling interval 15]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request polling count 40]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1999969062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate request-status]{lang="EN-US"}**]{#struct_0_18308_19795_x35419129}
:::

::: {#-1354896552 .myid}
[]{#_Toc404793063}[]{#struct_0_18308_19795_1538030948}

**PKI \-- PKI配置命令 \-- certificate request url**

------------------------------------------------------------------------

[**[certificate request url]{lang="EN-US"}**]{#struct_0_18308_19795_953881886}[命令用来配置实体通过]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[进行证书申请的注册受理机构服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo certificate request url]{lang="EN-US"}**]{#struct_0_18308_19795_x1032333176}[命令用来删除指定的注册受理机构服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2098801793}

[**[certificate request url]{lang="EN-US"}**[ *url-string* \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_18308_19795_1636701103}

[**[undo certificate request url]{lang="EN-US"}**]{#struct_0_18308_19795_461152286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1576663276}

[[未指定注册受理机构服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_18308_19795_1900224605}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1999903526}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_2118675094}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1535923888}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1791129450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x306322753}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2071132208}

[*[url-string]{lang="EN-US"}*]{#struct_0_18308_19795_x1719151034}[：表示证书申请的注册受理机构服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[511]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_18308_19795_2145468410}[：指定注册受理机构服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，则表示该注册受理机构服务器属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1116265650}

[[本命令配置的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_18308_19795_x2000362278}[内容包括注册受理机构服务器的位置及]{style="font-family:宋体"}[CGI]{lang="EN-US"}[命令接口脚本位置，格式为]{style="font-family:宋体"}[http://*server_location/cgi_script_location*]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[server_location]{lang="EN-US"}*[是服务器的地址，可以是]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址、]{style="font-family:宋体"}[ IPv6]{lang="EN-US"}[地址和]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名，]{style="font-family:宋体"}*[cgi_script_location]{lang="EN-US"}*[是注册授权机构（]{style="font-family:宋体"}[CA]{lang="EN-US"}[或]{style="font-family:宋体"}[RA ]{lang="EN-US"}[）在服务器主机上的应用程序脚本的路径。]{style="font-family:宋体"}

[[实际可输入的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_18308_19795_29971071}[长度受命令行允许输入的最大字符数限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_601734441}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x399984280}[指定实体]{style="font-family:宋体"}[进行证书申请的注册受理机构服务器的]{style="font-family:
宋体"}[URL]{lang="EN-US"}[为]{style="font-family:
宋体"}[http://169.254.0.100/certsrv/mscep/mscep.dll]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x753665794}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request url http://169.254.0.100/certsrv/mscep/mscep.dll]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x2127713332}[指定实体向]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中的注册受理机构服务器申请证书，该服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://mytest.net/certsrv/mscep/mscep.dll]{lang="EN-US"}[，所在的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的实例名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x535056561}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] certificate request url http:// mytest.net /certsrv/mscep/mscep.dll vpn-instance vpn1]{lang="EN-US"}
:::

::: {#1267752382 .myid}
[]{#_Toc404793064}[]{#struct_0_18308_19795_x1434060682}[]{#_Toc279490534}[]{#_Toc279082863}[]{#_Toc265512453}[]{#_Toc61836613}[]{#_Toc286333932}[]{#_Toc286333933}

**PKI \-- PKI配置命令 \-- common-name**

------------------------------------------------------------------------

[**[common-name]{lang="EN-US"}**]{#struct_0_18308_19795_x2000296742}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的通用名，比如用户名称。]{style="font-family:宋体"}

[**[undo common-name]{lang="EN-US"}**]{#struct_0_18308_19795_910566153}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的通用名。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1711781352}

[**[common-name ]{lang="EN-US"}***[common-name-sting]{lang="EN-US"}*]{#struct_0_18308_19795_531730467}

[**[undo common-name]{lang="EN-US"}**]{#struct_0_18308_19795_x1126185289}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1585035017}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x704856455}[实体的通用名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1266342680}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1569340701}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1880445934}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x2000231206}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1384698688}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2099129760}

[*[common-name-sting]{lang="EN-US"}*]{#struct_0_18308_19795_x1866035459}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的通用名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，不能包含逗号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x709867026}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_579030968}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[的通用名为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1560531360}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] common-name test]{lang="EN-US"}
:::

::: {#717170147 .myid}
[]{#_Toc404793065}[]{#struct_0_18308_19795_545146657}[]{#_Toc279490535}[]{#_Toc279082864}[]{#_Toc265512454}[]{#_Toc61836614}

**PKI \-- PKI配置命令 \-- country**

------------------------------------------------------------------------

[**[country]{lang="EN-US"}**]{#struct_0_18308_19795_x2000165670}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的国家代码。]{style="font-family:宋体"}

[**[undo country]{lang="EN-US"}**]{#struct_0_18308_19795_x196432477}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的国家代码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x788775692}

[**[country ]{lang="EN-US"}***[country-code-string]{lang="EN-US"}*]{#struct_0_18308_19795_x1927377894}

[**[undo country]{lang="EN-US"}**]{#struct_0_18308_19795_1721251024}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_2033952954}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1187647358}[实体所属的国家代码。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1553063320}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x2010576651}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_905662713}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1999575846}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x60732452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x162872438}

[*[country-code-string]{lang="EN-US"}*]{#struct_0_18308_19795_x946468097}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的国家代码，为标准的两字符代码，区分大小写，例如中国为]{style="font-family:宋体"}[CN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_331265581}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1255515467}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[所属的国家代码为]{style="font-family:宋体"}[CN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_973576075}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] country CN]{lang="EN-US"}
:::

::: {#-975631424 .myid}
[]{#_Toc404793066}[]{#struct_0_18308_19795_x49990948}

**PKI \-- PKI配置命令 \-- crl check**

------------------------------------------------------------------------

[**[crl check enable]{lang="EN-US"}**]{#struct_0_18308_19795_1359744287}[命令用来使能]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[**[undo crl check enable]{lang="EN-US"}**]{#struct_0_18308_19795_x1999510310}[命令用来禁止]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1254230145}

[**[crl check enable]{lang="EN-US"}**]{#struct_0_18308_19795_x50676123}

[**[undo crl check enable]{lang="EN-US"}**]{#struct_0_18308_19795_x1411291620}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1439328599}

[[CRL]{lang="EN-US"}]{#struct_0_18308_19795_1787813032}[检查处于使能状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_222757329}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x174095030}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x189636755}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1870582171}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x2000100133}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1882123703}

[[CRL]{lang="EN-US"}]{#struct_0_18308_19795_2099162827}[（]{style="font-family:宋体"}[Certificate Revocation List]{lang="EN-US"}[，证书废除列表）是一个由]{style="font-family:宋体"}[CA]{lang="EN-US"}[签发的文件，该文件中包含被该]{style="font-family:宋体"}[CA]{lang="EN-US"}[吊销的所有证书的列表。一个证书有可能在有效期达到之前被]{style="font-family:宋体"}[CA]{lang="EN-US"}[吊销。使能]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查的目的是查看设备上的实体证书或者即将要导入、获取到设备上的实体证书是否已经被]{style="font-family:宋体"}[CA]{lang="EN-US"}[吊销，若检查结果表明实体证书已被吊销，那么该证书就不被设备信任。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1556570771}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x300800918}[禁止]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x89198107}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] undo crl check enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1883746794}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_x1539284928}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x2000034597}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki validate-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_483149780}
:::

::: {#-1027135824 .myid}
[]{#_Toc404793067}[]{#struct_0_18308_19795_652190411}

**PKI \-- PKI配置命令 \-- crl url**

------------------------------------------------------------------------

[**[crl url]{lang="EN-US"}**]{#struct_0_18308_19795_x911457130}[命令用来设置]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo crl url]{lang="EN-US"}**]{#struct_0_18308_19795_x2081077447}[命令用来删除]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x588247814}

[**[crl url ]{lang="EN-US"}***[url-string ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_18308_19795_x245063143}

[**[undo crl url]{lang="EN-US"}**]{#struct_0_18308_19795_x710370357}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_2059391574}

[[未设置]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_822453071}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1999969061}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1530664812}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_434061933}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x721467121}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1473540930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2008084394}

[*[url-string]{lang="EN-US"}*]{#struct_0_18308_19795_1061096580}[：表示]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[511]{lang="EN-US"}[个字符的字符串，区分大小写。格式为]{style="font-family:宋体"}[ldap://*server_location*]{lang="EN-US"}[或]{style="font-family:宋体"}[http://*server_location*]{lang="EN-US"}[，其中]{style="font-family:宋体"}*[server_location]{lang="EN-US"}*[可以为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址和]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_18308_19795_x242675866}[：指定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，则表示该]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2117094463}

[[如果]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_701135493}[检查处于使能状态，则进行]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查之前，需要首先从]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域指定的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。若]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中未配置]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[时，从该待验证的证书中获取发布点信息：优先获取待验证的证书中记录的发布点，如果待验证的证书中没有记录发布点，则获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书中记录的发布点（若待验证的证书为]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，则获取上一级]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书中记录的发布点）。如果无法通过任何途径得到发布点，则通过]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[若配置了]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_18308_19795_x1999903525}[格式的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[，则表示要通过]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。若该]{style="font-family:宋体"}[URL]{lang="EN-US"}[中未携带主机名，则需要根据]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器地址信息来得到完整的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[实际可输入的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_18308_19795_1715390567}[长度受命令行允许输入的最大字符数限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x122878647}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x807033168}[指定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[http://169.254.0.30]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_767327201}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] crl url http://169.254.0.30]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1709900917}[指定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[ldap://169.254.0.30]{lang="EN-US"}[，所在的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的实例名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_192619201}

[\[Sysname\] pki domain 1]{lang="EN-US"}

[\[Sysname-pki-domain-1\] crl url ldap://169.254.0.30 vpn-instance vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1442323704}[]{#_Toc279416407}[]{#_Toc257792951}[]{#_Toc168802556}[]{#_Toc124237068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap-server]{lang="EN-US"}**]{#struct_0_18308_19795_x2000362277}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-crl]{lang="EN-US"}**]{#struct_0_18308_19795_2046393706}
:::

::: {#670665270 .myid}
[]{#_Toc404793068}[]{#struct_0_18308_19795_430555671}[]{#_Toc279163109}[]{#_Toc265512459}

**PKI \-- PKI配置命令 \-- display pki certificate access-control-policy**

------------------------------------------------------------------------

[**[display pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_396097599}[命令用来显示证书访问控制策略的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_458723635}

[**[display pki certificate access-control-policy]{lang="EN-US"}**[ \[ *policy-name* \]]{lang="EN-US"}]{#struct_0_18308_19795_1541688289}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x106829709}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1967191207}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x939989764}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x2000296741}

[[network-operator]{lang="EN-US"}]{#struct_0_18308_19795_507281626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x245899717}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18308_19795_1941056324}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1194948554}

[*[policy-name]{lang="EN-US"}*]{#struct_0_18308_19795_x528836215}[：指定证书访问控制策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1469114202}

[[若不指定证书访问控制策略的名称，则显示所有证书访问控制策略的配置信息。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1656260990}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x99735141}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1684517162}[显示证书]{style="font-family:宋体"}[访问控制策略]{style="font-family:
宋体"}[mypolicy]{lang="EN-US"}[的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate access-control-policy mypolicy]{lang="EN-US"}]{#struct_0_18308_19795_x2000231205}

[ Access control policy name: mypolicy]{lang="EN-US"}

[     Rule 1  deny    mygroup1]{lang="EN-US"}

[     Rule 2  permit  mygroup2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1344184667}[显示所有证书属性]{style="font-family:宋体"}[访问控制策略的配置信息。]{style="font-family:
宋体"}

[[\<Sysname\> display pki certificate access-control-policy]{lang="EN-US"}]{#struct_0_18308_19795_x301801441}

[ Total PKI certificate access control policies: 2]{lang="EN-US"}

[ Access control policy name: mypolicy1]{lang="EN-US"}

[     Rule 1  deny    mygroup1]{lang="EN-US"}

[     Rule 2  permit  mygroup2]{lang="EN-US"}

[ Access control policy name: mypolicy2]{lang="EN-US"}

[     Rule 1  deny    mygroup3]{lang="EN-US"}

[     Rule 2  permit  mygroup4]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display pki certificate access-control-policy]{lang="EN-US"}]{#struct_0_18308_19795_1850304125}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1970081916}[[字段]{style="font-family:黑体"}]{#struct_0_18308_19795_702567114}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18308_19795_868060619}

[[Total PKI certificate access control policies]{lang="EN-US"}]{#struct_0_18308_19795_x2000165669}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1725816288}[证书访问控制策略的总数]{style="font-family:宋体"}

[[Access control policy name]{lang="EN-US"}]{#struct_0_18308_19795_x932492887}

[[证书访问控制策略名]{style="font-family:宋体"}]{#struct_0_18308_19795_682740689}

[[Rule *number*]{lang="EN-US"}]{#struct_0_18308_19795_1624714410}

[[访问控制规则编号]{style="font-family:宋体"}]{#struct_0_18308_19795_2011586833}

[[permit]{lang="EN-US"}]{#struct_0_18308_19795_x1999575845}

[[当证书的属性与属性组里定义的属性匹配时，认为该证书有效，通过了访问控制策略的检测]{style="font-family:宋体"}]{#struct_0_18308_19795_x1626816393}

[[deny]{lang="EN-US"}]{#struct_0_18308_19795_241915776}

[[当证书的属性与属性组里定义的属性匹配时，认为该证书无效，未通过访问控制策略的检测]{style="font-family:宋体"}]{#struct_0_18308_19795_x1620939560}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1025771645}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_57518110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_18308_19795_2122096685}

::: {#1440076900 .myid}
[]{#_Toc404793069}[]{#struct_0_18308_19795_1956593185}[]{#_Toc279490545}[]{#_Toc279082874}[]{#_Toc265512460}[]{#_Toc133119719}

**PKI \-- PKI配置命令 \-- display pki certificate attribute-group**

------------------------------------------------------------------------

[**[display pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_x1999510309}[命令用来显示证书属性组的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x44311028}

[**[display pki certificate attribute-group ]{lang="EN-US"}**[\[ *group-name* \] ]{lang="EN-US"}]{#struct_0_18308_19795_x727117629}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_534744123}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1818187790}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x384770588}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_997606677}

[[network-operator]{lang="EN-US"}]{#struct_0_18308_19795_x616493514}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_327775436}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18308_19795_951123734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2000100136}

[*[group-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1478839176}[：指定证书属性组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1327690876}

[[若不指定证书属性组的名字，则显示所有证书属性组的配置信息。]{style="font-family:宋体"}]{#struct_0_18308_19795_1884510474}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x484411702}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x883115643}[显示证书]{style="font-family:宋体"}[属性组]{style="font-family:
宋体"}[mygroup]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate attribute-group mygroup]{lang="EN-US"}]{#struct_0_18308_19795_409439082}

[ Attribute group name: mygroup]{lang="EN-US"}

[      Attribute  1 subject-name     dn    ctn   abc]{lang="EN-US"}

[      Attribute  2 issuer-name      fqdn  nctn  app]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1994308727}[显示所有证书]{style="font-family:宋体"}[属性组的信息。]{style="font-family:
宋体"}

[[\<Sysname\> display pki certificate attribute-group]{lang="EN-US"}]{#struct_0_18308_19795_x2000034600}

[ Total PKI certificate attribute groups: 2.]{lang="EN-US"}

[ Attribute group name: mygroup1]{lang="EN-US"}

[      Attribute  1 subject-name     dn    ctn   abc]{lang="EN-US"}

[      Attribute  2 issuer-name      fqdn  nctn  app]{lang="EN-US"}

[Attribute group name: mygroup2]{lang="EN-US"}

[      Attribute  1 subject-name     dn    ctn   def]{lang="EN-US"}

[      Attribute  2 issuer-name      fqdn  nctn  fqd]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display pki certificate attribute-group]{lang="EN-US"}]{#struct_0_18308_19795_x1082344334}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1963900732}[[字段]{style="font-family:黑体"}]{#struct_0_18308_19795_915574854}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18308_19795_74114964}

[[Total PKI certificate attribute groups]{lang="EN-US"}]{#struct_0_18308_19795_1529077204}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1477263548}[证书属性组的总数]{style="font-family:宋体"}

[[Attribute group name]{lang="EN-US"}]{#struct_0_18308_19795_x1999969064}

[[证书属性组名称]{style="font-family:宋体"}]{#struct_0_18308_19795_1127380285}

[[Attribute *number*]{lang="EN-US"}]{#struct_0_18308_19795_150483963}

[[属性规则编号]{style="font-family:宋体"}]{#struct_0_18308_19795_x1333642153}

[[subject-name]{lang="EN-US"}]{#struct_0_18308_19795_x252316823}

[[证书主题名]{style="font-family:宋体"}]{#struct_0_18308_19795_x405981560}

[[alt-subject-name]{lang="EN-US"}]{#struct_0_18308_19795_x1999903528}

[[证书备用主题名]{style="font-family:宋体"}]{#struct_0_18308_19795_955875680}

[[issuer-name]{lang="EN-US"}]{#struct_0_18308_19795_x855668939}

[[证书颁发者名]{style="font-family:宋体"}]{#struct_0_18308_19795_x1514367072}

[[dn]{lang="EN-US"}]{#struct_0_18308_19795_758414830}

[[实体的]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_18308_19795_x640304908}

[[fqdn]{lang="EN-US"}]{#struct_0_18308_19795_x2000362280}

[[实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}]{#struct_0_18308_19795_x326718041}

[[ip]{lang="EN-US"}]{#struct_0_18308_19795_x27154865}

[[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18308_19795_x197567091}[地址]{style="font-family:宋体"}

[[ctn]{lang="EN-US"}]{#struct_0_18308_19795_x1175020886}

[[表示包含操作]{style="font-family:宋体"}]{#struct_0_18308_19795_x2000296744}

[[nctn]{lang="EN-US"}]{#struct_0_18308_19795_x252233261}

[[表示不包含操作]{style="font-family:宋体"}]{#struct_0_18308_19795_1106875408}

[[equ]{lang="EN-US"}]{#struct_0_18308_19795_1562143209}

[[表示等于操作]{style="font-family:宋体"}]{#struct_0_18308_19795_x1632652931}

[[nequ]{lang="EN-US"}]{#struct_0_18308_19795_x2000231208}

[[表示不等操作]{style="font-family:宋体"}]{#struct_0_18308_19795_x1391238834}

[[Attribute  1 subject-name     dn    ctn   abc]{lang="EN-US"}]{#struct_0_18308_19795_2045687424}

[[属性规则内容，包括以下参数：]{style="font-family:宋体"}]{#struct_0_18308_19795_197587086}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[alt-subject-name]{lang="EN-US"}]{#struct_0_18308_19795_1723400244}[：表示证书备用主题名]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[issuer-name]{lang="EN-US"}]{#struct_0_18308_19795_x796576937}[：表示证书颁发者名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[subject-name]{lang="EN-US"}]{#struct_0_18308_19795_1137774396}[：表示证书主题名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[fqdn]{lang="EN-US"}]{#struct_0_18308_19795_1091060295}[：表示实体的]{lang="EN-US" style="font-family:宋体"}[FQDN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ip]{lang="EN-US"}]{#struct_0_18308_19795_170809508}[：表示实体的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[dn]{lang="EN-US"}]{#struct_0_18308_19795_1723465780}[：表示实体的]{lang="EN-US" style="font-family:宋体"}[DN]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ctn]{lang="EN-US"}]{#struct_0_18308_19795_x1986275950}[：表示包含操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[equ]{lang="EN-US"}]{#struct_0_18308_19795_x1218115750}[：表示相等操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nctn]{lang="EN-US"}]{#struct_0_18308_19795_x1928340347}[：表示不包含操作]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[nequ]{lang="EN-US"}]{#struct_0_18308_19795_1722875957}[：表示不等操作]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x15911931}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attribute]{lang="EN-US"}**]{#struct_0_18308_19795_2130190916}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_x2000165672}

::: {#2000779825 .myid}
[]{#_Toc404793070}[]{#struct_0_18308_19795_x1359231891}[]{#_Toc279163117}[]{#_Toc265512458}[]{#_Toc61836629}

**PKI \-- PKI配置命令 \-- display pki certificate domain**

------------------------------------------------------------------------

[**[display pki certificate domain]{lang="EN-US"}**]{#struct_0_18308_19795_x716386750}[命令用来显示证书的内容。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1294646156}

[**[display pki certificate]{lang="EN-US"}**[ **domain** *domain-name* { **ca** \| **local** \| **peer** \[ **serial** *serial-num* \] }]{lang="EN-US"}]{#struct_0_18308_19795_x1391705700}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1263225508}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18308_19795_1057852582}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1799502555}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_593850062}

[[network-operator]{lang="EN-US"}]{#struct_0_18308_19795_x1999575848}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1223531866}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18308_19795_x1715809065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x786729632}

[*[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_1394349260}[：显示指定证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_36978523}[：显示]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_601186160}[：显示本地证书。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_18308_19795_x1584827379}[：显示对端证书。]{style="font-family:宋体"}

[**[serial ]{lang="EN-US"}***[serial-num]{lang="EN-US"}*]{#struct_0_18308_19795_556106856}[：指定要显示的对端证书的序列号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1999510312}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示]{style="font-family:宋体"}]{#struct_0_18308_19795_x91430731}[CA]{lang="EN-US"}[证书时，会显示此]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中所有]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书的详细信息，若]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中存在]{style="font-family:宋体"}[RA]{lang="EN-US"}[证书，则同时显示]{style="font-family:宋体"}[RA]{lang="EN-US"}[证书的详细信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示本地证书时，会显示此]{style="font-family:宋体"}]{#struct_0_18308_19795_1973110488}[PKI]{lang="EN-US"}[域中所有本地证书的详细信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[显示对端证书时，如果不指定序列号，将显示所有对端证书的简要信息；如果指定序列号，将显示该序号对应的指定对端证书的详细信息。]{style="font-family:宋体"}]{#struct_0_18308_19795_2016228576}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_722509109}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1235316996}[显示]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate domain aaa ca]{lang="IT"}]{#struct_0_18308_19795_x2000100135}

[Certificate:]{lang="IT"}

[    Data:]{lang="IT"}

[        Version: 1 (0x0)]{lang="IT"}

[        ]{lang="IT"}[Serial Number:]{lang="EN-US"}

[            5c:72:dc:c4:a5:43:cd:f9:32:b9:c1:90:8f:dd:50:f6]{lang="EN-US"}

[        Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        Issuer: C=cn, O=docm, OU=rnd, CN=rootca]{lang="EN-US"}

[        Validity]{lang="EN-US"}

[            Not Before: Jan  6 02:51:41 2011 GMT]{lang="EN-US"}

[            Not After : Dec  7 03:12:05 2013 GMT]{lang="EN-US"}

[        Subject: C=cn, O=ccc, OU=ppp, CN=rootca]{lang="EN-US"}

[        Subject Public Key Info:]{lang="EN-US"}

[            Public Key Algorithm: rsaEncryption]{lang="EN-US"}

[                Public-Key: (1024 bit)]{lang="EN-US"}

[                ]{lang="EN-US"}[Modulus:]{lang="IT"}

[                    00:c4:fd:97:2c:51:36:df:4c:ea:e8:c8:70:66:f0:]{lang="IT"}

[                    28:98:ec:5a:ee:d7:35:af:86:c4:49:76:6e:dd:40:]{lang="IT"}

[                    4a:9e:8d:c0:cb:d9:10:9b:61:eb:0c:e0:22:ce:f6:]{lang="IT"}

[                    57:7c:bb:bb:1b:1d:b6:81:ad:90:77:3d:25:21:e6:]{lang="IT"}

[                    7e:11:0a:d8:1d:3c:8e:a4:17:1e:8c:38:da:97:f6:]{lang="IT"}

[                    6d:be:09:e3:5f:21:c5:a0:6f:27:4b:e3:fb:9f:cd:]{lang="IT"}

[                    c1:91:18:ff:16:ee:d8:cf:8c:e3:4c:a3:1b:08:5d:]{lang="IT"}

[                    84:7e:11:32:5f:1a:f8:35:25:c0:7e:10:bd:aa:0f:]{lang="IT"}

[                    ]{lang="IT"}[52:db:7b:cd:5d:2b:66:5a:fb]{lang="EN-US"}

[                Exponent: 65537 (0x10001)]{lang="EN-US"}

[    Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        6d:b1:4e:d7:ef:bb:1d:67:53:67:d0:8f:7c:96:1d:2a:03:98:]{lang="EN-US"}

[        ]{lang="EN-US"}[3b:48:41:08:a4:8f:a9:c1:98:e3:ac:7d:05:54:7c:34:d5:ee:]{lang="IT"}

[        09:5a:11:e3:c8:7a:ab:3b:27:d7:62:a7:bb:bc:7e:12:5e:9e:]{lang="IT"}

[        4c:1c:4a:9f:d7:89:ca:20:46:de:c5:b3:ce:36:ca:5e:6e:dc:]{lang="IT"}

[        e7:c6:fe:3f:c5:38:dd:d5:a3:36:ad:f4:3d:e6:32:7f:48:df:]{lang="IT"}

[        07:f0:a2:32:89:86:72:22:cd:ed:e5:0f:95:df:9c:75:71:e7:]{lang="IT"}

[        fe:34:c5:a0:64:1c:f0:5c:e4:8f:d3:00:bd:fa:90:b6:64:d8:]{lang="IT"}

[        88:a6]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_18308_19795_x2000034599}[显示]{style="font-family:宋体"}[PKI]{lang="IT"}[域]{style="font-family:
宋体"}[aaa]{lang="IT"}[中的本地证书。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate domain aaa local]{lang="IT"}]{#struct_0_18308_19795_x1999903527}

[Certificate:]{lang="IT"}

[    Data:]{lang="IT"}

[        Version: 3 (0x2)]{lang="IT"}

[        Serial Number:]{lang="IT"}

[            bc:05:70:1f:0e:da:0d:10:16:1e]{lang="IT"}

[        Signature Algorithm: sha256WithRSAEncryption]{lang="IT"}

[        Issuer: C=CN, O=sec, OU=software, CN=ipsec]{lang="IT"}

[        ]{lang="IT"}[Validity]{lang="EN-US"}

[            Not Before: Jan  7 20:05:44 2011 GMT]{lang="EN-US"}

[            Not After : Jan  7 20:05:44 2012 GMT]{lang="EN-US"}

[        Subject: O=OpenCA Labs, OU=Users, CN=fips fips-sec]{lang="EN-US"}

[        Subject Public Key Info:]{lang="EN-US"}

[            Public Key Algorithm: rsaEncryption]{lang="EN-US"}

[                Public-Key: (1024 bit)]{lang="EN-US"}

[                ]{lang="EN-US"}[Modulus:]{lang="FR"}

[                    00:b2:38:ad:8c:7d:78:38:37:88:ce:cc:97:17:39:]{lang="FR"}

[                    ]{lang="FR"}[52:e1:99:b3:de:73:8b:ad:a8:04:f9:a1:f9:0d:67:]{lang="IT"}

[                    d8:95:e2:26:a4:0b:c2:8c:63:32:5d:38:3e:fd:b7:]{lang="IT"}

[                    4a:83:69:0e:3e:24:e4:ab:91:6c:56:51:88:93:9e:]{lang="IT"}

[                    12:a4:30:ad:ae:72:57:a7:ba:fb:bc:ac:20:8a:21:]{lang="IT"}

[                    46:ea:e8:93:55:f3:41:49:e9:9d:cc:ec:76:13:fd:]{lang="IT"}

[                    ]{lang="IT"}[a5:8d:cb:5b:45:08:b7:d1:c5:b5:58:89:47:ce:12:]{lang="FR"}

[                    ]{lang="FR"}[bd:5c:ce:b6:17:2f:e0:fc:c0:3e:b7:c4:99:31:5b:]{lang="IT"}

[                    ]{lang="IT"}[8a:f0:ea:02:fd:2d:44:7a:67]{lang="EN-US"}

[                Exponent: 65537 (0x10001)]{lang="EN-US"}

[        X509v3 extensions:]{lang="EN-US"}

[            X509v3 Basic Constraints:]{lang="EN-US"}

[                CA:FALSE]{lang="EN-US"}

[            Netscape Cert Type:]{lang="EN-US"}

[                SSL Client, S/MIME]{lang="EN-US"}

[            X509v3 Key Usage:]{lang="EN-US"}

[                Digital Signature, Non Repudiation, Key Encipherment]{lang="EN-US"}

[            X509v3 Extended Key Usage:]{lang="EN-US"}

[                TLS Web Client Authentication, E-mail Protection, Microsoft Smartcardlogin]{lang="EN-US"}

[            Netscape Comment:]{lang="EN-US"}

[                User Certificate of OpenCA Labs]{lang="EN-US"}

[            X509v3 Subject Key Identifier:]{lang="EN-US"}

[                91:95:51:DD:BF:4F:55:FA:E4:C4:D0:10:C2:A1:C2:99:AF:A5:CB:30]{lang="EN-US"}

[            X509v3 Authority Key Identifier:]{lang="EN-US"}

[                keyid:DF:D2:C9:1A:06:1F:BC:61:54:39:FE:12:C4:22:64:EB:57:3B:11:9F]{lang="EN-US"}

[ ]{lang="EN-US"}

[            X509v3 Subject Alternative Name:]{lang="EN-US"}

[                email:fips@ccc.com]{lang="EN-US"}

[            X509v3 Issuer Alternative Name:]{lang="EN-US"}

[                email:pki@openca.org]{lang="EN-US"}

[            Authority Information Access:]{lang="EN-US"}

[                CA Issuers - URI:http://titan/pki/pub/cacert/cacert.crt]{lang="EN-US"}

[                OCSP - URI:http://titan:2560/]{lang="EN-US"}

[                1.3.6.1.5.5.7.48.12 - URI:http://titan:830/]{lang="EN-US"}

[ ]{lang="EN-US"}

[            X509v3 CRL Distribution Points:]{lang="EN-US"}

[ ]{lang="EN-US"}

[                Full Name:]{lang="EN-US"}

[                  URI:http://titan/pki/pub/crl/cacrl.crl]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Signature Algorithm: sha256WithRSAEncryption]{lang="EN-US"}

[        94:ef:56:70:48:66:be:8f:9d:bb:77:0f:c9:f4:65:77:e3:bd:]{lang="EN-US"}

[        ]{lang="EN-US"}[ea:9a:b8:24:ae:a1:38:2d:f4:ab:e8:0e:93:c2:30:33:c8:ef:]{lang="IT"}

[        f5:e9:eb:9d:37:04:6f:99:bd:b2:c0:e9:eb:b1:19:7e:e3:cb:]{lang="IT"}

[        95:cd:6c:b8:47:e2:cf:18:8d:99:f4:11:74:b1:1b:86:92:98:]{lang="IT"}

[        af:a2:34:f7:1b:15:ee:ea:91:ed:51:17:d0:76:ec:22:4c:56:]{lang="IT"}

[        da:d6:d1:3c:f2:43:31:4f:1d:20:c8:c2:c3:4d:e5:92:29:ee:]{lang="IT"}

[        43:c6:d7:72:92:e8:13:87:38:9a:9c:cd:54:38:b2:ad:ba:aa:]{lang="IT"}

[        ]{lang="IT"}[f9:a4:68:b5:2a:df:9a:31:2f:42:80:0c:0c:d9:6d:b3:ab:0f:]{lang="EN-US"}

[        ]{lang="EN-US"}[dd:a0:2c:c0:aa:16:81:aa:d9:33:ca:01:75:94:92:44:05:1a:]{lang="IT"}

[        65:41:fa:1e:41:b5:8a:cc:2b:09:6e:67:70:c4:ed:b4:bc:28:]{lang="IT"}

[        04:50:a6:33:65:6d:49:3c:fc:a8:93:88:53:94:4c:af:23:64:]{lang="IT"}

[        cb:af:e3:02:d1:b6:59:5f:95:52:6d:00:00:a0:cb:75:cf:b4:]{lang="IT"}

[        50:c5:50:00:65:f4:7d:69:cc:2d:68:a4:13:5c:ef:75:aa:8f:]{lang="IT"}

[        3f:ca:fa:eb:4d:d5:5d:27:db:46:c7:f4:7d:3a:b2:fb:a7:c9:]{lang="IT"}

[        de:18:9d:c1]{lang="IT"}

[[\# ]{lang="IT"}]{#struct_0_18308_19795_552591153}[显示]{style="font-family:宋体"}[PKI]{lang="IT"}[域]{style="font-family:
宋体"}[aaa]{lang="IT"}[中的所有对端证书的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate domain aaa peer]{lang="EN-US"}]{#struct_0_18308_19795_1146132080}

[Total peer certificates: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Serial Number: 9a0337eb2156ba1f5476e4d754a5a9f7]{lang="EN-US"}

[Subject  Name: CN=sldsslserver]{lang="EN-US"}

[[\# ]{lang="IT"}]{#struct_0_18308_19795_x1681368455}[显示]{style="font-family:宋体"}[PKI]{lang="IT"}[域]{style="font-family:
宋体"}[aaa]{lang="IT"}[中的一个特定序号的对端证书的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate domain aaa peer serial 9a0337eb2156ba1f5476e4d754a5a9f7]{lang="IT"}]{#struct_0_18308_19795_x2000296743}

[ ]{lang="IT"}

[Certificate:]{lang="IT"}

[    Data:]{lang="IT"}

[        Version: 3 (0x2)]{lang="IT"}

[        Serial Number:]{lang="IT"}

[            9a:03:37:eb:21:56:ba:1f:54:76:e4:d7:54:a5:a9:f7]{lang="IT"}

[        ]{lang="IT"}[Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        Issuer: C=cn, O=ccc, OU=sec, CN=ssl]{lang="EN-US"}

[        Validity]{lang="EN-US"}

[            Not Before: Oct 15 01:23:06 2010 GMT]{lang="EN-US"}

[            Not After : Jul 26 06:30:54 2012 GMT]{lang="EN-US"}

[        Subject: CN=sldsslserver]{lang="EN-US"}

[        Subject Public Key Info:]{lang="EN-US"}

[            Public Key Algorithm: rsaEncryption]{lang="EN-US"}

[                Public-Key: (1024 bit)]{lang="EN-US"}

[                Modulus:]{lang="EN-US"}

[                    00:c2:cf:37:76:93:29:5e:cd:0e:77:48:3a:4d:0f:]{lang="EN-US"}

[                    ]{lang="EN-US"}[a6:28:a4:60:f8:31:56:28:7f:81:e3:17:47:78:98:]{lang="IT"}

[                    68:03:5b:72:f4:57:d3:bf:c5:30:32:0d:58:72:67:]{lang="IT"}

[                    04:06:61:08:3b:e9:ac:53:b9:e7:69:68:1a:23:f2:]{lang="IT"}

[                    97:4c:26:14:c2:b5:d9:34:8b:ee:c1:ef:af:1a:f4:]{lang="IT"}

[                    ]{lang="IT"}[39:da:c5:ae:ab:56:95:b5:be:0e:c3:46:35:c1:52:]{lang="DE"}

[                    ]{lang="DE"}[29:9c:b7:46:f2:27:80:2d:a4:65:9a:81:78:53:d4:]{lang="EN-US"}

[                    ca:d3:f5:f3:92:54:85:b3:ab:55:a5:03:96:2b:19:]{lang="EN-US"}

[                    8b:a3:4d:b2:17:08:8d:dd:81]{lang="EN-US"}

[                Exponent: 65537 (0x10001)]{lang="EN-US"}

[        X509v3 extensions:]{lang="EN-US"}

[            X509v3 Authority Key Identifier:]{lang="EN-US"}

[                ]{lang="EN-US"}[keyid:9A:83:29:13:29:D9:62:83:CB:41:D4:75:2E:52:A1:66:38:3C:90:1]{lang="IT"}[1]{lang="EN-US"}

[ ]{lang="EN-US"}

[            X509v3 Key Usage: critical]{lang="EN-US"}

[                Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement]{lang="EN-US"}

[            Netscape Cert Type:]{lang="EN-US"}

[                SSL Server]{lang="EN-US"}

[            X509v3 Subject Alternative Name:]{lang="EN-US"}

[                DNS:docm.com]{lang="EN-US"}

[            X509v3 Subject Key Identifier:]{lang="EN-US"}

[                3C:76:95:9B:DD:C2:7F:5F:98:83:B7:C7:A0:F8:99:1E:4B:D7:2F:26]{lang="EN-US"}

[            X509v3 CRL Distribution Points:]{lang="EN-US"}

[ ]{lang="EN-US"}

[                Full Name:]{lang="EN-US"}

[                  URI:http://s03130.ccc.sec.com:447/ssl.crl]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        61:2d:79:c7:49:16:e3:be:25:bb:8b:70:37:31:32:e5:d3:e3:]{lang="EN-US"}

[        31:2c:2d:c1:f9:bf:50:ad:35:4b:c1:90:8c:65:79:b6:5f:59:]{lang="EN-US"}

[        ]{lang="EN-US"}[36:24:c7:14:63:44:17:1e:e4:cf:10:69:fc:93:e9:70:53:3c:]{lang="IT"}

[        85:aa:40:7e:b5:47:75:0f:f0:b2:da:b4:a5:50:dd:06:4a:d5:]{lang="IT"}

[        17:a5:ca:20:19:2c:e9:78:02:bd:19:77:da:07:1a:42:df:72:]{lang="IT"}

[        ad:07:7d:e5:16:d6:75:eb:6e:06:58:ee:76:31:63:db:96:a2:]{lang="IT"}

[        ]{lang="IT"}[ad:83:b6:bb:ba:4b:79:59:9d:59:6c:77:59:5b:d9:07:33:a8:]{lang="EN-US"}

[        ]{lang="EN-US"}[f0:a5]{lang="IT"}

[]{#struct_0_18308_19795_x655517788}[[表1-4 ]{lang="EN-US"}[display pki certificate]{lang="EN-US"}]{#_Toc138075230}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_1995676252}[[字段]{style="font-family:黑体"}]{#struct_0_18308_19795_x2030255564}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18308_19795_x187253059}

[[Version]{lang="EN-US"}]{#struct_0_18308_19795_x2000231207}

[[证书版本号]{style="font-family:宋体"}]{#struct_0_18308_19795_x181385253}

[[Serial Number]{lang="EN-US"}]{#struct_0_18308_19795_x587494507}

[[证书序列号]{style="font-family:宋体"}]{#struct_0_18308_19795_x1993599147}

[[Signature Algorithm]{lang="EN-US"}]{#struct_0_18308_19795_x659072750}

[[签名算法]{style="font-family:宋体"}]{#struct_0_18308_19795_x1921775509}

[[Issuer]{lang="EN-US"}]{#struct_0_18308_19795_1221455128}

[[证书颁发者]{style="font-family:宋体"}]{#struct_0_18308_19795_x2000165671}

[[Validity]{lang="EN-US"}]{#struct_0_18308_19795_1369651464}

[[证书有效期]{style="font-family:宋体"}]{#struct_0_18308_19795_x1887713249}

[[Subject]{lang="EN-US"}]{#struct_0_18308_19795_790613598}

[[证书所属的实体信息]{style="font-family:宋体"}]{#struct_0_18308_19795_2117685588}

[[Subject Public Key Info]{lang="EN-US"}]{#struct_0_18308_19795_x1387309393}

[[证书所属的实体的公钥信息]{style="font-family:宋体"}]{#struct_0_18308_19795_x1999575847}

[[X509v3 extensions]{lang="EN-US"}]{#struct_0_18308_19795_1505351489}

[[X.509]{lang="EN-US"}]{#struct_0_18308_19795_x520841057}[版本]{style="font-family:宋体"}[3]{lang="EN-US"}[格式的证书扩展属性]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1414690419}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_1754531042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1646964686}

::: {#-933777909 .myid}
[]{#_Toc404793071}[]{#struct_0_18308_19795_x1900449718}[]{#_Toc293674854}

**PKI \-- PKI配置命令 \-- display pki certificate request-status**

------------------------------------------------------------------------

[**[display pki certificate request-status]{lang="EN-US"}**]{#struct_0_18308_19795_x1999510311}[命令用来显示证书的申请状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_311853796}

[**[display pki certificate request-status ]{lang="EN-US"}**[\[ **domain** *domain-name* \]]{lang="EN-US"}]{#struct_0_18308_19795_x43880031}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x749673706}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x734946060}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x797705793}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_373326879}

[[network-operator]{lang="EN-US"}]{#struct_0_18308_19795_x726224585}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_111291969}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18308_19795_x1943784380}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2000100138}

[**[domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_40190598}[：指定证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1697981698}

[[若不指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_571859697}[域的名称，则显示所有]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的证书申请状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2025202240}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x330326414}[显示]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的证书申请状态。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate request-status domain aaa]{lang="EN-US"}]{#struct_0_18308_19795_x1808402179}

[Certificate Request Transaction 1]{lang="EN-US"}

[    Domain name: aaa]{lang="EN-US"}

[    Status: Pending]{lang="EN-US"}

[    Key usage: General]{lang="EN-US"}

[    Remain polling attempts: 10]{lang="EN-US"}

[    Next polling attempt after : 1191 seconds]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x542571445}[显示所有]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的证书申请状态。]{style="font-family:宋体"}

[[\<Sysname\> display pki certificate request-status]{lang="EN-US"}]{#struct_0_18308_19795_x2000034602}

[Certificate Request Transaction 1]{lang="EN-US"}

[    Domain name: domain1]{lang="EN-US"}

[    Status: Pending]{lang="EN-US"}

[    Key usage: General]{lang="EN-US"}

[    Remain polling attempts: 10]{lang="EN-US"}

[    Next polling attempt after : 1191 seconds]{lang="EN-US"}

[Certificate Request Transaction 2]{lang="EN-US"}

[    Domain name: domain2]{lang="EN-US"}

[    Status: Pending]{lang="EN-US"}

[    Key usage: Signature]{lang="EN-US"}

[    Remain polling attempts: 10]{lang="EN-US"}

[    Next polling attempt after : 188 seconds]{lang="EN-US"}

[[表1-1 ]{lang="EN-US"}[display pki certificate request]{lang="EN-US"}]{#struct_0_18308_19795_80455080}[命令显示信息描述表]{style="font-family:
黑体"}

[]{#table_struct_0_1988462716}[[字段]{style="font-family:黑体"}]{#struct_0_18308_19795_163240373}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18308_19795_702843188}

[[Certificate Request Transaction *number*]{lang="EN-US"}]{#struct_0_18308_19795_531598857}

[[证书申请任务的编号，从]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_18308_19795_x1999969066}[开始顺序编号]{style="font-family:宋体"}

[[Domain name]{lang="EN-US"}]{#struct_0_18308_19795_x2004787597}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x377323363}[域名]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_18308_19795_1149859519}

[[证书申请状态。目前，仅有一种取值]{style="font-family:宋体"}[Pending]{lang="EN-US"}]{#struct_0_18308_19795_832789568}[，表示等待]{style="font-family:宋体"}

[[Key usage]{lang="EN-US"}]{#struct_0_18308_19795_x359272296}

[[证书用途，包括以下取值：]{style="font-family:宋体"}]{#struct_0_18308_19795_x1999903530}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[General]{lang="EN-US"}]{#struct_0_18308_19795_1312040504}[：表示通用，既可以]{lang="EN-US" style="font-family:宋体"}[用于]{style="font-family:宋体"}[加密也可以]{lang="EN-US" style="font-family:宋体"}[用于]{style="font-family:宋体"}[签名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[Signature]{lang="EN-US"}]{#struct_0_18308_19795_x2038823643}[：表示]{lang="EN-US" style="font-family:宋体"}[用于]{style="font-family:宋体"}[签名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="IT" style="font-size:10.0pt;font-family:Symbol"}[Encryption]{lang="IT"}]{#struct_0_18308_19795_1105539406}[：表示]{lang="EN-US" style="font-family:宋体"}[用于]{style="font-family:宋体"}[加密]{lang="EN-US" style="font-family:宋体"}

[[Remain polling attempts]{lang="EN-US"}]{#struct_0_18308_19795_117259450}

[[剩余的证书申请状态的查询次数]{style="font-family:宋体"}]{#struct_0_18308_19795_x448461104}

[[Next polling attempt after]{lang="EN-US"}]{#struct_0_18308_19795_x2000362282}

[[当前到下次查询证书申请状态的时间间隔，单位为秒]{style="font-family:宋体"}]{#struct_0_18308_19795_x1489517455}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1290023458}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[certificate request polling]{lang="EN-US"}**]{#struct_0_18308_19795_x1482556705}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_1632660564}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1902974162}

::: {#-2135290363 .myid}
[]{#_Toc404793072}[]{#struct_0_18308_19795_376960305}[]{#_Toc61836630}[]{#_Toc279163120}[]{#_Toc265512461}

**PKI \-- PKI配置命令 \-- display pki crl**

------------------------------------------------------------------------

[**[display pki crl domain]{lang="EN-US"}**]{#struct_0_18308_19795_x251418271}[命令用来显示存储在本地的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1571723110}

[**[display pki crl]{lang="EN-US"}**[ **domain** *domain-name*]{lang="EN-US"}]{#struct_0_18308_19795_x2000296746}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1415032675}

[[任意视图]{style="font-family:宋体"}]{#struct_0_18308_19795_1750802862}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1158822616}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x920110382}

[[network-operator]{lang="EN-US"}]{#struct_0_18308_19795_1416364237}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x305997897}

[[mdc-operator]{lang="EN-US"}]{#struct_0_18308_19795_x1533063263}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x558763478}

[**[domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_18308_19795_x2000231210}[：指定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1747534730}

[[用户可以通过该命令查看证书吊销列表，看所需的证书是否已经被吊销。]{style="font-family:宋体"}]{#struct_0_18308_19795_171508269}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1438456807}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1965239137}[显示存储在本地的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display pki crl domain aaa]{lang="EN-US"}]{#struct_0_18308_19795_x2000165674}

[Certificate Revocation List (CRL):]{lang="EN-US"}

[        Version 2 (0x1)]{lang="EN-US"}

[        Signature Algorithm: sha1WithRSAEncryption]{lang="EN-US"}

[        Issuer: /C=cn/O=docm/OU=sec/CN=therootca]{lang="EN-US"}

[        Last Update: Apr 28 01:42:13 2011 GMT]{lang="EN-US"}

[        Next Update: NONE]{lang="EN-US"}

[        CRL extensions:]{lang="EN-US"}

[            X509v3 CRL Number:]{lang="EN-US"}

[                6]{lang="EN-US"}

[            X509v3 Authority Key Identifier:]{lang="EN-US"}

[                keyid:49:25:DB:07:3A:C4:8A:C2:B5:A0:64:A5:F1:54:93:69:14:51:11:EF]{lang="EN-US"}

[ ]{lang="EN-US"}

[Revoked Certificates:]{lang="EN-US"}

[    Serial Number: CDE626BF7A44A727B25F9CD81475C004]{lang="EN-US"}

[        Revocation Date: Apr 28 01:37:52 2011 GMT]{lang="EN-US"}

[        CRL entry extensions:]{lang="EN-US"}

[            Invalidity Date:]{lang="EN-US"}

[                Apr 28 01:37:49 2011 GMT]{lang="EN-US"}

[    Serial Number: FCADFA81E1F56F43D3F2D3EF7EB56DE5]{lang="EN-US"}

[        Revocation Date: Apr 28 01:33:28 2011 GMT]{lang="EN-US"}

[        CRL entry extensions:]{lang="EN-US"}

[            Invalidity Date:]{lang="EN-US"}

[                Apr 28 01:33:09 2011 GMT]{lang="EN-US"}

[    ]{lang="EN-US"}[Signature Algorithm: sha1WithRSAEncryption]{lang="IT"}

[        57:ac:00:3e:1e:e2:5f:59:62:04:05:9b:c7:61:58:2a:df:a4:]{lang="IT"}

[        5c:e5:c0:14:af:c8:e7:de:cf:2a:0a:31:7d:32:da:be:cd:6a:]{lang="IT"}

[        36:b5:83:e8:95:06:bd:b4:c0:36:fe:91:7c:77:d9:00:0f:9e:]{lang="IT"}

[        99:03:65:9e:0c:9c:16:22:ef:4a:40:ec:59:40:60:53:4a:fc:]{lang="IT"}

[        8e:47:57:23:e0:75:0a:a4:1c:0e:2f:3d:e0:b2:87:4d:61:8a:]{lang="IT"}

[        ]{lang="IT"}[4a:cb:cb:37:af:51:bd:53:78:76:a1:16:3d:0b:89:01:91:61:]{lang="EN-US"}

[        52:d0:6f:5c:09:59:15:be:b8:68:65:0c:5d:1b:a1:f8:42:04:]{lang="EN-US"}

[        ba:aa]{lang="EN-US"}

[]{#struct_0_18308_19795_1772935991}[]{#_Toc138075231}[]{#_Toc121759878}[]{#_Toc95386928}[]{#_Toc85621942}[[表1-5 ]{lang="EN-US"}[display pki crl domain]{lang="EN-US"}]{#_Toc81452891}[显示信息描述]{style="font-family:黑体"}[表]{style="font-family:黑体"}

[]{#table_struct_0_1990494620}[[字段]{style="font-family:黑体"}]{#struct_0_18308_19795_x63401545}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_18308_19795_x1999575850}

[[Version ]{lang="EN-US"}]{#struct_0_18308_19795_x867367042}

[[CRL]{lang="EN-US"}]{#struct_0_18308_19795_x1693036252}[版本号]{style="font-family:宋体"}

[[Signature Algorithm]{lang="EN-US"}]{#struct_0_18308_19795_x1924980783}

[[CA]{lang="EN-US"}]{#struct_0_18308_19795_988901736}[签名该]{style="font-family:宋体"}[CRL]{lang="EN-US"}[采用的签名算法]{style="font-family:宋体"}

[[Issuer]{lang="EN-US"}]{#struct_0_18308_19795_x1959595311}

[[颁发该]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_2127536349}[的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书名称]{style="font-family:宋体"}

[[Last Update]{lang="EN-US"}]{#struct_0_18308_19795_x1999510314}

[[上次更新]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_715138323}[的时间]{style="font-family:宋体"}

[[Next Update]{lang="EN-US"}]{#struct_0_18308_19795_1533259096}

[[下次更新]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_x1337244270}[的时间]{style="font-family:宋体"}

[[CRL extensions]{lang="EN-US"}]{#struct_0_18308_19795_x644114915}

[[CRL]{lang="EN-US"}]{#struct_0_18308_19795_1773682269}[扩展属性]{style="font-family:宋体"}

[[X509v3 CRL Number]{lang="EN-US"}]{#struct_0_18308_19795_x2000100137}

[[X509]{lang="EN-US"}]{#struct_0_18308_19795_87244765}[版本]{style="font-family:宋体"}[3]{lang="EN-US"}[格式的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[序号]{style="font-family:宋体"}

[[X509v3 Authority Key Identifier]{lang="EN-US"}]{#struct_0_18308_19795_1226062770}

[[X509]{lang="EN-US"}]{#struct_0_18308_19795_182000923}[版本]{style="font-family:宋体"}[3]{lang="EN-US"}[格式的签发该]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的]{style="font-family:宋体"}[CA]{lang="EN-US"}[的标识符]{style="font-family:宋体"}

[[keyid]{lang="EN-US"}]{#struct_0_18308_19795_x1921364652}

[[公钥标识符]{style="font-family:宋体"}]{#struct_0_18308_19795_x1694069991}

[[一个]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x2000034601}[可能有多个密钥对，该字段用于标识]{style="font-family:宋体"}[CA]{lang="EN-US"}[用哪个密钥对对该]{style="font-family:宋体"}[CRL]{lang="EN-US"}[进行签名]{style="font-family:宋体"}

[[Revoked Certificates]{lang="EN-US"}]{#struct_0_18308_19795_1646539021}

[[撤销的证书信息]{style="font-family:宋体"}]{#struct_0_18308_19795_x1942463321}

[[Serial Number]{lang="EN-US"}]{#struct_0_18308_19795_x289794462}

[[被吊销证书的序列号]{style="font-family:宋体"}]{#struct_0_18308_19795_1297946487}

[[Revocation Date]{lang="EN-US"}]{#struct_0_18308_19795_x1999969065}

[[证书被吊销的日期]{style="font-family:宋体"}]{#struct_0_18308_19795_x438703656}

[[CRL entry extensions:]{lang="EN-US"}]{#struct_0_18308_19795_x1121364146}

[[CRL]{lang="EN-US"}]{#struct_0_18308_19795_x608210364}[项目扩展属性]{style="font-family:宋体"}

[[Signature Algorithm:]{lang="IT"}]{#struct_0_18308_19795_x1913196359}

[[签名算法以及签名数据]{style="font-family:宋体"}]{#struct_0_18308_19795_x1999903529}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x610208261}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-crl]{lang="EN-US"}**]{#struct_0_18308_19795_304117452}

::: {#1176784048 .myid}
[]{#_Toc404793073}[]{#struct_0_18308_19795_x1474008885}[]{#_Toc285010683}

**PKI \-- PKI配置命令 \-- fqdn**

------------------------------------------------------------------------

[**[fqdn]{lang="EN-US"}**]{#struct_0_18308_19795_1425045417}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo fqdn]{lang="EN-US"}**]{#struct_0_18308_19795_1382995470}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1897315669}

[**[fqdn ]{lang="EN-US"}***[fqdn-name-string]{lang="EN-US"}*]{#struct_0_18308_19795_x442780001}

[**[undo fqdn]{lang="EN-US"}**]{#struct_0_18308_19795_x2000362281}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1239365900}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_945737271}[实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1145592327}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1152211451}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1046851771}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1602205550}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1627614007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1996594895}

[*[fqdn-name-string]{lang="EN-US"}*]{#struct_0_18308_19795_x2000296745}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1818317202}

[[FQDN]{lang="EN-US"}]{#struct_0_18308_19795_x1367992890}[是实体在网络中的唯一标识，由一个主机名和一个域名组成，形式为]{style="font-family:宋体"}*[hostname]{lang="EN-US"}*[@*domainname*]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1706560025}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1692140699}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[为]{style="font-family:宋体"}[abc@pki.domain.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1516939132}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] fqdn abc@pki.domain.com]{lang="EN-US"}
:::

::: {#-839206969 .myid}
[]{#struct_0_18308_19795_1640884852}[]{#_Toc404793074}

**PKI \-- PKI配置命令 \-- ip**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**]{#struct_0_18308_19795_x1121750938}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**]{#struct_0_18308_19795_x2000231209}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1337644521}

[**[ip ]{lang="EN-US"}**[{ *ip-address* \| **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_18308_19795_585777771}

[**[undo ip]{lang="EN-US"}**]{#struct_0_18308_19795_1155982456}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_888355513}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1973540798}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x714394515}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1801168070}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1079363750}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x2000165673}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_206852050}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1575503726}

[*[ip-address]{lang="EN-US"}*]{#struct_0_18308_19795_x2022266624}[：指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-numbe]{lang="EN-US"}*]{#struct_0_18308_19795_1891883893}[：指定接口的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型及接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x811730469}

[[通过本命令，可以直接指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1275908798}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，也可以指定设备上某接口的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址作为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。如果指定使用某接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则不要求本配置执行时该接口上已经配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，只要设备申请证书时，该接口上配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，就可以直接使用该地址作为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体身份的一部分。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x460026095}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1805835257}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1999575849}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] ip 192.168.0.2]{lang="EN-US"}
:::

::: {#1883734488 .myid}
[]{#_Toc404793075}[]{#struct_0_18308_19795_342552075}[]{#_Toc293674818}

**PKI \-- PKI配置命令 \-- ldap-server**

------------------------------------------------------------------------

[**[ldap-server]{lang="EN-US"}**]{#struct_0_18308_19795_x992793664}[命令用来指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[**[undo ldap-server]{lang="EN-US"}**]{#struct_0_18308_19795_x388249483}[命令用来删除指定的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_379524099}

[**[ldap-server host]{lang="EN-US"}**[ *hostname* \[ **port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_18308_19795_114511857}

[**[undo ldap-server]{lang="EN-US"}**]{#struct_0_18308_19795_x1223366510}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x312959753}

[[未指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_18308_19795_x1999510313}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1474653210}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1780176545}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1930029951}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x797096613}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x6353289}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2131318611}

[**[host ]{lang="EN-US"}***[host-name]{lang="EN-US"}*]{#struct_0_18308_19795_1451970767}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，支持]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[与]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的表示方法以及]{style="font-family:宋体"}[DNS]{lang="EN-US"}[域名的表示方法。]{style="font-family:宋体"}

[**[port]{lang="EN-US"}**[ *port-number*]{lang="EN-US"}]{#struct_0_18308_19795_x2026101780}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[389]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_18308_19795_x434016193}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若未指定本参数，则表示该]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1900279920}

[[以下两种情况下，需要配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_18308_19795_x660521571}[服务器：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_18308_19795_x1808493116}[LDAP]{lang="EN-US"}[协议获取本地证书或对端证书时，需要指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过]{style="font-family:宋体"}]{#struct_0_18308_19795_1353909119}[LDAP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[时，若]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[格式的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[中未携带主机名，则需要根据此处配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器地址来得到完整的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_476337192}[域中，只能指定一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器，若重复执行本命令，最新的配置生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2136034494}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_884181167}[指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.0.0.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x433950657}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] ldap-server host 10.0.0.1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1631380213}[指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.0.0.11]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[333]{lang="EN-US"}[，所在的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的实例名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1190794556}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] ldap-server host 10.0.0.11 port 333 vpn-instance vpn1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1610667331}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x1362477255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-crl]{lang="EN-US"}**]{#struct_0_18308_19795_878172889}
:::

::: {#2005552659 .myid}
[]{#_Toc404793076}[]{#struct_0_18308_19795_261745688}[]{#_Toc279490538}[]{#_Toc279082867}[]{#_Toc265512465}[]{#_Toc61836616}

**PKI \-- PKI配置命令 \-- locality**

------------------------------------------------------------------------

[**[locality]{lang="EN-US"}**]{#struct_0_18308_19795_322495061}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所在的地理区域名称，比如城市名称。]{style="font-family:宋体"}

[**[undo locality]{lang="EN-US"}**]{#struct_0_18308_19795_x62248392}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所在的地理区域名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x433885121}

[**[locality ]{lang="EN-US"}***[locality-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1879335918}

[**[undo locality]{lang="EN-US"}**]{#struct_0_18308_19795_x837042511}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_611830500}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1543718094}[实体所在的地理区域名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x203954093}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1616526276}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_643494325}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1216647973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x433819585}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1589121884}

[*[locality-name]{lang="EN-US"}*]{#struct_0_18308_19795_x628167707}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所在的地理区域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，不能包含逗号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1378776007}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1556542155}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[所在地理区域的名称为]{style="font-family:宋体"}[pukras]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1686780722}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] locality pukras]{lang="EN-US"}
:::

::: {#-1479011592 .myid}
[]{#_Toc404793077}[]{#struct_0_18308_19795_1551136526}[]{#_Toc279490539}[]{#_Toc279082868}[]{#_Toc265512466}[]{#_Toc61836617}

**PKI \-- PKI配置命令 \-- organization**

------------------------------------------------------------------------

[**[organization]{lang="EN-US"}**]{#struct_0_18308_19795_x1816565423}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属组织的名称。]{style="font-family:宋体"}

[**[undo organization]{lang="EN-US"}**]{#struct_0_18308_19795_x434278337}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属组织的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1253669178}

[**[organization]{lang="EN-US"}***[ org-name]{lang="EN-US"}*]{#struct_0_18308_19795_x238111130}

[**[undo organization]{lang="EN-US"}**]{#struct_0_18308_19795_1342598516}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_713418764}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1567137185}[实体所属组织名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x719027231}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1117931094}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x594571412}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x434212801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_357747495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1767374983}

[*[org-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1558868285}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的组织名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，不能包含逗号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1581727022}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x647455401}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[所属的组织名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x305679492}

[[\[Sysname\] pki entity en]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_18308_19795_x25490658}

[[\[Sysname-pki-entity-en\] organization abc]{lang="EN-US"}]{#struct_0_18308_19795_198457172}
:::

::: {#1228747264 .myid}
[]{#_Toc404793078}[]{#struct_0_18308_19795_x434147265}[]{#_Toc279490540}[]{#_Toc279082869}[]{#_Toc265512467}[]{#_Toc61836618}

**PKI \-- PKI配置命令 \-- organization-unit**

------------------------------------------------------------------------

[**[organization-unit]{lang="EN-US"}**]{#struct_0_18308_19795_756057145}[命令用来指定实体所属的组织部门的名称。]{style="font-family:宋体"}

[**[undo organization-unit]{lang="EN-US"}**]{#struct_0_18308_19795_84192856}[命令用来删除实体所属的组织部门的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1746686980}

[**[organization-unit]{lang="EN-US"}***[ org-unit-name]{lang="EN-US"}*]{#struct_0_18308_19795_688424953}

[**[undo organization-unit]{lang="EN-US"}**]{#struct_0_18308_19795_x79681171}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x65424882}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x866412868}[实体所属组织部门的名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x453309824}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x434081729}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_694185238}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1127759387}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_898714858}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_416738378}

[*[org-unit-name]{lang="EN-US"}*]{#struct_0_18308_19795_370711683}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属组织部门的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，不能包含逗号。使用该参数可在同一个单位内区分不同部门的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1204222853}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1610691042}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[所属组织部门的名称为]{style="font-family:宋体"}[rdtest]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1879019587}

[[\[Sysname\] pki entity en]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_18308_19795_705239948}

[[\[Sysname-pki-entity-en\] organization-unit rdtest]{lang="EN-US"}]{#struct_0_18308_19795_x433491905}
:::

::: {#-307252400 .myid}
[]{#_Toc404793079}[]{#struct_0_18308_19795_x1078432264}

**PKI \-- PKI配置命令 \-- pki abort-certificate-request**

------------------------------------------------------------------------

[**[pki abort-certificate-request]{lang="EN-US"}**]{#struct_0_18308_19795_x180068339}[命令用来停止证书申请过程。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x900686033}

[**[pki abort-certificate-request]{lang="EN-US"}**]{#struct_0_18308_19795_920246999}**[ domain]{lang="FR"}***[ domain-name]{lang="EN-US"}*

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x828417416}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_1876724924}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_46204692}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1459961079}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x433426369}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1649801571}

[**[domain]{lang="FR"}***[ ]{lang="FR"}[domain-]{lang="EN-US"}[name]{lang="EN-US"}*]{#struct_0_18308_19795_272611183}[：]{style="font-family:宋体"}[指定证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_531798935}

[[用户在证书申请时，可能由于某种原因需要改变证书申请的一些参数，比如通用名、国家代码、]{style="font-family:宋体"}[FQDN]{lang="EN-US"}]{#struct_0_18308_19795_1174217556}[等，而此时证书申请正在运行，为了新的申请不与之前的申请发生冲突，建议先停止之前的申请程序，再进行新的申请。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x200770477}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1458769532}[停止证书申请过程。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_399305325}

[\[Sysname\] pki abort-certificate- request domain 1]{lang="EN-US"}

[The certificate request is in process.]{lang="EN-US"}

[Confirm to abort it? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434016192}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate request-status]{lang="EN-US"}**]{#struct_0_18308_19795_1900214384}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol;border:none"}]{.TerminalDisplayshading}**[pki request-certificate domain]{lang="EN-US"}**]{#struct_0_18308_19795_x270535024}
:::

::: {#-515143108 .myid}
[]{#_Toc404793080}[]{#struct_0_18308_19795_x632463313}[]{#_Toc279163107}[]{#_Toc265512469}[]{#_Toc133119717}[]{#_Toc128811559}[]{#_Toc124237080}

**PKI \-- PKI配置命令 \-- pki certificate access-control-policy**

------------------------------------------------------------------------

[**[pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_1483429678}[命令用来创建证书访问控制策略，并进入证书访问控制策略视图。如果指定的证书访问控制策略已存在，则直接进入其视图。]{style="font-family:宋体"}

[**[undo pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_1231308462}[命令用来删除指定的证书访问控制策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_709147156}

[**[pki certificate access-control-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_18308_19795_x433950656}

[**[undo pki certificate access-control-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_18308_19795_1631314677}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1878310190}

[[不存在证书访问控制策略。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1433111660}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1351281247}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1738035012}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1338829765}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_339559510}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1515236961}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x433885120}

[*[policy-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1879270382}[：表示证书访问控制策略名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1971136191}

[[一个证书访问控制策略中可以定义多个证书属性的访问控制规则。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1554460711}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x319056707}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1035582191}[配置一个名称为]{style="font-family:宋体"}[mypolicy]{lang="EN-US"}[的证书访问控制策略，并进入证书访问控制策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_602537399}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki certificate access-control-policy mypolicy]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname-pki-cert-acp-mypolicy]{lang="ES-AR"}[\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_501511056}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_503116796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_18308_19795_x433819584}
:::

::: {#642182618 .myid}
[]{#_Toc404793081}[]{#struct_0_18308_19795_1589056348}[]{#_Toc279490543}[]{#_Toc279082872}[]{#_Toc265512470}[]{#_Toc133119715}[]{#_Toc128811557}[]{#_Toc124237078}

**PKI \-- PKI配置命令 \-- pki certificate attribute-group**

------------------------------------------------------------------------

[**[pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_x1387765589}[命令用来]{style="font-family:宋体"}[创建证书属性组]{style="font-family:宋体"}[并进入证书属性组视图。如果指定的]{style="font-family:宋体"}[证书属性组]{style="font-family:宋体"}[已存在，则直接进入其视图。]{style="font-family:宋体"}

[**[undo pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_1734524801}[命令用来删除指定的证书属性组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_809517579}

[**[pki certificate attribute-group ]{lang="EN-US"}***[group-nam]{lang="EN-US"}[e]{lang="EN-US"}*]{#struct_0_18308_19795_x1271541715}

[**[undo pki certificate attribute-group]{lang="EN-US"}**[ *group-name* ]{lang="EN-US"}]{#struct_0_18308_19795_x744250465}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x461107035}

[[不存在证书属性组。]{style="font-family:宋体"}]{#struct_0_18308_19795_1028083965}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434278336}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1253734714}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_2127835815}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1814378361}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1486024616}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1699826141}

[*[group-name]{lang="EN-US"}*]{#struct_0_18308_19795_x396607266}[：证书属性组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1714775292}

[[一个证书属性组就是一系列证书属性规则（通过]{style="font-family:宋体"}**[attribute]{lang="EN-US"}**]{#struct_0_18308_19795_163280847}[命令配置）的集合，这些属性规则定义了对证书的颁发者名、主题名以及备用主题名进行过滤的匹配条件。当证书属性组下没有任何属性规则时，则认为对证书的属性没有任何限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434212800}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_357681959}[创建一个名为]{style="font-family:宋体"}[mygroup]{lang="EN-US"}[的]{style="font-family:宋体"}[证书属性组，并进入证书属性组视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_232526242}

[\[Sysname\] pki certificate attribute-group mygroup]{lang="EN-US"}

[\[Sysname-pki-cert-attribute-group-mygroup\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_2067927121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attribute]{lang="EN-US"}**]{#struct_0_18308_19795_x225806787}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_x2005067602}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[rule]{lang="EN-US"}**]{#struct_0_18308_19795_x1089616586}
:::

::: {#1673410531 .myid}
[]{#_Toc404793082}[]{#struct_0_18308_19795_x1359932914}[]{#_Toc279163116}[]{#_Toc265512471}

**PKI \-- PKI配置命令 \-- pki delete-certificate**

------------------------------------------------------------------------

[**[pki delete-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x1548932076}[命令用来删除]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的证书。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434147264}

[**[pki delete-certificate]{lang="EN-US"}**[ **domain** *domain*-*name* { **ca** \| **local** \| **peer** \[ **serial** *serial-num* \] }]{lang="EN-US"}]{#struct_0_18308_19795_756122681}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_856552870}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x2114795465}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1635237576}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_199538574}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x951470435}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_498332298}

[**[domain ]{lang="EN-US"}***[domain]{lang="EN-US"}*[-*name*]{lang="EN-US"}]{#struct_0_18308_19795_x1677100766}[：证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_x434081728}[：表示删除]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_694250774}[：表示删除本地证书。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_18308_19795_643292801}[：表示删除对端证书。]{style="font-family:宋体"}

[**[serial]{lang="EN-US"}***[ serial-num]{lang="EN-US"}*]{#struct_0_18308_19795_807247124}[：表示通过指定序列号删除一个指定的对端证书。]{style="font-family:宋体"}*[serial-num]{lang="EN-US"}*[为对端证书的序列号，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[127]{lang="EN-US"}[个字符的字符串，不区分大小写。在每个]{style="font-family:宋体"}[CA]{lang="EN-US"}[签发的证书范围内，序列号可以唯一标识一个证书。如果不指定本参数，则表示删除本]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的所有对端证书。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_2113788301}

[[删除]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x781476515}[证书时将同时删除所在]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的本地证书和所有对端证书，以及]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[如果需要删除指定的对端证书，则需要首先通过]{style="font-family:宋体"}**[display pki certificate]{lang="EN-US"}**]{#struct_0_18308_19795_196685344}[命令查看本域中已有的对端证书的序列号，然后再通过指定序列号的方式删除该对端证书。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_50311321}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x318181871}[删除]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x433491904}

[\[Sysname\] pki delete-certificate domain aaa ca]{lang="EN-US"}

[Local certificates, peer certificates and CRL will also be deleted while deleting the CA certificate.]{lang="EN-US"}

[Confirm to delete the CA certificate? \[Y/N\]:y]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1078497800}[删除]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的本地证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1403748941}

[\[Sysname\] pki delete-certificate domain aaa local]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1012648037}[删除]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的所有对端证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1373415864}

[\[Sysname\] pki delete-certificate domain aaa peer]{lang="EN-US"}

[\[Sysname\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1328442798}[首先查看]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的对端证书，然后通过指定序列号的方式删除对端证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x433426368}

[\[Sysname\] display pki certificate domain aaa peer]{lang="EN-US"}

[Total peer certificates: 1]{lang="EN-US"}

[ ]{lang="EN-US"}

[Serial Number: 9a0337eb2156ba1f5476e4d754a5a9f7]{lang="EN-US"}

[Subject  Name: CN=abc]{lang="EN-US"}

[\[Sysname\] pki delete-certificate domain aaa peer serial 9a0337eb2156ba1f5476e4d754a5a9f7]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1649867107}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1856961478}
:::

::: {#-902351988 .myid}
[]{#_Toc404793083}[]{#struct_0_18308_19795_x482955438}[]{#_Toc285123230}

**PKI \-- PKI配置命令 \-- pki domain**

------------------------------------------------------------------------

[**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_1992002645}[命令用来创建]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，并进入]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域视图。如果指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域已存在，则直接进入其视图。]{style="font-family:宋体"}

[**[undo pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_x1973588101}[命令用来删除指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1044126306}

[**[pki domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_1283618772}

[**[undo pki domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_x434016195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1900410992}

[[不存在]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_551691117}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_671055483}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_902805829}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_537916999}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_2146175610}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1023072546}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x202564326}

[*[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_x433950659}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1630986997}

[[删除]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x329307452}[域的同时，会将该域相关的证书和]{style="font-family:宋体"}[CRL]{lang="EN-US"}[都删除掉，因此请慎重操作。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1806666849}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_375327962}[创建]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1400943477}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\]]{lang="EN-US"}
:::

::: {#-62323887 .myid}
[]{#_Toc404793084}[]{#struct_0_18308_19795_x756073126}[]{#_Toc279490533}[]{#_Toc279082862}[]{#_Toc265512473}[]{#_Toc61836620}[]{#_Toc298870235}[]{#_Toc298924384}

**PKI \-- PKI配置命令 \-- pki entity**

------------------------------------------------------------------------

[**[pki entity]{lang="EN-US"}**]{#struct_0_18308_19795_x1211198507}[命令用来创建]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体，并进入]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体视图。如果指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体已存在，则直接进入其视图。]{style="font-family:宋体"}

[**[undo pki entity]{lang="EN-US"}**]{#struct_0_18308_19795_2136193075}[命令用来删除指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x433885123}

[**[pki entity ]{lang="EN-US"}***[entity-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1879466990}

[**[undo pki entity]{lang="EN-US"}**[ *entity-name*]{lang="EN-US"}]{#struct_0_18308_19795_648548058}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1448434033}

[[无]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1968795879}[实体存在。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1692689799}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1347044751}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2069755211}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1894772125}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x433819587}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1589252956}

[*[entity-name]{lang="EN-US"}*]{#struct_0_18308_19795_1729531522}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_334669785}

[[在]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1324217490}[实体视图下可配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的各种属性（通用名、组织部门、组织、地理区域、省、国家、]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[、]{style="font-family:宋体"}[IP]{lang="EN-US"}[），这些属性用于描述]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的身份信息。当申请证书时，]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的信息将作为证书中主题（]{style="font-family:宋体"}[Subjuct]{lang="EN-US"}[）部分的内容。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1679671166}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_907001891}[创建名称为]{style="font-family:宋体"}[en]{lang="EN-US"}[的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体，并进入该实体视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="ES-AR"}]{#struct_0_18308_19795_363638198}

[\[Sysname\] pki entity en]{lang="ES-AR"}

[\[Sysname-pki-entity-en\]]{lang="ES-AR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1088710748}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_x434278339}
:::

::: {#797454571 .myid}
[]{#_Toc404793085}[]{#struct_0_18308_19795_x1254324538}[]{#_Toc279163115}

**PKI \-- PKI配置命令 \-- pki export**

------------------------------------------------------------------------

[**[pki export]{lang="EN-US"}**]{#struct_0_18308_19795_1040813317}[命令用来将]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书、本地证书导出到文件中或终端上。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1884762574}

[**[pki export]{lang="EN-US"}**[ **domain** *domain*-*name* **der** { **all** \| **ca** \| **local** } **filename** *filename*]{lang="EN-US"}]{#struct_0_18308_19795_x1065264440}

[**[pki export]{lang="EN-US"}**[ **domain** *domain*-*name* **p12** { **all** \| **local** } **passphrase** *p12passwordstring* **filename** *filename*]{lang="EN-US"}]{#struct_0_18308_19795_x2020465911}

[**[pki export]{lang="EN-US"}**[ **domain** *domain*-*name* **pem** { { **all** \| **local** } \[ { **3des-cbc** \| **aes-128-cbc** \| **aes-192-cbc** \| **aes-256-cbc** \| **des-cbc** } *pempasswordstring* \] \| **ca** } \[ **filename** *filename* \]]{lang="EN-US"}]{#struct_0_18308_19795_1609578753}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1141848039}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1239509414}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434212803}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_357878567}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x753038723}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1003055490}

[**[domain ]{lang="EN-US"}***[domain]{lang="EN-US"}*[-*name*]{lang="EN-US"}]{#struct_0_18308_19795_x2130711331}[：证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[der]{lang="EN-US"}**]{#struct_0_18308_19795_506220661}[：指定证书文件格式为]{style="font-family:宋体"}[DER]{lang="EN-US"}[编码。]{style="font-family:宋体"}

[**[p12]{lang="EN-US"}**]{#struct_0_18308_19795_1978269355}[：]{style="font-family:宋体"}[指定证书文件格式为]{style="font-family:宋体"}[PKCS12]{lang="EN-US"}[编码。]{style="font-family:宋体"}

[**[pem]{lang="EN-US"}**]{#struct_0_18308_19795_465837017}[：指定证书文件格式为]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_18308_19795_x777252887}[：表示导出所有证书，包括]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中所有的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书和本地证书，但不包括]{style="font-family:宋体"}[RA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_x434147267}[：表示导出]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_755926073}[：表示导出本地证书或者本地证书和其对应私钥。]{style="font-family:宋体"}

[**[passphrase]{lang="EN-US"}***[ p12]{lang="EN-US"}[passwordstring]{lang="EN-US"}*]{#struct_0_18308_19795_x827126965}[：指定对]{style="font-family:宋体"}[PKCS12]{lang="EN-US"}[编码格式的本地证书对应的私钥进行加密所采用的口令。]{style="font-family:宋体"}

[**[3des-cbc]{lang="EN-US"}**]{#struct_0_18308_19795_x721217639}**[：]{style="font-family:宋体"}**[对本地证书对应的私钥数据采用]{style="font-family:宋体"}[3DES_CBC]{lang="EN-US"}[算法进行加密。]{style="font-family:宋体"}

[**[aes-128-cbc]{lang="EN-US"}**]{#struct_0_18308_19795_496077849}[：]{style="font-family:宋体"}[对本地证书对应的私钥数据采用]{style="font-family:宋体"}[128]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[算法进行加密。]{style="font-family:宋体"}

[**[aes-192-cbc]{lang="EN-US"}**]{#struct_0_18308_19795_2063964749}[：]{style="font-family:宋体"}[对本地证书对应的私钥数据采用]{style="font-family:宋体"}[192]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[算法进行加密。]{style="font-family:宋体"}

[**[aes-256-cbc]{lang="EN-US"}**]{#struct_0_18308_19795_16128106}[：]{style="font-family:宋体"}[对本地证书对应的私钥数据采用]{style="font-family:宋体"}[256]{lang="EN-US"}[位]{style="font-family:宋体"}[AES_CBC]{lang="EN-US"}[算法进行加密。]{style="font-family:宋体"}

[**[des-cbc]{lang="EN-US"}**]{#struct_0_18308_19795_228586848}[：]{style="font-family:宋体"}[对本地证书对应的私钥数据采用]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[算法进行加密。]{style="font-family:宋体"}

[*[pem]{lang="EN-US"}[passwordstring]{lang="EN-US"}*]{#struct_0_18308_19795_x708393703}[：指定对]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码格式的本地证书对应的私钥进行加密所采用的口令。]{style="font-family:宋体"}

[**[filename ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_18308_19795_x434081731}[：指定保存证书的文件名，不区分大小写。如果不指定本参数，则表示要将证书直接导出到终端上显示，这种方式仅]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码格式的证书才支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_694709525}

[[导出]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_802146429}[证书时，如果]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中只有一个]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书则导出单个]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书到用户指定的一个文件或终端，如果是一个]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链则导出整个]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链到用户指定的一个文件或终端。]{style="font-family:宋体"}

[[导出本地证书时，设备上实际保存证书的证书文件名称并不一定是用户指定的名称，它与本地证书的密钥对用途相关，具体的命名规则如下（假设用户指定的文件名为]{style="font-family:宋体"}*[filename]{lang="EN-US"}*]{#struct_0_18308_19795_x2003141998}[）：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书的密钥对用途为签名，则证书文件名称为]{style="font-family:宋体"}]{#struct_0_18308_19795_x1371203249}*[filename]{lang="EN-US"}*[-signature]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书的密钥对用途为加密，则证书文件名称为]{style="font-family:宋体"}]{#struct_0_18308_19795_x134344569}*[filename]{lang="EN-US"}*[-encryption]{lang="EN-US"}[；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书的密钥对用途为通用（]{style="font-family:宋体"}]{#struct_0_18308_19795_1571622860}[RSA/ECDSA/DSA]{lang="EN-US"}[），则证书文件名称为用户输入的]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[。]{style="font-family:宋体"}

[[导出本地证书时，如果]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x161931788}[域中有两个本地证书，则导出结果如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若指定文件名，则将每个本地证书分别导出到一个单独的文件中；]{style="font-family:宋体"}]{#struct_0_18308_19795_x812870068}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定文件名，则将所有本地证书一次性全部导出到终端上，并由不同的提示信息进行分割显示。]{style="font-family:宋体"}]{#struct_0_18308_19795_x433491907}

[[导出所有证书时，如果]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1078301192}[域中只有本地证书或者只有]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，则导出结果与单独导出相同。如果]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中存在本地证书和]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，则具体导出结果如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若指定文件名，则将每个本地证书分别导出到一个单独的文件，该本地证书对应的完整]{style="font-family:宋体"}]{#struct_0_18308_19795_x2135741829}[CA]{lang="EN-US"}[证书链也会同时导出到该文件中。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定文件名，则将所有的本地证书及域中的]{style="font-family:宋体"}]{#struct_0_18308_19795_2052036294}[CA]{lang="EN-US"}[证书或者]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链一次性全部导出到终端上，并由不同的提示信息进行分割显示。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_18308_19795_1644453095}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以]{style="font-family:宋体"}]{#struct_0_18308_19795_570281663}[PKCS12]{lang="EN-US"}[格式导出所有证书时，]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中必须有本地证书，否则会导出失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以]{style="font-family:宋体"}]{#struct_0_18308_19795_x140510538}[PEM]{lang="EN-US"}[格式导出本地证书或者所有证书时，若不指定私钥的加密算法和私钥加密口令，则不会导出本地证书对应的私钥信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以]{style="font-family:宋体"}]{#struct_0_18308_19795_247206190}[PEM]{lang="EN-US"}[格式导出本地证书或者所有证书时，若指定私钥加密算法和私钥加密口令，且此时本地证书有匹配的私钥，则同时导出本地证书的私钥信息；如果此时本地证书没有匹配的私钥，则导出该本地证书失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[导出本地证书时，若当前]{style="font-family:宋体"}]{#struct_0_18308_19795_x2024557589}[PKI]{lang="EN-US"}[域中的密钥对配置已被修改，导致本地证书的公钥与该密钥对的公钥部分不匹配，则导出该本地证书失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[导出本地证书或者所有证书时，如果]{style="font-family:宋体"}]{#struct_0_18308_19795_x433426371}[PKI]{lang="EN-US"}[域中有两个本地证书，则导出某种密钥用途的本地证书失败并不会影响导出另外一个本地证书。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的文件名中可以带完整路径，当系统中不存在用户所指定路径时，则会导出失败。]{style="font-family:宋体"}]{#struct_0_18308_19795_1649277282}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_281017608}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1885871743}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书到]{style="font-family:宋体"}[DER]{lang="EN-US"}[编码的文件，文件名称为]{style="font-family:宋体"}[cert-ca.der]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_328521921}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 der ca filename cert-ca.der]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1644641904}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的本地证书到]{style="font-family:宋体"}[DER]{lang="EN-US"}[编码的文件，文件名称为]{style="font-family:宋体"}[cert-lo.der]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x1750616018}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 der local filename cert-lo.der]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1623146252}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的所有证书到]{style="font-family:宋体"}[DER]{lang="EN-US"}[编码的文件，文件名称为]{style="font-family:宋体"}[cert-all.p7b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x434016194}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 der all filename cert-all.p7b]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1900345456}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书到]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的文件，文件名称为]{style="font-family:宋体"}[cacert]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x271881455}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem ca filename cacert]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1337101923}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的本地证书及其对应的私钥到]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的文件，指定保护私钥信息的加密算法为]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、加密口令为]{style="font-family:宋体"}[111]{lang="EN-US"}[，文件名称为]{style="font-family:宋体"}[local.pem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x1826971553}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem local des-cbc 111 filename local.pem]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1566628130}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中所有证书到]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的文件，不指定加密算法和加密口令，不导出本地证书对应的私钥信息，文件名称为]{style="font-family:宋体"}[all.pem]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x433950658}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem all filename all.pem]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1630921461}[以]{style="font-family:宋体"}[PEM]{lang="EN-US"}[格式导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中本地证书及其对应的私钥到终端，指定保护私钥信息的加密算法为]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、加密口令为]{style="font-family:宋体"}[111]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x433819586}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem local des-cbc 111]{lang="FR"}

[ ]{lang="FR"}

[%The signature usage local certificate:]{lang="EN-US"}

[Bag Attributes]{lang="EN-US"}

[    friendlyName:]{lang="EN-US"}

[    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D]{lang="EN-US"}

[subject=/C=CN/O=OpenCA Labs/OU=Users/CN=chktest chktest]{lang="EN-US"}

[issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIEqjCCA5KgAwIBAgILAOhID4rI04kBfYgwDQYJKoZIhvcNAQELBQAwRTELMAkG]{lang="EN-US"}

[A1UEBhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2Fy]{lang="EN-US"}

[ZTENMAsGA1UEAwwEYWJjZDAeFw0xMTA0MjYxMzMxMjlaFw0xMjA0MjUxMzMxMjla]{lang="EN-US"}

[ME0xCzAJBgNVBAYTAkNOMRQwEgYDVQQKDAtPcGVuQ0EgTGFiczEOMAwGA1UECwwF]{lang="EN-US"}

[VXNlcnMxGDAWBgNVBAMMD2Noa3Rlc3QgY2hrdGVzdDCBnzANBgkqhkiG9w0BAQEF]{lang="EN-US"}

[AAOBjQAwgYkCgYEA54rUZ0Ux2kApceE4ATpQ437CU6ovuHS5eJKZyky8fhMoTHhE]{lang="EN-US"}

[jE2KfBQIzOZSgo2mdgpkccjr9Ek6IUC03ed1lPn0IG/YaAl4Tjgkiv+w1NrlSvAy]{lang="EN-US"}

[cnPaSUko2QbO9sg3ycye1zqpbbqj775ulGpcXyXYD9OY63/Cp5+DRQ92zGsCAwEA]{lang="EN-US"}

[AaOCAhUwggIRMAkGA1UdEwQCMAAwUAYDVR0gBEkwRzAGBgQqAwMEMAYGBCoDAwUw]{lang="EN-US"}

[NQYEKgMDBjAtMCsGCCsGAQUFBwIBFh9odHRwczovL3RpdGFuL3BraS9wdWIvY3Bz]{lang="EN-US"}

[L2Jhc2ljMBEGCWCGSAGG+EIBAQQEAwIFoDALBgNVHQ8EBAMCBsAwKQYDVR0lBCIw]{lang="EN-US"}

[IAYIKwYBBQUHAwIGCCsGAQUFBwMEBgorBgEEAYI3FAICMC4GCWCGSAGG+EIBDQQh]{lang="EN-US"}

[Fh9Vc2VyIENlcnRpZmljYXRlIG9mIE9wZW5DQSBMYWJzMB0GA1UdDgQWBBTPw8FY]{lang="EN-US"}

[ut7Xr2Ct/23zU/ybgU9dQjAfBgNVHSMEGDAWgBQzEQ58yIC54wxodp6JzZvn/gx0]{lang="EN-US"}

[CDAaBgNVHREEEzARgQ9jaGt0ZXN0QGgzYy5jb20wGQYDVR0SBBIwEIEOcGtpQG9w]{lang="EN-US"}

[ZW5jYS5vcmcwgYEGCCsGAQUFBwEBBHUwczAyBggrBgEFBQcwAoYmaHR0cDovL3Rp]{lang="EN-US"}

[dGFuL3BraS9wdWIvY2FjZXJ0L2NhY2VydC5jcnQwHgYIKwYBBQUHMAGGEmh0dHA6]{lang="EN-US"}

[Ly90aXRhbjoyNTYwLzAdBggrBgEFBQcwDIYRaHR0cDovL3RpdGFuOjgzMC8wPAYD]{lang="EN-US"}

[VR0fBDUwMzAxoC+gLYYraHR0cDovLzE5Mi4xNjguNDAuMTI4L3BraS9wdWIvY3Js]{lang="EN-US"}

[L2NhY3JsLmNybDANBgkqhkiG9w0BAQsFAAOCAQEAGcMeSpBJiuRmsJW0iZK5nygB]{lang="EN-US"}

[tgD8c0b+n4v/F36sJjY1fRFSr4gPLIxZhPWhTrqsCd+QMELRCDNHDxvt3/1NEG12]{lang="EN-US"}

[X6BVjLcKXKH/EQe0fnwK+7PegAJ15P56xDeACHz2oysvNQ0Ot6hGylMqaZ8pKUKv]{lang="EN-US"}

[UDS8c+HgIBrhmxvXztI08N1imYHq27Wy9j6NpSS60mMFmI5whzCWfTSHzqlT2DNd]{lang="EN-US"}

[no0id18SZidApfCZL8zoMWEFI163JZSarv+H5Kbb063dxXfbsqX9Noxggh0gD8dK]{lang="EN-US"}

[7X7/rTJuuhTWVof5gxSUJp+aCCdvSKg0lvJY+tJeXoaznrINVw3SuXJ+Ax8GEw==]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[Bag Attributes]{lang="EN-US"}

[    friendlyName:]{lang="EN-US"}

[    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D]{lang="EN-US"}

[Key Attributes: \<No Attributes\>]{lang="EN-US"}

[\-\-\-\--BEGIN ENCRYPTED PRIVATE KEY\-\-\-\--]{lang="EN-US"}

[MIICwzA9BgkqhkiG9w0BBQ0wMDAbBgkqhkiG9w0BBQwwDgQIAbfcE+KoYYoCAggA]{lang="EN-US"}

[MBEGBSsOAwIHBAjB+UsJM07JRQSCAoABqtASbjGTQbdxL3n4wNHmyWLxbvL9v27C]{lang="EN-US"}

[Uu6MjYJDCipVzxHU0rExgn+6cQsK5uK99FPBmy4q9/nnyrooTX8BVlXAjenvgyii]{lang="EN-US"}

[WQLwnIg1IuM8j2aPkQ3wbae1+0RACjSLy1u/PCl5sp6CDxI0b9xz6cxIGxKvUOCc]{lang="EN-US"}

[/gxdgk97XZSW/0qnOSZkhgeqBZuxq6Va8iRyho7RCStVxQaeiAZpq/WoZbcS5CKI]{lang="EN-US"}

[/WXEBQd4AX2UxN0Ld/On7Wc6KFToixROTxWTtf8SEsKGPDfrEKq3fSTW1xokB8nM]{lang="EN-US"}

[bkRtU+fUiY27V/mr1RHO6+yEr+/wGGClBy5YDoD4I9xPkGUkmqx+kfYbMo4yxkSi]{lang="EN-US"}

[JdL+X3uEjHnQ/rvnPSKBEU/URwXHxMX9CdCTSqh/SajnrGuB/E4JhOEnS/H9dIM+]{lang="EN-US"}

[DN6iz1IwPFklbcK9KMGwV1bosymXmuEbYCYmSmhZb5FnR/RIyE804Jz9ifin3g0Q]{lang="EN-US"}

[ZrykfG7LHL7Ga4nh0hpEeEDiHGEMcQU+g0EtfpOLTI8cMJf7kdNWDnI0AYCvBAAM]{lang="EN-US"}

[3CY3BElDVjJq3ioyHSJca8C+3lzcueuAF+lO7Y4Zluq3dqWeuJjE+/1BZJbMmaQA]{lang="EN-US"}

[X6NmXKNzmtTPcMtojf+n3+uju0le0d0QYXQz/wPsV+9IYRYasjzoXE5dhZ5sIPOd]{lang="EN-US"}

[u9x9hhp5Ns23bwyNP135qTNjx9i/CZMKvLKywm3Yg+Bgg8Df4bBrFrsH1U0ifmmp]{lang="EN-US"}

[ir2+OuhlC+GbHOxWNeBCa8iAq91k6FGFJ0OLA2oIvhCnh45tM7BjjKTHk+RZdMiA]{lang="EN-US"}

[0TKSWuOyihrwxdUEWh999GKUpkwDHLZJFd21z/kWspqThodEx8ea]{lang="EN-US"}

[\-\-\-\--END ENCRYPTED PRIVATE KEY\-\-\-\--]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_18308_19795_1589187420}[以]{style="font-family:宋体"}[PEM]{lang="FR"}[格式导出]{style="font-family:
宋体"}[PKI]{lang="FR"}[域中]{style="font-family:宋体"}[所有]{style="font-family:宋体"}[证书到终端]{style="font-family:宋体"}[，]{style="font-family:宋体"}[指定保护本地证书对应私钥的加密算法为]{style="font-family:宋体"}[DES_CBC]{lang="EN-US"}[、加密口令为]{style="font-family:宋体"}[111]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x434147266}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem all des-cbc 111]{lang="EN-US"}

[ ]{lang="EN-US"}

[ %The signature usage local certificate:]{lang="EN-US"}

[Bag Attributes]{lang="EN-US"}

[    friendlyName:]{lang="EN-US"}

[    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D]{lang="EN-US"}

[subject=/C=CN/O=OpenCA Labs/OU=Users/CN=chktest chktest]{lang="EN-US"}

[issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIEqjCCA5KgAwIBAgILAOhID4rI04kBfYgwDQYJKoZIhvcNAQELBQAwRTELMAkG]{lang="EN-US"}

[A1UEBhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2Fy]{lang="EN-US"}

[ZTENMAsGA1UEAwwEYWJjZDAeFw0xMTA0MjYxMzMxMjlaFw0xMjA0MjUxMzMxMjla]{lang="EN-US"}

[ME0xCzAJBgNVBAYTAkNOMRQwEgYDVQQKDAtPcGVuQ0EgTGFiczEOMAwGA1UECwwF]{lang="EN-US"}

[VXNlcnMxGDAWBgNVBAMMD2Noa3Rlc3QgY2hrdGVzdDCBnzANBgkqhkiG9w0BAQEF]{lang="EN-US"}

[AAOBjQAwgYkCgYEA54rUZ0Ux2kApceE4ATpQ437CU6ovuHS5eJKZyky8fhMoTHhE]{lang="EN-US"}

[jE2KfBQIzOZSgo2mdgpkccjr9Ek6IUC03ed1lPn0IG/YaAl4Tjgkiv+w1NrlSvAy]{lang="EN-US"}

[cnPaSUko2QbO9sg3ycye1zqpbbqj775ulGpcXyXYD9OY63/Cp5+DRQ92zGsCAwEA]{lang="EN-US"}

[AaOCAhUwggIRMAkGA1UdEwQCMAAwUAYDVR0gBEkwRzAGBgQqAwMEMAYGBCoDAwUw]{lang="EN-US"}

[NQYEKgMDBjAtMCsGCCsGAQUFBwIBFh9odHRwczovL3RpdGFuL3BraS9wdWIvY3Bz]{lang="EN-US"}

[L2Jhc2ljMBEGCWCGSAGG+EIBAQQEAwIFoDALBgNVHQ8EBAMCBsAwKQYDVR0lBCIw]{lang="EN-US"}

[IAYIKwYBBQUHAwIGCCsGAQUFBwMEBgorBgEEAYI3FAICMC4GCWCGSAGG+EIBDQQh]{lang="EN-US"}

[Fh9Vc2VyIENlcnRpZmljYXRlIG9mIE9wZW5DQSBMYWJzMB0GA1UdDgQWBBTPw8FY]{lang="EN-US"}

[ut7Xr2Ct/23zU/ybgU9dQjAfBgNVHSMEGDAWgBQzEQ58yIC54wxodp6JzZvn/gx0]{lang="EN-US"}

[CDAaBgNVHREEEzARgQ9jaGt0ZXN0QGgzYy5jb20wGQYDVR0SBBIwEIEOcGtpQG9w]{lang="EN-US"}

[ZW5jYS5vcmcwgYEGCCsGAQUFBwEBBHUwczAyBggrBgEFBQcwAoYmaHR0cDovL3Rp]{lang="EN-US"}

[dGFuL3BraS9wdWIvY2FjZXJ0L2NhY2VydC5jcnQwHgYIKwYBBQUHMAGGEmh0dHA6]{lang="EN-US"}

[Ly90aXRhbjoyNTYwLzAdBggrBgEFBQcwDIYRaHR0cDovL3RpdGFuOjgzMC8wPAYD]{lang="EN-US"}

[VR0fBDUwMzAxoC+gLYYraHR0cDovLzE5Mi4xNjguNDAuMTI4L3BraS9wdWIvY3Js]{lang="EN-US"}

[L2NhY3JsLmNybDANBgkqhkiG9w0BAQsFAAOCAQEAGcMeSpBJiuRmsJW0iZK5nygB]{lang="EN-US"}

[tgD8c0b+n4v/F36sJjY1fRFSr4gPLIxZhPWhTrqsCd+QMELRCDNHDxvt3/1NEG12]{lang="EN-US"}

[X6BVjLcKXKH/EQe0fnwK+7PegAJ15P56xDeACHz2oysvNQ0Ot6hGylMqaZ8pKUKv]{lang="EN-US"}

[UDS8c+HgIBrhmxvXztI08N1imYHq27Wy9j6NpSS60mMFmI5whzCWfTSHzqlT2DNd]{lang="EN-US"}

[no0id18SZidApfCZL8zoMWEFI163JZSarv+H5Kbb063dxXfbsqX9Noxggh0gD8dK]{lang="EN-US"}

[7X7/rTJuuhTWVof5gxSUJp+aCCdvSKg0lvJY+tJeXoaznrINVw3SuXJ+Ax8GEw==]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[Bag Attributes: \<No Attributes\>]{lang="EN-US"}

[subject=/C=CN/O=OpenCA Labs/OU=software/CN=abcd]{lang="EN-US"}

[issuer=/C=CN/O=OpenCA Labs/OU=software/CN=abcd]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIEYTCCA0mgAwIBAgIBFzANBgkqhkiG9w0BAQsFADBFMQswCQYDVQQGEwJDTjEU]{lang="EN-US"}

[MBIGA1UECgwLT3BlbkNBIExhYnMxETAPBgNVBAsMCHNvZnR3YXJlMQ0wCwYDVQQD]{lang="EN-US"}

[DARhYmNkMB4XDTExMDQxODExNDQ0N1oXDTEzMDQxNzExNDQ0N1owRTELMAkGA1UE]{lang="EN-US"}

[BhMCQ04xFDASBgNVBAoMC09wZW5DQSBMYWJzMREwDwYDVQQLDAhzb2Z0d2FyZTEN]{lang="EN-US"}

[MAsGA1UEAwwEYWJjZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM1g]{lang="EN-US"}

[vomMF8S4u6q51bOwjKFUBwxyvOy4D897LmOSedaCyDt6Lvp+PBEHfwWBYBpsHhk7]{lang="EN-US"}

[kmnSNhX5dZ6NxunHaARZ2VlcctsYKyvAQapuaThy1tuOcphAB+jQQL9dPoqdk0xp]{lang="EN-US"}

[jvmPDlW+k832Konn9U4dIivS0n+/KMGh0g5UyzHGqUUOo7s9qFuQf5EjQon40TZg]{lang="EN-US"}

[BwUnFYRlvGe7bSQpXjwi8LTyxHPy+dDVjO5CP+rXx5IiToFy1YGWewkyn/WeswDf]{lang="EN-US"}

[Yx7ZludNus5vKWTihgx2Qalgb+sqUMwI/WUET7ghO2dRxPUdUbgIYF0saTndKPYd]{lang="EN-US"}

[4oBgl6M0SMsHhe9nF5UCAwEAAaOCAVowggFWMA8GA1UdEwEB/wQFMAMBAf8wCwYD]{lang="EN-US"}

[VR0PBAQDAgEGMB0GA1UdDgQWBBQzEQ58yIC54wxodp6JzZvn/gx0CDAfBgNVHSME]{lang="EN-US"}

[GDAWgBQzEQ58yIC54wxodp6JzZvn/gx0CDAZBgNVHREEEjAQgQ5wa2lAb3BlbmNh]{lang="EN-US"}

[Lm9yZzAZBgNVHRIEEjAQgQ5wa2lAb3BlbmNhLm9yZzCBgQYIKwYBBQUHAQEEdTBz]{lang="EN-US"}

[MDIGCCsGAQUFBzAChiZodHRwOi8mdcGl0YW4vcGtpL3B1Yi9jYWNlcnQvY2FjZXJ0]{lang="EN-US"}

[LmNydDAeBggrBgEFBQcwAYYSaHR0cDovL3RpdGFuOjI1NjAvMB0GCCsGAQUFBzAM]{lang="EN-US"}

[hhFodHRwOi8mdcGl0YW46ODMwLzA8BgNVHR8ENTAzMDGgL6AthitodHRwOi8vMTky]{lang="EN-US"}

[LjE2OC40MC4xMjgvcGtpL3B1Yi9jcmwvY2FjcmwuY3JsMA0GCSqGSIb3DQEBCwUA]{lang="EN-US"}

[A4IBAQC0q0SSmvQNfa5ELtRKYF62C/Y8QTLbk6lZDTZuIzN15SGKQcbNM970ffCD]{lang="EN-US"}

[Lk1zosyEVE7PLnii3bZ5khcGO3byyXfluAqRyOGVJcudaw7uIQqgv0AJQ+zaQSHi]{lang="EN-US"}

[d4kQf5QWgYkQ55/C5puOmcMRgCbMpR2lYkqXLDjTIAZIHRZ/sTp6c+ie2bFxi/YT]{lang="EN-US"}

[3xYbO0wDMuGOKJJpsyKTKcbG9NdfbDyFgzEYAobyYqAUB3C0/bMfBduwhQWKSoYE]{lang="EN-US"}

[6vZsPGAEisCmAl3dIp49jPgVkixoShraYF1jLsWzJGlzem8QvWYzOqKEDwq3SV0Z]{lang="EN-US"}

[cXK8gzDBcsobcUMkwIYPAmd1kAPX]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[Bag Attributes]{lang="EN-US"}

[    friendlyName:]{lang="EN-US"}

[    localKeyID: 99 0B C2 3B 8B D1 E4 33 42 2B 31 C3 37 C0 1D DF 0D 79 09 1D]{lang="EN-US"}

[Key Attributes: \<No Attributes\>]{lang="EN-US"}

[\-\-\-\--BEGIN ENCRYPTED PRIVATE KEY\-\-\-\--]{lang="EN-US"}

[MIICwzA9BgkqhkiG9w0BBQ0wMDAbBgkqhkiG9w0BBQwwDgQIcUSKSW9GVmICAggA]{lang="EN-US"}

[MBEGBSsOAwIHBAi5QZM+lSYWPASCAoBKDYulE5f2BXL9ZhI9zWAJpx2cShz/9PsW]{lang="EN-US"}

[5Qm106D+xSj1eAzkx/m4Xb4xRU8oOAuzu1DlWfSHKXoaa0OoRSiOEX1eg0eo/2vv]{lang="EN-US"}

[CHCvKHfTJr4gVSSa7i4I+aQ6AItrI6q99WlkN/e/IE5U1UE4ZhcsIiFJG+IvG7S8]{lang="EN-US"}

[f9liWQ2CImy/hjgFCD9nqSLN8wUzP7O2SdLVlUb5z4FR6VISZdgTFE8j7ko2HtUs]{lang="EN-US"}

[HVSg0nm114EwPtPMMbHefcuQ6b82y1M+dWfVxBN9K03lN4tZNfPWwLSRrPvjUzBG]{lang="EN-US"}

[dKtjf3/IFdV7/tUMy9JJSpt4iFt1h7SZPcOoGp1ZW+YUR30I7YnFE+9Yp/46KWT8]{lang="EN-US"}

[bk7j0STRnZX/xMy/9E52uHkLdW1ET3TXralLMYt/4jg4M0jUvoi3GS2Kbo+czsUn]{lang="EN-US"}

[gKgqwYnxVfRSvt8d6GBYrpF2tMFS9LEyngPKXExd+m4mAryuT5PhdFTkb1B190Lp]{lang="EN-US"}

[UIBjk3IXnr7AdrhvyLkH0UuQE95emXBD/K0HlD73cMrtmogL8F4yS5B2hpIr/v5/]{lang="EN-US"}

[eW35+1QMnJ9FtHFnVsLx9wl9lX8iNfsoBhg6FQ/hNSioN7rNBe7wwIRzxPVfEhO8]{lang="EN-US"}

[5ajQxWlidRn5RkzfUo6HuAcq02QTpSXI6wf2bzsVmr5sk+fRaELD/cwL6VjtXO6x]{lang="EN-US"}

[ZBLJcUyAwvScrOtTEK7Q5n0I34gQd4qcF0D1x9yQ4sqvTeU/7Jkm6XCPV05/5uiF]{lang="EN-US"}

[RLCfFAwaJMBdIQ6jDQHnpWT67uNDwdEzaPmuTVMme5Woc5zsqE5DY3hWu4oqFdDz]{lang="EN-US"}

[kPLnbX74IZ0gOLki9eIJkVswnF5HkBCKS50ejlW6TgbMNZ+JPk2w]{lang="EN-US"}

[\-\-\-\--END ENCRYPTED PRIVATE KEY\-\-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_755991609}[以]{style="font-family:宋体"}[PEM]{lang="FR"}[格式导出]{style="font-family:
宋体"}[PKI]{lang="EN-US"}[域中]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书到终端。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x434081730}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem ca]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIB+TCCAWICEQDMbgjRKygg3vpGFVY6pa3ZMA0GCSqGSIb3DQEBBQUAMD0xCzAJ]{lang="EN-US"}

[BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxETAPBgNVBAsTCGgzYy10ZXN0MQ0wCwYD]{lang="EN-US"}

[VQQDEwQ4MDQzMB4XDTExMDMyMjA0NDQyNFoXDTE0MDMyMzA0MzUyNFowPTELMAkG]{lang="EN-US"}

[A1UEBhMCY24xDDAKBgNVBAoTA2gzYzERMA8GA1UECxMIaDNjLXRlc3QxDTALBgNV]{lang="EN-US"}

[BAMTBDgwNDMwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOvDAYQhyc++G7h5]{lang="EN-US"}

[eNDzJs22OQjCn/4JqnNKIdKz1BbaJT8/+IueSn9JIsg64Ex2WBeCd/tcmnSW57ag]{lang="EN-US"}

[dCvNIUYXXVOGca2iaSOElqCF4CQfV9zLrBtA7giHD49T+JbxLrrJLmdIQMJ+vYdC]{lang="EN-US"}

[sCxIp3YMAiuCahVLZeXklooqwqIXAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAElm7]{lang="EN-US"}

[W2Lp9Xk4nZVIpVV76CkNe8/C+Id00GCRUUVQFSMvo7Pded76bmYX2KzJSz+DlMqy]{lang="EN-US"}

[TdVrgG9Fp6XTFO80aKJGe6NapsfhJHKS+Q7mL0XpXeMONgK+e3dX7rsDxsY7hF+j]{lang="EN-US"}

[0gwsHrjV7kWvwJvDlhzGW6xbpr4DRmdcao19Cr6o=]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_694775061}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书到]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的文件，指定文件名称为]{style="font-family:宋体"}[cacert]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x391764663}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 pem ca filename cacert]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1396766898}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书（证书链）到终端。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x433426370}[\> system-view]{lang="ES-AR"}

[\[]{lang="EN-US"}[Sys]{lang="ES-AR"}[name\] pki export domain domain1 pem ca]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIB7jCCAVcCEQCdSVShJFEMifVG8zRRoSsWMA0GCSqGSIb3DQEBBQUAMDcxCzAJ]{lang="EN-US"}

[BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxDDAKBgNVBAsTA2gzYzEMMAoGA1UEAxMD]{lang="EN-US"}

[YWNhMB4XDTExMDEwNjAyNTc0NFoXDTEzMTIwMTAzMTMyMFowODELMAkGA1UEBhMC]{lang="EN-US"}

[Y24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQ0wCwYDVQQDEwRhYWNhMIGf]{lang="EN-US"}

[MA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcuJsWhAJXEDmowGb5z7VDVms54TKi]{lang="EN-US"}

[xnaNJCWvBOrU64ftvpVB7xQekbkjgAS9FjDyXlLQ8IyIsYIp5ebJr8P+n9i9Pl7j]{lang="EN-US"}

[lBx5mi4XeIldyv2OjfNx5oSQ+gWY9/m1R8uv13RS05r3rxPg+7EvKBjmiy0Giddw]{lang="EN-US"}

[vu3Y3WrjBPp6GQIDAQABMA0GCSqGSIb3DQEBBQUAA4GBAJrQddzVQEiy4AcgtzUL]{lang="EN-US"}

[ltkmlmWoz87+jUsgFB+H+xeyiZE4sancf2UwH8kXWqZ5AuReFCCBC2fkvvQvUGnV]{lang="EN-US"}

[cso7JXAhfw8sUFok9eHz2R+GSoEk5BZFzZ8eCmNyGq9ln6mJsO1hAqMpsCW6G2zh]{lang="EN-US"}

[5mus7FTHhywXpJ22/fnHg61m]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIB8DCCAVkCEQD2PBUx/rvslNw9uTrZB3DlMA0GCSqGSIb3DQEBBQUAMDoxCzAJ]{lang="EN-US"}

[BgNVBAYTAmNuMQwwCgYDVQQKEwNoM2MxDDAKBgNVBAsTA2gzYzEPMA0GA1UEAxMG]{lang="EN-US"}

[cm9mdcGNhMB4XDTExMDEwNjAyNTY1OFoXDTEzMTIwNDAzMTMxMFowNzELMAkGA1UE]{lang="EN-US"}

[BhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQwwCgYDVQQDEwNhY2Ew]{lang="EN-US"}

[gZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOeklR7DpeEV72N1OLz+dydIDTx0]{lang="EN-US"}

[zVZDdPxF1gQYWSfIBwwFKJEyQ/4y8VIfDIm0EGTM4dsOX/QFwudhl/Czkio3dWLh]{lang="EN-US"}

[Q1y5XCJy68vQKrB82WZ2mah5Nuekus3LSZZBoZKTAOY5MCCMFcULM858dtSq15Sh]{lang="EN-US"}

[xF7tKSeAT7ARlJxTAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEADJQCo6m0RNup0ewa]{lang="EN-US"}

[ItX4XK/tYcJXAQWMA0IuwaWpr+ofqVVgYBPwVpYglhJDOuIZxKdR2pfQOA4f35wM]{lang="EN-US"}

[Vz6kAujLATsEA1GW9ACUWa5PHwVgJk9BDEXhKSJ2e7odmrg/iROhJjc1NMV3pvIs]{lang="EN-US"}

[CuFiCLxRQcMGhCNHlOn4wuydssc=]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{lang="EN-US"}

[MIIB8jCCAVsCEFxy3MSlQ835MrnBkI/dUPYwDQYJKoZIhvcNAQEFBQAwOjELMAkG]{lang="EN-US"}

[A1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDaDNjMQ8wDQYDVQQDEwZy]{lang="EN-US"}

[b290Y2EwHhcNMTEwMTA2MDI1MTQxWhcNMTMxMjA3MDMxMjA1WjA6MQswCQYDVQQG]{lang="EN-US"}

[EwJjbjEMMAoGA1UEChMDaDNjMQwwCgYDVQQLEwNoM2MxDzANBgNVBAMTBnJvb3Rj]{lang="EN-US"}

[YTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAxP2XLFE230zq6MhwZvAomOxa]{lang="EN-US"}

[7tc1r4bESXZu3UBKno3Ay9kQm2HrDOAizvZXfLu7Gx22ga2Qdz0lIeZ+EQrYHTyO]{lang="EN-US"}

[pBcejDjal/ZtvgnjXyHFoG8nS+P7n83BkRj/Fu7Yz4zjTKMbCF2EfhEyXxr4NSXA]{lang="EN-US"}

[fhC9qg9S23vNXStmWvsCAwEAATANBgkqhkiG9w0BAQUFAAOBgQBtsU7X77sdZ1Nn]{lang="EN-US"}

[0I98lh0qA5g7SEEIpI+pwZjjrH0FVHw01e4JWhHjyHqrOyfXYqe7vH4SXp5MHEqf]{lang="EN-US"}

[14nKIEbexbPONspebtznxv4/xTjd1aM2rfQ95jJ/SN8H8KIyiYZyIs3t5Q+V35x1]{lang="EN-US"}

[cef+NMWgZBzwXOSP0wC9+pC2ZNiIpg==]{lang="EN-US"}

[\-\-\-\--END CERTIFICATE\-\-\-\--]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1649342818}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的本地证书及其对应的私钥到]{style="font-family:宋体"}[PKCS12]{lang="EN-US"}[编码的文件，指定保护私钥信息的加密口令为]{style="font-family:宋体"}[123]{lang="EN-US"}[，文件名称为]{style="font-family:宋体"}[cert-lo.der]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_1021795009}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 p12 local passphrase 123 filename cert-lo.der]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_340776366}[导出]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的所有证书到]{style="font-family:宋体"}[PKCS12]{lang="EN-US"}[编码的文件，指定文件名称为]{style="font-family:宋体"}[cert-all.p7b]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_1176676082}[\> system-view]{lang="ES-AR"}

[\[Sysname\] pki export domain domain1 p12 all passphrase 123 filename cert-all.p7b]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x312283025}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_1060074536}
:::

::: {#758329447 .myid}
[]{#_Toc404793086}[]{#struct_0_18308_19795_x1803213255}[]{#_Toc279163114}[]{#_Toc265512474}[]{#_Toc298870239}[]{#_Toc298924388}

**PKI \-- PKI配置命令 \-- pki import**

------------------------------------------------------------------------

[**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_x165961658}[命令用来将]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书、本地证书或对端证书导入到指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中保存。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434016197}

[**[pki import domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **der** { **ca** \| **local** \| **peer** } **filename** *filename \|* **p12 local filename** *filename \|* **pem** { **ca** \| **local** \| **peer** } \[ **filename** *filename* \] }]{lang="EN-US"}]{#struct_0_18308_19795_1900542064}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1429390837}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1838811792}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1403644479}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1184091123}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1211438065}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1052364162}

[**[domain]{lang="EN-US"}**[ *domain*-*name*]{lang="EN-US"}]{#struct_0_18308_19795_x1008006217}[：保存证书的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[der]{lang="EN-US"}**]{#struct_0_18308_19795_x433950661}[：指定证书格式为]{style="font-family:宋体"}[DER]{lang="EN-US"}[编码（包括]{style="font-family:宋体"}[PKCS#7]{lang="EN-US"}[格式的证书）。]{style="font-family:宋体"}

[**[p12]{lang="EN-US"}**]{#struct_0_18308_19795_1631511282}[：指定证书格式为]{style="font-family:宋体"}[PKCS#12]{lang="EN-US"}[编码。]{style="font-family:宋体"}

[**[pem]{lang="EN-US"}**]{#struct_0_18308_19795_x1516724252}[：指定证书格式为]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_318610970}[：表示]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_x132432236}[：表示本地证书。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**]{#struct_0_18308_19795_2077412298}[：表示对端证书。]{style="font-family:宋体"}

[**[filename ]{lang="EN-US"}***[filename]{lang="EN-US"}*]{#struct_0_18308_19795_x2018176455}[：要导入的证书所在的文件名，不区分大小写。如果不指定本参数，则表示要通过直接在终端上粘贴证书内容的方式导入证书，这种方式仅]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码格式的证书才支持。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1054530357}

[[如果设备所处的环境中，没有证书的发布点，或者]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_2027934755}[服务器不支持通过]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[协议与设备交互，则可通过此命令将证书导入到设备。另外，当证书对应的密钥对由]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器生成时，]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器会将证书和对应的密钥对打包成一个文件，使用这样的证书前也需要通过此命令将其导入到设备。只有]{style="font-family:宋体"}[PKCS#12]{lang="EN-US"}[格式或]{style="font-family:宋体"}[PEM]{lang="EN-US"}[格式的证书文件中可能包含密钥对。]{style="font-family:宋体"}

[[证书导入之前：]{style="font-family:宋体"}]{#struct_0_18308_19795_x433885125}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[需要通过]{style="font-family:宋体"}]{#struct_0_18308_19795_x1879598062}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[等协议将证书文件传送到设备的存储介质中。如果设备所处的环境不允许使用]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[等协议，则可以直接在终端上粘贴证书的内容，但是粘贴的证书必须是]{style="font-family:宋体"}[PEM]{lang="EN-US"}[格式的，因为只有]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的证书内容为可打印字符。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须存在签发本地证书（或对端证书）的]{style="font-family:宋体"}]{#struct_0_18308_19795_1744718440}[CA]{lang="EN-US"}[证书链才能成功导入本地证书（或对端证书），这里的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链可以是保存在设备上的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的，也可以是本地证书（或对端证书）中携带的。因此，若设备和本地证书（或对端证书）中都没有]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链，则需要首先执行导入]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书的命令。]{style="font-family:宋体"}

[[导入本地证书或对端证书时：]{style="font-family:宋体"}]{#struct_0_18308_19795_x97982392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果用户要导入的本地证书（或对端证书）中含有]{style="font-family:宋体"}]{#struct_0_18308_19795_14710688}[CA]{lang="EN-US"}[证书链，则可以通过导入本地证书（或对端证书）的命令一次性将]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书和本地证书（或对端证书）均导入到设备。导入的过程中，如果发现签发此本地证书（或对端证书）的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书已经存在于设备上的任一]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，则系统会提示用户是否将其进行覆盖。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果要导入的本地证书（或对端证书）中不含有]{style="font-family:宋体"}]{#struct_0_18308_19795_x1601011598}[CA]{lang="EN-US"}[证书链，但签发此本地证书（或对端证书）的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书已经存在于设备上的任一]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，则可以直接导入本地证书（或对端证书）。]{style="font-family:宋体"}

[[导入]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x343256046}[证书时：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要导入的]{style="font-family:宋体"}]{#struct_0_18308_19795_398152966}[CA]{lang="EN-US"}[证书为根]{style="font-family:宋体"}[CA]{lang="EN-US"}[或者包含了完整的证书链（即含有根证书），则可以导入到设备。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要导入的]{style="font-family:宋体"}]{#struct_0_18308_19795_781270806}[CA]{lang="EN-US"}[证书没有包含完整的证书链（即不含有根证书），但能够与设备上已有的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书拼接成完整的证书链，则也可以导入到设备；如果不能与设备上已有的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书拼接成完成的证书链，则不能导入到设备。]{style="font-family:宋体"}

[[一些情况下，在证书导入的过程中，需要用户确认或输入相关信息：]{style="font-family:宋体"}]{#struct_0_18308_19795_x433819589}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若要导入的证书文件中包含了根证书，且设备上目前还没有任何]{style="font-family:宋体"}]{#struct_0_18308_19795_1588335452}[PKI]{lang="EN-US"}[域中有此根证书，且要导入的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中没有配置]{style="font-family:宋体"}**[root-certificate fingerprint]{lang="EN-US"}**[，则在导入过程中还需要确认该根证书的指纹信息是否与用户的预期一致。用户需要通过联系]{style="font-family:
宋体"}[CA]{lang="EN-US"}[服务器管理员来获取预期的根证书指纹信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当导入含有密钥对的本地证书时，需要输入口令。用户需要联系]{style="font-family:宋体"}]{#struct_0_18308_19795_x1387348322}[CA]{lang="EN-US"}[服务器管理员取得口令的内容。]{style="font-family:宋体"}

[[导入含有密钥对的本地证书时，系统首先会根据查找到的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1370259628}[域中已有的密钥对配置来保存该密钥对。若]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中已保存了对应的密钥对，则设备会提示用户选择是否覆盖已有的密钥对。若]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中没有任何密钥对的配置，则根据密钥对的算法及证书的密钥用途，生成相应的密钥对配置。密钥对的具体保存规则如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书携带的密钥对的用途为通用，则依次查找指定]{style="font-family:宋体"}]{#struct_0_18308_19795_1229180234}[PKI]{lang="EN-US"}[域中通用用途、签名用途、加密用途的密钥对配置，并以找到配置中的密钥对名称保存该密钥对；若以上用途的密钥对配置均不存在，则提示用户输入密钥对名称（缺省的密钥对名称为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称），并生成相应的密钥对配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书携带的密钥对的用途为签名，则依次查找指定]{style="font-family:宋体"}]{#struct_0_18308_19795_1580217280}[PKI]{lang="EN-US"}[域中通用用途、签名用途的密钥对配置，并以找到配置中的密钥对名称保存该密钥对；若以上两种用途的密钥对配置均不存在，则提示用户输入密钥对名称（缺省的密钥对名称为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称），并生成相应的密钥对配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果本地证书携带的密钥对的用途为加密，则查找指定]{style="font-family:宋体"}]{#struct_0_18308_19795_721540476}[PKI]{lang="EN-US"}[域中加密用途的密钥对配置，并以该配置中的密钥对名称保存密钥对；若加密用途密钥对的配置不存在，则提示用户输入密钥对名称（缺省的密钥对名称为]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称），并生成相应的密钥对配置。]{style="font-family:宋体"}

[[由于以上过程中系统会自动更新或生成密钥对配置，因此建议用户在进行此类导入操作后，保存配置文件。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1228817119}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_42052682}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x434278341}[向]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中导入]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，证书文件格式为]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码，证书文件名称为]{style="font-family:宋体"}[rootca_pem.cer]{lang="EN-US"}[，证书文件中包含根证书。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x1253800251}[\> system-view]{lang="ES-AR"}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki import domain aaa pem ca filename rootca_pem.cer]{lang="EN-US"}

[The trusted CA\'s finger print is:]{lang="EN-US"}

[    MD5  fingerprint:FFFF 3EFF FFFF 37FF FFFF 137B FFFF 7535]{lang="EN-US"}

[    SHA1 fingerprint:FFFF FF7F FF2B FFFF 7618 FF4C FFFF 0A7D FFFF FF69]{lang="EN-US"}

[Is the finger print correct?(Y/N):y]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_634099232}[向]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[bbb]{lang="EN-US"}[中导入]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，证书文件格式为]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码，证书文件名称为]{style="font-family:宋体"}[aca_pem.cer]{lang="EN-US"}[，证书文件中不包含根证书。]{style="font-family:宋体"}

[[\<Sys]{lang="ES-AR"}[name]{lang="EN-US"}]{#struct_0_18308_19795_x691716672}[\> system-view]{lang="ES-AR"}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki import domain bbb pem ca filename aca_pem.cer]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_151850878}[向]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[bbb]{lang="EN-US"}[中导入本地证书，证书文件格式为]{style="font-family:宋体"}[PKCS#12]{lang="EN-US"}[编码，证书文件名称为]{style="font-family:宋体"}[local-ca.p12]{lang="EN-US"}[，证书文件中包含了密钥对。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x434212805}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki import domain bbb p12 local filename local-ca.p12]{lang="EN-US"}

[Please input challenge password:]{lang="EN-US"}

[\*\*\*\*\*\*]{lang="EN-US"}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_358009639}[向]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[bbb]{lang="EN-US"}[中通过粘贴证书内容的方式导入]{style="font-family:宋体"}[PEM]{lang="EN-US"}[编码的本地证书。证书中含有密钥对和]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x434081733}

[\[Sysname\] pki import domain bbb pem local]{lang="EN-US"}

[Enter PEM-formatted certificate.]{lang="EN-US"}

[End with a Ctrl+c on a line by itself.]{lang="EN-US"}

[[[Bag Attributes]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[localKeyID: 01 00 00 00]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[fri[endlyName: {F7619D96-3AC2-40D4-B6F3-4EAB73DEED73}]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Microsoft CSP Name: Microsoft Enhanced Cryptographic Provider v1.0]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Key Attributes]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[X509v3 Key Usage: 10]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--BEGIN RSA PRIVATE KEY\-\-\-\--]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Proc-Type: 4,ENCRYPTED]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[DEK-Info: DES-EDE3-CBC,8DCE37F0A61A4B8C]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[ ]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[k9C3KHY[5S3EtnF5iQymvHYYrVFy5ZdjSasU5y4XFubjdcvmpFHQteMjD0GKX6+xO]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[kuKbvpyCnWsPVg56sL/PDRyrRmqLmtUV3bpyQsFXgnc7p+Snj3CG2Ciow9XApybW]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Ec1TDCD75yuQckpVQdhguTvoPQXf9zHmiGu5jLkySp2k7ec/Mc97Ef+qqpfnHpQp]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[GDmMqnFpp59ZzB21OGlbGzlPcsjoT+EGpZg6B1KrPiCyFim95L9dWVwX9sk+U1s2]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[+8wqac8jETwwM0UZ1NGJ50JJz1QYIzMbcrw+S5WlPxACTIz1cldlBlb1kpc+7mcX]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[4W+MxFzsL88IJ99T72eu4iUNsy26g0BZMAcc1sJA3A4w9RNhfs9hSG43S3hAh5li]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[JPp720LfYBlkQHn/MgMCZASWDJ5G0eSXQt9QymHAth4BiT9v7zetnQqf4q8plfd/]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Xqd9zEFlBPpoJFtJqXwxHUCKgw6kJeC4CxHvi9ZCJU/upg9IpiguFPoaDOPia[+Pm]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[GbRqSyy55clVde5GOccGN1DZ94DW7AypazgLpBbrkIYAdjFPRmq+zMOdyqsGMTNj]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[jnheI5l784pNOAKuGi0i/uXmRRcfoMh6qAnK6YZGS7rOLC9CfPmy8fgY+/Sl9d9x]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Q00ruO1psxzh9c2YfuaiXFIx0auKl6o5+ZZYn7Rg/xy2Y0awVP+dO925GoAcHO40]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[cCl6jA/HsGAU9HkpwKHL35lmBDRLEzQeBFcaGwSm1JvRfE4tkJM7+Uz2Q[HJOfP10]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[0VLqMgxMlpk3TvBWgzHGJDe7TdzFCDPMPhod8pi4P8gGXmQd01PbyQ==]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--END RSA PRIVATE KEY\-\-\-\--]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[Bag Attributes]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[localKeyID: 01 00 00 00]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[subject=/CN=sldsslserver]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[issuer=/C=cn/O=]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[ccc]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[/OU=sec/CN=ssl]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[MIICjzCCAfigAwIBAgIRAJoDN+shVrofVHbk[11SlqfcwDQYJKoZIhvcNAQEFBQAw]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[NzELMAkGA1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDc2VjMQwwCgYD]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[VQQDEwNzc2wwHhcNMTAxMDE1MDEyMzA2WhcNMTIwNzI2MDYzMDU0WjAXMRUwEwYD]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[VQQDEwxzbGRzc2xzZXJ2ZXIwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMLP]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[N3aTKV7NDndIOk0PpiikYPgxVih/geMX[R3iYaANbcvRX07/FMDINWHJnBAZhCDvp]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[rFO552loGiPyl0wmFMK12TSL7sHvrxr0OdrFrqtWlbW+DsNGNcFSKZy3RvIngC2k]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[ZZqBeFPUytP185JUhbOrVaUDlisZi6NNshcIjd2BAgMBAAGjgbowgbcwHwYDVR0j]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[BBgwFoAUmoMpEynZYoPLQdR1LlKhZjg8kBEwDgYDVR0PAQH/BAQDAgP4MBEGCWCG]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[SAGG+EIBAQQEAwIGQDASBgNVHREE[CzAJggdoM2MuY29tMB0GA1UdDgQWBBQ8dpWb]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[3cJ/X5iDt8eg+JkeS9cvJjA+BgNVHR8ENzA1MDOgMaAvhi1odHRwOi8vczAzMTMw]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[LmgzYy5odWF3ZWktM2NvbS5jb206NDQ3L3NzbC5jcmwwDQYJKoZIhvcNAQEFBQAD]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[gYEAYS15x0kW474lu4twNzEy5dPjMSwtwfm/UK01S8GQjGV5tl9ZNiTHFGNEFx7k]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[zxBp/JPpcFM8hapAfrVHdQ/w[stq0pVDdBkrVF6XKIBks6XgCvRl32gcaQt9yrQd9]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[5RbWdetuBljudjFj25airYO2u7pLeVmdWWx3WVvZBzOo8KU=]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--END CERTIFICATE\-\-\-\--]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[Bag Attributes: \<Empty Attributes\>]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[subject=/C=cn/O=]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[ccc]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[/OU=sec/CN=ssl]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[issuer=/C=cn/O=]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[ccc]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}[[[/OU=sec/CN=ssl]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--BEGIN CERTIFICATE\-\-\-\--]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[MIIB7DCCAVUCEG+jJTPxxiE67pl2ff0SnOMwDQYJKoZIhvcNAQEFBQAwNzELMAkG]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[A1UEBhMCY24xDDAKBgNVBAoTA2gzYzEMMAoGA1UECxMDc2VjMQwwCgYDVQQDEwNz]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[c2wwHhcNMDkwNzMxMDY0ODQ2WhcNMTIwNzI5MDYyODU4WjA3MQswCQYDVQQGEwJj]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[bjEMMAoGA1UEChMDaDNjMQwwCgYDVQQLEwNzZWMxDDAKBgNVBAMTA3NzbDCBn[zAN]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[BgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAt8QSMetQ70GONiFh7iJkvGQ8nC15zCF1]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[cqC/RcJhE/88LkKyQcu9j+Tz8Bk9Qj2UPaZdrk8fOrgtBsa7lZ+UO3j3l30q84l+]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[HjWq8yxVLRQahU3gqJze6pGR2l0s76u6GRyCX/zizGrHKqYlNnxK44NyRZx2klQ2]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[tKQAfpXCPIkCAwEAATANBgkqhkiG9w0BAQUFAAOBgQBWsaMgRbBMtYNrr[YCMjY6g]{style="border:none"}]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[c7PBjvajVOKNUMxaDalePmXfKCxl91+PKM7+i8I/zLcoQO+sHbva26a2/C4sNvoJ]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[2QZs6GtAOahP6CDqXC5VuNBU6eTKNKjL+mf6uuDeMxrlDNha0iymdrXXVIp5cuIu]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[fl7xgArs8Ks6aXDXM1o4DQ==]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--END CERTIFICATE\-\-\-\--]{style="border:none"}]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[[ ]{lang="FR" style="border:none"}]{.TerminalDisplayshading}

[ ]{lang="FR"}

[Please input the password:\*\*\*\*\*\*\*\*]{lang="EN-US"}

[Local certificate already exist, confirm to overwrite it? \[Y/N\]:y]{lang="EN-US"}

[The PKI domain already has a CA certificate. If it is overwritten, local certificates, peer certificates and CRL of this domain will also be deleted.]{lang="EN-US"}

[Overwrite it? \[Y/N\]:y]{lang="EN-US"}

[The system is going to save the key pair. You must specify a key pair name, which is a case-insensitive string of 1 to 64 characters. Valid characters include a to z, A to Z, 0 to 9, and hyphens (-). ]{lang="EN-US"}

[Please enter the key pair name \[default name: bbb\]:]{lang="EN-US"}

[ ]{lang="EN-US"}

[The key pair already exists.]{lang="EN-US"}

[Please enter the key pair name:]{lang="EN-US"}

[import-key]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_694578453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate]{lang="EN-US"}**]{#struct_0_18308_19795_910971615}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key dsa]{lang="EN-US"}**]{#struct_0_18308_19795_x433491909}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key ecdsa]{lang="EN-US"}**]{#struct_0_18308_19795_x1078170120}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key rsa]{lang="EN-US"}**]{#struct_0_18308_19795_1315918434}
:::

::: {#-851820870 .myid}
[]{#_Toc404793087}[]{#struct_0_18308_19795_x1455118123}

**PKI \-- PKI配置命令 \-- pki request-certificate**

------------------------------------------------------------------------

[**[pki request-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1372258662}[命令用来手工申请本地证书或生成]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}[证书申请。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x909602701}

[**[pki request-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x1958082450}**[ domain]{lang="FR"}***[ domain-name ]{lang="EN-US"}*[\[ **password** *password* \] \[ ]{lang="EN-US"}**[pkcs10 ]{lang="EN-US"}**[\[ **filename** *filename* \] \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2038342887}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_499713554}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x433426373}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1649408354}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x953227226}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x769146456}

[**[domain]{lang="FR"}***[ ]{lang="FR"}[domain-]{lang="EN-US"}[name]{lang="EN-US"}*]{#struct_0_18308_19795_x1424499619}[：指定]{style="font-family:宋体"}[证书申请所属的]{style="font-family:宋体"} [PKI]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**[ *password*]{lang="EN-US"}]{#struct_0_18308_19795_x1714507605}[：]{style="font-family:宋体"}[在证书撤销时需要提供的口令，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该口令包含在提交给]{style="font-family:宋体"}[CA]{lang="EN-US"}[的证书申请中，在吊销该证书时，需要提供该口令。]{style="font-family:宋体"}

[**[pkcs10]{lang="EN-US"}**]{#struct_0_18308_19795_x1587907195}[：在终端上显示出]{style="font-family:宋体"}[BASE64]{lang="EN-US"}[格式的]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}[证书申请信息，该信息可用于带外方式（如电话]{style="font-family:宋体"}[、磁盘、电子邮件等）的证书请求。]{style="font-family:宋体"}

[**[filename]{lang="EN-US"}**]{#struct_0_18308_19795_x1345451067}*[ filename]{lang="EN-US"}*[：将]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}[格式的证书申请信息保存到本地的]{style="font-family:宋体"}[文件中。其中，]{style="font-family:宋体"}*[filename]{lang="EN-US"}*[表示保存证书申请信息的文件名，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1313548601}

[[当]{style="font-family:宋体"}[SCEP]{lang="EN-US"}]{#struct_0_18308_19795_x434016196}[协议不能正常通信时，可以通过执行指定参数]{style="font-family:宋体"}**[pkcs10]{lang="EN-US"}**[的本命令打印出本地的证书申请信息（]{style="font-family:宋体"}[BASE64]{lang="EN-US"}[格式），或者通过执行指定]{style="font-family:宋体"}**[pkcs10 filename]{lang="EN-US"}***[ filename]{lang="EN-US"}*[参数的本命令将证书申请信息直接保存到本地的指定文件中，然后通过带外方式将这些本地证书申请信息发送给]{style="font-family:宋体"}[CA]{lang="EN-US"}[进行证书申请。]{style="font-family:宋体"}[指定的文件名中可以带完整路径，当系统中不存在用户所指定路径时，则会保存失败。]{style="font-family:宋体"}

[[此命令不会被保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_18308_19795_1900476528}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1818686306}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1678838606}[在终端上显示]{style="font-family:宋体"}[PKCS#10]{lang="EN-US"}[格式的证书申请信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1140079903}

[\[Sysname\] pki request-certificate domain aaa pkcs10]{lang="EN-US"}

[ ]{lang="EN-US"}

[[[\*\*\* Request for [general certificate \*\*\*]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--BEGIN ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[NEW ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[CERTIFICATE REQUEST\-\-\-\--]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[MIIBTDCBtgIBADANMQswCQYDVQQDEwJqajCBnzANBgkqhkiG9w0BAQEFAAOBjQAw]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[gYkCgYEAw5Drj8ofs9THA4ezkDcQPBy8pvH1kumampPsJmx8sGG52NFtbrDTnTT5]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[ALx3LJijB3d/ndKpcHT/DfbJVDCn5gdw32tBZyCkEwMHZN3ol2z7N]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[mdc]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[u5TED6[iN8]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[4m+hfp1QWoV6lty3o9pxAXuQl8peUDcfN6WV3LBXYyl1WCtkLkECAwEAAaAAMA0G]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[CSqGSIb3DQEBBAUAA4GBAA8E7BaIdmT6NVCZgv/I/1tqZH3TS4e4H9Qo5NiCKiEw]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[R8owVmA0XVtGMbyqBNcDTG0f5NbHrXZQT5+MbFJOnm5K/mn1ro5TJKMTKV46PlCZ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[JUjsugaY02GBY0BVcylpC9iIXLuXNIqjh1MBIqVsa1lQOHS7YMvnop6hX[AQlkM4c]{style="border:none"}]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[[\-\-\-\--END ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[NEW ]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}[[[CERTIFICATE REQUEST\-\-\-\--]{style="border:none"}]{lang="EN-US" style="border:none"}]{.TerminalDisplayshading}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x52070613}[手工申请本地证书。]{style="font-family:宋体"}

[[\[Sysname\] pki request-certificate domain openca]{lang="EN-US"}]{#struct_0_18308_19795_x433950660}

[Start to request the general certificate \...]{lang="EN-US"}

[......]{lang="EN-US"}

[Certificate requested successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1631445746}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate]{lang="EN-US"}**]{#struct_0_18308_19795_1655491979}
:::

::: {#1206252758 .myid}
[]{#_Toc404793088}[]{#struct_0_18308_19795_x1234391056}[]{#_Toc279163113}[]{#_Toc265512476}[]{#_Toc61836624}

**PKI \-- PKI配置命令 \-- pki retrieve-certificate**

------------------------------------------------------------------------

[**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x1278589922}[命令用来从证书发布服务器上在线]{style="font-family:
宋体"}[获取证书并下载至本地。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1525155229}

[**[pki retrieve-certificate]{lang="EN-US"}**[ **domain** *domain-name* { **ca** \| **local** \| **peer** *entity-name* } ]{lang="EN-US"}]{#struct_0_18308_19795_783865329}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_421293825}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x433885124}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1879532526}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x2058061241}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1296734277}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1906431297}

[**[domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_18308_19795_x1769579520}[：指定证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_x1664482412}[：表示获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_x1371281230}[：表示获取本地证书。]{style="font-family:宋体"}

[**[peer]{lang="EN-US"}**[ *entity-name*]{lang="EN-US"}]{#struct_0_18308_19795_1533944818}[：表示获取对端的证书。其中]{style="font-family:宋体"}*[entity-name]{lang="EN-US"}*[为对端的实体名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x433819588}

[[获取]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_1588269916}[证书是通过]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[协议进行的。获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书时，如果本地已有]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书存在，则该操作将不被允许。这种情况下，若要重新获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，请先使用]{style="font-family:宋体"}**[pki delete-certificate]{lang="EN-US"}**[命令删除已有的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书与对应的本地证书后，再执行此命令。]{style="font-family:宋体"}

[[获取本地证书和对端证书是通过]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_18308_19795_578504567}[协议进行的。获取本地证书或对端证书时，如果本地已有本地证书或对端证书，则该操作是被允许进行的。最终，属于一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体的同一种公钥算法的本地证书只能存在一个，后者直接覆盖已有的，但对于]{style="font-family:宋体"}[RSA]{lang="EN-US"}[算法的证书而言，可以存在一个签名用途的证书和一个加密用途的证书。]{style="font-family:宋体"}

[[所有获取到的]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_290106739}[证书、本地证书或对端证书只有通过验证之后才会被保存到本地证书库中。]{style="font-family:宋体"}

[[需要注意的是，此命令不会被保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1836550861}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_366149607}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1861482638}[从证书发布服务器上]{style="font-family:宋体"}[获取]{style="font-family:
宋体"}[CA]{lang="EN-US"}[证书。（需要用户确认]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书的指纹）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x434278340}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki retrieve-certificate domain aaa ca]{lang="EN-US"}

[The trusted CA\'s finger print is:]{lang="EN-US"}

[    ]{lang="EN-US"}[MD5  fingerprint:5C41 E657 A0D6 ECB4 6BD6 1823 7473 AABC]{lang="IT"}

[    SHA1 fingerprint:1616 E7A5 D89A 2A99 9419 1C12 D696 8228 87BC C266]{lang="IT"}

[Is the finger print correct?(Y/N):y]{lang="EN-US"}

[Retrieved the certificates successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1253865787}[从证书发布服务器上]{style="font-family:宋体"}[获取本地]{style="font-family:
宋体"}[证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1321519757}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki retrieve-certificate domain aaa local]{lang="EN-US"}

[Retrieved the certificates successfully.]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x38974291}[从证书发布服务器上]{style="font-family:宋体"}[获取对端]{style="font-family:宋体"}[证书。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1875074008}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki retrieve-certificate domain aaa peer en1]{lang="EN-US"}

[Retrieved the certificates successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x247855245}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate]{lang="EN-US"}**]{#struct_0_18308_19795_344568829}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol;border:none"}]{.TerminalDisplayshading}**[pki delete-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_642113637}
:::

::: {#-742304369 .myid}
[]{#_Toc404793089}[]{#struct_0_18308_19795_x434212804}

**PKI \-- PKI配置命令 \-- pki retrieve-crl**

------------------------------------------------------------------------

[**[pki retrieve-crl]{lang="EN-US"}**]{#struct_0_18308_19795_357944103}[命令用来获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[并下载至本地。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1121666964}

[**[pki retrieve-crl]{lang="EN-US"}**[ **domain** *domain-name* ]{lang="EN-US"}]{#struct_0_18308_19795_x2040952570}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1722618799}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1261250567}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1747374684}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_644116868}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x636499248}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x434147268}

[*[domain-name]{lang="EN-US"}*]{#struct_0_18308_19795_755336249}[：指定]{style="font-family:宋体"}[CRL]{lang="EN-US"}[所属的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，]{style="font-family:宋体"}[不能包括"]{lang="EN-US" style="font-family:
宋体"}[\~]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\*]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\\]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\|]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[:]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[.]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\<]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\>]{lang="EN-US"}["、"]{lang="EN-US" style="font-family:
宋体"}[\"]{lang="EN-US"}["和"]{lang="EN-US" style="font-family:
宋体"}[\']{lang="EN-US"}["]{lang="EN-US" style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_362095098}

[[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_x439014834}[的目的是为了验证]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的本地证书和对端证书的合法性。若要成功获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[，]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中必须存在]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[[设备支持通过]{style="font-family:宋体"}[HTTP]{lang="EN-US"}]{#struct_0_18308_19795_1578110788}[、]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[或]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[协议从]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点上获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[，具体采用那种协议，由]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点的配置决定：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若配置的]{style="font-family:宋体"}]{#struct_0_18308_19795_2003514591}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式为]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[格式，则通过]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若配置的]{style="font-family:宋体"}]{#struct_0_18308_19795_1255991791}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式为]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[格式，则通过]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。若配置的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[（通过命令]{style="font-family:宋体"}**[crl url]{lang="EN-US"}**[）中缺少主机名，例如]{style="font-family:宋体"}[ldap:///CN=8088,OU=test,U=rd,C=cn]{lang="EN-US"}[，则还需要在]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[URL]{lang="EN-US"}[（通过命令]{style="font-family:宋体"}**[ldap server]{lang="EN-US"}**[）。此时，设备会将配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[URL]{lang="EN-US"}[和配置的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点]{style="font-family:宋体"}[URL]{lang="EN-US"}[中的不完整的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[发布点拼装成完整的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[发布点，再通过]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若]{style="font-family:宋体"}]{#struct_0_18308_19795_1725869912}[PKI]{lang="EN-US"}[域中没有配置]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点，则设备会依次从本地证书、]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书中查找]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的发布点，如果从中查找到了]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点，则通过该发布点获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[；否则，通过]{style="font-family:宋体"}[SCEP]{lang="EN-US"}[协议获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x948482997}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x434081732}[从]{style="font-family:宋体"}[CRL]{lang="EN-US"}[发布点上]{style="font-family:宋体"}[获取]{style="font-family:宋体"}[CRL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_694643989}

[\[]{lang="EN-US"}[Sysname]{lang="ES-AR"}[\] pki retrieve-crl domain aaa]{lang="EN-US"}

[Retrieve CRL of the domain aaa successfully.]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1539981129}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[crl url]{lang="EN-US"}**]{#struct_0_18308_19795_1369743194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_18308_19795_2001908021}
:::

::: {#2127153028 .myid}
[]{#_Toc404793090}[]{#struct_0_18308_19795_594721526}[]{#_Toc279163122}[]{#_Toc293674859}

**PKI \-- PKI配置命令 \-- pki storage**

------------------------------------------------------------------------

[**[pki storage]{lang="EN-US"}**]{#struct_0_18308_19795_784848189}[命令用来配置证书和]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的存储路径。]{style="font-family:宋体"}

[**[undo pki storage]{lang="EN-US"}**]{#struct_0_18308_19795_770481662}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_891942047}

[**[pki storage ]{lang="EN-US"}**[{ **certificates** \| **crls** } ]{lang="EN-US"}*[dir-path]{lang="EN-US"}*]{#struct_0_18308_19795_x433491908}

[**[undo pki storage]{lang="IT" style="color:windowtext"}**]{#struct_0_18308_19795_x1078235656}[ { **certificates** \| **crls** }]{lang="IT" style="color:windowtext"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1397573951}

[[证书和]{style="font-family:宋体"}[CRL]{lang="EN-US"}]{#struct_0_18308_19795_x155518410}[的存储路径为设备存储介质上的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[目录。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1876781245}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1078922131}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2143782826}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_199568139}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_253223895}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1413262634}

[**[certificates]{lang="EN-US"}**]{#struct_0_18308_19795_x433426372}[：指定]{lang="EN-US" style="font-family:宋体"}[证书的存储目录。]{lang="EN-US" style="font-family:
宋体"}

[**[crls]{lang="EN-US"}**]{#struct_0_18308_19795_1649473890}[：指定]{lang="EN-US" style="font-family:宋体"}[CRL]{lang="EN-US"}[的存储目录。]{lang="EN-US" style="font-family:宋体"}

[*[dir-path]{lang="EN-US"}*]{#struct_0_18308_19795_x541471041}[：存储目录的路径名称，区分大小写，]{style="font-family:宋体"}[不能以']{style="font-family:宋体"}[/]{lang="EN-US"}['开头，不能包含"]{style="font-family:宋体"}[../]{lang="EN-US"}["。]{style="font-family:宋体"}*[dir-path]{lang="EN-US"}*[可以是绝对路径也可以是相对路径，但必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1914078700}

[*[dir-path]{lang="EN-US"}*]{#struct_0_18308_19795_361802237}[只能是当前主控板上的路径，不能是其它主控板上的路径。]{style="font-family:宋体"}

[[设备缺省的]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1768549529}[目录在设备首次成功申请、获取或导入证书时自动创建。]{style="font-family:宋体"}

[[如果需要指定的目录还不存在，需要先使用]{style="font-family:宋体"}**[mkdir]{lang="EN-US"}**]{#struct_0_18308_19795_x1046129997}[命令创建这个目录，再使用此命令配存储路径。若修改了证书或]{style="font-family:宋体"}[CRL]{lang="EN-US"}[的存储目录，则原存储路径下的证书文件（以]{style="font-family:宋体"}[.cer]{lang="EN-US"}[和]{style="font-family:宋体"}[.p12]{lang="EN-US"}[为后缀的文件）和]{style="font-family:宋体"}[CRL]{lang="EN-US"}[文件（以]{style="font-family:宋体"}[.crl]{lang="EN-US"}[为后缀的文件）将被移动到该路径下保存，且原存储路径下的其它文件不受影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x240843903}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1113955639}[设置证书的存储路径为]{style="font-family:宋体"}[flash:/pki-new]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1565024718}

[\[Sysname\] pki storage certificates flash:/pki-new]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1132067748}[设置]{style="font-family:宋体"}[CRL]{lang="EN-US"}[存储路径为]{style="font-family:宋体"}[pki-new]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1406027954}

[\[Sysname\] pki storage crls pki-new]{lang="EN-US"}
:::

::: {#1535974242 .myid}
[]{#_Toc404793091}[]{#struct_0_18308_19795_1086904806}[]{#_Toc279163111}[]{#_Toc265512478}[]{#_Toc61836626}

**PKI \-- PKI配置命令 \-- pki validate-certificate**

------------------------------------------------------------------------

[**[pki validate-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x686470985}[命令用来验证证书的有效性。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1091025679}

[**[pki validate-certificate]{lang="EN-US"}**[ **domain** *domain-name* { **ca** \| **local** } ]{lang="EN-US"}]{#struct_0_18308_19795_1598013009}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_321321691}

[[系统视图]{style="font-family:宋体"}]{#struct_0_18308_19795_x1038621290}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_379686691}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_1132133284}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x651327089}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1367883262}

[**[domain]{lang="EN-US"}**[ *domain-name*]{lang="EN-US"}]{#struct_0_18308_19795_2037059026}[：指定证书所在的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[\~]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[.]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["、"]{style="font-family:宋体"}[\"]{lang="EN-US"}["和"]{style="font-family:宋体"}[\']{lang="EN-US"}["。]{style="font-family:宋体"}

[**[ca]{lang="EN-US"}**]{#struct_0_18308_19795_x319407911}[：表示验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_18308_19795_216090423}[：表示验证本地证书。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_337909867}

[[证书验证的内容包括：证书是否由用户信任的]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_983271334}[签发；证书是否仍在有效期内；如果使能了]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查功能，还会验证证书是否被吊销。如果验证证书的时候，]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中没有]{style="font-family:宋体"}[CRL]{lang="EN-US"}[，则会先从本地证书库中查找是否存在]{style="font-family:宋体"}[CRL]{lang="EN-US"}[，如果找到]{style="font-family:宋体"}[CRL]{lang="EN-US"}[，则把证书库中保存的]{style="font-family:宋体"}[CRL]{lang="EN-US"}[加载到该]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，否则，就从]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器上获取并保存到本地。]{style="font-family:宋体"}

[[导入证书、申请证书、获取证书以及应用程序使用]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1895323807}[功能时，都会自动对证书进行验证，因此一般不需要使用此命令进行额外的验证。如果用户希望在没有任何前述操作的情况下单独执行证书的验证，可以使用此命令。]{style="font-family:宋体"}

[[验证]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_x31227447}[证书时，会对从当前]{style="font-family:宋体"}[CA]{lang="EN-US"}[到根]{style="font-family:宋体"}[CA]{lang="EN-US"}[的整条]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书链进行]{style="font-family:宋体"}[CRL]{lang="EN-US"}[检查。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2061261728}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1132198820}[验证]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书的有效性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1132264356}

[\[Sysname\] pki validate-certificate domain aaa ca]{lang="EN-US"}

[Verifying certificate\...\...]{lang="EN-US"}

[        Serial Number:]{lang="EN-US"}

[            f6:3c:15:31:fe:bb:ec:94:dc:3d:b9:3a:d9:07:70:e5]{lang="EN-US"}

[        Issuer:]{lang="EN-US"}

[            C=cn]{lang="EN-US"}

[            O=ccc]{lang="EN-US"}

[            OU=ppp]{lang="EN-US"}

[            CN=rootca]{lang="EN-US"}

[        Subject:]{lang="EN-US"}

[            C=cn]{lang="EN-US"}

[            O=abc]{lang="EN-US"}

[            OU=test]{lang="EN-US"}

[            CN=aca]{lang="EN-US"}

[ ]{lang="EN-US"}

[Verify result: OK]{lang="EN-US"}

[Verifying certificate\...\...]{lang="EN-US"}

[        Serial Number:]{lang="EN-US"}

[            5c:72:dc:c4:a5:43:cd:f9:32:b9:c1:90:8f:dd:50:f6]{lang="EN-US"}

[        ]{lang="EN-US"}[Issuer:]{lang="FR"}

[            C=cn]{lang="FR"}

[            O=ccc]{lang="FR"}

[            OU=ppp]{lang="FR"}

[            ]{lang="FR"}[CN=rootca]{lang="EN-US"}

[        Subject:]{lang="EN-US"}

[            C=cn]{lang="EN-US"}

[            O=ccc]{lang="EN-US"}

[            OU=ppp]{lang="EN-US"}

[            CN=rootca]{lang="EN-US"}

[ ]{lang="EN-US"}

[Verify result: OK]{lang="EN-US"}

[[\# ]{lang="IT"}]{#struct_0_18308_19795_925647604}[验证]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域]{style="font-family:宋体"}[aaa]{lang="EN-US"}[中的]{style="font-family:宋体"}[本地]{style="font-family:宋体"}[证书的有效性。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1655735951}

[\[Sysname\] pki validate-certificate domain aaa local]{lang="EN-US"}

[Verifying certificate\...\...]{lang="IT"}

[        Serial Number:]{lang="IT"}

[            bc:05:70:1f:0e:da:0d:10:16:1e]{lang="IT"}

[        Issuer:]{lang="IT"}

[            C=CN]{lang="IT"}

[            O=sec]{lang="IT"}

[            OU=software]{lang="IT"}

[            CN=bca]{lang="IT"}

[        Subject:]{lang="IT"}

[            O=OpenCA Labs]{lang="IT"}

[            OU=Users]{lang="IT"}

[            CN=fips fips-sec]{lang="IT"}

[ ]{lang="IT"}

[Verify result: OK]{lang="IT"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_755031459}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[crl check]{lang="EN-US"}**]{#struct_0_18308_19795_x1058326332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_18308_19795_1131805604}
:::

::: {#-771249820 .myid}
[]{#_Toc404793092}[]{#struct_0_18308_19795_x91173620}[]{#_Toc285123233}

**PKI \-- PKI配置命令 \-- public-key dsa**

------------------------------------------------------------------------

[**[public-key dsa]{lang="EN-US"}**]{#struct_0_18308_19795_x916341770}[命令用来指定证书申请使用的]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对。]{style="font-family:宋体"}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_x1697227352}[命令用来取消指定的密钥对。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_2124596231}

[**[public-key dsa name]{lang="EN-US"}***[ key-name]{lang="EN-US"}*[ \[ **length** *key-length* \]]{lang="EN-US"}]{#struct_0_18308_19795_x2070856119}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_x1192278147}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1475894007}

[[未指定任何密钥对。]{style="font-family:宋体"}]{#struct_0_18308_19795_843808841}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1131871140}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_267165564}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x510622052}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x895096403}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1510863241}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1773865073}

[**[name]{lang="EN-US"}***[ key-name]{lang="EN-US"}*]{#struct_0_18308_19795_x97283626}[：密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写]{style="font-family:宋体"}[，]{style="font-family:宋体"}[只能包含字母、数字和连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}***[ key-length]{lang="EN-US"}*]{#struct_0_18308_19795_46055075}[：密钥的长度。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[key-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[2048]{lang="EN-US"}[，单位为比特，缺省值为]{style="font-family:宋体"}[1024]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[key-length]{lang="EN-US"}*[的取值为]{style="font-family:宋体"}[2048]{lang="EN-US"}[，单位为比特，缺省值为]{style="font-family:宋体"}[2048]{lang="EN-US"}[。密钥越长，密钥安全性越高，但相关的公钥运算越耗时。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1618579106}

[[本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：]{style="font-family:宋体"}]{#struct_0_18308_19795_330661803}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过执行]{lang="EN-US" style="font-family:宋体"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_1131936676}[命令生成。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过应用程序认证过程触发生成。例如]{style="font-family:宋体"}]{#struct_0_18308_19795_x496620863}[IKE]{lang="EN-US"}[协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过导入证书（使用]{style="font-family:宋体"}]{#struct_0_18308_19795_x1997986199}**[pki import]{lang="EN-US"}**[命令）的方式从外界获得。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_1633550229}[域中只能同时存在一种算法（]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}[或]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[）的密钥对。对于]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对来说，一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中只允许单独存在一种用途的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对，或同时存在一个用于签名的和一个用于加密的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对。因此，在一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，除]{style="font-family:宋体"}[RSA]{lang="EN-US"}[签名密钥对和]{style="font-family:宋体"}[RSA]{lang="EN-US"}[加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。]{style="font-family:宋体"}

[[本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。]{style="font-family:宋体"}]{#struct_0_18308_19795_723588217}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_456713684}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_421460485}[指定证书申请所使用的]{style="font-family:宋体"}[DSA]{lang="EN-US"}[密钥对为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，密钥的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1944437585}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] public-key dsa name abc length 2048]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132002212}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_2079194704}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_1681980049}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[公钥管理）]{lang="EN-US" style="font-family:宋体"}
:::

::::: {#-1467674053 .myid}
[]{#_Toc404793093}[]{#struct_0_18308_19795_x1954580914}[]{#_Toc285123232}

**PKI \-- PKI配置命令 \-- public-key ecdsa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](PKI命令.files/image002.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_18308_19795_183404596}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_18308_19795_1551486490}
:::

[ ]{lang="EN-US"}

[**[public-key ecdsa]{lang="EN-US"}**]{#struct_0_18308_19795_500918515}[命令用来指定证书申请使用的]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对。]{style="font-family:宋体"}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_40393163}[命令用来取消指定的密钥对。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x859890810}

[**[public-key ecdsa name]{lang="EN-US"}**[ *key-name*]{lang="EN-US"}]{#struct_0_18308_19795_132772620}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_1132592036}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_1673723309}

[[未指定任何密钥对。]{style="font-family:宋体"}]{#struct_0_18308_19795_547793216}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_32246828}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1066070759}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1865074513}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1046780888}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1383056931}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132657572}

[**[name]{lang="EN-US"}**[ *key-name*]{lang="EN-US"}]{#struct_0_18308_19795_x1798392063}[：密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写]{style="font-family:宋体"}[，]{style="font-family:宋体"}[只能包含字母、数字和连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_878335216}

[[本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：]{style="font-family:宋体"}]{#struct_0_18308_19795_x1092835289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过执行]{lang="EN-US" style="font-family:宋体"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_1157551655}[命令生成。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过应用程序认证过程触发生成。例如]{style="font-family:宋体"}]{#struct_0_18308_19795_1975168976}[IKE]{lang="EN-US"}[协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过导入证书（使用]{style="font-family:宋体"}]{#struct_0_18308_19795_1583583251}**[pki import]{lang="EN-US"}**[命令）的方式从外界获得。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x569441746}[域中只能同时存在一种算法（]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}[或]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[）的密钥对。对于]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对来说，一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中只允许单独存在一种用途的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对，或同时存在一个用于签名的和一个用于加密的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对。因此，在一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，除]{style="font-family:宋体"}[RSA]{lang="EN-US"}[签名密钥对和]{style="font-family:宋体"}[RSA]{lang="EN-US"}[加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。]{style="font-family:宋体"}

[[本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。]{style="font-family:宋体"}]{#struct_0_18308_19795_1132067749}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1405962418}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x387305254}[指定证书申请所使用的]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[密钥对为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x673936491}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] public-key ecdsa name abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_495566476}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_x1719320986}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_x1856165870}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[公钥管理）]{lang="EN-US" style="font-family:宋体"}
:::::

::: {#847358308 .myid}
[]{#_Toc404793094}[]{#struct_0_18308_19795_x801239370}[]{#_Toc285123231}

**PKI \-- PKI配置命令 \-- public-key rsa**

------------------------------------------------------------------------

[**[public-key rsa]{lang="EN-US"}**]{#struct_0_18308_19795_1132133285}[命令用来指定证书申请使用的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对。]{style="font-family:宋体"}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_x651392625}[命令用来取消指定的密钥对。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1012922097}

[**[public-key rsa ]{lang="EN-US"}**[{ {]{lang="EN-US"}[ **encryption name** *encryption-key-name* \[ **length** *key-length* \] \| **signature name** *signature-key-name* \[ **length** *key-length* \] } \* \| **general name** *key-name* \[ **length** *key-length* \] }]{lang="EN-US"}]{#struct_0_18308_19795_x1853291882}

[**[undo public-key]{lang="EN-US"}**]{#struct_0_18308_19795_x1573107286}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x383573492}

[[未指定任何密钥对。]{style="font-family:宋体"}]{#struct_0_18308_19795_741920825}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x901083080}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_2107603931}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132198821}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x662652462}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1148253507}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x777179803}

[**[encryption]{lang="EN-US"}**]{#struct_0_18308_19795_x712054648}[：指定密钥对的用途为加密。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ encryption-key-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1976851424}[：加密密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字母、数字和连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[signature]{lang="EN-US"}**]{#struct_0_18308_19795_x614610188}[：指定密钥对的用途为签名。]{style="font-family:宋体"}

[**[name]{lang="EN-US"}***[ signature-key-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1091972378}[：签名密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字母、数字和连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[general]{lang="EN-US"}**]{#struct_0_18308_19795_502740968}[：指定密钥对的用途为通用，既可以用于签名也可以用于加密。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[key-name]{lang="EN-US"}*]{#struct_0_18308_19795_1132264357}[：通用密钥对的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写，只能包含字母、数字和连字符"]{style="font-family:宋体"}[-]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[length]{lang="EN-US"}**[ *key-length*]{lang="EN-US"}]{#struct_0_18308_19795_925713140}[：密钥的长度。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[key-length]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[512]{lang="EN-US"}[～]{style="font-family:宋体"}[2048]{lang="EN-US"}[，单位为比特，缺省为]{style="font-family:宋体"}[1024]{lang="EN-US"}[；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[key-length]{lang="EN-US"}*[的取值为]{style="font-family:宋体"}[2048]{lang="EN-US"}[，单位为比特，缺省为]{style="font-family:宋体"}[2048]{lang="EN-US"}[。密钥越长，密钥安全性越高，但相关的公钥运算越耗时。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1851732385}

[[本命令中引用的密钥对并不要求已经存在，可以通过以下任意一种途径获得：]{style="font-family:宋体"}]{#struct_0_18308_19795_1862540176}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过执行]{lang="EN-US" style="font-family:宋体"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_1702515492}[命令生成。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过应用程序认证过程触发生成。例如]{style="font-family:宋体"}]{#struct_0_18308_19795_x927307180}[IKE]{lang="EN-US"}[协商过程中，如果使用数字签名认证方式，则可能会触发生成密钥对。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[通过导入证书（使用]{style="font-family:宋体"}]{#struct_0_18308_19795_272665700}**[pki import]{lang="EN-US"}**[命令）的方式从外界获得。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_889697029}[域中只能同时存在一种算法（]{style="font-family:宋体"}[RSA]{lang="EN-US"}[、]{style="font-family:宋体"}[DSA]{lang="EN-US"}[或]{style="font-family:宋体"}[ECDSA]{lang="EN-US"}[）的密钥对。对于]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对来说，一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中只允许单独存在一种用途的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对，或同时存在一个用于签名的和一个用于加密的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对。因此，在一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中，除]{style="font-family:宋体"}[RSA]{lang="EN-US"}[签名密钥对和]{style="font-family:宋体"}[RSA]{lang="EN-US"}[加密密钥对的配置不会互相覆盖之外，其它类型的新的密钥对配置均会覆盖已有的密钥对配置。]{style="font-family:宋体"}

[[分别指定]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_18308_19795_691237716}[签名密钥对和]{style="font-family:宋体"}[RSA]{lang="EN-US"}[加密密钥对时，它们的密钥长度可以不相同。]{style="font-family:宋体"}

[[本命令中指定的密钥长度仅对将要由设备生成的密钥对有效。如果执行本命令时，设备上已经存在指定名称的密钥对，则后续通过此命令指定的该密钥对的密钥长度没有意义。如果指定名称的密钥对是通过导入证书的方式获得，则通过本命令指定的密钥长度也没有意义。]{style="font-family:宋体"}]{#struct_0_18308_19795_1131805605}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x91108084}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_319279541}[指定证书申请所使用的]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对为]{style="font-family:宋体"}[abc]{lang="EN-US"}[，密钥用途为通用，密钥的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x2114802144}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] public-key rsa general name abc length 2048]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1554109633}[指定证书申请所使用的加密]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对为]{style="font-family:宋体"}[rsa1]{lang="EN-US"}[（密钥的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特），签名]{style="font-family:宋体"}[RSA]{lang="EN-US"}[密钥对为]{style="font-family:宋体"}[sig1]{lang="EN-US"}[（密钥的长度为]{style="font-family:宋体"}[2048]{lang="EN-US"}[比特）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1756211921}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] public-key rsa encryption name rsa1 length 2048]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] public-key rsa signature name sig1 length 2048]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1887052908}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_1224421382}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[public-key local create]{lang="EN-US"}**]{#struct_0_18308_19795_1131871141}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[公钥管理）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#1736882264 .myid}
[]{#_Toc404793095}[]{#struct_0_18308_19795_267100028}

**PKI \-- PKI配置命令 \-- root-certificate fingerprint**

------------------------------------------------------------------------

[**[root-certificate fingerprint]{lang="EN-US"}**]{#struct_0_18308_19795_646523021}[命令用来配置验证]{style="font-family:
宋体"}[CA]{lang="EN-US"}[根证书时所使用的指纹。]{style="font-family:宋体"}

[**[undo root-certificate fingerprint]{lang="EN-US"}**]{#struct_0_18308_19795_18691590}[命令用来取消配置的根证书指纹。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1516760109}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_18308_19795_x2024624532}[模式下：]{style="font-family:宋体"}

[**[root-certificate fingerprint ]{lang="EN-US"}**[{ **md5** \| **sha1** } *string*]{lang="EN-US"}]{#struct_0_18308_19795_x416570006}

[**[undo root-certificate fingerprint]{lang="EN-US"}**]{#struct_0_18308_19795_1278792318}

[[FIPS ]{lang="EN-US"}]{#struct_0_18308_19795_x24437283}[模式下：]{style="font-family:宋体"}

[**[root-certificate fingerprint sha1 ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_18308_19795_1131936677}

[**[undo root-certificate fingerprint]{lang="EN-US"}**]{#struct_0_18308_19795_x496686399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x899739740}

[[未指定验证]{style="font-family:宋体"}[CA]{lang="EN-US"}]{#struct_0_18308_19795_189533393}[根证书时使用的指纹。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1664023298}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x2065845867}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1501073620}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_933670736}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_x246819593}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132002213}

[**[md5]{lang="EN-US"}**]{#struct_0_18308_19795_2079260240}[：使用]{style="font-family:宋体"}[MD5]{lang="EN-US"}[指纹。]{style="font-family:宋体"}

[**[sha1]{lang="EN-US"}**]{#struct_0_18308_19795_x1828640704}[：使用]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[指纹。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_18308_19795_x1432716108}[：指定所使用的指纹信息。当选择]{style="font-family:宋体"}[MD5]{lang="EN-US"}[指纹时，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[必须为]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，并且以]{style="font-family:宋体"}[16]{lang="EN-US"}[进制的形式输入；当选择]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[指纹时，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[必须为]{style="font-family:宋体"}[40]{lang="EN-US"}[个字符的字符串，并且以]{style="font-family:宋体"}[16]{lang="EN-US"}[进制的形式输入。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_588662079}

[[当本地证书申请模式为自动方式且]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1797888213}[域中没有]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书时，必须通过本命令配置验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书时所使用的指纹。当]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商等应用触发设备进行本地证书申请时，设备会自动从]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器上获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，如果获取的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书中包含了本地不存在的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书，则设备会验证该]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书的指纹。此时，如果设备上没有配置]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书指纹或者配置了错误的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书指纹，则本地证书申请失败。]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_557052270}[命令导入]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书或者通过]{style="font-family:宋体"}**[pki retrieval]{lang="EN-US"}**[命令获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书时，可以选择是否配置验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书使用的指纹：如果]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中配置了验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书使用的指纹，则当导入的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书文件或者获取的]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书中包含本地不存在的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书时，直接使用配置的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书指纹进行验证。如果配置了错误的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书指纹，则]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书导入和]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书获取均会失败；否则，需要用户来确认该]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书的]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书指纹是否可信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_1771900317}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x1898826786}[配置验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书时使用的]{style="font-family:宋体"}[MD5]{lang="EN-US"}[指纹。（仅非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下支持）]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1132592037}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] root-certificate fingerprint md5 12EF53FA355CD23E12EF53FA355CD23E]{lang="IT"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1673657773}[配置验证]{style="font-family:宋体"}[CA]{lang="EN-US"}[根证书时使用的]{style="font-family:宋体"}[SHA1]{lang="EN-US"}[指纹。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x655131706}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] root-certificate fingerprint sha1 D1526110AAD7527FB093ED7FC037B0B3CDDDAD93]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1462336874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[certificate request mode]{lang="EN-US"}**]{#struct_0_18308_19795_542314384}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki import]{lang="EN-US"}**]{#struct_0_18308_19795_x1988591478}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki retrieve-certificate]{lang="EN-US"}**]{#struct_0_18308_19795_x5153637}
:::

::: {#1629595628 .myid}
[]{#_Toc404793096}[]{#struct_0_18308_19795_872650254}[]{#_Toc279163108}[]{#_Toc265512480}[]{#_Toc133119718}[]{#_Toc128811560}[]{#_Toc124237081}

**PKI \-- PKI配置命令 \-- rule**

------------------------------------------------------------------------

[**[rule]{lang="EN-US"}**]{#struct_0_18308_19795_1132657573}[命令用来配置证书属性的访问控制规则。]{style="font-family:宋体"}

[**[undo rule]{lang="EN-US"}**]{#struct_0_18308_19795_x1798457599}[命令用来删除指定的证书属性访问控制规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_654244109}

[**[rule]{lang="EN-US"}**[ \[ *id* \] { **deny** \| **permit** } *group-nam*]{lang="EN-US"}*[e]{lang="EN-US"}*]{#struct_0_18308_19795_1396808190}

[**[undo rule ]{lang="EN-US"}***[id]{lang="EN-US"}*]{#struct_0_18308_19795_1451012820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x2001781795}

[[不存在证书属性的访问控制规则。]{style="font-family:宋体"}]{#struct_0_18308_19795_1951504092}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1062186485}

[[证书访问控制策略视图]{style="font-family:宋体"}]{#struct_0_18308_19795_1552086159}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132067746}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1405110450}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_867953311}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_2062336742}

[*[id]{lang="EN-US"}*]{#struct_0_18308_19795_18612806}[：证书属性访问控制规则编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[16]{lang="EN-US"}[，缺省值为当前还未被使用的且合法的最小编号，取值越小优先级越高。]{style="font-family:宋体"}

[**[deny]{lang="EN-US"}**]{#struct_0_18308_19795_x1377483759}[：当证书的属性与所关联的属性组匹配时，认为该证书无效，未通过访问控制策略的检测。]{style="font-family:宋体"}

[**[permit]{lang="EN-US"}**]{#struct_0_18308_19795_x584297258}[：当证书的属性与所关联的属性组匹配时，认为该证书有效，通过了访问控制策略的检测。]{style="font-family:宋体"}

[*[group-name]{lang="EN-US"}*]{#struct_0_18308_19795_1241358869}[：规则所关联的证书属性组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1652037425}

[[配置]{style="font-family:宋体"}]{#struct_0_18308_19795_1132133282}[证书属性访问控制规则时，可以关联一个当前并不存在的证书属性组，后续可以通过命令]{style="font-family:宋体"}**[pki certificate attribute-group]{lang="EN-US"}**[完成相应的配置。]{style="font-family:
宋体"}

[[若]{style="font-family:宋体"}]{#struct_0_18308_19795_x651720305}[规则所关联的证书属性组中没有定义任何属性规则（通过命令]{style="font-family:宋体"}**[attribute]{lang="EN-US"}**[配置），或关联的证书属性组不存在，则认为被检测的]{style="font-family:宋体"}[证书属性与该属性组匹配。]{style="font-family:宋体"}

[[如果一个访问控制策略中有多个规则，则按照规则编号从小到大的顺序遍历所有规则，一旦证书与某一个规则匹配，则立即结束检测，不再继续匹配其它规则；若遍历完所有规则后，证书没有与任何规则匹配，则认为该证书不能通过访问控制策略的检测。]{style="font-family:宋体"}]{#struct_0_18308_19795_x1402670421}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_150810317}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x32657612}[配置一个访问控制规则，要求当证书与证书属性组]{style="font-family:宋体"}[mygroup]{lang="EN-US"}[匹配时，认为该证书有效，通过了访问控制策略的检测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_797906945}

[\[Sysname\] pki certificate access-control-policy mypolicy]{lang="EN-US"}

[\[Sysname-pki-cert-acp-mypolicy\] rule 1 permit mygroup]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1468333551}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attribute]{lang="EN-US"}**]{#struct_0_18308_19795_1493359427}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display pki certificate access-control-policy]{lang="EN-US"}**]{#struct_0_18308_19795_1765162847}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki certificate attribute-group]{lang="EN-US"}**]{#struct_0_18308_19795_1132198818}
:::

::: {#-773629 .myid}
[]{#_Toc404793097}[]{#struct_0_18308_19795_x662062635}

**PKI \-- PKI配置命令 \-- source**

------------------------------------------------------------------------

[**[source]{lang="EN-US"}**]{#struct_0_18308_19795_x759232104}[命令用来指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[操作产生的协议报文使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo source]{lang="EN-US"}**]{#struct_0_18308_19795_x1770583888}[命令用来取消指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1330795521}

[**[source ]{lang="EN-US"}**[{ **ip** \| **ipv6** } { *ip-address* *\|* **interface** *interface-type interface-number* }]{lang="EN-US"}]{#struct_0_18308_19795_x1957126403}

[**[undo source]{lang="EN-US"}**]{#struct_0_18308_19795_x698679499}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_446631164}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x1294617791}[操作产生的协议报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为系统根据路由表项查找到的出接口的地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132264354}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_925516532}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1352598543}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x907390234}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_964817156}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_x116992417}

[**[ip ]{lang="SV"}**]{#struct_0_18308_19795_930605517}*[ip-address]{lang="SV"}*[：]{lang="EN-US" style="font-family:宋体"}[指定源]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[**[ipv6 ]{lang="SV"}**]{#struct_0_18308_19795_x1288075138}*[ip-address]{lang="SV"}*[：]{lang="EN-US" style="font-family:宋体"}[指定源]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[**[interface ]{lang="SV"}**]{#struct_0_18308_19795_1643344233}*[interface-type interface-number]{lang="SV"}*[：指定]{lang="EN-US" style="font-family:宋体"}[该接口的]{lang="EN-US" style="font-family:宋体"}[主]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="SV"}[地址或接口上最小的]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="SV"}[地址为源]{lang="EN-US" style="font-family:宋体"}[IP]{lang="SV"}[地址。]{lang="EN-US" style="font-family:宋体"}*[interface-type interface-number]{lang="SV"}*[表示]{lang="EN-US" style="font-family:宋体"}[接口类型和接口编号。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1131805602}

[[如果希望]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x91566836}[操作产生的协议报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是一个特定的地址，则需要配置此命令，例如]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器上的策略要求仅接受来自指定地址或网段的证书申请。如果该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是动态获取的，则可以指定一个接口，使用该接口上的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址作为源地址。]{style="font-family:宋体"}

[[此处指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_18308_19795_762476473}[地址，必须与]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器之间路由可达。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x315209943}[域中只能存在一个源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，后配置的生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x219938252}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_x752781353}[指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[操作产生的协议报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[111.1.1.8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x166756845}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] source ip 111.1.1.8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1144839429}[指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[操作产生的协议报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1::8]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_1131871138}

[\[Sysname\] pki domain 1]{lang="EN-US"}

[\[Sysname-pki-domain-1\] source ipv6 1::8]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_267689849}[指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[操作产生的协议报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_676823612}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] source ip interface gigabitethernet 1/0/1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_893448616}[指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[操作产生的协议报文的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为接口]{style="font-family:宋体"}[GigabitEthernet1/0/1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x1801239292}

[\[Sysname\] pki domain 1]{lang="EN-US"}

[\[Sysname-pki-domain-1\] source ipv6 interface gigabitethernet 1/0/1]{lang="EN-US"}
:::

::: {#-1970034355 .myid}
[]{#_Toc404793098}[]{#struct_0_18308_19795_1678956337}[]{#_Toc279490541}[]{#_Toc279082870}[]{#_Toc265512482}[]{#_Toc61836619}

**PKI \-- PKI配置命令 \-- state**

------------------------------------------------------------------------

[**[state]{lang="EN-US"}**]{#struct_0_18308_19795_2041311106}[命令用来配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的州或省的名称。]{style="font-family:宋体"}

[**[undo state]{lang="EN-US"}**]{#struct_0_18308_19795_61975373}[命令用来删除配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[所属的州或省的名称。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1131936674}

[**[state ]{lang="EN-US"}***[state-name]{lang="EN-US"}*]{#struct_0_18308_19795_x496489791}

[**[undo state]{lang="EN-US"}**]{#struct_0_18308_19795_x87487303}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x631212129}

[[未配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_18308_19795_x345322716}[实体所属的州或省的名称。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1792747448}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_603639010}[实体视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_x695077133}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_310483422}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_1132002210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_2079325776}

[*[state-name]{lang="EN-US"}*]{#struct_0_18308_19795_x1031240271}[：]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体所属的州或省的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写，不能包含逗号。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_973949279}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_477436781}[配置]{style="font-family:宋体"}[PKI]{lang="EN-US"}[实体]{style="font-family:宋体"}[en]{lang="EN-US"}[所在省为]{style="font-family:宋体"}[countryA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_x976853268}

[\[Sysname\] pki entity en]{lang="EN-US"}

[\[Sysname-pki-entity-en\] state countryA]{lang="EN-US"}
:::

::: {#842377611 .myid}
[]{#_Toc404793099}[]{#struct_0_18308_19795_x188254308}[]{#_Toc298870255}[]{#_Toc298924404}

**PKI \-- PKI配置命令 \-- usage**

------------------------------------------------------------------------

[**[usage]{lang="EN-US"}**]{#struct_0_18308_19795_1132592034}[命令用来指定证书的扩展用途。]{style="font-family:宋体"}

[**[undo usage]{lang="EN-US"}**]{#struct_0_18308_19795_1673592237}[命令用来删除指定证书的扩展用途。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_18308_19795_1298013594}

[**[usage ]{lang="EN-US"}**[{ **ike** \| **ssl-client** \| **ssl-server** } **\***]{lang="EN-US"}]{#struct_0_18308_19795_x2043020589}

[**[undo usage ]{lang="EN-US"}**[\[ **ike** \| **ssl-client** \| **ssl-server** \] **\***]{lang="EN-US"}]{#struct_0_18308_19795_x1911177602}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1291248302}

[[未指定证书的扩展用途，表示可用于所有用途。]{style="font-family:宋体"}]{#struct_0_18308_19795_626959267}

[[【视图】]{style="font-family:黑体"}]{#struct_0_18308_19795_1412439729}

[[PKI]{lang="EN-US"}]{#struct_0_18308_19795_318715104}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_18308_19795_1132657570}

[[network-admin]{lang="EN-US"}]{#struct_0_18308_19795_x1798523135}

[[mdc-admin]{lang="EN-US"}]{#struct_0_18308_19795_891520504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_18308_19795_1963621565}

[**[ike]{lang="FR"}**]{#struct_0_18308_19795_1104070687}[：]{style="font-family:宋体"}[指定证书扩展用途为]{style="font-family:宋体"}[IKE]{lang="FR"}[，即]{style="font-family:宋体"}[IKE]{lang="FR"}[对等体使用的证书]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[ssl-client]{lang="FR"}**]{#struct_0_18308_19795_151528418}[：]{lang="EN-US" style="font-family:宋体"}[指定证书扩展用途为]{lang="EN-US" style="font-family:
宋体"}[SSL]{lang="FR"}[客户端，即]{lang="EN-US" style="font-family:
宋体"}[SSL]{lang="FR"}[客户端使用]{lang="EN-US" style="font-family:
宋体"}[的]{style="font-family:宋体"}[证书]{lang="EN-US" style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[**[ssl-server]{lang="FR"}**]{#struct_0_18308_19795_1549326282}**[：]{lang="EN-US" style="font-family:宋体"}**[指定证书扩展用途为]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="FR"}[服务器端，即]{lang="EN-US" style="font-family:宋体"}[SSL]{lang="FR"}[服务器端使用]{lang="EN-US" style="font-family:宋体"}[的]{style="font-family:宋体"}[证书。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_18308_19795_1773439054}

[[若不指定任何参数，则]{style="font-family:宋体"}]{#struct_0_18308_19795_1524767500}**[undo usage]{lang="FR"}**[命令表示删除所有指定的证书扩展用途，证书的用途由证书的使用者决定，]{style="font-family:宋体"}[PKI]{lang="FR"}[不做任何限定。]{style="font-family:宋体"}

[[证书中携带的]{style="font-family:宋体"}]{#struct_0_18308_19795_1132067747}[扩展用途与]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器的策略相关，申请到的证书中的扩展用途可能与此处指定的不完全一致，最终请以]{style="font-family:宋体"}[CA]{lang="EN-US"}[服务器的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_18308_19795_x1405044914}

[[\# ]{lang="EN-US"}]{#struct_0_18308_19795_1235077521}[指定证书扩展用途为]{style="font-family:宋体"}[IKE]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_18308_19795_476034892}

[\[Sysname\] pki domain aaa]{lang="EN-US"}

[\[Sysname-pki-domain-aaa\] usage ike]{lang="EN-US"}
:::
