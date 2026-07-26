::: {#-217826367 .myid}
[]{#_Toc404792519}[]{#struct_0_86480_74578_1656915518}[]{#_Toc400718762}

**AAA \-- ISP域中实现AAA配置命令 \-- aaa nas-id profile**

------------------------------------------------------------------------

[**[aaa nas-id profile]{lang="EN-US"}**]{#struct_0_86480_74578_x1383670559}[命令用来创建]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[，并进入]{style="font-family:宋体"}[NAS-ID-Profile]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[**[undo aaa nas-id profile]{lang="EN-US"}**]{#struct_0_86480_74578_x1127746412}[命令用来删除指定的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1523524093}

[**[aaa ]{lang="EN-US"}[nas-id profile]{lang="EN-US"}**[ ]{lang="EN-US"}*[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1106636268}

[**[undo aaa ]{lang="EN-US"}[nas-id profile]{lang="EN-US"}**[ ]{lang="EN-US"}*[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_x165913835}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2073526137}

[[不存在]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}]{#struct_0_86480_74578_2109072456}[。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_x508350920}[[【视图】]{style="font-family:黑体"}]{#_Toc400718763}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1071967837}

[]{#struct_0_86480_74578_1449415382}[[【缺省用户角色】]{style="font-family:黑体"}]{#_Toc400718764}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x765074039}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1596912334}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_877424208}

[*[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_960116751}[：]{style="font-family:宋体"}[Profile]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。该]{style="font-family:宋体"}[Profile]{lang="EN-US"}[用于保存]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[与]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定关系。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_608542626}[[【使用指导】]{style="font-family:黑体"}]{#_Toc400718765}

[[在某些应用环境中，网络运营商需要使用接入设备发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_571032229}[服务器的]{style="font-family:宋体"}[NAS-Identifier]{lang="EN-US"}[属性值来获知用户的接入位置，而用户的接入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[可标识用户的接入位置，因此接入设备上可通过建立用户接入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与指定的]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[之间的绑定关系来实现接入位置信息的映射。]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[用于保存]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定关系。这样，当用户上线时，设备会将与用户接入]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[匹配的]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[填充在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[请求报文中的]{style="font-family:宋体"}[NAS-Identifier]{lang="EN-US"}[属性中发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_x1432089836}[[【举例】]{style="font-family:黑体"}]{#_Toc400718766}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_2058514671}[创建一个名字为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_494116104}

[\[Sysname\] aaa nas-id profile aaa]{lang="EN-US"}

[\[Sysname-nas-id-prof-aaa\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1607687415}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal nas-id-profile]{lang="EN-US"}**]{#struct_0_86480_74578_x1170151219}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/Portal]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port-security nas-id-profile]{lang="EN-US"}**]{#struct_0_86480_74578_x391632549}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[端口安全）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nas-id bind vlan]{lang="EN-US"}**]{#struct_0_86480_74578_x532136651}
:::

::: {#438604805 .myid}
[]{#_Toc162860222}[]{#_Toc147117539}[]{#_Toc147049899}[]{#_Toc146447619}[]{#_Toc69900450}[]{#_Toc205699628}[]{#_Toc268769693}[]{#_Toc404792520}[]{#struct_0_86480_74578_x1854655587}[]{#_Toc334602005}[]{#_Hlt19451604}

**AAA \-- ISP域中实现AAA配置命令 \-- aaa session-limit**

------------------------------------------------------------------------

[**[aaa session-limit]{lang="EN-US"}**]{#struct_0_86480_74578_x408421471}[命令用来配置同时在线的最大用户连接数，即采用指定登录方式登录设备并同时在线的用户数。]{style="font-family:宋体"}

[**[undo aaa session-limit]{lang="EN-US"}**]{#struct_0_86480_74578_x1764661758}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_340186826}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_692829906}[模式下：]{style="font-family:宋体"}

[**[aaa session-limit ]{lang="EN-US"}**[{ **ftp** \| **http** \| **https** \| **ssh** \| **telnet** } *max-sessions*]{lang="EN-US"}]{#struct_0_86480_74578_x332255346}

[**[undo aaa session-limit ]{lang="EN-US"}**[{ **ftp** \| **http** \| **https** \| **ssh** \| **telnet** }]{lang="EN-US"}]{#struct_0_86480_74578_x1939629338}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x453938836}[模式下：]{style="font-family:宋体"}

[**[aaa session-limit ]{lang="EN-US"}**[{ **https** \| **ssh** } *max-sessions*]{lang="EN-US"}]{#struct_0_86480_74578_x219703355}

[**[undo aaa session-limit ]{lang="EN-US"}**[{ **https** \| **ssh** }]{lang="EN-US"}]{#struct_0_86480_74578_1248359660}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158121225}

[[缺省的最大用户连接数为]{style="font-family:宋体"}[32]{lang="EN-US"}]{#struct_0_86480_74578_x1721585579}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1927566235}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1916725656}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1699519846}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1431703719}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_983075158}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x186597841}

[**[ftp]{lang="EN-US"}**]{#struct_0_86480_74578_645964448}[：表示]{style="font-family:宋体"}[FTP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_86480_74578_1158186761}[：表示]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[https]{lang="EN-US"}**]{#struct_0_86480_74578_x928487086}[：表示]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[ssh]{lang="EN-US"}**]{#struct_0_86480_74578_x1852142395}[：表示]{style="font-family:宋体"}[SSH]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[**[telnet]{lang="EN-US"}**]{#struct_0_86480_74578_x191077180}[：表示]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[*[max-sessions]{lang="EN-US"}*]{#struct_0_86480_74578_x28468780}[：允许同时在线的最大用户连接数，取值范围以各产品实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_448504573}

[[配置本命令后，当指定类型的接入用户的用户数超过当前配置的最大连接数后，新的接入请求将被拒绝。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1678726795}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1924461046}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1576556557}[设置同时在线的最大]{style="font-family:宋体"}[FTP]{lang="EN-US"}[用户连接数为]{style="font-family:宋体"}[4]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1158252297}

[\[Sysname\] aaa session-limit ftp 4]{lang="EN-US"}
:::

::::: {#1492048249 .myid}
[]{#_Toc404792521}[]{#struct_0_86480_74578_1930658984}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting advpn**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_1930724520}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_14565968}
:::

[ ]{lang="EN-US"}

[**[accounting advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x137143889}[命令用来为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting advpn]{lang="EN-US"}**]{#struct_0_86480_74578_1808946851}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x258012162}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1668741011}[模式下：]{style="font-family:宋体"}

[**[accounting advpn]{lang="EN-US"}**[ { **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1387622789}

[**[undo accounting advpn]{lang="EN-US"}**]{#struct_0_86480_74578_328832447}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_534593782}[模式下：]{style="font-family:宋体"}

[**[accounting advpn]{lang="EN-US"}**[ { **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1931052200}

[**[undo accounting advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1208484271}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x144410356}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_1166020945}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_14570448}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_574112488}[域视图]{style="font-family:宋体"}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x531537842}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x363297626}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1589530845}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_930969290}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x707241958}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1931117736}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x769411286}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1034971674}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_535801782}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_844489682}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1601068349}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x434838416}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting advpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1840416750}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1930527911}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting advpn radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1978840744}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x1511508989}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1778226131}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x2092175127}
:::::

::: {#1841784429 .myid}
[]{#_Toc205699630}[]{#_Toc162860223}[]{#_Toc147117540}[]{#_Toc147049900}[]{#_Toc146447620}[]{#_Toc125946353}[]{#_Toc404792522}[]{#struct_0_86480_74578_x886421734}[]{#_Toc268769694}[]{#_Toc375040166}[]{#_Toc375040167}[]{#_Toc375040168}[]{#_Toc375040169}[]{#_Toc375040170}[]{#_Toc375040171}[]{#_Toc375040172}[]{#_Toc375040173}[]{#_Toc375040174}[]{#_Toc375040175}[]{#_Toc375040176}[]{#_Toc375040177}[]{#_Toc375040178}[]{#_Toc375040179}[]{#_Toc375040180}[]{#_Toc375040181}[]{#_Toc375040182}[]{#_Toc375040183}[]{#_Toc375040184}[]{#_Toc375040185}[]{#_Toc375040186}[]{#_Toc375040187}[]{#_Toc375040188}[]{#_Toc375040189}[]{#_Toc151192654}[]{#_Toc151192831}[]{#_Toc151262727}[]{#_Toc151351802}[]{#_Toc153008556}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting command**

------------------------------------------------------------------------

[**[accounting command]{lang="EN-US"}**]{#struct_0_86480_74578_928102790}[命令用来配置命令行计费方法。]{style="font-family:宋体"}

[**[undo accounting command]{lang="EN-US"}**]{#struct_0_86480_74578_x1620053301}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158448905}

[**[accounting command hwtacacs-scheme]{lang="EN-US"}**[ *hwtacacs-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_1305921893}

[**[undo accounting command]{lang="EN-US"}**]{#struct_0_86480_74578_1616746343}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_731180533}

[[命令行计费采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1172747659}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_548282778}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x758332721}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_975374607}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1158514441}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1711189506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1212700228}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x659926659}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1914882234}

[[命令行计费是指，用户执行过的所有命令或被成功授权执行的命令，会被计费服务器进行记录。]{style="font-family:宋体"}]{#struct_0_86480_74578_985797524}

[[目前，仅支持使用远程]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1127152895}[服务器完成命令行计费功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1068360464}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_834729488}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置使用]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费方案]{style="font-family:宋体"}[hwtac]{lang="EN-US"}[进行命令行计费。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1158579977}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting command hwtacacs-scheme hwtac]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1425255258}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x1847365755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[command accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1064232524}[（基础命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[登录设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x891798206}
:::

::: {#-560144503 .myid}
[]{#_Toc404792523}[]{#struct_0_86480_74578_346849648}[]{#_Toc268769695}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting default**

------------------------------------------------------------------------

[**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x1866004632}[命令用来为当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域配置缺省的计费方法。]{style="font-family:宋体"}

[**[undo accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x240342812}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1157596937}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1545365707}[模式下：]{style="font-family:宋体"}

[**[accounting default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1061231065}

[**[undo accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_895150697}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1794735440}[模式下：]{style="font-family:宋体"}

[**[accounting default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x8388081}

[**[undo accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x109729614}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x157938951}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1116248003}[域的缺省计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1157662473}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x360170606}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1401364673}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1900738168}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1852979097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1443219956}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x823077992}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x1587115056}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1158121226}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1721520043}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x964989400}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1711541908}[域的缺省计费方法对于该域中未指定具体计费方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的计费方法，则该计费方法对于这类用户不能生效。]{style="font-family:宋体"}

[[本地计费只是为了支持本地用户的连接数管理，没有实际的计费相关的统计功能。]{style="font-family:宋体"}]{#struct_0_86480_74578_1807372714}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_1179073240}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_692758950}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1047473929}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置缺省计费方法为使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1158186762}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting default radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x928683694}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x673423502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1694201625}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1073210449}
:::

::: {#-2020424372 .myid}
[]{#_Toc404792524}[]{#struct_0_86480_74578_390934073}[]{#_Toc359405560}[]{#_Toc355710203}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting ipoe**

------------------------------------------------------------------------

[**[accounting ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x800843002}[命令用来为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_1509391691}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x825321314}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1755739539}[模式下：]{style="font-family:宋体"}

[**[accounting ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1213551849}**[broadcast]{lang="EN-US"}**[ ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name1* ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name2* \[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \] \[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[ \] \| ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[ \] \| ]{lang="EN-US"}**[none]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* \[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \] \[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[ \] }]{lang="EN-US"}

[**[undo accounting ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_390868537}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x417045834}[模式下：]{style="font-family:宋体"}

[**[accounting ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x1099616373}**[broadcast]{lang="EN-US"}**[ ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name1* ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name2* \[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \] \| ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* \[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ \] }]{lang="EN-US"}

[**[undo accounting ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1032562409}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1861017120}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_x522943477}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_2080595850}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1219605022}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1896914254}

[[network-admin]{lang="FR"}]{#struct_0_86480_74578_878914634}

[[mdc-admin]{lang="FR"}]{#struct_0_86480_74578_x1544062381}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_391327289}

[**[broadcast]{lang="FR"}**]{#struct_0_86480_74578_x599518414}[：指定广播]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案，即同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中的计费服务器发送计费请求。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="FR"}**]{#struct_0_86480_74578_x419593940}*[radius-scheme-name1]{lang="FR"}*[：]{style="font-family:宋体"}[表示主送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_x2061863759}[ ]{lang="FR"}*[radius-scheme-name2]{lang="FR"}*[：]{style="font-family:宋体"}[表示抄送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="FR"}**]{#struct_0_86480_74578_531952223}[：]{style="font-family:宋体"}[本地计费。]{style="font-family:宋体"}

[**[none]{lang="FR"}**]{#struct_0_86480_74578_1803488079}[：]{style="font-family:宋体"}[不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_1374734395}*[ radius-scheme-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[radius-scheme-name]{lang="FR"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_70518539}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}]{#struct_0_86480_74578_1405466309}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* ]{lang="EN-US"}**[local]{lang="EN-US"}**[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}]{#struct_0_86480_74578_391261753}**[broadcast]{lang="FR"}**[关键字时，将同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1320841601}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_410298227}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1288362907}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ipoe local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1154138099}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1857700875}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ipoe radius-scheme rd local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x488758089}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd1]{lang="EN-US"}[和]{style="font-family:宋体"}[rd2]{lang="EN-US"}[进行广播计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_390803000}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ipoe broadcast radius-scheme rd1 radius-scheme rd2 local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x583455289}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x1350792200}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x1838418726}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1510884181}
:::

::::: {#-1942523800 .myid}
[]{#_Toc268769697}[]{#_Toc205699632}[]{#_Toc162860225}[]{#_Toc147117542}[]{#_Toc147049902}[]{#_Toc146447622}[]{#_Toc125946355}[]{#_Toc404792525}[]{#struct_0_86480_74578_1725510989}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting lan-access**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_274871108}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x1918063672}
:::

[ ]{lang="EN-US"}

[**[accounting lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1789103140}[命令用来为]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1158252298}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x174113772}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1385985682}[模式下：]{style="font-family:宋体"}

[**[accounting ]{lang="EN-US"}[lan-access]{lang="EN-US"}**[ {]{lang="EN-US"}]{#struct_0_86480_74578_570211674}**[ ]{lang="EN-US"}[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1]{lang="EN-US"}***[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2 ]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo accounting lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_x2096825352}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1437358682}[模式下：]{style="font-family:宋体"}

[**[accounting ]{lang="EN-US"}[lan-access]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1693770169}**[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1]{lang="EN-US"}***[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2 ]{lang="EN-US"}*[\[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \|]{lang="EN-US"}**[ ]{lang="EN-US"}[local ]{lang="EN-US"}**[\| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}

[**[undo accounting lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1608144965}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1959725508}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_1158317834}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_986445050}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1556385552}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1144370628}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1038517561}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_961823336}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x200293089}

[**[broadcast]{lang="FR"}**]{#struct_0_86480_74578_390737464}[：指定广播]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案，即同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中的计费服务器发送计费请求。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="FR"}**]{#struct_0_86480_74578_x1792152209}*[radius-scheme-name1]{lang="FR"}*[：]{style="font-family:宋体"}[表示主送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_390671928}[ ]{lang="FR"}*[radius-scheme-name2]{lang="FR"}*[：]{style="font-family:宋体"}[表示抄送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="FR"}**]{#struct_0_86480_74578_859143197}[：]{style="font-family:宋体"}[本地计费。]{style="font-family:宋体"}

[**[none]{lang="FR"}**]{#struct_0_86480_74578_1298595123}[：]{style="font-family:宋体"}[不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_1158383370}*[ radius-scheme-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[radius-scheme-name]{lang="FR"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x567163038}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x691175790}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}]{#struct_0_86480_74578_390606392}**[broadcast]{lang="FR"}**[关键字时，将同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_555189097}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_886968995}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1422705445}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting lan-access local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1600317142}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1977803201}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting lan-access radius-scheme rd local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_391065144}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd1]{lang="EN-US"}[和]{style="font-family:宋体"}[rd2]{lang="EN-US"}[进行广播计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_390999608}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ]{lang="EN-US"}[lan-access ]{lang="EN-US"}[broadcast radius-scheme rd1 radius-scheme rd2 local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158448906}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_1305725285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1558932104}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x2021377357}
:::::

::: {#1065218787 .myid}
[]{#_Toc404792526}[]{#struct_0_86480_74578_122555645}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting login**

------------------------------------------------------------------------

[**[accounting login]{lang="EN-US"}**]{#struct_0_86480_74578_x58701308}[命令用来为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting login]{lang="EN-US"}**]{#struct_0_86480_74578_366661474}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_498015739}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x455163930}[模式下：]{style="font-family:宋体"}

[**[accounting login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1158514442}

[**[undo accounting login]{lang="EN-US"}**]{#struct_0_86480_74578_x1710992898}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1807701545}[模式下：]{style="font-family:宋体"}

[**[accounting login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1163106344}

[**[undo accounting login]{lang="EN-US"}**]{#struct_0_86480_74578_217255763}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_332754861}

[[login]{lang="EN-US"}]{#struct_0_86480_74578_x378220388}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1382022699}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_333223157}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158579978}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1424272218}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2060738482}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1775149644}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1353376904}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x1854380406}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x1047423392}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x642013811}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1235772465}

[[不支持对]{style="font-family:宋体"}[FTP]{lang="EN-US"}]{#struct_0_86480_74578_1157596938}[类型的]{style="font-family:宋体"}[login]{lang="EN-US"}[用户进行计费。]{style="font-family:宋体"}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_1545562315}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_902846971}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_539322998}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1346383488}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting login local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1654706006}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[login]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1107650829}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting login radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1948048474}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_1157662474}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x360105070}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x985438269}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x648044520}
:::

::: {#1617448184 .myid}
[]{#_Toc404792527}[]{#struct_0_86480_74578_x687568051}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting portal**

------------------------------------------------------------------------

[**[accounting portal]{lang="EN-US"}**]{#struct_0_86480_74578_x1470390283}[命令用来为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting portal]{lang="EN-US"}**]{#struct_0_86480_74578_x2002604774}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2108765314}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x2089186795}[模式下：]{style="font-family:宋体"}

[**[accounting ]{lang="EN-US"}[portal ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_1895339972}**[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1]{lang="EN-US"}***[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2 ]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo accounting portal]{lang="EN-US"}**]{#struct_0_86480_74578_x687502515}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1098556525}[模式下：]{style="font-family:宋体"}

[**[accounting ]{lang="EN-US"}[portal ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_1880175808}**[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1 ]{lang="EN-US"}***[radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}

[**[undo accounting portal]{lang="EN-US"}**]{#struct_0_86480_74578_1729347162}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x61423767}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_x314554736}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1695589609}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x688092338}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x537240878}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1189223957}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_688792331}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1359485448}

[**[broadcast]{lang="FR"}**]{#struct_0_86480_74578_390802999}[：指定广播]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案，即同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中的计费服务器发送计费请求。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="FR"}**]{#struct_0_86480_74578_x487705374}*[radius-scheme-name1]{lang="FR"}*[：]{style="font-family:宋体"}[表示主送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_1348897811}[ ]{lang="FR"}*[radius-scheme-name2]{lang="FR"}*[：]{style="font-family:宋体"}[表示抄送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="FR"}**]{#struct_0_86480_74578_x688026802}[：]{style="font-family:宋体"}[本地计费。]{style="font-family:宋体"}

[**[none]{lang="FR"}**]{#struct_0_86480_74578_1383345467}[：]{style="font-family:宋体"}[不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_x54149478}*[ radius-scheme-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案。其中]{style="font-family:宋体"}[，]{style="font-family:宋体"}*[radius-scheme-name]{lang="FR"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1595588887}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x992207796}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}]{#struct_0_86480_74578_390606391}**[broadcast]{lang="FR"}**[关键字时，将同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x688223410}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x507261011}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1006410405}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting portal local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1572638781}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1845445642}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting portal radius-scheme rd local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1377196340}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[portal]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd1]{lang="EN-US"}[和]{style="font-family:宋体"}[rd2]{lang="EN-US"}[进行广播计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_391065143}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ]{lang="EN-US"}[portal ]{lang="EN-US"}[broadcast radius-scheme rd1 radius-scheme rd2 local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1272222432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_x688157874}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x180051404}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x547047263}
:::

::::: {#-1130081675 .myid}
[]{#_Toc95387176}[]{#_Toc268769704}[]{#_Toc205699638}[]{#_Toc162860231}[]{#_Toc147117548}[]{#_Toc147049908}[]{#_Toc146447628}[]{#_Toc125946359}[]{#_Toc404792528}[]{#struct_0_86480_74578_x879870465}[]{#_Toc196727129}[]{#_Toc196727132}[]{#_Toc196727133}[]{#_Toc196727134}[]{#_Toc196727135}[]{#_Toc196727136}[]{#_Toc196727137}[]{#_Toc196727138}[]{#_Toc196727139}[]{#_Toc196727140}[]{#_Toc196727141}[]{#_Toc196727142}[]{#_Toc196727143}[]{#_Toc196727144}[]{#_Toc196727145}[]{#_Toc196727146}[]{#_Toc196727147}[]{#_Toc196727148}[]{#_Toc196727149}[]{#_Toc196727150}[]{#_Toc196727151}[]{#_Toc196727152}[]{#_Toc196727153}[]{#_Toc196727155}[]{#_Toc196727156}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting ppp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_1823015681}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_1511511559}
:::

**[ ]{lang="EN-US"}**

[**[accounting ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x495874079}[命令用来为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting ppp]{lang="EN-US"}**]{#struct_0_86480_74578_1158121223}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1721192363}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2016367592}[模式下：]{style="font-family:宋体"}

[**[accounting ppp]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x1208718173}**[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1]{lang="EN-US"}***[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2 ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[hwtacacs-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[hwtacacs-scheme-name]{lang="EN-US"}*[ \] \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \| **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo accounting ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x2037368232}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x336214664}[模式下：]{style="font-family:宋体"}

[**[accounting ppp]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x258207873}**[broadcast radius-scheme ]{lang="EN-US"}***[radius-scheme-name1]{lang="EN-US"}***[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name2 ]{lang="EN-US"}*[\[ ]{lang="EN-US"}**[hwtacacs-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[hwtacacs-scheme-name]{lang="EN-US"}*[ \] \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \| **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}

[**[undo accounting ppp]{lang="EN-US"}**]{#struct_0_86480_74578_1059635619}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1230626247}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_1158186759}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x927962795}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1281627396}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1765242973}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_870464838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1652875808}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2049957121}

[**[broadcast]{lang="FR"}**]{#struct_0_86480_74578_390868535}[：指定广播]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案，即同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中的计费服务器发送计费请求。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="FR"}**]{#struct_0_86480_74578_x417045836}*[radius-scheme-name1]{lang="FR"}*[：]{style="font-family:宋体"}[表示主送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写]{style="font-family:宋体"}[；]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_x1099747445}[ ]{lang="FR"}*[radius-scheme-name2]{lang="FR"}*[：]{style="font-family:宋体"}[表示抄送计费]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="FR"}[～]{style="font-family:宋体"}[32]{lang="FR"}[个字符的字符串]{style="font-family:宋体"}[，]{style="font-family:宋体"}[不区分大小写。]{style="font-family:宋体"}

[**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x2033455357}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_1365396141}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1158252295}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x174965740}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1744281423}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1390087859}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[当指定]{style="font-family:宋体"}]{#struct_0_86480_74578_391327287}**[broadcast]{lang="FR"}**[关键字时，将同时向指定的两个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的主计费服务器发送计费请求，若主计费服务器不可达，再依次向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案里的从计费服务器发送计费请求。主送计费方案计费成功时，表示用户计费成功；抄送计费方案的计费结果对用户无影响。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_415615075}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x35844184}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_48725490}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ppp local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1001655095}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1158317831}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ppp radius-scheme rd local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_391261751}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[ppp]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd1]{lang="EN-US"}[和]{style="font-family:宋体"}[rd2]{lang="EN-US"}[进行广播计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_390802998}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting ]{lang="EN-US"}[ppp ]{lang="EN-US"}[broadcast radius-scheme rd1 radius-scheme rd2 local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_986117370}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}**]{#struct_0_86480_74578_1050070918}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_988685584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x1760568051}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1551254418}
:::::

::::: {#-1064639432 .myid}
[]{#_Toc404792529}[]{#struct_0_86480_74578_1930855590}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting quota-out**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 17 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_1571802387}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x593552068}
:::

[ ]{lang="EN-US"}

[**[accounting quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_1930658982}[命令用来配置用户计费流量配额耗尽策略。]{style="font-family:宋体"}

[**[undo accounting quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_1923004857}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_949903735}

[**[accounting quota-out ]{lang="EN-US"}**[{ **offline** \| **online** }]{lang="EN-US"}]{#struct_0_86480_74578_1684990675}

[**[undo accounting quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_x1813940657}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1132654707}

[[用户的计费流量配额耗尽后将被强制下线。]{style="font-family:宋体"}]{#struct_0_86480_74578_149701229}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1226477714}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x70256155}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x923900448}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1274872249}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1930724518}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_15090255}

[**[offline]{lang="EN-US"}**]{#struct_0_86480_74578_x1121166540}[：当用户的整体流量配额耗尽后，强制用户下线。]{style="font-family:宋体"}

[**[online]{lang="EN-US"}**]{#struct_0_86480_74578_x73746786}[：当用户的整体流量配额耗尽后，允许用户保持在线状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x952924985}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x764862326}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置用户计费流量配额耗尽策略为：当流量配额耗尽后用户仍能保持在线状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1604586239}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-domain-test\] accounting quota-out online]{lang="EN-US"}
:::::

::: {#969487796 .myid}
[]{#_Toc404792530}[]{#struct_0_86480_74578_1943247060}[]{#_Toc391364206}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting sslvpn**

------------------------------------------------------------------------

[**[accounting sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_377163119}[命令用来为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置计费方法。]{style="font-family:宋体"}

[**[undo accounting sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x724649948}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1338893552}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_406137802}[模式下：]{style="font-family:宋体"}

[**[accounting sslvpn]{lang="EN-US"}**[ { **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x978609712}

[**[undo accounting sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x294983347}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1753204917}[模式下：]{style="font-family:宋体"}

[**[accounting sslvpn]{lang="EN-US"}**[ { **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1291037977}

[**[undo accounting sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_421873985}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1177231559}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_x1594147412}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省计费方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1443281788}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_404666539}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1493577279}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_2413548}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_519412194}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1720111851}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x272652194}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x767890434}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="EN-US"}***[radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1134735943}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}[radius-scheme-name]{lang="EN-US"}[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_849530295}

[[可以指定一个或多个备选的计费方法，在当前的计费方法无效时按照配置顺序尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x687109788}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则进行本地计费，若本地计费也无效则不进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2055410721}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_319822102}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置计费方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1776671568}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting sslvpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_433569827}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x2135775819}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] accounting sslvpn radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_44434959}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[accounting default]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_86480_74578_1538020470}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_622007585}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x2101888889}
:::

::::: {#-1011667167 .myid}
[]{#_Toc404792531}[]{#struct_0_86480_74578_318180477}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting start-fail**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 13 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x2110504979}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x815743052}
:::

[ ]{lang="EN-US"}

[**[accounting start-fail]{lang="EN-US"}**]{#struct_0_86480_74578_1931052198}[命令用来配置用户计费开始失败策略，即设备向计费服务器发送计费开始请求失败后，是否允许用户接入网络。]{style="font-family:宋体"}

[**[undo accounting start-fail]{lang="EN-US"}**]{#struct_0_86480_74578_364969544}[命令用来恢复默认情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_267443656}

[**[accounting start-fail ]{lang="EN-US"}**[{ **offline** \| **online** }]{lang="EN-US"}]{#struct_0_86480_74578_x1975982931}

[**[undo accounting start-fail]{lang="EN-US"}**]{#struct_0_86480_74578_286189032}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2046671291}

[[如果用户计费开始失败，允许用户保持在线状态。]{style="font-family:宋体"}]{#struct_0_86480_74578_902189599}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_768210070}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x493462068}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1374929675}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_898865228}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2143070091}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1931117734}

[**[offline]{lang="EN-US"}**]{#struct_0_86480_74578_x769542358}[：强制用户下线。]{style="font-family:宋体"}

[**[online]{lang="EN-US"}**]{#struct_0_86480_74578_x646641059}[：允许用户保持在线状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2001962543}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_254487782}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置计费开始失败策略为：用户计费开始失败时允许用户保持在线状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_943976163}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-domain-test\] accounting start-fail online]{lang="EN-US"}
:::::

::::: {#44161804 .myid}
[]{#_Toc404792532}[]{#struct_0_86480_74578_x733888982}

**AAA \-- ISP域中实现AAA配置命令 \-- accounting update-fail**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 15 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_1690601462}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x798355440}
:::

[ ]{lang="EN-US"}

[**[accounting update-fail]{lang="EN-US"}**]{#struct_0_86480_74578_x1399684176}[命令用来配置用户计费更新失败策略，即设备向计费服务器发送用户的计费更新报文失败时，是否允许用户接入网络。]{style="font-family:宋体"}

[**[undo accounting update-fail]{lang="EN-US"}**]{#struct_0_86480_74578_948595684}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1610973283}

[**[accounting update-fail]{lang="EN-US"}**[ { \[ **max-times** *times* \] **offline** \| **online** }]{lang="EN-US"}]{#struct_0_86480_74578_x613080971}

[**[undo accounting update-fail]{lang="EN-US"}**]{#struct_0_86480_74578_1785385399}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1510391442}

[[如果用户计费更新失败，允许用户保持在线状态。]{style="font-family:宋体"}]{#struct_0_86480_74578_1043239088}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1275044477}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x798289904}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_581110799}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_901998758}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1745905495}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2018932068}

[**[max-times ]{lang="EN-US"}***[times]{lang="EN-US"}*]{#struct_0_86480_74578_990252575}[：]{style="font-family:宋体"}[允许用户连续计费更新失败的次数，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[1]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[offline]{lang="EN-US"}**]{#struct_0_86480_74578_x1563654029}[：如果用户连续计费更新失败的次数达到了指定的次数，则强制用户下线。]{style="font-family:宋体"}

[**[online]{lang="EN-US"}**]{#struct_0_86480_74578_x773107424}[：如果用户计费更新失败，允许用户保持在线状态]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1849248004}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1920198896}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置计费开始失败策略为：用户计费更新失败时允许用户保持在线状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x798486512}

[\[Sysname\] domain isp1]{lang="EN-US"}

[\[Sysname-isp-domain-isp1\] accounting update-fail online]{lang="EN-US"}
:::::

::::: {#1894338506 .myid}
[]{#_Toc404792533}[]{#struct_0_86480_74578_x1759572133}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication advpn**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x1447850243}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x813541800}
:::

**[ ]{lang="EN-US"}**

[**[authentication advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1959043613}[命令用来为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x325334645}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1050333553}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x61823579}[模式下：]{style="font-family:宋体"}

[**[authentication advpn]{lang="EN-US"}**[ { **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1771556924}

[**[undo authentication advpn]{lang="EN-US"}**]{#struct_0_86480_74578_911983902}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x798420976}[模式下：]{style="font-family:宋体"}

[**[authentication advpn]{lang="EN-US"}**[ { **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x649976277}

[**[undo authentication advpn]{lang="EN-US"}**]{#struct_0_86480_74578_1846892045}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x950642276}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x1072559722}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1075087370}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1296084250}[域视图]{style="font-family:宋体"}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1698491745}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1563696247}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_941908452}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1860302107}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x798093296}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x186792088}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1416387551}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1505003040}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1619344261}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x923830679}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_898826713}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1335095057}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication advpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_661704215}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1578303892}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication advpn radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x798027760}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x597583399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_2063059003}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_2021529358}
:::::

::: {#559631199 .myid}
[]{#_Toc404792534}[]{#struct_0_86480_74578_657185887}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication default**

------------------------------------------------------------------------

[**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1681951822}[命令用来为当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域配置缺省的认证方法。]{style="font-family:宋体"}

[**[undo authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1834586457}[命令用来为恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158383367}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x566966431}[模式下：]{style="font-family:宋体"}

[**[authentication default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **ldap-scheme** *ldap-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1113203381}

[**[undo authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1893655701}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x198115517}[模式下：]{style="font-family:宋体"}

[**[authentication default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **ldap-scheme** *ldap-scheme-name* \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1374061428}

[**[undo authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1865826194}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1405243562}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_30967087}[域的缺省认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158448903}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1306052965}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x445629766}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1812998917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1584092969}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x124207077}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1064274964}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[ldap-scheme]{lang="EN-US"}**[ *ldap-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_x2032195972}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_48374597}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1158514439}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x1711713791}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_2035121394}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1401459621}[域的缺省的认证方法对于该域中未指定具体认证方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的认证方法，则该认证方法对于这类用户不能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1632420645}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1032098556}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1640252938}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置缺省认证方法为使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x720098841}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication default radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158579975}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1425124186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_29814857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_438218335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1895689582}
:::

::: {#-421791945 .myid}
[]{#_Toc404792535}[]{#struct_0_86480_74578_390606390}[]{#_Toc359405564}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication ipoe**

------------------------------------------------------------------------

[**[authentication ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1377196339}[命令用来为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1725952171}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1467850056}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_391065142}[模式下：]{style="font-family:宋体"}

[**[authentication ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1837926476}**[local ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \|]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\]]{lang="EN-US"}**[ ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo authentication ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_627583681}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_390999606}[模式下：]{style="font-family:宋体"}

[**[authentication ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x1188232323}**[local ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] }]{lang="EN-US"}

[**[undo authentication ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1643751247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_428848602}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_390934070}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x800843001}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1509457227}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_390868534}

[[network-admin]{lang="FR"}]{#struct_0_86480_74578_x417045835}

[[mdc-admin]{lang="FR"}]{#struct_0_86480_74578_x1099681909}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1066154650}

[**[local]{lang="FR"}**]{#struct_0_86480_74578_391327286}[：]{style="font-family:宋体"}[本地认证。]{style="font-family:宋体"}

[**[none]{lang="FR"}**]{#struct_0_86480_74578_x599518423}[：]{style="font-family:宋体"}[不认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_x419266257}*[ radius-scheme-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="FR"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_391261750}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}]{#struct_0_86480_74578_1320841600}**[radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_410232691}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1485830141}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_390803005}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication ipoe local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1146952547}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1408784765}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication ipoe radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x583455287}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1349874696}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1025170396}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1479920710}
:::

::::: {#-2134319034 .myid}
[]{#_Toc268769706}[]{#_Toc205699640}[]{#_Toc162860233}[]{#_Toc147117550}[]{#_Toc147049910}[]{#_Toc146447630}[]{#_Toc125946361}[]{#_Toc404792536}[]{#struct_0_86480_74578_485834496}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication lan-access**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x667337347}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x1029222085}
:::

**[ ]{lang="EN-US"}**

[**[authentication lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_x519115565}[命令用来为]{style="font-family:
宋体"}[lan-access]{lang="EN-US"}[用户配置认证方法。]{style="font-family:
宋体"}

[**[undo authentication lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1157596935}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1545234635}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1466732118}[模式下：]{style="font-family:宋体"}

[**[authentication lan-access]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x303977784}**[ldap-scheme ]{lang="EN-US"}***[ldap-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo authentication lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_2087407520}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_89508168}[模式下：]{style="font-family:宋体"}

[**[authentication lan-access]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x922592637}**[ldap-scheme ]{lang="EN-US"}***[ldap-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}

[**[undo authentication lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_525789806}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1976416123}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_1157662471}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x360301678}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x163605115}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2129237876}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_293380000}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1816790930}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1404697401}

[**[ldap-scheme ]{lang="EN-US"}***[ldap-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1713900497}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_1936917508}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1158121224}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x1721651115}[ *radius-scheme-name*]{lang="DE"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x704787848}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_1731219289}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1374009967}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1927515763}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1276613672}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication lan-access local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1158186760}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x928552622}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication lan-access radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_870705773}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_795974468}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x48482222}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="DE"}**]{#struct_0_86480_74578_706239546}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x1148092178}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1967153526}
:::::

::: {#1019136450 .myid}
[]{#_Toc404792537}[]{#struct_0_86480_74578_1264300412}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication login**

------------------------------------------------------------------------

[**[authentication login]{lang="EN-US"}**]{#struct_0_86480_74578_1158252296}[命令用来为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication login]{lang="EN-US"}**]{#struct_0_86480_74578_x174769132}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x513349326}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_525140630}[模式下：]{style="font-family:宋体"}

[**[authentication login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **ldap-scheme** *ldap-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x317761297}

[**[undo authentication login]{lang="EN-US"}**]{#struct_0_86480_74578_x1113366994}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2110949688}[模式下：]{style="font-family:宋体"}

[**[authentication login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **ldap-scheme** *ldap-scheme-name* \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1315907472}

[**[undo authentication login]{lang="EN-US"}**]{#struct_0_86480_74578_924285084}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158317832}

[[login]{lang="EN-US"}]{#struct_0_86480_74578_986313978}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_572146048}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1462557865}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1098778696}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x737830552}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1688345837}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1351632144}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1158383368}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[ldap-scheme]{lang="EN-US"}**[ *ldap-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_x566638751}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_2042985650}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x838674378}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_1998721130}[ *radius-scheme-name*]{lang="DE"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_318956468}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_1625244089}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2041012653}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1873064412}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1158448904}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication login local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1305856357}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[login]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x369554405}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication login radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2003891089}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x1078490364}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1859473446}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x38949974}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1158514440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1711123970}
:::

::: {#-1618392496 .myid}
[]{#_Toc404792538}[]{#struct_0_86480_74578_x687830197}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication portal**

------------------------------------------------------------------------

[**[authentication portal]{lang="EN-US"}**]{#struct_0_86480_74578_x687764661}[命令用来为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication portal]{lang="EN-US"}**]{#struct_0_86480_74578_64427898}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_301812896}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2081726818}[模式下：]{style="font-family:宋体"}

[**[authentication portal ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1873587193}

[**[undo authentication portal]{lang="EN-US"}**]{#struct_0_86480_74578_883612931}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2122145535}[模式下：]{style="font-family:宋体"}

[**[authentication portal ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x687961269}

[**[undo authentication portal]{lang="EN-US"}**]{#struct_0_86480_74578_1231862247}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1637155507}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_21280345}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x586722986}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1968069598}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x687895733}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_424447095}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_86716252}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_259294178}

[**[ldap-scheme]{lang="EN-US"}**[ *ldap-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_x1976773057}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x461367093}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1032802601}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x687568053}[ *radius-scheme-name*]{lang="DE"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1470521355}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1397397816}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1145854218}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1958055839}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x620096959}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication portal local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x687502517}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1098425453}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication portal radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_69939532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x303437247}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x642691273}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1823376941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x688092340}
:::

::::: {#-138050318 .myid}
[]{#_Toc205699645}[]{#_Toc162860237}[]{#_Toc147117554}[]{#_Toc147049914}[]{#_Toc146447634}[]{#_Toc268769712}[]{#_Toc229972067}[]{#_Toc404792539}[]{#struct_0_86480_74578_1494868668}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication ppp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x702237997}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x520008055}
:::

**[ ]{lang="EN-US"}**

[**[authentication ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x967006904}[命令用来为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x1135027198}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_553532402}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1023921717}[模式下：]{style="font-family:宋体"}

[**[authentication ppp]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_1158579976}**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] ]{lang="EN-US"}[\| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* ]{lang="EN-US"}[\[ **hwtacacs-scheme** *hwtacacs-scheme-name* \]]{lang="EN-US"}[ \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo authentication ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x1425189722}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x643457263}[模式下：]{style="font-family:宋体"}

[**[authentication ppp]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_x1621833140}**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] ]{lang="EN-US"}[\| **local** \| **radius-scheme** *radius-scheme-name* ]{lang="EN-US"}[\[ **hwtacacs-scheme** *hwtacacs-scheme-name* \]]{lang="EN-US"}[ \[ **local** \] }]{lang="EN-US"}

[**[undo authentication ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x306902812}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1508313234}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_1537847150}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x358435258}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_90745733}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1157596936}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1545431243}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1471760408}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1365269239}

[**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1294027429}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x1387082422}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x1743480527}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_699932289}[ *radius-scheme-name*]{lang="DE"}[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1157662472}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x360236142}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x223421376}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_93615608}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1744192756}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication ppp local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_356735619}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_852756113}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication ppp radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_664388033}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_1158121221}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1721323435}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1778549998}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1449728759}
:::::

::: {#2080518176 .myid}
[]{#_Toc404792540}[]{#struct_0_86480_74578_x1950246700}[]{#_Toc391364202}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication sslvpn**

------------------------------------------------------------------------

[**[authentication sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1393809898}[命令用来为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置认证方法。]{style="font-family:宋体"}

[**[undo authentication sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_1062801587}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_778636655}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2129151683}[模式下：]{style="font-family:宋体"}

[**[authentication sslvpn ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x815490143}

[**[undo authentication sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_258724513}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1527230902}[模式下：]{style="font-family:宋体"}

[**[authentication sslvpn ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x547146719}

[**[undo authentication sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_1606047015}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x564756037}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_2138889477}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1486604330}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1994112062}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1321636006}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1385668542}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1593950804}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1442385746}

[**[ldap-scheme ]{lang="EN-US"}***[ldap-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_326725872}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_495625778}[：本地认证。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x1456414709}[：不进行认证。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="EN-US"}***[radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_569722405}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}[radius-scheme-name]{lang="EN-US"}[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1791288749}

[[可以指定一个或多个备选的认证方法，在当前的认证方法无效时按照配置顺序尝试使用备选的方法完成认证。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x228217757}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证无效则进行本地认证，若本地认证也无效则不进行认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1134932551}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_771030319}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置认证方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1435660941}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication sslvpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_923670380}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案]{style="font-family:宋体"}[ldp]{lang="EN-US"}[进行认证，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选认证方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1961777315}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authentication sslvpn ldap-scheme ldp local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1229729487}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_86480_74578_x755217174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_903332260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x1229316996}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1538217078}
:::

::: {#-1964574916 .myid}
[]{#_Toc404792541}[]{#struct_0_86480_74578_x1578768302}

**AAA \-- ISP域中实现AAA配置命令 \-- authentication super**

------------------------------------------------------------------------

[**[authentication super]{lang="EN-US"}**]{#struct_0_86480_74578_x1548750066}[命令用来配置用户角色切换认证方法。]{style="font-family:宋体"}

[**[undo authentication super]{lang="EN-US"}**]{#struct_0_86480_74578_1121901249}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1437751464}

[**[authentication super]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \| **radius-scheme** *radius-scheme-name* } \*]{lang="EN-US"}]{#struct_0_86480_74578_x414779263}

[**[undo authentication super ]{lang="EN-US"}**]{#struct_0_86480_74578_1158186757}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x928356011}

[[用户角色切换认证采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x308078654}[域的缺省认证方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x289106607}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_537275805}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x526090289}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x159514517}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1029513215}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158252293}

[**[hwtacacs-scheme]{lang="EN-US"}**[ *hwtacacs-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_x174572524}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="DE"}**]{#struct_0_86480_74578_197520276}*[radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1491082881}

[[可以指定一个备选的认证方法，在当前的认证方法无效时尝试使用备选的方法完成认证。]{style="font-family:宋体"}]{#struct_0_86480_74578_1095462767}

[[目前，远程方案只能支持对名称为]{style="font-family:宋体"}[level-*n*]{lang="EN-US"}]{#struct_0_86480_74578_x2030276879}[的用户角色之间的切换进行认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{style="font-family:宋体"}]{#struct_0_86480_74578_275950619}[HWTACACS]{lang="EN-US"}[方案进行用户角色切换认证时，系统使用用户输入的用户角色切换用户名进行角色切换认证，]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上也必须存在相应的用户名，该用户名代表了能够切换到的最大级别。例如，用户希望切换到用户角色]{style="font-family:宋体"}[level-3]{lang="EN-US"}[，输入的用户名为"]{style="font-family:宋体"}[test]{lang="EN-US"}["，在要求携带域名认证的情况下，系统使用用户名"]{style="font-family:宋体"}[test@*domain-name*]{lang="EN-US"}["进行用户角色切换认证；在要求不携带域名认证的情况下使用"]{style="font-family:宋体"}[test]{lang="EN-US"}["进行用户角色切换认证。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当使用]{style="font-family:宋体"}]{#struct_0_86480_74578_206069001}[RADIUS]{lang="EN-US"}[方案进行用户角色切换认证时，系统使用"]{style="font-family:宋体"}[\$enab*n*\$]{lang="EN-US"}["形式的用户名进行用户角色切换认证，其中]{style="font-family:宋体"}*[n]{lang="EN-US"}*[为用户希望切换到的用户角色]{style="font-family:宋体"}[level-*n*]{lang="EN-US"}[中的]{style="font-family:宋体"}*[n]{lang="EN-US"}*[，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器上也必须存在相同形式的用户名。例如，用户希望切换到用户角色]{style="font-family:宋体"}[level-3]{lang="EN-US"}[，输入任意用户名，系统忽略用户输入的用户名，使用"]{style="font-family:宋体"}[\$enab3\$@*domain-name*]{lang="EN-US"}["或"]{style="font-family:宋体"}[\$enab3\$]{lang="EN-US"}["形式的用户名进行用户角色切换认证（是否携带域名由]{style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[命令决定）。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1410709618}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1158317829}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置使用]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[tac]{lang="EN-US"}[进行用户角色切换认证。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_985593081}

[\[Sysname\] super authentication-mode scheme]{lang="EN-US"}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-domain-test\] authentication super hwtacacs-scheme tac]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_480527363}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authentication default]{lang="EN-US"}**]{#struct_0_86480_74578_x319972719}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1294997043}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1873615283}
:::

::::: {#-1614274227 .myid}
[]{#_Toc404792542}[]{#struct_0_86480_74578_x797765617}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization advpn**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x1602780137}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_1285947093}
:::

**[ ]{lang="EN-US"}**

[**[authorization advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x798355442}[命令用来为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1399815248}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2077653476}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x842162842}[模式下：]{style="font-family:宋体"}

[**[authorization advpn]{lang="EN-US"}**[ { **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1245194129}

[**[undo authorization advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x321294007}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1551052362}[模式下：]{style="font-family:宋体"}

[**[authorization advpn]{lang="EN-US"}**[ { **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1660894176}

[**[undo authorization advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1468979914}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x516661870}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x798289906}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_581241871}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x455370372}[域视图]{style="font-family:宋体"}

[[【支持的缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x726207953}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1713146903}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1541345733}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_199176075}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_1660246097}[：本地计费。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_1676742568}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_265952725}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_412280954}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x408799516}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x798486514}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1759965349}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1474716302}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1309470792}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization advpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1435425939}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行计费，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选计费方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_308927536}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization advpn radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1311525453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_1013600440}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x1719991073}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x2038672175}
:::::

::: {#854012426 .myid}
[]{#_Toc404792543}[]{#struct_0_86480_74578_x362605343}[]{#_Toc268769713}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization command**

------------------------------------------------------------------------

[**[authorization command]{lang="EN-US"}**]{#struct_0_86480_74578_2003527825}[命令用来配置命令行授权方法。]{style="font-family:宋体"}

[**[undo authorization command]{lang="EN-US"}**]{#struct_0_86480_74578_1158383365}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x566835359}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1900386101}[模式下：]{style="font-family:宋体"}

[**[authorization command]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** }]{lang="EN-US"}]{#struct_0_86480_74578_x1565632076}

[**[undo authorization command]{lang="EN-US"}**]{#struct_0_86480_74578_x384040057}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x2094578687}[模式下：]{style="font-family:宋体"}

[**[authorization command]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **local** \] \| **local** }]{lang="EN-US"}]{#struct_0_86480_74578_2058161543}

[**[undo authorization command]{lang="EN-US"}**]{#struct_0_86480_74578_427467664}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x125182872}

[[命令行授权采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1158448901}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1306184037}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x2080836042}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x666524246}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1694561172}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1252269205}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x182865031}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1472951178}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_1158514437}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x1710796287}[：不授权。用户执行角色所允许的命令时，无须接受授权服务器的检查。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_433989110}

[[命令行授权是指，用户执行的每一条命令都需要接受授权服务器的检查，只有授权成功的命令才被允许执行。用户登录后可以执行的命令受登录授权的用户角色和命令行授权的用户角色的双重限制，即，仅登录授权的用户角色和命令行授权的用户角色均允许执行的命令行，才能被执行。需要注意的是，命令行授权功能只利用角色中的权限规则对命令行执行权限检查，不进行其它方面的权限检查，例如资源控制策略等。]{style="font-family:宋体"}]{#struct_0_86480_74578_1513916949}

[[对用户采用本地命令行授权时，设备将根据用户登录设备时输入的用户名对应的本地用户配置来对用户输入的命令进行检查，只有本地用户中配置的授权用户角色所允许的命令才被允许执行。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1396052681}

[[可以指定一个或多个备选的命令行授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成命令授权。例如，]{style="font-family:宋体"}**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*[ **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1424993114}[表示，先进行]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_466905501}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1131972046}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置命令行授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x2092827346}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization command local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_620525358}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置使用]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[hwtac]{lang="EN-US"}[进行命令行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_613847440}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization command hwtacacs-scheme hwtac local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1432083290}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1157596933}[（基础命令参考]{lang="EN-US" style="font-family:宋体"}[/]{lang="EN-US"}[登录设备）]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1545103563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x293744863}
:::

::: {#1267095320 .myid}
[]{#_Toc404792544}[]{#struct_0_86480_74578_714471602}[]{#_Toc268769714}[]{#_Toc205699646}[]{#_Toc162860238}[]{#_Toc147117555}[]{#_Toc147049915}[]{#_Toc146447635}[]{#_Toc125946364}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization default**

------------------------------------------------------------------------

[**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_16936423}[命令用来为当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域配置缺省的授权方法。]{style="font-family:宋体"}

[**[undo authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_65560504}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1344607343}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_269941897}[模式下：]{style="font-family:宋体"}

[**[authorization default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x391534632}

[**[undo authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_1157662469}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x360825965}[模式下：]{style="font-family:宋体"}

[**[authorization default]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x180655923}

[**[undo authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_x942109647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2146314810}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x82877371}[域的缺省授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1849777997}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x2884505}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_282224173}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1158121222}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1721257899}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1540487171}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x49742775}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x444622141}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_311437406}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。此时，认证通过的]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户（通过]{style="font-family:宋体"}[Console/AUX/]{lang="EN-US"}[异步串口或者]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[访问设备的用户）只有系统所给予的缺省用户角色，其中]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户的工作目录是设备的根目录，但并无访问权限；认证通过的非]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户可直接访问网络。关于缺省用户角色的详细介绍请参见"基础配置指导"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x894710104}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1901451704}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x150383221}[域的缺省的授权方法对于该域中未指定具体授权方法的所有接入用户都起作用，但是如果某类型的用户不支持指定的授权方法，则该授权方法对于这类用户不能生效。]{style="font-family:宋体"}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1158186758}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x928028331}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1118722739}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1403670228}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置缺省授权方法为使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_2073124689}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization default radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x628622695}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_165210840}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x378156599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1158252294}
:::

::: {#1125183885 .myid}
[]{#_Toc404792545}[]{#struct_0_86480_74578_1956886942}[]{#_Toc359405565}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization ipoe**

------------------------------------------------------------------------

[**[authorization ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1379047317}[命令用来为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_155299110}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x446451890}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1956821406}[模式下：]{style="font-family:宋体"}

[**[authorization ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x677138578}**[local ]{lang="EN-US"}**[\[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\] \|]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] \[]{lang="EN-US"}**[ none ]{lang="EN-US"}**[\]]{lang="EN-US"}**[ ]{lang="EN-US"}**[}]{lang="EN-US"}

[**[undo authorization ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_1956755870}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1010508368}[模式下：]{style="font-family:宋体"}

[**[authorization ipoe]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1133658760}**[local ]{lang="EN-US"}**[\|]{lang="EN-US"}**[ radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ \[]{lang="EN-US"}**[ local ]{lang="EN-US"}**[\] }]{lang="EN-US"}

[**[undo authorization ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_1956690334}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x271506228}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_128040448}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1957149086}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x312715993}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1073229978}

[[network-admin]{lang="FR"}]{#struct_0_86480_74578_1957083550}

[[mdc-admin]{lang="FR"}]{#struct_0_86480_74578_x615856317}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_863157335}

[**[local]{lang="FR"}**]{#struct_0_86480_74578_1957018014}[：]{style="font-family:宋体"}[本地授权。]{style="font-family:宋体"}

[**[none]{lang="FR"}**]{#struct_0_86480_74578_x1869559320}[：]{style="font-family:宋体"}[不授权。]{style="font-family:宋体"}

[**[radius-scheme]{lang="FR"}**]{#struct_0_86480_74578_1694826497}*[ radius-scheme-name]{lang="FR"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="FR"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="FR"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1956952478}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_879704759}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}]{#struct_0_86480_74578_x419109161}**[radius-scheme]{lang="EN-US"}**[ ]{lang="EN-US"}*[radius-scheme-name]{lang="EN-US"}*[ ]{lang="EN-US"}**[local]{lang="EN-US"}**[ ]{lang="EN-US"}**[none]{lang="EN-US"}**[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1957411230}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1042305037}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x155762656}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization ipoe local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1957345694}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_153542182}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization ipoe radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x583717437}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_x1374838054}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x2098713690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x583782973}
:::

::::: {#-1568924054 .myid}
[]{#_Toc268769716}[]{#_Toc205699648}[]{#_Toc162860240}[]{#_Toc147117557}[]{#_Toc147049917}[]{#_Toc146447637}[]{#_Toc125946366}[]{#_Toc404792546}[]{#struct_0_86480_74578_x174900204}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization lan-access**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x144768284}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x814500271}
:::

**[ ]{lang="EN-US"}**

[**[authorization lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1407111809}[命令用来为]{style="font-family:
宋体"}[lan-access]{lang="EN-US"}[用户配置授权方法。]{style="font-family:
宋体"}

[**[undo authorization lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_717199462}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1888555304}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x982295053}[模式下：]{style="font-family:宋体"}

[**[authorization lan-access]{lang="EN-US"}**[ { **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x953840822}

[**[undo authorization lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_1158317830}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_986182906}[模式下：]{style="font-family:宋体"}

[**[authorization lan-access]{lang="EN-US"}**[ { **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x2036448731}

[**[undo authorization lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_2099268135}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1504991471}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_92150592}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x319215987}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1372008388}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2103930841}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1158383366}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x567031967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1616745720}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x70294894}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_238065306}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户可直接访问网络。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x1069287782}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x137205200}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_711891690}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1614293570}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1158448902}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1305987429}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_766279826}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization lan-access local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1545038682}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1921247766}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization lan-access radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x919945335}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_863252690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1158514438}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1711648255}
:::::

::: {#77353551 .myid}
[]{#_Toc404792547}[]{#struct_0_86480_74578_x1136069666}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization login**

------------------------------------------------------------------------

[**[authorization login]{lang="EN-US"}**]{#struct_0_86480_74578_165573386}[命令用来为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization login]{lang="EN-US"}**]{#struct_0_86480_74578_x37501224}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1876563251}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1326480569}[模式下：]{style="font-family:宋体"}

[**[authorization login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1146669460}

[**[undo authorization login]{lang="EN-US"}**]{#struct_0_86480_74578_x966042367}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1158579974}[模式下：]{style="font-family:宋体"}

[**[authorization login]{lang="EN-US"}**[ { **hwtacacs-scheme** *hwtacacs-scheme-name* \[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **hwtacacs-scheme** *hwtacacs-scheme-name* \] \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1425058650}

[**[undo authorization login]{lang="EN-US"}**]{#struct_0_86480_74578_x1537946959}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1954266701}

[[login]{lang="EN-US"}]{#struct_0_86480_74578_243427761}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1515235976}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1604084538}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_671741528}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_916931716}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1157596934}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1545300171}

[**[hwtacacs-scheme]{lang="EN-US"}***[ hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1670595577}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_636457521}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x833192824}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。此时，认证通过的]{style="font-family:宋体"}[Login]{lang="EN-US"}[用户（通过]{style="font-family:宋体"}[Console/AUX/]{lang="EN-US"}[异步串口或者]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[访问设备的用户）只有系统所给予的缺省用户角色，其中]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户的工作目录是设备的根目录，但并无访问权限。关于缺省用户角色的详细介绍请参见"基础配置指导"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_1680264004}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x375567841}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_113133931}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_1015432572}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1157662470}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x360367214}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[login]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x200388319}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization login local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1607505370}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[login]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1347786166}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization login radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1526950818}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_x2047266121}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1214531770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1539697663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x2129152255}
:::

::: {#551238453 .myid}
[]{#_Toc404792548}[]{#struct_0_86480_74578_878188212}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization portal**

------------------------------------------------------------------------

[**[authorization portal]{lang="EN-US"}**]{#struct_0_86480_74578_x1332500274}[命令用来为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization portal]{lang="EN-US"}**]{#struct_0_86480_74578_1632929708}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x95730640}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_878515892}[模式下：]{style="font-family:宋体"}

[**[authorization portal ]{lang="EN-US"}**[{ **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1547834301}

[**[undo authorization portal]{lang="EN-US"}**]{#struct_0_86480_74578_x1268293900}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_2118647202}[模式下：]{style="font-family:宋体"}

[**[authorization portal ]{lang="EN-US"}**[{ **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x7049855}

[**[undo authorization portal]{lang="EN-US"}**]{#struct_0_86480_74578_878581428}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1098015846}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_1543091842}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_624539764}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_435936939}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_877991605}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_647105373}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_425626656}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_461919412}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_878057141}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x978254511}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户可直接访问网络。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_1198642248}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1343852751}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_544489416}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_877860533}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2070107077}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x861287613}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1444106462}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization portal local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_711100439}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_877926069}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization portal radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1060523736}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_x607997703}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1002393495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_504213355}
:::

::::: {#625890479 .myid}
[]{#_Toc404792549}[]{#struct_0_86480_74578_1767523347}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization ppp**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_723497205}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_2026497457}
:::

**[ ]{lang="EN-US"}**

[**[authorization ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x2008042683}[命令用来为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization ppp]{lang="EN-US"}**]{#struct_0_86480_74578_2117546908}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214466234}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1505413865}[模式下：]{style="font-family:宋体"}

[**[authorization ppp]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_308915912}**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] \[ **none** \] ]{lang="EN-US"}[\| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* ]{lang="EN-US"}[\[ **hwtacacs-scheme** *hwtacacs-scheme-name* \]]{lang="EN-US"}[ \[ **local** \] \[ **none** \] }]{lang="EN-US"}

[**[undo authorization ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x76398954}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x165809817}[模式下：]{style="font-family:宋体"}

[**[authorization ppp]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_560853386}**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **radius-scheme** *radius-scheme-name* \] \[ **local** \] ]{lang="EN-US"}[\| **local** \| **radius-scheme** *radius-scheme-name* ]{lang="EN-US"}[\[ **hwtacacs-scheme** *hwtacacs-scheme-name* \]]{lang="EN-US"}[ \[ **local** \] }]{lang="EN-US"}

[**[undo authorization ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x1672028209}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x768434507}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_x1034751057}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1831881483}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1214400698}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x657173977}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_957846577}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1615900666}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1498217469}

[**[hwtacacs-scheme ]{lang="EN-US"}***[hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1537623299}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。其中]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_1647608972}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x403904410}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权。]{style="font-family:宋体"}

[**[radius-scheme]{lang="DE"}**]{#struct_0_86480_74578_x983841740}*[ radius-scheme-name]{lang="DE"}*[：]{style="font-family:宋体"}[指定]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214335162}

[[在一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_925762243}[域中，只有配置的认证和授权方法中引用了相同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案时，]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权过程才能生效。]{style="font-family:宋体"}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_x287811266}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1503050247}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x368630803}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1175200134}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization ppp local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1317063354}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[rd]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1214269626}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization ppp radius-scheme rd local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x676350941}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}**]{#struct_0_86480_74578_1102643769}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1268076793}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_657056601}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1380461985}
:::::

::: {#-2141635009 .myid}
[]{#_Toc404792550}[]{#struct_0_86480_74578_x1950050092}[]{#_Toc391364204}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization sslvpn**

------------------------------------------------------------------------

[**[authorization sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x171766232}[命令用来为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置授权方法。]{style="font-family:宋体"}

[**[undo authorization sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_57327175}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1995593968}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_97344517}[模式下：]{style="font-family:宋体"}

[**[authorization sslvpn ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \[ **none** \] \| **local** \[ **none** \] \| **none** \| **radius-scheme** *radius-scheme-name* \[ **local** \] \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_581734823}

[**[undo authorization sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x1485268705}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_839576018}[模式下：]{style="font-family:宋体"}

[**[authorization sslvpn ]{lang="EN-US"}**[{ **ldap-scheme** *ldap-scheme-name* \[ **local** \] \| **local** \| **radius-scheme** *radius-scheme-name* \[ **local** \] }]{lang="EN-US"}]{#struct_0_86480_74578_1942319659}

[**[undo authorization sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_778833263}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_452752469}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_1087851660}[用户采用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域缺省授权方法。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_872344331}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_744925908}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x412335223}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_713437199}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1127250270}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1917458940}

[**[ldap-scheme ]{lang="EN-US"}***[ldap-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1168800813}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[ldap-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[local]{lang="EN-US"}**]{#struct_0_86480_74578_x739524988}[：本地授权。]{style="font-family:宋体"}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x1728037460}[：不授权。接入设备不请求授权信息，不对用户可以使用的操作以及用户允许使用的网络服务进行授权，认证通过的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户可以直接访问网络。]{style="font-family:宋体"}

[**[radius-scheme ]{lang="EN-US"}***[radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_609223307}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}[radius-scheme-name]{lang="EN-US"}[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x316482280}

[[可以指定一个或多个备选的授权方法，在当前的授权方法无效时按照配置顺序尝试使用备选的方法完成授权。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **local** **none**]{lang="EN-US"}]{#struct_0_86480_74578_411560303}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[授权无效则进行本地授权，若本地授权也无效则不进行授权。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2026532070}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1649885798}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，为]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户配置授权方法为]{style="font-family:宋体"}**[local]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1268371435}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization sslvpn local]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_161937954}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户使用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案]{style="font-family:宋体"}[ldp]{lang="EN-US"}[进行授权，并且使用]{style="font-family:宋体"}**[local]{lang="EN-US"}**[作为备选授权方法。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1000845895}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization sslvpn ldap-scheme ldp local]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1324258832}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[authorization default]{lang="EN-US"}[ ]{lang="EN-US"}**]{#struct_0_86480_74578_x1606366321}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1061273509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_2032220134}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1216411561}
:::

::: {#306714968 .myid}
[]{#_Toc268769725}[]{#_Toc205699657}[]{#_Toc162860246}[]{#_Toc147117563}[]{#_Toc147049923}[]{#_Toc146447643}[]{#_Toc69900455}[]{#_Toc404792551}[]{#struct_0_86480_74578_x1480833232}[]{#_Toc335845110}

**AAA \-- ISP域中实现AAA配置命令 \-- authorization-attribute（ISP domain view）**

------------------------------------------------------------------------

[**[authorization-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_1438040856}[命令用来设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域下的用户授权属性。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ **authorization-attribute**]{lang="EN-US"}]{#struct_0_86480_74578_x1164700386}[命令用来删除配置的授权属性，恢复用户具有的缺省访问权限。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x329162712}

[**[authorization-attribute ]{lang="EN-US"}**[{ **acl** *acl-number* \| **car** **inbound** **cir** *committed-information-rate* \[ **pir** *peak-information-rate* \] **outbound cir** *committed-information-rate* \[ **pir** *peak-information-rate* \] \| **idle-cut** *minute* \[ *flow* \] \| **igmp max-access-number** *number* \| **ip-pool** *pool-name* \| **ipv6-pool** *ipv6-pool-name* \| **ipv6-prefix** *ipv6-prefix prefix-length*]{lang="EN-US"}]{#struct_0_86480_74578_x1214204090}**[ ]{lang="EN-US"}**[\| **mld max-access-number** *number* \| { **primary-dns** \| **secondary-dns** } { **ip** *ipv4-address* \| **ipv6** *ipv6-address* } \| **session-group-profile** *session-group-profile-name* \| **url** *url-string* \| **user-group** *user-group-name* \| **user-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* }]{lang="EN-US"}

[**[undo authorization-attribute ]{lang="EN-US"}**[{ **acl** \| **car** \| **idle-cut** \| **igmp** \| **ip-pool** \| **ipv6-pool** \| **ipv6-prefix** \| **mld** \| **primary-dns** \| **secondary-dns** \| **session-group-profile** \| **url** \| **user-group** \| **user-profile** \| **vpn-instance** }]{lang="EN-US"}]{#struct_0_86480_74578_x465916599}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1553587540}

[[未对当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1525478444}[域下的用户设置任何授权属性，其中用户闲置切换功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1124325423}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_670488116}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_138837001}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1238272106}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x983822097}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214138554}

[**[acl ]{lang="EN-US"}***[acl]{lang="EN-US"}[-number]{lang="EN-US"}*]{#struct_0_86480_74578_x161953519}[：指定用于匹配用户流量的]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。其中]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[表示]{style="font-family:宋体"}[ACL]{lang="EN-US"}[编号，]{style="font-family:宋体"}[取值范围]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[。]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[用户认证成功后，将仅被授权访问指定的]{style="font-family:宋体"}[IPv4/IPv6 ACL]{lang="EN-US"}[网络资源。]{style="font-family:宋体"}[IPv4/IPv6 Portal]{lang="EN-US"}[用户在认证前，若被授权认证域，则将被授权访问指定的]{style="font-family:宋体"}[IPv4/IPv6 ACL]{lang="EN-US"}[网络资源。]{style="font-family:宋体"}

[**[car]{lang="EN-US"}**]{#struct_0_86480_74578_x44400773}[：指定授权用户的流量监管动作。]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户在认证前，若被授权认证域，则其流量将受到指定的流量监管动作控制。]{style="font-family:宋体"}

[**[inbound]{lang="EN-US"}**]{#struct_0_86480_74578_1098303844}[：表示用户的上传速率。]{style="font-family:宋体"}

[**[outbound]{lang="EN-US"}**]{#struct_0_86480_74578_x1942881541}[：表示用户的下载速率。]{style="font-family:宋体"}

[**[cir]{lang="EN-US"}**[ *committed-information-rate*]{lang="EN-US"}]{#struct_0_86480_74578_x2024252942}[：承诺信息速率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4194303]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[pir ]{lang="EN-US"}***[peak-information-rate]{lang="EN-US"}*]{#struct_0_86480_74578_650904587}[：峰值速率，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4194303]{lang="EN-US"}[，单位为]{style="font-family:宋体"}[kbps]{lang="EN-US"}[。若不指定该参数，则表示不对峰值速率进行限制。]{style="font-family:宋体"}

[**[idle-cut ]{lang="EN-US"}***[minute]{lang="EN-US"}*]{#struct_0_86480_74578_516603497}[：指定用户的闲置切断时间。其中，]{style="font-family:宋体"}*[minute]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[600]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[*[flow]{lang="EN-US"}*]{#struct_0_86480_74578_x1959914191}[：用户在闲置切断时间内产生的数据流量，取值范围]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10240000]{lang="EN-US"}[，单位为字节，缺省值为]{style="font-family:宋体"}[10240]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[igmp max-access-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_86480_74578_1957149084}[：指定]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[用户可以同时点播的最大节目数。其中，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ip-pool ]{lang="EN-US"}***[pool-name]{lang="EN-US"}*]{#struct_0_86480_74578_856219831}[：指定为用户分配]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的地址池。其中，]{style="font-family:宋体"}*[pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ipv6-pool]{lang="EN-US"}**[ *ipv6-pool-name*]{lang="EN-US"}]{#struct_0_86480_74578_x312584921}[：指定为用户分配]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址的地址池。其中，]{style="font-family:宋体"}*[ipv6-pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ipv6-prefix]{lang="EN-US"}**[ *ipv6-prefix prefix-length*]{lang="EN-US"}]{#struct_0_86480_74578_1957083548}[：指定为用户分配的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。其中，]{style="font-family:宋体"}*[ipv6-prefix prefix-length]{lang="EN-US"}*[为前缀地址和前缀长度，前缀长度取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[mld max-access-number]{lang="EN-US"}**[ *number*]{lang="EN-US"}]{#struct_0_86480_74578_x616380604}[：指定]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[用户可以同时点播的最大节目数。其中，]{style="font-family:宋体"}*[number]{lang="EN-US"}*[的取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[primary-dns ip]{lang="EN-US"}**[ *ipv4-address*]{lang="EN-US"}]{#struct_0_86480_74578_1957018012}[：指定用户的主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[primary-dns ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_x1869690392}[：指定用户的主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[secondary-dns ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_86480_74578_1956952476}[：指定用户的从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[secondary-dns ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_880097975}[：指定用户的从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[session-group-profile ]{lang="EN-US"}***[session-group-profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_597561368}[：指定用户的授权]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[session-group-profile-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户在认证前，若被授权认证域，则其]{style="font-family:宋体"}[访问行为将受到该]{style="font-family:宋体"}[域中的]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}[配置的限制]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[url ]{lang="EN-US"}***[url-string]{lang="EN-US"}*]{#struct_0_86480_74578_x75868144}[：指定用户的强制]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。用户认证成功后，此]{style="font-family:宋体"}[URL]{lang="EN-US"}[将被推送至]{style="font-family:宋体"}[PPP]{lang="EN-US"}[客户端。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[user-group ]{lang="EN-US"}***[user-group-name]{lang="EN-US"}*]{#struct_0_86480_74578_x968522573}[：表示用户所属用户组。其中，]{style="font-family:宋体"}*[user-group-name]{lang="EN-US"}*[表示用户组名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。用户认证成功后，将继承该用户组中的所有属性。]{style="font-family:宋体"}

[**[user-profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_722258076}[：指定用户的授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}[Portal]{lang="EN-US"}[用户在认证前，若被授权认证域，则其]{style="font-family:宋体"}[访问行为将受到该]{style="font-family:宋体"}[域中的]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[配置的限制]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-nam*e]{lang="EN-US"}]{#struct_0_86480_74578_1957411228}[：指定用户所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。用户认证成功后，将被授权允许访问指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中的网络资源。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1233131965}

[[用户上线后，设备会周期性检测用户的流量，若域内某用户在指定的闲置检测时间内产生的流量小于本命令中指定的数据流量，则会被强制下线。需要注意的是，服务器上也可以配置最大空闲时间实现对用户的闲置切断功能，具体为当用户在指定的闲置检测时间内产生的流量小于]{style="font-family:宋体"}[10240]{lang="EN-US"}]{#struct_0_86480_74578_x914579357}[个字节（服务器上该阈值为固定值，不可配置）时，会被强制下线。但是，只有在设备上的闲置切断功能处于关闭状态时，服务器才会根据自身的配置来控制用户的闲置切断。]{style="font-family:宋体"}

[[如果当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1162740416}[域的用户认证成功，但认证服务器（包括本地认证下的接入设备）未对该]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域下发授权属性，则系统使用当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[下指定的授权属性为用户授权。]{style="font-family:宋体"}

[[需要注意的是，可通过多次执行本命令配置多个授权属性，但对于相同授权属性，新配置会覆盖原有的配置。]{style="font-family:宋体"}]{#struct_0_86480_74578_x2108140692}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214073018}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x2086899482}[指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下的用户闲置切断时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[分钟，闲置切断时间内产生的流量为]{style="font-family:宋体"}[10240]{lang="EN-US"}[字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x2116869066}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] authorization-attribute idle-cut 30 10240]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x31231224}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_x112006902}
:::

::: {#-24409866 .myid}
[]{#_Toc404792552}[]{#struct_0_86480_74578_x1506493713}

**AAA \-- ISP域中实现AAA配置命令 \-- display domain**

------------------------------------------------------------------------

[**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_1537475765}[命令用来显示所有或指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1624886669}

[**[display domain]{lang="EN-US"}**[ \[ *isp-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_x1215056058}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1402642223}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1722552330}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1622074253}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_224207027}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_x608028836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1977707176}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x920723725}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_250371918}

[*[isp-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1214990522}[：指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_288387509}

[[如果不指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_12890361}[域，则显示系统中所有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1683205909}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1943228182}[显示系统中所有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display domain]{lang="EN-US"}]{#struct_0_86480_74578_x1214531769}

[Total 2 domains]{lang="EN-US"}

[ ]{lang="EN-US"}

[Domain: system]{lang="EN-US"}

[  State: Active]{lang="EN-US"}

[  Default authentication scheme:  Local]{lang="EN-US"}

[  Default authorization  scheme:  Local]{lang="EN-US"}

[  Default accounting     scheme:  Local]{lang="EN-US"}

[  Accounting start failure action: Online]{lang="EN-US"}

[  Accounting update failure action: Online]{lang="EN-US"}

[  Accounting quota out action: Offline]{lang="EN-US"}

[  Service type: HSI]{lang="EN-US"}

[  Session time: Exclude idle time]{lang="EN-US"}

[  Authorization attributes :]{lang="EN-US"}

[    Idle-cut: Disabled]{lang="EN-US"}

[    IGMP access number: 4]{lang="EN-US"}

[    MLD access number:  4]{lang="EN-US"}

[ ]{lang="EN-US"}

[Domain: dm]{lang="EN-US"}

[  State: Active]{lang="EN-US"}

[  Login   authentication scheme:  RADIUS=rad]{lang="EN-US"}

[  Login   authorization  scheme:  HWTACACS=hw]{lang="EN-US"}

[  Super   authentication scheme:  RADIUS=rad]{lang="EN-US"}

[  PPP     accounting     scheme:  RADIUS=r1, (RADIUS=r2), HWTACACS=tc, Local]{lang="EN-US"}

[  Command authorization  scheme:  HWTACACS=hw]{lang="EN-US"}

[  LAN access authentication scheme:  RADIUS=r4]{lang="EN-US"}

[  Portal  authentication scheme:  LDAP=ldp]{lang="EN-US"}

[  IPoE    authentication scheme:  RADIUS=rad, Local, None]{lang="EN-US"}

[  SSL VPN authentication scheme:  LDAP=ldp, Local, None]{lang="EN-US"}

[  SSL VPN authorization  scheme:  LDAP=ldp, Local]{lang="EN-US"}

[  SSL VPN accounting     scheme:  None]{lang="EN-US"}

[  Default authentication scheme:  ldap=rad, Local, None]{lang="EN-US"}

[  Default authorization  scheme:  Local]{lang="EN-US"}

[  Default accounting     scheme:  None]{lang="EN-US"}

[  Accounting start failure action: Online]{lang="EN-US"}

[  Accounting update failure action: Online]{lang="EN-US"}

[  Accounting quota out action: Offline]{lang="EN-US"}

[  ITA service poilcy: ita1]{lang="EN-US"}

[  Service type: HIS]{lang="EN-US"}

[  Session time: Include idle time]{lang="EN-US"}

[  Authorization attributes :]{lang="EN-US"}

[    Idle-cut : Enabled]{lang="EN-US"}

[      Idle timeout: 2 minutes]{lang="EN-US"}

[      Flow: 10240 bytes]{lang="EN-US"}

[    IP pool: appy]{lang="EN-US"}

[    User profile: test]{lang="EN-US"}

[    Session group profile: abc]{lang="EN-US"}

[    Inbound CAR: CIR 64000 bps PIR 640000 bps]{lang="EN-US"}

[    Outbound CAR: CIR 64000 bps PIR 640000 bps]{lang="EN-US"}

[    ACL number]{lang="EN-US"}[：]{style="font-family:宋体"}[3000]{lang="EN-US"}

[    User group: ugg]{lang="EN-US"}

[    IPv6 prefix: 1::1/34]{lang="EN-US"}

[    IPv6 pool: ipv6pool]{lang="EN-US"}

[    Primary DNS server: 6.6.6.6]{lang="EN-US"}

[    Secondary DNS server: 3.6.2.3]{lang="EN-US"}

[    URL: http://portal]{lang="EN-US"}

[    VPN instance: vpn1]{lang="EN-US"}

[    IGMP access number: 12]{lang="EN-US"}

[    MLD access number: 35]{lang="EN-US"}

[ ]{lang="EN-US"}

[Default domain name: system]{lang="EN-US"}

[]{#struct_0_86480_74578_x382551102}[[表1-1 ]{lang="EN-US"}[display domain]{lang="EN-US"}]{#_Toc138066606}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_760945794}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_x1596212890}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214466233}

[[Total 2 domains]{lang="EN-US"}]{#struct_0_86480_74578_x2030038544}

[[总计]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_86480_74578_1772087811}[个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}

[[Domain]{lang="EN-US"}]{#struct_0_86480_74578_x1211139058}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x2031335777}[域名]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_86480_74578_x102021067}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x2049284841}[域的状态]{style="font-family:宋体"}

[[Default authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_1958770641}

[[缺省的认证方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214335161}

[[Default authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_522477716}

[[缺省的授权方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x830492954}

[[Default accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_x1327838260}

[[缺省的计费方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x1312234300}

[[Accounting start failure action]{lang="EN-US"}]{#struct_0_86480_74578_x798420980}

[[用户计费开始失败的动作，包括以下取值：]{style="font-family:宋体"}]{#struct_0_86480_74578_x650107348}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_86480_74578_x798093300}[：如果用户计费开始失败，则保持用户在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_86480_74578_x2143238289}[：如果用户计费开始失败，则强制用户下线]{lang="EN-US" style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86480_74578_x2058623525}

[[Accounting update failure max-times]{lang="EN-US"}]{#struct_0_86480_74578_x736713242}

[[允许用户连续计费更新失败的次数]{style="font-family:宋体"}]{#struct_0_86480_74578_x798027764}

[[Accounting update failure action]{lang="EN-US"}]{#struct_0_86480_74578_x597321255}

[[用户计费更新失败的动作，包括以下取值：]{style="font-family:宋体"}]{#struct_0_86480_74578_1298248003}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_86480_74578_x88361961}[：如果]{style="font-family:宋体"}[用户]{lang="EN-US" style="font-family:宋体"}[计费更新失败，则保持用户在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_86480_74578_2021332206}[：如果用户计费更新失败，则强制用户下线]{lang="EN-US" style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86480_74578_x798224372}

[[Accounting quota out action]{lang="EN-US"}]{#struct_0_86480_74578_x236324887}

[[用户计费流量配额耗尽策略，包括以下取值：]{style="font-family:宋体"}]{#struct_0_86480_74578_1581191118}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Online]{lang="EN-US"}]{#struct_0_86480_74578_x1629295636}[：如果用户]{style="font-family:宋体"}[计费流量配额]{lang="EN-US" style="font-family:宋体"}[耗尽，则保持用户在线]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_86480_74578_x798158836}[：如果用户计费流量配额耗尽，则强制用户下线]{lang="EN-US" style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86480_74578_940998858}

[[ITA service poilcy]{lang="EN-US"}]{#struct_0_86480_74578_x1413027925}

[[采用的]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x1807784790}[业务策略]{style="font-family:宋体"}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86480_74578_x356590203}

[[Service type]{lang="EN-US"}]{#struct_0_86480_74578_1956952475}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1957411227}[域的业务类型，取值为]{style="font-family:宋体"}[HIS]{lang="EN-US"}[，]{style="font-family:宋体"}[STB]{lang="EN-US"}[和]{style="font-family:宋体"}[VoIP]{lang="EN-US"}

[[Session time]{lang="EN-US"}]{#struct_0_86480_74578_x797831156}

[[设备上传到服务器的用户在线时间，有以下两种情况：]{style="font-family:宋体"}]{#struct_0_86480_74578_x815746550}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Include idle time]{lang="EN-US"}]{#struct_0_86480_74578_x2139177997}[：保留闲置切断时间]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Exclude idle time]{lang="EN-US"}]{#struct_0_86480_74578_766354970}[：扣除闲置切断时间]{lang="EN-US" style="font-family:
  宋体"}

[[ADVPN authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_x797765620}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x1602452458}[用户认证方案]{style="font-family:宋体"}

[[ADVPN authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_x1227085266}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x781897308}[用户授权方案]{style="font-family:宋体"}

[[ADVPN accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_x798355445}

[[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x1400011856}[用户计费方案]{style="font-family:宋体"}

[[Login authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_x1970674694}

[[Login]{lang="EN-US"}]{#struct_0_86480_74578_x1214269625}[用户认证方案]{style="font-family:宋体"}

[[Login authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_x273066414}

[[Login]{lang="EN-US"}]{#struct_0_86480_74578_774094140}[用户授权方案]{style="font-family:宋体"}

[[Login accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_204316627}

[[Login]{lang="EN-US"}]{#struct_0_86480_74578_x1214204089}[用户计费方案]{style="font-family:宋体"}

[[Authorization attributes]{lang="EN-US"}]{#struct_0_86480_74578_1456332166}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1880833020}[的用户授权属性]{style="font-family:宋体"}

[[Idle-cut]{lang="EN-US"}]{#struct_0_86480_74578_x222625327}

[[用户闲置切断功能，包括以下取值：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1869044793}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_86480_74578_x1214138553}[：处于使能状态，表示当]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中的用户在指定的最大闲置切断时间内产生的流量小于指定的最小数据流量时，会被强制下线。]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_86480_74578_x242911390}[：处于关闭状态，表示不对用户进行闲置切断控制，它为缺省状态]{style="font-family:宋体"}

[[Idle timeout]{lang="EN-US"}]{#struct_0_86480_74578_167806551}

[[用户闲置切断时间（单位为分钟）]{style="font-family:宋体"}]{#struct_0_86480_74578_2065273560}

[[Flow]{lang="EN-US"}]{#struct_0_86480_74578_x2065128236}

[[用户数据流量阈值（单位为字节）]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214073017}

[[IP pool]{lang="EN-US"}]{#struct_0_86480_74578_1092322567}

[[授权]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_86480_74578_x307269736}[地址池的名称]{style="font-family:宋体"}

[[User profile]{lang="EN-US"}]{#struct_0_86480_74578_293276208}

[[授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_86480_74578_x1215056057}[的名称]{style="font-family:宋体"}

[[Session group profile]{lang="EN-US"}]{#struct_0_86480_74578_597626904}

[[授权]{style="font-family:宋体"}[Session Group Profile]{lang="EN-US"}]{#struct_0_86480_74578_x968457037}[的名称]{style="font-family:宋体"}

[[Inbound CAR]{lang="EN-US"}]{#struct_0_86480_74578_x2082713214}

[[授权的入方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_86480_74578_x800982466}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Outbound CAR]{lang="EN-US"}]{#struct_0_86480_74578_x565172510}

[[授权的出方向]{style="font-family:宋体"}[CAR]{lang="EN-US"}]{#struct_0_86480_74578_x972682763}[（]{style="font-family:宋体"}[CIR]{lang="EN-US"}[：平均速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[；]{style="font-family:宋体"}[PIR]{lang="EN-US"}[：峰值速率，单位为]{style="font-family:宋体"}[bps]{lang="EN-US"}[）]{style="font-family:宋体"}

[[ACL number]{lang="EN-US"}]{#struct_0_86480_74578_x2131256451}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_86480_74578_x449417027}[编号]{style="font-family:宋体"}

[[User group]{lang="EN-US"}]{#struct_0_86480_74578_28756553}

[[授权]{style="font-family:宋体"}[User group]{lang="EN-US"}]{#struct_0_86480_74578_x2084202284}[的名称]{style="font-family:宋体"}

[[IPv6 prefix]{lang="EN-US"}]{#struct_0_86480_74578_1957149090}

[[授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_1957083554}[前缀]{style="font-family:宋体"}

[[IPv6 pool]{lang="EN-US"}]{#struct_0_86480_74578_1957018018}

[[授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_1956952482}[地址池的名称]{style="font-family:宋体"}

[[Primary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_1957345698}

[[授权主]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_1956886945}[服务器地址]{style="font-family:宋体"}

[[Secondary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_1956821409}

[[授权从]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_1956755873}[服务器地址]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_86480_74578_1956690337}

[[授权强制]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_1957149089}

[[VPN instance]{lang="EN-US"}]{#struct_0_86480_74578_1957083553}

[[授权]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_1957018017}[实例名称]{style="font-family:宋体"}

[[IGMP max access number]{lang="EN-US"}]{#struct_0_86480_74578_1956952481}

[[授权]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_86480_74578_1957411233}[用户可以同时点播的最大节目数]{style="font-family:宋体"}

[[MLD max access number]{lang="EN-US"}]{#struct_0_86480_74578_1957345697}

[[授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_221415777}[用户可以同时点播的最大节目数]{style="font-family:宋体"}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x192788642}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1680244372}[方案]{style="font-family:宋体"}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x451739512}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1214990521}[方案]{style="font-family:宋体"}

[[ldap]{lang="EN-US"}]{#struct_0_86480_74578_1854471450}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x743854099}[方案]{style="font-family:宋体"}

[[local]{lang="EN-US"}]{#struct_0_86480_74578_1259552622}

[[本地方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214531772}

[[none]{lang="EN-US"}]{#struct_0_86480_74578_376898249}

[[不认证、不授权和不计费]{style="font-family:宋体"}]{#struct_0_86480_74578_x216714385}

[[Super authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_221284705}

[[用户角色切换认证方案]{style="font-family:宋体"}]{#struct_0_86480_74578_221153633}

[[PPP authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_220957025}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_221022561}[用户的认证方案]{style="font-family:宋体"}

[[PPP authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_221874529}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_221350240}[用户的授权方案]{style="font-family:宋体"}

[[PPP accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_221284704}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_221088096}[用户的计费方案]{style="font-family:宋体"}

[[Command authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_x1214466236}

[[命令行授权方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x1626754017}

[[Command accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_851687035}

[[命令行计费方案]{style="font-family:宋体"}]{#struct_0_86480_74578_x499703880}

[[LAN access authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_221415775}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_221219167}[用户认证方案]{style="font-family:宋体"}

[[LAN access authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_221088095}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_221153631}[用户授权方案]{style="font-family:宋体"}

[[LAN access accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_220957023}

[[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_221022559}[用户计费方案]{style="font-family:宋体"}

[[Portal authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_221940063}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_221350238}[用户认证方案]{style="font-family:宋体"}

[[Portal authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_221415774}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_221284702}[用户授权方案]{style="font-family:宋体"}

[[Portal accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_221088094}

[[Portal]{lang="EN-US"}]{#struct_0_86480_74578_221153630}[用户计费方案]{style="font-family:宋体"}

[[IPoE authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_220957022}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_221022558}[用户认证方案]{style="font-family:宋体"}

[[IPoE authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_221940062}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_221350245}[用户授权方案]{style="font-family:宋体"}

[[IPoE accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_221415781}

[[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_221284709}[用户计费方案]{style="font-family:宋体"}

[[SSL VPN authentication scheme]{lang="EN-US"}]{#struct_0_86480_74578_1404261494}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_x1092183874}[用户认证方案]{style="font-family:宋体"}

[[SSL VPN authorization scheme]{lang="EN-US"}]{#struct_0_86480_74578_x161822447}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_x415823110}[用户授权方案]{style="font-family:宋体"}

[[SSL VPN accounting scheme]{lang="EN-US"}]{#struct_0_86480_74578_597692440}

[[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_x196676248}[用户计费方案]{style="font-family:宋体"}

[[Default Domain Name]{lang="EN-US"}]{#struct_0_86480_74578_650322832}

[[缺省]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1214335164}[域名]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#-365177566 .myid}
[]{#_Toc404792553}[]{#struct_0_86480_74578_119193189}[]{#_Toc268769726}[]{#_Toc205699660}[]{#_Toc162860248}[]{#_Toc147117565}[]{#_Toc147049925}[]{#_Toc146447645}[]{#_Toc69900457}[]{#_Toc299047478}[]{#_Toc299111991}[]{#_Toc299130039}[]{#_Toc299130133}[]{#_Toc299047479}[]{#_Toc299111992}[]{#_Toc299130040}[]{#_Toc299130134}[]{#_Hlt19451715}

**AAA \-- ISP域中实现AAA配置命令 \-- domain**

------------------------------------------------------------------------

[**[domain]{lang="EN-US"}**]{#struct_0_86480_74578_x372251916}[命令用来创建]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域并进入其视图。]{style="font-family:宋体"}

[**[undo domain]{lang="EN-US"}**]{#struct_0_86480_74578_x2090365631}[命令用来删除指定的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_746469640}

[**[domain]{lang="EN-US"}**[ *isp-name*]{lang="EN-US"}]{#struct_0_86480_74578_x1202522942}

[**[undo domain]{lang="EN-US"}**[ *isp-name*]{lang="EN-US"}]{#struct_0_86480_74578_25208266}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_740047492}

[[系统存在一个名称为]{style="font-family:宋体"}[system]{lang="EN-US"}]{#struct_0_86480_74578_x1987650582}[的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_2121755901}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214269628}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_842678833}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1548094917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x599074967}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2064058454}

[*[isp-name]{lang="EN-US"}*]{#struct_0_86480_74578_106378309}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符，且不能为字符串"]{style="font-family:宋体"}[d]{lang="EN-US"}["、"]{style="font-family:宋体"}[de]{lang="EN-US"}["、"]{style="font-family:宋体"}[def]{lang="EN-US"}["、"]{style="font-family:宋体"}[defa]{lang="EN-US"}["、"]{style="font-family:宋体"}[defau]{lang="EN-US"}["、"]{style="font-family:宋体"}[defaul]{lang="EN-US"}["、"]{style="font-family:宋体"}[default]{lang="EN-US"}["、"]{style="font-family:宋体"}[i]{lang="EN-US"}["、"]{style="font-family:宋体"}[if]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-u]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-un]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unk]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkn]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkno]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unknow]{lang="EN-US"}["和"]{style="font-family:宋体"}[if-unknown]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x764366539}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_782163105}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[所有的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214204092}[ISP]{lang="EN-US"}[域在创建后即处于]{style="font-family:宋体"}**[active]{lang="EN-US"}**[状态。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能删除系统中预定义的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1628716013}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[system]{lang="EN-US"}[，只能修改该域的配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能删除系统缺省的]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_247879621}[域，除非先恢复要删除的域为非缺省域，系统缺省的]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}[域的配置请参考]{lang="EN-US" style="font-family:宋体"}**[domain]{lang="EN-US"}**[ **default** **enable**]{lang="EN-US"}[命令。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能删除为未知域名的用户指定的]{lang="EN-US" style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_878581425}[域，除非首先使用命令]{lang="EN-US" style="font-family:宋体"}**[undo domain if-unknown]{lang="EN-US"}**[将其恢复为缺省情况。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x179706872}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1685143997}[创建一个新的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[，并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1624130994}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\]]{lang="EN-US"}[]{#_Hlt20817145}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2074228481}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_851149684}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain]{lang="EN-US"}**[ **default** **enable**]{lang="EN-US"}]{#struct_0_86480_74578_x1214138556}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain if-unkn]{lang="EN-US"}**]{#struct_0_86480_74578_x1850891751}**[ow]{lang="EN-US"}[n]{lang="EN-US"}**

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state]{lang="EN-US"}**]{#struct_0_86480_74578_x646195917}
:::

::: {#1975043417 .myid}
[]{#_Toc404792554}[]{#struct_0_86480_74578_460043000}[]{#_Toc268769727}[]{#_Toc205699661}[]{#_Toc162860249}[]{#_Toc147117566}[]{#_Toc147049926}[]{#_Toc146447646}

**AAA \-- ISP域中实现AAA配置命令 \-- domain default enable**

------------------------------------------------------------------------

[**[domain default enable]{lang="EN-US"}**]{#struct_0_86480_74578_x970322070}[命令用来配置系统缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域，所有在登录时没有提供]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名的用户都属于这个域。]{style="font-family:宋体"}

[**[undo domain default enable]{lang="EN-US"}**]{#struct_0_86480_74578_1364323163}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_721596862}

[**[domain]{lang="EN-US"}**[ **default** **enable** *isp-name*]{lang="EN-US"}]{#struct_0_86480_74578_x863858334}

[**[undo domain default enable]{lang="EN-US"}**]{#struct_0_86480_74578_1370520817}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1974979483}

[[系统缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1214073020}[域为]{style="font-family:宋体"}[system]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1851640846}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x62970677}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1337464901}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1419492821}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_874646586}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2086928601}

[*[isp-name]{lang="EN-US"}*]{#struct_0_86480_74578_x553706938}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1984444166}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1215056060}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[缺省的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1759069191}[ISP]{lang="EN-US"}[域有且只有一个。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定的缺省]{style="font-family:宋体"}]{#struct_0_86480_74578_x1546863176}[ISP]{lang="EN-US"}[域必须已经存在。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置为缺省的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1458918461}[ISP]{lang="EN-US"}[域不能被删除，除非先恢复要删除的域为非缺省域。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1776948422}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_574753651}[创建一个新的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[，并设置为系统缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1827829651}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] quit]{lang="EN-US"}

[\[Sysname\] domain default enable test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1106228146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_x1214990524}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[domain]{lang="EN-US"}**]{#struct_0_86480_74578_1451186923}
:::

::: {#50418192 .myid}
[]{#_Toc404792555}[]{#struct_0_86480_74578_x1851022823}[]{#_Toc335845112}

**AAA \-- ISP域中实现AAA配置命令 \-- domain if-unknown**

------------------------------------------------------------------------

[**[domain if-unknown]{lang="EN-US"}**]{#struct_0_86480_74578_x1850957287}[命令用来为未知域名的用户指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。]{style="font-family:宋体"}

[**[undo domain if-unknown]{lang="EN-US"}**]{#struct_0_86480_74578_x1630571690}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850629607}

[**[domain if-unknown]{lang="EN-US"}**[ *isp-domain-name*]{lang="EN-US"}]{#struct_0_86480_74578_67832927}

[**[undo domain if-unknown]{lang="EN-US"}**]{#struct_0_86480_74578_x479887976}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850564071}

[[没有为未知域名的用户指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1784578595}[域。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_340906493}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1850760679}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1614534919}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1850695143}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x550447997}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1405566380}

[*[isp-domain-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1850367463}[：]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[24]{lang="EN-US"}[个字符的字符串，不区分大小写，不能包括"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["]{style="font-family:宋体"} [、"]{style="font-family:宋体"}["]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["以及"]{style="font-family:宋体"}[@]{lang="EN-US"}["字符，且不能为字符串"]{style="font-family:宋体"}[d]{lang="EN-US"}["、"]{style="font-family:宋体"}[de]{lang="EN-US"}["、"]{style="font-family:宋体"}[def]{lang="EN-US"}["、"]{style="font-family:宋体"}[defa]{lang="EN-US"}["、"]{style="font-family:宋体"}[defau]{lang="EN-US"}["、"]{style="font-family:宋体"}[defaul]{lang="EN-US"}["、"]{style="font-family:宋体"}[default]{lang="EN-US"}["、"]{style="font-family:宋体"}[i]{lang="EN-US"}["、"]{style="font-family:宋体"}[if]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-u]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-un]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unk]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkn]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unkno]{lang="EN-US"}["、"]{style="font-family:宋体"}[if-unknow]{lang="EN-US"}["和"]{style="font-family:宋体"}[if-unknown]{lang="EN-US"}["。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1468175531}

[[设备将按照如下先后顺序选择认证域：接入模块指定的认证域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}]{#struct_0_86480_74578_x1850301927}[用户名中指定的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[\--\>]{lang="EN-US"}[系统缺省的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域。其中，仅部分接入模块支持指定认证域，例如]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证。]{style="font-family:宋体"}

[[如果根据以上原则决定的认证域在设备上不存在，但设备上为未知域名的用户指定了]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_685918690}[域，则最终使用该指定的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域认证，否则，用户将无法认证。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1402516599}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1850891750}[为未知域名的用户指定]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x431082926}

[\[Sysname\] domain if-unknown test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850826214}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_x1550143854}
:::

::::: {#-1581216975 .myid}
[]{#_Toc404792556}[]{#struct_0_86480_74578_x797765621}

**AAA \-- ISP域中实现AAA配置命令 \-- ita-policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 19 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x1602386922}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x1793679108}
:::

[ ]{lang="EN-US"}

[**[ita-policy]{lang="EN-US"}**]{#struct_0_86480_74578_1053176591}[命令用来指定当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域采用的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[**[undo ita-policy]{lang="EN-US"}**]{#struct_0_86480_74578_463300937}[命令用来删除当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域采用的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1580916691}

[**[ita-policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_86480_74578_1522884487}

[**[undo ita-policy]{lang="EN-US"}**]{#struct_0_86480_74578_125526131}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_972992695}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1259902563}[域中未指定]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1522827287}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_897957444}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x354737997}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x746995080}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x530533399}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1580851155}

[*[service-policy-name]{lang="EN-US"}*]{#struct_0_86480_74578_x2006390007}[：]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略名称，由]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符组成，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_508216929}

[[当]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_720451099}[服务器为当前用户动态授权了]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略时，将使用]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器授权的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略，否则使用用户认证域中指定的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[[若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_655690186}[服务器为当前用户授权了]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略，但该策略在设备上不存在，则即使认证域中指定了]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略且存在，设备也不会对该用户进行]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_535532441}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x407486011}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[中，指定采用]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1895553687}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-domain-test\] ita-policy ita1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1913718207}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_1222285547}
:::::

::: {#-1170145790 .myid}
[]{#_Toc404792557}[]{#struct_0_86480_74578_x400706606}[]{#_Toc400718938}[]{#_Toc393791496}[]{#_Toc385923038}[]{#_Toc315873175}[]{#_Toc268769734}

**AAA \-- ISP域中实现AAA配置命令 \-- nas-id bind vlan**

------------------------------------------------------------------------

[**[nas-id bind vlan]{lang="EN-US"}**]{#struct_0_86480_74578_x815539525}[命令用来设置]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[与]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定关系。]{style="font-family:宋体"}

[**[undo nas-id bind vlan]{lang="EN-US"}**]{#struct_0_86480_74578_x1370750279}[命令用来删除指定的]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[和]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定关系。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_584729065}[[【命令】]{style="font-family:黑体"}]{#_Toc400718939}

[**[nas-id ]{lang="EN-US"}***[nas-identifier]{lang="EN-US"}***[ bind vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_86480_74578_x151702769}

[**[undo nas-id ]{lang="EN-US"}***[nas-identifier]{lang="EN-US"}***[ bind vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_86480_74578_1178798452}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1165377335}

[[未设置任何绑定关系。]{style="font-family:宋体"}]{#struct_0_86480_74578_x327646161}

[]{#struct_0_86480_74578_1209276518}[[【视图】]{style="font-family:黑体"}]{#_Toc400718940}

[[NAS-ID Profile]{lang="EN-US"}]{#struct_0_86480_74578_x450163359}[视图]{style="font-family:宋体"}

[]{#struct_0_86480_74578_x2023254990}[[【缺省用户角色】]{style="font-family:黑体"}]{#_Toc400718941}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1678775070}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2105477905}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_577009086}

[*[nas-identifier]{lang="EN-US"}*]{#struct_0_86480_74578_2051154944}[：]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[*[vlan-id]{lang="EN-US"}*]{#struct_0_86480_74578_x1563506020}[：与]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[绑定的]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_897595604}[[【使用指导】]{style="font-family:黑体"}]{#_Toc400718942}

[[一个]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}]{#struct_0_86480_74578_702548829}[视图下，可以指定多个]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[与]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[的绑定关系。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}]{#struct_0_86480_74578_1209908805}[可以与多个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[绑定，但是一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[只能与一个]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[绑定。若多次将一个]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[与不同的]{style="font-family:宋体"}[NAS-ID]{lang="EN-US"}[进行绑定，则最后的绑定关系生效。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_x911947877}[[【举例】]{style="font-family:黑体"}]{#_Toc400718943}

[[\#]{lang="EN-US"}]{#struct_0_86480_74578_x1274132584}[在名称为]{style="font-family:宋体"}[aaa]{lang="EN-US"}[的]{style="font-family:宋体"}[NAS-ID Profile]{lang="EN-US"}[视图下，配置]{style="font-family:宋体"}[NAS-ID 222]{lang="EN-US"}[与]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[的绑定关系。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1113115900}

[\[Sysname\] aaa nas-id profile aaa]{lang="EN-US"}

[\[Sysname-nas-id-prof-aaa\] nas-id 222 bind vlan 2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x838351461}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[aaa nas-id profil]{lang="EN-US"}[e]{lang="EN-US"}**]{#struct_0_86480_74578_x1122734691}
:::

::: {#-1462192690 .myid}
[]{#_Toc404792558}[]{#struct_0_86480_74578_220957028}

**AAA \-- ISP域中实现AAA配置命令 \-- service-type（ISP domain view）**

------------------------------------------------------------------------

[**[service-type]{lang="EN-US"}**]{#struct_0_86480_74578_1874270084}[命令用来设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的业务类型。]{style="font-family:宋体"}

[**[undo]{lang="EN-US"}**[ ]{lang="EN-US"}]{#struct_0_86480_74578_221022564}**[service-type]{lang="EN-US"}**[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x933341649}

[**[service-type]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_221874532}**[hsi]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[stb]{lang="EN-US"}**[ \| ]{lang="EN-US"}**[voip]{lang="EN-US"}**[ }]{lang="EN-US"}

[**[undo service-type]{lang="EN-US"}**]{#struct_0_86480_74578_221940068}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1879246560}

[[当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_378478276}[域的业务类型为]{style="font-family:宋体"}**[hsi]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787434182}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1360443039}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787499718}

[[network-admin]{lang="FR"}]{#struct_0_86480_74578_1787303110}

[[mdc-admin]{lang="FR"}]{#struct_0_86480_74578_x2109406472}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787368646}

[**[hsi]{lang="FR"}**]{#struct_0_86480_74578_1787172038}[：表示高速上网业务。]{style="font-family:宋体"}

[**[stb]{lang="FR"}**]{#struct_0_86480_74578_1787237574}[：]{style="font-family:宋体"}[表示数字机顶盒接入业务。]{style="font-family:宋体"}

[**[voip]{lang="FR"}**]{#struct_0_86480_74578_x558901881}[：]{style="font-family:宋体"}[表示]{style="font-family:宋体"}[VoIP]{lang="FR"}[业务]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787040966}

[[本命令用来配置当前认证域的用户使用的业务类型，用来决定接入模块是否开启组播功能。]{style="font-family:宋体"}]{#struct_0_86480_74578_1787106502}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HSI]{lang="EN-US"}]{#struct_0_86480_74578_1017733256}[（]{style="font-family:宋体"}[High Speed Internet]{lang="EN-US"}[，高速上网）业务：主要指使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[专线方式接入网络的用户业务。用户使用该业务类型的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域接入时，接入模块不会开启组播功能，可节省系统资源。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[STB]{lang="EN-US"}]{#struct_0_86480_74578_1787958470}[（]{style="font-family:宋体"}[Set Top Box]{lang="EN-US"}[，机顶盒）接入业务：专指使用数字机顶盒接入网络的用户业务。用户使用该业务类型的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域接入时，接入模块会开启组播功能，可提高系统处理组播业务的性能。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[VoIP]{lang="EN-US"}]{#struct_0_86480_74578_1824313719}[（]{style="font-family:宋体"}[Voice over IP]{lang="EN-US"}[，]{style="font-family:宋体"}[IP]{lang="EN-US"}[电话）业务：指使用]{style="font-family:宋体"}[IP]{lang="EN-US"}[电话的用户业务。用户使用该业务类型的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域接入时，]{style="font-family:宋体"}[QoS]{lang="EN-US"}[功能会开启保证用户语音数据的低延迟传送。]{style="font-family:宋体"}

[[对于]{style="font-family:宋体"}[IPoE]{lang="EN-US"}]{#struct_0_86480_74578_1788024006}[三层专线用户、]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户、]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户，]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中配置的业务类型无效，系统强制使用]{style="font-family:宋体"}[HSI]{lang="EN-US"}[业务类型。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787434181}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1360639647}[设置域]{style="font-family:宋体"}[test]{lang="EN-US"}[下用户业务类型为]{style="font-family:宋体"}[STB]{lang="EN-US"}[终端业务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1787499717}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] service-type stb]{lang="EN-US"}
:::

::: {#1162988424 .myid}
[]{#_Toc404792559}[]{#struct_0_86480_74578_x329562639}[]{#_Toc335845124}

**AAA \-- ISP域中实现AAA配置命令 \-- session-time include-idle-time**

------------------------------------------------------------------------

[**[session-time include-idle-time]{lang="EN-US"}**]{#struct_0_86480_74578_x1851022822}[命令用来配置设备上传到服务器的用户在线时间中保留闲置切断时间。]{style="font-family:
宋体"}

[**[undo session-time include-idle-time]{lang="EN-US"}**]{#struct_0_86480_74578_x1804047733}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850957286}

[**[session-time include-idle-time]{lang="EN-US"}**]{#struct_0_86480_74578_1098311665}

[**[undo session-time]{lang="EN-US"}**[ **include-idle-time**]{lang="EN-US"}]{#struct_0_86480_74578_836035635}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850629606}

[[设备上传到服务器的用户在线时间中扣除闲置切断时间。]{style="font-family:宋体"}]{#struct_0_86480_74578_1633916868}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850564070}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x944304760}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_106512007}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1850760678}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x48450978}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850695142}

[[当用户正常下线时，设备上传到服务器上的用户在线时间为实际在线时间。当用户异常下线时，若配置为保留闲置切断时间，则上传到服务器上的用户在线时间中包含了一定的闲置切断检测间隔或用户在线探测间隔（该在线探测机制目前仅]{style="font-family:宋体"}[Portal]{lang="EN-US"}]{#struct_0_86480_74578_x2116531938}[认证支持），此时服务器上记录的用户时长将大于用户实际在线时长。若配置为扣除闲置切断时间，则上传到服务器上的用户在线时间为，闲置切断检测机制（或用户在线探测机制）计算出的用户已在线时长扣除掉一个闲置切断检测间隔（或一个用户在线探测间隔），此时服务器上记录的用户时长将小于用户实际在线时长。]{style="font-family:宋体"}

[[请根据实际的计费策略决定是否在用户在线时间中保留该闲置切换时间。]{style="font-family:宋体"}]{#struct_0_86480_74578_x672703714}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1850367462}

[[\#]{lang="EN-US"}]{#struct_0_86480_74578_97908410}[在]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[下，]{style="font-family:宋体"} [配置设备上传到服务器的用户在线时间中保留闲置切断时间。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1850301926}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\]session-time include-idle-time]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2042964665}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_x1416927526}
:::

::: {#1056402728 .myid}
[]{#_Toc404792560}[]{#struct_0_86480_74578_1902143822}[]{#_Toc268769737}[]{#_Toc205699675}[]{#_Toc162860260}[]{#_Toc147117577}[]{#_Toc147049937}[]{#_Toc146447657}[]{#_Toc69900468}

**AAA \-- ISP域中实现AAA配置命令 \-- state（ISP domain view）**

------------------------------------------------------------------------

[**[state]{lang="EN-US"}**]{#struct_0_86480_74578_38055726}[命令用来设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的状态。]{style="font-family:宋体"}

[**[undo state]{lang="EN-US"}**]{#struct_0_86480_74578_370748090}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x391242773}

[**[state]{lang="EN-US"}**[ { **active** \| **block** }]{lang="EN-US"}]{#struct_0_86480_74578_x130728890}

[**[undo state]{lang="EN-US"}**]{#struct_0_86480_74578_x902396009}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1189534263}

[[当一个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1214531771}[域被创建以后，其状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x26386278}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1284371706}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1556156529}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_118581585}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1951548044}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1508312858}

[**[active]{lang="EN-US"}**]{#struct_0_86480_74578_1147223827}[：指定当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域处于活动状态，即系统允许该域下的用户请求网络服务。]{style="font-family:宋体"}

[**[block]{lang="EN-US"}**]{#struct_0_86480_74578_x927805573}[：指定当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域处于"阻塞"状态，即系统不允许该域下的用户请求网络服务。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214466235}

[[当指定某个]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1223469490}[域处于]{style="font-family:宋体"}**[block]{lang="EN-US"}**[状态时，不允许该域下的用户请求网络服务，但是不影响已经在线的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_350526710}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1841723638}[设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域]{style="font-family:宋体"}[test]{lang="EN-US"}[处于"阻塞"状态，域下的接入用户不能再请求网络服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1349308125}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] state block]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1259280173}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_668629523}
:::

::: {#-827688465 .myid}
[]{#_Toc404792561}[]{#struct_0_86480_74578_1787040965}

**AAA \-- ISP域中实现AAA配置命令 \-- user-address-type**

------------------------------------------------------------------------

[**[user-address-type]{lang="EN-US"}**]{#struct_0_86480_74578_1787106501}[命令用来设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的用户地址类型。]{style="font-family:宋体"}

[**[undo user-address-type]{lang="EN-US"}**]{#struct_0_86480_74578_1017667720}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787958469}

[**[user-address-type]{lang="EN-US"}**[ { **ds-lite** \| **ipv6** \| **nat64** \| **private-ds** \| **private-ipv4** \| **public-ds** \| **public-ipv4** }]{lang="EN-US"}]{#struct_0_86480_74578_1788024005}

[**[undo user-address-type]{lang="EN-US"}**]{#struct_0_86480_74578_798837213}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787434180}

[[未指定当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_x1360574111}[域的用户地址类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787499716}

[[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1787303108}[域视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2108882183}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1787368644}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1435357888}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787172036}

[**[ds-lite]{lang="EN-US"}**]{#struct_0_86480_74578_1787237572}[：表示当前用户的地址类型为轻量级双栈地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_x559032953}[：表示当前用户的地址类型为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[nat64]{lang="EN-US"}**]{#struct_0_86480_74578_1787040964}[：表示当前用户的地址类型为]{style="font-family:宋体"}[NAT64]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[private-ds]{lang="EN-US"}**]{#struct_0_86480_74578_x1992711582}[：表示当前用户的地址类型为私网双栈地址。]{style="font-family:宋体"}

[**[private-ipv4]{lang="EN-US"}**]{#struct_0_86480_74578_47374250}[：表示当前用户的地址类型为私网]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[public-ds]{lang="EN-US"}**]{#struct_0_86480_74578_1787106500}[：表示当前用户的地址类型为公网双栈地址。]{style="font-family:宋体"}

[**[public-ipv4]{lang="EN-US"}**]{#struct_0_86480_74578_1017602184}[：表示当前用户的地址类型为公网]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1788024004}

[[当更改当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}]{#struct_0_86480_74578_1787434179}[域的用户地址类型时，不影响已经在线的用户。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1360115368}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1787499715}[设置当前]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域用户地址类型为私网双栈地址。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1787303107}

[\[Sysname\] domain test]{lang="EN-US"}

[\[Sysname-isp-test\] user-address-type private-ds]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2109472007}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display domain]{lang="EN-US"}**]{#struct_0_86480_74578_1787368643}
:::

::: {#1427103382 .myid}
[]{#_Toc268769740}[]{#_Toc205699653}[]{#_Toc194221083}[]{#_Toc404792563}[]{#struct_0_86480_74578_x1214400699}[]{#_Toc334602003}[]{#_Toc268769739}

**AAA \-- 本地用户配置命令 \-- access-limit**

------------------------------------------------------------------------

[**[access-limit]{lang="EN-US"}**]{#struct_0_86480_74578_908909964}[命令用来设置使用当前本地用户名接入设备的最大用户数。]{style="font-family:宋体"}

[**[undo access-limit]{lang="EN-US"}**]{#struct_0_86480_74578_1871275201}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1165595418}

[**[access-limit ]{lang="EN-US"}***[max-user-number]{lang="EN-US"}*]{#struct_0_86480_74578_1218419249}

[**[undo access-limit]{lang="EN-US"}**]{#struct_0_86480_74578_x740281126}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x958364348}

[[不限制使用当前本地用户名接入的用户数。]{style="font-family:宋体"}]{#struct_0_86480_74578_1507860416}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x205184286}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214335163}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x640321698}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_48399774}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1912645345}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x672046416}

[*[max-user-number]{lang="EN-US"}*]{#struct_0_86480_74578_x1811104451}[：表示使用当前本地用户名接入设备的最大用户数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[1024]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_186689561}

[[本地用户视图下的]{style="font-family:宋体"}**[access-limit]{lang="EN-US"}**]{#struct_0_86480_74578_1835506122}[命令只在该用户采用了本地计费方法的情况下生效。]{style="font-family:宋体"}

[[由于]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_x1210373312}[用户不支持计费，因此]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户不受此属性限制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214269627}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_889733000}[允许同时以本地用户名]{style="font-family:宋体"}[abc]{lang="EN-US"}[在线的用户数为]{style="font-family:宋体"}[5]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1101558423}

[\[Sysname\] local-user abc]{lang="EN-US"}

[\[Sysname-luser-manage-abc\] access-limit 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x394606563}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x827846753}
:::

::: {#-935697955 .myid}
[]{#_Toc404792564}[]{#struct_0_86480_74578_894769313}

**AAA \-- 本地用户配置命令 \-- authorization-attribute（Local user view/user group view）**

------------------------------------------------------------------------

[**[authorization-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_8644741}[命令用来设置本地用户或用户组的授权属性，该属性在本地用户认证通过之后，由设备下发给用户。]{style="font-family:宋体"}

[**[undo authorization-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_1153018234}[命令用来删除配置的授权属性，恢复用户具有的缺省访问权限。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214204091}

[**[authorization-attribute]{lang="EN-US"}**[ { **acl** *acl-number* \| **callback-number** *callback-number* \| **idle-cut** *minute* \| **ip** *ipv4-address* \| **ipv6** *ipv6-address* \| **ipv6-pool** *ipv6-pool-name* \| **ipv6-prefix** *ipv6-prefix prefix-length* \| { **primary-dns** \| **secondary-dns** } { **ip** *ip-address* \| **ipv6** *ipv6-address* } \| **sslvpn-policy-group** *group-name* \| **url** *url-string* \| **user-profile** *profile-name* \| **user-role** *role-name* \| **vlan** *vlan-id* \| **vpn-instance** *vpn-instance-name* \| **work-directory** *directory-name* } \*]{lang="EN-US"}]{#struct_0_86480_74578_1100167342}

[**[undo]{lang="EN-US"}**[ **authorization-attribute** { **acl** \| **callback-number** \| **idle-cut** \| **ip** \| **ipv6** \| **ipv6-pool** \| **ipv6-prefix** \| **primary-dns** \| **secondary-dns** \| **sslvpn-policy-group** \| **url** \| **user-profile** \| **user-role** *role-name* \| **vlan** \| **vpn-instance** \| **work-directory** } \*]{lang="EN-US"}]{#struct_0_86480_74578_793608608}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_422842983}

[[授权]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_751581395}[用户可以访问的目录为设备的根目录，但无访问权限。由用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[或]{style="font-family:宋体"}[level-15]{lang="EN-US"}[的用户创建的本地用户被授权用户角色]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[。（不支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[、]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[授权]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_x105813192}[用户可以访问的目录为设备的根目录，但无访问权限。在缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中由用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[或者]{style="font-family:宋体"}[level-15]{lang="EN-US"}[的用户创建的本地用户被授权用户角色]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[；在非缺省]{style="font-family:宋体"}[MDC]{lang="EN-US"}[中由用户角色为]{style="font-family:宋体"}[mdc-admin]{lang="EN-US"}[或者]{style="font-family:宋体"}[level-15]{lang="EN-US"}[的用户创建的本地用户被授权用户角色]{style="font-family:宋体"}[mdc-operator]{lang="EN-US"}[（支持]{style="font-family:宋体"}[MDC]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[授权]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_1787499722}[用户可以访问的目录为设备的根目录，但无访问权限。在缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[中由用户角色为]{style="font-family:宋体"}[network-admin]{lang="EN-US"}[或者]{style="font-family:宋体"}[level-15]{lang="EN-US"}[的用户创建的本地用户被授权用户角色]{style="font-family:宋体"}[network-operator]{lang="EN-US"}[；在非缺省]{style="font-family:宋体"}[Context]{lang="EN-US"}[中由用户角色为]{style="font-family:宋体"}[context-admin]{lang="EN-US"}[或者]{style="font-family:宋体"}[level-15]{lang="EN-US"}[的用户创建的本地用户被授权用户角色]{style="font-family:宋体"}[context-operator]{lang="EN-US"}[（支持]{style="font-family:宋体"}[Context]{lang="EN-US"}[的设备）]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1887203622}

[[本地用户视图]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86480_74578_x1707800942}[用户组视图（该视图的支持情况与设备的型号有关，请以设备的实际情况为准）]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1334526798}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1598349049}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1214138555}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1049480444}

[**[acl ]{lang="EN-US"}***[acl-number]{lang="EN-US"}*]{#struct_0_86480_74578_943787104}[：指定本地用户的授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[acl-number]{lang="EN-US"}*[为授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}[的编号，取值范围为]{style="font-family:宋体"}[2000]{lang="EN-US"}[～]{style="font-family:宋体"}[5999]{lang="EN-US"}[。本地用户认证成功后，将被授权仅可以访问符合指定]{style="font-family:宋体"}[ACL]{lang="EN-US"}[规则的网络资源。]{style="font-family:宋体"}

[**[callback-number]{lang="EN-US"}**[ *callback-number*]{lang="EN-US"}]{#struct_0_86480_74578_x947470572}[：指定本地用户的授权]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼号码。其中，]{style="font-family:宋体"}*[callback-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[64]{lang="EN-US"}[个字符的字符串，区分大小写。本地用户认证成功后，设备将可以使用该用户的授权]{style="font-family:宋体"}[PPP]{lang="EN-US"}[回呼号码向]{style="font-family:宋体"}[PPP]{lang="EN-US"}[协商的对端设备发起回呼。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[idle-cut]{lang="EN-US"}**[ *minute*]{lang="EN-US"}]{#struct_0_86480_74578_1954222419}[：设置本地用户的闲置切断时间。其中，]{style="font-family:宋体"}*[minute]{lang="EN-US"}*[为设定的闲置切断时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[120]{lang="EN-US"}[，单位为分钟。如果用户在线后连续闲置的时长超过该值，设备会强制该用户下线。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_1787368650}[：指定本地用户的静态]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。本地用户认证成功后，将允许使用该]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_1435620031}[：指定本地用户的静态]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。本地用户认证成功后，将允许使用该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ipv6-pool]{lang="EN-US"}**[ *ipv6-pool-name*]{lang="EN-US"}]{#struct_0_86480_74578_1787172042}[：指定本地用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址池信息。本地用户认证成功后，将允许使用该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址池分配地址。其中，]{style="font-family:宋体"}*[ipv6-pool-name]{lang="EN-US"}*[表示地址池名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[ipv6-prefix]{lang="EN-US"}**[ *ipv6-prefix prefix-length*]{lang="EN-US"}]{#struct_0_86480_74578_1787237578}[：指定本地用户的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀信息。]{style="font-family:宋体"}*[ipv6-prefix prefix-length]{lang="EN-US"}*[为前缀地址和前缀长度，前缀长度取值范围是]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[。本地用户认证成功后，将允许使用该]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[前缀。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[primary-dns ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_86480_74578_1787040970}[：指定本地用户的首选]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。本地用户认证成功后，将被授权使用该主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[primary-dns ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_1787106506}[：指定本地用户的首选]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。本地用户认证成功后，将被授权使用该主]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[secondary-dns ip]{lang="EN-US"}**[ *ip-address*]{lang="EN-US"}]{#struct_0_86480_74578_1017471112}[：指定本地用户的备用]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。本地用户认证成功后，将被授权使用该从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[secondary-dns ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_1787958474}[：指定本地用户的备用]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。本地用户认证成功后，将被授权使用该从]{style="font-family:宋体"}[DNS]{lang="EN-US"}[服务器。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[sslvpn-policy-group]{lang="EN-US"}***[ group-name]{lang="EN-US"}*]{#struct_0_86480_74578_644877679}[：指定本地用户所引用的]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[策略组名，其中，]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。此属性只对]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户生效。关于]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[策略组的详细介绍请参见"安全配置指导"中的"]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[url ]{lang="EN-US"}***[url-string]{lang="EN-US"}*]{#struct_0_86480_74578_1824051575}[：指定本地用户的强制]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，区分大小写。用户认证成功后，此]{style="font-family:宋体"}[URL]{lang="EN-US"}[将被推送至]{style="font-family:宋体"}[PPP]{lang="EN-US"}[客户端。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[user-profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_621886492}[：指定本地用户的授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[profile-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[名称，]{style="font-family:宋体"}[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，只能包含英文字母、数字、下划线，区分大小写。当用户认证成功后，其访问行为将受到]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[中的预设配置的限制。关于]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[的详细介绍请参见"安全配置指导"中的"]{style="font-family:宋体"}[User Profile]{lang="EN-US"}["。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[user-role ]{lang="EN-US"}***[role-name]{lang="EN-US"}*]{#struct_0_86480_74578_x386614506}[：指定本地用户的授权用户角色。其中，]{style="font-family:宋体"}*[role-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[63]{lang="EN-US"}[个字符的字符串，区分大小写。可以为每个用户最多指定]{style="font-family:宋体"}[64]{lang="EN-US"}[个用户角色。本地用户角色的相关命令请参见"基础命令参考"中的"]{style="font-family:宋体"}[RBAC]{lang="EN-US"}["。该授权属性只能在本地用户视图下配置，不能在本地用户组视图下配置。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}***[ vlan-id]{lang="EN-US"}*]{#struct_0_86480_74578_x708175976}[：指定本地用户的授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。本地用户认证成功后，将被授权仅可以访问指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的网络资源。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_86480_74578_1788024010}[：指定本地用户所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例。其中，]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。本地用户认证成功后，将允许访问指定]{style="font-family:宋体"}[VPN]{lang="EN-US"}[中的网络资源。此属性只对]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户生效。]{style="font-family:宋体"}

[**[work-directory]{lang="EN-US"}***[ directory-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1214073019}[：授权]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户可以访问的目录。其中，]{style="font-family:宋体"}*[directory-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户可以访问的目录，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写，且该目录必须已经存在。缺省情况下，]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[用户可访问设备的根目录，可通过本参数来修改用户可以访问的目录。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_641983873}

[[可配置的授权属性都有其明确的使用环境和用途，请针对用户的服务类型配置对应的授权属性：]{style="font-family:宋体"}]{#struct_0_86480_74578_288394627}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[ppp]{lang="EN-US"}]{#struct_0_86480_74578_x1850695145}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[callback-number]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[idle-cut]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[user-profile]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ip]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6-prefix]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6-pool]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[primary-dns]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[secondary-dns]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[url]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[vpn]{lang="EN-US"}[-instance]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{style="font-family:宋体"}]{#struct_0_86480_74578_1787303113}[IPoE]{lang="EN-US"}[用户，]{style="font-family:宋体"}[仅授权属性]{lang="EN-US" style="font-family:宋体"}**[idle-cut]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[user-profile]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ip]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6-prefix]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6-pool]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[vpn]{lang="EN-US"}[-instance]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[portal]{lang="EN-US"}]{#struct_0_86480_74578_36000471}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[acl]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[idle-cut]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[user-profile]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ip]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ipv6]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_1787368649}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[acl]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[user-profile]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}]{#struct_0_86480_74578_974746044}[http]{lang="EN-US"}[、]{style="font-family:宋体"}[https]{lang="EN-US"}[、]{style="font-family:宋体"}[telnet]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[terminal]{lang="EN-US"}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[user-role]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[ssh]{lang="EN-US"}]{#struct_0_86480_74578_x941530891}[、]{lang="EN-US" style="font-family:宋体"}[ftp]{lang="EN-US"}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[user-role]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[work-directory]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_1001173575}[用户，仅授权属性]{lang="EN-US" style="font-family:宋体"}**[sslvpn-policy-group]{lang="EN-US"}**[有效；]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于其它类型的本地用户，所有授权属性均无效。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1563487944}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1945765185}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[用户组的授权属性对于组内的所有本地用户生效，因此具有相同属性的用户可通过加入相同的用户组来统一配置和管理。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1444223588}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[本地用户视图下未配置的授权属性继承所属用户组的授权属性配置，但是如果本地用户视图与所属的用户组视图下都配置了某授权属性，则本地用户视图下的授权属性生效。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1215056059}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为了避免设备上进行主备倒换后]{style="font-family:宋体"}]{#struct_0_86480_74578_1326241132}[FTP/SFTP/SCP]{lang="EN-US"}[用户无法正常登录，建议用户在指定工作目录时不要携带槽位信息。主备倒换特性以及]{style="font-family:宋体"}[FTP/SFTP/SCP]{lang="EN-US"}[类型用户的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果希望本地用户仅使用本命令授权的用户角色]{lang="EN-US" style="font-family:宋体"}]{#struct_0_86480_74578_404400314}[，建议使用]{lang="EN-US" style="font-family:宋体"}**[undo authorization-attribute user-role]{lang="EN-US"}**[命令删除该用户已有的缺省用户角色。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[被授权安全日志管理员的本地用户登录设备后，仅可执行安全日志文件管理相关的命令以及安全日志文件操作相关的命令，具体命令可通过]{style="font-family:宋体"}]{#struct_0_86480_74578_x105944264}**[display role name security-audit]{lang="EN-US"}**[命令查看。安全日志文件管理相关命令的介绍，请参见"网络管理与监控"中的"信息中心"。文件系统管理相关命令的介绍，请参见"基础配置命令参考"中的"文件系统管理"。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为一个用户授权安全日志管理员角色时，经过界面的交互式确认后，系统会自动删除当前用户的所有其它他用户角色；如果已经授权当前用户安全日志管理员角色，再授权其它的用户角色时，经过界面的交互式确认后，系统会自动删除当前用户的安全日志管理员角色。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1031617491}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统中的最后一个安全日志管理员角色的本地用户不可被删除。]{style="font-family:宋体"}]{#struct_0_86480_74578_972177762}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x967919052}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1439567511}[配置网络接入类本地用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_778770404}

[\[Sysname\] local-user abc class network]{lang="EN-US"}

[\[Sysname-luser-network-abc\] authorization-attribute vlan 2]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_985608078}[配置用户组]{style="font-family:宋体"}[abc]{lang="EN-US"}[的授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[为]{style="font-family:宋体"}[VLAN 3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1214990523}

[\[Sysname\] user-group abc]{lang="EN-US"}

[\[Sysname-ugroup-abc\] authorization-attribute vlan 3]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x104961224}[配置设备管理类本地用户]{style="font-family:宋体"}[xyz]{lang="EN-US"}[的授权用户角色为]{style="font-family:宋体"}[security-audit]{lang="EN-US"}[（安全日志管理员）。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_2122802784}

[\[Sysname\] local-user xyz class manage]{lang="EN-US"}

[\[Sysname-luser-manage-xyz\]authorization-attribute user-role security-audit]{lang="EN-US"}

[This operation will delete all other roles of the user. Are you sure? \[Y/N\]:y]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1277696432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_285468268}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_86480_74578_464859028}
:::

::: {#-1251072692 .myid}
[]{#_Toc404792565}[]{#struct_0_86480_74578_x537514259}[]{#_Toc268769741}

**AAA \-- 本地用户配置命令 \-- bind-attribute**

------------------------------------------------------------------------

[**[bind-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_x1145565174}[命令用来设置用户的绑定属性。]{style="font-family:宋体"}

[**[undo bind-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_1552320882}[命令用来删除配置的用户绑定属性。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1558502101}

[**[bind-attribute ]{lang="EN-US"}**[{ **call-number** *call-number* \[ **:** *subcall-number* \] \| **ip** *ip-address* \| **location** **interface** *interface-type* *interface-number* \| **mac** *mac-address* \| **vlan** *vlan-id* } \*]{lang="EN-US"}]{#struct_0_86480_74578_x1440234211}

[**[undo bind-attribute ]{lang="EN-US"}**[{ **call-number** \| **ip** \| **location** \| **mac** \| **vlan** } \*]{lang="EN-US"}]{#struct_0_86480_74578_x1214531774}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x429670805}

[[未设置用户的任何绑定属性。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1690828390}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x531834424}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1967329452}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_2093032367}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_474571516}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1925763432}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1134661971}

[**[call-number]{lang="EN-US"}**[ *call-number*]{lang="EN-US"}]{#struct_0_86480_74578_x1214466238}[：指定]{style="font-family:宋体"}[PPP]{lang="EN-US"}[用户认证的主叫号码。其中]{style="font-family:宋体"}*[call-number]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:
宋体"}[64]{lang="EN-US"}[个字符的字符串。本参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[*[subcall-number]{lang="EN-US"}*]{#struct_0_86480_74578_x107724243}[：指定子主叫号码。如果配置了子主叫号码，则主叫号码与子主叫号码的总长度不能大于]{style="font-family:宋体"}[62]{lang="EN-US"}[个字符。]{style="font-family:宋体"}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}*]{#struct_0_86480_74578_x1515076627}[：指定用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[location ]{lang="EN-US"}[interface ]{lang="EN-US"}***[interface-type interface-number]{lang="EN-US"}*]{#struct_0_86480_74578_888481787}[：指定用户绑定的接口。其中]{style="font-family:宋体"}*[interface-type interface-number]{lang="EN-US"}*[表示接口类型和接口编号]{style="font-family:宋体"}[。如果用户接入的接口与此处绑定的接口不一致，则认证失败。]{style="font-family:宋体"}

[**[mac ]{lang="EN-US"}***[mac-address]{lang="EN-US"}*]{#struct_0_86480_74578_1112469463}[：指定用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址。其中，]{style="font-family:宋体"}*[mac-address]{lang="EN-US"}*[为]{style="font-family:宋体"}[H-H-H]{lang="EN-US"}[格式。]{style="font-family:宋体"}

[**[vlan ]{lang="EN-US"}***[vlan-id]{lang="EN-US"}*]{#struct_0_86480_74578_1970025692}[：指定用户所属于的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1348627761}

[[需要注意的是，当对本地用户进行认证时，如果配置了绑定属性，则会检查用户的实际属性与配置的绑定属性是否一致，如果不一致或用户未携带该绑定属性则认证失败。而且，由于认证检测时不区分用户的接入服务类型，即会对所有类型的用户都进行已配置绑定属性的认证检测，因此在配置绑定属性时要考虑某类型的用户是否需要绑定某些属性。例如，只有支持]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_1507867382}[地址上传功能的]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证用户才可以配置绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址；对于不支持]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址上传功能的]{style="font-family:宋体"}[MAC]{lang="EN-US"}[地址认证用户，如果配置了绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址，则会导致该用户的本地认证失败。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[绑定属性]{lang="EN-US" style="font-family:宋体"}**[call-number]{lang="EN-US"}**]{#struct_0_86480_74578_1975826486}[仅适用于]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[用户；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[绑定属性]{lang="EN-US" style="font-family:宋体"}**[ip]{lang="EN-US"}**]{#struct_0_86480_74578_1479077801}[仅适用于]{lang="EN-US" style="font-family:宋体"}[lan-access]{lang="EN-US"}[类型中的]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户；]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[绑定属性]{lang="EN-US" style="font-family:宋体"}**[location]{lang="EN-US"}**]{#struct_0_86480_74578_53512185}[、]{lang="EN-US" style="font-family:宋体"}**[mac]{lang="EN-US"}**[和]{lang="EN-US" style="font-family:宋体"}**[vlan]{lang="EN-US"}**[仅适用于]{lang="EN-US" style="font-family:宋体"}[lan-access]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[IPoE]{lang="EN-US"}[、]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[类型的用户。]{lang="EN-US" style="font-family:宋体"}

[[在绑定接口属性时要考虑绑定接口类型是否合理。例如对]{style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_86480_74578_1730445498}[认证用户绑定接口需要绑定物理接口，如果绑定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[接口等虚接口，则会导致该用户的本地认证失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214400702}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_2118173720}[配置网络接入类本地用户]{style="font-family:宋体"}[abc]{lang="EN-US"}[的绑定]{style="font-family:宋体"}[IP]{lang="EN-US"}[为]{style="font-family:宋体"}[3.3.3.3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x760571280}

[\[Sysname\] local-user abc class network]{lang="EN-US"}

[\[Sysname-luser-network-abc\] bind-attribute ip 3.3.3.3]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_298882503}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_167882995}
:::

::: {#-337538337 .myid}
[]{#_Toc404792566}[]{#struct_0_86480_74578_1668815504}[]{#_Toc268769742}

**AAA \-- 本地用户配置命令 \-- display local-user**

------------------------------------------------------------------------

[**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1911986634}[命令用来显示本地用户的配置信息和在线用户数的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1668747981}

[**[display local-user ]{lang="EN-US"}**[\[ **class** { **manage** \| **network** } \| **idle-cut** { **disable** \| **enable** } \| **service-type** { **advpn** \| **ftp** \| **http** \| **https** \| ]{lang="EN-US"}]{#struct_0_86480_74578_2104594050}**[ipoe]{lang="EN-US"}**[ \| **lan-access** \| **pad** \| **portal** \| **ppp** \| **ssh** \| **sslvpn** \| **telnet** \| **terminal** } \| **state** { **active** \| **block** } \| **user-name** *user-name* \| **vlan** *vlan-id* \]]{lang="EN-US"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214335166}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1043606225}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x918857939}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_447432637}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_1303894912}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1410271923}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_1558583228}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1096861342}

[**[class]{lang="EN-US"}**]{#struct_0_86480_74578_x199630066}[：显示指定用户类别的本地用户信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[manage]{lang="EN-US"}**]{#struct_0_86480_74578_x1214269630}[：设备管理类用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_86480_74578_486514009}[：网络接入类用户。]{lang="EN-US" style="font-family:宋体"}

[**[idle-cut]{lang="EN-US"}**[ { **disable** \| **enable** }]{lang="EN-US"}]{#struct_0_86480_74578_417087087}[：显示使能或未使能闲置切断功能的本地用户信息。其中，]{style="font-family:宋体"}**[disable]{lang="EN-US"}**[表示未启用闲置切断功能的本地用户；]{style="font-family:宋体"}**[enable]{lang="EN-US"}**[表示启用了闲置切断功能并配置了闲置切断时间的本地用户。]{style="font-family:宋体"}

[**[service-type]{lang="EN-US"}**]{#struct_0_86480_74578_x1837228393}[：显示指定用户类型的本地用户信息。各用户类型的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[a]{lang="EN-US"}[dvpn]{lang="EN-US"}**]{#struct_0_86480_74578_98611098}[：]{lang="EN-US" style="font-family:宋体"}[A]{lang="EN-US"}[DVPN]{lang="EN-US"}[隧道用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ftp]{lang="EN-US"}**]{#struct_0_86480_74578_x152365893}[：]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http]{lang="EN-US"}**]{#struct_0_86480_74578_x2041140438}[：]{lang="EN-US" style="font-family:宋体"}[HTTP]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[https]{lang="EN-US"}**]{#struct_0_86480_74578_x743302880}[：]{lang="EN-US" style="font-family:宋体"}[HTTPS]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_1384149655}[：]{style="font-family:
宋体"}[IPoE]{lang="EN-US"}[用户（主要指]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户，比如二]{style="font-family:宋体"}[/]{lang="EN-US"}[三层专线用户，数字机顶盒接入用户）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_906504142}[：]{lang="EN-US" style="font-family:宋体"}[lan-access]{lang="EN-US"}[类型用户（主要指以太网接入用户，比如]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pad]{lang="EN-US"}**]{#struct_0_86480_74578_x1214204094}[：]{lang="EN-US" style="font-family:宋体"}[X.25 PAD]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal]{lang="EN-US"}**]{#struct_0_86480_74578_1503451869}[：]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp]{lang="EN-US"}**]{#struct_0_86480_74578_1212323838}[：]{lang="EN-US" style="font-family:宋体"}[PPP]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssh]{lang="EN-US"}**]{#struct_0_86480_74578_x238704774}[：]{lang="EN-US" style="font-family:宋体"}[SSH]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[**[sslvpn]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_86480_74578_1897479596}[：]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[telnet]{lang="EN-US"}**]{#struct_0_86480_74578_601165897}[：]{lang="EN-US" style="font-family:宋体"}[Telnet]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal]{lang="EN-US"}**]{#struct_0_86480_74578_x1978889395}[：从]{style="font-family:宋体"}[CON]{lang="EN-US"}[口、]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口、]{style="font-family:宋体"}[Asyn]{lang="EN-US"}[口登录的终端用户。不同型号的设备支持的用户登录接口类型不同，请以设备的实际情况为准]{style="font-family:宋体"}

[**[state]{lang="EN-US"}**[ { **active** \| **block** }]{lang="EN-US"}]{#struct_0_86480_74578_1057428503}[：显示处于指定状态的本地用户信息。其中，]{style="font-family:宋体"}**[active]{lang="EN-US"}**[表示用户处于活动状态，即系统允许该用户请求网络服务；]{style="font-family:宋体"}**[block]{lang="EN-US"}**[表示用户处于阻塞状态，即系统不允许用户请求网络服务。]{style="font-family:宋体"}

[**[user-name]{lang="EN-US"}**[ *user-name*]{lang="EN-US"}]{#struct_0_86480_74578_x970143387}[：显示指定用户名的本地用户信息。其中，]{style="font-family:宋体"}*[user-name]{lang="EN-US"}*[表示本地用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写，不能携带域名。]{style="font-family:宋体"}

[**[vlan]{lang="EN-US"}**[ *vlan-id*]{lang="EN-US"}]{#struct_0_86480_74578_580548239}[：显示指定]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[内的所有本地用户信息。其中，]{style="font-family:宋体"}*[vlan-id]{lang="EN-US"}*[为]{style="font-family:宋体"}[VLAN]{lang="EN-US"}[编号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[4094]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1214138558}

[[如果不指定任何参数，则显示所有本地用户信息。]{style="font-family:宋体"}]{#struct_0_86480_74578_2129741605}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x809395237}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x994101237}[显示所有本地用户的相关信息。]{style="font-family:宋体"}

[[\<Sysname\> display local-user]{lang="EN-US"}]{#struct_0_86480_74578_x1214073022}

[Total 2 local users matched.]{lang="EN-US"}

[ ]{lang="EN-US"}

[Device management user root:]{lang="EN-US"}

[ State:                    Active]{lang="EN-US"}

[ Service type:             SSH/Telnet/Terminal]{lang="EN-US"}

[ Access limit:             Enabled           Max access number: 3]{lang="EN-US"}

[ Current access number:    1]{lang="EN-US"}

[ User group:               system]{lang="EN-US"}

[ Bind attributes:]{lang="EN-US"}

[ Authorization attributes:]{lang="EN-US"}

[  Work directory:          flash:]{lang="EN-US"}

[  User role list:          network-admin]{lang="EN-US"}

[ Password control configurations:]{lang="EN-US"}

[  Password aging:          Enabled (3 days)]{lang="EN-US"}

[Network access user jj:]{lang="EN-US"}

[ State:                    Active]{lang="EN-US"}

[ Service type:             Lan-access]{lang="EN-US"}

[ User group:               system]{lang="EN-US"}

[ Bind attributes:]{lang="EN-US"}

[  IP address:              2.2.2.2]{lang="EN-US"}

[  Location bound:          GigabitEthernet1/0/1]{lang="EN-US"}

[  MAC address:             0001-0001-0001]{lang="EN-US"}

[  VLAN ID:                 2]{lang="EN-US"}

[  Calling number:          2:2]{lang="EN-US"}

[ Authorization attributes:]{lang="EN-US"}

[  Idle timeOut:            33 (min)]{lang="EN-US"}

[  Work directory:          flash:]{lang="EN-US"}

[  ACL number:              2000]{lang="EN-US"}

[  User profile:            pp]{lang="EN-US"}

[  User role list:          network-operator, level-0, level-3]{lang="EN-US"}

[  SSL VPN policy group:    spg]{lang="EN-US"}

[]{#struct_0_86480_74578_688841432}[]{#_Toc138066607}[]{#_Toc95386911}[]{#_Toc85621925}[]{#_Toc81452873}[[表1-2 ]{lang="EN-US"}[display local-user]{lang="EN-US"}]{#_Toc38965299}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_784540962}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_x397071401}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_1051898022}

[[Total 2 local users matched.]{lang="EN-US"}]{#struct_0_86480_74578_x1215056062}

[[总计有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_86480_74578_x596269777}[个本地用户匹配]{style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_86480_74578_x260699126}

[[本地用户状态]{style="font-family:宋体"}]{#struct_0_86480_74578_x1138036409}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_86480_74578_682223290}[：活动状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Block]{lang="EN-US"}]{#struct_0_86480_74578_1908539215}[：阻塞状态]{lang="EN-US" style="font-family:宋体"}

[[Service type]{lang="EN-US"}]{#struct_0_86480_74578_x1214990526}

[[本地用户使用的服务类型，取值包括]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}]{#struct_0_86480_74578_x1680980959}[、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[、]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[、]{style="font-family:宋体"}[Lan-access]{lang="EN-US"}[、]{style="font-family:宋体"}[PAD]{lang="EN-US"}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[、]{style="font-family:宋体"}[Terminal]{lang="EN-US"}[和]{style="font-family:宋体"}[[SSL VPN]{lang="EN-US"}]{.TableTextChar}

[[Access limit]{lang="EN-US"}]{#struct_0_86480_74578_x530925011}

[[是否对使用该用户名的接入用户数进行限制]{style="font-family:宋体"}]{#struct_0_86480_74578_x774202385}

[[Max access number]{lang="EN-US"}]{#struct_0_86480_74578_x1366955254}

[[最大接入用户数]{style="font-family:宋体"}]{#struct_0_86480_74578_x1315219668}

[[Current access number]{lang="EN-US"}]{#struct_0_86480_74578_x1214531773}

[[使用该用户名的当前接入用户数]{style="font-family:宋体"}]{#struct_0_86480_74578_x1189185692}

[[User group]{lang="EN-US"}]{#struct_0_86480_74578_1099955759}

[[本地用户所属的用户组]{style="font-family:宋体"}]{#struct_0_86480_74578_x1932216996}

[[Bind attributes]{lang="EN-US"}]{#struct_0_86480_74578_x1421341382}

[[本地用户的绑定属性]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214466237}

[[IP address]{lang="EN-US"}]{#struct_0_86480_74578_x60670076}

[[本地用户的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x982781562}[地址]{style="font-family:宋体"}

[[Location bound]{lang="EN-US"}]{#struct_0_86480_74578_x1707689562}

[[本地用户绑定的端口]{style="font-family:宋体"}]{#struct_0_86480_74578_745110734}

[[MAC address]{lang="EN-US"}]{#struct_0_86480_74578_x1214400701}

[[本地用户的]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_86480_74578_552089779}[地址]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_86480_74578_1412082897}

[[本地用户绑定的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_86480_74578_x1975378970}

[[Calling number]{lang="EN-US"}]{#struct_0_86480_74578_447539254}

[[ISDN]{lang="EN-US"}]{#struct_0_86480_74578_x1214335165}[用户的主叫号码]{style="font-family:宋体"}

[[Authorization attributes]{lang="EN-US"}]{#struct_0_86480_74578_x1446890752}

[[本地用户的授权属性]{style="font-family:宋体"}]{#struct_0_86480_74578_1928703551}

[[Idle timeOut]{lang="EN-US"}]{#struct_0_86480_74578_2030080341}

[[本地用户闲置切断时间（单位为分钟）]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214269629}

[[Callback number]{lang="EN-US"}]{#struct_0_86480_74578_x1886204522}

[[本地用户的授权]{style="font-family:宋体"}[PPP]{lang="EN-US"}]{#struct_0_86480_74578_x1306130762}[回呼号码]{style="font-family:宋体"}

[[Work directory]{lang="EN-US"}]{#struct_0_86480_74578_x1456157160}

[[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_x1214204093}[用户可以访问的目录]{style="font-family:宋体"}

[[ACL number]{lang="EN-US"}]{#struct_0_86480_74578_x1344733701}

[[本地用户授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_86480_74578_x1344864773}

[[VLAN ID]{lang="EN-US"}]{#struct_0_86480_74578_x2064251856}

[[本地用户授权]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_86480_74578_x1214138557}

[[User profile]{lang="EN-US"}]{#struct_0_86480_74578_2082687438}

[[本地用户授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_86480_74578_1091815683}

[[该字段的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}]{#struct_0_86480_74578_1580916689}

[[User role list]{lang="EN-US"}]{#struct_0_86480_74578_x985680514}

[[本地用户的授权用户角色列表]{style="font-family:宋体"}]{#struct_0_86480_74578_x1214073021}

[[SSL VPN policy group]{lang="EN-US"}]{#struct_0_86480_74578_x831338223}

[[本地用户的授权]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_x71823336}[策略组]{style="font-family:宋体"}

[[IP address]{lang="EN-US"}]{#struct_0_86480_74578_x1344995846}

[[本地用户的授权]{style="font-family:宋体"}[IPv4]{lang="EN-US"}]{#struct_0_86480_74578_x1345126918}[地址]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_86480_74578_x1344209414}

[[本地用户的授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x1344733703}[地址]{style="font-family:宋体"}

[[IPv6 prefix]{lang="EN-US"}]{#struct_0_86480_74578_x1344864775}

[[本地用户的授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x1344995847}[前缀]{style="font-family:宋体"}

[[IPv6 pool]{lang="EN-US"}]{#struct_0_86480_74578_x1345126919}

[[本地用户的授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x1344209415}[地址池]{style="font-family:宋体"}

[[Primary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_x1344143879}

[[本地用户的授权首选]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_x1344668160}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Secondary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_x1344799232}

[[本地用户的授权备用]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_x1344930304}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_86480_74578_x1345061376}

[[本地用户的授权强制]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_x1344143872}

[[VPN instance]{lang="EN-US"}]{#struct_0_86480_74578_x1344668161}

[[本地用户的授权]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_x1344799233}[实例]{style="font-family:宋体"}

[[Password control configurations]{lang="EN-US"}]{#struct_0_86480_74578_285556905}

[[本地用户的密码控制属性]{style="font-family:宋体"}]{#struct_0_86480_74578_x373602061}

[[Password aging]{lang="EN-US"}]{#struct_0_86480_74578_1773661177}

[[密码老化功能的开启状态（密码的老化时间）]{style="font-family:宋体"}]{#struct_0_86480_74578_x1215056061}

[[Password length]{lang="EN-US"}]{#struct_0_86480_74578_969814164}

[[密码最小长度功能的开启状态（密码的最小长度）]{style="font-family:宋体"}]{#struct_0_86480_74578_415564286}

[[Password composition]{lang="EN-US"}]{#struct_0_86480_74578_x1214990525}

[[密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）]{style="font-family:宋体"}]{#struct_0_86480_74578_x114897018}

[[Password complexity]{lang="EN-US"}]{#struct_0_86480_74578_x504936517}

[[密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）]{style="font-family:宋体"}]{#struct_0_86480_74578_x536487173}

[[Maximum login attempts]{lang="EN-US"}]{#struct_0_86480_74578_351552171}

[[用户最大登录尝试次数]{style="font-family:宋体"}]{#struct_0_86480_74578_1958447211}

[[Action for exceeding login attempts]{lang="EN-US"}]{#struct_0_86480_74578_x430181297}

[[登录尝试次数达到设定次数后的用户帐户锁定行为]{style="font-family:宋体"}]{#struct_0_86480_74578_351617707}

[ ]{lang="EN-US"}

::::: {#-160839194 .myid}
[]{#_Toc404792567}[]{#struct_0_86480_74578_x491818729}[]{#_Toc268769743}[]{#_Toc299047487}[]{#_Toc299112000}[]{#_Toc299130048}[]{#_Toc299130142}[]{#_Toc299047488}[]{#_Toc299112001}[]{#_Toc299130049}[]{#_Toc299130143}

**AAA \-- 本地用户配置命令 \-- display user-group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_731546067}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x1421219148}
:::

[ ]{lang="EN-US"}

[**[display user-group]{lang="EN-US"}**]{#struct_0_86480_74578_1705985376}[命令用来]{style="font-family:宋体"}[显示用户组的相关配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1043502642}

[**[display user-group]{lang="EN-US"}**[ \[ *group-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_351683243}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_667488771}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x816029809}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1848573450}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1802339444}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1815078034}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1084575065}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1006322224}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_351748779}

[*[group-name]{lang="EN-US"}*]{#struct_0_86480_74578_1073377722}[：显示指定用户组的配置。]{style="font-family:宋体"}*[group-name]{lang="EN-US"}*[表示用户组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x248611789}

[[若不指定用户组名称，则显示所有用户组的相关配置。]{style="font-family:宋体"}]{#struct_0_86480_74578_x228358605}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x370760241}

[]{#_Toc268769745}[]{#_Toc205699664}[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x818937186}[显示所有用户组的相关配置。]{style="font-family:宋体"}

[[\<Sysname\> display user-group ]{lang="EN-US"}]{#struct_0_86480_74578_351814315}

[Total 2 user groups matched.]{lang="EN-US"}

[ ]{lang="EN-US"}

[The contents of user group system:]{lang="EN-US"}

[ Authorization attributes:]{lang="EN-US"}

[  Work directory:          flash:]{lang="EN-US"}

[The contents of user group jj:]{lang="EN-US"}

[ Authorization attributes:]{lang="EN-US"}

[  Idle timeOut:            2 (min)]{lang="EN-US"}

[  Callback number:         2:2]{lang="EN-US"}

[  Work directory:          flash:/]{lang="EN-US"}

[  ]{lang="EN-US"}[ACL number:              2000]{lang="NO-BOK"}

[  VLAN ID:                 2]{lang="NO-BOK"}

[  User profile:            pp]{lang="NO-BOK"}

[  ]{lang="NO-BOK"}[SSL VPN policy group:    policygroup1]{lang="EN-US"}

[Password control configurations:]{lang="NO-BOK"}

[  Password aging:          Enabled (2 days)]{lang="NO-BOK"}

[[表1-3 ]{lang="EN-US"}[display user-group]{lang="EN-US"}]{#struct_0_86480_74578_117153453}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_779538914}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_x292944177}
:::::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_x496764687}

[[Total 2 user groups matched.]{lang="EN-US"}]{#struct_0_86480_74578_x1282082628}

[[总计有]{style="font-family:宋体"}[2]{lang="EN-US"}]{#struct_0_86480_74578_971589537}[个用户组匹配]{style="font-family:宋体"}

[[Idle timeOut]{lang="EN-US"}]{#struct_0_86480_74578_351879851}

[[闲置切断时间（单位：分钟）]{style="font-family:宋体"}]{#struct_0_86480_74578_x722689636}

[[Callback number]{lang="EN-US"}]{#struct_0_86480_74578_1521949451}

[[PPP]{lang="EN-US"}]{#struct_0_86480_74578_1790135342}[回呼号码]{style="font-family:宋体"}

[[Work directory]{lang="EN-US"}]{#struct_0_86480_74578_x77744542}

[[FTP/SFTP/SCP]{lang="EN-US"}]{#struct_0_86480_74578_x318873519}[用户可以访问的目录]{style="font-family:宋体"}

[[ACL number]{lang="EN-US"}]{#struct_0_86480_74578_351945387}

[[授权]{style="font-family:宋体"}[ACL]{lang="EN-US"}]{#struct_0_86480_74578_89694040}[号]{style="font-family:宋体"}

[[VLAN ID]{lang="EN-US"}]{#struct_0_86480_74578_x1569974464}

[[授权]{style="font-family:宋体"}[VLAN ID]{lang="EN-US"}]{#struct_0_86480_74578_x1625598451}

[[User profile]{lang="EN-US"}]{#struct_0_86480_74578_1013132824}

[[授权]{style="font-family:宋体"}[User Profile]{lang="EN-US"}]{#struct_0_86480_74578_x887940146}[名称]{style="font-family:宋体"}

[[SSL VPN policy group]{lang="EN-US"}]{#struct_0_86480_74578_1541380308}

[[授权]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}]{#struct_0_86480_74578_1493189624}[策略组名称]{style="font-family:宋体"}

[[IPv6 prefix]{lang="EN-US"}]{#struct_0_86480_74578_x1747428405}

[[授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x1747952694}[前缀]{style="font-family:宋体"}

[[IPv6 pool]{lang="EN-US"}]{#struct_0_86480_74578_x1748083766}

[[授权]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x1748214838}[地址池]{style="font-family:宋体"}

[[Primary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_x1748345910}

[[授权首选]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_x1747428406}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Secondary DNS server]{lang="EN-US"}]{#struct_0_86480_74578_x1747952687}

[[授权备用]{style="font-family:宋体"}[DNS]{lang="EN-US"}]{#struct_0_86480_74578_x1748083759}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[URL]{lang="EN-US"}]{#struct_0_86480_74578_x1748214831}

[[授权强制]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_x1748345903}

[[VPN instance]{lang="EN-US"}]{#struct_0_86480_74578_x1747428399}

[[授权]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_x1747952688}[实例]{style="font-family:宋体"}

[[Password control configurations]{lang="EN-US"}]{#struct_0_86480_74578_352010923}

[[用户组的密码控制属性]{style="font-family:宋体"}]{#struct_0_86480_74578_1376601262}

[[Password aging]{lang="EN-US"}]{#struct_0_86480_74578_x1984053212}

[[密码老化功能的开启状态（密码的老化时间）]{style="font-family:宋体"}]{#struct_0_86480_74578_x2034406177}

[[Password length]{lang="EN-US"}]{#struct_0_86480_74578_161956033}

[[密码最小长度功能的开启状态（密码的最小长度）]{style="font-family:宋体"}]{#struct_0_86480_74578_351027883}

[[Password composition]{lang="EN-US"}]{#struct_0_86480_74578_x902192837}

[[密码组合策略的开启状态（密码元素的组合类型、至少要包含每种元素的个数）]{style="font-family:宋体"}]{#struct_0_86480_74578_1630472104}

[[Password complexity]{lang="EN-US"}]{#struct_0_86480_74578_x734855732}

[[密码复杂度检查功能的开启状态（检查是否包含用户名或者颠倒的用户名；检查是否包含三个或以上相同字符）]{style="font-family:宋体"}]{#struct_0_86480_74578_x1972790254}

[[Maximum login attempts]{lang="EN-US"}]{#struct_0_86480_74578_351093419}

[[用户最大登录尝试次数]{style="font-family:宋体"}]{#struct_0_86480_74578_631557630}

[[Action for exceeding login attempts]{lang="EN-US"}]{#struct_0_86480_74578_931057681}

[[登录尝试次数达到设定次数后的用户帐户锁定行为]{style="font-family:宋体"}]{#struct_0_86480_74578_38472673}

[ ]{lang="EN-US"}

::: {#-1172193874 .myid}
[]{#_Toc404792568}[]{#struct_0_86480_74578_904064206}[]{#_Toc299047490}[]{#_Toc299112003}[]{#_Toc299130051}[]{#_Toc299130145}[]{#_Toc299047491}[]{#_Toc299112004}[]{#_Toc299130052}[]{#_Toc299130146}

**AAA \-- 本地用户配置命令 \-- group**

------------------------------------------------------------------------

[**[group]{lang="EN-US"}**]{#struct_0_86480_74578_351552172}[命令用来设置本地用户所属的用户组。]{style="font-family:宋体"}

[**[undo group]{lang="EN-US"}**]{#struct_0_86480_74578_1958447210}[命令用来恢复缺省配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x430246833}

[**[group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_86480_74578_1801975992}

[**[undo group]{lang="EN-US"}**]{#struct_0_86480_74578_1915840979}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1511259102}

[[用户属于系统默认创建的用户组]{style="font-family:宋体"}[system]{lang="EN-US"}]{#struct_0_86480_74578_x18240473}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_2050561879}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_218080281}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_351617708}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x491818714}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_732266960}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1791439527}

[*[group-name]{lang="EN-US"}*]{#struct_0_86480_74578_1554923191}[：用户组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1314470369}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x32639759}[设置设备管理类本地用户]{style="font-family:宋体"}[111]{lang="EN-US"}[所属的用户组为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x25129883}

[\[Sysname\] local-user 111 class manage]{lang="EN-US"}

[\[Sysname-luser-manage-111\] group abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x356280644}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_351683244}
:::

::: {#626049738 .myid}
[]{#_Toc404792569}[]{#struct_0_86480_74578_667488768}

**AAA \-- 本地用户配置命令 \-- local-user**

------------------------------------------------------------------------

[**[local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1140285320}[命令用来添加本地用户，并进入本地用户视图。]{style="font-family:宋体"}

[**[undo local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1022420549}[命令用来删除指定的本地用户。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1009070936}

[**[local-user ]{lang="EN-US"}***[user-name ]{lang="EN-US"}*[\[ **class** { **manage** \| **network** } \]]{lang="EN-US"}]{#struct_0_86480_74578_815277035}

[**[undo local-user ]{lang="EN-US"}**[{ *user-name* **class** { **manage** \| **network** } \| **all** \[ **service-type** { **advpn** \| **ftp** \| **http** \| **https** \| **ipoe** \| **lan-access** \| **pad** \| **portal** \| **ppp** \| **ssh** \| **sslvpn** \| **telnet** \| **terminal** } \| **class** { **manage** \| **network** } \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1331741038}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_366426701}

[[不存在本地用户。]{style="font-family:宋体"}]{#struct_0_86480_74578_351748780}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1793421761}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x962927733}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1250799131}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_836863895}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1136342976}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_913289369}

[*[user-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1436833731}[：表示本地用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[55]{lang="EN-US"}[个字符的字符串，区分大小写。用户名不能携带域名，不能包括符号"]{style="font-family:宋体"}[\\]{lang="EN-US"}["、"]{style="font-family:宋体"}[\|]{lang="EN-US"}["、"]{style="font-family:宋体"}[/]{lang="EN-US"}["、"]{style="font-family:宋体"}[:]{lang="EN-US"}["、"]{style="font-family:宋体"}[\*]{lang="EN-US"}["、"]{style="font-family:宋体"}[?]{lang="EN-US"}["、"]{style="font-family:宋体"}[\<]{lang="EN-US"}["、"]{style="font-family:宋体"}[\>]{lang="EN-US"}["和"]{style="font-family:宋体"}[@]{lang="EN-US"}["，且不能为"]{style="font-family:宋体"}[a]{lang="EN-US"}["、"]{style="font-family:宋体"}[al]{lang="EN-US"}["或"]{style="font-family:宋体"}[all]{lang="EN-US"}["。]{style="font-family:宋体"}

[**[class]{lang="EN-US"}**]{#struct_0_86480_74578_323899298}[：指定本地用户的类别。若不指定本参数，则表示设备管理类用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[manage]{lang="EN-US"}**]{#struct_0_86480_74578_351814316}[：设备管理类用户，用于登录设备，对设备进行配置和监控。此类用户可以提供]{style="font-family:
宋体"}**[ftp]{lang="EN-US"}**[、]{style="font-family:宋体"}**[http]{lang="EN-US"}**[、]{style="font-family:宋体"}**[https]{lang="EN-US"}**[、]{style="font-family:宋体"}**[telnet]{lang="EN-US"}**[、]{style="font-family:宋体"}**[ssh]{lang="EN-US"}**[、]{style="font-family:宋体"}**[terminal]{lang="EN-US"}**[和]{style="font-family:宋体"}**[pad]{lang="EN-US"}**[服务。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[network]{lang="EN-US"}**]{#struct_0_86480_74578_117153452}[：网络接入类用户，用于通过设备接入网络，访问网络资源。]{style="font-family:
宋体"}[此类用户可以提供]{lang="EN-US" style="font-family:宋体"}**[a]{lang="EN-US"}[dvpn]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[lan-access]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[portal]{lang="EN-US"}**[、]{lang="EN-US" style="font-family:宋体"}**[ppp]{lang="EN-US"}**[和]{style="font-family:宋体"}**[sslvpn]{lang="EN-US"}**[服务。]{lang="EN-US" style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_86480_74578_x292944178}[：所有的用户。]{style="font-family:宋体"}

[**[service-type]{lang="EN-US"}**]{#struct_0_86480_74578_x496043791}[：指定用户的类型。各用户类型的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[advpn]{lang="EN-US"}**]{#struct_0_86480_74578_x861812889}[：]{style="font-family:
宋体"}[ADVPN]{lang="EN-US"}[隧道用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ftp]{lang="EN-US"}**]{#struct_0_86480_74578_x472577274}[：表示]{style="font-family:
宋体"}[FTP]{lang="EN-US"}[类型用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http]{lang="EN-US"}**]{#struct_0_86480_74578_1038240106}[：表示]{style="font-family:
宋体"}[HTTP]{lang="EN-US"}[类型用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[http]{lang="EN-US"}**]{#struct_0_86480_74578_1975695414}**[s]{lang="EN-US"}**[：表示]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[类型用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x1747428400}[：表示]{style="font-family:
宋体"}[IPoE]{lang="EN-US"}[类型用户（主要指以]{style="font-family:宋体"}[IP]{lang="EN-US"}[接入用户，比如二三层专线，数字机顶盒接入的用户）。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_x87747235}[：表示]{lang="EN-US" style="font-family:宋体"}[lan-access]{lang="EN-US"}[类型用户（主要指以太网接入用户，比如]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}[用户）。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[pad]{lang="EN-US"}**]{#struct_0_86480_74578_428469176}[：]{style="font-family:
宋体"}[X.25 PAD]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[portal]{lang="EN-US"}**]{#struct_0_86480_74578_351879852}[：表示]{lang="EN-US" style="font-family:宋体"}[Portal]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}[ ]{lang="EN-US"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ppp]{lang="EN-US"}**]{#struct_0_86480_74578_x722689633}[：]{style="font-family:
宋体"}[PPP]{lang="EN-US"}[用户。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ssh]{lang="EN-US"}**]{#struct_0_86480_74578_1522277131}[：表示]{lang="EN-US" style="font-family:宋体"}[SSH]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[**[sslvpn]{lang="EN-US"}**]{.ItemStepChar}]{#struct_0_86480_74578_1541445844}[：表示]{lang="EN-US" style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[telnet]{lang="EN-US"}**]{#struct_0_86480_74578_x1438924923}[：表示]{lang="EN-US" style="font-family:宋体"}[Telnet]{lang="EN-US"}[用户。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[terminal]{lang="EN-US"}**]{#struct_0_86480_74578_x1358803261}[：表示从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口、]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口、]{style="font-family:宋体"}[Asyn]{lang="EN-US"}[口登录的终端用户。不同型号的设备支持的接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x581716374}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1497378371}[添加名称为]{style="font-family:宋体"}[user1]{lang="EN-US"}[的设备管理类本地用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1539748855}

[\[Sysname\] local-user user1 class manage]{lang="EN-US"}

[\[Sysname-luser-manage-user1\]]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_351945388}[添加名称为]{style="font-family:宋体"}[user2]{lang="EN-US"}[的网络接入类本地用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_89694029}

[\[Sysname\] local-user user2 class network]{lang="EN-US"}

[\[Sysname-luser-network-user2\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_752889354}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_1226471734}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[service-type]{lang="EN-US"}**]{#struct_0_86480_74578_1746315256}
:::

::: {#-231203086 .myid}
[]{#_Toc404792570}[]{#struct_0_86480_74578_x165353942}[]{#_Toc268769748}[]{#_Toc205699671}[]{#_Toc162860255}[]{#_Toc147117572}[]{#_Toc147049932}[]{#_Toc146447652}[]{#_Toc69900463}[]{#_Toc320536873}[]{#_Toc320536874}[]{#_Toc320536875}[]{#_Toc320536876}[]{#_Toc320536877}[]{#_Toc320536878}[]{#_Toc320536879}[]{#_Toc320536880}[]{#_Toc320536881}[]{#_Toc320536882}[]{#_Toc320536883}[]{#_Toc320536884}[]{#_Toc320536885}[]{#_Toc320536886}[]{#_Toc320536887}[]{#_Toc320536888}[]{#_Toc320536889}[]{#_Toc320536890}[]{#_Toc320536891}[]{#_Toc320536892}[]{#_Toc320536893}[]{#_Toc320536894}[]{#_Toc320536895}[]{#_Toc320536896}[]{#_Toc320536897}

**AAA \-- 本地用户配置命令 \-- password**

------------------------------------------------------------------------

[**[password]{lang="EN-US"}**]{#struct_0_86480_74578_x273842504}[命令用来设置本地用户的密码。]{style="font-family:宋体"}

[**[undo password]{lang="EN-US"}**]{#struct_0_86480_74578_400485433}[命令用来删除本地用户的密码。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_352010924}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_1376601261}[模式下：]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**[ \[ { **cipher** \| **hash** \| **simple** } *password* \]]{lang="EN-US"}]{#struct_0_86480_74578_x1984118748}

[**[undo password]{lang="EN-US"}**]{#struct_0_86480_74578_1519931976}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x1091924121}[模式下：]{style="font-family:宋体"}

[**[password]{lang="EN-US"}**]{#struct_0_86480_74578_1084168576}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_983356030}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x707382624}[模式下：]{style="font-family:宋体"}

[[不存在本地用户密码，即本地用户认证时无需输入密码，只要用户名有效且其它属性验证通过即可认证成功。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1888876568}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_351027884}[模式下：]{style="font-family:宋体"}

[[不存在本地用户密码，但本地用户认证时不能成功。]{style="font-family:宋体"}]{#struct_0_86480_74578_x902192844}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1630406565}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_458828638}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1718635502}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1612881229}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_709147254}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x183347959}

[**[cipher]{lang="EN-US"}**]{#struct_0_86480_74578_x1428577697}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[hash]{lang="EN-US"}**]{#struct_0_86480_74578_351093420}[：表示以哈希方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_86480_74578_x2089431545}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[password]{lang="EN-US"}*]{#struct_0_86480_74578_1939824617}[：设置的明文密码或密文密码，区分大小写。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串；哈希密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[110]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密码为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，密码元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_243614118}

[[如果不指定任何参数，则表示以交互式方式设置本地用户密码，涵义与指定]{style="font-family:宋体"}**[simple]{lang="EN-US"}**]{#struct_0_86480_74578_609325990}[关键字相同。若不设置本地用户密码，则本地用户认证时无需输入密码，只要用户名有效且其它属性验证通过即可认证成功。因此为提高用户帐户的安全性，建议设置本地用户密码。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1696735603}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于设备管理类本地用户，可以使用交互式方式、明文或哈希方式设置用户密码，设置的明文密码将以哈希计算后生成的密文形式保存在配置文件中，设置的哈希密码将以设置的原始形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_139114012}[FIPS]{lang="EN-US"}[模式下，只支持交互式方式设置本地用户密码，且必须设置本地用户密码，否则用户的本地认证不能成功。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[对于网络接入类本地用户，可以使用明文或密文方式设置用户密码，设置的明文密码将以加密后生成的密文形式保存在配置文件中，设置的密文密码将以设置的原始形式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_1411078284}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1998170613}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_351552169}[设置设备管理类本地用户]{style="font-family:宋体"}[user1]{lang="EN-US"}[的密码为明文]{style="font-family:宋体"}[123456TESTplat&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_2132067}

[\[Sysname\] local-user user1 class manage]{lang="EN-US"}

[\[Sysname-luser-manage-user1\] password simple 123456TESTplat&!]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_152151852}[以交互式方式设置设备管理类本地用户]{style="font-family:宋体"}[test]{lang="EN-US"}[的密码。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1003542550}

[\[Sysname\] local-user test class manage]{lang="EN-US"}

[\[Sysname-luser-manage-test\] password]{lang="EN-US"}

[Password:]{lang="EN-US"}

[Confirm :]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_2055879182}[设置网络接入类本地用户]{style="font-family:宋体"}[user2]{lang="EN-US"}[的密码为明文]{style="font-family:宋体"}[123456TESTuser&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_351617705}

[\[Sysname\] local-user user1 class network]{lang="EN-US"}

[\[Sysname-luser-network-user1\] password simple 123456TESTuser&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x491818727}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_732463571}
:::

::: {#-393956928 .myid}
[]{#_Toc404792571}[]{#struct_0_86480_74578_457726630}[]{#_Toc268769749}[]{#_Toc205699673}[]{#_Toc162860257}[]{#_Toc147117574}[]{#_Toc147049934}[]{#_Toc146447654}[]{#_Toc69900465}

**AAA \-- 本地用户配置命令 \-- service-type**

------------------------------------------------------------------------

[**[service-type]{lang="EN-US"}**]{#struct_0_86480_74578_1780866023}[命令用来设置用户可以使用的服务类型。]{style="font-family:宋体"}

[**[undo service-type]{lang="EN-US"}**]{#struct_0_86480_74578_x1780719711}[命令用来删除用户可以使用的服务类型。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x136676205}

[[非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_278264223}[模式下：]{style="font-family:宋体"}

[**[service-type ]{lang="EN-US"}**[{ **advpn** \| **ftp** \| **ipoe** \| **lan-access** \| { **http** \| **https** \| **pad** \| **ssh** \| **telnet** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]{lang="EN-US"}]{#struct_0_86480_74578_351683241}

[**[undo service-type ]{lang="EN-US"}**[{ **dvpn** \| **ftp** \| **ipoe** \| **lan-access** \| { **http** \| **https** \| **pad** \| **ssh** \| **telnet** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]{lang="EN-US"}]{#struct_0_86480_74578_667488773}

[[FIPS]{lang="EN-US"}]{#struct_0_86480_74578_x816029811}[模式下：]{style="font-family:宋体"}

[**[service-type ]{lang="EN-US"}**[{ **dvpn** \| **ipoe** \| **lan-access** \| { **https** \| **pad** \| **ssh** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]{lang="EN-US"}]{#struct_0_86480_74578_x1849097739}

[**[undo service-type ]{lang="EN-US"}**[{ **dvpn** \| **ipoe** \| **lan-access** \| { **https** \| **pad** \| **ssh** \| **terminal** } \* \| **portal** \| **ppp** \| **sslvpn** }]{lang="EN-US"}]{#struct_0_86480_74578_x695936911}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1501237182}

[[系统不对用户授权任何服务，即用户不能使用任何服务。]{style="font-family:宋体"}]{#struct_0_86480_74578_351748777}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1073377732}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x248611788}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x228424141}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_448212720}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1962655711}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1872272016}

[**[advpn]{lang="EN-US"}**]{#struct_0_86480_74578_1832656510}[：指定用户可以使用]{style="font-family:宋体"}[ADVPN]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ftp]{lang="EN-US"}**]{#struct_0_86480_74578_351814313}[：指定用户可以使用]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务。若授权]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务，缺省授权]{style="font-family:宋体"}[FTP]{lang="EN-US"}[用户可访问设备的根目录，授权目录可以通过]{style="font-family:宋体"}**[authorization-attribute work-directory]{lang="EN-US"}**[命令来修改。]{style="font-family:宋体"}

[**[http]{lang="EN-US"}**]{#struct_0_86480_74578_117153455}[：指定用户可以使用]{style="font-family:宋体"}[HTTP]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[https]{lang="EN-US"}**]{#struct_0_86480_74578_x292944179}[：指定用户可以使用]{style="font-family:宋体"}[HTTPS]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ipoe]{lang="EN-US"}**]{#struct_0_86480_74578_x345288447}[：指定用户可以使用]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[lan-access]{lang="EN-US"}**]{#struct_0_86480_74578_x496109327}[：指定用户可以使用]{style="font-family:宋体"}[lan-access]{lang="EN-US"}[服务。主要指以太网接入，比如用户可以通过]{style="font-family:宋体"}[802.1X]{lang="EN-US"}[认证接入。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[pad]{lang="EN-US"}**]{#struct_0_86480_74578_x828961747}[：指定用户可以使用]{style="font-family:宋体"}[X.25 PAD]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ssh]{lang="EN-US"}**]{#struct_0_86480_74578_683570772}[：指定用户可以使用]{style="font-family:宋体"}[SSH]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[telnet]{lang="EN-US"}**]{#struct_0_86480_74578_1505990848}[：指定用户可以使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[**[terminal]{lang="EN-US"}**]{#struct_0_86480_74578_x1272569146}[：指定用户可以使用]{style="font-family:宋体"}[terminal]{lang="EN-US"}[服务（即从]{style="font-family:宋体"}[Console]{lang="EN-US"}[口、]{style="font-family:宋体"}[AUX]{lang="EN-US"}[口、]{style="font-family:宋体"}[Asyn]{lang="EN-US"}[口登录）。不同型号的设备支持的用户登录接口类型不同，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[portal]{lang="EN-US"}**]{#struct_0_86480_74578_x1694607959}[：指定用户可以使用]{style="font-family:宋体"}[Portal]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[ppp]{lang="EN-US"}**]{#struct_0_86480_74578_351879849}[：指定用户可以使用]{style="font-family:宋体"}[PPP]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[**[sslvpn]{lang="EN-US"}**]{#struct_0_86480_74578_x24572561}[：指定用户可以使用]{style="font-family:宋体"}[SSL VPN]{lang="EN-US"}[服务。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1233625492}

[[可以通过多次执行本命令，设置用户可以使用多种服务类型。]{style="font-family:宋体"}]{#struct_0_86480_74578_1394593241}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x799868363}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1766686258}[指定设备管理类用户可以使用]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[服务和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1667214635}

[\[Sysname\] local-user user1 class manage]{lang="EN-US"}

[\[Sysname-luser-manage-user1\] service-type telnet]{lang="FR"}

[\[Sysname-luser-manage-user1\] service-type ftp]{lang="FR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_943072888}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_x989866078}
:::

::: {#582462387 .myid}
[]{#_Toc404792572}[]{#struct_0_86480_74578_351945385}[]{#_Toc268769750}

**AAA \-- 本地用户配置命令 \-- state（Local user view）**

------------------------------------------------------------------------

[**[state]{lang="EN-US"}**]{#struct_0_86480_74578_89694042}[命令用来设置当前本地用户的状态。]{style="font-family:宋体"}

[**[undo state]{lang="EN-US"}**]{#struct_0_86480_74578_x1187637440}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1653885412}

[**[state]{lang="EN-US"}**[ { **active** \| **block** }]{lang="EN-US"}]{#struct_0_86480_74578_x1658197935}

[**[undo state]{lang="EN-US"}**]{#struct_0_86480_74578_x1128667209}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2128181395}

[[当一个本地用户被创建以后，其状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_x848459334}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1531194050}

[[本地用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_352010921}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1376601264}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1983922140}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1893799296}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1416052434}

[**[active]{lang="EN-US"}**]{#struct_0_86480_74578_884612080}[：指定当前本地用户处于活动状态，即系统允许当前本地用户请求网络服务。]{style="font-family:宋体"}

[**[block]{lang="EN-US"}**]{#struct_0_86480_74578_x1341825666}[：指定当前本地用户处于"阻塞"状态，即系统不允许当前本地用户请求网络服务。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x339235193}

[[本命令仅对当前用户生效，不影响其它用户。]{style="font-family:宋体"}]{#struct_0_86480_74578_351027881}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x902192839}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1629554600}[设置设备管理类本地用户]{style="font-family:宋体"}[user1]{lang="EN-US"}[处于"阻塞"状态。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1771872048}

[\[Sysname\] local-user user1 class manage]{lang="EN-US"}

[\[Sysname-luser-manage-user1\] state block]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1877432441}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display local-user]{lang="EN-US"}**]{#struct_0_86480_74578_676785823}
:::

::::: {#1099864600 .myid}
[]{#_Toc404792573}[]{#struct_0_86480_74578_x1195601293}[]{#_Toc268769751}[]{#_Toc205699676}

**AAA \-- 本地用户配置命令 \-- user-group**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 2 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_499987058}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_351093417}
:::

[ ]{lang="EN-US"}

[**[user-group]{lang="EN-US"}**]{#struct_0_86480_74578_631557632}[命令用来创建用户组，并进入其视图。]{style="font-family:宋体"}

[**[undo user-group]{lang="EN-US"}**]{#struct_0_86480_74578_931057679}[命令用来删除指定的用户组。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1535505447}

[**[user-group]{lang="EN-US"}**[ *group-name*]{lang="EN-US"}]{#struct_0_86480_74578_2070487632}

[**[undo user-group ]{lang="EN-US"}***[group-name]{lang="EN-US"}*]{#struct_0_86480_74578_x493391852}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x198397650}

[[存在一个名称为]{style="font-family:宋体"}[system]{lang="EN-US"}]{#struct_0_86480_74578_1767610980}[的用户组。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1258728559}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_351552170}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1958447212}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x430377905}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1405912161}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1280194959}

[*[group-name]{lang="EN-US"}*]{#struct_0_86480_74578_687229380}[：用户组名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1896909787}

[[用户组是一个本地用户的集合，某些需要集中管理的属性可在用户组中统一配置和管理。目前，用户组中可配置的内容为本地用户的授权属性。]{style="font-family:宋体"}]{#struct_0_86480_74578_717176347}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1852469422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当用户组中有本地用户时，不允许使用]{lang="EN-US" style="font-family:宋体"}**[undo user-group]{lang="EN-US"}**]{#struct_0_86480_74578_351617706}[删除该用户组。]{lang="EN-US" style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[不能删除系统中存在的默认用户组]{style="font-family:宋体"}]{#struct_0_86480_74578_x491818728}[system]{lang="EN-US"}[，但可以修改该用户组的配置。]{style="font-family:宋体"}

[]{#_Toc69900471}[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_731480531}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1803531657}[创建名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[的用户组并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_991918474}

[\[Sysname\] user-group abc]{lang="EN-US"}

[\[Sysname-ugroup-abc\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1440287362}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display user-group]{lang="EN-US"}**]{#struct_0_86480_74578_x1725129142}
:::::

::: {#-686797348 .myid}
[]{#_Toc404792575}[]{#struct_0_86480_74578_351683242}[]{#_Toc268769753}[]{#_Toc205699679}[]{#_Toc162860263}

**AAA \-- RADIUS配置命令 \-- accounting-on enable**

------------------------------------------------------------------------

[**[accounting-on enable]{lang="EN-US"}**]{#struct_0_86480_74578_667488770}[命令用来配置]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[**[undo accounting-on enable]{lang="EN-US"}**]{#struct_0_86480_74578_x816029808}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1848507914}

[**[accounting-on enable ]{lang="EN-US"}**[\[ **interval** *seconds* \| **send** *send-times* \] \*]{lang="EN-US"}]{#struct_0_86480_74578_35015514}

[**[undo accounting-on enable]{lang="EN-US"}**]{#struct_0_86480_74578_1785497739}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1105777857}

[[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_x1379434145}[功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2050056025}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351748778}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1073377721}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x248415181}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1406422139}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_629136519}

[**[interval]{lang="EN-US"}**[ *seconds*]{lang="EN-US"}]{#struct_0_86480_74578_1204590685}[：指定]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[报文重发时间间隔，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[15]{lang="EN-US"}[，单位为秒，缺省值为]{style="font-family:宋体"}[3]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[send]{lang="EN-US"}**[ *send-times*]{lang="EN-US"}]{#struct_0_86480_74578_210707279}[：指定]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[报文的最大发送次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[50]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_468987436}

[[在]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_x147704976}[功能处于使能的情况下，若设备重启，则设备会在重启之后发送]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[报文通知该方案所使用的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器，要求]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器停止计费且强制该设备的用户下线。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_351814314}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[执行完该命令后，请执行]{lang="EN-US" style="font-family:宋体"}**[save]{lang="EN-US"}**]{#struct_0_86480_74578_117153454}[操作，以保证设备重启后]{lang="EN-US" style="font-family:宋体"}[accounting-on]{lang="EN-US"}[功能生效。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在执行]{style="font-family:宋体"}]{#struct_0_86480_74578_x292944180}[accounting-on]{lang="EN-US"}[功能的过程中，使用该命令重新设置的报文重发间隔时间以及报文最大发送次数会立即生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x496568066}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x815890128}[使能]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[功能，并配置]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[报文重发时间间隔为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒、]{style="font-family:宋体"}[accounting-on]{lang="EN-US"}[报文的最大发送次数为]{style="font-family:宋体"}[15]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_258003747}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] accounting-on enable interval 5 send 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_344574138}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_702066698}
:::

::: {#-1516149597 .myid}
[]{#_Toc404792576}[]{#struct_0_86480_74578_x610652617}

**AAA \-- RADIUS配置命令 \-- attribute 15 check-mode**

------------------------------------------------------------------------

[**[attribute 15 check-mode]{lang="EN-US"}**]{#struct_0_86480_74578_x1972704855}[命令用来配置]{style="font-family:宋体"}[RADIUS Attribute 15]{lang="EN-US"}[的检查方式。]{style="font-family:宋体"}

[**[undo attribute 15 check-mode]{lang="EN-US"}**]{#struct_0_86480_74578_1406620352}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x611111364}

[**[attribute 15 check-mode ]{lang="EN-US"}**[{ **loose** \| **strict** }]{lang="EN-US"}]{#struct_0_86480_74578_721771900}

[**[undo attribute 15 check-mode]{lang="EN-US"}**]{#struct_0_86480_74578_x170517737}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1646872934}

[[RADIUS Attribute 15]{lang="EN-US"}]{#struct_0_86480_74578_x1077782118}[的检查方式为]{style="font-family:宋体"}**[strict]{lang="EN-US"}**[方式。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x611176900}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1579959473}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1684456404}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x244490205}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1118629554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1039743669}

[**[loose]{lang="EN-US"}**]{#struct_0_86480_74578_x611242436}[：松散检查方式。设备使用]{style="font-family:宋体"}[RADIUS Attribute 15]{lang="EN-US"}[的标准属性值对用户业务类型进行检查，对于]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[Terminal]{lang="EN-US"}[用户，在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器下发的]{style="font-family:宋体"}[Login-Service]{lang="EN-US"}[属性值为]{style="font-family:宋体"}[0]{lang="EN-US"}[（表示用户业务类型为]{style="font-family:宋体"}[Telnet]{lang="EN-US"}[）时才，这类用户才能够通过认证。]{style="font-family:宋体"}

[**[strict]{lang="EN-US"}**]{#struct_0_86480_74578_x804132669}[：严格检查方式。设备使用]{style="font-family:宋体"}[RADIUS Attribute 15]{lang="EN-US"}[的标准属性值以及扩展属性值对用户业务类型进行检查，对于]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[Terminal]{lang="EN-US"}[用户，当]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器下发的]{style="font-family:宋体"}[Login-Service]{lang="EN-US"}[属性值为对应的扩展取值时，这类用户才能够通过认证。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x292288605}

[[由于某些]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1612873557}[服务器不支持自定义的属性，无法下发扩展的]{style="font-family:宋体"}[Login-Service]{lang="EN-US"}[属性，若要使用这类]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器对]{style="font-family:宋体"}[SSH]{lang="EN-US"}[、]{style="font-family:宋体"}[FTP]{lang="EN-US"}[、]{style="font-family:宋体"}[Terminal]{lang="EN-US"}[用户进行认证，建议设备上对]{style="font-family:宋体"}[RADIUS 15]{lang="EN-US"}[号属性值采用松散检查方式。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1718678300}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x611307972}[在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图]{style="font-family:宋体"}[radius1]{lang="EN-US"}[下，配置]{style="font-family:宋体"}[RADIUS Attribute 15]{lang="EN-US"}[的检查方式为]{style="font-family:宋体"}[loose]{lang="EN-US"}[方式。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x24688913}

[\[Sysname\] radius scheme ]{lang="EN-US"}[radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] attribute 15 check-mode loose]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_658844486}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1814549650}
:::

::: {#-135827509 .myid}
[]{#_Toc335845114}[]{#_Toc404792577}[]{#struct_0_86480_74578_71619156}[]{#_Toc335845126}

**AAA \-- RADIUS配置命令 \-- attribute 25 car**

------------------------------------------------------------------------

[**[attribute 25 car]{lang="EN-US"}**]{#struct_0_86480_74578_x640120231}[命令用来开启]{style="font-family:宋体"}[RADIUS Attribute 25]{lang="EN-US"}[的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数解析功能。]{style="font-family:宋体"}

[**[undo attribute 25 car]{lang="EN-US"}**]{#struct_0_86480_74578_71946836}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x70391213}

[**[attribute 25 car]{lang="EN-US"}**]{#struct_0_86480_74578_72012372}

[**[undo attribute 25 car]{lang="EN-US"}**]{#struct_0_86480_74578_x188976842}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_71422549}

[[RADIUS Attribute 25]{lang="EN-US"}]{#struct_0_86480_74578_1527210213}[的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数解析功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x124308446}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_71488085}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1812715571}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_71291477}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x206328125}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_71357013}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_996708344}[的]{style="font-family:宋体"}[25]{lang="EN-US"}[号属性为]{style="font-family:宋体"}[class]{lang="EN-US"}[属性，该属性由]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器下发给设备，但]{style="font-family:宋体"}[RFC]{lang="EN-US"}[中并未定义具体的用途，仅规定了设备需要将服务器下发的]{style="font-family:宋体"}[class]{lang="EN-US"}[属性再原封不动地携带在计费请求报文中发送给服务器即可，同时]{style="font-family:宋体"}[RFC]{lang="EN-US"}[并未要求设备必须对该属性进行解析。目前，某些]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器利用]{style="font-family:宋体"}[class]{lang="EN-US"}[属性来对用户下发]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数，为了支持这种应用，可以通过本特性来控制设备是否将]{style="font-family:宋体"}[RADIUS 25]{lang="EN-US"}[号属性解析为]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数，解析出的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数可被用来进行基于用户的流量监管控制。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x666906839}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_71684693}[在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图]{style="font-family:宋体"}[test]{lang="EN-US"}[下，开启]{style="font-family:宋体"}[RADIUS Attribute 25]{lang="EN-US"}[的]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数解析功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x365948152}

[\[Sysname\]radius scheme test]{lang="EN-US"}

[\[Sysname-radius-test\] attribute 25 car]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_71750229}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1882780230}
:::

::: {#-1874807237 .myid}
[]{#_Toc404792578}[]{#struct_0_86480_74578_1165049655}

**AAA \-- RADIUS配置命令 \-- attribute remanent-volume**

------------------------------------------------------------------------

[**[attribute remanent-volume]{lang="EN-US"}**]{#struct_0_86480_74578_x1066785902}[命令用来配置]{style="font-family:
宋体"}[RADIUS ]{lang="EN-US"}[Remanent-Volume]{lang="EN-US"}[属性的流量单位。]{style="font-family:宋体"}

[**[undo attribute remanent-volume]{lang="EN-US"}**]{#struct_0_86480_74578_116091417}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1238227692}

[**[attribute remanent-volume unit ]{lang="EN-US"}**[{ **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** }]{lang="EN-US"}]{#struct_0_86480_74578_x8083721}

[**[undo attribute remanent-volume unit]{lang="EN-US"}**]{#struct_0_86480_74578_1644243310}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1766666371}

[[Remanent-Volume]{lang="EN-US"}]{#struct_0_86480_74578_880721297}[属性的流量单位是千字节。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1563833700}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_275204010}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2144462705}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_997064240}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_589839267}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1372561763}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x945570801}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1034481361}

[**[byte]{lang="EN-US"}**]{#struct_0_86480_74578_529885649}[：表示流量单位为字节。]{style="font-family:宋体"}

[**[giga-byte]{lang="EN-US"}**]{#struct_0_86480_74578_664940398}[：表示流量单位为千兆字节。]{style="font-family:宋体"}

[**[kilo-byte]{lang="EN-US"}**]{#struct_0_86480_74578_1400746185}[：表示流量单位为千字节。]{style="font-family:宋体"}

[**[mega-byte]{lang="EN-US"}**]{#struct_0_86480_74578_714710961}[：表示流量单位为兆字节。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2092547163}

[[Remanent-Volume]{lang="EN-US"}]{#struct_0_86480_74578_1345598071}[属性为]{style="font-family:宋体"}[H3C]{lang="EN-US"}[自定义]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[属性，携带在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送给接入设备的认证响应或实时计费响应报文中，用于向接入设备通知在线用户的剩余流量值。设备管理员通过本命令设置的流量单位]{style="font-family:宋体"}[应与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器上统计用户流量的单位保持一致，否则设备无法正确使用]{style="font-family:宋体"}[Remanent-Volume]{lang="EN-US"}[属性值对用户进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_191555590}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1915198893}[在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[中，设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器下发的]{style="font-family:宋体"}[Remanent-Volume]{lang="EN-US"}[属性的流量单位为千字节。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_385952711}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] attribute remanent-volume unit kilo-byte]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1387402056}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1722905001}
:::

::: {#848233114 .myid}
[]{#struct_0_86480_74578_71553621}[]{#_Toc404792579}

**AAA \-- RADIUS配置命令 \-- client**

------------------------------------------------------------------------

[**[client]{lang="EN-US"}**]{#struct_0_86480_74578_1897999191}[命令用来指定]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[**[undo client]{lang="EN-US"}**]{#struct_0_86480_74578_71619157}[命令用来删除指定的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1316194905}

[**[client ]{lang="EN-US"}**[{ **ip** *ipv4-address* \| **ipv6** *ipv6-address* } \[ **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}]{#struct_0_86480_74578_27383666}

[**[undo client ]{lang="EN-US"}**[{ **ip** *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_71946837}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2026706349}

[[未指定]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_72012373}[客户端。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1767338294}

[[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_71422546}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_335569125}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1208244167}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1569455493}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_71488082}

[**[ip]{lang="EN-US"}***[ ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x143599565}[：]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_71291474}[：]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[key ]{lang="EN-US"}**[{ **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_1749987011}[：与]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端交互]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文时使用的共享密钥。此共享密钥的设置必须与]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端的共享密钥设置保持一致。如果此处未指定本参数，则对应的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端上也必须未指定。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_71357010}[：以密文方式设置共享密钥。非]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{lang="EN-US" style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{lang="EN-US" style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[15]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1341943816}[：以明文方式设置共享密钥。非]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{lang="EN-US" style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[1]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{lang="EN-US" style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{lang="EN-US" style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[15]{lang="EN-US"}[～]{lang="EN-US" style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写，密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{lang="EN-US" style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_86480_74578_x1021072329}[：]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}[vpn-instance-name]{lang="EN-US"}[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_71684690}

[[使能]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_1972704008}[服务之后，设备会监听并处理指定的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端发起的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求消息（用于动态授权修改或断开连接），并向其发送应答消息。对于非指定的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文进行丢弃处理。]{style="font-family:宋体"}

[[可通过多次执行本命令指定多个]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_71750226}[客户端。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1162736198}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_71553618}[设置]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，与]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端交互]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文时使用的共享密钥为明文]{style="font-family:宋体"}[123456]{lang="EN-US"}[，]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称为]{style="font-family:宋体"}[abc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1141219314}

[\[Sysname\]radius dynamic-author server]{lang="EN-US"}

[\[Sysname-radius-da-server\]client ip 10.110.1.2 key simple 123456 vpn-instance abc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_71619154}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_x1022457255}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port]{lang="EN-US"}**]{#struct_0_86480_74578_71946834}
:::

::: {#-1394077759 .myid}
[]{#_Toc69900490}[]{#_Toc268769756}[]{#_Toc205699683}[]{#_Toc162860267}[]{#_Toc147117584}[]{#_Toc147049944}[]{#_Toc146447664}[]{#_Toc404792580}[]{#struct_0_86480_74578_351879850}[]{#_Toc315873220}[]{#_Toc268769755}[]{#_Toc205699682}[]{#_Toc162860266}[]{#_Toc147117582}[]{#_Toc147049942}[]{#_Toc146447662}[]{#_Toc245641221}[]{#_Toc245641222}[]{#_Toc245641223}[]{#_Toc245641224}[]{#_Toc245641225}[]{#_Toc245641226}[]{#_Toc245641227}[]{#_Toc245641228}[]{#_Toc245641229}[]{#_Toc245641230}[]{#_Toc245641231}[]{#_Toc245641232}[]{#_Toc245641233}[]{#_Toc245641234}[]{#_Toc245641235}[]{#_Toc245641236}[]{#_Toc245641237}[]{#_Toc245641238}[]{#_Toc245641239}[]{#_Toc245641240}[]{#_Toc245641241}[]{#_Toc245641244}[]{#_Toc245641246}[]{#_Toc245641248}[]{#_Toc245641249}[]{#_Toc245641250}[]{#_Toc245641251}[]{#_Toc245641252}[]{#_Toc245641253}[]{#_Toc245641254}[]{#_Toc245641255}[]{#_Toc245641256}[]{#_Toc245641257}[]{#_Toc245641258}[]{#_Toc245641259}[]{#_Toc245641260}[]{#_Toc245641261}[]{#_Toc245641262}[]{#_Toc245641263}[]{#_Toc245641264}[]{#_Toc245641267}[]{#_Toc156363407}[]{#_Toc156377056}[]{#_Toc156377292}[]{#_Toc156635093}[]{#_Toc156636032}[]{#_Toc156363408}[]{#_Toc156377057}[]{#_Toc156377293}[]{#_Toc156635094}[]{#_Toc156636033}[]{#_Toc156363409}[]{#_Toc156377058}[]{#_Toc156377294}[]{#_Toc156635095}[]{#_Toc156636034}[]{#_Toc156363410}[]{#_Toc156377059}[]{#_Toc156377295}[]{#_Toc156635096}[]{#_Toc156636035}[]{#_Toc156363411}[]{#_Toc156377060}[]{#_Toc156377296}[]{#_Toc156635097}[]{#_Toc156636036}[]{#_Toc156363412}[]{#_Toc156377061}[]{#_Toc156377297}[]{#_Toc156635098}[]{#_Toc156636037}[]{#_Toc156363413}[]{#_Toc156377062}[]{#_Toc156377298}[]{#_Toc156635099}[]{#_Toc156636038}[]{#_Toc156363414}[]{#_Toc156377063}[]{#_Toc156377299}[]{#_Toc156635100}[]{#_Toc156636039}[]{#_Toc156363415}[]{#_Toc156377064}[]{#_Toc156377300}[]{#_Toc156635101}[]{#_Toc156636040}[]{#_Toc156363416}[]{#_Toc156377065}[]{#_Toc156377301}[]{#_Toc156635102}[]{#_Toc156636041}[]{#_Toc156363417}[]{#_Toc156377066}[]{#_Toc156377302}[]{#_Toc156635103}[]{#_Toc156636042}[]{#_Toc156363418}[]{#_Toc156377067}[]{#_Toc156377303}[]{#_Toc156635104}[]{#_Toc156636043}[]{#_Toc156363419}[]{#_Toc156377068}[]{#_Toc156377304}[]{#_Toc156635105}[]{#_Toc156636044}[]{#_Toc156363424}[]{#_Toc156377073}[]{#_Toc156377309}[]{#_Toc156635110}[]{#_Toc156636049}[]{#_Toc156363425}[]{#_Toc156377074}[]{#_Toc156377310}[]{#_Toc156635111}[]{#_Toc156636050}[]{#_Toc156363453}[]{#_Toc156377102}[]{#_Toc156377338}[]{#_Toc156635139}[]{#_Toc156636078}

**AAA \-- RADIUS配置命令 \-- data-flow-format (RADIUS scheme view)**

------------------------------------------------------------------------

[**[data-flow-format]{lang="EN-US"}**]{#struct_0_86480_74578_x722689635}[命令用来配置发送到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的数据流及数据包的单位。]{style="font-family:宋体"}

[**[undo data-flow-format]{lang="EN-US"}**]{#struct_0_86480_74578_1521883915}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x539127639}

[**[data-flow-format ]{lang="EN-US"}**[{ **data** { **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** } \| **packet** { **giga-packet** \| **kilo-packet** \| **mega-packet** \| **one-packet** } } \*]{lang="EN-US"}]{#struct_0_86480_74578_x2103802817}

[**[undo data-flow-format ]{lang="EN-US"}**[{ **data** \| **packet** }]{lang="EN-US"}]{#struct_0_86480_74578_x741974066}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_987905860}

[[数据流的单位为]{style="font-family:宋体"}**[byte]{lang="EN-US"}**]{#struct_0_86480_74578_1850518967}[，数据包的单位为]{style="font-family:宋体"}**[one-packet]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1861142848}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351945386}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_89694039}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x813194587}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1214012290}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1435098118}

[**[data]{lang="EN-US"}**]{#struct_0_86480_74578_x490948110}[：设置数据流的单位。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[byte]{lang="EN-US"}**]{#struct_0_86480_74578_723354035}[：数据流的单位为字节。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[giga-byte]{lang="EN-US"}**]{#struct_0_86480_74578_x1347552521}[：数据流的单位千兆字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[kilo-byte]{lang="EN-US"}**]{#struct_0_86480_74578_546586690}[：数据流的单位为千字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mega-byte]{lang="EN-US"}**]{#struct_0_86480_74578_352010922}[：数据流的单位为兆字节。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_86480_74578_1376601263}[：设置数据包的单位。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[giga-packet]{lang="EN-US"}**]{#struct_0_86480_74578_x1983987676}[：数据包的单位为千兆包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[kilo-packet]{lang="EN-US"}**]{#struct_0_86480_74578_x345888255}[：数据包的单位为千包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mega-packet]{lang="EN-US"}**]{#struct_0_86480_74578_578533029}[：数据包的单位为兆包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[one-packet]{lang="EN-US"}**]{#struct_0_86480_74578_x1231919465}[：数据包的单位为包。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x403561852}

[[设备上配置的发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1424844259}[服务器的数据流单位及数据包单位应与]{style="font-family:宋体"}[RADUIS]{lang="EN-US"}[服务器上的流量统计单位保持一致，否则无法正确计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1017405551}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_351027882}[在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[中，设置发往]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的数据流单位为千字节、数据包单位为千包。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x902192838}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] data-flow-format data kilo-byte packet kilo-packet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1629620136}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1405275236}
:::

::: {#-1505001864 .myid}
[]{#_Toc404792581}[]{#struct_0_86480_74578_964481409}

**AAA \-- RADIUS配置命令 \-- display radius scheme**

------------------------------------------------------------------------

[**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_965644274}[命令用来显示所有或指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1397597958}

[**[display radius scheme]{lang="EN-US"}**[ \[ *radius-scheme-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_x30183467}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_351093418}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_631557631}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_931057680}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_38472672}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1052250930}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_797532458}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x2019103340}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x347169033}

[*[radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1080874435}[：显示]{style="font-family:宋体"}[指定的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案的配置信息。]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_351552167}

[[如果不指定]{style="font-family:宋体"}]{#struct_0_86480_74578_2132077}[RADIUS]{lang="DE"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则显示所有]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_152086316}

[[\# ]{lang="DE"}]{#struct_0_86480_74578_622170286}[显示所有]{style="font-family:宋体"}[RADIUS]{lang="DE"}[方案的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display radius scheme]{lang="EN-US"}]{#struct_0_86480_74578_351617703}

[Total 1 RADIUS schemes]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[RADIUS scheme name  : radius1]{lang="EN-US"}

[  Index : 0]{lang="EN-US"}

[  Primary authentication server:]{lang="EN-US"}

[    IP   : 2.2.2.2                                  Port: 1812]{lang="EN-US"}

[    VPN  : vpn1]{lang="EN-US"}

[    State: Active]{lang="EN-US"}

[    Test profile: 132]{lang="EN-US"}

[      Probe username: test]{lang="EN-US"}

[      Probe interval: 60 minutes]{lang="EN-US"}

[  Primary accounting server:]{lang="EN-US"}

[    IP : 1.1.1.1                                    Port: 1813]{lang="EN-US"}

[    VPN : Not configured]{lang="EN-US"}

[    State: Active]{lang="EN-US"}

[  Second authentication server:]{lang="EN-US"}

[    IP: Not configured                             Port: 1812]{lang="EN-US"}

[    VPN : Not configured]{lang="EN-US"}

[    State: Block]{lang="EN-US"}

[    Test profile: Not configured]{lang="EN-US"}

[  Second accounting server:]{lang="EN-US"}

[    IP : 3.3.3.3                                    Port: 1813]{lang="EN-US"}

[    State: Block (Mandatory)]{lang="EN-US"}

[    VPN : Not configured]{lang="EN-US"}

[  Security policy server:]{lang="EN-US"}

[    Server: 0     IP: 2.2.2.2         VPN: Not configured ]{lang="EN-US"}

[    Server: 1     IP: 3.3.3.3         VPN: 2]{lang="EN-US"}

[ ]{lang="EN-US"}

[  Accounting-On function                     : Enabled]{lang="EN-US"}

[    retransmission times                     : 5]{lang="EN-US"}

[    retransmission interval(seconds)         : 2]{lang="EN-US"}

[  Timeout Interval(seconds)                  : 3]{lang="EN-US"}

[  Retransmission Times                       : 3]{lang="EN-US"}

[  Retransmission Times for Accounting Update : 5]{lang="EN-US"}

[  Server Quiet Period(minutes)               : 5]{lang="EN-US"}

[  Realtime Accounting Interval(minutes)      : 22  ]{lang="EN-US"}

[  NAS IP Address                             : 1.1.1.1]{lang="EN-US"}

[  VPN                                        : Not configured]{lang="EN-US"}

[  User Name Format                           : with-domain]{lang="EN-US"}

[  Data flow unit                             : Megabyte]{lang="EN-US"}

[  Packet unit                                : One]{lang="EN-US"}

[  Attribute 15 check-mode                    : Strict]{lang="EN-US"}

[  Attribute 25                               : CAR]{lang="EN-US"}

[  Attribute Remanent-Volume unit             : Mega]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[]{#struct_0_86480_74578_x491818725}[]{#_Toc138066609}[]{#_Toc95386912}[]{#_Toc85621926}[]{#_Toc81452874}[[表1-4 ]{lang="EN-US"}[display radius scheme]{lang="EN-US"}]{#_Toc38965300}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_774532802}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_732332499}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_351683239}

[[Total 1 RADIUS schemes.]{lang="DE"}]{#struct_0_86480_74578_x1671163395}

[[共计]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_86480_74578_1297444821}[个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}

[[RADIUS scheme name]{lang="EN-US"}]{#struct_0_86480_74578_13642391}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x853863468}[方案的名称]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_86480_74578_x1397320390}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351748775}[方案的索引号]{style="font-family:宋体"}

[[Primary authentication server]{lang="EN-US"}]{#struct_0_86480_74578_1073377734}

[[主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x248742860}[认证服务器]{style="font-family:宋体"}

[[Primary accounting server]{lang="EN-US"}]{#struct_0_86480_74578_506472505}

[[主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x104822157}[计费服务器]{style="font-family:宋体"}

[[Second authentication server]{lang="EN-US"}]{#struct_0_86480_74578_960432299}

[[从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351814311}[认证服务器]{style="font-family:宋体"}

[[Second accounting server]{lang="EN-US"}]{#struct_0_86480_74578_117153457}

[[从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x292944181}[计费服务器]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_86480_74578_x496633602}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1079429270}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_351879847}

[[Port]{lang="EN-US"}]{#struct_0_86480_74578_1233625506}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x943796782}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器接入端口号]{style="font-family:宋体"}

[[未配置时，显示缺省值]{style="font-family:宋体"}]{#struct_0_86480_74578_x902933033}

[[State]{lang="EN-US"}]{#struct_0_86480_74578_1580236075}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351945383}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器目前状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_86480_74578_89694036}[：激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Block]{lang="EN-US"}]{#struct_0_86480_74578_x386227547}[：自动转换的静默状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Block(Mandatory)]{lang="EN-US"}]{#struct_0_86480_74578_1637834171}[：手工配置的静默状态]{lang="EN-US" style="font-family:宋体"}

[[VPN]{lang="EN-US"}]{#struct_0_86480_74578_860004885}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_352010919}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_x197376840}

[[Security policy server]{lang="EN-US"}]{#struct_0_86480_74578_x1218179330}

[[安全策略服务器]{style="font-family:宋体"}]{#struct_0_86480_74578_x1110586221}

[[Server: *n*]{lang="EN-US"}]{#struct_0_86480_74578_351027879}

[[安全策略服务器编号]{style="font-family:宋体"}]{#struct_0_86480_74578_1818796353}

[[IP]{lang="EN-US"}]{#struct_0_86480_74578_1503391231}

[[安全策略服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x1958963036}[地址]{style="font-family:宋体"}

[[VPN]{lang="EN-US"}]{#struct_0_86480_74578_351093415}

[[安全策略服务器所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_631557634}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_931057677}

[[Test profile]{lang="EN-US"}]{#struct_0_86480_74578_1637703099}

[[探测服务器状态使用的模版名称]{style="font-family:宋体"}]{#struct_0_86480_74578_1638030779}

[[Probe username]{lang="EN-US"}]{#struct_0_86480_74578_1638096315}

[[探测服务器状态使用的用户名]{style="font-family:宋体"}]{#struct_0_86480_74578_1637506492}

[[Probe interval]{lang="EN-US"}]{#struct_0_86480_74578_1637572028}

[[探测服务器状态的周期（单位为分钟）]{style="font-family:宋体"}]{#struct_0_86480_74578_1637375420}

[[Accounting-On function]{lang="EN-US"}]{#struct_0_86480_74578_x1535505445}

[[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_351552168}[功能的使能情况]{style="font-family:宋体"}

[[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_2132068}[功能的显示信息的支持情况与设备的型号有关，请以设备的实际情况为准]{style="font-family:宋体"}

[[retransmission times]{lang="EN-US"}]{#struct_0_86480_74578_105097685}

[[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_x542873523}[报文的发送尝试次数]{style="font-family:宋体"}

[[retransmission interval(seconds)]{lang="EN-US"}]{#struct_0_86480_74578_351617704}

[[accounting-on]{lang="EN-US"}]{#struct_0_86480_74578_x491818726}[报文的重发间隔（单位为秒）]{style="font-family:宋体"}

[[Timeout Interval(seconds)]{lang="EN-US"}]{#struct_0_86480_74578_732398035}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351683240}[服务器超时时间（单位为秒）]{style="font-family:宋体"}

[[Retransmission Times]{lang="EN-US"}]{#struct_0_86480_74578_667488772}

[[发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x816029810}[报文的最大尝试次数]{style="font-family:宋体"}

[[Retransmission Times for Accounting Update]{lang="EN-US"}]{#struct_0_86480_74578_x1849032203}

[[实时计费更新报文的最大尝试次数]{style="font-family:宋体"}]{#struct_0_86480_74578_351748776}

[[Server Quiet Period(minutes)]{lang="EN-US"}]{#struct_0_86480_74578_1073377731}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x248415180}[服务器恢复激活状态的时间（单位为分钟）]{style="font-family:宋体"}

[[Realtime Accounting Interval(minutes)]{lang="EN-US"}]{#struct_0_86480_74578_351814312}

[[实时计费更新报文的发送间隔（单位为分钟）]{style="font-family:宋体"}]{#struct_0_86480_74578_117153456}

[[NAS IP Address]{lang="EN-US"}]{#struct_0_86480_74578_x292944182}

[[发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_351879848}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[VPN]{lang="EN-US"}]{#struct_0_86480_74578_1233625493}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1394527705}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_351945384}

[[User Name Format]{lang="EN-US"}]{#struct_0_86480_74578_89694041}

[[发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_386340672}[服务器的用户名格式]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[with-domain]{lang="EN-US"}]{#struct_0_86480_74578_352010920}[：携带域名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[without-domain]{lang="EN-US"}]{#struct_0_86480_74578_1376601265}[：不携带域名]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[keep-original]{lang="EN-US"}]{#struct_0_86480_74578_x1983856604}[：与用户输入保持一致]{lang="EN-US" style="font-family:宋体"}

[[Data flow unit]{lang="EN-US"}]{#struct_0_86480_74578_1638096316}

[[数据流的单位]{style="font-family:宋体"}]{#struct_0_86480_74578_1637506489}

[[Packet unit]{lang="EN-US"}]{#struct_0_86480_74578_1637572025}

[[数据包的单位]{style="font-family:宋体"}]{#struct_0_86480_74578_x1486094929}

[[Attribute 15 check-mode]{lang="EN-US"}]{#struct_0_86480_74578_954972573}

[[对]{style="font-family:宋体"}[RADIUS  Attribute 15]{lang="EN-US"}]{#struct_0_86480_74578_954907037}[的检查方式，包括以下两种取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Strict]{lang="EN-US"}]{#struct_0_86480_74578_954841501}[：表示使用]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[标准属性值和私有扩展的属性值进行检查]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Loose]{lang="EN-US"}]{#struct_0_86480_74578_194052905}[：表示使用]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[标准属性值进行检查]{lang="EN-US" style="font-family:宋体"}

[[Attribute 25]{lang="EN-US"}]{#struct_0_86480_74578_1637375417}

[[对]{style="font-family:宋体"}[RADIUS Attribute 25]{lang="EN-US"}]{#struct_0_86480_74578_1637440953}[的处理，包括以下两种取值：]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Standard]{lang="EN-US"}]{#struct_0_86480_74578_1637834169}[：表示不对]{style="font-family:宋体"}[RADIUS Attribute 25]{lang="EN-US"}[进行解析]{lang="EN-US" style="font-family:
  宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CAR]{lang="EN-US"}]{#struct_0_86480_74578_1637637561}[：表示将]{style="font-family:宋体"}[RADIUS 25]{lang="EN-US"}[号属性解析为]{style="font-family:宋体"}[CAR]{lang="EN-US"}[参数]{style="font-family:宋体"}

[[Attribute Remanent-Volume unit]{lang="EN-US"}]{#struct_0_86480_74578_x2100746131}

[[RADIUS ]{lang="EN-US"}[Remanent-Volume]{lang="EN-US"}]{#struct_0_86480_74578_x1566426416}[属性的流量单位]{style="font-family:宋体"}

[ ]{lang="EN-US"}

::: {#1483132697 .myid}
[]{#_Toc404792582}[]{#struct_0_86480_74578_x219523656}[]{#_Toc268769757}[]{#_Toc205699684}[]{#_Toc162860268}[]{#_Toc147117585}[]{#_Toc147049945}[]{#_Toc146447665}[]{#_Toc69900491}[]{#_Toc299047502}[]{#_Toc299112015}[]{#_Toc299130063}[]{#_Toc299130157}[]{#_Toc299047503}[]{#_Toc299112016}[]{#_Toc299130064}[]{#_Toc299130158}

**AAA \-- RADIUS配置命令 \-- display radius statistics**

------------------------------------------------------------------------

[**[display radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_x1468369742}[命令用来显示]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_351027880}

[**[display radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_x902192840}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1630144421}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1261257361}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x795769779}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x302183211}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_1300986949}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1057426429}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_1818192109}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_351093416}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_631557633}[显示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> display radius statistics]{lang="EN-US"}]{#struct_0_86480_74578_931057678}

[ ]{lang="EN-US"}

[                                 Auth.         Acct.       SessCtrl.]{lang="EN-US"}

[          Request Packet:          0             0             0]{lang="EN-US"}

[            Retry Packet:          0             0             -]{lang="EN-US"}

[          Timeout Packet:          0             0             -]{lang="EN-US"}

[        Access Challenge:          0             -             -]{lang="EN-US"}

[           Account Start:          -             0             -]{lang="EN-US"}

[          Account Update:          -             0             -]{lang="EN-US"}

[            Account Stop:          -             0             -]{lang="EN-US"}

[       Terminate Request:          -             -             0]{lang="EN-US"}

[              Set Policy:          -             -             0]{lang="EN-US"}

[    Packet With Response:          0             0             0]{lang="EN-US"}

[ Packet Without Response:          0             0             -]{lang="EN-US"}

[          Access Rejects:          0             -             -]{lang="EN-US"}

[          Dropped Packet:          0             0             0]{lang="EN-US"}

[          Check Failures:          0             0             0]{lang="EN-US"}

[]{#struct_0_86480_74578_x1535505448}[[表1-5 ]{lang="EN-US"}[display radius statistics]{lang="EN-US"}]{#_Toc138066610}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_794072322}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_1917636112}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_1461906968}

[[Auth.]{lang="EN-US"}]{#struct_0_86480_74578_x1272967607}

[[认证报文]{style="font-family:宋体"}]{#struct_0_86480_74578_x1394619841}

[[Acct.]{lang="EN-US"}]{#struct_0_86480_74578_1693802518}

[[计费报文]{style="font-family:宋体"}]{#struct_0_86480_74578_1200057967}

[[SessCtrl.]{lang="EN-US"}]{#struct_0_86480_74578_x293174847}

[[Session-control]{lang="EN-US"}]{#struct_0_86480_74578_1917701648}[报文]{style="font-family:宋体"}

[[Request Packet]{lang="EN-US"}]{#struct_0_86480_74578_x1243836371}

[[发送的请求报文总数]{style="font-family:宋体"}]{#struct_0_86480_74578_x38772681}

[[Retry Packet]{lang="EN-US"}]{#struct_0_86480_74578_1633300036}

[[重传的请求报文总数]{style="font-family:宋体"}]{#struct_0_86480_74578_1099633978}

[[Timeout Packet]{lang="EN-US"}]{#struct_0_86480_74578_790297235}

[[超时的请求报文总数]{style="font-family:宋体"}]{#struct_0_86480_74578_1917767184}

[[Access Challenge]{lang="EN-US"}]{#struct_0_86480_74578_x1277265577}

[[Access challenge]{lang="EN-US"}]{#struct_0_86480_74578_x1634481401}[报文数]{style="font-family:宋体"}

[[Account Start]{lang="EN-US"}]{#struct_0_86480_74578_608507462}

[[计费开始报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x1802949541}

[[Account Update]{lang="EN-US"}]{#struct_0_86480_74578_1917832720}

[[计费更新报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x2010572055}

[[Account Stop]{lang="EN-US"}]{#struct_0_86480_74578_x1599265945}

[[计费结束报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x725010603}

[[Terminate Request]{lang="EN-US"}]{#struct_0_86480_74578_994246771}

[[服务器强制下线报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_1917898256}

[[Set Policy]{lang="EN-US"}]{#struct_0_86480_74578_x1669814024}

[[更新用户授权信息报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_738040836}

[[Packet With Response]{lang="EN-US"}]{#struct_0_86480_74578_x1041778646}

[[有回应信息的报文数]{style="font-family:宋体"}]{#struct_0_86480_74578_x1502373795}

[[Packet Without Response]{lang="EN-US"}]{#struct_0_86480_74578_1917963792}

[[无回应信息的报文数]{style="font-family:宋体"}]{#struct_0_86480_74578_x455039434}

[[Access Rejects]{lang="EN-US"}]{#struct_0_86480_74578_x386653725}

[[认证拒绝报文的数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x1076113265}

[[Dropped Packet]{lang="EN-US"}]{#struct_0_86480_74578_1918029328}

[[丢弃的报文数]{style="font-family:宋体"}]{#struct_0_86480_74578_2034120036}

[[Check Failures]{lang="EN-US"}]{#struct_0_86480_74578_1007814710}

[[报文校验错误的报文数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x120195763}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_533766910}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_1918094864}

::: {#1865101644 .myid}
[]{#_Toc205699688}[]{#_Toc162860271}[]{#_Toc147117589}[]{#_Toc147049949}[]{#_Toc146447669}[]{#_Toc69900494}[]{#_Toc404792583}[]{#struct_0_86480_74578_2025183127}[]{#_Toc268769760}[]{#_Toc205699687}[]{#_Toc162860270}[]{#_Toc147117587}[]{#_Toc147049947}[]{#_Toc146447667}[]{#_Toc69900493}[]{#_Toc156363459}[]{#_Toc156377108}[]{#_Toc156377344}[]{#_Toc156635145}[]{#_Toc156636084}[]{#_Toc156363460}[]{#_Toc156377109}[]{#_Toc156377345}[]{#_Toc156635146}[]{#_Toc156636085}[]{#_Toc156363461}[]{#_Toc156377110}[]{#_Toc156377346}[]{#_Toc156635147}[]{#_Toc156636086}[]{#_Toc156363462}[]{#_Toc156377111}[]{#_Toc156377347}[]{#_Toc156635148}[]{#_Toc156636087}[]{#_Toc156363463}[]{#_Toc156377112}[]{#_Toc156377348}[]{#_Toc156635149}[]{#_Toc156636088}[]{#_Toc156363464}[]{#_Toc156377113}[]{#_Toc156377349}[]{#_Toc156635150}[]{#_Toc156636089}[]{#_Toc156363465}[]{#_Toc156377114}[]{#_Toc156377350}[]{#_Toc156635151}[]{#_Toc156636090}[]{#_Toc156363466}[]{#_Toc156377115}[]{#_Toc156377351}[]{#_Toc156635152}[]{#_Toc156636091}[]{#_Toc156363467}[]{#_Toc156377116}[]{#_Toc156377352}[]{#_Toc156635153}[]{#_Toc156636092}[]{#_Toc156363468}[]{#_Toc156377117}[]{#_Toc156377353}[]{#_Toc156635154}[]{#_Toc156636093}[]{#_Toc156363469}[]{#_Toc156377118}[]{#_Toc156377354}[]{#_Toc156635155}[]{#_Toc156636094}[]{#_Toc156363470}[]{#_Toc156377119}[]{#_Toc156377355}[]{#_Toc156635156}[]{#_Toc156636095}[]{#_Toc156363471}[]{#_Toc156377120}[]{#_Toc156377356}[]{#_Toc156635157}[]{#_Toc156636096}[]{#_Toc156363472}[]{#_Toc156377121}[]{#_Toc156377357}[]{#_Toc156635158}[]{#_Toc156636097}[]{#_Toc156363473}[]{#_Toc156377122}[]{#_Toc156377358}[]{#_Toc156635159}[]{#_Toc156636098}[]{#_Toc156363474}[]{#_Toc156377123}[]{#_Toc156377359}[]{#_Toc156635160}[]{#_Toc156636099}[]{#_Toc156363475}[]{#_Toc156377124}[]{#_Toc156377360}[]{#_Toc156635161}[]{#_Toc156636100}[]{#_Toc156363476}[]{#_Toc156377125}[]{#_Toc156377361}[]{#_Toc156635162}[]{#_Toc156636101}[]{#_Hlt19451951}

**AAA \-- RADIUS配置命令 \-- key (RADIUS scheme view)**

------------------------------------------------------------------------

[**[key]{lang="EN-US"}**]{#struct_0_86480_74578_2027586765}[命令用来配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的共享密钥。]{style="font-family:宋体"}

[**[undo key]{lang="EN-US"}**]{#struct_0_86480_74578_388972110}[命令用来删除]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的共享密钥。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_783737774}

[**[key]{lang="EN-US"}**[ { **accounting** \| **authentication** } { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_x531063449}

[**[undo key]{lang="EN-US"}**[ { **accounting** \| **authentication** }]{lang="EN-US"}]{#struct_0_86480_74578_x1553312187}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x406145685}

[[无共享密钥。]{style="font-family:宋体"}]{#struct_0_86480_74578_1887778782}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917111824}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1434292329}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x468320623}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1427758875}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1146131160}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x967788994}

[**[accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x667386728}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费报文的共享密钥。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x254681950}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证报文的共享密钥。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_86480_74578_x1350205901}[：表示以密文方式设置共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_86480_74578_1917177360}[：表示以明文方式设置共享密钥。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1655735901}[：设置的明文密钥或密文密钥，区分大小写。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密钥为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，密钥元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）；密文密钥为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_48695632}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_384409920}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备优先采用配置]{style="font-family:宋体"}]{#struct_0_86480_74578_x1648667449}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器时指定的报文共享密钥，本配置中指定的报文共享密钥仅在配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器时未指定相应密钥的情况下使用。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[必须保证设备上设置的共享密钥与]{style="font-family:宋体"}]{#struct_0_86480_74578_x1418336908}[RADIUS]{lang="EN-US"}[服务器上的完全一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_1168389751}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x948690001}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_596251024}[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的计费报文的共享密钥设置为明文]{style="font-family:宋体"}[ok]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1917636113}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] key accounting simple ok]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1461841432}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1078839136}
:::

::: {#-2059292624 .myid}
[]{#_Toc404792584}[]{#struct_0_86480_74578_560274061}[]{#_Toc268769763}

**AAA \-- RADIUS配置命令 \-- nas-ip (RADIUS scheme view)**

------------------------------------------------------------------------

[**[nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x1082715253}[命令用来设置设备发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x1008248817}[命令用来删除指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_889390610}

[**[nas-ip ]{lang="PT-BR"}**]{#struct_0_86480_74578_1917701649}[{ *ipv4-address* \| **ipv6**]{lang="PT-BR"}[ ]{lang="PT-BR"}*[ipv6-address]{lang="PT-BR"}*[ }]{lang="PT-BR"}

[**[undo nas-ip ]{lang="PT-BR"}**]{#struct_0_86480_74578_x1243770835}[\[ **ipv6** \]]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1525715484}

[[使用系统视图下由命令]{style="font-family:宋体"}]{#struct_0_86480_74578_x93538896}**[radius nas-ip]{lang="PT-BR"}**[指定的源地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若系统视图下未指定源地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则使用发送]{style="font-family:宋体"}[RADIUS]{lang="PT-BR"}[报文的接口的主]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1409906928}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1410984043}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_359410094}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x135770105}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x763698506}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917767185}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x1277200041}[：指定的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，应该为本机的地址，禁止配置全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址、]{style="font-family:宋体"}[D]{lang="EN-US"}[类地址、]{style="font-family:宋体"}[E]{lang="EN-US"}[类地址和环回地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_901944994}[：指定的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x249802110}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1726097563}[服务器上通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来标识接入设备，并根据收到的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是否与服务器所管理的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配，来决定是否处理来自该接入设备的认证或计费请求。因此，为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源地址必须与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器上指定的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址保持一致。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x277233846}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1321563764}[方案视图下的命令]{lang="EN-US" style="font-family:宋体"}**[nas-ip]{lang="EN-US"}**[只对本]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案有效，系统视图下的命令]{lang="EN-US" style="font-family:宋体"}**[radius nas-ip]{lang="EN-US"}**[对所有]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案有效。]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图下的设置具有更高的优先级。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[指定发送]{style="font-family:宋体"}]{#struct_0_86480_74578_778998024}[RADIUS]{lang="EN-US"}[报文使用的源地址，可以避免物理接口故障时从服务器返回的报文不可达。]{style="font-family:宋体"}[一般推荐使用]{lang="EN-US" style="font-family:宋体"}[Loopback]{lang="EN-US"}[接口地址。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果重复执行此命令，新配置的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x342270248}[源地址会覆盖原有的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[源地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917832721}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x2010637591}[配置设备发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1611215114}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] nas-ip 10.1.1.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1629920456}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_511832534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x790605287}
:::

::: {#1212291552 .myid}
[]{#_Toc404792585}[]{#struct_0_86480_74578_1637834170}

**AAA \-- RADIUS配置命令 \-- port**

------------------------------------------------------------------------

[**[port]{lang="EN-US"}**]{#struct_0_86480_74578_1637637562}[命令用来指定]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务端口。]{style="font-family:宋体"}

[**[undo port]{lang="EN-US"}**]{#struct_0_86480_74578_x1062291711}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1637703098}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_69765467}

[**[undo port]{lang="EN-US"}**]{#struct_0_86480_74578_1638030778}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1652157151}

[[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_1638096314}[服务端口为]{style="font-family:宋体"}[3799]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2069550107}

[[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_1637506487}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1637572023}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1485701713}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1637375415}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_121884213}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1637440951}[：]{style="font-family:宋体"}[DAE]{lang="EN-US"}[服务器接收]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求消息的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_834606227}

[[通常]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_1637768631}[客户端使用]{style="font-family:宋体"}[UDP 3799]{lang="EN-US"}[作为发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文的目的端口，因此不需要修改设备上的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务端口。若要修改，必须保证设备上的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务端口与]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端发送]{style="font-family:宋体"}[DAE]{lang="EN-US"}[报文的目的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口一致。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_857454990}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1637834167}[使能]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务后，指定]{style="font-family:宋体"}[DAE]{lang="EN-US"}[服务端口为]{style="font-family:宋体"}[3790]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1268793772}

[\[Sysname\] radius dynamic-author server]{lang="EN-US"}

[\[Sysname-radius-da-server\] port 3790]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1637637559}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client]{lang="EN-US"}**]{#struct_0_86480_74578_x1062881532}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_1637703095}
:::

::: {#-591335709 .myid}
[]{#_Toc404792586}[]{#struct_0_86480_74578_1889043519}[]{#_Toc268769764}[]{#_Toc205699689}[]{#_Toc162860272}[]{#_Toc147117590}[]{#_Toc147049950}[]{#_Toc146447670}[]{#_Ref106847689}[]{#_Ref106847684}[]{#_Toc69900495}

**AAA \-- RADIUS配置命令 \-- primary accounting (RADIUS scheme view)**

------------------------------------------------------------------------

[**[primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1149697322}[命令用来配置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[**[undo primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1917898257}[命令用来删除设置的主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1669879560}

[**[primary accounting ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_x2030171409}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* *\|* **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_671198239}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2094530313}

[[未配置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1503218766}[计费服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1595487995}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1649804675}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917963793}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x454973898}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x680356570}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_28978647}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x942597389}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_1423559216}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x1647162191}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，缺省为]{style="font-family:宋体"}[1813]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。此端口号必须与服务器提供计费服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_x1108000704}[：与主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1669453123}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1918029329}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_2034185572}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x956841685}

[[在同一个方案中指定的主计费服务器和从计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x305758598}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同。]{style="font-family:宋体"}

[[设备与主计费服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用]{style="font-family:宋体"}**[key]{lang="EN-US"}**[ **accounting**]{lang="EN-US"}]{#struct_0_86480_74578_x794388890}[命令设置的共享密钥。]{style="font-family:宋体"}

[[若服务器位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}]{#struct_0_86480_74578_1342013698}[私网中，为保证]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例比]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例具有更高的优先级。]{style="font-family:宋体"}

[[如果计费开始请求过程中使用本命令修改或删除了正在使用的主计费服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_x16920782}[的服务器进行通信。]{style="font-family:宋体"}

[[如果在线用户正在使用的计费服务器被删除，则设备将无法发送用户的实时计费请求和停止计费请求，且停止计费报文不会被缓存到本地，这将造成对用户计费的不准确。]{style="font-family:宋体"}]{#struct_0_86480_74578_x263237411}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_1918094865}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2025117591}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_481931882}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的主计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1813]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务，计费报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTacct&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1035310297}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] primary accounting 10.110.1.2 1813 key simple 123456TESTacct&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2118970057}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_636921392}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x777415724}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1260806225}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1917111825}
:::

::: {#-976543257 .myid}
[]{#_Toc404792587}[]{#struct_0_86480_74578_1434226793}[]{#_Toc268769765}[]{#_Toc205699690}[]{#_Toc162860273}[]{#_Toc147117591}[]{#_Toc147049951}[]{#_Toc146447671}[]{#_Ref106847719}[]{#_Ref106847707}[]{#_Toc69900496}

**AAA \-- RADIUS配置命令 \-- primary authentication (RADIUS scheme view)**

------------------------------------------------------------------------

[**[primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x2014761954}[命令用来配置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[**[undo primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_1603394596}[命令用来删除设置的主]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[认证服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_812119663}

[**[primary authentication ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_x1821285293}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **test-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1795665543}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2011281251}

[[未配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_363686219}[主认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917177361}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1655801437}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1848784230}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x934748695}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2029225879}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1009596089}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_64937294}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_1632841361}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1917636110}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号[]{#_Hlt15897255}，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535,]{lang="EN-US"}[缺省为]{style="font-family:宋体"}[1812]{lang="EN-US"}[。此端口号必须与服务器提供认证服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_1462038040}[：与主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1772704008}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"} [FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1260102257}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[test-profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_1637440952}[：]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测模版名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x754369304}[：主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x344448380}

[[在同一个方案中指定的主认证服务器和从认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_1394128430}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同。]{style="font-family:宋体"}

[[设备与主认证服务器通信时优先使用本命令设置的共享密钥，如果本命令中未设置，则使用]{style="font-family:宋体"}**[key]{lang="EN-US"}**[ **authenticaiton**]{lang="EN-US"}]{#struct_0_86480_74578_x395070539}[命令设置的共享密钥。]{style="font-family:宋体"}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1637768632}[认证服务器引用了存在的服务器探测模版后，将会触发对该服务器的探测功能。]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测功能是指，设备周期性发送探测报文探测]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器是否可达：如果服务器不可达，则置服务器状态为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，如果服务器可达，则置服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[若服务器位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}]{#struct_0_86480_74578_1917701646}[私网中，为保证]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[如果在认证过程中使用本命令修改或删除了正在使用的主认证服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_x1244229587}[的服务器进行通信。]{style="font-family:宋体"}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_804062281}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_485258216}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x2141575423}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的主认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权服务，认证报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1602521199}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] primary authentication 10.110.1.1 1812 key simple 123456TESTauth&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1782267755}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1382876080}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1917767182}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_1637834168}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1277396649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1047342453}
:::

::: {#-708706228 .myid}
[]{#_Toc404792588}[]{#struct_0_86480_74578_1637637560}[]{#_Toc335845120}

**AAA \-- RADIUS配置命令 \-- radius-server test-profile**

------------------------------------------------------------------------

[**[radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_x1062422783}[命令用来配置]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[服务器探测模版。]{style="font-family:宋体"}

[**[undo radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_1637703096}[命令用来删除指定的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测模版。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_69110107}

[**[radius-server test-profile]{lang="EN-US"}**[ *profile-name* **username** *name* \[ **interval** *interval* \]]{lang="EN-US"}]{#struct_0_86480_74578_1638030776}

[**[undo radius-server test-profile ]{lang="EN-US"}***[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_1638096312}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2069419035}

[[无]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1091376864}[服务器探测模版。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x553406683}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1091311328}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091507936}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x2052344621}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1091442400}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2117353992}

[*[profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1091114720}[：探测模版名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写]{style="font-family:宋体"}

[**[username ]{lang="EN-US"}***[name]{lang="EN-US"}*]{#struct_0_86480_74578_1961741510}[：探测报文中的用户名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[253]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[interval]{lang="EN-US"}**[ *interval*]{lang="EN-US"}]{#struct_0_86480_74578_x1091049184}[：发送探测报文的周期，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[3600]{lang="EN-US"}[，单位为分钟，缺省值为]{style="font-family:宋体"}[60]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091245792}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x4806867}[服务器探测模版用于配置探测用户名以及探测周期，并且可以被]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图下的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权服务器配置引用。只有一个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器配置中成功引用了一个已经存在的服务器探测模版，且该服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[时，设备才会启动对该]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的探测功能。]{style="font-family:宋体"}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1091180256}[服务器探测报文是一种模拟的认证请求报文，服务器探测模版中配置的探测用户名即为该探测报文中的认证用户名。设备会在配置的探测周期内选择随机时间点向引用了服务器探测模版的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送探测报文，且每次收到的探测应答消息仅能说明当前探测周期内该]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器可达。如果服务器不可达，则置服务器状态为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，如果服务器可达，则置服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[服务器探测功能启动后，周期性的探测过程会一直执行，直到相关的配置发生变化才会停止。这些配置包括：删除该]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_720434352}[服务器配置、取消对服务器探测模版的引用、删除对应的服务器探测模版、将该]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态手工置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[、删除当前]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[系统支持配置多个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1090852576}[服务器探测模版。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1090787040}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x2014847609}[方案视图下的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器配置成功引用了某探测模板后，若被引用的探测模板不存在，则暂不启动探测功能。之后，当该探测模板被成功配置时，针对该服务器的探测过程将会立即开始。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[一个]{style="font-family:宋体"}]{#struct_0_86480_74578_x1091376863}[RADIUS]{lang="EN-US"}[服务器探测模版可被多个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案引用，用于对不同的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器进行探测。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[删除一个]{style="font-family:宋体"}]{#struct_0_86480_74578_1012677258}[RADIUS]{lang="EN-US"}[服务器探测模版时，引用该探测模版的所有]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的探测功能也会被关闭。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091311327}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1091507935}[配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测模版]{style="font-family:宋体"}[abc]{lang="EN-US"}[，探测报文中携带的用户名为]{style="font-family:宋体"}[admin]{lang="EN-US"}[，探测报文的发送间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1649060094}

[\[Sysname\] radius-server test-profile abc username admin interval 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091442399}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary authentication]{lang="EN-US"}**[ (RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x906910584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary ]{lang="EN-US"}[authentication]{lang="EN-US"}**[ (RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x1091114719}
:::

::: {#1890469916 .myid}
[]{#_Toc404792589}[]{#struct_0_86480_74578_x1091049183}[]{#_Toc335845116}

**AAA \-- RADIUS配置命令 \-- radius dynamic-author server**

------------------------------------------------------------------------

[**[radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_x49794408}[命令用来使能]{style="font-family:
宋体"}[RADIUS DAE]{lang="EN-US"}[服务，并进入]{style="font-family:
宋体"}[RADIUS DAE]{lang="EN-US"}[服务器视图。]{style="font-family:
宋体"}

[**[undo radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_x1091245791}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_398477660}

[**[radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_x1091180255}

[**[undo radius dynamic-author server]{lang="EN-US"}**]{#struct_0_86480_74578_1123718879}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1090852575}

[[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_x1090787039}[服务处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x804928492}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1091376866}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_609392731}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1091311330}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1564069066}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091507938}

[[使能]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}]{#struct_0_86480_74578_x533314847}[服务后，设备将默认开启]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[3799]{lang="EN-US"}[，并能够接收指定的]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[客户端发送的]{style="font-family:宋体"}[DAE]{lang="EN-US"}[请求消息，然后根据请求消息进行用户授权信息的修改或断开用户连接请求。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091442402}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x954554578}[使能]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务，并进入]{style="font-family:宋体"}[RADIUS DAE]{lang="EN-US"}[服务器视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1091114722}

[\[Sysname\] radius dynamic-author server]{lang="EN-US"}

[\[Sysname -radius-da-server\] ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091049186}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[client]{lang="EN-US"}**]{#struct_0_86480_74578_709720479}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[port]{lang="EN-US"}**]{#struct_0_86480_74578_x1091245794}
:::

::: {#1839355718 .myid}
[]{#_Toc404792590}[]{#struct_0_86480_74578_1157992547}[]{#_Toc335845128}

**AAA \-- RADIUS配置命令 \-- radius dscp**

------------------------------------------------------------------------

[**[radius dscp]{lang="EN-US"}**]{#struct_0_86480_74578_x1091180258}[命令用来配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[协议报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级。]{style="font-family:宋体"}

[**[undo radius dscp]{lang="EN-US"}**]{#struct_0_86480_74578_1527003406}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1090852578}

[**[radius]{lang="EN-US"}**[ \[ **ipv6** \] **dscp** *dscp-value*]{lang="EN-US"}]{#struct_0_86480_74578_x1090787042}

[**[undo radius]{lang="EN-US"}**[ \[ **ipv6** \] **dscp**]{lang="EN-US"}]{#struct_0_86480_74578_x852048195}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091376865}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x2119490624}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[0]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x602852418}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1091311329}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_354281021}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1091507937}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1091442401}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x551270051}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_x1091114721}[：表示设置]{style="font-family:宋体"}[IPv6 RADIUS]{lang="EN-US"}[报文。若不指定该参数，则表示设置]{style="font-family:宋体"}[IPv4 RADIUS]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[*[dscp-value]{lang="EN-US"}*]{#struct_0_86480_74578_395657569}[：]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[。取值越大，优先级越高。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091049185}

[[DSCP]{lang="EN-US"}]{#struct_0_86480_74578_1113005006}[携带在]{style="font-family:宋体"}[IP]{lang="EN-US"}[报文中的]{style="font-family:宋体"}[ToS]{lang="EN-US"}[字段，用来体现报文自身的优先等级，决定报文传输的优先程度。通过本命令可以指定设备发送的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文携带的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级的取值。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1091245793}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1561277074}[配置]{style="font-family:宋体"}[IPv4 RADIUS]{lang="EN-US"}[报文的]{style="font-family:宋体"}[DSCP]{lang="EN-US"}[优先级为]{style="font-family:宋体"}[10]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1091180257}

[\[Sysname\] radius dscp 10]{lang="EN-US"}
:::

::: {#-1860524998 .myid}
[]{#_Toc404792591}[]{#struct_0_86480_74578_x1459070272}[]{#_Toc268769768}[]{#_Toc205699692}[]{#_Toc162860275}[]{#_Toc147117592}[]{#_Toc147049952}[]{#_Toc146447672}[]{#_Toc69900498}[]{#_Toc145062321}[]{#_Toc145062322}[]{#_Toc156377135}[]{#_Toc156377371}[]{#_Toc156635172}[]{#_Toc156636112}[]{#_Toc156377136}[]{#_Toc156377372}[]{#_Toc156635173}[]{#_Toc156636113}[]{#_Toc156377137}[]{#_Toc156377373}[]{#_Toc156635174}[]{#_Toc156636114}[]{#_Toc156377138}[]{#_Toc156377374}[]{#_Toc156635175}[]{#_Toc156636115}[]{#_Toc156377139}[]{#_Toc156377375}[]{#_Toc156635176}[]{#_Toc156636116}[]{#_Toc156377140}[]{#_Toc156377376}[]{#_Toc156635177}[]{#_Toc156636117}[]{#_Toc156377141}[]{#_Toc156377377}[]{#_Toc156635178}[]{#_Toc156636118}[]{#_Toc156377142}[]{#_Toc156377378}[]{#_Toc156635179}[]{#_Toc156636119}[]{#_Toc156377143}[]{#_Toc156377379}[]{#_Toc156635180}[]{#_Toc156636120}[]{#_Toc156377144}[]{#_Toc156377380}[]{#_Toc156635181}[]{#_Toc156636121}[]{#_Toc156377145}[]{#_Toc156377381}[]{#_Toc156635182}[]{#_Toc156636122}[]{#_Toc156377146}[]{#_Toc156377382}[]{#_Toc156635183}[]{#_Toc156636123}

**AAA \-- RADIUS配置命令 \-- radius nas-ip**

------------------------------------------------------------------------

[**[radius nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_1914050828}[命令用来指定设备发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源地址。]{style="font-family:宋体"}

[**[undo radius nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_45352231}[命令用来删除指定的源地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1768651096}

[**[radius nas-ip]{lang="EN-US"}**[ { *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_2086586413}

[**[undo radius nas-ip]{lang="PT-BR"}**]{#struct_0_86480_74578_427119689}[ ]{lang="PT-BR"}[{ *ipv4-address* \| **ipv6** *ipv6-address* }]{lang="EN-US"}[ \[ **vpn-instance** *vpn-instance-name* ]{lang="PT-BR"}[\]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917832718}

[[不指定源地址，即以发送报文的接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x2010047770}[地址作为源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x374162024}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1261955888}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1531143756}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_362473604}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1879883186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x413690174}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x832908576}[：指定的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，应该为本机的地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址、]{style="font-family:宋体"}[D]{lang="EN-US"}[类地址、]{style="font-family:宋体"}[E]{lang="EN-US"}[类地址和环回地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_1917898254}[：指定的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1669945096}[：指定私网源]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示配置的是公网源地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1176119965}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1427954950}[服务器上通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来标识接入设备，并根据收到的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是否与服务器所管理的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配，来决定是否处理来自该接入设备的认证或计费请求。指定发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源地址，可以避免物理接口故障时从服务器返回的报文不可达。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1640783954}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[系统最多允许指定]{style="font-family:宋体"}]{#struct_0_86480_74578_813223636}[16]{lang="EN-US"}[个源地址，其中，最多包括一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网源地址和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[公网源地址，其余为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网源地址。新配置的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[公网源地址会覆盖原有的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[公网源地址。而且，对于同一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，最多只能指定一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网源地址和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网源地址。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送]{style="font-family:宋体"}]{#struct_0_86480_74578_2091402670}[RADIUS]{lang="EN-US"}[报文使用的源地址必须与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器上指定的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1743363207}[方案视图下的命令]{lang="EN-US" style="font-family:宋体"}**[nas-ip]{lang="EN-US"}**[只对本]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案有效，系统视图下的命令]{lang="EN-US" style="font-family:宋体"}**[radius nas-ip]{lang="EN-US"}**[对所有]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案有效。]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图下的设置具有更高的优先级。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917963790}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x455170506}[配置设备发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文使用的源地址为]{style="font-family:宋体"}[129.10.10.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x343608826}

[\[Sysname\] radius nas-ip 129.10.10.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1583565210}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nas-ip ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x1517644711}
:::

::: {#-1735036893 .myid}
[]{#_Toc404792592}[]{#struct_0_86480_74578_1917111822}[]{#_Toc268769769}[]{#_Toc205699693}[]{#_Toc162860276}[]{#_Toc147117593}[]{#_Toc147049953}[]{#_Toc146447673}[]{#_Toc69900497}

**AAA \-- RADIUS配置命令 \-- radius scheme**

------------------------------------------------------------------------

[**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1434161257}[命令用来创建]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案，并进入]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案视图。]{style="font-family:宋体"}

[**[undo radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1914675302}[命令用来删除指定的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1162517836}

[**[radius scheme]{lang="DE"}**]{#struct_0_86480_74578_1719828034}[ *radius-scheme-name*]{lang="DE"}

[**[undo radius scheme]{lang="DE"}**]{#struct_0_86480_74578_x1636849417}[ *radius-scheme-name*]{lang="DE"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_783661738}

[[不存在任何]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_609590422}[方案。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1252848071}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1917177358}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1656260186}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1062998729}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_456699339}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1210751817}

[*[radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_641503274}[：]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x567148954}

[[一个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1456964637}[方案可以同时被多个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域引用。]{style="font-family:宋体"}

[[系统最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_86480_74578_x950694815}[个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917636111}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1461972504}[创建名为]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1463106523}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1288113997}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_109773489}
:::

::: {#1310118682 .myid}
[]{#_Toc404792593}[]{#struct_0_86480_74578_x2121197205}[]{#_Toc335845118}

**AAA \-- RADIUS配置命令 \-- radius session-control enable**

------------------------------------------------------------------------

[**[radius session-control enable]{lang="EN-US"}**]{#struct_0_86480_74578_1247985215}[命令用来使能]{style="font-family:
宋体"}[RADIUS session control]{lang="EN-US"}[功能，即打开知名]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo radius session-control enable]{lang="EN-US"}**]{#struct_0_86480_74578_338355423}[命令恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_359678404}

[**[radius session-control enable]{lang="EN-US"}**]{#struct_0_86480_74578_1918029326}

[**[undo radius session-control enable]{lang="EN-US"}**]{#struct_0_86480_74578_2033464676}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x428394831}

[[RADIUS session control]{lang="EN-US"}]{#struct_0_86480_74578_x527356274}[功能处于关闭状态，即知名]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1278273575}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_806418977}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x78627524}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x997291190}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1918094862}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2025052055}

[[无]{style="font-family:宋体"}]{#struct_0_86480_74578_1644236954}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_615680122}

[[H3C]{lang="EN-US"}]{#struct_0_86480_74578_x1562274821}[的]{style="font-family:宋体"}[IMC RADIUS]{lang="EN-US"}[服务器使用]{style="font-family:宋体"}[session control]{lang="EN-US"}[报文向设备发送授权信息的动态修改请求以及断开连接请求。使能]{style="font-family:宋体"}[RADIUS session control]{lang="EN-US"}[功能后，设备会打开知名]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[来监听并接收]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送的]{style="font-family:宋体"}[session control]{lang="EN-US"}[报文。]{style="font-family:宋体"}

[[需要注意的是，该功能仅能和]{style="font-family:宋体"}[H3C IMC]{lang="EN-US"}]{#struct_0_86480_74578_x838362103}[的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器配合使用。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1568721768}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x856897537}[使能]{style="font-family:宋体"}[RADIUS session control]{lang="EN-US"}[功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1597717807}

[\[Sysname\] radius session-control enable]{lang="EN-US"}
:::

::: {#2138529384 .myid}
[]{#_Toc404792594}[]{#struct_0_86480_74578_159787697}[]{#_Toc268769771}[]{#_Toc205699695}[]{#_Toc162860278}[]{#_Toc147117596}[]{#_Toc147049956}[]{#_Toc146447676}[]{#_Toc69900499}

**AAA \-- RADIUS配置命令 \-- reset radius statistics**

------------------------------------------------------------------------

[**[reset radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_471023841}[命令用来清除]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[协议的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917701647}

[**[reset radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_x1244164051}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_692529336}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1563855892}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x872460673}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_281608836}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_860003714}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_965057351}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1754916035}[清除]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[协议的统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset radius statistics]{lang="EN-US"}]{#struct_0_86480_74578_1917767183}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1277331113}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius statistics]{lang="EN-US"}**]{#struct_0_86480_74578_1130431208}
:::

::: {#1554758993 .myid}
[]{#_Toc404792595}[]{#struct_0_86480_74578_1447600124}[]{#_Toc268769773}[]{#_Toc205699697}[]{#_Toc162860280}[]{#_Toc147117598}[]{#_Toc147049958}[]{#_Toc146447678}[]{#_Toc69900501}

**AAA \-- RADIUS配置命令 \-- retry**

------------------------------------------------------------------------

[**[retry]{lang="EN-US"}**]{#struct_0_86480_74578_x2147138670}[命令用来设置发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的最大尝试次数，即如果某]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器在指定的时间内未响应或未及时响应设备发送的]{style="font-family:宋体"}[RAIUDS]{lang="EN-US"}[报文，设备尝试向该服务器发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的最大次数。]{style="font-family:宋体"}

[**[undo retry]{lang="EN-US"}**]{#struct_0_86480_74578_308393502}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x480201518}

[**[retry]{lang="EN-US"}**[ *retry-times*]{lang="EN-US"}]{#struct_0_86480_74578_1731705058}

[**[undo retry]{lang="EN-US"}**]{#struct_0_86480_74578_x136786515}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917832719}

[[发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x2010113306}[报文的最大尝试次数为]{style="font-family:宋体"}[3]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1127149367}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x89774831}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1982168719}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1667414838}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x674814538}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1151325553}

[*[retry-times]{lang="EN-US"}*]{#struct_0_86480_74578_1204739626}[：发送]{style="font-family:宋体"}[RAIUDS]{lang="EN-US"}[报文的最大尝试次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917898255}

[[由于]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1670010632}[协议采用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[报文来承载数据，因此其通信过程是不可靠的。如果设备在应答超时定时器规定的时长内（由]{style="font-family:宋体"}**[timer response-timeout]{lang="EN-US"}**[命令配置）没有收到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的响应，则设备有必要向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器重传]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[请求报文。如果累计的传送次数已达到最大传送次数而]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器仍旧没有响应，则设备将认为本次请求失败。]{style="font-family:宋体"}

[[发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_586831451}[报文的最大尝试次数与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器应答超时时间的乘积不能超过]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_114365784}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1724054665}[设置在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[下，发送]{style="font-family:宋体"}[RAIUDS]{lang="EN-US"}[报文的最大尝试次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1408262521}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] retry 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_985938676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_980780952}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_1917963791}
:::

::: {#670032396 .myid}
[]{#_Toc404792596}[]{#struct_0_86480_74578_x455104970}[]{#_Toc268769774}[]{#_Toc205699698}[]{#_Toc162860281}[]{#_Toc147117599}[]{#_Toc147049959}[]{#_Toc146447679}[]{#_Toc69900502}

**AAA \-- RADIUS配置命令 \-- retry realtime-accounting**

------------------------------------------------------------------------

[**[retry realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x670687339}[命令用来设置允许发起实时计费请求的最大尝试次数。]{style="font-family:
宋体"}

[**[undo]{lang="EN-US"}**[ **retry realtime-accounting**]{lang="EN-US"}]{#struct_0_86480_74578_x2120005178}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_772164385}

[**[retry realtime-accounting]{lang="EN-US"}**[ *retry-times*]{lang="EN-US"}]{#struct_0_86480_74578_1668773633}

[**[undo retry realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1958366920}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1117972590}

[[设备最多允许]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_86480_74578_1918029327}[次实时计费请求无响应，之后将切断用户连接。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_2033530212}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1139148988}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1990638028}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1045908591}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1568331298}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_201434034}

[*[retry-times]{lang="EN-US"}*]{#struct_0_86480_74578_x1056376835}[：允许发起实时计费请求的最大尝试次数，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x133517318}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1918094863}[服务器通常通过连接超时定时器来判断用户是否在线。如果]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器在连接超时时间之内一直收不到设备传来的实时计费报文，它会认为线路或设备故障并停止对用户记帐。为了配合]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的这种特性，有必要在不可预见的故障条件下，尽量保持设备端与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器同步切断用户连接。设备提供对实时计费请求连续无响应次数限制的设置，保证设备尽可能得在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的连接超时时长内向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器尝试发出实时计费请求。如果设备没有收到响应的次数超过了设定的限度，才会切断用户连接。]{style="font-family:宋体"}

[[假设]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_2024986519}[服务器的应答超时时长（]{style="font-family:宋体"}**[timer response-timeout]{lang="EN-US"}**[命令设置）为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒，发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文的最大尝试次数（]{style="font-family:宋体"}**[retry]{lang="EN-US"}**[命令设置）为]{style="font-family:宋体"}[3]{lang="EN-US"}[，设备的实时计费间隔（]{style="font-family:宋体"}**[timer realtime-accounting]{lang="EN-US"}**[命令设置）为]{style="font-family:宋体"}[12]{lang="EN-US"}[分钟，设备允许实时计费无响应的最大次数为]{style="font-family:宋体"}[5]{lang="EN-US"}[次（]{style="font-family:宋体"}**[retry realtime-accounting]{lang="EN-US"}**[命令设置），则其含义为：设备每隔]{style="font-family:宋体"}[12]{lang="EN-US"}[分钟发起一次计费请求，如果]{style="font-family:宋体"}[3]{lang="EN-US"}[秒钟得不到回应就重新发起一次请求，如果]{style="font-family:宋体"}[3]{lang="EN-US"}[次发送都没有得到回应就认为该次实时计费失败，然后每隔]{style="font-family:宋体"}[12]{lang="EN-US"}[分钟再发送一次，]{style="font-family:宋体"}[5]{lang="EN-US"}[次均失败以后，设备将切断用户连接。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1631468767}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1519732372}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[最多允许]{style="font-family:宋体"}[10]{lang="EN-US"}[次实时计费请求无响应。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_180546199}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] retry realtime-accounting 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_120625160}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[retry]{lang="EN-US"}**]{#struct_0_86480_74578_x313550649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1841812098}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_1917111823}
:::

::: {#-688792923 .myid}
[]{#_Toc404792597}[]{#struct_0_86480_74578_1434095721}[]{#_Toc268769776}[]{#_Toc205699700}[]{#_Toc162860283}[]{#_Toc147117601}[]{#_Toc147049961}[]{#_Toc146447681}[]{#_Toc69900504}

**AAA \-- RADIUS配置命令 \-- secondary accounting (RADIUS scheme view)**

------------------------------------------------------------------------

[**[secondary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1626485226}[命令用来配置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[**[undo secondary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_370439251}[命令用来删除指定的从]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[计费服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1304637903}

[**[secondary accounting ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_32997753}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo secondary accounting ]{lang="EN-US"}**[\[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x1563253118}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \] \* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_935451782}

[[未配置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1917177359}[计费服务器]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1656325722}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1085381037}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_2054127739}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1523181551}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_860137566}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_199525596}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_639022786}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_x142692477}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1917636108}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，缺省为]{style="font-family:宋体"}[1813]{lang="EN-US"}[，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。此端口号必须与服务器提供计费服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_1462562329}[：与从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1817559971}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1324285897}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1787636152}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1192815461}

[[可通过多次执行本命令，配置多个从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x2098612868}[计费服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器并与之交互。每个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1583182514}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个方案中指定的主计费服务器和从计费服务器的]{style="font-family:宋体"}]{#struct_0_86480_74578_x195326437}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同，并且各从计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数也不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备与从计费服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用命令]{style="font-family:宋体"}]{#struct_0_86480_74578_1917701644}**[key]{lang="EN-US"}**[ **accounting**]{lang="EN-US"}[命令设置的共享密钥。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若服务器位于]{style="font-family:宋体"}]{#struct_0_86480_74578_x1244098515}[MPLS VPN]{lang="EN-US"}[私网中，为保证]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在发送计费开始请求过程中使用本命令删除了正在使用的从服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为]{style="font-family:宋体"}]{#struct_0_86480_74578_1371000710}**[active]{lang="EN-US"}**[的服务器进行通信。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在线用户正在使用的计费服务器被删除，则设备将无法发送用户的实时计费请求和停止计费请求，且停止计费报文不会被缓存到本地。]{style="font-family:宋体"}]{#struct_0_86480_74578_1917007110}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1273202241}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1169724960}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_2103846365}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的从计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1813]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1270480995}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] secondary accounting 10.110.1.1 1813]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1917767180}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius2]{lang="EN-US"}[的从计费服务器：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分别为]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，均使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1813]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1277527721}

[\[Sysname\] radius scheme radius2]{lang="EN-US"}

[\[Sysname-radius-radius2\] secondary accounting 10.110.1.1 1813]{lang="EN-US"}

[\[Sysname-radius-radius2\] secondary accounting 10.110.1.2 1813]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1537910423}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_797316085}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x281535649}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1265923114}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x315554776}
:::

::: {#-2011523264 .myid}
[]{#_Toc404792598}[]{#struct_0_86480_74578_1917832716}[]{#_Toc268769777}[]{#_Toc205699701}[]{#_Toc162860284}[]{#_Toc147117602}[]{#_Toc147049962}[]{#_Toc146447682}[]{#_Toc69900505}

**AAA \-- RADIUS配置命令 \-- secondary authentication (RADIUS scheme view)**

------------------------------------------------------------------------

[**[secondary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x2010440986}[命令用来配置从]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[**[undo secondary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1590855372}[命令用来删除指定的从]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[认证服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1572951098}

[**[secondary authentication ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_1545854020}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **test-profile** *profile-name* \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo secondary authentication ]{lang="EN-US"}**[\[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1685876835}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \] \* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1750638686}

[[未配置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1131199006}[认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1345501895}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1917898252}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1670076168}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1688097152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2111480657}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_933296421}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x1550622303}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_15572215}*[ ]{lang="EN-US"}[ipv6-address]{lang="NO-BOK"}*[：]{style="font-family:宋体"}[从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x173367109}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[1812]{lang="EN-US"}[。此端口号必须与服务器提供认证服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="NO-BOK"}**]{#struct_0_86480_74578_x830387931}[ { **cipher** \| **simple** } *string*]{lang="NO-BOK"}[：]{style="font-family:宋体"}[与从]{style="font-family:宋体"}[RADIUS]{lang="NO-BOK"}[认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1917963788}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[117]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x454646219}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[test-profile]{lang="EN-US"}***[ profile-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1091049187}[：]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测模版名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_876230440}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器位于公网中。该参数支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x204849119}

[[可通过多次执行本命令，配置多个从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_967969624}[认证服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器并与之交互。每个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x2019162876}[认证服务器引用了存在的服务器探测模版后，将会触发对该服务器的探测功能。]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器探测功能是指，设备周期性发送探测报文探测]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器是否可达：如果服务器不可达，则置服务器状态为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，如果服务器可达，则置服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1226247690}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个方案中指定的主认证服务器和从认证服务器的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1757692034}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同，并且各从认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数也不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[设备与从认证服务器通信时优先使用本命令设置的共享密钥，如果此处未设置，则使用命令]{lang="EN-US" style="font-family:宋体"}**[key]{lang="EN-US"}**[ **authentication**]{lang="EN-US"}]{#struct_0_86480_74578_x1927523185}[命令设置的共享密钥。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若服务器位于]{style="font-family:宋体"}]{#struct_0_86480_74578_1918029324}[MPLS VPN]{lang="EN-US"}[私网中，为保证]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果在认证过程中使用本命令删除了正在使用的从服务器，则设备在与当前服务器通信超时后，将会重新按照优先级顺序开始依次查找状态为]{style="font-family:宋体"}]{#struct_0_86480_74578_2033333604}**[active]{lang="EN-US"}**[的服务器进行通信。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_338132114}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1471945946}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x540519294}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的从认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1090792104}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] secondary authentication 10.110.1.2 1812]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_174026518}[设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius2]{lang="EN-US"}[的从认证服务器：]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址分别为]{style="font-family:宋体"}[10.110.1.1]{lang="EN-US"}[，]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[，均使用]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口]{style="font-family:宋体"}[1812]{lang="EN-US"}[提供]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权服务。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1918094860}

[\[Sysname\] radius scheme radius2]{lang="EN-US"}

[\[Sysname-radius-radius2\] secondary authentication 10.110.1.1 1812]{lang="EN-US"}

[\[Sysname-radius-radius2\] secondary authentication 10.110.1.2 1812]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2024920983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_512828942}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x1631110001}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1075876472}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_x1091180259}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(RADIUS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x1023788294}
:::

::: {#-1320117794 .myid}
[]{#_Toc404792599}[]{#struct_0_86480_74578_1766788000}[]{#_Toc268769778}[]{#_Toc205699702}[]{#_Toc162860285}

**AAA \-- RADIUS配置命令 \-- security-policy-server**

------------------------------------------------------------------------

[**[security-policy-server]{lang="EN-US"}**]{#struct_0_86480_74578_x1566003566}[命令用来指定安全策略服务器。]{style="font-family:宋体"}

[**[undo security-policy-server]{lang="EN-US"}**]{#struct_0_86480_74578_x1817894224}[命令用来删除指定的安全策略服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917111820}

[**[security-policy-server ]{lang="EN-US"}**[{ ]{lang="EN-US"}*[ipv4-address \| ]{lang="EN-US"}***[ipv6]{lang="EN-US"}***[ ipv6-address ]{lang="EN-US"}*[}]{lang="EN-US"}*[ ]{lang="EN-US"}*[\[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_1434030185}

[**[undo security-policy-server ]{lang="EN-US"}**[{ { *ipv4-address \| * **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \] \| **all** }]{lang="EN-US"}]{#struct_0_86480_74578_x1236593389}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1426742738}

[[未指定安全策略服务器。]{style="font-family:宋体"}]{#struct_0_86480_74578_x945536722}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_116282763}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_206734082}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1712473770}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1917177356}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1656129114}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x645759717}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_1681533666}[：安全策略服务器]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_x743964111}[：安全策略服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}**[ *vpn-instance-name*]{lang="EN-US"}]{#struct_0_86480_74578_x1084801211}[：安全策略服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[的实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果不指定本参数，则表示安全策略服务器属于公网。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_86480_74578_36252154}[：所有安全策略服务器。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1244382734}

[[一个]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_823876294}[方案中最多可以指定]{style="font-family:宋体"}[8]{lang="EN-US"}[个安全策略服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917636109}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1462496793}[指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的安全策略服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.110.1.2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x279507215}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] security-policy-server 10.110.1.2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1198700184}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_764007749}
:::

::: {#-791671905 .myid}
[]{#_Toc69900510}[]{#_Toc205699704}[]{#_Toc162860287}[]{#_Toc147117604}[]{#_Toc147049964}[]{#_Toc146447684}[]{#_Toc69900507}[]{#_Toc268769780}[]{#_Toc404792600}[]{#struct_0_86480_74578_1244455761}[]{#_Toc343519521}[]{#_Toc336438671}

**AAA \-- RADIUS配置命令 \-- snmp-agent trap enable radius**

------------------------------------------------------------------------

[**[snmp-agent trap enable radius]{lang="EN-US"}**]{#struct_0_86480_74578_x1898584705}[命令用来开启]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable radius]{lang="EN-US"}**]{#struct_0_86480_74578_x2016176419}[命令用来关闭指定的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917701645}

[**[snmp-agent trap enable radius ]{lang="EN-US"}**[\[ **accounting-server-down** \| **accounting-server-up** \| **authentication-error-threshold** \| **authentication-server-down** \|  **authentication-server-up** \] \*]{lang="EN-US"}]{#struct_0_86480_74578_x1244032979}

[**[undo snmp-agent trap enable radius ]{lang="EN-US"}**[\[ **accounting-server-down** \| **accounting-server-up** \| **authentication-error-threshold** \| **authentication-server-down \| authentication-server-up** \] \*]{lang="EN-US"}]{#struct_0_86480_74578_157858756}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1164215448}

[[所有类型的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1556275050}[告警功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x250945968}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_92777441}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1078786205}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_106950728}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1917767181}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1277462185}

[**[accounting-server-down]{lang="EN-US"}**]{#struct_0_86480_74578_x885738431}[：表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器可达状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[时发送告警信息。]{style="font-family:宋体"}

[**[accounting-server-up]{lang="EN-US"}**]{#struct_0_86480_74578_x60645320}[：表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器可达状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}[时发送告警信息。]{style="font-family:宋体"}

[**[authentication-error-threshold]{lang="EN-US"}**]{#struct_0_86480_74578_1785756870}[：表示认证失败次数超过阈值时发送告警信息。该阈值为认证失败次数占认证请求总数的百分比数值，目前仅能通过]{style="font-family:
宋体"}[MIB]{lang="EN-US"}[方式配置，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[30]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[authentication-server-down]{lang="EN-US"}**]{#struct_0_86480_74578_x1984077761}[：表示]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[认证服务器可达状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[时发送告警信息。]{style="font-family:宋体"}

[**[authentication-server-up]{lang="EN-US"}**]{#struct_0_86480_74578_611750523}[：表示]{style="font-family:
宋体"}[RADIUS]{lang="EN-US"}[认证服务器可达状态变为]{style="font-family:宋体"}[up]{lang="EN-US"}[时发送告警信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1347306665}

[[不指定可选参数时，表示开启]{style="font-family:宋体"}[/]{lang="EN-US"}]{#struct_0_86480_74578_x215381931}[关闭所有类型的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[告警功能。]{style="font-family:宋体"}

[[开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1917832717}[服务器可达状态改变时的告警功能后，告警信息的发送包括以下两种情况：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_86480_74578_x2010506522}[NAS]{lang="EN-US"}[向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送计费或认证请求没有收到响应时，会重传请求，当重传次数达到最大传送次数时仍然没有收到响应时，]{style="font-family:宋体"}[NAS]{lang="EN-US"}[认为该服务器不可达，并发送表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器不可达的告警信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_86480_74578_1208256224}**[timer quiet]{lang="EN-US"}**[定时器设定的时间到达后，]{style="font-family:宋体"}[NAS]{lang="EN-US"}[将服务器的状态置为激活状态并发送表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器可达的告警信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[当]{style="font-family:宋体"}]{#struct_0_86480_74578_1482755424}[NAS]{lang="EN-US"}[发现认证失败次数与认证请求总数的百分比超过阈值时，会发送表示认证失败次数超过阈值的告警信息。]{style="font-family:宋体"}

[[开启认证失败次数超过阈值时的告警功能后，当]{style="font-family:宋体"}[NAS]{lang="EN-US"}]{#struct_0_86480_74578_1992277530}[发现认证失败次数与认证请求总数的百分比超过阈值时，会发送表示认证失败次数超过阈值的告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x421081721}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x345017071}[开启]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器可达状态变为]{style="font-family:宋体"}[down]{lang="EN-US"}[时的告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x908998304}

[\[Sysname\] snmp-agent trap enable radius accounting-server-down]{lang="EN-US"}
:::

::: {#1131445377 .myid}
[]{#_Toc404792601}[]{#struct_0_86480_74578_x821193057}

**AAA \-- RADIUS配置命令 \-- state primary**

------------------------------------------------------------------------

[**[state primary]{lang="EN-US"}**]{#struct_0_86480_74578_1917898253}[命令用来设置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1670141704}

[**[state]{lang="EN-US"}**[ **primary** { **accounting** \| **authentication** } { **active** \| **block** }]{lang="EN-US"}]{#struct_0_86480_74578_x1416303903}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_860827875}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1987633807}[方案中配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1606286699}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1297464158}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_445524624}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1872603982}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1917963789}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x454580683}

[**[accounting]{lang="EN-US"}**]{#struct_0_86480_74578_802484850}[：设置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的状态。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1139412151}[：设置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的状态。]{style="font-family:宋体"}

[**[active]{lang="EN-US"}**]{#struct_0_86480_74578_570380734}[：设置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[，即处于正常工作状态。]{style="font-family:宋体"}

[**[block]{lang="EN-US"}**]{#struct_0_86480_74578_1035890506}[：设置主]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，即处于通信中断状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_202314771}

[[每次用户发起认证或计费，如果主服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_x178015646}[，则设备都会首先尝试与主服务器进行通信，如果主服务器不可达，则将主服务器的状态置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，同时启动主服务器的]{style="font-family:宋体"}**[timer quiet]{lang="EN-US"}**[定时器，然后设备会严格按照从服务器的配置先后顺序依次查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器。在]{style="font-family:宋体"}**[timer quiet]{lang="EN-US"}**[定时器设定的时间到达之后，主服务器状态将由]{style="font-family:宋体"}**[block]{lang="EN-US"}**[恢复为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。若该定时器超时之前，通过本命令将主服务器的状态手工设置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，则定时器超时之后主服务器状态不会自动恢复为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[，除非通过本命令手工将其设置为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[如果主服务器与所有从服务器状态都是]{style="font-family:宋体"}**[block]{lang="EN-US"}**]{#struct_0_86480_74578_1918029325}[，则认证或计费失败。]{style="font-family:宋体"}

[[认证服务器的状态会影响设备对该服务器可达性探测功能的开启。当指定的服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_474969221}[，且该服务器通过]{style="font-family:宋体"}**[radius-server test-profile]{lang="EN-US"}**[命令成功引用了一个已存在的服务器探测模版时，则设备会开启对该服务器的可达性探测功能。当手工将该服务器状态置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[时，会关闭对该服务器的可达性探测功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2033399140}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1092302896}[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的主认证服务器的状态设置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_888500115}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] state primary authentication block]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x77789797}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **radius scheme**]{lang="EN-US"}]{#struct_0_86480_74578_823085576}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_475034757}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state]{lang="EN-US"}**[ **secondary**]{lang="EN-US"}]{#struct_0_86480_74578_755951783}
:::

::: {#-1988884604 .myid}
[]{#_Toc404792602}[]{#struct_0_86480_74578_1485757127}[]{#_Toc268769781}

**AAA \-- RADIUS配置命令 \-- state secondary**

------------------------------------------------------------------------

[**[state secondary]{lang="EN-US"}**]{#struct_0_86480_74578_1918094861}[命令用来设置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2024855447}

[**[state]{lang="EN-US"}**[ **secondary** { **accounting** \| **authentication** } \[ { *ip*]{lang="EN-US"}]{#struct_0_86480_74578_865519754}*[v4]{lang="PT-BR"}[-address]{lang="EN-US"}*[ \| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \] \* \] { **active** \| **block** }]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1865617023}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1943501883}[方案中配置了]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址的各从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x18829086}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_412173378}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_916159755}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x2021809781}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1917111821}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1433964649}

[**[accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x697024116}[：设置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的状态。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_86480_74578_167770029}[：设置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的状态。]{style="font-family:宋体"}

[*[ip]{lang="EN-US"}*]{#struct_0_86480_74578_685192364}*[v4]{lang="PT-BR"}[-address]{lang="EN-US"}*[：指定从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_x1131622951}*[ ]{lang="EN-US"}[ipv6-address]{lang="NO-BOK"}*[：指定]{style="font-family:宋体"}[从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1493084774}[：指定从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费服务器的缺省]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[1813]{lang="EN-US"}[，从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证服务器的缺省]{style="font-family:宋体"}[UDP]{lang="EN-US"}[端口号为]{style="font-family:宋体"}[1812]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_129510174}[：从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[**[active]{lang="EN-US"}**]{#struct_0_86480_74578_565896183}[：设置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[，即处于正常工作状态。]{style="font-family:宋体"}

[**[block]{lang="EN-US"}**]{#struct_0_86480_74578_x22634901}[：设置从]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的状态为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，即处于通信中断状态。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1917177357}

[[如果不指定从服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x1656194650}[地址，那么本命令将会修改所有已配置的从认证服务器或从计费服务器的状态。]{style="font-family:宋体"}

[[如果设备查找到的状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_x235131273}[的从服务器不可达，则设备会将该从服务器的状态置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，同时启动该服务器的]{style="font-family:宋体"}**[timer quiet]{lang="EN-US"}**[定时器，并继续查找下一个状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器。在]{style="font-family:宋体"}**[timer quiet]{lang="EN-US"}**[定时器设定的时间到达之后，从服务器状态将由]{style="font-family:宋体"}**[block]{lang="EN-US"}**[恢复为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。若该定时器超时之前，通过本命令将从服务器的状态手工设置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[，则定时器超时之后从服务器状态不会自动恢复为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[，除非通过本命令手工将其设置为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[。如果所有已配置的从服务器都不可达，则本次认证或计费失败。]{style="font-family:宋体"}

[[认证服务器的状态会影响设备对该服务器可达性探测功能的开启。当指定的服务器状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_475231365}[，且该服务器通过]{style="font-family:宋体"}**[radius-server test-profile]{lang="EN-US"}**[命令成功引用了一个已存在的服务器探测模版时，则设备会开启对该服务器的可达性探测功能。当手工将该服务器状态置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[时，会关闭对该服务器的可达性探测功能。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x691049104}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1746334771}[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的从认证服务器的状态设置为]{style="font-family:宋体"}**[block]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1750568371}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] state secondary authentication block]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1849215298}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display]{lang="EN-US"}**[ **radius scheme**]{lang="EN-US"}]{#struct_0_86480_74578_x1931680194}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius-server test-profile]{lang="EN-US"}**]{#struct_0_86480_74578_475296901}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[state]{lang="EN-US"}**[ **primary**]{lang="EN-US"}]{#struct_0_86480_74578_x811247243}
:::

::: {#126985712 .myid}
[]{#_Toc404792603}[]{#struct_0_86480_74578_847464082}[]{#_Toc268769783}[]{#_Toc205699706}[]{#_Toc162860289}[]{#_Toc147117606}[]{#_Toc147049966}[]{#_Toc146447686}

**AAA \-- RADIUS配置命令 \-- timer quiet (RADIUS scheme view)**

------------------------------------------------------------------------

[**[timer quiet]{lang="FR"}**]{#struct_0_86480_74578_x1362211248}[命令用来设置服务器恢复激活状态的时间。]{style="font-family:宋体"}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_86480_74578_652583880}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1177568198}

[**[timer quiet ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_1547601675}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_86480_74578_1563670569}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1891128195}

[[服务器恢复激活状态的时间为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_86480_74578_1893184431}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811181707}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_900423039}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1941127611}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1177879375}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1490719153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2016002338}

[*[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_x122993750}[：恢复激活状态的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_759586699}

[[建议根据配置的从服务器数量合理设置服务器恢复激活状态的时间。如果服务器恢复激活状态时间设置的过短，就会出现设备反复尝试与状态]{style="font-family:宋体"}**[active]{lang="EN-US"}**]{#struct_0_86480_74578_1441671517}[但实际不可达的服务器通信而导致的认证或计费频繁失败的问题。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811116171}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_868531019}[设置服务器恢复激活状态的时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_560501092}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] timer quiet 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_771887847}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1095209345}
:::

::: {#-1270887104 .myid}
[]{#_Toc404792604}[]{#struct_0_86480_74578_x408928384}[]{#_Toc268769784}[]{#_Toc205699707}[]{#_Toc162860290}[]{#_Toc147117607}[]{#_Toc147049967}[]{#_Toc146447687}

**AAA \-- RADIUS配置命令 \-- timer realtime-accounting (RADIUS scheme view)**

------------------------------------------------------------------------

[**[timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1416522073}[命令用来设置实时计费的时间间隔。]{style="font-family:
宋体"}

[**[undo timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x811050635}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1653658042}

[**[timer realtime-accounting]{lang="EN-US"}**[ *interval* \[ **second** \]]{lang="EN-US"}]{#struct_0_86480_74578_1180158370}

[**[undo timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x910896514}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x494420906}

[[实时计费的时间间隔为]{style="font-family:宋体"}[12]{lang="EN-US"}]{#struct_0_86480_74578_72689189}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1180918150}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_598787342}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_384888941}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x810985099}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_867381468}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1052892677}

[*[interval]{lang="EN-US"}*]{#struct_0_86480_74578_x1978838820}[：实时计费的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[71582]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[second]{lang="EN-US"}**]{#struct_0_86480_74578_1391030938}[：表示实时计费的时间间隔以秒为单位，缺省以分钟为单位。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1873322932}

[[为了对用户实施实时计费，有必要设置实时计费的时间间隔。不同的取值的处理有所不同：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1023776066}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若实时计费间隔不为]{style="font-family:宋体"}]{#struct_0_86480_74578_1742313605}[0]{lang="EN-US"}[，则每隔设定的时间，设备会向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送一次在线用户的计费信息。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若实时计费间隔设置为]{style="font-family:宋体"}]{#struct_0_86480_74578_x302723235}[0]{lang="EN-US"}[，且服务器上配置了实时计费间隔，则设备按照服务器上配置的实时计费间隔向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送在线用户的计费信息；如果服务器上没有配置该值，则设备不向]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器发送在线用户的计费信息。]{style="font-family:宋体"}

[[实时计费间隔的取值与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_1313701101}[服务器的性能和用户的数目有一定关系。取值小，会增加网络中的数据流量，对设备和]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的性能要求就高；取值大，会影响计费的准确性。因此要结合网络的实际情况合理设置计费间隔。一般情况下，建议当用户量比较大（大于等于]{style="font-family:宋体"}[1000]{lang="EN-US"}[）时，尽量把该间隔的值设置得大一些。以下是实时计费间隔与用户量之间的推荐比例关系。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_x810919563}[]{#_Toc138066611}[]{#_Toc95386913}[]{#_Toc85621927}[[表1-6 ]{lang="EN-US"}[实时计费间隔与用户量之间的推荐比例关系]{style="font-family:黑体"}]{#_Toc81452875}

[]{#table_struct_0_789376290}[[用户数]{style="font-family:黑体"}]{#struct_0_86480_74578_461833017}
:::

[[实时计费间隔（分钟）]{style="font-family:黑体"}]{#struct_0_86480_74578_x221253635}

[[1]{lang="EN-US"}]{#struct_0_86480_74578_x983015804}[～]{style="font-family:宋体"}[99]{lang="EN-US"}

[[3]{lang="EN-US"}]{#struct_0_86480_74578_x1716286707}

[[100]{lang="EN-US"}]{#struct_0_86480_74578_589635360}[～]{style="font-family:宋体"}[499]{lang="EN-US"}

[[6]{lang="EN-US"}]{#struct_0_86480_74578_x810854027}

[[500]{lang="EN-US"}]{#struct_0_86480_74578_x717249137}[～]{style="font-family:宋体"}[999]{lang="EN-US"}

[[12]{lang="EN-US"}]{#struct_0_86480_74578_1283326518}

[[大于等于]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_86480_74578_x1784520500}

[[大于等于]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_86480_74578_519627593}

**[ ]{lang="EN-US"}**

[[【举例】]{style="font-family:
黑体"}]{#struct_0_86480_74578_7710137}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1815713474}[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的实时计费的时间间隔设置为]{style="font-family:宋体"}[51]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x810788491}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] timer realtime-accounting 51]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_862746529}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[retry realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_362147626}

::: {#922707397 .myid}
[]{#_Toc404792605}[]{#struct_0_86480_74578_x1240448339}[]{#_Toc268769785}[]{#_Toc205699708}[]{#_Toc162860291}[]{#_Toc147117608}[]{#_Toc147049968}[]{#_Toc146447688}

**AAA \-- RADIUS配置命令 \-- timer response-timeout (RADIUS scheme view)**

------------------------------------------------------------------------

[**[timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_x1359758153}[命令用来设置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器响应超时时间。]{style="font-family:宋体"}

[**[undo timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_x2079225969}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1290789607}

[**[timer response-timeout]{lang="EN-US"}***[ ]{lang="EN-US"}[seconds]{lang="EN-US"}*]{#struct_0_86480_74578_x1707623426}

[**[undo timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_x811771531}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_496262696}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x828769489}[服务器响应超时时间为]{style="font-family:宋体"}[3]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x916907274}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_664029080}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1209017870}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1673690688}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_904778416}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_87527191}

[*[seconds]{lang="EN-US"}*]{#struct_0_86480_74578_x811705995}[：]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器响应超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[10]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_2061840538}

[[如果在]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_575096390}[请求报文传送出去一段时间后，设备还没有得到]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的响应，则有必要重传]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[请求报文，以保证用户尽可能地获得]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务，这段时间被称为]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器响应超时时间，本命令用于调整这个时间。]{style="font-family:宋体"}

[[需要注意的是，发送]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_752334132}[报文的最大尝试次数与]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器响应超时时间的乘积不能超过]{style="font-family:宋体"}[300]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x257847659}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1439055157}[将]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[的服务器响应超时时间设置为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_627147821}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] timer response-timeout 5]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_573600295}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1684476599}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[retry]{lang="EN-US"}**]{#struct_0_86480_74578_x811247242}
:::

::: {#-694254284 .myid}
[]{#_Toc404792606}[]{#struct_0_86480_74578_847529618}[]{#_Toc268769786}[]{#_Toc205699709}[]{#_Toc162860292}[]{#_Toc147117609}[]{#_Toc147049969}[]{#_Toc146447689}[]{#_Toc69900513}

**AAA \-- RADIUS配置命令 \-- user-name-format (RADIUS scheme view)**

------------------------------------------------------------------------

[**[user-name-format]{lang="DE"}**]{#struct_0_86480_74578_2077100668}[命令用来设置发送给]{style="font-family:宋体"}[RADIUS]{lang="DE"}[服务器的用户名格式。]{style="font-family:宋体"}

[**[undo user-name-format]{lang="DE"}**]{#struct_0_86480_74578_351348767}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_110850500}

[**[user-name-format]{lang="EN-US"}**[ { **keep-original** \| **with-domain** \| **without-domain** }]{lang="EN-US"}]{#struct_0_86480_74578_1402563150}

[**[undo user-name-format]{lang="EN-US"}**]{#struct_0_86480_74578_x949047639}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811181706}

[[设备发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_900488575}[服务器的用户名携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x844789372}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_684534499}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1199221943}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1178208905}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1445516621}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1875609487}

[**[keep-original]{lang="EN-US"}**]{#struct_0_86480_74578_x593814694}[：发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名与用户的输入保持一致。]{style="font-family:宋体"}

[**[with-domain]{lang="EN-US"}**]{#struct_0_86480_74578_x811116170}[：发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[**[without-domain]{lang="EN-US"}**]{#struct_0_86480_74578_868465483}[：发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名不带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1374919871}

[[接入用户通常以"]{style="font-family:宋体"}*[userid@isp-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1285571097}["的格式命名，"]{style="font-family:宋体"}*[@]{lang="EN-US"}*["后面的部分为]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，设备就是通过该域名来决定将用户归于哪个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的。但是，有些较早期的]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器不能接受携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名的用户名，在这种情况下，有必要将用户名中携带的域名去除后再传送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器。因此，设备提供此命令以指定发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名是否携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x22444824}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果指定某个]{style="font-family:宋体"}]{#struct_0_86480_74578_x472865228}[RADIUS]{lang="EN-US"}[方案不允许用户名中携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，那么请不要在两个或两个以上的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中同时设置使用该]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。否则，会出现虽然实际用户不同（在不同的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中），但]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器认为用户相同（因为传送到它的用户名相同）的错误。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在]{lang="EN-US" style="font-family:宋体"}[802.1X]{lang="EN-US"}]{#struct_0_86480_74578_x123313962}[用户采用]{lang="EN-US" style="font-family:宋体"}[EAP]{lang="EN-US"}[认证方式的情况下，]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案中配置的]{lang="EN-US" style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[命令无效，客户端传送给]{lang="EN-US" style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名与用户输入的用户名保持一致。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若接入用户为需要漫游的无线用户，建议接入设备上将发送给]{style="font-family:宋体"}]{#struct_0_86480_74578_31678158}[RADIUS]{lang="DE"}[服务器的用户名格式配置为]{style="font-family:宋体"}**[keep-original]{lang="EN-US"}**[类型，否则可能导致这类用户认证失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2074905292}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x811050634}[指定发送给]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[中]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[服务器的用户名不得携带域名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1653592506}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] user-name-format without-domain]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1936966857}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1657089293}
:::

::::: {#-773178992 .myid}
[]{#_Toc404792607}[]{#struct_0_86480_74578_x1600823954}[]{#_Toc268769787}[]{#_Toc241406162}

**AAA \-- RADIUS配置命令 \-- vpn-instance (RADIUS scheme view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x757397678}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持请与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x1915698685}
:::

[ ]{lang="EN-US"}

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_x810985098}[命令用来配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_867447004}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_30887463}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_1831620780}

[**[undo ]{lang="PT-BR"}[vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_x969665311}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x122394484}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_411512467}[方案属于公网。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1047118378}

[[RADIUS]{lang="EN-US"}]{#struct_0_86480_74578_x1890064238}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x810919562}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_461767481}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1489617746}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_782816509}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_1462549619}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_588260077}

[[本命令配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_436496181}[对于该方案下的所有]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器生效，但设备优先使用配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器时为各服务器单独指定的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x8670694}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1415254598}[配置]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x810854026}

[\[Sysname\] radius scheme radius1]{lang="EN-US"}

[\[Sysname-radius-radius1\] vpn-instance test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x717314673}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1415076672}
:::::

::: {#-1948869357 .myid}
[]{#_Toc49337465}[]{#_Toc49337071}[]{#_Toc268769790}[]{#_Toc205699713}[]{#_Toc162860295}[]{#_Toc147117612}[]{#_Toc147049972}[]{#_Toc146447692}[]{#_Toc69900516}[]{#_Toc58654829}[]{#_Toc55038147}[]{#_Toc404792609}[]{#struct_0_86480_74578_x1965606649}[]{#_Toc315873254}[]{#_Toc268769789}[]{#_Toc205699712}[]{#_Toc162860294}[]{#_Toc147117611}[]{#_Toc147049971}[]{#_Toc146447691}

**AAA \-- HWTACACS配置命令 \-- data-flow-format (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[data-flow-format]{lang="EN-US"}**]{#struct_0_86480_74578_1941602529}[命令用来配置发送到]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的数据流的单位。]{style="font-family:宋体"}

[**[undo data-flow-format]{lang="EN-US"}**]{#struct_0_86480_74578_x10986916}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x810788490}

[**[data-flow-format ]{lang="EN-US"}**[{ **data** { **byte** \| **giga-byte** \| **kilo-byte** \| **mega-byte** } \| **packet** { **giga-packet** \| **kilo-packet** \| **mega-packet** \| **one-packet** } } \*]{lang="EN-US"}]{#struct_0_86480_74578_862812065}

[**[undo data-flow-format ]{lang="EN-US"}**[{ **data** \| **packet** }]{lang="EN-US"}]{#struct_0_86480_74578_x1000387188}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1199621970}

[[数据流的单位为]{style="font-family:宋体"}**[byte]{lang="EN-US"}**]{#struct_0_86480_74578_x782854234}[，数据包的单位为]{style="font-family:宋体"}**[one-packet]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_38344668}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x2068046870}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1787704230}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_606423417}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x811771530}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_496197160}

[**[data]{lang="EN-US"}**]{#struct_0_86480_74578_2020454939}[：设置数据流的单位。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[byte]{lang="EN-US"}**]{#struct_0_86480_74578_1939756410}[：数据流的单位为字节。]{style="font-family:
宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[giga-byte]{lang="EN-US"}**]{#struct_0_86480_74578_1015294853}[：数据流的单位千兆字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[kilo-byte]{lang="EN-US"}**]{#struct_0_86480_74578_x1439770666}[：数据流的单位为千字节。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mega-byte]{lang="EN-US"}**]{#struct_0_86480_74578_896455169}[：数据流的单位为兆字节。]{style="font-family:宋体"}

[**[packet]{lang="EN-US"}**]{#struct_0_86480_74578_x1762598494}[：设置数据包的单位。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[giga-packet]{lang="EN-US"}**]{#struct_0_86480_74578_x811705994}[：数据包的单位为千兆包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[kilo-packet]{lang="EN-US"}**]{#struct_0_86480_74578_2061906074}[：数据包的单位为千包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[mega-packet]{lang="EN-US"}**]{#struct_0_86480_74578_x1414725219}[：数据包的单位为兆包。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[one-packet]{lang="EN-US"}**]{#struct_0_86480_74578_1131207752}[：数据包的单位为包。]{lang="EN-US" style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1267419249}

[[设备上配置的发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1381550255}[服务器的数据流单位及数据包单位应与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上的流量统计单位保持一致，否则无法正确计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1112609289}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1174260440}[在]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[radius1]{lang="EN-US"}[中，设置发往]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的数据流的数据单位为]{style="font-family:宋体"}**[kilo-byte]{lang="EN-US"}**[、数据包的单位为]{style="font-family:宋体"}**[kilo-packet]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x811247245}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] data-flow-format data kilo-byte packet kilo-packet]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_847333010}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1666101519}
:::

::: {#450678287 .myid}
[]{#_Toc404792610}[]{#struct_0_86480_74578_x1154674856}

**AAA \-- HWTACACS配置命令 \-- display hwtacacs scheme**

------------------------------------------------------------------------

[**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_92603950}[命令用来查看]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案的配置信息或]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务相关的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1040151551}

[**[display hwtacacs scheme ]{lang="EN-US"}**[\[ *hwtacacs-scheme-name* \[ **statistics** \] \]]{lang="EN-US"}]{#struct_0_86480_74578_550527212}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1080044015}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_30427613}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811181709}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_899767679}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1435411661}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x217882824}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1742345747}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1320428304}

[*[hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1969121437}[：显示指定的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的配置或统计信息。]{style="font-family:宋体"}*[hwtacacs-scheme-name]{lang="EN-US"}*[为]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[statistics]{lang="EN-US"}**]{#struct_0_86480_74578_2084580619}[：显示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务相关的统计信息。不指定该参数，则显示]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案的配置信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1385141485}

[[如果不指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x811116173}[方案名，则显示所有]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_868662091}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1100574505}[查看所有]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案的配置情况。]{style="font-family:宋体"}

[[\<]{lang="EN-US"}]{#struct_0_86480_74578_x811050637}[]{#_Toc58654830}[[Sysname\> display hwtacacs scheme]{lang="EN-US"}]{#_Toc55038148}

[Total 1 TACACS schemes]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[HWTACACS Scheme Name  : hwtac]{lang="EN-US"}

[  Index : 0]{lang="EN-US"}

[  Primary Auth Server:]{lang="EN-US"}

[    IP  : 2.2.2.2         Port: 49     State: Active]{lang="EN-US"}

[    VPN Instance: 2]{lang="EN-US"}

[    Single-connection: Enabled]{lang="EN-US"}

[  Primary Author Server:]{lang="EN-US"}

[    IP  : 2.2.2.2         Port: 49     State: Active]{lang="EN-US"}

[    VPN Instance: 2]{lang="EN-US"}

[    Single-connection: Disabled]{lang="EN-US"}

[  Primary Acct Server:]{lang="EN-US"}

[    IP  : Not Configured  Port: 49     State: Block]{lang="EN-US"}

[    VPN Instance: Not configured]{lang="EN-US"}

[    Single-connection: Disabled]{lang="EN-US"}

[ ]{lang="EN-US"}

[  VPN Instance                          : 2]{lang="EN-US"}

[  NAS IP Address                        : 2.2.2.3]{lang="EN-US"}

[  Server Quiet Period(minutes)          : 5]{lang="EN-US"}

[  Realtime Accounting Interval(minutes) : 12]{lang="EN-US"}

[  Response Timeout Interval(seconds)    : 5]{lang="EN-US"}

[  Username Format                       : with-domain]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[]{#struct_0_86480_74578_1653789114}[[表1-7 ]{lang="EN-US"}[display hwtacacs scheme]{lang="EN-US"}]{#_Toc138066612}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_791232674}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_377246955}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_x1985932390}

[[Total 1 TACACS schemes]{lang="EN-US"}]{#struct_0_86480_74578_x814684411}

[[共计]{style="font-family:宋体"}[1]{lang="EN-US"}]{#struct_0_86480_74578_602056010}[个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}

[[HWTACACS Scheme Name]{lang="EN-US"}]{#struct_0_86480_74578_x810985101}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1088409389}[方案的名称]{style="font-family:宋体"}

[[Index]{lang="EN-US"}]{#struct_0_86480_74578_x669528235}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_394886221}[方案的索引号]{style="font-family:宋体"}

[[Primary Auth Server]{lang="EN-US"}]{#struct_0_86480_74578_x969322315}

[[主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_289278490}[认证服务器]{style="font-family:宋体"}

[[Primary Author Server]{lang="EN-US"}]{#struct_0_86480_74578_x810919565}

[[主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_461439801}[授权服务器]{style="font-family:宋体"}

[[Primary Acct Server]{lang="EN-US"}]{#struct_0_86480_74578_1203803355}

[[主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x791105974}[计费服务器]{style="font-family:宋体"}

[[Secondary Auth Server]{lang="EN-US"}]{#struct_0_86480_74578_x812809361}

[[从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x810854029}[认证服务器]{style="font-family:宋体"}

[[Secondary Author Server]{lang="EN-US"}]{#struct_0_86480_74578_x717118065}

[[从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_2057926383}[授权服务器]{style="font-family:宋体"}

[[Secondary Acct Server]{lang="EN-US"}]{#struct_0_86480_74578_x137471075}

[[从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x886149635}[计费服务器]{style="font-family:宋体"}

[[IP]{lang="EN-US"}]{#struct_0_86480_74578_x810788493}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_862615457}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_332757794}

[[Port]{lang="EN-US"}]{#struct_0_86480_74578_1162852132}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x2142815237}[服务器的端口号]{style="font-family:宋体"}

[[未配置时，显示缺省值]{style="font-family:宋体"}]{#struct_0_86480_74578_x811771533}

[[Single-connection]{lang="EN-US"}]{#struct_0_86480_74578_496131624}

[[单连接状态]{style="font-family:宋体"}]{#struct_0_86480_74578_x745997752}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[Enabled]{lang="EN-US"}]{#struct_0_86480_74578_1926089382}[：使用一条]{style="font-family:
  宋体"}[TCP]{lang="EN-US"}[连接与服务器通信]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Disabled]{lang="EN-US"}]{#struct_0_86480_74578_x811705997}[：每次新建]{lang="EN-US" style="font-family:宋体"}[TCP]{lang="EN-US"}[连接与服务器通信]{lang="EN-US" style="font-family:宋体"}

[[State]{lang="EN-US"}]{#struct_0_86480_74578_2061709466}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_999692021}[服务器目前状态]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Active]{lang="EN-US"}]{#struct_0_86480_74578_496596895}[：激活状态]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[Block]{lang="EN-US"}]{#struct_0_86480_74578_282368163}[：静默状态]{lang="EN-US" style="font-family:宋体"}

[[VPN Instance]{lang="EN-US"}]{#struct_0_86480_74578_x811247244}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_847398546}[服务器所在的]{style="font-family:宋体"}[VPN]{lang="EN-US"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_1018801550}

[[VPN Instance ]{lang="EN-US"}]{#struct_0_86480_74578_x811181708}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_899833215}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[名称]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_1886030180}

[[NAS IP Address]{lang="EN-US"}]{#struct_0_86480_74578_1353283434}

[[发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x811116172}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[Server Quiet Period]{lang="EN-US"}]{#struct_0_86480_74578_868596555}

[[主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_2095503661}[服务器恢复激活状态的时间（分钟）]{style="font-family:宋体"}

[[Realtime Accounting Interval(minutes)]{lang="EN-US"}]{#struct_0_86480_74578_1887563392}

[[实时]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x811050636}[计费更新报文的发送间隔（分钟）]{style="font-family:宋体"}

[[Response Timeout Interval]{lang="EN-US"}]{#struct_0_86480_74578_1653723578}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x348404009}[服务器超时时间（秒）]{style="font-family:宋体"}

[[Username Format]{lang="EN-US"}]{#struct_0_86480_74578_x810985100}

[[用户名格式]{style="font-family:宋体"}]{#struct_0_86480_74578_x1088343853}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[with-domain]{lang="EN-US"}]{#struct_0_86480_74578_917582758}[：携带]{lang="EN-US" style="font-family:宋体"}[域名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
  font-family:Symbol"}[without-domain]{lang="EN-US"}]{#struct_0_86480_74578_208050838}[：不携带]{lang="EN-US" style="font-family:宋体"}[域名]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:
  10.0pt;font-family:Symbol"}[keep-original]{lang="EN-US"}]{#struct_0_86480_74578_x810919564}[：与用户输入保持一致]{lang="EN-US" style="font-family:宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_461374265}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[reset hwtacacs statistics]{lang="EN-US"}**]{#struct_0_86480_74578_607127381}

::: {#-1179791907 .myid}
[]{#_Toc49337466}[]{#_Toc49337072}[]{#_Toc69900521}[]{#_Toc404792611}[]{#struct_0_86480_74578_1881115612}[]{#_Toc268769792}[]{#_Toc205699715}[]{#_Toc162860297}[]{#_Toc147117614}[]{#_Toc147049974}[]{#_Toc146447694}

**AAA \-- HWTACACS配置命令 \-- hwtacacs nas-ip**

------------------------------------------------------------------------

[**[hwtacacs nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x623067557}[命令用来指定设备发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文使用的源地址。]{style="font-family:宋体"}

[**[undo hwtacacs nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x199062571}[命令用来删除指定的源地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1017986056}

[**[hwtacacs nas-ip]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_x803476167}

[**[undo hwtacacs nas-ip ]{lang="EN-US"}**[{ *ipv4-address* \| **ipv6** *ipv6-address* } \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_x810854028}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x717183601}

[[未指定源地址，即以发送报文的接口的主]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_981496904}[地址作为源地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x592948137}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_781550002}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1718293762}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_449956232}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2094750361}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x810788492}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_862680993}[：指定的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，应该为本机的地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址、]{style="font-family:宋体"}[D]{lang="EN-US"}[类地址、]{style="font-family:宋体"}[E]{lang="EN-US"}[类地址和环回地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_x856332316}[：指定的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1241970445}[：指定私网源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。若不指定该参数，则表示配置的是公网源地址。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1538232906}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1347217326}[服务器上通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来标识接入设备，并根据收到的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是否与服务器所管理的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配，来决定是否处理来自该接入设备的认证或计费请求。因此，为保证认证、授权和计费报文可被服务器正常接收并处理，接入设备上发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文使用的源地址必须与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上指定的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址保持一致。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1427695315}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[系统最多允许指定]{style="font-family:宋体"}]{#struct_0_86480_74578_x276373921}[16]{lang="EN-US"}[个源地址，其中，最多包括一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[公网源地址和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[公网源地址，其余为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[或]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网源地址。新配置的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[公网源地址会覆盖原有的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[公网源地址。而且，对于同一个]{style="font-family:宋体"}[VPN]{lang="EN-US"}[，最多只能指定一个]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[私网源地址和一个]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[私网源地址，新配置会覆盖原有配置。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x811771532}[方案视图下的命令]{lang="EN-US" style="font-family:宋体"}**[nas-ip]{lang="EN-US"}**[只对本]{lang="EN-US" style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案有效，系统视图下的命令]{lang="EN-US" style="font-family:宋体"}**[hwtacacs nas-ip]{lang="EN-US"}**[对所有]{lang="EN-US" style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案有效。]{lang="EN-US" style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案视图下的设置具有更高的优先级。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_496066088}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1657683847}[配置设备发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文使用的源地址为]{style="font-family:宋体"}[129.10.10.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1033124103}

[\[Sysname\] hwtacacs nas-ip 129.10.10.1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_111947884}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_315140469}
:::

::: {#-721016590 .myid}
[]{#_Toc404792612}[]{#struct_0_86480_74578_x1942992226}[]{#_Toc268769793}[]{#_Toc205699716}[]{#_Toc162860298}[]{#_Toc147117615}[]{#_Toc147049975}[]{#_Toc146447695}

**AAA \-- HWTACACS配置命令 \-- hwtacacs scheme**

------------------------------------------------------------------------

[**[hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_360500585}[命令用来创建]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案，并进入]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案视图。]{style="font-family:宋体"}

[**[undo hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x811705996}[命令用来删除指定的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2061775002}

[**[hwtacacs scheme]{lang="EN-US"}**[ *hwtacacs-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_135958067}

[**[undo hwtacacs scheme]{lang="EN-US"}**[ *hwtacacs-scheme-name*]{lang="EN-US"}]{#struct_0_86480_74578_1623991401}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1022777517}

[[不存在任何]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_42667226}[方案。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1314073767}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x230840486}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811247247}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_847201938}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x471255771}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1587437479}

[*[hwtacacs-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1931334845}[：]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1992442574}

[[一个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x24416528}[方案可以同时被多个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域引用。]{style="font-family:宋体"}

[[最多可以配置]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_86480_74578_x703810830}[个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1667370520}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x811181711}[创建名为]{style="font-family:宋体"}[hwt1]{lang="EN-US"}[的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案并进入相应的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_900291968}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1870832570}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x897490382}
:::

::: {#-1868206349 .myid}
[]{#_Toc404792613}[]{#struct_0_86480_74578_x1596643795}[]{#_Toc268769794}[]{#_Toc205699717}[]{#_Toc162860299}[]{#_Toc147117616}[]{#_Toc147049976}[]{#_Toc146447696}

**AAA \-- HWTACACS配置命令 \-- key (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[key]{lang="EN-US"}**]{#struct_0_86480_74578_x1819523296}[命令用来配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证、授权、计费报文的共享密钥。]{style="font-family:宋体"}

[**[undo key]{lang="EN-US"}**]{#struct_0_86480_74578_x612108578}[命令用来删除配置。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811116175}

[**[key ]{lang="EN-US"}**[{ **accounting** \| **authentication** \| **authorization** } { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_868268875}

[**[undo key ]{lang="EN-US"}**[{ **accounting** \| **authentication** \| **authorization** }]{lang="EN-US"}]{#struct_0_86480_74578_x866980869}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1606278749}

[[无共享密钥。]{style="font-family:宋体"}]{#struct_0_86480_74578_2035724200}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x151833073}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1169134905}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_2097686041}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1750545832}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x811050639}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1653920186}

[**[accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1517280271}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费报文的共享密钥。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x67423406}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证报文的共享密钥。]{style="font-family:宋体"}

[**[authorization]{lang="EN-US"}**]{#struct_0_86480_74578_x1947151294}[：指定]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权报文的共享密钥。]{style="font-family:宋体"}

[**[cipher]{lang="EN-US"}**]{#struct_0_86480_74578_344938040}[：表示以密文方式设置共享密钥。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_86480_74578_4733683}[：表示以明文方式设置共享密钥。]{style="font-family:宋体"}

[*[key]{lang="EN-US"}*]{#struct_0_86480_74578_x1695647396}[：设置的明文密钥或密文密钥，区分大小写。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串；密文密钥为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，明文密钥为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，密钥元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）；密文密钥为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1477127903}

[[必须保证设备上设置的共享密钥与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x810985103}[服务器上的完全一致。]{style="font-family:宋体"}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1088540461}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x392410524}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_500377127}[配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证报文共享密钥为明文]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1456043993}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] key authentication simple 123456TESTauth&!]{lang="EN-US"}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x808215460}[配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权报文共享密钥为明文]{style="font-family:宋体"}[123456TESTautr&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-hwtacacs-hwt1\] key authorization simple 123456TESTautr&!]{lang="EN-US"}]{#struct_0_86480_74578_1352611777}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x810919567}[配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费报文共享密钥为明文]{style="font-family:宋体"}[123456TESTacct&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\[Sysname-hwtacacs-hwt1\] key accounting simple 123456TESTacct&!]{lang="EN-US"}]{#struct_0_86480_74578_461570873}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_811308381}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_454017246}
:::

::: {#-1340810809 .myid}
[]{#_Toc404792614}[]{#struct_0_86480_74578_769803577}[]{#_Toc268769795}[]{#_Toc205699718}[]{#_Toc162860300}[]{#_Toc147117617}[]{#_Toc147049977}[]{#_Toc146447697}

**AAA \-- HWTACACS配置命令 \-- nas-ip (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_782671098}[命令用来指定设备发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_1285626253}[命令用来删除指定的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_439902305}

[**[nas-ip]{lang="PT-BR"}**]{#struct_0_86480_74578_x810854031}[ { *ipv4-address* \| **ipv6**]{lang="PT-BR"}[ ]{lang="PT-BR"}*[ipv6-address]{lang="PT-BR"}*[ }]{lang="PT-BR"}

[**[undo nas-ip ]{lang="PT-BR"}**]{#struct_0_86480_74578_x717642354}[\[ **ipv6** \]]{lang="PT-BR"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2110646701}

[[使用系统视图下由命令]{style="font-family:宋体"}]{#struct_0_86480_74578_x1400380900}**[hwtacacs nas-ip]{lang="PT-BR"}**[指定的源地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[若系统视图下未指定源地址]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则使用发送]{style="font-family:宋体"}[HWTACACS]{lang="PT-BR"}[报文的接口的主]{style="font-family:宋体"}[IP]{lang="PT-BR"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1308865802}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1498453527}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x358710202}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_853930668}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_618087894}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x810788495}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_863008673}[：指定的源]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址，应该为本机的地址，不能为全]{style="font-family:宋体"}[0]{lang="EN-US"}[地址、全]{style="font-family:宋体"}[1]{lang="EN-US"}[地址、]{style="font-family:宋体"}[D]{lang="EN-US"}[类地址、]{style="font-family:宋体"}[E]{lang="EN-US"}[类地址和环回地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**[ *ipv6-address*]{lang="EN-US"}]{#struct_0_86480_74578_56378734}[：指定的源]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址，应该为本机的地址，必须是单播地址，不能为环回地址与本地链路地址。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x682198675}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1092329355}[服务器上通过]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址来标识接入设备，并根据收到的]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址是否与服务器所管理的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址匹配，来决定是否处理来自该接入设备的认证、授权、计费请求。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1082704038}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[为保证认证和计费报文可被服务器正常接收并处理，接入设备上发送]{style="font-family:宋体"}]{#struct_0_86480_74578_x497794359}[HWTACACS]{lang="EN-US"}[报文使用的源地址必须与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器上指定的接入设备的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x94504783}[方案视图下的命令]{style="font-family:
宋体"}**[nas-ip]{lang="EN-US"}**[只对本]{style="font-family:
宋体"}[HW]{lang="EN-US"}[TACACS]{lang="EN-US"}[方案有效，系统视图下的命令]{lang="EN-US" style="font-family:宋体"}**[hwtacacs nas-ip]{lang="EN-US"}**[对所有]{lang="EN-US" style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案有效。]{lang="EN-US" style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案视图下的设置具有更高的优先级。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果重复执行此命令，新配置的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x811771535}[源地址会覆盖原有的]{style="font-family:宋体"}[IPv4/IPv6]{lang="EN-US"}[源地址。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_496000552}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1229882830}[为]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[hwt1]{lang="EN-US"}[配置设备发送]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文使用的源]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.1.1.1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x405201905}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] nas-ip 10.1.1.1]{lang="PT-BR"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x650812069}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[hwtacacs nas-ip]{lang="EN-US"}**]{#struct_0_86480_74578_x1398601260}
:::

::: {#-964502779 .myid}
[]{#_Toc404792615}[]{#struct_0_86480_74578_x1792035222}[]{#_Toc268769796}[]{#_Toc205699719}[]{#_Toc162860301}[]{#_Toc147117618}[]{#_Toc147049978}[]{#_Toc146447698}

**AAA \-- HWTACACS配置命令 \-- primary accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1165224605}[命令用来配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[**[undo primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x811705999}[命令用来删除配置的主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2062102682}

[**[primary accounting ]{lang="EN-US"}**[{ ]{lang="EN-US"}]{#struct_0_86480_74578_x344313816}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] **\***]{lang="EN-US"}

[**[undo primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x897082285}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x427082749}

[[未配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1872959066}[主计费服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1077209137}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_370154451}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1188958665}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x811247246}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_847267474}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x115859266}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x137165988}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_280075009}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x53340351}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供计费服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_x2110499026}[：与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1764957105}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x811181710}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_900357504}[：所有与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器交互的计费报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示每次计费都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_1251903602}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[ ]{lang="EN-US"}[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。如果未指定本参数，则表示主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器位于公网中。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_856213017}

[[在同一个方案中指定的主计费服务器和从计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_717778298}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同。]{style="font-family:宋体"}

[[若服务器位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}]{#struct_0_86480_74578_1622148074}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[只有在设备与计费服务器没有报文交互时，才允许删除该服务器。计费服务器删除后，只对之后的计费过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_x623060835}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1720385418}

[[配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x811116174}[参数后可节省]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_868203339}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1843797094}[配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.12]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器通信，计费报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTacct&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x298976153}

[\[Sysname\] hwtacacs scheme test1]{lang="EN-US"}

[\[Sysname-hwtacacs-test1\] primary accounting 10.163.155.12 49 key simple 123456TESTacct&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x523235395}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1703650013}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x144759896}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary]{lang="EN-US"}[ accounting]{lang="EN-US"}**]{#struct_0_86480_74578_756296429}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x811050638}
:::

::: {#-760081391 .myid}
[]{#_Toc404792616}[]{#struct_0_86480_74578_1653854650}[]{#_Toc268769797}[]{#_Toc205699720}[]{#_Toc162860302}[]{#_Toc147117619}[]{#_Toc147049979}[]{#_Toc146447699}[]{#_Toc69900523}

**AAA \-- HWTACACS配置命令 \-- primary authentication (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1119202911}[命令用来配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[**[undo primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x2026955721}[命令用来删除配置的主]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[认证服务器]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_893018648}

[**[primary authentication]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x1145158251}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_956133667}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2001415577}

[[未配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x2107351309}[认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x810985102}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1088474925}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1961024298}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_929228062}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1259964811}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_374114038}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_1362770748}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_476599151}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x810919566}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供认证服务的端口号保持一致。]{style="font-family:宋体"}

[**[key ]{lang="EN-US"}**[{ **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_461505337}[：与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_104501837}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1391597389}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_1536752266}[：所有与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器交互的计费报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示向主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器发送计费报文都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1962869271}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1976852024}

[[在同一个方案中指定的主认证服务器和从认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x480720144}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同。]{style="font-family:宋体"}

[[若服务器位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}]{#struct_0_86480_74578_x237615863}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[只有在设备与认证服务器没有报文交互时，才允许删除该服务器。认证服务器删除后，只对之后的认证过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_x810854030}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x717707890}

[[配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_1671120737}[参数后可节省]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1845179624}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_637295912}[配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.13]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器通信，认证报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x916324684}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] primary authentication 10.163.155.13 49 key simple 123456TESTauth&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1029219504}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1337150869}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x810788494}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary]{lang="EN-US"}[ authentication]{lang="EN-US"}**]{#struct_0_86480_74578_863074209}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1216288719}
:::

::: {#1195535760 .myid}
[]{#_Toc404792617}[]{#struct_0_86480_74578_949201470}[]{#_Toc268769798}[]{#_Toc205699721}[]{#_Toc162860303}[]{#_Toc147117620}[]{#_Toc147049980}[]{#_Toc146447700}[]{#_Toc69900525}

**AAA \-- HWTACACS配置命令 \-- primary authorization**

------------------------------------------------------------------------

[**[primary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_x1013954399}[命令用来配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器。]{style="font-family:宋体"}

[**[undo primary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_455523487}[命令用来删除配置的主]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[授权服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1457208796}

[**[primary authorization]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ ]{lang="EN-US"}]{#struct_0_86480_74578_x1634088414}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo primary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_x1980998323}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x811771534}

[[未配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_495935016}[授权服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_318640105}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1033102354}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x29950409}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x912066437}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1706212080}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1549255955}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_870939866}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_x811705998}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_2062168218}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供授权服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_x1110990319}[：与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器交互的授权报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x1444615307}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_290670732}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[ FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x1430555363}[：所有与主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器交互的授权报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示每次授权都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1357687472}[：主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1638206924}

[[在同一个方案中指定的主授权服务器和从授权服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_1111067058}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同。]{style="font-family:宋体"}

[[若服务器位于]{style="font-family:宋体"}[MPLS VPN]{lang="EN-US"}]{#struct_0_86480_74578_x238192189}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[只有在设备与授权服务器没有报文交互时，才允许删除该服务器。授权服务器删除后，只对之后的授权过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_922602302}

[[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x569266373}

[[配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_1842994238}[参数后可节省]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{style="font-family:宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2027974722}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x771861592}[配置主]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.13]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器通信，授权报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTautr&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1499099536}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] primary authorization 10.163.155.13 49[]{#_Toc58654835}[]{#_Toc55038153}[]{#_Toc50534432} [key simple 123456TESTautr&!]{#_Toc49337059}]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111132594}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1359813577}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x680081859}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[secondary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_x1539065699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_2125704842}
:::

::: {#-751687974 .myid}
[]{#_Toc69900529}[]{#_Toc404792618}[]{#struct_0_86480_74578_721900760}[]{#_Toc268769799}[]{#_Toc205699722}[]{#_Toc162860304}[]{#_Toc147117621}[]{#_Toc147049981}[]{#_Toc146447701}

**AAA \-- HWTACACS配置命令 \-- reset hwtacacs statistics**

------------------------------------------------------------------------

[**[reset hwtacacs statistics]{lang="EN-US"}**]{#struct_0_86480_74578_849633338}[命令用来清除]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[协议的统计信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1640360754}

[**[reset hwtacacs statistics ]{lang="EN-US"}**[{ **accounting** \| **all** \| **authentication** \| **authorization** }]{lang="EN-US"}]{#struct_0_86480_74578_x611154372}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111198130}

[[用户视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x673338915}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_608460132}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1363554976}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x10272822}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_252286559}

[**[accounting]{lang="EN-US"}**]{#struct_0_86480_74578_931842076}[：清除]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[协议关于计费的统计信息。]{style="font-family:宋体"}

[**[all]{lang="EN-US"}**]{#struct_0_86480_74578_x1303371193}[：清除]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[的所有统计信息。]{style="font-family:宋体"}

[**[authentication]{lang="EN-US"}**]{#struct_0_86480_74578_544028910}[：清除]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[协议关于认证的统计信息。]{style="font-family:宋体"}

[**[authorization]{lang="EN-US"}**]{#struct_0_86480_74578_1111263666}[：清除]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[协议关于授权的统计信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1349756824}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1233680427}[清除]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[协议的所有统计信息。]{style="font-family:宋体"}

[[\<Sysname\> reset hwtacacs statistics all]{lang="EN-US"}]{#struct_0_86480_74578_480623751}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x840602373}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_178661467}
:::

::: {#-1743419711 .myid}
[]{#_Toc404792619}[]{#struct_0_86480_74578_1346455958}[]{#_Toc268769802}[]{#_Toc205699725}[]{#_Toc162860307}[]{#_Toc147117624}[]{#_Toc147049984}[]{#_Toc146447704}

**AAA \-- HWTACACS配置命令 \-- secondary accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[secondary]{lang="EN-US"}[ accounting]{lang="EN-US"}**]{#struct_0_86480_74578_555083132}[命令用来配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[**[undo secondary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_1111329202}[命令用来删除指定的从]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[计费服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x653118075}

[**[secondary]{lang="EN-US"}[ accounting]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1171429082}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo secondary accounting ]{lang="EN-US"}**[\[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1700076312}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \] \* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1918569760}

[[未配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1260270777}[计费服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x349416433}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_758142381}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1959532435}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1111394738}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_914216887}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2062288538}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_76325424}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_726920651}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1032189349}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供计费服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[ { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_1075463485}[：与从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器交互的计费报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_416393510}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1111460274}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_1711015070}[：所有与从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器交互的计费报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示每次计费都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_494887676}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1723108925}

[[可通过多次执行本命令，配置多个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x765299417}[计费服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器并与之交互。每个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案中最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1857490843}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则]{style="font-family:宋体"}]{#struct_0_86480_74578_x153627245}**[undo]{lang="EN-US"}**[命令将删除所有从计费服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个方案中指定的主计费服务器和从计费服务器的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1264663918}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同，并且各从计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数也不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若服务器位于]{style="font-family:宋体"}]{#struct_0_86480_74578_x1700809011}[MPLS VPN]{lang="EN-US"}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在设备与计费服务器没有报文交互时，才允许删除该服务器。计费服务器删除后，只对之后的计费过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_1111525810}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x595565996}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x121404451}[参数后可节省]{lang="EN-US" style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{lang="EN-US" style="font-family:
宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_951201519}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1833860986}[配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.12]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[计费服务器通信，计费报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTacct&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1154518729}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] secondary accounting 10.163.155.12 49 key simple 123456TESTacct&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1567446022}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1098379541}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1110542770}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary accounting]{lang="EN-US"}**]{#struct_0_86480_74578_568924999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1039873659}
:::

::: {#437020189 .myid}
[]{#_Toc404792620}[]{#struct_0_86480_74578_698779825}[]{#_Toc268769803}[]{#_Toc205699726}[]{#_Toc162860308}[]{#_Toc147117625}[]{#_Toc147049985}[]{#_Toc146447705}

**AAA \-- HWTACACS配置命令 \-- secondary authentication (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[secondary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1133464567}[命令用来配置从]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[认证服务器。]{style="font-family:
宋体"}

[**[undo secondary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_1144710917}[命令用来删除指定的从]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[认证服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_18957174}

[**[secondary authentication]{lang="EN-US"}**[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x851264118}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* I **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo secondary authentication ]{lang="EN-US"}**[\[ { ]{lang="EN-US"}]{#struct_0_86480_74578_1110608306}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \]\* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1433556549}

[[未配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_295101413}[认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_895239719}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1181945541}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_230604118}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_683445244}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x863641524}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1302894111}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_1111067059}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}***[ ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_x238126653}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x570820393}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供认证服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="EN-US"}**[  { **cipher** \| **simple** } *string*]{lang="EN-US"}]{#struct_0_86480_74578_1377108747}[：与从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器交互的认证报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_1599901716}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_x447356183}[：]{lang="EN-US" style="font-family:宋体"}[以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写；]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[密钥元素的最少组合类型为]{lang="EN-US" style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x1333504685}[：所有与从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器交互的认证报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示每次认证都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x467993456}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111132595}

[[可通过多次执行本命令，配置多个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1359748041}[认证服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器并与之交互。每个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案中最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1903244916}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则]{style="font-family:宋体"}]{#struct_0_86480_74578_2077989696}**[undo]{lang="EN-US"}**[命令命令将删除所有从认证服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个方案中指定的主认证服务器和从认证服务器的]{style="font-family:宋体"}]{#struct_0_86480_74578_1544555969}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同，并且各从认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数也不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若服务器位于]{style="font-family:宋体"}]{#struct_0_86480_74578_144500063}[MPLS VPN]{lang="EN-US"}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在设备与认证服务器没有报文交互时，才允许删除该服务器。认证服务器删除后，只对之后的认证过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_1067860951}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x627420473}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x429194914}[参数后可节省]{lang="EN-US" style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{lang="EN-US" style="font-family:
宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111198131}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x673404451}[配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.13]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证服务器通信，认证报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTauth&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x669657873}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] secondary authentication 10.163.155.13 49 key simple 123456TESTauth&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x471969339}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x332666512}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_806812062}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary authentication]{lang="EN-US"}**]{#struct_0_86480_74578_x1145475722}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1061350551}
:::

::: {#-1163366803 .myid}
[]{#_Toc404792621}[]{#struct_0_86480_74578_1111263667}[]{#_Toc268769804}[]{#_Toc205699727}[]{#_Toc162860309}[]{#_Toc147117626}[]{#_Toc147049986}[]{#_Toc146447706}

**AAA \-- HWTACACS配置命令 \-- secondary authorization**

------------------------------------------------------------------------

[**[secondary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_1349822360}[命令用来配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器。]{style="font-family:宋体"}

[**[undo secondary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_1894341022}[命令用来删除指定的从]{style="font-family:
宋体"}[HWTACACS]{lang="EN-US"}[授权服务器。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1608180791}

[**[secondary authorization]{lang="EN-US"}***[ ]{lang="EN-US"}*[{ ]{lang="EN-US"}]{#struct_0_86480_74578_1595745217}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* I **key** { **cipher** \| **simple** } *string* \| **single-connection** \| **vpn-instance** *vpn-instance-name* \] \*]{lang="EN-US"}

[**[undo secondary authorization ]{lang="EN-US"}**[\[ { ]{lang="EN-US"}]{#struct_0_86480_74578_x170019301}*[ipv4-address]{lang="PT-BR"}*[ ]{lang="PT-BR"}[\| **ipv6** *ipv6-address* } \[ *port-number* \| **vpn-instance** *vpn-instance-name* \]\* \]]{lang="EN-US"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1433475032}

[[未配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x1472224339}[授权服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111329203}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x653052539}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1913190287}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1284266259}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1116774163}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x856000423}

[*[ipv4-address]{lang="EN-US"}*]{#struct_0_86480_74578_x2037845593}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_1781019450}*[ ]{lang="EN-US"}[ipv6-address]{lang="NO-BOK"}*[：]{style="font-family:宋体"}[从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权]{style="font-family:宋体"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[*[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x538556615}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省为]{style="font-family:宋体"}[49]{lang="EN-US"}[。此端口号必须与服务器提供授权服务的端口号保持一致。]{style="font-family:宋体"}

[**[key]{lang="NO-BOK"}**]{#struct_0_86480_74578_1111394739}[ { **cipher** \| **simple** } *string*]{lang="NO-BOK"}[：]{style="font-family:宋体"}[与从]{style="font-family:宋体"}[HWTACACS]{lang="NO-BOK"}[授权服务器交互的授权报文的共享密钥。此共享密钥必须与服务器上配置的共享密钥保持一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[cipher ]{lang="EN-US"}***[string]{lang="EN-US"}*]{#struct_0_86480_74578_914151351}[：]{lang="EN-US" style="font-family:宋体"}[以密文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写；]{style="font-family:宋体"}[ FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[373]{lang="EN-US"}[个字符的密文字符串，区分大小写。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[simple ]{lang="EN-US"}**]{#struct_0_86480_74578_x2078413631}*[string]{lang="EN-US"}*[：以明文方式设置共享密钥。非]{style="font-family:宋体"}[FIPS]{lang="EN-US"}[模式下，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，]{style="font-family:宋体"}[ FIPS]{lang="EN-US"}[模式下，]{style="font-family:宋体"}*[string]{lang="EN-US"}*[为]{style="font-family:宋体"}[15]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的明文字符串，区分大小写，密钥元素的最少组合类型为]{style="font-family:宋体"}[4]{lang="EN-US"}[（必须包括数字、大写字母、小写字母以及特殊字符）。]{style="font-family:宋体"}

[**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x664285744}[：所有与从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器交互的授权报文使用同一个]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。如果未指定本参数，则表示每次授权都会使用一个新的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[连接。]{style="font-family:宋体"}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x2123405404}[：从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。该参数的支持情况与设备的型号有关，请以设备的实际情况为准。如果未指定本参数，则表示从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器位于公网中。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1918643099}

[[可通过多次执行本命令，配置多个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x870855591}[授权服务器。当主服务器不可达时，设备根据从服务器的配置顺序由先到后查找状态为]{style="font-family:宋体"}**[active]{lang="EN-US"}**[的从服务器并与之交互。每个]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案中最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}[个从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_1575444699}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[如果不指定任何参数，则]{style="font-family:宋体"}]{#struct_0_86480_74578_x78313737}**[undo]{lang="EN-US"}**[命令将删除所有从授权服务器。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[在同一个方案中指定的主授权服务器和从授权服务器的]{style="font-family:宋体"}]{#struct_0_86480_74578_1111460275}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数不能完全相同，并且各从授权服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址、端口号和]{style="font-family:宋体"}[VPN]{lang="EN-US"}[参数也不能完全相同。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[若服务器位于]{style="font-family:宋体"}]{#struct_0_86480_74578_1711080606}[MPLS VPN]{lang="EN-US"}[私网中，为保证]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[报文被发送到指定的私网服务器，必须指定服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称。本命令指定的服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[比]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[优先级高。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[只有在设备与授权服务器没有报文交互时，才允许删除该服务器。授权服务器删除后，只对之后的授权过程有影响。]{style="font-family:宋体"}]{#struct_0_86480_74578_539362596}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[以明文或密文方式设置的共享密钥，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_x266754494}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**]{#struct_0_86480_74578_x1947470884}[参数后可节省]{lang="EN-US" style="font-family:
宋体"}[TCP]{lang="EN-US"}[连接资源，但有些]{lang="EN-US" style="font-family:
宋体"}[TACACS]{lang="EN-US"}[服务器不支持这种方式，需要根据服务器支持情况进行配置。在服务器支持这种方式的情况下，建议配置]{lang="EN-US" style="font-family:宋体"}**[single-connection]{lang="EN-US"}**[参数，以提高性能和效率。]{lang="EN-US" style="font-family:
宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1828664528}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_306078000}[配置从]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[10.163.155.13]{lang="EN-US"}[，使用]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口]{style="font-family:宋体"}[49]{lang="EN-US"}[与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[授权服务器通信，授权报文的共享密钥为明文]{style="font-family:宋体"}[123456TESTautr&!]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1111525811}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] secondary authorization 10.163.155.13 49 key simple 123456TESTautr&!]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x595500460}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_606742027}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[key ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_x194890294}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[primary authorization]{lang="EN-US"}**]{#struct_0_86480_74578_x1062197584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[vpn-instance ]{lang="EN-US"}**[(HWTACACS scheme view)]{lang="EN-US"}]{#struct_0_86480_74578_1397993134}
:::

::: {#-1292253321 .myid}
[]{#_Toc404792622}[]{#struct_0_86480_74578_x1704592972}[]{#_Toc268769806}[]{#_Toc205699729}[]{#_Toc162860311}[]{#_Toc147117628}[]{#_Toc147049988}[]{#_Toc146447708}

**AAA \-- HWTACACS配置命令 \-- timer quiet (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[timer quiet]{lang="EN-US"}**]{#struct_0_86480_74578_729794830}[命令用来设置服务器恢复激活状态的时间。]{style="font-family:宋体"}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_86480_74578_1110542771}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_568990535}

[**[timer quiet ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_x1728926616}

[**[undo timer quiet]{lang="EN-US"}**]{#struct_0_86480_74578_x1465178074}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x365077272}

[[服务器恢复激活状态的时间为]{style="font-family:宋体"}[5]{lang="EN-US"}]{#struct_0_86480_74578_1877364890}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1543440271}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x927186096}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x100132968}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1110608307}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1433491013}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_360522294}

[*[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_x388746773}[：恢复激活状态的时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1125985858}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x860826387}[设置服务器恢复激活状态的时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_248765810}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] timer quiet 10]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_623429211}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1111067056}
:::

::: {#-1497274746 .myid}
[]{#_Toc404792623}[]{#struct_0_86480_74578_x237274685}[]{#_Toc268769807}[]{#_Toc205699730}[]{#_Toc162860312}[]{#_Toc147117629}[]{#_Toc147049989}[]{#_Toc146447709}

**AAA \-- HWTACACS配置命令 \-- timer realtime-accounting (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1557852291}[命令用来设置实时计费的时间间隔。]{style="font-family:
宋体"}

[**[undo timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x1018450738}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1500530915}

[**[timer realtime-accounting ]{lang="EN-US"}***[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_x233757883}

[**[undo timer realtime-accounting]{lang="EN-US"}**]{#struct_0_86480_74578_248415469}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_679492867}

[[实时计费的时间间隔为]{style="font-family:宋体"}[12]{lang="EN-US"}]{#struct_0_86480_74578_x1066035463}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111132592}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1359420361}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_66200715}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1234855975}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1795662258}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_136667657}

[*[minutes]{lang="EN-US"}*]{#struct_0_86480_74578_1354174245}[：实时计费的时间间隔，取值范围为]{style="font-family:宋体"}[0]{lang="EN-US"}[～]{style="font-family:宋体"}[60]{lang="EN-US"}[，单位为分钟。]{style="font-family:宋体"}[0]{lang="EN-US"}[表示设备不向]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器发送在线用户的计费信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1962103434}

[[为了对用户实施实时计费，有必要设置实时计费的时间间隔。在设置了该属性以后，每隔设定的时间，设备会向]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1111198128}[服务器发送一次在线用户的计费信息。]{style="font-family:宋体"}

[[实时计费间隔的取值与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x672814628}[服务器的性能和用户的数目有一定的关系。取值越小，对设备和]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的性能要求越高。建议当用户量比较大（大于等于]{style="font-family:宋体"}[1000]{lang="EN-US"}[）时，尽量把该间隔的值设置得大一些。以下是实时计费间隔与用户量之间的推荐比例关系。]{style="font-family:宋体"}

[]{#struct_0_86480_74578_1692849520}[]{#_Toc138066613}[]{#_Toc95386914}[]{#_Toc85621928}[[表1-8 ]{lang="EN-US"}[实时计费间隔与用户量之间的推荐比例关系]{style="font-family:黑体"}]{#_Toc81452876}

[]{#table_struct_0_548868962}[[用户数]{style="font-family:黑体"}]{#struct_0_86480_74578_1649819187}
:::

[[实时计费间隔（分钟）]{style="font-family:黑体"}]{#struct_0_86480_74578_1391221832}

[[1]{lang="EN-US"}]{#struct_0_86480_74578_x518462383}[～]{style="font-family:宋体"}[99]{lang="EN-US"}

[[3]{lang="EN-US"}]{#struct_0_86480_74578_x1823610514}

[[100]{lang="EN-US"}]{#struct_0_86480_74578_1111263664}[～]{style="font-family:宋体"}[499]{lang="EN-US"}

[[6]{lang="EN-US"}]{#struct_0_86480_74578_1349625752}

[[500]{lang="EN-US"}]{#struct_0_86480_74578_x1599347266}[～]{style="font-family:宋体"}[999]{lang="EN-US"}

[[12]{lang="EN-US"}]{#struct_0_86480_74578_x877794961}

[[大于等于]{style="font-family:宋体"}[1000]{lang="EN-US"}]{#struct_0_86480_74578_x760621812}

[[大于等于]{style="font-family:宋体"}[15]{lang="EN-US"}]{#struct_0_86480_74578_x835348959}

**[ ]{lang="EN-US"}**

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111329200}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x653249147}[将]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[hwt1]{lang="EN-US"}[的实时计费的时间间隔设置为]{style="font-family:宋体"}[51]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_410067487}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] timer realtime-accounting 51]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_31384088}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x940594696}

::: {#-112544359 .myid}
[]{#_Toc404792624}[]{#struct_0_86480_74578_17645260}[]{#_Toc268769808}[]{#_Toc205699731}[]{#_Toc162860313}[]{#_Toc147117630}[]{#_Toc147049990}[]{#_Toc146447710}[]{#_Toc69900530}

**AAA \-- HWTACACS配置命令 \-- timer response-timeout (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_x2085355602}[命令用来设置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器响应超时时间。]{style="font-family:宋体"}

[**[undo timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_73532391}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111394736}

[**[timer response-timeout ]{lang="EN-US"}***[seconds]{lang="EN-US"}*]{#struct_0_86480_74578_914085815}

[**[undo timer response-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_1361053505}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x170085987}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_90660708}[服务器响应超时时间为]{style="font-family:宋体"}[5]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1773749495}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x2003428551}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1698358874}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1111460272}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1710883998}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1349887572}

[*[seconds]{lang="EN-US"}*]{#struct_0_86480_74578_1137769420}[：]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器响应超时时间，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[300]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1287895815}

[[由于]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_x807088210}[是基于]{style="font-family:宋体"}[TCP]{lang="EN-US"}[实现的，因此，服务器响应超时或]{style="font-family:宋体"}[TCP]{lang="EN-US"}[超时都可能导致与]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的连接断开。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1528534357}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x293379893}[配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器响应超时时间为]{style="font-family:宋体"}[30]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1111525808}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] timer response-timeout 30]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x596090285}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x313711304}
:::

::: {#-1710700952 .myid}
[]{#_Toc404792625}[]{#struct_0_86480_74578_296246821}[]{#_Toc268769809}[]{#_Toc205699732}[]{#_Toc162860314}[]{#_Toc147117631}[]{#_Toc147049991}[]{#_Toc146447711}[]{#_Toc69900532}

**AAA \-- HWTACACS配置命令 \-- user-name-format (HWTACACS scheme view)**

------------------------------------------------------------------------

[**[user-name-format]{lang="DE"}**]{#struct_0_86480_74578_x814046472}[命令用来设置发送给]{style="font-family:宋体"}[HWTACACS]{lang="DE"}[服务器的用户名格式。]{style="font-family:宋体"}

[**[undo user-name-format]{lang="DE"}**]{#struct_0_86480_74578_x584664340}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2048989083}

[**[user-name-format]{lang="EN-US"}**[ { **keep-original** \| **with-domain** \| **without-domain** }]{lang="EN-US"}]{#struct_0_86480_74578_x936030345}

[**[undo user-name-format]{lang="EN-US"}**]{#struct_0_86480_74578_x2235989}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1110542768}

[[设备发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_569449286}[服务器的用户名携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_709648124}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1749076388}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x730167253}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x160201671}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x20277962}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2017916166}

[**[keep-original]{lang="EN-US"}**]{#struct_0_86480_74578_1110608304}[：发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的用户名与用户输入的保持一致。]{style="font-family:宋体"}

[**[with-domain]{lang="EN-US"}**]{#struct_0_86480_74578_x1433425477}[：发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的用户名带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[**[without-domain]{lang="EN-US"}**]{#struct_0_86480_74578_759004015}[：发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的用户名不带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_866664235}

[[接入用户通常以"]{style="font-family:宋体"}*[userid@isp-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1422961053}["的格式命名，"]{style="font-family:宋体"}*[@]{lang="EN-US"}*["后面的部分为]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，设备就是通过该域名来决定将用户归于哪个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域的。但是，有些]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器不能接受携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名的用户名，在这种情况下，有必要将用户名中携带的域名去除后再传送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器。因此，设备提供此命令以指定发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器的用户名是否携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x494850646}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[如果指定某个]{style="font-family:宋体"}]{#struct_0_86480_74578_x343333211}[HWTACACS]{lang="EN-US"}[方案不允许用户名中携带有]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名，那么请不要在两个乃至两个以上的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中同时设置使用该]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案。否则，会出现虽然实际用户不同（在不同的]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域中），但]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[服务器认为用户相同（因为传送到它的用户名相同）的错误。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[若接入用户为需要漫游的无线用户，接入设备上将发送给]{style="font-family:宋体"}]{#struct_0_86480_74578_762158163}[HWTACACS]{lang="EN-US"}[服务器的用户名格式配置为]{style="font-family:宋体"}**[keep-original]{lang="EN-US"}**[类型，否则可能导致这类用户认证失败。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111067057}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x237209149}[指定发送给]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[hwt1]{lang="EN-US"}[的用户不带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1503859242}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] user-name-format without-domain]{lang="EN-US"}[]{#_Hlt15806306}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1578681256}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1961434345}
:::

::::: {#232469504 .myid}
[]{#_Toc404792626}[]{#struct_0_86480_74578_53093808}[]{#_Toc268769810}[]{#_Toc241406186}

**AAA \-- HWTACACS配置命令 \-- vpn-instance (HWTACACS scheme view)**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 4 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x1539304532}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持请与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_1190124486}
:::

**[ ]{lang="EN-US"}**

[**[vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_1111132593}[命令用来配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_1359354825}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1233015498}

[**[vpn-instance ]{lang="EN-US"}***[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_1387843083}

[**[undo ]{lang="PT-BR"}[vpn-instance]{lang="EN-US"}**]{#struct_0_86480_74578_523567575}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x303448615}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_900830777}[方案属于公网。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1641193445}

[[HWTACACS]{lang="EN-US"}]{#struct_0_86480_74578_1111198129}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x672880164}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_2065892096}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1070477186}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1300661358}

[*[vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_x526038557}[：]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[实例名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1357601464}

[[本命令配置的]{style="font-family:宋体"}[VPN]{lang="EN-US"}]{#struct_0_86480_74578_458816778}[对于该方案下的所有]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器生效，但设备优先使用配置认证]{style="font-family:宋体"}[/]{lang="EN-US"}[授权]{style="font-family:宋体"}[/]{lang="EN-US"}[计费服务器时指定的各服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111263665}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1349691288}[配置]{style="font-family:宋体"}[HWTACACS]{lang="EN-US"}[方案]{style="font-family:宋体"}[hw1]{lang="EN-US"}[所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[为]{style="font-family:宋体"}[test]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x483018697}

[\[Sysname\] hwtacacs scheme hwt1]{lang="EN-US"}

[\[Sysname-hwtacacs-hwt1\] vpn-instance test]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1495359707}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display hwtacacs scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1155300437}
:::::

::: {#-1026601401 .myid}
[]{#_Toc404792628}[]{#struct_0_86480_74578_2093783638}[]{#_Toc391364212}

**AAA \-- LDAP配置命令 \-- attribute-map**

------------------------------------------------------------------------

[**[attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_838397501}[命令用来在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案中引用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表。]{style="font-family:宋体"}

[**[undo attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_1690499111}[命令用来删除引用的指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_2120892086}

[[**[attribute-map]{lang="EN-US"}**]{.ItemListCharChar}[ *map-name*]{lang="EN-US"}]{#struct_0_86480_74578_101978005}

[[**[undo attribute-map]{lang="EN-US"}**]{.ItemListCharChar}]{#struct_0_86480_74578_x1371470647}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_754971070}

[[未引用任何]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x2146227830}[属性映射表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1038384244}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_270994565}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1367366947}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1768943731}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1544990173}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1247363763}

[*[map-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1589588132}[：表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1854614078}

[[在使用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1441668771}[授权方案的情况下，可以通过在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案中引用]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表，将]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[授权服务器下发给用户的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射为]{style="font-family:宋体"}[AAA]{lang="EN-US"}[模块可以解析的某类属性。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_2139363066}[方案视图中只能引用一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表，后配置的生效。]{style="font-family:宋体"}

[[如果在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_881818768}[授权过程中修改了引用的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表，或者修改了引用的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表的内容，则该修改对当前的授权过程不会生效，只对修改后新的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[授权过程生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x37252240}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_217443222}[在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案]{style="font-family:宋体"}[test]{lang="EN-US"}[中引用名称为]{style="font-family:宋体"}[map1]{lang="EN-US"}[的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1016795714}

[\[Sysname\] ldap scheme test]{lang="EN-US"}

[\[Sysname-ldap-test\] attribute-map map1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_329671318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap-scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1875643787}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_124415170}
:::

::: {#1709755323 .myid}
[]{#_Toc404792629}[]{#struct_0_86480_74578_x388273559}[]{#_Toc268769812}[]{#_Toc205699735}[]{#_Toc187115167}[]{#_Toc181517528}

**AAA \-- LDAP配置命令 \-- authentication-server**

------------------------------------------------------------------------

[**[authentication-server]{lang="EN-US"}**]{#struct_0_86480_74578_1900138408}[命令用来指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[**[undo authentication-server]{lang="EN-US"}**]{#struct_0_86480_74578_1111329201}[命令用来删除指定的]{style="font-family:
宋体"}[LDAP]{lang="EN-US"}[认证服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x653183611}

[**[authentication-server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_1579390003}

[**[undo authentication-server]{lang="EN-US"}**]{#struct_0_86480_74578_1580217641}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x43199096}

[[未指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1383391986}[认证服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1546972200}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1575855752}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_568610492}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1111394737}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_914020279}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1294174095}

[*[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_1919839805}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。该服务器必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1902103462}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1329937402}[方案视图下仅能指定一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证服务器，如果重复执行此命令，新的配置将覆盖原来的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1795997214}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1473197025}[指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证服务器为]{style="font-family:宋体"}[ccc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1111460273}

[\[Sysname\] ldap scheme ldap1]{lang="EN-US"}

[\[Sysname-ldap-ldap1\] authentication-server ccc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1710949534}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x686541765}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_17348971}
:::

::: {#1863312826 .myid}
[]{#_Toc404792630}[]{#struct_0_86480_74578_171469337}[]{#_Toc391364208}

**AAA \-- LDAP配置命令 \-- authorization-server**

------------------------------------------------------------------------

[**[authorization-server]{lang="EN-US"}**]{#struct_0_86480_74578_x1267292404}[命令用来指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[授权服务器。]{style="font-family:宋体"}

[**[undo authorization-server]{lang="EN-US"}**]{#struct_0_86480_74578_283168674}[命令用来删除指定的]{style="font-family:
宋体"}[LDAP]{lang="EN-US"}[授权服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2107695190}

[**[authorization-server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_2026636783}

[**[undo authorization-server]{lang="EN-US"}**]{#struct_0_86480_74578_x2002960797}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1757642147}

[[未指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1928543124}[授权服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1737553278}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x536311537}[方案视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1152150963}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1046226164}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1460565896}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_634918550}

[*[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1997682657}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。该服务器必须已经存在。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_527765233}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x211677700}[方案视图下仅能指定一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[授权服务器，如果重复执行此命令，新的配置将覆盖原来的配置。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1401309050}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1256768131}[指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[授权服务器为]{style="font-family:宋体"}[ccc]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1993639626}

[\[Sysname\] ldap scheme ldap1]{lang="EN-US"}

[\[Sysname-ldap-ldap1\] authorization-server ccc]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1953906422}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1192531898}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_x1741268437}
:::

::: {#-847418897 .myid}
[]{#_Toc404792631}[]{#struct_0_86480_74578_x962615419}[]{#_Toc268769814}[]{#_Toc205699737}[]{#_Toc187115176}[]{#_Toc181517537}

**AAA \-- LDAP配置命令 \-- display ldap scheme**

------------------------------------------------------------------------

[**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x841652084}[命令用来查看]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案的配置信息。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x995481502}

[**[display ldap scheme]{lang="EN-US"}**[ \[ *scheme-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_632271242}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111525809}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x596024749}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_846002088}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1080257885}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_65787261}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1867259904}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x255339979}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x573169044}

[*[scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_1690626180}[：指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1110542769}

[[如果不指定]{style="font-family:宋体"}]{#struct_0_86480_74578_569514822}[LDAP]{lang="DE"}[方案名]{style="font-family:宋体"}[，]{style="font-family:宋体"}[则显示所有]{style="font-family:宋体"}[LDAP]{lang="DE"}[方案的配置信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x59268429}

[]{#_Toc294201364}[[\# ]{lang="DE"}]{#struct_0_86480_74578_1477769435}[查看所有]{style="font-family:宋体"}[LDAP]{lang="DE"}[方案的配置信息。]{style="font-family:宋体"}

[[\<Sysname\> display ldap scheme]{lang="EN-US"}]{#struct_0_86480_74578_1110608305}

[Total 1 LDAP schemes]{lang="EN-US"}

[ ]{lang="EN-US"}

[\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[LDAP scheme name             : aaa]{lang="EN-US"}

[  Authentication server      : aaa]{lang="EN-US"}

[    IP                       : 1.1.1.1]{lang="EN-US"}

[    Port                     : 111]{lang="EN-US"}

[    VPN instance             : Not configured]{lang="EN-US"}

[    LDAP protocol version    : LDAPv3]{lang="EN-US"}

[    Server timeout interval  : 10 seconds]{lang="EN-US"}

[    Login account DN         : Not configured]{lang="EN-US"}

[    Base DN                  : Not configured]{lang="EN-US"}

[    Search scope             : all-level]{lang="EN-US"}

[    User searching parameters:]{lang="EN-US"}

[      User object class      : Not configured]{lang="EN-US"}

[      Username attribute     : cn]{lang="EN-US"}

[      Username format        : with-domain]{lang="EN-US"}

[  Authorization server       : aaa]{lang="EN-US"}

[    IP                       : 1.1.1.1]{lang="EN-US"}

[    Port                     : 111]{lang="EN-US"}

[    VPN instance             : Not configured]{lang="EN-US"}

[    LDAP protocol version    : LDAPv3]{lang="EN-US"}

[    Server timeout interval  : 10 seconds]{lang="EN-US"}

[    Login account DN         : Not configured]{lang="EN-US"}

[    Base DN                  : Not configured]{lang="EN-US"}

[    Search scope             : all-level]{lang="EN-US"}

[    User searching parameters:]{lang="EN-US"}

[      User object class      : Not configured]{lang="EN-US"}

[      Username attribute     : cn]{lang="EN-US"}

[      Username format        : with-domain]{lang="EN-US"}

[  Attribute map              : map1]{lang="EN-US"}

[ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]{lang="EN-US"}

[[表1-9 ]{lang="EN-US"}[display ldap scheme]{lang="EN-US"}]{#struct_0_86480_74578_x1433359941}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_542512258}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_1425162001}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_1373379831}

[[Total 1 LDAP schemes]{lang="EN-US"}]{#struct_0_86480_74578_289217466}

[[总共有]{style="font-family:宋体"}]{#struct_0_86480_74578_1716592177}[1]{lang="EN-US"}[个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案]{style="font-family:宋体"}

[[LDAP Scheme Name]{lang="EN-US"}]{#struct_0_86480_74578_1111067054}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x237405757}[方案名称]{style="font-family:宋体"}

[[Authentication Server]{lang="EN-US"}]{#struct_0_86480_74578_1970903951}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x559503232}[认证服务器名称]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}]{#struct_0_86480_74578_x1625451367}[Not configured]{lang="EN-US"}

[[Authorization server]{lang="EN-US"}]{#struct_0_86480_74578_1287280120}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1097430962}[授权服务器名字]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}]{#struct_0_86480_74578_x210675673}[Not configured]{lang="EN-US"}

[[IP]{lang="EN-US"}]{#struct_0_86480_74578_183940633}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1111132590}[认证服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址]{style="font-family:宋体"}

[[未配置认证服务器]{style="font-family:宋体"}]{#struct_0_86480_74578_1359551433}[IP]{lang="EN-US"}[时，]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址显示为]{style="font-family:宋体"}[Not configured ]{lang="EN-US"}

[[Port]{lang="EN-US"}]{#struct_0_86480_74578_x1464684590}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x55104875}[认证服务器的端口号]{style="font-family:宋体"}

[[未配置认证服务器]{style="font-family:宋体"}]{#struct_0_86480_74578_x1876650375}[IP]{lang="EN-US"}[时，端口号显示为缺省值]{style="font-family:宋体"}

[[VPN Instance]{lang="EN-US"}]{#struct_0_86480_74578_1111198126}

[[VPN]{lang="EN-US"}]{#struct_0_86480_74578_x672945700}[实例名称]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}]{#struct_0_86480_74578_1312776372}[Not configured]{lang="EN-US"}

[[LDAP Protocol Version]{lang="EN-US"}]{#struct_0_86480_74578_260697601}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1004470102}[协议的版本号（]{style="font-family:宋体"}[LDAPv2]{lang="EN-US"}[、]{style="font-family:宋体"}[LDAPv3]{lang="EN-US"}[）]{style="font-family:宋体"}

[[Server Timeout Interval]{lang="EN-US"}]{#struct_0_86480_74578_1111263662}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1349494680}[服务器连接超时时间（单位为秒）]{style="font-family:宋体"}

[[Login Account DN]{lang="EN-US"}]{#struct_0_86480_74578_x2006683410}

[[管理员用户的]{style="font-family:宋体"}]{#struct_0_86480_74578_x1313743183}[DN]{lang="EN-US"}

[[Base DN]{lang="EN-US"}]{#struct_0_86480_74578_x906955927}

[[用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_86480_74578_1111329198}[查询的起始]{style="font-family:宋体"}[DN]{lang="EN-US"}

[[Search Scope]{lang="EN-US"}]{#struct_0_86480_74578_920204670}

[[用户]{style="font-family:宋体"}]{#struct_0_86480_74578_x1608045912}[DN]{lang="EN-US"}[查询的范围（]{style="font-family:宋体"}[all-level]{lang="EN-US"}[：所有子目录查询，]{style="font-family:宋体"}[single-level]{lang="EN-US"}[：下级目录查询）]{style="font-family:宋体"}

[[User Searching Parameters]{lang="EN-US"}]{#struct_0_86480_74578_407896566}

[[用户查询参数]{style="font-family:宋体"}]{#struct_0_86480_74578_1111394734}

[[User Object Class]{lang="EN-US"}]{#struct_0_86480_74578_913954743}

[[查询用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_86480_74578_2078659790}[时使用的用户对象类型]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}]{#struct_0_86480_74578_x591196338}[Not configured]{lang="EN-US"}

[[Username Attribute]{lang="EN-US"}]{#struct_0_86480_74578_1111460270}

[[用户登录帐号的属性类型]{style="font-family:宋体"}]{#struct_0_86480_74578_1710752926}

[[Username Format]{lang="EN-US"}]{#struct_0_86480_74578_x246277237}

[[发送给服务器的用户名格式]{style="font-family:宋体"}]{#struct_0_86480_74578_x832583262}

[[Attribute map]{lang="EN-US"}]{#struct_0_86480_74578_527830769}

[[引用的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_2093914710}[属性映射表名称]{style="font-family:宋体"}

[[未配置时，显示为]{style="font-family:宋体"}[Not configured]{lang="EN-US"}]{#struct_0_86480_74578_436804942}

[ ]{lang="EN-US"}

::: {#-839206969 .myid}
[]{#_Toc404792632}[]{#struct_0_86480_74578_72832785}[]{#_Toc299047545}[]{#_Toc299112058}[]{#_Toc299130106}[]{#_Toc299130200}[]{#_Toc299047546}[]{#_Toc299112059}[]{#_Toc299130107}[]{#_Toc299130201}

**AAA \-- LDAP配置命令 \-- ip**

------------------------------------------------------------------------

[**[ip]{lang="EN-US"}**]{#struct_0_86480_74578_1111525806}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[undo ip]{lang="EN-US"}**]{#struct_0_86480_74578_x595697069}[命令用来删除配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1746167037}

[**[ip ]{lang="EN-US"}***[ip-address]{lang="EN-US"}***[ ]{lang="EN-US"}**[\[ **port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_629873509}

[**[undo ip]{lang="EN-US"}**]{#struct_0_86480_74578_x123496471}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x407627737}

[[未配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1157910386}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1110542766}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_568531782}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_966509663}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x178901768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x434598333}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1275295925}

[*[ip-address]{lang="EN-US"}*]{#struct_0_86480_74578_x1405920558}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_x1219473209}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器所使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[389]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_633267684}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1110608302}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x1433818693}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[需保证设备上的]{style="font-family:宋体"}]{#struct_0_86480_74578_x451119676}[LDAP]{lang="EN-US"}[服务端口与]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器上使用的端口设置一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[更改后的服务器]{style="font-family:宋体"}]{#struct_0_86480_74578_x2064244162}[IP]{lang="EN-US"}[地址和端口号，只对更改之后进行的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_896813539}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1279150974}[配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址为]{style="font-family:宋体"}[192.168.0.10]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[4300]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x889299275}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] ip 192.168.0.10 port 4300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1121840124}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_1111067055}
:::

::: {#-488313789 .myid}
[]{#_Toc404792633}[]{#struct_0_86480_74578_x237340221}

**AAA \-- LDAP配置命令 \-- ipv6**

------------------------------------------------------------------------

[**[ipv6]{lang="NO-BOK"}**]{#struct_0_86480_74578_1529733684}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="NO-BOK"}[地址。]{style="font-family:宋体"}

[**[undo ipv6]{lang="NO-BOK"}**]{#struct_0_86480_74578_74486103}[命令用来删除配置的]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[服务器]{style="font-family:宋体"}[IPv6]{lang="NO-BOK"}[地址。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1836593997}

[**[ipv6 ]{lang="EN-US"}***[ipv6-address]{lang="EN-US"}*[ \[ **port** *port-number* \] \[ **vpn-instance** *vpn-instance-name* \]]{lang="EN-US"}]{#struct_0_86480_74578_1041795356}

[**[undo ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_x1898584663}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1472090752}

[[缺省情况下，未配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1111132591}[服务器的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1359485897}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1515201139}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_860001343}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x173225768}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1602265176}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_465792950}

[*[ipv6-address]{lang="EN-US"}*]{#struct_0_86480_74578_173162241}[：]{style="font-family:宋体"}[LDAP]{lang="NO-BOK"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="NO-BOK"}[地址。]{style="font-family:宋体"}

[**[port ]{lang="EN-US"}***[port-number]{lang="EN-US"}*]{#struct_0_86480_74578_1012858383}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器所使用的]{style="font-family:宋体"}[TCP]{lang="EN-US"}[端口号，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[，缺省值为]{style="font-family:宋体"}[389]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[vpn-instance]{lang="EN-US"}***[ vpn-instance-name]{lang="EN-US"}*]{#struct_0_86480_74578_1111198127}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器所属的]{style="font-family:宋体"}[VPN]{lang="EN-US"}[。]{style="font-family:宋体"}*[vpn-instance-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[MPLS L3VPN]{lang="EN-US"}[实例的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，区分大小写。不指定该参数时，表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器属于公网。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x673011236}

[[需保证设备上的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1716423938}[服务端口与]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器上使用的端口设置一致。]{style="font-family:宋体"}

[[更改后的服务器]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_2132649682}[地址和端口号，只对更改之后的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_2065381649}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x508773569}[配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[地址为]{style="font-family:宋体"}[1:2::3:4]{lang="EN-US"}[，端口号为]{style="font-family:宋体"}[4300]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x788169493}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] ipv6 1:2::3:4 port 4300]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111263663}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_1349560216}
:::

::: {#-1920735795 .myid}
[]{#struct_0_86480_74578_1287345656}[]{#_Toc404792634}[]{#_Toc391364210}

**AAA \-- LDAP配置命令 \-- ldap attribute-map**

------------------------------------------------------------------------

[**[ldap attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_x1237860711}[命令用来创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[的属性映射表，并进入属性映射表视图。]{style="font-family:宋体"}

[**[undo ldap attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_1072638170}[命令用来删除指定的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x2139582490}

[[**[ldap attribute-map]{lang="EN-US"}**]{.ItemListCharChar}[ *map-name*]{lang="EN-US"}]{#struct_0_86480_74578_x755243161}

[[**[undo ldap attribute-map]{lang="EN-US"}**]{.ItemListCharChar}*[ map-name]{lang="EN-US"}*]{#struct_0_86480_74578_171600409}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1048651895}

[[不存在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1417464627}[属性映射表。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1924464423}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_1027866689}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1562752598}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1054727231}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1579617162}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_284782378}

[*[map-name]{lang="EN-US"}*]{#struct_0_86480_74578_1737684350}[：表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_691225193}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x615288126}[的属性映射表中可以添加多个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表项，每个表项表示一个]{style="font-family:宋体"}[LDAP ]{lang="EN-US"}[属性和一个]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性的映射关系。]{style="font-family:宋体"}

[[可以通过多次执行本命令配置多个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x356288816}[的属性映射表。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x545352002}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1446172714}[添加名称为]{style="font-family:宋体"}[map1]{lang="EN-US"}[的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_150464687}

[\[Sysname\] ldap attribute-map map1]{lang="EN-US"}

[\[Sysname-ldap-map-map1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x866186024}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_x882647967}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1123966209}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[map]{lang="EN-US"}**]{#struct_0_86480_74578_527896305}
:::

::: {#286304851 .myid}
[]{#_Toc404792635}[]{#struct_0_86480_74578_1109607220}[]{#_Toc268769816}[]{#_Toc205699739}[]{#_Toc187115166}[]{#_Toc181517527}

**AAA \-- LDAP配置命令 \-- ldap scheme**

------------------------------------------------------------------------

[**[ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1409253751}[命令用来创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案，并进入]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案视图。]{style="font-family:宋体"}

[**[undo ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_206286740}[命令用来删除指定的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_16873088}

[**[ldap scheme]{lang="DE"}**]{#struct_0_86480_74578_58835680}[ *ldap-scheme-name*]{lang="DE"}

[**[undo ldap scheme]{lang="DE"}**]{#struct_0_86480_74578_x1978285474}[ *ldap-scheme-name*]{lang="DE"}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1118996653}

[[未定义]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1111329199}[方案。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_920270206}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1586341791}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_405805452}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_834026912}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x332630250}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_763093720}

[*[ldap-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_72261292}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1258603311}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1111394735}[方案可以同时被多个]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域引用。]{style="font-family:宋体"}

[[系统最多支持配置]{style="font-family:宋体"}[16]{lang="EN-US"}]{#struct_0_86480_74578_913889207}[个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1486938906}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1742629201}[创建名为]{style="font-family:宋体"}[ldap1]{lang="EN-US"}[的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[方案并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1392793405}

[\[Sysname\] ldap scheme ldap1]{lang="EN-US"}

[\[Sysname-ldap-ldap1\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1450247557}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_630180030}
:::

::: {#1883734081 .myid}
[]{#_Toc268769817}[]{#_Toc205699740}[]{#_Toc187115172}[]{#_Toc181517533}[]{#_Toc404792636}[]{#struct_0_86480_74578_1111460271}[]{#_Toc294201366}

**AAA \-- LDAP配置命令 \-- ldap server**

------------------------------------------------------------------------

[**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_1710818462}[用来创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器并进入]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器视图。]{style="font-family:宋体"}

[**[undo ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_x294409990}[命令用来删除配置的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1429736633}

[**[ldap server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_x479376820}

[**[undo ldap server ]{lang="EN-US"}***[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1758413374}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1367184585}

[[不存在]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x952293871}[服务器。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1111525807}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x595631533}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x168054326}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x228986162}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1589581953}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1299901284}

[*[server-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1285823757}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1511390166}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x2022749449}[创建]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器]{style="font-family:宋体"}[ccc]{lang="EN-US"}[并进入其视图。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1110542767}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\]]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_568597318}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_2139549891}
:::

::: {#151374121 .myid}
[]{#_Toc404792637}[]{#struct_0_86480_74578_1599944945}

**AAA \-- LDAP配置命令 \-- login-dn**

------------------------------------------------------------------------

[**[login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_x2061751819}[命令用来配置具有管理员权限的用户]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_2074101719}[命令用来删除已配置的具有管理员权限的用户]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_438612873}

[**[login-dn ]{lang="EN-US"}***[dn-string]{lang="EN-US"}*]{#struct_0_86480_74578_1286585655}

[**[undo login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_1110608303}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1433753157}

[[未配置具有管理员权限的用户]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_86480_74578_1419150183}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_326632702}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1191672612}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1963954380}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_577173476}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x347474153}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x246530331}

[*[dn-string]{lang="EN-US"}*]{#struct_0_86480_74578_x1617816297}[：具有管理员权限的用户]{style="font-family:宋体"}[DN]{lang="EN-US"}[，是绑定服务器时使用的用户标识名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_2066908410}

[[需要注意的是：]{style="font-family:宋体"}]{#struct_0_86480_74578_x180641495}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[设备上的管理员]{style="font-family:宋体"}]{#struct_0_86480_74578_x540624434}[DN]{lang="EN-US"}[必须与服务器上管理员的]{style="font-family:宋体"}[DN]{lang="EN-US"}[一致。]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;
font-family:Symbol"}[更改后的管理员]{style="font-family:宋体"}]{#struct_0_86480_74578_x396083422}[DN]{lang="EN-US"}[，只对更改之后的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_619366258}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1410486468}[配置管理员权限的用户]{style="font-family:宋体"}[DN]{lang="EN-US"}[为]{style="font-family:宋体"}[uid=test, ou=people, o=example, c=city]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1617750761}

[\[Sysname\] ldap server ldap1]{lang="EN-US"}

[\[Sysname-ldap-server-ldap1\] login-dn uid=test,ou=people,o=example,c=city]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_977992377}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1459406999}
:::

::: {#2056824638 .myid}
[]{#_Toc404792638}[]{#struct_0_86480_74578_2091542770}[]{#_Toc268769818}[]{#_Toc205699741}[]{#_Toc187115173}[]{#_Toc181517534}

**AAA \-- LDAP配置命令 \-- login-password**

------------------------------------------------------------------------

[**[login-password]{lang="EN-US"}**]{#struct_0_86480_74578_204301082}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证中，绑定服务器时所使用的具有管理员权限的用户密码。]{style="font-family:宋体"}

[**[undo login-password]{lang="EN-US"}**]{#struct_0_86480_74578_x1588644009}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1429782181}

[**[login-password]{lang="EN-US"}**[ { **cipher** *\|* **simple** } *password*]{lang="EN-US"}]{#struct_0_86480_74578_x127329107}

[**[undo login-password]{lang="EN-US"}**]{#struct_0_86480_74578_1300503146}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1617685225}

[[未配置具有管理权限的用户密码。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1067652909}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1875134606}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_906364756}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x4087447}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x332602092}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1554369554}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_977556851}

[**[cipher]{lang="EN-US"}**]{#struct_0_86480_74578_x1617619689}[：表示以密文方式设置用户密码。]{style="font-family:宋体"}

[**[simple]{lang="EN-US"}**]{#struct_0_86480_74578_x472397484}[：表示以明文方式设置用户密码。]{style="font-family:宋体"}

[*[string]{lang="EN-US"}*]{#struct_0_86480_74578_x130397907}[：设置的明文密码或密文密码，区分大小写。明文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[128]{lang="EN-US"}[个字符的字符串；密文密码为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[201]{lang="EN-US"}[个字符的字符串。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_1455653985}

[[该命令只有在配置了]{style="font-family:宋体"}**[login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_2064631558}[的情况下生效。当未配置]{style="font-family:宋体"}**[login-dn]{lang="EN-US"}**[时，该命令不生效。]{style="font-family:宋体"}

[[以明文或密文方式设置的用户密码，均以密文的方式保存在配置文件中。]{style="font-family:宋体"}]{#struct_0_86480_74578_673496109}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1923711898}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1711777811}[配置具有管理员权限的用户密码为明文]{style="font-family:宋体"}[abcdefg]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1617554153}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] login-password simple abcdefg]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1622875151}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1235814890}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_2091008430}
:::

::: {#227881117 .myid}
[]{#_Toc404792639}[]{#struct_0_86480_74578_1690761255}[]{#_Toc391364214}[]{#_Toc388895005}

**AAA \-- LDAP配置命令 \-- map**

------------------------------------------------------------------------

[**[map]{lang="EN-US"}**]{#struct_0_86480_74578_x213523541}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表项，即将一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的属性映射为一个]{style="font-family:宋体"}[AAA]{lang="EN-US"}[的属性。]{style="font-family:宋体"}

[**[undo map]{lang="EN-US"}**]{#struct_0_86480_74578_501118129}[命令用来删除指定的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性映射表项。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x824475792}

[**[map ldap-attribute ]{lang="EN-US"}***[ldap-]{lang="EN-US"}[attribute-name]{lang="EN-US"}*[ \[ **prefix** *prefix-value* **delimiter** *delimiter-value* \] **aaa-attribute** { **user-group** \| **user-profile** }]{lang="EN-US"}]{#struct_0_86480_74578_x1038122100}

[**[undo map]{lang="EN-US"}**[ \[ **ldap-attribute** *ldap-*]{lang="EN-US"}*[attribute-name]{lang="EN-US"}*[ \]]{lang="EN-US"}]{#struct_0_86480_74578_512003872}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_509331382}

[[未指定]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1057494531}[属性映射关系。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1250168134}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1553544759}[属性映射表视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x787461844}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1393116792}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1441406627}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x857996675}

[**[ldap-attribute ]{lang="EN-US"}***[ldap-]{lang="EN-US"}[attribute-name]{lang="EN-US"}*]{#struct_0_86480_74578_1959671623}[：表示要映射的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性。其中，]{style="font-family:宋体"}*[ldap-]{lang="EN-US"}[attribute-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[prefix]{lang="EN-US"}**[ *prefix-value* **delimiter** *delimiter-value*]{lang="EN-US"}]{#struct_0_86480_74578_x446648270}[：表示按照一定的格式提取]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性字符串中的内容映射为]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。其中，]{style="font-family:宋体"}*[prefix-value]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性字符串中的某内容前缀（例如]{style="font-family:宋体"}[cn=]{lang="EN-US"}[），为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[7]{lang="EN-US"}[个字符的字符串，不区分大小写；]{style="font-family:
宋体"}*[delimiter-value]{lang="EN-US"}*[表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性字符串中的内容分隔符（例如逗号）。若不指定该可选参数，则表示要将一个完整的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性字符串映射为指定的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[aaa-attribute]{lang="EN-US"}**[ *aaa-attribute-name*]{lang="EN-US"}]{#struct_0_86480_74578_154973801}[：表示要映射为的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。其中，]{style="font-family:宋体"}*[aaa-attribute-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性名称，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[63]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[**[user-group]{lang="EN-US"}**]{#struct_0_86480_74578_935323723}[：表示]{style="font-family:宋体"}[User group]{lang="EN-US"}[类型的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[**[user-profile]{lang="EN-US"}**]{#struct_0_86480_74578_124677314}[：表示]{style="font-family:宋体"}[User Profile]{lang="EN-US"}[类型的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x845033762}

[[在用户的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1081252813}[授权过程中，设备会通过查询操作得到用户的授权信息，该授权信息由]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器通过若干]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性下发给设备。若设备从]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器查询得到某]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性，则该属性只有在被设备的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[模块解析之后才能实际生效。如果某]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器下发给用户的属性不能被]{style="font-family:宋体"}[AAA]{lang="EN-US"}[模块解析，则该属性将被忽略。因此，需要通过本命令指定要获取哪些]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[属性，以及]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器下发的这些属性将被]{style="font-family:宋体"}[AAA]{lang="EN-US"}[模块解析为什么类型的]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性，具体映射为]{style="font-family:宋体"}

[[哪种类型的]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_86480_74578_90148477}[属性由实际应用需求决定。]{style="font-family:宋体"}

[[一个]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_2046257907}[服务器属性只能映射为一个]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性，但不同的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器属性可映射为同一个]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x267194356}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x362417366}[配置将]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器属性]{style="font-family:宋体"}[memberof]{lang="EN-US"}[按照前缀为]{style="font-family:宋体"}[cn=]{lang="EN-US"}[、分隔符为逗号（]{style="font-family:宋体"}[,]{lang="EN-US"}[）的格式提取出的内容映射成]{style="font-family:宋体"}[AAA]{lang="EN-US"}[属性]{style="font-family:宋体"}[User group]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x278607213}

[\[Sysname\] ldap attribute-map ccc]{lang="EN-US"}

[\[Sysname-ldap-map-ccc\] map ldap-attribute memberof prefix cn= delimiter ; aaa-attribute user-group]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1547454919}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap attribute-map]{lang="EN-US"}**]{#struct_0_86480_74578_1143763174}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-group]{lang="EN-US"}**]{#struct_0_86480_74578_x1044721951}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[user-profile]{lang="EN-US"}**]{#struct_0_86480_74578_1816140297}[（安全命令参考]{lang="EN-US" style="font-family:宋体"}[/User Profile]{lang="EN-US"}[）]{lang="EN-US" style="font-family:宋体"}
:::

::: {#146348544 .myid}
[]{#_Toc404792640}[]{#struct_0_86480_74578_x1319131305}[]{#_Toc268769819}[]{#_Toc205699742}[]{#_Toc187115169}[]{#_Toc181517530}

**AAA \-- LDAP配置命令 \-- protocol-version**

------------------------------------------------------------------------

[**[protocol-version]{lang="EN-US"}**]{#struct_0_86480_74578_1508655828}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证中所支持的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议的版本号。]{style="font-family:宋体"}

[**[undo protocol-version]{lang="EN-US"}**]{#struct_0_86480_74578_x1643615572}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1130422858}

[**[protocol-version]{lang="IT"}**]{#struct_0_86480_74578_x96338488}[ { **v2** \| **v3** }]{lang="IT"}

[**[undo protocol-version]{lang="IT"}**]{#struct_0_86480_74578_x1617488617}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1833173095}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x911031886}[版本号为]{style="font-family:宋体"}[LDAPv3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1871404310}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_1560282862}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_2017017157}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1560974012}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1862340714}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1617423081}

[**[v2]{lang="DE"}**]{#struct_0_86480_74578_x1317181901}[：表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议版本号为]{style="font-family:宋体"}[LDAPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[v3]{lang="DE"}**]{#struct_0_86480_74578_782640291}[：表示]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议版本号为]{style="font-family:宋体"}[LDAPv3]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1848704341}

[[为保证]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x498030299}[认证成功，请保证设备上的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[版本号与]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器上使用的版本号一致。]{style="font-family:宋体"}

[[更改后的服务器版本号，只对更改之后的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x254401224}[认证生效。]{style="font-family:宋体"}

[[Microsoft]{lang="EN-US"}]{#struct_0_86480_74578_1770683888}[的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器只支持]{style="font-family:宋体"}[LDAPv3]{lang="EN-US"}[，配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[版本为]{style="font-family:宋体"}[v2]{lang="EN-US"}[时无效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_489859431}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_924194360}[配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[协议版本号为]{style="font-family:宋体"}[LDAPv2]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1617357545}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] protocol-version v2]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x580399837}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1959914392}
:::

::: {#-1379509060 .myid}
[]{#_Toc205699743}[]{#_Toc187115171}[]{#_Toc181517532}[]{#_Toc404792641}[]{#struct_0_86480_74578_1259504356}[]{#_Toc294201370}

**AAA \-- LDAP配置命令 \-- search-base-dn**

------------------------------------------------------------------------

[**[search-base-dn]{lang="EN-US"}**]{#struct_0_86480_74578_x2044964353}[命令用来配置用户查询的起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo search-base-dn]{lang="EN-US"}**]{#struct_0_86480_74578_x253931335}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x49906094}

[**[search-base-dn ]{lang="EN-US"}***[base-dn]{lang="EN-US"}*]{#struct_0_86480_74578_x1618340585}

[**[undo search-base-dn]{lang="EN-US"}**]{#struct_0_86480_74578_509322265}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x718381392}

[[未指定用户查询的起始]{style="font-family:宋体"}[DN]{lang="EN-US"}]{#struct_0_86480_74578_766795191}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1693953992}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_478083515}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_164341768}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x864682926}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1618275049}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1736486889}

[*[base-dn]{lang="EN-US"}*]{#struct_0_86480_74578_x2033767576}[：表示查询待认证用户的起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[。]{style="font-family:宋体"}*[base-dn]{lang="EN-US"}*[表示起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[的值，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[255]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_419754635}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1174655738}[配置用户查询的起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[为]{style="font-family:宋体"}[dc=ldap,dc=com]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1712305575}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] search-base-dn dc=ldap,dc=com]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1558799129}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_1043879146}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_x1617816296}
:::

::: {#-247023584 .myid}
[]{#_Toc404792642}[]{#struct_0_86480_74578_x661974945}[]{#_Toc294201371}[]{#_Toc299047554}[]{#_Toc299112067}[]{#_Toc299130115}[]{#_Toc299130209}

**AAA \-- LDAP配置命令 \-- search-scope**

------------------------------------------------------------------------

[**[search-scope]{lang="EN-US"}**]{#struct_0_86480_74578_1726673936}[命令用来配置用户查询的范围。]{style="font-family:宋体"}

[**[undo search-scope]{lang="EN-US"}**]{#struct_0_86480_74578_x273772179}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x362091561}

[**[search-scope ]{lang="EN-US"}**[{ **all-level** \| **single-level** }]{lang="EN-US"}]{#struct_0_86480_74578_x1490905863}

[**[undo search-scope]{lang="EN-US"}**]{#struct_0_86480_74578_645214126}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_2130088594}

[[用户查询的范围为]{style="font-family:宋体"}**[all-level]{lang="EN-US"}**]{#struct_0_86480_74578_x2115392149}[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1617750760}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1750890978}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_1009109699}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_47201591}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x121094926}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2119511562}

[**[all-level]{lang="EN-US"}**]{#struct_0_86480_74578_1190691886}[：表示在起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[的所有子目录下进行查询。]{style="font-family:宋体"}

[**[single-level]{lang="EN-US"}**]{#struct_0_86480_74578_x1178541096}[：表示只在起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[的下一级子目录下进行查询。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x305650321}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1617685224}[配置在起始]{style="font-family:宋体"}[DN]{lang="EN-US"}[的所有子目录下查询]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[认证用户。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1661230446}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] search-scope all-level]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1798613999}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_686610733}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ldap server]{lang="EN-US"}**]{#struct_0_86480_74578_257844768}
:::

::: {#1057524222 .myid}
[]{#_Toc404792643}[]{#struct_0_86480_74578_435712008}[]{#_Toc294201372}[]{#_Toc299047556}[]{#_Toc299112069}[]{#_Toc299130117}[]{#_Toc299130211}

**AAA \-- LDAP配置命令 \-- server-timeout**

------------------------------------------------------------------------

[**[server-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_1421217717}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器连接超时时间，即认证、授权时等待]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器回应的最大时间。]{style="font-family:宋体"}

[**[undo server-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_x1485717626}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1617619688}

[**[server-timeout]{lang="EN-US"}**[ *time-interval*]{lang="EN-US"}]{#struct_0_86480_74578_1093686457}

[**[undo server-timeout]{lang="EN-US"}**]{#struct_0_86480_74578_1979793820}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1929729725}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x71321489}[服务器连接超时时间为]{style="font-family:宋体"}[10]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1963238495}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_360034093}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x158852345}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1617554152}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x56791210}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1481504034}

[*[time-interval]{lang="EN-US"}*]{#struct_0_86480_74578_13929960}[：]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器连接超时时间，取值范围为]{style="font-family:宋体"}[5]{lang="EN-US"}[～]{style="font-family:宋体"}[20]{lang="EN-US"}[，单位为秒。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_34615839}

[[更改后的连接超时时间，只对更改之后的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x996367965}[认证生效。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x654009755}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_649208286}[配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器连接超时时间为]{style="font-family:宋体"}[15]{lang="EN-US"}[秒。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x1617488616}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] server-timeout 15]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_895710260}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x239774333}
:::

::: {#306216520 .myid}
[]{#_Toc404792644}[]{#struct_0_86480_74578_x1769205683}[]{#_Toc294201373}[]{#_Toc205699745}[]{#_Toc187115174}[]{#_Toc181517535}

**AAA \-- LDAP配置命令 \-- user-parameters**

------------------------------------------------------------------------

[**[user-parameters]{lang="EN-US"}**]{#struct_0_86480_74578_x1242710811}[命令用来配置]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[用户查询的属性参数，包括用户名属性、用户名格式和自定义用户对象类型。]{style="font-family:宋体"}

[**[undo user-parameters]{lang="EN-US"}**]{#struct_0_86480_74578_517689333}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1637390135}

[**[user-parameters ]{lang="EN-US"}**[{ **user-name-attribute** { *name-attribute* \| **cn** \| **uid** } \| **user-name-format** { **with-domain** \| **without-domain** } \| **user-object-class** *object-class-name* }]{lang="EN-US"}]{#struct_0_86480_74578_x720759494}

[**[undo user-parameters ]{lang="EN-US"}**[{ **user-name-attribute** \| **user-name-format** \| **user-object-class** }]{lang="EN-US"}]{#struct_0_86480_74578_841489140}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1617423080}

[**[user-name-attribute]{lang="EN-US"}**]{#struct_0_86480_74578_1411701454}[为]{style="font-family:宋体"}**[cn]{lang="EN-US"}**[；]{style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[为]{style="font-family:宋体"}**[without-domain]{lang="EN-US"}**[；未指定自定义]{style="font-family:宋体"}**[user-object-class]{lang="EN-US"}**[，根据使用的]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器的类型使用各服务器缺省的用户对象类型。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_2058194990}

[[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_x1176615478}[服务器视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1305288788}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x745057128}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_754829668}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x566989197}

[**[user-name-attribute ]{lang="EN-US"}**[{ *name-attribute* \| **cn** \| **uid** }]{lang="EN-US"}]{#struct_0_86480_74578_x1617357544}[：表示用户名的属性类型。其中，]{style="font-family:宋体"}*[name-attribute]{lang="EN-US"}*[表示属性类型值，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写；]{style="font-family:宋体"}**[cn]{lang="EN-US"}**[表示用户登录帐号的属性为]{style="font-family:宋体"}[cn]{lang="EN-US"}[（]{style="font-family:宋体"}[Common Name]{lang="EN-US"}[）；]{style="font-family:宋体"}**[uid]{lang="EN-US"}**[表示用户登录帐号的属性为]{style="font-family:宋体"}[uid]{lang="EN-US"}[（]{style="font-family:宋体"}[User ID]{lang="EN-US"}[）。]{style="font-family:宋体"}

[**[user-name-format]{lang="EN-US"}**[ { **with-domain** \| **without-domain** }]{lang="EN-US"}]{#struct_0_86480_74578_985684104}[：表示发送给服务器的用户名格式。其中，]{style="font-family:宋体"}**[with-domain]{lang="EN-US"}**[表示发送给服务器的用户名带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名；]{style="font-family:宋体"}**[without-domain]{lang="EN-US"}**[表示发送给服务器的用户名不带]{style="font-family:宋体"}[ISP]{lang="EN-US"}[域名。]{style="font-family:宋体"}

[**[user-object-class ]{lang="EN-US"}***[object-class-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1241723126}[：表示查询用户]{style="font-family:宋体"}[DN]{lang="EN-US"}[时使用的用户对象类型。其中，]{style="font-family:宋体"}*[object-class-name]{lang="EN-US"}*[表示对象类型值，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[64]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1579976609}

[[如果]{style="font-family:宋体"}[LDAP]{lang="EN-US"}]{#struct_0_86480_74578_931086826}[服务器上的用户名不包含域名，必须配置]{style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[为]{style="font-family:宋体"}**[without-domain]{lang="EN-US"}**[，将用户名的域名去除后再传送给]{style="font-family:宋体"}[LDAP]{lang="EN-US"}[服务器；如果包含域名则需配置]{style="font-family:宋体"}**[user-name-format]{lang="EN-US"}**[为]{style="font-family:宋体"}**[with-domain]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_381077651}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x311892483}[配置用户对象类型为]{style="font-family:宋体"}[person]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x759240205}

[\[Sysname\] ldap server ccc]{lang="EN-US"}

[\[Sysname-ldap-server-ccc\] user-parameters user-object-class person]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1618340584}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[display ldap scheme]{lang="EN-US"}**]{#struct_0_86480_74578_x1056761676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[login-dn]{lang="EN-US"}**]{#struct_0_86480_74578_1977802506}
:::

::: {#-966553539 .myid}
[]{#_Toc404792646}[]{#struct_0_86480_74578_x1741988916}[]{#_Toc362533103}

**AAA \-- 本地话单缓存配置命令 \-- display local-bill**

------------------------------------------------------------------------

[**[display local-bill]{lang="EN-US"}**]{#struct_0_86480_74578_x1742054452}[命令用来显示缓存中指定的具体话单信息或者缓存中话单资源的使用情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1742119988}

[**[display local-bill ]{lang="EN-US"}**[{ **cache-usage** \| **verbose** *start-number* **count** *count* }]{lang="EN-US"}]{#struct_0_86480_74578_x1741202484}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741661237}

[[任意视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x1741726773}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741857845}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1741923381}

[[network-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1741988917}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1742054453}

[[mdc-operator]{lang="EN-US"}]{#struct_0_86480_74578_x1742119989}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741136949}

[**[cache-usage]{lang="EN-US"}**]{#struct_0_86480_74578_1742667824}[：查看本地缓存中话单资源的使用情况。]{style="font-family:宋体"}

[**[verbose]{lang="EN-US"}**]{#struct_0_86480_74578_506264714}[：查看本地缓存中的具体话单信息。]{style="font-family:宋体"}

[*[start-number]{lang="EN-US"}*]{#struct_0_86480_74578_x1741202485}[：指定显示话单的起始位置，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[50000]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[count]{lang="EN-US"}***[ count]{lang="EN-US"}*]{#struct_0_86480_74578_x1741661238}[：连续显示的话单总数目，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[100]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741857846}

[[查看本地缓存中的具体话单信息时，需要指定开始显示话单的位置]{style="font-family:宋体"}*[start-number]{lang="EN-US"}*]{#struct_0_86480_74578_x1741923382}[，即从第几个话单开始显示，以及从这个位置开始总共连续显示多少个话单数目。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741988918}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x1742054454}[从本地缓存的第一个话单开始显示连续]{style="font-family:宋体"}[2]{lang="EN-US"}[个话单的详细信息。]{style="font-family:宋体"}

[[\<Sysname\> display local-bill verbose 1 count 2]{lang="EN-US"}]{#struct_0_86480_74578_x1741136950}

[Bill 1 details: ]{lang="EN-US"}

[  Session ID  : 000000012013-05-21:18:04:02-12345678011]{lang="EN-US"}

[  User name   : user1@h3c]{lang="EN-US"}

[  Start time  : 2013-05-21 18:04:10]{lang="EN-US"}

[  Stop time   : 2013-05-21 18:05:35    Duration   : 0:01:35]{lang="EN-US"}

[  IP address  : 111.8.10.125           MAC address: 0016-ecb7-a879]{lang="EN-US"}

[  IPv6 address: N/A]{lang="EN-US"}

[  Service type: PPP                    Access type: PPP]{lang="EN-US"}

[  Interface   : Ethernet 1/1]{lang="EN-US"}

[  VLAN ID     : N/A]{lang="EN-US"}

[  Status      : Offline                Reason code: 6  Ref: 98]{lang="EN-US"}

[  User traffic: ]{lang="EN-US"}

[    Received: 0            bytes, 0            packets]{lang="EN-US"}

[    Sent    : 0            bytes, 0            packets]{lang="EN-US"}

[ ]{lang="EN-US"}

[Bill 2 details: ]{lang="EN-US"}

[Session ID  : 000000012013-05-21:18:14:07-12341234011]{lang="EN-US"}

[User name   : user2]{lang="EN-US"}

[Start time  : 2013-05-21 18:14:15]{lang="EN-US"}

[Stop time   : 2013-05-21 18:15:35    Duration   : 0:01:20]{lang="EN-US"}

[IP address  : 111.8.10.124           MAC address: 0016-ec89-a8e9]{lang="EN-US"}

[IPv6 address: N/A]{lang="EN-US"}

[Service type: PPP                    Access type: PPP]{lang="EN-US"}

[Interface   : Ethernet 1/2]{lang="EN-US"}

[VLAN ID     : 100]{lang="EN-US"}

[Status      : Offline                Reason code: 6  Ref: 98]{lang="EN-US"}

[User traffic: ]{lang="EN-US"}

[    Received: 0            bytes, 0            packets]{lang="EN-US"}

[    Sent    : 0            bytes, 0            packets]{lang="EN-US"}

[ ]{lang="EN-US"}

[Total bills: 2.]{lang="EN-US"}

[[表1-10 ]{lang="EN-US"}[display local-bill verbose]{lang="EN-US"}]{#struct_0_86480_74578_x1741202486}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x644732691}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741726767}
:::

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_x1741857839}

[[Bill 1 details]{lang="EN-US"}]{#struct_0_86480_74578_x1741988911}

[[第]{style="font-family:宋体"}[n]{lang="EN-US"}]{#struct_0_86480_74578_x1742119983}[个话单的详细内容]{style="font-family:宋体"}

[[Session ID]{lang="EN-US"}]{#struct_0_86480_74578_x1741202479}

[[会话]{style="font-family:宋体"}[ID]{lang="EN-US"}]{#struct_0_86480_74578_x1741726768}[，用户的唯一标识]{style="font-family:宋体"}

[[User name]{lang="EN-US"}]{#struct_0_86480_74578_x1741857840}

[[用户名称]{style="font-family:宋体"}]{#struct_0_86480_74578_x1741988912}

[[Start time]{lang="EN-US"}]{#struct_0_86480_74578_x1742119984}

[[开始计费时间]{style="font-family:宋体"}]{#struct_0_86480_74578_x1741202480}

[[Stop time]{lang="EN-US"}]{#struct_0_86480_74578_x175642830}

[[停止计费时间]{style="font-family:宋体"}]{#struct_0_86480_74578_x175773902}

[[Duration]{lang="EN-US"}]{#struct_0_86480_74578_x175904974}

[[用户在线时长]{style="font-family:宋体"}]{#struct_0_86480_74578_x176036046}

[[IP address]{lang="EN-US"}]{#struct_0_86480_74578_x175118542}

[[用户]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_x175642831}[地址]{style="font-family:宋体"}

[[MAC address]{lang="EN-US"}]{#struct_0_86480_74578_x175773903}

[[用户]{style="font-family:宋体"}[MAC]{lang="EN-US"}]{#struct_0_86480_74578_x175904975}[地址]{style="font-family:宋体"}

[[IPv6 address]{lang="EN-US"}]{#struct_0_86480_74578_x176036047}

[[用户]{style="font-family:宋体"}[IPv6]{lang="EN-US"}]{#struct_0_86480_74578_x175118543}[地址]{style="font-family:宋体"}

[[Service type]{lang="EN-US"}]{#struct_0_86480_74578_x175642832}

[[用户使用的服务类型]{style="font-family:宋体"}]{#struct_0_86480_74578_x175773904}

[[Access type]{lang="EN-US"}]{#struct_0_86480_74578_x175904976}

[[用户使用的接入类型]{style="font-family:宋体"}]{#struct_0_86480_74578_x176036048}

[[Interface]{lang="EN-US"}]{#struct_0_86480_74578_x175118544}

[[用户接入到设备的端口号]{style="font-family:宋体"}]{#struct_0_86480_74578_x175642833}

[[VLAN ID]{lang="EN-US"}]{#struct_0_86480_74578_x175773905}

[[用户接入的]{style="font-family:宋体"}[VLAN]{lang="EN-US"}]{#struct_0_86480_74578_x175904977}

[[Status]{lang="EN-US"}]{#struct_0_86480_74578_x176036049}

[[话单类型。目前只支持本地话单缓存，是在用户下线后才产生的话单]{style="font-family:宋体"}]{#struct_0_86480_74578_x175118545}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Invalid]{lang="EN-US"}]{#struct_0_86480_74578_x175642826}[：无效]{lang="EN-US" style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Realtime]{lang="EN-US"}]{#struct_0_86480_74578_x175773898}[：实时计费话单]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[Offline]{lang="EN-US"}]{#struct_0_86480_74578_x175904970}[：下线话单]{style="font-family:宋体"}

[[·[       ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[CRC Failed]{lang="EN-US"}]{#struct_0_86480_74578_x176036042}[：错误话单，即]{style="font-family:宋体"}[CRC]{lang="EN-US"}[校验错误的话单]{style="font-family:宋体"}

[[Code]{lang="EN-US"}]{#struct_0_86480_74578_x175118538}

[[设备外部的下线原因代码。为按照]{style="font-family:宋体"}[RFC 2866]{lang="EN-US"}]{#struct_0_86480_74578_x175642827}[远端计费提供的标准下线原因，具体请参考]{style="font-family:宋体"}[RFC 2866]{lang="EN-US"}

[[Ref]{lang="EN-US"}]{#struct_0_86480_74578_x175839435}

[[设备内部的下线原因代码，作为外部下线原因的补充，提供更加详细的原因，一般无需使用]{style="font-family:宋体"}]{#struct_0_86480_74578_x175970507}

[[User traffic]{lang="EN-US"}]{#struct_0_86480_74578_x175053003}

[[用户流量统计信息，包括上行字节数、上行包数、下行字节数、下行包数]{style="font-family:宋体"}]{#struct_0_86480_74578_x578861821}

[[Received]{lang="EN-US"}]{#struct_0_86480_74578_x578992893}

[[下行流量，即用户收到报文的流量]{style="font-family:宋体"}]{#struct_0_86480_74578_x579123965}

[[Sent]{lang="EN-US"}]{#struct_0_86480_74578_x579255037}

[[上行流量，即用户发送出去的流量]{style="font-family:宋体"}]{#struct_0_86480_74578_x578337533}

[[Total bills]{lang="EN-US"}]{#struct_0_86480_74578_x578861822}

[[当前显示的话单总数]{style="font-family:宋体"}]{#struct_0_86480_74578_x578927358}

[ ]{lang="EN-US"}

[[\#]{lang="EN-US"}]{#struct_0_86480_74578_x578992894}[显示本地缓存中的话单资源的使用情况。]{style="font-family:宋体"}

[[\<Sysname\> display local-bill cache-usage]{lang="EN-US"}]{#struct_0_86480_74578_x579123966}

[Cache usage:]{lang="EN-US"}

[  Existing bills: 0         Available bills      : 50000]{lang="EN-US"}

[  Max bills     : 50000     Auto export threshold: 4000]{lang="EN-US"}

[  Bytes per bill: 448]{lang="EN-US"}

[[表1-11 ]{lang="EN-US"}[display local-bill cache-usage]{lang="EN-US"}]{#struct_0_86480_74578_x579189502}[命令显示信息描述表]{style="font-family:黑体"}

[]{#table_struct_0_x610294267}[[字段]{style="font-family:黑体"}]{#struct_0_86480_74578_x579320574}

[[描述]{style="font-family:黑体"}]{#struct_0_86480_74578_x578403070}

[[Cache usage]{lang="EN-US"}]{#struct_0_86480_74578_x578927359}

[[缓存的使用情况]{style="font-family:宋体"}]{#struct_0_86480_74578_x579058431}

[[Existing bills]{lang="EN-US"}]{#struct_0_86480_74578_x579189503}

[[当前缓存中已保存的话单数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x579320575}

[[Available bills]{lang="EN-US"}]{#struct_0_86480_74578_x578403071}

[[当前缓存中还可以保存的话单数目]{style="font-family:宋体"}]{#struct_0_86480_74578_x578927360}

[[Max bills]{lang="EN-US"}]{#struct_0_86480_74578_x579058432}

[[当前缓存中可保存的话单总数]{style="font-family:宋体"}]{#struct_0_86480_74578_x579189504}

[[Auto export threshold]{lang="EN-US"}]{#struct_0_86480_74578_x579320576}

[[自动上传阈值，取值为触发自动上传的话单数]{style="font-family:宋体"}]{#struct_0_86480_74578_x578403072}

[[Bytes per bill]{lang="EN-US"}]{#struct_0_86480_74578_x578927353}

[[缓存中每个话单的存储空间大小]{style="font-family:宋体"}]{#struct_0_86480_74578_x579058425} [（单位：字节）]{style="font-family:
  宋体"}

[ ]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x579123961}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_x579189497}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export]{lang="EN-US"}**]{#struct_0_86480_74578_1338465796}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_1961676183}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_x579255033}

::: {#248205670 .myid}
[]{#_Toc404792647}[]{#struct_0_86480_74578_x578403065}[]{#_Toc362533095}

**AAA \-- 本地话单缓存配置命令 \-- local-bill enable**

------------------------------------------------------------------------

[**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_x578861818}[命令用来使能本地话单缓存功能。]{style="font-family:宋体"}

[**[undo local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_x578927354}[用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x578992890}

[**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_x579058426}

[**[undo local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_x579123962}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x579189498}

[[本地话单缓存功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_86480_74578_x579255034}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x579320570}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x578337530}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x578403066}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_987222120}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_987156584}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_987091048}

[[使能本地话单缓存功能后，当]{style="font-family:宋体"}[AAA]{lang="EN-US"}]{#struct_0_86480_74578_987025512}[服务器不能提供计费服务时（例如计费服务器不可达时），接入设备将用户计费停止时产生的话单保存在本地。本地话单缓存功能处于使能状态的情况下，可以通过配置指定本地自动定期将缓存的话单上传到指定的服务器上，或手动上传到指定服务器上。]{style="font-family:宋体"}

[[本功能可以支持对]{style="font-family:宋体"}[lan-access]{lang="EN-US"}]{#struct_0_86480_74578_986959976}[、]{style="font-family:宋体"}[Portal]{lang="EN-US"}[、]{style="font-family:宋体"}[PPP]{lang="EN-US"}[、和]{style="font-family:宋体"}[IPoE]{lang="EN-US"}[用户进行本地话单缓存。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_986894440}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_986828904}[使能本地话单缓存功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_986763368}

[\[Sysname\] local-bill enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_987746408}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_987680872}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_987222119}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export]{lang="EN-US"}**]{#struct_0_86480_74578_987156583}
:::

::: {#844125014 .myid}
[]{#_Toc404792648}[]{#struct_0_86480_74578_987091047}[]{#_Toc362533101}

**AAA \-- 本地话单缓存配置命令 \-- local-bill export**

------------------------------------------------------------------------

[**[local-bill export]{lang="EN-US"}**]{#struct_0_86480_74578_987025511}[命令用来执行话单手动上传。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_986959975}

[**[local-bill export ]{lang="EN-US"}**[\[ *url* \] \[ **clear-cache** \]]{lang="EN-US"}]{#struct_0_86480_74578_986894439}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_986828903}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_986763367}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_987746407}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_987680871}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_987222118}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_987156582}

[*[url]{lang="EN-US"}*]{#struct_0_86480_74578_987091046}[：手动上传话单的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串。若不指定该参数，则会将本地缓存的话单上传到]{style="font-family:宋体"}**[local-bill export-url]{lang="EN-US"}**[命令指定的路径上。]{style="font-family:宋体"}

[**[clear-cache]{lang="EN-US"}**]{#struct_0_86480_74578_987025510}[：手动上传话单后，清除本地缓存的话单信息。若不指定该参数，则表示手动上传话单后，不清除本地缓存的话单信息。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_986959974}

[[本地话单缓存功能处于使能状态的情况下，通过本命令可立即将本地缓存的话单上传到指定的路径上，该路径可以是本命令中通过]{style="font-family:宋体"}*[url]{lang="EN-US"}*]{#struct_0_86480_74578_986894438}[参数指定，如果本命令中未指定]{style="font-family:宋体"}*[url]{lang="EN-US"}*[参数，则使用]{style="font-family:宋体"}**[local-bill export-url]{lang="EN-US"}**[命令指定的]{style="font-family:宋体"}*[url]{lang="EN-US"}*[参数。]{style="font-family:宋体"}

[[具体上传]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_332952783}[格式要求如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFTP]{lang="EN-US"}]{#struct_0_86480_74578_x201869525}[协议]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[格式：]{lang="EN-US" style="font-family:宋体"}[tftp://*path*]{lang="EN-US"}[，例如]{lang="EN-US" style="font-family:宋体"}[tftp://1.1.1.1/lbill]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP]{lang="EN-US"}]{#struct_0_86480_74578_72944475}[协议]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[携带用户名和密码的格式为]{lang="EN-US" style="font-family:宋体"}[ftp://*username*:*password*@*server*/*path*]{lang="EN-US"}]{#struct_0_86480_74578_683523265}[，例如]{lang="EN-US" style="font-family:宋体"}[ftp://1:1@1.1.1.1/lbill]{lang="EN-US"}[。其中，]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[用户名，]{lang="EN-US" style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[认证密码*，*]{lang="EN-US" style="font-family:宋体"}*[server]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址或主机名。如果]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[用户名中携带域名，则该域名会被设备忽略，例如]{lang="EN-US" style="font-family:宋体"}[ftp://1@]{lang="EN-US"}[abc]{lang="EN-US"}[:1@1.1.1.1/lbill]{lang="EN-US"}[将被当作]{lang="EN-US" style="font-family:宋体"}[ftp://1:1@1.1.1.1/lbill]{lang="EN-US"}[处理]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[不需要携带用户名和密码的格式为]{lang="EN-US" style="font-family:宋体"}[ftp://*path*]{lang="EN-US"}]{#struct_0_86480_74578_307028111}[，例如]{lang="EN-US" style="font-family:
宋体"}[ftp://1.1.1.1/lbill]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[本命令为一次性执行命令，所有参数仅对本次手动上传有效。]{style="font-family:宋体"}]{#struct_0_86480_74578_986828902}

[[通常情况下，使用话单自动上传功能即可，在自动上传路径不可达（例如存储话单的服务器故障）、有临时审计、数据分析等需求的情况下，可通过本命令进行手工上传话单，为避免]{style="font-family:宋体"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_986763366}[命令指定的上传]{style="font-family:宋体"}[URL]{lang="EN-US"}[不可达造成话单上传失败问题，可通过]{style="font-family:宋体"}*[url]{lang="EN-US"}*[参数指定一个其它的上传]{style="font-family:宋体"}[URL]{lang="EN-US"}[。]{style="font-family:宋体"}

[[在上传的话单用于计费或审计等用途的情况下，建议执行话单手动上传的同时，指定]{style="font-family:宋体"}**[clear-cache]{lang="EN-US"}**]{#struct_0_86480_74578_987746406}[参数清除本地缓存的话单信息；在上传的话单用于数据分析、故障排除等用途的情况下，建议执行话单手工上传的同时，不要指定]{style="font-family:宋体"}**[clear-cache]{lang="EN-US"}**[参数，保留本地缓存的话单信息用于正常的话单上传。]{style="font-family:宋体"}

[[手动上传操作仅能同时在一个用户线上执行。某用户线上的用户执行了该操作后，系统需要一定的时间进行上传，在此期间，该用户线上的用户必须等待上传结果，不能执行命令行操作，且正在进行的自动上传也会暂停等待。同时，其它用户线上的用户执行手动上传话单命令时，系统会提示当前正在处理手动上传话单不能执行本次命令。]{style="font-family:宋体"}]{#struct_0_86480_74578_987680870}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_987222117}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_987156581}[将本地缓存话单手动上传到]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[tftp://10.10.10.10/tftp]{lang="EN-US"}[的服务器上，并在上传后清除缓存的话单信息。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_987091045}

[\[Sysname\] local-bill export tftp://10.10.10.10/tftp clear-cache]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_987025509}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_986959973}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_1338793477}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_986894437}
:::

::: {#-982817283 .myid}
[]{#_Toc404792649}[]{#struct_0_86480_74578_986763365}[]{#_Toc362533099}

**AAA \-- 本地话单缓存配置命令 \-- local-bill export-interval**

------------------------------------------------------------------------

[**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_987746405}[命令用来配置话单自动上传的周期。]{style="font-family:
宋体"}

[**[undo local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_987680869}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_987222124}

[**[local-bill export-interval ]{lang="EN-US"}***[interval]{lang="EN-US"}*]{#struct_0_86480_74578_987156588}

[**[undo local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_987091052}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_987025516}

[[自动上传话单的周期为]{style="font-family:宋体"}[1440]{lang="EN-US"}]{#struct_0_86480_74578_986959980}[分钟。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_986894444}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_986828908}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_986763372}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_987680876}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_987222123}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_987156587}

[*[interval]{lang="EN-US"}*]{#struct_0_86480_74578_987091051}[：话单自动上传的周期，单位为分钟，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[65535]{lang="EN-US"}[。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_987025515}

[[本地话单缓存功能处于使能状态的情况下，系统将以本命令指定的周期向指定路径上进行话单上传。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1955942235}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_986959979}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_986894443}[配置本地缓存话单自动上传的周期为]{style="font-family:宋体"}[100]{lang="EN-US"}[分钟。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_986828907}

[\[Sysname\] local-bill export-interval 100]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_986763371}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_987746411}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_987680875}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export]{lang="EN-US"}**]{#struct_0_86480_74578_583937593}
:::

::: {#-1979243063 .myid}
[]{#_Toc404792650}[]{#struct_0_86480_74578_583872057}[]{#_Toc362533097}

**AAA \-- 本地话单缓存配置命令 \-- local-bill export-url**

------------------------------------------------------------------------

[**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_583806521}[命令用来配置对本地缓存话单进行上传的]{style="font-family:宋体"}[URL ]{lang="EN-US"}[。]{style="font-family:宋体"}

[**[undo local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_583740985}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_583675449}

[**[local-bill export-url ]{lang="EN-US"}***[url]{lang="EN-US"}*]{#struct_0_86480_74578_583609913}

[**[undo local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_583478841}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_584461881}

[[未指定对话单上传的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_584396345}[，对缓存话单的自动上传会失败。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_583937592}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_583872056}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_583806520}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_583740984}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_583675448}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_583609912}

[*[url]{lang="EN-US"}*]{#struct_0_86480_74578_583544376}[：对本地缓存话单进行上传的]{style="font-family:宋体"}[URL]{lang="EN-US"}[，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[256]{lang="EN-US"}[个字符的字符串。该路径必须是可存储文件的路径。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_583478840}

[[本地话单缓存功能处于使能状态的情况下，指定合法的上传话单的]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_584461880}[后，系统将定期向该指定路径上进行话单上传，或当本地缓存话单数目达到系统设定的阈值时，系统也会自动向该指定路径上进行话单上传。上传的话单将以文本格式保存在指定路径中供计费、审校或分析。上传方式包括]{style="font-family:宋体"}[TFTP]{lang="EN-US"}[和]{style="font-family:宋体"}[FTP]{lang="EN-US"}[。每次话单信息上传完成之后，系统将自动清除当前本地话单缓存中的所有话单信息。]{style="font-family:宋体"}

[[具体上传]{style="font-family:宋体"}[URL]{lang="EN-US"}]{#struct_0_86480_74578_332100814}[格式要求如下：]{style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[TFTP]{lang="EN-US"}]{#struct_0_86480_74578_1913114674}[协议]{lang="EN-US" style="font-family:宋体"}[URL]{lang="EN-US"}[格式：]{lang="EN-US" style="font-family:宋体"}[tftp://*path*]{lang="EN-US"}[，例如]{lang="EN-US" style="font-family:宋体"}[tftp://1.1.1.1/lbill]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}[FTP]{lang="EN-US"}]{#struct_0_86480_74578_511235957}[协议]{style="font-family:宋体"}[URL]{lang="EN-US"}[格式：]{style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[携带用户名和密码的格式为]{lang="EN-US" style="font-family:宋体"}[ftp://*username*:*password*@*server*/*path*]{lang="EN-US"}]{#struct_0_86480_74578_3875976}[，例如]{lang="EN-US" style="font-family:宋体"}[ftp://1:1@1.1.1.1/lbill]{lang="EN-US"}[。其中，]{lang="EN-US" style="font-family:宋体"}*[username]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[用户名，]{lang="EN-US" style="font-family:宋体"}*[password]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[认证密码*，*]{lang="EN-US" style="font-family:宋体"}*[server]{lang="EN-US"}*[为]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[服务器]{lang="EN-US" style="font-family:宋体"}[IP]{lang="EN-US"}[地址或主机名。如果]{lang="EN-US" style="font-family:宋体"}[FTP]{lang="EN-US"}[用户名中携带域名，则该域名会被设备忽略，例如]{lang="EN-US" style="font-family:宋体"}[ftp://1@]{lang="EN-US"}[abc]{lang="EN-US"}[:1@1.1.1.1/lbill]{lang="EN-US"}[将被当作]{lang="EN-US" style="font-family:宋体"}[ftp://1:1@1.1.1.1/lbill]{lang="EN-US"}[处理]{style="font-family:宋体"}[。]{lang="EN-US" style="font-family:宋体"}

[[¡[  ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:6.0pt;font-family:Wingdings"}[不需要携带用户名和密码的格式为]{lang="EN-US" style="font-family:宋体"}[ftp://*path*]{lang="EN-US"}]{#struct_0_86480_74578_x1199316829}[，例如]{lang="EN-US" style="font-family:
宋体"}[ftp://1.1.1.1/lbill]{lang="EN-US"}[。]{lang="EN-US" style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_584396344}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_583937591}[配置本地缓存话单的上传]{style="font-family:宋体"}[URL]{lang="EN-US"}[为]{style="font-family:宋体"}[tftp://10.10.10.10/tftp]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_583872055}

[\[Sysname\] local-bill export-url tftp://10.10.10.10/tftp]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_583806519}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill enable]{lang="EN-US"}**]{#struct_0_86480_74578_583740983}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_583675447}
:::

::: {#637162196 .myid}
[]{#_Toc404792651}[]{#struct_0_86480_74578_583609911}[]{#_Toc362533105}

**AAA \-- 本地话单缓存配置命令 \-- snmp-agent trap enable local-bill**

------------------------------------------------------------------------

[**[snmp-agent trap enable local-bill]{lang="EN-US"}**]{#struct_0_86480_74578_583544375}[命令用来开启本地话单缓存告警功能。]{style="font-family:宋体"}

[**[undo snmp-agent trap enable local-bill]{lang="EN-US"}**]{#struct_0_86480_74578_583478839}[用来关闭本地话单缓存告警功能。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_584461879}

[**[snmp-agent  trap enable local-bill ]{lang="EN-US"}**]{#struct_0_86480_74578_584396343}

[**[undo snmp-agent trap enable local-bill]{lang="EN-US"}**]{#struct_0_86480_74578_583937590}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_583872054}

[[本地话单缓存告警功能处于开启状态。]{style="font-family:宋体"}]{#struct_0_86480_74578_583806518}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_583740982}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_583675446}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_583609910}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_583544374}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_583478838}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_584461878}

[[使能本地话单上传缓存告警功能后，当系统定时自动上传或超过阈值时自动上传本地缓存的话单到服务器失败时，会发送表示本地话单上传失败的告警信息。]{style="font-family:宋体"}]{#struct_0_86480_74578_584396342}

[[发送告警信息的最小时间间隔为]{style="font-family:宋体"}[10]{lang="EN-US"}]{#struct_0_86480_74578_583937597}[秒。当出现上传话单失败而需要发送告警信息时，如果距离上次上传失败发送告警信息间隔不足]{style="font-family:宋体"}[10]{lang="EN-US"}[秒，则本次不会发送告警信息。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_583872061}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_583806525}[使能本地话单缓存告警功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_583740989}

[\[Sysname\] snmp-agent trap enable local-bill]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_583675453}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-url]{lang="EN-US"}**]{#struct_0_86480_74578_583609917}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[local-bill export-interval]{lang="EN-US"}**]{#struct_0_86480_74578_583544381}
:::

::::: {#-628492702 .myid}
[]{#_Toc404792653}[]{#struct_0_86480_74578_417920664}

**AAA \-- ITA业务策略配置命令 \-- accounting-level**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 3 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_695131116}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_491950676}
:::

[ ]{lang="EN-US"}

[**[accounting-level]{lang="EN-US"}**]{#struct_0_86480_74578_1674566017}[命令用来指定需要进行计费的流量计费级别。]{style="font-family:宋体"}

[**[undo accounting-level]{lang="EN-US"}**]{#struct_0_86480_74578_x774639612}[命令用来删除需要进行计费的计费级别。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_1390733646}

[**[accounting-level ]{lang="EN-US"}***[level]{lang="EN-US"}***[ ]{lang="EN-US"}**[{ **ipv4** \| **ipv6** }]{lang="EN-US"}]{#struct_0_86480_74578_x2089289089}

[**[undo accounting-level ]{lang="EN-US"}**[\[ *level* \]]{lang="EN-US"}]{#struct_0_86480_74578_1862649181}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x219471019}

[[未指定需要计费的流量计费级别。]{style="font-family:宋体"}]{#struct_0_86480_74578_65494529}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_417855128}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x2022003836}[业务策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1631537997}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x693714475}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1565591372}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_840702748}

[**[accounting-level ]{lang="EN-US"}***[level]{lang="EN-US"}*]{#struct_0_86480_74578_x418997428}[：流量计费级别，取值范围为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[8]{lang="EN-US"}[。]{style="font-family:
宋体"}

[**[ipv4]{lang="EN-US"}**]{#struct_0_86480_74578_x475117669}[：指定该级别的流量按照]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量进行计费。]{style="font-family:宋体"}

[**[Ipv6]{lang="EN-US"}**]{#struct_0_86480_74578_x1445312259}[：指定该级别的流量按照]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量进行计费。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x288638372}

[[流量计费级别是指运营商对用户访问不同目的的流量收取不同等级的费用，例如在校园网环境中，用户访问校园网或教育网内资源只需交纳一定的费用（通常较低）；如果访问]{style="font-family:宋体"}[Internet]{lang="EN-US"}]{#struct_0_86480_74578_574988373}[则需要交纳相对较高的费用。]{style="font-family:宋体"}

[[可以通过多次执行本命令为]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_417789592}[业务策略指定多个需要计费的流量计费级别。]{style="font-family:宋体"}

[[执行]{style="font-family:宋体"}**[undo accounting-level]{lang="EN-US"}**]{#struct_0_86480_74578_53902443}[命令时，如果不指定级别，则表示删除本]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略内所有的流量计费级别。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1408165158}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x235851400}[在]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[中，指定需要计费的流量计费级别为]{style="font-family:宋体"}[2]{lang="EN-US"}[和]{style="font-family:宋体"}[5]{lang="EN-US"}[，其中]{style="font-family:
宋体"}[2]{lang="EN-US"}[级作为]{style="font-family:宋体"}[IPv4]{lang="EN-US"}[流量计费，]{style="font-family:宋体"}[5]{lang="EN-US"}[级作为]{style="font-family:宋体"}[IPv6]{lang="EN-US"}[流量计费。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x321884548}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] accounting-level 2 ipv4]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] accounting-level 5 ipv6]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1547030676}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_x1474750488}
:::::

::::: {#192263011 .myid}
[]{#_Toc404792654}[]{#struct_0_86480_74578_1061610565}

**AAA \-- ITA业务策略配置命令 \-- accounting-merge enable**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 5 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_580998020}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_417724056}
:::

[ ]{lang="EN-US"}

[**[accounting-merge enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1826021300}[命令用来开启统一计费功能。]{style="font-family:宋体"}

[**[undo accounting-merge enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1615983228}[命令用来关闭统一计费功能。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1130811500}

[**[accounting-merge enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1138047734}

[**[undo accounting-merge enable]{lang="EN-US"}**]{#struct_0_86480_74578_1676319239}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1877416883}

[[统一计费功能处于关闭状态。]{style="font-family:宋体"}]{#struct_0_86480_74578_x1571295187}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1769971263}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x1177907462}[业务策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1271975246}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_417658520}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_463699448}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x727896998}

[[开启]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x1840113490}[业务策略的统一计费功能后，系统会将策略下所有级别的流量进行合并，并以该策略中配置的最低的流量计费级别上报给计费服务器。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x86704754}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x496152423}[在]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[中使能统一计费功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x855688086}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] accounting-merge enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1912432725}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_x638958515}
:::::

::::: {#-285178587 .myid}
[]{#_Toc404792655}[]{#struct_0_86480_74578_x908425266}

**AAA \-- ITA业务策略配置命令 \-- accounting-method**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_418641560}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_208579066}
:::

[ ]{lang="EN-US"}

[**[accounting-method]{lang="EN-US"}**]{#struct_0_86480_74578_162097880}[命令用来指定]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略采用的计费方案。]{style="font-family:宋体"}

[**[undo accounting-method]{lang="EN-US"}**]{#struct_0_86480_74578_1877858192}[命令用来恢复]{style="font-family:宋体"}[ITA]{lang="EN-US"}[缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x702705874}

[**[accounting-method ]{lang="EN-US"}**[{ **none** \| **radius-scheme** *radius-scheme-name* \[ **none** \] }]{lang="EN-US"}]{#struct_0_86480_74578_x1685768052}

[**[undo accounting]{lang="EN-US"}**]{#struct_0_86480_74578_x50618930}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1253313105}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x834156701}[业务策略使用的计费方案为]{style="font-family:宋体"}**[none]{lang="EN-US"}**[。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1231816486}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_418576024}[业务策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x801545512}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x1616496565}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_2041076748}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_2039970743}

[**[none]{lang="EN-US"}**]{#struct_0_86480_74578_x74447027}[：不计费。]{style="font-family:宋体"}

[**[radius-scheme]{lang="EN-US"}***[ radius-scheme-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1613164204}[：指定]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案。其中，]{style="font-family:宋体"}*[radius-scheme-name]{lang="EN-US"}*[表示]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[方案名，为]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[32]{lang="EN-US"}[个字符的字符串，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x471300412}

[[可以对]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x354745825}[业务流量采用独立的计费方案，与对非]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量采用的计费方案不同。]{style="font-family:宋体"}

[[可以指定备选计费方法，在当前的计费方法无效时尝试使用备选的方法完成计费。例如，]{style="font-family:宋体"}**[radius-scheme]{lang="EN-US"}**[ *radius-scheme-name* **none**]{lang="EN-US"}]{#struct_0_86480_74578_x1903514713}[表示，先进行]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费，若]{style="font-family:宋体"}[RADIUS]{lang="EN-US"}[计费无效则不进行计费。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1389466788}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_1984201218}[在]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[中指定采用的计费方案为]{style="font-family:宋体"}[radius1]{lang="EN-US"}[。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_882109518}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] accounting radius-scheme radius1]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1461063776}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[radius scheme]{lang="EN-US"}**]{#struct_0_86480_74578_917444346}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_x575879484}
:::::

::::: {#439061297 .myid}
[]{#_Toc404792656}[]{#struct_0_86480_74578_x1577719401}[]{#_Toc383010753}

**AAA \-- ITA业务策略配置命令 \-- ita policy**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 1 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_x1999713100}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{lang="EN-US" style="font-family:
KaiTi_GB2312"}]{#struct_0_86480_74578_x1383729279}
:::

[ ]{lang="EN-US"}

[**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_x1150249666}[命令用来创建]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[**[undo ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_1984135682}[命令用来删除指定的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x316883374}

[**[ita policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_86480_74578_21591373}

[**[undo ita policy ]{lang="EN-US"}***[policy-name]{lang="EN-US"}*]{#struct_0_86480_74578_x1908087627}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x891052167}

[[无]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_1088896009}[业务策略。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_259284896}

[[系统视图]{style="font-family:宋体"}]{#struct_0_86480_74578_x751131163}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x443318936}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_437761480}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_701035318}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1984070146}

[*[policy-name]{lang="EN-US"}*]{#struct_0_86480_74578_873101174}[：]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略名称，由]{style="font-family:宋体"}[1]{lang="EN-US"}[～]{style="font-family:宋体"}[31]{lang="EN-US"}[个字符组成，不区分大小写。]{style="font-family:宋体"}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_x538002932}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_2118044391}[业务策略用来配置智能靶向计费功能相关控制参数，包括选用的计费方案、需要进行计费的流量计费级别、用户流量配额耗尽后采用的接入策略等。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_1928514313}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_492134610}[创建一个名称为]{style="font-family:宋体"}[ita1]{lang="EN-US"}[的]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_1029911944}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] ]{lang="EN-US"}
:::::

::::: {#-1806179340 .myid}
[]{#_Toc404792657}[]{#struct_0_86480_74578_x1020025000}

**AAA \-- ITA业务策略配置命令 \-- traffic-quota-out**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 7 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_549817785}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_100318242}
:::

[ ]{lang="EN-US"}

[**[traffic-quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_1984004610}[命令用来配置流量配额耗尽策略。]{style="font-family:宋体"}

[**[undo traffic-quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_1242974685}[命令用来恢复缺省情况。]{style="font-family:宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_595947595}

[**[traffic-quota-out ]{lang="EN-US"}**[{ **offline** \| **online** }]{lang="EN-US"}]{#struct_0_86480_74578_1092799885}

[**[undo traffic-quota-out]{lang="EN-US"}**]{#struct_0_86480_74578_x1053475119}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_1874933772}

[[流量配额耗尽后用户不能访问授权的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}]{#struct_0_86480_74578_2099357822}[地址段。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_1155907622}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_528217003}[业务策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_2128504398}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_x5942003}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_1983939074}

[[【参数】]{style="font-family:黑体"}]{#struct_0_86480_74578_1430537745}

[**[offline]{lang="EN-US"}**]{#struct_0_86480_74578_1779087011}[：当用户的指定级别的流量配额耗尽后，用户不能访问授权的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[**[online]{lang="EN-US"}**]{#struct_0_86480_74578_x2059109362}[：当用户的指定级别的流量配额耗尽后，用户仍能访问授权的目的]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段]{style="font-family:宋体"}[。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1243665828}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x649248302}[在]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[中配置流量配额耗尽策略为流量耗尽后不能访问授权的目前]{style="font-family:宋体"}[IP]{lang="EN-US"}[地址段。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x944196221}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] traffic-quota-out offline]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_154621223}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_x1587782944}
:::::

::::: {#-1741503818 .myid}
[]{#_Toc404792658}[]{#struct_0_86480_74578_x1318285014}

**AAA \-- ITA业务策略配置命令 \-- traffic-seperate**

------------------------------------------------------------------------

::: {style="border:none;border-top:solid windowtext 1.0pt;padding:1.0pt 0cm 0cm 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[![说明](AAA命令.files/image001.png){#图片 9 width="62" height="25"}]{lang="EN-US"}]{#struct_0_86480_74578_1983873538}
:::

::: {style="border:none;border-bottom:solid windowtext 1.0pt;padding:0cm 0cm 1.0pt 0cm;
margin-left:31.2pt;margin-right:0cm"}
[[本命令的支持情况与设备的型号有关，请以设备的实际情况为准。]{style="font-family:KaiTi_GB2312"}]{#struct_0_86480_74578_x957349424}
:::

[ ]{lang="EN-US"}

[**[traffic-separate enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1077271961}[命令用来开启]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量与用户总计费流量分离功能。]{style="font-family:宋体"}

[**[undo traffic-separate enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1268654736}[命令用来恢复缺省情况。]{style="font-family:
宋体"}

[[【命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x362592258}

[**[traffic-separate enable]{lang="EN-US"}**]{#struct_0_86480_74578_45877856}

[**[undo traffic-separate enable]{lang="EN-US"}**]{#struct_0_86480_74578_x1504334306}

[[【缺省情况】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1435035704}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x865358572}[业务流量与用户总计费流量分离功能处于关闭状态。]{style="font-family:宋体"}

[[【视图】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1509786606}

[[ITA]{lang="EN-US"}]{#struct_0_86480_74578_1983808002}[业务策略视图]{style="font-family:宋体"}

[[【缺省用户角色】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1305095790}

[[network-admin]{lang="EN-US"}]{#struct_0_86480_74578_1236210789}

[[mdc-admin]{lang="EN-US"}]{#struct_0_86480_74578_324998485}

[[【使用指导】]{style="font-family:黑体"}]{#struct_0_86480_74578_115894214}

[[缺省情况下，设备上报给计费服务器的用户总计费流量为]{style="font-family:宋体"}[ITA]{lang="EN-US"}]{#struct_0_86480_74578_x1745405256}[业务流量和非]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量之和。开启]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量与用户总计费流量分离功能后，设备上报给计费服务器的用户总计费流量中将不包含]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量。]{style="font-family:宋体"}

[[【举例】]{style="font-family:黑体"}]{#struct_0_86480_74578_467200505}

[[\# ]{lang="EN-US"}]{#struct_0_86480_74578_x655327793}[在]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务策略]{style="font-family:宋体"}[ita1]{lang="EN-US"}[中开启]{style="font-family:宋体"}[ITA]{lang="EN-US"}[业务流量与用户总计费流量分离功能。]{style="font-family:宋体"}

[[\<Sysname\> system-view]{lang="EN-US"}]{#struct_0_86480_74578_x2024619519}

[\[Sysname\] ita policy ita1]{lang="EN-US"}

[\[Sysname-ita-policy-ita1\] traffic-separate enable]{lang="EN-US"}

[[【相关命令】]{style="font-family:黑体"}]{#struct_0_86480_74578_x1930434876}

[[·[              ]{style="font:7.0pt "}]{lang="EN-US" style="font-size:10.0pt;font-family:Symbol"}**[ita policy]{lang="EN-US"}**]{#struct_0_86480_74578_905957231}

[ ]{lang="EN-US"}
:::::
