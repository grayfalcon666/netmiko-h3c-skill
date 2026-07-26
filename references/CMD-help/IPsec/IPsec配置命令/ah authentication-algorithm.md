::: {#2023285187 .myid}
[]{#_Toc404793263}[]{#struct_0_x5828_x5730_x425183273}

**IPsec \-- IPsec配置命令 \-- ah authentication-algorithm**

------------------------------------------------------------------------

[**[ah authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1352937969}[命令用来配置]{style="font-family:
宋体"}[AH]{lang="EN-US"}[协议采用的认证算法。]{style="font-family:宋体"}

[**[undo ah authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1903089582}[命令用来删除所有指定的]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议采用的认证算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1026950036}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x1145907534}[模式下：]{style="font-family:宋体"}

[**[ah authentication-algorithm ]{lang="EN-US"}**[{ **md5** \| **sha1** } \*]{lang="EN-US"}]{#struct_0_x5828_x5730_1737807016}

[**[undo ah authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_1828697666}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353527796}[模式下：]{style="font-family:宋体"}

[**[ah authentication-algorithm sha1]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1800264879}

[**[undo ah authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x543878446}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_574076581}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_1404687782}[协议没有采用任何认证算法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1998619009}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1917206264}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1353462260}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1991239126}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x726806567}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1278023843}

[**[md5]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_1137617318}[：采用]{style="font-family:宋体;
color:black"}[HMAC-MD5]{lang="EN-US"}[认证算法，密钥长度]{style="font-family:
宋体;color:black"}[128]{lang="EN-US" style="color:black"}[比特。]{style="font-family:宋体;color:black"}

[**[sha1]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x470829305}[：采用]{style="font-family:
宋体;color:black"}[HMAC-SHA1]{lang="EN-US"}[认证算法，密钥长度]{style="font-family:宋体;color:black"}[160]{lang="EN-US" style="color:black"}[比特。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1507399280}

[[非]{style="font-family:宋体;color:black"}[FIPS]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_x382038020}[模式下，每个]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}[安全提议中均可以配置多个]{style="font-family:宋体;color:black"}[AH]{lang="EN-US" style="color:black"}[认证算法，其优先级为配置顺序。]{style="font-family:宋体;color:black"}

[[对于手工方式以及]{style="font-family:宋体"}[IKEv1]{lang="EN-US"}]{#struct_0_x5828_x5730_1557110576}[（]{style="font-family:宋体"}[第]{style="font-family:宋体"}[1]{lang="EN-US"}[版本的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协议]{style="font-family:宋体"}[）协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置顺序首位的]{style="font-family:宋体"}[AH]{lang="EN-US"}[认证算法生效。为保证成功建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道，隧道两端指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置的首个]{style="font-family:宋体"}[AH]{lang="EN-US"}[认证算法需要一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x39860274}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_92355893}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议采用的]{style="font-family:宋体"}[AH]{lang="EN-US"}[认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[160]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1354446464}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] ah authentication-algorithm sha1]{lang="EN-US"}
:::

::: {#-1461383778 .myid}
[]{#_Toc404793264}[]{#struct_0_x5828_x5730_1956538601}[]{#_Toc300044734}

**IPsec \-- IPsec配置命令 \-- description**

------------------------------------------------------------------------

[**[description]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1502557882}[命令用来配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架的描述信息。]{style="font-family:宋体"}

[**[undo description]{lang="EN-US"}**]{#struct_0_x5828_x5730_x675042305}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_18213584}

[**[description ]{lang="EN-US"}***[text]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1353331188}

[**[undo description]{lang="EN-US"}**]{#struct_0_x5828_x5730_487044098}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1210785920}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[无描述信息。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1004495511}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x461280660}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1299832676}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1301206415}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_284495201}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1245229867}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1353789940}

[*[text]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1952177121}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架的描述信息，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[80]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x967943100}

[[当系统中存在多个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2027061114}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架时，可通过配置相应的描述信息来有效区分不同的安全策略。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1136565243}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_688442733}[配置序号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的描述信息为]{style="font-family:宋体"}[CenterToA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_296662845}

[\[Sysname\] ipsec policy policy1 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy1-1\] description CenterToA]{lang="EN-US"}
:::

::: {#961939470 .myid}
[]{#_Toc404793265}[]{#struct_0_x5828_x5730_112501434}[]{#_Toc292201223}[]{#_Toc145229910}[]{#_Toc32567516}

**IPsec \-- IPsec配置命令 \-- display ipsec { ipv6-policy \| policy }**

------------------------------------------------------------------------

[**[display ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353724404}[命令用来显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x499708796}

[**[display]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** } \[ *policy-name* \[ *seq-number* \] \]]{lang="EN-US"}]{#struct_0_x5828_x5730_2135064953}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x316787149}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1965180759}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x961981518}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x680421819}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x1510098555}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x546116417}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353658868}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1312633385}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_1242382795}[：显示]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略的信息。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x208643396}[：显示]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略的信息。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x68125424}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_785192623}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1633922859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1040269089}[IPsec]{lang="EN-US"}[安全策略的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1601315358}[和]{style="font-family:宋体"}*[seq-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[则]{lang="EN-US" style="font-family:宋体"}[显示指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{lang="EN-US" style="font-family:宋体"}[表项]{style="font-family:宋体"}[的信息]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[而没有指定]{lang="EN-US" style="font-family:宋体"}*[seq-number]{lang="EN-US"}*[，则显示]{lang="EN-US" style="font-family:宋体"}[所有名称相同的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{lang="EN-US" style="font-family:宋体"}[表项]{style="font-family:宋体"}[的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1353593332}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x545988972}[显示所有]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec policy]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353527795}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IPsec Policy: mypolicy]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  Mode: manual]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  The policy configuration is incomplete:]{lang="EN-US"}

[           ACL not specified]{lang="EN-US"}

[           Incomplete transform-set configuration]{lang="EN-US"}

[  Description: This is my first IPv4 manual policy]{lang="EN-US"}

[  Security data flow:]{lang="EN-US"}

[  Remote address: 2.5.2.1]{lang="EN-US"}

[  Transform set: transform]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound AH setting:]{lang="EN-US"}

[    AH SPI: 1200 (0x000004b0)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 1400 (0x00000578)]{lang="EN-US"}

[    ESP string-key:]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound AH setting:]{lang="EN-US"}

[    AH SPI: 1300 (0x00000514)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 1500 (0x000005dc)]{lang="EN-US"}

[    ESP string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 2]{lang="EN-US"}

[  Mode: isakmp]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  The policy configuration is incomplete:]{lang="EN-US"}

[           Remote-address not set]{lang="EN-US"}

[           ACL not specified]{lang="EN-US"}

[           Transform-set not set]{lang="EN-US"}

[  Description: This is my first IPv4 Isakmp policy]{lang="EN-US"}

[  Security data flow:]{lang="EN-US"}

[  Selector mode: standard]{lang="EN-US"}

[  Local address:]{lang="EN-US"}

[  Remote address:]{lang="EN-US"}

[  Transform set:]{lang="EN-US"}

[  IKE profile:]{lang="EN-US"}

[  SA duration(time based):]{lang="EN-US"}

[  SA duration(traffic based):]{lang="EN-US"}

[  SA idle time:]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IPsec Policy: mycompletepolicy]{lang="EN-US"}

[Interface: LoopBack2]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  Mode: manual]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Description: This is my complete policy]{lang="EN-US"}

[  Security data flow: 3100]{lang="EN-US"}

[  Remote address: 2.2.2.2]{lang="EN-US"}

[  Transform set: completetransform]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound AH setting:]{lang="EN-US"}

[    AH SPI: 5000 (0x00001388)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 7000 (0x00001b58)]{lang="EN-US"}

[    ESP string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound AH setting:]{lang="EN-US"}

[    AH SPI: 6000 (0x00001770)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 8000 (0x00001f40)]{lang="EN-US"}

[    ESP string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 2]{lang="EN-US"}

[  Mode: isakmp]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Description: This is my complete policy]{lang="EN-US"}

[  Security data flow: 3200]{lang="EN-US"}

[  Selector mode: standard]{lang="EN-US"}

[  Local address:]{lang="EN-US"}

[  Remote address: 5.3.6.9]{lang="EN-US"}

[  Transform set:  completetransform]{lang="EN-US"}

[  IKE profile:]{lang="EN-US"}

[  SA duration(time based):]{lang="EN-US"}

[  SA duration(traffic based):]{lang="EN-US"}

[  SA idle time:]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_928618476}[显示所有]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec ipv6-policy]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353396723}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IPsec Policy: mypolicy]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  Mode: manual]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Description: This is my first IPv6 policy]{lang="EN-US"}

[  Security data flow: 3600]{lang="EN-US"}

[  Remote address: 1000::2]{lang="EN-US"}

[  Transform set: mytransform]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound AH setting:]{lang="EN-US"}

[    AH SPI: 1235 (0x000004d3)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 1236 (0x000004d4)]{lang="EN-US"}

[    ESP string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound AH setting:]{lang="EN-US"}

[    AH SPI: 1237 (0x000004d5)]{lang="EN-US"}

[    AH string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    AH authentication hex key:]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Outbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 1238 (0x000004d6)]{lang="EN-US"}

[    ESP string-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP encryption hex key:]{lang="EN-US"}

[    ESP authentication hex key:]{lang="EN-US"}

[]{#struct_0_x5828_x5730_1526223667}[]{#_Toc138131783}[]{#_Toc95386919}[]{#_Toc85621933}[]{#_Toc81452881}[]{#_Toc74712938}[]{#_Toc74712796}[]{#_Toc72595594}[]{#_Toc66003028}[]{#_Toc60131209}[]{#_Toc42655612}[]{#_Toc40150010}[]{#_Toc535897061}[]{#_Toc534882583}[[表1-1 ]{lang="EN-US"}[display ipsec { ipv6-policy \| policy }]{lang="EN-US"}]{#_Toc533152964}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x579897785}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_228823540}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1029328458}

[[IPsec Policy ]{lang="EN-US"}]{#struct_0_x5828_x5730_1573663702}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1253747039}[安全策略的名称]{style="font-family:宋体"}

[[Interface]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353331187}

[[应用了]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_439989931}[安全策略的接口名称]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x5828_x5730_81602768}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_157614204}[安全策略表项的顺序号]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x5828_x5730_1387929121}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1021622772}[安全策略采用的协商方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[mannul]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353789939}[：手工方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[isakmp]{lang="EN-US"}]{#struct_0_x5828_x5730_x29797284}[：]{lang="EN-US" style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[template]{lang="EN-US"}]{#struct_0_x5828_x5730_823606608}[：策略模板方式]{lang="EN-US" style="font-family:宋体"}

[[The policy configuration is incomplete]{lang="EN-US"}]{#struct_0_x5828_x5730_x33471114}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_263679511}[安全策略配置不完整，可能的原因包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x5828_x5730_x1882799756}[未配置]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353724403}[安全提议未配置]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ACL]{lang="EN-US"}]{#struct_0_x5828_x5730_1872944199}[中没有]{style="font-family:宋体"}**[permit]{lang="EN-US"}**[规则]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1036912213}[安全提议配置不完整]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1472135893}[隧道对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址未指定]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x470367408}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[和密钥与]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[和密钥不匹配]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353658867}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x102779804}[安全策略的描述信息]{style="font-family:宋体"}

[[Security data flow]{lang="EN-US"}]{#struct_0_x5828_x5730_1057360632}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_621356343}[安全策略引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}

[[Selector mode]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353593331}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1020094969}[安全策略的数据流保护方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[standard]{lang="EN-US"}]{#struct_0_x5828_x5730_1932157306}[：标准方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aggregation]{lang="EN-US"}]{#struct_0_x5828_x5730_x145705173}[：聚合方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[per-host]{lang="EN-US"}]{#struct_0_x5828_x5730_x1935756385}[：主机方式]{lang="EN-US" style="font-family:宋体"}

[[Local address]{lang="EN-US"}]{#struct_0_x5828_x5730_x1353003507}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1371115222}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址（仅]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略下存在）]{style="font-family:宋体"}

[[Remote address]{lang="EN-US"}]{#struct_0_x5828_x5730_x1227869707}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_744570788}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或主机名]{style="font-family:宋体"}

[[Transform set ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1352937971}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1546924758}[安全策略引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议的名字]{style="font-family:宋体"}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x1892806641}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1089689608}[安全策略引用的]{style="font-family:宋体"}[IKE Profile]{lang="EN-US"}[的名称]{style="font-family:宋体"}

[[SA duration(time based)]{lang="EN-US"}]{#struct_0_x5828_x5730_212556149}

[[基于时间的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x526869484}[生命周期，单位为秒]{style="font-family:宋体"}

[[SA duration(traffic based)]{lang="EN-US"}]{#struct_0_x5828_x5730_x952165546}

[[基于流量的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1557834491}[生命周期，单位为千字节]{style="font-family:宋体"}

[[SA idle time]{lang="EN-US"}]{#struct_0_x5828_x5730_212621685}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1363295716}[的空闲超时时间，单位为秒]{style="font-family:宋体"}

[[Inbound AH setting]{lang="EN-US"}]{#struct_0_x5828_x5730_x1911907564}

[[入方向采用的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_520049380}[协议的相关设置]{style="font-family:宋体"}

[[outbound AH setting]{lang="EN-US"}]{#struct_0_x5828_x5730_212687221}

[[出方向采用的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_1301286798}[协议的相关设置]{style="font-family:宋体"}

[[AH SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x1688924839}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x2119581244}[协议的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[AH string-key]{lang="EN-US"}]{#struct_0_x5828_x5730_212752757}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x986271000}[协议的字符类型的密钥（若配置，则显示为]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[AH authentication hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_1531492579}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_212294005}[协议的十六进制密钥（若配置，则显示为]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Inbound ESP setting]{lang="EN-US"}]{#struct_0_x5828_x5730_x781572591}

[[入方向采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x2128651365}[协议的相关设置]{style="font-family:宋体"}

[[outbound ESP setting]{lang="EN-US"}]{#struct_0_x5828_x5730_212359541}

[[出方向采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_1159580080}[协议的相关设置]{style="font-family:宋体"}

[[ESP SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x2142755722}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_212425077}[协议的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[ESP string-key]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933032}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1338333453}[协议的字符类型的密钥（若配置，则显示为]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ESP encryption hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_212490613}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_670711005}[协议的十六进制加密密钥（若配置，则显示为]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ESP authentication hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_398591496}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_213080437}[协议的十六进制认证密钥（若配置，则显示为]{style="font-family:宋体"}[\*\*\*\*\*\*]{lang="EN-US"}[）]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x106023635}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1529644060}

::: {#1739385697 .myid}
[]{#_Toc404793266}[]{#struct_0_x5828_x5730_x410409709}[]{#_Toc292201224}[]{#_Toc145229911}

**IPsec \-- IPsec配置命令 \-- display ipsec { ipv6-policy-template \| policy-template }**

------------------------------------------------------------------------

[**[display ipsec]{lang="EN-US"}**[ { **ipv6-policy-template** \| **policy-template** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x707525926}[命令用来显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_349911115}

[**[display]{lang="EN-US"}**[ **ipsec** { **ipv6-policy-template** \| **policy-template** } \[ *template-name* \[ *seq-number* \] \]]{lang="EN-US"}]{#struct_0_x5828_x5730_144169846}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1038292890}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1819282866}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_213145973}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_237779294}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_1477251489}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2020982950}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_1127026503}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_583158442}

[**[ipv6-policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1314180594}[：显示]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略模板的信息。]{style="font-family:宋体"}

[**[policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_244875851}[：显示]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略模板的信息。]{style="font-family:宋体"}

[*[template-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1943723021}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_212556150}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板表项的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1429445661}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则显示所有]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1101714825}[IPsec]{lang="EN-US"}[安全策略模板的信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[template-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_818869751}[和]{style="font-family:宋体"}*[seq-number]{lang="EN-US"}*[，]{style="font-family:宋体"}[则]{lang="EN-US" style="font-family:宋体"}[显示指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{lang="EN-US" style="font-family:宋体"}[模板表项]{style="font-family:宋体"}[的信息]{lang="EN-US" style="font-family:宋体"}[；]{style="font-family:宋体"}[如果指定了]{lang="EN-US" style="font-family:宋体"}*[template-name]{lang="EN-US"}*[而没有指定]{lang="EN-US" style="font-family:宋体"}*[seq-number]{lang="EN-US"}*[，则显示]{lang="EN-US" style="font-family:宋体"}[所有名称相同的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{lang="EN-US" style="font-family:宋体"}[模板表项]{style="font-family:宋体"}[的信息。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_53538443}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_81150556}[显示所有]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略模板的信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec policy-template]{lang="EN-US"}]{#struct_0_x5828_x5730_212621686}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IPsec Policy Template: template]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Description: This is policy template]{lang="EN-US"}

[    Security data flow :]{lang="EN-US"}

[    Selector mode: standard]{lang="EN-US"}

[    Local address:]{lang="EN-US"}

[    IKE profile:  None]{lang="EN-US"}

[    Remote address: 162.105.10.2]{lang="EN-US"}

[    Transform set:  testprop]{lang="EN-US"}

[    IPsec SA local duration(time based): 3600 seconds]{lang="EN-US"}

[    IPsec SA local duration(traffic based): 1843200 kilobytes]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1363295713}[显示所有]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略模板的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec ipv6-policy-template]{lang="EN-US"}]{#struct_0_x5828_x5730_x1911710956}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[IPsec Policy Template: template6]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Description: This is policy template]{lang="EN-US"}

[    Security data flow :]{lang="EN-US"}

[    Selector mode: standard]{lang="EN-US"}

[    Local address:]{lang="EN-US"}

[    IKE profile:  None]{lang="EN-US"}

[    Remote address: 200::1/64]{lang="EN-US"}

[    Transform set: testprop]{lang="EN-US"}

[    IPsec SA local duration(time based): 3600 seconds]{lang="EN-US"}

[    IPsec SA local duration(traffic based): 1843200 kilobytes]{lang="EN-US"}

[[表1-2 ]{lang="EN-US"}[display ipsec { ipv6-policy-template \| policy-template }]{lang="EN-US"}]{#struct_0_x5828_x5730_212687222}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x560664193}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1301286799}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1688859303}

[[IPsec Policy Template]{lang="EN-US"}]{#struct_0_x5828_x5730_x170597294}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_55527792}[安全策略模板名称]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x5828_x5730_x1945811692}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1161945140}[安全策略模板表项的序号]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x5828_x5730_212752758}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x986271009}[安全策略模板的描述信息]{style="font-family:宋体"}

[[Security data flow]{lang="EN-US"}]{#struct_0_x5828_x5730_1530902755}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1959789268}[安全策略模板引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}

[[Selector mode]{lang="EN-US"}]{#struct_0_x5828_x5730_1488452124}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_11963834}[安全策略模板的数据流保护方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[standard]{lang="EN-US"}]{#struct_0_x5828_x5730_579726114}[：标准方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[aggregation]{lang="EN-US"}]{#struct_0_x5828_x5730_x1240431231}[：聚合方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[per-host]{lang="EN-US"}]{#struct_0_x5828_x5730_103505843}[：主机方式]{lang="EN-US" style="font-family:宋体"}

[[Local address]{lang="EN-US"}]{#struct_0_x5828_x5730_x1387939340}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x544152379}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x220725292}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x945380429}[安全策略模板引用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Remote address]{lang="EN-US"}]{#struct_0_x5828_x5730_212294006}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x781572592}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Transform set]{lang="EN-US"}]{#struct_0_x5828_x5730_x2128454757}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x568578713}[安全策略模板引用的安全提议的名字]{style="font-family:宋体"}

[[IPsec SA local duration(time based)]{lang="EN-US"}]{#struct_0_x5828_x5730_355564619}

[[基于时间的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_212359542}[生命周期，单位为秒]{style="font-family:宋体"}

[[IPsec SA local duration(traffic based)]{lang="FR"}]{#struct_0_x5828_x5730_1159580079}

[[基于流量的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x2142165911}[生命周期，单位为千字节]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2035886868}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } **isakmp template**]{lang="EN-US"}]{#struct_0_x5828_x5730_x913170846}

::: {#181058413 .myid}
[]{#_Toc404793267}[]{#struct_0_x5828_x5730_566022678}

**IPsec \-- IPsec配置命令 \-- display ipsec profile**

------------------------------------------------------------------------

[**[display ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1434386765}[命令用来显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212425078}

[**[display ipsec profile]{lang="EN-US"}**[ \[ *profile-name* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933019}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_584111920}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x652850138}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1916800241}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_884120241}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x1754958740}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1401162943}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x322622014}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212490614}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_670711004}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_398591495}

[[如果没有指定任何参数，则显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2072592442}[安全框架的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_558240227}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_997686722}[显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec profile]{lang="EN-US" style="font-size:8.5pt;
font-family:\"Courier New\""}]{#struct_0_x5828_x5730_2141231776}

[[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}]{#struct_0_x5828_x5730_213080438}

[IPsec profile: profile]{lang="EN-US"}

[Mode: manual]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  Description:]{lang="EN-US"}

[  Transform set: prop1]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Inbound AH setting:]{lang="EN-US"}

[    AH SPI: 12345 (0x00003039)]{lang="EN-US"}

[    AH string-key:]{lang="EN-US"}

[    AH authentication hex key: \*\*\*\*\*\*]{lang="EN-US"}

[  Inbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 23456 (0x00005ba0)]{lang="EN-US"}

[    ESP string-key:]{lang="EN-US"}

[    ESP encryption hex-key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP authentication hex-key: \*\*\*\*\*\*]{lang="EN-US"}

[  Outbound AH setting:]{lang="EN-US"}

[    AH SPI: 12345 (0x00003039)]{lang="EN-US"}

[    AH string-key:]{lang="EN-US"}

[    AH authentication hex key: \*\*\*\*\*\*]{lang="EN-US"}

[  Outbound ESP setting:]{lang="EN-US"}

[    ESP SPI: 23456 (0x00005ba0)]{lang="EN-US"}

[    ESP string-key:]{lang="EN-US"}

[    ESP encryption hex key: \*\*\*\*\*\*]{lang="EN-US"}

[    ESP authentication hex key: \*\*\*\*\*\*]{lang="EN-US"}

[[表1-3 ]{lang="EN-US"}[display ipsec profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x106023634}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x559174924}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_213145974}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_237779287}

[[IPsec profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x479063646}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x132221390}[安全框架的名称]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x5828_x5730_530607437}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_656008527}[安全框架采用的协商方式，目前仅支持手工方式（]{style="font-family:宋体"}[mannul]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Description]{lang="EN-US"}]{#struct_0_x5828_x5730_x1530954418}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_212556147}[安全框架的描述信息]{style="font-family:宋体"}

[[Transform set]{lang="EN-US"}]{#struct_0_x5828_x5730_x526869474}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x952165555}[安全策略引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议的名字]{style="font-family:宋体"}

[[Inbound AH setting]{lang="EN-US"}]{#struct_0_x5828_x5730_1557768956}

[[入方向采用的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_845728130}[协议的相关设置]{style="font-family:宋体"}

[[outbound AH setting]{lang="EN-US"}]{#struct_0_x5828_x5730_320391745}

[[出方向采用的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_212621683}[协议的相关设置]{style="font-family:宋体"}

[[AH SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_1363295718}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x1912038636}[协议的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[AH string-key]{lang="EN-US"}]{#struct_0_x5828_x5730_x2020225101}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x2107696867}[协议的字符类型的密钥]{style="font-family:宋体"}

[[AH authentication hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_212687219}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x1037365354}[协议的十六进制密钥]{style="font-family:宋体"}

[[Inbound ESP setting]{lang="EN-US"}]{#struct_0_x5828_x5730_1251793987}

[[入方向采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_1646249687}[协议的相关设置]{style="font-family:宋体"}

[[outbound ESP setting]{lang="EN-US"}]{#struct_0_x5828_x5730_x788832894}

[[出方向采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_212752755}[协议的相关设置]{style="font-family:宋体"}

[[ESP SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x986270998}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x388611009}[协议的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[ESP string-key]{lang="EN-US"}]{#struct_0_x5828_x5730_1485683143}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_212294003}[协议的字符类型的密钥]{style="font-family:宋体"}

[[ESP encryption hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_x781572589}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x2129175652}[协议的十六进制加密密钥]{style="font-family:宋体"}

[[ESP authentication hex key]{lang="EN-US"}]{#struct_0_x5828_x5730_1959783698}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1592277288}[协议的十六进制认证密钥]{style="font-family:宋体"}

[ ]{lang="EN-US" style="font-size:8.5pt;font-family:\"Courier New\""}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212359539}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}**[ipsec p]{lang="EN-US"}**]{#struct_0_x5828_x5730_1968884136}**[rofile]{lang="EN-US"}**

::: {#1166989323 .myid}
[]{#_Toc404793268}[]{#struct_0_x5828_x5730_681387313}[]{#_Toc292201227}[]{#_Toc145229913}[]{#_Toc32567518}

**IPsec \-- IPsec配置命令 \-- display ipsec sa**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipsec** **sa**]{lang="EN-US"}]{#struct_0_x5828_x5730_362711770}[命令用来显示]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的相关信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1589201245}

[**[display]{lang="EN-US"}**[ **ipsec** **sa** \[ **brief** \| **count** \| **interface** *interface-type interface-number* \| { **ipv6-policy** \| **policy** } *policy-name* \[ *seq-number* \] \| **profile** *profile-name* \| **remote** \[ **ipv6** \] *ip-address* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x2121528316}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_193965438}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1342291339}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_212425075}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933030}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_1793834429}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1783354862}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x1680791438}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_490364296}

[**[brief]{lang="EN-US"}**]{#struct_0_x5828_x5730_50669173}[：显示所有的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x5828_x5730_x643140671}[：显示]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的个数。]{style="font-family:宋体"}

[**[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_212490611}[：显示指定接口下的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号。]{style="font-family:宋体"}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_670711007}[：显示由指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_398591494}[：显示由指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_2072592441}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_558174691}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x402173879}[：显示由指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x524583873}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}***[ ip-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_1551195918}[：显示指定对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_127983081}[：显示指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[对端地址的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。若不指定本参数，则表示显示指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[对端地址的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_213080435}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[如果不指定任何参数，则显示所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x106023637}[的详细信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1529512988}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_845823733}[显示]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec sa brief]{lang="EN-US"}]{#struct_0_x5828_x5730_1338511010}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface/Global   Dst Address      SPI         Protocol  Status]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[GE1/0/1            10.1.1.1         400         ESP       Active]{lang="EN-US"}

[GE1/0/1            255.255.255.255  4294967295  ESP       Active]{lang="EN-US"}

[GE1/0/1            100::1/64        500         AH        Active]{lang="EN-US"}

[Global             \--               600         ESP       Active]{lang="EN-US"}

[]{#struct_0_x5828_x5730_x1210146850}[]{#_Toc138131786}[]{#_Toc95386922}[]{#_Toc85621936}[]{#_Toc81452884}[]{#_Toc74712941}[]{#_Toc74712799}[]{#_Toc72595597}[]{#_Toc66003031}[]{#_Toc60131212}[]{#_Toc42655615}[]{#_Toc40150013}[]{#_Toc535897055}[]{#_Toc534882577}[[表1-4 ]{lang="EN-US"}[display ipsec sa brief]{lang="EN-US"}]{#_Toc533152958}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x568550826}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_213145971}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_237779292}

[[Interface/Global]{lang="PT-BR"}]{#struct_0_x5828_x5730_1477251487}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_2021376166}[属于的接口或是全局（全局]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[由]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架生成）]{style="font-family:宋体"}

[[Dst Address]{lang="EN-US"}]{#struct_0_x5828_x5730_734346628}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_14577090}[隧道对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_212556148}[安全框架生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[中，该值无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x526869483}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x951706794}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[Protocol]{lang="EN-US"}]{#struct_0_x5828_x5730_x650627309}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x195575155}[采用的安全协议]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x5828_x5730_1669563356}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_212621684}[的状态：主用（]{style="font-family:宋体"}[Active]{lang="EN-US"}[）、备用（]{style="font-family:宋体"}[Backup]{lang="EN-US"}[）]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多机备份环境下，取值为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2132451935}[Active]{lang="EN-US"}[表示主用、取值为]{style="font-family:宋体"}[Standby]{lang="EN-US"}[表示备用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单机运行环境下，仅为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1363295715}[Active]{lang="EN-US"}[，表示]{style="font-family:宋体"}[SA]{lang="EN-US"}[处于可用状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1911842028}[显示]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的个数。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec sa count]{lang="EN-US"}]{#struct_0_x5828_x5730_548689591}

[Total IPsec SAs count]{lang="EN-US"}[：]{style="font-family:宋体"}[4]{lang="EN-US"}

[[\# ]{lang="FR"}]{#struct_0_x5828_x5730_x217797620}[显示所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的详细信息]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec sa]{lang="EN-US"}]{#struct_0_x5828_x5730_212752756}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Interface: GigabitEthernet1/0/1]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  IPsec policy: r2]{lang="EN-US"}

[  Sequence number: 1]{lang="EN-US"}

[  Mode: ISAKMP]{lang="EN-US"}

[  Flow table status]{lang="EN-US"}[：]{style="font-family:宋体"}[Active]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Tunnel id: 3]{lang="EN-US"}

[    Encapsulation mode: tunnel]{lang="EN-US"}

[    Perfect Forward Secrecy:]{lang="EN-US"}

[    Inside VRF: vp1]{lang="EN-US"}

[    Path MTU: 1443]{lang="EN-US"}

[    Tunnel:]{lang="EN-US"}

[        local  address: 2.2.2.2]{lang="EN-US"}

[        remote address: 1.1.1.2]{lang="EN-US"}

[    Flow:]{lang="EN-US"}

[    sour addr: 192.168.2.0/255.255.255.0  port: 0  protocol: ip]{lang="EN-US"}

[    dest addr: 192.168.1.0/255.255.255.0  port: 0  protocol: ip]{lang="EN-US"}

[ ]{lang="EN-US"}

[    \[Inbound ESP SAs\]]{lang="EN-US"}

[      SPI: 3564837569 (0xd47b1ac1)]{lang="EN-US"}

[      Connection ID]{lang="EN-US"}[：]{style="font-family:宋体"}[ 1]{lang="EN-US"}

[      Transform set: ESP-ENCRYPT-AES-CBC-128 ESP-AUTH-SHA1]{lang="EN-US"}

[      SA duration (kilobytes/sec): 4294967295/604800]{lang="EN-US"}

[      SA remaining duration (kilobytes/sec): 1843200/2686]{lang="EN-US"}

[      Max received sequence-number: 5]{lang="EN-US"}

[      Anti-replay check enable: Y]{lang="EN-US"}

[      Anti-replay window size: 32]{lang="EN-US"}

[      UDP encapsulation used for NAT traversal: N]{lang="EN-US"}

[      Status: Active]{lang="EN-US"}

[ ]{lang="EN-US"}

[    \[Outbound ESP SAs\]]{lang="EN-US"}

[      SPI: 801701189 (0x2fc8fd45)]{lang="EN-US"}

[      Connection ID]{lang="EN-US"}[：]{style="font-family:宋体"}[ 2]{lang="EN-US"}

[      Transform set: ESP-ENCRYPT-AES-CBC-128 ESP-AUTH-SHA1]{lang="EN-US"}

[      SA duration (kilobytes/sec): 4294967295/604800]{lang="EN-US"}

[      SA remaining duration (kilobytes/sec): 1843200/2686]{lang="FR"}

[      ]{lang="FR"}[Max sent sequence-number: 6]{lang="EN-US"}

[      UDP encapsulation used for NAT traversal: N]{lang="EN-US"}

[      Status: Active]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Global IPsec SA]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ ]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[  IPsec profile: profile]{lang="EN-US"}

[  Mode: Manual]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Encapsulation mode: transport]{lang="EN-US"}

[    \[Inbound AH SAs\]]{lang="EN-US"}

[      SPI: 1234563 (0x0012d683)]{lang="EN-US"}

[      Connection ID]{lang="EN-US"}[：]{style="font-family:宋体"}[ 9]{lang="EN-US"}

[      Transform set: AH-SHA1]{lang="EN-US"}

[      No duration limit for this SA]{lang="EN-US"}

[    \[Outbound AH SAs\]]{lang="EN-US"}

[      SPI: 1234563 (0x002d683)]{lang="EN-US"}

[      Connection ID]{lang="EN-US"}[：]{style="font-family:宋体"}[ 10]{lang="EN-US"}

[      Transform set: AH-SHA1]{lang="EN-US"}

[      No duration limit for this SA]{lang="EN-US"}

[]{#struct_0_x5828_x5730_x986270999}[]{#_Toc138131787}[]{#_Toc95386923}[]{#_Toc85621937}[]{#_Toc81452885}[]{#_Toc74712942}[]{#_Toc74712800}[]{#_Toc72595598}[]{#_Toc66003032}[]{#_Toc60131213}[]{#_Toc42655616}[]{#_Toc40150014}[]{#_Toc535897057}[]{#_Toc534882579}[[表1-5 ]{lang="EN-US"}[display ipsec sa]{lang="EN-US"}]{#_Toc533152960}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x566518907}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212294004}

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x781572590}

[[Interface]{lang="EN-US"}]{#struct_0_x5828_x5730_x2128585829}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1648146261}[所在的接口]{style="font-family:宋体"}

[[Global IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_295929882}

[[全局]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_273857828}

[[IPsec policy]{lang="EN-US"}]{#struct_0_x5828_x5730_212359540}

[[采用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1159580081}[安全策略名]{style="font-family:宋体"}

[[IPsec profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x2142690186}

[[采用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_955849714}[安全框架名]{style="font-family:宋体"}

[[Sequence number]{lang="EN-US"}]{#struct_0_x5828_x5730_1493766643}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1333608838}[安全策略表项顺序号]{style="font-family:宋体"}

[[Mode]{lang="EN-US"}]{#struct_0_x5828_x5730_212425076}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933033}[安全策略采用的协商方式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Mannul]{lang="EN-US"}]{#struct_0_x5828_x5730_1390549902}[：手工方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ISAKMP]{lang="EN-US"}]{#struct_0_x5828_x5730_693190295}[：]{lang="EN-US" style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Template]{lang="EN-US"}]{#struct_0_x5828_x5730_208496800}[：]{style="font-family:宋体"}[IKE]{lang="EN-US"}[模板方式]{style="font-family:宋体"}

[[Flow table status]{lang="EN-US"}]{#struct_0_x5828_x5730_2132714079}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1798359532}[下发引流规则的状态，包括以下取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Inactive]{lang="EN-US"}]{#struct_0_x5828_x5730_2132910687}[：]{lang="EN-US" style="font-family:宋体"}[引流规则下发失败]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_x5828_x5730_145819465}[：]{lang="EN-US" style="font-family:宋体"}[引流规则下发成功]{style="font-family:宋体"}

[[该字段的显示与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2113884811}

[[Tunnel id]{lang="EN-US"}]{#struct_0_x5828_x5730_x1156193930}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_212490612}[隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Encapsulation mode]{lang="EN-US"}]{#struct_0_x5828_x5730_670711006}

[[采用的报文封装模式，有两种：传输（]{style="font-family:宋体"}[transport]{lang="EN-US"}]{#struct_0_x5828_x5730_398591493}[）和隧道（]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[）模式]{style="font-family:宋体"}

[[Perfect Forward Secrecy]{lang="EN-US"}]{#struct_0_x5828_x5730_2072592440}

[[此]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_558109155}[安全策略发起协商时使用完善的前向安全（]{style="font-family:宋体"}[PFS]{lang="EN-US"}[）特性，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[768-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_213080436}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group1]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1024-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_x106023636}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group2]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1536-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_x1529578524}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group5]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2048-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_1418167883}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group14]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2048-bit]{lang="EN-US"}]{#struct_0_x5828_x5730_213145972}[和]{lang="EN-US" style="font-family:宋体"}[256_bit]{lang="EN-US"}[子群]{lang="EN-US" style="font-family:宋体"}[Diffie-Hellman]{lang="EN-US"}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group24]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[Inside VRF]{lang="EN-US"}]{#struct_0_x5828_x5730_x2046934749}

[[被保护数据所属的]{style="font-family:宋体"}[VRF]{lang="EN-US"}]{#struct_0_x5828_x5730_1406195470}[实例名称]{style="font-family:宋体"}

[[Path MTU]{lang="EN-US"}]{#struct_0_x5828_x5730_237779293}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1477251486}[的路径]{style="font-family:宋体"}[MTU]{lang="EN-US"}[值]{style="font-family:宋体"}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_2021310630}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x428136771}[隧道的端点地址信息]{style="font-family:宋体"}

[[local address]{lang="EN-US"}]{#struct_0_x5828_x5730_212556145}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x526869472}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[remote address]{lang="EN-US"}]{#struct_0_x5828_x5730_x951772339}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1856370311}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Flow]{lang="EN-US"}]{#struct_0_x5828_x5730_212621681}

[[受保护的数据流信息]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1363295720}

[[sour addr]{lang="EN-US"}]{#struct_0_x5828_x5730_x1911514349}

[[数据流的源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_212687217}[地址]{style="font-family:宋体"}

[[dest addr]{lang="EN-US"}]{#struct_0_x5828_x5730_x1037365356}

[[数据流的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_88994573}[地址]{style="font-family:宋体"}

[[port]{lang="EN-US"}]{#struct_0_x5828_x5730_1588313680}

[[端口号]{style="font-family:宋体"}]{#struct_0_x5828_x5730_212752753}

[[protocol]{lang="EN-US"}]{#struct_0_x5828_x5730_x986271004}

[[协议类型，取值包括：]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1531230435}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ip]{lang="EN-US"}]{#struct_0_x5828_x5730_x1383209169}[：]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[协议]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ipv6]{lang="EN-US"}]{#struct_0_x5828_x5730_x852589241}[：]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[协议]{style="font-family:宋体"}

[[Inbound ESP SAs]{lang="EN-US"}]{#struct_0_x5828_x5730_x2091685}

[[入方向的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_212294001}[协议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Outbound ESP SAs]{lang="EN-US"}]{#struct_0_x5828_x5730_x781572587}

[[出方向的]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x2128782436}[协议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Inbound AH SAs]{lang="EN-US"}]{#struct_0_x5828_x5730_212359537}

[[入方向的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_1968884146}[协议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[Outbound AH SAs]{lang="EN-US"}]{#struct_0_x5828_x5730_681387316}

[[出方向的]{style="font-family:宋体"}[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_212425073}[协议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[信息]{style="font-family:宋体"}

[[SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933028}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x2144968043}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[Connection ID]{lang="EN-US"}]{#struct_0_x5828_x5730_1821634908}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1444388558}[标识]{style="font-family:宋体"}

[[Transform set]{lang="EN-US"}]{#struct_0_x5828_x5730_212490609}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1667941161}[安全提议所采用的安全协议及算法]{style="font-family:宋体"}

[[SA duration ]{lang="FR"}[(kilobytes/sec)]{lang="EN-US"}]{#struct_0_x5828_x5730_x1400140261}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_290203286}[生存时间，单位为千字节或者秒]{style="font-family:宋体"}

[[SA remaining duration (kilobytes/sec)]{lang="EN-US"}]{#struct_0_x5828_x5730_213080433}

[[剩余的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x106023639}[生存时间，单位为千字节或者秒]{style="font-family:宋体"}

[[Max received sequence-number]{lang="EN-US"}]{#struct_0_x5828_x5730_x1529906204}

[[入方向接收到的报文最大序列号]{style="font-family:宋体"}]{#struct_0_x5828_x5730_213145969}

[[Max sent sequence-number]{lang="EN-US"}]{#struct_0_x5828_x5730_x1718535852}

[[出方向发送的报文最大序列号]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2147226675}

[[Anti-replay check enable]{lang="EN-US"}]{#struct_0_x5828_x5730_212556146}

[[抗重放检测功能是否使能]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x526869473}

[[Anti-replay window size]{lang="EN-US"}]{#struct_0_x5828_x5730_x951706803}

[[抗重放窗口宽度]{style="font-family:宋体"}]{#struct_0_x5828_x5730_212621682}

[[UDP encapsulation used for NAT traversal]{lang="EN-US"}]{#struct_0_x5828_x5730_1363295717}

[[此]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1911973100}[是否使用]{style="font-family:宋体"}[NAT]{lang="EN-US"}[穿越功能]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x5828_x5730_212687218}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1037365355}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多机备份环境下，取值为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x596234809}[Active]{lang="EN-US"}[表示]{style="font-family:宋体"}[主用、取值为]{style="font-family:宋体"}[Standby]{lang="EN-US"}[表示]{style="font-family:宋体"}[备用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单机运行环境下，取值仅为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_120518638}[Active]{lang="EN-US"}[，表示]{style="font-family:宋体"}[SA]{lang="EN-US"}[处于可用状态]{style="font-family:宋体"}

[[No duration limit for this SA]{lang="EN-US"}]{#struct_0_x5828_x5730_212752754}

[[手工方式创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x986270997}[无生命周期]{style="font-family:宋体"}

[]{#_Toc292201230}[]{#_Toc145229916}[]{#_Toc300907100}[[ ]{lang="EN-US"}]{#_Toc145229915}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x388545473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec sa global-duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1233613867}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x24769560}

::: {#975151035 .myid}
[]{#_Toc404793269}[]{#struct_0_x5828_x5730_x427510849}

**IPsec \-- IPsec配置命令 \-- display ipsec statistics**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipsec** **statistics**]{lang="EN-US"}]{#struct_0_x5828_x5730_2000945469}[命令用来显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理的报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212294002}

[**[display ipsec statistics ]{lang="EN-US"}**[\[ **tunnel-id** *tunnel-id* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x781572588}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2129110116}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1840176419}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x577730538}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2101214562}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_165981859}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x796997399}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_348363563}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_212359538}

[**[tunnel-id ]{lang="EN-US"}***[tunnel-id]{lang="EN-US"}*]{#struct_0_x5828_x5730_1968884137}[：显示指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道处理的报文统计信息。其中，]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围与设备的型号有关，请以设备的实际情况为准。通过]{style="font-family:宋体"}**[display ipsec tunnel brief]{lang="EN-US"}**[可以查看到已建立的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_681452849}

[[如果不指定任何参数，则显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1385722966}[处理的所有报文的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x887247110}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1343070744}[显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[处理的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec statistics]{lang="EN-US"}]{#struct_0_x5828_x5730_212425074}

[  IPsec packet statistics:]{lang="EN-US"}

[    Received/sent packets: 47/64]{lang="EN-US"}

[    Received/sent bytes: 3948/5208]{lang="EN-US"}

[    Dropped packets (received/sent): 0/45]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Dropped packets statistics]{lang="EN-US"}

[      No available SA: 0]{lang="EN-US"}

[      Wrong SA: 0]{lang="EN-US"}

[      Invalid length: 0]{lang="EN-US"}

[      Authentication failure: 0]{lang="EN-US"}

[      Encapsulation failure: 0]{lang="EN-US"}

[      Decapsulation failure: 0]{lang="EN-US"}

[      Replayed packets: 0]{lang="EN-US"}

[      ACL check failure: 45]{lang="EN-US"}

[      MTU check failure: 0]{lang="EN-US"}

[      Loopback limit exceeded: 0]{lang="EN-US"}

[      Crypto speed limit exceeded: 0]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x2089933031}[显示]{style="font-family:宋体"}[ID]{lang="EN-US"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[隧道处理的报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec statistics tunnel-id 1]{lang="EN-US"}]{#struct_0_x5828_x5730_212490610}

[  IPsec packet statistics:]{lang="EN-US"}

[    Received/sent packets: 5124/8231]{lang="EN-US"}

[    Received/sent bytes: 52348/64356]{lang="EN-US"}

[    Dropped packets (received/sent): 0/0]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Dropped packets statistics]{lang="EN-US"}

[      No available SA: 0]{lang="EN-US"}

[      Wrong SA: 0]{lang="EN-US"}

[      Invalid length: 0]{lang="EN-US"}

[      Authentication failure: 0]{lang="EN-US"}

[      Encapsulation failure: 0]{lang="EN-US"}

[      Decapsulation failure: 0]{lang="EN-US"}

[      Replayed packets: 0]{lang="EN-US"}

[      ACL check failure: 0]{lang="EN-US"}

[      MTU check failure: 0]{lang="EN-US"}

[      Loopback limit exceeded: 0]{lang="EN-US"}

[      Crypto speed limit exceeded: 0]{lang="EN-US"}

[]{#struct_0_x5828_x5730_670711008}[]{#_Toc138131789}[]{#_Toc95386924}[]{#_Toc85621938}[]{#_Toc81452886}[]{#_Toc74712943}[]{#_Toc74712801}[]{#_Toc72595599}[]{#_Toc66003033}[]{#_Toc60131214}[]{#_Toc42655617}[]{#_Toc40150015}[]{#_Toc535897058}[]{#_Toc534882580}[[表1-6 ]{lang="EN-US"}[display ipsec statistics]{lang="EN-US"}]{#_Toc533152961}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x547660634}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_398591499}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2072592446}

[[IPsec packet statistics]{lang="EN-US"}]{#struct_0_x5828_x5730_557978083}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1184357210}[处理的报文统计信息]{style="font-family:宋体"}

[[Received/sent packets]{lang="EN-US"}]{#struct_0_x5828_x5730_213080434}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5828_x5730_x106023638}[发送的受安全保护的数据包的数目]{style="font-family:宋体"}

[[Received/sent bytes]{lang="EN-US"}]{#struct_0_x5828_x5730_x1529971740}

[[接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5828_x5730_x2120961059}[发送的受安全保护的字节数目]{style="font-family:宋体"}

[[Dropped packets (received/sent)]{lang="EN-US"}]{#struct_0_x5828_x5730_1951368707}

[[被设备丢弃了的受安全保护的数据包的数目（接收]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_x5828_x5730_x1105081844}[发送）]{style="font-family:宋体"}

[[Dropped packets statistics]{lang="EN-US"}]{#struct_0_x5828_x5730_213145970}

[[被丢弃的数据包的详细信息]{style="font-family:宋体"}]{#struct_0_x5828_x5730_237779291}

[[No available SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1477251484}

[[因为找不到]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_2021179558}[而被丢弃的数据包的数目]{style="font-family:宋体"}

[[Wrong SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x76464020}

[[因为]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1889001083}[错误而被丢弃的数据包的数目]{style="font-family:宋体"}

[[Invalid length]{lang="EN-US"}]{#struct_0_x5828_x5730_2134870450}

[[因为数据包长度不正确而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1555957655}

[[Authentication failure]{lang="EN-US"}]{#struct_0_x5828_x5730_245363631}

[[因为认证失败而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x959554255}

[[Encapsulation failure]{lang="EN-US"}]{#struct_0_x5828_x5730_716840963}

[[因为加封装失败而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2134935986}

[[Decapsulation failure]{lang="EN-US"}]{#struct_0_x5828_x5730_849854530}

[[因为解封装失败而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1692258242}

[[Replayed packets]{lang="EN-US"}]{#struct_0_x5828_x5730_x1110068198}

[[被丢弃的重放的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2135001522}

[[ACL check failure]{lang="EN-US"}]{#struct_0_x5828_x5730_1577948161}

[[因为]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_x5828_x5730_x1682534643}[检测失败而被丢弃的数据包的数目]{style="font-family:宋体"}

[[MTU check failure]{lang="EN-US"}]{#struct_0_x5828_x5730_953652259}

[[因为]{style="font-family:宋体"}[MTU]{lang="EN-US"}]{#struct_0_x5828_x5730_756620236}[检测失败而被丢弃的数据包的数目]{style="font-family:宋体"}

[[Loopback limit exceeded]{lang="EN-US"}]{#struct_0_x5828_x5730_2135067058}

[[因为本机处理的次数超过限制而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1984408270}

[[Crypto speed limit exceeded]{lang="EN-US"}]{#struct_0_x5828_x5730_x1614836839}

[[因为加密速度的限制而被丢弃的数据包的数目]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1704470223}

[]{#_Toc299973493}[]{#_Toc272768855}[]{#_Toc33096883}[]{#_Toc33096884}[]{#_Toc292201226}[]{#_Toc145229912}[]{#_Toc141674701}[]{#_Toc141674796}[]{#_Toc141685277}[]{#_Toc141686198}[]{#_Toc141674702}[]{#_Toc141674797}[]{#_Toc141685278}[]{#_Toc141686199}[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2091438611}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset ipsec statistics]{lang="EN-US"}**]{#struct_0_x5828_x5730_x943085607}

::: {#518741201 .myid}
[]{#_Toc404793270}[]{#struct_0_x5828_x5730_1030468249}

**IPsec \-- IPsec配置命令 \-- display ipsec transform-set**

------------------------------------------------------------------------

[**[display ipsec transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_437565803}[命令用来显示]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[安全提议的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_525695989}

[**[display]{lang="EN-US"}**[ **ipsec transform-set** \[ *transform-set-name* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_2134608306}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1180324428}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x125682904}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1854728912}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1908749943}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x1427358126}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x733868208}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_844072942}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_917403341}

[*[transform-set-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_2134673842}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1990688123}

[[如果没有指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1303098257}[安全提议的名字，则显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议的信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_105695429}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x955690617}[显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议的信息。]{style="font-family:宋体"}

[[\<Sysname\> ]{lang="EN-US"}]{#struct_0_x5828_x5730_2134739378}[[display ipsec transform-set]{lang="EN-US"}]{#_Toc533152962}

[IPsec transform set: mytransform]{lang="EN-US"}

[  State: incomplete]{lang="EN-US"}

[  Encapsulation mode: tunnel]{lang="EN-US"}

[  Transform: ESP]{lang="EN-US"}

[ ]{lang="EN-US"}

[IPsec transform set: completeTransform]{lang="EN-US"}

[  State: complete]{lang="EN-US"}

[  Encapsulation mode: transport]{lang="EN-US"}

[  Transform: AH-ESP]{lang="EN-US"}

[  AH protocol:]{lang="EN-US"}

[    Integrity: SHA1]{lang="EN-US"}

[  ESP protocol:]{lang="EN-US"}

[    Integrity: SHA1]{lang="EN-US"}

[    Encryption: AES-CBC-128]{lang="EN-US"}

[]{#struct_0_x5828_x5730_383072445}[]{#_Toc138131785}[]{#_Toc95386921}[]{#_Toc85621935}[]{#_Toc81452883}[]{#_Toc74712940}[]{#_Toc74712798}[]{#_Toc72595596}[]{#_Toc66003030}[]{#_Toc60131211}[]{#_Toc42655614}[]{#_Toc40150012}[]{#_Toc535897059}[[表1-7 ]{lang="EN-US"}[display ipsec transform-set]{lang="EN-US"}]{#_Toc534882581}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x552980895}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2119812523}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1009531632}

[[IPsec transform set ]{lang="EN-US"}]{#struct_0_x5828_x5730_x314927135}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1709590428}[安全提议的名字]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_x5828_x5730_2134804914}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x714066649}[安全提议是否完整]{style="font-family:宋体"}

[[Encapsulation mode]{lang="EN-US"}]{#struct_0_x5828_x5730_x2113488150}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x197597530}[安全提议采用的封装模式，包括两种：传输（]{style="font-family:宋体"}[transport]{lang="EN-US"}[）和隧道（]{style="font-family:宋体"}[tunnel]{lang="EN-US"}[）模式]{style="font-family:宋体"}

[[Transform]{lang="EN-US"}]{#struct_0_x5828_x5730_x2778464}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x479404184}[安全提议采用的安全协议，包括三种：]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议、]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议、]{style="font-family:宋体"}[AH-ESP]{lang="EN-US"}[（先采用]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议，再采用]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议）]{style="font-family:宋体"}

[[AH protocol]{lang="EN-US"}]{#struct_0_x5828_x5730_2135394738}

[[AH]{lang="EN-US"}]{#struct_0_x5828_x5730_x1954400884}[协议相关配置]{style="font-family:宋体"}

[[ESP protocol]{lang="EN-US"}]{#struct_0_x5828_x5730_x938948595}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x208238631}[协议相关配置]{style="font-family:宋体"}

[[Integrity]{lang="EN-US"}]{#struct_0_x5828_x5730_x75197035}

[[安全协议采用的认证算法]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2135460274}

[[Encryption]{lang="EN-US"}]{#struct_0_x5828_x5730_1964247325}

[[安全协议采用的加密算法]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x994278327}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1438417065}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_1993717444}

::: {#-779432565 .myid}
[]{#_Toc404793271}[]{#struct_0_x5828_x5730_x443888405}[]{#_Toc300907103}

**IPsec \-- IPsec配置命令 \-- display ipsec tunnel**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ipsec** **tunnel**]{lang="EN-US"}]{#struct_0_x5828_x5730_753186474}[命令用来显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2134870451}

[**[display ipsec tunnel ]{lang="EN-US"}**[{ **brief** \| **count** \| **tunnel-id** *tunnel-id* }]{lang="EN-US"}]{#struct_0_x5828_x5730_1555892119}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1789541075}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1981803366}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1606614571}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x887067056}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x617700910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1108333246}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_1828040558}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2134935987}

[**[brief]{lang="EN-US"}**]{#struct_0_x5828_x5730_849788994}[：显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的简要信息。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}**]{#struct_0_x5828_x5730_699750863}[：显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的个数。]{style="font-family:宋体"}

[**[tunnel-id ]{lang="EN-US"}***[tunnel-id]{lang="EN-US"}*]{#struct_0_x5828_x5730_x609315448}[：显示指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的详细信息。其中，]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1205090339}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1343675413}[通过在特定通信方之间（例如两个安全网关之间）建立"通道"，来保护通信方之间传输的用户数据，该通道通常称为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_500447473}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_727770583}[显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的简要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec tunnel brief]{lang="EN-US"}]{#struct_0_x5828_x5730_2135001523}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[Tunn-id   Src Address     Dst Address     Inbound SPI   Outbound SPI  Status]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[0         \--              \--              1000          2000          Active]{lang="EN-US"}

[                                          3000          4000]{lang="EN-US"}

[1         1.2.3.1         2.2.2.2         5000          6000          Active]{lang="EN-US"}

[                                          7000          8000]{lang="EN-US"}

[[表1-8 ]{lang="EN-US"}[display ipsec tunnel brief]{lang="EN-US"}]{#struct_0_x5828_x5730_1578013697}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x550638890}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1901942374}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1349680054}

[[Tunn-id]{lang="EN-US"}]{#struct_0_x5828_x5730_639009453}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2135067059}[隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号]{style="font-family:宋体"}

[[Src Address]{lang="EN-US"}]{#struct_0_x5828_x5730_1984473806}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1428815277}[隧道的源地址]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IPsec Profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1102203153}[生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[中，该值无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Dst Address]{lang="EN-US"}]{#struct_0_x5828_x5730_x877744236}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x364325615}[隧道的目的地址]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[IPsec Profile]{lang="EN-US"}]{#struct_0_x5828_x5730_2134608307}[生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[中，该值无意义，显示为"]{style="font-family:宋体"}[\--]{lang="EN-US"}["]{style="font-family:宋体"}

[[Inbound SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x1180258892}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1224265257}[隧道中生效的入方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[如果该隧道使用了两种安全协议，则会分为两行分别显示两个入方向的]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x418785708}

[[Outbound SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x1656278895}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1872062632}[隧道中生效的出方向]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[如果该隧道使用了两种安全协议，则会分为两行分别显示两个入方向的]{style="font-family:宋体"}[SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_2134673843}

[[Status]{lang="EN-US"}]{#struct_0_x5828_x5730_1990622587}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x281120963}[的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[多机备份环境下，取值为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x595972664}[Active]{lang="EN-US"}[表示]{style="font-family:宋体"}[主用、取值为]{style="font-family:宋体"}[Standby]{lang="EN-US"}[表示]{style="font-family:宋体"}[备用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单机运行环境下，取值仅为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x166838959}[Active]{lang="EN-US"}[，表示]{style="font-family:宋体"}[SA]{lang="EN-US"}[处于可用状态]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x2023554663}[显示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的数目。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec tunnel count]{lang="EN-US"}]{#struct_0_x5828_x5730_2134739379}

[Total IPsec Tunnel Count: 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_383006909}[显示所有]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_2134804915}

[Tunnel ID: 0]{lang="EN-US"}

[Status: active]{lang="EN-US"}

[Perfect forward secrecy:]{lang="EN-US"}

[SA\'s SPI:]{lang="EN-US"}

[    outbound:  2000        (0x000007d0)   \[AH\]]{lang="EN-US"}

[    inbound:   1000        (0x000003e8)   \[AH\]]{lang="EN-US"}

[    outbound:  4000        (0x00000fa0)   \[ESP\]]{lang="EN-US"}

[    inbound:   3000        (0x00000bb8)   \[ESP\]]{lang="EN-US"}

[Tunnel:]{lang="EN-US"}

[    local  address:]{lang="EN-US"}

[    remote address:]{lang="EN-US"}

[Flow:]{lang="EN-US"}

[ ]{lang="EN-US"}

[Tunnel ID: 1]{lang="EN-US"}

[Status: Active]{lang="EN-US"}

[Perfect forward secrecy:]{lang="EN-US"}

[SA\'s SPI:]{lang="EN-US"}

[    outbound:  6000        (0x00001770)   \[AH\]]{lang="EN-US"}

[    inbound:   5000        (0x00001388)   \[AH\]]{lang="EN-US"}

[    outbound:  8000        (0x00001f40)   \[ESP\]]{lang="EN-US"}

[    inbound:   7000        (0x00001b58)   \[ESP\]]{lang="EN-US"}

[Tunnel:]{lang="EN-US"}

[    local  address: 1.2.3.1]{lang="EN-US"}

[    remote address: 2.2.2.2]{lang="EN-US"}

[Flow:]{lang="EN-US"}

[    as defined in ACL 3100]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x714001113}[显示]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ipsec tunnel tunnel-id 1]{lang="EN-US"}]{#struct_0_x5828_x5730_266034462}

[Tunnel ID: 1]{lang="EN-US"}

[Status: Active]{lang="EN-US"}

[Perfect forward secrecy:]{lang="EN-US"}

[SA\'s SPI:]{lang="EN-US"}

[    outbound:  6000        (0x00001770)   \[AH\]]{lang="EN-US"}

[    inbound:   5000        (0x00001388)   \[AH\]]{lang="EN-US"}

[    outbound:  8000        (0x00001f40)   \[ESP\]]{lang="EN-US"}

[    inbound:   7000        (0x00001b58)   \[ESP\]]{lang="EN-US"}

[Tunnel:]{lang="EN-US"}

[    local  address: 1.2.3.1]{lang="EN-US"}

[    remote address: 2.2.2.2]{lang="EN-US"}

[Flow:]{lang="EN-US"}

[    as defined in ACL 3100]{lang="EN-US"}

[]{#struct_0_x5828_x5730_2135394739}[[表1-9 ]{lang="EN-US"}[display ipsec tunnel]{lang="EN-US"}]{#_Toc138131790}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x791876603}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1954466420}

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1124591861}

[[Tunnel ID]{lang="EN-US"}]{#struct_0_x5828_x5730_x1069313736}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1904707239}[隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[，用来唯一地标识一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}

[[Status]{lang="EN-US"}]{#struct_0_x5828_x5730_x509247139}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2135460275}[隧道的状态：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[多机备份环境下，取值为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x595907128}[Active]{lang="EN-US"}[表示]{style="font-family:宋体"}[主用、取值为]{style="font-family:宋体"}[Standby]{lang="EN-US"}[表示]{style="font-family:宋体"}[备用]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[单机运行环境下，取值仅为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_232823590}[Active]{lang="EN-US"}[，表示隧道处于可用状态]{style="font-family:宋体"}

[[Perfect Forward Secrecy]{lang="EN-US"}]{#struct_0_x5828_x5730_1964312861}

[[此]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x935772893}[安全策略发起协商时使用完善的前向安全（]{style="font-family:宋体"}[PFS]{lang="EN-US"}[）特性，取值包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[768-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_1714473973}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group1]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1024-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_1851500238}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group2]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[1536-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_1856185453}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group5]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2048-bit Diffie-Hellman]{lang="EN-US"}]{#struct_0_x5828_x5730_2134870448}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group14]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[2048-bit]{lang="EN-US"}]{#struct_0_x5828_x5730_1556481942}[和]{lang="EN-US" style="font-family:宋体"}[256_bit]{lang="EN-US"}[子群]{lang="EN-US" style="font-family:宋体"}[Diffie-Hellman]{lang="EN-US"}[组（]{lang="EN-US" style="font-family:宋体"}**[dh-group24]{lang="EN-US"}**[）]{lang="EN-US" style="font-family:宋体"}

[[SA\'s SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x1441353747}

[[出方向和入方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1304986431}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_1547832312}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2134935984}[隧道的端点地址信息]{style="font-family:宋体"}

[[local  address]{lang="EN-US"}]{#struct_0_x5828_x5730_849985602}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2088197234}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[remote address]{lang="EN-US"}]{#struct_0_x5828_x5730_x1689991074}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2091050897}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Flow]{lang="EN-US"}]{#struct_0_x5828_x5730_2135001520}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1578079233}[隧道保护的数据流，包括源地址、目的地址、源端口、目的端口、协议]{style="font-family:宋体"}

[[as defined in ACL 3001]{lang="FR"}]{#struct_0_x5828_x5730_1651645334}

[[手工方式建立的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2137710022}[隧道所保护的数据流的范围，例如]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道保护]{style="font-family:宋体"}[ACL 3001]{lang="EN-US"}[中定义的所有数据流]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1729055658 .myid}
[]{#_Toc404793272}[]{#struct_0_x5828_x5730_1847527549}[]{#_Toc300907104}[]{#_Toc300128056}

**IPsec \-- IPsec配置命令 \-- encapsulation-mode**

------------------------------------------------------------------------

[**[encapsulation-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_1400962088}[命令用来配置安全协议对报文的封装模式。]{style="font-family:宋体"}

[**[undo encapsulation-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_2135067056}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1985325774}

[**[encapsulation-mode]{lang="EN-US"}**[ { **transport** \| **tunnel** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1109016933}

[**[undo encapsulation-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_1928280828}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1889520608}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[使用隧道模式对]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_1197107404}[报文进行封装。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1935160023}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_597295134}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134608304}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1180193356}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x471000142}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1928724073}

[**[transport]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x1279888331}[：采用传输模式。]{style="font-family:
宋体;color:black"}

[**[tunnel]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x1340108581}[：采用隧道模式。]{style="font-family:
宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1034933866}

[[传输模式]{style="font-family:宋体;color:black"}]{#struct_0_x5828_x5730_x2120100822}[下的安全协议主要用于保护上层协议报文，仅传输层数据被用来计算安全协议头，生成的安全协议头以及加密的用户数据（仅针对]{style="font-family:
宋体"}[ESP]{lang="EN-US"}[封装）被放置在原]{style="font-family:宋体"}[IP]{lang="EN-US"}[头后面。若要求端到端的安全保障，即数据包进行安全传输的起点和终点为数据包的实际起点和终点时，才能使用传输模式。]{style="font-family:宋体"}

[[隧道]{style="font-family:宋体;color:black"}]{#struct_0_x5828_x5730_2134673840}[模式下的安全协议用于保护整个]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包，用户的整个]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包都被用来计算安全协议头，生成的安全协议头以及加密的用户数据（仅针对]{style="font-family:宋体"}[ESP]{lang="EN-US"}[封装）被封装在一个新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包中。这种模式下，封装后的]{style="font-family:宋体"}[IP]{lang="EN-US"}[数据包有内外两个]{style="font-family:宋体"}[IP]{lang="EN-US"}[头，其中的内部]{style="font-family:宋体"}[IP]{lang="EN-US"}[头为原有的]{style="font-family:宋体"}[IP]{lang="EN-US"}[头，外部]{style="font-family:宋体"}[IP]{lang="EN-US"}[头由提供安全服务的设备添加。在安全保护由设备提供的情况下，数据包进行安全传输的起点或终点不为数据包的实际起点和终点时（例如安全网关后的主机），则必须使用隧道模式。隧道模式用于保护两个安全网关之间的数据传输。]{style="font-family:宋体"}

[[在]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_1990819195}[隧道的两端，]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}[安全提议所采用的封装模式要一致。]{style="font-family:宋体;color:black"}

[[IPsec profile]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_x1440793031}[要]{style="font-family:宋体;
color:black"}[引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议所采用的]{style="font-family:宋体"}[封装模式必须为传输模式[。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1665403625}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_242331930}[指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议]{style="font-family:宋体"}[tran1]{lang="EN-US"}[采用传输模式对]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文进行封装。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_301678639}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] encapsulation-mode transport]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1130227189}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1282754684}**[transform-set]{lang="EN-US"}**
:::

::: {#15152297 .myid}
[]{#_Toc404793273}[]{#struct_0_x5828_x5730_2134739376}

**IPsec \-- IPsec配置命令 \-- esp authentication-algorithm**

------------------------------------------------------------------------

[**[esp authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_383727805}[命令用来配置]{style="font-family:
宋体"}[ESP]{lang="EN-US"}[协议采用的认证算法。]{style="font-family:宋体"}

[**[undo esp authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1387417302}[命令用来删除所有指定的]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议采用的认证算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_464579481}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_202988748}[模式下：]{style="font-family:宋体"}

[**[esp authentication-algorithm ]{lang="EN-US"}**[{ **md5** \| **sha1** } \*]{lang="EN-US"}]{#struct_0_x5828_x5730_2138616260}

[**[undo esp authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_116334504}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_197303026}[模式下：]{style="font-family:宋体"}

[**[esp authentication-algorithm sha1]{lang="EN-US"}**]{#struct_0_x5828_x5730_2134804912}

[**[undo esp authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x714459865}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1035797215}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1733118230}[协议没有采用任何认证算法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1924788662}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_749197405}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1845236345}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x442464134}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2135394736}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1954531956}

[**[md5]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x2075823471}[：采用]{style="font-family:宋体;
color:black"}[HMAC-MD5]{lang="EN-US"}[认证算法，密钥长度]{style="font-family:
宋体;color:black"}[128]{lang="EN-US" style="color:black"}[比特。]{style="font-family:宋体;color:black"}

[**[sha1]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x1936230472}[：采用]{style="font-family:
宋体;color:black"}[HMAC-SHA1]{lang="EN-US"}[认证算法，密钥长度]{style="font-family:宋体;color:black"}[160]{lang="EN-US" style="color:black"}[比特。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x870842827}

[[非]{style="font-family:宋体;color:black"}[FIPS]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_33418299}[模式下，每个]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}[安全提议中均可以配置多个]{style="font-family:宋体;color:black"}[ESP]{lang="EN-US" style="color:black"}[认证算法，其优先级为配置顺序。]{style="font-family:宋体;
color:black"}

[[对于手工方式以及]{style="font-family:宋体"}[IKEv1]{lang="EN-US"}]{#struct_0_x5828_x5730_x1522250430}[（]{style="font-family:宋体"}[第]{style="font-family:宋体"}[1]{lang="EN-US"}[版本的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协议]{style="font-family:宋体"}[）协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置顺序首位的]{style="font-family:宋体"}[ESP]{lang="EN-US" style="color:black"}[认证算法生效。为保证成功建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道，隧道两端指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置的首个]{style="font-family:宋体"}[ESP]{lang="EN-US" style="color:black"}[认证算法需要一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_429738318}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2135460272}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}[认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[160]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1964116253}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] esp authentication-algorithm sha1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1757999276}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**]{#struct_0_x5828_x5730_688864711}**[transform-set]{lang="EN-US"}**
:::

::: {#1312144715 .myid}
[]{#_Toc404793274}[]{#struct_0_x5828_x5730_1540535961}

**IPsec \-- IPsec配置命令 \-- esp encryption-algorithm**

------------------------------------------------------------------------

[**[esp encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x394861217}[命令用来配置]{style="font-family:
宋体"}[ESP]{lang="EN-US"}[协议采用的加密算法。]{style="font-family:宋体"}

[**[undo esp encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_389067277}[命令用来删除所有指定的]{style="font-family:
宋体"}[ESP]{lang="EN-US"}[协议采用的加密算法。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x465606852}

[[低加密版本中：]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1641766330}

[**[esp encryption-algorithm des-cbc]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1891072049}

[**[undo esp encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x492203012}

[[高加密版本]{style="font-family:宋体"}[-]{lang="EN-US"}]{#struct_0_x5828_x5730_2134870449}[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下：]{style="font-family:宋体"}

[**[esp encryption-algorithm ]{lang="EN-US"}**[{ **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **des-cbc** \| **null** } \*]{lang="EN-US"}]{#struct_0_x5828_x5730_1556416406}

[**[undo esp encryption-algorithm.]{lang="EN-US"}**]{#struct_0_x5828_x5730_2066704618}

[[高加密版本]{style="font-family:宋体"}[-FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x1411966569}[模式下：]{style="font-family:宋体"}

[**[esp encryption-algorithm ]{lang="EN-US"}**[{ **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** }\*]{lang="EN-US"}]{#struct_0_x5828_x5730_1281670100}

[**[undo esp encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_305035056}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134935985}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_849920066}[协议没有采用任何加密算法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_532247158}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x905603085}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1668776687}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1034846294}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1444712685}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1642177993}

[**[3des-cbc]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x473489236}[：采用]{style="font-family:
宋体;color:black"}[CBC]{lang="EN-US"}[模式的]{style="font-family:
宋体"}[3DES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[168]{lang="EN-US"}[比特[。]{style="color:black"}]{style="font-family:宋体"}

[**[aes-cbc-128]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_2135001521}[：采用]{style="font-family:宋体;color:black"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[128]{lang="EN-US"}[比特[。]{style="color:black"}]{style="font-family:宋体"}

[**[aes-cbc-192]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_1578144769}[：采用]{style="font-family:宋体;color:black"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[192]{lang="EN-US"}[比特[。]{style="color:black"}]{style="font-family:宋体"}

[**[aes-cbc-256]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_48170841}[：采用]{style="font-family:宋体;
color:black"}[CBC]{lang="EN-US"}[模式的]{style="font-family:
宋体"}[AES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[256]{lang="EN-US"}[比特[。]{style="color:black"}]{style="font-family:宋体"}

[**[des-cbc]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_1946076977}[：采用]{style="font-family:
宋体;color:black"}[CBC]{lang="EN-US"}[模式的]{style="font-family:
宋体"}[DES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[64]{lang="EN-US"}[比特[。]{style="color:black"}]{style="font-family:宋体"}

[**[null]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_1594132537}[：采用]{style="font-family:
宋体;color:black"}[NULL]{lang="EN-US" style="color:black"}[加密算法，表示不进行加密。]{style="font-family:宋体;color:black"}

[[【描述】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_996110168}

[[每个]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_2026956376}[安全提议中均可以配置多个]{style="font-family:宋体;color:black"}[ESP]{lang="EN-US" style="color:black"}[加密算法，其优先级为配置顺序。]{style="font-family:宋体;color:black"}

[[对于手工方式以及]{style="font-family:宋体"}[IKEv1]{lang="EN-US"}]{#struct_0_x5828_x5730_1523465433}[（]{style="font-family:宋体"}[第]{style="font-family:宋体"}[1]{lang="EN-US"}[版本的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协议]{style="font-family:宋体"}[）协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置顺序首位的]{style="font-family:宋体"}[ESP]{lang="EN-US" style="color:black"}[加密]{style="font-family:宋体;
color:black"}[算法生效。为保证成功建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道，隧道两端指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议中配置的首个]{style="font-family:宋体"}[ESP]{lang="EN-US" style="color:black"}[加密]{style="font-family:宋体;
color:black"}[算法需要一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1985391310}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_110947377}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议采用的]{style="font-family:宋体"}[ESP]{lang="EN-US"}[加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[128]{lang="EN-US"}[比特。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_265662152}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] esp encryption-algorithm aes-cbc-128]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_944612408}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**]{#struct_0_x5828_x5730_1369673563}**[transform-set]{lang="EN-US"}**
:::

::: {#-1468642394 .myid}
[]{#_Toc404793275}[]{#struct_0_x5828_x5730_1226879317}[]{#_Toc300044735}

**IPsec \-- IPsec配置命令 \-- ike-profile**

------------------------------------------------------------------------

[**[ike-profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_1338068042}[命令用来指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板引用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo ike-profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_2134608305}[命令用来取消在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/]{lang="EN-US"}[安全策略模板中引用]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1180127820}

[**[ike-profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x352086452}

[**[undo ike-profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_133838334}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1894877653}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1139553213}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板没有引用任何]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。若系统视图下配置了]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，则使用系统视图下配置的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[进行性协商，否则使用全局的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[参数进行协商。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1296194269}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1927402756}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134673841}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1990753659}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1445397888}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1234486285}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1371711004}[：]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1902493707}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x744902965}[安全策略、]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板引用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中定义了用于]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商的相关参数。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1566234502}[安全策略视图或一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板视图下只能引用一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1325740415}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2134739377}[指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[中引用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[为]{style="font-family:宋体"}[profile1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_383662269}

[\[Sysname\] ipsec policy policy1 10 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy1-10\] ike-profile profile1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x211356152}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_213105527}[（安全命令参考]{style="font-family:宋体"}[/IKE]{lang="EN-US"}[）]{style="font-family:宋体"}
:::

::: {#1071491130 .myid}
[]{#_Toc404793276}[]{#struct_0_x5828_x5730_659276186}

**IPsec \-- IPsec配置命令 \-- ipsec anti-replay check**

------------------------------------------------------------------------

[**[ipsec anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1163147901}[命令用来开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放检测功能。]{style="font-family:宋体"}

[**[undo ipsec anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1067727166}[用来关闭]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[抗重放检测功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2134804913}

[**[ipsec anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x714394329}

[**[undo ipsec anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_653370565}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_652390276}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1067909063}[抗重放检测功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1273405110}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1921346989}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x322581685}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1417049564}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2135394737}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1954597492}

[[对重放报文的解封装无意义，并且解封装过程涉及密码学运算，会消耗设备大量的资源，导致业务可用性下降，造成了拒绝服务攻击。通过使能]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x2031402324}[抗重放检测功能，将检测到的重放报文在解封装处理之前丢弃，可以降低设备资源的消耗。]{style="font-family:宋体"}

[[在某些特定环境下，业务数据报文的接收顺序可能与正常的顺序差别较大，虽然并非有意的重放攻击，但会被抗重放检测认为是重放报文，导致业务数据报文被丢弃，影响业务的正常运行。因此，这种情况下就可以通过关闭]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x2031039581}[抗重放检测功能来避免业务数据报文的错误丢弃，也可以通过适当地增大抗重放窗口的宽度，来适应业务正常运行的需要。]{style="font-family:宋体"}

[[只有]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1630260883}[协商的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[才能够支持抗重放检测，手工方式生成的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[不支持抗重放检测。因此该功能使能与否对手工方式生成的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[没有影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x346609562}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1234316037}[开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放检测功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x295621621}

[\[Sysname\] ipsec anti-replay check]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2135460273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec anti-replay window]{lang="EN-US"}**]{#struct_0_x5828_x5730_1964181789}
:::

::: {#2058253839 .myid}
[]{#_Toc404793277}[]{#struct_0_x5828_x5730_600557632}

**IPsec \-- IPsec配置命令 \-- ipsec anti-replay window**

------------------------------------------------------------------------

[**[ipsec anti-replay window]{lang="EN-US"}**]{#struct_0_x5828_x5730_x33362220}[命令用来配置]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[抗重放窗口的宽度。]{style="font-family:宋体"}

[**[undo ipsec anti-replay window]{lang="EN-US"}**]{#struct_0_x5828_x5730_1948437515}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1398013002}

[**[ipsec anti-replay window ]{lang="EN-US"}***[width]{lang="EN-US"}*]{#struct_0_x5828_x5730_463469276}

[**[undo ipsec anti-replay window]{lang="EN-US"}**]{#struct_0_x5828_x5730_154069525}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134870446}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1555564438}[抗重放窗口的宽度为]{style="font-family:宋体"}[64]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x530296318}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_752351419}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x645839007}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1425855676}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1418260721}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_685381635}

[*[width]{lang="EN-US"}*]{#struct_0_x5828_x5730_x168014609}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放窗口的宽度，可取的值为]{style="font-family:宋体"}[64]{lang="EN-US"}[、]{style="font-family:宋体"}[128]{lang="EN-US"}[、]{style="font-family:宋体"}[256]{lang="EN-US"}[、]{style="font-family:宋体"}[512]{lang="EN-US"}[、]{style="font-family:宋体"}[1024]{lang="EN-US"}[，单位为报文个数。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2134935982}[描述]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[修改后的抗重放窗口宽度仅对新协商成功的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_849592386}[生效。]{style="font-family:宋体"}

[[在某些特定环境下，业务数据报文的接收顺序可能与正常的顺序差别较大，虽然并非有意的重放攻击，但会被抗重放检测认为是重放报文，导致业务数据报文被丢弃，影响业务的正常运行。因此，这种情况下就可以通过关闭]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1081666158}[抗重放检测功能来避免业务数据报文的错误丢弃，也可以通过适当地增大抗重放窗口的宽度，来适应业务正常运行的需要。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x505457953}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_304893751}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[抗重放窗口的宽度为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1100477223}

[\[Sysname\] ipsec anti-replay window 128]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1551728327}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}[anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x621383742}
:::

::: {#-280776620 .myid}
[]{#_Toc404793278}[]{#struct_0_x5828_x5730_2135001518}[]{#_Toc300907111}[]{#_Toc298398594}

**IPsec \-- IPsec配置命令 \-- ipsec decrypt-check enable**

------------------------------------------------------------------------

[**[ipsec decrypt-check enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_1577554944}[命令用来开启解封装后]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[报文的]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[检查功能。]{style="font-family:宋体"}

[**[undo ipsec decrypt-check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1772484917}[命令用来关闭解封装后]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[报文的]{style="font-family:
宋体"}[ACL]{lang="EN-US"}[检查功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1143953001}

[**[ipsec decrypt-check enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_1405155}

[**[undo ipsec decrypt-check enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_x113419467}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x13499680}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[解封装后]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1912800830}[报文的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查功能处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2135067054}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1985194702}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_472467903}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2136619282}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x926795503}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x507731030}

[[在隧道模式下，接口入方向上解封装的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1021483492}[报文的内部]{style="font-family:宋体"}[IP]{lang="EN-US"}[头有可能不在当前]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的保护范围内，如网络中一些恶意伪造的攻击报文就可能有此问题，所以设备需要重新检查解封装后的报文的]{style="font-family:宋体"}[IP]{lang="EN-US"}[头是否在]{style="font-family:宋体"}[ACL]{lang="EN-US"}[保护范围内。使能该功能后可以保证]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查不通过的报文被丢弃，从而提高网络安全性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x510408934}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1428518775}[开启解封装后]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[检查功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_2134608302}

[\[Sysname\] ipsec decrypt-check enable]{lang="EN-US"}
:::

::: {#157322265 .myid}
[]{#_Toc404793279}[]{#struct_0_x5828_x5730_x1180586572}

**IPsec \-- IPsec配置命令 \-- ipsec logging packet enable**

------------------------------------------------------------------------

[**[ipsec logging packet enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_1493368039}[命令用来开启]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[报文日志记录功能。]{style="font-family:宋体"}

[**[undo ipsec logging packet enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_x568413189}[命令用来关闭]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文日志记录功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1443200796}

[**[ipsec logging packet enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_1994474511}

[**[undo ipsec logging packet enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_972696212}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1472054264}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2134673838}[报文日志记录功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1991343478}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x281019650}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_343348164}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1124493178}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1041719538}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x346858261}

[[开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_81508008}[报文日志记录功能后，设备会在丢弃]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文的情况下，例如入方向找不到对应的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，]{style="font-family:宋体"}[AH/ESP]{lang="EN-US"}[认证失败或]{style="font-family:宋体"}[ESP]{lang="EN-US"}[加密失败等时，输出相应的日志信息，该日志信息内容主要包括报文的源和目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、报文的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[值、报文的序列号信息，以及设备丢包的原因。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1744300507}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2134739374}[开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文日志记录功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_383858877}

[\[Sysname\] ipsec logging packet enable]{lang="EN-US"}
:::

::: {#1441797522 .myid}
[]{#_Toc404793280}[]{#struct_0_x5828_x5730_x353586731}[]{#_Toc299973497}

**IPsec \-- IPsec配置命令 \-- ipsec df-bit**

------------------------------------------------------------------------

[**[ipsec df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_x273860921}[命令用来为当前接口设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[**[undo ipsec df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_1243153157}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x984625375}

[**[ipsec df-bit ]{lang="EN-US"}**[{ **clear** \| **copy** \| **set** }]{lang="EN-US"}]{#struct_0_x5828_x5730_1254984756}

[**[undo ipsec df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_965169539}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134804910}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[接口下未设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x714328793}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，采用全局设置的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x566069462}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2066083872}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1755817251}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x670960688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1651244309}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1562365365}

[**[clear]{lang="EN-US"}**]{#struct_0_x5828_x5730_2135394734}[：表示清除外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后的报文可被分片]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[copy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1954663028}[：表示外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位从原始报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中拷贝。]{style="font-family:宋体"}

[**[set]{lang="EN-US"}**]{#struct_0_x5828_x5730_x94323745}[：表示设置外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后的报文不能分片。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_237816224}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[该功能仅在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1742082391}[的封装模式为隧道模式时有效（因为传输模式不会增加新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[头，因此对于传输模式无影响）。]{style="font-family:宋体"}

[[该功能用于设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_95247000}[隧道模式封装后的外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，原始报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位不会被修改。]{style="font-family:宋体"}

[[如果有多个接口应用了共享源接口安全策略，则这些接口上必须使用相同的]{style="font-family:宋体"}[DF]{lang="EN-US"}]{#struct_0_x5828_x5730_x709679862}[位设置。]{style="font-family:宋体"}

[[转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。若设置了封装后]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1304365848}[报文的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，则不允许对]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文进行分片，可以避免引入分片延时。这种情况下，要求]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文长度，否则，会导致]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文被丢弃。如果无法保证转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文长度，则建议清除]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1128436976}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2135460270}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1963985181}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ipsec df-bit set]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1616733772}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}[global-df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1340399501}
:::

::: {#-1237939979 .myid}
[]{#_Toc404793281}[]{#struct_0_x5828_x5730_x465068291}[]{#_Toc299973496}

**IPsec \-- IPsec配置命令 \-- ipsec global-df-bit**

------------------------------------------------------------------------

[**[ipsec global-df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_x327976065}[命令用来为]{style="font-family:宋体"}[所有接口设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ipsec global-df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_x757589887}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_317137582}

[**[ipsec ]{lang="EN-US"}[global-df-bit]{lang="EN-US"}**[ { **clear** \| **copy** \| **set** }]{lang="EN-US"}]{#struct_0_x5828_x5730_2134870447}

[**[undo ipsec ]{lang="EN-US"}[global-df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_1555498902}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1779943780}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1458219138}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位从原始报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中拷贝。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1273255309}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1981190938}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x770738350}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_862936524}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2134935983}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_849526850}

[**[clear]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1877160544}[：表示清除外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后的报文可被分片]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[copy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2122194696}[：表示外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位从原始报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头中拷贝。]{style="font-family:宋体"}

[**[set]{lang="EN-US"}**]{#struct_0_x5828_x5730_1245912045}[：表示设置外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后的报文不能分片。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1097770627}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[该功能仅在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1233384030}[的封装模式为隧道模式时有效（因为传输模式不会增加新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[头，因此对于传输模式无影响）。]{style="font-family:宋体"}

[[该功能用于设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1869343936}[隧道模式封装后的外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，原始报文]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位不会被修改。]{style="font-family:宋体"}

[[转发报文时对报文进行分片、重组，可能会导致报文的转发延时较大。若设置了封装后]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_68923843}[报文的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位，则不允许对]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文进行分片，可以避免引入分片延时。这种情况下，要求]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文长度，否则，会导致]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文被丢弃。如果无法保证转发路径上各个接口的]{style="font-family:宋体"}[MTU]{lang="EN-US"}[大于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文长度，则建议清除]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2135001519}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1577620480}[为所有接口设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头的]{style="font-family:宋体"}[DF]{lang="EN-US"}[位。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_243283148}

[\[Sysname\] ipsec global-df-bit set]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1254593279}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec df-bit]{lang="EN-US"}**]{#struct_0_x5828_x5730_588891800}
:::

::: {#-1863640726 .myid}
[]{#_Toc404793282}[]{#struct_0_x5828_x5730_x740245361}[]{#_Toc299973500}

**IPsec \-- IPsec配置命令 \-- ipsec apply**

------------------------------------------------------------------------

[**[ipsec]{lang="EN-US"}**[ **apply**]{lang="EN-US"}]{#struct_0_x5828_x5730_602911444}[命令用来在接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[undo ipsec apply]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1733606510}[命令用来从接口上取消应用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2135067055}

[**[ipsec]{lang="EN-US"}**[ **apply** { **ipv6-policy** \| **policy** } *policy-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1985260238}

[**[undo]{lang="EN-US"}**[ **ipsec** **apply** { **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x302417999}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x230076614}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[接口上没有应用任何]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1982465928}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_408962713}

[[接口视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1444790537}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x2070527112}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2134608303}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1180521036}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1968024862}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x140892610}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_641607835}[：指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_61967477}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1331608735}

[[一个接口下只能应用一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1456752210}[安全策略。]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_190201769}[方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略可以应用到多个接口上，但建议只应用到一个接口上；手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略只能应用到一个接口上。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2134673839}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1991277942}[在接口]{style="font-family:宋体"}[GigabitEthernet1/0/2]{lang="EN-US"}[上应用名为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1051996786}

[\[Sysname\] interface gigabitethernet 1/0/2]{lang="EN-US"}

[\[Sysname-GigabitEthernet1/0/2\] ipsec apply policy policy1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_208455063}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1377932527}[ ]{lang="EN-US"}**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** }]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_799717163}
:::

::: {#-837850805 .myid}
[]{#_Toc404793283}[]{#struct_0_x5828_x5730_1306511984}[]{#_Toc300044736}

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy }**

------------------------------------------------------------------------

[**[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x858023958}[命令用来创建一条]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_2134739375}[命令用来删除指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_383793341}

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** } *policy-name* *seq-number* \[ **isakmp** \| **manual** \]]{lang="EN-US"}]{#struct_0_x5828_x5730_229212174}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* \[ *seq-number* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x1628580052}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1931584043}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[不存在任何]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x762494456}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x190647372}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x810575101}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2134804911}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x714263257}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_657421350}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1483770842}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_1247901461}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1996310708}[：指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1597418874}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1587721718}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[isakmp]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1947079766}[：指定通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商建立]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_x5828_x5730_2135394735}[：指定用手工方式建立]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1954728564}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_x5828_x5730_411547666}[IPsec]{lang="EN-US"}[安全策略时，必须指定协商方式（]{style="font-family:宋体"}**[isakmp]{lang="EN-US"}**[或]{style="font-family:宋体"}**[manual]{lang="EN-US"}**[）。进入已创建的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略时，可以不指定协商方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能修改已创建的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x126494242}[IPsec]{lang="EN-US"}[安全策略的协商方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2093952752}[IPsec]{lang="EN-US"}[安全策略是若干具有相同名字、不同顺序号的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项的集合。在同一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中，顺序号越小的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项优先级越高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1234854312}**[undo]{lang="EN-US"}**[命令，携带]{style="font-family:宋体"}*[seq-number]{lang="EN-US"}*[参数时表示删除一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项，不携带该参数时表示删除指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的所有表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_488915366}[安全策略和]{lang="EN-US" style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略名称可以相同。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1575087473}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2135460271}[创建一个名字为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[、顺序号为]{style="font-family:宋体"}[100]{lang="EN-US"}[、采用]{style="font-family:宋体"}[IKE]{lang="EN-US"}[方式协商]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1964050717}

[\[Sysname\] ipsec policy policy1 100 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy1-100\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2145080267}[创建一个名字为]{style="font-family:宋体"}[policy1]{lang="EN-US"}[、顺序号为]{style="font-family:宋体"}[101]{lang="EN-US"}[、采用手工方式建立]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_364918619}

[\[Sysname\] ipsec policy policy1 101 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-101\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x905412711}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1292695509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec apply]{lang="EN-US"}**]{#struct_0_x5828_x5730_1901633864}
:::

::: {#1707059537 .myid}
[]{#_Toc404793284}[]{#struct_0_x5828_x5730_567586567}[]{#_Toc300044737}

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy } isakmp template**

------------------------------------------------------------------------

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** } **isakmp template**]{lang="EN-US"}]{#struct_0_x5828_x5730_x594012905}[命令用来引用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板创建一条]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1302119414}[命令用来删除指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_569508247}

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** } *policy-name* *seq-number* **isakmp template** *template-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_x509452687}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* \[ *seq-number* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x397801421}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1054061072}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[没有任何]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x2012303237}[安全策略存在。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_60375070}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x593947369}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x409625822}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x655804247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x858251108}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1698725196}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_1930278435}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_352893490}[：指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1619810282}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_x593881833}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，值越小优先级越高。]{style="font-family:宋体"}

[**[isakmp template]{lang="EN-US"}***[ template-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x412634608}[：指定被引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板。]{style="font-family:宋体"}*[template-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1616730805}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不携带]{style="font-family:宋体"}]{#struct_0_x5828_x5730_360033247}*[seq-number]{lang="EN-US"}*[参数的]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令用来删除一个安全策略。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[应用了该类]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1397174733}[IPsec]{lang="EN-US"}[安全策略的接口不能发起协商，仅可以响应远端设备的协商请求。由于]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板中未定义的可选参数由发起方来决定，而响应方会接受发起方的建议，因此这种方式创建的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略适用于通信对端（例如对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址）未知的情况下，允许这些对端设备向本端设备主动发起协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x909432071}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_769132593}[引用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[策略模板]{style="font-family:宋体"}[temp1]{lang="EN-US"}[，创建名字为]{style="font-family:宋体"}[policy2]{lang="EN-US"}[、顺序号为]{style="font-family:宋体"}[200]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x601580393}

[\[Sysname\] ipsec policy policy2 200 isakmp template temp1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2125459785}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x593816297}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec]{lang="EN-US"}**[ { **ipv6-policy-template** \| **policy-template** }]{lang="EN-US"}]{#struct_0_x5828_x5730_348196839}
:::

::: {#1095579620 .myid}
[]{#struct_0_x5828_x5730_195938554}[]{#_Toc299973499}[]{#_Toc404793285}

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy \| policy } local-address**

------------------------------------------------------------------------

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** } **local-address**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1177428439}[命令用来配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略为共享源接口]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，即将指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略与一个源接口进行绑定。]{style="font-family:宋体"}

[**[undo ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** } **local-address**]{lang="EN-US"}]{#struct_0_x5828_x5730_101661743}[命令用来取消]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略为共享源接口]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_759462267}

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy** \| **policy** } *policy-name* **local-address** *interface-type interface-number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1721215799}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy** \| **policy** } *policy-name* **local-address**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1922050022}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x594275049}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1339194545}[安全策略不是共享源接口]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x116929060}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1016265927}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1809285483}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2042539425}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_205414113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_327394193}

[**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x594209513}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x923792368}[：指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略。]{style="font-family:宋体"}

[*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1029707089}[：共享该接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local-address]{lang="EN-US"}***[ interface-type interface-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1911869237}[：指定的共享源接口的名称。]{style="font-family:宋体"}*[interface-type interface-nunmber]{lang="EN-US"}*[为接口类型和接口编号。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x165989285}

[[在不同的接口上应用安全策略时，各个接口将分别协商生成]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1839599244}[。如果两个互为备份的接口上都引用了]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，并采用相同的安全策略，则在主备链路切换时，接口状态的变化会触发重新进行]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商，从而导致]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[业务流的暂时中断。通过将一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略与一个源接口绑定，使之成为共享源接口]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，可以实现多个应用该共享源接口]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的出接口共享同一个指定的源接口（称为共享源接口）协商出的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。只要该源接口的状态不变化，各接口上]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[业务就不会中断。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当非共享源接口]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x364581739}[IPsec]{lang="EN-US"}[安全策略应用于业务接口，并已经生成]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[时，如果将该安全策略配置为共享源接口安全策略，则已经生成的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[将被删除。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有]{lang="EN-US" style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x71199297}[协商方式的]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略才能配置为]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[共享源接口安全策略]{lang="EN-US" style="font-family:宋体"}[，]{style="font-family:宋体"}[手工方式的]{lang="EN-US" style="font-family:宋体"}[I]{lang="EN-US"}[P]{lang="EN-US"}[sec]{lang="EN-US"}[安全策略不能配置为共享源接口]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{lang="EN-US" style="font-family:宋体"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[一个]{style="font-family:宋体"}]{#struct_0_x5828_x5730_180677064}[IPsec]{lang="EN-US"}[安全策略只能与一个源接口绑定，新配置将覆盖旧配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个源接口可以同时与多个]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x594143977}[IPsec]{lang="EN-US"}[安全策略绑定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[推荐使用状态较为稳定的接口作为共享源接口，例如]{style="font-family:宋体"}]{#struct_0_x5828_x5730_279496653}[Loopback]{lang="EN-US"}[接口。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1129630697}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1649355511}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[map]{lang="EN-US"}[为共享源接口安全策略，共享源接口为]{style="font-family:宋体"}[Loopback11]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x2046237146}

[\[Sysname\] ipsec policy map local-address loopback 11]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1610798179}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1287476844}
:::

::: {#-1354934547 .myid}
[]{#_Toc289522167}[]{#_Toc404793286}[]{#struct_0_x5828_x5730_x645662259}[]{#_Toc300044738}

**IPsec \-- IPsec配置命令 \-- ipsec { ipv6-policy-template \| policy-template }**

------------------------------------------------------------------------

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy-template** \| **policy-template** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x594078441}[命令用来创建一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy-template** \| **policy-template** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x526942108}[命令用来删除指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1305089294}

[**[ipsec]{lang="EN-US"}**[ { **ipv6-policy-template** \| **policy-template** } *template-name* *seq-number*]{lang="EN-US"}]{#struct_0_x5828_x5730_1086161447}

[**[undo]{lang="EN-US"}**[ **ipsec** { **ipv6-policy-template** \| **policy-template** } *template-name* \[ *seq-number* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_1997532146}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1690791632}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[不存在任何]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1008737363}[IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1429857362}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x593488617}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x423526067}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1228793851}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1609694627}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1157499375}

[**[ipv6-policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2103894853}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略模板。]{style="font-family:宋体"}

[**[policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_581204493}[：指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略模板。]{style="font-family:宋体"}

[*[template-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_356173454}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1882382884}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板表项的顺序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，值越小优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x593423081}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x18036645}[安全策略模板与直接配置的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中可配置的参数类似，但是配置较为简单，除了]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议和]{style="font-family:宋体"}[IKE]{lang="EN-US"}[对等体之外的其它参数均为可选。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[携带]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2105332284}*[seq-number]{lang="EN-US"}*[参数的]{style="font-family:宋体"}**[undo]{lang="EN-US"}**[命令用来删除一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板表项。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1340639304}[IPsec]{lang="EN-US"}[安全策略模板是若干具有相同名字、不同顺序号的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板表项的集合。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPv4 IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x727098105}[安全策略模板和]{lang="EN-US" style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略模板名称可以相同。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1849711285}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_45588744}[创建一个名字为]{style="font-family:宋体"}[template1]{lang="EN-US"}[、顺序号为]{style="font-family:宋体"}[100]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x594012904}

[\[Sysname\] ipsec policy-template template1 100]{lang="EN-US"}

[\[Sysname-ipsec-policy-template-template1-100\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1302053878}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipsec ]{lang="EN-US"}**[{ **ipv6-policy**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1275701013}**[-template]{lang="EN-US"}**[ \| **policy**]{lang="EN-US"}**[-template]{lang="EN-US"}**[ }]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x2111144042}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec]{lang="EN-US"}**[ { **ipv6**-**policy** \| **policy** } **isakmp** **template**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1324098207}
:::

::: {#816746100 .myid}
[]{#_Toc404793287}[]{#struct_0_x5828_x5730_230614086}

**IPsec \-- IPsec配置命令 \-- ipsec profile**

------------------------------------------------------------------------

[**[ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1618471166}[命令用来创建一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架视图。]{style="font-family:宋体"}

[**[undo ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x734494805}[命令用来删除指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_824905766}

[**[ipsec profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*[ \[ **manual** \| **isakmp** \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x593947368}

[**[undo]{lang="EN-US"}**[ **ipsec** **profile** *profile-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_x409691358}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_2108253762}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[没有任何]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x905928058}[安全框架存在。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1420859036}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1978354764}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_816121748}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_334142940}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1634358603}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x593881832}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x412700144}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[manual]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1215769924}[：手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[**[isakmp]{lang="EN-US"}**]{#struct_0_x5828_x5730_902268070}[：指定通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商建立安全联盟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1854420271}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[创建]{style="font-family:宋体"}]{#struct_0_x5828_x5730_20969085}[IPsec]{lang="EN-US"}[安全框架时，必须指定协商方式（]{style="font-family:宋体"}**[manual]{lang="EN-US"}**[或]{style="font-family:宋体"}**[isakmp]{lang="EN-US"}**[）；进入已创建的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架时，可以不指定协商方式。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手工方式]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2129222738}[IPsec profile]{lang="EN-US"}[专门用于为应用协议配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，它相当于一个手工方式创建的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，其中的应用协议可包括但不限于]{style="font-family:宋体"}[OSPFv3]{lang="EN-US"}[、]{style="font-family:宋体"}[IPv6 BGP]{lang="EN-US"}[、]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1826484208}[协商方式]{style="font-family:宋体"}[IPsec profile]{lang="EN-US"}[用于为应用协议模块自动协商生成安全联盟，不限制对端的地址，不需要进行]{style="font-family:宋体"}[ACL]{lang="EN-US"}[匹配，且适用于]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[和]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[应用协议，其中的应用协议模块包括但是不限于]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[等。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_388840560}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x773671301}[配置名字为]{style="font-family:宋体"}[profile1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，通过手工配置建立安全联盟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x593816296}

[\[Sysname\] ipsec profile profile1 manual]{lang="EN-US"}

[\[Sysname-ipsec-profile---manual-profile1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1826418672}[配置名字为]{style="font-family:宋体"}[profile1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商建立安全联盟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1826353136}

[\[Sysname\] ipsec profile profile1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-profile-isakmp-profile1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_348262375}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="EN-US"}[ipsec ]{lang="EN-US"}**]{#struct_0_x5828_x5730_1211038362}**[profile]{lang="EN-US"}**
:::

::::: {#-220414129 .myid}
[]{#_Toc404793288}[]{#struct_0_x5828_x5730_x595907132}

**IPsec \-- IPsec配置命令 \-- ipsec redundancy enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_232168229}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_1128403152}
:::

[ ]{lang="EN-US"}

[**[ipsec redundancy enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1995861720}[命令用来使]{style="font-family:宋体"}[能]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[冗余备份功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}[ipsec redundancy enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_x121265584}[命令用来恢]{style="font-family:宋体"}[复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x999650408}

[**[ipsec redundancy enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_719136359}

[**[undo]{lang="EN-US"}**]{#struct_0_x5828_x5730_1179443454}**[ ]{lang="EN-US"}[ipsec redundancy enable ]{lang="EN-US"}**

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x452482791}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_946014554}[冗余备份功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_661108928}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x896460828}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1224202713}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x999715944}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_278561813}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x9845157}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[使能冗余备份功能后，系统会根据命令]{style="font-family:宋体"}**[redundancy replay-interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_1336192309}[指定的备份间隔对系统中的所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[进行抗重放窗口值和序列号的备份，当发生主备切换时，可以保证主备]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[流量不中断和抗重放保护不间断。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_493682226}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1177163808}[使能]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[冗余备份功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1266383086}

[\[Sysname\] ipsec redundancy enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:
黑体"}]{#struct_0_x5828_x5730_1234880}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[redundancy replay-interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_x999519336}
:::::

::: {#201294631 .myid}
[]{#_Toc404793289}[]{#struct_0_x5828_x5730_x197875197}[]{#_Toc300907116}[]{#_Toc298398598}

**IPsec \-- IPsec配置命令 \-- ipsec sa global-duration**

------------------------------------------------------------------------

[**[ipsec sa global-duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_1937212545}[命令用来配置全局的]{style="font-family:
宋体"}[IPsec SA]{lang="EN-US"}[生存时间。]{style="font-family:
宋体"}

[**[undo ipsec sa global-duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_410910359}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x110192142}

[**[ipsec sa global-duration]{lang="EN-US"}**[ { **time-based** *seconds* \| **traffic-based** *kilobytes* }]{lang="EN-US"}]{#struct_0_x5828_x5730_1701046496}

[**[undo ipsec sa global-duration]{lang="EN-US"}**[ { **time-based** \| **traffic-based** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x594275048}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1339129009}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1683450366}[基于时间的生存时间为]{style="font-family:宋体"}[3600]{lang="EN-US"}[秒，基于流量的生存时间为]{style="font-family:宋体"}[1843200]{lang="EN-US"}[千字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_639385920}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_547889853}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x2068021820}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x991034428}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1655240623}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x594209512}

[**[time-based]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x923857904}[：指定基于时间的全局生存时间，取值范围为]{style="font-family:宋体"}[180]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[traffic-based]{lang="EN-US"}***[ kilobytes]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1797026495}[：指定基于流量的全局生存时间，取值范围为]{style="font-family:宋体"}[2560]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为千字节。如果流量达到此值，则生存时间到期。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1307674004}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1281755628}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图下也可配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的生存时间，若]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图和全局都配置了]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的生存时间]{style="font-family:宋体"}[，则优先采用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图下的配置值与对端协商。]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1914921063}[为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[协商建立]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[时，采用本地配置的生存时间和对端提议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间中较小的一个。]{style="font-family:宋体"}

[[可同时存在基于时间和基于流量两种方式的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1144615067}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[生存时间，只要]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[的生存时间到达指定的时间或流量时，该]{style="font-family:
宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[就会失效。]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[失效前，]{style="font-family:宋体"}[IKE]{lang="EN-US"}[将为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[对等体协商建立新的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[，这样，在旧的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[失效前新的]{style="font-family:
宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[就已经准备好。在新的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[开始协商而没有协商好之前，继续使用旧的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[保护通信。在新的]{style="font-family:
宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[协商好之后，则立即采用新的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="EN-US"}[保护通信。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1380358110}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_458011608}[配置全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间为两个小时，即]{style="font-family:宋体"}[7200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x594143976}

[\[Sysname\] ipsec sa global-duration time-based 7200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_279431117}[配置全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间为]{style="font-family:宋体"}[10M]{lang="EN-US"}[字节，即传输]{style="font-family:宋体"}[10240]{lang="EN-US"}[千字节的流量后，当前的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[过期。]{style="font-family:宋体"}

[[\[Sysname\] ipsec sa global-duration traffic-based 10240]{lang="FR"}]{#struct_0_x5828_x5730_x1480206612}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x861756337}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_1417272588}

[[·[              ]{style="font:7.0pt "}]{lang="FR" style="font-size:10.0pt;font-family:Symbol"}**[sa duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_2090998825}
:::

::: {#-1961684402 .myid}
[]{#_Toc404793290}[]{#struct_0_x5828_x5730_1407624713}[]{#_Toc299973498}

**IPsec \-- IPsec配置命令 \-- ipsec sa idle-time**

------------------------------------------------------------------------

[**[ipsec sa idle-time]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x407898605}[命令用来开启全局的]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[空闲超时功能]{style="font-family:宋体"}[，]{style="font-family:宋体"}[并配置全局]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[空闲超时时间。]{style="font-family:宋体"}[在指定超时时间内没有流量匹配的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[SA]{lang="NO-BOK"}[即被删除。]{style="font-family:宋体"}

[**[undo ipsec sa idle-time]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x594078440}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x526876572}

[**[ipsec sa idle-time ]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_1427314852}*[seconds]{lang="NO-BOK"}*

[**[undo ipsec sa idle-time]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x324050540}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1834090384}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1554846669}[空闲超时功能处于关闭状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1057076852}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1435122496}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x861667797}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x593488616}

[[mdc-admin]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x423591603}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1264355884}

[*[seconds]{lang="NO-BOK"}*]{#struct_0_x5828_x5730_x1657708977}[：]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[的空闲超时时间]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[60]{lang="NO-BOK"}[～]{style="font-family:宋体"}[86400]{lang="NO-BOK"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x905327903}

[[此功能只适用于]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1087983314}[协商出的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1870790223}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图下也可配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的空闲超时时间，若]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图和全局都配置了]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[的空闲超时时间]{style="font-family:宋体"}[，则优先采用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图下的配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_91280518}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x593423080}[配置全局]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的空闲超时时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x18102181}

[\[Sysname\] ipsec sa idle-time 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x511264608}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1292000154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sa idle-time]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x33367494}
:::

::: {#1898481040 .myid}
[]{#_Toc404793291}[]{#struct_0_x5828_x5730_x724168595}

**IPsec \-- IPsec配置命令 \-- ipsec transform-set**

------------------------------------------------------------------------

[**[ipsec transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1785092701}[命令用来创建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议视图。]{style="font-family:宋体"}

[**[undo ipsec  transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1818804858}[命令用来删除指定的]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x594012907}

[**[ipsec transform-set ]{lang="EN-US"}***[transform-set-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1301988342}

[**[undo ipsec transform-set ]{lang="EN-US"}***[transform-set-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_34314382}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1587587576}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[没有任何]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x429730660}[安全提议存在]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_683475321}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x444568791}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x2073512432}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_765745238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x593947371}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x409101535}

[*[t]{lang="EN-US" style="color:black"}*]{#struct_0_x5828_x5730_979723641}*[ransform-set-name]{lang="SV" style="color:black"}*[：]{style="font-family:宋体;
color:black"}[IPsec]{lang="EN-US"}[安全提议的名字，为]{style="font-family:
宋体;color:black"}[1\~63]{lang="SV" style="color:black"}[个字符的字符串，不区分大小写。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_355622829}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1241694509}[安全提议是]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的一个组成部分，它用于保存]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[需要使用的安全协议、加密]{style="font-family:宋体"}[/]{lang="EN-US"}[认证算法以及封装模式，为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[协商]{style="font-family:宋体"}[SA]{lang="EN-US"}[提供各种安全参数。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1621528280}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1540236762}[创建名为]{style="font-family:宋体"}[tran1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议，并进入]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_587065676}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-transform-set-tran1[]{#_Toc311707220}[\]]{#_Toc289851369}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x593881835}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ]{lang="NO-BOK"}[ipsec transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_x412765680}
:::

::: {#1115757653 .myid}
[]{#_Toc404793292}[]{#struct_0_x5828_x5730_x40488807}

**IPsec \-- IPsec配置命令 \-- local-address**

------------------------------------------------------------------------

[**[local-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_40408763}[命令用来配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo local-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_1249998796}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1451366512}

[**[local-address]{lang="EN-US"}**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1600263832}

[**[undo local-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2127323903}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x506399435}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x593816299}[隧道的本端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的接口的主]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的接口的第一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_348852199}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1124197353}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1298153685}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1532780233}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_607392950}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_591724214}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x875427031}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的本端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x5828_x5730_x594275051}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的本端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1338670256}

[[采用]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1429068803}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略上，发起方的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址必须与响应方的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址一致。]{style="font-family:宋体"}

[[在]{style="font-family:宋体"}[VRRP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1516751144}[组网环境中，必须指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道本端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的接口所在备份组的虚拟]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1332815688}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x2043643687}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_504628523}

[\[Sysname\] ipsec policy map 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-map-1\] local-address 1.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_458413376}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[remote-address]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_2040196464}
:::

::: {#-175731077 .myid}
[]{#_Toc404793293}[]{#struct_0_x5828_x5730_x594209515}[]{#_Toc300907123}[]{#_Toc300128060}

**IPsec \-- IPsec配置命令 \-- pfs**

------------------------------------------------------------------------

[**[pfs]{lang="EN-US"}**]{#struct_0_x5828_x5730_x923923440}[命令用来配置在使用此安全提议发起]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时使用]{style="font-family:宋体"}[PFS]{lang="EN-US"}[（]{style="font-family:宋体"}[Perfect Forward Secrecy]{lang="EN-US"}[，完善的前向安全）特性。]{style="font-family:宋体"}

[**[undo pfs]{lang="EN-US"}**]{#struct_0_x5828_x5730_875388810}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1360599943}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x896904544}[模式下：]{style="font-family:宋体"}

[**[pfs ]{lang="EN-US"}**[{ **dh-group1** \| **dh-group2** \| **dh-group5** \| **dh-group14** \| **dh-group24** }]{lang="EN-US"}]{#struct_0_x5828_x5730_1450768626}

[**[undo pfs]{lang="EN-US"}**]{#struct_0_x5828_x5730_x877672054}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x1142625286}[模式下：]{style="font-family:宋体"}

[**[pfs dh-group14]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1361072802}

[**[undo pfs]{lang="EN-US"}**]{#struct_0_x5828_x5730_x594143979}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_278841293}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1177125435}[安全策略发起]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时不使用]{style="font-family:宋体"}[PFS]{lang="EN-US"}[特性。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_125276856}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x2053322354}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_702034030}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1116740089}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1344013500}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x558969029}

[**[dh-group1]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x594078443}[：]{style="font-family:
宋体;color:black"}[采用]{style="font-family:宋体"}[768-bit Diffie-Hellman]{lang="EN-US"}[组。]{style="font-family:宋体"}

[**[dh-group2]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x527073180}[：]{style="font-family:
宋体;color:black"}[采用]{style="font-family:宋体"}[1024-bit Diffie-Hellman]{lang="EN-US"}[组[。]{style="color:black"}]{style="font-family:宋体"}

[**[dh-group5]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_1823956540}[：]{style="font-family:
宋体;color:black"}[采用]{style="font-family:宋体"}[1536-bit Diffie-Hellman]{lang="EN-US"}[组。]{style="font-family:宋体"}

[**[dh-group14]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x2019604089}[：]{style="font-family:
宋体;color:black"}[采用]{style="font-family:宋体"}[2048-bit Diffie-Hellman]{lang="EN-US"}[组[。]{style="color:black"}]{style="font-family:宋体"}

[**[dh-group24]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x2052403403}[：]{style="font-family:
宋体;color:black"}[采用]{style="font-family:宋体"}[2048-bit]{lang="EN-US"}[和]{style="font-family:宋体"}[256_bit]{lang="EN-US"}[子群]{style="font-family:宋体"}[Diffie-Hellman]{lang="EN-US"}[组[。]{style="color:black"}]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_139566573}

[[2048-bit]{lang="EN-US"}]{#struct_0_x5828_x5730_x1608927687}[和]{style="font-family:宋体"}[256-bit]{lang="EN-US"}[子群]{style="font-family:宋体"}[Diffie-Hellman]{lang="EN-US"}[组（]{style="font-family:宋体"}**[dh-group24]{lang="EN-US"}**[）、]{style="font-family:宋体"}[2048-bit Diffie-Hellman]{lang="EN-US"}[组（]{style="font-family:宋体"}**[dh-group14]{lang="EN-US"}**[）、]{style="font-family:宋体"}[1536-bit Diffie-Hellman]{lang="EN-US"}[组（]{style="font-family:宋体"}**[dh-group5]{lang="EN-US"}**[）、]{style="font-family:宋体"}[1024-bit Diffie-Hellman]{lang="EN-US"}[组（]{style="font-family:宋体"}**[dh-group2]{lang="EN-US"}**[）、]{style="font-family:宋体"}[768-bit Diffie-Hellman]{lang="EN-US"}[组（]{style="font-family:宋体"}**[dh-group1]{lang="EN-US"}**[）算法的强度，即安全性和需要计算的时间依次递减。]{style="font-family:宋体"}

[[发起方的]{style="font-family:宋体"}[PFS]{lang="EN-US"}]{#struct_0_x5828_x5730_x1794081444}[强度必须大于或等于响应方的]{style="font-family:宋体"}[PFS]{lang="EN-US"}[强度，否则]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商会失败。]{style="font-family:宋体"}

[[不配置]{style="font-family:宋体"}[PFS]{lang="EN-US"}]{#struct_0_x5828_x5730_x593488619}[特性的一端，按照对端的]{style="font-family:宋体"}[PFS]{lang="EN-US"}[特性要求进行]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x423657139}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x827880196}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议使用]{style="font-family:宋体"}[PFS]{lang="EN-US"}[特性，并采用]{style="font-family:宋体"}[2048-bit Diffie-Hellman]{lang="EN-US"}[组。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1066204701}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] pfs dh-group14]{lang="EN-US"}
:::

::: {#-1826839497 .myid}
[]{#_Toc404793294}[]{#struct_0_x5828_x5730_991004684}

**IPsec \-- IPsec配置命令 \-- protocol**

------------------------------------------------------------------------

[**[protocol]{lang="EN-US"}**]{#struct_0_x5828_x5730_672140263}[命令用来配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议采用的安全协议。]{style="font-family:宋体"}

[**[undo protocol]{lang="EN-US"}**]{#struct_0_x5828_x5730_95551145}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1491289041}

[**[protocol ]{lang="EN-US"}**[{ **ah** \| **ah-esp** \| **esp** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x593423083}

[**[undo protocol]{lang="EN-US"}**]{#struct_0_x5828_x5730_x17905573}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1251057811}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[使用]{style="font-family:宋体"}[ESP]{lang="EN-US"}]{#struct_0_x5828_x5730_2092219277}[安全协议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_875639410}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_384265358}[安全提议视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1505114381}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x962695516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1514236044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x594012906}

[**[ah]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x1301922806}[：采用]{style="font-family:宋体;
color:black"}[AH]{lang="EN-US" style="color:black"}[协议对报文进行保护。]{style="font-family:宋体;color:black"}

[**[ah-esp]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_97889925}[：先用]{style="font-family:宋体;
color:black"}[ESP]{lang="EN-US" style="color:black"}[协议对报文进行保护，再用]{style="font-family:宋体;color:black"}[AH]{lang="EN-US" style="color:black"}[协议对报文进行保护。]{style="font-family:宋体;color:black"}

[**[esp]{lang="EN-US" style="color:black"}**]{#struct_0_x5828_x5730_x894926992}[：采用]{style="font-family:宋体;
color:black"}[ESP]{lang="EN-US" style="color:black"}[协议对报文进行保护。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2016677833}

[[在]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}]{#struct_0_x5828_x5730_x1548653184}[隧道的两端，]{style="font-family:宋体;color:black"}[IPsec]{lang="EN-US" style="color:black"}[安全[提议所采用的安全协议必须一致。]{style="color:black"}]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_99217802}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x54516470}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议采用]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x593947370}

[\[Sysname\] ipsec transform-set tran1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-tran1\] protocol ah]{lang="EN-US"}
:::

::: {#-1969927489 .myid}
[]{#_Toc300044744}[]{#_Toc404793295}[]{#struct_0_x5828_x5730_x409167071}[]{#_Toc300907124}

**IPsec \-- IPsec配置命令 \-- qos pre-classify**

------------------------------------------------------------------------

[**[qos pre-classify]{lang="PT-BR"}**]{#struct_0_x5828_x5730_955469483}[命令用来开启]{style="font-family:宋体"}[QoS]{lang="PT-BR"}[预分类功能。]{style="font-family:宋体"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x5828_x5730_651587593}[ **qos pre-classify**]{lang="PT-BR"}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1614169717}

[**[qos pre-classify]{lang="PT-BR"}**]{#struct_0_x5828_x5730_1227240769}

[**[undo]{lang="PT-BR"}**]{#struct_0_x5828_x5730_1417950244}[ **qos pre-classify**]{lang="PT-BR"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1684407298}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[QoS]{lang="PT-BR"}]{#struct_0_x5828_x5730_x593881834}[预分类功能处于关闭状态，即]{style="font-family:宋体"}[QoS]{lang="EN-US"}[使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[封装后报文的外层]{style="font-family:宋体"}[IP]{lang="EN-US"}[头信息来对报文进行分类。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x412831216}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1612489083}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="PT-BR"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_270543978}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="PT-BR"}]{#struct_0_x5828_x5730_2019963223}

[[mdc-admin]{lang="PT-BR"}]{#struct_0_x5828_x5730_x578315896}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1937268741}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[QoS]{lang="PT-BR"}]{#struct_0_x5828_x5730_x784483783}[预分类功能是指]{style="font-family:宋体"}[，]{style="font-family:宋体"}[QoS]{lang="PT-BR"}[基于被封装报文的原始]{style="font-family:宋体"}[IP]{lang="PT-BR"}[头信息对报文进行分类。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1915932758}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x593816298}[在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中开启]{style="font-family:宋体"}[QoS]{lang="PT-BR"}[预分类功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_348917735}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] qos pre-classify]{lang="EN-US"}
:::

::::: {#1920875470 .myid}
[]{#_Toc404793296}[]{#struct_0_x5828_x5730_x999257191}[]{#_Toc375900907}

**IPsec \-- IPsec配置命令 \-- redundancy replay-interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_1874500117}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x1013697435}
:::

[ ]{lang="EN-US"}

[**[redundancy]{lang="EN-US"}[ replay-interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_x999322727}[命令用来配置]{style="font-family:宋体"}[抗]{style="font-family:宋体"}[重放窗口和序号的同步间隔。]{style="font-family:宋体"}

[**[undo ]{lang="EN-US"}**]{#struct_0_x5828_x5730_1904295056}[[redundancy]{lang="EN-US" style="font-size:10.0pt"}]{.SC132527}**[ replay-interval]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1055025974}

[[[redundancy]{lang="EN-US" style="font-size:10.0pt"}]{.SC132527}**[ replay-interval inbound ]{lang="EN-US"}***[inbound-interval]{lang="EN-US"}***[ outbound ]{lang="EN-US"}***[outbound-interval]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1836925078}

[**[undo ]{lang="EN-US"}**]{#struct_0_x5828_x5730_2134075567}[[redundancy]{lang="EN-US" style="font-size:10.0pt"}]{.SC132527}**[ replay-interval]{lang="EN-US"}**

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1160330855}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[同步入方向]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1745761317}[抗]{style="font-family:宋体"}[重放窗口的报文间隔为]{style="font-family:宋体"}[1000]{lang="EN-US"}[，同步出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[抗]{style="font-family:宋体"}[重放序号的报文间隔为]{style="font-family:宋体"}[100000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_893197059}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x999126119}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_317918937}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1120277242}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_135380875}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x710096668}

[**[inbound ]{lang="EN-US"}***[inbound-interval]{lang="EN-US"}*]{#struct_0_x5828_x5730_146717420}[：同步入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[抗]{style="font-family:宋体"}[重放窗口左侧值的报文间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[1000]{lang="EN-US"}[，单位为报文个数，取值为]{style="font-family:宋体"}[0]{lang="EN-US"}[，表示不同步防重放窗口。]{style="font-family:宋体"}

[**[outbound ]{lang="EN-US"}***[outbound-interval]{lang="EN-US"}*]{#struct_0_x5828_x5730_1856054809}[：同步出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[抗]{style="font-family:宋体"}[重放序号的报文间隔，取值范围为]{style="font-family:宋体"}[1000]{lang="EN-US"}[～]{style="font-family:宋体"}[100000]{lang="EN-US"}[，单位为报文个数。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1930973861}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x999191655}[冗余备份功能]{style="font-family:宋体"}[处于开启状态时，]{style="font-family:宋体"}[抗]{style="font-family:宋体"}[重放序号同步间隔的配置]{style="font-family:宋体"}[才会生效。]{style="font-family:宋体"}

[[调小同步的报文间隔，可以增加主备间保持抗重放窗口和序号一致的精度，但同时对转发性能会有一定影响。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1602834172}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x779346035}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_644070876}[配置同步入方向]{style="font-family:宋体"}[抗]{style="font-family:宋体"}[重放窗口的报文间隔为]{style="font-family:宋体"}[800]{lang="EN-US"}[，同步出方向]{style="font-family:宋体"}[抗]{style="font-family:宋体"}[重放序号的报文间隔为]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_149146144}

[\[Sysname\] ipsec policy test 1]{lang="EN-US"}

[\[sysname-ipsec-policy-test-1\]]{lang="EN-US"}**[ ]{lang="EN-US" style="font-size:10.0pt;font-family:\"Arial\",\"sans-serif\";color:black"}**[redundancy]{lang="EN-US"}[ relay-interval inbound 800 outbound 50000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_318890890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec anti-replay check]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1880897295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec anti-replay window]{lang="EN-US"}**]{#struct_0_x5828_x5730_480337899}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec redundancy enable]{lang="EN-US"}**]{#struct_0_x5828_x5730_x999650406}
:::::

::: {#-653025436 .myid}
[]{#_Toc404793297}[]{#struct_0_x5828_x5730_1552469159}

**IPsec \-- IPsec配置命令 \-- remote-address**

------------------------------------------------------------------------

[**[remote-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x55094074}[命令用来指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo remote-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_895742697}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2071626383}

[**[remote-address ]{lang="PT-BR"}**]{#struct_0_x5828_x5730_x2071600030}[{ \[ **ipv6** \] *host-name* \| *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="PT-BR"}

[**[undo]{lang="PT-BR"}**]{#struct_0_x5828_x5730_x594275050}[ **remote-address** { \[ **ipv6** \] *host-name* \| *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="PT-BR"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1338604720}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[未指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1217218971}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1212633291}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1671538457}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x850817146}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1111868108}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x654530315}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2034830744}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_x594209514}[：指定]{style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[隧道的对端地址或主机名称]{style="font-family:宋体"}[。如果不指定该参数，则表示指定]{style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[隧道的对端地址或主机名称]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[*[hostname]{lang="EN-US"}*]{#struct_0_x5828_x5730_x923988976}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}[的对端主机名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。该主机名可被]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器解析为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_1310303888}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}[的对端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x720590993}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道]{style="font-family:宋体"}[的对端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x645725889}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1340034137}[协商发起方必须配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，对于使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的响应方可选配。]{style="font-family:宋体"}

[[手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1895486783}[安全策略不支持域名解析，因此只能指定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址类型的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[对于主机名方式的对端地址，地址更新的查询过程有所不同。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1211322850}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若此处指定对端主机名由]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x594143978}[DNS]{lang="EN-US"}[服务器来解析，则本端按照]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器通知的域名解析有效期，在该有效期超时之后向]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器查询主机名对应的最新的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若此处指定对端主机名由本地配置的静态域名解析（通过]{lang="EN-US" style="font-family:宋体"}**[ip host]{lang="EN-US"}**]{#struct_0_x5828_x5730_278775757}[命令配置）来解析，则更改此主机名对应的]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址之后，需要在]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板中重新配置]{lang="EN-US" style="font-family:宋体"}**[remote-address]{lang="PT-BR"}**[，]{lang="EN-US" style="font-family:宋体"}[才能使得本端解析到更新后的对端]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[例如，本端已经存在一条静态域名解析配置，它指定了主机名]{style="font-family:宋体"}[test]{lang="EN-US"}]{#struct_0_x5828_x5730_x562444119}[对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。若先后执行以下配置：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1242434640}[在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[中指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端主机名为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] ipsec policy policy1 1 isakmp]{lang="EN-US"}]{#struct_0_x5828_x5730_1267723090}

[\[Sysname-ipsec-policy-isakmp-policy1-1\] remote-address test]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x346771147}[更改主机名]{style="font-family:宋体"}[test]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] ip host test 2.2.2.2]{lang="EN-US"}]{#struct_0_x5828_x5730_111576584}

[[则，需要在]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x71802215}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[中重新指定对端主机名，使得本端可以根据更新后的本地域名解析配置得到最新的对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[，否则仍会解析为原来的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[1.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x594078442}[重新指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端主机名为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname\] ipsec policy policy1 1 isakmp]{lang="EN-US"}]{#struct_0_x5828_x5730_x527007644}

[\[Sysname -ipsec-policy-isakmp-policy1-1\] remote-address test]{lang="EN-US"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_683117524}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1370796082}[指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1269239744}

[\[Sysname\] ipsec policy policy1 10 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-10\] remote-addresss 10.1.1.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x535153823}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ip host]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1792584020}[（三层技术]{style="font-family:
宋体"}[-IP]{lang="EN-US"}[业务]{style="font-family:宋体"}[/]{lang="EN-US"}[域名解析）]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-address]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x1725590826}
:::

::: {#2073630965 .myid}
[]{#_Toc404793298}[]{#struct_0_x5828_x5730_x593488618}[]{#_Toc292201256}

**IPsec \-- IPsec配置命令 \-- reset ipsec sa**

------------------------------------------------------------------------

[**[reset ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x423722675}[命令用来清除已经建立的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1479010992}

[**[reset]{lang="EN-US"}**[ **ipsec** **sa** \[ { **ipv6-policy** \| **policy** } *policy-name* \[ *seq-number* \] \| **profile** *policy-name* \| **remote** { *ipv4-address* \| **ipv6** *ipv6-address* } \| **spi** { *ipv4-address* \| **ipv6** *ipv6-address* } { **ah** \| **esp** } *spi-num* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_1000289534}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x198361700}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1332170455}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1830190342}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1343220480}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x593423082}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x17971109}

[[{ **ipv6-policy** \| **policy** } *policy-name* \[ *seq-number* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x847016432}[：表示根据]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略名称清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6-policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_1021072585}[：]{lang="EN-US" style="font-family:宋体"}[IPv6 IPsec]{lang="EN-US"}[安全策略。]{lang="EN-US" style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1999495922}[：]{lang="EN-US" style="font-family:宋体"}[IPv4 IPsec]{lang="EN-US"}[安全策略。]{lang="EN-US" style="font-family:宋体"}[该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1713610983}[：]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的名字，为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[seq-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1592722666}[：]{lang="EN-US" style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略表项的顺序号，取值范围为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[65535]{lang="EN-US"}[。如果不指定该参数，则表示指定名字为]{lang="EN-US" style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[的安全策略中所有安全策略表项。]{lang="EN-US" style="font-family:宋体"}

[**[profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1544843023}[：表示根据]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架名称清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_504876596}[：表示根据对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x594012909}[：对端的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1301332982}*[ ipv6-address]{lang="EN-US"}*[：对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[spi ]{lang="EN-US"}**[{ *ipv4-address* \| **ipv6** *ipv6-address* } { **ah** \| **esp** } *spi-num*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1184969397}[：表示根据]{style="font-family:宋体"}[SA]{lang="EN-US"}[的三元组信息（对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、安全协议、安全参数索引）清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x885856414}[：对端的]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_1454255779}*[ ipv6-address]{lang="EN-US"}*[：对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ah]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1883382195}[：]{lang="EN-US" style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[esp]{lang="EN-US"}**]{#struct_0_x5828_x5730_1920964092}[：]{style="font-family:
宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}*[spi-num]{lang="EN-US"}*]{#struct_0_x5828_x5730_1423073366}[：安全参数索引，取值范围为]{style="font-family:
宋体"}[256]{lang="EN-US"}[～]{style="font-family:
宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1111658935}

[[如果不指定任何参数，则清除所有的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x593947373}[。]{style="font-family:宋体"}

[[如果指定了一个]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x409232607}[的三元组信息，则将清除符合该三元组的某一个方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[以及对应的另外一个方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。若是同时采用了两种安全协议，则还会清除另外一个协议的出方向和入方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[对于出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x197326966}[，三元组是它的唯一标识；对于入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，]{style="font-family:宋体"}[SPI]{lang="EN-US"}[是它的唯一标识。因此，]{style="font-family:宋体"}[若是希望通过指定出方向的三元组信息来清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，则需要准确指定三元组信息（其中，]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架生成的]{style="font-family:宋体"}[SA]{lang="EN-US"}[由于没有地址信息，所以地址信息可以任意]{style="font-family:宋体"}[）；若是希望通过指定入方向]{style="font-family:宋体"}[的三元组信息来清除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，则只需要准确指定]{style="font-family:宋体"}[SPI]{lang="EN-US"}[值即可，另外两个信息可以任意。]{style="font-family:宋体"}

[[通过手工建立的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_753012480}[被清除后，系统会立即根据对应的手工]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略建立新的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_422127881}[协商建立的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[被清除后，系统会在有报文需要进行]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护时触发协商新的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1364933640}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_431249728}[清除所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec sa]{lang="EN-US"}]{#struct_0_x5828_x5730_x532585159}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x593881837}[清除]{style="font-family:宋体"}[SPI]{lang="EN-US"}[为]{style="font-family:宋体"}[123]{lang="EN-US"}[、对端地址为]{style="font-family:宋体"}[10.1.1.2]{lang="EN-US"}[、安全协议为]{style="font-family:宋体"}[AH]{lang="EN-US"}[的出方向和入方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec sa spi 10.1.1.2 ah 123]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x412896752}

[[\# ]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x454247342}[清除]{style="font-family:宋体"}[IPsec]{lang="NO-BOK"}[对端地址为]{style="font-family:宋体"}[10.1.1.2]{lang="NO-BOK"}[的所有]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec sa remote 10.1.1.2]{lang="NO-BOK"}]{#struct_0_x5828_x5730_486457766}

[[\# ]{lang="NO-BOK"}]{#struct_0_x5828_x5730_1935568687}[清除]{style="font-family:宋体"}[IPsec]{lang="NO-BOK"}[安全策略名字为]{style="font-family:宋体"}[policy1]{lang="NO-BOK"}[、顺序号为]{style="font-family:宋体"}[10]{lang="NO-BOK"}[的所有]{style="font-family:宋体"}[IPsec SA]{lang="NO-BOK"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec sa policy policy1 10]{lang="EN-US"}]{#struct_0_x5828_x5730_x714163880}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x489262016}[清除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[中的所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec sa policy policy1]{lang="EN-US"}]{#struct_0_x5828_x5730_x1544332527}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_356754223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}[ ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x593816301}
:::

::: {#-1796722460 .myid}
[]{#_Toc404793299}[]{#struct_0_x5828_x5730_x1990324258}

**IPsec \-- IPsec配置命令 \-- reset ipsec statistics**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **ipsec** **statistics**]{lang="EN-US"}]{#struct_0_x5828_x5730_1929343014}[命令用来清除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的报文统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1233228245}

[**[reset ipsec statistics ]{lang="EN-US"}**[\[ **tunnel-id** *tunnel-id[ ]{style="color:red"}*\]]{lang="EN-US"}]{#struct_0_x5828_x5730_1363655225}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x313484657}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x146103028}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1049009198}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x594275053}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1338801328}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x917237359}

[**[tunnel-id ]{lang="EN-US"}***[tunnel-id]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1648736623}[：清除指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的报文统计信息。其中，]{style="font-family:宋体"}*[tunnel-id]{lang="EN-US"}*[为隧道的]{style="font-family:宋体"}[ID]{lang="EN-US"}[号，取值范围与设备的型号有关，请以设备的实际情况为准。如果未指定任何参数，则清除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的所有报文统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1646105933}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_477685222}[清除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的所有报文统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ipsec statistics]{lang="EN-US"}]{#struct_0_x5828_x5730_1608058835}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1974679356}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec statistics]{lang="EN-US"}**]{#struct_0_x5828_x5730_x227171345}
:::

::: {#654907839 .myid}
[]{#_Toc300907128}[]{#_Toc404793300}[]{#struct_0_x5828_x5730_x594209517}[]{#_Toc338870379}[]{#_Toc336619147}

**IPsec \-- IPsec配置命令 \-- reverse-route dynamic**

------------------------------------------------------------------------

[**[reverse-route dynamic]{lang="EN-US"}**]{#struct_0_x5828_x5730_x924054512}[命令用来开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能。]{style="font-family:宋体"}

[**[undo reverse-route dynamic]{lang="EN-US"}**]{#struct_0_x5828_x5730_766782983}[命令用来关闭]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x625079537}

[**[reverse-route]{lang="EN-US"}**[ **dynamic**]{lang="EN-US"}]{#struct_0_x5828_x5730_1585584617}

[**[undo reverse-route]{lang="EN-US"}**[ **dynamic**]{lang="EN-US"}]{#struct_0_x5828_x5730_1986808121}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_785306004}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1731267471}[反向路]{style="font-family:宋体"}[由注入功能处于关闭状态]{style="font-size:11.0pt;font-family:
宋体"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_241612686}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x594143981}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_279365576}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1352968772}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1869100859}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x470392314}

[[在企业中心侧网关设备上的某安全策略视图[/]{lang="EN-US"}安全策略模板视图下开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1568871595}[反向路由注入功能后，设备会]{style="font-family:宋体"}[根据协商的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[自动生成一条静态路由，该路由的目的地址为受保护的对端私网，下一跳地址为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道的对端地址。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1511508678}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[开启反向路由注入功能时，会删除本策略协商出的所有]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1021684054}[IPsec SA]{lang="EN-US"}[。当有新的流量触发生成]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[时，根据新协商的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[生成路由信息。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[关闭反向路由注入功能时，会删除本策略协商出的所有]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x594078445}[IPsec SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[生成的静态路由随]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x526679964}[IPsec SA]{lang="EN-US"}[的创建而创建，随]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的删除而删除。]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[需要查看生成的路由信息时，可以通过]{lang="EN-US" style="font-family:宋体"}**[display ip routing-table]{lang="EN-US"}**]{#struct_0_x5828_x5730_x913368306}[命令查看。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x272730348}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1535638882}[开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能，根据协商成功的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[动态生成静态路由，目的地址为受保护的对端私网网段]{style="font-family:宋体"}[3.0.0.0/24]{lang="EN-US"}[，下一跳地址为对端隧道地址]{style="font-family:宋体"}[1.1.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1772546588}

[\[Sysname\] ipsec policy 1 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-1-1\] reverse-route dynamic]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-1-1\] quit]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_300609549}[隧道两端的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[协商成功后，可查看到生成如下静态路由（其它显示信息略）。]{style="font-family:宋体"}

[[\[Sysname\] display ip routing-table]{lang="EN-US"}]{#struct_0_x5828_x5730_x593488621}

[\...]{lang="EN-US"}

[Destination/Mask    Proto  Pre  Cost         NextHop         Interface]{lang="EN-US"}

[3.0.0.0/24          Static 60   0            1.1.1.2         Eth1/1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x423132850}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display ip routing-table]{lang="EN-US"}**]{#struct_0_x5828_x5730_x434378232}[（三层技术]{lang="EN-US" style="font-family:宋体"}[-IP]{lang="EN-US"}[路由命令参考]{lang="EN-US" style="font-family:宋体"}[/IP]{lang="EN-US"}[路由基础）]{lang="EN-US" style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ipsec policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_702318349}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_564951061}
:::

::: {#-557939340 .myid}
[]{#_Toc404793301}[]{#struct_0_x5828_x5730_263795509}

**IPsec \-- IPsec配置命令 \-- reverse-route preference**

------------------------------------------------------------------------

[**[reverse-route preference]{lang="EN-US"}**]{#struct_0_x5828_x5730_883474498}[命令用来设置]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能生成的静态路由的优先级。]{style="font-family:宋体"}

[**[undo reverse-route preference]{lang="EN-US"}**]{#struct_0_x5828_x5730_x14590931}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1125329703}

[**[reverse-route]{lang="EN-US"}[ preference]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x593423085}

[**[undo reverse-route preference]{lang="EN-US"}**]{#struct_0_x5828_x5730_x17774501}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_874012788}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_250549886}[反向路由注入功能生成的静态路由的优先级为]{style="font-family:宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x916865850}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x89444115}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x346967667}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x267269466}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x594012908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1301267446}

[*[number]{lang="EN-US"}*]{#struct_0_x5828_x5730_735701445}[：静态路由的优先级，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。该值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1666893534}

[[若对静态路由优先级进行修改，会删除本策略协商生成的所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_2001296396}[和根据这些]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生成的静态路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x574422938}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1927736247}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能生成的静态路由的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x493467059}

[\[Sysname\] ipsec policy 1 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-1-1\] reverse-route preference 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x593947372}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ipsec policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x409298143}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_x647064172}
:::

::: {#-1464954185 .myid}
[]{#_Toc404793302}[]{#struct_0_x5828_x5730_x307413508}[]{#_Toc338870381}

**IPsec \-- IPsec配置命令 \-- reverse-route tag**

------------------------------------------------------------------------

[**[reverse-route tag]{lang="EN-US"}**]{#struct_0_x5828_x5730_x853705529}[命令用来设置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能生成的静态路由的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，该值用于标识静态路由，以便在路由策略中根据]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值对路由进行灵活的控制。]{style="font-family:宋体"}

[**[undo reverse-route tag]{lang="EN-US"}**]{#struct_0_x5828_x5730_x591942745}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x273334961}

[**[reverse-route tag ]{lang="EN-US"}***[tag-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_x719465328}

[**[undo reverse-route tag]{lang="EN-US"}**]{#struct_0_x5828_x5730_x593881836}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x412962288}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x35853868}[反向路由注入功能生成的静态路由的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_442341194}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1201564672}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_857703936}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x508480222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x45354653}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_198260423}

[*[tag-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_x593816300}[：静态路由的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1990258722}

[[若对静态路由]{style="font-family:宋体"}[Tag]{lang="EN-US"}]{#struct_0_x5828_x5730_1162374134}[值进行修改，则会删除本策略协商生成的所有]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[和根据这些]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生成的静态路由。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x976083362}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x2122353100}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[反向路由注入功能生成的静态路由的]{style="font-family:宋体"}[Tag]{lang="EN-US"}[值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\>system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_2040915260}

[\[Sysname\] ipsec policy 1 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-1-1\] reverse-route tag 50]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1091184587}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ipsec policy]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1473609708}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec policy-template]{lang="EN-US"}**]{#struct_0_x5828_x5730_x594275052}
:::

::: {#-1919080408 .myid}
[]{#_Toc404793303}[]{#struct_0_x5828_x5730_x1338735792}

**IPsec \-- IPsec配置命令 \-- sa duration**

------------------------------------------------------------------------

[**[sa]{lang="EN-US"}**[ **duration**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1512845738}[命令用来配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的生存时间。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sa** **duration**]{lang="EN-US"}]{#struct_0_x5828_x5730_x78100259}[命令用来删除配置的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2114495800}

[]{#struct_0_x5828_x5730_x1902901805}[**[sa duration]{lang="EN-US"}**[ ]{lang="EN-US"}]{#_Hlt16152231}[{ **time-based** *seconds* \| **traffic-based** *kilobytes* }]{lang="EN-US"}

[**[undo sa duration]{lang="EN-US"}**[ { **time-based** \| **traffic-based** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1684420773}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1121497269}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1151669293}[安全策略和]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间均为当前全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x594209516}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x924120048}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1703727}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1856965879}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x807674650}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1583561709}

[**[time-based]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_1031974353}[：指定基于时间的生存时间，取值范围为]{style="font-family:宋体"}[180]{lang="EN-US"}[～]{style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[**[traffic-based]{lang="EN-US"}***[ kilobytes]{lang="EN-US"}*]{#struct_0_x5828_x5730_1258176909}[：指定基于流量的生存时间，取值范围为]{style="font-family:宋体"}[2560]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[，单位为千字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x594143980}

[[当]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_279300040}[协商]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[时，如果采用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略下未配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的生存时间，将采用全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间（通过命令]{style="font-family:宋体"}**[ipsec sa global-duration]{lang="EN-US"}**[设置）与对端协商。如果]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板下配置了]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的生存时间，则优先使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板下的配置值与对端协商。]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_193088555}[为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[协商建立]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[时，采用本地配置的生存时间和对端提议的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间中较小的一个。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1596771599}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x293674057}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间为两个小时，即]{style="font-family:宋体"}[7200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x2048460586}

[\[Sysname\] ipsec policy policy1 100 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy1-100\] sa duration time-based 7200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_695792486}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[policy1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生存时间为]{style="font-family:宋体"}[20M]{lang="EN-US"}[字节，即传输]{style="font-family:宋体"}[20480]{lang="EN-US"}[千字节的流量后，当前的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[就过期。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x594078444}

[\[Sysname\] ipsec policy policy1 100 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy1-100\] sa duration traffic-based 20480]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x526614428}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2086457557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec sa global-duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_1089555280}
:::

::: {#-740400455 .myid}
[]{#struct_0_x5828_x5730_1030405598}[]{#_Toc404793304}

**IPsec \-- IPsec配置命令 \-- sa hex-key authentication**

------------------------------------------------------------------------

[**[sa hex-key authentication]{lang="EN-US"}**]{#struct_0_x5828_x5730_1290128791}[命令用来为手工创建的]{style="font-family:
宋体"}[IPsec SA]{lang="EN-US"}[配置十六进制形式的认证密钥。]{style="font-family:
宋体"}

[**[undo sa hex-key authentication]{lang="EN-US"}**]{#struct_0_x5828_x5730_x285297745}[命令用来删除为]{style="font-family:
宋体"}[IPsec SA]{lang="EN-US"}[配置的十六进制形式的认证密钥。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1571660309}

[**[sa hex-key]{lang="EN-US"}**[ **authentication** { **inbound** \| **outbound** } { **ah** \| **esp** } { **cipher** \| **simple** } *key-value*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1743506236}

[**[undo sa hex-key]{lang="EN-US"}**[ **authentication** { **inbound** \| **outbound** } { **ah** \| **esp** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x593488620}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x423198386}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[未配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1849796005}[使用的认证密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1894152237}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_25487573}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1070853298}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2048087903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1377588113}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1565618291}

[**[inbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_x593423084}[：指定入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[使用的认证密钥。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_x17840037}[：指定出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[使用的认证密钥。]{style="font-family:宋体"}

[**[ah]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1238629756}[：指定]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[esp]{lang="EN-US"}**]{#struct_0_x5828_x5730_x646416030}[：指定]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[cipher ]{lang="EN-US"}***[key-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_69555630}[：表示以密文形式设置认证密钥。]{style="font-family:
宋体"}*[key-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[85]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[simple ]{lang="EN-US"}***[key-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_1522972313}[：表示以明文形式设置认证密钥。]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[为十六进制格式的字符串，不区分大小写。对于不同的算法，密钥长度不同：]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[个字节；]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[20]{lang="EN-US"}[个字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1460003859}

[[此命令仅用于手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x688914575}[安全策略及]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须分别配置]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1767957722}**[inbound]{lang="EN-US"}**[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[两个方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2019458333}[IPsec]{lang="EN-US"}[隧道的两端设置的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数必须是完全匹配的。本端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥必须和对端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥一致；本端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥必须和对端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于要应用于]{style="font-family:宋体"}]{#struct_0_x5828_x5730_266172675}[IPv6]{lang="EN-US"}[路由协议的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，还必须保证本端出方向]{style="font-family:宋体"}[SA]{lang="EN-US"}[的密钥和本端入方向]{style="font-family:宋体"}[SA]{lang="EN-US"}[的密钥一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果先后以不同的方式输入了密钥，则最后设定的密钥有效。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x268041518}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x133982982}[IPsec]{lang="EN-US"}[隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的认证密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1404449738}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_14827760}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1266528022}[配置采用]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥为明文]{style="font-family:宋体"}[0x112233445566778899aabbccddeeff00]{lang="EN-US"}[；出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的认证密钥为明文]{style="font-family:宋体"}[0xaabbccddeeff001100aabbccddeeff00]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1767892186}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa hex-key authentication inbound ah simple 112233445566778899aabbccddeeff00]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa hex-key authentication outbound ah simple aabbccddeeff001100aabbccddeeff00]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1607844863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_2090634491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sa string-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_572399315}
:::

::: {#640622374 .myid}
[]{#_Toc300044742}[]{#_Toc404793305}[]{#struct_0_x5828_x5730_1151041440}

**IPsec \-- IPsec配置命令 \-- sa hex-key encryption**

------------------------------------------------------------------------

[**[sa hex-key encryption]{lang="EN-US"}**]{#struct_0_x5828_x5730_1560850554}[命令用来为手工创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[配置十六进制形式的加密密钥。]{style="font-family:宋体"}

[**[undo sa hex-key encryption]{lang="EN-US"}**]{#struct_0_x5828_x5730_x311143736}[命令用来删除为]{style="font-family:
宋体"}[IPsec SA]{lang="EN-US"}[配置的十六进制形式的加密密钥。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1119194040}

[**[sa hex-key encryption]{lang="EN-US"}**[ { **inbound** \| **outbound** } **esp** { **cipher** \| **simple** } *key-value*]{lang="EN-US"}]{#struct_0_x5828_x5730_1768088794}

[**[undo sa hex-key  encryption]{lang="EN-US"}**[ { **inbound** \| **outbound** } **esp**]{lang="EN-US"}]{#struct_0_x5828_x5730_223457004}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_863701185}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[未配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_434813451}[使用的加密密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x822453243}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x87597267}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x266277867}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x344764199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x910147826}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1768023258}

[**[inbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1418415711}[：指定入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[使用的加密密钥。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_71327702}[：指定出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[使用的加密密钥。]{style="font-family:宋体"}

[**[esp]{lang="EN-US"}**]{#struct_0_x5828_x5730_717292691}[：指定]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[cipher ]{lang="EN-US"}***[key-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_x26552307}[：表示以密文形式设置加密密钥。]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[117]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[simple ]{lang="EN-US"}***[key-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_x617709831}[：表示以明文形式设置加密密钥。]{style="font-family:宋体"}*[key-value]{lang="EN-US"}*[为]{style="font-family:宋体"}[16]{lang="EN-US"}[进制格式的字符串，不区分大小写。对于不同的算法，密钥长度不同：]{style="font-family:宋体"}[DES-CBC]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[8]{lang="EN-US"}[个字节；]{style="font-family:宋体"}[3DES-CBC]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}[个字节；]{style="font-family:宋体"}[AES128-CBC]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[16]{lang="EN-US"}[字节；]{style="font-family:宋体"}[AES192-CBC]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[24]{lang="EN-US"}[字节；]{style="font-family:宋体"}[AES256-CBC]{lang="EN-US"}[算法，密钥长度为]{style="font-family:宋体"}[32]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1074266873}

[[此命令仅用于手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1901727508}[安全策略及]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须分别配置]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1345294206}**[inbound]{lang="EN-US"}**[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[两个方向的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1768219866}[IPsec]{lang="EN-US"}[隧道的两端设置的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数必须是完全匹配的。本端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密密钥必须和对端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密密钥一致；本端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密密钥必须和对端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密密钥一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于要应用于]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1028185134}[IPv6]{lang="EN-US"}[路由协议的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，还必须保证本端出方向]{style="font-family:宋体"}[SA]{lang="EN-US"}[的密钥和本端入方向]{style="font-family:宋体"}[SA]{lang="EN-US"}[的密钥一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果先后以不同的方式输入了密钥，则最后设定的密钥有效。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1101270146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1974019120}[IPsec]{lang="EN-US"}[隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的加密密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x11658346}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1795394385}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_874450926}[配置采用]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密算法的密钥为明文]{style="font-family:宋体"}[0x1234567890abcdef]{lang="EN-US"}[；出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的加密算法的密钥为明文]{style="font-family:宋体"}[0xabcdefabcdef1234]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1768154330}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa hex-key encryption inbound esp simple 1234567890abcdef]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa hex-key encryption outbound esp simple abcdefabcdef1234]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x654957031}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1614429519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sa string-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_x334970565}
:::

::: {#41746007 .myid}
[]{#_Toc404793306}[]{#struct_0_x5828_x5730_x534256910}

**IPsec \-- IPsec配置命令 \-- sa idle-time**

------------------------------------------------------------------------

[**[sa idle-time]{lang="EN-US"}**]{#struct_0_x5828_x5730_165279931}[命令用来配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的空闲超时时间。在指定的超时时间内，没有流量使用的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[将被删除。]{style="font-family:宋体"}

[**[undo sa idle-time]{lang="EN-US"}**]{#struct_0_x5828_x5730_363484395}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x167739448}

[**[sa idle-time]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x5828_x5730_1590554918}

[**[undo sa idle-time]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768350938}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1069394965}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x924239064}[安全策略和]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板下的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[空闲超时时间为当前全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[空闲超时时间。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1209787869}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x368847845}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1178381823}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1617428900}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1678779689}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1872872628}

[*[seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_1768285402}[：]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的空闲超时时间，取值范围为]{style="font-family:宋体"}[60]{lang="EN-US"}[～]{style="font-family:宋体"}[86400]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x616719596}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[此功能只适用于]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1861878531}[协商出的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，且只有通过]{style="font-family:宋体"}**[ipsec sa idle-time]{lang="EN-US"}**[命令开启空闲超时功能后，本功能才会生效。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_717991405}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图下没有配置]{style="font-family:宋体"}[IPsec SA ]{lang="EN-US"}[空闲超时时间，将采用全局的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[空闲超时时间（通过命令]{style="font-family:宋体"}**[ipsec sa idle-time]{lang="EN-US"}**[设置）决定]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[是否空闲并进行删除。如果]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图下配置了]{style="font-family:宋体"}[IPsec SA ]{lang="EN-US"}[空闲超时时间，则优先使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图下的配置值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x87494957}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_955246956}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的空闲超时时间为]{style="font-family:宋体"}[600]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x822447505}

[\[Sysname\] ipsec policy map 100 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-map-100\] sa idle-time 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1226339139}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768482010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec sa idle-time]{lang="EN-US"}**]{#struct_0_x5828_x5730_551107710}
:::

::: {#467164029 .myid}
[]{#_Toc404793307}[]{#struct_0_x5828_x5730_1445161147}[]{#_Toc300907131}[]{#_Toc300135409}[]{#_Toc299984528}[]{#_Toc145229940}[]{#_Toc32567533}

**IPsec \-- IPsec配置命令 \-- sa spi**

------------------------------------------------------------------------

[**[sa]{lang="EN-US"}**[ **spi**]{lang="EN-US"}]{#struct_0_x5828_x5730_318879830}[命令用来配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sa** **spi**]{lang="EN-US"}]{#struct_0_x5828_x5730_482921019}[命令用来删除指定的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x480239848}

[**[sa]{lang="EN-US"}**[ **spi** { **inbound** \| **outbound** } { **ah** \| **esp** } *spi-number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1734208505}

[**[undo sa spi]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **ah** \| **esp** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x652315262}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x345920710}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[不存在]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1768416474}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2088636136}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1684515736}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1626468289}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x196418252}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x368803504}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_827424665}

[**[inbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_x131659151}[：指定入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_1767957723}[：指定出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ah]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2019523869}[：指定]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[esp]{lang="EN-US"}**]{#struct_0_x5828_x5730_1848164167}[：指定]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[*[spi-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_788754765}[：]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的安全参数索引，取值范围为]{style="font-family:宋体"}[256]{lang="EN-US"}[～]{style="font-family:宋体"}[4294967295]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1759200481}

[[此命令仅用于手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1880435791}[安全策略以及]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。对于]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，]{style="font-family:宋体"}[IKE]{lang="EN-US"}[将自动协商]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的参数并创建]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，不需要手工设置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须分别配置]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1699832372}**[inbound]{lang="EN-US"}**[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[两个方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的参数，且保证每一个方向上的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的唯一性：对于出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，必须保证三元组（对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、安全协议、]{style="font-family:宋体"}[SPI]{lang="EN-US"}[）唯一；对于入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，必须保证]{style="font-family:宋体"}[SPI]{lang="EN-US"}[唯一。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1953263221}[IPsec]{lang="EN-US"}[隧道的两端设置的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数必须是完全匹配的。本端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[必须和对端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[一样；本端的出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[必须和对端的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[一样。]{style="font-family:宋体"}

[[在配置应用于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5828_x5730_1548011392}[路由协议的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架时，还需要注意的是：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端出方向]{lang="EN-US" style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1767892187}[的]{lang="EN-US" style="font-family:宋体"}[SPI]{lang="EN-US"}[必须和本端入方向]{lang="EN-US" style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[SPI]{lang="EN-US"}[保持一致；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个范围内的、所有设备上的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1607910399}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[均要保持一致。该范围与协议相关：对于]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[，是]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居之间或邻居所在的区域；对于]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[，是]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[直连邻居之间或邻居所在的进程；对于]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，是]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居之间或邻居所在的一个组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1798190759}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1634082053}[配置入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[为]{style="font-family:宋体"}[10000]{lang="EN-US"}[，出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[为]{style="font-family:宋体"}[20000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x411423476}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa spi inbound ah 10000]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa spi outbound ah 20000]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_891188433}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2077035999}
:::

::: {#71034681 .myid}
[]{#_Toc404793308}[]{#struct_0_x5828_x5730_1768088795}

**IPsec \-- IPsec配置命令 \-- sa string-key**

------------------------------------------------------------------------

[**[sa]{lang="EN-US"}**[ **string-key**]{lang="EN-US"}]{#struct_0_x5828_x5730_223522540}[命令用来为手工创建的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[配置字符串形式的密钥。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sa** **string-key**]{lang="EN-US"}]{#struct_0_x5828_x5730_1659355473}[命令用来删除为指定的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[配置的字符串形式的密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_433446445}

[**[sa string-key]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **ah** \| **esp** } { **cipher** \| **simple** } *key-value*]{lang="EN-US"}]{#struct_0_x5828_x5730_x900518347}

[**[undo sa string-key]{lang="EN-US"}**[ { **inbound** \| **outbound** } { **ah** \| **esp** }]{lang="EN-US"}]{#struct_0_x5828_x5730_2055116319}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_361192588}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[未配置]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x817145500}[使用的密钥。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x671862805}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1768023259}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1418350175}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1942515072}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x151198371}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x855730471}

[**[inbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1519324501}[：指定入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_x5828_x5730_1893673377}[：指定出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥。]{style="font-family:宋体"}

[**[ah]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1757545837}[：指定]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[esp]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768219867}[：指定]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1028250670}[：表示以密文形式设置密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x5828_x5730_2014113212}[：表示以明文形式设置密码。]{style="font-family:宋体"}

[*[key-value]{lang="EN-US"}*]{#struct_0_x5828_x5730_1313118833}[：设置的明文密钥或密文密钥，区分大小写。明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串。对于不同的算法，系统会根据输入的字符串自动生成符合算法要求的密钥。对于]{style="font-family:宋体"}[ESP]{lang="EN-US"}[协议，系统会自动地同时生成认证算法的密钥和加密算法的密钥。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_278112733}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[此命令仅用于手工方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x212285345}[安全策略及]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须分别配置]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1110822968}**[inbound]{lang="EN-US"}**[和]{style="font-family:宋体"}**[outbound]{lang="EN-US"}**[两个方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的参数。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_156121891}[IPsec]{lang="EN-US"}[隧道的两端设置的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[参数必须是完全匹配的。本端入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥必须和对端出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥一样；本端出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥必须和对端入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥一样。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果先后以不同的方式输入了密钥，则最后设定的密钥有效。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1038241994}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1768154331}[IPsec]{lang="EN-US"}[隧道的两端，应当以相同的方式输入密钥。如果一端以字符串方式输入密钥，另一端以十六进制方式输入密钥，则不能正确地建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x655022567}

[[在配置应用于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_x5828_x5730_x1647703956}[路由协议的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架时，还需要注意的是：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本端出方向]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x782060521}[IPsec SA]{lang="EN-US"}[的密钥必须和本端入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥保持一致；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[同一个范围内的，所有设备上的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1101642745}[IPsec SA]{lang="EN-US"}[的密钥均要保持一致。该范围内容与协议相关：对于]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[，是]{style="font-family:宋体"}[OSPF]{lang="EN-US"}[邻居之间或邻居所在的区域；对于]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[，是]{style="font-family:宋体"}[RIPng]{lang="EN-US"}[直连邻居之间或邻居所在的进程；对于]{style="font-family:宋体"}[BGP]{lang="EN-US"}[，是]{style="font-family:宋体"}[BGP]{lang="EN-US"}[邻居之间或邻居所在的一个组。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_158666137}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x813372475}[配置采用]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥为明文字符串]{style="font-family:宋体"}[abcdef]{lang="EN-US"}[；出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥为明文字符串]{style="font-family:宋体"}[efcdab]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1768350939}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa string-key inbound ah simple abcdef]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa string-key outbound ah simple efcdab]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1069460501}[在要应用于]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[路由协议的安全策略中，配置采用]{style="font-family:宋体"}[AH]{lang="EN-US"}[协议的入方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥为明文字符串]{style="font-family:宋体"}[abcdef]{lang="EN-US"}[；出方向]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的密钥为明文字符串]{style="font-family:宋体"}[abcdef]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1231263777}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa string-key inbound ah simple abcdef]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] sa string-key outbound ah simple abcdef]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1120569849}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_513428652}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[sa ]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1572922591}**[hex]{lang="EN-US"}[-key]{lang="EN-US"}**
:::

::: {#1162131072 .myid}
[]{#_Toc404793309}[]{#struct_0_x5828_x5730_x383732739}[]{#_Toc300044739}

**IPsec \-- IPsec配置命令 \-- security acl**

------------------------------------------------------------------------

[**[security]{lang="EN-US"}**[ **acl**]{lang="EN-US"}]{#struct_0_x5828_x5730_x421307430}[命令用来指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **security** **acl**]{lang="EN-US"}]{#struct_0_x5828_x5730_1768285403}[命令用来取消]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板引用的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x616654060}

[**[security]{lang="EN-US"}**[ **acl** \[ **ipv6** \] { *acl-number* \| **name** *acl-name* } \[ **aggregation** \| **per-host** \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x829119156}

[**[undo security acl]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1689183675}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_1589766413}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x184721339}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板没有引用任何]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1566328405}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1631025322}[安全策略视图]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1733442723}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1768482011}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_551173246}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x881194093}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_1342707404}[：指定]{style="font-family:宋体"}[IPv6 ACL]{lang="EN-US"}[。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[acl-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1576205422}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[3000]{lang="EN-US"}[～]{style="font-family:宋体"}[3999]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[name ]{lang="EN-US"}***[acl-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_580883223}[：]{style="font-family:宋体"}[ACL]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[aggregation]{lang="EN-US"}**]{#struct_0_x5828_x5730_x192731063}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的数据流保护方式为聚合方式。不支持对]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[数据流采用该保护方式。]{style="font-family:宋体"}

[**[per-host]{lang="EN-US"}**]{#struct_0_x5828_x5730_639611307}[：指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的数据流保护方式为主机方式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x133440265}

[[对于]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1768416475}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，数据流的保护方式包括以下几种：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[标准方式：一条隧道保护一条数据流。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2088570600}[ACL]{lang="EN-US"}[中的每一个规则对应的数据流都会由一条单独创建的隧道来保护。]{style="font-family:宋体"}[不指定]{lang="EN-US" style="font-family:宋体"}**[aggregation]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[per-host]{lang="EN-US"}**[参数的情况下，缺省采用此方式。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[聚合方式：一条隧道保护]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2046792940}[ACL]{lang="EN-US"}[中定义的所有数据流。]{style="font-family:宋体"}[ACL]{lang="EN-US"}[中的所有规则对应的数据流只会由一条创建的隧道来保护。对于聚合方式和标准方式都支持的设备，聚合方式仅用于和老版本的设备互通。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[主机方式：一条隧道保护一条主机到主机的数据流。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2020740463}[ACL]{lang="EN-US"}[中的每一个规则对应的不同主机之间的数据流，都会由一条单独创建的隧道来保护。这种方式下，受保护的网段之间存在多条数据流的情况下，将会消耗更多的系统资源。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1601296570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[手工方式的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2084223250}[IPsec]{lang="EN-US"}[安全策略缺省使用聚合方式，且仅支持聚合方式；]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x571214319}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中可以通过配置来选择不同的保护方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_563663945}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1767957720}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略引用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3001]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x2019327261}

[\[Sysname\] acl advanced 3001]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3001\] rule permit tcp source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3001\] quit]{lang="EN-US"}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] security acl 3001]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2040732261}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略引用]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[高级]{style="font-family:宋体"}[ACL 3002]{lang="EN-US"}[，并设置数据流保护方式为聚合方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1633439238}

[\[Sysname\] acl advanced 3002]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule 0 permit ip source 10.1.2.1 0.0.0.255 destination 10.1.2.2 0.0.0.255]{lang="EN-US"}

[\[Sysname-acl-ipv4-adv-3002\] rule 1 permit ip source 10.1.3.1 0.0.0.255 destination 10.1.3.2 0.0.0.255]{lang="EN-US"}

[\[Sysname\] ipsec policy policy2 1 isakmp]{lang="EN-US"}

[\[Sysname-ipsec-policy-isakmp-policy2-1\] security acl 3002 aggregation]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1653455658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_1767892184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ipsec tunnel]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1607713791}
:::

::: {#-1208437618 .myid}
[]{#_Toc404793310}[]{#struct_0_x5828_x5730_x1295094227}[]{#_Toc342398173}[]{#_Toc336450638}

**IPsec \-- IPsec配置命令 \-- snmp-agent trap enable ipsec**

------------------------------------------------------------------------

[**[snmp-agent  trap enable ipsec]{lang="EN-US"}**]{#struct_0_x5828_x5730_609138840}[命令用来开启]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent]{lang="EN-US"}**[ **trap** **enable** **ipsec**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1339583059}[命令用来关闭指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x5828_x5730_1644480948}

[**[snmp-agent]{lang="EN-US"}**[ **trap** **enable** **ipsec** \[ **auth-failure** \| **decrypt-failure** \| **encrypt-failure** \| **global** \| **invalid-sa-failure** \| **no-sa-failure** \| **policy-add** \| **policy-attach** \| **policy-delete** \| **policy-detach tunnel-start** \| **tunnel-stop**\] \*]{lang="EN-US"}]{#struct_0_x5828_x5730_x217562291}

[**[undo snmp-agent]{lang="EN-US"}**[ **trap** **enable** **ipsec** \[ **auth-failure** \| **decrypt-failure** \| **encrypt-failure** \| **global** \| **invalid-sa-failure** \| **no-sa-failure** \| **policy-add** \| **policy-attach** \| **policy-delete** \| **policy-detach tunnel-start** \| **tunnel-stop**\] \*]{lang="EN-US"}]{#struct_0_x5828_x5730_653584721}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2091621067}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1768088792}[的所有告警功能均处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_223850220}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1782779405}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x82908222}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x876287572}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_795363549}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1541784405}

[**[auth-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_359559432}[：表示认证失败时的告警功能。]{style="font-family:宋体"}[ ]{style="font-size:10.0pt"}

[**[decrypt-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768023256}[：表示解密失败时的告警功能。]{style="font-family:宋体"}

[**[encrypt-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1418808927}[：表示加密失败时的告警功能。]{style="font-family:宋体"}

[**[global]{lang="EN-US"}**]{#struct_0_x5828_x5730_81068945}**[：]{style="font-family:宋体"}**[表示全局告警功能。]{style="font-family:宋体"}

[**[invalid-sa-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_982443882}[：表示无效]{style="font-family:宋体"}[SA]{lang="EN-US"}[的告警功能。]{style="font-family:宋体"}

[**[no-sa-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_x968886818}[：表示无法查找到]{style="font-family:宋体"}[SA]{lang="EN-US"}[时的告警功能。]{style="font-family:宋体"}

[**[policy-add]{lang="EN-US"}**]{#struct_0_x5828_x5730_1034214761}[：表示添加]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略时的告警功能。]{style="font-family:宋体"}

[**[policy-attach]{lang="EN-US"}**]{#struct_0_x5828_x5730_1405174515}[：]{style="font-family:宋体"}[表示将]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略应用到接口时的告警功能。]{style="font-family:宋体"}

[**[policy-delete]{lang="EN-US"}**]{#struct_0_x5828_x5730_1242887736}[：]{style="font-family:宋体"}[表示删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略时的告警功能。]{style="font-family:宋体"}

[**[policy-detach]{lang="EN-US"}**]{#struct_0_x5828_x5730_194837448}[：表示将]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[安全策略从接口下删除时的告警功能]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[tunnel-start]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768219864}[：表示创建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道时的告警功能。]{style="font-family:宋体"}

[**[tunnel-stop]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1028054062}[：表示删除]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道时的告警功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1382745224}

[[如果不指定任何参数，则表示开启或关闭所有类型的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1220690406}[告警功能。]{style="font-family:宋体"}

[[如果希望生成并输出某种类型的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1517403338}[告警信息，则需要保证]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[的全局告警功能以及相应类型的告警功能均处于开启状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2145066984}

[[希望设备在创建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1229159339}[隧道时生成并发送告警信息，需要开启以下告警功能：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1961341645}[开启全局]{style="font-family:宋体"}[IPsec Trap]{lang="EN-US"}[告警。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1768154328}

[\[Sysname\] snmp-agent trap enable ipsec global]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x655481318}[开启创建]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道时的告警功能。]{style="font-family:宋体"}

[[\[Sysname\] snmp-agent trap enable ipsec tunnel-start]{lang="EN-US"}]{#struct_0_x5828_x5730_670858734}
:::

::: {#252523777 .myid}
[]{#_Toc404793311}[]{#struct_0_x5828_x5730_1785160556}[]{#_Toc300044745}

**IPsec \-- IPsec配置命令 \-- transform-set**

------------------------------------------------------------------------

[**[transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_1096709973}[命令用来指定]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[所引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[**[undo transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_1840070368}[命令用来取消]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1336624092}

[**[transform-set ]{lang="EN-US"}***[transform-set-name]{lang="EN-US"}*[&\<1-6\>]{lang="EN-US"}]{#struct_0_x5828_x5730_x1403043212}

[**[undo]{lang="EN-US"}**[ **transform-set** \[ *transform-set-name* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_1768350936}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_x1069263893}[缺省情况]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_2004910434}[安全策略]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全策略模板]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全框架没有引用任何]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_752490013}

[[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_1548032831}[安全策略视图]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全策略模板视图]{style="font-family:宋体"}[/]{lang="EN-US"}[IPsec]{lang="EN-US"}[安全框架视图]{style="font-family:宋体"}

[[【]{style="font-size:10.0pt;font-family:黑体;color:#0096d6"}]{#struct_0_x5828_x5730_160520866}[缺省用户角色]{style="font-family:黑体;color:#0096d6"}[】]{style="font-size:10.0pt;
font-family:黑体;color:#0096d6"}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1846003973}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1731080384}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_967098504}

[*[transform-set-name]{lang="EN-US"}*[&\<1-6\>]{lang="EN-US"}]{#struct_0_x5828_x5730_1768285400}[：]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全]{style="font-family:宋体"}[提议的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}[&\<1-6\>]{lang="EN-US"}[表示前面的参数最多可以输入]{style="font-family:宋体"}[6]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x616850668}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于手工方式的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x2008231138}[IPsec]{lang="EN-US"}[安全策略，只能引用一个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。改变]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略引用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议时，新配置的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议将覆盖旧的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1391435085}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略，一条]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略最多可以引用六个]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商过程中，]{style="font-family:宋体"}[IKE]{lang="EN-US"}[将会在隧道两端配置的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中查找能够完全匹配的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。如果]{style="font-family:宋体"}[IKE]{lang="EN-US"}[在两端找不到完全匹配的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议，则]{style="font-family:宋体"}[SA]{lang="EN-US"}[不能协商成功，需要被保护的报文将被丢弃]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若不指定任何参数，则]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5828_x5730_1044726253}**[undo transform-set]{lang="EN-US"}**[命令表示删除所有引用的]{lang="EN-US" style="font-family:
宋体"}[IPsec]{lang="EN-US"}[安全提议。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x154564648}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1428479998}[配置]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略引用名字为]{style="font-family:宋体"}[prop1]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全提议。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1768482008}

[\[Sysname\] ipsec transform-set prop1]{lang="EN-US"}

[\[Sysname-ipsec-transform-set-prop1\] quit]{lang="EN-US"}

[\[Sysname\] ipsec policy policy1 100 manual]{lang="EN-US"}

[\[Sysname-ipsec-policy-manual-policy1-100\] transform-set prop1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_550583421}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec ]{lang="EN-US"}**[{ **ipv6-policy** \| **policy** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1309154326}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x73884073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec transform-set]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1875516647}
:::

::: {#-891418090 .myid}
[]{#_Toc404793312}[]{#struct_0_x5828_x5730_829051208}

**IPsec \-- IPsec配置命令 \-- tunnel protection ipsec**

------------------------------------------------------------------------

[**[tunnel protection ipsec]{lang="EN-US"}**]{#struct_0_x5828_x5730_2006223027}[命令用来]{style="font-family:宋体"}[在隧道接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo tunnel protection ipsec]{lang="EN-US"}**]{#struct_0_x5828_x5730_1819976330}[命令用来删除指定的]{style="font-family:
宋体"}[IPsec]{lang="EN-US"}[安全框架的应用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1653609165}

[**[tunnel protection ipsec profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1927028449}

[**[undo ]{lang="EN-US"}[tunnel protection ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_2043012546}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_829051209}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_2006223026}[接口下没有引用任何的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1820041866}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_860268673}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1902172541}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1201574351}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_458814896}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2137242931}

[**[profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x2096303731}[：指定使用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，且必须为]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。其中，]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_225454651}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[在隧道接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_189816080}[安全框架后，隧道两端会通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对隧道接口上传输的数据流进行]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护。目前，仅支持对]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道报文进行]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_829051210}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_49907899}[配置使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[prf1]{lang="EN-US"}[来保护接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_643837663}

[\[Sysname\] interface tunnel 1 mode advpn gre]{lang="EN-US"}

[\[Sysname-Tunnel1\] tunnel protection ipsec profile prf1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x714338882}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_x5828_x5730_x527599829}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_x5828_x5730_561650349}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1996515669}
:::

[\
]{lang="EN-US" style="font-size:10.5pt;font-family:\"Arial\",\"sans-serif\""}

::: {.Section3 style="layout-grid:15.6pt"}
:::

::: {#651077146 .myid}
[]{#_Toc279163110}[]{#_Toc404793315}[]{#struct_0_x5828_x5730_1768416472}[]{#_Toc339467213}

**IKE \-- IKE配置命令 \-- authentication-algorithm**

------------------------------------------------------------------------

[**[authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_2088242920}[命令用来指定一个供]{style="font-family:
宋体"}[IKE]{lang="EN-US"}[提议使用的认证算法。]{style="font-family:宋体"}

[**[undo authentication-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_1811775863}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_100754075}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_1839407940}[模式下：]{style="font-family:宋体"}

[**[authentication-algorithm]{lang="EN-US"}**[ { **md5** \| **sha** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1543915838}

[**[undo]{lang="EN-US"}**[ **authentication-algorithm**]{lang="EN-US"}]{#struct_0_x5828_x5730_681852462}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x462177979}[模式下：]{style="font-family:宋体"}

[**[authentication-algorithm ]{lang="EN-US"}**[ **sha**]{lang="EN-US"}]{#struct_0_x5828_x5730_1323323641}

[**[undo]{lang="EN-US"}**[ **authentication-algorithm**]{lang="EN-US"}]{#struct_0_x5828_x5730_1767957721}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2019392797}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_342410879}[提议使用的认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1798582256}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_602778312}[提议视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2002816217}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1873771101}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1767892185}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1607779327}

[**[md5]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1601440791}[：指定认证算法为]{style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[sha]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1567984258}[：指定认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_363517994}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x566149966}[指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[的认证算法为]{style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_2106388609}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\] authentication-algorithm sha]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1534639006}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1858583275}
:::

::: {#-1695505525 .myid}
[]{#_Toc404793316}[]{#struct_0_x5828_x5730_1768088793}[]{#_Toc339467214}

**IKE \-- IKE配置命令 \-- authentication-method**

------------------------------------------------------------------------

[**[authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_223915756}[命令用来指定一个供]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议使用的认证方法。]{style="font-family:宋体"}

[**[undo authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_x190797214}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1131125476}

[**[authentication-method]{lang="EN-US"}**[ { **dsa-signature** \| **pre-share** \| **rsa-signature** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x469578248}

[**[undo authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_535395409}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1429127021}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_388315091}[提议使用预共享密钥的认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1768023257}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1418743391}[提议视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_254486525}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1039017962}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1380377734}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1852123799}

[**[dsa-signature]{lang="EN-US"}**]{#struct_0_x5828_x5730_x467119878}[：指定认证方法为]{style="font-family:宋体"}[DSA]{lang="EN-US"}[数字签名方法。]{style="font-family:宋体"}

[**[pre-share]{lang="EN-US"}**]{#struct_0_x5828_x5730_x486084481}[：指定认证方法为预共享密钥方法。]{style="font-family:宋体"}

[**[rsa-signature]{lang="EN-US"}**]{#struct_0_x5828_x5730_1298273898}[：指定认证方法为]{style="font-family:宋体"}[RSA]{lang="EN-US"}[数字签名方法。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1768219865}

[[认证方法分为预共享密钥认证和数字签名认证（包括]{style="font-family:宋体"}[RSA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1028119598}[数字签名认证和]{style="font-family:宋体"}[DSA]{lang="EN-US"}[数字签名认证）。预共享密钥认证机制简单、不需要证书，常在小型组网环境中使用；数字签名认证安全性更高，常在"中心---分支"模式的组网环境中使用。例如，在"中心---分支"组网中使用预共享密钥认证进行]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时，中心侧可能需要为每个分支配置一个预共享密钥，当分支很多时，配置会很复杂，而使用数字签名认证时中心只需配置一个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x433950043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[协商双方必须有匹配的认证方法。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1249305332}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定认证方法为]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x620304853}[RSA]{lang="EN-US"}[数字签名方法或者]{style="font-family:宋体"}[DSA]{lang="EN-US"}[数字签名方法，则还必须保证对端从]{style="font-family:宋体"}[CA]{lang="EN-US"}[（证书认证机构）获得数字证书。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定认证方法为预共享密钥方法，必须使用]{lang="EN-US" style="font-family:宋体"}**[pre-shared-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_x815911259}[命令在两端配置相同的预共享密钥。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_233922148}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1191930939}[指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[的认证方法为预共享密钥。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1768154329}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\] authentication-method pre-share]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x655546854}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_371341002}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ike keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_1166998820}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[pre-shared-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_1586867659}
:::

::: {#543736395 .myid}
[]{#_Toc404793317}[]{#struct_0_x5828_x5730_x1221864385}[]{#_Toc339467215}

**IKE \-- IKE配置命令 \-- certificate domain**

------------------------------------------------------------------------

[**[certificate domain]{lang="EN-US"}**]{#struct_0_x5828_x5730_x819374648}[命令用来指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商采用数字签名认证时使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo certificate domain]{lang="EN-US"}**]{#struct_0_x5828_x5730_1082631340}[命令用来取消]{style="font-family:宋体"}[配置]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x869864505}

[**[certificate domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1768350937}

[**[undo certificate domain ]{lang="EN-US"}***[domain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1069329429}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1199104756}

[[未指定用于]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_140766188}[协商的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_720869451}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_299555753}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1770242279}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_45948545}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1768285401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x616785132}

[*[domain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1249431411}[：]{lang="EN-US" style="font-family:宋体"}[PKI]{lang="EN-US"}[域的名称]{lang="EN-US" style="font-family:宋体"}[，为]{lang="EN-US" style="font-family:
宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_103637238}

[[可通过多次执行本命令指定多个]{style="font-family:宋体"}[PKI]{lang="EN-US"}]{#struct_0_x5828_x5730_854392428}[域。如果在]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中指定了]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，则使用指定的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域发送本端证书请求、验证对端证书请求、发送本端证书、验证对端证书、进行数字签名。如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中没有指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，则使用设备上配置的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域进行以上证书相关的操作。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1034652689}[中最多可以引用六个]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1749221865}[可以通过]{style="font-family:宋体"}[PKI]{lang="EN-US"}[自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书、自动申请证书，对这种情况，有几点需要说明：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于发起方：若在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1995405854}[IKE profile]{lang="EN-US"}[中指定了]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，且]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的证书申请为自动申请方式，则发起方会自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书；若在]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中没有指定]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，则发起方不会自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，需要手动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于响应方：第一阶段采用主模式的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x195472557}[IKE]{lang="EN-US"}[协商时，响应方不会自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，需要手动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书；第一阶段采用野蛮模式的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时，若响应方找到了匹配的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[并且]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[下指定了]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域，且]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域中的证书申请为自动申请方式，则会自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书；否则，响应方不会自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，需要手动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1768482009}[IKE]{lang="EN-US"}[协商过程中先自动获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，再自动申请证书。若]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书存在，则不获取]{style="font-family:宋体"}[CA]{lang="EN-US"}[证书，直接自动申请证书。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_550648957}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1635658979}[在]{style="font-family:宋体"}[IKE profile 1]{lang="EN-US"}[中指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商时使用的]{style="font-family:宋体"}[PKI]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x2138064469}

[\[Sysname\] ike profile 1]{lang="EN-US"}

[\[Sysname-ike-profile-1\] certificate domain abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1671530343}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1686490017}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pki domain]{lang="EN-US"}**]{#struct_0_x5828_x5730_1836401983}[（]{lang="EN-US" style="font-family:宋体"}[安全命令参考]{lang="EN-US" style="font-family:宋体"}[/PKI]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#-839731268 .myid}
[]{#_Toc404793318}[]{#struct_0_x5828_x5730_x144793596}[]{#_Toc339467216}

**IKE \-- IKE配置命令 \-- dh**

------------------------------------------------------------------------

[**[dh]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768416473}[命令用来配置]{style="font-family:宋体"}[IKE]{lang="EN-US"}[阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时所使用的]{style="font-family:宋体"}[DH]{lang="EN-US"}[密钥交换参数。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **dh**]{lang="EN-US"}]{#struct_0_x5828_x5730_2088177384}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_652986473}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_120603891}[模式下：]{style="font-family:宋体"}

[**[dh ]{lang="EN-US"}**[{ **group1** \| **group14** \| **group2** \| **group24** \| **group5** }]{lang="EN-US"}]{#struct_0_x5828_x5730_1284032705}

[**[undo dh]{lang="EN-US"}**]{#struct_0_x5828_x5730_x333083076}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x407546297}[模式下：]{style="font-family:宋体"}

[**[dh group14]{lang="EN-US"}**]{#struct_0_x5828_x5730_1545591426}

[**[undo dh]{lang="EN-US"}**]{#struct_0_x5828_x5730_1767957718}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2019851552}

[[非]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_886506598}[模式下：]{lang="EN-US" style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1599255652}[提议使用的]{lang="EN-US" style="font-family:宋体"}[DH]{lang="EN-US"}[密钥交换参数为]{lang="EN-US" style="font-family:宋体"}**[group1]{lang="EN-US"}**[，即]{lang="EN-US" style="font-family:宋体"}[768-bit]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x75254076}[模式下：]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1768157807}[提议使用的]{lang="EN-US" style="font-family:宋体"}[DH]{lang="EN-US"}[密钥交换参数为]{lang="EN-US" style="font-family:宋体"}**[group14]{lang="EN-US"}**[，即]{lang="EN-US" style="font-family:宋体"}[2048-bit]{lang="EN-US"}[的]{lang="EN-US" style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1485667351}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_246224738}[提议视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1056278706}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1767892182}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1608107007}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_830619604}

[**[group1]{lang="EN-US"}**]{#struct_0_x5828_x5730_1045571276}[：指定阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时采用]{style="font-family:宋体"}[768-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[group14]{lang="EN-US"}**]{#struct_0_x5828_x5730_x989677623}[：指定阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时采用]{style="font-family:宋体"}[2048-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[group2]{lang="EN-US"}**]{#struct_0_x5828_x5730_x601120005}[：指定阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时采用]{style="font-family:宋体"}[1024-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[group24]{lang="EN-US"}**]{#struct_0_x5828_x5730_x185667362}[：指定阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时采用含]{style="font-family:宋体"}[256-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[sub-group]{lang="EN-US"}[的]{style="font-family:宋体"}[2048-bit Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[group5]{lang="EN-US"}**]{#struct_0_x5828_x5730_754754303}[：指定阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时采用]{style="font-family:宋体"}[1536-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1553577262}

[**[group1]{lang="EN-US"}**]{#struct_0_x5828_x5730_1768088790}[提供了最低的安全性，但是处理速度最快。]{style="font-family:宋体"}**[group24]{lang="EN-US"}**[提供了最高的安全性，但是处理速度最慢。其它的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[随着其位数的增加提供更高的安全性，但是处理速度会相应减慢。请根据实际组网环境中对安全性和性能的要求选择合适的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_223719148}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1591045210}[指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[使用]{style="font-family:宋体"}[2048-bit]{lang="EN-US"}[的]{style="font-family:宋体"}[Diffie-Hellman group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1414618071}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\] dh group14]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_477716309}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x721316794}
:::

::: {#926088509 .myid}
[]{#_Toc404793319}[]{#struct_0_x5828_x5730_x276686889}[]{#_Toc339467217}

**IKE \-- IKE配置命令 \-- display ike proposal**

------------------------------------------------------------------------

[**[display]{lang="EN-US"}**[ **ike** **proposal**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1780629909}[命令用来显示所有]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1768023254}

[**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1418677855}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1670488685}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1463722177}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1806484312}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_807847640}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x272234034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1930767290}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_1768219862}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1028447278}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x930145747}[提议按照优先级的先后顺序显示。如果没有配置任何]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议，则只显示缺省的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1187093253}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_251527898}[显示]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display ike proposal]{lang="EN-US"}]{#struct_0_x5828_x5730_x1921278655}

[ Priority Authentication Authentication Encryption  Diffie-Hellman Duration]{lang="EN-US"}

[              method       algorithm    algorithm       group      (seconds)]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[ 1        RSA-SIG            MD5        DES-CBC     Group 1        5000]{lang="EN-US"}

[ 11       PRE-SHARED-KEY     MD5        DES-CBC     Group 1        50000]{lang="EN-US"}

[ default  PRE-SHARED-KEY     SHA1       DES-CBC     Group 1        86400]{lang="EN-US"}

[[表2-1 ]{lang="EN-US"}[display ike proposal]{lang="EN-US"}]{#struct_0_x5828_x5730_x63651967}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x796686990}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1768154326}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x655350246}

[[Priority]{lang="EN-US"}]{#struct_0_x5828_x5730_1474294339}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_129828786}[提议的优先级]{style="font-family:宋体"}

[[Authentication method]{lang="EN-US"}]{#struct_0_x5828_x5730_219270540}

[[IKE]{lang="FR"}]{#struct_0_x5828_x5730_x2095339042}[提议使用的认证方法，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRE-SHARED-KEY]{lang="EN-US"}]{#struct_0_x5828_x5730_1768350934}[：预共享密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSA-SIG]{lang="EN-US"}]{#struct_0_x5828_x5730_x1069132821}[：]{lang="EN-US" style="font-family:宋体"}[RSA]{lang="EN-US"}[签名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSA-SIG]{lang="EN-US"}]{#struct_0_x5828_x5730_x1218527803}[：]{lang="EN-US" style="font-family:宋体"}[DSA]{lang="EN-US"}[签名]{lang="EN-US" style="font-family:宋体"}

[[Authentication algorithm]{lang="EN-US"}]{#struct_0_x5828_x5730_1827877478}

[[IKE]{lang="FR"}]{#struct_0_x5828_x5730_2051391042}[提议使用的认证算法，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x5828_x5730_x1770216626}[：]{lang="EN-US" style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA1]{lang="EN-US"}]{#struct_0_x5828_x5730_1768285398}[：]{lang="EN-US" style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[Encryption algorithm]{lang="EN-US"}]{#struct_0_x5828_x5730_2103614221}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x2061571563}[提议使用的加密算法，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3DES-CBC]{lang="EN-US"}]{#struct_0_x5828_x5730_x424294924}[：]{lang="EN-US" style="font-family:宋体"}[168]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[3DES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-128]{lang="EN-US"}]{#struct_0_x5828_x5730_x2113065400}[：]{lang="EN-US" style="font-family:宋体"}[128]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-192]{lang="EN-US"}]{#struct_0_x5828_x5730_1768482006}[：]{lang="EN-US" style="font-family:宋体"}[192]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-256]{lang="EN-US"}]{#struct_0_x5828_x5730_550976637}[：]{lang="EN-US" style="font-family:宋体"}[256]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DES-CBC]{lang="EN-US"}]{#struct_0_x5828_x5730_361036995}[：]{lang="EN-US" style="font-family:宋体"}[56]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[DES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[Diffie-Hellman group]{lang="EN-US"}]{#struct_0_x5828_x5730_x1223218055}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1768416470}[阶段]{style="font-family:宋体"}[1]{lang="EN-US"}[密钥协商时所使用的]{style="font-family:宋体"}[DH]{lang="EN-US"}[密钥交换参数，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 1]{lang="EN-US"}]{#struct_0_x5828_x5730_2088373992}[：]{lang="EN-US" style="font-family:宋体"}[DH group1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 2]{lang="EN-US"}]{#struct_0_x5828_x5730_239203770}[：]{lang="EN-US" style="font-family:宋体"}[DH group2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 5]{lang="EN-US"}]{#struct_0_x5828_x5730_x686374713}[：]{lang="EN-US" style="font-family:宋体"}[DH group5]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 14]{lang="EN-US"}]{#struct_0_x5828_x5730_x383641837}[：]{lang="EN-US" style="font-family:宋体"}[DH group14]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 24]{lang="EN-US"}]{#struct_0_x5828_x5730_1767957719}[：]{lang="EN-US" style="font-family:宋体"}[DH group24]{lang="EN-US"}

[[Duration (seconds)]{lang="EN-US"}]{#struct_0_x5828_x5730_x2019917088}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1058704757}[提议中指定的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[存活时间，单位为秒]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1637862568}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike]{lang="EN-US"}**[ **proposal**]{lang="EN-US"}]{#struct_0_x5828_x5730_x292750002}

::::: {#-1365692897 .myid}
[]{#_Toc404793320}[]{#struct_0_x5828_x5730_x868014520}[]{#_Toc339467218}

**IKE \-- IKE配置命令 \-- display ike sa**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_1767892183}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x1608172543}
:::

[ ]{lang="EN-US"}

[**[display]{lang="EN-US"}**[ **ike** **sa**]{lang="EN-US"}]{#struct_0_x5828_x5730_x296803882}[命令用来显示当前]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1447573280}

[**[display ike sa]{lang="EN-US"}**[ ]{lang="EN-US"}[\[ **verbose** \[ **connection-id** *connection-id* \| **remote-address** \[ **ipv6** \] *remote-address* \[ **vpn-instance** *vpn-name* \] \] \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x1960854787}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_180245804}

[[任意视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_570673210}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_786115158}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1768088791}

[[network-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_223784684}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2019418528}

[[mdc-operator]{lang="EN-US"}]{#struct_0_x5828_x5730_x378965368}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1777704785}

[**[verbose]{lang="EN-US"}**]{#struct_0_x5828_x5730_857342214}[：显示当前]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[**[connection-id]{lang="EN-US"}***[ connection-id]{lang="EN-US"}*]{#struct_0_x5828_x5730_x706594979}[：按照连接标识符显示]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2000000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[remote-address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1529822285}[：显示指定对端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_x749405170}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[remote-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_1768023255}[：对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1418612319}[：显示指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[内的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息，]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[如果不指定该参数，则表示显示的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1217807614}

[[若不指定任何参数，则显示当前所有]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1348459262}[的摘要信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1651221309}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1302847867}[显示当前所有]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的摘要信息。]{style="font-family:宋体"}

[[\<Sysname\> display ike sa]{lang="EN-US"}]{#struct_0_x5828_x5730_1768219863}

[    Connection-ID  Remote          Flag        DOI]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      1            202.38.0.2      RD          IPSEC]{lang="EN-US"}

[Flags:]{lang="EN-US"}

[RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING]{lang="EN-US"}

[[表2-2 ]{lang="EN-US"}[display ike sa]{lang="EN-US"}]{#struct_0_x5828_x5730_x1028512814}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x794030803}[[字段]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x33948818}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_x5828_x5730_306218867}

[[Connection-ID]{lang="EN-US"}]{#struct_0_x5828_x5730_x1883658662}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1637441167}[的标识符]{style="font-family:宋体"}

[[Remote]{lang="EN-US"}]{#struct_0_x5828_x5730_x279266680}

[[此]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1768154327}[的对端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Flags]{lang="EN-US"}]{#struct_0_x5828_x5730_x655415782}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x868111479}[的状态，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RD]{lang="EN-US"}]{#struct_0_x5828_x5730_x1819372201}[（]{lang="EN-US" style="font-family:宋体"}[READY]{lang="EN-US"}[）：表示此]{lang="EN-US" style="font-family:宋体"}[IKE SA]{lang="EN-US"}[已建立成功]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[ST]{lang="EN-US"}]{#struct_0_x5828_x5730_146993162}[（]{style="font-family:宋体"}[STAYALIVE]{lang="EN-US"}[）：]{lang="EN-US" style="font-family:宋体"}[表示此端是隧道协商发起方]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RL]{lang="EN-US"}]{#struct_0_x5828_x5730_x1446197442}[（]{lang="EN-US" style="font-family:宋体"}[REPLACED]{lang="EN-US"}[）：表示此]{lang="EN-US" style="font-family:宋体"}[IKE SA]{lang="EN-US"}[已经被新的]{lang="EN-US" style="font-family:宋体"}[IKE SA]{lang="EN-US"}[代替，一段时间后将被删除]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FD]{lang="EN-US"}]{#struct_0_x5828_x5730_1768350935}[（]{style="font-family:宋体"}[FADING]{lang="EN-US"}[）：表示此]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[正在接近超时时间，目前还在使用，但即将被删除]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Unknown]{lang="EN-US"}]{#struct_0_x5828_x5730_x1069198357}[：表示]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商的状态未知]{style="font-family:宋体"}

[[DOI]{lang="EN-US"}]{#struct_0_x5828_x5730_x484617752}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_279683840}[所属解释域，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[IPSEC]{lang="EN-US"}]{#struct_0_x5828_x5730_1768285399}[：表示此]{lang="EN-US" style="font-family:宋体"}[IKE SA]{lang="EN-US"}[使用的]{style="font-family:宋体"}[DOI]{lang="EN-US"}[为]{style="font-family:宋体"}[IPSEC DOI]{lang="EN-US"}

[ ]{lang="EN-US" style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_2103679757}[显示当前]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ike sa verbose]{lang="EN-US"}]{#struct_0_x5828_x5730_1768482007}

[    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Connection ID: 2]{lang="EN-US"}

[    Outside VPN: 1]{lang="EN-US"}

[    Inside VPN: 1]{lang="EN-US"}

[    Profile: prof1]{lang="EN-US"}

[    Transmitting entity: Initiator]{lang="EN-US"}

[    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Local IP: 4.4.4.4]{lang="EN-US"}

[    Local ID type: IPV4_ADDR]{lang="EN-US"}

[    Local ID: 4.4.4.4]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Remote IP: 4.4.4.5]{lang="EN-US"}

[    Remote ID type: IPV4_ADDR]{lang="EN-US"}

[    Remote ID: 4.4.4.5]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Authentication-method: PRE-SHARED-KEY]{lang="EN-US"}

[    Authentication-algorithm: SHA1]{lang="EN-US"}

[    Encryption-algorithm: AES-CBC-128]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Life duration(sec): 86400]{lang="EN-US"}

[    Remaining key duration(sec): 86379]{lang="EN-US"}

[    Exchange-mode: Main]{lang="EN-US"}

[    Diffie-Hellman group: Group 1]{lang="EN-US"}

[    NAT traversal: Not detected]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_551042173}[显示目的地址为]{style="font-family:宋体"}[4.4.4.5]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display ike sa verbose remote-address 4.4.4.5]{lang="EN-US"}]{#struct_0_x5828_x5730_1768416471}

[    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Connection ID: 2]{lang="EN-US"}

[    Outside VPN: 1]{lang="EN-US"}

[    Inside VPN: 1]{lang="EN-US"}

[    Profile: prof1]{lang="EN-US"}

[    Transmitting entity: Initiator]{lang="EN-US"}

[    \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[    Local IP: 4.4.4.4]{lang="EN-US"}

[    Local ID type: IPV4_ADDR]{lang="EN-US"}

[    Local ID: 4.4.4.4]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Remote IP: 4.4.4.5]{lang="EN-US"}

[    Remote ID type: IPV4_ADDR]{lang="EN-US"}

[    Remote ID: 4.4.4.5]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Authentication-method: PRE-SHARED-KEY]{lang="EN-US"}

[    Authentication-algorithm: SHA1]{lang="EN-US"}

[    Encryption-algorithm: AES-CBC-128]{lang="EN-US"}

[ ]{lang="EN-US"}

[    Life duration(sec): 86400]{lang="EN-US"}

[    Remaining key duration(sec): 86379]{lang="EN-US"}

[    Exchange-mode: Main]{lang="EN-US"}

[    Diffie-Hellman group: Group 1]{lang="EN-US"}

[    NAT traversal: Not detected]{lang="EN-US"}

[[表2-3 ]{lang="EN-US"}[display ike sa verbose]{lang="EN-US"}]{#struct_0_x5828_x5730_2088308456}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x798355577}[[字段]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x5828_x5730_x2005547663}

[[描述]{style="font-size:10.0pt;
   font-family:黑体"}]{#struct_0_x5828_x5730_x1786301699}

[[Connection ID]{lang="EN-US"}]{#struct_0_x5828_x5730_x960925633}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1489737553}[的标识符]{style="font-family:宋体"}

[[Outside VPN]{lang="EN-US"}]{#struct_0_x5828_x5730_413874423}

[[接收报文的接口所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_x5828_x5730_x1051906546}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[[Inside VPN]{lang="EN-US"}]{#struct_0_x5828_x5730_x1371187450}

[[被保护数据所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}]{#struct_0_x5828_x5730_x1968364560}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称]{style="font-family:宋体"}

[[Profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x960991169}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x315451842}[协商过程中匹配到的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的名称，如果协商过程中没有匹配到任何]{style="font-family:宋体"}[profile]{lang="EN-US"}[，则该字段不会显示任何]{style="font-family:宋体"}[KE profile]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[Transmitting entity]{lang="EN-US"}]{#struct_0_x5828_x5730_1764449798}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x704306413}[协商中的实体角色，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Initiator]{lang="EN-US"}]{#struct_0_x5828_x5730_1279777365}[：]{lang="EN-US" style="font-family:宋体"}[发起方]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Responder]{lang="EN-US"}]{#struct_0_x5828_x5730_751401907}[：响应方]{lang="EN-US" style="font-family:宋体"}

[[Local IP]{lang="EN-US"}]{#struct_0_x5828_x5730_x960794561}

[[本端安全网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1482886191}[地址]{style="font-family:宋体"}

[[Local ID type]{lang="EN-US"}]{#struct_0_x5828_x5730_x1629077319}

[[本端安全网关的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1341304777}[身份信息]{style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[Local ID]{lang="EN-US"}]{#struct_0_x5828_x5730_x1429769844}

[[本端安全网关的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x960860097}[身份信息]{style="font-family:宋体"}

[[Remote IP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1110629937}

[[对端安全网关的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_x1443159632}[地址]{style="font-family:宋体"}

[[Remote ID type]{lang="EN-US"}]{#struct_0_x5828_x5730_1700520253}

[[对端安全网关的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x960663489}[身份信息]{style="font-family:宋体"}[类型]{style="font-family:宋体"}

[[Remote ID]{lang="EN-US"}]{#struct_0_x5828_x5730_2016509791}

[[对端安全网关的]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x1620170501}[身份信息]{style="font-family:宋体"}

[[Authentication-method]{lang="EN-US"}]{#struct_0_x5828_x5730_844761508}

[[IKE]{lang="FR"}]{#struct_0_x5828_x5730_594083668}[提议使用的认证方法]{style="font-family:宋体"}[，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[PRE-SHARED-KEY]{lang="EN-US"}]{#struct_0_x5828_x5730_x960729025}[：预共享密钥]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RSA-SIG]{lang="EN-US"}]{#struct_0_x5828_x5730_1270018348}[：]{lang="EN-US" style="font-family:宋体"}[RSA]{lang="EN-US"}[签名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DSA-SIG]{lang="EN-US"}]{#struct_0_x5828_x5730_1366331443}[：]{lang="EN-US" style="font-family:宋体"}[DSA]{lang="EN-US"}[签名]{lang="EN-US" style="font-family:宋体"}

[[Authentication-algorithm]{lang="EN-US"}]{#struct_0_x5828_x5730_x1753626490}

[[IKE]{lang="FR"}]{#struct_0_x5828_x5730_x960532417}[提议使用的认证算法]{style="font-family:宋体"}[，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[MD5]{lang="EN-US"}]{#struct_0_x5828_x5730_x702215588}[：]{lang="EN-US" style="font-family:宋体"}[HMAC-MD5]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[SHA1]{lang="EN-US"}]{#struct_0_x5828_x5730_1411987390}[：]{lang="EN-US" style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[Encryption-algorithm]{lang="EN-US"}]{#struct_0_x5828_x5730_2006022306}

[[IKE]{lang="FR"}]{#struct_0_x5828_x5730_x960597953}[提议使用的加密算法，]{style="font-family:宋体"}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[3DES-CBC]{lang="EN-US"}]{#struct_0_x5828_x5730_1644253543}[：]{lang="EN-US" style="font-family:宋体"}[168]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[3DES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-128]{lang="EN-US"}]{#struct_0_x5828_x5730_x621752448}[：]{lang="EN-US" style="font-family:宋体"}[128]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-192]{lang="EN-US"}]{#struct_0_x5828_x5730_x67769676}[：]{lang="EN-US" style="font-family:宋体"}[192]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[AES-CBC-256]{lang="EN-US"}]{#struct_0_x5828_x5730_x960401345}[：]{lang="EN-US" style="font-family:宋体"}[256]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[AES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[DES-CBC]{lang="EN-US"}]{#struct_0_x5828_x5730_x716204573}[：]{lang="EN-US" style="font-family:宋体"}[56]{lang="EN-US"}[位]{lang="EN-US" style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{lang="EN-US" style="font-family:宋体"}[DES]{lang="EN-US"}[算法]{lang="EN-US" style="font-family:宋体"}

[[Life duration(sec)]{lang="EN-US"}]{#struct_0_x5828_x5730_2058003553}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x960466881}[的存活时间]{style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[Remaining key duration(sec)]{lang="EN-US"}]{#struct_0_x5828_x5730_848026862}

[[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_221244519}[的剩余存活时间]{style="font-family:宋体"}[，单位为秒]{style="font-family:宋体"}

[[Exchange-mode]{lang="EN-US"}]{#struct_0_x5828_x5730_x1487841550}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x960925632}[第一阶段的协商模式，]{style="font-family:宋体"}[包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Main]{lang="EN-US"}]{#struct_0_x5828_x5730_x1489803089}[：主模式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Aggressive]{lang="EN-US"}]{#struct_0_x5828_x5730_x1505320207}[：]{style="font-family:宋体"} [野蛮模式]{style="font-family:宋体"}

[[Diffie-Hellman group]{lang="EN-US"}]{#struct_0_x5828_x5730_x960991168}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x315386306}[第一阶段密钥协商时所使用的]{style="font-family:宋体"}[DH]{lang="EN-US"}[密钥交换参数，包括：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 1]{lang="EN-US"}]{#struct_0_x5828_x5730_915127154}[：]{lang="EN-US" style="font-family:宋体"}[DH group1]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 2]{lang="EN-US"}]{#struct_0_x5828_x5730_x778777020}[：]{lang="EN-US" style="font-family:宋体"}[DH group2]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 5]{lang="EN-US"}]{#struct_0_x5828_x5730_x960794560}[：]{lang="EN-US" style="font-family:宋体"}[DH group5]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 14]{lang="EN-US"}]{#struct_0_x5828_x5730_x1482820655}[：]{lang="EN-US" style="font-family:宋体"}[DH group14]{lang="EN-US"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Group 24]{lang="EN-US"}]{#struct_0_x5828_x5730_968516698}[：]{lang="EN-US" style="font-family:宋体"}[DH group24]{lang="EN-US"}

[[NAT traversal]{lang="EN-US"}]{#struct_0_x5828_x5730_x960860096}

[[是否检测到协商双方之间存在]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x5828_x5730_x1110695473}[网关]{style="font-family:宋体"}[设备]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-1027912526 .myid}
[]{#_Toc404793321}[]{#struct_0_x5828_x5730_763722110}[]{#_Toc339467219}

**IKE \-- IKE配置命令 \-- dpd**

------------------------------------------------------------------------

[**[dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_863930039}[命令用来配置]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_273952525}[命令用来关闭]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1638973882}

[**[dpd interval ]{lang="EN-US"}***[interval-seconds ]{lang="EN-US"}*[\[ **retry** *seconds* \] { **on-demand** \| **periodic** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x960663488}

[**[undo dpd interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_2016444255}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x34157679}

[[IKE DPD]{lang="EN-US"}]{#struct_0_x5828_x5730_1700943254}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x8081878}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1595306099}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1005470204}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1141187430}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x960729024}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1269952812}

[**[interval ]{lang="EN-US"}***[interval-seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x963363876}[：指定触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。对于按需探测模式，指定经过多长时间没有从对端收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文，则触发一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测；对于定时探测模式，指触发一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测的时间间隔。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1991541061}[：指定]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文的重传时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒。缺省情况下，]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文的重传时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[on-demand]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1967380870}[：指定按需探测模式，根据流量来探测对端是否存活，在本端发送用户报文时，如果发现当前距离最后一次收到对端报文的时间超过指定的触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔，则触发]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测。]{style="font-family:宋体"}

[**[periodic]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1628480828}[：指定定时探测模式，按照触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔定时探测对端是否存活。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x837799871}

[[IKE DPD]{lang="EN-US"}]{#struct_0_x5828_x5730_1739395826}[有两种模式：按需探测模式和定时探测模式。一般若无特别要求，建议使用按需探测模式，在此模式下，仅在本端需要发送报文时，才会触发探测；如果需要尽快地检测出对端的状态，则可以使用定时探测模式。在定时探测模式下工作，会消耗更多的带宽和计算资源，因此当设备与大量的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[对端通信时，应优先考虑使用按需探测模式。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x960532416}[视图下和系统视图下都配置了]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能，则]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[视图下的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[配置生效，如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[视图下没有配置]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能，则采用系统视图下的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[建议配置的]{style="font-family:宋体"}**[interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_x702150052}[时间大于]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[时间，使得直到当前]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测结束才可以触发下一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测，在重传]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文过程中不会触发新的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x928714535}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_109915922}[为]{style="font-family:宋体"}[IKE profile 1]{lang="EN-US"}[配置]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能，指定若]{style="font-family:宋体"}[10]{lang="EN-US"}[秒内没有从对端收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文，则触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测，]{style="font-family:宋体"}[DPD]{lang="EN-US"}[请求报文的重传时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，探测模式为按需探测。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1509212391}

[\[Sysname\] ike profile 1]{lang="EN-US"}

[\[Sysname-ike-profile-1\] dpd interval 10 retry 5 on-demand]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1219727576}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ike dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1703708349}
:::

::: {#711665932 .myid}
[]{#_Toc404793322}[]{#struct_0_x5828_x5730_952541877}[]{#_Toc339467220}[]{#_Toc286333932}[]{#_Toc286333933}

**IKE \-- IKE配置命令 \-- encryption-algorithm**

------------------------------------------------------------------------

[**[encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960597952}[命令用来指定一个供]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议使用的加密算法。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **encryption-algorithm**]{lang="EN-US"}]{#struct_0_x5828_x5730_1644319079}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2080922988}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_1650425962}[模式下：]{style="font-family:宋体"}

[**[encryption-algorithm]{lang="EN-US"}**[ { **3des-cbc** \| **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** \| **des-cbc** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x180363901}

[**[undo encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_x124858386}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_1795401404}[模式下：]{style="font-family:宋体"}

[**[encryption-algorithm]{lang="EN-US"}**[ { **aes-cbc-128** \| **aes-cbc-192** \| **aes-cbc-256** }]{lang="EN-US"}]{#struct_0_x5828_x5730_2029839245}

[**[undo encryption-algorithm]{lang="EN-US"}**]{#struct_0_x5828_x5730_524107726}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960401344}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_x716270109}[模式下：]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1050291718}[提议使用的加密算法为]{style="font-family:宋体"}**[des-cbc]{lang="EN-US"}**[，即]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[56-bit DES]{lang="EN-US"}[加密算法。]{style="font-family:宋体"}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_10411010}[模式下：]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_2000332981}[提议使用的加密算法为]{style="font-family:宋体"}**[aes-cbc-128]{lang="EN-US"}**[，即]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x905237096}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_662982280}[提议视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x672202600}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x960466880}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_847961326}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_626770671}

[**[3des-cbc]{lang="EN-US"}**]{#struct_0_x5828_x5730_51769569}[：指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[安全提议采用的加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[3DES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[3DES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[168]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[**[aes-cbc-128]{lang="EN-US"}**]{#struct_0_x5828_x5730_308469857}[：指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[安全提议采用的加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[128]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[**[aes-cbc-192]{lang="EN-US"}**]{#struct_0_x5828_x5730_978176607}[：指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[安全提议采用的加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[192]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[**[aes-cbc-256]{lang="EN-US"}**]{#struct_0_x5828_x5730_x993493401}[：指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[安全提议采用的加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[AES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[256]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[**[des-cbc]{lang="EN-US"}**]{#struct_0_x5828_x5730_1542441044}[：指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[安全提议采用的加密算法为]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[DES]{lang="EN-US"}[算法，]{style="font-family:宋体"}[DES]{lang="EN-US"}[算法采用]{style="font-family:宋体"}[56]{lang="EN-US"}[比特的密钥进行加密。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1400223720}

[[算法强度从低到高依次为]{style="font-family:宋体"}**[des-cbc]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960925635}[、]{style="font-family:宋体"}**[3des-cbc]{lang="EN-US"}**[、]{style="font-family:宋体"}**[aes-cbc-128]{lang="EN-US"}**[、]{style="font-family:宋体"}**[aes-cbc-192]{lang="EN-US"}**[、]{style="font-family:宋体"}**[aes-cbc-256]{lang="EN-US"}**[，算法强度越高，安全性越好，计算量越大。请根据实际组网环境中对安全性和性能的要求选择适当强度的算法。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1490130769}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1667126880}[指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[的加密算法为]{style="font-family:宋体"}[128]{lang="EN-US"}[比特的]{style="font-family:宋体"}[CBC]{lang="EN-US"}[模式的]{style="font-family:宋体"}[AES]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x184594575}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\] encryption-algorithm aes-cbc-128]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x849930438}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_808653234}
:::

::: {#-893640877 .myid}
[]{#_Toc404793323}[]{#struct_0_x5828_x5730_70035324}[]{#_Toc339467221}

**IKE \-- IKE配置命令 \-- exchange-mode**

------------------------------------------------------------------------

[**[exchange-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960991171}[命令用来选择]{style="font-family:宋体"}[IKE]{lang="EN-US"}[第一]{style="font-family:宋体"}[阶段的协商模式。]{style="font-family:宋体"}

[**[undo exchange-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_x314927553}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1820571750}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_1978038821}[模式下：]{style="font-family:宋体"}

[**[exchange-mode ]{lang="EN-US"}**[{ **aggressive** \| **main** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1516924879}

[**[undo exchange-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_1516143793}

[[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_669165355}[模式下：]{style="font-family:宋体"}

[**[exchange-mode main]{lang="EN-US"}**]{#struct_0_x5828_x5730_976149547}

[**[undo exchange-mode]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1239566347}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960794563}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1482755119}[第一]{style="font-family:宋体"}[阶段的协商模式为主模式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x377887842}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x876918266}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1242652166}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_179722840}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1161251818}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_815052055}

[**[aggressive]{lang="EN-US"}**]{#struct_0_x5828_x5730_1559248464}[：野蛮模式。]{style="font-family:宋体"}

[**[main]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960860099}[：主模式。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1110498865}

[[当本端的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_1966783960}[地址为自动获取（如本端用户为拨号方式]{style="font-family:宋体"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为动态分配]{style="font-family:宋体"}[），且采用预共享密钥认证方式时，建议将本端的协商模式配置为野蛮模式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_119910722}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x193475289}[配置]{style="font-family:宋体"}[IKE]{lang="EN-US"}[第一]{style="font-family:宋体"}[阶段协商使用主模式]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x936082434}

[\[Sysname\] ike profile 1]{lang="EN-US"}

[\[Sysname-ike-profile-1\] exchange-mode main]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x784741658}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960663491}
:::

::::: {#-568827284 .myid}
[]{#_Toc404793324}[]{#struct_0_x5828_x5730_2015985502}[]{#_Toc339467222}

**IKE \-- IKE配置命令 \-- ike dpd**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 17 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_83383596}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x2054998427}
:::

**[ ]{lang="EN-US"}**

[**[ike dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_x575254136}[命令用来配置全局]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo ike dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_725472327}[命令用来关闭全局]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_608808176}

[**[ike dpd interval ]{lang="EN-US"}***[interval-seconds ]{lang="EN-US"}*[\[ **retry** *seconds* \] { **on-demand** \| **periodic** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1279668602}

[**[undo ike dpd interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_508045591}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960729027}

[[全局]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}]{#struct_0_x5828_x5730_1270149420}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_205331315}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x690701801}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1373785684}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_85456520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1370600534}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_571538434}

[**[interval ]{lang="EN-US"}***[interval-seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x960532419}[：指定触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。对于按需探测模式，指定经过多长时间没有从对端收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文，则触发一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测；对于定时探测模式，指触发一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测的时间间隔。]{style="font-family:宋体"}

[**[retry]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x701822372}[：指定]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文的重传时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[**[on-demand]{lang="EN-US"}**]{#struct_0_x5828_x5730_771950766}[：指定按需探测模式，根据流量来探测对端是否存活，在本端发送]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文时，如果发现当前距离最后一次收到对端报文的时间超过指定的触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔（即通过]{style="font-family:宋体"}*[interval-seconds]{lang="EN-US"}*[指定的时间），则触发]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测。]{style="font-family:宋体"}

[**[periodic]{lang="EN-US"}**]{#struct_0_x5828_x5730_354377648}[：指定定时探测模式，按照触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测的时间间隔（即通过]{style="font-family:宋体"}*[interval-seconds]{lang="EN-US"}*[指定的时间）定时探测对端是否存活。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1025343436}

[[IKE DPD]{lang="EN-US"}]{#struct_0_x5828_x5730_844141015}[有两种模式：按需探测模式和定时探测模式。一般若无特别要求，建议使用按需探测模式，在此模式下，仅在本端需要发送报文时，才会触发探测；如果需要尽快地检测出对端的状态，则可以使用定时探测模式。在定时探测模式下工作，会消耗更多的带宽和计算资源，因此当设备与大量的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[对端通信时，应优先考虑使用按需探测模式。]{style="font-family:宋体"}

[[如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x960597955}[视图下和系统视图下都配置了]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测功能，则]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[视图下的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[配置生效，如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[视图下没有配置]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测功能，则采用系统视图下的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[配置。]{style="font-family:宋体"}

[[建议配置的]{style="font-family:宋体"}**[interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_1644384615}[大于]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[，使得直到当前]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测结束才可以触发下一次]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测，在重传]{style="font-family:宋体"}[DPD]{lang="EN-US"}[报文的过程中不触发新的]{style="font-family:宋体"}[DPD]{lang="EN-US"}[探测。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960401347}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x716335645}[配置流量触发]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[探测间隔时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，重传时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒，探测模式为按需探测。]{style="font-family:宋体"}

[[\<Sysname\> system-view ]{lang="EN-US"}]{#struct_0_x5828_x5730_1657090088}

[\[Sysname\] ike dpd interval 10 retry 5 on-demand]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1335239944}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[dpd]{lang="EN-US"}**]{#struct_0_x5828_x5730_x513391202}
:::::

::: {#-716133889 .myid}
[]{#_Toc404793325}[]{#struct_0_x5828_x5730_x1817616960}[]{#_Toc339467223}

**IKE \-- IKE配置命令 \-- ike identity**

------------------------------------------------------------------------

[**[ike identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960466883}[命令用来配置本端身份信息，用于在]{style="font-family:宋体"}[IKE]{lang="EN-US"}[认证协商阶段向对端标识自己的身份。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ike identity**]{lang="EN-US"}]{#struct_0_x5828_x5730_848157934}[命令用来删除配置的本端身份信息，并恢复为默认身份。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1367973771}

[**[ike identity ]{lang="EN-US"}**[{ **address** { *ipv4-address \|* **ipv6** *ipv6-address* } \| **dn** \| **fqdn** \[ *fqdn-name* \] \| **user-fqdn** \[ *user-fqdn-name* \] }]{lang="EN-US"}]{#struct_0_x5828_x5730_x570118645}

[**[undo ike identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2093654753}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1263175611}

[[使用]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_1947782067}[地址标识本端的身份，该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板应用的接口]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x382379451}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x765062063}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960925634}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1490196305}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1554457258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_510057704}

[**[address]{lang="EN-US"}**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1168150240}[：指定标识本端身份的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其中]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为标识本端身份的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为标识本端身份的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[dn]{lang="EN-US"}**]{#struct_0_x5828_x5730_1294686976}[：使用从数字证书中获得的]{style="font-family:宋体"}[DN]{lang="EN-US"}[名作为本端身份。]{style="font-family:宋体"}

[**[fqdn]{lang="EN-US"}**[ *fqdn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1365787034}[：指定标识本端身份的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[fqdn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{style="font-family:宋体"}[www.test.com]{lang="EN-US"}[。不指定]{style="font-family:宋体"}*[fqdn-name]{lang="EN-US"}*[时，则设备将使用]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置的设备的名称作为本端]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[类型的身份。]{style="font-family:宋体"}

[**[user-fqdn ]{lang="EN-US"}***[user-fqdn-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1479902123}[：指定标识本端身份的]{style="font-family:宋体"}[User FQDN]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[user-fqdn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[User FQDN]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{style="font-family:宋体"}[adc@test.com]{lang="EN-US"}[。不指定]{style="font-family:宋体"}*[user-fqdn-name]{lang="EN-US"}*[时，则设备将使用]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置的设备的名称作为本端]{style="font-family:宋体"}[user FQDN]{lang="EN-US"}[类型的身份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960991170}

[[本命令用于全局配置]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x314862017}[对等体的本端身份，适用于所有]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的协商，而]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[下的]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**[为局部配置身份，仅适用于使用本]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的协商。]{style="font-family:宋体"}

[[如果本端的认证方式为数字签名方式，则本端可以配置任何类型的身份信息；如果本端的认证方式为预共享密钥方式，则只能配置除]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x5828_x5730_x216733206}[之外的其它类型的身份信息。]{style="font-family:宋体"}

[[如果希望在采用数字签名认证时，总是从证书中的主题字段取得本端身份，则可以通过]{style="font-family:宋体"}**[ike signature-identity from-certificate]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2088078097}[命令实现。如果没有配置]{style="font-family:宋体"}**[ike signature-identity from-certificate]{lang="EN-US"}**[，并且]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板下指定的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置了本端身份（由]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**[命令指定），则使用]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置的本端身份；若]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板下未指定]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[或]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[下没有配置本端身份，则使用全局配置的本端身份（由]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**[命令指定）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1965297157}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x183860146}[指定使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[标识本端身份。]{style="font-family:宋体"}

[[\<sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_508183914}

[\[sysname\] ike identity address 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_x960794562}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1482689583}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike signature-identity from-certificate]{lang="EN-US"}**]{#struct_0_x5828_x5730_1832200683}
:::

::: {#-232183604 .myid}
[]{#_Toc404793326}[]{#struct_0_x5828_x5730_856888661}[]{#_Toc339467224}

**IKE \-- IKE配置命令 \-- ike invalid-spi-recovery enable**

------------------------------------------------------------------------

[**[ike invalid-spi-recovery enable]{lang="DA"}**]{#struct_0_x5828_x5730_1834691069}[命令用来使能针对无效]{style="font-family:宋体"}[IPsec SPI]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[恢复功能。]{style="font-family:宋体"}

[**[undo ike invalid-spi-recovery enable]{lang="DA"}**]{#struct_0_x5828_x5730_x1198481352}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_932707925}

[**[ike invalid-spi-recovery enable]{lang="DA"}**]{#struct_0_x5828_x5730_x1186108706}

[**[undo ike invalid-spi-recovery enable]{lang="DA"}**]{#struct_0_x5828_x5730_x960860098}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1110564401}

[[针对无效]{style="font-family:宋体"}[IPsec SPI]{lang="EN-US"}]{#struct_0_x5828_x5730_x1525339433}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[恢复功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1190038147}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x558814797}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x40492887}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1475963238}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x976509585}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1019078901}

[[当]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x960663490}[隧道一端的安全网关出现问题（例如安全网关重启）导致本端]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[丢失时，会造成]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[流量黑洞现象：一端（接收端）的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[已经完全丢失，而另一端（发送端）还持有对应的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[且不断地向对端发送报文，当接收端收到发送端使用此]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[封装的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文时，就会因为找不到对应的]{style="font-family:宋体"}[SA]{lang="EN-US"}[而持续丢弃报文，形成流量黑洞。该现象造成]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[通信链路长时间得不到恢复（只有等到发送端旧的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[生命周期超时，并重建]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[后，两端的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[流量才能得以恢复），因此需要采取有效的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[恢复手段来快速恢复中断的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[通信链路。]{style="font-family:宋体"}

[[SA]{lang="EN-US"}]{#struct_0_x5828_x5730_2015919966}[由]{style="font-family:宋体"}[SPI]{lang="EN-US"}[唯一标识，接收方根据]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[在]{style="font-family:宋体"}[SA]{lang="EN-US"}[数据库中查找对应的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，若接收方找不到处理该报文的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，则认为此报文的]{style="font-family:宋体"}[SPI]{lang="EN-US"}[无效。如果接收端当前存在]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，则会向对端发送删除对应]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的通知消息，发送端]{style="font-family:宋体"}[IKE]{lang="EN-US"}[接收到此通知消息后，就会立即删除此无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}[对应的]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[。之后，当发送端需要继续向接收端发送报文时，就会触发两端重建]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[，使得中断的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[通信链路得以恢复；如果接收端当前不存在]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，就不会触发本端向对端发送删除]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的通知消息，接受端将默认丢弃无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}[的]{style="font-family:宋体"}[IPsec ]{lang="EN-US"}[报文，使得链路无法恢复。后一种情况下，如果使能了]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}[恢复]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[功能，就会触发本端与对端协商新的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[并发送删除消息给对端，从而使链路恢复正常。]{style="font-family:宋体"}

[[由于使能此功能后，若攻击者伪造大量源]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_130230162}[地址不同但目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址相同的无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}[报文发给设备，会导致设备因忙于与无效对端协商建立]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[而面临受到]{style="font-family:宋体"}[DoS]{lang="EN-US"}[（]{style="font-family:宋体"}[Denial of Sevice]{lang="EN-US"}[）攻击的风险，通常情况下，建议关闭针对无效]{style="font-family:宋体"}[IPsec SPI]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[恢复功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1713215658}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1145529148}[使能]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[无效]{style="font-family:宋体"}[SPI]{lang="EN-US"}[恢复]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x5828_x5730_749952162}

[\[Sysname\] ike invalid-spi-recovery enable]{lang="NO-BOK"}
:::

::::: {#-2140596052 .myid}
[]{#_Toc404793327}[]{#struct_0_x5828_x5730_2093992427}[]{#_Toc339467225}

**IKE \-- IKE配置命令 \-- ike keepalive interval**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_x347971157}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x960729026}
:::

[ ]{lang="EN-US"}

[**[ike keepalive interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_1270083884}[命令用来配置通过]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[向对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的时间间隔。]{style="font-family:宋体"}

[**[undo ike  keepalive interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_951298458}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_115209849}

[**[ike keepalive interval]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_x5828_x5730_x179189280}

[**[undo ike keepalive interval]{lang="SV"}**]{#struct_0_x5828_x5730_x832903039}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x326215790}

[[不向对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}]{#struct_0_x5828_x5730_x789339428}[报文。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960532418}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x701756836}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x779298121}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1225040638}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_59847192}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x153995525}

[*[seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1321096219}[：指定向对端发送]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[28800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1735460215}

[[当有检测对方]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_2047673400}[和]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[是否存活的需求时，通常建议配置]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[，不建议配置]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[功能。仅当对方不支持]{style="font-family:宋体"}[IKE DPD]{lang="EN-US"}[特性，但支持]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[功能时，才考虑配置]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[本端配置的]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}]{#struct_0_x5828_x5730_x960597954}[报文的等待超时时间要大于对端发送的时间间隔。由于网络中一般不会出现超过三次的报文丢失，所以，本端的超时时间可以配置为对端配置的发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的时间间隔的三倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1644450151}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1342587726}[配置本端向对端发送]{style="font-family:宋体"}[Keepalive]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[200]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x14943190}

[\[Sysname\] ike keepalive interval 200]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1510832663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike keepalive timeout]{lang="EN-US"}**]{#struct_0_x5828_x5730_1740600498}
:::::

::::: {#-1846649750 .myid}
[]{#_Toc404793328}[]{#struct_0_x5828_x5730_1782727580}[]{#_Toc339467226}

**IKE \-- IKE配置命令 \-- ike keepalive timeout**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_x960401346}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x716401181}
:::

[ ]{lang="EN-US"}

[**[ike keepalive timeout]{lang="EN-US"}**]{#struct_0_x5828_x5730_533683721}[命令用来配置本端等待对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的超时时间。超过该时间之后，本端的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[将会被删除。]{style="font-family:宋体"}

[**[undo ike keepalive timeout]{lang="EN-US"}**]{#struct_0_x5828_x5730_1702995165}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2101319217}

[**[ike keepalive timeout]{lang="EN-US"}***[ seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x193960035}

[**[undo ike keepalive timeout]{lang="NO-BOK"}**]{#struct_0_x5828_x5730_x144234871}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x346407367}

[[永不超时。无论是否收到对端的]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}]{#struct_0_x5828_x5730_1302645325}[报文，本端]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[仅按照协商出来的老化时间进行老化。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960466882}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_848092398}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x203743873}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_391740649}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1262164396}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1387047513}

[*[seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1193544727}[：指定本端等待对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的超时时间，取值范围为]{style="font-family:宋体"}[20]{lang="EN-US"}[～]{style="font-family:宋体"}[28800]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1642453871}

[[本端配置的等待对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}]{#struct_0_x5828_x5730_x960925637}[报文的超时时间要大于对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的时间间隔。由于网络中一般不会出现超过三次的报文丢失，所以，本端的超时时间可以配置为对端配置的发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的时间间隔的三倍。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1489999697}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x14355102}[配置本端等待对端发送]{style="font-family:宋体"}[IKE Keepalive]{lang="EN-US"}[报文的超时时间为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x1848146488}

[\[Sysname\] ike keepalive timeout 20]{lang="NO-BOK"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_869355295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike keepalive interval]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1086814025}
:::::

::: {#-731670520 .myid}
[]{#_Toc404793329}[]{#struct_0_x5828_x5730_x2043580481}[]{#_Toc339467227}

**IKE \-- IKE配置命令 \-- ike keychain**

------------------------------------------------------------------------

[**[ike keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_606300531}[命令用来创建并进入一个]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[视图，该视图用于配置]{style="font-family:宋体"}[IKE]{lang="EN-US"}[对等体的密钥信息。]{style="font-family:宋体"}

[**[undo ike keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960991173}[命令用来删除指定的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[以及]{style="font-family:宋体"}[IKE]{lang="EN-US"}[对等体的密钥信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x314796481}

[**[ike keychain]{lang="EN-US"}**[ *keychain-name* \[ **vpn-instance** *vpn-name* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x1447576578}

[**[undo]{lang="EN-US"}**[ **ike keychain** *keychain-name* \[ **vpn-instance** *vpn-name* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x2007015472}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1633936439}

[[不存在]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_703474366}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x183799963}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1331827918}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1734129217}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x960794565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1482624047}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_354188074}

[*[keychain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_732183015}[：]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1550392165}[：]{style="font-family:宋体;color:black"}[指定]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[如果不指定该参数，则表示]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_852573183}

[[在]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1195098623}[需要通过预共享密钥方式进行认证时，需要创建并指定]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_894743511}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1167130837}[创建]{style="font-family:宋体"}[IKE keychain key1]{lang="EN-US"}[并进入]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x960860101}

[\[Sysname\] ike keychain key1]{lang="EN-US"}

[\[Sysname-ike-keychain-key1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1227629000}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_x588690159}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[pre-shared-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_936461616}
:::

::::: {#474910538 .myid}
[]{#_Toc404793330}[]{#struct_0_x5828_x5730_317402318}[]{#_Toc339467228}[]{#_Toc335756534}

**IKE \-- IKE配置命令 \-- ike limit**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_1011065128}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x1211866376}
:::

[ ]{lang="EN-US"}

[**[ike limit]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960663493}[命令用来配置对本端]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[数目的限制。]{style="font-family:宋体"}

[**[undo ike limit]{lang="EN-US"}**]{#struct_0_x5828_x5730_2016116574}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1530716530}

[**[ike limit]{lang="EN-US"}**[ { **max-negotiating-sa** *negotiation-limit* \| **max-sa** *sa-limit* }]{lang="EN-US"}]{#struct_0_x5828_x5730_385756032}

[**[undo ike limit ]{lang="EN-US"}**[{ **max-negotiating-sa** \| **max-sa** }]{lang="EN-US"}]{#struct_0_x5828_x5730_x454157066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1471888957}

[[不限制]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x903706663}[数目。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1957897543}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_694990691}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960729029}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1270804780}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1008925069}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2092908706}

[**[max-negotiating-sa]{lang="EN-US"}**[ *negotiation-limit*]{lang="EN-US"}]{#struct_0_x5828_x5730_832484532}[：指定允许同时处于协商状态的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[和]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的最大总和数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[max-sa]{lang="EN-US"}**[ *sa-limit*]{lang="EN-US"}]{#struct_0_x5828_x5730_1720381598}[：指定允许建立的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的最大数，取值范围与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1441093484}

[[可以通过]{style="font-family:宋体"}**[max-negotiating-sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_1272473879}[参数设置允许同时协商更多的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，以充分利用设备处理能力，以便在设备有较强处理能力的情况下得到更高的新建性能；可以通过该参数设置允许同时协商更少的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，以避免产生大量不能完成协商的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，以便在设备处理能力较弱时保证一定的新建性能。]{style="font-family:宋体"}

[[可以通过]{style="font-family:宋体"}**[max-sa]{lang="EN-US"}**]{#struct_0_x5828_x5730_x960532421}[参数设置允许建立更多的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，以便在设备有充足内存的情况下得到更高的并发性能；可以通过该参数设置允许建立更少的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，以便在设备没有充足的内存的情况下，使]{style="font-family:宋体"}[IKE]{lang="EN-US"}[不过多占用系统内存。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x702346663}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x143664560}[配置本端允许同时处于协商状态的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[和]{style="font-family:宋体"}[IPsec SA]{lang="EN-US"}[的最大总和数为]{style="font-family:宋体"}[200]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_122961702}

[\[Sysname\] ike limit max-negotiating-sa 200]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1514946815}[配置本端允许成功建立的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[的最大数为]{style="font-family:宋体"}[5000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x439073051}

[\[Sysname\] ike limit max-sa 5000]{lang="EN-US"}
:::::

::::: {#1921277857 .myid}
[]{#_Toc404793331}[]{#struct_0_x5828_x5730_812406341}[]{#_Toc339467229}

**IKE \-- IKE配置命令 \-- ike nat-keepalive**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](IPsec命令.files/image001.png){#图片 11 width="62" height="25"}]{lang="EN-US"}]{#struct_0_x5828_x5730_x960597957}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_x5828_x5730_x960401349}
:::

[ ]{lang="EN-US"}

[**[ike nat-keepalive]{lang="DA"}**]{#struct_0_x5828_x5730_x715942429}[命令用来配置向对端发送]{style="font-family:宋体"}[NAT Keepalive]{lang="DA"}[报文的时间间隔]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo ike nat-keepalive]{lang="DA"}**]{#struct_0_x5828_x5730_1033890253}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1126503446}

[**[ike nat-keepalive ]{lang="DA"}**]{#struct_0_x5828_x5730_127308042}*[seconds]{lang="DA"}*

[**[undo ike nat-keepalive]{lang="DA"}**]{#struct_0_x5828_x5730_1564816649}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1782247831}

[[向对端发送]{style="font-family:宋体"}[NAT Keepalive]{lang="EN-US"}]{#struct_0_x5828_x5730_x960466885}[报文的时间间隔为]{style="font-family:宋体"}[20]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_848289006}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1972802053}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1627725112}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1599810132}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1487654139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x991213159}

[*[seconds]{lang="DA"}*]{#struct_0_x5828_x5730_x1845442643}[：]{style="font-family:宋体"}[指定向对端发送]{style="font-family:宋体"}[NAT Keepalive]{lang="DA"}[报文的时间间隔]{style="font-family:宋体"}[，]{style="font-family:宋体"}[取值范围为]{style="font-family:宋体"}[5]{lang="DA"}[～]{style="font-family:宋体"}[300]{lang="DA"}[，]{style="font-family:宋体"}[单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960925636}

[[该命令仅对位于]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x5828_x5730_x1490065233}[之后的设备（即该设备位于]{style="font-family:宋体"}[NAT]{lang="EN-US"}[设备连接的私网侧）有意义。]{style="font-family:宋体"}[NAT]{lang="EN-US"}[之后的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[网关设备需要定时向]{style="font-family:宋体"}[NAT]{lang="EN-US"}[之外的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[网关设备发送]{style="font-family:宋体"}[NAT Keepalive]{lang="EN-US"}[报文，以便维持]{style="font-family:宋体"}[NAT]{lang="EN-US"}[设备上对应的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[流量的会话存活，从而让]{style="font-family:宋体"}[NAT]{lang="EN-US"}[之外的设备可以访问]{style="font-family:宋体"}[NAT]{lang="EN-US"}[之后的设备。]{style="font-family:宋体"}

[[因此，需要确保该命令配置的时间小于]{style="font-family:宋体"}[NAT]{lang="EN-US"}]{#struct_0_x5828_x5730_x810209942}[设备上会话表项的存活时间。关于如何查看]{style="font-family:宋体"}[NAT]{lang="EN-US"}[表项的存活时间，请参见"三层技术]{style="font-family:宋体"}[-IP]{lang="EN-US"}[业务命令参考"中的"]{style="font-family:宋体"}[NAT]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x309525964}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1233074252}[配置向对端发送]{style="font-family:宋体"}[NAT Keepalive]{lang="EN-US"}[报文的时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="NO-BOK"}]{#struct_0_x5828_x5730_x1328921934}

[\[Sysname\] ike nat-keepalive 5]{lang="NO-BOK"}
:::::

::: {#508251046 .myid}
[]{#_Toc404793332}[]{#struct_0_x5828_x5730_1105893585}[]{#_Toc339467230}

**IKE \-- IKE配置命令 \-- ike profile**

------------------------------------------------------------------------

[**[ike profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_532983375}[命令用来创建一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ike profile**]{lang="EN-US"}]{#struct_0_x5828_x5730_x960991172}[命令用来删除指定的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x5828_x5730_x314730945}

[**[ike profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1739838140}

[**[undo ike profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_30521582}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_797555179}

[[不存在]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1883547212}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1531259743}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1794389894}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x960794564}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1482558511}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_2083733186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2013202897}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x72269719}[：]{lang="EN-US" style="font-family:宋体"}[IKE profile]{lang="EN-US"}[名称，为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1576235769}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x452061174}[创建]{style="font-family:宋体"}[IKE profile 1]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x209486585}

[\[Sysname\] ike profile 1]{lang="EN-US"}

[\[Sysname-ike-profile-1\]]{lang="EN-US"}
:::

::: {#55844376 .myid}
[]{#_Toc404793333}[]{#struct_0_x5828_x5730_x960860100}[]{#_Toc339467231}

**IKE \-- IKE配置命令 \-- ike proposal**

------------------------------------------------------------------------

[**[ike]{lang="EN-US"}**[ **proposal**]{lang="EN-US"}]{#struct_0_x5828_x5730_1227563464}[命令用来创建]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议，并进入]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议视图。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ike** **proposal**]{lang="EN-US"}]{#struct_0_x5828_x5730_x555708152}[命令用来删除一个]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x964388986}

[**[ike]{lang="EN-US"}**[ **proposal** *proposal-number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x100697069}

[**[undo]{lang="EN-US"}**[ **ike** **proposal** *proposal-number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1181724809}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1700286432}

[[系统提供一条缺省的]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_619674566}[提议，此缺省的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议具有最低的优先级。缺省的提议的参数不可修改，其参数包括：]{style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[加密算法：非]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_x5828_x5730_343250928}[模式下使用]{lang="EN-US" style="font-family:宋体"}[DES-CBC]{lang="EN-US"}[，]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下使用]{style="font-family:宋体"}[AES-CBC-128]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[认证算法：]{lang="EN-US" style="font-family:宋体"}[HMAC-SHA1]{lang="EN-US"}]{#struct_0_x5828_x5730_x960663492}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[认证方法：预共享密钥]{lang="EN-US" style="font-family:宋体"}]{#struct_0_x5828_x5730_2016051038}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[DH]{lang="EN-US"}]{#struct_0_x5828_x5730_x1178237940}[密钥交换参数：非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式使用]{style="font-family:宋体"}[group1]{lang="EN-US"}[，]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下使用]{style="font-family:宋体"}[group14]{lang="EN-US"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x1103484125}[存活时间]{lang="EN-US" style="font-family:宋体"}[：]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x499152683}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x620610460}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2022702693}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1907813754}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x960729028}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1270739244}

[*[proposal-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_598350647}[：]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。该序号同时表示优先级，数值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_981880844}

[[在进行]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x2044868463}[协商的时候，协商发起方会将自己的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议发送给对端，由对端进行匹配。若发起方使用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略中没有引用]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，则会将当前系统中所有的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议发送给对端；否则，发起方会将引用的]{style="font-family:宋体"}[IKE profle]{lang="EN-US"}[中的所有]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议发送给对端。]{style="font-family:宋体"}

[[响应方则以对端发送的]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1354846396}[提议优先级从高到低的顺序与本端所有的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议进行匹配，一旦找到匹配项则停止匹配并使用匹配的提议，否则继续查找其它的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议。如果本端配置中没有和对端匹配的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议，则使用系统缺省的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议进行匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1146656658}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1992048971}[创建]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x960532420}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_x702281127}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x125868712}
:::

::: {#398195372 .myid}
[]{#_Toc404793334}[]{#struct_0_x5828_x5730_x557603149}[]{#_Toc339467232}

**IKE \-- IKE配置命令 \-- ike signature-identity from-certificate**

------------------------------------------------------------------------

[**[ike signature-identity from-certificate]{lang="EN-US"}**]{#struct_0_x5828_x5730_x648833795}[命令用来配置当使用数字签名认证方式时，本端的身份总是从本端证书的主题字段中获得，不论]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**[或]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**[如何配置。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **ike signature-identity from-certificate**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1671520961}[命令用来恢复缺省的情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x853163177}

[**[ike signature-identity from-certificate]{lang="EN-US"}**]{#struct_0_x5828_x5730_x205351888}

[**[undo]{lang="EN-US"}**[ **ike signature-identity from-certificate**]{lang="EN-US"}]{#struct_0_x5828_x5730_x960597956}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1644581223}

[[当使用数字签名认证方式时，本端身份信息由]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_1320269775}[或]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**[命令指定。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1193849450}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1580910269}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1125283408}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_626627059}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1928776178}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x478977348}

[[在采用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x960401348}[野蛮协商模式以及数字签名认证方式的情况下，与仅支持使用]{style="font-family:宋体"}[DN]{lang="EN-US"}[类型身份进行数字签名认证的]{style="font-family:宋体"}[ComwareV5]{lang="EN-US"}[设备互通时需要配置本命令。]{style="font-family:宋体"}

[[如果没有配置]{style="font-family:宋体"}**[ike signature-identity from-certificate]{lang="EN-US"}**]{#struct_0_x5828_x5730_x716007965}[，并且]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板下指定的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置了本端身份（由]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**[命令指定），则使用]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置的本端身份；若]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板下未指定]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[或]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[下没有配置本端身份，则使用全局配置的本端身份（由]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**[命令指定）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_166872657}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_349376261}[在采用数字签名认证时，指定总从本端证书中的主题字段取得本端身份。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x995203303}

[\[sysname\] ike signature-identity from-certificate]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_x930101326}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x10588813}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[ike identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1438542145}
:::

::: {#1465430336 .myid}
[]{#_Toc404793335}[]{#struct_0_x5828_x5730_x960466884}[]{#_Toc339467233}

**IKE \-- IKE配置命令 \-- inside-vpn**

------------------------------------------------------------------------

[**[inside-vpn]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x5828_x5730_848223470}[命令用来指定内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **inside-vpn** ]{lang="EN-US"}]{#struct_0_x5828_x5730_1972724649}[命令用来取消指定的内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1881798890}

[**[inside-vpn]{lang="EN-US"}**[ **vpn-instance** *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1657029101}

[**[undo inside-vpn]{lang="EN-US"}**]{#struct_0_x5828_x5730_120177669}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_870976696}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1339369119}[未指定内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，设备在收到]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[报文的接口所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中查找路由。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605158308}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1360701678}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x163592179}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1749480866}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x2029213009}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1034348326}

[**[vpn-instance]{lang="EN-US"}***[ vpn-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x979715560}[：保护的数据属于指定的]{style="font-family:宋体;color:black"}[VPN]{lang="EN-US" style="color:black"}[。]{style="font-family:宋体;color:black"}*[vpn-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1121951631}

[[当]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x513118021}[解封装后得到的报文需要继续转发到不同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中去时，设备需要知道在哪个]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例中查找相应的路由。缺省情况下，设备在与外网相同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中查找路由。如果不希望在与外网相同的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中查找路由去转发解封装后的报文，则可以通过此命令指定一个内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例，指定设备通过查找该内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中的路由来转发解封装后的报文。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605092772}

[[\# ]{lang="DA"}]{#struct_0_x5828_x5730_x544286732}[在]{style="font-family:宋体"}[IKE profile prof1]{lang="DA"}[中]{style="font-family:宋体"}[指定内部]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x1860938488}

[\[Sysname\] ike profile prof1]{lang="EN-US"}

[\[Sysname-ike-profile-prof1\] inside-vpn vpn-instance vpn1]{lang="EN-US"}
:::

::: {#107661051 .myid}
[]{#_Toc404793336}[]{#struct_0_x5828_x5730_x558842533}[]{#_Toc339467234}

**IKE \-- IKE配置命令 \-- keychain**

------------------------------------------------------------------------

[**[keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_1519782361}[命令用来指定采用预共享密钥认证时使用的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **keychain**]{lang="EN-US"}]{#struct_0_x5828_x5730_x693953657}[命令用取消指定的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_433768627}

[**[keychain ]{lang="EN-US"}***[keychain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_605289380}

[**[undo keychain ]{lang="EN-US"}***[keychain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x682710333}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_272254217}

[[未指定]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_x2003300166}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1474579203}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x1520458736}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1948571990}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1416251433}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1049274759}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605223844}

[*[keychain-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_47885350}[：指定配置的]{lang="EN-US" style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[名称，为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x547246564}

[[一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1989104899}[中最多可以指定六个]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[，先配置的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x254522952}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_237373753}[在]{style="font-family:宋体"}[IKE profile 1]{lang="EN-US"}[中指定名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的配置的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_x213291153}

[\[Sysname\] ike profile 1]{lang="EN-US"}

[\[Sysname-ike-profile-1\] keychain abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605420452}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_1503999196}
:::

::: {#839288832 .myid}
[]{#_Toc404793337}[]{#struct_0_x5828_x5730_735853628}[]{#_Toc339467235}

**IKE \-- IKE配置命令 \-- local-identity**

------------------------------------------------------------------------

[**[local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_1657360206}[命令用来配置本端身份信息，用于在]{style="font-family:宋体"}[IKE]{lang="EN-US"}[认证协商阶段向对端标识自己的身份。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **local-identity**]{lang="EN-US"}]{#struct_0_x5828_x5730_983770419}[命令用来删除配置的本端身份信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x2102108065}

[**[local-identity ]{lang="EN-US"}**[{ **address** { *ipv4-address \|* **ipv6** *ipv6-address* } \| **dn** \| **fqdn** \[ *fqdn-name* \] \| **user-fqdn** \[ *user-fqdn-name* \] }]{lang="EN-US"}]{#struct_0_x5828_x5730_1239632059}

[**[undo local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_x611451382}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_730553865}

[[未配置本端身份信息。此时使用系统视图下通过]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_605354916}[命令配置的身份信息作为本端身份信息。若两者都没有配置，则使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址标识本端的身份，该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略或]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略模板应用的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_817510142}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x946021866}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1182631171}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1457722428}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1137867755}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1232619963}

[**[address]{lang="EN-US"}**[ { *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1547028182}[：指定标识本端身份的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，其中]{style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为标识本端身份的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为标识本端身份的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[dn]{lang="EN-US"}**]{#struct_0_x5828_x5730_605551524}[：使用从本端数字证书中获得的]{style="font-family:宋体"}[DN]{lang="EN-US"}[名作为本端身份。]{style="font-family:宋体"}

[**[fqdn]{lang="EN-US"}**[ *fqdn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1135263676}[：指定标识本端身份的]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[fqdn-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{style="font-family:宋体"}[www.test.com]{lang="EN-US"}[。不指定]{style="font-family:宋体"}*[fqdn-name]{lang="EN-US"}*[时，则设备将使用]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置的设备的名称作为本端]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[类型的身份。]{style="font-family:宋体"}

[**[user-fqdn ]{lang="EN-US"}***[user-fqdn-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_1162971641}[：指定标识本端身份的]{style="font-family:宋体"}[user FQDN]{lang="EN-US"}[名称，]{style="font-family:宋体"}*[user-fqdn-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{style="font-family:宋体"}[adc@test.com]{lang="EN-US"}[。不指定]{style="font-family:宋体"}*[user-fqdn-name]{lang="EN-US"}*[时，则设备将使用]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置的设备的名称作为本端]{style="font-family:宋体"}[user FQDN]{lang="EN-US"}[类型的身份。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1001375556}

[[如果本端的认证方式为数字签名方式，则本端可以配置任何类型的身份信息；如果本端的认证方式为预共享密钥方式，则只能配置除]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_x5828_x5730_x2120652015}[之外的其它类型的身份信息。]{style="font-family:宋体"}

[[如果本端的认证方式为数字签名方式，且配置的本端身份为]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_x5828_x5730_1764836044}[地址，但这个]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址与本端证书中的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址不同，则设备将使用]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[类型的本端身份标识，该标识为使用]{style="font-family:宋体"}**[sysname]{lang="EN-US"}**[命令配置的设备名称。]{style="font-family:宋体"}

[[响应方使用发起方的身份信息查找本地的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1983123049}[，通过与]{style="font-family:宋体"}**[match remote]{lang="EN-US"}**[命令中指定的发起方身份信息进行匹配，可查找到本端要采用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_622265020}[中只能配置一条本端身份信息。]{style="font-family:宋体"}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_605485988}[下的本端身份信息优先级高于系统视图下通过]{style="font-family:宋体"}**[ike identity]{lang="EN-US"}**[命令配置的本端身份信息。如果]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[下未配置本端身份信息，则使用系统视图下配置的本端身份信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1112750281}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x583432226}[指定使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[标识本端身份。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1017732021}

[\[Sysname\] ike profile prof1]{lang="EN-US"}

[\[Sysname-ike-profile-prof1\] local-identity address 2.2.2.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_1176771472}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[match remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1469923310}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol;border:none"}]{.TerminalDisplayshading}**[ike identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_605682596}
:::

::: {#1952176894 .myid}
[]{#_Toc404793338}[]{#struct_0_x5828_x5730_1039516043}[]{#_Toc339467236}

**IKE \-- IKE配置命令 \-- match local address (IKE keychain view)**

------------------------------------------------------------------------

[**[match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_1496984382}[命令用来限制]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的使用范围，即]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[只能用于指定地址或指定接口的地址上的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[**[undo match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_263531002}[命令用来取消对]{style="font-family:
宋体"}[IKE keychain]{lang="EN-US"}[使用范围的限制。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1366558712}

[**[match local address ]{lang="EN-US"}**[{ *interface-type interface-number* \| { *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-name* \] }]{lang="EN-US"}]{#struct_0_x5828_x5730_x2104971694}

[**[undo match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2423933}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1257456139}

[[未限制]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_x1989189356}[的使用范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605617060}

[[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_2130249515}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x541116266}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_361059622}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1092478523}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_488223571}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1193847225}[：]{style="font-family:宋体;color:black"}[本端接口名称。可以是任意的三层接口。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x2097492926}[：本端接口的]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;
color:black"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x5828_x5730_605158309}[：本端接口的]{style="font-family:宋体;color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1360701677}[：]{style="font-family:宋体;color:black"}[指定接口地址]{style="font-family:宋体"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[如果不指定该参数，则表示接口地址属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x162609139}

[[此命令用于限制]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_x918556346}[只能用于指定地址或指定接口的地址上的协商，这里的地址指的是]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板下配置的本端地址（通过命令]{style="font-family:宋体"}**[local-address]{lang="EN-US"}**[配置），若本端地址没有配置，则为引用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1265089464}[中最多可以指定六个]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[，先配置的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[优先级高。若希望本端在匹配某些]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的时候，不按照配置的优先级来查找，则可以通过本命令来指定这类]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的使用范围。例如，]{style="font-family:宋体"}[IKE keychain A]{lang="EN-US"}[中的预共享密钥的匹配地址范围大（]{style="font-family:宋体"}[2.2.0.0/16]{lang="EN-US"}[），]{style="font-family:宋体"}[IKE keychain B]{lang="EN-US"}[中的预共享密钥的匹配地址范围小（]{style="font-family:宋体"}[2.2.2.0/24]{lang="EN-US"}[），]{style="font-family:宋体"}[IKE keychain A]{lang="EN-US"}[先于]{style="font-family:宋体"}[IKE keychain B]{lang="EN-US"}[配置。若希望本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用]{style="font-family:宋体"}[IKE keychain B]{lang="EN-US"}[，但是按照配置顺序匹配，依据本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[总会匹配到预共享密钥地址范围大的]{style="font-family:宋体"}[IKE keychain A]{lang="EN-US"}[，而找不到期望的]{style="font-family:宋体"}[IKE keychain B]{lang="EN-US"}[。这中情况下，可以通过配置]{style="font-family:宋体"}[IKE keychainB]{lang="EN-US"}[在指定地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用，使其找到正确的预共享密钥。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1390271595}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_729578691}[创建]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[，名称为]{style="font-family:宋体"}[key1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1763911577}

[\[Sysname\] ike keychain key1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_605092773}[限制]{style="font-family:宋体"}[IKE keychain key1]{lang="EN-US"}[只能在名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用。]{style="font-family:宋体"}

[[\[sysname-ike-keychain-key1\] match local address 2.2.2.2 vpn-instance vpn1]{lang="EN-US"}]{#struct_0_x5828_x5730_x544286733}
:::

::: {#-778768563 .myid}
[]{#_Toc404793339}[]{#struct_0_x5828_x5730_x1860872952}[]{#_Toc339467237}

**IKE \-- IKE配置命令 \-- match local address (IKE profile view)**

------------------------------------------------------------------------

[**[match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_1932842992}[命令用来限制]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的使用范围，即]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[只能用于指定地址或指定接口的地址上的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[**[undo match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1299907248}[命令用来取消对]{style="font-family:
宋体"}[IKE profile]{lang="EN-US"}[使用范围的限制。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1268559228}

[**[match local address ]{lang="EN-US"}**[{ *interface-type interface-number* \| { *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-name* \] }]{lang="EN-US"}]{#struct_0_x5828_x5730_x1676487151}

[**[undo match]{lang="EN-US"}**[ **local address**]{lang="EN-US"}]{#struct_0_x5828_x5730_1501983828}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x244077015}

[[未限制]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_605289381}[的使用范围。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x682710332}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_272188681}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_935214271}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_908155333}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1902043045}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1268906183}

[*[interface-type interface-number]{lang="EN-US"}*]{#struct_0_x5828_x5730_1398410831}[：]{style="font-family:宋体;color:black"}[本端接口名称。可以是任意三层接口。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_605223845}[：本端接口]{style="font-family:宋体;color:black"}[IPv4]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;
color:black"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_x5828_x5730_47885351}[：本端接口]{style="font-family:宋体;
color:black"}[IPv6]{lang="EN-US" style="color:black"}[地址。]{style="font-family:宋体;color:black"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1791405596}[：]{style="font-family:宋体;color:black"}[指定接口地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，则表示接口地址属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x47991294}

[[此命令用于限制]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x2130973674}[只能用于指定地址或指定接口的地址上的协商，这里的地址指的是]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略]{style="font-family:宋体"}[/IPsec]{lang="EN-US"}[安全策略模板下配置的本端地址（通过命令]{style="font-family:宋体"}**[local-address]{lang="EN-US"}**[配置），若本端地址没有配置，则为引用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略的接口的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[先配置的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_881984151}[优先级高，若希望本端在匹配某些]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的时候，不按照配置的优先级来查找，则可以通过本命令来指定这类]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的使用范围。例如，]{style="font-family:宋体"}[IKE profile A]{lang="EN-US"}[中的]{style="font-family:宋体"}[match remote]{lang="EN-US"}[地址范围大（]{style="font-family:宋体"}[match remote identity address range 2.2.2.1 2.2.2.100]{lang="EN-US"}[），]{style="font-family:
宋体"}[IKE profile B]{lang="EN-US"}[中的]{style="font-family:
宋体"}[match remote]{lang="EN-US"}[地址范围小（]{style="font-family:宋体"}[match remote identity address range 2.2.2.1 2.2.2.10]{lang="EN-US"}[），]{style="font-family:宋体"}[IKE profile A]{lang="EN-US"}[先于]{style="font-family:宋体"}[IKE profile B]{lang="EN-US"}[配置。若希望本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用]{style="font-family:宋体"}[IKE profile B]{lang="EN-US"}[，但是按照配置顺序匹配，依据本端]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[总会匹配到预共享密钥地址范围大的]{style="font-family:宋体"}[IKE profile A]{lang="EN-US"}[，而找不到期望的]{style="font-family:宋体"}[IKE profile B]{lang="EN-US"}[。这种情况下，可以通过配置]{style="font-family:宋体"}[IKE profile B]{lang="EN-US"}[在指定地址]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用，使其找到正确的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1896655644}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1058256440}[创建]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，名称为]{style="font-family:宋体"}[prof1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_605420453}

[\[Sysname\] ike profile prof1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1503999197}[限制]{style="font-family:宋体"}[IKE profile prof1 ]{lang="EN-US"}[只能在名称为]{style="font-family:宋体"}[vpn1]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[2.2.2.2]{lang="EN-US"}[的接口上使用。]{style="font-family:宋体"}

[[\[sysname-ike-profile-prof1\] match local address 2.2.2.2 vpn-instance vpn1]{lang="EN-US"}]{#struct_0_x5828_x5730_735788092}
:::

::: {#-663666364 .myid}
[]{#_Toc404793340}[]{#struct_0_x5828_x5730_598936721}[]{#_Toc339467238}

**IKE \-- IKE配置命令 \-- match remote**

------------------------------------------------------------------------

[**[match remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_162776163}[命令用来配置一条用于匹配对端身份的规则。]{style="font-family:宋体"}

[**[undo match remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_1923065878}[命令用来删除一条用于匹配对端身份的规则。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x620177900}

[**[match remote ]{lang="EN-US"}**[{ **certificate** *policy-name* \| **identity** { **address** { { *ipv4-address* \[ *mask \| mask-length* \] \| **range** *low-ipv4-address high-ipv4-address* } \| **ipv6** { *ipv6-address* \[ *prefix-length* \] \| **range** *low-ipv6-address high-ipv6-address* } } \[ **vpn-instance** *vpn-name* \] \| **fqdn** *fqdn-name* \| **user-fqdn** *user-fqdn-name* } }]{lang="EN-US"}]{#struct_0_x5828_x5730_1130335289}

[**[undo]{lang="EN-US"}**[ **match remote** { **certificate** *policy-name* \| **identity** { **address** { { *ipv4-address* \[ *mask \| mask-length* \] \| **range** *low-ipv4-address high-ipv4-address* } \| **ipv6** { *ipv6-address* \[ *prefix-length* \] \| **range** *low-ipv6-address high-ipv6-address* } } \[ **vpn-instance** *vpn-name* \] \| **fqdn** *fqdn-name* \| **user-fqdn** *user-fqdn-name* } }]{lang="EN-US"}]{#struct_0_x5828_x5730_605354917}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_817510141}

[[未配置任何用于匹配对端身份的规则。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x946021869}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1183352067}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1672777309}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1052869716}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1252139491}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1182274732}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_788327434}

[**[certificate ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_605551525}[：基于对端数字证书中的信息匹配]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[policy-name]{lang="EN-US"}*[是证书访问控制策略的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串。本参数用于响应方根据收到的发起方证书中的]{style="font-family:宋体"}[DN]{lang="EN-US"}[字段来过滤使用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_1135263675}[：基于指定的对端身份信息匹配]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。本参数用于响应方根据发起方通过]{style="font-family:宋体"}**[local-identity]{lang="EN-US"}**[命令配置的身份信息来选择使用的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address]{lang="EN-US"}**[ *ipv4-address* \[ *mask* \| *mask-length* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_1162906105}[：对端]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址或]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[网段。其中，]{lang="EN-US" style="font-family:宋体"}*[ipv4-address]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}*[mask]{lang="EN-US"}*[为子网掩码，]{lang="EN-US" style="font-family:宋体"}*[mask-length]{lang="EN-US"}*[为子网掩码长度，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[32]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address range ]{lang="EN-US"}***[low-ipv4-address high-ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_197987911}[：对端]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址范围。其中]{lang="EN-US" style="font-family:宋体"}*[low-ipv4-address]{lang="EN-US"}*[为起始]{lang="EN-US" style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}*[high-ipv4-address]{lang="EN-US"}*[为结束]{lang="EN-US" style="font-family:
宋体"}[IPv4]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:
宋体"}[结束地址必须大于起始地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address]{lang="EN-US"}**[ **ipv6** *ipv6-address* \[ *prefix-length* \] ]{lang="EN-US"}]{#struct_0_x5828_x5730_1250499211}[：对端]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址或]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[网段。其中，]{lang="EN-US" style="font-family:宋体"}*[ipv6-address]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}*[prefix-length]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀，取值范围为]{lang="EN-US" style="font-family:宋体"}[0]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[address]{lang="EN-US"}**[ **ipv6 range** *low-ipv6-address high-ipv6-address*]{lang="EN-US"}]{#struct_0_x5828_x5730_1571837129}[：对端]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址范围。其中]{lang="EN-US" style="font-family:宋体"}*[low-ipv6-address]{lang="EN-US"}*[为起始]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，]{lang="EN-US" style="font-family:宋体"}*[high-ipv6-address]{lang="EN-US"}*[为结束]{lang="EN-US" style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{lang="EN-US" style="font-family:宋体"}[结束地址必须大于起始地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[fqdn]{lang="EN-US"}**[ *fqdn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_x1380418809}[：对端]{lang="EN-US" style="font-family:宋体"}[FQDN]{lang="EN-US"}[名称，为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{lang="EN-US" style="font-family:宋体"}[www.test.com]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-fqdn]{lang="EN-US"}**[ *user-fqdn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_1809122298}[：对端]{lang="EN-US" style="font-family:宋体"}[User FQDN]{lang="EN-US"}[名称，为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写，例如]{lang="EN-US" style="font-family:宋体"}[abc@test.com]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-name*]{lang="EN-US"}]{#struct_0_x5828_x5730_605485989}[：指定对端地址所属的]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定该参数，则表示对端地址属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1112750282}

[[响应方根据发起发的身份信息通过本配置查找]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1183974588}[并验证对端身份，发起方根据响应方的身份信息通过本配置验证对端身份。]{style="font-family:宋体"}

[[协商双方都必须配置至少一个]{style="font-family:宋体"}**[match remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_x702723905}[规则，当对端的身份与]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置的]{style="font-family:宋体"}**[match remote]{lang="EN-US"}**[规则匹配时，则使用此]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中的信息与对端完成认证。为了使得每个对端能够匹配到唯一的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，不建议在两个或两个以上]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中配置相同的]{style="font-family:宋体"}**[match remote]{lang="EN-US"}**[规则，否则能够匹配到哪个]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[是不可预知的。]{style="font-family:宋体"}

[**[match remote]{lang="EN-US"}**]{#struct_0_x5828_x5730_1455717609}[规则可以配置多个，并同时都有效，其匹配优先级为配置顺序。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_450163827}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_480883845}[创建]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，名称为]{style="font-family:宋体"}[prof1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_943960660}

[\[Sysname\] ike profile prof1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_605682597}[指定需要匹配对端身份类型为]{style="font-family:宋体"}[FQDN]{lang="EN-US"}[，取值为]{style="font-family:宋体"}[www.test.com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-ike-profile-prof1\] match remote identity fqdn www.test.com]{lang="EN-US"}]{#struct_0_x5828_x5730_1039516044}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_1496525630}[指定需要匹配对端身份类型为]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，取值为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-ike-profile-prof1\] match remote identity address 10.1.1.1]{lang="EN-US"}]{#struct_0_x5828_x5730_275035610}

[[【相关命令】]{style="font-family:黑体"} ]{#struct_0_x5828_x5730_x1607836598}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-identity]{lang="EN-US"}**]{#struct_0_x5828_x5730_295396526}
:::

::: {#235804999 .myid}
[]{#_Toc404793341}[]{#struct_0_x5828_x5730_388288570}[]{#_Toc339467239}

**IKE \-- IKE配置命令 \-- pre-shared-key**

------------------------------------------------------------------------

[**[pre-shared-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_1213314191}[命令用来配置预共享密钥。]{style="font-family:宋体"}

[**[undo pre-shared-key]{lang="EN-US"}**]{#struct_0_x5828_x5730_605617061}[命令用来取消配置的预共享密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2130249514}

[**[pre-shared-key ]{lang="EN-US"}**[{ **address** { *ipv4-address* \[ *mask \| mask-length* \] \| **ipv6** *ipv6-address* \[ *prefix-length* \] } \| **hostname** *host-name* } **key** { **cipher** *cipher-key* \| **simple** *simple-key* } ]{lang="EN-US"}]{#struct_0_x5828_x5730_x541181802}

[**[undo pre-shared-key ]{lang="EN-US"}**[{ **address** { *ipv4-address* \[ *mask \| mask-length* \] \| **ipv6** *ipv6-address* \[ *prefix-length* \] } \| **hostname** *host-name* } ]{lang="EN-US"}]{#struct_0_x5828_x5730_354452837}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1243930769}

[[未配置预共享密钥。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_2139439793}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1650932052}

[[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_x1394722122}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_649256099}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_605158306}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1360701680}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x163067906}

[**[address]{lang="EN-US"}**]{#struct_0_x5828_x5730_1794920605}[：对端的地址。]{style="font-family:宋体"}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_x706324603}[：对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[mask]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1206860916}[：对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址掩码，缺省值为]{style="font-family:宋体"}[255.255.255.255]{lang="EN-US"}[。]{style="font-family:宋体"}

[*[mask-length]{lang="EN-US"}*]{#struct_0_x5828_x5730_x2005486490}[：对端的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址掩码长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[32]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_x5828_x5730_x648094128}[：指定对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_x5828_x5730_605092770}[：对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[prefix-length]{lang="EN-US"}*]{#struct_0_x5828_x5730_x544286730}[：对端的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址前缀长度，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[128]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[hostname ]{lang="EN-US"}***[host-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1860807416}[：对端主机名。取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，区分大小写。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**]{#struct_0_x5828_x5730_1310184780}[：设置的预共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_x5828_x5730_x389032086}[：表示以明文方式设置预共享密钥。]{style="font-family:宋体"}

[*[simple-key]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1626907960}[：设置的明文密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串，区分大小写，]{style="font-family:宋体"}[密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_x5828_x5730_2091043582}[：表示以密文方式设置预共享密钥。]{style="font-family:宋体"}

[*[cipher-key]{lang="EN-US"}*]{#struct_0_x5828_x5730_1387916883}[：设置密文密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[201]{lang="EN-US"}[个字符的字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[201]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1634230153}

[[配置预共享密钥的同时，还通过参数]{style="font-family:宋体"}**[address]{lang="EN-US"}**]{#struct_0_x5828_x5730_605289378}[和]{style="font-family:宋体"}**[hostname]{lang="EN-US"}**[指定了使用该预共享密钥的匹配条件，即与哪些]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址或哪些主机名的对端协商时，才可以使用该预共享密钥。]{style="font-family:宋体"}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1492014405}[协商双方必须配置了相同的预共享密钥，预共享密钥类型的身份认证才会成功。]{style="font-family:宋体"}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1273901339}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x334905532}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1291805712}[创建]{style="font-family:宋体"}[IKE keychain key1]{lang="EN-US"}[并进入]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_1781318539}

[\[Sysname\] ike keychain key1]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1310666055}[配置与地址为]{style="font-family:宋体"}[1.1.1.2]{lang="FR"}[的对端使用的]{style="font-family:宋体"}[预共享密钥为明文的]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-ike-keychain-key1\] pre-shared-key address 1.1.1.2 255.255.255.255 key simple 123456TESTplat&!]{lang="EN-US"}]{#struct_0_x5828_x5730_25118521}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605223842}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[authentication-method]{lang="EN-US"}**]{#struct_0_x5828_x5730_47885344}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[keychain]{lang="EN-US"}**]{#struct_0_x5828_x5730_254163329}
:::

::: {#416241956 .myid}
[]{#_Toc404793342}[]{#struct_0_x5828_x5730_1126089458}[]{#_Toc339467240}[]{#_Toc298870235}[]{#_Toc298924384}

**IKE \-- IKE配置命令 \-- priority (IKE keychain view)**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**]{#struct_0_x5828_x5730_x696169130}[命令用来指定]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **priority**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1340601297}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1250551103}

[**[priority]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x5828_x5730_x349851693}

[**[undo priority]{lang="EN-US"}**]{#struct_0_x5828_x5730_605420450}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1503999198}

[[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_735460412}[的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_386807803}

[[IKE keychain]{lang="EN-US"}]{#struct_0_x5828_x5730_140551791}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_511344921}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1166269215}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x869561904}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1098082880}

[**[priority]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x5828_x5730_605354914}[：]{style="font-family:宋体;color:black"}[IKE keychain]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[65535]{lang="EN-US" style="color:black"}[。该数值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_817510144}

[[配置了]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_x946021864}[的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[，优先级高于所有未配置]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**[的]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[。即]{style="font-family:宋体"}[IKE keychain]{lang="EN-US"}[的使用优先级首先决定于其中是否配置了]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**[，其次取决于它的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1182500099}

[[\# ]{lang="DA"}]{#struct_0_x5828_x5730_2066314968}[指定]{style="font-family:宋体"}[IKE keychain key1]{lang="DA"}[的]{style="font-family:宋体"}[优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x5828_x5730_x1751705326}

[\[Sysname\] ike keychain key1]{lang="DA"}

[\[Sysname-ike-keychain-key1\] priority 10]{lang="DA"}
:::

::: {#1309284762 .myid}
[]{#_Toc404793343}[]{#struct_0_x5828_x5730_x730636751}[]{#_Toc339467241}

**IKE \-- IKE配置命令 \-- priority (IKE profile view)**

------------------------------------------------------------------------

[**[priority]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x5828_x5730_x143722077}[命令用来指定]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的优先级。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **priority** ]{lang="EN-US"}]{#struct_0_x5828_x5730_605551522}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1135263678}

[**[priority]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x5828_x5730_1162054137}

[**[undo priority]{lang="EN-US"}**]{#struct_0_x5828_x5730_x980343239}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x823799823}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x1995891984}[的优先级为]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1976624321}

[[IKE-Profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1756563247}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605485986}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1112750287}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1183646908}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_137453670}

[**[priority]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_x5828_x5730_1999368198}[：]{style="font-family:宋体;color:black"}[IKE profile]{lang="EN-US"}[优先级号，取值范围为]{style="font-family:宋体;color:black"}[1]{lang="EN-US" style="color:black"}[～]{style="font-family:宋体;color:black"}[65535]{lang="EN-US" style="color:black"}[。该数值越小，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1209814031}

[[配置了]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**]{#struct_0_x5828_x5730_553013508}[的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，优先级高于所有未配置]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**[的]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[。即]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[的匹配优先级首先决定于其中是否配置了]{style="font-family:宋体"}**[match local address]{lang="EN-US"}**[，其次决定于它的优先级。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x779567880}

[[\# ]{lang="DA"}]{#struct_0_x5828_x5730_x566408850}[指定]{style="font-family:宋体"}[在]{style="font-family:宋体"}[IKE profile prof1]{lang="DA"}[的]{style="font-family:宋体"}[优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x5828_x5730_605682594}

[\[Sysname\] ike profile prof1]{lang="DA"}

[\[Sysname-ike-profile-prof1\] priority 10]{lang="DA"}
:::

::: {#854606781 .myid}
[]{#_Toc404793344}[]{#struct_0_x5828_x5730_1039516041}[]{#_Toc339467242}[]{#_Toc298870239}[]{#_Toc298924388}

**IKE \-- IKE配置命令 \-- proposal**

------------------------------------------------------------------------

[**[proposal]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_x5828_x5730_1496853310}[命令用来配置]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[引用的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **proposal** ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1628440109}[命令用来取消所有引用]{style="font-family:宋体"}[的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1677995599}

[**[proposal]{lang="EN-US"}**[ *proposal-number*&\<1-6\>]{lang="EN-US"}]{#struct_0_x5828_x5730_x1173004656}

[**[undo proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_319315916}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605617058}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_x208402637}[未引用任何]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议，使用系统视图下配置的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议进行]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1596258259}

[[IKE profile]{lang="EN-US"}]{#struct_0_x5828_x5730_1762194416}[视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x190634473}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_366672084}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1749502832}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_804018685}

[*[proposal-number]{lang="EN-US"}*[&\<1-6\>]{lang="EN-US"}]{#struct_0_x5828_x5730_x1853316641}[：]{style="font-family:宋体;color:black"}[IKE]{lang="EN-US"}[提议序号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。该序号在]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中与优先级无关，先配置的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议优先级高。]{style="font-family:宋体"}[&\<1-6\>]{lang="EN-US" style="color:black"}[表示前面的参数最多可以输入]{style="font-family:宋体;color:black"}[6]{lang="EN-US" style="color:black"}[次。]{style="font-family:宋体;color:black"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605158307}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1360701679}[协商过程中，对于发起方，如果使用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全策略下指定了]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[，则使用]{style="font-family:宋体"}[IKE profile]{lang="EN-US"}[中引用的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议进行协商；对于响应方，则使用系统视图下配置的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议与对端发送的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议进行匹配。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x163526643}

[[\# ]{lang="DA"}]{#struct_0_x5828_x5730_x970138421}[设置]{style="font-family:宋体"}[IKE profile prof1]{lang="DA"}[引用序号为]{style="font-family:宋体"}[10]{lang="DA"}[的]{style="font-family:宋体"}[IKE]{lang="DA"}[安全提议]{style="font-family:
宋体"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="DA"}]{#struct_0_x5828_x5730_x917414622}

[\[Sysname\] ike profile prof1]{lang="DA"}

[[\[Sysname-ike-profile-prof1\] proposal 10]{lang="DA" style="font-size:8.5pt;
font-family:\"Courier New\";color:windowtext"}]{#struct_0_x5828_x5730_x482695925}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x754086863}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ike proposal]{lang="DA"}**]{#struct_0_x5828_x5730_x613861888}
:::

::: {#1887032056 .myid}
[]{#_Toc404793345}[]{#struct_0_x5828_x5730_605092771}[]{#_Toc339467243}

**IKE \-- IKE配置命令 \-- reset ike sa**

------------------------------------------------------------------------

[**[reset]{lang="EN-US"}**[ **ike** **sa**]{lang="EN-US"}]{#struct_0_x5828_x5730_x544286731}[命令用来清除]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1860741880}

[**[reset]{lang="EN-US"}**[ **ike** **sa** \[ **connection-id** *connection-id* \]]{lang="EN-US"}]{#struct_0_x5828_x5730_x675537546}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x8894102}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x105617875}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1374466186}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_134176486}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x237407985}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605289379}

[**[connection-id]{lang="EN-US"}***[ connection-id]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1492014404}[：清除指定连接]{style="font-family:宋体"}[ID]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[2000000000]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1454982016}

[[删除]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_1212158920}[时，会向对端发送删除通知消息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_2038409692}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x1642186412}[查看当前的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ike sa]{lang="EN-US"}]{#struct_0_x5828_x5730_605223843}

[    Total IKE SAs:  2]{lang="EN-US"}

[    Connection-ID  Remote            Flag        DOI]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      1            202.38.0.2      RD\|ST       IPSEC]{lang="EN-US"}

[      2            202.38.0.3      RD\|ST       IPSEC]{lang="EN-US"}

[Flags:]{lang="EN-US"}

[RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING TO---TIMEOUT]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_47885345}[清除连接]{style="font-family:宋体"}[ID]{lang="EN-US"}[号为]{style="font-family:宋体"}[2 ]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[ ]{lang="EN-US"}

[[\<Sysname\> reset ike sa 2]{lang="EN-US"}]{#struct_0_x5828_x5730_x1702151807}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x2116493030}[查看当前的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> display ike sa]{lang="EN-US"}]{#struct_0_x5828_x5730_605420451}

[ ]{lang="EN-US"}

[Total IKE SAs:  1]{lang="EN-US"}

[    Connection-ID  Remote            Flag        DOI]{lang="EN-US"}

[  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[      1            202.38.0.2      RD\|ST       IPSEC]{lang="EN-US"}

[Flags:]{lang="EN-US"}

[RD\--READY ST\--STAYALIVE RL\--REPLACED FD---FADING TO---TIMEOUT]{lang="EN-US"}
:::

::: {#-842236237 .myid}
[]{#_Toc339467244}[]{#_Toc404793346}[]{#struct_0_x5828_x5730_1503999199}[]{#_Toc342398094}[]{#_Toc336450642}

**IKE \-- IKE配置命令 \-- reset ike statistics**

------------------------------------------------------------------------

[**[reset ike statistics]{lang="EN-US"}**]{#struct_0_x5828_x5730_735394876}[命令用于清除]{style="font-family:宋体"}[IKE]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x5828_x5730_x701451958}

[**[reset ike statistics]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1551997439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_105323870}

[[用户视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_x359740885}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x730402124}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x955593782}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_605354915}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_817510143}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_x946021867}[清除]{style="font-family:宋体"}[IKE]{lang="EN-US"}[的]{style="font-family:宋体"}[MIB]{lang="EN-US"}[统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset ike statistics]{lang="EN-US"}]{#struct_0_x5828_x5730_1182696707}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_867590246}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[snmp-agent trap enable ike]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1567737614}
:::

::: {#-342193353 .myid}
[]{#_Toc404793347}[]{#struct_0_x5828_x5730_2071796369}

**IKE \-- IKE配置命令 \-- sa duration**

------------------------------------------------------------------------

[**[sa]{lang="EN-US"}**[ **duration**]{lang="EN-US"}]{#struct_0_x5828_x5730_x2086083569}[命令用来指定一个]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[存活时间，超时后]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[将自动更新。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **sa** **duration**]{lang="EN-US"}]{#struct_0_x5828_x5730_x1096825539}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_605551523}

[]{#struct_0_x5828_x5730_1135263677}[**[sa duration]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#_Hlt16152291}

[**[undo sa duration]{lang="EN-US"}**]{#struct_0_x5828_x5730_1163037177}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x968719346}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_331084070}[提议的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[存活时间为]{style="font-family:宋体"}[86400]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1603140411}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_851387337}[提议视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x994983447}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_605485987}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1112750288}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1184367804}

[*[seconds]{lang="EN-US"}*]{#struct_0_x5828_x5730_397858150}[：指定]{lang="EN-US" style="font-family:宋体"}[IKE SA]{lang="EN-US"}[存活时间，取值范围为]{lang="EN-US" style="font-family:宋体"}[60]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[604800]{lang="EN-US"}[，单位为秒。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_464173135}

[[在指定的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_21603287}[存活时间超时前，设备会提前协商另一个]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[来替换旧的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[。在新的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[还没有协商完之前，依然使用旧的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[；在新的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[建立后，将立即使用新的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[，而旧的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[在存活时间超时后，将被自动清除。]{style="font-family:宋体"}

[[如果协商双方配置了不同的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}]{#struct_0_x5828_x5730_x965697837}[存活时间，则时间较短的存活时间生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_625430976}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_931870508}[指定]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议]{style="font-family:宋体"}[1]{lang="EN-US"}[的]{style="font-family:宋体"}[IKE SA]{lang="EN-US"}[存活时间]{style="font-family:宋体"}[600]{lang="EN-US"}[秒（]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_605682595}

[\[Sysname\] ike proposal 1]{lang="EN-US"}

[\[Sysname-ike-proposal-1\] sa duration 600]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1039516042}

[[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol;border:none"}]{.TerminalDisplayshading}**[display ike proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_1496918846}
:::

::: {#-517257186 .myid}
[]{#_Toc404793348}[]{#struct_0_x5828_x5730_1943384754}[]{#_Toc342398096}[]{#_Toc336450641}

**IKE \-- IKE配置命令 \-- snmp-agent trap enable ike**

------------------------------------------------------------------------

[**[snmp-agent trap enable ike]{lang="EN-US"}**]{#struct_0_x5828_x5730_257978762}[命令用来开启]{style="font-family:
宋体"}[IKE]{lang="EN-US"}[的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[undo snmp-agent]{lang="EN-US"}**[ **trap** **enable** **ike**]{lang="EN-US"}]{#struct_0_x5828_x5730_1958440815}[命令用来关闭指定的]{style="font-family:宋体"}[IKE]{lang="EN-US"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}[       ]{lang="EN-US"}]{#struct_0_x5828_x5730_x891411316}

[**[snmp-agent trap enable]{lang="EN-US"}**[ **ike** \[ ]{lang="EN-US"}**[attr]{lang="EN-US"}**]{#struct_0_x5828_x5730_x86789751}**[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[not]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:
\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[support]{lang="EN-US"}**[ \| **auth-failure** \| **cert**]{lang="EN-US"}**[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[type]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[unsupport]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[cert-unavailable ]{lang="EN-US"}**[\| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[decrypt-failure]{lang="EN-US"}**[ \| **encrypt-failure** \| **global** \| **invalid-cert-auth**]{lang="EN-US"}[ \|]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[ invalid-cookie]{lang="EN-US"}**[ \| **invalid-id** ]{lang="EN-US"}[\|]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}**[ invalid-proposal]{lang="EN-US"}**[ \|]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[invalid]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[protocol]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[invalid]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[sign]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[no-sa-failure ]{lang="EN-US"}**[\|]{lang="EN-US"}[ **proposal-add** \| **proposal--delete** \| **tunnel-start** \| **tunnel-stop** \| **unsupport**]{lang="EN-US"}**[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[exch]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[type ]{lang="EN-US"}**[\] \*]{lang="EN-US"}

[**[undo snmp-agent trap enable]{lang="EN-US"}**[ **ike** \[ ]{lang="EN-US"}**[attr]{lang="EN-US"}**]{#struct_0_x5828_x5730_605617059}**[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[not]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:
\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[support]{lang="EN-US"}**[ \| **auth-failure** \| **cert**]{lang="EN-US"}**[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[type]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[unsupport]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[cert-unavailable ]{lang="EN-US"}**[\| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[decrypt-failure]{lang="EN-US"}**[ \| **encrypt-failure** \| **global** \| **invalid-cert-auth**]{lang="EN-US"}[ \|]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[ invalid-cookie]{lang="EN-US"}**[ \| **invalid-id** ]{lang="EN-US"}[\|]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}**[ invalid-proposal]{lang="EN-US"}**[ \|]{lang="EN-US"}[ ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[invalid]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[protocol]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[invalid]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[sign]{lang="EN-US"}**[ \| ]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}**[no-sa-failure ]{lang="EN-US"}**[\|]{lang="EN-US"}[ **proposal-add** \| **proposal--delete** \| **tunnel-start** \| **tunnel-stop** \| **unsupport**]{lang="EN-US"}**[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[exch]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;font-family:\"charset0MS Sans Serif\",\"sans-serif\";
color:black"}[type ]{lang="EN-US"}**[\] \*]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x208402638}

[[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_x1597110227}[的所有]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:
宋体"}[功能均处于开启状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1095510667}

[[系统视图]{style="font-family:宋体"}]{#struct_0_x5828_x5730_1482250244}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1915193416}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x415248910}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1710524718}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1799044487}

[**[attr-not-support]{lang="EN-US"}**]{#struct_0_x5828_x5730_605158304}[：表示属性参数不支持时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[auth-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_1360701682}[：表示认证失败时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[cert]{lang="EN-US"}**]{#struct_0_x5828_x5730_x162936834}**[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[type]{lang="EN-US"}[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[unsupport]{lang="EN-US"}**[：表示证书类型不支持时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[cert-unavailable]{lang="EN-US"}**]{#struct_0_x5828_x5730_622845258}[：表示无法获取证书时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[decrypt-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1136918763}[：表示解密失败时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[encrypt-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1772864815}[：表示加密失败时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[global]{lang="EN-US" style="font-size:10.0pt"}**]{#struct_0_x5828_x5730_339316500}[：表示全局]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:
宋体"}[功能。]{style="font-family:宋体"}

[**[invalid-cert-auth]{lang="EN-US"}**]{#struct_0_x5828_x5730_x685068835}[：表示证书认证无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[invalid-cookie]{lang="EN-US"}**]{#struct_0_x5828_x5730_605092768}[：表示]{style="font-family:宋体"}[cookie]{lang="EN-US"}[无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[invalid-id]{lang="EN-US"}**]{#struct_0_x5828_x5730_1412028398}[：表示身份信息无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[invalid-proposal]{lang="EN-US"}**]{#struct_0_x5828_x5730_x480728588}[：表示]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[invalid]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1357733827}**[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[protocol]{lang="EN-US"}**[：表示安全协议无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[invalid]{lang="EN-US"}**]{#struct_0_x5828_x5730_163952438}**[-]{lang="EN-US" style="font-size:9.0pt;
font-family:\"charset0MS Sans Serif\",\"sans-serif\";color:black"}[sign]{lang="EN-US"}**[：表示证书签名无效时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[no-sa-failure]{lang="EN-US"}**]{#struct_0_x5828_x5730_x2047327725}[：表示无法查到]{style="font-family:宋体"}[SA]{lang="EN-US"}[时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[proposal-add]{lang="EN-US"}**]{#struct_0_x5828_x5730_x340530032}[：表示添加]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[proposal-delete]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1473179346}[：表示删除]{style="font-family:宋体"}[IKE]{lang="EN-US"}[提议时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[tunnel-start]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1108261409}[：表示创建]{style="font-family:宋体"}[IKE]{lang="EN-US"}[隧道时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[tunnel-stop]{lang="EN-US"}**]{#struct_0_x5828_x5730_605289376}[：表示删除]{style="font-family:宋体"}[IKE]{lang="EN-US"}[隧道时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[**[unsupport-exch-type]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1492014399}[：表示协商类型不支持时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1408386600}

[[如果不指定任何参数，则表示开启或关闭所有类型的]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_2112206457}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[[如果希望生成并输出某种类型的]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_1214833045}[告警信息，则需要保证]{style="font-family:宋体"}[IKE]{lang="EN-US"}[的全局]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:
宋体"}[功能以及相应类型的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能均处于开启状态。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1556719184}

[[希望设备在创建]{style="font-family:宋体"}[IKE]{lang="EN-US"}]{#struct_0_x5828_x5730_461329652}[隧道时生成并发送告警信息，需要开启以下]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;
font-family:宋体"}[功能：]{style="font-family:宋体"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_952621463}[开启全局]{style="font-family:宋体"}[IKE]{lang="EN-US"}[告警]{style="font-size:10.0pt;font-family:宋体"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_605223840}

[\[Sysname\] snmp-agent trap enable ike global]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_47885346}[开启创建]{style="font-family:宋体"}[IKE ]{lang="EN-US"}[隧道时的]{style="font-family:宋体"}[告警]{style="font-size:10.0pt;font-family:
宋体"}[功能。]{style="font-family:宋体"}

[[\[Sysname\] snmp-agent trap enable ike tunnel-start]{lang="EN-US"}]{#struct_0_x5828_x5730_x128173695}
:::

::: {#-1803711523 .myid}
[]{#struct_0_x5828_x5730_x1427328453}[]{#_Toc404793349}[]{#_Toc373826876}[]{#_Toc365898452}

**IKE \-- IKE配置命令 \-- tunnel protection**

------------------------------------------------------------------------

[**[tunnel protection]{lang="EN-US"}**]{#struct_0_x5828_x5730_167136855}[命令用来]{style="font-family:宋体"}[在隧道接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[undo tunnel protection]{lang="EN-US"}**]{#struct_0_x5828_x5730_1112576084}[命令用来删除指定的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的应用]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1968369088}

[**[tunnel protection ipsec profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1631444054}

[**[undo ]{lang="EN-US"}[tunnel protection]{lang="EN-US"}**]{#struct_0_x5828_x5730_x1427000773}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1141321916}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_x1670793067}[接口下没有引用任何的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1347276670}

[[Tunnel]{lang="EN-US"}]{#struct_0_x5828_x5730_x217741193}[接口视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_1421958702}

[[network-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_1607718801}

[[mdc-admin]{lang="EN-US"}]{#struct_0_x5828_x5730_x1797666720}

[[【参数】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_315800948}

[*[profile-name]{lang="EN-US"}*]{#struct_0_x5828_x5730_x1426935237}[：指定使用的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架，且必须为]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商方式的]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架。其中，]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架的名字，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x591328447}[使用指导]{style="font-family:黑体"}[】]{style="font-family:黑体"}

[[在隧道接口上应用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}]{#struct_0_x5828_x5730_x1809612537}[安全框架后，隧道两端会通过]{style="font-family:宋体"}[IKE]{lang="EN-US"}[协商建立]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[隧道对隧道接口上传输的数据流进行]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护。目前，仅支持对]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[隧道报文进行]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[保护。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1203128367}

[[\# ]{lang="EN-US"}]{#struct_0_x5828_x5730_434570216}[配置使用]{style="font-family:宋体"}[IPsec]{lang="EN-US"}[安全框架]{style="font-family:宋体"}[prf1]{lang="EN-US"}[来保护接口]{style="font-family:宋体"}[Tunnel1]{lang="EN-US"}[的报文。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_x5828_x5730_647316996}

[\[Sysname\] interface tunnel 1 mode advpn gre]{lang="EN-US"}

[\[Sysname-Tunnel1\]tunnel protection ipsec profile prf1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_x5828_x5730_x1979122256}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[interface tunnel]{lang="EN-US"}**]{#struct_0_x5828_x5730_1022730664}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[l[   ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.5pt;font-family:Wingdings"}**[display interface tunnel]{lang="EN-US"}**]{#struct_0_x5828_x5730_x948423803}[（]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[业务命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[隧道]{style="font-family:宋体"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipsec profile]{lang="EN-US"}**]{#struct_0_x5828_x5730_x618029901}
:::
